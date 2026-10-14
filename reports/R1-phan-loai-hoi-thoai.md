# R1 — PHÂN LOẠI & KỊCH BẢN HỘI THOẠI

**Trả lời câu hỏi:** *Khách inbox tháng này là ai, đang vướng gì, và nhắn lại thế nào.*

**Cần có:** một file hội thoại đã xuất ra (`.md`, `.txt`, `.docx` hoặc `.xlsx` đều được).
**Nhận lại:** 2 file Excel.

| File | Góc nhìn |
|---|---|
| `output/Paris_<DV>_PhanLoai_KichBan.xlsx` | **QUY TRÌNH** — mỗi hội thoại đi trọn 4 bước trên một dòng, có sẵn tin nhắn gửi được ngay |
| `output/Paris_KichBan_<DV>.xlsx` | **PHÂN LOẠI + BANK KỊCH BẢN** — chi tiết từng hội thoại + bộ kịch bản theo nhóm A/B/C |

> **Trước khi chạy:** thay `{{FILE}}` và `{{DỊCH VỤ}}` ở đầu prompt. Dịch vụ ví dụ: *Implant · Niềng răng · Bọc răng sứ · Tổng quát*.

> **📎 Có code mẫu sẵn.** Không cần viết `openpyxl` từ đầu — [`tools/xuat_bao_cao.py`](../tools/xuat_bao_cao.py) đã dựng đúng cấu trúc sheet, định dạng và sheet chú giải của báo cáo này:
> ```
> python phan_loai.py --src <file hội thoại> --out rows.json
> python xuat_bao_cao.py --bao-cao R1 --rows rows.json --ky "<kỳ>" --out ../output
> ```
> Ô nào script không tính được thì để `⚠` cho người hoặc trợ lý điền. Style dùng chung ở [`tools/excel_style.py`](../tools/excel_style.py) — sửa quy ước màu ở đó thì đổi cả hệ.

---

## PROMPT — copy từ đây

````
# NHIỆM VỤ
Đọc file hội thoại `{{FILE}}` và sinh ra ĐÚNG 2 file Excel trong thư mục `output/`.
Dịch vụ đang phân tích: {{DỊCH VỤ}}.

Viết script Python dùng openpyxl để tạo file. Không trả bảng trong chat — ghi ra file thật.
Nếu môi trường không chạy được code: nói rõ, rồi trả bảng markdown dán được vào Excel.

# ĐẦU VÀO — cấu trúc file hội thoại
Mỗi hội thoại là một khối:

  ## <STT>. <Tên KH> — <DD/MM HH:MM>
  - Phụ trách: <tên NV> · Có SĐT: <Có|Không> · Số tin: <n>
  - **<DD/MM HH:MM> KH:** <nội dung khách>
  - **<DD/MM HH:MM> NV (<tên NV>):** <nội dung nhân viên>

Quy ước: `[Ảnh]` `[Tệp]` `[Thẻ: …]` là đính kèm hoặc tin tự động, KHÔNG phải chữ khách gõ.
Trường `Có SĐT` lấy nguyên từ dữ liệu, không tự suy luận lại.
File có cấu trúc khác → tự nhận dạng, báo cấu trúc đọc được, rồi tiếp tục. Không bắt tôi sửa file.

# BƯỚC 1 — CHẤM MỘT LẦN, HAI FILE DÙNG CHUNG
Chấm từng hội thoại đúng một lần, lưu kết quả, rồi cả hai file đọc từ kết quả đó.
Hai file BẮT BUỘC khớp nhau tuyệt đối về: L-code · độ nóng · nhóm giá trị · vấn đề răng · giai đoạn.
Hai file cho ra con số khác nhau cho cùng một hội thoại là SAI.

## Chấm 5 tín hiệu (mỗi tín hiệu 1 điểm)
① Nêu dịch vụ/tình trạng răng CỤ THỂ ("mất răng số 6", "niềng trong suốt", "bọc sứ 4 răng")
   — không tính "làm răng", "tư vấn giúp em"
② Mốc thời gian dự kiến ≤ 14 ngày, hoặc đã đặt lịch, hoặc đang đến phòng khám
③ Hỏi lịch, bác sĩ, chi phí hoặc trả góp THEO ĐÚNG TÌNH TRẠNG CỦA MÌNH
   — không tính câu hỏi giá chung chung ở tin đầu
