# AGENTS.md

## Gambaran Projek

**MCP untuk Pemula** adalah kurikulum pendidikan sumber terbuka untuk mempelajari Protokol Konteks Model (MCP) - sebuah kerangka kerja standard untuk interaksi antara model AI dan aplikasi klien. Repositori ini menyediakan bahan pembelajaran yang lengkap dengan contoh kod praktikal dalam pelbagai bahasa pengaturcaraan.

### Teknologi Utama

- **Bahasa Pengaturcaraan**: C#, Java, JavaScript, TypeScript, Python, Rust
- **Rangka Kerja & SDK**: 
  - MCP SDK (`@modelcontextprotocol/sdk`)
  - Spring Boot (Java)
  - FastMCP (Python)
  - LangChain4j (Java)
- **Pangkalan Data**: PostgreSQL dengan sambungan pgvector
- **Platform Awan**: Azure (Container Apps, OpenAI, Content Safety, Application Insights)
- **Alat Pembinaan**: npm, Maven, pip, Cargo
- **Dokumentasi**: Markdown dengan terjemahan automatik pelbagai bahasa (48+ bahasa)

### Seni Bina

- **11 Modul Teras (00-11)**: Laluan pembelajaran berurutan dari asas hingga topik lanjutan
- **Makmal Praktikal**: Latihan praktikal dengan kod penyelesaian lengkap dalam pelbagai bahasa
- **Projek Contoh**: Pelaksanaan server dan klien MCP yang berfungsi
- **Sistem Terjemahan**: Aliran kerja GitHub Actions automatik untuk sokongan pelbagai bahasa
- **Aset Imej**: Direktori imej berpusat dengan versi yang diterjemah

## Perintah Persediaan

Ini adalah repositori yang memfokuskan pada dokumentasi. Kebanyakan persediaan berlaku dalam projek contoh dan makmal individu.

### Persediaan Repositori

```bash
# Klon repositori
git clone https://github.com/microsoft/mcp-for-beginners.git
cd mcp-for-beginners
```

### Bekerja dengan Projek Contoh

Projek contoh terletak di:
- `03-GettingStarted/samples/` - Contoh khusus bahasa
- `03-GettingStarted/01-first-server/solution/` - Pelaksanaan server pertama
- `03-GettingStarted/02-client/solution/` - Pelaksanaan klien
- `11-MCPServerHandsOnLabs/` - Makmal integrasi pangkalan data yang komprehensif

Setiap projek contoh mengandungi arahan persediaan sendiri:

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
# atau
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

### Kesediaan MCP 7-28

#### Senarai semak kesediaan repositori

- [x] **Kejelasan penyumbang baru**: Fail ini mentakrifkan tujuan repositori,
  struktur, peraturan sumbangan, dan laluan persediaan contoh.
- [x] **Perintah bina/ujian/lint dengan bendera tepat**:
  - Lint dokumen repositori:
    `npx --yes markdownlint-cli2 "**/*.md" "#node_modules" "#translations" "#translated_images"`
  - Audit corak pautan dokumen repositori:
    `find . -name "*.md" -not -path "*/node_modules/*" -not -path "./translations/*" -not -path "./translated_images/*" -print0 | xargs -0 grep -En "\[.*\]\(.*\)"`
  - Pengesahan contoh TypeScript:
    `cd 03-GettingStarted/samples/typescript && npm ci && npm test && npm run build`
  - Pengesahan contoh Python:
    `cd 10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp && python -m pip install -e . && pytest -q`
  - Pengesahan contoh Java:
    `cd 03-GettingStarted/samples/java/calculator && mvn -B -ntp test verify`
- [x] **Satu aliran kerja realistik yang boleh menjadi alat MCP**:
  `validate_curriculum_change`
- [x] **Input/output adalah jelas** (lihat spesifikasi di bawah).
- [x] **Kebenaran dan mod kegagalan didokumentasikan** (lihat spesifikasi di bawah).
- [x] **Kebolehtest CI adalah jelas** (perintah deterministik, kod keluar jelas,
  dan output boleh dibaca mesin).

#### Aliran kerja calon alat MCP: `validate_curriculum_change`

##### Matlamat

Memastikan perubahan dokumentasi kurikulum dan kod contoh wakil
berada dalam keadaan sihat sebelum penggabungan.

