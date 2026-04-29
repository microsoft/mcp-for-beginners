# 開始使用 MCP

歡迎踏出使用 Model Context Protocol (MCP) 的第一步！無論你是 MCP 新手或希望加深理解，本指南將帶你了解基本設置和開發流程。你將發現 MCP 如何實現 AI 模型與應用程式之間的無縫整合，並學習如何快速準備環境來構建和測試基於 MCP 的解決方案。

> 重點摘要；如果你開發 AI 應用，你會知道可以為 LLM（大型語言模型）添加工具和其他資源，令 LLM 更加博學。然而，如果你把這些工具和資源放在伺服器上，應用和伺服器能力便可被任何有或無 LLM 的用戶端使用。

## 概述

本課程提供設置 MCP 環境與構建首個 MCP 應用的實務指導。你將學習如何安裝必要工具和框架、構建基本 MCP 伺服器、創建主機應用程式，以及測試你的實作。

Model Context Protocol (MCP) 是一個開放式協議，標準化應用程式如何向 LLM 提供上下文。你可以將 MCP 看作 AI 應用的 USB-C 接口——它為 AI 模型連接不同資料來源和工具提供統一標準。

## 學習目標

完成本課程後，你將能夠：

- 為 C#、Java、Python、TypeScript 和 Rust 設置 MCP 開發環境
- 建構和部署具備自訂功能（資源、提示和工具）的基本 MCP 伺服器
- 創建可連接 MCP 伺服器的主機應用程式
- 測試與除錯 MCP 實作

## 設置你的 MCP 環境

開始使用 MCP 之前，準備開發環境並理解基本工作流程非常重要。本節將引導你完成初始設置步驟，確保使用 MCP 能順利起步。

### 先決條件

開始 MCP 開發前，請確認你已具備：

