<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8fdac7600a5f4722643d0f14e15ac259",
  "translation_date": "2025-12-11T08:23:36+00:00",
  "source_file": "03-GettingStarted/01-first-server/README.md",
  "language_code": "sl"
}
-->
# Začetek z MCP

Dobrodošli pri vaših prvih korakih z Model Context Protocol (MCP)! Ne glede na to, ali ste novi pri MCP ali želite poglobiti svoje razumevanje, vas ta vodič popelje skozi osnovni postopek nastavitve in razvoja. Spoznali boste, kako MCP omogoča nemoteno integracijo med AI modeli in aplikacijami ter se naučili, kako hitro pripraviti svoje okolje za gradnjo in testiranje rešitev, ki temeljijo na MCP.

> TLDR; Če gradite AI aplikacije, veste, da lahko svojemu LLM (velikemu jezikovnemu modelu) dodate orodja in druge vire, da postane LLM bolj poučen. Če pa ta orodja in vire postavite na strežnik, lahko aplikacija in zmogljivosti strežnika uporabljajo kateri koli odjemalec z ali brez LLM.

## Pregled

Ta lekcija ponuja praktična navodila za nastavitev MCP okolij in gradnjo vaših prvih MCP aplikacij. Naučili se boste, kako nastaviti potrebna orodja in ogrodja, zgraditi osnovne MCP strežnike, ustvariti gostiteljske aplikacije in testirati vaše implementacije.

Model Context Protocol (MCP) je odprt protokol, ki standardizira, kako aplikacije zagotavljajo kontekst LLM-jem. MCP si lahko predstavljate kot USB-C priključek za AI aplikacije - zagotavlja standardiziran način povezovanja AI modelov z različnimi viri podatkov in orodji.

## Cilji učenja

Do konca te lekcije boste znali:

- Nastaviti razvojna okolja za MCP v C#, Javi, Pythonu, TypeScriptu in Rustu
- Zgraditi in namestiti osnovne MCP strežnike s prilagojenimi funkcijami (viri, pozivi in orodja)
- Ustvariti gostiteljske aplikacije, ki se povezujejo z MCP strežniki
- Testirati in odpravljati napake v implementacijah MCP

## Nastavitev vašega MCP okolja

Preden začnete delati z MCP, je pomembno pripraviti razvojno okolje in razumeti osnovni potek dela. Ta razdelek vas bo vodil skozi začetne korake nastavitve, da zagotovite nemoten začetek z MCP.

### Predpogoji

Preden se lotite razvoja MCP, poskrbite, da imate:

- **Razvojno okolje**: Za izbrani programski jezik (C#, Java, Python, TypeScript ali Rust)
- **IDE/Urejevalnik**: Visual Studio, Visual Studio Code, IntelliJ, Eclipse, PyCharm ali kateri koli sodoben urejevalnik kode
- **Upravitelji paketov**: NuGet, Maven/Gradle, pip, npm/yarn ali Cargo
- **API ključi**: Za vse AI storitve, ki jih nameravate uporabljati v gostiteljskih aplikacijah

## Osnovna struktura MCP strežnika

MCP strežnik običajno vključuje:

- **Konfiguracija strežnika**: Nastavitev vrat, avtentikacije in drugih nastavitev
- **Viri**: Podatki in kontekst, ki so na voljo LLM-jem
- **Orodja**: Funkcionalnosti, ki jih modeli lahko kličejo
- **Pozivi**: Predloge za generiranje ali strukturiranje besedila

Tukaj je poenostavljen primer v TypeScriptu:

```typescript
import { McpServer, ResourceTemplate } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";

// Ustvari MCP strežnik
const server = new McpServer({
  name: "Demo",
  version: "1.0.0"
});

// Dodaj orodje za seštevanje
server.tool("add",
  { a: z.number(), b: z.number() },
  async ({ a, b }) => ({
    content: [{ type: "text", text: String(a + b) }]
  })
);

// Dodaj dinamični vir pozdravov
server.resource(
  "file",
  // Parameter 'list' nadzoruje, kako vir navaja razpoložljive datoteke. Nastavitev na undefined onemogoči seznam za ta vir.
  new ResourceTemplate("file://{path}", { list: undefined }),
  async (uri, { path }) => ({
    contents: [{
      uri: uri.href,
      text: `File, ${path}!`
    }]
  })
);

// Dodaj datotečni vir, ki bere vsebino datoteke
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

// Začni prejemati sporočila na stdin in pošiljati sporočila na stdout
const transport = new StdioServerTransport();
await server.connect(transport);
```

V zgornji kodi smo:

- Uvozili potrebne razrede iz MCP TypeScript SDK.
- Ustvarili in konfigurirali novo instanco MCP strežnika.
- Registrirali prilagojeno orodje (`calculator`) s funkcijo obdelave.
- Zagnali strežnik, da posluša dohodne MCP zahteve.

## Testiranje in odpravljanje napak

Preden začnete testirati svoj MCP strežnik, je pomembno razumeti razpoložljiva orodja in najboljše prakse za odpravljanje napak. Učinkovito testiranje zagotavlja, da se strežnik obnaša kot pričakovano, in vam pomaga hitro prepoznati ter odpraviti težave. Naslednji razdelek opisuje priporočene pristope za preverjanje vaše MCP implementacije.

MCP ponuja orodja, ki vam pomagajo testirati in odpravljati napake na vaših strežnikih:

- **Orodje Inspector**, ta grafični vmesnik vam omogoča povezavo s strežnikom in testiranje vaših orodij, pozivov in virov.
- **curl**, lahko se tudi povežete s strežnikom z ukazno vrstico, kot je curl, ali drugimi odjemalci, ki lahko ustvarjajo in izvajajo HTTP ukaze.

### Uporaba MCP Inspectorja

[MCP Inspector](https://github.com/modelcontextprotocol/inspector) je vizualno orodje za testiranje, ki vam pomaga:

1. **Odkriti zmogljivosti strežnika**: Samodejno zaznati razpoložljive vire, orodja in pozive
2. **Testirati izvajanje orodij**: Preizkusiti različne parametre in videti odzive v realnem času
3. **Ogledati metapodatke strežnika**: Pregledati informacije o strežniku, sheme in konfiguracije

```bash
# primer TypeScript, namestitev in zagon MCP Inspectorja
npx @modelcontextprotocol/inspector node build/index.js
```

Ko zaženete zgornje ukaze, bo MCP Inspector zagnal lokalni spletni vmesnik v vašem brskalniku. Pričakujete lahko nadzorno ploščo, ki prikazuje vaše registrirane MCP strežnike, njihova razpoložljiva orodja, vire in pozive. Vmesnik omogoča interaktivno testiranje izvajanja orodij, pregled metapodatkov strežnika in ogled odzivov v realnem času, kar olajša preverjanje in odpravljanje napak v vaših MCP strežniških implementacijah.

Tukaj je posnetek zaslona, kako lahko izgleda:

![MCP Inspector server connection](../../../../translated_images/connected.73d1e042c24075d386cacdd4ee7cd748c16364c277d814e646ff2f7b5eefde85.sl.png)

## Pogoste težave pri nastavitvi in rešitve

| Težava | Možna rešitev |
|-------|-------------------|
| Povezava zavrnjena | Preverite, ali strežnik teče in ali so vrata pravilna |
| Napake pri izvajanju orodij | Preglejte preverjanje parametrov in obravnavo napak |
| Napake avtentikacije | Preverite API ključe in dovoljenja |
| Napake preverjanja sheme | Zagotovite, da parametri ustrezajo definirani shemi |
| Strežnik se ne zažene | Preverite konflikte vrat ali manjkajoče odvisnosti |
| Napake CORS | Konfigurirajte ustrezne CORS glave za zahteve iz drugih virov |
| Težave z avtentikacijo | Preverite veljavnost žetona in dovoljenja |

## Lokalni razvoj

Za lokalni razvoj in testiranje lahko MCP strežnike zaženete neposredno na svojem računalniku:

1. **Zaženite strežniški proces**: Zaženite svojo MCP strežniško aplikacijo
2. **Konfigurirajte omrežje**: Poskrbite, da je strežnik dostopen na pričakovanih vratih
3. **Povežite odjemalce**: Uporabite lokalne povezovalne URL-je, kot je `http://localhost:3000`

```bash
# Primer: Zagon TypeScript MCP strežnika lokalno
npm run start
# Strežnik teče na http://localhost:3000
```

## Gradnja vašega prvega MCP strežnika

V prejšnji lekciji smo obravnavali [osnovne koncepte](/01-CoreConcepts/README.md), zdaj pa je čas, da to znanje uporabimo v praksi.

### Kaj strežnik lahko počne

Preden začnemo pisati kodo, si le osvežimo, kaj strežnik lahko počne:

MCP strežnik lahko na primer:

- Dostopa do lokalnih datotek in baz podatkov
- Povezuje se z oddaljenimi API-ji
- Izvaja izračune
- Integrira z drugimi orodji in storitvami
- Zagotavlja uporabniški vmesnik za interakcijo

Odlično, zdaj ko vemo, kaj lahko naredimo, začnimo s kodiranjem.

## Vaja: Ustvarjanje strežnika

Za ustvarjanje strežnika morate slediti tem korakom:

- Namestite MCP SDK.
- Ustvarite projekt in nastavite strukturo projekta.
- Napišite kodo strežnika.
- Testirajte strežnik.

### -1- Ustvarite projekt

#### TypeScript

```sh
# Ustvari imenik projekta in inicializiraj npm projekt
mkdir calculator-server
cd calculator-server
npm init -y
```

#### Python

```sh
# Ustvari imenik projekta
mkdir calculator-server
cd calculator-server
# Odpri mapo v Visual Studio Code - preskoči to, če uporabljaš drug IDE
code .
```

#### .NET

```sh
dotnet new console -n McpCalculatorServer
cd McpCalculatorServer
```

#### Java

Za Javo ustvarite Spring Boot projekt:

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

Razpakirajte zip datoteko:

```bash
unzip calculator-server.zip -d calculator-server
cd calculator-server
# neobvezno odstranite neuporabljeni test
rm -rf src/test/java
```

Dodajte naslednjo celotno konfiguracijo v vašo datoteko *pom.xml*:

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

### -2- Dodajte odvisnosti

Ko imate ustvarjen projekt, dodajte naslednje odvisnosti:

#### TypeScript

```sh
# Če še ni nameščen, namestite TypeScript globalno
npm install typescript -g

# Namestite MCP SDK in Zod za preverjanje shem
npm install @modelcontextprotocol/sdk zod
npm install -D @types/node typescript
```

#### Python

```sh
# Ustvari virtualno okolje in namesti odvisnosti
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

### -3- Ustvarite projektne datoteke

#### TypeScript

Odprite datoteko *package.json* in zamenjajte vsebino z naslednjo, da zagotovite, da lahko zgradite in zaženete strežnik:

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

Ustvarite *tsconfig.json* z naslednjo vsebino:

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

Ustvarite imenik za vašo izvorno kodo:

```sh
mkdir src
touch src/index.ts
```

#### Python

Ustvarite datoteko *server.py*

```sh
touch server.py
```

#### .NET

Namestite zahtevane NuGet pakete:

```sh
dotnet add package ModelContextProtocol --prerelease
dotnet add package Microsoft.Extensions.Hosting
```

#### Java

Za Java Spring Boot projekte je struktura projekta ustvarjena samodejno.

#### Rust

Za Rust je datoteka *src/main.rs* ustvarjena privzeto, ko zaženete `cargo init`. Odprite datoteko in izbrišite privzeto kodo.

### -4- Ustvarite kodo strežnika

#### TypeScript

Ustvarite datoteko *index.ts* in dodajte naslednjo kodo:

```typescript
import { McpServer, ResourceTemplate } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";
 
// Ustvari MCP strežnik
const server = new McpServer({
  name: "Calculator MCP Server",
  version: "1.0.0"
});
```

Zdaj imate strežnik, vendar ne počne veliko, to bomo popravili.

#### Python

```python
# server.py
from mcp.server.fastmcp import FastMCP

# Ustvari MCP strežnik
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

Za Javo ustvarite osnovne strežniške komponente. Najprej spremenite glavno aplikacijsko razredno datoteko:

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

Ustvarite storitev kalkulatorja *src/main/java/com/microsoft/mcp/sample/server/service/CalculatorService.java*:

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

**Neobvezne komponente za produkcijsko pripravljeno storitev:**

Ustvarite konfiguracijo zagona *src/main/java/com/microsoft/mcp/sample/server/config/StartupConfig.java*:

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

Ustvarite kontroler zdravja *src/main/java/com/microsoft/mcp/sample/server/controller/HealthController.java*:

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

Ustvarite upravljalnik izjem *src/main/java/com/microsoft/mcp/sample/server/exception/GlobalExceptionHandler.java*:

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

        // Pridobivalci
        public String getCode() { return code; }
        public String getMessage() { return message; }
    }
}
```

Ustvarite prilagojeni banner *src/main/resources/banner.txt*:

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

Dodajte naslednjo kodo na vrh datoteke *src/main.rs*. Ta uvozi potrebne knjižnice in module za vaš MCP strežnik.

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

Kalkulator strežnik bo preprost, ki lahko sešteje dve števili. Ustvarimo strukturo za predstavitev zahteve kalkulatorja.

```rust
#[derive(Debug, serde::Deserialize, schemars::JsonSchema)]
pub struct CalculatorRequest {
    pub a: f64,
    pub b: f64,
}
```

Nato ustvarite strukturo za predstavitev kalkulator strežnika. Ta struktura bo vsebovala usmerjevalnik orodij, ki se uporablja za registracijo orodij.

```rust
#[derive(Debug, Clone)]
pub struct Calculator {
    tool_router: ToolRouter<Self>,
}
```

Zdaj lahko implementiramo strukturo `Calculator`, da ustvarimo novo instanco strežnika in implementiramo strežniški upravljalnik za zagotavljanje informacij o strežniku.

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

Nazadnje moramo implementirati glavno funkcijo za zagon strežnika. Ta funkcija bo ustvarila instanco strukture `Calculator` in jo postregla preko standardnega vhoda/izhoda.

```rust
#[tokio::main]
async fn main() -> Result<(), Box<dyn Error>> {
    let service = Calculator::new().serve(stdio()).await?;
    service.waiting().await?;
    Ok(())
}
```

Strežnik je zdaj nastavljen za zagotavljanje osnovnih informacij o sebi. Naslednje bomo dodali orodje za izvajanje seštevanja.

### -5- Dodajanje orodja in vira

Dodajte orodje in vir z dodajanjem naslednje kode:

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

Vaše orodje sprejema parametra `a` in `b` ter izvaja funkcijo, ki ustvari odgovor v obliki:

```typescript
{
  contents: [{
    type: "text", content: "some content"
  }]
}
```

Vaš vir je dostopen preko niza "greeting" in sprejema parameter `name` ter ustvari podoben odgovor kot orodje:

```typescript
{
  uri: "<href>",
  text: "a text"
}
```

#### Python

```python
# Dodajte orodje za seštevanje
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


