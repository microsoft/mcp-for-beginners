# MCP ile Başlarken

Model Context Protocol (MCP) ile ilk adımlarınıza hoş geldiniz! MCP'ye yeniyseniz veya bilginizi derinleştirmek istiyorsanız, bu rehber sizi temel kurulum ve geliştirme süreci boyunca yönlendirecektir. MCP'nin AI modelleri ile uygulamalar arasında nasıl sorunsuz entegrasyon sağladığını keşfedecek ve MCP destekli çözümler geliştirmek ve test etmek için ortamınızı hızlıca nasıl hazırlayacağınızı öğreneceksiniz.

> Özet; AI uygulamaları geliştiriyorsanız, LLM'inizi (büyük dil modeli) daha bilgili hale getirmek için araçlar ve diğer kaynaklar ekleyebileceğinizi bilirsiniz. Ancak bu araçları ve kaynakları bir sunucuya yerleştirirseniz, uygulama ve sunucu yetenekleri LLM ile/LM olmadan herhangi bir istemci tarafından kullanılabilir.

## Genel Bakış

Bu ders, MCP ortamlarının kurulması ve ilk MCP uygulamalarınızın geliştirilmesi hakkında pratik rehberlik sağlar. Gerekli araçları ve çerçeveleri nasıl kuracağınızı, temel MCP sunucuları oluşturmayı, host uygulamalar yaratmayı ve uygulamalarınızı test etmeyi öğreneceksiniz.

Model Context Protocol (MCP), uygulamaların LLM'lere (büyük dil modellerine) bağlam sağlamasını standartlaştıran açık bir protokoldür. MCP'yi AI uygulamaları için USB-C portu gibi düşünebilirsiniz - AI modellerini farklı veri kaynakları ve araçlara çekici biçimde bağlamak için standart bir yol sağlar.

## Öğrenme Hedefleri

Bu ders sonunda şunları yapabileceksiniz:

- C#, Java, Python, TypeScript ve Rust için MCP geliştirme ortamlarını kurmak
- Özel özelliklere (kaynaklar, istemler, araçlar) sahip temel MCP sunucuları oluşturmak ve dağıtmak
- MCP sunucularına bağlanan host uygulamalar geliştirmek
- MCP uygulamalarını test etmek ve hata ayıklamak

## MCP Ortamınızı Kurma

MCP ile çalışmaya başlamadan önce, geliştirme ortamınızı hazırlamanız ve temel iş akışını anlamanız önemlidir. Bu bölüm, MCP ile sorunsuz bir başlangıç yapmanızı sağlamak için ilk kurulum adımlarında size rehberlik edecektir.

### Önkoşullar

MCP geliştirmesine başlamadan önce, aşağıdakilere sahip olduğunuzdan emin olun:

- **Geliştirme Ortamı**: Seçtiğiniz dil için (C#, Java, Python, TypeScript veya Rust)
- **IDE/Editor**: Visual Studio, Visual Studio Code, IntelliJ, Eclipse, PyCharm veya herhangi modern bir kod editörü
- **Paket Yöneticileri**: NuGet, Maven/Gradle, pip, npm/yarn veya Cargo
- **API Anahtarları**: Host uygulamalarınızda kullanmayı planladığınız herhangi bir AI servisi için

## Temel MCP Sunucu Yapısı

Bir MCP sunucusu tipik olarak şunları içerir:

- **Sunucu Konfigürasyonu**: Port, kimlik doğrulama ve diğer ayarların kurulumu
- **Kaynaklar**: LLM'lere sunulan veri ve bağlam
- **Araçlar**: Modellerin tetikleyebileceği işlevsellik
- **İstemler**: Metin oluşturma veya yapılandırma için şablonlar

İşte TypeScript ile basitleştirilmiş bir örnek:

```typescript
import { McpServer, ResourceTemplate } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";

// Bir MCP sunucusu oluşturun
const server = new McpServer({
  name: "Demo",
  version: "1.0.0"
});

// Bir toplama aracı ekleyin
server.tool("add",
  { a: z.number(), b: z.number() },
  async ({ a, b }) => ({
    content: [{ type: "text", text: String(a + b) }]
  })
);

// Dinamik bir karşılama kaynağı ekleyin
server.resource(
  "file",
  // 'list' parametresi kaynağın mevcut dosyaları nasıl listelediğini kontrol eder. Undefined olarak ayarlanması bu kaynak için listelemeyi devre dışı bırakır.
  new ResourceTemplate("file://{path}", { list: undefined }),
  async (uri, { path }) => ({
    contents: [{
      uri: uri.href,
      text: `File, ${path}!`
    }]
  })
);

// Dosya içeriğini okuyan bir dosya kaynağı ekleyin
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

// stdin üzerinden mesaj almayı ve stdout üzerinden mesaj göndermeyi başlatın
const transport = new StdioServerTransport();
await server.connect(transport);
```

Yukarıdaki kodda:

- MCP TypeScript SDK’dan gerekli sınıflar içe aktarılır.
- Yeni bir MCP sunucu örneği oluşturulur ve yapılandırılır.
- Özel bir araç (`calculator`) bir işleyici fonksiyon ile kaydedilir.
- MCP isteklerini dinlemek için sunucu başlatılır.

## Test ve Hata Ayıklama

MCP sunucunuzu test etmeye başlamadan önce, kullanılabilir araçları ve hata ayıklama için en iyi uygulamaları anlamak önemlidir. Etkili testler, sunucunuzun beklendiği gibi çalışmasını sağlar ve sorunları hızlıca belirleyip çözmenize yardımcı olur. Aşağıdaki bölüm, MCP uygulamanızın doğrulanması için önerilen yaklaşımları özetler.

MCP, sunucularınızı test edip hata ayıklamanıza yardımcı olacak araçlar sunar:

- **Inspector aracı**: Bu grafik arayüz, sunucuya bağlanmanızı ve araçlarınızı, istemlerinizi ve kaynaklarınızı test etmenizi sağlar.
- **curl**: Ayrıca curl gibi komut satırı araçları ya da HTTP komutları oluşturup çalıştırabilen diğer istemcilerle sunucuya bağlanabilirsiniz.

### MCP Inspector Kullanımı

[MCP Inspector](https://github.com/modelcontextprotocol/inspector), size şu konularda yardımcı olan görsel bir test aracıdır:

1. **Sunucu Yetkinliklerini Keşfetme**: Mevcut kaynakları, araçları ve istemleri otomatik olarak algılar
2. **Araç Çalıştırmayı Test Etme**: Farklı parametreleri deneyip yanıtları gerçek zamanlı görme
3. **Sunucu Meta Verilerini Görüntüleme**: Sunucu bilgileri, şemalar ve yapılandırmaları inceleme

```bash
# Örnek TypeScript, MCP Inspector'ı kurma ve çalıştırma
npx @modelcontextprotocol/inspector node build/index.js
```

Yukarıdaki komutları çalıştırdığınızda, MCP Inspector tarayıcınızda yerel bir web arayüzü başlatır. Kayıtlı MCP sunucuları, mevcut araçları, kaynakları ve istemleri gösteren bir kontrol paneli görmeyi bekleyebilirsiniz. Arayüz, araç çalıştırmayı interaktif olarak test etmenize, sunucu meta verilerini incelemenize ve gerçek zamanlı yanıtları görüntülemenize olanak tanır; böylece MCP sunucu uygulamalarınızı kolayca doğrulayabilir ve hata ayıklayabilirsiniz.

Böyle görünebilir:

![MCP Inspector server connection](../../../../translated_images/tr/connected.73d1e042c24075d3.webp)

## Yaygın Kurulum Sorunları ve Çözümleri

| Sorun | Olası Çözüm |
|-------|-------------|
| Bağlantı reddedildi | Sunucunun çalıştığını ve portun doğru olduğunu kontrol edin |
| Araç çalıştırma hataları | Parametre doğrulaması ve hata yönetimini gözden geçirin |
| Kimlik doğrulama hataları | API anahtarlarını ve izinleri doğrulayın |
| Şema doğrulama hataları | Parametrelerin tanımlı şemaya uygun olduğundan emin olun |
| Sunucu başlatılamıyor | Port çakışması veya eksik bağımlılıkları kontrol edin |
| CORS hataları | Cross-origin istekler için uygun CORS başlıklarını yapılandırın |
| Kimlik doğrulama sorunları | Token geçerliliği ve izinlerini doğrulayın |

## Yerel Geliştirme

Yerel geliştirme ve testler için, MCP sunucularını doğrudan makinenizde çalıştırabilirsiniz:

1. **Sunucu işlemini başlatın**: MCP sunucu uygulamanızı çalıştırın
2. **Ağ yapılandırması yapın**: Sunucunun beklenen portta erişilebilir olduğundan emin olun
3. **İstemcileri bağlayın**: `http://localhost:3000` gibi yerel bağlantı URL’lerini kullanın

```bash
# Örnek: Yerel olarak TypeScript MCP sunucusu çalıştırmak
npm run start
# Sunucu http://localhost:3000 adresinde çalışıyor
```

## İlk MCP Sunucunuzu Oluşturma

Önceki dersimizde [Temel Kavramlar](../../01-CoreConcepts/README.md) konusunu ele aldık; şimdi bu bilgileri uygulamaya koyma zamanı.

### Bir sunucu neler yapabilir?

Koda geçmeden önce sunucunun yapabileceklerini hatırlayalım:

Bir MCP sunucu örneğin şunları yapabilir:

- Yerel dosya ve veritabanlarına erişmek
- Uzak API’lere bağlanmak
- Hesaplamalar yapmak
- Diğer araçlar ve servislerle entegre olmak
- Kullanıcı ile etkileşim için bir arayüz sağlamak

Harika, şimdi ne yapabileceğimizi bildiğimize göre kodlamaya başlayalım.

## Alıştırma: Bir sunucu oluşturma

Bir sunucu oluşturmak için şu adımları izlemelisiniz:

- MCP SDK'sını kurmak.
- Bir proje oluşturup proje yapısını kurmak.
- Sunucu kodunu yazmak.
- Sunucuyu test etmek.

### -1- Proje Oluşturma

#### TypeScript

```sh
# Proje dizini oluşturun ve npm projesini başlatın
mkdir calculator-server
cd calculator-server
npm init -y
```

#### Python

```sh
# Proje dizini oluştur
mkdir calculator-server
cd calculator-server
# Klasörü Visual Studio Code'da aç - Farklı bir IDE kullanıyorsanız bunu atlayın
code .
```

#### .NET

```sh
dotnet new console -n McpCalculatorServer
cd McpCalculatorServer
```

#### Java

Java için, Spring Boot projesi oluşturun:

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
# isteğe bağlı kullanılmayan testi kaldır
rm -rf src/test/java
```

*Pom.xml* dosyanıza aşağıdaki tam konfigürasyonu ekleyin:

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

### -2- Bağımlılıkları ekle

Projeyi oluşturduktan sonra, şimdi bağımlılıkları ekleyelim:

#### TypeScript

```sh
# Henüz yüklenmemişse, TypeScript'i global olarak yükleyin
npm install typescript -g

# Schema doğrulama için MCP SDK ve Zod'u yükleyin
npm install @modelcontextprotocol/sdk zod
npm install -D @types/node typescript
```

#### Python

```sh
# Sanal bir ortam oluşturun ve bağımlılıkları yükleyin
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

### -3- Proje dosyalarını oluştur

#### TypeScript

*package.json* dosyasını açın ve sunucuyu derleyip çalıştırabilmenizi sağlamak için içeriğini aşağıdakiyle değiştirin:

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

Aşağıdaki içeriğe sahip *tsconfig.json* dosyasını oluşturun:

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

Kaynak kodlarınız için bir dizin oluşturun:

```sh
mkdir src
touch src/index.ts
```

#### Python

*server.py* dosyası oluşturun

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

Rust için, `cargo init` komutunu çalıştırdığınızda *src/main.rs* dosyası varsayılan olarak oluşturulur. Dosyayı açın ve varsayılan kodu silin.

### -4- Sunucu kodunu oluşturun

#### TypeScript

*index.ts* dosyasını oluşturun ve aşağıdaki kodu ekleyin:

```typescript
import { McpServer, ResourceTemplate } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";
 
// Bir MCP sunucusu oluşturun
const server = new McpServer({
  name: "Calculator MCP Server",
  version: "1.0.0"
});
```

Şimdi bir sunucunuz var, ancak çok fazla işi yok, bunu düzeltelim.

#### Python

```python
# server.py
from mcp.server.fastmcp import FastMCP

# Bir MCP sunucusu oluşturun
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

Java için, temel sunucu bileşenlerini oluşturun. İlk olarak ana uygulama sınıfını değiştirin:

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

Calculator servisi oluşturun *src/main/java/com/microsoft/mcp/sample/server/service/CalculatorService.java*:

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

**Üretim için opsiyonel bileşenler:**

Başlatma konfigürasyonu oluşturun *src/main/java/com/microsoft/mcp/sample/server/config/StartupConfig.java*:

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

Sağlık denetleyicisi oluşturun *src/main/java/com/microsoft/mcp/sample/server/controller/HealthController.java*:

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

Hata yakalayıcı oluşturun *src/main/java/com/microsoft/mcp/sample/server/exception/GlobalExceptionHandler.java*:

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

        // Erişimciler
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

*src/main.rs* dosyasının en üstüne aşağıdaki kodu ekleyin. Bu, MCP sunucunuz için gerekli kütüphaneleri ve modülleri içe aktarır.

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

Calculator sunucusu, iki sayıyı toplama işlemi yapabilen basit bir sunucu olacak. Calculator isteğini temsil eden bir struct oluşturalım.

```rust
#[derive(Debug, serde::Deserialize, schemars::JsonSchema)]
pub struct CalculatorRequest {
    pub a: f64,
    pub b: f64,
}
```

Sonra, araç yönlendiriciyi tutacak olan calculator sunucusunu temsil eden başka bir struct oluşturun.

```rust
#[derive(Debug, Clone)]
pub struct Calculator {
    tool_router: ToolRouter<Self>,
}
```

Şimdi, `Calculator` struct'ını, sunucunun yeni bir örneğini oluşturmak ve sunucu bilgisi sağlamak için sunucu tutucusunu implemente etmek üzere uygulayabiliriz.

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

Son olarak, sunucuyu başlatmak için ana fonksiyonu implemente etmeliyiz. Bu fonksiyon `Calculator` struct’ının bir örneğini oluşturacak ve standart giriş/çıkış üzerinden hizmet verecek.

```rust
#[tokio::main]
async fn main() -> Result<(), Box<dyn Error>> {
    let service = Calculator::new().serve(stdio()).await?;
    service.waiting().await?;
    Ok(())
}
```

Sunucu artık kendisi hakkında temel bilgiler sunacak şekilde ayarlandı. Şimdi toplama işlemi yapacak bir araç ekleyeceğiz.

### -5- Bir araç ve kaynak ekleyin

Aşağıdaki kodları ekleyerek bir araç ve kaynak ekleyin:

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

Aracınız `a` ve `b` parametrelerini alır ve aşağıdaki formda bir yanıt üreten bir fonksiyonu çalıştırır:

```typescript
{
  contents: [{
    type: "text", content: "some content"
  }]
}
```

Kaynağınıza `"greeting"` dizgesi üzerinden erişilir, `name` parametresi alır ve araca benzer bir yanıt üretir:

```typescript
{
  uri: "<href>",
  text: "a text"
}
```

#### Python

```python
# Bir toplama aracı ekleyin
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


# Dinamik bir selamlama kaynağı ekleyin
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}!"
```

Yukarıdaki kodda:

- `add` adında parametreleri `a` ve `b` olan, her ikisi de tamsayı, bir araç tanımladık.
- `name` parametresi alan `greeting` adlı bir kaynak oluşturduk.

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

`impl Calculator` bloğu içine yeni bir araç ekleyin:

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

Sunucunun başlatılabilmesi için gereken son kodu ekleyelim:

#### TypeScript

```typescript
// stdin üzerinden mesaj almaya ve stdout üzerinden mesaj göndermeye başlayın
const transport = new StdioServerTransport();
await server.connect(transport);
```

Tam kod aşağıdaki gibidir:

```typescript
// index.ts
import { McpServer, ResourceTemplate } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";

// Bir MCP sunucusu oluştur
const server = new McpServer({
  name: "Calculator MCP Server",
  version: "1.0.0"
});

// Bir toplama aracı ekle
server.tool(
  "add",
  { a: z.number(), b: z.number() },
  async ({ a, b }) => ({
    content: [{ type: "text", text: String(a + b) }]
  })
);

// Dinamik bir karşılama kaynağı ekle
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

// stdin'den mesaj almaya ve stdout'a mesaj göndermeye başla
const transport = new StdioServerTransport();
server.connect(transport);
```

#### Python

```python
# server.py
from mcp.server.fastmcp import FastMCP

# Bir MCP sunucusu oluşturun
mcp = FastMCP("Demo")


# Bir toplama aracı ekleyin
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


# Dinamik bir karşılama kaynağı ekleyin
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}!"

