# R4 — BÁO CÁO ĐIỀU HÀNH THEO DỊCH VỤ

**Trả lời câu hỏi:** *Phễu đang rò ở khâu nào, dịch vụ nào đang mất tiền, và tháng tới dồn lực vào đâu.*

**Dành cho:** giám đốc dịch vụ, trưởng phòng marketing, ban điều hành.
**Cần có:** file hội thoại trong kỳ. Có thêm số đặt lịch / đến khám thì đọc được cả phễu.
**Nhận lại:** 1 file Excel — `output/Paris_BaoCaoDieuHanh_<KỲ>.xlsx`, 8 sheet. Kèm **bản tóm tắt 1 trang** để trình bày.

---

## ⚠ Phễu nha khoa có mốc "đến khám" — không được bỏ

```
inbox → có SĐT → kết nối (gọi được) → đặt lịch khám → ĐẾN KHÁM
      → chốt phác đồ điều trị → bắt đầu điều trị
```

**"Đặt lịch khám" không phải "đến khám".** Ở nha khoa hai con số này lệch nhau rất nhiều, và khoảng lệch đó chính là chỗ rò nặng nhất. Dữ liệu không có số đến khám → ghi `⚠ chưa đo được show-up`, **tuyệt đối không lấy "đặt lịch" thay thế**.

**Quyết định tiền thật xảy ra trên ghế khám, không xảy ra trong inbox.** Vì vậy báo cáo này đo trách nhiệm của trực page **tới mốc đến khám**, và tách riêng mốc "chốt phác đồ" như một chỉ số của phòng khám, không phải của marketing.

---

## PROMPT — copy từ đây

````
# NHIỆM VỤ
Sinh báo cáo điều hành theo dịch vụ cho ban lãnh đạo Nha khoa Paris.
Sinh ra ĐÚNG 1 file: `output/Paris_BaoCaoDieuHanh_{{KỲ}}.xlsx`
Kèm theo: một BẢN TÓM TẮT 1 TRANG dạng markdown in ra ngay trong chat, để trình bày.

Đầu vào:
- File hội thoại trong kỳ: {{FILE HỘI THOẠI}}
- Số đặt lịch / đến khám / chốt phác đồ (nếu có): {{FILE SỐ LIỆU}} — không có thì bỏ qua
  và ghi rõ chưa đo được
- Kỳ: {{KỲ}}

Viết script Python dùng openpyxl, ghi file thật. Không chạy được code → nói rõ rồi
trả bảng markdown dán được vào Excel.

# BA TRỤC BẮT BUỘC TÁCH RIÊNG
- **Dịch vụ / vấn đề răng:** 11 nhóm V-01 … V-11
- **Độ nóng:** HOT / WARM / COLD (5 tín hiệu + 3 luật ghi đè, xem R1)
- **Nhóm giá trị:** V1 lớn (Implant · All-On · Invisalign · sứ toàn hàm) ·
  V2 trung (sứ lẻ · Veneer · mắc cài) · V3 nhỏ/cửa vào (cạo vôi · tẩy trắng ·
  trám · nhổ · trẻ em)

MỌI BẢNG PHỄU PHẢI TÁCH THEO V1/V2/V3. Gộp lại thì nhóm V3 đông và dễ chốt sẽ
che mất việc V1 đang rò — và V1 là chỗ tiền thật.

# CẤU TRÚC FILE EXCEL — 8 sheet

1. **Một trang cho lãnh đạo**
   Dòng 1–3: BA KẾT LUẬN, mỗi dòng một con số, viết bằng lời thường.
   Rồi: bảng phễu toàn kỳ · bảng phễu tách V1/V2/V3 · 3 dịch vụ đang rò nặng nhất ·
   3 việc tháng tới kèm người phụ trách.
   Rồi: **khối cảnh báo phương pháp** — mẫu là toàn bộ hay đã lọc · chỉ số nào
   chưa đo được · con số nào KHÔNG dùng để quyết ngân sách.
   Sheet này phải đọc hết trong 2 phút. Không có bảng nào quá 10 dòng.

2. **Phễu theo dịch vụ** — cột:
   Vấn đề răng (V-xx) | Nhóm giá trị | Inbox | Có SĐT | % có SĐT | Kết nối được |
   % kết nối | Đặt lịch khám | % đặt lịch | Đến khám | % show-up | Chốt phác đồ |
   % chốt | Khâu rò nặng nhất | Chênh so mốc KPI
   → Mốc KPI để so: kết nối/số ≥78% · đặt lịch/kết nối ≥50%. Các mốc khác chưa có →
     ghi `⚠ chưa có mốc so sánh`, KHÔNG tự đặt mốc rồi kết luận đạt/không đạt.
   → Cột "Khâu rò nặng nhất" = khâu có % thấp nhất so với mốc, hoặc thấp nhất
     so với trung bình các dịch vụ khác khi chưa có mốc.
   → Nhóm dưới 10 hội thoại: ghi ⚠ chưa đủ mẫu, KHÔNG kết luận khâu rò.

