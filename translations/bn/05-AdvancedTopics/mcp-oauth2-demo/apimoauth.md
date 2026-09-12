# Spring AI MCP অ্যাপটি Azure Container Apps এ ডিপ্লয় করা

> [!WARNING]
> এই সম্মিলিত অনুমোদন/রিসোর্স সার্ভারটি শেখার এবং
> ডেভ/টেস্ট ব্যবহারের জন্য পরিকল্পিত। প্রোডাকশন সিস্টেমগুলোর জন্য একটি নিবেদিত পরিচয় প্রদানকারী,
> স্থায়ী সাইনিং কী এবং ব্যবস্থাপিত সিক্রেট স্টোরে সংরক্ষিত ক্রেডেনশিয়াল ব্যবহার করা উচিত।

 ([Securing Spring AI MCP servers with OAuth2](https://spring.io/blog/2025/04/02/mcp-server-oauth2)) *চিত্র: Spring Authorization Server দ্বারা সুরক্ষিত Spring AI MCP সার্ভার। সার্ভার ক্লায়েন্টদের অ্যাক্সেস টোকেন ইস্যু করে এবং আগত অনুরোধগুলিতে তা যাচাই করে (সূত্র: Spring ব্লগ) ([Securing Spring AI MCP servers with OAuth2](https://spring.io/blog/2025/04/02/mcp-server-oauth2#:~:text=,server%20with%20the%20MCP%20inspector)).* Spring MCP সার্ভার ডিপ্লয় করতে, এটিকে একটি কন্টেইনার হিসেবে তৈরি করুন এবং বাইরের ইনগ্রেস সহ Azure Container Apps ব্যবহার করুন। উদাহরণস্বরূপ, Azure CLI ব্যবহার করে আপনি চালাতে পারেন:

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

এটি একটি পাবলিকলি-অ্যাকসেসযোগ্য Container App তৈরি করে HTTPS সক্ষম (Azure ডিফল্ট `*.azurecontainerapps.io` ডোমেইনের জন্য একটি বিনামূল্যের TLS সার্টিফিকেট ইস্যু করে ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements))). কমান্ড আউটপুটে অ্যাপের FQDN (যেমন `my-mcp-app.eastus.azurecontainerapps.io`) অন্তর্ভুক্ত থাকবে, যা **issuer URL** বেস হয়ে ওঠে। HTTP ingress সক্রিয় আছে তা নিশ্চিত করুন (উপরের মতো) যাতে APIM অ্যাপটি পৌঁছাতে পারে। একটি টেস্ট/ডেভ সেটআপে, `--ingress external` বিকল্প ব্যবহার করুন (অথবা [Microsoft docs](https://learn.microsoft.com/azure/container-apps/custom-domains-managed-certificates) অনুসারে TLS সহ একটি কাস্টম ডোমেইন বাইন করুন ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)))। কোনো সংবেদনশীল প্রোপার্টিজ (যেমন OAuth ক্লায়েন্ট সিক্রেট) Container Apps সিক্রেটস বা Azure Key Vault এ সংরক্ষণ করুন এবং পরিবেশ ভেরিয়াবল হিসাবে কন্টেইনারে ম্যাপ করুন। 

## Spring Authorization Server কনফিগারেশন

আপনার Spring Boot অ্যাপের কোডে Spring Authorization Server এবং Resource Server স্টার্টার অন্তর্ভুক্ত করুন। একটি `RegisteredClient` কনফিগার করুন (ডেভ/টেস্টে `client_credentials` গ্রান্টের জন্য) এবং একটি JWT কী সোর্স সেট করুন। উদাহরণস্বরূপ, `application.properties` এ আপনি সেট করতে পারেন:

```properties
# OAuth2 client (for testing token issuance)
demo.oauth.client-id=${OAUTH_CLIENT_ID:mcp-client}
demo.oauth.client-secret=${OAUTH_CLIENT_SECRET}
```

একটি সিকিউরিটি ফিল্টার চেইন সংজ্ঞায়িত করে Authorization Server এবং Resource Server সক্ষম করুন। উদাহরণস্বরূপ:

```java
@Configuration
@EnableWebSecurity
public class SecurityConfiguration {

    @Bean
    SecurityFilterChain securityFilterChain(HttpSecurity http) throws Exception {
        OAuth2AuthorizationServerConfigurer<HttpSecurity> authzServer = OAuth2AuthorizationServerConfigurer.authorizationServer();
        http
            .authorizeHttpRequests(auth -> auth.anyRequest().authenticated())
            // অথোরাইজেশন সার্ভার এন্ডপয়েন্টগুলি সক্ষম করুন
            .apply(authzServer.and())
            // রিসোর্স সার্ভার সক্ষম করুন (আসা রিকোয়েস্টে JWT যাচাই করুন)
            .oauth2ResourceServer(oauth2 -> oauth2.jwt(withDefaults()))
            // CSRF নিষ্ক্রিয় করুন (MCP সার্ভার ব্রাউজার-ভিত্তিক নয়)
            .csrf(csrf -> csrf.disable())
            // ক্লায়েন্ট ডেমো টুলগুলির জন্য CORS অনুমোদন করুন
            .cors(withDefaults());
        return http.build();
    }

    // একটি ইন-মেমরি ক্লায়েন্ট (RegisteredClient) এবং একটি JWK সোর্স সংজ্ঞায়িত করুন:
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
        // একটি RSA কী তৈরি করুন (ডেভ/টেস্ট এর জন্য, স্টার্টআপে নতুন করে তৈরি করুন)
        RSAKey rsaKey = new RSAKeyGenerator(2048).keyID("1").generate();
        JWKSet jwkSet = new JWKSet(rsaKey);
        return (selector, context) -> selector.select(jwkSet);
    }
}
```

এই সেটআপ ডিফল্ট OAuth2 এন্ডপয়েন্টগুলি প্রকাশ করবে: `/oauth2/token` টোকেনগুলির জন্য এবং `/oauth2/jwks` JSON ওয়েব কী সেটের জন্য। (ডিফল্টরূপে Spring এর `AuthorizationServerSettings` `/oauth2/token` এবং `/oauth2/jwks` ম্যাপ করে ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)).) সার্ভার উপরের RSA কী দিয়ে স্বাক্ষরিত JWT অ্যাক্সেস টোকেন ইস্যু করবে, এবং তার পাবলিক কী `https://<your-app>:/oauth2/jwks` এ প্রকাশ করবে। 

