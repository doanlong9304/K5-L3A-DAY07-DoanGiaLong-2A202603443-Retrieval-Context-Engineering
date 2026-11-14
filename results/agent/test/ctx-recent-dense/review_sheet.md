# Review sheet — test / ctx-recent-dense

Chấm theo BENCHMARK.md: `answer_grade` 0 = sai/thiếu evidence, 1 = đúng một phần, 2 = đúng và đủ (từ chối câu có đáp án = 0); `citation_support`: mỗi citation có thực sự hỗ trợ ý được trích không; `abstention_correct`: câu thiếu evidence có được từ chối mà không thêm khẳng định vô căn cứ không.

## t01 — abstain (3 search, filter={'chapter': 'V'})

**Câu hỏi:** Những ngành, nghề nào bị cấm đầu tư?

**Đáp án chuẩn:** Ngành, nghề cấm theo Điều 6 và điều ước quốc tế liên quan; ngành, nghề có công nghệ, sản phẩm cấm xuất khẩu theo pháp luật quản lý ngoại thương; ngành, nghề bị cấm theo pháp luật nước tiếp nhận đầu tư.

**Evidence gold (trang 30):** 2. Ngành, nghề có công nghệ, sản phẩm thuộc đối tượng cấm xuất khẩu theo quy định của pháp luật về quản lý ngoại thương. 3. Ngành, nghề cấm đầu tư kinh doanh theo quy định của pháp luật nước tiếp nhận đầu tư.

*Tự động:* context có evidence = True, chunk được trích có evidence = False

**Truy vấn của agent:** ngành, nghề cấm đầu tư kinh doanh | Điều 6 cấm hoạt động đầu tư kinh doanh chất ma túy | nghiêm cấm kinh doanh mại dâm, mua bán người, mô, xác, bộ phận cơ thể người

**Câu trả lời của agent:**

> Không đủ bằng chứng trong tài liệu để trả lời.

**Lý do từ chối (model):** Tôi chưa trả lời được vì các đoạn luật tìm được không có danh sách ngành, nghề bị cấm đầu tư kinh doanh. Danh sách này nằm ở Điều 6 của Luật Đầu tư 143/2025/QH15. Đoạn gần nhất tìm được là Điều 40 [B-4679425b231441ae], nói về ngành, nghề cấm đầu tư ra nước ngoài. Điều này chỉ dẫn chiếu sang Điều 6, chứ không liệt kê từng ngành, nghề. Theo Điều 40, các ngành, nghề cấm đầu tư ra nước ngoài gồm: (1) ngành, nghề cấm theo Điều 6 và các điều ước quốc tế mà Việt Nam là thành viên; (2) ngành, nghề có công nghệ, sản phẩm bị cấm xuất khẩu theo pháp luật về quản lý ngoại thương; (3) ngành, nghề bị cấm theo pháp luật của nước tiếp nhận đầu tư. Muốn trả lời đầy đủ câu hỏi thì cần có nội dung Điều 6, nhưng đã hết lượt tìm kiếm.

## t02 — answered (1 search, filter=None)

**Câu hỏi:** Một công ty được thành lập theo pháp luật nước ngoài, kinh doanh tại Việt Nam thì được coi là loại nhà đầu tư nào?

**Đáp án chuẩn:** Nhà đầu tư nước ngoài.

**Evidence gold (trang 3):** Nhà đầu tư nước ngoài là cá nhân có quốc tịch nước ngoài, tổ chức thành lập theo pháp luật nước ngoài thực hiện hoạt động đầu tư kinh doanh tại Việt Nam.

*Tự động:* context có evidence = True, chunk được trích có evidence = True

**Truy vấn của agent:** nhà đầu tư nước ngoài là cá nhân có quốc tịch nước ngoài, tổ chức thành lập theo pháp luật nước ngoài

**Câu trả lời của agent:**

