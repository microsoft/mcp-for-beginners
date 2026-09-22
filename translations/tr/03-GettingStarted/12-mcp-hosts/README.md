# Popüler MCP Host İstemcilerinin Kurulumu

> [!NOTE]
> `/sse` adresine işaret eden host yapılandırmaları MCP `2025-11-25` için eski HTTP+SSE örnekleridir. MCP `2026-07-28` için, destekleyen hostlarda Streamable HTTP seçin ve sunucu tarafından yapılandırılan uç noktayı kullanın.
> 
> 

Bu rehber, popüler AI host uygulamaları ile MCP sunucularını nasıl yapılandıracağınızı ve kullanacağınızı anlatır. Her bir hostun kendine özgü bir yapılandırma yöntemi vardır, ancak kurulduktan sonra hepsi standartlaştırılmış protokolü kullanarak MCP sunucularıyla iletişim kurar.

## MCP Host Nedir?

**MCP Host**, yeteneklerini genişletmek için MCP sunucularına bağlanabilen bir AI uygulamasıdır. Bunu, kullanıcıların etkileşimde bulunduğu "ön yüz" olarak, MCP sunucularının ise "arka uç" araçlar ve veriler sağladığı yer olarak düşünebilirsiniz.

```mermaid
flowchart LR
    User[👤 Kullanıcı] --> Host[🖥️ MCP Ana Bilgisayarı]
    Host --> S1[MCP Sunucusu A]
    Host --> S2[MCP Sunucusu B]
    Host --> S3[MCP Sunucusu C]
    
    subgraph "Popüler Ana Bilgisayarlar"
        H1[Claude Masaüstü]
        H2[VS Code]
        H3[İmleç]
        H4[Cline]
        H5[Windsurf]
    end
```

## Önkoşullar

- Bağlanılacak bir MCP sunucusu (bkz. [Modül 3.1 - İlk Sunucu](../01-first-server/README.md))
- Sisteminizde yüklü olan host uygulaması
- JSON yapılandırma dosyalarına temel aşinalık

---

## 1. Claude Desktop

**Claude Desktop**, Anthropic'in yerel olarak MCP'yi destekleyen resmi masaüstü uygulamasıdır.

### Kurulum

1. Claude Desktop'ı [claude.ai/download](https://claude.ai/download) adresinden indirin
2. Kurun ve Anthropic hesabınızla giriş yapın

### Yapılandırma

Claude Desktop, MCP sunucularını tanımlamak için bir JSON yapılandırma dosyası kullanır.

**Yapılandırma dosyasının yeri:**
- **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
- **Windows**: `%APPDATA%\Claude\claude_desktop_config.json`
- **Linux**: `~/.config/Claude/claude_desktop_config.json`

**Örnek yapılandırma:**

```json
{
  "mcpServers": {
    "calculator": {
      "command": "python",
      "args": ["-m", "mcp_calculator_server"],
      "env": {
        "PYTHONPATH": "/path/to/your/server"
      }
    },
    "weather": {
      "command": "node",
      "args": ["/path/to/weather-server/build/index.js"]
    },
    "database": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-postgres"],
      "env": {
        "DATABASE_URL": "postgresql://user:pass@localhost/mydb"
      }
    }
  }
}
```

### Yapılandırma Seçenekleri

| Alan | Açıklama | Örnek |
|-------|-------------|---------|
| `command` | Çalıştırılacak yürütülebilir dosya | `"python"`, `"node"`, `"npx"` |
| `args` | Komut satırı argümanları | `["-m", "my_server"]` |
| `env` | Ortam değişkenleri | `{"API_KEY": "xxx"}` |
| `cwd` | Çalışma dizini | `"/path/to/server"` |

### Kurulumunuzu Test Etme

1. Yapılandırma dosyasını kaydedin
2. Claude Desktop'ı tamamen yeniden başlatın (kapatıp tekrar açın)
3. Yeni bir konuşma açın
4. Bağlı sunucuları gösteren 🔌 simgesini arayın
5. Claude'dan araçlarınızdan birini kullanmasını isteyin

### Claude Desktop Sorun Giderme

**Sunucu görünmüyorsa:**
- Yapılandırma dosyası sözdizimini bir JSON doğrulayıcı ile kontrol edin
- Komut yolu doğru olduğundan emin olun
- Claude Desktop günlüklerini kontrol edin: Yardım → Günlükleri Göster

