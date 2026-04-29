# شروع به کار با MCP

به اولین قدم‌های خود با پروتکل مدل کانتکست (MCP) خوش آمدید! چه تازه با MCP آشنا شده باشید یا به دنبال تعمیق درک خود باشید، این راهنما شما را در مراحل ضروری راه‌اندازی و توسعه همراهی می‌کند. خواهید فهمید که چگونه MCP امکان ادغام یکپارچه بین مدل‌های هوش مصنوعی و برنامه‌ها را فراهم می‌کند و یاد می‌گیرید که چگونه محیط خود را به سرعت آماده ساختن و آزمایش راه‌حل‌های مبتنی بر MCP کنید.

> خلاصه؛ اگر شما برنامه‌های هوش مصنوعی می‌سازید، می‌دانید که می‌توانید ابزارها و منابع دیگری را به مدل زبان بزرگ خود (LLM) اضافه کنید تا دانش آن افزایش یابد. اما اگر این ابزارها و منابع را روی یک سرور قرار دهید، قابلیت‌های برنامه و سرور می‌تواند توسط هر مشتری با/بدون LLM استفاده شود.

## مرور کلی

این درس راهنمایی‌های عملی درباره راه‌اندازی محیط‌های MCP و ساخت اولین برنامه‌های MCP شما ارائه می‌دهد. خواهید آموخت که چگونه ابزارها و چارچوب‌های لازم را تنظیم کنید، سرورهای MCP پایه بسازید، برنامه‌های میزبان ایجاد کنید و پیاده‌سازی‌های خود را آزمایش کنید.

پروتکل مدل کانتکست (MCP) یک پروتکل باز است که استانداردسازی نحوه ارائه کانتکست به مدل‌های زبانی بزرگ را ارائه می‌دهد. MCP را مانند پورت USB-C برای برنامه‌های هوش مصنوعی تصور کنید - این یک روش استاندارد شده برای اتصال مدل‌های هوش مصنوعی به منابع داده و ابزارهای مختلف است.

## اهداف آموزشی

تا پایان این درس، قادر خواهید بود:

- محیط‌های توسعه MCP را در C#، Java، Python، TypeScript و Rust راه‌اندازی کنید
- سرورهای MCP پایه را با ویژگی‌های سفارشی (منابع، پرامپت‌ها و ابزارها) بسازید و ارائه دهید
- برنامه‌های میزبان ایجاد کنید که به سرورهای MCP متصل شوند
- پیاده‌سازی‌های MCP را تست و اشکال‌زدایی کنید

## راه‌اندازی محیط MCP شما

قبل از شروع کار با MCP، مهم است که محیط توسعه خود را آماده کرده و جریان کاری پایه را درک کنید. این بخش شما را از طریق مراحل اولیه راه‌اندازی برای شروع روان با MCP هدایت می‌کند.

### پیش‌نیازها

قبل از شروع توسعه MCP، مطمئن شوید که:

- **محیط توسعه**: برای زبان برنامه‌نویسی انتخابی شما (C#، Java، Python، TypeScript یا Rust)
- **IDE/ویرایشگر**: Visual Studio، Visual Studio Code، IntelliJ، Eclipse، PyCharm یا هر ویرایشگر کد مدرن دیگر
- **مدیریت بسته‌ها**: NuGet، Maven/Gradle، pip، npm/yarn، یا Cargo
- **کلیدهای API**: برای هر سرویس هوش مصنوعی که قصد استفاده در برنامه‌های میزبان خود را دارید

## ساختار پایه سرور MCP

یک سرور MCP معمولا شامل موارد زیر است:

- **پیکربندی سرور**: تنظیم پورت، احراز هویت و تنظیمات دیگر
- **منابع**: داده‌ها و کانتکست در دسترس مدل‌های زبانی بزرگ
- **ابزارها**: قابلیت‌هایی که مدل‌ها می‌توانند فراخوانی کنند
- **پرامپت‌ها**: قالب‌ها برای تولید یا ساختاردهی متن

در اینجا یک مثال ساده شده در TypeScript آمده است:

```typescript
import { McpServer, ResourceTemplate } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";

// ایجاد یک سرور MCP
const server = new McpServer({
  name: "Demo",
  version: "1.0.0"
});

// افزودن یک ابزار اضافی
server.tool("add",
  { a: z.number(), b: z.number() },
  async ({ a, b }) => ({
    content: [{ type: "text", text: String(a + b) }]
  })
);

// افزودن یک منبع خوش‌آمدگویی پویا
server.resource(
  "file",
  // پارامتر 'list' کنترل می‌کند که منبع چگونه فایل‌های موجود را لیست کند. تنظیم آن به undefined لیست کردن این منبع را غیرفعال می‌کند.
  new ResourceTemplate("file://{path}", { list: undefined }),
  async (uri, { path }) => ({
    contents: [{
      uri: uri.href,
      text: `File, ${path}!`
    }]
  })
);

// افزودن یک منبع فایل که محتوای فایل را می‌خواند
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

// شروع به دریافت پیام‌ها از ورودی استاندارد و ارسال پیام‌ها به خروجی استاندارد
const transport = new StdioServerTransport();
await server.connect(transport);
```

در کد بالا ما:

- کلاس‌های لازم را از SDK TypeScript MCP وارد کرده‌ایم.
- یک نمونه جدید از سرور MCP ساخته و پیکربندی کرده‌ایم.
- یک ابزار سفارشی (`calculator`) با یک تابع هندلر ثبت کرده‌ایم.
- سرور را برای گوش دادن به درخواست‌های ورودی MCP راه‌اندازی کرده‌ایم.

## آزمایش و اشکال‌زدایی

قبل از شروع به آزمایش سرور MCP خود، مهم است که ابزارهای موجود و بهترین روش‌ها برای اشکال‌زدایی را درک کنید. آزمایش موثر اطمینان می‌دهد که سرور شما مطابق انتظار عمل می‌کند و به شما کمک می‌کند تا مشکلات را سریع شناسایی و حل نمایید. بخش زیر روش‌های توصیه شده برای اعتبارسنجی پیاده‌سازی MCP شما را تشریح می‌کند.

MCP ابزارهایی برای کمک به آزمایش و اشکال‌زدایی سرورهای شما فراهم می‌کند:

- **ابزار Inspector**، این رابط گرافیکی به شما اجازه می‌دهد به سرور خود متصل شده و ابزارها، پرامپت‌ها و منابع خود را آزمایش کنید.
- **curl**، شما همچنین می‌توانید با استفاده از ابزار خط فرمانی مانند curl یا سایر مشتریانی که می‌توانند دستورات HTTP ایجاد و اجرا کنند به سرور خود متصل شوید.

### استفاده از MCP Inspector

[MCP Inspector](https://github.com/modelcontextprotocol/inspector) یک ابزار آزمایش بصری است که به شما کمک می‌کند:

1. **کشف قابلیت‌های سرور**: منابع، ابزارها و پرامپت‌های موجود را به طور خودکار شناسایی کنید
2. **آزمایش اجرای ابزارها**: پارامترهای مختلف را امتحان کنید و پاسخ‌ها را در زمان واقعی ببینید
3. **مشاهده فراداده سرور**: اطلاعات سرور، طرح‌ها و پیکربندی‌ها را بررسی کنید

```bash
# به عنوان مثال TypeScript، نصب و اجرای MCP Inspector
npx @modelcontextprotocol/inspector node build/index.js
```

وقتی دستورات بالا را اجرا می‌کنید، MCP Inspector یک رابط وب محلی در مرورگر شما باز می‌کند. انتظار دارید یک داشبورد نمایش داده شود که سرورهای MCP ثبت‌شده شما، ابزارها، منابع و پرامپت‌هایشان را به نمایش می‌گذارد. این رابط امکان آزمایش تعاملی اجرای ابزارها، بررسی فراداده سرور و مشاهده پاسخ‌های زمان واقعی را فراهم می‌کند، که اعتبارسنجی و اشکال‌زدایی پیاده‌سازی‌های سرور MCP شما را آسان‌تر می‌کند.

این هم یک اسکرین‌شات از ظاهر آن:

![MCP Inspector server connection](../../../../translated_images/fa/connected.73d1e042c24075d3.webp)

## مشکلات رایج راه‌اندازی و راه‌حل‌ها

| مشکل | راه‌حل ممکن |
|-------|-------------|
| اتصال رد شده | بررسی کنید آیا سرور در حال اجراست و پورت صحیح است |
| خطاهای اجرای ابزار | اعتبارسنجی پارامترها و مدیریت خطا را مرور کنید |
| شکست‌های احراز هویت | کلیدهای API و مجوزها را بررسی کنید |
| خطاهای اعتبارسنجی شِما | اطمینان حاصل کنید پارامترها با شمای تعریف شده مطابقت دارند |
| راه‌اندازی سرور انجام نمی‌شود | تداخل پورت یا وابستگی‌های ناقص را بررسی کنید |
| خطاهای CORS | هدرهای CORS مناسب برای درخواست‌های چندمبدا را پیکربندی کنید |
| مشکلات احراز هویت | صحت توکن و مجوزها را بررسی کنید |

## توسعه محلی

برای توسعه و آزمایش محلی، می‌توانید سرورهای MCP را مستقیما روی دستگاه خود اجرا کنید:

1. **راه‌اندازی فرآیند سرور**: برنامه سرور MCP خود را اجرا کنید
2. **پیکربندی شبکه**: اطمینان حاصل کنید سرور روی پورت مورد انتظار قابل دسترسی است
3. **اتصال مشتری‌ها**: از URLهای محلی مانند `http://localhost:3000` استفاده کنید

```bash
# نمونه: اجرای یک سرور MCP تایپ‌اسکریپت به‌صورت محلی
npm run start
# سرور در آدرس http://localhost:3000 در حال اجرا است
```

## ساخت اولین سرور MCP خود

ما در درس قبلی [مفاهیم اصلی](../../01-CoreConcepts/README.md) را پوشش دادیم، اکنون وقت آن است که آن دانش را به کار بگیریم.

### سرور چه کاری می‌تواند انجام دهد

قبل از شروع نوشتن کد، بیایید به خاطر بیاوریم که یک سرور چه قابلیت‌هایی دارد:

یک سرور MCP می‌تواند برای مثال:

- به فایل‌ها و پایگاه‌های داده محلی دسترسی داشته باشد
- به APIهای از راه دور متصل شود
- محاسبات انجام دهد
- با ابزارها و سرویس‌های دیگر ادغام شود
- یک رابط کاربری برای تعامل فراهم کند

عالی است، حالا که می‌دانیم چه کارهایی می‌توان انجام داد، بیایید برنامه‌نویسی را شروع کنیم.

## تمرین: ایجاد یک سرور

برای ایجاد سرور، باید مراحل زیر را دنبال کنید:

- SDK MCP را نصب کنید.
- یک پروژه ایجاد و ساختار پروژه را تنظیم کنید.
- کد سرور را بنویسید.
- سرور را تست کنید.

### -1- ایجاد پروژه

#### TypeScript

```sh
# ایجاد پوشه پروژه و راه‌اندازی پروژه npm
mkdir calculator-server
cd calculator-server
npm init -y
```

#### Python

```sh
# ایجاد پوشه پروژه
mkdir calculator-server
cd calculator-server
# پوشه را در ویژوال استودیو کد باز کنید - اگر از IDE دیگری استفاده می‌کنید این مرحله را رد کنید
code .
```

#### .NET

```sh
dotnet new console -n McpCalculatorServer
cd McpCalculatorServer
```

#### Java

برای Java، یک پروژه Spring Boot بسازید:

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

فایل زیپ را استخراج کنید:

```bash
unzip calculator-server.zip -d calculator-server
cd calculator-server
# به صورت اختیاری، تست بدون استفاده را حذف کنید
rm -rf src/test/java
```

پیکربندی کامل زیر را به فایل *pom.xml* خود اضافه کنید:

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

### -2- افزودن وابستگی‌ها

حال که پروژه خود را ایجاد کرده‌اید، بیایید وابستگی‌ها را اضافه کنیم:

#### TypeScript

```sh
# اگر قبلاً نصب نشده است، TypeScript را به صورت سراسری نصب کنید
npm install typescript -g

# MCP SDK و Zod را برای اعتبارسنجی طرح نصب کنید
npm install @modelcontextprotocol/sdk zod
npm install -D @types/node typescript
```

#### Python

```sh
# یک محیط مجازی ایجاد کنید و وابستگی‌ها را نصب کنید
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

### -3- ایجاد فایل‌های پروژه

#### TypeScript

فایل *package.json* را باز کرده و محتوای آن را با موارد زیر جایگزین کنید تا اطمینان حاصل شود می‌توانید سرور را بسازید و اجرا کنید:

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

یک فایل *tsconfig.json* با محتوای زیر بسازید:

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

یک دایرکتوری برای کد منبع خود ایجاد کنید:

```sh
mkdir src
touch src/index.ts
```

#### Python

فایل *server.py* بسازید

```sh
touch server.py
```

#### .NET

بسته‌های NuGet مورد نیاز را نصب کنید:

```sh
dotnet add package ModelContextProtocol --prerelease
dotnet add package Microsoft.Extensions.Hosting
```

#### Java

برای پروژه‌های Java Spring Boot، ساختار پروژه به طور خودکار ایجاد می‌شود.

#### Rust

برای Rust، فایل *src/main.rs* به طور پیش‌فرض هنگام اجرای `cargo init` ساخته می‌شود. فایل را باز کرده و کد پیش‌فرض را حذف کنید.

### -4- ایجاد کد سرور

#### TypeScript

فایل *index.ts* را بسازید و کد زیر را اضافه کنید:

```typescript
import { McpServer, ResourceTemplate } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";
 
// ایجاد یک سرور MCP
const server = new McpServer({
  name: "Calculator MCP Server",
  version: "1.0.0"
});
```

اکنون یک سرور دارید، اما کاری انجام نمی‌دهد، بیایید آن را اصلاح کنیم.

#### Python

```python
# سرور.py
from mcp.server.fastmcp import FastMCP

# ایجاد یک سرور MCP
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

برای Java، اجزای اصلی سرور را بسازید. ابتدا کلاس برنامه اصلی را اصلاح کنید:

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

سرویس ماشین حساب را ایجاد کنید *src/main/java/com/microsoft/mcp/sample/server/service/CalculatorService.java*:

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

**اجزای اختیاری برای سرویس آماده تولید:**

پیکربندی راه‌اندازی را بسازید *src/main/java/com/microsoft/mcp/sample/server/config/StartupConfig.java*:

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

کنترلر سلامت را بسازید *src/main/java/com/microsoft/mcp/sample/server/controller/HealthController.java*:

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

دستگیره خطا را بسازید *src/main/java/com/microsoft/mcp/sample/server/exception/GlobalExceptionHandler.java*:

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

        // گیرنده‌ها
        public String getCode() { return code; }
        public String getMessage() { return message; }
    }
}
```

یک بنر سفارشی بسازید *src/main/resources/banner.txt*:

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

کد زیر را به بالای فایل *src/main.rs* اضافه کنید. این کتابخانه‌ها و ماژول‌های لازم برای سرور MCP شما را وارد می‌کند.

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

سرور ماشین حساب یک نمونه ساده خواهد بود که می‌تواند دو عدد را با هم جمع کند. بیایید یک ساختار برای نشان دادن درخواست ماشین حساب ایجاد کنیم.

```rust
#[derive(Debug, serde::Deserialize, schemars::JsonSchema)]
pub struct CalculatorRequest {
    pub a: f64,
    pub b: f64,
}
```

بعد، یک ساختار برای نشان دادن سرور ماشین حساب بسازید. این ساختار نگهدارنده ابزار روتر است که برای ثبت ابزارها استفاده می‌شود.

```rust
#[derive(Debug, Clone)]
pub struct Calculator {
    tool_router: ToolRouter<Self>,
}
```

حالا، می‌توانیم ساختار `Calculator` را پیاده‌سازی کنیم تا یک نمونه جدید از سرور ساخته و هندلر سرور را برای ارائه اطلاعات سرور پیاده‌سازی کنیم.

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

در نهایت، باید تابع اصلی را پیاده‌سازی کنیم تا سرور را راه‌اندازی کند. این تابع یک نمونه از ساختار `Calculator` ایجاد کرده و آن را بر روی ورودی/خروجی استاندارد سرو می‌کند.

```rust
#[tokio::main]
async fn main() -> Result<(), Box<dyn Error>> {
    let service = Calculator::new().serve(stdio()).await?;
    service.waiting().await?;
    Ok(())
}
```

اکنون سرور آماده ارائه اطلاعات پایه درباره خود است. در مرحله بعد، یک ابزار برای انجام جمع اضافه خواهیم کرد.

### -5- افزودن یک ابزار و یک منبع

با اضافه کردن کد زیر، یک ابزار و یک منبع اضافه کنید:

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

ابزار شما پارامترهای `a` و `b` را می‌گیرد و تابعی اجرا می‌کند که پاسخ را به فرم زیر تولید می‌کند:

```typescript
{
  contents: [{
    type: "text", content: "some content"
  }]
}
```

منبع شما از طریق رشته "greeting" دسترسی دارد، پارامتر `name` را می‌گیرد و پاسخی مشابه ابزار تولید می‌کند:

```typescript
{
  uri: "<href>",
  text: "a text"
}
```

#### Python

```python
# افزودن ابزار جمع
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


