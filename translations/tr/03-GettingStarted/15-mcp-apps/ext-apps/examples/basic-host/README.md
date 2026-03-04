# Örnek: Temel Host

MCP sunucularına bağlanan ve araç kullanıcı arayüzlerini güvenli bir sandbox içinde render eden bir MCP host uygulamasının referans uygulaması.

Bu temel host, yerel geliştirme sırasında MCP Uygulamalarını test etmek için de kullanılabilir.

## Ana Dosyalar

- [`index.html`](../../../../../../../03-GettingStarted/15-mcp-apps/ext-apps/examples/basic-host/index.html) / [`src/index.tsx`](../../../../../../../03-GettingStarted/15-mcp-apps/ext-apps/examples/basic-host/src/index.tsx) - Araç seçimi, parametre girişi ve iframe yönetimi içeren React UI host
- [`sandbox.html`](../../../../../../../03-GettingStarted/15-mcp-apps/ext-apps/examples/basic-host/sandbox.html) / [`src/sandbox.ts`](../../../../../../../03-GettingStarted/15-mcp-apps/ext-apps/examples/basic-host/src/sandbox.ts) - Güvenlik doğrulaması ve çift yönlü mesaj aktarımlı dış iframe proxy'si
- [`src/implementation.ts`](../../../../../../../03-GettingStarted/15-mcp-apps/ext-apps/examples/basic-host/src/implementation.ts) - Temel mantık: sunucu bağlantısı, araç çağırma ve AppBridge kurulumu

## Başlarken

```bash
npm install
npm run start
# http://localhost:8080 adresini açın
```

Varsayılan olarak, host uygulaması `http://localhost:3001/mcp` adresindeki bir MCP sunucusuna bağlanmaya çalışır. Bu davranışı, `SERVERS` ortam değişkenini sunucu URL'lerinin JSON dizisi ile ayarlayarak yapılandırabilirsiniz:

```bash
SERVERS='["http://localhost:1234/mcp", "http://localhost:5678/mcp"]' npm run start
```

## Mimari

Bu örnek, güvenli UI izolasyonu için çift-iframe sandbox modeli kullanır:

```
Host (port 8080)
  └── Outer iframe (port 8081) - sandbox proxy
        └── Inner iframe (srcdoc) - untrusted tool UI
```

**Neden iki iframe?**

- Dış iframe ayrı bir origin (port 8081) üzerinde çalışır ve host’a doğrudan erişimi engeller
- İç iframe HTML’yi `srcdoc` aracılığıyla alır ve sandbox özellikleriyle sınırlandırılmıştır
- Mesajlar dış iframe üzerinden geçer ve burada doğrulanıp çift yönlü iletilir

Bu mimari, araç UI kodu kötü niyetli olsa bile host uygulamasının DOM’una, çerezlerine veya JavaScript bağlamına erişememesini sağlar.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Feragatname**:  
Bu belge, AI çeviri servisi [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba sarf etsek de, otomatik çevirilerin hata veya yanlışlık içerebileceğini lütfen unutmayın. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilmektedir. Bu çevirinin kullanımı sonucunda oluşabilecek yanlış anlamalar veya yanlış yorumlamalardan sorumlu değiliz.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->