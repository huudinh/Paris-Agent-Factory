# R6 — CHÂN DUNG KHÁCH HÀNG TỪ DANH SÁCH KHÁCH

**Trả lời câu hỏi:** *Khách đang đến Paris là những ai, mỗi nhóm bao nhiêu người, họ vướng gì và đang dùng dịch vụ nào — để viết nội dung và chia ngân sách cho đúng người.*

**Cần có:** một **bảng danh sách khách** (`.xlsx` · `.csv` · dán thẳng cũng được) có các cột:

| Cột | Bắt buộc | Dùng để |
|---|---|---|
| **Năm sinh** *hoặc* **Tuổi** | ✅ một trong hai | Xếp dải tuổi → nhóm khách N1–N6 |
| **Giới tính** | ✅ | Chọn giọng và góc tiếp cận |
| **Vấn đề gặp phải** | ✅ | Gán mã `V-01…V-11` — trục chính của chân dung |
| **Dịch vụ sử dụng** | ✅ | Gán nhóm giá trị `V1/V2/V3` |
| **Chi nhánh** | Nên có | So chân dung giữa các cơ sở |
| **Tình trạng** | Nên có | Tuỳ hệ: trạng thái lead · tình trạng răng · hôn nhân (xem §*Cột "Tình trạng"*) |

**Nhận lại:** 1 file Excel `output/Paris_ChanDung_<kỳ>.xlsx`, 5 sheet.

| Sheet | Góc nhìn |
|---|---|
| `1 · Chân dung` | 4–6 thẻ chân dung: quy mô · tuổi · giới · vấn đề · dịch vụ · rào cản · giọng · góc tiếp cận |
| `2 · Bảng chéo` | Vấn đề × Dịch vụ · Tuổi × Nhóm giá trị · Chi nhánh × Nhóm giá trị · Giới × Vấn đề |
| `3 · Khoảng trống` | Vấn đề nhiều mà dịch vụ tương ứng ít · chi nhánh lệch so với toàn hệ |
| `4 · Dữ liệu chuẩn hoá` | Từng dòng khách kèm mã đã gán, để kiểm lại |
| `5 · Chú giải` | Bộ mã N · V-xx · V1/V2/V3 · rào cản |

> **R6 khác R1 ở chỗ nào.** R1 đọc **hội thoại** — biết khách *nói* gì, nên chấm được độ nóng và viết được kịch bản nhắn lại. R6 đọc **danh sách khách** — biết khách *là ai và đã làm gì*, nên dựng được chân dung để nhắm quảng cáo và viết nội dung. Có cả hai thì chạy R1 trước, rồi R6 đối chiếu: **nhóm đông trong danh sách mà vắng trong inbox là nhóm quảng cáo đang không chạm tới.**

> **📎 Không có code mẫu sẵn.** `tools/phan_loai.py` đọc hội thoại, không đọc bảng khách. R6 để trợ lý viết script tại chỗ, dùng lại style ở [`tools/excel_style.py`](../tools/excel_style.py).

---

## PROMPT — copy từ đây

````
# NHIỆM VỤ
Đọc bảng danh sách khách `{{FILE}}` và dựng CHÂN DUNG KHÁCH HÀNG, xuất ra ĐÚNG 1 file
Excel trong thư mục `output/`: Paris_ChanDung_{{KỲ}}.xlsx — 5 sheet.
Kỳ dữ liệu: {{KỲ}}. (Không biết kỳ thì đọc từ dữ liệu và báo lại.)

Viết script Python dùng openpyxl. Không trả bảng trong chat — ghi ra file thật.
Nếu môi trường không chạy được code: nói rõ, rồi trả bảng markdown dán được vào Excel.

# ĐẦU VÀO — nhận cột, không bắt tôi sửa file
Các cột cần tìm (tên cột trong file có thể viết hoa/thường, có dấu hoặc không,
có thể kèm chữ thừa — tự nhận dạng, đừng đòi tôi đổi tên cột):

  Năm sinh | Tuổi | Giới tính | Chi nhánh | Tình trạng | Vấn đề gặp phải | Dịch vụ sử dụng

Thiếu cột nào thì BÁO RÕ cột đó và phần nào của báo cáo sẽ không chạy được,
rồi CHẠY TIẾP phần còn lại. Không dừng chỉ vì thiếu một cột không bắt buộc.

# BƯỚC 1 — CHUẨN HOÁ. Chuẩn hoá một lần, cả 5 sheet đọc chung kết quả đó.

