<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8fdac7600a5f4722643d0f14e15ac259",
  "translation_date": "2025-12-11T07:39:52+00:00",
  "source_file": "03-GettingStarted/01-first-server/README.md",
  "language_code": "hu"
}
-->
# MCP használatának megkezdése

Üdvözlünk az első lépéseidnél a Model Context Protocol (MCP) használatában! Akár új vagy az MCP-ben, akár mélyíteni szeretnéd a tudásodat, ez az útmutató végigvezet a lényeges beállítási és fejlesztési folyamatokon. Megtudhatod, hogyan teszi lehetővé az MCP az AI modellek és alkalmazások közötti zökkenőmentes integrációt, és megtanulhatod, hogyan készítheted elő gyorsan a környezeted MCP-alapú megoldások építéséhez és teszteléséhez.

> Összefoglaló; Ha AI alkalmazásokat fejlesztesz, tudod, hogy hozzáadhatsz eszközöket és egyéb erőforrásokat a nagy nyelvi modelledhez (LLM), hogy az tudásgazdagabb legyen. Azonban ha ezeket az eszközöket és erőforrásokat egy szerveren helyezed el, az alkalmazás és a szerver képességei bármely kliens által használhatók LLM-mel vagy anélkül.

## Áttekintés

Ez a lecke gyakorlati útmutatást nyújt az MCP környezetek beállításához és az első MCP alkalmazások elkészítéséhez. Megtanulod, hogyan állítsd be a szükséges eszközöket és keretrendszereket, hogyan építs alap MCP szervereket, készíts hoszt alkalmazásokat, és teszteld a megvalósításaidat.

A Model Context Protocol (MCP) egy nyílt protokoll, amely szabványosítja, hogyan biztosítanak az alkalmazások kontextust a nagy nyelvi modelleknek. Gondolj az MCP-re úgy, mint egy USB-C portra az AI alkalmazások számára – szabványos módot ad arra, hogy AI modelleket különböző adatforrásokhoz és eszközökhöz csatlakoztass.

## Tanulási célok

A lecke végére képes leszel:

- MCP fejlesztői környezetek beállítása C#, Java, Python, TypeScript és Rust nyelveken
- Alap MCP szerverek építése és telepítése egyedi funkciókkal (erőforrások, promptok és eszközök)
- Hoszt alkalmazások létrehozása, amelyek MCP szerverekhez kapcsolódnak
- MCP megvalósítások tesztelése és hibakeresése

## MCP környezeted beállítása

Mielőtt elkezdenéd az MCP-vel való munkát, fontos előkészíteni a fejlesztői környezetet és megérteni az alapvető munkafolyamatot. Ez a rész végigvezet az első beállítási lépéseken, hogy zökkenőmentesen indulhass az MCP-vel.

### Előfeltételek

Mielőtt belevágnál az MCP fejlesztésbe, győződj meg róla, hogy rendelkezel:

- **Fejlesztői környezet**: a választott nyelvhez (C#, Java, Python, TypeScript vagy Rust)
- **IDE/Szerkesztő**: Visual Studio, Visual Studio Code, IntelliJ, Eclipse, PyCharm vagy bármely modern kódszerkesztő
- **Csomagkezelők**: NuGet, Maven/Gradle, pip, npm/yarn vagy Cargo
- **API kulcsok**: bármely AI szolgáltatáshoz, amelyet a hoszt alkalmazásaidban használni tervezel

## Alap MCP szerver felépítés

Egy MCP szerver általában tartalmazza:

- **Szerver konfiguráció**: port, hitelesítés és egyéb beállítások
- **Erőforrások**: adatok és kontextus, amelyeket a nagy nyelvi modellek elérhetnek
- **Eszközök**: funkciók, amelyeket a modellek meghívhatnak
- **Promptok**: sablonok szöveg generálásához vagy strukturálásához

Íme egy egyszerűsített példa TypeScript-ben:

```typescript
import { McpServer, ResourceTemplate } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";

// Hozzon létre egy MCP szervert
const server = new McpServer({
  name: "Demo",
  version: "1.0.0"
});

// Adjon hozzá egy összeadási eszközt
server.tool("add",
  { a: z.number(), b: z.number() },
  async ({ a, b }) => ({
    content: [{ type: "text", text: String(a + b) }]
  })
);

// Adjon hozzá egy dinamikus üdvözlő erőforrást
server.resource(
  "file",
  // A 'list' paraméter szabályozza, hogyan listázza az erőforrás a rendelkezésre álló fájlokat. Ha undefined értékre állítjuk, az letiltja a listázást ennél az erőforrásnál.
  new ResourceTemplate("file://{path}", { list: undefined }),
  async (uri, { path }) => ({
    contents: [{
      uri: uri.href,
      text: `File, ${path}!`
    }]
  })
);

// Adjon hozzá egy fájl erőforrást, amely beolvassa a fájl tartalmát
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

// Kezdje el fogadni az üzeneteket a stdin-en és küldeni azokat a stdout-ra
const transport = new StdioServerTransport();
await server.connect(transport);
```

A fenti kódban:

- Importáljuk a szükséges osztályokat az MCP TypeScript SDK-ból.
- Létrehozunk és konfigurálunk egy új MCP szerver példányt.
- Regisztrálunk egy egyedi eszközt (`calculator`) egy kezelő függvénnyel.
- Elindítjuk a szervert, hogy figyelje a bejövő MCP kéréseket.

## Tesztelés és hibakeresés

Mielőtt elkezdenéd tesztelni az MCP szerveredet, fontos megérteni a rendelkezésre álló eszközöket és a hibakeresés legjobb gyakorlatait. A hatékony tesztelés biztosítja, hogy a szerver a várakozásoknak megfelelően működjön, és segít gyorsan azonosítani és megoldani a problémákat. A következő rész ajánlott megközelítéseket vázol fel az MCP megvalósításod érvényesítéséhez.

Az MCP eszközöket biztosít a szerverek teszteléséhez és hibakereséséhez:

- **Inspector eszköz**, ez a grafikus felület lehetővé teszi, hogy csatlakozz a szerveredhez, és teszteld az eszközeidet, promptjaidat és erőforrásaidat.
- **curl**, parancssori eszközzel is csatlakozhatsz a szerverhez, mint például a curl vagy más kliens, amelyek HTTP parancsokat tudnak létrehozni és futtatni.

### MCP Inspector használata

Az [MCP Inspector](https://github.com/modelcontextprotocol/inspector) egy vizuális tesztelő eszköz, amely segít:

1. **Szerver képességek felfedezése**: automatikusan felismeri az elérhető erőforrásokat, eszközöket és promptokat
2. **Eszköz végrehajtás tesztelése**: különböző paraméterek kipróbálása és válaszok valós idejű megtekintése
3. **Szerver metaadatok megtekintése**: szerver információk, sémák és konfigurációk vizsgálata

```bash
# Példa TypeScriptből, az MCP Inspector telepítése és futtatása
npx @modelcontextprotocol/inspector node build/index.js
```

A fenti parancsok futtatásakor az MCP Inspector elindít egy helyi webes felületet a böngésződben. Egy irányítópultot fogsz látni, amely megjeleníti a regisztrált MCP szervereidet, azok elérhető eszközeit, erőforrásait és promptjait. A felület lehetővé teszi az eszközök interaktív tesztelését, a szerver metaadatainak megtekintését és a valós idejű válaszok megjelenítését, megkönnyítve az MCP szerver megvalósítások érvényesítését és hibakeresését.

Íme egy képernyőkép arról, hogyan nézhet ki:

![MCP Inspector szerverkapcsolat](../../../../translated_images/connected.73d1e042c24075d386cacdd4ee7cd748c16364c277d814e646ff2f7b5eefde85.hu.png)

## Gyakori beállítási problémák és megoldások

| Probléma | Lehetséges megoldás |
|----------|---------------------|
| Kapcsolat megtagadva | Ellenőrizd, hogy a szerver fut-e és a port helyes-e |
| Eszköz végrehajtási hibák | Ellenőrizd a paraméterek érvényesítését és a hibakezelést |
| Hitelesítési hibák | Ellenőrizd az API kulcsokat és jogosultságokat |
| Séma érvényesítési hibák | Győződj meg róla, hogy a paraméterek megfelelnek a definiált sémának |
| Szerver nem indul | Ellenőrizd a portütközéseket vagy hiányzó függőségeket |
| CORS hibák | Állíts be megfelelő CORS fejléceket a kereszt-eredetű kérésekhez |
| Hitelesítési problémák | Ellenőrizd a token érvényességét és jogosultságait |

## Helyi fejlesztés

Helyi fejlesztéshez és teszteléshez közvetlenül a gépeden futtathatod az MCP szervereket:

1. **Indítsd el a szerver folyamatot**: futtasd az MCP szerver alkalmazásodat
2. **Hálózat konfigurálása**: győződj meg róla, hogy a szerver elérhető a várt porton
3. **Csatlakoztasd a klienseket**: használj helyi kapcsolati URL-eket, például `http://localhost:3000`

```bash
# Példa: Egy TypeScript MCP szerver futtatása helyben
npm run start
# A szerver fut a http://localhost:3000 címen
```

## Az első MCP szervered építése

Korábban már áttekintettük a [Core concepts](/01-CoreConcepts/README.md) témakört, most ideje alkalmazni a tudást.

### Mit tud egy szerver

Mielőtt kódolni kezdenénk, emlékezzünk rá, mit tud egy szerver:

Egy MCP szerver például képes:

- Hozzáférni helyi fájlokhoz és adatbázisokhoz
- Csatlakozni távoli API-khoz
- Számításokat végezni
- Integrálódni más eszközökkel és szolgáltatásokkal
- Felhasználói felületet biztosítani az interakcióhoz

Remek, most, hogy tudjuk, mit tehet, kezdjünk el kódolni.

## Gyakorlat: Szerver létrehozása

A szerver létrehozásához kövesd az alábbi lépéseket:

- Telepítsd az MCP SDK-t.
- Hozz létre egy projektet és állítsd be a projekt struktúráját.
- Írd meg a szerver kódját.
- Teszteld a szervert.

### -1- Projekt létrehozása

#### TypeScript

```sh
# Hozd létre a projekt könyvtárat és inicializáld az npm projektet
mkdir calculator-server
cd calculator-server
npm init -y
```

#### Python

```sh
# Projekt könyvtár létrehozása
mkdir calculator-server
cd calculator-server
# Nyisd meg a mappát a Visual Studio Code-ban - Ezt hagyd ki, ha más IDE-t használsz
code .
```

#### .NET

```sh
dotnet new console -n McpCalculatorServer
cd McpCalculatorServer
```

#### Java

Java esetén hozz létre egy Spring Boot projektet:

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

Csomagold ki a zip fájlt:

```bash
unzip calculator-server.zip -d calculator-server
cd calculator-server
# opcionális, távolítsa el a nem használt tesztet
rm -rf src/test/java
```

Add hozzá a következő teljes konfigurációt a *pom.xml* fájlodhoz:

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

### -2- Függőségek hozzáadása

Most, hogy létrehoztad a projektet, adjuk hozzá a függőségeket:

#### TypeScript

```sh
# Ha még nincs telepítve, telepítse globálisan a TypeScriptet
npm install typescript -g

# Telepítse az MCP SDK-t és a Zod-ot sémavalidációhoz
npm install @modelcontextprotocol/sdk zod
npm install -D @types/node typescript
```

#### Python

```sh
# Hozz létre egy virtuális környezetet és telepítsd a függőségeket
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

### -3- Projektfájlok létrehozása

#### TypeScript

Nyisd meg a *package.json* fájlt, és cseréld le a tartalmát az alábbiakra, hogy biztosan tudj szervert építeni és futtatni:

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

Hozz létre egy *tsconfig.json* fájlt az alábbi tartalommal:

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

Hozz létre egy könyvtárat a forráskódodnak:

```sh
mkdir src
touch src/index.ts
```

#### Python

Hozz létre egy *server.py* fájlt

```sh
touch server.py
```

#### .NET

Telepítsd a szükséges NuGet csomagokat:

```sh
dotnet add package ModelContextProtocol --prerelease
dotnet add package Microsoft.Extensions.Hosting
```

#### Java

Java Spring Boot projektek esetén a projekt struktúra automatikusan létrejön.

#### Rust

Rust esetén a *src/main.rs* fájl alapértelmezés szerint létrejön a `cargo init` futtatásakor. Nyisd meg a fájlt és töröld az alapértelmezett kódot.

### -4- Szerverkód létrehozása

#### TypeScript

Hozz létre egy *index.ts* fájlt, és add hozzá az alábbi kódot:

```typescript
import { McpServer, ResourceTemplate } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";
 
// Hozzon létre egy MCP szervert
const server = new McpServer({
  name: "Calculator MCP Server",
  version: "1.0.0"
});
```

Most már van egy szervered, de nem csinál sokat, javítsuk ki ezt.

#### Python

```python
# server.py
from mcp.server.fastmcp import FastMCP

# MCP szerver létrehozása
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

Java esetén hozd létre a szerver alap komponenseit. Először módosítsd a fő alkalmazás osztályt:

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

Hozd létre a kalkulátor szolgáltatást *src/main/java/com/microsoft/mcp/sample/server/service/CalculatorService.java*:

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

**Opcionális komponensek egy éles szolgáltatáshoz:**

Hozz létre egy indítási konfigurációt *src/main/java/com/microsoft/mcp/sample/server/config/StartupConfig.java*:

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

Hozz létre egy egészségügyi kontrollert *src/main/java/com/microsoft/mcp/sample/server/controller/HealthController.java*:

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

Hozz létre egy kivételkezelőt *src/main/java/com/microsoft/mcp/sample/server/exception/GlobalExceptionHandler.java*:

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

        // Getterek
        public String getCode() { return code; }
        public String getMessage() { return message; }
    }
}
```

Hozz létre egy egyedi bannert *src/main/resources/banner.txt*:

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

Add hozzá a következő kódot a *src/main.rs* fájl tetejéhez. Ez importálja a szükséges könyvtárakat és modulokat az MCP szerveredhez.

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

A kalkulátor szerver egy egyszerű lesz, amely két számot összead. Hozzunk létre egy struktúrát a kalkulátor kérés reprezentálására.

```rust
#[derive(Debug, serde::Deserialize, schemars::JsonSchema)]
pub struct CalculatorRequest {
    pub a: f64,
    pub b: f64,
}
```

Ezután hozz létre egy struktúrát a kalkulátor szerver reprezentálására. Ez a struktúra tartalmazza az eszköz routert, amely az eszközök regisztrálására szolgál.

```rust
#[derive(Debug, Clone)]
pub struct Calculator {
    tool_router: ToolRouter<Self>,
}
```

Most implementálhatjuk a `Calculator` struktúrát, hogy létrehozzunk egy új szerver példányt és megvalósítsuk a szerver kezelőt, amely szerver információkat szolgáltat.

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

Végül implementálni kell a fő függvényt a szerver indításához. Ez a függvény létrehoz egy `Calculator` példányt és a standard bemenet/kimenet felett szolgálja ki.

```rust
#[tokio::main]
async fn main() -> Result<(), Box<dyn Error>> {
    let service = Calculator::new().serve(stdio()).await?;
    service.waiting().await?;
    Ok(())
}
```

A szerver most már alapvető információkat szolgáltat magáról. Következő lépésként hozzáadunk egy eszközt az összeadás elvégzéséhez.

### -5- Eszköz és erőforrás hozzáadása

Adj hozzá egy eszközt és egy erőforrást az alábbi kód hozzáadásával:

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

Az eszközöd paramétereket vesz át `a` és `b` néven, és egy olyan választ ad, amely a következő formátumú:

```typescript
{
  contents: [{
    type: "text", content: "some content"
  }]
}
```

Az erőforrásod egy "greeting" nevű stringen keresztül érhető el, és egy `name` paramétert vesz át, amely hasonló választ ad, mint az eszköz:

```typescript
{
  uri: "<href>",
  text: "a text"
}
```

#### Python

```python
# Adj hozzá egy összeadási eszközt
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


