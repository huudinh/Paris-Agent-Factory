# CHANGELOG & VIỆC CÒN TREO

---

## v1.0 — 2026-10-14 · Bản đầu

Dựng `Paris-Agent-Factory` cho thương hiệu **nhakhoaparis.vn**, tham khảo kiến trúc [`Kangnam-Agent-Factory`](../../Kangnam-Agent-Factory/) v2.3 của `benhvienthammykangnam.com.vn`.

### Đổi mục tiêu so với bản Kangnam

| | Kangnam-Agent-Factory | Paris-Agent-Factory |
|---|---|---|
| **Là gì** | Meta-agent **sinh ra agent** CSKH | Trợ lý **đọc số liệu ra báo cáo** |
| **Người dùng** | Kỹ sư · quản lý sản phẩm · người quyết ngân sách | **Trực page · trưởng nhóm · ads · giám đốc dịch vụ — không làm IT** |
| **Chế độ** | 5 mode: NĂNG LỰC · KIẾN TRÚC · LỘ TRÌNH · ĐỀ BÀI · **SINH AGENT** | 4 mode: KIỂM DỮ LIỆU · **RA BÁO CÁO** · TRA NHANH · GIẢI THÍCH SỐ |
| **Đầu ra** | System prompt agent con + phiếu 6 ô + bảng test 4 tiêu chí | **5 báo cáo R1–R5**, phần lớn là file Excel |
| **Thư mục** | `templates/A1–A5` (khuôn agent con) | `reports/R1–R5` (khuôn báo cáo) |
| **Module** | `knowledge/K1–K8` | `knowledge/P1–P8` |
| **Lộ trình 4 phase · 12 đề bài tích hợp** | Có — vì phục vụ người dựng hệ | **Bỏ** — người dùng không cần, và hệ này không nối vào CRM |

### Giữ nguyên từ bản Kangnam

- Công thức **lõi brand-neutral + module thương hiệu** → đổi brand = đổi module, không sửa lõi.
- Trạng thái **L1–L6** làm xương sống.
- **5 tín hiệu → HOT/WARM/COLD**, ghi bitmask 5 chữ số.
- **Rubric 10 tiêu chí**, chuẩn đạt ≥8/10, vi phạm ngôn từ → 0 điểm.
- **Luật `% HOT*`** chống lặp vòng khi chia nhóm theo thuộc tính đang chấm điểm.
- **Luật mẫu nhỏ** dưới 10 hội thoại → không xếp hạng, không khuyến nghị.
- **Cảnh báo mẫu bị lọc** — bài học từ vụ 100 hội thoại chọn từ 520 ưu tiên hội thoại dài.
- **Luật một lần chấm** — bài học từ vụ hai file lệch nhau (HOT 47 vs HOT 25 trên cùng 100 hội thoại).
- Hai điểm dừng chờ người xác nhận con số.

### Thêm mới cho ngành nha — bốn thứ

| # | Thêm gì | Vì sao |
|---|---|---|
| **1** | **Trục thứ ba: nhóm giá trị V1 · V2 · V3** (`P4` §3) + ma trận ưu tiên độ nóng × giá trị | Dải giá nha khoa rộng gấp nhiều lần thẩm mỹ. Một lead WARM Implant đáng hơn một lead HOT cạo vôi. Gộp lại thì V3 đông và dễ chốt che mất việc V1 đang rò |
| **2** | **Mã `L6.7` — ngờ vật liệu** (`P6` §2) | Khách không tự kiểm được vật liệu trong miệng mình. Đây cũng là chỗ Paris mạnh nhất (Straumann · Invisalign · Nacera · Ormco), nên phải đo riêng xem nhân viên có dùng bằng chứng đó không |
| **3** | **Mốc "đến khám" trong phễu** (`P3` §3) | "Đặt lịch" ≠ "đến khám", và khoảng lệch là chỗ rò nặng nhất. Quyết định tiền thật xảy ra trên ghế khám |
| **4** | **Ba luật ghi đè khi chấm độ nóng** (`P8` §1) | Thang 5 tín hiệu chấm thấp oan cho ba nhóm nóng nhất: đã đặt lịch · **đã có phim X-quang / đã khám nơi khác** · đau cấp |

### Sửa đổi khác cho ngành nha

