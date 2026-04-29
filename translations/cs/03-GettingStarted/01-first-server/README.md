# Začínáme s MCP

Vítejte na vašich prvních krocích s Model Context Protocol (MCP)! Ať už jste v MCP noví, nebo chcete prohloubit své znalosti, tento průvodce vás provede základním nastavením a vývojovým procesem. Zjistíte, jak MCP umožňuje bezproblémovou integraci mezi AI modely a aplikacemi, a naučíte se, jak rychle připravit své prostředí pro tvorbu a testování řešení poháněných MCP.

> TLDR; Pokud vytváříte aplikace s AI, víte, že můžete vašemu LLM (velkému jazykovému modelu) přidávat nástroje a další zdroje, aby byl LLM více informovaný. Pokud ale tyto nástroje a zdroje umístíte na server, kapacity aplikace i serveru mohou využít jakékoli klienty s LLM, tak i bez něj.

## Přehled

Tato lekce poskytuje praktické pokyny pro nastavení MCP prostředí a tvorbu vašich prvních MCP aplikací. Naučíte se, jak nastavit potřebné nástroje a frameworky, vytvořit základní MCP servery, vytvářet hostitelské aplikace a testovat vaše implementace.

Model Context Protocol (MCP) je otevřený protokol, který standardizuje způsob, jakým aplikace poskytují kontext LLM. MCP si můžete představit jako USB-C port pro AI aplikace – poskytuje standardizovaný způsob propojení AI modelů s různými zdroji dat a nástroji.

## Cíle učení

Na konci této lekce budete schopni:

- Nastavit vývojová prostředí pro MCP v jazycích C#, Java, Python, TypeScript a Rust
- Vytvořit a nasadit základní MCP servery s vlastními funkcemi (zdroje, výzvy a nástroje)
- Vytvořit hostitelské aplikace, které se připojují k MCP serverům
- Testovat a ladit implementace MCP

## Nastavení vašeho MCP prostředí

Předtím než začnete pracovat s MCP, je důležité připravit vaše vývojové prostředí a pochopit základní pracovní tok. Tato sekce vás provede počátečními kroky nastavení, aby byl start s MCP plynulý.

### Požadavky

Před ponořením do vývoje s MCP se ujistěte, že máte:

- **Vývojové prostředí**: Pro zvolený jazyk (C#, Java, Python, TypeScript nebo Rust)
- **IDE/Editor**: Visual Studio, Visual Studio Code, IntelliJ, Eclipse, PyCharm nebo jakýkoli moderní editor kódu
- **Správce balíčků**: NuGet, Maven/Gradle, pip, npm/yarn nebo Cargo
- **API klíče**: Pro všechny AI služby, které plánujete používat ve svých hostitelských aplikacích

## Základní struktura MCP serveru

MCP server obvykle zahrnuje:

- **Konfigurace serveru**: Nastavení portu, autentizace a dalších parametrů
- **Zdroje**: Data a kontext zpřístupněné pro LLM
- **Nástroje**: Funkce, které mohou modely volat
- **Výzvy**: Šablony pro generování nebo strukturování textu

Zde je zjednodušený příklad v TypeScriptu:

```typescript
import { McpServer, ResourceTemplate } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";

// Vytvořit MCP server
const server = new McpServer({
  name: "Demo",
  version: "1.0.0"
});

// Přidat nástroj pro sčítání
server.tool("add",
  { a: z.number(), b: z.number() },
  async ({ a, b }) => ({
    content: [{ type: "text", text: String(a + b) }]
  })
);

// Přidat dynamický zdroj pozdravu
server.resource(
  "file",
  // Parametr 'list' řídí, jak zdroj vypisuje dostupné soubory. Nastavení na undefined zakáže výpis pro tento zdroj.
  new ResourceTemplate("file://{path}", { list: undefined }),
  async (uri, { path }) => ({
    contents: [{
      uri: uri.href,
      text: `File, ${path}!`
    }]
  })
);

// Přidat zdroj souboru, který čte obsah souboru
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

// Začít přijímat zprávy na stdin a odesílat zprávy na stdout
const transport = new StdioServerTransport();
await server.connect(transport);
```

V předchozím kódu:

- Importujeme potřebné třídy z MCP TypeScript SDK.
- Vytváříme a konfigurujeme novou instanci MCP serveru.
- Registrujeme vlastní nástroj (`calculator`) s obslužnou funkcí.
- Spouštíme server a nasloucháme přicházejícím MCP požadavkům.

## Testování a ladění

Než začnete testovat svůj MCP server, je důležité pochopit dostupné nástroje a osvědčené postupy ladění. Efektivní testování zajistí, že server se chová podle očekávání a pomůže rychle identifikovat a vyřešit problémy. Následující sekce obsahuje doporučené přístupy pro ověření vaší MCP implementace.

MCP poskytuje nástroje pro testování a ladění serverů:

- **Inspector tool**, tento grafický nástroj vám umožní připojit se k serveru a testovat vaše nástroje, výzvy a zdroje.
- **curl**, můžete se také připojit k serveru pomocí příkazového řádku s nástrojem jako curl nebo jinými klienty, které umí vytvářet a spouštět HTTP příkazy.

### Použití MCP Inspector

[MCP Inspector](https://github.com/modelcontextprotocol/inspector) je vizuální testovací nástroj, který vám umožní:

1. **Objevování schopností serveru**: Automaticky detekuje dostupné zdroje, nástroje a výzvy
2. **Testování spuštění nástrojů**: Vyzkouší různé parametry a zobrazí odpovědi v reálném čase
3. **Zobrazení metadat serveru**: Prohlédne informace o serveru, schémata a konfigurace

```bash
# příklad TypeScript, instalace a spuštění MCP Inspector
npx @modelcontextprotocol/inspector node build/index.js
```

Po spuštění výše uvedených příkazů MCP Inspector otevře lokální webové rozhraní ve vašem prohlížeči. Můžete očekávat dashboard zobrazující vaše registrované MCP servery, jejich dostupné nástroje, zdroje a výzvy. Rozhraní vám umožňuje interaktivně testovat spouštění nástrojů, zkoumat metadata serveru a sledovat odpovědi v reálném čase, což usnadňuje ověřování a ladění implementací vašeho MCP serveru.

Zde je screenshot, jak může vypadat:

![MCP Inspector server connection](../../../../translated_images/cs/connected.73d1e042c24075d3.webp)

## Běžné problémy při nastavení a jejich řešení

| Problém | Možné řešení |
|---------|--------------|
| Odepřeno připojení | Zkontrolujte, zda je server spuštěný a port je správný |
| Chyby při vykonávání nástroje | Prověřte validaci parametrů a zpracování chyb |
| Selhání autentizace | Ověřte API klíče a oprávnění |
| Chyby validace schématu | Ujistěte se, že parametry odpovídají definovanému schématu |
| Server se nespouští | Zkontrolujte konflikt portů nebo chybějící závislosti |
| Chyby CORS | Nastavte správné CORS hlavičky pro cross-origin požadavky |
| Problémy s autentizací | Ověřte platnost tokenu a oprávnění |

## Lokální vývoj

Pro lokální vývoj a testování můžete MCP servery spustit přímo na svém počítači:

1. **Spusťte proces serveru**: Spusťte svou MCP serverovou aplikaci
2. **Nakonfigurujte síť**: Ujistěte se, že server je přístupný na očekávaném portu
3. **Připojte klienty**: Použijte lokální připojovací URL jako `http://localhost:3000`

```bash
# Příklad: Spuštění TypeScript MCP serveru lokálně
npm run start
# Server běží na http://localhost:3000
```

## Vytvoření vašeho prvního MCP serveru

Procvičili jsme si [Základní koncepty](../../01-CoreConcepts/README.md) v předchozí lekci, nyní je čas je uvést do praxe.

### Co server může dělat

Než začneme psát kód, připomeňme si, co všechno může server umět:

MCP server může například:

- Přistupovat k lokálním souborům a databázím
- Připojovat se k vzdáleným API
- Provádět výpočty
- Integrovat se s dalšími nástroji a službami
- Poskytovat uživatelské rozhraní pro interakci

Skvělé, teď když víme, co všechno můžeme dělat, pojďme začít programovat.

## Cvičení: Vytvoření serveru

Pro vytvoření serveru musíte projít těmito kroky:

- Nainstalovat MCP SDK.
- Vytvořit projekt a nastavit strukturu projektu.
- Napsat serverový kód.
- Otestovat server.

### -1- Vytvoření projektu

#### TypeScript

```sh
# Vytvořte adresář projektu a inicializujte npm projekt
mkdir calculator-server
cd calculator-server
npm init -y
```

#### Python

```sh
# Vytvořit adresář projektu
mkdir calculator-server
cd calculator-server
# Otevřete složku ve Visual Studio Code - přeskočit, pokud používáte jiné IDE
code .
```

#### .NET

```sh
dotnet new console -n McpCalculatorServer
cd McpCalculatorServer
```

#### Java

Pro Javu vytvořte Spring Boot projekt:

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

Rozbalte zip soubor:

```bash
unzip calculator-server.zip -d calculator-server
cd calculator-server
# volitelně odstraňte nepoužitý test
rm -rf src/test/java
```

Přidejte následující kompletní konfiguraci do souboru *pom.xml*:

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

### -2- Přidání závislostí

Nyní, když máte projekt vytvořený, přidejme další závislosti:

#### TypeScript

```sh
# Pokud není již nainstalován, nainstalujte TypeScript globálně
npm install typescript -g

# Nainstalujte MCP SDK a Zod pro ověřování schémat
npm install @modelcontextprotocol/sdk zod
npm install -D @types/node typescript
```

#### Python

```sh
# Vytvořte virtuální prostředí a nainstalujte závislosti
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

### -3- Vytvoření souborů projektu

#### TypeScript

Otevřete soubor *package.json* a nahraďte jeho obsah tímto, aby bylo možné server sestavit a spustit:

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

Vytvořte *tsconfig.json* s následujícím obsahem:

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

Vytvořte adresář pro zdrojový kód:

```sh
mkdir src
touch src/index.ts
```

#### Python

Vytvořte soubor *server.py*

```sh
touch server.py
```

#### .NET

Nainstalujte potřebné NuGet balíčky:

```sh
dotnet add package ModelContextProtocol --prerelease
dotnet add package Microsoft.Extensions.Hosting
```

#### Java

Ve Spring Boot projektech v Javě je struktura projektu vytvořena automaticky.

#### Rust

Pro Rust je soubor *src/main.rs* vytvořen automaticky při spuštění `cargo init`. Otevřete ho a smažte výchozí kód.

### -4- Vytvoření serverového kódu

#### TypeScript

Vytvořte soubor *index.ts* a přidejte tento kód:

```typescript
import { McpServer, ResourceTemplate } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";
 
// Vytvořit MCP server
const server = new McpServer({
  name: "Calculator MCP Server",
  version: "1.0.0"
});
```

Nyní máte server, ale ještě nic moc nedělá, opravme to.

#### Python

```python
# server.py
from mcp.server.fastmcp import FastMCP

# Vytvořit MCP server
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

Pro Javu vytvořte základní součásti serveru. Nejprve upravte hlavní aplikační třídu:

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

Vytvořte službu kalkulačky *src/main/java/com/microsoft/mcp/sample/server/service/CalculatorService.java*:

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

**Volitelné součásti pro produkční připravenost:**

Vytvořte startup konfiguraci *src/main/java/com/microsoft/mcp/sample/server/config/StartupConfig.java*:

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

Vytvořte Health Controller *src/main/java/com/microsoft/mcp/sample/server/controller/HealthController.java*:

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

Vytvořte globální obsluhu výjimek *src/main/java/com/microsoft/mcp/sample/server/exception/GlobalExceptionHandler.java*:

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

        // Gettery
        public String getCode() { return code; }
        public String getMessage() { return message; }
    }
}
```

Vytvořte vlastní banner *src/main/resources/banner.txt*:

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

Přidejte následující kód na začátek souboru *src/main.rs*. Tento kód importuje potřebné knihovny a moduly pro MCP server.

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

Server kalkulačky bude jednoduchý, umí sčítat dvě čísla. Vytvořme strukturu, která bude reprezentovat požadavek kalkulačky.

```rust
#[derive(Debug, serde::Deserialize, schemars::JsonSchema)]
pub struct CalculatorRequest {
    pub a: f64,
    pub b: f64,
}
```

Dále vytvořte strukturu, která bude reprezentovat server kalkulačky. Tato struktura bude obsahovat router nástrojů, který se používá k registraci nástrojů.

```rust
#[derive(Debug, Clone)]
pub struct Calculator {
    tool_router: ToolRouter<Self>,
}
```

Nyní můžeme implementovat strukturu `Calculator` pro vytvoření nové instance serveru a implementovat handler serveru pro poskytování informací o serveru.

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

Nakonec implementujeme hlavní funkci pro spuštění serveru. Tato funkce vytvoří instanci struktury `Calculator` a bude ji obsluhovat přes standardní vstup/výstup.

```rust
#[tokio::main]
async fn main() -> Result<(), Box<dyn Error>> {
    let service = Calculator::new().serve(stdio()).await?;
    service.waiting().await?;
    Ok(())
}
```

Server je nyní nastaven k poskytování základních informací o sobě. Následně přidáme nástroj pro sčítání.

### -5- Přidání nástroje a zdroje

Přidejte nástroj a zdroj přidáním následujícího kódu:

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

Váš nástroj přijímá parametry `a` a `b` a spouští funkci, která produkuje odpověď ve formě:

```typescript
{
  contents: [{
    type: "text", content: "some content"
  }]
}
```

Váš zdroj je přístupný přes řetězec "greeting" a bere parametr `name` a vytváří podobnou odpověď jako nástroj:

```typescript
{
  uri: "<href>",
  text: "a text"
}
```

#### Python

```python
# Přidejte nástroj pro sčítání
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