**OpenID Connect ডিসকভারি সক্ষম করুন:** APIM যাতে issuer এবং JWKS স্বয়ংক্রিয়ভাবে পুনরুদ্ধার করতে পারে, আপনার সিকিউরিটি কনফিগে `.oidc(Customizer.withDefaults())` যোগ করে OIDC প্রোভাইডার কনফিগারেশন এন্ডপয়েন্ট সক্ষম করুন ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)). উদাহরণস্বরূপ:

```java
http
  .apply(authzServer.and())
  .securityMatcher(authzServer.getEndpointsMatcher())
  .with(authzServer, authz -> authz
      .oidc(Customizer.withDefaults()));  // <– সক্রিয় করে /.well-known/openid-configuration
```

এটি `/.well-known/openid-configuration` প্রকাশ করে, যা APIM মেটাডেটার জন্য ব্যবহার করতে পারে। অবশেষে, আপনি JWT **audience** ক্লেইমটি কাস্টমাইজ করতে চাইতে পারেন যাতে APIM এর `<audiences>` যাচাই সফল হয়। উদাহরণস্বরূপ, একটি টোকেন কাস্টমাইজার যোগ করুন:

```java
@Bean
public OAuth2TokenCustomizer<OAuth2TokenClaimsContext> tokenCustomizer() {
    return context -> {
        // একটি কাস্টম শ্রোতা সেট করুন (যেমন ক্লায়েন্ট আইডি বা এপিআই শনাক্তকারী)
        context.getClaims().audience(Collections.singletonList("mcp-client"));
    };
}
```

