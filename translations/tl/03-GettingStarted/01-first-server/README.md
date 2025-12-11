<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8fdac7600a5f4722643d0f14e15ac259",
  "translation_date": "2025-12-11T07:28:44+00:00",
  "source_file": "03-GettingStarted/01-first-server/README.md",
  "language_code": "tl"
}
-->
# Pagsisimula sa MCP

Maligayang pagdating sa iyong mga unang hakbang sa Model Context Protocol (MCP)! Kung bago ka sa MCP o nais mong palalimin ang iyong kaalaman, gagabayan ka ng gabay na ito sa mahahalagang setup at proseso ng pag-develop. Matutuklasan mo kung paano pinapadali ng MCP ang tuloy-tuloy na integrasyon sa pagitan ng mga AI model at mga aplikasyon, at matutunan kung paano mabilis na ihanda ang iyong kapaligiran para sa pagbuo at pagsubok ng mga solusyong pinapagana ng MCP.

> TLDR; Kung gumagawa ka ng mga AI app, alam mo na maaari kang magdagdag ng mga tool at iba pang mga mapagkukunan sa iyong LLM (large language model), upang maging mas may kaalaman ang LLM. Gayunpaman, kung ilalagay mo ang mga tool at mapagkukunang iyon sa isang server, ang kakayahan ng app at server ay maaaring magamit ng anumang kliyente na may o walang LLM.

## Pangkalahatang-ideya

Nagbibigay ang araling ito ng praktikal na gabay sa pag-setup ng mga MCP environment at pagbuo ng iyong mga unang MCP application. Matututuhan mo kung paano i-setup ang mga kinakailangang tool at framework, bumuo ng mga basic MCP server, gumawa ng mga host application, at subukan ang iyong mga implementasyon.

Ang Model Context Protocol (MCP) ay isang bukas na protocol na nagtatakda kung paano nagbibigay ng konteksto ang mga aplikasyon sa mga LLM. Isipin ang MCP bilang isang USB-C port para sa mga AI application - nagbibigay ito ng isang standard na paraan upang ikonekta ang mga AI model sa iba't ibang mga pinagkukunan ng data at mga tool.

## Mga Layunin sa Pagkatuto

Sa pagtatapos ng araling ito, magagawa mong:

- Mag-setup ng mga development environment para sa MCP sa C#, Java, Python, TypeScript, at Rust
- Bumuo at mag-deploy ng mga basic MCP server na may custom na mga tampok (mga resources, prompts, at tools)
- Gumawa ng mga host application na kumokonekta sa mga MCP server
- Subukan at i-debug ang mga implementasyon ng MCP

## Pag-setup ng Iyong MCP Environment

Bago ka magsimulang magtrabaho sa MCP, mahalagang ihanda ang iyong development environment at maunawaan ang pangunahing workflow. Gagabayan ka ng seksyong ito sa mga unang hakbang ng setup upang matiyak ang maayos na pagsisimula sa MCP.

### Mga Kinakailangan

Bago sumabak sa pag-develop ng MCP, siguraduhing mayroon kang:

- **Development Environment**: Para sa iyong napiling wika (C#, Java, Python, TypeScript, o Rust)
- **IDE/Editor**: Visual Studio, Visual Studio Code, IntelliJ, Eclipse, PyCharm, o anumang modernong code editor
- **Package Managers**: NuGet, Maven/Gradle, pip, npm/yarn, o Cargo
- **API Keys**: Para sa anumang AI services na balak mong gamitin sa iyong mga host application

## Pangunahing Estruktura ng MCP Server

Karaniwang kasama sa isang MCP server ang:

- **Server Configuration**: Setup ng port, authentication, at iba pang mga setting
- **Resources**: Data at konteksto na ibinibigay sa mga LLM
- **Tools**: Mga functionality na maaaring tawagin ng mga modelo
- **Prompts**: Mga template para sa pagbuo o pag-istruktura ng teksto

Narito ang isang pinasimpleng halimbawa sa TypeScript:

```typescript
import { McpServer, ResourceTemplate } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";

// Gumawa ng isang MCP server
const server = new McpServer({
  name: "Demo",
  version: "1.0.0"
});

// Magdagdag ng isang karagdagang tool
server.tool("add",
  { a: z.number(), b: z.number() },
  async ({ a, b }) => ({
    content: [{ type: "text", text: String(a + b) }]
  })
);

// Magdagdag ng isang dynamic na resource ng pagbati
server.resource(
  "file",
  // Kinokontrol ng parameter na 'list' kung paano inililista ng resource ang mga available na file. Ang pagtatakda nito sa undefined ay nagdi-disable ng paglista para sa resource na ito.
  new ResourceTemplate("file://{path}", { list: undefined }),
  async (uri, { path }) => ({
    contents: [{
      uri: uri.href,
      text: `File, ${path}!`
    }]
  })
);

// Magdagdag ng isang file resource na nagbabasa ng nilalaman ng file
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

// Simulan ang pagtanggap ng mga mensahe sa stdin at pagpapadala ng mga mensahe sa stdout
const transport = new StdioServerTransport();
await server.connect(transport);
```

Sa naunang code ay:

- In-import ang mga kinakailangang klase mula sa MCP TypeScript SDK.
- Gumawa at nag-configure ng bagong MCP server instance.
- Nagrehistro ng custom na tool (`calculator`) na may handler function.
- Sinimulan ang server upang makinig sa mga papasok na MCP request.

## Pagsubok at Pag-debug

Bago ka magsimulang subukan ang iyong MCP server, mahalagang maunawaan ang mga magagamit na tool at mga pinakamahusay na kasanayan sa pag-debug. Tinitiyak ng epektibong pagsubok na ang iyong server ay kumikilos ayon sa inaasahan at tumutulong sa mabilis na pagtukoy at paglutas ng mga isyu. Inilalahad ng sumusunod na seksyon ang mga inirerekomendang pamamaraan para sa pag-validate ng iyong implementasyon ng MCP.

Nagbibigay ang MCP ng mga tool upang tulungan kang subukan at i-debug ang iyong mga server:

- **Inspector tool**, ang graphical interface na ito ay nagpapahintulot sa iyo na kumonekta sa iyong server at subukan ang iyong mga tool, prompt, at resource.
- **curl**, maaari ka ring kumonekta sa iyong server gamit ang command line tool tulad ng curl o iba pang mga kliyente na maaaring gumawa at magpatakbo ng mga HTTP command.

### Paggamit ng MCP Inspector

Ang [MCP Inspector](https://github.com/modelcontextprotocol/inspector) ay isang visual testing tool na tumutulong sa iyo na:

1. **Matuklasan ang Mga Kakayahan ng Server**: Awtomatikong tuklasin ang mga available na resource, tool, at prompt
2. **Subukan ang Pagpapatakbo ng Tool**: Subukan ang iba't ibang mga parameter at makita ang mga tugon nang real-time
3. **Tingnan ang Metadata ng Server**: Suriin ang impormasyon ng server, mga schema, at mga configuration

```bash
# halimbawa ng TypeScript, pag-install at pagpapatakbo ng MCP Inspector
npx @modelcontextprotocol/inspector node build/index.js
```

Kapag pinatakbo mo ang mga utos sa itaas, magbubukas ang MCP Inspector ng lokal na web interface sa iyong browser. Maaari mong asahan na makikita ang dashboard na nagpapakita ng iyong mga nakarehistrong MCP server, ang kanilang mga available na tool, resource, at prompt. Pinapayagan ka ng interface na ito na interaktibong subukan ang pagpapatakbo ng tool, suriin ang metadata ng server, at tingnan ang mga tugon nang real-time, na nagpapadali sa pag-validate at pag-debug ng iyong mga implementasyon ng MCP server.

Narito ang isang screenshot kung ano ang maaaring hitsura nito:

![MCP Inspector server connection](../../../../translated_images/connected.73d1e042c24075d386cacdd4ee7cd748c16364c277d814e646ff2f7b5eefde85.tl.png)

## Mga Karaniwang Isyu sa Setup at Mga Solusyon

| Isyu | Posibleng Solusyon |
|-------|-------------------|
| Connection refused | Suriin kung tumatakbo ang server at tama ang port |
| Mga error sa pagpapatakbo ng tool | Suriin ang validation ng parameter at paghawak ng error |
| Mga pagkabigo sa authentication | Beripikahin ang API keys at mga permiso |
| Mga error sa schema validation | Siguraduhing tumutugma ang mga parameter sa tinukoy na schema |
| Hindi nagsisimula ang server | Suriin ang mga conflict sa port o nawawalang dependencies |
| Mga error sa CORS | I-configure nang tama ang mga CORS header para sa cross-origin requests |
| Mga isyu sa authentication | Beripikahin ang bisa ng token at mga permiso |

## Lokal na Pag-develop

Para sa lokal na pag-develop at pagsubok, maaari mong patakbuhin ang mga MCP server nang direkta sa iyong makina:

1. **Simulan ang proseso ng server**: Patakbuhin ang iyong MCP server application
2. **I-configure ang networking**: Siguraduhing naa-access ang server sa inaasahang port
3. **Kumonekta ang mga kliyente**: Gamitin ang mga lokal na URL ng koneksyon tulad ng `http://localhost:3000`

```bash
# Halimbawa: Pagpapatakbo ng isang TypeScript MCP server nang lokal
npm run start
# Server na tumatakbo sa http://localhost:3000
```

## Pagbuo ng iyong unang MCP Server

Napag-usapan na natin ang [Core concepts](/01-CoreConcepts/README.md) sa isang naunang aralin, ngayon ay panahon na upang gamitin ang kaalamang iyon.

### Ano ang magagawa ng isang server

Bago tayo magsimulang magsulat ng code, paalalahanan muna natin ang ating sarili kung ano ang magagawa ng isang server:

Ang isang MCP server ay maaaring halimbawa:

- Mag-access ng mga lokal na file at database
- Kumonekta sa mga remote API
- Magsagawa ng mga kalkulasyon
- Makipag-integrate sa iba pang mga tool at serbisyo
- Magbigay ng user interface para sa interaksyon

Maganda, ngayon na alam natin kung ano ang magagawa nito, simulan na natin ang pag-cocode.

## Ehersisyo: Paglikha ng isang server

Upang makagawa ng server, kailangan mong sundin ang mga hakbang na ito:

- I-install ang MCP SDK.
- Gumawa ng proyekto at i-setup ang estruktura ng proyekto.
- Isulat ang code ng server.
- Subukan ang server.

### -1- Gumawa ng proyekto

#### TypeScript

```sh
# Gumawa ng direktoryo ng proyekto at simulan ang npm na proyekto
mkdir calculator-server
cd calculator-server
npm init -y
```

#### Python

```sh
# Gumawa ng direktoryo ng proyekto
mkdir calculator-server
cd calculator-server
# Buksan ang folder sa Visual Studio Code - Laktawan ito kung gumagamit ka ng ibang IDE
code .
```

#### .NET

```sh
dotnet new console -n McpCalculatorServer
cd McpCalculatorServer
```

#### Java

Para sa Java, gumawa ng Spring Boot project:

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

I-extract ang zip file:

```bash
unzip calculator-server.zip -d calculator-server
cd calculator-server
# opsyonal na alisin ang hindi nagamit na pagsubok
rm -rf src/test/java
```

Idagdag ang sumusunod na kumpletong configuration sa iyong *pom.xml* file:

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

### -2- Magdagdag ng dependencies

Ngayon na nagawa mo na ang iyong proyekto, magdagdag tayo ng mga dependencies:

#### TypeScript

```sh
# Kung hindi pa naka-install, i-install ang TypeScript nang global
npm install typescript -g

# I-install ang MCP SDK at Zod para sa pag-validate ng schema
npm install @modelcontextprotocol/sdk zod
npm install -D @types/node typescript
```

#### Python

```sh
# Gumawa ng virtual na kapaligiran at i-install ang mga kinakailangang dependencies
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

### -3- Gumawa ng mga file ng proyekto

#### TypeScript

Buksan ang *package.json* file at palitan ang nilalaman nito ng sumusunod upang matiyak na maaari mong i-build at patakbuhin ang server:

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

Gumawa ng *tsconfig.json* na may sumusunod na nilalaman:

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

Gumawa ng direktoryo para sa iyong source code:

```sh
mkdir src
touch src/index.ts
```

#### Python

Gumawa ng file na *server.py*

```sh
touch server.py
```

#### .NET

I-install ang mga kinakailangang NuGet packages:

```sh
dotnet add package ModelContextProtocol --prerelease
dotnet add package Microsoft.Extensions.Hosting
```

#### Java

Para sa mga Java Spring Boot project, awtomatikong nagagawa ang estruktura ng proyekto.

#### Rust

Para sa Rust, isang *src/main.rs* file ang awtomatikong nagagawa kapag pinatakbo mo ang `cargo init`. Buksan ang file at tanggalin ang default na code.

### -4- Gumawa ng code ng server

#### TypeScript

Gumawa ng file na *index.ts* at idagdag ang sumusunod na code:

```typescript
import { McpServer, ResourceTemplate } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";
 
// Gumawa ng isang MCP server
const server = new McpServer({
  name: "Calculator MCP Server",
  version: "1.0.0"
});
```

Ngayon ay mayroon ka nang server, ngunit hindi pa ito masyadong gumagana, ayusin natin iyon.

#### Python

```python
# server.py
from mcp.server.fastmcp import FastMCP

# Gumawa ng isang MCP server
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

Para sa Java, gumawa ng mga pangunahing bahagi ng server. Una, baguhin ang pangunahing klase ng application:

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

Gumawa ng calculator service *src/main/java/com/microsoft/mcp/sample/server/service/CalculatorService.java*:

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

**Opsyonal na mga bahagi para sa production-ready na serbisyo:**

Gumawa ng startup configuration *src/main/java/com/microsoft/mcp/sample/server/config/StartupConfig.java*:

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

Gumawa ng health controller *src/main/java/com/microsoft/mcp/sample/server/controller/HealthController.java*:

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

Gumawa ng exception handler *src/main/java/com/microsoft/mcp/sample/server/exception/GlobalExceptionHandler.java*:

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

        // Mga getter
        public String getCode() { return code; }
        public String getMessage() { return message; }
    }
}
```

Gumawa ng custom banner *src/main/resources/banner.txt*:

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

Idagdag ang sumusunod na code sa itaas ng *src/main.rs* file. Ini-import nito ang mga kinakailangang library at module para sa iyong MCP server.

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

Ang calculator server ay magiging isang simple na server na maaaring magdagdag ng dalawang numero. Gumawa tayo ng struct upang irepresenta ang calculator request.

```rust
#[derive(Debug, serde::Deserialize, schemars::JsonSchema)]
pub struct CalculatorRequest {
    pub a: f64,
    pub b: f64,
}
```

Sunod, gumawa ng struct upang irepresenta ang calculator server. Ang struct na ito ay maglalaman ng tool router, na ginagamit upang magrehistro ng mga tool.

```rust
#[derive(Debug, Clone)]
pub struct Calculator {
    tool_router: ToolRouter<Self>,
}
```

Ngayon, maaari nating i-implement ang `Calculator` struct upang gumawa ng bagong instance ng server at i-implement ang server handler upang magbigay ng impormasyon tungkol sa server.

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

Sa wakas, kailangan nating i-implement ang main function upang simulan ang server. Ang function na ito ay gagawa ng instance ng `Calculator` struct at maglilingkod gamit ang standard input/output.

```rust
#[tokio::main]
async fn main() -> Result<(), Box<dyn Error>> {
    let service = Calculator::new().serve(stdio()).await?;
    service.waiting().await?;
    Ok(())
}
```

Naka-setup na ang server upang magbigay ng pangunahing impormasyon tungkol sa sarili nito. Sunod, magdadagdag tayo ng tool para magsagawa ng addition.

### -5- Pagdaragdag ng tool at resource

Magdagdag ng tool at resource sa pamamagitan ng pagdagdag ng sumusunod na code:

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

Ang iyong tool ay tumatanggap ng mga parameter na `a` at `b` at nagpapatakbo ng function na gumagawa ng tugon sa porma ng:

```typescript
{
  contents: [{
    type: "text", content: "some content"
  }]
}
```

Ang iyong resource ay naa-access sa pamamagitan ng string na "greeting" at tumatanggap ng parameter na `name` at gumagawa ng katulad na tugon sa tool:

```typescript
{
  uri: "<href>",
  text: "a text"
}
```

#### Python

```python
# Magdagdag ng isang tool para sa pagdaragdag
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


