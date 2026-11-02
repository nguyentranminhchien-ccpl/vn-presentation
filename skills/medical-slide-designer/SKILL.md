---
name: medical-slide-designer
description: >-
  Thiết kế bộ Slide bài giảng lâm sàng, Báo cáo Hội nghị Khoa học (HNKH), Bảo vệ
  Luận văn/Đề cương và Quy trình kỹ thuật (SOP) chuẩn tỷ lệ 16:9 trên cả hai định
  dạng PowerPoint (.pptx qua python-pptx) và HTML/PDF tương tác, kết hợp cấu trúc
  sư phạm 2 tầng (Slide hiển thị từ khóa định lượng cô đọng >= 18pt + Speaker Notes
  phân tích cơ chế bệnh sinh và bằng chứng chuyên sâu) theo văn phong BS. Nguyễn
  Trần Minh Chiến, nguyên tắc của Davies và cộng sự (2024) và kinh nghiệm thực
  chiến từ phiên Thiết kế Bài giảng Đột quỵ. Kích hoạt khi người dùng yêu cầu tạo
  mới, nâng cấp, kiểm định (audit) hoặc chỉnh sửa phẫu thuật bộ slide y khoa.
---

# Thiết kế slide bài giảng lâm sàng & báo cáo hội nghị khoa học (Medical Slide Designer)

## Overview

Kỹ năng này thiết kế, nâng cấp và kiểm định các bộ **Slide thuyết trình y khoa tỷ lệ $16:9$** trên cả **PowerPoint (`.pptx` qua `python-pptx`)** và **HTML/PDF vector tương tác**, đúc kết từ kinh nghiệm thực chiến xây dựng các bài giảng chuyên sâu về Đột quỵ (*Quản lý đột quỵ sau giai đoạn cấp*, *Đột quỵ não do vữa xơ mạch máu lớn ECAD/ICAD*) và Hồi sức tích cực:
1. **Bài giảng Đào tạo Liên tục (CME) & Chỉ đạo tuyến (Tuyến khu vực / cơ sở & Chuyên khoa):** Cấu trúc sư phạm khép kín từ Câu chuyện mở đầu $\rightarrow$ Mục tiêu đo lường được $\rightarrow$ Lộ trình gắn thời lượng $\rightarrow$ Nội dung phân tầng $\rightarrow$ 5 thông điệp mang về $\rightarrow$ Bảng kiểm thực hành ngoại trú (A–F).
2. **Báo cáo Hội nghị Khoa học (HNKH) & Bảo vệ Luận văn:** Trình bày Đặt vấn đề, Đối tượng & Phương pháp (PICO / Sơ đồ luồng), Kết quả thống kê định lượng và Bàn luận đối chiếu y văn.
3. **Chỉnh sửa Phẫu thuật Slide PowerPoint Hiện có (Surgical `.pptx` Updating):** Bổ sung slide mới, cập nhật phác đồ/bảng biểu theo Guideline mới (`Quyết định 3312/QĐ-BYT 2024`, `AHA/ASA 2021/2022`, `ESVS 2023`, `ESO 2022`) trực tiếp trên file `.pptx` của người dùng mà **không làm mất các chỉnh sửa thủ công hay định dạng mẫu gốc**.

## Dependencies & Tài liệu tham chiếu nội bộ

