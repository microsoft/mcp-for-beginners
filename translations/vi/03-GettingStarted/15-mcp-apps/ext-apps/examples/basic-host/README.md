# Ví dụ: Máy chủ Cơ bản

Một triển khai tham khảo cho thấy cách xây dựng ứng dụng máy chủ MCP kết nối với các máy chủ MCP và hiển thị giao diện công cụ trong một vùng an toàn.

Máy chủ cơ bản này cũng có thể được sử dụng để kiểm thử Ứng dụng MCP trong quá trình phát triển cục bộ.

## Các Tệp Chính

- [`index.html`](../../../../../../../03-GettingStarted/15-mcp-apps/ext-apps/examples/basic-host/index.html) / [`src/index.tsx`](../../../../../../../03-GettingStarted/15-mcp-apps/ext-apps/examples/basic-host/src/index.tsx) - Máy chủ UI React với lựa chọn công cụ, nhập tham số, và quản lý iframe
- [`sandbox.html`](../../../../../../../03-GettingStarted/15-mcp-apps/ext-apps/examples/basic-host/sandbox.html) / [`src/sandbox.ts`](../../../../../../../03-GettingStarted/15-mcp-apps/ext-apps/examples/basic-host/src/sandbox.ts) - Proxy iframe ngoài với xác thực bảo mật và trung chuyển tin nhắn hai chiều
- [`src/implementation.ts`](../../../../../../../03-GettingStarted/15-mcp-apps/ext-apps/examples/basic-host/src/implementation.ts) - Logic cốt lõi: kết nối máy chủ, gọi công cụ, và thiết lập AppBridge

## Bắt đầu

```bash
npm install
npm run start
# Mở http://localhost:8080
```

Mặc định, ứng dụng máy chủ sẽ cố gắng kết nối đến một máy chủ MCP tại `http://localhost:3001/mcp`. Bạn có thể cấu hình hành vi này bằng cách đặt biến môi trường `SERVERS` với một mảng JSON các địa chỉ máy chủ:

```bash
SERVERS='["http://localhost:1234/mcp", "http://localhost:5678/mcp"]' npm run start
```

## Kiến trúc

Ví dụ này sử dụng mẫu vùng an toàn với hai iframe để cách ly UI an toàn:

```
Host (port 8080)
  └── Outer iframe (port 8081) - sandbox proxy
        └── Inner iframe (srcdoc) - untrusted tool UI
```

**Tại sao lại sử dụng hai iframe?**

- Iframe ngoài chạy trên nguồn gốc riêng biệt (cổng 8081) ngăn ngừa truy cập trực tiếp tới máy chủ
- Iframe trong nhận HTML qua `srcdoc` và bị giới hạn bằng các thuộc tính sandbox
- Các tin nhắn được truyền qua iframe ngoài, nơi xác thực và trung chuyển chúng hai chiều

Kiến trúc này đảm bảo rằng ngay cả khi mã giao diện công cụ độc hại, nó cũng không thể truy cập DOM, cookie, hay ngữ cảnh JavaScript của ứng dụng máy chủ.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Tuyên bố miễn trừ trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ bản địa của nó nên được coi là nguồn tin cậy chính thức. Đối với thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp do con người thực hiện. Chúng tôi không chịu trách nhiệm đối với bất kỳ sự hiểu nhầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->