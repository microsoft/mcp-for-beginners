# stdio Taşıma ile MCP Sunucusu

> **⚠️ Önemli Güncelleme**: MCP Spesifikasyonu 2025-06-18 itibarıyla, bağımsız SSE (Server-Sent Events) taşıma yöntemi **kullanımdan kaldırılmış** ve "Streamable HTTP" taşıma yöntemi ile değiştirilmiştir. Mevcut MCP spesifikasyonu iki ana taşıma mekanizmasını tanımlar:
> 1. **stdio** - Standart giriş/çıkış (yerel sunucular için önerilen)
> 2. **Streamable HTTP** - Dahili olarak SSE kullanabilen uzak sunucular için
>
> Bu ders, çoğu MCP sunucu uygulaması için önerilen yöntem olan **stdio taşıma** üzerine güncellenmiştir.

Stdio taşıma, MCP sunucularının istemcilerle standart giriş ve çıkış akışları üzerinden iletişim kurmasını sağlar. Bu, mevcut MCP spesifikasyonunda en yaygın kullanılan ve önerilen taşıma mekanizmasıdır. Farklı istemci uygulamalarıyla kolayca entegre edilebilen, basit ve verimli bir MCP sunucusu oluşturma yoludur.

## Genel Bakış

Bu ders, stdio taşıma kullanarak MCP Sunucularının nasıl oluşturulacağını ve tüketileceğini kapsar.

## Öğrenme Hedefleri

Bu dersin sonunda şunları yapabileceksiniz:

- stdio taşıma kullanarak MCP Sunucusu oluşturmak.
- MCP Sunucusunu Inspector ile hata ayıklamak.
- Visual Studio Code kullanarak MCP Sunucusunu tüketmek.
- Mevcut MCP taşıma mekanizmalarını anlamak ve neden stdio'nun önerildiğini kavramak.


## stdio Taşıma - Nasıl Çalışır

Stdio taşıma, MCP Spesifikasyonu
`2026-07-28`'de belirtilen iki standart taşıma yönteminden biridir. İşte nasıl çalışır:

- **Basit İletişim**: Sunucu, standart girişten (`stdin`) JSON-RPC mesajlarını okur ve standart çıkışa (`stdout`) mesaj gönderir.
- **İşlem Tabanlı**: İstemci, MCP sunucusunu bir alt süreç olarak başlatır.
- **Mesaj Formatı**: Mesajlar, yeni satır ile ayrılmış tekil JSON-RPC istekleri, bildirimler veya yanıtlar şeklindedir.
- **Kayıt Tutma**: Sunucu, kayıt amacıyla standart hata çıkışına (`stderr`) UTF-8 dizeleri yazabilir.

### Ana Gereksinimler:
- Mesajlar yeni satır ile ayrılmalı ve gömülü yeni satır içeremez.
- Sunucu, geçerli bir MCP mesajı olmayan hiçbir şeyi `stdout`'a yazmamalıdır.
- İstemci, geçerli bir MCP mesajı olmayan hiçbir şeyi sunucunun `stdin`'ine yazmamalıdır.

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

async function runServer() {
  const transport = new StdioServerTransport();
  await server.connect(transport);
}