এটি নিশ্চিত করবে টোকেনগুলো `"aud": ["mcp-client"]` বহন করবে, যা APIM প্রত্যাশিত ক্লায়েন্ট আইডি বা স্কোপের সাথে মেলে। 

## টোকেন এবং JWKS এন্ডপয়েন্ট প্রকাশ করা

ডিপ্লয়মেন্টের পর, আপনার অ্যাপের **issuer URL** হবে `https://<app-fqdn>`, যেমন `https://my-mcp-app.eastus.azurecontainerapps.io`। এর OAuth2 এন্ডপয়েন্টগুলি হল:

- **টোকেন এন্ডপয়েন্ট:** `https://<app-fqdn>/oauth2/token` – ক্লায়েন্টরা এখান থেকে টোকেন পাবে (`client_credentials` প্রবাহ).
- **JWKS এন্ডপয়েন্ট:** `https://<app-fqdn>/oauth2/jwks` – JWK সেট ফেরত দেয় (APIM স্বাক্ষর কী পেতে এটি ব্যবহার করে).
- **OpenID কনফিগ:** `https://<app-fqdn>/.well-known/openid-configuration` – OIDC ডিসকভারি JSON (যাতে `issuer`, `token_endpoint`, `jwks_uri` ইত্যাদি থাকে)।  

APIM **OpenID কনফিগারেশন URL** নির্দেশ করবে, যেখান থেকে এটি `jwks_uri` আবিষ্কার করে। উদাহরণস্বরূপ, যদি আপনার Container App FQDN হয় `my-mcp-app.eastus.azurecontainerapps.io`, তাহলে APIM এর `<openid-config url="...">` হওয়া উচিত `https://my-mcp-app.eastus.azurecontainerapps.io/.well-known/openid-configuration`। (ডিফল্টরূপে Spring সেই মেটাডেটাতে `issuer` একই বেস URL হিসাবে সেট করে ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)).)

## Azure API Management (`validate-jwt`) কনফিগারেশন

Azure APIM-এ এমন একটি ইনবাউন্ড পলিসি যোগ করুন যা `<validate-jwt>` পলিসি ব্যবহার করে আসা JWT গুলো আপনার Spring Authorization Server এর বিরুদ্ধে যাচাই করে। একটি সাধারণ সেটআপের জন্য, আপনি OpenID Connect মেটাডেটা URL ব্যবহার করতে পারেন। পলিসি স্নিপেট উদাহরণ:

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

এই পলিসি APIM-কে বলে Spring Auth Server থেকে OpenID কনফিগারেশন নিয়ে আসে, তার JWKS পুনরুদ্ধার করে, এবং প্রত্যেক টোকেন একটি নির্ভরযোগ্য কী দ্বারা স্বাক্ষরিত এবং সঠিক audience রয়েছে কিনা যাচাই করে। (`<issuers>` বাদ দিলে APIM মেটাডেটার issuer ক্লেইম ব্যবহার করে।) `<audience>` আপনার ক্লায়েন্ট আইডি বা টোকেনে থাকা API রিসোর্স আইডেন্টিফায়ারের সাথে মেলে (উদাহরণে `"mcp-client"` এ সেট করা হয়েছে)। এটি Microsoft এর ডকুমেন্টেশনের সাথে সঙ্গত যেখানে `<openid-config>` সহ `validate-jwt` ব্যবহারের কথা বলা হয়েছে ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation))।

যাচাইয়ের পরে, APIM অনুরোধ (মৌলিক `Authorization` হেডারসহ) ব্যাকএন্ডে ফরোয়ার্ড করবে। যেহেতু Spring অ্যাপ একটি রিসোর্স সার্ভারও, এটি টোকেন পুনরায় যাচাই করবে, তবে APIM ইতিমধ্যেই এর বৈধতা নিশ্চিত করেছে। (ডেভেলপমেন্টের জন্য, আপনি APIM এর যাচাইয়ের উপর নির্ভর করতে পারেন এবং অ্যাপে অতিরিক্ত যাচাই নিষ্ক্রিয় করতে পারেন, তবে উভয়েরই থাকা নিরাপদ।)