④ Gửi ảnh răng / phim X-quang, hoặc mô tả rõ: vị trí · bao lâu · đã làm gì
⑤ Để lại SĐT/Zalo thật và đồng ý nhận tư vấn (ưu tiên có nêu khung giờ)

→ HOT 4–5 · WARM 2–3 · COLD 0–1.
Ghi bitmask 5 chữ số, ví dụ `[10110]` = có ①③④, thiếu ②⑤.

## BA LUẬT GHI ĐÈ — đặc thù nha khoa, bắt buộc áp
① Đã đặt lịch khám hoặc đang đến phòng khám → HOT bất kể điểm.
② ĐÃ CÓ PHIM X-QUANG, hoặc đã khám nơi khác và có phác đồ/báo giá rồi → HOT bất kể điểm.
   Khách đã qua giai đoạn chẩn đoán, chỉ còn chọn nơi làm. Đây là lead nóng nhất của
   ngành nha, mà thang 5 tín hiệu thường chấm thấp oan cho họ.
③ Đang đau cấp (nhóm V-06) → tối thiểu WARM, kể cả chỉ được 1 điểm.
   Người đau răng viết tin ngắn nhưng họ đến trong ngày.

# BỘ MÃ BẮT BUỘC — không tự chế mã mới

## Giai đoạn hành trình
S1 · NHẬN BIẾT — hỏi chung, hỏi giá/địa chỉ ngay từ đầu, chưa nói tình trạng (Cold)
S2 · TÌM HIỂU — gửi ảnh/mô tả, hỏi phương pháp, loại trụ, loại sứ, bác sĩ (Warm)
S3 · CÂN NHẮC & NỖI SỢ — lo đau/mài răng/biến chứng, ngờ vật liệu, so sánh,
     hỏi người nhà, chần chừ giá hoặc thời gian (Warm→Hot) ★ điểm quyết định
CS · Hậu điều trị / đang niềng / tái khám / hỏi cho người nhà

## L-code (trạng thái vận hành, chuẩn P6)
L1.1 lần đầu nhắn chưa tư vấn · L2.1 đang tư vấn hợp tác · L2.3 chưa phản hồi lại
L2.4 hẹn nhắn lại sau · L2.5 ngoài 7 tỉnh/thành có cơ sở · L4.1 có SĐT + rõ dịch vụ
L5.3 gọi không bắt máy · L5.4 từ chối nghe điện thoại · L5.5 hẹn gọi lại · L5.6 chỉ Zalo
L6.1 chưa rõ rào cản · L6.2 so sánh nơi khác · L6.3 chưa tài chính / hỏi trả góp
L6.4 chưa có thời gian / lo đi nhiều buổi · L6.5 sợ đau, sợ mài răng, sợ biến chứng
L6.6 hỏi ý kiến người thân · L6.7 NGỜ VẬT LIỆU (hỏi trụ gì, phôi sứ gì, có chính hãng
     không, có phiếu bảo hành không) — mã riêng của ngành nha, KHÔNG gộp vào L6.2

7 tỉnh/thành có cơ sở Paris: Hà Nội · Hải Phòng · Quảng Ninh · Vinh · Đà Nẵng · TP.HCM · Bình Dương.
Khách TRONG 7 tỉnh/thành mà bảo xa/bận → L6.4, không phải L2.5.

## 11 nhóm vấn đề răng — xét ưu tiên từ trên xuống, đúng nhóm đầu tiên thì lấy
V-01 làm lại / sửa ca lỗi (sứ lệch, trụ đào thải, niềng dở dang, làm ở chỗ khác)
V-02 mất nhiều răng / mất cả hàm (All-On, hàm giả, tháo lắp)
V-03 mất răng lẻ / trồng lại (Implant, cầu răng)
V-04 răng lệch · khấp khểnh · thưa · hô · khớp cắn (niềng)
V-05 răng xỉn màu · vỡ · sứt · mòn (bọc sứ, Veneer, trám)
V-06 đau nhức · viêm tủy · áp xe
V-07 viêm nướu · chảy máu chân răng · vôi răng · hôi miệng
V-08 răng khôn · nhổ răng
V-09 tẩy trắng · đính đá · Teeth Spa
V-10 răng trẻ em
V-11 chưa rõ / hỏi chung

