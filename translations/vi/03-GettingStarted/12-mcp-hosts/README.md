# Cài Đặt Các Khách Chủ MCP Phổ Biến

> [!NOTE]
> Các cấu hình host trỏ đến `/sse` là ví dụ cũ về HTTP+SSE cho
> MCP `2025-11-25`. Đối với MCP `2026-07-28`, chọn Streamable HTTP trong các host
> hỗ trợ và sử dụng điểm cuối được cấu hình bởi máy chủ.

Hướng dẫn này bao gồm cách cấu hình và sử dụng các máy chủ MCP với các ứng dụng host AI phổ biến. Mỗi host có cách tiếp cận cấu hình riêng, nhưng khi đã được thiết lập, tất cả chúng đều giao tiếp với máy chủ MCP bằng giao thức tiêu chuẩn.

## Host MCP là gì?

Một **Host MCP** là một ứng dụng AI có thể kết nối với các máy chủ MCP để mở rộng khả năng của nó. Bạn có thể nghĩ nó như "giao diện người dùng" mà người dùng tương tác, trong khi các máy chủ MCP cung cấp công cụ và dữ liệu ở phía "hậu trường".

```mermaid
flowchart LR
    User[👤 Người dùng] --> Host[🖥️ Máy chủ MCP]
    Host --> S1[Máy chủ MCP A]
    Host --> S2[Máy chủ MCP B]
    Host --> S3[Máy chủ MCP C]
    
    subgraph "Máy chủ Phổ biến"
        H1[Claude Desktop]
        H2[VS Code]
        H3[Cursor]
        H4[Cline]
        H5[Windsurf]
    end
```

## Yêu Cầu Trước Khi Bắt Đầu

- Một máy chủ MCP để kết nối (xem [Module 3.1 - Máy chủ đầu tiên](../01-first-server/README.md))
- Ứng dụng host được cài đặt trên hệ thống của bạn
- Hiểu biết cơ bản về các tập tin cấu hình JSON

---

## 1. Claude Desktop

**Claude Desktop** là ứng dụng desktop chính thức của Anthropic hỗ trợ MCP một cách bản địa.

### Cài Đặt

