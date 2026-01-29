# Vaka Çalışması: API Management'te REST API'yi MCP sunucusu olarak açığa çıkarma

Azure API Management, API uç noktalarınızın üzerinde bir Gateway sağlayan bir hizmettir. Çalışma şekli, Azure API Management'ın API'lerinizin önünde bir proxy gibi davranması ve gelen isteklerle ne yapılacağına karar vermesidir.

Bu hizmeti kullanarak aşağıdaki gibi birçok özellik ekleyebilirsiniz:

- **Güvenlik**, API anahtarlarından JWT'ye ve yönetilen kimliklere kadar her şeyi kullanabilirsiniz.
- **Hız sınırlama**, belirli bir zaman biriminde kaç çağrının geçeceğini belirleyebilmek harika bir özelliktir. Bu, tüm kullanıcıların harika bir deneyim yaşamasını ve hizmetinizin isteklerle aşırı yüklenmemesini sağlar.
- **Ölçeklendirme ve Yük dengeleme**, yükü dengelemek için bir dizi uç nokta ayarlayabilir ve "yük dengeleme" yöntemini seçebilirsiniz.
- **AI özellikleri, örneğin semantik önbellekleme**, token sınırı ve token izleme gibi özellikler. Bu özellikler yanıt verme hızını artırır ve token harcamalarınızı kontrol altında tutmanıza yardımcı olur. [Buradan daha fazla bilgi edinin](https://learn.microsoft.com/en-us/azure/api-management/genai-gateway-capabilities).

## Neden MCP + Azure API Management?

Model Context Protocol, araçsal AI uygulamaları ve araçları ve verileri tutarlı bir şekilde açığa çıkarma konusunda hızla bir standart haline geliyor. Azure API Management, API'leri "yönetmeniz" gerektiğinde doğal bir seçimdir. MCP Sunucuları genellikle bir araca istekleri çözmek için diğer API'lerle entegre olur. Bu nedenle Azure API Management ve MCP'yi birleştirmek mantıklıdır.

## Genel Bakış

Bu özel kullanım senaryosunda, API uç noktalarını bir MCP Sunucusu olarak açığa çıkarmayı öğreneceğiz. Bunu yaparak, bu uç noktaları bir araçsal uygulamanın parçası haline kolayca getirebilir ve aynı zamanda Azure API Management'ın özelliklerinden yararlanabilirsiniz.

## Temel Özellikler

- Araç olarak açığa çıkarmak istediğiniz uç nokta yöntemlerini seçersiniz.
- Ek özellikler, API'niz için politika bölümünde yapılandırdığınız şeylere bağlıdır. Ancak burada hız sınırlama eklemeyi nasıl yapabileceğinizi göstereceğiz.

## Ön Adım: Bir API'yi içe aktarma

Azure API Management'te zaten bir API'niz varsa harika, bu adımı atlayabilirsiniz. Eğer yoksa, şu bağlantıya göz atın: [Azure API Management'e bir API içe aktarma ve yayınlama](https://learn.microsoft.com/en-us/azure/api-management/import-and-publish#import-and-publish-a-backend-api).

## API'yi MCP Sunucusu olarak açığa çıkarma

API uç noktalarını açığa çıkarmak için şu adımları izleyelim:

1. Azure Portal'a ve şu adrese gidin: <https://portal.azure.com/?Microsoft_Azure_ApiManagement=mcp> 
API Management örneğinize gidin.

1. Sol menüde, **APIs > MCP Servers > + Create new MCP Server** seçeneğini seçin.

1. API'de, bir MCP sunucusu olarak açığa çıkarılacak bir REST API seçin.

1. Araç olarak açığa çıkarılacak bir veya daha fazla API İşlemi seçin. Tüm işlemleri veya yalnızca belirli işlemleri seçebilirsiniz.

    ![Açığa çıkarılacak yöntemleri seçin](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/create-mcp-server-small.png)

1. **Create** seçeneğini seçin.

1. Menü seçeneği **APIs** ve **MCP Servers**'a gidin, aşağıdaki gibi bir görünüm görmelisiniz:

    ![Ana panelde MCP Sunucusunu görün](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-list.png)

    MCP sunucusu oluşturulur ve API işlemleri araçlar olarak açığa çıkarılır. MCP sunucusu MCP Servers panelinde listelenir. URL sütunu, test etmek veya bir istemci uygulamasında kullanmak için çağırabileceğiniz MCP sunucusunun uç noktasını gösterir.

## İsteğe Bağlı: Politikaları yapılandırma

Azure API Management, uç noktalarınız için hız sınırlama veya semantik önbellekleme gibi farklı kurallar belirlediğiniz politikaların temel kavramına sahiptir. Bu politikalar XML formatında yazılır.

MCP Sunucunuz için hız sınırlama politikası nasıl ayarlanır:

1. Portalda, **APIs** altında **MCP Servers**'ı seçin.

1. Oluşturduğunuz MCP sunucusunu seçin.

1. Sol menüde, MCP altında **Policies**'i seçin.

1. Politika düzenleyicisinde, MCP sunucusunun araçlarına uygulamak istediğiniz politikaları ekleyin veya düzenleyin. Politikalar XML formatında tanımlanır. Örneğin, MCP sunucusunun araçlarına yapılan çağrıları sınırlamak için bir politika ekleyebilirsiniz (bu örnekte, müşteri IP adresi başına 30 saniyede 5 çağrı). İşte hız sınırlama yapacak bir XML:

    ```xml
     <rate-limit-by-key calls="5" 
       renewal-period="30" 
       counter-key="@(context.Request.IpAddress)" 
       remaining-calls-variable-name="remainingCallsPerIP" 
    />
    ```

    İşte politika düzenleyicisinin bir görüntüsü:

    ![Politika düzenleyici](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-policies-small.png)

## Deneyin

MCP Sunucumuzun beklendiği gibi çalıştığından emin olalım.

Bunun için Visual Studio Code ve GitHub Copilot'un Agent modunu kullanacağız. MCP sunucusunu bir *mcp.json* dosyasına ekleyeceğiz. Bunu yaparak, Visual Studio Code bir istemci gibi davranacak ve son kullanıcılar bir istemciyle etkileşim kurmak için bir istem yazabilecek.

Nasıl yapılacağını görelim, MCP sunucusunu Visual Studio Code'a eklemek için:

1. Komut Paleti'nden MCP: **Add Server komutunu** kullanın.

1. İstendiğinde, sunucu türünü seçin: **HTTP (HTTP veya Server Sent Events)**.

1. API Management'teki MCP sunucusunun URL'sini girin. Örnek: **https://<apim-service-name>.azure-api.net/<api-name>-mcp/sse** (SSE uç noktası için) veya **https://<apim-service-name>.azure-api.net/<api-name>-mcp/mcp** (MCP uç noktası için), taşıma türleri arasındaki farkın `/sse` veya `/mcp` olduğunu unutmayın.

1. Seçtiğiniz bir sunucu kimliği girin. Bu önemli bir değer değildir ancak bu sunucu örneğinin ne olduğunu hatırlamanıza yardımcı olur.

1. Yapılandırmayı çalışma alanı ayarlarınıza mı yoksa kullanıcı ayarlarınıza mı kaydedeceğinizi seçin.

  - **Çalışma alanı ayarları** - Sunucu yapılandırması yalnızca mevcut çalışma alanında bulunan bir .vscode/mcp.json dosyasına kaydedilir.

    *mcp.json*

    ```json
    "servers": {
        "APIM petstore" : {
            "type": "sse",
            "url": "url-to-mcp-server/sse"
        }
    }
    ```

    veya taşıma olarak akışlı HTTP'yi seçerseniz biraz farklı olur:

    ```json
    "servers": {
        "APIM petstore" : {
            "type": "http",
            "url": "url-to-mcp-server/mcp"
        }
    }
    ```

  - **Kullanıcı ayarları** - Sunucu yapılandırması global *settings.json* dosyanıza eklenir ve tüm çalışma alanlarında kullanılabilir. Yapılandırma aşağıdaki gibi görünür:

    ![Kullanıcı ayarı](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-servers-visual-studio-code.png)

1. Ayrıca Azure API Management'e doğru şekilde kimlik doğrulaması yapmasını sağlamak için bir başlık eklemeniz gerekir. **Ocp-Apim-Subscription-Key** adlı bir başlık kullanır.

    - İşte ayarlara nasıl ekleyebileceğiniz:

    ![Kimlik doğrulama için başlık ekleme](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-with-header-visual-studio-code.png), bu, API anahtar değerini Azure Portal'da Azure API Management örneğiniz için bulmanızı isteyen bir istem görüntülenmesine neden olur.

   - Bunun yerine *mcp.json* dosyasına eklemek için şöyle ekleyebilirsiniz:

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

### Agent modunu kullanma

Artık ayarları veya *.vscode/mcp.json* dosyasını yapılandırdık. Deneyelim.

Sunucunuzdan açığa çıkarılan araçların listelendiği şu şekilde bir Araçlar simgesi olmalıdır:

![Sunucudan araçlar](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/tools-button-visual-studio-code.png)

1. Araçlar simgesine tıklayın ve aşağıdaki gibi bir araç listesi görmelisiniz:

    ![Araçlar](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/select-tools-visual-studio-code.png)

1. Aracı çağırmak için sohbette bir istem girin. Örneğin, bir sipariş hakkında bilgi almak için bir araç seçtiyseniz, ajana sipariş hakkında sorabilirsiniz. İşte bir örnek istem:

    ```text
    get information from order 2
    ```

    Şimdi bir aracı çağırmaya devam etmenizi isteyen bir araç simgesi görüntülenecektir. Aracı çalıştırmaya devam etmeyi seçin, şimdi aşağıdaki gibi bir çıktı görmelisiniz:

    ![İstemden sonuç](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/chat-results-visual-studio-code.png)

    **yukarıda gördüğünüz şey, ayarladığınız araçlara bağlıdır, ancak fikir, yukarıdaki gibi metinsel bir yanıt almanızdır**

## Referanslar

Daha fazla bilgi edinmek için:

- [Azure API Management ve MCP hakkında eğitim](https://learn.microsoft.com/en-us/azure/api-management/export-rest-mcp-server)
- [Python örneği: Azure API Management kullanarak uzak MCP sunucularını güvence altına alma (deneysel)](https://github.com/Azure-Samples/remote-mcp-apim-functions-python)

- [MCP istemci yetkilendirme laboratuvarı](https://github.com/Azure-Samples/AI-Gateway/tree/main/labs/mcp-client-authorization)

- [Azure API Management uzantısını kullanarak VS Code'da API'leri içe aktarma ve yönetme](https://learn.microsoft.com/en-us/azure/api-management/visual-studio-code-tutorial)

- [Azure API Center'da uzak MCP sunucularını kaydetme ve keşfetme](https://learn.microsoft.com/en-us/azure/api-center/register-discover-mcp-server)
- [AI Gateway](https://github.com/Azure-Samples/AI-Gateway) Azure API Management ile birçok AI yeteneğini gösteren harika bir repo
- [AI Gateway atölyeleri](https://azure-samples.github.io/AI-Gateway/) Azure Portal'ı kullanarak atölyeler içerir, AI yeteneklerini değerlendirmeye başlamak için harika bir yol.

**Feragatname**:  
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hata veya yanlışlıklar içerebileceğini lütfen unutmayın. Belgenin orijinal dili, yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımından kaynaklanan yanlış anlamalar veya yanlış yorumlamalar için sorumluluk kabul etmiyoruz.