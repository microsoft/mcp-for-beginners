# Alustamine MCP-ga

Tere tulemast esimestesse sammudesse Model Context Protocoli (MCP) kasutamisel! Olenemata sellest, kas oled MCP-ga uus või soovid oma teadmisi süvendada, juhendab see juhend sind olulise seadistuse ja arenduse protsessi läbi. Saad teada, kuidas MCP võimaldab sujuvat integreerimist AI mudelite ja rakenduste vahel ning kuidas kiiresti valmis seada oma keskkond MCP-põhiste lahenduste loomiseks ja testimiseks.

> TLDR; Kui ehitad AI-rakendusi, tead, et saad lisada oma suurele keelemudelile (LLM) tööriistu ja muid ressursse, et muuta mudel teadlikumaks. Kuid kui paigutad need tööriistad ja ressursid serverisse, saavad rakendus ja serveri võimed olla kasutatavad iga kliendi poolt, olgu tal LLM või mitte.

## Ülevaade

See õppetund annab praktilisi juhiseid MCP keskkondade seadistamiseks ja esimeste MCP rakenduste loomiseks. Õpid, kuidas seadistada vajalikud tööriistad ja raamistikud, ehitada lihtsaid MCP servereid, luua hostrakendusi ja testida oma lahendusi.

Model Context Protocol (MCP) on avatud protokoll, mis standardiseerib, kuidas rakendused pakuvad konteksti LLM-idele. Mõtle MCP-st nagu USB-C pesast AI rakendustele – see annab standardse võimaluse ühendada AI mudelid erinevate andmeallikate ja tööriistadega.

## Õpieesmärgid

Selle õppetunni lõpuks suudad:

- Seadistada MCP arenduskeskkonnad C#, Java, Python, TypeScripti ja Rusti jaoks
- Ehitatud ja juurutatud lihtsad MCP serverid kohandatud funktsioonidega (ressursid, promptid ja tööriistad)
- Luua hostrakendused, mis ühenduvad MCP serveritega
- Testida ja siluda MCP lahendusi

## MCP keskkonna seadistamine

Enne MCP-ga töötama hakkamist on oluline ette valmistada oma arenduskeskkond ja mõista põhitähtaegu. See jaotis juhendab sind algsete seadistuste tegemisel, et MCP-ga sujuvalt alustada.

### Nõuded

Enne kui süüvida MCP arendusse, veendu, et sul on olemas:

- **Arenduskeskkond**: Valitud programmeerimiskeele jaoks (C#, Java, Python, TypeScript või Rust)
- **IDE/Tekstiredaktor**: Visual Studio, Visual Studio Code, IntelliJ, Eclipse, PyCharm või mõni kaasaegne koodiredaktor
- **Paketihaldurid**: NuGet, Maven/Gradle, pip, npm/yarn või Cargo
- **API võtmed**: Iga AI teenuse jaoks, mida plaanid oma hostrakendustes kasutada

## Põhiline MCP serveri struktuur

MCP server sisaldab tavaliselt:

- **Serveri konfiguratsioon**: Pordi, autentimise ja teiste sätete seadistamine
- **Ressursid**: Andmed ja kontekst, mis on LLM-idele kättesaadavad
- **Tööriistad**: Funktsionaalsus, mida mudelid saavad kutsuda
- **Promptid**: Mallid teksti genereerimiseks või struktureerimiseks

Siin on lihtsustatud näide TypeScriptis:

```typescript
import { McpServer, ResourceTemplate } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";

// Loo MCP server
const server = new McpServer({
  name: "Demo",
  version: "1.0.0"
});

// Lisa liitmistööriist
server.tool("add",
  { a: z.number(), b: z.number() },
  async ({ a, b }) => ({
    content: [{ type: "text", text: String(a + b) }]
  })
);

// Lisa dünaamiline tervituse ressurss
server.resource(
  "file",
  // Parameeter 'list' kontrollib, kuidas ressursil olevad failid kuvatakse. Selle väärtuseks undefined seadmine keelab selle ressursi failinimekirja kuvamise.
  new ResourceTemplate("file://{path}", { list: undefined }),
  async (uri, { path }) => ({
    contents: [{
      uri: uri.href,
      text: `File, ${path}!`
    }]
  })
);

// Lisa failiresurss, mis loeb faili sisu
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

// Alusta sõnumite vastuvõtmist stdin-lt ja sõnumite saatmist stdout-ile
const transport = new StdioServerTransport();
await server.connect(transport);
```

Eelnevas koodis me:

- Importisime vajalikud klassid MCP TypeScript SDK-st.
- Lõime ja konfigureerisime uue MCP serveri näite.
- Registreerisime kohandatud tööriista (`calculator`) käsitlejafunktsiooniga.
- Käivitasime serveri, et kuulata sissetulevaid MCP päringuid.

## Testimine ja silumine

Enne kui hakkad oma MCP serverit testima, on oluline mõista saadaval olevaid tööriistu ja parimaid tavasid silumiseks. Tõhus testimine tagab, et server käitub ootuspäraselt ja aitab kiiresti üles leida ning lahendada probleemid. Järgmises jaotises on kirjeldatud soovitatud lähenemisi MCP implementatsiooni valideerimiseks.

MCP pakub tööriistu, mis aitavad sul servereid testida ja siluda:

- **Inspector tööriist**, see graafiline liides võimaldab sul serveriga ühendada ja testida tööriistu, promptisid ja ressursse.
- **curl**, samuti saad serveriga ühendada käsureatööriistadega nagu curl või muud kliendid, kes suudavad luua ja käivitada HTTP käske.

### MCP Inspectori kasutamine

[MCP Inspector](https://github.com/modelcontextprotocol/inspector) on visuaalne testimise tööriist, mis toetab sind selleks:

1. **Serveri võimekuse avastamine**: Automaatne olemasolevate ressursside, tööriistade ja promptide tuvastamine
2. **Tööriistade täitmise testimine**: Katseta erinevaid parameetreid ja vaata reaalajas vastuseid
3. **Serveri metaandmete vaatamine**: Uuri serveri infot, skeeme ja konfiguratsioone

```bash
# Näide TypeScriptist, MCP Inspector'i installimine ja käivitamine
npx @modelcontextprotocol/inspector node build/index.js
```

Kui käivitad ülaltoodud käsud, avab MCP Inspector veebipõhise liidese sinu brauseris. Näed juhtpaneeli, mis kuvab registreeritud MCP servereid, nende saadaolevaid tööriistu, ressursse ja promptisid. Liides võimaldab sul interaktiivselt testida tööriistade täitmist, uurida serveri metaandmeid ja jälgida reaalajas vastuseid, mis muudab MCP serveri implementatsioonide valideerimise ja silumise lihtsamaks.

Siin on kuvatõmmis sellest, kuidas see võib välja näha:

![MCP Inspector server connection](../../../../translated_images/et/connected.73d1e042c24075d3.webp)

## Levinumad seadistamise probleemid ja lahendused

| Probleem | Võimalik lahendus |
|-------|-------------------|
| Ühendus keelatud | Kontrolli, kas server jookseb ja port on õige |
| Tööriista täitmiste vead | Kontrolli parameetrite valideerimist ja veahaldust |
| Autentimise ebaõnnestumine | Kontrolli API võtmeid ja õigusi |
| Skeemi valideerimise vead | Veendu, et parameetrid vastaksid määratletud skeemile |
| Server ei käivitu | Kontrolli portide konflikte või puuduvaid sõltuvusi |
| CORS vead | Seadista õiged CORS päised ristallikapäringuteks |
| Autentimise probleemid | Kontrolli tokeni kehtivust ja õigusi |

## Kohalik arendus

Kohalikuks arenduseks ja testimiseks võid käivitada MCP servereid otse oma masinas:

1. **Käivita serveriprotsess**: Käivita oma MCP serverirakendus
2. **Võrgu konfiguratsioon**: Veendu, et server on ootuspärasel pordil ligipääsetav
3. **Ühenda kliendid**: Kasuta kohalikke ühenduse URL-e nagu `http://localhost:3000`

```bash
# Näide: TypeScript MCP serveri kohalik käivitamine
npm run start
# Server töötab aadressil http://localhost:3000
```

## Esimese MCP serveri ehitamine

Oleme varasemates õppetundides käsitlenud [Põhimõisteid](../../01-CoreConcepts/README.md), nüüd on aeg neid teadmisi rakendada.

### Mida server suudab teha

Enne koodi kirjutama hakkamist meenutame, mida server suudab teha:

MCP server võib näiteks:

- Juurdepääs kohalikule failisüsteemile ja andmebaasidele
- Ühenduda kaug-API-dega
- Teha arvutusi
- Integreeruda teiste tööriistade ja teenustega
- Pakkuda kasutajaliidest suhtlemiseks

Suurepärane, nüüd kui teame, mida saame teha, alustame kodeerimist.

## Harjutus: serveri loomine

Serveri loomiseks tuleb järgida neid samme:

- Paigalda MCP SDK.
- Loo projekt ja sea üles projektistruktuur.
- Kirjuta serveri kood.
- Testi serverit.

### -1- Projekti loomine

#### TypeScript

```sh
# Loo projekti kaust ja inicialiseeri npm projekt
mkdir calculator-server
cd calculator-server
npm init -y
```

#### Python

```sh
# Loo projekti kaust
mkdir calculator-server
cd calculator-server
# Ava kaust Visual Studio Code'is - Jäta see vahele, kui kasutad mõnda teist IDE-d
code .
```

#### .NET

```sh
dotnet new console -n McpCalculatorServer
cd McpCalculatorServer
```

#### Java

Java puhul loo Spring Boot projekt:

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

Paki zip-fail lahti:

```bash
unzip calculator-server.zip -d calculator-server
cd calculator-server
# valikuliselt eemalda kasutamata test
rm -rf src/test/java
```

Lisa järgmine täielik konfiguratsioon oma *pom.xml* faili:

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

### -2- Lisada sõltuvused

Nüüd, kui projekt on loodud, lisame järgmised sõltuvused:

#### TypeScript

```sh
# Kui pole veel installitud, installi TypeScript globaalselt
npm install typescript -g

# Paigalda MCP SDK ja Zod skeemi valideerimiseks
npm install @modelcontextprotocol/sdk zod
npm install -D @types/node typescript
```

#### Python

```sh
# Loo virtuaalne keskkond ja paigalda sõltuvused
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

### -3- Loo projekti failid

#### TypeScript

Ava *package.json* fail ja asenda sisu järgmisega, et tagada serveri ehitus ja käivitamine:

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

Loo *tsconfig.json* järgmise sisuga:

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

Loo kaust lähtekoodile:

```sh
mkdir src
touch src/index.ts
```

#### Python

Loo fail *server.py*

```sh
touch server.py
```

#### .NET

Paigalda vajalikud NuGet paketid:

```sh
dotnet add package ModelContextProtocol --prerelease
dotnet add package Microsoft.Extensions.Hosting
```

#### Java

Java Spring Boot projektides luuakse projektistruktuur automaatselt.

#### Rust

Rustis luuakse vaikimisi fail *src/main.rs* kui käivitad `cargo init`. Ava fail ja kustuta vaikimisi kood.

### -4- Kirjuta serveri kood

#### TypeScript

Loo fail *index.ts* ja lisa järgmine kood:

```typescript
import { McpServer, ResourceTemplate } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";
 
// Loo MCP server
const server = new McpServer({
  name: "Calculator MCP Server",
  version: "1.0.0"
});
```

Nüüd on sul server olemas, kuid see ei tee eriti palju, parandame selle.

#### Python

```python
# server.py
from mcp.server.fastmcp import FastMCP

# Loo MCP server
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

Java puhul loo tuumikkomponendid. Muuda esmalt põhiklassi:

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

Loo kalkulaatori teenus *src/main/java/com/microsoft/mcp/sample/server/service/CalculatorService.java*:

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

**Valikulised komponendid tootmiskõlblikuks teenuseks:**

Loo käivituse konfiguratsioon *src/main/java/com/microsoft/mcp/sample/server/config/StartupConfig.java*:

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

Loo tervisekontroller *src/main/java/com/microsoft/mcp/sample/server/controller/HealthController.java*:

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

Loo vea käitleja *src/main/java/com/microsoft/mcp/sample/server/exception/GlobalExceptionHandler.java*:

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

        // Getid
        public String getCode() { return code; }
        public String getMessage() { return message; }
    }
}
```

Loo kohandatud banner *src/main/resources/banner.txt*:

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

Lisa järgnev kood *src/main.rs* faili algusesse. See impordib vajalikud teegid ja moodulid sinu MCP serveri jaoks.

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

Kalkulaatori server saab olema lihtne, mis liidab kaks arvu kokku. Loome struktuuri, mis esindab kalkulaatori päringut.

```rust
#[derive(Debug, serde::Deserialize, schemars::JsonSchema)]
pub struct CalculatorRequest {
    pub a: f64,
    pub b: f64,
}
```

Seejärel loo struktuur, mis esindab kalkulaatori serverit. See hõlmab tööriistade marsruutijat, mida kasutatakse tööriistade registreerimiseks.

```rust
#[derive(Debug, Clone)]
pub struct Calculator {
    tool_router: ToolRouter<Self>,
}
```

Nüüd rakendame `Calculator` struktuuri, et luua serveri uus instants ja implementeerida serveri käitleja, mis annab serveri info.

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

Lõpuks implementeerime põhifunktsiooni serveri käivitamiseks. See funktsioon loob `Calculator` instantsi ja teenindab seda standardse sisendi/väljundi kaudu.

```rust
#[tokio::main]
async fn main() -> Result<(), Box<dyn Error>> {
    let service = Calculator::new().serve(stdio()).await?;
    service.waiting().await?;
    Ok(())
}
```

Server on nüüd seadistatud, et pakkuda enda kohta põhiinfot. Järgmine samm on lisada tööriist arvutuste tegemiseks.

### -5- Tööriista ja ressursi lisamine

Lisa tööriist ja ressurss, lisades järgmise koodi:

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

Sinu tööriist võtab parameetrid `a` ja `b` ning käivitab funktsiooni, mis toodab vastuse kujul:

```typescript
{
  contents: [{
    type: "text", content: "some content"
  }]
}
```

Sinu ressursile pääseb ligi stringiga "greeting", mis võtab parameetrina `name` ja loob sarnase vastuse:

```typescript
{
  uri: "<href>",
  text: "a text"
}
```

#### Python

```python
# Lisa liitmiste tööriist
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


