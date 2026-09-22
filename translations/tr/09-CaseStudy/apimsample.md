# Vaka Çalışması: REST API’yi API Yönetiminde MCP sunucusu olarak açığa çıkarma

Azure API Management, API Uç Noktalarınızın üstünde bir Ağ Geçidi sağlayan bir hizmettir. Çalışma şekli, Azure API Management'ın API'lerinizin önünde bir vekil gibi davranması ve gelen isteklerle ne yapılacağına karar vermesidir.

Bunu kullanarak, şunlar gibi birçok özellik eklersiniz:

- **Güvenlik**, API anahtarlarından JWT’ye ve yönetilen kimliğe kadar her şeyi kullanabilirsiniz.
- **Oran sınırlaması (Rate limiting)**, harika bir özellik, belirli bir zaman biriminde kaç çağrının geçeceğine karar verebilmenizdir. Bu, tüm kullanıcıların iyi bir deneyim yaşamasını sağlarken hizmetinizin isteklerle aşırı yüklenmesini de önler.
- **Ölçeklendirme ve Yük dengeleme**. Yükü dengelemek için birden çok uç nokta ayarlayabilir ve "yük dengelemesini" nasıl yapacağınıza karar verebilirsiniz.
- **Anlamsal önbellekleme (semantic caching), token limiti ve token izlemesi gibi AI özellikleri** ve daha fazlası. Bunlar, yanıt verme hızını artıran ve token harcamalarınızın kontrolünde yardımcı olan harika özelliklerdir. [Buradan daha fazlasını okuyun](https://learn.microsoft.com/en-us/azure/api-management/genai-gateway-capabilities).

## Neden MCP + Azure API Management?

Model Context Protocol, ajan tabanlı AI uygulamaları ve araçları tutarlı bir şekilde açığa çıkarma yöntemleri için hızla bir standart haline geliyor. Azure API Management, API'leri "yönetmeniz" gerektiğinde doğal bir seçimdir. MCP Sunucuları genellikle bir aracın isteğini çözmek için diğer API’lerle entegre olur. Bu nedenle Azure API Management ile MCP birleşimi çok mantıklıdır.

## Genel Bakış

Bu özel kullanım durumunda, API uç noktalarını MCP Sunucusu olarak açığa çıkarmayı öğreneceğiz. Böylece bu uç noktaları kolayca ajan tabanlı bir uygulamanın parçası haline getirebilir ve Azure API Management özelliklerinden faydalanabiliriz.

## Temel Özellikler

- Açığa çıkarmak istediğiniz uç nokta yöntemlerini seçersiniz.
- Aldığınız ek özellikler, API'niz için politika bölümünde yapılandırdıklarınıza bağlıdır. Burada ise oran sınırlama nasıl eklenir göstereceğiz.

## Ön adım: bir API içe aktarın

Eğer Azure API Management’da zaten bir API'niz varsa harika, bu adımı atlayabilirsiniz. Yoksa bu bağlantıya göz atın, [Azure API Management’a API içe aktarma](https://learn.microsoft.com/en-us/azure/api-management/import-and-publish#import-and-publish-a-backend-api).

## API’yi MCP Sunucusu olarak açığa çıkarma

API uç noktalarını açığa çıkarmak için şu adımları izleyelim:

1. Azure Portal’a gidin ve şu adrese erişin <https://portal.azure.com/?Microsoft_Azure_ApiManagement=mcp>
API Yönetim örneğinize gidin.

1. Sol menüde, API'ler > MCP Sunucular > + Yeni MCP Sunucusu Oluştur’u seçin.

1. API bölümünde, MCP sunucusu olarak açığa çıkarılacak REST API’yi seçin.

1. Araç olarak açığa çıkarılacak bir veya daha fazla API İşlemini seçin. Tüm işlemleri veya sadece belirli işlemleri seçebilirsiniz.

    ![Açığa çıkarılacak yöntemleri seçin](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/create-mcp-server-small.png)


1. **Oluştur** seçeneğine tıklayın.

1. Menüden **API’ler** ve ardından **MCP Sunucular**’a gidin, aşağıdaki görünmelidir:

    ![Ana panelde MCP Sunucuyu görün](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-list.png)

    MCP sunucusu oluşturuldu ve API işlemleri araçlar olarak açığa çıkarıldı. MCP sunucusu MCP Sunucular panelinde listelenir. URL sütunu, test yapmak veya istemci uygulaması içinde çağırmak için kullanabileceğiniz MCP sunucusunun uç noktasını gösterir.

## İsteğe bağlı: Politikaları yapılandırma

Azure API Management, uç noktalarınız için oran sınırlama veya anlamsal önbellekleme gibi farklı kuralları ayarladığınız politika kavramına sahiptir. Bu politikalar XML formatında yazılır.

MCP Sunucunuzda oran sınırlama uygulamak için şöyle yapabilirsiniz:

1. Portalda, API’ler altında **MCP Sunucular**’ı seçin.

1. Oluşturduğunuz MCP sunucusunu seçin.

1. Sol menüde MCP altında **Politikalar**’ı seçin.

1. Politika düzenleyicide, MCP sunucusunun araçlarına uygulamak istediğiniz politikaları ekleyin veya düzenleyin. Politikalar XML formatındadır. Örneğin, MCP sunucusunun araçlarına yapılacak çağrıları 30 saniyede 5 ile sınırlandırmak için bir politika ekleyebilirsiniz. İşte sınırlandırmayı sağlayan XML:

    ```xml
     <rate-limit-by-key calls="5" 
       renewal-period="30" 
       counter-key="@(context.Request.IpAddress)" 
       remaining-calls-variable-name="remainingCallsPerIP" 
    />
    ```

    İşte politika düzenleyicinin bir resmi:

    ![Politika düzenleyici](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-policies-small.png)
 
## Deneyin

MCP Sunucumuzun amaçlandığı gibi çalıştığından emin olalım.

> [!NOTE]
> Azure API Management şu anda bu sunucuyu Streamable
> HTTP `/mcp` uç noktası üzerinden açığa çıkarıyor. Eski HTTP+SSE `/sse` taşıması kullanımdan kaldırılmıştır
> ve yalnızca eski istemcilerle kullanılmalıdır.

Bunun için Visual Studio Code ve GitHub Copilot ile Agent modunu kullanacağız. MCP sunucusunu bir *mcp.json* dosyasına ekleyeceğiz. Böylece Visual Studio Code ajan özelliklerine sahip bir istemci gibi davranacak ve son kullanıcılar bir komut yazıp sunucu ile etkileşime girebilecek.

MCP sunucusunu Visual Studio Code’a eklemenin yolu şöyle:

1. Komut Paletinden MCP: **Sunucu Ekle komutunu kullanın**.

1. İstendiğinde, sunucu türünü seçin: **HTTP (HTTP veya Server Sent Events)**.

1. API Management'da gösterilen MCP sunucusunun Streamable HTTP URL’sini girin.
    Örneğin:
    `https://<apim-service-name>.azure-api.net/<api-name>-mcp/mcp`.

1. İstediğiniz bir sunucu kimliği girin. Bu önemli bir değer değildir ama bu sunucu örneğinin ne olduğunu hatırlamanıza yardımcı olur.

1. Yapılandırmanın çalışma alanı ayarlarına mı yoksa kullanıcı ayarlarına mı kaydedileceğini seçin.

  - **Çalışma alanı ayarları** - Sunucu yapılandırması yalnızca mevcut çalışma alanında bulunan .vscode/mcp.json dosyasına kaydedilir.

    *mcp.json*

    ```json
    "servers": {
        "APIM petstore" : {
            "type": "http",
            "url": "url-to-mcp-server/mcp"
        }
    }
    ```

  - **Kullanıcı ayarları** - Sunucu yapılandırması küresel *settings.json* dosyanıza eklenir ve tüm çalışma alanlarında kullanılabilir. Yapılandırma şöyle görünür:

    ![Kullanıcı ayarı](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-servers-visual-studio-code.png)

1. Ayrıca Azure API Management'a doğru düzgün kimlik doğrulaması yapılmasını sağlamak için bir üstbilgi eklemeniz gerekir. Bu, **Ocp-Apim-Subscription-Key** adlı bir üstbilgi kullanır.

    - İşte bunu ayarlara nasıl ekleyebileceğiniz:

    ![Kimlik doğrulama için üstbilgi ekleme](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-with-header-visual-studio-code.png), bu, Azure Portal'da Azure API Management örneğiniz için bulabileceğiniz API anahtarı değerini sormak üzere bir istemin gösterilmesine neden olur.

   - Bunun yerine *mcp.json* dosyasına eklemek için şöyle yapabilirsiniz:

    ```json
    "inputs": [
      {
        "type": "promptString",
        "id": "apim_key",
        "description": "API Key for Azure API Management",
        "password": true
      }
    ]
    "servers": {
        "APIM petstore" : {
            "type": "http",
            "url": "url-to-mcp-server/mcp",
            "headers": {
                "Ocp-Apim-Subscription-Key": "Bearer ${input:apim_key}"
            }
        }
    }
    ```

### Agent modunu kullanın

Artık ya ayarlarda ya da *.vscode/mcp.json* içinde her şey hazır. Hadi deneyelim.

Sunucunuzdan açığa çıkarılan araçların listelendiği şunlara benzer bir Araçlar simgesi olmalıdır:

![Sunucudan araçlar](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/tools-button-visual-studio-code.png)

1. Araçlar simgesine tıklayın ve aşağıdaki gibi bir araçlar listesi görmelisiniz:

    ![Araçlar](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/select-tools-visual-studio-code.png)

1. Aracı çağırmak için sohbete bir komut girin. Örneğin, bir sipariş bilgisi almak için bir araç seçtiyseniz, ajanla sipariş hakkında sorabilirsiniz. İşte örnek bir komut:

    ```text
    get information from order 2
    ```

    Şimdi bir araç çağrısı yapmanızı isteyen bir araçlar simgesi gösterilecektir. Aracı çalıştırmaya devam etmeyi seçin, aşağıdaki gibi bir çıktı görmelisiniz:

    ![Komut sonuçları](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/chat-results-visual-studio-code.png)

    **Yukarıda gördüğünüz, kurduğunuz araçlara bağlıdır, ama amaç yukarıdaki gibi metinsel yanıt almanızdır**


## Referanslar

Daha fazla öğrenmek için:

- [Azure API Management ve MCP üzerine eğitim](https://learn.microsoft.com/en-us/azure/api-management/export-rest-mcp-server)
- [Python örneği: Azure API Management kullanarak güvenli uzak MCP sunucuları (deneysel)](https://github.com/Azure-Samples/remote-mcp-apim-functions-python)

- [MCP istemci yetkilendirme laboratuvarı](https://github.com/Azure-Samples/AI-Gateway/tree/main/labs/mcp-client-authorization)

- [VS Code için Azure API Management uzantısını kullanarak API’leri içe aktarın ve yönetin](https://learn.microsoft.com/en-us/azure/api-management/visual-studio-code-tutorial)

- [Azure API Center’da uzak MCP sunucularını kaydedin ve keşfedin](https://learn.microsoft.com/en-us/azure/api-center/register-discover-mcp-server)
- [AI Gateway](https://github.com/Azure-Samples/AI-Gateway) Azure API Management ile birçok AI özelliğini gösteren harika bir depo
- [AI Gateway atölyeleri](https://azure-samples.github.io/AI-Gateway/) Azure Portal kullanımıyla atölyeler içerir, AI özelliklerini değerlendirmeye başlamak için harika bir yöntem.

## Sonraki Adımlar

- Geri: [Vaka Çalışmaları Genel Bakış](./README.md)
- Sonraki: [Azure AI Seyahat Acenteleri](./travelagentsample.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Feragatname**:
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba sarf etsek de, otomatik çevirilerin hata veya yanlışlık içerebileceğini lütfen unutmayınız. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu ortaya çıkabilecek yanlış anlamalardan veya yanlış yorumlamalardan sorumlu değiliz.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->