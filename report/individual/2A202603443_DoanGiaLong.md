# Báo cáo Day 7 — Đoàn Gia Long (2A202603443)

## Dữ liệu và benchmark

- **Nguồn, quyền sử dụng, số trang và số chunk:** Luật Đầu tư số 143/2025/QH15 (`luat-dau-tu-143-2025-qh15`). Đây là văn bản quy phạm pháp luật công khai, được phép chia sẻ. Tài liệu có 43 trang nội dung, `doc_version` = sha256 của PDF (`567993cf…`). Day 7 dùng lại index Day 6, chiến lược **B** (chia theo Điều/khoản, tối đa 1200 ký tự): **118 chunk**, ID dạng `B-<hash>`, metadata gồm `page`, `page_end`, `chapter`, `section`, `article`. Chi tiết ở [docs/day6_connection.md](../../docs/day6_connection.md) và [data/day6/README.md](../../data/day6/README.md).
- **Vector store, embedding model, phiên bản và số chiều:** PostgreSQL 16 + pgvector 0.8.7, bảng `lab_chunks`, đo bằng cosine (`<=>`, score = 1 − distance), tìm chính xác (không dùng ANN). Embedding dùng `gemini-embedding-001` với **768 chiều**: tài liệu ở chế độ `RETRIEVAL_DOCUMENT`, câu hỏi ở chế độ `RETRIEVAL_QUERY`, cùng model và số chiều với index Day 6. Kết nối chỉ đọc (`default_transaction_read_only=on`). Cấu hình ở [configs/day6_index.json](../../configs/day6_index.json).
- **Agent model, cách chạy và phân chia dev/test:** agent dùng `claude-opus-5-5` qua Anthropic API (effort `medium`). Model API này không cho đặt temperature. Lệnh chạy ở [docs/RUN.md](../../docs/RUN.md). Dev có **16 câu có đáp án và 3 câu thiếu evidence**; test có **5 câu có đáp án và 3 câu thiếu evidence**, tổng 27 câu.
- **Cách xác định câu có/thiếu evidence và tiêu chí chấm:**
  - *Câu có đáp án:* chuyển từ benchmark Day 6 ([scripts/build_benchmark.py](../../scripts/build_benchmark.py)). Gold gồm `source_id`, `page` và `evidence` là đoạn nguyên văn trong chunk.
  - *Quy tắc khớp ([src/evidence.py](../../src/evidence.py)):* chunk khớp nếu cùng nguồn, trang gold nằm trong khoảng `[page, page_end]` của chunk, và chunk chứa trọn evidence. 21/21 gold khớp quy tắc này. `hit()` của starter yêu cầu `page == gold.page` nên chỉ nhận 17/21.
  - *Câu thiếu evidence* (`unanswerable.json`) là câu gần chủ đề. Mỗi câu ghi `absence_reason` và `absence_check` (đã tìm từ khóa trên toàn văn bản), không kết luận chỉ dựa vào top-k.
  - *Filter `chapter`:* chỉ có ở q08, q09, q16, t01, khi người dùng nêu phạm vi chương ngay trong câu hỏi.
  - *Gold* chỉ được đọc khi chấm, sau khi retrieval/agent đã chạy. `cases.json` (đầu vào của agent) không chứa gold hay đáp án.

## Retrieval và thử nghiệm

Bốn phương pháp chạy trên cùng corpus, index, câu hỏi và nhãn ([src/lexical.py](../../src/lexical.py), [src/hybrid.py](../../src/hybrid.py), [src/day6_index.py](../../src/day6_index.py)):
- **dense:** pgvector Day 6.
- **BM25 âm tiết:** tách theo khoảng trắng.
- **BM25-bigram:** dùng âm tiết và cặp âm tiết liền kề, để giữ từ ghép tiếng Việt như "nhà đầu tư" hay "ký quỹ".
- **hybrid RRF:** gộp dense và BM25-bigram, k = 60, 20 candidate mỗi bên. Chỉ hợp nhất theo hạng nên không phải chuẩn hóa score.

Mỗi phương pháp xuất top-10. Hit@1 và Evidence Hit@3 chấm cùng quy tắc trên. Context lấy top-3, ghép tối đa 3000 ký tự (tính cả dòng header nguồn).

