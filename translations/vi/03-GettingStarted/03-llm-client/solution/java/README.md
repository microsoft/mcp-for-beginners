# Calculator LLM Client

Một ứng dụng Java minh họa cách sử dụng LangChain4j để kết nối với dịch vụ máy tính MCP (Model Context Protocol) tích hợp GitHub Models.

## Yêu cầu trước

- Java 21 trở lên
- Maven 3.6+ (hoặc sử dụng Maven wrapper đi kèm)
- Tài khoản GitHub có quyền truy cập GitHub Models
- Dịch vụ máy tính MCP đang chạy trên `http://localhost:8080`

## Lấy GitHub Token

Ứng dụng này sử dụng GitHub Models, yêu cầu token truy cập cá nhân GitHub. Thực hiện các bước sau để lấy token:

### 1. Truy cập GitHub Models
1. Truy cập [GitHub Models](https://github.com/marketplace/models)
2. Đăng nhập bằng tài khoản GitHub của bạn
3. Yêu cầu quyền truy cập GitHub Models nếu bạn chưa có

### 2. Tạo Personal Access Token
1. Truy cập [GitHub Settings → Developer settings → Personal access tokens → Tokens (classic)](https://github.com/settings/tokens)
2. Nhấn "Generate new token" → "Generate new token (classic)"
3. Đặt tên mô tả cho token (ví dụ: "MCP Calculator Client")
4. Chọn thời hạn hết hạn phù hợp
5. Chọn các phạm vi sau:
   - `repo` (nếu truy cập kho riêng tư)
   - `user:email`
6. Nhấn "Generate token"
7. **Quan trọng**: Sao chép token ngay lập tức - bạn sẽ không thể xem lại!

### 3. Thiết lập biến môi trường

#### Trên Windows (Command Prompt):
```cmd
set GITHUB_TOKEN=your_github_token_here
```

#### Trên Windows (PowerShell):
```powershell
$env:GITHUB_TOKEN="your_github_token_here"
```

#### Trên macOS/Linux:
```bash
export GITHUB_TOKEN=your_github_token_here
```

## Cài đặt và Thiết lập

1. **Clone hoặc chuyển đến thư mục dự án**

2. **Cài đặt các phụ thuộc**:
   ```cmd
   mvnw clean install
   ```
   Hoặc nếu bạn đã cài Maven toàn cục:
   ```cmd
   mvn clean install
   ```

3. **Thiết lập biến môi trường** (xem phần "Lấy GitHub Token" ở trên)

4. **Khởi động dịch vụ MCP Calculator**:
   Đảm bảo dịch vụ MCP calculator của chương 1 đang chạy trên `http://localhost:8080/sse`. Dịch vụ này phải chạy trước khi bạn khởi động client.

## Chạy Ứng dụng

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

### Các vấn đề thường gặp

1. **"GITHUB_TOKEN environment variable not set"**
   - Đảm bảo bạn đã thiết lập biến môi trường `GITHUB_TOKEN`
   - Khởi động lại terminal/command prompt sau khi thiết lập biến

2. **"Connection refused to localhost:8080"**
   - Đảm bảo dịch vụ MCP calculator đang chạy trên cổng 8080
   - Kiểm tra xem có dịch vụ khác đang chiếm cổng 8080 không

3. **"Authentication failed"**
   - Xác nhận token GitHub của bạn hợp lệ và có quyền phù hợp
   - Kiểm tra xem bạn có quyền truy cập GitHub Models không

4. **Lỗi build Maven**
   - Đảm bảo bạn đang dùng Java 21 trở lên: `java -version`
   - Thử dọn dẹp build: `mvnw clean`

### Gỡ lỗi

Để bật ghi log debug, thêm đối số JVM sau khi chạy:
```cmd
java -Dlogging.level.dev.langchain4j=DEBUG -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## Cấu hình

Ứng dụng được cấu hình để:
- Sử dụng GitHub Models với model `gpt-4.1-nano`
- Kết nối tới dịch vụ MCP tại `http://localhost:8080/sse`
- Sử dụng timeout 60 giây cho các yêu cầu
- Bật ghi log yêu cầu/phản hồi để hỗ trợ gỡ lỗi

## Phụ thuộc

Các phụ thuộc chính trong dự án:
- **LangChain4j**: Cho tích hợp AI và quản lý công cụ
- **LangChain4j MCP**: Hỗ trợ Model Context Protocol
- **LangChain4j GitHub Models**: Tích hợp GitHub Models
- **Spring Boot**: Framework ứng dụng và tiêm phụ thuộc

## Giấy phép

Dự án này được cấp phép theo Apache License 2.0 - xem file [LICENSE](../../../../../../03-GettingStarted/03-llm-client/solution/java/LICENSE) để biết chi tiết.

**Tuyên bố từ chối trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ gốc của nó nên được coi là nguồn chính xác và đáng tin cậy. Đối với các thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp do con người thực hiện. Chúng tôi không chịu trách nhiệm về bất kỳ sự hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.