# MCP OAuth2 Demo

Proyek ini adalah **aplikasi Spring Boot minimal** yang berfungsi sebagai:

* **Spring Authorization Server** (mengeluarkan token akses JWT melalui flow `client_credentials`), dan  
* **Resource Server** (melindungi endpoint `/hello` miliknya sendiri).

Ini mencerminkan pengaturan yang ditunjukkan dalam [posting blog Spring (2 Apr 2025)](https://spring.io/blog/2025/04/02/mcp-server-oauth2).

---

## Mulai cepat (lokal)

```bash
# build & run
./mvnw spring-boot:run

# obtain a token
curl -u mcp-client:secret -d grant_type=client_credentials \
     http://localhost:8081/oauth2/token | jq -r .access_token > token.txt

# call the protected endpoint
curl -H "Authorization: Bearer $(cat token.txt)" http://localhost:8081/hello
```

---

## Menguji Konfigurasi OAuth2

Anda dapat menguji konfigurasi keamanan OAuth2 dengan langkah-langkah berikut:

### 1. Pastikan server berjalan dan terlindungi

```bash
# This should return 401 Unauthorized, confirming OAuth2 security is active
curl -v http://localhost:8081/
```

### 2. Dapatkan token akses menggunakan client credentials

```bash
# Get and extract the full token response
curl -v -X POST http://localhost:8081/oauth2/token \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -H "Authorization: Basic bWNwLWNsaWVudDpzZWNyZXQ=" \
  -d "grant_type=client_credentials&scope=mcp.access"

# Or to extract just the token (requires jq)
curl -s -X POST http://localhost:8081/oauth2/token \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -H "Authorization: Basic bWNwLWNsaWVudDpzZWNyZXQ=" \
  -d "grant_type=client_credentials&scope=mcp.access" | jq -r .access_token > token.txt
```

Catatan: Header Basic Authentication (`bWNwLWNsaWVudDpzZWNyZXQ=`) adalah encoding Base64 dari `mcp-client:secret`.

### 3. Akses endpoint yang dilindungi menggunakan token

```bash
# Using the saved token
curl -H "Authorization: Bearer $(cat token.txt)" http://localhost:8081/hello

# Or directly with the token value
curl -H "Authorization: Bearer eyJra...token_value...xyz" http://localhost:8081/hello
```

Respon berhasil dengan "Hello from MCP OAuth2 Demo!" menandakan konfigurasi OAuth2 berfungsi dengan benar.

---

## Build container

```bash
docker build -t mcp-oauth2-demo .
docker run -p 8081:8081 mcp-oauth2-demo
```

---

## Deploy ke **Azure Container Apps**

```bash
az containerapp up -n mcp-oauth2 \
  -g demo-rg -l westeurope \
  --image <your-registry>/mcp-oauth2-demo:latest \
  --ingress external --target-port 8081
```

Ingress FQDN menjadi **issuer** Anda (`https://<fqdn>`).  
Azure secara otomatis menyediakan sertifikat TLS terpercaya untuk `*.azurecontainerapps.io`.

---

## Integrasi dengan **Azure API Management**

Tambahkan kebijakan inbound ini ke API Anda:

```xml
<inbound>
  <validate-jwt header-name="Authorization">
    <openid-config url="https://<fqdn>/.well-known/openid-configuration"/>
    <audiences>
      <audience>mcp-client</audience>
    </audiences>
  </validate-jwt>
  <base/>
</inbound>
```

APIM akan mengambil JWKS dan memvalidasi setiap permintaan.

---

## Selanjutnya

- [5.4 Root contexts](../mcp-root-contexts/README.md)

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk mencapai akurasi, harap diingat bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sahih. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.