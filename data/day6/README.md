# Dữ liệu Day 7 (từ Day 6)

Corpus: Luật Đầu tư số 143/2025/QH15 (`luat-dau-tu-143-2025-qh15`), văn bản quy phạm pháp luật công khai, 43 trang nội dung. Chunk và vector lấy từ index Day 6 (chiến lược B), xem [docs/day6_connection.md](../../docs/day6_connection.md).

| File | Nội dung | Ai được dùng |
|---|---|---|
| `chunks.json` | 118 chunk B: `id, text, source_id, source, page, metadata` (`page_end, chapter, chapter_title, section, article, strategy, doc_version, embedding_model`) | Retrieval (TF-IDF/BM25…), kiểm tra citation |
| `questions.json` | 21 câu có đáp án (16 dev, 5 test), có `gold` và `expected_answer` | **Chỉ dùng để chấm**, không đưa vào agent hay retrieval |
| `unanswerable.json` | 6 câu thiếu bằng chứng (3 dev, 3 test), có `absence_reason` và `absence_check` | Chấm abstention |
| `cases.json` | 27 câu: `id, split, question, answerable, expected_behavior`, và `filter` nếu người dùng cung cấp. Không có gold hay đáp án | Đầu vào agent, `agent_metrics.py --cases` |

Tạo lại:

```powershell
.venv\Scripts\python.exe scripts/export_day6.py       # DB Day 6 -> chunks.json
.venv\Scripts\python.exe scripts/build_benchmark.py   # benchmark Day 6 + unanswerable.json -> questions.json, cases.json
```

## Chuyển benchmark Day 6

- `gold_page: [p]` → `gold: [{source_id, page: p, evidence}]`; mọi câu Day 6 chỉ có một trang gold.
- `evidence` là đoạn nguyên văn trong chunk (giữ xuống dòng của PDF), cùng chữ với `evidence_quote` Day 6; bản gốc giữ ở `evidence_quote_day6`.
- `filter` (`chapter`) giữ nguyên cho q08, q09, q16, t01: đây là phạm vi chương người dùng cho biết trước trong câu hỏi, không suy ra từ gold.

## Quy tắc khớp evidence

Dùng [src/evidence.py](../../src/evidence.py), giống cách chấm Day 6: cùng `source_id`, trang gold nằm trong `[page, metadata.page_end]` của chunk, và evidence (đã chuẩn hóa khoảng trắng) nằm trọn trong chunk.

`hit()` trong `starter/baseline.py` yêu cầu `chunk.page == gold.page`. Với 4 câu q05, t02, t03, t04, chunk bắt đầu ở trang trước và evidence nằm ở trang sau (`page_end`), nên `hit()` của starter chấm sai thành miss. Sau khi chuyển, 21/21 gold khớp với quy tắc trên; quy tắc của starter chỉ nhận 17/21.

## Câu thiếu bằng chứng

Gần chủ đề (lệ phí, phạt tiền, thuế suất, thời hạn xử lý hồ sơ, mức ký quỹ, tiền lương), được kiểm tra bằng tìm kiếm toàn văn 43 trang, không chỉ dựa vào top-k. Từ khóa và kết quả ghi trong `absence_check`. Dense top-3 của các câu này rơi vào đúng điều liên quan (Điều 14, 26, 27, 30, 31…) nhưng không chứa con số được hỏi, nên chúng kiểm tra việc agent có từ chối thay vì bịa hay không.

Giới hạn: một văn bản duy nhất; dev và test cùng văn phong. Điều 40 (test) dẫn chiếu Điều 6 (dev). Test Day 6 đã chạy ở Day 6 nhưng không dùng để chỉnh; ở Day 7 chỉ chỉnh trên dev.
