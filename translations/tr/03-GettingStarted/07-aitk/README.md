# Visual Studio Code için AI Toolkit uzantısından bir sunucu tüketme

Bir yapay zeka ajanı oluştururken, sadece akıllı yanıtlar üretmek değil; ajanınıza harekete geçme yeteneği kazandırmak da önemlidir. İşte burada Model Context Protocol (MCP) devreye girer. MCP, ajanların dış araçlara ve hizmetlere tutarlı bir şekilde erişmesini kolaylaştırır. Bunu, ajanın gerçekten kullanabileceği bir alet kutusuna bağlanmak gibi düşünün.

Diyelim ki bir ajanı hesap makinesi MCP sunucunuza bağladınız. Birden ajanınız “47 çarpı 89 kaçtır?” gibi bir istem alarak matematik işlemleri yapabilir—mantığı elle kodlamaya veya özel API'ler oluşturmaya gerek yok.

## Genel Bakış

Bu ders, bir hesap makinesi MCP sunucusunu Visual Studio Code'da [AI Toolkit](https://aka.ms/AIToolkit) uzantısı ile bir ajana nasıl bağlayacağınızı ve ajanın toplama, çıkarma, çarpma ve bölme gibi matematik işlemlerini doğal dil aracılığıyla nasıl yapabileceğini kapsar.

AI Toolkit, ajan geliştirmeyi kolaylaştıran güçlü bir Visual Studio Code uzantısıdır. AI mühendisleri, yerel veya bulutta üretken AI modellerini geliştirip test ederek kolayca AI uygulamaları oluşturabilir. Uzantı, günümüzde mevcut çoğu önemli üretken modeli destekler.

*Not*: AI Toolkit şu anda Python ve TypeScript'i desteklemektedir.

## Öğrenme Hedefleri

Bu dersin sonunda şunları yapabileceksiniz:

- AI Toolkit aracılığıyla bir MCP sunucusunu kullanmak.
- Bir ajan yapılandırması oluşturarak MCP sunucusunun sağladığı araçları bulmasını ve kullanmasını sağlamak.
- Doğal dil yoluyla MCP araçlarını kullanmak.

## Yaklaşım

Bunu genel olarak şöyle ele almamız gerekiyor:

- Bir ajan oluşturup sistem istemini tanımlayın.
- Hesap makinesi araçlarına sahip bir MCP sunucusu oluşturun.
- Agent Builder'ı MCP sunucusuna bağlayın.
- Doğal dil yoluyla aracın çağrımını test edin.

Harika, akışı anladığımıza göre, MCP aracılığıyla dış araçları kullanarak AI ajanını yapılandıralım ve onun yeteneklerini geliştirelim!

## Ön Koşullar

