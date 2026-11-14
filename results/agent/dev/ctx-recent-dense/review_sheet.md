# Review sheet — dev / ctx-recent-dense

Chấm theo BENCHMARK.md: `answer_grade` 0 = sai/thiếu evidence, 1 = đúng một phần, 2 = đúng và đủ (từ chối câu có đáp án = 0); `citation_support`: mỗi citation có thực sự hỗ trợ ý được trích không; `abstention_correct`: câu thiếu evidence có được từ chối mà không thêm khẳng định vô căn cứ không.

## q01 — answered (1 search, filter=None)

**Câu hỏi:** Thời hạn hoạt động tối đa của dự án đầu tư trong khu kinh tế là bao lâu?

**Đáp án chuẩn:** Không quá 70 năm.

**Evidence gold (trang 23):** Thời hạn hoạt động của dự án đầu tư trong khu kinh tế không quá 70 năm.

*Tự động:* context có evidence = True, chunk được trích có evidence = True

**Truy vấn của agent:** thời hạn hoạt động của dự án đầu tư trong khu kinh tế

**Câu trả lời của agent:**

> Theo Luật Đầu tư 143/2025/QH15, dự án đầu tư trong khu kinh tế được hoạt động **tối đa 70 năm** [B-0288b0e0f7ba0af3].
> 
> Một số điểm liên quan:
> - **Thời gian bị chậm không tính vào thời hạn:** Nếu tiến độ hoặc thời hạn hoạt động bị ảnh hưởng bởi các trường hợp tại các điểm a, b, c, d và g khoản 4 Điều 33, thời gian chậm đó không bị tính vào thời hạn hoạt động [B-0288b0e0f7ba0af3].
> - **Điều chỉnh thời hạn:** Trong quá trình thực hiện dự án, nhà đầu tư được tăng hoặc giảm thời hạn hoạt động. Sau khi điều chỉnh, thời hạn vẫn không được quá mức tối đa nêu trên [B-e7304ebd3af27c91].
> - **Gia hạn khi hết thời hạn:** Nếu nhà đầu tư muốn tiếp tục và đáp ứng điều kiện pháp luật, dự án được xem xét gia hạn. Mỗi lần gia hạn không quá thời hạn tối đa nêu trên [B-e7304ebd3af27c91].
> - **Trường hợp không được gia hạn:** (a) dự án dùng công nghệ lạc hậu, có nguy cơ gây ô nhiễm môi trường hoặc thâm dụng tài nguyên; (b) dự án mà nhà đầu tư phải chuyển giao tài sản không bồi hoàn cho Nhà nước Việt Nam hoặc bên Việt Nam [B-e7304ebd3af27c91].

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

> Theo nguyên tắc chung, một dự án đầu tư nằm ngoài khu kinh tế được hoạt động **tối đa 50 năm** [B-0288b0e0f7ba0af3].
> 
> **Khi nào được tới 70 năm:** Thời hạn có thể dài hơn 50 năm nhưng không quá 70 năm nếu dự án thuộc một trong các trường hợp sau [B-0288b0e0f7ba0af3]:
> - Thực hiện tại địa bàn có điều kiện kinh tế - xã hội khó khăn hoặc đặc biệt khó khăn.
> - Có vốn đầu tư lớn nhưng thu hồi vốn chậm.
> - Xây dựng và kinh doanh kết cấu hạ tầng khu công nghệ cao, khu công nghiệp công nghệ cao, khu công nghệ số tập trung.
> - Thuộc diện ưu đãi, hỗ trợ đầu tư đặc biệt theo khoản 2 Điều 17.
> 
> **Những điểm cần lưu ý thêm:**
> - Nếu tiến độ bị chậm do các trường hợp tại các điểm a, b, c, d và g khoản 4 Điều 33, thời gian chậm đó không tính vào thời hạn hoạt động [B-0288b0e0f7ba0af3].
> - Nhà đầu tư được điều chỉnh tăng hoặc giảm thời hạn, nhưng sau khi điều chỉnh vẫn không được vượt mức tối đa nêu trên [B-e7304ebd3af27c91].
> - Khi hết thời hạn, dự án có thể được xem xét gia hạn nếu nhà đầu tư có nhu cầu và đáp ứng điều kiện. Mỗi lần gia hạn cũng không quá mức tối đa nêu trên [B-e7304ebd3af27c91].
> - Không được gia hạn nếu dự án dùng công nghệ lạc hậu, có nguy cơ gây ô nhiễm môi trường, thâm dụng tài nguyên, hoặc nhà đầu tư phải chuyển giao tài sản không bồi hoàn cho Nhà nước Việt Nam hoặc bên Việt Nam [B-e7304ebd3af27c91].

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

