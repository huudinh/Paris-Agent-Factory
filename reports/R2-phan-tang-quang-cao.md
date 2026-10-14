# R2 — PHÂN TẦNG POST QUẢNG CÁO + BIỂU ĐỒ NHIỆT

**Trả lời câu hỏi:** *Post nào kéo về khách nóng, post nào chỉ kéo về người hỏi dạo — và post nào kéo về khách Implant, post nào kéo về khách cạo vôi.*

**Cần có:** danh sách post đang chạy **+** file hội thoại cùng kỳ.
**Nhận lại:** 1 file Excel — `output/Paris_PhanTang_QuangCao_<KỲ>.xlsx`, 13 sheet.

> **📎 Có code mẫu sẵn.** Không cần viết `openpyxl` từ đầu — [`tools/xuat_bao_cao.py`](../tools/xuat_bao_cao.py) đã dựng đúng cấu trúc sheet, định dạng và sheet chú giải của báo cáo này:
> ```
> python phan_loai.py --src <file hội thoại> --out rows.json
> python xuat_bao_cao.py --bao-cao R2 --rows rows.json --ky "<kỳ>" --out ../output
> ```
> Ô nào script không tính được thì để `⚠` cho người hoặc trợ lý điền. Style dùng chung ở [`tools/excel_style.py`](../tools/excel_style.py) — sửa quy ước màu ở đó thì đổi cả hệ.

---

## Hai chế độ — chọn đúng chế độ trước khi chạy

| Chế độ | Khi nào | Độ tin cậy |
|---|---|---|
| **A · ĐO THẬT** | Có cả danh sách post **và** file hội thoại cùng kỳ | Cao — đếm kết quả thật |
| **B · DỰ ĐOÁN** | Chỉ có post, chưa có hội thoại (post mới, hoặc kỳ cũ không còn log) | Thấp — chỉ là giả thuyết |

**Luôn ưu tiên chế độ A.** Hội thoại xuất từ CRM/Fanpage thường có thẻ nguồn ở tin đầu:

```
[Thẻ: Inbox từ quảng cáo QC_Implant_Straumann – Trồng răng Implant trụ Straumann…]
```

Thẻ này là **khoá nối** giữa post và hội thoại. Có nó thì không cần đoán.

Chạy chế độ A cho kỳ có dữ liệu trước, rút ra quy luật, rồi mới dùng chế độ B cho kỳ không có dữ liệu.

---

## ⚠ Đọc trước khi tin kết quả

**Mẫu phải là toàn bộ, không được lọc.** File hội thoại chỉ gồm "hội thoại dài" hoặc "hội thoại có số" thì đã **thiên về phía nóng** — dùng để so sánh post sẽ **thổi phồng chất lượng của mọi post, và thổi không đều nhau**.

→ Muốn so sánh post để quyết ngân sách, phải xin **toàn bộ hội thoại trong kỳ**, không lọc theo độ dài.

**Mẫu nhỏ không kết luận được.** Dưới 10 hội thoại thì con số % không nói lên gì. Prompt bắt đánh dấu `⚠ chưa đủ mẫu` cho các post này và **không xếp hạng chúng**.

**Riêng ngành nha — bẫy quan trọng nhất:** một post kéo 40 hội thoại cạo vôi và một post kéo 8 hội thoại Implant trông rất khác nhau trên bảng `% HOT`, nhưng giá trị thật thì ngược lại. **Bắt buộc đọc bảng phân tầng cùng với sheet 5 (Post × Nhóm giá trị).** Xếp hạng post chỉ bằng `% HOT` là quyết sai ngân sách cho ngành nha.

---

## PROMPT — copy từ đây

````
# NHIỆM VỤ
Phân tầng các post quảng cáo theo chất lượng VÀ giá trị khách mà chúng kéo về.
Sinh ra ĐÚNG 1 file: `output/Paris_PhanTang_QuangCao_{{KỲ}}.xlsx`

Viết script Python dùng openpyxl. Ghi ra file thật, không trả bảng trong chat.
Môi trường không chạy được code → nói rõ, rồi trả bảng markdown dán được vào Excel.