# افزودن منبع خوش‌آمدگویی پویا
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}!"
```

در کد بالا ما:

- یک ابزار `add` تعریف کردیم که پارامترهای `a` و `b` هر دو عدد صحیح هستند.
- یک منبع به نام `greeting` ایجاد کردیم که پارامتر `name` را می‌گیرد.

#### .NET

این را به فایل Program.cs خود اضافه کنید:

```csharp
[McpServerToolType]
public static class CalculatorTool
{
    [McpServerTool, Description("Adds two numbers")]
    public static string Add(int a, int b) => $"Sum {a + b}";
}
```

#### Java

ابزارها در مرحله قبل ایجاد شده‌اند.

#### Rust

داخل بلوک `impl Calculator` ابزار جدیدی اضافه کنید:

```rust
#[tool(description = "Adds a and b")]
async fn add(
    &self,
    Parameters(CalculatorRequest { a, b }): Parameters<CalculatorRequest>,
) -> String {
    (a + b).to_string()
}
```

### -6- کد نهایی

آخرین کدی که نیاز داریم را اضافه کنیم تا سرور بتواند شروع به کار کند:

#### TypeScript

```typescript
// شروع به دریافت پیام‌ها از stdin و ارسال پیام‌ها روی stdout
const transport = new StdioServerTransport();
await server.connect(transport);
```

کد کامل به شرح زیر است:

```typescript
// index.ts
import { McpServer, ResourceTemplate } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";

