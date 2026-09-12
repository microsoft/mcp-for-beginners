# Penyahpepijatan dengan Pemeriksa MCP

> [!NOTE]
> Arahan menggunakan `--sse` dan URL yang berakhir dengan `/sse` menguji pengangkutan HTTP+SSE warisan.
> Untuk pelayan MCP `2026-07-28` yang baru, gunakan versi Pemeriksa yang
> menyokong HTTP BolehAlir dan pilih pengangkutan itu sebaliknya.

**Pemeriksa MCP** adalah alat penyahpepijatan penting yang membolehkan anda menguji dan menyelesaikan masalah pelayan MCP anda secara interaktif tanpa memerlukan aplikasi hos AI penuh. Anggap sahaja ia sebagai "Postman untuk MCP" - ia menyediakan antara muka visual untuk menghantar permintaan, melihat respons, dan memahami bagaimana pelayan anda berfungsi.

## Mengapa Gunakan Pemeriksa MCP?

Apabila membina pelayan MCP, anda sering akan menghadapi cabaran berikut:

- **"Adakah pelayan saya sedang berjalan?"** - Pemeriksa menunjukkan status sambungan
- **"Adakah alat saya didaftarkan dengan betul?"** - Pemeriksa menyenaraikan semua alat yang tersedia
- **"Apakah format respons?"** - Pemeriksa memaparkan respons JSON sepenuhnya
- **"Kenapa alat ini tidak berfungsi?"** - Pemeriksa menunjukkan mesej ralat terperinci

## Prasyarat

- Node.js 18+ dipasang
- npm (disediakan bersama Node.js)
- Pelayan MCP untuk diuji (rujuk [Modul 3.1 - Pelayan Pertama](../01-first-server/README.md))

## Pemasangan

### Pilihan 1: Jalankan dengan npx (Disyorkan untuk Ujian Pantas)

```bash
npx @modelcontextprotocol/inspector
```

### Pilihan 2: Pasang secara Global

```bash
npm install -g @modelcontextprotocol/inspector
mcp-inspector
```

### Pilihan 3: Tambah ke Projek Anda

```bash
cd your-mcp-server-project
npm install --save-dev @modelcontextprotocol/inspector
```

Tambah ke `package.json`:
```json
{
  "scripts": {
    "inspector": "mcp-inspector"
  }
}
```

---

## Sambung ke Pelayan Anda

### Pelayan stdio (Proses Tempatan)

Untuk pelayan yang berkomunikasi melalui input/output standard:

```bash
# Pelayan Python
npx @modelcontextprotocol/inspector python -m your_server_module

# Pelayan Node.js
npx @modelcontextprotocol/inspector node ./build/index.js

# Dengan pembolehubah persekitaran
OPENAI_API_KEY=xxx npx @modelcontextprotocol/inspector python server.py
```

### Pelayan SSE/HTTP (Rangkaian)

Untuk pelayan yang berjalan sebagai perkhidmatan HTTP:

1. Mula pelayan anda dahulu:
   ```bash
   python server.py  # Pelayan berjalan di http://localhost:8080
   ```

2. Lancarkan Pemeriksa dan sambung:
   ```bash
   npx @modelcontextprotocol/inspector --sse http://localhost:8080/sse
   ```

---

## Gambaran Keseluruhan Antara Muka Pemeriksa

Apabila Pemeriksa dilancarkan, anda akan melihat antara muka web (biasanya di `http://localhost:5173`):

```
┌─────────────────────────────────────────────────────────────┐
│  MCP Inspector                              [Connected ✅]   │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐         │
│  │   🔧 Tools  │  │ 📄 Resources│  │ 💬 Prompts  │         │
│  │    (3)      │  │    (2)      │  │    (1)      │         │
│  └─────────────┘  └─────────────┘  └─────────────┘         │
│                                                             │
│  ┌───────────────────────────────────────────────────────┐ │
│  │  📋 Message Log                                       │ │
│  │  ─────────────────────────────────────────────────── │ │
│  │  → initialize                                         │ │
│  │  ← initialized (server info)                          │ │
│  │  → tools/list                                         │ │
│  │  ← tools (3 tools)                                    │ │
│  └───────────────────────────────────────────────────────┘ │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## Menguji Alat

### Menyenaraikan Alat Tersedia

1. Klik tab **Alat**
2. Pemeriksa secara automatik memanggil `tools/list`
3. Anda akan melihat semua alat yang didaftarkan bersama:
   - Nama alat
   - Penerangan
   - Skema input (parameter)

### Memanggil Alat

1. Pilih satu alat dari senarai
2. Isikan parameter yang diperlukan dalam borang
3. Klik **Jalankan Alat**
4. Lihat respons dalam panel hasil

**Contoh: Menguji alat kalkulator**

```
Tool: add
Parameters:
  a: 25
  b: 17