- <strong>開發環境</strong>：選擇的語言環境 (C#、Java、Python、TypeScript 或 Rust)
- **IDE/編輯器**：Visual Studio、Visual Studio Code、IntelliJ、Eclipse、PyCharm 或任何現代程式碼編輯器
- <strong>套件管理器</strong>：NuGet、Maven/Gradle、pip、npm/yarn 或 Cargo
- **API 密鑰**：若你的主機應用使用任何 AI 服務，需準備好密鑰

## 基本 MCP 伺服器結構

一個 MCP 伺服器通常包含：

- <strong>伺服器設定</strong>：設定連接埠、認證及其他選項
- <strong>資源</strong>：提供給 LLM 的資料和上下文
- <strong>工具</strong>：模型可調用的功能
- <strong>提示</strong>：用於生成或結構化文字的範本

以下是用 TypeScript 的簡化範例：

```typescript
import { McpServer, ResourceTemplate } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";

// 建立一個 MCP 伺服器
const server = new McpServer({
  name: "Demo",
  version: "1.0.0"
});

// 新增一個加法工具
server.tool("add",
  { a: z.number(), b: z.number() },
  async ({ a, b }) => ({
    content: [{ type: "text", text: String(a + b) }]
  })
);

// 新增一個動態問候資源
server.resource(
  "file",
  // 'list' 參數控制資源如何列出可用的檔案。設為 undefined 則會關閉此資源的列出功能。
  new ResourceTemplate("file://{path}", { list: undefined }),
  async (uri, { path }) => ({
    contents: [{
      uri: uri.href,
      text: `File, ${path}!`
    }]
  })
);

// 新增一個讀取檔案內容的檔案資源
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

// 開始從標準輸入接收訊息及從標準輸出發送訊息
const transport = new StdioServerTransport();
await server.connect(transport);
```

在前述程式碼中，我們：

- 從 MCP TypeScript SDK 匯入必要類別。
- 建立並配置 MCP 伺服器實例。
- 註冊自訂工具（`calculator`），並附上處理函式。
- 啟動伺服器開始監聽 MCP 請求。

## 測試與除錯

開始測試你的 MCP 伺服器前，了解可用工具和除錯最佳實務很重要。有效測試能確保伺服器按預期運作，並快速辨識和解決問題。以下部分列出建議的方法來驗證 MCP 實作。

MCP 提供多種工具幫助你測試和除錯伺服器：

- **Inspector 工具**：此圖形介面允許你連接伺服器，測試工具、提示和資源。
- **curl**：你也可使用 curl 等命令行工具或其他可發送 HTTP 請求的用戶端連接伺服器。

### 使用 MCP Inspector

[MCP Inspector](https://github.com/modelcontextprotocol/inspector) 是視覺化測試工具，協助你：

1. <strong>發現伺服器能力</strong>：自動偵測可用的資源、工具和提示
2. <strong>測試工具執行</strong>：嘗試不同參數並即時查看回應
3. <strong>檢視伺服器元資料</strong>：查看伺服器資訊、結構化定義和設定

```bash
# 例如 TypeScript，安裝及運行 MCP Inspector
npx @modelcontextprotocol/inspector node build/index.js
```

執行以上命令後，MCP Inspector 將啟動瀏覽器中的本地網頁介面。你會看到儀表板顯示你註冊的 MCP 伺服器、可用工具、資源與提示。介面讓你能互動式測試工具執行、檢視伺服器元資料和即時回應，便於驗證與除錯 MCP 伺服器實作。

以下是介面截圖示例：

![MCP Inspector server connection](../../../../translated_images/zh-HK/connected.73d1e042c24075d3.webp)

## 常見設置問題與解決方案

| 問題 | 可能解決方案 |
|-------|-------------------|
| 連線被拒絕 | 檢查伺服器是否啟動及連接埠正確 |
| 工具執行錯誤 | 檢視參數驗證和錯誤處理 |
| 認證失敗 | 核實 API 金鑰與權限 |
| 結構驗證錯誤 | 確保參數符合定義的結構 |
| 伺服器無法啟動 | 檢查連接埠衝突或缺少相依 |
| CORS 錯誤 | 設定適當跨域請求標頭 |
| 認證問題 | 驗證令牌有效性與授權 |

## 本地開發

本地開發及測試時，可直接在你的機器上運行 MCP 伺服器：

1. <strong>啟動伺服器程序</strong>：執行你的 MCP 伺服器應用
2. <strong>配置網路</strong>：確定伺服器可在預期連接埠存取
3. <strong>連接用戶端</strong>：使用本地連接 URL，如 `http://localhost:3000`

```bash
# 範例：本地運行 TypeScript MCP 服務器
npm run start
# 服務器運行於 http://localhost:3000
```

## 建立你的第一個 MCP 伺服器

我們已在之前課程中涵蓋了[核心概念](../../01-CoreConcepts/README.md)，現在是時候將知識付諸實踐。

### 伺服器能做什麼

開始撰寫程式碼前，先回顧伺服器的功能範圍：

MCP 伺服器可用於：

- 存取本地文件和資料庫
- 連接遠端 API
- 執行計算
- 整合其他工具和服務
- 提供用戶操作介面

很好，既然知道它能做什麼，我們開始編碼。

## 練習：建立伺服器

建立伺服器需要以下步驟：

- 安裝 MCP SDK。
- 創建專案並設置專案結構。
- 撰寫伺服器程式碼。
- 測試伺服器。

### -1- 創建專案

#### TypeScript

```sh
# 建立專案目錄並初始化 npm 專案
mkdir calculator-server
cd calculator-server
npm init -y
```

#### Python

```sh
# 建立專案目錄
mkdir calculator-server
cd calculator-server
# 在 Visual Studio Code 開啟資料夾 - 如果你使用其他 IDE 可跳過此步驟
code .
```

#### .NET

```sh
dotnet new console -n McpCalculatorServer
cd McpCalculatorServer
```

#### Java

Java 請建立 Spring Boot 專案：

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

解壓縮 zip 檔：

```bash
unzip calculator-server.zip -d calculator-server
cd calculator-server
# 可選擇移除未使用的測試
rm -rf src/test/java
```

將以下完整設定加入 *pom.xml* 文件：

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

### -2- 新增相依套件

你已建立專案，接著新增所需依賴：

#### TypeScript

```sh
# 如果尚未安裝，請全局安裝 TypeScript
npm install typescript -g

# 安裝 MCP SDK 和 Zod 用於結構驗證
npm install @modelcontextprotocol/sdk zod
npm install -D @types/node typescript
```

#### Python

```sh
# 建立虛擬環境並安裝依賴項
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

### -3- 創建專案檔案

#### TypeScript

打開 *package.json*，用以下內容替換，確保能編譯並執行伺服器：

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

創建 *tsconfig.json*，內容如下：

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

創建源代碼資料夾：

```sh
mkdir src
touch src/index.ts
```

#### Python

創建檔案 *server.py*

```sh
touch server.py
```

#### .NET

安裝必要 NuGet 套件：

```sh
dotnet add package ModelContextProtocol --prerelease
dotnet add package Microsoft.Extensions.Hosting
```

#### Java

Java Spring Boot 專案結構會自動建立。

#### Rust

Rust 在執行 `cargo init` 時會自動建立 *src/main.rs*，打開檔案並刪除預設程式碼。

### -4- 撰寫伺服器程式碼

#### TypeScript

創建檔案 *index.ts* 並加入以下程式碼：

```typescript
import { McpServer, ResourceTemplate } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";
 
// 建立一個MCP伺服器
const server = new McpServer({
  name: "Calculator MCP Server",
  version: "1.0.0"
});
```

你已擁有伺服器，但功能有限，讓我們來完善。

#### Python

```python
# server.py
from mcp.server.fastmcp import FastMCP

# 建立一個 MCP 伺服器
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

Java 端，創建核心伺服器元件。首先，修改主應用程式類別：

*src/main/java/com/microsoft/mcp/sample/server/McpServerApplication.java*：

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

創建計算服務類別 *src/main/java/com/microsoft/mcp/sample/server/service/CalculatorService.java*：

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

**生產用元件(可選)：**

建立啟動配置 *src/main/java/com/microsoft/mcp/sample/server/config/StartupConfig.java*：

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

建立健康檢查控制器 *src/main/java/com/microsoft/mcp/sample/server/controller/HealthController.java*：

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

建立例外處理器 *src/main/java/com/microsoft/mcp/sample/server/exception/GlobalExceptionHandler.java*：

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

        // 取值函數
        public String getCode() { return code; }
        public String getMessage() { return message; }
    }
}
```

建立自訂啟動橫幅 *src/main/resources/banner.txt*：

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

將以下程式碼加入 *src/main.rs* 頂端，引入所需函式庫和模組。

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

此計算器伺服器將可執行兩數相加。先建立一個結構體表示計算請求。

```rust
#[derive(Debug, serde::Deserialize, schemars::JsonSchema)]
pub struct CalculatorRequest {
    pub a: f64,
    pub b: f64,
}
```

接著建立代表計算器伺服器的結構體，內含工具路由器，用於註冊工具。

```rust
#[derive(Debug, Clone)]
pub struct Calculator {
    tool_router: ToolRouter<Self>,
}
```

現在實作 `Calculator` 結構體以建立伺服器新實例及實現伺服器處理程序以提供伺服器訊息。

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

最後實作主函數啟動伺服器，此函數會創建 `Calculator` 實例並透過標準輸入/輸出提供服務。

```rust
#[tokio::main]
async fn main() -> Result<(), Box<dyn Error>> {
    let service = Calculator::new().serve(stdio()).await?;
    service.waiting().await?;
    Ok(())
}
```

伺服器已設置基礎資訊提供，下一步加入執行加法的工具。

### -5- 新增工具與資源

新增工具和資源，程式碼如下：

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

你的工具接受參數 `a` 和 `b`，執行一函數並產生如下形式的回應：

```typescript
{
  contents: [{
    type: "text", content: "some content"
  }]
}
```

你的資源以字串 "greeting" 方式存取，接受參數 `name`，並產生類似工具的回應：

```typescript
{
  uri: "<href>",
  text: "a text"
}
```

#### Python

```python
# 新增一個加法工具
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


