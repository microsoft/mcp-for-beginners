# การปรับใช้แอป Spring AI MCP บน Azure Container Apps

([Securing Spring AI MCP servers with OAuth2](https://spring.io/blog/2025/04/02/mcp-server-oauth2)) *รูปภาพ: เซิร์ฟเวอร์ Spring AI MCP ที่ได้รับการปกป้องด้วย Spring Authorization Server เซิร์ฟเวอร์จะออก access token ให้กับไคลเอนต์และตรวจสอบความถูกต้องของโทเค็นเมื่อมีคำขอเข้ามา (ที่มา: Spring blog) ([Securing Spring AI MCP servers with OAuth2](https://spring.io/blog/2025/04/02/mcp-server-oauth2#:~:text=,server%20with%20the%20MCP%20inspector)).* ในการปรับใช้ Spring MCP server ให้สร้างเป็นคอนเทนเนอร์และใช้ Azure Container Apps พร้อม ingress ภายนอก เช่น ใช้ Azure CLI รันคำสั่ง:

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

คำสั่งนี้จะสร้าง Container App ที่เข้าถึงได้สาธารณะพร้อมเปิดใช้งาน HTTPS (Azure จะออกใบรับรอง TLS ฟรีสำหรับโดเมน `*.azurecontainerapps.io` เริ่มต้น ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements))) ผลลัพธ์ของคำสั่งจะรวม FQDN ของแอป (เช่น `my-mcp-app.eastus.azurecontainerapps.io`) ซึ่งจะกลายเป็นฐานของ **issuer URL** ให้แน่ใจว่าเปิดใช้งาน HTTP ingress (ตามตัวอย่างข้างต้น) เพื่อให้ APIM สามารถเข้าถึงแอปได้ ในการตั้งค่าสำหรับทดสอบ/พัฒนา ให้ใช้ตัวเลือก `--ingress external` (หรือผูกโดเมนที่กำหนดเองพร้อม TLS ตาม [เอกสาร Microsoft](https://learn.microsoft.com/azure/container-apps/custom-domains-managed-certificates) ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements))) เก็บข้อมูลที่เป็นความลับ เช่น OAuth client secrets ใน Container Apps secrets หรือ Azure Key Vault และแมปข้อมูลเหล่านั้นเข้าไปในคอนเทนเนอร์เป็น environment variables

## การกำหนดค่า Spring Authorization Server

ในโค้ดของแอป Spring Boot ให้เพิ่ม Spring Authorization Server และ Resource Server starters กำหนด `RegisteredClient` (สำหรับ `client_credentials` grant ใน dev/test) และแหล่งที่มาของคีย์ JWT เช่น ใน `application.properties` อาจตั้งค่าเป็น:

```properties
# OAuth2 client (for testing token issuance)
spring.security.oauth2.authorizationserver.client.oidc-client.registration.client-id=mcp-client
spring.security.oauth2.authorizationserver.client.oidc-client.registration.client-secret={noop}secret
spring.security.oauth2.authorizationserver.client.oidc-client.registration.authorization-grant-types=client_credentials
spring.security.oauth2.authorizationserver.client.oidc-client.registration.client-authentication-methods=client_secret_basic
```

เปิดใช้งาน Authorization Server และ Resource Server โดยกำหนด security filter chain เช่น:

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

การตั้งค่านี้จะเปิดเผย OAuth2 endpoints เริ่มต้น: `/oauth2/token` สำหรับรับโทเค็น และ `/oauth2/jwks` สำหรับ JSON Web Key Set (โดยค่าเริ่มต้น Spring’s `AuthorizationServerSettings` จะแมป `/oauth2/token` และ `/oauth2/jwks` ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize))) เซิร์ฟเวอร์จะออก JWT access tokens ที่ลงนามด้วยคีย์ RSA ข้างต้น และเผยแพร่คีย์สาธารณะที่ `https://<your-app>:/oauth2/jwks`

