# MCP 시작하기

Model Context Protocol (MCP)와 함께하는 첫 걸음에 오신 것을 환영합니다! MCP가 처음이든 이해도를 높이고자 하든, 이 가이드는 필수 설정 및 개발 과정을 안내합니다. MCP가 AI 모델과 애플리케이션 간의 원활한 통합을 어떻게 가능하게 하는지 살펴보고, MCP 기반 솔루션 구축 및 테스트를 위한 환경을 빠르게 준비하는 방법을 배우게 됩니다.

> TLDR; AI 애플리케이션을 개발한다면 LLM(대형 언어 모델)에 도구와 기타 리소스를 추가하여 LLM을 더 똑똑하게 만들 수 있다는 것을 아실 겁니다. 하지만 도구와 리소스를 서버에 배치하면 앱과 서버 기능은 LLM이 있든 없든 모든 클라이언트가 사용할 수 있습니다.

## 개요

이 수업은 MCP 환경 설정과 첫 MCP 애플리케이션 구축에 관한 실용적인 안내를 제공합니다. 필요한 도구 및 프레임워크 설정, 기본 MCP 서버 구축, 호스트 애플리케이션 생성, 구현 테스트 방법을 배우게 됩니다.

Model Context Protocol (MCP)은 애플리케이션이 LLM에 컨텍스트를 제공하는 방식을 표준화하는 오픈 프로토콜입니다. MCP는 AI 애플리케이션을 위한 USB-C 포트와 같아서 AI 모델을 다양한 데이터 소스 및 도구와 연결하는 표준화된 방법을 제공합니다.

## 학습 목표

이 수업을 마치면 다음을 수행할 수 있습니다:

- C#, Java, Python, TypeScript, Rust에서 MCP 개발 환경 설정
- 맞춤 기능(리소스, 프롬프트, 도구)을 갖춘 기본 MCP 서버 구축 및 배포
- MCP 서버에 연결하는 호스트 애플리케이션 생성
- MCP 구현 테스트 및 디버깅

## MCP 환경 설정하기

MCP 작업을 시작하기 전에 개발 환경을 준비하고 기본 작업 흐름을 이해하는 것이 중요합니다. 이 섹션은 MCP 시작을 원활하게 하기 위한 초기 설정 단계를 안내합니다.

### 사전 준비 사항

MCP 개발에 착수하기 전에 다음이 준비되었는지 확인하세요:

- **개발 환경**: 선택한 언어(C#, Java, Python, TypeScript, Rust)용
- **IDE/편집기**: Visual Studio, Visual Studio Code, IntelliJ, Eclipse, PyCharm, 또는 최신 코드 편집기
- **패키지 관리자**: NuGet, Maven/Gradle, pip, npm/yarn, Cargo
- **API 키**: 호스트 애플리케이션에서 사용할 AI 서비스용

## 기본 MCP 서버 구조

MCP 서버는 일반적으로 다음을 포함합니다:

- **서버 구성**: 포트, 인증 및 기타 설정
- <strong>리소스</strong>: LLM에 제공할 데이터 및 컨텍스트
- <strong>도구</strong>: 모델이 호출할 수 있는 기능
- <strong>프롬프트</strong>: 텍스트 생성 또는 구조화 템플릿

아래는 TypeScript 예제입니다:

```typescript
import { McpServer, ResourceTemplate } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";

// MCP 서버를 생성합니다
const server = new McpServer({
  name: "Demo",
  version: "1.0.0"
});

// 추가 도구를 추가합니다
server.tool("add",
  { a: z.number(), b: z.number() },
  async ({ a, b }) => ({
    content: [{ type: "text", text: String(a + b) }]
  })
);

// 동적 인사말 리소스를 추가합니다
server.resource(
  "file",
  // 'list' 매개변수는 리소스가 사용 가능한 파일을 나열하는 방식을 제어합니다. undefined로 설정하면 이 리소스의 목록 표시가 비활성화됩니다.
  new ResourceTemplate("file://{path}", { list: undefined }),
  async (uri, { path }) => ({
    contents: [{
      uri: uri.href,
      text: `File, ${path}!`
    }]
  })
);

// 파일 내용을 읽는 파일 리소스를 추가합니다
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

// stdin에서 메시지를 받고 stdout으로 메시지를 전송하기 시작합니다
const transport = new StdioServerTransport();
await server.connect(transport);
```

위 코드에서 우리는:

- MCP TypeScript SDK에서 필요한 클래스를 가져왔습니다.
- 새 MCP 서버 인스턴스를 생성 및 구성했습니다.
- 핸들러 함수가 있는 사용자 지정 도구(`calculator`)를 등록했습니다.
- MCP 요청을 수신하도록 서버를 시작했습니다.

## 테스트 및 디버깅

MCP 서버를 테스트하기 전에 이용 가능한 도구 및 디버깅 모범 사례를 이해하는 것이 중요합니다. 효과적인 테스트는 서버가 예상대로 작동하는지 확인하고 문제를 신속히 파악 및 해결하는 데 도움이 됩니다. 다음 섹션에서 MCP 구현을 검증하기 위한 권장 방법을 설명합니다.

MCP는 서버 테스트 및 디버깅을 도와주는 도구를 제공합니다:

- **Inspector 도구**: 이 그래픽 인터페이스는 서버에 연결하여 도구, 프롬프트, 리소스를 테스트할 수 있습니다.
- **curl**: 커맨드 라인 도구인 curl이나 다른 HTTP 명령을 생성 및 실행할 수 있는 클라이언트로도 서버에 연결할 수 있습니다.

### MCP Inspector 사용하기

[MCP Inspector](https://github.com/modelcontextprotocol/inspector)는 다음을 지원하는 시각적 테스트 도구입니다:

1. **서버 기능 탐색**: 사용 가능한 리소스, 도구, 프롬프트 자동 감지
2. **도구 실행 테스트**: 다양한 매개변수로 실시간 응답 확인
3. **서버 메타데이터 조회**: 서버 정보, 스키마, 구성 검토

```bash
# 예제 TypeScript, MCP Inspector 설치 및 실행
npx @modelcontextprotocol/inspector node build/index.js
```

위 명령어를 실행하면 MCP Inspector가 브라우저에서 로컬 웹 인터페이스를 실행합니다. 등록된 MCP 서버, 사용 가능한 도구, 리소스 및 프롬프트 대시보드를 볼 수 있습니다. 이 인터페이스로 도구 실행 테스트, 서버 메타데이터 조사, 실시간 응답 확인 등이 가능해 MCP 서버 구현 검증 및 디버깅이 수월해집니다.

다음은 화면 예시입니다:

![MCP Inspector server connection](../../../../translated_images/ko/connected.73d1e042c24075d3.webp)

## 일반적인 설정 문제 및 해결책

| 문제                    | 가능한 해결책                                |
|-------------------------|--------------------------------------------|
| 연결 거부됨             | 서버 실행 여부 및 포트 확인                 |
| 도구 실행 오류          | 매개변수 검증 및 오류 처리 검토            |
| 인증 실패               | API 키 및 권한 확인                         |
| 스키마 검증 오류        | 매개변수가 정의된 스키마와 일치하는지 확인|
| 서버가 시작되지 않음    | 포트 충돌 또는 누락된 종속성 점검          |
| CORS 오류               | 교차 출처 요청에 적절한 CORS 헤더 구성     |
| 인증 문제               | 토큰 유효성 및 권한 확인                    |

## 로컬 개발

로컬 개발 및 테스트용으로, MCP 서버를 자신의 머신에서 직접 실행할 수 있습니다:

1. **서버 프로세스 시작**: MCP 서버 애플리케이션 실행
2. **네트워킹 구성**: 서버가 예상 포트에서 접근 가능하게 설정
3. **클라이언트 연결**: `http://localhost:3000` 같은 로컬 연결 URL 사용

```bash
# 예시: TypeScript MCP 서버를 로컬에서 실행하기
npm run start
# 서버가 http://localhost:3000 에서 실행 중입니다
```

## 첫 번째 MCP 서버 구축하기

이전 수업에서 [핵심 개념](../../01-CoreConcepts/README.md)을 다뤘으니 이제 그 지식을 실습해 보겠습니다.

### 서버가 할 수 있는 일

코딩을 시작하기 전에 서버의 역할을 상기해 봅시다:

MCP 서버는 예를 들어:

- 로컬 파일 및 데이터베이스 접근
- 원격 API 연결
- 계산 수행
- 다른 도구 및 서비스 통합
- 상호작용을 위한 사용자 인터페이스 제공

좋습니다, 무엇을 할 수 있는지 알았으니 코딩을 시작해 봅시다.

## 연습: 서버 만들기

서버를 만들려면 다음 단계를 따르세요:

- MCP SDK 설치
- 프로젝트 생성 및 구조 설정
- 서버 코드 작성
- 서버 테스트

### -1- 프로젝트 생성하기

#### TypeScript

```sh
# 프로젝트 디렉토리를 생성하고 npm 프로젝트를 초기화하십시오
mkdir calculator-server
cd calculator-server
npm init -y
```

#### Python

```sh
# 프로젝트 디렉토리 생성
mkdir calculator-server
cd calculator-server
# Visual Studio Code에서 폴더 열기 - 다른 IDE를 사용하는 경우 생략하세요
code .
```

#### .NET

```sh
dotnet new console -n McpCalculatorServer
cd McpCalculatorServer
```

#### Java

Java의 경우 Spring Boot 프로젝트를 만드세요:

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

압축 파일 풀기:

```bash
unzip calculator-server.zip -d calculator-server
cd calculator-server
# 선택적으로 사용하지 않는 테스트 제거
rm -rf src/test/java
```

*pom.xml* 파일에 다음과 같은 전체 구성을 추가하세요:

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

### -2- 의존성 추가하기

프로젝트를 생성했으니 다음은 의존성 추가입니다:

#### TypeScript

```sh
# 아직 설치하지 않은 경우 TypeScript를 전역에 설치하세요
npm install typescript -g

# MCP SDK와 스키마 검증을 위해 Zod를 설치하세요
npm install @modelcontextprotocol/sdk zod
npm install -D @types/node typescript
```

#### Python

```sh
# 가상 환경을 만들고 종속성을 설치합니다
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

### -3- 프로젝트 파일 생성하기

#### TypeScript

*package.json* 파일을 열어 다음 내용으로 교체해 서버 빌드 및 실행이 가능하게 합니다:

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

*tsconfig.json* 파일을 다음 내용으로 생성하세요:

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

소스 코드용 디렉터리를 생성합니다:

```sh
mkdir src
touch src/index.ts
```

#### Python

*server.py* 파일을 생성하세요

```sh
touch server.py
```

#### .NET

필요한 NuGet 패키지를 설치하세요:

```sh
dotnet add package ModelContextProtocol --prerelease
dotnet add package Microsoft.Extensions.Hosting
```

#### Java

Java Spring Boot 프로젝트는 프로젝트 구조가 자동으로 생성됩니다.

#### Rust

Rust는 `cargo init` 실행 시 기본적으로 *src/main.rs* 파일이 생성됩니다. 해당 파일을 열고 기본 코드를 삭제하세요.

### -4- 서버 코드 작성하기

#### TypeScript

*index.ts* 파일을 생성하고 다음 코드를 추가하세요:

```typescript
import { McpServer, ResourceTemplate } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";
 
// MCP 서버 생성
const server = new McpServer({
  name: "Calculator MCP Server",
  version: "1.0.0"
});
```

서버가 생성되었으나 할 일이 많지 않습니다. 고쳐 봅시다.

#### Python

```python
# server.py
from mcp.server.fastmcp import FastMCP

# MCP 서버 생성
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

Java는 핵심 서버 구성 요소를 생성합니다. 먼저 메인 애플리케이션 클래스를 수정하세요:

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

계산기 서비스 생성 *src/main/java/com/microsoft/mcp/sample/server/service/CalculatorService.java*:

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

**프로덕션 준비 서비스를 위한 선택적 구성 요소:**

시작 구성 생성 *src/main/java/com/microsoft/mcp/sample/server/config/StartupConfig.java*:

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

헬스 컨트롤러 생성 *src/main/java/com/microsoft/mcp/sample/server/controller/HealthController.java*:

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

예외 핸들러 생성 *src/main/java/com/microsoft/mcp/sample/server/exception/GlobalExceptionHandler.java*:

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

        // 게터
        public String getCode() { return code; }
        public String getMessage() { return message; }
    }
}
```

커스텀 배너 생성 *src/main/resources/banner.txt*:

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

*src/main.rs* 파일 상단에 다음 코드를 추가하세요. 이는 MCP 서버에 필요한 라이브러리와 모듈을 가져옵니다.

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

계산기 서버는 두 숫자를 더하는 간단한 서버가 될 것입니다. 계산기 요청을 나타내는 struct를 만들어 봅시다.

```rust
#[derive(Debug, serde::Deserialize, schemars::JsonSchema)]
pub struct CalculatorRequest {
    pub a: f64,
    pub b: f64,
}
```

다음으로 계산기 서버를 나타내는 struct를 만듭니다. 이 struct는 도구 라우터를 보유하며 도구 등록에 사용됩니다.

```rust
#[derive(Debug, Clone)]
pub struct Calculator {
    tool_router: ToolRouter<Self>,
}
```

이제 `Calculator` struct를 구현하여 서버 새 인스턴스를 생성하고 서버 정보를 제공하는 핸들러를 구현합니다.

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

마지막으로 서버를 시작하는 main 함수를 구현해야 합니다. 이 함수는 `Calculator` struct 인스턴스를 만들고 표준 입출력으로 서버를 운영합니다.

```rust
#[tokio::main]
async fn main() -> Result<(), Box<dyn Error>> {
    let service = Calculator::new().serve(stdio()).await?;
    service.waiting().await?;
    Ok(())
}
```

서버는 이제 자체에 관한 기본 정보를 제공합니다. 다음으로 덧셈을 수행하는 도구를 추가합니다.

### -5- 도구 및 리소스 추가

다음 코드로 도구와 리소스를 추가하세요:

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

도구는 `a` 및 `b` 매개변수를 받고, 다음 형식의 응답을 생성합니다:

```typescript
{
  contents: [{
    type: "text", content: "some content"
  }]
}
```

리소스는 문자열 "greeting"으로 접근하며, 이름(`name`) 매개변수를 받아 도구와 유사한 응답을 생성합니다:

```typescript
{
  uri: "<href>",
  text: "a text"
}
```

#### Python

```python
# 덧셈 도구 추가
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


