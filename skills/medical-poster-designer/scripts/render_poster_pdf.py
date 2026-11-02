#!/usr/bin/env python3
"""
render_poster_pdf.py — Kết xuất HTML Poster (120x90 cm) hoặc Tờ rơi A4 (210x297 mm)
sang file PDF vector chuẩn in ấn bằng Chromium/Edge headless, đồng thời hỗ trợ
xuất ảnh PNG preview qua pypdfium2 để kiểm tra thị giác (read_file).
"""

import argparse
import os
import pathlib
import subprocess
import sys
import tempfile


def find_headless_browser() -> str:
    """Tìm binary trình duyệt headless ổn định nhất trên Windows (ưu tiên chrome-headless-shell)."""
    local_app_data = os.environ.get("LOCALAPPDATA", "")
    candidates = []

    pw_root = pathlib.Path(local_app_data) / "ms-playwright"
    if pw_root.exists():
        for shell_exe in sorted(pw_root.glob("chromium_headless_shell-*/chrome-headless-shell-win64/chrome-headless-shell.exe"), reverse=True):
            candidates.append(str(shell_exe))
        for chrome_exe in sorted(pw_root.glob("chromium-*/chrome-win/chrome.exe"), reverse=True):
            candidates.append(str(chrome_exe))

    candidates.extend([
        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
        r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
    ])

    for path in candidates:
        if os.path.isfile(path):
            return path

    raise FileNotFoundError("Không tìm thấy chrome-headless-shell.exe, chrome.exe hoặc msedge.exe trên hệ thống.")


def render_html_to_pdf(input_html: pathlib.Path, output_pdf: pathlib.Path) -> None:
    browser_exe = find_headless_browser()
    file_uri = input_html.resolve().as_uri()
    output_pdf.parent.mkdir(parents=True, exist_ok=True)

    with tempfile.TemporaryDirectory(prefix="vn_med_poster_") as tmp_profile:
        cmd = [
            browser_exe,
            "--headless=new" if "chrome-headless-shell" not in browser_exe else "--headless",
            "--no-sandbox",
            "--disable-gpu",
            "--no-pdf-header-footer",
            f"--user-data-dir={tmp_profile}",
            f"--print-to-pdf={str(output_pdf.resolve())}",
            file_uri,
        ]
        res = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
        if not output_pdf.exists() or output_pdf.stat().st_size == 0:
            sys.stderr.write(f"Lỗi khi kết xuất PDF:\nSTDOUT: {res.stdout}\nSTDERR: {res.stderr}\n")
            sys.exit(1)


def render_pdf_to_png(pdf_path: pathlib.Path, preview_path: pathlib.Path, scale: float = 0.5) -> None:
    import pypdfium2 as pdfium
    doc = pdfium.PdfDocument(str(pdf_path))
    preview_path.parent.mkdir(parents=True, exist_ok=True)
    if len(doc) == 1:
        img = doc[0].render(scale=scale).to_pil()
        img.save(str(preview_path))
        print(f"Preview PNG written to: {preview_path.resolve()} ({img.size})")
    else:
        for idx in range(len(doc)):
            stem = preview_path.stem
            page_png = preview_path.with_name(f"{stem}_page{idx + 1}.png")
            img = doc[idx].render(scale=scale).to_pil()
            img.save(str(page_png))
            if idx == 0:
                img.save(str(preview_path))
            print(f"Preview Page {idx + 1} PNG written to: {page_png.resolve()} ({img.size})")


def main() -> None:
    parser = argparse.ArgumentParser(description="Kết xuất HTML Poster / Tờ rơi A4 sang PDF chuẩn in ấn và PNG preview.")
    parser.add_argument("--input", required=True, help="Đường dẫn file HTML đầu vào.")
    parser.add_argument("--output", required=True, help="Đường dẫn file PDF đầu ra.")
    parser.add_argument("--preview", required=False, help="Đường dẫn file PNG xem trước (tùy chọn).")
    parser.add_argument("--scale", type=float, default=0.5, help="Tỷ lệ xuất ảnh PNG từ PDF (mặc định: 0.5).")
    args = parser.parse_args()

    in_path = pathlib.Path(args.input)
    out_path = pathlib.Path(args.output)

    if not in_path.exists():
        sys.stderr.write(f"Không tìm thấy file HTML đầu vào: {in_path}\n")
        sys.exit(1)

    render_html_to_pdf(in_path, out_path)
    print(f"Success! PDF written to: {out_path.resolve()} ({out_path.stat().st_size} bytes)")

    if args.preview:
        render_pdf_to_png(out_path, pathlib.Path(args.preview), scale=args.scale)


if __name__ == "__main__":
    main()
