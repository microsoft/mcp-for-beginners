# Mendeploy Aplikasi Spring AI MCP ke Azure Container Apps

([Mengamankan server Spring AI MCP dengan OAuth2](https://spring.io/blog/2025/04/02/mcp-server-oauth2)) *Gambar: Server Spring AI MCP yang diamankan dengan Spring Authorization Server. Server mengeluarkan token akses ke klien dan memvalidasinya pada permintaan masuk (sumber: blog Spring) ([Mengamankan server Spring AI MCP dengan OAuth2](https://spring.io/blog/2025/04/02/mcp-server-oauth2#:~:text=,server%20with%20the%20MCP%20inspector)).* Untuk mendeploy server Spring MCP, bangun sebagai container dan gunakan Azure Container Apps dengan ingress eksternal. Misalnya, menggunakan Azure CLI Anda dapat menjalankan:

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

Ini membuat Container App yang dapat diakses publik dengan HTTPS diaktifkan (Azure mengeluarkan sertifikat TLS gratis untuk domain default `*.azurecontainerapps.io` ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements))). Output perintah mencakup FQDN aplikasi (misalnya `my-mcp-app.eastus.azurecontainerapps.io`), yang menjadi basis **issuer URL**. Pastikan ingress HTTP diaktifkan (seperti di atas) agar APIM dapat mengakses aplikasi. Dalam pengaturan test/dev, gunakan opsi `--ingress external` (atau tautkan domain kustom dengan TLS sesuai [dokumentasi Microsoft](https://learn.microsoft.com/azure/container-apps/custom-domains-managed-certificates) ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements))). Simpan properti sensitif (seperti rahasia klien OAuth) di Container Apps secrets atau Azure Key Vault, dan peta-kan ke dalam container sebagai variabel lingkungan.

## Mengonfigurasi Spring Authorization Server

Dalam kode aplikasi Spring Boot Anda, sertakan starter Spring Authorization Server dan Resource Server. Konfigurasikan `RegisteredClient` (untuk grant `client_credentials` di dev/test) dan sumber kunci JWT. Misalnya, di `application.properties` Anda bisa mengatur:

```properties
# OAuth2 client (for testing token issuance)
spring.security.oauth2.authorizationserver.client.oidc-client.registration.client-id=mcp-client
spring.security.oauth2.authorizationserver.client.oidc-client.registration.client-secret={noop}secret
spring.security.oauth2.authorizationserver.client.oidc-client.registration.authorization-grant-types=client_credentials
spring.security.oauth2.authorizationserver.client.oidc-client.registration.client-authentication-methods=client_secret_basic
```

Aktifkan Authorization Server dan Resource Server dengan mendefinisikan security filter chain. Contohnya:

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

Pengaturan ini akan mengekspos endpoint OAuth2 default: `/oauth2/token` untuk token dan `/oauth2/jwks` untuk JSON Web Key Set. (Secara default, `AuthorizationServerSettings` Spring memetakan `/oauth2/token` dan `/oauth2/jwks` ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)).) Server akan mengeluarkan token akses JWT yang ditandatangani dengan kunci RSA di atas, dan mempublikasikan kunci publiknya di `https://<your-app>:/oauth2/jwks`.

**Aktifkan OpenID Connect discovery:** Agar APIM dapat secara otomatis mengambil issuer dan JWKS, aktifkan endpoint konfigurasi penyedia OIDC dengan menambahkan `.oidc(Customizer.withDefaults())` dalam konfigurasi keamanan Anda ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)). Contohnya:

```java
http
  .apply(authzServer.and())
  .securityMatcher(authzServer.getEndpointsMatcher())
  .with(authzServer, authz -> authz
      .oidc(Customizer.withDefaults()));  // <– enables /.well-known/openid-configuration
```

Ini mengekspos `/.well-known/openid-configuration`, yang dapat digunakan APIM untuk metadata. Terakhir, Anda mungkin ingin menyesuaikan klaim **audience** JWT agar pemeriksaan `<audiences>` APIM berhasil. Misalnya, tambahkan token customizer:

```java
@Bean
public OAuth2TokenCustomizer<OAuth2TokenClaimsContext> tokenCustomizer() {
    return context -> {
        // Set a custom audience (e.g. the client ID or API identifier)
        context.getClaims().audience(Collections.singletonList("mcp-client"));
    };
}
```

Ini memastikan token membawa `"aud": ["mcp-client"]`, yang sesuai dengan client ID atau scope yang diharapkan oleh APIM.

## Mengekspos Endpoint Token dan JWKS

Setelah dideploy, **issuer URL** aplikasi Anda akan menjadi `https://<app-fqdn>`, misalnya `https://my-mcp-app.eastus.azurecontainerapps.io`. Endpoint OAuth2-nya adalah:

- **Token endpoint:** `https://<app-fqdn>/oauth2/token` – klien mendapatkan token di sini (flow client_credentials).
- **JWKS endpoint:** `https://<app-fqdn>/oauth2/jwks` – mengembalikan set JWK (digunakan APIM untuk mendapatkan kunci tanda tangan).
- **OpenID Config:** `https://<app-fqdn>/.well-known/openid-configuration` – JSON OIDC discovery (berisi `issuer`, `token_endpoint`, `jwks_uri`, dll.).

APIM akan mengarah ke **OpenID configuration URL**, dari situ ia menemukan `jwks_uri`. Misalnya, jika FQDN Container App Anda adalah `my-mcp-app.eastus.azurecontainerapps.io`, maka `<openid-config url="...">` APIM harus menggunakan `https://my-mcp-app.eastus.azurecontainerapps.io/.well-known/openid-configuration`. (Secara default Spring akan mengatur `issuer` dalam metadata tersebut ke URL dasar yang sama ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)).)

## Mengonfigurasi Azure API Management (`validate-jwt`)

Di Azure APIM, tambahkan kebijakan inbound yang menggunakan kebijakan `<validate-jwt>` untuk memeriksa JWT yang masuk terhadap Spring Authorization Server Anda. Untuk pengaturan sederhana, Anda dapat menggunakan URL metadata OpenID Connect. Contoh potongan kebijakan:

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

Kebijakan ini memberitahu APIM untuk mengambil konfigurasi OpenID dari Spring Auth Server, mengambil JWKS-nya, dan memvalidasi bahwa setiap token ditandatangani oleh kunci yang dipercaya dan memiliki audience yang benar. (Jika Anda menghilangkan `<issuers>`, APIM akan otomatis menggunakan klaim `issuer` dari metadata.) `<audience>` harus sesuai dengan client ID atau identifier sumber daya API dalam token (dalam contoh di atas, kami mengaturnya ke `"mcp-client"`). Ini konsisten dengan dokumentasi Microsoft tentang penggunaan `validate-jwt` dengan `<openid-config>` ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)).

Setelah validasi, APIM akan meneruskan permintaan (termasuk header `Authorization` asli) ke backend. Karena aplikasi Spring juga merupakan resource server, ia akan memvalidasi ulang token, tetapi APIM sudah memastikan validitasnya. (Untuk pengembangan, Anda bisa mengandalkan pemeriksaan APIM dan menonaktifkan pemeriksaan tambahan di aplikasi jika diinginkan, tapi lebih aman mempertahankan keduanya.)

## Contoh Pengaturan

| Pengaturan          | Contoh Nilai                                                        | Catatan                                    |
|---------------------|--------------------------------------------------------------------|--------------------------------------------|
| **Issuer**          | `https://my-mcp-app.eastus.azurecontainerapps.io`                  | URL Container App Anda (base URI)          |
| **Token endpoint**  | `https://my-mcp-app.eastus.azurecontainerapps.io/oauth2/token`     | Endpoint token default Spring ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize))  |
| **JWKS endpoint**   | `https://my-mcp-app.eastus.azurecontainerapps.io/oauth2/jwks`      | Endpoint JWK Set default ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize))    |
| **OpenID Config**   | `https://my-mcp-app.eastus.azurecontainerapps.io/.well-known/openid-configuration` | Dokumen discovery OIDC (otomatis dibuat)  |
| **APIM audience**   | `mcp-client`                                                       | OAuth client ID atau nama resource API     |
| **APIM policy**     | `<openid-config url="https://.../.well-known/openid-configuration" />` | `<validate-jwt>` menggunakan URL ini ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)) |

