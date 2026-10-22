# 🦷 PARIS AGENT FACTORY — Trợ lý đọc số liệu Fanpage, trả về báo cáo

> Version 1.0 · **Bạn đưa file hội thoại và danh sách post. Nó trả về báo cáo.**
>
> **Không cần biết lập trình. Không cần tạo AI-Agent. Không cài gì lên máy.**

Kiến trúc kế thừa [`Kangnam-Agent-Factory`](../Kangnam-Agent-Factory/) v2.3, nhưng **đổi mục tiêu**: Kangnam là meta-agent *sinh ra agent* cho người làm kỹ thuật; bản Paris này là **trợ lý đọc số liệu ra báo cáo** cho người vận hành. Cùng công thức **lõi brand-neutral + module thương hiệu**, nên đổi brand = đổi module `P`, không sửa lõi.

---

## 📘 Hướng dẫn sử dụng

> ### → **[Mở trang hướng dẫn](https://claude.ai/artifact/RGqakkH2sxNpvFCx62hhjn)**
>
> **Trang tự đủ để cài — không tải repo cũng được.** Phần cài đặt nhúng sẵn **toàn bộ bộ não** (bản đầy đủ 14.010 ký tự và bản ngắn 7.744 cho ChatGPT), mỗi cái một nút Copy; cộng hai **file gộp dự phòng** thay cho 13 file rời khi máy không tải được file.
>
> Mở đầu là **phần giới thiệu riêng cho từng nhóm người dùng** — nhóm đó hỏi trợ lý việc gì, và trợ lý **không** làm gì cho họ. Sau đó là **15 prompt** bấm copy là dán được:
>
> | Nhóm | Có gì ở đó |
> |---|---|
> | **① Trực Page** | Prompt gợi ý câu nhắn tiếp · tra nhanh mã trạng thái · chạm lại tệp nguội |
> | **② Ads** | Prompt phân tầng post · cách chống bẫy xếp hạng bằng `%HOT` · chọn góc tiếp cận |
> | **③ Trưởng nhóm** | Prompt chấm 10 tiêu chí · kế hoạch đào tạo 4 tuần · lỗi trượt câu hỏi ngầm |
> | **④ Giám đốc dịch vụ** | Prompt phễu theo dịch vụ · so hai kỳ · rút báo cáo thành 1 trang |
>
> Kèm **năm ô cần điền theo đúng thứ tự trên form** (có 5 biến thể ô Mô tả cho từng bộ phận) · **cài trên 3 nền tảng** · **bảng kiểm 4 câu** bắt đúng ba lỗi cài đặt hay gặp · **cách chuẩn bị dữ liệu** và luật không được lọc mẫu · mục **hỏi nhanh lọc theo nhóm** · **ba thứ chỉ ngành nha mới có**.

**Người mới bắt đầu từ trang đó, không phải từ đây.** Repo này là phần file để cài vào Project/GPT/Gem — trang hướng dẫn nói *khi nào dùng cái gì*.

> ⚠️ Trang đang ở chế độ **private**. Mở menu **Share** trên trang để cả nhóm xem được.

---

## Dùng trong 3 bước

```
① Xuất file hội thoại từ Fanpage / CRM     →  doc/02-chuan-bi-du-lieu.md
② Dán vào trợ lý, nói một câu              →  doc/03-cau-lenh-mau.md
③ Xác nhận con số khi nó dừng lại           →  nhận báo cáo
```

**Chưa cài?** Bắt đầu từ [`doc/01-cai-dat.md`](doc/01-cai-dat.md) — mất 15 phút, làm một lần.

**Không biết bắt đầu từ đâu?** Dán file vào rồi gõ: *"Đây là file hội thoại tháng 10. Xem giúp mình dùng được những gì."*

---

## Năm báo cáo

| Mã | Báo cáo | Trả lời câu hỏi | Cần có |
|---|---|---|---|
| **[R1](reports/R1-phan-loai-hoi-thoai.md)** | Phân loại & kịch bản hội thoại | Khách là ai, đang vướng gì, **nhắn lại thế nào** | File hội thoại |
| **[R2](reports/R2-phan-tang-quang-cao.md)** | Phân tầng post quảng cáo + biểu đồ nhiệt | Post nào kéo khách nóng, post nào kéo khách **giá trị lớn** | Danh sách post **+** hội thoại cùng kỳ |
| **[R3](reports/R3-chat-luong-tu-van.md)** | Chất lượng tư vấn & đào tạo | Nhân viên hổng khâu nào, **tuần tới dạy gì** | Hội thoại có dấu thời gian |
| **[R4](reports/R4-bao-cao-dieu-hanh.md)** | Báo cáo điều hành theo dịch vụ | **Phễu rò ở đâu**, dịch vụ nào đang mất tiền | Hội thoại (+ số đến khám nếu có) |
| **[R5](reports/R5-so-sanh-hai-ky.md)** | So sánh hai kỳ | Có tốt lên không, **nhờ cái gì** | Dữ liệu 2 kỳ đã chạy R1 |

