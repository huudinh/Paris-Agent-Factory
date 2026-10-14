# MẪU — DANH SÁCH POST QUẢNG CÁO

Đi kèm báo cáo [`R2`](../../reports/R2-phan-tang-quang-cao.md). Dùng bản markdown này dán thẳng vào chat, hoặc tự chuyển sang Excel nếu cần điền hàng loạt.

> Dữ liệu dưới đây là **ví dụ mô phỏng**, khớp với [`MAU_Hoi-thoai.md`](MAU_Hoi-thoai.md) để chạy thử.

---

## Cần điền những gì

| Cột | Mức | Giải thích |
|---|---|---|
| **Mã post** | Bắt buộc | Tự đặt: `P01`, `P02`… để tra cứu giữa các sheet |
| **Tên post đúng như trong thẻ hội thoại** | Bắt buộc | **Khoá nối — cột quan trọng nhất.** Sai một ký tự là không nối được |
| **Dịch vụ** | Bắt buộc | Implant · Niềng · Bọc sứ · Tổng quát · Trẻ em |
| **Nội dung / headline** | Bắt buộc | Câu chính hiển thị trên quảng cáo |
| **Từ ngày · Đến ngày** | Bắt buộc | `DD/MM/YYYY`. Còn chạy thì để trống ô "Đến ngày" |
| **Gom vào post gốc** | Nên có | Bản sao thì ghi mã post gốc. Post gốc để trống |
| **Định dạng** | Nên có | Ảnh đơn · Video · Carousel · Banner |
| **Góc tiếp cận** | Nên có | Để trống được, trợ lý tự suy. Điền sẵn thì chính xác hơn |
| **Trạng thái** | Nên có | Đang chạy · Đã tắt |
| **Chi tiêu** | Tuỳ chọn | Chỉ cần nếu muốn tính *chi phí trên một lead HOT·V1* |
| **Số inbox (FB báo)** | Tuỳ chọn | Để đối chiếu với số hội thoại đếm được |
| **Reach** | Tuỳ chọn | |

**Không cần điền:** số hội thoại · HOT/WARM/COLD · tỷ lệ có SĐT · nhóm giá trị · rào cản — trợ lý tự đếm từ file hội thoại.

**Tám giá trị của cột "Góc tiếp cận":**
`Giá - ưu đãi - trả góp` · `Công nghệ giảm đau` · `Tình trạng cụ thể` · `Giáo dục - giải đáp lo lắng` · `Chuyên môn - bác sĩ - đối tác hãng` · `Case thật / before-after` · `Banner thông báo` · `Gói gia đình - trẻ em`

---

## Bảng để điền

Copy bảng dưới, xoá các dòng ví dụ, điền dữ liệu thật.

```markdown
| Mã post | Tên post đúng như trong thẻ | Dịch vụ | Nội dung / headline | Từ ngày | Đến ngày | Gom vào post gốc | Định dạng | Góc tiếp cận | Trạng thái | Chi tiêu | Số inbox (FB báo) | Reach |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| P01 | QC_Implant_Straumann | Implant | Trồng răng Implant trụ Straumann, ăn nhai như răng thật | 01/10/2026 |  |  | Video | Chuyên môn - bác sĩ - đối tác hãng | Đang chạy |  |  |  |
| P01b | implant straumann - Bản sao | Implant | Trồng răng Implant trụ chính hãng. Inbox nhận tư vấn | 03/10/2026 |  | P01 | Video | Chuyên môn - bác sĩ - đối tác hãng | Đang chạy |  |  |  |
| P02 | QC_Invisalign_BlackDiamond | Niềng | Niềng trong suốt Invisalign, không ai biết bạn đang niềng | 01/10/2026 |  |  | Video | Tình trạng cụ thể | Đang chạy |  |  |  |
| P03 | QC_BocSu_Banner | Bọc sứ | Bọc răng sứ thẩm mỹ, nụ cười mới chỉ sau 1 lần hẹn | 01/10/2026 |  |  | Banner | Banner thông báo | Đang chạy |  |  |  |
| P04 | QC_BocSu_MaiRang | Bọc sứ | Bọc răng sứ có phải mài nhiều răng thật không? Bác sĩ giải đáp | 02/10/2026 |  |  | Ảnh đơn | Giáo dục - giải đáp lo lắng | Đang chạy |  |  |  |
| P05 | QC_AllOn_MatCaHam | Implant | Mất cả hàm vẫn ăn nhai tốt với All-On 4 | 01/10/2026 |  |  | Video | Tình trạng cụ thể | Đang chạy |  |  |  |
| P06 | QC_NhoRang_Piezotome | Tổng quát | Nhổ răng khôn êm với máy siêu âm Piezotome | 05/10/2026 |  |  | Video | Công nghệ giảm đau | Đang chạy |  |  |  |
| P07 | QC_GiaDinh_TreEm | Trẻ em | Gói khám răng cả gia đình, bé được bác sĩ dỗ dành | 01/10/2026 |  |  | Carousel | Gói gia đình - trẻ em | Đang chạy |  |  |  |
| P08 | QC_BocSu_LamLai | Bọc sứ | Răng sứ cũ bị hở, lệch? Bác sĩ đánh giá và làm lại | 04/10/2026 |  |  | Ảnh đơn | Tình trạng cụ thể | Đang chạy |  |  |  |
```

---

## Lấy "tên post đúng như trong thẻ" ở đâu

Đây là cột quyết định R2 chạy được hay không.

1. Mở một hội thoại bất kỳ, xem **tin nhắn đầu tiên**.
2. Tin đó có dạng `[Thẻ: Inbox từ quảng cáo <TÊN POST> – <headline>]`.
3. Copy đúng phần `<TÊN POST>` — nằm giữa `Inbox từ quảng cáo ` và dấu `–` đầu tiên.
4. Hoặc lấy từ Facebook Ads Manager (ad name). **Hai bên phải trùng khớp.**

Sai một ký tự, hoặc thiếu tiền tố `QC_`, là không nối được post với hội thoại.

---

## Gom bản sao về post gốc

Facebook hay nhân bản quảng cáo và thêm hậu tố `- Bản sao`, `- Bản sao 2`, `_Group_1`. Các bản sao thường cùng một nội dung, **phải gom lại mới đủ mẫu**.

Trong ví dụ trên, `P01` và `P01b` là cùng một creative → `P01b` ghi `P01` vào cột *Gom vào post gốc*. Trợ lý sẽ gộp số hội thoại của cả hai, nhưng vẫn giữ một cột ghi rõ đã gom biến thể nào.

---

## Thẻ không phải quảng cáo

Thẻ dạng `[Thẻ: Ưu đãi và thông báo]` là **tin nhắn hàng loạt**, không phải quảng cáo. Đừng đưa vào danh sách post — trợ lý sẽ tách thành nhóm nguồn riêng.

Hội thoại không có thẻ nào → nhóm **"Không rõ nguồn"**, không tính vào bảng phân tầng post.

---

## Muốn đo chi phí trên một lead HOT·V1

Điền thêm cột **Chi tiêu** cho từng post. Đây là con số đáng đo nhất với ngành nha: một lead Implant đắt hơn một lead cạo vôi nhiều lần, nên **cùng một mức CPL thì ý nghĩa hoàn toàn khác nhau**.

Ví dụ: post A chi 10 triệu ra 50 lead (CPL 200k) nhưng toàn lead cạo vôi; post B chi 10 triệu ra 15 lead (CPL 667k) nhưng 11 lead là Implant. Bảng CPL nói post A thắng. Bảng *chi phí trên một lead HOT·V1* nói ngược lại — và bảng sau mới là bảng đúng.
