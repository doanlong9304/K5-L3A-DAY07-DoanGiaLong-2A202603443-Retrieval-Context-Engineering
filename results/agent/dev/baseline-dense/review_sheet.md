# Review sheet — dev / baseline-dense

Chấm theo BENCHMARK.md: `answer_grade` 0 = sai/thiếu evidence, 1 = đúng một phần, 2 = đúng và đủ (từ chối câu có đáp án = 0); `citation_support`: mỗi citation có thực sự hỗ trợ ý được trích không; `abstention_correct`: câu thiếu evidence có được từ chối mà không thêm khẳng định vô căn cứ không.

## q01 — answered (1 search, filter=None)

**Câu hỏi:** Thời hạn hoạt động tối đa của dự án đầu tư trong khu kinh tế là bao lâu?

**Đáp án chuẩn:** Không quá 70 năm.

**Evidence gold (trang 23):** Thời hạn hoạt động của dự án đầu tư trong khu kinh tế không quá 70 năm.

*Tự động:* context có evidence = True, chunk được trích có evidence = True

**Truy vấn của agent:** thời hạn hoạt động của dự án đầu tư trong khu kinh tế

**Câu trả lời của agent:**

> Theo Điều 31 Luật Đầu tư 143/2025/QH15, thời hạn hoạt động của dự án đầu tư trong khu kinh tế **không quá 70 năm** [B-0288b0e0f7ba0af3].
> 
> Một số quy định liên quan:
> - Trường hợp tiến độ, thời hạn hoạt động bị ảnh hưởng do các trường hợp tại điểm a, b, c, d và g khoản 4 Điều 33 thì thời gian bị chậm không tính vào thời hạn hoạt động của dự án [B-0288b0e0f7ba0af3].
> - Trong quá trình thực hiện dự án, nhà đầu tư được điều chỉnh tăng hoặc giảm thời hạn hoạt động. Thời hạn sau khi điều chỉnh không được vượt quá mức tối đa nói trên [B-e7304ebd3af27c91].
> - Khi hết thời hạn, nếu nhà đầu tư muốn tiếp tục và đáp ứng điều kiện theo quy định của pháp luật thì được xem xét gia hạn. Mỗi lần gia hạn tối đa không quá thời hạn nói trên [B-e7304ebd3af27c91].
> - Hai loại dự án không được gia hạn: (a) dự án dùng công nghệ lạc hậu, tiềm ẩn nguy cơ gây ô nhiễm môi trường, thâm dụng tài nguyên; (b) dự án mà nhà đầu tư phải chuyển giao không bồi hoàn tài sản cho Nhà nước Việt Nam hoặc bên Việt Nam [B-e7304ebd3af27c91].

<details><summary>[B-0288b0e0f7ba0af3] trang 23-23, Điều 31</summary>

```text
Điều 31. Thời hạn hoạt động, tiến độ thực hiện của dự án đầu tư
1. Thời hạn hoạt động của dự án đầu tư trong khu kinh tế không quá 70 năm.
2. Thời hạn hoạt động của dự án đầu tư ngoài khu kinh tế không quá 50 năm.
Dự án đầu tư thực hiện tại địa bàn có điều kiện kinh tế - xã hội khó khăn, địa bàn
có điều kiện kinh tế - xã hội đặc biệt khó khăn hoặc dự án đầu tư có vốn đầu tư lớn
nhưng thu hồi vốn chậm; dự án đầu tư xây dựng và kinh doanh kết cấu hạ tầng khu
công nghệ cao, khu công nghiệp công nghệ cao, khu công nghệ số tập trung; dự án
thuộc diện ưu đãi, hỗ trợ đầu tư đặc biệt quy định tại khoản 2 Điều 17 của Luật này
thì thời hạn hoạt động của dự án đầu tư có thể dài hơn nhưng không quá 70 năm.
3. Trường hợp tiến độ, thời hạn hoạt động của dự án bị ảnh hưởng trong các
trường hợp quy định tại các khoản a, b, c, d và g khoản 4 Điều 33 của Luật này thì
thời gian bị chậm đó không tính vào thời hạn hoạt động, tiến độ thực hiện của dự
án đầu tư.
```
</details>

<details><summary>[B-e7304ebd3af27c91] trang 24-24, Điều 31</summary>

```text
Điều 31. Thời hạn hoạt động, tiến độ thực hiện của dự án đầu tư (tiếp)
4. Trong quá trình thực hiện dự án đầu tư, nhà đầu tư được điều chỉnh tăng
hoặc giảm thời hạn hoạt động của dự án đầu tư. Thời hạn hoạt động của dự án đầu
tư sau khi điều chỉnh không được vượt quá thời hạn quy định tại khoản 1 và khoản
2 Điều này.
5. Khi hết thời hạn hoạt động của dự án đầu tư mà nhà đầu tư có nhu cầu
tiếp tục thực hiện dự án đầu tư và đáp ứng điều kiện theo quy định của pháp luật
thì được xem xét gia hạn thời hạn hoạt động, trừ các dự án đầu tư sau đây:
a) Dự án đầu tư sử dụng công nghệ lạc hậu, tiềm ẩn nguy cơ gây ô nhiễm
môi trường, thâm dụng tài nguyên;
b) Dự án đầu tư thuộc trường hợp nhà đầu tư phải chuyển giao không bồi
hoàn tài sản cho Nhà nước Việt Nam hoặc bên Việt Nam.
Thời gian mỗi lần gia hạn tối đa không quá thời hạn quy định tại khoản 1 và
khoản 2 Điều này.
6. Chính phủ quy định chi tiết Điều này.
```
</details>

## q02 — answered (1 search, filter=None)

**Câu hỏi:** Một dự án nằm ngoài khu kinh tế thì được phép hoạt động trong thời gian dài nhất là bao nhiêu năm?

**Đáp án chuẩn:** Không quá 50 năm (trừ các trường hợp đặc biệt được kéo dài tối đa 70 năm).

**Evidence gold (trang 23):** Thời hạn hoạt động của dự án đầu tư ngoài khu kinh tế không quá 50 năm.

*Tự động:* context có evidence = True, chunk được trích có evidence = True

**Truy vấn của agent:** thời hạn hoạt động của dự án đầu tư ngoài khu kinh tế không quá năm

**Câu trả lời của agent:**

> Theo Luật Đầu tư 143/2025/QH15, dự án đầu tư nằm ngoài khu kinh tế được hoạt động **không quá 50 năm** [B-0288b0e0f7ba0af3].
> 
> **Trường hợp được dài hơn, nhưng tối đa 70 năm** [B-0288b0e0f7ba0af3]:
> - Dự án ở địa bàn có điều kiện kinh tế - xã hội khó khăn hoặc đặc biệt khó khăn.
> - Dự án có vốn đầu tư lớn nhưng thu hồi vốn chậm.
> - Dự án xây dựng và kinh doanh hạ tầng khu công nghệ cao, khu công nghiệp công nghệ cao hoặc khu công nghệ số tập trung.
> - Dự án được ưu đãi, hỗ trợ đầu tư đặc biệt theo khoản 2 Điều 17.
> 
> **Các điểm liên quan:**
> - Nếu dự án bị chậm vì các trường hợp ở điểm a, b, c, d và g khoản 4 Điều 33, thời gian bị chậm không tính vào thời hạn hoạt động [B-0288b0e0f7ba0af3].
> - Nhà đầu tư được điều chỉnh tăng hoặc giảm thời hạn, nhưng sau khi điều chỉnh không được vượt mức tối đa nêu trên [B-e7304ebd3af27c91].
> - Khi hết hạn, dự án có thể được xem xét gia hạn nếu đáp ứng điều kiện. Mỗi lần gia hạn không quá mức tối đa nêu trên [B-e7304ebd3af27c91].
> - Không được gia hạn với hai loại dự án [B-e7304ebd3af27c91]:
>   - Dự án dùng công nghệ lạc hậu, có nguy cơ gây ô nhiễm môi trường hoặc thâm dụng tài nguyên.
>   - Dự án mà nhà đầu tư phải chuyển giao tài sản không bồi hoàn cho Nhà nước Việt Nam hoặc bên Việt Nam.

<details><summary>[B-0288b0e0f7ba0af3] trang 23-23, Điều 31</summary>

```text
Điều 31. Thời hạn hoạt động, tiến độ thực hiện của dự án đầu tư
1. Thời hạn hoạt động của dự án đầu tư trong khu kinh tế không quá 70 năm.
2. Thời hạn hoạt động của dự án đầu tư ngoài khu kinh tế không quá 50 năm.
Dự án đầu tư thực hiện tại địa bàn có điều kiện kinh tế - xã hội khó khăn, địa bàn
có điều kiện kinh tế - xã hội đặc biệt khó khăn hoặc dự án đầu tư có vốn đầu tư lớn
nhưng thu hồi vốn chậm; dự án đầu tư xây dựng và kinh doanh kết cấu hạ tầng khu
công nghệ cao, khu công nghiệp công nghệ cao, khu công nghệ số tập trung; dự án
thuộc diện ưu đãi, hỗ trợ đầu tư đặc biệt quy định tại khoản 2 Điều 17 của Luật này
thì thời hạn hoạt động của dự án đầu tư có thể dài hơn nhưng không quá 70 năm.
3. Trường hợp tiến độ, thời hạn hoạt động của dự án bị ảnh hưởng trong các
trường hợp quy định tại các khoản a, b, c, d và g khoản 4 Điều 33 của Luật này thì
thời gian bị chậm đó không tính vào thời hạn hoạt động, tiến độ thực hiện của dự
án đầu tư.
```
</details>

<details><summary>[B-e7304ebd3af27c91] trang 24-24, Điều 31</summary>

