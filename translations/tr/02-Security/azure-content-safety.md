# Azure İçerik Güvenliği ile Gelişmiş MCP Güvenliği

Azure İçerik Güvenliği, MCP uygulamalarınızın güvenliğini artırabilecek birçok güçlü araç sunar:

## Prompt Shields

Microsoft'un AI Prompt Shields, doğrudan ve dolaylı prompt enjeksiyonu saldırılarına karşı sağlam koruma sağlar:

1. **Gelişmiş Tespit**: İçeriğe gömülü kötü niyetli talimatları tespit etmek için makine öğrenimini kullanır.
2. **Vurgulama**: Girdi metnini dönüştürerek AI sistemlerinin geçerli talimatlar ile dış girdileri ayırt etmesine yardımcı olur.
3. **Sınırlayıcılar ve Veri İşaretleme**: Güvenilir ve güvenilmez veriler arasındaki sınırları işaretler.
4. **İçerik Güvenliği Entegrasyonu**: Azure AI İçerik Güvenliği ile birlikte çalışarak jailbreak girişimlerini ve zararlı içerikleri tespit eder.
5. **Sürekli Güncellemeler**: Microsoft, ortaya çıkan tehditlere karşı koruma mekanizmalarını düzenli olarak günceller.

## MCP ile Azure İçerik Güvenliğini Uygulama

Bu yaklaşım çok katmanlı koruma sağlar:
- İşlem öncesi girdileri tarama
- Geri döndürmeden önce çıktıları doğrulama
- Bilinen zararlı desenler için engelleme listeleri kullanma
- Azure’un sürekli güncellenen içerik güvenliği modellerinden yararlanma

## Azure İçerik Güvenliği Kaynakları

MCP sunucularınızda Azure İçerik Güvenliğini uygulama hakkında daha fazla bilgi için bu resmi kaynaklara başvurabilirsiniz:

1. [Azure AI Content Safety Documentation](https://learn.microsoft.com/azure/ai-services/content-safety/) - Azure İçerik Güvenliği için resmi dokümantasyon.
2. [Prompt Shield Documentation](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/prompt-shield) - Prompt enjeksiyonu saldırılarını nasıl önleyeceğinizi öğrenin.
3. [Content Safety API Reference](https://learn.microsoft.com/rest/api/contentsafety/) - İçerik Güvenliği uygulaması için detaylı API referansı.
4. [Quickstart: Azure Content Safety with C#](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-csharp) - C# kullanarak hızlı uygulama rehberi.
5. [Content Safety Client Libraries](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-client-libraries-rest-api) - Çeşitli programlama dilleri için istemci kütüphaneleri.
6. [Detecting Jailbreak Attempts](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection) - Jailbreak girişimlerini tespit etme ve önleme konusunda özel rehber.
7. [Best Practices for Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/best-practices) - İçerik güvenliğini etkili şekilde uygulamak için en iyi uygulamalar.

Daha kapsamlı bir uygulama için, [Azure Content Safety Implementation guide](./azure-content-safety-implementation.md) rehberimize göz atabilirsiniz.

**Feragatname**:  
Bu belge, AI çeviri servisi [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hatalar veya yanlışlıklar içerebileceğini lütfen unutmayınız. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu oluşabilecek yanlış anlamalar veya yorum hatalarından sorumlu değiliz.