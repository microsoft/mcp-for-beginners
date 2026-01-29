# Spring AI MCP 앱을 Azure Container Apps에 배포하기

([Securing Spring AI MCP servers with OAuth2](https://spring.io/blog/2025/04/02/mcp-server-oauth2))  
*그림: Spring Authorization Server로 보호된 Spring AI MCP 서버. 서버는 클라이언트에 액세스 토큰을 발급하고, 들어오는 요청에서 이를 검증합니다 (출처: Spring 블로그) ([Securing Spring AI MCP servers with OAuth2](https://spring.io/blog/2025/04/02/mcp-server-oauth2#:~:text=,server%20with%20the%20MCP%20inspector)).*  
Spring MCP 서버를 배포하려면 컨테이너로 빌드한 후 Azure Container Apps에서 외부 인그레스를 사용하세요. 예를 들어, Azure CLI를 사용해 다음 명령을 실행할 수 있습니다:

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

이 명령은 HTTPS가 활성화된 공개 접근 가능한 Container App을 생성합니다 (Azure는 기본 `*.azurecontainerapps.io` 도메인에 대해 무료 TLS 인증서를 발급합니다 ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements))). 명령 출력에는 앱의 FQDN(예: `my-mcp-app.eastus.azurecontainerapps.io`)이 포함되며, 이 주소가 **issuer URL**의 기본이 됩니다. APIM이 앱에 접근할 수 있도록 HTTP 인그레스가 활성화되어 있는지 확인하세요 (위와 같이). 테스트/개발 환경에서는 `--ingress external` 옵션을 사용하거나, [Microsoft 문서](https://learn.microsoft.com/azure/container-apps/custom-domains-managed-certificates) ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements))에 따라 TLS가 적용된 커스텀 도메인을 바인딩할 수 있습니다.  
OAuth 클라이언트 시크릿 같은 민감한 속성은 Container Apps 시크릿이나 Azure Key Vault에 저장하고, 컨테이너 내 환경 변수로 매핑하세요.

## Spring Authorization Server 구성하기

Spring Boot 앱 코드에 Spring Authorization Server와 Resource Server 스타터를 포함하세요. `RegisteredClient`를 구성하고 (개발/테스트용 `client_credentials` 그랜트용), JWT 키 소스를 설정합니다. 예를 들어, `application.properties`에 다음과 같이 설정할 수 있습니다:

```properties
# OAuth2 client (for testing token issuance)
spring.security.oauth2.authorizationserver.client.oidc-client.registration.client-id=mcp-client
spring.security.oauth2.authorizationserver.client.oidc-client.registration.client-secret={noop}secret
spring.security.oauth2.authorizationserver.client.oidc-client.registration.authorization-grant-types=client_credentials
spring.security.oauth2.authorizationserver.client.oidc-client.registration.client-authentication-methods=client_secret_basic
```

보안 필터 체인을 정의하여 Authorization Server와 Resource Server를 활성화하세요. 예를 들면:

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

이 설정은 기본 OAuth2 엔드포인트인 `/oauth2/token` (토큰 발급용)과 `/oauth2/jwks` (JSON Web Key Set 제공용)를 노출합니다. (기본적으로 Spring의 `AuthorizationServerSettings`는 `/oauth2/token`과 `/oauth2/jwks`를 매핑합니다 ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)).) 서버는 위에서 설정한 RSA 키로 서명된 JWT 액세스 토큰을 발급하며, 공개 키는 `https://<your-app>:/oauth2/jwks`에서 제공합니다.

**OpenID Connect 디스커버리 활성화:** APIM이 issuer와 JWKS를 자동으로 가져갈 수 있도록, 보안 설정에 `.oidc(Customizer.withDefaults())`를 추가하여 OIDC 공급자 구성 엔드포인트를 활성화하세요 ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)). 예를 들면:

```java
http
  .apply(authzServer.and())
  .securityMatcher(authzServer.getEndpointsMatcher())
  .with(authzServer, authz -> authz
      .oidc(Customizer.withDefaults()));  // <– enables /.well-known/openid-configuration
```

이렇게 하면 `/.well-known/openid-configuration`이 노출되어 APIM이 메타데이터를 사용할 수 있습니다. 마지막으로, JWT의 **audience** 클레임을 APIM의 `<audiences>` 검사에 맞게 커스터마이징할 수 있습니다. 예를 들어, 토큰 커스터마이저를 추가하세요:

```java
@Bean
public OAuth2TokenCustomizer<OAuth2TokenClaimsContext> tokenCustomizer() {
    return context -> {
        // Set a custom audience (e.g. the client ID or API identifier)
        context.getClaims().audience(Collections.singletonList("mcp-client"));
    };
}
```

이렇게 하면 토큰에 `"aud": ["mcp-client"]`가 포함되어 APIM이 기대하는 클라이언트 ID 또는 스코프와 일치하게 됩니다.

## 토큰 및 JWKS 엔드포인트 노출하기

배포 후 앱의 **issuer URL**은 `https://<app-fqdn>`가 됩니다. 예: `https://my-mcp-app.eastus.azurecontainerapps.io`. OAuth2 엔드포인트는 다음과 같습니다:

- **토큰 엔드포인트:** `https://<app-fqdn>/oauth2/token` – 클라이언트가 토큰을 발급받는 곳 (client_credentials 플로우)
- **JWKS 엔드포인트:** `https://<app-fqdn>/oauth2/jwks` – JWK 세트를 반환 (APIM이 서명 키를 가져갈 때 사용)
- **OpenID 구성:** `https://<app-fqdn>/.well-known/openid-configuration` – OIDC 디스커버리 JSON (issuer, token_endpoint, jwks_uri 등 포함)

APIM은 **OpenID 구성 URL**을 참조하여 `jwks_uri`를 발견합니다. 예를 들어, Container App FQDN이 `my-mcp-app.eastus.azurecontainerapps.io`라면 APIM의 `<openid-config url="...">`는 `https://my-mcp-app.eastus.azurecontainerapps.io/.well-known/openid-configuration`을 사용해야 합니다. (기본적으로 Spring은 메타데이터 내 `issuer`를 동일한 기본 URL로 설정합니다 ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)).)

## Azure API Management (`validate-jwt`) 구성하기

Azure APIM에서, 들어오는 JWT를 Spring Authorization Server에 맞춰 검증하는 `<validate-jwt>` 정책을 인바운드 정책에 추가하세요. 간단한 설정으로 OpenID Connect 메타데이터 URL을 사용할 수 있습니다. 정책 예시는 다음과 같습니다:

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

이 정책은 APIM이 Spring Auth Server에서 OpenID 구성을 가져오고, JWKS를 조회하며, 각 토큰이 신뢰할 수 있는 키로 서명되었고 올바른 audience를 갖고 있는지 검증하도록 합니다. (`<issuers>`를 생략하면 APIM이 메타데이터의 `issuer` 클레임을 자동으로 사용합니다.) `<audience>`는 토큰 내 클라이언트 ID 또는 API 리소스 식별자와 일치해야 합니다 (위 예시에서는 `"mcp-client"`로 설정). 이는 Microsoft 문서에서 `<openid-config>`와 함께 `validate-jwt`를 사용하는 방법과 일치합니다 ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)).

검증 후 APIM은 원본 `Authorization` 헤더를 포함해 요청을 백엔드로 전달합니다. Spring 앱도 리소스 서버이므로 토큰을 다시 검증하지만, APIM이 이미 유효성을 확인한 상태입니다. (개발 시에는 APIM 검증만 신뢰하고 앱 내 추가 검증을 비활성화할 수 있지만, 두 단계 모두 유지하는 것이 더 안전합니다.)

## 예시 설정

| 설정               | 예시 값                                                             | 비고                                        |
|--------------------|----------------------------------------------------------------------|--------------------------------------------|
| **Issuer**         | `https://my-mcp-app.eastus.azurecontainerapps.io`                    | Container App의 URL (기본 URI)              |
| **Token endpoint** | `https://my-mcp-app.eastus.azurecontainerapps.io/oauth2/token`       | 기본 Spring 토큰 엔드포인트 ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize))  |
| **JWKS endpoint**  | `https://my-mcp-app.eastus.azurecontainerapps.io/oauth2/jwks`        | 기본 JWK 세트 엔드포인트 ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize))    |
| **OpenID Config**  | `https://my-mcp-app.eastus.azurecontainerapps.io/.well-known/openid-configuration` | OIDC 디스커버리 문서 (자동 생성)             |
| **APIM audience**  | `mcp-client`                                                         | OAuth 클라이언트 ID 또는 API 리소스 이름    |
| **APIM policy**    | `<openid-config url="https://.../.well-known/openid-configuration" />` | `<validate-jwt>`가 사용하는 URL ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)) |

## 자주 발생하는 문제점

