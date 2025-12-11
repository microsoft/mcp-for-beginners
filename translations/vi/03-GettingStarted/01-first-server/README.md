<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8fdac7600a5f4722643d0f14e15ac259",
  "translation_date": "2025-12-11T07:13:10+00:00",
  "source_file": "03-GettingStarted/01-first-server/README.md",
  "language_code": "vi"
}
-->
# Bắt đầu với MCP

Chào mừng bạn đến với những bước đầu tiên với Model Context Protocol (MCP)! Dù bạn mới làm quen với MCP hay muốn nâng cao hiểu biết, hướng dẫn này sẽ dẫn bạn qua quá trình thiết lập và phát triển cơ bản. Bạn sẽ khám phá cách MCP cho phép tích hợp liền mạch giữa các mô hình AI và ứng dụng, đồng thời học cách nhanh chóng chuẩn bị môi trường để xây dựng và thử nghiệm các giải pháp sử dụng MCP.

> TLDR; Nếu bạn xây dựng ứng dụng AI, bạn biết rằng bạn có thể thêm công cụ và các tài nguyên khác vào LLM (mô hình ngôn ngữ lớn), để làm cho LLM hiểu biết hơn. Tuy nhiên nếu bạn đặt các công cụ và tài nguyên đó trên một máy chủ, khả năng của ứng dụng và máy chủ có thể được sử dụng bởi bất kỳ khách hàng nào có hoặc không có LLM.

## Tổng quan

Bài học này cung cấp hướng dẫn thực tiễn về cách thiết lập môi trường MCP và xây dựng các ứng dụng MCP đầu tiên của bạn. Bạn sẽ học cách thiết lập các công cụ và framework cần thiết, xây dựng các máy chủ MCP cơ bản, tạo ứng dụng host và thử nghiệm các triển khai của bạn.

Model Context Protocol (MCP) là một giao thức mở chuẩn hóa cách các ứng dụng cung cấp ngữ cảnh cho LLM. Hãy nghĩ về MCP như một cổng USB-C cho các ứng dụng AI - nó cung cấp một cách chuẩn hóa để kết nối các mô hình AI với các nguồn dữ liệu và công cụ khác nhau.

## Mục tiêu học tập

Kết thúc bài học này, bạn sẽ có thể:

- Thiết lập môi trường phát triển cho MCP bằng C#, Java, Python, TypeScript và Rust
- Xây dựng và triển khai các máy chủ MCP cơ bản với các tính năng tùy chỉnh (tài nguyên, lời nhắc, và công cụ)
- Tạo các ứng dụng host kết nối với máy chủ MCP
- Thử nghiệm và gỡ lỗi các triển khai MCP

## Thiết lập môi trường MCP của bạn

Trước khi bắt đầu làm việc với MCP, điều quan trọng là chuẩn bị môi trường phát triển và hiểu quy trình làm việc cơ bản. Phần này sẽ hướng dẫn bạn qua các bước thiết lập ban đầu để đảm bảo khởi đầu suôn sẻ với MCP.

### Yêu cầu trước

Trước khi bắt đầu phát triển MCP, hãy đảm bảo bạn có:

- **Môi trường phát triển**: Cho ngôn ngữ bạn chọn (C#, Java, Python, TypeScript hoặc Rust)
- **IDE/Trình soạn thảo**: Visual Studio, Visual Studio Code, IntelliJ, Eclipse, PyCharm hoặc bất kỳ trình soạn thảo mã hiện đại nào
- **Trình quản lý gói**: NuGet, Maven/Gradle, pip, npm/yarn hoặc Cargo
- **Khóa API**: Cho bất kỳ dịch vụ AI nào bạn dự định sử dụng trong ứng dụng host của mình

## Cấu trúc máy chủ MCP cơ bản

Một máy chủ MCP thường bao gồm:

- **Cấu hình máy chủ**: Thiết lập cổng, xác thực và các cài đặt khác
- **Tài nguyên**: Dữ liệu và ngữ cảnh được cung cấp cho LLM
- **Công cụ**: Chức năng mà các mô hình có thể gọi
- **Lời nhắc**: Mẫu để tạo hoặc cấu trúc văn bản

Dưới đây là ví dụ đơn giản bằng TypeScript:

```typescript
import { McpServer, ResourceTemplate } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";

// Tạo một máy chủ MCP
const server = new McpServer({
  name: "Demo",
  version: "1.0.0"
});

// Thêm một công cụ cộng
server.tool("add",
  { a: z.number(), b: z.number() },
  async ({ a, b }) => ({
    content: [{ type: "text", text: String(a + b) }]
  })
);

// Thêm một tài nguyên chào hỏi động
server.resource(
  "file",
  // Tham số 'list' kiểm soát cách tài nguyên liệt kê các tệp có sẵn. Đặt nó thành undefined sẽ vô hiệu hóa việc liệt kê cho tài nguyên này.
  new ResourceTemplate("file://{path}", { list: undefined }),
  async (uri, { path }) => ({
    contents: [{
      uri: uri.href,
      text: `File, ${path}!`
    }]
  })
);

// Thêm một tài nguyên tệp đọc nội dung tệp
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

// Bắt đầu nhận tin nhắn trên stdin và gửi tin nhắn trên stdout
const transport = new StdioServerTransport();
await server.connect(transport);
```

Trong đoạn mã trên chúng ta:

- Nhập các lớp cần thiết từ MCP TypeScript SDK.
- Tạo và cấu hình một phiên bản máy chủ MCP mới.
- Đăng ký một công cụ tùy chỉnh (`calculator`) với một hàm xử lý.
- Khởi động máy chủ để lắng nghe các yêu cầu MCP đến.

## Thử nghiệm và gỡ lỗi

Trước khi bắt đầu thử nghiệm máy chủ MCP của bạn, điều quan trọng là hiểu các công cụ có sẵn và các thực hành tốt nhất để gỡ lỗi. Thử nghiệm hiệu quả đảm bảo máy chủ của bạn hoạt động như mong đợi và giúp bạn nhanh chóng xác định và giải quyết các vấn đề. Phần sau đây trình bày các phương pháp được khuyến nghị để xác thực triển khai MCP của bạn.

MCP cung cấp các công cụ giúp bạn thử nghiệm và gỡ lỗi máy chủ:

- **Công cụ Inspector**, giao diện đồ họa này cho phép bạn kết nối với máy chủ và thử nghiệm các công cụ, lời nhắc và tài nguyên của bạn.
- **curl**, bạn cũng có thể kết nối với máy chủ bằng công cụ dòng lệnh như curl hoặc các khách hàng khác có thể tạo và chạy các lệnh HTTP.

### Sử dụng MCP Inspector

[MCP Inspector](https://github.com/modelcontextprotocol/inspector) là công cụ thử nghiệm trực quan giúp bạn:

1. **Khám phá khả năng máy chủ**: Tự động phát hiện các tài nguyên, công cụ và lời nhắc có sẵn
2. **Thử nghiệm thực thi công cụ**: Thử các tham số khác nhau và xem phản hồi theo thời gian thực
3. **Xem metadata máy chủ**: Kiểm tra thông tin máy chủ, sơ đồ và cấu hình

```bash
# ví dụ TypeScript, cài đặt và chạy MCP Inspector
npx @modelcontextprotocol/inspector node build/index.js
```

Khi bạn chạy các lệnh trên, MCP Inspector sẽ khởi chạy giao diện web cục bộ trong trình duyệt của bạn. Bạn có thể mong đợi thấy một bảng điều khiển hiển thị các máy chủ MCP đã đăng ký, các công cụ, tài nguyên và lời nhắc có sẵn của chúng. Giao diện cho phép bạn tương tác thử nghiệm thực thi công cụ, kiểm tra metadata máy chủ và xem phản hồi theo thời gian thực, giúp bạn dễ dàng xác thực và gỡ lỗi các triển khai máy chủ MCP của mình.

Dưới đây là ảnh chụp màn hình của giao diện:

![MCP Inspector server connection](../../../../translated_images/connected.73d1e042c24075d386cacdd4ee7cd748c16364c277d814e646ff2f7b5eefde85.vi.png)

## Các vấn đề thiết lập phổ biến và giải pháp

| Vấn đề | Giải pháp khả thi |
|-------|-------------------|
| Kết nối bị từ chối | Kiểm tra xem máy chủ có đang chạy và cổng có đúng không |
| Lỗi thực thi công cụ | Xem lại xác thực tham số và xử lý lỗi |
| Lỗi xác thực | Xác minh khóa API và quyền truy cập |
| Lỗi xác thực sơ đồ | Đảm bảo tham số phù hợp với sơ đồ đã định nghĩa |
| Máy chủ không khởi động | Kiểm tra xung đột cổng hoặc thiếu phụ thuộc |
| Lỗi CORS | Cấu hình đúng header CORS cho các yêu cầu đa nguồn |
| Vấn đề xác thực | Xác minh tính hợp lệ của token và quyền truy cập |

## Phát triển cục bộ

Để phát triển và thử nghiệm cục bộ, bạn có thể chạy các máy chủ MCP trực tiếp trên máy của mình:

1. **Khởi động tiến trình máy chủ**: Chạy ứng dụng máy chủ MCP của bạn
2. **Cấu hình mạng**: Đảm bảo máy chủ có thể truy cập trên cổng mong muốn
3. **Kết nối khách hàng**: Sử dụng URL kết nối cục bộ như `http://localhost:3000`

```bash
# Ví dụ: Chạy một máy chủ MCP TypeScript cục bộ
npm run start
# Máy chủ đang chạy tại http://localhost:3000
```

## Xây dựng máy chủ MCP đầu tiên của bạn

Chúng ta đã đề cập đến [Các khái niệm cốt lõi](/01-CoreConcepts/README.md) trong bài học trước, giờ là lúc áp dụng kiến thức đó.

### Máy chủ có thể làm gì

Trước khi bắt đầu viết mã, hãy nhắc lại máy chủ có thể làm gì:

Một máy chủ MCP có thể ví dụ:

- Truy cập các tập tin và cơ sở dữ liệu cục bộ
- Kết nối với các API từ xa
- Thực hiện các phép tính
- Tích hợp với các công cụ và dịch vụ khác
- Cung cấp giao diện người dùng để tương tác

Tuyệt vời, giờ chúng ta đã biết những gì có thể làm, hãy bắt đầu viết mã.

## Bài tập: Tạo máy chủ

Để tạo một máy chủ, bạn cần thực hiện các bước sau:

- Cài đặt MCP SDK.
- Tạo một dự án và thiết lập cấu trúc dự án.
- Viết mã máy chủ.
- Thử nghiệm máy chủ.

### -1- Tạo dự án

#### TypeScript

```sh
# Tạo thư mục dự án và khởi tạo dự án npm
mkdir calculator-server
cd calculator-server
npm init -y
```

#### Python

```sh
# Tạo thư mục dự án
mkdir calculator-server
cd calculator-server
# Mở thư mục trong Visual Studio Code - Bỏ qua nếu bạn đang sử dụng IDE khác
code .
```

#### .NET

```sh
dotnet new console -n McpCalculatorServer
cd McpCalculatorServer
```

#### Java

Đối với Java, tạo một dự án Spring Boot:

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

Giải nén file zip:

```bash
unzip calculator-server.zip -d calculator-server
cd calculator-server
# tùy chọn loại bỏ các bài kiểm tra không sử dụng
rm -rf src/test/java
```

Thêm cấu hình đầy đủ sau vào file *pom.xml* của bạn:

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

### -2- Thêm phụ thuộc

Bây giờ bạn đã tạo dự án, tiếp theo hãy thêm các phụ thuộc:

#### TypeScript

```sh
# Nếu chưa được cài đặt, hãy cài đặt TypeScript toàn cục
npm install typescript -g

# Cài đặt MCP SDK và Zod để xác thực schema
npm install @modelcontextprotocol/sdk zod
npm install -D @types/node typescript
```

#### Python

```sh
# Tạo một môi trường ảo và cài đặt các phụ thuộc
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

### -3- Tạo các file dự án

#### TypeScript

Mở file *package.json* và thay thế nội dung bằng đoạn sau để đảm bảo bạn có thể build và chạy máy chủ:

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

Tạo file *tsconfig.json* với nội dung sau:

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

Tạo thư mục cho mã nguồn của bạn:

```sh
mkdir src
touch src/index.ts
```

#### Python

Tạo file *server.py*

```sh
touch server.py
```

#### .NET

Cài đặt các gói NuGet cần thiết:

```sh
dotnet add package ModelContextProtocol --prerelease
dotnet add package Microsoft.Extensions.Hosting
```

#### Java

Đối với dự án Java Spring Boot, cấu trúc dự án được tạo tự động.

#### Rust

Đối với Rust, file *src/main.rs* được tạo mặc định khi bạn chạy `cargo init`. Mở file và xóa mã mặc định.

### -4- Tạo mã máy chủ

#### TypeScript

Tạo file *index.ts* và thêm đoạn mã sau:

```typescript
import { McpServer, ResourceTemplate } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";
 
// Tạo một máy chủ MCP
const server = new McpServer({
  name: "Calculator MCP Server",
  version: "1.0.0"
});
```

Bây giờ bạn đã có máy chủ, nhưng nó chưa làm được nhiều, hãy sửa điều đó.

#### Python

```python
# server.py
from mcp.server.fastmcp import FastMCP

# Tạo một máy chủ MCP
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

Đối với Java, tạo các thành phần máy chủ cốt lõi. Đầu tiên, sửa đổi lớp ứng dụng chính:

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

Tạo dịch vụ calculator *src/main/java/com/microsoft/mcp/sample/server/service/CalculatorService.java*:

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

**Các thành phần tùy chọn cho dịch vụ sẵn sàng sản xuất:**

Tạo cấu hình khởi động *src/main/java/com/microsoft/mcp/sample/server/config/StartupConfig.java*:

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

Tạo bộ điều khiển sức khỏe *src/main/java/com/microsoft/mcp/sample/server/controller/HealthController.java*:

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

Tạo trình xử lý ngoại lệ *src/main/java/com/microsoft/mcp/sample/server/exception/GlobalExceptionHandler.java*:

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

        // Các phương thức lấy giá trị
        public String getCode() { return code; }
        public String getMessage() { return message; }
    }
}
```

Tạo banner tùy chỉnh *src/main/resources/banner.txt*:

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

Thêm đoạn mã sau vào đầu file *src/main.rs*. Đoạn này nhập các thư viện và module cần thiết cho máy chủ MCP của bạn.

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

Máy chủ calculator sẽ là một máy chủ đơn giản có thể cộng hai số lại với nhau. Hãy tạo một struct để đại diện cho yêu cầu calculator.

```rust
#[derive(Debug, serde::Deserialize, schemars::JsonSchema)]
pub struct CalculatorRequest {
    pub a: f64,
    pub b: f64,
}
```

Tiếp theo, tạo một struct để đại diện cho máy chủ calculator. Struct này sẽ giữ bộ định tuyến công cụ, được dùng để đăng ký các công cụ.

```rust
#[derive(Debug, Clone)]
pub struct Calculator {
    tool_router: ToolRouter<Self>,
}
```

Bây giờ, chúng ta có thể triển khai struct `Calculator` để tạo một phiên bản mới của máy chủ và triển khai trình xử lý máy chủ để cung cấp thông tin máy chủ.

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

Cuối cùng, chúng ta cần triển khai hàm main để khởi động máy chủ. Hàm này sẽ tạo một phiên bản của struct `Calculator` và phục vụ nó qua đầu vào/đầu ra chuẩn.

```rust
#[tokio::main]
async fn main() -> Result<(), Box<dyn Error>> {
    let service = Calculator::new().serve(stdio()).await?;
    service.waiting().await?;
    Ok(())
}
```

Máy chủ hiện đã được thiết lập để cung cấp thông tin cơ bản về chính nó. Tiếp theo, chúng ta sẽ thêm một công cụ để thực hiện phép cộng.

### -5- Thêm công cụ và tài nguyên

Thêm một công cụ và một tài nguyên bằng cách thêm đoạn mã sau:

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

Công cụ của bạn nhận các tham số `a` và `b` và chạy một hàm tạo ra phản hồi theo dạng:

```typescript
{
  contents: [{
    type: "text", content: "some content"
  }]
}
```

Tài nguyên của bạn được truy cập qua chuỗi "greeting" và nhận tham số `name` và tạo ra phản hồi tương tự công cụ:

```typescript
{
  uri: "<href>",
  text: "a text"
}
```

#### Python

```python
# Thêm một công cụ cộng
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


