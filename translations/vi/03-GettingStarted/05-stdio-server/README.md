# MCP Server với phương thức truyền stdio

> **⚠️ Cập nhật quan trọng**: Từ MCP Specification 2025-06-18, phương thức truyền SSE (Server-Sent Events) độc lập đã bị **khai tử** và được thay thế bằng phương thức "Streamable HTTP". Đặc tả MCP hiện tại định nghĩa hai cơ chế truyền chính:
> 1. **stdio** - Đầu vào/đầu ra chuẩn (được khuyến nghị cho máy chủ nội bộ)
> 2. **Streamable HTTP** - Dành cho các máy chủ từ xa có thể sử dụng SSE nội bộ
>
> Bài học này đã được cập nhật để tập trung vào **phương thức truyền stdio**, phương pháp được khuyến nghị cho hầu hết các triển khai máy chủ MCP.

Phương thức truyền stdio cho phép các máy chủ MCP giao tiếp với khách hàng thông qua các luồng đầu vào và đầu ra chuẩn. Đây là cơ chế truyền phổ biến nhất và được khuyến nghị trong đặc tả MCP hiện tại, cung cấp cách đơn giản và hiệu quả để xây dựng các máy chủ MCP có thể tích hợp dễ dàng với nhiều ứng dụng khách khác nhau.

## Tổng quan

Bài học này hướng dẫn cách xây dựng và sử dụng các máy chủ MCP sử dụng phương thức truyền stdio.

## Mục tiêu học tập

Sau bài học này, bạn sẽ có thể:

- Xây dựng máy chủ MCP sử dụng phương thức truyền stdio.
- Gỡ lỗi máy chủ MCP sử dụng Inspector.
- Sử dụng máy chủ MCP trong Visual Studio Code.
- Hiểu các cơ chế truyền MCP hiện tại và lý do tại sao stdio được khuyến nghị.

## Phương thức truyền stdio - Cách hoạt động

Phương thức truyền stdio là một trong hai loại phương thức truyền được hỗ trợ trong đặc tả MCP hiện tại (2025-06-18). Cách hoạt động như sau:

- **Giao tiếp đơn giản**: Máy chủ đọc các thông điệp JSON-RPC từ đầu vào chuẩn (`stdin`) và gửi thông điệp qua đầu ra chuẩn (`stdout`).
- **Dựa trên tiến trình**: Khách hàng khởi chạy máy chủ MCP như một tiến trình con.
- **Định dạng thông điệp**: Thông điệp là các yêu cầu, thông báo hoặc phản hồi JSON-RPC riêng biệt, được phân cách bằng dòng mới.
- **Ghi nhật ký**: Máy chủ CÓ THỂ ghi các chuỗi UTF-8 vào đầu lỗi chuẩn (`stderr`) để phục vụ ghi nhận nhật ký.

### Yêu cầu chính:
- Các thông điệp PHẢI được phân cách bằng dòng mới và KHÔNG được chứa dòng mới bên trong
- Máy chủ KHÔNG ĐƯỢC ghi bất cứ điều gì vào `stdout` không phải là thông điệp MCP hợp lệ
- Khách hàng KHÔNG ĐƯỢC ghi vào `stdin` của máy chủ bất cứ điều gì không phải là thông điệp MCP hợp lệ

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

- Chúng ta nhập lớp `Server` và `StdioServerTransport` từ MCP SDK
- Tạo một thể hiện máy chủ với cấu hình và khả năng cơ bản

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
- Định nghĩa các công cụ sử dụng decorator
- Sử dụng trình quản lý ngữ cảnh stdio_server để xử lý phương thức truyền

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

- Không yêu cầu thiết lập máy chủ web hoặc các điểm cuối HTTP
- Được khởi chạy như tiến trình con bởi khách hàng
- Giao tiếp qua các luồng stdin/stdout
- Đơn giản hơn để triển khai và gỡ lỗi

## Bài tập: Tạo máy chủ stdio

Để tạo máy chủ, chúng ta cần nhớ hai điều:

- Cần sử dụng máy chủ web để mở các điểm cuối cho kết nối và thông điệp.
## Bài thực hành: Tạo máy chủ MCP stdio đơn giản

Trong bài thực hành này, chúng ta sẽ tạo một máy chủ MCP đơn giản sử dụng phương thức truyền stdio được khuyến nghị. Máy chủ này sẽ mở các công cụ mà khách hàng có thể gọi bằng giao thức Model Context Protocol chuẩn.

### Yêu cầu

- Python 3.8 trở lên
- MCP Python SDK: `pip install mcp`
- Hiểu biết cơ bản về lập trình bất đồng bộ

Hãy bắt đầu bằng cách tạo máy chủ MCP stdio đầu tiên của bạn:

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp import types

# Cấu hình ghi log
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

## Các điểm khác biệt chính so với cách tiếp cận SSE đã bị khai tử

