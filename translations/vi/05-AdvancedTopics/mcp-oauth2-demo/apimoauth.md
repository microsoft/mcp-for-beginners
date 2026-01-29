# Triển khai ứng dụng Spring AI MCP trên Azure Container Apps

([Securing Spring AI MCP servers with OAuth2](https://spring.io/blog/2025/04/02/mcp-server-oauth2)) *Hình minh họa: Máy chủ Spring AI MCP được bảo mật bằng Spring Authorization Server. Máy chủ phát hành token truy cập cho client và xác thực chúng trên các yêu cầu đến (nguồn: Spring blog) ([Securing Spring AI MCP servers with OAuth2](https://spring.io/blog/2025/04/02/mcp-server-oauth2#:~:text=,server%20with%20the%20MCP%20inspector)).* Để triển khai máy chủ Spring MCP, bạn xây dựng nó dưới dạng container và sử dụng Azure Container Apps với ingress bên ngoài. Ví dụ, sử dụng Azure CLI bạn có thể chạy:

```bash
az containerapp up \
  --name my-mcp-app \
  --resource-group MyResourceGroup \
  --location eastus \
  --environment MyContainerEnv \
  --image myregistry.azurecr.io/my-mcp-server:latest \
  --ingress external \
  --target-port 8080 \
  --query properties.configuration.ingress.fqdn
```

Lệnh này tạo một Container App có thể truy cập công khai với HTTPS được bật (Azure cấp chứng chỉ TLS miễn phí cho domain mặc định `*.azurecontainerapps.io` ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements))). Kết quả lệnh bao gồm FQDN của ứng dụng (ví dụ `my-mcp-app.eastus.azurecontainerapps.io`), đây sẽ là cơ sở của **issuer URL**. Đảm bảo ingress HTTP được bật (như trên) để APIM có thể truy cập ứng dụng. Trong môi trường thử nghiệm/phát triển, sử dụng tùy chọn `--ingress external` (hoặc liên kết domain tùy chỉnh với TLS theo [Microsoft docs](https://learn.microsoft.com/azure/container-apps/custom-domains-managed-certificates) ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements))). Lưu trữ các thuộc tính nhạy cảm (như client secret OAuth) trong Container Apps secrets hoặc Azure Key Vault, và ánh xạ chúng vào container dưới dạng biến môi trường.

## Cấu hình Spring Authorization Server

Trong mã ứng dụng Spring Boot của bạn, bao gồm các starter Spring Authorization Server và Resource Server. Cấu hình một `RegisteredClient` (cho grant `client_credentials` trong dev/test) và nguồn khóa JWT. Ví dụ, trong `application.properties` bạn có thể đặt:

```properties
# OAuth2 client (for testing token issuance)
spring.security.oauth2.authorizationserver.client.oidc-client.registration.client-id=mcp-client
spring.security.oauth2.authorizationserver.client.oidc-client.registration.client-secret={noop}secret
spring.security.oauth2.authorizationserver.client.oidc-client.registration.authorization-grant-types=client_credentials
spring.security.oauth2.authorizationserver.client.oidc-client.registration.client-authentication-methods=client_secret_basic
```

Kích hoạt Authorization Server và Resource Server bằng cách định nghĩa một chuỗi filter bảo mật. Ví dụ:

```java
@Configuration
@EnableWebSecurity
public class SecurityConfiguration {

    @Bean
    SecurityFilterChain securityFilterChain(HttpSecurity http) throws Exception {
        OAuth2AuthorizationServerConfigurer<HttpSecurity> authzServer = OAuth2AuthorizationServerConfigurer.authorizationServer();
        http
            .authorizeHttpRequests(auth -> auth.anyRequest().authenticated())
            // Enable the Authorization Server endpoints
            .apply(authzServer.and())
            // Enable the Resource Server (validate JWT on incoming requests)
            .oauth2ResourceServer(oauth2 -> oauth2.jwt(withDefaults()))
            // Disable CSRF (MCP server is not browser-based)
            .csrf(csrf -> csrf.disable())
            // Allow CORS for client demo tools
            .cors(withDefaults());
        return http.build();
    }

    // Define an in-memory client (RegisteredClient) and a JWK source:
    @Bean
    public RegisteredClientRepository registeredClientRepository() {
        RegisteredClient client = RegisteredClient.withId("1")
            .clientId("mcp-client")
            .clientSecret("{noop}secret")
            .authorizationGrantType(AuthorizationGrantType.CLIENT_CREDENTIALS)
            .scope("mcp.read")
            .clientSettings(ClientSettings.builder().build())
            .tokenSettings(TokenSettings.builder().build())
            .build();
        return new InMemoryRegisteredClientRepository(client);
    }

    @Bean
    public JWKSource<SecurityContext> jwkSource() {
        // Generate an RSA key (for dev/test, generate anew at startup)
        RSAKey rsaKey = new RSAKeyGenerator(2048).keyID("1").generate();
        JWKSet jwkSet = new JWKSet(rsaKey);
        return (selector, context) -> selector.select(jwkSet);
    }
}
```

Cấu hình này sẽ mở các endpoint OAuth2 mặc định: `/oauth2/token` để lấy token và `/oauth2/jwks` cho JSON Web Key Set. (Mặc định, `AuthorizationServerSettings` của Spring ánh xạ `/oauth2/token` và `/oauth2/jwks` ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)).) Máy chủ sẽ phát hành token truy cập JWT được ký bằng khóa RSA ở trên, và công bố khóa công khai tại `https://<your-app>:/oauth2/jwks`.