- **11 nhóm vấn đề răng `V-01…V-11`** thay bảng "vấn đề mắt" của bản Kangnam. `V-01 làm lại ca lỗi` đặt ở đầu thứ tự ưu tiên — khách sửa ca cũ cần giọng khác hoàn toàn.
- **B2 thu 4 thông tin** (thêm *"đã điều trị ở đâu chưa"*) thay vì 3 như thẩm mỹ. Thiếu mục này thì không phát hiện được ca `V-01`.
- **Phiếu bàn giao 13 trường** thay 12, thêm *vị trí răng & thời gian bị* và *đã điều trị ở đâu chưa*.
- **7 lý do từ chối** thay 5, thêm *"bọc sứ có phải mài răng không"* và *"trụ/phôi sứ có chính hãng không"*.
- **8 góc tiếp cận post** thay 6, thêm *Công nghệ giảm đau*, *Case thật/before-after*, *Gói gia đình-trẻ em*.
- **Từ cấm mở rộng:** thêm `dùng vĩnh viễn` / `trọn đời` · `rẻ nhất`, và hai lỗi tính tương đương từ cấm — **gắn "chính hãng" sai** và **chốt giá cứng ca cụ thể**.
- **Mức khuyến nghị thứ 5 cho post:** `TĂNG NGÂN SÁCH (giá trị cao)` — post ít khách nhưng toàn khách V1.
- **Nuôi `L6.x · V1` tới 90 ngày** thay vì hạ tệp ở 30 ngày — chu kỳ quyết định Implant/All-On/Invisalign dài hơn hẳn.
- **Ngoại lệ SLA cho đau cấp:** gọi ngay bất kể độ nóng, bất kể khung giờ.
- **Tệp giá trị dài hạn** (`R4` sheet 7) — nhóm riêng của ngành nha: đã đến khám chưa chốt phác đồ · đã nhổ răng chưa trồng lại · có dấu hiệu gia đình.

### Nguồn dữ liệu thương hiệu

`P1` và `P4` kế thừa từ [`Agent-AdsOptimize-NhaKhoaParis/knowledge/np-ho-so-thuong-hieu.md`](../../Agent-AdsOptimize-NhaKhoaParis/knowledge/np-ho-so-thuong-hieu.md) v2.0.
`P2` kế thừa từ `np-chan-dung-hanh-trinh.md` v2.0.
`P5` phần từ cấm kế thừa từ `np-rao-phap-ly.md` v2.0.

### Trang hướng dẫn (artifact)

`https://claude.ai/artifact/RGqakkH2sxNpvFCx62hhjn` — trang HTML cho người dùng cuối, tương đương trang hướng dẫn của bản Kangnam. Gồm: giới thiệu theo **4 nhóm người dùng** (Trực Page · Ads · Trưởng nhóm · Giám đốc dịch vụ) với cột *làm được / không làm* · cài đặt 3 nền tảng dạng tab · 10 câu chạy thử · cách chuẩn bị dữ liệu và luật không được lọc mẫu · **15 prompt copy-dán** chia theo nhóm · mục hỏi nhanh lọc được theo nhóm · ba thứ riêng ngành nha · ranh giới pháp lý · link tải repo.

**Phần cài đặt nhúng sẵn nội dung file** theo mẫu Kangnam, nên trang tự đủ để cài mà không cần tải repo: 5 thẻ theo đúng thứ tự ô trên form (Tên · Mô tả với 5 biến thể cho từng bộ phận · Instructions bản đầy đủ 14.010 ký tự · bản ngắn 7.744 cho ChatGPT · Tri thức), mỗi thẻ có nút Copy và khối xem nội dung; cộng hai file gộp dự phòng (`P1–P8` 55,6 KB · `R1–R5` 78,6 KB, mỗi phần có dòng `===== tên file =====` để trợ lý vẫn đọc đúng từng module). Kèm cảnh báo: dùng file gộp thì mất khả năng thay riêng `P7` hàng tháng.

Thiết kế theo **Design System Paris v3.1** trong `P1` §1 — Cerulean Blue `#2A52BE`, Pantone Red 032 C `#ED2E38` (chỉ dùng cho CTA và cảnh báo, giữ tỷ lệ 5%), kem `#FBF8F3`, navy `#0C1D4D`; font Bricolage Grotesque + Be Vietnam Pro. Không tự chế biến thể màu mới.

**Đổi tên thống nhất:** tên artifact, tiêu đề trang, nhãn thanh điều hướng và **tên Project để dán vào ô Name** (`doc/01-cai-dat.md` §0) đều đổi thành `Paris-Agent-Factory` — trùng tên repo. Trước đó Project tên *Trợ lý Báo cáo Fanpage Paris*, tức một hệ có ba cái tên; người mới phải nhớ cả ba.

> ⚠️ Artifact mặc định **private**. Phải mở Share trên trang để cả nhóm xem được.

### Công cụ

