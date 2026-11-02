---
name: vn-medical-translation-studio
description: >-
  Chuẩn hóa văn phong dịch thuật, hiệu đính và chuyển thể học thuật y khoa tiếng
  Việt theo phong cách lâm sàng của BS. Nguyễn Trần Minh Chiến, đồng thời kết nối
  trực tiếp từ bản dịch bài báo quốc tế (NEJM, Lancet, JACC, Stroke, ESICM, ESO,
  ESVS) hoặc chương sách giáo khoa (Braunwald, Katzung, Cambridge Acute Stroke
  Care) sang Poster hội nghị khổ ngang, Tờ rơi A4 2 mặt và Slide báo cáo HNKH.
---

# Dịch thuật & chuyển thể ấn phẩm y khoa tiếng Việt (Clinical Translation & Publication Studio)

## Overview

Kỹ năng này tích hợp toàn bộ hệ thống quy chuẩn dịch thuật học thuật lâm sàng của **BS. Nguyễn Trần Minh Chiến** (`vn-medical-translation`) với quy trình chuyển thể trực tiếp từ văn bản y học tiếng Anh sang 3 định dạng xuất bản học thuật tiếng Việt:
1. **Bản dịch học thuật đầy đủ (Full-text Clinical Translation):** Tạp chí quốc tế (*JACC, NEJM, Lancet Neurology, Stroke, Intensive Care Medicine*), Guideline (*ESICM, AHA/ASA, ESO, ESVS, ESC*), sách giáo khoa (*Braunwald, Katzung, Acute Stroke Care Cambridge, Stroke Rehabilitation Clinician Handbook*) kèm hệ thống chú thích chuyên môn trong ngoặc nhọn `{...}`.
2. **Chuyển thể sang Poster hội nghị khổ ngang ($120 \times 90\text{ cm}$):** Chắt lọc từ bài báo/đề tài sang cấu trúc đa giác trung tâm (*CAS in Brain Health* / Davies et al., 2024).
3. **Chuyển thể sang Bộ Slide bài giảng / HNKH ($16:9$) & Tờ rơi lâm sàng A4 2 mặt ($210 \times 297\text{ mm}$).**

## Dependencies

- **`vn-medical-translation`** (`C:\Users\Thinkpad T14 gen 2\.gemini\config\skills\vn-medical-translation\SKILL.md`): Hệ quy chiếu gốc về chính tả **Sentence-case**, khử câu bị động tiếng Anh, từ nối biện luận và từ điển thuật ngữ Hồi sức – Đột quỵ – Tim mạch.
- **`medical-poster-designer`**: Thiết kế và kết xuất Poster khổ ngang $120 \times 90\text{ cm}$ & Tờ rơi A4 2 mặt.
- **`medical-slide-designer`**: Thiết kế và kết xuất Slide thuyết trình $16:9$ kèm Speaker Notes.

## Quick Start

1. **Khi dịch thuật bài báo / sách giáo khoa / guideline y khoa:**
   - Lập bảng ánh xạ thuật ngữ (Glossary Mapping) ngay từ đầu: lần đầu xuất hiện dịch đầy đủ kèm chữ viết tắt trong ngoặc đơn `(...)`, các lần sau dùng chữ viết tắt.
   - Chuyển câu bị động tiếng Anh (*"It was shown that..."*, *"The use of X was associated with..."*) sang chủ động tự nhiên (*"Người ta thấy rằng..."*, *"Việc dùng X đi kèm với..."*).
   - Chủ động bổ sung **chú thích chuyên môn của người dịch trong ngoặc nhọn `{...}`** để giải thích định luật sinh lý, định khu giải phẫu thần kinh hoặc mẹo chẩn đoán phân biệt tại giường (xem 10 mẫu chuẩn tại [references/translation_corpus_examples.md](./references/translation_corpus_examples.md)).
