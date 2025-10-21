<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "726b74589522653d930c7395c9e1fab8",
  "translation_date": "2025-10-20T17:04:05+00:00",
  "source_file": "03-GettingStarted/01-first-server/README.md",
  "language_code": "tr"
}
-->
# MCP ile Başlarken

Model Context Protocol (MCP) ile ilk adımlarınıza hoş geldiniz! MCP'ye yeniyseniz veya bilginizi derinleştirmek istiyorsanız, bu rehber sizi temel kurulum ve geliştirme süreci boyunca yönlendirecek. MCP'nin yapay zeka modelleri ile uygulamalar arasında sorunsuz entegrasyonu nasıl sağladığını keşfedecek ve MCP destekli çözümler oluşturmak ve test etmek için ortamınızı hızlı bir şekilde nasıl hazırlayacağınızı öğreneceksiniz.

> Kısaca; Eğer yapay zeka uygulamaları geliştiriyorsanız, LLM'nize (büyük dil modeli) araçlar ve diğer kaynaklar ekleyerek LLM'nin daha bilgili olmasını sağlayabilirsiniz. Ancak bu araçları ve kaynakları bir sunucuya yerleştirirseniz, uygulama ve sunucu yetenekleri LLM olsun ya da olmasın herhangi bir istemci tarafından kullanılabilir.

## Genel Bakış

Bu ders, MCP ortamlarını kurma ve ilk MCP uygulamalarınızı oluşturma konusunda pratik rehberlik sağlar. Gerekli araçları ve çerçeveleri nasıl kuracağınızı, temel MCP sunucularını nasıl oluşturacağınızı, ana uygulamalar yaratmayı ve uygulamalarınızı test etmeyi öğreneceksiniz.

Model Context Protocol (MCP), uygulamaların LLM'lere bağlam sağlamasını standartlaştıran açık bir protokoldür. MCP'yi yapay zeka uygulamaları için bir USB-C portu gibi düşünebilirsiniz - yapay zeka modellerini farklı veri kaynaklarına ve araçlara bağlamak için standart bir yol sağlar.

## Öğrenme Hedefleri

Bu dersin sonunda şunları yapabileceksiniz:

- MCP için C#, Java, Python, TypeScript ve Rust dillerinde geliştirme ortamları kurmak
- Özel özelliklere (kaynaklar, istemler ve araçlar) sahip temel MCP sunucuları oluşturmak ve dağıtmak
- MCP sunucularına bağlanan ana uygulamalar oluşturmak
- MCP uygulamalarını test etmek ve hata ayıklamak

## MCP Ortamınızı Kurma

MCP ile çalışmaya başlamadan önce, geliştirme ortamınızı hazırlamak ve temel iş akışını anlamak önemlidir. Bu bölüm, MCP ile sorunsuz bir başlangıç için gerekli kurulum adımlarında size rehberlik edecektir.

### Ön Koşullar

MCP geliştirmeye başlamadan önce şunlara sahip olduğunuzdan emin olun:

- **Geliştirme Ortamı**: Seçtiğiniz dil için (C#, Java, Python, TypeScript veya Rust)
- **IDE/Düzenleyici**: Visual Studio, Visual Studio Code, IntelliJ, Eclipse, PyCharm veya herhangi bir modern kod düzenleyici
- **Paket Yöneticileri**: NuGet, Maven/Gradle, pip, npm/yarn veya Cargo
- **API Anahtarları**: Ana uygulamalarınızda kullanmayı planladığınız herhangi bir yapay zeka hizmeti için

## Temel MCP Sunucu Yapısı

Bir MCP sunucusu genellikle şunları içerir:

- **Sunucu Yapılandırması**: Port, kimlik doğrulama ve diğer ayarların kurulumu
- **Kaynaklar**: LLM'lere sunulan veri ve bağlam
- **Araçlar**: Modellerin çağırabileceği işlevsellik
- **İstemler**: Metin oluşturma veya yapılandırma şablonları

TypeScript'te basitleştirilmiş bir örnek:

```typescript
import { McpServer, ResourceTemplate } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";

// Create an MCP server
const server = new McpServer({
  name: "Demo",
  version: "1.0.0"
});

// Add an addition tool
server.tool("add",
  { a: z.number(), b: z.number() },
  async ({ a, b }) => ({
    content: [{ type: "text", text: String(a + b) }]
  })
);

// Add a dynamic greeting resource
server.resource(
  "file",
  // The 'list' parameter controls how the resource lists available files. Setting it to undefined disables listing for this resource.
  new ResourceTemplate("file://{path}", { list: undefined }),
  async (uri, { path }) => ({
    contents: [{
      uri: uri.href,
      text: `File, ${path}!`
    }]
  })
);

// Add a file resource that reads the file contents
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

// Start receiving messages on stdin and sending messages on stdout
const transport = new StdioServerTransport();
await server.connect(transport);
```

Yukarıdaki kodda şunları yaptık:

- MCP TypeScript SDK'sından gerekli sınıfları içe aktardık.
- Yeni bir MCP sunucu örneği oluşturup yapılandırdık.
- Bir işleyici işleviyle özel bir araç (`calculator`) kaydettik.
- Gelen MCP isteklerini dinlemek için sunucuyu başlattık.

## Test ve Hata Ayıklama

MCP sunucunuzu test etmeye başlamadan önce, mevcut araçları ve hata ayıklama için en iyi uygulamaları anlamak önemlidir. Etkili testler, sunucunuzun beklendiği gibi davranmasını sağlar ve sorunları hızlı bir şekilde tanımlayıp çözmenize yardımcı olur. Aşağıdaki bölüm, MCP uygulamanızı doğrulamak için önerilen yaklaşımları özetler.

MCP, sunucularınızı test etmenize ve hata ayıklamanıza yardımcı olacak araçlar sağlar:

- **Inspector aracı**, bu grafik arayüzü sunucunuza bağlanmanıza ve araçlarınızı, istemlerinizi ve kaynaklarınızı test etmenize olanak tanır.
- **curl**, ayrıca curl gibi bir komut satırı aracı veya HTTP komutları oluşturup çalıştırabilen diğer istemcilerle sunucunuza bağlanabilirsiniz.

### MCP Inspector Kullanımı

[MCP Inspector](https://github.com/modelcontextprotocol/inspector), görsel bir test aracıdır ve şu işlevleri yerine getirir:

1. **Sunucu Yeteneklerini Keşfetme**: Mevcut kaynakları, araçları ve istemleri otomatik olarak algılar
2. **Araç Çalıştırma Testi**: Farklı parametreleri deneyin ve yanıtları gerçek zamanlı olarak görün
3. **Sunucu Meta Verilerini Görüntüleme**: Sunucu bilgilerini, şemaları ve yapılandırmaları inceleyin

```bash
# ex TypeScript, installing and running MCP Inspector
npx @modelcontextprotocol/inspector node build/index.js
```

Yukarıdaki komutları çalıştırdığınızda, MCP Inspector tarayıcınızda yerel bir web arayüzü başlatacaktır. Kayıtlı MCP sunucularınızı, mevcut araçlarını, kaynaklarını ve istemlerini gösteren bir kontrol paneli görmeyi bekleyebilirsiniz. Arayüz, araç çalıştırmayı etkileşimli olarak test etmenize, sunucu meta verilerini incelemenize ve gerçek zamanlı yanıtları görüntülemenize olanak tanır, bu da MCP sunucu uygulamalarınızı doğrulamanızı ve hata ayıklamanızı kolaylaştırır.

İşte nasıl görünebileceğine dair bir ekran görüntüsü:

![MCP Inspector sunucu bağlantısı](../../../../translated_images/connected.73d1e042c24075d386cacdd4ee7cd748c16364c277d814e646ff2f7b5eefde85.tr.png)

## Yaygın Kurulum Sorunları ve Çözümleri

| Sorun | Olası Çözüm |
|-------|-------------|
| Bağlantı reddedildi | Sunucunun çalıştığını ve portun doğru olduğunu kontrol edin |
| Araç çalıştırma hataları | Parametre doğrulamasını ve hata işleme mekanizmasını gözden geçirin |
| Kimlik doğrulama hataları | API anahtarlarını ve izinleri doğrulayın |
| Şema doğrulama hataları | Parametrelerin tanımlı şemaya uygun olduğundan emin olun |
| Sunucu başlatılamıyor | Port çakışmalarını veya eksik bağımlılıkları kontrol edin |
| CORS hataları | Çapraz kaynak istekleri için uygun CORS başlıklarını yapılandırın |
| Kimlik doğrulama sorunları | Token geçerliliğini ve izinleri doğrulayın |

## Yerel Geliştirme

Yerel geliştirme ve test için MCP sunucularını doğrudan bilgisayarınızda çalıştırabilirsiniz:

1. **Sunucu sürecini başlatın**: MCP sunucu uygulamanızı çalıştırın
2. **Ağ yapılandırması**: Sunucunun beklenen portta erişilebilir olduğundan emin olun
3. **İstemcileri bağlayın**: `http://localhost:3000` gibi yerel bağlantı URL'lerini kullanın

```bash
# Example: Running a TypeScript MCP server locally
npm run start
# Server running at http://localhost:3000
```

## İlk MCP Sunucunuzu Oluşturma

[Temel Kavramlar](/01-CoreConcepts/README.md) konusunu önceki bir derste ele aldık, şimdi bu bilgiyi uygulama zamanı.

### Bir sunucu neler yapabilir?

Kod yazmaya başlamadan önce, bir sunucunun neler yapabileceğini hatırlayalım:

Bir MCP sunucusu örneğin:

- Yerel dosyalara ve veri tabanlarına erişebilir
- Uzak API'lere bağlanabilir
- Hesaplamalar yapabilir
- Diğer araçlar ve hizmetlerle entegre olabilir
- Etkileşim için bir kullanıcı arayüzü sağlayabilir

Harika, şimdi onun için neler yapabileceğimizi biliyoruz, kodlamaya başlayalım.

## Alıştırma: Bir sunucu oluşturma

Bir sunucu oluşturmak için şu adımları takip etmelisiniz:

- MCP SDK'sını yükleyin.
- Bir proje oluşturun ve proje yapısını ayarlayın.
- Sunucu kodunu yazın.
- Sunucuyu test edin.

### -1- Proje oluşturma

#### TypeScript

```sh
# Create project directory and initialize npm project
mkdir calculator-server
cd calculator-server
npm init -y
```

#### Python

```sh
# Create project dir
mkdir calculator-server
cd calculator-server
# Open the folder in Visual Studio Code - Skip this if you are using a different IDE
code .
```

#### .NET

```sh
dotnet new console -n McpCalculatorServer
cd McpCalculatorServer
```

#### Java

Java için bir Spring Boot projesi oluşturun:

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

Zip dosyasını çıkarın:

```bash
unzip calculator-server.zip -d calculator-server
cd calculator-server
# optional remove the unused test
rm -rf src/test/java
```

Aşağıdaki tam yapılandırmayı *pom.xml* dosyanıza ekleyin:

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

### -2- Bağımlılıkları ekleme

Artık projenizi oluşturduğunuza göre, sıradaki adım bağımlılıkları eklemek:

#### TypeScript

```sh
# If not already installed, install TypeScript globally
npm install typescript -g

# Install the MCP SDK and Zod for schema validation
npm install @modelcontextprotocol/sdk zod
npm install -D @types/node typescript
```

#### Python

```sh
# Create a virtual env and install dependencies
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

### -3- Proje dosyalarını oluşturma

#### TypeScript

*package.json* dosyasını açın ve sunucuyu oluşturup çalıştırabilmeniz için içeriği aşağıdakiyle değiştirin:

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

Aşağıdaki içerikle bir *tsconfig.json* oluşturun:

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

Kaynak kodunuz için bir dizin oluşturun:

```sh
mkdir src
touch src/index.ts
```

#### Python

*server.py* dosyası oluşturun:

```sh
touch server.py
```

#### .NET

Gerekli NuGet paketlerini yükleyin:

```sh
dotnet add package ModelContextProtocol --prerelease
dotnet add package Microsoft.Extensions.Hosting
```

#### Java

Java Spring Boot projeleri için proje yapısı otomatik olarak oluşturulur.

#### Rust

Rust için, `cargo init` komutunu çalıştırdığınızda varsayılan olarak bir *src/main.rs* dosyası oluşturulur. Dosyayı açın ve varsayılan kodu silin.

### -4- Sunucu kodu oluşturma

#### TypeScript

*index.ts* dosyası oluşturun ve aşağıdaki kodu ekleyin:

```typescript
import { McpServer, ResourceTemplate } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";
 
// Create an MCP server
const server = new McpServer({
  name: "Calculator MCP Server",
  version: "1.0.0"
});
```

Artık bir sunucunuz var, ancak pek bir şey yapmıyor, bunu düzeltelim.

#### Python

```python
# server.py
from mcp.server.fastmcp import FastMCP

# Create an MCP server
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

Java için, temel sunucu bileşenlerini oluşturun. Öncelikle ana uygulama sınıfını değiştirin:

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

Hesaplama hizmetini oluşturun *src/main/java/com/microsoft/mcp/sample/server/service/CalculatorService.java*:

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

**Üretime hazır bir hizmet için isteğe bağlı bileşenler:**

Başlangıç yapılandırmasını oluşturun *src/main/java/com/microsoft/mcp/sample/server/config/StartupConfig.java*:

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

Sağlık kontrolcüsü oluşturun *src/main/java/com/microsoft/mcp/sample/server/controller/HealthController.java*:

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

Hata işleyicisi oluşturun *src/main/java/com/microsoft/mcp/sample/server/exception/GlobalExceptionHandler.java*:

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

        // Getters
        public String getCode() { return code; }
        public String getMessage() { return message; }
    }
}
```

Özel bir banner oluşturun *src/main/resources/banner.txt*:

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

*src/main.rs* dosyasının üst kısmına aşağıdaki kodu ekleyin. Bu, MCP sunucunuz için gerekli kütüphaneleri ve modülleri içe aktarır.

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

Hesaplama sunucusu, iki sayıyı toplamak için basit bir sunucu olacak. Hesaplama isteğini temsil etmek için bir yapı oluşturalım.

```rust
#[derive(Debug, serde::Deserialize, schemars::JsonSchema)]
pub struct CalculatorRequest {
    pub a: f64,
    pub b: f64,
}
```

Sonra, hesaplama sunucusunu temsil etmek için bir yapı oluşturalım. Bu yapı, araç yönlendiricisini tutacak ve araçları kaydetmek için kullanılacak.

```rust
#[derive(Debug, Clone)]
pub struct Calculator {
    tool_router: ToolRouter<Self>,
}
```

Şimdi, `Calculator` yapısını uygulayarak yeni bir sunucu örneği oluşturabilir ve sunucu işleyicisini sunucu bilgilerini sağlamak için uygulayabiliriz.

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

Son olarak, sunucuyu başlatmak için ana işlevi uygulamamız gerekiyor. Bu işlev, `Calculator` yapısının bir örneğini oluşturacak ve standart giriş/çıkış üzerinden sunacak.

```rust
#[tokio::main]
async fn main() -> Result<(), Box<dyn Error>> {
    let service = Calculator::new().serve(stdio()).await?;
    service.waiting().await?;
    Ok(())
}
```

Sunucu artık kendisi hakkında temel bilgiler sağlamak için ayarlandı. Şimdi toplama işlemi yapmak için bir araç ekleyeceğiz.

### -5- Bir araç ve kaynak ekleme

Bir araç ve kaynak eklemek için aşağıdaki kodu ekleyin:

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

Aracınız `a` ve `b` parametrelerini alır ve bir yanıt üreten bir işlev çalıştırır:

```typescript
{
  contents: [{
    type: "text", content: "some content"
  }]
}
```

Kaynağınız "greeting" adlı bir dize üzerinden erişilir ve `name` parametresini alır ve araca benzer bir yanıt üretir:

```typescript
{
  uri: "<href>",
  text: "a text"
}
```

#### Python

```python
# Add an addition tool
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