// ساخت یک سرور MCP
const server = new McpServer({
  name: "Calculator MCP Server",
  version: "1.0.0"
});

// افزودن یک ابزار افزودنی
server.tool(
  "add",
  { a: z.number(), b: z.number() },
  async ({ a, b }) => ({
    content: [{ type: "text", text: String(a + b) }]
  })
);

// افزودن یک منبع خوش‌آمدگویی پویا
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

// شروع دریافت پیام‌ها از stdin و ارسال پیام‌ها به stdout
const transport = new StdioServerTransport();
server.connect(transport);
```

#### Python

```python
# سرور.py
from mcp.server.fastmcp import FastMCP

# ایجاد یک سرور MCP
mcp = FastMCP("Demo")


# افزودن یک ابزار جمع
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


# افزودن یک منبع خوش‌آمدگویی پویا
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}!"

# بلوک اجرای اصلی - این برای اجرای سرور لازم است
if __name__ == "__main__":
    mcp.run()
```

#### .NET

یک فایل Program.cs با محتوای زیر ایجاد کنید:

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

کلاس اصلی برنامه شما باید به این شکل کامل باشد:

```java
// برنامه McpServerApplication.java
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

کد نهایی برای سرور Rust باید به این صورت باشد:

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

### -7- تست سرور

