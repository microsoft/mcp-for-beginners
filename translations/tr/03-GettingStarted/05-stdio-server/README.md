# stdio Taşıma Yöntemi ile MCP Sunucusu

> **⚠️ Önemli Güncelleme**: MCP Spesifikasyonu 2025-06-18 itibarıyla, bağımsız SSE (Server-Sent Events) taşıma yöntemi **kaldırılmış** ve yerini "Streamable HTTP" taşıma yöntemine bırakmıştır. Güncel MCP spesifikasyonu iki temel taşıma mekanizması tanımlar:
> 1. **stdio** - Standart giriş/çıkış (yerel sunucular için önerilir)
> 2. **Streamable HTTP** - Dahili olarak SSE kullanabilen uzak sunucular için
>
> Bu ders, çoğu MCP sunucu uygulaması için önerilen **stdio taşıma yöntemi**ne odaklanacak şekilde güncellenmiştir.

Stdio taşıma yöntemi, MCP sunucularının standart giriş ve çıkış akışları aracılığıyla istemcilerle iletişim kurmasını sağlar. Bu, mevcut MCP spesifikasyonunda en çok kullanılan ve önerilen taşıma mekanizmasıdır; basit ve verimli bir yol sunar, böylece çeşitli istemci uygulamalarla kolayca entegre olabilen MCP sunucuları inşa edebilirsiniz.

## Genel Bakış

Bu derste, stdio taşıma yöntemini kullanarak MCP Sunucuları nasıl oluşturulur ve tüketilir, bunun üzerine durulacaktır.

## Öğrenme Hedefleri

Bu dersin sonunda şunları yapabileceksiniz:

- Stdio taşıma yöntemi kullanarak bir MCP Sunucusu oluşturmak.
- MCP Sunucusunu Inspector ile hata ayıklamak.
- MCP Sunucusunu Visual Studio Code kullanarak tüketmek.
- Mevcut MCP taşıma mekanizmalarını ve neden stdio'nun önerildiğini anlamak.

## stdio Taşıma Yöntemi - Nasıl Çalışır?

Stdio taşıma yöntemi, mevcut MCP spesifikasyonunda (2025-06-18) desteklenen iki taşıma tipinden biridir. İşte nasıl çalışır:

- **Basit İletişim**: Sunucu standart girişten (`stdin`) JSON-RPC mesajlarını okur ve standart çıkışa (`stdout`) mesajlar gönderir.
- **İşlem Tabanlı**: İstemci, MCP sunucusunu alt süreç olarak başlatır.
- **Mesaj Formatı**: Mesajlar, yeni satır karakterleri ile ayrılmış tekil JSON-RPC istekleri, bildirimleri veya yanıtlarıdır.
- **Kayıt Tutma**: Sunucu, kayıt amacıyla UTF-8 dizelerini standart hata çıkışına (`stderr`) yazabilir.

### Temel Gereksinimler:
- Mesajlar yeni satırlarla ayrılmalı ve gömülü yeni satır karakterleri içermemelidir.
- Sunucu, `stdout`'a geçerli olmayan herhangi bir MCP mesajı yazmamalıdır.
- İstemci, sunucunun `stdin`'ine geçerli olmayan herhangi bir MCP mesajı yazmamalıdır.

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

Önceki kodda:

- MCP SDK'dan `Server` sınıfı ve `StdioServerTransport` ithal edilmiştir.
- Basit yapılandırma ve yeteneklerle bir sunucu örneği oluşturulmuştur.

### Python

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server

# Sunucu örneği oluşturun
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

Önceki kodda:

- MCP SDK kullanılarak bir sunucu örneği oluşturulmuştur.
- Dekoratörlerle araçlar tanımlanmıştır.
- Taşıma işlemi için stdio_server bağlam yöneticisi kullanılmıştır.

### .NET

```csharp
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;
using Microsoft.Extensions.Logging;
using ModelContextProtocol.Server;

var builder = Host.CreateApplicationBuilder(args);

builder.Services
    .AddMcpServer()
    .WithStdioServerTransport()
    .WithTools<Tools>();

builder.Services.AddLogging(logging => logging.AddConsole());

var app = builder.Build();
await app.RunAsync();
```

SSE'den farkı olarak stdio sunucuları:

- Web sunucusu kurulumu veya HTTP uç noktaları gerektirmez.
- İstemci tarafından alt süreç olarak başlatılır.
- stdin/stdout akışları üzerinden iletişim kurar.
- Daha basit uygulanır ve hata ayıklanması kolaydır.

## Alıştırma: Bir stdio Sunucusu Oluşturma

Sunucumuzu oluştururken iki önemli noktayı göz önünde bulundurmamız gerekiyor:

- Bağlantı ve mesajlar için uç noktaları açmak amacıyla bir web sunucusu kullanmamız gerekebilir.

## Laboratuvar: Basit Bir MCP stdio Sunucusu Oluşturma

Bu laboratuvarda, önerilen stdio taşıma yöntemini kullanarak basit bir MCP sunucusu oluşturacağız. Bu sunucu, istemcilerin standart Model Context Protocol kullanarak çağırabileceği araçlar sunacak.

### Önkoşullar

- Python 3.8 veya üzeri
- MCP Python SDK: `pip install mcp`
- Asenkron programlama konusunda temel bilgi

İlk MCP stdio sunucumuzu oluşturarak başlayalım:

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp import types

# Günlüklemeyi yapılandır
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Sunucuyu oluştur
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
    # stdio taşımasını kullan
    async with stdio_server(server) as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            server.create_initialization_options()
        )

if __name__ == "__main__":
    asyncio.run(main())
```

## Kaldırılan SSE yaklaşımından temel farklar

**Stdio Taşıma (Güncel Standart):**
- Basit alt süreç modeli - istemci sunucuyu çocuk süreç olarak başlatır
- JSON-RPC mesajları ile stdin/stdout üzerinden iletişim
- HTTP sunucusu kurulumu gerekli değildir
- Daha iyi performans ve güvenlik
- Daha kolay hata ayıklama ve geliştirme

**SSE Taşıma (MCP 2025-06-18 itibarıyla kaldırılmış):**
- SSE uç noktalarına sahip HTTP sunucusu gerekliydi
- Web sunucusu altyapısıyla daha karmaşık kurulum
- HTTP uç noktaları için ek güvenlik hususları
- Şimdi web tabanlı senaryolar için Streamable HTTP ile değiştirildi

### stdio taşıma yöntemi ile sunucu oluşturma

stdio sunucumuzu oluşturmak için:

1. **Gerekli kütüphaneleri içe aktarın** - MCP sunucu bileşenleri ve stdio taşıma yöntemi gerekir
2. **Sunucu örneği oluşturun** - Sunucuyu yetenekleri ile tanımlayın
3. **Araçlar tanımlayın** - Açıklamak istediğiniz fonksiyonları ekleyin
4. **Taşımayı yapılandırın** - stdio iletişimini ayarlayın
5. **Sunucuyu çalıştırın** - Başlatın ve mesajları yönetin

Adım adım ilerleyelim:

### Adım 1: Temel bir stdio sunucusu oluşturma

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server

# Günlük kaydını yapılandır
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Sunucuyu oluştur
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

Kodu `server.py` olarak kaydedin ve komut satırından çalıştırın:

```bash
python server.py
```

Sunucu başlayacak ve stdin'den gelen girişleri bekleyecektir. stdio taşıma yöntemiyle JSON-RPC mesajları üzerinden iletişim kurar.

### Adım 4: Inspector ile test

Sunucunuzu MCP Inspector ile test edebilirsiniz:

1. Inspector'ı yükleyin: `npx @modelcontextprotocol/inspector`
2. Inspector'ı başlatın ve sunucunuza yönlendirin
3. Oluşturduğunuz araçları test edin

### .NET

```csharp
var builder = WebApplication.CreateBuilder(args);
builder.Services
    .AddMcpServer();
 ```

## stdio sunucunuzu hata ayıklama

### MCP Inspector Kullanımı

MCP Inspector, MCP sunucularını hata ayıklamak ve test etmek için değerli bir araçtır. İşte bunu stdio sunucunuzla nasıl kullanacağınız:

1. **Inspector’ı kurun**:
   ```bash
   npx @modelcontextprotocol/inspector
   ```

2. **Inspector’ı çalıştırın**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

3. **Sunucunuzu test edin**: Inspector, şu özellikleri sağlayan bir web arayüzü sunar:
   - Sunucu yeteneklerini görüntüleme
   - Farklı parametrelerle araçları test etme
   - JSON-RPC mesajlarını izleme
   - Bağlantı sorunlarını hata ayıklama

### VS Code Kullanımı

MCP sunucunuzu doğrudan VS Code içinde de hata ayıklayabilirsiniz:

1. `.vscode/launch.json` içinde bir çalıştırma yapılandırması oluşturun:
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

2. Sunucu kodunuza kesme noktaları koyun
3. Hata ayıklayıcıyı başlatın ve Inspector ile test edin

### Yaygın hata ayıklama ipuçları

- Kayıt için `stderr` kullanın - kesinlikle `stdout`’a yazmayın çünkü MCP mesajlarına ayrılmıştır
- Tüm JSON-RPC mesajlarının yeni satır karakteri ile ayrıldığından emin olun
- Öncelikle basit araçlarla test yapın, karmaşık fonksiyonlar eklemeden önce
- Mesaj formatlarını doğrulamak için Inspector’ı kullanın

## stdio sunucunuzu VS Code'da kullanma

MCP stdio sunucunuzu oluşturduktan sonra, bunu VS Code ile entegre ederek Claude veya diğer MCP uyumlu istemcilerle kullanabilirsiniz.

### Yapılandırma

1. `%APPDATA%\Claude\claude_desktop_config.json` (Windows) veya `~/Library/Application Support/Claude/claude_desktop_config.json` (Mac) yolunda bir MCP yapılandırma dosyası oluşturun:

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

2. **Claude’u yeniden başlatın**: Yeni sunucu yapılandırmasını yüklemek için Claude’u kapatıp açın.

3. **Bağlantıyı test edin**: Claude ile bir konuşma başlatıp sunucu araçlarınızı deneyin:
   - "Karşılama aracını kullanarak bana merhaba diyebilir misin?"
   - "15 ve 27'nin toplamını hesapla"
   - "Sunucu bilgilerini alabilir miyim?"

### TypeScript stdio sunucu örneği

Referans için tam bir TypeScript örneği:

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

// Araçlar ekle
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
    .WithStdioServerTransport()
    .WithTools<Tools>();

var app = builder.Build();
await app.RunAsync();

[McpServerToolType]
public class Tools
{
    [McpServerTool, Description("Get a personalized greeting")]
    public string GetGreeting(string name)
    {
        return $"Hello, {name}! Welcome to MCP stdio server.";
    }

    [McpServerTool, Description("Calculate the sum of two numbers")]
    public int CalculateSum(int a, int b)
    {
        return a + b;
    }
}
```

