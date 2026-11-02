# RULE — VN Medical Studio: Quy chuẩn Thiết kế Poster Khoa học, Tờ rơi A4, Slide Lâm sàng & Dịch thuật Y khoa

## 1. Quy chuẩn Thiết kế Poster Khoa học & Đào tạo Y khoa (Theo Davies et al., *Clinical Nutrition ESPEN*, 2024)

Mọi tác vụ thiết kế poster hội nghị y khoa, poster giới thiệu chương trình đào tạo hoặc báo cáo nghiên cứu phải tuân thủ nghiêm ngặt 5 nguyên tắc cốt lõi từ bài báo hướng dẫn của Davies NA, Deutz NE, Delzenne N, Lobo DN (*Presentation and publication skills: How to prepare a scientific poster*, *Clinical Nutrition ESPEN*, 2024;63:457–461, DOI: `10.1016/j.clnesp.2024.06.056`) và kinh nghiệm thực chiến khắc phục lỗi của các model Flash:

1. **Ưu tiên khổ ngang (Landscape $120 \times 90\text{ cm}$, tỷ lệ $4:3$ hoặc $16:9$) & Phân tách chức năng Poster vs. Tờ rơi A4:**
   - **Poster hội nghị ($120 \times 90\text{ cm}$):** Thiết kế để đại biểu đứng đọc ở khoảng cách $1,5 - 2,5\text{ m}$ trong $60 - 90\text{ giây}$. Tổng lượng chữ trên poster giới hạn ở mức cô đọng ($300 - 450\text{ từ}$), tập trung vào tiêu đề trung tâm, các chỉ số định lượng then chốt, các thẻ học phần/kết quả nổi (Floating Cards) và điều kiện/kết luận cốt lõi.
   - **Tờ rơi cầm tay (A4 2 mặt, $210 \times 297\text{ mm}$):** Toàn bộ nội dung diễn giải chi tiết ($800 - 1.200\text{ từ}$) phải được tách sang ấn phẩm Tờ rơi A4 2 mặt đặt tại bàn hội nghị, tuyệt đối không nhồi nhét toàn bộ văn bản của tờ rơi lên một tấm poster dọc gây hiện tượng "bức tường chữ" (*Wall of Text*).

2. **Quy chuẩn Cỡ chữ Bắt buộc trên Poster Khổ ngang ($120 \times 90\text{ cm}$):**
   - **Tiêu đề chính (Main Title):** `76pt – 96pt` (in đậm `800`, nổi bật tại tâm điểm hoặc dải băng đa giác trung tâm).
   - **Phụ đề / Dẫn nhập (Subtitle / Lead):** `25pt – 30pt`.
   - **Tiêu đề các khu vực / cột (Section Headers):** `34pt – 38pt`.
   - **Tiêu đề thẻ học phần / kết quả (Card Titles):** `24pt – 28pt`.
   - **Nội dung thân bài (Body Text & Bullets):** `19.5pt – 25pt`.
   - **Chú thích ảnh & Nhãn phụ (Captions & Badges):** Tối thiểu `15pt – 18pt`.
   - **CẤM TUYỆT ĐỐI:** Không được phép dùng cỡ chữ `< 14pt` (như lỗi `6.3pt – 9.7pt` của các model Flash) ở bất kỳ vị trí nào trên poster.

3. **Kiểm định Nguyên liệu Hình ảnh Thực tế 100% (Authentic Asset Verification):**
   - **Bắt buộc kiểm tra trực quan từng file ảnh (`read_file`)** trước khi chèn vào HTML/PDF/PPTX.
   - **Cấm chèn ảnh ngoại lai từ mục "Bài viết khác":** Khi trích xuất ảnh từ PDF hoặc trang web của trường/bệnh viện, phải kiểm tra ngữ cảnh trang chứa ảnh để loại bỏ các ảnh thumbnail thuộc chuyên mục *"Bài viết khác"*, *"Tin liên quan"* của các bộ môn/đơn vị khác.
   - **Cấm ảnh AI giả tạo & hình vẽ SVG màn hình tối rối mắt:** Tuyệt đối không dùng ảnh não bộ phát sáng 3D, tòa nhà/bệnh viện giả tưởng do AI sinh ra (thường chứa chữ tiếng Anh sai như *"Stroke Reecovery"*, *"Northbridge Health"* hoặc nhầm bệnh *Parkinson/MS/ALS*) hoặc các hình vẽ SVG giả lập màn hình monitor tối màu. Chỉ sử dụng ảnh chụp lâm sàng/tập thể thực tế, ảnh mở từ Wikimedia Commons / NIH / Radiopaedia (đã ẩn danh), sơ đồ vector tự dựng bằng `python-pptx` và biểu tượng vector y khoa tối giản.
   - **Kiểm soát cắt cúp ảnh (Cropping Guardrail):** Không để `object-fit: cover` cắt ngang qua đầu người hoặc cắt cụt dòng chữ biển hiệu phía trên (ví dụ lỗi cắt chữ `"TRUNG TÂM ĐỘT QUỴ"` thành `"NG TÂM ĐỘT"`). Phải xử lý cắt ảnh gốc sạch sẽ trước khi đưa vào khung.