3. **Chân dung khách theo vấn đề & rào cản** — cột:
   Vấn đề răng | Số HT | Nhóm khách chủ đạo (N1–N6) | Độ tuổi/đặc điểm quan sát được |
   Rào cản số 1 | Rào cản số 2 | % mang rào cản NGỜ | Mong muốn chính nêu ra |
   Hàm ý cho nội dung
   Sáu nhóm khách: N1 mất răng trung–cao niên · N2 thẩm mỹ răng 22–40 ·
   N3 niềng 15–30 + phụ huynh · N4 đau cấp · N5 làm lại ca lỗi · N6 gia đình & trẻ em
   → Một hội thoại có thể mang nhiều rào cản. Ghi rõ cách đếm ở đầu bảng.
   → Cột "% mang rào cản NGỜ" (L6.2 + L6.7) là chỉ số đáng theo nhất của ngành nha:
     NGỜ cao mà Paris lại có bằng chứng mạnh nhất về vật liệu → đây là khoảng cách
     giữa thứ mình có và thứ mình đang nói.

4. **Rào cản toàn kỳ** — cột:
   Rào cản | Nhóm (SỢ/NGỜ/NGẠI) | L-code | Số ca | % trên tổng HT |
   Dịch vụ vướng nhiều nhất | Nhân viên xử lý được bao nhiêu ca | Bằng chứng nên dùng |
   Việc cần làm
   → Cột "Nhân viên xử lý được bao nhiêu ca": đếm số ca mà sau khi khách nêu rào cản,
     nhân viên có đưa ra bằng chứng/kịch bản phù hợp. Đây là chỗ nối sang R3.

5. **Chất lượng tư vấn — bản rút gọn** — cột:
   Chỉ số | Giá trị kỳ này | Mốc | Chênh | Hậu quả thấy được trong dữ liệu
   Tối thiểu các chỉ số: điểm chấm TB · % hội thoại đạt ≥8/10 · % có bước B5 đầy đủ ·
   % thu đủ 4 thông tin · % đưa bằng chứng đúng rào cản · số ca vi phạm ngôn từ.
   → Chạy R3 rồi thì DÙNG LẠI kết quả, không chấm lại.
   → Chưa chạy R3 thì chấm rút gọn 4 tiêu chí: ①②⑤⑩, và ghi rõ là bản rút gọn.

6. **Hiệu quả quảng cáo — bản rút gọn** — cột:
   Mã post | Góc tiếp cận | Số HT | % có SĐT | % HOT | % V1 | Khuyến nghị | Đủ mẫu?
   → Chạy R2 rồi thì DÙNG LẠI kết quả. Chưa chạy thì ghi `⚠ chưa có dữ liệu post`,
     KHÔNG suy đoán.
   → Luôn có cột %V1. Xếp hạng post chỉ bằng %HOT là quyết sai ngân sách ngành nha.

7. **Tệp giá trị dài hạn** ⭐ — sheet riêng của ngành nha. Cột:
   Nhóm tệp | Số HT | Mô tả | Vì sao đáng giữ | Nhịp chạm đề xuất | Ai phụ trách
   Tối thiểu các nhóm:
   - **WARM/COLD · V1** — chưa sẵn sàng nhưng là ca Implant/All-On/Invisalign.
     Nuôi tới 90 ngày, không hạ tệp ở 30 ngày như nhóm khác
   - **Đã đến khám chưa chốt phác đồ** — khách đã bỏ công đến tận nơi, đây là tệp
     nóng nhất mà hay bị bỏ nhất
   - **V-01 làm lại ca lỗi** — ngờ rất nặng, chu kỳ dài, giá trị cao
   - **Có dấu hiệu gia đình** — hội thoại nhắc "cho con", "cả nhà", "vợ/chồng em cũng".
     Đếm riêng. Nhóm này hay bị chấm COLD vì không đặt lịch ngay, nhưng là cửa LTV
     mạnh nhất của Paris
   - **Đang điều trị / đang niềng** — cross-sell tự nhiên, xem P3 §4
   - **Đã nhổ răng chưa trồng lại** — mất răng để lâu thì tiêu xương, trồng lại khó
     và đắt hơn. Lý do cấp thiết CÓ THẬT, hợp pháp, đúng y khoa
   → Mỗi nhóm phải có con số đếm được. Nhóm không đếm được từ dữ liệu → ghi
     `⚠ chưa đo được`, nêu cần thêm dữ liệu gì.

