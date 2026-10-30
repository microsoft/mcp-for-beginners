# HTTPS Streaming với Giao thức Ngữ cảnh Mô hình (MCP)

Chương này cung cấp một hướng dẫn toàn diện về cách triển khai streaming an toàn, có thể mở rộng và thời gian thực với Giao thức Ngữ cảnh Mô hình (MCP) sử dụng HTTPS. Nội dung bao gồm động lực cho streaming, các cơ chế vận chuyển có sẵn, cách triển khai HTTP có thể stream trong MCP, các thực hành bảo mật tốt nhất, chuyển đổi từ SSE, và hướng dẫn thực tiễn để xây dựng các ứng dụng MCP streaming của bạn.

> [!WARNING]
> Các ví dụ triển khai trong bài học này hướng tới **Đặc tả MCP
> `2025-11-25`** và minh họa giao thức bắt tay `initialize` cũ,
> `Mcp-Session-Id`, sự kiện GET stream, và mô hình có thể tiếp tục. MCP `2026-07-28`
> đã loại bỏ các tính năng đó. Các yêu cầu Streamable HTTP hiện tại là các yêu cầu POST tự chứa
> với các header `MCP-Protocol-Version` và `Mcp-Method`, thêm `Mcp-Name` nếu cần. Xem
> [Những thay đổi trong MCP: Đặc tả 2026-07-28](../../01-CoreConcepts/mcp-2026-07-28.md)
> trước khi sử dụng các ví dụ này trong triển khai mới.


## Cơ chế Vận chuyển và Streaming trong MCP

Phần này khám phá các cơ chế vận chuyển khác nhau có trong MCP và vai trò của chúng trong việc hỗ trợ khả năng streaming cho giao tiếp thời gian thực giữa client và server.

### Cơ chế Vận chuyển là gì?

Một cơ chế vận chuyển định nghĩa cách dữ liệu được trao đổi giữa client và server. MCP hỗ trợ nhiều loại vận chuyển để phù hợp với các môi trường và yêu cầu khác nhau:

- **stdio**: Đầu vào/đầu ra chuẩn, phù hợp cho các công cụ địa phương và dòng lệnh. Đơn giản nhưng không phù hợp cho môi trường web hoặc đám mây.
- **HTTP+SSE**: Vận chuyển từ xa đời cũ, đã bị loại bỏ trong MCP `2025-03-26`
    và được thay thế bởi Streamable HTTP. Không sử dụng cho các triển khai mới.
- **Streamable HTTP**: Vận chuyển streaming dựa trên HTTP hiện đại, hỗ trợ thông báo và khả năng mở rộng tốt hơn. Được khuyến nghị cho hầu hết các kịch bản sản xuất và đám mây.

### Bảng So sánh

Hãy xem bảng so sánh dưới đây để hiểu sự khác biệt giữa các cơ chế vận chuyển này:

| Vận chuyển | Tình trạng | Thông báo | Sử dụng điển hình |
|---|---|---|---|
| stdio | Hiện tại | Có | Các tiến trình phụ địa phương |
| HTTP+SSE | Đã loại bỏ | Có | Các triển khai từ xa đời cũ |
| Streamable HTTP | Hiện tại | Có | Máy chủ từ xa và đám mây |

> **Mẹo:** Việc chọn cơ chế vận chuyển đúng ảnh hưởng đến hiệu suất, khả năng mở rộng và trải nghiệm người dùng. **Streamable HTTP** được khuyến nghị cho các ứng dụng hiện đại, có thể mở rộng và sẵn sàng cho đám mây.

Các cơ chế vận chuyển tiêu chuẩn là stdio và Streamable HTTP. HTTP+SSE chỉ xuất hiện trong
các ví dụ cũ hơn.

## Streaming: Khái niệm và Động lực

Hiểu các khái niệm cơ bản và động lực đằng sau streaming là điều cần thiết để triển khai các hệ thống giao tiếp thời gian thực hiệu quả.

**Streaming** là một kỹ thuật trong lập trình mạng cho phép dữ liệu được gửi và nhận theo các phần nhỏ, dễ quản lý hoặc theo chuỗi các sự kiện, thay vì phải chờ toàn bộ phản hồi hoàn thành. Điều này rất hữu ích cho:

- Các tệp hoặc bộ dữ liệu lớn.
- Cập nhật thời gian thực (ví dụ, chat, thanh tiến trình).
- Tính toán thời gian dài mà bạn muốn cập nhật liên tục cho người dùng.

Đây là những điều bạn cần biết về streaming ở mức độ cao:

- Dữ liệu được truyền dần dần, không đồng thời.
- Client có thể xử lý dữ liệu ngay khi nó đến.
- Giảm độ trễ cảm nhận và cải thiện trải nghiệm người dùng.

### Tại sao sử dụng streaming?

Các lý do sử dụng streaming được liệt kê như sau:

- Người dùng nhận phản hồi ngay lập tức, không chỉ cuối cùng
- Cho phép các ứng dụng thời gian thực và giao diện người dùng phản hồi nhanh
- Sử dụng tài nguyên mạng và tính toán hiệu quả hơn

### Ví dụ đơn giản: Server & Client HTTP Streaming

Dưới đây là một ví dụ đơn giản về cách triển khai streaming:

#### Python

**Server (Python, dùng FastAPI và StreamingResponse):**

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

**Client (Python, dùng requests):**

```python
import requests

with requests.get("http://localhost:8000/stream", stream=True) as r:
    for line in r.iter_lines():
        if line:
            print(line.decode())
```

Ví dụ này minh họa máy chủ gửi một chuỗi các thông điệp đến client khi chúng sẵn sàng, thay vì đợi tất cả thông điệp xong mới gửi.

**Cách hoạt động:**

- Máy chủ phát từng thông điệp khi nó sẵn sàng.
- Client nhận và in từng phần khi dữ liệu đến.

**Yêu cầu:**

- Server phải dùng phản hồi streaming (ví dụ, `StreamingResponse` trong FastAPI).
- Client phải xử lý phản hồi như một stream (`stream=True` trong requests).
- Content-Type thường là `text/event-stream` hoặc `application/octet-stream`.

#### Java

**Server (Java, dùng Spring Boot và Server-Sent Events):**

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

**Client (Java, dùng Spring WebFlux WebClient):**

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

- Sử dụng stack phản ứng của Spring Boot với `Flux` để streaming
- `ServerSentEvent` cung cấp streaming sự kiện có cấu trúc với các loại sự kiện
- `WebClient` với `bodyToFlux()` cho phép tiêu thụ streaming theo phản ứng
- `delayElements()` giả lập thời gian xử lý giữa các sự kiện
- Sự kiện có thể có các loại (`info`, `result`) để client xử lý tốt hơn

### So sánh: Streaming Cổ điển vs Streaming MCP

Sự khác biệt giữa cách streaming hoạt động theo kiểu "cổ điển" so với trong MCP có thể được biểu diễn như sau:

| Tính năng               | Streaming HTTP Cổ điển       | Streaming MCP (Thông báo)       |
|------------------------|------------------------------|-------------------------------|
| Phản hồi chính          | Chia đoạn                    | Một lần, ở cuối                |
| Cập nhật tiến trình     | Gửi dưới dạng dữ liệu chia   | Gửi dưới dạng thông báo        |
| Yêu cầu client          | Phải xử lý stream            | Phải triển khai bộ xử lý thông điệp |
| Trường hợp sử dụng      | Tệp lớn, dòng token AI       | Tiến trình, ghi nhật ký, phản hồi thời gian thực |

### Những khác biệt chính được ghi nhận

Thêm vào đó, đây là một số khác biệt chính:

- **Mô hình giao tiếp:**
  - Streaming HTTP cổ điển: Dùng mã hóa truyền tải chia đoạn đơn giản để gửi dữ liệu theo từng phần
  - Streaming MCP: Dùng hệ thống thông báo có cấu trúc với giao thức JSON-RPC

- **Định dạng thông điệp:**
  - HTTP cổ điển: Các phần văn bản thuần với các dòng mới
  - MCP: Các đối tượng LoggingMessageNotification có cấu trúc với siêu dữ liệu

- **Triển khai client:**
  - HTTP cổ điển: Client đơn giản xử lý phản hồi streaming
  - MCP: Client tinh vi hơn với bộ xử lý thông điệp để xử lý các loại tin khác nhau

