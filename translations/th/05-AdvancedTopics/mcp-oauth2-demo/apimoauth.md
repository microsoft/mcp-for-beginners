# การปรับใช้แอป Spring AI MCP ไปยัง Azure Container Apps

> [!WARNING]
> เซิร์ฟเวอร์การอนุญาต/ทรัพยากรรวมนี้มีไว้สำหรับการเรียนรู้และ
> ใช้ในการพัฒนา/ทดสอบเท่านั้น ระบบที่ใช้งานจริงควรใช้ผู้ให้บริการตัวตนเฉพาะ,
> กุญแจการเซ็นชื่อที่คงทน และข้อมูลประจำตัวที่เก็บในที่จัดเก็บความลับที่มีการจัดการ

 ([Securing Spring AI MCP servers with OAuth2](https://spring.io/blog/2025/04/02/mcp-server-oauth2)) *รูปภาพ: เซิร์ฟเวอร์ Spring AI MCP ที่ได้รับการป้องกันด้วย Spring Authorization Server เซิร์ฟเวอร์ออกโทเค็นการเข้าถึงให้กับไคลเอ็นต์และตรวจสอบความถูกต้องในคำขอที่เข้ามา (ที่มา: บล็อกของ Spring) ([Securing Spring AI MCP servers with OAuth2](https://spring.io/blog/2025/04/02/mcp-server-oauth2#:~:text=,server%20with%20the%20MCP%20inspector)).* ในการปรับใช้เซิร์ฟเวอร์ Spring MCP ให้สร้างเป็นคอนเทนเนอร์และใช้ Azure Container Apps พร้อมอินกรีสภายนอก ตัวอย่างเช่น โดยใช้ Azure CLI คุณสามารถรันคำสั่งได้ว่า:

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

คำสั่งนี้จะสร้าง Container App ที่เข้าถึงได้สาธารณะโดยเปิดใช้ HTTPS (Azure ออกใบรับรอง TLS ฟรีสำหรับโดเมนเริ่มต้น `*.azurecontainerapps.io` ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements))). ผลลัพธ์ของคำสั่งรวมถึงชื่อ FQDN ของแอป (เช่น `my-mcp-app.eastus.azurecontainerapps.io`) ซึ่งจะกลายเป็นฐานของ **issuer URL** ตรวจสอบให้แน่ใจว่าได้เปิดใช้ HTTP ingress (ตามด้านบน) เพื่อให้ APIM สามารถเข้าถึงแอปได้ ในการติดตั้งแบบทดสอบ/พัฒนา ให้ใช้ตัวเลือก `--ingress external` (หรือผูกโดเมนที่กำหนดเองพร้อม TLS ตาม [เอกสารของ Microsoft](https://learn.microsoft.com/azure/container-apps/custom-domains-managed-certificates) ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements))). จัดเก็บข้อมูลลับใด ๆ (เช่น ความลับของ OAuth client) ในความลับของ Container Apps หรือ Azure Key Vault และแม็ปเข้ากับคอนเทนเนอร์เป็นตัวแปรสภาพแวดล้อม

## การกำหนดค่า Spring Authorization Server

ในโค้ดแอป Spring Boot ของคุณ ให้รวม Spring Authorization Server และ Resource Server starters กำหนด `RegisteredClient` (สำหรับการให้สิทธิ์ `client_credentials` ในการพัฒนา/ทดสอบ) และแหล่งกุญแจ JWT ตัวอย่างเช่น ใน `application.properties` คุณอาจตั้งค่า:

```properties
# OAuth2 client (for testing token issuance)
demo.oauth.client-id=${OAUTH_CLIENT_ID:mcp-client}
demo.oauth.client-secret=${OAUTH_CLIENT_SECRET}
```

เปิดใช้งาน Authorization Server และ Resource Server โดยกำหนด security filter chain ตัวอย่างเช่น:

```java
@Configuration
@EnableWebSecurity
public class SecurityConfiguration {

    @Bean
    SecurityFilterChain securityFilterChain(HttpSecurity http) throws Exception {
        OAuth2AuthorizationServerConfigurer<HttpSecurity> authzServer = OAuth2AuthorizationServerConfigurer.authorizationServer();
        http
            .authorizeHttpRequests(auth -> auth.anyRequest().authenticated())
            // เปิดใช้งาน endpoints ของ Authorization Server
            .apply(authzServer.and())
            // เปิดใช้งาน Resource Server (ตรวจสอบ JWT ในคำขอที่เข้ามา)
            .oauth2ResourceServer(oauth2 -> oauth2.jwt(withDefaults()))
            // ปิดการใช้งาน CSRF (เซิร์ฟเวอร์ MCP ไม่ใช่แบบเบราว์เซอร์)
            .csrf(csrf -> csrf.disable())
            // อนุญาต CORS สำหรับเครื่องมือสาธิตของไคลเอนต์
            .cors(withDefaults());
        return http.build();
    }

    // กำหนดลูกค้าในหน่วยความจำ (RegisteredClient) และแหล่ง JWK:
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
        // สร้างกุญแจ RSA (สำหรับการพัฒนา/ทดสอบ สร้างใหม่ทุกครั้งเมื่อเริ่มใช้งาน)
        RSAKey rsaKey = new RSAKeyGenerator(2048).keyID("1").generate();
        JWKSet jwkSet = new JWKSet(rsaKey);
        return (selector, context) -> selector.select(jwkSet);
    }
}
```

การตั้งค่านี้จะเปิดเผยจุดสิ้นสุด OAuth2 เริ่มต้น: `/oauth2/token` สำหรับโทเค็นและ `/oauth2/jwks` สำหรับ JSON Web Key Set (โดยค่าเริ่มต้น Spring `AuthorizationServerSettings` จะทำแม็ป `/oauth2/token` และ `/oauth2/jwks` ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)).) เซิร์ฟเวอร์จะออกโทเค็นการเข้าถึง JWT ที่ลงนามโดยกุญแจ RSA ข้างต้น และเผยแพร่กุญแจสาธารณะที่ `https://<your-app>:/oauth2/jwks`

