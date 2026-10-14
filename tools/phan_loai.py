# -*- coding: utf-8 -*-
"""Doc file hoi thoai -> phan loai -> rows.json + bang dem.

Cong cu KIEM TRA DOI CHIEU, khong thay the viec doc hieu cua tro ly.
Script khop tu khoa nen no bat duoc nhung thu hien ro trong chu; nhung sac thai
("de em tinh da" la ngai tien hay ngai thoi gian) thi chi nguoi hoac AI doc duoc.

Dung de: dem lai con so o DUNG 1 va DUNG 2, xem tro ly co dem lech khong.

Cach dung:
    python phan_loai.py --src <file hoi thoai .md> [--out rows.json] [--tu-dien <file .json>]

Vi du:
    python phan_loai.py --src ../doc/mau-du-lieu/MAU_Hoi-thoai.md
"""
import argparse
import collections
import io
import json
import os
import re
import sys

VN = ("àáảãạăắằẳẵặâấầẩẫậèéẻẽẹêếềểễệìíỉĩịòóỏõọôốồổỗộơớờởỡợ"
      "ùúủũụưứừửữựỳýỷỹỵđ")
_PAT = {}


def has(text, kw):
    """So khop co bien tu, de 'gia' khong khop trong 'gia dinh'.

    Giu nguyen dau tieng Viet: bo dau roi so khop chuoi con la sai, vi
    'khong' se chua 'hong'.
    """
    pat = _PAT.get(kw)
    if pat is None:
        pat = _PAT[kw] = re.compile(
            r"(?<![\w" + VN + r"])" + re.escape(kw) + r"(?![\w" + VN + r"])")
    return bool(pat.search(text))


def has_any(text, kws):
    return any(has(text, k) for k in kws)


# ---------------------------------------------------------------- tach file

RE_HEAD = re.compile(r"^##\s+(\d+)\.\s*(.+?)\s+—\s+(.+?)\s*$")
RE_META = re.compile(r"Phụ trách:\s*(.*?)\s*·\s*Có SĐT:\s*(\S+)\s*·\s*Số tin:\s*(\d+)")
RE_TIN = re.compile(r"^-\s+\*\*(.+?)\s+(KH|NV)(?:\s*\((.*?)\))?:\*\*\s*(.*)$")
RE_THE = re.compile(r"\[Thẻ:\s*(.*?)\]")
RE_QC = re.compile(r"Inbox từ quảng cáo\s+(.+?)\s*[–-]")


def tach(path):
    """Tach file markdown thanh danh sach hoi thoai."""
    raw = io.open(path, encoding="utf-8").read().splitlines()
    hts, cur = [], None
    for line in raw:
        m = RE_HEAD.match(line)
        if m:
            if cur:
                hts.append(cur)
            cur = {"stt": int(m.group(1)), "ten": m.group(2).strip(),
                   "ngay": m.group(3).strip(), "nv": "", "co_sdt": "",
                   "so_tin": 0, "the": "", "post": "", "kh": [], "nvtin": []}
            continue
        if cur is None:
            continue
        mm = RE_META.search(line)
        if mm:
            cur["nv"] = mm.group(1).strip()
            cur["co_sdt"] = mm.group(2).strip()
            cur["so_tin"] = int(mm.group(3))
            continue
        mt = RE_TIN.match(line)
        if mt:
            noi_dung = mt.group(4)
            mthe = RE_THE.search(noi_dung)
            if mthe and not cur["the"]:
                cur["the"] = mthe.group(1).strip()
                mqc = RE_QC.search(cur["the"])
                cur["post"] = mqc.group(1).strip() if mqc else ""
            # Bo phan [The: ...] khoi chu khach: do la tin tu dong, va headline
            # quang cao trong the se lam lech phan loai (vd the "khong ai biet
            # ban dang nieng" bi doc thanh khach dang nieng -> giai doan CS).
            noi_dung = RE_THE.sub(" ", noi_dung).strip()
            if not noi_dung:
                continue
            if mt.group(2) == "KH":
                cur["kh"].append(noi_dung)
            else:
                cur["nvtin"].append(noi_dung)
    if cur:
        hts.append(cur)
    return hts


# ------------------------------------------------------------- phan loai

def van_de(text, td):
    """Xet 11 nhom van de rang theo thu tu uu tien."""
    for ma, ten, kws in td["van_de"]:
        if kws and has_any(text, kws):
            return ma, ten
    return "V-11", "Chưa rõ / hỏi chung"


def nhom_gia_tri(ma_vd, text, td):
    g = td["gia_tri"]
    if ma_vd in g["V1"]:
        return "V1"
    if ma_vd == "V-04":
        return "V1" if has_any(text, g["v04_v1"]) else "V2"
    if ma_vd == "V-01":
        return "V1" if has_any(text, g["v01_v1"]) else "V2"
    if ma_vd in g["V2"]:
        return "V2"
    if ma_vd in g["V3"]:
        return "V3"
    return "?"


