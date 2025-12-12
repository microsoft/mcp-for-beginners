<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8fdac7600a5f4722643d0f14e15ac259",
  "translation_date": "2025-12-11T06:52:29+00:00",
  "source_file": "03-GettingStarted/01-first-server/README.md",
  "language_code": "no"
}
-->
# Komme i gang med MCP

Velkommen til dine første steg med Model Context Protocol (MCP)! Enten du er ny til MCP eller ønsker å utdype din forståelse, vil denne guiden lede deg gjennom den essensielle oppsett- og utviklingsprosessen. Du vil oppdage hvordan MCP muliggjør sømløs integrasjon mellom AI-modeller og applikasjoner, og lære hvordan du raskt får miljøet ditt klart for å bygge og teste MCP-drevne løsninger.

> TLDR; Hvis du bygger AI-apper, vet du at du kan legge til verktøy og andre ressurser til din LLM (stor språkmodell), for å gjøre LLM mer kunnskapsrik. Men hvis du plasserer disse verktøyene og ressursene på en server, kan appen og serverens kapasiteter brukes av enhver klient med/uten en LLM.

## Oversikt

Denne leksjonen gir praktisk veiledning om hvordan du setter opp MCP-miljøer og bygger dine første MCP-applikasjoner. Du vil lære hvordan du setter opp nødvendige verktøy og rammeverk, bygger grunnleggende MCP-servere, lager vertsapplikasjoner og tester implementeringene dine.

Model Context Protocol (MCP) er en åpen protokoll som standardiserer hvordan applikasjoner gir kontekst til LLM-er. Tenk på MCP som en USB-C-port for AI-applikasjoner – det gir en standardisert måte å koble AI-modeller til forskjellige datakilder og verktøy.

## Læringsmål

Ved slutten av denne leksjonen vil du kunne:

- Sette opp utviklingsmiljøer for MCP i C#, Java, Python, TypeScript og Rust
- Bygge og distribuere grunnleggende MCP-servere med tilpassede funksjoner (ressurser, prompts og verktøy)
- Lage vertsapplikasjoner som kobler til MCP-servere
- Teste og feilsøke MCP-implementeringer

## Sette opp ditt MCP-miljø

Før du begynner å jobbe med MCP, er det viktig å forberede utviklingsmiljøet ditt og forstå den grunnleggende arbeidsflyten. Denne seksjonen vil veilede deg gjennom de innledende oppsettsstegene for å sikre en smidig start med MCP.

### Forutsetninger

Før du dykker inn i MCP-utvikling, sørg for at du har:

- **Utviklingsmiljø**: For ditt valgte språk (C#, Java, Python, TypeScript eller Rust)
- **IDE/Editor**: Visual Studio, Visual Studio Code, IntelliJ, Eclipse, PyCharm eller en moderne kodeeditor
- **Pakkebehandlere**: NuGet, Maven/Gradle, pip, npm/yarn eller Cargo
- **API-nøkler**: For eventuelle AI-tjenester du planlegger å bruke i vertsapplikasjonene dine

## Grunnleggende MCP-serverstruktur

En MCP-server inkluderer vanligvis:

- **Serverkonfigurasjon**: Oppsett av port, autentisering og andre innstillinger
- **Ressurser**: Data og kontekst gjort tilgjengelig for LLM-er
- **Verktøy**: Funksjonalitet som modeller kan påkalle
- **Prompts**: Maler for å generere eller strukturere tekst

Her er et forenklet eksempel i TypeScript:

```typescript
import { McpServer, ResourceTemplate } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";

// Opprett en MCP-server
const server = new McpServer({
  name: "Demo",
  version: "1.0.0"
});

// Legg til et tillegg verktøy
server.tool("add",
  { a: z.number(), b: z.number() },
  async ({ a, b }) => ({
    content: [{ type: "text", text: String(a + b) }]
  })
);

// Legg til en dynamisk hilsenressurs
server.resource(
  "file",
  // 'list'-parameteren styrer hvordan ressursen viser tilgjengelige filer. Å sette den til undefined deaktiverer visning for denne ressursen.
  new ResourceTemplate("file://{path}", { list: undefined }),
  async (uri, { path }) => ({
    contents: [{
      uri: uri.href,
      text: `File, ${path}!`
    }]
  })
);

// Legg til en filressurs som leser filinnholdet
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

// Begynn å motta meldinger på stdin og sende meldinger på stdout
const transport = new StdioServerTransport();
await server.connect(transport);
```

I koden ovenfor:

- Importerer vi nødvendige klasser fra MCP TypeScript SDK.
- Oppretter og konfigurerer en ny MCP-serverinstans.
- Registrerer et tilpasset verktøy (`calculator`) med en håndteringsfunksjon.
- Starter serveren for å lytte etter innkommende MCP-forespørsler.

## Testing og feilsøking

Før du begynner å teste MCP-serveren din, er det viktig å forstå tilgjengelige verktøy og beste praksis for feilsøking. Effektiv testing sikrer at serveren oppfører seg som forventet og hjelper deg raskt å identifisere og løse problemer. Følgende seksjon skisserer anbefalte tilnærminger for å validere din MCP-implementering.

MCP tilbyr verktøy som hjelper deg å teste og feilsøke serverne dine:

- **Inspector-verktøyet**, dette grafiske grensesnittet lar deg koble til serveren din og teste verktøy, prompts og ressurser.
- **curl**, du kan også koble til serveren din ved hjelp av et kommandolinjeverktøy som curl eller andre klienter som kan lage og kjøre HTTP-kommandoer.

### Bruke MCP Inspector

[MCP Inspector](https://github.com/modelcontextprotocol/inspector) er et visuelt testverktøy som hjelper deg med å:

1. **Oppdage serverkapasiteter**: Automatisk oppdage tilgjengelige ressurser, verktøy og prompts
2. **Teste verktøykjøring**: Prøve forskjellige parametere og se svar i sanntid
3. **Se servermetadata**: Undersøke serverinfo, skjemaer og konfigurasjoner

```bash
# for eksempel TypeScript, installere og kjøre MCP Inspector
npx @modelcontextprotocol/inspector node build/index.js
```

Når du kjører kommandoene ovenfor, vil MCP Inspector starte et lokalt webgrensesnitt i nettleseren din. Du kan forvente å se et dashbord som viser dine registrerte MCP-servere, deres tilgjengelige verktøy, ressurser og prompts. Grensesnittet lar deg interaktivt teste verktøykjøring, inspisere servermetadata og se svar i sanntid, noe som gjør det enklere å validere og feilsøke dine MCP-serverimplementeringer.

Her er et skjermbilde av hvordan det kan se ut:

![MCP Inspector server connection](../../../../translated_images/connected.73d1e042c24075d386cacdd4ee7cd748c16364c277d814e646ff2f7b5eefde85.no.png)

## Vanlige oppsettproblemer og løsninger

| Problem | Mulig løsning |
|---------|---------------|
| Tilkobling nektet | Sjekk om serveren kjører og at porten er korrekt |
| Feil ved verktøykjøring | Gå gjennom parameter-validering og feilhåndtering |
| Autentiseringsfeil | Verifiser API-nøkler og tillatelser |
| Skjemavalideringsfeil | Sørg for at parametere samsvarer med definert skjema |
| Server starter ikke | Sjekk for portkonflikter eller manglende avhengigheter |
| CORS-feil | Konfigurer riktige CORS-headere for kryss-opprinnelsesforespørsler |
| Autentiseringsproblemer | Verifiser token gyldighet og tillatelser |

## Lokal utvikling

For lokal utvikling og testing kan du kjøre MCP-servere direkte på maskinen din:

1. **Start serverprosessen**: Kjør MCP-serverapplikasjonen din
2. **Konfigurer nettverk**: Sørg for at serveren er tilgjengelig på forventet port
3. **Koble til klienter**: Bruk lokale tilkoblings-URLer som `http://localhost:3000`

```bash
# Eksempel: Kjøre en TypeScript MCP-server lokalt
npm run start
# Server kjører på http://localhost:3000
```

## Bygge din første MCP-server

Vi har dekket [Kjernebegreper](/01-CoreConcepts/README.md) i en tidligere leksjon, nå er det på tide å sette den kunnskapen ut i praksis.

### Hva en server kan gjøre

Før vi begynner å skrive kode, la oss minne oss selv på hva en server kan gjøre:

En MCP-server kan for eksempel:

- Få tilgang til lokale filer og databaser
- Koble til eksterne API-er
- Utføre beregninger
- Integrere med andre verktøy og tjenester
- Tilby et brukergrensesnitt for interaksjon

Flott, nå som vi vet hva vi kan gjøre for den, la oss begynne å kode.

## Øvelse: Lage en server

For å lage en server må du følge disse stegene:

- Installer MCP SDK.
- Opprett et prosjekt og sett opp prosjektstrukturen.
- Skriv serverkoden.
- Test serveren.

### -1- Opprett prosjekt

#### TypeScript

```sh
# Opprett prosjektmappe og initialiser npm-prosjekt
mkdir calculator-server
cd calculator-server
npm init -y
```

#### Python

```sh
# Opprett prosjektmappe
mkdir calculator-server
cd calculator-server
# Åpne mappen i Visual Studio Code - Hopp over dette hvis du bruker en annen IDE
code .
```

#### .NET

```sh
dotnet new console -n McpCalculatorServer
cd McpCalculatorServer
```

#### Java

For Java, opprett et Spring Boot-prosjekt:

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

Pakk ut zip-filen:

```bash
unzip calculator-server.zip -d calculator-server
cd calculator-server
# valgfritt fjern den ubrukte testen
rm -rf src/test/java
```

Legg til følgende komplette konfigurasjon i din *pom.xml*-fil:

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

### -2- Legg til avhengigheter

Nå som du har opprettet prosjektet, la oss legge til avhengigheter:

#### TypeScript

```sh
# Hvis det ikke allerede er installert, installer TypeScript globalt
npm install typescript -g

# Installer MCP SDK og Zod for skjema-validering
npm install @modelcontextprotocol/sdk zod
npm install -D @types/node typescript
```

#### Python

```sh
# Opprett et virtuelt miljø og installer avhengigheter
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

### -3- Opprett prosjektfiler

#### TypeScript

Åpne *package.json*-filen og erstatt innholdet med følgende for å sikre at du kan bygge og kjøre serveren:

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

Opprett en *tsconfig.json* med følgende innhold:

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

Opprett en katalog for kildekoden din:

```sh
mkdir src
touch src/index.ts
```

#### Python

Opprett en fil *server.py*

```sh
touch server.py
```

#### .NET

Installer nødvendige NuGet-pakker:

```sh
dotnet add package ModelContextProtocol --prerelease
dotnet add package Microsoft.Extensions.Hosting
```

#### Java

For Java Spring Boot-prosjekter opprettes prosjektstrukturen automatisk.

#### Rust

For Rust opprettes en *src/main.rs*-fil som standard når du kjører `cargo init`. Åpne filen og slett standardkoden.

### -4- Lag serverkode

#### TypeScript

Opprett en fil *index.ts* og legg til følgende kode:

```typescript
import { McpServer, ResourceTemplate } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";
 
// Opprett en MCP-server
const server = new McpServer({
  name: "Calculator MCP Server",
  version: "1.0.0"
});
```

Nå har du en server, men den gjør ikke så mye, la oss fikse det.

#### Python

```python
# server.py
from mcp.server.fastmcp import FastMCP

# Opprett en MCP-server
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

For Java, opprett kjernekomponentene for serveren. Først, endre hovedapplikasjonsklassen:

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

Opprett kalkulatortjenesten *src/main/java/com/microsoft/mcp/sample/server/service/CalculatorService.java*:

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

**Valgfrie komponenter for en produksjonsklar tjeneste:**

Opprett en oppstartskonfigurasjon *src/main/java/com/microsoft/mcp/sample/server/config/StartupConfig.java*:

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

Opprett en helsekontroller *src/main/java/com/microsoft/mcp/sample/server/controller/HealthController.java*:

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

Opprett en unntakshåndterer *src/main/java/com/microsoft/mcp/sample/server/exception/GlobalExceptionHandler.java*:

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

        // Gettere
        public String getCode() { return code; }
        public String getMessage() { return message; }
    }
}
```

Opprett et tilpasset banner *src/main/resources/banner.txt*:

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

Legg til følgende kode øverst i *src/main.rs*-filen. Dette importerer nødvendige biblioteker og moduler for MCP-serveren din.

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

Kalkulatorserveren vil være enkel og kan legge sammen to tall. La oss lage en struct for å representere kalkulatorforespørselen.

```rust
#[derive(Debug, serde::Deserialize, schemars::JsonSchema)]
pub struct CalculatorRequest {
    pub a: f64,
    pub b: f64,
}
```

Deretter lager vi en struct for å representere kalkulatorserveren. Denne structen vil holde verktøyruteren, som brukes til å registrere verktøy.

```rust
#[derive(Debug, Clone)]
pub struct Calculator {
    tool_router: ToolRouter<Self>,
}
```

Nå kan vi implementere `Calculator`-structen for å lage en ny instans av serveren og implementere serverhåndtereren for å gi serverinformasjon.

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

Til slutt må vi implementere main-funksjonen for å starte serveren. Denne funksjonen vil lage en instans av `Calculator`-structen og serve den over standard input/output.

```rust
#[tokio::main]
async fn main() -> Result<(), Box<dyn Error>> {
    let service = Calculator::new().serve(stdio()).await?;
    service.waiting().await?;
    Ok(())
}
```

Serveren er nå satt opp til å gi grunnleggende informasjon om seg selv. Neste steg er å legge til et verktøy for å utføre addisjon.

### -5- Legge til et verktøy og en ressurs

Legg til et verktøy og en ressurs ved å legge til følgende kode:

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

Verktøyet ditt tar parametrene `a` og `b` og kjører en funksjon som produserer et svar på formen:

```typescript
{
  contents: [{
    type: "text", content: "some content"
  }]
}
```

Ressursen din nås gjennom strengen "greeting" og tar parameteren `name` og produserer et lignende svar som verktøyet:

```typescript
{
  uri: "<href>",
  text: "a text"
}
```

#### Python

```python
# Legg til et tillegg verktøy
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


