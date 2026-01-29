# MCP stdio Sunucusu - .NET Çözümü

> **⚠️ Önemli**: Bu çözüm, MCP Spesifikasyonu 2025-06-18 tarafından önerildiği gibi **stdio taşıma** yöntemini kullanacak şekilde güncellenmiştir. Orijinal SSE taşıma yöntemi artık kullanımdan kaldırılmıştır.

## Genel Bakış

Bu .NET çözümü, mevcut stdio taşıma yöntemini kullanarak bir MCP sunucusunun nasıl oluşturulacağını gösterir. Stdio taşıma yöntemi, kullanımdan kaldırılan SSE yaklaşımına göre daha basit, daha güvenli ve daha iyi performans sunar.

## Gereksinimler

- .NET 9.0 SDK veya daha yenisi
- .NET bağımlılık enjeksiyonu hakkında temel bilgi

## Kurulum Talimatları

### Adım 1: Bağımlılıkları geri yükleyin

```bash
dotnet restore
```

### Adım 2: Projeyi derleyin

```bash
dotnet build
```

## Sunucuyu Çalıştırma

Stdio sunucusu, eski HTTP tabanlı sunucudan farklı şekilde çalışır. Bir web sunucusu başlatmak yerine stdin/stdout üzerinden iletişim kurar:

```bash
dotnet run
```

**Önemli**: Sunucu donmuş gibi görünebilir - bu normaldir! stdin'den JSON-RPC mesajlarını bekliyor.

## Sunucuyu Test Etme

### Yöntem 1: MCP Inspector Kullanımı (Önerilir)

```bash
npx @modelcontextprotocol/inspector dotnet run
```

Bu işlem şunları yapar:
1. Sunucunuzu bir alt işlem olarak başlatır
2. Test için bir web arayüzü açar
3. Tüm sunucu araçlarını etkileşimli olarak test etmenizi sağlar

### Yöntem 2: Komut satırı ile doğrudan test

Inspector'ı doğrudan başlatarak da test edebilirsiniz:

```bash
npx @modelcontextprotocol/inspector dotnet run --project .
```

### Mevcut Araçlar

Sunucu şu araçları sağlar:

- **AddNumbers(a, b)**: İki sayıyı toplar
- **MultiplyNumbers(a, b)**: İki sayıyı çarpar  
- **GetGreeting(name)**: Kişiselleştirilmiş bir selamlama oluşturur
- **GetServerInfo()**: Sunucu hakkında bilgi alır

### Claude Desktop ile Test Etme

Bu sunucuyu Claude Desktop ile kullanmak için `claude_desktop_config.json` dosyanıza şu yapılandırmayı ekleyin:

```json
{
  "mcpServers": {
    "example-stdio-server": {
      "command": "dotnet",
      "args": ["run", "--project", "path/to/server.csproj"]
    }
  }
}
```

## Proje Yapısı

```
dotnet/
├── Program.cs           # Main server setup and configuration
├── Tools.cs            # Tool implementations
├── server.csproj       # Project file with dependencies
├── server.sln         # Solution file
├── Properties/         # Project properties
└── README.md          # This file
```

## HTTP/SSE ile Farklılıklar

**stdio taşıma (Mevcut):**
- ✅ Daha basit kurulum - web sunucusuna gerek yok
- ✅ Daha iyi güvenlik - HTTP uç noktaları yok
- ✅ `Host.CreateApplicationBuilder()` kullanır, `WebApplication.CreateBuilder()` yerine
- ✅ `WithStdioTransport()` kullanır, `WithHttpTransport()` yerine
- ✅ Konsol uygulaması, web uygulaması yerine
- ✅ Daha iyi performans

**HTTP/SSE taşıma (Kullanımdan kaldırıldı):**
- ❌ ASP.NET Core web sunucusu gerektiriyordu
- ❌ `app.MapMcp()` yönlendirme kurulumu gerekiyordu
- ❌ Daha karmaşık yapılandırma ve bağımlılıklar
- ❌ Ek güvenlik hususları
- ❌ MCP 2025-06-18'de artık kullanımdan kaldırıldı

## Geliştirme Özellikleri

- **Bağımlılık Enjeksiyonu**: Hizmetler ve günlükleme için tam DI desteği
- **Yapılandırılmış Günlükleme**: `ILogger<T>` kullanarak stderr'e doğru günlükleme
- **Araç Nitelikleri**: `[McpServerTool]` nitelikleri kullanarak temiz araç tanımı
- **Async Desteği**: Tüm araçlar async işlemleri destekler
- **Hata Yönetimi**: Zarif hata yönetimi ve günlükleme

## Geliştirme İpuçları

- Günlükleme için `ILogger` kullanın (stdout'a doğrudan yazmayın)
- Test etmeden önce `dotnet build` ile derleyin
- Görsel hata ayıklama için Inspector ile test edin
- Tüm günlükler otomatik olarak stderr'e gider
- Sunucu, zarif kapatma sinyallerini işler

Bu çözüm, mevcut MCP spesifikasyonunu takip eder ve .NET kullanarak stdio taşıma yönteminin en iyi uygulamalarını gösterir.

---

**Feragatname**:  
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hata veya yanlışlıklar içerebileceğini lütfen unutmayın. Belgenin orijinal dilindeki hali, yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımından kaynaklanan yanlış anlamalar veya yanlış yorumlamalar için sorumluluk kabul etmiyoruz.