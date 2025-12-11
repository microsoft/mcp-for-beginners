<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8fdac7600a5f4722643d0f14e15ac259",
  "translation_date": "2025-12-11T04:47:02+00:00",
  "source_file": "03-GettingStarted/01-first-server/README.md",
  "language_code": "ru"
}
-->
# Начало работы с MCP

Добро пожаловать в ваши первые шаги с протоколом контекста модели (MCP)! Независимо от того, новичок ли вы в MCP или хотите углубить свои знания, это руководство проведет вас через основные этапы настройки и разработки. Вы узнаете, как MCP обеспечивает бесшовную интеграцию между ИИ-моделями и приложениями, а также как быстро подготовить вашу среду для создания и тестирования решений на базе MCP.

> Кратко; Если вы создаете ИИ-приложения, вы знаете, что можно добавить инструменты и другие ресурсы в вашу LLM (большую языковую модель), чтобы сделать LLM более информированной. Однако, если вы размещаете эти инструменты и ресурсы на сервере, возможности приложения и сервера могут использовать любые клиенты с LLM или без него.

## Обзор

Этот урок предоставляет практические рекомендации по настройке сред MCP и созданию ваших первых приложений MCP. Вы узнаете, как настроить необходимые инструменты и фреймворки, создать базовые серверы MCP, создать хост-приложения и протестировать ваши реализации.

Протокол контекста модели (MCP) — это открытый протокол, стандартизирующий способ предоставления контекста LLM приложениями. Представьте MCP как порт USB-C для ИИ-приложений — он обеспечивает стандартизированный способ подключения ИИ-моделей к различным источникам данных и инструментам.

## Цели обучения

К концу этого урока вы сможете:

- Настроить среды разработки для MCP на C#, Java, Python, TypeScript и Rust
- Создавать и развертывать базовые серверы MCP с пользовательскими функциями (ресурсы, подсказки и инструменты)
- Создавать хост-приложения, подключающиеся к серверам MCP
- Тестировать и отлаживать реализации MCP

## Настройка вашей среды MCP

Прежде чем начать работу с MCP, важно подготовить вашу среду разработки и понять базовый рабочий процесс. Этот раздел проведет вас через начальные шаги настройки, чтобы обеспечить плавный старт с MCP.

### Требования

Перед тем как погрузиться в разработку MCP, убедитесь, что у вас есть:

- **Среда разработки**: для выбранного языка (C#, Java, Python, TypeScript или Rust)
- **IDE/редактор**: Visual Studio, Visual Studio Code, IntelliJ, Eclipse, PyCharm или любой современный редактор кода
- **Менеджеры пакетов**: NuGet, Maven/Gradle, pip, npm/yarn или Cargo
- **API-ключи**: для любых ИИ-сервисов, которые вы планируете использовать в своих хост-приложениях

## Базовая структура сервера MCP

Сервер MCP обычно включает:

- **Конфигурация сервера**: настройка порта, аутентификации и других параметров
- **Ресурсы**: данные и контекст, доступные для LLM
- **Инструменты**: функциональность, которую модели могут вызывать
- **Подсказки**: шаблоны для генерации или структурирования текста

Вот упрощенный пример на TypeScript:

```typescript
import { McpServer, ResourceTemplate } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";

// Создать MCP сервер
const server = new McpServer({
  name: "Demo",
  version: "1.0.0"
});

// Добавить инструмент сложения
server.tool("add",
  { a: z.number(), b: z.number() },
  async ({ a, b }) => ({
    content: [{ type: "text", text: String(a + b) }]
  })
);

// Добавить динамический ресурс приветствия
server.resource(
  "file",
  // Параметр 'list' контролирует, как ресурс перечисляет доступные файлы. Установка его в undefined отключает перечисление для этого ресурса.
  new ResourceTemplate("file://{path}", { list: undefined }),
  async (uri, { path }) => ({
    contents: [{
      uri: uri.href,
      text: `File, ${path}!`
    }]
  })
);

// Добавить файловый ресурс, который читает содержимое файла
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

// Начать прием сообщений на stdin и отправку сообщений на stdout
const transport = new StdioServerTransport();
await server.connect(transport);
```

В приведенном выше коде мы:

- Импортируем необходимые классы из MCP TypeScript SDK.
- Создаем и настраиваем новый экземпляр сервера MCP.
- Регистрируем пользовательский инструмент (`calculator`) с функцией-обработчиком.
- Запускаем сервер для прослушивания входящих запросов MCP.

## Тестирование и отладка

Прежде чем начать тестировать ваш сервер MCP, важно понять доступные инструменты и лучшие практики отладки. Эффективное тестирование гарантирует, что ваш сервер работает как ожидается, и помогает быстро выявлять и устранять проблемы. В следующем разделе описаны рекомендуемые подходы для проверки вашей реализации MCP.

MCP предоставляет инструменты, которые помогут вам тестировать и отлаживать ваши серверы:

- **Инструмент Inspector**, этот графический интерфейс позволяет подключаться к вашему серверу и тестировать ваши инструменты, подсказки и ресурсы.
- **curl**, вы также можете подключаться к серверу с помощью командной строки, используя curl или другие клиенты, которые могут создавать и выполнять HTTP-команды.

### Использование MCP Inspector

[MCP Inspector](https://github.com/modelcontextprotocol/inspector) — это визуальный инструмент тестирования, который помогает вам:

1. **Обнаруживать возможности сервера**: автоматически определять доступные ресурсы, инструменты и подсказки
2. **Тестировать выполнение инструментов**: пробовать разные параметры и видеть ответы в реальном времени
3. **Просматривать метаданные сервера**: изучать информацию о сервере, схемы и конфигурации

```bash
# пример TypeScript, установка и запуск MCP Inspector
npx @modelcontextprotocol/inspector node build/index.js
```

При выполнении вышеуказанных команд MCP Inspector запустит локальный веб-интерфейс в вашем браузере. Вы увидите панель управления с зарегистрированными серверами MCP, их доступными инструментами, ресурсами и подсказками. Интерфейс позволяет интерактивно тестировать выполнение инструментов, просматривать метаданные сервера и видеть ответы в реальном времени, что облегчает проверку и отладку ваших реализаций MCP.

Вот скриншот того, как это может выглядеть:

![MCP Inspector server connection](../../../../translated_images/connected.73d1e042c24075d386cacdd4ee7cd748c16364c277d814e646ff2f7b5eefde85.ru.png)

## Распространенные проблемы настройки и решения

| Проблема | Возможное решение |
|----------|-------------------|
| Отказ в подключении | Проверьте, запущен ли сервер и правильный ли порт |
| Ошибки выполнения инструментов | Проверьте валидацию параметров и обработку ошибок |
| Ошибки аутентификации | Проверьте API-ключи и разрешения |
| Ошибки валидации схемы | Убедитесь, что параметры соответствуют определенной схеме |
| Сервер не запускается | Проверьте конфликты портов или отсутствующие зависимости |
| Ошибки CORS | Настройте правильные заголовки CORS для кросс-доменных запросов |
| Проблемы с аутентификацией | Проверьте действительность токена и разрешения |

## Локальная разработка

Для локальной разработки и тестирования вы можете запускать серверы MCP непосредственно на вашем компьютере:

1. **Запустите процесс сервера**: запустите ваше приложение сервера MCP
2. **Настройте сеть**: убедитесь, что сервер доступен на ожидаемом порту
3. **Подключите клиентов**: используйте локальные URL, например `http://localhost:3000`

```bash
# Пример: Запуск TypeScript MCP сервера локально
npm run start
# Сервер запущен по адресу http://localhost:3000
```

## Создание вашего первого сервера MCP

Мы уже рассмотрели [Основные концепции](/01-CoreConcepts/README.md) в предыдущем уроке, теперь пора применить эти знания на практике.

### Что может делать сервер

Прежде чем начать писать код, давайте напомним, что может делать сервер:

Сервер MCP может, например:

- Получать доступ к локальным файлам и базам данных
- Подключаться к удаленным API
- Выполнять вычисления
- Интегрироваться с другими инструментами и сервисами
- Предоставлять пользовательский интерфейс для взаимодействия

Отлично, теперь, когда мы знаем, что он может делать, приступим к кодированию.

## Упражнение: Создание сервера

Чтобы создать сервер, нужно выполнить следующие шаги:

- Установить MCP SDK.
- Создать проект и настроить структуру проекта.
- Написать код сервера.
- Протестировать сервер.

### -1- Создание проекта

#### TypeScript

```sh
# Создайте каталог проекта и инициализируйте npm проект
mkdir calculator-server
cd calculator-server
npm init -y
```

#### Python

```sh
# Создать каталог проекта
mkdir calculator-server
cd calculator-server
# Откройте папку в Visual Studio Code - пропустите этот шаг, если вы используете другую IDE
code .
```

#### .NET

```sh
dotnet new console -n McpCalculatorServer
cd McpCalculatorServer
```

#### Java

Для Java создайте проект Spring Boot:

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

Распакуйте zip-файл:

```bash
unzip calculator-server.zip -d calculator-server
cd calculator-server
# необязательно удалить неиспользуемый тест
rm -rf src/test/java
```

Добавьте следующую полную конфигурацию в ваш файл *pom.xml*:

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

### -2- Добавление зависимостей

Теперь, когда проект создан, давайте добавим зависимости:

#### TypeScript

```sh
# Если еще не установлен, установите TypeScript глобально
npm install typescript -g

# Установите MCP SDK и Zod для проверки схемы
npm install @modelcontextprotocol/sdk zod
npm install -D @types/node typescript
```

#### Python

```sh
# Создайте виртуальное окружение и установите зависимости
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

### -3- Создание файлов проекта

#### TypeScript

Откройте файл *package.json* и замените содержимое следующим, чтобы обеспечить возможность сборки и запуска сервера:

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

Создайте *tsconfig.json* со следующим содержимым:

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

Создайте каталог для исходного кода:

```sh
mkdir src
touch src/index.ts
```

#### Python

Создайте файл *server.py*

```sh
touch server.py
```

#### .NET

Установите необходимые пакеты NuGet:

```sh
dotnet add package ModelContextProtocol --prerelease
dotnet add package Microsoft.Extensions.Hosting
```

#### Java

Для проектов Java Spring Boot структура проекта создается автоматически.

#### Rust

Для Rust файл *src/main.rs* создается по умолчанию при запуске `cargo init`. Откройте файл и удалите код по умолчанию.

### -4- Создание кода сервера

#### TypeScript

Создайте файл *index.ts* и добавьте следующий код:

```typescript
import { McpServer, ResourceTemplate } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";
 
// Создать MCP сервер
const server = new McpServer({
  name: "Calculator MCP Server",
  version: "1.0.0"
});
```

Теперь у вас есть сервер, но он мало что делает, давайте исправим это.

#### Python

```python
# server.py
from mcp.server.fastmcp import FastMCP

# Создать MCP сервер
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

Для Java создайте основные компоненты сервера. Сначала измените главный класс приложения:

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

Создайте сервис калькулятора *src/main/java/com/microsoft/mcp/sample/server/service/CalculatorService.java*:

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

**Опциональные компоненты для готового к продакшену сервиса:**

Создайте конфигурацию запуска *src/main/java/com/microsoft/mcp/sample/server/config/StartupConfig.java*:

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

Создайте контроллер состояния *src/main/java/com/microsoft/mcp/sample/server/controller/HealthController.java*:

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

Создайте обработчик исключений *src/main/java/com/microsoft/mcp/sample/server/exception/GlobalExceptionHandler.java*:

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

        // Геттеры
        public String getCode() { return code; }
        public String getMessage() { return message; }
    }
}
```

Создайте пользовательский баннер *src/main/resources/banner.txt*:

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

Добавьте следующий код в начало файла *src/main.rs*. Это импортирует необходимые библиотеки и модули для вашего сервера MCP.

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

Сервер калькулятора будет простым и сможет складывать два числа. Давайте создадим структуру для представления запроса калькулятора.

```rust
#[derive(Debug, serde::Deserialize, schemars::JsonSchema)]
pub struct CalculatorRequest {
    pub a: f64,
    pub b: f64,
}
```

Далее создайте структуру для представления сервера калькулятора. Эта структура будет содержать маршрутизатор инструментов, который используется для регистрации инструментов.

```rust
#[derive(Debug, Clone)]
pub struct Calculator {
    tool_router: ToolRouter<Self>,
}
```

Теперь мы можем реализовать структуру `Calculator`, чтобы создать новый экземпляр сервера и реализовать обработчик сервера для предоставления информации о сервере.

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

Наконец, нужно реализовать основную функцию для запуска сервера. Эта функция создаст экземпляр структуры `Calculator` и будет обслуживать его через стандартный ввод/вывод.

```rust
#[tokio::main]
async fn main() -> Result<(), Box<dyn Error>> {
    let service = Calculator::new().serve(stdio()).await?;
    service.waiting().await?;
    Ok(())
}
```

Сервер теперь настроен для предоставления базовой информации о себе. Далее мы добавим инструмент для выполнения сложения.

### -5- Добавление инструмента и ресурса

Добавьте инструмент и ресурс, добавив следующий код:

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

Ваш инструмент принимает параметры `a` и `b` и выполняет функцию, которая возвращает ответ в форме:

```typescript
{
  contents: [{
    type: "text", content: "some content"
  }]
}
```

Ваш ресурс доступен по строке "greeting", принимает параметр `name` и возвращает ответ, аналогичный инструменту:

```typescript
{
  uri: "<href>",
  text: "a text"
}
```

#### Python

```python
# Добавить инструмент сложения
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