# Adj hozzá egy dinamikus üdvözlő erőforrást
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}!"
```

A fenti kódban:

- Definiáltunk egy `add` nevű eszközt, amely `a` és `b` paramétereket vesz át, mindkettő egész szám.
- Létrehoztunk egy `greeting` nevű erőforrást, amely `name` paramétert fogad.

#### .NET

Add ezt a Program.cs fájlodhoz:

```csharp
[McpServerToolType]
public static class CalculatorTool
{
    [McpServerTool, Description("Adds two numbers")]
    public static string Add(int a, int b) => $"Sum {a + b}";
}
```

#### Java

Az eszközök már létre lettek hozva az előző lépésben.

#### Rust

Adj hozzá egy új eszközt az `impl Calculator` blokkban:

```rust
#[tool(description = "Adds a and b")]
async fn add(
    &self,
    Parameters(CalculatorRequest { a, b }): Parameters<CalculatorRequest>,
) -> String {
    (a + b).to_string()
}
```

### -6- Végleges kód

Adjuk hozzá az utolsó kódot, amire szükség van, hogy a szerver elindulhasson:

#### TypeScript

```typescript
// Kezdje el az üzenetek fogadását a stdin-en és az üzenetek küldését a stdout-on
const transport = new StdioServerTransport();
await server.connect(transport);
```

Íme a teljes kód:

```typescript
// index.ts
import { McpServer, ResourceTemplate } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";

