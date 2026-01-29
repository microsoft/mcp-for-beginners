# MCP Sunucusu stdio Taşıma ile

> **⚠️ Önemli Güncelleme**: MCP Spesifikasyonu 2025-06-18 itibarıyla, bağımsız SSE (Sunucu Tarafından Gönderilen Olaylar) taşıma yöntemi **kullanımdan kaldırılmış** ve "Akışlı HTTP" taşıma yöntemi ile değiştirilmiştir. Mevcut MCP spesifikasyonu iki ana taşıma mekanizmasını tanımlar:
> 1. **stdio** - Standart giriş/çıkış (yerel sunucular için önerilir)
> 2. **Akışlı HTTP** - SSE'yi dahili olarak kullanabilecek uzak sunucular için
>
> Bu ders, çoğu MCP sunucu uygulaması için önerilen yaklaşım olan **stdio taşıma** üzerine odaklanacak şekilde güncellenmiştir.

Stdio taşıma, MCP sunucularının standart giriş ve çıkış akışları aracılığıyla istemcilerle iletişim kurmasını sağlar. Bu, mevcut MCP spesifikasyonunda en yaygın kullanılan ve önerilen taşıma mekanizmasıdır ve çeşitli istemci uygulamalarıyla kolayca entegre edilebilen basit ve verimli bir yol sunar.

## Genel Bakış

Bu ders, stdio taşıma kullanarak MCP Sunucuları oluşturmayı ve tüketmeyi kapsar.

## Öğrenme Hedefleri

Bu dersin sonunda şunları yapabileceksiniz:

- Stdio taşıma kullanarak bir MCP Sunucusu oluşturmak.
- MCP Sunucusunu Inspector ile hata ayıklamak.
- MCP Sunucusunu Visual Studio Code kullanarak tüketmek.
- Mevcut MCP taşıma mekanizmalarını ve neden stdio'nun önerildiğini anlamak.

## stdio Taşıma - Nasıl Çalışır?

Stdio taşıma, mevcut MCP spesifikasyonunda (2025-06-18) desteklenen iki taşıma türünden biridir. İşte nasıl çalıştığı:

- **Basit İletişim**: Sunucu, standart girişten (`stdin`) JSON-RPC mesajlarını okur ve standart çıkışa (`stdout`) mesajlar gönderir.
- **İşlem Tabanlı**: İstemci, MCP sunucusunu bir alt işlem olarak başlatır.
- **Mesaj Formatı**: Mesajlar, yeni satırlarla ayrılmış bireysel JSON-RPC istekleri, bildirimleri veya yanıtlarıdır.
- **Günlükleme**: Sunucu, günlükleme amacıyla standart hataya (`stderr`) UTF-8 dizileri yazabilir.

### Temel Gereksinimler:
- Mesajlar yeni satırlarla ayrılmalı ve gömülü yeni satırlar içermemelidir.
- Sunucu, `stdout`'a geçerli bir MCP mesajı olmayan hiçbir şey yazmamalıdır.
- İstemci, sunucunun `stdin`'ine geçerli bir MCP mesajı olmayan hiçbir şey yazmamalıdır.

### TypeScript

```typescript
import { Server } from "@modelcontextprotocol/sdk/server/index.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";

const server = new Server(
  {
    name: "example-server",
    version: "1.0.0",
  },
  {
    capabilities: {
      tools: {},
    },
  }
);
```

Yukarıdaki kodda:

- MCP SDK'den `Server` sınıfını ve `StdioServerTransport`'u içe aktarıyoruz.
- Temel yapılandırma ve yeteneklerle bir sunucu örneği oluşturuyoruz.

### Python

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server

# Create server instance
server = Server("example-server")

@server.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

async def main():
    async with stdio_server(server) as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            server.create_initialization_options()
        )

if __name__ == "__main__":
    asyncio.run(main())
```

Yukarıdaki kodda:

- MCP SDK kullanarak bir sunucu örneği oluşturuyoruz.
- Dekoratörler kullanarak araçlar tanımlıyoruz.
- Taşıma işlemini yönetmek için stdio_server bağlam yöneticisini kullanıyoruz.

### .NET

```csharp
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;
using Microsoft.Extensions.Logging;
using ModelContextProtocol.Server;

