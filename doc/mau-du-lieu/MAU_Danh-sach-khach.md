# MẪU — BẢNG DANH SÁCH KHÁCH

Đi kèm báo cáo [`R6`](../../reports/R6-chan-dung-khach-hang.md). Dùng bản markdown này dán thẳng vào chat, hoặc tự chuyển sang Excel nếu cần điền hàng loạt.

> Dữ liệu dưới đây là **ví dụ mô phỏng** — tên đã thay, không phải khách thật.

---

## Cần điền những gì

| Cột | Mức | Giải thích |
|---|---|---|
| **Năm sinh** *hoặc* **Tuổi** | Bắt buộc một trong hai | Có cả hai thì trợ lý lấy theo năm sinh và báo số dòng lệch |
| **Giới tính** | Bắt buộc | Nữ · Nam · Không rõ. ⛔ Không để trợ lý đoán theo tên |
| **Vấn đề gặp phải** | Bắt buộc | **Trục chính của chân dung.** Ghi bằng chữ thường cũng được — trợ lý gán mã `V-01…V-11` |
| **Dịch vụ sử dụng** | Bắt buộc | Tên dịch vụ thật. Trợ lý gán nhóm giá trị `V1/V2/V3` |
| **Chi nhánh** | Nên có | Gom về 7 tỉnh/thành có cơ sở. Nơi khác xếp nhóm "Khác" |
| **Tình trạng** | Nên có | Mỗi hệ ghi một kiểu — cứ xuất nguyên, trợ lý đọc giá trị rồi báo lại đã hiểu theo loại nào |
| **STT / Mã khách** | Nên có | Để đối chiếu ngược lại file gốc mà không cần in tên khách |

**Không cần điền:** nhóm khách N1–N6 · mã `V-xx` · nhóm giá trị · rào cản · giọng — trợ lý tự gán hết từ bốn cột bắt buộc.

⛔ **Không cần che tên khách trước khi đưa**, nhưng cũng **không cần đưa tên**. R6 được dặn không in tên, số điện thoại hay thông tin định danh vào file đầu ra.

⛔ **Đừng lọc sẵn.** Lọc "chỉ lấy khách đã chốt" cho ra chân dung của **người đã mua**, không phải người **đến với Paris** — mất đúng nhóm đang rò.

---

## Ba cách ghi cột "Vấn đề gặp phải" — cách nào cũng đọc được

| Cách ghi | Trợ lý hiểu |
|---|---|
| `Mất răng số 6 hàm dưới` | `V-03` · nhóm giá trị V1 |
| `răng hô, muốn niềng` | `V-04` |
| `Sứ cũ bị lệch, làm ở chỗ khác` | `V-01` (ưu tiên cao nhất khi có dấu hiệu làm lại) |

Một ô có nhiều vấn đề thì **ngăn cách bằng `·` hoặc dấu phẩy** — trợ lý lấy mã ưu tiên cao nhất làm mã chính và giữ phần còn lại ở cột *Vấn đề phụ*. Viết liền không dấu phân cách thì mất phần phụ.

---

## Bảng mẫu — dán thẳng vào chat được

| STT | Năm sinh | Giới tính | Chi nhánh | Tình trạng | Vấn đề gặp phải | Dịch vụ sử dụng |
|---|---|---|---|---|---|---|
| 1 | 1972 | Nữ | Hà Nội | Đã đến khám | Mất 2 răng hàm dưới, ăn nhai khó | Implant 2 trụ |
| 2 | 1995 | Nữ | Hà Nội | Đang tư vấn | Răng hô nhẹ, muốn niềng trong suốt | Invisalign |
| 3 | 1988 | Nam | Hải Phòng | Đã chốt | Răng xỉn màu, vỡ 1 răng cửa | Bọc sứ 4 răng |
| 4 | 2009 | Nữ | Hà Nội | Mới | Răng khấp khểnh, mẹ đưa đi khám | Niềng mắc cài |
| 5 | 1965 | Nam | Vinh | Đã đến khám | Mất gần cả hàm trên | All-On 4 |
| 6 | 1999 | Nữ | TP.HCM | Đang tư vấn | Sứ cũ lệch, làm ở nơi khác 2 năm trước | Chờ khám lại |
| 7 | 1993 | Nam | Đà Nẵng | Mới | Đau nhức răng hàm 3 ngày nay | Điều trị tủy |
| 8 | 1980 | Nữ | Quảng Ninh | Đã chốt | Chảy máu chân răng, hôi miệng | Cạo vôi + điều trị nha chu |
| 9 | 2016 | Nam | Hà Nội | Đã đến khám | Bé sâu răng sữa | Nha khoa trẻ em |
| 10 | 1990 | Nữ | Bình Dương | Đang tư vấn | Răng ố vàng, muốn trắng nhanh trước cưới | WhiteMax |

> **Mười dòng là để xem cấu trúc, không đủ để chạy R6 thật.** Ngưỡng tối thiểu là **10 khách cho mỗi nhóm** mới được kết luận — tức là cần vài trăm dòng thì chân dung mới có nghĩa. Dưới ngưỡng, trợ lý vẫn in nhưng ghi `⚠ chưa đủ mẫu` và không khuyến nghị.

---

## Chạy thử

Dán bảng trên vào chat rồi gõ:

```
Dựng chân dung khách hàng từ bảng này. Kỳ: tháng 10.
```

Trợ lý phải **dừng lại** ở điểm dừng đầu tiên và báo: 10 dòng · cột nào thiếu bao nhiêu · hiểu cột *Tình trạng* là **trạng thái lead** · mọi nhóm đều dưới 10 khách nên chưa kết luận được gì. Nó chạy thẳng ra 5 sheet mà không dừng → phần chỉ dẫn đang nạp thiếu.
