---
name: medical-poster-designer
description: >-
  Thiết kế Poster hội nghị y khoa khổ ngang (120x90 cm, tỷ lệ 4:3 hoặc 16:9) và
  Tờ rơi A4 2 mặt (210x297 mm) chuẩn quốc tế theo hướng dẫn của Davies và cộng
  sự (Clinical Nutrition ESPEN, 2024;63:457–461, DOI: 10.1016/j.clnesp.2024.06.056)
  kết hợp kiến trúc đa giác trung tâm của hội nghị châu Âu (CAS in Brain Health –
  University of Bern, EAN Congress). Kích hoạt kỹ năng này khi người dùng yêu cầu
  thiết kế poster khoa học, poster giới thiệu chương trình đào tạo y khoa, sửa lỗi
  poster chữ nhỏ/rối mắt do các model khác tạo, hoặc chuyển đổi tài liệu dài thành
  bộ Poster khổ ngang + Tờ rơi A4 2 mặt.
---

# Thiết kế poster hội nghị y khoa khổ ngang & tờ rơi A4 2 mặt (Medical Poster & Handout Designer)

## Overview

Kỹ năng này chuẩn hóa toàn bộ quy trình thiết kế **Poster hội nghị y khoa khổ ngang ($120 \times 90\text{ cm}$)** và **Tờ rơi cầm tay A4 2 mặt ($210 \times 297\text{ mm}$)** dựa trên:
1. **Tiêu chuẩn thiết kế poster khoa học quốc tế:** Davies NA, Deutz NE, Delzenne N, Lobo DN. *Presentation and publication skills: How to prepare a scientific poster*. *Clinical Nutrition ESPEN*, 2024;63:457–461 (DOI: `10.1016/j.clnesp.2024.06.056`, PMID: `39003733`).
2. **Kiến trúc thị giác gian hàng hội nghị châu Âu (*CAS in Brain Health* – Đại học Bern tại EAN Congress):** Sử dụng dải đa giác vát chéo trung tâm làm nổi bật tiêu đề chính giữa, các thẻ học phần/kết quả nổi (Floating Cards) vắt qua ranh giới khối màu và bố cục phân tầng có khoảng thở thị giác.
3. **Bộ lọc chống lỗi của các model Flash (Anti-Flash-Model Audit):** Triệt tiêu hoàn toàn 5 lỗi kinh điển: (1) cỡ chữ siêu nhỏ `6pt–10pt`, (2) nhồi nhét văn bản tờ rơi lên poster dọc, (3) chèn nhầm ảnh ngoại lai từ mục *"Bài viết khác"*, (4) cắt cúp ảnh lỗi làm cụt chữ/đầu người, và (5) dùng ảnh AI 3D hoặc hình vẽ SVG màn hình tối giả tạo.

## Dependencies

- **`vn-medical-translation`** (`C:\Users\Thinkpad T14 gen 2\.gemini\config\skills\vn-medical-translation\SKILL.md`): Bắt buộc áp dụng quy tắc chính tả **Sentence-case** cho toàn bộ tiêu đề, đề mục, nhãn bảng và chuẩn hóa thuật ngữ lâm sàng tiếng Việt.

## Quick Start