8. **Dữ liệu thô & cách tính** — cột:
   Chỉ số | Công thức | Tử số | Mẫu số | Nguồn dữ liệu | Hạn chế khi đọc
   → Bắt buộc có sheet này. Lãnh đạo hỏi "số này ở đâu ra" thì mở sheet này, không
     phải hỏi lại người làm báo cáo.

# BẢN TÓM TẮT 1 TRANG — in ra trong chat
Cấu trúc:
- **3 câu kết luận**, mỗi câu một con số, viết cho người không đọc bảng
- **Phễu toàn kỳ** 1 bảng nhỏ
- **Phễu tách V1/V2/V3** 1 bảng nhỏ — kèm một câu nhận định về chênh lệch
- **Khâu rò nặng nhất** và nó làm mất bao nhiêu lead trong kỳ
- **3 việc tháng tới**, mỗi việc có người phụ trách và cách đo kết quả
- **Điều chưa đo được** — liệt kê, và nói rõ cần xin dữ liệu gì từ ai

# QUY TẮC
- Mọi con số phải đếm được. Không ước lượng, không làm tròn đẹp.
- Nhóm dưới 10 hội thoại: ⚠ chưa đủ mẫu, không kết luận khâu rò.
- Chưa có mốc KPI: nêu số thật + `⚠ chưa có mốc so sánh`. KHÔNG tự đặt mốc rồi
  kết luận đạt/không đạt.
- Không lấy "đặt lịch khám" thay cho "đến khám".
- Mọi bảng phễu tách theo V1/V2/V3.
- Mỗi con số đi kèm một việc phải làm. Số không gắn hành động thì bỏ khỏi báo cáo.
- Mọi con số giá/ưu đãi trích từ hội thoại: ghi rõ "nhân viên đã nói với khách", gắn ⚠.
- Phát hiện hai nhân viên báo hai giá hoặc hai mức ưu đãi khác nhau cho cùng dịch vụ
  → ĐƯA LÊN SHEET 1, không ghi chú nhỏ ở cuối.
- Không đưa số điện thoại, thông tin định danh khách vào file.
- Phần có tên nhân viên: chỉ để ở sheet 5 dạng tổng hợp, không xếp hạng cá nhân
  trong báo cáo này (xếp hạng cá nhân thuộc R3).

# CÁCH LÀM
1. Đọc dữ liệu. Báo: số hội thoại · khoảng thời gian · có số đặt lịch/đến khám không ·
   mẫu là toàn bộ hay đã lọc · đã chạy R1/R2/R3 cho kỳ này chưa.
   DỪNG LẠI cho tôi xác nhận.
2. Dựng phễu. In bảng phễu toàn kỳ + bảng phễu tách V1/V2/V3.
   DỪNG LẠI cho tôi xác nhận con số.
3. Ghi file Excel + in bản tóm tắt 1 trang.
4. Tự kiểm và báo: tổng hội thoại mọi sheet có bằng nhau không · có nhóm nào <10 HT
   mà vẫn kết luận không · có chỗ nào lấy "đặt lịch" thay "đến khám" không ·
   mỗi con số ở sheet 1 có gắn một việc phải làm không.
````

## Đến đây

---

## Lưu ý khi dùng

**Chạy R4 sau cùng.** Nó dùng lại kết quả của R1 (phân loại), R2 (quảng cáo), R3 (chất lượng tư vấn). Chạy R4 đầu tiên thì sheet 5 và sheet 6 chỉ còn bản rút gọn, giá trị thấp hơn nhiều.

**Sheet 7 là phần hay bị bỏ nhưng đáng tiền nhất.** Ở ngành nha, tệp "đã đến khám mà chưa chốt phác đồ" và tệp "đã nhổ răng chưa trồng lại" là hai nhóm khách đã tự chứng minh họ có nhu cầu thật — mà thường không ai chăm, vì họ không xuất hiện trong báo cáo lead mới.

**Phần "điều chưa đo được" không phải phần thừa.** Nó là danh sách việc cần làm để báo cáo tháng sau tốt hơn. Báo cáo nào cũng kết thúc bằng mục này thì sau 3 kỳ, dữ liệu đủ để đo cả phễu.

**Đừng gộp V1/V2/V3 vì "cho gọn".** Một kỳ có 200 inbox cạo vôi và 20 inbox All-On sẽ cho ra bảng phễu trông rất đẹp — trong khi 20 ca All-On rò hết mà không ai thấy. Đây là lỗi đọc số đặc trưng của ngành nha.