# 新增一個動態問候資源
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}!"
```

程式碼中我們：

- 定義工具 `add`，參數為整數型態之 `a` 與 `b`。
- 建立資源 `greeting`，接受 `name` 作為參數。

#### .NET

將此程式碼加入 Program.cs：

```csharp
[McpServerToolType]
public static class CalculatorTool
{
    [McpServerTool, Description("Adds two numbers")]
    public static string Add(int a, int b) => $"Sum {a + b}";
}
```

#### Java

工具在前步驟已建立。

#### Rust

在 `impl Calculator` 區塊中新增工具：

```rust
#[tool(description = "Adds a and b")]
async fn add(
    &self,
    Parameters(CalculatorRequest { a, b }): Parameters<CalculatorRequest>,
) -> String {
    (a + b).to_string()
}
```

### -6- 完整程式碼

讓我們加入啟動伺服器所需的最後程式：

#### TypeScript

```typescript
// 開始從標準輸入接收訊息並於標準輸出發送訊息
const transport = new StdioServerTransport();
await server.connect(transport);
```

完整程式碼如下：

```typescript
// index.ts
import { McpServer, ResourceTemplate } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";

// 建立一個 MCP 伺服器
const server = new McpServer({
  name: "Calculator MCP Server",
  version: "1.0.0"
});