# Add a dynamic greeting resource
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}!"
```

Yukarıdaki kodda şunları yaptık:

- `add` adlı bir araç tanımladık, bu araç iki tam sayı parametresi `a` ve `p` alır.
- `greeting` adlı bir kaynak oluşturduk, bu kaynak `name` parametresini alır.

#### .NET

Program.cs dosyanıza şunu ekleyin:

```csharp
[McpServerToolType]
public static class CalculatorTool
{
    [McpServerTool, Description("Adds two numbers")]
    public static string Add(int a, int b) => $"Sum {a + b}";
}
```

#### Java

Araçlar önceki adımda zaten oluşturuldu.

#### Rust

`impl Calculator` bloğu içinde yeni bir araç ekleyin:

```rust
#[tool(description = "Adds a and b")]
async fn add(
    &self,
    Parameters(CalculatorRequest { a, b }): Parameters<CalculatorRequest>,
) -> String {
    (a + b).to_string()
}
```

### -6- Son kod

Sunucunun başlatılabilmesi için gerekli son kodu ekleyelim:

#### TypeScript

```typescript
// Start receiving messages on stdin and sending messages on stdout
const transport = new StdioServerTransport();
await server.connect(transport);
```

İşte tam kod:

```typescript
// index.ts
import { McpServer, ResourceTemplate } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";