- `tools/phan_loai.py` — đối chiếu con số, chạy được, đã test trên `doc/mau-du-lieu/MAU_Hoi-thoai.md`.
- `tools/tu-dien-van-de-rang.json` — từ điển từ khoá, người làm nội dung sửa được không cần biết code.
- `tools/excel_style.py` — style dùng chung cho mọi file Excel: màu Design System Paris v3.1 · font Arial · freeze · wrap · bảng nhiệt bằng `ColorScaleRule` · sheet chú giải 20 mục. **Sửa quy ước màu ở một chỗ thì đổi cả hệ.**
- `tools/xuat_bao_cao.py` — **xuất file Excel theo đúng khuôn R1–R5.** Trước đó mỗi lần chạy trợ lý lại tự viết `openpyxl` từ đầu nên định dạng mỗi lần một khác; giờ có bản tham chiếu. Ô nào script không tính được thì để `⚠` nền vàng kèm chữ mô tả cần điền gì.

### Ranh giới của bộ code xuất Excel

Script tính được con số, **không đọc hiểu được nội dung**. Phân chia rõ:

| Script làm | Người / trợ lý làm |
|---|---|
| Toàn bộ cấu trúc sheet, định dạng, sheet chú giải | Ba kết luận mở đầu mỗi báo cáo |
| Mọi con số đếm được · chấm 5 tín hiệu + 3 luật ghi đè · gán `V-01…V-11` · V1/V2/V3 · L-code | **Bảng chấm 10 tiêu chí của R3** — chỉ tiêu chí ⑨ (từ cấm) là script điền được |
| Phát hiện từ cấm · phát hiện ca `L6.7` mà NV không nhắc đối tác hãng | Khối "Đọc nhanh" dưới mỗi bảng nhiệt · trích dẫn bằng chứng · nội dung tin nhắn (script chỉ cho khung theo rào cản) |

→ Vì vậy **R3 xuất ra là KHUNG, không phải bảng điểm hoàn chỉnh**. Nói rõ ngay trên sheet Tổng quan của file.

### Sửa trong quá trình dựng

- **Lỗi thẻ quảng cáo làm lệch phân loại:** dòng `[Thẻ: …]` là tin tự động nhưng ban đầu bị tính như chữ khách gõ. Headline *"không ai biết bạn đang niềng"* bị đọc thành *khách đang niềng* → xếp sai giai đoạn `CS`. Đã lọc bỏ phần thẻ khỏi chữ khách trước khi phân loại.
- **Lỗi chữ hoa/thường ở dấu `[Ảnh]`:** văn bản đã `lower()` nên so khớp `[Ảnh]` không bao giờ trúng → tín hiệu ④ bị bỏ sót với khách chỉ gửi ảnh mà không mô tả.
- **Lỗi định dạng phần trăm:** hàm `pc()` thay dấu `.` thành `,` ngay trong chuỗi format nên `%.1f%%` thành `%,1f%%` → `ValueError`. Phải format xong rồi mới thay dấu.
- **Số ký tự khối chỉ dẫn lệch 1:** tài liệu ghi 14.011 / 7.745 trong khi nút Copy của trang hướng dẫn trả về 14.010 / 7.744 — chênh một ký tự xuống dòng cuối. Đã đồng bộ tài liệu theo **số thật mà người dùng dán**, vì con số này tồn tại để so với giới hạn 8.000 ký tự của ChatGPT.
- **Lỗi freeze pane trên sheet nhiều bảng:** sheet Tổng quan có nhiều bảng, freeze theo dòng tiêu đề cuối sẽ ghim tới 63 dòng đầu, cuộn xuống không đọc được gì. Đã đổi: chỉ freeze khi sheet có **đúng một** bảng và dòng tiêu đề nằm trong 10 dòng đầu.

### Sửa khuôn báo cáo cho khớp code

- `R4`: **8 → 9 sheet**, thêm sheet *Chú giải ký hiệu* ở vị trí 2 cho đồng bộ với R1/R2/R3.
- `R5`: **6 → 7 sheet**, thêm sheet *Chú giải ký hiệu* kèm hai mục riêng của R5 — *ngưỡng nhiễu* và *tương quan ≠ nhân quả*.
- Cả 5 khuôn `R1–R5`: thêm khối **📎 Có code mẫu sẵn** trỏ sang `tools/xuat_bao_cao.py`, để trợ lý dùng lại thay vì tự viết `openpyxl`.

---

## 🔴 VIỆC CÒN TREO — phải đóng trước khi dùng thật

