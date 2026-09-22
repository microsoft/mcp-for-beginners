# AGENTS.md

## Gambaran Projek

**MCP untuk Pemula** adalah kurikulum pendidikan sumber terbuka untuk mempelajari Model Context Protocol (MCP) - rangka kerja piawai untuk interaksi antara model AI dan aplikasi klien. Repositori ini menyediakan bahan pembelajaran komprehensif dengan contoh kod berasaskan praktikal merentasi pelbagai bahasa pengaturcaraan.

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
- **Dokumentasi**: Markdown dengan penterjemahan automatik pelbagai bahasa (48+ bahasa)

### Seni Bina

- **11 Modul Teras (00-11)**: Laluan pembelajaran berurutan dari asas ke topik lanjutan
- **Makmal Praktikal**: Latihan praktikal dengan kod penyelesaian lengkap dalam pelbagai bahasa
- **Projek Contoh**: Implementasi pelayan dan klien MCP yang berfungsi
- **Sistem Terjemahan**: Aliran kerja GitHub Actions automatik untuk sokongan pelbagai bahasa
- **Aset Imej**: Direktori imej terpusat dengan versi terjemahan

## Arahan Persediaan

Ini adalah repositori berfokuskan dokumentasi. Kebanyakan persediaan berlaku dalam projek contoh dan makmal individu.

### Persediaan Repositori

```bash
# Klon repositori
git clone https://github.com/microsoft/mcp-for-beginners.git
cd mcp-for-beginners
```

### Bekerja dengan Projek Contoh

Projek contoh terletak di:
- `03-GettingStarted/samples/` - Contoh khusus bahasa
- `03-GettingStarted/01-first-server/solution/` - Implementasi pelayan pertama
- `03-GettingStarted/02-client/solution/` - Implementasi klien
- `11-MCPServerHandsOnLabs/` - Makmal integrasi pangkalan data komprehensif

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

- [x] **Kejelasan penyumbang baru**: Fail ini mendefinisikan tujuan repositori,
  struktur, peraturan sumbangan, dan laluan persediaan contoh.
- [x] **Arahan bina/ujian/lint dengan bendera tepat**:
  - Lint dokumentasi repositori:
    `npx --yes markdownlint-cli2 "**/*.md" "#node_modules" "#translations" "#translated_images"`
  - Audit corak pautan dokumentasi repositori:
    `find . -name "*.md" -not -path "*/node_modules/*" -not -path "./translations/*" -not -path "./translated_images/*" -print0 | xargs -0 grep -En "\[.*\]\(.*\)"`
  - Pengesahan contoh TypeScript:
    `cd 03-GettingStarted/samples/typescript && npm ci && npm test && npm run build`
  - Pengesahan contoh Python:
    `cd 10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp && python -m pip install -e . && pytest -q`
  - Pengesahan contoh Java:
    `cd 03-GettingStarted/samples/java/calculator && mvn -B -ntp test verify`
- [x] **Satu aliran kerja realistik yang boleh menjadi alat MCP**:
  `validate_curriculum_change`
- [x] **Input/output adalah nyata** (lihat spesifikasi di bawah).
- [x] **Kebenaran dan mod kegagalan didokumentasikan** (lihat spesifikasi di bawah).
- [x] **Kebolehujian CI nyata** (arahan deterministik, kod keluar nyata,
  dan output boleh dibaca mesin).

#### Aliran kerja calon alat MCP: `validate_curriculum_change`

##### Matlamat

Sahihkan perubahan dokumentasi kurikulum dan kesihatan kod contoh wakil
sebelum penggabungan.

##### Input

- `changed_paths: string[]` (wajib) - laluan relatif yang diubah dalam PR.
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

- Baca fail ruang kerja dan tulis artifak yang dijana alat (contohnya, laporan lint,
  log ujian) sahaja; tiada penulisan ke `translations/` atau
  `translated_images/`.
- Jalankan arahan shell tempatan.
- Akses rangkaian pilihan hanya untuk pemulihan pakej (`npm ci`,
  `python -m pip install`, penyelesaian kebergantungan `mvn`).
- Tiada kebenaran untuk mendorong, menggabungkan, atau mengubah `translations/` atau
  `translated_images/`.

##### Mod kegagalan

- `E_NO_INPUT_PATHS`: `changed_paths` kosong.
- `E_INVALID_PATH`: laluan input melarikan diri dari akar repositori.
- `E_LINT_FAILED`: lint markdown keluar dengan kode bukan sifar.
- `E_LINK_AUDIT_FAILED`: arahan audit pautan keluar dengan kode bukan sifar.
- `E_SAMPLE_TEST_FAILED`: ujian/binaan contoh keluar dengan kode bukan sifar.
- `E_TIMEOUT`: arahan melebihi masa tamat yang ditetapkan.

##### Kontrak CI yang disyorkan

Untuk mengautomasi pengesahan, konfigurasikan kerja CI yang:

- Dicetuskan pada permintaan tarik yang menyentuh `*.md`, kod contoh, atau fail ini.
- Menjalankan arahan tepat yang disenaraikan di atas.
- Menyimpan log sebagai artifak.
- Menganggap gagal kerja pada sebarang kod keluar bukan sifar.

#### Jika anda menghantar pelayan MCP dari repositori ini

- [ ] Baca nota perubahan MCP akhir `2026-07-28`:
  <https://modelcontextprotocol.io/specification/2026-07-28/changelog>
- [ ] Sahkan bahawa pelepasan SDK terpilih menyokong MCP `2026-07-28`:
  <https://modelcontextprotocol.io/docs/sdk>
- [ ] Buang andaian sesi dan persalaman; anggap setiap permintaan sebagai
  berdikari:
  <https://modelcontextprotocol.io/specification/2026-07-28/basic/lifecycle>
- [ ] Hantar pengepala `Mcp-Method` dan `Mcp-Name` untuk permintaan HTTP mentah:
  <https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/streamable-http>
- [ ] Audit kod ralat keras (contoh `sumber hilang` dipindahkan dari `-32002` ke `-32602`).

- [ ] Migrasi Roots, Sampling, Logging, dan Dynamic Client lama
  Pendaftaran:
  <https://modelcontextprotocol.io/specification/2026-07-28/deprecated>
- [ ] Berpindah dari API Tugas `2025-11-25` yang eksperimen:
  <https://modelcontextprotocol.io/extensions/tasks>
- [ ] Semak kebenaran untuk pengukuhan OAuth dan OpenID Connect:
  <https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization>

### Struktur Dokumentasi

- **Modul 00-11**: Kandungan kurikulum teras mengikut urutan berturutan
- **translations/**: Versi bahasa spesifik (auto-dijana, jangan edit terus)
- **translated_images/**: Versi imej yang dilokalkan (auto-dijana)
- **images/**: Imej dan rajah sumber

### Membuat Perubahan Dokumentasi

1. Edit hanya fail markdown Bahasa Inggeris dalam direktori modul akar (00-11)
2. Kemas kini imej dalam direktori `images/` jika perlu
3. Tindakan GitHub co-op-translator akan menjana terjemahan secara automatik
4. Terjemahan dijana semula apabila ada pendorongan ke cawangan utama

### Bekerja dengan Terjemahan

- **Terjemahan Automatik**: Aliran kerja GitHub Actions mengendalikan semua terjemahan
- **JANGAN edit secara manual** fail dalam direktori `translations/`
- Metadata terjemahan disisipkan dalam setiap fail terjemahan
- Bahasa yang disokong: 48+ bahasa termasuk Arab, Cina, Perancis, Jerman, Hindi, Jepun, Korea, Portugis, Rusia, Sepanyol, dan banyak lagi

## Arahan Ujian

### Pengesahan Dokumentasi

Oleh kerana ini adalah repositori dokumentasi utama, ujian memfokuskan pada:

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

3. **Linting Markdown**: Semak konsistensi format

   ```bash
   # Gunakan markdownlint jika perlu
   npx --yes markdownlint-cli2 "**/*.md" "#node_modules" "#translations" "#translated_images"
   ```

### Ujian Projek Contoh

Setiap sampel bahasa spesifik mempunyai pendekatan ujian sendiri:

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
  - Gunakan pengepala gaya ATX (`#` sintaks)
  - Gunakan blok kod ber pagar dengan penunjuk bahasa
  - Sertakan teks alt yang deskriptif untuk imej
  - Kekalkan panjang baris yang munasabah (tiada had keras, tapi berhemah)

### Gaya Contoh Kod

#### TypeScript/JavaScript
- Gunakan modul ES (`import`/`export`)
- Ikuti konvensyen mod ketat TypeScript
- Sertakan anotasi jenis
- Sasarkan ES2022

#### Python
- Ikuti garis panduan gaya PEP 8
- Gunakan petunjuk jenis bila sesuai
- Sertakan docstrings untuk fungsi dan kelas
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

## Pembinaan dan Penempatan

### Penempatan Dokumentasi

Repositori menggunakan GitHub Pages atau serupa untuk pengehosan dokumentasi (jika terpakai). Perubahan pada cawangan utama akan mencetuskan:

1. Aliran kerja terjemahan (`.github/workflows/co-op-translator.yml`)
2. Terjemahan automatik semua fail markdown Bahasa Inggeris
3. Pelokalan imej jika perlu

### Tiada Proses Pembinaan Diperlukan

Repositori ini terutamanya mengandungi dokumentasi markdown. Tiada langkah penyusunan atau pembinaan diperlukan untuk kandungan kurikulum teras.

### Penempatan Projek Contoh

Projek contoh individu mungkin mempunyai arahan penempatan:
- Lihat `03-GettingStarted/09-deployment/` untuk panduan penempatan pelayan MCP
- Contoh penempatan Azure Container Apps dalam `11-MCPServerHandsOnLabs/`

