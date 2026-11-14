# So sánh cấu hình agent — dev

| Run | Retriever | Context | Grounded (TB /2) | 2 / 1 / 0 | Citation hợp lệ | Từ chối đúng | Từ chối nhầm | Context Evidence | Search/câu | LLM calls | Token vào / ra | Chi phí | Trung vị s/câu | Nhãn |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| baseline-dense | dense | first | 1.875 | 15 / 0 / 1 | 33/33 | 3/3 | 1/16 | 15/16 (94%) | 1:13, 2:1, 3:5 | 49 | 113,752 / 16,372 | $0.78 | 10.96 | đã duyệt |
| ctx-recent-dense | dense | recent | 2.000 | 16 / 0 / 0 | 36/36 | 3/3 | 0/16 | 16/16 (100%) | 1:13, 2:1, 3:5 | 49 | 115,271 / 16,250 | $0.79 | 9.39 | đã duyệt |
| hybrid-recent | hybrid | recent | 1.875 | 15 / 0 / 1 | 32/32 | 3/3 | 1/16 | 15/16 (94%) | 1:13, 2:2, 3:4 | 48 | 110,577 / 16,442 | $0.77 | 9.07 | đã duyệt |

Search/câu: số lượt search → số câu. Chi phí theo giá niêm yết claude-opus-5-5 ($4 / $20 mỗi 1M token).
