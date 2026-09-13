# Menyebarkan Aplikasi Spring AI MCP ke Azure Container Apps

> [!WARNING]
> Pelayan gabungan kebenaran/sumber ini bertujuan untuk pembelajaran dan
> penggunaan pembangunan/ujian. Sistem pengeluaran harus menggunakan penyedia identiti khusus,
> kunci tandatangan yang berterusan, dan kelayakan yang disimpan dalam stor rahsia yang diurus.

 ([Melindungi pelayan Spring AI MCP dengan OAuth2](https://spring.io/blog/2025/04/02/mcp-server-oauth2)) *Rajah: Pelayan Spring AI MCP dilindungi dengan Spring Authorization Server. Pelayan mengeluarkan token akses kepada klien dan mengesahkannya pada permintaan masuk (sumber: blog Spring) ([Melindungi pelayan Spring AI MCP dengan OAuth2](https://spring.io/blog/2025/04/02/mcp-server-oauth2#:~:text=,server%20with%20the%20MCP%20inspector)).* Untuk menyebarkan pelayan Spring MCP, bina ia sebagai bekas dan gunakan Azure Container Apps dengan ingress luaran. Sebagai contoh, menggunakan Azure CLI anda boleh jalankan:

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

Ini menghasilkan Aplikasi Bekas yang boleh diakses secara umum dengan HTTPS diaktifkan (Azure mengeluarkan sijil TLS percuma untuk domain lalai `*.azurecontainerapps.io` ([Nama domain tersuai dan sijil yang diurus percuma dalam Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements))). Output arahan termasuk FQDN aplikasi (contoh `my-mcp-app.eastus.azurecontainerapps.io`), yang menjadi asas **URL penerbit**. Pastikan ingress HTTP diaktifkan (seperti di atas) supaya APIM dapat mencapai aplikasi. Dalam setup ujian/pembangunan, gunakan pilihan `--ingress external` (atau pautkan domain tersuai dengan TLS mengikut [dokumen Microsoft](https://learn.microsoft.com/azure/container-apps/custom-domains-managed-certificates) ([Nama domain tersuai dan sijil yang diurus percuma dalam Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements))). Simpan mana-mana sifat sensitif (seperti rahsia klien OAuth) dalam rahsia Container Apps atau Azure Key Vault, dan mapkannya ke dalam bekas sebagai pembolehubah persekitaran. 

## Mengkonfigurasi Spring Authorization Server

Dalam kod aplikasi Spring Boot anda, sertakan permulaan Spring Authorization Server dan Resource Server. Konfigurasikan `RegisteredClient` (untuk pemberian `client_credentials` dalam dev/test) dan sumber kunci JWT. Sebagai contoh, dalam `application.properties` anda boleh menetapkan:

```properties
# OAuth2 client (for testing token issuance)
demo.oauth.client-id=${OAUTH_CLIENT_ID:mcp-client}
demo.oauth.client-secret=${OAUTH_CLIENT_SECRET}
```

Hidupkan Authorization Server dan Resource Server dengan mendefinisikan rantai penapis keselamatan. Sebagai contoh:

```java
@Configuration
@EnableWebSecurity
public class SecurityConfiguration {

    @Bean
    SecurityFilterChain securityFilterChain(HttpSecurity http) throws Exception {
        OAuth2AuthorizationServerConfigurer<HttpSecurity> authzServer = OAuth2AuthorizationServerConfigurer.authorizationServer();
        http
            .authorizeHttpRequests(auth -> auth.anyRequest().authenticated())
            // Hidupkan endpoint Authorization Server
            .apply(authzServer.and())
            // Hidupkan Resource Server (sahkan JWT pada permintaan masuk)
            .oauth2ResourceServer(oauth2 -> oauth2.jwt(withDefaults()))
            // Matikan CSRF (server MCP bukan berasaskan pelayar)
            .csrf(csrf -> csrf.disable())
            // Benarkan CORS untuk alat demo klien
            .cors(withDefaults());
        return http.build();
    }

    // Tetapkan klien dalam memori (RegisteredClient) dan sumber JWK:
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
        // Jana kekunci RSA (untuk dev/test, jana semula semasa permulaan)
        RSAKey rsaKey = new RSAKeyGenerator(2048).keyID("1").generate();
        JWKSet jwkSet = new JWKSet(rsaKey);
        return (selector, context) -> selector.select(jwkSet);
    }
}
```

Setup ini akan mendedahkan endpoint OAuth2 lalai: `/oauth2/token` untuk token dan `/oauth2/jwks` untuk Set Kunci Web JSON. (Secara lalai `AuthorizationServerSettings` Spring memetakan `/oauth2/token` dan `/oauth2/jwks` ([Model Konfigurasi :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)).) Pelayan akan mengeluarkan token akses JWT yang ditandatangani dengan kunci RSA di atas, dan menerbitkan kunci awamnya di `https://<your-app>:/oauth2/jwks`. 

**Hidupkan penemuan OpenID Connect:** Untuk membolehkan APIM secara automatik mengambil penerbit dan JWKS, hidupkan endpoint konfigurasi penyedia OIDC dengan menambah `.oidc(Customizer.withDefaults())` dalam konfigurasi keselamatan anda ([Model Konfigurasi :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)). Sebagai contoh:

```java
http
  .apply(authzServer.and())
  .securityMatcher(authzServer.getEndpointsMatcher())
  .with(authzServer, authz -> authz
      .oidc(Customizer.withDefaults()));  // <– mengaktifkan /.well-known/openid-configuration
```

Ini mendedahkan `/.well-known/openid-configuration`, yang boleh digunakan APIM untuk metadata. Akhir sekali, anda mungkin mahu menyesuaikan tuntutan **audience** JWT supaya pemeriksaan `<audiences>` APIM akan lulus. Sebagai contoh, tambah penyesuai token:

```java
@Bean
public OAuth2TokenCustomizer<OAuth2TokenClaimsContext> tokenCustomizer() {
    return context -> {
        // Tetapkan penonton tersuai (contoh ID klien atau pengecam API)
        context.getClaims().audience(Collections.singletonList("mcp-client"));
    };
}
```

Ini memastikan token membawa `"aud": ["mcp-client"]`, sepadan dengan ID klien atau skop yang dijangka oleh APIM. 

## Mendedahkan Endpoint Token dan JWKS

Selepas penyebaran, **URL penerbit** aplikasi anda akan menjadi `https://<app-fqdn>`, contohnya `https://my-mcp-app.eastus.azurecontainerapps.io`. Endpoint OAuth2nya adalah:

- **Endpoint Token:** `https://<app-fqdn>/oauth2/token` – klien mendapat token di sini (aliran client_credentials).
- **Endpoint JWKS:** `https://<app-fqdn>/oauth2/jwks` – mengembalikan set JWK (digunakan oleh APIM untuk mendapatkan kunci tandatangan).
- **Konfigurasi OpenID:** `https://<app-fqdn>/.well-known/openid-configuration` – JSON penemuan OIDC (mengandungi `issuer`, `token_endpoint`, `jwks_uri`, dll.).  

APIM akan menunjuk ke **URL konfigurasi OpenID**, dari situ ia menemui `jwks_uri`. Contohnya, jika FQDN Container App anda adalah `my-mcp-app.eastus.azurecontainerapps.io`, maka `<openid-config url="...">` APIM harus menggunakan `https://my-mcp-app.eastus.azurecontainerapps.io/.well-known/openid-configuration`. (Secara lalai Spring akan menetapkan `issuer` dalam metadata tersebut kepada URL asas yang sama ([Model Konfigurasi :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)).)

## Mengkonfigurasi Azure API Management (`validate-jwt`)

Dalam Azure APIM, tambah dasar inbound yang menggunakan dasar `<validate-jwt>` untuk memeriksa JWT masuk terhadap Spring Authorization Server anda. Untuk setup ringkas, anda boleh menggunakan URL metadata OpenID Connect. Contoh petikan dasar:

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

Dasar ini memberitahu APIM untuk mengambil konfigurasi OpenID dari Spring Auth Server, mendapatkan JWKSnya, dan mengesahkan bahawa setiap token ditandatangani oleh kunci yang dipercayai dan mempunyai audience yang betul. (Jika anda tidak sertakan `<issuers>`, APIM akan menggunakan tuntutan `issuer` dari metadata secara automatik.) `<audience>` harus sepadan dengan ID klien atau pengenalpasti sumber API dalam token (dalam contoh di atas, kami menetapkannya kepada `"mcp-client"`). Ini sejajar dengan dokumentasi Microsoft mengenai penggunaan `validate-jwt` dengan `<openid-config>` ([Rujukan dasar Azure API Management - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)).

Selepas pengesahan, APIM akan meneruskan permintaan (termasuk tajuk `Authorization` asal) kepada backend. Oleh kerana aplikasi Spring juga merupakan pelayan sumber, ia akan mengesahkan semula token, tetapi APIM telah memastikan kesahihannya terlebih dahulu. (Untuk pembangunan, anda boleh bergantung pada pemeriksaan APIM dan mematikan pemeriksaan tambahan dalam aplikasi jika dikehendaki, tetapi lebih selamat untuk mengekalkan kedua-duanya.)

## Contoh Tetapan

| Tetapan           | Nilai Contoh                                                       | Nota                                       |
|-------------------|--------------------------------------------------------------------|--------------------------------------------|
| **Penerbit**      | `https://my-mcp-app.eastus.azurecontainerapps.io`                  | URL aplikasi Container App anda (URI asas)|
| **Endpoint Token**| `https://my-mcp-app.eastus.azurecontainerapps.io/oauth2/token`     | Endpoint token Spring lalai ([Model Konfigurasi :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize))  |
| **Endpoint JWKS** | `https://my-mcp-app.eastus.azurecontainerapps.io/oauth2/jwks`      | Endpoint Set JWK lalai ([Model Konfigurasi :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize))    |
| **Konfigurasi OpenID** | `https://my-mcp-app.eastus.azurecontainerapps.io/.well-known/openid-configuration` | Dokumen penemuan OIDC (auto-dihasilkan)    |
| **Audience APIM** | `mcp-client`                                                      | ID klien OAuth atau nama sumber API         |
| **Dasar APIM**    | `<openid-config url="https://.../.well-known/openid-configuration" />` | `<validate-jwt>` menggunakan URL ini ([Rujukan Dasar Azure API Management - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)) |

## Kesilapan Biasa

- **HTTPS/TLS:** Gateway APIM menghendaki endpoint OpenID/JWKS menggunakan HTTPS dengan sijil yang sah. Secara lalai, Azure Container Apps menyediakan sijil TLS yang dipercayai untuk domain yang diurus Azure ([Nama domain tersuai dan sijil yang diurus percuma dalam Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)). Jika anda menggunakan domain tersuai, pastikan anda pautkan sijil (anda boleh menggunakan ciri sijil yang diurus percuma Azure) ([Nama domain tersuai dan sijil yang diurus percuma dalam Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)). Jika APIM tidak boleh mempercayai sijil endpoint, `<validate-jwt>` akan gagal mendapatkan metadata.  

- **Kebolehcapaian Endpoint:** Pastikan endpoint aplikasi Spring boleh dicapai dari APIM. Menggunakan `--ingress external` (atau mengaktifkan ingress di portal) adalah paling mudah. Jika anda memilih persekitaran dalaman atau terikat vNet, APIM (yang secara lalai awam) mungkin tidak dapat menjangka kecuali ia diletakkan dalam VNet yang sama. Dalam setup ujian, utamakan ingress awam supaya APIM dapat memanggil URL `.well-known` dan `/jwks`. 

- **Penemuan OpenID Diaktifkan:** Secara lalai, Spring Authorization Server **tidak mendedahkan** `/.well-known/openid-configuration` melainkan OIDC diaktifkan. Pastikan anda sertakan `.oidc(Customizer.withDefaults())` dalam konfigurasi keselamatan anda (lihat di atas) supaya endpoint konfigurasi penyedia aktif ([Model Konfigurasi :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)). Jika tidak, panggilan `<openid-config>` APIM akan memaparkan 404.

- **Tuntutan Audience:** Tingkah laku lalai Spring ialah menetapkan tuntutan `aud` kepada ID klien. Jika pemeriksaan `<audience>` oleh APIM gagal, anda mungkin perlu menyesuaikan token (seperti yang ditunjukkan di atas) atau laraskan dasar APIM. Pastikan audience dalam JWT anda sepadan dengan apa yang anda konfigurasikan dalam `<audience>`. 

- **Parsing Metadata JSON:** Konfigurasi OpenID perlu sah. Konfigurasi lalai Spring akan mengeluarkan dokumen metadata OIDC standard. Sahkan ia mengandungi `issuer` dan `jwks_uri` yang betul. Jika anda menghoskan Spring di belakang proksi atau laluan berasaskan laluan, semak URL dalam metadata ini. APIM akan menggunakan nilai ini seperti adanya. 

- **Urutan Dasar:** Dalam dasar APIM, letakkan `<validate-jwt>` **sebelum** apa-apa routing ke backend. Jika tidak, panggilan mungkin sampai ke aplikasi anda tanpa token yang sah. Juga pastikan `<validate-jwt>` muncul terus di bawah `<inbound>` (tidak terbenam dalam syarat lain) supaya APIM boleh mengaplikasikannya.

Dengan mengikuti langkah-langkah di atas, anda boleh menjalankan pelayan Spring AI MCP dalam Azure Container Apps dan membolehkan Azure API Management mengesahkan JWT OAuth2 masuk dengan dasar minimal. Titik utama adalah: dedahkan endpoint Spring Auth secara umum dengan TLS, aktifkan penemuan OIDC, dan arahkan `validate-jwt` APIM ke URL konfigurasi OpenID (supaya ia boleh mengambil JWKS secara automatik). Setup ini sesuai untuk persekitaran dev/test; untuk pengeluaran, pertimbangkan pengurusan rahsia yang betul, jangka hayat token, dan putaran kunci dalam JWKS jika perlu. 


**Rujukan:** Lihat dokumen Spring Authorization Server untuk titik akhir lalai ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)) dan konfigurasi OIDC ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)); lihat dokumen Microsoft APIM untuk contoh `validate-jwt` ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)); dan dokumen Azure Container Apps untuk penyebaran dan sijil ([Deploy Java Spring Boot apps to Azure Container Apps - Java on Azure | Microsoft Learn](https://learn.microsoft.com/en-us/azure/developer/java/identity/deploy-spring-boot-to-azure-container-apps#:~:text=Now%20you%20can%20deploy%20your,CLI%20command)) ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan oleh manusia profesional adalah disyorkan. Kami tidak bertanggungjawab terhadap sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->