**Bật OpenID Connect discovery:** Để APIM tự động lấy issuer và JWKS, bật endpoint cấu hình nhà cung cấp OIDC bằng cách thêm `.oidc(Customizer.withDefaults())` trong cấu hình bảo mật của bạn ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)). Ví dụ:

```java
http
  .apply(authzServer.and())
  .securityMatcher(authzServer.getEndpointsMatcher())
  .with(authzServer, authz -> authz
      .oidc(Customizer.withDefaults()));  // <– enables /.well-known/openid-configuration
```

Điều này sẽ mở endpoint `/.well-known/openid-configuration`, mà APIM có thể dùng để lấy metadata. Cuối cùng, bạn có thể muốn tùy chỉnh claim **audience** trong JWT để APIM có thể kiểm tra `<audiences>` thành công. Ví dụ, thêm một token customizer:

```java
@Bean
public OAuth2TokenCustomizer<OAuth2TokenClaimsContext> tokenCustomizer() {
    return context -> {
        // Set a custom audience (e.g. the client ID or API identifier)
        context.getClaims().audience(Collections.singletonList("mcp-client"));
    };
}
```

Điều này đảm bảo token mang `"aud": ["mcp-client"]`, khớp với client ID hoặc scope mà APIM mong đợi.

## Mở các endpoint Token và JWKS

Sau khi triển khai, **issuer URL** của ứng dụng bạn sẽ là `https://<app-fqdn>`, ví dụ `https://my-mcp-app.eastus.azurecontainerapps.io`. Các endpoint OAuth2 của nó là:

- **Token endpoint:** `https://<app-fqdn>/oauth2/token` – nơi client lấy token (flow client_credentials).
- **JWKS endpoint:** `https://<app-fqdn>/oauth2/jwks` – trả về bộ JWK (APIM dùng để lấy khóa ký).
- **OpenID Config:** `https://<app-fqdn>/.well-known/openid-configuration` – JSON OIDC discovery (chứa `issuer`, `token_endpoint`, `jwks_uri`, v.v.).

APIM sẽ trỏ đến **URL cấu hình OpenID**, từ đó nó phát hiện `jwks_uri`. Ví dụ, nếu FQDN Container App của bạn là `my-mcp-app.eastus.azurecontainerapps.io`, thì `<openid-config url="...">` của APIM nên dùng `https://my-mcp-app.eastus.azurecontainerapps.io/.well-known/openid-configuration`. (Mặc định Spring sẽ đặt `issuer` trong metadata này là cùng URL cơ sở ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)).)

## Cấu hình Azure API Management (`validate-jwt`)

Trong Azure APIM, thêm một policy inbound sử dụng `<validate-jwt>` để kiểm tra JWT đến với Spring Authorization Server của bạn. Với cấu hình đơn giản, bạn có thể dùng URL metadata OpenID Connect. Ví dụ đoạn policy:

```xml
<inbound>
  <validate-jwt header-name="Authorization" require-scheme="Bearer">
    <openid-config url="https://my-mcp-app.eastus.azurecontainerapps.io/.well-known/openid-configuration" />
    <audiences>
      <audience>mcp-client</audience>  <!-- Expected audience in the JWT -->
    </audiences>
    <issuers>
      <issuer>https://my-mcp-app.eastus.azurecontainerapps.io</issuer>
    </issuers>
  </validate-jwt>
  <!-- (optional) other policies -->
</inbound>
```

Policy này yêu cầu APIM lấy cấu hình OpenID từ Spring Auth Server, lấy JWKS, và xác thực mỗi token được ký bởi khóa tin cậy và có audience đúng. (Nếu bạn bỏ `<issuers>`, APIM sẽ tự động dùng claim `issuer` từ metadata.) `<audience>` phải khớp với client ID hoặc tên tài nguyên API trong token (ví dụ trên là `"mcp-client"`). Điều này phù hợp với tài liệu Microsoft về dùng `validate-jwt` với `<openid-config>` ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)).

Sau khi xác thực, APIM sẽ chuyển tiếp yêu cầu (bao gồm header `Authorization` gốc) đến backend. Vì ứng dụng Spring cũng là resource server, nó sẽ xác thực lại token, nhưng APIM đã đảm bảo token hợp lệ. (Trong phát triển, bạn có thể chỉ dựa vào kiểm tra của APIM và tắt kiểm tra thêm trong app nếu muốn, nhưng tốt hơn là giữ cả hai.)

## Ví dụ cấu hình

