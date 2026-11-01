# Gỡ lỗi với MCP Inspector

> [!NOTE]
> Các lệnh sử dụng `--sse` và các URL kết thúc bằng `/sse` kiểm tra truyền tải HTTP+SSE cũ.
> Đối với máy chủ MCP `2026-07-28` mới, hãy sử dụng phiên bản Inspector hỗ trợ Streamable HTTP và chọn truyền tải đó thay thế.








- **"Các công cụ của tôi có đăng ký đúng không?"** - Inspector liệt kê tất cả công cụ có sẵn
- **"Định dạng phản hồi là gì?"** - Inspector hiển thị phản hồi JSON đầy đủ
- **"Tại sao công cụ này không hoạt động?"** - Inspector hiển thị chi tiết lỗi




- npm (được cài cùng Node.js)
- Một máy chủ MCP để thử nghiệm (xem [Module 3.1 - Máy chủ đầu tiên](../01-first-server/README.md))






```bash
npx @modelcontextprotocol/inspector
```

### Tùy chọn 2: Cài đặt Toàn cục

```bash
npm install -g @modelcontextprotocol/inspector
mcp-inspector
```

### Tùy chọn 3: Thêm vào Dự án của Bạn

```bash
cd your-mcp-server-project
npm install --save-dev @modelcontextprotocol/inspector
```

Thêm vào `package.json`:
```json
{
  "scripts": {
    "inspector": "mcp-inspector"
  }
}
```

---

## Kết nối tới Máy chủ của Bạn

### Máy chủ stdio (Quy trình cục bộ)

Đối với các máy chủ giao tiếp qua đầu vào/đầu ra tiêu chuẩn:

```bash
# Python server
npx @modelcontextprotocol/inspector python -m your_server_module

# Node.js server
npx @modelcontextprotocol/inspector node ./build/index.js

# With environment variables
OPENAI_API_KEY=xxx npx @modelcontextprotocol/inspector python server.py
```

### Máy chủ SSE/HTTP (Mạng)

Đối với các máy chủ chạy như dịch vụ HTTP:

1. Khởi động máy chủ của bạn trước:
   ```bash
   python server.py  # Server running on http://localhost:8080
   ```

2. Khởi chạy Inspector và kết nối:
   ```bash
   npx @modelcontextprotocol/inspector --sse http://localhost:8080/sse
   ```

---

## Tổng quan Giao diện Inspector

Khi Inspector khởi chạy, bạn sẽ thấy giao diện web (thường tại `http://localhost:5173`):

```
┌─────────────────────────────────────────────────────────────┐
│  MCP Inspector                              [Connected ✅]   │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐         │
│  │   🔧 Tools  │  │ 📄 Resources│  │ 💬 Prompts  │         │
│  │    (3)      │  │    (2)      │  │    (1)      │         │
│  └─────────────┘  └─────────────┘  └─────────────┘         │
│                                                             │
│  ┌───────────────────────────────────────────────────────┐ │
│  │  📋 Message Log                                       │ │
│  │  ─────────────────────────────────────────────────── │ │
│  │  → initialize                                         │ │
│  │  ← initialized (server info)                          │ │
│  │  → tools/list                                         │ │
│  │  ← tools (3 tools)                                    │ │
│  └───────────────────────────────────────────────────────┘ │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## Công cụ Kiểm thử

### Liệt kê Các Công cụ Có sẵn

1. Nhấp vào tab **Tools**
2. Inspector tự động gọi `tools/list`
3. Bạn sẽ thấy tất cả các công cụ đã đăng ký với:
   - Tên công cụ
   - Mô tả
   - Lược đồ đầu vào (tham số)

### Gọi một Công cụ

1. Chọn một công cụ từ danh sách
2. Điền các tham số cần thiết trong biểu mẫu
3. Nhấp **Run Tool**
4. Xem phản hồi trong bảng kết quả

**Ví dụ: Kiểm thử công cụ máy tính**

```
Tool: add
Parameters:
  a: 25
  b: 17

