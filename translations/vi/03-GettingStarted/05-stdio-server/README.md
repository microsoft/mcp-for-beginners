# Máy chủ MCP với giao thức stdio

> **⚠️ Cập nhật quan trọng**: Kể từ đặc tả MCP ngày 2025-06-18, giao thức SSE (Server-Sent Events) độc lập đã bị **loại bỏ** và thay thế bằng giao thức "HTTP có thể truyền phát". Đặc tả MCP hiện tại định nghĩa hai cơ chế giao thức chính:
> 1. **stdio** - Đầu vào/đầu ra tiêu chuẩn (khuyến nghị cho các máy chủ cục bộ)
> 2. **HTTP có thể truyền phát** - Dành cho các máy chủ từ xa có thể sử dụng SSE bên trong
>
> Bài học này đã được cập nhật tập trung vào **giao thức stdio**, là cách tiếp cận được khuyến nghị cho hầu hết các triển khai máy chủ MCP.

Giao thức stdio cho phép các máy chủ MCP giao tiếp với khách hàng qua các luồng đầu vào và đầu ra tiêu chuẩn. Đây là cơ chế giao thức được sử dụng phổ biến nhất và được khuyến nghị trong đặc tả MCP hiện tại, cung cấp một cách đơn giản và hiệu quả để xây dựng máy chủ MCP có thể dễ dàng tích hợp với nhiều ứng dụng khách khác nhau.

## Tổng quan

Bài học này hướng dẫn cách xây dựng và sử dụng Máy chủ MCP sử dụng giao thức stdio.

## Mục tiêu học tập

Đến cuối bài học này, bạn sẽ có khả năng:

- Xây dựng một máy chủ MCP sử dụng giao thức stdio.
- Gỡ lỗi một máy chủ MCP bằng Inspector.
- Sử dụng máy chủ MCP bằng Visual Studio Code.
- Hiểu các cơ chế giao thức MCP hiện tại và tại sao stdio được khuyến nghị.


## Giao thức stdio - Cách thức hoạt động

Giao thức stdio là một trong hai giao thức tiêu chuẩn trong đặc tả MCP
`2026-07-28`. Đây là cách hoạt động:

- **Giao tiếp đơn giản**: Máy chủ đọc các thông điệp JSON-RPC từ đầu vào tiêu chuẩn (`stdin`) và gửi thông điệp đến đầu ra tiêu chuẩn (`stdout`).
- **Dựa trên tiến trình**: Khách hàng khởi chạy máy chủ MCP như một tiến trình con.
- **Định dạng thông điệp**: Thông điệp là các yêu cầu, thông báo hoặc phản hồi JSON-RPC riêng biệt, được phân cách bằng dòng mới.
- **Ghi nhật ký**: Máy chủ CÓ THỂ ghi chuỗi UTF-8 vào đầu ra lỗi tiêu chuẩn (`stderr`) để mục đích ghi nhật ký.

### Yêu cầu chính:
- Thông điệp PHẢI được phân cách bằng dòng mới và KHÔNG PHẢI chứa dòng mới nhúng
- Máy chủ KHÔNG được ghi gì vào `stdout` nếu không phải là thông điệp MCP hợp lệ
- Khách hàng KHÔNG được ghi gì vào `stdin` của máy chủ nếu không phải là thông điệp MCP hợp lệ

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

Trong mã trên:

- Chúng ta nhập lớp `Server` và `StdioServerTransport` từ SDK MCP
- Tạo một thể hiện máy chủ với cấu hình và khả năng cơ bản
- Tạo một thể hiện `StdioServerTransport` và kết nối máy chủ với nó, cho phép giao tiếp qua stdin/stdout

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

Trong mã trên chúng ta:

- Tạo một thể hiện máy chủ sử dụng SDK MCP
- Định nghĩa các công cụ bằng decorators
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

Sự khác biệt chính so với SSE là các máy chủ stdio:

- Không yêu cầu thiết lập máy chủ web hoặc điểm cuối HTTP
- Được khởi chạy như tiến trình con bởi khách hàng
- Giao tiếp qua các luồng stdin/stdout
- Dễ dàng triển khai và gỡ lỗi hơn

## Bài tập: Tạo máy chủ stdio

Để tạo máy chủ của chúng ta, cần lưu ý hai điều:

- Cần sử dụng một máy chủ web để lộ các điểm cuối cho kết nối và thông điệp.
## Thực hành: Tạo máy chủ MCP stdio đơn giản

Trong bài thực hành này, chúng ta sẽ tạo một máy chủ MCP đơn giản sử dụng giao thức stdio được khuyến nghị. Máy chủ này sẽ cung cấp các công cụ mà khách hàng có thể gọi bằng giao thức Model Context tiêu chuẩn.

### Yêu cầu trước

- Python 3.8 hoặc mới hơn
- SDK MCP Python: `pip install mcp`
- Hiểu biết cơ bản về lập trình bất đồng bộ

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

## Những khác biệt chính so với cách tiếp cận SSE bị loại bỏ

