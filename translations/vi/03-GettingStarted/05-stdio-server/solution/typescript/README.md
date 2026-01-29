# MCP stdio Server - Giải pháp TypeScript

> **⚠️ Quan trọng**: Giải pháp này đã được cập nhật để sử dụng **giao thức stdio** theo khuyến nghị của MCP Specification 2025-06-18. Giao thức SSE cũ đã bị ngừng sử dụng.

## Tổng quan

Giải pháp TypeScript này minh họa cách xây dựng một máy chủ MCP sử dụng giao thức stdio hiện tại. Giao thức stdio đơn giản hơn, an toàn hơn và mang lại hiệu suất tốt hơn so với phương pháp SSE đã bị ngừng sử dụng.

## Yêu cầu trước

- Node.js 18+ hoặc phiên bản mới hơn
- Trình quản lý gói npm hoặc yarn

## Hướng dẫn thiết lập

### Bước 1: Cài đặt các phụ thuộc

```bash
npm install
```

### Bước 2: Xây dựng dự án

```bash
npm run build
```

## Chạy máy chủ

Máy chủ stdio hoạt động khác so với máy chủ SSE cũ. Thay vì khởi động một máy chủ web, nó giao tiếp thông qua stdin/stdout:

```bash
npm start
```

**Quan trọng**: Máy chủ sẽ có vẻ như bị treo - điều này là bình thường! Nó đang chờ các thông điệp JSON-RPC từ stdin.

## Kiểm tra máy chủ

### Phương pháp 1: Sử dụng MCP Inspector (Khuyến nghị)

```bash
npm run inspector
```

Điều này sẽ:
1. Khởi chạy máy chủ của bạn dưới dạng một tiến trình con
2. Mở giao diện web để kiểm tra
3. Cho phép bạn kiểm tra tất cả các công cụ của máy chủ một cách tương tác

### Phương pháp 2: Kiểm tra trực tiếp qua dòng lệnh

Bạn cũng có thể kiểm tra bằng cách khởi chạy Inspector trực tiếp:

```bash
npx @modelcontextprotocol/inspector node build/index.js
```

### Các công cụ có sẵn

Máy chủ cung cấp các công cụ sau:

- **add(a, b)**: Cộng hai số
- **multiply(a, b)**: Nhân hai số  
- **get_greeting(name)**: Tạo lời chào cá nhân hóa
- **get_server_info()**: Lấy thông tin về máy chủ

### Kiểm tra với Claude Desktop

Để sử dụng máy chủ này với Claude Desktop, thêm cấu hình sau vào tệp `claude_desktop_config.json` của bạn:

```json
{
  "mcpServers": {
    "example-stdio-server": {
      "command": "node",
      "args": ["path/to/build/index.js"]
    }
  }
}
```

## Cấu trúc dự án

```
typescript/
├── src/
│   └── index.ts          # Main server implementation
├── build/                # Compiled JavaScript (generated)
├── package.json          # Project configuration
├── tsconfig.json         # TypeScript configuration
└── README.md            # This file
```

## Những điểm khác biệt chính so với SSE

**Giao thức stdio (Hiện tại):**
- ✅ Thiết lập đơn giản hơn - không cần máy chủ HTTP
- ✅ An toàn hơn - không có endpoint HTTP
- ✅ Giao tiếp dựa trên tiến trình con
- ✅ JSON-RPC qua stdin/stdout
- ✅ Hiệu suất tốt hơn

**Giao thức SSE (Đã ngừng sử dụng):**
- ❌ Yêu cầu thiết lập máy chủ Express
- ❌ Cần định tuyến và quản lý phiên phức tạp
- ❌ Nhiều phụ thuộc hơn (Express, xử lý HTTP)
- ❌ Cần xem xét thêm về bảo mật
- ❌ Hiện đã bị ngừng sử dụng trong MCP 2025-06-18

## Mẹo phát triển

- Sử dụng `console.error()` để ghi nhật ký (không bao giờ sử dụng `console.log()` vì nó ghi vào stdout)
- Xây dựng với `npm run build` trước khi kiểm tra
- Kiểm tra với Inspector để gỡ lỗi trực quan
- Đảm bảo tất cả các thông điệp JSON được định dạng đúng
- Máy chủ tự động xử lý việc tắt máy an toàn khi nhận SIGINT/SIGTERM

Giải pháp này tuân theo đặc tả MCP hiện tại và minh họa các phương pháp tốt nhất để triển khai giao thức stdio bằng TypeScript.

---

**Tuyên bố miễn trừ trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ bản địa nên được coi là nguồn thông tin chính thức. Đối với các thông tin quan trọng, khuyến nghị sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm cho bất kỳ sự hiểu lầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.