##### Input

- `changed_paths: string[]` (diperlukan) - laluan relatif yang diubah dalam PR.
- `run_docs_lint: boolean` (lalai `true`)
- `run_links_audit: boolean` (lalai `true`)
- `run_samples: { typescript?: boolean, python?: boolean, java?: boolean }`
  (lalai semua `false`)

##### Output

- `status: "ok" | "failed"`
- `checks: Array<{ name: string, command: string, exit_code: number,
  summary: string }>`
- `artifacts: Array<{ type: "log" | "report", path: string }>`
- `failed_checks: string[]`

##### Kebenaran

- Membaca fail ruang kerja dan menulis artifak yang dijana alat (contoh, laporan lint,
  log ujian) sahaja; tiada penulisan ke `translations/` atau
  `translated_images/`.
- Melaksanakan perintah shell tempatan.
- Akses rangkaian pilihan hanya untuk pemulihan pakej (`npm ci`,
  `python -m pip install`, penyelesaian pergantungan `mvn`).
- Tiada kebenaran untuk menolak, menggabung, atau mengubah `translations/` atau
  `translated_images/`.

##### Mod kegagalan

- `E_NO_INPUT_PATHS`: `changed_paths` kosong.
- `E_INVALID_PATH`: laluan input melepasi akar repositori.
- `E_LINT_FAILED`: lint markdown keluar kod bukan sifar.
- `E_LINK_AUDIT_FAILED`: perintah audit pautan keluar kod bukan sifar.
- `E_SAMPLE_TEST_FAILED`: ujian/pembinaan contoh keluar kod bukan sifar.
- `E_TIMEOUT`: perintah melebihi masa tamat yang ditetapkan.

##### Kontrak CI yang disyorkan

Untuk mengautomasikan pengesahan, konfigurasikan kerja CI yang:

- Dicetuskan pada permintaan tarik yang menyentuh `*.md`, kod contoh, atau fail ini.
- Menjalankan perintah tepat yang disenaraikan di atas.
- Memelihara log sebagai artifak.
- Gagal kerja jika terdapat sebarang kod keluar bukan sifar.

#### Jika anda menghasilkan server MCP dari repo ini

- [ ] Baca draf changelog untuk MCP 7-28:
  <https://modelcontextprotocol.io/specification/draft/changelog>
- [ ] Jalankan server anda dengan beta SDK:
  <https://blog.modelcontextprotocol.io/posts/sdk-betas-2026-07-28/>
- [ ] Keluarkan andaian sesi dan handshake; anggap setiap permintaan sebagai
  berdiri sendiri:
  <https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/#a-stateless-protocol>
- [ ] Hantar header `Mcp-Method` dan `Mcp-Name` untuk permintaan HTTP mentah:
  <https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/#routable-cacheable-traceable>
- [ ] Audit kod ralat yang dikodkan keras (`missing resource` dipindahkan dari `-32002` ke `-32602`).

- [ ] Tandakan dan rancangkan migrasi untuk akar, pensampelan, dan
  log yang tamat tempoh:
  <https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/#roots-sampling-and-logging-are-deprecated>
- [ ] Migrasi dari API Tugas `2025-11-25` yang eksperimental:
  <https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/#tasks-graduates-to-an-extension>
- [ ] Semak pengesahan untuk pengukuhan OAuth dan OpenID Connect:
  <https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/#authorization-hardening>

### Struktur Dokumentasi

