# R5 — SO SÁNH HAI KỲ

**Trả lời câu hỏi:** *Tháng này có tốt lên không, tốt lên nhờ cái gì, và cái gì đang xấu đi.*

**Cần có:** dữ liệu của **hai kỳ đã chạy R1** (và R2/R3 nếu muốn so sâu hơn).
**Nhận lại:** 1 file Excel — `output/Paris_SoSanh_<KỲ1>_vs_<KỲ2>.xlsx`, 7 sheet.

> **📎 Có code mẫu sẵn.** Không cần viết `openpyxl` từ đầu — [`tools/xuat_bao_cao.py`](../tools/xuat_bao_cao.py) đã dựng đúng cấu trúc sheet, định dạng và sheet chú giải của báo cáo này:
> ```
> python phan_loai.py --src <file hội thoại> --out rows.json
> python xuat_bao_cao.py --bao-cao R5 --rows rows.json --ky "<kỳ>" --out ../output
> ```
> Ô nào script không tính được thì để `⚠` cho người hoặc trợ lý điền. Style dùng chung ở [`tools/excel_style.py`](../tools/excel_style.py) — sửa quy ước màu ở đó thì đổi cả hệ.

---

## 🛑 Cổng chặn: hai kỳ có so được với nhau không

**Đây là bước đầu tiên, và nó có quyền dừng cả báo cáo.** So hai kỳ lấy mẫu khác nhau thì mọi con số chênh lệch đều vô nghĩa — và tệ hơn là nó sẽ được dùng để ra quyết định.

Bốn câu phải trả lời được "giống nhau" trước khi so:

| # | Câu hỏi | Khác nhau thì sao |
|---|---|---|
| ① | Hai kỳ có cùng **cách lấy mẫu** không? (toàn bộ hội thoại, hay đã lọc theo độ dài / theo có số) | **DỪNG.** Không so được. Chỉ được so trong nội bộ từng kỳ |
| ② | Hai kỳ có cùng **phạm vi dịch vụ** không? | Chỉ so phần dịch vụ trùng nhau, nói rõ đã loại gì |
| ③ | Hai kỳ có cùng **cách chấm** không? (cùng bộ 5 tín hiệu, cùng 3 luật ghi đè) | Chấm lại kỳ cũ theo chuẩn mới, hoặc dừng |
| ④ | Hai kỳ có **độ dài tương đương** không? (10 ngày vs 31 ngày thì không) | Quy về chỉ số tỷ lệ, không so số tuyệt đối |

**Khác ở ①** → báo cáo chỉ được trả về một trang: *vì sao không so được, và cần làm gì để kỳ sau so được*. Không chạy tiếp.

---

## PROMPT — copy từ đây

````
# NHIỆM VỤ
So sánh hai kỳ và chỉ ra điều gì tốt lên, điều gì xấu đi, nhờ cái gì.
Sinh ra ĐÚNG 1 file: `output/Paris_SoSanh_{{KỲ1}}_vs_{{KỲ2}}.xlsx`

Đầu vào:
- Dữ liệu kỳ 1: {{DỮ LIỆU KỲ 1}}   — kỳ: {{KỲ1}}
- Dữ liệu kỳ 2: {{DỮ LIỆU KỲ 2}}   — kỳ: {{KỲ2}}

Viết script Python dùng openpyxl, ghi file thật. Không chạy được code → nói rõ rồi
trả bảng markdown dán được vào Excel.

# BƯỚC 0 — CỔNG CHẶN, LÀM TRƯỚC MỌI THỨ
Trả lời 4 câu, in ra ngay trong chat:
① Hai kỳ có cùng CÁCH LẤY MẪU không? (toàn bộ hội thoại, hay đã lọc theo độ dài /
   theo có số điện thoại)
② Hai kỳ có cùng PHẠM VI DỊCH VỤ không?
③ Hai kỳ có cùng CÁCH CHẤM không? (cùng bộ 5 tín hiệu, cùng 3 luật ghi đè của
   ngành nha: đã đặt lịch → HOT · đã có phim X-quang → HOT · đau cấp → tối thiểu WARM)
④ Hai kỳ có ĐỘ DÀI tương đương không?

- Khác ở ① → DỪNG. Chỉ trả về một trang: vì sao không so được, cần làm gì để kỳ sau
  so được. KHÔNG chạy tiếp, KHÔNG đưa ra con số chênh lệch nào.