```text
Điều 31. Thời hạn hoạt động, tiến độ thực hiện của dự án đầu tư (tiếp)
4. Trong quá trình thực hiện dự án đầu tư, nhà đầu tư được điều chỉnh tăng
hoặc giảm thời hạn hoạt động của dự án đầu tư. Thời hạn hoạt động của dự án đầu
tư sau khi điều chỉnh không được vượt quá thời hạn quy định tại khoản 1 và khoản
2 Điều này.
5. Khi hết thời hạn hoạt động của dự án đầu tư mà nhà đầu tư có nhu cầu
tiếp tục thực hiện dự án đầu tư và đáp ứng điều kiện theo quy định của pháp luật
thì được xem xét gia hạn thời hạn hoạt động, trừ các dự án đầu tư sau đây:
a) Dự án đầu tư sử dụng công nghệ lạc hậu, tiềm ẩn nguy cơ gây ô nhiễm
môi trường, thâm dụng tài nguyên;
b) Dự án đầu tư thuộc trường hợp nhà đầu tư phải chuyển giao không bồi
hoàn tài sản cho Nhà nước Việt Nam hoặc bên Việt Nam.
Thời gian mỗi lần gia hạn tối đa không quá thời hạn quy định tại khoản 1 và
khoản 2 Điều này.
6. Chính phủ quy định chi tiết Điều này.
```
</details>

## q03 — answered (1 search, filter=None)

**Câu hỏi:** Tài sản hợp pháp của nhà đầu tư có bị quốc hữu hóa hay tịch thu bằng biện pháp hành chính không?

**Đáp án chuẩn:** Không, tài sản hợp pháp của nhà đầu tư không bị quốc hữu hóa hoặc bị tịch thu bằng biện pháp hành chính.

**Evidence gold (trang 8):** Tài sản hợp pháp của nhà đầu tư không bị quốc hữu hóa hoặc bị tịch thu bằng biện pháp hành chính.

*Tự động:* context có evidence = True, chunk được trích có evidence = True

**Truy vấn của agent:** bảo đảm quyền sở hữu tài sản không bị quốc hữu hóa tịch thu bằng biện pháp hành chính

**Câu trả lời của agent:**

> Không. Theo Luật Đầu tư 143/2025/QH15, tài sản hợp pháp của nhà đầu tư không bị quốc hữu hóa và cũng không bị tịch thu bằng biện pháp hành chính [B-2bc6a34e63543c75].
> 
> Có một trường hợp được luật nêu riêng: Nhà nước có thể trưng mua hoặc trưng dụng tài sản vì lý do quốc phòng, an ninh, lợi ích quốc gia, tình trạng khẩn cấp hoặc phòng, chống thiên tai. Khi đó, nhà đầu tư được thanh toán và bồi thường theo pháp luật về trưng mua, trưng dụng tài sản và các quy định pháp luật khác có liên quan [B-2bc6a34e63543c75].
> 
> Quy định này nằm trong nguyên tắc chung: Nhà nước công nhận và bảo hộ quyền sở hữu về tài sản, vốn đầu tư, thu nhập và các quyền, lợi ích hợp pháp khác của nhà đầu tư [B-0d831dd4fbfc1eb9].

<details><summary>[B-2bc6a34e63543c75] trang 8-8, Điều 9</summary>

```text
Điều 9. Bảo đảm quyền sở hữu tài sản
1. Tài sản hợp pháp của nhà đầu tư không bị quốc hữu hóa hoặc bị tịch thu
bằng biện pháp hành chính.
2. Trường hợp Nhà nước trưng mua, trưng dụng tài sản vì lý do quốc phòng,
an ninh hoặc vì lợi ích quốc gia, tình trạng khẩn cấp, phòng, chống thiên tai thì nhà
đầu tư được thanh toán, bồi thường theo quy định của pháp luật về trưng mua,
trưng dụng tài sản và quy định của pháp luật khác có liên quan.
```
</details>

<details><summary>[B-0d831dd4fbfc1eb9] trang 4-5, Điều 5</summary>

```text
Điều 5. Chính sách về đầu tư kinh doanh
1. Nhà đầu tư có quyền thực hiện hoạt động đầu tư kinh doanh trong ngành,
nghề mà Luật này không cấm. Đối với ngành, nghề đầu tư kinh doanh có điều
kiện thì nhà đầu tư phải đáp ứng các điều kiện đầu tư kinh doanh theo quy định
của pháp luật.
2. Nhà đầu tư được tự quyết định và tự chịu trách nhiệm về hoạt động đầu
tư kinh doanh theo quy định của Luật này và quy định khác của pháp luật có liên
quan; được tiếp cận, sử dụng các nguồn vốn tín dụng, quỹ hỗ trợ, sử dụng đất đai
và tài nguyên khác theo quy định của pháp luật.
3. Nhà đầu tư bị đình chỉ, ngừng, chấm dứt hoạt động đầu tư kinh doanh nếu
hoạt động này gây phương hại hoặc có nguy cơ gây phương hại đến quốc phòng,
an ninh quốc gia.
4. Nhà nước công nhận và bảo hộ quyền sở hữu về tài sản, vốn đầu tư, thu
nhập và các quyền, lợi ích hợp pháp khác của nhà đầu tư.
5. Nhà nước đối xử bình đẳng giữa các nhà đầu tư; có chính sách khuyến
khích và tạo điều kiện thuận lợi để nhà đầu tư thực hiện hoạt động đầu tư kinh
doanh, phát triển bền vững các ngành kinh tế.
6. Nhà nước tôn trọng và thực hiện các điều ước quốc tế về đầu tư mà nước
Cộng hòa xã hội chủ nghĩa Việt Nam là thành viên.
```
</details>

## q04 — answered (1 search, filter=None)

**Câu hỏi:** Nhà đầu tư nước ngoài cần đáp ứng điều kiện gì để được chuyển vốn đầu tư ra nước ngoài?

**Đáp án chuẩn:** Phải thực hiện đầy đủ nghĩa vụ tài chính đối với Nhà nước Việt Nam theo quy định của pháp luật.

**Evidence gold (trang 9):** Sau khi thực hiện đầy đủ nghĩa vụ tài chính đối với Nhà nước Việt Nam theo quy định của pháp luật, nhà đầu tư nước ngoài được chuyển ra nước ngoài các tài sản sau đây: 1. Vốn đầu tư, các khoản thanh lý đầu tư;

*Tự động:* context có evidence = True, chunk được trích có evidence = True

**Truy vấn của agent:** điều kiện chuyển vốn đầu tư ra nước ngoài

**Câu trả lời của agent:**

> Theo Điều 11, nhà đầu tư nước ngoài phải **thực hiện đầy đủ nghĩa vụ tài chính đối với Nhà nước Việt Nam theo quy định của pháp luật** trước khi chuyển vốn ra nước ngoài [B-0b6f226d8638bc81].
> 
> Khi đã làm xong nghĩa vụ này, nhà đầu tư nước ngoài được chuyển ra nước ngoài các tài sản sau [B-0b6f226d8638bc81]:
> 1. Vốn đầu tư và các khoản thanh lý đầu tư;
> 2. Thu nhập từ hoạt động đầu tư kinh doanh;
> 3. Tiền và tài sản khác thuộc sở hữu hợp pháp của nhà đầu tư.
> 
> Lưu ý: Điều 43 nói về việc chuyển vốn khi đầu tư ra nước ngoài. Theo điều này, Chính phủ quy định việc mở tài khoản vốn đầu tư ra nước ngoài, chuyển vốn đầu tư ra nước ngoài và chuyển lợi nhuận về nước. Các đoạn luật đã tra cứu không nêu chi tiết những quy định đó [B-f79f725070650181].

<details><summary>[B-0b6f226d8638bc81] trang 9-9, Điều 11</summary>

```text
Điều 11. Bảo đảm quyền chuyển tài sản của nhà đầu tư ra nước ngoài
Sau khi thực hiện đầy đủ nghĩa vụ tài chính đối với Nhà nước Việt Nam theo
quy định của pháp luật, nhà đầu tư nước ngoài được chuyển ra nước ngoài các tài
sản sau đây:
1. Vốn đầu tư, các khoản thanh lý đầu tư;
2. Thu nhập từ hoạt động đầu tư kinh doanh;
3. Tiền và tài sản khác thuộc sở hữu hợp pháp của nhà đầu tư.
```
</details>

<details><summary>[B-f79f725070650181] trang 31-31, Điều 43</summary>

```text
Điều 43. Triển khai hoạt động đầu tư ở nước ngoài
Chính phủ quy định việc mở tài khoản vốn đầu tư ra nước ngoài, chuyển vốn
đầu tư ra nước ngoài, sử dụng lợi nhuận ở nước ngoài, chuyển lợi nhuận về nước
và việc triển khai hoạt động đầu tư ở nước ngoài.
```
</details>

## q05 — answered (1 search, filter=None)

**Câu hỏi:** Tranh chấp giữa các nhà đầu tư mà có ít nhất một bên là nhà đầu tư nước ngoài có được giải quyết tại Trọng tài nước ngoài không?

**Đáp án chuẩn:** Có. Có thể giải quyết qua Tòa án Việt Nam, Trọng tài Việt Nam, Trọng tài nước ngoài, Trọng tài quốc tế hoặc trọng tài do các bên thỏa thuận thành lập.

**Evidence gold (trang 10):** Tranh chấp giữa các nhà đầu tư trong đó có ít nhất một bên là nhà đầu tư nước ngoài hoặc tổ chức kinh tế quy định tại các điểm a, b và c khoản 1 Điều 20 của Luật này được giải quyết thông qua một trong những cơ quan, tổ chức sau đây: a) Tòa án Việt Nam; b) Trọng tài Việt Nam; c) Trọng tài nước ngoài;

*Tự động:* context có evidence = True, chunk được trích có evidence = True

**Truy vấn của agent:** giải quyết tranh chấp nhà đầu tư nước ngoài Trọng tài nước ngoài

**Câu trả lời của agent:**

