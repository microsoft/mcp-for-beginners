# AGENTS.md

## Ikhtisar Proyek

**MCP untuk Pemula** adalah kurikulum edukasi sumber terbuka untuk mempelajari Model Context Protocol (MCP) - kerangka standar untuk interaksi antara model AI dan aplikasi klien. Repositori ini menyediakan materi pembelajaran lengkap dengan contoh kode praktis dalam berbagai bahasa pemrograman.

### Teknologi Kunci

- **Bahasa Pemrograman**: C#, Java, JavaScript, TypeScript, Python, Rust
- **Framework & SDK**: 
  - MCP SDK (`@modelcontextprotocol/sdk`)
  - Spring Boot (Java)
  - FastMCP (Python)
  - LangChain4j (Java)
- **Basis Data**: PostgreSQL dengan ekstensi pgvector
- **Platform Cloud**: Azure (Container Apps, OpenAI, Content Safety, Application Insights)
- **Alat Build**: npm, Maven, pip, Cargo
- **Dokumentasi**: Markdown dengan terjemahan otomatis multi-bahasa (lebih dari 48 bahasa)

### Arsitektur

- **11 Modul Inti (00-11)**: Jalur pembelajaran berurutan dari dasar hingga topik lanjutan
- **Lab Praktik**: Latihan praktis dengan kode solusi lengkap dalam berbagai bahasa
- **Proyek Contoh**: Implementasi server dan klien MCP yang berfungsi
- **Sistem Terjemahan**: Alur kerja GitHub Actions otomatis untuk dukungan multi-bahasa
- **Aset Gambar**: Direktori gambar terpusat dengan versi terjemahan

## Perintah Setup

Ini adalah repositori yang berfokus pada dokumentasi. Sebagian besar setup terjadi di dalam proyek contoh dan lab individual.

### Setup Repositori

```bash
# Kloning repositori
git clone https://github.com/microsoft/mcp-for-beginners.git
cd mcp-for-beginners
```

### Bekerja dengan Proyek Contoh

Proyek contoh terletak di:
- `03-GettingStarted/samples/` - Contoh spesifik bahasa
- `03-GettingStarted/01-first-server/solution/` - Implementasi server pertama
- `03-GettingStarted/02-client/solution/` - Implementasi klien
- `11-MCPServerHandsOnLabs/` - Lab integrasi basis data komprehensif

Setiap proyek contoh memiliki instruksi setup sendiri:

#### Proyek TypeScript/JavaScript
```bash
cd <project-directory>
npm install
npm start
```

#### Proyek Python
```bash
cd <project-directory>
pip install -r requirements.txt
# atau
pip install -e .
python main.py
```

#### Proyek Java
```bash
cd <project-directory>
mvn clean install
mvn spring-boot:run
```

## Alur Kerja Pengembangan

### Kesiapan MCP 7-28

#### Daftar periksa kesiapan repo

- [x] **Kejelasan kontributor baru**: File ini mendefinisikan tujuan repositori,
  struktur, aturan kontribusi, dan jalur setup contoh.
- [x] **Perintah build/test/lint dengan flag tepat**:
  - Lint dokumentasi repositori:
    `npx --yes markdownlint-cli2 "**/*.md" "#node_modules" "#translations" "#translated_images"`
  - Audit pola tautan dokumentasi repositori:
    `find . -name "*.md" -not -path "*/node_modules/*" -not -path "./translations/*" -not -path "./translated_images/*" -print0 | xargs -0 grep -En "\[.*\]\(.*\)"`
  - Validasi contoh TypeScript:
    `cd 03-GettingStarted/samples/typescript && npm ci && npm test && npm run build`
  - Validasi contoh Python:
    `cd 10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp && python -m pip install -e . && pytest -q`
  - Validasi contoh Java:
    `cd 03-GettingStarted/samples/java/calculator && mvn -B -ntp test verify`
- [x] **Satu alur kerja realistis yang dapat menjadi alat MCP**:
  `validate_curriculum_change`
- [x] **Input/output yang eksplisit** (lihat spesifikasi di bawah).
- [x] **Izin dan mode kegagalan didokumentasikan** (lihat spesifikasi di bawah).
- [x] **Keberhasilan pengujian CI eksplisit** (perintah deterministik, kode keluar eksplisit,
  dan output yang dapat dibaca mesin).