# Lisa dünaamiline tervituse ressurss
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}!"
```

Eelnevas koodis oleme:

- Määratlenud tööriista `add`, mis võtab parameetritena täisarvud `a` ja `b`.
- Loonud ressursi nimega `greeting`, mis võtab parameetrina `name`.

#### .NET

Lisa see oma Program.cs faili:

```csharp
[McpServerToolType]
public static class CalculatorTool
{
    [McpServerTool, Description("Adds two numbers")]
    public static string Add(int a, int b) => $"Sum {a + b}";
}
```

#### Java

Tööriistad on eelnevas etapis juba loodud.

#### Rust

Lisa uus tööriist `impl Calculator` plokki:

```rust
#[tool(description = "Adds a and b")]
async fn add(
    &self,
    Parameters(CalculatorRequest { a, b }): Parameters<CalculatorRequest>,
) -> String {
    (a + b).to_string()
}
```

### -6- Lõplik kood

Lisame viimased koodiridad, et server saaks käivituda:

#### TypeScript

```typescript
// Alusta sõnumite vastuvõtmist stdin-ist ja sõnumite saatmist stdout-i
const transport = new StdioServerTransport();
await server.connect(transport);
```

Siin on täielik kood:

```typescript
// index.ts
import { McpServer, ResourceTemplate } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";

