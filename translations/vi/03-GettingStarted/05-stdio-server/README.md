# MCP Server với Giao thức stdio

> **⚠️ Cập nhật quan trọng**: Từ phiên bản MCP Specification 2025-06-18, giao thức SSE (Server-Sent Events) độc lập đã bị **khai tử** và được thay thế bằng giao thức "Streamable HTTP". Phiên bản MCP hiện tại định nghĩa hai cơ chế giao tiếp chính:
> 1. **stdio** - Giao tiếp qua đầu vào/đầu ra tiêu chuẩn (khuyến nghị cho các máy chủ cục bộ)
> 2. **Streamable HTTP** - Dành cho các máy chủ từ xa có thể sử dụng SSE nội bộ
>
> Bài học này đã được cập nhật để tập trung vào **giao thức stdio**, đây là phương pháp được khuyến nghị cho hầu hết các triển khai máy chủ MCP.

Giao thức stdio cho phép các máy chủ MCP giao tiếp với khách hàng thông qua các luồng đầu vào và đầu ra tiêu chuẩn. Đây là cơ chế giao tiếp được sử dụng phổ biến nhất và được khuyến nghị trong phiên bản MCP hiện tại, cung cấp một cách đơn giản và hiệu quả để xây dựng các máy chủ MCP có thể dễ dàng tích hợp với nhiều ứng dụng khách khác nhau.

## Tổng quan

Bài học này hướng dẫn cách xây dựng và sử dụng máy chủ MCP với giao thức stdio.

## Mục tiêu học tập

Sau khi hoàn thành bài học này, bạn sẽ có thể:

- Xây dựng một máy chủ MCP sử dụng giao thức stdio.
- Gỡ lỗi máy chủ MCP bằng công cụ Inspector.
- Sử dụng máy chủ MCP trong Visual Studio Code.
- Hiểu các cơ chế giao tiếp MCP hiện tại và lý do tại sao stdio được khuyến nghị.

## Giao thức stdio - Cách hoạt động

Giao thức stdio là một trong hai loại giao thức được hỗ trợ trong phiên bản MCP hiện tại (2025-06-18). Cách hoạt động như sau:

- **Giao tiếp đơn giản**: Máy chủ đọc các thông điệp JSON-RPC từ đầu vào tiêu chuẩn (`stdin`) và gửi thông điệp qua đầu ra tiêu chuẩn (`stdout`).
- **Dựa trên tiến trình**: Khách hàng khởi chạy máy chủ MCP như một tiến trình con.
- **Định dạng thông điệp**: Các thông điệp là các yêu cầu, thông báo, hoặc phản hồi JSON-RPC riêng lẻ, được phân cách bằng dòng mới.
- **Ghi nhật ký**: Máy chủ CÓ THỂ ghi các chuỗi UTF-8 vào đầu ra lỗi tiêu chuẩn (`stderr`) để ghi nhật ký.

### Yêu cầu chính:
- Các thông điệp PHẢI được phân cách bằng dòng mới và KHÔNG ĐƯỢC chứa dòng mới nhúng.
- Máy chủ KHÔNG ĐƯỢC ghi bất kỳ thứ gì vào `stdout` không phải là thông điệp MCP hợp lệ.
- Khách hàng KHÔNG ĐƯỢC ghi bất kỳ thứ gì vào `stdin` của máy chủ không phải là thông điệp MCP hợp lệ.

### TypeScript

```typescript
import { Server } from "@modelcontextprotocol/sdk/server/index.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";

const server = new Server(
  {
    name: "example-server",
    version: "1.0.0",
  },
  {
    capabilities: {
      tools: {},
    },
  }
);
```

Trong đoạn mã trên:

- Chúng ta nhập lớp `Server` và `StdioServerTransport` từ MCP SDK.
- Chúng ta tạo một phiên bản máy chủ với cấu hình và khả năng cơ bản.

### Python

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server

# Create server instance
server = Server("example-server")

@server.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

async def main():
    async with stdio_server(server) as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            server.create_initialization_options()
        )

if __name__ == "__main__":
    asyncio.run(main())
