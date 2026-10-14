# -*- coding: utf-8 -*-
"""Style chuan cho moi file Excel cua Paris-Agent-Factory.

Dung module nay thay vi tu viet openpyxl moi lan -> moi bao cao ra cung mot
dinh dang, va sua quy uoc mau o MOT cho thi doi ca he.

Mau lay tu Design System Paris v3.1 (knowledge/P1-thuong-hieu.md):
  Cerulean Blue #2A52BE · Pantone Red 032 C #ED2E38 · White #FFFFFF
Ty le 80% trang/kem - 15% xanh - 5% do: trong Excel nghia la nen trang,
tieu de bang mau xanh deep, va do CHI dung cho nhan HOT va o canh bao.

Dung:
    from excel_style import *
    wb = so_moi()
    ws = sheet(wb, "Tổng quan")
    tieu_de(ws, "BÁO CÁO R1 — PHÂN LOẠI HỘI THOẠI", "Kỳ 01-31/10/2026")
    dong_tieu_de(ws, ["STT", "Tên KH", "Độ nóng"])
    for r in data: dong(ws, r)
    hoan_thien(ws, dong_tieu_de_o=5)
    wb.save("out.xlsx")
"""
from openpyxl import Workbook
from openpyxl.formatting.rule import ColorScaleRule
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.utils import get_column_letter

# ----------------------------------------------------------------- mau

BLUE = "2A52BE"        # Cerulean Blue — bo NDTH
BLUE_DEEP = "0C1D4D"   # tieu de section, nen header bang
BLUE_LIGHT = "EAF0FC"  # nen khoi nhat
BLUE_MID = "D7E2FA"    # vien, duong ke
RED = "ED2E38"         # Pantone Red 032 C — HOT, canh bao
RED_LIGHT = "FDEAEB"   # nen HOT
CREAM = "FBF8F3"       # nen section xen ke
INK = "131A2E"         # chu thuong
INK_SOFT = "4A5270"    # chu phu
LINE = "E4E1D8"        # vien the

# Quy uoc mau theo R1 §Trinh bay Excel + R2 §Trinh bay
HOT = RED_LIGHT        # do nhat
WARM = "FFE8CC"        # cam
COLD = "DCE9FB"        # xanh duong nhat
CANH_BAO = "FFF3C4"    # vang — MOI o co ⚠
TOT = "DFF3E3"         # xanh la nhat — khuyen nghi TANG NGAN SACH
MO = "EFEFEF"          # xam — dong chua du mau
B1 = BLUE_LIGHT        # buoc ① / giai doan S1
B2 = "FFE8CC"          # buoc ②
B3 = TOT               # buoc ③
B4 = CANH_BAO          # buoc ④

MAU_NONG = {"HOT": HOT, "WARM": WARM, "COLD": COLD}
MAU_GIA_TRI = {"V1": BLUE_MID, "V2": BLUE_LIGHT, "V3": CREAM}

FONT = "Arial"

# --------------------------------------------------------------- style

_th = Side(style="thin", color=LINE)
VIEN = Border(left=_th, right=_th, top=_th, bottom=_th)

F_H1 = Font(name=FONT, size=14, bold=True, color=BLUE_DEEP)
F_H2 = Font(name=FONT, size=11, bold=True, color=BLUE_DEEP)
F_HEAD = Font(name=FONT, size=10, bold=True, color="FFFFFF")
F = Font(name=FONT, size=10, color=INK)
F_B = Font(name=FONT, size=10, bold=True, color=INK)
F_PHU = Font(name=FONT, size=9, italic=True, color=INK_SOFT)
F_DO = Font(name=FONT, size=10, bold=True, color="C11B26")

NEN_HEAD = PatternFill("solid", fgColor=BLUE_DEEP)
NEN_CANH_BAO = PatternFill("solid", fgColor=CANH_BAO)
NEN_KHOI = PatternFill("solid", fgColor=BLUE_LIGHT)

TREN = Alignment(vertical="top", wrap_text=True)
GIUA = Alignment(vertical="center", horizontal="center", wrap_text=True)