4. **Quy trình Bắt buộc: Render PDF/PPTX $\rightarrow$ Xuất ảnh PNG $\rightarrow$ Kiểm tra Thị giác (`read_file`):**
   - Sau khi viết mã HTML/CSS hoặc tạo/cập nhật file `.pptx`, agent **BẮT BUỘC** phải kết xuất sang ảnh PNG độ phân giải cao và dùng `read_file` để kiểm tra bằng mắt:
     - Có bị tràn trang (page overflow) hoặc cắt mất chân trang không?
     - Các thẻ thông tin có bị khoảng trống thừa bên trong hoặc lệch chiều cao giữa các cột không?
     - Độ tương phản của chữ trên nền đã sắc nét 100% chưa?

---

## 2. Quy chuẩn Thiết kế & Chỉnh sửa Phẫu thuật Slide Bài giảng Lâm sàng (`medical-slide-designer`)

1. **Kiến trúc Sư phạm 2 Tầng & Cỡ chữ Tối thiểu `>= 18pt` (`MIN_FONT_PT = 18`):**
   - **Trên mặt Slide:** Cỡ chữ tối thiểu `>= 18pt` cho mọi thẻ, danh sách và bảng biểu chuẩn; chỉ giữ từ khóa hành động cô đọng (`3–4 ý/thẻ`) kết hợp hệ ký hiệu trực quan **`✓` (Nên làm)**, **`✗` (Không làm / Chống chỉ định)**, **`⚠` (Cẩn trọng)**, **`→` (Hành động tiếp theo / Chuyển tuyến)**. Đối với bài giảng tuyến khu vực/cơ sở, lọc bỏ các mã `COR/LOE` và tên viết tắt thử nghiệm lâm sàng khỏi mặt slide, đưa toàn bộ xuống **Speaker Notes**.
   - **Trong Speaker Notes (Bắt buộc 100% số slide):** Mọi slide đều phải có ghi chú thuyết trình chi tiết giải thích cơ chế bệnh sinh, phân tích thử nghiệm lâm sàng, lưu ý thực hành và dòng `[Nguồn tham khảo]: ...`.
   - **Cấu trúc bài giảng khép kín:** Mục tiêu học tập bắt đầu bằng động từ hành động đo lường được (*«Trình bày được...»*, *«Áp dụng được...»*, *«Thực hành được...»*); Lộ trình và Slide chuyển phần có gắn số phút cụ thể; cuối bài có **5 thông điệp mang về (Take-home messages)** và **Bảng kiểm thực hành ngoại trú 6 mục (A–F)**.

2. **Quy tắc Bảo toàn Chỉnh sửa Thủ công & Cập nhật Phẫu thuật File `.pptx`:**
   - **CẤM TUYỆT ĐỐI** chạy lại script build toàn bộ từ đầu để ghi đè lên file `.pptx` mà người dùng đã mở và chỉnh sửa thủ công.
   - Bắt buộc tạo bản sao lưu `.backup_*.pptx` trước khi sửa, sử dụng kỹ thuật cập nhật phẫu thuật tại chỗ (`rep_para`, `copy.deepcopy(shape._element)`, xóa `<a:lstStyle>` và gắn `<a:buNone/>` để tránh lỗi hai dấu chấm đầu dòng, và di chuyển vị trí slide qua `prs.slides._sldIdLst`).

---

## 3. Quy chuẩn Chính tả Sentence-case & Văn phong Học thuật Lâm sàng (Phong cách BS. Nguyễn Trần Minh Chiến)

Áp dụng nhất quán kỹ năng **`vn-medical-translation`** cho toàn bộ văn bản trên Poster, Tờ rơi A4, Slide bài giảng và bản dịch y khoa:
- **Quy tắc Sentence-case tuyệt đối:** Mọi tiêu đề (`H1–H4`), tiêu đề slide, nhãn bảng, chú thích hình ảnh chỉ viết hoa chữ cái đầu câu và danh từ riêng / từ viết tắt quốc tế (`UMP`, `ĐHQGHN`, `WSO`, `ANGELS`, `RES-Q`, `CT`, `CTA`, `CTP`, `MRI`, `DSA`, `IVT`, `EVT`, `TCD`, `TOAST`, `NIHSS`, `mRS`, `PiCCO`, `POCUS`...). Không viết hoa từng chữ cái đầu kiểu tiếng Anh (*Title Case*).
- **Chuẩn hóa thuật ngữ y khoa thực hành:** Dùng **chảy máu não** (không dùng *xuất huyết não*), **sau giai đoạn cấp** (không viết tắt *sau cấp*), **giãn** (không viết *dãn*), **xẹp / đè dẹt** (tuyệt đối không viết *bẹp / đè bẹp*), **ứ khí**, **trống âm / giảm âm / tăng âm**, **sốc tim**, **quy trình / phác đồ** (không dùng *giao thức*), **vữa xơ mạch máu lớn (LAA)**, **nhồi máu vùng giáp ranh**, **đáp ứng bù dịch vs. dung nạp dịch**.
- **Loại bỏ 100% giọng điệu AI cường điệu:** Không dùng các từ *"vũ khí tối thượng", "thần thánh", "sát thủ thầm lặng", "đột phá vô song", "tuyệt hảo"*.
