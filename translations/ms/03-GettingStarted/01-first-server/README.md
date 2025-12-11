<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8fdac7600a5f4722643d0f14e15ac259",
  "translation_date": "2025-12-11T07:23:05+00:00",
  "source_file": "03-GettingStarted/01-first-server/README.md",
  "language_code": "ms"
}
-->
# Memulakan dengan MCP

Selamat datang ke langkah pertama anda dengan Model Context Protocol (MCP)! Sama ada anda baru dengan MCP atau ingin memperdalam pemahaman anda, panduan ini akan membimbing anda melalui proses penyediaan dan pembangunan yang penting. Anda akan mengetahui bagaimana MCP membolehkan integrasi lancar antara model AI dan aplikasi, serta belajar bagaimana untuk menyediakan persekitaran anda dengan cepat untuk membina dan menguji penyelesaian yang dikuasakan oleh MCP.

> TLDR; Jika anda membina aplikasi AI, anda tahu bahawa anda boleh menambah alat dan sumber lain ke LLM (model bahasa besar) anda, untuk menjadikan LLM lebih berpengetahuan. Walau bagaimanapun jika anda meletakkan alat dan sumber tersebut pada pelayan, keupayaan aplikasi dan pelayan boleh digunakan oleh mana-mana klien dengan/tanpa LLM.

## Gambaran Keseluruhan

Pelajaran ini menyediakan panduan praktikal tentang penyediaan persekitaran MCP dan membina aplikasi MCP pertama anda. Anda akan belajar bagaimana untuk menyediakan alat dan rangka kerja yang diperlukan, membina pelayan MCP asas, mencipta aplikasi hos, dan menguji pelaksanaan anda.

Model Context Protocol (MCP) adalah protokol terbuka yang menstandardkan bagaimana aplikasi menyediakan konteks kepada LLM. Fikirkan MCP seperti port USB-C untuk aplikasi AI - ia menyediakan cara standard untuk menyambungkan model AI kepada pelbagai sumber data dan alat.

## Objektif Pembelajaran

Menjelang akhir pelajaran ini, anda akan dapat:

- Menyediakan persekitaran pembangunan untuk MCP dalam C#, Java, Python, TypeScript, dan Rust
- Membina dan menyebarkan pelayan MCP asas dengan ciri tersuai (sumber, arahan, dan alat)
- Mencipta aplikasi hos yang menyambung ke pelayan MCP
- Menguji dan menyahpepijat pelaksanaan MCP

## Menyediakan Persekitaran MCP Anda

Sebelum anda mula bekerja dengan MCP, adalah penting untuk menyediakan persekitaran pembangunan anda dan memahami aliran kerja asas. Bahagian ini akan membimbing anda melalui langkah penyediaan awal untuk memastikan permulaan yang lancar dengan MCP.

### Prasyarat

Sebelum menyelami pembangunan MCP, pastikan anda mempunyai:

- **Persekitaran Pembangunan**: Untuk bahasa pilihan anda (C#, Java, Python, TypeScript, atau Rust)
- **IDE/Penyunting**: Visual Studio, Visual Studio Code, IntelliJ, Eclipse, PyCharm, atau mana-mana penyunting kod moden
- **Pengurus Pakej**: NuGet, Maven/Gradle, pip, npm/yarn, atau Cargo
- **Kunci API**: Untuk mana-mana perkhidmatan AI yang anda rancangkan untuk digunakan dalam aplikasi hos anda

## Struktur Pelayan MCP Asas

Pelayan MCP biasanya merangkumi:

- **Konfigurasi Pelayan**: Menyediakan port, pengesahan, dan tetapan lain
- **Sumber**: Data dan konteks yang disediakan kepada LLM
- **Alat**: Fungsi yang boleh dipanggil oleh model
- **Arahan**: Templat untuk menjana atau menyusun teks

Berikut adalah contoh ringkas dalam TypeScript:

```typescript
import { McpServer, ResourceTemplate } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";

// Cipta pelayan MCP
const server = new McpServer({
  name: "Demo",
  version: "1.0.0"
});

// Tambah alat penambahan
server.tool("add",
  { a: z.number(), b: z.number() },
  async ({ a, b }) => ({
    content: [{ type: "text", text: String(a + b) }]
  })
);

// Tambah sumber ucapan dinamik
server.resource(
  "file",
  // Parameter 'list' mengawal bagaimana sumber menyenaraikan fail yang tersedia. Menetapkannya kepada tidak ditakrifkan mematikan penyenaraian untuk sumber ini.
  new ResourceTemplate("file://{path}", { list: undefined }),
  async (uri, { path }) => ({
    contents: [{
      uri: uri.href,
      text: `File, ${path}!`
    }]
  })
);

// Tambah sumber fail yang membaca kandungan fail
server.resource(
  "file",
  new ResourceTemplate("file://{path}", { list: undefined }),
  async (uri, { path }) => {
    let text;
    try {
      text = await fs.readFile(path, "utf8");
    } catch (err) {
      text = `Error reading file: ${err.message}`;
    }
    return {
      contents: [{
        uri: uri.href,
        text
      }]
    };
  }
);

server.prompt(
  "review-code",
  { code: z.string() },
  ({ code }) => ({
    messages: [{
      role: "user",
      content: {
        type: "text",
        text: `Please review this code:\n\n${code}`
      }
    }]
  })
);

// Mula menerima mesej pada stdin dan menghantar mesej pada stdout
const transport = new StdioServerTransport();
await server.connect(transport);
```

Dalam kod sebelumnya kami:

- Mengimport kelas yang diperlukan dari SDK MCP TypeScript.
- Mencipta dan mengkonfigurasi contoh pelayan MCP baru.
- Mendaftar alat tersuai (`calculator`) dengan fungsi pengendali.
- Memulakan pelayan untuk mendengar permintaan MCP yang masuk.

## Menguji dan Menyahpepijat

Sebelum anda mula menguji pelayan MCP anda, adalah penting untuk memahami alat yang tersedia dan amalan terbaik untuk menyahpepijat. Ujian yang berkesan memastikan pelayan anda berfungsi seperti yang dijangka dan membantu anda mengenal pasti serta menyelesaikan isu dengan cepat. Bahagian berikut menggariskan pendekatan yang disyorkan untuk mengesahkan pelaksanaan MCP anda.

MCP menyediakan alat untuk membantu anda menguji dan menyahpepijat pelayan anda:

- **Alat Inspector**, antara muka grafik ini membolehkan anda menyambung ke pelayan anda dan menguji alat, arahan dan sumber anda.
- **curl**, anda juga boleh menyambung ke pelayan anda menggunakan alat baris perintah seperti curl atau klien lain yang boleh mencipta dan menjalankan arahan HTTP.

### Menggunakan MCP Inspector

[MCP Inspector](https://github.com/modelcontextprotocol/inspector) adalah alat ujian visual yang membantu anda:

1. **Mengesan Keupayaan Pelayan**: Mengesan secara automatik sumber, alat, dan arahan yang tersedia
2. **Uji Pelaksanaan Alat**: Cuba parameter berbeza dan lihat respons secara masa nyata
3. **Lihat Metadata Pelayan**: Periksa maklumat pelayan, skema, dan konfigurasi

```bash
# contoh TypeScript, memasang dan menjalankan MCP Inspector
npx @modelcontextprotocol/inspector node build/index.js
```

Apabila anda menjalankan arahan di atas, MCP Inspector akan melancarkan antara muka web tempatan dalam pelayar anda. Anda boleh menjangkakan untuk melihat papan pemuka yang memaparkan pelayan MCP yang didaftarkan, alat, sumber, dan arahan yang tersedia. Antara muka membolehkan anda menguji pelaksanaan alat secara interaktif, memeriksa metadata pelayan, dan melihat respons masa nyata, memudahkan anda mengesahkan dan menyahpepijat pelaksanaan pelayan MCP anda.

Berikut adalah tangkapan skrin bagaimana ia boleh kelihatan:

![MCP Inspector server connection](../../../../translated_images/connected.73d1e042c24075d386cacdd4ee7cd748c16364c277d814e646ff2f7b5eefde85.ms.png)

## Isu dan Penyelesaian Penyediaan Biasa

| Isu | Penyelesaian Mungkin |
|-------|-------------------|
| Sambungan ditolak | Semak jika pelayan sedang berjalan dan port adalah betul |
| Ralat pelaksanaan alat | Semak pengesahan parameter dan pengendalian ralat |
| Kegagalan pengesahan | Sahkan kunci API dan kebenaran |
| Ralat pengesahan skema | Pastikan parameter sepadan dengan skema yang ditakrifkan |
| Pelayan tidak bermula | Semak konflik port atau kebergantungan yang hilang |
| Ralat CORS | Konfigurasikan header CORS yang betul untuk permintaan silang asal |
| Isu pengesahan | Sahkan kesahihan token dan kebenaran |

## Pembangunan Tempatan

Untuk pembangunan dan ujian tempatan, anda boleh menjalankan pelayan MCP terus pada mesin anda:

1. **Mulakan proses pelayan**: Jalankan aplikasi pelayan MCP anda
2. **Konfigurasikan rangkaian**: Pastikan pelayan boleh diakses pada port yang dijangka
3. **Sambungkan klien**: Gunakan URL sambungan tempatan seperti `http://localhost:3000`

```bash
# Contoh: Menjalankan pelayan MCP TypeScript secara tempatan
npm run start
# Pelayan berjalan di http://localhost:3000
```

## Membina Pelayan MCP Pertama Anda

Kami telah membincangkan [Konsep Teras](/01-CoreConcepts/README.md) dalam pelajaran sebelum ini, kini tiba masanya untuk mengaplikasikan pengetahuan itu.

### Apa yang boleh dilakukan oleh pelayan

Sebelum kita mula menulis kod, mari kita ingatkan apa yang boleh dilakukan oleh pelayan:

Pelayan MCP boleh contohnya:

- Mengakses fail dan pangkalan data tempatan
- Menyambung ke API jauh
- Melakukan pengiraan
- Mengintegrasi dengan alat dan perkhidmatan lain
- Menyediakan antara muka pengguna untuk interaksi

Bagus, sekarang kita tahu apa yang boleh kita lakukan, mari kita mula menulis kod.

## Latihan: Mencipta pelayan

Untuk mencipta pelayan, anda perlu mengikuti langkah-langkah berikut:

- Pasang SDK MCP.
- Cipta projek dan sediakan struktur projek.
- Tulis kod pelayan.
- Uji pelayan.

### -1- Cipta projek

#### TypeScript

```sh
# Cipta direktori projek dan inisialisasi projek npm
mkdir calculator-server
cd calculator-server
npm init -y
```

#### Python

```sh
# Cipta direktori projek
mkdir calculator-server
cd calculator-server
# Buka folder dalam Visual Studio Code - Langkau ini jika anda menggunakan IDE yang berbeza
code .
```

#### .NET

```sh
dotnet new console -n McpCalculatorServer
cd McpCalculatorServer
```

#### Java

Untuk Java, cipta projek Spring Boot:

```bash
curl https://start.spring.io/starter.zip \
  -d dependencies=web \
  -d javaVersion=21 \
  -d type=maven-project \
  -d groupId=com.example \
  -d artifactId=calculator-server \
  -d name=McpServer \
  -d packageName=com.microsoft.mcp.sample.server \
  -o calculator-server.zip
```

Ekstrak fail zip:

```bash
unzip calculator-server.zip -d calculator-server
cd calculator-server
# pilihan untuk membuang ujian yang tidak digunakan
rm -rf src/test/java
```

Tambah konfigurasi lengkap berikut ke fail *pom.xml* anda:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    
    <!-- Spring Boot parent for dependency management -->
    <parent>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-parent</artifactId>
        <version>3.5.0</version>
        <relativePath />
    </parent>

    <!-- Project coordinates -->
    <groupId>com.example</groupId>
    <artifactId>calculator-server</artifactId>
    <version>0.0.1-SNAPSHOT</version>
    <name>Calculator Server</name>
    <description>Basic calculator MCP service for beginners</description>

    <!-- Properties -->
    <properties>
        <java.version>21</java.version>
        <maven.compiler.source>21</maven.compiler.source>
        <maven.compiler.target>21</maven.compiler.target>
    </properties>

    <!-- Spring AI BOM for version management -->
    <dependencyManagement>
        <dependencies>
            <dependency>
                <groupId>org.springframework.ai</groupId>
                <artifactId>spring-ai-bom</artifactId>
                <version>1.0.0-SNAPSHOT</version>
                <type>pom</type>
                <scope>import</scope>
            </dependency>
        </dependencies>
    </dependencyManagement>

    <!-- Dependencies -->
    <dependencies>
        <dependency>
            <groupId>org.springframework.ai</groupId>
            <artifactId>spring-ai-starter-mcp-server-webflux</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-actuator</artifactId>
        </dependency>
        <dependency>
         <groupId>org.springframework.boot</groupId>
         <artifactId>spring-boot-starter-test</artifactId>
         <scope>test</scope>
      </dependency>
    </dependencies>

    <!-- Build configuration -->
    <build>
        <plugins>
            <plugin>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-maven-plugin</artifactId>
            </plugin>
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-compiler-plugin</artifactId>
                <configuration>
                    <release>21</release>
                </configuration>
            </plugin>
        </plugins>
    </build>

    <!-- Repositories for Spring AI snapshots -->
    <repositories>
        <repository>
            <id>spring-milestones</id>
            <name>Spring Milestones</name>
            <url>https://repo.spring.io/milestone</url>
            <snapshots>
                <enabled>false</enabled>
            </snapshots>
        </repository>
        <repository>
            <id>spring-snapshots</id>
            <name>Spring Snapshots</name>
            <url>https://repo.spring.io/snapshot</url>
            <releases>
                <enabled>false</enabled>
            </releases>
        </repository>
    </repositories>
</project>
```

#### Rust

```sh
mkdir calculator-server
cd calculator-server
cargo init
```

### -2- Tambah kebergantungan

Sekarang anda telah mencipta projek anda, mari kita tambah kebergantungan seterusnya:

#### TypeScript

```sh
# Jika belum dipasang, pasang TypeScript secara global
npm install typescript -g

# Pasang MCP SDK dan Zod untuk pengesahan skema
npm install @modelcontextprotocol/sdk zod
npm install -D @types/node typescript
```

#### Python

```sh
# Cipta persekitaran maya dan pasang kebergantungan
python -m venv venv
venv\Scripts\activate
pip install "mcp[cli]"
```

#### Java

```bash
cd calculator-server
./mvnw clean install -DskipTests
```

#### Rust

```sh
cargo add rmcp --features server,transport-io
cargo add serde
cargo add tokio --features rt-multi-thread
```

### -3- Cipta fail projek

#### TypeScript

Buka fail *package.json* dan gantikan kandungannya dengan yang berikut untuk memastikan anda boleh membina dan menjalankan pelayan:

```json
{
  "name": "calculator-server",
  "version": "1.0.0",
  "main": "index.js",
  "type": "module",
  "scripts": {
    "build": "tsc",
    "start": "npm run build && node ./build/index.js",
  },
  "keywords": [],
  "author": "",
  "license": "ISC",
  "description": "A simple calculator server using Model Context Protocol",
  "dependencies": {
    "@modelcontextprotocol/sdk": "^1.16.0",
    "zod": "^3.25.76"
  },
  "devDependencies": {
    "@types/node": "^24.0.14",
    "typescript": "^5.8.3"
  }
}
```

Cipta *tsconfig.json* dengan kandungan berikut:

```json
{
  "compilerOptions": {
    "target": "ES2022",
    "module": "Node16",
    "moduleResolution": "Node16",
    "outDir": "./build",
    "rootDir": "./src",
    "strict": true,
    "esModuleInterop": true,
    "skipLibCheck": true,
    "forceConsistentCasingInFileNames": true
  },
  "include": ["src/**/*"],
  "exclude": ["node_modules"]
}
```

Cipta direktori untuk kod sumber anda:

```sh
mkdir src
touch src/index.ts
```

#### Python

Cipta fail *server.py*

```sh
touch server.py
```

#### .NET

Pasang pakej NuGet yang diperlukan:

```sh
dotnet add package ModelContextProtocol --prerelease
dotnet add package Microsoft.Extensions.Hosting
```

#### Java

Untuk projek Java Spring Boot, struktur projek dicipta secara automatik.

#### Rust

Untuk Rust, fail *src/main.rs* dicipta secara lalai apabila anda menjalankan `cargo init`. Buka fail tersebut dan padamkan kod lalai.

### -4- Cipta kod pelayan

#### TypeScript

Cipta fail *index.ts* dan tambah kod berikut:

```typescript
import { McpServer, ResourceTemplate } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";
 
// Cipta pelayan MCP
const server = new McpServer({
  name: "Calculator MCP Server",
  version: "1.0.0"
});
```

Sekarang anda mempunyai pelayan, tetapi ia tidak melakukan banyak, mari kita betulkan itu.

#### Python

```python
# server.py
from mcp.server.fastmcp import FastMCP

# Cipta pelayan MCP
mcp = FastMCP("Demo")
```

#### .NET

```csharp
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;
using Microsoft.Extensions.Logging;
using ModelContextProtocol.Server;
using System.ComponentModel;

var builder = Host.CreateApplicationBuilder(args);
builder.Logging.AddConsole(consoleLogOptions =>
{
    // Configure all logs to go to stderr
    consoleLogOptions.LogToStandardErrorThreshold = LogLevel.Trace;
});

builder.Services
    .AddMcpServer()
    .WithStdioServerTransport()
    .WithToolsFromAssembly();
await builder.Build().RunAsync();

// add features
```

#### Java

Untuk Java, cipta komponen pelayan teras. Pertama, ubah kelas aplikasi utama:

*src/main/java/com/microsoft/mcp/sample/server/McpServerApplication.java*:

```java
package com.microsoft.mcp.sample.server;

import org.springframework.ai.tool.ToolCallbackProvider;
import org.springframework.ai.tool.method.MethodToolCallbackProvider;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.Bean;
import com.microsoft.mcp.sample.server.service.CalculatorService;

@SpringBootApplication
public class McpServerApplication {

    public static void main(String[] args) {
        SpringApplication.run(McpServerApplication.class, args);
    }
    
    @Bean
    public ToolCallbackProvider calculatorTools(CalculatorService calculator) {
        return MethodToolCallbackProvider.builder().toolObjects(calculator).build();
    }
}
```

Cipta perkhidmatan kalkulator *src/main/java/com/microsoft/mcp/sample/server/service/CalculatorService.java*:

```java
package com.microsoft.mcp.sample.server.service;

import org.springframework.ai.tool.annotation.Tool;
import org.springframework.stereotype.Service;

/**
 * Service for basic calculator operations.
 * This service provides simple calculator functionality through MCP.
 */
@Service
public class CalculatorService {

    /**
     * Add two numbers
     * @param a The first number
     * @param b The second number
     * @return The sum of the two numbers
     */
    @Tool(description = "Add two numbers together")
    public String add(double a, double b) {
        double result = a + b;
        return formatResult(a, "+", b, result);
    }

    /**
     * Subtract one number from another
     * @param a The number to subtract from
     * @param b The number to subtract
     * @return The result of the subtraction
     */
    @Tool(description = "Subtract the second number from the first number")
    public String subtract(double a, double b) {
        double result = a - b;
        return formatResult(a, "-", b, result);
    }

    /**
     * Multiply two numbers
     * @param a The first number
     * @param b The second number
     * @return The product of the two numbers
     */
    @Tool(description = "Multiply two numbers together")
    public String multiply(double a, double b) {
        double result = a * b;
        return formatResult(a, "*", b, result);
    }

    /**
     * Divide one number by another
     * @param a The numerator
     * @param b The denominator
     * @return The result of the division
     */
    @Tool(description = "Divide the first number by the second number")
    public String divide(double a, double b) {
        if (b == 0) {
            return "Error: Cannot divide by zero";
        }
        double result = a / b;
        return formatResult(a, "/", b, result);
    }

    /**
     * Calculate the power of a number
     * @param base The base number
     * @param exponent The exponent
     * @return The result of raising the base to the exponent
     */
    @Tool(description = "Calculate the power of a number (base raised to an exponent)")
    public String power(double base, double exponent) {
        double result = Math.pow(base, exponent);
        return formatResult(base, "^", exponent, result);
    }

    /**
     * Calculate the square root of a number
     * @param number The number to find the square root of
     * @return The square root of the number
     */
    @Tool(description = "Calculate the square root of a number")
    public String squareRoot(double number) {
        if (number < 0) {
            return "Error: Cannot calculate square root of a negative number";
        }
        double result = Math.sqrt(number);
        return String.format("√%.2f = %.2f", number, result);
    }

    /**
     * Calculate the modulus (remainder) of division
     * @param a The dividend
     * @param b The divisor
     * @return The remainder of the division
     */
    @Tool(description = "Calculate the remainder when one number is divided by another")
    public String modulus(double a, double b) {
        if (b == 0) {
            return "Error: Cannot divide by zero";
        }
        double result = a % b;
        return formatResult(a, "%", b, result);
    }

    /**
     * Calculate the absolute value of a number
     * @param number The number to find the absolute value of
     * @return The absolute value of the number
     */
    @Tool(description = "Calculate the absolute value of a number")
    public String absolute(double number) {
        double result = Math.abs(number);
        return String.format("|%.2f| = %.2f", number, result);
    }

    /**
     * Get help about available calculator operations
     * @return Information about available operations
     */
    @Tool(description = "Get help about available calculator operations")
    public String help() {
        return "Basic Calculator MCP Service\n\n" +
               "Available operations:\n" +
               "1. add(a, b) - Adds two numbers\n" +
               "2. subtract(a, b) - Subtracts the second number from the first\n" +
               "3. multiply(a, b) - Multiplies two numbers\n" +
               "4. divide(a, b) - Divides the first number by the second\n" +
               "5. power(base, exponent) - Raises a number to a power\n" +
               "6. squareRoot(number) - Calculates the square root\n" + 
               "7. modulus(a, b) - Calculates the remainder of division\n" +
               "8. absolute(number) - Calculates the absolute value\n\n" +
               "Example usage: add(5, 3) will return 5 + 3 = 8";
    }

    /**
     * Format the result of a calculation
     */
    private String formatResult(double a, String operator, double b, double result) {
        return String.format("%.2f %s %.2f = %.2f", a, operator, b, result);
    }
}
```

**Komponen pilihan untuk perkhidmatan sedia produksi:**

Cipta konfigurasi permulaan *src/main/java/com/microsoft/mcp/sample/server/config/StartupConfig.java*:

```java
package com.microsoft.mcp.sample.server.config;

import org.springframework.boot.CommandLineRunner;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

@Configuration
public class StartupConfig {
    
    @Bean
    public CommandLineRunner startupInfo() {
        return args -> {
            System.out.println("\n" + "=".repeat(60));
            System.out.println("Calculator MCP Server is starting...");
            System.out.println("SSE endpoint: http://localhost:8080/sse");
            System.out.println("Health check: http://localhost:8080/actuator/health");
            System.out.println("=".repeat(60) + "\n");
        };
    }
}
```

Cipta pengawal kesihatan *src/main/java/com/microsoft/mcp/sample/server/controller/HealthController.java*:

```java
package com.microsoft.mcp.sample.server.controller;

import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;
import java.time.LocalDateTime;
import java.util.HashMap;
import java.util.Map;

@RestController
public class HealthController {
    
    @GetMapping("/health")
    public ResponseEntity<Map<String, Object>> healthCheck() {
        Map<String, Object> response = new HashMap<>();
        response.put("status", "UP");
        response.put("timestamp", LocalDateTime.now().toString());
        response.put("service", "Calculator MCP Server");
        return ResponseEntity.ok(response);
    }
}
```

Cipta pengendali pengecualian *src/main/java/com/microsoft/mcp/sample/server/exception/GlobalExceptionHandler.java*:

```java
package com.microsoft.mcp.sample.server.exception;

import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.ExceptionHandler;
import org.springframework.web.bind.annotation.RestControllerAdvice;

@RestControllerAdvice
public class GlobalExceptionHandler {

    @ExceptionHandler(IllegalArgumentException.class)
    public ResponseEntity<ErrorResponse> handleIllegalArgumentException(IllegalArgumentException ex) {
        ErrorResponse error = new ErrorResponse(
            "Invalid_Input", 
            "Invalid input parameter: " + ex.getMessage());
        return new ResponseEntity<>(error, HttpStatus.BAD_REQUEST);
    }

    public static class ErrorResponse {
        private String code;
        private String message;

        public ErrorResponse(String code, String message) {
            this.code = code;
            this.message = message;
        }

        // Pengambil nilai
        public String getCode() { return code; }
        public String getMessage() { return message; }
    }
}
```

Cipta sepanduk tersuai *src/main/resources/banner.txt*:

```text
_____      _            _       _             
 / ____|    | |          | |     | |            
| |     __ _| | ___ _   _| | __ _| |_ ___  _ __ 
| |    / _` | |/ __| | | | |/ _` | __/ _ \| '__|
| |___| (_| | | (__| |_| | | (_| | || (_) | |   
 \_____\__,_|_|\___|\__,_|_|\__,_|\__\___/|_|   
                                                
Calculator MCP Server v1.0
Spring Boot MCP Application
```

</details>

#### Rust

Tambah kod berikut di bahagian atas fail *src/main.rs*. Ini mengimport perpustakaan dan modul yang diperlukan untuk pelayan MCP anda.

```rust
use rmcp::{
    handler::server::{router::tool::ToolRouter, tool::Parameters},
    model::{ServerCapabilities, ServerInfo},
    schemars, tool, tool_handler, tool_router,
    transport::stdio,
    ServerHandler, ServiceExt,
};
use std::error::Error;
```

Pelayan kalkulator akan menjadi yang mudah yang boleh menambah dua nombor bersama. Mari kita cipta struct untuk mewakili permintaan kalkulator.

```rust
#[derive(Debug, serde::Deserialize, schemars::JsonSchema)]
pub struct CalculatorRequest {
    pub a: f64,
    pub b: f64,
}
```

Seterusnya, cipta struct untuk mewakili pelayan kalkulator. Struct ini akan memegang router alat, yang digunakan untuk mendaftar alat.

```rust
#[derive(Debug, Clone)]
pub struct Calculator {
    tool_router: ToolRouter<Self>,
}
```

Sekarang, kita boleh melaksanakan struct `Calculator` untuk mencipta contoh baru pelayan dan melaksanakan pengendali pelayan untuk menyediakan maklumat pelayan.

```rust
#[tool_router]
impl Calculator {
    pub fn new() -> Self {
        Self {
            tool_router: Self::tool_router(),
        }
    }
}

#[tool_handler]
impl ServerHandler for Calculator {
    fn get_info(&self) -> ServerInfo {
        ServerInfo {
            instructions: Some("A simple calculator tool".into()),
            capabilities: ServerCapabilities::builder().enable_tools().build(),
            ..Default::default()
        }
    }
}
```

Akhir sekali, kita perlu melaksanakan fungsi utama untuk memulakan pelayan. Fungsi ini akan mencipta contoh struct `Calculator` dan menyajikannya melalui input/output standard.

```rust
#[tokio::main]
async fn main() -> Result<(), Box<dyn Error>> {
    let service = Calculator::new().serve(stdio()).await?;
    service.waiting().await?;
    Ok(())
}
```

Pelayan kini disediakan untuk menyediakan maklumat asas tentang dirinya. Seterusnya, kita akan menambah alat untuk melakukan penambahan.

### -5- Menambah alat dan sumber

Tambah alat dan sumber dengan menambah kod berikut:

#### TypeScript

```typescript
server.tool(
  "add",
  { a: z.number(), b: z.number() },
  async ({ a, b }) => ({
    content: [{ type: "text", text: String(a + b) }]
  })
);

server.resource(
  "greeting",
  new ResourceTemplate("greeting://{name}", { list: undefined }),
  async (uri, { name }) => ({
    contents: [{
      uri: uri.href,
      text: `Hello, ${name}!`
    }]
  })
);
```

Alat anda mengambil parameter `a` dan `b` dan menjalankan fungsi yang menghasilkan respons dalam bentuk:

```typescript
{
  contents: [{
    type: "text", content: "some content"
  }]
}
```

Sumber anda diakses melalui string "greeting" dan mengambil parameter `name` serta menghasilkan respons yang serupa dengan alat:

```typescript
{
  uri: "<href>",
  text: "a text"
}
```

#### Python

```python
# Tambah alat penambahan
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


# Tambah sumber ucapan dinamik
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}!"
```

Dalam kod sebelumnya kami telah:

- Mendefinisikan alat `add` yang mengambil parameter `a` dan `b`, kedua-duanya integer.
- Mencipta sumber bernama `greeting` yang mengambil parameter `name`.

#### .NET

Tambah ini ke fail Program.cs anda:

```csharp
[McpServerToolType]
public static class CalculatorTool
{
    [McpServerTool, Description("Adds two numbers")]
    public static string Add(int a, int b) => $"Sum {a + b}";
}
```

#### Java

Alat telah pun dicipta dalam langkah sebelumnya.

#### Rust

Tambah alat baru di dalam blok `impl Calculator`:

```rust
#[tool(description = "Adds a and b")]
async fn add(
    &self,
    Parameters(CalculatorRequest { a, b }): Parameters<CalculatorRequest>,
) -> String {
    (a + b).to_string()
}
```

### -6- Kod akhir

Mari kita tambah kod terakhir yang kita perlukan supaya pelayan boleh bermula:

#### TypeScript

```typescript
// Mula menerima mesej pada stdin dan menghantar mesej pada stdout
const transport = new StdioServerTransport();
await server.connect(transport);
```

Berikut adalah kod penuh:

```typescript
// index.ts
import { McpServer, ResourceTemplate } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";

// Cipta pelayan MCP
const server = new McpServer({
  name: "Calculator MCP Server",
  version: "1.0.0"
});

// Tambah alat penambahan
server.tool(
  "add",
  { a: z.number(), b: z.number() },
  async ({ a, b }) => ({
    content: [{ type: "text", text: String(a + b) }]
  })
);

// Tambah sumber ucapan dinamik
server.resource(
  "greeting",
  new ResourceTemplate("greeting://{name}", { list: undefined }),
  async (uri, { name }) => ({
    contents: [{
      uri: uri.href,
      text: `Hello, ${name}!`
    }]
  })
);

// Mula menerima mesej pada stdin dan menghantar mesej pada stdout
const transport = new StdioServerTransport();
server.connect(transport);
```

#### Python

```python
# server.py
from mcp.server.fastmcp import FastMCP

# Cipta pelayan MCP
mcp = FastMCP("Demo")


# Tambah alat penambahan
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


# Tambah sumber ucapan selamat dinamik
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}!"

# Blok pelaksanaan utama - ini diperlukan untuk menjalankan pelayan
if __name__ == "__main__":
    mcp.run()
```

#### .NET

Cipta fail Program.cs dengan kandungan berikut:

```csharp
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;
using Microsoft.Extensions.Logging;
using ModelContextProtocol.Server;
using System.ComponentModel;

var builder = Host.CreateApplicationBuilder(args);
builder.Logging.AddConsole(consoleLogOptions =>
{
    // Configure all logs to go to stderr
    consoleLogOptions.LogToStandardErrorThreshold = LogLevel.Trace;
});

builder.Services
    .AddMcpServer()
    .WithStdioServerTransport()
    .WithToolsFromAssembly();
await builder.Build().RunAsync();

[McpServerToolType]
public static class CalculatorTool
{
    [McpServerTool, Description("Adds two numbers")]
    public static string Add(int a, int b) => $"Sum {a + b}";
}
```

#### Java

Kelas aplikasi utama lengkap anda harus kelihatan seperti ini:

```java
// McpServerApplication.java
package com.microsoft.mcp.sample.server;

import org.springframework.ai.tool.ToolCallbackProvider;
import org.springframework.ai.tool.method.MethodToolCallbackProvider;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.Bean;
import com.microsoft.mcp.sample.server.service.CalculatorService;

@SpringBootApplication
public class McpServerApplication {

    public static void main(String[] args) {
        SpringApplication.run(McpServerApplication.class, args);
    }
    
    @Bean
    public ToolCallbackProvider calculatorTools(CalculatorService calculator) {
        return MethodToolCallbackProvider.builder().toolObjects(calculator).build();
    }
}
```

#### Rust

Kod akhir untuk pelayan Rust harus kelihatan seperti ini:

```rust
use rmcp::{
    ServerHandler, ServiceExt,
    handler::server::{router::tool::ToolRouter, tool::Parameters},
    model::{ServerCapabilities, ServerInfo},
    schemars, tool, tool_handler, tool_router,
    transport::stdio,
};
use std::error::Error;

#[derive(Debug, serde::Deserialize, schemars::JsonSchema)]
pub struct CalculatorRequest {
    pub a: f64,
    pub b: f64,
}

#[derive(Debug, Clone)]
pub struct Calculator {
    tool_router: ToolRouter<Self>,
}

#[tool_router]
impl Calculator {
    pub fn new() -> Self {
        Self {
            tool_router: Self::tool_router(),
        }
    }
    
    #[tool(description = "Adds a and b")]
    async fn add(
        &self,
        Parameters(CalculatorRequest { a, b }): Parameters<CalculatorRequest>,
    ) -> String {
        (a + b).to_string()
    }
}

#[tool_handler]
impl ServerHandler for Calculator {
    fn get_info(&self) -> ServerInfo {
        ServerInfo {
            instructions: Some("A simple calculator tool".into()),
            capabilities: ServerCapabilities::builder().enable_tools().build(),
            ..Default::default()
        }
    }
}

#[tokio::main]
async fn main() -> Result<(), Box<dyn Error>> {
    let service = Calculator::new().serve(stdio()).await?;
    service.waiting().await?;
    Ok(())
}
```

### -7- Uji pelayan

Mulakan pelayan dengan arahan berikut:

#### TypeScript

```sh
npm run build
```

#### Python

```sh
mcp run server.py
```

> Untuk menggunakan MCP Inspector, gunakan `mcp dev server.py` yang secara automatik melancarkan Inspector dan menyediakan token sesi proksi yang diperlukan. Jika menggunakan `mcp run server.py`, anda perlu memulakan Inspector secara manual dan mengkonfigurasi sambungan.

#### .NET

Pastikan anda berada dalam direktori projek anda:

```sh
cd McpCalculatorServer
dotnet run
```

#### Java

```bash
./mvnw clean install -DskipTests
java -jar target/calculator-server-0.0.1-SNAPSHOT.jar
```

#### Rust

Jalankan arahan berikut untuk memformat dan menjalankan pelayan:

```sh
cargo fmt
cargo run
```

### -8- Jalankan menggunakan inspector

Inspector adalah alat hebat yang boleh memulakan pelayan anda dan membolehkan anda berinteraksi dengannya supaya anda boleh menguji bahawa ia berfungsi. Mari kita mulakan:

> [!NOTE]
> ia mungkin kelihatan berbeza dalam medan "command" kerana ia mengandungi arahan untuk menjalankan pelayan dengan runtime khusus anda/

#### TypeScript

```sh
npx @modelcontextprotocol/inspector node build/index.js
```

atau tambahkannya ke *package.json* anda seperti ini: `"inspector": "npx @modelcontextprotocol/inspector node build/index.js"` dan kemudian jalankan `npm run inspector`

#### Python

Python membalut alat Node.js yang dipanggil inspector. Adalah mungkin untuk memanggil alat tersebut seperti berikut:

```sh
mcp dev server.py
```

Walau bagaimanapun, ia tidak melaksanakan semua kaedah yang tersedia pada alat itu jadi anda disyorkan untuk menjalankan alat Node.js secara langsung seperti di bawah:

```sh
npx @modelcontextprotocol/inspector mcp run server.py
```

Jika anda menggunakan alat atau IDE yang membolehkan anda mengkonfigurasi arahan dan argumen untuk menjalankan skrip, 
pastikan untuk menetapkan `python` dalam medan `Command` dan `server.py` sebagai `Arguments`. Ini memastikan skrip berjalan dengan betul.

#### .NET

Pastikan anda berada dalam direktori projek anda:

```sh
cd McpCalculatorServer
npx @modelcontextprotocol/inspector dotnet run
```

#### Java

Pastikan pelayan kalkulator anda sedang berjalan
Kemudian jalankan pemeriksa:

```cmd
npx @modelcontextprotocol/inspector
```

Dalam antara muka web pemeriksa:

1. Pilih "SSE" sebagai jenis pengangkutan
2. Tetapkan URL kepada: `http://localhost:8080/sse`
3. Klik "Connect"

![Connect](../../../../translated_images/tool.163d33e3ee307e209ef146d8f85060d2f7e83e9f59b3b1699a77204ae0454ad2.ms.png)

**Anda kini disambungkan ke pelayan**
**Bahagian ujian pelayan Java kini selesai**

Bahagian seterusnya adalah tentang berinteraksi dengan pelayan.

Anda sepatutnya melihat antara muka pengguna berikut:

![Connect](../../../../translated_images/connect.141db0b2bd05f096fb1dd91273771fd8b2469d6507656c3b0c9df4b3c5473929.ms.png)

1. Sambungkan ke pelayan dengan memilih butang Connect
  Setelah anda bersambung ke pelayan, anda sepatutnya melihat yang berikut:

  ![Connected](../../../../translated_images/connected.73d1e042c24075d386cacdd4ee7cd748c16364c277d814e646ff2f7b5eefde85.ms.png)

1. Pilih "Tools" dan "listTools", anda sepatutnya melihat "Add" muncul, pilih "Add" dan isi nilai parameter.

  Anda sepatutnya melihat respons berikut, iaitu hasil dari alat "add":

  ![Result of running add](../../../../translated_images/ran-tool.a5a6ee878c1369ec1e379b81053395252a441799dbf23416c36ddf288faf8249.ms.png)

Tahniah, anda telah berjaya mencipta dan menjalankan pelayan pertama anda!

#### Rust

Untuk menjalankan pelayan Rust dengan MCP Inspector CLI, gunakan arahan berikut:

```sh
npx @modelcontextprotocol/inspector cargo run --cli --method tools/call --tool-name add --tool-arg a=1 b=2
```

### SDK Rasmi

MCP menyediakan SDK rasmi untuk pelbagai bahasa:

- [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk) - Diselenggara bersama Microsoft
- [Java SDK](https://github.com/modelcontextprotocol/java-sdk) - Diselenggara bersama Spring AI
- [TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk) - Implementasi rasmi TypeScript
- [Python SDK](https://github.com/modelcontextprotocol/python-sdk) - Implementasi rasmi Python
- [Kotlin SDK](https://github.com/modelcontextprotocol/kotlin-sdk) - Implementasi rasmi Kotlin
- [Swift SDK](https://github.com/modelcontextprotocol/swift-sdk) - Diselenggara bersama Loopwork AI
- [Rust SDK](https://github.com/modelcontextprotocol/rust-sdk) - Implementasi rasmi Rust

## Perkara Penting

- Menyediakan persekitaran pembangunan MCP adalah mudah dengan SDK khusus bahasa
- Membina pelayan MCP melibatkan penciptaan dan pendaftaran alat dengan skema yang jelas
- Ujian dan penyahpepijatan adalah penting untuk pelaksanaan MCP yang boleh dipercayai

## Contoh

- [Java Calculator](../samples/java/calculator/README.md)
- [.Net Calculator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Calculator](../samples/javascript/README.md)
- [TypeScript Calculator](../samples/typescript/README.md)
- [Python Calculator](../../../../03-GettingStarted/samples/python)
- [Rust Calculator](../../../../03-GettingStarted/samples/rust)

## Tugasan

Cipta pelayan MCP ringkas dengan alat pilihan anda:

1. Laksanakan alat dalam bahasa pilihan anda (.NET, Java, Python, TypeScript, atau Rust).
2. Definisikan parameter input dan nilai pulangan.
3. Jalankan alat pemeriksa untuk memastikan pelayan berfungsi seperti yang diingini.
4. Uji pelaksanaan dengan pelbagai input.

## Penyelesaian

[Penyelesaian](./solution/README.md)

## Sumber Tambahan

- [Bina Ejen menggunakan Model Context Protocol di Azure](https://learn.microsoft.com/azure/developer/ai/intro-agents-mcp)
- [MCP Jauh dengan Azure Container Apps (Node.js/TypeScript/JavaScript)](https://learn.microsoft.com/samples/azure-samples/mcp-container-ts/mcp-container-ts/)
- [.NET OpenAI MCP Agent](https://learn.microsoft.com/samples/azure-samples/openai-mcp-agent-dotnet/openai-mcp-agent-dotnet/)

## Apa seterusnya

Seterusnya: [Memulakan dengan Klien MCP](../02-client/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan profesional oleh manusia adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->