## উদাহরণ সেটিংস

| সেটিং             | উদাহরণ মান                                                     | নোটস                                       |
|--------------------|----------------------------------------------------------------------|--------------------------------------------|
| **Issuer**         | `https://my-mcp-app.eastus.azurecontainerapps.io`                    | আপনার Container App এর URL (বেস URI)      |
| **Token endpoint** | `https://my-mcp-app.eastus.azurecontainerapps.io/oauth2/token`       | ডিফল্ট Spring টোকেন এন্ডপয়েন্ট ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize))  |
| **JWKS endpoint**  | `https://my-mcp-app.eastus.azurecontainerapps.io/oauth2/jwks`        | ডিফল্ট JWK সেট এন্ডপয়েন্ট ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize))    |
| **OpenID Config**  | `https://my-mcp-app.eastus.azurecontainerapps.io/.well-known/openid-configuration` | OIDC ডিসকভারি ডকুমেন্ট (স্বয়ংক্রিয়ভাবে তৈরি)    |
| **APIM audience**  | `mcp-client`                                                         | OAuth ক্লায়েন্ট আইডি বা API রিসোর্স নাম   |
| **APIM policy**    | `<openid-config url="https://.../.well-known/openid-configuration" />` | `<validate-jwt>` এই URL ব্যবহার করে ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)) |

## সাধারণ সমস্যাগুলি

- **HTTPS/TLS:** APIM গেটওয়ে OpenID/JWKS এন্ডপয়েন্ট HTTPS এবং বৈধ সার্টিফিকেট দরকার। ডিফল্টরূপে, Azure Container Apps Azure-পরিচালিত ডোমেইনের জন্য একটি বিশ্বাসযোগ্য TLS সার্টিফিকেট সরবরাহ করে ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)). যদি আপনি একটি কাস্টম ডোমেইন ব্যবহার করেন, সার্টিফিকেট বাধ্যতামূলক (Azure এর ফ্রি ম্যানেজড সার্ট বৈশিষ্ট্য ব্যবহার করতে পারেন) ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements))। APIM যদি এন্ডপয়েন্টের সার্টিফিকেট বিশ্বাস করতে না পারে, `<validate-jwt>` মেটাডেটা আনতে ব্যর্থ হবে।  

- **এন্ডপয়েন্ট অ্যাক্সেসিবিলিটি:** নিশ্চিত করুন Spring অ্যাপের এন্ডপয়েন্টগুলি APIM থেকে পৌঁছানো যায়। `--ingress external` ব্যবহার করা (অথবা পোর্টালে ইনগ্রেস সক্রিয় করা) সবচেয়ে সহজ। যদি আপনি একটি অভ্যন্তরীণ বা vNet-বদ্ধ পরিবেশ বেছে নেন, APIM (ডিফল্টরূপে পাবলিক) এটি পৌঁছাতে নাও পারে যদি না একই VNet-এ থাকে। একটি টেস্ট সেটআপে পাবলিক ইনগ্রেস পছন্দ করুন যাতে APIM `.well-known` এবং `/jwks` URL কল করতে পারে। 

- **OpenID ডিসকভারি সক্ষম:** ডিফল্টরূপে, Spring Authorization Server `/.well-known/openid-configuration` প্রকাশ করে না যদি না OIDC সক্রিয় করা হয়। নিশ্চিত করুন `.oidc(Customizer.withDefaults())` আপনার সিকিউরিটি কনফিগে আছে (উপর দেখানো হয়েছে) যাতে প্রোভাইডার কনফিগারেশন এন্ডপয়েন্ট সক্রিয় থাকে ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build))। অন্যথায় APIM এর `<openid-config>` কল ৪০৪ দিবে।

- **Audience ক্লেইম:** Spring ডিফল্ট আচরণ হল `aud` ক্লেইম ক্লায়েন্ট আইডিতে সেট করা। যদি APIM এর `<audience>` যাচাই ব্যর্থ হয়, তাহলে টোকেন কাস্টমাইজ করতে হতে পারে (উপর দেখানো হয়েছে) অথবা APIM পলিসি সামঞ্জস্য করতে হতে পারে। নিশ্চিত করুন JWT এর audience আপনার `<audience>` সাথে মিলে। 

