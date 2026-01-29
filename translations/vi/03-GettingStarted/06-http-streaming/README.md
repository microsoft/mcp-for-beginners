# Phát trực tuyến HTTPS với Giao thức Ngữ cảnh Mô hình (MCP)

Chương này cung cấp hướng dẫn toàn diện về cách triển khai phát trực tuyến an toàn, có khả năng mở rộng và thời gian thực với Giao thức Ngữ cảnh Mô hình (MCP) sử dụng HTTPS. Nội dung bao gồm động lực của phát trực tuyến, các cơ chế truyền tải có sẵn, cách triển khai HTTP có thể phát trực tuyến trong MCP, các thực hành bảo mật tốt nhất, chuyển đổi từ SSE, và hướng dẫn thực tiễn để xây dựng ứng dụng MCP phát trực tuyến của riêng bạn.

## Cơ chế truyền tải và phát trực tuyến trong MCP

Phần này khám phá các cơ chế truyền tải khác nhau có sẵn trong MCP và vai trò của chúng trong việc cung cấp khả năng phát trực tuyến cho giao tiếp thời gian thực giữa máy khách và máy chủ.

### Cơ chế truyền tải là gì?

Cơ chế truyền tải định nghĩa cách dữ liệu được trao đổi giữa máy khách và máy chủ. MCP hỗ trợ nhiều loại truyền tải để phù hợp với các môi trường và yêu cầu khác nhau:

- **stdio**: Đầu vào/đầu ra tiêu chuẩn, phù hợp cho các công cụ cục bộ và dựa trên CLI. Đơn giản nhưng không phù hợp cho web hoặc đám mây.
- **SSE (Server-Sent Events)**: Cho phép máy chủ gửi cập nhật thời gian thực đến máy khách qua HTTP. Tốt cho giao diện web, nhưng hạn chế về khả năng mở rộng và tính linh hoạt.
- **HTTP có thể phát trực tuyến**: Giao thức truyền tải hiện đại dựa trên HTTP, hỗ trợ thông báo và khả năng mở rộng tốt hơn. Được khuyến nghị cho hầu hết các kịch bản sản xuất và đám mây.

### Bảng so sánh

Hãy xem bảng so sánh dưới đây để hiểu sự khác biệt giữa các cơ chế truyền tải này:

| Truyền tải         | Cập nhật thời gian thực | Phát trực tuyến | Khả năng mở rộng | Trường hợp sử dụng         |
|--------------------|-------------------------|-----------------|------------------|---------------------------|
| stdio             | Không                  | Không           | Thấp             | Công cụ CLI cục bộ        |
| SSE               | Có                     | Có              | Trung bình       | Web, cập nhật thời gian thực |
| HTTP có thể phát trực tuyến | Có              | Có              | Cao              | Đám mây, đa máy khách     |

> **Mẹo:** Việc chọn đúng cơ chế truyền tải ảnh hưởng đến hiệu suất, khả năng mở rộng và trải nghiệm người dùng. **HTTP có thể phát trực tuyến** được khuyến nghị cho các ứng dụng hiện đại, có khả năng mở rộng và sẵn sàng cho đám mây.

Lưu ý các cơ chế truyền tải stdio và SSE đã được giới thiệu trong các chương trước và cách HTTP có thể phát trực tuyến là cơ chế truyền tải được đề cập trong chương này.

## Phát trực tuyến: Khái niệm và Động lực

Hiểu các khái niệm cơ bản và động lực đằng sau phát trực tuyến là điều cần thiết để triển khai các hệ thống giao tiếp thời gian thực hiệu quả.

**Phát trực tuyến** là một kỹ thuật trong lập trình mạng cho phép dữ liệu được gửi và nhận theo từng phần nhỏ, dễ quản lý hoặc dưới dạng chuỗi sự kiện, thay vì chờ toàn bộ phản hồi sẵn sàng. Điều này đặc biệt hữu ích cho:

- Các tệp hoặc tập dữ liệu lớn.
- Cập nhật thời gian thực (ví dụ: trò chuyện, thanh tiến trình).
- Các tính toán dài hạn mà bạn muốn thông báo cho người dùng.

Những điều cần biết về phát trực tuyến ở mức độ cao:

- Dữ liệu được gửi dần dần, không phải tất cả cùng một lúc.
- Máy khách có thể xử lý dữ liệu khi nó đến.
- Giảm độ trễ cảm nhận và cải thiện trải nghiệm người dùng.

### Tại sao sử dụng phát trực tuyến?

Các lý do để sử dụng phát trực tuyến bao gồm:

- Người dùng nhận được phản hồi ngay lập tức, không phải chỉ khi kết thúc.
- Cho phép các ứng dụng thời gian thực và giao diện người dùng phản hồi nhanh.
- Sử dụng tài nguyên mạng và tính toán hiệu quả hơn.

### Ví dụ đơn giản: Máy chủ & Máy khách HTTP phát trực tuyến

Dưới đây là một ví dụ đơn giản về cách triển khai phát trực tuyến:

#### Python

**Máy chủ (Python, sử dụng FastAPI và StreamingResponse):**

```python
from fastapi import FastAPI
from fastapi.responses import StreamingResponse
import time

app = FastAPI()

async def event_stream():
    for i in range(1, 6):
        yield f"data: Message {i}\n\n"
        time.sleep(1)

@app.get("/stream")
def stream():
    return StreamingResponse(event_stream(), media_type="text/event-stream")
```

**Máy khách (Python, sử dụng requests):**

```python
import requests

with requests.get("http://localhost:8000/stream", stream=True) as r:
    for line in r.iter_lines():
        if line:
            print(line.decode())
```

Ví dụ này minh họa một máy chủ gửi một loạt thông báo đến máy khách khi chúng sẵn sàng, thay vì chờ tất cả thông báo sẵn sàng.

**Cách hoạt động:**

- Máy chủ tạo từng thông báo khi chúng sẵn sàng.
- Máy khách nhận và in từng phần khi chúng đến.

**Yêu cầu:**

- Máy chủ phải sử dụng phản hồi phát trực tuyến (ví dụ: `StreamingResponse` trong FastAPI).
- Máy khách phải xử lý phản hồi dưới dạng luồng (`stream=True` trong requests).
- Content-Type thường là `text/event-stream` hoặc `application/octet-stream`.

#### Java

**Máy chủ (Java, sử dụng Spring Boot và Server-Sent Events):**

```java
@RestController
public class CalculatorController {

    @GetMapping(value = "/calculate", produces = MediaType.TEXT_EVENT_STREAM_VALUE)
    public Flux<ServerSentEvent<String>> calculate(@RequestParam double a,
                                                   @RequestParam double b,
                                                   @RequestParam String op) {
        
        double result;
        switch (op) {
            case "add": result = a + b; break;
            case "sub": result = a - b; break;
            case "mul": result = a * b; break;
            case "div": result = b != 0 ? a / b : Double.NaN; break;
            default: result = Double.NaN;
        }

        return Flux.<ServerSentEvent<String>>just(
                    ServerSentEvent.<String>builder()
                        .event("info")
                        .data("Calculating: " + a + " " + op + " " + b)
                        .build(),
                    ServerSentEvent.<String>builder()
                        .event("result")
                        .data(String.valueOf(result))
                        .build()
                )
                .delayElements(Duration.ofSeconds(1));
    }
}
```

**Máy khách (Java, sử dụng Spring WebFlux WebClient):**

