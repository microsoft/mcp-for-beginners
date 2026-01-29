# Menyebarkan Aplikasi Spring AI MCP ke Azure Container Apps

 ([Mengamankan pelayan Spring AI MCP dengan OAuth2](https://spring.io/blog/2025/04/02/mcp-server-oauth2)) *Rajah: Pelayan Spring AI MCP yang dilindungi dengan Spring Authorization Server. Pelayan mengeluarkan token akses kepada klien dan mengesahkannya pada permintaan masuk (sumber: blog Spring) ([Mengamankan pelayan Spring AI MCP dengan OAuth2](https://spring.io/blog/2025/04/02/mcp-server-oauth2#:~:text=,server%20with%20the%20MCP%20inspector)).* Untuk menyebarkan pelayan Spring MCP, bina ia sebagai kontena dan gunakan Azure Container Apps dengan ingress luaran. Contohnya, menggunakan Azure CLI anda boleh jalankan:

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

Ini akan mencipta Container App yang boleh diakses secara awam dengan HTTPS diaktifkan (Azure mengeluarkan sijil TLS percuma untuk domain lalai `*.azurecontainerapps.io` ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements))). Output arahan termasuk FQDN aplikasi (contoh `my-mcp-app.eastus.azurecontainerapps.io`), yang menjadi asas **URL penerbit**. Pastikan ingress HTTP diaktifkan (seperti di atas) supaya APIM boleh mengakses aplikasi. Dalam tetapan ujian/pembangunan, gunakan pilihan `--ingress external` (atau pautkan domain tersuai dengan TLS mengikut [dokumentasi Microsoft](https://learn.microsoft.com/azure/container-apps/custom-domains-managed-certificates) ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements))). Simpan sebarang sifat sensitif (seperti rahsia klien OAuth) dalam rahsia Container Apps atau Azure Key Vault, dan peta mereka ke dalam kontena sebagai pembolehubah persekitaran.

## Mengkonfigurasi Spring Authorization Server

Dalam kod aplikasi Spring Boot anda, sertakan starter Spring Authorization Server dan Resource Server. Konfigurasikan `RegisteredClient` (untuk pemberian `client_credentials` dalam dev/test) dan sumber kunci JWT. Contohnya, dalam `application.properties` anda mungkin tetapkan:

```properties
# OAuth2 client (for testing token issuance)
spring.security.oauth2.authorizationserver.client.oidc-client.registration.client-id=mcp-client
spring.security.oauth2.authorizationserver.client.oidc-client.registration.client-secret={noop}secret
spring.security.oauth2.authorizationserver.client.oidc-client.registration.authorization-grant-types=client_credentials
spring.security.oauth2.authorizationserver.client.oidc-client.registration.client-authentication-methods=client_secret_basic
```

Aktifkan Authorization Server dan Resource Server dengan mentakrifkan rantaian penapis keselamatan. Contohnya:

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

Tetapan ini akan mendedahkan titik akhir OAuth2 lalai: `/oauth2/token` untuk token dan `/oauth2/jwks` untuk Set Kunci Web JSON. (Secara lalai, `AuthorizationServerSettings` Spring memetakan `/oauth2/token` dan `/oauth2/jwks` ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)).) Pelayan akan mengeluarkan token akses JWT yang ditandatangani oleh kunci RSA di atas, dan menerbitkan kunci awamnya di `https://<your-app>:/oauth2/jwks`.

**Aktifkan penemuan OpenID Connect:** Untuk membolehkan APIM secara automatik mengambil penerbit dan JWKS, aktifkan titik akhir konfigurasi penyedia OIDC dengan menambah `.oidc(Customizer.withDefaults())` dalam konfigurasi keselamatan anda ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)). Contohnya:

```java
http
  .apply(authzServer.and())
  .securityMatcher(authzServer.getEndpointsMatcher())
  .with(authzServer, authz -> authz
      .oidc(Customizer.withDefaults()));  // <– enables /.well-known/openid-configuration
```

Ini mendedahkan `/.well-known/openid-configuration`, yang boleh digunakan APIM untuk metadata. Akhir sekali, anda mungkin ingin menyesuaikan tuntutan **audience** JWT supaya semakan `<audiences>` APIM lulus. Contohnya, tambah penyesuai token:

```java
@Bean
public OAuth2TokenCustomizer<OAuth2TokenClaimsContext> tokenCustomizer() {
    return context -> {
        // Set a custom audience (e.g. the client ID or API identifier)
        context.getClaims().audience(Collections.singletonList("mcp-client"));
    };
}
```

Ini memastikan token membawa `"aud": ["mcp-client"]`, sepadan dengan ID klien atau skop yang dijangka oleh APIM.

## Mendedahkan Titik Akhir Token dan JWKS

Selepas penyebaran, **URL penerbit** aplikasi anda akan menjadi `https://<app-fqdn>`, contohnya `https://my-mcp-app.eastus.azurecontainerapps.io`. Titik akhir OAuth2 adalah:

- **Titik akhir Token:** `https://<app-fqdn>/oauth2/token` – klien mendapatkan token di sini (aliran client_credentials).
- **Titik akhir JWKS:** `https://<app-fqdn>/oauth2/jwks` – mengembalikan set JWK (digunakan oleh APIM untuk mendapatkan kunci tandatangan).
- **Konfigurasi OpenID:** `https://<app-fqdn>/.well-known/openid-configuration` – JSON penemuan OIDC (mengandungi `issuer`, `token_endpoint`, `jwks_uri`, dan lain-lain).

APIM akan menunjuk ke **URL konfigurasi OpenID**, dari situ ia menemui `jwks_uri`. Contohnya, jika FQDN Container App anda ialah `my-mcp-app.eastus.azurecontainerapps.io`, maka `<openid-config url="...">` APIM harus menggunakan `https://my-mcp-app.eastus.azurecontainerapps.io/.well-known/openid-configuration`. (Secara lalai Spring akan menetapkan `issuer` dalam metadata itu ke URL asas yang sama ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)).)

## Mengkonfigurasi Azure API Management (`validate-jwt`)

Dalam Azure APIM, tambah polisi inbound yang menggunakan polisi `<validate-jwt>` untuk memeriksa JWT masuk terhadap Spring Authorization Server anda. Untuk tetapan mudah, anda boleh menggunakan URL metadata OpenID Connect. Contoh petikan polisi:

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

Polisi ini memberitahu APIM untuk mengambil konfigurasi OpenID dari Spring Auth Server, mendapatkan JWKS-nya, dan mengesahkan bahawa setiap token ditandatangani oleh kunci yang dipercayai dan mempunyai audience yang betul. (Jika anda tidak sertakan `<issuers>`, APIM akan menggunakan tuntutan `issuer` dari metadata secara automatik.) `<audience>` harus sepadan dengan ID klien atau pengecam sumber API dalam token (dalam contoh di atas, kami tetapkan kepada `"mcp-client"`). Ini selaras dengan dokumentasi Microsoft mengenai penggunaan `validate-jwt` dengan `<openid-config>` ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)).

Selepas pengesahan, APIM akan meneruskan permintaan (termasuk header `Authorization` asal) ke backend. Oleh kerana aplikasi Spring juga adalah pelayan sumber, ia akan mengesahkan semula token, tetapi APIM sudah memastikan kesahihannya. (Untuk pembangunan, anda boleh bergantung pada semakan APIM dan mematikan semakan tambahan dalam aplikasi jika mahu, tetapi lebih selamat untuk mengekalkan kedua-duanya.)

## Contoh Tetapan

| Tetapan            | Nilai Contoh                                                        | Nota                                      |
|--------------------|----------------------------------------------------------------------|--------------------------------------------|
| **Issuer**         | `https://my-mcp-app.eastus.azurecontainerapps.io`                    | URL Container App anda (URI asas)        |
| **Titik akhir Token** | `https://my-mcp-app.eastus.azurecontainerapps.io/oauth2/token`       | Titik akhir token Spring lalai ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize))  |
| **Titik akhir JWKS**  | `https://my-mcp-app.eastus.azurecontainerapps.io/oauth2/jwks`        | Titik akhir Set JWK lalai ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize))    |
| **Konfigurasi OpenID**  | `https://my-mcp-app.eastus.azurecontainerapps.io/.well-known/openid-configuration` | Dokumen penemuan OIDC (auto-generated)    |
| **Audience APIM**  | `mcp-client`                                                         | ID klien OAuth atau nama sumber API       |
| **Polisi APIM**    | `<openid-config url="https://.../.well-known/openid-configuration" />` | `<validate-jwt>` menggunakan URL ini ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)) |

