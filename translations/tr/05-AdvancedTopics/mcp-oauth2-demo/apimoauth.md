# Spring AI MCP Uygulamasını Azure Container Apps'e Dağıtma

> [!WARNING]
> Bu birleşik yetkilendirme/kaynak sunucusu öğrenme ve geliştirme/test amaçlıdır.
> Üretim sistemleri ayrı bir kimlik sağlayıcısı,
> kalıcı imzalama anahtarları ve yönetilen gizli depolarda saklanan kimlik bilgileri kullanmalıdır.

 ([Spring AI MCP sunucularını OAuth2 ile güvence altına alma](https://spring.io/blog/2025/04/02/mcp-server-oauth2)) *Şekil: Spring Yetkilendirme Sunucusu ile güvence altına alınmış Spring AI MCP sunucusu. Sunucu erişim belirteçlerini istemcilere verir ve gelen isteklere bunları doğrular (kaynak: Spring blog) ([Spring AI MCP sunucularını OAuth2 ile güvence altına alma](https://spring.io/blog/2025/04/02/mcp-server-oauth2#:~:text=,server%20with%20the%20MCP%20inspector)).* Spring MCP sunucusunu dağıtmak için, onu bir konteyner olarak oluşturun ve dış giriş ile Azure Container Apps kullanın. Örneğin, Azure CLI ile şu komutu çalıştırabilirsiniz:

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

Bu, HTTPS etkinleştirilmiş ve herkese açık erişimli bir Container App oluşturur (Azure, varsayılan `*.azurecontainerapps.io` alan adı için ücretsiz bir TLS sertifikası verir ([Azure Container Apps'de özel alan adları ve ücretsiz yönetilen sertifikalar | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements))). Komut çıktısı, uygulamanın FQDN'sini (örneğin `my-mcp-app.eastus.azurecontainerapps.io`) içerir ve bu **issuer URL** tabanı olur. APIM’nin uygulamaya ulaşabilmesi için HTTP girişi etkinleştirdiğinizden emin olun (yukarıdaki gibi). Test/geliştirme ortamında, `--ingress external` seçeneğini kullanın (veya bir özel alan adını TLS ile bağlayın, bkz. [Microsoft belgeleri](https://learn.microsoft.com/azure/container-apps/custom-domains-managed-certificates) ([Azure Container Apps'de özel alan adları ve ücretsiz yönetilen sertifikalar | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements))). Hassas özellikleri (OAuth istemci gizli anahtarları gibi) Container Apps gizli anahtarlarına veya Azure Key Vault'a kaydedin ve konteynere ortam değişkenleri olarak eşleyin.

## Spring Yetkilendirme Sunucusunu Yapılandırma

Spring Boot uygulamanızın kodunda, Spring Yetkilendirme Sunucusu ve Kaynak Sunucusu başlangıçlarını dahil edin. `RegisteredClient` (geliştirme/test için `client_credentials` grant) ve bir JWT anahtar kaynağı yapılandırın. Örneğin, `application.properties` dosyasında şu ayarları yapabilirsiniz:

```properties
# OAuth2 client (for testing token issuance)
demo.oauth.client-id=${OAUTH_CLIENT_ID:mcp-client}
demo.oauth.client-secret=${OAUTH_CLIENT_SECRET}
```

Yetkilendirme Sunucusunu ve Kaynak Sunucusunu bir güvenlik filtre zinciri tanımlayarak etkinleştirin. Örneğin:

```java
@Configuration
@EnableWebSecurity
public class SecurityConfiguration {

    @Bean
    SecurityFilterChain securityFilterChain(HttpSecurity http) throws Exception {
        OAuth2AuthorizationServerConfigurer<HttpSecurity> authzServer = OAuth2AuthorizationServerConfigurer.authorizationServer();
        http
            .authorizeHttpRequests(auth -> auth.anyRequest().authenticated())
            // Yetkilendirme Sunucusu uç noktalarını etkinleştir
            .apply(authzServer.and())
            // Kaynak Sunucusunu etkinleştir (gelen isteklerde JWT doğrulaması yap)
            .oauth2ResourceServer(oauth2 -> oauth2.jwt(withDefaults()))
            // CSRF'yi devre dışı bırak (MCP sunucusu tarayıcı tabanlı değildir)
            .csrf(csrf -> csrf.disable())
            // İstemci demo araçları için CORS'a izin ver
            .cors(withDefaults());
        return http.build();
    }

    // Bir bellek içi istemci (RegisteredClient) ve bir JWK kaynağı tanımla:
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
        // Bir RSA anahtarı oluştur (geliştirme/test için, her başlatmada yenisini oluştur)
        RSAKey rsaKey = new RSAKeyGenerator(2048).keyID("1").generate();
        JWKSet jwkSet = new JWKSet(rsaKey);
        return (selector, context) -> selector.select(jwkSet);
    }
}
```

Bu yapılandırma varsayılan OAuth2 uç noktalarını açığa çıkarır: jetonlar için `/oauth2/token` ve JSON Web Anahtar Seti için `/oauth2/jwks`. (Varsayılan olarak Spring’in `AuthorizationServerSettings` `/oauth2/token` ve `/oauth2/jwks` adreslerini eşler ([Yapılandırma Modeli :: Spring Yetkilendirme Sunucusu](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)).) Sunucu, yukarıdaki RSA anahtarıyla imzalanmış JWT erişim belirteçleri verir ve genel anahtarını `https://<uygulamanız>:/oauth2/jwks` adresinde yayınlar.

**OpenID Connect keşfini etkinleştirin:** APIM’in issuer ve JWKS’yi otomatik almasını sağlamak için, güvenlik yapılandırmanızda `.oidc(Customizer.withDefaults())` ekleyerek OIDC sağlayıcı yapılandırma uç noktasını etkinleştirin ([Yapılandırma Modeli :: Spring Yetkilendirme Sunucusu](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)). Örneğin:

```java
http
  .apply(authzServer.and())
  .securityMatcher(authzServer.getEndpointsMatcher())
  .with(authzServer, authz -> authz
      .oidc(Customizer.withDefaults()));  // <– /.well-known/openid-configuration için etkinleştirir
```

Bu, APIM’in meta verileri için kullanabileceği `/.well-known/openid-configuration` adresini açığa çıkarır. Son olarak, JWT **audience** (hedef kitle) alanını APIM’in `<audiences>` kontrolünden geçmesi için özelleştirebilirsiniz. Örnek olarak bir token özelleştirici ekleyin:

```java
@Bean
public OAuth2TokenCustomizer<OAuth2TokenClaimsContext> tokenCustomizer() {
    return context -> {
        // Özel bir hedef kitle belirleyin (ör. müşteri kimliği veya API tanımlayıcısı)
        context.getClaims().audience(Collections.singletonList("mcp-client"));
    };
}
```

Bu, belirteçlerin `"aud": ["mcp-client"]` içermesini sağlar ve APIM’in beklediği istemci kimliği veya kapsamla eşleşir.

## Jeton ve JWKS Uç Noktalarını Açığa Çıkarma

Dağıtım sonrası, uygulamanızın **issuer URL**’si `https://<uygulama-fqdn>` olacaktır, örneğin `https://my-mcp-app.eastus.azurecontainerapps.io`. OAuth2 uç noktaları:

- **Jeton uç noktası:** `https://<uygulama-fqdn>/oauth2/token` – istemciler buradan jeton alır (client_credentials akışı).
- **JWKS uç noktası:** `https://<uygulama-fqdn>/oauth2/jwks` – JWK setini döndürür (APIM imzalama anahtarlarını bu uç noktadan alır).
- **OpenID Yapılandırma:** `https://<uygulama-fqdn>/.well-known/openid-configuration` – OIDC keşif JSON’u (içinde `issuer`, `token_endpoint`, `jwks_uri` vb. bulunur).  

APIM, `jwks_uri`yi keşfetmek için **OpenID yapılandırma URL**'sini kullanır. Örneğin, Container App’inizin FQDN’si `my-mcp-app.eastus.azurecontainerapps.io` ise, APIM’in `<openid-config url="...">` `https://my-mcp-app.eastus.azurecontainerapps.io/.well-known/openid-configuration` olmalıdır. (Spring varsayılan olarak bu meta veride `issuer` olarak aynı taban URL’yi ayarlar ([Yapılandırma Modeli :: Spring Yetkilendirme Sunucusu](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)).)

## Azure API Yönetimi'ni Yapılandırma (`validate-jwt`)

Azure APIM’de, Spring Yetkilendirme Sunucunuza karşı gelen JWT’leri doğrulamak için `<validate-jwt>` politikası kullanan bir inbound policy ekleyin. Basit bir kurulum için OpenID Connect meta veri URL’sini kullanabilirsiniz. Örnek politika parçacığı:

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

Bu politika, APIM’e Spring Yetkilendirme Sunucusundan OpenID yapılandırmasını almasını, onun JWKS’sini getirmesini ve her jetonu güvenilen anahtar tarafından imzalanmış ve doğru hedef kitleye sahip olup olmadığını doğrulamasını söyler. (`<issuers>` atlanırsa APIM otomatik olarak meta verideki `issuer` alanını kullanır.) `<audience>`, belirteç içindeki istemci kimliği veya API kaynak tanımlayıcısı ile eşleşmelidir (yukarıdaki örnekte `"mcp-client"` olarak ayarlanmıştır). Bu, Microsoft'un `validate-jwt` ile `<openid-config>` kullanımı belgeleriyle uyumludur ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)).

Doğrulama sonrası, APIM isteği (orijinal `Authorization` başlığıyla birlikte) backend’e iletir. Spring uygulaması da bir kaynak sunucusu olduğundan, jetonu tekrar doğrulayacaktır, ancak APIM zaten geçerliliğini sağlamıştır. (Geliştirme sırasında, APIM’in kontrolüne güvenebilir ve uygulamadaki ek kontrolleri devre dışı bırakabilirsiniz, ancak her ikisini de tutmak daha güvenlidir.)

## Örnek Ayarlar

| Ayar              | Örnek Değer                                                         | Notlar                                     |
|-------------------|--------------------------------------------------------------------|--------------------------------------------|
| **Issuer**        | `https://my-mcp-app.eastus.azurecontainerapps.io`                  | Container App’inizin URL’si (taban URI)    |
| **Jeton uç noktası** | `https://my-mcp-app.eastus.azurecontainerapps.io/oauth2/token`     | Varsayılan Spring jeton uç noktası ([Yapılandırma Modeli :: Spring Yetkilendirme Sunucusu](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize))  |
| **JWKS uç noktası** | `https://my-mcp-app.eastus.azurecontainerapps.io/oauth2/jwks`      | Varsayılan JWK Set uç noktası ([Yapılandırma Modeli :: Spring Yetkilendirme Sunucusu](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize))    |
| **OpenID Yapılandırması** | `https://my-mcp-app.eastus.azurecontainerapps.io/.well-known/openid-configuration` | OIDC keşif belgesi (otomatik oluşturulur)  |
| **APIM hedef kitlesi** | `mcp-client`                                                      | OAuth istemci kimliği veya API kaynak adı |
| **APIM politikası** | `<openid-config url="https://.../.well-known/openid-configuration" />` | `<validate-jwt>` bu URL’yi kullanır ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)) |

## Ortak Sorunlar

- **HTTPS/TLS:** APIM geçidi, OpenID/JWKS uç noktasının geçerli sertifikalı HTTPS olması gerekir. Varsayılan olarak, Azure Container Apps Azure tarafından yönetilen alan adı için güvenilir bir TLS sertifikası sağlar ([Azure Container Apps'de özel alan adları ve ücretsiz yönetilen sertifikalar | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)). Özel alan adı kullanıyorsanız, bir sertifika bağladığınızdan emin olun (Azure’un ücretsiz yönetilen sertifika özelliğini kullanabilirsiniz) ([Azure Container Apps'de özel alan adları ve ücretsiz yönetilen sertifikalar | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)). APIM uç noktasının sertifikasına güvenemezse, `<validate-jwt>` meta verileri getirmede başarısız olur.

- **Uç Nokta Erişilebilirliği:** Spring uygulamanızın uç noktalarının APIM’den erişilebilir olduğundan emin olun. `--ingress external` kullanmak (veya portalda girişi etkinleştirmek) en basit yoldur. Dahili veya vNet bağlı bir ortam seçerseniz, APIM (varsayılan olarak genel) aynı VNet’te değilse uygulamaya ulaşamayabilir. Test ortamında, APIM’in `.well-known` ve `/jwks` URL’lerini çağırabilmesi için genel giriş tercih edin.

- **OpenID Keşfi Etkin:** Varsayılan olarak, Spring Yetkilendirme Sunucusu `.well-known/openid-configuration` adresini **açığa çıkarmaz**; OIDC etkin değilse. Sağlayıcı yapılandırma uç noktasının etkin olması için güvenlik yapılandırmanıza `.oidc(Customizer.withDefaults())` ekleyin (bkz. yukarıdaki) ([Yapılandırma Modeli :: Spring Yetkilendirme Sunucusu](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)). Aksi takdirde APIM’in `<openid-config>` çağrısı 404 döner.

- **Audience (Hedef Kitle) Alanı:** Spring’in varsayılan davranışı, `aud` alanını istemci kimliğine ayarlamaktır. APIM’in `<audience>` kontrolü başarısız olursa, belirteci (yukarıda gösterildiği gibi) özelleştirmeniz veya APIM politikasını ayarlamanız gerekebilir. JWT’deki hedef kitlenizin `<audience>` ile eşleştiğinden emin olun.

- **JSON Meta Veri Ayrıştırma:** OpenID yapılandırma JSON’u geçerli olmalıdır. Spring’in varsayılan ayarı standart bir OIDC meta veri belgesi üretir. İçinde doğru `issuer` ve `jwks_uri` olduğundan emin olun. Spring’i proxy veya yol tabanlı bir rotanın arkasında barındırıyorsanız, bu meta verilere ait URL’leri iki kez kontrol edin. APIM bu değerleri aynen kullanır.

- **Politika Sıralaması:** APIM politikasında, `<validate-jwt>`’yi backend yönlendirmesinden **önce** yerleştirin. Aksi halde çağrılar geçerli jeton olmadan uygulamaya ulaşabilir. Ayrıca, `<validate-jwt>`’nin `<inbound>` altında (başka bir koşul içine gömülü olmadan) hemen görünmesini sağlayın.

Yukarıdaki adımları izleyerek, Spring AI MCP sunucunuzu Azure Container Apps’te çalıştırabilir ve Azure API Yönetimi’nin gelen OAuth2 JWT’lerini minimum politika ile doğrulamasını sağlayabilirsiniz. Temel noktalar: Spring Yetkilendirme uç noktalarını TLS ile genel kullanıma açmak, OIDC keşfini etkinleştirmek ve APIM’in `validate-jwt` politikası için OpenID yapılandırma URL’sini göstermek (JWKS’yi otomatik getirebilmesi için). Bu kurulum geliştirme/test ortamları içindir; üretim için uygun gizli yönetimi, jeton ömürleri ve JWKS anahtar dönüşümü gibi önlemleri değerlendirin.


**Referanslar:** Varsayılan uç noktalar için Spring Authorization Server belgelerine bakınız ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)) ve OIDC yapılandırması için ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)); `validate-jwt` örnekleri için Microsoft APIM belgelerine bakınız ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)); dağıtım ve sertifikalar için Azure Container Apps belgelerine bakınız ([Deploy Java Spring Boot apps to Azure Container Apps - Java on Azure | Microsoft Learn](https://learn.microsoft.com/en-us/azure/developer/java/identity/deploy-spring-boot-to-azure-container-apps#:~:text=Now%20you%20can%20deploy%20your,CLI%20command)) ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Feragatname**:
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba sarf etsek de, otomatik çevirilerin hata veya yanlışlık içerebileceğini lütfen unutmayınız. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu ortaya çıkabilecek yanlış anlamalardan veya yanlış yorumlamalardan sorumlu değiliz.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->