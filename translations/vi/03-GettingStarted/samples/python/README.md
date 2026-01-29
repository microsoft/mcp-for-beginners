# Máy chủ MCP Calculator (Python)

Một triển khai máy chủ Model Context Protocol (MCP) đơn giản bằng Python cung cấp chức năng máy tính cơ bản.

## Cài đặt

Cài đặt các thư viện cần thiết:

```bash
pip install -r requirements.txt
```

Hoặc cài đặt trực tiếp MCP Python SDK:

```bash
pip install mcp>=1.18.0
```

## Sử dụng

### Chạy máy chủ

Máy chủ được thiết kế để sử dụng bởi các client MCP (như Claude Desktop). Để khởi động máy chủ:

```bash
python mcp_calculator_server.py
```

**Lưu ý**: Khi chạy trực tiếp trong terminal, bạn sẽ thấy các lỗi xác thực JSON-RPC. Đây là hành vi bình thường - máy chủ đang chờ các tin nhắn từ client MCP được định dạng đúng.

### Kiểm tra các chức năng

Để kiểm tra xem các chức năng của máy tính có hoạt động đúng không:

```bash
python test_calculator.py
```

## Xử lý sự cố

### Lỗi nhập khẩu

Nếu bạn thấy `ModuleNotFoundError: No module named 'mcp'`, hãy cài đặt MCP Python SDK:

```bash
pip install mcp>=1.18.0
```

### Lỗi JSON-RPC khi chạy trực tiếp

Các lỗi như "Invalid JSON: EOF while parsing a value" khi chạy máy chủ trực tiếp là điều bình thường. Máy chủ cần các tin nhắn từ client MCP, không phải đầu vào trực tiếp từ terminal.

---

**Tuyên bố miễn trừ trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ bản địa nên được coi là nguồn thông tin chính thức. Đối với thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp của con người. Chúng tôi không chịu trách nhiệm về bất kỳ sự hiểu lầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.