**Phương thức truyền Stdio (Tiêu chuẩn hiện tại):**
- Mô hình subprocess đơn giản - khách hàng khởi chạy máy chủ như tiến trình con
- Giao tiếp qua stdin/stdout sử dụng thông điệp JSON-RPC
- Không cần thiết lập máy chủ HTTP
- Hiệu suất và bảo mật tốt hơn
- Dễ dàng gỡ lỗi và phát triển

**Phương thức truyền SSE (Khai tử kể từ MCP 2025-06-18):**
- Yêu cầu máy chủ HTTP với các điểm cuối SSE
- Phức tạp hơn do cần hạ tầng máy chủ web
- Cân nhắc bảo mật thêm cho các điểm cuối HTTP
- Đã được thay thế bằng Streamable HTTP cho các kịch bản web

### Tạo máy chủ với phương thức truyền stdio

Để tạo máy chủ stdio, chúng ta cần:

1. **Nhập các thư viện cần thiết** - Các thành phần máy chủ MCP và phương thức truyền stdio
2. **Tạo một thể hiện máy chủ** - Định nghĩa máy chủ với các khả năng của nó
3. **Định nghĩa công cụ** - Thêm chức năng muốn mở cho khách hàng
4. **Cấu hình phương thức truyền** - Thiết lập giao tiếp stdio
5. **Chạy máy chủ** - Khởi động máy chủ và xử lý thông điệp

Hãy xây dựng từng bước một:

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

Lưu mã nguồn dưới tên `server.py` và chạy từ dòng lệnh:

```bash
python server.py
```

Máy chủ sẽ khởi động và chờ đầu vào từ stdin. Nó giao tiếp bằng các thông điệp JSON-RPC qua phương thức truyền stdio.

### Bước 4: Kiểm tra với Inspector

Bạn có thể kiểm tra máy chủ bằng MCP Inspector:

1. Cài đặt Inspector: `npx @modelcontextprotocol/inspector`
2. Chạy Inspector và trỏ đến máy chủ của bạn
3. Kiểm tra các công cụ bạn đã tạo

### .NET

```csharp
var builder = WebApplication.CreateBuilder(args);
builder.Services
    .AddMcpServer();
 ```
## Gỡ lỗi máy chủ stdio của bạn

### Sử dụng MCP Inspector

MCP Inspector là công cụ hữu ích để gỡ lỗi và kiểm thử các máy chủ MCP. Đây là cách sử dụng nó với máy chủ stdio:

1. **Cài đặt Inspector**:
   ```bash
   npx @modelcontextprotocol/inspector
   ```

2. **Chạy Inspector**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

3. **Kiểm tra máy chủ**: Inspector cung cấp giao diện web cho phép bạn:
   - Xem các khả năng của máy chủ
   - Kiểm thử các công cụ với các tham số khác nhau
   - Giám sát các thông điệp JSON-RPC
   - Gỡ lỗi các vấn đề kết nối

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

2. Đặt breakpoint trong mã máy chủ
3. Chạy trình gỡ lỗi và kiểm tra với Inspector

### Mẹo gỡ lỗi thường gặp

- Dùng `stderr` để ghi nhật ký - không bao giờ ghi vào `stdout` vì nó dành cho thông điệp MCP
- Đảm bảo tất cả thông điệp JSON-RPC được phân cách bằng dòng mới
- Kiểm tra với công cụ đơn giản trước khi thêm chức năng phức tạp
- Dùng Inspector để xác minh định dạng thông điệp

## Sử dụng máy chủ stdio trong VS Code

Khi bạn đã tạo xong máy chủ MCP stdio, bạn có thể tích hợp nó với VS Code để dùng với Claude hoặc các khách hàng tương thích MCP khác.

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

3. **Kiểm tra kết nối**: Bắt đầu trò chuyện với Claude và thử sử dụng các công cụ của máy chủ:
   - "Bạn có thể chào tôi dùng công cụ greeting không?"
   - "Tính tổng của 15 và 27"
   - "Thông tin máy chủ như thế nào?"

### Ví dụ máy chủ stdio TypeScript

Dưới đây là ví dụ đầy đủ bằng TypeScript để tham khảo:

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

Trong bài học cập nhật này, bạn đã học được cách:

- Xây dựng máy chủ MCP sử dụng phương thức truyền **stdio** hiện tại (phương pháp được khuyến nghị)
- Hiểu tại sao phương thức truyền SSE bị khai tử thay cho stdio và Streamable HTTP
- Tạo các công cụ có thể được gọi bởi khách hàng MCP
- Gỡ lỗi máy chủ bằng MCP Inspector
- Tích hợp máy chủ stdio với VS Code và Claude

Phương thức truyền stdio cung cấp cách xây dựng máy chủ MCP đơn giản hơn, an toàn hơn và hiệu suất tốt hơn so với cách tiếp cận SSE đã bị khai tử. Đây là phương thức truyền được khuyến nghị cho hầu hết các triển khai máy chủ MCP theo đặc tả 2025-06-18.


### .NET

1. Trước tiên, hãy tạo một số công cụ, cho việc này ta tạo tệp *Tools.cs* với nội dung sau:

  ```csharp
  using System.ComponentModel;
  using System.Text.Json;
  using ModelContextProtocol.Server;
  ```

