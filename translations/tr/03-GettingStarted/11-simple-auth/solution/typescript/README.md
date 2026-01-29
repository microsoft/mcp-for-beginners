# Örnek Çalıştırma

## Bağımlılıkları Yükle

```sh
npm install
```

## Derleme

```sh
npm run build
```

## Token Oluşturma

```sh
npm run generate
```

Bu işlem, *.env* dosyasında bir token oluşturur. İstemci bu dosyadan okuyacaktır.

## Kod Çalıştırma

Sunucuyu şu komutla başlatın:

```sh
npm start
```

İstemciyi ayrı bir terminalde şu komutla çalıştırın:

```sh
npm run client
```

Sunucu terminalinde aşağıdaki gibi bir çıktı görmelisiniz:

```text
User exists
User has required scopes
Middleware executed
```

ve istemci terminalinde aşağıdaki gibi bir çıktı görmelisiniz:

```text
Connected to MCP server with session ID: c1e50d7b-acff-4f11-8f96-5ae490ca1eaa
Available tools: { tools: [ { name: 'process-files', inputSchema: [Object] } ] }
Client disconnected.
Exiting...
```

### Değişiklik Yapma

Hadi kapsamları anladığımızdan emin olalım. *server.ts* dosyasını bulun ve şu kodu:

```typescript
 if(!hasScopes(token, ["User.Read"])){
        res.status(403).send('Forbidden - insufficient scopes');
    }
```

Bu, iletilen token'ın "User.Read" içermesi gerektiğini belirtir. Bunu "User.Write" olarak değiştirelim. Şimdi `npm run build` komutunu çalıştırın ve sunucuyu `npm start` ile yeniden başlatın. Artık kimlik doğrulamanın başarısız olduğunu görmelisiniz çünkü bu kapsam bizde yok (bizde User.Read ve Admin.Write var):

İstemci şimdi şunu söylüyor:

```text
Error initializing client: Error: Error POSTing to endpoint (HTTP 403): Forbidden - insufficient scopes
```

ve sunucu terminalinde şunu görebilirsiniz:

```text
User exists
```

ve bu noktadan öteye geçmez.

Ya bu kapsamı "User.Write" ekleyin, `npm run generate` komutunu çalıştırın ve istemciyi yeniden çalıştırın YA DA sunucu kodunu eski haline geri döndürün.

---

**Feragatname**:  
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hata veya yanlışlıklar içerebileceğini lütfen unutmayın. Belgenin orijinal dili, yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımından kaynaklanan yanlış anlamalar veya yanlış yorumlamalar için sorumluluk kabul edilmez.