**เปิดใช้งานการค้นหา OpenID Connect:** เพื่อให้ APIM ดึงข้อมูล issuer และ JWKS โดยอัตโนมัติ ให้เปิดใช้งานจุดสิ้นสุดการกำหนดค่าผู้ให้บริการ OIDC โดยเพิ่ม `.oidc(Customizer.withDefaults())` ในการกำหนดค่าความปลอดภัยของคุณ ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)). ตัวอย่างเช่น:

```java
http
  .apply(authzServer.and())
  .securityMatcher(authzServer.getEndpointsMatcher())
  .with(authzServer, authz -> authz
      .oidc(Customizer.withDefaults()));  // <– เปิดใช้งาน /.well-known/openid-configuration
```

นี้จะเปิดเผย `/.well-known/openid-configuration` ซึ่ง APIM สามารถใช้สำหรับเมตาดาต้า สุดท้าย คุณอาจต้องการปรับแต่ง JWT **audience** claim เพื่อให้ตรวจสอบ `<audiences>` ของ APIM ผ่าน ตัวอย่างเช่น เพิ่ม token customizer:

```java
@Bean
public OAuth2TokenCustomizer<OAuth2TokenClaimsContext> tokenCustomizer() {
    return context -> {
        // ตั้งค่ากลุ่มเป้าหมายที่กำหนดเอง (เช่น รหัสลูกค้าหรือรหัส API)
        context.getClaims().audience(Collections.singletonList("mcp-client"));
    };
}
```

สิ่งนี้ช่วยให้โทเค็นมีค่า `"aud": ["mcp-client"]` ซึ่งตรงกับ client ID หรือ scope ที่ APIM คาดหวัง

## การเปิดเผย Token และ JWKS Endpoints

หลังจากปรับใช้แล้ว **issuer URL** ของแอปคุณจะเป็น `https://<app-fqdn>` เช่น `https://my-mcp-app.eastus.azurecontainerapps.io` จุดสิ้นสุด OAuth2 มีดังนี้:

- **Token endpoint:** `https://<app-fqdn>/oauth2/token` – ลูกค้าใช้รับโทเค็นที่นี่ (การไหลของ client_credentials)
- **JWKS endpoint:** `https://<app-fqdn>/oauth2/jwks` – คืนค่า JWK set (ใช้โดย APIM เพื่อรับกุญแจสำหรับการเซ็นชื่อ)
- **OpenID Config:** `https://<app-fqdn>/.well-known/openid-configuration` – JSON การค้นหา OIDC (ประกอบด้วย `issuer`, `token_endpoint`, `jwks_uri`, เป็นต้น)

APIM จะชี้ไปที่ **OpenID configuration URL** ซึ่งจะค้นพบ `jwks_uri` ตัวอย่างเช่น หาก FQDN ของ Container App คุณคือ `my-mcp-app.eastus.azurecontainerapps.io` ดังนั้นค่า `<openid-config url="...">` ของ APIM ควรใช้ `https://my-mcp-app.eastus.azurecontainerapps.io/.well-known/openid-configuration` (โดยค่าเริ่มต้น Spring จะตั้งค่า `issuer` ในเมตาดาต้านั้นเป็น URL ฐานเดียวกัน ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)).)

## การกำหนดค่า Azure API Management (`validate-jwt`)

