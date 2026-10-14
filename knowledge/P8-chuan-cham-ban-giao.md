# P8 — CHUẨN CHẤM ĐIỂM · PHÂN LOẠI · SLA · KPI
Module brand-specific. **Đây là thước đo của toàn bộ hệ báo cáo.** Khi module khác mâu thuẫn với P8 về cách chấm, **P8 thắng**. Cập nhật: 2026-10-14.

---

## §1. ⭐ NĂM TÍN HIỆU → HOT / WARM / COLD

Mỗi tín hiệu **1 điểm**, chấm trên toàn hội thoại:

| # | Tín hiệu | Tính là CÓ khi |
|---|---|---|
| **①** | **Nêu dịch vụ / tình trạng răng cụ thể** | *"mất răng số 6"*, *"niềng trong suốt"*, *"bọc sứ 4 răng trên"*, *"răng khôn mọc lệch"* — **không** tính *"làm răng"*, *"tư vấn giúp em"* |
| **②** | **Mốc thời gian ≤ 14 ngày** | Nói rõ tuần này / tháng này / cuối tuần · hoặc đã đặt lịch · hoặc đang trên đường đến |
| **③** | **Hỏi lịch, bác sĩ, chi phí hoặc trả góp theo đúng tình trạng của mình** | *"ca của em thì bao nhiêu"*, *"bác sĩ nào làm Implant"*, *"mai có lịch không"* — **không** tính câu hỏi giá chung chung ở tin đầu |
| **④** | **Gửi ảnh răng / phim X-quang / mô tả rõ tình trạng** | Có ảnh, hoặc mô tả đủ: vị trí · bao lâu · đã làm gì |
| **⑤** | **Để lại SĐT/Zalo thật và đồng ý nhận tư vấn** | Ưu tiên có nêu khung giờ tiện nghe máy |

| Mức | Điểm | Nghĩa |
|---|---|---|
| **HOT** | **4–5** | Sẵn sàng đặt lịch khám |
| **WARM** | **2–3** | Quan tâm rõ, còn vướng rào cản hoặc đang so sánh |
| **COLD** | **0–1** | Hỏi tham khảo |

### Ba luật ghi đè — đặc thù nha khoa

1. **Đã đặt lịch khám, hoặc đang đến phòng khám → HOT** bất kể điểm.
2. **Đã có phim X-quang, hoặc đã khám nơi khác và có phác đồ/báo giá rồi → HOT** bất kể điểm. Khách đã qua giai đoạn chẩn đoán, chỉ còn chọn nơi làm — đây là lead nóng nhất của ngành nha, mà thang 5 tín hiệu thường chấm thấp oan cho họ.
3. **Đang đau cấp (V-06) → tối thiểu WARM**, kể cả chỉ được 1 điểm. Người đau răng không viết tin dài, nhưng họ đến trong ngày.

### Cách ghi lại
Ghi kết quả dạng **bitmask 5 chữ số**: `[10110]` = có ①③④, thiếu ②⑤.
Mọi file Excel phải có cột bitmask này. **Không có bitmask thì không ai kiểm lại được điểm.**

---

## §2. CHẤM LẠI KHÔNG KỂ TÍN HIỆU ① — cột `% HOT*`

> ⚠️ **Luật chống lặp vòng. Đây là lỗi phân tích đã xảy ra thật và phải chống bằng quy tắc, không bằng sự cẩn thận.**

Tín hiệu ① là *"nêu dịch vụ/tình trạng cụ thể"*. Khi một bảng **chia nhóm theo vấn đề răng** (biểu đồ nhiệt), thì mọi nhóm có vấn đề cụ thể **đã được cộng sẵn 1 điểm** — trong khi nhóm `V-11 chưa rõ` thì không. So sánh `% HOT` giữa các nhóm đó là so sánh một thứ đã được định nghĩa sẵn: **kết luận giả**.

**Bắt buộc:** mọi bảng chia nhóm theo vấn đề răng phải có thêm cột **`% HOT*`** — chấm lại chỉ bằng 4 tín hiệu ②③④⑤, đạt **≥3/4** tính là HOT\*.

Ghi ngay dưới bảng: cột nào dùng được, cột nào không, và số thật là bao nhiêu. **Nếu bỏ tín hiệu ① mà chênh lệch biến mất thì nói thẳng là "không có bằng chứng"**, không được giữ kết luận cũ.

→ Luật này áp cho **mọi** trường hợp chia nhóm theo một thuộc tính vốn là tín hiệu chấm điểm, không chỉ riêng tín hiệu ①.

---

## §3. BA TRỤC & MA TRẬN ƯU TIÊN