- **`vn-medical-translation`** (`C:\Users\Thinkpad T14 gen 2\.gemini\config\skills\vn-medical-translation\SKILL.md`): Chuẩn hóa chính tả **Sentence-case**, hệ thuật ngữ lâm sàng (`chảy máu não`, `sau giai đoạn cấp`, `vữa xơ mạch máu lớn`, `giãn`, `xẹp / đè dẹt`, `ứ khí`, `trống âm`, `sốc tim`) và văn phong **Speaker Notes**.
- **Kinh nghiệm thực chiến Thiết kế Bài giảng Đột quỵ:** Xem chi tiết tại [references/stroke_lecture_design_experience.md](./references/stroke_lecture_design_experience.md).
- **Bộ công cụ tự động hóa `.pptx` & Kiểm định QA:**
  - [scripts/pptx_medical_helper.py](./scripts/pptx_medical_helper.py): Thư viện dựng slide `.pptx` chuẩn `BVT Medical Infographic Style` (`13.333" x 7.5"`), hàm cập nhật phẫu thuật không ghi đè (`rep_para`, `set_clean_box`, `move_slide_to_index`) và công cụ tìm ảnh y khoa hợp lệ từ Wikimedia Commons API.
  - [scripts/verify_pptx_qa.py](./scripts/verify_pptx_qa.py): Kịch bản kiểm định tự động cỡ chữ tối thiểu (`>= 18pt`), kiểm tra 100% Speaker Notes, quét thuật ngữ lỗi và kết xuất ảnh PNG (`1600x900`) qua PowerPoint COM để duyệt trực quan bằng `read_file`.
  - [templates/slide_deck_16x9_clinical.html](./templates/slide_deck_16x9_clinical.html): Mẫu HTML/PDF $16:9$ tương tác (hỗ trợ phím `←`/`→` và phím `N` mở Speaker Notes).

---

## 6 Nguyên tắc Sư phạm & Thiết kế Cốt lõi (Đúc kết từ Phiên Bài giảng Đột quỵ)

### 1. Kiến trúc Sư phạm Khép kín & Phân bổ Thời lượng (Pedagogical Flow)
Một bài giảng lâm sàng chuẩn mực (25–30 slides cho 30–45 phút) phải có vòng lặp sư phạm hoàn chỉnh:
- **Slide 1 (Trang bìa):** Tiêu đề chuẩn thuật ngữ Bộ Y tế (ví dụ: dùng *«chảy máu não»* thay cho *«xuất huyết não»*, dùng *«sau giai đoạn cấp»* thay cho *«sau cấp»*), tên báo cáo viên, đơn vị và thời lượng.
- **Slide 2 (Mục tiêu học tập & Lộ trình gắn số phút):**
  - Mục tiêu học tập (3–5 mục tiêu) **bắt buộc mở đầu bằng động từ hành động đo lường được**: *«Trình bày được...»*, *«Áp dụng được...»*, *«Thực hành được...»*, *«Phân tầng được...»* (tuyệt đối không viết danh từ cụt ngủn như *«Thực trạng đột quỵ»*).
  - Lộ trình bài giảng chia thành 4 phần rõ ràng, **mỗi phần gắn huy hiệu thời lượng cụ thể** (ví dụ: `Phần 1: 4 phút`, `Phần 2: 10 phút`, `Phần 3: 6 phút`, `Phần 4: 6 phút`, `Thảo luận: 3 phút`).
- **Slide Mở đầu (Clinical Hook & Bối cảnh Việt Nam):** Dẫn dắt bằng số liệu thực tế tại Việt Nam (`GBD 2021 Vietnam – 167.000 ca tử vong/năm`, `Ton MD et al. SVIN 2022` về hệ thống đơn vị đột quỵ & ANGELS) và khoảng trống chăm sóc sau khi bệnh nhân xuất viện về tuyến cơ sở.
- **Slide Chuyển phần (Section Dividers):** Đánh dấu rõ số thứ tự phần, tiêu đề phần, các từ khóa trọng tâm và huy hiệu thời lượng.
- **Slide Kết bài (Đóng vòng sư phạm):**
  - **5 thông điệp cốt lõi cần mang về (*Take-home messages*):** Tóm lược mỗi phần thành 1 câu hành động định lượng.
  - **Bảng kiểm thực hành ngoại trú 6 mục (A–F):** Công cụ cầm tay dùng ngay tại bàn khám tái khám (`A. Thần kinh & chức năng`, `B. Đích yếu tố nguy cơ`, `C. Rà soát đơn thuốc & ngày ngưng DAPT`, `D. Tầm soát biến chứng muộn`, `E. PHCN & người chăm sóc`, `F. Tiêu chí hội chẩn / chuyển tuyến chuyên khoa`).

