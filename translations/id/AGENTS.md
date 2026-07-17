# AGENTS.md

## Ikhtisar Proyek

**MCP untuk Pemula** adalah kurikulum pendidikan open-source untuk mempelajari Model Context Protocol (MCP) - sebuah kerangka standar untuk interaksi antara model AI dan aplikasi klien. Repositori ini menyediakan materi pembelajaran komprehensif dengan contoh kode langsung dalam berbagai bahasa pemrograman.

### Teknologi Kunci

- **Bahasa Pemrograman**: C#, Java, JavaScript, TypeScript, Python, Rust
- **Framework & SDK**: 
  - MCP SDK (`@modelcontextprotocol/sdk`)
  - Spring Boot (Java)
  - FastMCP (Python)
  - LangChain4j (Java)
- **Database**: PostgreSQL dengan ekstensi pgvector
- **Platform Cloud**: Azure (Container Apps, OpenAI, Content Safety, Application Insights)
- **Alat Build**: npm, Maven, pip, Cargo
- **Dokumentasi**: Markdown dengan terjemahan otomatis multi-bahasa (lebih dari 48 bahasa)

### Arsitektur

- **11 Modul Inti (00-11)**: Jalur pembelajaran berurutan dari dasar hingga topik lanjutan
- **Lab Praktik**: Latihan praktis dengan kode solusi lengkap dalam berbagai bahasa
- **Proyek Contoh**: Implementasi server dan klien MCP yang berfungsi
- **Sistem Terjemahan**: Alur kerja GitHub Actions otomatis untuk dukungan multi-bahasa
- **Aset Gambar**: Direktori gambar sentral dengan versi terjemahan

## Perintah Setup

Ini adalah repositori yang fokus pada dokumentasi. Sebagian besar pengaturan dilakukan dalam proyek contoh dan lab individu.

### Pengaturan Repositori

```bash
# Kloning repositori
git clone https://github.com/microsoft/mcp-for-beginners.git
cd mcp-for-beginners
```

### Bekerja dengan Proyek Contoh

Proyek contoh berada di:
- `03-GettingStarted/samples/` - Contoh khusus bahasa
- `03-GettingStarted/01-first-server/solution/` - Implementasi server pertama
- `03-GettingStarted/02-client/solution/` - Implementasi klien
- `11-MCPServerHandsOnLabs/` - Lab integrasi database lengkap

Setiap proyek contoh berisi instruksi setup sendiri:

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
- [x] **Perintah build/test/lint dengan flag yang tepat**:
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
- [x] **Input/output eksplisit** (lihat spesifikasi di bawah).
- [x] **Izin dan mode kegagalan didokumentasikan** (lihat spesifikasi di bawah).
- [x] **Kemampuan tes CI eksplisit** (perintah deterministik, kode keluaran eksplisit,
  dan output yang dapat dibaca mesin).

#### Alur kerja alat MCP kandidat: `validate_curriculum_change`

##### Tujuan

Memvalidasi perubahan dokumentasi kurikulum dan kesehatan kode contoh representatif
sebelum penggabungan.

##### Input

- `changed_paths: string[]` (wajib) - jalur relatif yang diubah dalam PR.
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

- Membaca file workspace dan menulis artefak yang dihasilkan alat (misalnya, laporan lint,
  log tes) saja; tidak menulis ke `translations/` atau
  `translated_images/`.
- Menjalankan perintah shell lokal.
- Akses jaringan opsional hanya untuk pemulihan paket (`npm ci`,
  `python -m pip install`, resolusi dependensi `mvn`).
- Tidak memiliki izin untuk mendorong, menggabungkan, atau memodifikasi `translations/` atau
  `translated_images/`.

##### Mode kegagalan

- `E_NO_INPUT_PATHS`: `changed_paths` kosong.
- `E_INVALID_PATH`: jalur input keluar dari root repositori.
- `E_LINT_FAILED`: lint markdown keluar dengan kode bukan nol.
- `E_LINK_AUDIT_FAILED`: perintah audit tautan keluar dengan kode bukan nol.
- `E_SAMPLE_TEST_FAILED`: tes/build contoh keluar dengan kode bukan nol.
- `E_TIMEOUT`: perintah melebihi batas waktu yang dikonfigurasi.

##### Kontrak CI yang dianjurkan

Untuk mengotomatisasi validasi, konfigurasikan pekerjaan CI yang:

- Memicu pada permintaan tarik yang menyentuh `*.md`, kode contoh, atau file ini.
- Menjalankan perintah tepat yang tercantum di atas.
- Menyimpan log sebagai artefak.
- Gagal pada pekerjaan jika ada kode keluar bukan nol.

#### Jika Anda mengirimkan server MCP dari repo ini