> Công ty này được coi là **nhà đầu tư nước ngoài**. Luật quy định nhà đầu tư nước ngoài là cá nhân có quốc tịch nước ngoài hoặc tổ chức thành lập theo pháp luật nước ngoài, thực hiện hoạt động đầu tư kinh doanh tại Việt Nam [B-0a9a8be259cae4c2].
> 
> Đây là một trong ba loại nhà đầu tư theo luật: nhà đầu tư trong nước, nhà đầu tư nước ngoài và tổ chức kinh tế có vốn đầu tư nước ngoài [B-0a9a8be259cae4c2].
> 
> Cần phân biệt với tổ chức kinh tế có vốn đầu tư nước ngoài. Đó là tổ chức được thành lập theo pháp luật Việt Nam và có nhà đầu tư nước ngoài là thành viên hoặc cổ đông [B-0a9a8be259cae4c2].
> 
> Nếu nhà đầu tư nước ngoài muốn thành lập tổ chức kinh tế tại Việt Nam, họ phải đáp ứng điều kiện tiếp cận thị trường đối với nhà đầu tư nước ngoài theo Điều 8 khi làm thủ tục [B-d809ebe15fe79a20].

<details><summary>[B-0a9a8be259cae4c2] trang 2-3, Điều 3</summary>

```text
Điều 3. Giải thích từ ngữ (tiếp)
17. Khu kinh tế là khu vực có ranh giới địa lý xác định, gồm nhiều khu chức
năng, được thành lập để thực hiện các mục tiêu thu hút đầu tư, phát triển kinh tế -
xã hội và bảo vệ quốc phòng, an ninh.
18. Nhà đầu tư là tổ chức, cá nhân thực hiện hoạt động đầu tư kinh doanh,
gồm nhà đầu tư trong nước, nhà đầu tư nước ngoài và tổ chức kinh tế có vốn đầu
tư nước ngoài.
19. Nhà đầu tư nước ngoài là cá nhân có quốc tịch nước ngoài, tổ chức thành
lập theo pháp luật nước ngoài thực hiện hoạt động đầu tư kinh doanh tại Việt Nam.
20. Nhà đầu tư trong nước là cá nhân có quốc tịch Việt Nam, tổ chức kinh
tế không có nhà đầu tư nước ngoài là thành viên hoặc cổ đông.
21. Tổ chức kinh tế là tổ chức được thành lập và hoạt động theo quy định
của pháp luật Việt Nam, gồm doanh nghiệp, hợp tác xã, liên hiệp hợp tác xã và tổ
chức khác thực hiện hoạt động đầu tư kinh doanh.
22. Tổ chức kinh tế có vốn đầu tư nước ngoài là tổ chức kinh tế có nhà đầu
tư nước ngoài là thành viên hoặc cổ đông.
```
</details>

<details><summary>[B-d809ebe15fe79a20] trang 14-15, Điều 19</summary>

```text
Điều 19. Đầu tư thành lập tổ chức kinh tế
1. Nhà đầu tư trong nước thành lập tổ chức kinh tế theo quy định của pháp
luật về doanh nghiệp và pháp luật tương ứng với từng loại hình tổ chức kinh tế.
2. Nhà đầu tư nước ngoài được thành lập tổ chức kinh tế thực hiện dự án đầu
tư trước khi thực hiện thủ tục cấp, điều chỉnh Giấy chứng nhận đăng ký đầu tư và
phải đáp ứng điều kiện tiếp cận thị trường đối với nhà đầu tư nước ngoài quy định
tại Điều 8 của Luật này khi thực hiện thủ tục thành lập tổ chức kinh tế.
3. Chính phủ quy định chi tiết Điều này.
```
</details>

## t03 — answered (1 search, filter=None)

**Câu hỏi:** Sau bao lâu kể từ khi kết thúc tiến độ thực hiện mục tiêu hoạt động thì cơ quan đăng ký đầu tư có thể chấm dứt dự án?

**Đáp án chuẩn:** Sau 24 tháng kể từ thời điểm kết thúc tiến độ thực hiện các mục tiêu hoạt động của dự án (hoặc của từng giai đoạn) nếu nhà đầu tư vẫn không thực hiện được.

