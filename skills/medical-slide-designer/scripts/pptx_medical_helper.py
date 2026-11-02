# -*- coding: utf-8 -*-
"""
Thư viện hỗ trợ thiết kế mới và chỉnh sửa phẫu thuật (Surgical Editing) Slide PowerPoint (.pptx)
theo chuẩn BVT Medical Infographic Style & Kinh nghiệm Thiết kế Bài giảng Đột quỵ.
"""
import copy
import re
import shutil
import requests
from lxml import etree
from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import MSO_ANCHOR, PP_ALIGN
from pptx.util import Inches, Pt

# ==============================================================================
# 1. HỆ THỐNG BẢNG MÀU & CỠ CHỮ CHUẨN (BVT MEDICAL INFOGRAPHIC PALETTE)
# ==============================================================================
MIN_FONT_PT = 18.0
FONT_FAMILY = "Calibri"

C_WHITE = RGBColor(255, 255, 255)
C_DARK = RGBColor(31, 30, 30)       # #1F1E1E — Tiêu đề slide
C_NAVY = RGBColor(14, 40, 65)       # #0E2841 — Chữ chính & Nhồi máu não
C_TEAL = RGBColor(21, 96, 130)      # #156082 — Chẩn đoán & Đích sinh học
C_DK_TEAL = RGBColor(11, 110, 158)  # #0B6E9E — Nhấn phụ
C_ORANGE = RGBColor(233, 113, 50)   # #E97132 — Thanh nhấn & Chảy máu não
C_DK_ORANGE = RGBColor(197, 90, 17) # #C55A11 — Cảnh báo / Hành động cơ sở
C_GREEN = RGBColor(25, 107, 36)     # #196B24 — Phục hồi chức năng / Nên làm
C_RED = RGBColor(192, 0, 0)         # #C00000 — Chống chỉ định / Cấp cứu
C_DK_BROWN = RGBColor(131, 60, 12)  # #833C0C — Chữ trên nền cam nhạt
C_GRAY_BDR = RGBColor(210, 220, 228)

BG_ICE = RGBColor(241, 245, 248)       # #F1F5F8
BG_PEACH = RGBColor(251, 237, 227)     # #FBEDE3
BG_SOFT_TEAL = RGBColor(234, 241, 245) # #EAF1F5
BG_LT_GREEN = RGBColor(214, 235, 211)  # #D6EBD3
BG_LT_RED = RGBColor(250, 229, 229)    # #FAE5E5

ACCENT_CYCLE = [C_TEAL, C_NAVY, C_DK_ORANGE, C_DK_TEAL, C_GREEN, C_RED]


# ==============================================================================
# 2. CÁC HÀM DỰNG THÀNH PHẦN GIAO DIỆN TRÊN SLIDE (UI COMPONENTS)
# ==============================================================================
def enforce_min_font(font_size_pt, allow_specialist_table=False):
    if allow_specialist_table:
        return max(float(font_size_pt), 11.5)
    return max(float(font_size_pt), MIN_FONT_PT)


def add_card(slide, left, top, width, height, bg_color=BG_ICE, border_color=None, rounded=True):
    shape_type = MSO_SHAPE.ROUNDED_RECTANGLE if rounded else MSO_SHAPE.RECTANGLE
    sh = slide.shapes.add_shape(
        shape_type, Inches(left), Inches(top), Inches(width), Inches(height)
    )
    sh.fill.solid()
    sh.fill.fore_color.rgb = bg_color
    if border_color:
        sh.line.color.rgb = border_color
        sh.line.width = Pt(1.5)
    else:
        sh.line.color.rgb = C_GRAY_BDR
        sh.line.width = Pt(0.75)
    if rounded and sh.adjustments:
        sh.adjustments[0] = 0.04
    return sh


def add_header_badge(slide, left, top, width, height, text, bg_color=C_TEAL, font_size=18, align=PP_ALIGN.CENTER):
    font_size = enforce_min_font(font_size)
    sh = slide.shapes.add_shape(
        MSO_SHAPE.ROUNDED_RECTANGLE, Inches(left), Inches(top), Inches(width), Inches(height)
    )
    sh.fill.solid()
    sh.fill.fore_color.rgb = bg_color
    sh.line.fill.background()
    if sh.adjustments:
        sh.adjustments[0] = 0.12
    tf = sh.text_frame
    tf.word_wrap = True
    tf.vertical_anchor = MSO_ANCHOR.MIDDLE
    p = tf.paragraphs[0]
    p.alignment = align
    r = p.add_run()
    r.text = text
    r.font.name = FONT_FAMILY
    r.font.size = Pt(font_size)
    r.font.bold = True
    r.font.color.rgb = C_WHITE
    return sh


