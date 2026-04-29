# Pagsisimula sa MCP

Maligayang pagdating sa iyong mga unang hakbang gamit ang Model Context Protocol (MCP)! Kung bago ka sa MCP o nais mong palalimin ang iyong pag-unawa, gagabayan ka ng gabay na ito sa mahalagang proseso ng setup at pagbuo. Malalaman mo kung paano pinapagana ng MCP ang seamless integration sa pagitan ng AI models at mga aplikasyon, at matututo kung paano mabilis na ihanda ang iyong kapaligiran para sa pagbuo at pagsubok ng mga solusyong pinapatakbo ng MCP.

> TLDR; Kung bumubuo ka ng AI apps, alam mo na maaari kang magdagdag ng mga tools at iba pang mga resources sa iyong LLM (large language model), upang maging mas knowledgeable ang LLM. Gayunpaman, kung ilalagay mo ang mga tools at resources na iyon sa isang server, ang kakayahan ng app at server ay maaaring magamit ng anumang kliyente kahit may o walang LLM.

## Pangkalahatang-ideya

Ang araling ito ay nagbibigay ng praktikal na gabay sa pag-set up ng mga MCP environment at pagbuo ng iyong mga unang MCP application. Matututuhan mo kung paano i-set up ang kinakailangang mga tools at frameworks, bumuo ng batayang MCP servers, lumikha ng mga host application, at subukan ang iyong mga implementasyon.

Ang Model Context Protocol (MCP) ay isang bukas na protocol na nag-standardize kung paano nagbibigay ang mga aplikasyon ng konteksto sa LLMs. Isipin ang MCP bilang isang USB-C port para sa mga AI application - nagbibigay ito ng isang standardized na paraan para ikonekta ang mga AI model sa iba't ibang data sources at tools.

## Mga Layuning Pangkatuto

Sa pagtatapos ng araling ito, magagawa mong:

- Mag-set up ng development environment para sa MCP gamit ang C#, Java, Python, TypeScript, at Rust
- Bumuo at mag-deploy ng mga batayang MCP server na may custom na mga tampok (resources, prompts, at tools)
- Lumikha ng mga host application na nakakonekta sa MCP servers
- Subukan at i-debug ang mga implementasyon ng MCP

## Pag-set Up ng Iyong MCP Environment

Bago ka magsimulang magtrabaho gamit ang MCP, mahalagang ihanda ang iyong development environment at maunawaan ang pangunahing workflow. Gabayan ka ng seksyong ito sa mga unang hakbang ng setup upang matiyak ang maayos na pagsisimula gamit ang MCP.

### Mga Kinakailangan

Bago sumabak sa MCP development, tiyaking mayroon ka ng:

- **Development Environment**: Para sa napili mong wika (C#, Java, Python, TypeScript, o Rust)
- **IDE/Editor**: Visual Studio, Visual Studio Code, IntelliJ, Eclipse, PyCharm, o anumang modernong code editor
- **Package Managers**: NuGet, Maven/Gradle, pip, npm/yarn, o Cargo
- **API Keys**: Para sa anumang AI services na plano mong gamitin sa iyong mga host application

## Pangunahing Istruktura ng MCP Server

Kadalasang kasama sa isang MCP server ang:

- **Server Configuration**: Setup ng port, authentication, at iba pang settings
- **Resources**: Data at kontekstong ibinibigay sa LLMs
- **Tools**: Mga functionality na maaaring tawagin ng mga modelo
- **Prompts**: Mga templates para sa pag-generate o pag-istraktura ng teksto

Narito ang isang pinaikling halimbawa sa TypeScript:

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

// Magdagdag ng isang dynamic na mapagkukunan ng pagbati
server.resource(
  "file",
  // Kinokontrol ng parameter na 'list' kung paano inililista ng resource ang mga available na file. Ang pagtatakda nito sa undefined ay nagdi-disable ng listing para sa resource na ito.
  new ResourceTemplate("file://{path}", { list: undefined }),
  async (uri, { path }) => ({
    contents: [{
      uri: uri.href,
      text: `File, ${path}!`
    }]
  })
);

// Magdagdag ng file resource na nagbabasa ng mga nilalaman ng file
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
- Nilikha at na-configure ang isang bagong MCP server instance.
- Nirehistro ang isang custom na tool (`calculator`) na may handler function.
- Sinimulan ang server upang makinig sa mga papasok na MCP request.

## Pagsubok at Pag-debug

Bago ka magsimulang subukan ang iyong MCP server, mahalagang maunawaan ang mga magagamit na tools at mga pinakamahusay na kasanayan sa pag-debug. Ang epektibong pagsusuri ay nagsisiguro na kumikilos ang iyong server ayon sa inaasahan at tumutulong sa mabilisang pagtukoy at paglutas ng mga isyu. Ipinapaliwanag sa susunod na seksyon ang mga inirekumendang paraan ng pag-validate ng iyong implementasyon ng MCP.

Nagbibigay ang MCP ng mga tool upang tulungan kang subukin at i-debug ang iyong mga server:

- **Inspector tool**, isang graphical interface na nagpapahintulot sa iyo na kumonekta sa iyong server at subukin ang iyong mga tools, prompts at resources.
- **curl**, maaari ka ring kumonekta sa iyong server gamit ang command line tool tulad ng curl o iba pang kliyente na maaaring gumawa at magpatakbo ng mga HTTP command.

### Paggamit ng MCP Inspector

Ang [MCP Inspector](https://github.com/modelcontextprotocol/inspector) ay isang visual testing tool na tumutulong sa iyo na:

1. **Tuklasin ang Mga Kakayahan ng Server**: Awtomatikong matuklasan ang mga magagamit na resources, tools, at prompts
2. **Subukan ang Pagpapatakbo ng Tool**: Subukan ang iba't ibang mga parametera at makita ang mga tugon nang real-time
3. **Tingnan ang Metadata ng Server**: Suriin ang impormasyon ng server, mga schema, at configuration

```bash
# halimbawa ng TypeScript, pag-install at pagpapatakbo ng MCP Inspector
npx @modelcontextprotocol/inspector node build/index.js
```

Kapag pinatakbo mo ang mga utos sa itaas, magsisimula ang MCP Inspector ng lokal na web interface sa iyong browser. Inaasahan mong makikita ang isang dashboard na nagpapakita ng iyong mga rehistradong MCP server, mga magagamit nitong tools, resources, at prompts. Pinapahintulutan ka ng interface na subukin nang interactive ang pagpapatakbo ng mga tool, inspeksyunin ang metadata ng server, at makita ang mga tugon nang real-time, na nagpapadali sa pag-validate at pag-debug ng iyong mga implementasyon ng MCP server.

Narito ang isang screenshot kung ano ang itsura nito:

![MCP Inspector server connection](../../../../translated_images/tl/connected.73d1e042c24075d3.webp)

## Karaniwang Mga Isyu sa Setup at Mga Solusyon

| Isyu | Posibleng Solusyon |
|-------|-------------------|
| Connection refused | Suriin kung tumatakbo ang server at tama ang port |
| Mga error sa pagpapatakbo ng tool | Suriin ang validation ng mga parameter at error handling |
| Pagkabigo sa authentication | Beripikahin ang mga API key at permiso |
| Mga error sa schema validation | Siguraduhing tugma ang mga parameter sa tinukoy na schema |
| Hindi nagsisimulang server | Suriin ang mga conflict sa port o mga nawawalang dependencies |
| Mga error sa CORS | I-configure nang tama ang mga CORS header para sa cross-origin requests |
| Mga isyu sa authentication | Siguraduhing valid ang token at mga permiso |

## Lokal na Development

Para sa lokal na development at pagsubok, maaari mong patakbuhin ang mga MCP server nang direkta sa iyong makina:

1. **Simulan ang proseso ng server**: Patakbuhin ang iyong MCP server application
2. **I-configure ang networking**: Siguraduhing accessible ang server sa inaasahang port
3. **Ikonekta ang mga client**: Gamitin ang mga lokal na URL tulad ng `http://localhost:3000`

```bash
# Halimbawa: Pagpapatakbo ng TypeScript MCP server nang lokal
npm run start
# Naka-run ang server sa http://localhost:3000
```

## Pagbuo ng iyong unang MCP Server

Napag-usapan na natin ang [Mga Core Concept](../../01-CoreConcepts/README.md) sa naunang aralin, ngayon ay panahon na para gamitin ang kaalaman na iyon.

### Ano ang magagawa ng isang server

Bago tayo magsulat ng code, alalahanin muna natin kung ano ang magagawa ng isang server:

Halimbawa, ang isang MCP server ay maaaring:

- Mag-access ng mga lokal na file at database
- Kumonekta sa mga remote API
- Magsagawa ng mga computation
- Makipag-integrate sa ibang mga tool at serbisyo
- Magbigay ng user interface para sa interaksyon

Magandang bagay, ngayon na alam natin kung ano ang magagawa natin para dito, simulan na natin ang pag-cocode.

## Ehersisyo: Paggawa ng server

Para gumawa ng server, kailangan mong sundin ang mga hakbang na ito:

- I-install ang MCP SDK.
- Gumawa ng proyekto at i-set up ang istruktura ng proyekto.
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
# opsyonal alisin ang hindi nagamit na pagsubok
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

Ngayon na nagawa mo na ang proyekto, magdagdag tayo ng dependencies:

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

Gumawa ng directory para sa iyong source code:

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

Para sa mga Java Spring Boot project, awtomatikong ginagawa ang istruktura ng proyekto.

#### Rust

Para sa Rust, ang *src/main.rs* na file ay awtomatikong nalilikha kapag pinatakbo mo ang `cargo init`. Buksan ang file at tanggalin ang default na code.

### -4- Gumawa ng code ng server

#### TypeScript

Gumawa ng file na *index.ts* at idagdag ang sumusunod na code:

```typescript
import { McpServer, ResourceTemplate } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";
 
// Gumawa ng MCP server
const server = new McpServer({
  name: "Calculator MCP Server",
  version: "1.0.0"
});
```

Ngayon ay mayroon ka nang server, ngunit hindi pa ito gaanong gumagana, aayusin natin iyon.

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

Para sa Java, gumawa ng pangunahing bahagi ng server. Una, baguhin ang pangunahing klase ng application:

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

Idagdag ang sumusunod na code sa taas ng *src/main.rs* file. Ikinakarga nito ang mga kinakailangang library at mga module para sa iyong MCP server.

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

Ang calculator server ay magiging isang simple lamang na makakapagdagdag ng dalawang numero. Gumawa tayo ng struct para irepresenta ang calculator request.

```rust
#[derive(Debug, serde::Deserialize, schemars::JsonSchema)]
pub struct CalculatorRequest {
    pub a: f64,
    pub b: f64,
}
```

Susunod, gumawa ng struct para irepresenta ang calculator server. Hahawakan ng struct na ito ang tool router, na ginagamit para magrehistro ng mga tool.

```rust
#[derive(Debug, Clone)]
pub struct Calculator {
    tool_router: ToolRouter<Self>,
}
```

Ngayon, maaari nating i-implement ang `Calculator` struct para gumawa ng bagong instance ng server at iimplement ang server handler para magbigay ng impormasyon tungkol sa server.

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

Panghuli, kailangan nating iimplement ang main function para simulan ang server. Gumagawa ito ng instance ng `Calculator` struct at naglilingkod gamit ang standard input/output.

```rust
#[tokio::main]
async fn main() -> Result<(), Box<dyn Error>> {
    let service = Calculator::new().serve(stdio()).await?;
    service.waiting().await?;
    Ok(())
}
```

Nai-set up na ang server upang magbigay ng batayang impormasyon tungkol sa sarili nito. Susunod, magdadagdag tayo ng tool para gumawa ng addition.

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

Tumatanggap ang iyong tool ng mga parametro `a` at `b` at nagpapatakbo ng isang function na gumagawa ng tugon na may anyo:

```typescript
{
  contents: [{
    type: "text", content: "some content"
  }]
}
```

Ang iyong resource ay naa-access sa pamamagitan ng string na "greeting" at tumatanggap ng parametro `name` at gumagawa ng katulad na tugon sa tool:

```typescript
{
  uri: "<href>",
  text: "a text"
}
```

#### Python

```python
# Magdagdag ng isang tool sa pagdadagdag
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


# Magdagdag ng isang dinamiko na resource para sa pagbati
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}!"
```

Sa naunang code ay:

- Nag-declare ng tool na `add` na tumatanggap ng mga parameter `a` at `b`, parehong mga integer.
- Gumawa ng resource na `greeting` na tumatanggap ng parametro `name`.

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

Nalikha na ang mga tool sa nakaraang hakbang.

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

Idagdag natin ang huling code na kailangan natin upang makapagsimula ang server:

#### TypeScript

```typescript
// Magsimula ng pagtanggap ng mga mensahe sa stdin at pagpapadala ng mga mensahe sa stdout
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

// Magdagdag ng isang tool para sa pagdadagdag
server.tool(
  "add",
  { a: z.number(), b: z.number() },
  async ({ a, b }) => ({
    content: [{ type: "text", text: String(a + b) }]
  })
);

// Magdagdag ng isang dynamic na mapagkukunan ng pagbati
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


# Magdagdag ng karagdagang tool
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


# Magdagdag ng isang dynamic na greeting resource
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

Dapat ganito ang hitsura ng iyong kumpletong main application class:

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

Ganito ang magiging hitsura ng panghuling code para sa Rust server:

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

> Para gamitin ang MCP Inspector, gamitin ang `mcp dev server.py` na awtomatikong naglulunsad ng Inspector at nagbibigay ng kinakailangang proxy session token. Kung gumagamit ng `mcp run server.py`, kailangan mong manu-manong simulan ang Inspector at i-configure ang koneksyon.

#### .NET

Siguraduhing nasa directory ka ng iyong proyekto:

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

Patakbuhin ang sumusunod na mga utos upang i-format at patakbuhin ang server:

```sh
cargo fmt
cargo run
```

### -8- Patakbuhin gamit ang inspector

Ang inspector ay isang mahusay na tool na maaaring magsimula ng iyong server at payagan kang makipag-ugnayan dito upang masubukan mo kung gumagana ito. Simulan natin ito:

> [!NOTE]
> Maaaring iba ang itsura sa field na "command" dahil naglalaman ito ng utos para patakbuhin ang server gamit ang iyong partikular na runtime.

#### TypeScript

```sh
npx @modelcontextprotocol/inspector node build/index.js
```

o idagdag ito sa iyong *package.json* ng ganito: `"inspector": "npx @modelcontextprotocol/inspector node build/index.js"` pagkatapos ay patakbuhin `npm run inspector`

#### Python

Naka-wrap ang Python sa isang Node.js tool na tinatawag na inspector. Posibleng tawagin ang nasabing tool nang ganito:

```sh
mcp dev server.py
```

Gayunpaman, hindi nito naipapatupad ang lahat ng mga method na available sa tool kaya inirerekomenda na patakbuhin mo ang Node.js tool nang direkta tulad ng nasa ibaba:

```sh
npx @modelcontextprotocol/inspector mcp run server.py
```

Kung gumagamit ka ng tool o IDE na nagpapahintulot sa pag-configure ng mga utos at argumento para sa pagpapatakbo ng mga script,
siguraduhing itakda ang `python` sa `Command` field at `server.py` bilang `Arguments`. Tinitiyak nito na tumatakbo nang tama ang script.

#### .NET

Siguraduhing nasa iyong project directory ka:

```sh
cd McpCalculatorServer
npx @modelcontextprotocol/inspector dotnet run
```

#### Java

Tiyaking tumatakbo ang iyong calculator server
Pagkatapos, patakbuhin ang inspector:

```cmd
npx @modelcontextprotocol/inspector
```

Sa inspector web interface:

1. Piliin ang "SSE" bilang uri ng transport
2. Itakda ang URL sa: `http://localhost:8080/sse`
3. I-click ang "Connect"

![Connect](../../../../translated_images/tl/tool.163d33e3ee307e20.webp)

**Ikaw ay nakakonekta na sa server**
**Ang seksyon ng pagsubok sa Java server ay natapos na**

Ang susunod na seksyon ay tungkol sa pakikipag-ugnayan sa server.

Dapat mong makita ang sumusunod na user interface:

![Connect](../../../../translated_images/tl/connect.141db0b2bd05f096.webp)

1. Kumonekta sa server sa pamamagitan ng pagpili sa Connect na button
  Kapag nakakonekta ka na sa server, dapat mong makita ang sumusunod:

  ![Connected](../../../../translated_images/tl/connected.73d1e042c24075d3.webp)

1. Piliin ang "Tools" at "listTools", dapat lumabas ang "Add", piliin ang "Add" at punan ang mga halaga ng parameter.

  Dapat mong makita ang sumusunod na tugon, i.e. isang resulta mula sa "add" tool:

  ![Result of running add](../../../../translated_images/tl/ran-tool.a5a6ee878c1369ec.webp)

Binabati kita, nagawa mong lumikha at patakbuhin ang iyong unang server!

#### Rust

Upang patakbuhin ang Rust server gamit ang MCP Inspector CLI, gamitin ang sumusunod na utos:

```sh
npx @modelcontextprotocol/inspector cargo run --cli --method tools/call --tool-name add --tool-arg a=1 b=2
```

### Official SDKs

Nagbibigay ang MCP ng opisyal na SDKs para sa iba't ibang mga wika:

- [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk) - Pinapanatili kasama ang Microsoft
- [Java SDK](https://github.com/modelcontextprotocol/java-sdk) - Pinapanatili kasama ang Spring AI
- [TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk) - Ang opisyal na implementasyon ng TypeScript
- [Python SDK](https://github.com/modelcontextprotocol/python-sdk) - Ang opisyal na implementasyon ng Python
- [Kotlin SDK](https://github.com/modelcontextprotocol/kotlin-sdk) - Ang opisyal na implementasyon ng Kotlin
- [Swift SDK](https://github.com/modelcontextprotocol/swift-sdk) - Pinapanatili kasama ang Loopwork AI
- [Rust SDK](https://github.com/modelcontextprotocol/rust-sdk) - Ang opisyal na implementasyon ng Rust

## Pangunahing Mga Punto

- Ang pagsasaayos ng MCP development environment ay diretso sa pamamagitan ng mga language-specific na SDKs
- Ang paggawa ng MCP servers ay kinabibilangan ng paglikha at pagrerehistro ng mga tools na may malinaw na mga schema
- Mahalaga ang pagsubok at pag-debug para sa maaasahang mga MCP na implementasyon

## Mga Sample

- [Java Calculator](../samples/java/calculator/README.md)
- [.Net Calculator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Calculator](../samples/javascript/README.md)
- [TypeScript Calculator](../samples/typescript/README.md)
- [Python Calculator](../../../../03-GettingStarted/samples/python)
- [Rust Calculator](../../../../03-GettingStarted/samples/rust)

## Assignment

Gumawa ng simpleng MCP server na may tool na iyong pipiliin:

1. I-implementa ang tool sa iyong preferred na wika (.NET, Java, Python, TypeScript, o Rust).
2. Tukuyin ang mga input parameters at mga return values.
3. Patakbuhin ang inspector tool upang matiyak na gumagana nang maayos ang server.
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
**Pagtanggi**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagamat nagsusumikap kami para sa katumpakan, pakitandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o kamalian. Ang orihinal na dokumento sa likas nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, ipinapayo ang propesyonal na pagsasalin ng tao. Hindi kami mananagot para sa anumang hindi pagkakaunawaan o maling interpretasyon na bunga ng paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->