**Bảng retrieval (một lượt tìm, câu hỏi gốc, có filter của người dùng).** Nguồn: [results/retrieval/dev/comparison.md](../../results/retrieval/dev/comparison.md) và [results/retrieval/test/comparison.md](../../results/retrieval/test/comparison.md).

| Cấu hình | Phương pháp, top-k, filter, rerank, context budget | Giả thuyết / thay đổi | Split | Hit@1 | Evidence Hit@3 | Context Evidence Rate | Thời gian / chi phí |
|---|---|---|---|---|---|---|---|
| Baseline | dense pgvector, top-3, filter chương nếu có, không rerank, 3000 ký tự | Vector store Day 6 nguyên trạng | dev | 12/16 (75%) | 16/16 (100%) | 16/16 (100%) | ~360 ms/câu (gọi embedding Gemini lần đầu); 1 lần gọi embedding/câu, ~$0 |
| Phương pháp 2 | BM25 âm tiết, top-3, filter, 3000 ký tự | Luật dùng nhiều thuật ngữ cố định → khớp từ khóa có lợi | dev | 13/16 (81%) | 15/16 (94%) | 15/16 (94%) | 0,5 ms/câu, chạy cục bộ, $0 |
| Phương pháp 3 | BM25-bigram, top-3, filter, 3000 ký tự | Tách âm tiết làm vỡ từ ghép → thêm bigram | dev | 16/16 (100%) | 16/16 (100%) | 16/16 (100%) | 0,8 ms/câu, $0 |
| Phương pháp 4 | Hybrid RRF (dense + BM25-bigram), top-3, filter, 3000 ký tự | Hai tín hiệu bù nhau, đưa evidence lên hạng 1 | dev | 16/16 (100%) | 16/16 (100%) | 16/16 (100%) | ~360 ms/câu (embedding) + 5 ms, ~$0 |
| Cải thiện 1 (agent) | Agent + dense, context `recent` (xem bảng agent) | Ưu tiên chunk của lượt search mới nhất | dev | — | — | 16/16 (100%) | $0,79; trung vị 9,4 s/câu |
| Cải thiện 2 (agent) | Agent + hybrid RRF, context `recent` | Hit@1 tốt hơn → ít lượt search, rẻ hơn | dev | — | — | 15/16 (94%) | $0,77; trung vị 9,1 s/câu |
| Cấu hình đã chọn | Agent `ctx-recent-dense`; retrieval một lượt = dense | Chốt trên dev trước khi chạy test | test | 5/5 (100%) | 5/5 (100%) | agent 5/5 (100%) | $0,34; trung vị 10,6 s/câu |
| Baseline | Agent `baseline-dense` (context `first`); retrieval một lượt = dense | — | test | 5/5 (100%) | 5/5 (100%) | agent 5/5 (100%) | $0,35; trung vị 11,0 s/câu |

**Ghi chú cho bảng:**
- Bỏ filter (`--no-filter`), dev cho dense 11/16 · 15/16, BM25 10/16 · 14/16, BM25-bigram 15/16 · 16/16, hybrid 14/16 · 15/16. Filter của người dùng giúp mọi phương pháp.
- Trên test, BM25, BM25-bigram và hybrid cũng đạt 5/5 · 5/5 · 5/5. Bộ test nhỏ và dễ nên không phân biệt được các phương pháp.
- Hybrid là phương pháp retrieval mới. Khi gắn vào agent, nó cũng là "cải thiện 2"; cả hai được mô tả và đo riêng.

**Hai lỗi dev, nguyên nhân và cách thử:**

1. **q04 với BM25 âm tiết (lỗi retrieval).** Câu hỏi: "…điều kiện gì để được chuyển vốn đầu tư ra nước ngoài?"
   - *Kết quả:* chunk gold (trang 9, Điều 11) không có trong top-6. Top-1 là Điều 7 (trang 5) vì trùng nhiều âm tiết rời như "đầu", "tư", "nước", "ngoài".
   - *Giả thuyết:* tách âm tiết làm mất nghĩa của từ ghép.
   - *Thử:* thêm bigram âm tiết (BM25-bigram). Gold lên **hạng 1**, và Hit@1 dev tăng từ 13/16 lên 16/16.