Khách vừa mất răng vừa đau → V-03, ghi chú "kèm đau".
Khách sửa lại ca cũ → LUÔN là V-01, kể cả đã nêu dịch vụ gì, vì cách tư vấn khác hoàn toàn.

## Nhóm giá trị — CỘT RIÊNG, không gộp vào độ nóng
V1 giá trị lớn: Implant · All-On 4/6 · Invisalign · răng sứ toàn hàm · ghép xương/nâng xoang
V2 giá trị trung: bọc sứ 1–6 răng · Veneer · niềng mắc cài · tủy + sứ
V3 giá trị nhỏ / cửa vào: cạo vôi · tẩy trắng · trám · nhổ răng · răng khôn · trẻ em · Teeth Spa

LƯU Ý KHI VIẾT KHUYẾN NGHỊ: một lead WARM của Implant (WARM·V1) đáng đầu tư hơn
một lead HOT của cạo vôi (HOT·V3). Không xếp hạng lead chỉ bằng độ nóng.

## 3 rào cản
SỢ → L6.5 · NGỜ → L6.2, L6.7 · NGẠI → L6.3, L6.4, L2.5
Một hội thoại có thể mang nhiều rào cản. Đếm theo lượt, và ghi rõ cách đếm ở đầu bảng.

## Nhóm đối tượng theo insight
NHÓM A — chưa để lại SĐT (mục tiêu: xin số)
  A1 hỏi giá ngay chưa nói tình trạng · A2 mất răng trung–cao niên
  A3 làm lại ca lỗi ở nơi khác · A4 niềng (bạn trẻ hoặc phụ huynh)
  A5 ở xa / ngoài 7 tỉnh có cơ sở / Việt kiều · A6 sợ đau, sợ mài răng, muốn tư vấn kỹ
  A7 ngờ vật liệu — hỏi trụ, phôi sứ, chính hãng
NHÓM B — đã để lại SĐT (mục tiêu: kết nối → đến khám)
  B1 vừa cho số · B2 chưa kết nối được · B3 chỉ nhắn Zalo
  B4 đã gọi còn rào cản · B5 đã đặt lịch khám
NHÓM C — sau điều trị (LTV)
  C1 đang điều trị / hậu điều trị · C2 gắn bó, mở rộng, hỏi cho người nhà
Loại — không phải khách hàng (B2B chào bán, tuyển dụng)

## Mã kịch bản
S1.1 hỏi giá ngay · S1.2 hỏi địa chỉ/cơ sở · S1.3 chào mở chưa rõ nhu cầu
S2.1 đã gửi ảnh → nhận định sơ bộ theo vùng + mời chụp phim + xin số
S2.2 hỏi phương pháp / loại trụ / dòng sứ / công nghệ / bao lâu xong
S2.3 niềng — bạn trẻ · S2.4 niềng — phụ huynh hỏi cho con
S2.5 mất răng trung–cao niên (nhấn ăn nhai trước thẩm mỹ)
S3.1 sợ đau · S3.2 sợ mài răng thật · S3.3 ngờ vật liệu / chính hãng
S3.4 so sánh nơi khác · S3.5 chưa tài chính / hỏi trả góp · S3.6 chưa sắp xếp thời gian
S3.7 hỏi/giấu người nhà · S3.8 làm lại ca lỗi · S3.9 ở xa/nước ngoài
S3.10 muốn đặt lịch → chốt khám + chụp phim
X1 xin SĐT đúng cách · X2 gọi nhỡ · X3 chỉ Zalo · X4 nuôi dưỡng Cold/im lặng
X5 khách đau cấp — xử lý trong ngày
CS hậu điều trị + cross-sell + gói gia đình

Nhiều mã dùng kèm thì nối bằng ` · ` — ví dụ `S3.3 · X1`.

# FILE 1 — output/Paris_<DV>_PhanLoai_KichBan.xlsx
Góc nhìn: QUY TRÌNH. Mỗi hội thoại đi trọn 4 bước trên một dòng. 5 sheet, đúng thứ tự:

1. **Tổng quan** — tiêu đề, nguồn dữ liệu, ngày lập; sơ đồ 4 bước
   ① ĐỐI TƯỢNG → ② NHÓM → ③ KỊCH BẢN → ④ NỘI DUNG;
   bảng 5 tín hiệu + 3 luật ghi đè; bảng HOT/WARM/COLD; bảng giai đoạn S1–S3;
   bảng nhóm giá trị V1/V2/V3; kết quả phân loại (đếm thật);
   6 nguyên tắc bắt buộc khi dùng nội dung.
2. **Chú giải ký hiệu** — giải nghĩa mọi ký hiệu dùng trong file:
   ⚠ · giai đoạn S · nhóm chăm sóc · L-code (có L6.7) · mã vấn đề răng V-xx ·
   nhóm giá trị V1/V2/V3 · mã kịch bản · `[ … ]` chỗ cần điền ·
   `{ … }` biến lấy từ chương trình tháng · `·` phân tách mã · `→` bước kế tiếp ·
   nhịp T/D · quy ước màu · viết tắt.
3. **Khung 5 bước B1-B5** — khung tư vấn chuẩn, cột: Bước | Làm gì | Câu mẫu | Lưu ý.
   Bước B2 phải ghi rõ 4 THÔNG TIN BẮT BUỘC: tình trạng (vị trí · bao lâu) ·
   đã điều trị ở đâu chưa · mong muốn · thời gian dự kiến.
4. **Quy trình <N> HT** — một dòng mỗi hội thoại, cột đúng thứ tự:
   STT | Tên khách | Vấn đề răng (V-xx) | Tình trạng / Nhu cầu | Giai đoạn |
   Nhóm KH (insight) | Nhóm giá trị | Nhóm chăm sóc | Kịch bản (mã) | Tên kịch bản |
   Nội dung gợi ý gửi ngay | Rào cản / ghi chú
   → Cột "Nội dung gợi ý gửi ngay" phải là TIN NHẮN gửi được ngay, đã cá nhân hoá
     theo tình trạng của chính khách đó (vị trí răng, thời gian mất răng, điều khách
     vừa lo), không phải mô tả việc cần làm.
5. **Nhịp chăm sóc** — cột: Nhóm | Khi nào dùng | Nhịp chạm | Kịch bản gợi ý | Điều kiện dừng.
   Tối thiểu các nhóm: HOT·V1 · HOT·V2–V3 · HOT gọi nhỡ · WARM·V1 (nuôi dài) ·
   WARM·V2–V3 · COLD · đau cấp · ở xa/ngoài 7 tỉnh · làm lại ca lỗi · gia đình/trẻ em.
   Chốt bằng dòng trần nhắn: tối đa 6 lần / 7 ngày, khách từ chối thì dừng.
   Ghi rõ: L6.x·V1 nuôi tới 90 ngày, các nhóm khác 30 ngày.

# FILE 2 — output/Paris_KichBan_<DV>.xlsx
Góc nhìn: PHÂN LOẠI + BANK KỊCH BẢN theo nhóm đối tượng. 5 sheet, đúng thứ tự:

1. **Tổng quan** — kết quả phân loại (tổng HT · có/không SĐT kèm % · HOT/WARM/COLD ·
   phân bố V1/V2/V3 · đã đặt lịch khám · đang điều trị);
   bảng nhóm đối tượng A/B/C kèm insight từng nhóm;
   bảng phân bố 11 nhóm vấn đề răng;
   **mục "Lỗi quan sát trong data — phải tránh"**: trích số hiệu hội thoại thật làm
   dẫn chứng cho từng lỗi trong 8 lỗi cấm (lờ câu hỏi giá · bắn giá cứng · dán mẫu
   máy móc · nói "không đau" · gắn "chính hãng" sai · xin số không lý do · xin số
   rồi để yên · hứa thời gian điều trị cứng);
   mục biến số từ chương trình tháng, mọi số gắn ⚠.
2. **Chú giải ký hiệu** — theo cột của file này: cột SĐT · Vấn đề răng · Ghi chú
   (bitmask) · Nhóm ĐT · L-code · Độ nóng · Nhóm giá trị · nhịp chăm sóc · ⚠ ·
   lưu ý cốt lõi BA TRỤC không gộp.