# 동적 인사말 리소스 추가
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}!"
```

위 코드에서 우리는:

- `a`와 `b`라는 정수 매개변수를 받는 `add` 도구를 정의했습니다.
- `name` 매개변수를 받는 `greeting` 리소스를 만들었습니다.

#### .NET

Program.cs 파일에 다음을 추가하세요:

```csharp
[McpServerToolType]
public static class CalculatorTool
{
    [McpServerTool, Description("Adds two numbers")]
    public static string Add(int a, int b) => $"Sum {a + b}";
}
```

#### Java

도구는 이전 단계에서 이미 생성했습니다.

#### Rust

`impl Calculator` 블록 내에 새 도구를 추가하세요:

```rust
#[tool(description = "Adds a and b")]
async fn add(
    &self,
    Parameters(CalculatorRequest { a, b }): Parameters<CalculatorRequest>,
) -> String {
    (a + b).to_string()
}
```

### -6- 최종 코드

서버가 시작할 수 있도록 마지막 코드를 추가합시다:

#### TypeScript

```typescript
// stdin에서 메시지 수신을 시작하고 stdout에서 메시지 전송을 시작합니다
const transport = new StdioServerTransport();
await server.connect(transport);
```

전체 코드는 다음과 같습니다:

```typescript
// index.ts
import { McpServer, ResourceTemplate } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";