## Özet

Bu güncellenmiş derste şunları öğrendiniz:

- Mevcut **stdio taşıma yöntemi** ile MCP sunucuları oluşturmayı (önerilen yol)
- SSE taşıma yönteminin neden stdio ve Streamable HTTP lehine kaldırıldığını
- MCP istemcileri tarafından çağrılabilecek araçlar oluşturmayı
- MCP Inspector kullanarak sunucunuzu hata ayıklamayı
- Stdio sunucunuzu VS Code ve Claude ile entegre etmeyi

stdio taşıma, kaldırılan SSE yaklaşımına kıyasla MCP sunucuları oluşturmak için daha basit, daha güvenilir ve daha performanslı bir yol sunar. 2025-06-18 spesifikasyonundan itibaren çoğu MCP sunucu uygulaması için önerilen taşıma yöntemidir.


### .NET

1. Öncelikle bazı araçlar oluşturalım, bunun için aşağıdaki içeriğe sahip *Tools.cs* dosyasını oluşturacağız:

  ```csharp
  using System.ComponentModel;
  using System.Text.Json;
  using ModelContextProtocol.Server;
  ```

## Alıştırma: stdio sunucunuzu test etme

Stdio sunucunuzu oluşturduğunuz için şimdi düzgün çalıştığından emin olmak için test edelim.

### Önkoşullar

1. MCP Inspector’ın kurulu olduğundan emin olun:
   ```bash
   npm install -g @modelcontextprotocol/inspector
   ```

2. Sunucu kodunuzun kaydedildiğinden emin olun (örneğin, `server.py` olarak)

### Inspector ile test

1. **Sunucunuzla birlikte Inspector’ı başlatın**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

2. **Web arayüzünü açın**: Inspector, sunucunuzun yeteneklerini gösteren bir tarayıcı penceresi açar.