def add_circle_number(slide, left, top, diameter, text, bg_color=C_TEAL, font_size=20):
    font_size = enforce_min_font(font_size)
    sh = slide.shapes.add_shape(
        MSO_SHAPE.OVAL, Inches(left), Inches(top), Inches(diameter), Inches(diameter)
    )
    sh.fill.solid()
    sh.fill.fore_color.rgb = bg_color
    sh.line.fill.background()
    tf = sh.text_frame
    tf.vertical_anchor = MSO_ANCHOR.MIDDLE
    p = tf.paragraphs[0]
    p.alignment = PP_ALIGN.CENTER
    r = p.add_run()
    r.text = str(text)
    r.font.name = FONT_FAMILY
    r.font.size = Pt(font_size)
    r.font.bold = True
    r.font.color.rgb = C_WHITE
    return sh


def add_rich_bullets(slide, left, top, width, height, items, font_size=18, color=C_NAVY, space_after=8):
    """
    items: list of tuples (bold_prefix, normal_text) hoặc list of strings.
    """
    font_size = enforce_min_font(font_size)
    tb = slide.shapes.add_textbox(Inches(left), Inches(top), Inches(width), Inches(height))
    tf = tb.text_frame
    tf.word_wrap = True
    for idx, item in enumerate(items):
        p = tf.paragraphs[0] if idx == 0 else tf.add_paragraph()
        p.space_after = Pt(space_after)
        if isinstance(item, tuple):
            b_pref, n_txt = item
            if b_pref:
                rb = p.add_run()
                rb.text = b_pref + (" " if not b_pref.endswith(" ") and n_txt else "")
                rb.font.name = FONT_FAMILY
                rb.font.size = Pt(font_size)
                rb.font.bold = True
                rb.font.color.rgb = color
            if n_txt:
                rn = p.add_run()
                rn.text = n_txt
                rn.font.name = FONT_FAMILY
                rn.font.size = Pt(font_size)
                rn.font.bold = False
                rn.font.color.rgb = color
        else:
            r = p.add_run()
            r.text = str(item)
            r.font.name = FONT_FAMILY
            r.font.size = Pt(font_size)
            r.font.color.rgb = color
    return tb


def set_notes(slide, notes_text, source_text=None):
    full_notes = notes_text.strip()
    if source_text:
        full_notes += f"\n\n[Nguồn tham khảo]: {source_text.strip()}"
    notes_slide = slide.notes_slide
    tf = notes_slide.notes_text_frame
    tf.text = full_notes


# ==============================================================================
# 3. CÁC HÀM CHỈNH SỬA PHẪU THUẬT (.PPTX SURGICAL IN-PLACE EDITING)
# ==============================================================================
def backup_pptx(pptx_path, suffix=".backup_truoc_cap_nhat.pptx"):
    backup_path = pptx_path.replace(".pptx", suffix)
    shutil.copy2(pptx_path, backup_path)
    return backup_path


def iter_slide_paragraphs(slide, include_notes=False):
    if include_notes:
        if slide.has_notes_slide:
            yield from slide.notes_slide.notes_text_frame.paragraphs
        return
    for sh in slide.shapes:
        if sh.has_text_frame:
            yield from sh.text_frame.paragraphs
        if sh.has_table:
            for row in sh.table.rows:
                for cell in row.cells:
                    yield from cell.text_frame.paragraphs


def rep_para(paragraph, old_text, new_text):
    """Thay thế văn bản trong paragraph mà bảo toàn định dạng font/color của run đầu tiên."""
    for r in paragraph.runs:
        if old_text in r.text:
            r.text = r.text.replace(old_text, new_text)
            return True
    full = "".join(r.text for r in paragraph.runs)
    if old_text in full and paragraph.runs:
        paragraph.runs[0].text = full.replace(old_text, new_text)
        for r in paragraph.runs[1:]:
            r.text = ""
        return True
    return False


def surgical_replace(prs, slide_number_1based, old_text, new_text, in_notes=False):
    slide = prs.slides[slide_number_1based - 1]
    count = 0
    for p in iter_slide_paragraphs(slide, include_notes=in_notes):
        while rep_para(p, old_text, new_text):
            count += 1
            if old_text in new_text:
                break
    return count


def strip_evidence_codes_from_slide_face(prs):
    """
    Loại bỏ các mã (COR 1, 2a, 2b...) khỏi mặt slide dành cho tuyến cơ sở mà không đụng tới Speaker Notes.
    """
    pat = re.compile(r"\s*\((?:[^()]*?— )?COR [^)]*\)")
    removed = 0
    for slide in prs.slides:
        for p in iter_slide_paragraphs(slide, include_notes=False):
            for r in p.runs:
                new_txt = pat.sub("", r.text)
                if new_txt != r.text:
                    r.text = new_txt
                    removed += 1
    return removed


