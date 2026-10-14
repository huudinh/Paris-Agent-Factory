# R3 — CHẤT LƯỢNG TƯ VẤN & KẾ HOẠCH ĐÀO TẠO

**Trả lời câu hỏi:** *Nhân viên trực page đang hổng khâu nào, mất khách ở bước nào, và tuần tới phải dạy gì cho ai.*

**Cần có:** file hội thoại **có dấu thời gian từng tin** và **tên người phụ trách**.
**Nhận lại:** 1 file Excel — `output/Paris_ChatLuongTuVan_<KỲ>.xlsx`, 7 sheet.

> 🔒 **Báo cáo này có tên người thật.** Dùng cho **đào tạo và định tuyến**, không đưa vào nội dung gửi khách, không chia sẻ ra ngoài nhóm quản lý. Phần xếp hạng cá nhân để sheet riêng, có thể ẩn khi trình bày chung.

> **📎 Có code mẫu sẵn.** Không cần viết `openpyxl` từ đầu — [`tools/xuat_bao_cao.py`](../tools/xuat_bao_cao.py) đã dựng đúng cấu trúc sheet, định dạng và sheet chú giải của báo cáo này:
> ```
> python phan_loai.py --src <file hội thoại> --out rows.json
> python xuat_bao_cao.py --bao-cao R3 --rows rows.json --ky "<kỳ>" --out ../output
> ```
> Ô nào script không tính được thì để `⚠` cho người hoặc trợ lý điền. Style dùng chung ở [`tools/excel_style.py`](../tools/excel_style.py) — sửa quy ước màu ở đó thì đổi cả hệ.

---

## Thiếu dấu thời gian thì sao

Tiêu chí ① (phản hồi ≤2 phút) cần dấu thời gian từng tin. Không có thì:
- **Không cho 0 điểm oan.** Ghi `⚠ không đo được tiêu chí ①`, chấm trên 9 tiêu chí còn lại, và **đổi chuẩn đạt sang ≥7/9**.
- Nói rõ trên sheet Tổng quan rằng điểm của kỳ này không so được với kỳ có đủ dấu thời gian.

Cùng cách xử lý cho tiêu chí ⑧ (phiếu bàn giao) khi dữ liệu không có phần ghi chú nội bộ.

---

## PROMPT — copy từ đây

````
# NHIỆM VỤ
Chấm chất lượng tư vấn của trực page từ file hội thoại, rồi sinh kế hoạch đào tạo.
Sinh ra ĐÚNG 1 file: `output/Paris_ChatLuongTuVan_{{KỲ}}.xlsx`

Đầu vào: {{FILE HỘI THOẠI}} · Kỳ: {{KỲ}} · Dịch vụ: {{DỊCH VỤ}}

Viết script Python dùng openpyxl, ghi file thật. Không chạy được code → nói rõ rồi
trả bảng markdown dán được vào Excel.

# BẢNG CHẤM 10 TIÊU CHÍ — CHUẨN ĐẠT ≥ 8/10

① PHẢN HỒI ≤ 2 PHÚT
   Đạt khi: chênh lệch dấu thời gian tin khách đầu tiên → tin nhân viên đầu tiên ≤ 2'.
   Không có dấu thời gian → ⚠ không đo được, KHÔNG cho 0 điểm.

② GỌI ĐÚNG TÊN DỊCH VỤ / TÌNH TRẠNG theo post khách bấm vào
   Đạt khi: tin mở nhắc đúng dịch vụ khách quan tâm.
   Không đạt khi: hỏi chung "anh/chị cần tư vấn gì ạ", hoặc dán lời chào mặc định.