### 2. Kiến trúc 2 Tầng & Giảm tải Nhận thức trên Mặt Slide (Dual-Layer Cognitive Offloading)
- **Tầng 1 — Mặt Slide (On-Slide Layer):**
  - **Cỡ chữ tối thiểu bắt buộc `>= 18pt` (`MIN_FONT_PT = 18`)** cho toàn bộ nội dung thẻ, danh sách và bảng biểu trên bài giảng chuẩn (Tiêu đề slide `25–28pt` đậm kèm thanh nhấn màu cam `#E97132`).
  - **Chỉ giữ từ khóa hành động & Ký hiệu trực quan:** Mỗi thẻ tối đa `3–4 dòng ngắn`; sử dụng nhất quán bộ ký hiệu:
    - **`✓`** : Nên làm / Chỉ định ưu tiên.
    - **`✗`** : Không làm / Chống chỉ định (ví dụ: `✗ Không dùng tất đàn hồi áp lực`, `✗ Không vận động cường độ cao trong 24h đầu`).
    - **`⚠`** : Cẩn trọng / Nguy cơ cao.
    - **`→`** : Hành động tiếp theo / Chuyển đổi phác đồ / Chuyển tuyến.
  - **Quy tắc Lọc nhiễu cho Tuyến cơ sở:** Khi giảng cho bác sĩ đa khoa hoặc tuyến khu vực/cơ sở, **lược bỏ các mã `COR 1, 2a, 2b, 3`, `LOE A, B-R` và tên viết tắt hàng loạt thử nghiệm (`CHANCE`, `POINT`, `THALES`, `SPARCL`, `IMPROVE-IT`) khỏi mặt slide**, chuyển toàn bộ xuống **Speaker Notes**. Với bảng phân loại (như bảng TOAST), chỉ giữ 3 cột hành động trên mặt slide (*Phân nhóm*, *Thuốc kháng huyết khối nền*, *Điều trị phối hợp trọng tâm*) và đưa cột *Cơ chế bệnh sinh* vào Notes.
- **Tầng 2 — Ghi chú Thuyết trình (Speaker Notes Layer):**
  - **Bắt buộc 100% các slide phải có Speaker Notes** (kể cả trang bìa, trang chuyển phần, trang cảm ơn và tài liệu tham khảo).
  - Nội dung Notes viết bằng văn phong học thuật lâm sàng hoàn chỉnh: giải thích cơ chế bệnh sinh, phân tích các thử nghiệm nền tảng, giải thích các điểm giao thoa giữa các Guideline (ví dụ: vì sao giữ mốc khởi động kháng đông theo `Quyết định 3312/QĐ-BYT 2024` nhưng dùng đích huyết áp `< 130/80 mmHg` theo `AHA/ASA 2021`), kèm mục `LƯU Ý THỰC HÀNH` / `CÂU HỎI THƯỜNG GẶP` và dòng `[Nguồn tham khảo]: ...`.

### 3. Phân hóa Nội dung theo Đúng Giai đoạn Bệnh & Phân tầng Mức độ Nặng
- **Không trộn lẫn giai đoạn cấp vào bài giảng sau giai đoạn cấp:** Ví dụ ở phần Chảy máu não sau giai đoạn cấp, không đưa thang điểm ICH (tiên lượng tử vong 30 ngày lúc nhập viện) hay cầm máu cấp cứu lên mặt slide chính; thay bằng **3 trọng tâm giai đoạn muộn**:
  1. *Phân tầng nguy cơ tái phát theo vị trí giải phẫu:* Chảy máu sâu (nhân bèo, đồi thị, cầu não do tăng huyết áp $\rightarrow$ nguy cơ tái phát thấp nếu kiểm soát HA tốt) vs. Chảy máu thùy não (gợi ý bệnh mạch máu dạng bột não `CAA` ở người cao tuổi $\rightarrow$ nguy cơ tái phát rất cao).
  2. *Tầm soát căn nguyên mạch máu muộn:* Hẹn chụp lại `MRI/MRA/CTA` sau 4–8 tuần khi khối máu tụ đã tiêu để loại trừ dị dạng mạch (`AVM`, u máu thể hang, phình mạch).
  3. *Theo dõi biến chứng muộn:* Động kinh muộn, giãn não thất mạn tính (tam chứng rối loạn dáng đi, tiểu không tự chủ, suy giảm nhận thức), trầm cảm và co cứng cơ.
