# Khách hàng LLM Máy tính

Một ứng dụng Java minh họa cách sử dụng LangChain4j để kết nối với dịch vụ máy tính MCP (Model Context Protocol) qua API tương thích MiniMax OpenAI.

## Yêu cầu trước

- Java 21 hoặc cao hơn
- Maven 3.6+ (hoặc sử dụng Maven wrapper kèm theo)
- Một khóa API MiniMax
- Dịch vụ máy tính MCP đang chạy trên `http://localhost:8080`

## Lấy khóa API

Ứng dụng này sử dụng API tương thích MiniMax OpenAI. Làm theo các bước sau để lấy khóa và điểm cuối của bạn:

### 1. Chọn điểm cuối
1. Sử dụng `https://api.minimax.io/v1` cho điểm cuối toàn cầu
2. Sử dụng `https://api.minimaxi.com/v1` cho điểm cuối Trung Quốc

### 2. Tạo khóa API
1. Tạo khóa API MiniMax từ tài khoản MiniMax của bạn
2. Giữ khóa ở nơi an toàn

### 3. Đặt biến môi trường

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

## Thiết lập và cài đặt

1. **Sao chép hoặc vào thư mục dự án**

2. **Cài đặt các phụ thuộc**:
   ```cmd
   mvnw clean install
   ```
   Hoặc nếu bạn đã cài Maven toàn cục:
   ```cmd
   mvn clean install
   ```

3. **Thiết lập biến môi trường** (xem phần "Lấy khóa API" phía trên)

4. **Khởi động Dịch vụ Máy tính MCP**:
   Đảm bảo dịch vụ máy tính MCP của chương 1 đang chạy trên `http://localhost:8080/sse`. Dịch vụ này phải chạy trước khi bạn khởi động client.

## Chạy ứng dụng

```cmd
mvnw clean package
java -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## Ứng dụng làm gì

Ứng dụng minh họa ba tương tác chính với dịch vụ máy tính:

1. **Phép cộng**: Tính tổng của 24.5 và 17.3
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

### Vấn đề thường gặp

1. **"Biến môi trường OPENAI_API_KEY chưa được thiết lập"**
   - Đảm bảo bạn đã thiết lập biến môi trường `OPENAI_API_KEY`
   - Khởi động lại terminal/command prompt sau khi thiết lập biến

2. **"Kết nối bị từ chối với localhost:8080"**
   - Đảm bảo dịch vụ máy tính MCP đang chạy trên cổng 8080
   - Kiểm tra xem có dịch vụ nào khác đang dùng cổng 8080 không

3. **"Xác thực không thành công"**
   - Xác minh khóa API của bạn hợp lệ
   - Kiểm tra xem `OPENAI_BASE_URL` có khớp với điểm cuối bạn muốn dùng không

4. **Lỗi khi build Maven**
   - Đảm bảo bạn đang dùng Java 21 trở lên: `java -version`
   - Thử làm sạch build: `mvnw clean`

### Gỡ lỗi

Để bật ghi nhật ký gỡ lỗi, thêm đối số JVM sau khi chạy:
```cmd
java -Dlogging.level.dev.langchain4j=DEBUG -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## Cấu hình

Ứng dụng được cấu hình để:
- Sử dụng MiniMax-M3 theo mặc định, hoặc MiniMax-M2.7 khi `MINIMAX_MODEL_ID` được đặt
- Kết nối tới `OPENAI_BASE_URL` khi được đặt; nếu không dùng `https://api.minimaxi.com/v1` khi `MINIMAX_REGION=cn_zh`, hoặc `https://api.minimax.io/v1` theo mặc định
- Kết nối tới dịch vụ MCP tại `http://localhost:8080/sse`
- Sử dụng thời gian chờ 60 giây cho các yêu cầu

## Phụ thuộc

Các phụ thuộc chính được sử dụng trong dự án này:
- **LangChain4j**: Để tích hợp AI và quản lý công cụ
- **LangChain4j MCP**: Để hỗ trợ Model Context Protocol
- **LangChain4j OpenAI official**: Để tích hợp API tương thích MiniMax OpenAI
- **Spring Boot**: Để làm framework ứng dụng và tiêm phụ thuộc

## Giấy phép

Dự án này được cấp phép theo Giấy phép Apache 2.0 - xem file [LICENSE](../../../../../../03-GettingStarted/03-llm-client/solution/java/LICENSE) để biết chi tiết.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Tuyên bố miễn trừ trách nhiệm**:
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng bản dịch tự động có thể chứa lỗi hoặc sai sót. Tài liệu gốc bằng ngôn ngữ gốc nên được coi là nguồn tin chính thức. Đối với thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm về bất kỳ hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->