# Cot nao de rong bao nhieu. Cot khong co trong bang -> tu do theo noi dung.
RONG = {
    "STT": 6, "STT HT": 8, "HT#": 7, "Mã post": 10, "Mã": 8, "#": 5,
    "Tên KH": 20, "Tên khách": 20, "Ngày": 13, "Phụ trách": 16,
    "Số tin": 7, "SĐT": 7, "Có SĐT": 8,
    "Vấn đề răng": 26, "Vấn đề răng (V-xx)": 26, "Tình trạng / Nhu cầu": 34,
    "Giai đoạn": 10, "Nhóm KH (insight)": 16, "Nhóm giá trị": 11,
    "Nhóm chăm sóc": 15, "L-code": 9, "Độ nóng": 10, "Rào cản": 22,
    "Kịch bản (mã)": 13, "Tên kịch bản": 26,
    "Nội dung gợi ý gửi ngay": 62, "Nội dung 1": 60, "Nội dung 2": 60,
    "Nội dung 3": 60, "Câu mẫu": 60, "Trích lời khách": 58,
    "Trích nguyên văn": 58, "Trích dẫn bằng chứng": 58,
    "Rào cản / ghi chú": 30, "Ghi chú (tín hiệu ①②③④⑤)": 34, "Ghi chú": 28,
    "Lưu ý": 40, "Lưu ý an toàn": 40, "Khi nào dùng": 30,
    "Insight khách hàng (nỗi lo thật)": 40, "Nhịp chăm sóc": 30,
    "Điều kiện dừng": 30, "Kịch bản gợi ý": 20, "Hành động": 30,
    "Mục tiêu": 24, "Tín hiệu nhận biết": 34, "Nghĩa": 26,
    "SLA kết nối": 18, "Số lead": 9,
    "Tên post (chuẩn hoá)": 30, "Tên post đúng như trong thẻ": 30,
    "Biến thể đã gom": 24, "Thông điệp chính": 40, "Góc tiếp cận": 24,
    "Số HT": 7, "Tỷ lệ có SĐT": 12, "% HOT": 9, "% HOT*": 9, "% V1": 8,
    "Điểm TB": 9, "Tầng chủ đạo": 13, "Đủ mẫu?": 11,
    "Rào cản nổi bật": 36, "Khuyến nghị": 22, "Lý do": 36,
    "Việc cần làm": 40, "Nhận định": 40, "Hàm ý cho thông điệp": 36,
    "Thẻ nguồn gốc (nguyên văn)": 46, "Mã post sau chuẩn hoá": 20,
    "Bitmask tín hiệu": 13, "Ghi đè?": 22, "Bước": 7, "Làm gì": 36,
    "Ký hiệu": 16, "Nghĩa là gì": 50, "Dùng ở đâu": 26,
    "Chỉ số": 30, "Giá trị": 30, "Công thức": 40, "Mốc": 14, "Chênh": 10,
    "Tiêu chí": 30, "Tổng điểm": 10, "Đạt?": 8,
    "Học phần": 11, "Nội dung": 40, "Người học": 26, "Mentor đề xuất": 16,
    "Cách đo kết quả": 36, "Vì sao cần (dẫn số từ sheet 4)": 40,
    "Mức rủi ro": 12, "Loại vi phạm": 22,
}


# ------------------------------------------------------------- ham dung

def so_moi():
    """Workbook moi, da bo sheet mac dinh."""
    wb = Workbook()
    wb.remove(wb.active)
    return wb


def sheet(wb, ten):
    """Them sheet. Excel gioi han ten sheet 31 ky tu va mot so ky tu cam."""
    ten = str(ten)
    for c in "[]:*?/\\":
        ten = ten.replace(c, "-")
    return wb.create_sheet(ten[:31])


def tieu_de(ws, chinh, phu=None, cot=1):
    """Tieu de sheet. Tra ve so dong da dung."""
    ws.cell(ws.max_row if ws.max_row > 1 else 1, cot, chinh).font = F_H1
    n = 1
    if phu:
        ws.cell(ws.max_row + 1, cot, phu).font = F_PHU
        n += 1
    ws.cell(ws.max_row + 1, cot, "")      # dong trong
    return n + 1


def muc(ws, chu):
    """Tieu de muc nho trong sheet."""
    ws.cell(ws.max_row + 1, 1, chu).font = F_H2
    return ws.max_row


def dong_tieu_de(ws, cot_ten):
    """Dong tieu de bang: nen xanh deep, chu trang, in dam."""
    r = ws.max_row + 1
    for i, ten in enumerate(cot_ten, start=1):
        c = ws.cell(r, i, ten)
        c.font = F_HEAD
        c.fill = NEN_HEAD
        c.alignment = GIUA
        c.border = VIEN
    ws._pf_head = r          # nho lai de freeze dung dong
    ws._pf_cot = list(cot_ten)
    ws._pf_so_head = getattr(ws, "_pf_so_head", 0) + 1
    return r


