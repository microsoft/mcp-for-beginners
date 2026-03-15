# MCP Sunucularını Dağıtma

MCP sunucunuzu dağıtmak, başkalarının araçlarına ve kaynaklarına yerel ortamınızın ötesinde erişmesini sağlar. Ölçeklenebilirlik, güvenilirlik ve yönetim kolaylığı gereksinimlerinize bağlı olarak değerlendirmeniz gereken birkaç dağıtım stratejisi vardır. Aşağıda MCP sunucularını yerel olarak, konteynerlerde ve buluta dağıtmak için rehberlik bulacaksınız.

## Genel Bakış

Bu ders, MCP Server uygulamanızı nasıl dağıtacağınızı kapsar.

## Öğrenme Hedefleri

Bu dersin sonunda şunları yapabileceksiniz:

- Farklı dağıtım yaklaşımlarını değerlendirmek.
- Uygulamanızı dağıtmak.

## Yerel geliştirme ve dağıtım

Sunucunuzun kullanıcıların makinelerinde çalışarak tüketilmesi amaçlanıyorsa, aşağıdaki adımları izleyebilirsiniz:

1. **Sunucuyu indirin**. Sunucuyu siz yazmadıysanız, önce makinize indirin.  
1. **Sunucu işlemini başlatın**: MCP sunucu uygulamanızı çalıştırın.

SSE için (stdio tipi sunucu için gerekmez)

1. **Ağ yapılandırması yapın**: Sunucunun beklenen portta erişilebilir olduğundan emin olun.  
1. **İstemcileri bağlayın**: `http://localhost:3000` gibi yerel bağlantı URL'lerini kullanın.

## Bulut Dağıtımı

MCP sunucuları çeşitli bulut platformlarına dağıtılabilir:

- **Sunucusuz Fonksiyonlar**: Hafif MCP sunucularını sunucusuz fonksiyon olarak dağıtın.
- **Konteyner Hizmetleri**: Azure Container Apps, AWS ECS veya Google Cloud Run gibi hizmetleri kullanın.
- **Kubernetes**: Yüksek kullanılabilirlik için MCP sunucularını Kubernetes kümelerinde dağıtın ve yönetin.

### Örnek: Azure Container Apps

Azure Container Apps, MCP Sunucularının dağıtımını destekler. Hala geliştirme aşamasında olup şu anda SSE sunucularını desteklemektedir.

Şöyle yapabilirsiniz:

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

  SSE sunucusu başlatıldıktan sonra JSON dosyasındaki oynat simgesine tıklayabilirsiniz, artık sunucudaki araçların GitHub Copilot tarafından alındığını görmelisiniz, Araç simgesine bakınız.

1. Dağıtmak için aşağıdaki komutu çalıştırın:

  ```sh
  az containerapp up -g <RESOURCE_GROUP_NAME> -n weather-mcp --environment mcp -l westus --env-vars API_KEYS=<AN_API_KEY> --source .
  ```

İşte bu kadar, yerel olarak dağıtın, Azure'a bu adımlarla dağıtın.

## Ek Kaynaklar

- [Azure Functions + MCP](https://learn.microsoft.com/en-us/samples/azure-samples/remote-mcp-functions-dotnet/remote-mcp-functions-dotnet/)
- [Azure Container Apps makalesi](https://techcommunity.microsoft.com/blog/appsonazureblog/host-remote-mcp-servers-in-azure-container-apps/4403550)
- [Azure Container Apps MCP repo](https://github.com/anthonychu/azure-container-apps-mcp-sample)


## Sonraki Konu

- Sonraki: [Gelişmiş Sunucu Konuları](../10-advanced/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Feragatname**:
Bu belge, AI çeviri servisi [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba sarf etsek de, otomatik çevirilerin hatalar veya yanlışlıklar içerebileceğini unutmayınız. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu ortaya çıkabilecek yanlış anlamalar veya yorum hatalarından sorumlu değiliz.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->