var builder = Host.CreateApplicationBuilder(args);

builder.Services
    .AddMcpServer()
    .WithStdioTransport()
    .WithTools<Tools>();

builder.Services.AddLogging(logging => logging.AddConsole());

var app = builder.Build();
await app.RunAsync();
```

SSE'den temel farklar şunlardır:

- Web sunucusu kurulumu veya HTTP uç noktaları gerektirmez.
- İstemci tarafından alt işlem olarak başlatılır.
- stdin/stdout akışları aracılığıyla iletişim kurar.
- Uygulaması ve hata ayıklaması daha basittir.

## Egzersiz: Bir stdio Sunucusu Oluşturma

Sunucumuzu oluşturmak için iki şeyi akılda tutmamız gerekiyor:

- Bağlantı ve mesajlar için uç noktalar sunmak üzere bir web sunucusu kullanmamız gerekiyor.

## Laboratuvar: Basit bir MCP stdio sunucusu oluşturma

Bu laboratuvarda, önerilen stdio taşıma yöntemini kullanarak basit bir MCP sunucusu oluşturacağız. Bu sunucu, istemcilerin standart Model Context Protocol kullanarak çağırabileceği araçlar sunacak.

### Ön Koşullar

- Python 3.8 veya üstü
- MCP Python SDK: `pip install mcp`
- Temel async programlama bilgisi

İlk MCP stdio sunucumuzu oluşturmaya başlayalım:

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp import types

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Create the server
server = Server("example-stdio-server")

@server.tool()
def calculate_sum(a: int, b: int) -> int:
    """Calculate the sum of two numbers"""
    return a + b

@server.tool() 
def get_greeting(name: str) -> str:
    """Generate a personalized greeting"""
    return f"Hello, {name}! Welcome to MCP stdio server."

async def main():
    # Use stdio transport
    async with stdio_server(server) as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            server.create_initialization_options()
        )

if __name__ == "__main__":
    asyncio.run(main())
```

## Kullanımdan kaldırılan SSE yaklaşımından temel farklar

**Stdio Taşıma (Mevcut Standart):**
- Basit alt işlem modeli - istemci sunucuyu alt işlem olarak başlatır.
- JSON-RPC mesajları kullanarak stdin/stdout üzerinden iletişim.
- HTTP sunucu kurulumu gerektirmez.
- Daha iyi performans ve güvenlik.
- Daha kolay hata ayıklama ve geliştirme.

**SSE Taşıma (MCP 2025-06-18 itibarıyla kullanımdan kaldırıldı):**
- SSE uç noktaları olan HTTP sunucusu gerektiriyordu.
- Web sunucusu altyapısı ile daha karmaşık kurulum.
- HTTP uç noktaları için ek güvenlik hususları.
- Web tabanlı senaryolar için Akışlı HTTP ile değiştirildi.

### Stdio taşıma ile bir sunucu oluşturma

Stdio sunucumuzu oluşturmak için şunları yapmamız gerekiyor:

1. **Gerekli kütüphaneleri içe aktarın** - MCP sunucu bileşenlerini ve stdio taşımayı içe aktarmamız gerekiyor.
2. **Bir sunucu örneği oluşturun** - Sunucuyu yetenekleriyle tanımlayın.
3. **Araçlar tanımlayın** - Sunmak istediğimiz işlevselliği ekleyin.
4. **Taşımayı ayarlayın** - Stdio iletişimini yapılandırın.
5. **Sunucuyu çalıştırın** - Sunucuyu başlatın ve mesajları yönetin.

Adım adım oluşturalım:

### Adım 1: Temel bir stdio sunucu oluşturma

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Create the server
server = Server("example-stdio-server")

@server.tool()
def get_greeting(name: str) -> str:
    """Generate a personalized greeting"""
    return f"Hello, {name}! Welcome to MCP stdio server."

async def main():
    async with stdio_server(server) as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            server.create_initialization_options()
        )

if __name__ == "__main__":
    asyncio.run(main())
```

### Adım 2: Daha fazla araç ekleme

```python
@server.tool()
def calculate_sum(a: int, b: int) -> int:
    """Calculate the sum of two numbers"""
    return a + b