③ THU ĐỦ 4 THÔNG TIN
   (a) tình trạng răng — VỊ TRÍ và BAO LÂU
   (b) ĐÃ ĐIỀU TRỊ Ở ĐÂU CHƯA
   (c) mong muốn — ăn nhai / thẩm mỹ / hết đau
   (d) thời gian dự kiến
   Đạt khi có cả 4. Thiếu mục nào thì ghi rõ thiếu mục nào.
   → Ngành nha cần 4 thông tin, nhiều hơn thẩm mỹ một mục: (b). Thiếu (b) thì không
     phát hiện được khách LÀM LẠI CA LỖI (V-01) — nhóm cần giọng tư vấn khác hoàn
     toàn và tuyệt đối không được chê nơi cũ.

④ TẠO TIN CẬY BẰNG BẰNG CHỨNG, ĐÚNG RÀO CẢN KHÁCH MANG
   Đạt khi: có ít nhất 1 bằng chứng thật, và bằng chứng đó khớp rào cản khách nêu.
   Bằng chứng thật, theo thứ tự ưu tiên:
     1. Đối tác hãng: Straumann (Implant) · Invisalign Black Diamond (niềng trong suốt)
        · Nacera (răng sứ) · Ormco Diamond Star (mắc cài)
     2. 100% bác sĩ tốt nghiệp ĐH Y, có chứng chỉ hành nghề
     3. Giấy phép KCB 2032/HNO-GPHĐ/CL1 (Sở Y tế Hà Nội)
     4. Công nghệ giảm đau: Piezotome · RECIPROC BLUE
     5. Bảo hành / trả góp
     6. Báo chí
   KHÔNG đạt khi: chỉ dùng tính từ ("uy tín", "chất lượng", "yên tâm nhé ạ").
   LỖI NẶNG riêng ngành nha: khách hỏi về VẬT LIỆU / TRỤ / PHÔI SỨ (rào cản L6.7)
   mà nhân viên KHÔNG nhắc đối tác hãng → đây là bỏ mất bằng chứng mạnh nhất của
   Paris đúng lúc cần nhất. Ghi riêng vào cột "lỗi bỏ sót bằng chứng".

⑤ XIN SỐ CÓ LÝ DO CÓ LỢI CHO KHÁCH
   Đạt: "để bác sĩ xem phim và báo lộ trình, chi phí sát với tình trạng của anh/chị".
   KHÔNG đạt: xin số trần, hoặc lý do "để em gửi ưu đãi/báo giá".

⑥ XÁC THỰC SỐ / ZALO
   Đạt khi: có hỏi số đó có Zalo không, hoặc đọc lại số để khách xác nhận.

⑦ PHÂN LOẠI HOT/WARM/COLD + NHÓM GIÁ TRỊ V
   Đạt khi: có ghi chú phân loại trong hội thoại hoặc phần ghi chú nội bộ.
   Không có phần ghi chú trong dữ liệu → ⚠ không đo được.

⑧ PHIẾU BÀN GIAO ĐỦ 13 TRƯỜNG
   Họ tên · SĐT · Zalo · Dịch vụ/vấn đề răng · Vị trí răng & thời gian bị ·
   Đã điều trị ở đâu chưa · Mong muốn · Rào cản chính · Thời gian dự kiến ·
   Khung giờ tiện · Độ nóng + Nhóm giá trị · Link hội thoại · Tên trực page
   Dữ liệu không có phần ghi chú bàn giao → ⚠ không đo được, KHÔNG cho 0 oan.

⑨ KHÔNG VI PHẠM NGÔN TỪ — VI PHẠM THÌ TOÀN HỘI THOẠI 0 ĐIỂM
   (a) Từ cấm: `cam kết 100%` · `khỏi 100%` · `tốt nhất` · `số 1` · `duy nhất` ·
       `không đau` · `an toàn tuyệt đối` · `không biến chứng` · `dùng vĩnh viễn` /
       `trọn đời` · `rẻ nhất` · `cam kết kết quả như hình`
   (b) Gắn chữ "CHÍNH HÃNG" cho vật liệu ngoài 4 hãng Straumann/Invisalign/
       Nacera/Ormco → SAI PHÁP LÝ, tính như từ cấm
   (c) Chốt một con số giá cuối cùng cho ca cụ thể qua tin nhắn → tính như từ cấm
       (nêu khung giá niêm yết thì KHÔNG phải lỗi)
   (d) Hứa thời gian điều trị cứng ("niềng xong trong 12 tháng") → tính như từ cấm
   (e) Chẩn đoán qua ảnh/mô tả ("răng chị bị viêm tủy rồi") → tính như từ cấm
   → Mỗi vi phạm phải TRÍCH NGUYÊN VĂN câu vi phạm làm bằng chứng.