Response:
{
  "content": [
    {
      "type": "text",
      "text": "42"
    }
  ]
}
```

### Menyahpepijat Ralat Alat

Apabila alat gagal, Pemeriksa menunjukkan:

```
Error Response:
{
  "error": {
    "code": -32602,
    "message": "Invalid params: 'b' is required"
  }
}
```

Kod ralat biasa:
| Kod | Maksud |
|------|---------|
| -32700 | Ralat parse (JSON tidak sah) |
| -32600 | Permintaan tidak sah |
| -32601 | Kaedah tidak ditemui |
| -32602 | Parameter tidak sah |
| -32603 | Ralat dalaman |

---

## Menguji Sumber

### Menyenaraikan Sumber

1. Klik tab **Sumber**
2. Pemeriksa memanggil `resources/list`
3. Anda akan melihat:
   - URI sumber
   - Nama dan penerangan
   - Jenis MIME

### Membaca Sumber

1. Pilih satu sumber
2. Klik **Baca Sumber**
3. Lihat kandungan yang dipulangkan

**Contoh output:**

```
Resource: file:///config/settings.json
Content-Type: application/json

{
  "config": {
    "debug": true,
    "maxConnections": 10
  }
}
```

---

## Menguji Petunjuk

### Menyenaraikan Petunjuk

1. Klik tab **Petunjuk**
2. Pemeriksa memanggil `prompts/list`
3. Lihat templat petunjuk yang tersedia

### Mendapatkan Petunjuk

1. Pilih satu petunjuk
2. Isikan sebarang hujah yang diperlukan
3. Klik **Dapatkan Petunjuk**
4. Lihat mesej petunjuk yang dirender

---

## Analisis Log Mesej

Log mesej menunjukkan semua mesej protokol MCP. Transkrip di bawah adalah dari
pelayan `2025-11-25` warisan dan termasuk jabat tangan `initialize` yang telah dialih keluar. Pelayan
`2026-07-28` menggunakan metadata permintaan sendiri dan `server/discover`
sebaliknya.

```
14:32:01 → {"jsonrpc":"2.0","id":1,"method":"initialize",...}
14:32:01 ← {"jsonrpc":"2.0","id":1,"result":{"protocolVersion":"2025-11-25",...}}
14:32:02 → {"jsonrpc":"2.0","id":2,"method":"tools/list"}
14:32:02 ← {"jsonrpc":"2.0","id":2,"result":{"tools":[...]}}
14:32:05 → {"jsonrpc":"2.0","id":3,"method":"tools/call","params":{"name":"add",...}}
14:32:05 ← {"jsonrpc":"2.0","id":3,"result":{"content":[...]}}
```

### Apa Yang Perlu Dicari

- **Pasangan Permintaan/Respons**: Setiap `→` harus mempunyai pasangan `←`
- **Mesej ralat**: Cari `"error"` dalam respons
- **Masa**: Jurang besar mungkin menunjukkan isu prestasi
- **Versi protokol**: Pastikan pelayan dan klien bersetuju pada versi

---

## Integrasi VS Code

Anda boleh menjalankan Pemeriksa terus dari VS Code:

### Menggunakan launch.json

Tambah ke `.vscode/launch.json`:

```json
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "Debug with MCP Inspector",
      "type": "node",
      "request": "launch",
      "runtimeExecutable": "npx",
      "runtimeArgs": [
        "@modelcontextprotocol/inspector",
        "python",
        "${workspaceFolder}/server.py"
      ],
      "console": "integratedTerminal"
    },
    {
      "name": "Debug SSE Server with Inspector",
      "type": "chrome",
      "request": "launch",
      "url": "http://localhost:5173",
      "preLaunchTask": "Start MCP Inspector"
    }
  ]
}
```

### Menggunakan Tugas

Tambah ke `.vscode/tasks.json`:

```json
{
  "version": "2.0.0",
  "tasks": [
    {
      "label": "Start MCP Inspector",
      "type": "shell",
      "command": "npx @modelcontextprotocol/inspector node ${workspaceFolder}/build/index.js",
      "isBackground": true,
      "problemMatcher": {
        "pattern": {
          "regexp": "^$"
        },
        "background": {
          "activeOnStart": true,
          "beginsPattern": "Inspector",
          "endsPattern": "listening"
        }
      }
    }
  ]
}
```

---

## Senario Penyahpepijatan Biasa

### Senario 1: Pelayan Tidak Sambung

**Gejala:** Pemeriksa menunjukkan "Terputus" atau tersekat pada "Menyambung..."

**Senarai Semak:**
1. ✅ Adakah arahan pelayan betul?
2. ✅ Adakah semua kebergantungan dipasang?
3. ✅ Adakah laluan pelayan mutlak atau relatif kepada direktori semasa?
4. ✅ Adakah pembolehubah persekitaran yang diperlukan disetkan?

**Langkah penyahpepijatan:**
```bash
# Uji pelayan secara manual terlebih dahulu
python -c "import your_server_module; print('OK')"