@server.tool()
def calculate_product(a: int, b: int) -> int:
    """Calculate the product of two numbers"""
    return a * b

@server.tool()
def get_server_info() -> dict:
    """Get information about this MCP server"""
    return {
        "server_name": "example-stdio-server",
        "version": "1.0.0",
        "transport": "stdio",
        "capabilities": ["tools"]
    }
```

### Adım 3: Sunucuyu çalıştırma

Kodunuzu `server.py` olarak kaydedin ve komut satırından çalıştırın:

```bash
python server.py
```

Sunucu başlayacak ve stdin'den giriş bekleyecek. JSON-RPC mesajlarını stdio taşıma üzerinden iletişim kurarak kullanır.

### Adım 4: Inspector ile test etme

Sunucunuzu MCP Inspector kullanarak test edebilirsiniz:

1. Inspector'ı yükleyin: `npx @modelcontextprotocol/inspector`
2. Inspector'ı çalıştırın ve sunucunuza yönlendirin.
3. Oluşturduğunuz araçları test edin.

### .NET

```csharp
var builder = WebApplication.CreateBuilder(args);
builder.Services
    .AddMcpServer();
 ```

## Stdio sunucunuzu hata ayıklama

### MCP Inspector kullanımı

MCP Inspector, MCP sunucularını hata ayıklamak ve test etmek için değerli bir araçtır. İşte stdio sunucunuzla nasıl kullanılacağı:

1. **Inspector'ı yükleyin**:
   ```bash
   npx @modelcontextprotocol/inspector
   ```

2. **Inspector'ı çalıştırın**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

3. **Sunucunuzu test edin**: Inspector, web arayüzü sağlar ve burada:
   - Sunucu yeteneklerini görüntüleyebilirsiniz.
   - Farklı parametrelerle araçları test edebilirsiniz.
   - JSON-RPC mesajlarını izleyebilirsiniz.
   - Bağlantı sorunlarını hata ayıklayabilirsiniz.

### VS Code kullanımı

MCP sunucunuzu doğrudan VS Code'da da hata ayıklayabilirsiniz:

1. `.vscode/launch.json` içinde bir başlatma yapılandırması oluşturun:
   ```json
   {
     "version": "0.2.0",
     "configurations": [
       {
         "name": "Debug MCP Server",
         "type": "python",
         "request": "launch",
         "program": "server.py",
         "console": "integratedTerminal"
       }
     ]
   }
   ```

2. Sunucu kodunuzda kesme noktaları ayarlayın.
3. Hata ayıklayıcıyı çalıştırın ve Inspector ile test edin.

### Yaygın hata ayıklama ipuçları

- Günlükleme için `stderr` kullanın - `stdout`'a yazmayın çünkü MCP mesajları için ayrılmıştır.
- Tüm JSON-RPC mesajlarının yeni satırlarla ayrıldığından emin olun.
- Önce basit araçlarla test yapın, ardından karmaşık işlevsellik ekleyin.
- Mesaj formatlarını doğrulamak için Inspector'ı kullanın.

## Stdio sunucunuzu VS Code'da tüketme

Stdio sunucunuzu oluşturduktan sonra, Claude veya diğer MCP uyumlu istemcilerle kullanmak için VS Code ile entegre edebilirsiniz.

### Yapılandırma

1. **Bir MCP yapılandırma dosyası oluşturun** `%APPDATA%\Claude\claude_desktop_config.json` (Windows) veya `~/Library/Application Support/Claude/claude_desktop_config.json` (Mac):

   ```json
   {
     "mcpServers": {
       "example-stdio-server": {
         "command": "python",
         "args": ["path/to/your/server.py"]
       }
     }
   }
   ```

2. **Claude'u yeniden başlatın**: Yeni sunucu yapılandırmasını yüklemek için Claude'u kapatıp yeniden açın.

3. **Bağlantıyı test edin**: Claude ile bir konuşma başlatın ve sunucunuzun araçlarını deneyin:
   - "Beni selamlama aracıyla selamlayabilir misin?"
   - "15 ve 27'nin toplamını hesapla."
   - "Sunucu bilgisi nedir?"

### TypeScript stdio sunucu örneği

Referans için eksiksiz bir TypeScript örneği:

```typescript
#!/usr/bin/env node
import { Server } from "@modelcontextprotocol/sdk/server/index.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { CallToolRequestSchema, ListToolsRequestSchema } from "@modelcontextprotocol/sdk/types.js";

