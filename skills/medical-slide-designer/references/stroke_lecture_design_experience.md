# Kinh nghiệm thực chiến thiết kế & kiểm định bài giảng lâm sàng đột quỵ (Từ phiên 6f31df31-9e24-47cb-8fe6-c74feed7515b)

Tài liệu này đúc kết toàn bộ quy chuẩn sư phạm, bảng màu, mẫu bố cục PowerPoint (`python-pptx`), kỹ thuật chỉnh sửa phẫu thuật (`.pptx` surgical editing) và danh mục kiểm định chất lượng (Audit Checklist) từ phiên thiết kế hai bộ bài giảng lớn:
1. **Bài giảng đào tạo tuyến khu vực/cơ sở (29 slides):** *«Quản lý và chăm sóc toàn diện bệnh nhân đột quỵ sau giai đoạn cấp»*.
2. **Bài giảng chuyên khoa sâu (62 slides):** *«Quản lý, điều trị, dự phòng đột quỵ não do vữa xơ mạch máu lớn (ECAD & ICAD)»*.

---

## 1. Hệ thống Bảng màu & Typography Chuẩn (`BVT Medical Infographic Style`)

- **Kích thước Slide chuẩn Widescreen $16:9$:** `13.333 inches × 7.5 inches` (`33,867 cm × 19,05 cm`).
- **Font chữ chuẩn:** `Calibri` hoặc `Arial` (đồng bộ hoàn toàn giữa Tiêu đề, Thân bài, Bảng biểu và Chân trang).
- **Quy chuẩn Cỡ chữ (`MIN_FONT_PT = 18`):**
  - **Tiêu đề Slide nội dung:** `25pt – 28pt` (In đậm, màu `#1F1E1E` hoặc `#0E2841`), đặt tại tọa độ `left=0.47"`, `top=0.18"`, `width=12.39"`, `height=0.80"`, đi kèm thanh nhấn ngang màu cam (`#E97132`, `width=2.84"`, `height=0.06"`, `top=1.02"`).
  - **Tiêu đề dải băng / Huy hiệu đầu cột (Header Badge):** `18pt – 19.5pt` (In đậm, chữ trắng `#FFFFFF` trên nền màu đậm).
  - **Nội dung trong thẻ / Bảng biểu / Danh sách (Body & Cards):** **`18pt – 20pt`** (tuyệt đối không nhỏ hơn `18pt` đối với bài giảng chuẩn; riêng bảng ma trận đa chiều 4 cột chuyên sâu cho bác sĩ chuyên khoa có thể dùng `11.8pt – 14.5pt` nhưng phải căn lề ô thoáng và kiểm tra PNG thực tế).
- **Bảng màu Chức năng Lâm sàng (Semantic Clinical Color Palette):**
  - `C_NAVY = RGBColor(14, 40, 65)` (`#0E2841`): Màu chữ chính và tiêu đề nhóm Phác đồ nền tảng / Nhồi máu não.
  - `C_TEAL = RGBColor(21, 96, 130)` (`#156082`) & `C_DK_TEAL = RGBColor(11, 110, 158)` (`#0B6E9E`): Màu chủ đạo cho Chẩn đoán, Phân tầng nguy cơ và Đích sinh học.
  - `C_ORANGE = RGBColor(233, 113, 50)` (`#E97132`) & `C_DK_ORANGE = RGBColor(197, 90, 17)` (`#C55A11`): Màu nhấn cho Chảy máu não, Cửa sổ vàng chuyển tuyến và Hành động tại tuyến cơ sở.
  - `C_GREEN = RGBColor(25, 107, 36)` (`#196B24`): Màu chủ đạo cho Phục hồi chức năng, Lối sống và Chỉ định nên làm (`✓`).
  - `C_RED = RGBColor(192, 0, 0)` (`#C00000`): Màu cảnh báo Chống chỉ định (`✗`), Biến chứng nguy hiểm (`COR 3: Harm`) và Tiêu chí chuyển tuyến khẩn.
  - **Màu nền thẻ dịu mắt (Soft Card Backgrounds):**
    - `BG_ICE = RGBColor(241, 245, 248)` (`#F1F5F8` — Xanh băng nhạt cho thẻ thông tin chuẩn).
    - `BG_PEACH = RGBColor(251, 237, 227)` (`#FBEDE3` — Cam đào nhạt cho thẻ lưu ý thực hành/tuyến cơ sở).
    - `BG_SOFT_TEAL = RGBColor(234, 241, 245)` (`#EAF1F5` — Xanh ngọc nhạt cho thẻ nguyên tắc thực hành).
    - `BG_LT_GREEN = RGBColor(214, 235, 211)` (`#D6EBD3` — Xanh lá nhạt cho thẻ chỉ định an toàn).
    - `BG_LT_RED = RGBColor(250, 229, 229)` (`#FAE5E5` — Đỏ hồng nhạt kèm viền `C_RED` cho thẻ cảnh báo có hại / chuyển tuyến).

