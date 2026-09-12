# Máy chủ MCP với giao thức stdio

> **⚠️ Cập nhật quan trọng**: Theo đặc tả MCP ngày 2025-06-18, giao thức SSE độc lập (Server-Sent Events) đã bị **ngừng sử dụng** và được thay thế bằng giao thức "Streamable HTTP". Đặc tả MCP hiện tại định nghĩa hai cơ chế giao thức chính:
> 1. **stdio** - Nhập/xuất chuẩn (khuyên dùng cho máy chủ cục bộ)
> 2. **Streamable HTTP** - Dành cho máy chủ từ xa có thể sử dụng SSE nội bộ
>
> Bài học này đã được cập nhật để tập trung vào **giao thức stdio**, đây là cách tiếp cận được khuyến nghị cho hầu hết các triển khai máy chủ MCP.

Giao thức stdio cho phép máy chủ MCP giao tiếp với các khách hàng thông qua các luồng nhập và xuất chuẩn. Đây là cơ chế giao thức được sử dụng phổ biến nhất và được khuyến nghị trong đặc tả MCP hiện tại, cung cấp một cách đơn giản và hiệu quả để xây dựng máy chủ MCP có thể dễ dàng tích hợp với các ứng dụng khách đa dạng.

## Tổng quan

Bài học này hướng dẫn cách xây dựng và sử dụng các máy chủ MCP bằng giao thức stdio.

## Mục tiêu học tập

Sau bài học này, bạn sẽ có thể:

- Xây dựng một máy chủ MCP sử dụng giao thức stdio.
- Gỡ lỗi một máy chủ MCP bằng Inspector.
- Sử dụng một máy chủ MCP với Visual Studio Code.
- Hiểu các cơ chế giao thức MCP hiện tại và lý do tại sao giao thức stdio được khuyến nghị.


## Giao thức stdio - Cách hoạt động

Giao thức stdio là một trong hai giao thức tiêu chuẩn trong Đặc tả MCP
`2026-07-28`. Cách hoạt động như sau:

- **Giao tiếp đơn giản**: Máy chủ đọc các thông điệp JSON-RPC từ đầu vào chuẩn (`stdin`) và gửi thông điệp qua đầu ra chuẩn (`stdout`).
- **Dựa trên tiến trình**: Khách hàng khởi chạy máy chủ MCP như một tiến trình con.
- **Định dạng thông điệp**: Các thông điệp là các yêu cầu, thông báo hoặc phản hồi JSON-RPC riêng biệt, phân cách bằng dòng mới.
- **Ghi nhật ký**: Máy chủ CÓ THỂ ghi các chuỗi UTF-8 vào đầu ra lỗi chuẩn (`stderr`) cho mục đích ghi nhật ký.

### Yêu cầu chính:
- Thông điệp PHẢI được phân cách bằng dòng mới và KHÔNG ĐƯỢC chứa dòng mới nhúng bên trong
- Máy chủ KHÔNG ĐƯỢC gửi bất kỳ dữ liệu nào lên `stdout` không phải là thông điệp MCP hợp lệ
- Khách hàng KHÔNG ĐƯỢC gửi bất kỳ dữ liệu nào vào `stdin` máy chủ không phải là thông điệp MCP hợp lệ

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

async function runServer() {
  const transport = new StdioServerTransport();
  await server.connect(transport);
}

runServer().catch(console.error);
```

Trong đoạn mã trên:

- Chúng ta nhập lớp `Server` và `StdioServerTransport` từ MCP SDK
- Tạo một thể hiện máy chủ với cấu hình và khả năng cơ bản
- Tạo một thể hiện `StdioServerTransport` và kết nối máy chủ với nó, kích hoạt giao tiếp qua stdin/stdout

### Python

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server

# Tạo phiên bản máy chủ
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

- Tạo một thể hiện máy chủ sử dụng MCP SDK
- Định nghĩa các công cụ dùng decorators
- Sử dụng trình quản lý ngữ cảnh stdio_server để xử lý giao thức

### .NET

```csharp
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;
using Microsoft.Extensions.Logging;
using ModelContextProtocol.Server;

var builder = Host.CreateApplicationBuilder(args);

builder.Services
    .AddMcpServer()
    .WithStdioServerTransport()
    .WithTools<Tools>();

builder.Services.AddLogging(logging => logging.AddConsole());

