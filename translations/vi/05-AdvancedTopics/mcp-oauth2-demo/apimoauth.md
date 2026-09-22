# Triển khai Ứng dụng Spring AI MCP lên Azure Container Apps

> [!WARNING]
> Máy chủ ủy quyền/tài nguyên kết hợp này nhằm mục đích học tập và sử dụng thử/nghiệm. Các hệ thống sản xuất nên sử dụng nhà cung cấp danh tính riêng biệt,
> khóa ký bền vững và thông tin đăng nhập được lưu trữ trong kho bí mật được quản lý.




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

Lệnh này tạo một Container App có thể truy cập công khai với HTTPS được bật (Azure cấp chứng chỉ TLS miễn phí cho tên miền mặc định `*.azurecontainerapps.io` ([Tên miền tùy chỉnh và chứng chỉ được quản lý miễn phí trong Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements))). Kết quả lệnh bao gồm tên miền đầy đủ của ứng dụng (ví dụ `my-mcp-app.eastus.azurecontainerapps.io`), đây là cơ sở của **URL issuer**. Đảm bảo đã bật ingress HTTP (như trên) để APIM có thể truy cập ứng dụng. Trong cấu hình kiểm thử/ phát triển, sử dụng tùy chọn `--ingress external` (hoặc liên kết một tên miền tùy chỉnh với TLS theo [tài liệu Microsoft](https://learn.microsoft.com/azure/container-apps/custom-domains-managed-certificates) ([Tên miền tùy chỉnh và chứng chỉ được quản lý miễn phí trong Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements))). Lưu trữ các thuộc tính nhạy cảm (như bí mật client OAuth) trong secrets của Container Apps hoặc Azure Key Vault, và ánh xạ chúng vào container dưới dạng biến môi trường. 

## Cấu hình Spring Authorization Server

Trong mã ứng dụng Spring Boot của bạn, bao gồm các starter của Spring Authorization Server và Resource Server. Cấu hình một `RegisteredClient` (cho grant `client_credentials` trong dev/test) và nguồn khóa JWT. Ví dụ, trong `application.properties` bạn có thể thiết lập:

```properties
# OAuth2 client (for testing token issuance)
demo.oauth.client-id=${OAUTH_CLIENT_ID:mcp-client}
demo.oauth.client-secret=${OAUTH_CLIENT_SECRET}
```

Kích hoạt Authorization Server và Resource Server bằng cách định nghĩa chuỗi bộ lọc bảo mật. Ví dụ:

```java
@Configuration
@EnableWebSecurity
public class SecurityConfiguration {

    @Bean
    SecurityFilterChain securityFilterChain(HttpSecurity http) throws Exception {
        OAuth2AuthorizationServerConfigurer<HttpSecurity> authzServer = OAuth2AuthorizationServerConfigurer.authorizationServer();
        http
            .authorizeHttpRequests(auth -> auth.anyRequest().authenticated())
            // Bật các điểm cuối của Máy chủ Ủy quyền
            .apply(authzServer.and())
            // Bật Máy chủ Tài nguyên (xác thực JWT trên các yêu cầu đến)
            .oauth2ResourceServer(oauth2 -> oauth2.jwt(withDefaults()))
            // Tắt CSRF (máy chủ MCP không dựa trên trình duyệt)
            .csrf(csrf -> csrf.disable())
            // Cho phép CORS cho các công cụ demo của khách hàng
            .cors(withDefaults());
        return http.build();
    }

    // Định nghĩa một khách hàng bộ nhớ trong (RegisteredClient) và một nguồn JWK:
    @Bean
    public RegisteredClientRepository registeredClientRepository(
        @Value("${demo.oauth.client-id}") String clientId,
        @Value("${demo.oauth.client-secret}") String clientSecret) {
      PasswordEncoder encoder = PasswordEncoderFactories.createDelegatingPasswordEncoder();
        RegisteredClient client = RegisteredClient.withId("1")
        .clientId(clientId)
        .clientSecret(encoder.encode(clientSecret))
            .authorizationGrantType(AuthorizationGrantType.CLIENT_CREDENTIALS)
            .scope("mcp.read")
            .clientSettings(ClientSettings.builder().build())
            .tokenSettings(TokenSettings.builder().build())
            .build();
        return new InMemoryRegisteredClientRepository(client);
    }

    @Bean
    public JWKSource<SecurityContext> jwkSource() {
        // Tạo khóa RSA (dành cho phát triển/kiểm thử, tạo mới mỗi lần khởi động)
        RSAKey rsaKey = new RSAKeyGenerator(2048).keyID("1").generate();
        JWKSet jwkSet = new JWKSet(rsaKey);
        return (selector, context) -> selector.select(jwkSet);
    }
}
```

Cấu hình này sẽ tiết lộ các endpoint OAuth2 mặc định: `/oauth2/token` để lấy token và `/oauth2/jwks` cho JSON Web Key Set. (Mặc định Spring’s `AuthorizationServerSettings` ánh xạ `/oauth2/token` và `/oauth2/jwks` ([Mô hình Cấu hình :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)).) Máy chủ phát hành token truy cập JWT được ký bởi khóa RSA ở trên và công bố khóa công khai tại `https://<your-app>:/oauth2/jwks`. 

**Kích hoạt khám phá OpenID Connect:** Để APIM tự động lấy issuer và JWKS, hãy kích hoạt endpoint cấu hình nhà cung cấp OIDC bằng cách thêm `.oidc(Customizer.withDefaults())` trong cấu hình bảo mật của bạn ([Mô hình Cấu hình :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)). Ví dụ:

```java
http
  .apply(authzServer.and())
  .securityMatcher(authzServer.getEndpointsMatcher())
  .with(authzServer, authz -> authz
      .oidc(Customizer.withDefaults()));  // <– cho phép /.well-known/openid-configuration
```

Endpoint này tiết lộ `/.well-known/openid-configuration` mà APIM có thể dùng để lấy metadata. Cuối cùng, bạn có thể muốn tùy chỉnh claim **audience** trong JWT để kiểm tra `<audiences>` của APIM sẽ vượt qua. Ví dụ, thêm một token customizer:

```java
@Bean
public OAuth2TokenCustomizer<OAuth2TokenClaimsContext> tokenCustomizer() {
    return context -> {
        // Đặt một đối tượng tùy chỉnh (ví dụ: ID khách hàng hoặc nhận dạng API)
        context.getClaims().audience(Collections.singletonList("mcp-client"));
    };
}
```

Điều này đảm bảo token mang `"aud": ["mcp-client"]`, khớp với client ID hoặc phạm vi mà APIM mong đợi. 

## Tiết lộ các Endpoint Token và JWKS

Sau khi triển khai, **URL issuer** của ứng dụng bạn sẽ là `https://<app-fqdn>`, ví dụ `https://my-mcp-app.eastus.azurecontainerapps.io`. Các endpoint OAuth2 của nó là:

- **Token endpoint:** `https://<app-fqdn>/oauth2/token` – client lấy token ở đây (luồng client_credentials).
- **JWKS endpoint:** `https://<app-fqdn>/oauth2/jwks` – trả về tập JWK (APIM dùng để lấy khóa ký).
- **Cấu hình OpenID:** `https://<app-fqdn>/.well-known/openid-configuration` – JSON khám phá OIDC (chứa `issuer`, `token_endpoint`, `jwks_uri`, vv.).  

APIM sẽ dùng **URL cấu hình OpenID**, từ đó phát hiện `jwks_uri`. Ví dụ, nếu FQDN Container App của bạn là `my-mcp-app.eastus.azurecontainerapps.io`, thì `<openid-config url="...">` của APIM nên dùng `https://my-mcp-app.eastus.azurecontainerapps.io/.well-known/openid-configuration`. (Mặc định Spring sẽ đặt `issuer` trong metadata này giống URL cơ sở ([Mô hình Cấu hình :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)).)

## Cấu hình Azure API Management (`validate-jwt`)

Trong Azure APIM, thêm một chính sách inbound sử dụng `<validate-jwt>` để kiểm tra JWT đến với Spring Authorization Server của bạn. Với cấu hình đơn giản, bạn có thể dùng URL metadata OpenID Connect. Ví dụ đoạn chính sách:

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

Chính sách này yêu cầu APIM lấy cấu hình OpenID từ Spring Auth Server, lấy JWKS của nó và xác thực mỗi token được ký bởi khóa tin cậy và có audience đúng. (Nếu bạn bỏ qua `<issuers>`, APIM sẽ tự động dùng claim `issuer` trong metadata.) `<audience>` phải khớp với client ID hoặc định danh tài nguyên API trong token (ví dụ trên, chúng ta đặt `"mcp-client"`). Điều này phù hợp với tài liệu Microsoft về sử dụng `validate-jwt` với `<openid-config>` ([Tham khảo chính sách Azure API Management - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)).

Sau khi xác thực, APIM sẽ chuyển tiếp yêu cầu (bao gồm header `Authorization` gốc) tới backend. Vì ứng dụng Spring cũng là máy chủ tài nguyên, nó sẽ xác thực lại token, nhưng APIM đã đảm bảo token hợp lệ. (Trong phát triển, bạn có thể chỉ dựa vào kiểm tra của APIM và tắt kiểm tra thêm trong ứng dụng nếu muốn, nhưng tốt nhất là giữ cả hai.)

## Ví dụ Cài đặt

| Cài đặt           | Giá trị Ví dụ                                                     | Ghi chú                                    |
|-------------------|------------------------------------------------------------------|--------------------------------------------|
| **Issuer**        | `https://my-mcp-app.eastus.azurecontainerapps.io`                | URL Container App của bạn (URI cơ sở)      |
| **Token endpoint**| `https://my-mcp-app.eastus.azurecontainerapps.io/oauth2/token`   | Endpoint token mặc định của Spring ([Mô hình Cấu hình :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize))  |
| **JWKS endpoint** | `https://my-mcp-app.eastus.azurecontainerapps.io/oauth2/jwks`    | Endpoint JWK Set mặc định ([Mô hình Cấu hình :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize))    |
| **OpenID Config** | `https://my-mcp-app.eastus.azurecontainerapps.io/.well-known/openid-configuration` | Tài liệu khám phá OIDC (tạo tự động)        |
| **APIM audience** | `mcp-client`                                                     | ID client OAuth hoặc tên tài nguyên API    |
| **Chính sách APIM**| `<openid-config url="https://.../.well-known/openid-configuration" />` | `<validate-jwt>` sử dụng URL này ([Tham khảo chính sách Azure API Management - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)) |

## Những lỗi Thường Gặp

- **HTTPS/TLS:** Gateway APIM yêu cầu endpoint OpenID/JWKS phải dùng HTTPS với chứng chỉ hợp lệ. Mặc định, Azure Container Apps cung cấp chứng chỉ TLS tin cậy cho tên miền được Azure quản lý ([Tên miền tùy chỉnh và chứng chỉ được quản lý miễn phí trong Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)). Nếu bạn dùng tên miền tùy chỉnh, hãy chắc chắn liên kết chứng chỉ (bạn có thể dùng tính năng chứng chỉ quản lý miễn phí của Azure) ([Tên miền tùy chỉnh và chứng chỉ được quản lý miễn phí trong Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)). Nếu APIM không tin cậy chứng chỉ của endpoint, `<validate-jwt>` sẽ không thể lấy metadata.  

- **Truy cập Endpoint:** Đảm bảo các endpoint của ứng dụng Spring có thể truy cập từ APIM. Dùng `--ingress external` (hoặc kích hoạt ingress trong portal) là cách đơn giản nhất. Nếu bạn chọn môi trường nội bộ hoặc ràng buộc vNet, APIM (mặc định công khai) có thể không truy cập được trừ khi đặt cùng trong VNet. Trong thiết lập thử nghiệm, ưu tiên ingress công khai để APIM có thể gọi các URL `.well-known` và `/jwks`. 

- **Kích hoạt khám phá OpenID:** Theo mặc định, Spring Authorization Server **không công bố** `/.well-known/openid-configuration` nếu không bật OIDC. Hãy chắc chắn thêm `.oidc(Customizer.withDefaults())` trong cấu hình bảo mật của bạn (xem trên) để kích hoạt endpoint cấu hình nhà cung cấp ([Mô hình Cấu hình :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)). Nếu không, lệnh gọi `<openid-config>` của APIM sẽ trả về 404.

- **Claim Audience:** Hành vi mặc định của Spring là đặt claim `aud` thành client ID. Nếu kiểm tra `<audience>` của APIM thất bại, bạn có thể cần tùy chỉnh token (như đã trình bày) hoặc điều chỉnh chính sách APIM. Đảm bảo audience trong JWT của bạn khớp với cấu hình trong `<audience>`. 

- **Phân tích Metadata JSON:** JSON cấu hình OpenID phải hợp lệ. Cấu hình mặc định của Spring sẽ xuất một tài liệu metadata OIDC chuẩn. Kiểm tra xem có chứa `issuer` và `jwks_uri` đúng không. Nếu bạn host Spring phía sau proxy hoặc tuyến đường dựa trên đường dẫn, hãy kiểm tra kỹ các URL trong metadata này. APIM sẽ dùng các giá trị đó y nguyên. 

- **Thứ tự Chính sách:** Trong chính sách APIM, đặt `<validate-jwt>` **trước** bất kỳ định tuyến nào tới backend. Nếu không, các cuộc gọi có thể đến ứng dụng của bạn mà không có token hợp lệ. Cũng đảm bảo `<validate-jwt>` nằm ngay dưới `<inbound>` (không lồng trong điều kiện khác) để APIM áp dụng chính sách.

Bằng cách thực hiện theo các bước trên, bạn có thể chạy máy chủ Spring AI MCP của mình trong Azure Container Apps và để Azure API Management xác thực JWT OAuth2 đến với chính sách tối giản. Các điểm chính là: tiết lộ các endpoint Spring Auth công khai với TLS, bật khám phá OIDC, và trỏ `validate-jwt` của APIM tới URL cấu hình OpenID (để có thể tự động lấy JWKS). Cấu hình này phù hợp với môi trường dev/test; với sản xuất, hãy cân nhắc quản lý bí mật đúng cách, thời gian sống token và xoay khóa trong JWKS khi cần.


**Tài liệu tham khảo:** Xem tài liệu Spring Authorization Server cho các điểm cuối mặc định ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)) và cấu hình OIDC ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)); xem tài liệu Microsoft APIM cho ví dụ `validate-jwt` ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)); và tài liệu Azure Container Apps cho triển khai và chứng chỉ ([Deploy Java Spring Boot apps to Azure Container Apps - Java on Azure | Microsoft Learn](https://learn.microsoft.com/en-us/azure/developer/java/identity/deploy-spring-boot-to-azure-container-apps#:~:text=Now%20you%20can%20deploy%20your,CLI%20command)) ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Tuyên bố miễn trừ trách nhiệm**:
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng bản dịch tự động có thể chứa lỗi hoặc sai sót. Tài liệu gốc bằng ngôn ngữ gốc nên được coi là nguồn tin chính thức. Đối với thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm về bất kỳ hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->