**Chạy theo thứ tự R1 → R2 → R3 → R4.** R4 dùng lại kết quả ba cái trước; chạy R4 đầu tiên thì chỉ có bản rút gọn.

---

## Bốn việc trợ lý KHÔNG làm

Đây là **giới hạn cố ý**, không phải thiếu sót.

| Không làm | Vì sao |
|---|---|
| **Tạo AI-Agent, viết system prompt** | Người dùng không cần việc đó. Nó chỉ đọc số liệu ra báo cáo |
| **Chat với khách, tự gửi tin** | Mọi nội dung nó viết là **bản gợi ý để người duyệt rồi dán lại** |
| **Thao tác trên CRM, website, phần mềm** | Nó chỉ đọc file bạn đưa |
| **Chẩn đoán răng, chốt giá ca cụ thể** | Rủi ro pháp lý ngành y tế. Nêu khung giá niêm yết thì được, chốt số cuối thì không |

---

## ⭐ Ba thứ khiến bản nha khoa khác bản thẩm mỹ

Không phải đổi tên thương hiệu là xong. Ba điểm dưới đây là lý do bản Paris không dùng được khuôn Kangnam nguyên xi.

### ① Trục thứ ba: NHÓM GIÁ TRỊ V1 · V2 · V3

Hệ thẩm mỹ có **hai trục**: `L-code` (trạng thái) và `HOT/WARM/COLD` (độ nóng). Nha khoa **bắt buộc có trục thứ ba**, vì dải giá rộng gấp nhiều lần — từ vài trăm nghìn (cạo vôi) tới vài trăm triệu (All-On).

| Nhóm | Dịch vụ |
|---|---|
| **V1** giá trị lớn | Implant · All-On 4/6 · Invisalign · răng sứ toàn hàm · ghép xương |
| **V2** giá trị trung | Bọc sứ 1–6 răng · Veneer · niềng mắc cài |
| **V3** nhỏ / cửa vào | Cạo vôi · tẩy trắng · trám · nhổ răng · răng trẻ em · Teeth Spa |

> **Một lead WARM của Implant đáng hơn một lead HOT của cạo vôi.**
> Gộp lại thì nhóm V3 đông và dễ chốt sẽ che mất việc V1 đang rò — và V1 là chỗ tiền thật. Xếp hạng post chỉ bằng `% HOT` sẽ dồn ngân sách vào đúng chỗ ít tiền nhất.

### ② Mã riêng `L6.7` — NGỜ VẬT LIỆU

Khách nha khoa **không tự kiểm tra được vật liệu trong miệng mình**. Nên câu *"trụ này có chính hãng không"* là một rào cản riêng, không gộp được vào *"đang xem thêm vài nơi"*.

Đây cũng là chỗ Paris mạnh nhất: **Straumann · Invisalign Black Diamond · Nacera · Ormco Diamond Star**. Hội thoại có `L6.7` mà nhân viên không nhắc đối tác hãng là **bỏ bằng chứng mạnh nhất đúng lúc cần nhất** — báo cáo đếm riêng lỗi này.

### ③ Phễu có thêm mốc ĐẾN KHÁM

```
inbox → có SĐT → kết nối → đặt lịch khám → ĐẾN KHÁM → chốt phác đồ → điều trị
```

**"Đặt lịch khám" không phải "đến khám"**, và khoảng lệch giữa hai con số là chỗ rò nặng nhất của ngành nha. Quyết định tiền thật xảy ra **trên ghế khám**, không xảy ra trong inbox.

Mặt khác: **mời đi khám dễ hơn mời phẫu thuật rất nhiều.** Khám + chụp X-quang là bước có giá trị thật với khách (biết mình đang bị gì), **chưa phải điều trị, chưa phải trả tiền lớn**. Đây là CTA mạnh nhất của ngành nha — hội thoại nào nhảy thẳng vào báo giá là tư vấn sai nhịp.

---

## Ba luật ghi đè khi chấm độ nóng

Thang 5 tín hiệu chấm thấp oan cho ba nhóm khách nóng nhất của ngành nha:

| Luật | Vì sao |
|---|---|
| Đã **đặt lịch khám** / đang đến → **HOT** bất kể điểm | Hiển nhiên |
| **Đã có phim X-quang**, hoặc đã khám nơi khác và có phác đồ → **HOT** bất kể điểm | Khách đã qua giai đoạn chẩn đoán, **chỉ còn chọn nơi làm**. Đây là lead nóng nhất, mà tin nhắn của họ thường ngắn gọn nên bị chấm WARM/COLD |
| **Đau cấp** → tối thiểu **WARM** | Người đau răng viết tin ngắn, nhưng họ đến trong ngày — và sẽ đi nơi nào gọi lại trước |

---

## Cấu trúc repo

```
SYSTEM-PROMPT.md          ← bộ não, dán vào ô chỉ dẫn (14.010 ký tự)
SYSTEM-PROMPT-NGAN.md     ← bản 7.744 ký tự, CHỈ cho ChatGPT
knowledge/P1–P8           ← module thương hiệu, upload lên Knowledge
reports/R1–R5             ← khuôn báo cáo, upload lên Knowledge
doc/                      ← tài liệu cho người đọc, KHÔNG upload
tools/                    ← đối chiếu con số + XUẤT FILE EXCEL, tuỳ chọn
```

### Code xuất Excel — có sẵn, không phải viết lại mỗi lần

| File | Việc |
|---|---|
| [tools/phan_loai.py](tools/phan_loai.py) | File hội thoại → phân loại → `rows.json` + bảng đếm |
| [tools/xuat_bao_cao.py](tools/xuat_bao_cao.py) | `rows.json` → **file Excel theo đúng khuôn R1–R5** |
| [tools/excel_style.py](tools/excel_style.py) | Style dùng chung — màu thương hiệu · freeze · wrap · bảng nhiệt · sheet chú giải. Sửa ở đây thì đổi cả hệ |

```bash
cd tools
python phan_loai.py --src <file hội thoại> --out rows.json
python xuat_bao_cao.py --bao-cao tat-ca --rows rows.json --ky "T10/2026" --out ../output
```

Ô nào script không tính được (kết luận, nhận định, bảng chấm 10 tiêu chí của R3) thì để sẵn `⚠` nền vàng kèm chữ mô tả cần điền gì. Chi tiết ở [tools/README.md](tools/README.md).

### Module tri thức — upload cả 8 file

| File | Nội dung | Trạng thái |
|---|---|---|
| [P1-thuong-hieu](knowledge/P1-thuong-hieu.md) | Định vị · **4 trụ bằng chứng** · luật chữ "chính hãng" · 3 bác sĩ được nêu tên · 7 tỉnh/thành | ✅ |
| [P2-khach-hang](knowledge/P2-khach-hang.md) | **3 rào cản SỢ · NGỜ · NGẠI** · 6 nhóm khách · bảng câu hỏi ngầm | ✅ |
| [P3-hanh-vi-trang-thai](knowledge/P3-hanh-vi-trang-thai.md) | Giai đoạn S1–S3·CS · **phễu có mốc đến khám** · cross-sell & LTV | ✅ |
| [P4-dich-vu](knowledge/P4-dich-vu.md) | **11 nhóm vấn đề răng V-01…V-11** · **nhóm giá trị V1/V2/V3** · ma trận ưu tiên | ⚠ bảng giá là dữ liệu động |
| [P5-kich-ban](knowledge/P5-kich-ban.md) | 8 lỗi cấm · 8 quy tắc vàng · **khung B1–B5** · 7 lý do từ chối · từ cấm | ✅ |
| [P6-van-hanh](knowledge/P6-van-hanh.md) | **Xương sống** — L1–L6 (có **L6.7**) · 3 trục · phiếu 13 trường · điều kiện thoát | ✅ |
| [P7-chien-dich-thang](knowledge/P7-chien-dich-thang.md) | **HOT-SWAP, thay mỗi tháng** — mọi con số ưu đãi/giá/trả góp | 🔴 **chưa điền, chờ Paris cấp** |
| [P8-chuan-cham-ban-giao](knowledge/P8-chuan-cham-ban-giao.md) | **Thước đo** — 5 tín hiệu · 3 luật ghi đè · luật `% HOT*` · SLA · rubric 10 tiêu chí · KPI · 4 rủi ro đọc số | ⚠ một số mốc KPI chờ Paris chốt |

### Tài liệu

