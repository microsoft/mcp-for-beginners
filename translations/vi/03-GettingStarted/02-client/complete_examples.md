# Các Ví Dụ MCP Client Hoàn Chỉnh

Thư mục này chứa các ví dụ hoàn chỉnh và hoạt động của MCP client trong các ngôn ngữ lập trình khác nhau. Mỗi client minh họa đầy đủ các chức năng được mô tả trong hướng dẫn README.md chính.

## Các Client Có Sẵn

### 1. Java Client (`client_example_java.java`)

- **Giao thức truyền tải**: SSE (Server-Sent Events) qua HTTP
- **Máy chủ mục tiêu**: `http://localhost:8080`
- **Tính năng**:
  - Thiết lập kết nối và ping
  - Liệt kê công cụ
  - Các phép toán máy tính (cộng, trừ, nhân, chia, trợ giúp)
  - Xử lý lỗi và trích xuất kết quả

**Cách chạy:**

```bash
# Ensure your MCP server is running on localhost:8080
javac client_example_java.java
java client_example_java
```

### 2. C# Client (`client_example_csharp.cs`)

- **Giao thức truyền tải**: Stdio (Đầu vào/Đầu ra chuẩn)
- **Máy chủ mục tiêu**: Máy chủ MCP .NET cục bộ qua dotnet run
- **Tính năng**:
  - Tự động khởi động máy chủ qua giao thức stdio
  - Liệt kê công cụ và tài nguyên
  - Các phép toán máy tính
  - Phân tích kết quả JSON
  - Xử lý lỗi toàn diện

**Cách chạy:**

```bash
dotnet run
```

### 3. TypeScript Client (`client_example_typescript.ts`)

- **Giao thức truyền tải**: Stdio (Đầu vào/Đầu ra chuẩn)
- **Máy chủ mục tiêu**: Máy chủ MCP Node.js cục bộ
- **Tính năng**:
  - Hỗ trợ đầy đủ giao thức MCP
  - Các thao tác công cụ, tài nguyên và prompt
  - Các phép toán máy tính
  - Đọc tài nguyên và thực thi prompt
  - Xử lý lỗi mạnh mẽ

**Cách chạy:**

```bash
# First compile TypeScript (if needed)
npm run build

# Then run the client
npm run client
# or
node client_example_typescript.js
```

### 4. Python Client (`client_example_python.py`)

- **Giao thức truyền tải**: Stdio (Đầu vào/Đầu ra chuẩn)  
- **Máy chủ mục tiêu**: Máy chủ MCP Python cục bộ
- **Tính năng**:
  - Mô hình async/await cho các thao tác
  - Khám phá công cụ và tài nguyên
  - Kiểm tra các phép toán máy tính
  - Đọc nội dung tài nguyên
  - Tổ chức theo lớp

**Cách chạy:**

```bash
python client_example_python.py
```

## Các Tính Năng Chung Giữa Các Client

Mỗi triển khai client minh họa:

1. **Quản lý kết nối**
   - Thiết lập kết nối với máy chủ MCP
   - Xử lý lỗi kết nối
   - Dọn dẹp và quản lý tài nguyên đúng cách

2. **Khám phá máy chủ**
   - Liệt kê các công cụ có sẵn
   - Liệt kê các tài nguyên có sẵn (nếu được hỗ trợ)
   - Liệt kê các prompt có sẵn (nếu được hỗ trợ)

3. **Thực thi công cụ**
   - Các phép toán máy tính cơ bản (cộng, trừ, nhân, chia)
   - Lệnh trợ giúp để lấy thông tin máy chủ
   - Truyền tham số đúng cách và xử lý kết quả

4. **Xử lý lỗi**
   - Lỗi kết nối
   - Lỗi thực thi công cụ
   - Xử lý thất bại một cách nhẹ nhàng và phản hồi cho người dùng

5. **Xử lý kết quả**
   - Trích xuất nội dung văn bản từ phản hồi
   - Định dạng đầu ra để dễ đọc
   - Xử lý các định dạng phản hồi khác nhau

## Yêu Cầu Trước Khi Chạy

Trước khi chạy các client này, hãy đảm bảo bạn đã:

1. **Máy chủ MCP tương ứng đang chạy** (từ `../01-first-server/`)
2. **Cài đặt các phụ thuộc cần thiết** cho ngôn ngữ bạn chọn
3. **Kết nối mạng đúng cách** (đối với các giao thức truyền tải qua HTTP)

## Sự Khác Biệt Chính Giữa Các Triển Khai

| Ngôn ngữ   | Giao thức truyền tải | Khởi động máy chủ | Mô hình Async | Thư viện chính       |
|------------|----------------------|-------------------|---------------|---------------------|
| Java       | SSE/HTTP            | Bên ngoài         | Đồng bộ       | WebFlux, MCP SDK    |
| C#         | Stdio               | Tự động           | Async/Await   | .NET MCP SDK        |
| TypeScript | Stdio               | Tự động           | Async/Await   | Node MCP SDK        |
| Python     | Stdio               | Tự động           | AsyncIO       | Python MCP SDK      |
| Rust       | Stdio               | Tự động           | Async/Await   | Rust MCP SDK, Tokio |

## Các Bước Tiếp Theo

Sau khi khám phá các ví dụ client này:

1. **Chỉnh sửa các client** để thêm tính năng hoặc thao tác mới
2. **Tạo máy chủ của riêng bạn** và kiểm tra với các client này
3. **Thử nghiệm với các giao thức truyền tải khác nhau** (SSE so với Stdio)
4. **Xây dựng ứng dụng phức tạp hơn** tích hợp chức năng MCP

## Xử Lý Sự Cố

### Các Vấn Đề Thường Gặp

1. **Kết nối bị từ chối**: Đảm bảo máy chủ MCP đang chạy trên cổng/đường dẫn mong đợi
2. **Không tìm thấy module**: Cài đặt MCP SDK cần thiết cho ngôn ngữ của bạn
3. **Quyền bị từ chối**: Kiểm tra quyền tệp cho giao thức stdio
4. **Không tìm thấy công cụ**: Xác minh máy chủ triển khai các công cụ mong đợi

### Mẹo Gỡ Lỗi

1. **Bật ghi nhật ký chi tiết** trong MCP SDK của bạn
2. **Kiểm tra nhật ký máy chủ** để tìm thông báo lỗi
3. **Xác minh tên và chữ ký công cụ** khớp giữa client và máy chủ
4. **Kiểm tra với MCP Inspector** trước để xác thực chức năng máy chủ

## Tài Liệu Liên Quan

- [Hướng Dẫn Client Chính](./README.md)
- [Ví Dụ Máy Chủ MCP](../../../../03-GettingStarted/01-first-server)
- [MCP với Tích Hợp LLM](../../../../03-GettingStarted/03-llm-client)
- [Tài Liệu MCP Chính Thức](https://modelcontextprotocol.io/)

**Tuyên bố miễn trừ trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ bản địa nên được coi là nguồn tham khảo chính thức. Đối với các thông tin quan trọng, chúng tôi khuyến nghị sử dụng dịch vụ dịch thuật chuyên nghiệp từ con người. Chúng tôi không chịu trách nhiệm cho bất kỳ sự hiểu lầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.