**Sunucu başlangıçta çökerse:**
- Sunucunuzu önce terminalde manuel olarak test edin
- Ortam değişkenlerinin doğru ayarlandığını kontrol edin
- Tüm bağımlılıkların kurulu olduğundan emin olun

---

## 2. VS Code ile GitHub Copilot

VS Code, GitHub Copilot Chat uzantıları aracılığıyla MCP'yi destekler.

### Önkoşullar

1. VS Code 1.99+ kurulu
2. GitHub Copilot uzantısı kurulu
3. GitHub Copilot Chat uzantısı kurulu

### Yapılandırma

VS Code, çalışma alanınızda veya kullanıcı ayarlarında `.vscode/mcp.json` dosyasını kullanır.

**Çalışma alanı yapılandırması** (`.vscode/mcp.json`):


```json
{
  "servers": {
    "my-calculator": {
      "type": "stdio",
      "command": "python",
      "args": ["-m", "mcp_calculator_server"]
    },
    "my-database": {
      "type": "sse",
      "url": "http://localhost:8080/sse"
    }
  }
}
```

**Kullanıcı ayarları** (`settings.json`):

```json
{
  "mcp.servers": {
    "global-server": {
      "type": "stdio",
      "command": "npx",
      "args": ["-y", "@anthropic/mcp-server-memory"]
    }
  },
  "mcp.enableLogging": true
}
```

### VS Code'da MCP kullanımı

1. Copilot Sohbet panelini açın (Ctrl+Shift+I / Cmd+Shift+I)
2. Kullanılabilir MCP araçlarını görmek için `@` yazın
3. Araçları çağırmak için doğal dil kullanın: "Kalkülatör kullanarak 25 * 48 hesapla"

### VS Code sorun giderme

**MCP sunucuları yüklenmiyor:**
- Hata kayıtları için Çıktı panelini → "MCP" kontrol edin
- Pencereyi yeniden yükleyin: Ctrl+Shift+P → "Geliştirici: Pencereyi Yeniden Yükle"
- İlk önce sunucunun bağımsız çalıştığını doğrulayın

---

## 3. Cursor

**Cursor** yerleşik MCP desteği olan yapay zeka öncelikli bir kod editörüdür.

### Kurulum

1. Cursor'ı [cursor.sh](https://cursor.sh) üzerinden indirin
2. Kurun ve oturum açın

### Konfigürasyon

Cursor, Claude Desktop ile benzer bir konfigürasyon formatı kullanır.

**Konfigürasyon dosyası konumu:**
- **macOS**: `~/.cursor/mcp.json`
- **Windows**: `%USERPROFILE%\.cursor\mcp.json`
- **Linux**: `~/.cursor/mcp.json`

**Örnek konfigürasyon:**

```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "/path/to/allowed/directory"]
    },
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_TOKEN": "ghp_your_token_here"
      }
    }
  }
}
```

### Cursor'da MCP kullanımı

1. Cursor'ın Yapay Zeka sohbetini açın (Ctrl+L / Cmd+L)
2. MCP araçları önerilerde otomatik olarak görünür
3. Bağlı sunucuları kullanarak Yapay Zekadan görev yapmasını isteyin

---

## 4. Cline (Terminal Tabanlı)

**Cline**, komut satırı iş akışları için ideal terminal tabanlı bir MCP istemcisidir.

### Kurulum

```bash
npm install -g @anthropic/cline
```

### Konfigürasyon

Cline, çevre değişkenleri ve komut satırı argümanlarını kullanır.

**Çevre değişkenleri kullanımı:**

```bash
export ANTHROPIC_API_KEY="your-api-key"
export MCP_SERVER_CALCULATOR="python -m mcp_calculator_server"
```

**Komut satırı argümanları kullanımı:**

```bash
cline --mcp-server "calculator:python -m mcp_calculator_server" \
      --mcp-server "weather:node /path/to/weather/index.js"
```

**Konfigürasyon dosyası** (`~/.clinerc`):

```json
{
  "apiKey": "your-api-key",
  "mcpServers": {
    "calculator": {
      "command": "python",
      "args": ["-m", "mcp_calculator_server"]
    }
  }
}
```

### Cline kullanımı

```bash
# Etkileşimli bir oturum başlat
cline

# MCP ile tek sorgu
cline "Calculate the square root of 144 using the calculator"

# Mevcut araçları listele
cline --list-tools
```

---

## 5. Windsurf

