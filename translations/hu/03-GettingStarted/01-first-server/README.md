# Kezdés az MCP-vel

Üdvözlünk az első lépésekben a Model Context Protocol (MCP) használatával! Akár új vagy az MCP-ben, akár mélyíteni szeretnéd a tudásodat, ez az útmutató végigvezet az alapvető beállítási és fejlesztési folyamatokon. Megtudhatod, hogyan teszi lehetővé az MCP az AI modellek és alkalmazások zökkenőmentes integrációját, és megtanulhatod, hogyan készítheted el gyorsan a környezeted MCP-alapú megoldások építéséhez és teszteléséhez.

> Összefoglaló: Ha AI alkalmazásokat fejlesztesz, tudod, hogy eszközöket és más erőforrásokat adhatsz hozzá az LLM-hez (nagy nyelvi modellhez), hogy az LLM tudásosabb legyen. Azonban ha ezeket az eszközöket és erőforrásokat egy szerveren helyezed el, az alkalmazás és a szerver képességei bármely kliens által használhatók LLM-fel vagy anélkül.

## Áttekintés

Ez a lecke gyakorlati útmutatást nyújt az MCP környezetek beállításához és első MCP alkalmazásaid elkészítéséhez. Megtanulod, hogyan kell telepíteni a szükséges eszközöket és keretrendszereket, alap MCP szervereket építeni, hoszt alkalmazásokat létrehozni, és tesztelni a megvalósításaidat.

A Model Context Protocol (MCP) egy nyílt protokoll, amely szabványosítja, hogyan biztosítanak az alkalmazások kontextust az LLM-ek számára. Gondolj az MCP-re úgy, mint egy USB-C portra az AI alkalmazások számára – szabványos módot nyújt AI modellek különböző adatforrásokhoz és eszközökhöz való csatlakoztatására.

## Tanulási célok

A lecke végére képes leszel:

- MCP fejlesztői környezetek beállítása C#, Java, Python, TypeScript és Rust nyelveken
- Alap MCP szerverek építése és telepítése egyedi funkciókkal (erőforrások, promptok és eszközök)
- Hoszt alkalmazások létrehozása, amelyek csatlakoznak MCP szerverekhez
- MCP megvalósítások tesztelése és hibakeresése

## Az MCP környezeted beállítása

Mielőtt elkezdenéd az MCP-vel való munkát, fontos előkészíteni a fejlesztői környezetet és megérteni az alapvető munkafolyamatot. Ez a szakasz végigvezet az első beállítási lépéseken, hogy biztosítsa a zökkenőmentes kezdést az MCP-vel.

### Előfeltételek

Mielőtt belemerülnél az MCP fejlesztésbe, bizonyosodj meg arról, hogy rendelkezel:

- **Fejlesztői környezet**: Az általad választott nyelvhez (C#, Java, Python, TypeScript, vagy Rust)
- **IDE/Szerkesztő**: Visual Studio, Visual Studio Code, IntelliJ, Eclipse, PyCharm, vagy bármilyen modern kódszerkesztő
- **Csomagkezelők**: NuGet, Maven/Gradle, pip, npm/yarn vagy Cargo
- **API kulcsok**: Azokhoz az AI szolgáltatásokhoz, amelyeket használni tervezel a hoszt alkalmazásaiban

## Alap MCP szerver felépítése

Egy MCP szerver tipikusan tartalmazza:

- **Szerver konfiguráció**: Port, hitelesítés és egyéb beállítások megadása
- **Erőforrások**: Az LLM-ek számára rendelkezésre álló adatok és kontextus
- **Eszközök**: Az a funkció, amelyet a modellek meghívhatnak
- **Promptok**: Szöveg generálására vagy strukturálására szolgáló sablonok

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
  // A 'list' paraméter vezérli, hogyan sorolja fel az erőforrás az elérhető fájlokat. Ha undefined-ra állítja, az letiltja a listázást erre az erőforrásra.
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

// Kezdje meg az üzenetek fogadását a stdin-en és az üzenetek küldését a stdout-ra
const transport = new StdioServerTransport();
await server.connect(transport);
```

A fenti kódban:

- Importáljuk az MCP TypeScript SDK szükséges osztályait.
- Létrehozunk és konfigurálunk egy új MCP szerver példányt.
- Regisztrálunk egy egyedi eszközt (`calculator`) egy kezelőfüggvénnyel.
- Elindítjuk a szervert, hogy fogadja a bejövő MCP kéréseket.

## Tesztelés és hibakeresés

Mielőtt elkezdenéd tesztelni az MCP szerveredet, fontos megismerkedni a rendelkezésre álló eszközökkel és a hibakeresés legjobb gyakorlataival. A hatékony tesztelés biztosítja, hogy a szerver a várt módon működjön, és segít gyorsan felismerni, valamint megoldani a problémákat. A következő szakasz ajánlásokat tartalmaz az MCP megvalósításod érvényesítéséhez.

Az MCP eszközöket kínál a szerverek teszteléséhez és hibakereséséhez:

- **Inspector eszköz**, ez a grafikus felület lehetővé teszi, hogy csatlakozz a szerveredhez és teszteld az eszközöket, promptokat és erőforrásokat.
- **curl**, parancssori eszköz segítségével is csatlakozhatsz a szerverhez, vagy bármely más klienssel, amely HTTP parancsokat tud létrehozni és futtatni.

### Az MCP Inspector használata

Az [MCP Inspector](https://github.com/modelcontextprotocol/inspector) egy vizuális tesztelő eszköz, amely segít:

1. **A szerver képességeinek felfedezése**: Automatikusan felismeri a rendelkezésre álló erőforrásokat, eszközöket és promptokat
2. **Eszközök futtatásának tesztelése**: Különböző paramétereket próbálhatsz ki, és valós időben láthatod a válaszokat
3. **Szerver metaadatainak megtekintése**: Megvizsgálhatod a szerver információit, sémákat és konfigurációkat

```bash
# ex TypeScript, az MCP Inspector telepítése és futtatása
npx @modelcontextprotocol/inspector node build/index.js
```

A fenti parancsok futtatásakor az MCP Inspector elindít egy helyi webes felületet a böngésződben. Egy műszerfalat fogsz látni, amely megjeleníti a regisztrált MCP szervereidet, azok elérhető eszközeit, erőforrásait és promptjait. A felület lehetővé teszi az eszközök interaktív tesztelését, a szerver metaadatainak ellenőrzését és a valós idejű válaszok megtekintését, megkönnyítve ezzel az MCP szerver megvalósítások ellenőrzését és hibakeresését.

Íme egy képernyőkép arról, hogyan nézhet ki:

![MCP Inspector szerver kapcsolat](../../../../translated_images/hu/connected.73d1e042c24075d3.webp)

## Gyakori beállítási problémák és megoldásaik

| Probléma | Lehetséges megoldás |
|-------|-------------------|
| Kapcsolat elutasítva | Ellenőrizd, hogy a szerver fut-e és a port helyes-e |
| Eszköz futtatási hibák | Ellenőrizd a paraméterek érvényességét és a hibakezelést |
| Hitelesítési hibák | Ellenőrizd az API kulcsokat és jogosultságokat |
| Séma érvényesítési hibák | Győződj meg róla, hogy a paraméterek megfelelnek a meghatározott sémának |
| Szerver nem indul | Ellenőrizd a portütközéseket vagy hiányzó függőségeket |
| CORS hibák | Állíts be megfelelő CORS fejlécet a kereszt-eredetű kérésekhez |
| Hitelesítési problémák | Ellenőrizd a token érvényességét és jogosultságait |

## Helyi fejlesztés

A helyi fejlesztéshez és teszteléshez közvetlenül a gépeden is futtathatod az MCP szervereket:

1. **Indítsd el a szerver folyamatot**: Futtasd az MCP szerver alkalmazásodat
2. **Hálózati beállítások**: Győződj meg róla, hogy a szerver elérhető a várt porton
3. **Kliens csatlakozás**: Használj helyi kapcsolati URL-eket, például `http://localhost:3000`

```bash
# Példa: Egy TypeScript MCP szerver futtatása helyben
npm run start
# A szerver fut a http://localhost:3000 címen
```

## Az első MCP szervered építése

Korábban már foglalkoztunk a [core fogalmakkal](../../01-CoreConcepts/README.md), most pedig ideje tudásodat gyakorlati alkalmazásba helyezni.

### Mit tud egy szerver?

Mielőtt elkezdjük a kódírást, emlékezzünk arra, mit is tud egy szerver:

Egy MCP szerver például képes:

- Helyi fájlokhoz és adatbázisokhoz hozzáférni
- Távoli API-khoz csatlakozni
- Számításokat végezni
- Más eszközökkel és szolgáltatásokkal integrálódni
- Felhasználói felületet biztosítani az interakciókhoz

Nagyszerű, most, hogy tudjuk, mit tudunk vele csinálni, lássunk neki a kódolásnak.

## Gyakorlat: Szerver létrehozása

Ehhez a következő lépéseket kell követned:

- Telepítsd az MCP SDK-t.
- Hozz létre egy projektet és állítsd be a projekt struktúráját.
- Írd meg a szerver kódját.
- Teszteld a szervert.

### -1- Projekt létrehozása

#### TypeScript

```sh
# Projektkönyvtár létrehozása és npm projekt inicializálása
mkdir calculator-server
cd calculator-server
npm init -y
```

#### Python

```sh
# Projekt könyvtár létrehozása
mkdir calculator-server
cd calculator-server
# Nyisd meg a mappát a Visual Studio Code-ban - Ezt kihagyhatod, ha másik fejlesztői környezetet használsz
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

Bontsd ki a zip fájlt:

```bash
unzip calculator-server.zip -d calculator-server
cd calculator-server
# opcionális, eltávolíthatja a nem használt tesztet
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

Miután létrehoztad a projektet, adjuk hozzá a függőségeket:

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
# Hozzon létre egy virtuális környezetet és telepítse a függőségeket
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

Hozz létre egy *tsconfig.json* fájlt a következő tartalommal:

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

Hozz létre egy mappát a forráskód számára:

```sh
mkdir src
touch src/index.ts
```

#### Python

Hozd létre a *server.py* fájlt

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

Java Spring Boot projektek esetén a projekt struktúrát automatikusan létrehozza a rendszer.

#### Rust

Rust esetén a *src/main.rs* fájl alapértelmezetten létrejön a `cargo init` futtatásakor. Nyisd meg a fájlt és töröld az alapértelmezett kódot.

### -4- Szerverkód létrehozása

#### TypeScript

Hozz létre egy *index.ts* fájlt, és másold bele az alábbi kódot:

```typescript
import { McpServer, ResourceTemplate } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";
 
// MCP szerver létrehozása
const server = new McpServer({
  name: "Calculator MCP Server",
  version: "1.0.0"
});
```

Most van egy szervered, de még nem csinál sokat, javítsuk ki ezt.

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

**Opcionális komponensek egy éles környezethez:**

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

Hozz létre egy egészségi vezérlőt *src/main/java/com/microsoft/mcp/sample/server/controller/HealthController.java*:

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

Add hozzá a következő kódot a *src/main.rs* fájl tetejére. Ez importálja a szükséges könyvtárakat és modulokat az MCP szerveredhez.

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

A kalkulátor szerver egy egyszerű lesz, amely két szám összegzésére képes. Hozzunk létre egy structot, amely a kalkulátor kérést reprezentálja.

```rust
#[derive(Debug, serde::Deserialize, schemars::JsonSchema)]
pub struct CalculatorRequest {
    pub a: f64,
    pub b: f64,
}
```

Ezután hozzunk létre egy structot a kalkulátor szerver reprezentálásához. Ez a struct tartalmazni fogja az eszköz routert, amely az eszközök regisztrálására szolgál.

```rust
#[derive(Debug, Clone)]
pub struct Calculator {
    tool_router: ToolRouter<Self>,
}
```

Most implementáljuk a `Calculator` structot, hogy létrehozzunk egy új szerver példányt, valamint implementáljuk a szerver kezelőt, amely a szerver információit szolgáltatja.

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

Végül implementálnunk kell a fő függvényt a szerver indításához. Ez a függvény létrehozza a `Calculator` struct példányát, és a standard bemenet/kimenet felett futtatja.

```rust
#[tokio::main]
async fn main() -> Result<(), Box<dyn Error>> {
    let service = Calculator::new().serve(stdio()).await?;
    service.waiting().await?;
    Ok(())
}
```

A szerver most már alap információkat tud szolgáltatni magáról. Ezután hozzáadunk egy eszközt az összeadás elvégzéséhez.

### -5- Eszköz és erőforrás hozzáadása

Adjunk hozzá egy eszközt és egy erőforrást az alábbi kód hozzáadásával:

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

Az eszközöd paraméterként fogadja az `a` és `b` értékeket és futtat egy függvényt, amely a következő formátumú választ állít elő:

```typescript
{
  contents: [{
    type: "text", content: "some content"
  }]
}
```

Az erőforrásod egy "greeting" stringen keresztül érhető el, és a `name` paramétert veszi át, és hasonló választ ad, mint az eszköz:

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


# Adj hozzá egy dinamikus üdvözlő forrást
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}!"
```

A fenti kódban:

- Definiáltunk egy `add` nevű eszközt, amely paraméterként két egész számot, `a`-t és `b`-t vár.
- Létrehoztunk egy `greeting` erőforrást, amely `name` paramétert fogad.

#### .NET

Add ezt a Program.cs fájlodba:

```csharp
[McpServerToolType]
public static class CalculatorTool
{
    [McpServerTool, Description("Adds two numbers")]
    public static string Add(int a, int b) => $"Sum {a + b}";
}
```

#### Java

Az eszközök már elkészültek az előző lépésben.

#### Rust

Adj hozzá egy új eszközt az `impl Calculator` blokkba:

```rust
#[tool(description = "Adds a and b")]
async fn add(
    &self,
    Parameters(CalculatorRequest { a, b }): Parameters<CalculatorRequest>,
) -> String {
    (a + b).to_string()
}
```

### -6- Végső kód

Adjunk hozzá minden szükséges kódot, hogy a szerver elinduljon:

#### TypeScript

```typescript
// Kezdd el fogadni az üzeneteket a stdin-en, és küldeni az üzeneteket a stdout-ra
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