## Bài tập: Kiểm thử máy chủ stdio của bạn

Bây giờ bạn đã xây dựng máy chủ stdio, hãy kiểm thử để chắc chắn nó hoạt động đúng.

### Yêu cầu

1. Đảm bảo bạn đã cài MCP Inspector:
   ```bash
   npm install -g @modelcontextprotocol/inspector
   ```

2. Mã máy chủ của bạn đã được lưu (ví dụ, `server.py`)

### Kiểm thử với Inspector

1. **Khởi động Inspector cùng máy chủ**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

2. **Mở giao diện web**: Inspector sẽ mở cửa sổ trình duyệt hiển thị các khả năng máy chủ.

3. **Kiểm thử các công cụ**: 
   - Thử công cụ `get_greeting` với các tên khác nhau
   - Kiểm thử công cụ `calculate_sum` với các số khác nhau
   - Gọi công cụ `get_server_info` để xem thông tin meta máy chủ

4. **Giám sát giao tiếp**: Inspector hiển thị các thông điệp JSON-RPC được trao đổi giữa khách hàng và máy chủ.

### Bạn nên thấy gì

Khi máy chủ bắt đầu đúng, bạn sẽ thấy:
- Các khả năng máy chủ được liệt kê trong Inspector
- Các công cụ sẵn sàng để kiểm thử
- Các thông điệp JSON-RPC trao đổi thành công
- Phản hồi của công cụ hiển thị trên giao diện

### Các vấn đề thường gặp và giải pháp

**Máy chủ không khởi động:**
- Kiểm tra xem tất cả các thư viện đã được cài đặt: `pip install mcp`
- Xác thực cú pháp và thụt lề Python
- Tìm lỗi trong bảng điều khiển

**Công cụ không hiển thị:**
- Đảm bảo các decorator `@server.tool()` có mặt
- Kiểm tra các hàm công cụ được định nghĩa trước `main()`
- Đảm bảo máy chủ được cấu hình đúng

**Vấn đề kết nối:**
- Đảm bảo máy chủ sử dụng phương thức truyền stdio chính xác
- Kiểm tra xem không có tiến trình khác xen vào
- Xác minh cú pháp lệnh Inspector

## Bài tập lớn

Thử phát triển thêm khả năng cho máy chủ của bạn. Tham khảo [trang này](https://api.chucknorris.io/) để ví dụ thêm công cụ gọi API. Bạn quyết định máy chủ sẽ trông như thế nào. Chúc bạn vui :)

## Giải pháp

[Giải pháp](./solution/README.md) Đây là một giải pháp có mã hoạt động.

## Những điểm chính cần nhớ

Những điểm chính rút ra từ chương này là:

- Phương thức truyền stdio là cơ chế được khuyến nghị cho các máy chủ MCP nội bộ.
- Phương thức stdio cho phép giao tiếp liền mạch giữa các máy chủ MCP và khách hàng sử dụng luồng đầu vào và đầu ra chuẩn.
- Bạn có thể sử dụng cả Inspector và Visual Studio Code để sử dụng trực tiếp các máy chủ stdio, giúp việc gỡ lỗi và tích hợp dễ dàng.

## Mẫu mã

- [Máy tính Java](../samples/java/calculator/README.md)
- [Máy tính .Net](../../../../03-GettingStarted/samples/csharp)
- [Máy tính JavaScript](../samples/javascript/README.md)
- [Máy tính TypeScript](../samples/typescript/README.md)
- [Máy tính Python](../../../../03-GettingStarted/samples/python) 

## Tài nguyên bổ sung

- [SSE](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events)

## Tiếp theo là gì

## Các bước tiếp theo

Bây giờ bạn đã học cách xây dựng máy chủ MCP với phương thức truyền stdio, bạn có thể khám phá các chủ đề nâng cao hơn:

- **Tiếp theo**: [HTTP Streaming với MCP (Streamable HTTP)](../06-http-streaming/README.md) - Tìm hiểu về cơ chế truyền khác được hỗ trợ cho máy chủ từ xa
- **Nâng cao**: [Thực hành bảo mật MCP](../../02-Security/README.md) - Triển khai bảo mật trong máy chủ MCP
- **Triển khai sản xuất**: [Chiến lược triển khai](../09-deployment/README.md) - Triển khai máy chủ cho môi trường sản xuất

## Tài nguyên bổ sung

- [Đặc tả MCP 2025-06-18](https://spec.modelcontextprotocol.io/specification/) - Đặc tả chính thức
- [Tài liệu MCP SDK](https://github.com/modelcontextprotocol/sdk) - Tham khảo SDK cho các ngôn ngữ
- [Ví dụ cộng đồng](../../06-CommunityContributions/README.md) - Thêm ví dụ máy chủ từ cộng đồng

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Tuyên bố từ chối trách nhiệm**:
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ gốc của nó nên được xem là nguồn thông tin chính xác và đáng tin cậy. Đối với những thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm về bất kỳ hiểu lầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->