# ĐẦU VÀO
- Danh sách post đang quảng cáo: {{FILE POST}}
- File hội thoại cùng kỳ (nếu có): {{FILE HỘI THOẠI}}
- Dịch vụ: {{DỊCH VỤ}}   — ví dụ: Implant, Niềng răng, Bọc răng sứ, Tổng quát
- Kỳ: {{KỲ}}             — ví dụ: 01-31/10/2026

Chế độ chạy:
- Có file hội thoại  → CHẾ ĐỘ A (đo thật). Bắt buộc dùng chế độ này.
- Không có           → CHẾ ĐỘ B (dự đoán). Ghi rõ trên MỌI sheet rằng đây là giả thuyết.

# CHẾ ĐỘ A — ĐO THẬT

## A1. Nối post với hội thoại
Mỗi hội thoại có thẻ nguồn ở tin đầu dạng:
  [Thẻ: Inbox từ quảng cáo <TÊN POST> – <HEADLINE>]
Tách `<TÊN POST>` làm khoá nối. Chuẩn hoá trước khi gom:
- Bỏ hậu tố nhân bản: "- Bản sao", "- Bản sao 2", "_Group_1"… → gom về post gốc,
  NHƯNG giữ cột riêng ghi rõ đã gom những biến thể nào.
- Thẻ không phải quảng cáo (ví dụ "Ưu đãi và thông báo" = tin nhắn hàng loạt)
  → tách thành nhóm nguồn riêng, không xếp chung với post quảng cáo.
- Hội thoại không có thẻ → nhóm "Không rõ nguồn".

Báo ngay: tổng hội thoại · số nối được · số không nối được · số post duy nhất.

## A2. Chấm từng hội thoại (5 tín hiệu — giống R1)
① nêu dịch vụ/tình trạng răng cụ thể · ② mốc thời gian ≤14 ngày · ③ hỏi lịch/bác sĩ/
chi phí/trả góp theo tình trạng mình · ④ gửi ảnh răng hoặc phim X-quang hoặc mô tả rõ ·
⑤ để lại liên hệ và đồng ý nhận tư vấn
→ HOT 4–5 · WARM 2–3 · COLD 0–1.

BA LUẬT GHI ĐÈ bắt buộc áp: ① đã đặt lịch/đang đến → HOT · ② đã có phim X-quang hoặc
đã khám nơi khác có phác đồ → HOT · ③ đau cấp (V-06) → tối thiểu WARM.

Nếu đã chạy R1 cho cùng kỳ, DÙNG LẠI kết quả chấm đó, không chấm lại.

## A3. Gán nhóm vấn đề răng và nhóm giá trị cho từng hội thoại
11 nhóm vấn đề răng: V-01 làm lại ca lỗi · V-02 mất nhiều răng/cả hàm · V-03 mất răng lẻ ·
V-04 lệch-khấp khểnh-thưa-hô · V-05 xỉn-vỡ-sứt-mòn · V-06 đau-viêm tủy-áp xe ·
V-07 viêm nướu-vôi răng-hôi miệng · V-08 răng khôn-nhổ · V-09 tẩy trắng-Teeth Spa ·
V-10 trẻ em · V-11 chưa rõ. Xét ưu tiên từ trên xuống.

Nhóm giá trị: V1 (Implant · All-On · Invisalign · sứ toàn hàm) · V2 (sứ lẻ · Veneer ·
mắc cài) · V3 (cạo vôi · tẩy trắng · trám · nhổ · răng khôn · trẻ em · Teeth Spa).

## A4. Tính cho từng post
- Số hội thoại
- Tỷ lệ có SĐT (%)        ← bám KPI xin số của trực page
- Số và tỷ lệ HOT / WARM / COLD
- Điểm tín hiệu trung bình (0–5)
- PHÂN BỐ NHÓM GIÁ TRỊ: số và % hội thoại thuộc V1 / V2 / V3   ← đặc thù ngành nha
- Tầng chủ đạo = tầng chiếm tỷ lệ cao nhất
- Nhóm vấn đề răng chủ đạo
- Rào cản nổi bật: đếm các dấu hiệu trong hội thoại thuộc post đó —
  hỏi giá ngay · ở xa/ngoài 7 tỉnh có cơ sở · sợ đau · SỢ MÀI RĂNG ·
  NGỜ VẬT LIỆU/trụ/phôi sứ · so sánh nơi khác · chưa tài chính · hỏi người nhà ·
  chỉ Zalo/không nghe máy
