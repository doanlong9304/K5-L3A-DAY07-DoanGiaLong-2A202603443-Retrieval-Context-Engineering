# Nhật ký thử nghiệm Day 7

Mọi cấu hình chạy trên **dev** (16 câu có đáp án + 3 câu thiếu evidence), cùng corpus (Day 6 chiến lược B, 118 chunk), cùng agent model `claude-opus-5-5` (effort `medium`), `max_searches=3`, `top_k=3`, budget 3000 ký tự, trừ tham số được thay đổi. Test chỉ chạy sau khi đã chốt cấu hình.

## Tiêu chí chọn cấu hình (ghi trước khi chạy cấu hình cải thiện, 2026-11-14)

Xếp theo thứ tự ưu tiên; chỉ dùng tiêu chí sau khi các tiêu chí trước bằng nhau:

1. Grounded answer trung bình trên dev (nhãn 0–2 đã duyệt).
2. Không làm giảm abstention đúng trên câu thiếu evidence (3/3), và ít từ chối nhầm câu có đáp án hơn.
3. Context Evidence Rate của agent (evidence gold có trong context cuối).
4. Chi phí LLM (USD) rồi thời gian trung vị mỗi câu.

Chênh lệch 1 câu trên 16 câu (6 điểm %) được coi là có thể do ngẫu nhiên: model không cho đặt temperature, nên hai lần chạy cùng cấu hình có thể khác nhau. Khi chênh lệch chỉ 1 câu, ưu tiên cấu hình đơn giản hơn và rẻ hơn.

## Baseline — `baseline-dense`

- Retriever dense (pgvector Day 6), ghép context theo starter: giữ chunk của lượt search **đầu tiên** trước, chunk mới chỉ vào nếu còn budget.
- Kết quả dev: grounded 1,875/2 (15×2, 1×0), citation 33/33, abstention 3/3, từ chối nhầm 1/16 (q13), Context Evidence 15/16, $0,78, trung vị 11,0 s/câu.
- Lỗi 1 (q13): lượt search 3 lấy được Điều 29 chứa evidence ở hạng 1, nhưng context đã đầy với chunk của lượt 1 (Điều 25, 33) nên chunk đúng không vào context → model từ chối.
- Quan sát 2: câu trả lời dài, thêm 3–5 ý phụ (đều có nguồn), làm tăng output token.

## Cấu hình 1 — `ctx-recent-dense`: ưu tiên chunk của lượt search mới nhất

- **Thay đổi duy nhất:** khi ghép context, xếp kết quả của lượt search mới nhất lên trước, sau đó mới đến các lượt cũ (trong mỗi lượt giữ thứ hạng retriever), rồi cắt theo budget.
- **Giả thuyết:** model chỉ tìm thêm khi context chưa đủ, nên kết quả của truy vấn mới (đã được viết lại) thường liên quan hơn. Ưu tiên chúng sẽ sửa q13 mà không làm hỏng các câu chỉ cần 1 lượt search (13/16 câu, không bị ảnh hưởng vì chỉ có một lượt).
- **Rủi ro:** câu cần evidence từ nhiều lượt có thể mất chunk của lượt đầu.
- **Kết quả dev** (nhãn đã duyệt): grounded **2,000/2** (16×2), citation 36/36, abstention 3/3, từ chối nhầm **0/16**, Context Evidence **16/16**, $0,79, trung vị 9,4 s/câu. Phân bố số lượt search giống hệt baseline (13 câu 1 lượt, 1 câu 2 lượt, 5 câu 3 lượt).
- **Đo lại lỗi q13:** lượt 3 lấy Điều 29 → nay được đưa lên đầu context → agent trả lời đúng "trước khi nhà đầu tư thực hiện dự án đầu tư" [Điều 29 k1], điểm 2.
- **Rủi ro có xảy ra không:** 5 câu dùng 3 lượt search (q09, q13, q16, u01, u02) vẫn đúng; không câu nào mất evidence của lượt đầu trên dev. Rủi ro vẫn còn với câu cần ghép evidence từ nhiều lượt (dev chưa có loại câu này).
- **Đánh giá:** chênh 1 câu (q13) nằm trong ngưỡng có thể do ngẫu nhiên theo tiêu chí, nhưng cơ chế được xác nhận: cùng truy vấn lượt 3 tìm ra evidence ở cả hai lần chạy; khác biệt chỉ ở bước ghép context (test `tests/test_agent_context.py` tái hiện tình huống không cần API). Chi phí gần như không đổi. → Giữ `recent` cho các cấu hình sau.

## Cấu hình 2 — `hybrid-recent`: retriever hybrid RRF + context `recent`

