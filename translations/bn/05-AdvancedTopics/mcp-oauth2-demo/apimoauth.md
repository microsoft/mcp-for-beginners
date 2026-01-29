# Spring AI MCP অ্যাপ Azure Container Apps-এ ডিপ্লয় করা

([Securing Spring AI MCP servers with OAuth2](https://spring.io/blog/2025/04/02/mcp-server-oauth2)) *চিত্র: Spring Authorization Server দিয়ে সুরক্ষিত Spring AI MCP সার্ভার। সার্ভার ক্লায়েন্টদের কাছে অ্যাক্সেস টোকেন ইস্যু করে এবং আসা রিকোয়েস্টে সেগুলো যাচাই করে (উৎস: Spring ব্লগ) ([Securing Spring AI MCP servers with OAuth2](https://spring.io/blog/2025/04/02/mcp-server-oauth2#:~:text=,server%20with%20the%20MCP%20inspector)).* Spring MCP সার্ভার ডিপ্লয় করতে, এটিকে একটি কন্টেইনার হিসেবে তৈরি করুন এবং Azure Container Apps ব্যবহার করে এক্সটার্নাল ইনগ্রেস দিন। উদাহরণস্বরূপ, Azure CLI ব্যবহার করে আপনি চালাতে পারেন:

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

এটি একটি পাবলিকলি-অ্যাক্সেসযোগ্য Container App তৈরি করবে HTTPS সক্রিয় করে (Azure ডিফল্ট `*.azurecontainerapps.io` ডোমেইনের জন্য একটি ফ্রি TLS সার্টিফিকেট ইস্যু করে ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)))। কমান্ড আউটপুটে অ্যাপের FQDN (যেমন `my-mcp-app.eastus.azurecontainerapps.io`) থাকবে, যা **issuer URL** বেস হিসেবে ব্যবহৃত হবে। HTTP ইনগ্রেস সক্রিয় আছে কিনা নিশ্চিত করুন (উপরের মতো) যাতে APIM অ্যাপটিতে পৌঁছাতে পারে। টেস্ট/ডেভেলপমেন্ট সেটআপে, `--ingress external` অপশন ব্যবহার করুন (অথবা [Microsoft ডকুমেন্টেশন](https://learn.microsoft.com/azure/container-apps/custom-domains-managed-certificates) অনুযায়ী TLS সহ কাস্টম ডোমেইন বেঁধে দিন)। সংবেদনশীল প্রোপার্টিজ (যেমন OAuth ক্লায়েন্ট সিক্রেট) Container Apps secrets বা Azure Key Vault-এ সংরক্ষণ করুন এবং সেগুলো কন্টেইনারে এনভায়রনমেন্ট ভেরিয়েবল হিসেবে ম্যাপ করুন।

## Spring Authorization Server কনফিগারেশন

আপনার Spring Boot অ্যাপের কোডে Spring Authorization Server এবং Resource Server স্টার্টারগুলো অন্তর্ভুক্ত করুন। একটি `RegisteredClient` কনফিগার করুন (dev/test-এ `client_credentials` গ্রান্টের জন্য) এবং একটি JWT কী সোর্স সেট করুন। উদাহরণস্বরূপ, `application.properties`-এ আপনি লিখতে পারেন:

```properties
# OAuth2 client (for testing token issuance)
spring.security.oauth2.authorizationserver.client.oidc-client.registration.client-id=mcp-client
spring.security.oauth2.authorizationserver.client.oidc-client.registration.client-secret={noop}secret
spring.security.oauth2.authorizationserver.client.oidc-client.registration.authorization-grant-types=client_credentials
spring.security.oauth2.authorizationserver.client.oidc-client.registration.client-authentication-methods=client_secret_basic
```

Authorization Server এবং Resource Server সক্রিয় করতে একটি সিকিউরিটি ফিল্টার চেইন ডিফাইন করুন। উদাহরণস্বরূপ:

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

এই সেটআপ ডিফল্ট OAuth2 এন্ডপয়েন্টগুলো প্রকাশ করবে: `/oauth2/token` টোকেনের জন্য এবং `/oauth2/jwks` JSON Web Key Set-এর জন্য। (ডিফল্ট হিসেবে Spring-এর `AuthorizationServerSettings` `/oauth2/token` এবং `/oauth2/jwks` ম্যাপ করে ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize))।) সার্ভার উপরের RSA কী দিয়ে সাইন করা JWT অ্যাক্সেস টোকেন ইস্যু করবে এবং তার পাবলিক কী `https://<your-app>:/oauth2/jwks` এ প্রকাশ করবে।