- Đủ mẫu? ≥10 hội thoại = Đủ · <10 = ⚠ chưa đủ mẫu, không kết luận

# CHẾ ĐỘ B — DỰ ĐOÁN TỪ NỘI DUNG
Chỉ dùng khi không có hội thoại. Chấm từng post theo 5 đặc trưng, mỗi cái 1 điểm:
① Nêu TÌNH TRẠNG RĂNG CỤ THỂ để khách tự nhận ra mình (mất răng số 6, răng thưa,
   răng xỉn, hô) thay vì nói chung "làm răng đẹp"
② Nhắm ĐÚNG MỘT NHÓM khách (trung niên mất răng, phụ huynh, người bận, khách làm lại)
   thay vì nhắm tất cả
③ Nói về CHUYÊN MÔN hoặc VẬT LIỆU HÃNG (bác sĩ, Straumann, Invisalign, quy trình)
   thay vì chỉ nói giá
④ Có yếu tố GIẢM LO (giải đáp nỗi sợ đau, nỗi sợ mài răng, minh bạch quy trình, bảo hành)
⑤ CTA dẫn tới KHÁM + CHỤP PHIM, thay vì chỉ "inbox nhận giá"

→ 4–5 điểm: dự đoán kéo HOT · 2–3: WARM · 0–1: COLD
Ghi rõ đây là DỰ ĐOÁN, phải đối chiếu lại khi có hội thoại thật.

# CẤU TRÚC FILE EXCEL — 13 sheet, đúng thứ tự

1. **Tổng quan**
   Kỳ · dịch vụ · chế độ chạy (A hay B) · nguồn dữ liệu · ngày lập.
   Số post · số hội thoại · số nối được · số không rõ nguồn.
   Phân bố HOT/WARM/COLD toàn kỳ. Phân bố V1/V2/V3 toàn kỳ.
   **Khối cảnh báo phương pháp**, ghi rõ:
   - mẫu có phải toàn bộ hội thoại trong kỳ không, hay đã bị lọc
   - nếu đã lọc (ví dụ "ưu tiên hội thoại dài") → ghi rõ kết quả bị thiên về phía nóng,
     chỉ dùng tham khảo, KHÔNG dùng để quyết ngân sách
   - số post chưa đủ mẫu
   - **cảnh báo riêng ngành nha:** xếp hạng post chỉ bằng %HOT là quyết sai, phải đọc
     kèm sheet 5 (Post × Nhóm giá trị)
   3 kết luận chính, mỗi cái một dòng, có số kèm theo.

2. **Chú giải ký hiệu**
   HOT/WARM/COLD và 5 tín hiệu · 3 luật ghi đè · V1/V2/V3 · V-01…V-11 ·
   tỷ lệ có SĐT · điểm tín hiệu TB · tầng chủ đạo · ⚠ chưa đủ mẫu · góc tiếp cận ·
   các loại rào cản · quy ước màu.

3. **Phân tầng theo post** — một dòng mỗi post, cột đúng thứ tự:
   Mã post | Tên post (chuẩn hoá) | Biến thể đã gom | Dịch vụ | Thông điệp chính |
   Góc tiếp cận | Số HT | Tỷ lệ có SĐT | HOT | WARM | COLD | % HOT |
   Điểm TB | V1 | V2 | V3 | % V1 | Tầng chủ đạo | Vấn đề răng chủ đạo |
   Đủ mẫu? | Rào cản nổi bật
   → Sắp xếp theo % HOT giảm dần, nhưng đẩy mọi dòng ⚠ chưa đủ mẫu xuống cuối.