> Có. Tranh chấp giữa các nhà đầu tư, trong đó ít nhất một bên là nhà đầu tư nước ngoài hoặc là tổ chức kinh tế nêu tại các điểm a, b và c khoản 1 Điều 20, có thể được giải quyết tại Trọng tài nước ngoài. Theo khoản 3 Điều 13, các bên được chọn một trong các cơ quan, tổ chức sau: (a) Tòa án Việt Nam, (b) Trọng tài Việt Nam, (c) Trọng tài nước ngoài, (d) Trọng tài quốc tế, hoặc (đ) Trọng tài do các bên tranh chấp thỏa thuận thành lập [B-24ba71437a3919fc].
> 
> Lưu ý:
> - Trước hết, tranh chấp được giải quyết bằng thương lượng, hòa giải. Chỉ khi không thương lượng, hòa giải được thì mới đưa ra Trọng tài hoặc Tòa án [B-24ba71437a3919fc].
> - Quy định trên áp dụng cho tranh chấp giữa các nhà đầu tư với nhau. Nếu nhà đầu tư nước ngoài tranh chấp với cơ quan nhà nước có thẩm quyền về hoạt động đầu tư kinh doanh trên lãnh thổ Việt Nam, thì tranh chấp được giải quyết tại Trọng tài Việt Nam hoặc Tòa án Việt Nam. Ngoại lệ là khi hợp đồng có thỏa thuận khác hoặc điều ước quốc tế mà Việt Nam là thành viên quy định khác [B-ef9489fe04774cc0].

<details><summary>[B-24ba71437a3919fc] trang 9-10, Điều 13</summary>

```text
Điều 13. Giải quyết tranh chấp trong hoạt động đầu tư kinh doanh
1. Tranh chấp liên quan đến hoạt động đầu tư kinh doanh tại Việt Nam được
giải quyết thông qua thương lượng, hòa giải. Trường hợp không thương lượng, hòa
giải được thì tranh chấp được giải quyết tại Trọng tài hoặc Tòa án theo quy định
tại các khoản 2, 3 và 4 Điều này.
2. Tranh chấp giữa các nhà đầu tư trong nước, tổ chức kinh tế có vốn đầu tư
nước ngoài hoặc giữa nhà đầu tư trong nước, tổ chức kinh tế có vốn đầu tư nước
ngoài với cơ quan nhà nước có thẩm quyền liên quan đến hoạt động đầu tư kinh
doanh trên lãnh thổ Việt Nam được giải quyết thông qua Trọng tài Việt Nam hoặc
Tòa án Việt Nam, trừ trường hợp quy định tại khoản 3 Điều này.
3. Tranh chấp giữa các nhà đầu tư trong đó có ít nhất một bên là nhà đầu tư
nước ngoài hoặc tổ chức kinh tế quy định tại các điểm a, b và c khoản 1 Điều 20
của Luật này được giải quyết thông qua một trong những cơ quan, tổ chức sau đây:
a) Tòa án Việt Nam;
b) Trọng tài Việt Nam;
c) Trọng tài nước ngoài;
d) Trọng tài quốc tế;
đ) Trọng tài do các bên tranh chấp thỏa thuận thành lập.
```
</details>

<details><summary>[B-ef9489fe04774cc0] trang 10-10, Điều 13</summary>

```text
Điều 13. Giải quyết tranh chấp trong hoạt động đầu tư kinh doanh (tiếp)
4. Tranh chấp giữa nhà đầu tư nước ngoài với cơ quan nhà nước có thẩm
quyền liên quan đến hoạt động đầu tư kinh doanh trên lãnh thổ Việt Nam được giải
quyết thông qua Trọng tài Việt Nam hoặc Tòa án Việt Nam, trừ trường hợp có thỏa
thuận khác theo hợp đồng hoặc điều ước quốc tế mà nước Cộng hòa xã hội chủ
nghĩa Việt Nam là thành viên có quy định khác.
```
</details>

## q06 — answered (1 search, filter=None)

**Câu hỏi:** Kinh doanh dịch vụ đòi nợ có thuộc ngành, nghề cấm đầu tư kinh doanh không?

**Đáp án chuẩn:** Có, kinh doanh dịch vụ đòi nợ bị cấm.

**Evidence gold (trang 5):** h) Kinh doanh dịch vụ đòi nợ;

*Tự động:* context có evidence = True, chunk được trích có evidence = True

**Truy vấn của agent:** ngành, nghề cấm đầu tư kinh doanh dịch vụ đòi nợ

**Câu trả lời của agent:**

> Có. Kinh doanh dịch vụ đòi nợ là ngành, nghề cấm đầu tư kinh doanh. Điểm h khoản 1 Điều 6 Luật Đầu tư 143/2025/QH15 nêu rõ "Kinh doanh dịch vụ đòi nợ" là một trong các hoạt động bị cấm [B-598fa8ff504ec744].
> 
> Ngoài ra, các ngành, nghề bị cấm tại Điều 6 cũng thuộc ngành, nghề cấm đầu tư ra nước ngoài theo khoản 1 Điều 40 [B-4679425b231441ae].

<details><summary>[B-598fa8ff504ec744] trang 5-5, Điều 6</summary>

```text
Điều 6. Ngành, nghề cấm đầu tư kinh doanh
1. Cấm các hoạt động đầu tư kinh doanh sau đây:
a) Kinh doanh các chất ma túy quy định tại Phụ lục I ban hành kèm theo
Luật này;
b) Kinh doanh các loại hóa chất, khoáng vật quy định tại Phụ lục II ban hành
kèm theo Luật này;
c) Kinh doanh mẫu vật các loài thực vật, động vật hoang dã có nguồn gốc
khai thác từ tự nhiên quy định tại Phụ lục I của Công ước về buôn bán quốc tế các
loài thực vật, động vật hoang dã nguy cấp; mẫu vật các loài thực vật rừng, động
vật rừng, thủy sản nguy cấp, quý, hiếm Nhóm I có nguồn gốc khai thác từ tự nhiên
quy định tại Phụ lục III ban hành kèm theo Luật này;
d) Kinh doanh mại dâm;
đ) Mua, bán người, mô, xác, bộ phận cơ thể người, bào thai người;
e) Hoạt động kinh doanh liên quan đến sinh sản vô tính trên người;
g) Kinh doanh pháo nổ;
h) Kinh doanh dịch vụ đòi nợ;
i) Kinh doanh mua bán bảo vật quốc gia;
k) Kinh doanh xuất khẩu di vật, cổ vật;
l) Kinh doanh thuốc lá điện tử, thuốc lá nung nóng.
```
</details>

<details><summary>[B-4679425b231441ae] trang 30-30, Điều 40</summary>

```text
Điều 40. Ngành, nghề cấm đầu tư ra nước ngoài
1. Ngành, nghề cấm đầu tư kinh doanh quy định tại Điều 6 của Luật này và
các điều ước quốc tế có liên quan mà nước Cộng hòa xã hội chủ nghĩa Việt Nam
là thành viên.
2. Ngành, nghề có công nghệ, sản phẩm thuộc đối tượng cấm xuất khẩu theo
quy định của pháp luật về quản lý ngoại thương.
3. Ngành, nghề cấm đầu tư kinh doanh theo quy định của pháp luật nước
tiếp nhận đầu tư.
```
</details>

## q07 — answered (1 search, filter=None)

**Câu hỏi:** Cơ quan nào lập ra Quỹ Hỗ trợ đầu tư và quỹ này nhằm mục đích gì?

**Đáp án chuẩn:** Chính phủ thành lập, để ổn định môi trường đầu tư, khuyến khích, thu hút nhà đầu tư chiến lược, tập đoàn đa quốc gia và hỗ trợ doanh nghiệp trong nước ở một số lĩnh vực cần khuyến khích đầu tư.

**Evidence gold (trang 13):** Chính phủ thành lập Quỹ Hỗ trợ đầu tư để ổn định môi trường đầu tư, khuyến khích, thu hút nhà đầu tư chiến lược, tập đoàn đa quốc gia và hỗ trợ doanh nghiệp trong nước đối với một số lĩnh vực cần khuyến khích đầu tư.

*Tự động:* context có evidence = True, chunk được trích có evidence = True

**Truy vấn của agent:** Quỹ Hỗ trợ đầu tư thành lập mục đích

**Câu trả lời của agent:**

> Theo Điều 16 Luật Đầu tư 143/2025/QH15:
> 
> - **Cơ quan lập quỹ:** Chính phủ là cơ quan thành lập Quỹ Hỗ trợ đầu tư [B-97c34c9fccf0514f].
> - **Mục đích:** Quỹ nhằm ổn định môi trường đầu tư; khuyến khích, thu hút nhà đầu tư chiến lược và tập đoàn đa quốc gia; hỗ trợ doanh nghiệp trong nước trong một số lĩnh vực cần khuyến khích đầu tư [B-97c34c9fccf0514f].
> - **Chi tiết do Chính phủ quy định:** Chính phủ quy định cụ thể các nội dung sau của Quỹ [B-97c34c9fccf0514f]:
>   - mô hình hoạt động và địa vị pháp lý;
>   - nguồn ngân sách cấp hằng năm và bổ sung cho Quỹ;
>   - hình thức hỗ trợ và cơ chế bồi hoàn hỗ trợ;
>   - các chính sách đặc thù khác.
> - **Yêu cầu trước khi ban hành:** Chính phủ phải báo cáo Ủy ban Thường vụ Quốc hội cho ý kiến trước khi ban hành các quy định này [B-97c34c9fccf0514f].

<details><summary>[B-97c34c9fccf0514f] trang 13-13, Điều 16</summary>

```text
Điều 16. Quỹ Hỗ trợ đầu tư
1. Chính phủ thành lập Quỹ Hỗ trợ đầu tư để ổn định môi trường đầu tư,
khuyến khích, thu hút nhà đầu tư chiến lược, tập đoàn đa quốc gia và hỗ trợ doanh
nghiệp trong nước đối với một số lĩnh vực cần khuyến khích đầu tư.
2. Chính phủ quy định chi tiết mô hình hoạt động, địa vị pháp lý, nguồn ngân
sách cấp hằng năm và bổ sung cho Quỹ, hình thức hỗ trợ, cơ chế bồi hoàn hỗ trợ
và các chính sách đặc thù khác của Quỹ, báo cáo Ủy ban Thường vụ Quốc hội cho
ý kiến trước khi ban hành.
```
</details>