> Không. Theo Luật Đầu tư 143/2025/QH15, tài sản hợp pháp của nhà đầu tư không bị quốc hữu hóa hoặc bị tịch thu bằng biện pháp hành chính [B-2bc6a34e63543c75]. Nhà nước công nhận và bảo hộ quyền sở hữu về tài sản, vốn đầu tư, thu nhập và các quyền, lợi ích hợp pháp khác của nhà đầu tư [B-0d831dd4fbfc1eb9].
> 
> Có một trường hợp cần lưu ý: Nhà nước có thể trưng mua hoặc trưng dụng tài sản vì lý do quốc phòng, an ninh, lợi ích quốc gia, tình trạng khẩn cấp hoặc phòng, chống thiên tai. Khi đó, nhà đầu tư được thanh toán và bồi thường theo pháp luật về trưng mua, trưng dụng tài sản và các quy định pháp luật khác có liên quan [B-2bc6a34e63543c75].

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

> Nhà đầu tư nước ngoài cần đáp ứng một điều kiện: **thực hiện đầy đủ nghĩa vụ tài chính đối với Nhà nước Việt Nam** theo quy định của pháp luật. Khi đã làm xong, họ được chuyển ra nước ngoài các tài sản sau [B-0b6f226d8638bc81]:
> 1. Vốn đầu tư và các khoản thanh lý đầu tư;
> 2. Thu nhập từ hoạt động đầu tư kinh doanh;
> 3. Tiền và tài sản khác thuộc sở hữu hợp pháp của nhà đầu tư.
> 
> Lưu ý: Điều 43 nói về việc chuyển vốn khi đầu tư ra nước ngoài, là trường hợp khác. Theo điều này, Chính phủ quy định việc mở tài khoản vốn đầu tư ra nước ngoài và chuyển vốn đầu tư ra nước ngoài [B-f79f725070650181].

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

> Có. Theo Luật Đầu tư 143/2025/QH15, tranh chấp này có thể được giải quyết tại Trọng tài nước ngoài.
> 
> - **Trước hết phải thương lượng, hòa giải:** Tranh chấp liên quan đến hoạt động đầu tư kinh doanh tại Việt Nam được giải quyết thông qua thương lượng, hòa giải. Nếu không thương lượng, hòa giải được thì mới đưa ra Trọng tài hoặc Tòa án [B-24ba71437a3919fc].
> - **Các nơi có thể giải quyết:** Tranh chấp giữa các nhà đầu tư mà có ít nhất một bên là nhà đầu tư nước ngoài được giải quyết tại một trong các cơ quan, tổ chức sau [B-24ba71437a3919fc]:
>   a) Tòa án Việt Nam;
>   b) Trọng tài Việt Nam;
>   c) Trọng tài nước ngoài;
>   d) Trọng tài quốc tế;
>   đ) Trọng tài do các bên tranh chấp thỏa thuận thành lập.
> - **Cũng áp dụng cho một số tổ chức kinh tế:** Quy định này áp dụng cả khi một bên là tổ chức kinh tế nêu tại các điểm a, b và c khoản 1 Điều 20 của Luật [B-24ba71437a3919fc].
> - **Khác với tranh chấp với cơ quan nhà nước:** Nếu tranh chấp là giữa nhà đầu tư nước ngoài với cơ quan nhà nước có thẩm quyền, thì về nguyên tắc được giải quyết tại Trọng tài Việt Nam hoặc Tòa án Việt Nam. Ngoại lệ là khi hợp đồng có thỏa thuận khác, hoặc điều ước quốc tế mà Việt Nam là thành viên có quy định khác [B-ef9489fe04774cc0].

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

> Có. Kinh doanh dịch vụ đòi nợ thuộc ngành, nghề cấm đầu tư kinh doanh. Điểm h khoản 1 Điều 6 Luật Đầu tư 143/2025/QH15 cấm hoạt động này [B-598fa8ff504ec744].
> 
> Ngoài ra, các ngành, nghề bị cấm theo Điều 6 cũng không được đầu tư ra nước ngoài (khoản 1 Điều 40) [B-4679425b231441ae].

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

