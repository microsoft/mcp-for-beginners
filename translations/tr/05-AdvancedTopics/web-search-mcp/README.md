# Ders: Web Arama MCP Sunucusu Oluşturma

Bu bölüm, dış API'lerle entegrasyon sağlayan, çeşitli veri türlerini işleyen, hata yönetimi yapan ve birden fazla aracı koordine eden gerçek dünya yapay zeka ajanı oluşturmayı gösterir—hepsi üretime hazır bir formatta. Şunları göreceksiniz:

- **Kimlik doğrulama gerektiren dış API entegrasyonu**
- **Birden fazla uç noktadan gelen çeşitli veri türlerinin işlenmesi**
- **Sağlam hata yönetimi ve kayıt stratejileri**
- **Tek bir sunucuda çoklu araç koordinasyonu**

Bölüm sonunda, gelişmiş yapay zeka ve LLM destekli uygulamalar için gerekli olan kalıplar ve en iyi uygulamalar konusunda pratik deneyime sahip olacaksınız.

## Giriş

Bu derste, SerpAPI kullanarak gerçek zamanlı web verisiyle LLM yeteneklerini genişleten gelişmiş bir MCP sunucusu ve istemcisi nasıl oluşturulur öğreneceksiniz. Bu, web’den güncel bilgilere erişebilen dinamik yapay zeka ajanları geliştirmek için kritik bir beceridir.

## Öğrenme Hedefleri

Bu dersin sonunda şunları yapabileceksiniz:

- Dış API’leri (örneğin SerpAPI) güvenli şekilde MCP sunucusuna entegre etmek
- Web, haber, ürün arama ve Soru-Cevap için birden fazla araç uygulamak
- Yapılandırılmış verileri LLM tüketimi için ayrıştırmak ve biçimlendirmek
- Hataları yönetmek ve API hız sınırlarını etkili şekilde kontrol etmek
- Hem otomatik hem de etkileşimli MCP istemcileri oluşturup test etmek

## Web Arama MCP Sunucusu

Bu bölüm, Web Arama MCP Sunucusunun mimarisini ve özelliklerini tanıtır. FastMCP ve SerpAPI’nin birlikte nasıl kullanıldığını, LLM yeteneklerini gerçek zamanlı web verisiyle nasıl genişlettiğini göreceksiniz.

### Genel Bakış

Bu uygulama, MCP’nin çeşitli, dış API tabanlı görevleri güvenli ve verimli şekilde yönetme yeteneğini gösteren dört aracı içerir:

- **general_search**: Geniş kapsamlı web sonuçları için
- **news_search**: Güncel haber başlıkları için
- **product_search**: E-ticaret verileri için
- **qna**: Soru-cevap parçacıkları için

### Özellikler
- **Kod Örnekleri**: Python için (ve kolayca diğer dillere genişletilebilir) dil özelinde kod blokları, açıklık için kod pivotları kullanılarak

### Python

```python
# Example usage of the general_search tool
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def run_search():
    server_params = StdioServerParameters(
        command="python",
        args=["server.py"],
    )
    async with stdio_client(server_params) as (reader, writer):
        async with ClientSession(reader, writer) as session:
            await session.initialize()
            result = await session.call_tool("general_search", arguments={"query": "open source LLMs"})
            print(result)
```

---

İstemciyi çalıştırmadan önce, sunucunun ne yaptığını anlamak faydalıdır. [`server.py`](../../../../05-AdvancedTopics/web-search-mcp/server.py) dosyası, MCP sunucusunu uygular; SerpAPI ile entegrasyon sağlayarak web, haber, ürün arama ve Soru-Cevap araçlarını sunar. Gelen istekleri işler, API çağrılarını yönetir, yanıtları ayrıştırır ve yapılandırılmış sonuçları istemciye döner.

Tam uygulamayı [`server.py`](../../../../05-AdvancedTopics/web-search-mcp/server.py) dosyasında inceleyebilirsiniz.

İşte sunucunun bir aracı nasıl tanımlayıp kaydettiğine dair kısa bir örnek:

### Python Sunucu

```python
# server.py (excerpt)
from mcp.server import MCPServer, Tool

async def general_search(query: str):
    # ...implementation...

server = MCPServer()
server.add_tool(Tool("general_search", general_search))

if __name__ == "__main__":
    server.run()
```

---

