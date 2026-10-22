# 05 · XỬ LÝ SỰ CỐ

> Tra theo **triệu chứng** ở cột đầu. Phần lớn sự cố là do thiếu một file trên Knowledge.

---

# 1. Trợ lý trả lời sai kiểu

| Triệu chứng | Nguyên nhân | Cách xử lý |
|---|---|---|
| Nhận lời tạo AI-Agent, viết system prompt cho bạn | Dán thiếu khối ▼▲, hoặc dán bản đầy đủ vào ChatGPT và **bị cắt mất phần cuối** | Dán lại. ChatGPT thì phải dùng [`SYSTEM-PROMPT-NGAN.md`](../SYSTEM-PROMPT-NGAN.md) |
| Tự nhận sẽ nhắn cho khách, hoặc trả lời như đang chat với khách | Bỏ qua §1 của bộ não | Nhắc: *"Bạn không chat với khách. Mọi nội dung là bản gợi ý để người duyệt."* |
| Trả lời toàn mã L6.7, V-03, HOT·V1 — đọc không hiểu | Bỏ khối "làm việc với người không làm IT" | Nhắc: *"Giải nghĩa mã bằng lời thường ngay lần đầu dùng."* |
| Chạy một mạch rồi mới cho xem, không dừng lại hỏi | Bỏ hai điểm dừng | Nhắc: *"Dừng lại ở bước đếm và bước phân bố cho tôi xác nhận."* |
| Tự nghĩ ra cấu trúc báo cáo khác mỗi lần chạy | **Chưa upload `reports/R1–R6`** | Upload 6 file trong [`reports/`](../reports/) |

---

# 2. Trợ lý chấm sai

| Triệu chứng | Nguyên nhân | Cách xử lý |
|---|---|---|
| Xếp sai trạng thái L, hoặc không biết L6.7 | **Chưa upload `P6-van-hanh.md`** | Upload lại. `P6` là xương sống, thiếu nó cả hệ sai |
| Không có cột nhóm giá trị V1/V2/V3 | Chưa upload `P4-dich-vu.md` | Upload lại `P4` |
| Chấm khách đã có phim X-quang thành WARM hoặc COLD | Bỏ **luật ghi đè** | Nhắc: *"Áp 3 luật ghi đè ở P8 §1."* Kiểm đã upload `P8` chưa |
| Xếp khách ở Hải Phòng vào L2.5 "xa cơ sở" | Không biết 7 tỉnh/thành có cơ sở | Nhắc `P1` §5. Hải Phòng **có** cơ sở → khách bảo xa thì là **L6.4** |
| Gộp L6.7 vào L6.2 | Bỏ mã riêng của ngành nha | Nhắc: *"L6.7 ngờ vật liệu là mã riêng, không gộp vào L6.2 so sánh nơi khác."* |
| Hai bảng cho hai con số khác nhau về cùng một hội thoại | Chấm hai lần | Nhắc: *"Chấm một lần, mọi bảng đọc chung kết quả đó."* Yêu cầu chạy lại tự kiểm bước cuối |

---

# 3. Trợ lý kết luận sai hướng

| Triệu chứng | Nguyên nhân | Cách xử lý |
|---|---|---|
| Xếp hạng post chỉ bằng `% HOT`, khuyên tăng tiền cho post banner giá rẻ | Thiếu cột `% V1` | Nhắc: *"Thêm sheet Post × Nhóm giá trị. Không xếp hạng post chỉ bằng %HOT."* |
| Khuyên tắt post có 6 hội thoại vì "% HOT thấp" | Bỏ luật mẫu nhỏ | Nhắc: *"Dưới 10 hội thoại là ⚠ chưa đủ mẫu, không xếp hạng, không khuyến nghị."* |
| Kết luận "nhóm mất răng nóng hơn nhóm hỏi chung" từ bảng chia theo vấn đề răng | **Lặp vòng** — tín hiệu ① chính là "nêu vấn đề cụ thể" | Nhắc: *"Chạy cột `% HOT*` ở P8 §2. Bỏ tín hiệu ① mà chênh lệch biến mất thì nói thẳng là không có bằng chứng."* |
| Nói phễu đang ổn trong khi chưa có số đến khám | Lấy "đặt lịch" thay "đến khám" | Nhắc: *"Không lấy đặt lịch thay đến khám. Ghi ⚠ chưa đo được show-up."* |
| Tự kết luận "đạt KPI" khi Paris chưa chốt mốc | Tự đặt mốc | Nhắc: *"Chưa có mốc thì nêu số thật + ⚠ chưa có mốc so sánh."* |
| Nói "tháng này cải thiện" khi chênh lệch chỉ 2 điểm % trên mẫu 40 ca | Bỏ ngưỡng nhiễu | Nhắc khuôn [`R5`](../reports/R5-so-sanh-hai-ky.md): ngưỡng nhiễu theo cỡ mẫu |
| So sánh hai kỳ lấy mẫu khác nhau | Bỏ cổng chặn bước 0 của R5 | Nhắc: *"Chạy cổng chặn 4 câu trước. Khác cách lấy mẫu thì dừng."* |

---

# 4. Lỗi an toàn & pháp lý — xử lý ngay

