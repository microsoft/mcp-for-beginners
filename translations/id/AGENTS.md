# AGENTS.md

## Gambaran Proyek

**MCP untuk Pemula** adalah kurikulum pendidikan sumber terbuka untuk mempelajari Model Context Protocol (MCP) - sebuah kerangka kerja standar untuk interaksi antara model AI dan aplikasi klien. Repository ini menyediakan materi pembelajaran yang komprehensif dengan contoh kode praktis dalam berbagai bahasa pemrograman.

### Teknologi Utama

- **Bahasa Pemrograman**: C#, Java, JavaScript, TypeScript, Python, Rust
- **Framework & SDK**: 
  - MCP SDK (`@modelcontextprotocol/sdk`)
  - Spring Boot (Java)
  - FastMCP (Python)
  - LangChain4j (Java)
- **Basis Data**: PostgreSQL dengan ekstensi pgvector
- **Platform Cloud**: Azure (Container Apps, OpenAI, Content Safety, Application Insights)
- **Alat Build**: npm, Maven, pip, Cargo
- **Dokumentasi**: Markdown dengan terjemahan otomatis multi-bahasa (48+ bahasa)

### Arsitektur

- **11 Modul Inti (00-11)**: Jalur pembelajaran berurutan dari dasar hingga topik lanjutan
- **Lab Praktis**: Latihan praktis dengan kode solusi lengkap dalam berbagai bahasa
- **Proyek Contoh**: Implementasi server dan klien MCP yang berfungsi
- **Sistem Terjemahan**: Workflow GitHub Actions otomatis untuk dukungan multi-bahasa
- **Aset Gambar**: Direktori gambar terpusat dengan versi terjemahan

## Perintah Setup

Ini adalah repository yang berfokus pada dokumentasi. Sebagian besar setup dilakukan dalam proyek contoh dan lab individu.

### Setup Repository

```bash
# Clone the repository
git clone https://github.com/microsoft/mcp-for-beginners.git
cd mcp-for-beginners
```

### Bekerja dengan Proyek Contoh

Proyek contoh terletak di:
- `03-GettingStarted/samples/` - Contoh spesifik bahasa
- `03-GettingStarted/01-first-server/solution/` - Implementasi server pertama
- `03-GettingStarted/02-client/solution/` - Implementasi klien
- `11-MCPServerHandsOnLabs/` - Lab integrasi basis data yang komprehensif

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
# or
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

### Struktur Dokumentasi

- **Modul 00-11**: Konten kurikulum inti dalam urutan berurutan
- **translations/**: Versi spesifik bahasa (dihasilkan otomatis, jangan edit langsung)
- **translated_images/**: Versi gambar yang dilokalkan (dihasilkan otomatis)
- **images/**: Gambar dan diagram sumber

### Membuat Perubahan pada Dokumentasi

1. Edit hanya file markdown bahasa Inggris di direktori modul root (00-11)
2. Perbarui gambar di direktori `images/` jika diperlukan
3. GitHub Action co-op-translator akan secara otomatis menghasilkan terjemahan
4. Terjemahan dihasilkan ulang saat ada push ke cabang utama

### Bekerja dengan Terjemahan

- **Terjemahan Otomatis**: Workflow GitHub Actions menangani semua terjemahan
- **Jangan Edit Secara Manual** file di direktori `translations/`
- Metadata terjemahan disematkan di setiap file terjemahan
- Bahasa yang didukung: 48+ bahasa termasuk Arab, Cina, Prancis, Jerman, Hindi, Jepang, Korea, Portugis, Rusia, Spanyol, dan banyak lagi

## Instruksi Pengujian

### Validasi Dokumentasi

Karena ini terutama adalah repository dokumentasi, pengujian berfokus pada:

1. **Validasi Tautan**: Pastikan semua tautan internal berfungsi
```bash
# Check for broken markdown links
find . -name "*.md" -type f | xargs grep -n "\[.*\](../../.*)"
```

2. **Validasi Contoh Kode**: Uji bahwa contoh kode dapat dikompilasi/dijalankan
```bash
# Navigate to specific sample and run its tests
cd 03-GettingStarted/samples/typescript
npm install && npm test
```

3. **Linting Markdown**: Periksa konsistensi format
```bash
# Use markdownlint if needed
npx markdownlint-cli2 "**/*.md" "#node_modules"
```

### Pengujian Proyek Contoh

Setiap contoh spesifik bahasa memiliki pendekatan pengujian sendiri:

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
- Sertakan contoh kode dalam berbagai bahasa jika memungkinkan
- Ikuti praktik terbaik markdown:
  - Gunakan header gaya ATX (`#` sintaks)
  - Gunakan blok kode berpagar dengan identifikasi bahasa
  - Sertakan teks alt deskriptif untuk gambar
  - Jaga panjang baris tetap masuk akal (tidak ada batas keras, tetapi tetap bijaksana)

### Gaya Contoh Kode

#### TypeScript/JavaScript
- Gunakan modul ES (`import`/`export`)
- Ikuti konvensi mode ketat TypeScript
- Sertakan anotasi tipe
- Targetkan ES2022

#### Python
- Ikuti panduan gaya PEP 8
- Gunakan petunjuk tipe jika sesuai
- Sertakan docstring untuk fungsi dan kelas
- Gunakan fitur Python modern (3.8+)

#### Java
- Ikuti konvensi Spring Boot
- Gunakan fitur Java 21
- Ikuti struktur proyek Maven standar
- Sertakan komentar Javadoc

### Organisasi File

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

Repository ini menggunakan GitHub Pages atau serupa untuk hosting dokumentasi (jika berlaku). Perubahan pada cabang utama memicu:

1. Workflow terjemahan (`.github/workflows/co-op-translator.yml`)
2. Terjemahan otomatis semua file markdown bahasa Inggris
3. Lokalisasi gambar jika diperlukan

### Tidak Ada Proses Build yang Diperlukan

Repository ini terutama berisi dokumentasi markdown. Tidak ada langkah kompilasi atau build yang diperlukan untuk konten kurikulum inti.

### Deployment Proyek Contoh

Proyek contoh individu mungkin memiliki instruksi deployment:
- Lihat `03-GettingStarted/09-deployment/` untuk panduan deployment server MCP
- Contoh deployment Azure Container Apps di `11-MCPServerHandsOnLabs/`

## Panduan Kontribusi

### Proses Pull Request

1. **Fork dan Clone**: Fork repository dan clone fork Anda secara lokal
2. **Buat Cabang**: Gunakan nama cabang yang deskriptif (misalnya, `fix/typo-module-3`, `add/python-example`)
3. **Lakukan Perubahan**: Edit hanya file markdown bahasa Inggris (bukan terjemahan)
4. **Uji Secara Lokal**: Verifikasi bahwa markdown dirender dengan benar
5. **Kirim PR**: Gunakan judul dan deskripsi PR yang jelas
6. **CLA**: Tanda tangani Microsoft Contributor License Agreement saat diminta

### Format Judul PR

Gunakan judul yang jelas dan deskriptif:
- `[Module XX] Deskripsi singkat` untuk perubahan spesifik modul
- `[Samples] Deskripsi` untuk perubahan kode contoh
- `[Docs] Deskripsi` untuk pembaruan dokumentasi umum

### Apa yang Dapat Dikontribusikan

- Perbaikan bug dalam dokumentasi atau contoh kode
- Contoh kode baru dalam bahasa tambahan
- Klarifikasi dan peningkatan konten yang ada
- Studi kasus baru atau contoh praktis
- Laporan masalah untuk konten yang tidak jelas atau salah

### Apa yang Tidak Boleh Dilakukan

- Jangan langsung mengedit file di direktori `translations/`
- Jangan mengedit direktori `translated_images/`
- Jangan menambahkan file biner besar tanpa diskusi
- Jangan mengubah file workflow terjemahan tanpa koordinasi

## Catatan Tambahan

### Pemeliharaan Repository

- **Changelog**: Semua perubahan signifikan didokumentasikan di `changelog.md`
- **Panduan Studi**: Gunakan `study_guide.md` untuk gambaran navigasi kurikulum
- **Template Masalah**: Gunakan template masalah GitHub untuk laporan bug dan permintaan fitur
- **Kode Etik**: Semua kontributor harus mengikuti Microsoft Open Source Code of Conduct

### Jalur Pembelajaran

Ikuti modul secara berurutan (00-11) untuk pembelajaran yang optimal:
1. **00-02**: Dasar-dasar (Pengantar, Konsep Inti, Keamanan)
2. **03**: Memulai dengan implementasi praktis
3. **04-05**: Implementasi praktis dan topik lanjutan
4. **06-10**: Komunitas, praktik terbaik, dan aplikasi dunia nyata
5. **11**: Lab integrasi basis data yang komprehensif (13 lab berurutan)

### Sumber Daya Dukungan

- **Dokumentasi**: https://modelcontextprotocol.io/
- **Spesifikasi**: https://spec.modelcontextprotocol.io/
- **Komunitas**: https://github.com/orgs/modelcontextprotocol/discussions
- **Discord**: Server Discord Microsoft Azure AI Foundry
- **Kursus Terkait**: Lihat README.md untuk jalur pembelajaran Microsoft lainnya

### Pemecahan Masalah Umum

**T: PR saya gagal dalam pemeriksaan terjemahan**
J: Pastikan Anda hanya mengedit file markdown bahasa Inggris di direktori modul root, bukan versi terjemahan.

**T: Bagaimana cara menambahkan bahasa baru?**
J: Dukungan bahasa dikelola melalui workflow co-op-translator. Buka masalah untuk mendiskusikan penambahan bahasa baru.

**T: Contoh kode tidak berfungsi**
J: Pastikan Anda telah mengikuti instruksi setup di README spesifik contoh. Periksa bahwa Anda memiliki versi dependensi yang benar terinstal.

**T: Gambar tidak muncul**
J: Verifikasi bahwa jalur gambar bersifat relatif dan menggunakan garis miring maju. Gambar harus berada di direktori `images/` atau `translated_images/` untuk versi yang dilokalkan.

### Pertimbangan Kinerja

- Workflow terjemahan mungkin memerlukan beberapa menit untuk selesai
- Gambar besar harus dioptimalkan sebelum dikomit
- Jaga file markdown individu tetap fokus dan berukuran wajar
- Gunakan tautan relatif untuk portabilitas yang lebih baik

### Tata Kelola Proyek

Proyek ini mengikuti praktik sumber terbuka Microsoft:
- Lisensi MIT untuk kode dan dokumentasi
- Microsoft Open Source Code of Conduct
- CLA diperlukan untuk kontribusi
- Masalah keamanan: Ikuti pedoman SECURITY.md
- Dukungan: Lihat SUPPORT.md untuk sumber daya bantuan

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan penerjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk memberikan hasil yang akurat, harap diperhatikan bahwa terjemahan otomatis dapat mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang otoritatif. Untuk informasi yang bersifat kritis, disarankan menggunakan jasa penerjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau interpretasi yang keliru yang timbul dari penggunaan terjemahan ini.