---

## 2. Năm Mẫu Bố cục Slide (Slide Layout Archetypes) Đã Kiểm chứng

1. **Mẫu A — Ba cột song song có huy hiệu đầu cột (`3-Column Card Layout`):**
   - Tọa độ: `x_l = 0.47 + i * 4.20` (`i = 0, 1, 2`), `width = 3.99"`.
   - Huy hiệu tiêu đề (`add_header_badge`): `top = 1.25"`, `height = 0.56"`.
   - Thân thẻ (`add_card`): `top = 1.90"`, `height = 5.15"`.
   - Ứng dụng: Phân tầng 3 trọng tâm chảy máu não giai đoạn muộn (Slide 16), 3 trụ cột kiểm soát huyết áp (Slide 17), Tổ chức PHCN tại tuyến cơ sở (Slide 24).
2. **Mẫu B — Hai cột đối chiếu (`2-Column Split Comparison`):**
   - Cột trái: `left = 0.47"`, `width = 6.05"`. Cột phải: `left = 6.75"`, `width = 6.11"`.
   - Ứng dụng: Đối chiếu Khuyến cáo quốc tế vs. Thực hành tại tuyến cơ sở (Slide 18), Cơ sở sinh học thần kinh vs. 4 nguyên tắc tập luyện (Slide 21), Kháng kết tập tiểu cầu đơn trị (SAPT) vs. Kép ngắn hạn (DAPT) (Slide 9).
3. **Mẫu C — Các dải băng ngang đánh số tròn (`Horizontal Numbered Action Bands`):**
   - 3 đến 5 dải băng ngang (`left = 0.47"`, `width = 12.39"`), bên trái có vòng tròn đánh số `1, 2, 3...` hoặc `A, B, C, D` (`add_circle_number`), bên phải là tiêu đề đậm và 1–2 dòng hành động.
   - Ứng dụng: Hẹp động mạch cảnh & cửa sổ vàng 2 tuần (Slide 14), Phác đồ kháng tiểu cầu theo 4 nhóm hẹp cảnh A–D (Slide 15), 5 thông điệp mang về (Slide 25).
4. **Mẫu D — Lưới 6 ô (`2×3 Action Grid`):**
   - 2 hàng × 3 cột (`x_l = 0.47 + c_i * 4.20`, `y_t = 1.25 + r_i * 2.92`, `width = 3.99"`, `height = 2.74"`).
   - Ứng dụng: Kiểm soát 6 yếu tố nguy cơ & lối sống (Slide 13), Quản lý 6 biến chứng sau chảy máu não (Slide 19), Bảng kiểm tái khám 6 mục A–F (Slide 26).
5. **Mẫu E — Quy trình 4 bước ngang kết hợp thanh tổng hợp đáy (`4-Step Process + Bottom Banner`):**
   - 4 thẻ dọc (`x_l = 0.47 + i * 3.14`, `width = 2.98"`, `top = 1.25"`, `height = 4.05"`) + 1 dải băng tổng hợp ngang bên dưới (`top = 5.48"`, `width = 12.39"`).
   - Ứng dụng: Quy trình phục hồi chức năng 4 bước (Lượng giá $\rightarrow$ Đặt mục tiêu $\rightarrow$ Can thiệp $\rightarrow$ Tái lượng giá) kèm Tổ hợp đa chuyên ngành nòng cốt tại tuyến cơ sở (Slide 22).

---

## 3. Bài học Kinh nghiệm từ Báo cáo Kiểm định (`Audit Findings & Fixes`)

Khi tự kiểm định (Self-Audit) một bộ slide bài giảng y khoa trước khi trình chiếu, luôn rà soát 10 lỗi kinh điển đã được phát hiện và xử lý triệt để trong phiên `6f31df31-9e24-47cb-8fe6-c74feed7515b`:

| STT | Lỗi phát hiện khi Audit | Giải pháp chuẩn hóa trong `medical-slide-designer` |
| :-- | :--- | :--- |
| 1 | **Mục tiêu học tập thiếu động từ hành động** (*«Thực trạng đột quỵ tại Việt Nam»*) | Bắt buộc mở đầu bằng động từ đo lường được: *«Trình bày được thực trạng...»*, *«Áp dụng được dự phòng...»*, *«Thực hành được nguyên lý...»*. |
| 2 | **Lộ trình bài giảng không có phân bổ thời gian** khiến báo cáo viên cháy giáo án | Gắn huy hiệu số phút cụ thể cho từng phần ngay tại Slide Lộ trình và trên từng Slide Chuyển phần (`4 phút`, `10 phút`, `6 phút`, `6 phút`). |
| 3 | **Mặt slide quá tải các mã `COR 1, 2a, 2b`, `LOE B-R` và tên thử nghiệm (`CHANCE`, `POINT`, `SPARCL`)** gây nhiễu cho tuyến cơ sở | Dùng biểu thức chính quy (Regex) hoặc biên tập viên lọc sạch `COR/LOE` và tên thử nghiệm khỏi mặt slide của bài giảng tuyến cơ sở; chuyển toàn bộ xuống **Speaker Notes**. |
| 4 | **Bảng phân loại TOAST trên slide có cột "Cơ chế bệnh sinh" quá dài** làm chữ nhỏ và rối | Rút gọn bảng trên mặt slide còn đúng 3 cột hành động (*Phân nhóm căn nguyên*, *Thuốc kháng huyết khối nền*, *Điều trị phối hợp trọng tâm*); thuyết minh 4 cơ chế bệnh sinh trong Notes. |
| 5 | **Thiếu hướng dẫn cho nhóm Nhồi máu não căn nguyên không xác định (`ESUS / Cryptogenic`)** | Luôn bổ sung ghi chú thực hành: Nhóm căn nguyên chưa xác định dùng kháng kết tập tiểu cầu và tầm soát rung nhĩ kéo dài (Holter điện tim), **không dùng kháng đông kinh nghiệm thường quy**. |
| 6 | **Viết "duy trì suốt đời" cho thuốc kháng tiểu cầu/hạ áp trên mặt slide** dễ gây cứng nhắc khi có biến cố chảy máu | Chuẩn hóa thành *«dùng dài hạn»* trên mặt slide; giải thích nguyên tắc theo dõi định kỳ trong Notes. |
| 7 | **Mâu thuẫn nội bộ về mốc thời gian can thiệp động mạch cảnh** (chỗ ghi *«trong tuần đầu»*, chỗ ghi *«2 tuần»*) | Chuẩn hóa thống nhất trên toàn bộ slide và Notes theo `ESVS 2023` & `Bộ Y tế 2024`: **«trong vòng 14 ngày đầu (2 tuần) kể từ khi khởi phát biến cố»**. |
| 8 | **Nhầm nguồn khuyến cáo giữa các Guideline** (ví dụ gắn `AHA/ASA 2022 ICH` cho khuyến cáo *Xuất viện sớm có hỗ trợ – ESD*) | Kiểm tra chéo từng nguồn: `ESD` thuộc `AHA/ASA 2016 Adult Stroke Rehabilitation Guideline` (Winstein CJ et al.) và `Quyết định 3312/QĐ-BYT 2024 (Mục 13)`, không phải `AHA/ASA 2022`. |
| 9 | **Tài liệu tham khảo "mồ côi"** (có trong danh mục cuối bài nhưng không xuất hiện ở bất kỳ slide nào, hoặc ngược lại) | Lập ma trận ánh xạ Nguồn $\leftrightarrow$ Slide trước khi xuất bản; xóa các tài liệu không dùng và bổ sung đủ các tài liệu được trích dẫn ở Notes. |
| 10 | **Đề xuất gửi video bệnh nhân qua Zalo nhưng quên lưu ý bảo mật thông tin người bệnh** | Luôn kèm cụm từ: *«(cần người bệnh đồng ý, ẩn thông tin định danh)»* khi hướng dẫn hội chẩn hoặc theo dõi tập luyện qua Zalo. |