- **Thay đổi so với cấu hình 1:** retriever của tool `search` đổi từ dense sang hybrid RRF (dense + BM25-bigram, k = 60, 20 candidate mỗi bên); giữ context `recent`, top-3, budget 3000 ký tự.
- **Giả thuyết:** ở bước đánh giá retrieval (dev), hybrid đưa evidence lên hạng 1 ở 16/16 câu so với 12/16 của dense, nên agent sẽ thấy evidence ngay lượt đầu nhiều hơn → **ít lượt search hơn, ít token hơn, rẻ và nhanh hơn**, chất lượng câu trả lời giữ nguyên.
- **Rủi ro:** RRF phạt chunk chỉ một phía tìm thấy (trường hợp q16 không filter); BM25 có thể kéo lên chunk trùng từ nhưng sai ý với các truy vấn do agent tự viết lại.
- **Chi phí thêm của hybrid:** BM25 chạy cục bộ, không gọi API; embedding câu hỏi giống dense.
- **Kết quả dev** (nhãn đã duyệt): grounded 1,875/2 (15×2, 1×0), citation 32/32, abstention 3/3, từ chối nhầm 1/16 (q13), Context Evidence 15/16, 48 lần gọi LLM, $0,77, trung vị 9,1 s/câu. Số lượt search: 13 câu 1 lượt, 2 câu 2 lượt, 4 câu 3 lượt.
- **Giả thuyết không được xác nhận:** số câu chỉ cần 1 lượt search vẫn là 13/16 như dense, vì với dense các câu này đã có evidence trong top-3 ngay lượt đầu (Hit@1 của hybrid tốt hơn không làm giảm số lượt search). Tiết kiệm chỉ 1 lần gọi LLM, $0,02.
- **Lỗi q13 (kiểu mới):** lần chạy này agent viết truy vấn lượt 3 là "Điều 24 các dự án đầu tư sau đây phải được chấp thuận…" thay vì "…được thực hiện trước khi". Với cả 3 truy vấn, Điều 29 chỉ ở hạng 6–9 ở dense, BM25 lẫn hybrid → không vào top-3 → agent từ chối. Đây là lỗi do cách viết truy vấn và xếp hạng, không do ghép context; cho thấy q13 phụ thuộc vào truy vấn mà model tự viết (không ổn định giữa các lần chạy).

## Chốt cấu hình (trước khi chạy test)

| Cấu hình | Grounded /2 | Từ chối đúng | Từ chối nhầm | Context Evidence | Chi phí | Trung vị |
|---|---|---|---|---|---|---|
| baseline-dense | 1,875 | 3/3 | 1/16 | 15/16 | $0,78 | 11,0 s |
| **ctx-recent-dense** | **2,000** | 3/3 | **0/16** | **16/16** | $0,79 | 9,4 s |
| hybrid-recent | 1,875 | 3/3 | 1/16 | 15/16 | $0,77 | 9,1 s |

Áp dụng tiêu chí theo thứ tự: (1) grounded cao nhất là `ctx-recent-dense`; (2) abstention bằng nhau, từ chối nhầm thấp nhất cũng là `ctx-recent-dense`; (3) Context Evidence cao nhất; (4) chi phí chênh ≤ $0,02, không đổi thứ tự. **Chọn `ctx-recent-dense`** (dense pgvector Day 6 + ghép context ưu tiên lượt search mới nhất). Lưu ý: hơn baseline/hybrid đúng 1 câu (q13), trong ngưỡng có thể do ngẫu nhiên; lựa chọn dựa thêm vào việc cơ chế sửa lỗi được xác nhận bằng trace và unit test, và cấu hình này đơn giản hơn hybrid.

Test sẽ chạy **baseline-dense** và **ctx-recent-dense** trên cùng 8 câu test (5 có đáp án, 3 thiếu evidence), không chỉnh gì thêm sau khi xem kết quả test.

## Kết quả test (chạy 2026-11-14, sau khi đã chốt cấu hình; nhãn đã duyệt)

| Cấu hình | Grounded /2 | Từ chối đúng | Từ chối nhầm | Context Evidence | Citation hợp lệ | Chi phí | Trung vị |
|---|---|---|---|---|---|---|---|
| baseline-dense | 1,600 (4×2, 1×0) | 3/3 | 1/5 (t01) | 5/5 | 7/7 | $0,35 | 11,0 s |
| ctx-recent-dense | 1,600 (4×2, 1×0) | 3/3 | 1/5 (t01) | 5/5 | 7/7 | $0,34 | 10,6 s |

- Hai cấu hình **cho kết quả như nhau** trên test: cùng truy vấn lượt 1 ở mọi câu, cùng phân bố lượt search (4 câu 1 lượt, 2 câu 2 lượt, 2 câu 3 lượt), không câu nào có evidence bị đẩy ra khỏi context (`lost_in_context` rỗng). Test không có tình huống như q13 trên dev (evidence chỉ xuất hiện ở lượt search sau) nên chính sách `recent` không tạo khác biệt; ưu điểm của nó trên dev chưa được xác nhận lại trên test.
- **Lỗi t01 (cả hai cấu hình):** câu hỏi "Những ngành, nghề nào bị cấm đầu tư?" có filter chương V (đầu tư ra nước ngoài). Evidence gold (Điều 40) đã ở hạng 1 ngay lượt đầu và nằm trong context, nhưng model hiểu câu hỏi là Điều 6 (cấm đầu tư kinh doanh nói chung), tìm thêm 2 lượt rồi từ chối. Trong lý do từ chối, model vẫn nêu đúng 3 ý của Điều 40. Đây là lỗi diễn giải câu hỏi mơ hồ, không do retrieval hay ghép context. Theo quy tắc, không chỉnh gì sau khi xem test.
- Kết luận giữ nguyên: chọn `ctx-recent-dense` dựa trên dev; trên test nó ngang baseline về chất lượng và rẻ hơn không đáng kể.