// MCP szerver létrehozása
const server = new McpServer({
  name: "Calculator MCP Server",
  version: "1.0.0"
});

// Egy kiegészítő eszköz hozzáadása
server.tool(
  "add",
  { a: z.number(), b: z.number() },
  async ({ a, b }) => ({
    content: [{ type: "text", text: String(a + b) }]
  })
);

// Dinamikus üdvözlő erőforrás hozzáadása
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

// Üzenetek fogadása stdin-en és üzenetek küldése stdout-on kezdődik
const transport = new StdioServerTransport();
server.connect(transport);
```

#### Python

```python
# server.py
from mcp.server.fastmcp import FastMCP

# MCP szerver létrehozása
mcp = FastMCP("Demo")


# Egy összeadási eszköz hozzáadása
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


# Dinamikus üdvözlő erőforrás hozzáadása
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}!"

# Fő végrehajtási blokk - ez szükséges a szerver futtatásához
if __name__ == "__main__":
    mcp.run()
```

#### .NET

Hozz létre egy Program.cs fájlt az alábbi tartalommal:

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

A teljes fő alkalmazás osztályod így nézzen ki:

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

A Rust szerver végleges kódja így nézzen ki:

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

### -7- A szerver tesztelése

Indítsd el a szervert az alábbi paranccsal:

#### TypeScript

```sh
npm run build
```

#### Python

```sh
mcp run server.py
```

> Az MCP Inspector használatához használd a `mcp dev server.py` parancsot, amely automatikusan elindítja az Inspectort és biztosítja a szükséges proxy munkamenet tokent. Ha a `mcp run server.py` parancsot használod, manuálisan kell elindítanod az Inspectort és konfigurálnod a kapcsolatot.

#### .NET

Győződj meg róla, hogy a projekt könyvtáradban vagy:

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

Futtasd a következő parancsokat a formázáshoz és a szerver futtatásához:

```sh
cargo fmt
cargo run
```

### -8-
győződj meg róla, hogy a `Command` mezőben a `python` van beállítva, az `Arguments` mezőben pedig a `server.py`. Ez biztosítja, hogy a szkript helyesen fusson.

#### .NET

Győződj meg róla, hogy a projekt könyvtáradban vagy:

```sh
cd McpCalculatorServer
npx @modelcontextprotocol/inspector dotnet run
```

#### Java

Győződj meg róla, hogy a kalkulátor szervered fut
Ezután indítsd el az inspectort:

```cmd
npx @modelcontextprotocol/inspector
```

Az inspector webes felületén:

1. Válaszd ki az "SSE" szállítási típust
2. Állítsd be az URL-t erre: `http://localhost:8080/sse`
3. Kattints a "Connect" gombra