// Create an MCP server
const server = new McpServer({
  name: "Calculator MCP Server",
  version: "1.0.0"
});

// Add an addition tool
server.tool(
  "add",
  { a: z.number(), b: z.number() },
  async ({ a, b }) => ({
    content: [{ type: "text", text: String(a + b) }]
  })
);

// Add a dynamic greeting resource
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

// Start receiving messages on stdin and sending messages on stdout
const transport = new StdioServerTransport();
server.connect(transport);
```

#### Python

```python
# server.py
from mcp.server.fastmcp import FastMCP

# Create an MCP server
mcp = FastMCP("Demo")


# Add an addition tool
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


# Add a dynamic greeting resource
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}!"

# Main execution block - this is required to run the server
if __name__ == "__main__":
    mcp.run()
```

#### .NET

Aşağıdaki içerikle bir Program.cs dosyası oluşturun:

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

Tam ana uygulama sınıfınız şu şekilde görünmelidir:

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

Rust sunucusu için nihai kod şu şekilde olmalıdır:

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

### -7- Sunucuyu test etme

Sunucuyu aşağıdaki komutla başlatın:

#### TypeScript

```sh
npm run build
```

#### Python

```sh
mcp run server.py
```

> MCP Inspector'ı kullanmak için `mcp dev server.py` komutunu kullanın, bu komut Inspector'ı otomatik olarak başlatır ve gerekli proxy oturum tokenini sağlar. Eğer `mcp run server.py` kullanıyorsanız, Inspector'ı manuel olarak başlatmanız ve bağlantıyı yapılandırmanız gerekir.

#### .NET

Proje dizininizde olduğunuzdan emin olun:

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

Sunucuyu biçimlendirmek ve çalıştırmak için aşağıdaki komutları çalıştırın:

```sh
cargo fmt
cargo run
```

### -8- Inspector ile çalıştırma

Inspector, sunucunuzu başlatabilen ve onunla etkileşim kurmanıza olanak tanıyan harika bir araçtır, böylece çalıştığını test edebilirsiniz. Hadi başlatalım:

> [!NOTE]
> "command" alanı, belirli çalışma zamanınızla bir sunucu çalıştırma komutunu içerdiği için farklı görünebilir.

#### TypeScript

```sh
npx @modelcontextprotocol/inspector node build/index.js
```

veya bunu *package.json* dosyanıza şu şekilde ekleyin: `"inspector": "npx @modelcontextprotocol/inspector node build/index.js"` ve ardından `npm run inspector` komutunu çalıştırın.

Python, Node.js tabanlı bir araç olan Inspector'ı sarar. Bu aracı şu şekilde çağırmak mümkündür:

```sh
mcp dev server.py
```

Ancak, araçta mevcut olan tüm yöntemleri uygulamaz, bu nedenle aşağıdaki gibi doğrudan Node.js aracını çalıştırmanız önerilir:

```sh
npx @modelcontextprotocol/inspector mcp run server.py
```

Eğer komutları ve argümanları yapılandırmanıza olanak tanıyan bir araç veya IDE kullanıyorsanız,
`Command` alanında `python` ve `Arguments` olarak `server.py` ayarladığınızdan emin olun. Bu, scriptin doğru şekilde çalışmasını sağlar.

#### .NET

Proje dizininizde olduğunuzdan emin olun:

```sh
cd McpCalculatorServer
npx @modelcontextprotocol/inspector dotnet run
```

#### Java

Hesap makinesi sunucunuzun çalıştığından emin olun.  
Sonrasında denetleyiciyi çalıştırın:

```cmd
npx @modelcontextprotocol/inspector
```

Denetleyici web arayüzünde:

1. "SSE"yi taşıma türü olarak seçin  
2. URL'yi şu şekilde ayarlayın: `http://localhost:8080/sse`  
3. "Bağlan" butonuna tıklayın  