> **Cơ quan lập Quỹ:** Chính phủ là cơ quan thành lập Quỹ Hỗ trợ đầu tư [B-97c34c9fccf0514f].
> 
> **Mục đích của Quỹ:**
> - Ổn định môi trường đầu tư.
> - Khuyến khích và thu hút nhà đầu tư chiến lược, tập đoàn đa quốc gia.
> - Hỗ trợ doanh nghiệp trong nước trong một số lĩnh vực cần khuyến khích đầu tư. [B-97c34c9fccf0514f]
> 
> **Quy định chi tiết:** Chính phủ quy định chi tiết các nội dung sau của Quỹ:
> - Mô hình hoạt động và địa vị pháp lý.
> - Nguồn ngân sách cấp hằng năm và bổ sung cho Quỹ.
> - Hình thức hỗ trợ và cơ chế bồi hoàn hỗ trợ.
> - Các chính sách đặc thù khác.
> 
> Trước khi ban hành các quy định này, Chính phủ phải báo cáo Ủy ban Thường vụ Quốc hội cho ý kiến [B-97c34c9fccf0514f].

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
> 1. Đầu tư thành lập tổ chức kinh tế [B-9462dc6128622f7a].
> 2. Đầu tư góp vốn, mua cổ phần, mua phần vốn góp [B-9462dc6128622f7a].
> 3. Thực hiện dự án đầu tư [B-9462dc6128622f7a].
> 4. Đầu tư theo hình thức hợp đồng BCC [B-9462dc6128622f7a].
> 5. Các hình thức đầu tư, loại hình tổ chức kinh tế mới theo quy định của Chính phủ [B-9462dc6128622f7a].
> 
> Điều kiện riêng đối với hình thức góp vốn, mua cổ phần, mua phần vốn góp:
> - Nhà đầu tư có quyền góp vốn, mua cổ phần, mua phần vốn góp của tổ chức kinh tế [B-2a38b8fa7e90b581].
> - Nếu là nhà đầu tư nước ngoài, phải đáp ứng 3 điều kiện [B-2a38b8fa7e90b581]:
>   + Điều kiện tiếp cận thị trường đối với nhà đầu tư nước ngoài theo Điều 8 [B-2a38b8fa7e90b581].
>   + Bảo đảm quốc phòng, an ninh [B-2a38b8fa7e90b581].
>   + Quy định của pháp luật đất đai về điều kiện nhận quyền sử dụng đất và điều kiện sử dụng đất tại đảo; xã, phường, đặc khu khu vực biên giới; xã, phường ven biển [B-2a38b8fa7e90b581].
> - Chính phủ sẽ quy định cụ thể cách góp vốn, mua cổ phần, mua phần vốn góp, cùng hồ sơ, trình tự và thủ tục thực hiện [B-93781a19d12412a9].

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

**Truy vấn của agent:** ngành, nghề đầu tư kinh doanh có điều kiện | Danh mục ngành, nghề đầu tư kinh doanh có điều kiện Điều 7 | hoạt động đầu tư kinh doanh phải đáp ứng điều kiện vì lý do quốc phòng, an ninh quốc gia, trật tự an toàn xã hội

**Câu trả lời của agent:**

> Các đoạn luật tìm được chỉ nêu danh sách ngành, nghề **đầu tư ra nước ngoài** có điều kiện. Chúng không có danh mục ngành, nghề đầu tư kinh doanh có điều kiện nói chung (đầu tư trong nước). Vì vậy, tôi chỉ trả lời được phần đầu tư ra nước ngoài.
> 
> **Ngành, nghề đầu tư ra nước ngoài có điều kiện (khoản 1 Điều 41):**
> a) Ngân hàng;
> b) Bảo hiểm;
> c) Chứng khoán;
> d) Báo chí, phát thanh, truyền hình;
> đ) Kinh doanh bất động sản. [B-30b81c76d49df66f]
> 
> **Điều kiện áp dụng cho các ngành, nghề này** được quy định ở các văn bản sau: luật, nghị quyết của Quốc hội, pháp lệnh, nghị quyết của Ủy ban Thường vụ Quốc hội, nghị định của Chính phủ và điều ước quốc tế về đầu tư mà Việt Nam là thành viên. [B-30b81c76d49df66f]
> 
> **Hệ quả về thủ tục:** Thông thường, dự án đầu tư ra nước ngoài có vốn nhỏ hơn mức Chính phủ quy định chỉ cần đăng ký giao dịch ngoại hối. Khi đó nhà đầu tư không phải xin Giấy chứng nhận đăng ký đầu tư ra nước ngoài. Tuy nhiên, ngoại lệ này không áp dụng nếu dự án thuộc các ngành, nghề có điều kiện nêu trên. [B-67bca7e9097c9c87]
> 
> **Để phân biệt:** Ngành, nghề **cấm** đầu tư ra nước ngoài là một nhóm khác (Điều 40). Nhóm này gồm:
> - ngành, nghề cấm đầu tư kinh doanh theo Điều 6 Luật này và các điều ước quốc tế liên quan;
> - ngành, nghề có công nghệ, sản phẩm bị cấm xuất khẩu;
> - ngành, nghề bị cấm theo pháp luật của nước tiếp nhận đầu tư. [B-4679425b231441ae]

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

