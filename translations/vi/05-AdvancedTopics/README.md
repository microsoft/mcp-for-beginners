# Chủ đề nâng cao trong MCP

[![Advanced MCP: Secure, Scalable, and Multi-modal AI Agents](../../../translated_images/vi/06.42259eaf91fccfc6.webp)](https://youtu.be/4yjmGvJzYdY)

_(Nhấp vào hình ảnh bên trên để xem video bài học này)_

Chương này bao gồm một loạt các chủ đề nâng cao trong việc triển khai Model Context Protocol (MCP), bao gồm tích hợp đa phương thức, khả năng mở rộng, các thực hành an ninh tốt nhất và tích hợp doanh nghiệp. Những chủ đề này rất quan trọng để xây dựng các ứng dụng MCP mạnh mẽ và sẵn sàng triển khai trong sản xuất, đáp ứng nhu cầu của các hệ thống AI hiện đại.

## Tổng quan

Bài học này khám phá các khái niệm nâng cao trong việc triển khai Model Context Protocol, tập trung vào tích hợp đa phương thức, khả năng mở rộng, các thực hành an ninh tốt nhất và tích hợp doanh nghiệp. Những chủ đề này là thiết yếu để xây dựng các ứng dụng MCP có chất lượng sản xuất có thể xử lý các yêu cầu phức tạp trong môi trường doanh nghiệp.

## Mục tiêu học tập

Vào cuối bài học này, bạn sẽ có khả năng:

- Triển khai khả năng đa phương thức trong các khung MCP
- Thiết kế kiến trúc MCP có khả năng mở rộng cho các tình huống nhu cầu cao
- Áp dụng các thực hành an ninh tốt nhất phù hợp với các nguyên tắc bảo mật của MCP
- Tích hợp MCP với các hệ thống và khung AI doanh nghiệp
- Tối ưu hóa hiệu suất và độ tin cậy trong môi trường sản xuất

## Các bài học và dự án mẫu

| Link | Tiêu đề | Mô tả |
|------|-------|-------------|
| [5.1 Integration with Azure](./mcp-integration/README.md) | Tích hợp với Azure | Học cách tích hợp MCP Server của bạn trên Azure |
| [5.2 Multi modal sample](./mcp-multi-modality/README.md) | Mẫu đa phương thức MCP | Mẫu cho âm thanh, hình ảnh và phản hồi đa phương thức |
| [5.3 MCP OAuth2 sample](../../../05-AdvancedTopics/mcp-oauth2-demo) | Demo MCP OAuth2 | Ứng dụng Spring Boot tối giản trình bày OAuth2 với MCP, cả dưới dạng Authorization và Resource Server. Minh họa phát hành token an toàn, các điểm cuối được bảo vệ, triển khai Azure Container Apps, và tích hợp API Management. |
| [5.4 Root Contexts](./mcp-root-contexts/README.md) | Các ngữ cảnh gốc | Tìm hiểu thêm về ngữ cảnh gốc và cách triển khai chúng |
| [5.5 Routing](./mcp-routing/README.md) | Định tuyến | Học các loại định tuyến khác nhau |
| [5.6 Sampling](./mcp-sampling/README.md) | Lấy mẫu | Học cách làm việc với lấy mẫu |
| [5.7 Scaling](./mcp-scaling/README.md) | Mở rộng | Tìm hiểu về mở rộng |
| [5.8 Security](./mcp-security/README.md) | An ninh | Bảo mật MCP Server của bạn |
| [5.9 Web Search sample](./web-search-mcp/README.md) | Tìm kiếm Web MCP | Máy chủ và khách MCP Python tích hợp với SerpAPI cho tìm kiếm web, tin tức, sản phẩm và hỏi đáp thời gian thực. Minh họa phối hợp đa công cụ, tích hợp API bên ngoài, và xử lý lỗi mạnh mẽ. |
| [5.10 Realtime Streaming](./mcp-realtimestreaming/README.md) | Streaming | Truyền dữ liệu thời gian thực đã trở thành thiết yếu trong thế giới dữ liệu hiện nay, nơi các doanh nghiệp và ứng dụng cần truy cập thông tin ngay lập tức để ra quyết định kịp thời. |
| [5.11 Realtime Web Search](./mcp-realtimesearch/README.md) | Tìm kiếm Web | Tìm kiếm web thời gian thực như thế nào MCP biến đổi tìm kiếm web thời gian thực bằng cách cung cấp cách tiếp cận tiêu chuẩn quản lý ngữ cảnh trên các mô hình AI, công cụ tìm kiếm và ứng dụng.| 
| [5.12  Entra ID Authentication for Model Context Protocol Servers](./mcp-security-entra/README.md) | Xác thực Entra ID | Microsoft Entra ID cung cấp giải pháp quản lý định danh và truy cập dựa trên đám mây mạnh mẽ, giúp đảm bảo chỉ người dùng và ứng dụng được ủy quyền mới có thể tương tác với MCP server của bạn.|
| [5.13 Azure AI Foundry Agent Integration](./mcp-foundry-agent-integration/README.md) | Tích hợp Azure AI Foundry | Học cách tích hợp các MCP server với các agent Azure AI Foundry, cho phép phối hợp công cụ mạnh mẽ và khả năng AI doanh nghiệp với các kết nối nguồn dữ liệu bên ngoài tiêu chuẩn.|
| [5.14 Context Engineering](./mcp-contextengineering/README.md) | Kỹ thuật ngữ cảnh | Cơ hội tương lai của các kỹ thuật kỹ thuật ngữ cảnh cho các MCP server, bao gồm tối ưu hóa ngữ cảnh, quản lý ngữ cảnh động, và chiến lược kỹ thuật tạo prompt hiệu quả trong các khung MCP.|
| [5.15 MCP Custom Transport](./mcp-transport/README.md) | Giao thức Tuyến tùy chỉnh | Học cách triển khai các cơ chế giao thức tùy chỉnh cho các kịch bản giao tiếp MCP chuyên biệt.|
| [5.16 Protocol Features Deep Dive](./mcp-protocol-features/README.md) | Tính năng giao thức | Thành thạo các tính năng giao thức nâng cao bao gồm thông báo tiến trình, hủy yêu cầu, mẫu tài nguyên, và các mẫu xử lý lỗi.|
| [5.17 Adversarial Multi-Agent Reasoning](./mcp-adversarial-agents/README.md) | Tác nhân đối kháng | Sử dụng hai tác nhân với các quan điểm đối lập, chia sẻ một bộ công cụ MCP, để phát hiện ảo giác, lộ ra các trường hợp biên, và tạo ra kết quả hiệu chỉnh tốt hơn thông qua tranh luận có cấu trúc.|

> **Mới trong MCP Specification 2025-11-25**: Bản đặc tả hiện bao gồm hỗ trợ thử nghiệm cho **Tasks** (các tác vụ chạy dài có theo dõi tiến độ), **Tool Annotations** (siêu dữ liệu về hành vi công cụ để đảm bảo an toàn), **URL Mode Elicitation** (yêu cầu nội dung URL cụ thể từ khách hàng), và cải tiến **Roots** (cho quản lý ngữ cảnh không gian làm việc). Xem [MCP Specification changelog](https://spec.modelcontextprotocol.io/) để biết chi tiết đầy đủ.

## Tài liệu tham khảo bổ sung

Để có thông tin cập nhật nhất về các chủ đề MCP nâng cao, tham khảo:
- [Tài liệu MCP](https://modelcontextprotocol.io/)
- [Bản đặc tả MCP (2025-11-25)](https://spec.modelcontextprotocol.io/specification/2025-11-25/)
- [Kho GitHub](https://github.com/modelcontextprotocol)
- [OWASP MCP Top 10](https://microsoft.github.io/mcp-azure-security-guide/mcp/) - Rủi ro bảo mật và biện pháp giảm thiểu
- [Hội thảo MCP Security Summit (Sherpa)](https://azure-samples.github.io/sherpa/) - Đào tạo thực hành về bảo mật

## Những điểm chính rút ra

- Triển khai MCP đa phương thức mở rộng khả năng AI vượt ra ngoài xử lý văn bản
- Khả năng mở rộng thiết yếu cho triển khai doanh nghiệp và có thể giải quyết qua mở rộng ngang và dọc
- Các biện pháp bảo mật toàn diện bảo vệ dữ liệu và đảm bảo kiểm soát truy cập đúng đắn
- Tích hợp doanh nghiệp với các nền tảng như Azure OpenAI và Microsoft AI Foundry nâng cao khả năng MCP
- Các triển khai MCP nâng cao được hưởng lợi từ kiến trúc tối ưu và quản lý tài nguyên cẩn thận

## Bài tập

Thiết kế một triển khai MCP cấp doanh nghiệp cho một trường hợp sử dụng cụ thể:

1. Xác định các yêu cầu đa phương thức cho trường hợp sử dụng của bạn
2. Phác thảo các kiểm soát an ninh cần thiết để bảo vệ dữ liệu nhạy cảm
3. Thiết kế kiến trúc có khả năng mở rộng có thể xử lý tải khác nhau
4. Lập kế hoạch các điểm tích hợp với các hệ thống AI doanh nghiệp
5. Ghi lại các điểm nghẽn hiệu suất tiềm năng và chiến lược giảm thiểu

## Tài nguyên bổ sung

- [Tài liệu Azure OpenAI](https://learn.microsoft.com/en-us/azure/ai-services/openai/)
- [Tài liệu Microsoft AI Foundry](https://learn.microsoft.com/en-us/ai-services/)

---

## Tiếp theo là gì

Khám phá các bài học trong mô-đun này bắt đầu với: [5.1 MCP Integration](./mcp-integration/README.md)

Khi bạn đã hoàn thành mô-đun này, tiếp tục với: [Mô-đun 6: Đóng góp của cộng đồng](../06-CommunityContributions/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Tuyên bố từ chối trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể có lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ gốc của nó nên được xem là nguồn thông tin chính xác nhất. Đối với các thông tin quan trọng, khuyến nghị sử dụng dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm cho bất kỳ sự hiểu nhầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->