# Visual Studio Code için AI Toolkit uzantısından bir sunucu tüketmek

Bir AI ajanı oluştururken, sadece akıllı yanıtlar üretmek değil, aynı zamanda ajanın harekete geçebilme yeteneğini kazandırmak da önemlidir. İşte burada Model Context Protocol (MCP) devreye giriyor. MCP, ajanların harici araçlara ve hizmetlere tutarlı bir şekilde erişmesini kolaylaştırır. Bunu, ajanın gerçekten kullanabileceği bir alet çantasına bağlanması gibi düşünebilirsiniz.

Diyelim ki bir ajanı hesap makinesi MCP sunucunuza bağladınız. Bir anda, ajanın “47 çarpı 89 nedir?” gibi bir istem alarak matematik işlemleri yapabilmesi mümkün hale gelir—mantığı kodlamaya veya özel API'ler oluşturmaya gerek kalmaz.

## Genel Bakış

Bu ders, Visual Studio Code'daki [AI Toolkit](https://aka.ms/AIToolkit) uzantısını kullanarak bir hesap makinesi MCP sunucusunu bir ajana bağlamayı ve ajanın toplama, çıkarma, çarpma ve bölme gibi matematik işlemlerini doğal dil aracılığıyla gerçekleştirmesini sağlar.

AI Toolkit, Visual Studio Code için güçlü bir uzantıdır ve ajan geliştirme sürecini kolaylaştırır. AI mühendisleri, generatif AI modellerini yerel olarak veya bulutta geliştirerek ve test ederek AI uygulamaları oluşturabilir. Uzantı, bugün mevcut olan en büyük generatif modelleri destekler.

*Not*: AI Toolkit şu anda Python ve TypeScript'i desteklemektedir.

## Öğrenme Hedefleri

Bu dersin sonunda şunları yapabileceksiniz:

- AI Toolkit aracılığıyla bir MCP sunucusunu tüketmek.
- MCP sunucusunun sağladığı araçları keşfetmek ve kullanmak için bir ajan yapılandırmasını ayarlamak.
- MCP araçlarını doğal dil aracılığıyla kullanmak.

## Yaklaşım

Bu sürece genel olarak şu şekilde yaklaşmamız gerekiyor:

- Bir ajan oluşturun ve sistem istemini tanımlayın.
- Hesap makinesi araçlarıyla bir MCP sunucusu oluşturun.
- Agent Builder'ı MCP sunucusuna bağlayın.
- Ajanın araç çağrısını doğal dil aracılığıyla test edin.

Harika, şimdi süreci anladığımıza göre, MCP aracılığıyla harici araçlardan yararlanarak AI ajanımızın yeteneklerini geliştirelim!

## Ön Koşullar