# Semak untuk ralat import
python -m your_server_module 2>&1 | head -20

# Sahkan MCP SDK telah dipasang
pip show mcp
```

### Senario 2: Alat Tidak Muncul

**Gejala:** Tab Alat menunjukkan senarai kosong

**Punca mungkin:**
1. Alat tidak didaftarkan semasa inisialisasi pelayan
2. Pelayan terhenti selepas dimulakan
3. Pengendali `tools/list` mengembalikan tatasusunan kosong

**Langkah penyahpepijatan:**
1. Periksa log mesej untuk respons `tools/list`
2. Tambah log pada kod pendaftaran alat anda
3. Sahkan hiasan `@mcp.tool()` hadir (Python)

### Senario 3: Alat Mengembalikan Ralat

**Gejala:** Panggilan alat mengembalikan respons ralat

**Pendekatan penyahpepijatan:**
1. Baca mesej ralat dengan teliti
2. Periksa padanan jenis parameter dengan skema
3. Tambah try/catch dengan mesej ralat terperinci
4. Semak log pelayan untuk jejak tumpukan

**Contoh pengendalian ralat yang diperbaiki:**

```python
@mcp.tool()
async def my_tool(param1: str, param2: int) -> str:
    try:
        # Logik alatan di sini
        result = process(param1, param2)
        return str(result)
    except ValueError as e:
        raise McpError(f"Invalid parameter: {e}")
    except Exception as e:
        raise McpError(f"Tool failed: {type(e).__name__}: {e}")
```

### Senario 4: Kandungan Sumber Kosong

**Gejala:** Sumber dipulangkan tetapi kandungan kosong atau null

**Senarai Semak:**
1. ✅ Laluan fail atau URI adalah betul
2. ✅ Pelayan mempunyai kebenaran untuk membaca sumber
3. ✅ Kandungan sumber dipulangkan dengan betul

---

## Ciri Lanjutan Pemeriksa

### Tajuk Tersuai (SSE)

```bash
npx @modelcontextprotocol/inspector \
  --sse http://localhost:8080/sse \
  --header "Authorization: Bearer your-token"
```

### Log Verbose

```bash
DEBUG=mcp* npx @modelcontextprotocol/inspector python server.py
```

### Rakaman Sesi

Pemeriksa boleh mengeksport log mesej untuk analisis kemudian:
1. Klik **Eksport Log** dalam panel mesej
2. Simpan fail JSON
3. Kongsi dengan ahli pasukan untuk penyahpepijatan

---

## Amalan Terbaik

1. **Uji awal dan kerap** - Gunakan Pemeriksa semasa pembangunan, bukan hanya bila ada masalah
2. **Mulakan dengan mudah** - Uji sambungan asas sebelum panggilan alat kompleks
3. **Periksa skema** - Banyak ralat berasal dari ketidakpadanan jenis parameter
4. **Baca mesej ralat** - Ralat MCP biasanya deskriptif
5. **Buka Pemeriksa sentiasa** - Ia membantu mengesan isu semasa anda membangunkan

---

## Apa Seterusnya

Anda telah menyiapkan Modul 3: Memulakan! Teruskan pembelajaran anda:

- [Modul 4: Pelaksanaan Praktikal](../../04-PracticalImplementation/README.md)

---

## Sumber Tambahan

- [Repositori GitHub MCP Inspector](https://github.com/modelcontextprotocol/inspector)
- [Spesifikasi MCP - Mesej Protokol](https://modelcontextprotocol.io/specification/2026-07-28/)
- [Spesifikasi JSON-RPC 2.0](https://www.jsonrpc.org/specification)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan oleh manusia profesional adalah disyorkan. Kami tidak bertanggungjawab terhadap sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->