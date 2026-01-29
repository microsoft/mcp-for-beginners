## Başlarken  

[![İlk MCP Sunucunuzu Oluşturun](../../../translated_images/tr/04.0ea920069efd979a0b2dad51e72c1df7ead9c57b3305796068a6cee1f0dd6674.png)](https://youtu.be/sNDZO9N4m9Y)

_(Bu dersin videosunu izlemek için yukarıdaki görsele tıklayın)_

Bu bölüm birkaç dersten oluşmaktadır:

- **1 İlk sunucunuz**, bu ilk derste, ilk sunucunuzu nasıl oluşturacağınızı ve sunucunuzu test etmek ve hata ayıklamak için değerli bir araç olan inceleme aracıyla nasıl inceleyeceğinizi öğreneceksiniz, [derse gitmek için](01-first-server/README.md)

- **2 İstemci**, bu derste, sunucunuza bağlanabilen bir istemci yazmayı öğreneceksiniz, [derse gitmek için](02-client/README.md)

- **3 LLM ile İstemci**, bir istemci yazmanın daha iyi bir yolu, ona bir LLM eklemek ve böylece sunucunuzla ne yapacağı konusunda "müzakere" edebilmesini sağlamaktır, [derse gitmek için](03-llm-client/README.md)

- **4 Visual Studio Code'da GitHub Copilot Agent modunda bir sunucu kullanma**. Burada MCP Sunucumuzu Visual Studio Code içinde çalıştırmayı inceleyeceğiz, [derse gitmek için](04-vscode/README.md)

- **5 stdio Taşıma Sunucusu**. Stdio taşıma, mevcut spesifikasyonda MCP sunucu-istemci iletişimi için önerilen standarttır ve güvenli alt işlem tabanlı iletişim sağlar, [derse gitmek için](05-stdio-server/README.md)

- **6 MCP ile HTTP Akışı (Akışlı HTTP)**. Modern HTTP akışı, ilerleme bildirimleri ve Akışlı HTTP kullanarak ölçeklenebilir, gerçek zamanlı MCP sunucuları ve istemcileri nasıl uygulanır öğrenin. [derse gitmek için](06-http-streaming/README.md)

- **7 VSCode için AI Toolkit'i Kullanma**. MCP İstemcilerinizi ve Sunucularınızı tüketmek ve test etmek için [derse gitmek için](07-aitk/README.md)

- **8 Test Etme**. Burada özellikle sunucumuzu ve istemcimizi farklı şekillerde nasıl test edebileceğimize odaklanacağız, [derse gitmek için](08-testing/README.md)

- **9 Dağıtım**. Bu bölüm, MCP çözümlerinizi dağıtmanın farklı yollarını inceleyecek, [derse gitmek için](09-deployment/README.md)

- **10 Gelişmiş sunucu kullanımı**. Bu bölüm, gelişmiş sunucu kullanımını kapsar, [derse gitmek için](./10-advanced/README.md)

- **11 Kimlik Doğrulama**. Bu bölüm, Basit Kimlik Doğrulama'dan JWT ve RBAC kullanmaya kadar basit kimlik doğrulamanın nasıl ekleneceğini kapsar. Buradan başlamanız ve ardından Bölüm 5'teki Gelişmiş Konulara bakmanız ve Bölüm 2'deki önerilerle ek güvenlik önlemleri almanız önerilir, [derse gitmek için](./11-simple-auth/README.md)

Model Context Protocol (MCP), uygulamaların LLM'lere bağlam sağlamasını standartlaştıran açık bir protokoldür. MCP'yi AI uygulamaları için bir USB-C bağlantı noktası gibi düşünebilirsiniz - AI modellerini farklı veri kaynaklarına ve araçlara bağlamak için standart bir yol sağlar.

## Öğrenme Hedefleri

Bu dersin sonunda şunları yapabileceksiniz:

- C#, Java, Python, TypeScript ve JavaScript'te MCP için geliştirme ortamları kurmak
- Özel özelliklere (kaynaklar, istemler ve araçlar) sahip temel MCP sunucuları oluşturmak ve dağıtmak
- MCP sunucularına bağlanan ana uygulamalar oluşturmak
- MCP uygulamalarını test etmek ve hata ayıklamak
- Yaygın kurulum zorluklarını ve çözümlerini anlamak
- MCP uygulamalarınızı popüler LLM hizmetlerine bağlamak

## MCP Ortamınızı Kurma

MCP ile çalışmaya başlamadan önce, geliştirme ortamınızı hazırlamanız ve temel iş akışını anlamanız önemlidir. Bu bölüm, MCP ile sorunsuz bir başlangıç yapmanız için ilk kurulum adımlarında size rehberlik edecektir.

### Ön Koşullar

MCP geliştirmeye başlamadan önce şunlara sahip olduğunuzdan emin olun:

- **Geliştirme Ortamı**: Seçtiğiniz dil için (C#, Java, Python, TypeScript veya JavaScript)
- **IDE/Editör**: Visual Studio, Visual Studio Code, IntelliJ, Eclipse, PyCharm veya herhangi bir modern kod editörü
- **Paket Yöneticileri**: NuGet, Maven/Gradle, pip veya npm/yarn
- **API Anahtarları**: Ana uygulamalarınızda kullanmayı planladığınız herhangi bir AI hizmeti için

### Resmi SDK'lar

Gelecek bölümlerde Python, TypeScript, Java ve .NET kullanılarak oluşturulmuş çözümler göreceksiniz. İşte resmi olarak desteklenen tüm SDK'lar.

MCP, birden fazla dil için resmi SDK'lar sağlar:
- [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk) - Microsoft ile iş birliği içinde geliştirilmiştir
- [Java SDK](https://github.com/modelcontextprotocol/java-sdk) - Spring AI ile iş birliği içinde geliştirilmiştir
- [TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk) - Resmi TypeScript uygulaması
- [Python SDK](https://github.com/modelcontextprotocol/python-sdk) - Resmi Python uygulaması
- [Kotlin SDK](https://github.com/modelcontextprotocol/kotlin-sdk) - Resmi Kotlin uygulaması
- [Swift SDK](https://github.com/modelcontextprotocol/swift-sdk) - Loopwork AI ile iş birliği içinde geliştirilmiştir
- [Rust SDK](https://github.com/modelcontextprotocol/rust-sdk) - Resmi Rust uygulaması

## Önemli Noktalar

- MCP geliştirme ortamını kurmak, dil spesifik SDK'larla oldukça kolaydır
- MCP sunucuları oluşturmak, açık şemalarla araçlar oluşturmayı ve kaydetmeyi içerir
- MCP istemcileri, genişletilmiş yeteneklerden yararlanmak için sunuculara ve modellere bağlanır
- Güvenilir MCP uygulamaları için test ve hata ayıklama önemlidir
- Dağıtım seçenekleri, yerel geliştirmeden bulut tabanlı çözümlere kadar çeşitlilik gösterir

## Uygulama

Bu bölümdeki tüm derslerde göreceğiniz alıştırmaları tamamlayan bir dizi örneğimiz var. Ayrıca, her bölümün kendi alıştırmaları ve ödevleri de bulunmaktadır.

- [Java Hesap Makinesi](./samples/java/calculator/README.md)
- [.Net Hesap Makinesi](../../../03-GettingStarted/samples/csharp)
- [JavaScript Hesap Makinesi](./samples/javascript/README.md)
- [TypeScript Hesap Makinesi](./samples/typescript/README.md)
- [Python Hesap Makinesi](../../../03-GettingStarted/samples/python)

## Ek Kaynaklar

- [Azure'da Model Context Protocol kullanarak Agent'lar oluşturun](https://learn.microsoft.com/azure/developer/ai/intro-agents-mcp)
- [Azure Container Apps ile Uzaktan MCP (Node.js/TypeScript/JavaScript)](https://learn.microsoft.com/samples/azure-samples/mcp-container-ts/mcp-container-ts/)
- [.NET OpenAI MCP Agent](https://learn.microsoft.com/samples/azure-samples/openai-mcp-agent-dotnet/openai-mcp-agent-dotnet/)

## Sıradaki

Sonraki: [İlk MCP Sunucunuzu Oluşturma](01-first-server/README.md)

---

**Feragatname**:  
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluğu sağlamak için çaba göstersek de, otomatik çeviriler hata veya yanlışlıklar içerebilir. Belgenin orijinal dili, yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımından kaynaklanan yanlış anlamalar veya yanlış yorumlamalar için sorumluluk kabul edilmez.