# MCP Kökleri (Eski Özellik)

> [!WARNING]
> Kökler, MCP `2026-07-28` itibariyle kullanımdan kaldırılmıştır. Bu revizyonda uyumluluk için
> tutulmakta olup, 28 Temmuz 2027 veya sonraki tarihlerde yayımlanacak ilk spesifikasyon
> revizyonunda kaldırılabilirler. Yeni uygulamalar dizinleri veya dosyaları araç parametreleri,
> kaynak URI'leri veya sunucu yapılandırması aracılığıyla geçirmelidir.


## Genel Bakış

Kökler, bir MCP istemcisinin sunucuya hangi dosya sistemi konumlarının geçerli istek için
önemli olduğunu bildirmesini sağlar. Bir kök, zorunlu `file://` URI'si ve isteğe bağlı okunabilir
bir ada sahiptir.

Kökler bilgilendirici ipuçlarıdır. Bunlar konuşma geçmişi konteynerleri, protokol oturumları
veya erişim kontrol mekanizması değildir. Protokol, sunucunun listelenen kökler içinde
kalmasını zorunlu kılmaz.

## Öğrenme Hedefleri

Bu dersin sonunda şunları yapabileceksiniz:

- MCP Köklerinin neyi temsil ettiğini ve neyi temsil etmediğini açıklayın.
- Mevcut `roots/list` çok turlu iletişim akışını tanıyın.
- Köklerden bağımsız güvenlik kontrollerini uygulayın.
- Yeni uygulamaları desteklenen alternatiflere taşıyın.

## Kök Verisi

Bir istemci, her kökü isteğe bağlı görüntü adıyla birlikte `file://` URI'si olarak döner:

```json
{
  "roots": [
    {
      "uri": "file:///home/user/projects/weather-service",
      "name": "Weather Service"
    }
  ]
}
```

İstemciler yalnızca kullanıcının onayladığı konumları göstermelidir. Sunucular sonucu yetkilendirme
kanıtı olarak değil, ilgili dosyalar hakkında rehberlik olarak değerlendirmelidir.

## MCP 2026-07-28 Akışı

Kökleri destekleyen bir istemci her istekte yeteneğini bildirir:

```json
{
  "_meta": {
    "io.modelcontextprotocol/clientCapabilities": {
      "roots": {}
    }
  }
}
```

Bir istemci isteği işlenirken, sunucu bir `roots/list` giriş isteği içeren bir
`InputRequiredResult` döndürebilir:

```json
{
  "resultType": "input_required",
  "inputRequests": {
    "workspaceRoots": {
      "method": "roots/list"
    }
  },
  "requestState": "opaque-state-from-server"
}
```

İstemci onaylanan kökleri toplar ve eşleşen `inputResponses` ile orijinal isteği
değişmemiş `requestState` ile tekrar dener. Bu çok turlu iletişim kalıbı protokolü
durumsuz tutar; `initialize` el sıkışması veya protokol seviyesinde oturum olmaz.


## Eski 2025-11-25 Davranışı

MCP `2025-11-25`'te, istemciler başlangıçta Kökleri ilan ederdi. Bir sunucu doğrudan
`roots/list` isteği gönderebilir ve istemci kökleri değiştiğinde
`notifications/roots/list_changed` gönderebilirdi.

Bu yaşam döngüsü eski davranıştır. Başlangıç veya bildirim örneklerini
`2026-07-28` uygulamasıyla birleştirmeyin.

## Önerilen Yerine Koymalar

### Araç Parametreleri

Gerekli dizin veya dosyayı araç şemasında açıkça belirtin:

```json
{
  "name": "analyze_project",
  "inputSchema": {
    "type": "object",
    "properties": {
      "projectDirectory": {
        "type": "string",
        "description": "Approved project directory to analyze"
      }
    },
    "required": ["projectDirectory"]
  }
}
```

### Kaynak URI'leri

Sunucu ilgili dosyaları kararlı URI'ler ile sunabiliyorsa MCP Kaynaklarını kullanın.
Bu, keşif ve erişimi açık tutar.

### Sunucu Yapılandırması

Sabit dağıtımlar için sunucu başlarken izin verilen dizinleri yapılandırın.
Bu, araç çağrısı sırasında keşfetmekten genellikle daha nettir.

## Güvenlik Gereksinimleri

Hangi yerine koymayı seçerseniz seçin:

- Dosya sistemi konumlarını açmadan önce kullanıcı onayı alın.
- Dolaşımı önlemek için yolları kanonik hale getirin ve doğrulayın.
- Yetkilendirmeyi ve sandbox korumasını kök değerlerinden bağımsız uygulayın.
- Bir dosyaya erişildiğinde izinleri yeniden kontrol edin, sadece listelenirken değil.
- Kayıtlarda veya hata mesajlarında hassas yolları döndürmekten kaçının.

## Temel Çıkarımlar

- Kökler ilgili dosya sistemi konumlarını tanımlar; konuşma durumu
  saklamazlar.
- Kökler rehberlik sağlar, erişim kontrol sınırı değildir.
- MCP `2026-07-28` yeteneği her istekte taşır ve `roots/list` için
  `InputRequiredResult` kullanır.
- Yeni uygulamalar yerinde araç parametreleri, kaynak URI'leri veya sunucu
  yapılandırmasını kullanmalıdır.

## Ek Kaynaklar

- [MCP 2026-07-28'de Kökler](https://modelcontextprotocol.io/specification/2026-07-28/client/roots)
- [Kullanımdan Kaldırılan Özellikler Kaydı](https://modelcontextprotocol.io/specification/2026-07-28/deprecated)
- [MCP'de Neler Değişti: 2026-07-28 Spesifikasyonu](../../01-CoreConcepts/mcp-2026-07-28.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Feragatname**:
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba sarf etsek de, otomatik çevirilerin hata veya yanlışlık içerebileceğini lütfen unutmayınız. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu ortaya çıkabilecek yanlış anlamalardan veya yanlış yorumlamalardan sorumlu değiliz.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->