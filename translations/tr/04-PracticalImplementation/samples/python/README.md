# Model Context Protocol (MCP) Python Uygulaması

Bu depo, Model Context Protocol (MCP) standardını kullanarak iletişim kuran hem sunucu hem de istemci uygulaması oluşturmayı gösteren bir Python uygulaması içerir.

## Genel Bakış

MCP uygulaması iki ana bileşenden oluşur:

1. **MCP Sunucusu (`server.py`)** - Şunları sunan bir sunucu:
   - **Araçlar**: Uzaktan çağrılabilen fonksiyonlar
   - **Kaynaklar**: Erişilebilen veriler
   - **Prompts**: Dil modelleri için prompt şablonları

2. **MCP İstemcisi (`client.py`)** - Sunucuya bağlanan ve özelliklerini kullanan bir istemci uygulaması

## Özellikler

Bu uygulama, MCP'nin birkaç temel özelliğini gösterir:

### Araçlar
- `completion` - Yapay zeka modellerinden metin tamamlama üretir (simüle edilmiş)
- `add` - İki sayıyı toplayan basit hesap makinesi

### Kaynaklar
- `models://` - Mevcut yapay zeka modelleri hakkında bilgi döner
- `greeting://{name}` - Verilen isim için kişiselleştirilmiş selamlama döner

### Prompts
- `review_code` - Kod incelemesi için prompt oluşturur

## Kurulum

Bu MCP uygulamasını kullanmak için gerekli paketleri yükleyin:

```powershell
pip install mcp-server mcp-client
```

## Sunucu ve İstemciyi Çalıştırma

### Sunucuyu Başlatma

Sunucuyu bir terminal penceresinde çalıştırın:

```powershell
python server.py
```

Sunucu, MCP CLI kullanılarak geliştirme modunda da çalıştırılabilir:

```powershell
mcp dev server.py
```

Ya da Claude Desktop’a (varsa) kurulabilir:

```powershell
mcp install server.py
```

### İstemciyi Çalıştırma

İstemciyi başka bir terminal penceresinde çalıştırın:

```powershell
python client.py
```

Bu, sunucuya bağlanacak ve mevcut tüm özellikleri gösterecektir.

### İstemci Kullanımı

İstemci (`client.py`), MCP’nin tüm yeteneklerini gösterir:

```powershell
python client.py
```

Bu, sunucuya bağlanacak ve araçlar, kaynaklar ve prompts dahil tüm özellikleri kullanacaktır. Çıktı şunları gösterecektir:

1. Hesap makinesi aracı sonucu (5 + 7 = 12)
2. "What is the meaning of life?" sorusuna completion aracı yanıtı
3. Mevcut yapay zeka modellerinin listesi
4. "MCP Explorer" için kişiselleştirilmiş selamlama
5. Kod inceleme prompt şablonu

## Uygulama Detayları

Sunucu, MCP servislerini tanımlamak için yüksek seviyeli soyutlamalar sağlayan `FastMCP` API kullanılarak uygulanmıştır. İşte araçların nasıl tanımlandığına dair basitleştirilmiş bir örnek:

```python
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers together
    
    Args:
        a: First number
        b: Second number
    
    Returns:
        The sum of the two numbers
    """
    logger.info(f"Adding {a} and {b}")
    return a + b
```

İstemci, sunucuya bağlanmak ve çağrı yapmak için MCP istemci kütüphanesini kullanır:

```python
async with stdio_client(server_params) as (reader, writer):
    async with ClientSession(reader, writer) as session:
        await session.initialize()
        result = await session.call_tool("add", arguments={"a": 5, "b": 7})
```

## Daha Fazla Bilgi

MCP hakkında daha fazla bilgi için ziyaret edin: https://modelcontextprotocol.io/

**Feragatname**:  
Bu belge, AI çeviri servisi [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba gösterilse de, otomatik çevirilerin hatalar veya yanlışlıklar içerebileceğini lütfen unutmayınız. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu ortaya çıkabilecek yanlış anlamalar veya yorum hatalarından sorumlu değiliz.