سرور را با دستور زیر اجرا کنید:

#### TypeScript

```sh
npm run build
```

#### Python

```sh
mcp run server.py
```

> برای استفاده از MCP Inspector، از `mcp dev server.py` استفاده کنید که به طور خودکار Inspector را راه‌اندازی کرده و توکن جلسه پراکسی مورد نیاز را ارائه می‌دهد. اگر از `mcp run server.py` استفاده می‌کنید، باید به صورت دستی Inspector را راه‌اندازی کرده و اتصال را پیکربندی کنید.

#### .NET

اطمینان حاصل کنید که در دایرکتوری پروژه خود هستید:

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

دستورات زیر را برای فرمت‌بندی و اجرای سرور اجرا کنید:

```sh
cargo fmt
cargo run
```

### -8- اجرا با استفاده از Inspector

Inspector یک ابزار عالی است که می‌تواند سرور شما را راه‌اندازی کند و به شما اجازه می‌دهد با آن تعامل داشته باشید تا مطمئن شوید که درست کار می‌کند. بیایید آن را راه‌اندازی کنیم:

> [!NOTE]
> ممکن است در فیلد "command" متفاوت به نظر برسد چون شامل دستور اجرای سرور با زمان اجرای خاص شما است.

#### TypeScript

```sh
npx @modelcontextprotocol/inspector node build/index.js
```