def dong(ws, gia_tri, nen=None, dam=False):
    """Mot dong du lieu. `nen` la ma mau HEX hoac None.

    O nao chua ky tu ⚠ thi tu to vang — luat chung cua ca he: moi so chua
    xac minh phai nhin thay ngay.
    """
    r = ws.max_row + 1
    for i, v in enumerate(gia_tri, start=1):
        c = ws.cell(r, i, v)
        c.font = F_B if dam else F
        c.alignment = TREN
        c.border = VIEN
        if isinstance(v, str) and "⚠" in v:
            c.fill = NEN_CANH_BAO
        elif nen:
            c.fill = PatternFill("solid", fgColor=nen)
    return r


def dong_nong(ws, gia_tri, do_nong, cot_nong=None):
    """Dong du lieu, to mau theo do nong (HOT/WARM/COLD).

    `cot_nong` = chi to rieng o do nong (1-based). None = to ca dong.
    """
    nen = MAU_NONG.get(str(do_nong).upper().rstrip("*"))
    if cot_nong is None:
        return dong(ws, gia_tri, nen=nen)
    r = dong(ws, gia_tri)
    if nen:
        ws.cell(r, cot_nong).fill = PatternFill("solid", fgColor=nen)
    return r


def to_mau(ws, r, c, hex_mau):
    """To nen mot o. Dung khi can to le ngoai cac ham dong()."""
    ws.cell(r, c).fill = PatternFill("solid", fgColor=hex_mau)


def so_do_buoc(ws, buoc):
    """So do cac buoc nam ngang: [(ten, mo_ta, mau), ...] -> 2 dong."""
    r1 = ws.max_row + 1
    r2 = r1 + 1
    for i, (ten, mo_ta, mau) in enumerate(buoc):
        c1, c2 = i * 2 + 1, i * 2 + 1
        a = ws.cell(r1, c1, ten)
        a.font = F_B
        a.alignment = GIUA
        a.border = VIEN
        a.fill = PatternFill("solid", fgColor=mau)
        b = ws.cell(r2, c2, mo_ta)
        b.font = F
        b.alignment = TREN
        b.border = VIEN
        b.fill = PatternFill("solid", fgColor=mau)
        if i < len(buoc) - 1:
            m = ws.cell(r1, c1 + 1, "→")
            m.font = F_B
            m.alignment = GIUA
    return r1


def trong(ws, n=1):
    for _ in range(n):
        ws.cell(ws.max_row + 1, 1, "")


def khoi_canh_bao(ws, tieu, dong_chu):
    """Khoi canh bao phuong phap — bat buoc co o sheet dau moi bao cao.

    Dat ngay sau ket luan, KHONG dat o cuoi file noi khong ai doc.
    """
    trong(ws)
    r = ws.max_row + 1
    c = ws.cell(r, 1, "⚠ " + tieu)
    c.font = Font(name=FONT, size=11, bold=True, color="C11B26")
    c.fill = NEN_CANH_BAO
    c.border = VIEN
    for d in dong_chu:
        rr = ws.max_row + 1
        cc = ws.cell(rr, 1, "• " + d)
        cc.font = F
        cc.alignment = TREN
        cc.fill = NEN_CANH_BAO
        cc.border = VIEN
    return r


def doc_nhanh(ws, dong_chu):
    """Khoi 'Doc nhanh' bat buoc di kem MOI bang nhiet.

    Khong co dien giai thi bang mau chi de nhin cho dep (R2 §Quy tac ve nhiet).
    """
    trong(ws)
    r = ws.max_row + 1
    c = ws.cell(r, 1, "ĐỌC NHANH")
    c.font = F_H2
    c.fill = NEN_KHOI
    for d in dong_chu:
        cc = ws.cell(ws.max_row + 1, 1, "→ " + d)
        cc.font = F
        cc.alignment = TREN
    return r


def nhiet(ws, dong_dau, cot_dau, dong_cuoi, cot_cuoi):
    """To nhiet vung o DEM bang color scale.

    KHONG to mau cung tung o, va KHONG to cot Tong/%/Du mau — thang gia tri
    khac han nen cot % se at het (R2 §Quy tac ve bieu do nhiet).
    Moi bang mot thang rieng: mau chi so sanh trong cung mot bang.
    """
    vung = "%s%d:%s%d" % (get_column_letter(cot_dau), dong_dau,
                          get_column_letter(cot_cuoi), dong_cuoi)
    ws.conditional_formatting.add(vung, ColorScaleRule(
        start_type="min", start_color="FFFFFF",
        mid_type="percentile", mid_value=50, mid_color="FFC46B",
        end_type="max", end_color=RED))
    return vung