# Dodajte dinamičen vir pozdravov
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}!"
```

V zgornji kodi smo:

- Definirali orodje `add`, ki sprejema parametra `a` in `b`, oba cela števila.
- Ustvarili vir z imenom `greeting`, ki sprejema parameter `name`.

#### .NET

Dodajte to v vašo datoteko Program.cs:

```csharp
[McpServerToolType]
public static class CalculatorTool
{
    [McpServerTool, Description("Adds two numbers")]
    public static string Add(int a, int b) => $"Sum {a + b}";
}
```

#### Java

Orodja so bila že ustvarjena v prejšnjem koraku.

#### Rust

Dodajte novo orodje znotraj bloka `impl Calculator`:

```rust
#[tool(description = "Adds a and b")]
async fn add(
    &self,
    Parameters(CalculatorRequest { a, b }): Parameters<CalculatorRequest>,
) -> String {
    (a + b).to_string()
}
```

### -6- Končna koda

Dodajmo zadnjo kodo, ki jo potrebujemo, da se strežnik lahko zažene:

#### TypeScript

```typescript
// Začni prejemati sporočila na stdin in pošiljati sporočila na stdout
const transport = new StdioServerTransport();
await server.connect(transport);
```

Tukaj je celotna koda:

```typescript
// index.ts
import { McpServer, ResourceTemplate } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";

