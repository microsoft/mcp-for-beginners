# Máy tính LLM Client

> [!NOTE]
> Giải pháp này kết nối với dịch vụ máy tính HTTP+SSE cũ của khóa học và
> nhắm đến các API MCP `2025-11-25` SDK. Đây không phải là một ví dụ `2026-07-28` HTTP Streamable.






- Maven 3.6+ (hoặc sử dụng công cụ Maven wrapper đi kèm)
- Một khóa API MiniMax
- Dịch vụ máy tính MCP đang chạy trên `http://localhost:8080`






1. Sử dụng `https://api.minimax.io/v1` cho điểm kết nối toàn cầu
2. Sử dụng `https://api.minimaxi.com/v1` cho điểm kết nối tại Trung Quốc


1. Tạo khóa API MiniMax từ tài khoản MiniMax của bạn
2. Giữ khóa ở nơi an toàn




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

## Thiết lập và Cài đặt




   ```cmd
   mvnw clean install
   ```
   Hoặc nếu bạn đã cài Maven toàn cục:
   ```cmd
   mvn clean install
   ```

3. **Thiết lập các biến môi trường** (xem phần "Lấy khóa API" ở trên)


   Đảm bảo bạn đã khởi động dịch vụ máy tính MCP trong chương 1 trên `http://localhost:8080/sse`. Dịch vụ này nên được chạy trước khi bạn khởi động client.




```cmd
mvnw clean package
java -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## Ứng dụng làm gì

Ứng dụng trình bày ba tương tác chính với dịch vụ máy tính:

1. **Cộng**: Tính tổng của 24.5 và 17.3
2. **Căn bậc hai**: Tính căn bậc hai của 144
3. **Trợ giúp**: Hiển thị các chức năng máy tính có sẵn

## Kết quả mong đợi

Khi chạy thành công, bạn sẽ thấy kết quả tương tự như:

```
The sum of 24.5 and 17.3 is 41.8.
The square root of 144 is 12.
The calculator service provides the following functions: add, subtract, multiply, divide, sqrt, power...
```

## Khắc phục sự cố

### Các vấn đề phổ biến

1. **"Biến môi trường OPENAI_API_KEY chưa được thiết lập"**
   - Đảm bảo bạn đã thiết lập biến môi trường `OPENAI_API_KEY`
   - Khởi động lại terminal/cửa sổ lệnh sau khi thiết lập biến

2. **"Kết nối bị từ chối đến localhost:8080"**
   - Đảm bảo dịch vụ máy tính MCP đang chạy trên cổng 8080
   - Kiểm tra xem có dịch vụ nào khác đang dùng cổng 8080 không

3. **"Xác thực thất bại"**
   - Xác nhận khóa API của bạn hợp lệ
   - Kiểm tra `OPENAI_BASE_URL` có khớp với điểm cuối bạn dự định sử dụng không

4. **Lỗi build Maven**
   - Đảm bảo bạn dùng Java 21 hoặc mới hơn: `java -version`
   - Thử làm sạch build: `mvnw clean`

### Gỡ lỗi

Để bật ghi log gỡ lỗi, thêm tham số JVM sau khi chạy:
```cmd
java -Dlogging.level.dev.langchain4j=DEBUG -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## Cấu hình

Ứng dụng được cấu hình để:
- Mặc định sử dụng MiniMax-M3; đặt `MINIMAX_MODEL_ID` để chọn `MiniMax-M3` hoặc `MiniMax-M2.7`
- Kết nối đến `OPENAI_BASE_URL` nếu được đặt; nếu không sẽ dùng `https://api.minimaxi.com/v1` khi `MINIMAX_REGION=cn_zh`, hoặc `https://api.minimax.io/v1` mặc định
- Kết nối dịch vụ MCP tại `http://localhost:8080/sse`
- Sử dụng thời gian chờ 60 giây cho các yêu cầu

## Phụ thuộc

Các phụ thuộc chính được sử dụng trong dự án này:
- **LangChain4j**: Cho tích hợp AI và quản lý công cụ
- **LangChain4j MCP**: Cho hỗ trợ Model Context Protocol
- **LangChain4j OpenAI official**: Cho tích hợp API MiniMax tương thích OpenAI
- **Spring Boot**: Làm framework ứng dụng và tiêm phụ thuộc

## Giấy phép

Dự án này được cấp phép theo giấy phép Apache 2.0 - xem file [LICENSE](../../../../../../03-GettingStarted/03-llm-client/solution/java/LICENSE) để biết chi tiết.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Tuyên bố miễn trừ trách nhiệm**:
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng bản dịch tự động có thể chứa lỗi hoặc sai sót. Tài liệu gốc bằng ngôn ngữ gốc nên được coi là nguồn tin chính thức. Đối với thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm về bất kỳ hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->