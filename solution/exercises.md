# Ngày 1 — Bài Tập & Phản Ánh
## Nền Tảng LLM API | Phiếu Thực Hành

**Thời lượng:** 1:30 giờ  
**Cấu trúc:** Lập trình cốt lõi (60 phút) → Bài tập mở rộng (30 phút)

---

## Phần 1 — Lập Trình Cốt Lõi (0:00–1:00)

Chạy các ví dụ trong Google Colab tại: https://colab.research.google.com/drive/172zCiXpLr1FEXMRCAbmZoqTrKiSkUERm?usp=sharing

Triển khai tất cả TODO trong `template.py`. Chạy `pytest tests/` để kiểm tra tiến độ.

**Điểm kiểm tra:** Sau khi hoàn thành 4 nhiệm vụ, chạy:
```bash
python template.py
```
Bạn sẽ thấy output so sánh phản hồi của GPT-4o và GPT-4o-mini.

---

## Phần 2 — Bài Tập Mở Rộng (1:00–1:30)

### Bài tập 2.1 — Độ Nhạy Của Temperature
Gọi `call_openai` với các giá trị temperature 0.0, 0.5, 1.0 và 1.5 sử dụng prompt **"Hãy kể cho tôi một sự thật thú vị về Việt Nam."**

**Bạn nhận thấy quy luật gì qua bốn phản hồi?** (2–3 câu)
> Khi temperature tăng dần từ 0.0 đến 1.5, câu trả lời chuyển từ trạng thái ổn định, ngắn gọn sang sáng tạo và ngẫu hứng. Ở mức 0.0, mô hình luôn đưa ra một kết quả duy nhất (deterministic); ở mức 1.5, văn phong trở nên bay bổng hơn nhưng bắt đầu xuất hiện dấu hiệu thiếu logic hoặc lặp từ không cần thiết.

**Bạn sẽ đặt temperature bao nhiêu cho chatbot hỗ trợ khách hàng, và tại sao?**
> Tôi sẽ đặt temperature thấp, khoảng 0.0 đến 0.3. Bởi vì chatbot hỗ trợ khách hàng ưu tiên sự chính xác, nhất quán và đáng tin cậy hơn là sự sáng tạo; việc giữ temperature thấp giúp giảm thiểu tình trạng "ảo giác" (hallucination) khi cung cấp thông tin sản phẩm hoặc chính sách.
---

### Bài tập 2.2 — Đánh Đổi Chi Phí
Xem xét kịch bản: 10.000 người dùng hoạt động mỗi ngày, mỗi người thực hiện 3 lần gọi API, mỗi lần trung bình ~350 token.

**Ước tính xem GPT-4o đắt hơn GPT-4o-mini bao nhiêu lần cho workload này:**
> Dựa trên bảng giá trong code: GPT-4o có giá 0.010 USD/1k tokens và GPT-4o-mini là 0.0006 USD/1k tokens. Với cùng một khối lượng công việc (10.5 triệu tokens/ngày), GPT-4o sẽ đắt hơn GPT-4o-mini khoảng 16.67 lần ($0.010 / 0.0006 = 16.666...$).

**Mô tả một trường hợp mà chi phí cao hơn của GPT-4o là xứng đáng, và một trường hợp GPT-4o-mini là lựa chọn tốt hơn:**
> *GPT-4o xứng đáng: Khi cần thực hiện các tác vụ suy luận phức tạp, phân tích dữ liệu chuyên sâu hoặc giải quyết các bài toán logic/lập trình khó mà các mô hình nhỏ thường mắc lỗi.
*GPT-4o-mini tốt hơn: Khi cần xử lý các tác vụ đơn giản với số lượng lớn (High-volume) như phân loại cảm xúc (sentiment analysis), tóm tắt văn bản ngắn, hoặc dịch thuật cơ bản để tối ưu chi phí vận hành.

---

### Bài tập 2.3 — Trải Nghiệm Người Dùng với Streaming
**Streaming quan trọng nhất trong trường hợp nào, và khi nào thì non-streaming lại phù hợp hơn?** (1 đoạn văn)
> Streaming đóng vai trò sống còn trong các ứng dụng chatbot trực tiếp (như ChatGPT), nơi giảm thiểu "độ trễ cảm nhận" (Perceived Latency) là ưu tiên hàng đầu; người dùng thấy chữ hiện ra ngay lập tức thay vì phải đợi cả block văn bản dài. Ngược lại, non-streaming phù hợp hơn cho các tác vụ xử lý hậu trường (backend processing), tích hợp API để trích xuất dữ liệu có cấu trúc (JSON), hoặc khi cần thực hiện các bước kiểm tra chất lượng toàn bộ câu trả lời trước khi hiển thị cho người dùng.


## Danh Sách Kiểm Tra Nộp Bài
- [x ] Tất cả tests pass: `pytest tests/ -v`
- [x] `call_openai` đã triển khai và kiểm thử
- [x] `call_openai_mini` đã triển khai và kiểm thử
- [x] `compare_models` đã triển khai và kiểm thử
- [x] `streaming_chatbot` đã triển khai và kiểm thử
- [x] `retry_with_backoff` đã triển khai và kiểm thử
- [x] `batch_compare` đã triển khai và kiểm thử
- [x] `format_comparison_table` đã triển khai và kiểm thử
- [x] `exercises.md` đã điền đầy đủ
- [x] Sao chép bài làm vào folder `solution` và đặt tên theo quy định 
