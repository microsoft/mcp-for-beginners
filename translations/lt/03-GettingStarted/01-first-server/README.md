# Pradžia su MCP

Sveiki atvykę į pirmuosius Model Context Protocol (MCP) žingsnius! Nesvarbu, ar esate naujokas MCP, ar norite gilinti savo žinias, ši pamoka padės jums peržengti esminį aplinkos nustatymą ir vystymo procesą. Sužinosite, kaip MCP leidžia sklandžiai integruoti DI modelius ir programas, bei išmoksite greitai paruošti savo aplinką MCP pagrįstų sprendimų kūrimui ir testavimui.

> TLDR; Jei kuriate DI programas, žinote, kad galite pridėti įrankių ir kitų išteklių prie savo LLM (didelio kalbos modelio), kad LLM būtų išmanesnis. Tačiau jei šiuos įrankius ir išteklius dedate į serverį, programos ir serverio galimybės gali būti naudojamos bet kurio kliento su/ be LLM.

## Apžvalga

Ši pamoka pateikia praktines rekomendacijas, kaip nustatyti MCP aplinkas ir kurti pirmąsias MCP programas. Sužinosite, kaip įdiegti reikiamus įrankius ir karkasus, sukurti pagrindinius MCP serverius, kurti pagrindines programas ir testuoti savo įgyvendinimus.

Model Context Protocol (MCP) yra atviras protokolas, standartizuojantis, kaip programos suteikia kontekstą LLM. Įsivaizduokite MCP kaip USB-C lizdą DI programoms – jis suteikia standartizuotą būdą prijungti DI modelius prie skirtingų duomenų šaltinių ir įrankių.

## Mokymosi tikslai

Pamokos pabaigoje galėsite:

- Nustatyti MCP kūrimo aplinkas C#, Java, Python, TypeScript ir Rust kalbomis
- Kurti ir diegti pagrindinius MCP serverius su pasirinktomis funkcijomis (ištekliai, užklausos ir įrankiai)
- Kurti pagrindines programas, kurios jungiasi prie MCP serverių
- Testuoti ir derinti MCP įgyvendinimus

## MCP aplinkos nustatymas

Prieš pradėdami dirbti su MCP, svarbu pasiruošti kūrimo aplinką ir suprasti pagrindinį darbo procesą. Ši dalis padės jums žingsnis po žingsnio pradėti MCP darbą sklandžiai.

### Reikalavimai

Prieš pradėdami MCP kūrimą, įsitikinkite, kad turite:

- **Kūrimo aplinka**: Jūsų pasirinkta kalba (C#, Java, Python, TypeScript arba Rust)
- **IDE / Redaktorius**: Visual Studio, Visual Studio Code, IntelliJ, Eclipse, PyCharm arba bet koks šiuolaikinis kodo redaktorius
- **Paketo valdytojai**: NuGet, Maven/Gradle, pip, npm/yarn arba Cargo
- **API raktai**: Bet kokioms DI paslaugoms, kurias planuojate naudoti pagrindinėse programose

## Pagrindinė MCP serverio struktūra

MCP serveris paprastai turi:

- **Serverio konfigūracija**: Prievado, autentifikacijos ir kitų nustatymų paruošimas
- **Ištekliai**: Duomenys ir kontekstas, suteikiamas LLM
- **Įrankiai**: Funkcionalumas, kurį modeliai gali iškviesti
- **Užklausos**: Šablonai tekstui generuoti arba struktūrizuoti

Štai supaprastintas pavyzdys TypeScript kalba:

```typescript
import { McpServer, ResourceTemplate } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";

// Sukurkite MCP serverį
const server = new McpServer({
  name: "Demo",
  version: "1.0.0"
});

// Pridėti papildomą įrankį
server.tool("add",
  { a: z.number(), b: z.number() },
  async ({ a, b }) => ({
    content: [{ type: "text", text: String(a + b) }]
  })
);

// Pridėti dinaminį pasveikinimo išteklių
server.resource(
  "file",
  // Parametras 'list' nustato, kaip išteklius pateikia galimus failus. Nustačius jį į undefined, išvardijimas šiam ištekliui išjungiamas.
  new ResourceTemplate("file://{path}", { list: undefined }),
  async (uri, { path }) => ({
    contents: [{
      uri: uri.href,
      text: `File, ${path}!`
    }]
  })
);

// Pridėti failo išteklių, kuris skaito failo turinį
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

// Pradėti gauti žinutes iš stdin ir siųsti žinutes į stdout
const transport = new StdioServerTransport();
await server.connect(transport);
```

Ankstesniame kode mes:

- Importuojame reikiamas MCP TypeScript SDK klases.
- Kuriame ir konfigūruojame naują MCP serverio egzempliorių.
- Registruojame pasirinktinį įrankį (`calculator`) su apdorojimo funkcija.
- Pradedame serverį klausytis atvykstančių MCP užklausų.

## Testavimas ir derinimas

Prieš pradėdami testuoti savo MCP serverį, svarbu suprasti turimus įrankius ir geriausias derinimo praktikas. Efektyvus testavimas užtikrina, kad serveris veikia pagal lūkesčius, ir padeda greitai identifikuoti bei spręsti problemas. Toliau pateikiami siūlomi metodai MCP įgyvendinimo patikrinimui.

MCP siūlo įrankius, kurie padeda testuoti ir derinti serverius:

- **Inspector įrankis**, ši grafinė sąsaja leidžia prisijungti prie serverio ir testuoti įrankius, užklausas ir išteklius.
- **curl**, taip pat galite prisijungti prie serverio naudodami komandų eilutės įrankį kaip curl ar kitus klientus, kurie gali kurti ir vykdyti HTTP komandas.

### MCP Inspector naudojimas

[MCP Inspector](https://github.com/modelcontextprotocol/inspector) yra vizualinis testavimo įrankis, kuris padeda jums:

1. **Aptikti serverio galimybes**: Automatiškai surasti prieinamus išteklius, įrankius ir užklausas
2. **Testuoti įrankių vykdymą**: Išbandyti skirtingus parametrus ir stebėti atsakymus realiu laiku
3. **Peržiūrėti serverio metaduomenis**: Peržvelgti serverio informaciją, schemas ir konfigūracijas

```bash
# pvz., TypeScript, MCP Inspector įdiegimas ir vykdymas
npx @modelcontextprotocol/inspector node build/index.js
```

Kai paleidžiate aukščiau pateiktas komandas, MCP Inspector paleidžia vietinę žiniatinklio sąsają jūsų naršyklėje. Galite tikėtis pamatyti prietaisų skydelį, rodantį jūsų registruotus MCP serverius, juose prieinamus įrankius, išteklius ir užklausas. Sąsaja leidžia interaktyviai testuoti įrankių vykdymą, tikrinti serverio metaduomenis ir matyti atsakymus realiu laiku, taip palengvinant MCP serverio įgyvendinimų validavimą ir derinimą.

Štai kaip tai gali atrodyti:

![MCP Inspector serverio prisijungimas](../../../../translated_images/lt/connected.73d1e042c24075d3.webp)

## Dažniausios klaidos diegiant ir sprendimai

| Klaida | Galimas sprendimas |
|-------|-------------------|
| Prisijungimas atmestas | Patikrinkite, ar serveris veikia ir ar prievadas teisingas |
| Įrankių vykdymo klaidos | Peržiūrėkite parametrų validavimą ir klaidų apdorojimą |
| Autentifikacijos klaidos | Patikrinkite API raktus ir teises |
| Schema klaidų validavimas | Įsitikinkite, kad parametrai atitinka apibrėžtą schemą |
| Serveris neprasideda | Patikrinkite, ar nėra prievadų konfliktų ar trūksta priklausomybių |
| CORS klaidos | Sukonfigūruokite tinkamus CORS antraštes tarpdomens užklausoms |
| Autentifikacijos problemos | Patikrinkite žetono galiojimą ir teises |

## Vietinis vystymas

Vietiniam vystymui ir testavimui galite paleisti MCP serverius tiesiogiai savo kompiuteryje:

1. **Paleiskite serverio procesą**: Vykdykite savo MCP serverio programą
2. **Sukurti tinklą**: Įsitikinkite, kad serveris yra pasiekiamas numatytu prievadu
3. **Prijungti klientus**: Naudokite vietinius prisijungimo URL kaip `http://localhost:3000`

```bash
# Pavyzdys: TypeScript MCP serverio paleidimas vietoje
npm run start
# Serveris veikia adresu http://localhost:3000
```

## Pirmojo MCP serverio kūrimas

Ankstesnėje pamokoje apžvelgėme [Pagrindines sąvokas](../../01-CoreConcepts/README.md), dabar laikas tą žinią pritaikyti.

### Ką gali serveris

Prieš rašydami kodą, prisiminkime, ką gali serveris:

MCP serveris gali, pavyzdžiui:

- Prieiti prie vietinių failų ir duomenų bazių
- Jungtis prie nuotolinių API
- Atlikti skaičiavimus
- Integruotis su kitais įrankiais ir paslaugomis
- Teikti vartotojo sąsają bendraujant

Šaunu, kad žinome ko galime siekti, pradėkime koduoti.

## Pratybos: Serverio kūrimas

Norint sukurti serverį, reikia atlikti šiuos žingsnius:

- Įdiegti MCP SDK.
- Sukurti projektą ir nustatyti projekto struktūrą.
- Parašyti serverio kodą.
- Testuoti serverį.

### -1- Projekto sukūrimas

#### TypeScript

```sh
# Sukurkite projekto katalogą ir inicializuokite npm projektą
mkdir calculator-server
cd calculator-server
npm init -y
```

#### Python

```sh
# Sukurkite projekto katalogą
mkdir calculator-server
cd calculator-server
# Atidarykite aplanką Visual Studio Code – jei naudojate kitą IDE, praleiskite šį veiksmą
code .
```

#### .NET

```sh
dotnet new console -n McpCalculatorServer
cd McpCalculatorServer
```

#### Java

Java atveju sukurkite Spring Boot projektą:

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

Išskleiskite zip failą:

```bash
unzip calculator-server.zip -d calculator-server
cd calculator-server
# neprivaloma pašalinti nenaudojamą testą
rm -rf src/test/java
```

Pridėkite šią pilną konfigūraciją į savo *pom.xml* failą:

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

### -2- Pridėti priklausomybes

Dabar, kai projektas sukurtas, pridėkime priklausomybes:

#### TypeScript

```sh
# Jei dar neįdiegta, įdiekite TypeScript globaliai
npm install typescript -g

# Įdiekite MCP SDK ir Zod schemos patikrinimui
npm install @modelcontextprotocol/sdk zod
npm install -D @types/node typescript
```

#### Python

```sh
# Sukurkite virtualią aplinką ir įdiekite priklausomybes
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

### -3- Projekto failų kūrimas

#### TypeScript

Atidarykite *package.json* failą ir pakeiskite turinį taip, kad galėtumėte konstruoti ir vykdyti serverį:

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

Sukurkite *tsconfig.json* su tokiu turiniu:

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

Sukurkite katalogą savo šaltinio kodui:

```sh
mkdir src
touch src/index.ts
```

#### Python

Sukurkite failą *server.py*

```sh
touch server.py
```

#### .NET

Įdiekite reikalingas NuGet paketas:

```sh
dotnet add package ModelContextProtocol --prerelease
dotnet add package Microsoft.Extensions.Hosting
```

#### Java

Java Spring Boot projektų struktūra susikuria automatiškai.

#### Rust

Rust atveju faile *src/main.rs* bus sukurtas numatytasis failas, kai vykdysite `cargo init`. Atidarykite failą ir ištrinkite numatytąjį kodą.

### -4- Serverio kodo kūrimas

#### TypeScript

Sukurkite failą *index.ts* ir įdėkite šį kodą:

```typescript
import { McpServer, ResourceTemplate } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";
 
// Sukurkite MCP serverį
const server = new McpServer({
  name: "Calculator MCP Server",
  version: "1.0.0"
});
```

Dabar turite serverį, bet jis dar nedaug ką daro, pataisykime tai.

#### Python

```python
# server.py
from mcp.server.fastmcp import FastMCP

# Sukurti MCP serverį
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

Java atveju sukurkite pagrindinius serverio komponentus. Pirmiausia pakeiskite pagrindinę programos klasę:

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

Sukurkite skaičiuotuvo servisą *src/main/java/com/microsoft/mcp/sample/server/service/CalculatorService.java*:

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

**Pasirinktiniai komponentai gamybinei paslaugai:**

Sukurkite paleidimo konfigūraciją *src/main/java/com/microsoft/mcp/sample/server/config/StartupConfig.java*:

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

Sukurkite sveikatos kontrolerį *src/main/java/com/microsoft/mcp/sample/server/controller/HealthController.java*:

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

Sukurkite išimčių tvarkytoją *src/main/java/com/microsoft/mcp/sample/server/exception/GlobalExceptionHandler.java*:

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

        // Gavimo metodai
        public String getCode() { return code; }
        public String getMessage() { return message; }
    }
}
```

Sukurkite pasirinktinį banerį *src/main/resources/banner.txt*:

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

Pridėkite šį kodą į *src/main.rs* failo viršų. Tai importuoja reikiamas bibliotekas ir modulius jūsų MCP serveriui.

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

Skaičiuotuvo serveris bus paprastas ir galės sudėti du skaičius. Sukurkime struktūrą, kuri reprezentuos skaičiuotuvo užklausą.

```rust
#[derive(Debug, serde::Deserialize, schemars::JsonSchema)]
pub struct CalculatorRequest {
    pub a: f64,
    pub b: f64,
}
```

Toliau sukurkite struktūrą, kuri reprezentuos skaičiuotuvo serverį. Ši struktūra saugos įrankių maršrutizatorių, kuris naudojamas įrankių registravimui.

```rust
#[derive(Debug, Clone)]
pub struct Calculator {
    tool_router: ToolRouter<Self>,
}
```

Dabar galime įgyvendinti `Calculator` struktūrą, sukurti naują serverio egzempliorių ir įgyvendinti serverio apdorotoją, kuris pateikia serverio informaciją.

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

Galiausiai įgyvendinkite pagrindinę funkciją serverio paleidimui. Ši funkcija sukurs `Calculator` struktūros egzempliorių ir aptarnaus jį per standartinę įvestį/išvestį.

```rust
#[tokio::main]
async fn main() -> Result<(), Box<dyn Error>> {
    let service = Calculator::new().serve(stdio()).await?;
    service.waiting().await?;
    Ok(())
}
```

Serveris dabar paruoštas pateikti pagrindinę informaciją apie save. Toliau pridėsime įrankį, kuris vykdys sudėjimą.

### -5- Įrankio ir ištekliaus pridėjimas

Pridėkite įrankį ir išteklių pridėdami šį kodą:

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

Jūsų įrankis priima parametrus `a` ir `b` ir vykdo funkciją, kuri pateikia atsakymą tokia forma:

```typescript
{
  contents: [{
    type: "text", content: "some content"
  }]
}
```

Jūsų išteklius pasiekiamas per eilutę „greeting“ ir priima parametrą `name`, bei pateikia panašų atsakymą kaip įrankis:

```typescript
{
  uri: "<href>",
  text: "a text"
}
```

#### Python

```python
# Pridėti sudėjimo įrankį
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