// Egy összeadó eszköz hozzáadása
server.tool(
  "add",
  { a: z.number(), b: z.number() },
  async ({ a, b }) => ({
    content: [{ type: "text", text: String(a + b) }]
  })
);

// Egy dinamikus üdvözlő erőforrás hozzáadása
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

// Üzenetek fogadásának indítása stdin-ről és üzenetek küldése stdout-ra
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

# Fő végrehajtási blokk - a szerver futtatásához szükséges
if __name__ == "__main__":
    mcp.run()
```

#### .NET

Hozz létre egy Program.cs fájlt a következő tartalommal:

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

> Az MCP Inspector használatához használd a `mcp dev server.py` parancsot, amely automatikusan elindítja az Inspectort és biztosítja a szükséges proxy munkamenet tokent. Ha a `mcp run server.py` parancsot használod, kézzel kell elindítanod az Inspectort és konfigurálnod a kapcsolatot.

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

Futtasd az alábbi parancsokat a formázáshoz és a szerver indításához:

```sh
cargo fmt
cargo run
```

### -8- Futtatás az Inspectorral

Az Inspector egy nagyszerű eszköz, amely el tudja indítani a szervered, és lehetővé teszi az interakciót vele, hogy le tudjad tesztelni, működik-e. Indítsuk el:

> [!NOTE]
> A "command" mezőben eltérő lehet a parancs, mert az a szerver futtatására szolgáló parancsot tartalmazza a te adott futtatókörnyezetedre szabva.

#### TypeScript

```sh
npx @modelcontextprotocol/inspector node build/index.js
```

Vagy add hozzá a *package.json* fájlodhoz így: `"inspector": "npx @modelcontextprotocol/inspector node build/index.js"` majd futtasd a `npm run inspector` parancsot.

#### Python

A Python környezet egy Node.js eszközt, az Inspectort használja. Lehet úgy is hívni az eszközt, hogy:

```sh
mcp dev server.py
```

Azonban nem implementálja az összes elérhető metódust, ezért ajánlott közvetlenül a Node.js eszközt futtatni az alábbi módon:

```sh
npx @modelcontextprotocol/inspector mcp run server.py
```

Ha olyan eszközt vagy IDE-t használsz, amely lehetővé teszi, hogy futtatási parancsokat és argumentumokat konfigurálj szkriptek számára,
győződj meg róla, hogy a `Command` mezőbe a `python` van beállítva, az `Arguments` mezőbe pedig a `server.py`. Ez biztosítja, hogy a szkript helyesen fusson.

#### .NET

Győződj meg róla, hogy a projekt könyvtáradban vagy:

```sh
cd McpCalculatorServer
npx @modelcontextprotocol/inspector dotnet run
```

#### Java

Biztosítsd, hogy a kalkulátor szerver fusson
Ezután futtasd az inspektort:

```cmd
npx @modelcontextprotocol/inspector
```

Az inspektor webes felületén:

1. Válaszd ki a "SSE" szállítási típust
2. Állítsd be az URL-t erre: `http://localhost:8080/sse`
3. Kattints a "Connect"-re

