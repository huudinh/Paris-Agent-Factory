# 02 · CHUẨN BỊ DỮ LIỆU — lấy số liệu đầu vào ở đâu

> **Đây là bước duy nhất cần làm bằng tay, và nó quyết định chất lượng cả báo cáo.**
> Dữ liệu tốt thì báo cáo tốt. Dữ liệu đã bị lọc thì mọi con số đều lệch, và lệch theo hướng khó phát hiện.

---

# 1. Báo cáo nào cần dữ liệu gì

| Báo cáo | Bắt buộc có | Có thì tốt hơn |
|---|---|---|
| **R1** Phân loại hội thoại | File hội thoại | Tên người phụ trách · cột Có SĐT |
| **R2** Phân tầng quảng cáo | Danh sách post **+** file hội thoại cùng kỳ | Chi tiêu từng post · reach · số inbox FB báo |
| **R3** Chất lượng tư vấn | File hội thoại **có dấu thời gian từng tin** + tên phụ trách | Phần ghi chú bàn giao nội bộ |
| **R4** Báo cáo điều hành | File hội thoại | **Số đặt lịch · số đến khám · số chốt phác đồ** |
| **R5** So sánh hai kỳ | Dữ liệu 2 kỳ đã chạy R1 | Dữ liệu R2/R3 của cả 2 kỳ |

---

# 2. ⚠ LUẬT QUAN TRỌNG NHẤT: XUẤT TOÀN BỘ, KHÔNG LỌC

**Đừng lọc hội thoại trước khi đưa cho trợ lý.** Ba cách lọc hay gặp, và tác hại:

| Lọc kiểu | Người ta nghĩ | Thực tế xảy ra |
|---|---|---|
| "Chỉ lấy hội thoại dài, cho đỡ rác" | Hội thoại ngắn không có gì để đọc | Hội thoại dài = khách tương tác nhiều = **đã thiên về phía nóng**. Mọi post sẽ trông tốt hơn thật, và **thổi không đều nhau** → so sánh post thành vô nghĩa |
| "Chỉ lấy hội thoại có số điện thoại" | Khách không cho số thì không phải lead | Mất luôn **mẫu số** để tính tỷ lệ xin số — chỉ số chính của trực page. Báo cáo sẽ ra 100% có SĐT |
| "Lấy 100 cái tiêu biểu" | 100 là đủ nhiều | Nếu chọn tay thì chọn theo cảm nhận, không phải theo xác suất. Và cảm nhận thường nghiêng về ca đáng nhớ = ca đặc biệt |

**Nếu buộc phải lọc** (ví dụ hệ thống chỉ xuất được 100 dòng một lần): nói rõ cho trợ lý *"đây là 100 hội thoại chọn từ 520, ưu tiên hội thoại dài"*. Trợ lý sẽ ghi cảnh báo lên sheet đầu và **không dùng số đó để khuyến nghị ngân sách** — vẫn đọc được chân dung khách và rào cản, chỉ không so được post với post.

---

# 3. Xuất hội thoại — ba cách

## Cách A · Từ CRM (Caresoft, hoặc hệ đang dùng) — tốt nhất

Xuất ra `.xlsx` hoặc `.csv`, **giữ nguyên các cột sau**:

| Cột | Bắt buộc | Dùng để |
|---|---|---|
| Tên khách | ✅ | Đánh dấu từng hội thoại |
| Thời gian từng tin | ✅ với R3 | Chấm tiêu chí "phản hồi ≤2 phút" |
| Nội dung tin | ✅ | Toàn bộ việc đọc hiểu |
| Người gửi (KH / NV) | ✅ | Phân biệt ai nói gì |
| Tên nhân viên phụ trách | ✅ với R3 | Chấm theo người |
| **Thẻ nguồn / tên quảng cáo** | ✅ với R2 | **Khoá nối post ↔ hội thoại** |
| Có SĐT (Có/Không) | Nên có | Trợ lý lấy nguyên, không tự suy lại |
| Ghi chú nội bộ / phiếu bàn giao | Nên có | Chấm tiêu chí ⑦ ⑧ của R3 |

