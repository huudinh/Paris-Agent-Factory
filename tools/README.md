# tools/ — công cụ đối chiếu con số (tuỳ chọn)

> **Người dùng không làm IT thì bỏ qua thư mục này.** Trợ lý tự đọc và tự đếm, không cần script nào.
>
> Thư mục này dành cho người muốn **đếm lại con số bằng máy** để đối chiếu với kết quả trợ lý — hữu ích khi mẫu lớn và bạn muốn chắc chắn trợ lý không đếm lệch.

---

## Dùng để làm gì

Trợ lý AI đọc hiểu được sắc thái, nhưng khi đếm vài trăm hội thoại thì có thể lệch vài ca mà không ai biết. Script này đếm bằng khớp từ khoá — **dở hơn về đọc hiểu, nhưng không bao giờ đếm lệch**.

Chạy cả hai, rồi so con số ở **DỪNG 1** và **DỪNG 2**:

| Lệch bao nhiêu | Nghĩa |
|---|---|
| Dưới 5% | Bình thường. Script bắt theo chữ, trợ lý bắt theo nghĩa |
| 5–15% | Xem lại vài ca lệch, thường là ca nói vòng hoặc viết sai chính tả |
| Trên 15% | **Có vấn đề.** Hoặc file có định dạng lạ, hoặc trợ lý bỏ qua một phần dữ liệu |

**Khi lệch, tin bản đọc tay.** Script không hiểu *"để em tính đã"* là ngại tiền hay ngại thời gian.

---

## Cài đặt

Cần **Python 3.8+**. Không cần thư viện ngoài cho `phan_loai.py`.

```bash
python --version
```

---

## Chạy

```bash
cd tools
python phan_loai.py --src ../doc/mau-du-lieu/MAU_Hoi-thoai.md
```

Tham số:

| Tham số | Mặc định | Nghĩa |
|---|---|---|
| `--src` | *(bắt buộc)* | File hội thoại `.md` theo định dạng ở [`doc/02-chuan-bi-du-lieu.md`](../doc/02-chuan-bi-du-lieu.md) §4 |
| `--out` | `rows.json` | File kết quả. Trợ lý đọc được file này để khỏi phải chấm lại |
| `--tu-dien` | `tu-dien-van-de-rang.json` | Từ điển từ khoá |

**Kết quả:**
- In ra màn hình: bảng đếm — tổng hội thoại · có SĐT · HOT/WARM/COLD · V1/V2/V3 · 11 nhóm vấn đề răng · giai đoạn · rào cản · **cảnh báo từ cấm** · phân bố post.
- Ghi ra `rows.json`: một dòng mỗi hội thoại, có đủ bitmask · L-code · vấn đề răng · nhóm giá trị · rào cản.

---

## Sửa từ điển — không cần biết code

Mở [`tu-dien-van-de-rang.json`](tu-dien-van-de-rang.json), thêm từ khoá vào đúng nhóm. Đây là việc của người làm nội dung, không phải của IT.

**Khi nào cần sửa:**
- Khách Paris dùng cách gọi khác mà từ điển chưa có (*"răng cấm"*, *"răng hàm trong"*, *"làm cầu"*).
- Thêm dịch vụ mới → thêm từ khoá vào nhóm `van_de` và xếp vào `gia_tri`.
- Script xếp nhiều hội thoại vào `V-11 chưa rõ` → thiếu từ khoá, bổ sung vào.

**Lưu ý khi sửa:**
- Thứ tự trong `van_de` là **thứ tự ưu tiên** — khớp nhóm đầu tiên thì lấy. `V-01 làm lại ca lỗi` đứng đầu là cố ý: khách sửa ca cũ cần giọng tư vấn khác hoàn toàn.
- Từ khoá viết **chữ thường, có dấu đầy đủ**. Script khớp theo biên từ, nên `"giá"` không khớp trong `"gia đình"`.
- Đừng thêm từ quá ngắn hoặc quá chung (`"răng"`, `"làm"`) — sẽ khớp bừa.
- Sửa xong chạy lại trên [`MAU_Hoi-thoai.md`](../doc/mau-du-lieu/MAU_Hoi-thoai.md) xem con số có còn hợp lý không.

---

## Giới hạn của script — đọc trước khi tin

Script này **khớp từ khoá**, không hiểu nghĩa. Nó làm được và không làm được:

| Làm được | Không làm được |
|---|---|
| Đếm chính xác số hội thoại, số có SĐT | Hiểu *"để em tính đã"* là ngại tiền hay ngại thời gian |
| Nhận ra khách nói *"trụ có chính hãng không"* → `L6.7` | Nhận ra khách ngờ vật liệu mà diễn đạt vòng (*"em sợ không được như quảng cáo"*) |
| Bắt từ cấm trong lời nhân viên | Bắt lỗi *"trượt câu hỏi ngầm"* — cái này cần đọc hiểu |
| Gán `V-01…V-11` khi khách nói rõ tình trạng | Gán đúng khi khách tả vòng hoặc viết sai chính tả |
| Chấm 5 tín hiệu theo chữ | Chấm tiêu chí ④ *"tạo tin cậy bằng bằng chứng đúng rào cản"* |
| Áp 3 luật ghi đè khi có từ khoá rõ | Phát hiện khách đã khám nơi khác mà không nói chữ *"khám"* |

**Tiêu chí ① (phản hồi ≤2 phút) và cả bảng chấm 10 tiêu chí của [`R3`](../reports/R3-chat-luong-tu-van.md) thì script không làm.** Việc đó cần đọc hiểu, để trợ lý làm.

---

## Đưa `rows.json` cho trợ lý

Có `rows.json` rồi thì nói với trợ lý:

```
Đây là file rows.json em đã đếm bằng script. Dùng lại kết quả chấm này,
đừng chấm lại. Chỉ cần kiểm giúp mình vài ca lệch rồi viết báo cáo.
```

Cách này tiết kiệm thời gian với mẫu lớn, và đảm bảo con số giữa các bảng khớp nhau tuyệt đối — vì cả báo cáo đọc từ một nguồn duy nhất.

---

## Đối chiếu trên file mẫu

Chạy script trên [`MAU_Hoi-thoai.md`](../doc/mau-du-lieu/MAU_Hoi-thoai.md) (12 hội thoại mô phỏng) sẽ ra:

```
Tach duoc            12 hoi thoai
Co SDT                5  (41.7%)
HOT 2 · WARM 7 · COLD 3     — trong do 3 ca do LUAT GHI DE
V1 6 · V2 3 · V3 3
RAO CAN: NGO 4 · SO 4 · NGAI 2 · NGO+NGAI 1   (mot HT mang nhieu rao can)
HT co TU CAM trong loi nhan vien: 1   -> HT#4 (cam ket 100%, khong dau, khong hai gi)
```

Con số này khớp với bảng ghi chú ở cuối file mẫu. Chạy ra khác → kiểm lại đã sửa gì trong từ điển.

> Lưu ý về con số trên: nhiều hội thoại trong mẫu bị xếp `S3` thay vì `S2`, vì script ưu tiên rào cản — có rào cản thì vào `S3`. Đúng theo thiết kế, nhưng nghĩa là **phân bố giai đoạn của script thô hơn bản trợ lý đọc**. Dùng con số giai đoạn của trợ lý, dùng con số tổng và độ nóng của script.
