<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8fdac7600a5f4722643d0f14e15ac259",
  "translation_date": "2025-12-11T08:05:51+00:00",
  "source_file": "03-GettingStarted/01-first-server/README.md",
  "language_code": "bg"
}
-->
# Започване с MCP

Добре дошли в първите си стъпки с Model Context Protocol (MCP)! Независимо дали сте нови в MCP или искате да задълбочите разбирането си, това ръководство ще ви преведе през основния процес на настройка и разработка. Ще откриете как MCP позволява безпроблемна интеграция между AI модели и приложения и ще научите как бързо да подготвите средата си за изграждане и тестване на решения, базирани на MCP.

> TLDR; Ако създавате AI приложения, знаете, че можете да добавяте инструменти и други ресурси към вашия LLM (голям езиков модел), за да направите LLM по-знаещ. Въпреки това, ако поставите тези инструменти и ресурси на сървър, възможностите на приложението и сървъра могат да се използват от всеки клиент с/без LLM.

## Преглед

Този урок предоставя практическо ръководство за настройка на MCP среди и изграждане на първите ви MCP приложения. Ще научите как да настроите необходимите инструменти и рамки, да изградите базови MCP сървъри, да създадете хост приложения и да тествате вашите реализации.

Model Context Protocol (MCP) е отворен протокол, който стандартизира начина, по който приложенията предоставят контекст на LLM. Мислете за MCP като за USB-C порт за AI приложения - той осигурява стандартизиран начин за свързване на AI модели с различни източници на данни и инструменти.

## Учебни цели

Към края на този урок ще можете да:

- Настроите среди за разработка за MCP на C#, Java, Python, TypeScript и Rust
- Изградите и разположите базови MCP сървъри с персонализирани функции (ресурси, подсказки и инструменти)
- Създадете хост приложения, които се свързват с MCP сървъри
- Тествате и отстранявате грешки в MCP реализации

## Настройка на вашата MCP среда

Преди да започнете работа с MCP, е важно да подготвите средата си за разработка и да разберете основния работен процес. Този раздел ще ви преведе през началните стъпки за настройка, за да осигури гладък старт с MCP.

### Предварителни изисквания

Преди да се потопите в разработката с MCP, уверете се, че имате:

- **Среда за разработка**: За избрания от вас език (C#, Java, Python, TypeScript или Rust)
- **IDE/Редактор**: Visual Studio, Visual Studio Code, IntelliJ, Eclipse, PyCharm или друг модерен редактор на код
- **Мениджъри на пакети**: NuGet, Maven/Gradle, pip, npm/yarn или Cargo
- **API ключове**: За всички AI услуги, които планирате да използвате в хост приложенията си

## Основна структура на MCP сървър

MCP сървърът обикновено включва:

- **Конфигурация на сървъра**: Настройка на порт, удостоверяване и други параметри
- **Ресурси**: Данни и контекст, достъпни за LLM
- **Инструменти**: Функционалности, които моделите могат да извикват
- **Подсказки**: Шаблони за генериране или структуриране на текст

Ето един опростен пример на TypeScript:

```typescript
import { McpServer, ResourceTemplate } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";

// Създайте MCP сървър
const server = new McpServer({
  name: "Demo",
  version: "1.0.0"
});

// Добавете инструмент за събиране
server.tool("add",
  { a: z.number(), b: z.number() },
  async ({ a, b }) => ({
    content: [{ type: "text", text: String(a + b) }]
  })
);

// Добавете динамичен ресурс за поздрав
server.resource(
  "file",
  // Параметърът 'list' контролира как ресурсът изброява наличните файлове. Задаването му на undefined деактивира изброяването за този ресурс.
  new ResourceTemplate("file://{path}", { list: undefined }),
  async (uri, { path }) => ({
    contents: [{
      uri: uri.href,
      text: `File, ${path}!`
    }]
  })
);

// Добавете файлов ресурс, който чете съдържанието на файла
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

// Започнете да получавате съобщения от stdin и да изпращате съобщения към stdout
const transport = new StdioServerTransport();
await server.connect(transport);
```

В горния код ние:

- Импортираме необходимите класове от MCP TypeScript SDK.
- Създаваме и конфигурираме нов MCP сървър.
- Регистрираме персонализиран инструмент (`calculator`) с функция за обработка.
- Стартираме сървъра, за да слуша входящи MCP заявки.

## Тестване и отстраняване на грешки

Преди да започнете да тествате вашия MCP сървър, е важно да разберете наличните инструменти и най-добрите практики за отстраняване на грешки. Ефективното тестване гарантира, че сървърът ви се държи както се очаква и ви помага бързо да идентифицирате и решите проблеми. Следващият раздел очертава препоръчителни подходи за валидиране на вашата MCP реализация.

MCP предоставя инструменти, които да ви помогнат да тествате и отстранявате грешки в сървърите си:

- **Инструмент Inspector**, този графичен интерфейс ви позволява да се свържете със сървъра и да тествате вашите инструменти, подсказки и ресурси.
- **curl**, можете също да се свържете със сървъра си чрез команден ред с инструмент като curl или други клиенти, които могат да създават и изпълняват HTTP команди.

### Използване на MCP Inspector

[MCP Inspector](https://github.com/modelcontextprotocol/inspector) е визуален инструмент за тестване, който ви помага да:

1. **Откривате възможностите на сървъра**: Автоматично открива налични ресурси, инструменти и подсказки
2. **Тествате изпълнението на инструменти**: Пробвате различни параметри и виждате отговорите в реално време
3. **Преглеждате метаданни на сървъра**: Изследвате информация за сървъра, схеми и конфигурации

```bash
# пример TypeScript, инсталиране и стартиране на MCP Inspector
npx @modelcontextprotocol/inspector node build/index.js
```

Когато изпълните горните команди, MCP Inspector ще стартира локален уеб интерфейс в браузъра ви. Можете да очаквате табло, показващо регистрираните MCP сървъри, наличните им инструменти, ресурси и подсказки. Интерфейсът ви позволява интерактивно да тествате изпълнението на инструменти, да инспектирате метаданни на сървъра и да виждате отговори в реално време, което улеснява валидирането и отстраняването на грешки в MCP сървърните реализации.

Ето екранна снимка как може да изглежда:

![MCP Inspector server connection](../../../../translated_images/connected.73d1e042c24075d386cacdd4ee7cd748c16364c277d814e646ff2f7b5eefde85.bg.png)

## Чести проблеми при настройка и решения

| Проблем | Възможно решение |
|---------|------------------|
| Връзката е отказана | Проверете дали сървърът работи и портът е правилен |
| Грешки при изпълнение на инструмент | Прегледайте валидирането на параметрите и обработката на грешки |
| Провали при удостоверяване | Проверете API ключовете и разрешенията |
| Грешки при валидиране на схема | Уверете се, че параметрите съвпадат с дефинираната схема |
| Сървърът не стартира | Проверете за конфликти на портове или липсващи зависимости |
| Грешки с CORS | Конфигурирайте правилни CORS заглавки за заявки от различен произход |
| Проблеми с удостоверяване | Проверете валидността на токена и разрешенията |

## Локална разработка

За локална разработка и тестване можете да стартирате MCP сървъри директно на вашата машина:

1. **Стартирайте процеса на сървъра**: Изпълнете вашето MCP сървърно приложение
2. **Конфигурирайте мрежата**: Уверете се, че сървърът е достъпен на очаквания порт
3. **Свържете клиенти**: Използвайте локални URL адреси като `http://localhost:3000`

```bash
# Пример: Стартиране на TypeScript MCP сървър локално
npm run start
# Сървърът работи на http://localhost:3000
```

## Изграждане на първия ви MCP сървър

В предишен урок разгледахме [Основни концепции](/01-CoreConcepts/README.md), сега е време да приложим тези знания.

### Какво може да прави сървърът

Преди да започнем да пишем код, нека си припомним какво може да прави сървърът:

MCP сървърът може например:

- Да достъпва локални файлове и бази данни
- Да се свързва с отдалечени API-та
- Да извършва изчисления
- Да се интегрира с други инструменти и услуги
- Да предоставя потребителски интерфейс за взаимодействие

Страхотно, сега когато знаем какво може да прави, нека започнем да кодираме.

## Упражнение: Създаване на сървър

За да създадете сървър, трябва да следвате тези стъпки:

- Инсталирайте MCP SDK.
- Създайте проект и настройте структурата на проекта.
- Напишете кода на сървъра.
- Тествайте сървъра.

### -1- Създаване на проект

#### TypeScript

```sh
# Създайте директория за проекта и инициализирайте npm проект
mkdir calculator-server
cd calculator-server
npm init -y
```

#### Python

```sh
# Създайте директория за проекта
mkdir calculator-server
cd calculator-server
# Отворете папката във Visual Studio Code - Пропуснете това, ако използвате различна IDE
code .
```

#### .NET

```sh
dotnet new console -n McpCalculatorServer
cd McpCalculatorServer
```

#### Java

За Java създайте Spring Boot проект:

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

Разархивирайте zip файла:

```bash
unzip calculator-server.zip -d calculator-server
cd calculator-server
# по избор премахнете неизползвания тест
rm -rf src/test/java
```

Добавете следната пълна конфигурация във вашия *pom.xml* файл:

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

### -2- Добавяне на зависимости

След като проектът е създаден, нека добавим зависимости:

#### TypeScript

```sh
# Ако все още не е инсталиран, инсталирайте TypeScript глобално
npm install typescript -g

# Инсталирайте MCP SDK и Zod за валидиране на схеми
npm install @modelcontextprotocol/sdk zod
npm install -D @types/node typescript
```

#### Python

```sh
# Създайте виртуална среда и инсталирайте зависимостите
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

### -3- Създаване на файлове в проекта

#### TypeScript

Отворете файла *package.json* и заменете съдържанието с следното, за да осигурите възможност за компилиране и стартиране на сървъра:

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

Създайте *tsconfig.json* със следното съдържание:

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

Създайте директория за вашия изходен код:

```sh
mkdir src
touch src/index.ts
```

#### Python

Създайте файл *server.py*

```sh
touch server.py
```

#### .NET

Инсталирайте необходимите NuGet пакети:

```sh
dotnet add package ModelContextProtocol --prerelease
dotnet add package Microsoft.Extensions.Hosting
```

#### Java

За Java Spring Boot проекти структурата на проекта се създава автоматично.

#### Rust

За Rust, файл *src/main.rs* се създава по подразбиране при изпълнение на `cargo init`. Отворете файла и изтрийте кода по подразбиране.

### -4- Създаване на кода на сървъра

#### TypeScript

Създайте файл *index.ts* и добавете следния код:

```typescript
import { McpServer, ResourceTemplate } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";
 
// Създайте MCP сървър
const server = new McpServer({
  name: "Calculator MCP Server",
  version: "1.0.0"
});
```

Сега имате сървър, но той не прави много, нека го поправим.

#### Python

```python
# server.py
from mcp.server.fastmcp import FastMCP

# Създайте MCP сървър
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

За Java създайте основните компоненти на сървъра. Първо, модифицирайте главния клас на приложението:

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

Създайте услугата за калкулатор *src/main/java/com/microsoft/mcp/sample/server/service/CalculatorService.java*:

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

**Опционални компоненти за продукционна услуга:**

Създайте конфигурация за стартиране *src/main/java/com/microsoft/mcp/sample/server/config/StartupConfig.java*:

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

Създайте контролер за здравословно състояние *src/main/java/com/microsoft/mcp/sample/server/controller/HealthController.java*:

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

Създайте обработчик на изключения *src/main/java/com/microsoft/mcp/sample/server/exception/GlobalExceptionHandler.java*:

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

        // Гетъри
        public String getCode() { return code; }
        public String getMessage() { return message; }
    }
}
```

Създайте персонализиран банер *src/main/resources/banner.txt*:

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

Добавете следния код в началото на файла *src/main.rs*. Това импортира необходимите библиотеки и модули за вашия MCP сървър.

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

Калкулаторният сървър ще бъде прост, който може да събира две числа. Нека създадем структура, която да представя заявката към калкулатора.

```rust
#[derive(Debug, serde::Deserialize, schemars::JsonSchema)]
pub struct CalculatorRequest {
    pub a: f64,
    pub b: f64,
}
```

След това създайте структура, която да представя калкулаторния сървър. Тази структура ще държи маршрутизатора на инструментите, който се използва за регистриране на инструменти.

```rust
#[derive(Debug, Clone)]
pub struct Calculator {
    tool_router: ToolRouter<Self>,
}
```

Сега можем да имплементираме структурата `Calculator`, за да създадем нова инстанция на сървъра и да имплементираме обработчика на сървъра, който предоставя информация за сървъра.

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

Накрая трябва да имплементираме главната функция, която стартира сървъра. Тази функция ще създаде инстанция на структурата `Calculator` и ще я обслужва чрез стандартен вход/изход.

```rust
#[tokio::main]
async fn main() -> Result<(), Box<dyn Error>> {
    let service = Calculator::new().serve(stdio()).await?;
    service.waiting().await?;
    Ok(())
}
```

Сървърът вече е настроен да предоставя основна информация за себе си. След това ще добавим инструмент за извършване на събиране.

### -5- Добавяне на инструмент и ресурс

Добавете инструмент и ресурс, като добавите следния код:

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

Вашият инструмент приема параметри `a` и `b` и изпълнява функция, която произвежда отговор във формата:

```typescript
{
  contents: [{
    type: "text", content: "some content"
  }]
}
```

Вашият ресурс се достъпва чрез низ "greeting", приема параметър `name` и произвежда подобен отговор като инструмента:

```typescript
{
  uri: "<href>",
  text: "a text"
}
```

#### Python

```python
# Добавете инструмент за събиране
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