# Přidejte zdroj dynamického pozdravu
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}!"
```

V předchozím kódu jsme:

- Definovali nástroj `add`, který bere parametry `a` a `b`, oba typu integer.
- Vytvořili zdroj s názvem `greeting`, který bere parametr `name`.

#### .NET

Přidejte toto do souboru Program.cs:

```csharp
[McpServerToolType]
public static class CalculatorTool
{
    [McpServerTool, Description("Adds two numbers")]
    public static string Add(int a, int b) => $"Sum {a + b}";
}
```

#### Java

Nástroje již byly vytvořeny v předchozím kroku.

#### Rust

Přidejte nový nástroj uvnitř bloku `impl Calculator`:

```rust
#[tool(description = "Adds a and b")]
async fn add(
    &self,
    Parameters(CalculatorRequest { a, b }): Parameters<CalculatorRequest>,
) -> String {
    (a + b).to_string()
}
```

### -6- Konečný kód

Přidejme poslední kód, který server potřebuje ke spuštění:

#### TypeScript

```typescript
// Začněte přijímat zprávy na stdin a odesílat zprávy na stdout
const transport = new StdioServerTransport();
await server.connect(transport);
```

Zde je celý kód:

```typescript
// index.ts
import { McpServer, ResourceTemplate } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";