- **JSON মেটাডেটা পার্সিং:** OpenID কনফিগারেশন JSON বৈধ হতে হবে। Spring ডিফল্ট কনফিগ একটি স্ট্যান্ডার্ড OIDC মেটাডেটা ডকুমেন্ট তৈরি করবে। যাচাই করুন এতে সঠিক `issuer` এবং `jwks_uri` আছে। যদি আপনি Spring কে প্রোক্সির পিছনে বা পাথ-বেসড রুটে হোস্ট করেন, এই মেটাডেটার URL গুলো অতিরিক্তভাবে যাচাই করুন। APIM এগুলো যেমন আছে তেমন ব্যবহার করবে। 

- **পলিসি অর্ডারিং:** APIM পলিসিতে `<validate-jwt>` **ব্যাকএন্ডে রাউটিংয়ের আগে** রাখুন। অন্যথায় কলগুলো বৈধ টোকেন ছাড়াই অ্যাপে পৌঁছাতে পারে। এছাড়াও নিশ্চিত করুন `<validate-jwt>` সরাসরি `<inbound>` এর অধীনে রয়েছে (অন্য কোনো শর্তের অভ্যন্তরে নয়) যাতে APIM এটিকে প্রয়োগ করে।

উপরোক্ত ধাপগুলো অনুসরণ করে আপনি আপনার Spring AI MCP সার্ভার Azure Container Apps-এ চালাতে পারবেন এবং Azure API Management *আসা* OAuth2 JWT গুলো একটি নূন্যতম পলিসি দিয়ে যাচাই করতে পারবে। মূল পয়েন্ট হল: Spring Auth এন্ডপয়েন্টগুলো TLS সঙ্গে পাবলিকলি প্রকাশ করা, OIDC ডিসকভারি সক্ষম করা এবং APIM এর `validate-jwt` কে OpenID কনফিগ URL নির্দেশ করা (যাতে এটি JWKS স্বয়ংক্রিয়ভাবে আনতে পারে)। এই সেটআপ ডেভ/টেস্ট পরিবেশের জন্য উপযোগী; প্রোডাকশনের জন্য উপযুক্ত সিক্রেট ম্যানেজমেন্ট, টোকেন লাইফটাইম এবং JWKS এ কী ঘোরানো বিবেচনা করুন।


**তথ্যসূত্র:** ডিফল্ট এন্ডপয়েন্টগুলির জন্য Spring Authorization Server ডকুমেন্টেশন দেখুন ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)) এবং OIDC কনফিগারেশন ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)); Microsoft APIM ডকুমেন্টেশন দেখুন `validate-jwt` উদাহরণের জন্য ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)); এবং Azure Container Apps ডকুমেন্টেশন দেখুন ডিপ্লয়মেন্ট এবং সার্টিফিকেটগুলির জন্য ([Deploy Java Spring Boot apps to Azure Container Apps - Java on Azure | Microsoft Learn](https://learn.microsoft.com/en-us/azure/developer/java/identity/deploy-spring-boot-to-azure-container-apps#:~:text=Now%20you%20can%20deploy%20your,CLI%20command)) ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**অস্বীকৃতি**:
এই নথিটি AI অনুবাদ পরিষেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনূদিত হয়েছে। যদিও আমরা শুদ্ধতার জন্য চেষ্টা করি, অনুগ্রহ করে মনে রাখবেন যে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা অসঙ্গতি থাকতে পারে। মূল নথিটি তার স্বভাষায় কর্তৃত্বপূর্ণ উৎস হিসেবে বিবেচিত হওয়া উচিত। গুরুত্বপূর্ণ তথ্যের জন্য পেশাদার মানব অনুবাদ সুপারিশ করা হয়। এই অনুবাদের ব্যবহারে প্রয়োজনীয় ভুল বোঝাবুঝি বা ভুল ব্যাখ্যার জন্য আমরা দায়বদ্ধ নই।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->