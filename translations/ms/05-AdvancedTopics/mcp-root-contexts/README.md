# Akar MCP (Ciri Warisan)

> [!WARNING]
> Akar tidak digunakan lagi mulai MCP `2026-07-28`. Ia kekal dalam semakan ini untuk
> keserasian dan layak untuk dipadam dalam semakan spesifikasi pertama
> yang dikeluarkan pada atau selepas 28 Julai 2027. Pelaksanaan baru harus mempasskan
> direktori atau fail melalui parameter alat, URI sumber, atau konfigurasi
> pelayan.

## Gambaran Keseluruhan

Akar membolehkan pelanggan MCP memberitahu pelayan lokasi sistem fail yang relevan
kepada permintaan semasa. Satu akar mengandungi URI `file://` yang diperlukan dan nama
yang boleh dibaca manusia secara pilihan.

Akar adalah petunjuk maklumat. Ia bukan bekas sejarah perbualan,
sesi protokol, atau mekanisme kawalan akses. Protokol tidak
menguatkuasakan agar pelayan kekal dalam akar yang disenaraikan.

## Objektif Pembelajaran

Selepas pelajaran ini, anda akan dapat:

- Terangkan apa yang Akar MCP wakili dan apa yang ia tidak wakili.
- Kenal pasti aliran multi-pusingan `roots/list` semasa.
- Terapkan kawalan keselamatan secara bebas dari Akar.
- Migrasi pelaksanaan baru ke alternatif yang disokong.

## Data Akar

Pelanggan mengembalikan setiap akar sebagai URI `file://` dengan nama paparan pilihan:

```json
{
  "roots": [
    {
      "uri": "file:///home/user/projects/weather-service",
      "name": "Weather Service"
    }
  ]
}
```

Pelanggan harus mendedahkan hanya lokasi yang diluluskan oleh pengguna. Pelayan harus melayan
keputusan sebagai panduan mengenai fail yang relevan, bukan sebagai bukti kebenaran.

## Aliran MCP 2026-07-28

Pelanggan yang menyokong Akar menyatakan keupayaan dalam setiap permintaan:

```json
{
  "_meta": {
    "io.modelcontextprotocol/clientCapabilities": {
      "roots": {}
    }
  }
}
```

Semasa memproses permintaan pelanggan, pelayan boleh mengembalikan
`InputRequiredResult` yang mengandungi permintaan input `roots/list`:

```json
{
  "resultType": "input_required",
  "inputRequests": {
    "workspaceRoots": {
      "method": "roots/list"
    }
  },
  "requestState": "opaque-state-from-server"
}
```

Pelanggan mengumpul akar yang diluluskan dan mencuba semula permintaan asal dengan
`inputResponses` yang sepadan dan `requestState` yang tidak berubah. Corak multi-pusingan
ini memastikan protokol tanpa keadaan; tiada jabat tangan `initialize` atau
sesi paras protokol.

## Tingkah Laku Warisan 2025-11-25

Dalam MCP `2025-11-25`, pelanggan mengiklan Akar semasa inisialisasi. Pelayan
boleh mengeluarkan permintaan langsung `roots/list`, dan pelanggan boleh menghantar
`notifications/roots/list_changed` apabila akar mereka berubah.

Kitar hayat itu adalah tingkah laku warisan. Jangan gabungkan contoh inisialisasi atau
pemberitahuannya dengan pelaksanaan `2026-07-28`.

## Pengganti yang Disyorkan

### Parameter Alat

Nyatakan direktori atau fail yang diperlukan secara eksplisit dalam skema alat:

```json
{
  "name": "analyze_project",
  "inputSchema": {
    "type": "object",
    "properties": {
      "projectDirectory": {
        "type": "string",
        "description": "Approved project directory to analyze"
      }
    },
    "required": ["projectDirectory"]
  }
}
```

### URI Sumber

Gunakan Sumber MCP apabila pelayan boleh mendedahkan fail berkaitan melalui URI stabil.
Ini memastikan penemuan dan pengambilan berlaku secara eksplisit.

### Konfigurasi Pelayan

Untuk penempatan tetap, konfigurasikan direktori yang dibenarkan semasa pelayan bermula.
Ini biasanya lebih jelas daripada menemukannya semasa panggilan alat.

## Keperluan Keselamatan

Mana-mana pengganti yang anda pilih:

- Dapatkan persetujuan pengguna sebelum mendedahkan lokasi sistem fail.
- Kanonikan dan sahkan laluan untuk mengelakkan traversal.
- Tegaskan kebenaran dan sandboxing secara bebas dari nilai akar.
- Semak semula kebenaran apabila fail diakses, bukan hanya ketika ia disenaraikan.
- Elakkan mengembalikan laluan sensitif dalam log atau mesej ralat.

## Perkara Penting

- Akar menggambarkan lokasi sistem fail yang relevan; mereka tidak menyimpan keadaan perbualan.

- Akar adalah panduan, bukan sempadan kawalan akses.
- MCP `2026-07-28` membawa keupayaan per permintaan dan menggunakan
  `InputRequiredResult` untuk `roots/list`.
- Pelaksanaan baru harus menggunakan parameter alat, URI sumber, atau konfigurasi pelayan
  sebagai gantinya.

## Sumber Tambahan

- [Akar dalam MCP 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/client/roots)
- [Daftar ciri yang tidak digunakan lagi](https://modelcontextprotocol.io/specification/2026-07-28/deprecated)
- [Apa yang Berubah dalam MCP: Spesifikasi 2026-07-28](../../01-CoreConcepts/mcp-2026-07-28.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan oleh manusia profesional adalah disyorkan. Kami tidak bertanggungjawab terhadap sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->