// Ustvari MCP strežnik
const server = new McpServer({
  name: "Calculator MCP Server",
  version: "1.0.0"
});

// Dodaj orodje za seštevanje
server.tool(
  "add",
  { a: z.number(), b: z.number() },
  async ({ a, b }) => ({
    content: [{ type: "text", text: String(a + b) }]
  })
);

// Dodaj dinamični vir pozdravov
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

// Začni prejemati sporočila na stdin in pošiljati sporočila na stdout
const transport = new StdioServerTransport();
server.connect(transport);
```

#### Python

```python
# server.py
from mcp.server.fastmcp import FastMCP

# Ustvari MCP strežnik
mcp = FastMCP("Demo")


# Dodaj orodje za seštevanje
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


# Dodaj dinamični vir pozdravov
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}!"

# Glavni blok izvajanja - to je potrebno za zagon strežnika
if __name__ == "__main__":
    mcp.run()
```

#### .NET

Ustvarite datoteko Program.cs z naslednjo vsebino:

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

Vaša popolna glavna aplikacijska razrednica naj izgleda tako:

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

Končna koda za Rust strežnik naj izgleda tako:

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

### -7- Testirajte strežnik

Zaženite strežnik z naslednjim ukazom:

#### TypeScript

```sh
npm run build
```

#### Python

```sh
mcp run server.py
```

> Za uporabo MCP Inspectorja uporabite `mcp dev server.py`, ki samodejno zažene Inspector in zagotovi zahtevan žeton seje proxyja. Če uporabljate `mcp run server.py`, boste morali Inspector ročno zagnati in konfigurirati povezavo.

#### .NET

Prepričajte se, da ste v svojem projektni m imeniku:

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

Zaženite naslednje ukaze za formatiranje in zagon strežnika:

```sh
cargo fmt
cargo run
```

### -8- Zagon z uporabo inspectorja

Inspector je odlično orodje, ki lahko zažene vaš strežnik in vam omogoča interakcijo z njim, da lahko testirate, ali deluje. Zaženimo ga:

> [!NOTE]
> lahko izgleda drugače v polju "command", saj vsebuje ukaz za zagon strežnika z vašim specifičnim runtime/

#### TypeScript

```sh
npx @modelcontextprotocol/inspector node build/index.js
```

ali ga dodajte v vaš *package.json* tako: `"inspector": "npx @modelcontextprotocol/inspector node build/index.js"` in nato zaženite `npm run inspector`

#### Python

Python ovije Node.js orodje imenovano inspector. Možno je poklicati to orodje tako:

```sh
mcp dev server.py
```

Vendar ne implementira vseh metod, ki so na voljo na orodju, zato je priporočljivo, da zaženete Node.js orodje neposredno, kot spodaj:

```sh
npx @modelcontextprotocol/inspector mcp run server.py
```

Če uporabljate orodje ali IDE, ki omogoča konfiguracijo ukazov in argumentov za zagon skript,
poskrbite, da nastavite `python` v polju `Command` in `server.py` kot `Arguments`. To zagotavlja pravilno delovanje skripte.

#### .NET

Prepričajte se, da ste v svoji projektni mapi:

```sh
cd McpCalculatorServer
npx @modelcontextprotocol/inspector dotnet run
```

#### Java

Prepričajte se, da vaš kalkulator strežnik deluje
Nato zaženite inšpektor:

```cmd
npx @modelcontextprotocol/inspector
```

V spletni vmesnik inšpektorja:

1. Izberite "SSE" kot tip prenosa
2. Nastavite URL na: `http://localhost:8080/sse`
3. Kliknite "Connect"

