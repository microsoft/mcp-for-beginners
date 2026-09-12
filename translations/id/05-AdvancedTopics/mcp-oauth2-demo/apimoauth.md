# Men-deploy Aplikasi Spring AI MCP ke Azure Container Apps

> [!WARNING]
> Server otorisasi/gabungan sumber daya ini dimaksudkan untuk digunakan dalam pembelajaran dan
> penggunaan dev/test. Sistem produksi harus menggunakan penyedia identitas khusus,
> kunci penandatanganan yang permanen, dan kredensial yang disimpan dalam penyimpanan rahasia terkelola.

 ([Mengamankan server Spring AI MCP dengan OAuth2](https://spring.io/blog/2025/04/02/mcp-server-oauth2)) *Gambar: Server Spring AI MCP diamankan dengan Spring Authorization Server. Server mengeluarkan token akses untuk klien dan memvalidasi token tersebut pada permintaan masuk (sumber: blog Spring) ([Mengamankan server Spring AI MCP dengan OAuth2](https://spring.io/blog/2025/04/02/mcp-server-oauth2#:~:text=,server%20with%20the%20MCP%20inspector)).* Untuk mendeply server Spring MCP, buat sebagai container dan gunakan Azure Container Apps dengan ingress eksternal. Sebagai contoh, menggunakan Azure CLI Anda dapat menjalankan:

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

Ini membuat Container App yang dapat diakses publik dengan HTTPS diaktifkan (Azure menyediakan sertifikat TLS gratis untuk domain default `*.azurecontainerapps.io` ([Nama domain kustom dan sertifikat dikelola gratis di Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements))). Output perintah mencakup FQDN aplikasi (misal `my-mcp-app.eastus.azurecontainerapps.io`), yang menjadi basis **URL issuer**. Pastikan ingress HTTP diaktifkan (seperti di atas) agar APIM dapat menjangkau aplikasi. Dalam setup test/dev, gunakan opsi `--ingress external` (atau pasangkan domain kustom dengan TLS sesuai [dokumentasi Microsoft](https://learn.microsoft.com/azure/container-apps/custom-domains-managed-certificates) ([Nama domain kustom dan sertifikat dikelola gratis di Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements))). Simpan properti sensitif (seperti rahasia klien OAuth) dalam rahasia Container Apps atau Azure Key Vault, dan petakan ke dalam container sebagai variabel lingkungan.

## Mengonfigurasi Spring Authorization Server

Di kode aplikasi Spring Boot Anda, sertakan starter Spring Authorization Server dan Resource Server. Konfigurasikan `RegisteredClient` (untuk grant `client_credentials` dalam dev/test) dan sumber kunci JWT. Misalnya, di `application.properties` Anda bisa mengatur:

```properties
# OAuth2 client (for testing token issuance)
demo.oauth.client-id=${OAUTH_CLIENT_ID:mcp-client}
demo.oauth.client-secret=${OAUTH_CLIENT_SECRET}
```

Aktifkan Authorization Server dan Resource Server dengan mendefinisikan rantai filter keamanan. Contohnya:

```java
@Configuration
@EnableWebSecurity
public class SecurityConfiguration {

    @Bean
    SecurityFilterChain securityFilterChain(HttpSecurity http) throws Exception {
        OAuth2AuthorizationServerConfigurer<HttpSecurity> authzServer = OAuth2AuthorizationServerConfigurer.authorizationServer();
        http
            .authorizeHttpRequests(auth -> auth.anyRequest().authenticated())
            // Aktifkan endpoint Server Otorisasi
            .apply(authzServer.and())
            // Aktifkan Server Sumber Daya (validasi JWT pada permintaan masuk)
            .oauth2ResourceServer(oauth2 -> oauth2.jwt(withDefaults()))
            // Nonaktifkan CSRF (server MCP bukan berbasis browser)
            .csrf(csrf -> csrf.disable())
            // Izinkan CORS untuk alat demo klien
            .cors(withDefaults());
        return http.build();
    }

    // Definisikan klien dalam memori (RegisteredClient) dan sumber JWK:
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
        // Buat kunci RSA (untuk dev/test, buat ulang saat startup)
        RSAKey rsaKey = new RSAKeyGenerator(2048).keyID("1").generate();
        JWKSet jwkSet = new JWKSet(rsaKey);
        return (selector, context) -> selector.select(jwkSet);
    }
}
```

Setup ini akan mengekspos endpoint OAuth2 default: `/oauth2/token` untuk token dan `/oauth2/jwks` untuk JSON Web Key Set. (Secara default `AuthorizationServerSettings` Spring memetakan `/oauth2/token` dan `/oauth2/jwks` ([Model Konfigurasi :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)).) Server akan mengeluarkan token akses JWT yang ditandatangani oleh kunci RSA di atas, dan mempublikasikan kunci publiknya di `https://<your-app>:/oauth2/jwks`.

**Aktifkan penemuan OpenID Connect:** Agar APIM secara otomatis mengambil issuer dan JWKS, aktifkan endpoint konfigurasi penyedia OIDC dengan menambahkan `.oidc(Customizer.withDefaults())` di konfigurasi keamanan Anda ([Model Konfigurasi :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)). Contohnya:

```java
http
  .apply(authzServer.and())
  .securityMatcher(authzServer.getEndpointsMatcher())
  .with(authzServer, authz -> authz
      .oidc(Customizer.withDefaults()));  // <– mengaktifkan /.well-known/openid-configuration
```

Ini mengekspos `/.well-known/openid-configuration`, yang bisa digunakan APIM untuk metadata. Terakhir, Anda mungkin ingin mempersonalisasi klaim **audience** JWT supaya pengecekan `<audiences>` APIM melewati. Misalnya, tambahkan kustomizer token:

```java
@Bean
public OAuth2TokenCustomizer<OAuth2TokenClaimsContext> tokenCustomizer() {
    return context -> {
        // Tetapkan audiens khusus (misalnya ID klien atau pengenal API)
        context.getClaims().audience(Collections.singletonList("mcp-client"));
    };
}
```

Ini memastikan token membawa `"aud": ["mcp-client"]`, cocok dengan client ID atau scope yang diharapkan APIM.

## Mengekspos Endpoint Token dan JWKS

Setelah deploy, **URL issuer** aplikasi Anda akan menjadi `https://<app-fqdn>`, misalnya `https://my-mcp-app.eastus.azurecontainerapps.io`. Endpoint OAuth2-nya adalah:

- **Endpoint Token:** `https://<app-fqdn>/oauth2/token` – klien memperoleh token di sini (flow client_credentials).
- **Endpoint JWKS:** `https://<app-fqdn>/oauth2/jwks` – mengembalikan set JWK (dipakai APIM untuk mendapatkan kunci tanda tangan).
- **Konfigurasi OpenID:** `https://<app-fqdn>/.well-known/openid-configuration` – JSON penemuan OIDC (berisi `issuer`, `token_endpoint`, `jwks_uri`, dll.).  

APIM akan mengarah ke **URL konfigurasi OpenID**, dari mana ia menemukan `jwks_uri`. Misalnya, jika FQDN Container App Anda adalah `my-mcp-app.eastus.azurecontainerapps.io`, maka `<openid-config url="...">` APIM harus menggunakan `https://my-mcp-app.eastus.azurecontainerapps.io/.well-known/openid-configuration`. (Spring secara default akan menetapkan `issuer` dalam metadata tersebut ke URL dasar yang sama ([Model Konfigurasi :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)).)

## Mengonfigurasi Azure API Management (`validate-jwt`)

Di Azure APIM, tambahkan kebijakan inbound yang menggunakan kebijakan `<validate-jwt>` untuk memeriksa JWT masuk terhadap Spring Authorization Server Anda. Untuk setup sederhana, Anda bisa menggunakan URL metadata OpenID Connect. Contoh cuplikan kebijakan:

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

Kebijakan ini memberitahu APIM untuk mengambil konfigurasi OpenID dari Spring Auth Server, mengambil JWKS-nya, dan memvalidasi bahwa setiap token ditandatangani oleh kunci terpercaya dan memiliki audience yang tepat. (Jika Anda menghilangkan `<issuers>`, APIM akan menggunakan klaim `issuer` dari metadata secara otomatis.) `<audience>` harus cocok dengan client ID atau identifier sumber daya API dalam token (dalam contoh di atas, kami mengaturnya ke `"mcp-client"`). Ini sesuai dengan dokumentasi Microsoft mengenai penggunaan `validate-jwt` dengan `<openid-config>` ([Referensi kebijakan Azure API Management - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)).

Setelah validasi, APIM akan meneruskan permintaan (termasuk header `Authorization` asli) ke backend. Karena aplikasi Spring juga resource server, ia akan memvalidasi ulang token, tetapi APIM sudah memastikan validitasnya. (Untuk pengembangan, Anda bisa mengandalkan pemeriksaan APIM dan menonaktifkan pemeriksaan tambahan di aplikasi jika diinginkan, tapi lebih aman menjaga keduanya.)

## Contoh Pengaturan

| Pengaturan          | Contoh Nilai                                                      | Catatan                                     |
|--------------------|----------------------------------------------------------------------|--------------------------------------------|
| **Issuer**         | `https://my-mcp-app.eastus.azurecontainerapps.io`                    | URL Container App Anda (URI dasar)         |
| **Endpoint token** | `https://my-mcp-app.eastus.azurecontainerapps.io/oauth2/token`       | Endpoint token Spring default ([Model Konfigurasi :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize))  |
| **Endpoint JWKS**  | `https://my-mcp-app.eastus.azurecontainerapps.io/oauth2/jwks`        | Endpoint JWK Set default ([Model Konfigurasi :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize))    |
| **Konfigurasi OpenID**  | `https://my-mcp-app.eastus.azurecontainerapps.io/.well-known/openid-configuration` | Dokumen penemuan OIDC (hasil auto)          |
| **Audience APIM**  | `mcp-client`                                                         | ID klien OAuth atau nama sumber daya API   |
| **Kebijakan APIM** | `<openid-config url="https://.../.well-known/openid-configuration" />` | `<validate-jwt>` menggunakan URL ini ([Referensi kebijakan Azure API Management - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)) |

## Kesalahan Umum

- **HTTPS/TLS:** Gateway APIM mengharuskan endpoint OpenID/JWKS menggunakan HTTPS dengan sertifikat valid. Secara default, Azure Container Apps menyediakan sertifikat TLS yang dipercaya untuk domain yang dikelola Azure ([Nama domain kustom dan sertifikat dikelola gratis di Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)). Jika Anda menggunakan domain kustom, pastikan untuk memasangkan sertifikat (Anda dapat menggunakan fitur sertifikat terkelola gratis Azure) ([Nama domain kustom dan sertifikat dikelola gratis di Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)). Jika APIM tidak dapat mempercayai sertifikat endpoint, `<validate-jwt>` akan gagal mengambil metadata.  

- **Keterjangkauan Endpoint:** Pastikan endpoint aplikasi Spring dapat dijangkau dari APIM. Menggunakan `--ingress external` (atau mengaktifkan ingress di portal) adalah yang paling sederhana. Jika Anda memilih lingkungan internal atau yang terikat vNet, APIM (secara default publik) mungkin tidak dapat menjangkaunya kecuali ditempatkan di vNet yang sama. Dalam setup pengujian, sebaiknya gunakan ingress publik agar APIM dapat mengakses URL `.well-known` dan `/jwks`.

- **Penemuan OpenID Diaktifkan:** Secara default, Spring Authorization Server **tidak mengekspos** `/.well-known/openid-configuration` kecuali OIDC diaktifkan. Pastikan untuk menyertakan `.oidc(Customizer.withDefaults())` dalam konfigurasi keamanan Anda (lihat di atas) sehingga endpoint konfigurasi penyedia aktif ([Model Konfigurasi :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)). Jika tidak, panggilan `<openid-config>` APIM akan menghasilkan 404.

- **Klaim Audience:** Perilaku default Spring adalah menetapkan klaim `aud` ke client ID. Jika pengecekan `<audience>` APIM gagal, Anda mungkin perlu mempersonalisasi token (seperti yang ditunjukkan di atas) atau menyesuaikan kebijakan APIM. Pastikan audience dalam JWT Anda sesuai dengan konfigurasi di `<audience>`.

- **Parsing Metadata JSON:** Konfigurasi OpenID berupa JSON harus valid. Konfigurasi default Spring akan mengeluarkan dokumen metadata OIDC standar. Verifikasi bahwa dokumen tersebut berisi `issuer` dan `jwks_uri` yang benar. Jika Anda menaruh Spring di balik proxy atau route berbasis path, periksa kembali URL dalam metadata ini. APIM akan menggunakan nilai-nilai ini apa adanya.

- **Urutan Kebijakan:** Dalam kebijakan APIM, tempatkan `<validate-jwt>` **sebelum** routing apapun ke backend. Jika tidak, panggilan bisa sampai ke aplikasi Anda tanpa token valid. Juga pastikan `<validate-jwt>` muncul tepat di bawah `<inbound>` (tidak bersarang dalam kondisi lain) agar APIM menerapkannya dengan benar.

Dengan mengikuti langkah-langkah di atas, Anda dapat menjalankan server Spring AI MCP di Azure Container Apps dan menggunakan Azure API Management untuk memvalidasi JWT OAuth2 masuk dengan kebijakan minimal. Poin utamanya adalah: mengekspos endpoint Spring Auth secara publik dengan TLS, mengaktifkan penemuan OIDC, dan mengarahkan `validate-jwt` APIM ke URL konfigurasi OpenID (agar secara otomatis dapat mengambil JWKS). Setup ini cocok untuk lingkungan dev/test; untuk produksi, pertimbangkan manajemen rahasia yang tepat, masa berlaku token, dan rotasi kunci di JWKS sesuai kebutuhan.


**Referensi:** Lihat dokumen Spring Authorization Server untuk endpoint default ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)) dan konfigurasi OIDC ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)); lihat dokumen Microsoft APIM untuk contoh `validate-jwt` ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)); dan dokumen Azure Container Apps untuk deployment dan sertifikat ([Deploy Java Spring Boot apps to Azure Container Apps - Java on Azure | Microsoft Learn](https://learn.microsoft.com/en-us/azure/developer/java/identity/deploy-spring-boot-to-azure-container-apps#:~:text=Now%20you%20can%20deploy%20your,CLI%20command)) ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk mencapai akurasi, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sah. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->