const server = new Server(
  {
    name: "example-stdio-server",
    version: "1.0.0",
  },
  {
    capabilities: {
      tools: {},
    },
  }
);

// Add tools
server.setRequestHandler(ListToolsRequestSchema, async () => {
  return {
    tools: [
      {
        name: "get_greeting",
        description: "Get a personalized greeting",
        inputSchema: {
          type: "object",
          properties: {
            name: {
              type: "string",
              description: "Name of the person to greet",
            },
          },
          required: ["name"],
        },
      },
    ],
  };
});

server.setRequestHandler(CallToolRequestSchema, async (request) => {
  if (request.params.name === "get_greeting") {
    return {
      content: [
        {
          type: "text",
          text: `Hello, ${request.params.arguments?.name}! Welcome to MCP stdio server.`,
        },
      ],
    };
  } else {
    throw new Error(`Unknown tool: ${request.params.name}`);
  }
});

async function runServer() {
  const transport = new StdioServerTransport();
  await server.connect(transport);
}

runServer().catch(console.error);
```

### .NET stdio sunucu örneği

```csharp
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;
using Microsoft.Extensions.Logging;
using ModelContextProtocol.Server;
using System.ComponentModel;

var builder = Host.CreateApplicationBuilder(args);

builder.Services
    .AddMcpServer()
    .WithStdioTransport()
    .WithTools<Tools>();

var app = builder.Build();
await app.RunAsync();

public class Tools
{
    [Description("Get a personalized greeting")]
    public string GetGreeting(string name)
    {
        return $"Hello, {name}! Welcome to MCP stdio server.";
    }

