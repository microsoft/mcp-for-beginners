# MCP OAuth2 데모

이 프로젝트는 **최소한의 Spring Boot 애플리케이션**으로, 다음 두 가지 역할을 합니다:

* **Spring 인증 서버** (`client_credentials` 플로우를 통해 JWT 액세스 토큰 발급),  
* **리소스 서버** (자체 `/hello` 엔드포인트 보호).

이는 [Spring 블로그 게시물(2025년 4월 2일)](https://spring.io/blog/2025/04/02/mcp-server-oauth2)에 소개된 설정을 그대로 반영합니다.

---

## 빠른 시작 (로컬)

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

## OAuth2 설정 테스트

다음 단계로 OAuth2 보안 구성을 테스트할 수 있습니다:

### 1. 서버가 실행 중이며 보안이 적용되었는지 확인

```bash
# This should return 401 Unauthorized, confirming OAuth2 security is active
curl -v http://localhost:8081/
```

### 2. 클라이언트 자격 증명을 사용해 액세스 토큰 받기

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

참고: Basic 인증 헤더(`bWNwLWNsaWVudDpzZWNyZXQ=`)는 `mcp-client:secret`의 Base64 인코딩 값입니다.

### 3. 토큰을 사용해 보호된 엔드포인트에 접근

```bash
# Using the saved token
curl -H "Authorization: Bearer $(cat token.txt)" http://localhost:8081/hello

# Or directly with the token value
curl -H "Authorization: Bearer eyJra...token_value...xyz" http://localhost:8081/hello
```

"Hello from MCP OAuth2 Demo!"라는 성공 응답이 오면 OAuth2 구성이 정상적으로 작동하는 것입니다.

---

## 컨테이너 빌드

```bash
docker build -t mcp-oauth2-demo .
docker run -p 8081:8081 mcp-oauth2-demo
```

---

## **Azure Container Apps**에 배포

```bash
az containerapp up -n mcp-oauth2 \
  -g demo-rg -l westeurope \
  --image <your-registry>/mcp-oauth2-demo:latest \
  --ingress external --target-port 8081
```

인그레스 FQDN이 **issuer** (`https://<fqdn>`)가 됩니다.  
Azure는 `*.azurecontainerapps.io`에 대해 신뢰할 수 있는 TLS 인증서를 자동으로 제공합니다.

---

## **Azure API Management**와 연동

API에 다음 인바운드 정책을 추가하세요:

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

APIM이 JWKS를 가져와 모든 요청을 검증합니다.

---

## 다음 단계

- [5.4 루트 컨텍스트](../mcp-root-contexts/README.md)

**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 최선을 다하고 있으나, 자동 번역에는 오류나 부정확한 부분이 있을 수 있음을 유의해 주시기 바랍니다. 원문은 해당 언어의 원본 문서가 권위 있는 출처로 간주되어야 합니다. 중요한 정보의 경우 전문적인 인간 번역을 권장합니다. 본 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.