# Magdagdag ng isang dynamic na mapagkukunan ng pagbati
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}!"
```

Sa naunang code ay:

- Tinukoy ang tool na `add` na tumatanggap ng mga parameter na `a` at `b`, parehong integer.
- Gumawa ng resource na tinatawag na `greeting` na tumatanggap ng parameter na `name`.

#### .NET

Idagdag ito sa iyong Program.cs file:

```csharp
[McpServerToolType]
public static class CalculatorTool
{
    [McpServerTool, Description("Adds two numbers")]
    public static string Add(int a, int b) => $"Sum {a + b}";
}
```

#### Java

Nagawa na ang mga tool sa naunang hakbang.

#### Rust

Magdagdag ng bagong tool sa loob ng `impl Calculator` block:

```rust
#[tool(description = "Adds a and b")]
async fn add(
    &self,
    Parameters(CalculatorRequest { a, b }): Parameters<CalculatorRequest>,
) -> String {
    (a + b).to_string()
}
```

### -6- Panghuling code

Idagdag natin ang huling code na kailangan upang makapagsimula ang server:

#### TypeScript

```typescript
// Simulan ang pagtanggap ng mga mensahe sa stdin at pagpapadala ng mga mensahe sa stdout
const transport = new StdioServerTransport();
await server.connect(transport);
```

Narito ang buong code:

```typescript
// index.ts
import { McpServer, ResourceTemplate } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";

