# VN Medical Studio Plugin (`vn-medical-studio`)

Bộ công cụ (Plugin) tích hợp chuyên biệt dành cho bác sĩ lâm sàng, giảng viên y khoa và nhà nghiên cứu, kết hợp 3 năng lực cốt lõi trong một hệ sinh thái thống nhất:

1. **`medical-poster-designer` — Thiết kế Poster Hội nghị Khổ ngang ($120 \times 90\text{ cm}$) & Tờ rơi A4 2 mặt ($210 \times 297\text{ mm}$):**
   - Áp dụng tiêu chuẩn thiết kế poster khoa học quốc tế của **Davies NA, Deutz NE, Delzenne N, Lobo DN** (*Presentation and publication skills: How to prepare a scientific poster*, *Clinical Nutrition ESPEN*, 2024;63:457–461, DOI: `10.1016/j.clnesp.2024.06.056`).
   - Cung cấp 2 kiến trúc Poster khổ ngang chuẩn in ấn:
     - **Version 2 (Kiến trúc đa giác trung tâm kiểu *CAS in Brain Health* – Đại học Bern tại EAN Congress):** Nổi bật tiêu đề chính giữa (`88pt–94pt`), chuỗi 8 thẻ học phần/kết quả trắng nổi (Floating Cards) vắt ngang ranh giới khối màu, cùng khối Đối tượng dự tuyển / Kết luận chính xếp ngang rõ nét.
     - **Version 1 (Kiến trúc 3 cột cân đối khổ ngang):** Dải Hero vát chéo kèm 4 chỉ số dịch tễ/thống kê thực chứng và 3 cột nội dung tự động cân bằng chiều cao (`flex: 1`).
   - Tự động tách các nội dung diễn giải dài sang **Tờ rơi A4 2 mặt ($210 \times 297\text{ mm}$)** và kiểm định 100% nguyên liệu hình ảnh thực tế (loại bỏ ảnh ngoại lai từ mục *"Bài viết khác"*, ảnh AI giả tạo và lỗi cắt cúp ảnh).

2. **`medical-slide-designer` — Thiết kế Slide Bài giảng Lâm sàng, Quy trình Kỹ thuật (SOP) & Báo cáo HNKH ($16:9$):**
   - Kiến trúc Slide 2 tầng:
     - **Tầng 1 (Trên mặt Slide $16:9$):** Tiêu đề mang thông điệp định lượng chuẩn Sentence-case, thẻ chỉ số lâm sàng, bảng đối chiếu thử nghiệm và hộp cảnh báo cạm bẫy (*Pitfalls*).
     - **Tầng 2 (Speaker Notes):** Lời giảng giải thích cơ chế bệnh sinh chuyên sâu và phân tích thử nghiệm lâm sàng (bật/tắt trực tiếp bằng phím `N` hoặc xuất PDF).

3. **`vn-medical-translation-studio` — Dịch thuật & Biên soạn Y khoa Học thuật (Phong cách BS. Nguyễn Trần Minh Chiến):**
   - Chuẩn hóa chính tả **Sentence-case** tuyệt đối, khử cấu trúc câu bị động tiếng Anh, hệ thống từ nối biện luận sắc sảo, từ điển thuật ngữ chuẩn Hồi sức – Đột quỵ – Tim mạch và kỹ thuật chú thích lâm sàng trong ngoặc nhọn `{...}`.

---

## Cấu trúc Thư mục Plugin

```text
vn-medical-studio/
├── plugin.json
├── README.md
├── assets/
│   └── logo.svg
├── rules/
│   └── AGENTS.md
└── skills/
    ├── medical-poster-designer/
    │   ├── SKILL.md
    │   ├── references/
    │   │   └── davies_2024_poster_guidelines.md
    │   ├── scripts/
    │   │   └── render_poster_pdf.py
    │   └── templates/
    │       ├── poster_landscape_cas_ver2.html
    │       ├── poster_landscape_3col_ver1.html
    │       └── flyer_a4_2sided.html
    ├── medical-slide-designer/
    │   ├── SKILL.md
    │   └── templates/
    │       └── slide_deck_16x9_clinical.html
    └── vn-medical-translation-studio/
        ├── SKILL.md
        └── references/
            └── translation_corpus_examples.md
```