2. **Khi dịch & chuyển thể đồng thời sang Poster hoặc Slide:**
   - Thực hiện dịch chuẩn hóa các chỉ tiêu chính (`Primary Endpoint`), tỉ suất chênh hiệu chỉnh (`aOR`), tỉ số nguy cơ hiệu chỉnh (`aRR`), khoảng tin cậy `95% CI` và giá trị `p`.
   - Đưa các mệnh đề định lượng ngắn gọn lên **Poster khổ ngang** hoặc **Mặt Slide $16:9$**, và đưa phần lập luận phân tích cơ chế bệnh sinh (`Thứ nhất... Thứ hai... Và cuối cùng...`) vào **Tờ rơi A4** hoặc **Speaker Notes**.

## Workflow

### Bước 1 — Chuẩn hóa Chính tả Sentence-case & Thuật ngữ Chuyên ngành
- **Quy tắc Sentence-case tuyệt đối:** Chỉ viết hoa chữ cái đầu tiên của tiêu đề/đề mục và các danh từ riêng, tên người (`Broca`, `Wernicke`, `Wallenberg`, `Heubner`), hoặc từ viết tắt quốc tế (`ICU`, `PiCCO`, `TPTD`, `GEDVI`, `EVLWI`, `LAA`, `ICAD`, `CEA`, `CAS`, `IVT`, `EVT`).
- **Chuẩn hóa từ vựng bắt buộc:**
  - Dùng **giãn** (không viết *dãn*).
  - Dùng **xẹp** hoặc **đè dẹt / ép dẹt** (tuyệt đối không viết *bẹp / bẹp phổi / đè bẹp*).
  - Dùng **ứ khí** (không viết *bóng khí COPD / chướng khí*).
  - Dùng **trống âm / giảm âm / tăng âm** (không viết *rỗng âm / không âm*).
  - Dùng **sốc tim** (không viết *choáng tim*).
  - Dùng **quy trình / phác đồ** (không viết *giao thức*).
  - Phân biệt rõ **đáp ứng bù dịch (fluid responsiveness)** và **dung nạp dịch (fluid tolerance)**.

### Bước 2 — Chuyển ngữ Biện luận & Chèn Chú thích Ngoặc nhọn `{...}`
- Sử dụng hệ thống từ nối học thuật sắc sảo: *"Hơn hết,"*, *"Tuy vậy,"*, *"Mặc dù vậy,"*, *"Trái lại,"*, *"Ở chiều ngược lại,"*, *"Nghịch lý thay,"*, *"Chính vì vậy,"*.
- Chuẩn hóa dịch mức độ khuyến cáo trong Guideline quốc tế:
  - *"We recommend that..."* $\rightarrow$ **`"Chúng tôi khuyến nghị rằng..."`** hoặc **`"Chúng tôi khuyên rằng..."`**
  - *"We suggest that..."* $\rightarrow$ **`"Chúng tôi gợi ý rằng..."`**
  - *"We do not recommend routine..."* $\rightarrow$ **`"Chúng tôi không khuyến nghị [thực hiện] thường quy..."`**

### Bước 3 — Kiểm định Chất lượng Cuối cùng (Anti-AI Tone QA)
- Quét và xóa bỏ 100% các tính từ kịch tính hóa kiểu dịch máy (*"vũ khí tối thượng", "thần thánh", "sát thủ thầm lặng", "chết người", "đột phá vô song", "Trong bức tranh toàn cảnh..."*).

## Common Mistakes

1. **Lẫn lộn ngoặc đơn `(...)` và ngoặc nhọn `{...}`:** Ngoặc đơn `(...)` chỉ dùng cho nội dung có sẵn trong nguyên bản tiếng Anh hoặc giải nghĩa chữ viết tắt/tên thử nghiệm lâm sàng; mọi lời giảng giải bổ sung của người dịch bắt buộc đặt trong ngoặc nhọn `{...}`.
2. **Viết hoa danh từ giải phẫu giữa câu:** Các cụm từ như `thất trái`, `động mạch cảnh trong`, `động mạch não giữa`, `thùy đảo`, `nhân đậu`, `bệnh nhân` phải viết thường khi đứng giữa câu.