// Loo MCP server
const server = new McpServer({
  name: "Calculator MCP Server",
  version: "1.0.0"
});

// Lisa lisa tööriist
server.tool(
  "add",
  { a: z.number(), b: z.number() },
  async ({ a, b }) => ({
    content: [{ type: "text", text: String(a + b) }]
  })
);

// Lisa dünaamiline tervitusressurss
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

// Alusta sõnumite vastuvõtmist stdin kaudu ja sõnumite saatmist stdout kaudu
const transport = new StdioServerTransport();
server.connect(transport);
```

#### Python

```python
# server.py
from mcp.server.fastmcp import FastMCP

# Loo MCP-server
mcp = FastMCP("Demo")


# Lisa liitmismeede
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


# Lisa dünaamiline tervituse ressurss
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}!"

# Peamine täitmisplokk - serveri käivitamiseks on see vajalik
if __name__ == "__main__":
    mcp.run()
```

#### .NET

Loo Program.cs fail järgmise sisuga:

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

Sinu põhiklass peaks nüüd välja nägema selline:

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

Rust serveri lõplik kood peaks välja nägema nii:

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

### -7- Testi serverit

Käivita server järgmise käsuga:

#### TypeScript

```sh
npm run build
```

#### Python

```sh
mcp run server.py
```

> MCP Inspectori kasutamiseks kasuta käsku `mcp dev server.py`, mis käivitab automaatselt Inspectori ning annab vajaliku proksiseansi tokeni. Kui kasutad `mcp run server.py`, pead Inspectori käsitsi käivitama ja ühenduse konfigureerima.

#### .NET

Veendu, et oled oma projekti kaustas:

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

Käivita järgmised käsud, et vormindada ja käivitada server:

```sh
cargo fmt
cargo run
```

### -8- Käivita Inspectori abil

Inspector on suurepärane tööriist, mis suudab su serveri käivitada ja võimaldab sul selle peal suhelda, et testida, kas kõik töötab. Käivitame selle:

> [!NOTE]
> käsk võib välja näha erinev "command" väljale ilmuv käsk, kuna seal sisaldub käsk serveri jooksutamiseks sinu konkreetse runtime'iga.

#### TypeScript

```sh
npx @modelcontextprotocol/inspector node build/index.js
```

või lisa see oma *package.json* faili nii: `"inspector": "npx @modelcontextprotocol/inspector node build/index.js"` ja seejärel käivita `npm run inspector`

#### Python

Python kasutab Node.js tööriista nimega inspector. On võimalik käivitada seda tööriista nii:

```sh
mcp dev server.py
```

Siiski ei implementeeri see kõikidest saadaolevatest meetoditest kõiki, seega soovitatakse Node.js tööriista käivitada otse nii:

```sh
npx @modelcontextprotocol/inspector mcp run server.py
```

Kui kasutad tööriista või IDE-t, mis võimaldab konfigureerida käske ja argumente skriptide jooksutamiseks,
veenduge, et väljal `Command` oleks seatud `python` ja `Arguments` oleks `server.py`. See tagab, et skript töötab õigesti.

#### .NET

Veenduge, et olete oma projekti kataloogis:

```sh
cd McpCalculatorServer
npx @modelcontextprotocol/inspector dotnet run
```

#### Java

Veenduge, et teie kalkulaatori server töötab
Seejärel käivitage inspektor:

```cmd
npx @modelcontextprotocol/inspector
```

Inspektori veebiliideses:

1. Valige transpordi tüübiks "SSE"
2. Määrake URL-iks: `http://localhost:8080/sse`
3. Klõpsake "Connect"