- **Phân tầng điều trị chuyên sâu theo mức độ nặng (Nhẹ/TIA – Trung bình – Nặng – Tắc mạch lớn cấp ICAS-LVO):**
  - Khi thiết kế bài giảng chuyên khoa sâu (như *Vữa xơ mạch máu lớn ECAD & ICAD*), phải lập bảng đối chiếu rõ ràng giữa **ECAD (ĐM cảnh / ĐM đốt sống V1–V3)** và **ICAD (ĐM nội sọ / ĐM đốt sống V4)**, phân tầng kháng kết tập tiểu cầu theo mức độ đột quỵ (khi nào dùng DAPT 21 ngày vs. 90 ngày `SAMMPRIS` vs. 30 ngày `THALES/CHANCE-2` vs. phối hợp `Cilostazol` giai đoạn bán cấp vs. bắt buộc đơn trị `SAPT` ở ổ nhồi máu lớn `> 1/3 MCA` hoặc `mRS >= 3` để tránh chuyển dạng chảy máu `sICH`), và quy trình chu phẫu `CEA / CAS / TCAR` hoặc `Rescue Stenting + GP IIb/IIIa`.

### 4. Quy chuẩn Minh họa Y khoa & Cấm Tuyệt đối Ảnh AI Giả tạo
- **Cấm 100% ảnh do AI sinh ra (AI-generated images):** Các ảnh AI vẽ cảnh bệnh viện/bác sĩ thường chứa chữ tiếng Anh vô nghĩa (*"Northbridge Health System"*, *"Stroke Reecovery"*), giải phẫu sai lệch hoặc nhầm sang bệnh lý khác (*Parkinson*, *Multiple Sclerosis*, *ALS*).
- **Cấm logo thương hiệu & thông tin định danh bệnh nhân (PHI):** Không dùng ảnh còn watermark thương mại (*"timeisbrain"*, tên hãng thiết bị) hoặc phim CT/MRI chưa cắt bỏ tên/tuổi/ID bệnh nhân.
- **4 Nguồn hình ảnh y khoa chuẩn mực được phép sử dụng:**
  1. **Sơ đồ vector tự dựng bằng `python-pptx` / SVG:** Đường cong 5 giai đoạn hồi phục sau đột quỵ (*Bernhardt 2017*), sơ đồ giải phẫu chảy máu sâu vs. chảy máu thùy, lưu đồ quyết định kháng tiểu cầu.
  2. **Wikimedia Commons / NIH / CDC PHIL / OpenStax:** Tìm kiếm và tải tự động qua script `commons_search.py` (chỉ chọn ảnh có giấy phép mở `CC BY`, `CC BY-SA`, `CC0`, `Public Domain`, chiều rộng `>= 1200px`).
  3. **Radiopaedia.org / Học liệu gốc của Bộ môn:** Ảnh cắt lớp vi tính (`CT`), cộng hưởng từ (`MRI`), chụp mạch (`CTA/DSA`) thực tế đã ẩn danh hoàn toàn và ghi công đầy đủ (`Case courtesy of..., Radiopaedia.org, rID:...`) trong Speaker Notes của slide Tài liệu tham khảo.
  4. **Biểu tượng y khoa vector sạch:** Dùng cho các slide quy trình, kiểm soát yếu tố nguy cơ.

