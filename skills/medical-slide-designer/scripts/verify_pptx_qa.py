# -*- coding: utf-8 -*-
"""
Công cụ Kiểm định Chất lượng Tự động (QA Audit) & Xuất ảnh PNG Kiểm tra Thị giác cho Slide .pptx
Thực thi:
  python verify_pptx_qa.py <duong_dan_file.pptx> [--export-png <thu_muc_png>] [--slides 1,9,15]
"""
import argparse
import os
import re
import sys
from pptx import Presentation

sys.stdout.reconfigure(encoding="utf-8")

FORBIDDEN_TERMS = [
    (r"xuất huyết não", "Dùng 'chảy máu não' theo chuẩn Bộ Y tế & miền Bắc"),
    (r"\bsau cấp\b", "Dùng 'sau giai đoạn cấp' (không viết tắt là 'sau cấp')"),
    (r"\bdãn\b", "Dùng 'giãn' (giãn não thất, giãn thất), không viết 'dãn'"),
    (r"đè bẹp|ép bẹp|bẹp phổi", "Dùng 'đè dẹt / ép dẹt / xẹp', cấm dùng 'bẹp'"),
    (r"choáng tim", "Dùng 'sốc tim', không dùng 'choáng tim'"),
    (r"vũ khí tối thượng|sát thủ thầm lặng|thần thánh|đột phá vô song", "Cấm dùng từ ngữ AI cường điệu"),
]


def audit_pptx(pptx_path, min_required_pt=18.0):
    prs = Presentation(pptx_path)
    min_pt = 999.0
    min_info = ""
    small_font_slides = []
    missing_notes = []
    term_violations = []

    def check_tf(tf, slide_idx, loc):
        nonlocal min_pt, min_info
        for p in tf.paragraphs:
            txt = p.text
            for pattern, reason in FORBIDDEN_TERMS:
                if re.search(pattern, txt, re.I):
                    term_violations.append((slide_idx, loc, pattern, reason, txt[:70]))
            if loc == "slide":
                for r in p.runs:
                    if r.text.strip() and r.font.size:
                        pt = r.font.size.pt
                        if pt < min_pt:
                            min_pt = pt
                            min_info = f"Slide {slide_idx}: '{r.text.strip()[:35]}' ({pt} pt)"
                        if pt < min_required_pt:
                            small_font_slides.append((slide_idx, pt, r.text.strip()[:35]))

    for i, slide in enumerate(prs.slides, 1):
        for shape in slide.shapes:
            if shape.has_text_frame:
                check_tf(shape.text_frame, i, "slide")
            if shape.has_table:
                for row in shape.table.rows:
                    for cell in row.cells:
                        check_tf(cell.text_frame, i, "slide")
        if slide.has_notes_slide and slide.notes_slide.notes_text_frame.text.strip():
            check_tf(slide.notes_slide.notes_text_frame, i, "notes")
        else:
            missing_notes.append(i)

    print("=" * 72)
    print(f"BÁO CÁO KIỂM ĐỊNH QA SLIDE: {os.path.basename(pptx_path)}")
    print(f"- Tổng số slide: {len(prs.slides)}")
    print(f"- Cỡ chữ nhỏ nhất trên mặt slide: {min_pt:.1f} pt ({min_info})")
    print(f"- Số slide thiếu Speaker Notes: {len(missing_notes)} -> {missing_notes}")
    print(f"- Số lỗi thuật ngữ phát hiện: {len(term_violations)}")
    for v in term_violations:
        print(f"  [!] Slide {v[0]} ({v[1]}): Khớp '{v[2]}' -> {v[3]} | '{v[4]}'")
    if small_font_slides:
        print(f"- Các đoạn chữ nhỏ hơn ngưỡng {min_required_pt} pt ({len(small_font_slides)} vị trí):")
        for s_idx, pt_val, sample in small_font_slides[:10]:
            print(f"  [!] Slide {s_idx}: {pt_val:.1f} pt -> '{sample}'")
    print("=" * 72)
    return {
        "total_slides": len(prs.slides),
        "min_pt": min_pt,
        "missing_notes": missing_notes,
        "term_violations": term_violations,
    }


def export_slides_to_png(pptx_path, out_dir, slide_numbers=None, width=1600, height=900):
    import win32com.client
    os.makedirs(out_dir, exist_ok=True)
    abs_pptx = os.path.abspath(pptx_path)
    ppt = win32com.client.Dispatch("PowerPoint.Application")
    pres = ppt.Presentations.Open(abs_pptx, True, False, False)
    try:
        target_nums = slide_numbers if slide_numbers else list(range(1, pres.Slides.Count + 1))
        for s_num in target_nums:
            out_png = os.path.abspath(os.path.join(out_dir, f"slide_{s_num:02d}.png"))
            pres.Slides(s_num).Export(out_png, "PNG", width, height)
            print(f"Đã kết xuất PNG: {out_png}")
    finally:
        pres.Close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Kiểm định QA & Xuất PNG cho bộ slide y khoa .pptx")
    parser.add_argument("pptx_path", help="Đường dẫn tới file .pptx")
    parser.add_argument("--min-pt", type=float, default=18.0, help="Ngưỡng cỡ chữ tối thiểu (mặc định: 18.0)")
    parser.add_argument("--export-png", help="Thư mục xuất ảnh PNG để kiểm tra trực quan")
    parser.add_argument("--slides", help="Danh sách số thứ tự slide cần xuất PNG (vd: 1,9,15)")
    args = parser.parse_args()

    audit_pptx(args.pptx_path, min_required_pt=args.min_pt)
    if args.export_png:
        s_nums = [int(x.strip()) for x in args.slides.split(",") if x.strip()] if args.slides else None
        export_slides_to_png(args.pptx_path, args.export_png, slide_numbers=s_nums)