**OpenID Connect ডিসকভারি সক্রিয় করুন:** APIM যাতে স্বয়ংক্রিয়ভাবে issuer এবং JWKS পেতে পারে, আপনার সিকিউরিটি কনফিগারেশনে `.oidc(Customizer.withDefaults())` যোগ করুন ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build))। উদাহরণস্বরূপ:

```java
http
  .apply(authzServer.and())
  .securityMatcher(authzServer.getEndpointsMatcher())
  .with(authzServer, authz -> authz
      .oidc(Customizer.withDefaults()));  // <– enables /.well-known/openid-configuration
```

এটি `/.well-known/openid-configuration` প্রকাশ করবে, যা APIM মেটাডেটার জন্য ব্যবহার করতে পারে। শেষ পর্যন্ত, আপনি JWT **audience** ক্লেইম কাস্টমাইজ করতে চাইতে পারেন যাতে APIM-এর `<audiences>` চেক সফল হয়। উদাহরণস্বরূপ, একটি টোকেন কাস্টমাইজার যোগ করুন:

```java
@Bean
public OAuth2TokenCustomizer<OAuth2TokenClaimsContext> tokenCustomizer() {
    return context -> {
        // Set a custom audience (e.g. the client ID or API identifier)
        context.getClaims().audience(Collections.singletonList("mcp-client"));
    };
}
```

এটি নিশ্চিত করবে টোকেনগুলো `"aud": ["mcp-client"]` বহন করে, যা APIM-এর প্রত্যাশিত ক্লায়েন্ট আইডি বা স্কোপের সাথে মেলে।

## Token এবং JWKS এন্ডপয়েন্ট প্রকাশ

ডিপ্লয় করার পর, আপনার অ্যাপের **issuer URL** হবে `https://<app-fqdn>`, যেমন `https://my-mcp-app.eastus.azurecontainerapps.io`। এর OAuth2 এন্ডপয়েন্টগুলো:

- **Token endpoint:** `https://<app-fqdn>/oauth2/token` – ক্লায়েন্টরা এখানে টোকেন পাবে (client_credentials ফ্লো)।
- **JWKS endpoint:** `https://<app-fqdn>/oauth2/jwks` – JWK সেট রিটার্ন করে (APIM সাইনিং কী পেতে ব্যবহার করে)।
- **OpenID Config:** `https://<app-fqdn>/.well-known/openid-configuration` – OIDC ডিসকভারি JSON (যাতে থাকে `issuer`, `token_endpoint`, `jwks_uri` ইত্যাদি)।

APIM **OpenID configuration URL**-এ পয়েন্ট করবে, যেখান থেকে এটি `jwks_uri` আবিষ্কার করে। উদাহরণস্বরূপ, যদি আপনার Container App FQDN হয় `my-mcp-app.eastus.azurecontainerapps.io`, তাহলে APIM-এর `<openid-config url="...">` হবে `https://my-mcp-app.eastus.azurecontainerapps.io/.well-known/openid-configuration`। (ডিফল্ট হিসেবে Spring ঐ মেটাডেটাতে একই বেস URL কে `issuer` হিসেবে সেট করে ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize))।

## Azure API Management (`validate-jwt`) কনফিগারেশন

Azure APIM-এ একটি ইনবাউন্ড পলিসি যোগ করুন যা `<validate-jwt>` পলিসি ব্যবহার করে আসা JWT গুলো Spring Authorization Server-এর বিরুদ্ধে যাচাই করবে। একটি সাধারণ সেটআপের জন্য OpenID Connect মেটাডেটা URL ব্যবহার করতে পারেন। উদাহরণ পলিসি স্নিপেট:

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

এই পলিসি APIM-কে Spring Auth Server থেকে OpenID কনফিগারেশন নিয়ে JWKS রিট্রিভ করতে বলে এবং নিশ্চিত করে প্রতিটি টোকেন একটি বিশ্বাসযোগ্য কী দিয়ে সাইন করা এবং সঠিক audience আছে। (যদি `<issuers>` বাদ দেন, APIM মেটাডেটার `issuer` ক্লেইম ব্যবহার করবে স্বয়ংক্রিয়ভাবে)। `<audience>` অবশ্যই আপনার ক্লায়েন্ট আইডি বা API রিসোর্স আইডেন্টিফায়ারের সাথে মেলে (উপরের উদাহরণে `"mcp-client"` সেট করা হয়েছে)। এটি Microsoft-এর ডকুমেন্টেশনের সাথে সামঞ্জস্যপূর্ণ ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation))।