# Добавете динамичен ресурс за поздравление
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}!"
```

В горния код ние:

- Дефинирахме инструмент `add`, който приема параметри `a` и `b`, и двата цели числа.
- Създадохме ресурс, наречен `greeting`, който приема параметър `name`.

#### .NET

Добавете това във вашия файл Program.cs:

```csharp
[McpServerToolType]
public static class CalculatorTool
{
    [McpServerTool, Description("Adds two numbers")]
    public static string Add(int a, int b) => $"Sum {a + b}";
}
```

#### Java

Инструментите вече бяха създадени в предишната стъпка.

#### Rust

Добавете нов инструмент вътре в блока `impl Calculator`:

```rust
#[tool(description = "Adds a and b")]
async fn add(
    &self,
    Parameters(CalculatorRequest { a, b }): Parameters<CalculatorRequest>,
) -> String {
    (a + b).to_string()
}
```

### -6- Финален код

Нека добавим последния необходим код, за да може сървърът да стартира:

#### TypeScript

```typescript
// Започнете да получавате съобщения от stdin и да изпращате съобщения към stdout
const transport = new StdioServerTransport();
await server.connect(transport);
```

Ето пълния код:

```typescript
// index.ts
import { McpServer, ResourceTemplate } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";

// Създайте MCP сървър
const server = new McpServer({
  name: "Calculator MCP Server",
  version: "1.0.0"
});