- **HTTPS/TLS:** APIM 게이트웨이는 OpenID/JWKS 엔드포인트가 유효한 인증서가 적용된 HTTPS여야 합니다. 기본적으로 Azure Container Apps는 Azure 관리 도메인에 대해 신뢰할 수 있는 TLS 인증서를 제공합니다 ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)). 커스텀 도메인을 사용하는 경우 인증서를 반드시 바인딩해야 하며, Azure의 무료 관리 인증서 기능을 활용할 수 있습니다 ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)). APIM이 엔드포인트 인증서를 신뢰하지 못하면 `<validate-jwt>`가 메타데이터를 가져오지 못해 실패합니다.

- **엔드포인트 접근성:** Spring 앱의 엔드포인트가 APIM에서 접근 가능해야 합니다. `--ingress external` 옵션을 사용하거나 포털에서 인그레스를 활성화하는 것이 가장 간단합니다. 내부 또는 vNet 바인딩 환경을 선택한 경우, APIM(기본적으로 공개)은 동일한 vNet에 있지 않으면 접근할 수 없습니다. 테스트 환경에서는 APIM이 `.well-known`과 `/jwks` URL에 접근할 수 있도록 공개 인그레스를 권장합니다.

- **OpenID 디스커버리 활성화:** 기본적으로 Spring Authorization Server는 OIDC가 활성화되지 않으면 `/.well-known/openid-configuration`을 노출하지 않습니다. 보안 설정에 `.oidc(Customizer.withDefaults())`를 포함해 공급자 구성 엔드포인트가 활성화되어 있는지 확인하세요 ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)). 그렇지 않으면 APIM의 `<openid-config>` 호출이 404 오류를 반환합니다.

- **Audience 클레임:** Spring 기본 동작은 `aud` 클레임을 클라이언트 ID로 설정합니다. APIM의 `<audience>` 검증이 실패하면 토큰을 커스터마이징하거나 APIM 정책을 조정해야 할 수 있습니다. JWT 내 audience가 `<audience>` 설정과 일치하는지 반드시 확인하세요.

- **JSON 메타데이터 파싱:** OpenID 구성 JSON은 유효해야 합니다. Spring 기본 설정은 표준 OIDC 메타데이터 문서를 생성합니다. `issuer`와 `jwks_uri`가 올바른지 확인하세요. Spring을 프록시 뒤나 경로 기반 라우팅으로 호스팅하는 경우, 메타데이터 내 URL을 꼼꼼히 점검해야 합니다. APIM은 이 값을 그대로 사용합니다.

- **정책 순서:** APIM 정책에서 `<validate-jwt>`는 백엔드 라우팅 전에 위치해야 합니다. 그렇지 않으면 유효하지 않은 토큰으로 앱에 호출이 도달할 수 있습니다. 또한 `<validate-jwt>`는 `<inbound>` 바로 아래에 위치해야 하며, 다른 조건문 안에 중첩되지 않아야 APIM이 제대로 적용합니다.

위 단계를 따르면 Spring AI MCP 서버를 Azure Container Apps에서 실행하고, Azure API Management가 최소한의 정책으로 들어오는 OAuth2 JWT를 검증하도록 할 수 있습니다. 핵심은 Spring 인증 서버 엔드포인트를 TLS로 공개하고, OIDC 디스커버리를 활성화하며, APIM의 `validate-jwt`가 OpenID 구성 URL을 참조하도록 설정하는 것입니다. 이 구성은 개발/테스트 환경에 적합하며, 운영 환경에서는 적절한 시크릿 관리, 토큰 수명, JWKS 키 교체 등을 고려하세요.
**참고 자료:** 기본 엔드포인트에 대해서는 Spring Authorization Server 문서([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize))와 OIDC 구성([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build))를 참고하세요; `validate-jwt` 예제는 Microsoft APIM 문서([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation))를 참고하시고, 배포 및 인증서 관련 내용은 Azure Container Apps 문서([Deploy Java Spring Boot apps to Azure Container Apps - Java on Azure | Microsoft Learn](https://learn.microsoft.com/en-us/azure/developer/java/identity/deploy-spring-boot-to-azure-container-apps#:~:text=Now%20you%20can%20deploy%20your,CLI%20command)) ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements))를 참고하세요.

**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 노력하고 있으나, 자동 번역에는 오류나 부정확한 부분이 있을 수 있음을 유의하시기 바랍니다. 원문은 해당 언어의 원본 문서가 권위 있는 자료로 간주되어야 합니다. 중요한 정보의 경우 전문적인 인간 번역을 권장합니다. 본 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.