Response:
{
  "content": [
    {
      "type": "text",
      "text": "42"
    }
  ]
}
```

### Gỡ lỗi Lỗi Công cụ

Khi một công cụ thất bại, Inspector hiển thị:

```
Error Response:
{
  "error": {
    "code": -32602,
    "message": "Invalid params: 'b' is required"
  }
}
```

Các mã lỗi phổ biến:
| Mã | Ý nghĩa |
|------|---------|
| -32700 | Lỗi phân tích (JSON không hợp lệ) |
| -32600 | Yêu cầu không hợp lệ |
| -32601 | Không tìm thấy phương thức |
| -32602 | Tham số không hợp lệ |
| -32603 | Lỗi nội bộ |

---

## Tài nguyên Kiểm thử

### Liệt kê Tài nguyên

1. Nhấp vào tab **Resources**
2. Inspector gọi `resources/list`
3. Bạn sẽ thấy:
   - URI tài nguyên
   - Tên và mô tả
   - Loại MIME

### Đọc một Tài nguyên

1. Chọn một tài nguyên
2. Nhấp **Read Resource**
3. Xem nội dung được trả về

**Ví dụ đầu ra:**

```
Resource: file:///config/settings.json
Content-Type: application/json

{
  "config": {
    "debug": true,
    "maxConnections": 10
  }
}
```

---

## Kiểm thử Các Prompt

### Liệt kê Các Prompt

1. Nhấp tab **Prompts**
2. Inspector gọi `prompts/list`
3. Xem các mẫu prompt có sẵn

### Lấy một Prompt

1. Chọn một prompt
2. Điền các đối số cần thiết
3. Nhấp **Get Prompt**
4. Xem các tin nhắn prompt đã được kết xuất

---

## Phân tích Nhật ký Tin nhắn

Nhật ký tin nhắn hiển thị tất cả các tin nhắn giao thức MCP. Bản ghi dưới đây là từ một
máy chủ `2025-11-25` kế thừa và bao gồm việc loại bỏ bắt tay `initialize`. Một
máy chủ `2026-07-28` sử dụng siêu dữ liệu yêu cầu tự chứa và `server/discover`
thay thế.

```
14:32:01 → {"jsonrpc":"2.0","id":1,"method":"initialize",...}
14:32:01 ← {"jsonrpc":"2.0","id":1,"result":{"protocolVersion":"2025-11-25",...}}
14:32:02 → {"jsonrpc":"2.0","id":2,"method":"tools/list"}
14:32:02 ← {"jsonrpc":"2.0","id":2,"result":{"tools":[...]}}
14:32:05 → {"jsonrpc":"2.0","id":3,"method":"tools/call","params":{"name":"add",...}}
14:32:05 ← {"jsonrpc":"2.0","id":3,"result":{"content":[...]}}
```

### Cần Quan tâm Điều gì

- **Cặp Yêu cầu/Phản hồi**: Mỗi `→` nên có một `←` tương ứng
- **Thông báo lỗi**: Tìm `"error"` trong phản hồi
- **Thời gian**: Khoảng cách lớn có thể chỉ ra vấn đề hiệu suất
- **Phiên bản giao thức**: Đảm bảo máy chủ và client đồng thuận phiên bản

---

## Tích hợp VS Code

Bạn có thể chạy Inspector trực tiếp từ VS Code:

### Sử dụng launch.json

Thêm vào `.vscode/launch.json`:

```json
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "Debug with MCP Inspector",
      "type": "node",
      "request": "launch",
      "runtimeExecutable": "npx",
      "runtimeArgs": [
        "@modelcontextprotocol/inspector",
        "python",
        "${workspaceFolder}/server.py"
      ],
      "console": "integratedTerminal"
    },
    {
      "name": "Debug SSE Server with Inspector",
      "type": "chrome",
      "request": "launch",
      "url": "http://localhost:5173",
      "preLaunchTask": "Start MCP Inspector"
    }
  ]
}
```

### Sử dụng Tasks

Thêm vào `.vscode/tasks.json`:

```json
{
  "version": "2.0.0",
  "tasks": [
    {
      "label": "Start MCP Inspector",
      "type": "shell",
      "command": "npx @modelcontextprotocol/inspector node ${workspaceFolder}/build/index.js",
      "isBackground": true,
      "problemMatcher": {
        "pattern": {
          "regexp": "^$"
        },
        "background": {
          "activeOnStart": true,
          "beginsPattern": "Inspector",
          "endsPattern": "listening"
        }
      }
    }
  ]
}
```

---

## Các Tình huống Gỡ lỗi Thường gặp

### Tình huống 1: Máy chủ Không Kết nối được

**Triệu chứng:** Inspector hiển thị "Disconnected" hoặc bị treo ở "Connecting..."

**Danh sách kiểm tra:**
1. ✅ Lệnh máy chủ có đúng không?
2. ✅ Tất cả phụ thuộc có được cài đặt không?
3. ✅ Đường dẫn máy chủ có phải tuyệt đối hoặc tương đối với thư mục hiện tại?
4. ✅ Biến môi trường cần thiết đã được thiết lập?

**Các bước gỡ lỗi:**
```bash
# Test server manually first
python -c "import your_server_module; print('OK')"

