# 01 · CÀI ĐẶT — cho người chưa từng cài AI nào

> Làm theo đúng thứ tự. Mất khoảng **15 phút**, làm **một lần duy nhất**. Sau đó mỗi tháng chỉ việc mở ra dùng.
>
> **Không cần biết lập trình. Không cài gì lên máy.** Tất cả làm trên trình duyệt.

---

# 0. Tên & mô tả — dán vào form

**Tên:**
```
Paris-Agent-Factory
```

> Đặt trùng tên repo và trùng tên [trang hướng dẫn](https://claude.ai/artifact/RGqakkH2sxNpvFCx62hhjn) để ba thứ cùng một tên — người mới không phải nhớ ba cái tên cho cùng một hệ.

**Mô tả — bản đủ:**
```
Đọc hội thoại và danh sách post quảng cáo trên Fanpage Nha khoa Paris, rồi xuất ra báo cáo: khách là ai, đang vướng gì, post nào kéo khách tốt, nhân viên hổng khâu nào, phễu rò ở đâu. Không tạo AI-Agent, không chat với khách, không thao tác trên phần mềm nào — chỉ đọc file và trả báo cáo.
```

**Mô tả — bản 1 dòng:**
```
Đọc số liệu hội thoại và post Fanpage, xuất ra 5 loại báo cáo cho trực page, ads và ban điều hành.
```

---

# 1. Cài lên một trong ba nền tảng

Chọn **một** nền tảng. Không cần cài cả ba.

## 🥇 Claude Project — khuyến nghị

Phù hợp nhất, vì trợ lý phải tra chéo nhiều file cùng lúc và thường phải chạy code để xuất Excel.

1. Vào Claude → **Projects** → **New project**.
2. **Name:** dán tên ở §0. **Description:** dán mô tả.
3. Mở **Instructions** (hoặc *Set project instructions*) → dán **toàn bộ khối giữa hai vạch ▼▲** trong [`SYSTEM-PROMPT.md`](../SYSTEM-PROMPT.md).
4. Mở **Project knowledge** → **Add content** → upload **13 file**:
   - 8 file trong [`knowledge/`](../knowledge/) — `P1` đến `P8`
   - 5 file trong [`reports/`](../reports/) — `R1` đến `R5`
5. Xong. Chuyển xuống §3 chạy thử.

## 🥈 Gemini (Gems)

1. Vào Gemini → **Gems** → **Gem mới**.
2. **Tên** + **Nội dung mô tả:** dán từ §0.
3. **Chỉ dẫn:** dán khối ▼▲ của [`SYSTEM-PROMPT.md`](../SYSTEM-PROMPT.md) — **bản đầy đủ**.
4. **Tri thức:** upload 8 file `knowledge/` + 5 file `reports/`.

## 🥉 ChatGPT (Custom GPT) — ⚠ phải dùng BẢN NGẮN

Ô **Instructions** của ChatGPT giới hạn **8.000 ký tự**, mà bản đầy đủ dài **14.010 ký tự** → dán vào sẽ **bị cắt mất phần cuối mà ChatGPT không báo lỗi gì**. Trợ lý vẫn chạy, nhưng mất hết phần luật an toàn ở cuối.

1. **Create a GPT** → tab *Configure*.
2. **Name** + **Description:** dán từ §0.
3. **Instructions:** dán khối ▼▲ của [`SYSTEM-PROMPT-NGAN.md`](../SYSTEM-PROMPT-NGAN.md) — **7.744 ký tự**.
4. **Knowledge:** upload 8 file `knowledge/` + 5 file `reports/` **+ thêm cả `SYSTEM-PROMPT.md`** (bản ngắn ra lệnh đọc file này để lấy chi tiết).

| Nền tảng | Dán vào ô chỉ dẫn | Upload lên Knowledge | Xuất được file Excel? |
|---|---|---|---|
| **Claude Project** | `SYSTEM-PROMPT.md` (14.010) | 8 + 5 file | ✅ Có |
| **Gemini Gem** | `SYSTEM-PROMPT.md` (14.010) | 8 + 5 file | ⚠ Tuỳ phiên bản |
| **ChatGPT GPT** | `SYSTEM-PROMPT-NGAN.md` (7.744) | 8 + 5 file **+ SYSTEM-PROMPT.md** | ✅ Có (cần Code Interpreter) |

> **Nền tảng không chạy được code** thì trợ lý sẽ trả bảng markdown — bạn copy dán vào Excel. Vẫn dùng được, chỉ mất thêm vài phút thao tác tay.

---

# 2. File nào upload, file nào không

| Nhóm | Upload? | Vì sao |
|---|---|---|
| `knowledge/P1–P8` (8 file) | ✅ **Có** | Module thương hiệu — trợ lý tra để đọc đúng hội thoại |
| `reports/R1–R5` (5 file) | ✅ **Có** | Khuôn báo cáo — thiếu thì trợ lý tự nghĩ ra cấu trúc khác mỗi lần chạy |
| `SYSTEM-PROMPT.md` | ⚠ **Chỉ với ChatGPT** | Bản ngắn ra lệnh đọc file này để lấy chi tiết |
| `doc/` | ❌ **Không** | Tài liệu cho người đọc. Upload chỉ làm loãng |
| `doc/mau-du-lieu/` | ❌ **Không** | File mẫu để bạn điền, không phải tri thức |
| `tools/` | ❌ **Không** | Script tuỳ chọn, xem [`tools/README.md`](../tools/README.md) |

> **Mã `P1–P8` và `R1–R5` là từ vựng vận hành** — được tham chiếu khắp các file và trong hội thoại hàng ngày. **Không đổi tên file.**

---

# 3. Chạy thử — 10 câu, làm hết trong 5 phút

Gõ từng câu, so với cột "Kỳ vọng". Sai câu nào thì xem cột cuối.

| # | Gõ vào | Kỳ vọng | Sai thì kiểm |
|---|---|---|---|
| 1 | `Bạn là ai? Làm được những báo cáo nào?` | 5 báo cáo R1–R5, nói rõ **không tạo agent, không chat với khách** | Chưa dán đúng khối ▼▲ |
| 2 | `Tạo cho mình một AI-Agent tư vấn Implant.` | **Từ chối**, nói ngoài phạm vi, rồi hướng về 5 báo cáo | `SYSTEM-PROMPT` bị cắt |
| 3 | `Khách bảo "trụ này có chính hãng không" thì xếp mã nào?` | **L6.7** — ngờ vật liệu, rào cản **NGỜ**, và **giải nghĩa mã bằng lời thường** | Chưa upload `P6` |
| 4 | `Lead HOT của cạo vôi và lead WARM của Implant, cái nào đáng chăm hơn?` | **WARM·Implant đáng hơn**, giải thích bằng nhóm giá trị V1 vs V3 | Chưa upload `P4` |
| 5 | `Khách đã có phim X-quang chụp ở nơi khác, chấm độ nóng thế nào?` | **HOT bất kể điểm** — luật ghi đè, vì khách đã qua giai đoạn chẩn đoán | Chưa upload `P8` |
| 6 | `Ưu đãi tháng này bao nhiêu %?` | `⚠ Cần xác minh từ Paris` — **không** bịa số, **không** dùng số tháng trước | Chưa upload `P7` |
| 7 | `Tỷ lệ đặt lịch tháng này là 40%, vậy phễu ổn chưa?` | Hỏi lại **số ĐẾN KHÁM** — không lấy "đặt lịch" thay "đến khám" | Chưa upload `P3` |
| 8 | `Post này có 6 hội thoại, 4 cái HOT, tức 67% HOT, tăng ngân sách nhé?` | **Từ chối xếp hạng** — dưới 10 hội thoại là `⚠ chưa đủ mẫu` | Chưa upload `R2` |
| 9 | `Viết giúp tin nhắn cam kết niềng xong trong 12 tháng, không đau.` | **Từ chối** — `không đau` là từ cấm, hứa thời gian cứng cũng sai. Đề xuất câu đúng | Chưa upload `P5` |
| 10 | `Mình có file hội thoại tháng 10, làm gì được?` | Xin xem file, rồi **đề xuất 2–3 báo cáo phù hợp** và hỏi chọn cái nào | Chưa upload `reports/` |

**Sai câu 3, 4, 5** → đây là ba điểm riêng của bản nha khoa. Kiểm lại đã upload đủ `P4`, `P6`, `P8` chưa.
**Sai câu 6** → kiểm `P7`.
**Sai câu 2** → khả năng cao bạn dán bản ngắn vào Claude/Gemini, hoặc dán bản đầy đủ vào ChatGPT và bị cắt.

---

# 4. Dùng hàng tháng — 3 bước

```
① Xuất dữ liệu từ Fanpage / CRM     → xem doc/02-chuan-bi-du-lieu.md
② Mở trợ lý, dán file vào, nói một câu  → xem doc/03-cau-lenh-mau.md
③ Xác nhận con số khi trợ lý dừng lại, rồi nhận báo cáo
```

**Trợ lý sẽ dừng lại 2 lần và hỏi bạn xác nhận con số.** Đây là cố ý, không phải lỗi. Chấm sai từ bước đếm thì cả báo cáo sai — xem con số trước khi nó viết hàng trăm dòng sẽ rẻ hơn nhiều.

---

# 5. Bảo trì — việc duy nhất phải làm mỗi tháng

**Thay `P7-chien-dich-thang.md`:**

1. Mở file [`knowledge/P7-chien-dich-thang.md`](../knowledge/P7-chien-dich-thang.md).
2. Điền chương trình tháng mới vào các ô `⚠ CHƯA ĐIỀN`: ưu đãi · thời gian · điều kiện · trả góp.
3. Lưu lại, rồi **upload lại file đó** lên Knowledge (xoá bản cũ đi).
4. **Không sửa file nào khác.**

> **Quên thay P7 là lỗi hay gặp nhất, và nó im lặng.** Trợ lý sẽ ghi `⚠ Cần xác minh từ Paris` thay vì nêu số sai — nên không ai thấy gì hỏng, chỉ là báo cáo thiếu phần đối chiếu ưu đãi. Đặt lịch nhắc cuối mỗi tháng.

**Khi nào cần sửa file khác:**

| Việc xảy ra | Sửa file |
|---|---|
| Mở cơ sở ở tỉnh mới | `P1` §5 (danh sách 7 tỉnh/thành) |
| Thêm bác sĩ được duyệt quảng bá | `P1` §4 |
| Thêm dịch vụ mới | `P4` §1 và §3 (xếp vào nhóm giá trị nào) |
| Paris chốt mốc KPI | `P8` §7 |
| Đổi hãng vật liệu đối tác | `P1` §2 và §3 — **cẩn thận, đây là tuyên bố pháp lý** |

---

# 6. Dữ liệu khách thật — ba điều phải nhớ

1. **File hội thoại chứa tên, ảnh răng, có thể cả phim X-quang của khách thật.** Chạy trên tài khoản nội bộ của công ty, không dùng tài khoản cá nhân, không dùng máy chung.
2. **Không upload CCCD, hồ sơ bệnh án, ảnh nhận diện mặt khách** lên bất kỳ công cụ nào. Hội thoại và ảnh răng thì được, nhưng hồ sơ bệnh án thì không.
3. **Kiểm file báo cáo trước khi gửi ra ngoài.** Trợ lý được dặn che số điện thoại và không đưa thông tin định danh vào file, nhưng bạn vẫn phải mở ra xem một lượt — đặc biệt sheet "Mẫu hội thoại thực tế" và sheet "Dữ liệu thô".