    [Description("Calculate the sum of two numbers")]
    public int CalculateSum(int a, int b)
    {
        return a + b;
    }
}
```

## Özet

Bu güncellenmiş derste şunları öğrendiniz:

- Mevcut **stdio taşıma** (önerilen yaklaşım) kullanarak MCP sunucuları oluşturmak.
- SSE taşımanın neden stdio ve Akışlı HTTP lehine kullanımdan kaldırıldığını anlamak.
- MCP istemcileri tarafından çağrılabilecek araçlar oluşturmak.
- MCP Inspector kullanarak sunucunuzu hata ayıklamak.
- Stdio sunucunuzu VS Code ve Claude ile entegre etmek.

Stdio taşıma, kullanımdan kaldırılan SSE yaklaşımına kıyasla MCP sunucuları oluşturmak için daha basit, daha güvenli ve daha performanslı bir yol sağlar. 2025-06-18 spesifikasyonuna göre çoğu MCP sunucu uygulaması için önerilen taşıma yöntemidir.

### .NET

1. Önce bazı araçlar oluşturalım, bunun için *Tools.cs* adlı bir dosya oluşturacağız ve aşağıdaki içeriği ekleyeceğiz:

  ```csharp
  using System.ComponentModel;
  using System.Text.Json;
  using ModelContextProtocol.Server;
  ```

## Egzersiz: Stdio sunucunuzu test etme

Artık stdio sunucunuzu oluşturduğunuza göre, doğru çalıştığından emin olmak için test edelim.

### Ön Koşullar

1. MCP Inspector'ın yüklü olduğundan emin olun:
   ```bash
   npm install -g @modelcontextprotocol/inspector
   ```

2. Sunucu kodunuz kaydedilmiş olmalı (örneğin, `server.py` olarak).

### Inspector ile test etme

1. **Sunucunuzla Inspector'ı başlatın**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

2. **Web arayüzünü açın**: Inspector, sunucunuzun yeteneklerini gösteren bir tarayıcı penceresi açacaktır.

3. **Araçları test edin**: 
   - Farklı isimlerle `get_greeting` aracını deneyin.
   - Çeşitli sayılarla `calculate_sum` aracını test edin.
   - Sunucu meta verilerini görmek için `get_server_info` aracını çağırın.

4. **İletişimi izleyin**: Inspector, istemci ve sunucu arasında değiş tokuş edilen JSON-RPC mesajlarını gösterir.

### Görmeniz gerekenler

Sunucunuz doğru şekilde başlatıldığında şunları görmelisiniz:
- Inspector'da listelenen sunucu yetenekleri.
- Test edilebilecek araçlar.
- Başarılı JSON-RPC mesaj alışverişleri.
- Araç yanıtlarının arayüzde görüntülenmesi.

### Yaygın sorunlar ve çözümler

**Sunucu başlamıyor:**
- Tüm bağımlılıkların yüklü olduğundan emin olun: `pip install mcp`
- Python sözdizimini ve girintiyi doğrulayın.
- Konsoldaki hata mesajlarını kontrol edin.

**Araçlar görünmüyor:**
- `@server.tool()` dekoratörlerinin mevcut olduğundan emin olun.
- Araç işlevlerinin `main()`'den önce tanımlandığını kontrol edin.
- Sunucunun doğru şekilde yapılandırıldığını doğrulayın.

**Bağlantı sorunları:**
- Sunucunun stdio taşımayı doğru şekilde kullandığından emin olun.
- Başka işlemlerin müdahale etmediğinden emin olun.
- Inspector komut sözdizimini doğrulayın.

## Ödev

Sunucunuzu daha fazla yetenekle geliştirmeyi deneyin. Örneğin, [bu sayfayı](https://api.chucknorris.io/) kullanarak bir API çağıran bir araç ekleyin. Sunucunun nasıl görüneceğine siz karar verin. İyi eğlenceler :)

## Çözüm

[Çözüm](./solution/README.md) Çalışan kodla olası bir çözüm burada.

## Temel Çıkarımlar

Bu bölümden çıkarılacak temel noktalar şunlardır:

- Stdio taşıma, yerel MCP sunucuları için önerilen mekanizmadır.
- Stdio taşıma, MCP sunucuları ve istemcileri arasında standart giriş ve çıkış akışlarını kullanarak sorunsuz iletişim sağlar.
- Stdio sunucularını doğrudan Inspector ve Visual Studio Code ile kullanabilirsiniz, bu da hata ayıklamayı ve entegrasyonu kolaylaştırır.

## Örnekler 

- [Java Hesap Makinesi](../samples/java/calculator/README.md)
- [.Net Hesap Makinesi](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Hesap Makinesi](../samples/javascript/README.md)
- [TypeScript Hesap Makinesi](../samples/typescript/README.md)
- [Python Hesap Makinesi](../../../../03-GettingStarted/samples/python) 

## Ek Kaynaklar

- [SSE](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events)

## Sırada Ne Var

## Sonraki Adımlar

Artık stdio taşıma ile MCP sunucuları oluşturmayı öğrendiğinize göre, daha ileri konuları keşfedebilirsiniz:

- **Sonraki**: [MCP ile HTTP Akışı (Akışlı HTTP)](../06-http-streaming/README.md) - Uzak sunucular için desteklenen diğer taşıma mekanizmasını öğrenin.
- **İleri Düzey**: [MCP Güvenlik En İyi Uygulamaları](../../02-Security/README.md) - MCP sunucularınızda güvenlik uygulayın.
- **Üretim**: [Dağıtım Stratejileri](../09-deployment/README.md) - Sunucularınızı üretim kullanımı için dağıtın.

## Ek Kaynaklar

- [MCP Spesifikasyonu 2025-06-18](https://spec.modelcontextprotocol.io/specification/) - Resmi spesifikasyon.
- [MCP SDK Belgeleri](https://github.com/modelcontextprotocol/sdk) - Tüm diller için SDK referansları.
- [Topluluk Örnekleri](../../06-CommunityContributions/README.md) - Topluluktan daha fazla sunucu örneği.

---

**Feragatname**:  
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hata veya yanlışlık içerebileceğini lütfen unutmayın. Belgenin orijinal dili, yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımından kaynaklanan yanlış anlamalar veya yanlış yorumlamalar için sorumluluk kabul edilmez.