// Добавете инструмент за събиране
server.tool(
  "add",
  { a: z.number(), b: z.number() },
  async ({ a, b }) => ({
    content: [{ type: "text", text: String(a + b) }]
  })
);

// Добавете динамичен ресурс за поздрав
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

// Започнете да получавате съобщения от stdin и да изпращате съобщения към stdout
const transport = new StdioServerTransport();
server.connect(transport);
```

#### Python

```python
# server.py
from mcp.server.fastmcp import FastMCP

# Създаване на MCP сървър
mcp = FastMCP("Demo")


# Добавяне на инструмент за събиране
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


# Добавяне на динамичен ресурс за поздрав
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}!"

# Основен блок за изпълнение - това е необходимо за стартиране на сървъра
if __name__ == "__main__":
    mcp.run()
```

#### .NET

Създайте файл Program.cs със следното съдържание:

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

Вашият пълен главен клас на приложението трябва да изглежда така:

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

Финалният код за Rust сървъра трябва да изглежда така:

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

### -7- Тествайте сървъра

Стартирайте сървъра с следната команда:

#### TypeScript

```sh
npm run build
```

#### Python

```sh
mcp run server.py
```

> За да използвате MCP Inspector, използвайте `mcp dev server.py`, който автоматично стартира Inspector и предоставя необходимия прокси сесионен токен. Ако използвате `mcp run server.py`, ще трябва ръчно да стартирате Inspector и да конфигурирате връзката.

#### .NET

Уверете се, че сте в директорията на проекта:

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

Изпълнете следните команди за форматиране и стартиране на сървъра:

```sh
cargo fmt
cargo run
```

### -8- Стартиране с помощта на инспектора

Инспекторът е страхотен инструмент, който може да стартира вашия сървър и ви позволява да взаимодействате с него, за да тествате дали работи. Нека го стартираме:

> [!NOTE]
> може да изглежда различно в полето "command", тъй като съдържа командата за стартиране на сървър с вашата конкретна среда за изпълнение.

#### TypeScript

```sh
npx @modelcontextprotocol/inspector node build/index.js
```

или го добавете във вашия *package.json* така: `"inspector": "npx @modelcontextprotocol/inspector node build/index.js"` и след това изпълнете `npm run inspector`

#### Python

Python обвива Node.js инструмент, наречен inspector. Възможно е да извикате този инструмент така:

```sh
mcp dev server.py
```

Въпреки това, той не имплементира всички методи, налични в инструмента, затова се препоръчва да стартирате директно Node.js инструмента, както е показано по-долу:

```sh
npx @modelcontextprotocol/inspector mcp run server.py
```

Ако използвате инструмент или IDE, който позволява конфигуриране на команди и аргументи за стартиране на скриптове,
уверете се, че сте задали `python` в полето `Command` и `server.py` като `Arguments`. Това гарантира, че скриптът ще се изпълни правилно.

#### .NET

Уверете се, че сте в директорията на вашия проект:

```sh
cd McpCalculatorServer
npx @modelcontextprotocol/inspector dotnet run
```

#### Java

Уверете се, че вашият калкулатор сървър работи
След това стартирайте инспектора:

```cmd
npx @modelcontextprotocol/inspector
```

В уеб интерфейса на инспектора:

1. Изберете "SSE" като тип транспорт
2. Задайте URL на: `http://localhost:8080/sse`
3. Натиснете "Connect"