## q08 — answered (1 search, filter={'chapter': 'IV'})

**Câu hỏi:** Có những hình thức đầu tư nào?

**Đáp án chuẩn:** Đầu tư thành lập tổ chức kinh tế; góp vốn, mua cổ phần, mua phần vốn góp; thực hiện dự án đầu tư; hợp đồng BCC; các hình thức, loại hình tổ chức kinh tế mới theo quy định của Chính phủ.

**Evidence gold (trang 14):** 1. Đầu tư thành lập tổ chức kinh tế. 2. Đầu tư góp vốn, mua cổ phần, mua phần vốn góp. 3. Thực hiện dự án đầu tư. 4. Đầu tư theo hình thức hợp đồng BCC.

*Tự động:* context có evidence = True, chunk được trích có evidence = True

**Truy vấn của agent:** hình thức đầu tư

**Câu trả lời của agent:**

> Theo Điều 18 Luật Đầu tư số 143/2025/QH15, có 5 hình thức đầu tư [B-9462dc6128622f7a]:
> 1. Đầu tư thành lập tổ chức kinh tế.
> 2. Đầu tư góp vốn, mua cổ phần, mua phần vốn góp.
> 3. Thực hiện dự án đầu tư.
> 4. Đầu tư theo hình thức hợp đồng BCC.
> 5. Các hình thức đầu tư, loại hình tổ chức kinh tế mới theo quy định của Chính phủ.
> 
> Riêng với hình thức góp vốn, mua cổ phần, mua phần vốn góp, nhà đầu tư nước ngoài phải đáp ứng các điều kiện sau [B-2a38b8fa7e90b581]:
> - Điều kiện tiếp cận thị trường theo Điều 8.
> - Bảo đảm quốc phòng, an ninh.
> - Quy định của pháp luật đất đai về điều kiện nhận quyền sử dụng đất và điều kiện sử dụng đất tại đảo, tại xã, phường, đặc khu khu vực biên giới và tại xã, phường ven biển.
> 
> Chính phủ quy định cụ thể hình thức góp vốn, mua cổ phần, mua phần vốn góp, cùng hồ sơ, trình tự và thủ tục thực hiện [B-93781a19d12412a9].

<details><summary>[B-9462dc6128622f7a] trang 14-14, Điều 18</summary>

```text
Điều 18. Hình thức đầu tư
1. Đầu tư thành lập tổ chức kinh tế.
2. Đầu tư góp vốn, mua cổ phần, mua phần vốn góp.
3. Thực hiện dự án đầu tư.
4. Đầu tư theo hình thức hợp đồng BCC.
5. Các hình thức đầu tư, loại hình tổ chức kinh tế mới theo quy định của
Chính phủ.
```
</details>

<details><summary>[B-2a38b8fa7e90b581] trang 15-16, Điều 21</summary>

```text
Điều 21. Đầu tư theo hình thức góp vốn, mua cổ phần, mua phần vốn góp
1. Nhà đầu tư có quyền góp vốn, mua cổ phần, mua phần vốn góp của tổ
chức kinh tế.
2. Việc nhà đầu tư nước ngoài góp vốn, mua cổ phần, mua phần vốn góp của
tổ chức kinh tế phải đáp ứng các quy định, điều kiện sau đây:
a) Điều kiện tiếp cận thị trường đối với nhà đầu tư nước ngoài quy định tại
Điều 8 của Luật này;
b) Bảo đảm quốc phòng, an ninh theo quy định của Luật này và pháp luật có
liên quan;
c) Quy định của pháp luật về đất đai về điều kiện nhận quyền sử dụng đất,
điều kiện sử dụng đất tại đảo; xã, phường, đặc khu khu vực biên giới; xã, phường
ven biển.
```
</details>

<details><summary>[B-93781a19d12412a9] trang 16-16, Điều 21</summary>

```text
Điều 21. Đầu tư theo hình thức góp vốn, mua cổ phần, mua phần vốn góp (tiếp)
4. Chính phủ quy định hình thức góp vốn, mua cổ phần, mua phần vốn góp
của tổ chức kinh tế; hồ sơ, trình tự, thủ tục góp vốn, mua cổ phần, mua phần vốn
góp của tổ chức kinh tế.
```
</details>

## q09 — answered (3 search, filter={'chapter': 'V'})

**Câu hỏi:** Những ngành, nghề nào thuộc diện đầu tư có điều kiện?

**Đáp án chuẩn:** Ngân hàng; bảo hiểm; chứng khoán; báo chí, phát thanh, truyền hình; kinh doanh bất động sản.

**Evidence gold (trang 30):** 1. Ngành, nghề đầu tư ra nước ngoài có điều kiện bao gồm: a) Ngân hàng; b) Bảo hiểm; c) Chứng khoán; d) Báo chí, phát thanh, truyền hình; đ) Kinh doanh bất động sản.

*Tự động:* context có evidence = True, chunk được trích có evidence = True

**Truy vấn của agent:** ngành, nghề đầu tư kinh doanh có điều kiện | Điều 7 danh mục ngành, nghề đầu tư kinh doanh có điều kiện phụ lục | điều kiện đầu tư kinh doanh vì lý do quốc phòng, an ninh quốc gia, trật tự an toàn xã hội

**Câu trả lời của agent:**

> Các đoạn luật tìm được chưa có danh mục chung về ngành, nghề đầu tư kinh doanh có điều kiện trong nước, nên tôi chưa trả lời được đầy đủ phần đó. Văn bản tìm được chỉ quy định ngành, nghề có điều kiện khi đầu tư ra nước ngoài.
> 
> **Ngành, nghề đầu tư ra nước ngoài có điều kiện gồm:** [B-30b81c76d49df66f]
> - Ngân hàng
> - Bảo hiểm
> - Chứng khoán
> - Báo chí, phát thanh, truyền hình
> - Kinh doanh bất động sản
> 
> **Điều kiện cụ thể nằm ở đâu:** Điều kiện đầu tư ra nước ngoài trong các ngành này do luật, nghị quyết của Quốc hội, pháp lệnh, nghị quyết của Ủy ban Thường vụ Quốc hội, nghị định của Chính phủ và điều ước quốc tế về đầu tư mà Việt Nam là thành viên quy định. [B-30b81c76d49df66f]
> 
> **Ảnh hưởng đến thủ tục:** Thông thường, dự án đầu tư ra nước ngoài phải xin Giấy chứng nhận đăng ký đầu tư ra nước ngoài. Có trường hợp không cần giấy này mà chỉ đăng ký giao dịch ngoại hối: dự án có vốn nhỏ hơn mức Chính phủ quy định. Tuy nhiên, ngoại lệ này chỉ áp dụng khi dự án không thuộc các ngành có điều kiện nêu trên. [B-67bca7e9097c9c87]
> 
> Luật cũng tách riêng một nhóm ngành, nghề bị cấm đầu tư ra nước ngoài, gồm:
> - Ngành, nghề cấm đầu tư kinh doanh theo Điều 6 của Luật và các điều ước quốc tế liên quan.
> - Ngành, nghề có công nghệ, sản phẩm bị cấm xuất khẩu.
> - Ngành, nghề bị cấm theo pháp luật nước tiếp nhận đầu tư.
> 
> [B-4679425b231441ae]

<details><summary>[B-30b81c76d49df66f] trang 30-30, Điều 41</summary>

```text
Điều 41. Ngành, nghề đầu tư ra nước ngoài có điều kiện
1. Ngành, nghề đầu tư ra nước ngoài có điều kiện bao gồm:
a) Ngân hàng;
b) Bảo hiểm;
c) Chứng khoán;
d) Báo chí, phát thanh, truyền hình;
đ) Kinh doanh bất động sản.
2. Điều kiện đầu tư ra nước ngoài trong ngành, nghề quy định tại khoản 1
Điều này được quy định tại luật, nghị quyết của Quốc hội, pháp lệnh, nghị quyết
của Ủy ban Thường vụ Quốc hội, nghị định của Chính phủ và điều ước quốc tế về
đầu tư mà nước Cộng hòa xã hội chủ nghĩa Việt Nam là thành viên.
```
</details>

<details><summary>[B-67bca7e9097c9c87] trang 31-31, Điều 42</summary>

```text
Điều 42. Cấp, điều chỉnh, chấm dứt hiệu lực của Giấy chứng nhận đăng (tiếp)
3. Nhà đầu tư thực hiện thủ tục đăng ký giao dịch ngoại hối theo quy định
của pháp luật về quản lý ngoại hối mà không phải thực hiện thủ tục cấp Giấy chứng
nhận đăng ký đầu tư ra nước ngoài trong các trường hợp sau đây:
a) Dự án đầu tư ra nước ngoài có mức vốn đầu tư ra nước ngoài nhỏ hơn
mức quy định của Chính phủ và không thuộc ngành, nghề đầu tư ra nước ngoài có
điều kiện theo quy định tại khoản 1 Điều 41 của Luật này;
b) Dự án đầu tư ra nước ngoài gắn với quốc phòng, an ninh triển khai theo
thỏa thuận giữa Chính phủ Việt Nam và Chính phủ các nước;
c) Dự án đầu tư ra nước ngoài của các tập đoàn, tổng công ty nhà nước và tổ
chức kinh tế khác theo quy định của Chính phủ.
4. Chính phủ quy định chi tiết Điều này; quy định về điều kiện, hồ sơ, trình
tự thủ tục cấp, điều chỉnh, chấm dứt hiệu lực của Giấy chứng nhận đăng ký đầu tư
ra nước ngoài và nội dung Giấy chứng nhận đăng ký đầu tư ra nước ngoài.
```
</details>

<details><summary>[B-4679425b231441ae] trang 30-30, Điều 40</summary>