- [ ] Baca changelog draf untuk MCP 7-28:
  <https://modelcontextprotocol.io/specification/draft/changelog>
- [ ] Jalankan server Anda dengan SDK beta:
  <https://blog.modelcontextprotocol.io/posts/sdk-betas-2026-07-28/>
- [ ] Hapus asumsi sesi dan handshake; perlakukan setiap permintaan sebagai
  mandiri:
  <https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/#a-stateless-protocol>
- [ ] Kirim header `Mcp-Method` dan `Mcp-Name` untuk permintaan HTTP mentah:
  <https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/#routable-cacheable-traceable>
- [ ] Audit kode kesalahan yang dikodekan keras (`missing resource` dipindahkan dari `-32002` ke `-32602`).

- [ ] Tandai dan rencanakan migrasi untuk roots, sampling, dan
  logging yang sudah deprecated:
  <https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/#roots-sampling-and-logging-are-deprecated>
- [ ] Migrasi dari API Tasks eksperimental `2025-11-25`:
  <https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/#tasks-graduates-to-an-extension>
- [ ] Tinjau otorisasi untuk penguatan OAuth dan OpenID Connect:
  <https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/#authorization-hardening>

### Struktur Dokumentasi

- **Modul 00-11**: Konten kurikulum inti dalam urutan berurutan
- **translations/**: Versi spesifik bahasa (dibuat otomatis, jangan edit langsung)
- **translated_images/**: Versi gambar yang sudah dilokalisasi (dibuat otomatis)
- **images/**: Gambar sumber dan diagram

### Membuat Perubahan pada Dokumentasi

1. Edit hanya berkas markdown bahasa Inggris di direktori modul root (00-11)
2. Perbarui gambar di direktori `images/` jika perlu
3. GitHub Action co-op-translator akan secara otomatis menghasilkan terjemahan
4. Terjemahan dihasilkan ulang saat push ke cabang utama (main)

### Bekerja dengan Terjemahan

- **Terjemahan Otomatis**: Alur kerja GitHub Actions menangani semua terjemahan
- **Jangan edit secara manual** berkas di direktori `translations/`
- Metadata terjemahan disematkan di setiap berkas terjemahan
- Bahasa yang didukung: lebih dari 48 bahasa termasuk Arab, Cina, Prancis, Jerman, Hindi, Jepang, Korea, Portugis, Rusia, Spanyol, dan banyak lagi

## Instruksi Pengujian

### Validasi Dokumentasi

Karena ini terutama adalah repositori dokumentasi, pengujian difokuskan pada:

1. **Audit Pola Link**: Daftar link Markdown untuk ditinjau

   ```bash
   # Daftar tautan Markdown (audit pola)
   find . -name "*.md" -not -path "*/node_modules/*" -not -path "./translations/*" -not -path "./translated_images/*" -print0 | xargs -0 grep -En "\[.*\]\(.*\)"
   ```

2. **Validasi Contoh Kode**: Uji agar contoh kode dapat dikompilasi/dijalankan

   ```bash
   # Navigasi ke sampel tertentu dan jalankan ujiannya
   cd 03-GettingStarted/samples/typescript
   npm install && npm test
   ```

3. **Linting Markdown**: Periksa konsistensi format

   ```bash
   # Gunakan markdownlint jika diperlukan
   npx --yes markdownlint-cli2 "**/*.md" "#node_modules" "#translations" "#translated_images"
   ```

### Pengujian Proyek Contoh

Setiap contoh bahasa memiliki pendekatan pengujian sendiri:

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
- Sertakan contoh kode dalam berbagai bahasa bila relevan
- Ikuti praktik terbaik markdown:
  - Gunakan header gaya ATX (sintaks `#`)
  - Gunakan blok kode berpagar dengan identifikasi bahasa
  - Sertakan teks alt yang deskriptif untuk gambar
  - Jaga panjang baris agar wajar (tidak ada batas keras, tapi gunakan penilaian)

### Gaya Contoh Kode

#### TypeScript/JavaScript
- Gunakan modul ES (`import`/`export`)
- Ikuti konvensi mode ketat TypeScript
- Sertakan anotasi tipe
- Targetkan ES2022

#### Python
- Ikuti pedoman gaya PEP 8
- Gunakan petunjuk tipe bila sesuai
- Sertakan docstring untuk fungsi dan kelas
- Gunakan fitur modern Python (3.8+)

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

## Proses Build dan Deployment

### Deployment Dokumentasi

Repositori menggunakan GitHub Pages atau sejenisnya untuk hosting dokumentasi (jika berlaku). Perubahan pada cabang utama memicu:

1. Alur kerja terjemahan (`.github/workflows/co-op-translator.yml`)
2. Terjemahan otomatis semua berkas markdown bahasa Inggris
3. Lokalisasi gambar jika diperlukan

### Tidak Memerlukan Proses Build

Repositori ini terutama berisi dokumentasi markdown. Tidak diperlukan langkah kompilasi atau build untuk konten kurikulum inti.

### Deployment Proyek Contoh

Proyek contoh individual mungkin memiliki instruksi deployment:
- Lihat `03-GettingStarted/09-deployment/` untuk panduan deployment server MCP
- Contoh deployment Azure Container Apps di `11-MCPServerHandsOnLabs/`

## Pedoman Kontribusi

### Proses Pull Request

1. **Fork dan Clone**: Fork repositori dan clone fork Anda secara lokal
2. **Buat Cabang**: Gunakan nama cabang yang deskriptif (misal, `fix/typo-module-3`, `add/python-example`)
3. **Buat Perubahan**: Edit hanya berkas markdown bahasa Inggris (bukan terjemahan)
4. **Uji Secara Lokal**: Pastikan markdown dirender dengan benar
5. **Kirim PR**: Gunakan judul dan deskripsi PR yang jelas
6. **CLA**: Tanda tangani Microsoft Contributor License Agreement saat diminta

### Format Judul PR

Gunakan judul yang jelas dan deskriptif:
- `[Module XX] Deskripsi singkat` untuk perubahan spesifik modul
- `[Samples] Deskripsi` untuk perubahan contoh kode
- `[Docs] Deskripsi` untuk pembaruan dokumentasi umum

### Apa yang Harus Dikontribusikan

- Perbaikan bug di dokumentasi atau contoh kode
- Contoh kode baru dalam bahasa tambahan
- Klarifikasi dan peningkatan untuk konten yang ada
- Studi kasus baru atau contoh praktis
- Laporan isu untuk konten yang tidak jelas atau salah

### Apa yang Tidak Boleh Dilakukan

- Jangan edit langsung berkas di direktori `translations/`
- Jangan edit direktori `translated_images/`
- Jangan tambahkan berkas biner besar tanpa diskusi
- Jangan ubah berkas alur terjemahan tanpa koordinasi

## Catatan Tambahan

### Pemeliharaan Repositori

- **Catatan Perubahan**: Semua perubahan signifikan didokumentasikan di `changelog.md`
- **Panduan Studi**: Gunakan `study_guide.md` untuk gambaran navigasi kurikulum
- **Template Isu**: Gunakan template isu GitHub untuk laporan bug dan permintaan fitur
- **Kode Etik**: Semua kontributor harus mengikuti Kode Etik Open Source Microsoft

### Jalur Pembelajaran

Ikuti modul secara berurutan (00-11) untuk pembelajaran optimal:
1. **00-02**: Dasar-dasar (Pengantar, Konsep Inti, Keamanan)
2. **03**: Memulai dengan implementasi langsung
3. **04-05**: Implementasi praktis dan topik lanjutan
4. **06-10**: Komunitas, praktik terbaik, dan aplikasi dunia nyata
5. **11**: Lab integrasi database komprehensif (13 lab berurutan)

### Sumber Dukungan

- **Dokumentasi**: https://modelcontextprotocol.io/
- **Spesifikasi**: https://spec.modelcontextprotocol.io/
- **Komunitas**: https://github.com/orgs/modelcontextprotocol/discussions
- **Discord**: Server Discord Microsoft Foundry
- **Kursus Terkait**: Lihat README.md untuk jalur pembelajaran Microsoft lainnya

### Pemecahan Masalah Umum

**Q: PR saya gagal pemeriksaan terjemahan**
A: Pastikan Anda hanya mengedit berkas markdown bahasa Inggris di direktori modul root, bukan versi terjemahan.

**Q: Bagaimana cara menambahkan bahasa baru?**
A: Dukungan bahasa dikelola melalui alur kerja co-op-translator. Buka isu untuk mendiskusikan penambahan bahasa baru.

**Q: Contoh kode tidak berfungsi**

A: Pastikan Anda telah mengikuti petunjuk pengaturan dalam README sampel spesifik tersebut. Periksa bahwa Anda memiliki versi dependensi yang tepat terinstal.

**Q: Gambar tidak tampil**
A: Verifikasi jalur gambar bersifat relatif dan menggunakan garis miring maju. Gambar harus berada di direktori `images/` atau `translated_images/` untuk versi yang dilokalkan.

### Pertimbangan Kinerja

- Alur kerja terjemahan mungkin memerlukan beberapa menit untuk selesai
- Gambar besar harus dioptimalkan sebelum dikomit
- Jaga file markdown individual tetap fokus dan ukurannya wajar
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