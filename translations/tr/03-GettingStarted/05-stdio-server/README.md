# stdio Transport ile MCP Sunucusu

> **⚠️ Önemli Güncelleme**: MCP Spesifikasyonu 2025-06-18 itibarıyla, bağımsız SSE (Server-Sent Events) taşıyıcı **kaldırılmış** ve yerine "Streamable HTTP" taşıyıcı gelmiştir. Mevcut MCP spesifikasyonu iki temel taşıyıcı mekanizmayı tanımlar:
> 1. **stdio** - Standart giriş/çıkış (yerel sunucular için önerilir)
> 2. **Streamable HTTP** - Dahili olarak SSE kullanabilecek uzak sunucular için
>
> Bu ders, çoğu MCP sunucu uygulaması için önerilen **stdio taşıyıcısı**na odaklanacak şekilde güncellenmiştir.

stdio taşıyıcısı, MCP sunucularının standart giriş ve çıkış akışları ile istemcilerle iletişim kurmasına olanak tanır. Bu, mevcut MCP spesifikasyonunda en yaygın kullanılan ve önerilen taşıyıcı mekanizmadır ve çeşitli istemci uygulamalarıyla kolayca entegre olabilen basit ve verimli bir MCP sunucusu oluşturmanın yolunu sağlar.

## Genel Bakış

Bu derste stdio taşıyıcı kullanarak MCP Sunucularının nasıl oluşturulup kullanılacağı anlatılmaktadır.

## Öğrenme Hedefleri

Bu dersin sonunda şunları yapabileceksiniz:

- stdio taşıyıcı kullanarak bir MCP Sunucusu oluşturmak.
- Inspector kullanarak bir MCP Sunucusunu hata ayıklamak.
- Visual Studio Code kullanarak bir MCP Sunucusunu tüketmek.
- Mevcut MCP taşıyıcı mekanizmalarını ve stdio'nun neden önerildiğini anlamak.


## stdio Taşıyıcı - Nasıl Çalışır

stdio taşıyıcı, mevcut MCP spesifikasyonundaki (2025-06-18) desteklenen iki taşıyıcı türünden biridir. İşleyişi:

- **Basit İletişim**: Sunucu, standart girdiden (`stdin`) JSON-RPC mesajları okur ve mesajları standart çıktıya (`stdout`) gönderir.
- **İşlem Tabanlı**: İstemci, MCP sunucusunu bir alt işlem olarak başlatır.
- **Mesaj Formatı**: Mesajlar bireysel JSON-RPC istekleri, bildirimleri veya yanıtlarıdır, satır sonları ile ayrılır.
- **Kayıt**: Sunucu, günlük amaçlı UTF-8 dizgilerini standart hata çıkışına (`stderr`) yazabilir.

### Temel Gereksinimler:
- Mesajlar satır sonları ile ayrılmalı ve gömülü satır sonları içermemelidir
- Sunucu, geçerli bir MCP mesajı olmayan hiçbir şeyi `stdout`'a yazmamalıdır
- İstemci, geçerli bir MCP mesajı olmayan hiçbir şeyi sunucunun `stdin`'ine yazmamalıdır

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

Yukarıdaki kodda:

- MCP SDK'dan `Server` sınıfı ve `StdioServerTransport` import edilir
- Temel yapılandırma ve yeteneklerle bir sunucu örneği oluşturulur
- `StdioServerTransport` örneği oluşturularak sunucu ile bağlantı kurulur, stdin/stdout üzerinden iletişim etkinleştirilir

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

Yukarıdaki kodda:

- MCP SDK kullanılarak bir sunucu örneği oluşturulur
- Dekoratörler ile araçlar tanımlanır
- Taşıyıcıyı yönetmek için stdio_server bağlam yöneticisi kullanılır

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

SSE'den temel farklar şunlardır:

- stdio sunucuları web sunucusu kurulumu veya HTTP uç noktaları gerektirmez
- İstemci tarafından alt işlem olarak başlatılırlar
- stdin/stdout akışları üzerinden iletişim kurarlar
- Uygulaması ve hata ayıklaması daha basittir

## Alıştırma: stdio Sunucu Oluşturma

Sunucumuzu oluştururken iki şeyi akılda tutmalıyız:

- Bağlantı ve mesajlar için uç noktaları açmak amacıyla bir web sunucusu kullanmamız gerekir.
## Laboratuvar: Basit Bir MCP stdio Sunucusu Oluşturma

Bu laboratuvarda, önerilen stdio taşıyıcısını kullanarak basit bir MCP sunucusu oluşturacağız. Bu sunucu, istemcilerin Standart Model Context Protocol kullanarak çağırabileceği araçları sunacak.

### Ön Koşullar

- Python 3.8 veya üzeri
- MCP Python SDK: `pip install mcp`
- Async programlama hakkında temel bilgi

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
    # stdio taşımayı kullan
    async with stdio_server(server) as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            server.create_initialization_options()
        )

if __name__ == "__main__":
    asyncio.run(main())