3. **Phân loại <N> HT** — một dòng mỗi hội thoại, cột đúng thứ tự:
   STT | Tên KH | Ngày | Phụ trách | Số tin | SĐT | Vấn đề răng | Nhóm ĐT |
   L-code | Độ nóng | Nhóm giá trị | Rào cản | Ghi chú (tín hiệu ①②③④⑤)
   → Cột Ghi chú: bitmask `[01011]` + dấu hiệu quan sát (gửi ảnh, có phim X-quang,
     hỏi giá, ở xa, sợ đau, sợ mài răng, ngờ vật liệu, so sánh, hỏi người nhà, bận).
   → Nếu áp luật ghi đè thì ghi rõ: `[01011] → HOT (ghi đè: đã có phim)`.
4. **Kịch bản <DV>** — bank kịch bản theo nhóm đối tượng, cột:
   Nhóm | Mã | Giai đoạn | Insight khách hàng (nỗi lo thật) | Rào cản | L-code |
   Nhóm giá trị | Khi nào dùng | Nội dung 1 | Nội dung 2 | Nội dung 3 | Lưu ý an toàn
   → Mỗi mã A1–A7, B1–B5, C1–C2 một dòng.
5. **Chăm sóc theo độ nóng × giá trị** — cột:
   Độ nóng | Nhóm giá trị | Số lead | Nghĩa | Tín hiệu nhận biết | SLA kết nối |
   Nhịp chăm sóc | Hành động | Mục tiêu
   → Tối thiểu 9 dòng (3 độ nóng × 3 nhóm giá trị). Cột "Số lead" phải khớp
     con số đếm được ở bước 1.

# QUY TẮC VIẾT NỘI DUNG KỊCH BẢN
- Nội dung là TIN NHẮN gửi khách, viết sẵn để trực page dán — không phải hướng dẫn.
- Mỗi tin một giá trị mới, 2–4 dòng, một câu hỏi chính.
- Trả lời câu khách hỏi TRƯỚC, rồi mới hỏi câu mới.
- Không lờ câu hỏi giá: nêu khung giá niêm yết + giải thích chi phí cuối phụ thuộc
  phim X-quang và chỉ định + mời khám.
- CTA của nha khoa là ĐI KHÁM + CHỤP PHIM, nói rõ CHƯA PHẢI ĐIỀU TRỊ.
  Đây là CTA dễ nhận nhất của ngành — dùng nó, đừng nhảy thẳng vào báo giá.
- Đề nghị = chọn giữa 2 phương án, không hỏi có/không.
- Xin SĐT kèm lý do có lợi cho khách ("để bác sĩ xem phim và báo lộ trình sát")
  + 2 khung giờ cụ thể, tối đa 2 lần/hội thoại.
- Chưa rõ giới tính → xưng "mình". Khách nói về con → chuyển giọng sang phụ huynh.
- Nhóm mất răng: nhắc "mất răng để lâu sẽ tiêu xương, trồng lại khó hơn" —
  đây là lý do cấp thiết CÓ THẬT, hợp pháp, đúng y khoa.
- `[ … ]` = chỗ điền theo tình huống. `{ … }` = biến lấy từ chương trình tháng, luôn kèm ⚠.

# QUY TẮC AN TOÀN — kiểm trước khi ghi file
- ❌ Từ cấm: `cam kết 100%` · `khỏi 100%` · `tốt nhất` · `số 1` · `duy nhất` ·
  `không đau` · `an toàn tuyệt đối` · `không biến chứng` · `dùng vĩnh viễn` /
  `trọn đời` · `rẻ nhất` · `cam kết kết quả như hình`.
- ❌ Không bắn giá cứng cho ca cụ thể. Nêu khung giá niêm yết thì được.
- ❌ Chữ "CHÍNH HÃNG" chỉ dùng cho 4 hãng: Straumann · Invisalign · Nacera · Ormco.
  Gắn cho vật liệu khác là SAI PHÁP LÝ.
- ❌ Không hứa thời gian điều trị cứng ("niềng xong trong 12 tháng").
- ❌ Không chẩn đoán qua ảnh/mô tả. Nhận định sơ bộ rồi mời khám + chụp phim.
- ❌ Chỉ nêu 3 bác sĩ: TS-BS. Đàm Ngọc Trâm · BS. Hồ Hiệp Anh Tuấn ·
  BS.CKI Nguyễn Ngọc Linh. Tên khác → ⚠ cần xác minh.
