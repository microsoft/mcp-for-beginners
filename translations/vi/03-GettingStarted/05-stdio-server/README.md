# MCP Server với giao thức stdio

> **⚠️ Cập nhật quan trọng**: Kể từ MCP Specification 2025-06-18, giao thức SSE (Server-Sent Events) độc lập đã bị **ngưng sử dụng** và được thay thế bằng giao thức "Streamable HTTP". Bộ tiêu chuẩn MCP hiện tại định nghĩa hai cơ chế giao thức chính:
> 1. **stdio** - Đầu vào/đầu ra chuẩn (khuyến nghị cho các máy chủ cục bộ)
> 2. **Streamable HTTP** - Dành cho các máy chủ từ xa có thể sử dụng SSE nội bộ
>
> Bài học này đã được cập nhật để tập trung vào **giao thức stdio**, đây là cách tiếp cận được khuyến nghị cho hầu hết các triển khai MCP server.

Giao thức stdio cho phép các MCP server giao tiếp với client thông qua các dòng dữ liệu đầu vào và đầu ra chuẩn. Đây là cơ chế giao thức phổ biến nhất và được khuyến nghị trong bộ tiêu chuẩn MCP hiện tại, cung cấp một cách đơn giản và hiệu quả để xây dựng MCP server có thể dễ dàng tích hợp với các ứng dụng client khác nhau.

## Tổng quan

Bài học này sẽ hướng dẫn cách xây dựng và sử dụng MCP Server bằng giao thức stdio.

## Mục tiêu học tập

Sau bài học này, bạn sẽ có thể:

- Xây dựng MCP Server sử dụng giao thức stdio.
- Gỡ lỗi MCP Server bằng Inspector.
- Sử dụng MCP Server trong Visual Studio Code.
- Hiểu các cơ chế giao thức MCP hiện tại và lý do vì sao stdio được khuyến nghị.

## Giao thức stdio - Cách hoạt động

Giao thức stdio là một trong hai loại giao thức được hỗ trợ trong tiêu chuẩn MCP hiện tại (2025-06-18). Cách hoạt động như sau:

- **Giao tiếp đơn giản**: Server đọc các thông điệp JSON-RPC từ đầu vào chuẩn (`stdin`) và gửi thông điệp ra đầu ra chuẩn (`stdout`).
- **Dựa trên tiến trình**: Client khởi chạy MCP server dưới dạng tiến trình con.
- **Định dạng thông điệp**: Thông điệp là các yêu cầu, thông báo hoặc phản hồi JSON-RPC riêng biệt, phân cách bằng dòng mới.
- **Ghi log**: Server CÓ THỂ ghi chuỗi UTF-8 vào đầu ra lỗi chuẩn (`stderr`) để phục vụ ghi log.

### Yêu cầu chính:
- Thông điệp PHẢI được phân tách bằng dòng mới và KHÔNG được chứa dòng mới nhúng trong thông điệp
- Server KHÔNG PHẢI ghi gì vào `stdout` mà không phải thông điệp MCP hợp lệ
- Client KHÔNG PHẢI ghi gì vào `stdin` của server mà không phải thông điệp MCP hợp lệ

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

- Chúng ta import lớp `Server` và `StdioServerTransport` từ MCP SDK
- Tạo một instance server với cấu hình và khả năng cơ bản
- Tạo một instance `StdioServerTransport` và kết nối server với nó, cho phép giao tiếp qua stdin/stdout

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

- Tạo một instance server sử dụng MCP SDK
- Định nghĩa các công cụ (tools) bằng cách sử dụng decorators
- Sử dụng context manager stdio_server để xử lý giao thức

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

Điểm khác biệt chính so với SSE là các server stdio:

- Không yêu cầu thiết lập web server hoặc các endpoint HTTP
- Được client khởi chạy dưới dạng tiến trình con
- Giao tiếp qua các dòng stdin/stdout
- Đơn giản hơn để triển khai và gỡ lỗi

## Bài tập: Tạo server stdio

Để tạo server, chúng ta cần lưu ý hai điểm:

- Cần sử dụng web server để cung cấp các endpoint cho kết nối và tin nhắn.

## Thực hành: Tạo một MCP stdio server đơn giản

Trong bài lab này, chúng ta sẽ tạo một MCP server đơn giản sử dụng giao thức stdio được khuyến nghị. Server này sẽ cung cấp các công cụ mà client có thể gọi thông qua giao thức Model Context Protocol chuẩn.

### Điều kiện cần chuẩn bị

- Python 3.8 hoặc mới hơn
- MCP Python SDK: `pip install mcp`
- Hiểu biết cơ bản về lập trình bất đồng bộ (async)

Bắt đầu bằng cách tạo MCP stdio server đầu tiên:

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
    # Sử dụng phương thức truyền stdio
    async with stdio_server(server) as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            server.create_initialization_options()
        )

if __name__ == "__main__":
    asyncio.run(main())