def cham(ht, ma_vd, text_kh, td):
    """Cham 5 tin hieu + 3 luat ghi de. Tra ve (bitmask, do_nong, ghi_de)."""
    th = td["tin_hieu"]
    s1 = ma_vd != "V-11"
    s2 = has_any(text_kh, th["th2_thoi_gian"])
    s4 = has_any(text_kh, th["th4_mo_ta_ro"]) or "[ảnh]" in text_kh
    # (3) chi tinh khi hoi cu the VA da co mo ta tinh trang, hoac da trao doi
    #     tu 3 tin tro len -> tranh dem cau "bao nhieu tien" o tin dau.
    s3 = has_any(text_kh, th["th3_hoi_cu_the"]) and (s4 or len(ht["kh"]) >= 3)
    s5 = ht["co_sdt"].lower().startswith("c")

    bits = [s1, s2, s3, s4, s5]
    diem = sum(1 for b in bits if b)
    bitmask = "".join("1" if b else "0" for b in bits)

    gd = td["ghi_de"]
    ghi_de = ""
    if has_any(text_kh, gd["da_dat_lich"]):
        ghi_de = "đã đặt lịch"
    elif has_any(text_kh, gd["da_co_phim"]):
        ghi_de = "đã có phim / đã khám nơi khác"
    elif ma_vd == "V-06":
        ghi_de = "đau cấp"

    if ghi_de in ("đã đặt lịch", "đã có phim / đã khám nơi khác"):
        nong = "HOT"
    elif ghi_de == "đau cấp":
        nong = "HOT" if diem >= 4 else "WARM"
    else:
        nong = "HOT" if diem >= 4 else ("WARM" if diem >= 2 else "COLD")

    # diem4: cham lai khong ke tin hieu (1) -> chong lap vong (P8 §2)
    diem4 = sum(1 for b in bits[1:] if b)
    nong4 = "HOT*" if diem4 >= 3 else ("WARM*" if diem4 >= 1 else "COLD*")
    return bitmask, diem, nong, ghi_de, diem4, nong4


def rao_can(text_kh, td):
    out = []
    for ma, d in td["rao_can"].items():
        if ma.startswith("_"):
            continue
        if has_any(text_kh, d["kw"]):
            out.append((ma, d["nhom"], d["ten"]))
    return out


def l_code(ht, nong, rcs, text_kh, td):
    """Suy ma L. Day la DE XUAT, nguoi/AI doc lai van la nguon chot."""
    co_sdt = ht["co_sdt"].lower().startswith("c")
    if co_sdt:
        return "L4.1"
    # ngoai 7 tinh/thanh co co so
    if has_any(text_kh, ["ở xa", "tỉnh em", "không có cơ sở", "cơ sở gần"]) \
            and not has_any(text_kh, td["tinh_co_co_so"]):
        return "L2.5"
    if rcs:
        return rcs[0][0]
    if len(ht["kh"]) <= 1:
        return "L1.1"
    return "L2.1"


def giai_doan(ma_vd, rcs, text_kh, td):
    if has_any(text_kh, ["đang niềng", "đã trồng", "tái khám", "sau khi làm",
                         "chăm sóc sau", "siết niềng"]):
        return "CS"
    if rcs:
        return "S3"
    th = td["tin_hieu"]
    if ma_vd != "V-11" and (has_any(text_kh, th["th4_mo_ta_ro"])
                            or "[ảnh]" in text_kh):
        return "S2"
    return "S1"