# Thêm một tài nguyên chào hỏi động
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}!"
```

Trong đoạn mã trên chúng ta đã:

- Định nghĩa công cụ `add` nhận các tham số `a` và `b`, cả hai đều là số nguyên.
- Tạo tài nguyên có tên `greeting` nhận tham số `name`.

#### .NET

Thêm đoạn này vào file Program.cs của bạn:

```csharp
[McpServerToolType]
public static class CalculatorTool
{
    [McpServerTool, Description("Adds two numbers")]
    public static string Add(int a, int b) => $"Sum {a + b}";
}
```

#### Java

Các công cụ đã được tạo trong bước trước.

#### Rust

Thêm một công cụ mới bên trong khối `impl Calculator`:

```rust
#[tool(description = "Adds a and b")]
async fn add(
    &self,
    Parameters(CalculatorRequest { a, b }): Parameters<CalculatorRequest>,
) -> String {
    (a + b).to_string()
}
```

### -6- Mã hoàn chỉnh

Hãy thêm đoạn mã cuối cùng cần thiết để máy chủ có thể khởi động:

#### TypeScript

```typescript
// Bắt đầu nhận tin nhắn trên stdin và gửi tin nhắn trên stdout
const transport = new StdioServerTransport();
await server.connect(transport);
```

Dưới đây là mã đầy đủ:

```typescript
// index.ts
import { McpServer, ResourceTemplate } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";