![Connect](../../../../translated_images/et/tool.163d33e3ee307e20.webp)

**Olete nüüd serveriga ühendatud**
**Java serveri testimise osa on nüüd lõpetatud**

Järgmine osa käsitleb suhtlust serveriga.

Te peaksite nägema järgmist kasutajaliidest:

![Connect](../../../../translated_images/et/connect.141db0b2bd05f096.webp)

1. Ühendage serveriga, valides nupu Connect
  Kui olete serveriga ühendatud, peaksite nüüd nägema järgmist:

  ![Connected](../../../../translated_images/et/connected.73d1e042c24075d3.webp)

1. Valige "Tools" ja "listTools", peaksite nägema "Add" ilmumist, valige "Add" ja täitke parameetri väärtused.

  Peaksite nägema järgmist vastust, see tähendab "add"-tööriista tulemust:

  ![Result of running add](../../../../translated_images/et/ran-tool.a5a6ee878c1369ec.webp)

Palju õnne, olete loonud ja käivitanud oma esimese serveri!

#### Rust

Rust-serveri käivitamiseks koos MCP Inspector CLI-ga kasutage järgmist käsku:

```sh
npx @modelcontextprotocol/inspector cargo run --cli --method tools/call --tool-name add --tool-arg a=1 b=2
```