**Truy vấn của agent:** hợp đồng BCC ký kết giữa các nhà đầu tư trong nước

**Câu trả lời của agent:**

> Hợp đồng BCC ký giữa các nhà đầu tư trong nước được thực hiện theo quy định của pháp luật về dân sự và pháp luật có liên quan [B-ab5a5a7a520af026].
> 
> Để phân biệt: hợp đồng BCC ký giữa nhà đầu tư trong nước với nhà đầu tư nước ngoài, hoặc giữa các nhà đầu tư nước ngoài, thì phải làm thủ tục cấp Giấy chứng nhận đăng ký đầu tư theo Điều 26 của Luật Đầu tư [B-ab5a5a7a520af026].
> 
> Hợp đồng BCC là hợp đồng ký giữa các nhà đầu tư để hợp tác kinh doanh, chia lợi nhuận hoặc chia sản phẩm theo quy định của pháp luật mà không thành lập tổ chức kinh tế [B-22a114fa9d26e013].
> 
> Một số quy định chung cho hợp đồng BCC:
> - Các bên lập ban điều phối để thực hiện hợp đồng. Chức năng, nhiệm vụ và quyền hạn của ban này do các bên thỏa thuận [B-ab5a5a7a520af026].
> - Các bên được thỏa thuận dùng tài sản hình thành từ việc hợp tác kinh doanh để thành lập doanh nghiệp theo pháp luật về doanh nghiệp [B-ab5a5a7a520af026].
> - Nội dung hợp đồng BCC do Chính phủ quy định [B-ab5a5a7a520af026].

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

> Theo Luật Đầu tư 143/2025/QH15:
> 
> 1. **Thủ tục bắt buộc là xin cấp Giấy chứng nhận đăng ký đầu tư.** Quy định này áp dụng khi hợp đồng BCC được ký giữa nhà đầu tư trong nước với nhà đầu tư nước ngoài, hoặc giữa các nhà đầu tư nước ngoài với nhau. Thủ tục thực hiện theo Điều 26 [B-ab5a5a7a520af026]. Điều 26 cũng xếp dự án đầu tư của nhà đầu tư nước ngoài vào diện phải làm thủ tục này [B-ee1e89ea371943d8].
>    - Nếu hợp đồng BCC chỉ ký giữa các nhà đầu tư trong nước thì không cần thủ tục trên. Hợp đồng chỉ thực hiện theo pháp luật về dân sự và pháp luật liên quan [B-ab5a5a7a520af026].
>    - Điều kiện, hồ sơ, trình tự, thủ tục cấp và điều chỉnh, cũng như nội dung Giấy chứng nhận đăng ký đầu tư, do Chính phủ quy định [B-ee1e89ea371943d8]. Luật này không nêu chi tiết hồ sơ hay thời hạn.
> 
> 2. **Các bên phải thành lập ban điều phối** để thực hiện hợp đồng BCC. Chức năng, nhiệm vụ và quyền hạn của ban này do các bên tự thỏa thuận [B-ab5a5a7a520af026].
> 
> 3. **Nhà đầu tư nước ngoài có thể (không bắt buộc) lập văn phòng điều hành tại Việt Nam** để thực hiện hợp đồng. Địa điểm do nhà đầu tư nước ngoài tự quyết định theo yêu cầu thực hiện hợp đồng. Văn phòng có con dấu, được mở tài khoản, tuyển lao động, ký hợp đồng và kinh doanh trong phạm vi hợp đồng BCC và Giấy chứng nhận đăng ký thành lập văn phòng điều hành. Hồ sơ, trình tự, thủ tục thành lập, điều chỉnh và chấm dứt hoạt động văn phòng do Chính phủ quy định [B-19128a8b6b25c365].
> 
> 4. **Nội dung hợp đồng BCC cũng do Chính phủ quy định** [B-ab5a5a7a520af026].

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