# Ana yürütme bloğu - sunucuyu çalıştırmak için gereklidir
if __name__ == "__main__":
    mcp.run()
```

#### .NET

Aşağıdaki içeriğe sahip bir Program.cs dosyası oluşturun:

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

Tam ana uygulama sınıfınız şöyle görünmelidir:

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

Rust sunucusu için son kod şöyle görünmelidir:

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

### -7- Sunucuyu test edin

Sunucuyu aşağıdaki komutla başlatın:

#### TypeScript

```sh
npm run build
```

#### Python

```sh
mcp run server.py
```

> MCP Inspector'u kullanmak için `mcp dev server.py` komutunu kullanın; bu komut Inspector’u otomatik başlatır ve gerekli proxy oturum tokenını sağlar. Eğer `mcp run server.py` kullanıyorsanız, Inspector’u manuel başlatmanız ve bağlantıyı yapılandırmanız gerekir.

#### .NET

Proje dizininde olduğunuzdan emin olun:

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

Sunucuyu biçimlendirmek ve çalıştırmak için şu komutları kullanın:

```sh
cargo fmt
cargo run
```

### -8- Inspector ile çalıştırma

Inspector, sunucunuzu başlatan ve onunla etkileşime girip çalıştığını test etmenizi sağlayan harika bir araçtır. Hadi başlatalım:

> [!NOTE]
> "komut" alanı, sunucunuzu belirli çalışma ortamınızla çalıştırmak için kullandığınız komutu içereceğinden farklı görünebilir.

#### TypeScript

```sh
npx @modelcontextprotocol/inspector node build/index.js
```

ya da *package.json* dosyanıza şöyle ekleyin: `"inspector": "npx @modelcontextprotocol/inspector node build/index.js"` ve ardından `npm run inspector` komutu ile çalıştırın

#### Python

Python, inspector adında bir Node.js aracını sarmalar. Bu araç şu şekilde çağrılabilir:

```sh
mcp dev server.py
```

Ancak, araçta mevcut tüm yöntemleri uygulamaz, bu nedenle Node.js aracını doğrudan aşağıdaki şekilde çalıştırmanız önerilir:

```sh
npx @modelcontextprotocol/inspector mcp run server.py
```

Eğer komutların ve argümanların çalışma zamanında yapılandırılmasına izin veren bir araç veya IDE kullanıyorsanız,
`Command` alanına `python` ve `Arguments` alanına `server.py` ayarlandığından emin olun. Bu, betiğin düzgün çalışmasını sağlar.

#### .NET

Proje dizininizde olduğunuzdan emin olun:

```sh
cd McpCalculatorServer
npx @modelcontextprotocol/inspector dotnet run
```

#### Java

Calculator sunucunuzun çalıştığından emin olun
Ardından denetleyiciyi çalıştırın:

```cmd
npx @modelcontextprotocol/inspector
```

Denetleyici web arayüzünde:

1. İletim türü olarak "SSE" seçin
2. URL'yi şu şekilde ayarlayın: `http://localhost:8080/sse`
3. "Connect" düğmesine tıklayın

