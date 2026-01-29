# MCP stdio Sunucusu - TypeScript Çözümü

> **⚠️ Önemli**: Bu çözüm, MCP Spesifikasyonu 2025-06-18 tarafından önerildiği gibi **stdio taşımacılığını** kullanacak şekilde güncellenmiştir. Orijinal SSE taşımacılığı artık kullanımdan kaldırılmıştır.

## Genel Bakış

Bu TypeScript çözümü, mevcut stdio taşımacılığını kullanarak bir MCP sunucusunun nasıl oluşturulacağını göstermektedir. Stdio taşımacılığı, kullanımdan kaldırılan SSE yaklaşımına göre daha basit, daha güvenli ve daha iyi performans sunar.

## Gereksinimler

- Node.js 18+ veya daha yeni bir sürüm
- npm veya yarn paket yöneticisi

## Kurulum Talimatları

### Adım 1: Bağımlılıkları yükleyin

```bash
npm install
```

### Adım 2: Projeyi derleyin

```bash
npm run build
```

## Sunucuyu Çalıştırma

Stdio sunucusu, eski SSE sunucusundan farklı şekilde çalışır. Bir web sunucusu başlatmak yerine, stdin/stdout üzerinden iletişim kurar:

```bash
npm start
```

**Önemli**: Sunucu donmuş gibi görünebilir - bu normaldir! stdin'den JSON-RPC mesajlarını bekliyor.

## Sunucuyu Test Etme

### Yöntem 1: MCP Inspector Kullanımı (Önerilen)

```bash
npm run inspector
```

Bu işlem şunları yapar:
1. Sunucunuzu bir alt işlem olarak başlatır
2. Test için bir web arayüzü açar
3. Tüm sunucu araçlarını etkileşimli olarak test etmenizi sağlar

### Yöntem 2: Doğrudan komut satırı testi

Inspector'ı doğrudan başlatarak da test yapabilirsiniz:

```bash
npx @modelcontextprotocol/inspector node build/index.js
```

### Mevcut Araçlar

Sunucu şu araçları sağlar:

- **add(a, b)**: İki sayıyı toplar
- **multiply(a, b)**: İki sayıyı çarpar  
- **get_greeting(name)**: Kişiselleştirilmiş bir selamlama oluşturur
- **get_server_info()**: Sunucu hakkında bilgi alır

### Claude Desktop ile Test Etme

Bu sunucuyu Claude Desktop ile kullanmak için, `claude_desktop_config.json` dosyanıza şu yapılandırmayı ekleyin:

```json
{
  "mcpServers": {
    "example-stdio-server": {
      "command": "node",
      "args": ["path/to/build/index.js"]
    }
  }
}
```

## Proje Yapısı

```
typescript/
├── src/
│   └── index.ts          # Main server implementation
├── build/                # Compiled JavaScript (generated)
├── package.json          # Project configuration
├── tsconfig.json         # TypeScript configuration
└── README.md            # This file
```

## SSE ile Olan Temel Farklılıklar

**stdio taşımacılığı (Mevcut):**
- ✅ Daha basit kurulum - HTTP sunucusuna gerek yok
- ✅ Daha iyi güvenlik - HTTP uç noktaları yok
- ✅ Alt işlem tabanlı iletişim
- ✅ stdin/stdout üzerinden JSON-RPC
- ✅ Daha iyi performans

**SSE taşımacılığı (Kullanımdan Kaldırıldı):**
- ❌ Express sunucusu kurulumu gerekiyordu
- ❌ Karmaşık yönlendirme ve oturum yönetimi gerekiyordu
- ❌ Daha fazla bağımlılık (Express, HTTP işleme)
- ❌ Ek güvenlik hususları
- ❌ MCP 2025-06-18'de artık kullanımdan kaldırıldı

## Geliştirme İpuçları

- Günlük kaydı için `console.error()` kullanın (`console.log()` kullanmayın çünkü stdout'a yazar)
- Test etmeden önce `npm run build` ile derleme yapın
- Görsel hata ayıklama için Inspector ile test yapın
- Tüm JSON mesajlarının doğru biçimlendirildiğinden emin olun
- Sunucu, SIGINT/SIGTERM sinyallerinde otomatik olarak düzgün bir şekilde kapanır

Bu çözüm, mevcut MCP spesifikasyonunu takip eder ve TypeScript kullanarak stdio taşımacılığı uygulaması için en iyi uygulamaları gösterir.

---

**Feragatname**:  
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hata veya yanlışlık içerebileceğini lütfen unutmayın. Belgenin orijinal dili, yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımından kaynaklanan yanlış anlamalar veya yanlış yorumlamalar için sorumluluk kabul edilmez.