4. **Xếp hạng & khuyến nghị** — cột:
   Hạng | Mã post | % HOT | % V1 | Tỷ lệ có SĐT | Khuyến nghị | Lý do | Việc cần làm
   Khuyến nghị chọn trong 5 mức:
   - TĂNG NGÂN SÁCH — %HOT và tỷ lệ có SĐT đều trên trung bình kỳ
   - TĂNG NGÂN SÁCH (giá trị cao) — %HOT quanh trung bình NHƯNG %V1 cao rõ rệt.
     Đây là mức riêng của ngành nha: post kéo ít khách nhưng toàn khách Implant/
     All-On/Invisalign thì đáng tiền hơn post kéo đông khách cạo vôi
   - GIỮ NGUYÊN — quanh mức trung bình
   - SỬA THÔNG ĐIỆP — kéo được nhiều hội thoại nhưng tầng thấp, nêu sửa gì cụ thể
   - XEM XÉT TẮT — vừa ít hội thoại vừa tầng thấp vừa toàn V3
   Post ⚠ chưa đủ mẫu → khuyến nghị bắt buộc là "CHỜ THÊM DỮ LIỆU".
   → Cột "Việc cần làm" phải cụ thể: sửa câu nào, thêm bằng chứng gì, đổi CTA thành gì.

5. **Post × Nhóm giá trị** ⭐ — sheet riêng của ngành nha. Cột:
   Mã post | Góc tiếp cận | Số HT | V1 | V2 | V3 | % V1 | % HOT | % HOT trong nhóm V1 |
   Nhận định
   → Dùng để trả lời: post nào kéo về khách giá trị lớn. Đây là sheet quyết định
     ngân sách, không phải sheet 3.
   → Khối "Đọc nhanh" bên dưới nêu rõ: post nào nên tăng tiền dù %HOT thấp.

6. **Góc tiếp cận → tầng** — quy luật rút ra được, cột:
   Góc tiếp cận | Post đại diện | Số HT gộp | % HOT gộp | % V1 gộp |
   Tầng thường kéo về | Vấn đề răng thường kéo về | Vì sao | Dùng khi nào
   Tám góc tiếp cận cần phân biệt:
   - Giá / ưu đãi / trả góp (nêu con số giá, nhấn trả góp)
   - Công nghệ giảm đau (Piezotome, "không ê buốt", "nhổ răng êm")
   - Tình trạng cụ thể ("mất răng số 6", "răng thưa", "hô", "răng xỉn")
   - Giáo dục / giải đáp lo lắng ("bọc sứ có hại không", "implant bao lâu", "mài răng")
   - Chuyên môn / bác sĩ / đối tác hãng (Straumann, Invisalign Black Diamond, BS ĐH Y)
   - Case thật / before-after
   - Banner thông báo chương trình
   - Gói gia đình / trẻ em
   → Chỉ kết luận khi tổng hội thoại của góc đó ≥10. Chưa đủ thì ghi ⚠.

7. **Rào cản theo post** — post nào đẻ ra rào cản gì, cột:
   Mã post | Rào cản | Nhóm (SỢ/NGỜ/NGẠI) | Số ca | % trên tổng HT của post |
   Hàm ý cho thông điệp | Kịch bản cần chuẩn bị (mã S3.x / X.x)
   → Dùng để biết post nào cần sửa thông điệp từ gốc, post nào chỉ cần trang bị
     trước kịch bản xử lý cho trực page.
   → Chú ý riêng: post nói nhiều về giá thường đẻ ra rào cản NGỜ VẬT LIỆU (L6.7) —
     khách nghĩ "rẻ thế thì trụ gì". Nếu thấy quy luật này trong dữ liệu, nói thẳng.

8. **① Nhiệt · Vấn đề răng × Độ nóng** — biểu đồ nhiệt. Hàng = 11 nhóm vấn đề răng,
   cột = HOT/WARM/COLD. Cột phụ bên phải: Tổng HT · **% HOT** · **% HOT\*** · % cho số.
   > ⚠ **Bắt buộc có cột `% HOT*`.** Tín hiệu ① của thang chấm chính là "nêu dịch vụ/
   > tình trạng cụ thể". Bảng này lại chia nhóm THEO VẤN ĐỀ, nên mọi nhóm có vấn đề
   > cụ thể đã được cộng sẵn 1 điểm — cột `% HOT` bị **lặp vòng** và không so sánh được.
   > `% HOT*` chấm lại chỉ bằng 4 tín hiệu còn lại (②③④⑤), đạt ≥3/4 tính HOT*.
   > Ghi ngay dưới bảng: cột nào dùng được, cột nào không, và số thật là bao nhiêu.
   > Nếu bỏ tín hiệu ① mà chênh lệch biến mất → NÓI THẲNG LÀ KHÔNG CÓ BẰNG CHỨNG.

