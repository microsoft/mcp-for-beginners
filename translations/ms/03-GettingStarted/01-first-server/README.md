<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "726b74589522653d930c7395c9e1fab8",
  "translation_date": "2025-10-20T17:10:30+00:00",
  "source_file": "03-GettingStarted/01-first-server/README.md",
  "language_code": "ms"
}
-->
# Memulakan dengan MCP

Selamat datang ke langkah pertama anda dengan Model Context Protocol (MCP)! Sama ada anda baru dengan MCP atau ingin mendalami pemahaman anda, panduan ini akan membawa anda melalui proses persediaan dan pembangunan yang penting. Anda akan mengetahui bagaimana MCP membolehkan integrasi lancar antara model AI dan aplikasi, serta belajar cara menyediakan persekitaran anda dengan cepat untuk membina dan menguji penyelesaian berkuasa MCP.

> TLDR; Jika anda membina aplikasi AI, anda tahu bahawa anda boleh menambah alat dan sumber lain kepada LLM (model bahasa besar), untuk menjadikan LLM lebih berpengetahuan. Walau bagaimanapun, jika anda meletakkan alat dan sumber tersebut di pelayan, aplikasi dan keupayaan pelayan boleh digunakan oleh mana-mana klien dengan/tanpa LLM.

## Gambaran Keseluruhan

Pelajaran ini menyediakan panduan praktikal untuk menyediakan persekitaran MCP dan membina aplikasi MCP pertama anda. Anda akan belajar cara menyediakan alat dan rangka kerja yang diperlukan, membina pelayan MCP asas, mencipta aplikasi hos, dan menguji pelaksanaan anda.

Model Context Protocol (MCP) adalah protokol terbuka yang menyeragamkan cara aplikasi menyediakan konteks kepada LLM. Fikirkan MCP seperti port USB-C untuk aplikasi AI - ia menyediakan cara standard untuk menghubungkan model AI kepada pelbagai sumber data dan alat.

## Objektif Pembelajaran

Pada akhir pelajaran ini, anda akan dapat:

- Menyediakan persekitaran pembangunan untuk MCP dalam C#, Java, Python, TypeScript, dan Rust
- Membina dan melancarkan pelayan MCP asas dengan ciri-ciri tersuai (sumber, arahan, dan alat)
- Mencipta aplikasi hos yang berhubung dengan pelayan MCP
- Menguji dan menyahpepijat pelaksanaan MCP

## Menyediakan Persekitaran MCP Anda

Sebelum anda mula bekerja dengan MCP, adalah penting untuk menyediakan persekitaran pembangunan anda dan memahami aliran kerja asas. Bahagian ini akan membimbing anda melalui langkah-langkah persediaan awal untuk memastikan permulaan yang lancar dengan MCP.

### Prasyarat

Sebelum memulakan pembangunan MCP, pastikan anda mempunyai:

- **Persekitaran Pembangunan**: Untuk bahasa pilihan anda (C#, Java, Python, TypeScript, atau Rust)
- **IDE/Editor**: Visual Studio, Visual Studio Code, IntelliJ, Eclipse, PyCharm, atau editor kod moden lain
- **Pengurus Pakej**: NuGet, Maven/Gradle, pip, npm/yarn, atau Cargo
- **Kunci API**: Untuk sebarang perkhidmatan AI yang anda rancang untuk digunakan dalam aplikasi hos anda

## Struktur Pelayan MCP Asas

Pelayan MCP biasanya merangkumi:

- **Konfigurasi Pelayan**: Menyediakan port, pengesahan, dan tetapan lain
- **Sumber**: Data dan konteks yang tersedia untuk LLM
- **Alat**: Fungsi yang boleh dipanggil oleh model
- **Arahan**: Templat untuk menghasilkan atau menyusun teks

Berikut adalah contoh ringkas dalam TypeScript:

```typescript
import { McpServer, ResourceTemplate } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";

// Create an MCP server
const server = new McpServer({
  name: "Demo",
  version: "1.0.0"
});

// Add an addition tool
server.tool("add",
  { a: z.number(), b: z.number() },
  async ({ a, b }) => ({
    content: [{ type: "text", text: String(a + b) }]
  })
);

// Add a dynamic greeting resource
server.resource(
  "file",
  // The 'list' parameter controls how the resource lists available files. Setting it to undefined disables listing for this resource.
  new ResourceTemplate("file://{path}", { list: undefined }),
  async (uri, { path }) => ({
    contents: [{
      uri: uri.href,
      text: `File, ${path}!`
    }]
  })
);

// Add a file resource that reads the file contents
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

// Start receiving messages on stdin and sending messages on stdout
const transport = new StdioServerTransport();
await server.connect(transport);
```

Dalam kod di atas kita:

- Mengimport kelas yang diperlukan dari SDK TypeScript MCP.
- Mencipta dan mengkonfigurasi contoh pelayan MCP baru.
- Mendaftarkan alat tersuai (`calculator`) dengan fungsi pengendali.
- Memulakan pelayan untuk mendengar permintaan MCP yang masuk.

## Ujian dan Penyahpepijatan

Sebelum anda mula menguji pelayan MCP anda, adalah penting untuk memahami alat yang tersedia dan amalan terbaik untuk penyahpepijatan. Ujian yang berkesan memastikan pelayan anda berfungsi seperti yang diharapkan dan membantu anda mengenal pasti serta menyelesaikan masalah dengan cepat. Bahagian berikut menggariskan pendekatan yang disyorkan untuk mengesahkan pelaksanaan MCP anda.

MCP menyediakan alat untuk membantu anda menguji dan menyahpepijat pelayan anda:

- **Alat Inspector**, antara muka grafik ini membolehkan anda berhubung dengan pelayan anda dan menguji alat, arahan, dan sumber anda.
- **curl**, anda juga boleh berhubung dengan pelayan anda menggunakan alat baris perintah seperti curl atau klien lain yang boleh mencipta dan menjalankan arahan HTTP.

### Menggunakan MCP Inspector

[MCP Inspector](https://github.com/modelcontextprotocol/inspector) adalah alat ujian visual yang membantu anda:

1. **Menemui Keupayaan Pelayan**: Mengesan sumber, alat, dan arahan yang tersedia secara automatik
2. **Ujian Pelaksanaan Alat**: Mencuba parameter yang berbeza dan melihat respons secara langsung
3. **Melihat Metadata Pelayan**: Memeriksa maklumat pelayan, skema, dan konfigurasi

```bash
# ex TypeScript, installing and running MCP Inspector
npx @modelcontextprotocol/inspector node build/index.js
```

Apabila anda menjalankan arahan di atas, MCP Inspector akan melancarkan antara muka web tempatan dalam pelayar anda. Anda boleh menjangkakan untuk melihat papan pemuka yang memaparkan pelayan MCP yang didaftarkan, alat, sumber, dan arahan yang tersedia. Antara muka ini membolehkan anda menguji pelaksanaan alat secara interaktif, memeriksa metadata pelayan, dan melihat respons masa nyata, menjadikannya lebih mudah untuk mengesahkan dan menyahpepijat pelaksanaan pelayan MCP anda.

Berikut adalah tangkapan skrin bagaimana ia kelihatan:

![Sambungan pelayan MCP Inspector](../../../../translated_images/connected.73d1e042c24075d386cacdd4ee7cd748c16364c277d814e646ff2f7b5eefde85.ms.png)

## Masalah Persediaan Biasa dan Penyelesaian

| Masalah | Penyelesaian yang Mungkin |
|---------|---------------------------|
| Sambungan ditolak | Periksa sama ada pelayan sedang berjalan dan port adalah betul |
| Kesalahan pelaksanaan alat | Semak pengesahan parameter dan pengendalian kesalahan |
| Kegagalan pengesahan | Sahkan kunci API dan kebenaran |
| Kesalahan pengesahan skema | Pastikan parameter sepadan dengan skema yang ditentukan |
| Pelayan tidak bermula | Periksa konflik port atau kebergantungan yang hilang |
| Kesalahan CORS | Konfigurasi tajuk CORS yang betul untuk permintaan asal silang |
| Masalah pengesahan | Sahkan kesahihan token dan kebenaran |

## Pembangunan Tempatan

Untuk pembangunan dan ujian tempatan, anda boleh menjalankan pelayan MCP secara langsung di mesin anda:

1. **Mulakan proses pelayan**: Jalankan aplikasi pelayan MCP anda
2. **Konfigurasi rangkaian**: Pastikan pelayan boleh diakses pada port yang diharapkan
3. **Sambungkan klien**: Gunakan URL sambungan tempatan seperti `http://localhost:3000`

```bash
# Example: Running a TypeScript MCP server locally
npm run start
# Server running at http://localhost:3000
```

## Membina Pelayan MCP Pertama Anda

Kami telah membincangkan [Konsep Teras](/01-CoreConcepts/README.md) dalam pelajaran sebelumnya, kini tiba masanya untuk menggunakan pengetahuan tersebut.

### Apa yang boleh dilakukan oleh pelayan

Sebelum kita mula menulis kod, mari kita ingatkan diri kita tentang apa yang boleh dilakukan oleh pelayan:

Pelayan MCP boleh, sebagai contoh:

- Mengakses fail dan pangkalan data tempatan
- Berhubung dengan API jauh
- Melakukan pengiraan
- Mengintegrasikan dengan alat dan perkhidmatan lain
- Menyediakan antara muka pengguna untuk interaksi

Bagus, sekarang kita tahu apa yang boleh kita lakukan, mari kita mula menulis kod.

## Latihan: Mencipta Pelayan

Untuk mencipta pelayan, anda perlu mengikuti langkah-langkah ini:

- Pasang SDK MCP.
- Cipta projek dan sediakan struktur projek.
- Tulis kod pelayan.
- Uji pelayan.

### -1- Cipta projek

#### TypeScript

```sh
# Create project directory and initialize npm project
mkdir calculator-server
cd calculator-server
npm init -y
```

#### Python

```sh
# Create project dir
mkdir calculator-server
cd calculator-server
# Open the folder in Visual Studio Code - Skip this if you are using a different IDE
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
# optional remove the unused test
rm -rf src/test/java
```

Tambahkan konfigurasi lengkap berikut ke fail *pom.xml* anda:

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

Sekarang anda telah mencipta projek anda, mari tambahkan kebergantungan seterusnya:

#### TypeScript

```sh
# If not already installed, install TypeScript globally
npm install typescript -g

# Install the MCP SDK and Zod for schema validation
npm install @modelcontextprotocol/sdk zod
npm install -D @types/node typescript
```

#### Python

```sh
# Create a virtual env and install dependencies
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

Buka fail *package.json* dan gantikan kandungan dengan yang berikut untuk memastikan anda boleh membina dan menjalankan pelayan:

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

Cipta fail *tsconfig.json* dengan kandungan berikut:

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

Cipta fail *index.ts* dan tambahkan kod berikut:

```typescript
import { McpServer, ResourceTemplate } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";
 
// Create an MCP server
const server = new McpServer({
  name: "Calculator MCP Server",
  version: "1.0.0"
});
```

Sekarang anda mempunyai pelayan, tetapi ia tidak melakukan banyak perkara, mari kita perbaiki.

#### Python

```python
# server.py
from mcp.server.fastmcp import FastMCP

# Create an MCP server
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

**Komponen pilihan untuk perkhidmatan yang sedia pengeluaran:**

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

        // Getters
        public String getCode() { return code; }
        public String getMessage() { return message; }
    }
}
```

Cipta banner tersuai *src/main/resources/banner.txt*:

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

Tambahkan kod berikut ke bahagian atas fail *src/main.rs*. Ini mengimport pustaka dan modul yang diperlukan untuk pelayan MCP anda.

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

Pelayan kalkulator akan menjadi pelayan mudah yang boleh menambah dua nombor bersama. Mari cipta struktur untuk mewakili permintaan kalkulator.

```rust
#[derive(Debug, serde::Deserialize, schemars::JsonSchema)]
pub struct CalculatorRequest {
    pub a: f64,
    pub b: f64,
}
```

Seterusnya, cipta struktur untuk mewakili pelayan kalkulator. Struktur ini akan memegang router alat, yang digunakan untuk mendaftarkan alat.

```rust
#[derive(Debug, Clone)]
pub struct Calculator {
    tool_router: ToolRouter<Self>,
}
```

Sekarang, kita boleh melaksanakan struktur `Calculator` untuk mencipta contoh baru pelayan dan melaksanakan pengendali pelayan untuk menyediakan maklumat pelayan.

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

Akhirnya, kita perlu melaksanakan fungsi utama untuk memulakan pelayan. Fungsi ini akan mencipta contoh struktur `Calculator` dan menjalankannya melalui input/output standard.

```rust
#[tokio::main]
async fn main() -> Result<(), Box<dyn Error>> {
    let service = Calculator::new().serve(stdio()).await?;
    service.waiting().await?;
    Ok(())
}
```

Pelayan kini disediakan untuk menyediakan maklumat asas tentang dirinya. Seterusnya, kita akan menambah alat untuk melakukan penjumlahan.

### -5- Menambah alat dan sumber

Tambahkan alat dan sumber dengan menambahkan kod berikut:

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
# Add an addition tool
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


# Add a dynamic greeting resource
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}!"
```