| File | Nội dung |
|---|---|
| [doc/01-cai-dat.md](doc/01-cai-dat.md) | Cài lên Claude / Gemini / ChatGPT · **10 câu chạy thử** · bảo trì hàng tháng. Bản cho người dùng cuối: [trang hướng dẫn](https://claude.ai/artifact/RGqakkH2sxNpvFCx62hhjn) |
| [doc/02-chuan-bi-du-lieu.md](doc/02-chuan-bi-du-lieu.md) | **Xuất dữ liệu ở đâu** · luật không được lọc mẫu · định dạng chuẩn · danh sách kiểm |
| [doc/03-cau-lenh-mau.md](doc/03-cau-lenh-mau.md) | Câu lệnh copy-dán cho 5 báo cáo · bảng hỏi nhanh · 4 việc trợ lý sẽ từ chối |
| [doc/04-output-mau.md](doc/04-output-mau.md) | Output mẫu từng mode · **6 dấu hiệu đúng · 6 dấu hiệu sai** |
| [doc/05-xu-ly-su-co.md](doc/05-xu-ly-su-co.md) | Tra theo triệu chứng · lỗi pháp lý xử lý ngay · lỗi dữ liệu đầu vào |
| [doc/mau-du-lieu/](doc/mau-du-lieu/) | **12 hội thoại mô phỏng** để chạy thử · bảng danh sách post điền sẵn |
| [tools/](tools/) | Đếm lại con số để đối chiếu **+ code xuất file Excel theo khuôn R1–R5** — tuỳ chọn, người không làm IT bỏ qua |
| [doc/CHANGELOG.md](doc/CHANGELOG.md) | Lịch sử · việc còn treo |

> **Quy ước:** mã `P1–P8` và `R1–R5` là **từ vựng vận hành**, được tham chiếu khắp các file — **không đổi tên**.

---

## 🔴 VIỆC PHẢI LÀM TRƯỚC KHI DÙNG THẬT

**`P7-chien-dich-thang.md` hiện đang trống.** File này giữ mọi con số ưu đãi · giá · % · điều kiện trả góp, và nó **có hạn sử dụng**.

Chưa điền thì trợ lý vẫn chạy, nhưng mọi chỗ cần số sẽ ghi `⚠ Cần xác minh từ Paris` — tức là báo cáo thiếu phần đối chiếu ưu đãi. Điền vào trước khi chạy báo cáo thật.

**Bảo trì cuối mỗi tháng:**
1. Đổi tên bản cũ → `P7-2026-10.md`
2. Tạo `P7-chien-dich-thang.md` mới cho tháng sau
3. Upload lại lên Knowledge, xoá bản cũ
4. **Không đụng file nào khác**

**Lỗi phải chống:** giá mâu thuẫn giữa hai nhân viên · sai ngày chương trình · dùng % ưu đãi tháng trước. Ba lỗi này báo cáo được dặn **chủ động đi tìm**, không chờ ai hỏi.

---

## Bốn rủi ro đọc số — báo cáo tự đi tìm

| Rủi ro | Hậu quả nếu bỏ qua |
|---|---|
| **Mẫu bị lọc** — file chỉ gồm hội thoại dài, hoặc chỉ hội thoại có số | Đã thiên về phía nóng. Thổi phồng mọi post, và **thổi không đều nhau** → so sánh post thành vô nghĩa |
| **Mẫu nhỏ** — dưới 10 hội thoại một nhóm | `⚠ chưa đủ mẫu`. Không xếp hạng, không khuyến nghị |
| **Lặp vòng** — chia nhóm theo đúng thuộc tính đang chấm điểm | Chênh lệch là **giả**. Bắt buộc có cột `% HOT*` chấm lại không kể tín hiệu ①. Bỏ nó mà chênh lệch biến mất → **nói thẳng là không có bằng chứng** |
| **Lạm phát HOT** — chấm rộng tay | HOT tràn lan, SLA vỡ. HOT mà tỷ lệ đến khám thấp là **chấm sai**, không phải khách tệ |

---

## Ranh giới

Human-in-the-loop, mọi nội dung là bản đề xuất · không cam kết y khoa tuyệt đối (`khỏi 100%` · `an toàn tuyệt đối` · `không đau` · `dùng vĩnh viễn` · `tốt nhất` · `rẻ nhất`) · không chẩn đoán/kê đơn · không chốt giá ca cụ thể · **chữ "chính hãng" chỉ dùng cho Straumann · Invisalign · Nacera · Ormco** · chỉ nêu bác sĩ trong danh sách đã duyệt · mọi con số lấy từ `P7` hiện hành · không đưa SĐT / CCCD / hồ sơ bệnh án / ảnh khách vào file báo cáo · không nêu tên đối thủ để hạ thấp · khách có thể là trẻ em hoặc vị thành niên → hướng có phụ huynh · báo cáo có tên nhân viên **chỉ dùng cho đào tạo và định tuyến**.

Quyết định cuối luôn thuộc người dùng.
"# Paris-Agent-Factory" 
