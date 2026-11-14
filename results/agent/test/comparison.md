# So sánh cấu hình agent — test

| Run | Retriever | Context | Grounded (TB /2) | 2 / 1 / 0 | Citation hợp lệ | Từ chối đúng | Từ chối nhầm | Context Evidence | Search/câu | LLM calls | Token vào / ra | Chi phí | Trung vị s/câu | Nhãn |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| baseline-dense | dense | first | 1.600 | 4 / 0 / 1 | 7/7 | 3/3 | 1/5 | 5/5 (100%) | 1:4, 2:2, 3:2 | 22 | 54,156 / 6,560 | $0.35 | 10.95 | đã duyệt |
| ctx-recent-dense | dense | recent | 1.600 | 4 / 0 / 1 | 7/7 | 3/3 | 1/5 | 5/5 (100%) | 1:4, 2:2, 3:2 | 22 | 54,317 / 6,316 | $0.34 | 10.59 | đã duyệt |

Search/câu: số lượt search → số câu. Chi phí theo giá niêm yết claude-opus-5-5 ($4 / $20 mỗi 1M token).
