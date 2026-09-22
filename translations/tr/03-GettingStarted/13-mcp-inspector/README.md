# MCP Inspector ile Hata Ayıklama

> [!NOTE]
> `--sse` kullanan komutlar ve `/sse` ile biten URL'ler eski HTTP+SSE
> taşıma protokolünü test eder. Yeni bir MCP `2026-07-28` sunucusu için,
> Streamable HTTP'yi destekleyen bir Inspector sürümü kullanın ve o taşıma protokolünü seçin.

**MCP Inspector**, tam bir AI host uygulamasına ihtiyaç duymadan MCP sunucularınızı etkileşimli olarak test edip sorunlarını gidermenizi sağlayan temel bir hata ayıklama aracıdır. Bunu "MCP için Postman" olarak düşünebilirsiniz - istek göndermek, yanıtları görüntülemek ve sunucunuzun nasıl davrandığını anlamak için görsel bir arayüz sağlar.

## Neden MCP Inspector Kullanmalısınız?

MCP sunucuları oluştururken genellikle şu zorluklarla karşılaşırsınız:

- **"Sunucum çalışıyor mu?"** - Inspector bağlantı durumunu gösterir
- **"Araçlarım doğru kayıtlı mı?"** - Inspector tüm kullanılabilir araçları listeler
- **"Yanıt formatı nedir?"** - Inspector tam JSON yanıtlarını gösterir
- **"Bu araç neden çalışmıyor?"** - Inspector ayrıntılı hata mesajları gösterir

## Önkoşullar

- Node.js 18+ yüklü olmalıdır
- npm (Node.js ile birlikte gelir)
- Test etmek için bir MCP sunucusu (bkz. [Modül 3.1 - İlk Sunucu](../01-first-server/README.md))

## Kurulum

### Seçenek 1: npx ile Çalıştırma (Hızlı Test için Önerilir)

```bash
npx @modelcontextprotocol/inspector
```

### Seçenek 2: Global Olarak Yükleme

```bash
npm install -g @modelcontextprotocol/inspector
mcp-inspector
```

### Seçenek 3: Projenize Ekleme

```bash
cd your-mcp-server-project
npm install --save-dev @modelcontextprotocol/inspector
```

`package.json` dosyanıza ekleyin:
```json
{
  "scripts": {
    "inspector": "mcp-inspector"
  }
}
```

---

## Sunucunuza Bağlanma

### stdio Sunucuları (Yerel İşlem)

Standart girdi/çıktı ile iletişim kuran sunucular için:

```bash
# Python sunucusu
npx @modelcontextprotocol/inspector python -m your_server_module

# Node.js sunucusu
npx @modelcontextprotocol/inspector node ./build/index.js

# Ortam değişkenleri ile
OPENAI_API_KEY=xxx npx @modelcontextprotocol/inspector python server.py
```

### SSE/HTTP Sunucuları (Ağ)

HTTP servisi olarak çalışan sunucular için:

1. Önce sunucunuzu başlatın:
   ```bash
   python server.py  # Sunucu http://localhost:8080 adresinde çalışıyor
   ```

2. Inspector'u başlatıp bağlanın:
   ```bash
   npx @modelcontextprotocol/inspector --sse http://localhost:8080/sse
   ```

---

## Inspector Arayüzü Genel Bakış

Inspector açıldığında, genellikle `http://localhost:5173` adresinde bir web arayüzü görürsünüz:

```
┌─────────────────────────────────────────────────────────────┐
│  MCP Inspector                              [Connected ✅]   │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐         │
│  │   🔧 Tools  │  │ 📄 Resources│  │ 💬 Prompts  │         │
│  │    (3)      │  │    (2)      │  │    (1)      │         │
│  └─────────────┘  └─────────────┘  └─────────────┘         │
│                                                             │
│  ┌───────────────────────────────────────────────────────┐ │
│  │  📋 Message Log                                       │ │
│  │  ─────────────────────────────────────────────────── │ │
│  │  → initialize                                         │ │
│  │  ← initialized (server info)                          │ │
│  │  → tools/list                                         │ │
│  │  ← tools (3 tools)                                    │ │
│  └───────────────────────────────────────────────────────┘ │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## Araçları Test Etme

### Kullanılabilir Araçları Listeleme

1. **Tools** sekmesine tıklayın
2. Inspector otomatik olarak `tools/list` çağrısı yapar
3. Kayıtlı tüm araçları görürsünüz:
   - Araç ismi
   - Açıklama
   - Girdi şeması (parametreler)

### Bir Araç Çağırma

1. Listeden bir araç seçin
2. Formdaki gerekli parametreleri doldurun
3. **Run Tool** butonuna tıklayın
4. Sonuçlar panelinde yanıtı görün

**Örnek: Bir hesap makinesi aracını test etmek**

```
Tool: add
Parameters:
  a: 25
  b: 17