2. **q13 với agent baseline (lỗi ghép context).** Câu hỏi: "chấp thuận chủ trương đầu tư phải thực hiện vào thời điểm nào?"
   - *Kết quả:* lượt search 3 lấy được Điều 29 (chứa evidence) ở hạng 1. Nhưng chính sách `first` giữ chunk của lượt 1 (Điều 25, 33) trước, context đầy 3000 ký tự, nên Điều 29 bị loại. Model từ chối, và câu có đáp án bị chấm 0.
   - *Giả thuyết:* model chỉ tìm thêm khi context chưa đủ, nên kết quả của truy vấn mới thường liên quan hơn.
   - *Thử:* chính sách `recent`. q13 được trả lời đúng, điểm 2. Lỗi được tái hiện bằng test không gọi API: [tests/test_agent_context.py](../../tests/test_agent_context.py).
3. **Thêm: q16 khi bỏ filter.**
   - *Kết quả:* dense không tìm ra gold (trang 29, Điều 38) trong top-10. Hybrid kéo gold lên hạng 5, vì RRF phạt chunk mà chỉ một retriever tìm thấy. Có filter chương thì dense xếp gold ở hạng 2.
   - *Kết luận:* filter do người dùng cung cấp là thông tin quan trọng, nên giữ lại.

**Lý do chọn cấu hình.** Tiêu chí được ghi trong [docs/experiments.md](../../docs/experiments.md) *trước* khi chạy cải thiện, xét theo thứ tự:
1. Grounded trung bình trên dev.
2. Abstention đúng, và ít từ chối nhầm.
3. Context Evidence Rate.
4. Chi phí, rồi thời gian.

`ctx-recent-dense` đứng đầu ở (1)–(3): grounded 2,000, 0/16 từ chối nhầm, Context Evidence 16/16. Chi phí chênh không quá $0,02. Hơn baseline đúng 1 câu là trong ngưỡng có thể do ngẫu nhiên, nên lựa chọn còn dựa trên cơ chế đã được xác nhận bằng trace và unit test, và cấu hình này đơn giản hơn hybrid. Test chỉ chạy sau khi đã chốt.

## Agent và đánh giá

- **Tool, số lượt gọi, điều kiện dừng, cách chọn context và xử lý lỗi** ([src/agent.py](../../src/agent.py), [src/context.py](../../src/context.py)):
  - *Tool và quy tắc mỗi lượt:* mỗi lượt model gọi đúng một trong 3 tool: `search(query)`, `answer(answer, citations)`, `abstain(reason)`. Model chỉ viết truy vấn. Retriever và filter của người dùng do harness cố định, nên gold không bao giờ vào agent.
  - *Giới hạn:* tối đa **3 lượt search** và 6 lượt model. Mỗi lượt lấy top-3.
  - *Điều kiện dừng:* `answer`, `abstain`, hết lượt search (chuyển thành abstain), hoặc hết lượt model.
  - *Ghép context:* context cộng dồn qua các lượt, bỏ chunk trùng ID và cắt theo **3000 ký tự**. Mỗi chunk kèm header `[id] (nguồn | trang | Điều)`. Chính sách `first` (starter) giữ chunk của lượt cũ trước. `recent` (đã chọn) xếp lượt mới nhất lên đầu và giữ thứ hạng trong từng lượt.
  - *Kiểm tra citation:* câu trả lời chỉ được nhận khi mọi citation là ID có trong context cuối và có xuất hiện dạng `[id]` trong câu trả lời; nếu không thì thành abstain. Bước này chỉ kiểm tra ID; nguồn có hỗ trợ ý hay không thì chấm tay.
  - *Xử lý lỗi:* lỗi API được thử lại tối đa 4 lần, sau đó ghi `status = error` (không tạo đầu ra giả). Trong tất cả các run có 0 lỗi provider và 0 lỗi vector store.
  - *An toàn:* system prompt yêu cầu coi nội dung tài liệu là dữ liệu, không phải chỉ dẫn.