# Legg til en dynamisk hilsen ressurs
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}!"
```

I koden ovenfor har vi:

- Definert et verktøy `add` som tar parametrene `a` og `b`, begge heltall.
- Opprettet en ressurs kalt `greeting` som tar parameteren `name`.

#### .NET

Legg dette til i din Program.cs-fil:

```csharp
[McpServerToolType]
public static class CalculatorTool
{
    [McpServerTool, Description("Adds two numbers")]
    public static string Add(int a, int b) => $"Sum {a + b}";
}
```

#### Java

Verktøyene er allerede opprettet i forrige steg.

#### Rust

Legg til et nytt verktøy inne i `impl Calculator`-blokken:

```rust
#[tool(description = "Adds a and b")]
async fn add(
    &self,
    Parameters(CalculatorRequest { a, b }): Parameters<CalculatorRequest>,
) -> String {
    (a + b).to_string()
}
```

### -6- Endelig kode

La oss legge til den siste koden vi trenger slik at serveren kan starte:

#### TypeScript

```typescript
// Begynn å motta meldinger på stdin og sende meldinger på stdout
const transport = new StdioServerTransport();
await server.connect(transport);
```

Her er hele koden:

```typescript
// index.ts
import { McpServer, ResourceTemplate } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";

// Opprett en MCP-server
const server = new McpServer({
  name: "Calculator MCP Server",
  version: "1.0.0"
});