> **Thẻ nguồn là cột dễ mất nhất và quan trọng nhất với R2.** Nó thường nằm trong **tin nhắn đầu tiên** của hội thoại, dạng `[Thẻ: Inbox từ quảng cáo QC_Implant_Straumann – ...]`. Nhiều người xuất file rồi xoá dòng này vì tưởng là rác. **Mất thẻ là R2 chỉ chạy được chế độ dự đoán.**

## Cách B · Từ Meta Business Suite

1. Vào **Business Suite** → **Hộp thư** (Inbox).
2. Chọn khoảng thời gian.
3. Không có nút xuất toàn bộ → mở từng hội thoại, copy nội dung. Chậm, chỉ nên dùng khi mẫu nhỏ.
4. **Nhớ copy cả dòng đầu có tên quảng cáo** nếu khách vào từ post.

## Cách C · Dán trực tiếp vào chat

Với mẫu nhỏ (dưới ~30 hội thoại), copy dán thẳng vào trợ lý cũng được. Giữ định dạng rõ ai nói gì là đủ — trợ lý được dặn **tự nhận dạng cấu trúc, không bắt bạn sửa file**.

---

# 4. Định dạng chuẩn — nếu bạn muốn chỉnh file cho chuẩn

Không bắt buộc, nhưng dùng đúng định dạng này thì trợ lý đọc chính xác nhất:

```markdown
## 1. Nguyễn Thị A — 03/10 09:12
- Phụ trách: Trần B · Có SĐT: Có · Số tin: 14
- **03/10 09:12 KH:** [Thẻ: Inbox từ quảng cáo QC_Implant_Straumann – Trồng răng Implant trụ Straumann, ăn nhai như răng thật]
- **03/10 09:12 KH:** em mất răng số 6 hàm dưới 2 năm rồi, giờ trồng được không ạ
- **03/10 09:13 NV (Trần B):** Dạ chào anh/chị, em là B tư vấn viên Nha khoa Paris...
- **03/10 09:20 KH:** [Ảnh]
- **03/10 09:25 KH:** trụ của mình là trụ gì ạ, có chính hãng không
```

**Quy ước:**
- `[Ảnh]` `[Tệp]` `[Thẻ: …]` là đính kèm hoặc tin tự động, **không phải chữ khách gõ**.
- Một hội thoại = một khối bắt đầu bằng `## <STT>. <Tên> — <ngày giờ>`.
- File mẫu đầy đủ: [`mau-du-lieu/MAU_Hoi-thoai.md`](mau-du-lieu/MAU_Hoi-thoai.md).

---

# 5. Danh sách post quảng cáo — cho R2

Bảng điền sẵn ở [`mau-du-lieu/MAU_Danh-sach-post.md`](mau-du-lieu/MAU_Danh-sach-post.md).

| Cột | Mức | Giải thích |
|---|---|---|
| **Mã post** | Bắt buộc | Tự đặt: `P01`, `P02`… để tra cứu giữa các sheet |
| **Tên post đúng như trong thẻ hội thoại** | Bắt buộc | **Khoá nối — cột quan trọng nhất.** Sai một ký tự là không nối được |
| **Dịch vụ** | Bắt buộc | Implant · Niềng · Bọc sứ · Tổng quát… |
| **Nội dung / headline** | Bắt buộc | Câu chính hiển thị trên quảng cáo |
| **Từ ngày · Đến ngày** | Bắt buộc | `DD/MM/YYYY`. Còn chạy thì để trống ô "Đến ngày" |
| **Gom vào post gốc** | Nên có | Bản sao thì ghi mã post gốc. Post gốc để trống |
| **Góc tiếp cận** | Nên có | Để trống được, trợ lý tự suy. Điền sẵn thì chính xác hơn |
| **Định dạng** | Nên có | Ảnh đơn · Video · Carousel · Banner |
| **Trạng thái** | Nên có | Đang chạy · Đã tắt |
| **Chi tiêu** | Tuỳ chọn | Cần nếu muốn tính *chi phí trên một lead HOT·V1* |
| **Số inbox (FB báo)** | Tuỳ chọn | Để đối chiếu với số hội thoại đếm được |
| **Reach** | Tuỳ chọn | |

**Không cần điền:** số hội thoại, HOT/WARM/COLD, tỷ lệ có SĐT, nhóm giá trị, rào cản — trợ lý tự đếm từ file hội thoại.