### Ametlikud SDK-d

MCP pakub ametlikke SDK-sid mitmele keelele:

- [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk) - Hooldatud koostöös Microsoftiga
- [Java SDK](https://github.com/modelcontextprotocol/java-sdk) - Hooldatud koostöös Spring AI-ga
- [TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk) - Ametlik TypeScripti implementatsioon
- [Python SDK](https://github.com/modelcontextprotocol/python-sdk) - Ametlik Python implementatsioon
- [Kotlin SDK](https://github.com/modelcontextprotocol/kotlin-sdk) - Ametlik Kotlin implementatsioon
- [Swift SDK](https://github.com/modelcontextprotocol/swift-sdk) - Hooldatud koostöös Loopwork AI-ga
- [Rust SDK](https://github.com/modelcontextprotocol/rust-sdk) - Ametlik Rust implementatsioon

## Põhipunktid

- MCP arenduskeskkonna seadistamine on keeltespetsiifiliste SDK-dega lihtne
- MCP serverite ehitamine hõlmab tööriistade loomist ja registreerimist selgete skeemidega
- Testimine ja silumine on usaldusväärsete MCP implementatsioonide jaoks hädavajalikud

## Näited

- [Java kalkulaator](../samples/java/calculator/README.md)
- [.Net kalkulaator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript kalkulaator](../samples/javascript/README.md)
- [TypeScript kalkulaator](../samples/typescript/README.md)
- [Python kalkulaator](../../../../03-GettingStarted/samples/python)
- [Rust kalkulaator](../../../../03-GettingStarted/samples/rust)

## Ülesanne

Loo lihtne MCP server valitud tööriistaga:

1. Rakenda tööriist eelistatud keeles (.NET, Java, Python, TypeScript või Rust).
2. Määra sisendi parameetrid ja tagastatavad väärtused.
3. Käivita inspektor tööriist, et veenduda serveri õigesti töötamises.
4. Testi implementatsiooni erinevate sisenditega.

## Lahendus

[Lahendus](./solution/README.md)

## Täiendavad ressursid

- [Agentide loomine Model Context Protocol abil Azure’is](https://learn.microsoft.com/azure/developer/ai/intro-agents-mcp)
- [Kaug-MCP Azure Container Apps’iga (Node.js/TypeScript/JavaScript)](https://learn.microsoft.com/samples/azure-samples/mcp-container-ts/mcp-container-ts/)
- [.NET OpenAI MCP Agent](https://learn.microsoft.com/samples/azure-samples/openai-mcp-agent-dotnet/openai-mcp-agent-dotnet/)

## Mis järgmiseks

Järgmine: [MCP klientide kasutuselevõtt](../02-client/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastutusest loobumine**:  
See dokument on tõlgitud kasutades AI tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi püüame täpsust, palun arvestage, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Originaaldokument selle algkeeles tuleks pidada autoriteetseks allikaks. Kriitilise teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valesti mõistmiste eest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->