# Добавить динамический ресурс приветствия
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}!"
```

В приведенном выше коде мы:

- Определили инструмент `add`, который принимает параметры `a` и `b`, оба целые числа.
- Создали ресурс с именем `greeting`, который принимает параметр `name`.

#### .NET

Добавьте это в ваш файл Program.cs:

```csharp
[McpServerToolType]
public static class CalculatorTool
{
    [McpServerTool, Description("Adds two numbers")]
    public static string Add(int a, int b) => $"Sum {a + b}";
}
```

#### Java

Инструменты уже были созданы на предыдущем шаге.

#### Rust

Добавьте новый инструмент внутри блока `impl Calculator`:

```rust
#[tool(description = "Adds a and b")]
async fn add(
    &self,
    Parameters(CalculatorRequest { a, b }): Parameters<CalculatorRequest>,
) -> String {
    (a + b).to_string()
}
```

### -6- Финальный код

Добавим последний необходимый код, чтобы сервер мог запуститься:

#### TypeScript

```typescript
// Начать получение сообщений на stdin и отправку сообщений на stdout
const transport = new StdioServerTransport();
await server.connect(transport);
```

Вот полный код:

```typescript
// index.ts
import { McpServer, ResourceTemplate } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";

// Создать MCP сервер
const server = new McpServer({
  name: "Calculator MCP Server",
  version: "1.0.0"
});