- [Visual Studio Code](https://code.visualstudio.com/)
- [Visual Studio Code için AI Toolkit](https://aka.ms/AIToolkit)

## Egzersiz: Bir sunucu tüketme

> [!UYARI]
> macOS Kullanıcıları için Not. macOS'ta bağımlılık kurulumu etkileyen bir sorunu şu anda araştırıyoruz. Bu nedenle macOS kullanıcıları bu eğitimi şu anda tamamlayamayacak. Düzeltme hazır olur olmaz talimatları güncelleyeceğiz. Sabır ve anlayışınız için teşekkürler!

Bu egzersizde, Visual Studio Code içindeki AI Toolkit kullanarak bir MCP sunucusundan araçlarla bir AI ajanı oluşturacak, çalıştıracak ve geliştireceksiniz.

### -0- Ön adım, OpenAI GPT-4o modelini Benim Modellerime ekleyin

Bu egzersiz **GPT-4o** modelini kullanır. Ajan oluşturulmadan önce modelin **Benim Modellerim** listesine eklenmiş olması gerekir.

![Visual Studio Code'un AI Toolkit uzantısındaki model seçim arayüzü ekran görüntüsü. Başlık “AI Çözümünüz için doğru modeli bulun” ve altbaşlıkta kullanıcıları AI modellerini keşfetmeye, test etmeye ve dağıtmaya teşvik ediyor. “Popüler Modeller” altında altı model kartı gösteriliyor: DeepSeek-R1 (GitHub tarafından barındırılıyor), OpenAI GPT-4o, OpenAI GPT-4.1, OpenAI o1, Phi 4 Mini (CPU - Küçük, Hızlı) ve DeepSeek-R1 (Ollama tarafından barındırılıyor). Her kartta modeli “Ekle” veya “Playground'da Deneyin” seçenekleri var.](../../../../translated_images/tr/aitk-model-catalog.2acd38953bb9c119.webp)

1. **AI Toolkit** uzantısını **Aktivite Çubuğu**ndan açın.
1. **Katalog** bölümünde **Modeller**i seçin. **Modeller** seçimi yeni bir editör sekmesinde **Model Kataloğu**nu açar.
1. **Model Kataloğu** arama çubuğuna **OpenAI GPT-4o** yazın.
1. Modeli **Benim Modellerim** listesine eklemek için **+ Ekle**ye tıklayın. GitHub tarafından barındırılan modeli seçtiğinizden emin olun.
1. **Aktivite Çubuğu**nda, **OpenAI GPT-4o** modelinin listede göründüğünden emin olun.

### -1- Bir ajan oluşturun

**Agent (Prompt) Builder** size kendi AI destekli ajanlarınızı oluşturup özelleştirme imkanı verir. Bu bölümde yeni bir ajan oluşturacak ve konuşmayı desteklemesi için bir model atayacaksınız.

![Visual Studio Code için AI Toolkit uzantısında “Calculator Agent” yapıcı arayüzü ekran görüntüsü. Sol panelde seçili model "OpenAI GPT-4o (GitHub üzerinden)" olarak görünüyor. Sistem istemi olarak “Üniversitede matematik öğreten bir profesörsünüz” yazıyor; kullanıcı istemi ise “Fourier denklemini basit terimlerle açıkla.” Araç ekleme, MCP Server etkinleştirme ve yapılandırılmış çıktı seçenekleri butonları mevcut. Alt kısımda mavi “Çalıştır” butonu var. Sağ panelde “Örneklerle Başlayın” altında üç örnek ajan: Web Developer (MCP Server, İkinci Sınıf Basitleştirici ve Rüya Yorumlayıcı özellikleriyle, işlev açıklamalarıyla belirtilmiş).](../../../../translated_images/tr/aitk-agent-builder.901e3a2960c3e477.webp)

1. **AI Toolkit** uzantısını **Aktivite Çubuğu**ndan açın.
1. **Araçlar** bölümünde **Agent (Prompt) Builder**'ı seçin. Bu seçim yeni bir editör sekmesinde **Agent (Prompt) Builder**'ı açar.
1. **+ Yeni Ajan** butonuna tıklayın. Uzantı, **Komut Paleti** aracılığıyla bir kurulum sihirbazı başlatır.
1. Ajan adı olarak **Calculator Agent** yazın ve **Enter** tuşuna basın.
1. **Agent (Prompt) Builder**da **Model** alanında **OpenAI GPT-4o (GitHub üzerinden)** modelini seçin.

### -2- Ajan için sistem istemi oluşturun

Ajan iskeleti hazır, şimdi kişiliğini ve amacını tanımlama zamanı. Bu bölümde **Sistem istemi oluştur** özelliğini kullanarak ajanın amaçlanan davranışını—burada bir hesap makinesi ajanı—tasvir edecek ve modeli sizin için sistem istemini yazdıracak.

![Visual Studio Code için AI Toolkit'te “Calculator Agent” arayüzü, açık "İstem Oluştur" başlıklı modali gösteriyor. Modal, temel bilgileri paylaşarak bir istem şablonu oluşturulabileceğini açıklıyor ve örnek sistem istemi içeren bir metin kutusu mevcut: "Yardımcı ve verimli bir matematik asistanısınız. Basit aritmetik problemleri verildiğinde doğru sonucu verirsiniz." Metin kutusunun altında “Kapat” ve “Oluştur” butonları bulunuyor. Arka planda, seçili model "OpenAI GPT-4o (GitHub üzerinden)" ve sistem ile kullanıcı istemi alanları görünmekte.](../../../../translated_images/tr/aitk-generate-prompt.ba9e69d3d2bbe2a2.webp)

1. **İstemler** bölümünde **Sistem istemi oluştur** butonuna tıklayın. Bu buton, ajan için bir sistem istemi oluşturmak üzere AI kullanan istem oluşturucuyu açar.
1. **İstem Oluştur** penceresine şu metni yazın: `Yardımcı ve verimli bir matematik asistanısınız. Basit aritmetik problemleri verildiğinde doğru sonucu verirsiniz.`
1. **Oluştur** butonuna tıklayın. Sağ alt köşede sistem isteminin oluşturulduğunu belirten bir bildirim çıkacak. İstem oluşturma tamamlandığında, istem **Agent (Prompt) Builder**daki **Sistem istemi** alanında görünecektir.
1. **Sistem istemi**ni gözden geçirin ve gerekirse değiştirin.

### -3- Bir MCP sunucusu oluşturun

Artık ajanın davranışını ve yanıtlarını yöneten sistem istemini tanımladığınıza göre, ajanın pratik özelliklerle donatılma zamanı. Bu bölümde toplama, çıkarma, çarpma ve bölme işlemlerini gerçekleştiren bir hesap makinesi MCP sunucusu oluşturacaksınız. Bu sunucu, ajanın doğal dil taleplerine gerçek zamanlı matematik işlemleri yapmasını sağlar.

![Visual Studio Code için AI Toolkit uzantısında Calculator Agent arayüzünün alt kısmının ekran görüntüsü. “Araçlar” ve “Yapılandırılmış çıktı” açılabilir menüler gösteriliyor, yanında “Çıktı formatı seç” açılır menüsü "metin" olarak ayarlı. Sağda Model Context Protocol sunucusu eklemek için “+ MCP Server” butonu var. Araçlar bölümünün üzerinde bir resim simgesi yer tutucu var.](../../../../translated_images/tr/aitk-add-mcp-server.9742cfddfe808353.webp)

AI Toolkit, kendi MCP sunucunuzu oluşturmayı kolaylaştırmak için şablonlar sunar. Biz hesap makinesi MCP sunucusu oluşturmak için Python şablonunu kullanacağız.

*Not*: AI Toolkit şu anda Python ve TypeScript'i desteklemektedir.

1. **Agent (Prompt) Builder**'daki **Araçlar** bölümünde **+ MCP Server** butonuna tıklayın. Uzantı **Komut Paleti** aracılığıyla bir kurulum sihirbazı başlatacak.
1. **+ Sunucu Ekle**yi seçin.
1. **Yeni bir MCP Sunucusu Oluştur**u seçin.
1. Şablon olarak **python-weather**i seçin.
1. MCP sunucu şablonunu kaydetmek için **Varsayılan klasör**ü seçin.
1. Sunucu için şu adı girin: **Calculator**
1. Yeni bir Visual Studio Code penceresi açılacak. **Evet, yazarlara güveniyorum** seçeneğini seçin.
1. Terminali kullanarak (**Terminal** > **Yeni Terminal**) sanal ortam oluşturun: `python -m venv .venv`
1. Terminalde sanal ortamı etkinleştirin:
    1. Windows - `.venv\Scripts\activate`
    1. macOS/Linux - `source .venv/bin/activate`
1. Terminalde bağımlılıkları yükleyin: `pip install -e .[dev]`
1. **Aktivite Çubuğu**ndaki **Explorer** görünümünde **src** dizinini genişletin ve **server.py** dosyasını editörde açmak için seçin.
1. **server.py** dosyasındaki kodu aşağıdaki kod bloğuyla değiştirin ve kaydedin:

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

### -4- Hesap makinesi MCP sunucusuyla ajanı çalıştırma

Artık ajanın araçlara sahip, onları kullanma zamanı geldi! Bu bölümde, ajana talimatlar gönderip ajanın hesap makinesi MCP sunucusundan uygun aracı kullanıp kullanmadığını test edeceksiniz.

![Visual Studio Code için AI Toolkit uzantısındaki Calculator Agent arayüzünün ekran görüntüsü. Sol panelde “Araçlar” altında local-server-calculator_server adlı bir MCP sunucusu eklenmiş, dört araç mevcut: toplama, çıkarma, çarpma ve bölme. Dört aracın aktif olduğunu gösteren bir rozet var. Altında kapanmış “Yapılandırılmış çıktı” bölümü ve mavi “Çalıştır” butonu var. Sağ panelde “Model Yanıtı” altında ajan sırasıyla {"a": 3, "b": 25} ve {"a": 75, "b": 20} girdileriyle çarpma ve çıkarma araçlarını çağırdı. Son “Araç Yanıtı” 75.0 olarak görünüyor. Altta “Kodu Görüntüle” butonu var.](../../../../translated_images/tr/aitk-agent-response-with-tools.e7c781869dc8041a.webp)

Hesap makinesi MCP sunucusunu, **Agent Builder** aracılığıyla MCP istemcisi olarak yerel geliştirme makinenizde çalıştıracaksınız.

1. MCP sunucusunu hata ayıklama için başlatmak üzere `F5` tuşuna basın. **Agent (Prompt) Builder** yeni bir editör sekmesinde açılacaktır. Sunucunun durumu terminalde görünür olacak.
1. **Agent (Prompt) Builder**'daki **Kullanıcı istemi** alanına şu istemi girin: `3 adeti 25 $ olan ürünler aldım, sonra 20 $ indirim kullandım. Ne kadar ödedim?`
1. Ajanın yanıtını oluşturmak için **Çalıştır** butonuna tıklayın.
1. Ajan çıktısını gözden geçirin. Modelin ödediğiniz miktarın **55 $** olduğunu sonucuna varması gerekir.
1. İşte olması gerekenlerin dökümü:
    - Ajan hesaplama sırasında yardımcı olmak için **çarpma** ve **çıkarma** araçlarını seçer.
    - **Çarpma** aracı için ilgili `a` ve `b` değerleri atanır.
    - **Çıkarma** aracı için ilgili `a` ve `b` değerleri atanır.
    - Her aracın yanıtı ilgili **Araç Yanıtı**nda verilir.
    - Modelin son çıktısı final **Model Yanıtı**nda sağlanır.
1. Ajanı daha fazla test etmek için ek istemler gönderin. Mevcut istemi **Kullanıcı istemi** alanına tıklayıp değiştirebilirsiniz.
1. Testi bitirdikten sonra terminalde **CTRL/CMD+C** ile sunucuyu durdurabilirsiniz.

## Ödev

**server.py** dosyanıza ek bir araç girdisi (mesela bir sayının karekökünü döndüren) eklemeyi deneyin. Ajanın yeni aracınızı (veya mevcut araçları) kullanmasını gerektiren ek istemler gönderin. Yeni eklenen araçların yüklenmesi için sunucuyu yeniden başlatmayı unutmayın.

## Çözüm

[Çözüm](./solution/README.md)

## Ana Noktalar

Bu bölümden çıkarılacak ana noktalar şunlardır:

- AI Toolkit uzantısı, MCP Sunucularını ve araçlarını tüketmenizi sağlayan mükemmel bir istemcidir.
- MCP sunucularına yeni araçlar ekleyerek ajanın yeteneklerini gelişen gereksinimlere uyacak şekilde genişletebilirsiniz.
- AI Toolkit, özel araçlar oluşturmayı basitleştirmek için Python MCP sunucu şablonları gibi şablonlar içerir.

## Ek Kaynaklar

- [AI Toolkit belgeleri](https://aka.ms/AIToolkit/doc)

## Sonraki Adım
- Sıradaki: [Test Etme ve Hata Ayıklama](../08-testing/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Feragatname**:
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba sarf etsek de, otomatik çevirilerin hata veya yanlışlık içerebileceğini lütfen unutmayınız. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu ortaya çıkabilecek yanlış anlamalardan veya yanlış yorumlamalardan sorumlu değiliz.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->