![Connect](../../../../translated_images/tr/tool.163d33e3ee307e20.webp)

**Şimdi sunucuya bağlısınız**
**Java sunucu test bölümü tamamlandı**

Sonraki bölüm, sunucu ile etkileşimle ilgilidir.

Aşağıdaki kullanıcı arayüzünü görmelisiniz:

![Connect](../../../../translated_images/tr/connect.141db0b2bd05f096.webp)

1. Bağlan düğmesini seçerek sunucuya bağlanın
  Sunucuya bağlandıktan sonra aşağıdakileri görmelisiniz:

  ![Connected](../../../../translated_images/tr/connected.73d1e042c24075d3.webp)

1. "Tools" ve "listTools" seçin, "Add" görünmelidir, "Add" seçin ve parametre değerlerini doldurun.

  Aşağıdaki yanıtı görmelisiniz, yani "add" aracından bir sonuç:

  ![Result of running add](../../../../translated_images/tr/ran-tool.a5a6ee878c1369ec.webp)

Tebrikler, ilk sunucunuzu oluşturup çalıştırmayı başardınız!

#### Rust

Rust sunucusunu MCP Inspector CLI ile çalıştırmak için şu komutu kullanın:

```sh
npx @modelcontextprotocol/inspector cargo run --cli --method tools/call --tool-name add --tool-arg a=1 b=2
```