var app = builder.Build();
await app.RunAsync();
```

Điểm khác biệt chính so với SSE là các máy chủ stdio:

- Không yêu cầu thiết lập máy chủ web hoặc điểm cuối HTTP
- Được khởi chạy như các tiến trình con bởi khách hàng
- Giao tiếp qua các luồng stdin/stdout
- Đơn giản hơn để triển khai và gỡ lỗi

## Bài tập: Tạo máy chủ stdio

Để tạo máy chủ, chúng ta cần lưu ý hai điều:

- Chúng ta cần sử dụng máy chủ web để mở các điểm cuối cho kết nối và thông điệp.
## Lab: Tạo máy chủ MCP stdio đơn giản

Trong phòng thí nghiệm này, chúng ta sẽ tạo một máy chủ MCP đơn giản sử dụng giao thức stdio được khuyến nghị. Máy chủ này sẽ cung cấp các công cụ mà khách hàng có thể gọi qua chuẩn Model Context Protocol.

### Yêu cầu chuẩn bị

- Python 3.8 trở lên
- MCP Python SDK: `pip install mcp`
- Hiểu biết cơ bản về lập trình bất đồng bộ

Hãy bắt đầu tạo máy chủ MCP stdio đầu tiên:

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp import types

# Cấu hình ghi nhật ký
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Tạo máy chủ
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
    # Sử dụng giao thức stdio
    async with stdio_server(server) as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            server.create_initialization_options()
        )

if __name__ == "__main__":
    asyncio.run(main())
```

## Sự khác biệt chính so với phương pháp SSE đã ngừng sử dụng

**Giao thức Stdio (Tiêu chuẩn hiện tại):**
- Mô hình tiến trình con đơn giản - khách hàng khởi chạy máy chủ như tiến trình con
- Giao tiếp qua stdin/stdout dùng thông điệp JSON-RPC
- Không cần thiết lập máy chủ HTTP
- Hiệu năng và bảo mật tốt hơn
- Dễ dàng gỡ lỗi và phát triển

**Giao thức SSE (Ngừng sử dụng từ MCP 2025-06-18):**
- Yêu cầu máy chủ HTTP với các điểm cuối SSE
- Thiết lập phức tạp với cơ sở hạ tầng máy chủ web
- Cân nhắc bảo mật bổ sung cho các điểm cuối HTTP
- Hiện đã được thay thế bằng Streamable HTTP cho các kịch bản dựa trên web

### Tạo máy chủ với giao thức stdio

Để tạo máy chủ stdio, chúng ta cần:

1. **Nhập các thư viện cần thiết** - Chúng ta cần các thành phần máy chủ MCP và giao thức stdio
2. **Tạo một thể hiện máy chủ** - Định nghĩa máy chủ và các khả năng của nó
3. **Định nghĩa các công cụ** - Thêm chức năng muốn cung cấp
4. **Cấu hình giao thức** - Thiết lập giao tiếp stdio
5. **Chạy máy chủ** - Khởi động máy chủ và xử lý thông điệp

Hãy xây dựng từng bước:

### Bước 1: Tạo máy chủ stdio cơ bản

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server

# Cấu hình ghi nhật ký
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Tạo máy chủ
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

Lưu mã nguồn thành `server.py` và chạy từ dòng lệnh:

```bash
python server.py
```

Máy chủ sẽ khởi động và chờ nhập từ stdin. Nó giao tiếp bằng các thông điệp JSON-RPC qua giao thức stdio.

### Bước 4: Kiểm thử với Inspector

Bạn có thể kiểm thử máy chủ với MCP Inspector:

1. Cài đặt Inspector: `npx @modelcontextprotocol/inspector`
2. Chạy Inspector và kết nối đến máy chủ của bạn
3. Kiểm thử các công cụ bạn đã tạo

### .NET

```csharp
var builder = WebApplication.CreateBuilder(args);
builder.Services
    .AddMcpServer();
 ```
## Gỡ lỗi máy chủ stdio của bạn

### Sử dụng MCP Inspector

MCP Inspector là công cụ hữu ích để gỡ lỗi và kiểm thử máy chủ MCP. Đây là cách sử dụng nó với máy chủ stdio của bạn:

1. **Cài đặt Inspector**:
   ```bash
   npx @modelcontextprotocol/inspector
   ```

2. **Khởi chạy Inspector**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

