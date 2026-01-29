# Bảo mật MCP nâng cao với Azure Content Safety

Azure Content Safety cung cấp nhiều công cụ mạnh mẽ giúp tăng cường bảo mật cho các triển khai MCP của bạn:

## Prompt Shields

AI Prompt Shields của Microsoft mang lại khả năng bảo vệ vững chắc chống lại các cuộc tấn công chèn lệnh trực tiếp và gián tiếp thông qua:

1. **Phát hiện nâng cao**: Sử dụng máy học để nhận diện các chỉ dẫn độc hại được nhúng trong nội dung.
2. **Spotlighting**: Biến đổi văn bản đầu vào giúp hệ thống AI phân biệt giữa chỉ dẫn hợp lệ và dữ liệu bên ngoài.
3. **Dấu phân cách và đánh dấu dữ liệu**: Đánh dấu ranh giới giữa dữ liệu tin cậy và không tin cậy.
4. **Tích hợp Content Safety**: Hoạt động cùng Azure AI Content Safety để phát hiện các nỗ lực jailbreak và nội dung có hại.
5. **Cập nhật liên tục**: Microsoft thường xuyên cập nhật các cơ chế bảo vệ để đối phó với các mối đe dọa mới.

## Triển khai Azure Content Safety với MCP

Phương pháp này cung cấp bảo vệ đa lớp:
- Quét đầu vào trước khi xử lý
- Xác thực đầu ra trước khi trả về
- Sử dụng danh sách chặn cho các mẫu độc hại đã biết
- Tận dụng các mô hình content safety được Azure cập nhật liên tục

## Tài nguyên Azure Content Safety

Để tìm hiểu thêm về cách triển khai Azure Content Safety với các máy chủ MCP của bạn, hãy tham khảo các tài nguyên chính thức sau:

1. [Azure AI Content Safety Documentation](https://learn.microsoft.com/azure/ai-services/content-safety/) - Tài liệu chính thức về Azure Content Safety.
2. [Prompt Shield Documentation](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/prompt-shield) - Hướng dẫn cách ngăn chặn các cuộc tấn công chèn lệnh.
3. [Content Safety API Reference](https://learn.microsoft.com/rest/api/contentsafety/) - Tham khảo chi tiết API để triển khai Content Safety.
4. [Quickstart: Azure Content Safety with C#](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-csharp) - Hướng dẫn nhanh triển khai sử dụng C#.
5. [Content Safety Client Libraries](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-client-libraries-rest-api) - Thư viện client cho nhiều ngôn ngữ lập trình.
6. [Detecting Jailbreak Attempts](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection) - Hướng dẫn cụ thể về phát hiện và ngăn chặn các nỗ lực jailbreak.
7. [Best Practices for Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/best-practices) - Các thực hành tốt nhất để triển khai content safety hiệu quả.

Để triển khai chi tiết hơn, xem hướng dẫn [Azure Content Safety Implementation guide](./azure-content-safety-implementation.md).

**Tuyên bố từ chối trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ gốc của nó nên được coi là nguồn chính xác và đáng tin cậy. Đối với các thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp do con người thực hiện. Chúng tôi không chịu trách nhiệm về bất kỳ sự hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.