- **Modul 00-11**: Kandungan kurikulum teras dalam urutan berperingkat
- **translations/**: Versi khusus bahasa (dijana automatik, jangan sunting terus)
- **translated_images/**: Versi imej yang dilokalkan (dijana automatik)
- **images/**: Imej dan rajah sumber

### Membuat Perubahan Dokumentasi

1. Sunting hanya fail markdown Bahasa Inggeris dalam direktori modul akar (00-11)
2. Kemas kini imej dalam direktori `images/` jika perlu
3. Tindakan GitHub co-op-translator akan menjana terjemahan secara automatik
4. Terjemahan dijana semula apabila ada push ke cawangan utama

### Bekerja dengan Terjemahan

- **Terjemahan Automatik**: Aliran kerja GitHub Actions mengendalikan semua terjemahan
- Jangan sunting fail dalam direktori `translations/` secara manual
- Metadata terjemahan dimasukkan dalam setiap fail terjemahan
- Bahasa yang disokong: 48+ bahasa termasuk Arab, Cina, Perancis, Jerman, Hindi, Jepun, Korea, Portugis, Rusia, Sepanyol, dan banyak lagi

## Arahan Ujian

### Pengesahan Dokumentasi

Oleh kerana ini terutamanya repositori dokumentasi, ujian difokuskan pada:

1. **Audit Corak Pautan**: Senaraikan pautan Markdown untuk semakan

   ```bash
   # Senaraikan pautan Markdown (audit corak)
   find . -name "*.md" -not -path "*/node_modules/*" -not -path "./translations/*" -not -path "./translated_images/*" -print0 | xargs -0 grep -En "\[.*\]\(.*\)"
   ```

2. **Pengesahan Contoh Kod**: Uji bahawa contoh kod boleh disusun/dijalankan

   ```bash
   # Navigasi ke sampel tertentu dan jalankan ujian-ujiannya
   cd 03-GettingStarted/samples/typescript
   npm install && npm test
   ```

3. **Linting Markdown**: Periksa konsistensi format

   ```bash
   # Gunakan markdownlint jika perlu
   npx --yes markdownlint-cli2 "**/*.md" "#node_modules" "#translations" "#translated_images"
   ```

### Ujian Projek Sampel

Setiap sampel mengikut bahasa termasuk pendekatan ujian tersendiri:

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

## Panduan Gaya Kod

### Gaya Dokumentasi

- Gunakan bahasa yang jelas dan mesra pemula
- Sertakan contoh kod dalam pelbagai bahasa apabila berkenaan
- Ikuti amalan terbaik markdown:
  - Gunakan header gaya ATX (`#` sintaks)
  - Gunakan blok kod berpagar dengan pengecam bahasa
  - Sertakan teks alt yang deskriptif untuk imej
  - Kekalkan panjang baris yang munasabah (tiada had keras, tapi berhemah)

### Gaya Contoh Kod

#### TypeScript/JavaScript
- Gunakan modul ES (`import`/`export`)
- Ikuti konvensyen mod ketat TypeScript
- Sertakan anotasi jenis
- Sasaran ES2022

#### Python
- Ikuti garis panduan gaya PEP 8
- Gunakan petunjuk jenis apabila sesuai
- Sertakan docstring untuk fungsi dan kelas
- Gunakan ciri Python moden (3.8+)

#### Java
- Ikuti konvensyen Spring Boot
- Gunakan ciri Java 21
- Ikuti struktur projek Maven standard
- Sertakan komen Javadoc

### Pengurusan Fail

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

## Pembinaan dan Penghantaran

### Penghantaran Dokumentasi

Repositori menggunakan GitHub Pages atau yang serupa untuk pengehosan dokumentasi (jika berkenaan). Perubahan pada cawangan utama akan mencetuskan:

1. Aliran kerja terjemahan (`.github/workflows/co-op-translator.yml`)
2. Terjemahan automatik semua fail markdown Bahasa Inggeris
3. Pelokalan imej jika diperlukan

### Tiada Proses Pembinaan Diperlukan

Repositori ini terutamanya mengandungi dokumentasi markdown. Tiada langkah penyusunan atau pembinaan diperlukan untuk kandungan kurikulum teras.

### Penghantaran Projek Sampel

Projek sampel individu mungkin mempunyai arahan penghantaran:
- Lihat `03-GettingStarted/09-deployment/` untuk panduan penghantaran pelayan MCP
- Contoh penghantaran Azure Container Apps di `11-MCPServerHandsOnLabs/`

## Panduan Menyumbang

### Proses Permintaan Tarikan

1. **Fork dan Clone**: Fork repositori dan clone fork anda secara tempatan
2. **Buat Cawangan**: Gunakan nama cawangan yang deskriptif (contohnya, `fix/typo-module-3`, `add/python-example`)
3. **Buat Perubahan**: Sunting hanya fail markdown Bahasa Inggeris (bukan terjemahan)
4. **Uji Secara Tempatan**: Sahkan markdown dipaparkan dengan betul
5. **Hantar PR**: Gunakan tajuk dan penerangan PR yang jelas
6. **CLA**: Tandatangani Perjanjian Lesen Penyumbang Microsoft apabila diminta

