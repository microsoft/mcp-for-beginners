<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8fdac7600a5f4722643d0f14e15ac259",
  "translation_date": "2025-12-11T08:56:10+00:00",
  "source_file": "03-GettingStarted/01-first-server/README.md",
  "language_code": "et"
}
-->
# MCP-ga alustamine

Tere tulemast oma esimestele sammudele Model Context Protocoli (MCP) kasutamisel! Olenemata sellest, kas oled MCP uus kasutaja või soovid oma teadmisi süvendada, juhendab see juhend sind olulise seadistuse ja arendusprotsessi kaudu. Sa avastad, kuidas MCP võimaldab sujuvat integratsiooni AI mudelite ja rakenduste vahel ning õpid, kuidas kiiresti oma keskkonda valmis seada MCP-põhiste lahenduste ehitamiseks ja testimiseks.

> TLDR; Kui ehitad AI rakendusi, tead, et saad lisada tööriistu ja muid ressursse oma LLM-ile (suur keelemudel), et muuta LLM teadlikumaks. Kuid kui paigutad need tööriistad ja ressursid serverisse, saavad rakendus ja serveri võimekused olla kasutatavad iga kliendi poolt, olenemata sellest, kas kliendil on LLM või mitte.

## Ülevaade

See õppetund annab praktilisi juhiseid MCP keskkondade seadistamiseks ja esimeste MCP rakenduste loomiseks. Sa õpid, kuidas seadistada vajalikke tööriistu ja raamistikke, ehitada põhilisi MCP servereid, luua host-rakendusi ja testida oma rakendusi.

Model Context Protocol (MCP) on avatud protokoll, mis standardiseerib, kuidas rakendused pakuvad konteksti LLM-idele. Mõtle MCP-le nagu USB-C pordile AI rakendustes – see pakub standardiseeritud viisi AI mudelite ühendamiseks erinevate andmeallikate ja tööriistadega.

## Õpieesmärgid

Selle õppetunni lõpuks oskad:

- Seadistada MCP arenduskeskkondi C#, Java, Python, TypeScript ja Rust keeles
- Ehita ja juuruta põhilisi MCP servereid kohandatud funktsioonidega (ressursid, promptid ja tööriistad)
- Loo host-rakendusi, mis ühenduvad MCP serveritega
- Testida ja siluda MCP rakendusi

## MCP keskkonna seadistamine

Enne MCP-ga töötamise alustamist on oluline ette valmistada oma arenduskeskkond ja mõista põhilist töövoogu. See jaotis juhendab sind esialgsete seadistuste sammude kaudu, et tagada sujuv algus MCP-ga.

### Eeltingimused

Enne MCP arendusse sukeldumist veendu, et sul on olemas:

- **Arenduskeskkond**: Sinu valitud keele jaoks (C#, Java, Python, TypeScript või Rust)
- **IDE/Redaktor**: Visual Studio, Visual Studio Code, IntelliJ, Eclipse, PyCharm või mõni kaasaegne koodiredaktor
- **Pakihaldurid**: NuGet, Maven/Gradle, pip, npm/yarn või Cargo
- **API võtmed**: Kõigi AI teenuste jaoks, mida plaanid kasutada oma host-rakendustes

## Põhiline MCP serveri struktuur

MCP server sisaldab tavaliselt:

- **Serveri konfiguratsioon**: Pordi, autentimise ja muude seadete seadistamine
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
  // Parameeter 'list' kontrollib, kuidas ressurss kuvab saadaolevaid faile. Selle väärtuseks undefined seadmine keelab selle ressursi failide kuvamise.
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

// Alusta sõnumite vastuvõtmist stdin-ist ja sõnumite saatmist stdout-i
const transport = new StdioServerTransport();
await server.connect(transport);
```

Eelnevas koodis me:

- Impordime vajalikud klassid MCP TypeScript SDK-st.
- Loome ja konfigureerime uue MCP serveri instantsi.
- Registreerime kohandatud tööriista (`calculator`) koos käsitlejafunktsiooniga.
- Käivitame serveri, et kuulata sissetulevaid MCP päringuid.

## Testimine ja silumine

Enne MCP serveri testimise alustamist on oluline mõista saadaolevaid tööriistu ja parimaid praktikaid silumiseks. Tõhus testimine tagab, et server käitub ootuspäraselt ja aitab kiiresti tuvastada ning lahendada probleeme. Järgmine jaotis kirjeldab soovitatud lähenemisi MCP rakenduse valideerimiseks.

MCP pakub tööriistu, mis aitavad sul oma servereid testida ja siluda:

- **Inspector tööriist**, see graafiline liides võimaldab sul ühendada serveriga ja testida oma tööriistu, promptisid ja ressursse.
- **curl**, saad ka ühendada serveriga käsurea tööriista nagu curl või teiste klientidega, mis suudavad luua ja käivitada HTTP käske.

### MCP Inspectori kasutamine

[MCP Inspector](https://github.com/modelcontextprotocol/inspector) on visuaalne testimisvahend, mis aitab sul:

1. **Avastada serveri võimekusi**: Automaatne saadaolevate ressursside, tööriistade ja promptide tuvastamine
2. **Testida tööriistade täitmist**: Proovi erinevaid parameetreid ja vaata vastuseid reaalajas
3. **Vaadata serveri metaandmeid**: Uuri serveri infot, skeeme ja konfiguratsioone

```bash
# Näide TypeScriptist, MCP Inspector'i installimine ja käivitamine
npx @modelcontextprotocol/inspector node build/index.js
```

Kui käivitad ülaltoodud käsud, avab MCP Inspector sinu brauseris kohaliku veebiliidese. Sa näed armatuurlaua, mis kuvab sinu registreeritud MCP servereid, nende saadaolevaid tööriistu, ressursse ja promptisid. Liides võimaldab interaktiivselt testida tööriistade täitmist, uurida serveri metaandmeid ja vaadata reaalajas vastuseid, muutes MCP serveri rakenduste valideerimise ja silumise lihtsamaks.

Siin on ekraanipilt, kuidas see võib välja näha:

![MCP Inspector serveri ühendus](../../../../translated_images/connected.73d1e042c24075d386cacdd4ee7cd748c16364c277d814e646ff2f7b5eefde85.et.png)

## Levinud seadistusprobleemid ja lahendused

| Probleem | Võimalik lahendus |
|----------|-------------------|
| Ühendus keelatud | Kontrolli, kas server töötab ja port on õige |
| Tööriista täitmise vead | Kontrolli parameetrite valideerimist ja veahaldust |
| Autentimise tõrked | Kontrolli API võtmeid ja õigusi |
| Skeemi valideerimise vead | Veendu, et parameetrid vastavad määratletud skeemile |
| Server ei käivitu | Kontrolli pordikonflikte või puuduvad sõltuvused |
| CORS vead | Sea õiged CORS päised ristallikate päringute jaoks |
| Autentimise probleemid | Kontrolli tokeni kehtivust ja õigusi |

## Kohalik arendus

Kohalikuks arenduseks ja testimiseks saad MCP servereid käivitada otse oma masinas:

1. **Käivita serveri protsess**: Käivita oma MCP serveri rakendus
2. **Seadista võrgustik**: Veendu, et server on ligipääsetav oodatud pordil
3. **Ühenda kliendid**: Kasuta kohalikke ühenduse URL-e nagu `http://localhost:3000`

```bash
# Näide: TypeScript MCP serveri käivitamine lokaalselt
npm run start
# Server töötab aadressil http://localhost:3000
```

## Oma esimese MCP serveri ehitamine

Oleme eelnevas õppetunnis käsitlenud [Põhikontseptsioone](/01-CoreConcepts/README.md), nüüd on aeg neid teadmisi rakendada.

### Mida server suudab teha

Enne koodi kirjutama asumist meenutame, mida server suudab teha:

MCP server võib näiteks:

- Ligipääs kohalikele failidele ja andmebaasidele
- Ühenduda kaug-API-dega
- Teha arvutusi
- Integreeruda teiste tööriistade ja teenustega
- Pakkuda kasutajaliidest suhtlemiseks

Suurepärane, nüüd kui teame, mida saame teha, alustame kodeerimist.

## Harjutus: serveri loomine

Serveri loomiseks pead järgima järgmisi samme:

- Paigalda MCP SDK.
- Loo projekt ja seadista projekti struktuur.
- Kirjuta serveri kood.
- Testi serverit.

### -1- Projekti loomine

#### TypeScript

```sh
# Loo projekti kataloog ja algata npm projekt
mkdir calculator-server
cd calculator-server
npm init -y
```

#### Python

```sh
# Loo projekti kaust
mkdir calculator-server
cd calculator-server
# Ava kaust Visual Studio Code'is - Jäta see vahele, kui kasutad teist IDE-d
code .
```

#### .NET

```sh
dotnet new console -n McpCalculatorServer
cd McpCalculatorServer
```

#### Java

Java jaoks loo Spring Boot projekt:

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
# valikuline eemaldada kasutamata test
rm -rf src/test/java
```

Lisa oma *pom.xml* faili järgmine täielik konfiguratsioon:

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

### -2- Sõltuvuste lisamine

Nüüd, kui projekt on loodud, lisame järgmised sõltuvused:

#### TypeScript

```sh
# Kui pole veel installitud, paigalda TypeScript globaalselt
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

### -3- Projekti failide loomine

#### TypeScript

Ava *package.json* fail ja asenda selle sisu järgmisega, et tagada serveri ehitamine ja käivitamine:

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

Loo kataloog oma lähtekoodi jaoks:

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

Java Spring Boot projektide puhul luuakse projekti struktuur automaatselt.

#### Rust

Rustis luuakse *src/main.rs* fail vaikimisi, kui käivitad `cargo init`. Ava fail ja kustuta vaikimisi kood.

### -4- Serveri koodi loomine

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

Nüüd on sul server olemas, kuid see ei tee veel palju, parandame selle.

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

Java jaoks loo põhiserveri komponendid. Muuda esmalt peamist rakenduse klassi:

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

**Valikulised komponendid tootmisvalmis teenuse jaoks:**

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

Loo erandite käsitleja *src/main/java/com/microsoft/mcp/sample/server/exception/GlobalExceptionHandler.java*:

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

        // Getrid
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

Lisa järgmine kood *src/main.rs* faili algusesse. See impordib vajalikud teegid ja moodulid sinu MCP serveri jaoks.

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

Kalkulaatori server on lihtne, mis suudab liita kaks arvu. Loo struktuur kalkulaatori päringu esindamiseks.

```rust
#[derive(Debug, serde::Deserialize, schemars::JsonSchema)]
pub struct CalculatorRequest {
    pub a: f64,
    pub b: f64,
}
```

Seejärel loo struktuur kalkulaatori serveri esindamiseks. See struktuur hoiab tööriistade marsruuterit, mida kasutatakse tööriistade registreerimiseks.

```rust
#[derive(Debug, Clone)]
pub struct Calculator {
    tool_router: ToolRouter<Self>,
}
```

Nüüd saame rakendada `Calculator` struktuuri, et luua uus serveri instants ja rakendada serveri käsitlejat serveri info pakkumiseks.

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

Lõpuks peame rakendama põhifunktsiooni serveri käivitamiseks. See funktsioon loob `Calculator` struktuuri instantsi ja teenindab seda standardse sisendi/väljundi kaudu.

```rust
#[tokio::main]
async fn main() -> Result<(), Box<dyn Error>> {
    let service = Calculator::new().serve(stdio()).await?;
    service.waiting().await?;
    Ok(())
}
```

Server on nüüd seadistatud, et pakkuda enda kohta põhiinfot. Järgmisena lisame tööriista liitmiseks.

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

Sinu ressurssile pääseb ligi stringi "greeting" kaudu, see võtab parameetri `name` ja toodab sarnase vastuse nagu tööriist:

```typescript
{
  uri: "<href>",
  text: "a text"
}
```

#### Python

```python
# Lisa liitmistööriist
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

Eelnevas koodis me:

- Määratlesime tööriista `add`, mis võtab parameetrid `a` ja `b`, mõlemad täisarvud.
- Lõime ressursi nimega `greeting`, mis võtab parameetri `name`.

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

Tööriistad on juba eelnevas sammus loodud.

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

Lisame viimase koodi, mida serveri käivitamiseks vaja:

#### TypeScript

```typescript
// Alusta sõnumite vastuvõtmist stdin-ist ja sõnumite saatmist stdout-i
const transport = new StdioServerTransport();
await server.connect(transport);
```

Siin on kogu kood:

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

// Lisa liitmisvahend
server.tool(
  "add",
  { a: z.number(), b: z.number() },
  async ({ a, b }) => ({
    content: [{ type: "text", text: String(a + b) }]
  })
);

// Lisa dünaamiline tervituse ressurss
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

// Alusta sõnumite vastuvõtmist stdin-ist ja sõnumite saatmist stdout-i
const transport = new StdioServerTransport();
server.connect(transport);
```

#### Python

```python
# server.py
from mcp.server.fastmcp import FastMCP

# Loo MCP server
mcp = FastMCP("Demo")


# Lisa liitmistööriist
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


# Lisa dünaamiline tervituse ressurss
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}!"

# Peamine täitmisplokk - serveri käivitamiseks vajalik
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

Sinu täielik peamine rakenduse klass peaks välja nägema selline:

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

Rust serveri lõplik kood peaks välja nägema selline:

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

### -7- Serveri testimine

Käivita server järgmise käsuga:

#### TypeScript

```sh
npm run build
```

#### Python

```sh
mcp run server.py
```

> MCP Inspectori kasutamiseks kasuta `mcp dev server.py`, mis automaatselt käivitab Inspectori ja annab vajaliku proxy sessioonitokeni. Kui kasutad `mcp run server.py`, pead Inspectori käsitsi käivitama ja ühenduse seadistama.

#### .NET

Veendu, et oled oma projekti kataloogis:

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

### -8- Käivita Inspectoriga

Inspector on suurepärane tööriist, mis suudab sinu serveri käivitada ja võimaldab sul sellega suhelda, et testida selle toimimist. Alustame:

> [!NOTE]
> käsk võib "command" väljal välja näha erinev, kuna see sisaldab käsku serveri käivitamiseks sinu konkreetse runtime'iga.

#### TypeScript

```sh
npx @modelcontextprotocol/inspector node build/index.js
```

või lisa see oma *package.json* faili nii: `"inspector": "npx @modelcontextprotocol/inspector node build/index.js"` ja seejärel käivita `npm run inspector`

#### Python

Python kasutab Node.js tööriista nimega inspector. Seda tööriista saab kutsuda nii:

```sh
mcp dev server.py
```

Kuid see ei implementeeri kõiki tööriista meetodeid, seega soovitatakse Node.js tööriista käivitada otse nii:

```sh
npx @modelcontextprotocol/inspector mcp run server.py
```

Kui kasutad tööriista või IDE-d, mis võimaldab konfigureerida käske ja argumente skriptide käivitamiseks,
veenduge, et `Command` väljale oleks seatud `python` ja `Arguments` väljale `server.py`. See tagab skripti õige käivitamise.

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

1. Valige transporditüübiks "SSE"
2. Määrake URL-iks: `http://localhost:8080/sse`
3. Klõpsake "Connect"

![Connect](../../../../translated_images/tool.163d33e3ee307e209ef146d8f85060d2f7e83e9f59b3b1699a77204ae0454ad2.et.png)

**Olete nüüd serveriga ühendatud**
**Java serveri testimise osa on nüüd lõpetatud**

Järgmine osa käsitleb suhtlust serveriga.

Te peaksite nägema järgmist kasutajaliidest:

![Connect](../../../../translated_images/connect.141db0b2bd05f096fb1dd91273771fd8b2469d6507656c3b0c9df4b3c5473929.et.png)

1. Ühenduge serveriga, valides nupu Connect
  Kui olete serveriga ühendatud, peaksite nüüd nägema järgmist:

  ![Connected](../../../../translated_images/connected.73d1e042c24075d386cacdd4ee7cd748c16364c277d814e646ff2f7b5eefde85.et.png)

1. Valige "Tools" ja "listTools", peaksite nägema "Add" valikut, valige "Add" ja täitke parameetrite väärtused.

  Peaksite nägema järgmist vastust, st "add" tööriista tulemust:

  ![Result of running add](../../../../translated_images/ran-tool.a5a6ee878c1369ec1e379b81053395252a441799dbf23416c36ddf288faf8249.et.png)

Palju õnne, olete loonud ja käivitanud oma esimese serveri!

#### Rust

Rust serveri käivitamiseks MCP Inspector CLI abil kasutage järgmist käsku:

```sh
npx @modelcontextprotocol/inspector cargo run --cli --method tools/call --tool-name add --tool-arg a=1 b=2
```

### Ametlikud SDK-d

MCP pakub ametlikke SDK-sid mitmele keelele:

- [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk) - Hooldatud koostöös Microsoftiga
- [Java SDK](https://github.com/modelcontextprotocol/java-sdk) - Hooldatud koostöös Spring AI-ga
- [TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk) - Ametlik TypeScripti teostus
- [Python SDK](https://github.com/modelcontextprotocol/python-sdk) - Ametlik Pythoni teostus
- [Kotlin SDK](https://github.com/modelcontextprotocol/kotlin-sdk) - Ametlik Kotlini teostus
- [Swift SDK](https://github.com/modelcontextprotocol/swift-sdk) - Hooldatud koostöös Loopwork AI-ga
- [Rust SDK](https://github.com/modelcontextprotocol/rust-sdk) - Ametlik Rusti teostus

## Peamised järeldused

- MCP arenduskeskkonna seadistamine on lihtne keelepõhiste SDK-dega
- MCP serverite loomine hõlmab tööriistade loomist ja registreerimist selgete skeemidega
- Testimine ja silumine on usaldusväärsete MCP teostuste jaoks hädavajalikud

## Näited

- [Java kalkulaator](../samples/java/calculator/README.md)
- [.Net kalkulaator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript kalkulaator](../samples/javascript/README.md)
- [TypeScript kalkulaator](../samples/typescript/README.md)
- [Python kalkulaator](../../../../03-GettingStarted/samples/python)
- [Rust kalkulaator](../../../../03-GettingStarted/samples/rust)

## Ülesanne

Loo lihtne MCP server oma valitud tööriistaga:

1. Rakenda tööriist oma eelistatud keeles (.NET, Java, Python, TypeScript või Rust).
2. Määra sisendparameetrid ja tagastatavad väärtused.
3. Käivita inspektori tööriist, et veenduda serveri õiges töös.
4. Testi teostust erinevate sisenditega.

## Lahendus

[Lahendus](./solution/README.md)

## Täiendavad ressursid

- [Agentide loomine Model Context Protocol abil Azure'is](https://learn.microsoft.com/azure/developer/ai/intro-agents-mcp)
- [Kaug-MCP Azure Container Appsiga (Node.js/TypeScript/JavaScript)](https://learn.microsoft.com/samples/azure-samples/mcp-container-ts/mcp-container-ts/)
- [.NET OpenAI MCP agent](https://learn.microsoft.com/samples/azure-samples/openai-mcp-agent-dotnet/openai-mcp-agent-dotnet/)

## Mis järgmiseks

Järgmine: [MCP klientidega alustamine](../02-client/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastutusest loobumine**:
See dokument on tõlgitud kasutades tehisintellekti tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi püüame täpsust, palun arvestage, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Originaaldokument selle emakeeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valesti mõistmiste eest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->