// Vytvořit MCP server
const server = new McpServer({
  name: "Calculator MCP Server",
  version: "1.0.0"
});

// Přidat nástroj pro sčítání
server.tool(
  "add",
  { a: z.number(), b: z.number() },
  async ({ a, b }) => ({
    content: [{ type: "text", text: String(a + b) }]
  })
);

// Přidat dynamický zdroj pozdravu
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

// Začít přijímat zprávy na stdin a odesílat zprávy na stdout
const transport = new StdioServerTransport();
server.connect(transport);
```

#### Python

```python
# server.py
from mcp.server.fastmcp import FastMCP

# Vytvořit MCP server
mcp = FastMCP("Demo")


# Přidat nástroj pro sčítání
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


# Přidat dynamický zdroj pozdravu
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}!"

# Hlavní spouštěcí blok - toto je potřeba pro spuštění serveru
if __name__ == "__main__":
    mcp.run()
```

#### .NET

Vytvořte soubor Program.cs s následujícím obsahem:

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

Vaše kompletní hlavní aplikační třída by měla vypadat takto:

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

Konečný kód pro Rust server by měl vypadat takto:

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

### -7- Otestujte server

Spusťte server následujícím příkazem:

#### TypeScript

```sh
npm run build
```

#### Python

```sh
mcp run server.py
```

> Pro použití MCP Inspectoru spusťte `mcp dev server.py`, který automaticky spustí Inspector a poskytne potřebný token proxy relace. Při použití `mcp run server.py` je třeba Inspector spustit ručně a nakonfigurovat připojení.

#### .NET

Ujistěte se, že jste ve složce vašeho projektu:

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

Spusťte následující příkazy pro formátování a spuštění serveru:

```sh
cargo fmt
cargo run
```

### -8- Spuštění pomocí inspectoru

Inspector je skvělý nástroj, který dokáže spustit váš server a umožnit vám s ním interagovat, abyste mohli otestovat jeho funkčnost. Spusťme jej:

> [!NOTE]
> V poli "command" to může vypadat jinak, protože obsahuje příkaz pro spuštění serveru se specifickým runtime.

#### TypeScript

```sh
npx @modelcontextprotocol/inspector node build/index.js
```

nebo přidejte do svého *package.json* řádek `"inspector": "npx @modelcontextprotocol/inspector node build/index.js"` a pak spusťte `npm run inspector`

#### Python

Python využívá Node.js nástroj s názvem inspector. Je možné tento nástroj volat takto:

```sh
mcp dev server.py
```

Nicméně neimplementuje všechny metody dostupné v tomto nástroji, proto se doporučuje spouštět nástroj Node.js přímo takto:

```sh
npx @modelcontextprotocol/inspector mcp run server.py
```

Pokud používáte nástroj nebo IDE, které umožňuje konfigurovat příkazy a argumenty pro spouštění skriptů,
ujistěte se, že máte v poli `Command` nastaveno `python` a jako `Arguments` `server.py`. To zajistí správné spuštění skriptu.

#### .NET

Ujistěte se, že jste ve svém projektovém adresáři:

```sh
cd McpCalculatorServer
npx @modelcontextprotocol/inspector dotnet run
```

#### Java

Ujistěte se, že máte spuštěný server kalkulačky
Poté spusťte inspektora:

```cmd
npx @modelcontextprotocol/inspector
```

V inspektoru webového rozhraní:

1. Vyberte "SSE" jako typ přenosu
2. Nastavte URL na: `http://localhost:8080/sse`
3. Klikněte na "Connect"