⑩ NÊU RÕ BƯỚC TIẾP THEO
   Đạt khi có cả ba: TÊN người sẽ gọi · SỐ sẽ gọi đến · GIỜ gọi.
   → Đây là bước B5. Bỏ B5 là mất lead ở khâu đắt nhất: số đã xin được mà không
     gọi được. Đếm riêng tỷ lệ hội thoại có đủ B5.

# TÁM LỖI CẤM — ĐẾM RIÊNG, CÓ TRÍCH DẪN
1. Lờ câu hỏi giá (khách hỏi giá, nhân viên chỉ đáp "để lại số em tư vấn")
2. Bắn giá cứng cho một ca cụ thể
3. Dán mẫu máy móc — trả lời không dính gì tới điều khách vừa nói
4. Nói "không đau"
5. Gắn "chính hãng" sai
6. Xin số không có lý do, hoặc lý do "để gửi ưu đãi"
7. Xin số rồi để yên — không nhắn xác nhận ai gọi, số nào, mấy giờ
8. Hứa thời gian điều trị cứng

Lỗi 1 và lỗi 2 là HAI LỖI KHÁC NHAU, đừng gộp: lờ câu hỏi giá là né, bắn giá cứng
là nói quá. Cả hai đều sai, cách sửa ngược nhau.

# LỖI "TRƯỢT CÂU HỎI NGẦM" — chấm riêng, đây là lỗi hay gặp nhất
Nhân viên trả lời đúng chữ nhưng trượt điều khách thật sự đang hỏi:
| Khách gõ | Thật sự đang hỏi | Trả lời trượt là |
|---|---|---|
| "Bao nhiêu tiền?" | Tôi có đủ tiền không, có bị đội giá không | Chỉ bắn con số, không nói minh bạch chi phí / trả góp |
| "Có đau không?" | Tôi chịu được không, các anh có trung thực không | Nói "không đau" |
| "Trụ nào tốt?" | Các anh có tráo vật liệu của tôi không | Kể tên trụ mà không nói hãng và phiếu bảo hành |
| "Niềng bao lâu?" | Tôi phải chịu xấu/khó chịu bao lâu | Chỉ nói số tháng, không nói Invisalign trong suốt |
| "Bọc sứ có hại không?" | Tôi có mất răng thật không | Nói "không hại gì đâu ạ" |
| "Để em hỏi nhà đã" | Tôi chưa đủ tin để tự quyết khoản lớn | Ép chốt, hoặc buông luôn |
| "Em ở xa" | Đi lại nhiều lần có đáng không | Chỉ đọc địa chỉ cơ sở |
→ Đếm số hội thoại có lỗi này, kèm trích dẫn. Lỗi này KHÔNG trừ vào 10 tiêu chí
  (để tránh trừ hai lần), mà báo thành chỉ số riêng: "tỷ lệ trượt câu hỏi ngầm".

# CẤU TRÚC FILE EXCEL — 7 sheet

1. **Tổng quan**
   Kỳ · dịch vụ · nguồn dữ liệu · số hội thoại chấm được · ngày lập.
   Điểm trung bình toàn kỳ · % hội thoại đạt ≥8/10 · số hội thoại bị 0 điểm (vi phạm ⑨).
   Bảng: tiêu chí nào đạt cao nhất / thấp nhất, kèm %.
   **Khối cảnh báo:** tiêu chí nào không đo được và vì sao · mẫu là toàn bộ hay đã lọc ·
   điểm kỳ này có so được với kỳ trước không.
   3 kết luận chính, mỗi dòng một con số.