// Gumawa ng isang MCP server
const server = new McpServer({
  name: "Calculator MCP Server",
  version: "1.0.0"
});

// Magdagdag ng isang tool para sa pagdaragdag
server.tool(
  "add",
  { a: z.number(), b: z.number() },
  async ({ a, b }) => ({
    content: [{ type: "text", text: String(a + b) }]
  })
);

// Magdagdag ng isang dynamic na resource para sa pagbati
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

// Simulan ang pagtanggap ng mga mensahe sa stdin at pagpapadala ng mga mensahe sa stdout
const transport = new StdioServerTransport();
server.connect(transport);
```

#### Python

```python
# server.py
from mcp.server.fastmcp import FastMCP

# Gumawa ng isang MCP server
mcp = FastMCP("Demo")


# Magdagdag ng isang tool para sa pagdaragdag
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


# Magdagdag ng isang dynamic na mapagkukunan ng pagbati
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}!"

# Pangunahing bloke ng pagpapatupad - ito ay kinakailangan upang patakbuhin ang server
if __name__ == "__main__":
    mcp.run()
```

#### .NET

Gumawa ng Program.cs file na may sumusunod na nilalaman:

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

Ang iyong kumpletong pangunahing klase ng application ay dapat ganito ang hitsura:

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

Ang panghuling code para sa Rust server ay dapat ganito ang hitsura:

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

### -7- Subukan ang server

Simulan ang server gamit ang sumusunod na utos:

#### TypeScript

```sh
npm run build
```

#### Python

```sh
mcp run server.py
```

> Upang gamitin ang MCP Inspector, gamitin ang `mcp dev server.py` na awtomatikong naglulunsad ng Inspector at nagbibigay ng kinakailangang proxy session token. Kung gumagamit ng `mcp run server.py`, kailangan mong manu-manong simulan ang Inspector at i-configure ang koneksyon.

#### .NET

Siguraduhing nasa loob ka ng iyong project directory:

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

Patakbuhin ang mga sumusunod na utos upang i-format at patakbuhin ang server:

```sh
cargo fmt
cargo run
```

### -8- Patakbuhin gamit ang inspector

Ang inspector ay isang mahusay na tool na maaaring magsimula ng iyong server at pinapayagan kang makipag-ugnayan dito upang masubukan kung gumagana ito. Simulan natin ito:

> [!NOTE]
> maaaring mag-iba ang hitsura sa "command" field dahil naglalaman ito ng utos para patakbuhin ang server gamit ang iyong partikular na runtime/

#### TypeScript

```sh
npx @modelcontextprotocol/inspector node build/index.js
```

o idagdag ito sa iyong *package.json* tulad nito: `"inspector": "npx @modelcontextprotocol/inspector node build/index.js"` at pagkatapos ay patakbuhin ang `npm run inspector`

#### Python

Ang Python ay nagra-wrap ng isang Node.js tool na tinatawag na inspector. Posibleng tawagin ang nasabing tool tulad nito:

```sh
mcp dev server.py
```

Gayunpaman, hindi nito naipapatupad ang lahat ng mga method na available sa tool kaya inirerekomenda kang patakbuhin ang Node.js tool nang direkta tulad ng nasa ibaba:

```sh
npx @modelcontextprotocol/inspector mcp run server.py
```

Kung gumagamit ka ng tool o IDE na nagpapahintulot sa iyo na i-configure ang mga command at argumento para sa pagpapatakbo ng mga script,
siguraduhing itakda ang `python` sa `Command` na patlang at `server.py` bilang `Arguments`. Tinitiyak nito na tatakbo nang tama ang script.

#### .NET

Siguraduhing nasa direktoryo ng iyong proyekto ka:

```sh
cd McpCalculatorServer
npx @modelcontextprotocol/inspector dotnet run
```

#### Java

Tiyaking tumatakbo ang iyong calculator server
Pagkatapos patakbuhin ang inspector:

```cmd
npx @modelcontextprotocol/inspector
```

Sa web interface ng inspector:

1. Piliin ang "SSE" bilang uri ng transport
2. Itakda ang URL sa: `http://localhost:8080/sse`
3. I-click ang "Connect"