![Bağlan](../../../../translated_images/tool.163d33e3ee307e209ef146d8f85060d2f7e83e9f59b3b1699a77204ae0454ad2.tr.png)

**Artık sunucuya bağlandınız**  
**Java sunucu test etme bölümü tamamlandı**

Bir sonraki bölüm, sunucuyla etkileşim kurmakla ilgili.

Aşağıdaki kullanıcı arayüzünü görmelisiniz:

![Bağlan](../../../../translated_images/connect.141db0b2bd05f096fb1dd91273771fd8b2469d6507656c3b0c9df4b3c5473929.tr.png)

1. Bağlan butonunu seçerek sunucuya bağlanın  
   Sunucuya bağlandıktan sonra aşağıdaki ekranı görmelisiniz:

   ![Bağlandı](../../../../translated_images/connected.73d1e042c24075d386cacdd4ee7cd748c16364c277d814e646ff2f7b5eefde85.tr.png)

1. "Araçlar" ve "listTools"u seçin, "Add" seçeneğini görmelisiniz. "Add"i seçin ve parametre değerlerini doldurun.

   "add" aracından gelen bir sonucu görmelisiniz:

   ![Add çalıştırma sonucu](../../../../translated_images/ran-tool.a5a6ee878c1369ec1e379b81053395252a441799dbf23416c36ddf288faf8249.tr.png)