যাচাইয়ের পর, APIM রিকোয়েস্ট (মূল `Authorization` হেডারসহ) ব্যাকএন্ডে ফরোয়ার্ড করবে। যেহেতু Spring অ্যাপও একটি রিসোর্স সার্ভার, এটি টোকেন পুনরায় যাচাই করবে, তবে APIM ইতিমধ্যে এর বৈধতা নিশ্চিত করেছে। (ডেভেলপমেন্টে, আপনি APIM-এর চেকের উপর নির্ভর করতে পারেন এবং অ্যাপে অতিরিক্ত চেক বন্ধ করতে পারেন, তবে উভয় রাখা নিরাপদ)।

## উদাহরণ সেটিংস

| সেটিং             | উদাহরণ মান                                                        | মন্তব্য                                      |
|--------------------|------------------------------------------------------------------|----------------------------------------------|
| **Issuer**         | `https://my-mcp-app.eastus.azurecontainerapps.io`                | আপনার Container App-এর URL (বেস URI)         |
| **Token endpoint** | `https://my-mcp-app.eastus.azurecontainerapps.io/oauth2/token`   | ডিফল্ট Spring টোকেন এন্ডপয়েন্ট ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize))  |
| **JWKS endpoint**  | `https://my-mcp-app.eastus.azurecontainerapps.io/oauth2/jwks`    | ডিফল্ট JWK সেট এন্ডপয়েন্ট ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize))    |
| **OpenID Config**  | `https://my-mcp-app.eastus.azurecontainerapps.io/.well-known/openid-configuration` | OIDC ডিসকভারি ডকুমেন্ট (স্বয়ংক্রিয়ভাবে তৈরি)    |
| **APIM audience**  | `mcp-client`                                                     | OAuth ক্লায়েন্ট আইডি বা API রিসোর্স নাম       |
| **APIM policy**    | `<openid-config url="https://.../.well-known/openid-configuration" />` | `<validate-jwt>` এই URL ব্যবহার করে ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)) |

## সাধারণ সমস্যা ও সমাধান

- **HTTPS/TLS:** APIM গেটওয়ে OpenID/JWKS এন্ডপয়েন্টের জন্য বৈধ সার্টিফিকেটসহ HTTPS প্রয়োজন। ডিফল্টভাবে, Azure Container Apps Azure-ম্যানেজড ডোমেইনের জন্য একটি বিশ্বাসযোগ্য TLS সার্টিফিকেট দেয় ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements))। কাস্টম ডোমেইন ব্যবহার করলে অবশ্যই একটি সার্টিফিকেট বেঁধে দিন (Azure-এর ফ্রি ম্যানেজড সার্টিফিকেট ফিচার ব্যবহার করতে পারেন) ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements))। APIM যদি এন্ডপয়েন্টের সার্টিফিকেট বিশ্বাস না করে, `<validate-jwt>` মেটাডেটা ফেচ করতে ব্যর্থ হবে।

- **এন্ডপয়েন্ট অ্যাক্সেসিবিলিটি:** নিশ্চিত করুন Spring অ্যাপের এন্ডপয়েন্টগুলো APIM থেকে পৌঁছানো যায়। `--ingress external` (অথবা পোর্টালে ইনগ্রেস সক্রিয় করা) সবচেয়ে সহজ। যদি আপনি ইন্টারনাল বা vNet-বাউন্ড এনভায়রনমেন্ট বেছে নেন, APIM (ডিফল্ট পাবলিক) হয়তো পৌঁছাতে পারবে না যদি না একই VNet-এ থাকে। টেস্ট সেটআপে পাবলিক ইনগ্রেস প্রেফার করুন যাতে APIM `.well-known` এবং `/jwks` URL কল করতে পারে।

- **OpenID ডিসকভারি সক্রিয়:** ডিফল্টভাবে Spring Authorization Server `/.well-known/openid-configuration` প্রকাশ করে না যদি না OIDC সক্রিয় করা হয়। `.oidc(Customizer.withDefaults())` আপনার সিকিউরিটি কনফিগে অন্তর্ভুক্ত করুন (উপর দেখানো হয়েছে) যাতে প্রোভাইডার কনফিগারেশন এন্ডপয়েন্ট সক্রিয় হয় ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build))। না হলে APIM-এর `<openid-config>` কল 404 দিবে।