- **Cập nhật tiến trình:**
  - HTTP cổ điển: Tiến trình nằm trong stream phản hồi chính
  - MCP: Tiến trình được gửi qua các thông báo riêng biệt trong khi phản hồi chính được gửi cuối cùng

### Khuyến nghị

Có một số điều chúng tôi khuyên bạn khi lựa chọn giữa triển khai streaming cổ điển (như endpoint chúng tôi đã giới thiệu dùng `/stream`) so với lựa chọn streaming qua MCP.

- **Cho nhu cầu streaming đơn giản:** Streaming HTTP cổ điển dễ triển khai hơn và đủ cho nhu cầu streaming cơ bản.

- **Cho các ứng dụng tương tác phức tạp:** Streaming MCP cung cấp cách tiếp cận cấu trúc hơn với siêu dữ liệu phong phú và tách biệt giữa thông báo và kết quả cuối cùng.

- **Cho ứng dụng AI:** Hệ thống thông báo của MCP đặc biệt hữu ích cho các tác vụ AI thời gian chạy dài mà bạn muốn giữ cho người dùng cập nhật tiến độ.

## Streaming trong MCP

Vậy, bạn đã thấy một số khuyến nghị và so sánh về sự khác biệt giữa streaming cổ điển và streaming trong MCP. Bây giờ hãy tìm hiểu chi tiết chính xác cách bạn có thể tận dụng streaming trong MCP.

Hiểu cách streaming hoạt động trong khuôn khổ MCP là điều thiết yếu để xây dựng các ứng dụng phản hồi nhanh, cung cấp phản hồi thời gian thực cho người dùng trong các thao tác chạy dài.

Trong MCP, streaming không phải là gửi phản hồi chính thành các đoạn nhỏ, mà là gửi **thông báo** đến client trong khi công cụ đang xử lý yêu cầu. Các thông báo này có thể bao gồm cập nhật tiến trình, nhật ký hoặc các sự kiện khác.

### Cách hoạt động

Kết quả chính vẫn được gửi thành một phản hồi duy nhất. Tuy nhiên, các thông báo có thể gửi dưới dạng các tin riêng biệt trong quá trình xử lý và do đó cập nhật client theo thời gian thực. Client phải có khả năng xử lý và hiển thị các thông báo này.

### Bài tập tùy chọn: kết nối với máy chủ MCP được lưu trữ