```

Trong đoạn mã trên, chúng ta:

- Tạo một phiên bản máy chủ sử dụng MCP SDK.
- Định nghĩa các công cụ bằng cách sử dụng decorators.
- Sử dụng context manager `stdio_server` để xử lý giao thức.

### .NET

```csharp
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;
using Microsoft.Extensions.Logging;
using ModelContextProtocol.Server;

var builder = Host.CreateApplicationBuilder(args);

builder.Services
    .AddMcpServer()
    .WithStdioTransport()
    .WithTools<Tools>();

builder.Services.AddLogging(logging => logging.AddConsole());

var app = builder.Build();
await app.RunAsync();
```

Sự khác biệt chính so với SSE là các máy chủ stdio:

- Không yêu cầu thiết lập máy chủ web hoặc các điểm cuối HTTP.
- Được khởi chạy như các tiến trình con bởi khách hàng.
- Giao tiếp qua các luồng stdin/stdout.
- Dễ triển khai và gỡ lỗi hơn.

## Bài tập: Tạo một máy chủ stdio

Để tạo máy chủ của chúng ta, cần lưu ý hai điều:

- Chúng ta cần sử dụng một máy chủ web để cung cấp các điểm cuối cho kết nối và thông điệp.

## Phòng thí nghiệm: Tạo một máy chủ MCP stdio đơn giản

Trong phòng thí nghiệm này, chúng ta sẽ tạo một máy chủ MCP đơn giản sử dụng giao thức stdio được khuyến nghị. Máy chủ này sẽ cung cấp các công cụ mà khách hàng có thể gọi bằng giao thức Model Context Protocol tiêu chuẩn.

### Yêu cầu

- Python 3.8 hoặc mới hơn.
- MCP Python SDK: `pip install mcp`.
- Hiểu biết cơ bản về lập trình bất đồng bộ.

Hãy bắt đầu tạo máy chủ MCP stdio đầu tiên của chúng ta:

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp import types

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Create the server
server = Server("example-stdio-server")

@server.tool()
def calculate_sum(a: int, b: int) -> int:
    """Calculate the sum of two numbers"""
    return a + b

@server.tool() 
def get_greeting(name: str) -> str:
    """Generate a personalized greeting"""
    return f"Hello, {name}! Welcome to MCP stdio server."

async def main():
    # Use stdio transport
    async with stdio_server(server) as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            server.create_initialization_options()
        )

if __name__ == "__main__":
    asyncio.run(main())
```

## Sự khác biệt chính so với phương pháp SSE đã khai tử

**Giao thức Stdio (Tiêu chuẩn hiện tại):**
- Mô hình tiến trình con đơn giản - khách hàng khởi chạy máy chủ như một tiến trình con.
- Giao tiếp qua stdin/stdout sử dụng thông điệp JSON-RPC.
- Không yêu cầu thiết lập máy chủ HTTP.
- Hiệu suất và bảo mật tốt hơn.
- Dễ dàng gỡ lỗi và phát triển.

**Giao thức SSE (Đã khai tử từ MCP 2025-06-18):**
- Yêu cầu máy chủ HTTP với các điểm cuối SSE.
- Thiết lập phức tạp hơn với hạ tầng máy chủ web.
- Cần xem xét thêm về bảo mật cho các điểm cuối HTTP.
- Hiện đã được thay thế bằng Streamable HTTP cho các kịch bản dựa trên web.

### Tạo máy chủ với giao thức stdio

Để tạo máy chủ stdio, chúng ta cần:

1. **Nhập các thư viện cần thiết** - Chúng ta cần các thành phần máy chủ MCP và giao thức stdio.
2. **Tạo một phiên bản máy chủ** - Định nghĩa máy chủ với các khả năng của nó.
3. **Định nghĩa các công cụ** - Thêm các chức năng mà chúng ta muốn cung cấp.
4. **Thiết lập giao thức** - Cấu hình giao tiếp stdio.
5. **Chạy máy chủ** - Khởi chạy máy chủ và xử lý thông điệp.

Hãy xây dựng từng bước:

### Bước 1: Tạo một máy chủ stdio cơ bản

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Create the server
server = Server("example-stdio-server")

@server.tool()
def get_greeting(name: str) -> str:
    """Generate a personalized greeting"""
    return f"Hello, {name}! Welcome to MCP stdio server."

async def main():
    async with stdio_server(server) as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            server.create_initialization_options()
        )