**Bảng agent.** Nguồn: [results/agent/dev/comparison.md](../../results/agent/dev/comparison.md) và [results/agent/test/comparison.md](../../results/agent/test/comparison.md). Grounded tính trên câu có đáp án, nhãn chấm tay.

| Cấu hình / split | Tool use | Số lượt gọi | Grounded answer 0/1/2 và trung bình | Citation hợp lệ | Câu có citation | Abstention đúng | Từ chối nhầm |
|---|---|---|---|---|---|---|---|
| baseline-dense / dev | 19/19 | search 1:13, 2:1, 3:5; 49 lần gọi LLM | 1 / 0 / 15 → 1,875 | 33/33 | 15/15 | 3/3 | 1/16 (q13) |
| ctx-recent-dense / dev | 19/19 | 1:13, 2:1, 3:5; 49 lần gọi LLM | 0 / 0 / 16 → **2,000** | 36/36 | 16/16 | 3/3 | **0/16** |
| hybrid-recent / dev | 19/19 | 1:13, 2:2, 3:4; 48 lần gọi LLM | 1 / 0 / 15 → 1,875 | 32/32 | 15/15 | 3/3 | 1/16 (q13) |
| baseline-dense / test | 8/8 | 1:4, 2:2, 3:2; 22 lần gọi LLM | 1 / 0 / 4 → 1,600 | 7/7 | 4/4 | 3/3 | 1/5 (t01) |
| ctx-recent-dense / test | 8/8 | 1:4, 2:2, 3:2; 22 lần gọi LLM | 1 / 0 / 4 → 1,600 | 7/7 | 4/4 | 3/3 | 1/5 (t01) |

**Context Evidence của agent:** dev 15/16 · 16/16 · 15/16; test 5/5 · 5/5.

**Chấm context 0/1/2 trên test** (BENCHMARK mục 2, 5 câu có đáp án, nhãn đã duyệt): cả baseline và cấu hình đã chọn đều có **0 câu mức 0, 0 câu mức 1, 5 câu mức 2**. Hai cấu hình có context giống nhau ở t02–t05; ở t01 chỉ khác thứ tự chunk. Nhãn và lý do ở `results/agent/test/<run>/context_reviews.json`.

**Ví dụ minh họa** (trích từ trace, dùng cấu hình đã chọn trừ khi ghi khác):

| Query ID | Loại câu | Tool call và kết quả | Câu trả lời và citation | Nhãn, lý do |
|---|---|---|---|---|
| t04 (test) | Có đáp án, diễn đạt lại | 1 search → top-3 có Điều 48 [B-71df…] (gold trang 37) | "Định kỳ 06 tháng và hằng năm… gửi Bộ Tài chính, Ngân hàng Nhà nước Việt Nam và Cơ quan đại diện Việt Nam tại nước tiếp nhận đầu tư [B-71dfbbff0a0b5b66]", kèm các nghĩa vụ báo cáo khác [B-d5ba…] | Grounded 2; citation 2/2 hỗ trợ; context 2. Đúng và đủ, có thêm ý phụ nhưng đều có nguồn. |
| u05 (test) | Thiếu evidence | 2 search ("ký quỹ bảo đảm…", "tỷ lệ ký quỹ theo tổng vốn…") → Điều 30, Điều 52 | Từ chối: Điều 30 chỉ quy định ai phải ký quỹ và các trường hợp miễn; khoản 2 giao Chính phủ quy định chi tiết; không đưa ra con số % nào | Abstention đúng. Khớp `absence_check` (không có "mức/tỷ lệ ký quỹ" trong luật). |
| t01 (test) | **Lỗi**: có đáp án, filter chương V | Lượt 1 đưa Điều 40 [B-4679…] (gold) lên hạng 1 và vào context; model tìm thêm "Điều 6 …", "nghiêm cấm kinh doanh mại dâm…" | Từ chối. Trong lý do, model vẫn nêu đúng 3 ý của Điều 40, nhưng cho rằng câu hỏi hỏi về Điều 6 (cấm đầu tư kinh doanh nói chung) | Grounded 0 (từ chối câu có đáp án); context 2. Lỗi do model hiểu câu hỏi mơ hồ, không do retrieval/context. Xảy ra ở cả hai cấu hình. |
| q13 (dev, baseline) | **Lỗi**: có đáp án | Lượt 3 "…được thực hiện trước khi triển khai dự án" → Điều 29 [B-47d1…] hạng 1, nhưng context `first` giữ Điều 25, 33 của lượt 1 | Từ chối | Grounded 0. Lỗi ghép context; `recent` sửa được (điểm 2 ở `ctx-recent-dense`). |