## Garis Panduan Menyumbang

### Proses Permintaan Tarik

1. **Fork dan Clone**: Fork repositori dan clone fork secara tempatan
2. **Buat Cawangan**: Gunakan nama cawangan yang deskriptif (contoh, `fix/typo-module-3`, `add/python-example`)
3. **Buat Perubahan**: Edit hanya fail markdown Bahasa Inggeris (bukan terjemahan)
4. **Uji Secara Tempatan**: Sahkan markdown dipaparkan dengan betul
5. **Hantar PR**: Gunakan tajuk dan penerangan PR yang jelas
6. **CLA**: Tandatangani Perjanjian Lesen Penyumbang Microsoft apabila diminta

### Format Tajuk PR

Gunakan tajuk yang jelas dan deskriptif:
- `[Module XX] Penerangan ringkas` untuk perubahan spesifik modul
- `[Samples] Penerangan` untuk perubahan kod contoh
- `[Docs] Penerangan` untuk kemas kini dokumentasi umum

### Apa yang Perlu Disumbangkan

- Pembetulan pepijat dalam dokumentasi atau contoh kod
- Contoh kod baru dalam bahasa tambahan
- Penjelasan dan penambahbaikan kandungan sedia ada
- Kajian kes baru atau contoh praktikal
- Laporan isu untuk kandungan yang tidak jelas atau salah

### Apa yang TIDAK Perlu Dilakukan

- Jangan terus edit fail dalam direktori `translations/`
- Jangan edit direktori `translated_images/`
- Jangan tambah fail binari besar tanpa perbincangan
- Jangan ubah aliran kerja terjemahan tanpa penyelarasan

## Nota Tambahan

### Penyelenggaraan Repositori

- **Changelog**: Semua perubahan penting didokumentasikan dalam `changelog.md`
- **Panduan Belajar**: Gunakan `study_guide.md` untuk gambaran navigasi kurikulum
- **Templat Isu**: Gunakan templat isu GitHub untuk laporan pepijat dan permintaan ciri
- **Kod Etika**: Semua penyumbang mesti mengikuti Kod Etika Sumber Terbuka Microsoft

### Laluan Pembelajaran

Ikuti modul secara berturutan (00-11) untuk pembelajaran optimum:
1. **00-02**: Asas (Pengenalan, Konsep Teras, Keselamatan)
2. **03**: Memulakan dengan pelaksanaan praktikal
3. **04-05**: Pelaksanaan praktikal dan topik lanjutan
4. **06-10**: Komuniti, amalan terbaik, dan aplikasi dunia sebenar
5. **11**: Makmal integrasi pangkalan data menyeluruh (13 makmal berturut-turut)

### Sumber Sokongan

- **Dokumentasi**: https://modelcontextprotocol.io/
- **Spesifikasi**: https://modelcontextprotocol.io/specification/2026-07-28/
- **Komuniti**: https://github.com/orgs/modelcontextprotocol/discussions
- **Discord**: Pelayan Discord Microsoft Foundry
- **Kursus Berkaitan**: Lihat README.md untuk laluan pembelajaran Microsoft lain

### Troubleshooting Biasa

**S: PR saya gagal pemeriksaan terjemahan**
J: Pastikan anda hanya mengedit fail markdown Bahasa Inggeris dalam direktori modul akar, bukan versi terjemahan.

**S: Bagaimana saya menambah bahasa baru?**
J: Sokongan bahasa dikendalikan melalui aliran kerja co-op-translator. Buka isu untuk berbincang menambah bahasa baru.

**S: Contoh kod tidak berfungsi**
J: Pastikan anda mengikuti arahan persediaan dalam README sampel tertentu. Semak bahawa anda mempunyai versi kebergantungan yang betul dipasang.


**S: Imej tidak dipaparkan**

A: Sahkan laluan imej adalah relatif dan menggunakan garis miring ke hadapan. Imej harus berada dalam direktori `images/` atau `translated_images/` untuk versi yang dilokalkan.

### Pertimbangan Prestasi

- Aliran kerja terjemahan mungkin mengambil masa beberapa minit untuk disiapkan
- Imej bersaiz besar harus dioptimumkan sebelum diserahkan
- Kekalkan fail markdown individu agar fokus dan bersaiz munasabah
- Gunakan pautan relatif untuk kebolehgerakan yang lebih baik

### Tadbir Urus Projek

Projek ini mengikuti amalan sumber terbuka Microsoft:
- Lesen MIT untuk kod dan dokumentasi
- Kod Etika Microsoft Sumber Terbuka
- CLA diperlukan untuk sumbangan
- Isu keselamatan: Ikuti garis panduan SECURITY.md
- Sokongan: Rujuk SUPPORT.md untuk sumber bantuan

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan oleh manusia profesional adalah disyorkan. Kami tidak bertanggungjawab terhadap sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->