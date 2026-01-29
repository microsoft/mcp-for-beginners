# MCP stdio Server - Solusi TypeScript

> **⚠️ Penting**: Solusi ini telah diperbarui untuk menggunakan **transport stdio** sesuai rekomendasi Spesifikasi MCP 2025-06-18. Transport SSE yang lama telah dihentikan.

## Ikhtisar

Solusi TypeScript ini menunjukkan cara membangun server MCP menggunakan transport stdio terkini. Transport stdio lebih sederhana, lebih aman, dan memberikan kinerja yang lebih baik dibandingkan pendekatan SSE yang sudah usang.

## Prasyarat

- Node.js 18+ atau versi lebih baru
- Pengelola paket npm atau yarn

## Instruksi Pengaturan

### Langkah 1: Instal dependensi

```bash
npm install
```

### Langkah 2: Bangun proyek

```bash
npm run build
```

## Menjalankan Server

Server stdio berjalan berbeda dari server SSE lama. Alih-alih memulai server web, server ini berkomunikasi melalui stdin/stdout:

```bash
npm start
```

**Penting**: Server akan tampak seperti berhenti - ini normal! Server sedang menunggu pesan JSON-RPC dari stdin.

## Menguji Server

### Metode 1: Menggunakan MCP Inspector (Direkomendasikan)

```bash
npm run inspector
```

Ini akan:
1. Meluncurkan server Anda sebagai subprocess
2. Membuka antarmuka web untuk pengujian
3. Memungkinkan Anda menguji semua alat server secara interaktif

### Metode 2: Pengujian langsung melalui command line

Anda juga dapat menguji dengan meluncurkan Inspector secara langsung:

```bash
npx @modelcontextprotocol/inspector node build/index.js
```

### Alat yang Tersedia

Server menyediakan alat-alat berikut:

- **add(a, b)**: Menjumlahkan dua angka
- **multiply(a, b)**: Mengalikan dua angka  
- **get_greeting(name)**: Membuat salam yang dipersonalisasi
- **get_server_info()**: Mendapatkan informasi tentang server

### Pengujian dengan Claude Desktop

Untuk menggunakan server ini dengan Claude Desktop, tambahkan konfigurasi berikut ke `claude_desktop_config.json` Anda:

```json
{
  "mcpServers": {
    "example-stdio-server": {
      "command": "node",
      "args": ["path/to/build/index.js"]
    }
  }
}
```

## Struktur Proyek

```
typescript/
├── src/
│   └── index.ts          # Main server implementation
├── build/                # Compiled JavaScript (generated)
├── package.json          # Project configuration
├── tsconfig.json         # TypeScript configuration
└── README.md            # This file
```

## Perbedaan Utama dari SSE

**Transport stdio (Saat Ini):**
- ✅ Pengaturan lebih sederhana - tidak memerlukan server HTTP
- ✅ Keamanan lebih baik - tidak ada endpoint HTTP
- ✅ Komunikasi berbasis subprocess
- ✅ JSON-RPC melalui stdin/stdout
- ✅ Kinerja lebih baik

**Transport SSE (Dihentikan):**
- ❌ Memerlukan pengaturan server Express
- ❌ Membutuhkan routing dan manajemen sesi yang kompleks
- ❌ Lebih banyak dependensi (Express, penanganan HTTP)
- ❌ Pertimbangan keamanan tambahan
- ❌ Sekarang dihentikan dalam MCP 2025-06-18

## Tips Pengembangan

- Gunakan `console.error()` untuk logging (jangan pernah menggunakan `console.log()` karena menulis ke stdout)
- Bangun dengan `npm run build` sebelum pengujian
- Uji dengan Inspector untuk debugging visual
- Pastikan semua pesan JSON diformat dengan benar
- Server secara otomatis menangani shutdown yang baik pada SIGINT/SIGTERM

Solusi ini mengikuti spesifikasi MCP terkini dan menunjukkan praktik terbaik untuk implementasi transport stdio menggunakan TypeScript.

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan penerjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berusaha untuk memberikan hasil yang akurat, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang otoritatif. Untuk informasi yang bersifat kritis, disarankan menggunakan jasa penerjemahan manusia profesional. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.