![Connect](../../../../translated_images/tool.163d33e3ee307e209ef146d8f85060d2f7e83e9f59b3b1699a77204ae0454ad2.tl.png)

**Konektado ka na ngayon sa server**
**Natapos na ang seksyon ng pagsubok sa Java server**

Ang susunod na seksyon ay tungkol sa pakikipag-ugnayan sa server.

Dapat mong makita ang sumusunod na user interface:

![Connect](../../../../translated_images/connect.141db0b2bd05f096fb1dd91273771fd8b2469d6507656c3b0c9df4b3c5473929.tl.png)

1. Kumonekta sa server sa pamamagitan ng pagpili sa Connect button
  Kapag nakakonekta ka na sa server, dapat mong makita ang sumusunod:

  ![Connected](../../../../translated_images/connected.73d1e042c24075d386cacdd4ee7cd748c16364c277d814e646ff2f7b5eefde85.tl.png)

1. Piliin ang "Tools" at "listTools", dapat lumabas ang "Add", piliin ang "Add" at punan ang mga halaga ng parameter.

  Dapat mong makita ang sumusunod na tugon, ibig sabihin ay resulta mula sa "add" tool:

  ![Result of running add](../../../../translated_images/ran-tool.a5a6ee878c1369ec1e379b81053395252a441799dbf23416c36ddf288faf8249.tl.png)