#### Alur kerja kandidat alat MCP: `validate_curriculum_change`

##### Tujuan

Memvalidasi perubahan dokumentasi kurikulum dan kesehatan kode contoh representatif
sebelum digabungkan.

##### Input

- `changed_paths: string[]` (required) - jalur relatif yang diubah dalam PR.
- `run_docs_lint: boolean` (default `true`)
- `run_links_audit: boolean` (default `true`)
- `run_samples: { typescript?: boolean, python?: boolean, java?: boolean }`
  (default semua `false`)

##### Output

- `status: "ok" | "failed"`
- `checks: Array<{ name: string, command: string, exit_code: number,
  summary: string }>`
- `artifacts: Array<{ type: "log" | "report", path: string }>`
- `failed_checks: string[]`

##### Izin

- Membaca file ruang kerja dan menulis artefak yang dihasilkan alat (misalnya, laporan lint,
  log pengujian) saja; tidak menulis ke `translations/` atau
  `translated_images/`.
- Menjalankan perintah shell lokal.
- Akses jaringan opsional hanya untuk restore paket (`npm ci`,
  `python -m pip install`, resolusi dependensi `mvn`).
- Tidak diperbolehkan melakukan push, merge, atau memodifikasi `translations/` atau
  `translated_images/`.

##### Mode kegagalan

- `E_NO_INPUT_PATHS`: `changed_paths` kosong.
- `E_INVALID_PATH`: jalur input keluar dari root repositori.
- `E_LINT_FAILED`: lint markdown keluar dengan kode bukan nol.
- `E_LINK_AUDIT_FAILED`: perintah audit tautan keluar dengan kode bukan nol.
- `E_SAMPLE_TEST_FAILED`: pengujian/ build contoh keluar dengan kode bukan nol.
- `E_TIMEOUT`: perintah melebihi batas waktu yang ditentukan.

##### Kontrak CI yang direkomendasikan

Untuk mengotomatiskan validasi, konfigurasikan pekerjaan CI yang:

- Memicu pada pull request yang menyentuh `*.md`, kode contoh, atau file ini.
- Menjalankan perintah tepat yang tercantum di atas.
- Menyimpan log sebagai artefak.
- Gagal pekerjaan jika ada kode keluar bukan nol.

#### Jika Anda mengirimkan server MCP dari repo ini

- [ ] Baca changelog MCP terakhir `2026-07-28`:
  <https://modelcontextprotocol.io/specification/2026-07-28/changelog>
- [ ] Verifikasi bahwa rilis SDK yang dipilih mendukung MCP `2026-07-28`:
  <https://modelcontextprotocol.io/docs/sdk>
- [ ] Hapus asumsi sesi dan handshake; perlakukan setiap permintaan sebagai
  mandiri:
  <https://modelcontextprotocol.io/specification/2026-07-28/basic/lifecycle>
- [ ] Kirim header `Mcp-Method` dan `Mcp-Name` untuk permintaan HTTP mentah:
  <https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/streamable-http>
- [ ] Audit kode kesalahan hardcoded (`missing resource` dipindah dari `-32002` ke `-32602`).

- [ ] Migrasi Roots, Sampling, Logging, dan Pendaftaran Klien Dinamis yang sudah usang
  Registrasi:
  <https://modelcontextprotocol.io/specification/2026-07-28/deprecated>
- [ ] Migrasi dari API Tugas eksperimental `2025-11-25`:
  <https://modelcontextprotocol.io/extensions/tasks>
- [ ] Tinjau otorisasi untuk penguatan OAuth dan OpenID Connect:
  <https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization>

### Struktur Dokumentasi

