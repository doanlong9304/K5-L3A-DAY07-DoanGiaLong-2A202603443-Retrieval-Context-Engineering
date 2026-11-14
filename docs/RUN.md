# Hướng dẫn chạy Day 7

Mọi lệnh chạy từ thư mục gốc repo, bằng Python của `.venv` (Python hệ thống không có `psycopg`, `google-genai`, `anthropic`). Ví dụ dưới đây dùng PowerShell trên Windows; trên Linux/macOS đổi `.venv\Scripts\python.exe` thành `.venv/bin/python`.

## 0. Cài đặt và kết nối Day 6

```powershell
py -3.12 -m venv .venv
.venv\Scripts\python.exe -m pip install -r requirements.txt
copy .env.example .env    # điền DATABASE_URL, GEMINI_API_KEY, ANTHROPIC_API_KEY, DAY6_STARTER_DIR
.venv\Scripts\python.exe scripts/check_day6.py --start          # bật container pgvector Day 6 và kiểm tra index (chỉ đọc)
.venv\Scripts\python.exe -m unittest discover -s tests -v       # 20 test, không gọi API
```

Chi tiết index, cổng và cách tái tạo khi không có database: [day6_connection.md](day6_connection.md).

## 1. Dữ liệu và benchmark (đã có sẵn trong `data/day6/`, chỉ chạy khi cần tạo lại)

```powershell
.venv\Scripts\python.exe scripts/export_day6.py       # DB Day 6 -> data/day6/chunks.json (118 chunk B)
.venv\Scripts\python.exe scripts/build_benchmark.py   # -> questions.json (gold, chỉ để chấm), cases.json (đầu vào agent)
```

## 2. Đánh giá retrieval (không gọi LLM; dense/hybrid gọi embedding câu hỏi, có cache)

```powershell
foreach ($m in "dense","bm25","bm25-bigram","hybrid") {
  .venv\Scripts\python.exe scripts/eval_retrieval.py --method $m --split dev
  .venv\Scripts\python.exe scripts/eval_retrieval.py --method $m --split dev --no-filter
}
.venv\Scripts\python.exe scripts/compare_retrieval.py --split dev    # -> results/retrieval/dev/comparison.md
```

Test: thay `--split dev` bằng `--split test` (chỉ chạy sau khi chốt cấu hình).

## 3. Agent trên dev (gọi API Anthropic; ~$0,8 và ~4 phút mỗi cấu hình 19 câu)

```powershell
.venv\Scripts\python.exe scripts/run_agent.py --split dev --retriever dense  --run baseline-dense   --context-policy first
.venv\Scripts\python.exe scripts/run_agent.py --split dev --retriever dense  --run ctx-recent-dense --context-policy recent
.venv\Scripts\python.exe scripts/run_agent.py --split dev --retriever hybrid --run hybrid-recent    --context-policy recent
```

Mặc định: `--model claude-opus-5-5 --max-searches 3 --top-k 3 --budget 3000`. Chạy thử vài câu: `--run smoke --ids q01,u01`. Bị ngắt giữa chừng: chạy lại cùng lệnh với `--resume`.

## 4. Chấm và tổng hợp

```powershell
$run = "ctx-recent-dense"; $split = "dev"; $d = "results/agent/$split/$run"
.venv\Scripts\python.exe scripts/score_agent.py --split $split --run $run
#   -> auto_metrics.json, review_sheet.md, reviews.json (nhãn trống). Đọc review_sheet.md rồi điền nhãn vào reviews.json.
.venv\Scripts\python.exe starter/agent_metrics.py --cases data/day6/cases.json --traces $d/traces.json --reviews $d/reviews.json --split $split --output $d/agent_metrics.json
.venv\Scripts\python.exe scripts/compare_agent.py --split $split --runs baseline-dense ctx-recent-dense hybrid-recent
```

Nhãn có `reviewer` chứa `DRAFT` được báo là "nháp" trong bảng so sánh.

## 5. Test (sau khi chốt cấu hình trong [experiments.md](experiments.md))

```powershell
.venv\Scripts\python.exe scripts/run_agent.py --split test --retriever dense --run baseline-dense   --context-policy first
.venv\Scripts\python.exe scripts/run_agent.py --split test --retriever dense --run ctx-recent-dense --context-policy recent
```

Sau đó chạy bước 4 với `$split = "test"` và `--runs baseline-dense ctx-recent-dense`. Nhãn context 0/1/2 của 5 câu test có đáp án nằm ở `results/agent/test/<run>/context_reviews.json`.

## Đầu ra

| Đường dẫn | Nội dung |
|---|---|
| `results/retrieval/<split>/<run>/` | `summary.json` (Hit@1/3/10, MRR, Context Evidence, độ trễ), `traces.json` (top-10 từng câu: ID, score, rank, trang, metadata) |
| `results/agent/<split>/<run>/traces.json` | Từng câu: mọi tool call, truy vấn, kết quả, context cuối, câu trả lời, citation, token, thời gian, lỗi |
| `results/agent/<split>/<run>/reviews.json`, `context_reviews.json` | Nhãn chấm tay và lý do |
| `results/agent/<split>/comparison.md` | Bảng so sánh cấu hình |
| `results/cache/query_embeddings.json` | Cache embedding câu hỏi (không chứa gold) |