**Evidence gold (trang 28):** b) Sau 24 tháng kể từ thời điểm kết thúc tiến độ thực hiện các mục tiêu hoạt động của dự án đầu tư hoặc mục tiêu hoạt động của từng giai đoạn (nếu có)

*Tự động:* context có evidence = True, chunk được trích có evidence = True

**Truy vấn của agent:** chấm dứt hoạt động dự án đầu tư không thực hiện tiến độ

**Câu trả lời của agent:**

> Theo Điều 36 khoản 2 điểm b, cơ quan đăng ký đầu tư có thể chấm dứt hoặc chấm dứt một phần hoạt động của dự án đầu tư **sau 24 tháng** kể từ khi kết thúc tiến độ thực hiện mục tiêu hoạt động [B-2b7d8deec90172dc].
> 
> **Điều kiện áp dụng** [B-2b7d8deec90172dc]:
> - Mốc tính là thời điểm kết thúc tiến độ thực hiện các mục tiêu hoạt động của dự án, hoặc mục tiêu hoạt động của từng giai đoạn (nếu có).
> - Tiến độ này phải được quy định tại văn bản chấp thuận chủ trương đầu tư, Giấy chứng nhận đăng ký đầu tư, hoặc văn bản điều chỉnh hay Giấy chứng nhận điều chỉnh tương ứng.
> - Đến hết 24 tháng, nhà đầu tư vẫn chưa hoàn thành mục tiêu hoạt động đó.
> - Dự án không thuộc trường hợp được điều chỉnh tiến độ theo quy định.
> 
> **Ngoại lệ:** Quy định này không áp dụng cho trường hợp tại điểm đ cùng khoản, tức là dự án đầu tư bị thu hồi đất theo quy định của pháp luật về đất đai [B-2b7d8deec90172dc][B-d4340505f6e7f329].

<details><summary>[B-2b7d8deec90172dc] trang 27-28, Điều 36</summary>

```text
Điều 36. Chấm dứt hoạt động của dự án đầu tư
1. Nhà đầu tư chấm dứt hoạt động đầu tư, dự án đầu tư trong các trường hợp
sau đây:
a) Nhà đầu tư quyết định chấm dứt hoạt động của dự án đầu tư;
b) Theo các điều kiện chấm dứt hoạt động được quy định trong hợp đồng,
điều lệ doanh nghiệp;
c) Hết thời hạn hoạt động của dự án đầu tư.
2. Cơ quan đăng ký đầu tư chấm dứt hoặc chấm dứt một phần hoạt động của
dự án đầu tư trong các trường hợp sau đây:
a) Dự án đầu tư thuộc một trong các trường hợp quy định tại khoản 2 và
khoản 3 Điều 35 của Luật này mà nhà đầu tư không có khả năng khắc phục điều
kiện ngừng hoạt động;
b) Sau 24 tháng kể từ thời điểm kết thúc tiến độ thực hiện các mục tiêu hoạt
động của dự án đầu tư hoặc mục tiêu hoạt động của từng giai đoạn (nếu có) quy
định tại văn bản chấp thuận chủ trương đầu tư, Giấy chứng nhận đăng ký đầu tư
hoặc văn bản chấp thuận điều chỉnh chủ trương đầu tư, Giấy chứng nhận đăng ký
đầu tư điều chỉnh mà nhà đầu tư vẫn không hoàn thành mục tiêu hoạt động này và
không thuộc trường hợp được điều chỉnh tiến độ theo quy định, trừ trường hợp quy
định tại điểm đ khoản này;
```
</details>

<details><summary>[B-d4340505f6e7f329] trang 28-28, Điều 36</summary>

