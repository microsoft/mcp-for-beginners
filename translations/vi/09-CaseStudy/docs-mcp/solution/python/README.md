# Trình Tạo Kế Hoạch Học Tập với Chainlit & Microsoft Learn Docs MCP

## Yêu cầu trước

- Python 3.8 hoặc cao hơn
- pip (trình quản lý gói Python)
- Kết nối Internet để truy cập máy chủ Microsoft Learn Docs MCP

## Cài đặt

1. Clone kho lưu trữ này hoặc tải xuống các tệp dự án.
2. Cài đặt các thư viện cần thiết:

   ```bash
   pip install -r requirements.txt
   ```

## Sử dụng

### Kịch bản 1: Truy vấn đơn giản tới Docs MCP
Một ứng dụng dòng lệnh kết nối với máy chủ Docs MCP, gửi truy vấn và hiển thị kết quả.

1. Chạy script:
   ```bash
   python scenario1.py
   ```
2. Nhập câu hỏi về tài liệu của bạn vào dòng lệnh.

### Kịch bản 2: Trình Tạo Kế Hoạch Học Tập (Ứng dụng Web Chainlit)
Một giao diện web (sử dụng Chainlit) cho phép người dùng tạo kế hoạch học tập cá nhân hóa theo tuần cho bất kỳ chủ đề kỹ thuật nào.

1. Khởi động ứng dụng Chainlit:
   ```bash
   chainlit run scenario2.py
   ```
2. Mở URL cục bộ được cung cấp trong terminal của bạn (ví dụ: http://localhost:8000) trên trình duyệt.
3. Trong cửa sổ chat, nhập chủ đề học tập và số tuần bạn muốn học (ví dụ: "Chứng chỉ AI-900, 8 tuần").
4. Ứng dụng sẽ phản hồi với kế hoạch học tập theo tuần, bao gồm các liên kết đến tài liệu Microsoft Learn liên quan.

**Các biến môi trường cần thiết:**

Để sử dụng Kịch bản 2 (ứng dụng web Chainlit với Azure OpenAI), bạn cần thiết lập các biến môi trường sau trong tệp `.env` trong thư mục `python`:

```
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=
AZURE_OPENAI_API_KEY=
AZURE_OPENAI_ENDPOINT=
AZURE_OPENAI_API_VERSION=
```

Điền các giá trị này với thông tin chi tiết về tài nguyên Azure OpenAI của bạn trước khi chạy ứng dụng.

> [!TIP]
> Bạn có thể dễ dàng triển khai các mô hình của riêng mình bằng [Azure AI Foundry](https://ai.azure.com/).

### Kịch bản 3: Tích hợp Docs MCP trong VS Code

Thay vì chuyển đổi giữa các tab trình duyệt để tìm kiếm tài liệu, bạn có thể mang Microsoft Learn Docs trực tiếp vào VS Code bằng máy chủ MCP. Điều này cho phép bạn:
- Tìm kiếm và đọc tài liệu ngay trong VS Code mà không cần rời khỏi môi trường lập trình.
- Tham khảo tài liệu và chèn liên kết trực tiếp vào README hoặc các tệp khóa học.
- Sử dụng GitHub Copilot và MCP cùng nhau để có một quy trình làm việc tài liệu được hỗ trợ bởi AI liền mạch.

**Ví dụ về trường hợp sử dụng:**
- Nhanh chóng thêm liên kết tham khảo vào README khi viết tài liệu khóa học hoặc dự án.
- Sử dụng Copilot để tạo mã và MCP để tìm và trích dẫn tài liệu liên quan ngay lập tức.
- Tập trung trong trình soạn thảo và tăng năng suất.

> [!IMPORTANT]
> Đảm bảo bạn có một tệp cấu hình [`mcp.json`](../../../../../../09-CaseStudy/docs-mcp/solution/scenario3/mcp.json) hợp lệ trong không gian làm việc của mình (vị trí là `.vscode/mcp.json`).

## Tại sao sử dụng Chainlit cho Kịch bản 2?

Chainlit là một framework mã nguồn mở hiện đại để xây dựng các ứng dụng web hội thoại. Nó giúp dễ dàng tạo giao diện người dùng dựa trên chat kết nối với các dịch vụ backend như máy chủ Microsoft Learn Docs MCP. Dự án này sử dụng Chainlit để cung cấp một cách đơn giản và tương tác nhằm tạo kế hoạch học tập cá nhân hóa theo thời gian thực. Bằng cách tận dụng Chainlit, bạn có thể nhanh chóng xây dựng và triển khai các công cụ dựa trên chat giúp tăng cường năng suất và học tập.

## Ứng dụng này làm gì?

Ứng dụng này cho phép người dùng tạo kế hoạch học tập cá nhân hóa chỉ bằng cách nhập chủ đề và thời gian học. Ứng dụng sẽ phân tích đầu vào của bạn, truy vấn máy chủ Microsoft Learn Docs MCP để lấy nội dung liên quan, và tổ chức kết quả thành một kế hoạch học tập theo tuần. Các gợi ý cho từng tuần sẽ được hiển thị trong cửa sổ chat, giúp bạn dễ dàng theo dõi và thực hiện. Tích hợp này đảm bảo bạn luôn nhận được các tài nguyên học tập mới nhất và phù hợp nhất.

## Các truy vấn mẫu

Hãy thử các truy vấn sau trong cửa sổ chat để xem cách ứng dụng phản hồi:

- `Chứng chỉ AI-900, 8 tuần`
- `Học Azure Functions, 4 tuần`
- `Azure DevOps, 6 tuần`
- `Kỹ thuật dữ liệu trên Azure, 10 tuần`
- `Kiến thức cơ bản về bảo mật của Microsoft, 5 tuần`
- `Power Platform, 7 tuần`
- `Dịch vụ AI của Azure, 12 tuần`
- `Kiến trúc đám mây, 9 tuần`

Những ví dụ này minh họa tính linh hoạt của ứng dụng đối với các mục tiêu và khung thời gian học tập khác nhau.

## Tham khảo

- [Tài liệu Chainlit](https://docs.chainlit.io/)
- [Tài liệu MCP](https://github.com/MicrosoftDocs/mcp)

---

**Tuyên bố miễn trừ trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc sự không chính xác. Tài liệu gốc bằng ngôn ngữ bản địa nên được coi là nguồn tham khảo chính thức. Đối với các thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp từ con người. Chúng tôi không chịu trách nhiệm cho bất kỳ sự hiểu lầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.