Tebrikler, ilk sunucunuzu oluşturup çalıştırmayı başardınız!

#### Rust

MCP Inspector CLI ile Rust sunucusunu çalıştırmak için şu komutu kullanın:

```sh
npx @modelcontextprotocol/inspector cargo run --cli --method tools/call --tool-name add --tool-arg a=1 b=2
```

### Resmi SDK'lar

MCP, birçok dil için resmi SDK'lar sağlar:

- [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk) - Microsoft ile iş birliği içinde geliştirilmiştir  
- [Java SDK](https://github.com/modelcontextprotocol/java-sdk) - Spring AI ile iş birliği içinde geliştirilmiştir  
- [TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk) - Resmi TypeScript uygulaması  
- [Python SDK](https://github.com/modelcontextprotocol/python-sdk) - Resmi Python uygulaması  
- [Kotlin SDK](https://github.com/modelcontextprotocol/kotlin-sdk) - Resmi Kotlin uygulaması  
- [Swift SDK](https://github.com/modelcontextprotocol/swift-sdk) - Loopwork AI ile iş birliği içinde geliştirilmiştir  
- [Rust SDK](https://github.com/modelcontextprotocol/rust-sdk) - Resmi Rust uygulaması  

## Önemli Noktalar

- MCP geliştirme ortamını kurmak, dil özelindeki SDK'larla oldukça kolaydır  
- MCP sunucuları oluşturmak, net şemalarla araçlar oluşturmayı ve kaydetmeyi içerir  
- Güvenilir MCP uygulamaları için test ve hata ayıklama çok önemlidir  

## Örnekler

- [Java Hesap Makinesi](../samples/java/calculator/README.md)  
- [.Net Hesap Makinesi](../../../../03-GettingStarted/samples/csharp)  
- [JavaScript Hesap Makinesi](../samples/javascript/README.md)  
- [TypeScript Hesap Makinesi](../samples/typescript/README.md)  
- [Python Hesap Makinesi](../../../../03-GettingStarted/samples/python)  
- [Rust Hesap Makinesi](../../../../03-GettingStarted/samples/rust)  

## Ödev

Seçtiğiniz bir araçla basit bir MCP sunucusu oluşturun:

1. Aracı tercih ettiğiniz dilde (.NET, Java, Python, TypeScript veya Rust) uygulayın.  
2. Girdi parametrelerini ve dönüş değerlerini tanımlayın.  
3. Sunucunun beklendiği gibi çalıştığından emin olmak için denetleyici aracını çalıştırın.  
4. Çeşitli girdilerle uygulamayı test edin.  

## Çözüm

[Çözüm](./solution/README.md)

## Ek Kaynaklar

- [Azure'da Model Context Protocol kullanarak Agent oluşturma](https://learn.microsoft.com/azure/developer/ai/intro-agents-mcp)  
- [Azure Container Apps ile Uzaktan MCP (Node.js/TypeScript/JavaScript)](https://learn.microsoft.com/samples/azure-samples/mcp-container-ts/mcp-container-ts/)  
- [.NET OpenAI MCP Agent](https://learn.microsoft.com/samples/azure-samples/openai-mcp-agent-dotnet/openai-mcp-agent-dotnet/)  

## Sıradaki Adım

Sonraki: [MCP İstemcileriyle Başlangıç](../02-client/README.md)

---

**Feragatname**:  
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çeviriler hata veya yanlışlıklar içerebilir. Belgenin orijinal dili, yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımından kaynaklanan yanlış anlamalar veya yanlış yorumlamalardan sorumlu değiliz.