```text
Điều 36. Chấm dứt hoạt động của dự án đầu tư (tiếp)
c) Nhà đầu tư không được tiếp tục sử dụng địa điểm đầu tư và không thực hiện
thủ tục điều chỉnh địa điểm đầu tư trong thời hạn 06 tháng kể từ ngày không được
tiếp tục sử dụng địa điểm đầu tư, trừ trường hợp quy định tại điểm đ khoản này;
d) Dự án đầu tư đã ngừng hoạt động và hết thời hạn 12 tháng kể từ ngày
ngừng hoạt động, cơ quan đăng ký đầu tư không liên lạc được với nhà đầu tư hoặc
đại diện hợp pháp của nhà đầu tư;
đ) Dự án đầu tư thuộc trường hợp bị thu hồi đất theo quy định của pháp luật
về đất đai;
e) Nhà đầu tư không ký quỹ hoặc không có bảo lãnh nghĩa vụ ký quỹ theo quy
định của pháp luật đối với dự án đầu tư thuộc diện bảo đảm thực hiện dự án đầu tư;
g) Nhà đầu tư thực hiện hoạt động đầu tư trên cơ sở giao dịch dân sự giả tạo
theo quy định của pháp luật về dân sự;
h) Theo bản án, quyết định của Tòa án, phán quyết trọng tài;
i) Tổ chức kinh tế đã giải thể nhưng không chấm dứt hoạt động hoặc không
chuyển nhượng, chuyển quyền sở hữu khác theo quy định pháp luật đối với dự án
đầu tư.
```
</details>

## t04 — answered (1 search, filter=None)

**Câu hỏi:** Nhà đầu tư có dự án ở nước ngoài phải gửi báo cáo tình hình hoạt động bao lâu một lần và gửi cho ai?

**Đáp án chuẩn:** Định kỳ 06 tháng và hằng năm, gửi Bộ Tài chính, Ngân hàng Nhà nước Việt Nam và Cơ quan đại diện Việt Nam tại nước tiếp nhận đầu tư.

**Evidence gold (trang 37):** b) Định kỳ 06 tháng, hằng năm, nhà đầu tư gửi báo cáo tình hình hoạt động của dự án đầu tư cho Bộ Tài chính, Ngân hàng Nhà nước Việt Nam, Cơ quan đại diện Việt Nam tại nước tiếp nhận đầu tư;

*Tự động:* context có evidence = True, chunk được trích có evidence = True

**Truy vấn của agent:** chế độ báo cáo hoạt động đầu tư ra nước ngoài

**Câu trả lời của agent:**

> Theo Điều 48 Luật Đầu tư 143/2025/QH15, chế độ báo cáo của nhà đầu tư có dự án ở nước ngoài như sau:
> 
> - **Bao lâu một lần:** Định kỳ 06 tháng và hằng năm, nhà đầu tư gửi báo cáo tình hình hoạt động của dự án [B-71dfbbff0a0b5b66].
> - **Gửi cho ai:** Bộ Tài chính, Ngân hàng Nhà nước Việt Nam và Cơ quan đại diện Việt Nam tại nước tiếp nhận đầu tư [B-71dfbbff0a0b5b66].
> 
> Ngoài báo cáo định kỳ, nhà đầu tư còn phải:
> - **Thông báo khi dự án bắt đầu:** Trong 60 ngày kể từ ngày dự án được nước tiếp nhận đầu tư chấp thuận hoặc cấp phép, gửi thông báo bằng văn bản cho ba cơ quan nêu trên. Kèm theo là bản sao văn bản chấp thuận dự án hoặc tài liệu chứng minh quyền hoạt động đầu tư tại nước đó [B-71dfbbff0a0b5b66].
> - **Báo cáo sau quyết toán thuế:** Trong 06 tháng kể từ ngày có báo cáo quyết toán thuế (hoặc văn bản có giá trị pháp lý tương đương theo luật nước tiếp nhận đầu tư), báo cáo tình hình hoạt động của dự án. Kèm theo là báo cáo tài chính và báo cáo quyết toán thuế (hoặc văn bản tương đương). Báo cáo này gửi ba cơ quan nêu trên và cơ quan quản lý nhà nước có thẩm quyền [B-d5ba860915fd82bb].
> - **Nếu dự án dùng vốn nhà nước:** Thực hiện thêm chế độ báo cáo theo pháp luật về quản lý và đầu tư vốn nhà nước tại doanh nghiệp [B-d5ba860915fd82bb].
> 
> **Hình thức:** Các báo cáo được lập bằng văn bản và gửi qua Hệ thống thông tin quốc gia về đầu tư [B-d5ba860915fd82bb].

