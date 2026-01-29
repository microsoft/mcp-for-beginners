# MCP Sunucularını Dağıtma

MCP sunucunuzu dağıtarak, araçlarına ve kaynaklarına yerel ortamınızın dışından erişilmesini sağlayabilirsiniz. Ölçeklenebilirlik, güvenilirlik ve yönetim kolaylığı gibi gereksinimlerinize bağlı olarak dikkate almanız gereken çeşitli dağıtım stratejileri vardır. Aşağıda MCP sunucularını yerel olarak, konteynerlerde ve buluta dağıtma rehberini bulacaksınız.

## Genel Bakış

Bu ders, MCP Server uygulamanızı nasıl dağıtacağınızı ele almaktadır.

## Öğrenme Hedefleri

Bu dersin sonunda şunları yapabileceksiniz:

- Farklı dağıtım yaklaşımlarını değerlendirmek.
- Uygulamanızı dağıtmak.

## Yerel geliştirme ve dağıtım

Sunucunuzun kullanıcıların makinelerinde çalıştırılarak kullanılacaksa, aşağıdaki adımları izleyebilirsiniz:

1. **Sunucuyu indirin**. Sunucuyu siz yazmadıysanız, önce makinenize indirin.  
1. **Sunucu sürecini başlatın**: MCP sunucu uygulamanızı çalıştırın.

SSE için (stdio tipi sunucu için gerekmez)

1. **Ağ yapılandırmasını yapın**: Sunucunun beklenen port üzerinden erişilebilir olduğundan emin olun.  
1. **İstemcileri bağlayın**: `http://localhost:3000` gibi yerel bağlantı URL’lerini kullanın.

## Bulut Dağıtımı

MCP sunucuları çeşitli bulut platformlarına dağıtılabilir:

- **Serverless Fonksiyonlar**: Hafif MCP sunucularını serverless fonksiyonlar olarak dağıtın.  
- **Konteyner Servisleri**: Azure Container Apps, AWS ECS veya Google Cloud Run gibi servisleri kullanın.  
- **Kubernetes**: Yüksek erişilebilirlik için MCP sunucularını Kubernetes kümelerinde dağıtın ve yönetin.

### Örnek: Azure Container Apps

Azure Container Apps, MCP Sunucularının dağıtımını destekler. Hâlâ geliştirme aşamasında olup şu anda SSE sunucularını desteklemektedir.

Bunu nasıl yapabileceğiniz aşağıda açıklanmıştır:

1. Bir repo klonlayın:

  ```sh
  git clone https://github.com/anthonychu/azure-container-apps-mcp-sample.git
  ```

1. Yerelde test etmek için çalıştırın:

  ```sh
  uv venv
  uv sync

  # linux/macOS
  export API_KEYS=<AN_API_KEY>
  # windows
  set API_KEYS=<AN_API_KEY>

  uv run fastapi dev main.py
  ```

1. Yerelde denemek için, *.vscode* dizininde *mcp.json* dosyası oluşturun ve aşağıdaki içeriği ekleyin:

  ```json
  {
      "inputs": [
          {
              "type": "promptString",
              "id": "weather-api-key",
              "description": "Weather API Key",
              "password": true
          }
      ],
      "servers": {
          "weather-sse": {
              "type": "sse",
              "url": "http://localhost:8000/sse",
              "headers": {
                  "x-api-key": "${input:weather-api-key}"
              }
          }
      }
  }
  ```

  SSE sunucusu başlatıldıktan sonra, JSON dosyasındaki oynat düğmesine tıklayabilirsiniz; artık GitHub Copilot tarafından sunucudaki araçların algılandığını, Araç simgesini görebilirsiniz.

1. Dağıtmak için aşağıdaki komutu çalıştırın:

  ```sh
  az containerapp up -g <RESOURCE_GROUP_NAME> -n weather-mcp --environment mcp -l westus --env-vars API_KEYS=<AN_API_KEY> --source .
  ```

İşte bu kadar, yerelde dağıtın veya bu adımlarla Azure’a dağıtın.

## Ek Kaynaklar

- [Azure Functions + MCP](https://learn.microsoft.com/en-us/samples/azure-samples/remote-mcp-functions-dotnet/remote-mcp-functions-dotnet/)  
- [Azure Container Apps makalesi](https://techcommunity.microsoft.com/blog/appsonazureblog/host-remote-mcp-servers-in-azure-container-apps/4403550)  
- [Azure Container Apps MCP repo](https://github.com/anthonychu/azure-container-apps-mcp-sample)  

## Sonraki Adım

- Sonraki: [Pratik Uygulama](../../04-PracticalImplementation/README.md)

**Feragatname**:  
Bu belge, AI çeviri servisi [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hatalar veya yanlışlıklar içerebileceğini lütfen unutmayınız. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu oluşabilecek yanlış anlamalar veya yorum hatalarından sorumlu değiliz.