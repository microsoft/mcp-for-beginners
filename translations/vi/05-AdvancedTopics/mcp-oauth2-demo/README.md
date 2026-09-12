# MCP OAuth2 Demo

> [!WARNING]
> Đây là một ví dụ học tập cục bộ, không phải dịch vụ ủy quyền sản xuất. Nó
> sử dụng client trong bộ nhớ và tạo khóa ký mới khi khởi động. Không bao giờ
> triển khai nó với client secret được chia sẻ, mặc định hoặc kiểm soát nguồn.

## Giới thiệu

OAuth2 là giao thức tiêu chuẩn công nghiệp cho việc ủy quyền, cho phép truy cập an toàn tới tài nguyên mà không cần chia sẻ thông tin đăng nhập. Trong các triển khai MCP (Model Context Protocol), OAuth2 cung cấp cách mạnh mẽ để xác thực và ủy quyền cho các client (như tác nhân AI) truy cập các máy chủ MCP và công cụ của chúng.

Bài học này trình bày cách triển khai xác thực OAuth2 cho các máy chủ MCP sử dụng Spring Boot, một mô hình phổ biến cho các triển khai doanh nghiệp và sản xuất.

## Mục tiêu học tập

Sau bài học này, bạn sẽ:
- Hiểu cách OAuth2 tích hợp với các máy chủ MCP
- Triển khai một Spring Authorization Server để cấp token
- Bảo vệ các đầu cuối MCP với xác thực dựa trên JWT
- Cấu hình luồng client credentials cho giao tiếp máy với máy

## Yêu cầu trước

- Hiểu biết cơ bản về Java và Spring Boot
- Quen thuộc với các khái niệm MCP từ các module trước
- Đã cài đặt Maven hoặc Gradle

---

## Tổng quan dự án

Dự án này là một **ứng dụng Spring Boot tối giản** vừa làm:

* một **Spring Authorization Server** (cấp token truy cập JWT qua luồng `client_credentials`), và  
* một **Resource Server** (bảo vệ endpoint `/hello` của chính nó).

Nó mô phỏng cấu hình được trình bày trong [bài đăng blog Spring (2 Tháng 4 2025)](https://spring.io/blog/2025/04/02/mcp-server-oauth2).

---

## Bắt đầu nhanh (cục bộ)

```bash
# Sử dụng một giá trị cục bộ duy nhất và giữ nó khỏi lịch sử shell nếu có thể.
export OAUTH_CLIENT_SECRET="replace-with-a-random-local-secret"
mvn spring-boot:run

# lấy một token
curl -u "mcp-client:${OAUTH_CLIENT_SECRET}" -d grant_type=client_credentials \
     http://localhost:8081/oauth2/token | jq -r .access_token > token.txt

# gọi endpoint được bảo vệ
curl -H "Authorization: Bearer $(cat token.txt)" http://localhost:8081/hello
```

---

## Kiểm tra cấu hình OAuth2

Bạn có thể kiểm tra cấu hình bảo mật OAuth2 theo các bước sau:

### 1. Xác nhận máy chủ đang chạy và được bảo vệ

```bash
# Điều này nên trả về 401 Unauthorized, xác nhận rằng bảo mật OAuth2 đang hoạt động
curl -v http://localhost:8081/
```

### 2. Lấy token truy cập sử dụng client credentials

```bash
# Lấy và trích xuất phản hồi token đầy đủ
curl -v -X POST http://localhost:8081/oauth2/token \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -u "mcp-client:${OAUTH_CLIENT_SECRET}" \
  -d "grant_type=client_credentials&scope=mcp.access"

# Hoặc chỉ trích xuất token (yêu cầu jq)
curl -s -X POST http://localhost:8081/oauth2/token \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -u "mcp-client:${OAUTH_CLIENT_SECRET}" \
  -d "grant_type=client_credentials&scope=mcp.access" | jq -r .access_token > token.txt
```

Trên PowerShell, đặt secret cục bộ trước khi chạy Maven:

```powershell
$env:OAUTH_CLIENT_SECRET = "replace-with-a-random-local-secret"
mvn spring-boot:run
```

### 3. Truy cập endpoint được bảo vệ bằng token

```bash
# Sử dụng token đã lưu
curl -H "Authorization: Bearer $(cat token.txt)" http://localhost:8081/hello

# Hoặc trực tiếp với giá trị token
curl -H "Authorization: Bearer eyJra...token_value...xyz" http://localhost:8081/hello
```

Phản hồi thành công với "Hello from MCP OAuth2 Demo!" xác nhận cấu hình OAuth2 hoạt động đúng.

---

## Xây dựng container

```bash
docker build -t mcp-oauth2-demo .
docker run --rm -p 8081:8081 \
  -e OAUTH_CLIENT_SECRET="$OAUTH_CLIENT_SECRET" \
  mcp-oauth2-demo
```

## Bảo mật trong môi trường sản xuất

Đối với triển khai sản xuất, sử dụng nhà cung cấp định danh riêng thay vì
server ủy quyền demo chạy trong cùng tiến trình này. Lưu trữ thông tin đăng nhập trong kho secret được quản lý,
xoay vòng chúng, dùng khóa ký lâu dài, giới hạn phạm vi, và
đặt một issuer rõ ràng. Không bao giờ đặt client secret trong mã nguồn, hình ảnh container,
manifest triển khai, hoặc đầu ra lệnh.

Đối với Azure Container Apps, lưu giá trị này như một secret Container Apps được bảo vệ bởi
Key Vault nếu có thể, sau đó chỉ tiết lộ tham chiếu secret qua
biến môi trường `OAUTH_CLIENT_SECRET`.

---

## Triển khai vào **Azure Container Apps**

```bash
az containerapp up -n mcp-oauth2 \
  -g demo-rg -l westeurope \
  --image <your-registry>/mcp-oauth2-demo:latest \
  --ingress external --target-port 8081
```

Tên miền FQDN ingress sẽ trở thành **issuer** của bạn (`https://<fqdn>`).  
Azure tự động cung cấp chứng chỉ TLS đáng tin cậy cho `*.azurecontainerapps.io`.

---

## Kết nối vào **Azure API Management**

Thêm chính sách inbound này vào API của bạn:

```xml
<inbound>
  <validate-jwt header-name="Authorization">
    <openid-config url="https://<fqdn>/.well-known/openid-configuration"/>
    <audiences>
      <audience>mcp-client</audience>
    </audiences>
  </validate-jwt>
  <base/>
</inbound>
```

APIM sẽ lấy JWKS và xác thực từng yêu cầu.

---

## Tiếp theo là gì

- [5.4 Root contexts](../mcp-root-contexts/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Tuyên bố miễn trừ trách nhiệm**:
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng bản dịch tự động có thể chứa lỗi hoặc sai sót. Tài liệu gốc bằng ngôn ngữ gốc nên được coi là nguồn tin chính thức. Đối với thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm về bất kỳ hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->