```text
Điều 40. Ngành, nghề cấm đầu tư ra nước ngoài
1. Ngành, nghề cấm đầu tư kinh doanh quy định tại Điều 6 của Luật này và
các điều ước quốc tế có liên quan mà nước Cộng hòa xã hội chủ nghĩa Việt Nam
là thành viên.
2. Ngành, nghề có công nghệ, sản phẩm thuộc đối tượng cấm xuất khẩu theo
quy định của pháp luật về quản lý ngoại thương.
3. Ngành, nghề cấm đầu tư kinh doanh theo quy định của pháp luật nước
tiếp nhận đầu tư.
```
</details>

## q10 — answered (1 search, filter=None)

**Câu hỏi:** Hợp đồng BCC ký giữa các nhà đầu tư trong nước được thực hiện theo quy định nào?

**Đáp án chuẩn:** Theo quy định của pháp luật về dân sự và pháp luật có liên quan.

**Evidence gold (trang 16):** 1. Hợp đồng BCC được ký kết giữa các nhà đầu tư trong nước thực hiện theo quy định của pháp luật về dân sự và pháp luật có liên quan.

*Tự động:* context có evidence = True, chunk được trích có evidence = True

**Truy vấn của agent:** hợp đồng BCC giữa các nhà đầu tư trong nước

**Câu trả lời của agent:**

> Theo khoản 1 Điều 22, hợp đồng BCC ký giữa các nhà đầu tư trong nước được thực hiện theo quy định của pháp luật về dân sự và pháp luật có liên quan [B-ab5a5a7a520af026].
> 
> Trường hợp khác: hợp đồng BCC ký giữa nhà đầu tư trong nước với nhà đầu tư nước ngoài, hoặc giữa các nhà đầu tư nước ngoài với nhau, thì phải làm thủ tục cấp Giấy chứng nhận đăng ký đầu tư theo Điều 26 của Luật này [B-ab5a5a7a520af026].
> 
> Điều 22 cũng quy định thêm một số điểm:
> - Các bên tham gia hợp đồng BCC lập ban điều phối để thực hiện hợp đồng. Chức năng, nhiệm vụ, quyền hạn của ban điều phối do các bên thỏa thuận [B-ab5a5a7a520af026].
> - Trong quá trình thực hiện hợp đồng, các bên được thỏa thuận dùng tài sản hình thành từ việc hợp tác kinh doanh để thành lập doanh nghiệp theo pháp luật về doanh nghiệp [B-ab5a5a7a520af026].
> - Chính phủ quy định về nội dung hợp đồng BCC [B-ab5a5a7a520af026].
> 
> Hợp đồng BCC là hợp đồng ký giữa các nhà đầu tư nhằm hợp tác kinh doanh, phân chia lợi nhuận, phân chia sản phẩm theo quy định của pháp luật mà không thành lập tổ chức kinh tế [B-22a114fa9d26e013].

<details><summary>[B-ab5a5a7a520af026] trang 16-16, Điều 22</summary>

```text
Điều 22. Đầu tư theo hình thức hợp đồng BCC
1. Hợp đồng BCC được ký kết giữa các nhà đầu tư trong nước thực hiện theo
quy định của pháp luật về dân sự và pháp luật có liên quan.
2. Hợp đồng BCC được ký kết giữa nhà đầu tư trong nước với nhà đầu tư
nước ngoài hoặc giữa các nhà đầu tư nước ngoài thực hiện thủ tục cấp Giấy chứng
nhận đăng ký đầu tư theo quy định tại Điều 26 của Luật này.
3. Các bên tham gia hợp đồng BCC thành lập ban điều phối để thực hiện hợp
đồng BCC. Chức năng, nhiệm vụ, quyền hạn của ban điều phối do các bên thỏa thuận.
4. Trong quá trình thực hiện hợp đồng BCC, các bên tham gia hợp đồng
được thỏa thuận sử dụng tài sản hình thành từ việc hợp tác kinh doanh để thành lập
doanh nghiệp theo quy định của pháp luật về doanh nghiệp.
5. Chính phủ quy định về nội dung hợp đồng BCC.
```
</details>

<details><summary>[B-22a114fa9d26e013] trang 2-2, Điều 3</summary>

```text
Điều 3. Giải thích từ ngữ (tiếp)
12. Hệ thống thông tin quốc gia về đầu tư là hệ thống thông tin nghiệp vụ
chuyên môn để theo dõi, đánh giá, phân tích tình hình đầu tư trên phạm vi toàn
quốc nhằm phục vụ công tác quản lý nhà nước và hỗ trợ nhà đầu tư trong việc thực
hiện hoạt động đầu tư kinh doanh.
13. Hoạt động đầu tư ra nước ngoài là việc nhà đầu tư chuyển vốn đầu tư từ
Việt Nam ra nước ngoài, sử dụng lợi nhuận thu được từ nguồn vốn đầu tư này để
thực hiện hoạt động đầu tư kinh doanh ở nước ngoài.
14. Hợp đồng hợp tác kinh doanh (sau đây gọi là hợp đồng BCC) là hợp đồng
được ký giữa các nhà đầu tư nhằm hợp tác kinh doanh, phân chia lợi nhuận, phân
chia sản phẩm theo quy định của pháp luật mà không thành lập tổ chức kinh tế.
15. Khu chế xuất là khu công nghiệp chuyên sản xuất hàng xuất khẩu, cung
ứng dịch vụ cho sản xuất hàng xuất khẩu và hoạt động xuất khẩu.
16. Khu công nghiệp là khu vực có ranh giới địa lý xác định, chuyên sản
xuất hàng công nghiệp và cung ứng dịch vụ cho sản xuất công nghiệp.
```
</details>

## q11 — answered (1 search, filter=None)

**Câu hỏi:** Nếu hợp đồng BCC có nhà đầu tư nước ngoài tham gia thì phải làm thủ tục gì?

**Đáp án chuẩn:** Thực hiện thủ tục cấp Giấy chứng nhận đăng ký đầu tư theo Điều 26.

**Evidence gold (trang 16):** 2. Hợp đồng BCC được ký kết giữa nhà đầu tư trong nước với nhà đầu tư nước ngoài hoặc giữa các nhà đầu tư nước ngoài thực hiện thủ tục cấp Giấy chứng nhận đăng ký đầu tư theo quy định tại Điều 26 của Luật này.

*Tự động:* context có evidence = True, chunk được trích có evidence = True

**Truy vấn của agent:** hợp đồng BCC nhà đầu tư nước ngoài thủ tục cấp Giấy chứng nhận đăng ký đầu tư

**Câu trả lời của agent:**

> Nếu hợp đồng BCC có nhà đầu tư nước ngoài tham gia, các bên phải làm thủ tục cấp Giấy chứng nhận đăng ký đầu tư.
> 
> 1. **Thủ tục bắt buộc:** Áp dụng khi hợp đồng BCC được ký giữa nhà đầu tư trong nước với nhà đầu tư nước ngoài, hoặc giữa các nhà đầu tư nước ngoài với nhau. Thủ tục này làm theo Điều 26 của Luật Đầu tư [B-ab5a5a7a520af026]. Điều 26 cũng xếp dự án đầu tư của nhà đầu tư nước ngoài vào nhóm phải làm thủ tục này [B-ee1e89ea371943d8].
>    - Nếu hợp đồng BCC chỉ ký giữa các nhà đầu tư trong nước thì không làm thủ tục này. Khi đó áp dụng pháp luật về dân sự và pháp luật có liên quan [B-ab5a5a7a520af026].
>    - Luật giao Chính phủ quy định điều kiện, hồ sơ, trình tự, thủ tục cấp và nội dung Giấy chứng nhận đăng ký đầu tư [B-ee1e89ea371943d8]. Các tài liệu tìm được không nêu chi tiết hồ sơ, thời hạn hay trình tự cụ thể.
> 
> 2. **Thực hiện hợp đồng:** Các bên phải thành lập ban điều phối để thực hiện hợp đồng BCC. Chức năng, nhiệm vụ và quyền hạn của ban này do các bên tự thỏa thuận [B-ab5a5a7a520af026].
> 
> 3. **Văn phòng điều hành (không bắt buộc):** Nhà đầu tư nước ngoài được thành lập văn phòng điều hành tại Việt Nam để thực hiện hợp đồng. Địa điểm do nhà đầu tư quyết định.
>    - Văn phòng có con dấu, được mở tài khoản, tuyển lao động, ký hợp đồng và kinh doanh trong phạm vi hợp đồng BCC và Giấy chứng nhận đăng ký thành lập văn phòng điều hành.
>    - Hồ sơ, trình tự và thủ tục thành lập, điều chỉnh, chấm dứt văn phòng này do Chính phủ quy định [B-19128a8b6b25c365].

<details><summary>[B-ab5a5a7a520af026] trang 16-16, Điều 22</summary>

```text
Điều 22. Đầu tư theo hình thức hợp đồng BCC
1. Hợp đồng BCC được ký kết giữa các nhà đầu tư trong nước thực hiện theo
quy định của pháp luật về dân sự và pháp luật có liên quan.
2. Hợp đồng BCC được ký kết giữa nhà đầu tư trong nước với nhà đầu tư
nước ngoài hoặc giữa các nhà đầu tư nước ngoài thực hiện thủ tục cấp Giấy chứng
nhận đăng ký đầu tư theo quy định tại Điều 26 của Luật này.
3. Các bên tham gia hợp đồng BCC thành lập ban điều phối để thực hiện hợp
đồng BCC. Chức năng, nhiệm vụ, quyền hạn của ban điều phối do các bên thỏa thuận.
4. Trong quá trình thực hiện hợp đồng BCC, các bên tham gia hợp đồng
được thỏa thuận sử dụng tài sản hình thành từ việc hợp tác kinh doanh để thành lập
doanh nghiệp theo quy định của pháp luật về doanh nghiệp.
5. Chính phủ quy định về nội dung hợp đồng BCC.
```
</details>

<details><summary>[B-ee1e89ea371943d8] trang 20-21, Điều 26</summary>

