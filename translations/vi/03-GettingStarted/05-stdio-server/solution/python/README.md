# MCP stdio Server - Giải pháp Python

> **⚠️ Quan trọng**: Giải pháp này đã được cập nhật để sử dụng **giao thức stdio** theo khuyến nghị của MCP Specification 2025-06-18. Giao thức SSE ban đầu đã bị ngừng sử dụng.

## Tổng quan

Giải pháp Python này minh họa cách xây dựng một máy chủ MCP sử dụng giao thức stdio hiện tại. Giao thức stdio đơn giản hơn, an toàn hơn và cung cấp hiệu suất tốt hơn so với phương pháp SSE đã bị ngừng sử dụng.

## Yêu cầu

- Python 3.8 hoặc mới hơn
- Khuyến nghị cài đặt `uv` để quản lý gói, xem [hướng dẫn](https://docs.astral.sh/uv/#highlights)

## Hướng dẫn thiết lập

### Bước 1: Tạo môi trường ảo

```bash
python -m venv venv
```

### Bước 2: Kích hoạt môi trường ảo

**Windows:**
```bash
venv\Scripts\activate
```

**macOS/Linux:**
```bash
source venv/bin/activate
```

### Bước 3: Cài đặt các phụ thuộc

```bash
pip install mcp
```

## Chạy máy chủ

Máy chủ stdio hoạt động khác so với máy chủ SSE cũ. Thay vì khởi động một máy chủ web, nó giao tiếp thông qua stdin/stdout:

```bash
python server.py
```

**Quan trọng**: Máy chủ sẽ có vẻ như bị treo - điều này là bình thường! Nó đang chờ các thông điệp JSON-RPC từ stdin.

## Kiểm tra máy chủ

### Phương pháp 1: Sử dụng MCP Inspector (Khuyến nghị)

```bash
npx @modelcontextprotocol/inspector python server.py
```

Điều này sẽ:
1. Khởi chạy máy chủ của bạn dưới dạng một subprocess
2. Mở giao diện web để kiểm tra
3. Cho phép bạn kiểm tra tất cả các công cụ của máy chủ một cách tương tác

### Phương pháp 2: Kiểm tra trực tiếp JSON-RPC

Bạn cũng có thể kiểm tra bằng cách gửi các thông điệp JSON-RPC trực tiếp:

1. Khởi động máy chủ: `python server.py`
2. Gửi một thông điệp JSON-RPC (ví dụ):

```json
{"jsonrpc": "2.0", "id": 1, "method": "tools/list"}
```

3. Máy chủ sẽ phản hồi với các công cụ có sẵn

### Các công cụ có sẵn

Máy chủ cung cấp các công cụ sau:

- **add(a, b)**: Cộng hai số
- **multiply(a, b)**: Nhân hai số  
- **get_greeting(name)**: Tạo lời chào cá nhân hóa
- **get_server_info()**: Lấy thông tin về máy chủ

### Kiểm tra với Claude Desktop

Để sử dụng máy chủ này với Claude Desktop, thêm cấu hình sau vào `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "example-stdio-server": {
      "command": "python",
      "args": ["path/to/server.py"]
    }
  }
}
```

## Sự khác biệt chính so với SSE

**Giao thức stdio (Hiện tại):**
- ✅ Thiết lập đơn giản hơn - không cần máy chủ web
- ✅ Bảo mật tốt hơn - không có điểm cuối HTTP
- ✅ Giao tiếp dựa trên subprocess
- ✅ JSON-RPC qua stdin/stdout
- ✅ Hiệu suất tốt hơn

**Giao thức SSE (Đã ngừng sử dụng):**
- ❌ Yêu cầu thiết lập máy chủ HTTP
- ❌ Cần framework web (Starlette/FastAPI)
- ❌ Quản lý định tuyến và phiên phức tạp hơn
- ❌ Các vấn đề bảo mật bổ sung
- ❌ Đã ngừng sử dụng trong MCP 2025-06-18

## Mẹo gỡ lỗi

- Sử dụng `stderr` để ghi log (không bao giờ dùng `stdout`)
- Kiểm tra với Inspector để gỡ lỗi trực quan
- Đảm bảo tất cả các thông điệp JSON được phân cách bằng dòng mới
- Kiểm tra rằng máy chủ khởi động mà không có lỗi

Giải pháp này tuân theo đặc tả MCP hiện tại và minh họa các thực hành tốt nhất cho việc triển khai giao thức stdio.

---

**Tuyên bố miễn trừ trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ bản địa nên được coi là nguồn thông tin chính thức. Đối với các thông tin quan trọng, khuyến nghị sử dụng dịch vụ dịch thuật chuyên nghiệp từ con người. Chúng tôi không chịu trách nhiệm cho bất kỳ sự hiểu lầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.