# Pridėti dinamišką pasveikinimo išteklių
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}!"
```

Ankstesniame kode mes:

- Apibrėžėme įrankį `add`, kuris priima parametrus `a` ir `b`, abu sveikieji skaičiai.
- Sukūrėme išteklių pavadinimu `greeting`, kuris priima parametrą `name`.

#### .NET

Pridėkite šį kodą į savo Program.cs failą:

```csharp
[McpServerToolType]
public static class CalculatorTool
{
    [McpServerTool, Description("Adds two numbers")]
    public static string Add(int a, int b) => $"Sum {a + b}";
}
```

#### Java

Įrankiai jau sukurti ankstesniame žingsnyje.

#### Rust

Pridėkite naują įrankį `impl Calculator` bloke:

```rust
#[tool(description = "Adds a and b")]
async fn add(
    &self,
    Parameters(CalculatorRequest { a, b }): Parameters<CalculatorRequest>,
) -> String {
    (a + b).to_string()
}
```

### -6- Galutinis kodas

Pridėkime paskutinį reikalingą kodą, kad serveris galėtų startuoti:

#### TypeScript

```typescript
// Pradėti gauti pranešimus per stdin ir siųsti pranešimus per stdout
const transport = new StdioServerTransport();
await server.connect(transport);
```

Čia pilnas kodas:

```typescript
// index.ts
import { McpServer, ResourceTemplate } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";