![Connect](../../../../translated_images/tool.163d33e3ee307e209ef146d8f85060d2f7e83e9f59b3b1699a77204ae0454ad2.bg.png)

**Вече сте свързани със сървъра**
**Секцията за тестване на Java сървъра е завършена**

Следващата секция е за взаимодействие със сървъра.

Трябва да видите следния потребителски интерфейс:

![Connect](../../../../translated_images/connect.141db0b2bd05f096fb1dd91273771fd8b2469d6507656c3b0c9df4b3c5473929.bg.png)

1. Свържете се със сървъра, като изберете бутона Connect
  След като се свържете със сървъра, трябва да видите следното:

  ![Connected](../../../../translated_images/connected.73d1e042c24075d386cacdd4ee7cd748c16364c277d814e646ff2f7b5eefde85.bg.png)

1. Изберете "Tools" и "listTools", трябва да видите "Add", изберете "Add" и попълнете стойностите на параметрите.

  Трябва да видите следния отговор, т.е. резултат от инструмента "add":

  ![Result of running add](../../../../translated_images/ran-tool.a5a6ee878c1369ec1e379b81053395252a441799dbf23416c36ddf288faf8249.bg.png)

Поздравления, успяхте да създадете и стартирате първия си сървър!

#### Rust

За да стартирате Rust сървъра с MCP Inspector CLI, използвайте следната команда:

```sh
npx @modelcontextprotocol/inspector cargo run --cli --method tools/call --tool-name add --tool-arg a=1 b=2
```

### Официални SDK

MCP предоставя официални SDK за няколко езика:

- [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk) - Поддържан в сътрудничество с Microsoft
- [Java SDK](https://github.com/modelcontextprotocol/java-sdk) - Поддържан в сътрудничество със Spring AI
- [TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk) - Официалната TypeScript имплементация
- [Python SDK](https://github.com/modelcontextprotocol/python-sdk) - Официалната Python имплементация
- [Kotlin SDK](https://github.com/modelcontextprotocol/kotlin-sdk) - Официалната Kotlin имплементация
- [Swift SDK](https://github.com/modelcontextprotocol/swift-sdk) - Поддържан в сътрудничество с Loopwork AI
- [Rust SDK](https://github.com/modelcontextprotocol/rust-sdk) - Официалната Rust имплементация

## Основни изводи

- Настройването на MCP среда за разработка е лесно с езиково-специфични SDK
- Създаването на MCP сървъри включва създаване и регистриране на инструменти с ясни схеми
- Тестването и отстраняването на грешки са от съществено значение за надеждни MCP реализации

## Примери

- [Java Calculator](../samples/java/calculator/README.md)
- [.Net Calculator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Calculator](../samples/javascript/README.md)
- [TypeScript Calculator](../samples/typescript/README.md)
- [Python Calculator](../../../../03-GettingStarted/samples/python)
- [Rust Calculator](../../../../03-GettingStarted/samples/rust)

## Задача

Създайте прост MCP сървър с инструмент по ваш избор:

1. Имплементирайте инструмента на предпочитания от вас език (.NET, Java, Python, TypeScript или Rust).
2. Дефинирайте входни параметри и стойности за връщане.
3. Стартирайте инспекторския инструмент, за да се уверите, че сървърът работи както трябва.
4. Тествайте имплементацията с различни входни данни.

## Решение

[Решение](./solution/README.md)

## Допълнителни ресурси

- [Създаване на агенти с Model Context Protocol в Azure](https://learn.microsoft.com/azure/developer/ai/intro-agents-mcp)
- [Отдалечен MCP с Azure Container Apps (Node.js/TypeScript/JavaScript)](https://learn.microsoft.com/samples/azure-samples/mcp-container-ts/mcp-container-ts/)
- [.NET OpenAI MCP агент](https://learn.microsoft.com/samples/azure-samples/openai-mcp-agent-dotnet/openai-mcp-agent-dotnet/)

## Какво следва

Следва: [Започване с MCP клиенти](../02-client/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Отказ от отговорност**:
Този документ е преведен с помощта на AI преводаческа услуга [Co-op Translator](https://github.com/Azure/co-op-translator). Въпреки че се стремим към точност, моля, имайте предвид, че автоматизираните преводи могат да съдържат грешки или неточности. Оригиналният документ на неговия роден език трябва да се счита за авторитетен източник. За критична информация се препоръчва професионален човешки превод. Ние не носим отговорност за каквито и да е недоразумения или неправилни тълкувания, произтичащи от използването на този превод.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->