if __name__ == "__main__":
    asyncio.run(main())
```

### Bước 2: Thêm nhiều công cụ hơn

```python
@server.tool()
def calculate_sum(a: int, b: int) -> int:
    """Calculate the sum of two numbers"""
    return a + b

@server.tool()
def calculate_product(a: int, b: int) -> int:
    """Calculate the product of two numbers"""
    return a * b

@server.tool()
def get_server_info() -> dict:
    """Get information about this MCP server"""
    return {
        "server_name": "example-stdio-server",
        "version": "1.0.0",
        "transport": "stdio",
        "capabilities": ["tools"]
    }
```

### Bước 3: Chạy máy chủ

Lưu mã dưới dạng `server.py` và chạy từ dòng lệnh:

```bash
python server.py
```

Máy chủ sẽ khởi động và chờ đầu vào từ stdin. Nó giao tiếp bằng các thông điệp JSON-RPC qua giao thức stdio.

### Bước 4: Kiểm tra với công cụ Inspector

Bạn có thể kiểm tra máy chủ của mình bằng công cụ MCP Inspector:

1. Cài đặt Inspector: `npx @modelcontextprotocol/inspector`.
2. Chạy Inspector và trỏ nó đến máy chủ của bạn.
3. Kiểm tra các công cụ bạn đã tạo.

### .NET

```csharp
var builder = WebApplication.CreateBuilder(args);
builder.Services
    .AddMcpServer();
 ```

## Gỡ lỗi máy chủ stdio của bạn

### Sử dụng MCP Inspector

MCP Inspector là một công cụ hữu ích để gỡ lỗi và kiểm tra các máy chủ MCP. Đây là cách sử dụng nó với máy chủ stdio của bạn:

1. **Cài đặt Inspector**:
   ```bash
   npx @modelcontextprotocol/inspector
   ```

2. **Chạy Inspector**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

3. **Kiểm tra máy chủ của bạn**: Inspector cung cấp giao diện web nơi bạn có thể:
   - Xem các khả năng của máy chủ.
   - Kiểm tra các công cụ với các tham số khác nhau.
   - Theo dõi các thông điệp JSON-RPC.
   - Gỡ lỗi các vấn đề kết nối.

### Sử dụng VS Code

Bạn cũng có thể gỡ lỗi máy chủ MCP trực tiếp trong VS Code:

1. Tạo cấu hình khởi chạy trong `.vscode/launch.json`:
   ```json
   {
     "version": "0.2.0",
     "configurations": [
       {
         "name": "Debug MCP Server",
         "type": "python",
         "request": "launch",
         "program": "server.py",
         "console": "integratedTerminal"
       }
     ]
   }
   ```

2. Đặt các điểm dừng trong mã máy chủ của bạn.
3. Chạy trình gỡ lỗi và kiểm tra với Inspector.

### Mẹo gỡ lỗi phổ biến

- Sử dụng `stderr` để ghi nhật ký - không bao giờ ghi vào `stdout` vì nó được dành riêng cho các thông điệp MCP.
- Đảm bảo tất cả các thông điệp JSON-RPC được phân cách bằng dòng mới.
- Kiểm tra với các công cụ đơn giản trước khi thêm các chức năng phức tạp.
- Sử dụng Inspector để xác minh định dạng thông điệp.

## Sử dụng máy chủ stdio của bạn trong VS Code

Sau khi bạn đã xây dựng máy chủ MCP stdio, bạn có thể tích hợp nó với VS Code để sử dụng với Claude hoặc các khách hàng tương thích MCP khác.

### Cấu hình

1. **Tạo tệp cấu hình MCP** tại `%APPDATA%\Claude\claude_desktop_config.json` (Windows) hoặc `~/Library/Application Support/Claude/claude_desktop_config.json` (Mac):

   ```json
   {
     "mcpServers": {
       "example-stdio-server": {
         "command": "python",
         "args": ["path/to/your/server.py"]
       }
     }
   }
   ```

2. **Khởi động lại Claude**: Đóng và mở lại Claude để tải cấu hình máy chủ mới.

3. **Kiểm tra kết nối**: Bắt đầu một cuộc trò chuyện với Claude và thử sử dụng các công cụ của máy chủ:
   - "Bạn có thể chào tôi bằng công cụ chào hỏi không?"
   - "Tính tổng của 15 và 27."
   - "Thông tin về máy chủ là gì?"

### Ví dụ máy chủ stdio TypeScript

Dưới đây là một ví dụ hoàn chỉnh bằng TypeScript để tham khảo:

```typescript
#!/usr/bin/env node
import { Server } from "@modelcontextprotocol/sdk/server/index.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { CallToolRequestSchema, ListToolsRequestSchema } from "@modelcontextprotocol/sdk/types.js";