> Đó là **hợp đồng hợp tác kinh doanh (hợp đồng BCC)**. Đây là hợp đồng ký giữa các nhà đầu tư để hợp tác kinh doanh, chia lợi nhuận và chia sản phẩm theo quy định của pháp luật mà không lập tổ chức kinh tế [B-22a114fa9d26e013].
> 
> Một số điểm cần lưu ý:
> - **Thủ tục tùy theo các bên ký:** Nếu chỉ có nhà đầu tư trong nước ký với nhau, hợp đồng thực hiện theo pháp luật về dân sự và pháp luật liên quan. Nếu nhà đầu tư trong nước ký với nhà đầu tư nước ngoài, hoặc các nhà đầu tư nước ngoài ký với nhau, thì phải làm thủ tục cấp Giấy chứng nhận đăng ký đầu tư theo Điều 26 [B-ab5a5a7a520af026].
> - **Ban điều phối:** Các bên lập ban điều phối để thực hiện hợp đồng. Chức năng, nhiệm vụ và quyền hạn của ban này do các bên tự thỏa thuận [B-ab5a5a7a520af026].
> - **Lập doanh nghiệp sau này:** Trong quá trình thực hiện hợp đồng, các bên có thể thỏa thuận dùng tài sản hình thành từ việc hợp tác để lập doanh nghiệp theo pháp luật về doanh nghiệp [B-ab5a5a7a520af026].
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

## q13 — answered (3 search, filter=None)

**Câu hỏi:** Với dự án thuộc diện chấp thuận chủ trương đầu tư, việc chấp thuận phải được thực hiện vào thời điểm nào?

**Đáp án chuẩn:** Trước khi nhà đầu tư thực hiện dự án đầu tư.

**Evidence gold (trang 22):** 1. Đối với dự án đầu tư thuộc diện chấp thuận chủ trương đầu tư, việc chấp thuận chủ trương đầu tư phải được thực hiện trước khi nhà đầu tư thực hiện dự án đầu tư.

*Tự động:* context có evidence = True, chunk được trích có evidence = True

**Truy vấn của agent:** thời điểm chấp thuận chủ trương đầu tư | chấp thuận chủ trương đầu tư trước khi giao đất, cho thuê đất, chấp thuận nhà đầu tư | dự án đầu tư thuộc diện chấp thuận chủ trương đầu tư được thực hiện trước khi

**Câu trả lời của agent:**

> Với dự án thuộc diện chấp thuận chủ trương đầu tư, việc chấp thuận phải được thực hiện **trước khi nhà đầu tư thực hiện dự án** [B-47d122394db119d3].
> 
> Liên quan đến việc chọn nhà đầu tư: nếu chọn bằng đấu giá quyền sử dụng đất hoặc đấu thầu lựa chọn nhà đầu tư, việc lựa chọn được tiến hành **sau khi** đã chấp thuận chủ trương đầu tư. Ngoại lệ là dự án không thuộc diện chấp thuận chủ trương đầu tư [B-ea1e0977de0c98c6].
> 
> Trong quá trình triển khai, nhà đầu tư phải tuân thủ văn bản chấp thuận chủ trương đầu tư (nếu có) [B-47d122394db119d3].

<details><summary>[B-47d122394db119d3] trang 22-23, Điều 29</summary>

```text
Điều 29. Nguyên tắc thực hiện dự án đầu tư
1. Đối với dự án đầu tư thuộc diện chấp thuận chủ trương đầu tư, việc chấp
thuận chủ trương đầu tư phải được thực hiện trước khi nhà đầu tư thực hiện dự
án đầu tư.
2. Đối với dự án đầu tư thuộc diện cấp Giấy chứng nhận đăng ký đầu tư, nhà
đầu tư có trách nhiệm thực hiện thủ tục cấp Giấy chứng nhận đăng ký đầu tư trước
khi thực hiện dự án đầu tư.
3. Nhà đầu tư có trách nhiệm tuân thủ quy định của Luật này, pháp luật về
quy hoạch, đất đai, môi trường, xây dựng, lao động, phòng cháy và chữa cháy, quy
định khác của pháp luật có liên quan, văn bản chấp thuận chủ trương đầu tư (nếu
có) và Giấy chứng nhận đăng ký đầu tư (nếu có) trong quá trình triển khai thực
hiện dự án đầu tư.
```
</details>

