## Penafian Contoh Kod

> **Nota Penting**: Contoh kod di bawah menunjukkan integrasi Model Context Protocol (MCP) dengan fungsi carian web. Walaupun ia mengikuti corak dan struktur SDK MCP rasmi, ia telah dipermudahkan untuk tujuan pembelajaran.
> 
> Contoh-contoh ini mempamerkan:
> 
> 1. **Pelaksanaan Python**: Pelaksanaan pelayan FastMCP yang menyediakan alat carian web dan menyambung ke API carian luaran. Contoh ini menunjukkan pengurusan jangka hayat yang betul, pengendalian konteks, dan pelaksanaan alat mengikut corak [SDK Python MCP rasmi](https://github.com/modelcontextprotocol/python-sdk). Pelayan menggunakan pengangkutan HTTP Streamable yang disyorkan, yang telah menggantikan pengangkutan SSE lama untuk penggunaan produksi.
> 
> 2. **Pelaksanaan JavaScript**: Pelaksanaan TypeScript/JavaScript menggunakan corak FastMCP dari [SDK TypeScript MCP rasmi](https://github.com/modelcontextprotocol/typescript-sdk) untuk mencipta pelayan carian dengan definisi alat dan sambungan klien yang betul. Ia mengikuti corak terkini yang disyorkan untuk pengurusan sesi dan pemeliharaan konteks.
> 
> Contoh-contoh ini memerlukan pengendalian ralat tambahan, pengesahan, dan kod integrasi API khusus untuk penggunaan produksi. Titik akhir API carian yang ditunjukkan (`https://api.search-service.example/search`) adalah tempat letak dan perlu digantikan dengan titik akhir perkhidmatan carian sebenar.
> 
> Untuk butiran pelaksanaan lengkap dan pendekatan terkini, sila rujuk [spesifikasi MCP rasmi](https://spec.modelcontextprotocol.io/) dan dokumentasi SDK.

## Konsep Teras

### Rangka Kerja Model Context Protocol (MCP)

Pada asasnya, Model Context Protocol menyediakan cara standard untuk model AI, aplikasi, dan perkhidmatan bertukar konteks. Dalam carian web masa nyata, rangka kerja ini penting untuk mencipta pengalaman carian berbilang pusingan yang koheren. Komponen utama termasuk:

1. **Seni Bina Klien-Pelayan**: MCP mewujudkan pemisahan jelas antara klien carian (peminta) dan pelayan carian (penyedia), membolehkan model penyebaran yang fleksibel.

2. **Komunikasi JSON-RPC**: Protokol menggunakan JSON-RPC untuk pertukaran mesej, menjadikannya serasi dengan teknologi web dan mudah dilaksanakan merentasi platform berbeza.

3. **Pengurusan Konteks**: MCP mentakrifkan kaedah berstruktur untuk mengekalkan, mengemas kini, dan memanfaatkan konteks carian merentasi pelbagai interaksi.

4. **Definisi Alat**: Keupayaan carian didedahkan sebagai alat standard dengan parameter dan nilai pulangan yang jelas.

5. **Sokongan Penstriman**: Protokol menyokong penstriman hasil, penting untuk carian masa nyata di mana hasil mungkin tiba secara berperingkat.

### Corak Integrasi Carian Web

Apabila mengintegrasikan MCP dengan carian web, beberapa corak muncul:

#### 1. Integrasi Penyedia Carian Terus

```mermaid
graph LR
    Client[MCP Client] --> |MCP Request| Server[MCP Server]
    Server --> |API Call| SearchAPI[Search API]
    SearchAPI --> |Results| Server
    Server --> |MCP Response| Client
```

Dalam corak ini, pelayan MCP berinteraksi terus dengan satu atau lebih API carian, menterjemah permintaan MCP ke panggilan API khusus dan memformat hasil sebagai respons MCP.

#### 2. Carian Federasi dengan Pemeliharaan Konteks

```mermaid
graph LR
    Client[MCP Client] --> |MCP Request| Federation[MCP Federation Layer]
    Federation --> |MCP Request 1| Search1[Search Provider 1]
    Federation --> |MCP Request 2| Search2[Search Provider 2]
    Federation --> |MCP Request 3| Search3[Search Provider 3]
    Search1 --> |MCP Response 1| Federation
    Search2 --> |MCP Response 2| Federation
    Search3 --> |MCP Response 3| Federation
    Federation --> |Aggregated MCP Response| Client
```

Corak ini mengagihkan pertanyaan carian ke beberapa penyedia carian yang serasi MCP, masing-masing mungkin mengkhusus dalam jenis kandungan atau keupayaan carian yang berbeza, sambil mengekalkan konteks yang bersatu.

#### 3. Rantaian Carian Dipertingkatkan Konteks

```mermaid
graph LR
    Client[MCP Client] --> |Query + Context| Server[MCP Server]
    Server --> |1. Query Analysis| NLP[NLP Service]
    NLP --> |Enhanced Query| Server
    Server --> |2. Search Execution| Search[Search Engine]
    Search --> |Raw Results| Server
    Server --> |3. Result Processing| Enhancement[Result Enhancement]
    Enhancement --> |Enhanced Results| Server
    Server --> |Final Results + Updated Context| Client
```

Dalam corak ini, proses carian dibahagikan kepada beberapa peringkat, dengan konteks diperkaya pada setiap langkah, menghasilkan hasil yang semakin relevan.

### Komponen Konteks Carian

Dalam carian web berasaskan MCP, konteks biasanya merangkumi:

- **Sejarah Pertanyaan**: Pertanyaan carian sebelumnya dalam sesi
- **Keutamaan Pengguna**: Bahasa, wilayah, tetapan carian selamat
- **Sejarah Interaksi**: Hasil yang diklik, masa yang dihabiskan pada hasil
- **Parameter Carian**: Penapis, susunan, dan pengubah carian lain
- **Pengetahuan Domain**: Konteks khusus subjek yang relevan dengan carian
- **Konteks Temporal**: Faktor relevansi berasaskan masa
- **Keutamaan Sumber**: Sumber maklumat yang dipercayai atau disukai

## Kes Penggunaan dan Aplikasi

### Penyelidikan dan Pengumpulan Maklumat

MCP meningkatkan aliran kerja penyelidikan dengan:

- Memelihara konteks penyelidikan merentasi sesi carian
- Membolehkan pertanyaan yang lebih canggih dan relevan secara kontekstual
- Menyokong federasi carian pelbagai sumber
- Memudahkan pengekstrakan pengetahuan dari hasil carian

### Pemantauan Berita dan Trend Masa Nyata

Carian berkuasa MCP menawarkan kelebihan untuk pemantauan berita:

- Penemuan hampir masa nyata cerita berita yang muncul
- Penapisan kontekstual maklumat yang relevan
- Penjejakan topik dan entiti merentasi pelbagai sumber
- Amaran berita peribadi berdasarkan konteks pengguna

### Pelayaran dan Penyelidikan Dipertingkatkan AI

MCP mencipta kemungkinan baru untuk pelayaran dipertingkatkan AI:

- Cadangan carian kontekstual berdasarkan aktiviti pelayar semasa
- Integrasi lancar carian web dengan pembantu berkuasa LLM
- Penapisan carian berbilang pusingan dengan konteks yang dikekalkan
- Peningkatan pemeriksaan fakta dan pengesahan maklumat

## Trend dan Inovasi Masa Depan

### Evolusi MCP dalam Carian Web

Melangkah ke hadapan, kami menjangkakan MCP akan berkembang untuk menangani:

- **Carian Multimodal**: Mengintegrasikan carian teks, imej, audio, dan video dengan konteks yang dikekalkan
- **Carian Terdesentralisasi**: Menyokong ekosistem carian teragih dan federasi
- **Privasi Carian**: Mekanisme carian yang menjaga privasi dengan kesedaran konteks  
- **Pemahaman Pertanyaan**: Penguraian semantik mendalam bagi pertanyaan carian dalam bahasa semula jadi  

### Kemajuan Potensi dalam Teknologi  

Teknologi baru yang akan membentuk masa depan carian MCP:  

1. **Senibina Carian Neural**: Sistem carian berasaskan penanaman yang dioptimumkan untuk MCP  
2. **Konteks Carian Peribadi**: Pembelajaran corak carian pengguna individu dari masa ke masa  
3. **Integrasi Graf Pengetahuan**: Carian kontekstual dipertingkatkan dengan graf pengetahuan khusus domain  
4. **Konteks Merentas Modaliti**: Mengekalkan konteks merentas pelbagai modaliti carian  

## Latihan Praktikal  

### Latihan 1: Menyediakan Saluran Carian MCP Asas  

Dalam latihan ini, anda akan belajar untuk:  
- Mengkonfigurasi persekitaran carian MCP asas  
- Melaksanakan pengendali konteks untuk carian web  
- Menguji dan mengesahkan pemeliharaan konteks sepanjang iterasi carian  

### Latihan 2: Membangunkan Pembantu Penyelidikan dengan Carian MCP  

Cipta aplikasi lengkap yang:  
- Memproses soalan penyelidikan dalam bahasa semula jadi  
- Melakukan carian web dengan kesedaran konteks  
- Mensintesis maklumat dari pelbagai sumber  
- Membentangkan penemuan penyelidikan yang tersusun  

### Latihan 3: Melaksanakan Persekutuan Carian Pelbagai Sumber dengan MCP  

Latihan lanjutan yang merangkumi:  
- Penghantaran pertanyaan berasaskan konteks ke pelbagai enjin carian  
- Pengurutan dan penggabungan keputusan  
- Penghapusan penduaan keputusan carian secara kontekstual  
- Pengendalian metadata khusus sumber  

## Sumber Tambahan  

- [Model Context Protocol Specification](https://spec.modelcontextprotocol.io/) - Spesifikasi rasmi MCP dan dokumentasi protokol terperinci  
- [Model Context Protocol Documentation](https://modelcontextprotocol.io/) - Tutorial terperinci dan panduan pelaksanaan  
- [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk) - Pelaksanaan rasmi MCP dalam Python  
- [MCP TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk) - Pelaksanaan rasmi MCP dalam TypeScript  
- [MCP Reference Servers](https://github.com/modelcontextprotocol/servers) - Pelaksanaan rujukan pelayan MCP  
- [Bing Web Search API Documentation](https://learn.microsoft.com/en-us/bing/search-apis/bing-web-search/overview) - API carian web Microsoft  
- [Google Custom Search JSON API](https://developers.google.com/custom-search/v1/overview) - Enjin carian boleh atur Google  
- [SerpAPI Documentation](https://serpapi.com/search-api) - API halaman keputusan enjin carian  
- [Meilisearch Documentation](https://www.meilisearch.com/docs) - Enjin carian sumber terbuka  
- [Elasticsearch Documentation](https://www.elastic.co/guide/index.html) - Enjin carian dan analitik teragih  
- [LangChain Documentation](https://python.langchain.com/docs/get_started/introduction) - Membangun aplikasi dengan LLM  

## Hasil Pembelajaran  

Dengan menamatkan modul ini, anda akan dapat:  

- Memahami asas carian web masa nyata dan cabarannya  
- Menerangkan bagaimana Model Context Protocol (MCP) meningkatkan keupayaan carian web masa nyata  
- Melaksanakan penyelesaian carian berasaskan MCP menggunakan rangka kerja dan API popular  
- Mereka bentuk dan melancarkan senibina carian yang boleh diskala dan berprestasi tinggi dengan MCP  
- Mengaplikasikan konsep MCP kepada pelbagai kes penggunaan termasuk carian semantik, bantuan penyelidikan, dan pelayaran dipertingkatkan AI  
- Menilai trend terkini dan inovasi masa depan dalam teknologi carian berasaskan MCP  

### Pertimbangan Kepercayaan dan Keselamatan  

Apabila melaksanakan penyelesaian carian web berasaskan MCP, ingat prinsip penting berikut dari spesifikasi MCP:  

1. **Persetujuan dan Kawalan Pengguna**: Pengguna mesti memberi persetujuan secara jelas dan memahami semua akses data dan operasi. Ini amat penting untuk pelaksanaan carian web yang mungkin mengakses sumber data luaran.  

2. **Privasi Data**: Pastikan pengendalian yang sesuai terhadap pertanyaan carian dan keputusan, terutamanya jika mengandungi maklumat sensitif. Laksanakan kawalan akses yang sesuai untuk melindungi data pengguna.  

3. **Keselamatan Alat**: Laksanakan kebenaran dan pengesahan yang betul untuk alat carian, kerana ia berpotensi menjadi risiko keselamatan melalui pelaksanaan kod sewenang-wenangnya. Penerangan tingkah laku alat harus dianggap tidak dipercayai kecuali diperoleh dari pelayan yang dipercayai.  

4. **Dokumentasi Jelas**: Sediakan dokumentasi yang jelas mengenai keupayaan, had, dan pertimbangan keselamatan pelaksanaan carian berasaskan MCP anda, mengikut garis panduan pelaksanaan dari spesifikasi MCP.  

5. **Aliran Persetujuan yang Kukuh**: Bina aliran persetujuan dan kebenaran yang kukuh yang menerangkan dengan jelas fungsi setiap alat sebelum membenarkan penggunaannya, terutamanya untuk alat yang berinteraksi dengan sumber web luaran.  

Untuk maklumat lengkap mengenai keselamatan dan pertimbangan kepercayaan MCP, rujuk [dokumentasi rasmi](https://modelcontextprotocol.io/specification/2025-03-26#security-and-trust-%26-safety).  

## Apa seterusnya  

- [5.12 Entra ID Authentication for Model Context Protocol Servers](../mcp-security-entra/README.md)

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil perhatian bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan profesional oleh manusia adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.