Congrats, nagawa mo nang likhain at patakbuhin ang iyong unang server!

#### Rust

Upang patakbuhin ang Rust server gamit ang MCP Inspector CLI, gamitin ang sumusunod na utos:

```sh
npx @modelcontextprotocol/inspector cargo run --cli --method tools/call --tool-name add --tool-arg a=1 b=2
```

### Opisyal na SDKs

Nagbibigay ang MCP ng opisyal na SDKs para sa iba't ibang wika:

- [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk) - Pinapanatili sa pakikipagtulungan sa Microsoft
- [Java SDK](https://github.com/modelcontextprotocol/java-sdk) - Pinapanatili sa pakikipagtulungan sa Spring AI
- [TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk) - Ang opisyal na implementasyon ng TypeScript
- [Python SDK](https://github.com/modelcontextprotocol/python-sdk) - Ang opisyal na implementasyon ng Python
- [Kotlin SDK](https://github.com/modelcontextprotocol/kotlin-sdk) - Ang opisyal na implementasyon ng Kotlin
- [Swift SDK](https://github.com/modelcontextprotocol/swift-sdk) - Pinapanatili sa pakikipagtulungan sa Loopwork AI
- [Rust SDK](https://github.com/modelcontextprotocol/rust-sdk) - Ang opisyal na implementasyon ng Rust

## Mga Pangunahing Punto

- Ang pagsasaayos ng MCP development environment ay diretso gamit ang mga language-specific SDKs
- Ang paggawa ng MCP servers ay kinabibilangan ng paglikha at pagrerehistro ng mga tools na may malinaw na mga schema
- Mahalaga ang pagsubok at pag-debug para sa maaasahang mga implementasyon ng MCP

## Mga Halimbawa

- [Java Calculator](../samples/java/calculator/README.md)
- [.Net Calculator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Calculator](../samples/javascript/README.md)
- [TypeScript Calculator](../samples/typescript/README.md)
- [Python Calculator](../../../../03-GettingStarted/samples/python)
- [Rust Calculator](../../../../03-GettingStarted/samples/rust)

## Takdang-Aralin

Gumawa ng isang simpleng MCP server na may tool na iyong pipiliin:

1. Ipatupad ang tool sa iyong gustong wika (.NET, Java, Python, TypeScript, o Rust).
2. Tukuyin ang mga input parameter at mga return value.
3. Patakbuhin ang inspector tool upang matiyak na gumagana ang server ayon sa inaasahan.
4. Subukan ang implementasyon gamit ang iba't ibang mga input.

## Solusyon

[Solution](./solution/README.md)

## Karagdagang Mga Mapagkukunan

- [Build Agents using Model Context Protocol on Azure](https://learn.microsoft.com/azure/developer/ai/intro-agents-mcp)
- [Remote MCP with Azure Container Apps (Node.js/TypeScript/JavaScript)](https://learn.microsoft.com/samples/azure-samples/mcp-container-ts/mcp-container-ts/)
- [.NET OpenAI MCP Agent](https://learn.microsoft.com/samples/azure-samples/openai-mcp-agent-dotnet/openai-mcp-agent-dotnet/)

## Ano ang susunod

Susunod: [Getting Started with MCP Clients](../02-client/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Paalala**:
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagamat nagsusumikap kami para sa katumpakan, pakatandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o di-tumpak na impormasyon. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na maaaring magmula sa paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->