```text
Điều 26. Dự án thuộc diện cấp Giấy chứng nhận đăng ký đầu tư
1. Các dự án phải thực hiện thủ tục cấp Giấy chứng nhận đăng ký đầu tư
bao gồm:
a) Dự án đầu tư của nhà đầu tư nước ngoài;
b) Dự án đầu tư của tổ chức kinh tế quy định tại khoản 1 Điều 20 của Luật này.
2. Các dự án không phải thực hiện thủ tục cấp Giấy chứng nhận đăng ký đầu
tư bao gồm:
a) Dự án đầu tư của nhà đầu tư trong nước;
b) Dự án đầu tư của tổ chức kinh tế quy định tại khoản 2 Điều 20 của Luật này;
c) Đầu tư theo hình thức góp vốn, mua cổ phần, mua phần vốn góp của tổ
chức kinh tế.
3. Đối với dự án đầu tư quy định tại Điều 24 của Luật này, nhà đầu tư trong
nước, tổ chức kinh tế quy định tại khoản 2 Điều 20 của Luật này triển khai thực
hiện dự án đầu tư sau khi được chấp thuận chủ trương đầu tư.
4. Trường hợp nhà đầu tư có nhu cầu cấp Giấy chứng nhận đăng ký đầu tư
đối với dự án đầu tư quy định tại điểm a và điểm b khoản 2 Điều này, nhà đầu tư
thực hiện thủ tục cấp Giấy chứng nhận đăng ký đầu tư.
5. Chính phủ quy định về điều kiện, hồ sơ, trình tự, thủ tục cấp, điều chỉnh
và nội dung Giấy chứng nhận đăng ký đầu tư.
```
</details>

<details><summary>[B-19128a8b6b25c365] trang 29-29, Điều 37</summary>

```text
Điều 37. Thành lập, điều chỉnh, chấm dứt hoạt động văn phòng điều
hành của nhà đầu tư nước ngoài trong hợp đồng BCC
1. Nhà đầu tư nước ngoài trong hợp đồng BCC được thành lập văn phòng điều
hành tại Việt Nam để thực hiện hợp đồng. Địa điểm văn phòng điều hành do nhà
đầu tư nước ngoài trong hợp đồng BCC quyết định theo yêu cầu thực hiện hợp đồng.
2. Văn phòng điều hành của nhà đầu tư nước ngoài trong hợp đồng BCC có
con dấu; được mở tài khoản, tuyển dụng lao động, ký hợp đồng và tiến hành các
hoạt động kinh doanh trong phạm vi quyền và nghĩa vụ quy định tại hợp đồng BCC
và Giấy chứng nhận đăng ký thành lập văn phòng điều hành.
3. Chính phủ quy định về hồ sơ, trình tự, thủ tục thành lập, điều chỉnh, chấm dứt
hoạt động của văn phòng điều hành của nhà đầu tư nước ngoài trong hợp đồng BCC.
```
</details>

## q12 — answered (1 search, filter=None)

**Câu hỏi:** Loại hợp đồng nào cho phép các nhà đầu tư hợp tác kinh doanh, chia lợi nhuận mà không phải lập tổ chức kinh tế?

**Đáp án chuẩn:** Hợp đồng hợp tác kinh doanh (hợp đồng BCC).

**Evidence gold (trang 2):** Hợp đồng hợp tác kinh doanh (sau đây gọi là hợp đồng BCC) là hợp đồng được ký giữa các nhà đầu tư nhằm hợp tác kinh doanh, phân chia lợi nhuận, phân chia sản phẩm theo quy định của pháp luật mà không thành lập tổ chức kinh tế.

*Tự động:* context có evidence = True, chunk được trích có evidence = True

**Truy vấn của agent:** hợp đồng hợp tác kinh doanh không thành lập tổ chức kinh tế

**Câu trả lời của agent:**

> Đó là **hợp đồng hợp tác kinh doanh**, gọi tắt là **hợp đồng BCC**. Đây là hợp đồng ký giữa các nhà đầu tư để hợp tác kinh doanh và chia lợi nhuận, chia sản phẩm theo quy định của pháp luật mà không lập tổ chức kinh tế [B-22a114fa9d26e013].
> 
> Một số điểm cần lưu ý về hợp đồng BCC:
> - **Thủ tục áp dụng:**
>   - Nếu chỉ các nhà đầu tư trong nước ký với nhau, hợp đồng thực hiện theo pháp luật về dân sự và pháp luật có liên quan [B-ab5a5a7a520af026].
>   - Nếu nhà đầu tư trong nước ký với nhà đầu tư nước ngoài, hoặc các nhà đầu tư nước ngoài ký với nhau, phải làm thủ tục cấp Giấy chứng nhận đăng ký đầu tư theo Điều 26 [B-ab5a5a7a520af026].
> - **Điều hành:** Các bên lập ban điều phối để thực hiện hợp đồng. Chức năng, nhiệm vụ và quyền hạn của ban này do các bên tự thỏa thuận [B-ab5a5a7a520af026].
> - **Lập doanh nghiệp về sau:** Trong quá trình thực hiện hợp đồng, các bên có thể thỏa thuận dùng tài sản hình thành từ việc hợp tác để thành lập doanh nghiệp theo pháp luật về doanh nghiệp [B-ab5a5a7a520af026].
> - **Văn phòng điều hành:** Nhà đầu tư nước ngoài trong hợp đồng BCC được lập văn phòng điều hành tại Việt Nam để thực hiện hợp đồng [B-19128a8b6b25c365].

<details><summary>[B-22a114fa9d26e013] trang 2-2, Điều 3</summary>

```text
Điều 3. Giải thích từ ngữ (tiếp)
12. Hệ thống thông tin quốc gia về đầu tư là hệ thống thông tin nghiệp vụ
chuyên môn để theo dõi, đánh giá, phân tích tình hình đầu tư trên phạm vi toàn
quốc nhằm phục vụ công tác quản lý nhà nước và hỗ trợ nhà đầu tư trong việc thực
hiện hoạt động đầu tư kinh doanh.
13. Hoạt động đầu tư ra nước ngoài là việc nhà đầu tư chuyển vốn đầu tư từ
Việt Nam ra nước ngoài, sử dụng lợi nhuận thu được từ nguồn vốn đầu tư này để
thực hiện hoạt động đầu tư kinh doanh ở nước ngoài.
14. Hợp đồng hợp tác kinh doanh (sau đây gọi là hợp đồng BCC) là hợp đồng
được ký giữa các nhà đầu tư nhằm hợp tác kinh doanh, phân chia lợi nhuận, phân
chia sản phẩm theo quy định của pháp luật mà không thành lập tổ chức kinh tế.
15. Khu chế xuất là khu công nghiệp chuyên sản xuất hàng xuất khẩu, cung
ứng dịch vụ cho sản xuất hàng xuất khẩu và hoạt động xuất khẩu.
16. Khu công nghiệp là khu vực có ranh giới địa lý xác định, chuyên sản
xuất hàng công nghiệp và cung ứng dịch vụ cho sản xuất công nghiệp.
```
</details>

<details><summary>[B-ab5a5a7a520af026] trang 16-16, Điều 22</summary>

```text
Điều 22. Đầu tư theo hình thức hợp đồng BCC
1. Hợp đồng BCC được ký kết giữa các nhà đầu tư trong nước thực hiện theo
quy định của pháp luật về dân sự và pháp luật có liên quan.
2. Hợp đồng BCC được ký kết giữa nhà đầu tư trong nước với nhà đầu tư
nước ngoài hoặc giữa các nhà đầu tư nước ngoài thực hiện thủ tục cấp Giấy chứng
nhận đăng ký đầu tư theo quy định tại Điều 26 của Luật này.
3. Các bên tham gia hợp đồng BCC thành lập ban điều phối để thực hiện hợp
đồng BCC. Chức năng, nhiệm vụ, quyền hạn của ban điều phối do các bên thỏa thuận.
4. Trong quá trình thực hiện hợp đồng BCC, các bên tham gia hợp đồng
được thỏa thuận sử dụng tài sản hình thành từ việc hợp tác kinh doanh để thành lập
doanh nghiệp theo quy định của pháp luật về doanh nghiệp.
5. Chính phủ quy định về nội dung hợp đồng BCC.
```
</details>

<details><summary>[B-19128a8b6b25c365] trang 29-29, Điều 37</summary>

```text
Điều 37. Thành lập, điều chỉnh, chấm dứt hoạt động văn phòng điều
hành của nhà đầu tư nước ngoài trong hợp đồng BCC
1. Nhà đầu tư nước ngoài trong hợp đồng BCC được thành lập văn phòng điều
hành tại Việt Nam để thực hiện hợp đồng. Địa điểm văn phòng điều hành do nhà
đầu tư nước ngoài trong hợp đồng BCC quyết định theo yêu cầu thực hiện hợp đồng.
2. Văn phòng điều hành của nhà đầu tư nước ngoài trong hợp đồng BCC có
con dấu; được mở tài khoản, tuyển dụng lao động, ký hợp đồng và tiến hành các
hoạt động kinh doanh trong phạm vi quyền và nghĩa vụ quy định tại hợp đồng BCC
và Giấy chứng nhận đăng ký thành lập văn phòng điều hành.
3. Chính phủ quy định về hồ sơ, trình tự, thủ tục thành lập, điều chỉnh, chấm dứt
hoạt động của văn phòng điều hành của nhà đầu tư nước ngoài trong hợp đồng BCC.
```
</details>

## q13 — abstain (3 search, filter=None)

**Câu hỏi:** Với dự án thuộc diện chấp thuận chủ trương đầu tư, việc chấp thuận phải được thực hiện vào thời điểm nào?

**Đáp án chuẩn:** Trước khi nhà đầu tư thực hiện dự án đầu tư.

**Evidence gold (trang 22):** 1. Đối với dự án đầu tư thuộc diện chấp thuận chủ trương đầu tư, việc chấp thuận chủ trương đầu tư phải được thực hiện trước khi nhà đầu tư thực hiện dự án đầu tư.

*Tự động:* context có evidence = False, chunk được trích có evidence = False

