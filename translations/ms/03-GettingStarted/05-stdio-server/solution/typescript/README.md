# Pelayan MCP stdio - Penyelesaian TypeScript

> **⚠️ Penting**: Penyelesaian ini telah dikemas kini untuk menggunakan **pengangkutan stdio** seperti yang disyorkan oleh Spesifikasi MCP 2025-06-18. Pengangkutan SSE asal telah dihentikan.

## Gambaran Keseluruhan

Penyelesaian TypeScript ini menunjukkan cara membina pelayan MCP menggunakan pengangkutan stdio semasa. Pengangkutan stdio adalah lebih mudah, lebih selamat, dan memberikan prestasi yang lebih baik berbanding pendekatan SSE yang telah dihentikan.

## Prasyarat

- Node.js 18+ atau lebih baharu
- Pengurus pakej npm atau yarn

## Arahan Persediaan

### Langkah 1: Pasang kebergantungan

```bash
npm install
```

### Langkah 2: Bina projek

```bash
npm run build
```

## Menjalankan Pelayan

Pelayan stdio berfungsi secara berbeza daripada pelayan SSE lama. Daripada memulakan pelayan web, ia berkomunikasi melalui stdin/stdout:

```bash
npm start
```

**Penting**: Pelayan akan kelihatan seperti tergantung - ini adalah normal! Ia sedang menunggu mesej JSON-RPC daripada stdin.

## Menguji Pelayan

### Kaedah 1: Menggunakan MCP Inspector (Disyorkan)

```bash
npm run inspector
```

Ini akan:
1. Melancarkan pelayan anda sebagai subprocess
2. Membuka antara muka web untuk ujian
3. Membolehkan anda menguji semua alat pelayan secara interaktif

### Kaedah 2: Ujian terus melalui baris arahan

Anda juga boleh menguji dengan melancarkan Inspector secara langsung:

```bash
npx @modelcontextprotocol/inspector node build/index.js
```

### Alat yang Tersedia

Pelayan menyediakan alat berikut:

- **add(a, b)**: Menjumlahkan dua nombor
- **multiply(a, b)**: Mendarab dua nombor  
- **get_greeting(name)**: Menjana ucapan peribadi
- **get_server_info()**: Mendapatkan maklumat tentang pelayan

### Ujian dengan Claude Desktop

Untuk menggunakan pelayan ini dengan Claude Desktop, tambahkan konfigurasi ini ke dalam `claude_desktop_config.json` anda:

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

## Struktur Projek

```
typescript/
├── src/
│   └── index.ts          # Main server implementation
├── build/                # Compiled JavaScript (generated)
├── package.json          # Project configuration
├── tsconfig.json         # TypeScript configuration
└── README.md            # This file
```

## Perbezaan Utama daripada SSE

**Pengangkutan stdio (Semasa):**
- ✅ Persediaan lebih mudah - tidak memerlukan pelayan HTTP
- ✅ Keselamatan lebih baik - tiada endpoint HTTP
- ✅ Komunikasi berasaskan subprocess
- ✅ JSON-RPC melalui stdin/stdout
- ✅ Prestasi lebih baik

**Pengangkutan SSE (Dihentikan):**
- ❌ Memerlukan persediaan pelayan Express
- ❌ Memerlukan pengurusan routing dan sesi yang kompleks
- ❌ Lebih banyak kebergantungan (Express, pengendalian HTTP)
- ❌ Pertimbangan keselamatan tambahan
- ❌ Kini dihentikan dalam MCP 2025-06-18

## Petua Pembangunan

- Gunakan `console.error()` untuk log (jangan gunakan `console.log()` kerana ia menulis ke stdout)
- Bina dengan `npm run build` sebelum menguji
- Uji dengan Inspector untuk debugging secara visual
- Pastikan semua mesej JSON diformatkan dengan betul
- Pelayan secara automatik mengendalikan penutupan yang teratur pada SIGINT/SIGTERM

Penyelesaian ini mengikuti spesifikasi MCP semasa dan menunjukkan amalan terbaik untuk pelaksanaan pengangkutan stdio menggunakan TypeScript.

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk memastikan ketepatan, sila ambil perhatian bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang berwibawa. Untuk maklumat penting, terjemahan manusia profesional adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.