Response:
{
  "content": [
    {
      "type": "text",
      "text": "42"
    }
  ]
}
```

### Araç Hatalarını Ayıklama

Bir araç başarısız olduğunda, Inspector şunları gösterir:

```
Error Response:
{
  "error": {
    "code": -32602,
    "message": "Invalid params: 'b' is required"
  }
}
```

Yaygın hata kodları:
| Kod | Anlamı |
|------|---------|
| -32700 | Ayrıştırma hatası (geçersiz JSON) |
| -32600 | Geçersiz istek |
| -32601 | Yöntem bulunamadı |
| -32602 | Geçersiz parametreler |
| -32603 | Dahili hata |

---

## Kaynakları Test Etme

### Kaynakları Listeleme

1. **Resources** sekmesine tıklayın
2. Inspector `resources/list` çağrısını yapar
3. Şunları görürsünüz:
   - Kaynak URI'leri
   - İsimler ve açıklamalar
   - MIME türleri

### Bir Kaynağı Okuma

1. Bir kaynak seçin
2. **Read Resource** butonuna tıklayın
3. Dönen içeriği görüntüleyin

**Örnek çıktı:**

```
Resource: file:///config/settings.json
Content-Type: application/json

{
  "config": {
    "debug": true,
    "maxConnections": 10
  }
}
```

---

## Prompts Testi

### Prompts Listesi

1. **Prompts** sekmesine tıklayın
2. Inspector `prompts/list` çağrısı yapar
3. Mevcut prompt şablonlarını görüntüleyin

### Prompt Alma

1. Bir prompt seçin
2. Gereken argümanları doldurun
3. **Get Prompt** butonuna tıklayın
4. Oluşturulan prompt mesajlarını görün

---

## Mesaj Kaydı Analizi

Mesaj kaydı tüm MCP protokol mesajlarını gösterir. Aşağıdaki döküm, eski bir
`2025-11-25` sunucusundan ve kaldırılmış `initialize` el sıkışmasını içerir. Bir
`2026-07-28` sunucusu ise kendi içinde isteğe ait meta veriler ve
`server/discover` kullanır.

```
14:32:01 → {"jsonrpc":"2.0","id":1,"method":"initialize",...}
14:32:01 ← {"jsonrpc":"2.0","id":1,"result":{"protocolVersion":"2025-11-25",...}}
14:32:02 → {"jsonrpc":"2.0","id":2,"method":"tools/list"}
14:32:02 ← {"jsonrpc":"2.0","id":2,"result":{"tools":[...]}}
14:32:05 → {"jsonrpc":"2.0","id":3,"method":"tools/call","params":{"name":"add",...}}
14:32:05 ← {"jsonrpc":"2.0","id":3,"result":{"content":[...]}}
```

### Nelere Dikkat Edilmeli

- **İstek/Yanıt çiftleri**: Her `→` karşılık gelen bir `←` olmalı
- **Hata mesajları**: Yanıtlarda `"error"` arayın
- **Zamanlama**: Büyük boşluklar performans sorunlarına işaret edebilir
- **Protokol sürümü**: Sunucu ve istemcinin sürüm üzerinde anlaşmış olması gerekir

---

## VS Code Entegrasyonu

Inspector'u doğrudan VS Code'dan çalıştırabilirsiniz:

### launch.json Kullanımı

`.vscode/launch.json` dosyasına ekleyin:

```json
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "Debug with MCP Inspector",
      "type": "node",
      "request": "launch",
      "runtimeExecutable": "npx",
      "runtimeArgs": [
        "@modelcontextprotocol/inspector",
        "python",
        "${workspaceFolder}/server.py"
      ],
      "console": "integratedTerminal"
    },
    {
      "name": "Debug SSE Server with Inspector",
      "type": "chrome",
      "request": "launch",
      "url": "http://localhost:5173",
      "preLaunchTask": "Start MCP Inspector"
    }
  ]
}
```

### Görevler (Tasks) Kullanımı

`.vscode/tasks.json` dosyasına ekleyin:

```json
{
  "version": "2.0.0",
  "tasks": [
    {
      "label": "Start MCP Inspector",
      "type": "shell",
      "command": "npx @modelcontextprotocol/inspector node ${workspaceFolder}/build/index.js",
      "isBackground": true,
      "problemMatcher": {
        "pattern": {
          "regexp": "^$"
        },
        "background": {
          "activeOnStart": true,
          "beginsPattern": "Inspector",
          "endsPattern": "listening"
        }
      }
    }
  ]
}
```

---

## Yaygın Hata Ayıklama Senaryoları

### Senaryo 1: Sunucu Bağlanmıyor

**Belirtiler:** Inspector "Disconnected" gösterir veya "Connecting..." kısmında takılır

**Kontrol Listesi:**
1. ✅ Sunucu komutu doğru mu?
2. ✅ Tüm bağımlılıklar yüklü mü?
3. ✅ Sunucu yolu mutlak mı yoksa geçerli dizine göre mi?
4. ✅ Gerekli ortam değişkenleri ayarlı mı?

**Hata ayıklama adımları:**
```bash
# Önce sunucuyu manuel olarak test edin
python -c "import your_server_module; print('OK')"