// Добавить инструмент сложения
server.tool(
  "add",
  { a: z.number(), b: z.number() },
  async ({ a, b }) => ({
    content: [{ type: "text", text: String(a + b) }]
  })
);

// Добавить динамический ресурс приветствия
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

// Начать прием сообщений на stdin и отправку сообщений на stdout
const transport = new StdioServerTransport();
server.connect(transport);
```

#### Python

```python
# server.py
from mcp.server.fastmcp import FastMCP

# Создать MCP сервер
mcp = FastMCP("Demo")


# Добавить инструмент сложения
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


# Добавить динамический ресурс приветствия
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}!"

# Основной блок выполнения - это необходимо для запуска сервера
if __name__ == "__main__":
    mcp.run()
```

#### .NET

Создайте файл Program.cs со следующим содержимым:

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

Ваш полный главный класс приложения должен выглядеть так:

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

Финальный код для сервера на Rust должен выглядеть так:

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

### -7- Тестирование сервера

Запустите сервер следующей командой:

#### TypeScript

```sh
npm run build
```

#### Python

```sh
mcp run server.py
```

> Для использования MCP Inspector используйте `mcp dev server.py`, который автоматически запускает Inspector и предоставляет необходимый токен сессии прокси. Если использовать `mcp run server.py`, вам нужно будет вручную запустить Inspector и настроить подключение.

#### .NET

Убедитесь, что вы находитесь в каталоге проекта:

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

Выполните следующие команды для форматирования и запуска сервера:

```sh
cargo fmt
cargo run
```

### -8- Запуск с использованием инспектора

Inspector — отличный инструмент, который может запустить ваш сервер и позволит вам взаимодействовать с ним, чтобы проверить его работу. Давайте запустим его:

> [!NOTE]
> в поле "command" может отображаться другая команда, так как она содержит команду для запуска сервера с вашим конкретным рантаймом.

#### TypeScript

```sh
npx @modelcontextprotocol/inspector node build/index.js
```

или добавьте это в ваш *package.json* так: `"inspector": "npx @modelcontextprotocol/inspector node build/index.js"` и затем запустите `npm run inspector`

#### Python

Python оборачивает инструмент Node.js под названием inspector. Можно вызвать этот инструмент так:

```sh
mcp dev server.py
```

Однако он не реализует все методы, доступные в инструменте, поэтому рекомендуется запускать инструмент Node.js напрямую, как показано ниже:

```sh
npx @modelcontextprotocol/inspector mcp run server.py
```

Если вы используете инструмент или IDE, которые позволяют настраивать команды и аргументы для запуска скриптов, 
убедитесь, что в поле `Command` установлено значение `python`, а в поле `Arguments` — `server.py`. Это гарантирует правильный запуск скрипта.

#### .NET

Убедитесь, что вы находитесь в каталоге вашего проекта:

```sh
cd McpCalculatorServer
npx @modelcontextprotocol/inspector dotnet run
```

#### Java

Убедитесь, что ваш калькулятор-сервер запущен
Затем запустите инспектор:

```cmd
npx @modelcontextprotocol/inspector
```

В веб-интерфейсе инспектора:

1. Выберите "SSE" в качестве типа транспорта
2. Установите URL: `http://localhost:8080/sse`
3. Нажмите "Connect"