def set_clean_box(shape, left_in, top_in, width_in, height_in, lines, pt_size=18.0, font_name="Arial"):
    """
    Điền văn bản vào shape có sẵn trong template và xóa sạch <a:lstStyle> / gắn <a:buNone/>
    để ngăn lỗi tự động chèn 2 dấu chấm đầu dòng (double-bullets).
    """
    shape.left = Inches(left_in)
    shape.top = Inches(top_in)
    shape.width = Inches(width_in)
    shape.height = Inches(height_in)
    tf = shape.text_frame
    tf.clear()
    tf.word_wrap = True
    lstStyle = tf._txBody.find("{http://schemas.openxmlformats.org/drawingml/2006/main}lstStyle")
    if lstStyle is not None:
        for child in list(lstStyle):
            lstStyle.remove(child)
    for idx, (b_txt, n_txt) in enumerate(lines):
        p = tf.paragraphs[0] if idx == 0 else tf.add_paragraph()
        pPr = p._p.get_or_add_pPr()
        for child in list(pPr):
            pPr.remove(child)
        pPr.set("marL", "0")
        pPr.set("indent", "0")
        pPr.set("algn", "l")
        etree.SubElement(pPr, "{http://schemas.openxmlformats.org/drawingml/2006/main}buNone")
        p.space_before = Pt(3)
        p.space_after = Pt(2)
        if b_txt:
            rb = p.add_run()
            rb.text = b_txt
            rb.font.name = font_name
            rb.font.size = Pt(pt_size)
            rb.font.bold = True
        if n_txt:
            rn = p.add_run()
            rn.text = n_txt
            rn.font.name = font_name
            rn.font.size = Pt(pt_size)
            rn.font.bold = False


def move_slide_to_index(prs, old_index_0based, new_index_0based):
    """Di chuyển slide tới đúng vị trí logic trong bộ bài giảng."""
    xml_slides = prs.slides._sldIdLst
    slides = list(xml_slides)
    el = slides[old_index_0based]
    xml_slides.remove(el)
    xml_slides.insert(new_index_0based, el)


def clone_slide_from_existing(prs, source_slide_index_0based, target_index_0based=None):
    """Nhân bản toàn bộ shapes từ một slide mẫu có sẵn trong bài giảng."""
    src_slide = prs.slides[source_slide_index_0based]
    new_slide = prs.slides.add_slide(src_slide.slide_layout)
    for ph in list(new_slide.placeholders):
        ph._element.getparent().remove(ph._element)
    src_tree = src_slide.shapes._spTree
    dst_tree = new_slide.shapes._spTree
    for el in list(src_tree)[2:]:
        dst_tree.append(copy.deepcopy(el))
    if target_index_0based is not None:
        move_slide_to_index(prs, len(prs.slides) - 1, target_index_0based)
    return new_slide


# ==============================================================================
# 4. TÌM KIẾM HÌNH ẢNH Y KHOA HỢP LỆ TRÊN WIKIMEDIA COMMONS
# ==============================================================================
def search_wikimedia_commons(query, min_width=1200, limit=15):
    """Tìm ảnh bitmap độ phân giải cao có giấy phép mở trên Wikimedia Commons."""
    headers = {"User-Agent": "VNMedicalStudio/1.0 (educational medical slides)"}
    resp = requests.get(
        "https://commons.wikimedia.org/w/api.php",
        headers=headers,
        params={
            "action": "query",
            "format": "json",
            "generator": "search",
            "gsrsearch": f"{query} filetype:bitmap",
            "gsrnamespace": 6,
            "gsrlimit": limit,
            "prop": "imageinfo",
            "iiprop": "url|size|extmetadata|mime",
            "iiextmetadatafilter": "LicenseShortName|Artist|ImageDescription",
        },
        timeout=30,
    )
    results = []
    for page in resp.json().get("query", {}).get("pages", {}).values():
        ii = page["imageinfo"][0]
        if ii.get("width", 0) < min_width:
            continue
        md = ii.get("extmetadata", {})
        lic = md.get("LicenseShortName", {}).get("value", "?")
        artist = re.sub(r"<[^>]+>", "", md.get("Artist", {}).get("value", "?"))[:60]
        results.append({
            "title": page["title"],
            "width": ii["width"],
            "height": ii["height"],
            "license": lic,
            "artist": artist,
            "url": ii["url"],
        })
    return results
