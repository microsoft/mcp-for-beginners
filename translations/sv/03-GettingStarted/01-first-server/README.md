<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8fdac7600a5f4722643d0f14e15ac259",
  "translation_date": "2025-12-11T06:42:17+00:00",
  "source_file": "03-GettingStarted/01-first-server/README.md",
  "language_code": "sv"
}
-->
# Komma igång med MCP

Välkommen till dina första steg med Model Context Protocol (MCP)! Oavsett om du är ny på MCP eller vill fördjupa din förståelse, kommer denna guide att leda dig genom den grundläggande installationen och utvecklingsprocessen. Du kommer att upptäcka hur MCP möjliggör sömlös integration mellan AI-modeller och applikationer, och lära dig hur du snabbt förbereder din miljö för att bygga och testa lösningar som drivs av MCP.

> TLDR; Om du bygger AI-appar vet du att du kan lägga till verktyg och andra resurser till din LLM (stora språkmodell) för att göra LLM mer kunnig. Men om du placerar dessa verktyg och resurser på en server kan appen och serverns kapabiliteter användas av vilken klient som helst med eller utan en LLM.

## Översikt

Denna lektion ger praktisk vägledning för att sätta upp MCP-miljöer och bygga dina första MCP-applikationer. Du kommer att lära dig hur du installerar nödvändiga verktyg och ramverk, bygger grundläggande MCP-servrar, skapar värd-applikationer och testar dina implementationer.

Model Context Protocol (MCP) är ett öppet protokoll som standardiserar hur applikationer tillhandahåller kontext till LLM:er. Tänk på MCP som en USB-C-port för AI-applikationer – det ger ett standardiserat sätt att koppla AI-modeller till olika datakällor och verktyg.

## Lärandemål

I slutet av denna lektion kommer du att kunna:

- Sätta upp utvecklingsmiljöer för MCP i C#, Java, Python, TypeScript och Rust
- Bygga och distribuera grundläggande MCP-servrar med anpassade funktioner (resurser, prompts och verktyg)
- Skapa värd-applikationer som ansluter till MCP-servrar
- Testa och felsöka MCP-implementationer

## Sätta upp din MCP-miljö

Innan du börjar arbeta med MCP är det viktigt att förbereda din utvecklingsmiljö och förstå den grundläggande arbetsflödet. Denna sektion guidar dig genom de initiala installationsstegen för att säkerställa en smidig start med MCP.

### Förutsättningar

Innan du dyker in i MCP-utveckling, se till att du har:

- **Utvecklingsmiljö**: För ditt valda språk (C#, Java, Python, TypeScript eller Rust)
- **IDE/Editor**: Visual Studio, Visual Studio Code, IntelliJ, Eclipse, PyCharm eller någon modern kodredigerare
- **Paketchefer**: NuGet, Maven/Gradle, pip, npm/yarn eller Cargo
- **API-nycklar**: För alla AI-tjänster du planerar att använda i dina värd-applikationer

## Grundläggande MCP-serverstruktur

En MCP-server inkluderar vanligtvis:

- **Serverkonfiguration**: Ställ in port, autentisering och andra inställningar
- **Resurser**: Data och kontext som görs tillgängliga för LLM:er
- **Verktyg**: Funktionalitet som modeller kan anropa
- **Prompts**: Mallar för att generera eller strukturera text

Här är ett förenklat exempel i TypeScript:

```typescript
import { McpServer, ResourceTemplate } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";

// Skapa en MCP-server
const server = new McpServer({
  name: "Demo",
  version: "1.0.0"
});

// Lägg till ett additionsverktyg
server.tool("add",
  { a: z.number(), b: z.number() },
  async ({ a, b }) => ({
    content: [{ type: "text", text: String(a + b) }]
  })
);

// Lägg till en dynamisk hälsningsresurs
server.resource(
  "file",
  // Parametern 'list' styr hur resursen listar tillgängliga filer. Att sätta den till undefined inaktiverar listning för denna resurs.
  new ResourceTemplate("file://{path}", { list: undefined }),
  async (uri, { path }) => ({
    contents: [{
      uri: uri.href,
      text: `File, ${path}!`
    }]
  })
);

// Lägg till en filresurs som läser filinnehållet
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

// Börja ta emot meddelanden på stdin och skicka meddelanden på stdout
const transport = new StdioServerTransport();
await server.connect(transport);
```

I koden ovan:

- Importerar vi nödvändiga klasser från MCP TypeScript SDK.
- Skapar och konfigurerar en ny MCP-serverinstans.
- Registrerar ett anpassat verktyg (`calculator`) med en hanteringsfunktion.
- Startar servern för att lyssna på inkommande MCP-förfrågningar.

## Testning och felsökning

Innan du börjar testa din MCP-server är det viktigt att förstå de tillgängliga verktygen och bästa praxis för felsökning. Effektiv testning säkerställer att din server beter sig som förväntat och hjälper dig snabbt att identifiera och lösa problem. Följande avsnitt beskriver rekommenderade metoder för att validera din MCP-implementation.

MCP tillhandahåller verktyg för att hjälpa dig testa och felsöka dina servrar:

- **Inspector-verktyget**, detta grafiska gränssnitt låter dig ansluta till din server och testa dina verktyg, prompts och resurser.
- **curl**, du kan också ansluta till din server med ett kommandoradsverktyg som curl eller andra klienter som kan skapa och köra HTTP-kommandon.

### Använda MCP Inspector

[MCP Inspector](https://github.com/modelcontextprotocol/inspector) är ett visuellt testverktyg som hjälper dig att:

1. **Upptäcka serverkapabiliteter**: Automatiskt upptäcka tillgängliga resurser, verktyg och prompts
2. **Testa verktygsexekvering**: Prova olika parametrar och se svar i realtid
3. **Visa servermetadata**: Granska serverinformation, scheman och konfigurationer

```bash
# ex TypeScript, installera och köra MCP Inspector
npx @modelcontextprotocol/inspector node build/index.js
```

När du kör ovanstående kommandon startar MCP Inspector ett lokalt webbgränssnitt i din webbläsare. Du kan förvänta dig att se en instrumentpanel som visar dina registrerade MCP-servrar, deras tillgängliga verktyg, resurser och prompts. Gränssnittet låter dig interaktivt testa verktygsexekvering, inspektera servermetadata och se svar i realtid, vilket gör det enklare att validera och felsöka dina MCP-serverimplementationer.

Här är en skärmbild av hur det kan se ut:

![MCP Inspector server connection](../../../../translated_images/connected.73d1e042c24075d386cacdd4ee7cd748c16364c277d814e646ff2f7b5eefde85.sv.png)

## Vanliga installationsproblem och lösningar

| Problem | Möjlig lösning |
|---------|----------------|
| Anslutning nekad | Kontrollera att servern körs och att porten är korrekt |
| Fel vid verktygsexekvering | Granska parameterkontroll och felhantering |
| Autentiseringsfel | Verifiera API-nycklar och behörigheter |
| Schema-valideringsfel | Säkerställ att parametrar matchar det definierade schemat |
| Server startar inte | Kontrollera portkonflikter eller saknade beroenden |
| CORS-fel | Konfigurera korrekta CORS-rubriker för cross-origin-förfrågningar |
| Autentiseringsproblem | Verifiera token giltighet och behörigheter |

## Lokal utveckling

För lokal utveckling och testning kan du köra MCP-servrar direkt på din dator:

1. **Starta serverprocessen**: Kör din MCP-serverapplikation
2. **Konfigurera nätverk**: Säkerställ att servern är tillgänglig på förväntad port
3. **Anslut klienter**: Använd lokala anslutnings-URL:er som `http://localhost:3000`

```bash
# Exempel: Köra en TypeScript MCP-server lokalt
npm run start
# Server körs på http://localhost:3000
```

## Bygga din första MCP-server

Vi har täckt [Kärnbegrepp](/01-CoreConcepts/README.md) i en tidigare lektion, nu är det dags att omsätta den kunskapen i praktiken.

### Vad en server kan göra

Innan vi börjar skriva kod, låt oss påminna oss vad en server kan göra:

En MCP-server kan till exempel:

- Åtkomst till lokala filer och databaser
- Ansluta till fjärr-API:er
- Utföra beräkningar
- Integrera med andra verktyg och tjänster
- Tillhandahålla ett användargränssnitt för interaktion

Bra, nu när vi vet vad vi kan göra för den, låt oss börja koda.

## Övning: Skapa en server

För att skapa en server behöver du följa dessa steg:

- Installera MCP SDK.
- Skapa ett projekt och sätt upp projektstrukturen.
- Skriv serverkoden.
- Testa servern.

### -1- Skapa projekt

#### TypeScript

```sh
# Skapa projektmapp och initiera npm-projekt
mkdir calculator-server
cd calculator-server
npm init -y
```

#### Python

```sh
# Skapa projektmapp
mkdir calculator-server
cd calculator-server
# Öppna mappen i Visual Studio Code - Hoppa över detta om du använder en annan IDE
code .
```

#### .NET

```sh
dotnet new console -n McpCalculatorServer
cd McpCalculatorServer
```

#### Java

För Java, skapa ett Spring Boot-projekt:

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

Packa upp zip-filen:

```bash
unzip calculator-server.zip -d calculator-server
cd calculator-server
# valfritt ta bort det oanvända testet
rm -rf src/test/java
```

Lägg till följande kompletta konfiguration i din *pom.xml*-fil:

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

### -2- Lägg till beroenden

Nu när du har skapat ditt projekt, låt oss lägga till beroenden:

#### TypeScript

```sh
# Om det inte redan är installerat, installera TypeScript globalt
npm install typescript -g

# Installera MCP SDK och Zod för schema validering
npm install @modelcontextprotocol/sdk zod
npm install -D @types/node typescript
```

#### Python

```sh
# Skapa en virtuell miljö och installera beroenden
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

### -3- Skapa projektfiler

#### TypeScript

Öppna filen *package.json* och ersätt innehållet med följande för att säkerställa att du kan bygga och köra servern:

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

Skapa en *tsconfig.json* med följande innehåll:

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

Skapa en katalog för din källkod:

```sh
mkdir src
touch src/index.ts
```

#### Python

Skapa en fil *server.py*

```sh
touch server.py
```

#### .NET

Installera nödvändiga NuGet-paket:

```sh
dotnet add package ModelContextProtocol --prerelease
dotnet add package Microsoft.Extensions.Hosting
```

#### Java

För Java Spring Boot-projekt skapas projektstrukturen automatiskt.

#### Rust

För Rust skapas en *src/main.rs*-fil som standard när du kör `cargo init`. Öppna filen och ta bort standardkoden.

### -4- Skapa serverkod

#### TypeScript

Skapa en fil *index.ts* och lägg till följande kod:

```typescript
import { McpServer, ResourceTemplate } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";
 
// Skapa en MCP-server
const server = new McpServer({
  name: "Calculator MCP Server",
  version: "1.0.0"
});
```

Nu har du en server, men den gör inte mycket, låt oss fixa det.

#### Python

```python
# server.py
from mcp.server.fastmcp import FastMCP

# Skapa en MCP-server
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

För Java, skapa kärnserverkomponenterna. Modifiera först huvudapplikationsklassen:

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

Skapa kalkylatortjänsten *src/main/java/com/microsoft/mcp/sample/server/service/CalculatorService.java*:

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

**Valfria komponenter för en produktionsklar tjänst:**

Skapa en startkonfiguration *src/main/java/com/microsoft/mcp/sample/server/config/StartupConfig.java*:

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

Skapa en hälsokontroller *src/main/java/com/microsoft/mcp/sample/server/controller/HealthController.java*:

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

Skapa en undantagshanterare *src/main/java/com/microsoft/mcp/sample/server/exception/GlobalExceptionHandler.java*:

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

Skapa en anpassad banner *src/main/resources/banner.txt*:

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

Lägg till följande kod högst upp i *src/main.rs*-filen. Detta importerar nödvändiga bibliotek och moduler för din MCP-server.

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

Kalkylatorsservern kommer att vara en enkel som kan addera två tal. Låt oss skapa en struct för att representera kalkylatorförfrågan.

```rust
#[derive(Debug, serde::Deserialize, schemars::JsonSchema)]
pub struct CalculatorRequest {
    pub a: f64,
    pub b: f64,
}
```

Skapa sedan en struct för att representera kalkylatorsservern. Denna struct kommer att hålla verktygsroutern, som används för att registrera verktyg.

```rust
#[derive(Debug, Clone)]
pub struct Calculator {
    tool_router: ToolRouter<Self>,
}
```

Nu kan vi implementera `Calculator`-structen för att skapa en ny instans av servern och implementera serverhanteraren för att tillhandahålla serverinformation.

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

Slutligen behöver vi implementera huvudfunktionen för att starta servern. Denna funktion skapar en instans av `Calculator`-structen och serverar den över standard in/ut.

```rust
#[tokio::main]
async fn main() -> Result<(), Box<dyn Error>> {
    let service = Calculator::new().serve(stdio()).await?;
    service.waiting().await?;
    Ok(())
}
```

Servern är nu inställd för att tillhandahålla grundläggande information om sig själv. Nästa steg är att lägga till ett verktyg för att utföra addition.

### -5- Lägga till ett verktyg och en resurs

Lägg till ett verktyg och en resurs genom att lägga till följande kod:

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

Ditt verktyg tar parametrarna `a` och `b` och kör en funktion som producerar ett svar i formen:

```typescript
{
  contents: [{
    type: "text", content: "some content"
  }]
}
```

Din resurs nås via strängen "greeting" och tar parametern `name` och producerar ett liknande svar som verktyget:

```typescript
{
  uri: "<href>",
  text: "a text"
}
```

#### Python

```python
# Lägg till ett additionsverktyg
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


# Lägg till en dynamisk hälsningsresurs
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}!"
```

I koden ovan har vi:

- Definierat ett verktyg `add` som tar parametrarna `a` och `b`, båda heltal.
- Skapat en resurs kallad `greeting` som tar parametern `name`.

#### .NET

Lägg till detta i din Program.cs-fil:

```csharp
[McpServerToolType]
public static class CalculatorTool
{
    [McpServerTool, Description("Adds two numbers")]
    public static string Add(int a, int b) => $"Sum {a + b}";
}
```

#### Java

Verktygen har redan skapats i föregående steg.

#### Rust

Lägg till ett nytt verktyg inuti `impl Calculator`-blocket:

```rust
#[tool(description = "Adds a and b")]
async fn add(
    &self,
    Parameters(CalculatorRequest { a, b }): Parameters<CalculatorRequest>,
) -> String {
    (a + b).to_string()
}
```

### -6- Slutgiltig kod

Låt oss lägga till den sista koden vi behöver så att servern kan starta:

#### TypeScript

```typescript
// Börja ta emot meddelanden på stdin och skicka meddelanden på stdout
const transport = new StdioServerTransport();
await server.connect(transport);
```

Här är hela koden:

```typescript
// index.ts
import { McpServer, ResourceTemplate } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";

// Skapa en MCP-server
const server = new McpServer({
  name: "Calculator MCP Server",
  version: "1.0.0"
});

// Lägg till ett tilläggsverktyg
server.tool(
  "add",
  { a: z.number(), b: z.number() },
  async ({ a, b }) => ({
    content: [{ type: "text", text: String(a + b) }]
  })
);

// Lägg till en dynamisk hälsningsresurs
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

// Börja ta emot meddelanden på stdin och skicka meddelanden på stdout
const transport = new StdioServerTransport();
server.connect(transport);
```

#### Python

```python
# server.py
from mcp.server.fastmcp import FastMCP

# Skapa en MCP-server
mcp = FastMCP("Demo")


# Lägg till ett additionsverktyg
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


# Lägg till en dynamisk hälsningsresurs
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}!"

# Huvudkörningsblock - detta krävs för att köra servern
if __name__ == "__main__":
    mcp.run()
```

#### .NET

Skapa en Program.cs-fil med följande innehåll:

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

Din kompletta huvudapplikationsklass bör se ut så här:

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

Den slutgiltiga koden för Rust-servern bör se ut så här:

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

### -7- Testa servern

Starta servern med följande kommando:

#### TypeScript

```sh
npm run build
```

#### Python

```sh
mcp run server.py
```

> För att använda MCP Inspector, använd `mcp dev server.py` som automatiskt startar Inspector och tillhandahåller den nödvändiga proxy-sessionstoken. Om du använder `mcp run server.py` måste du manuellt starta Inspector och konfigurera anslutningen.

#### .NET

Se till att du är i din projektkatalog:

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

Kör följande kommandon för att formatera och köra servern:

```sh
cargo fmt
cargo run
```

### -8- Kör med inspector

Inspector är ett utmärkt verktyg som kan starta din server och låter dig interagera med den så att du kan testa att den fungerar. Låt oss starta den:

> [!NOTE]
> det kan se annorlunda ut i "command"-fältet eftersom det innehåller kommandot för att köra en server med din specifika runtime/

#### TypeScript

```sh
npx @modelcontextprotocol/inspector node build/index.js
```

eller lägg till det i din *package.json* så här: `"inspector": "npx @modelcontextprotocol/inspector node build/index.js"` och kör sedan `npm run inspector`

#### Python

Python omsluter ett Node.js-verktyg som heter inspector. Det är möjligt att anropa detta verktyg så här:

```sh
mcp dev server.py
```

Men det implementerar inte alla metoder som finns tillgängliga i verktyget, så det rekommenderas att du kör Node.js-verktyget direkt som nedan:

```sh
npx @modelcontextprotocol/inspector mcp run server.py
```

Om du använder ett verktyg eller IDE som tillåter dig att konfigurera kommandon och argument för att köra skript, 
se till att ange `python` i fältet `Command` och `server.py` som `Arguments`. Detta säkerställer att skriptet körs korrekt.

#### .NET

Se till att du är i din projektkatalog:

```sh
cd McpCalculatorServer
npx @modelcontextprotocol/inspector dotnet run
```

#### Java

Se till att din kalkylatorserver körs
Kör sedan inspektören:

```cmd
npx @modelcontextprotocol/inspector
```

I inspektörens webbgränssnitt:

1. Välj "SSE" som transporttyp
2. Ange URL:en till: `http://localhost:8080/sse`
3. Klicka på "Connect"

![Connect](../../../../translated_images/tool.163d33e3ee307e209ef146d8f85060d2f7e83e9f59b3b1699a77204ae0454ad2.sv.png)

**Du är nu ansluten till servern**
**Testavsnittet för Java-servern är nu slutfört**

Nästa avsnitt handlar om att interagera med servern.

Du bör se följande användargränssnitt:

![Connect](../../../../translated_images/connect.141db0b2bd05f096fb1dd91273771fd8b2469d6507656c3b0c9df4b3c5473929.sv.png)

1. Anslut till servern genom att välja Connect-knappen
  När du ansluter till servern bör du nu se följande:

  ![Connected](../../../../translated_images/connected.73d1e042c24075d386cacdd4ee7cd748c16364c277d814e646ff2f7b5eefde85.sv.png)

1. Välj "Tools" och "listTools", du bör se "Add" dyka upp, välj "Add" och fyll i parametervärdena.

  Du bör se följande svar, dvs ett resultat från "add"-verktyget:

  ![Result of running add](../../../../translated_images/ran-tool.a5a6ee878c1369ec1e379b81053395252a441799dbf23416c36ddf288faf8249.sv.png)

Grattis, du har lyckats skapa och köra din första server!

#### Rust

För att köra Rust-servern med MCP Inspector CLI, använd följande kommando:

```sh
npx @modelcontextprotocol/inspector cargo run --cli --method tools/call --tool-name add --tool-arg a=1 b=2
```

### Officiella SDK:er

MCP tillhandahåller officiella SDK:er för flera språk:

- [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk) - Underhålls i samarbete med Microsoft
- [Java SDK](https://github.com/modelcontextprotocol/java-sdk) - Underhålls i samarbete med Spring AI
- [TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk) - Den officiella TypeScript-implementeringen
- [Python SDK](https://github.com/modelcontextprotocol/python-sdk) - Den officiella Python-implementeringen
- [Kotlin SDK](https://github.com/modelcontextprotocol/kotlin-sdk) - Den officiella Kotlin-implementeringen
- [Swift SDK](https://github.com/modelcontextprotocol/swift-sdk) - Underhålls i samarbete med Loopwork AI
- [Rust SDK](https://github.com/modelcontextprotocol/rust-sdk) - Den officiella Rust-implementeringen

## Viktiga punkter

- Att sätta upp en MCP-utvecklingsmiljö är enkelt med språksspecifika SDK:er
- Att bygga MCP-servrar innebär att skapa och registrera verktyg med tydliga scheman
- Testning och felsökning är avgörande för pålitliga MCP-implementationer

## Exempel

- [Java Calculator](../samples/java/calculator/README.md)
- [.Net Calculator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Calculator](../samples/javascript/README.md)
- [TypeScript Calculator](../samples/typescript/README.md)
- [Python Calculator](../../../../03-GettingStarted/samples/python)
- [Rust Calculator](../../../../03-GettingStarted/samples/rust)

## Uppgift

Skapa en enkel MCP-server med ett verktyg du väljer:

1. Implementera verktyget i ditt föredragna språk (.NET, Java, Python, TypeScript eller Rust).
2. Definiera inparametrar och returvärden.
3. Kör inspektörsverktyget för att säkerställa att servern fungerar som avsett.
4. Testa implementationen med olika indata.

## Lösning

[Lösning](./solution/README.md)

## Ytterligare resurser

- [Bygg agenter med Model Context Protocol på Azure](https://learn.microsoft.com/azure/developer/ai/intro-agents-mcp)
- [Fjärr-MCP med Azure Container Apps (Node.js/TypeScript/JavaScript)](https://learn.microsoft.com/samples/azure-samples/mcp-container-ts/mcp-container-ts/)
- [.NET OpenAI MCP Agent](https://learn.microsoft.com/samples/azure-samples/openai-mcp-agent-dotnet/openai-mcp-agent-dotnet/)

## Vad händer härnäst

Nästa: [Kom igång med MCP-klienter](../02-client/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfriskrivning**:
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, vänligen observera att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår till följd av användningen av denna översättning.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->