9. **② Nhiệt · Góc tiếp cận × Vấn đề răng** — mỗi góc quảng cáo kéo về nhóm vấn đề nào.
   Dùng để chọn góc khi viết content mới.

10. **③ Nhiệt · Vấn đề răng × Rào cản** — mỗi nhóm vấn đề thường vướng gì.
    Một hội thoại có thể mang nhiều rào cản — ghi rõ cách đếm ở đầu bảng.
    Dùng để biết nên sửa thông điệp từ gốc hay chỉ cần trang bị trước kịch bản.

11. **④ Nhiệt · Post × Độ nóng** — như sheet 3 nhưng dạng nhiệt, có cột *Đủ mẫu?*

12. **Mẫu hội thoại thực tế** — mỗi nhóm vấn đề răng tối đa 3 ca, cột:
    Vấn đề răng | HT# | Độ nóng | Nhóm giá trị | Có SĐT | Post | Trích lời khách
    → **Che số điện thoại** trong phần trích. Đây là phần giúp người đọc kiểm tra
      máy phân loại có đúng không — bảng số mà không có ví dụ thì không ai tin được.

13. **Dữ liệu thô** — để kiểm chứng lại, cột:
    STT HT | Tên KH | Ngày | Thẻ nguồn gốc (nguyên văn) | Mã post sau chuẩn hoá |
    Có SĐT | Bitmask tín hiệu | Ghi đè? | Độ nóng | Vấn đề răng | Nhóm giá trị | L-code
    → Bắt buộc có sheet này. Không có thì không ai kiểm được con số ở sheet 3.
    → Cột "Ghi đè?" ghi rõ luật nào đã áp (đã đặt lịch / đã có phim / đau cấp).

# KHI CHẠY NHIỀU KỲ
Từ 2 kỳ trở lên thì thêm sheet cuối: **So sánh kỳ** — xem khuôn R5.
→ Chỉ so sánh ở mức GÓC TIẾP CẬN, không so từng post, vì post thường đổi tên và
  nhân bản giữa các kỳ nên không khớp 1-1.
→ Nêu rõ hai kỳ có cùng cách lấy mẫu không. Khác cách lấy mẫu thì không so sánh được.

# QUY TẮC
- Mọi con số phải đếm được từ dữ liệu. Không ước lượng, không làm tròn đẹp.
- Post dưới 10 hội thoại: ghi ⚠ chưa đủ mẫu, KHÔNG xếp hạng, KHÔNG khuyến nghị.
- **Kiểm tra lặp vòng trước khi kết luận.** Khi chia nhóm theo một thuộc tính X mà X
  lại là một trong các tín hiệu dùng để chấm điểm, thì chênh lệch điểm giữa các nhóm
  là giả. Phải chấm lại không kể tín hiệu đó rồi mới so sánh. Nếu sau khi bỏ mà chênh
  lệch biến mất, phải nói thẳng là KHÔNG CÓ BẰNG CHỨNG, không được giữ kết luận cũ.
- **Không xếp hạng post chỉ bằng %HOT.** Luôn đọc kèm %V1 (sheet 5).
- Không suy ra hiệu quả quảng cáo từ nội dung post khi đã có dữ liệu thật.
- Không đưa số điện thoại hay thông tin định danh khách vào file.
- Số ưu đãi/giá xuất hiện trong post thì trích nguyên văn và gắn ⚠.
- Post nào dùng chữ "chính hãng" cho vật liệu ngoài Straumann/Invisalign/Nacera/Ormco
  → ghi vào cột riêng "⚠ rủi ro pháp lý", báo lên sheet Tổng quan.
- Post nào có từ cấm (`không đau`, `tốt nhất`, `rẻ nhất`, `cam kết 100%`,
  `dùng vĩnh viễn`) → ghi vào cùng cột rủi ro pháp lý đó.

