# Spring AI MCP 앱을 Azure Container Apps에 배포하기

> [!WARNING]
> 이 결합된 권한 부여/리소스 서버는 학습 및 개발/테스트 용도로 설계되었습니다. 프로덕션 시스템에서는 전용 ID 공급자, 영구 서명 키 및 관리되는 비밀 저장소에 저장된 자격 증명을 사용해야 합니다.
> 




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

이는 HTTPS가 활성화된 공개 접근 가능한 Container App을 생성합니다(Azure는 기본 `*.azurecontainerapps.io` 도메인에 대해 무료 TLS 인증서를 발급합니다 ([Azure Container Apps의 사용자 지정 도메인 이름 및 무료 관리 인증서 | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements))). 명령 출력에는 앱의 FQDN(예: `my-mcp-app.eastus.azurecontainerapps.io`)이 포함되며, 이는 <strong>issuer URL</strong>의 기본 값이 됩니다. APIM이 앱에 접근할 수 있도록 HTTP 인그레스를 위와 같이 활성화하세요. 테스트/개발 환경에서는 `--ingress external` 옵션을 사용하거나 [Microsoft 문서](https://learn.microsoft.com/azure/container-apps/custom-domains-managed-certificates)처럼 TLS가 적용된 사용자 지정 도메인을 바인딩할 수 있습니다 ([Azure Container Apps의 사용자 지정 도메인 이름 및 무료 관리 인증서 | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)). OAuth 클라이언트 시크릿과 같은 민감한 속성은 Container Apps 비밀 또는 Azure Key Vault에 저장하고 컨테이너 환경 변수로 매핑하세요.

## Spring Authorization Server 구성

Spring Boot 앱 코드에 Spring Authorization Server 및 Resource Server 스타터를 포함하세요. `RegisteredClient`를 구성하고(dev/test 용 `client_credentials` 그랜트) JWT 키 소스를 설정하세요. 예를 들어, `application.properties`에서 다음과 같이 설정할 수 있습니다:

```properties
# OAuth2 client (for testing token issuance)
demo.oauth.client-id=${OAUTH_CLIENT_ID:mcp-client}
demo.oauth.client-secret=${OAUTH_CLIENT_SECRET}
```

보안 필터 체인을 정의하여 Authorization Server와 Resource Server를 활성화하세요. 예를 들어:

```java
@Configuration
@EnableWebSecurity
public class SecurityConfiguration {

    @Bean
    SecurityFilterChain securityFilterChain(HttpSecurity http) throws Exception {
        OAuth2AuthorizationServerConfigurer<HttpSecurity> authzServer = OAuth2AuthorizationServerConfigurer.authorizationServer();
        http
            .authorizeHttpRequests(auth -> auth.anyRequest().authenticated())
            // 인증 서버 엔드포인트 활성화
            .apply(authzServer.and())
            // 리소스 서버 활성화 (들어오는 요청에 대해 JWT 검증)
            .oauth2ResourceServer(oauth2 -> oauth2.jwt(withDefaults()))
            // CSRF 비활성화 (MCP 서버는 브라우저 기반이 아님)
            .csrf(csrf -> csrf.disable())
            // 클라이언트 데모 도구에 대해 CORS 허용
            .cors(withDefaults());
        return http.build();
    }

    // 인메모리 클라이언트(RegisteredClient) 및 JWK 소스 정의:
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
        // RSA 키 생성 (개발/테스트용, 시작 시 새로 생성)
        RSAKey rsaKey = new RSAKeyGenerator(2048).keyID("1").generate();
        JWKSet jwkSet = new JWKSet(rsaKey);
        return (selector, context) -> selector.select(jwkSet);
    }
}
```

이 설정은 기본 OAuth2 엔드포인트(`/oauth2/token` 및 `/oauth2/jwks`)를 노출합니다. (기본적으로 Spring의 `AuthorizationServerSettings`는 `/oauth2/token` 및 `/oauth2/jwks`에 매핑됩니다 ([Spring Authorization Server 구성 모델](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)).) 서버는 위에서 설정한 RSA 키로 서명된 JWT 액세스 토큰을 발급하며, 공개 키는 `https://<your-app>:/oauth2/jwks`에서 공개됩니다.

**OpenID Connect 검색 활성화:** APIM이 발급자 및 JWKS를 자동으로 검색하도록 하려면 보안 구성에 `.oidc(Customizer.withDefaults())`를 추가하여 OIDC 공급자 구성 엔드포인트를 활성화하세요 ([Spring Authorization Server 구성 모델](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)). 예를 들어:

```java
http
  .apply(authzServer.and())
  .securityMatcher(authzServer.getEndpointsMatcher())
  .with(authzServer, authz -> authz
      .oidc(Customizer.withDefaults()));  // <– /.well-known/openid-configuration를 활성화합니다
```

이 설정으로 `/.well-known/openid-configuration`이 노출되어 APIM이 메타데이터를 사용할 수 있습니다. 마지막으로 JWT **audience** 클레임을 APIM의 `<audiences>` 검증에 맞게 사용자 지정하려면 토큰 커스터마이저를 추가하세요:

```java
@Bean
public OAuth2TokenCustomizer<OAuth2TokenClaimsContext> tokenCustomizer() {
    return context -> {
        // 맞춤 잠재고객 설정(예: 클라이언트 ID 또는 API 식별자)
        context.getClaims().audience(Collections.singletonList("mcp-client"));
    };
}
```

이로써 토큰에 `"aud": ["mcp-client"]`가 포함되어 APIM이 예상하는 클라이언트 ID 또는 범위와 일치합니다.

## 토큰 및 JWKS 엔드포인트 노출

배포 후 앱의 <strong>issuer URL</strong>은 `https://<app-fqdn>`, 예: `https://my-mcp-app.eastus.azurecontainerapps.io`가 됩니다. OAuth2 엔드포인트는 다음과 같습니다:

- **토큰 엔드포인트:** `https://<app-fqdn>/oauth2/token` – 클라이언트가 토큰을 얻는 곳 (`client_credentials` 흐름).
- **JWKS 엔드포인트:** `https://<app-fqdn>/oauth2/jwks` – JWK 집합 반환 (APIM이 서명 키를 얻는 데 사용).
- **OpenID 구성:** `https://<app-fqdn>/.well-known/openid-configuration` – OIDC 검색 JSON(여기에 `issuer`, `token_endpoint`, `jwks_uri` 등 포함).  

APIM은 <strong>OpenID 구성 URL</strong>을 참조하여 `jwks_uri`를 검색합니다. 예를 들어 Container App FQDN이 `my-mcp-app.eastus.azurecontainerapps.io`라면 APIM의 `<openid-config url="...">`는 `https://my-mcp-app.eastus.azurecontainerapps.io/.well-known/openid-configuration`이어야 합니다. (기본적으로 Spring은 해당 메타데이터에서 `issuer`를 동일한 기본 URL로 설정합니다 ([Spring Authorization Server 구성 모델](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)).)

## Azure API Management (`validate-jwt`) 구성

Azure APIM에서 인바운드 정책에 `<validate-jwt>` 정책을 추가하여 들어오는 JWT를 Spring Authorization Server에 대해 검사하세요. 간단한 설정은 OpenID Connect 메타데이터 URL을 사용할 수 있습니다. 정책 예제:

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

이 정책은 APIM에 Spring 인증 서버에서 OpenID 구성을 가져오고 JWKS를 검색하며, 각 토큰이 신뢰할 수 있는 키로 서명되었는지 및 올바른 audience를 갖는지 검증하도록 지시합니다. (`<issuers>`를 생략하면 APIM은 메타데이터의 `issuer` 클레임을 자동으로 사용합니다.) `<audience>`는 토큰의 클라이언트 ID 또는 API 리소스 식별자와 일치해야 하는데 (위 예제에서는 `"mcp-client"`로 설정됐습니다), 이는 Microsoft 문서에서 `<openid-config>`와 함께 `validate-jwt`를 사용하는 방법과 일치합니다 ([Azure API Management 정책 참조 - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)).

검증 후 APIM은 원본 `Authorization` 헤더를 포함하여 요청을 백엔드로 전달합니다. Spring 앱도 리소스 서버이기 때문에 토큰을 재검증하지만 APIM이 이미 유효성을 보장했습니다. (개발 중에는 APIM 검사만 신뢰하고 앱 내 추가 검증을 비활성화할 수 있지만, 두 검증을 모두 유지하는 것이 더 안전합니다.)

## 예시 설정

| 설정               | 예시 값                                                              | 참고                                       |
|--------------------|----------------------------------------------------------------------|--------------------------------------------|
| **Issuer**         | `https://my-mcp-app.eastus.azurecontainerapps.io`                    | Container App의 URL (기본 URI)             |
| **토큰 엔드포인트**| `https://my-mcp-app.eastus.azurecontainerapps.io/oauth2/token`       | 기본 Spring 토큰 엔드포인트 ([Spring Authorization Server 구성 모델](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize))  |
| **JWKS 엔드포인트**| `https://my-mcp-app.eastus.azurecontainerapps.io/oauth2/jwks`        | 기본 JWK 집합 엔드포인트 ([Spring Authorization Server 구성 모델](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize))   |
| **OpenID 구성**    | `https://my-mcp-app.eastus.azurecontainerapps.io/.well-known/openid-configuration` | OIDC 검색 문서 (자동 생성)                 |
| **APIM audience**  | `mcp-client`                                                         | OAuth 클라이언트 ID 또는 API 리소스 이름   |
| **APIM 정책**      | `<openid-config url="https://.../.well-known/openid-configuration" />` | `<validate-jwt>`가 이 URL을 사용 ([Azure API Management 정책 참조 - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)) |

## 일반적인 주의사항

- **HTTPS/TLS:** APIM 게이트웨이는 OpenID/JWKS 엔드포인트가 유효한 인증서가 적용된 HTTPS여야 합니다. 기본적으로 Azure Container Apps는 Azure 관리 도메인에 대해 신뢰할 수 있는 TLS 인증서를 제공합니다 ([Azure Container Apps의 사용자 지정 도메인 이름 및 무료 관리 인증서 | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)). 사용자 지정 도메인을 사용하는 경우 인증서를 바인딩해야 합니다(무료 관리 인증서 기능을 사용할 수 있음) ([Azure Container Apps의 사용자 지정 도메인 이름 및 무료 관리 인증서 | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)). APIM이 엔드포인트 인증서를 신뢰하지 못하면 `<validate-jwt>`가 메타데이터를 가져오지 못합니다.

- **엔드포인트 접근성:** Spring 앱의 엔드포인트가 APIM에서 접근 가능해야 합니다. `--ingress external`을 사용하거나 포털에서 인그레스를 활성화하는 것이 가장 쉽습니다. 내부 또는 가상 네트워크에 바인딩된 환경을 선택한 경우 APIM(기본적으로 공개)은 동일 가상 네트워크 내에 있어야 접근할 수 있습니다. 테스트 환경에는 공개 인그레스를 권장하여 APIM이 `.well-known` 및 `/jwks` URL에 접근할 수 있도록 하세요.

- **OpenID 검색 활성화:** 기본적으로 Spring Authorization Server는 OIDC가 활성화되지 않으면 `/.well-known/openid-configuration`을 **노출하지 않습니다**. 보안 구성에 `.oidc(Customizer.withDefaults())`를 포함하여 공급자 구성 엔드포인트가 활성화되었는지 확인하세요(위 참조). 그렇지 않으면 APIM의 `<openid-config>` 호출이 404를 반환합니다.

- **Audience 클레임:** Spring의 기본 동작은 `aud` 클레임을 클라이언트 ID로 설정합니다. APIM의 `<audience>` 검증이 실패하면 위에 보여준 것처럼 토큰을 사용자 지정하거나 APIM 정책을 조정해야 할 수 있습니다. JWT의 audience가 `<audience>` 설정과 일치하는지 확인하세요.

- **JSON 메타데이터 구문 분석:** OpenID 구성 JSON은 유효해야 합니다. Spring 기본 구성은 표준 OIDC 메타데이터 문서를 출력합니다. 올바른 `issuer` 및 `jwks_uri`가 포함됐는지 확인하세요. 프록시나 경로 기반 라우트 뒤에서 Spring을 호스팅하는 경우 이 메타데이터 내 URL을 재확인하세요. APIM은 해당 값을 그대로 사용합니다.

- **정책 순서:** APIM 정책에서 `<validate-jwt>`는 백엔드로 라우팅하기 <strong>전</strong>에 위치해야 합니다. 그렇지 않으면 유효한 토큰 없이 호출이 앱에 도달할 수 있습니다. 또한 `<validate-jwt>`는 다른 조건 안에 중첩하지 말고 `<inbound>` 바로 아래에 위치해야 APIM이 이를 적용합니다.

위 단계를 따르면 Azure Container Apps에서 Spring AI MCP 서버를 실행하고 Azure API Management가 최소한의 정책으로 들어오는 OAuth2 JWT를 검증할 수 있습니다. 핵심은 Spring 인증 엔드포인트를 TLS로 공개하고 OIDC 검색을 활성화하며, APIM `validate-jwt`가 OpenID 구성 URL을 가리키게 하여 JWKS를 자동으로 가져오도록 하는 것입니다. 이 설정은 개발/테스트 환경에 적합하며, 프로덕션에서는 적절한 비밀 관리, 토큰 수명, 그리고 필요에 따라 JWKS 키 순환을 고려하세요.


**참고자료:** 기본 엔드포인트에 대해서는 Spring Authorization Server 문서([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize))와 OIDC 구성([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)); `validate-jwt` 예제에 대해서는 Microsoft APIM 문서([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)); 배포 및 인증서 관련해서는 Azure Container Apps 문서([Deploy Java Spring Boot apps to Azure Container Apps - Java on Azure | Microsoft Learn](https://learn.microsoft.com/en-us/azure/developer/java/identity/deploy-spring-boot-to-azure-container-apps#:~:text=Now%20you%20can%20deploy%20your,CLI%20command)) ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements))를 참고하세요.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**면책 조항**:
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 기하기 위해 노력하고 있으나, 자동 번역은 오류나 부정확한 부분이 있을 수 있음을 유의하시기 바랍니다. 원본 문서의 원어본이 권위 있는 자료로 간주되어야 합니다. 중요한 정보의 경우, 전문가의 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->