## Tuổi
- Có CẢ "Năm sinh" lẫn "Tuổi" → tính tuổi từ năm sinh theo năm của kỳ dữ liệu,
  đếm số dòng lệch quá 1 tuổi và BÁO con số đó. Lấy theo năm sinh.
- Chỉ có "Tuổi" → dùng nguyên.
- Năm sinh dạng 2 chữ số, ngày tháng đầy đủ, hoặc text lẫn chữ → tự xử lý.
- Ngoài khoảng 1–100 → xếp "⚠ không hợp lệ", không đoán, không xoá dòng.
- Dải tuổi dùng chung: ≤17 · 18–24 · 25–34 · 35–44 · 45–54 · 55–64 · ≥65.

## Giới tính
Gom về Nữ / Nam / Không rõ. ⛔ Không đoán giới tính từ tên.

## Chi nhánh
Gom về 7 tỉnh/thành có cơ sở: Hà Nội · Hải Phòng · Quảng Ninh · Vinh (Nghệ An) ·
Đà Nẵng · TP.HCM · Bình Dương. Giá trị khác → giữ nguyên, nhóm "Khác".

## Cột "Tình trạng" — TỰ NHẬN LOẠI, đừng đoán bừa
Đọc các giá trị thật trong cột rồi xếp vào ĐÚNG MỘT trong ba loại, và GHI RÕ đã hiểu
theo loại nào ở đầu báo cáo:
  (a) TRẠNG THÁI LEAD — "mới", "đang tư vấn", "đã đặt lịch", "đã đến khám", "đã chốt", "huỷ"
  (b) TÌNH TRẠNG RĂNG — "mất 2 răng", "hô", "viêm nướu"…  → gộp vào cột Vấn đề, không tách trục riêng
  (c) TÌNH TRẠNG HÔN NHÂN/GIA ĐÌNH — "độc thân", "đã kết hôn", "có con"
Lẫn nhiều loại trong một cột → báo rõ tỷ lệ từng loại, dùng loại chiếm đa số,
phần còn lại xếp "Không rõ". ⛔ Không tự suy một giá trị sang loại khác.

# BƯỚC 2 — GÁN MÃ. Dùng đúng bộ mã có sẵn, ⛔ KHÔNG tự chế mã mới.

## Vấn đề gặp phải → V-01…V-11 (xét ưu tiên TỪ TRÊN XUỐNG, một dòng một mã chính)
V-01 làm lại/sửa ca lỗi · V-02 mất nhiều răng/cả hàm · V-03 mất răng lẻ/trồng lại ·
V-04 lệch-khấp khểnh-thưa-hô · V-05 xỉn-vỡ-sứt-mòn · V-06 đau nhức-viêm tủy-áp xe ·
V-07 viêm nướu-vôi răng-hôi miệng · V-08 răng khôn-nhổ răng · V-09 tẩy trắng-thẩm mỹ nhẹ ·
V-10 răng trẻ em · V-11 chưa rõ/hỏi chung.
Một dòng ghi nhiều vấn đề → lấy mã ưu tiên cao nhất làm mã chính, ghi phần còn lại
vào cột "Vấn đề phụ". Ô trống → V-11, KHÔNG đoán theo dịch vụ.

## Dịch vụ sử dụng → nhóm giá trị
V1 lớn: Implant · All-On 4/6 · Invisalign · sứ toàn hàm · ghép xương/nâng xoang
V2 trung: bọc sứ 1–6 răng · Veneer · niềng mắc cài · tủy + sứ
V3 nhỏ/cửa vào: cạo vôi · tẩy trắng · trám · nhổ răng · răng khôn · răng trẻ em · Teeth Spa
Không khớp mục nào → "⚠ chưa phân loại", liệt kê ra để tôi bổ sung từ điển.

## Nhóm khách N1–N6 (dùng tuổi + vấn đề + giới, theo thứ tự này)
N1 Mất răng trung–cao niên: 45+ và V-02/V-03
N2 Thẩm mỹ răng 22–40: 18–44 và V-04/V-05/V-09
N3 Niềng 15–30 (+ phụ huynh): 15–30 và V-04
N4 Đau cấp: V-06 (mọi tuổi — nhóm này cắt ngang tuổi)
N5 Làm lại ca lỗi: V-01 (mọi tuổi)
N6 Gia đình & trẻ em: ≤17, hoặc V-10
Rơi vào nhiều nhóm → ưu tiên N5 > N4 > N1 > N3 > N6 > N2.
Không rơi nhóm nào → "Ngoài 6 nhóm", giữ lại và đếm riêng, ⛔ không nhét bừa.

