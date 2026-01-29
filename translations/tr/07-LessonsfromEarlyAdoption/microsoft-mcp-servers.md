# 🚀 Geliştirici Verimliliğini Dönüştüren 10 Microsoft MCP Sunucusu

## 🎯 Bu Rehberde Neler Öğreneceksiniz

Bu pratik rehber, geliştiricilerin AI asistanlarıyla çalışma şeklini aktif olarak dönüştüren on Microsoft MCP sunucusunu tanıtıyor. MCP sunucularının *neler yapabileceğini* anlatmak yerine, Microsoft ve ötesinde günlük geliştirme iş akışlarında gerçek fark yaratan sunucuları göstereceğiz.

Bu rehberdeki her sunucu, gerçek dünya kullanımı ve geliştirici geri bildirimlerine dayanarak seçildi. Her sunucunun ne yaptığını değil, neden önemli olduğunu ve kendi projelerinizde en iyi şekilde nasıl kullanacağınızı keşfedeceksiniz. MCP’ye tamamen yeniyseniz ya da mevcut kurulumunuzu genişletmek istiyorsanız, bu sunucular Microsoft ekosistemindeki en pratik ve etkili araçlardan bazılarını temsil ediyor.

> **💡 Hızlı Başlangıç İpucu**
> 
> MCP’ye yeni misiniz? Endişelenmeyin! Bu rehber başlangıç seviyesine uygun olarak hazırlandı. Kavramları adım adım açıklayacağız ve her zaman [MCP’ye Giriş](../00-Introduction/README.md) ve [Temel Kavramlar](../01-CoreConcepts/README.md) modüllerimize dönerek daha derin bilgi edinebilirsiniz.

## Genel Bakış

Bu kapsamlı rehber, geliştiricilerin AI asistanları ve dış araçlarla etkileşim şeklini devrim niteliğinde değiştiren on Microsoft MCP sunucusunu inceliyor. Azure kaynak yönetiminden belge işlemeye kadar, bu sunucular Model Context Protocol’ün sorunsuz ve verimli geliştirme iş akışları yaratmadaki gücünü gösteriyor.

## Öğrenme Hedefleri

Bu rehberin sonunda:
- MCP sunucularının geliştirici verimliliğini nasıl artırdığını anlayacaksınız
- Microsoft’un en etkili MCP sunucu uygulamalarını öğreneceksiniz
- Her sunucu için pratik kullanım senaryolarını keşfedeceksiniz
- Bu sunucuları VS Code ve Visual Studio’da nasıl kurup yapılandıracağınızı bileceksiniz
- Daha geniş MCP ekosistemini ve gelecekteki yönelimleri keşfedeceksiniz

## 🔧 MCP Sunucularını Anlamak: Yeni Başlayanlar İçin Rehber

### MCP Sunucuları Nedir?

Model Context Protocol (MCP) konusunda yeniyseniz, “MCP sunucusu tam olarak nedir ve neden önemlidir?” diye merak ediyor olabilirsiniz. Basit bir benzetmeyle başlayalım.

MCP sunucularını, AI kodlama yardımcınızın (örneğin GitHub Copilot) dış araçlar ve hizmetlerle bağlantı kurmasına yardımcı olan özel asistanlar olarak düşünebilirsiniz. Telefonunuzda farklı işler için farklı uygulamalar kullanmanız gibi—biri hava durumu için, biri navigasyon için, biri bankacılık için—MCP sunucuları da AI asistanınıza farklı geliştirme araçları ve hizmetleriyle etkileşim kurma yeteneği verir.

### MCP Sunucularının Çözdüğü Sorun

MCP sunucuları olmadan, eğer:
- Azure kaynaklarınızı kontrol etmek,
- GitHub’da bir issue oluşturmak,
- Veritabanınızı sorgulamak,
- Dokümantasyon içinde arama yapmak

istiyorsanız, kodlamayı bırakıp tarayıcı açmanız, ilgili siteye gitmeniz ve bu işlemleri manuel yapmanız gerekirdi. Bu sürekli bağlam değiştirme, akışınızı böler ve verimliliği düşürür.

### MCP Sunucuları Geliştirme Deneyiminizi Nasıl Dönüştürür?

MCP sunucuları sayesinde, geliştirme ortamınızda (VS Code, Visual Studio vb.) kalabilir ve AI asistanınızdan bu işleri yapmasını isteyebilirsiniz. Örneğin:

**Geleneksel iş akışı yerine:**
1. Kodlamayı durdur
2. Tarayıcıyı aç
3. Azure portalına git
4. Depolama hesabı detaylarını kontrol et
5. VS Code’a dön
6. Kodlamaya devam et

**Şimdi bunu yapabilirsiniz:**
1. AI’a sor: "Azure depolama hesaplarımın durumu nedir?"
2. Sağlanan bilgilerle kodlamaya devam et

### Yeni Başlayanlar İçin Temel Faydalar

#### 1. 🔄 **Akış Halinde Kalın**
- Birden fazla uygulama arasında geçiş yapmaya son
- Yazdığınız koda odaklanmaya devam edin
- Farklı araçları yönetmenin zihinsel yükünü azaltın

#### 2. 🤖 **Karmaşık Komutlar Yerine Doğal Dil Kullanın**
- SQL sözdizimini ezberlemek yerine ihtiyacınız olan veriyi anlatın
- Azure CLI komutlarını hatırlamak yerine yapmak istediğinizi açıklayın
- Teknik detayları AI’a bırakın, siz mantığa odaklanın

#### 3. 🔗 **Birden Fazla Aracı Bir Araya Getirin**
- Farklı hizmetleri birleştirerek güçlü iş akışları oluşturun
- Örnek: "Tüm yeni GitHub issue’larını al ve karşılık gelen Azure DevOps iş öğeleri oluştur"
- Karmaşık betikler yazmadan otomasyon kurun

#### 4. 🌐 **Genişleyen Bir Ekosisteme Erişin**
- Microsoft, GitHub ve diğer şirketlerin geliştirdiği sunuculardan faydalanın
- Farklı satıcıların araçlarını sorunsuzca karıştırıp eşleştirin
- Farklı AI asistanları arasında çalışan standart bir ekosisteme katılın

#### 5. 🛠️ **Yaparak Öğrenin**
- Kavramları anlamak için önceden hazırlanmış sunucularla başlayın
- Rahatladıkça kendi sunucularınızı geliştirin
- Mevcut SDK’lar ve dokümantasyonla öğrenmenizi destekleyin

### Yeni Başlayanlar İçin Gerçek Dünya Örneği

Diyelim ki web geliştirmeye yeni başladınız ve ilk projeniz üzerinde çalışıyorsunuz. MCP sunucuları size nasıl yardımcı olabilir:

**Geleneksel yöntem:**
```
1. Code a feature
2. Open browser → Navigate to GitHub
3. Create an issue for testing
4. Open another tab → Check Azure docs for deployment
5. Open third tab → Look up database connection examples
6. Return to VS Code
7. Try to remember what you were doing
```

**MCP sunucularıyla:**
```
1. Code a feature
2. Ask AI: "Create a GitHub issue for testing this login feature"
3. Ask AI: "How do I deploy this to Azure according to the docs?"
4. Ask AI: "Show me the best way to connect to my database"
5. Continue coding with all the information you need
```

### Kurumsal Standart Avantajı

MCP, sektör çapında bir standart haline geliyor, bu da:
- **Tutarlılık**: Farklı araçlar ve şirketler arasında benzer deneyim
- **Birlikte Çalışabilirlik**: Farklı satıcıların sunucuları birlikte çalışabilir
- **Geleceğe Hazırlık**: Beceriler ve kurulumlar farklı AI asistanları arasında taşınabilir
- **Topluluk**: Paylaşılan bilgi ve kaynakların geniş ekosistemi

### Başlarken: Neler Öğreneceksiniz

Bu rehberde, her seviyeden geliştirici için özellikle faydalı olan 10 Microsoft MCP sunucusunu inceleyeceğiz. Her sunucu:
- Yaygın geliştirme zorluklarını çözer
- Tekrarlayan işleri azaltır
- Kod kalitesini artırır
- Öğrenme fırsatlarını geliştirir