// Sukurkite MCP serverį
const server = new McpServer({
  name: "Calculator MCP Server",
  version: "1.0.0"
});

// Pridėkite papildomą įrankį
server.tool(
  "add",
  { a: z.number(), b: z.number() },
  async ({ a, b }) => ({
    content: [{ type: "text", text: String(a + b) }]
  })
);

// Pridėkite dinaminį sveikinimosi išteklių
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

// Pradėkite gauti žinutes per stdin ir siųsti žinutes per stdout
const transport = new StdioServerTransport();
server.connect(transport);
```

#### Python

```python
# server.py
from mcp.server.fastmcp import FastMCP

# Sukurkite MCP serverį
mcp = FastMCP("Demo")


# Pridėti papildomą įrankį
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


# Pridėti dinamišką pasveikinimo išteklių
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}!"

# Pagrindinė vykdymo dalis - tai būtina, kad serveris veiktų
if __name__ == "__main__":
    mcp.run()
```

#### .NET

Sukurkite Program.cs failą su tokiu turiniu:

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

Jūsų pilna pagrindinės programos klasė turėtų atrodyti taip:

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

Galutinis Rust serverio kodas turėtų atrodyti taip:

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

### -7- Serverio testavimas

Paleiskite serverį su šia komanda:

#### TypeScript

```sh
npm run build
```

#### Python

```sh
mcp run server.py
```

> Naudojant MCP Inspector, naudokite `mcp dev server.py`, kuris automatiškai paleidžia Inspector ir pateikia reikiamą proxy sesijos žetoną. Jei naudojate `mcp run server.py`, reikės rankiniu būdu paleisti Inspector ir sukonfigūruoti ryšį.

#### .NET

Įsitikinkite, kad esate savo projekto kataloge:

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

Vykdykite šias komandas sukonstravimui ir serverio paleidimui:

```sh
cargo fmt
cargo run
```

### -8- Paleidimas naudojant Inspector

Inspector yra puikus įrankis, kuris gali paleisti jūsų serverį ir leidžia su juo bendrauti, kad galėtumėte testuoti, ar jis veikia. Pradėkime:

> [!NOTE]
> komanda lauke gali atrodyti kitaip, nes ji priklauso nuo jūsų paleidimo aplinkos/

#### TypeScript

```sh
npx @modelcontextprotocol/inspector node build/index.js
```

arba pridėkite į savo *package.json* panašiai: `"inspector": "npx @modelcontextprotocol/inspector node build/index.js"` ir tada vykdykite `npm run inspector`

#### Python

Python naudoja Node.js įrankį inspector. Galima paleisti šį įrankį taip:

```sh
mcp dev server.py
```

Tačiau jis nepalaiko visų metodų, prieinamų šioje priemonėje, tad rekomenduojama tiesiogiai paleisti Node.js įrankį, kaip parodyta žemiau:

```sh
npx @modelcontextprotocol/inspector mcp run server.py
```

Jei naudojate įrankį ar IDE, kuris leidžia konfigūruoti komandų paleidimą bei argumentus,
įsitikinkite, kad `Command` laukelyje yra nustatytas `python`, o kaip „Arguments“ – `server.py`. Tai užtikrina, kad scenarijus veiktų tinkamai.

#### .NET

Įsitikinkite, kad esate savo projekto kataloge:

```sh
cd McpCalculatorServer
npx @modelcontextprotocol/inspector dotnet run
```

#### Java

Įsitikinkite, kad jūsų skaičiuotuvo serveris veikia
Tada paleiskite inspektorių:

```cmd
npx @modelcontextprotocol/inspector
```

Inspektoriaus žiniatinklio sąsajoje:

1. Pasirinkite „SSE“ kaip transporto tipą
2. Nustatykite URL į: `http://localhost:8080/sse`
3. Spustelėkite „Connect“