// Legg til et tillegg verktøy
server.tool(
  "add",
  { a: z.number(), b: z.number() },
  async ({ a, b }) => ({
    content: [{ type: "text", text: String(a + b) }]
  })
);

// Legg til en dynamisk hilsen ressurs
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

// Begynn å motta meldinger på stdin og sende meldinger på stdout
const transport = new StdioServerTransport();
server.connect(transport);
```

#### Python

```python
# server.py
from mcp.server.fastmcp import FastMCP

# Opprett en MCP-server
mcp = FastMCP("Demo")


# Legg til et tillegg verktøy
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


# Legg til en dynamisk hilsen ressurs
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}!"

# Hovedutførelsesblokk - dette er nødvendig for å kjøre serveren
if __name__ == "__main__":
    mcp.run()
```

#### .NET

Opprett en Program.cs-fil med følgende innhold:

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

Din komplette hovedapplikasjonsklasse skal se slik ut:

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

Den endelige koden for Rust-serveren skal se slik ut:

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

### -7- Test serveren

Start serveren med følgende kommando:

#### TypeScript

```sh
npm run build
```

#### Python

```sh
mcp run server.py
```

> For å bruke MCP Inspector, bruk `mcp dev server.py` som automatisk starter Inspector og gir nødvendig proxy session token. Hvis du bruker `mcp run server.py`, må du manuelt starte Inspector og konfigurere tilkoblingen.

#### .NET

Sørg for at du er i prosjektmappen din:

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

Kjør følgende kommandoer for å formatere og kjøre serveren:

```sh
cargo fmt
cargo run
```

### -8- Kjør med inspector

Inspector er et flott verktøy som kan starte serveren din og lar deg interagere med den slik at du kan teste at den fungerer. La oss starte den:

> [!NOTE]
> Det kan se annerledes ut i "command"-feltet da det inneholder kommandoen for å kjøre en server med din spesifikke runtime/

#### TypeScript

```sh
npx @modelcontextprotocol/inspector node build/index.js
```

eller legg det til i din *package.json* slik: `"inspector": "npx @modelcontextprotocol/inspector node build/index.js"` og kjør deretter `npm run inspector`

#### Python

Python pakker inn et Node.js-verktøy kalt inspector. Det er mulig å kalle dette verktøyet slik:

```sh
mcp dev server.py
```

Men det implementerer ikke alle metodene som er tilgjengelige i verktøyet, så det anbefales å kjøre Node.js-verktøyet direkte som vist nedenfor:

```sh
npx @modelcontextprotocol/inspector mcp run server.py
```

Hvis du bruker et verktøy eller IDE som lar deg konfigurere kommandoer og argumenter for å kjøre skript, 
sørg for å sette `python` i `Command`-feltet og `server.py` som `Arguments`. Dette sikrer at skriptet kjører riktig.

#### .NET

Sørg for at du er i prosjektmappen din:

```sh
cd McpCalculatorServer
npx @modelcontextprotocol/inspector dotnet run
```

#### Java

Sørg for at kalkulatorserveren din kjører
Deretter kjører du inspektøren:

```cmd
npx @modelcontextprotocol/inspector
```

I inspektørens nettgrensesnitt:

1. Velg "SSE" som transporttype
2. Sett URL-en til: `http://localhost:8080/sse`
3. Klikk "Connect"