Dalam kod di atas kita telah:

- Mendefinisikan alat `add` yang mengambil parameter `a` dan `p`, kedua-duanya integer.
- Mencipta sumber yang dipanggil `greeting` yang mengambil parameter `name`.

#### .NET

Tambahkan ini ke fail Program.cs anda:

```csharp
[McpServerToolType]
public static class CalculatorTool
{
    [McpServerTool, Description("Adds two numbers")]
    public static string Add(int a, int b) => $"Sum {a + b}";
}
```

#### Java

Alat telah dicipta dalam langkah sebelumnya.

#### Rust

Tambahkan alat baru di dalam blok `impl Calculator`:

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

Mari tambahkan kod terakhir yang kita perlukan supaya pelayan dapat dimulakan:

#### TypeScript

```typescript
// Start receiving messages on stdin and sending messages on stdout
const transport = new StdioServerTransport();
await server.connect(transport);
```

Berikut adalah kod penuh:

```typescript
// index.ts
import { McpServer, ResourceTemplate } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";

// Create an MCP server
const server = new McpServer({
  name: "Calculator MCP Server",
  version: "1.0.0"
});

// Add an addition tool
server.tool(
  "add",
  { a: z.number(), b: z.number() },
  async ({ a, b }) => ({
    content: [{ type: "text", text: String(a + b) }]
  })
);

// Add a dynamic greeting resource
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

// Start receiving messages on stdin and sending messages on stdout
const transport = new StdioServerTransport();
server.connect(transport);
```

