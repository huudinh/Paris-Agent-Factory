# P6 — TRẠNG THÁI L1–L6 & LUỒNG VẬN HÀNH
Module brand-specific. **Đây là xương sống của cả hệ báo cáo** — mọi file Excel đều có cột L-code lấy từ đây. Cập nhật: 2026-10-14.

---

## 1. LUỒNG VẬN HÀNH ĐẦU–CUỐI

```
KH nhắn Fanpage (FB / Zalo / Web / TikTok)
  → Trực page đọc & trả lời
  → KH cho SĐT → tạo Lead, chuyển CSKH / tổng đài
  → Gọi tư vấn, mời đặt lịch khám
  → KH ĐẾN KHÁM + chụp X-quang/scan          ← mốc then chốt của ngành nha
  → Bác sĩ tư vấn phác đồ → KH chốt điều trị
  → Điều trị (nhiều buổi) → tái khám / kết thúc
```

**Hệ báo cáo này đứng ở đâu:** đọc **dữ liệu đã xảy ra** (hội thoại đã xuất ra file, danh sách post đã chạy) rồi sinh báo cáo. Nó **không** nối vào CRM, **không** tự trả lời khách, **không** thao tác trên phần mềm nào. Người dùng xuất file → dán cho trợ lý → nhận báo cáo → đọc và ra quyết định.

---

## 2. TAXONOMY TRẠNG THÁI L1–L6

Bộ mã này là chuẩn chung với hệ CSKH của tập đoàn, **cộng thêm một mã riêng của ngành nha: L6.7**.

| Level | Mã | Định nghĩa | Nhiệt | Rào cản |
|---|---|---|---|---|
| **L1 Tương tác mới** | **L1.1** | Lần đầu nhắn, chưa được tư vấn gì | Cold | — |
| **L2 Đang tư vấn** | **L2.1** | Có nhu cầu thật, hợp tác cung cấp thông tin, chưa cho số | Warm | — |
| | **L2.3** | Đã tư vấn nhưng chưa phản hồi lại | Warm | — |
| | **L2.4** | Khách chủ động hẹn nhắn lại sau | Warm | — |
| | **L2.5** | Tỉnh/thành **không có cơ sở Paris** hoặc quá xa → khách từ chối | Cool | NGẠI |
| **L4 Cơ hội mới** | **L4.1** | **Có SĐT + dịch vụ quan tâm** → chuyển CSKH/tổng đài | Hot | — |
| **L5 Đang kết nối** | **L5.3** | Gọi không bắt máy | Hot | — |
| | **L5.4** | Từ chối nghe điện thoại, chỉ muốn nhắn | Hot | — |
| | **L5.5** | Hẹn giờ gọi lại cụ thể | Hot | — |
| | **L5.6** | Chỉ trao đổi qua Zalo | Hot | — |
| **L6 Cơ hội ≤30 ngày** | **L6.1** | Có nhu cầu, **chưa xác định được rào cản** | Warm→Hot | ? |
| | **L6.2** | Đang so sánh nơi khác | Warm→Hot | **NGỜ** |
| | **L6.3** | Chưa đủ / chưa sẵn ngân sách · đang hỏi trả góp | Warm→Hot | **NGẠI** |
| | **L6.4** | Chưa sắp xếp được thời gian · lo điều trị dài, đi nhiều buổi | Warm→Hot | **NGẠI** |
| | **L6.5** | Sợ đau · sợ **mài răng thật** · sợ biến chứng | Warm→Hot | **SỢ** |
| | **L6.6** | Cần hỏi ý kiến người thân | Warm→Hot | NGỜ + NGẠI |
| | **L6.7** ⭐ | **Ngờ vật liệu** — hỏi trụ gì, phôi sứ gì, có chính hãng không, có bị tráo không, có phiếu bảo hành không | Warm→Hot | **NGỜ (nặng)** |

> ⭐ **L6.7 là mã riêng của ngành nha**, không có trong hệ thẩm mỹ. Lý do: khách **không tự kiểm tra được vật liệu trong miệng mình** ([[P2-khach-hang]] §2). Gộp L6.7 vào L6.2 là mất đi nhóm rào cản mà Paris có bằng chứng mạnh nhất để gỡ — và mất luôn khả năng đo xem nhân viên có dùng bằng chứng đó hay không.

**Nhịp theo dõi L6 (đã tư vấn, chưa đặt lịch khám):** **D+3 → D+7 → D+15**.

