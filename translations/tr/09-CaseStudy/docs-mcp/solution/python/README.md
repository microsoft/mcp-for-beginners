# Chainlit ve Microsoft Learn Docs MCP ile Çalışma Planı Oluşturucu

## Ön Koşullar

- Python 3.8 veya daha üstü
- pip (Python paket yöneticisi)
- Microsoft Learn Docs MCP sunucusuna bağlanmak için internet erişimi

## Kurulum

1. Bu depoyu klonlayın veya proje dosyalarını indirin.
2. Gerekli bağımlılıkları yükleyin:

   ```bash
   pip install -r requirements.txt
   ```

## Kullanım

### Senaryo 1: Docs MCP'ye Basit Sorgu
Docs MCP sunucusuna bağlanan, bir sorgu gönderen ve sonucu yazdıran bir komut satırı istemcisi.

1. Scripti çalıştırın:
   ```bash
   python scenario1.py
   ```
2. İstemde dokümantasyon sorularınızı girin.

### Senaryo 2: Çalışma Planı Oluşturucu (Chainlit Web Uygulaması)
Kullanıcıların herhangi bir teknik konu için kişiselleştirilmiş, haftalık bir çalışma planı oluşturmasına olanak tanıyan Chainlit tabanlı bir web arayüzü.

1. Chainlit uygulamasını başlatın:
   ```bash
   chainlit run scenario2.py
   ```
2. Terminalinizde sağlanan yerel URL'yi (ör. http://localhost:8000) tarayıcınızda açın.
3. Sohbet penceresine çalışma konunuzu ve çalışmak istediğiniz hafta sayısını girin (ör. "AI-900 sertifikası, 8 hafta").
4. Uygulama, ilgili Microsoft Learn dokümantasyon bağlantılarını içeren haftalık bir çalışma planı ile yanıt verecektir.

**Gerekli Ortam Değişkenleri:**

Senaryo 2'yi (Azure OpenAI ile Chainlit web uygulaması) kullanmak için, `python` dizininde bir `.env` dosyasına aşağıdaki ortam değişkenlerini eklemeniz gerekir:

```
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=
AZURE_OPENAI_API_KEY=
AZURE_OPENAI_ENDPOINT=
AZURE_OPENAI_API_VERSION=
```

Uygulamayı çalıştırmadan önce bu değerleri Azure OpenAI kaynak bilgilerinizle doldurun.

> [!TIP]
> [Azure AI Foundry](https://ai.azure.com/) kullanarak kendi modellerinizi kolayca dağıtabilirsiniz.

### Senaryo 3: VS Code'da MCP Sunucusu ile Editör İçi Dokümantasyon

Tarayıcı sekmeleri arasında geçiş yapmak yerine, Microsoft Learn Docs'u doğrudan VS Code'a getirebilirsiniz. Bu, aşağıdakileri yapmanıza olanak tanır:
- Kodlama ortamınızı terk etmeden VS Code içinde doküman arama ve okuma.
- Dokümantasyon referansları ekleme ve bağlantıları doğrudan README veya kurs dosyalarınıza yerleştirme.
- GitHub Copilot ve MCP'yi birlikte kullanarak kesintisiz, yapay zeka destekli bir dokümantasyon iş akışı oluşturma.

**Örnek Kullanım Senaryoları:**
- Bir kurs veya proje dokümantasyonu yazarken README'ye hızlıca referans bağlantıları ekleme.
- Kod oluşturmak için Copilot'u kullanma ve ilgili dokümanları bulup alıntı yapmak için MCP'yi kullanma.
- Editörünüzde odaklanmış kalma ve üretkenliği artırma.

> [!IMPORTANT]
> Çalışma alanınızda geçerli bir [`mcp.json`](../../../../../../09-CaseStudy/docs-mcp/solution/scenario3/mcp.json) yapılandırması olduğundan emin olun (konum: `.vscode/mcp.json`).

## Senaryo 2 için Neden Chainlit?

Chainlit, konuşma tabanlı web uygulamaları oluşturmak için modern bir açık kaynak çerçevesidir. Microsoft Learn Docs MCP sunucusu gibi arka uç hizmetlerine bağlanan sohbet tabanlı kullanıcı arayüzleri oluşturmayı kolaylaştırır. Bu proje, gerçek zamanlı olarak kişiselleştirilmiş çalışma planları oluşturmanın basit ve etkileşimli bir yolunu sağlamak için Chainlit'i kullanır. Chainlit sayesinde, üretkenliği ve öğrenmeyi artıran sohbet tabanlı araçları hızlıca oluşturabilir ve dağıtabilirsiniz.

## Bu Uygulama Ne Yapar?

Bu uygulama, kullanıcıların yalnızca bir konu ve süre girerek kişiselleştirilmiş bir çalışma planı oluşturmasına olanak tanır. Uygulama, girdinizi analiz eder, Microsoft Learn Docs MCP sunucusundan ilgili içerikleri sorgular ve sonuçları yapılandırılmış, haftalık bir plana dönüştürür. Her haftanın önerileri sohbet penceresinde görüntülenir, bu da takip etmeyi ve ilerlemenizi izlemeyi kolaylaştırır. En güncel ve en alakalı öğrenme kaynaklarını almanızı sağlamak için entegrasyon yapılmıştır.

## Örnek Sorgular

Uygulamanın nasıl yanıt verdiğini görmek için sohbet penceresinde şu sorguları deneyin:

- `AI-900 sertifikası, 8 hafta`
- `Azure Functions öğren, 4 hafta`
- `Azure DevOps, 6 hafta`
- `Azure'da veri mühendisliği, 10 hafta`
- `Microsoft güvenlik temelleri, 5 hafta`
- `Power Platform, 7 hafta`
- `Azure AI hizmetleri, 12 hafta`
- `Bulut mimarisi, 9 hafta`

Bu örnekler, uygulamanın farklı öğrenme hedefleri ve zaman dilimleri için esnekliğini göstermektedir.

## Referanslar

- [Chainlit Dokümantasyonu](https://docs.chainlit.io/)
- [MCP Dokümantasyonu](https://github.com/MicrosoftDocs/mcp)

---

**Feragatname**:  
Bu belge, [Co-op Translator](https://github.com/Azure/co-op-translator) adlı yapay zeka çeviri hizmeti kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hata veya yanlışlıklar içerebileceğini lütfen unutmayın. Belgenin orijinal dili, yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel bir insan çevirisi önerilir. Bu çevirinin kullanımından kaynaklanan yanlış anlama veya yanlış yorumlamalardan sorumlu değiliz.