```java
@SpringBootApplication
public class CalculatorClientApplication implements CommandLineRunner {

    private final WebClient client = WebClient.builder()
            .baseUrl("http://localhost:8080")
            .build();

    @Override
    public void run(String... args) {
        client.get()
                .uri(uriBuilder -> uriBuilder
                        .path("/calculate")
                        .queryParam("a", 7)
                        .queryParam("b", 5)
                        .queryParam("op", "mul")
                        .build())
                .accept(MediaType.TEXT_EVENT_STREAM)
                .retrieve()
                .bodyToFlux(String.class)
                .doOnNext(System.out::println)
                .blockLast();
    }
}
```

**Ghi chú triển khai Java:**

- Sử dụng ngăn xếp phản ứng của Spring Boot với `Flux` để phát trực tuyến.
- `ServerSentEvent` cung cấp phát trực tuyến sự kiện có cấu trúc với các loại sự kiện.
- `WebClient` với `bodyToFlux()` cho phép tiêu thụ phát trực tuyến phản ứng.
- `delayElements()` mô phỏng thời gian xử lý giữa các sự kiện.
- Các sự kiện có thể có loại (`info`, `result`) để máy khách xử lý tốt hơn.

### So sánh: Phát trực tuyến cổ điển và Phát trực tuyến MCP

Sự khác biệt giữa cách phát trực tuyến hoạt động theo cách "cổ điển" và cách nó hoạt động trong MCP có thể được mô tả như sau:

| Tính năng              | Phát trực tuyến HTTP cổ điển | Phát trực tuyến MCP (Thông báo) |
|------------------------|-----------------------------|---------------------------------|
| Phản hồi chính         | Chia thành từng phần        | Một lần, ở cuối                |
| Cập nhật tiến trình     | Gửi dưới dạng các phần dữ liệu | Gửi dưới dạng thông báo         |
| Yêu cầu máy khách      | Phải xử lý luồng            | Phải triển khai trình xử lý thông báo |
| Trường hợp sử dụng      | Tệp lớn, luồng token AI     | Tiến trình, nhật ký, phản hồi thời gian thực |

### Những khác biệt chính được quan sát

Ngoài ra, đây là một số khác biệt chính:

- **Mô hình giao tiếp:**
  - Phát trực tuyến HTTP cổ điển: Sử dụng mã hóa truyền tải chia thành từng phần đơn giản để gửi dữ liệu.
  - Phát trực tuyến MCP: Sử dụng hệ thống thông báo có cấu trúc với giao thức JSON-RPC.

- **Định dạng thông báo:**
  - HTTP cổ điển: Các phần văn bản thuần túy với dòng mới.
  - MCP: Các đối tượng LoggingMessageNotification có cấu trúc với siêu dữ liệu.

- **Triển khai máy khách:**
  - HTTP cổ điển: Máy khách đơn giản xử lý phản hồi phát trực tuyến.
  - MCP: Máy khách phức tạp hơn với trình xử lý thông báo để xử lý các loại thông báo khác nhau.

- **Cập nhật tiến trình:**
  - HTTP cổ điển: Tiến trình là một phần của luồng phản hồi chính.
  - MCP: Tiến trình được gửi qua các thông báo riêng biệt trong khi phản hồi chính được gửi ở cuối.

### Khuyến nghị

Dưới đây là một số khuyến nghị khi chọn giữa triển khai phát trực tuyến cổ điển (như một endpoint `/stream` mà chúng tôi đã chỉ cho bạn ở trên) và chọn phát trực tuyến qua MCP.

- **Đối với nhu cầu phát trực tuyến đơn giản:** Phát trực tuyến HTTP cổ điển đơn giản hơn để triển khai và đủ cho các nhu cầu phát trực tuyến cơ bản.

- **Đối với các ứng dụng phức tạp, tương tác:** Phát trực tuyến MCP cung cấp một cách tiếp cận có cấu trúc hơn với siêu dữ liệu phong phú và sự tách biệt giữa thông báo và kết quả cuối cùng.

- **Đối với các ứng dụng AI:** Hệ thống thông báo của MCP đặc biệt hữu ích cho các tác vụ AI dài hạn, nơi bạn muốn thông báo tiến trình cho người dùng.