یا آن را به *package.json* خود به این شکل اضافه کنید: `"inspector": "npx @modelcontextprotocol/inspector node build/index.js"` و سپس `npm run inspector` را اجرا کنید.

#### Python

پایتون یک ابزار Node.js به نام inspector را می‌پیچاند. امکان فراخوانی این ابزار به این شکل وجود دارد:

```sh
mcp dev server.py
```

با این حال، همه روش‌های موجود در ابزار را پیاده‌سازی نمی‌کند، بنابراین توصیه می‌شود ابزار Node.js را مستقیما به شکل زیر اجرا کنید:

```sh
npx @modelcontextprotocol/inspector mcp run server.py
```

اگر از ابزاری یا IDE‌ای استفاده می‌کنید که به شما اجازه می‌دهد دستورات و آرگومان‌ها را برای اجرای اسکریپت‌ها پیکربندی کنید،
مطمئن شوید که در قسمت `Command` مقدار `python` و در قسمت `Arguments` مقدار `server.py` را تنظیم کرده‌اید. این کار تضمین می‌کند که اسکریپت به درستی اجرا شود.

#### .NET

مطمئن شوید که در دایرکتوری پروژه‌تان هستید:

```sh
cd McpCalculatorServer
npx @modelcontextprotocol/inspector dotnet run
```

#### Java

اطمینان حاصل کنید که سرور ماشین حساب شما در حال اجرا است  
سپس Inspector را اجرا کنید:

```cmd
npx @modelcontextprotocol/inspector
```

در رابط وب Inspector:

1. "SSE" را به عنوان نوع انتقال انتخاب کنید  
2. URL را به صورت زیر تنظیم کنید: `http://localhost:8080/sse`  
3. روی "Connect" کلیک کنید

![Connect](../../../../translated_images/fa/tool.163d33e3ee307e20.webp)

**شما اکنون به سرور متصل شده‌اید**  
**بخش تست سرور Java اکنون تکمیل شده است**

بخش بعدی مربوط به تعامل با سرور است.

شما باید رابط کاربری زیر را مشاهده کنید:

![Connect](../../../../translated_images/fa/connect.141db0b2bd05f096.webp)

1. با انتخاب دکمه Connect به سرور متصل شوید  
  پس از اتصال به سرور، باید موارد زیر را مشاهده کنید:

  ![Connected](../../../../translated_images/fa/connected.73d1e042c24075d3.webp)

1. "Tools" و سپس "listTools" را انتخاب کنید، باید "Add" ظاهر شود، "Add" را انتخاب کرده و مقادیر پارامترها را پر کنید.

  شما باید پاسخ زیر را مشاهده کنید، یعنی نتیجه‌ای از ابزار "add":

  ![Result of running add](../../../../translated_images/fa/ran-tool.a5a6ee878c1369ec.webp)