![Connect](../../../../translated_images/tool.163d33e3ee307e209ef146d8f85060d2f7e83e9f59b3b1699a77204ae0454ad2.hu.png)

**Most már csatlakozva vagy a szerverhez**
**A Java szerver tesztelési szakasza most befejeződött**

A következő szakasz a szerverrel való interakcióról szól.

A következő felhasználói felületet kell látnod:

![Connect](../../../../translated_images/connect.141db0b2bd05f096fb1dd91273771fd8b2469d6507656c3b0c9df4b3c5473929.hu.png)

1. Csatlakozz a szerverhez a Connect gomb megnyomásával
  Miután csatlakoztál a szerverhez, a következőt kell látnod:

  ![Connected](../../../../translated_images/connected.73d1e042c24075d386cacdd4ee7cd748c16364c277d814e646ff2f7b5eefde85.hu.png)

1. Válaszd ki a "Tools" és a "listTools" opciót, meg kell jelennie az "Add" opciónak, válaszd ki az "Add"-ot és töltsd ki a paraméterértékeket.

  A következő választ kell látnod, azaz az "add" eszköz eredményét:

  ![Result of running add](../../../../translated_images/ran-tool.a5a6ee878c1369ec1e379b81053395252a441799dbf23416c36ddf288faf8249.hu.png)