## Kesilapan Lazim

- **HTTPS/TLS:** Pintu masuk APIM memerlukan titik akhir OpenID/JWKS menggunakan HTTPS dengan sijil yang sah. Secara lalai, Azure Container Apps menyediakan sijil TLS yang dipercayai untuk domain yang diurus Azure ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)). Jika anda menggunakan domain tersuai, pastikan anda pautkan sijil (anda boleh menggunakan ciri sijil terurus percuma Azure) ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)). Jika APIM tidak boleh mempercayai sijil titik akhir, `<validate-jwt>` akan gagal mengambil metadata.

- **Kebolehcapaian Titik Akhir:** Pastikan titik akhir aplikasi Spring boleh dicapai dari APIM. Menggunakan `--ingress external` (atau mengaktifkan ingress dalam portal) adalah paling mudah. Jika anda memilih persekitaran dalaman atau terikat vNet, APIM (secara lalai awam) mungkin tidak dapat mengaksesnya kecuali diletakkan dalam vNet yang sama. Dalam tetapan ujian, lebih baik gunakan ingress awam supaya APIM boleh memanggil URL `.well-known` dan `/jwks`.

- **Penemuan OpenID Diaktifkan:** Secara lalai, Spring Authorization Server **tidak mendedahkan** `/.well-known/openid-configuration` kecuali OIDC diaktifkan. Pastikan anda sertakan `.oidc(Customizer.withDefaults())` dalam konfigurasi keselamatan anda (lihat di atas) supaya titik akhir konfigurasi penyedia aktif ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)). Jika tidak, panggilan `<openid-config>` APIM akan mendapat ralat 404.

- **Tuntutan Audience:** Tingkah laku lalai Spring adalah menetapkan tuntutan `aud` kepada ID klien. Jika semakan `<audience>` APIM gagal, anda mungkin perlu sesuaikan token (seperti yang ditunjukkan di atas) atau laraskan polisi APIM. Pastikan audience dalam JWT anda sepadan dengan apa yang anda tetapkan dalam `<audience>`.

- **Parsing Metadata JSON:** Konfigurasi OpenID dalam bentuk JSON mesti sah. Konfigurasi lalai Spring akan mengeluarkan dokumen metadata OIDC standard. Sahkan ia mengandungi `issuer` dan `jwks_uri` yang betul. Jika anda menghoskan Spring di belakang proksi atau laluan berasaskan laluan, semak semula URL dalam metadata ini. APIM akan menggunakan nilai ini terus.

- **Susunan Polisi:** Dalam polisi APIM, letakkan `<validate-jwt>` **sebelum** sebarang penghalaan ke backend. Jika tidak, panggilan mungkin sampai ke aplikasi anda tanpa token yang sah. Juga pastikan `<validate-jwt>` muncul terus di bawah `<inbound>` (tidak bersarang dalam syarat lain) supaya APIM boleh melaksanakannya.

Dengan mengikuti langkah-langkah di atas, anda boleh menjalankan pelayan Spring AI MCP anda dalam Azure Container Apps dan membolehkan Azure API Management mengesahkan JWT OAuth2 yang masuk dengan polisi minimum. Perkara utama adalah: dedahkan titik akhir Spring Auth secara awam dengan TLS, aktifkan penemuan OIDC, dan tunjukkan `validate-jwt` APIM ke URL konfigurasi OpenID (supaya ia boleh mengambil JWKS secara automatik). Tetapan ini sesuai untuk persekitaran dev/test; untuk produksi, pertimbangkan pengurusan rahsia yang betul, jangka hayat token, dan putaran kunci dalam JWKS mengikut keperluan.
**Rujukan:** Lihat dokumen Spring Authorization Server untuk titik akhir lalai ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)) dan konfigurasi OIDC ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)); lihat dokumen Microsoft APIM untuk contoh `validate-jwt` ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)); dan dokumen Azure Container Apps untuk penyebaran dan sijil ([Deploy Java Spring Boot apps to Azure Container Apps - Java on Azure | Microsoft Learn](https://learn.microsoft.com/en-us/azure/developer/java/identity/deploy-spring-boot-to-azure-container-apps#:~:text=Now%20you%20can%20deploy%20your,CLI%20command)) ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)).

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil perhatian bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan profesional oleh manusia adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.