def cot_phu_vang(ws, dong_dau, dong_cuoi, cot):
    """Cot Tong / % / Du mau: nen vang nhat, khong to nhiet."""
    for r in range(dong_dau, dong_cuoi + 1):
        ws.cell(r, cot).fill = PatternFill("solid", fgColor=CREAM)


def hoan_thien(ws, freeze=True, rong_toi_thieu=9, rong_toi_da=70):
    """Freeze dong tieu de + dat do rong cot. Goi SAU khi ghi het du lieu."""
    cot_ten = getattr(ws, "_pf_cot", None)
    head = getattr(ws, "_pf_head", None)

    for i in range(1, ws.max_column + 1):
        ten = cot_ten[i - 1] if cot_ten and i <= len(cot_ten) else None
        if ten and ten in RONG:
            w = RONG[ten]
        else:
            dai = 0
            for r in range(1, min(ws.max_row, 400) + 1):
                v = ws.cell(r, i).value
                if v is None:
                    continue
                dai = max(dai, max(len(x) for x in str(v).split("\n")))
            w = min(max(dai + 2, rong_toi_thieu), rong_toi_da)
        ws.column_dimensions[get_column_letter(i)].width = w

    # Chi freeze khi sheet co DUNG MOT bang va dong tieu de nam gan dau sheet.
    # Sheet tong quan co nhieu bang: freeze o bang cuoi se ghim hang chuc dong
    # dau, cuon xuong khong doc duoc gi.
    if freeze and head and getattr(ws, "_pf_so_head", 0) == 1 and head <= 10:
        ws.freeze_panes = ws.cell(head + 1, 1)
    return ws


# ------------------------------------------------------- sheet chu giai