- **Dış API Entegrasyonu**: API anahtarlarının ve dış isteklerin güvenli yönetimini gösterir
- **Yapılandırılmış Veri Ayrıştırma**: API yanıtlarını LLM dostu formatlara dönüştürme yöntemini gösterir
- **Hata Yönetimi**: Uygun kayıtlarla sağlam hata yönetimi
- **Etkileşimli İstemci**: Hem otomatik testler hem de etkileşimli mod içerir
- **Bağlam Yönetimi**: MCP Context kullanarak kayıt ve istek takibi yapar

## Ön Koşullar

Başlamadan önce, ortamınızın düzgün kurulduğundan emin olun. Bu, tüm bağımlılıkların yüklendiğini ve API anahtarlarınızın doğru yapılandırıldığını garantiler, böylece geliştirme ve test sorunsuz olur.

- Python 3.8 veya üzeri
- SerpAPI API Anahtarı (Kayıt için [SerpAPI](https://serpapi.com/) - ücretsiz katman mevcut)

## Kurulum

Ortamınızı kurmak için şu adımları izleyin:

1. Bağımlılıkları uv (önerilen) veya pip ile yükleyin:

```bash
# Using uv (recommended)
uv pip install -r requirements.txt

# Using pip
pip install -r requirements.txt
```

2. Proje kök dizininde SerpAPI anahtarınızı içeren bir `.env` dosyası oluşturun:

```
SERPAPI_KEY=your_serpapi_key_here
```

## Kullanım

Web Arama MCP Sunucusu, SerpAPI ile entegrasyon sağlayarak web, haber, ürün arama ve Soru-Cevap araçlarını sunan temel bileşendir. Gelen istekleri işler, API çağrılarını yönetir, yanıtları ayrıştırır ve yapılandırılmış sonuçları istemciye döner.

Tam uygulamayı [`server.py`](../../../../05-AdvancedTopics/web-search-mcp/server.py) dosyasında inceleyebilirsiniz.

### Sunucuyu Çalıştırma

MCP sunucusunu başlatmak için şu komutu kullanın:

```bash
python server.py
```

Sunucu, istemcinin doğrudan bağlanabileceği stdio tabanlı bir MCP sunucusu olarak çalışacaktır.

### İstemci Modları

İstemci (`client.py`), MCP sunucusuyla etkileşim için iki modu destekler:

- **Normal mod**: Tüm araçları test eden ve yanıtlarını doğrulayan otomatik testleri çalıştırır. Sunucu ve araçların beklendiği gibi çalıştığını hızlıca kontrol etmek için kullanışlıdır.
- **Etkileşimli mod**: Menü tabanlı bir arayüz başlatır; burada araçları manuel seçip çağırabilir, özel sorgular girebilir ve sonuçları gerçek zamanlı görebilirsiniz. Sunucunun yeteneklerini keşfetmek ve farklı girdilerle denemeler yapmak için idealdir.

Tam uygulamayı [`client.py`](../../../../05-AdvancedTopics/web-search-mcp/client.py) dosyasında inceleyebilirsiniz.

### İstemciyi Çalıştırma

Otomatik testleri çalıştırmak için (bu sunucuyu otomatik başlatır):

```bash
python client.py
```

Ya da etkileşimli modda çalıştırmak için:

```bash
python client.py --interactive
```

### Farklı Yöntemlerle Test Etme

İhtiyaçlarınıza ve iş akışınıza bağlı olarak, sunucunun sağladığı araçları test etmek ve onlarla etkileşimde bulunmak için çeşitli yollar vardır.

#### MCP Python SDK ile Özel Test Scriptleri Yazma
Kendi test scriptlerinizi MCP Python SDK kullanarak da oluşturabilirsiniz:

# [Python](../../../../05-AdvancedTopics/web-search-mcp)

```python
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def test_custom_query():
    server_params = StdioServerParameters(
        command="python",
        args=["server.py"],
    )
    
    async with stdio_client(server_params) as (reader, writer):
        async with ClientSession(reader, writer) as session:
            await session.initialize()
            # Call tools with your custom parameters
            result = await session.call_tool("general_search", 
                                           arguments={"query": "your custom query"})
            # Process the result
```

---

Bu bağlamda "test scripti", MCP sunucusuna istemci olarak davranan kendi yazdığınız özel bir Python programı anlamına gelir. Resmi bir birim testi olmaktan ziyade, bu script sunucuya programatik olarak bağlanmanızı, istediğiniz parametrelerle araçları çağırmanızı ve sonuçları incelemenizi sağlar. Bu yaklaşım şunlar için faydalıdır:
- Araç çağrılarını prototiplemek ve denemek
- Sunucunun farklı girdilere nasıl yanıt verdiğini doğrulamak
- Tekrarlayan araç çağrılarını otomatikleştirmek
- MCP sunucusu üzerinde kendi iş akışlarınızı veya entegrasyonlarınızı oluşturmak

Test scriptleri, yeni sorguları hızlıca denemek, araç davranışlarını hata ayıklamak veya daha gelişmiş otomasyonlar için başlangıç noktası olarak kullanılabilir. Aşağıda MCP Python SDK kullanarak böyle bir script oluşturma örneği verilmiştir:

## Araç Açıklamaları

Sunucunun sağladığı aşağıdaki araçları farklı arama ve sorgu türleri için kullanabilirsiniz. Her araç, parametreleri ve örnek kullanımıyla birlikte aşağıda açıklanmıştır.

Bu bölüm, mevcut her aracın detayları ve parametreleri hakkında bilgi verir.

### general_search

Genel bir web araması yapar ve biçimlendirilmiş sonuçlar döner.

**Bu aracı nasıl çağırabilirsiniz:**

`general_search` aracını kendi scriptinizden MCP Python SDK ile veya Inspector ya da etkileşimli istemci modunda kullanabilirsiniz. İşte SDK ile bir kod örneği:

# [Python Örneği](../../../../05-AdvancedTopics/web-search-mcp)

```python
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def run_general_search():
    server_params = StdioServerParameters(
        command="python",
        args=["server.py"],
    )
    async with stdio_client(server_params) as (reader, writer):
        async with ClientSession(reader, writer) as session:
            await session.initialize()
            result = await session.call_tool("general_search", arguments={"query": "latest AI trends"})
            print(result)
```

---

Alternatif olarak, etkileşimli modda menüden `general_search` seçip sorgunuzu girebilirsiniz.

**Parametreler:**
- `query` (string): Arama sorgusu

**Örnek İstek:**

```json
{
  "query": "latest AI trends"
}
```

### news_search

Bir sorguyla ilgili güncel haber makalelerini arar.

**Bu aracı nasıl çağırabilirsiniz:**

`news_search` aracını kendi scriptinizden MCP Python SDK ile veya Inspector ya da etkileşimli istemci modunda kullanabilirsiniz. İşte SDK ile bir kod örneği:

# [Python Örneği](../../../../05-AdvancedTopics/web-search-mcp)

```python
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def run_news_search():
    server_params = StdioServerParameters(
        command="python",
        args=["server.py"],
    )
    async with stdio_client(server_params) as (reader, writer):
        async with ClientSession(reader, writer) as session:
            await session.initialize()
            result = await session.call_tool("news_search", arguments={"query": "AI policy updates"})
            print(result)
```

---

Alternatif olarak, etkileşimli modda menüden `news_search` seçip sorgunuzu girebilirsiniz.

**Parametreler:**
- `query` (string): Arama sorgusu

**Örnek İstek:**

```json
{
  "query": "AI policy updates"
}
```

### product_search

Bir sorguya uygun ürünleri arar.

**Bu aracı nasıl çağırabilirsiniz:**

`product_search` aracını kendi scriptinizden MCP Python SDK ile veya Inspector ya da etkileşimli istemci modunda kullanabilirsiniz. İşte SDK ile bir kod örneği:

# [Python Örneği](../../../../05-AdvancedTopics/web-search-mcp)

```python
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def run_product_search():
    server_params = StdioServerParameters(
        command="python",
        args=["server.py"],
    )
    async with stdio_client(server_params) as (reader, writer):
        async with ClientSession(reader, writer) as session:
            await session.initialize()
            result = await session.call_tool("product_search", arguments={"query": "best AI gadgets 2025"})
            print(result)
```

---

Alternatif olarak, etkileşimli modda menüden `product_search` seçip sorgunuzu girebilirsiniz.

**Parametreler:**
- `query` (string): Ürün arama sorgusu

**Örnek İstek:**

```json
{
  "query": "best AI gadgets 2025"
}
```

### qna

Arama motorlarından doğrudan sorulara cevaplar alır.

**Bu aracı nasıl çağırabilirsiniz:**

`qna` aracını kendi scriptinizden MCP Python SDK ile veya Inspector ya da etkileşimli istemci modunda kullanabilirsiniz. İşte SDK ile bir kod örneği:

# [Python Örneği](../../../../05-AdvancedTopics/web-search-mcp)

```python
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def run_qna():
    server_params = StdioServerParameters(
        command="python",
        args=["server.py"],
    )
    async with stdio_client(server_params) as (reader, writer):
        async with ClientSession(reader, writer) as session:
            await session.initialize()
            result = await session.call_tool("qna", arguments={"question": "what is artificial intelligence"})
            print(result)
```

---

Alternatif olarak, etkileşimli modda menüden `qna` seçip sorunuz girildiğinde cevabı alabilirsiniz.

**Parametreler:**
- `question` (string): Cevap aranacak soru

**Örnek İstek:**

```json
{
  "question": "what is artificial intelligence"
}
```

## Kod Detayları

Bu bölüm, sunucu ve istemci uygulamalarına ait kod parçacıkları ve referanslar içerir.

# [Python](../../../../05-AdvancedTopics/web-search-mcp)

Tam uygulama detayları için [`server.py`](../../../../05-AdvancedTopics/web-search-mcp/server.py) ve [`client.py`](../../../../05-AdvancedTopics/web-search-mcp/client.py) dosyalarına bakabilirsiniz.

```python
# Example snippet from server.py:
import os
import httpx
# ...existing code...
```

---

## Bu Derste İleri Düzey Kavramlar

Başlamadan önce, bu bölüm boyunca karşınıza çıkacak bazı önemli ileri düzey kavramlar şunlardır. Bunları anlamak, takip etmenizi kolaylaştıracaktır, özellikle yenilseniz bile:

- **Çoklu Araç Koordinasyonu**: Bu, bir MCP sunucusunda web arama, haber arama, ürün arama ve Soru-Cevap gibi farklı araçların aynı anda çalıştırılması demektir. Sunucunuzun sadece tek bir görev değil, çeşitli görevleri yönetmesini sağlar.
- **API Hız Sınırı Yönetimi**: Birçok dış API (örneğin SerpAPI), belirli bir zaman diliminde yapabileceğiniz istek sayısını sınırlar. İyi kod, bu sınırları kontrol eder ve aşılması durumunda uygulamanın çökmesini önleyecek şekilde davranır.
- **Yapılandırılmış Veri Ayrıştırma**: API yanıtları genellikle karmaşık ve iç içe geçmiş olur. Bu kavram, bu yanıtları LLM’ler veya diğer programlar için temiz ve kullanımı kolay formatlara dönüştürmeyi ifade eder.
- **Hata Kurtarma**: Bazen işler yolunda gitmez—örneğin ağ bağlantısı kopabilir veya API beklenen yanıtı vermez. Hata kurtarma, kodunuzun bu sorunları yönetip faydalı geri bildirim sağlaması, çökmeden devam etmesi anlamına gelir.
- **Parametre Doğrulama**: Araçlarınıza gelen tüm girdilerin doğru ve güvenli olduğundan emin olmakla ilgilidir. Varsayılan değerler belirlemek ve tür kontrolleri yapmak, hataları ve karışıklıkları önlemeye yardımcı olur.

Bu bölüm, Web Arama MCP Sunucusuyla çalışırken karşılaşabileceğiniz yaygın sorunları teşhis edip çözmenize yardımcı olacaktır. Hata veya beklenmedik davranışla karşılaşırsanız, bu sorun giderme bölümü en yaygın problemler için çözümler sunar. Daha fazla yardım aramadan önce bu ipuçlarını gözden geçirin—çoğu sorunu hızlıca çözer.

## Sorun Giderme

Web Arama MCP Sunucusuyla çalışırken zaman zaman sorunlarla karşılaşabilirsiniz—bu, dış API’lerle ve yeni araçlarla geliştirme yaparken normaldir. Bu bölüm, en yaygın sorunlara pratik çözümler sunar, böylece hızlıca yolunuza devam edebilirsiniz. Bir hata ile karşılaşırsanız, buradan başlayın: aşağıdaki ipuçları çoğu kullanıcının karşılaştığı sorunları ele alır ve genellikle ekstra yardıma gerek kalmadan problemi çözer.

### Yaygın Sorunlar

Aşağıda kullanıcıların en sık karşılaştığı sorunlar, açıklamaları ve çözüm adımları yer almaktadır:

1. **.env dosyasında SERPAPI_KEY eksik**
   - `SERPAPI_KEY environment variable not found` hatası görüyorsanız, uygulamanız SerpAPI’ye erişmek için gereken API anahtarını bulamıyor demektir. Bunu düzeltmek için, proje kök dizininde `.env` adında bir dosya oluşturun (zaten yoksa) ve içine `SERPAPI_KEY=your_serpapi_key_here` satırını ekleyin. Burada `your_serpapi_key_here` kısmını SerpAPI sitesinden aldığınız gerçek anahtarla değiştirin.

2. **Modül bulunamadı hataları**
   - `ModuleNotFoundError: No module named 'httpx'` gibi hatalar, gerekli Python paketlerinin eksik olduğunu gösterir. Genellikle tüm bağımlılıkları yüklemediğinizde olur. Bunu çözmek için terminalde `pip install -r requirements.txt` komutunu çalıştırarak projenizin ihtiyaç duyduğu tüm paketleri yükleyin.

3. **Bağlantı sorunları**
   - `Error during client execution` gibi bir hata alıyorsanız, istemci sunucuya bağlanamıyor ya da sunucu beklenildiği gibi çalışmıyor olabilir. İstemci ve sunucunun uyumlu sürümler olduğundan, `server.py` dosyasının doğru dizinde ve çalışır durumda olduğundan emin olun. Sunucu ve istemciyi yeniden başlatmak da yardımcı olabilir.

4. **SerpAPI hataları**
   - `Search API returned error status: 401` hatası, SerpAPI anahtarınızın eksik, yanlış veya süresi dolmuş olduğunu gösterir. SerpAPI kontrol panelinize gidip anahtarınızı doğrulayın ve gerekirse `.env` dosyanızı güncelleyin. Anahtar doğruysa ama hata devam ediyorsa, ücretsiz katman kotanızın dolup dolmadığını kontrol edin.

### Hata Ayıklama Modu

Varsayılan olarak, uygulama sadece önemli bilgileri kaydeder. Daha fazla detay görmek (örneğin karmaşık sorunları teşhis etmek için) isterseniz, DEBUG modunu etkinleştirebilirsiniz. Bu, uygulamanın her adımda neler yaptığını çok daha ayrıntılı gösterir.

**Örnek: Normal Çıktı**
```plaintext
2025-06-01 10:15:23,456 - __main__ - INFO - Calling general_search with params: {'query': 'open source LLMs'}
2025-06-01 10:15:24,123 - __main__ - INFO - Successfully called general_search

GENERAL_SEARCH RESULTS:
... (search results here) ...
```

**Örnek: DEBUG Çıktısı**
```plaintext
2025-06-01 10:15:23,456 - __main__ - INFO - Calling general_search with params: {'query': 'open source LLMs'}
2025-06-01 10:15:23,457 - httpx - DEBUG - HTTP Request: GET https://serpapi.com/search ...
2025-06-01 10:15:23,458 - httpx - DEBUG - HTTP Response: 200 OK ...
2025-06-01 10:15:24,123 - __main__ - INFO - Successfully called general_search

GENERAL_SEARCH RESULTS:
... (search results here) ...
```

DEBUG modunun HTTP istekleri, yanıtları ve diğer dahili detaylar hakkında ekstra satırlar içerdiğine dikkat edin. Bu, sorun giderme için çok faydalı olabilir.
DEBUG modunu etkinleştirmek için, `client.py` veya `server.py` dosyanızın en üstünde logging seviyesini DEBUG olarak ayarlayın:

# [Python](../../../../05-AdvancedTopics/web-search-mcp)

```python
# At the top of your client.py or server.py
import logging
logging.basicConfig(
    level=logging.DEBUG,  # Change from INFO to DEBUG
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
```

---

---

## Sonraki Adımlar

- [5.10 Gerçek Zamanlı Yayın](../mcp-realtimestreaming/README.md)

**Feragatname**:  
Bu belge, AI çeviri servisi [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hatalar veya yanlışlıklar içerebileceğini lütfen unutmayın. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu oluşabilecek yanlış anlamalar veya yorum hatalarından sorumlu değiliz.