![Connect](../../../../translated_images/tool.163d33e3ee307e209ef146d8f85060d2f7e83e9f59b3b1699a77204ae0454ad2.sl.png)

**Zdaj ste povezani s strežnikom**
**Oddelek za testiranje Java strežnika je zdaj zaključen**

Naslednji oddelek govori o interakciji s strežnikom.

Videti bi morali naslednji uporabniški vmesnik:

![Connect](../../../../translated_images/connect.141db0b2bd05f096fb1dd91273771fd8b2469d6507656c3b0c9df4b3c5473929.sl.png)

1. Povežite se s strežnikom s klikom na gumb Connect
  Ko se povežete s strežnikom, bi morali zdaj videti naslednje:

  ![Connected](../../../../translated_images/connected.73d1e042c24075d386cacdd4ee7cd748c16364c277d814e646ff2f7b5eefde85.sl.png)

1. Izberite "Tools" in "listTools", morali bi videti "Add", izberite "Add" in izpolnite vrednosti parametrov.

  Videli boste naslednji odgovor, tj. rezultat orodja "add":

  ![Result of running add](../../../../translated_images/ran-tool.a5a6ee878c1369ec1e379b81053395252a441799dbf23416c36ddf288faf8249.sl.png)

Čestitke, uspelo vam je ustvariti in zagnati svoj prvi strežnik!