## Phát trực tuyến trong MCP

Được rồi, bạn đã thấy một số khuyến nghị và so sánh về sự khác biệt giữa phát trực tuyến cổ điển và phát trực tuyến trong MCP. Hãy đi vào chi tiết chính xác cách bạn có thể tận dụng phát trực tuyến trong MCP.

Hiểu cách phát trực tuyến hoạt động trong khung MCP là điều cần thiết để xây dựng các ứng dụng phản hồi nhanh, cung cấp phản hồi thời gian thực cho người dùng trong các hoạt động dài hạn.

Trong MCP, phát trực tuyến không phải là gửi phản hồi chính theo từng phần, mà là gửi **thông báo** đến máy khách trong khi một công cụ đang xử lý yêu cầu. Những thông báo này có thể bao gồm cập nhật tiến trình, nhật ký hoặc các sự kiện khác.

### Cách hoạt động

Kết quả chính vẫn được gửi dưới dạng một phản hồi duy nhất. Tuy nhiên, các thông báo có thể được gửi dưới dạng các tin nhắn riêng biệt trong quá trình xử lý, từ đó cập nhật máy khách theo thời gian thực. Máy khách phải có khả năng xử lý và hiển thị các thông báo này.

## Thông báo là gì?

Chúng tôi đã đề cập đến "Thông báo", vậy điều đó có nghĩa là gì trong ngữ cảnh của MCP?

Thông báo là một tin nhắn được gửi từ máy chủ đến máy khách để thông báo về tiến trình, trạng thái hoặc các sự kiện khác trong một hoạt động dài hạn. Thông báo cải thiện tính minh bạch và trải nghiệm người dùng.

Ví dụ, máy khách được yêu cầu gửi một thông báo sau khi bắt tay ban đầu với máy chủ đã được thực hiện.

Một thông báo trông như sau dưới dạng tin nhắn JSON:

```json
{
  jsonrpc: "2.0";
  method: string;
  params?: {
    [key: string]: unknown;
  };
}
```