- **Đường dẫn trace, nhãn, lệnh chạy, thời gian và chi phí:**
  - *Trace* từng câu (mọi tool call, tham số, kết quả có ID/score/trang/Điều, context cuối, câu trả lời, citation, token, thời gian, lỗi): `results/agent/<split>/<run>/traces.json`.
  - *Retrieval:* `results/retrieval/<split>/<run>/traces.json`.
  - *Nhãn:* `reviews.json` (câu trả lời, citation, abstention) và `context_reviews.json` (context test). File để đọc khi chấm: `review_sheet.md`.
  - *Lệnh chạy:* [docs/RUN.md](../../docs/RUN.md). Demo: [docs/demo_day7.html](../../docs/demo_day7.html).
  - *Chi phí* theo giá niêm yết `claude-opus-5-5` ($4 vào / $20 ra mỗi 1M token): dev ~$0,77–0,79 mỗi cấu hình (19 câu, ~110–115k token vào và ~16k token ra); test ~$0,34–0,35 mỗi cấu hình (8 câu). Embedding câu hỏi ~$0 (gemini-embedding-001, $0,15/1M token).
  - *Thời gian:* trung vị 9–11 s/câu.
- **Kết quả trước/sau, ví dụ lỗi, đánh đổi và giới hạn:**
  - *Trước/sau trên dev:* `first` → `recent` tăng grounded 1,875 → 2,000, giảm từ chối nhầm 1/16 → 0/16, chi phí không đổi ($0,78 → $0,79), trung vị giảm 11,0 → 9,4 s.
  - *Dense → hybrid trong agent:* không xác nhận giả thuyết "ít lượt search hơn". Số câu chỉ cần 1 lượt vẫn là 13/16, vì dense đã có evidence trong top-3 ngay lượt đầu; Hit@1 tốt hơn không giảm số lượt. Chỉ tiết kiệm 1 lần gọi LLM ($0,02).
  - *Hybrid lặp lại lỗi q13 theo kiểu mới:* model viết truy vấn khác ("Điều 24…"), nên Điều 29 chỉ ở hạng 6–9 ở cả 3 retriever. Kết quả q13 phụ thuộc vào truy vấn do model tự viết, không ổn định giữa các lần chạy.
  - *Trên test:* baseline và cấu hình đã chọn **ngang nhau** (1,600; cùng lỗi t01). Test không có câu nào mà evidence chỉ xuất hiện ở lượt search sau, nên lợi ích của `recent` chưa được xác nhận lại ngoài dev. Theo quy tắc, không chỉnh gì sau khi xem test.
  - *Đánh đổi:* dense cần 1 lần gọi embedding (~360 ms) mỗi truy vấn. BM25-bigram chạy cục bộ dưới 1 ms và đạt Hit@1 tốt hơn trên dev. Phần lớn chi phí và thời gian nằm ở LLM của agent (~10 s/câu), không ở retrieval.
  - *Giới hạn:*
    - Benchmark nhỏ (16 + 5 câu có đáp án, mỗi câu chỉ 1 trang gold). Chênh 1 câu bằng 6 điểm % trên dev và 20 điểm % trên test.
    - Không có câu cần ghép evidence từ nhiều lượt, nên rủi ro của `recent` (mất chunk lượt đầu) chưa được kiểm tra.
    - Model không cho đặt temperature, nên các lần chạy lặp lại có thể khác nhau; mỗi cấu hình chỉ chạy 1 lần.
    - Corpus chỉ có một văn bản luật.
    - Nhãn do một người chấm (tác giả) đọc và duyệt; chưa có người chấm thứ hai để đo độ đồng thuận.
    - Người chấm cần chạy lại ingest Day 6 (cần key Gemini) để có database.

## Thử thách nâng cao (nếu thực hiện)

Không thực hiện.
