# MCP OAuth2 Demo

Dự án này là một **ứng dụng Spring Boot tối giản** hoạt động đồng thời như:

* một **Spring Authorization Server** (phát hành token truy cập JWT qua flow `client_credentials`), và  
* một **Resource Server** (bảo vệ endpoint `/hello` của chính nó).

Nó mô phỏng cấu hình được trình bày trong [bài viết trên blog Spring (2 Tháng 4, 2025)](https://spring.io/blog/2025/04/02/mcp-server-oauth2).

---

## Bắt đầu nhanh (cục bộ)

```bash
# build & run
./mvnw spring-boot:run

# obtain a token
curl -u mcp-client:secret -d grant_type=client_credentials \
     http://localhost:8081/oauth2/token | jq -r .access_token > token.txt

# call the protected endpoint
curl -H "Authorization: Bearer $(cat token.txt)" http://localhost:8081/hello
```

---

## Kiểm tra cấu hình OAuth2

Bạn có thể kiểm tra cấu hình bảo mật OAuth2 theo các bước sau:

### 1. Xác nhận server đang chạy và được bảo vệ

```bash
# This should return 401 Unauthorized, confirming OAuth2 security is active
curl -v http://localhost:8081/
```

### 2. Lấy token truy cập bằng client credentials

```bash
# Get and extract the full token response
curl -v -X POST http://localhost:8081/oauth2/token \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -H "Authorization: Basic bWNwLWNsaWVudDpzZWNyZXQ=" \
  -d "grant_type=client_credentials&scope=mcp.access"

# Or to extract just the token (requires jq)
curl -s -X POST http://localhost:8081/oauth2/token \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -H "Authorization: Basic bWNwLWNsaWVudDpzZWNyZXQ=" \
  -d "grant_type=client_credentials&scope=mcp.access" | jq -r .access_token > token.txt
```

Lưu ý: Header Basic Authentication (`bWNwLWNsaWVudDpzZWNyZXQ=`) là mã hóa Base64 của `mcp-client:secret`.

### 3. Truy cập endpoint được bảo vệ bằng token

```bash
# Using the saved token
curl -H "Authorization: Bearer $(cat token.txt)" http://localhost:8081/hello

# Or directly with the token value
curl -H "Authorization: Bearer eyJra...token_value...xyz" http://localhost:8081/hello
```

Phản hồi thành công với "Hello from MCP OAuth2 Demo!" xác nhận cấu hình OAuth2 hoạt động chính xác.

---

## Xây dựng container

```bash
docker build -t mcp-oauth2-demo .
docker run -p 8081:8081 mcp-oauth2-demo
```

---

## Triển khai lên **Azure Container Apps**

```bash
az containerapp up -n mcp-oauth2 \
  -g demo-rg -l westeurope \
  --image <your-registry>/mcp-oauth2-demo:latest \
  --ingress external --target-port 8081
```

Ingress FQDN sẽ trở thành **issuer** của bạn (`https://<fqdn>`).  
Azure tự động cung cấp chứng chỉ TLS đáng tin cậy cho `*.azurecontainerapps.io`.

---

## Kết nối với **Azure API Management**

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

APIM sẽ lấy JWKS và xác thực mọi yêu cầu.

---

## Tiếp theo

- [5.4 Root contexts](../mcp-root-contexts/README.md)

**Tuyên bố từ chối trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ gốc của nó nên được coi là nguồn chính xác và đáng tin cậy. Đối với các thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp do con người thực hiện. Chúng tôi không chịu trách nhiệm về bất kỳ sự hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.