# Contoh: Host Dasar

Contoh implementasi referensi yang menunjukkan cara membangun aplikasi host MCP yang terhubung ke server MCP dan merender UI alat dalam sandbox yang aman.

Host dasar ini juga dapat digunakan untuk menguji Aplikasi MCP selama pengembangan lokal.

## File Utama

- [`index.html`](../../../../../../../03-GettingStarted/15-mcp-apps/ext-apps/examples/basic-host/index.html) / [`src/index.tsx`](../../../../../../../03-GettingStarted/15-mcp-apps/ext-apps/examples/basic-host/src/index.tsx) - Host UI React dengan pemilihan alat, input parameter, dan manajemen iframe
- [`sandbox.html`](../../../../../../../03-GettingStarted/15-mcp-apps/ext-apps/examples/basic-host/sandbox.html) / [`src/sandbox.ts`](../../../../../../../03-GettingStarted/15-mcp-apps/ext-apps/examples/basic-host/src/sandbox.ts) - Proxy iframe luar dengan validasi keamanan dan relay pesan dua arah
- [`src/implementation.ts`](../../../../../../../03-GettingStarted/15-mcp-apps/ext-apps/examples/basic-host/src/implementation.ts) - Logika inti: koneksi server, pemanggilan alat, dan penyiapan AppBridge

## Memulai

```bash
npm install
npm run start
# Buka http://localhost:8080
```

Secara default, aplikasi host akan mencoba terhubung ke server MCP di `http://localhost:3001/mcp`. Anda dapat mengkonfigurasi perilaku ini dengan mengatur variabel lingkungan `SERVERS` dengan array JSON dari URL server:

```bash
SERVERS='["http://localhost:1234/mcp", "http://localhost:5678/mcp"]' npm run start
```

## Arsitektur

Contoh ini menggunakan pola sandbox double-iframe untuk isolasi UI yang aman:

```
Host (port 8080)
  └── Outer iframe (port 8081) - sandbox proxy
        └── Inner iframe (srcdoc) - untrusted tool UI
```

**Mengapa dua iframe?**

- Iframe luar berjalan pada origin terpisah (port 8081) mencegah akses langsung ke host
- Iframe dalam menerima HTML via `srcdoc` dan dibatasi oleh atribut sandbox
- Pesan mengalir melalui iframe luar yang memvalidasi dan meneruskannya secara dua arah

Arsitektur ini memastikan bahwa meskipun kode UI alat berbahaya, kode tersebut tidak dapat mengakses DOM aplikasi host, cookie, atau konteks JavaScript.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya mencapai ketepatan, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber otoritatif. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang salah yang timbul dari penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->