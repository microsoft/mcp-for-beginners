# Spring AI MCP Uygulamasını Azure Container Apps’e Dağıtma

([Spring AI MCP sunucularını OAuth2 ile güvence altına alma](https://spring.io/blog/2025/04/02/mcp-server-oauth2)) *Şekil: Spring Authorization Server ile güvence altına alınmış Spring AI MCP sunucusu. Sunucu, istemcilere erişim tokenları verir ve gelen isteklerde bunları doğrular (kaynak: Spring blog) ([Spring AI MCP sunucularını OAuth2 ile güvence altına alma](https://spring.io/blog/2025/04/02/mcp-server-oauth2#:~:text=,server%20with%20the%20MCP%20inspector)).* Spring MCP sunucusunu dağıtmak için, onu bir konteyner olarak oluşturun ve Azure Container Apps’i dış erişim ile kullanın. Örneğin, Azure CLI ile şu komutu çalıştırabilirsiniz:

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

Bu, HTTPS etkinleştirilmiş ve genel erişime açık bir Container App oluşturur (Azure, varsayılan `*.azurecontainerapps.io` alan adı için ücretsiz bir TLS sertifikası sağlar ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements))). Komut çıktısı, uygulamanın FQDN’sini (örneğin `my-mcp-app.eastus.azurecontainerapps.io`) içerir ve bu, **issuer URL** tabanı olur. APIM’in uygulamaya erişebilmesi için HTTP ingress’in etkin olduğundan emin olun (yukarıdaki gibi). Test/geliştirme ortamında `--ingress external` seçeneğini kullanın (veya [Microsoft dokümanlarına](https://learn.microsoft.com/azure/container-apps/custom-domains-managed-certificates) göre TLS ile özel bir alan adı bağlayın ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements))). Herhangi bir hassas özelliği (OAuth istemci gizli anahtarları gibi) Container Apps secrets veya Azure Key Vault içinde saklayın ve bunları konteynere ortam değişkenleri olarak eşleyin.

## Spring Authorization Server’ı Yapılandırma

Spring Boot uygulamanızın kodunda, Spring Authorization Server ve Resource Server starter’larını dahil edin. Bir `RegisteredClient` yapılandırın (geliştirme/test ortamında `client_credentials` grant için) ve bir JWT anahtar kaynağı belirleyin. Örneğin, `application.properties` içinde şu ayarları yapabilirsiniz:

```properties
# OAuth2 client (for testing token issuance)
spring.security.oauth2.authorizationserver.client.oidc-client.registration.client-id=mcp-client
spring.security.oauth2.authorizationserver.client.oidc-client.registration.client-secret={noop}secret
spring.security.oauth2.authorizationserver.client.oidc-client.registration.authorization-grant-types=client_credentials
spring.security.oauth2.authorizationserver.client.oidc-client.registration.client-authentication-methods=client_secret_basic
```

Authorization Server ve Resource Server’ı etkinleştirmek için bir güvenlik filtre zinciri tanımlayın. Örnek:

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

Bu yapılandırma, varsayılan OAuth2 uç noktalarını açığa çıkarır: tokenlar için `/oauth2/token` ve JSON Web Key Set için `/oauth2/jwks`. (Spring’in `AuthorizationServerSettings` varsayılan olarak `/oauth2/token` ve `/oauth2/jwks` adreslerini eşler ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)).) Sunucu, yukarıdaki RSA anahtarıyla imzalanmış JWT erişim tokenları verir ve genel anahtarını `https://<your-app>:/oauth2/jwks` adresinde yayınlar.

**OpenID Connect keşfini etkinleştirin:** APIM’in issuer ve JWKS bilgilerini otomatik alabilmesi için, güvenlik yapılandırmanıza `.oidc(Customizer.withDefaults())` ekleyerek OIDC sağlayıcı yapılandırma uç noktasını etkinleştirin ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)). Örnek:

```java
http
  .apply(authzServer.and())
  .securityMatcher(authzServer.getEndpointsMatcher())
  .with(authzServer, authz -> authz
      .oidc(Customizer.withDefaults()));  // <– enables /.well-known/openid-configuration
```

Bu, APIM’in metadata için kullanabileceği `/.well-known/openid-configuration` yolunu açar. Son olarak, JWT **audience** (hedef kitle) claim’ini APIM’in `<audiences>` kontrolünden geçecek şekilde özelleştirmek isteyebilirsiniz. Örneğin, bir token özelleştiricisi ekleyin:

```java
@Bean
public OAuth2TokenCustomizer<OAuth2TokenClaimsContext> tokenCustomizer() {
    return context -> {
        // Set a custom audience (e.g. the client ID or API identifier)
        context.getClaims().audience(Collections.singletonList("mcp-client"));
    };
}
```

Bu, tokenların `"aud": ["mcp-client"]` içermesini sağlar; bu, APIM’in beklediği istemci kimliği veya kapsam ile eşleşir.

## Token ve JWKS Uç Noktalarını Açığa Çıkarma

Dağıtımdan sonra, uygulamanızın **issuer URL**’si `https://<app-fqdn>` olacaktır, örneğin `https://my-mcp-app.eastus.azurecontainerapps.io`. OAuth2 uç noktaları şunlardır:

- **Token uç noktası:** `https://<app-fqdn>/oauth2/token` – istemciler tokenları buradan alır (client_credentials akışı).
- **JWKS uç noktası:** `https://<app-fqdn>/oauth2/jwks` – JWK setini döner (APIM, imzalama anahtarlarını almak için kullanır).
- **OpenID Konfigürasyonu:** `https://<app-fqdn>/.well-known/openid-configuration` – OIDC keşif JSON’u (içinde `issuer`, `token_endpoint`, `jwks_uri` vb. bulunur).

APIM, `jwks_uri`’yi keşfetmek için **OpenID konfigürasyon URL’sine** işaret eder. Örneğin, Container App FQDN’niz `my-mcp-app.eastus.azurecontainerapps.io` ise, APIM’in `<openid-config url="...">` değeri `https://my-mcp-app.eastus.azurecontainerapps.io/.well-known/openid-configuration` olmalıdır. (Spring varsayılan olarak metadata içindeki `issuer` değerini aynı temel URL olarak ayarlar ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)).)

## Azure API Management’ı (`validate-jwt`) Yapılandırma

Azure APIM’de, gelen JWT’leri Spring Authorization Server’a karşı doğrulamak için `<validate-jwt>` politikasını kullanan bir inbound policy ekleyin. Basit bir yapılandırma için OpenID Connect metadata URL’sini kullanabilirsiniz. Örnek politika parçası:

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

Bu politika, APIM’in Spring Auth Server’dan OpenID konfigürasyonunu almasını, JWKS’yi çekmesini ve her tokenın güvenilir bir anahtarla imzalandığını ve doğru audience’a sahip olduğunu doğrulamasını sağlar. (`<issuers>` atlanırsa, APIM metadata içindeki `issuer` claim’ini otomatik kullanır.) `<audience>`, token içindeki istemci kimliği veya API kaynak tanımlayıcısı ile eşleşmelidir (yukarıdaki örnekte `"mcp-client"` olarak ayarlanmıştır). Bu, Microsoft’un `<openid-config>` ile `validate-jwt` kullanımı dokümanıyla uyumludur ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)).

Doğrulamadan sonra, APIM isteği (orijinal `Authorization` başlığı dahil) backend’e iletir. Spring uygulaması da bir resource server olduğundan tokenı yeniden doğrular, ancak APIM zaten geçerliliğini sağlamıştır. (Geliştirme için, APIM’in doğrulamasına güvenip uygulamadaki ek kontrolleri devre dışı bırakabilirsiniz, ancak her ikisini de açık tutmak daha güvenlidir.)

## Örnek Ayarlar

| Ayar               | Örnek Değer                                                        | Notlar                                      |
|--------------------|-------------------------------------------------------------------|---------------------------------------------|
| **Issuer**         | `https://my-mcp-app.eastus.azurecontainerapps.io`                 | Container App’in URL’si (temel URI)          |
| **Token uç noktası** | `https://my-mcp-app.eastus.azurecontainerapps.io/oauth2/token`    | Varsayılan Spring token uç noktası ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize))  |
| **JWKS uç noktası**  | `https://my-mcp-app.eastus.azurecontainerapps.io/oauth2/jwks`     | Varsayılan JWK Set uç noktası ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize))    |
| **OpenID Konfig.**  | `https://my-mcp-app.eastus.azurecontainerapps.io/.well-known/openid-configuration` | OIDC keşif dokümanı (otomatik oluşturulur)  |
| **APIM audience**   | `mcp-client`                                                      | OAuth istemci kimliği veya API kaynak adı   |
| **APIM politikası** | `<openid-config url="https://.../.well-known/openid-configuration" />` | `<validate-jwt>` bu URL’yi kullanır ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)) |

## Yaygın Hatalar