### Resmi SDK'lar

MCP, birden çok dil için resmi SDK'lar sağlar:

- [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk) - Microsoft ile işbirliği içinde bakımda
- [Java SDK](https://github.com/modelcontextprotocol/java-sdk) - Spring AI ile işbirliği içinde bakımda
- [TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk) - Resmi TypeScript uygulaması
- [Python SDK](https://github.com/modelcontextprotocol/python-sdk) - Resmi Python uygulaması
- [Kotlin SDK](https://github.com/modelcontextprotocol/kotlin-sdk) - Resmi Kotlin uygulaması
- [Swift SDK](https://github.com/modelcontextprotocol/swift-sdk) - Loopwork AI ile işbirliği içinde bakımda
- [Rust SDK](https://github.com/modelcontextprotocol/rust-sdk) - Resmi Rust uygulaması

## Ana Hatlar

- MCP geliştirme ortamı, dil özel SDK'ları ile kurulumu kolaydır
- MCP sunucuları, açık şemalara sahip araçlar oluşturmak ve kaydetmekle ilgilidir
- Test ve hata ayıklama, güvenilir MCP uygulamaları için esastır

## Örnekler

- [Java Calculator](../samples/java/calculator/README.md)
- [.Net Calculator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Calculator](../samples/javascript/README.md)
- [TypeScript Calculator](../samples/typescript/README.md)
- [Python Calculator](../../../../03-GettingStarted/samples/python)
- [Rust Calculator](../../../../03-GettingStarted/samples/rust)

## Ödev

Seçtiğiniz bir araçla basit bir MCP sunucusu oluşturun:

1. Tercih ettiğiniz dilde aracı uygulayın (.NET, Java, Python, TypeScript veya Rust).
2. Girdi parametrelerini ve dönüş değerlerini tanımlayın.
3. Sunucunun doğru çalıştığından emin olmak için denetleyici aracını çalıştırın.
4. Uygulamayı çeşitli girdilerle test edin.

## Çözüm

[Solution](./solution/README.md)

## Ek Kaynaklar

- [Azure üzerinde Model Context Protocol kullanarak Agent'lar oluşturma](https://learn.microsoft.com/azure/developer/ai/intro-agents-mcp)
- [Azure Container Apps ile Uzaktan MCP (Node.js/TypeScript/JavaScript)](https://learn.microsoft.com/samples/azure-samples/mcp-container-ts/mcp-container-ts/)
- [.NET OpenAI MCP Agent](https://learn.microsoft.com/samples/azure-samples/openai-mcp-agent-dotnet/openai-mcp-agent-dotnet/)

## Sonraki

Sonraki: [MCP İstemcileri ile Başlarken](../02-client/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Feragatname**:
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hatalar veya yanlışlıklar içerebileceğini lütfen unutmayın. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanılmasından kaynaklanan herhangi bir yanlış anlama veya yanlış yorumlamadan sorumlu tutulamayız.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->