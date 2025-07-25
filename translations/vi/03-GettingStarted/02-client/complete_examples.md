<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "affcf199a44f60283a289dcb69dc144e",
  "translation_date": "2025-07-17T09:12:19+00:00",
  "source_file": "03-GettingStarted/02-client/complete_examples.md",
  "language_code": "vi"
}
-->
# Ví dụ đầy đủ về MCP Client

Thư mục này chứa các ví dụ hoàn chỉnh và hoạt động của các MCP client trong các ngôn ngữ lập trình khác nhau. Mỗi client đều minh họa đầy đủ các chức năng được mô tả trong hướng dẫn chính README.md.

## Các Client có sẵn

### 1. Java Client (`client_example_java.java`)
- **Giao thức**: SSE (Server-Sent Events) qua HTTP
- **Máy chủ mục tiêu**: `http://localhost:8080`
- **Tính năng**: 
  - Thiết lập kết nối và gửi ping
  - Liệt kê công cụ
  - Các phép tính toán (cộng, trừ, nhân, chia, trợ giúp)
  - Xử lý lỗi và trích xuất kết quả

**Để chạy:**
```bash
# Ensure your MCP server is running on localhost:8080
javac client_example_java.java
java client_example_java
```

### 2. C# Client (`client_example_csharp.cs`)
- **Giao thức**: Stdio (Đầu vào/đầu ra chuẩn)
- **Máy chủ mục tiêu**: Máy chủ MCP .NET cục bộ qua dotnet run
- **Tính năng**:
  - Tự động khởi động máy chủ qua giao thức stdio
  - Liệt kê công cụ và tài nguyên
  - Các phép tính toán
  - Phân tích kết quả JSON
  - Xử lý lỗi toàn diện

**Để chạy:**
```bash
dotnet run
```

### 3. TypeScript Client (`client_example_typescript.ts`)
- **Giao thức**: Stdio (Đầu vào/đầu ra chuẩn)
- **Máy chủ mục tiêu**: Máy chủ MCP Node.js cục bộ
- **Tính năng**:
  - Hỗ trợ đầy đủ giao thức MCP
  - Các thao tác với công cụ, tài nguyên và prompt
  - Các phép tính toán
  - Đọc tài nguyên và thực thi prompt
  - Xử lý lỗi mạnh mẽ

**Để chạy:**
```bash
# First compile TypeScript (if needed)
npm run build

# Then run the client
npm run client
# or
node client_example_typescript.js
```

### 4. Python Client (`client_example_python.py`)
- **Giao thức**: Stdio (Đầu vào/đầu ra chuẩn)  
- **Máy chủ mục tiêu**: Máy chủ MCP Python cục bộ
- **Tính năng**:
  - Mẫu async/await cho các thao tác
  - Khám phá công cụ và tài nguyên
  - Kiểm thử các phép tính toán
  - Đọc nội dung tài nguyên
  - Tổ chức theo lớp

**Để chạy:**
```bash
python client_example_python.py
```

## Các tính năng chung ở tất cả các client

Mỗi triển khai client đều thể hiện:

1. **Quản lý kết nối**
   - Thiết lập kết nối tới máy chủ MCP
   - Xử lý lỗi kết nối
   - Dọn dẹp và quản lý tài nguyên đúng cách

2. **Khám phá máy chủ**
   - Liệt kê các công cụ có sẵn
   - Liệt kê các tài nguyên có sẵn (nếu được hỗ trợ)
   - Liệt kê các prompt có sẵn (nếu được hỗ trợ)

3. **Gọi công cụ**
   - Các phép tính toán cơ bản (cộng, trừ, nhân, chia)
   - Lệnh trợ giúp để lấy thông tin máy chủ
   - Truyền đối số và xử lý kết quả đúng cách

4. **Xử lý lỗi**
   - Lỗi kết nối
   - Lỗi khi thực thi công cụ
   - Thất bại nhẹ nhàng và phản hồi cho người dùng

5. **Xử lý kết quả**
   - Trích xuất nội dung văn bản từ phản hồi
   - Định dạng đầu ra để dễ đọc
   - Xử lý các định dạng phản hồi khác nhau

## Yêu cầu trước khi chạy

Trước khi chạy các client này, hãy đảm bảo bạn đã:

1. **Máy chủ MCP tương ứng đang chạy** (từ `../01-first-server/`)
2. **Cài đặt các phụ thuộc cần thiết** cho ngôn ngữ bạn chọn
3. **Kết nối mạng phù hợp** (cho các giao thức dựa trên HTTP)

## Sự khác biệt chính giữa các triển khai

| Ngôn ngữ   | Giao thức | Khởi động máy chủ | Mô hình Async | Thư viện chính |
|------------|-----------|-------------------|---------------|----------------|
| Java       | SSE/HTTP  | Bên ngoài         | Đồng bộ       | WebFlux, MCP SDK |
| C#         | Stdio     | Tự động           | Async/Await   | .NET MCP SDK   |
| TypeScript | Stdio     | Tự động           | Async/Await   | Node MCP SDK   |
| Python     | Stdio     | Tự động           | AsyncIO       | Python MCP SDK |

## Bước tiếp theo

Sau khi khám phá các ví dụ client này:

1. **Chỉnh sửa client** để thêm tính năng hoặc thao tác mới
2. **Tạo máy chủ riêng của bạn** và thử nghiệm với các client này
3. **Thử nghiệm với các giao thức khác nhau** (SSE so với Stdio)
4. **Xây dựng ứng dụng phức tạp hơn** tích hợp chức năng MCP

## Khắc phục sự cố

### Các vấn đề phổ biến

1. **Kết nối bị từ chối**: Đảm bảo máy chủ MCP đang chạy trên cổng/đường dẫn mong đợi
2. **Không tìm thấy module**: Cài đặt MCP SDK cần thiết cho ngôn ngữ của bạn
3. **Từ chối quyền truy cập**: Kiểm tra quyền truy cập file cho giao thức stdio
4. **Không tìm thấy công cụ**: Xác nhận máy chủ đã triển khai các công cụ mong đợi

### Mẹo gỡ lỗi

1. **Bật ghi log chi tiết** trong MCP SDK của bạn
2. **Kiểm tra log máy chủ** để tìm thông báo lỗi
3. **Xác minh tên và chữ ký công cụ** khớp giữa client và máy chủ
4. **Thử với MCP Inspector** trước để kiểm tra chức năng máy chủ

## Tài liệu liên quan

- [Hướng dẫn chính cho Client](./README.md)
- [Ví dụ MCP Server](../../../../03-GettingStarted/01-first-server)
- [MCP với tích hợp LLM](../../../../03-GettingStarted/03-llm-client)
- [Tài liệu chính thức MCP](https://modelcontextprotocol.io/)

**Tuyên bố từ chối trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ gốc của nó nên được coi là nguồn chính xác và đáng tin cậy. Đối với các thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp do con người thực hiện. Chúng tôi không chịu trách nhiệm về bất kỳ sự hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.