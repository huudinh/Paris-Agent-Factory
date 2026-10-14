# 03 · CÂU LỆNH MẪU — copy, dán, xong

> Không cần học thuật ngữ. Nói bằng lời thường cũng được — trợ lý tự hiểu. Các câu dưới đây là bản gọn nhất, dùng khi bạn đã biết mình muốn gì.

---

# A · BẮT ĐẦU KHI CHƯA BIẾT LÀM GÌ

Dán file vào rồi gõ:

```
Đây là file hội thoại tháng 10. Xem giúp mình dùng được những gì.
```

Trợ lý sẽ đếm file, báo thiếu gì, rồi **đề xuất 2–3 báo cáo phù hợp với đúng dữ liệu bạn có** và hỏi chọn cái nào. Không tự chạy báo cáo nặng mà bạn chưa đồng ý.

Hoặc hỏi thẳng điều bạn đang thắc mắc:

```
Tháng này mình thấy inbox nhiều mà đặt lịch ít. Xem giúp mình nghẽn ở đâu.
```

---

# B · NĂM CÂU LỆNH CHO NĂM BÁO CÁO

## R1 — Khách là ai, nhắn lại thế nào

```
Chạy báo cáo R1 cho file hội thoại này. Dịch vụ: Implant.
```

## R2 — Post nào kéo khách tốt

```
Chạy báo cáo R2. Đây là danh sách post và file hội thoại tháng 10. Kỳ: 01-31/10/2026.
```

## R3 — Nhân viên hổng khâu nào

```
Chạy báo cáo R3 cho file hội thoại này, kỳ tháng 10.
```

## R4 — Phễu rò ở đâu

```
Chạy báo cáo R4 cho tháng 10. Mình có thêm số đặt lịch là 86, số đến khám là 51.
```

Chưa có số đặt lịch / đến khám thì cứ chạy, trợ lý sẽ ghi rõ phần nào chưa đo được:

```
Chạy báo cáo R4 cho tháng 10. Mình chưa có số đến khám.
```

## R5 — Tháng này so tháng trước

```
So sánh tháng 9 và tháng 10. Đây là dữ liệu hai kỳ.
```

---

# C · HỎI NHANH — không cần mở báo cáo

Dùng khi đang trực page, cần tra một thứ cho nhanh.

| Bạn gõ | Nhận lại |
|---|---|
| `Khách hỏi "trụ này có chính hãng không" thì xếp mã nào?` | **L6.7** · rào cản NGỜ · bằng chứng nên dùng · nhịp chăm |
| `Khách bảo "để em hỏi chồng đã" thì làm gì?` | **L6.6** · không ép chốt · mời người nhà đi cùng buổi khám |
| `Khách cho số rồi gọi không nghe là trạng thái gì?` | **L5.3** · nhịp T+30' · nhắn hỏi lại khung giờ |
| `Khách đau răng nhắn lúc 10h đêm, xử lý sao?` | **Ngoại lệ V-06** — gọi ngay bất kể giờ, bất kể độ nóng |
| `Khách ở Thái Nguyên, có tính là xa không?` | **Có** — ngoài 7 tỉnh/thành có cơ sở → L2.5. (Trong 7 tỉnh mà bảo xa → L6.4) |
| `Lead HOT cạo vôi và lead WARM Implant, gọi ai trước?` | **WARM Implant** — V1 vs V3, giải thích bằng ma trận ưu tiên |
| `Nhân viên nói "niềng không đau đâu chị" có sai không?` | **Sai** — từ cấm, hội thoại bị 0 điểm. Kèm câu đúng nên nói |

---

# D · GIẢI THÍCH SỐ — khi không tin một con số trong báo cáo

```
Con số 23% HOT của post P03 này tính thế nào, có tin được không?
```

Nhận lại: cách tính · mẫu bao nhiêu · có đủ không · có bị thiên lệch không · **dùng được để quyết việc gì và không dùng được để quyết việc gì**.

```
Báo cáo nói post P05 nên tăng ngân sách. Vì sao, dựa vào đâu?
```

```
Sao tháng này tổng lead tăng mà báo cáo lại nói đang xấu đi?
```

> Câu cuối là tình huống rất hay xảy ra ở ngành nha: tổng lead tăng nhờ post giá rẻ, nhưng **lead nhóm giá trị lớn (Implant, All-On, Invisalign) lại giảm**. Bảng tổng trông đẹp, doanh thu kỳ vọng lại giảm.

---

# E · SỬA BÁO CÁO ĐÃ CHẠY

```
Sheet 3 thiếu cột nhóm giá trị. Thêm vào rồi xuất lại.
```

```
Phần xếp hạng post bỏ giúp mình mấy post dưới 10 hội thoại.
```

```
Báo cáo này mình cần trình bày cho ban giám đốc. Rút lại thành 1 trang.
```

Trợ lý được dặn **chỉ nêu phần thay đổi**, không in lại toàn bộ.

---

# F · BỐN VIỆC TRỢ LÝ SẼ TỪ CHỐI

| Bạn yêu cầu | Trợ lý trả lời |
|---|---|
| `Tạo cho mình một AI-Agent tư vấn Implant` | Ngoài phạm vi — nó không tạo agent. Hướng về 5 báo cáo |
| `Nhắn luôn cho khách này giúp mình` | Nó không chat với khách. Nó soạn nội dung gợi ý, bạn duyệt rồi dán |
| `Khách này răng bị viêm tủy phải không?` | Không chẩn đoán. Mời khách đi khám và chụp phim |
| `Báo giá ca này bao nhiêu?` | Không chốt giá ca cụ thể. Nêu khung giá niêm yết + mời khám |

Đây là **giới hạn cố ý**, không phải lỗi. Ba việc đầu là việc của người; việc cuối là rủi ro pháp lý ngành y tế.

---

# G · MẸO DÙNG

**Nói mục đích, đừng nói kỹ thuật.** *"Mình cần biết tháng tới dồn tiền vào post nào"* cho ra kết quả tốt hơn *"chạy R2 chế độ A"* — vì trợ lý sẽ chọn đúng phần báo cáo bạn cần và bỏ phần bạn không dùng.

**Trả lời khi nó dừng lại.** Trợ lý dừng 2 lần để bạn xác nhận con số. Gõ `đúng rồi, chạy tiếp` là xong. Thấy số lạ thì nói ngay — sửa ở đây rẻ hơn sửa sau rất nhiều.

**Chạy theo thứ tự R1 → R2 → R3 → R4.** R4 dùng lại kết quả của ba cái trước. Chạy R4 đầu tiên thì nó chỉ có bản rút gọn.

**Lưu lại file dữ liệu thô mỗi kỳ.** Đó là thứ làm cho R5 kỳ sau chạy được. Không có nó thì không so được hai kỳ.