**Giao thức Stdio (Tiêu chuẩn hiện tại):**
- Mô hình tiến trình con đơn giản - khách hàng khởi chạy máy chủ như một tiến trình con
- Giao tiếp qua stdin/stdout sử dụng thông điệp JSON-RPC
- Không cần thiết lập máy chủ HTTP
- Hiệu năng và bảo mật tốt hơn
- Dễ dàng gỡ lỗi và phát triển

**Giao thức SSE (Bị loại bỏ từ MCP 2025-06-18):**
- Yêu cầu máy chủ HTTP với các điểm cuối SSE
- Thiết lập phức tạp hơn với hạ tầng máy chủ web
- Cân nhắc bảo mật bổ sung cho các điểm cuối HTTP
- Hiện được thay thế bằng HTTP có thể truyền phát cho các kịch bản web

### Tạo máy chủ với giao thức stdio

Để tạo máy chủ stdio, chúng ta cần:

1. **Nhập các thư viện cần thiết** - Cần các thành phần máy chủ MCP và giao thức stdio
2. **Tạo một thể hiện máy chủ** - Định nghĩa máy chủ với các khả năng của nó
3. **Định nghĩa công cụ** - Thêm các chức năng muốn cung cấp
4. **Cấu hình giao thức** - Cấu hình giao tiếp stdio
5. **Chạy máy chủ** - Khởi động máy chủ và xử lý thông điệp

Hãy xây dựng từng bước:

### Bước 1: Tạo máy chủ stdio cơ bản

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

Lưu mã vào `server.py` và chạy nó từ dòng lệnh:

```bash
python server.py
```

Máy chủ sẽ khởi động và chờ đầu vào từ stdin. Nó giao tiếp sử dụng các thông điệp JSON-RPC qua giao thức stdio.

### Bước 4: Kiểm tra với Inspector

Bạn có thể kiểm tra máy chủ của bạn bằng MCP Inspector:

1. Cài đặt Inspector: `npx @modelcontextprotocol/inspector`
2. Chạy Inspector và trỏ tới máy chủ của bạn
3. Kiểm tra các công cụ bạn đã tạo

### .NET

```csharp
var builder = WebApplication.CreateBuilder(args);
builder.Services
    .AddMcpServer();
 ```
## Gỡ lỗi máy chủ stdio của bạn

### Sử dụng MCP Inspector

MCP Inspector là công cụ hữu ích để gỡ lỗi và kiểm thử máy chủ MCP. Đây là cách sử dụng với máy chủ stdio của bạn:

1. **Cài đặt Inspector**:
   ```bash
   npx @modelcontextprotocol/inspector
   ```

2. **Chạy Inspector**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

3. **Kiểm tra máy chủ**: Inspector cung cấp giao diện web giúp bạn:
   - Xem các khả năng máy chủ
   - Thử nghiệm các công cụ với nhiều tham số khác nhau
   - Giám sát các thông điệp JSON-RPC
   - Gỡ lỗi các sự cố kết nối

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

2. Đặt điểm dừng trong mã máy chủ của bạn
3. Chạy trình gỡ lỗi và kiểm tra với Inspector

### Mẹo gỡ lỗi chung

- Sử dụng `stderr` để ghi nhật ký - không bao giờ viết vào `stdout` vì nó dành riêng cho thông điệp MCP
- Đảm bảo mọi thông điệp JSON-RPC được phân cách bằng dòng mới
- Thử nghiệm với các công cụ đơn giản trước khi thêm chức năng phức tạp
- Dùng Inspector để xác minh định dạng thông điệp

## Sử dụng máy chủ stdio của bạn trong VS Code

Khi bạn đã xây dựng xong máy chủ MCP stdio, bạn có thể tích hợp nó với VS Code để dùng với Claude hoặc các khách hàng tương thích MCP khác.

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

3. **Kiểm tra kết nối**: Bắt đầu cuộc trò chuyện với Claude và thử dùng các công cụ của máy chủ bạn:
   - "Bạn có thể chào tôi bằng công cụ chào hỏi không?"
   - "Tính tổng của 15 và 27"
   - "Thông tin máy chủ là gì?"

### Ví dụ máy chủ stdio TypeScript

Đây là ví dụ TypeScript hoàn chỉnh để tham khảo:

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

- Xây dựng máy chủ MCP sử dụng giao thức **stdio transport** hiện tại (cách tiếp cận khuyến nghị)
- Hiểu tại sao giao thức SSE bị loại bỏ thay thế bằng stdio và HTTP có thể truyền phát
- Tạo các công cụ có thể được khách hàng MCP gọi
- Gỡ lỗi máy chủ sử dụng MCP Inspector
- Tích hợp máy chủ stdio với VS Code và Claude

Giao thức stdio cung cấp một cách đơn giản hơn, bảo mật hơn và hiệu quả hơn để xây dựng máy chủ MCP so với cách tiếp cận SSE đã bị loại bỏ. Đây là giao thức được khuyến nghị cho hầu hết các triển khai máy chủ MCP kể từ đặc tả ngày 2025-06-18.


### .NET

1. Trước tiên hãy tạo vài công cụ, cho việc này chúng ta sẽ tạo tệp *Tools.cs* với nội dung sau:

  ```csharp
  using System.ComponentModel;
  using System.Text.Json;
  using ModelContextProtocol.Server;
  ```