ใน Azure APIM ให้เพิ่มนโยบาย inbound ที่ใช้ `<validate-jwt>` เพื่อตรวจสอบ JWT ที่เข้ามาต่อ Spring Authorization Server ของคุณ สำหรับการตั้งค่าพื้นฐาน คุณสามารถใช้ URL เมตาดาต้า OpenID Connect ได้ ตัวอย่างส่วนเล็ก ๆ ของนโยบาย:

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

นโยบายนี้บอก APIM ให้ดึงการกำหนดค่า OpenID จาก Spring Auth Server, รับ JWKS และตรวจสอบว่าโทเค็นแต่ละอันได้ลงชื่อด้วยกุญแจที่ไว้วางใจและมี audience ถูกต้อง (ถ้าคุณละเว้น `<issuers>` APIM จะใช้ค่า `issuer` จากเมตาดาต้าโดยอัตโนมัติ) `<audience>` ควรตรงกับ client ID ของคุณหรือรหัสทรัพยากร API ในโทเค็น (ในตัวอย่างข้างต้น เราตั้งค่าเป็น `"mcp-client"`). สิ่งนี้สอดคล้องกับเอกสาร Microsoft เกี่ยวกับการใช้ `validate-jwt` กับ `<openid-config>` ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)).

หลังจากการตรวจสอบนี้แล้ว APIM จะส่งคำขอ (รวมถึง header `Authorization` ดั้งเดิม) ไปยัง backend เนื่องจากแอป Spring ยังเป็น resource server ด้วย มันจะตรวจสอบโทเค็นอีกครั้ง แต่ APIM ได้ยืนยันความถูกต้องแล้ว (สำหรับการพัฒนา คุณสามารถพึ่งการตรวจสอบของ APIM และปิดการตรวจสอบเพิ่มเติมในแอปหากต้องการ แต่ปลอดภัยกว่าที่จะเก็บทั้งสองอย่างไว้)

## ตัวอย่างการตั้งค่า

| การตั้งค่า            | ตัวอย่างค่า                                                        | หมายเหตุ                                  |
|--------------------|----------------------------------------------------------------------|--------------------------------------------|
| **Issuer**         | `https://my-mcp-app.eastus.azurecontainerapps.io`                    | URL ของ Container App ของคุณ (ฐาน URI)     |
| **Token endpoint** | `https://my-mcp-app.eastus.azurecontainerapps.io/oauth2/token`       | จุดสิ้นสุด token เริ่มต้นของ Spring ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize))  |
| **JWKS endpoint**  | `https://my-mcp-app.eastus.azurecontainerapps.io/oauth2/jwks`        | จุดสิ้นสุด JWK Set เริ่มต้น ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize))    |
| **OpenID Config**  | `https://my-mcp-app.eastus.azurecontainerapps.io/.well-known/openid-configuration` | เอกสารค้นหา OIDC (สร้างอัตโนมัติ)           |
| **APIM audience**  | `mcp-client`                                                         | OAuth client ID หรือชื่อทรัพยากร API       |
| **APIM policy**    | `<openid-config url="https://.../.well-known/openid-configuration" />` | `<validate-jwt>` ใช้ URL นี้ ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)) |

## ข้อควรระวังทั่วไป

- **HTTPS/TLS:** 게이트เวย์ APIM ต้องการให้จุดสิ้นสุด OpenID/JWKS เป็น HTTPS ที่มีใบรับรองถูกต้อง โดยค่าเริ่มต้น Azure Container Apps ให้ใบรับรอง TLS ที่เชื่อถือได้สำหรับโดเมนที่จัดการโดย Azure ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)) หากคุณใช้โดเมนเฉพาะ ให้แน่ใจว่าได้ผูกใบรับรอง (คุณสามารถใช้ฟีเจอร์ใบรับรองที่จัดการฟรีของ Azure) ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)) หาก APIM ไม่สามารถเชื่อถือใบรับรองของจุดสิ้นสุดได้ `<validate-jwt>` จะไม่สามารถดึงข้อมูลเมตาดาต้าได้

- **การเข้าถึงจุดสิ้นสุด:** ตรวจสอบให้แน่ใจว่าจุดสิ้นสุดของแอป Spring สามารถเข้าถึงได้จาก APIM การใช้ `--ingress external` (หรือเปิดใช้งาน ingress ในพอร์ทัล) เป็นวิธีที่ง่ายที่สุด หากคุณเลือกสภาพแวดล้อมภายในหรือที่ผูกกับ vNet APIM (โดยค่าเริ่มต้นเป็นสาธารณะ) อาจไม่สามารถเข้าถึงได้เว้นแต่จะวางใน VNet เดียวกัน ในการติดตั้งแบบทดสอบ ควรใช้ ingress สาธารณะเพื่อให้ APIM สามารถเรียก URL `.well-known` และ `/jwks` ได้