// Tạo một máy chủ MCP
const server = new McpServer({
  name: "Calculator MCP Server",
  version: "1.0.0"
});

// Thêm một công cụ cộng
server.tool(
  "add",
  { a: z.number(), b: z.number() },
  async ({ a, b }) => ({
    content: [{ type: "text", text: String(a + b) }]
  })
);

// Thêm một tài nguyên chào hỏi động
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

// Bắt đầu nhận tin nhắn trên stdin và gửi tin nhắn trên stdout
const transport = new StdioServerTransport();
server.connect(transport);
```

#### Python

```python
# server.py
from mcp.server.fastmcp import FastMCP

# Tạo một máy chủ MCP
mcp = FastMCP("Demo")


# Thêm một công cụ cộng
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


# Thêm một tài nguyên chào hỏi động
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}!"

# Khối thực thi chính - điều này cần thiết để chạy máy chủ
if __name__ == "__main__":
    mcp.run()
```

#### .NET

Tạo file Program.cs với nội dung sau:

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

Lớp ứng dụng chính hoàn chỉnh của bạn nên trông như sau:

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

Mã cuối cùng cho máy chủ Rust nên trông như sau:

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

### -7- Thử nghiệm máy chủ

Khởi động máy chủ với lệnh sau:

#### TypeScript

```sh
npm run build
```

#### Python

```sh
mcp run server.py
```

> Để sử dụng MCP Inspector, dùng `mcp dev server.py` sẽ tự động khởi chạy Inspector và cung cấp token phiên proxy cần thiết. Nếu dùng `mcp run server.py`, bạn sẽ cần khởi động Inspector thủ công và cấu hình kết nối.

#### .NET

Đảm bảo bạn đang ở thư mục dự án:

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

Chạy các lệnh sau để định dạng và chạy máy chủ:

```sh
cargo fmt
cargo run
```

### -8- Chạy bằng inspector

Inspector là công cụ tuyệt vời có thể khởi động máy chủ của bạn và cho phép bạn tương tác với nó để thử nghiệm xem nó hoạt động. Hãy khởi động nó:

> [!NOTE]
> nó có thể trông khác trong trường "command" vì nó chứa lệnh chạy máy chủ với runtime cụ thể của bạn.

#### TypeScript

```sh
npx @modelcontextprotocol/inspector node build/index.js
```

hoặc thêm nó vào *package.json* của bạn như sau: `"inspector": "npx @modelcontextprotocol/inspector node build/index.js"` rồi chạy `npm run inspector`

#### Python

Python bao bọc một công cụ Node.js gọi là inspector. Có thể gọi công cụ đó như sau:

```sh
mcp dev server.py
```

Tuy nhiên, nó không triển khai tất cả các phương thức có trên công cụ nên bạn được khuyến nghị chạy công cụ Node.js trực tiếp như dưới đây:

```sh
npx @modelcontextprotocol/inspector mcp run server.py
```

Nếu bạn đang sử dụng công cụ hoặc IDE cho phép cấu hình lệnh và tham số để chạy script, 
đảm bảo đặt `python` trong trường `Command` và `server.py` làm `Arguments`. Điều này đảm bảo script chạy đúng.

#### .NET

Đảm bảo bạn đang ở trong thư mục dự án của mình:

```sh
cd McpCalculatorServer
npx @modelcontextprotocol/inspector dotnet run
```

#### Java

Đảm bảo máy chủ calculator của bạn đang chạy
Sau đó chạy trình kiểm tra:

```cmd
npx @modelcontextprotocol/inspector
```

Trong giao diện web của trình kiểm tra:

1. Chọn "SSE" làm loại giao thức truyền tải
2. Đặt URL thành: `http://localhost:8080/sse`
3. Nhấn "Connect"