<details><summary>[B-71dfbbff0a0b5b66] trang 36-37, Điều 48</summary>

```text
Điều 48. Chế độ báo cáo hoạt động đầu tư ở nước ngoài (tiếp)
a) Trong thời hạn 60 ngày kể từ ngày dự án đầu tư được chấp thuận hoặc cấp
phép theo quy định của pháp luật nước tiếp nhận đầu tư, nhà đầu tư phải gửi thông
báo bằng văn bản về việc thực hiện hoạt động đầu tư ở nước ngoài kèm theo bản
sao văn bản chấp thuận dự án đầu tư hoặc tài liệu chứng minh quyền hoạt động đầu
tư tại nước tiếp nhận đầu tư cho Bộ Tài chính, Ngân hàng Nhà nước Việt Nam, Cơ
quan đại diện Việt Nam tại nước tiếp nhận đầu tư;
b) Định kỳ 06 tháng, hằng năm, nhà đầu tư gửi báo cáo tình hình hoạt động
của dự án đầu tư cho Bộ Tài chính, Ngân hàng Nhà nước Việt Nam, Cơ quan đại
diện Việt Nam tại nước tiếp nhận đầu tư;
```
</details>

<details><summary>[B-d5ba860915fd82bb] trang 37-37, Điều 48</summary>

```text
Điều 48. Chế độ báo cáo hoạt động đầu tư ở nước ngoài (tiếp)
c) Trong thời hạn 06 tháng kể từ ngày có báo cáo quyết toán thuế hoặc văn
bản có giá trị pháp lý tương đương theo quy định của pháp luật nước tiếp nhận đầu
tư, nhà đầu tư báo cáo tình hình hoạt động của dự án đầu tư kèm theo báo cáo tài
chính, báo cáo quyết toán thuế hoặc văn bản có giá trị pháp lý tương đương theo
quy định của pháp luật nước tiếp nhận đầu tư gửi Bộ Tài chính, Ngân hàng Nhà
nước Việt Nam, Cơ quan đại diện Việt Nam tại nước tiếp nhận đầu tư và cơ quan
quản lý nhà nước có thẩm quyền theo quy định của Luật này và quy định khác của
pháp luật có liên quan;
d) Đối với dự án đầu tư ra nước ngoài có sử dụng vốn nhà nước, ngoài việc
thực hiện chế độ báo cáo quy định tại các điểm a, b và c khoản này, nhà đầu tư phải
thực hiện chế độ báo cáo đầu tư theo quy định của pháp luật về quản lý và đầu tư
vốn nhà nước tại doanh nghiệp.
4. Báo cáo quy định tại khoản 2 và khoản 3 Điều này được thực hiện bằng
văn bản và thông qua Hệ thống thông tin quốc gia về đầu tư.
```
</details>

## t05 — answered (1 search, filter=None)

**Câu hỏi:** Luật Đầu tư số 143/2025/QH15 có hiệu lực thi hành từ ngày nào?

**Đáp án chuẩn:** Từ ngày 01 tháng 03 năm 2026, trừ trường hợp quy định tại khoản 2 và khoản 3 Điều 51.

**Evidence gold (trang 39):** 1. Luật này có hiệu lực thi hành từ ngày 01 tháng 03 năm 2026, trừ trường hợp quy định tại khoản 2 và khoản 3 Điều này.

*Tự động:* context có evidence = True, chunk được trích có evidence = True

**Truy vấn của agent:** hiệu lực thi hành

**Câu trả lời của agent:**