![Connect](../../../../translated_images/tool.163d33e3ee307e209ef146d8f85060d2f7e83e9f59b3b1699a77204ae0454ad2.ru.png)

**Вы теперь подключены к серверу**
**Раздел тестирования Java-сервера завершён**

Следующий раздел посвящён взаимодействию с сервером.

Вы должны увидеть следующий пользовательский интерфейс:

![Connect](../../../../translated_images/connect.141db0b2bd05f096fb1dd91273771fd8b2469d6507656c3b0c9df4b3c5473929.ru.png)

1. Подключитесь к серверу, нажав кнопку Connect
  После подключения к серверу вы должны увидеть следующее:

  ![Connected](../../../../translated_images/connected.73d1e042c24075d386cacdd4ee7cd748c16364c277d814e646ff2f7b5eefde85.ru.png)

1. Выберите "Tools" и "listTools", вы должны увидеть появление "Add", выберите "Add" и заполните значения параметров.

  Вы должны увидеть следующий ответ, то есть результат работы инструмента "add":

  ![Result of running add](../../../../translated_images/ran-tool.a5a6ee878c1369ec1e379b81053395252a441799dbf23416c36ddf288faf8249.ru.png)

Поздравляем, вы создали и запустили свой первый сервер!

#### Rust

Для запуска Rust-сервера с помощью MCP Inspector CLI используйте следующую команду:

```sh
npx @modelcontextprotocol/inspector cargo run --cli --method tools/call --tool-name add --tool-arg a=1 b=2
```

### Официальные SDK

MCP предоставляет официальные SDK для нескольких языков:

- [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk) - Поддерживается в сотрудничестве с Microsoft
- [Java SDK](https://github.com/modelcontextprotocol/java-sdk) - Поддерживается в сотрудничестве с Spring AI
- [TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk) - Официальная реализация на TypeScript
- [Python SDK](https://github.com/modelcontextprotocol/python-sdk) - Официальная реализация на Python
- [Kotlin SDK](https://github.com/modelcontextprotocol/kotlin-sdk) - Официальная реализация на Kotlin
- [Swift SDK](https://github.com/modelcontextprotocol/swift-sdk) - Поддерживается в сотрудничестве с Loopwork AI
- [Rust SDK](https://github.com/modelcontextprotocol/rust-sdk) - Официальная реализация на Rust

## Основные выводы

- Настройка среды разработки MCP проста с использованием SDK для конкретных языков
- Создание MCP-серверов включает создание и регистрацию инструментов с чёткими схемами
- Тестирование и отладка необходимы для надёжной реализации MCP

## Примеры

- [Java Calculator](../samples/java/calculator/README.md)
- [.Net Calculator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Calculator](../samples/javascript/README.md)
- [TypeScript Calculator](../samples/typescript/README.md)
- [Python Calculator](../../../../03-GettingStarted/samples/python)
- [Rust Calculator](../../../../03-GettingStarted/samples/rust)

## Задание

Создайте простой MCP-сервер с инструментом на ваш выбор:

1. Реализуйте инструмент на предпочитаемом языке (.NET, Java, Python, TypeScript или Rust).
2. Определите входные параметры и возвращаемые значения.
3. Запустите инструмент инспектора, чтобы убедиться, что сервер работает корректно.
4. Протестируйте реализацию с различными входными данными.

## Решение

[Решение](./solution/README.md)

## Дополнительные ресурсы

- [Создание агентов с использованием Model Context Protocol на Azure](https://learn.microsoft.com/azure/developer/ai/intro-agents-mcp)
- [Удалённый MCP с Azure Container Apps (Node.js/TypeScript/JavaScript)](https://learn.microsoft.com/samples/azure-samples/mcp-container-ts/mcp-container-ts/)
- [.NET OpenAI MCP Agent](https://learn.microsoft.com/samples/azure-samples/openai-mcp-agent-dotnet/openai-mcp-agent-dotnet/)

## Что дальше

Далее: [Начало работы с MCP-клиентами](../02-client/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Отказ от ответственности**:  
Этот документ был переведен с помощью сервиса автоматического перевода [Co-op Translator](https://github.com/Azure/co-op-translator). Несмотря на наши усилия по обеспечению точности, имейте в виду, что автоматический перевод может содержать ошибки или неточности. Оригинальный документ на его исходном языке следует считать авторитетным источником. Для получения критически важной информации рекомендуется обращаться к профессиональному переводу, выполненному человеком. Мы не несем ответственности за любые недоразумения или неправильные толкования, возникшие в результате использования данного перевода.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->