# DỪNG 1 — BÁO ĐỦ RỒI CHỜ TÔI XÁC NHẬN
① tổng số dòng đọc được · ② mỗi cột thiếu bao nhiêu dòng (số + %) ·
③ kỳ dữ liệu đọc được · ④ cột "Tình trạng" hiểu theo loại nào và vì sao ·
⑤ bao nhiêu dòng "⚠ chưa phân loại" ở cột dịch vụ · ⑥ bao nhiêu dòng "Ngoài 6 nhóm" ·
⑦ danh sách này là TOÀN BỘ khách trong kỳ hay đã lọc sẵn (hỏi tôi nếu không rõ).
KHÔNG dựng chân dung trước khi tôi xác nhận.

# BƯỚC 3 — SHEET 1 · CHÂN DUNG
Mỗi nhóm N có ≥10 khách là MỘT dòng chân dung. Nhóm <10 khách: vẫn in, ghi
"⚠ chưa đủ mẫu", ⛔ KHÔNG viết insight và KHÔNG khuyến nghị cho nhóm đó.

Cột: Mã nhóm · Gọi là gì · Số khách · % tổng · Tuổi điển hình (trung vị + dải) ·
Nghiêng giới nào (ghi % — chỉ gọi là "nghiêng" khi lệch ≥60/40) · 3 chi nhánh đông nhất ·
Vấn đề chính (2–3 mã V-xx kèm %) · Dịch vụ đang dùng (top 3) · Nhóm giá trị chiếm đa số ·
Rào cản dự đoán · Giọng nên dùng · Góc tiếp cận post nên chạy · Câu hỏi ngầm họ chưa hỏi.

Rào cản · giọng · câu hỏi ngầm lấy từ tri thức P2 (6 nhóm khách, 3 rào cản SỢ·NGỜ·NGẠI)
và P5. ⛔ Không tự nghĩ ra đặc điểm tâm lý không có trong P2.
Góc tiếp cận chọn trong 8 giá trị chuẩn, ⛔ không tự chế góc mới.

⚠ Ghi rõ ngay dưới tiêu đề sheet: rào cản và câu hỏi ngầm là **suy luận từ nhóm**,
không phải điều từng khách đã nói. Muốn biết khách NÓI gì thì chạy R1 trên hội thoại.

# BƯỚC 4 — SHEET 2 · BẢNG CHÉO
Bốn bảng, mỗi bảng có cả số tuyệt đối và % theo hàng:
① Vấn đề (V-01…V-11) × Dịch vụ (V1/V2/V3)
② Dải tuổi × Nhóm giá trị
③ Chi nhánh × Nhóm giá trị
④ Giới tính × Vấn đề
Ô dưới 10 khách: ghi số, tô vàng, ⛔ không kết luận gì từ ô đó.
Có cột "Tình trạng" loại (a) → thêm bảng ⑤ Nhóm N × Trạng thái lead.

# BƯỚC 5 — SHEET 3 · KHOẢNG TRỐNG (phần đáng tiền nhất của báo cáo)
① **Lệch vấn đề ↔ dịch vụ.** Nhóm vấn đề có nhiều khách nhưng dịch vụ tương ứng lại ít
   → ghi ra, kèm số. Ví dụ dạng: "V-03 mất răng lẻ: 120 khách, nhưng chỉ 28 dùng dịch vụ
   nhóm V1 — 92 khách còn lại đang dùng gì?"
   ⚠ Đây KHÔNG tự động là lỗi: khách có thể đang điều trị dở, hoặc chọn phương án khác.
   Ghi như MỘT CÂU HỎI để người đọc đi kiểm, ⛔ không kết luận là "mất khách".
② **Chi nhánh lệch.** Chi nhánh nào có tỷ trọng một nhóm cao/thấp hơn toàn hệ ≥10 điểm %
   → ghi ra. Chỉ xét chi nhánh có ≥30 khách.
③ **Nhóm vắng.** Nhóm N nào gần như không có trong dữ liệu → nêu, kèm câu hỏi: do thị
   trường không có, hay do quảng cáo chưa chạm?

# DỪNG 2 — nêu 3 phát hiện lớn nhất bằng lời thường, chờ tôi xác nhận rồi mới ghi file.