### Format Tajuk PR

Gunakan tajuk yang jelas dan deskriptif:
- `[Module XX] Penerangan ringkas` untuk perubahan khusus modul
- `[Samples] Penerangan` untuk perubahan kod sampel
- `[Docs] Penerangan` untuk kemas kini dokumentasi umum

### Apa yang Boleh Disumbangkan

- Pembaikan pepijat dalam dokumentasi atau contoh kod
- Contoh kod baru dalam bahasa tambahan
- Penjelasan dan penambahbaikan kandungan sedia ada
- Kajian kes atau contoh praktikal baru
- Laporan isu untuk kandungan yang tidak jelas atau tidak betul

### Apa yang TIDAK Perlu Dilakukan

- Jangan sunting fail dalam direktori `translations/` secara langsung
- Jangan sunting direktori `translated_images/`
- Jangan tambah fail binari besar tanpa perbincangan
- Jangan ubah fail aliran kerja terjemahan tanpa koordinasi

## Nota Tambahan

### Penyelenggaraan Repositori

- **Sejarah Perubahan**: Semua perubahan penting didokumenkan dalam `changelog.md`
- **Panduan Kajian**: Gunakan `study_guide.md` untuk gambaran navigasi kurikulum
- **Templat Isu**: Gunakan templat isu GitHub untuk laporan pepijat dan permintaan ciri
- **Kod Tingkah Laku**: Semua penyumbang mesti mengikuti Kod Tingkah Laku Sumber Terbuka Microsoft

### Laluan Pembelajaran

Ikuti modul secara berperingkat (00-11) untuk pembelajaran optimum:
1. **00-02**: Asas (Pengenalan, Konsep Teras, Keselamatan)
2. **03**: Memulakan dengan pelaksanaan praktikal
3. **04-05**: Pelaksanaan praktikal dan topik lanjutan
4. **06-10**: Komuniti, amalan terbaik, dan aplikasi dunia sebenar
5. **11**: Makmal integrasi pangkalan data menyeluruh (13 makmal berperingkat)

### Sumber Sokongan

- **Dokumentasi**: https://modelcontextprotocol.io/
- **Spesifikasi**: https://spec.modelcontextprotocol.io/
- **Komuniti**: https://github.com/orgs/modelcontextprotocol/discussions
- **Discord**: Pelayan Microsoft Foundry Discord
- **Kursus Berkaitan**: Lihat README.md untuk laluan pembelajaran Microsoft lain

### Penyelesaian Masalah Umum

**S: PR saya gagal pemeriksaan terjemahan**
J: Pastikan anda hanya menyunting fail markdown Bahasa Inggeris dalam direktori modul akar, bukan versi terjemahan.

**S: Bagaimana saya tambah bahasa baru?**
J: Sokongan bahasa diurus melalui aliran kerja co-op-translator. Buka isu untuk berbincang menambah bahasa baru.

**S: Contoh kod tidak berfungsi**

A: Pastikan anda telah mengikuti arahan tetapan dalam README sampel khusus. Semak bahawa anda mempunyai versi pergantungan yang betul dipasang.

**Q: Imej tidak dipaparkan**
A: Sahkan laluan imej adalah relatif dan menggunakan garis miring ke hadapan. Imej harus berada dalam direktori `images/` atau `translated_images/` untuk versi diterjemah.

### Pertimbangan Prestasi

- Aliran kerja terjemahan mungkin mengambil masa beberapa minit untuk diselesaikan
- Imej besar harus dioptimumkan sebelum membuat komit
- Kekalkan fail markdown individu fokus dan bersaiz munasabah
- Gunakan pautan relatif untuk kebolehpindahan yang lebih baik

### Tadbir Urus Projek

Projek ini mengikuti amalan sumber terbuka Microsoft:
- Lesen MIT untuk kod dan dokumentasi
- Kod Etika Sumber Terbuka Microsoft
- CLA diperlukan untuk penyumbangan
- Isu keselamatan: Ikuti panduan SECURITY.md
- Sokongan: Lihat SUPPORT.md untuk sumber bantuan

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan oleh manusia profesional adalah disyorkan. Kami tidak bertanggungjawab terhadap sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->