| # | Việc | Mức chặn | Ai cấp |
|---|---|---|---|
| **1** | **`P7-chien-dich-thang.md` đang trống** — toàn bộ ưu đãi · giá · % · trả góp của tháng | 🔴 **Chặn cứng.** Chưa có thì mọi chỗ cần số đều ghi `⚠`, báo cáo thiếu phần đối chiếu ưu đãi | Marketing |
| **2** | **Bảng giá niêm yết theo từng dòng trụ / dòng sứ** (`P4` §4) | 🟠 Vừa. Không có thì không chấm được lỗi "bắn giá cứng" chính xác | Marketing + Phòng khám |
| **3** | **Điều kiện & lãi suất trả góp hiện hành** | 🟠 Vừa. Đây là **cam kết tài chính**, sai một chữ là rủi ro thật. Chưa có thì nhân viên chỉ được nói "có chính sách trả góp" | Tài chính |
| **4** | **Mốc KPI của Paris** — tỷ lệ xin số · show-up · chốt phác đồ (`P8` §7) | 🟠 Vừa. Chưa có thì báo cáo nêu số thật + `⚠ chưa có mốc so sánh`, không kết luận đạt/không đạt | Ban điều hành |
| **5** | **Số đặt lịch · số ĐẾN KHÁM · số chốt phác đồ theo kỳ** | 🟠 Vừa. Thiếu thì `R4` chỉ đọc được nửa phễu đầu | Phòng khám |
| **6** | **Cơ sở nào đủ năng lực All-On / ghép xương** | 🟡 Nhẹ. Ảnh hưởng việc định tuyến khách ở tỉnh | Phòng khám |
| **7** | **Chính sách bảo hành theo dịch vụ** (số năm) | 🟡 Nhẹ. Là bằng chứng gỡ rào cản NGỜ, đang thiếu | Phòng khám |
| **8** | **Danh sách case before–after đã có giấy đồng ý** | 🟡 Nhẹ. Cần nếu chạy post góc "Case thật" | Pháp chế + Marketing |
| **9** | **Giấy xác nhận nội dung quảng cáo** cho từng nội dung đang chạy | 🟠 Vừa. Chặn cứng việc bật chiến dịch, không chặn việc làm báo cáo | Pháp chế |
| **10** | **Phân tầng nhân sự CSKH** để định tuyến HOT·V1 | 🟡 Nhẹ. Chưa có thì SLA chỉ nêu mốc thời gian, không nêu ai nhận | Vận hành |

---

## Việc nên làm sau 2–3 kỳ

| Việc | Vì sao chờ |
|---|---|
| **Chốt mốc KPI thật của Paris** thay mốc tham chiếu kế thừa từ hệ tập đoàn | Cần 2–3 kỳ dữ liệu mới biết mốc nào hợp lý với ngành nha |
| **Đo lại ngưỡng nhiễu của `R5`** theo dao động thật của Paris | Ngưỡng hiện tại (10/5/3 điểm % theo cỡ mẫu) là ước lượng chung |
| **Bổ sung từ điển `tu-dien-van-de-rang.json`** theo cách khách Paris thật sự gõ | Từ điển hiện tại dựng từ hồ sơ thương hiệu, chưa qua dữ liệu thật |
| **Xem có cần thêm mã `V-12`** cho nhóm vấn đề chưa phủ | Chờ xem tỷ lệ `V-11 chưa rõ` có cao bất thường không |
| **Cân nhắc tách `R3` thành bản tự chấm cho nhân viên** | Nếu bảng chấm được dùng để đào tạo chứ không để xếp loại thì bản tự chấm hiệu quả hơn |

---

## Ghi chú kiểm chứng

Bộ này **chưa chạy trên dữ liệu thật của Paris**. Những gì đã kiểm:

| Đã kiểm | Cách kiểm |
|---|---|
| Script `phan_loai.py` chạy đúng | Chạy trên 12 hội thoại mô phỏng, đối chiếu từng ca với bảng ghi chú cuối `MAU_Hoi-thoai.md` |
| Phát hiện vi phạm từ cấm | Script bắt đúng `HT#4` với `cam kết 100%` · `không đau` · `không hại gì` |
| Luật ghi đè hoạt động | Bắt đúng 3 ca: đã đặt lịch (HT#12) · đã có phim (HT#5) · đau cấp (HT#6) |
| Độ dài khối chỉ dẫn | `SYSTEM-PROMPT.md` = **14.010** ký tự · `SYSTEM-PROMPT-NGAN.md` = **7.744** (dưới giới hạn 8.000 của ChatGPT, dư 256) |
| Bộ code xuất Excel | Chạy ra đủ **6 file / 46 sheet** trên dữ liệu mẫu: R1 2 file (5+5 sheet) · R2 13 sheet có 5 bảng nhiệt · R3 7 sheet · R4 9 sheet · R5 7 sheet. Đã mở lại từng file kiểm số sheet, số dòng, freeze pane và conditional formatting |

**Chưa kiểm:** chất lượng báo cáo trợ lý sinh ra trên dữ liệu thật. Lần chạy thật đầu tiên nên làm trên **một dịch vụ, một kỳ ngắn**, rồi đối chiếu với cảm nhận của người trực page — họ biết khách nào nóng, và đó là thước đo tốt nhất cho việc chấm có đúng không.
