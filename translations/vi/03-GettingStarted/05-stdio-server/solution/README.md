# Giải pháp Máy chủ MCP stdio

> **⚠️ Quan trọng**: Các giải pháp này đã được cập nhật để sử dụng **giao thức stdio** theo khuyến nghị của MCP Specification 2025-06-18. Giao thức SSE (Server-Sent Events) ban đầu đã bị ngừng sử dụng.

Dưới đây là các giải pháp hoàn chỉnh để xây dựng máy chủ MCP sử dụng giao thức stdio trong từng môi trường runtime:

- [TypeScript](../../../../../03-GettingStarted/05-stdio-server/solution/typescript) - Triển khai máy chủ stdio hoàn chỉnh
- [Python](../../../../../03-GettingStarted/05-stdio-server/solution/python) - Máy chủ stdio Python với asyncio
- [.NET](../../../../../03-GettingStarted/05-stdio-server/solution/dotnet) - Máy chủ stdio .NET với dependency injection

Mỗi giải pháp minh họa:
- Cách thiết lập giao thức stdio
- Định nghĩa các công cụ máy chủ
- Xử lý thông điệp JSON-RPC đúng cách
- Tích hợp với các client MCP như Claude

Tất cả các giải pháp đều tuân theo đặc tả MCP hiện tại và sử dụng giao thức stdio được khuyến nghị để đạt hiệu suất và bảo mật tối ưu.

---

**Tuyên bố miễn trừ trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ bản địa nên được coi là nguồn thông tin chính thức. Đối với các thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp của con người. Chúng tôi không chịu trách nhiệm về bất kỳ sự hiểu lầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.