> Theo Điều 51, Luật Đầu tư số 143/2025/QH15 có hiệu lực thi hành từ ngày 01/3/2026, nhưng có 2 ngoại lệ [B-fbf3fa0919e2dd84]:
> - Điều 7 và Danh mục ngành, nghề đầu tư kinh doanh có điều kiện tại Phụ lục IV có hiệu lực từ ngày 01/7/2026 [B-fbf3fa0919e2dd84].
> - Khoản 3 Điều 50 có hiệu lực từ ngày 01/01/2026 [B-fbf3fa0919e2dd84].
> 
> Luật Đầu tư năm 2020 (Luật số 61/2020/QH14 và các luật sửa đổi, bổ sung) hết hiệu lực từ ngày Luật này có hiệu lực thi hành. Riêng Điều 7 và Phụ lục IV của Luật Đầu tư năm 2020 hết hiệu lực từ ngày 01/7/2026 [B-fbf3fa0919e2dd84].

<details><summary>[B-fbf3fa0919e2dd84] trang 39-39, Điều 51</summary>

```text
Điều 51. Hiệu lực thi hành
1. Luật này có hiệu lực thi hành từ ngày 01 tháng 03 năm 2026, trừ trường
hợp quy định tại khoản 2 và khoản 3 Điều này.
2. Điều 7 và Danh mục ngành, nghề đầu tư kinh doanh có điều kiện quy định
tại Phụ lục IV ban hành kèm theo Luật này có hiệu lực thi hành từ ngày 01 tháng
7 năm 2026.
3. Khoản 3 Điều 50 của Luật này có hiệu lực thi hành từ ngày 01 tháng 01
năm 2026.
4. Luật Đầu tư số 61/2020/QH14 đã được sửa đổi, bổ sung một số điều theo
Luật số 72/2020/QH14, Luật số 03/2022/QH15, Luật số 05/2022/QH15, Luật
số 08/2022/QH15, Luật số 09/2022/QH15, Luật số 20/2023/QH15, Luật
số 26/2023/QH15, Luật số 27/2023/QH15, Luật số 28/2023/QH15, Luật
số 31/2024/QH15, Luật số 33/2024/QH15, Luật số 43/2024/QH15, Luật
số 57/2024/QH15 và Luật số 90/2025/QH15 (sau đây gọi là Luật Đầu tư năm 2020)
hết hiệu lực kể từ ngày Luật này có hiệu lực thi hành, trừ Điều 7 và Danh mục
ngành, nghề đầu tư kinh doanh có điều kiện quy định tại Phụ lục IV ban hành kèm
theo Luật Đầu tư năm 2020 hết hiệu lực kể từ ngày 01 tháng 7 năm 2026.
```
</details>

## u04 — abstain (3 search, filter=None)

**Câu hỏi:** Cơ quan đăng ký đầu tư phải cấp Giấy chứng nhận đăng ký đầu tư trong bao nhiêu ngày kể từ khi nhận đủ hồ sơ hợp lệ?

**Câu thiếu evidence.** Lý do: Luật không quy định số ngày xử lý hồ sơ cấp Giấy chứng nhận đăng ký đầu tư; thời hạn tính bằng ngày duy nhất trong luật là 60 ngày cho chế độ báo cáo đầu tư ra nước ngoài (tr.36).

**Truy vấn của agent:** thời hạn cấp Giấy chứng nhận đăng ký đầu tư kể từ ngày nhận đủ hồ sơ hợp lệ | trong thời hạn ngày làm việc cơ quan đăng ký đầu tư cấp Giấy chứng nhận | thủ tục cấp Giấy chứng nhận đăng ký đầu tư đối với dự án không thuộc diện chấp thuận chủ trương

**Câu trả lời của agent:**

> Không đủ bằng chứng trong tài liệu để trả lời.

**Lý do từ chối (model):** Các đoạn đã tìm được không nêu số ngày cụ thể mà cơ quan đăng ký đầu tư phải cấp Giấy chứng nhận đăng ký đầu tư kể từ khi nhận đủ hồ sơ hợp lệ. Có ba điểm liên quan. Điều 26 xác định dự án nào phải làm thủ tục cấp Giấy chứng nhận đăng ký đầu tư [B-ee1e89ea371943d8]. Khoản 5 Điều 26 giao Chính phủ quy định điều kiện, hồ sơ, trình tự, thủ tục cấp Giấy chứng nhận [B-ee1e89ea371943d8]. Điều 27 quy định cơ quan nào có thẩm quyền cấp [B-1456b3d32f36a55c][B-4faa68df46076e62]. Thời hạn cấp Giấy chứng nhận có thể nằm trong văn bản của Chính phủ, nhưng văn bản đó không có trong các đoạn đã tìm. Đã hết lượt tìm kiếm.

