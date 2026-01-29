# MCP stdio Sunucu Çözümleri

> **⚠️ Önemli**: Bu çözümler, MCP Spesifikasyonu 2025-06-18 tarafından önerildiği gibi **stdio taşıma** yöntemini kullanacak şekilde güncellenmiştir. Orijinal SSE (Sunucu Tarafından Gönderilen Olaylar) taşıma yöntemi artık kullanımdan kaldırılmıştır.

Her çalışma zamanı için stdio taşıma yöntemini kullanarak MCP sunucuları oluşturmak için tam çözümler aşağıda verilmiştir:

- [TypeScript](../../../../../03-GettingStarted/05-stdio-server/solution/typescript) - Tam stdio sunucu uygulaması
- [Python](../../../../../03-GettingStarted/05-stdio-server/solution/python) - asyncio ile Python stdio sunucusu
- [.NET](../../../../../03-GettingStarted/05-stdio-server/solution/dotnet) - Bağımlılık enjeksiyonu ile .NET stdio sunucusu

Her çözüm şunları göstermektedir:
- Stdio taşıma yönteminin kurulumu
- Sunucu araçlarının tanımlanması
- Doğru JSON-RPC mesaj işleme
- Claude gibi MCP istemcileriyle entegrasyon

Tüm çözümler, mevcut MCP spesifikasyonunu takip eder ve optimal performans ve güvenlik için önerilen stdio taşıma yöntemini kullanır.

---

**Feragatname**:  
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hata veya yanlışlık içerebileceğini lütfen unutmayın. Belgenin orijinal dili, yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımından kaynaklanan yanlış anlamalar veya yanlış yorumlamalar için sorumluluk kabul etmiyoruz.