![Connect](../../../../translated_images/lt/tool.163d33e3ee307e20.webp)

**Dabar esate prisijungę prie serverio**
**Java serverio testavimo skiltis dabar baigta**

Kitas skyrius skirtas sąveikai su serveriu.

Turėtumėte matyti tokią vartotojo sąsają:

![Connect](../../../../translated_images/lt/connect.141db0b2bd05f096.webp)

1. Prisijunkite prie serverio pasirinkdami mygtuką Connect
  Prisijungus prie serverio, turėtumėte pamatyti tai:

  ![Connected](../../../../translated_images/lt/connected.73d1e042c24075d3.webp)

1. Pasirinkite „Tools“ ir „listTools“, turėtumėte matyti „Add“, pasirinkite „Add“ ir užpildykite parametro reikšmes.

  Turėtumėte pamatyti tokį atsakymą, t.y. „add“ įrankio rezultatą:

  ![Result of running add](../../../../translated_images/lt/ran-tool.a5a6ee878c1369ec.webp)

Sveikiname, jums pavyko sukurti ir paleisti savo pirmąjį serverį!

#### Rust

Norėdami paleisti Rust serverį su MCP Inspector CLI, naudokite šią komandą:

```sh
npx @modelcontextprotocol/inspector cargo run --cli --method tools/call --tool-name add --tool-arg a=1 b=2
```