<details><summary>[B-ea1e0977de0c98c6] trang 17-17, Điều 23</summary>

```text
Điều 23. Lựa chọn nhà đầu tư thực hiện dự án đầu tư
1. Lựa chọn nhà đầu tư được tiến hành thông qua một trong các hình thức sau đây:
a) Đấu giá quyền sử dụng đất theo quy định của pháp luật về đất đai;
b) Đấu thầu lựa chọn nhà đầu tư theo quy định của pháp luật về đấu thầu;
c) Chấp thuận nhà đầu tư theo quy định tại khoản 3 và khoản 4 Điều này.
2. Việc lựa chọn nhà đầu tư thực hiện dự án đầu tư theo quy định tại điểm a
và điểm b khoản 1 Điều này được thực hiện sau khi chấp thuận chủ trương đầu tư,
trừ trường hợp dự án đầu tư không thuộc diện chấp thuận chủ trương đầu tư.
3. Cơ quan có thẩm quyền thực hiện thủ tục chấp thuận nhà đầu tư trong các
trường hợp sau đây:
a) Đấu giá quyền sử dụng đất hai lần không thành theo quy định của Luật
Đất đai;
b) Chỉ có một nhà đầu tư đáp ứng điều kiện mời quan tâm trong trường hợp
pháp luật quản lý ngành, lĩnh vực quy định xác định số lượng nhà đầu tư quan tâm
khi thực hiện thủ tục lựa chọn nhà đầu tư.
```
</details>

## q14 — answered (1 search, filter=None)

**Câu hỏi:** Nhà đầu tư trúng đấu giá quyền sử dụng đất có phải ký quỹ bảo đảm thực hiện dự án không?

**Đáp án chuẩn:** Không. Đây là trường hợp được trừ khỏi nghĩa vụ ký quỹ/bảo lãnh ngân hàng.

**Evidence gold (trang 23):** cho phép chuyển mục đích sử dụng đất, trừ các trường hợp sau đây: a) Nhà đầu tư trúng đấu giá quyền sử dụng đất;

*Tự động:* context có evidence = True, chunk được trích có evidence = True

**Truy vấn của agent:** ký quỹ bảo đảm thực hiện dự án đầu tư trúng đấu giá quyền sử dụng đất

**Câu trả lời của agent:**

> Không. Nhà đầu tư trúng đấu giá quyền sử dụng đất không phải ký quỹ để bảo đảm thực hiện dự án đầu tư.
> 
> - **Quy định chung:** Dự án đầu tư có đề nghị Nhà nước giao đất, cho thuê đất hoặc cho phép chuyển mục đích sử dụng đất thì nhà đầu tư phải ký quỹ, hoặc có bảo lãnh ngân hàng về nghĩa vụ ký quỹ [B-9e8417206087b503].
> - **Trường hợp được miễn:** Luật liệt kê các trường hợp không phải ký quỹ. Trường hợp đầu tiên (điểm a khoản 1 Điều 30) là nhà đầu tư trúng đấu giá quyền sử dụng đất [B-9e8417206087b503].
> - **Các trường hợp miễn khác cùng khoản:**
>   - Nhà đầu tư trúng đấu thầu thực hiện dự án có sử dụng đất.
>   - Nhà đầu tư nhận chuyển nhượng dự án đã ký quỹ, hoặc dự án đã hoàn thành góp vốn, huy động vốn theo tiến độ.
>   - Nhà đầu tư nhận chuyển nhượng quyền sử dụng đất, tài sản gắn liền với đất của người khác.
>   - Nhà đầu tư trúng đấu giá quyền khai thác khoáng sản [B-9e8417206087b503].
> - **Hướng dẫn chi tiết:** Chính phủ quy định chi tiết Điều 30 [B-9e8417206087b503].

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

> Khi dự án đầu tư phải ngừng hoạt động vì bất khả kháng, Nhà nước hỗ trợ nhà đầu tư hai điều về đất:
> - Miễn tiền thuê đất.
> - Giảm tiền sử dụng đất.
> 
> Hai ưu đãi này chỉ áp dụng trong thời gian dự án ngừng hoạt động để khắc phục hậu quả do bất khả kháng gây ra. [B-ec40f8d841582794]
> 
> Nhà đầu tư cũng phải thông báo bằng văn bản cho cơ quan đăng ký đầu tư về việc ngừng hoạt động. [B-ec40f8d841582794]

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