![Connect](../../../../translated_images/tool.163d33e3ee307e209ef146d8f85060d2f7e83e9f59b3b1699a77204ae0454ad2.vi.png)

**Bạn đã kết nối với máy chủ**
**Phần kiểm tra máy chủ Java đã hoàn thành**

Phần tiếp theo là về tương tác với máy chủ.

Bạn sẽ thấy giao diện người dùng sau:

![Connect](../../../../translated_images/connect.141db0b2bd05f096fb1dd91273771fd8b2469d6507656c3b0c9df4b3c5473929.vi.png)

1. Kết nối với máy chủ bằng cách chọn nút Connect
  Khi bạn kết nối với máy chủ, bạn sẽ thấy như sau:

  ![Connected](../../../../translated_images/connected.73d1e042c24075d386cacdd4ee7cd748c16364c277d814e646ff2f7b5eefde85.vi.png)

1. Chọn "Tools" và "listTools", bạn sẽ thấy "Add" xuất hiện, chọn "Add" và điền các giá trị tham số.

  Bạn sẽ thấy phản hồi sau, tức là kết quả từ công cụ "add":

  ![Result of running add](../../../../translated_images/ran-tool.a5a6ee878c1369ec1e379b81053395252a441799dbf23416c36ddf288faf8249.vi.png)

