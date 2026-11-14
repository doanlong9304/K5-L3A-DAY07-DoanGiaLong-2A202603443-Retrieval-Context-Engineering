# Kết nối index Day 6

Day 7 dùng lại nguyên index Day 6, **chỉ đọc**, không ingest lại và không tạo database mới.

| Thành phần | Giá trị |
|---|---|
| Corpus | Luật Đầu tư 143/2025/QH15 (`luat-dau-tu-143-2025-qh15`), 43 trang nội dung, `doc_version` = sha256 PDF `567993cf…` |
| Embedding | `gemini-embedding-001`, 768 chiều; tài liệu `RETRIEVAL_DOCUMENT`, query `RETRIEVAL_QUERY` (cùng model/chiều với index) |
| Vector store | PostgreSQL 16 + pgvector 0.8.7, bảng `lab_chunks`, cosine (`<=>`), tìm chính xác (không ANN) |
| Chunk dùng cho Day 7 | Chiến lược **B** (theo cấu trúc Điều/khoản, tối đa 1200 ký tự): 118 chunk, ID `B-<hash>` |
| Docker | Project `day6_student_starter`, container `day6_student_starter-postgres-1`, volume `day6_student_starter_pg_data`, cổng `127.0.0.1:55633` |

Cấu hình: [configs/day6_index.json](../configs/day6_index.json). Code: [src/day6_index.py](../src/day6_index.py) (`GeminiQueryEmbedder`, `Day6Store`, `DenseRetriever`).

## Chạy

```powershell
py -3.12 -m venv .venv
.venv\Scripts\python.exe -m pip install -r requirements.txt
copy .env.example .env      # điền GEMINI_API_KEY và DAY6_STARTER_DIR (thư mục starter/ của repo Day 6)
.venv\Scripts\python.exe scripts/check_day6.py --start                     # bật container Day 6 + kiểm tra index
.venv\Scripts\python.exe scripts/check_day6.py --query "câu hỏi thử"       # thêm 1 lần gọi embedding thật
```

`--start` chạy `docker compose` bằng file compose và tên project của Day 6, nên dùng lại đúng container và volume đã có vector. Không chạy `docker compose down -v` (xóa volume = mất index, phải ingest lại).

## Ghi chú

- Kết nối mở với `default_transaction_read_only=on`; mọi lệnh ghi vào index bị PostgreSQL từ chối.
- Cổng 55633 thay cho 55433 của đề vì 55433 nằm trong dải cổng Windows (WinNAT/Hyper-V) giữ chỗ trên máy này; đổi bằng `docker-compose.override.yml` trong repo Day 6.
- Người chấm không có database này: để tái lập, chạy `python -m src.pipeline ingest` trong repo Day 6 (cần key Gemini; chi phí ~58k token, xem `results/ingest_report.json` của Day 6).