Bạn cũng có thể sử dụng Streamable HTTP mà không cần chạy server cục bộ. Ví dụ này
kết nối với [Parallel Search MCP](https://docs.parallel.ai/integrations/mcp/search-mcp),
khám phá các công cụ của nó, và tìm kiếm tài liệu MCP công khai sử dụng cùng
SDK Python như [client địa phương](../../../../03-GettingStarted/06-http-streaming/solution/python/client.py).

Địa chỉ endpoint ẩn danh của Parallel không yêu cầu tài khoản hay key API. Truy cập miễn phí
có giới hạn băng thông. Chạy script này gửi các truy vấn tìm kiếm, mục tiêu, và
một định danh phiên ngẫu nhiên tới Parallel. Dịch vụ cũng cung cấp `web_fetch`,
gửi URL yêu cầu và bất kỳ ngữ cảnh nào cung cấp đến Parallel. Sử dụng thông tin công khai
cho bài tập này; xem [điều khoản](https://parallel.ai/customer-terms) và [chính sách bảo mật](https://parallel.ai/privacy-policy).




```sh
python -m pip install "mcp>=1.10,<2"
```

Lưu lại file này dưới tên `hosted_search.py` và chạy `python hosted_search.py`:

```python
import asyncio
from uuid import uuid4

from mcp import ClientSession
from mcp.client.streamable_http import streamablehttp_client


async def main() -> None:
    session_id = str(uuid4())
    async with streamablehttp_client("https://search.parallel.ai/mcp") as (
        read_stream,
        write_stream,
        _,
    ):
        async with ClientSession(read_stream, write_stream) as session:
            await session.initialize()
            tools = await session.list_tools()
            print("Available tools:", [tool.name for tool in tools.tools])

            result = await session.call_tool(
                "web_search",
                {
                    "objective": "Find the official MCP Streamable HTTP documentation",
                    "search_queries": ["MCP Streamable HTTP documentation"],
                    "session_id": session_id,
                },
            )
            if result.isError:
                raise RuntimeError(f"Search tool failed: {result.content}")
            for block in result.content:
                if block.type == "text":
                    print(block.text)


async def run() -> None:
    await asyncio.wait_for(main(), timeout=60)


if __name__ == "__main__":
    asyncio.run(run())
```

Mong đợi kết quả discovery bao gồm `web_search` và `web_fetch`, tiếp theo là một phản hồi tìm kiếm
chứa các URL nguồn và đoạn trích. Kết quả có thể khác nhau hoặc không có.
Kịch bản kiểm tra `isError` bởi vì một công cụ có thể thất bại ngay cả khi yêu cầu HTTP
thành công. Nếu bị giới hạn truy cập theo tỉ lệ, hãy đợi trước khi thử lại. Tái sử dụng cùng
`session_id` nếu bạn mở rộng kịch bản với các cuộc gọi tìm kiếm hoặc lấy dữ liệu liên quan.

HTTP có thể phát trực tiếp cho phép cả phản hồi JSON và SSE; máy chủ này có thể trả về một
kết quả JSON hoàn chỉnh mà không có thông báo tiến trình. SDK đảm nhận việc
vận chuyển. Tiếp tục với ví dụ cục bộ dưới đây để tìm hiểu về thông báo.
Kịch bản tùy chọn này thực hiện một tìm kiếm rõ ràng và đóng kết nối khi
hoàn thành. Nếu sau này bạn công khai các công cụ này cho một tác nhân, tác nhân có thể gọi
chúng trong quá trình làm việc; hãy xem văn bản web lấy được như là dữ liệu không đáng tin cậy.

## Thông báo là gì?

Chúng tôi nói "Thông báo", điều đó có nghĩa gì trong bối cảnh MCP?

Thông báo là một tin nhắn JSON-RPC không có `id` và không
nhận được phản hồi. MCP sử dụng thông báo cho tiến trình, hủy bỏ và
các sự kiện một chiều khác.

Trong MCP `2025-11-25`, một máy khách gửi `notifications/initialized` sau
khi bắt tay khởi tạo. MCP `2026-07-28` không có bắt tay khởi tạo, vì vậy
thông báo này là hành vi kế thừa.

Một thông báo trông như thế này dưới dạng tin nhắn JSON:

```json
{
  jsonrpc: "2.0";
  method: string;
  params?: {
    [key: string]: unknown;
  };
}
```

Việc ghi nhật ký là một tính năng sử dụng thông báo; bản thân thông báo là một
loại tin nhắn JSON-RPC chung.

> **Đã ngừng hỗ trợ trong MCP `2026-07-28`:** tính năng Ghi nhật ký vẫn còn
> để tương thích nhưng có thể được loại bỏ trong lần sửa đổi đặc tả đầu tiên
> phát hành từ hoặc sau ngày 28 tháng 7 năm 2027. Các triển khai mới nên sử dụng
> `stderr` với stdio hoặc OpenTelemetry để quan sát có cấu trúc.

Đối với một triển khai kế thừa `2025-11-25`, máy chủ bật tính năng Ghi nhật ký
như sau:

```json
{
  "capabilities": {
    "logging": {}
  }
}
```

> [!NOTE]
> Tùy thuộc vào SDK được sử dụng, ghi nhật ký có thể được bật mặc định, hoặc bạn có thể cần bật rõ ràng trong cấu hình máy chủ của bạn.

Có các loại thông báo khác nhau:

| Cấp độ   | Mô tả                         | Ví dụ sử dụng                  |
|----------|------------------------------|--------------------------------|
| debug    | Thông tin gỡ lỗi chi tiết      | Điểm vào/ra hàm                |
| info     | Thông điệp thông tin chung     | Cập nhật tiến trình hoạt động  |
| notice   | Sự kiện bình thường nhưng quan trọng | Thay đổi cấu hình         |
| warning  | Điều kiện cảnh báo              | Sử dụng tính năng đã ngừng hỗ trợ |
| error    | Điều kiện lỗi                  | Thất bại hoạt động             |
| critical | Điều kiện nghiêm trọng          | Hỏng thành phần hệ thống       |
| alert    | Phải hành động ngay lập tức     | Phát hiện dữ liệu bị hỏng      |
| emergency| Hệ thống không thể sử dụng      | Hỏng hoàn toàn hệ thống        |

## Triển khai Thông báo trong MCP

Để triển khai thông báo trong MCP, bạn cần thiết lập cả phía máy chủ và máy khách để xử lý cập nhật theo thời gian thực. Điều này cho phép ứng dụng của bạn cung cấp phản hồi ngay lập tức cho người dùng trong các hoạt động chạy lâu.

### Phía máy chủ: Gửi Thông báo

Hãy bắt đầu với phía máy chủ. Trong MCP, bạn định nghĩa các công cụ có thể gửi thông báo trong khi xử lý yêu cầu. Máy chủ sử dụng đối tượng context (thường là `ctx`) để gửi tin nhắn tới khách hàng.

#### Python

```python
@mcp.tool(description="A tool that sends progress notifications")
async def process_files(message: str, ctx: Context) -> TextContent:
    await ctx.info("Processing file 1/3...")
    await ctx.info("Processing file 2/3...")
    await ctx.info("Processing file 3/3...")
    return TextContent(type="text", text=f"Done: {message}")
```

Trong ví dụ trước, công cụ `process_files` gửi ba thông báo tới khách khi xử lý từng tệp. Phương thức `ctx.info()` được sử dụng để gửi các tin nhắn mang tính thông tin.

Thêm vào đó, để kích hoạt thông báo, đảm bảo máy chủ của bạn sử dụng phương thức truyền phát (streaming transport) (như `streamable-http`) và khách hàng của bạn triển khai bộ xử lý tin nhắn để xử lý các thông báo. Dưới đây là cách bạn có thể thiết lập máy chủ để sử dụng phương thức truyền `streamable-http`:

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

Trong ví dụ .NET này, công cụ `ProcessFiles` được trang trí với thuộc tính `Tool` và gửi ba thông báo tới khách khi xử lý từng tệp. Phương thức `ctx.Info()` được sử dụng để gửi các tin nhắn mang tính thông tin.

Để kích hoạt thông báo trong máy chủ MCP .NET của bạn, đảm bảo bạn đang sử dụng phương thức truyền phát:

```csharp
var builder = McpBuilder.Create();
await builder
    .UseStreamableHttp() // Enable streamable HTTP transport
    .Build()
    .RunAsync();
```

### Phía khách: Nhận thông báo

Khách hàng phải triển khai bộ xử lý tin nhắn để xử lý và hiển thị các thông báo khi chúng đến.

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

Trong đoạn mã trước, hàm `message_handler` kiểm tra xem tin nhắn đến có phải là thông báo hay không. Nếu đúng, nó in ra thông báo; nếu không, nó xử lý như một tin nhắn máy chủ thông thường. Cũng lưu ý cách `ClientSession` được khởi tạo với `message_handler` để xử lý các thông báo đến.

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

Trong ví dụ .NET này, hàm `MessageHandler` kiểm tra xem tin nhắn đến có phải là thông báo hay không. Nếu đúng, nó in ra thông báo; nếu không, nó xử lý như một tin nhắn máy chủ thông thường. `ClientSession` được khởi tạo với trình xử lý tin nhắn thông qua `ClientSessionOptions`.

Để bật thông báo, hãy đảm bảo server của bạn sử dụng giao thức truyền phát (như `streamable-http`) và client của bạn triển khai trình xử lý tin nhắn để xử lý các thông báo.

## Thông báo tiến trình & Kịch bản

Phần này giải thích khái niệm thông báo tiến trình trong MCP, lý do tại sao chúng quan trọng và cách triển khai chúng bằng cách sử dụng Streamable HTTP. Bạn cũng sẽ tìm thấy một bài tập thực tế để củng cố sự hiểu biết của mình.

Thông báo tiến trình là các tin nhắn thời gian thực được gửi từ server đến client trong quá trình thực thi các thao tác lâu dài. Thay vì chờ hoàn thành toàn bộ quá trình, server giữ cho client được cập nhật về trạng thái hiện tại. Điều này cải thiện tính minh bạch, trải nghiệm người dùng và giúp việc gỡ lỗi dễ dàng hơn.

**Ví dụ:**

```text

"Processing document 1/10"
"Processing document 2/10"
...
"Processing complete!"

```

### Tại sao nên sử dụng thông báo tiến trình?

Thông báo tiến trình rất cần thiết vì một số lý do:

- **Trải nghiệm người dùng tốt hơn:** Người dùng thấy được cập nhật trong suốt quá trình làm việc, không chỉ cuối cùng.
- **Phản hồi thời gian thực:** Client có thể hiển thị thanh tiến trình hoặc nhật ký, khiến ứng dụng cảm giác phản hồi nhanh.
- **Dễ dàng gỡ lỗi và theo dõi:** Nhà phát triển và người dùng có thể thấy quá trình bị chậm hoặc bị kẹt ở đâu.

### Cách triển khai thông báo tiến trình

Dưới đây là cách bạn có thể triển khai thông báo tiến trình trong MCP:

- **Trên server:** Sử dụng `ctx.info()` hoặc `ctx.log()` để gửi thông báo khi từng mục được xử lý. Điều này gửi tin nhắn đến client trước khi kết quả chính sẵn sàng.
- **Trên client:** Triển khai trình xử lý tin nhắn lắng nghe và hiển thị các thông báo khi chúng đến. Trình xử lý này phân biệt giữa thông báo và kết quả cuối cùng.

**Ví dụ server:**

#### Python

```python
@mcp.tool(description="A tool that sends progress notifications")
async def process_files(message: str, ctx: Context) -> TextContent:
    for i in range(1, 11):
        await ctx.info(f"Processing document {i}/10")
    await ctx.info("Processing complete!")
    return TextContent(type="text", text=f"Done: {message}")
```

**Ví dụ client:**

#### Python

```python
async def message_handler(message):
    if isinstance(message, types.ServerNotification):
        print("NOTIFICATION:", message)
    else:
        print("SERVER MESSAGE:", message)
```

## Các cân nhắc về bảo mật

Bảo mật nên là ưu tiên hàng đầu khi triển khai bất kỳ server nào, đặc biệt khi sử dụng các giao thức dựa trên HTTP như Streamable HTTP trong MCP.

Khi triển khai các server MCP với giao thức dựa trên HTTP, bảo mật trở thành mối quan tâm hàng đầu đòi hỏi sự chú ý cẩn thận đối với nhiều vectơ tấn công và cơ chế bảo vệ.

### Tổng quan

Bảo mật rất quan trọng khi mở rộng các server MCP qua HTTP. Streamable HTTP tạo ra các bề mặt tấn công mới và yêu cầu cấu hình cẩn thận.

Dưới đây là một số cân nhắc bảo mật chính:

- **Xác thực Header Origin**: Luôn xác thực header `Origin` để phòng chống các cuộc tấn công DNS rebinding.
- **Ràng buộc Localhost**: Đối với phát triển cục bộ, ràng buộc server với `localhost` để tránh lộ ra internet công cộng.
- **Xác thực**: Triển khai xác thực (ví dụ, khóa API, OAuth) cho môi trường sản xuất.
- **CORS**: Cấu hình các chính sách chia sẻ tài nguyên nguồn gốc chéo (CORS) để hạn chế truy cập.
- **HTTPS**: Sử dụng HTTPS trong môi trường sản xuất để mã hóa lưu lượng.

### Thực hành tốt nhất

Ngoài ra, dưới đây là một số thực hành tốt nhất cần tuân theo khi triển khai bảo mật trong server streaming MCP của bạn:

- Không bao giờ tin tưởng các yêu cầu đến mà không xác thực.
- Ghi nhật ký và giám sát tất cả các truy cập và lỗi.
- Cập nhật các phụ thuộc thường xuyên để vá các lỗ hổng bảo mật.

### Thách thức

Bạn sẽ gặp một số thách thức khi triển khai bảo mật trong server streaming MCP:

- Cân bằng giữa bảo mật và dễ dàng phát triển
- Đảm bảo tương thích với nhiều môi trường client khác nhau


## Nâng cấp từ SSE lên Streamable HTTP

Đối với các ứng dụng hiện đang sử dụng Server-Sent Events (SSE), việc chuyển sang Streamable HTTP cung cấp khả năng nâng cao và tính bền vững hơn cho các triển khai MCP của bạn trong dài hạn.

### Tại sao nên nâng cấp?

Có hai lý do thuyết phục để nâng cấp từ SSE sang Streamable HTTP:

- Streamable HTTP mang lại khả năng mở rộng, tương thích tốt hơn và hỗ trợ thông báo phong phú hơn so với SSE.
- Đây là giao thức được khuyến nghị cho các ứng dụng MCP mới.

### Các bước di chuyển

Dưới đây là cách bạn có thể di chuyển từ SSE sang Streamable HTTP trong các ứng dụng MCP của mình:

- **Cập nhật mã server** để sử dụng `transport="streamable-http"` trong `mcp.run()`.
- **Cập nhật mã client** để sử dụng `streamablehttp_client` thay vì client SSE.
- **Triển khai trình xử lý tin nhắn** trong client để xử lý các thông báo.
- **Kiểm tra tương thích** với các công cụ và quy trình hiện có.

### Duy trì tương thích

Khuyến nghị duy trì sự tương thích với các client SSE hiện có trong quá trình di chuyển. Dưới đây là một số chiến lược:

- Bạn có thể hỗ trợ cả SSE và Streamable HTTP bằng cách chạy cả hai giao thức trên các đầu cuối khác nhau.
- Di chuyển các client sang giao thức mới một cách dần dần.

### Thách thức

Hãy đảm bảo bạn xử lý các thách thức sau trong quá trình di chuyển:

- Đảm bảo tất cả client đều được cập nhật
- Xử lý sự khác biệt trong giao nhận thông báo

### Bài tập: Xây dựng ứng dụng streaming MCP của riêng bạn

**Kịch bản:**
Xây dựng một server và client MCP nơi server xử lý một danh sách các mục (ví dụ, tệp hoặc tài liệu) và gửi thông báo cho mỗi mục được xử lý. Client sẽ hiển thị mỗi thông báo khi nó đến.

**Các bước:**

1. Triển khai công cụ server xử lý danh sách và gửi thông báo cho từng mục.
2. Triển khai client với trình xử lý tin nhắn để hiển thị các thông báo thời gian thực.
3. Kiểm tra triển khai bằng cách chạy cả server và client, và quan sát các thông báo.

[Giải pháp](./solution/README.md)

## Đọc thêm & Tiếp theo là gì?

Để tiếp tục hành trình với streaming MCP và mở rộng kiến thức, phần này cung cấp thêm tài nguyên và các bước gợi ý tiếp theo để xây dựng các ứng dụng nâng cao hơn.

### Đọc thêm

- [Microsoft: Giới thiệu về HTTP Streaming](https://learn.microsoft.com/aspnet/core/fundamentals/http-requests?view=aspnetcore-8.0&WT.mc_id=%3Fwt.mc_id%3DMVP_452430#streaming)
- [Microsoft: Server-Sent Events (SSE)](https://learn.microsoft.com/azure/application-gateway/for-containers/server-sent-events?tabs=server-sent-events-gateway-api&WT.mc_id=%3Fwt.mc_id%3DMVP_452430)
- [Microsoft: CORS trong ASP.NET Core](https://learn.microsoft.com/aspnet/core/security/cors?view=aspnetcore-8.0&WT.mc_id=%3Fwt.mc_id%3DMVP_452430)
- [Python requests: Streaming Requests](https://requests.readthedocs.io/en/latest/user/advanced/#streaming-requests)

### Tiếp theo là gì?

- Thử xây dựng các công cụ MCP nâng cao hơn sử dụng streaming cho phân tích thời gian thực, chat hoặc chỉnh sửa cộng tác.
- Khám phá cách tích hợp streaming MCP với các framework frontend (React, Vue, v.v.) để cập nhật giao diện người dùng trực tiếp.
- Tiếp theo: [Sử dụng Microsoft Foundry Toolkit cho Visual Studio Code](../07-aitk/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Tuyên bố miễn trừ trách nhiệm**:
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng bản dịch tự động có thể chứa lỗi hoặc sai sót. Tài liệu gốc bằng ngôn ngữ gốc nên được coi là nguồn tin chính thức. Đối với thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm về bất kỳ hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->