# MCP OAuth2 Demo

Bu proje, hem:

* **Spring Authorization Server** (JWT erişim tokenlarını `client_credentials` akışıyla veren), hem de  
* kendi `/hello` uç noktasını koruyan bir **Resource Server** olan  

**minimal bir Spring Boot uygulamasıdır**.

Bu yapı, [Spring blog yazısında (2 Nis 2025)](https://spring.io/blog/2025/04/02/mcp-server-oauth2) gösterilen kurulumla aynıdır.

---

## Hızlı başlangıç (yerel)

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

## OAuth2 Yapılandırmasını Test Etme

OAuth2 güvenlik yapılandırmasını aşağıdaki adımlarla test edebilirsiniz:

### 1. Sunucunun çalıştığını ve korunduğunu doğrulayın

```bash
# This should return 401 Unauthorized, confirming OAuth2 security is active
curl -v http://localhost:8081/
```

### 2. Client credentials kullanarak erişim tokenı alın

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

Not: Basic Authentication başlığı (`bWNwLWNsaWVudDpzZWNyZXQ=`), `mcp-client:secret` ifadesinin Base64 kodlamasıdır.

### 3. Token ile korunan uç noktaya erişin

```bash
# Using the saved token
curl -H "Authorization: Bearer $(cat token.txt)" http://localhost:8081/hello

# Or directly with the token value
curl -H "Authorization: Bearer eyJra...token_value...xyz" http://localhost:8081/hello
```

"Hello from MCP OAuth2 Demo!" mesajı ile başarılı bir yanıt, OAuth2 yapılandırmasının doğru çalıştığını gösterir.

---

## Container oluşturma

```bash
docker build -t mcp-oauth2-demo .
docker run -p 8081:8081 mcp-oauth2-demo
```

---

## **Azure Container Apps** üzerine dağıtım

```bash
az containerapp up -n mcp-oauth2 \
  -g demo-rg -l westeurope \
  --image <your-registry>/mcp-oauth2-demo:latest \
  --ingress external --target-port 8081
```

Ingress FQDN, sizin **issuer** adresiniz olur (`https://<fqdn>`).  
Azure, `*.azurecontainerapps.io` için otomatik olarak güvenilir bir TLS sertifikası sağlar.

---

## **Azure API Management** ile entegrasyon

API'nize aşağıdaki inbound policy'i ekleyin:

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

APIM, JWKS'i alacak ve her isteği doğrulayacaktır.

---

## Sonraki adımlar

- [5.4 Root contexts](../mcp-root-contexts/README.md)

**Feragatname**:  
Bu belge, AI çeviri servisi [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hatalar veya yanlışlıklar içerebileceğini lütfen unutmayın. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu oluşabilecek yanlış anlamalar veya yorum hatalarından sorumlu değiliz.