- ❌ Không bịa ca bệnh, giải thưởng, tỷ lệ thành công.
- ⚠ Mọi con số ưu đãi / % / ngày / giá / hotline / địa chỉ phải gắn ⚠ và ghi rõ
  cần xác minh — không lấy số của tháng trước.
- Không đưa số điện thoại, link, hay thông tin định danh của khách vào file đầu ra.
- Tên khách giữ như trong file nguồn, không bổ sung thêm thông tin cá nhân nào khác.

# TRÌNH BÀY EXCEL
- Font Arial toàn bộ. Freeze dòng tiêu đề. Wrap text ở các cột nội dung dài.
- Tiêu đề bảng: nền đậm, chữ trắng, in đậm.
- Độ rộng cột đặt theo nội dung; cột nội dung tin nhắn tối thiểu 60.
- Màu quy ước: xanh nhạt bước ①/giai đoạn S1 · cam nhạt bước ② · xanh lá nhạt bước ③ ·
  vàng bước ④ và mọi ô có ⚠ · đỏ nhạt HOT · cam WARM · xanh dương nhạt COLD ·
  viền đậm cho dòng nhóm giá trị V1.

# CÁCH LÀM — theo thứ tự
1. Đọc và tách toàn bộ hội thoại. Báo số lượng tách được, đối chiếu với tiêu đề file.
   Báo luôn: bao nhiêu có SĐT · khoảng thời gian dữ liệu · bao nhiêu thiếu dấu
   thời gian · mẫu này là toàn bộ hay đã bị lọc.
   DỪNG LẠI cho tôi xác nhận trước khi chấm.
2. Chấm 5 tín hiệu + 3 luật ghi đè cho từng hội thoại, lưu một bảng kết quả duy nhất.
3. In ra bảng đếm: tổng HT · có/không SĐT · HOT/WARM/COLD · phân bố V1/V2/V3 ·
   phân bố 11 nhóm vấn đề răng · phân bố giai đoạn · phân bố rào cản.
   DỪNG LẠI cho tôi xác nhận con số trước khi viết kịch bản.
4. Sinh bank kịch bản cho các mã có xuất hiện trong dữ liệu.
   Mã không có hội thoại nào → ghi "⚠ chưa có ca trong kỳ", không viết lấp.
5. Ghi 2 file Excel.
6. Tự kiểm và báo cáo: hai file có khớp nhau về L-code / độ nóng / nhóm giá trị /
   vấn đề răng của từng hội thoại không · tổng số lead ở sheet "Chăm sóc theo độ nóng
   × giá trị" có bằng tổng đếm được không · còn sót từ cấm hoặc số chưa gắn ⚠ không ·
   có chỗ nào gắn "chính hãng" cho vật liệu ngoài 4 hãng không.
````

## Đến đây

---

## Lưu ý khi dùng

**Bước 1 và bước 3 cố tình dừng lại.** Chấm 5 tín hiệu là chỗ dễ lệch nhất — xem con số phân bố trước khi AI viết hàng trăm dòng kịch bản sẽ rẻ hơn nhiều so với sửa sau.

**Hai file phải khớp nhau.** Ở thương hiệu khác trong tập đoàn, bản sinh lần đầu từng bị lệch: một file ghi HOT 47 · WARM 50 · COLD 3, file kia ghi HOT 25 · WARM 57 · COLD 18 **trên cùng 100 hội thoại**. Prompt này ép chấm một lần rồi cả hai file đọc chung kết quả, và yêu cầu tự đối chiếu ở bước 6.

**Ba luật ghi đè là phần quan trọng nhất của bản nha khoa.** Khách đã có phim X-quang hoặc đã khám nơi khác là lead nóng nhất — họ chỉ còn chọn nơi làm. Nhưng tin nhắn của họ thường ngắn gọn, nên thang 5 tín hiệu chấm họ xuống WARM hoặc COLD. Bỏ luật ghi đè là bỏ đúng nhóm đáng gọi trước nhất.

**Đổi dịch vụ khác** chỉ cần thay `{{DỊCH VỤ}}`. Bảng 11 nhóm vấn đề răng dùng chung cho mọi dịch vụ, không cần sửa.

**File nguồn chứa dữ liệu khách thật** — tên, ảnh, mô tả tình trạng, có thể cả phim X-quang. Chạy trên máy nội bộ, và kiểm file đầu ra trước khi chia sẻ ra ngoài.