2. **Chú giải** — 10 tiêu chí · chuẩn đạt · luật 0 điểm · 8 lỗi cấm ·
   lỗi trượt câu hỏi ngầm · quy ước màu · ⚠.

3. **Chấm từng hội thoại** — một dòng mỗi hội thoại, cột:
   STT | Tên KH | Ngày | Phụ trách | Vấn đề răng | Nhóm giá trị | Độ nóng |
   ① | ② | ③ | ④ | ⑤ | ⑥ | ⑦ | ⑧ | ⑨ | ⑩ | Tổng điểm | Đạt? |
   Lỗi cấm mắc phải | Trượt câu hỏi ngầm? | Trích dẫn bằng chứng | Ghi chú
   → Mỗi tiêu chí ghi: 1 (đạt) · 0 (không đạt) · `⚠` (không đo được).
   → Cột "Trích dẫn bằng chứng" BẮT BUỘC có với mọi tiêu chí bị 0 và mọi lỗi cấm.
     Bảng điểm không có trích dẫn thì nhân viên không phục và trưởng nhóm không
     đào tạo được.
   → Che số điện thoại trong trích dẫn.

4. **Tiêu chí nào đang hổng** — cột:
   Tiêu chí | Số HT đạt | Số HT không đạt | Số HT không đo được | % đạt |
   Khâu phễu bị ảnh hưởng | Hậu quả thấy được trong dữ liệu | Học phần cần dạy
   → Sắp xếp theo % đạt tăng dần: tiêu chí hổng nhất lên đầu.
   → Cột "Hậu quả thấy được trong dữ liệu" phải dẫn số thật, ví dụ:
     "28 hội thoại thiếu B5 → trong đó 19 ca chuyển sang L5.3 gọi không bắt máy".

5. **Theo người phụ trách** 🔒 — cột:
   Tên NV | Số HT | Điểm TB | % đạt ≥8/10 | Số HT bị 0 điểm | Tỷ lệ xin được số |
   Tiêu chí mạnh nhất | Tiêu chí yếu nhất | Nhóm (A/B/C/D) | Học phần cần học
   Phân nhóm:
   - **A · Hạt nhân** — điểm TB cao, mạnh đều → làm mentor
   - **B · Yếu khâu chốt** — xin số tốt nhưng thiếu B5, thiếu ⑩
   - **C · Yếu khâu bằng chứng** — thiếu ④, hay dùng tính từ thay bằng chứng
   - **D · Yếu khâu mở / tân binh** — thiếu ①②③
   → NV dưới 10 hội thoại trong kỳ: ghi ⚠ chưa đủ mẫu, KHÔNG xếp nhóm, KHÔNG kết luận.
   → Sheet này là dữ liệu nhân sự nội bộ. Ghi chú rõ ở đầu sheet.

6. **Kế hoạch đào tạo 4 tuần** — cột:
   Học phần | Nội dung | Vì sao cần (dẫn số từ sheet 4) | Người học | Mentor đề xuất |
   Tuần | Cách đo kết quả
   Năm học phần tiêu chuẩn:
   - **M1 Mở hội thoại** — phản hồi 2' · chào theo đúng dịch vụ · 4 câu khám phá
   - **M2 Bằng chứng ngành nha** — đối tác hãng · xử lý câu "trụ nào tốt" ·
     xử lý câu "bọc sứ có hại không" · không nói "không đau"
   - **M3 Xin số & xác thực** — xin có lý do · kiểm Zalo · hỏi khung giờ · nhắn xác nhận
   - **M4 Chốt lịch khám** — xử lý 7 lý do từ chối · CTA khám + chụp phim ·
     đưa 2 khung giờ cụ thể
   - **M5 Phân loại & bàn giao** — HOT/WARM/COLD · nhóm giá trị V · phiếu 13 trường
   → Chỉ đưa vào kế hoạch học phần nào mà dữ liệu cho thấy đang hổng. Không rải đều.
   → Cột "Cách đo kết quả" phải nêu con số cụ thể sẽ đo lại sau 4 tuần.