const server = new Server(
  {
    name: "example-stdio-server",
    version: "1.0.0",
  },
  {
    capabilities: {
      tools: {},
    },
  }
);

// Add tools
server.setRequestHandler(ListToolsRequestSchema, async () => {
  return {
    tools: [
      {
        name: "get_greeting",
        description: "Get a personalized greeting",
        inputSchema: {
          type: "object",
          properties: {
            name: {
              type: "string",
              description: "Name of the person to greet",
            },
          },
          required: ["name"],
        },
      },
    ],
  };
});

server.setRequestHandler(CallToolRequestSchema, async (request) => {
  if (request.params.name === "get_greeting") {
    return {
      content: [
        {
          type: "text",
          text: `Hello, ${request.params.arguments?.name}! Welcome to MCP stdio server.`,
        },
      ],
    };
  } else {
    throw new Error(`Unknown tool: ${request.params.name}`);
  }
});

async function runServer() {
  const transport = new StdioServerTransport();
  await server.connect(transport);
}

runServer().catch(console.error);
```

### Ví dụ máy chủ stdio .NET

```csharp
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;
using Microsoft.Extensions.Logging;
using ModelContextProtocol.Server;
using System.ComponentModel;

var builder = Host.CreateApplicationBuilder(args);

builder.Services
    .AddMcpServer()
    .WithStdioTransport()
    .WithTools<Tools>();

var app = builder.Build();
await app.RunAsync();

public class Tools
{
    [Description("Get a personalized greeting")]
    public string GetGreeting(string name)
    {
        return $"Hello, {name}! Welcome to MCP stdio server.";
    }

