# Akar MCP (Fitur Lama)

> [!WARNING]
> Akar sudah tidak digunakan sejak MCP `2026-07-28`. Mereka tetap ada dalam revisi ini untuk
> kompatibilitas dan berpotensi dihapus dalam revisi spesifikasi pertama
> yang dirilis pada atau setelah 28 Juli 2027. Implementasi baru sebaiknya mengoper
> direktori atau file melalui parameter alat, URI sumber daya, atau konfigurasi
> server.

## Ikhtisar

Akar memungkinkan klien MCP memberi tahu server lokasi sistem berkas mana yang relevan
untuk permintaan saat ini. Sebuah akar berisi URI `file://` yang wajib dan nama
yang dapat dibaca manusia (opsional).

Akar adalah petunjuk informasional. Mereka bukan wadah riwayat percakapan,
sesi protokol, atau mekanisme pengendalian akses. Protokol tidak
memaksa server untuk tetap berada di dalam akar yang tercantum.

## Tujuan Pembelajaran

Pada akhir pelajaran ini, Anda akan mampu:

- Menjelaskan apa yang diwakili oleh Akar MCP dan apa yang tidak diwakili oleh mereka.
- Mengenali alur multi-perjalanan `roots/list` saat ini.
- Menerapkan kontrol keamanan secara independen dari Akar.
- Memigrasi implementasi baru ke alternatif yang didukung.

## Data Akar

Klien mengembalikan setiap akar sebagai URI `file://` dengan nama tampilan opsional:

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

Klien hanya boleh menampilkan lokasi yang disetujui oleh pengguna. Server harus memperlakukan
hasil tersebut sebagai panduan tentang file yang relevan, bukan sebagai bukti otorisasi.

## Alur MCP 2026-07-28

Klien yang mendukung Akar menyatakan kapabilitas tersebut di setiap permintaan:

```json
{
  "_meta": {
    "io.modelcontextprotocol/clientCapabilities": {
      "roots": {}
    }
  }
}
```

Saat memproses permintaan klien, server dapat mengembalikan
`InputRequiredResult` yang berisi permintaan input `roots/list`:

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

Klien mengumpulkan akar yang disetujui dan mengulang permintaan asli dengan
`inputResponses` yang sesuai dan `requestState` yang tidak berubah. Pola multi-perjalanan ini
menjaga protokol tetap tanpa status; tidak ada jabat tangan `initialize` atau
sesi tingkat protokol.

## Perilaku Lama 2025-11-25

Dalam MCP `2025-11-25`, klien mengumumkan Akar selama inisialisasi. Server
dapat mengirim permintaan `roots/list` langsung, dan klien dapat mengirim
`notifications/roots/list_changed` saat akar mereka berubah.

Siklus hidup tersebut adalah perilaku lama. Jangan gabungkan contoh inisialisasi atau
notifikasinya dengan implementasi `2026-07-28`.

## Pengganti yang Direkomendasikan

### Parameter Alat

Buat direktori atau file yang diperlukan eksplisit dalam skema alat:

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

### URI Sumber Daya

Gunakan Sumber Daya MCP ketika server dapat menampilkan file relevan melalui URI
yang stabil. Ini menjaga penemuan dan pengambilan eksplisit.

### Konfigurasi Server

Untuk penyebaran tetap, konfigurasikan direktori yang diizinkan ketika server mulai.
Ini seringkali lebih jelas daripada menemukannya selama panggilan alat.

## Persyaratan Keamanan

Apapun pengganti yang Anda pilih:

- Dapatkan persetujuan pengguna sebelum membuka lokasi sistem berkas.
- Kanonisasi dan validasi jalur untuk mencegah traversal.
- Tegakkan otorisasi dan sandboxing secara independen dari nilai akar.
- Periksa kembali izin saat file diakses, bukan hanya saat terdaftar.
- Hindari mengembalikan jalur sensitif dalam log atau pesan kesalahan.

## Poin Penting

- Akar menggambarkan lokasi sistem berkas yang relevan; mereka tidak menyimpan
  status percakapan.
- Akar adalah panduan, bukan batas kontrol akses.
- MCP `2026-07-28` membawa kapabilitas per permintaan dan menggunakan
  `InputRequiredResult` untuk `roots/list`.
- Implementasi baru harus menggunakan parameter alat, URI sumber daya, atau
  konfigurasi server sebagai gantinya.

## Sumber Daya Tambahan

- [Akar di MCP 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/client/roots)
- [Daftar fitur yang sudah usang](https://modelcontextprotocol.io/specification/2026-07-28/deprecated)
- [Apa yang Berubah di MCP: Spesifikasi 2026-07-28](../../01-CoreConcepts/mcp-2026-07-28.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk mencapai akurasi, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sah. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->