![Connect](../../../../translated_images/cs/tool.163d33e3ee307e20.webp)

**Nyní jste připojeni k serveru**
**Sekce testování Java serveru je nyní dokončena**

Další sekce se týká interakce se serverem.

Měli byste vidět následující uživatelské rozhraní:

![Connect](../../../../translated_images/cs/connect.141db0b2bd05f096.webp)

1. Připojte se k serveru kliknutím na tlačítko Connect
  Jakmile se připojíte k serveru, měli byste vidět následující:

  ![Connected](../../../../translated_images/cs/connected.73d1e042c24075d3.webp)

1. Vyberte "Tools" a poté "listTools", měli byste vidět zobrazenou možnost "Add", vyberte "Add" a vyplňte hodnoty parametrů.

  Měli byste vidět následující odpověď, tj. výsledek z nástroje "add":

  ![Result of running add](../../../../translated_images/cs/ran-tool.a5a6ee878c1369ec.webp)

Gratulujeme, podařilo se vám vytvořit a spustit váš první server!

#### Rust

Pro spuštění Rust serveru s MCP Inspector CLI použijte následující příkaz:

```sh
npx @modelcontextprotocol/inspector cargo run --cli --method tools/call --tool-name add --tool-arg a=1 b=2
```

### Oficiální SDK

