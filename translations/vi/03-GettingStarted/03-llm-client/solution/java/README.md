# Khách hàng LLM Máy tính

Một ứng dụng Java minh họa cách sử dụng LangChain4j để kết nối với dịch vụ máy tính MCP (Model Context Protocol) thông qua API MiniMax tương thích OpenAI.

## Yêu cầu trước

- Java 21 trở lên
- Maven 3.6+ (hoặc dùng Maven wrapper đi kèm)
- Một khóa API MiniMax
- Một dịch vụ máy tính MCP chạy trên `http://localhost:8080`

## Lấy Khóa API

Ứng dụng này sử dụng API MiniMax tương thích OpenAI. Thực hiện các bước sau để lấy khóa và endpoint của bạn:

### 1. Chọn endpoint
1. Dùng `https://api.minimax.io/v1` cho endpoint toàn cầu
2. Dùng `https://api.minimaxi.com/v1` cho endpoint Trung Quốc

### 2. Tạo khóa API
1. Tạo khóa API MiniMax từ tài khoản MiniMax của bạn
2. Giữ khóa ở nơi an toàn

### 3. Thiết lập Biến Môi Trường

#### Trên Windows (Command Prompt):
```cmd
set OPENAI_API_KEY=your_minimax_api_key_here
set OPENAI_BASE_URL=https://api.minimax.io/v1
set MINIMAX_MODEL_ID=MiniMax-M3
```

#### Trên Windows (PowerShell):
```powershell
$env:OPENAI_API_KEY="your_minimax_api_key_here"
$env:OPENAI_BASE_URL="https://api.minimax.io/v1"
$env:MINIMAX_MODEL_ID="MiniMax-M3"
```

#### Trên macOS/Linux:
```bash
export OPENAI_API_KEY=your_minimax_api_key_here
export OPENAI_BASE_URL=https://api.minimax.io/v1
export MINIMAX_MODEL_ID=MiniMax-M3
```

## Cài đặt và Thiết lập

1. **Sao chép hoặc điều hướng đến thư mục dự án**

2. **Cài đặt các phụ thuộc**:
   ```cmd
   mvnw clean install
   ```
   Hoặc nếu đã cài Maven toàn cục:
   ```cmd
   mvn clean install
   ```

3. **Thiết lập các biến môi trường** (xem phần "Lấy Khóa API" ở trên)

4. **Khởi động dịch vụ Máy tính MCP**:
   Đảm bảo bạn đã chạy dịch vụ máy tính MCP chương 1 trên `http://localhost:8080/sse`. Dịch vụ này phải đang chạy trước khi bạn khởi động client.

## Chạy Ứng dụng

```cmd
mvnw clean package
java -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## Ứng dụng Làm Gì

Ứng dụng minh họa ba tương tác chính với dịch vụ máy tính:

1. **Cộng**: Tính tổng 24.5 và 17.3
2. **Căn bậc hai**: Tính căn bậc hai của 144
3. **Trợ giúp**: Hiển thị các chức năng máy tính có sẵn

## Kết quả mong đợi

Khi chạy thành công, bạn sẽ thấy kết quả tương tự:

```
The sum of 24.5 and 17.3 is 41.8.
The square root of 144 is 12.
The calculator service provides the following functions: add, subtract, multiply, divide, sqrt, power...
```

## Khắc phục sự cố

### Các vấn đề phổ biến

1. **"Biến môi trường OPENAI_API_KEY chưa được thiết lập"**
   - Đảm bảo bạn đã thiết lập biến môi trường `OPENAI_API_KEY`
   - Khởi động lại terminal/cửa sổ command prompt sau khi thiết lập biến

2. **"Kết nối bị từ chối đến localhost:8080"**
   - Đảm bảo dịch vụ máy tính MCP đang chạy ở cổng 8080
   - Kiểm tra xem có dịch vụ khác đang dùng cổng 8080 không

3. **"Xác thực không thành công"**
   - Kiểm tra xem khóa API của bạn có hợp lệ không
   - Xác nhận rằng `OPENAI_BASE_URL` khớp với endpoint bạn định sử dụng

4. **Lỗi khi xây dựng bằng Maven**
   - Đảm bảo bạn đang dùng Java 21 trở lên: `java -version`
   - Thử xóa build trước: `mvnw clean`

### Gỡ lỗi

Để bật ghi nhật ký gỡ lỗi, thêm đối số JVM sau khi chạy:
```cmd
java -Dlogging.level.dev.langchain4j=DEBUG -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## Cấu hình

Ứng dụng được cấu hình để:
- Mặc định dùng MiniMax-M3; đặt `MINIMAX_MODEL_ID` để chọn `MiniMax-M3` hoặc `MiniMax-M2.7`
- Kết nối tới `OPENAI_BASE_URL` khi được thiết lập; nếu không sẽ dùng `https://api.minimaxi.com/v1` khi `MINIMAX_REGION=cn_zh`, hoặc `https://api.minimax.io/v1` theo mặc định
- Kết nối tới dịch vụ MCP tại `http://localhost:8080/sse`
- Dùng timeout 60 giây cho các yêu cầu

## Các phụ thuộc

Các phụ thuộc chính được sử dụng trong dự án này:
- **LangChain4j**: Để tích hợp AI và quản lý công cụ
- **LangChain4j MCP**: Cho hỗ trợ Model Context Protocol
- **LangChain4j OpenAI official**: Tích hợp API MiniMax tương thích OpenAI
- **Spring Boot**: Làm framework ứng dụng và tiêm phụ thuộc

## Giấy phép

Dự án này được cấp phép theo Giấy phép Apache 2.0 - xem tệp [LICENSE](../../../../../../03-GettingStarted/03-llm-client/solution/java/LICENSE) để biết chi tiết.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Tuyên bố miễn trừ trách nhiệm**:
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng bản dịch tự động có thể chứa lỗi hoặc sai sót. Tài liệu gốc bằng ngôn ngữ gốc nên được coi là nguồn tin chính thức. Đối với thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm về bất kỳ hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->