- **เปิดใช้ OpenID Discovery:** โดยค่าเริ่มต้น Spring Authorization Server **จะไม่เปิดเผย** `/.well-known/openid-configuration` เว้นแต่จะเปิดใช้ OIDC ตรวจสอบให้แน่ใจว่ารวม `.oidc(Customizer.withDefaults())` ในการกำหนดค่าความปลอดภัยของคุณ (ดูด้านบน) เพื่อให้จุดสิ้นสุดการกำหนดค่าผู้ให้บริการทำงาน ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)) มิฉะนั้นคำสั่ง `<openid-config>` ของ APIM จะส่งผลลัพธ์ 404

- **Audience Claim:** พฤติกรรมเริ่มต้นของ Spring คือการตั้งค่า claim `aud` เป็น client ID หากการตรวจสอบ `<audience>` ของ APIM ไม่ผ่าน คุณอาจต้องปรับแต่งโทเค็น (ตามที่แสดงด้านบน) หรือตั้งค่านโยบาย APIM ใหม่ ตรวจสอบให้แน่ใจว่า audience ใน JWT ของคุณตรงกับที่กำหนดในการตั้งค่า `<audience>`

- **การแยกวิเคราะห์เมตาดาต้า JSON:** ไฟล์ JSON การกำหนดค่า OpenID ต้องถูกต้อง การตั้งค่าเริ่มต้นของ Spring จะส่งออกเอกสารเมตาดาต้า OIDC มาตรฐาน ตรวจสอบให้แน่ใจว่ามี `issuer` และ `jwks_uri` ถูกต้อง หากคุณโฮสต์ Spring เบื้องหลังพร็อกซีหรือเส้นทางแบบ path-based ตรวจสอบ URL ในเมตาดาต้านี้อีกครั้ง APIM จะใช้ค่าเหล่านี้ตามที่ได้รับ

- **ลำดับนโยบาย:** ในนโยบาย APIM ให้วาง `<validate-jwt>` **ก่อน** การกำหนดเส้นทางไปยัง backend มิฉะนั้นคำขออาจถูกส่งไปยังแอปของคุณโดยไม่มีโทเค็นที่ถูกต้อง และตรวจสอบให้แน่ใจว่า `<validate-jwt>` อยู่ใต้ `<inbound>` ทันที (ไม่ซ้อนอยู่ภายใต้เงื่อนไขอื่น) เพื่อให้ APIM ใช้งานได้

โดยการทำตามขั้นตอนข้างต้น คุณสามารถรัน Spring AI MCP server ของคุณใน Azure Container Apps และให้ Azure API Management ตรวจสอบ OAuth2 JWT ที่เข้ามาด้วยนโยบายน้อยที่สุด จุดสำคัญคือ: เปิดเผยจุดสิ้นสุด Spring Auth อย่างสาธารณะพร้อม TLS, เปิดใช้งานการค้นหา OIDC และชี้ `validate-jwt` ของ APIM ไปยัง URL การตั้งค่า OpenID (เพื่อให้ดึง JWKS อัตโนมัติ) การตั้งค่านี้เหมาะสำหรับสภาพแวดล้อมพัฒนา/ทดสอบ; สำหรับการใช้งานจริง ควรพิจารณาการจัดการความลับอย่างเหมาะสม, อายุของโทเค็น และการหมุนกุญแจใน JWKS ตามความจำเป็น


**แหล่งอ้างอิง:** ดูเอกสาร Spring Authorization Server สำหรับค่าเริ่มต้นของ endpoints ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)) และการกำหนดค่า OIDC ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)); ดูเอกสาร Microsoft APIM สำหรับตัวอย่าง `validate-jwt` ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)); และเอกสาร Azure Container Apps สำหรับการปรับใช้และใบรับรอง ([Deploy Java Spring Boot apps to Azure Container Apps - Java on Azure | Microsoft Learn](https://learn.microsoft.com/en-us/azure/developer/java/identity/deploy-spring-boot-to-azure-container-apps#:~:text=Now%20you%20can%20deploy%20your,CLI%20command)) ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ปฏิเสธความรับผิดชอบ**:
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษา AI [Co-op Translator](https://github.com/Azure/co-op-translator) ขณะที่เราพยายามให้ความถูกต้อง โปรดทราบว่าการแปลโดยอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาต้นทางควรถูกพิจารณาเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ แนะนำให้ใช้การแปลโดยมนุษย์มืออาชีพ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความที่ผิดพลาดที่เกิดขึ้นจากการใช้การแปลนี้
<!-- CO-OP TRANSLATOR DISCLAIMER END -->