```


## Sự khác biệt chính so với phương pháp SSE đã bị ngưng

**Giao thức Stdio (Tiêu chuẩn hiện tại):**
- Mô hình tiến trình con đơn giản - client khởi chạy server dưới dạng tiến trình con
- Giao tiếp qua stdin/stdout dùng các thông điệp JSON-RPC
- Không cần thiết lập web server HTTP
- Hiệu năng và bảo mật tốt hơn
- Dễ dàng gỡ lỗi và phát triển hơn

**Giao thức SSE (Ngưng sử dụng từ MCP 2025-06-18):**
- Yêu cầu web server HTTP với các endpoint SSE
- Thiết lập phức tạp hơn với hạ tầng web server
- Cần quan tâm nhiều hơn về bảo mật của các endpoint HTTP
- Đã được thay thế bằng Streamable HTTP cho các kịch bản web

### Tạo server với giao thức stdio

Để tạo server stdio, chúng ta cần:

1. **Import thư viện cần thiết** - Bao gồm các thành phần MCP server và giao thức stdio
2. **Tạo instance server** - Định nghĩa server với các khả năng của nó
3. **Định nghĩa công cụ** - Thêm các chức năng muốn cung cấp
4. **Cấu hình giao thức** - Thiết lập giao tiếp stdio
5. **Khởi động server** - Bắt đầu server và xử lý tin nhắn

Hãy xây dựng theo từng bước:

### Bước 1: Tạo server stdio cơ bản

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

### Bước 3: Chạy server

Lưu mã code dưới tên `server.py` và chạy từ dòng lệnh:

```bash
python server.py
```

Server sẽ khởi động và đợi dữ liệu từ stdin. Nó giao tiếp bằng các thông điệp JSON-RPC qua giao thức stdio.

### Bước 4: Kiểm thử bằng Inspector

Bạn có thể kiểm thử server bằng MCP Inspector:

1. Cài đặt Inspector: `npx @modelcontextprotocol/inspector`
2. Chạy Inspector và trỏ đến server của bạn
3. Thử nghiệm các công cụ bạn đã tạo

### .NET

```csharp
var builder = WebApplication.CreateBuilder(args);
builder.Services
    .AddMcpServer();
 ```


## Gỡ lỗi server stdio

### Sử dụng MCP Inspector

Inspector MCP là công cụ hữu ích để gỡ lỗi và kiểm tra MCP server. Đây là cách dùng nó với server stdio của bạn:

1. **Cài đặt Inspector**:
   ```bash
   npx @modelcontextprotocol/inspector
   ```

2. **Chạy Inspector**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

3. **Kiểm thử server**: Inspector cung cấp giao diện web cho phép bạn:
   - Xem các khả năng của server
   - Thử các công cụ với nhiều tham số khác nhau
   - Giám sát các thông điệp JSON-RPC
   - Gỡ lỗi các sự cố kết nối

### Sử dụng VS Code

Bạn cũng có thể gỡ lỗi MCP server trực tiếp trong VS Code:

1. Tạo cấu hình launch trong `.vscode/launch.json`:
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

2. Đặt breakpoint trong mã server
3. Chạy debugger và kiểm thử với Inspector

### Mẹo gỡ lỗi phổ biến

- Sử dụng `stderr` để ghi log - không bao giờ ghi vào `stdout` vì nó dành riêng cho thông điệp MCP
- Đảm bảo tất cả thông điệp JSON-RPC được phân tách bằng dòng mới
- Thử các công cụ đơn giản trước khi thêm chức năng phức tạp
- Dùng Inspector để xác thực định dạng thông điệp

## Sử dụng server stdio trong VS Code

Khi đã xây dựng MCP stdio server, bạn có thể tích hợp với VS Code để dùng với Claude hoặc các client tương thích MCP khác.

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

2. **Khởi động lại Claude**: Đóng và mở lại Claude để tải cấu hình server mới.

3. **Kiểm thử kết nối**: Bắt đầu cuộc trò chuyện với Claude và thử sử dụng các công cụ của server:
   - "Bạn có thể chào tôi bằng công cụ greeting không?"
   - "Tính tổng 15 và 27"
   - "Thông tin server là gì?"

### Ví dụ server stdio TypeScript

Dưới đây là ví dụ TypeScript hoàn chỉnh để tham khảo:

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


### Ví dụ server stdio .NET

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

## Tổng kết

Trong bài học cập nhật này, bạn đã học được cách:

- Xây dựng MCP server sử dụng **giao thức stdio hiện tại** (cách tiếp cận được khuyến nghị)
- Hiểu lý do giao thức SSE bị ngưng và được thay thế bằng stdio và Streamable HTTP
- Tạo công cụ có thể được gọi bởi client MCP
- Gỡ lỗi server bằng MCP Inspector
- Tích hợp server stdio với VS Code và Claude

Giao thức stdio cung cấp cách đơn giản hơn, bảo mật hơn, và hiệu năng cao hơn để xây dựng MCP server so với phương pháp SSE đã ngưng sử dụng. Đây là giao thức được khuyến nghị cho phần lớn triển khai MCP server theo tiêu chuẩn 2025-06-18.

### .NET

1. Trước tiên chúng ta tạo một số công cụ, cho việc này chúng ta tạo file *Tools.cs* với nội dung sau:

  ```csharp
  using System.ComponentModel;
  using System.Text.Json;
  using ModelContextProtocol.Server;
  ```


## Bài tập: Kiểm thử server stdio

Khi đã xây dựng server stdio, hãy thử kiểm thử nó để đảm bảo hoạt động chính xác.

### Điều kiện cần chuẩn bị

1. Đảm bảo bạn đã cài đặt MCP Inspector:
   ```bash
   npm install -g @modelcontextprotocol/inspector
   ```

2. Mã server của bạn đã được lưu (ví dụ `server.py`)

### Kiểm thử với Inspector

1. **Khởi động Inspector cùng server**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

2. **Mở giao diện web**: Inspector sẽ mở cửa sổ trình duyệt hiển thị khả năng của server bạn.

3. **Thử các công cụ**:
   - Thử công cụ `get_greeting` với các tên khác nhau
   - Kiểm tra công cụ `calculate_sum` với các số khác nhau
   - Gọi công cụ `get_server_info` để xem metadata server

4. **Giám sát giao tiếp**: Inspector hiển thị các thông điệp JSON-RPC trao đổi giữa client và server.

### Những gì bạn nên thấy

Khi server khởi động đúng, bạn sẽ thấy:
- Danh sách khả năng server trong Inspector
- Các công cụ sẵn dùng để kiểm thử
- Trao đổi thông điệp JSON-RPC thành công
- Phản hồi của công cụ hiển thị trong giao diện

### Các vấn đề phổ biến và cách khắc phục

**Server không khởi động:**
- Kiểm tra đã cài đủ phụ thuộc: `pip install mcp`
- Kiểm tra cú pháp và thụt lề Python
- Xem lỗi trong console

**Công cụ không hiện ra:**
- Đảm bảo có decorators `@server.tool()`
- Kiểm tra các hàm công cụ được định nghĩa trước `main()`
- Đảm bảo server được cấu hình đúng

**Vấn đề kết nối:**
- Đảm bảo server sử dụng giao thức stdio đúng cách
- Kiểm tra không có tiến trình nào khác gây xung đột
- Xác minh cú pháp lệnh Inspector

## Bài tập

Hãy tiếp tục mở rộng server với nhiều khả năng hơn. Tham khảo [trang này](https://api.chucknorris.io/) để ví dụ thêm công cụ gọi API. Bạn quyết định server sẽ trông như thế nào. Chúc vui :)

## Giải pháp

[Giải pháp](./solution/README.md) Đây là một giải pháp có mã hoạt động.

## Những điểm chính cần ghi nhớ

Điểm chính rút ra trong chương này:

- Giao thức stdio là cơ chế được khuyến nghị cho các server MCP cục bộ.
- Giao thức stdio cho phép giao tiếp liền mạch giữa server MCP và client sử dụng dòng đầu vào và đầu ra chuẩn.
- Bạn có thể dùng cả Inspector và Visual Studio Code để sử dụng server stdio trực tiếp, giúp gỡ lỗi và tích hợp dễ dàng hơn.

## Mẫu ví dụ

- [Máy tính Java](../samples/java/calculator/README.md)
- [Máy tính .Net](../../../../03-GettingStarted/samples/csharp)
- [Máy tính JavaScript](../samples/javascript/README.md)
- [Máy tính TypeScript](../samples/typescript/README.md)
- [Máy tính Python](../../../../03-GettingStarted/samples/python)

## Tài nguyên bổ sung

- [SSE](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events)

## Tiếp theo

## Bước tiếp theo

Sau khi bạn đã biết cách xây dựng MCP server với giao thức stdio, bạn có thể khám phá các chủ đề nâng cao hơn:

- **Tiếp theo**: [HTTP Streaming với MCP (Streamable HTTP)](../06-http-streaming/README.md) - Tìm hiểu về cơ chế giao thức khác được hỗ trợ cho server từ xa
- **Nâng cao**: [Các thực hành bảo mật MCP tốt nhất](../../02-Security/README.md) - Triển khai bảo mật cho MCP server
- **Sản xuất**: [Chiến lược triển khai](../09-deployment/README.md) - Triển khai server cho môi trường sản xuất

## Tài nguyên bổ sung

- [MCP Specification 2025-06-18](https://spec.modelcontextprotocol.io/specification/) - Tiêu chuẩn chính thức
- [Tài liệu SDK MCP](https://github.com/modelcontextprotocol/sdk) - Tài liệu tham khảo SDK cho tất cả ngôn ngữ
- [Ví dụ cộng đồng](../../06-CommunityContributions/README.md) - Thêm ví dụ server từ cộng đồng

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Tuyên bố từ chối trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Trong khi chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng bản dịch tự động có thể chứa lỗi hoặc sự không chính xác. Tài liệu gốc bằng ngôn ngữ bản địa nên được xem là nguồn chính xác và đáng tin cậy. Đối với các thông tin quan trọng, nên sử dụng dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm đối với bất kỳ sự hiểu nhầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->