// MCP 서버 생성
const server = new McpServer({
  name: "Calculator MCP Server",
  version: "1.0.0"
});

// 추가 도구 추가
server.tool(
  "add",
  { a: z.number(), b: z.number() },
  async ({ a, b }) => ({
    content: [{ type: "text", text: String(a + b) }]
  })
);

// 동적 인사말 리소스 추가
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

// stdin에서 메시지 수신 시작 및 stdout으로 메시지 전송 시작
const transport = new StdioServerTransport();
server.connect(transport);
```

#### Python

```python
# server.py
from mcp.server.fastmcp import FastMCP

# MCP 서버 생성
mcp = FastMCP("Demo")


# 추가 도구 추가
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


# 동적 인사말 리소스 추가
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}!"

# 메인 실행 블록 - 서버를 실행하려면 필요합니다
if __name__ == "__main__":
    mcp.run()
```

#### .NET

다음 내용을 가진 Program.cs 파일을 생성하세요:

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

완성된 메인 애플리케이션 클래스는 다음과 같아야 합니다:

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

Rust 서버의 최종 코드는 다음과 같습니다:

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

### -7- 서버 테스트

다음 명령어로 서버를 시작하세요:

#### TypeScript

```sh
npm run build
```

#### Python

```sh
mcp run server.py
```

> MCP Inspector를 사용하려면 `mcp dev server.py`를 사용하세요. 이는 Inspector를 자동으로 실행하고 필요한 프록시 세션 토큰을 제공합니다. `mcp run server.py`를 사용할 경우 Inspector를 수동으로 시작하고 연결을 구성해야 합니다.

#### .NET

프로젝트 디렉터리 안에 있는지 확인하세요:

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

서버를 형식화하고 실행하려면 다음 명령어를 실행하세요:

```sh
cargo fmt
cargo run
```

### -8- Inspector를 사용해 실행하기

Inspector는 서버를 시작하고 상호작용할 수 있도록 도와주는 훌륭한 도구입니다. 시작해 봅시다:

> [!NOTE]
> "command" 필드의 내용은 특정 런타임으로 서버를 실행하는 명령어를 포함하므로 다르게 보일 수 있습니다.

#### TypeScript

```sh
npx @modelcontextprotocol/inspector node build/index.js
```

또는 <em>package.json</em>에 `"inspector": "npx @modelcontextprotocol/inspector node build/index.js"`를 추가하고 `npm run inspector`를 실행하세요.

#### Python

Python은 Node.js 도구인 inspector를 래핑합니다. 다음과 같이 해당 도구를 호출할 수 있습니다:

```sh
mcp dev server.py
```

하지만 전체 명령어를 구현하지 않으므로 Node.js 도구를 직접 실행하는 것이 권장됩니다:

```sh
npx @modelcontextprotocol/inspector mcp run server.py
```

스크립트 실행을 위한 명령과 인자를 구성할 수 있는 도구나 IDE를 사용하는 경우,
`Command` 필드에 `python`을 설정하고 `Arguments`에 `server.py`를 설정해야 합니다. 이렇게 해야 스크립트가 올바르게 실행됩니다.

#### .NET

프로젝트 디렉터리에 있는지 확인하세요:

```sh
cd McpCalculatorServer
npx @modelcontextprotocol/inspector dotnet run
```

#### Java

계산기 서버가 실행 중인지 확인하세요  
그런 다음 인스펙터를 실행합니다:

```cmd
npx @modelcontextprotocol/inspector
```

인스펙터 웹 인터페이스에서:

1. 전송 유형으로 "SSE"를 선택하세요
2. URL을 `http://localhost:8080/sse`로 설정하세요
3. "Connect"를 클릭하세요