#### Python

```python
# server.py
from mcp.server.fastmcp import FastMCP

# Create an MCP server
mcp = FastMCP("Demo")


# Add an addition tool
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


# Add a dynamic greeting resource
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}!"

# Main execution block - this is required to run the server
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

> Untuk menggunakan MCP Inspector, gunakan `mcp dev server.py` yang secara automatik melancarkan Inspector dan menyediakan token sesi proksi yang diperlukan. Jika menggunakan `mcp run server.py`, anda perlu melancarkan Inspector secara manual dan mengkonfigurasi sambungan.

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

Inspector adalah alat yang hebat yang boleh memulakan pelayan anda dan membolehkan anda berinteraksi dengannya supaya anda boleh menguji bahawa ia berfungsi. Mari kita mulakan:

> [!NOTE]
> ia mungkin kelihatan berbeza dalam medan "command" kerana ia mengandungi arahan untuk menjalankan pelayan dengan runtime khusus anda/

#### TypeScript

```sh
npx @modelcontextprotocol/inspector node build/index.js
```

atau tambahkan ke *package.json* anda seperti ini: `"inspector": "npx @modelcontextprotocol/inspector node build/index.js"` dan kemudian jalankan `npm run inspector`

Python membungkus alat Node.js yang dipanggil inspector. Adalah mungkin untuk memanggil alat tersebut seperti ini:

```sh
mcp dev server.py
```

Walau bagaimanapun, ia tidak melaksanakan semua kaedah yang tersedia pada alat tersebut jadi anda disarankan untuk menjalankan alat Node.js secara langsung seperti di bawah:

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
Kemudian jalankan inspector:

```cmd
npx @modelcontextprotocol/inspector
```

Dalam antara muka web inspector:

1. Pilih "SSE" sebagai jenis pengangkutan
2. Tetapkan URL kepada: `http://localhost:8080/sse`
3. Klik "Connect"