**Windsurf**, MCP desteği olan başka bir yapay zeka destekli kod editörüdür.

### Kurulum

1. Windsurf'u [codeium.com/windsurf](https://codeium.com/windsurf) adresinden indirin
2. Kurun ve bir hesap oluşturun

### Konfigürasyon

Windsurf konfigürasyonu ayarlar kullanıcı arayüzü üzerinden yönetilir:

1. Ayarları açın (Ctrl+, / Cmd+,)
2. "MCP" için arama yapın
3. "settings.json içinde düzenle"ye tıklayın

**Örnek konfigürasyon:**

```json
{
  "windsurf.mcp.servers": {
    "my-tools": {
      "command": "python",
      "args": ["/path/to/server.py"],
      "env": {}
    }
  },
  "windsurf.mcp.enabled": true
}
```

---

## Taşıma Türleri Karşılaştırması

Farklı sunucular farklı taşıma mekanizmalarını destekler:

| Sunucu | stdio | SSE/HTTP | WebSocket |
|------|-------|----------|-----------|
| Claude Desktop | ✅ | ❌ | ❌ |
| VS Code | ✅ | ✅ | ❌ |
| Cursor | ✅ | ✅ | ❌ |
| Cline | ✅ | ✅ | ❌ |
| Windsurf | ✅ | ✅ | ❌ |

**stdio** (standart giriş/çıkış): Sunucunun ev sahibi tarafından yerel olarak başlatılması için en iyisi
**SSE/HTTP**: Uzak sunucular veya birden fazla istemci arasında paylaşılan sunucular için en iyisi

---

## Yaygın Sorun Giderme

### Sunucu başlamıyor

1. **Önce sunucuyu manuel olarak test edin:**
   ```bash
   # Python için
   python -m your_server_module
   
   # Node.js için
   node /path/to/server/index.js
   ```

2. **Komut yolunu kontrol edin:**

   - Mümkün olduğunda mutlak yolları kullanın
   - Yürütülebilir dosyanın PATH'inizde olduğundan emin olun

3. **Bağımlılıkları doğrulayın:**
   ```bash
   # Python
   pip list | grep mcp
   
   # Node.js
   npm list @modelcontextprotocol/sdk
   ```

### Sunucu bağlanıyor ama araçlar çalışmıyor

1. **Sunucu günlüklerini kontrol edin** - Çoğu barındırıcı günlükleme seçeneklerine sahiptir
2. **Araç kaydını doğrulayın** - Test etmek için MCP Inspector'ı kullanın
3. **İzinleri kontrol edin** - Bazı araçlar dosya/ağ erişimi gerektirir

### Ortam değişkenleri iletilmiyor

- Bazı barındırıcılar ortam değişkenlerini temizler
- `env` yapılandırma alanını açıkça kullanın
- Yapılandırma dosyalarında hassas verilerden kaçının (gizli yönetimi kullanın)

---

## Güvenlik En İyi Uygulamaları

1. **API anahtarlarını asla** yapılandırma dosyalarına göndermeyin
2. **Hassas veriler için ortam değişkenlerini kullanın**
3. **Sunucu izinlerini yalnızca gerekenle sınırlayın**
4. **Sisteminize erişim vermeden önce sunucu kodunu gözden geçirin**
5. **Dosya sistemi ve ağ erişimi için izin listelerini kullanın**

---

## Sırada Ne Var

- [3.13 - MCP Inspector ile Hata Ayıklama](../13-mcp-inspector/README.md)
- [3.1 - İlk MCP sunucunuzu oluşturun](../01-first-server/README.md)
- [Modül 5 - İleri Konular](../../05-AdvancedTopics/README.md)

---

## Ekstra Kaynaklar

- [Claude Masaüstü MCP Dokümantasyonu](https://docs.anthropic.com/en/docs/claude-desktop/mcp)
- [VS Code MCP Uzantısı](https://marketplace.visualstudio.com/items?itemName=anthropic.claude-mcp)
- [MCP Spesifikasyonu - Taşıyıcılar](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/)
- [Resmi MCP Sunucuları Kaydı](https://github.com/modelcontextprotocol/servers)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Feragatname**:
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba sarf etsek de, otomatik çevirilerin hata veya yanlışlık içerebileceğini lütfen unutmayınız. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu ortaya çıkabilecek yanlış anlamalardan veya yanlış yorumlamalardan sorumlu değiliz.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->