![Connect](../../../../translated_images/ko/tool.163d33e3ee307e20.webp)

**이제 서버에 연결되었습니다**  
**Java 서버 테스트 섹션이 완료되었습니다**

다음 섹션은 서버와 상호작용하는 방법에 관한 내용입니다.

다음과 같은 사용자 인터페이스가 보일 것입니다:

![Connect](../../../../translated_images/ko/connect.141db0b2bd05f096.webp)

1. "Connect" 버튼을 선택하여 서버에 연결하세요  
  서버에 연결되면 다음 화면이 보입니다:

  ![Connected](../../../../translated_images/ko/connected.73d1e042c24075d3.webp)

1. "Tools"에서 "listTools"를 선택하세요. "Add"가 표시되면 "Add"를 선택하고 매개변수 값을 입력하세요.

  다음과 같은 응답, 즉 "add" 도구의 결과가 표시됩니다:

  ![Result of running add](../../../../translated_images/ko/ran-tool.a5a6ee878c1369ec.webp)

축하합니다, 첫 번째 서버를 성공적으로 만들고 실행했습니다!

#### Rust

MCP 인스펙터 CLI로 Rust 서버를 실행하려면 다음 명령어를 사용하세요:

```sh
npx @modelcontextprotocol/inspector cargo run --cli --method tools/call --tool-name add --tool-arg a=1 b=2
```