# Check for import errors
python -m your_server_module 2>&1 | head -20

# Verify MCP SDK is installed
pip show mcp
```

### Tình huống 2: Không Hiển thị Công cụ

**Triệu chứng:** Tab công cụ hiển thị danh sách trống

**Nguyên nhân có thể:**
1. Công cụ không được đăng ký trong quá trình khởi tạo máy chủ
2. Máy chủ bị lỗi sau khi khởi động
3. `tools/list` handler trả về mảng rỗng

**Các bước gỡ lỗi:**
1. Kiểm tra nhật ký tin nhắn cho phản hồi `tools/list`
2. Thêm ghi log vào mã đăng ký công cụ của bạn
3. Xác minh các decorators `@mcp.tool()` có mặt (Python)

### Tình huống 3: Công cụ Trả về Lỗi

**Triệu chứng:** Cuộc gọi công cụ trả về phản hồi lỗi

**Cách tiếp cận gỡ lỗi:**
1. Đọc kỹ thông báo lỗi
2. Kiểm tra loại tham số có khớp lược đồ không
3. Thêm try/catch với thông báo lỗi chi tiết
4. Kiểm tra nhật ký máy chủ cho dấu vết ngăn xếp

**Ví dụ xử lý lỗi cải tiến:**

```python
@mcp.tool()
async def my_tool(param1: str, param2: int) -> str:
    try:
        # Tool logic here
        result = process(param1, param2)
        return str(result)
    except ValueError as e:
        raise McpError(f"Invalid parameter: {e}")
    except Exception as e:
        raise McpError(f"Tool failed: {type(e).__name__}: {e}")
```

### Tình huống 4: Nội dung Tài nguyên Trống

**Triệu chứng:** Tài nguyên trả về nhưng nội dung trống hoặc null

**Danh sách kiểm tra:**
1. ✅ Đường dẫn tệp hoặc URI đúng
2. ✅ Máy chủ có quyền đọc tài nguyên
3. ✅ Nội dung tài nguyên được trả về chính xác

---

## Tính năng Nâng cao của Inspector

### Header tùy chỉnh (SSE)

```bash
npx @modelcontextprotocol/inspector \
  --sse http://localhost:8080/sse \
  --header "Authorization: Bearer your-token"
```

### Ghi log chi tiết

```bash
DEBUG=mcp* npx @modelcontextprotocol/inspector python server.py
```

### Ghi lại các Phiên làm việc

Inspector có thể xuất nhật ký tin nhắn để phân tích sau:
1. Nhấp **Export Log** trong bảng tin nhắn
2. Lưu tệp JSON
3. Chia sẻ với thành viên nhóm để gỡ lỗi

---

## Thực hành Tốt nhất

1. **Kiểm thử sớm và thường xuyên** - Dùng Inspector trong suốt quá trình phát triển, không chỉ khi gặp sự cố
2. **Bắt đầu đơn giản** - Kiểm thử kết nối cơ bản trước khi gọi các công cụ phức tạp
3. **Kiểm tra lược đồ** - Nhiều lỗi do không khớp loại tham số
4. **Đọc thông báo lỗi** - Lỗi MCP thường mô tả rõ ràng
5. **Giữ Inspector mở** - Giúp phát hiện lỗi khi bạn phát triển

---

## Tiếp theo Là Gì

Bạn đã hoàn thành Module 3: Bắt đầu! Tiếp tục học tập:

- [Module 4: Thực thi Thực tế](../../04-PracticalImplementation/README.md)

---

## Tài nguyên Bổ sung

- [Kho MCP Inspector trên GitHub](https://github.com/modelcontextprotocol/inspector)
- [Đặc tả MCP - Tin nhắn Giao thức](https://modelcontextprotocol.io/specification/2026-07-28/)
- [Đặc tả JSON-RPC 2.0](https://www.jsonrpc.org/specification)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Tuyên bố miễn trừ trách nhiệm**:
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng bản dịch tự động có thể chứa lỗi hoặc sai sót. Tài liệu gốc bằng ngôn ngữ gốc nên được coi là nguồn tin chính thức. Đối với thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm về bất kỳ hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->