**Tám giá trị của cột "Góc tiếp cận":** Giá - ưu đãi - trả góp · Công nghệ giảm đau · Tình trạng cụ thể · Giáo dục - giải đáp lo lắng · Chuyên môn - bác sĩ - đối tác hãng · Case thật / before-after · Banner thông báo · Gói gia đình - trẻ em.

## Lấy "tên post đúng như trong thẻ" ở đâu

Đây là cột quyết định R2 chạy được hay không.

1. Mở một hội thoại bất kỳ, xem **tin nhắn đầu tiên**.
2. Tin đó có dạng `[Thẻ: Inbox từ quảng cáo <TÊN POST> – <headline>]`.
3. Copy đúng phần `<TÊN POST>` — nằm giữa `Inbox từ quảng cáo ` và dấu `–` đầu tiên.
4. Hoặc lấy từ Facebook Ads Manager (ad name). **Hai bên phải trùng khớp.**

Sai một ký tự, hoặc thiếu tiền tố `QC_`, là không nối được post với hội thoại.

## Gom bản sao về post gốc

Facebook hay nhân bản quảng cáo và thêm hậu tố `- Bản sao`, `- Bản sao 2`, `_Group_1`. Các bản sao thường cùng một nội dung, **phải gom lại mới đủ mẫu**.

Ví dụ — ba dòng này là cùng một creative:

| Tên trong thẻ | Số hội thoại |
|---|---|
| `QC_Implant_Straumann` | 24 |
| `implant straumann - Bản sao` | 11 |
| `implant straumann - Bản sao 2` | 4 |

Gom lại **39 hội thoại** — đủ mẫu kết luận. Để riêng thì bản sao 2 chỉ có 4, không nói lên gì.

→ Post gốc cho mã `P01`; hai bản sao ghi `P01` vào cột *Gom vào post gốc*.

---

# 6. Số liệu phễu — cho R4

R4 đọc được **nửa phễu đầu** chỉ từ file hội thoại: inbox → có SĐT → kết nối. Muốn đọc tiếp thì cần ba con số sau, lấy từ phòng khám hoặc hệ thống đặt lịch:

| Con số | Lấy ở đâu | Vì sao cần |
|---|---|---|
| **Số đặt lịch khám trong kỳ** | Hệ thống đặt lịch / sổ lịch hẹn | Đo khâu kết nối → đặt lịch |
| **Số ĐẾN KHÁM trong kỳ** ⭐ | Sổ tiếp nhận tại phòng khám | **Con số quan trọng nhất của R4.** Đặt lịch ≠ đến khám, và khoảng lệch là chỗ rò nặng nhất |
| **Số chốt phác đồ** | Hệ thống điều trị | Tách riêng — đây là chỉ số của phòng khám, không phải của marketing |

**Chưa có ba số này vẫn chạy được R4**, chỉ là phần phễu sau sẽ ghi `⚠ chưa đo được show-up`. Lần đầu chạy thường như vậy. Mỗi kỳ bổ sung thêm một con số thì sau 2–3 kỳ là đủ cả phễu.

> **Tuyệt đối đừng lấy "đặt lịch" thay cho "đến khám" cho đủ bảng.** Ở nha khoa hai con số này lệch nhau rất nhiều. Lấy thay thì báo cáo sẽ nói phễu đang ổn ở đúng chỗ nó đang rò nặng nhất.

---

# 7. Danh sách kiểm trước khi đưa cho trợ lý

- [ ] File hội thoại là **toàn bộ** trong kỳ, không lọc theo độ dài hay theo có SĐT
- [ ] Nếu đã lọc → đã **ghi lại cách lọc** để nói cho trợ lý
- [ ] Còn **dấu thời gian** từng tin (cần cho R3)
- [ ] Còn **tên nhân viên phụ trách** (cần cho R3)
- [ ] Còn **thẻ nguồn / tên quảng cáo** ở tin đầu (cần cho R2)
- [ ] Danh sách post có **tên đúng như trong thẻ**, không phải tên tự đặt
- [ ] Đã gom **bản sao** về post gốc
- [ ] Đã xoá **CCCD, hồ sơ bệnh án, ảnh nhận diện mặt** nếu có lẫn trong file
- [ ] Chạy trên **tài khoản nội bộ công ty**, không phải tài khoản cá nhân