> **💡 Öğrenme İpucu**
> 
> MCP’ye tamamen yeniyseniz, önce [MCP’ye Giriş](../00-Introduction/README.md) ve [Temel Kavramlar](../01-CoreConcepts/README.md) modüllerimizle başlayın. Sonra buraya dönüp gerçek Microsoft araçlarıyla bu kavramları uygulamalı görün.
>
> MCP’nin önemine dair ek bağlam için Maria Naggaga’nın yazısını okuyabilirsiniz: [Connect Once, Integrate Anywhere with MCP](https://devblogs.microsoft.com/blog/connect-once-integrate-anywhere-with-mcps).

## VS Code ve Visual Studio’da MCP ile Başlamak 🚀

Bu MCP sunucularını kurmak, GitHub Copilot ile Visual Studio Code veya Visual Studio 2022 kullanıyorsanız oldukça basittir.

### VS Code Kurulumu

VS Code için temel süreç:

1. **Agent Modunu Etkinleştir**: VS Code’da Copilot Chat penceresinde Agent moduna geçin
2. **MCP Sunucularını Yapılandır**: Sunucu yapılandırmalarını VS Code settings.json dosyanıza ekleyin
3. **Sunucuları Başlat**: Kullanmak istediğiniz her sunucu için "Başlat" düğmesine tıklayın
4. **Araçları Seç**: Mevcut oturumunuz için hangi MCP sunucularını etkinleştireceğinizi seçin

Detaylı kurulum talimatları için [VS Code MCP dokümantasyonuna](https://code.visualstudio.com/docs/copilot/copilot-mcp) bakabilirsiniz.

> **💡 Uzman İpucu: MCP Sunucularını Profesyonelce Yönetin!**
> 
> VS Code Extensions görünümüne artık [kurulu MCP Sunucularını yönetmek için kullanışlı yeni bir arayüz](https://code.visualstudio.com/docs/copilot/chat/mcp-servers#_use-mcp-tools-in-agent-mode) eklendi! Kurulu MCP Sunucularını başlatmak, durdurmak ve yönetmek için hızlı ve basit bir arayüz sunuyor. Deneyin!

### Visual Studio 2022 Kurulumu

Visual Studio 2022 (17.14 veya üzeri sürüm) için:

1. **Agent Modunu Etkinleştir**: GitHub Copilot Chat penceresindeki "Ask" açılır menüsünden "Agent" seçeneğini seçin
2. **Yapılandırma Dosyası Oluştur**: Çözüm dizininizde `.mcp.json` dosyası oluşturun (önerilen konum: `<SOLUTIONDIR>\.mcp.json`)
3. **Sunucuları Yapılandır**: MCP sunucu yapılandırmalarınızı standart MCP formatında ekleyin
4. **Araç Onayı**: İstendiğinde, kullanmak istediğiniz araçları uygun kapsam izinleriyle onaylayın

Detaylı Visual Studio kurulum talimatları için [Visual Studio MCP dokümantasyonuna](https://learn.microsoft.com/visualstudio/ide/mcp-servers) bakabilirsiniz.

Her MCP sunucusunun kendi yapılandırma gereksinimleri (bağlantı dizeleri, kimlik doğrulama vb.) vardır, ancak her iki IDE’de de kurulum deseni tutarlıdır.

## Microsoft MCP Sunucularından Alınan Dersler 🛠️

### 1. 📚 Microsoft Learn Docs MCP Sunucusu

[![VS Code’da Kur](https://img.shields.io/badge/VS_Code-Install_Microsoft_Docs_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=microsoft.docs.mcp&config=%7B%22type%22%3A%22http%22%2C%22url%22%3A%22https%3A%2F%2Flearn.microsoft.com%2Fapi%2Fmcp%22%7D) [![VS Code Insiders’da Kur](https://img.shields.io/badge/VS_Code_Insiders-Install_Microsoft_Docs_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=microsoft.docs.mcp&config=%7B%22type%22%3A%22http%22%2C%22url%22%3A%22https%3A%2F%2Flearn.microsoft.com%2Fapi%2Fmcp%22%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/microsoft/mcp)

**Ne yapar**: Microsoft Learn Docs MCP Sunucusu, AI asistanlarına Model Context Protocol aracılığıyla resmi Microsoft dokümantasyonuna gerçek zamanlı erişim sağlayan bulut tabanlı bir hizmettir. `https://learn.microsoft.com/api/mcp` adresine bağlanır ve Microsoft Learn, Azure dokümantasyonu, Microsoft 365 dokümantasyonu ve diğer resmi Microsoft kaynakları arasında anlamsal arama yapılmasını mümkün kılar.

**Neden faydalı**: Sadece “dokümantasyon” gibi görünse de, bu sunucu Microsoft teknolojilerini kullanan her geliştirici için kritik önemdedir. .NET geliştiricilerinin AI kodlama asistanlarıyla ilgili en büyük şikayetlerinden biri, asistanların en güncel .NET ve C# sürümlerine hakim olmamasıdır. Microsoft Learn Docs MCP Sunucusu, en güncel dokümantasyon, API referansları ve en iyi uygulamalara gerçek zamanlı erişim sağlayarak bu sorunu çözer. En son Azure SDK’larıyla çalışıyor olun, yeni C# 13 özelliklerini keşfediyor olun ya da ileri düzey .NET Aspire desenlerini uyguluyor olun, bu sunucu AI asistanınızın doğru ve modern kod üretmesi için yetkili ve güncel bilgiye erişmesini sağlar.

**Gerçek dünya kullanımı**: “Resmi Microsoft Learn dokümantasyonuna göre Azure container app oluşturmak için az cli komutları nelerdir?” veya “ASP.NET Core’da Entity Framework’ü dependency injection ile nasıl yapılandırırım?” ya da “Bu kodu Microsoft Learn Dokümantasyonundaki performans önerileriyle uyumlu mu diye incele.” Sunucu, Microsoft Learn, Azure dokümanları ve Microsoft 365 dokümantasyonu genelinde gelişmiş anlamsal arama yaparak en bağlama uygun bilgileri bulur. En fazla 10 yüksek kaliteli içerik parçası, makale başlıkları ve URL’leri ile döner; her zaman yayımlanan en güncel Microsoft dokümantasyonuna erişir.

**Öne çıkan örnek**: Sunucu, Microsoft’un resmi teknik dokümantasyonuna karşı anlamsal arama yapan `microsoft_docs_search` aracını sunar. Yapılandırıldıktan sonra, “ASP.NET Core’da JWT kimlik doğrulamasını nasıl uygularım?” gibi sorular sorabilir ve kaynak bağlantılarıyla detaylı, resmi yanıtlar alabilirsiniz. Arama kalitesi mükemmeldir çünkü bağlamı anlar – Azure bağlamında “containers” sorulduğunda Azure Container Instances dokümantasyonunu, .NET bağlamında ise ilgili C# koleksiyon bilgilerini getirir.

Bu, hızla değişen veya yakın zamanda güncellenen kütüphaneler ve kullanım senaryoları için özellikle faydalıdır. Örneğin, bazı son kodlama projelerimde .NET Aspire ve Microsoft.Extensions.AI’nin en son sürümlerindeki özellikleri kullanmak istedim. Microsoft Learn Docs MCP sunucusunu dahil ederek sadece API dokümanlarına değil, yeni yayımlanmış rehberlik ve örneklere de erişebildim.
> **💡 Profesyonel İpucu**
> 
> Araç dostu modellerin bile MCP araçlarını kullanmaları için teşvik edilmeye ihtiyacı vardır! Bir sistem istemi veya [copilot-instructions.md](https://docs.github.com/copilot/how-tos/custom-instructions/adding-repository-custom-instructions-for-github-copilot) eklemeyi düşünebilirsiniz, örneğin: "Microsoft teknolojileriyle ilgili soruları yanıtlarken C#, Azure, ASP.NET Core veya Entity Framework gibi konularda Microsoft’un en güncel resmi dokümantasyonunu aramak için `microsoft.docs.mcp` aracına erişiminiz var."
>
> Bunun harika bir örneğini görmek için Awesome GitHub Copilot deposundaki [C# .NET Janitor sohbet modu](https://github.com/awesome-copilot/chatmodes/blob/main/csharp-dotnet-janitor.chatmode.md) sayfasına göz atabilirsiniz. Bu mod, özellikle Microsoft Learn Docs MCP sunucusunu kullanarak C# kodunu en güncel kalıplar ve en iyi uygulamalarla temizlemeye ve modernize etmeye yardımcı olur.
### 2. ☁️ Azure MCP Sunucusu

[![VS Code'da Yükle](https://img.shields.io/badge/VS_Code-Install_Azure_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=Azure%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40azure%2Fazure-mcp%40latest%22%5D%7D) [![VS Code Insiders'da Yükle](https://img.shields.io/badge/VS_Code_Insiders-Install_Azure_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Azure%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40azure%2Fazure-mcp%40latest%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Azure/azure-mcp)

**Ne yapar**: Azure MCP Sunucusu, 15'ten fazla özel Azure hizmet bağlayıcısından oluşan kapsamlı bir pakettir ve tüm Azure ekosistemini AI iş akışınıza getirir. Bu sadece tek bir sunucu değil – kaynak yönetimi, veritabanı bağlantısı (PostgreSQL, SQL Server), KQL ile Azure Monitor günlük analizi, Cosmos DB entegrasyonu ve çok daha fazlasını içeren güçlü bir koleksiyondur.

**Neden faydalı**: Sadece Azure kaynaklarını yönetmenin ötesinde, bu sunucu Azure SDK'ları ile çalışırken kod kalitesini önemli ölçüde artırır. Azure MCP'yi Agent modunda kullandığınızda, sadece kod yazmanıza yardımcı olmakla kalmaz – güncel kimlik doğrulama kalıplarını, hata yönetimi en iyi uygulamalarını takip eden ve en son SDK özelliklerini kullanan *daha iyi* Azure kodu yazmanıza destek olur. Çalışabilecek genel kodlar yerine, üretim iş yükleri için Azure'un önerdiği kalıplara uygun kodlar elde edersiniz.

**Ana modüller şunları içerir**:
- **🗄️ Veritabanı Bağlayıcıları**: Azure Database for PostgreSQL ve SQL Server’a doğal dil ile doğrudan erişim
- **📊 Azure Monitor**: KQL destekli günlük analizi ve operasyonel içgörüler
- **🌐 Kaynak Yönetimi**: Tam Azure kaynak yaşam döngüsü yönetimi
- **🔐 Kimlik Doğrulama**: DefaultAzureCredential ve yönetilen kimlik kalıpları
- **📦 Depolama Hizmetleri**: Blob Storage, Queue Storage ve Table Storage işlemleri
- **🚀 Konteyner Hizmetleri**: Azure Container Apps, Container Instances ve AKS yönetimi
- **Ve daha birçok özel bağlayıcı**

**Gerçek dünya kullanımı**: "Azure depolama hesaplarımı listele", "Son bir saatteki hatalar için Log Analytics çalışma alanımı sorgula" veya "Node.js kullanarak doğru kimlik doğrulama ile Azure uygulaması oluşturmama yardım et"

**Tam demo senaryosu**: İşte Azure MCP ile GitHub Copilot for Azure uzantısını VS Code’da birleştirmenin gücünü gösteren tam bir örnek. İkisi yüklü olduğunda ve şu komutu verdiğinizde:

> "DefaultAzureCredential kimlik doğrulaması kullanarak Azure Blob Storage’a dosya yükleyen bir Python betiği oluştur. Betik, 'mycompanystorage' adlı Azure depolama hesabıma bağlanmalı, 'documents' adlı bir konteynıra yükleme yapmalı, yüklemek için güncel zaman damgası içeren bir test dosyası oluşturmalı, hataları düzgün yönetmeli ve bilgilendirici çıktı sağlamalı, Azure kimlik doğrulama ve hata yönetimi en iyi uygulamalarını takip etmeli, DefaultAzureCredential kimlik doğrulamasının nasıl çalıştığını açıklayan yorumlar içermeli ve betik iyi yapılandırılmış, fonksiyonlar ve dokümantasyon içermeli."

Azure MCP Sunucusu, aşağıdaki özelliklere sahip tam, üretime hazır bir Python betiği oluşturacaktır:
- En son Azure Blob Storage SDK’sını uygun async kalıplarla kullanır
- DefaultAzureCredential’ı kapsamlı bir yedekleme zinciri açıklamasıyla uygular
- Belirli Azure istisna türleriyle sağlam hata yönetimi içerir
- Azure SDK en iyi uygulamalarına uygun kaynak yönetimi ve bağlantı işlemleri yapar
- Ayrıntılı günlük kaydı ve bilgilendirici konsol çıktısı sağlar
- Fonksiyonlar, dokümantasyon ve tip ipuçlarıyla düzgün yapılandırılmış bir betik oluşturur

Bunu özel kılan şey, Azure MCP olmadan, çalışabilecek ama güncel Azure kalıplarını takip etmeyen genel blob storage kodu almanızdır. Azure MCP ile en son kimlik doğrulama yöntemlerini kullanan, Azure’a özgü hata senaryolarını yöneten ve Microsoft’un üretim uygulamaları için önerdiği uygulamaları takip eden kod elde edersiniz.

**Öne çıkan örnek**: `az` ve `azd` CLI komutlarını anımsamakta zorlanıyorum. Benim için her zaman iki aşamalı bir süreç: önce sözdizimini araştırmak, sonra komutu çalıştırmak. Genellikle portalda dolaşıp işimi halletmek zorunda kalıyorum çünkü CLI sözdizimini hatırlayamadığımı kabul etmek istemiyorum. İstediğimi sadece tarif edebilmek harika ve bunu IDE’den çıkmadan yapabilmek daha da iyi!

Başlamak için [Azure MCP deposundaki](https://github.com/Azure/azure-mcp?tab=readme-ov-file#-what-can-you-do-with-the-azure-mcp-server) harika bir kullanım senaryoları listesi var. Kapsamlı kurulum rehberleri ve gelişmiş yapılandırma seçenekleri için [resmi Azure MCP dokümantasyonuna](https://learn.microsoft.com/azure/developer/azure-mcp-server/) göz atabilirsiniz.

### 3. 🐙 GitHub MCP Sunucusu

[![VS Code'da Yükle](https://img.shields.io/badge/VS_Code-Install_Server-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=github&config=%7B%22type%22%3A%20%22http%22%2C%22url%22%3A%20%22https%3A%2F%2Fapi.githubcopilot.com%2Fmcp%2F%22%7D) [![VS Code Insiders'da Yükle](https://img.shields.io/badge/VS_Code_Insiders-Install_Server-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=github&config=%7B%22type%22%3A%20%22http%22%2C%22url%22%3A%20%22https%3A%2F%2Fapi.githubcopilot.com%2Fmcp%2F%22%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/github/github-mcp-server)

**Ne yapar**: Resmi GitHub MCP Sunucusu, GitHub’ın tüm ekosistemiyle sorunsuz entegrasyon sağlar ve hem barındırılan uzak erişim hem de yerel Docker dağıtımı seçenekleri sunar. Bu sadece temel depo işlemleriyle ilgili değil – GitHub Actions yönetimi, pull request iş akışları, sorun takibi, güvenlik taramaları, bildirimler ve gelişmiş otomasyon yeteneklerini içeren kapsamlı bir araç setidir.

**Neden faydalı**: Bu sunucu, GitHub ile etkileşiminizi tamamen değiştirir ve tüm platform deneyimini doğrudan geliştirme ortamınıza getirir. Proje yönetimi, kod incelemeleri ve CI/CD takibi için sürekli VS Code ile GitHub.com arasında geçiş yapmak yerine, her şeyi doğal dil komutlarıyla kodunuza odaklanarak halledebilirsiniz.

> **ℹ️ Not: Farklı 'Agent' Türleri**
> 
> Bu GitHub MCP Sunucusunu, GitHub’ın Kodlama Agent’ı (otomatik kodlama görevleri için sorunlara atayabileceğiniz AI agent) ile karıştırmayın. GitHub MCP Sunucusu, VS Code’un Agent modunda GitHub API entegrasyonu sağlarken, GitHub Kodlama Agent’ı atandığında pull request oluşturan ayrı bir özelliktir.

**Ana özellikler şunlardır**:
- **⚙️ GitHub Actions**: Tam CI/CD boru hattı yönetimi, iş akışı takibi ve artefakt işlemleri
- **🔀 Pull Requestler**: PR oluşturma, inceleme, birleştirme ve kapsamlı durum takibi
- **🐛 Sorunlar**: Tam sorun yaşam döngüsü yönetimi, yorumlama, etiketleme ve atama
- **🔒 Güvenlik**: Kod tarama uyarıları, gizli anahtar tespiti ve Dependabot entegrasyonu
- **🔔 Bildirimler**: Akıllı bildirim yönetimi ve depo abonelik kontrolü
- **📁 Depo Yönetimi**: Dosya işlemleri, dal yönetimi ve depo idaresi
- **👥 İşbirliği**: Kullanıcı ve organizasyon araması, ekip yönetimi ve erişim kontrolü

**Gerçek dünya kullanımı**: "Özellik dalımdan bir pull request oluştur", "Bu hafta başarısız olan tüm CI çalıştırmalarını göster", "Depolarımdaki açık güvenlik uyarılarını listele" veya "Organizasyonlarımda bana atanmış tüm sorunları bul"

**Tam demo senaryosu**: İşte GitHub MCP Sunucusunun yeteneklerini gösteren güçlü bir iş akışı:

> "Sprint incelememize hazırlanmalıyım. Bu hafta oluşturduğum tüm pull requestleri göster, CI/CD boru hatlarımızın durumunu kontrol et, ele almamız gereken güvenlik uyarılarının özetini oluştur ve 'feature' etiketiyle birleştirilen PR’lere dayanarak sürüm notları taslağı hazırlamama yardım et."

GitHub MCP Sunucusu:
- Son pull requestlerinizi detaylı durum bilgileriyle sorgular
- İş akışı çalıştırmalarını analiz eder ve başarısızlıkları veya performans sorunlarını vurgular
- Güvenlik tarama sonuçlarını derler ve kritik uyarıları önceliklendirir
- Birleştirilen PR’lerden bilgi çıkararak kapsamlı sürüm notları oluşturur
- Sprint planlaması ve sürüm hazırlığı için uygulanabilir sonraki adımları sunar

**Öne çıkan örnek**: Kod inceleme iş akışları için bunu kullanmayı çok seviyorum. VS Code, GitHub bildirimleri ve pull request sayfaları arasında geçiş yapmak yerine, "İncelememi bekleyen tüm PR’leri göster" diyebiliyorum, ardından "PR #123’e kimlik doğrulama yöntemindeki hata yönetimi hakkında yorum ekle" diyorum. Sunucu GitHub API çağrılarını yapıyor, tartışma bağlamını koruyor ve daha yapıcı inceleme yorumları yazmama bile yardımcı oluyor.

**Kimlik doğrulama seçenekleri**: Sunucu hem OAuth’u (VS Code’da sorunsuz) hem de Kişisel Erişim Token’larını destekler ve sadece ihtiyacınız olan GitHub işlevselliğini etkinleştirmek için yapılandırılabilir araç setleri sunar. Anında kurulum için uzak barındırılan hizmet olarak veya tam kontrol için Docker ile yerel olarak çalıştırabilirsiniz.

> **💡 İpucu**
> 
> MCP sunucu ayarlarınızda `--toolsets` parametresini yapılandırarak sadece ihtiyacınız olan araç setlerini etkinleştirip bağlam boyutunu küçültebilir ve AI araç seçimini iyileştirebilirsiniz. Örneğin, temel geliştirme iş akışları için MCP yapılandırma argümanlarınıza `"--toolsets", "repos,issues,pull_requests,actions"` ekleyin veya öncelikle GitHub izleme özellikleri istiyorsanız `"--toolsets", "notifications, security"` kullanın.

### 4. 🔄 Azure DevOps MCP Sunucusu

[![VS Code'da Yükle](https://img.shields.io/badge/VS_Code-Install_Azure_DevOps_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=Azure%20DevOps%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-azure-devops%40latest%22%5D%7D) [![VS Code Insiders'da Yükle](https://img.shields.io/badge/VS_Code_Insiders-Install_Azure_DevOps_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Azure%20DevOps%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-azure-devops%40latest%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/microsoft/azure-devops-mcp)

**Ne yapar**: Azure DevOps hizmetlerine bağlanarak kapsamlı proje yönetimi, iş öğesi takibi, derleme boru hattı yönetimi ve depo işlemleri sağlar.

**Neden faydalı**: Azure DevOps’u ana DevOps platformu olarak kullanan ekipler için, bu MCP sunucusu geliştirme ortamınız ile Azure DevOps web arayüzü arasında sürekli sekme değiştirme ihtiyacını ortadan kaldırır. İş öğelerini yönetebilir, derleme durumlarını kontrol edebilir, depoları sorgulayabilir ve proje yönetimi görevlerini AI asistanınızdan doğrudan halledebilirsiniz.

**Gerçek dünya kullanımı**: "WebApp projesi için mevcut sprintteki tüm aktif iş öğelerini göster", "Yeni bulduğum giriş sorunu için hata raporu oluştur" veya "Derleme boru hatlarımızın durumunu kontrol et ve son başarısızlıkları göster"

**Öne çıkan örnek**: Geliştirme ortamınızı terk etmeden, "WebApp projesi için mevcut sprintteki tüm aktif iş öğelerini göster" veya "Yeni bulduğum giriş sorunu için hata raporu oluştur" gibi basit sorgularla ekibinizin mevcut sprint durumunu kolayca kontrol edebilirsiniz.

### 5. 📝 MarkItDown MCP Sunucusu
[![Install in VS Code](https://img.shields.io/badge/VS_Code-Install_MarkItDown_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=MarkItDown%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-markitdown%40latest%22%5D%7D) [![Install in VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_MarkItDown_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=MarkItDown%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-markitdown%40latest%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/microsoft/markitdown)

**Ne yapar**: MarkItDown, çeşitli dosya formatlarını yüksek kaliteli Markdown’a dönüştüren kapsamlı bir belge dönüştürme sunucusudur. Bu Markdown, LLM tüketimi ve metin analiz iş akışları için optimize edilmiştir.

**Neden faydalı**: Modern dokümantasyon iş akışları için vazgeçilmez! MarkItDown, başlıklar, listeler, tablolar ve bağlantılar gibi kritik belge yapısını korurken etkileyici bir dosya formatı yelpazesini işler. Basit metin çıkarma araçlarının aksine, hem yapay zeka işlemleri hem de insan okunabilirliği için değerli olan anlamsal anlam ve biçimlendirmeyi korumaya odaklanır.

**Desteklenen dosya formatları**:
- **Office Belgeleri**: PDF, PowerPoint (PPTX), Word (DOCX), Excel (XLSX/XLS)
- **Medya Dosyaları**: Görseller (EXIF meta verisi ve OCR ile), Ses (EXIF meta verisi ve konuşma transkripsiyonu ile)
- **Web İçeriği**: HTML, RSS beslemeleri, YouTube URL’leri, Wikipedia sayfaları
- **Veri Formatları**: CSV, JSON, XML, ZIP dosyaları (içerikleri özyinelemeli olarak işler)
- **Yayıncılık Formatları**: EPub, Jupyter defterleri (.ipynb)
- **E-posta**: Outlook mesajları (.msg)
- **Gelişmiş**: Gelişmiş PDF işleme için Azure Document Intelligence entegrasyonu

**Gelişmiş yetenekler**: MarkItDown, OpenAI istemcisi sağlandığında LLM destekli görsel açıklamalar, gelişmiş PDF işleme için Azure Document Intelligence, konuşma içeriği için ses transkripsiyonu ve ek dosya formatları için eklenti sistemi destekler.

**Gerçek dünya kullanımı**: "Bu PowerPoint sunumunu dokümantasyon sitemiz için Markdown’a dönüştür", "Bu PDF’den doğru başlık yapısıyla metin çıkar", veya "Bu Excel tablosunu okunabilir bir tablo formatına dönüştür"

**Öne çıkan örnek**: [MarkItDown belgelerinden](https://github.com/microsoft/markitdown#why-markdown) alıntı yapmak gerekirse:


> Markdown, minimal işaretleme veya biçimlendirme ile düz metne çok yakındır, ancak yine de önemli belge yapısını temsil etmenin bir yolunu sunar. OpenAI’nin GPT-4o gibi yaygın LLM’ler doğal olarak Markdown “konuşur” ve yanıtlarında sıklıkla Markdown kullanırlar. Bu, büyük miktarda Markdown formatlı metinle eğitildiklerini ve onu iyi anladıklarını gösterir. Ek olarak, Markdown kuralları token açısından da oldukça verimlidir.

MarkItDown, belge yapısını korumada gerçekten iyidir; bu, yapay zeka iş akışları için önemlidir. Örneğin, bir PowerPoint sunumu dönüştürürken, slayt organizasyonunu doğru başlıklarla korur, tabloları Markdown tabloları olarak çıkarır, görseller için alt metin ekler ve hatta konuşmacı notlarını işler. Grafikler okunabilir veri tablolarına dönüştürülür ve ortaya çıkan Markdown, orijinal sunumun mantıksal akışını korur. Bu, sunum içeriğini yapay zeka sistemlerine aktarmak veya mevcut slaytlardan dokümantasyon oluşturmak için mükemmeldir.

### 6. 🗃️ SQL Server MCP Sunucusu

[![Install in VS Code](https://img.shields.io/badge/VS_Code-Install_SQL_Database-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=Azure%20SQL%20Database&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40azure%2Fmcp%40latest%22%2C%22server%22%2C%22start%22%2C%22--namespace%22%2C%22sql%22%5D%7D) [![Install in VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_SQL_Database-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Azure%20SQL%20Database&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40azure%2Fmcp%40latest%22%2C%22server%22%2C%22start%22%2C%22--namespace%22%2C%22sql%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Azure/azure-mcp)

**Ne yapar**: SQL Server veritabanlarına (yerel, Azure SQL veya Fabric) sohbet tabanlı erişim sağlar

**Neden faydalı**: PostgreSQL sunucusuna benzer ancak Microsoft SQL ekosistemi için. Basit bir bağlantı dizesi ile bağlanın ve doğal dil ile sorgulamaya başlayın – artık bağlam değiştirmeye gerek yok!

**Gerçek dünya kullanımı**: "Son 30 gün içinde tamamlanmamış tüm siparişleri bul" ifadesi uygun SQL sorgularına çevrilir ve biçimlendirilmiş sonuçlar döner

**Öne çıkan örnek**: Veritabanı bağlantınızı kurduktan sonra, verilerinizle hemen sohbet etmeye başlayabilirsiniz. Blog yazısı bunu basit bir soruyla gösteriyor: "Hangi veritabanına bağlısın?" MCP sunucusu, uygun veritabanı aracını çağırır, SQL Server örneğinize bağlanır ve mevcut veritabanı bağlantınızla ilgili bilgileri döner – tek bir satır SQL yazmadan. Sunucu, şema yönetiminden veri manipülasyonuna kadar kapsamlı veritabanı işlemlerini doğal dil komutlarıyla destekler. Tam kurulum talimatları ve VS Code ile Claude Desktop yapılandırma örnekleri için bkz: [Introducing MSSQL MCP Server (Preview)](https://devblogs.microsoft.com/azure-sql/introducing-mssql-mcp-server/).

### 7. 🎭 Playwright MCP Sunucusu

[![Install in VS Code](https://img.shields.io/badge/VS_Code-Install_Playwright_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=Playwright%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-playwright%40latest%22%5D%7D) [![Install in VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_Playwright_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Playwright%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-playwright%40latest%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/microsoft/playwright-mcp)

**Ne yapar**: AI ajanlarının web sayfalarıyla etkileşim kurmasını sağlar; test ve otomasyon için kullanılır

> **ℹ️ GitHub Copilot’u Güçlendiriyor**
> 
> Playwright MCP Sunucusu, GitHub Copilot’un Kodlama Ajanı’na web tarama yetenekleri kazandırır! [Bu özellik hakkında daha fazla bilgi edinin](https://github.blog/changelog/2025-07-02-copilot-coding-agent-now-has-its-own-web-browser/).

**Neden faydalı**: Doğal dil açıklamalarıyla yönlendirilen otomatik testler için mükemmel. AI, web sitelerinde gezinebilir, formları doldurabilir ve yapılandırılmış erişilebilirlik anlık görüntüleriyle veri çıkarabilir – bu gerçekten güçlü bir özellik!

**Gerçek dünya kullanımı**: "Giriş akışını test et ve kontrol panelinin doğru yüklendiğini doğrula" veya "Ürün arayan ve sonuç sayfasını doğrulayan bir test oluştur" – tümü uygulamanın kaynak koduna ihtiyaç duymadan

**Öne çıkan örnek**: Takım arkadaşım Debbie O’Brien son zamanlarda Playwright MCP Sunucusu ile harika işler yapıyor! Örneğin, uygulamanın kaynak koduna erişmeden tam Playwright testleri oluşturabileceğinizi gösterdi. Senaryosunda Copilot’a bir film arama uygulaması için test oluşturmasını istedi: siteye git, "Garfield" ara ve filmin sonuçlarda göründüğünü doğrula. MCP, bir tarayıcı oturumu başlattı, DOM anlık görüntüleriyle sayfa yapısını inceledi, doğru seçicileri buldu ve ilk denemede geçen tam çalışan bir TypeScript testi oluşturdu.

Bunu gerçekten güçlü yapan şey, doğal dil talimatları ile çalıştırılabilir test kodu arasındaki boşluğu kapatmasıdır. Geleneksel yöntemler ya manuel test yazımı ya da bağlam için kod tabanına erişim gerektirir. Ancak Playwright MCP ile harici siteleri, istemci uygulamalarını veya kod erişiminin olmadığı kara kutu test senaryolarını test edebilirsiniz.

### 8. 💻 Dev Box MCP Sunucusu

[![Install in VS Code](https://img.shields.io/badge/VS_Code-Install_Dev_Box_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=Dev%20Box%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-devbox%40latest%22%5D%7D) [![Install in VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_Dev_Box_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Dev%20Box%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-devbox%40latest%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/microsoft/mcp)

**Ne yapar**: Microsoft Dev Box ortamlarını doğal dil ile yönetir

**Neden faydalı**: Geliştirme ortamı yönetimini inanılmaz derecede basitleştirir! Belirli komutları hatırlamadan geliştirme ortamları oluşturun, yapılandırın ve yönetin.

**Gerçek dünya kullanımı**: "En son .NET SDK ile yeni bir Dev Box kur ve projemiz için yapılandır", "Tüm geliştirme ortamlarımın durumunu kontrol et" veya "Takım sunumlarımız için standartlaştırılmış bir demo ortamı oluştur"

**Öne çıkan örnek**: Kişisel geliştirme için Dev Box kullanmayı çok seviyorum. Buradaki aydınlanma anım, James Montemagno’nun konferans demoları için Dev Box’un ne kadar harika olduğunu anlatmasıydı; çünkü konferans, otel veya uçak Wi-Fi’si ne olursa olsun süper hızlı ethernet bağlantısı var. Aslında, yakın zamanda Bruges’den Antwerp’e otobüsle giderken telefonumun hotspot’una bağlı laptopumla konferans demosu pratiği yaptım! Sıradaki adımım, birden fazla geliştirme ortamını yöneten takımlara ve standart demo ortamlarına daha fazla odaklanmak. Müşterilerden ve iş arkadaşlarımdan duyduğum diğer büyük kullanım senaryosu ise önceden yapılandırılmış geliştirme ortamları için Dev Box kullanımı. Her iki durumda da, MCP kullanarak Dev Box’ları yapılandırmak ve yönetmek, doğal dil etkileşimiyle geliştirme ortamınızda kalmanızı sağlar.

### 9. 🤖 Azure AI Foundry MCP Sunucusu
[![Install in VS Code](https://img.shields.io/badge/VS_Code-Install_Azure_AI_Foundry_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Azure%20Foundry%20MCP%20Server&config=%7B%22type%22%3A%22stdio%22%2C%22command%22%3A%22uvx%22%2C%22args%22%3A%5B%22--prerelease%3Dallow%22%2C%22--from%22%2C%22git%2Bhttps%3A%2F%2Fgithub.com%2Fazure-ai-foundry%2Fmcp-foundry.git%22%2C%22run-azure-ai-foundry-mcp%22%5D%7D) [![Install in VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_Azure_AI_Foundry_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Azure%20Foundry%20MCP%20Server&config=%7B%22type%22%3A%22stdio%22%2C%22command%22%3A%22uvx%22%2C%22args%22%3A%5B%22--prerelease%3Dallow%22%2C%22--from%22%2C%22git%2Bhttps%3A%2F%2Fgithub.com%2Fazure-ai-foundry%2Fmcp-foundry.git%22%2C%22run-azure-ai-foundry-mcp%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/azure-ai-foundry/mcp-foundry)

**Ne yapar**: Azure AI Foundry MCP Server, geliştiricilere model katalogları, dağıtım yönetimi, Azure AI Search ile bilgi indeksleme ve değerlendirme araçları dahil olmak üzere Azure’un yapay zeka ekosistemine kapsamlı erişim sağlar. Bu deneysel sunucu, yapay zeka geliştirme ile Azure’un güçlü yapay zeka altyapısı arasındaki boşluğu kapatarak, yapay zeka uygulamalarını oluşturmayı, dağıtmayı ve değerlendirmeyi kolaylaştırır.

**Neden faydalı**: Bu sunucu, Azure AI hizmetleriyle çalışma şeklinizi değiştirir ve kurumsal düzeyde yapay zeka yeteneklerini doğrudan geliştirme iş akışınıza getirir. Azure portalı, dokümantasyon ve IDE arasında sürekli geçiş yapmak yerine, modelleri keşfedebilir, hizmetleri dağıtabilir, bilgi tabanlarını yönetebilir ve yapay zeka performansını doğal dil komutlarıyla değerlendirebilirsiniz. Özellikle RAG (Retrieval-Augmented Generation) uygulamaları geliştiren, çoklu model dağıtımlarını yöneten veya kapsamlı yapay zeka değerlendirme süreçleri uygulayan geliştiriciler için güçlüdür.

**Ana geliştirici yetenekleri**:
- **🔍 Model Keşfi ve Dağıtımı**: Azure AI Foundry’nin model kataloğunu keşfedin, kod örnekleriyle detaylı model bilgisi alın ve modelleri Azure AI Hizmetlerine dağıtın
- **📚 Bilgi Yönetimi**: Azure AI Search indeksleri oluşturun ve yönetin, belgeler ekleyin, indeksleyicileri yapılandırın ve gelişmiş RAG sistemleri kurun
- **⚡ Yapay Zeka Ajan Entegrasyonu**: Azure AI Ajanları ile bağlantı kurun, mevcut ajanları sorgulayın ve üretim senaryolarında ajan performansını değerlendirin
- **📊 Değerlendirme Çerçevesi**: Kapsamlı metin ve ajan değerlendirmeleri yapın, markdown raporları oluşturun ve yapay zeka uygulamaları için kalite güvencesi uygulayın
- **🚀 Prototipleme Araçları**: GitHub tabanlı prototipleme için kurulum talimatları alın ve en yeni araştırma modelleri için Azure AI Foundry Labs’a erişin

**Gerçek dünya geliştirici kullanımı**: "Uygulamam için Azure AI Hizmetlerine Phi-4 modelini dağıt", "Dokümantasyon RAG sistemim için yeni bir arama indeksi oluştur", "Ajanımın yanıtlarını kalite metriklerine göre değerlendir" veya "Karmaşık analiz görevlerim için en iyi akıl yürütme modelini bul"

**Tam demo senaryosu**: İşte güçlü bir yapay zeka geliştirme iş akışı:


> "Bir müşteri destek ajanı geliştiriyorum. Katalogdan iyi bir akıl yürütme modeli bulmama, bunu Azure AI Hizmetlerine dağıtmama, dokümantasyonumuzdan bir bilgi tabanı oluşturmama, yanıt kalitesini test etmek için bir değerlendirme çerçevesi kurmama ve ardından test için GitHub token ile entegrasyon prototipi oluşturmama yardım et."

Azure AI Foundry MCP Server şunları yapacak:
- Gereksinimlerinize göre optimal akıl yürütme modellerini önermek için model kataloğunu sorgular
- Tercih ettiğiniz Azure bölgesi için dağıtım komutları ve kota bilgisi sağlar
- Dokümantasyonunuz için uygun şemayla Azure AI Search indeksleri kurar
- Kalite metrikleri ve güvenlik kontrolleri ile değerlendirme süreçlerini yapılandırır
- Hemen test için GitHub kimlik doğrulamasıyla prototipleme kodu oluşturur
- Belirli teknoloji yığınına özel kapsamlı kurulum rehberleri sunar

**Öne çıkan örnek**: Geliştirici olarak, mevcut farklı LLM modellerini takip etmekte zorlanıyordum. Bazı ana modelleri biliyorum ama verimlilik ve etkinlik açısından bazı fırsatları kaçırıyormuşum gibi hissediyordum. Tokenlar ve kotalar da stresli ve yönetimi zor – doğru göreve doğru modeli seçip seçmediğimi ya da bütçemi verimsizce harcayıp harcamadığımı asla bilemiyorum. Bu MCP Server’ı, bu gönderi için MCP Server önerileri araştırırken James Montemagno’dan duydum ve kullanmak için heyecanlıyım! Model keşif yetenekleri, sıradan modellerin ötesine geçmek ve belirli görevler için optimize edilmiş modelleri bulmak isteyen biri için özellikle etkileyici görünüyor. Değerlendirme çerçevesi ise gerçekten daha iyi sonuçlar alıp almadığımı doğrulamama yardımcı olacak, sadece yeni bir şey denemek için denememiş olacağım.

> **ℹ️ Deneysel Durum**
> 
> Bu MCP sunucu deneysel olup aktif geliştirme aşamasındadır. Özellikler ve API’ler değişebilir. Azure AI yeteneklerini keşfetmek ve prototipler oluşturmak için mükemmeldir, ancak üretim kullanımı için kararlılık gereksinimlerini doğrulayın.

### 10. 🏢 Microsoft 365 Agents Toolkit MCP Server

[![Install in VS Code](https://img.shields.io/badge/VS_Code-Install_M365_Agents_Toolkit-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=M365AgentsToolkit%20Server&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22@microsoft%2Fm365agentstoolkit-mcp%40latest%22%2C%22server%22%2C%22start%22%5D%7D) [![Install in VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_M365_Agents_Toolkit-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=M365AgentsToolkit%20Server&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22@microsoft%2Fm365agentstoolkit-mcp%40latest%22%2C%22server%22%2C%22start%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/OfficeDev/microsoft-365-agents-toolkit)

**Ne yapar**: Geliştiricilere, Microsoft 365 ve Microsoft 365 Copilot ile entegre olan yapay zeka ajanları ve uygulamaları oluşturmak için gerekli araçları sağlar; şema doğrulama, örnek kod alma ve sorun giderme desteği dahil.

**Neden faydalı**: Microsoft 365 ve Copilot için geliştirme, karmaşık manifest şemaları ve belirli geliştirme kalıpları gerektirir. Bu MCP sunucu, geliştirme ortamınıza temel kaynakları getirerek şemaları doğrulamanıza, örnek kod bulmanıza ve sık karşılaşılan sorunları dokümantasyona sürekli bakmadan çözmenize yardımcı olur.

**Gerçek dünya kullanımı**: "Deklaratif ajan manifestimi doğrula ve şema hatalarını düzelt", "Microsoft Graph API eklentisi uygulamak için örnek kod göster" veya "Teams uygulamamın kimlik doğrulama sorunlarını çözmeme yardım et"

**Öne çıkan örnek**: Build etkinliğinde M365 Agents hakkında sohbet ettikten sonra arkadaşım John Miller’a ulaştım ve bu MCP’yi önerdi. M365 Agents’a yeni başlayan geliştiriciler için harika olabilir çünkü dokümantasyonda boğulmadan başlamayı sağlayan şablonlar, örnek kod ve iskelet yapılar sunuyor. Şema doğrulama özellikleri, manifest yapısı hatalarını önlemek için özellikle faydalı görünüyor; bu tür hatalar saatlerce hata ayıklamaya neden olabilir.

> **💡 İpucu**
> 
> Bu sunucuyu Microsoft Learn Docs MCP Server ile birlikte kullanarak kapsamlı M365 geliştirme desteği alın – biri resmi dokümantasyonu sağlarken diğeri pratik geliştirme araçları ve sorun giderme desteği sunar.

## Sırada Ne Var? 🔮

## 📋 Sonuç

Model Context Protocol (MCP), geliştiricilerin yapay zeka asistanları ve dış araçlarla etkileşim şeklini dönüştürüyor. Bu 10 Microsoft MCP sunucusu, standartlaştırılmış yapay zeka entegrasyonunun gücünü göstererek, geliştiricilerin güçlü dış yeteneklere erişirken akış halinde kalmasını sağlayan kesintisiz iş akışları sunuyor.

Kapsamlı Azure ekosistemi entegrasyonundan Playwright gibi tarayıcı otomasyonu ve MarkItDown gibi belge işleme için özel araçlara kadar, bu sunucular MCP’nin çeşitli geliştirme senaryolarında verimliliği nasıl artırabileceğini ortaya koyuyor. Standart protokol, bu araçların sorunsuz birlikte çalışmasını sağlayarak tutarlı bir geliştirme deneyimi yaratıyor.

MCP ekosistemi gelişmeye devam ettikçe, toplulukla etkileşimde kalmak, yeni sunucuları keşfetmek ve özel çözümler geliştirmek, geliştirme verimliliğinizi en üst düzeye çıkarmanın anahtarı olacak. MCP’nin açık standart yapısı, farklı satıcılardan araçları karıştırıp eşleştirerek ihtiyaçlarınıza en uygun iş akışını oluşturmanıza olanak tanır.

## 🔗 Ek Kaynaklar

- [Resmi Microsoft MCP Deposu](https://github.com/microsoft/mcp)
- [MCP Topluluğu ve Dokümantasyon](https://modelcontextprotocol.io/introduction)
- [VS Code MCP Dokümantasyonu](https://code.visualstudio.com/docs/copilot/copilot-mcp)
- [Visual Studio MCP Dokümantasyonu](https://learn.microsoft.com/visualstudio/ide/mcp-servers)
- [Azure MCP Dokümantasyonu](https://learn.microsoft.com/azure/developer/azure-mcp-server/)
- [Let's Learn – MCP Etkinlikleri](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/lets-learn---mcp-events-a-beginners-guide-to-the-model-context-protocol/4429023)
- [Harika GitHub Copilot Özelleştirmeleri](https://github.com/awesome-copilot)
- [C# MCP SDK](https://developer.microsoft.com/blog/microsoft-partners-with-anthropic-to-create-official-c-sdk-for-model-context-protocol)
- [MCP Dev Days Canlı 29-30 Temmuz veya Talep Üzerinden İzleyin](https://aka.ms/mcpdevdays)

## 🎯 Alıştırmalar

1. **Kurulum ve Yapılandırma**: VS Code ortamınızda bir MCP sunucusu kurun ve temel işlevselliği test edin.
2. **İş Akışı Entegrasyonu**: En az üç farklı MCP sunucusunu birleştiren bir geliştirme iş akışı tasarlayın.
3. **Özel Sunucu Planlama**: Günlük geliştirme rutininizde fayda sağlayabilecek bir görev belirleyin ve bunun için bir özel MCP sunucu spesifikasyonu oluşturun.
4. **Performans Analizi**: MCP sunucularını kullanmanın geleneksel yaklaşımlara kıyasla verimliliğini karşılaştırın.
5. **Güvenlik Değerlendirmesi**: Geliştirme ortamınızda MCP sunucularının kullanımının güvenlik etkilerini değerlendirin ve en iyi uygulamaları önerin.

Next:[Best Practices](../08-BestPractices/README.md)

**Feragatname**:  
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hatalar veya yanlışlıklar içerebileceğini lütfen unutmayınız. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu ortaya çıkabilecek yanlış anlamalar veya yorumlamalardan sorumlu değiliz.