runServer().catch(console.error);
```

Önceki kodda:

- MCP SDK'dan `Server` sınıfı ve `StdioServerTransport`'u içe aktarıyoruz
- Temel yapılandırma ve özelliklerle bir sunucu örneği oluşturuyoruz
- `StdioServerTransport` örneği yaratıp sunucuyu ona bağlıyoruz, böylece stdin/stdout üzerinden iletişim sağlanıyor

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

- MCP SDK kullanarak sunucu örneği oluşturuyoruz
- Dekoratörlerle araçlar tanımlıyoruz
- Taşıma işlemi için stdio_server bağlam yöneticisini kullanıyoruz

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

SSE'den temel farkları şunlardır:

- Web sunucusu kurulumu veya HTTP uç noktaları gerektirmez
- İstemci tarafından alt süreç olarak başlatılır
- stdin/stdout akışları üzerinden iletişim kurar
- Uygulaması ve hata ayıklaması daha basittir

## Egzersiz: stdio Sunucu Oluşturma

Sunucumuzu oluştururken iki şeyi akılda tutmalıyız:

- Bağlantı ve mesajlar için uç noktaları açacak bir web sunucusu kullanmalıyız.
## Laboratuvar: Basit bir MCP stdio sunucu oluşturma

Bu laboratuvarda, önerilen stdio taşıma kullanarak basit bir MCP sunucu oluşturacağız. Bu sunucu, istemcilerin standart Model Context Protocol ile çağırabileceği araçları sunacak.

### Gereksinimler

- Python 3.8 veya üstü
- MCP Python SDK: `pip install mcp`
- Asenkron programlama hakkında temel bilgi

İlk MCP stdio sunucumuzu oluşturarak başlayalım:

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp import types

# Günlük kaydını yapılandır
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

## Kullanımdan kaldırılan SSE yönteminden temel farklar

**Stdio Taşıma (Mevcut Standart):**
- Basit alt süreç modeli - istemci sunucuyu çocuk süreç olarak başlatır
- JSON-RPC mesajları kullanarak stdin/stdout üzerinden iletişim
- HTTP sunucusu kurulumu gerektirmez
- Daha iyi performans ve güvenlik
- Hata ayıklama ve geliştirme kolaylığı

**SSE Taşıma (MCP 2025-06-18 ile Kullanımdan Kaldırıldı):**
- SSE uç noktalarıyla HTTP sunucusu gerekliydi
- Web sunucusu altyapısıyla daha karmaşık kurulum
- HTTP uç noktaları için ek güvenlik önlemleri
- Artık web tabanlı senaryolar için Streamable HTTP ile değiştirilmiştir

### stdio taşıma kullanarak sunucu oluşturma

stdio sunucumuzu oluşturmak için:

1. **Gerekli kütüphaneleri içe aktarın** - MCP sunucu bileşenleri ve stdio taşıma gereklidir
2. **Sunucu örneği oluşturun** - Sunucuyu özellikleri ile tanımlayın
3. **Araçları tanımlayın** - Sunmak istediğimiz işlevselliği ekleyin
4. **Taşımayı yapılandırın** - stdio iletişim ayarlarını yapın
5. **Sunucuyu çalıştırın** - Sunucuyu başlatın ve mesajları yönetin

Adım adım inşa edelim:

### Adım 1: Temel bir stdio sunucusu oluşturma

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server

# Günlüğü yapılandır
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

Kodu `server.py` olarak kaydedip komut satırından çalıştırın:

```bash
python server.py
```

Sunucu başlar ve stdin'den girdi bekler. Mesajlaşma stdio taşıma üzerinden JSON-RPC mesajlarıyla yapılır.

### Adım 4: Inspector ile test etme

Sunucunuzu MCP Inspector ile test edebilirsiniz:

1. Inspector'ı yükleyin: `npx @modelcontextprotocol/inspector`
2. Inspector'ı çalıştırın ve sunucunuza bağlayın
3. Oluşturduğunuz araçları test edin

### .NET

```csharp
var builder = WebApplication.CreateBuilder(args);
builder.Services
    .AddMcpServer();
 ```
## stdio sunucunuzu hata ayıklama

### MCP Inspector kullanımı

MCP Inspector, MCP sunucularını hata ayıklama ve test etmek için değerli bir araçtır. İşte stdio sunucunuzla nasıl kullanacağınız:

1. **Inspector'ı yükleyin**:
   ```bash
   npx @modelcontextprotocol/inspector
   ```

2. **Inspector'ı çalıştırın**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

3. **Sunucunuzu test edin**: Inspector, şu imkanları sağlayan bir web arayüzü sunar:
   - Sunucu özelliklerini görüntüleme
   - Araçları farklı parametrelerle test etme
   - JSON-RPC mesajlarını izleme
   - Bağlantı sorunlarını hata ayıklama

### VS Code kullanımı

MCP sunucunuzu doğrudan VS Code'da da hata ayıklayabilirsiniz:

1. `.vscode/launch.json` dosyasında bir başlatma yapılandırması oluşturun:
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

2. Sunucu kodunuzda kesme noktaları ayarlayın
3. Hata ayıklayıcıyı çalıştırıp Inspector ile test edin

### Yaygın hata ayıklama ipuçları

- Kayıt için `stderr` kullanın - MCP mesajları için ayrılmış olan `stdout`'a yazmayın
- Tüm JSON-RPC mesajlarının yeni satırla ayrıldığından emin olun
- Karmaşık işlevsellik eklemeden önce basit araçlarla test edin
- Mesaj formatlarını doğrulamak için Inspector'ı kullanın

## stdio sunucunuzu VS Code'da tüketme

MCP stdio sunucunuzu oluşturduktan sonra, Claude veya diğer MCP uyumlu istemcilerle kullanmak üzere VS Code'a entegre edebilirsiniz.

### Yapılandırma

1. Windows için `%APPDATA%\Claude\claude_desktop_config.json` veya Mac için `~/Library/Application Support/Claude/claude_desktop_config.json` yolunda bir MCP yapılandırma dosyası oluşturun:

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

2. **Claude'u yeniden başlatın**: Yeni sunucu yapılandırmasının yüklenmesi için Claude'u kapatıp açın.

3. **Bağlantıyı test edin**: Claude ile bir konuşma başlatıp sunucu araçlarınızı deneyin:
   - "Merhaba aracı kullanarak beni selamlayabilir misin?"
   - "15 ve 27'nin toplamını hesapla"
   - "Sunucu bilgisi nedir?"

### TypeScript stdio sunucu örneği

İşte referans olarak tam bir TypeScript örneği:

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

// Araç ekle
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

- Güncel **stdio taşıma** kullanarak MCP sunucuları oluşturmayı (önerilen yöntem)
- SSE taşıma yönteminin neden stdio ve Streamable HTTP lehine kullanımdan kaldırıldığını anlamayı
- MCP istemcileri tarafından çağrılabilecek araçları oluşturmayı
- MCP Inspector kullanarak sunucuyu hata ayıklamayı
- stdio sunucunuzu VS Code ve Claude ile entegre etmeyi

Stdio taşıma, kullanımdan kaldırılan SSE yöntemine göre daha basit, daha güvenli ve daha performanslı bir MCP sunucusu oluşturma yoludur. 2025-06-18 spesifikasyonundan itibaren çoğu MCP sunucu uygulaması için önerilen taşıma yöntemidir.


### .NET

1. Önce bazı araçlar oluşturalım, bunun için *Tools.cs* adlı bir dosya oluşturacağız, içeriği şu şekilde:

  ```csharp
  using System.ComponentModel;
  using System.Text.Json;
  using ModelContextProtocol.Server;
  ```

## Egzersiz: stdio sunucunuzu test etme

stdio sunucunuzu oluşturduğunuza göre, doğru çalıştığından emin olmak için test edelim.

### Gereksinimler

1. MCP Inspector'ın yüklü olduğundan emin olun:
   ```bash
   npm install -g @modelcontextprotocol/inspector
   ```

2. Sunucu kodunuz kaydedilmiş olmalı (örneğin `server.py`)

### Inspector ile test

1. **Sunucunuzla Inspector'ı başlatın**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

2. **Web arayüzünü açın**: Inspector, sunucunuzun özelliklerini gösteren bir tarayıcı penceresi açar.

3. **Araçları test edin**: 
   - `get_greeting` aracını farklı isimlerle deneyin
   - `calculate_sum` aracını çeşitli sayılarla test edin
   - `get_server_info` aracını çağırarak sunucu meta verilerini görün

4. **İletişimi izleyin**: Inspector, istemci ile sunucu arasındaki JSON-RPC mesajlarını gösterir.

### Neler görmelisiniz

Sunucunuz doğru başladıysa, şunları göreceksiniz:
- Inspector'da listelenen sunucu özellikleri
- Test için kullanılabilir araçlar
- Başarılı JSON-RPC mesaj alışverişleri
- Arayüzde gösterilen araç yanıtları

### Yaygın sorunlar ve çözümleri

**Sunucu başlamıyor:**
- Tüm bağımlılıkların yüklü olduğunu kontrol edin: `pip install mcp`
- Python söz dizimi ve girintileme kontrolü yapın
- Konsoldaki hata mesajlarını inceleyin

**Araçlar görünmüyor:**
- `@server.tool()` dekoratörlerinin var olduğundan emin olun
- Araç fonksiyonlarının `main()` öncesinde tanımlı olup olmadığını kontrol edin
- Sunucunun düzgün yapılandırıldığını doğrulayın

**Bağlantı sorunları:**
- Sunucunun stdio taşıma yöntemini doğru kullandığından emin olun
- Başka süreçlerin müdahale etmediğini kontrol edin
- Inspector komut sözdizimini doğrulayın

## Ödev

Sunucunuzu daha fazla özellik ekleyerek geliştirmeyi deneyin. Örneğin bir API çağrısı yapan bir araç eklemek için [bu sayfayı](https://api.chucknorris.io/) inceleyebilirsiniz. Sunucunun nasıl görüneceğine siz karar verin. İyi eğlenceler :)
## Çözüm

[Çözüm](./solution/README.md) İşleyen kod ile olası bir çözüm burada.

## Temel Çıkarımlar

Bu bölümün temel çıkarımları şunlardır:

- Stdio taşıma, yerel MCP sunucuları için önerilen mekanizmadır.
- Stdio taşıma, MCP sunucuları ile istemciler arasında standart giriş ve çıkış akışları kullanarak kesintisiz iletişim sağlar.
- Inspector ve Visual Studio Code kullanarak stdio sunucuları doğrudan tüketebilirsiniz, bu da hata ayıklamayı ve entegrasyonu kolaylaştırır.

## Örnekler 

- [Java Hesap Makinesi](../samples/java/calculator/README.md)
- [.Net Hesap Makinesi](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Hesap Makinesi](../samples/javascript/README.md)
- [TypeScript Hesap Makinesi](../samples/typescript/README.md)
- [Python Hesap Makinesi](../../../../03-GettingStarted/samples/python) 

## Ek Kaynaklar

- [SSE](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events)

## Sonraki Ne Var

## Sonraki Adımlar

Stdio taşıma ile MCP sunucularını nasıl oluşturacağınızı öğrendiğinize göre, daha ileri konuları keşfedebilirsiniz:

- **Sonraki**: [MCP ile HTTP Akışı (Streamable HTTP)](../06-http-streaming/README.md) - Uzak sunucular için desteklenen diğer taşıma mekanizmasını öğrenin
- **İleri Seviye**: [MCP Güvenlik En İyi Uygulamaları](../../02-Security/README.md) - MCP sunucularınızda güvenliği uygulayın
- **Üretim**: [Dağıtım Stratejileri](../09-deployment/README.md) - Sunucularınızı üretim için dağıtın

## Ek Kaynaklar

- [MCP Spesifikasyonu 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/) - Güncel spesifikasyon
- [MCP SDK Dokümantasyonu](https://github.com/modelcontextprotocol/sdk) - Tüm diller için SDK referansları
- [Topluluk Örnekleri](../../06-CommunityContributions/README.md) - Topluluktan daha fazla sunucu örneği

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Feragatname**:
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba sarf etsek de, otomatik çevirilerin hata veya yanlışlık içerebileceğini lütfen unutmayınız. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu ortaya çıkabilecek yanlış anlamalardan veya yanlış yorumlamalardan sorumlu değiliz.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->