| Cài đặt            | Giá trị ví dụ                                                        | Ghi chú                                    |
|--------------------|----------------------------------------------------------------------|--------------------------------------------|
| **Issuer**         | `https://my-mcp-app.eastus.azurecontainerapps.io`                    | URL Container App của bạn (URI cơ sở)      |
| **Token endpoint** | `https://my-mcp-app.eastus.azurecontainerapps.io/oauth2/token`       | Endpoint token mặc định của Spring ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize))  |
| **JWKS endpoint**  | `https://my-mcp-app.eastus.azurecontainerapps.io/oauth2/jwks`        | Endpoint JWK Set mặc định ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize))    |
| **OpenID Config**  | `https://my-mcp-app.eastus.azurecontainerapps.io/.well-known/openid-configuration` | Tài liệu discovery OIDC (tự động tạo)       |
| **APIM audience**  | `mcp-client`                                                         | Client ID OAuth hoặc tên tài nguyên API    |
| **APIM policy**    | `<openid-config url="https://.../.well-known/openid-configuration" />` | `<validate-jwt>` dùng URL này ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)) |

## Những lỗi thường gặp

- **HTTPS/TLS:** Cổng APIM yêu cầu endpoint OpenID/JWKS phải dùng HTTPS với chứng chỉ hợp lệ. Mặc định, Azure Container Apps cung cấp chứng chỉ TLS tin cậy cho domain do Azure quản lý ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)). Nếu bạn dùng domain tùy chỉnh, hãy chắc chắn đã liên kết chứng chỉ (bạn có thể dùng tính năng chứng chỉ quản lý miễn phí của Azure) ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)). Nếu APIM không tin tưởng chứng chỉ của endpoint, `<validate-jwt>` sẽ không lấy được metadata.

- **Khả năng truy cập endpoint:** Đảm bảo các endpoint của ứng dụng Spring có thể truy cập được từ APIM. Dùng `--ingress external` (hoặc bật ingress trong portal) là cách đơn giản nhất. Nếu bạn chọn môi trường nội bộ hoặc gắn với vNet, APIM (mặc định là công khai) có thể không truy cập được trừ khi đặt trong cùng vNet. Trong môi trường thử nghiệm, ưu tiên ingress công khai để APIM gọi được các URL `.well-known` và `/jwks`.

- **Bật OpenID Discovery:** Mặc định, Spring Authorization Server **không mở** `/.well-known/openid-configuration` nếu không bật OIDC. Hãy chắc chắn thêm `.oidc(Customizer.withDefaults())` trong cấu hình bảo mật (xem phần trên) để endpoint cấu hình nhà cung cấp hoạt động ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)). Nếu không, gọi `<openid-config>` của APIM sẽ trả về 404.

- **Claim Audience:** Hành vi mặc định của Spring là đặt claim `aud` bằng client ID. Nếu kiểm tra `<audience>` của APIM không thành công, bạn cần tùy chỉnh token (như ví dụ trên) hoặc điều chỉnh policy APIM. Đảm bảo audience trong JWT khớp với cấu hình `<audience>`.

- **Phân tích JSON Metadata:** JSON cấu hình OpenID phải hợp lệ. Cấu hình mặc định của Spring sẽ phát ra tài liệu metadata OIDC chuẩn. Kiểm tra xem nó có chứa `issuer` và `jwks_uri` chính xác không. Nếu bạn chạy Spring phía sau proxy hoặc route theo đường dẫn, hãy kiểm tra kỹ các URL trong metadata này. APIM sẽ dùng các giá trị này nguyên trạng.

- **Thứ tự policy:** Trong policy APIM, đặt `<validate-jwt>` **trước** bất kỳ routing nào đến backend. Nếu không, các yêu cầu có thể đến app mà không có token hợp lệ. Đồng thời, đảm bảo `<validate-jwt>` nằm ngay dưới `<inbound>` (không nằm trong điều kiện khác) để APIM áp dụng chính sách này.

Bằng cách làm theo các bước trên, bạn có thể chạy máy chủ Spring AI MCP trong Azure Container Apps và để Azure API Management xác thực các JWT OAuth2 đến với một policy tối giản. Các điểm chính là: mở các endpoint Spring Auth công khai với TLS, bật OIDC discovery, và trỏ `validate-jwt` của APIM đến URL cấu hình OpenID (để tự động lấy JWKS). Cấu hình này phù hợp cho môi trường dev/test; với môi trường sản xuất, hãy cân nhắc quản lý bí mật đúng cách, thời gian sống token, và xoay khóa JWKS khi cần.
**Tham khảo:** Xem tài liệu Spring Authorization Server để biết các điểm cuối mặc định ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)) và cấu hình OIDC ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)); xem tài liệu Microsoft APIM để lấy ví dụ về `validate-jwt` ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)); và tài liệu Azure Container Apps để biết về triển khai và chứng chỉ ([Deploy Java Spring Boot apps to Azure Container Apps - Java on Azure | Microsoft Learn](https://learn.microsoft.com/en-us/azure/developer/java/identity/deploy-spring-boot-to-azure-container-apps#:~:text=Now%20you%20can%20deploy%20your,CLI%20command)) ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)).

**Tuyên bố từ chối trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ gốc của nó nên được coi là nguồn chính xác và đáng tin cậy. Đối với các thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp do con người thực hiện. Chúng tôi không chịu trách nhiệm về bất kỳ sự hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.