Ba trục: **L-code** ([[P6-van-hanh]] §2) · **Độ nóng** (§1 trên) · **Nhóm giá trị V1/V2/V3** ([[P4-dich-vu]] §3). Ba cột riêng, không gộp.

Ma trận ưu tiên HOT/WARM/COLD × V1/V2/V3: xem [[P4-dich-vu]] §3.

**Điều phải nhớ khi viết khuyến nghị:** HOT·V3 chốt nhanh nhưng giá trị nhỏ; WARM·V1 chậm nhưng đáng đầu tư hơn. Báo cáo nào xếp hạng lead chỉ bằng độ nóng là báo cáo sai hướng cho ngành nha.

---

## §4. SLA GỌI SAU KHI CÓ SỐ

| Khung giờ nhận số | HOT · V1 | HOT · V2–V3 | WARM | COLD |
|---|---|---|---|---|
| **8h30–12h · 13h30–18h30** | ≤ **5'** | ≤ 10' | ≤ 30' | Nhắn Zalo ≤2h, gọi trong ngày |
| **12h–13h30** | ≤ 15' | ≤ 30' | Trước 14h | Trong ngày |
| **18h30–21h** | ≤ 10' | ≤ 20' | ≤ 60' hoặc đúng giờ hẹn | Hàng đợi sáng hôm sau |
| **21h–8h30** | Khách đồng ý tối: ≤15' | Sáng 8h30–10h | 8h30–10h | 10h–12h |

**Giới hạn tải:** khoảng **8 số HOT/giờ/người**. Vượt thì chuyển người cùng bậc đang rảnh.

**Ngoại lệ ngành nha — khách đau cấp (V-06):** gọi ngay bất kể độ nóng, bất kể khung giờ. Người đau răng sẽ đi nơi gần nhất gọi lại trước.

---

## §5. CHUỖI CHĂM SÓC SAU KHI XIN SỐ — T+0 → T+7

| Mốc | Việc |
|---|---|
| **T+0 ≤ 2'** | Nhắn xác nhận: **tên người sẽ gọi · số sẽ gọi · giờ gọi** (bước B5) |
| **T+30'** | Chưa nghe máy → hỏi lại khung giờ tiện nghe máy để báo bác sĩ sắp xếp |
| **T+2h** | Gửi nội dung giá trị theo đúng rào cản (bác sĩ · vật liệu hãng · lộ trình), hỏi lại khung giờ |
| **T+24h** | Gọi lần 2. Trực page **nhắn nhắc 15 phút trước** |
| **T+72h** | Mời khám + chụp phim (nhấn **chưa phải điều trị**), kèm chương trình nếu có |
| **T+7 ngày** | **Lần chạm cuối.** Không phản hồi thì chuyển nhóm nuôi dưỡng dài hạn |

**Trần: tối đa 6 lần nhắn / 7 ngày. Khách từ chối thì dừng ngay.**

> **Hai nhịp khác nhau, đừng lẫn:** chuỗi **T** dùng **ngay sau khi xin được số**; nhịp **D+3 / D+7 / D+15** dùng khi **đã tư vấn mà chưa đặt lịch khám** (L6.x). Với **L6.x · V1** thì nuôi tới **90 ngày** rồi mới hạ tệp.

---

## §6. ⭐ BẢNG CHẤM HỘI THOẠI — 10 TIÊU CHÍ · CHUẨN ĐẠT ≥ 8/10

| # | Tiêu chí | Đạt khi |
|---|---|---|
| **①** | **Phản hồi ≤ 2 phút** | Chênh lệch dấu thời gian tin khách → tin nhân viên đầu tiên ≤ 2' |
| **②** | **Gọi đúng tên dịch vụ / tình trạng** theo post khách bấm vào | Tin mở nhắc đúng dịch vụ, không hỏi chung "cần tư vấn gì" |
| **③** | **Thu đủ 4 thông tin** | Tình trạng (vị trí · bao lâu) · đã điều trị ở đâu chưa · mong muốn · thời gian dự kiến |
| **④** | **Tạo tin cậy bằng bằng chứng**, đúng rào cản khách mang | Có ít nhất 1 bằng chứng thật ([[P1-thuong-hieu]] §2), không chỉ tính từ |
| **⑤** | **Xin số có lý do có lợi cho khách** | Lý do kiểu "để bác sĩ xem phim, báo lộ trình sát". ❌ "để gửi ưu đãi" |
| **⑥** | **Xác thực số / Zalo** | Có hỏi lại số có Zalo không, hoặc có xác nhận đúng số |
| **⑦** | **Phân loại HOT/WARM/COLD + nhóm giá trị V** | Có ghi chú phân loại, không để trống |
| **⑧** | **Phiếu bàn giao đủ 13 trường** ([[P6-van-hanh]] §5) | Dữ liệu không có phần ghi chú → `⚠ không đo được`, không cho 0 oan |
| **⑨** | **Không dùng từ cấm · không gắn "chính hãng" sai · không chốt giá cứng** | Xem [[P5-kich-ban]] §5 |
| **⑩** | **Nêu rõ bước tiếp theo** | Ai gọi · số nào · lúc mấy giờ (bước B5) |