7. **Rủi ro pháp lý** ⚠ — cột:
   STT HT | Ngày | Phụ trách | Loại vi phạm | Trích nguyên văn | Mức rủi ro | Việc cần làm
   Loại vi phạm: từ cấm · "chính hãng" sai · chốt giá cứng · hứa thời gian cứng ·
   chẩn đoán qua tin nhắn · nêu tên bác sĩ ngoài danh sách duyệt.
   → Sheet này đi lên trước mọi sheet khác khi trình bày. Một câu "cam kết 100%"
     trong inbox là rủi ro pháp lý, không phải lỗi kỹ năng.
   → Nếu kỳ này không có vi phạm nào: vẫn giữ sheet, ghi "Không phát hiện vi phạm
     trong <N> hội thoại đã chấm".

# QUY TẮC
- Mỗi tiêu chí bị 0 và mỗi lỗi cấm BẮT BUỘC có trích dẫn nguyên văn.
- Không đo được thì ghi ⚠, không cho 0 điểm. Và ghi rõ chuẩn đạt đã đổi thành gì.
- NV dưới 10 hội thoại: không xếp nhóm, không kết luận.
- Che số điện thoại, không đưa thông tin định danh khách vào file.
- Không suy ra thái độ hay động cơ của nhân viên. Chỉ ghi hành vi quan sát được
  trong hội thoại.
- Kế hoạch đào tạo phải dẫn số từ sheet 4. Học phần không có số chứng minh đang
  hổng thì không đưa vào.

# CÁCH LÀM
1. Tách hội thoại. Báo: số hội thoại · số có dấu thời gian · số có tên phụ trách ·
   số có phần ghi chú nội bộ · tiêu chí nào đo được, tiêu chí nào không.
   DỪNG LẠI cho tôi xác nhận.
2. Chấm 10 tiêu chí, lưu một bảng kết quả duy nhất.
3. In bảng tóm tắt: điểm TB · % đạt · số ca 0 điểm · 3 tiêu chí hổng nhất.
   DỪNG LẠI cho tôi xác nhận.
4. Ghi file Excel.
5. Tự kiểm và báo: mọi tiêu chí bị 0 có trích dẫn chưa · có NV nào <10 HT mà vẫn
   bị xếp nhóm không · sheet 7 có bỏ sót vi phạm nào mà sheet 3 đã ghi không ·
   kế hoạch đào tạo có học phần nào không dẫn được số không.
````

## Đến đây

---

## Lưu ý khi dùng

**Sheet 7 đọc trước, không đọc sau.** Một câu "cam kết 100%" hoặc một chữ "chính hãng" gắn sai trong inbox là rủi ro pháp lý ngành y tế — nặng hơn mọi con số điểm trung bình trong báo cáo.

**Sheet 5 là dữ liệu nhân sự.** Có tên người và đánh giá hiệu suất. Khi trình bày cho nhóm, ẩn sheet này hoặc chỉ nói theo nhóm A/B/C/D, không đọc tên kèm điểm trước cả nhóm.

**Đừng dùng điểm để phạt.** Bảng này được thiết kế để chỉ ra **học phần nào cần dạy**, không phải để xếp loại. Phần có giá trị nhất là sheet 4 — tiêu chí nào hổng và hậu quả thấy được bằng số.

**Tiêu chí ④ là chỗ ngành nha khác hẳn.** Ở thẩm mỹ, "tạo tin cậy" có thể làm bằng nhiều cách. Ở nha khoa, khách **không tự kiểm được vật liệu trong miệng mình** — nên bằng chứng đối tác hãng là thứ không có gì thay được. Nhân viên để trượt câu "trụ nào tốt" là để trượt đúng lúc Paris mạnh nhất.