3. **Kiểm thử máy chủ**: Inspector cung cấp giao diện web, bạn có thể:
   - Xem các khả năng của máy chủ
   - Kiểm thử công cụ với các tham số khác nhau
   - Giám sát các thông điệp JSON-RPC
   - Gỡ lỗi các sự cố kết nối

### Sử dụng VS Code

Bạn cũng có thể gỡ lỗi máy chủ MCP trực tiếp trong VS Code:

1. Tạo cấu hình khởi chạy trong file `.vscode/launch.json`:
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

2. Đặt điểm dừng trong mã máy chủ
3. Chạy trình gỡ lỗi và kiểm thử với Inspector

### Các mẹo gỡ lỗi chung

- Sử dụng `stderr` để ghi nhật ký - không bao giờ viết lên `stdout` vì nó dành cho thông điệp MCP
- Đảm bảo tất cả thông điệp JSON-RPC được phân cách bằng dòng mới
- Kiểm thử với các công cụ đơn giản trước khi thêm chức năng phức tạp
- Dùng Inspector để xác minh định dạng thông điệp

## Sử dụng máy chủ stdio của bạn trong VS Code

Sau khi xây dựng máy chủ MCP stdio, bạn có thể tích hợp với VS Code để sử dụng cùng Claude hoặc các khách hàng tương thích MCP khác.

### Cấu hình

1. **Tạo file cấu hình MCP** tại `%APPDATA%\Claude\claude_desktop_config.json` (Windows) hoặc `~/Library/Application Support/Claude/claude_desktop_config.json` (Mac):

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

3. **Kiểm thử kết nối**: Bắt đầu cuộc trò chuyện với Claude và thử dùng các công cụ từ máy chủ của bạn:
   - "Bạn có thể chào tôi bằng công cụ chào hỏi không?"
   - "Tính tổng của 15 và 27"
   - "Thông tin máy chủ là gì?"

### Ví dụ máy chủ stdio TypeScript

Đây là ví dụ đầy đủ bằng TypeScript để tham khảo:

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

// Thêm công cụ
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
    .WithStdioServerTransport()
    .WithTools<Tools>();

var app = builder.Build();
await app.RunAsync();

[McpServerToolType]
public class Tools
{
    [McpServerTool, Description("Get a personalized greeting")]
    public string GetGreeting(string name)
    {
        return $"Hello, {name}! Welcome to MCP stdio server.";
    }