- [Visual Studio Code](https://code.visualstudio.com/)
- [Visual Studio Code için AI Toolkit](https://aka.ms/AIToolkit)

## Alıştırma: Bir sunucu tüketmek

> [!WARNING]
> macOS Kullanıcıları için Not. Şu anda macOS'ta bağımlılık yüklemeyi etkileyen bir sorunu araştırıyoruz. Bu nedenle, macOS kullanıcıları bu eğitimi şu anda tamamlayamayacak. Sorun çözüldüğünde talimatları güncelleyeceğiz. Sabır ve anlayışınız için teşekkür ederiz!

Bu alıştırmada, Visual Studio Code içindeki AI Toolkit ile bir MCP sunucusundan araçlarla bir AI ajanı oluşturacak, çalıştıracak ve geliştireceksiniz.

### -0- Ön adım, OpenAI GPT-4o modelini Modellerim'e ekleyin

Bu alıştırma **GPT-4o** modelini kullanır. Ajanı oluşturmadan önce modelin **Modellerim** bölümüne eklenmesi gerekir.

1. **AI Toolkit** uzantısını **Activity Bar** üzerinden açın.
1. **Catalog** bölümünde **Models** seçeneğini seçerek **Model Catalog**'u açın. **Models** seçeneğini seçmek, **Model Catalog**'u yeni bir editör sekmesinde açar.
1. **Model Catalog** arama çubuğuna **OpenAI GPT-4o** yazın.
1. Modeli **Modellerim** listesine eklemek için **+ Add** düğmesine tıklayın. **GitHub tarafından barındırılan** modeli seçtiğinizden emin olun.
1. **Activity Bar** üzerinden **OpenAI GPT-4o** modelinin listede göründüğünü doğrulayın.

### -1- Bir ajan oluşturun

**Agent (Prompt) Builder**, kendi AI destekli ajanlarınızı oluşturmanıza ve özelleştirmenize olanak tanır. Bu bölümde, yeni bir ajan oluşturacak ve konuşmayı yönlendirmek için bir model atayacaksınız.

1. **AI Toolkit** uzantısını **Activity Bar** üzerinden açın.
1. **Tools** bölümünde **Agent (Prompt) Builder** seçeneğini seçin. **Agent (Prompt) Builder** seçeneğini seçmek, **Agent (Prompt) Builder**'ı yeni bir editör sekmesinde açar.
1. **+ New Agent** düğmesine tıklayın. Uzantı, **Command Palette** üzerinden bir kurulum sihirbazı başlatacaktır.
1. **Calculator Agent** adını girin ve **Enter** tuşuna basın.
1. **Agent (Prompt) Builder**'da, **Model** alanı için **OpenAI GPT-4o (via GitHub)** modelini seçin.

### -2- Ajan için bir sistem istemi oluşturun

Ajanın iskeleti oluşturulduktan sonra, kişiliğini ve amacını tanımlama zamanı. Bu bölümde, **Generate system prompt** özelliğini kullanarak ajanın davranışını ve amacını tanımlayacak bir sistem istemi oluşturacaksınız—bu durumda bir hesap makinesi ajanı.

1. **Prompts** bölümünde, **Generate system prompt** düğmesine tıklayın. Bu düğme, ajanın sistem istemini oluşturmak için AI kullanan istem oluşturucuyu açar.
1. **Generate a prompt** penceresinde şu metni girin: `Sen yardımcı ve verimli bir matematik asistanısın. Temel aritmetik içeren bir problem verildiğinde, doğru sonucu vererek yanıt verirsin.`
1. **Generate** düğmesine tıklayın. Sağ alt köşede sistem isteminin oluşturulduğunu doğrulayan bir bildirim görünecektir. İstem oluşturma tamamlandığında, istem **Agent (Prompt) Builder**'ın **System prompt** alanında görünecektir.
1. **System prompt**'u gözden geçirin ve gerekirse düzenleyin.

### -3- Bir MCP sunucusu oluşturun

Ajanınızın sistem istemini tanımladıktan sonra—davranışını ve yanıtlarını yönlendiren—ajanı pratik yeteneklerle donatma zamanı. Bu bölümde, toplama, çıkarma, çarpma ve bölme işlemlerini gerçekleştirebilecek araçlarla bir hesap makinesi MCP sunucusu oluşturacaksınız. Bu sunucu, ajanın doğal dil istemlerine yanıt olarak gerçek zamanlı matematik işlemleri yapmasını sağlayacaktır.

AI Toolkit, kendi MCP sunucunuzu oluşturmayı kolaylaştıran şablonlarla donatılmıştır. Hesap makinesi MCP sunucusunu oluşturmak için Python şablonunu kullanacağız.

*Not*: AI Toolkit şu anda Python ve TypeScript'i desteklemektedir.

1. **Agent (Prompt) Builder**'ın **Tools** bölümünde **+ MCP Server** düğmesine tıklayın. Uzantı, **Command Palette** üzerinden bir kurulum sihirbazı başlatacaktır.
1. **+ Add Server** seçeneğini seçin.
1. **Create a New MCP Server** seçeneğini seçin.
1. **python-weather** şablonunu seçin.
1. MCP sunucu şablonunu kaydetmek için **Default folder** seçeneğini seçin.
1. Sunucu için şu adı girin: **Calculator**
1. Yeni bir Visual Studio Code penceresi açılacaktır. **Yes, I trust the authors** seçeneğini seçin.
1. **Terminal**'i kullanarak (**Terminal** > **New Terminal**) bir sanal ortam oluşturun: `python -m venv .venv`
1. **Terminal**'i kullanarak sanal ortamı etkinleştirin:
    1. Windows - `.venv\Scripts\activate`
    1. macOS/Linux - `source .venv/bin/activate`
1. **Terminal**'i kullanarak bağımlılıkları yükleyin: `pip install -e .[dev]`
1. **Activity Bar**'ın **Explorer** görünümünde **src** dizinini genişletin ve **server.py** dosyasını seçerek editörde açın.
1. **server.py** dosyasındaki kodu şu kodla değiştirin ve kaydedin:

    ```python
    """
    Sample MCP Calculator Server implementation in Python.

    
    This module demonstrates how to create a simple MCP server with calculator tools
    that can perform basic arithmetic operations (add, subtract, multiply, divide).
    """
    
    from mcp.server.fastmcp import FastMCP
    
    server = FastMCP("calculator")
    
    @server.tool()
    def add(a: float, b: float) -> float:
        """Add two numbers together and return the result."""
        return a + b
    
    @server.tool()
    def subtract(a: float, b: float) -> float:
        """Subtract b from a and return the result."""
        return a - b
    
    @server.tool()
    def multiply(a: float, b: float) -> float:
        """Multiply two numbers together and return the result."""
        return a * b
    
    @server.tool()
    def divide(a: float, b: float) -> float:
        """
        Divide a by b and return the result.
        
        Raises:
            ValueError: If b is zero
        """
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
    ```

### -4- Hesap makinesi MCP sunucusu ile ajanı çalıştırın

Artık ajanın araçları var, onları kullanma zamanı! Bu bölümde, ajana istemler göndererek hesap makinesi MCP sunucusundan uygun aracı kullanıp kullanmadığını test edecek ve doğrulayacaksınız.

1. MCP sunucusunu başlatmak için `F5` tuşuna basın. **Agent (Prompt) Builder** yeni bir editör sekmesinde açılacaktır. Sunucunun durumu terminalde görünür.
1. **Agent (Prompt) Builder**'ın **User prompt** alanına şu istemi girin: `3 adet ürünü 25$ fiyatla aldım ve ardından 20$ indirim kullandım. Ne kadar ödedim?`
1. **Run** düğmesine tıklayarak ajanın yanıtını oluşturun.
1. Ajan çıktısını gözden geçirin. Model, **55$** ödediğinizi belirlemelidir.
1. İşte gerçekleşmesi gerekenlerin bir özeti:
    - Ajan, hesaplama için **multiply** ve **subtract** araçlarını seçer.
    - **multiply** aracı için ilgili `a` ve `b` değerleri atanır.
    - **subtract** aracı için ilgili `a` ve `b` değerleri atanır.
    - Her araçtan gelen yanıt, ilgili **Tool Response** bölümünde sağlanır.
    - Modelin nihai çıktısı, **Model Response** bölümünde sağlanır.
1. Ajana ek istemler göndererek daha fazla test yapın. **User prompt** alanındaki mevcut istemi değiştirerek yeni istemler girebilirsiniz.
1. Test işlemini tamamladıktan sonra, sunucuyu **terminal** üzerinden **CTRL/CMD+C** tuşlarına basarak durdurabilirsiniz.

## Ödev

**server.py** dosyanıza ek bir araç girişi eklemeyi deneyin (örneğin: bir sayının karekökünü döndürmek). Ajanın yeni aracınızı (veya mevcut araçları) kullanmasını gerektiren ek istemler gönderin. Yeni eklenen araçları yüklemek için sunucuyu yeniden başlatmayı unutmayın.

## Çözüm

[Çözüm](./solution/README.md)

## Temel Çıkarımlar

Bu bölümden çıkarılacaklar şunlardır:

- AI Toolkit uzantısı, MCP Sunucuları ve araçlarını tüketmek için harika bir istemcidir.
- MCP sunucularına yeni araçlar ekleyerek, ajanın yeteneklerini gelişen gereksinimlere uygun şekilde genişletebilirsiniz.
- AI Toolkit, özel araçlar oluşturmayı kolaylaştıran şablonlar (örneğin, Python MCP sunucu şablonları) içerir.

## Ek Kaynaklar

- [AI Toolkit belgeleri](https://aka.ms/AIToolkit/doc)

## Sıradaki Adım
- Sıradaki: [Test ve Hata Ayıklama](../08-testing/README.md)

**Feragatname**:  
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hata veya yanlışlıklar içerebileceğini lütfen unutmayın. Orijinal belgenin kendi dilindeki hali yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımından kaynaklanan herhangi bir yanlış anlama veya yanlış yorumlama durumunda sorumluluk kabul edilmez.