# İçe aktarma hatalarını kontrol edin
python -m your_server_module 2>&1 | head -20

# MCP SDK'nın yüklü olduğunu doğrulayın
pip show mcp
```

### Senaryo 2: Araçlar Görünmüyor

**Belirtiler:** Tools sekmesi boş liste gösterir

**Olası nedenler:**
1. Sunucu başlatılırken araçlar kayıtlı değil
2. Sunucu başlatıldıktan sonra çöktü
3. `tools/list` işleyicisi boş dizi döndürüyor

**Hata ayıklama adımları:**
1. Mesaj kaydını `tools/list` yanıtı için kontrol edin
2. Araç kayıt kodunuza logging ekleyin
3. `@mcp.tool()` dekoratörlerinin varlığını doğrulayın (Python)

### Senaryo 3: Araç Hata Dönüyor

**Belirtiler:** Araç çağrısı hata yanıtı döndürüyor

**Hata ayıklama yaklaşımı:**
1. Hata mesajını dikkatlice okuyun
2. Parametre tiplerinin şema ile uyuştuğundan emin olun
3. Ayrıntılı hata mesajları için try/catch ekleyin
4. Yığın izleri için sunucu günlüklerini kontrol edin

**Geliştirilmiş hata yönetimi örneği:**

```python
@mcp.tool()
async def my_tool(param1: str, param2: int) -> str:
    try:
        # Araç mantığı burada
        result = process(param1, param2)
        return str(result)
    except ValueError as e:
        raise McpError(f"Invalid parameter: {e}")
    except Exception as e:
        raise McpError(f"Tool failed: {type(e).__name__}: {e}")
```

### Senaryo 4: Kaynak İçeriği Boş

**Belirtiler:** Kaynak döner ama içerik boş veya null

**Kontrol Listesi:**
1. ✅ Dosya yolu veya URI doğru mu?
2. ✅ Sunucunun kaynağı okuma izni var mı?
3. ✅ Kaynak içeriği doğru şekilde döndürülüyor mu?

---

## Gelişmiş Inspector Özellikleri

### Özel Başlıklar (SSE)

```bash
npx @modelcontextprotocol/inspector \
  --sse http://localhost:8080/sse \
  --header "Authorization: Bearer your-token"
```

### Ayrıntılı Kayıt Tutma

```bash
DEBUG=mcp* npx @modelcontextprotocol/inspector python server.py
```

### Oturum Kaydetme

Inspector, mesaj kayıtlarını daha sonra analiz için dışa aktarabilir:
1. Mesaj panelinde **Export Log** butonuna tıklayın
2. JSON dosyasını kaydedin
3. Hata ayıklama için ekip üyeleriyle paylaşın

---


## En İyi Uygulamalar

1. **Erken ve sık test edin** - Inspector'ı sadece hatalar oluştuğunda değil, geliştirme sırasında kullanın
2. **Basitten başlayın** - Karmaşık araç çağrılarından önce temel bağlantıyı test edin
3. **Şemayı kontrol edin** - Birçok hata parametre türü uyumsuzluklarından kaynaklanır
4. **Hata mesajlarını okuyun** - MCP hataları genellikle açıklayıcıdır
5. **Inspector'ı açık tutun** - Geliştirme sırasında sorunları yakalamanıza yardımcı olur

---

## Sonraki Adımlar

Modül 3: Başlarken tamamladınız! Öğrenmeye devam edin:

- [Modül 4: Pratik Uygulama](../../04-PracticalImplementation/README.md)

---

## Ek Kaynaklar

- [MCP Inspector GitHub Deposu](https://github.com/modelcontextprotocol/inspector)
- [MCP Spesifikasyonu - Protokol Mesajları](https://modelcontextprotocol.io/specification/2026-07-28/)
- [JSON-RPC 2.0 Spesifikasyonu](https://www.jsonrpc.org/specification)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Feragatname**:
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba sarf etsek de, otomatik çevirilerin hata veya yanlışlık içerebileceğini lütfen unutmayınız. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu ortaya çıkabilecek yanlış anlamalardan veya yanlış yorumlamalardan sorumlu değiliz.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->