Chúc mừng, bạn đã tạo và chạy thành công máy chủ đầu tiên của mình!

#### Rust

Để chạy máy chủ Rust với MCP Inspector CLI, sử dụng lệnh sau:

```sh
npx @modelcontextprotocol/inspector cargo run --cli --method tools/call --tool-name add --tool-arg a=1 b=2
```

### SDK chính thức

MCP cung cấp các SDK chính thức cho nhiều ngôn ngữ:

- [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk) - Được duy trì phối hợp với Microsoft
- [Java SDK](https://github.com/modelcontextprotocol/java-sdk) - Được duy trì phối hợp với Spring AI
- [TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk) - Triển khai TypeScript chính thức
- [Python SDK](https://github.com/modelcontextprotocol/python-sdk) - Triển khai Python chính thức
- [Kotlin SDK](https://github.com/modelcontextprotocol/kotlin-sdk) - Triển khai Kotlin chính thức
- [Swift SDK](https://github.com/modelcontextprotocol/swift-sdk) - Được duy trì phối hợp với Loopwork AI
- [Rust SDK](https://github.com/modelcontextprotocol/rust-sdk) - Triển khai Rust chính thức

## Những điểm chính cần nhớ

- Thiết lập môi trường phát triển MCP rất đơn giản với các SDK theo ngôn ngữ
- Xây dựng máy chủ MCP bao gồm tạo và đăng ký các công cụ với các schema rõ ràng
- Kiểm tra và gỡ lỗi là cần thiết để có các triển khai MCP đáng tin cậy

## Mẫu

- [Java Calculator](../samples/java/calculator/README.md)
- [.Net Calculator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Calculator](../samples/javascript/README.md)
- [TypeScript Calculator](../samples/typescript/README.md)
- [Python Calculator](../../../../03-GettingStarted/samples/python)
- [Rust Calculator](../../../../03-GettingStarted/samples/rust)

## Bài tập

Tạo một máy chủ MCP đơn giản với một công cụ bạn chọn:

1. Triển khai công cụ bằng ngôn ngữ bạn thích (.NET, Java, Python, TypeScript hoặc Rust).
2. Định nghĩa các tham số đầu vào và giá trị trả về.
3. Chạy công cụ kiểm tra để đảm bảo máy chủ hoạt động như mong muốn.
4. Kiểm tra triển khai với các đầu vào khác nhau.

## Giải pháp

[Solution](./solution/README.md)

## Tài nguyên bổ sung

- [Xây dựng Agents sử dụng Model Context Protocol trên Azure](https://learn.microsoft.com/azure/developer/ai/intro-agents-mcp)
- [MCP từ xa với Azure Container Apps (Node.js/TypeScript/JavaScript)](https://learn.microsoft.com/samples/azure-samples/mcp-container-ts/mcp-container-ts/)
- [Agent MCP OpenAI .NET](https://learn.microsoft.com/samples/azure-samples/openai-mcp-agent-dotnet/openai-mcp-agent-dotnet/)

## Tiếp theo

Tiếp theo: [Bắt đầu với MCP Clients](../02-client/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Tuyên bố từ chối trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ gốc của nó nên được coi là nguồn chính xác và đáng tin cậy. Đối với thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp do con người thực hiện. Chúng tôi không chịu trách nhiệm về bất kỳ sự hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->