- Khác ở ② → chỉ so phần dịch vụ trùng nhau, ghi rõ đã loại những gì.
- Khác ở ③ → chấm lại kỳ cũ theo chuẩn hiện hành, ghi rõ đã chấm lại. Không chấm
  lại được thì dừng.
- Khác ở ④ → chỉ so chỉ số TỶ LỆ, không so số tuyệt đối. Ghi rõ trên mọi sheet.

DỪNG LẠI cho tôi xác nhận kết quả cổng chặn trước khi tiếp tục.

# NGUYÊN TẮC SO SÁNH
- **So ở mức GÓC TIẾP CẬN, không so từng post.** Post hay bị nhân bản và đổi tên giữa
  các kỳ ("- Bản sao", "_Group_1") nên không khớp 1-1 được.
- **Chênh lệch dưới mức dao động tự nhiên thì KHÔNG gọi là thay đổi.** Quy tắc:
  nhóm dưới 30 hội thoại thì chênh lệch dưới 10 điểm % là nhiễu, không kết luận.
  Nhóm 30–100 thì dưới 5 điểm %. Trên 100 thì dưới 3 điểm %.
  Ghi rõ ngưỡng đã dùng ở đầu bảng.
- **Nhóm dưới 10 hội thoại ở MỘT trong hai kỳ → không so.** Ghi ⚠ chưa đủ mẫu.
- **Không gán nguyên nhân khi chưa có bằng chứng.** Chỉ được nói "tăng cùng lúc với
  việc X" nếu X có trong dữ liệu. Không suy ra "nhờ đào tạo nên tăng" khi không đo
  được điều đó.

# CẤU TRÚC FILE EXCEL — 7 sheet

1. **Tổng quan & cổng chặn**
   Kết quả 4 câu cổng chặn, ghi rõ ràng.
   Ngưỡng nhiễu đã dùng cho từng cỡ mẫu.
   Bảng so sánh tổng: số inbox · % có SĐT · % HOT · % V1 · điểm chấm TB · % đến khám.
   3 KẾT LUẬN, mỗi dòng: chỉ số nào đổi · đổi bao nhiêu · có vượt ngưỡng nhiễu không ·
   bằng chứng về nguyên nhân (hoặc "chưa xác định được nguyên nhân").
   **Khối cảnh báo:** điều gì không so được và vì sao.

2. **Chú giải ký hiệu** — như các báo cáo khác, THÊM hai mục riêng của R5:
   *ngưỡng nhiễu* (chênh dưới mức dao động tự nhiên thì không gọi là thay đổi)
   và *tương quan ≠ nhân quả*.

3. **So theo chỉ số phễu** — cột:
   Chỉ số | Kỳ 1 | Kỳ 2 | Chênh (điểm %) | Vượt ngưỡng nhiễu? | Nhận định |
   Bằng chứng về nguyên nhân
   Tối thiểu: % có SĐT · % kết nối · % đặt lịch khám · % đến khám · % chốt phác đồ ·
   % HOT · % WARM · % COLD · % V1 · % V2 · % V3 · điểm chấm TB · % đạt ≥8/10.
   → Cột "Vượt ngưỡng nhiễu?" ghi CÓ / KHÔNG. Ghi KHÔNG thì cột Nhận định phải là
     "chưa kết luận được", không được viết nhận định có hướng.

4. **So theo nhóm giá trị V1/V2/V3** ⭐ — cột:
   Nhóm giá trị | Chỉ số | Kỳ 1 | Kỳ 2 | Chênh | Vượt ngưỡng? | Nhận định
   → Đây là sheet quan trọng nhất của ngành nha. Một kỳ có thể tăng tổng số lead
     mà lại GIẢM lead V1 — tổng trông đẹp hơn trong khi doanh thu kỳ vọng giảm.
     Chỉ nhìn số tổng là không thấy.
   → Nếu thấy hiện tượng đó, đưa thẳng lên sheet 1.