![Connect](../../../../translated_images/tool.163d33e3ee307e209ef146d8f85060d2f7e83e9f59b3b1699a77204ae0454ad2.ms.png)

**Anda kini telah disambungkan ke pelayan**
**Bahagian ujian pelayan Java kini selesai**

Bahagian seterusnya adalah mengenai berinteraksi dengan pelayan.

Anda sepatutnya melihat antara muka pengguna berikut:

![Connect](../../../../translated_images/connect.141db0b2bd05f096fb1dd91273771fd8b2469d6507656c3b0c9df4b3c5473929.ms.png)

1. Sambungkan ke pelayan dengan memilih butang Connect
   Setelah anda disambungkan ke pelayan, anda sepatutnya melihat perkara berikut:

   ![Connected](../../../../translated_images/connected.73d1e042c24075d386cacdd4ee7cd748c16364c277d814e646ff2f7b5eefde85.ms.png)

1. Pilih "Tools" dan "listTools", anda sepatutnya melihat "Add" muncul, pilih "Add" dan isi nilai parameter.

   Anda sepatutnya melihat respons berikut, iaitu hasil daripada alat "add":

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

## Poin Penting

- Menyediakan persekitaran pembangunan MCP adalah mudah dengan SDK khusus bahasa
- Membina pelayan MCP melibatkan penciptaan dan pendaftaran alat dengan skema yang jelas
- Ujian dan debugging adalah penting untuk implementasi MCP yang boleh dipercayai

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
2. Tentukan parameter input dan nilai pulangan.
3. Jalankan alat inspector untuk memastikan pelayan berfungsi seperti yang diinginkan.
4. Uji implementasi dengan pelbagai input.

## Penyelesaian

[Penyelesaian](./solution/README.md)

## Sumber Tambahan

- [Bina Agen menggunakan Model Context Protocol di Azure](https://learn.microsoft.com/azure/developer/ai/intro-agents-mcp)
- [MCP Jarak Jauh dengan Azure Container Apps (Node.js/TypeScript/JavaScript)](https://learn.microsoft.com/samples/azure-samples/mcp-container-ts/mcp-container-ts/)
- [.NET OpenAI MCP Agent](https://learn.microsoft.com/samples/azure-samples/openai-mcp-agent-dotnet/openai-mcp-agent-dotnet/)

## Apa Seterusnya

Seterusnya: [Memulakan dengan MCP Clients](../02-client/README.md)

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil perhatian bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang berwibawa. Untuk maklumat penting, terjemahan manusia profesional adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.