**เปิดใช้งาน OpenID Connect discovery:** เพื่อให้ APIM ดึงข้อมูล issuer และ JWKS อัตโนมัติ ให้เปิดใช้งาน endpoint การกำหนดค่า OIDC provider โดยเพิ่ม `.oidc(Customizer.withDefaults())` ในการตั้งค่าความปลอดภัยของคุณ ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)) เช่น:

```java
http
  .apply(authzServer.and())
  .securityMatcher(authzServer.getEndpointsMatcher())
  .with(authzServer, authz -> authz
      .oidc(Customizer.withDefaults()));  // <– enables /.well-known/openid-configuration
```

จะเปิดเผย `/.well-known/openid-configuration` ซึ่ง APIM สามารถใช้สำหรับ metadata สุดท้าย คุณอาจต้องการปรับแต่ง JWT **audience** claim เพื่อให้การตรวจสอบ `<audiences>` ของ APIM ผ่าน เช่น เพิ่ม token customizer:

```java
@Bean
public OAuth2TokenCustomizer<OAuth2TokenClaimsContext> tokenCustomizer() {
    return context -> {
        // Set a custom audience (e.g. the client ID or API identifier)
        context.getClaims().audience(Collections.singletonList("mcp-client"));
    };
}
```

วิธีนี้จะทำให้โทเค็นมี `"aud": ["mcp-client"]` ซึ่งตรงกับ client ID หรือ scope ที่ APIM คาดหวัง

## การเปิดเผย Token และ JWKS Endpoints

หลังจากปรับใช้แล้ว **issuer URL** ของแอปจะเป็น `https://<app-fqdn>` เช่น `https://my-mcp-app.eastus.azurecontainerapps.io` โดย OAuth2 endpoints มีดังนี้:

- **Token endpoint:** `https://<app-fqdn>/oauth2/token` – ไคลเอนต์ใช้รับโทเค็น (client_credentials flow)
- **JWKS endpoint:** `https://<app-fqdn>/oauth2/jwks` – ส่งคืนชุด JWK (APIM ใช้ดึงคีย์สำหรับตรวจสอบลายเซ็น)
- **OpenID Config:** `https://<app-fqdn>/.well-known/openid-configuration` – JSON สำหรับ OIDC discovery (มี `issuer`, `token_endpoint`, `jwks_uri` เป็นต้น)

APIM จะชี้ไปที่ **OpenID configuration URL** เพื่อค้นหา `jwks_uri` เช่น ถ้า FQDN ของ Container App คือ `my-mcp-app.eastus.azurecontainerapps.io` ให้ตั้งค่า `<openid-config url="...">` ของ APIM เป็น `https://my-mcp-app.eastus.azurecontainerapps.io/.well-known/openid-configuration` (โดยค่าเริ่มต้น Spring จะตั้งค่า `issuer` ใน metadata ให้เป็น URL ฐานเดียวกัน ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)))

## การกำหนดค่า Azure API Management (`validate-jwt`)

ใน Azure APIM ให้เพิ่มนโยบาย inbound ที่ใช้ `<validate-jwt>` เพื่อตรวจสอบ JWT ที่เข้ามากับ Spring Authorization Server สำหรับการตั้งค่าง่าย ๆ คุณสามารถใช้ OpenID Connect metadata URL ตัวอย่างนโยบาย:

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

นโยบายนี้จะสั่งให้ APIM ดึง OpenID configuration จาก Spring Auth Server ดึง JWKS และตรวจสอบว่าโทเค็นแต่ละอันถูกลงนามด้วยคีย์ที่เชื่อถือได้และมี audience ถูกต้อง (ถ้าไม่ระบุ `<issuers>` APIM จะใช้ค่า `issuer` จาก metadata อัตโนมัติ) `<audience>` ควรตรงกับ client ID หรือชื่อ resource ของ API ในโทเค็น (ในตัวอย่างข้างต้นตั้งเป็น `"mcp-client"`) ซึ่งสอดคล้องกับเอกสารของ Microsoft เกี่ยวกับการใช้ `validate-jwt` กับ `<openid-config>` ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation))