| Triệu chứng | Mức | Cách xử lý |
|---|---|---|
| Nội dung gợi ý có `không đau`, `cam kết 100%`, `tốt nhất`, `rẻ nhất`, `dùng vĩnh viễn` | 🔴 Cao | Nhắc `P5` §5. **Không gửi nội dung đó cho khách.** Yêu cầu viết lại |
| Gắn "chính hãng" cho vật liệu ngoài Straumann/Invisalign/Nacera/Ormco | 🔴 Cao | **Tuyên bố pháp lý sai.** Nhắc `P1` §3. Sửa ngay |
| Chốt một con số giá cuối cùng cho ca cụ thể | 🔴 Cao | Nhắc: *"Nêu khung giá niêm yết thì được, chốt số cuối thì không."* |
| Nêu tên bác sĩ không có trong `P1` §4 | 🟠 Vừa | Nhắc: chỉ 3 bác sĩ trong danh sách. Tên khác → `⚠ Cần xác minh từ Paris` |
| Nêu % ưu đãi của tháng trước | 🟠 Vừa | **Chưa thay `P7`.** Điền `P7` tháng mới rồi upload lại |
| Hứa thời gian điều trị cứng ("niềng xong trong 12 tháng") | 🟠 Vừa | Nhắc `P5` §1 lỗi 8. Nói khung + "bác sĩ xác định sau khi chụp phim" |
| File báo cáo có số điện thoại khách, hoặc trích dẫn chưa che số | 🔴 Cao | Nhắc §10.8 bộ não. **Sửa file trước khi chia sẻ ra ngoài** |
| Chẩn đoán qua ảnh ("răng chị bị viêm tủy rồi") | 🔴 Cao | Nhắc: không chẩn đoán. Nhận định sơ bộ rồi mời khám + chụp phim |

> **Việc duy nhất phải làm mỗi tháng là thay `P7`.** Quên thay thì trợ lý ghi `⚠ Cần xác minh từ Paris` chứ không nêu số sai — nên không ai thấy gì hỏng, chỉ là báo cáo thiếu phần đối chiếu ưu đãi. Đặt lịch nhắc cuối tháng.

---

# 5. Lỗi dữ liệu đầu vào

| Triệu chứng | Nguyên nhân | Cách xử lý |
|---|---|---|
| Trợ lý đếm được ít hội thoại hơn bạn nghĩ | File cắt dở, hoặc định dạng không đồng nhất giữa các khối | Xem con số nó báo ở DỪNG 1. Lệch nhiều thì xuất lại file |
| R2 không nối được post với hội thoại | **Mất thẻ nguồn** ở tin đầu, hoặc tên post trong danh sách sai một ký tự | Xuất lại file giữ nguyên dòng `[Thẻ: Inbox từ quảng cáo …]`. Lấy tên post đúng theo [`02-chuan-bi-du-lieu`](02-chuan-bi-du-lieu.md) §5 |
| Mọi post đều trông tốt, không phân biệt được | **Mẫu đã bị lọc** theo độ dài | Xuất lại **toàn bộ** hội thoại trong kỳ. Hoặc nói rõ đã lọc và chỉ dùng báo cáo để đọc chân dung khách, không dùng để quyết ngân sách |
| Tỷ lệ có SĐT ra 100% | Mẫu đã lọc "chỉ hội thoại có số" | Mất luôn mẫu số. Xuất lại toàn bộ |
| R3 không chấm được tiêu chí ① | Mất dấu thời gian từng tin | Xuất lại có dấu thời gian. Không được thì chấp nhận chuẩn đạt đổi sang ≥7/9 |
| R3 ghi `⚠ không đo được` tiêu chí ⑦ ⑧ | CRM không có phần ghi chú bàn giao, hoặc không xuất ra | Bình thường ở lần đầu chạy. Nếu muốn đo thì cần CRM lưu phần ghi chú 13 trường |
| Nhiều hội thoại bị xếp `V-11 chưa rõ` | Khách hỏi chung thật, **hoặc** file mất phần nội dung tin khách | Mở vài ca `V-11` xem có đúng là hỏi chung không. Toàn ca có nội dung mà vẫn V-11 → báo lại trợ lý |

---

# 6. Vấn đề kỹ thuật nhẹ

| Triệu chứng | Cách xử lý |
|---|---|
| Nói đã tạo file Excel mà không thấy file đâu | Nền tảng không chạy được code. Yêu cầu: *"Trả bảng markdown để tôi dán vào Excel."* |
| File Excel mở ra lỗi font, chữ tiếng Việt thành ô vuông | Yêu cầu dùng font **Arial** toàn bộ, lưu UTF-8 |
| Báo cáo quá dài, không trình bày được | *"Rút lại thành 1 trang cho ban giám đốc."* Hoặc chạy [`R4`](../reports/R4-bao-cao-dieu-hanh.md) — nó có sẵn bản tóm tắt 1 trang |
| Dán bản ngắn vào ChatGPT vẫn bị cắt | Đã sửa bản ngắn làm vượt 8.000. Đếm lại khối ▼▲ (hiện **7.744**, chỉ dư **256**) |
| Hội thoại dài quá, trợ lý quên phần đầu | Chia file thành 2–3 phần, chạy từng phần rồi yêu cầu gộp kết quả. Hoặc dùng Claude Project (ngữ cảnh lớn hơn) |

---

# 7. Khi không biết lỗi ở đâu — làm lại 4 bước

1. **Hỏi lại trợ lý:** `Bạn là ai? Làm được những báo cáo nào?` → không trả về 6 báo cáo R1–R6 thì phần chỉ dẫn đang sai.
2. **Kiểm Knowledge:** đủ **13 file** chưa (8 file `P`, 5 file `R`)? Thiếu `P6` hoặc `P8` là sai nhiều nhất.
3. **Chạy lại 10 câu smoke test** ở [`01-cai-dat`](01-cai-dat.md) §3. Câu nào sai thì cột cuối chỉ đúng file cần kiểm.
4. **Vẫn sai** → tạo Project/Gem/GPT mới, cài lại từ đầu. Nhanh hơn đi tìm lỗi trong một cấu hình đã lộn xộn.