### 공식 SDK

MCP는 여러 언어에 대한 공식 SDK를 제공합니다:

- [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk) - Microsoft와 협력하여 유지 관리
- [Java SDK](https://github.com/modelcontextprotocol/java-sdk) - Spring AI와 협력하여 유지 관리
- [TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk) - 공식 TypeScript 구현
- [Python SDK](https://github.com/modelcontextprotocol/python-sdk) - 공식 Python 구현
- [Kotlin SDK](https://github.com/modelcontextprotocol/kotlin-sdk) - 공식 Kotlin 구현
- [Swift SDK](https://github.com/modelcontextprotocol/swift-sdk) - Loopwork AI와 협력하여 유지 관리
- [Rust SDK](https://github.com/modelcontextprotocol/rust-sdk) - 공식 Rust 구현

## 주요 요점

- 언어별 SDK를 통해 MCP 개발 환경을 간단히 구축할 수 있습니다
- MCP 서버 구축은 명확한 스키마를 가진 도구를 생성하고 등록하는 과정입니다
- 테스트 및 디버깅은 신뢰할 수 있는 MCP 구현에 필수적입니다

## 샘플

- [Java Calculator](../samples/java/calculator/README.md)
- [.Net Calculator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Calculator](../samples/javascript/README.md)
- [TypeScript Calculator](../samples/typescript/README.md)
- [Python Calculator](../../../../03-GettingStarted/samples/python)
- [Rust Calculator](../../../../03-GettingStarted/samples/rust)

## 과제

선택한 도구를 사용하여 간단한 MCP 서버를 만드세요:

1. 선호하는 언어(.NET, Java, Python, TypeScript, Rust)로 도구를 구현하세요.
2. 입력 매개변수와 반환 값을 정의하세요.
3. 인스펙터 도구를 실행하여 서버가 제대로 작동하는지 확인하세요.
4. 다양한 입력으로 구현을 테스트하세요.

## 솔루션

[Solution](./solution/README.md)

## 추가 리소스

- [Azure에서 Model Context Protocol을 사용하여 에이전트 빌드하기](https://learn.microsoft.com/azure/developer/ai/intro-agents-mcp)
- [원격 MCP with Azure Container Apps (Node.js/TypeScript/JavaScript)](https://learn.microsoft.com/samples/azure-samples/mcp-container-ts/mcp-container-ts/)
- [.NET OpenAI MCP 에이전트](https://learn.microsoft.com/samples/azure-samples/openai-mcp-agent-dotnet/openai-mcp-agent-dotnet/)

## 다음 단계

다음: [MCP 클라이언트 시작하기](../02-client/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 노력하고 있으나 자동 번역에는 오류나 부정확성이 포함될 수 있음을 유의해 주시기 바랍니다. 원본 문서가 원어로 된 공식 자료임을 참고하시기 바랍니다. 중요한 정보에 대해서는 전문 인간 번역가의 번역을 권장합니다. 본 번역 사용으로 인해 발생하는 모든 오해나 오역에 대해 당사는 책임을 지지 않습니다.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->