# Demo Penstriman HTTP Kalkulator

Projek ini menunjukkan penstriman HTTP menggunakan Server-Sent Events (SSE) dengan Spring Boot WebFlux. Ia terdiri daripada dua aplikasi:

- **Calculator Server**: Perkhidmatan web reaktif yang melakukan pengiraan dan menstrim keputusan menggunakan SSE
- **Calculator Client**: Aplikasi klien yang menggunakan endpoint penstriman

## Prasyarat

- Java 17 atau lebih tinggi
- Maven 3.6 atau lebih tinggi

## Struktur Projek

```
java/
├── calculator-server/     # Spring Boot server with SSE endpoint
│   ├── src/main/java/com/example/calculatorserver/
│   │   ├── CalculatorServerApplication.java
│   │   └── CalculatorController.java
│   └── pom.xml
├── calculator-client/     # Spring Boot client application
│   ├── src/main/java/com/example/calculatorclient/
│   │   └── CalculatorClientApplication.java
│   └── pom.xml
└── README.md
```

## Cara Ia Berfungsi

1. **Calculator Server** menyediakan endpoint `/calculate` yang:
   - Menerima parameter query: `a` (nombor), `b` (nombor), `op` (operasi)
   - Operasi yang disokong: `add`, `sub`, `mul`, `div`
   - Mengembalikan Server-Sent Events dengan kemajuan pengiraan dan keputusan

2. **Calculator Client** menyambung ke server dan:
   - Membuat permintaan untuk mengira `7 * 5`
   - Menggunakan respons penstriman
   - Mencetak setiap acara ke konsol

## Menjalankan Aplikasi

### Pilihan 1: Menggunakan Maven (Disyorkan)

#### 1. Mulakan Calculator Server

Buka terminal dan pergi ke direktori server:

```bash
cd calculator-server
mvn clean package
mvn spring-boot:run
```

Server akan bermula di `http://localhost:8080`

Anda akan melihat output seperti:
```
Started CalculatorServerApplication in X.XXX seconds
Netty started on port 8080 (http)
```

#### 2. Jalankan Calculator Client

Buka **terminal baru** dan pergi ke direktori klien:

```bash
cd calculator-client
mvn clean package
mvn spring-boot:run
```

Klien akan menyambung ke server, melakukan pengiraan, dan memaparkan keputusan penstriman.

### Pilihan 2: Menggunakan Java secara langsung

#### 1. Kompil dan jalankan server:

```bash
cd calculator-server
mvn clean package
java -jar target/calculator-server-0.0.1-SNAPSHOT.jar
```

#### 2. Kompil dan jalankan klien:

```bash
cd calculator-client
mvn clean package
java -jar target/calculator-client-0.0.1-SNAPSHOT.jar
```

## Uji Server Secara Manual

Anda juga boleh menguji server menggunakan pelayar web atau curl:

### Menggunakan pelayar web:
Lawati: `http://localhost:8080/calculate?a=10&b=5&op=add`

### Menggunakan curl:
```bash
curl "http://localhost:8080/calculate?a=10&b=5&op=add" -H "Accept: text/event-stream"
```

## Output Dijangka

Apabila menjalankan klien, anda akan melihat output penstriman seperti:

```
event:info
data:Calculating: 7.0 mul 5.0

event:result
data:35.0
```

## Operasi Disokong

- `add` - Penambahan (a + b)
- `sub` - Penolakan (a - b)
- `mul` - Pendaraban (a * b)
- `div` - Pembahagian (a / b, mengembalikan NaN jika b = 0)

## Rujukan API

### GET /calculate

**Parameter:**
- `a` (wajib): Nombor pertama (double)
- `b` (wajib): Nombor kedua (double)
- `op` (wajib): Operasi (`add`, `sub`, `mul`, `div`)

**Respons:**
- Content-Type: `text/event-stream`
- Mengembalikan Server-Sent Events dengan kemajuan pengiraan dan keputusan

**Contoh Permintaan:**
```
GET /calculate?a=7&b=5&op=mul HTTP/1.1
Host: localhost:8080
Accept: text/event-stream
```

**Contoh Respons:**
```
event: info
data: Calculating: 7.0 mul 5.0

event: result
data: 35.0
```

## Penyelesaian Masalah

### Isu Biasa

1. **Port 8080 sudah digunakan**
   - Hentikan mana-mana aplikasi lain yang menggunakan port 8080
   - Atau tukar port server dalam `calculator-server/src/main/resources/application.yml`

2. **Sambungan ditolak**
   - Pastikan server berjalan sebelum memulakan klien
   - Semak bahawa server berjaya bermula pada port 8080

3. **Isu nama parameter**
   - Projek ini termasuk konfigurasi compiler Maven dengan flag `-parameters`
   - Jika anda menghadapi masalah pengikatan parameter, pastikan projek dibina dengan konfigurasi ini

### Menghentikan Aplikasi

- Tekan `Ctrl+C` di terminal tempat setiap aplikasi dijalankan
- Atau gunakan `mvn spring-boot:stop` jika dijalankan sebagai proses latar belakang

## Teknologi Digunakan

- **Spring Boot 3.3.1** - Rangka kerja aplikasi
- **Spring WebFlux** - Rangka kerja web reaktif
- **Project Reactor** - Perpustakaan aliran reaktif
- **Netty** - Server I/O tanpa sekatan
- **Maven** - Alat binaan
- **Java 17+** - Bahasa pengaturcaraan

## Langkah Seterusnya

Cuba ubah suai kod untuk:
- Menambah lebih banyak operasi matematik
- Sertakan pengendalian ralat untuk operasi tidak sah
- Tambah log permintaan/respons
- Laksanakan pengesahan
- Tambah ujian unit

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil perhatian bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan profesional oleh manusia adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.