// 新增一個加法工具
server.tool(
  "add",
  { a: z.number(), b: z.number() },
  async ({ a, b }) => ({
    content: [{ type: "text", text: String(a + b) }]
  })
);

// 新增一個動態問候語資源
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

// 開始接收 stdin 的訊息並於 stdout 傳送訊息
const transport = new StdioServerTransport();
server.connect(transport);
```

#### Python

```python
# server.py
from mcp.server.fastmcp import FastMCP

# 建立一個MCP伺服器
mcp = FastMCP("Demo")


# 新增一個加法工具
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


# 新增動態打招呼的資源
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}!"

# 主執行區塊 - 運行伺服器所必需
if __name__ == "__main__":
    mcp.run()
```

#### .NET

建立 Program.cs，內容如下：

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

你的完整主應用程式類別應如下：

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

Rust 伺服器最終程式碼如下：

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

### -7- 測試伺服器

啟動伺服器執行以下命令：

#### TypeScript

```sh
npm run build
```

#### Python

```sh
mcp run server.py
```

> 使用 MCP Inspector 時，建議執行 `mcp dev server.py`，此命令會自動啟動 Inspector 且提供所需代理會話令牌。若使用 `mcp run server.py`，則需手動啟動 Inspector 並配置連接。

#### .NET

確保在專案目錄執行：

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

執行以下命令格式化並啟動伺服器：

```sh
cargo fmt
cargo run
```

### -8- 使用 Inspector 執行

Inspector 是一款極佳工具，可啟動伺服器並讓你互動測試其功能。讓我們啟動它：

> [!NOTE]
> 「命令」欄位顯示的內容可能因特定執行環境而異。

#### TypeScript

```sh
npx @modelcontextprotocol/inspector node build/index.js
```

或者加入 *package.json*，如下設定：`"inspector": "npx @modelcontextprotocol/inspector node build/index.js"`，然後執行 `npm run inspector`

#### Python

Python 包裝了一個 Node.js 工具 inspector，可透過以下方式呼叫：

```sh
mcp dev server.py
```

但它未實作該工具的所有方法，建議直接執行 Node.js 版工具，如下：

```sh
npx @modelcontextprotocol/inspector mcp run server.py
```

如果你使用的工具或 IDE 允許設定執行腳本的命令與參數，
確保在 `Command` 欄位設定 `python`，並將 `server.py` 設為 `Arguments`。這樣能確保腳本正確執行。

#### .NET

確保你已經位於你的專案目錄：

```sh
cd McpCalculatorServer
npx @modelcontextprotocol/inspector dotnet run
```

#### Java

確保你的計算器伺服器已經運行
接著執行檢查器：

```cmd
npx @modelcontextprotocol/inspector
```

在檢查器的網頁介面：

1. 選擇「SSE」作為傳輸類型
2. 將 URL 設為：`http://localhost:8080/sse`
3. 點擊「Connect」