1. Tải Claude Desktop từ [claude.ai/download](https://claude.ai/download)
2. Cài đặt và đăng nhập bằng tài khoản Anthropic của bạn

### Cấu Hình

Claude Desktop sử dụng tập tin cấu hình JSON để định nghĩa các máy chủ MCP.

**Vị trí tập tin cấu hình:**
- **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
- **Windows**: `%APPDATA%\Claude\claude_desktop_config.json`
- **Linux**: `~/.config/Claude/claude_desktop_config.json`

**Ví dụ cấu hình:**

```json
{
  "mcpServers": {
    "calculator": {
      "command": "python",
      "args": ["-m", "mcp_calculator_server"],
      "env": {
        "PYTHONPATH": "/path/to/your/server"
      }
    },
    "weather": {
      "command": "node",
      "args": ["/path/to/weather-server/build/index.js"]
    },
    "database": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-postgres"],
      "env": {
        "DATABASE_URL": "postgresql://user:pass@localhost/mydb"
      }
    }
  }
}
```

### Các Tùy Chọn Cấu Hình

| Trường | Mô tả | Ví dụ |
|-------|-------------|---------|
| `command` | Thực thi để chạy | `"python"`, `"node"`, `"npx"` |
| `args` | Tham số dòng lệnh | `["-m", "my_server"]` |
| `env` | Biến môi trường | `{"API_KEY": "xxx"}` |
| `cwd` | Thư mục làm việc | `"/path/to/server"` |

### Kiểm Tra Cấu Hình

1. Lưu tập tin cấu hình
2. Khởi động lại hoàn toàn Claude Desktop (thoát và mở lại)
3. Mở cuộc trò chuyện mới
4. Tìm biểu tượng 🔌 báo hiệu các máy chủ đã kết nối
5. Thử yêu cầu Claude sử dụng một trong các công cụ của bạn

### Khắc Phục Sự Cố Claude Desktop

**Máy chủ không hiển thị:**
- Kiểm tra cú pháp tập tin cấu hình với trình xác thực JSON
- Đảm bảo đường dẫn command chính xác
- Kiểm tra nhật ký Claude Desktop: Trợ giúp → Hiển thị Nhật ký

**Máy chủ bị crash khi khởi động:**
- Thử chạy máy chủ thủ công trong terminal trước
- Kiểm tra biến môi trường đã cài đặt đúng chưa
- Đảm bảo tất cả phụ thuộc đã được cài đặt

---

## 2. VS Code với GitHub Copilot

VS Code hỗ trợ MCP thông qua các tiện ích mở rộng GitHub Copilot Chat.

### Yêu Cầu Trước Khi Bắt Đầu

1. VS Code phiên bản 1.99+ được cài đặt
2. Tiện ích mở rộng GitHub Copilot được cài đặt
3. Tiện ích mở rộng GitHub Copilot Chat được cài đặt

### Cấu Hình

VS Code sử dụng `.vscode/mcp.json` trong workspace hoặc cài đặt người dùng.

**Cấu hình workspace** (`.vscode/mcp.json`):

```json
{
  "servers": {
    "my-calculator": {
      "type": "stdio",
      "command": "python",
      "args": ["-m", "mcp_calculator_server"]
    },
    "my-database": {
      "type": "sse",
      "url": "http://localhost:8080/sse"
    }
  }
}
```

**Cài đặt người dùng** (`settings.json`):

```json
{
  "mcp.servers": {
    "global-server": {
      "type": "stdio",
      "command": "npx",
      "args": ["-y", "@anthropic/mcp-server-memory"]
    }
  },
  "mcp.enableLogging": true
}
```

### Sử Dụng MCP trong VS Code

1. Mở bảng Copilot Chat (Ctrl+Shift+I / Cmd+Shift+I)
2. Gõ `@` để xem các công cụ MCP có sẵn
3. Sử dụng ngôn ngữ tự nhiên để gọi công cụ: "Calculate 25 * 48 using the calculator"

### Khắc Phục Sự Cố VS Code

**Máy chủ MCP không tải:**
- Kiểm tra bảng Output → "MCP" để xem nhật ký lỗi
- Tải lại cửa sổ: Ctrl+Shift+P → "Developer: Reload Window"
- Xác nhận máy chủ chạy độc lập trước

---

## 3. Cursor

**Cursor** là trình soạn thảo code tiên tiến tập trung AI với hỗ trợ MCP tích hợp.

### Cài Đặt

1. Tải Cursor từ [cursor.sh](https://cursor.sh)
2. Cài đặt và đăng nhập

### Cấu Hình

Cursor sử dụng định dạng cấu hình tương tự Claude Desktop.

**Vị trí tập tin cấu hình:**
- **macOS**: `~/.cursor/mcp.json`
- **Windows**: `%USERPROFILE%\.cursor\mcp.json`
- **Linux**: `~/.cursor/mcp.json`

**Ví dụ cấu hình:**

```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "/path/to/allowed/directory"]
    },
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_TOKEN": "ghp_your_token_here"
      }
    }
  }
}
```

### Sử Dụng MCP trong Cursor

1. Mở chat AI của Cursor (Ctrl+L / Cmd+L)
2. Công cụ MCP xuất hiện tự động trong gợi ý
3. Yêu cầu AI thực hiện công việc sử dụng các máy chủ đã kết nối

---

## 4. Cline (Dựa trên Terminal)

**Cline** là khách MCP dựa trên terminal, phù hợp cho quy trình làm việc dòng lệnh.

### Cài Đặt

```bash
npm install -g @anthropic/cline
```

### Cấu Hình

Cline sử dụng biến môi trường và tham số dòng lệnh.

**Sử dụng biến môi trường:**

```bash
export ANTHROPIC_API_KEY="your-api-key"
export MCP_SERVER_CALCULATOR="python -m mcp_calculator_server"
```

**Sử dụng tham số dòng lệnh:**

```bash
cline --mcp-server "calculator:python -m mcp_calculator_server" \
      --mcp-server "weather:node /path/to/weather/index.js"
```

**Tập tin cấu hình** (`~/.clinerc`):

```json
{
  "apiKey": "your-api-key",
  "mcpServers": {
    "calculator": {
      "command": "python",
      "args": ["-m", "mcp_calculator_server"]
    }
  }
}
```

### Sử Dụng Cline

```bash
# Bắt đầu phiên tương tác
cline

# Truy vấn đơn với MCP
cline "Calculate the square root of 144 using the calculator"

# Liệt kê các công cụ có sẵn
cline --list-tools
```

---

## 5. Windsurf

**Windsurf** là một trình soạn thảo code lấy AI làm trung tâm khác có hỗ trợ MCP.

### Cài Đặt

1. Tải Windsurf từ [codeium.com/windsurf](https://codeium.com/windsurf)
2. Cài đặt và tạo tài khoản

### Cấu Hình

Cấu hình Windsurf được quản lý qua giao diện cài đặt:

1. Mở Cài Đặt (Ctrl+, / Cmd+,)
2. Tìm "MCP"
3. Nhấn "Chỉnh sửa trong settings.json"

**Ví dụ cấu hình:**

```json
{
  "windsurf.mcp.servers": {
    "my-tools": {
      "command": "python",
      "args": ["/path/to/server.py"],
      "env": {}
    }
  },
  "windsurf.mcp.enabled": true
}
```

---

## So Sánh Các Loại Giao Thức

Các host khác nhau hỗ trợ các cơ chế truyền tải khác nhau:

| Host | stdio | SSE/HTTP | WebSocket |
|------|-------|----------|-----------|
| Claude Desktop | ✅ | ❌ | ❌ |
| VS Code | ✅ | ✅ | ❌ |
| Cursor | ✅ | ✅ | ❌ |
| Cline | ✅ | ✅ | ❌ |
| Windsurf | ✅ | ✅ | ❌ |

**stdio** (đầu vào/ra chuẩn): Tốt nhất cho các máy chủ cục bộ do host khởi tạo
**SSE/HTTP**: Tốt nhất cho máy chủ từ xa hoặc máy chủ chia sẻ giữa nhiều khách

---

## Sự Cố Thông Thường

### Máy chủ không khởi động được

1. **Kiểm tra máy chủ thủ công trước:**
   ```bash
   # Dành cho Python
   python -m your_server_module
   
   # Dành cho Node.js
   node /path/to/server/index.js
   ```

2. **Kiểm tra đường dẫn command:**
   - Sử dụng đường dẫn tuyệt đối khi có thể
   - Đảm bảo thực thi có trong PATH của bạn

3. **Xác minh các phụ thuộc:**
   ```bash
   # Python
   pip list | grep mcp
   
   # Node.js
   npm list @modelcontextprotocol/sdk
   ```

### Máy chủ kết nối nhưng công cụ không hoạt động

1. **Kiểm tra nhật ký máy chủ** - Hầu hết host đều có tùy chọn ghi nhật ký
2. **Xác nhận đăng ký công cụ** - Sử dụng MCP Inspector để kiểm tra
3. **Kiểm tra quyền** - Một số công cụ cần truy cập file/mạng

### Biến môi trường không được truyền

- Một số host làm sạch biến môi trường
- Sử dụng trường `env` trong cấu hình rõ ràng
- Tránh lưu dữ liệu nhạy cảm trong tập tin cấu hình (dùng quản lý bí mật)

---

## Các Thực Hành An Ninh Tốt Nhất

1. **Không bao giờ commit khóa API** vào tập tin cấu hình
2. **Sử dụng biến môi trường** cho dữ liệu nhạy cảm
3. **Giới hạn quyền của máy chủ** chỉ ở mức cần thiết
4. **Xem lại mã máy chủ** trước khi cấp quyền truy cập hệ thống
5. **Sử dụng danh sách cho phép** cho truy cập hệ thống file và mạng

---

## Tiếp Theo Là Gì

- [3.13 - Gỡ lỗi với MCP Inspector](../13-mcp-inspector/README.md)
- [3.1 - Tạo máy chủ MCP đầu tiên của bạn](../01-first-server/README.md)
- [Module 5 - Chủ đề Nâng cao](../../05-AdvancedTopics/README.md)

---

## Tài Nguyên Bổ Sung

- [Tài liệu MCP Claude Desktop](https://docs.anthropic.com/en/docs/claude-desktop/mcp)
- [Tiện ích mở rộng MCP VS Code](https://marketplace.visualstudio.com/items?itemName=anthropic.claude-mcp)
- [Đặc tả MCP - Các phương thức truyền tải](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/)
- [Danh mục Máy chủ MCP chính thức](https://github.com/modelcontextprotocol/servers)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Tuyên bố miễn trừ trách nhiệm**:
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng bản dịch tự động có thể chứa lỗi hoặc sai sót. Tài liệu gốc bằng ngôn ngữ gốc nên được coi là nguồn tin chính thức. Đối với thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm về bất kỳ hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->