### 5. Quy tắc Vàng khi Chỉnh sửa File `.pptx` Hiện có (Surgical In-Place Update Rule)
> [!CAUTION]
> **TUYỆT ĐỐI KHÔNG CHẠY LẠI SCRIPT BUILD TOÀN BỘ ĐỂ GHI ĐÈ FILE `.PPTX` KHI NGƯỜI DÙNG ĐÃ CHỈNH SỬA THỦ CÔNG!**
> Khi người dùng đã mở file `.pptx` để căn chỉnh bố cục, chèn thêm ảnh hoặc sửa chữ, việc chạy lại `build_slides.py` từ đầu sẽ xóa sạch mọi công sức chỉnh sửa của người dùng.

**Quy trình bắt buộc khi cập nhật/bổ sung slide vào bộ `.pptx` có sẵn:**
1. **Sao lưu tự động:** Luôn copy file gốc sang `.backup_truoc_cap_nhat.pptx` trước khi can thiệp.
2. **Thay thế văn bản bảo toàn định dạng (`rep_para`):** Duyệt qua các `runs` của từng đoạn văn (`paragraph`) để thay thế chuỗi đích mà giữ nguyên hoàn toàn font, cỡ chữ, màu sắc và vị trí hộp văn bản.
3. **Nhân bản cấu trúc XML từ slide mẫu cùng bộ (`copy.deepcopy`):** Khi cần thêm một dải thẻ (band/card) hoặc thêm slide mới đồng bộ tuyệt đối với thiết kế sẵn có của người dùng (như thêm slide `2.8 Kháng kết tập tiểu cầu chu phẫu CEA/CAS` từ mẫu slide `2.7`, hoặc thêm các bảng tổng hợp vào bài giảng `Vữa xơ mạch máu lớn`), dùng `copy.deepcopy(template_shape._element)` và chèn slide vào đúng vị trí logic qua `prs.slides._sldIdLst.insert(target_idx, el)`.
4. **Khử lỗi hai dấu chấm đầu dòng (Double-Bullets XML Fix):** Khi điền danh sách có ký tự `•` vào placeholder của template có sẵn, phải xóa `<a:lstStyle>` và gắn thẻ `<a:buNone/>` vào `pPr` (như hàm `set_clean_box` trong [scripts/pptx_medical_helper.py](./scripts/pptx_medical_helper.py)) để PowerPoint không tự sinh thêm một dấu bullet thứ hai chồng lên chữ.

### 6. Quy trình Kiểm định Chất lượng (Audit) & Duyệt Thị giác (`export_verify`)
Trước khi bàn giao bất kỳ bộ slide `.pptx` hoặc HTML/PDF nào, bắt buộc thực hiện:
1. **Kiểm định Nội dung & Sự nhất quán nội tại (Clinical & Internal Consistency Audit):**
   - Đối chiếu chéo các con số giữa các slide (ví dụ: mốc can thiệp động mạch cảnh `trong vòng 14 ngày đầu` phải thống nhất giữa slide chỉ định, slide phác đồ thuốc và bảng kiểm cuối bài; liều Aspirin, đích huyết áp `< 130/80 mmHg` và đích `LDL-C < 55` hay `< 70 mg/dL` không được mâu thuẫn nhau).
   - Mọi tài liệu trích dẫn ở chân slide hoặc Speaker Notes phải có mặt đầy đủ trong slide `Tài liệu tham khảo chính` cuối bài (và ngược lại, không để tài liệu "mồ côi").
2. **Chạy Script Kiểm định Tự động & Xuất ảnh PNG (`verify_pptx_qa.py`):**
   - Kiểm tra `min_font_size >= 18pt` (hoặc ngưỡng quy định của bảng chuyên khoa), `missing_notes == []`, và không còn thuật ngữ lỗi (`xuất huyết não`, `sau cấp`, `dãn`, `bẹp`).
   - Kết xuất các slide mới/vừa sửa ra ảnh PNG độ phân giải cao (`1600x900`) bằng `win32com.client.Dispatch("PowerPoint.Application")` và dùng công cụ `read_file` kiểm tra trực quan từng ảnh để đảm bảo không tràn khung, không đè chữ lên footer.