## Kesalahan Umum

- **HTTPS/TLS:** Gateway APIM mengharuskan endpoint OpenID/JWKS menggunakan HTTPS dengan sertifikat yang valid. Secara default, Azure Container Apps menyediakan sertifikat TLS terpercaya untuk domain yang dikelola Azure ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)). Jika Anda menggunakan domain kustom, pastikan untuk mengikat sertifikat (Anda bisa menggunakan fitur sertifikat terkelola gratis Azure) ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)). Jika APIM tidak dapat mempercayai sertifikat endpoint, `<validate-jwt>` akan gagal mengambil metadata.

- **Aksesibilitas Endpoint:** Pastikan endpoint aplikasi Spring dapat dijangkau dari APIM. Menggunakan `--ingress external` (atau mengaktifkan ingress di portal) adalah cara termudah. Jika Anda memilih lingkungan internal atau terikat vNet, APIM (yang secara default publik) mungkin tidak dapat mengaksesnya kecuali ditempatkan di vNet yang sama. Dalam pengaturan test, lebih baik menggunakan ingress publik agar APIM dapat memanggil URL `.well-known` dan `/jwks`.

- **OpenID Discovery Diaktifkan:** Secara default, Spring Authorization Server **tidak mengekspos** `/.well-known/openid-configuration` kecuali OIDC diaktifkan. Pastikan untuk menyertakan `.oidc(Customizer.withDefaults())` dalam konfigurasi keamanan Anda (lihat di atas) agar endpoint konfigurasi penyedia aktif ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)). Jika tidak, panggilan `<openid-config>` APIM akan menghasilkan 404.

- **Klaim Audience:** Perilaku default Spring adalah mengatur klaim `aud` ke client ID. Jika pemeriksaan `<audience>` APIM gagal, Anda mungkin perlu menyesuaikan token (seperti yang ditunjukkan di atas) atau mengubah kebijakan APIM. Pastikan audience dalam JWT Anda sesuai dengan yang dikonfigurasi di `<audience>`.

- **Parsing Metadata JSON:** JSON konfigurasi OpenID harus valid. Konfigurasi default Spring akan menghasilkan dokumen metadata OIDC standar. Verifikasi bahwa dokumen tersebut berisi `issuer` dan `jwks_uri` yang benar. Jika Anda menempatkan Spring di balik proxy atau rute berbasis path, periksa ulang URL dalam metadata ini. APIM akan menggunakan nilai tersebut apa adanya.

- **Urutan Kebijakan:** Dalam kebijakan APIM, tempatkan `<validate-jwt>` **sebelum** routing ke backend. Jika tidak, panggilan bisa sampai ke aplikasi tanpa token yang valid. Pastikan juga `<validate-jwt>` muncul langsung di bawah `<inbound>` (tidak bersarang dalam kondisi lain) agar APIM menerapkannya.

Dengan mengikuti langkah-langkah di atas, Anda dapat menjalankan server Spring AI MCP di Azure Container Apps dan membuat Azure API Management memvalidasi JWT OAuth2 yang masuk dengan kebijakan minimal. Poin utama adalah: mengekspos endpoint Spring Auth secara publik dengan TLS, mengaktifkan discovery OIDC, dan mengarahkan `validate-jwt` APIM ke URL konfigurasi OpenID (agar dapat mengambil JWKS secara otomatis). Pengaturan ini cocok untuk lingkungan dev/test; untuk produksi, pertimbangkan manajemen rahasia yang tepat, masa berlaku token, dan rotasi kunci di JWKS sesuai kebutuhan.
**Referensi:** Lihat dokumen Spring Authorization Server untuk endpoint default ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)) dan konfigurasi OIDC ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)); lihat dokumen Microsoft APIM untuk contoh `validate-jwt` ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)); dan dokumen Azure Container Apps untuk deployment dan sertifikat ([Deploy Java Spring Boot apps to Azure Container Apps - Java on Azure | Microsoft Learn](https://learn.microsoft.com/en-us/azure/developer/java/identity/deploy-spring-boot-to-azure-container-apps#:~:text=Now%20you%20can%20deploy%20your,CLI%20command)) ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)).

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk akurasi, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sah. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.