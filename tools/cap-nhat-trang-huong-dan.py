#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Bơm lại nội dung repo vào trang hướng dẫn (artifact HTML).

Trang hướng dẫn nhúng sẵn bốn khối để người dùng bấm Copy mà không cần tải repo:

    #src-full    bộ não đầy đủ      <- SYSTEM-PROMPT.md       (khối giữa ▼▲)
    #src-short   bộ não ngắn        <- SYSTEM-PROMPT-NGAN.md  (khối giữa ▼▲)
    #src-gop-k   tri thức P1-P8 gộp <- knowledge/P*.md
    #src-gop-r   khuôn báo cáo gộp  <- reports/R*.md

Sửa repo xong mà quên bơm lại thì trang dạy người dùng bản cũ — đã xảy ra: trang
còn ghi "Năm báo cáo R1-R5" sau khi repo đã có R6. Chạy:

    python tools/cap-nhat-trang-huong-dan.py <duong-dan-trang.html>

Script chỉ thay phần BÊN TRONG bốn thẻ <pre> đó cộng mấy nhãn cỡ file đi kèm.
Phần chữ còn lại của trang sửa tay.
"""
from __future__ import annotations

import io
import os
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def doc(path: str) -> str:
    return io.open(os.path.join(REPO, path), encoding="utf-8").read()


def esc(s: str) -> str:
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def khoi_copy(path: str) -> str:
    """Cắt phần giữa hai vạch ▼▲, bỏ rào ``` bọc ngoài."""
    s = doc(path)
    i = s.index("▼▼▼")
    i = s.index("\n", i) + 1
    j = s.index("▲▲▲", i)
    s = s[i:j].strip()
    if s.startswith("```"):
        s = s[s.index("\n") + 1:]
    if s.rstrip().endswith("```"):
        s = s.rstrip()[:-3]
    s = s.strip()
    assert s.startswith("#"), f"{path}: khối copy không bắt đầu bằng tiêu đề"
    return s


def gop(thu_muc: str, tien_to: str, tieu_de: str, mo_ta: str) -> tuple[str, int]:
    """Nối các file trong một thư mục, mỗi file có dòng ===== tên file ====="""
    ten = sorted(f for f in os.listdir(os.path.join(REPO, thu_muc))
                 if f.startswith(tien_to) and f.endswith(".md"))
    phan = [tieu_de, mo_ta.format(n=len(ten)), ""]
    for f in ten:
        phan.append("")
        phan.append(f"===== {f} =====")
        phan.append("")
        phan.append(doc(os.path.join(thu_muc, f)).strip())
    return "\n".join(phan) + "\n", len(ten)


def thay_pre(html: str, pre_id: str, noi_dung: str) -> str:
    """Thay phần bên trong <pre ... id="<pre_id>"> … </pre>."""
    mo = re.search(r'<pre class="filebody" id="%s">' % re.escape(pre_id), html)
    if not mo:
        raise SystemExit(f"Không thấy khối #{pre_id} trong trang")
    dau = mo.end()
    cuoi = html.index("</pre>", dau)
    return html[:dau] + esc(noi_dung) + html[cuoi:]


def thay_nhan(html: str, neo: str, cu_regex: str, moi: str) -> str:
    """Đổi nhãn cỡ file nằm gần một mỏ neo (tên thẻ file)."""
    i = html.index(neo)
    doan = html[i:i + 700]
    moi_doan, n = re.subn(cu_regex, moi, doan, count=1)
    if not n:
        print(f"  ! không đổi được nhãn gần: {neo[:40]}")
        return html
    return html[:i] + moi_doan + html[i + 700:]


def main(argv):
    if len(argv) < 2:
        raise SystemExit(__doc__)
    trang = argv[1]
    html = io.open(trang, encoding="utf-8").read()
    goc = len(html)

    full = khoi_copy("SYSTEM-PROMPT.md")
    short = khoi_copy("SYSTEM-PROMPT-NGAN.md")
    tri_thuc, n_p = gop("knowledge", "P", "# TRI THỨC P1–P8 — Paris Agent Factory",
                        "File này gộp {n} module tri thức. Mỗi phần bắt đầu bằng dòng\n"
                        "===== tên file ===== để trợ lý biết đang đọc module nào.")
    bao_cao, n_r = gop("reports", "R", "# KHUÔN BÁO CÁO R1–R%d — Paris Agent Factory" % 0,
                       "File này gộp {n} khuôn báo cáo. Mỗi phần bắt đầu bằng dòng\n"
                       "===== tên file ===== để trợ lý biết đang đọc khuôn nào.\n"
                       "Đọc khuôn trước khi làm, không tự nghĩ ra cấu trúc mới.")
    bao_cao = bao_cao.replace("R1–R0", "R1–R%d" % n_r, 1)

    html = thay_pre(html, "src-full", full)
    html = thay_pre(html, "src-short", short)
    html = thay_pre(html, "src-gop-k", tri_thuc)
    html = thay_pre(html, "src-gop-r", bao_cao)

    def kb(s): return "%.1f KB" % (len(s.encode("utf-8")) / 1024)
    def kt(n): return "{:,}".format(n).replace(",", ".") + " ký tự"

    html = thay_nhan(html, "Ô Instructions — bản đầy đủ", r"[\d.]+ ký tự", kt(len(full)))
    html = thay_nhan(html, "Ô Instructions — bản ngắn", r"[\d.]+ ký tự", kt(len(short)))
    html = thay_nhan(html, "Ô Instructions — bản ngắn", r"dư <b>[\d.]+ ký tự</b>",
                     "dư <b>%d ký tự</b>" % (8000 - len(short)))
    html = thay_nhan(html, "Tri thức P1–P8 (gộp sẵn)", r"[\d.]+ KB", kb(tri_thuc))
    html = thay_nhan(html, "Khuôn báo cáo R1–R", r"[\d.]+ KB", kb(bao_cao))

    io.open(trang, "w", encoding="utf-8").write(html)
    print(f"Đã bơm lại 4 khối vào {trang}")
    print(f"  bộ não đầy đủ : {kt(len(full))}")
    print(f"  bộ não ngắn   : {kt(len(short))}  (dư {8000 - len(short)} so với giới hạn 8.000)")
    print(f"  tri thức      : {n_p} module · {kb(tri_thuc)}")
    print(f"  khuôn báo cáo : {n_r} khuôn · {kb(bao_cao)}")
    print(f"  trang         : {goc / 1024:.0f} KB -> {len(html) / 1024:.0f} KB")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