**Truy vấn của agent:** thời điểm chấp thuận chủ trương đầu tư | chấp thuận chủ trương đầu tư trước khi giao đất, cho thuê đất, chuyển mục đích sử dụng đất | chấp thuận chủ trương đầu tư được thực hiện trước khi triển khai dự án đầu tư

**Câu trả lời của agent:**

> Không đủ bằng chứng trong tài liệu để trả lời.

**Lý do từ chối (model):** Tôi chưa tìm được quy định nào nói việc chấp thuận chủ trương đầu tư phải làm vào thời điểm nào, chẳng hạn trước khi giao đất, cho thuê đất hay trước khi triển khai dự án. Các đoạn tìm được chỉ nêu ba nội dung sau. Điều 25 quy định cơ quan nào có thẩm quyền chấp thuận: Quốc hội, Thủ tướng Chính phủ, hoặc Ban quản lý khu công nghiệp, khu chế xuất, khu công nghệ cao, khu kinh tế. Điều 25 khoản 5 giao Chính phủ quy định hồ sơ, trình tự, thủ tục chấp thuận. Điều 33 quy định thủ tục khi điều chỉnh dự án. Cũng không thấy đoạn nào của Điều 24 (danh mục dự án phải chấp thuận chủ trương đầu tư) hay các quy định chung về thời điểm thực hiện thủ tục. Tôi đã hết lượt tìm kiếm nên không thể trả lời chắc chắn.

## q14 — answered (1 search, filter=None)

**Câu hỏi:** Nhà đầu tư trúng đấu giá quyền sử dụng đất có phải ký quỹ bảo đảm thực hiện dự án không?

**Đáp án chuẩn:** Không. Đây là trường hợp được trừ khỏi nghĩa vụ ký quỹ/bảo lãnh ngân hàng.

**Evidence gold (trang 23):** cho phép chuyển mục đích sử dụng đất, trừ các trường hợp sau đây: a) Nhà đầu tư trúng đấu giá quyền sử dụng đất;

*Tự động:* context có evidence = True, chunk được trích có evidence = True

**Truy vấn của agent:** ký quỹ bảo đảm thực hiện dự án đầu tư trúng đấu giá quyền sử dụng đất

**Câu trả lời của agent:**

> Không. Theo Luật Đầu tư 143/2025/QH15, nhà đầu tư trúng đấu giá quyền sử dụng đất không phải ký quỹ bảo đảm thực hiện dự án đầu tư.
> 
> - **Nguyên tắc chung:** Nếu dự án có đề nghị Nhà nước giao đất, cho thuê đất hoặc cho phép chuyển mục đích sử dụng đất, nhà đầu tư phải ký quỹ hoặc có bảo lãnh ngân hàng về nghĩa vụ ký quỹ [B-9e8417206087b503].
> - **Ngoại lệ:** Luật liệt kê các trường hợp được miễn nghĩa vụ này. Trường hợp đầu tiên là nhà đầu tư trúng đấu giá quyền sử dụng đất (điểm a khoản 1 Điều 30) [B-9e8417206087b503].
> - **Các trường hợp miễn khác:**
>   - Nhà đầu tư trúng đấu thầu thực hiện dự án đầu tư có sử dụng đất [B-9e8417206087b503].
>   - Nhà đầu tư được giao đất, thuê đất do nhận chuyển nhượng một dự án đã ký quỹ, hoặc đã góp vốn, huy động vốn đúng tiến độ [B-9e8417206087b503].
>   - Nhà đầu tư được giao đất, thuê đất hoặc chuyển mục đích sử dụng đất do nhận chuyển nhượng quyền sử dụng đất, tài sản gắn liền với đất của người khác [B-9e8417206087b503].
>   - Nhà đầu tư trúng đấu giá quyền khai thác khoáng sản [B-9e8417206087b503].
> - **Lưu ý:** Chính phủ sẽ quy định chi tiết điều này [B-9e8417206087b503].

<details><summary>[B-9e8417206087b503] trang 23-23, Điều 30</summary>

```text
Điều 30. Bảo đảm thực hiện dự án đầu tư
1. Nhà đầu tư phải ký quỹ hoặc phải có bảo lãnh ngân hàng về nghĩa vụ ký
quỹ để bảo đảm thực hiện dự án đầu tư có đề nghị Nhà nước giao đất, cho thuê đất,
cho phép chuyển mục đích sử dụng đất, trừ các trường hợp sau đây:
a) Nhà đầu tư trúng đấu giá quyền sử dụng đất;
b) Nhà đầu tư trúng đấu thầu thực hiện dự án đầu tư có sử dụng đất;
c) Nhà đầu tư được Nhà nước giao đất, cho thuê đất trên cơ sở nhận chuyển
nhượng dự án đầu tư đã thực hiện ký quỹ hoặc đã hoàn thành việc góp vốn, huy
động vốn theo tiến độ quy định tại văn bản chấp thuận chủ trương đầu tư, Giấy
chứng nhận đăng ký đầu tư;
d) Nhà đầu tư được Nhà nước giao đất, cho thuê đất, chuyển mục đích sử
dụng đất (nếu có) để thực hiện dự án đầu tư trên cơ sở nhận chuyển nhượng quyền
sử dụng đất, tài sản gắn liền với đất của người sử dụng đất khác;
đ) Nhà đầu tư trúng đấu giá quyền khai thác khoáng sản.
2. Chính phủ quy định chi tiết Điều này.
```
</details>

## q15 — answered (1 search, filter=None)

**Câu hỏi:** Khi dự án phải ngừng hoạt động vì bất khả kháng, nhà đầu tư được Nhà nước hỗ trợ gì về đất?

**Đáp án chuẩn:** Được miễn tiền thuê đất, giảm tiền sử dụng đất trong thời gian ngừng hoạt động để khắc phục hậu quả do bất khả kháng.

**Evidence gold (trang 27):** Trường hợp ngừng hoạt động của dự án đầu tư vì lý do bất khả kháng thì nhà đầu tư được Nhà nước miễn tiền thuê đất, giảm tiền sử dụng đất trong thời gian ngừng hoạt động để khắc phục hậu quả do bất khả kháng gây ra.

*Tự động:* context có evidence = True, chunk được trích có evidence = True

**Truy vấn của agent:** ngừng hoạt động dự án đầu tư bất khả kháng miễn tiền thuê đất

**Câu trả lời của agent:**

> Theo Điều 35, khi dự án phải ngừng hoạt động vì lý do bất khả kháng, Nhà nước hỗ trợ nhà đầu tư về đất như sau [B-ec40f8d841582794]:
> - Miễn tiền thuê đất.
> - Giảm tiền sử dụng đất.
> 
> Hai khoản ưu đãi này chỉ áp dụng trong thời gian dự án ngừng hoạt động để khắc phục hậu quả do bất khả kháng gây ra [B-ec40f8d841582794].
> 
> Điều kiện kèm theo: khi ngừng hoạt động dự án, nhà đầu tư phải thông báo bằng văn bản cho cơ quan đăng ký đầu tư [B-ec40f8d841582794].

<details><summary>[B-ec40f8d841582794] trang 27-27, Điều 35</summary>

```text
Điều 35. Ngừng hoạt động của dự án đầu tư
1. Nhà đầu tư ngừng hoạt động của dự án đầu tư phải thông báo bằng văn bản
cho cơ quan đăng ký đầu tư. Trường hợp ngừng hoạt động của dự án đầu tư vì lý do
bất khả kháng thì nhà đầu tư được Nhà nước miễn tiền thuê đất, giảm tiền sử dụng
đất trong thời gian ngừng hoạt động để khắc phục hậu quả do bất khả kháng gây ra.
```
</details>

## q16 — answered (3 search, filter={'chapter': 'V'})

**Câu hỏi:** Nhà đầu tư phải tuân thủ những quy định nào khi thực hiện hoạt động đầu tư?

**Đáp án chuẩn:** Luật Đầu tư, quy định khác của pháp luật có liên quan, pháp luật của nước tiếp nhận đầu tư và điều ước quốc tế có liên quan; tự chịu trách nhiệm về hiệu quả đầu tư ở nước ngoài.

**Evidence gold (trang 29):** Nhà đầu tư thực hiện hoạt động đầu tư ra nước ngoài phải tuân thủ quy định của Luật này, quy định khác của pháp luật có liên quan, pháp luật của quốc gia, vùng lãnh thổ tiếp nhận đầu tư (sau đây gọi là nước tiếp nhận đầu tư) và điều ước quốc tế có liên quan;

*Tự động:* context có evidence = True, chunk được trích có evidence = True

**Truy vấn của agent:** nghĩa vụ của nhà đầu tư khi thực hiện hoạt động đầu tư | nguyên tắc thực hiện hoạt động đầu tư kinh doanh | áp dụng Luật Đầu tư và các luật có liên quan, điều ước quốc tế

**Câu trả lời của agent:**

> Tài liệu tìm được chỉ nêu quy định này cho **hoạt động đầu tư ra nước ngoài**. Tôi chưa tìm thấy quy định chung cho mọi hoạt động đầu tư, kể cả đầu tư trong nước.
> 
> Khi đầu tư ra nước ngoài, nhà đầu tư phải tuân thủ:
> 1. Luật Đầu tư [B-4941169e3efd28f4].
> 2. Các quy định khác của pháp luật có liên quan [B-4941169e3efd28f4].
> 3. Pháp luật của quốc gia hoặc vùng lãnh thổ nhận đầu tư (gọi là "nước tiếp nhận đầu tư") [B-4941169e3efd28f4].
> 4. Các điều ước quốc tế có liên quan [B-4941169e3efd28f4].
> 
> Nhà đầu tư cũng tự chịu trách nhiệm về hiệu quả hoạt động đầu tư ở nước ngoài [B-4941169e3efd28f4].
> 
> Nhà đầu tư còn phải tránh các ngành, nghề bị cấm đầu tư ra nước ngoài:
> - Ngành, nghề cấm đầu tư kinh doanh theo Điều 6 của Luật Đầu tư và theo các điều ước quốc tế có liên quan mà Việt Nam là thành viên [B-4679425b231441ae].
> - Ngành, nghề có công nghệ hoặc sản phẩm bị cấm xuất khẩu theo pháp luật về quản lý ngoại thương [B-4679425b231441ae].
> - Ngành, nghề bị cấm theo pháp luật của nước tiếp nhận đầu tư [B-4679425b231441ae].
> 
> Hoạt động đầu tư phải theo các hình thức luật cho phép, ví dụ:
> - Thành lập tổ chức kinh tế.
> - Đầu tư theo hợp đồng.
> - Góp vốn, mua cổ phần hoặc mua phần vốn góp.
> - Mua, bán chứng khoán [B-1887fa9bc4904616].
> 
> Ngoài ra, nhà đầu tư phải tuân thủ quy định của Chính phủ về:
> - Mở tài khoản và chuyển vốn đầu tư ra nước ngoài.
> - Sử dụng lợi nhuận ở nước ngoài và chuyển lợi nhuận về nước.
> - Triển khai hoạt động đầu tư ở nước ngoài [B-f79f725070650181].