![Connect](../../../../translated_images/zh-HK/tool.163d33e3ee307e20.webp)

<strong>你已成功連接到伺服器</strong>
**Java 伺服器測試部分已完成**

下一部分將介紹如何與伺服器互動。

你應該會看到以下用戶介面：

![Connect](../../../../translated_images/zh-HK/connect.141db0b2bd05f096.webp)

1. 按下 Connect 按鈕連接伺服器
  成功連接後，你應該會看到以下畫面：

  ![Connected](../../../../translated_images/zh-HK/connected.73d1e042c24075d3.webp)

1. 選擇「Tools」裡的「listTools」，你應該會看到「Add」出現，選擇「Add」並填寫參數值。

  你會看到以下回應，即是「add」工具的結果：

  ![Result of running add](../../../../translated_images/zh-HK/ran-tool.a5a6ee878c1369ec.webp)

恭喜，你已成功建立並運行你的第一個伺服器！

#### Rust

使用 MCP Inspector CLI 執行 Rust 伺服器，請使用以下指令：

```sh
npx @modelcontextprotocol/inspector cargo run --cli --method tools/call --tool-name add --tool-arg a=1 b=2
```

### 官方 SDK

MCP 提供多語言的官方 SDK：

- [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk) - 與 Microsoft 共同維護
- [Java SDK](https://github.com/modelcontextprotocol/java-sdk) - 與 Spring AI 共同維護
- [TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk) - 官方 TypeScript 實作
- [Python SDK](https://github.com/modelcontextprotocol/python-sdk) - 官方 Python 實作
- [Kotlin SDK](https://github.com/modelcontextprotocol/kotlin-sdk) - 官方 Kotlin 實作
- [Swift SDK](https://github.com/modelcontextprotocol/swift-sdk) - 與 Loopwork AI 共同維護
- [Rust SDK](https://github.com/modelcontextprotocol/rust-sdk) - 官方 Rust 實作

## 重要重點

- 透過語言特定的 SDK，設定 MCP 開發環境非常簡單
- 建立 MCP 伺服器包括建立並註冊具有明確結構的工具
- 測試與除錯對於可靠的 MCP 實作非常重要

## 範例

- [Java Calculator](../samples/java/calculator/README.md)
- [.Net Calculator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Calculator](../samples/javascript/README.md)
- [TypeScript Calculator](../samples/typescript/README.md)
- [Python Calculator](../../../../03-GettingStarted/samples/python)
- [Rust Calculator](../../../../03-GettingStarted/samples/rust)

## 作業

建立一個簡單的 MCP 伺服器，包含你選擇的工具：

1. 使用你偏好的語言實作該工具（.NET、Java、Python、TypeScript 或 Rust）
2. 定義輸入參數與回傳值
3. 運行檢查器工具，確保伺服器正常運作
4. 使用各種輸入測試實作結果

## 解答

[解答](./solution/README.md)

## 其他資源

- [在 Azure 上使用 Model Context Protocol 建置 Agents](https://learn.microsoft.com/azure/developer/ai/intro-agents-mcp)
- [使用 Azure Container Apps 遠端 MCP（Node.js/TypeScript/JavaScript）](https://learn.microsoft.com/samples/azure-samples/mcp-container-ts/mcp-container-ts/)
- [.NET OpenAI MCP Agent](https://learn.microsoft.com/samples/azure-samples/openai-mcp-agent-dotnet/openai-mcp-agent-dotnet/)

## 下一步

下一章：[MCP 用戶端入門](../02-client/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：  
本文件已使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們力求準確，但請注意自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議使用專業人工翻譯。我們不對因使用本翻譯而引起的任何誤解或誤譯承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->