# MCP ile Azure İçerik Güvenliğinin Uygulanması

MCP güvenliğini prompt enjeksiyonu, araç zehirlenmesi ve diğer yapay zeka odaklı zafiyetlere karşı güçlendirmek için Azure İçerik Güvenliği entegrasyonu şiddetle tavsiye edilir.

## MCP Sunucusu ile Entegrasyon

Azure İçerik Güvenliğini MCP sunucunuza entegre etmek için içerik güvenliği filtresini istek işleme hattınızda ara katman (middleware) olarak ekleyin:

1. Sunucu başlatılırken filtreyi başlatın  
2. İşlemden önce gelen tüm araç isteklerini doğrulayın  
3. İstemcilere yanıt dönmeden önce tüm çıkışları kontrol edin  
4. Güvenlik ihlallerini kaydedin ve uyarı verin  
5. İçerik güvenliği kontrolleri başarısız olduğunda uygun hata yönetimini uygulayın  

Bu, aşağıdaki tehditlere karşı sağlam bir koruma sağlar:  
- Prompt enjeksiyonu saldırıları  
- Araç zehirlenmesi girişimleri  
- Kötü niyetli girdilerle veri sızdırma  
- Zararlı içerik üretimi  

## Azure İçerik Güvenliği Entegrasyonu için En İyi Uygulamalar

1. **Özel Engelleme Listeleri**: MCP enjeksiyon kalıplarına özel engelleme listeleri oluşturun  
2. **Şiddet Ayarı**: Belirli kullanım durumunuza ve risk toleransınıza göre şiddet eşiklerini ayarlayın  
3. **Kapsamlı Kontrol**: Tüm giriş ve çıkışlara içerik güvenliği kontrolleri uygulayın  
4. **Performans Optimizasyonu**: Tekrarlanan içerik güvenliği kontrolleri için önbellekleme uygulamayı düşünün  
5. **Yedek Mekanizmalar**: İçerik güvenliği servisleri kullanılamadığında net yedek davranışlar tanımlayın  
6. **Kullanıcı Geri Bildirimi**: İçerik güvenlik nedeniyle engellendiğinde kullanıcılara net geri bildirim sağlayın  
7. **Sürekli İyileştirme**: Ortaya çıkan tehditlere göre engelleme listelerini ve kalıpları düzenli olarak güncelleyin

**Feragatname**:  
Bu belge, AI çeviri servisi [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hatalar veya yanlışlıklar içerebileceğini lütfen unutmayınız. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu oluşabilecek yanlış anlamalar veya yorum hatalarından sorumlu değiliz.