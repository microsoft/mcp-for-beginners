# Thực hiện Thực tiễn

[![Cách Xây dựng, Kiểm tra và Triển khai Ứng dụng MCP với Các Công cụ và Quy trình Thực tế](../../../translated_images/vi/05.64bea204e25ca891.webp)](https://youtu.be/vCN9-mKBDfQ)

_(Nhấp vào hình ảnh trên để xem video của bài học này)_

Việc thực hiện thực tế là nơi sức mạnh của Giao thức Ngữ cảnh Mô hình (MCP) trở nên rõ ràng. Mặc dù việc hiểu lý thuyết và kiến trúc đằng sau MCP là quan trọng, giá trị thực sự xuất hiện khi bạn áp dụng các khái niệm này để xây dựng, kiểm tra và triển khai các giải pháp giải quyết các vấn đề trong thế giới thực. Chương này nối liền khoảng cách giữa kiến thức khái niệm và phát triển thực hành, hướng dẫn bạn qua quá trình đưa các ứng dụng dựa trên MCP vào cuộc sống.

Dù bạn đang phát triển trợ lý thông minh, tích hợp AI vào quy trình kinh doanh, hay xây dựng công cụ tùy chỉnh cho xử lý dữ liệu, MCP cung cấp nền tảng linh hoạt. Thiết kế không phụ thuộc ngôn ngữ và các SDK chính thức cho các ngôn ngữ lập trình phổ biến giúp MCP dễ tiếp cận với nhiều nhà phát triển. Bằng cách tận dụng những SDK này, bạn có thể nhanh chóng tạo nguyên mẫu, lặp lại và mở rộng giải pháp trên các nền tảng và môi trường khác nhau.

Trong các phần sau, bạn sẽ tìm thấy các ví dụ thực tế, mã mẫu và chiến lược triển khai thể hiện cách thực hiện MCP trong C#, Java với Spring, TypeScript, JavaScript và Python. Bạn cũng sẽ học cách gỡ lỗi và kiểm tra các máy chủ MCP của mình, quản lý API, và triển khai giải pháp lên đám mây bằng Azure. Những tài nguyên thực hành này được thiết kế để tăng tốc quá trình học tập và giúp bạn tự tin xây dựng các ứng dụng MCP mạnh mẽ, sẵn sàng cho môi trường sản xuất.

## Tổng quan

Bài học này tập trung vào các khía cạnh thực tiễn của việc triển khai MCP trên nhiều ngôn ngữ lập trình. Chúng ta sẽ khám phá cách sử dụng SDK MCP trong C#, Java với Spring, TypeScript, JavaScript, và Python để xây dựng các ứng dụng mạnh mẽ, gỡ lỗi và kiểm tra các máy chủ MCP, cũng như tạo các tài nguyên, câu lệnh hướng dẫn và công cụ có thể tái sử dụng.

## Mục tiêu học tập

Kết thúc bài học này, bạn sẽ có khả năng:

- Triển khai giải pháp MCP sử dụng SDK chính thức trong nhiều ngôn ngữ lập trình
- Gỡ lỗi và kiểm tra các máy chủ MCP một cách có hệ thống
- Tạo và sử dụng các tính năng của máy chủ (Tài nguyên, Câu lệnh hướng dẫn, và Công cụ)
- Thiết kế các quy trình MCP hiệu quả cho các nhiệm vụ phức tạp
- Tối ưu hóa các triển khai MCP về hiệu suất và độ tin cậy

## Tài nguyên SDK chính thức

Giao thức Ngữ cảnh Mô hình cung cấp các SDK chính thức cho nhiều ngôn ngữ (theo [MCP Specification 2025-11-25](https://spec.modelcontextprotocol.io/specification/2025-11-25/)):

- [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk)
- [Java với Spring SDK](https://github.com/modelcontextprotocol/java-sdk) **Lưu ý:** yêu cầu phụ thuộc [Project Reactor](https://projectreactor.io). (Xem [vấn đề thảo luận 246](https://github.com/orgs/modelcontextprotocol/discussions/246).)
- [TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk)
- [Python SDK](https://github.com/modelcontextprotocol/python-sdk)
- [Kotlin SDK](https://github.com/modelcontextprotocol/kotlin-sdk)
- [Go SDK](https://github.com/modelcontextprotocol/go-sdk)

## Làm việc với MCP SDKs

Phần này cung cấp các ví dụ thực tiễn về việc triển khai MCP trên nhiều ngôn ngữ lập trình. Bạn có thể tìm mã mẫu trong thư mục `samples` được tổ chức theo ngôn ngữ.

### Mẫu có sẵn

Kho lưu trữ bao gồm [các triển khai mẫu](../../../04-PracticalImplementation/samples) trong các ngôn ngữ sau:

- [C#](./samples/csharp/README.md)
- [Java với Spring](./samples/java/containerapp/README.md)
- [TypeScript](./samples/typescript/README.md)
- [JavaScript](./samples/javascript/README.md)
- [Python](./samples/python/README.md)

Mỗi mẫu trình bày các khái niệm MCP chính và các mẫu triển khai cho ngôn ngữ và hệ sinh thái cụ thể đó.

### Hướng dẫn thực tiễn

Các hướng dẫn bổ sung cho việc triển khai MCP thực tế:

- [Phân trang và Tập kết quả lớn](./pagination/README.md) - Xử lý phân trang dựa trên con trỏ cho công cụ, tài nguyên và bộ dữ liệu lớn

## Các tính năng cốt lõi của máy chủ

Máy chủ MCP có thể triển khai bất kỳ sự kết hợp nào của các tính năng sau:

### Tài nguyên

Tài nguyên cung cấp ngữ cảnh và dữ liệu để người dùng hoặc mô hình AI sử dụng:

- Kho tài liệu
- Cơ sở tri thức
- Nguồn dữ liệu có cấu trúc
- Hệ thống tập tin

### Câu lệnh hướng dẫn

Câu lệnh hướng dẫn là các thông điệp mẫu và quy trình dành cho người dùng:

- Mẫu hội thoại được định nghĩa trước
- Các kiểu tương tác có hướng dẫn
- Cấu trúc đối thoại chuyên biệt

### Công cụ

Công cụ là các chức năng mà mô hình AI thực thi:

- Tiện ích xử lý dữ liệu
- Tích hợp API bên ngoài
- Khả năng tính toán
- Chức năng tìm kiếm

## Triển khai mẫu: Triển khai C#

Kho SDK C# chính thức chứa nhiều triển khai mẫu minh họa các khía cạnh khác nhau của MCP:

- **Khách hàng MCP cơ bản**: ví dụ đơn giản cho thấy cách tạo khách hàng MCP và gọi công cụ
- **Máy chủ MCP cơ bản**: triển khai máy chủ tối thiểu với đăng ký công cụ cơ bản
- **Máy chủ MCP cao cấp**: máy chủ đầy đủ chức năng với đăng ký công cụ, xác thực và xử lý lỗi
- **Tích hợp ASP.NET**: các ví dụ minh họa tích hợp với ASP.NET Core
- **Mẫu triển khai công cụ**: nhiều mẫu khác nhau để triển khai công cụ với các mức độ phức tạp khác nhau

SDK MCP C# đang trong giai đoạn xem trước và API có thể thay đổi. Chúng tôi sẽ liên tục cập nhật blog này khi SDK phát triển.

### Tính năng chính

- [C# MCP Nuget ModelContextProtocol](https://www.nuget.org/packages/ModelContextProtocol)
- Xây dựng [Máy chủ MCP đầu tiên của bạn](https://devblogs.microsoft.com/dotnet/build-a-model-context-protocol-mcp-server-in-csharp/).

Để xem các mẫu triển khai C# đầy đủ, hãy truy cập kho mẫu SDK C# chính thức tại [đây](https://github.com/modelcontextprotocol/csharp-sdk)

## Triển khai mẫu: Triển khai Java với Spring

SDK Java với Spring cung cấp các lựa chọn triển khai MCP mạnh mẽ với các tính năng cấp doanh nghiệp.

### Tính năng chính

- Tích hợp Spring Framework
- An toàn kiểu dữ liệu mạnh mẽ
- Hỗ trợ lập trình phản ứng
- Xử lý lỗi toàn diện

Để xem mẫu triển khai Java với Spring đầy đủ, xem [mẫu Java với Spring](samples/java/containerapp/README.md) trong thư mục mẫu.

## Triển khai mẫu: Triển khai JavaScript

SDK JavaScript cung cấp cách tiếp cận nhẹ và linh hoạt cho triển khai MCP.

### Tính năng chính

- Hỗ trợ Node.js và trình duyệt
- API dựa trên Promise
- Dễ dàng tích hợp với Express và các framework khác
- Hỗ trợ WebSocket cho phát trực tiếp

Để xem mẫu triển khai JavaScript đầy đủ, xem [mẫu JavaScript](samples/javascript/README.md) trong thư mục mẫu.

## Triển khai mẫu: Triển khai Python

SDK Python cung cấp cách tiếp cận Pythonic cho triển khai MCP với tích hợp tuyệt vời cho các framework ML.

### Tính năng chính

- Hỗ trợ async/await với asyncio
- Tích hợp FastAPI
- Đăng ký công cụ đơn giản
- Tích hợp gốc với các thư viện ML phổ biến

Để xem mẫu triển khai Python đầy đủ, xem [mẫu Python](samples/python/README.md) trong thư mục mẫu.

## Quản lý API

Azure API Management là câu trả lời tuyệt vời cho câu hỏi làm thế nào chúng ta có thể bảo mật các Máy chủ MCP. Ý tưởng là đặt một phiên bản Azure API Management trước Máy chủ MCP của bạn và để nó xử lý các tính năng bạn có thể muốn như:

- giới hạn tốc độ
- quản lý token
- giám sát
- cân bằng tải
- bảo mật

### Mẫu Azure

Dưới đây là một mẫu Azure thực hiện chính xác điều đó, tức là [tạo một Máy chủ MCP và bảo mật nó bằng Azure API Management](https://github.com/Azure-Samples/remote-mcp-apim-functions-python).

Xem cách luồng ủy quyền diễn ra trong hình dưới đây:

![APIM-MCP](https://github.com/Azure-Samples/remote-mcp-apim-functions-python/blob/main/mcp-client-authorization.gif?raw=true)

Trong hình trên, xảy ra các bước sau:

- Xác thực/Ủy quyền diễn ra bằng Microsoft Entra.
- Azure API Management hoạt động như một cổng và sử dụng các chính sách để chỉ đạo và quản lý lưu lượng.
- Azure Monitor ghi lại tất cả các yêu cầu để phân tích thêm.

#### Luồng ủy quyền

Hãy xem chi tiết hơn về luồng ủy quyền:

![Sequence Diagram](https://github.com/Azure-Samples/remote-mcp-apim-functions-python/blob/main/infra/app/apim-oauth/diagrams/images/mcp-client-auth.png?raw=true)

#### Đặc tả ủy quyền MCP

Tìm hiểu thêm về [Đặc tả ủy quyền MCP](https://spec.modelcontextprotocol.io/specification/2025-11-25/basic/authorization/)

## Triển khai Máy chủ MCP từ xa lên Azure

Hãy xem liệu chúng ta có thể triển khai mẫu đã đề cập ở trên không:

1. Sao chép kho mã

    ```bash
    git clone https://github.com/Azure-Samples/remote-mcp-apim-functions-python.git
    cd remote-mcp-apim-functions-python
    ```

1. Đăng ký nhà cung cấp tài nguyên `Microsoft.App`.

   - Nếu bạn dùng Azure CLI, chạy `az provider register --namespace Microsoft.App --wait`.
   - Nếu bạn dùng Azure PowerShell, chạy `Register-AzResourceProvider -ProviderNamespace Microsoft.App`. Sau một thời gian, chạy `(Get-AzResourceProvider -ProviderNamespace Microsoft.App).RegistrationState` để kiểm tra xem việc đăng ký đã hoàn thành chưa.

1. Chạy lệnh [azd](https://aka.ms/azd) này để cấp phát dịch vụ quản lý API, ứng dụng chức năng (với mã) và tất cả các tài nguyên Azure cần thiết khác

    ```shell
    azd up
    ```

    Lệnh này sẽ triển khai tất cả các tài nguyên đám mây trên Azure

### Kiểm tra máy chủ của bạn với MCP Inspector

1. Trong **cửa sổ terminal mới**, cài đặt và chạy MCP Inspector

    ```shell
    npx @modelcontextprotocol/inspector
    ```

    Bạn sẽ thấy giao diện tương tự như:

    ![Connect to Node inspector](../../../translated_images/vi/connect.141db0b2bd05f096.webp)

1. Nhấn CTRL và nhấp để tải ứng dụng web MCP Inspector từ URL được ứng dụng hiển thị (ví dụ [http://127.0.0.1:6274/#resources](http://127.0.0.1:6274/#resources))
1. Đặt loại vận chuyển là `SSE`
1. Đặt URL tới điểm cuối SSE của Azure API Management đang chạy được hiển thị sau khi chạy `azd up` và **Kết nối**:

    ```shell
    https://<apim-servicename-from-azd-output>.azure-api.net/mcp/sse
    ```

1. **Liệt kê Công cụ**. Nhấp vào một công cụ và **Chạy Công cụ**.  

Nếu tất cả các bước đã được thực hiện đúng, bạn giờ đây đã kết nối được với máy chủ MCP và có thể gọi một công cụ.

## Máy chủ MCP cho Azure

[Remote-mcp-functions](https://github.com/Azure-Samples/remote-mcp-functions-dotnet): Bộ kho lưu trữ mẫu nhanh này dùng để xây dựng và triển khai các máy chủ MCP từ xa tùy chỉnh sử dụng Azure Functions với Python, C# .NET hoặc Node/TypeScript.

Các Mẫu cung cấp một giải pháp hoàn chỉnh cho phép nhà phát triển:

- Xây dựng và chạy cục bộ: Phát triển và gỡ lỗi máy chủ MCP trên máy tính cục bộ
- Triển khai lên Azure: Triển khai dễ dàng lên đám mây với lệnh azd up đơn giản
- Kết nối từ các khách hàng: Kết nối tới máy chủ MCP từ nhiều khách hàng khác nhau bao gồm chế độ tác vụ Copilot của VS Code và công cụ MCP Inspector

### Tính năng chính

- Bảo mật theo thiết kế: Máy chủ MCP được bảo vệ bằng khóa và HTTPS
- Các lựa chọn xác thực: Hỗ trợ OAuth sử dụng xác thực tích hợp và/hoặc API Management
- Cô lập mạng: Cho phép cô lập mạng sử dụng Azure Virtual Networks (VNET)
- Kiến trúc không máy chủ: Tận dụng Azure Functions để thực thi linh hoạt, dựa trên sự kiện
- Phát triển cục bộ: Hỗ trợ phát triển và gỡ lỗi cục bộ toàn diện
- Triển khai đơn giản: Quy trình triển khai thuận tiện lên Azure

Kho lưu trữ bao gồm tất cả các tệp cấu hình cần thiết, mã nguồn và định nghĩa hạ tầng để nhanh chóng bắt đầu với triển khai máy chủ MCP sẵn sàng cho môi trường sản xuất.

- [Azure Remote MCP Functions Python](https://github.com/Azure-Samples/remote-mcp-functions-python) - Triển khai mẫu MCP sử dụng Azure Functions với Python

- [Azure Remote MCP Functions .NET](https://github.com/Azure-Samples/remote-mcp-functions-dotnet) - Triển khai mẫu MCP sử dụng Azure Functions với C# .NET

- [Azure Remote MCP Functions Node/Typescript](https://github.com/Azure-Samples/remote-mcp-functions-typescript) - Triển khai mẫu MCP sử dụng Azure Functions với Node/TypeScript.

## Những điểm chính cần nhớ

- Các SDK MCP cung cấp công cụ theo ngôn ngữ cụ thể để triển khai các giải pháp MCP mạnh mẽ
- Quá trình gỡ lỗi và kiểm tra rất quan trọng để xây dựng ứng dụng MCP đáng tin cậy
- Mẫu câu lệnh hướng dẫn có thể tái sử dụng giúp tương tác AI nhất quán
- Các quy trình được thiết kế tốt có thể điều phối các nhiệm vụ phức tạp sử dụng nhiều công cụ khác nhau
- Triển khai giải pháp MCP đòi hỏi cân nhắc về bảo mật, hiệu suất và xử lý lỗi

## Bài tập

Thiết kế một quy trình MCP thực tế giải quyết một vấn đề trong lĩnh vực của bạn:

1. Xác định 3-4 công cụ hữu ích cho việc giải quyết vấn đề này
2. Tạo biểu đồ quy trình thể hiện cách các công cụ tương tác với nhau
3. Triển khai phiên bản cơ bản của một trong các công cụ bằng ngôn ngữ bạn ưa thích
4. Tạo một mẫu câu lệnh hướng dẫn giúp mô hình sử dụng công cụ của bạn hiệu quả

## Tài nguyên bổ sung

---

## Bước tiếp theo

Tiếp theo: [Chủ đề Nâng cao](../05-AdvancedTopics/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Tuyên bố miễn trừ trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ gốc của nó nên được xem là nguồn thông tin chính thức. Đối với những thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm về bất kỳ sự hiểu lầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->