#### Rust

Za zagon Rust strežnika z MCP Inspector CLI uporabite naslednji ukaz:

```sh
npx @modelcontextprotocol/inspector cargo run --cli --method tools/call --tool-name add --tool-arg a=1 b=2
```

### Uradni SDK-ji

MCP ponuja uradne SDK-je za več jezikov:

- [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk) - Vzdrževan v sodelovanju z Microsoftom
- [Java SDK](https://github.com/modelcontextprotocol/java-sdk) - Vzdrževan v sodelovanju s Spring AI
- [TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk) - Uradna implementacija za TypeScript
- [Python SDK](https://github.com/modelcontextprotocol/python-sdk) - Uradna implementacija za Python
- [Kotlin SDK](https://github.com/modelcontextprotocol/kotlin-sdk) - Uradna implementacija za Kotlin
- [Swift SDK](https://github.com/modelcontextprotocol/swift-sdk) - Vzdrževan v sodelovanju z Loopwork AI
- [Rust SDK](https://github.com/modelcontextprotocol/rust-sdk) - Uradna implementacija za Rust

## Ključne ugotovitve

- Nastavitev MCP razvojnega okolja je enostavna z jezikovno specifičnimi SDK-ji
- Gradnja MCP strežnikov vključuje ustvarjanje in registracijo orodij z jasnimi shemami
- Testiranje in odpravljanje napak sta ključna za zanesljive MCP implementacije

## Vzorci

- [Java Calculator](../samples/java/calculator/README.md)
- [.Net Calculator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Calculator](../samples/javascript/README.md)
- [TypeScript Calculator](../samples/typescript/README.md)
- [Python Calculator](../../../../03-GettingStarted/samples/python)
- [Rust Calculator](../../../../03-GettingStarted/samples/rust)

## Naloga

Ustvarite preprost MCP strežnik z orodjem po vaši izbiri:

1. Implementirajte orodje v vašem izbranem jeziku (.NET, Java, Python, TypeScript ali Rust).
2. Določite vhodne parametre in vrednosti za vrnitev.
3. Zaženite inšpektor, da zagotovite, da strežnik deluje kot je predvideno.
4. Preizkusite implementacijo z različnimi vnosi.

## Rešitev

[Rešitev](./solution/README.md)

## Dodatni viri

- [Gradnja agentov z uporabo Model Context Protocol na Azure](https://learn.microsoft.com/azure/developer/ai/intro-agents-mcp)
- [Oddaljeni MCP z Azure Container Apps (Node.js/TypeScript/JavaScript)](https://learn.microsoft.com/samples/azure-samples/mcp-container-ts/mcp-container-ts/)
- [.NET OpenAI MCP Agent](https://learn.microsoft.com/samples/azure-samples/openai-mcp-agent-dotnet/openai-mcp-agent-dotnet/)

## Kaj sledi

Naslednje: [Začetek z MCP odjemalci](../02-client/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo storitve za prevajanje z umetno inteligenco [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas opozarjamo, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku velja za avtoritativni vir. Za ključne informacije priporočamo strokovni človeški prevod. Za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda, ne odgovarjamo.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->