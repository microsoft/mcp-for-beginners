## Test Etme ve Hata Ayıklama

MCP sunucunuzu test etmeye başlamadan önce, kullanılabilir araçları ve hata ayıklama için en iyi uygulamaları anlamak önemlidir. Etkili test, sunucunuzun beklendiği gibi davrandığını garanti eder ve sorunları hızlıca tanımlamanıza ve çözmenize yardımcı olur. Aşağıdaki bölüm, MCP uygulamanızı doğrulamak için önerilen yaklaşımları özetlemektedir.

## Genel Bakış

Bu ders, doğru test yaklaşımının nasıl seçileceğini ve en etkili test aracını kapsar.

## Öğrenme Hedefleri

Bu dersin sonunda şu becerilere sahip olacaksınız:

- Test etme için çeşitli yaklaşımları tanımlamak.
- Kodunuzu etkili şekilde test etmek için farklı araçları kullanmak.


## MCP Sunucularını Test Etme

MCP, sunucularınızı test etmeniz ve hata ayıklamanız için araçlar sunar:

- **MCP Inspector**: Hem CLI aracı hem de görsel araç olarak çalıştırılabilen bir komut satırı aracı.
- **Manuel test**: curl gibi bir araç kullanarak web istekleri yapabilirsiniz ancak HTTP yapabilen herhangi bir araç da iş görecektir.
- **Birim testi**: Tercih ettiğiniz test framework’ünü kullanarak hem sunucu hem de istemci özelliklerini test etmek mümkündür.

### MCP Inspector Kullanımı

Bu aracın kullanımını önceki derslerde anlattık ancak biraz üst düzeyde konuşalım. Node.js ile oluşturulmuş bir araçtır ve `npx` çalıştırılabilir dosyasını çağırarak kullanabilirsiniz; bu araç kendisini geçici olarak indirir ve kurar, çalıştırma bittikten sonra temizler.

