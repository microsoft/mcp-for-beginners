# MCP Java Client - Demo Máy Tính

Dự án này minh họa cách tạo một client Java kết nối và tương tác với server MCP (Model Context Protocol). Trong ví dụ này, chúng ta sẽ kết nối với server máy tính từ Chương 01 và thực hiện các phép toán khác nhau.

## Yêu Cầu

Trước khi chạy client này, bạn cần:

1. **Khởi động Server Máy Tính** từ Chương 01:
   - Điều hướng đến thư mục server máy tính: `03-GettingStarted/01-first-server/solution/java/`
   - Xây dựng và chạy server máy tính:
     ```cmd
     cd ..\01-first-server\solution\java
     .\mvnw clean install -DskipTests
     java -jar target\calculator-server-0.0.1-SNAPSHOT.jar
     ```
   - Server sẽ chạy tại `http://localhost:8080`

2. Cài đặt **Java 21 trở lên** trên hệ thống của bạn
3. **Maven** (đã bao gồm qua Maven Wrapper)

## SDKClient là gì?

`SDKClient` là một ứng dụng Java minh họa cách:
- Kết nối tới server MCP sử dụng giao thức Server-Sent Events (SSE)
- Liệt kê các công cụ có sẵn từ server
- Gọi các hàm máy tính từ xa
- Xử lý phản hồi và hiển thị kết quả

## Cách Hoạt Động

Client sử dụng framework Spring AI MCP để:

1. **Thiết lập kết nối**: Tạo một client WebFlux SSE để kết nối với server máy tính
2. **Khởi tạo client**: Thiết lập MCP client và thiết lập kết nối
3. **Khám phá công cụ**: Liệt kê tất cả các phép toán máy tính có sẵn
4. **Thực thi phép toán**: Gọi các hàm toán học với dữ liệu mẫu
5. **Hiển thị kết quả**: Trình bày kết quả của từng phép tính

## Cấu Trúc Dự Án

```
src/
└── main/
    └── java/
        └── com/
            └── microsoft/
                └── mcp/
                    └── sample/
                        └── client/
                            └── SDKClient.java    # Main client implementation
```

## Các Thư Viện Chính

Dự án sử dụng các thư viện chính sau:

```xml
<dependency>
    <groupId>org.springframework.ai</groupId>
    <artifactId>spring-ai-starter-mcp-server-webflux</artifactId>
</dependency>
```

Thư viện này cung cấp:
- `McpClient` - Giao diện client chính
- `WebFluxSseClientTransport` - Giao thức SSE cho giao tiếp web
- Các schema và kiểu request/response của giao thức MCP

## Xây Dựng Dự Án

Xây dựng dự án bằng Maven wrapper:

```cmd
.\mvnw clean install
```

## Chạy Client

```cmd
java -jar .\target\calculator-client-0.0.1-SNAPSHOT.jar
```

**Lưu ý**: Đảm bảo server máy tính đang chạy tại `http://localhost:8080` trước khi thực hiện các lệnh này.

## Client Thực Hiện Những Gì

Khi chạy client, nó sẽ:

1. **Kết nối** tới server máy tính tại `http://localhost:8080`
2. **Liệt kê công cụ** - Hiển thị tất cả các phép toán máy tính có sẵn
3. **Thực hiện các phép tính**:
   - Cộng: 5 + 3 = 8
   - Trừ: 10 - 4 = 6
   - Nhân: 6 × 7 = 42
   - Chia: 20 ÷ 4 = 5
   - Lũy thừa: 2^8 = 256
   - Căn bậc hai: √16 = 4
   - Giá trị tuyệt đối: |-5.5| = 5.5
   - Trợ giúp: Hiển thị các phép toán có sẵn

## Kết Quả Mong Đợi

```
Available Tools = ListToolsResult[tools=[Tool[name=add, description=Add two numbers together, ...], ...]]
Add Result = CallToolResult[content=[TextContent[text="5,00 + 3,00 = 8,00"]], isError=false]
Subtract Result = CallToolResult[content=[TextContent[text="10,00 - 4,00 = 6,00"]], isError=false]
Multiply Result = CallToolResult[content=[TextContent[text="6,00 * 7,00 = 42,00"]], isError=false]
Divide Result = CallToolResult[content=[TextContent[text="20,00 / 4,00 = 5,00"]], isError=false]
Power Result = CallToolResult[content=[TextContent[text="2,00 ^ 8,00 = 256,00"]], isError=false]
Square Root Result = CallToolResult[content=[TextContent[text="√16,00 = 4,00"]], isError=false]
Absolute Result = CallToolResult[content=[TextContent[text="|-5,50| = 5,50"]], isError=false]
Help = CallToolResult[content=[TextContent[text="Basic Calculator MCP Service\n\nAvailable operations:\n1. add(a, b) - Adds two numbers\n2. subtract(a, b) - Subtracts the second number from the first\n..."]], isError=false]
```

**Lưu ý**: Bạn có thể thấy các cảnh báo Maven về các luồng còn tồn tại ở cuối - điều này là bình thường với các ứng dụng reactive và không phải lỗi.

## Hiểu Về Mã Nguồn

### 1. Thiết Lập Giao Thức
```java
var transport = new WebFluxSseClientTransport(WebClient.builder().baseUrl("http://localhost:8080"));
```
Tạo một giao thức SSE (Server-Sent Events) để kết nối với server máy tính.

### 2. Tạo Client
```java
var client = McpClient.sync(this.transport).build();
client.initialize();
```
Tạo một MCP client đồng bộ và khởi tạo kết nối.

### 3. Gọi Công Cụ
```java
CallToolResult resultAdd = client.callTool(new CallToolRequest("add", Map.of("a", 5.0, "b", 3.0)));
```
Gọi công cụ "add" với tham số a=5.0 và b=3.0.

## Khắc Phục Sự Cố

### Server Không Chạy
Nếu bạn gặp lỗi kết nối, hãy chắc chắn server máy tính từ Chương 01 đang chạy:
```
Error: Connection refused
```
**Giải pháp**: Khởi động server máy tính trước.

### Cổng Đã Được Sử Dụng
Nếu cổng 8080 đang bị chiếm:
```
Error: Address already in use
```
**Giải pháp**: Dừng các ứng dụng khác đang dùng cổng 8080 hoặc thay đổi cổng server.

### Lỗi Xây Dựng
Nếu gặp lỗi khi xây dựng:
```cmd
.\mvnw clean install -DskipTests
```

## Tìm Hiểu Thêm

- [Spring AI MCP Documentation](https://docs.spring.io/spring-ai/reference/api/mcp/)
- [Model Context Protocol Specification](https://modelcontextprotocol.io/)
- [Spring WebFlux Documentation](https://docs.spring.io/spring-framework/docs/current/reference/html/web-reactive.html)

**Tuyên bố từ chối trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ gốc của nó nên được coi là nguồn chính xác và đáng tin cậy. Đối với các thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp do con người thực hiện. Chúng tôi không chịu trách nhiệm về bất kỳ sự hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.