**Truy vấn của agent:** nghĩa vụ của nhà đầu tư khi thực hiện hoạt động đầu tư | nguyên tắc thực hiện hoạt động đầu tư kinh doanh | nhà đầu tư có quyền thực hiện hoạt động đầu tư kinh doanh trong các ngành, nghề mà Luật này không cấm

**Câu trả lời của agent:**

> Các đoạn luật tìm được chỉ nói về đầu tư ra nước ngoài. Tôi không tìm thấy quy định chung cho hoạt động đầu tư trong nước, nên câu trả lời dưới đây chỉ áp dụng cho đầu tư ra nước ngoài.
> 
> 1. **Quy định phải tuân thủ:** Nhà đầu tư phải tuân thủ Luật Đầu tư, các luật liên quan khác, pháp luật của nước hoặc vùng lãnh thổ nhận đầu tư và các điều ước quốc tế liên quan. Nhà đầu tư cũng tự chịu trách nhiệm về hiệu quả đầu tư ở nước ngoài [B-4941169e3efd28f4].
> 
> 2. **Ngành, nghề bị cấm đầu tư ra nước ngoài:**
>    - Ngành, nghề bị cấm theo Điều 6 Luật Đầu tư và theo điều ước quốc tế mà Việt Nam tham gia.
>    - Ngành, nghề có công nghệ hoặc sản phẩm bị cấm xuất khẩu theo pháp luật về quản lý ngoại thương.
>    - Ngành, nghề bị cấm theo pháp luật của nước nhận đầu tư [B-4679425b231441ae].
> 
> 3. **Ngành, nghề phải đáp ứng điều kiện:** Ngân hàng, bảo hiểm, chứng khoán, báo chí - phát thanh - truyền hình và kinh doanh bất động sản. Điều kiện cụ thể nằm trong luật, nghị quyết của Quốc hội, pháp lệnh, nghị quyết của Ủy ban Thường vụ Quốc hội, nghị định của Chính phủ và điều ước quốc tế về đầu tư mà Việt Nam tham gia [B-30b81c76d49df66f].
> 
> 4. **Hình thức đầu tư được phép:**
>    - Thành lập tổ chức kinh tế theo pháp luật nước nhận đầu tư.
>    - Đầu tư theo hợp đồng ở nước ngoài.
>    - Góp vốn, mua cổ phần hoặc phần vốn góp để tham gia quản lý tổ chức kinh tế ở nước ngoài.
>    - Mua, bán chứng khoán, giấy tờ có giá, hoặc đầu tư qua quỹ đầu tư chứng khoán và các định chế tài chính trung gian khác ở nước ngoài. Chính phủ quy định chi tiết cho hình thức này.
>    - Các hình thức khác theo pháp luật nước nhận đầu tư [B-1887fa9bc4904616].
> 
> 5. **Triển khai đầu tư:** Chính phủ quy định việc mở tài khoản vốn đầu tư ra nước ngoài, chuyển vốn ra nước ngoài, sử dụng và chuyển lợi nhuận về nước, cũng như cách triển khai hoạt động đầu tư ở nước ngoài [B-f79f725070650181].

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

## u01 — abstain (3 search, filter=None)

**Câu hỏi:** Lệ phí cấp Giấy chứng nhận đăng ký đầu tư là bao nhiêu tiền?

**Câu thiếu evidence.** Lý do: Luật có định nghĩa và thủ tục về Giấy chứng nhận đăng ký đầu tư (Điều 3 khoản 11 và nhiều điều khác) nhưng không quy định lệ phí hay mức thu nào cho việc cấp giấy này.

**Truy vấn của agent:** lệ phí cấp Giấy chứng nhận đăng ký đầu tư | phí, lệ phí thực hiện thủ tục đầu tư | mức thu lệ phí đăng ký đầu tư

**Câu trả lời của agent:**

> Không đủ bằng chứng trong tài liệu để trả lời.