![Connect](../../../../translated_images/hu/tool.163d33e3ee307e20.webp)

**Most már kapcsolódva vagy a szerverhez**
**A Java szerver tesztelése szakasz most befejeződött**

A következő szakasz a szerverrel való interakcióról szól.

Ennek az alábbi felhasználói felületnek kell megjelennie:

![Connect](../../../../translated_images/hu/connect.141db0b2bd05f096.webp)

1. Kapcsolódj a szerverhez a Connect gomb kiválasztásával
  Miután kapcsolódtál a szerverhez, a következőt kell látnod:

  ![Connected](../../../../translated_images/hu/connected.73d1e042c24075d3.webp)

1. Válaszd ki a "Tools" majd a "listTools" opciót, meg kell jelennie az "Add"-nak, válaszd ki az "Add"-ot, és töltsd ki a paraméterértékeket.

  A következő választ kell látnod, azaz az "add" eszköz eredményét:

  ![Result of running add](../../../../translated_images/hu/ran-tool.a5a6ee878c1369ec.webp)

Gratulálunk, sikerült létrehoznod és futtatnod az első szerveredet!

#### Rust

A Rust szerver futtatásához az MCP Inspector CLI-vel használd a következő parancsot:

```sh
npx @modelcontextprotocol/inspector cargo run --cli --method tools/call --tool-name add --tool-arg a=1 b=2
```