# QUY TẮC VẼ BIỂU ĐỒ NHIỆT
- Tô nhiệt bằng conditional formatting kiểu color scale (openpyxl: `ColorScaleRule`),
  KHÔNG tô màu cứng từng ô. Thang: trắng (nhỏ nhất) → vàng cam (phân vị 50) → đỏ (lớn nhất).
- Chỉ tô nhiệt vùng ô đếm. Cột Tổng / % / Đủ mẫu để nền vàng nhạt, không tô nhiệt —
  nếu tô chung, cột % sẽ át hết vì thang giá trị khác hẳn.
- Mỗi bảng một thang màu riêng. Ghi rõ màu chỉ so sánh trong cùng một bảng.
- Mỗi bảng nhiệt phải có một khối "Đọc nhanh" ngay dưới, nêu 2–4 điều rút ra, mỗi
  điều kèm con số. Không có diễn giải thì bảng màu chỉ để nhìn cho đẹp.
- Ô dưới 10 ca: nói rõ trong phần Đọc nhanh là không kết luận được.

# TRÌNH BÀY
Font Arial · freeze dòng tiêu đề · wrap text cột dài · tiêu đề nền đậm chữ trắng.
Màu: đỏ nhạt HOT · cam WARM · xanh dương nhạt COLD · vàng mọi ô ⚠ ·
xanh lá nhạt khuyến nghị TĂNG NGÂN SÁCH · xám dòng chưa đủ mẫu ·
viền đậm dòng có %V1 cao.

# CÁCH LÀM — theo thứ tự
1. Đọc dữ liệu. Báo: số post · số hội thoại · số nối được qua thẻ · số không rõ nguồn ·
   mẫu là toàn bộ hay đã bị lọc.
2. Liệt kê danh sách post sau chuẩn hoá, kèm các biến thể đã gom vào.
   DỪNG LẠI cho tôi xác nhận việc gom có đúng không.
3. Chấm và tính chỉ số từng post.
4. In bảng tóm tắt: post · số HT · %HOT · %V1 · tỷ lệ có SĐT · đủ mẫu chưa.
   DỪNG LẠI cho tôi xác nhận con số.
5. Ghi file Excel.
6. Tự kiểm và báo: tổng HT ở sheet 3 có bằng tổng ở sheet 8 không · có post nào
   <10 HT mà vẫn bị xếp hạng không · cột %HOT* đã có chưa và kết luận có đổi không ·
   còn số nào chưa gắn ⚠ không · có post nào dùng "chính hãng" sai mà chưa gắn cờ không.
````

## Đến đây

---

## Chuẩn bị dữ liệu đầu vào

Xem [`doc/mau-du-lieu/MAU_Danh-sach-post.md`](../doc/mau-du-lieu/MAU_Danh-sach-post.md) — có bảng điền sẵn.

Danh sách post cần tối thiểu: **tên post đúng như hiển thị trong thẻ hội thoại** (đây là khoá nối, sai tên là không nối được) · nội dung/headline · dịch vụ · thời gian chạy. Có thêm chi tiêu, reach, số inbox thì tốt — nhưng không bắt buộc, vì prompt này đo chất lượng lead chứ không đo chi phí.

Muốn ra được **chi phí trên một lead HOT·V1** thì cần thêm cột chi tiêu từng post. Với ngành nha, đây là con số đáng đo nhất: một lead Implant đắt hơn một lead cạo vôi nhiều lần, nên cùng một mức CPL thì ý nghĩa hoàn toàn khác nhau.

## Vì sao bản nha khoa có thêm sheet 5

Ở thẩm mỹ, các dịch vụ chạy quảng cáo có giá tương đối gần nhau, nên `% HOT` đủ để xếp hạng post. Ở nha khoa thì không: **dải giá rộng từ vài trăm nghìn tới vài trăm triệu**. Một post banner "cạo vôi 0đ" sẽ thắng mọi post Implant trên bảng `% HOT` — và nếu xếp hạng theo đó thì sẽ dồn ngân sách vào đúng chỗ ít tiền nhất.

Sheet 5 (Post × Nhóm giá trị) và mức khuyến nghị **TĂNG NGÂN SÁCH (giá trị cao)** là để chống đúng cái bẫy đó.