**Lý do từ chối (model):** Tôi chưa tìm thấy mức lệ phí cấp Giấy chứng nhận đăng ký đầu tư trong các đoạn của Luật Đầu tư 143/2025/QH15 đã tra được. Các đoạn này chỉ nêu những nội dung sau: dự án nào phải làm thủ tục cấp Giấy chứng nhận đăng ký đầu tư (Điều 26), cơ quan nào có thẩm quyền cấp (Điều 27) và thủ tục đầu tư đặc biệt (Điều 28). Điều 26 khoản 5 có giao Chính phủ quy định điều kiện, hồ sơ, trình tự, thủ tục cấp Giấy chứng nhận, nhưng không nhắc đến lệ phí. Tôi đã thử 3 cách tìm khác nhau mà không ra số tiền, nên không thể nêu một con số cụ thể.

## u02 — abstain (3 search, filter=None)

**Câu hỏi:** Nhà đầu tư chậm tiến độ thực hiện dự án đầu tư bị phạt tiền tối đa bao nhiêu?

**Câu thiếu evidence.** Lý do: Luật chỉ nhắc việc nhà đầu tư 'đã bị xử phạt vi phạm hành chính' như một điều kiện chấm dứt dự án (tr.27) và giao xử lý vi phạm cho quy định khác; không có mức phạt tiền.

**Truy vấn của agent:** xử phạt chậm tiến độ thực hiện dự án đầu tư | mức phạt tiền vi phạm hành chính lĩnh vực đầu tư | nhà đầu tư không thực hiện đúng tiến độ dự án bị phạt tiền

**Câu trả lời của agent:**

> Không đủ bằng chứng trong tài liệu để trả lời.

**Lý do từ chối (model):** Các đoạn Luật Đầu tư 143/2025/QH15 tìm được không nêu mức phạt tiền tối đa khi nhà đầu tư chậm tiến độ dự án. Luật chỉ có quy định về điều chỉnh tiến độ: dự án được chấp thuận chủ trương đầu tư không được điều chỉnh tiến độ quá 24 tháng, trừ một số trường hợp [B-74be6ac4f631b6d2]. Luật cũng quy định các trường hợp ngừng hoạt động dự án, trong đó trường hợp không đúng tiến độ được loại trừ khỏi căn cứ ngừng hoạt động tại điểm đ khoản 2 Điều 35 [B-77ed886349b73469]. Mức phạt tiền cụ thể thường nằm ở văn bản về xử phạt vi phạm hành chính trong lĩnh vực đầu tư, không có trong phần văn bản đã tìm.

## u03 — abstain (2 search, filter=None)

**Câu hỏi:** Dự án đầu tư trong khu kinh tế được áp dụng thuế suất thuế thu nhập doanh nghiệp ưu đãi bao nhiêu phần trăm?

**Câu thiếu evidence.** Lý do: Luật chỉ nêu hình thức ưu đãi là 'thuế suất thấp hơn mức thuế suất thông thường' (tr.10) và dẫn chiếu Luật Thuế thu nhập doanh nghiệp (tr.14); không có con số thuế suất.

**Truy vấn của agent:** ưu đãi đầu tư khu kinh tế thuế suất thuế thu nhập doanh nghiệp | đối tượng được hưởng ưu đãi đầu tư dự án tại khu kinh tế địa bàn ưu đãi

**Câu trả lời của agent:**

> Không đủ bằng chứng trong tài liệu để trả lời.

**Lý do từ chối (model):** Các đoạn đã tìm trong Luật Đầu tư 143/2025/QH15 không ghi mức thuế suất thuế thu nhập doanh nghiệp ưu đãi (bao nhiêu phần trăm) cho dự án trong khu kinh tế. Luật chỉ nêu ba điểm sau. (1) Khu kinh tế là địa bàn ưu đãi đầu tư [B-c71837b5fc2f8f69]. (2) Dự án đầu tư tại địa bàn ưu đãi đầu tư được hưởng ưu đãi đầu tư [B-176ed7ca2416e097]. Ưu đãi này không áp dụng cho dự án khai thác khoáng sản, dự án xây dựng nhà ở thương mại và dự án sản xuất, kinh doanh hàng hóa, dịch vụ chịu thuế tiêu thụ đặc biệt (trừ ô tô, tàu bay, du thuyền) [B-93772e4b1bdf2a46]. (3) Mức ưu đãi cụ thể của từng loại ưu đãi áp dụng theo pháp luật về thuế, kế toán và đất đai [B-93772e4b1bdf2a46]. Vì vậy, muốn biết thuế suất cụ thể cần tra pháp luật về thuế thu nhập doanh nghiệp, không phải Luật Đầu tư.