### Hivatalos SDK-k

Az MCP hivatalos SDK-kat biztosít több nyelvhez:

- [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk) - Microsoft együttműködésben karbantartva
- [Java SDK](https://github.com/modelcontextprotocol/java-sdk) - Spring AI együttműködésben karbantartva
- [TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk) - A hivatalos TypeScript implementáció
- [Python SDK](https://github.com/modelcontextprotocol/python-sdk) - A hivatalos Python implementáció
- [Kotlin SDK](https://github.com/modelcontextprotocol/kotlin-sdk) - A hivatalos Kotlin implementáció
- [Swift SDK](https://github.com/modelcontextprotocol/swift-sdk) - Loopwork AI együttműködésben karbantartva
- [Rust SDK](https://github.com/modelcontextprotocol/rust-sdk) - A hivatalos Rust implementáció

## Főbb tanulságok

- Az MCP fejlesztői környezet beállítása egyszerű, nyelvspecifikus SDK-kkal
- MCP szerverek építése során világos sémákkal rendelkező eszközöket hozunk létre és regisztrálunk
- A tesztelés és hibakeresés elengedhetetlen a megbízható MCP megvalósításokhoz

## Példák

- [Java Kalkulátor](../samples/java/calculator/README.md)
- [.Net Kalkulátor](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Kalkulátor](../samples/javascript/README.md)
- [TypeScript Kalkulátor](../samples/typescript/README.md)
- [Python Kalkulátor](../../../../03-GettingStarted/samples/python)
- [Rust Kalkulátor](../../../../03-GettingStarted/samples/rust)

## Feladat

Hozz létre egy egyszerű MCP szervert egy általad választott eszközzel:

1. Valósítsd meg az eszközt a preferált nyelveden (.NET, Java, Python, TypeScript vagy Rust).
2. Határozd meg a bemeneti paramétereket és visszatérési értékeket.
3. Futtasd az inspektor eszközt, hogy megbizonyosodj arról, hogy a szerver helyesen működik.
4. Teszteld a megvalósítást különböző bemenetekkel.

## Megoldás

[Megoldás](./solution/README.md)

## További források

- [Agensek létrehozása Model Context Protocol segítségével az Azure-on](https://learn.microsoft.com/azure/developer/ai/intro-agents-mcp)
- [Távoli MCP Azure Container Apps segítségével (Node.js/TypeScript/JavaScript)](https://learn.microsoft.com/samples/azure-samples/mcp-container-ts/mcp-container-ts/)
- [.NET OpenAI MCP Agent](https://learn.microsoft.com/samples/azure-samples/openai-mcp-agent-dotnet/openai-mcp-agent-dotnet/)

## Mi következik

Következő: [Első lépések az MCP klienssel](../02-client/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Felmentés**:
Ezt a dokumentumot az AI fordító szolgáltatás [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével fordítottuk le. Bár igyekszünk pontosságra törekedni, kérjük, vegye figyelembe, hogy az automatizált fordítások tartalmazhatnak hibákat vagy pontatlanságokat. Az eredeti, anyanyelvi dokumentum tekintendő hivatalos forrásnak. Kritikus információk esetén professzionális emberi fordítást ajánlunk. Nem vállalunk felelősséget az ebből származó félreértésekért vagy félreértelmezésekért.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->