تبریک می‌گوییم، شما موفق شده‌اید اولین سرور خود را ایجاد و اجرا کنید!

#### Rust

برای اجرای سرور Rust با MCP Inspector CLI، از فرمان زیر استفاده کنید:

```sh
npx @modelcontextprotocol/inspector cargo run --cli --method tools/call --tool-name add --tool-arg a=1 b=2
```

### SDKهای رسمی

MCP SDKهای رسمی برای زبان‌های مختلف فراهم می‌کند:

- [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk) - با همکاری مایکروسافت نگهداری می‌شود  
- [Java SDK](https://github.com/modelcontextprotocol/java-sdk) - با همکاری Spring AI نگهداری می‌شود  
- [TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk) - پیاده‌سازی رسمی TypeScript  
- [Python SDK](https://github.com/modelcontextprotocol/python-sdk) - پیاده‌سازی رسمی Python  
- [Kotlin SDK](https://github.com/modelcontextprotocol/kotlin-sdk) - پیاده‌سازی رسمی Kotlin  
- [Swift SDK](https://github.com/modelcontextprotocol/swift-sdk) - با همکاری Loopwork AI نگهداری می‌شود  
- [Rust SDK](https://github.com/modelcontextprotocol/rust-sdk) - پیاده‌سازی رسمی Rust  

## نکات کلیدی

- راه‌اندازی محیط توسعه MCP با SDKهای خاص هر زبان ساده است  
- ساخت سرورهای MCP شامل ایجاد و ثبت ابزارها با شِماهای واضح است  
- تست و اشکال‌زدایی برای پیاده‌سازی‌های قابل اعتماد MCP ضروری است  

## نمونه‌ها

- [ماشین حساب Java](../samples/java/calculator/README.md)  
- [ماشین حساب .Net](../../../../03-GettingStarted/samples/csharp)  
- [ماشین حساب JavaScript](../samples/javascript/README.md)  
- [ماشین حساب TypeScript](../samples/typescript/README.md)  
- [ماشین حساب Python](../../../../03-GettingStarted/samples/python)  
- [ماشین حساب Rust](../../../../03-GettingStarted/samples/rust)  

## تمرین

یک سرور MCP ساده با یک ابزار از انتخاب خود ایجاد کنید:

1. ابزار را در زبان ترجیحی خود پیاده‌سازی کنید (.NET، Java، Python، TypeScript یا Rust)  
2. پارامترهای ورودی و مقادیر بازگشتی را تعریف کنید  
3. ابزار inspector را اجرا کنید تا مطمئن شوید سرور همان‌طور که انتظار می‌رود کار می‌کند  
4. پیاده‌سازی را با ورودی‌های مختلف آزمایش کنید  

## راه حل

[راه حل](./solution/README.md)

## منابع اضافی

- [ساخت عوامل با استفاده از Model Context Protocol در Azure](https://learn.microsoft.com/azure/developer/ai/intro-agents-mcp)  
- [MCP از راه دور با Azure Container Apps (Node.js/TypeScript/JavaScript)](https://learn.microsoft.com/samples/azure-samples/mcp-container-ts/mcp-container-ts/)  
- [عامل OpenAI MCP در .NET](https://learn.microsoft.com/samples/azure-samples/openai-mcp-agent-dotnet/openai-mcp-agent-dotnet/)  

## مرحله بعد

مرحله بعد: [شروع به کار با کلاینت‌های MCP](../02-client/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**توضیح مسئولیت**:
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما در تلاش برای دقت هستیم، لطفاً به خاطر داشته باشید که ترجمه‌های خودکار ممکن است حاوی خطاها یا نادرستی‌هایی باشند. سند اصلی به زبان بومی خود باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حیاتی، ترجمه حرفه‌ای انسانی توصیه می‌شود. ما مسئول هیچ گونه سوء تفاهم یا تفسیر نادرست ناشی از استفاده این ترجمه نیستیم.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->