```

## Kaldırılan SSE yönteminden temel farklar

**Stdio Taşıyıcı (Mevcut Standart):**
- Basit alt işlem modeli - istemci sunucuyu çocuk işlem olarak başlatır
- JSON-RPC mesajları ile stdin/stdout üzerinden iletişim
- HTTP sunucusu kurulumu gerekmez
- Daha iyi performans ve güvenlik
- Hata ayıklama ve geliştirme kolaylığı

**SSE Taşıyıcı (MCP 2025-06-18 itibarıyla kaldırıldı):**
- SSE uç noktalarıyla HTTP sunucusu gerektirirdi
- Web sunucusu altyapısı ile daha karmaşık kurulum
- HTTP uç noktaları için ek güvenlik kaygıları
- Şimdi web tabanlı senaryolar için Streamable HTTP ile değiştirildi

### stdio taşıyıcı ile sunucu oluşturma

stdio sunucumuzu oluşturmak için:

1. **Gerekli kütüphaneleri import edin** - MCP sunucu bileşenleri ve stdio taşıyıcı gerekli
2. **Bir sunucu örneği oluşturun** - Sunucuyu yetenekleri ile tanımlayın
3. **Araçları tanımlayın** - Sunmak istediğiniz fonksiyonları ekleyin
4. **Taşıyıcıyı ayarlayın** - stdio iletişimini yapılandırın
5. **Sunucuyu çalıştırın** - Sunucuyu başlatın ve mesajları yönetin

Bunu adım adım yapalım:

### Adım 1: Temel bir stdio sunucu oluşturun

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

### Adım 2: Daha fazla araç ekleyin

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

Sunucu başlar ve stdin'den giriş bekler. stdio taşıyıcısı üzerinden JSON-RPC mesajları kullanarak iletişim kurar.

### Adım 4: Inspector ile test etme

Sunucunuzu MCP Inspector kullanarak test edebilirsiniz:

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

### MCP Inspector kullanarak

MCP Inspector, MCP sunucularını hata ayıklamak ve test etmek için değerli bir araçtır. stdio sunucunuzla nasıl kullanacağınız:

1. **Inspector'ı Yükleyin**:
   ```bash
   npx @modelcontextprotocol/inspector
   ```

2. **Inspector'ı Çalıştırın**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

3. **Sunucunuzu Test Edin**: Inspector, bir web arayüzü sağlar ve şunları yapabilirsiniz:
   - Sunucu yeteneklerini görüntüleme
   - Farklı parametrelerle araçları test etme
   - JSON-RPC mesajlarını takip etme
   - Bağlantı sorunlarını hata ayıklama

### VS Code kullanarak

MCP sunucunuzu VS Code içinde doğrudan da hata ayıklayabilirsiniz:

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

2. Sunucu kodunuzda kırılma noktaları ayarlayın
3. Hata ayıklayıcıyı çalıştırın ve Inspector ile test edin

### Yaygın hata ayıklama ipuçları

- Kayıt için `stderr` kullanın - MCP mesajları için ayrılmış olan `stdout`'a asla yazmayın
- Tüm JSON-RPC mesajlarının satır sonları ile ayrıldığından emin olun
- Karmaşık işlevsellik eklemeden önce basit araçlarla test yapın
- Mesaj formatlarını doğrulamak için Inspector'u kullanın

## stdio sunucunuzu VS Code'da kullanma

MCP stdio sunucunuzu oluşturduktan sonra, onu VS Code ile entegre ederek Claude veya diğer MCP uyumlu istemcilerle kullanabilirsiniz.

### Yapılandırma

1. `%APPDATA%\Claude\claude_desktop_config.json` (Windows) veya `~/Library/Application Support/Claude/claude_desktop_config.json` (Mac) konumunda bir MCP yapılandırma dosyası oluşturun:

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

2. **Claude'u yeniden başlatın**: Yeni sunucu yapılandırmasını yüklemek için Claude'u kapatıp açın.

3. **Bağlantıyı test edin**: Claude ile bir konuşma başlatın ve sunucunuzun araçlarını deneyin:
   - "Selamlama aracını kullanarak beni selamlayabilir misin?"
   - "15 ile 27'nin toplamını hesapla"
   - "Sunucu bilgisi nedir?"

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

Bu güncellenen derste şunları öğrendiniz:

- Mevcut **stdio taşıyıcı** kullanarak MCP sunucuları oluşturmak (önerilen yöntem)
- SSE taşıyıcısının neden stdio ve Streamable HTTP lehine kaldırıldığını anlamak
- MCP istemcilerinin çağırabileceği araçlar oluşturmak
- Sunucunuzu MCP Inspector ile hata ayıklamak
- stdio sunucunuzu VS Code ve Claude ile entegre etmek

stdio taşıyıcı, kaldırılan SSE yöntemine kıyasla MCP sunucuları oluşturmak için daha basit, daha güvenli ve daha yüksek performanslı bir yöntem sunar. 2025-06-18 tarihli spesifikasyon itibarıyla çoğu MCP sunucu uygulaması için önerilen taşıyıcıdır.


### .NET

1. Öncelikle bazı araçlar oluşturalım, bunun için *Tools.cs* adlı bir dosya oluşturup aşağıdaki içeriği ekleyeceğiz:

  ```csharp
  using System.ComponentModel;
  using System.Text.Json;
  using ModelContextProtocol.Server;
  ```

## Alıştırma: stdio sunucunuzu test etme

stdio sunucunuzu oluşturduğunuza göre, doğru çalıştığından emin olmak için test edelim.

### Ön Koşullar

1. MCP Inspector'ın yüklü olduğundan emin olun:
   ```bash
   npm install -g @modelcontextprotocol/inspector
   ```

2. Sunucu kodunuzun kaydedilmiş olması (örneğin `server.py` olarak)

### Inspector ile Test

1. **Sunucunuzla birlikte Inspector'ı başlatın**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

2. **Web arayüzünü açın**: Inspector, sunucunuzun yeteneklerini gösteren bir tarayıcı penceresi açacaktır.

3. **Araçları test edin**: 
   - `get_greeting` aracını farklı isimlerle deneyin
   - `calculate_sum` aracını çeşitli sayılarla test edin
   - `get_server_info` aracını çağırarak sunucu meta verisini görün

4. **İletişimi izleyin**: Inspector, istemci ile sunucu arasındaki JSON-RPC mesajlarını gösterir.

### Görmeniz gerekenler

Sunucunuz doğru başladıysa, şunları görmelisiniz:
- Inspector'da listelenen sunucu yetenekleri
- Test için kullanılabilir araçlar
- Başarılı JSON-RPC mesaj alışverişi
- Araç yanıtlarının arayüzde görüntülenmesi

### Yaygın sorunlar ve çözümleri

**Sunucu başlamıyor:**
- Tüm bağımlılıkların yüklü olduğundan emin olun: `pip install mcp`
- Python sözdizimi ve girintilemesini kontrol edin
- Konsoldaki hata mesajlarına bakın

**Araçlar görünmüyor:**
- `@server.tool()` dekoratörlerinin mevcut olduğundan emin olun
- Araç fonksiyonlarının `main()`'den önce tanımlandığını kontrol edin
- Sunucunun doğru yapılandırıldığını doğrulayın

**Bağlantı sorunları:**
- Sunucunun stdio taşıyıcıyı doğru kullandığından emin olun
- Başka işlemlerin engellemediğini kontrol edin
- Inspector komut sözdizimini doğrulayın

## Ödev

Sunucunuzu daha fazla yetenekle geliştirmeye çalışın. Örneğin bir API çağıran araç eklemek için [bu sayfaya](https://api.chucknorris.io/) bakabilirsiniz. Sunucunun nasıl görünmesi gerektiğine siz karar verin. İyi eğlenceler :)
## Çözüm

[Çözüm](./solution/README.md) Çalışan kod ile olası bir çözüm örneği.

## Temel Noktalar

Bu bölümden çıkarılacak temel noktalar şunlardır:

- stdio taşıyıcı, yerel MCP sunucuları için önerilen mekanizmadır.
- Stdio taşıyıcı, MCP sunucuları ile istemciler arasında standart giriş ve çıkış akışları üzerinden kesintisiz iletişim sağlar.
- Inspector ve Visual Studio Code'u kullanarak stdio sunucularına doğrudan erişebilir, böylece hata ayıklama ve entegrasyon kolaylaşır.

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

stdio taşıyıcı ile MCP sunucuları oluşturmayı öğrendiğinize göre, daha ileri konuları keşfedebilirsiniz:

- **Sonraki**: [MCP ile HTTP Akışı (Streamable HTTP)](../06-http-streaming/README.md) - Uzak sunucular için diğer desteklenen taşıyıcıyı öğrenin
- **İleri Düzey**: [MCP Güvenlik En İyi Uygulamaları](../../02-Security/README.md) - MCP sunucularınızı güvenli hale getirin
- **Üretim**: [Dağıtım Stratejileri](../09-deployment/README.md) - Sunucularınızı üretim ortamına dağıtın

## Ek Kaynaklar

- [MCP Spesifikasyonu 2025-06-18](https://spec.modelcontextprotocol.io/specification/) - Resmi spesifikasyon
- [MCP SDK Dokümantasyonu](https://github.com/modelcontextprotocol/sdk) - Tüm diller için SDK referansları
- [Topluluk Örnekleri](../../06-CommunityContributions/README.md) - Topluluktan daha fazla sunucu örneği

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Feragatname**:  
Bu belge, AI çeviri servisi [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba gösterilse de, otomatik çevirilerin hata veya yanlışlık içerebileceğini lütfen unutmayınız. Orijinal belgenin ana dilindeki versiyonu yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımıyla ortaya çıkabilecek herhangi bir yanlış anlama veya yanlış yorumdan dolayı sorumluluk kabul edilmemektedir.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->