3. **Araçları test edin**:
   - Farklı isimlerle `get_greeting` aracını deneyin
   - Çeşitli sayılarla `calculate_sum` aracını test edin
   - `get_server_info` aracıyla sunucu meta verilerini çağırın

4. **İletişimi izleyin**: Inspector, istemci ve sunucu arasında değiş tokuş edilen JSON-RPC mesajlarını gösterir.

### Görmeniz gerekenler

Sunucunuz doğru başlarsa şunları görmelisiniz:
- Inspector’da listelenen sunucu yetenekleri
- Test için mevcut araçlar
- Başarılı JSON-RPC mesaj alışverişleri
- Arayüzde gösterilen araç yanıtları

### Yaygın sorunlar ve çözümleri

**Sunucu başlamıyor:**
- Tüm bağımlılıkların yüklü olduğunu doğrulayın: `pip install mcp`
- Python sözdizimi ve girintilerini kontrol edin
- Konsoldaki hata mesajlarına bakın

**Araçlar görünmüyor:**
- `@server.tool()` dekoratörlerinin varlığını kontrol edin
- Araç fonksiyonlarının `main()` öncesi tanımlandığından emin olun
- Sunucunun doğru yapılandırıldığını doğrulayın

**Bağlantı sorunları:**
- Sunucunun stdio taşıma kullanıyor olduğundan emin olun
- Başka süreçlerin müdahale etmediğini kontrol edin
- Inspector komut sözdizimini doğrulayın

## Ödev

Sunucunuzu daha fazla yetenekle geliştirmeyi deneyin. Örneğin, [bu sayfayı](https://api.chucknorris.io/) kullanarak bir API çağıran araç ekleyebilirsiniz. Sunucunuzun nasıl görüneceğine siz karar verin. İyi eğlenceler :)
## Çözüm

[Çözüm](./solution/README.md) İşleyen kodla olası bir çözüm burada.

## Anahtar Noktalar

Bu bölümün anahtar noktaları şunlardır:

- Stdio taşıma, yerel MCP sunucuları için önerilen mekanizmadır.
- Stdio taşıma, MCP sunucuları ile istemciler arasında standart giriş ve çıkış akışlarını kullanarak kesintisiz iletişim sağlar.
- Hem Inspector hem de Visual Studio Code kullanarak stdio sunucular doğrudan tüketilebilir; böylece hata ayıklama ve entegrasyon kolaylaşır.

## Örnekler

- [Java Hesap Makinesi](../samples/java/calculator/README.md)
- [.Net Hesap Makinesi](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Hesap Makinesi](../samples/javascript/README.md)
- [TypeScript Hesap Makinesi](../samples/typescript/README.md)
- [Python Hesap Makinesi](../../../../03-GettingStarted/samples/python) 

## Ek Kaynaklar

- [SSE](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events)

## Sonraki Konular

## Sonraki Adımlar

stdio taşıma yöntemi ile MCP sunucuları nasıl oluşturulacağını öğrendiğinize göre, daha gelişmiş konuları keşfedebilirsiniz:

- **Sonraki:** [MCP ile HTTP Akışı (Streamable HTTP)](../06-http-streaming/README.md) - Uzak sunucular için desteklenen diğer taşıma mekanizmasını öğrenin
- **İleri Düzey:** [MCP Güvenlik En İyi Uygulamaları](../../02-Security/README.md) - MCP sunucularınızda güvenlik uygulayın
- **Üretim:** [Dağıtım Stratejileri](../09-deployment/README.md) - Sunucularınızı üretim amaçlı dağıtın

## Ek Kaynaklar

- [MCP Spesifikasyonu 2025-06-18](https://spec.modelcontextprotocol.io/specification/) - Resmi spesifikasyon
- [MCP SDK Dokümantasyonu](https://github.com/modelcontextprotocol/sdk) - Tüm diller için SDK referansları
- [Topluluk Örnekleri](../../06-CommunityContributions/README.md) - Topluluktan daha fazla sunucu örnekleri

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Feragatname**:  
Bu belge, yapay zeka çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba gösterilse de, otomatik çevirilerin hatalar veya yanlışlıklar içerebileceğini lütfen unutmayınız. Orijinal belge, kendi ana dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımıyla ortaya çıkabilecek herhangi bir yanlış anlama veya yorum hatasından sorumlu değiliz.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->