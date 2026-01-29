# AGENTS.md

## Gambaran Projek

**MCP untuk Pemula** adalah kurikulum pendidikan sumber terbuka untuk mempelajari Model Context Protocol (MCP) - kerangka kerja standard untuk interaksi antara model AI dan aplikasi klien. Repositori ini menyediakan bahan pembelajaran yang komprehensif dengan contoh kod praktikal dalam pelbagai bahasa pengaturcaraan.

### Teknologi Utama

- **Bahasa Pengaturcaraan**: C#, Java, JavaScript, TypeScript, Python, Rust
- **Kerangka Kerja & SDK**: 
  - MCP SDK (`@modelcontextprotocol/sdk`)
  - Spring Boot (Java)
  - FastMCP (Python)
  - LangChain4j (Java)
- **Pangkalan Data**: PostgreSQL dengan sambungan pgvector
- **Platform Awan**: Azure (Container Apps, OpenAI, Content Safety, Application Insights)
- **Alat Binaan**: npm, Maven, pip, Cargo
- **Dokumentasi**: Markdown dengan terjemahan automatik pelbagai bahasa (48+ bahasa)

### Seni Bina

- **11 Modul Teras (00-11)**: Laluan pembelajaran berurutan dari asas hingga topik lanjutan
- **Makmal Praktikal**: Latihan praktikal dengan kod penyelesaian lengkap dalam pelbagai bahasa
- **Projek Contoh**: Pelaksanaan pelayan MCP dan klien yang berfungsi
- **Sistem Terjemahan**: Aliran kerja GitHub Actions automatik untuk sokongan pelbagai bahasa
- **Aset Imej**: Direktori imej berpusat dengan versi terjemahan

## Perintah Persediaan

Ini adalah repositori yang berfokus pada dokumentasi. Kebanyakan persediaan dilakukan dalam projek contoh dan makmal individu.

### Persediaan Repositori

```bash
# Clone the repository
git clone https://github.com/microsoft/mcp-for-beginners.git
cd mcp-for-beginners
```

### Bekerja dengan Projek Contoh

Projek contoh terletak di:
- `03-GettingStarted/samples/` - Contoh khusus bahasa
- `03-GettingStarted/01-first-server/solution/` - Pelaksanaan pelayan pertama
- `03-GettingStarted/02-client/solution/` - Pelaksanaan klien
- `11-MCPServerHandsOnLabs/` - Makmal integrasi pangkalan data yang komprehensif

Setiap projek contoh mengandungi arahan persediaan tersendiri:

#### Projek TypeScript/JavaScript
```bash
cd <project-directory>
npm install
npm start
```

#### Projek Python
```bash
cd <project-directory>
pip install -r requirements.txt
# or
pip install -e .
python main.py
```

#### Projek Java
```bash
cd <project-directory>
mvn clean install
mvn spring-boot:run
```

## Aliran Kerja Pembangunan

### Struktur Dokumentasi