# BƯỚC 6 — GHI FILE + TỰ KIỂM
Sheet 4 ghi lại từng dòng khách kèm mã đã gán (tuổi chuẩn hoá · N · V-xx · nhóm giá trị).
Sheet 5 chú giải đầy đủ bộ mã.
Tự kiểm và báo: tổng các nhóm N có bằng tổng số dòng không · tổng bảng chéo có khớp
tổng không · còn ô nào <10 mà vẫn có khuyến nghị không · còn mã nào tự chế không.

# KHÔNG ĐƯỢC
- ❌ KHÔNG chẩn đoán. Cột "Vấn đề gặp phải" là chữ người nhập ghi, không phải chẩn đoán
  y khoa. Mọi nhận định đều kèm "cần bác sĩ khám và chụp phim".
- ❌ KHÔNG suy thu nhập, học vấn, nghề nghiệp, khả năng chi trả từ tuổi, giới hay chi nhánh.
- ❌ KHÔNG gán đặc điểm giới tính không có trong số liệu (kiểu "nữ quan tâm thẩm mỹ hơn").
  Chỉ nói điều bảng chéo ④ cho thấy, kèm số.
- ❌ KHÔNG xếp hạng, KHÔNG khuyến nghị cho nhóm dưới 10 khách.
- ❌ KHÔNG đưa tên khách, số điện thoại, địa chỉ hay thông tin định danh vào file đầu ra.
  Sheet 4 dùng STT hoặc mã khách, ⛔ không dùng tên.
- ❌ KHÔNG tự chế mã nhóm, mã vấn đề hay góc tiếp cận mới.
- ❌ KHÔNG điền số thay cho ô trống. Thiếu là ghi thiếu.
- ⚠ Mọi con số giá / ưu đãi / % cam kết phải gắn ⚠ cần xác minh.

# TRÌNH BÀY EXCEL
- Font Arial toàn bộ. Freeze dòng tiêu đề. Wrap text ở cột mô tả dài (tối thiểu 50).
- Tiêu đề bảng: nền đậm, chữ trắng, in đậm.
- Màu quy ước: vàng cho mọi ô ⚠ và ô <10 khách · viền đậm cho dòng nhóm giá trị V1 ·
  đỏ nhạt cho dòng Khoảng trống cần đi kiểm.
- Sheet 1 mỗi chân dung một dòng, chiều cao dòng đủ đọc hết cột giọng và câu hỏi ngầm.
````

## Đến đây

---

## Lưu ý khi dùng

**Chân dung là mô tả NHÓM, không phải hồ sơ cá nhân.** Phần rào cản · giọng · câu hỏi ngầm là suy luận từ tri thức `P2` áp lên nhóm, không phải điều từng khách đã nói. Dùng để **viết nội dung và chọn góc quảng cáo** thì đúng; dùng để kết luận về một khách cụ thể thì sai.

**Cột "Vấn đề gặp phải" và "Dịch vụ sử dụng" là hai thời điểm khác nhau.** Vấn đề là lúc khách tìm tới; dịch vụ là thứ cuối cùng làm. Chênh lệch giữa hai cột chính là phần đáng đọc nhất — nhưng nó là **câu hỏi để đi kiểm**, không phải kết luận mất khách. Khách mất răng lẻ có thể đang chờ ghép xương, hoặc làm cầu răng thay vì Implant.

**Cột "Tình trạng" mỗi hệ CRM ghi một kiểu.** Chỗ này prompt bắt trợ lý tự đọc giá trị thật rồi nói rõ đã hiểu theo loại nào. Nếu nó hiểu sai, sửa ngay ở DỪNG 1 — rẻ hơn sửa sau khi đã dựng xong 5 sheet.

**Ngưỡng 10 khách giữ nguyên như R2 · R3 · R4.** Một nhóm 6 người thì mọi tỷ lệ phần trăm đều vô nghĩa: thêm một người là lệch 17 điểm %.

**Chạy cùng R1 thì mạnh hơn hẳn.** R6 cho biết **khách Paris là ai**; R1 cho biết **ai đang inbox**. Nhóm đông ở R6 mà vắng ở R1 là nhóm quảng cáo chưa chạm tới — và đó thường là nhóm đáng tiền nhất, vì họ vẫn đến phòng khám bằng đường khác.

**File nguồn là dữ liệu khách thật.** Chạy trên máy nội bộ. Sheet 4 cố tình không in tên khách — kiểm lại trước khi gửi file ra ngoài.