หลังจากตรวจสอบแล้ว APIM จะส่งคำขอ (รวมถึง header `Authorization` เดิม) ไปยัง backend เนื่องจากแอป Spring เป็น resource server ด้วย มันจะตรวจสอบโทเค็นอีกครั้ง แต่ APIM ได้ตรวจสอบความถูกต้องแล้ว (สำหรับการพัฒนา คุณอาจพึ่งพาการตรวจสอบของ APIM และปิดการตรวจสอบในแอปได้ แต่เพื่อความปลอดภัยควรเปิดทั้งสองส่วน)

## ตัวอย่างการตั้งค่า

| การตั้งค่า          | ตัวอย่างค่า                                                        | หมายเหตุ                                    |
|--------------------|----------------------------------------------------------------------|--------------------------------------------|
| **Issuer**         | `https://my-mcp-app.eastus.azurecontainerapps.io`                    | URL ของ Container App (ฐาน URI)             |
| **Token endpoint** | `https://my-mcp-app.eastus.azurecontainerapps.io/oauth2/token`       | token endpoint เริ่มต้นของ Spring ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize))  |
| **JWKS endpoint**  | `https://my-mcp-app.eastus.azurecontainerapps.io/oauth2/jwks`        | JWK Set endpoint เริ่มต้น ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize))    |
| **OpenID Config**  | `https://my-mcp-app.eastus.azurecontainerapps.io/.well-known/openid-configuration` | เอกสาร discovery OIDC (สร้างอัตโนมัติ)       |
| **APIM audience**  | `mcp-client`                                                         | OAuth client ID หรือชื่อ resource ของ API   |
| **APIM policy**    | `<openid-config url="https://.../.well-known/openid-configuration" />` | `<validate-jwt>` ใช้ URL นี้ ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)) |

## ข้อควรระวังทั่วไป

- **HTTPS/TLS:** เกตเวย์ APIM ต้องการให้ OpenID/JWKS endpoint ใช้ HTTPS พร้อมใบรับรองที่ถูกต้อง โดยค่าเริ่มต้น Azure Container Apps จะให้ใบรับรอง TLS ที่เชื่อถือได้สำหรับโดเมนที่ Azure จัดการ ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)) หากใช้โดเมนที่กำหนดเอง ต้องผูกใบรับรอง (สามารถใช้ฟีเจอร์ใบรับรองที่จัดการฟรีของ Azure) ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)) หาก APIM ไม่เชื่อถือใบรับรองของ endpoint `<validate-jwt>` จะไม่สามารถดึง metadata ได้

- **การเข้าถึง Endpoint:** ตรวจสอบให้แน่ใจว่า endpoint ของแอป Spring สามารถเข้าถึงได้จาก APIM การใช้ `--ingress external` (หรือเปิด ingress ในพอร์ทัล) เป็นวิธีที่ง่ายที่สุด หากเลือกสภาพแวดล้อมแบบ internal หรือผูกกับ vNet APIM (ซึ่งโดยปกติเป็นสาธารณะ) อาจไม่สามารถเข้าถึงได้เว้นแต่จะอยู่ใน vNet เดียวกัน ในการตั้งค่าสำหรับทดสอบ ควรใช้ ingress สาธารณะเพื่อให้ APIM เรียก `.well-known` และ `/jwks` ได้

- **เปิดใช้งาน OpenID Discovery:** โดยค่าเริ่มต้น Spring Authorization Server **จะไม่เปิดเผย** `/.well-known/openid-configuration` หากไม่ได้เปิดใช้งาน OIDC ให้แน่ใจว่าเพิ่ม `.oidc(Customizer.withDefaults())` ในการตั้งค่าความปลอดภัย (ดูข้างต้น) เพื่อเปิดใช้งาน endpoint การกำหนดค่า provider ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)) มิฉะนั้นการเรียก `<openid-config>` ของ APIM จะได้ผลลัพธ์ 404