Khi người dùng cung cấp thư mục nguyên liệu (gồm bản thảo `.md`/`.docx`, file `.pdf`, logo, ảnh thực tế) và yêu cầu thiết kế poster:
1. **Kiểm tra & lọc nguyên liệu thật:** Đọc toàn bộ văn bản gốc và dùng `read_file` xem từng ảnh trong thư mục để xác thực đâu là ảnh thật của đơn vị/nghiên cứu, loại bỏ 100% ảnh ngoại lai hoặc ảnh AI.
2. **Chọn kiến trúc thiết kế (hoặc xuất cả 2 phiên bản để người dùng lựa chọn):**
   - **Kiến trúc Ver 2 (Đa giác trung tâm kiểu *CAS in Brain Health* – Khuyến nghị ưu tiên):** Tiêu đề lớn (`88pt–94pt`) nổi bật ở chính giữa trên nền đa giác xanh đậm vát chéo; 8 thẻ học phần/kết quả trắng độc lập (Floating Cards) vắt ngang ranh giới dưới của khối đa giác; khối Đối tượng dự tuyển / Kết luận chính (`01` & `02`) xếp ngang nổi bật ở nửa dưới bên trái. Xem mẫu tại [templates/poster_landscape_cas_ver2.html](./templates/poster_landscape_cas_ver2.html).
   - **Kiến trúc Ver 1 (Bố cục 3 cột cân đối khổ ngang):** Dải Hero vát chéo ở trên kèm 4 chỉ số dịch tễ/thống kê thực chứng và hộp QR lớn; phần thân chia 3 cột đều nhau từ trái sang phải với các thẻ `flex: 1` tự động cân bằng chiều cao. Xem mẫu tại [templates/poster_landscape_3col_ver1.html](./templates/poster_landscape_3col_ver1.html).
   - **Tờ rơi A4 2 mặt ($210 \times 297\text{ mm}$):** Dành cho toàn bộ nội dung diễn giải chi tiết ($800 - 1.200\text{ từ}$) hoặc chuyển đổi từ các poster dọc nhiều chữ. Xem mẫu tại [templates/flyer_a4_2sided.html](./templates/flyer_a4_2sided.html).
3. **Kết xuất PDF & Kiểm tra thị giác bắt buộc:** Chạy script [scripts/render_poster_pdf.py](./scripts/render_poster_pdf.py) để xuất file PDF chuẩn in ấn và ảnh PNG xem trước, sau đó dùng `read_file` kiểm tra trực quan từng trang trước khi bàn giao.

## Utility Scripts

### `scripts/render_poster_pdf.py`
Script tự động kết xuất file HTML thiết kế sang PDF vector chuẩn kích thước (`1200mm x 900mm` hoặc `A4 210mm x 297mm`) bằng trình duyệt Chromium/Edge headless và tạo ảnh PNG preview để kiểm tra bố cục.

```bash
python "C:\Users\Thinkpad T14 gen 2\.gemini\config\plugins\vn-medical-studio\skills\medical-poster-designer\scripts\render_poster_pdf.py" \
  --input "Poster_Ngang_UMP_DotQuy_Ver2_120x90.html" \
  --output "Poster_Ngang_UMP_DotQuy_Ver2_120x90.pdf" \
  --preview "Poster_Ngang_UMP_DotQuy_Ver2_120x90_preview.png"
```

## Workflow

### Bước 1 — Nhận diện lỗi bản cũ & Kiểm định nguyên liệu hình ảnh (Asset Audit)
- Nếu trong thư mục có sẵn các bản poster do model khác tạo, hãy kiểm tra mã HTML/CSS và ảnh preview của chúng:
  - Đo cỡ chữ thực tế (`font-size` dưới `14pt` trên poster là lỗi nghiêm trọng).
  - Kiểm tra nguồn gốc từng file ảnh: Đối chiếu với trang PDF gốc để phát hiện ảnh lấy nhầm từ mục *"Bài viết khác"* ở cuối trang web (ví dụ: ảnh Bộ môn Y học cổ truyền, Y học thể thao bị chèn nhầm vào poster Bộ môn Đột quỵ).
  - Nếu ảnh tập thể bị vướng chữ mái hiên bị cắt cụt ở mép trên (như `"NG TÂM ĐỘT"`), dùng Python (`PIL.Image`) cắt bỏ phần rìa lỗi trước khi đưa vào thiết kế.

### Bước 2 — Phân bổ nội dung theo nguyên tắc Davies et al. (2024)
Tham chiếu chi tiết tại [references/davies_2024_poster_guidelines.md](./references/davies_2024_poster_guidelines.md):
- **Trên Poster khổ ngang ($120 \times 90\text{ cm}$):**
  - Cô đọng tối đa ($300 - 450\text{ từ}$).
  - Ưu tiên các con số thực chứng có trích dẫn y văn (ví dụ: tỷ lệ mắc mới `161/100.000 dân`, thời gian `"cửa – CT" < 25 phút`, tỷ lệ tái thông `15,1 – 18,8%`).
  - Trình bày các học phần hoặc kết quả nghiên cứu dưới dạng chuỗi thẻ đánh số (`01` đến `08`) hoặc bảng phân tầng ngắn gọn.