- **HTTPS/TLS:** APIM geçidi, OpenID/JWKS uç noktasının geçerli sertifikalı HTTPS olması gerekir. Azure Container Apps, Azure tarafından yönetilen alan adı için varsayılan olarak güvenilir bir TLS sertifikası sağlar ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)). Özel alan adı kullanıyorsanız, bir sertifika bağladığınızdan emin olun (Azure’nun ücretsiz yönetilen sertifika özelliğini kullanabilirsiniz) ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)). APIM uç noktasının sertifikasına güvenemezse, `<validate-jwt>` metadata’yı alamaz.

- **Uç Nokta Erişilebilirliği:** Spring uygulamasının uç noktalarının APIM’den erişilebilir olduğundan emin olun. `--ingress external` kullanmak (veya portalda ingress’i etkinleştirmek) en kolay yoldur. İç veya vNet’e bağlı bir ortam seçtiyseniz, APIM (varsayılan olarak genel) ona erişemeyebilir; aynı VNet içinde olması gerekir. Test ortamında, APIM’in `.well-known` ve `/jwks` URL’lerini çağırabilmesi için genel ingress tercih edin.

- **OpenID Keşfi Etkin:** Spring Authorization Server varsayılan olarak `/.well-known/openid-configuration`’ı **açığa çıkarmaz**; OIDC etkin değilse görünmez. Sağlayıcı yapılandırma uç noktasını aktif etmek için güvenlik konfigürasyonunuza `.oidc(Customizer.withDefaults())` ekleyin (yukarıya bakınız) ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)). Aksi takdirde APIM’in `<openid-config>` çağrısı 404 döner.

- **Audience Claim:** Spring varsayılan olarak `aud` claim’ini istemci kimliği olarak ayarlar. APIM’in `<audience>` kontrolü başarısız olursa, tokenı özelleştirmeniz (yukarıdaki gibi) veya APIM politikasını ayarlamanız gerekebilir. JWT içindeki audience, `<audience>` ile eşleşmelidir.

- **JSON Metadata Ayrıştırma:** OpenID konfigürasyon JSON’u geçerli olmalıdır. Spring varsayılan yapılandırması standart bir OIDC metadata dokümanı üretir. İçinde doğru `issuer` ve `jwks_uri` olduğundan emin olun. Spring’i proxy veya yol tabanlı yönlendirme arkasında barındırıyorsanız, bu metadata içindeki URL’leri kontrol edin. APIM bu değerleri olduğu gibi kullanır.

- **Politika Sıralaması:** APIM politikasında `<validate-jwt>` öğesini backend’e yönlendirmeden **önce** yerleştirin. Aksi halde, geçerli token olmadan istekler uygulamaya ulaşabilir. Ayrıca `<validate-jwt>`’nin `<inbound>` altında hemen bulunmasına dikkat edin (başka bir koşulun içinde olmamalı) ki APIM bunu uygulasın.

Yukarıdaki adımları takip ederek, Spring AI MCP sunucunuzu Azure Container Apps üzerinde çalıştırabilir ve Azure API Management ile gelen OAuth2 JWT’lerini minimal bir politika ile doğrulayabilirsiniz. Temel noktalar: Spring Auth uç noktalarını TLS ile genel erişime açmak, OIDC keşfini etkinleştirmek ve APIM’in `validate-jwt` politikasını OpenID konfigürasyon URL’sine yönlendirmek (böylece JWKS otomatik alınır). Bu yapılandırma geliştirme/test ortamları için uygundur; üretim için uygun gizli yönetimi, token ömürleri ve JWKS anahtar döndürme işlemlerini göz önünde bulundurun.
**Referanslar:** Varsayılan uç noktalar için Spring Authorization Server belgelerine bakınız ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)) ve OIDC yapılandırması için ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)); `validate-jwt` örnekleri için Microsoft APIM belgelerine bakınız ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)); ve dağıtım ile sertifikalar için Azure Container Apps belgelerine göz atınız ([Deploy Java Spring Boot apps to Azure Container Apps - Java on Azure | Microsoft Learn](https://learn.microsoft.com/en-us/azure/developer/java/identity/deploy-spring-boot-to-azure-container-apps#:~:text=Now%20you%20can%20deploy%20your,CLI%20command)) ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)).

**Feragatname**:  
Bu belge, AI çeviri servisi [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hatalar veya yanlışlıklar içerebileceğini lütfen unutmayınız. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu oluşabilecek yanlış anlamalar veya yorum hatalarından sorumlu değiliz.