- **Audience ক্লেইম:** Spring ডিফল্টভাবে `aud` ক্লেইম ক্লায়েন্ট আইডি হিসেবে সেট করে। APIM-এর `<audience>` চেক ফেল করলে, টোকেন কাস্টমাইজ করুন (উপর দেখানো মতো) অথবা APIM পলিসি সামঞ্জস্য করুন। নিশ্চিত করুন JWT-এর audience আপনার `<audience>`-এর সাথে মেলে।

- **JSON মেটাডেটা পার্সিং:** OpenID কনফিগারেশন JSON বৈধ হতে হবে। Spring ডিফল্ট কনফিগ একটি স্ট্যান্ডার্ড OIDC মেটাডেটা ডকুমেন্ট তৈরি করে। নিশ্চিত করুন এতে সঠিক `issuer` এবং `jwks_uri` আছে। Spring যদি প্রোক্সি বা পাথ-ভিত্তিক রাউটিংয়ের পিছনে হোস্ট করা হয়, URLs ডাবল চেক করুন। APIM এগুলো যেমন আছে তেমন ব্যবহার করবে।

- **পলিসি অর্ডারিং:** APIM পলিসিতে `<validate-jwt>` অবশ্যই ব্যাকএন্ড রাউটিংয়ের **আগে** থাকতে হবে। না হলে কলগুলো বৈধ টোকেন ছাড়াই অ্যাপে পৌঁছাতে পারে। এছাড়া `<validate-jwt>` অবশ্যই `<inbound>` এর ঠিক নিচে থাকতে হবে (অন্য কোনো কন্ডিশনের ভিতরে নয়) যাতে APIM এটি প্রয়োগ করে।

উপরের ধাপগুলো অনুসরণ করে, আপনি Azure Container Apps-এ Spring AI MCP সার্ভার চালাতে পারবেন এবং Azure API Management দিয়ে আসা OAuth2 JWT গুলো যাচাই করতে পারবেন একটি সহজ পলিসি দিয়ে। মূল বিষয়গুলো হল: Spring Auth এন্ডপয়েন্টগুলো TLS সহ পাবলিকলি প্রকাশ করা, OIDC ডিসকভারি সক্রিয় করা, এবং APIM-এর `validate-jwt` কে OpenID কনফিগ URL-এ পয়েন্ট করা যাতে JWKS স্বয়ংক্রিয়ভাবে ফেচ করা যায়। এই সেটআপ ডেভ/টেস্ট পরিবেশের জন্য উপযুক্ত; প্রোডাকশনের জন্য সঠিক সিক্রেট ম্যানেজমেন্ট, টোকেন লাইফটাইম এবং JWKS কী রোটেশন বিবেচনা করুন।
**References:** ডিফল্ট এন্ডপয়েন্টগুলোর জন্য Spring Authorization Server ডকুমেন্টেশন দেখুন ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)) এবং OIDC কনফিগারেশন ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)); Microsoft APIM ডকুমেন্টেশন থেকে `validate-jwt` উদাহরণ দেখুন ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)); এবং Azure Container Apps ডকুমেন্টেশন থেকে ডিপ্লয়মেন্ট ও সার্টিফিকেট সম্পর্কিত তথ্য দেখুন ([Deploy Java Spring Boot apps to Azure Container Apps - Java on Azure | Microsoft Learn](https://learn.microsoft.com/en-us/azure/developer/java/identity/deploy-spring-boot-to-azure-container-apps#:~:text=Now%20you%20can%20deploy%20your,CLI%20command)) ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)).

**অস্বীকৃতি**:  
এই নথিটি AI অনুবাদ সেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনূদিত হয়েছে। আমরা যথাসাধ্য সঠিকতার চেষ্টা করি, তবে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা অসঙ্গতি থাকতে পারে। মূল নথিটি তার নিজস্ব ভাষায়ই কর্তৃত্বপূর্ণ উৎস হিসেবে বিবেচিত হওয়া উচিত। গুরুত্বপূর্ণ তথ্যের জন্য পেশাদার মানব অনুবাদ গ্রহণ করার পরামর্শ দেওয়া হয়। এই অনুবাদের ব্যবহারে সৃষ্ট কোনো ভুল বোঝাবুঝি বা ভুল ব্যাখ্যার জন্য আমরা দায়ী নই।