## Bài tập: Kiểm thử máy chủ stdio của bạn

Bây giờ bạn đã xây dựng máy chủ stdio, hãy kiểm thử để chắc chắn nó hoạt động chính xác.

### Yêu cầu trước

1. Đảm bảo bạn đã cài đặt MCP Inspector:
   ```bash
   npm install -g @modelcontextprotocol/inspector
   ```

2. Mã máy chủ của bạn nên được lưu (ví dụ, dưới tên `server.py`)

### Kiểm thử với Inspector

1. **Khởi động Inspector với máy chủ của bạn**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

2. **Mở giao diện web**: Inspector sẽ mở trình duyệt hiển thị khả năng máy chủ của bạn.

3. **Kiểm thử các công cụ**: 
   - Thử công cụ `get_greeting` với các tên khác nhau
   - Kiểm thử công cụ `calculate_sum` với các số khác nhau
   - Gọi công cụ `get_server_info` để xem siêu dữ liệu máy chủ

4. **Giám sát giao tiếp**: Inspector hiển thị các thông điệp JSON-RPC được trao đổi giữa khách hàng và máy chủ.

### Những gì bạn nên thấy

Khi máy chủ của bạn khởi động đúng cách, bạn sẽ thấy:
- Các khả năng máy chủ được liệt kê trong Inspector
- Các công cụ có sẵn để kiểm thử
- Trao đổi thành công các thông điệp JSON-RPC
- Các phản hồi công cụ hiển thị trong giao diện

### Vấn đề phổ biến và cách giải quyết

**Máy chủ không khởi động:**
- Kiểm tra tất cả các phụ thuộc đã được cài đặt: `pip install mcp`
- Xác nhận cú pháp và thụt lề Python
- Tìm thông báo lỗi trong bảng điều khiển

**Công cụ không xuất hiện:**
- Đảm bảo các decorator `@server.tool()` có mặt
- Kiểm tra các hàm công cụ được định nghĩa trước `main()`
- Xác nhận máy chủ đã được cấu hình đúng

**Sự cố kết nối:**
- Đảm bảo máy chủ sử dụng đúng giao thức stdio
- Kiểm tra xem có tiến trình khác nào can thiệp không
- Xác nhận cú pháp câu lệnh Inspector

## Bài tập về nhà

Hãy thử mở rộng máy chủ với nhiều khả năng hơn. Xem [trang này](https://api.chucknorris.io/) để, ví dụ, thêm công cụ gọi API. Bạn quyết định máy chủ sẽ như thế nào. Chúc vui :)
## Giải pháp

[Giải pháp](./solution/README.md) Đây là một giải pháp có thể với mã hoạt động.

## Những điểm chính cần ghi nhớ

Những điểm chính trong chương này là:

- Giao thức stdio là cơ chế được khuyến nghị cho các máy chủ MCP cục bộ.
- Giao thức stdio cho phép giao tiếp liền mạch giữa máy chủ MCP và khách hàng qua các luồng đầu vào và đầu ra tiêu chuẩn.
- Bạn có thể sử dụng cả Inspector và Visual Studio Code để sử dụng máy chủ stdio trực tiếp, giúp gỡ lỗi và tích hợp dễ dàng.

## Mẫu minh họa

- [Máy tính Java](../samples/java/calculator/README.md)
- [Máy tính .NET](../../../../03-GettingStarted/samples/csharp)
- [Máy tính JavaScript](../samples/javascript/README.md)
- [Máy tính TypeScript](../samples/typescript/README.md)
- [Máy tính Python](../../../../03-GettingStarted/samples/python) 

## Tài nguyên bổ sung

- [SSE](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events)

## Tiếp theo

## Các bước tiếp theo

Bây giờ bạn đã học cách xây dựng máy chủ MCP với giao thức stdio, bạn có thể khám phá các chủ đề nâng cao hơn:

- **Tiếp theo**: [HTTP Streaming với MCP (Streamable HTTP)](../06-http-streaming/README.md) - Tìm hiểu về cơ chế giao thức khác được hỗ trợ cho máy chủ từ xa
- **Nâng cao**: [Thực hành bảo mật MCP](../../02-Security/README.md) - Triển khai bảo mật cho máy chủ MCP của bạn
- **Sản xuất**: [Chiến lược triển khai](../09-deployment/README.md) - Triển khai máy chủ cho môi trường thực tế

## Tài nguyên bổ sung

- [Đặc tả MCP 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/) - Đặc tả hiện tại
- [Tài liệu SDK MCP](https://github.com/modelcontextprotocol/sdk) - Tài liệu SDK cho tất cả các ngôn ngữ
- [Ví dụ cộng đồng](../../06-CommunityContributions/README.md) - Nhiều ví dụ máy chủ khác từ cộng đồng

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Tuyên bố miễn trừ trách nhiệm**:
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng bản dịch tự động có thể chứa lỗi hoặc sai sót. Tài liệu gốc bằng ngôn ngữ gốc nên được coi là nguồn tin chính thức. Đối với thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm về bất kỳ hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->