- **Modul 00-11**: Konten kurikulum inti dalam urutan berurutan
- **translations/**: Versi bahasa spesifik (dihasilkan otomatis, jangan diedit langsung)
- **translated_images/**: Versi gambar yang dilokalkan (dihasilkan otomatis)
- **images/**: Gambar dan diagram sumber

### Membuat Perubahan Dokumentasi

1. Edit hanya file markdown bahasa Inggris di direktori modul root (00-11)
2. Perbarui gambar di direktori `images/` jika diperlukan
3. GitHub Action co-op-translator akan secara otomatis menghasilkan terjemahan
4. Terjemahan dibuat ulang saat melakukan push ke cabang utama

### Bekerja dengan Terjemahan

- **Terjemahan Otomatis**: Alur kerja GitHub Actions menangani semua terjemahan
- **JANGAN mengedit secara manual** file dalam direktori `translations/`
- Metadata terjemahan disematkan dalam setiap file terjemahan
- Bahasa yang didukung: lebih dari 48 bahasa termasuk Arab, Cina, Prancis, Jerman, Hindi, Jepang, Korea, Portugis, Rusia, Spanyol, dan banyak lagi

## Instruksi Pengujian

### Validasi Dokumentasi

Karena ini terutama repositori dokumentasi, pengujian difokuskan pada:

1. **Audit Pola Tautan**: Daftar tautan Markdown untuk ditinjau

   ```bash
   # Daftar tautan Markdown (audit pola)
   find . -name "*.md" -not -path "*/node_modules/*" -not -path "./translations/*" -not -path "./translated_images/*" -print0 | xargs -0 grep -En "\[.*\]\(.*\)"
   ```

2. **Validasi Contoh Kode**: Uji bahwa contoh kode dapat dikompilasi/dijalankan

   ```bash
   # Navigasi ke contoh tertentu dan jalankan tesnya
   cd 03-GettingStarted/samples/typescript
   npm install && npm test
   ```

3. **Linting Markdown**: Periksa konsistensi format

   ```bash
   # Gunakan markdownlint jika diperlukan
   npx --yes markdownlint-cli2 "**/*.md" "#node_modules" "#translations" "#translated_images"
   ```

### Pengujian Proyek Sampel

Setiap sampel bahasa spesifik termasuk pendekatan pengujian tersendiri:

#### TypeScript/JavaScript
```bash
npm test
npm run build
```

#### Python
```bash
pytest
python -m pytest tests/
```

#### Java
```bash
mvn test
mvn verify
```

## Panduan Gaya Kode

### Gaya Dokumentasi

- Gunakan bahasa yang jelas dan ramah pemula
- Sertakan contoh kode dalam beberapa bahasa bila memungkinkan
- Ikuti praktik terbaik markdown:
  - Gunakan header gaya ATX (sintaks `#`)
  - Gunakan blok kode berpagar dengan penanda bahasa
  - Sertakan teks alt yang deskriptif untuk gambar
  - Jaga panjang baris agar wajar (tidak ada batas keras, tapi masuk akal)

### Gaya Contoh Kode

#### TypeScript/JavaScript
- Gunakan modul ES (`import`/`export`)
- Ikuti konvensi mode ketat TypeScript
- Sertakan anotasi tipe
- Target ES2022

#### Python
- Ikuti pedoman gaya PEP 8
- Gunakan petunjuk tipe bila sesuai
- Sertakan docstring untuk fungsi dan kelas
- Gunakan fitur Python modern (3.8+)

#### Java
- Ikuti konvensi Spring Boot
- Gunakan fitur Java 21
- Ikuti struktur proyek Maven standar
- Sertakan komentar Javadoc

### Organisasi Berkas

```
<module-number>-<ModuleName>/
├── README.md              # Main module content
├── samples/               # Code examples (if applicable)
│   ├── typescript/
│   ├── python/
│   ├── java/
│   └── ...
└── solution/              # Complete working solutions
    └── <language>/
```

## Build dan Deployment

### Deployment Dokumentasi

Repositori menggunakan GitHub Pages atau serupa untuk hosting dokumentasi (jika berlaku). Perubahan pada cabang utama memicu:

1. Alur kerja terjemahan (`.github/workflows/co-op-translator.yml`)
2. Terjemahan otomatis semua file markdown berbahasa Inggris
3. Lokalisasi gambar sesuai kebutuhan

### Tidak Memerlukan Proses Build

Repositori ini terutama berisi dokumentasi markdown. Tidak diperlukan langkah kompilasi atau build untuk konten kurikulum inti.

### Deployment Proyek Sampel

Proyek sampel individu mungkin memiliki instruksi deployment:
- Lihat `03-GettingStarted/09-deployment/` untuk panduan deployment server MCP
- Contoh deployment Azure Container Apps di `11-MCPServerHandsOnLabs/`

## Pedoman Kontribusi

### Proses Pull Request