- **Audience Claim:** พฤติกรรมเริ่มต้นของ Spring คือกำหนดค่า `aud` เป็น client ID หากการตรวจสอบ `<audience>` ของ APIM ล้มเหลว อาจต้องปรับแต่งโทเค็น (ตามตัวอย่างข้างต้น) หรือแก้ไขนโยบาย APIM ให้แน่ใจว่า audience ใน JWT ตรงกับที่ตั้งค่าใน `<audience>`

- **การแยกวิเคราะห์ JSON Metadata:** JSON ของ OpenID configuration ต้องถูกต้องตามมาตรฐาน การตั้งค่าเริ่มต้นของ Spring จะสร้างเอกสาร metadata OIDC มาตรฐาน ตรวจสอบให้แน่ใจว่ามีค่า `issuer` และ `jwks_uri` ที่ถูกต้อง หากโฮสต์ Spring อยู่หลังพร็อกซีหรือเส้นทางแบบ path-based ให้ตรวจสอบ URL ใน metadata นี้อย่างละเอียด APIM จะใช้ค่าที่ให้มาโดยตรง

- **ลำดับของนโยบาย:** ในนโยบาย APIM ให้วาง `<validate-jwt>` **ก่อน** การกำหนดเส้นทางไปยัง backend มิฉะนั้นคำขออาจถึงแอปโดยไม่มีโทเค็นที่ถูกต้อง และให้แน่ใจว่า `<validate-jwt>` อยู่ภายใต้ `<inbound>` โดยตรง (ไม่ซ้อนในเงื่อนไขอื่น) เพื่อให้ APIM ใช้งานนโยบายนี้

โดยทำตามขั้นตอนข้างต้น คุณจะสามารถรัน Spring AI MCP server บน Azure Container Apps และให้ Azure API Management ตรวจสอบ JWT OAuth2 ที่เข้ามาได้ด้วยนโยบายที่เรียบง่าย จุดสำคัญคือ เปิดเผย Spring Auth endpoints สู่สาธารณะพร้อม TLS, เปิดใช้งาน OIDC discovery และชี้ `validate-jwt` ของ APIM ไปที่ URL การกำหนดค่า OpenID (เพื่อให้ดึง JWKS อัตโนมัติ) การตั้งค่านี้เหมาะสำหรับสภาพแวดล้อมทดสอบ/พัฒนา สำหรับการใช้งานจริง ควรพิจารณาการจัดการความลับอย่างเหมาะสม, อายุของโทเค็น และการหมุนเวียนคีย์ใน JWKS ตามความจำเป็น
**References:** ดูเอกสาร Spring Authorization Server สำหรับ endpoints เริ่มต้น ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)) และการตั้งค่า OIDC ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)); ดูเอกสาร Microsoft APIM สำหรับตัวอย่าง `validate-jwt` ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)); และเอกสาร Azure Container Apps สำหรับการดีพลอยและใบรับรอง ([Deploy Java Spring Boot apps to Azure Container Apps - Java on Azure | Microsoft Learn](https://learn.microsoft.com/en-us/azure/developer/java/identity/deploy-spring-boot-to-azure-container-apps#:~:text=Now%20you%20can%20deploy%20your,CLI%20command)) ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)).

**ข้อจำกัดความรับผิดชอบ**:  
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษาอัตโนมัติ [Co-op Translator](https://github.com/Azure/co-op-translator) แม้เราจะพยายามให้ความถูกต้องสูงสุด แต่โปรดทราบว่าการแปลอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาต้นทางถือเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ ขอแนะนำให้ใช้บริการแปลโดยผู้เชี่ยวชาญมนุษย์ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความผิดใด ๆ ที่เกิดจากการใช้การแปลนี้