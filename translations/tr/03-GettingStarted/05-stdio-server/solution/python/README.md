# MCP stdio Sunucusu - Python Çözümü

> **⚠️ Önemli**: Bu çözüm, MCP Spesifikasyonu 2025-06-18 tarafından önerildiği gibi **stdio taşıma** yöntemini kullanacak şekilde güncellenmiştir. Orijinal SSE taşıma yöntemi artık kullanımdan kaldırılmıştır.

## Genel Bakış

Bu Python çözümü, mevcut stdio taşıma yöntemini kullanarak bir MCP sunucusu oluşturmayı gösterir. Stdio taşıma yöntemi, kullanımdan kaldırılan SSE yaklaşımına göre daha basit, daha güvenli ve daha iyi performans sağlar.

## Ön Koşullar

- Python 3.8 veya daha yeni bir sürüm
- Paket yönetimi için `uv` yüklemeniz önerilir, [talimatlar](https://docs.astral.sh/uv/#highlights) için bakınız.

## Kurulum Talimatları

### Adım 1: Sanal bir ortam oluşturun

```bash
python -m venv venv
```

### Adım 2: Sanal ortamı etkinleştirin

**Windows:**
```bash
venv\Scripts\activate
```

**macOS/Linux:**
```bash
source venv/bin/activate
```

### Adım 3: Bağımlılıkları yükleyin

```bash
pip install mcp
```

## Sunucuyu Çalıştırma

Stdio sunucusu, eski SSE sunucusundan farklı şekilde çalışır. Bir web sunucusu başlatmak yerine, stdin/stdout üzerinden iletişim kurar:

```bash
python server.py
```

**Önemli**: Sunucu donmuş gibi görünebilir - bu normaldir! stdin'den JSON-RPC mesajlarını bekliyor.

## Sunucuyu Test Etme

### Yöntem 1: MCP Inspector Kullanımı (Önerilen)

```bash
npx @modelcontextprotocol/inspector python server.py
```

Bu işlem:
1. Sunucunuzu bir alt işlem olarak başlatır
2. Test için bir web arayüzü açar
3. Tüm sunucu araçlarını etkileşimli olarak test etmenizi sağlar

### Yöntem 2: Doğrudan JSON-RPC Testi

JSON-RPC mesajlarını doğrudan göndererek de test yapabilirsiniz:

1. Sunucuyu başlatın: `python server.py`
2. Bir JSON-RPC mesajı gönderin (örnek):

```json
{"jsonrpc": "2.0", "id": 1, "method": "tools/list"}
```

3. Sunucu mevcut araçlarla yanıt verecektir

### Mevcut Araçlar

Sunucu şu araçları sağlar:

- **add(a, b)**: İki sayıyı toplar
- **multiply(a, b)**: İki sayıyı çarpar  
- **get_greeting(name)**: Kişiselleştirilmiş bir selamlama oluşturur
- **get_server_info()**: Sunucu hakkında bilgi alır

### Claude Desktop ile Test Etme

Bu sunucuyu Claude Desktop ile kullanmak için `claude_desktop_config.json` dosyanıza şu yapılandırmayı ekleyin:

```json
{
  "mcpServers": {
    "example-stdio-server": {
      "command": "python",
      "args": ["path/to/server.py"]
    }
  }
}
```

## SSE ile Farklılıklar

**stdio taşıma (Mevcut):**
- ✅ Daha basit kurulum - web sunucusu gerekmez
- ✅ Daha iyi güvenlik - HTTP uç noktaları yok
- ✅ Alt işlem tabanlı iletişim
- ✅ stdin/stdout üzerinden JSON-RPC
- ✅ Daha iyi performans

**SSE taşıma (Kullanımdan kaldırıldı):**
- ❌ HTTP sunucusu kurulumu gerektiriyordu
- ❌ Web çerçevesi (Starlette/FastAPI) gerekiyordu
- ❌ Daha karmaşık yönlendirme ve oturum yönetimi
- ❌ Ek güvenlik hususları
- ❌ MCP 2025-06-18'de artık kullanımdan kaldırıldı

## Hata Ayıklama İpuçları

- Günlük kaydı için `stderr` kullanın (asla `stdout` kullanmayın)
- Görsel hata ayıklama için Inspector ile test yapın
- Tüm JSON mesajlarının satır sonu ile ayrıldığından emin olun
- Sunucunun hatasız başladığını kontrol edin

Bu çözüm, mevcut MCP spesifikasyonunu takip eder ve stdio taşıma yönteminin en iyi uygulamalarını gösterir.

---

**Feragatname**:  
Bu belge, [Co-op Translator](https://github.com/Azure/co-op-translator) adlı yapay zeka çeviri hizmeti kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hata veya yanlışlıklar içerebileceğini lütfen unutmayın. Belgenin orijinal dili, yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımından kaynaklanan yanlış anlama veya yanlış yorumlamalardan sorumlu değiliz.