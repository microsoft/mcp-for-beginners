# Máy Chủ Máy Tính MCP (Python)



Một triển khai máy chủ Giao thức Ngữ cảnh Mô hình (MCP) đơn giản bằng Python cung cấp chức năng máy tính cơ bản.


## Cài Đặt

Cài đặt các phụ thuộc cần thiết:

```bash
pip install -r requirements.txt
```

Hoặc cài đặt trực tiếp MCP Python SDK:

```bash
pip install "mcp>=2.1.1,<3.0.0"
```

## Cách Sử Dụng

### Chạy Máy Chủ

Máy chủ được thiết kế để sử dụng bởi các khách hàng MCP (như Claude Desktop). Để khởi động máy chủ:

```bash
python mcp_calculator_server.py
```

**Lưu ý**: Khi chạy trực tiếp trong terminal, bạn sẽ thấy các lỗi xác thực JSON-RPC. Đây là hành vi bình thường - máy chủ đang chờ các thông điệp khách hàng MCP được định dạng đúng.

### Kiểm Tra Các Hàm

Để kiểm tra các hàm máy tính hoạt động chính xác:

```bash
python test_calculator.py
```

## Khắc Phục Sự Cố

### Lỗi Import

Nếu bạn thấy `ModuleNotFoundError: No module named 'mcp'`, hãy cài đặt MCP Python SDK:

```bash
pip install "mcp>=2.1.1,<3.0.0"
```

### Lỗi JSON-RPC Khi Chạy Trực Tiếp

Các lỗi như "Invalid JSON: EOF while parsing a value" khi chạy máy chủ trực tiếp là điều được mong đợi. Máy chủ cần các thông điệp khách hàng MCP, không phải nhập trực tiếp từ terminal.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Tuyên bố miễn trừ trách nhiệm**:
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng bản dịch tự động có thể chứa lỗi hoặc sai sót. Tài liệu gốc bằng ngôn ngữ gốc nên được coi là nguồn tin chính thức. Đối với thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm về bất kỳ hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->