5. **So theo góc tiếp cận** — cột:
   Góc tiếp cận | Số HT kỳ 1 | Số HT kỳ 2 | % HOT kỳ 1 | % HOT kỳ 2 | Chênh %HOT |
   % V1 kỳ 1 | % V1 kỳ 2 | Chênh %V1 | Vượt ngưỡng? | Nhận định | Dùng tiếp hay đổi
   Tám góc: Giá-ưu đãi-trả góp · Công nghệ giảm đau · Tình trạng cụ thể ·
   Giáo dục-giải đáp lo lắng · Chuyên môn-bác sĩ-đối tác hãng · Case thật/before-after ·
   Banner thông báo · Gói gia đình-trẻ em.
   → Góc nào chỉ xuất hiện ở một kỳ: ghi rõ, không so.

6. **So theo rào cản** — cột:
   Rào cản | Nhóm (SỢ/NGỜ/NGẠI) | % kỳ 1 | % kỳ 2 | Chênh | Vượt ngưỡng? |
   Nhân viên xử lý được bao nhiêu (kỳ 1 → kỳ 2) | Nhận định
   → Chỉ số đáng theo nhất: **tỷ lệ ca mang rào cản NGỜ (L6.2 + L6.7) mà nhân viên
     CÓ đưa bằng chứng đối tác hãng**. Nếu chỉ số này tăng mà % đặt lịch cũng tăng,
     đó là bằng chứng gần nhất cho việc đào tạo có tác dụng.
   → Vẫn phải ghi rõ đây là tương quan, không phải nhân quả.

7. **Dữ liệu thô & cách tính** — cột:
   Chỉ số | Công thức | Tử/mẫu kỳ 1 | Tử/mẫu kỳ 2 | Nguồn | Hạn chế khi đọc
   → Bắt buộc có. Không có sheet này thì không ai kiểm được con số chênh lệch.

# QUY TẮC
- Cổng chặn ở bước 0 có quyền dừng cả báo cáo. Không bỏ qua.
- Chênh lệch chưa vượt ngưỡng nhiễu → ghi "chưa kết luận được", KHÔNG viết nhận định
  có hướng ("có dấu hiệu cải thiện" cũng là nhận định có hướng — không được viết).
- Không gán nguyên nhân khi chưa có bằng chứng trong dữ liệu.
- Không so từng post, chỉ so góc tiếp cận.
- Nhóm dưới 10 HT ở một trong hai kỳ → không so.
- Không đưa thông tin định danh khách vào file.

# CÁCH LÀM
1. Chạy cổng chặn bước 0. In kết quả 4 câu.
   DỪNG LẠI cho tôi xác nhận.
2. Tính ngưỡng nhiễu theo cỡ mẫu từng nhóm. In bảng ngưỡng.
3. So các chỉ số. In bảng tóm tắt: chỉ số nào vượt ngưỡng, chỉ số nào không.
   DỪNG LẠI cho tôi xác nhận.
4. Ghi file Excel.
5. Tự kiểm và báo: có chỉ số nào chưa vượt ngưỡng mà vẫn bị viết nhận định có hướng
   không · có nhóm nào <10 HT mà vẫn bị so không · có chỗ nào gán nhân quả mà không
   có bằng chứng không.
````

## Đến đây

---

## Lưu ý khi dùng

**Ngưỡng nhiễu là phần quan trọng nhất của báo cáo này.** Không có nó thì mọi dao động tự nhiên đều bị đọc thành "tốt lên" hoặc "xấu đi", và quyết định sẽ chạy theo nhiễu. Một post có 12 hội thoại kỳ trước và 15 kỳ này, tỷ lệ HOT từ 33% lên 40% — nghe như tăng 7 điểm, thực tế là 4 ca thành 6 ca. Không nói lên gì.

**Sheet 4 (So theo nhóm giá trị) là chỗ ngành nha dễ bị lừa nhất.** Tổng lead tăng mà lead V1 giảm là tình huống rất hay xảy ra khi chuyển ngân sách sang post banner giá rẻ: số inbox tăng vọt, báo cáo trông đẹp, doanh thu kỳ vọng lại giảm. Bảng tổng không bắt được điều đó.

**"Tương quan" không phải "nhân quả".** Báo cáo này chỉ được nói *"X tăng cùng lúc với Y"*. Muốn kết luận nhân quả thì cần thiết kế khác: giữ nguyên mọi thứ, chỉ đổi một yếu tố, rồi so. Đừng để báo cáo so sánh kỳ gánh việc đó.

**Chạy R5 từ kỳ thứ hai trở đi.** Và từ bây giờ, mỗi kỳ nên lưu lại file dữ liệu thô của R1 — đó là thứ làm cho R5 kỳ sau chạy được.