    [Description("Calculate the sum of two numbers")]
    public int CalculateSum(int a, int b)
    {
        return a + b;
    }
}
```

## Tóm tắt

Trong bài học được cập nhật này, bạn đã học cách:

- Xây dựng máy chủ MCP sử dụng giao thức **stdio** (phương pháp được khuyến nghị).
- Hiểu lý do tại sao giao thức SSE bị khai tử và thay thế bằng stdio và Streamable HTTP.
- Tạo các công cụ mà khách hàng MCP có thể gọi.
- Gỡ lỗi máy chủ của bạn bằng công cụ MCP Inspector.
- Tích hợp máy chủ stdio của bạn với VS Code và Claude.

Giao thức stdio cung cấp một cách đơn giản, an toàn và hiệu quả hơn để xây dựng các máy chủ MCP so với phương pháp SSE đã khai tử. Đây là giao thức được khuyến nghị cho hầu hết các triển khai máy chủ MCP theo phiên bản đặc tả 2025-06-18.

### .NET

1. Hãy tạo một số công cụ trước, cho việc này chúng ta sẽ tạo một tệp *Tools.cs* với nội dung sau:

  ```csharp
  using System.ComponentModel;
  using System.Text.Json;
  using ModelContextProtocol.Server;
  ```

## Bài tập: Kiểm tra máy chủ stdio của bạn

Bây giờ bạn đã xây dựng máy chủ stdio, hãy kiểm tra để đảm bảo nó hoạt động chính xác.

### Yêu cầu

1. Đảm bảo bạn đã cài đặt MCP Inspector:
   ```bash
   npm install -g @modelcontextprotocol/inspector
   ```

2. Mã máy chủ của bạn nên được lưu (ví dụ: dưới dạng `server.py`).

### Kiểm tra với Inspector

1. **Khởi chạy Inspector với máy chủ của bạn**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

2. **Mở giao diện web**: Inspector sẽ mở một cửa sổ trình duyệt hiển thị các khả năng của máy chủ.

3. **Kiểm tra các công cụ**: 
   - Thử công cụ `get_greeting` với các tên khác nhau.
   - Kiểm tra công cụ `calculate_sum` với các số khác nhau.
   - Gọi công cụ `get_server_info` để xem thông tin máy chủ.

4. **Theo dõi giao tiếp**: Inspector hiển thị các thông điệp JSON-RPC được trao đổi giữa khách hàng và máy chủ.

### Những gì bạn nên thấy

Khi máy chủ của bạn khởi động đúng cách, bạn sẽ thấy:
- Các khả năng của máy chủ được liệt kê trong Inspector.
- Các công cụ có sẵn để kiểm tra.
- Các thông điệp JSON-RPC được trao đổi thành công.
- Phản hồi của công cụ được hiển thị trong giao diện.

### Các vấn đề phổ biến và giải pháp

**Máy chủ không khởi động:**
- Kiểm tra rằng tất cả các phụ thuộc đã được cài đặt: `pip install mcp`.
- Xác minh cú pháp và thụt lề Python.
- Tìm lỗi trong bảng điều khiển.

**Công cụ không xuất hiện:**
- Đảm bảo các decorators `@server.tool()` có mặt.
- Kiểm tra rằng các hàm công cụ được định nghĩa trước `main()`.
- Xác minh rằng máy chủ được cấu hình đúng cách.

**Vấn đề kết nối:**
- Đảm bảo máy chủ đang sử dụng giao thức stdio đúng cách.
- Kiểm tra rằng không có tiến trình nào khác gây cản trở.
- Xác minh cú pháp lệnh Inspector.

## Bài tập

Hãy thử xây dựng máy chủ của bạn với nhiều khả năng hơn. Xem [trang này](https://api.chucknorris.io/) để, ví dụ, thêm một công cụ gọi API. Bạn quyết định máy chủ sẽ trông như thế nào. Chúc vui vẻ :)

## Giải pháp

[Giải pháp](./solution/README.md) Đây là một giải pháp có mã hoạt động.

## Điểm chính

Những điểm chính từ chương này bao gồm:

- Giao thức stdio là cơ chế được khuyến nghị cho các máy chủ MCP cục bộ.
- Giao thức stdio cho phép giao tiếp liền mạch giữa các máy chủ MCP và khách hàng sử dụng luồng đầu vào và đầu ra tiêu chuẩn.
- Bạn có thể sử dụng cả Inspector và Visual Studio Code để sử dụng trực tiếp các máy chủ stdio, giúp việc gỡ lỗi và tích hợp trở nên đơn giản.

## Mẫu

- [Java Calculator](../samples/java/calculator/README.md)
- [.Net Calculator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Calculator](../samples/javascript/README.md)
- [TypeScript Calculator](../samples/typescript/README.md)
- [Python Calculator](../../../../03-GettingStarted/samples/python) 

## Tài nguyên bổ sung

- [SSE](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events)

## Tiếp theo

## Các bước tiếp theo

Bây giờ bạn đã học cách xây dựng máy chủ MCP với giao thức stdio, bạn có thể khám phá các chủ đề nâng cao hơn:

- **Tiếp theo**: [HTTP Streaming với MCP (Streamable HTTP)](../06-http-streaming/README.md) - Tìm hiểu về cơ chế giao tiếp được hỗ trợ khác cho các máy chủ từ xa.
- **Nâng cao**: [Thực hành bảo mật MCP](../../02-Security/README.md) - Triển khai bảo mật trong các máy chủ MCP của bạn.
- **Sản xuất**: [Chiến lược triển khai](../09-deployment/README.md) - Triển khai các máy chủ của bạn để sử dụng trong môi trường sản xuất.

## Tài nguyên bổ sung

- [MCP Specification 2025-06-18](https://spec.modelcontextprotocol.io/specification/) - Đặc tả chính thức.
- [Tài liệu MCP SDK](https://github.com/modelcontextprotocol/sdk) - Tham khảo SDK cho tất cả các ngôn ngữ.
- [Ví dụ cộng đồng](../../06-CommunityContributions/README.md) - Thêm các ví dụ máy chủ từ cộng đồng.

---

**Tuyên bố miễn trừ trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ bản địa nên được coi là nguồn thông tin chính thức. Đối với các thông tin quan trọng, khuyến nghị sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm cho bất kỳ sự hiểu lầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.