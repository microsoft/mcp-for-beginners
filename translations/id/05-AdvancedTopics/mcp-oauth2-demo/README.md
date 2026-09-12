# Demo OAuth2 MCP

> [!WARNING]
> Ini adalah contoh pembelajaran lokal, bukan layanan otorisasi produksi. Ini
> menggunakan klien dalam memori dan menghasilkan kunci tanda tangan baru saat startup. Jangan
> menerapkannya dengan rahasia klien yang dibagikan, default, atau dikontrol sumbernya.

## Pendahuluan

OAuth2 adalah protokol standar industri untuk otorisasi, memungkinkan akses aman ke sumber daya tanpa berbagi kredensial. Dalam implementasi MCP (Model Context Protocol), OAuth2 menyediakan cara yang kuat untuk mengautentikasi dan mengotorisasi klien (seperti agen AI) untuk mengakses server MCP dan alat-alatnya.

Pelajaran ini menunjukkan cara mengimplementasikan autentikasi OAuth2 untuk server MCP menggunakan Spring Boot, pola umum untuk penyebaran perusahaan dan produksi.

## Tujuan Pembelajaran

Pada akhir pelajaran ini, Anda akan:
- Memahami bagaimana OAuth2 terintegrasi dengan server MCP
- Mengimplementasikan Spring Authorization Server untuk penerbitan token
- Melindungi endpoint MCP dengan autentikasi berbasis JWT
- Mengonfigurasi alur kredensial klien untuk komunikasi mesin-ke-mesin

## Prasyarat

- Pemahaman dasar Java dan Spring Boot
- Familiar dengan konsep MCP dari modul sebelumnya
- Maven atau Gradle terpasang

---

## Gambaran Proyek

Proyek ini adalah **aplikasi Spring Boot minimal** yang berfungsi sebagai:

* **Spring Authorization Server** (mengeluarkan token akses JWT melalui alur `client_credentials`), dan  
* **Resource Server** (melindungi endpoint `/hello` sendiri).

Ini mencerminkan pengaturan yang ditunjukkan dalam [posting blog Spring (2 Apr 2025)](https://spring.io/blog/2025/04/02/mcp-server-oauth2).

---

## Mulai cepat (lokal)

```bash
# Gunakan nilai lokal unik dan simpan di luar riwayat shell jika memungkinkan.
export OAUTH_CLIENT_SECRET="replace-with-a-random-local-secret"
mvn spring-boot:run

# dapatkan token
curl -u "mcp-client:${OAUTH_CLIENT_SECRET}" -d grant_type=client_credentials \
     http://localhost:8081/oauth2/token | jq -r .access_token > token.txt

# panggil endpoint yang dilindungi
curl -H "Authorization: Bearer $(cat token.txt)" http://localhost:8081/hello
```

---

## Menguji Konfigurasi OAuth2

Anda dapat menguji konfigurasi keamanan OAuth2 dengan langkah-langkah berikut:

### 1. Verifikasi server berjalan dan terlindungi

```bash
# Ini harus mengembalikan 401 Unauthorized, mengonfirmasi bahwa keamanan OAuth2 aktif
curl -v http://localhost:8081/
```

### 2. Dapatkan token akses menggunakan kredensial klien

```bash
# Dapatkan dan ekstrak respons token lengkap
curl -v -X POST http://localhost:8081/oauth2/token \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -u "mcp-client:${OAUTH_CLIENT_SECRET}" \
  -d "grant_type=client_credentials&scope=mcp.access"

# Atau untuk mengekstrak hanya tokennya (memerlukan jq)
curl -s -X POST http://localhost:8081/oauth2/token \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -u "mcp-client:${OAUTH_CLIENT_SECRET}" \
  -d "grant_type=client_credentials&scope=mcp.access" | jq -r .access_token > token.txt
```

Di PowerShell, atur rahasia lokal sebelum menjalankan Maven:

```powershell
$env:OAUTH_CLIENT_SECRET = "replace-with-a-random-local-secret"
mvn spring-boot:run
```

### 3. Akses endpoint terlindungi menggunakan token

```bash
# Menggunakan token yang disimpan
curl -H "Authorization: Bearer $(cat token.txt)" http://localhost:8081/hello

# Atau langsung dengan nilai token
curl -H "Authorization: Bearer eyJra...token_value...xyz" http://localhost:8081/hello
```

Respon sukses dengan "Hello from MCP OAuth2 Demo!" mengonfirmasi bahwa konfigurasi OAuth2 berfungsi dengan benar.

---

## Membangun kontainer

```bash
docker build -t mcp-oauth2-demo .
docker run --rm -p 8081:8081 \
  -e OAUTH_CLIENT_SECRET="$OAUTH_CLIENT_SECRET" \
  mcp-oauth2-demo
```

## Keamanan Produksi

Untuk penyebaran produksi, gunakan penyedia identitas khusus daripada
server otorisasi demo in-process ini. Simpan kredensial dalam
penyimpanan rahasia yang dikelola, lakukan rotasi, gunakan kunci tanda tangan yang persisten, batasi cakupan, dan
tetapkan penerbit secara eksplisit. Jangan pernah meletakkan rahasia klien dalam kode sumber, gambar kontainer,
manifes penyebaran, atau keluaran perintah.

Untuk Azure Container Apps, simpan nilai sebagai rahasia Container Apps yang didukung oleh
Key Vault jika memungkinkan, lalu hanya ekspos referensi rahasia melalui
variabel lingkungan `OAUTH_CLIENT_SECRET`.

---

## Terapkan ke **Azure Container Apps**

```bash
az containerapp up -n mcp-oauth2 \
  -g demo-rg -l westeurope \
  --image <your-registry>/mcp-oauth2-demo:latest \
  --ingress external --target-port 8081
```

FQDN ingress menjadi **penerbit** Anda (`https://<fqdn>`).  
Azure menyediakan sertifikat TLS terpercaya secara otomatis untuk `*.azurecontainerapps.io`.

---

## Integrasi ke **Azure API Management**

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

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk mencapai akurasi, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sah. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->