> **Vi phạm tiêu chí ⑨ thì toàn hội thoại 0 điểm**, bất kể 9 tiêu chí kia. Đây là rủi ro pháp lý, không phải lỗi kỹ năng.

**Cách báo điểm:** luôn kèm **trích dẫn thật** từ hội thoại làm bằng chứng cho mỗi tiêu chí bị trừ. Bảng điểm không có trích dẫn thì nhân viên không phục và trưởng nhóm không đào tạo được.

---

## §7. KPI — mốc để báo cáo so vào

| Chỉ số | Mục tiêu | Ghi chú |
|---|---|---|
| Tỷ lệ hội thoại **xin được số** | `⚠ chờ Paris chốt` | Chỉ số chính của trực page |
| **Kết nối / số đã xin** (gọi được) | ≥ **78%** | Khâu hay hổng nhất |
| **Đặt lịch khám / kết nối** | ≥ **50%** | |
| **Đến khám / đặt lịch khám** (show-up) | `⚠ chờ Paris chốt` | Ngành nha thường rò nặng ở đây |
| **Chốt phác đồ / đến khám** | `⚠ chờ Paris chốt` | Xảy ra trên ghế khám, **không** thuộc trách nhiệm trực page |
| Số được **phân loại + có phiếu đủ** | ≥ **95%** | |
| HOT được gọi **đúng SLA** | ≥ **90%** | |
| Điểm chấm hội thoại | ≥ **8/10** | |

> **Chưa có mốc thì báo cáo nêu số thật và ghi `⚠ chưa có mốc so sánh`** — tuyệt đối không tự đặt mốc rồi kết luận "đạt / không đạt". Mốc là việc của Paris chốt, không phải việc của trợ lý suy ra.
>
> Năm mốc có số ở trên (78% · 50% · 95% · 90% · 8/10) là **mốc tham chiếu kế thừa từ hệ CSKH của tập đoàn**, chưa được Paris xác nhận cho ngành nha. Báo cáo phải ghi rõ điều đó khi so vào.

---

## §8. BỐN RỦI RO ĐỌC SỐ — báo cáo phải tự kiểm

| Rủi ro | Biểu hiện | Cách chống |
|---|---|---|
| **Mẫu bị lọc** | File hội thoại chỉ gồm "hội thoại dài" hoặc "hội thoại có số" | Hội thoại dài = khách tương tác nhiều = **đã thiên về phía nóng**. Thổi phồng mọi post, và thổi **không đều nhau** → ghi cảnh báo, **không dùng để quyết ngân sách** |
| **Mẫu nhỏ** | Một post / một nhóm có **dưới 10 hội thoại** | Ghi `⚠ chưa đủ mẫu`. **Không xếp hạng, không khuyến nghị** |
| **Lặp vòng** | Chia nhóm theo đúng thuộc tính đang dùng để chấm điểm | Chấm lại không kể tín hiệu đó (§2) |
| **Lạm phát HOT** | Chấm rộng tay nên HOT tràn lan, SLA vỡ | Đối chiếu **tỷ lệ đến khám của nhóm HOT** hằng tuần. HOT mà show-up thấp là chấm sai, không phải khách tệ |

---

## §9. BÁO CÁO NÀO DÙNG PHẦN NÀO CỦA P8

| Báo cáo | Dùng |
|---|---|
| [[R1-phan-loai-hoi-thoai]] | §1 · §2 · §3 · §5 |
| [[R2-phan-tang-quang-cao]] | §1 · §2 · §8 |
| [[R3-chat-luong-tu-van]] | §6 · §4 · §5 |
| [[R4-bao-cao-dieu-hanh]] | §3 · §7 · §8 |
| [[R5-so-sanh-hai-ky]] | §7 · §8 |

## 🔶 Cần Paris xác nhận
- Mốc KPI tỷ lệ xin số · show-up · chốt phác đồ: `⚠ chờ cấp`
- Cơ sở nào đủ năng lực All-On / ghép xương (ảnh hưởng định tuyến khách tỉnh): `⚠ chờ cấp`
- Phân tầng nhân sự CSKH để định tuyến HOT·V1: `⚠ chờ cấp`