[MCP Inspector](https://github.com/modelcontextprotocol/inspector) size şu konularda yardımcı olur:

- **Sunucu Yetkinliklerini Keşfetme**: Kullanılabilir kaynaklar, araçlar ve istemleri otomatik olarak algılar
- **Araç Çalıştırmayı Test Etme**: Farklı parametreleri deneyip yanıtları gerçek zamanlı görebilirsiniz
- **Sunucu Meta Verilerini Görüntüleme**: Sunucu bilgilerini, şemalarını ve yapılandırmalarını inceleyebilirsiniz

Aracın tipik çalıştırılması şu şekildedir:

```bash
npx @modelcontextprotocol/inspector node build/index.js
```

Yukarıdaki komut bir MCP ve onun görsel arayüzünü başlatır ve tarayıcınızda yerel bir web arayüzü açar. Kaydettirdiğiniz MCP sunucularını, mevcut araçlarını, kaynaklarını ve istemlerini gösteren bir kontrol paneli görmeyi beklersiniz. Arayüz, araç çalıştırmayı etkileşimsel test etmenize, sunucu meta verilerini incelemenize ve gerçek zamanlı yanıtları görüntülemenize olanak tanır; bu da MCP sunucu uygulamalarınızı onaylamayı ve hata ayıklamayı kolaylaştırır.

Şu şekilde görünebilir: ![Inspector](../../../../translated_images/tr/connect.141db0b2bd05f096.webp)

Ayrıca bu aracı CLI modunda çalıştırabilirsiniz; bu durumda `--cli` parametresini eklersiniz. İşte sunucudaki tüm araçları listeleyen "CLI" modunda aracın çalıştırılmasına örnek:

```sh
npx @modelcontextprotocol/inspector --cli node build/index.js --method tools/list
```

### Manuel Test

Sunucu yeteneklerini test etmek için inspector aracını çalıştırmanın yanı sıra, başka benzer bir yaklaşım HTTP yapabilen bir istemci çalıştırmaktır, örneğin curl.

Curl ile MCP sunucularını HTTP istekleri ile doğrudan test edebilirsiniz:

```bash
# Örnek: Test sunucusu meta verileri
curl http://localhost:3000/v1/metadata

# Örnek: Bir aracı çalıştır
curl -X POST http://localhost:3000/v1/tools/execute \
  -H "Content-Type: application/json" \
  -d '{"name": "calculator", "parameters": {"expression": "2+2"}}'
```

Yukarıdaki curl kullanımından görebileceğiniz gibi, bir aracın adından ve parametrelerinden oluşan bir yükle POST isteği göndererek aracı çağırıyorsunuz. Kendinize en uygun olan yaklaşımı kullanın. CLI araçları genel olarak kullanımı daha hızlıdır ve betiklenmeye elverişlidir; bu da CI/CD ortamlarında faydalı olabilir.

### Birim Testi

Araçlarınız ve kaynaklarınız için beklenildiği gibi çalıştıklarından emin olmak amacıyla birim testleri oluşturun. İşte örnek test kodu.

```python
import pytest

from mcp.server.fastmcp import FastMCP
from mcp.shared.memory import (
    create_connected_server_and_client_session as create_session,
)

# Asenkron testler için tüm modülü işaretle
pytestmark = pytest.mark.anyio


async def test_list_tools_cursor_parameter():
    """Test that the cursor parameter is accepted for list_tools.

    Note: FastMCP doesn't currently implement pagination, so this test
    only verifies that the cursor parameter is accepted by the client.
    """

 server = FastMCP("test")

    # Birkaç test aracı oluştur
    @server.tool(name="test_tool_1")
    async def test_tool_1() -> str:
        """First test tool"""
        return "Result 1"

    @server.tool(name="test_tool_2")
    async def test_tool_2() -> str:
        """Second test tool"""
        return "Result 2"

    async with create_session(server._mcp_server) as client_session:
        # İmleç parametresi olmadan test (atlandı)
        result1 = await client_session.list_tools()
        assert len(result1.tools) == 2

        # cursor=None ile test et
        result2 = await client_session.list_tools(cursor=None)
        assert len(result2.tools) == 2

        # İmleç olarak string ile test et
        result3 = await client_session.list_tools(cursor="some_cursor_value")
        assert len(result3.tools) == 2

        # Boş string imleç ile test et
        result4 = await client_session.list_tools(cursor="")
        assert len(result4.tools) == 2
    
```

Yukarıdaki kod şunları yapar:

- Testleri fonksiyonlar olarak oluşturmanıza ve assert ifadeleri kullanmanıza olanak tanıyan pytest framework'ünü kullanır.
- İki farklı araç içeren bir MCP Sunucusu oluşturur.
- Belirli koşulların sağlandığını kontrol etmek için `assert` ifadesi kullanır.

[Tam dosyaya buradan bakabilirsiniz](https://github.com/modelcontextprotocol/python-sdk/blob/main/tests/client/test_list_methods_cursor.py)

Yukarıdaki dosyaya dayanarak kendi sunucunuzu test edebilir ve yeteneklerin olması gerektiği gibi oluşturulduğundan emin olabilirsiniz.

Tüm önemli SDK'larda benzer test bölümleri bulunur, böylece seçtiğiniz çalışma zamanı ortamına uyarlayabilirsiniz.

## Örnekler

- [Java Hesap Makinesi](../samples/java/calculator/README.md)
- [.Net Hesap Makinesi](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Hesap Makinesi](../samples/javascript/README.md)
- [TypeScript Hesap Makinesi](../samples/typescript/README.md)
- [Python Hesap Makinesi](../../../../03-GettingStarted/samples/python)

## Ek Kaynaklar

- [Python SDK](https://github.com/modelcontextprotocol/python-sdk)

## Sonraki Adım

- Sonraki: [Dağıtım](../09-deployment/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Feragatname**:
Bu doküman, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hatalar veya yanlışlıklar içerebileceğini lütfen unutmayın. Orijinal doküman, kendi diliyle yetkili kaynak olarak kabul edilmelidir. Önemli bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu oluşabilecek herhangi bir yanlış anlama veya yoruma karşı sorumluluk kabul edilmemektedir.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->