1. **Fork dan Clone**: Fork repositori dan clone fork Anda secara lokal
2. **Buat Cabang**: Gunakan nama cabang deskriptif (misal, `fix/typo-module-3`, `add/python-example`)
3. **Lakukan Perubahan**: Edit hanya file markdown berbahasa Inggris (bukan terjemahan)
4. **Uji Lokal**: Pastikan markdown dirender dengan benar
5. **Kirim PR**: Gunakan judul dan deskripsi PR yang jelas
6. **CLA**: Tandatangani Microsoft Contributor License Agreement saat diminta

### Format Judul PR

Gunakan judul yang jelas dan deskriptif:
- `[Module XX] Deskripsi singkat` untuk perubahan spesifik modul
- `[Samples] Deskripsi` untuk perubahan kode sampel
- `[Docs] Deskripsi` untuk pembaruan dokumentasi umum

### Apa yang Harus Dikontribusikan

- Perbaikan bug pada dokumentasi atau contoh kode
- Contoh kode baru dalam bahasa tambahan
- Klarifikasi dan perbaikan pada konten yang ada
- Studi kasus baru atau contoh praktis
- Laporan masalah untuk konten yang tidak jelas atau salah

### Apa yang TIDAK Boleh Dilakukan

- Jangan mengedit langsung file dalam direktori `translations/`
- Jangan mengedit direktori `translated_images/`
- Jangan menambahkan file biner besar tanpa diskusi
- Jangan mengubah file alur kerja terjemahan tanpa koordinasi

## Catatan Tambahan

### Pemeliharaan Repositori

- **Changelog**: Semua perubahan signifikan didokumentasikan di `changelog.md`
- **Panduan Studi**: Gunakan `study_guide.md` untuk gambaran navigasi kurikulum
- **Template Isu**: Gunakan template isu GitHub untuk laporan bug dan permintaan fitur
- **Kode Etik**: Semua kontributor harus mengikuti Microsoft Open Source Code of Conduct

### Jalur Pembelajaran

Ikuti modul secara berurutan (00-11) untuk pembelajaran optimal:
1. **00-02**: Dasar-dasar (Pengantar, Konsep Inti, Keamanan)
2. **03**: Memulai dengan implementasi praktis
3. **04-05**: Implementasi praktis dan topik lanjutan
4. **06-10**: Komunitas, praktik terbaik, dan aplikasi dunia nyata
5. **11**: Lab integrasi database komprehensif (13 lab berurutan)

### Sumber Dukungan

- **Dokumentasi**: https://modelcontextprotocol.io/
- **Spesifikasi**: https://modelcontextprotocol.io/specification/2026-07-28/
- **Komunitas**: https://github.com/orgs/modelcontextprotocol/discussions
- **Discord**: Server Microsoft Foundry Discord
- **Kursus Terkait**: Lihat README.md untuk jalur pembelajaran Microsoft lainnya

### Pemecahan Masalah Umum

**Q: PR saya gagal pemeriksaan terjemahan**
A: Pastikan Anda hanya mengedit file markdown bahasa Inggris di direktori modul root, bukan versi terjemahan.

**Q: Bagaimana cara menambahkan bahasa baru?**
A: Dukungan bahasa dikelola melalui alur kerja co-op-translator. Buka isu untuk berdiskusi menambahkan bahasa baru.

**Q: Contoh kode tidak berfungsi**
A: Pastikan Anda mengikuti instruksi setup di README sampel spesifik. Periksa bahwa Anda memiliki versi dependensi yang benar terpasang.


**T: Gambar tidak ditampilkan**

A: Verifikasi jalur gambar menggunakan jalur relatif dan tanda garis miring ke depan. Gambar harus berada di direktori `images/` atau `translated_images/` untuk versi yang dilokalkan.

### Pertimbangan Performa

- Alur kerja terjemahan mungkin memakan waktu beberapa menit untuk selesai
- Gambar besar harus dioptimalkan sebelum dikomit
- Pertahankan file markdown individu agar tetap fokus dan berukuran wajar
- Gunakan tautan relatif untuk portabilitas yang lebih baik

### Tata Kelola Proyek

Proyek ini mengikuti praktik open source Microsoft:
- Lisensi MIT untuk kode dan dokumentasi
- Kode Etik Open Source Microsoft
- CLA diperlukan untuk kontribusi
- Masalah keamanan: Ikuti panduan SECURITY.md
- Dukungan: Lihat SUPPORT.md untuk sumber bantuan

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk mencapai akurasi, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sah. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->