<details><summary>[B-4941169e3efd28f4] trang 29-29, Điều 38</summary>

```text
Điều 38. Nguyên tắc thực hiện hoạt động đầu tư ra nước ngoài
1. Nhà nước khuyến khích đầu tư ra nước ngoài nhằm khai thác, phát triển,
mở rộng thị trường; tăng khả năng xuất khẩu hàng hóa, dịch vụ, thu ngoại tệ; tiếp
cận công nghệ hiện đại, nâng cao năng lực quản trị và bổ sung nguồn lực phát triển
kinh tế - xã hội của đất nước.
2. Nhà đầu tư thực hiện hoạt động đầu tư ra nước ngoài phải tuân thủ quy định
của Luật này, quy định khác của pháp luật có liên quan, pháp luật của quốc gia, vùng
lãnh thổ tiếp nhận đầu tư (sau đây gọi là nước tiếp nhận đầu tư) và điều ước quốc tế
có liên quan; tự chịu trách nhiệm về hiệu quả hoạt động đầu tư ở nước ngoài.
```
</details>

<details><summary>[B-4679425b231441ae] trang 30-30, Điều 40</summary>

```text
Điều 40. Ngành, nghề cấm đầu tư ra nước ngoài
1. Ngành, nghề cấm đầu tư kinh doanh quy định tại Điều 6 của Luật này và
các điều ước quốc tế có liên quan mà nước Cộng hòa xã hội chủ nghĩa Việt Nam
là thành viên.
2. Ngành, nghề có công nghệ, sản phẩm thuộc đối tượng cấm xuất khẩu theo
quy định của pháp luật về quản lý ngoại thương.
3. Ngành, nghề cấm đầu tư kinh doanh theo quy định của pháp luật nước
tiếp nhận đầu tư.
```
</details>

<details><summary>[B-1887fa9bc4904616] trang 29-30, Điều 39</summary>

```text
Điều 39. Hình thức đầu tư ra nước ngoài
1. Nhà đầu tư thực hiện hoạt động đầu tư ra nước ngoài theo các hình thức
sau đây:
a) Thành lập tổ chức kinh tế theo quy định của pháp luật nước tiếp nhận đầu tư;
b) Đầu tư theo hình thức hợp đồng ở nước ngoài;
c) Góp vốn, mua cổ phần, mua phần vốn góp của tổ chức kinh tế ở nước
ngoài để tham gia quản lý tổ chức kinh tế đó;
d) Mua, bán chứng khoán, giấy tờ có giá khác hoặc đầu tư thông qua các quỹ
đầu tư chứng khoán, các định chế tài chính trung gian khác ở nước ngoài;
đ) Các hình thức đầu tư khác theo quy định của pháp luật nước tiếp nhận đầu tư.
2. Chính phủ quy định chi tiết việc thực hiện hình thức đầu tư quy định tại
điểm d khoản 1 Điều này.
```
</details>

<details><summary>[B-f79f725070650181] trang 31-31, Điều 43</summary>

```text
Điều 43. Triển khai hoạt động đầu tư ở nước ngoài
Chính phủ quy định việc mở tài khoản vốn đầu tư ra nước ngoài, chuyển vốn
đầu tư ra nước ngoài, sử dụng lợi nhuận ở nước ngoài, chuyển lợi nhuận về nước
và việc triển khai hoạt động đầu tư ở nước ngoài.
```
</details>

## u01 — abstain (2 search, filter=None)

**Câu hỏi:** Lệ phí cấp Giấy chứng nhận đăng ký đầu tư là bao nhiêu tiền?

**Câu thiếu evidence.** Lý do: Luật có định nghĩa và thủ tục về Giấy chứng nhận đăng ký đầu tư (Điều 3 khoản 11 và nhiều điều khác) nhưng không quy định lệ phí hay mức thu nào cho việc cấp giấy này.

**Truy vấn của agent:** lệ phí cấp Giấy chứng nhận đăng ký đầu tư | phí, lệ phí thực hiện thủ tục đầu tư

**Câu trả lời của agent:**

> Không đủ bằng chứng trong tài liệu để trả lời.

**Lý do từ chối (model):** Tôi chưa tìm thấy mức lệ phí cấp Giấy chứng nhận đăng ký đầu tư trong Luật Đầu tư 143/2025/QH15 nên không thể nêu số tiền. Các đoạn tìm được chỉ nói về ba nội dung: (1) Dự án nào phải làm thủ tục cấp Giấy chứng nhận đăng ký đầu tư. Nếu thuộc diện không bắt buộc mà nhà đầu tư vẫn muốn có giấy thì cũng được làm thủ tục [B-ee1e89ea371943d8]. (2) Cơ quan có thẩm quyền cấp, điều chỉnh và thu hồi giấy là Ban quản lý các khu công nghiệp, khu chế xuất, khu công nghệ cao, khu kinh tế, hoặc Sở Tài chính đối với dự án ngoài các khu này [B-1456b3d32f36a55c]. (3) Chính phủ quy định điều kiện, hồ sơ, trình tự và thủ tục cấp giấy [B-ee1e89ea371943d8]. Không đoạn nào nêu khoản phí hay lệ phí, kể cả mức tiền cụ thể. Mức phí này có thể được quy định trong văn bản khác như nghị định hoặc thông tư hướng dẫn. Tuy vậy, tôi không xác minh được điều đó từ các đoạn đã tìm thấy.

## u02 — abstain (3 search, filter=None)

**Câu hỏi:** Nhà đầu tư chậm tiến độ thực hiện dự án đầu tư bị phạt tiền tối đa bao nhiêu?

**Câu thiếu evidence.** Lý do: Luật chỉ nhắc việc nhà đầu tư 'đã bị xử phạt vi phạm hành chính' như một điều kiện chấm dứt dự án (tr.27) và giao xử lý vi phạm cho quy định khác; không có mức phạt tiền.

**Truy vấn của agent:** chậm tiến độ thực hiện dự án đầu tư xử phạt | vi phạm tiến độ dự án đầu tư phạt tiền chấm dứt hoạt động | xử lý vi phạm hành chính mức phạt tiền nhà đầu tư không đáp ứng tiến độ

**Câu trả lời của agent:**

> Không đủ bằng chứng trong tài liệu để trả lời.

**Lý do từ chối (model):** Tôi đã tìm 3 lần nhưng không thấy mức phạt tiền tối đa khi nhà đầu tư chậm tiến độ thực hiện dự án đầu tư. Các đoạn tìm được chỉ nói về việc điều chỉnh tiến độ: dự án đã được chấp thuận chủ trương đầu tư không được kéo dài tiến độ quá 24 tháng so với văn bản chấp thuận lần đầu, trừ một số trường hợp ngoại lệ (Điều 33). Ngoài ra còn có quy định về thời hạn hoạt động và gia hạn dự án (Điều 31). Không đoạn nào nói về xử phạt hay số tiền phạt cụ thể. Có thể mức phạt nằm ở văn bản khác về xử phạt vi phạm hành chính trong lĩnh vực đầu tư, nhưng tài liệu tôi tra được không xác nhận điều này.

## u03 — abstain (3 search, filter=None)

**Câu hỏi:** Dự án đầu tư trong khu kinh tế được áp dụng thuế suất thuế thu nhập doanh nghiệp ưu đãi bao nhiêu phần trăm?

**Câu thiếu evidence.** Lý do: Luật chỉ nêu hình thức ưu đãi là 'thuế suất thấp hơn mức thuế suất thông thường' (tr.10) và dẫn chiếu Luật Thuế thu nhập doanh nghiệp (tr.14); không có con số thuế suất.

**Truy vấn của agent:** ưu đãi đầu tư khu kinh tế thuế suất thuế thu nhập doanh nghiệp | đối tượng được hưởng ưu đãi đầu tư địa bàn khu kinh tế | mức thuế suất ưu đãi dự án tại khu kinh tế, khu công nghệ cao

**Câu trả lời của agent:**

> Không đủ bằng chứng trong tài liệu để trả lời.

**Lý do từ chối (model):** Luật Đầu tư 143/2025/QH15, trong các đoạn đã tìm được, không nêu mức thuế suất thuế thu nhập doanh nghiệp ưu đãi (bao nhiêu phần trăm) cho dự án trong khu kinh tế. Các đoạn này chỉ cho biết: (1) một hình thức ưu đãi đầu tư là áp dụng thuế suất thuế thu nhập doanh nghiệp thấp hơn mức thông thường, có thời hạn hoặc trong toàn bộ thời gian thực hiện dự án, và được miễn, giảm thuế theo pháp luật về thuế thu nhập doanh nghiệp [B-abc6aedc04ad763f]; (2) mức ưu đãi và thời hạn áp dụng ưu đãi đặc biệt thực hiện theo Luật Thuế thu nhập doanh nghiệp và pháp luật về đất đai [B-04a63a3ffbc548e9]. Đã hết lượt tìm kiếm. Con số cụ thể cần tra trong Luật Thuế thu nhập doanh nghiệp số 67/2025/QH15 và các văn bản hướng dẫn.