### Oficialūs SDK

MCP teikia oficialius SDK kelioms programavimo kalboms:

- [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk) - palaikomas bendradarbiaujant su Microsoft
- [Java SDK](https://github.com/modelcontextprotocol/java-sdk) - palaikomas bendradarbiaujant su Spring AI
- [TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk) - oficiali TypeScript implementacija
- [Python SDK](https://github.com/modelcontextprotocol/python-sdk) - oficiali Python implementacija
- [Kotlin SDK](https://github.com/modelcontextprotocol/kotlin-sdk) - oficiali Kotlin implementacija
- [Swift SDK](https://github.com/modelcontextprotocol/swift-sdk) - palaikomas bendradarbiaujant su Loopwork AI
- [Rust SDK](https://github.com/modelcontextprotocol/rust-sdk) - oficiali Rust implementacija

## Pagrindinės Mintys

- MCP kūrimo aplinka yra paprastai įrengiama naudojant kalbai skirtus SDK
- MCP serverių kūrimas apima įrankių kūrimą ir registravimą su aiškiomis schemomis
- Testavimas ir derinimas yra būtini patikimoms MCP implementacijoms

## Pavyzdžiai

- [Java Calculator](../samples/java/calculator/README.md)
- [.Net Calculator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Calculator](../samples/javascript/README.md)
- [TypeScript Calculator](../samples/typescript/README.md)
- [Python Calculator](../../../../03-GettingStarted/samples/python)
- [Rust Calculator](../../../../03-GettingStarted/samples/rust)

## Užduotis

Sukurkite paprastą MCP serverį su jums patinkančiu įrankiu:

1. Įgyvendinkite įrankį pasirinktoje kalboje (.NET, Java, Python, TypeScript arba Rust).
2. Apibrėžkite įvesties parametrus ir grąžinimo reikšmes.
3. Paleiskite inspektorių, kad įsitikintumėte, jog serveris veikia tinkamai.
4. Išbandykite įgyvendinimą su įvairiomis įvestimis.

## Sprendimas

[Solution](./solution/README.md)

## Papildomi Šaltiniai

- [Agentų kūrimas naudojant Model Context Protocol Azure](https://learn.microsoft.com/azure/developer/ai/intro-agents-mcp)
- [Nuotolinis MCP su Azure Container Apps (Node.js/TypeScript/JavaScript)](https://learn.microsoft.com/samples/azure-samples/mcp-container-ts/mcp-container-ts/)
- [.NET OpenAI MCP Agent](https://learn.microsoft.com/samples/azure-samples/openai-mcp-agent-dotnet/openai-mcp-agent-dotnet/)

## Kas toliau

Toliau: [Getting Started with MCP Clients](../02-client/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome turėti omenyje, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojamas profesionalus žmogaus atliekamas vertimas. Mes neatsakome už jokius nesusipratimus ar neteisingą interpretaciją, kylančią naudojant šį vertimą.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->