- **Modul 00-11**: Kandungan kurikulum teras dalam urutan berurutan
- **translations/**: Versi khusus bahasa (dihasilkan secara automatik, jangan edit secara langsung)
- **translated_images/**: Versi imej yang dilokalkan (dihasilkan secara automatik)
- **images/**: Imej dan diagram sumber

### Membuat Perubahan Dokumentasi

1. Edit hanya fail markdown bahasa Inggeris dalam direktori modul akar (00-11)
2. Kemas kini imej dalam direktori `images/` jika diperlukan
3. GitHub Action co-op-translator akan menghasilkan terjemahan secara automatik
4. Terjemahan dijana semula apabila ditolak ke cabang utama

### Bekerja dengan Terjemahan

- **Terjemahan Automatik**: Aliran kerja GitHub Actions mengendalikan semua terjemahan
- **Jangan edit secara manual** fail dalam direktori `translations/`
- Metadata terjemahan disematkan dalam setiap fail terjemahan
- Bahasa yang disokong: 48+ bahasa termasuk Arab, Cina, Perancis, Jerman, Hindi, Jepun, Korea, Portugis, Rusia, Sepanyol, dan banyak lagi

## Arahan Pengujian

### Pengesahan Dokumentasi

Oleh kerana ini adalah repositori dokumentasi, pengujian berfokus pada:

1. **Pengesahan Pautan**: Pastikan semua pautan dalaman berfungsi
```bash
# Check for broken markdown links
find . -name "*.md" -type f | xargs grep -n "\[.*\](../../.*)"
```

2. **Pengesahan Contoh Kod**: Uji bahawa contoh kod boleh disusun/dijalankan
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

### Pengujian Projek Contoh

Setiap contoh khusus bahasa termasuk pendekatan pengujian tersendiri:

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

## Garis Panduan Gaya Kod

### Gaya Dokumentasi

- Gunakan bahasa yang jelas dan mesra pemula
- Sertakan contoh kod dalam pelbagai bahasa jika sesuai
- Ikuti amalan terbaik markdown:
  - Gunakan tajuk gaya ATX (`#` sintaks)
  - Gunakan blok kod berpagar dengan pengecam bahasa
  - Sertakan teks alt deskriptif untuk imej
  - Kekalkan panjang baris yang munasabah (tiada had keras, tetapi masuk akal)

### Gaya Contoh Kod

#### TypeScript/JavaScript
- Gunakan modul ES (`import`/`export`)
- Ikuti konvensyen mod ketat TypeScript
- Sertakan anotasi jenis
- Sasarkan ES2022

#### Python
- Ikuti garis panduan gaya PEP 8
- Gunakan petunjuk jenis jika sesuai
- Sertakan docstring untuk fungsi dan kelas
- Gunakan ciri Python moden (3.8+)

#### Java
- Ikuti konvensyen Spring Boot
- Gunakan ciri Java 21
- Ikuti struktur projek Maven standard
- Sertakan komen Javadoc

### Organisasi Fail

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

## Binaan dan Penghantaran

### Penghantaran Dokumentasi

Repositori menggunakan GitHub Pages atau yang serupa untuk hosting dokumentasi (jika berkenaan). Perubahan pada cabang utama mencetuskan:

1. Aliran kerja terjemahan (`.github/workflows/co-op-translator.yml`)
2. Terjemahan automatik semua fail markdown bahasa Inggeris
3. Lokalisasi imej jika diperlukan

### Tiada Proses Binaan Diperlukan

Repositori ini terutamanya mengandungi dokumentasi markdown. Tiada langkah penyusunan atau binaan diperlukan untuk kandungan kurikulum teras.

### Penghantaran Projek Contoh

Projek contoh individu mungkin mempunyai arahan penghantaran:
- Lihat `03-GettingStarted/09-deployment/` untuk panduan penghantaran pelayan MCP
- Contoh penghantaran Azure Container Apps dalam `11-MCPServerHandsOnLabs/`

## Garis Panduan Penyumbangan

### Proses Permintaan Tarik (Pull Request)

1. **Fork dan Clone**: Fork repositori dan clone fork anda secara tempatan
2. **Buat Cabang**: Gunakan nama cabang yang deskriptif (contoh: `fix/typo-module-3`, `add/python-example`)
3. **Buat Perubahan**: Edit hanya fail markdown bahasa Inggeris (bukan terjemahan)
4. **Uji Secara Tempatan**: Pastikan markdown dirender dengan betul
5. **Hantar PR**: Gunakan tajuk dan deskripsi PR yang jelas
6. **CLA**: Tandatangani Perjanjian Lesen Penyumbang Microsoft apabila diminta

### Format Tajuk PR

Gunakan tajuk yang jelas dan deskriptif:
- `[Module XX] Deskripsi ringkas` untuk perubahan khusus modul
- `[Samples] Deskripsi` untuk perubahan kod contoh
- `[Docs] Deskripsi` untuk kemas kini dokumentasi umum

### Apa yang Boleh Disumbangkan

- Pembetulan bug dalam dokumentasi atau contoh kod
- Contoh kod baru dalam bahasa tambahan
- Penjelasan dan penambahbaikan kepada kandungan sedia ada
- Kajian kes atau contoh praktikal baru
- Laporan isu untuk kandungan yang tidak jelas atau salah

### Apa yang TIDAK Boleh Dilakukan

- Jangan edit secara langsung fail dalam direktori `translations/`
- Jangan edit direktori `translated_images/`
- Jangan tambah fail binari besar tanpa perbincangan
- Jangan ubah fail aliran kerja terjemahan tanpa koordinasi

## Nota Tambahan

### Penyelenggaraan Repositori

- **Changelog**: Semua perubahan penting didokumentasikan dalam `changelog.md`
- **Panduan Belajar**: Gunakan `study_guide.md` untuk gambaran navigasi kurikulum
- **Templat Isu**: Gunakan templat isu GitHub untuk laporan bug dan permintaan ciri
- **Kod Etika**: Semua penyumbang mesti mengikuti Kod Etika Sumber Terbuka Microsoft

### Laluan Pembelajaran

Ikuti modul dalam urutan berurutan (00-11) untuk pembelajaran yang optimum:
1. **00-02**: Asas (Pengenalan, Konsep Teras, Keselamatan)
2. **03**: Bermula dengan pelaksanaan praktikal
3. **04-05**: Pelaksanaan praktikal dan topik lanjutan
4. **06-10**: Komuniti, amalan terbaik, dan aplikasi dunia nyata
5. **11**: Makmal integrasi pangkalan data yang komprehensif (13 makmal berurutan)

### Sumber Sokongan

- **Dokumentasi**: https://modelcontextprotocol.io/
- **Spesifikasi**: https://spec.modelcontextprotocol.io/
- **Komuniti**: https://github.com/orgs/modelcontextprotocol/discussions
- **Discord**: Pelayan Discord Microsoft Azure AI Foundry
- **Kursus Berkaitan**: Lihat README.md untuk laluan pembelajaran Microsoft lain

### Penyelesaian Masalah Biasa

**S: PR saya gagal dalam pemeriksaan terjemahan**
J: Pastikan anda hanya mengedit fail markdown bahasa Inggeris dalam direktori modul akar, bukan versi terjemahan.

**S: Bagaimana saya menambah bahasa baru?**
J: Sokongan bahasa diuruskan melalui aliran kerja co-op-translator. Buka isu untuk membincangkan penambahan bahasa baru.

**S: Contoh kod tidak berfungsi**
J: Pastikan anda telah mengikuti arahan persediaan dalam README contoh tertentu. Periksa bahawa anda mempunyai versi kebergantungan yang betul dipasang.

**S: Imej tidak dipaparkan**
J: Sahkan laluan imej adalah relatif dan gunakan garis miring ke depan. Imej harus berada dalam direktori `images/` atau `translated_images/` untuk versi yang dilokalkan.

### Pertimbangan Prestasi

- Aliran kerja terjemahan mungkin mengambil masa beberapa minit untuk selesai
- Imej besar harus dioptimumkan sebelum komit
- Kekalkan fail markdown individu fokus dan bersaiz munasabah
- Gunakan pautan relatif untuk kebolehgunaan yang lebih baik

### Tadbir Urus Projek

Projek ini mengikuti amalan sumber terbuka Microsoft:
- Lesen MIT untuk kod dan dokumentasi
- Kod Etika Sumber Terbuka Microsoft
- CLA diperlukan untuk penyumbangan
- Isu keselamatan: Ikuti garis panduan dalam SECURITY.md
- Sokongan: Lihat SUPPORT.md untuk sumber bantuan

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk memastikan ketepatan, sila ambil perhatian bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang berwibawa. Untuk maklumat yang kritikal, terjemahan manusia profesional adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.