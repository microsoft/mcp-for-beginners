# Jalankan Contoh

## Instalasi Dependensi

```sh
npm install
```

## Build

```sh
npm run build
```

## Buat Token

```sh
npm run generate
```

Ini akan membuat token dalam file *.env*. Klien akan membaca dari file ini.

## Jalankan Kode

Mulai server dengan:

```sh
npm start
```

Jalankan klien di terminal terpisah dengan:

```sh
npm run client
```

Di terminal server, Anda seharusnya melihat output yang mirip dengan:

```text
User exists
User has required scopes
Middleware executed
```

dan di terminal klien, Anda seharusnya melihat output yang mirip dengan:

```text
Connected to MCP server with session ID: c1e50d7b-acff-4f11-8f96-5ae490ca1eaa
Available tools: { tools: [ { name: 'process-files', inputSchema: [Object] } ] }
Client disconnected.
Exiting...
```

### Mengubah Hal-Hal

Mari kita pastikan kita memahami cakupan (scopes). Temukan file *server.ts* dan kode berikut:

```typescript
 if(!hasScopes(token, ["User.Read"])){
        res.status(403).send('Forbidden - insufficient scopes');
    }
```

Kode ini menunjukkan bahwa token yang diberikan harus memiliki "User.Read". Mari kita ubah menjadi "User.Write". Sekarang jalankan `npm run build` dan mulai ulang server dengan `npm start`. Anda sekarang seharusnya melihat otentikasi gagal karena kita tidak memiliki cakupan ini (kita hanya memiliki User.Read dan Admin.Write):

Klien sekarang mengatakan

```text
Error initializing client: Error: Error POSTing to endpoint (HTTP 403): Forbidden - insufficient scopes
```

dan Anda dapat melihat di terminal server bahwa ia mengatakan:

```text
User exists
```

dan tidak melanjutkan lebih jauh dari titik ini.

Anda bisa menambahkan cakupan "User.Write" dan menjalankan `npm run generate` lalu menjalankan ulang klien ATAU mengubah kode server kembali seperti semula.

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan penerjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berusaha untuk memberikan hasil yang akurat, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang otoritatif. Untuk informasi yang bersifat kritis, disarankan menggunakan jasa penerjemahan manusia profesional. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.