# ----------------------------------------------------------------- main

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--src", required=True, help="file hoi thoai .md")
    ap.add_argument("--out", default="rows.json")
    ap.add_argument("--tu-dien", default=None)
    a = ap.parse_args()

    td_path = a.tu_dien or os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "tu-dien-van-de-rang.json")
    td = json.load(io.open(td_path, encoding="utf-8"))

    hts = tach(a.src)
    if not hts:
        sys.stderr.write("Khong tach duoc hoi thoai nao. Kiem dinh dang file.\n")
        return 1

    rows = []
    for ht in hts:
        text_kh = "\n".join(ht["kh"]).lower()
        text_nv = "\n".join(ht["nvtin"]).lower()
        ma_vd, ten_vd = van_de(text_kh, td)
        gt = nhom_gia_tri(ma_vd, text_kh, td)
        bitmask, diem, nong, ghi_de, diem4, nong4 = cham(ht, ma_vd, text_kh, td)
        rcs = rao_can(text_kh, td)
        rows.append({
            "stt": ht["stt"], "ten": ht["ten"], "ngay": ht["ngay"],
            "nv": ht["nv"], "so_tin": ht["so_tin"], "co_sdt": ht["co_sdt"],
            "the": ht["the"], "post": ht["post"] or ("(thẻ không phải QC)"
                                                     if ht["the"] else "(không rõ nguồn)"),
            "van_de": ma_vd, "ten_van_de": ten_vd, "nhom_gia_tri": gt,
            "bitmask": bitmask, "diem": diem, "do_nong": nong, "ghi_de": ghi_de,
            "diem4": diem4, "nong4": nong4,
            "rao_can": [{"ma": m, "nhom": n, "ten": t} for m, n, t in rcs],
            "l_code": l_code(ht, nong, rcs, text_kh, td),
            "giai_doan": giai_doan(ma_vd, rcs, text_kh, td),
            "tu_cam_nv": [k for k in td["tu_cam"] if has(text_nv, k)],
            "hang_nv": [k for k in td["hang_duoc_duyet"] if has(text_nv, k)],
            "dau_hieu_gia_dinh": has_any(text_kh, td["dau_hieu_gia_dinh"]),
        })

    io.open(a.out, "w", encoding="utf-8").write(
        json.dumps(rows, ensure_ascii=False, indent=1))

    # ------------------------------------------------- bang dem
    n = len(rows)
    out = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

    def p(s=""):
        out.write(s + "\n")

    def dem(key):
        return collections.Counter(r[key] for r in rows)

    co_sdt = sum(1 for r in rows if r["co_sdt"].lower().startswith("c"))
    p("=" * 62)
    p("  DOI CHIEU CON SO  —  %s" % os.path.basename(a.src))
    p("=" * 62)
    p("Tach duoc            %d hoi thoai" % n)
    p("Co SDT               %d  (%.1f%%)" % (co_sdt, 100.0 * co_sdt / n))
    p("Khong co SDT         %d  (%.1f%%)" % (n - co_sdt, 100.0 * (n - co_sdt) / n))
    p("Co the nguon QC      %d" % sum(1 for r in rows if r["post"].startswith("QC")))
    p("The khong phai QC    %d" % sum(1 for r in rows if "không phải QC" in r["post"]))
    p("Khong ro nguon       %d" % sum(1 for r in rows if "không rõ nguồn" in r["post"]))
    p()
    p("-- DO NONG " + "-" * 50)
    for k in ("HOT", "WARM", "COLD"):
        v = dem("do_nong")[k]
        p("  %-6s %3d  (%.1f%%)" % (k, v, 100.0 * v / n))
    gd = [r for r in rows if r["ghi_de"]]
    p("  trong do %d ca do LUAT GHI DE:" % len(gd))
    for k, v in collections.Counter(r["ghi_de"] for r in gd).items():
        p("      %-36s %d" % (k, v))
    p()
    p("-- NHOM GIA TRI " + "-" * 45)
    for k in ("V1", "V2", "V3", "?"):
        v = dem("nhom_gia_tri")[k]
        if v:
            p("  %-3s %3d  (%.1f%%)" % (k, v, 100.0 * v / n))
    p()
    p("-- VAN DE RANG " + "-" * 46)
    for ma, ten, _ in td["van_de"]:
        v = dem("van_de")[ma]
        if v:
            p("  %-6s %-34s %d" % (ma, ten, v))
    p()
    p("-- GIAI DOAN " + "-" * 48)
    for k in ("S1", "S2", "S3", "CS"):
        v = dem("giai_doan")[k]
        if v:
            p("  %-3s %d" % (k, v))
    p()
    p("-- RAO CAN  (mot HT co the mang nhieu -> tong > %d la dung) " % n + "-" * 3)
    c = collections.Counter()
    cn = collections.Counter()
    for r in rows:
        for rc in r["rao_can"]:
            c[(rc["ma"], rc["ten"])] += 1
            cn[rc["nhom"]] += 1
    for (ma, ten), v in sorted(c.items(), key=lambda x: -x[1]):
        p("  %-6s %-34s %d" % (ma, ten, v))
    p("  theo nhom: " + " · ".join("%s %d" % (k, v) for k, v in cn.most_common()))
    p()
    p("-- CO CANH BAO " + "-" * 46)
    tc = [r for r in rows if r["tu_cam_nv"]]
    p("  HT co TU CAM trong loi nhan vien: %d" % len(tc))
    for r in tc:
        p("      HT#%-3d %-16s %s" % (r["stt"], r["nv"], ", ".join(r["tu_cam_nv"])))
    nghi = [r for r in rows
            if any(rc["ma"] == "L6.7" for rc in r["rao_can"]) and not r["hang_nv"]]
    p("  HT khach NGO VAT LIEU (L6.7) ma NV khong nhac doi tac hang: %d"
      % len(nghi))
    for r in nghi:
        p("      HT#%-3d %s" % (r["stt"], r["nv"]))
    gdinh = [r for r in rows if r["dau_hieu_gia_dinh"]]
    p("  HT co dau hieu GIA DINH (tep LTV): %d" % len(gdinh))
    p()
    p("-- POST " + "-" * 53)
    for k, v in collections.Counter(r["post"] for r in rows).most_common():
        cb = "" if v >= 10 else "   <-- chua du mau, khong xep hang"
        p("  %-34s %3d%s" % (k[:34], v, cb))
    p()
    p("Da ghi %s  (%d dong)" % (a.out, n))
    p()
    p("LUU Y: day la ket qua KHOP TU KHOA, dung de doi chieu con so.")
    p("Phan loai chot van la cua nguoi doc / tro ly. Lech thi tin ban doc tay.")
    out.flush()
    return 0


if __name__ == "__main__":
    sys.exit(main())
