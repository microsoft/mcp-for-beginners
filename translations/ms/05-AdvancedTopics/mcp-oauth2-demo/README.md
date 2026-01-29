# MCP OAuth2 Demo

Projek ini adalah **aplikasi Spring Boot minimal** yang berfungsi sebagai:

* **Spring Authorization Server** (mengeluarkan token akses JWT melalui aliran `client_credentials`), dan  
* **Resource Server** (melindungi endpoint `/hello` sendiri).

Ia meniru tetapan yang ditunjukkan dalam [catatan blog Spring (2 Apr 2025)](https://spring.io/blog/2025/04/02/mcp-server-oauth2).

---

## Mula cepat (tempatan)

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

## Uji Konfigurasi OAuth2

Anda boleh menguji konfigurasi keselamatan OAuth2 dengan langkah berikut:

### 1. Sahkan server berjalan dan dilindungi

```bash
# This should return 401 Unauthorized, confirming OAuth2 security is active
curl -v http://localhost:8081/
```

### 2. Dapatkan token akses menggunakan kelayakan klien

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

Nota: Header Basic Authentication (`bWNwLWNsaWVudDpzZWNyZXQ=`) adalah pengekodan Base64 bagi `mcp-client:secret`.

### 3. Akses endpoint yang dilindungi menggunakan token

```bash
# Using the saved token
curl -H "Authorization: Bearer $(cat token.txt)" http://localhost:8081/hello

# Or directly with the token value
curl -H "Authorization: Bearer eyJra...token_value...xyz" http://localhost:8081/hello
```

Respons berjaya dengan "Hello from MCP OAuth2 Demo!" mengesahkan bahawa konfigurasi OAuth2 berfungsi dengan betul.

---

## Bina kontena

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

FQDN ingress menjadi **issuer** anda (`https://<fqdn>`).  
Azure menyediakan sijil TLS yang dipercayai secara automatik untuk `*.azurecontainerapps.io`.

---

## Sambungkan ke **Azure API Management**

Tambah polisi inbound ini ke API anda:

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

APIM akan mengambil JWKS dan mengesahkan setiap permintaan.

---

## Apa seterusnya

- [5.4 Root contexts](../mcp-root-contexts/README.md)

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan profesional oleh manusia adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.