- **Trên Tờ rơi A4 2 mặt ($210 \times 297\text{ mm}$):**
  - Đưa toàn bộ phần giải thích chi tiết, bối cảnh dịch tễ học, bảng kỹ năng lâm sàng chi tiết và hướng dẫn hồ sơ vào 2 trang A4 (`@page { size: 210mm 297mm; margin: 0; }`).

### Bước 3 — Thiết lập Typography & Bố cục Flexbox không khoảng chết (Zero Dead-Space CSS)
- **Quy chuẩn cỡ chữ trên khổ $1200 \times 900\text{ mm}$:**
  - Tiêu đề chính ở giữa: `82pt – 96pt` (`font-weight: 800`, `line-height: 1.05`).
  - Phụ đề dưới tiêu đề chính: `26pt – 29pt`.
  - Tiêu đề khu vực (`Chương trình học chuyên sâu`, `Đối tượng đăng ký dự tuyển`): `35pt – 38pt`.
  - Tiêu đề thẻ (`mod-card h3`, `adm-wide-body h3`): `25pt – 28pt`.
  - Nội dung trong thẻ (`mod-card p`, `adm-card-text`): `20pt – 24.5pt`.
- **Kỹ thuật chống khoảng trống thừa bên trong thẻ:**
  - Khi đặt 2 nhóm nội dung (như Đối tượng `01` và `02`) trong một khung rộng, **ưu tiên xếp thành 2 dải thẻ ngang chồng lên nhau (`flex-direction: column`)** kèm biểu tượng vector bên phải thay vì chia 2 cột dọc hẹp dễ gây thừa giấy trắng ở nửa dưới.
  - Luôn đặt `flex: 1` cho các thẻ con trong cột để khoảng cách giữa các thẻ giữ cố định ở mức `3.5mm – 5mm`.

### Bước 4 — Kết xuất PDF, tạo ảnh Preview & Kiểm tra bằng `read_file`
- Chạy `scripts/render_poster_pdf.py` để tạo PDF và PNG.
- Dùng `read_file` mở file PNG vừa tạo để kiểm tra:
  1. Dải băng tiêu đề ở giữa có nằm trọn trong vùng đa giác màu đậm với độ tương phản cao không?
  2. Có thẻ nào bị thừa khoảng trắng lớn hoặc bị tràn chữ ra ngoài khung không?
  3. Tờ rơi A4 có nằm gọn trong đúng 2 trang mà không bị cắt chữ ở mép dưới hoặc nhảy sang trang thứ 3 không?

## Common Mistakes

1. **Đặt dải pill tiêu đề phụ đè lên đường vát chéo sáng màu:** Khi dùng `clip-path: polygon(...)` cho khối đa giác trung tâm, nếu góc vát trên quá dốc (`> 10%`), đầu bên phải của dải chữ màu vàng sẽ bị lọt ra ngoài nền sáng. Phải giữ độ dốc cạnh trên vừa phải (`5% – 6%`) và đặt nền tối bán trong suốt (`rgba(5, 32, 20, 0.9)`) cho dải pill.
2. **Chia cột dọc cho các mục ít chữ gây khoảng trống lớn bên trong hộp:** Với mục `Đối tượng đăng ký dự tuyển (01 & 02)`, chia làm 2 cột dọc sẽ khiến hộp `01` bị trống một nửa chiều cao. Xếp thành 2 hàng ngang (`adm-wide-card`) giúp lấp đầy 100% diện tích và cho phép tăng cỡ chữ lên `22.5pt – 25.5pt`.
3. **Dùng trình duyệt Chrome/Edge đang mở sẵn trên máy tính để chạy `--print-to-pdf`:** Khi người dùng đang mở Chrome/Edge trên màn hình, lệnh `chrome.exe --headless --print-to-pdf` thường thoát ngay mà không ghi file vì xung đột phiên (session handoff). Luôn ưu tiên dùng `chrome-headless-shell.exe` độc lập (như trong `scripts/render_poster_pdf.py`) hoặc truyền `--user-data-dir` riêng biệt.
