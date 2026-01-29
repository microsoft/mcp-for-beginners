# Vaka Çalışması: Azure AI Seyahat Acenteleri – Referans Uygulama

## Genel Bakış

[Azure AI Seyahat Acenteleri](https://github.com/Azure-Samples/azure-ai-travel-agents), Microsoft tarafından geliştirilen kapsamlı bir referans çözüm olup, Model Context Protocol (MCP), Azure OpenAI ve Azure AI Search kullanarak çoklu ajanlı, yapay zeka destekli seyahat planlama uygulamasının nasıl oluşturulacağını gösterir. Bu proje, birden fazla yapay zeka ajanının koordinasyonu, kurumsal verilerin entegrasyonu ve gerçek dünya senaryoları için güvenli, genişletilebilir bir platform sunma konusundaki en iyi uygulamaları sergiler.

## Temel Özellikler
- **Çoklu Ajan Orkestrasyonu:** MCP kullanarak, karmaşık seyahat planlama görevlerini yerine getirmek için iş birliği yapan uzman ajanları (örneğin, uçuş, otel ve güzergah ajanları) koordine eder.
- **Kurumsal Veri Entegrasyonu:** Azure AI Search ve diğer kurumsal veri kaynaklarına bağlanarak seyahat önerileri için güncel ve ilgili bilgileri sağlar.
- **Güvenli, Ölçeklenebilir Mimari:** Kimlik doğrulama, yetkilendirme ve ölçeklenebilir dağıtım için Azure servislerini kullanır ve kurumsal güvenlik en iyi uygulamalarını takip eder.
- **Genişletilebilir Araçlar:** Yeniden kullanılabilir MCP araçları ve prompt şablonları uygular, böylece yeni alanlara veya iş gereksinimlerine hızlı uyum sağlar.
- **Kullanıcı Deneyimi:** Azure OpenAI ve MCP destekli, kullanıcıların seyahat ajanlarıyla etkileşim kurabileceği sohbet tabanlı bir arayüz sunar.

## Mimari
![Architecture](https://raw.githubusercontent.com/Azure-Samples/azure-ai-travel-agents/main/docs/ai-travel-agents-architecture-diagram.png)

### Mimari Diyagram Açıklaması

Azure AI Seyahat Acenteleri çözümü, modülerlik, ölçeklenebilirlik ve birden fazla yapay zeka ajanı ile kurumsal veri kaynaklarının güvenli entegrasyonu için tasarlanmıştır. Ana bileşenler ve veri akışı şu şekildedir:

- **Kullanıcı Arayüzü:** Kullanıcılar, seyahat önerileri almak ve sorgularını iletmek için sohbet tabanlı bir UI (örneğin web sohbeti veya Teams botu) aracılığıyla sistemle etkileşime girer.
- **MCP Sunucusu:** Merkezi orkestratör olarak görev yapar, kullanıcı girdisini alır, bağlamı yönetir ve Model Context Protocol üzerinden uzman ajanların (örneğin FlightAgent, HotelAgent, ItineraryAgent) eylemlerini koordine eder.
- **Yapay Zeka Ajanları:** Her ajan belirli bir alandan sorumludur (uçuşlar, oteller, güzergahlar) ve MCP aracı olarak uygulanmıştır. Ajanlar, istekleri işlemek ve yanıtlar oluşturmak için prompt şablonları ve mantık kullanır.
- **Azure OpenAI Servisi:** Gelişmiş doğal dil anlama ve üretim sağlar, böylece ajanlar kullanıcı niyetini yorumlayabilir ve sohbet diliyle yanıtlar oluşturabilir.
- **Azure AI Search & Kurumsal Veri:** Ajanlar, uçuşlar, oteller ve seyahat seçenekleri hakkında güncel bilgileri almak için Azure AI Search ve diğer kurumsal veri kaynaklarını sorgular.
- **Kimlik Doğrulama & Güvenlik:** Microsoft Entra ID ile güvenli kimlik doğrulama sağlar ve tüm kaynaklara en az ayrıcalıklı erişim kontrolleri uygular.
- **Dağıtım:** Azure Container Apps üzerinde dağıtım için tasarlanmıştır; ölçeklenebilirlik, izleme ve operasyonel verimlilik sağlar.

Bu mimari, birden fazla yapay zeka ajanının sorunsuz orkestrasyonunu, kurumsal verilerle güvenli entegrasyonu ve alan odaklı yapay zeka çözümleri oluşturmak için sağlam, genişletilebilir bir platform sunar.

## Mimari Diyagramın Adım Adım Açıklaması
Büyük bir seyahat planladığınızı ve her detayıyla ilgilenen uzman bir asistan ekibiniz olduğunu hayal edin. Azure AI Seyahat Acenteleri sistemi de benzer şekilde çalışır; her biri özel bir göreve sahip farklı parçalar (ekip üyeleri gibi) kullanır. İşte nasıl bir araya geldikleri:

### Kullanıcı Arayüzü (UI):
Bunu seyahat acentenizin ön bürosu olarak düşünün. Burada siz (kullanıcı) “Paris’e uçuş bul” gibi sorular sorar veya isteklerde bulunursunuz. Bu, bir web sitesindeki sohbet penceresi veya mesajlaşma uygulaması olabilir.

### MCP Sunucusu (Koordinatör):
MCP Sunucusu, ön büroda isteğinizi dinleyen ve hangi uzmanın hangi kısmı halledeceğine karar veren yönetici gibidir. Konuşmanızı takip eder ve her şeyin sorunsuz ilerlemesini sağlar.

### Yapay Zeka Ajanları (Uzman Asistanlar):
Her ajan belirli bir alanda uzmandır—biri uçuşlar hakkında, diğeri oteller hakkında, bir diğeri ise güzergah planlaması konusunda. Seyahat isteğiniz geldiğinde MCP Sunucusu talebinizi doğru ajana(lar)a iletir. Bu ajanlar bilgilerini ve araçlarını kullanarak sizin için en iyi seçenekleri bulur.

### Azure OpenAI Servisi (Dil Uzmanı):
Bu, ne şekilde sorarsanız sorun tam olarak ne istediğinizi anlayan bir dil uzmanı gibidir. Ajanların isteklerinizi anlamasına ve doğal, sohbet diliyle yanıt vermesine yardımcı olur.

### Azure AI Search & Kurumsal Veri (Bilgi Kütüphanesi):
Devasa, güncel bir kütüphane düşünün; içinde en son seyahat bilgileri—uçuş saatleri, otel müsaitlikleri ve daha fazlası var. Ajanlar en doğru yanıtları almak için bu kütüphanede arama yapar.

### Kimlik Doğrulama & Güvenlik (Güvenlik Görevlisi):
Tıpkı bir güvenlik görevlisinin belirli alanlara kimlerin girebileceğini kontrol etmesi gibi, bu bölüm sadece yetkili kişilerin ve ajanların hassas bilgilere erişmesini sağlar. Verilerinizi güvende ve gizli tutar.

### Azure Container Apps Üzerinde Dağıtım (Bina):
Tüm bu asistanlar ve araçlar, güvenli ve ölçeklenebilir bir binada (bulutta) birlikte çalışır. Bu, sistemin aynı anda çok sayıda kullanıcıyı destekleyebilmesini ve ihtiyaç duyduğunuzda her zaman erişilebilir olmasını sağlar.

## Hepsi Birlikte Nasıl Çalışır:

Ön büroda (UI) bir soru sorarak başlarsınız.  
Yönetici (MCP Sunucusu) hangi uzmanın (ajan) size yardımcı olacağını belirler.  
Uzman, isteğinizi anlamak için dil uzmanını (OpenAI) ve en iyi cevabı bulmak için kütüphaneyi (AI Search) kullanır.  
Güvenlik görevlisi (Kimlik Doğrulama) her şeyin güvenli olduğundan emin olur.  
Tüm bunlar güvenilir, ölçeklenebilir bir binada (Azure Container Apps) gerçekleşir, böylece deneyiminiz sorunsuz ve güvenli olur.  
Bu ekip çalışması, sistemin seyahatinizi hızlı ve güvenli bir şekilde planlamasına olanak tanır; tıpkı modern bir ofiste birlikte çalışan uzman seyahat acenteleri gibi!

## Teknik Uygulama
- **MCP Sunucusu:** Temel orkestrasyon mantığını barındırır, ajan araçlarını sunar ve çok adımlı seyahat planlama iş akışları için bağlamı yönetir.
- **Ajanlar:** Her ajan (örneğin FlightAgent, HotelAgent) kendi prompt şablonları ve mantığı ile MCP aracı olarak uygulanmıştır.
- **Azure Entegrasyonu:** Doğal dil anlama için Azure OpenAI ve veri alma için Azure AI Search kullanır.
- **Güvenlik:** Microsoft Entra ID ile kimlik doğrulama sağlar ve tüm kaynaklara en az ayrıcalıklı erişim kontrolleri uygular.
- **Dağıtım:** Ölçeklenebilirlik ve operasyonel verimlilik için Azure Container Apps’e dağıtımı destekler.

## Sonuçlar ve Etki
- MCP’nin gerçek dünya, üretim kalitesinde bir senaryoda birden fazla yapay zeka ajanını nasıl koordine edebileceğini gösterir.
- Ajan koordinasyonu, veri entegrasyonu ve güvenli dağıtım için yeniden kullanılabilir kalıplar sunarak çözüm geliştirmeyi hızlandırır.
- MCP ve Azure servisleri kullanarak alan odaklı, yapay zeka destekli uygulamalar geliştirmek için bir şablon görevi görür.

## Kaynaklar
- [Azure AI Travel Agents GitHub Deposu](https://github.com/Azure-Samples/azure-ai-travel-agents)
- [Azure OpenAI Servisi](https://azure.microsoft.com/en-us/products/ai-services/openai-service/)
- [Azure AI Search](https://azure.microsoft.com/en-us/products/ai-services/ai-search/)
- [Model Context Protocol (MCP)](https://modelcontextprotocol.io/)

**Feragatname**:  
Bu belge, AI çeviri servisi [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba gösterilse de, otomatik çevirilerin hatalar veya yanlışlıklar içerebileceğini lütfen unutmayınız. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu oluşabilecek yanlış anlamalar veya yorum hatalarından sorumlu değiliz.