![Connect](../../../../translated_images/tool.163d33e3ee307e209ef146d8f85060d2f7e83e9f59b3b1699a77204ae0454ad2.no.png)

**Du er nå koblet til serveren**
**Java-server testseksjonen er nå fullført**

Neste seksjon handler om å samhandle med serveren.

Du bør se følgende brukergrensesnitt:

![Connect](../../../../translated_images/connect.141db0b2bd05f096fb1dd91273771fd8b2469d6507656c3b0c9df4b3c5473929.no.png)

1. Koble til serveren ved å velge Connect-knappen
  Når du kobler til serveren, bør du nå se følgende:

  ![Connected](../../../../translated_images/connected.73d1e042c24075d386cacdd4ee7cd748c16364c277d814e646ff2f7b5eefde85.no.png)

1. Velg "Tools" og "listTools", du bør se "Add" dukke opp, velg "Add" og fyll inn parameterverdiene.

  Du bør se følgende svar, altså et resultat fra "add"-verktøyet:

  ![Result of running add](../../../../translated_images/ran-tool.a5a6ee878c1369ec1e379b81053395252a441799dbf23416c36ddf288faf8249.no.png)

Gratulerer, du har klart å lage og kjøre din første server!

#### Rust

For å kjøre Rust-serveren med MCP Inspector CLI, bruk følgende kommando:

```sh
npx @modelcontextprotocol/inspector cargo run --cli --method tools/call --tool-name add --tool-arg a=1 b=2
```

### Offisielle SDK-er

MCP tilbyr offisielle SDK-er for flere språk:

- [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk) - Vedlikeholdes i samarbeid med Microsoft
- [Java SDK](https://github.com/modelcontextprotocol/java-sdk) - Vedlikeholdes i samarbeid med Spring AI
- [TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk) - Den offisielle TypeScript-implementeringen
- [Python SDK](https://github.com/modelcontextprotocol/python-sdk) - Den offisielle Python-implementeringen
- [Kotlin SDK](https://github.com/modelcontextprotocol/kotlin-sdk) - Den offisielle Kotlin-implementeringen
- [Swift SDK](https://github.com/modelcontextprotocol/swift-sdk) - Vedlikeholdes i samarbeid med Loopwork AI
- [Rust SDK](https://github.com/modelcontextprotocol/rust-sdk) - Den offisielle Rust-implementeringen

## Viktige punkter

- Å sette opp et MCP-utviklingsmiljø er enkelt med språkspesifikke SDK-er
- Å bygge MCP-servere innebærer å lage og registrere verktøy med klare skjemaer
- Testing og feilsøking er essensielt for pålitelige MCP-implementasjoner

## Eksempler

- [Java Calculator](../samples/java/calculator/README.md)
- [.Net Calculator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Calculator](../samples/javascript/README.md)
- [TypeScript Calculator](../samples/typescript/README.md)
- [Python Calculator](../../../../03-GettingStarted/samples/python)
- [Rust Calculator](../../../../03-GettingStarted/samples/rust)

## Oppgave

Lag en enkel MCP-server med et verktøy etter eget valg:

1. Implementer verktøyet i ditt foretrukne språk (.NET, Java, Python, TypeScript eller Rust).
2. Definer inndata-parametere og returverdier.
3. Kjør inspektørverktøyet for å sikre at serveren fungerer som forventet.
4. Test implementeringen med ulike inndata.

## Løsning

[Løsning](./solution/README.md)

## Ytterligere ressurser

- [Bygg agenter med Model Context Protocol på Azure](https://learn.microsoft.com/azure/developer/ai/intro-agents-mcp)
- [Fjernstyrt MCP med Azure Container Apps (Node.js/TypeScript/JavaScript)](https://learn.microsoft.com/samples/azure-samples/mcp-container-ts/mcp-container-ts/)
- [.NET OpenAI MCP Agent](https://learn.microsoft.com/samples/azure-samples/openai-mcp-agent-dotnet/openai-mcp-agent-dotnet/)

## Hva nå

Neste: [Kom i gang med MCP-klienter](../02-client/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vennligst vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->