MCP poskytuje oficiální SDK pro několik jazyků:

- [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk) - Udržováno ve spolupráci s Microsoftem
- [Java SDK](https://github.com/modelcontextprotocol/java-sdk) - Udržováno ve spolupráci se Spring AI
- [TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk) - Oficiální implementace v TypeScriptu
- [Python SDK](https://github.com/modelcontextprotocol/python-sdk) - Oficiální implementace v Pythonu
- [Kotlin SDK](https://github.com/modelcontextprotocol/kotlin-sdk) - Oficiální implementace v Kotlinu
- [Swift SDK](https://github.com/modelcontextprotocol/swift-sdk) - Udržováno ve spolupráci s Loopwork AI
- [Rust SDK](https://github.com/modelcontextprotocol/rust-sdk) - Oficiální implementace v Rustu

## Klíčová shrnutí

- Nastavení vývojového prostředí MCP je jednoduché s SDK specifickými pro jednotlivé jazyky
- Vytváření MCP serverů zahrnuje vytváření a registraci nástrojů s jasnými schématy
- Testování a ladění jsou nezbytné pro spolehlivé implementace MCP

## Ukázky

- [Java Calculator](../samples/java/calculator/README.md)
- [.Net Calculator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Calculator](../samples/javascript/README.md)
- [TypeScript Calculator](../samples/typescript/README.md)
- [Python Calculator](../../../../03-GettingStarted/samples/python)
- [Rust Calculator](../../../../03-GettingStarted/samples/rust)

## Zadání

Vytvořte jednoduchý MCP server s nástrojem podle vašeho výběru:

1. Implementujte nástroj ve svém preferovaném jazyce (.NET, Java, Python, TypeScript nebo Rust).
2. Definujte vstupní parametry a návratové hodnoty.
3. Spusťte inspektor, abyste zajistili, že server funguje správně.
4. Otestujte implementaci s různými vstupy.

## Řešení

[Řešení](./solution/README.md)

## Další zdroje

- [Vytváření agentů pomocí Model Context Protocol na Azure](https://learn.microsoft.com/azure/developer/ai/intro-agents-mcp)
- [Vzdálené MCP s Azure Container Apps (Node.js/TypeScript/JavaScript)](https://learn.microsoft.com/samples/azure-samples/mcp-container-ts/mcp-container-ts/)
- [.NET OpenAI MCP Agent](https://learn.microsoft.com/samples/azure-samples/openai-mcp-agent-dotnet/openai-mcp-agent-dotnet/)

## Co dál

Dále: [Začínáme s MCP klienty](../02-client/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Prohlášení o vyloučení odpovědnosti**:
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). I když se snažíme o přesnost, uvědomte si, že automatické překlady mohou obsahovat chyby nebo nepřesnosti. Originální dokument v jeho původním jazyce by měl být považován za autoritativní zdroj. Pro kritické informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoli nedorozumění nebo chybná vykládání vyplývající z použití tohoto překladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->