# Pratik Uygulama

[![Gerçek Araçlar ve İş Akışlarıyla MCP Uygulamalarını Nasıl Oluşturur, Test Eder ve Dağıtırsınız](../../../translated_images/tr/05.64bea204e25ca891.webp)](https://youtu.be/vCN9-mKBDfQ)

_(Bu dersin videosunu izlemek için yukarıdaki resme tıklayın)_

Pratik uygulama, Model Context Protocol’un (MCP) gücünün somut hale geldiği yerdir. MCP’nin arkasındaki teori ve mimariyi anlamak önemli olsa da, gerçek değer bu kavramları gerçek dünya problemlerini çözmek için çözümler oluştururken, test ederken ve dağıtırken ortaya çıkar. Bu bölüm kavramsal bilgi ile uygulamalı geliştirme arasındaki boşluğu doldurarak, MCP tabanlı uygulamaları hayata geçirme sürecinde size rehberlik eder.

İster akıllı asistanlar geliştiriyor olun, ister AI’yı iş akışlarına entegre ediyor olun ya da veri işleme için özel araçlar oluşturuyor olun, MCP esnek bir temel sunar. Dil bağımsız tasarımı ve popüler programlama dilleri için resmi SDK’ları sayesinde geniş bir geliştirici kitlesine erişilebilir. Bu SDK’ları kullanarak çözümlerinizi hızlıca prototipleyebilir, yineleyebilir ve farklı platformlarda ve ortamlarda ölçeklendirebilirsiniz.

Aşağıdaki bölümlerde, MCP’yi C#, Spring ile Java, TypeScript, JavaScript ve Python’da nasıl uygulayacağınıza dair pratik örnekler, örnek kodlar ve dağıtım stratejileri bulacaksınız. Ayrıca MCP sunucularınızı nasıl hata ayıklayacağınızı, test edeceğinizi, API’leri yöneteceğinizi ve Azure kullanarak çözümleri buluta nasıl dağıtacağınız öğreneceksiniz. Bu uygulamalı kaynaklar öğrenmenizi hızlandırmak ve sağlam, üretime hazır MCP uygulamaları oluştururken size güven sağlamak amacıyla tasarlanmıştır.

## Genel Bakış

Bu ders, MCP uygulamasının birden çok programlama dilinde pratik yönlerine odaklanır. C#, Spring ile Java, TypeScript, JavaScript ve Python’da MCP SDK’larının nasıl kullanılacağını, sağlam uygulamalar geliştirmeyi, MCP sunucularını hata ayıklamayı ve test etmeyi, yeniden kullanılabilir kaynaklar, istemler ve araçlar oluşturmayı keşfedeceğiz.

## Öğrenme Hedefleri

Bu dersin sonunda şunları yapabileceksiniz:

- Resmi SDK’ları kullanarak çeşitli programlama dillerinde MCP çözümleri uygulamak
- MCP sunucularını sistematik olarak hata ayıklamak ve test etmek
- Sunucu özellikleri (Kaynaklar, İstemler ve Araçlar) oluşturmak ve kullanmak
- Karmaşık görevler için etkili MCP iş akışları tasarlamak
- MCP uygulamalarını performans ve güvenilirlik için optimize etmek

## Resmi SDK Kaynakları

Model Context Protocol, birden çok dil için resmi SDK’lar sunar ([MCP Specification 2025-11-25](https://spec.modelcontextprotocol.io/specification/2025-11-25/) ile uyumlu):

- [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk)
- [Spring ile Java SDK](https://github.com/modelcontextprotocol/java-sdk) **Not:** [Project Reactor](https://projectreactor.io) bağımlılığı gerektirir. (Bkz. [tartışma 246](https://github.com/orgs/modelcontextprotocol/discussions/246).)
- [TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk)
- [Python SDK](https://github.com/modelcontextprotocol/python-sdk)
- [Kotlin SDK](https://github.com/modelcontextprotocol/kotlin-sdk)
- [Go SDK](https://github.com/modelcontextprotocol/go-sdk)

## MCP SDK’ları ile Çalışmak

Bu bölüm, MCP’yi birden çok programlama dilinde uygulamaya yönelik pratik örnekler sağlar. Örnek kodları, dil bazında düzenlenmiş `samples` dizininde bulabilirsiniz.

### Mevcut Örnekler

Depo aşağıdaki dillerde [örnek uygulamalar](../../../04-PracticalImplementation/samples) içerir:

- [C#](./samples/csharp/README.md)
- [Spring ile Java](./samples/java/containerapp/README.md)
- [TypeScript](./samples/typescript/README.md)
- [JavaScript](./samples/javascript/README.md)
- [Python](./samples/python/README.md)

Her örnek, ilgili dil ve ekosistem için temel MCP kavramlarını ve uygulama desenlerini gösterir.

### Pratik Kılavuzlar

Pratik MCP uygulaması için ek kılavuzlar:

- [Sayfalama ve Büyük Sonuç Kümeleri](./pagination/README.md) - Araçlar, kaynaklar ve büyük verisetleri için imleç tabanlı sayfalamayı ele alma

## Temel Sunucu Özellikleri

MCP sunucuları aşağıdaki özelliklerin herhangi bir kombinasyonunu uygulayabilir:

### Kaynaklar

Kaynaklar, kullanıcı ya da AI modelinin kullanması için bağlam ve veri sağlar:

- Belge depoları
- Bilgi tabanları
- Yapılandırılmış veri kaynakları
- Dosya sistemleri

### İstemler

İstemler, kullanıcılar için şablonlanmış mesajlar ve iş akışlarıdır:

- Önceden tanımlanmış sohbet şablonları
- Yönlendirilmiş etkileşim kalıpları
- Özel diyalog yapıları

### Araçlar

Araçlar, AI modelinin yürütmesi için fonksiyonlardır:

- Veri işleme araçları
- Harici API entegrasyonları
- Hesaplama yetenekleri
- Arama fonksiyonu

## Örnek Uygulamalar: C# Uygulaması

Resmi C# SDK deposu, MCP’nin farklı yönlerini gösteren birkaç örnek uygulama içerir:

- **Temel MCP İstemcisi**: MCP istemcisi oluşturmayı ve araçları çağırmayı gösteren basit örnek
- **Temel MCP Sunucusu**: Temel araç kaydı ile minimalist sunucu uygulaması
- **Gelişmiş MCP Sunucusu**: Araç kaydı, kimlik doğrulama ve hata yönetimi içeren tam özellikli sunucu
- **ASP.NET Entegrasyonu**: ASP.NET Core ile entegrasyonu gösteren örnekler
- **Araç Uygulama Desenleri**: Farklı karmaşıklık seviyelerinde araç uygulama desenleri

MCP C# SDK’sı önizlemede olup API’ler değişebilir. SDK geliştikçe bu blogu sürekli güncelleyeceğiz.

### Önemli Özellikler

- [C# MCP Nuget ModelContextProtocol](https://www.nuget.org/packages/ModelContextProtocol)
- [İlk MCP Sunucunuzu oluşturma](https://devblogs.microsoft.com/dotnet/build-a-model-context-protocol-mcp-server-in-csharp/).

Tam C# uygulama örnekleri için [resmi C# SDK örnekleri deposuna](https://github.com/modelcontextprotocol/csharp-sdk) bakınız.

## Örnek uygulama: Spring ile Java Uygulaması

Spring ile Java SDK, kurumsal sınıf özelliklerle sağlam MCP uygulama seçenekleri sunar.

### Önemli Özellikler

- Spring Framework entegrasyonu
- Güçlü tip güvenliği
- Reaktif programlama desteği
- Kapsamlı hata yönetimi

Tam Spring ile Java uygulama örneği için örnekler dizinindeki [Java with Spring örneğine](samples/java/containerapp/README.md) bakınız.

## Örnek uygulama: JavaScript Uygulaması

JavaScript SDK, MCP uygulaması için hafif ve esnek bir yaklaşım sunar.

### Önemli Özellikler

- Node.js ve tarayıcı desteği
- Promise tabanlı API
- Express ve diğer çerçevelerle kolay entegrasyon
- Streaming için WebSocket desteği

Tam JavaScript uygulama örneği için örnekler dizinindeki [JavaScript örneğine](samples/javascript/README.md) bakınız.

## Örnek uygulama: Python Uygulaması

Python SDK, mükemmel ML çerçeve entegrasyonlarıyla Python’cı bir MCP uygulama yaklaşımı sunar.

### Önemli Özellikler

- asyncio ile async/await desteği
- FastAPI entegrasyonu
- Basit araç kaydı
- Popüler ML kütüphaneleriyle doğal entegrasyon

Tam Python uygulama örneği için örnekler dizinindeki [Python örneğine](samples/python/README.md) bakınız.

## API yönetimi

Azure API Yönetimi, MCP Sunucuları nasıl güvence altına alabileceğimiz konusunda harika bir çözümdür. Fikir, MCP Sunucunuzun önüne bir Azure API Yönetimi örneği koymak ve aşağıdaki gibi istediğiniz özellikleri onun yönetmesine izin vermektir:

- hız sınırlaması
- jeton yönetimi
- izleme
- yük dengeleme
- güvenlik

### Azure Örneği

İşte tam olarak bunu yapan bir Azure örneği, yani [MCP Sunucusu oluşturup Azure API Yönetimi ile güvenceye alma](https://github.com/Azure-Samples/remote-mcp-apim-functions-python).

Yetkilendirme akışının aşağıdaki resimde nasıl gerçekleştiğine bakın:

![APIM-MCP](https://github.com/Azure-Samples/remote-mcp-apim-functions-python/blob/main/mcp-client-authorization.gif?raw=true)

Yukarıdaki resimde şu işlemler gerçekleşiyor:

- Kimlik doğrulama/Yetkilendirme Microsoft Entra kullanılarak yapılır.
- Azure API Yönetimi bir geçit olarak işlev görür ve trafiği yönlendirmek ve yönetmek için politikalar kullanır.
- Azure Monitor, tüm istekleri gelecekteki analiz için kaydeder.

#### Yetkilendirme akışı

Yetkilendirme akışına biraz daha ayrıntılı bakalım:

![Sequence Diagram](https://github.com/Azure-Samples/remote-mcp-apim-functions-python/blob/main/infra/app/apim-oauth/diagrams/images/mcp-client-auth.png?raw=true)

#### MCP yetkilendirme spesifikasyonu

[MCP Yetkilendirme spesifikasyonu](https://spec.modelcontextprotocol.io/specification/2025-11-25/basic/authorization/) hakkında daha fazla bilgi edinin.

## Uzaktaki MCP Sunucusunu Azure’a Dağıtma

Az önce bahsettiğimiz örneği dağıtıp dağıtamayacağımıza bakalım:

1. Depoyu klonlayın

    ```bash
    git clone https://github.com/Azure-Samples/remote-mcp-apim-functions-python.git
    cd remote-mcp-apim-functions-python
    ```

1. `Microsoft.App` kaynak sağlayıcısını kaydedin.

   - Azure CLI kullanıyorsanız `az provider register --namespace Microsoft.App --wait` komutunu çalıştırın.
   - Azure PowerShell kullanıyorsanız `Register-AzResourceProvider -ProviderNamespace Microsoft.App` komutunu çalıştırın. Ardından kaydın tamamlanıp tamamlanmadığını kontrol etmek için bir süre sonra `(Get-AzResourceProvider -ProviderNamespace Microsoft.App).RegistrationState` komutunu çalıştırın.

1. API yönetim hizmetini, fonksiyon uygulamasını (kod ile) ve diğer gerekli Azure kaynaklarını sağlamak için şu [azd](https://aka.ms/azd) komutunu çalıştırın:

    ```shell
    azd up
    ```

    Bu komut, Azure’da tüm bulut kaynaklarını dağıtmalıdır.

### MCP Inspector ile sunucunuzu test etme

1. **Yeni bir terminal penceresinde**, MCP Inspector’ı kurun ve çalıştırın

    ```shell
    npx @modelcontextprotocol/inspector
    ```

    Şöyle bir arayüz görmelisiniz:

    ![Connect to Node inspector](../../../translated_images/tr/connect.141db0b2bd05f096.webp)

1. Uygulamanın gösterdiği URL’den MCP Inspector web uygulamasını CTRL+klik ile açın (örneğin [http://127.0.0.1:6274/#resources](http://127.0.0.1:6274/#resources))
1. Taşıma türünü `SSE` olarak ayarlayın
1. `azd up` sonrası gösterilen API Yönetimi SSE uç noktanızın URL’sini ayarlayın ve **Bağlan**a tıklayın:

    ```shell
    https://<apim-servicename-from-azd-output>.azure-api.net/mcp/sse
    ```

1. **Araçları Listele**. Bir araca tıklayın ve **Aracı Çalıştır**.

Eğer tüm adımlar doğru yapıldıysa, artık MCP sunucusuna bağlısınız ve bir aracı çağırabildiniz demektir.

## Azure için MCP sunucuları

[Remote-mcp-functions](https://github.com/Azure-Samples/remote-mcp-functions-dotnet): Bu depo seti, Python, C# .NET veya Node/TypeScript kullanarak Azure Fonksiyonları ile özel uzaktaki MCP (Model Context Protocol) sunucuları oluşturup dağıtmak için hızlı başlangıç şablonu sağlar.

Örnekler, geliştiricilere aşağıdakileri yapma olanağı sunar:

- Yerel olarak oluşturma ve çalışma: MCP sunucusunu yerel makinede geliştirin ve hata ayıklayın
- Azure’a dağıtma: Sadece basit bir azd up komutuyla buluta kolayca dağıtın
- İstemcilerden bağlantı: VS Code’un Copilot agent modu ve MCP Inspector gibi çeşitli istemcilerden MCP sunucusuna bağlanın

### Önemli Özellikler

- Tasarım gereği güvenlik: MCP sunucusu anahtarlar ve HTTPS ile güvence altına alınmıştır
- Kimlik doğrulama seçenekleri: Dahili kimlik doğrulama ve/veya API Yönetimi aracılığıyla OAuth desteği
- Ağ izolasyonu: Azure Sanal Ağları (VNET) kullanarak ağ izolasyonu sağlar
- Sunucusuz mimari: Ölçeklenebilir, olay odaklı yürütme için Azure Fonksiyonları kullanımı
- Yerel geliştirme: Kapsamlı yerel geliştirme ve hata ayıklama desteği
- Basit dağıtım: Azure’a kolaylaştırılmış dağıtım süreci

Depo, üretime hazır MCP sunucu uygulamasıyla hızlıca başlamanızı sağlayacak tüm yapılandırma dosyalarını, kaynak kodlarını ve altyapı tanımlarını içerir.

- [Azure Remote MCP Functions Python](https://github.com/Azure-Samples/remote-mcp-functions-python) - Python ile Azure Fonksiyonları kullanarak MCP örnek uygulaması

- [Azure Remote MCP Functions .NET](https://github.com/Azure-Samples/remote-mcp-functions-dotnet) - C# .NET ile Azure Fonksiyonları kullanarak MCP örnek uygulaması

- [Azure Remote MCP Functions Node/Typescript](https://github.com/Azure-Samples/remote-mcp-functions-typescript) - Node/TypeScript ile Azure Fonksiyonları kullanarak MCP örnek uygulaması

## Önemli Notlar

- MCP SDK’ları, sağlam MCP çözümleri uygulamak için dil-spesifik araçlar sağlar
- Hata ayıklama ve test süreci, güvenilir MCP uygulamaları için kritiktir
- Yeniden kullanılabilir istem şablonları, tutarlı AI etkileşimleri sağlar
- İyi tasarlanmış iş akışları çoklu araçlarla karmaşık görevleri koordine edebilir
- MCP çözümleri uygularken güvenlik, performans ve hata yönetimi dikkate alınmalıdır

## Alıştırma

Alanınızdaki gerçek bir problemi ele alan pratik bir MCP iş akışı tasarlayın:

1. Bu problemi çözmek için faydalı olabilecek 3-4 araç belirleyin
2. Bu araçların nasıl etkileşime girdiğini gösteren bir iş akışı diyagramı oluşturun
3. Tercih ettiğiniz dili kullanarak araçlardan birinin temel bir sürümünü uygulayın
4. Modelin aracınızı etkili şekilde kullanmasını sağlayacak bir istem şablonu oluşturun

## Ek Kaynaklar

---

## Sonraki Bölüm

Sonraki: [İleri Konular](../05-AdvancedTopics/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Feragatname**:  
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hatalar veya yanlışlıklar içerebileceğinin farkında olmanızı rica ederiz. Orijinal belge, ana dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı nedeniyle ortaya çıkabilecek herhangi bir yanlış anlama veya yorum hatasından sorumlu değiliz.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->