Gratulálunk, sikerült létrehoznod és futtatnod az első szerveredet!

#### Rust

A Rust szerver futtatásához az MCP Inspector CLI-vel használd a következő parancsot:

```sh
npx @modelcontextprotocol/inspector cargo run --cli --method tools/call --tool-name add --tool-arg a=1 b=2
```

### Hivatalos SDK-k

Az MCP hivatalos SDK-kat biztosít több nyelvhez:

- [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk) - A Microsoft együttműködésével karbantartva
- [Java SDK](https://github.com/modelcontextprotocol/java-sdk) - A Spring AI együttműködésével karbantartva
- [TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk) - A hivatalos TypeScript implementáció
- [Python SDK](https://github.com/modelcontextprotocol/python-sdk) - A hivatalos Python implementáció
- [Kotlin SDK](https://github.com/modelcontextprotocol/kotlin-sdk) - A hivatalos Kotlin implementáció
- [Swift SDK](https://github.com/modelcontextprotocol/swift-sdk) - A Loopwork AI együttműködésével karbantartva
- [Rust SDK](https://github.com/modelcontextprotocol/rust-sdk) - A hivatalos Rust implementáció

## Főbb tanulságok

- Az MCP fejlesztői környezet beállítása egyszerű a nyelvspecifikus SDK-kkal
- MCP szerverek építése eszközök létrehozását és regisztrálását jelenti egyértelmű sémákkal
- A tesztelés és hibakeresés elengedhetetlen a megbízható MCP megvalósításokhoz

## Minták

- [Java Kalkulátor](../samples/java/calculator/README.md)
- [.Net Kalkulátor](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Kalkulátor](../samples/javascript/README.md)
- [TypeScript Kalkulátor](../samples/typescript/README.md)
- [Python Kalkulátor](../../../../03-GettingStarted/samples/python)
- [Rust Kalkulátor](../../../../03-GettingStarted/samples/rust)

## Feladat

Hozz létre egy egyszerű MCP szervert egy általad választott eszközzel:

1. Valósítsd meg az eszközt a preferált nyelveden (.NET, Java, Python, TypeScript vagy Rust).
2. Határozd meg a bemeneti paramétereket és a visszatérési értékeket.
3. Futtasd az inspector eszközt, hogy megbizonyosodj arról, hogy a szerver a vártak szerint működik.
4. Teszteld a megvalósítást különböző bemenetekkel.

## Megoldás

[Megoldás](./solution/README.md)

## További források

- [Ügynökök építése Model Context Protocol segítségével Azure-on](https://learn.microsoft.com/azure/developer/ai/intro-agents-mcp)
- [Távoli MCP Azure Container Apps segítségével (Node.js/TypeScript/JavaScript)](https://learn.microsoft.com/samples/azure-samples/mcp-container-ts/mcp-container-ts/)
- [.NET OpenAI MCP Ügynök](https://learn.microsoft.com/samples/azure-samples/openai-mcp-agent-dotnet/openai-mcp-agent-dotnet/)

## Mi következik

Következő: [MCP kliensekkel való kezdés](../02-client/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Jogi nyilatkozat**:
Ezt a dokumentumot az AI fordító szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével fordítottuk le. Bár a pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Kritikus információk esetén professzionális emberi fordítást javaslunk. Nem vállalunk felelősséget a fordítás használatából eredő félreértésekért vagy félreértelmezésekért.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->