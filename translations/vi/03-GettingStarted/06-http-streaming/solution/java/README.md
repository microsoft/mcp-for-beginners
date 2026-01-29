# Demo Streaming HTTP Máy Tính

Dự án này minh họa streaming HTTP sử dụng Server-Sent Events (SSE) với Spring Boot WebFlux. Nó bao gồm hai ứng dụng:

- **Calculator Server**: Dịch vụ web phản ứng thực hiện các phép tính và truyền kết quả qua SSE
- **Calculator Client**: Ứng dụng client tiêu thụ endpoint streaming

## Yêu cầu

- Java 17 trở lên
- Maven 3.6 trở lên

## Cấu trúc Dự án

```
java/
├── calculator-server/     # Spring Boot server with SSE endpoint
│   ├── src/main/java/com/example/calculatorserver/
│   │   ├── CalculatorServerApplication.java
│   │   └── CalculatorController.java
│   └── pom.xml
├── calculator-client/     # Spring Boot client application
│   ├── src/main/java/com/example/calculatorclient/
│   │   └── CalculatorClientApplication.java
│   └── pom.xml
└── README.md
```

## Cách Hoạt Động

1. **Calculator Server** cung cấp endpoint `/calculate`:
   - Nhận các tham số truy vấn: `a` (số), `b` (số), `op` (phép toán)
   - Các phép toán hỗ trợ: `add`, `sub`, `mul`, `div`
   - Trả về Server-Sent Events với tiến trình và kết quả tính toán

2. **Calculator Client** kết nối tới server và:
   - Gửi yêu cầu tính `7 * 5`
   - Tiêu thụ phản hồi streaming
   - In từng sự kiện ra console

## Chạy Ứng Dụng

### Lựa chọn 1: Dùng Maven (Khuyến nghị)

#### 1. Khởi động Calculator Server

Mở terminal và chuyển đến thư mục server:

```bash
cd calculator-server
mvn clean package
mvn spring-boot:run
```

Server sẽ chạy tại `http://localhost:8080`

Bạn sẽ thấy đầu ra như sau:
```
Started CalculatorServerApplication in X.XXX seconds
Netty started on port 8080 (http)
```

#### 2. Chạy Calculator Client

Mở **terminal mới** và chuyển đến thư mục client:

```bash
cd calculator-client
mvn clean package
mvn spring-boot:run
```

Client sẽ kết nối tới server, thực hiện phép tính và hiển thị kết quả streaming.

### Lựa chọn 2: Chạy trực tiếp bằng Java

#### 1. Biên dịch và chạy server:

```bash
cd calculator-server
mvn clean package
java -jar target/calculator-server-0.0.1-SNAPSHOT.jar
```

#### 2. Biên dịch và chạy client:

```bash
cd calculator-client
mvn clean package
java -jar target/calculator-client-0.0.1-SNAPSHOT.jar
```

## Kiểm Tra Server Thủ Công

Bạn cũng có thể kiểm tra server bằng trình duyệt hoặc curl:

### Dùng trình duyệt:
Truy cập: `http://localhost:8080/calculate?a=10&b=5&op=add`

### Dùng curl:
```bash
curl "http://localhost:8080/calculate?a=10&b=5&op=add" -H "Accept: text/event-stream"
```

## Kết Quả Mong Đợi

Khi chạy client, bạn sẽ thấy kết quả streaming tương tự:

```
event:info
data:Calculating: 7.0 mul 5.0

event:result
data:35.0
```

## Các Phép Toán Hỗ Trợ

- `add` - Cộng (a + b)
- `sub` - Trừ (a - b)
- `mul` - Nhân (a * b)
- `div` - Chia (a / b, trả về NaN nếu b = 0)

## Tham Khảo API

### GET /calculate

**Tham số:**
- `a` (bắt buộc): Số thứ nhất (double)
- `b` (bắt buộc): Số thứ hai (double)
- `op` (bắt buộc): Phép toán (`add`, `sub`, `mul`, `div`)

**Phản hồi:**
- Content-Type: `text/event-stream`
- Trả về Server-Sent Events với tiến trình và kết quả tính toán

**Ví dụ Yêu cầu:**
```
GET /calculate?a=7&b=5&op=mul HTTP/1.1
Host: localhost:8080
Accept: text/event-stream
```

**Ví dụ Phản hồi:**
```
event: info
data: Calculating: 7.0 mul 5.0

event: result
data: 35.0
```

## Khắc Phục Sự Cố

### Các Vấn Đề Thường Gặp

1. **Cổng 8080 đã được sử dụng**
   - Dừng các ứng dụng khác đang dùng cổng 8080
   - Hoặc thay đổi cổng server trong `calculator-server/src/main/resources/application.yml`

2. **Kết nối bị từ chối**
   - Đảm bảo server đang chạy trước khi khởi động client
   - Kiểm tra server đã khởi động thành công trên cổng 8080

3. **Lỗi tên tham số**
   - Dự án có cấu hình Maven compiler với flag `-parameters`
   - Nếu gặp lỗi binding tham số, hãy chắc chắn dự án được build với cấu hình này

### Dừng Ứng Dụng

- Nhấn `Ctrl+C` trong terminal nơi ứng dụng đang chạy
- Hoặc dùng `mvn spring-boot:stop` nếu chạy dưới dạng background process

## Công Nghệ Sử Dụng

- **Spring Boot 3.3.1** - Framework ứng dụng
- **Spring WebFlux** - Framework web phản ứng
- **Project Reactor** - Thư viện reactive streams
- **Netty** - Server I/O không chặn
- **Maven** - Công cụ build
- **Java 17+** - Ngôn ngữ lập trình

## Bước Tiếp Theo

Thử chỉnh sửa code để:
- Thêm nhiều phép toán hơn
- Bao gồm xử lý lỗi cho các phép toán không hợp lệ
- Thêm ghi log request/response
- Triển khai xác thực
- Thêm unit test

**Tuyên bố từ chối trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ gốc của nó nên được coi là nguồn chính xác và đáng tin cậy. Đối với các thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp do con người thực hiện. Chúng tôi không chịu trách nhiệm về bất kỳ sự hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.