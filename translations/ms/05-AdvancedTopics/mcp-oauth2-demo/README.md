# Demo MCP OAuth2

> [!WARNING]
> Ini adalah contoh pembelajaran tempatan, bukan perkhidmatan kebenaran produksi. Ia
> menggunakan klien dalam memori dan menjana kunci tandatangan baru semasa mula. Jangan
> sekali-kali mengerahkan dengan rahsia klien yang dikongsi, lalai, atau dikawal versi.

## Pengenalan

OAuth2 adalah protokol piawai industri untuk kebenaran, membolehkan akses selamat kepada sumber tanpa berkongsi kelayakan. Dalam pelaksanaan MCP (Protokol Konteks Model), OAuth2 menyediakan cara yang kukuh untuk mengesahkan dan memberi kebenaran kepada klien (seperti agen AI) mengakses pelayan MCP dan alatnya.

Pelajaran ini menunjukkan cara melaksanakan pengesahan OAuth2 untuk pelayan MCP menggunakan Spring Boot, satu corak biasa untuk penyebaran perusahaan dan produksi.

## Objektif Pembelajaran

Menjelang akhir pelajaran ini, anda akan:
- Memahami bagaimana OAuth2 digabungkan dengan pelayan MCP
- Melaksanakan Spring Authorization Server untuk pengeluaran token
- Melindungi titik akhir MCP dengan pengesahan berasaskan JWT
- Mengkonfigurasi aliran kelayakan klien untuk komunikasi mesin-ke-mesin

## Prasyarat

- Pemahaman asas Java dan Spring Boot
- Kefahaman dengan konsep MCP dari modul sebelumnya
- Maven atau Gradle dipasang

---

## Gambaran Keseluruhan Projek

Projek ini adalah **aplikasi Spring Boot minimal** yang bertindak sebagai kedua-duanya:

* **Spring Authorization Server** (mengeluarkan token akses JWT melalui aliran `client_credentials`), dan  
* **Resource Server** (melindungi titik akhir `/hello` sendiri).

Ia mencerminkan tetapan yang ditunjukkan dalam [pos blog Spring (2 Apr 2025)](https://spring.io/blog/2025/04/02/mcp-server-oauth2).

---

## Mula Pantas (tempatan)

```bash
# Gunakan nilai tempatan yang unik dan simpan ia daripada sejarah shell jika boleh.
export OAUTH_CLIENT_SECRET="replace-with-a-random-local-secret"
mvn spring-boot:run

# dapatkan token
curl -u "mcp-client:${OAUTH_CLIENT_SECRET}" -d grant_type=client_credentials \
     http://localhost:8081/oauth2/token | jq -r .access_token > token.txt

# panggil titik akhir yang dilindungi
curl -H "Authorization: Bearer $(cat token.txt)" http://localhost:8081/hello
```

---

## Uji Konfigurasi OAuth2

Anda boleh menguji konfigurasi keselamatan OAuth2 dengan langkah-langkah berikut:

### 1. Sahkan pelayan berjalan dan dilindungi

```bash
# Ini patut mengembalikan 401 Tidak Sah, mengesahkan keselamatan OAuth2 aktif
curl -v http://localhost:8081/
```

### 2. Dapatkan token akses menggunakan kelayakan klien

```bash
# Dapatkan dan ekstrak respons token penuh
curl -v -X POST http://localhost:8081/oauth2/token \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -u "mcp-client:${OAUTH_CLIENT_SECRET}" \
  -d "grant_type=client_credentials&scope=mcp.access"

# Atau untuk mengekstrak hanya token (memerlukan jq)
curl -s -X POST http://localhost:8081/oauth2/token \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -u "mcp-client:${OAUTH_CLIENT_SECRET}" \
  -d "grant_type=client_credentials&scope=mcp.access" | jq -r .access_token > token.txt
```

Pada PowerShell, tetapkan rahsia tempatan sebelum menjalankan Maven:

```powershell
$env:OAUTH_CLIENT_SECRET = "replace-with-a-random-local-secret"
mvn spring-boot:run
```

### 3. Akses titik akhir terlindung menggunakan token

```bash
# Menggunakan token yang disimpan
curl -H "Authorization: Bearer $(cat token.txt)" http://localhost:8081/hello

# Atau terus dengan nilai token
curl -H "Authorization: Bearer eyJra...token_value...xyz" http://localhost:8081/hello
```

Respons berjaya dengan "Hello from MCP OAuth2 Demo!" mengesahkan bahawa konfigurasi OAuth2 berfungsi dengan betul.

---

## Bina Kontena

```bash
docker build -t mcp-oauth2-demo .
docker run --rm -p 8081:8081 \
  -e OAUTH_CLIENT_SECRET="$OAUTH_CLIENT_SECRET" \
  mcp-oauth2-demo
```

## Keselamatan Produksi

Untuk penyebaran produksi, gunakan pembekal identiti khusus dan bukannya
pelayan kebenaran demo dalam proses ini. Simpan kelayakan dalam stor rahsia yang diurus,
putar mereka, gunakan kunci tandatangan kekal, hadkan skop, dan
tetapkan pengeluar eksplisit. Jangan sekali-kali meletakkan rahsia klien dalam kod sumber, imej kontena,
manifes penyebaran, atau output arahan.

Untuk Azure Container Apps, simpan nilai sebagai rahsia Container Apps yang disokong oleh
Key Vault di mana boleh, kemudian dedahkan hanya rujukan rahsia melalui
pembolehubah persekitaran `OAUTH_CLIENT_SECRET`.

---

## Sebar ke **Azure Container Apps**

```bash
az containerapp up -n mcp-oauth2 \
  -g demo-rg -l westeurope \
  --image <your-registry>/mcp-oauth2-demo:latest \
  --ingress external --target-port 8081
```

FQDN masuk menjadi **pengeluar** anda (`https://<fqdn>`).  
Azure menyediakan sijil TLS dipercayai secara automatik untuk `*.azurecontainerapps.io`.

---

## Sambungkan ke **Azure API Management**

Tambah polisi masuk ini kepada API anda:

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

- [5.4 Konteks akar](../mcp-root-contexts/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan oleh manusia profesional adalah disyorkan. Kami tidak bertanggungjawab terhadap sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->