## u05 — abstain (2 search, filter=None)

**Câu hỏi:** Mức ký quỹ bảo đảm thực hiện dự án đầu tư là bao nhiêu phần trăm tổng vốn đầu tư?

**Câu thiếu evidence.** Lý do: Điều 30 (tr.23) quy định nghĩa vụ ký quỹ hoặc bảo lãnh ngân hàng và các trường hợp được miễn, nhưng không quy định mức hay tỷ lệ ký quỹ; khoản 2 giao 'Chính phủ quy định chi tiết Điều này'.

**Truy vấn của agent:** ký quỹ bảo đảm thực hiện dự án đầu tư mức ký quỹ | tỷ lệ ký quỹ theo tổng vốn đầu tư dự án

**Câu trả lời của agent:**

> Không đủ bằng chứng trong tài liệu để trả lời.

**Lý do từ chối (model):** Các đoạn luật tìm được không nêu mức ký quỹ tính theo phần trăm tổng vốn đầu tư. Điều 30 Luật Đầu tư 143/2025/QH15 chỉ quy định ai phải ký quỹ (hoặc có bảo lãnh ngân hàng về nghĩa vụ ký quỹ), tức nhà đầu tư có dự án đề nghị Nhà nước giao đất, cho thuê đất hoặc cho phép chuyển mục đích sử dụng đất. Điều này cũng nêu các trường hợp được miễn: trúng đấu giá quyền sử dụng đất, trúng đấu thầu dự án có sử dụng đất, nhận chuyển nhượng dự án đã ký quỹ, nhận chuyển nhượng quyền sử dụng đất, trúng đấu giá quyền khai thác khoáng sản. Khoản 2 Điều 30 giao Chính phủ quy định chi tiết [B-9e8417206087b503]. Khoản 7 Điều 52 chỉ nói về chuyển tiếp cho dự án có trước ngày 01/7/2015 [B-7b895db1dad63922]. Vì vậy mức phần trăm cụ thể có lẽ nằm trong nghị định của Chính phủ hướng dẫn luật này, không có trong các đoạn luật đã tìm được.

## u06 — abstain (2 search, filter=None)

**Câu hỏi:** Doanh nghiệp có vốn đầu tư nước ngoài phải trả mức lương tối thiểu bao nhiêu cho người lao động Việt Nam?

**Câu thiếu evidence.** Lý do: Luật Đầu tư không quy định tiền lương; 'lao động' chỉ xuất hiện như tiêu chí dự án hoặc dẫn chiếu pháp luật về lao động (tr.10, 23, 27).

**Truy vấn của agent:** tổ chức kinh tế có vốn đầu tư nước ngoài người lao động tiền lương | mức lương tối thiểu quyền lợi người lao động trong dự án đầu tư

**Câu trả lời của agent:**

> Không đủ bằng chứng trong tài liệu để trả lời.

**Lý do từ chối (model):** Tôi không tìm thấy mức lương tối thiểu mà doanh nghiệp có vốn đầu tư nước ngoài phải trả cho người lao động Việt Nam trong các đoạn của Luật Đầu tư 143/2025/QH15 đã tra được. Tôi đã tìm theo hai hướng: tiền lương người lao động tại tổ chức kinh tế có vốn đầu tư nước ngoài, và mức lương tối thiểu, quyền lợi người lao động trong dự án đầu tư. Kết quả không có con số, mức tiền hay quy định nào về lương tối thiểu. Đoạn gần nhất là Điều 29 khoản 3, chỉ yêu cầu nhà đầu tư tuân thủ pháp luật về lao động khi thực hiện dự án đầu tư. Vì vậy mức lương cụ thể có lẽ nằm trong văn bản pháp luật về lao động và tiền lương, không có trong các đoạn Luật Đầu tư đã tra.