### Quy ước phân biệt hai mã dễ lẫn
- **L2.3 vs L6.x:** chưa biết rào cản *và* chưa tư vấn sâu → L2.3. Đã tư vấn, biết rào cản → L6.x tương ứng.
- **L2.5 vs L6.4:** khách ở **ngoài 7 tỉnh/thành** → L2.5. Khách **trong 7 tỉnh/thành** mà bảo xa/bận → **L6.4**, vẫn còn cửa.
- **L4.1:** phải có **cả hai**: số điện thoại **và** dịch vụ/tình trạng rõ. Có số mà không rõ làm gì → vẫn L2.x, ghi chú "có số, chưa rõ nhu cầu".

---

## 3. ⭐ BA TRỤC PHÂN LOẠI — KHÔNG ĐƯỢC GỘP

Mọi file Excel do hệ này sinh ra phải có **ba cột riêng**:

| Trục | Là gì | Giá trị | Quyết định điều gì |
|---|---|---|---|
| **L-code** | *Trạng thái vận hành* — khách đang ở đâu trong luồng | L1.1 … L6.7 | Dùng kịch bản nào, ai xử lý tiếp |
| **Độ nóng** | *Mức sẵn sàng* — chấm theo 5 tín hiệu ([[P8-chuan-cham-ban-giao]] §3) | HOT / WARM / COLD | SLA gọi, ai nhận |
| **Nhóm giá trị** | *Giá trị kỳ vọng của dịch vụ* ([[P4-dich-vu]] §3) | V1 / V2 / V3 | Mức đầu tư chăm sóc, được phép nuôi bao lâu |

Một lead mang cả ba: ví dụ `L6.7 · WARM · V1` = *đang ngờ vật liệu, chưa sẵn sàng, nhưng là ca Implant* → **nuôi kỹ bằng bằng chứng đối tác hãng, không bỏ**.

> Hệ thẩm mỹ chỉ có hai trục. Nha khoa **bắt buộc có trục thứ ba**, vì dải giá quá rộng. Gộp lại thì nhóm V3 đông và dễ chốt sẽ che mất việc V1 đang rò.

---

## 4. ĐIỀU KIỆN THOÁT — khi nào ngừng nuôi

- **Đã đến khám** → chuyển sang luồng điều trị, thoát luồng nuôi của trực page.
- **Từ chối dứt khoát** ("không có nhu cầu") → đóng, dừng nhắn.
- **Hết cửa sổ 24h Messenger** mà chưa phản hồi → ngừng nhắn tự do; có SĐT thì chuyển CSKH, chưa có thì chờ khách quay lại.
- **Quá 30 ngày ở L6 không tiến triển** → hạ về tệp remarketing. **Ngoại lệ: L6.x · V1 nuôi tới 90 ngày** — chu kỳ quyết định của Implant/All-On/Invisalign dài hơn hẳn, cắt ở 30 ngày là bỏ ca đắt nhất.

---

## 5. PHIẾU BÀN GIAO — 13 TRƯỜNG

Khi lead lên L4.1, trực page ghi lại cho CSKH:

`Họ tên` · `SĐT` · `Zalo` · `Dịch vụ / vấn đề răng` · `Vị trí răng & thời gian bị` · `Đã điều trị ở đâu chưa` · `Mong muốn` · `Rào cản chính (SỢ/NGỜ/NGẠI)` · `Thời gian dự kiến` · `Khung giờ tiện` · `Độ nóng + Nhóm giá trị` · `Link hội thoại` · `Tên trực page`

> Nha khoa cần **13 trường**, thêm so với thẩm mỹ hai mục: **vị trí răng & thời gian bị** và **đã điều trị ở đâu chưa**. Thiếu hai mục này thì CSKH gọi điện phải hỏi lại khách từ đầu, và không phát hiện được ca **V-01 làm lại**.

**Báo cáo chất lượng tư vấn chấm tiêu chí ⑧ bằng cách đếm xem phiếu đủ 13 trường hay không.** Dữ liệu không có phần ghi chú bàn giao → ghi `⚠ không đo được tiêu chí ⑧`, **không cho điểm 0 oan**.

---

## 6. LIÊN KẾT MODULE
[[P3-hanh-vi-trang-thai]] · [[P4-dich-vu]] · [[P5-kich-ban]] · [[P8-chuan-cham-ban-giao]]