CHU_GIAI_CHUNG = [
    ("⚠", "Số/thông tin CHƯA XÁC MINH. Mọi ô có ký hiệu này đều nền vàng. "
          "Không dùng để ra quyết định trước khi xác minh với Paris.", "Mọi sheet"),
    ("HOT / WARM / COLD", "Mức sẵn sàng, chấm theo 5 tín hiệu. "
     "HOT 4–5 điểm · WARM 2–3 · COLD 0–1.", "Cột Độ nóng"),
    ("① ② ③ ④ ⑤", "Năm tín hiệu: ① nêu dịch vụ/tình trạng răng cụ thể · "
     "② mốc thời gian ≤14 ngày · ③ hỏi lịch/bác sĩ/chi phí/trả góp theo tình "
     "trạng của mình · ④ gửi ảnh răng hoặc phim X-quang hoặc mô tả rõ · "
     "⑤ để lại SĐT/Zalo và đồng ý nhận tư vấn.", "Cột Ghi chú"),
    ("[10110]", "Bitmask 5 chữ số — tín hiệu nào có, tín hiệu nào không. "
     "Ví dụ [10110] = có ①③④, thiếu ②⑤. Không có bitmask thì không ai "
     "kiểm lại được điểm.", "Cột Ghi chú"),
    ("Ghi đè", "Ba luật riêng ngành nha, áp bất kể điểm: đã đặt lịch/đang đến "
     "→ HOT · ĐÃ CÓ PHIM X-QUANG hoặc đã khám nơi khác có phác đồ → HOT · "
     "đang đau cấp → tối thiểu WARM.", "Cột Ghi đè?"),
    ("% HOT*", "Chấm lại CHỈ bằng 4 tín hiệu ②③④⑤, đạt ≥3/4 tính HOT*. "
     "Dùng khi bảng chia nhóm theo vấn đề răng — vì tín hiệu ① chính là "
     "'nêu vấn đề cụ thể' nên cột % HOT bị LẶP VÒNG, không so sánh được.",
     "Bảng nhiệt theo vấn đề răng"),
    ("V1 / V2 / V3", "Nhóm giá trị dịch vụ. V1 lớn: Implant · All-On · "
     "Invisalign · sứ toàn hàm. V2 trung: sứ lẻ · Veneer · mắc cài. "
     "V3 nhỏ/cửa vào: cạo vôi · tẩy trắng · trám · nhổ · trẻ em. "
     "MỘT LEAD WARM CỦA IMPLANT ĐÁNG HƠN MỘT LEAD HOT CỦA CẠO VÔI.",
     "Cột Nhóm giá trị"),
    ("V-01 … V-11", "11 nhóm vấn đề răng, xét ưu tiên từ trên xuống: "
     "V-01 làm lại ca lỗi · V-02 mất nhiều răng/cả hàm · V-03 mất răng lẻ · "
     "V-04 lệch-khấp khểnh-thưa-hô · V-05 xỉn-vỡ-sứt-mòn · V-06 đau-viêm tủy · "
     "V-07 viêm nướu-vôi răng · V-08 răng khôn-nhổ · V-09 tẩy trắng · "
     "V-10 trẻ em · V-11 chưa rõ.", "Cột Vấn đề răng"),
    ("L1.1 … L6.7", "Trạng thái vận hành. L1.1 lần đầu nhắn · L2.1 đang tư vấn · "
     "L2.3 chưa phản hồi · L2.4 hẹn nhắn lại · L2.5 ngoài 7 tỉnh có cơ sở · "
     "L4.1 có SĐT + rõ dịch vụ · L5.3 gọi không bắt máy · L5.4 từ chối nghe · "
     "L5.5 hẹn gọi lại · L5.6 chỉ Zalo · L6.1 chưa rõ rào cản · L6.2 so sánh · "
     "L6.3 tài chính · L6.4 thời gian · L6.5 sợ đau/sợ mài răng · "
     "L6.6 hỏi người nhà · L6.7 NGỜ VẬT LIỆU (riêng ngành nha).", "Cột L-code"),
    ("SỢ / NGỜ / NGẠI", "Ba rào cản ngành nha. SỢ → L6.5 · "
     "NGỜ → L6.2, L6.7 · NGẠI → L6.3, L6.4, L2.5. "
     "Một hội thoại có thể mang nhiều rào cản nên tổng rào cản LỚN HƠN "
     "tổng hội thoại là đúng.", "Cột Rào cản"),
    ("S1 / S2 / S3 / CS", "Giai đoạn hành trình. S1 nhận biết · S2 tìm hiểu · "
     "S3 cân nhắc & nỗi sợ (★ điểm quyết định) · CS hậu điều trị & gắn bó.",
     "Cột Giai đoạn"),
    ("B1 → B5", "Khung 5 bước tư vấn: B1 mở · B2 khám phá (4 thông tin) · "
     "B3 tạo tin cậy · B4 xin số có lý do · B5 xác nhận ai gọi/số nào/mấy giờ.",
     "Sheet Khung 5 bước"),
    ("T+0 → T+7", "Nhịp chăm sau khi XIN ĐƯỢC SỐ. Trần 6 lần nhắn/7 ngày.",
     "Sheet Nhịp chăm sóc"),
    ("D+3 / D+7 / D+15", "Nhịp chăm khi ĐÃ TƯ VẤN mà chưa đặt lịch khám (L6.x). "
     "Với L6.x·V1 thì nuôi tới 90 ngày, không hạ tệp ở 30 ngày.",
     "Sheet Nhịp chăm sóc"),
    ("⚠ chưa đủ mẫu", "Nhóm/post dưới 10 hội thoại. KHÔNG xếp hạng, "
     "KHÔNG khuyến nghị. Dòng này nền xám.", "Cột Đủ mẫu?"),
    ("[ … ]", "Chỗ trực page tự điền theo tình huống.", "Cột nội dung"),
    ("{ … }", "Biến lấy từ chương trình tháng (P7 bản hiện hành). Luôn kèm ⚠.",
     "Cột nội dung"),
    ("·", "Dấu phân tách nhiều mã. Ví dụ V-03 · L6.7 · WARM · V1.", "Mọi sheet"),
    ("→", "Bước kế tiếp.", "Mọi sheet"),
    ("Màu", "Đỏ nhạt HOT · cam WARM · xanh dương nhạt COLD · vàng mọi ô ⚠ · "
     "xanh lá nhạt khuyến nghị tốt · xám dòng chưa đủ mẫu. "
     "Màu trong bảng nhiệt CHỈ so sánh được trong cùng một bảng.", "Mọi sheet"),
]


def sheet_chu_giai(wb, them=None):
    """Sheet 'Chu giai ky hieu' — bat buoc co o moi file Excel.

    `them` = danh sach (ky_hieu, nghia, dung_o_dau) rieng cua bao cao do.
    """
    ws = sheet(wb, "Chú giải ký hiệu")
    tieu_de(ws, "CHÚ GIẢI KÝ HIỆU",
            "Giải nghĩa mọi ký hiệu dùng trong file. Đọc sheet này trước "
            "khi đọc số.")
    dong_tieu_de(ws, ["Ký hiệu", "Nghĩa là gì", "Dùng ở đâu"])
    for kh, ng, do in list(CHU_GIAI_CHUNG) + list(them or []):
        dong(ws, [kh, ng, do])
    return hoan_thien(ws)