    [McpServerTool, Description("Calculate the sum of two numbers")]
    public int CalculateSum(int a, int b)
    {
        return a + b;
    }
}
```

## Tóm tắt

Trong bài học cập nhật này, bạn đã học cách:

- Xây dựng máy chủ MCP sử dụng giao thức **stdio** hiện tại (cách tiếp cận được khuyến nghị)
- Hiểu lý do tại sao giao thức SSE bị ngừng sử dụng thay vào đó là stdio và Streamable HTTP
- Tạo các công cụ có thể được gọi bởi các khách hàng MCP
- Gỡ lỗi máy chủ bằng MCP Inspector
- Tích hợp máy chủ stdio với VS Code và Claude

Giao thức stdio cung cấp cách đơn giản hơn, bảo mật hơn và hiệu quả hơn để xây dựng máy chủ MCP so với phương pháp SSE đã ngừng sử dụng. Đây là giao thức được khuyến nghị cho hầu hết các triển khai máy chủ MCP theo đặc tả ngày 2025-06-18.


### .NET

1. Trước tiên, chúng ta tạo một số công cụ, cho việc này ta sẽ tạo một file *Tools.cs* với nội dung sau:

  ```csharp
  using System.ComponentModel;
  using System.Text.Json;
  using ModelContextProtocol.Server;
  ```

## Bài tập: Kiểm thử máy chủ stdio của bạn

Bây giờ bạn đã xây dựng máy chủ stdio, hãy kiểm thử để đảm bảo nó hoạt động chính xác.

### Yêu cầu chuẩn bị

1. Đảm bảo bạn đã cài MCP Inspector:
   ```bash
   npm install -g @modelcontextprotocol/inspector
   ```

2. Mã nguồn máy chủ của bạn đã được lưu (ví dụ: `server.py`)

### Kiểm thử với Inspector

1. **Khởi động Inspector cùng máy chủ**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

2. **Mở giao diện web**: Inspector sẽ mở cửa sổ trình duyệt hiển thị khả năng máy chủ của bạn.

3. **Kiểm thử các công cụ**:
   - Thử công cụ `get_greeting` với các tên khác nhau
   - Kiểm thử công cụ `calculate_sum` với các số khác nhau
   - Gọi công cụ `get_server_info` để xem metadata máy chủ

4. **Giám sát giao tiếp**: Inspector hiển thị các thông điệp JSON-RPC được trao đổi giữa khách hàng và máy chủ.

### Những gì bạn nên thấy

Khi máy chủ của bạn khởi động thành công, bạn sẽ thấy:
- Các khả năng máy chủ được liệt kê trong Inspector
- Các công cụ có sẵn để kiểm thử
- Các thông điệp JSON-RPC trao đổi thành công
- Các phản hồi công cụ hiển thị trong giao diện

### Các vấn đề thường gặp và cách khắc phục

**Máy chủ không khởi động:**
- Kiểm tra tất cả các phụ thuộc đã được cài: `pip install mcp`
- Kiểm tra cú pháp và thụt lề Python
- Tìm lỗi trên console

**Công cụ không hiển thị:**
- Đảm bảo các decorator `@server.tool()` được ghi rõ ràng
- Kiểm tra rằng các hàm công cụ được định nghĩa trước `main()`
- Đảm bảo máy chủ được cấu hình đúng

**Sự cố kết nối:**
- Đảm bảo máy chủ sử dụng đúng giao thức stdio
- Kiểm tra không có tiến trình khác can thiệp
- Xác nhận cú pháp lệnh Inspector

## Bài tập

Thử xây dựng máy chủ của bạn với nhiều chức năng hơn. Xem [trang này](https://api.chucknorris.io/) để, ví dụ, thêm công cụ gọi API. Bạn tự quyết định máy chủ sẽ như thế nào. Chúc vui :)
## Giải pháp

[Giải pháp](./solution/README.md) Đây là một giải pháp có thể với mã hoạt động.

## Những điểm chính

Những điểm chính của chương này gồm:

- Giao thức stdio là cơ chế được khuyến nghị cho các máy chủ MCP cục bộ.
- Giao thức stdio cho phép giao tiếp mượt mà giữa máy chủ và khách hàng MCP sử dụng các luồng nhập và xuất chuẩn.
- Bạn có thể sử dụng cả Inspector và Visual Studio Code để sử dụng máy chủ stdio trực tiếp, giúp việc gỡ lỗi và tích hợp dễ dàng.

## Mẫu

- [Máy tính Java](../samples/java/calculator/README.md)
- [Máy tính .Net](../../../../03-GettingStarted/samples/csharp)
- [Máy tính JavaScript](../samples/javascript/README.md)
- [Máy tính TypeScript](../samples/typescript/README.md)
- [Máy tính Python](../../../../03-GettingStarted/samples/python)

## Tài nguyên bổ sung

- [SSE](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events)

## Tiếp theo

## Các bước tiếp theo

Giờ đây bạn đã học cách xây dựng máy chủ MCP với giao thức stdio, bạn có thể khám phá các chủ đề nâng cao hơn:

- **Tiếp theo**: [HTTP Streaming với MCP (Streamable HTTP)](../06-http-streaming/README.md) - Tìm hiểu về cơ chế giao thức hỗ trợ khác cho máy chủ từ xa
- **Nâng cao**: [Thực tiễn Bảo mật MCP](../../02-Security/README.md) - Triển khai bảo mật trong máy chủ MCP của bạn
- **Sản xuất**: [Chiến lược Triển khai](../09-deployment/README.md) - Triển khai các máy chủ của bạn cho môi trường sản xuất

## Tài nguyên bổ sung

- [Đặc tả MCP 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/) - Đặc tả hiện tại
- [Tài liệu SDK MCP](https://github.com/modelcontextprotocol/sdk) - Tham khảo SDK cho mọi ngôn ngữ
- [Ví dụ cộng đồng](../../06-CommunityContributions/README.md) - Thêm nhiều ví dụ máy chủ từ cộng đồng

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Tuyên bố miễn trừ trách nhiệm**:
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng bản dịch tự động có thể chứa lỗi hoặc sai sót. Tài liệu gốc bằng ngôn ngữ gốc nên được coi là nguồn tin chính thức. Đối với thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm về bất kỳ hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->