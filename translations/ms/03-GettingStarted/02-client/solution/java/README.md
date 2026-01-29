# MCP Java Client - Demo Kalkulator

Projek ini menunjukkan cara untuk mencipta klien Java yang berhubung dan berinteraksi dengan pelayan MCP (Model Context Protocol). Dalam contoh ini, kita akan berhubung dengan pelayan kalkulator dari Bab 01 dan melakukan pelbagai operasi matematik.

## Prasyarat

Sebelum menjalankan klien ini, anda perlu:

1. **Mulakan Pelayan Kalkulator** dari Bab 01:
   - Pergi ke direktori pelayan kalkulator: `03-GettingStarted/01-first-server/solution/java/`
   - Bina dan jalankan pelayan kalkulator:
     ```cmd
     cd ..\01-first-server\solution\java
     .\mvnw clean install -DskipTests
     java -jar target\calculator-server-0.0.1-SNAPSHOT.jar
     ```
   - Pelayan sepatutnya berjalan di `http://localhost:8080`

2. **Java 21 atau lebih tinggi** dipasang pada sistem anda  
3. **Maven** (termasuk melalui Maven Wrapper)

## Apakah SDKClient?

`SDKClient` adalah aplikasi Java yang menunjukkan cara untuk:
- Berhubung dengan pelayan MCP menggunakan pengangkutan Server-Sent Events (SSE)
- Senaraikan alat yang tersedia dari pelayan
- Panggil pelbagai fungsi kalkulator secara jauh
- Mengendalikan respons dan memaparkan keputusan

## Cara Ia Berfungsi

Klien menggunakan rangka kerja Spring AI MCP untuk:

1. **Mewujudkan Sambungan**: Mencipta pengangkutan WebFlux SSE untuk berhubung dengan pelayan kalkulator  
2. **Inisialisasi Klien**: Menyediakan klien MCP dan mewujudkan sambungan  
3. **Mengesan Alat**: Menyenaraikan semua operasi kalkulator yang tersedia  
4. **Melaksanakan Operasi**: Memanggil pelbagai fungsi matematik dengan data contoh  
5. **Memaparkan Keputusan**: Menunjukkan hasil setiap pengiraan

## Struktur Projek

```
src/
└── main/
    └── java/
        └── com/
            └── microsoft/
                └── mcp/
                    └── sample/
                        └── client/
                            └── SDKClient.java    # Main client implementation
```

## Kebergantungan Utama

Projek ini menggunakan kebergantungan utama berikut:

```xml
<dependency>
    <groupId>org.springframework.ai</groupId>
    <artifactId>spring-ai-starter-mcp-server-webflux</artifactId>
</dependency>
```

Kebergantungan ini menyediakan:  
- `McpClient` - Antara muka klien utama  
- `WebFluxSseClientTransport` - Pengangkutan SSE untuk komunikasi berasaskan web  
- Skema protokol MCP dan jenis permintaan/respons

## Membina Projek

Bina projek menggunakan Maven wrapper:

```cmd
.\mvnw clean install
```

## Menjalankan Klien

```cmd
java -jar .\target\calculator-client-0.0.1-SNAPSHOT.jar
```

**Nota**: Pastikan pelayan kalkulator berjalan di `http://localhost:8080` sebelum menjalankan mana-mana arahan ini.

## Apa Yang Klien Lakukan

Apabila anda menjalankan klien, ia akan:

1. **Berhubung** dengan pelayan kalkulator di `http://localhost:8080`  
2. **Senaraikan Alat** - Memaparkan semua operasi kalkulator yang tersedia  
3. **Lakukan Pengiraan**:  
   - Penambahan: 5 + 3 = 8  
   - Penolakan: 10 - 4 = 6  
   - Pendaraban: 6 × 7 = 42  
   - Pembahagian: 20 ÷ 4 = 5  
   - Kuasa: 2^8 = 256  
   - Punca Kuasa Dua: √16 = 4  
   - Nilai Mutlak: |-5.5| = 5.5  
   - Bantuan: Memaparkan operasi yang tersedia

## Output Dijangka

```
Available Tools = ListToolsResult[tools=[Tool[name=add, description=Add two numbers together, ...], ...]]
Add Result = CallToolResult[content=[TextContent[text="5,00 + 3,00 = 8,00"]], isError=false]
Subtract Result = CallToolResult[content=[TextContent[text="10,00 - 4,00 = 6,00"]], isError=false]
Multiply Result = CallToolResult[content=[TextContent[text="6,00 * 7,00 = 42,00"]], isError=false]
Divide Result = CallToolResult[content=[TextContent[text="20,00 / 4,00 = 5,00"]], isError=false]
Power Result = CallToolResult[content=[TextContent[text="2,00 ^ 8,00 = 256,00"]], isError=false]
Square Root Result = CallToolResult[content=[TextContent[text="√16,00 = 4,00"]], isError=false]
Absolute Result = CallToolResult[content=[TextContent[text="|-5,50| = 5,50"]], isError=false]
Help = CallToolResult[content=[TextContent[text="Basic Calculator MCP Service\n\nAvailable operations:\n1. add(a, b) - Adds two numbers\n2. subtract(a, b) - Subtracts the second number from the first\n..."]], isError=false]
```

**Nota**: Anda mungkin melihat amaran Maven tentang thread yang masih berjalan pada akhir - ini adalah normal untuk aplikasi reaktif dan tidak menunjukkan ralat.

## Memahami Kod

### 1. Persediaan Pengangkutan  
```java
var transport = new WebFluxSseClientTransport(WebClient.builder().baseUrl("http://localhost:8080"));
```  
Ini mencipta pengangkutan SSE (Server-Sent Events) yang berhubung dengan pelayan kalkulator.

### 2. Penciptaan Klien  
```java
var client = McpClient.sync(this.transport).build();
client.initialize();
```  
Mencipta klien MCP secara segerak dan memulakan sambungan.

### 3. Memanggil Alat  
```java
CallToolResult resultAdd = client.callTool(new CallToolRequest("add", Map.of("a", 5.0, "b", 3.0)));
```  
Memanggil alat "add" dengan parameter a=5.0 dan b=3.0.

## Penyelesaian Masalah

### Pelayan Tidak Berjalan  
Jika anda mendapat ralat sambungan, pastikan pelayan kalkulator dari Bab 01 sedang berjalan:  
```
Error: Connection refused
```  
**Penyelesaian**: Mulakan pelayan kalkulator terlebih dahulu.

### Port Sudah Digunakan  
Jika port 8080 sedang digunakan:  
```
Error: Address already in use
```  
**Penyelesaian**: Hentikan aplikasi lain yang menggunakan port 8080 atau ubah pelayan untuk menggunakan port lain.

### Ralat Semasa Membina  
Jika anda menghadapi ralat semasa membina:  
```cmd
.\mvnw clean install -DskipTests
```

## Ketahui Lebih Lanjut

- [Dokumentasi Spring AI MCP](https://docs.spring.io/spring-ai/reference/api/mcp/)  
- [Spesifikasi Model Context Protocol](https://modelcontextprotocol.io/)  
- [Dokumentasi Spring WebFlux](https://docs.spring.io/spring-framework/docs/current/reference/html/web-reactive.html)

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil perhatian bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan profesional oleh manusia adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.