Thông báo thuộc về một chủ đề trong MCP được gọi là ["Logging"](https://modelcontextprotocol.io/specification/draft/server/utilities/logging).

Để nhật ký hoạt động, máy chủ cần kích hoạt nó như một tính năng/khả năng như sau:

```json
{
  "capabilities": {
    "logging": {}
  }
}
```

> [!NOTE]
> Tùy thuộc vào SDK được sử dụng, nhật ký có thể được kích hoạt theo mặc định hoặc bạn có thể cần kích hoạt nó rõ ràng trong cấu hình máy chủ của mình.

Có các loại thông báo khác nhau:

| Cấp độ    | Mô tả                        | Trường hợp sử dụng ví dụ         |
|-----------|------------------------------|----------------------------------|
| debug     | Thông tin gỡ lỗi chi tiết    | Điểm vào/ra của hàm             |
| info      | Thông báo thông tin chung    | Cập nhật tiến trình hoạt động   |
| notice    | Các sự kiện bình thường nhưng quan trọng | Thay đổi cấu hình             |
| warning   | Điều kiện cảnh báo           | Sử dụng tính năng đã lỗi thời   |
| error     | Điều kiện lỗi                | Lỗi hoạt động                   |
| critical  | Điều kiện nghiêm trọng       | Lỗi thành phần hệ thống         |
| alert     | Cần hành động ngay lập tức   | Phát hiện hỏng dữ liệu          |
| emergency | Hệ thống không sử dụng được  | Hệ thống hoàn toàn thất bại     |

## Triển khai Thông báo trong MCP

Để triển khai thông báo trong MCP, bạn cần thiết lập cả phía máy chủ và máy khách để xử lý cập nhật thời gian thực. Điều này cho phép ứng dụng của bạn cung cấp phản hồi ngay lập tức cho người dùng trong các hoạt động dài hạn.

### Phía máy chủ: Gửi Thông báo

Hãy bắt đầu với phía máy chủ. Trong MCP, bạn định nghĩa các công cụ có thể gửi thông báo trong khi xử lý yêu cầu. Máy chủ sử dụng đối tượng ngữ cảnh (thường là `ctx`) để gửi tin nhắn đến máy khách.

#### Python

```python
@mcp.tool(description="A tool that sends progress notifications")
async def process_files(message: str, ctx: Context) -> TextContent:
    await ctx.info("Processing file 1/3...")
    await ctx.info("Processing file 2/3...")
    await ctx.info("Processing file 3/3...")
    return TextContent(type="text", text=f"Done: {message}")
```

Trong ví dụ trên, công cụ `process_files` gửi ba thông báo đến máy khách khi xử lý từng tệp. Phương thức `ctx.info()` được sử dụng để gửi các tin nhắn thông tin.

Ngoài ra, để kích hoạt thông báo, hãy đảm bảo máy chủ của bạn sử dụng một cơ chế truyền tải phát trực tuyến (như `streamable-http`) và máy khách của bạn triển khai một trình xử lý tin nhắn để xử lý thông báo. Dưới đây là cách bạn có thể thiết lập máy chủ để sử dụng cơ chế truyền tải `streamable-http`:

```python
mcp.run(transport="streamable-http")
```

#### .NET

```csharp
[Tool("A tool that sends progress notifications")]
public async Task<TextContent> ProcessFiles(string message, ToolContext ctx)
{
    await ctx.Info("Processing file 1/3...");
    await ctx.Info("Processing file 2/3...");
    await ctx.Info("Processing file 3/3...");
    return new TextContent
    {
        Type = "text",
        Text = $"Done: {message}"
    };
}
```

Trong ví dụ .NET này, công cụ `ProcessFiles` được trang trí với thuộc tính `Tool` và gửi ba thông báo đến máy khách khi xử lý từng tệp. Phương thức `ctx.Info()` được sử dụng để gửi các tin nhắn thông tin.

Để kích hoạt thông báo trong máy chủ MCP .NET của bạn, hãy đảm bảo bạn đang sử dụng một cơ chế truyền tải phát trực tuyến:

```csharp
var builder = McpBuilder.Create();
await builder
    .UseStreamableHttp() // Enable streamable HTTP transport
    .Build()
    .RunAsync();
```

### Phía máy khách: Nhận Thông báo

Máy khách phải triển khai một trình xử lý tin nhắn để xử lý và hiển thị thông báo khi chúng đến.

#### Python

```python
async def message_handler(message):
    if isinstance(message, types.ServerNotification):
        print("NOTIFICATION:", message)
    else:
        print("SERVER MESSAGE:", message)

async with ClientSession(
   read_stream, 
   write_stream,
   logging_callback=logging_collector,
   message_handler=message_handler,
) as session:
```

Trong đoạn mã trên, hàm `message_handler` kiểm tra xem tin nhắn đến có phải là thông báo không. Nếu đúng, nó in thông báo; nếu không, nó xử lý như một tin nhắn máy chủ thông thường. Cũng lưu ý cách `ClientSession` được khởi tạo với `message_handler` để xử lý các thông báo đến.

#### .NET

```csharp
// Define a message handler
void MessageHandler(IJsonRpcMessage message)
{
    if (message is ServerNotification notification)
    {
        Console.WriteLine($"NOTIFICATION: {notification}");
    }
    else
    {
        Console.WriteLine($"SERVER MESSAGE: {message}");
    }
}

// Create and use a client session with the message handler
var clientOptions = new ClientSessionOptions
{
    MessageHandler = MessageHandler,
    LoggingCallback = (level, message) => Console.WriteLine($"[{level}] {message}")
};

using var client = new ClientSession(readStream, writeStream, clientOptions);
await client.InitializeAsync();

// Now the client will process notifications through the MessageHandler
```

Trong ví dụ .NET này, hàm `MessageHandler` kiểm tra xem tin nhắn đến có phải là thông báo không. Nếu đúng, nó in thông báo; nếu không, nó xử lý như một tin nhắn máy chủ thông thường. `ClientSession` được khởi tạo với trình xử lý tin nhắn thông qua `ClientSessionOptions`.

Để kích hoạt thông báo, hãy đảm bảo máy chủ của bạn sử dụng một cơ chế truyền tải phát trực tuyến (như `streamable-http`) và máy khách của bạn triển khai một trình xử lý tin nhắn để xử lý thông báo.

## Thông báo Tiến trình & Kịch bản

Phần này giải thích khái niệm thông báo tiến trình trong MCP, tại sao chúng quan trọng, và cách triển khai chúng bằng HTTP có thể phát trực tuyến. Bạn cũng sẽ tìm thấy một bài tập thực hành để củng cố hiểu biết của mình.

Thông báo tiến trình là các tin nhắn thời gian thực được gửi từ máy chủ đến máy khách trong các hoạt động dài hạn. Thay vì chờ toàn bộ quá trình hoàn thành, máy chủ cập nhật máy khách về trạng thái hiện tại. Điều này cải thiện tính minh bạch, trải nghiệm người dùng, và giúp gỡ lỗi dễ dàng hơn.

**Ví dụ:**

```text

"Processing document 1/10"
"Processing document 2/10"
...
"Processing complete!"

```

### Tại sao sử dụng Thông báo Tiến trình?

Thông báo tiến trình rất cần thiết vì các lý do sau:

- **Cải thiện trải nghiệm người dùng:** Người dùng thấy các cập nhật khi công việc tiến triển, không chỉ khi kết thúc.
- **Phản hồi thời gian thực:** Máy khách có thể hiển thị thanh tiến trình hoặc nhật ký, làm cho ứng dụng cảm giác phản hồi nhanh.
- **Dễ dàng gỡ lỗi và giám sát:** Nhà phát triển và người dùng có thể thấy quá trình nào có thể chậm hoặc bị kẹt.

### Cách triển khai Thông báo Tiến trình

Dưới đây là cách bạn có thể triển khai thông báo tiến trình trong MCP:

- **Trên máy chủ:** Sử dụng `ctx.info()` hoặc `ctx.log()` để gửi thông báo khi từng mục được xử lý. Điều này gửi một tin nhắn đến máy khách trước khi kết quả chính sẵn sàng.
- **Trên máy khách:** Triển khai một trình xử lý tin nhắn lắng nghe và hiển thị thông báo khi chúng đến. Trình xử lý này phân biệt giữa thông báo và kết quả cuối cùng.

**Ví dụ Máy chủ:**

#### Python

```python
@mcp.tool(description="A tool that sends progress notifications")
async def process_files(message: str, ctx: Context) -> TextContent:
    for i in range(1, 11):
        await ctx.info(f"Processing document {i}/10")
    await ctx.info("Processing complete!")
    return TextContent(type="text", text=f"Done: {message}")
```

**Ví dụ Máy khách:**

#### Python

```python
async def message_handler(message):
    if isinstance(message, types.ServerNotification):
        print("NOTIFICATION:", message)
    else:
        print("SERVER MESSAGE:", message)
```

## Cân nhắc về Bảo mật

Khi triển khai máy chủ MCP với các cơ chế truyền tải dựa trên HTTP, bảo mật trở thành một mối quan tâm hàng đầu, yêu cầu chú ý cẩn thận đến nhiều vectơ tấn công và cơ chế bảo vệ.

### Tổng quan

Bảo mật rất quan trọng khi mở máy chủ MCP qua HTTP. HTTP có thể phát trực tuyến giới thiệu các bề mặt tấn công mới và yêu cầu cấu hình cẩn thận.

### Các điểm chính

- **Xác thực Header Origin**: Luôn xác thực header `Origin` để ngăn chặn các cuộc tấn công DNS rebinding.
- **Ràng buộc Localhost**: Đối với phát triển cục bộ, ràng buộc máy chủ vào `localhost` để tránh lộ ra internet công cộng.
- **Xác thực**: Triển khai xác thực (ví dụ: API keys, OAuth) cho các triển khai sản xuất.
- **CORS**: Cấu hình chính sách Cross-Origin Resource Sharing (CORS) để hạn chế truy cập.
- **HTTPS**: Sử dụng HTTPS trong sản xuất để mã hóa lưu lượng.

### Các thực hành tốt nhất

- Không bao giờ tin tưởng các yêu cầu đến mà không xác thực.
- Ghi nhật ký và giám sát tất cả các truy cập và lỗi.
- Thường xuyên cập nhật các phụ thuộc để vá các lỗ hổng bảo mật.

### Thách thức

- Cân bằng bảo mật với sự dễ dàng phát triển.
- Đảm bảo khả năng tương thích với các môi trường máy khách khác nhau.

## Nâng cấp từ SSE lên HTTP có thể phát trực tuyến

Đối với các ứng dụng hiện đang sử dụng Server-Sent Events (SSE), việc chuyển sang HTTP có thể phát trực tuyến cung cấp các khả năng nâng cao và tính bền vững tốt hơn cho các triển khai MCP của bạn.

### Tại sao nâng cấp?
Có hai lý do thuyết phục để nâng cấp từ SSE sang Streamable HTTP:

- Streamable HTTP cung cấp khả năng mở rộng tốt hơn, tương thích hơn và hỗ trợ thông báo phong phú hơn so với SSE.
- Đây là phương thức truyền tải được khuyến nghị cho các ứng dụng MCP mới.

### Các bước chuyển đổi

Dưới đây là cách bạn có thể chuyển đổi từ SSE sang Streamable HTTP trong các ứng dụng MCP của mình:

- **Cập nhật mã máy chủ** để sử dụng `transport="streamable-http"` trong `mcp.run()`.
- **Cập nhật mã khách hàng** để sử dụng `streamablehttp_client` thay vì SSE client.
- **Triển khai một trình xử lý thông báo** trong client để xử lý các thông báo.
- **Kiểm tra tính tương thích** với các công cụ và quy trình làm việc hiện có.

### Duy trì tính tương thích

Nên duy trì tính tương thích với các client SSE hiện có trong quá trình chuyển đổi. Dưới đây là một số chiến lược:

- Bạn có thể hỗ trợ cả SSE và Streamable HTTP bằng cách chạy cả hai phương thức truyền tải trên các điểm cuối khác nhau.
- Dần dần chuyển đổi các client sang phương thức truyền tải mới.

### Thách thức

Hãy đảm bảo bạn giải quyết các thách thức sau trong quá trình chuyển đổi:

- Đảm bảo tất cả các client được cập nhật
- Xử lý sự khác biệt trong việc phân phối thông báo

## Các cân nhắc về bảo mật

Bảo mật nên là ưu tiên hàng đầu khi triển khai bất kỳ máy chủ nào, đặc biệt khi sử dụng các phương thức truyền tải dựa trên HTTP như Streamable HTTP trong MCP.

Khi triển khai các máy chủ MCP với các phương thức truyền tải dựa trên HTTP, bảo mật trở thành một mối quan tâm hàng đầu, đòi hỏi sự chú ý cẩn thận đến nhiều lỗ hổng tấn công và cơ chế bảo vệ.

### Tổng quan

Bảo mật là yếu tố quan trọng khi mở máy chủ MCP qua HTTP. Streamable HTTP giới thiệu các bề mặt tấn công mới và yêu cầu cấu hình cẩn thận.

Dưới đây là một số cân nhắc bảo mật chính:

- **Xác thực Header Origin**: Luôn xác thực header `Origin` để ngăn chặn các cuộc tấn công DNS rebinding.
- **Ràng buộc Localhost**: Đối với phát triển cục bộ, ràng buộc máy chủ vào `localhost` để tránh lộ ra internet công cộng.
- **Xác thực**: Triển khai xác thực (ví dụ: API keys, OAuth) cho các triển khai sản xuất.
- **CORS**: Cấu hình chính sách Cross-Origin Resource Sharing (CORS) để hạn chế truy cập.
- **HTTPS**: Sử dụng HTTPS trong môi trường sản xuất để mã hóa lưu lượng.

### Các thực hành tốt nhất

Ngoài ra, dưới đây là một số thực hành tốt nhất khi triển khai bảo mật trong máy chủ MCP streaming:

- Không bao giờ tin tưởng các yêu cầu đến mà không xác thực.
- Ghi nhật ký và giám sát tất cả các truy cập và lỗi.
- Thường xuyên cập nhật các phụ thuộc để vá các lỗ hổng bảo mật.

### Thách thức

Bạn sẽ gặp một số thách thức khi triển khai bảo mật trong các máy chủ MCP streaming:

- Cân bằng giữa bảo mật và sự dễ dàng trong phát triển
- Đảm bảo tính tương thích với các môi trường client khác nhau

### Bài tập: Xây dựng ứng dụng MCP streaming của riêng bạn

**Kịch bản:**
Xây dựng một máy chủ và client MCP, trong đó máy chủ xử lý danh sách các mục (ví dụ: tệp hoặc tài liệu) và gửi thông báo cho mỗi mục được xử lý. Client sẽ hiển thị từng thông báo khi nó đến.

**Các bước:**

1. Triển khai một công cụ máy chủ xử lý danh sách và gửi thông báo cho mỗi mục.
2. Triển khai một client với trình xử lý thông báo để hiển thị thông báo theo thời gian thực.
3. Kiểm tra triển khai của bạn bằng cách chạy cả máy chủ và client, và quan sát các thông báo.

[Solution](./solution/README.md)

## Đọc thêm & Tiếp theo là gì?

Để tiếp tục hành trình với MCP streaming và mở rộng kiến thức của bạn, phần này cung cấp các tài nguyên bổ sung và các bước tiếp theo được đề xuất để xây dựng các ứng dụng nâng cao hơn.

### Đọc thêm

- [Microsoft: Giới thiệu về HTTP Streaming](https://learn.microsoft.com/aspnet/core/fundamentals/http-requests?view=aspnetcore-8.0&WT.mc_id=%3Fwt.mc_id%3DMVP_452430#streaming)
- [Microsoft: Server-Sent Events (SSE)](https://learn.microsoft.com/azure/application-gateway/for-containers/server-sent-events?tabs=server-sent-events-gateway-api&WT.mc_id=%3Fwt.mc_id%3DMVP_452430)
- [Microsoft: CORS trong ASP.NET Core](https://learn.microsoft.com/aspnet/core/security/cors?view=aspnetcore-8.0&WT.mc_id=%3Fwt.mc_id%3DMVP_452430)
- [Python requests: Streaming Requests](https://requests.readthedocs.io/en/latest/user/advanced/#streaming-requests)

### Tiếp theo là gì?

- Thử xây dựng các công cụ MCP nâng cao hơn sử dụng streaming cho phân tích thời gian thực, trò chuyện hoặc chỉnh sửa cộng tác.
- Khám phá tích hợp MCP streaming với các framework frontend (React, Vue, v.v.) để cập nhật giao diện người dùng trực tiếp.
- Tiếp theo: [Sử dụng AI Toolkit cho VSCode](../07-aitk/README.md)

**Tuyên bố miễn trừ trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ bản địa nên được coi là nguồn tham khảo chính thức. Đối với các thông tin quan trọng, chúng tôi khuyến nghị sử dụng dịch vụ dịch thuật chuyên nghiệp từ con người. Chúng tôi không chịu trách nhiệm cho bất kỳ sự hiểu lầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.