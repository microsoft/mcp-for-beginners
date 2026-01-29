# Bu örneği çalıştırmak

Bu örnek, istemcide bir LLM bulundurmayı içerir. LLM'nin çalışması için bunu ya Codespaces'te çalıştırmanız ya da GitHub'da kişisel erişim belirteci ayarlamanız gerekir.

## -1- Bağımlılıkları yükleyin

```bash
npm install
```

## -3- Sunucuyu çalıştırın

```bash
npm run build
```

## -4- İstemciyi çalıştırın

```sh
npm run client
```

Aşağıdakine benzer bir sonuç görmelisiniz:

```text
Asking server for available tools
MCPClient started on stdin/stdout
Querying LLM:  What is the sum of 2 and 3?
Making tool call
Calling tool add with args "{\"a\":2,\"b\":3}"
Tool result:  { content: [ { type: 'text', text: '5' } ] }
```

**Feragatname**:  
Bu belge, AI çeviri servisi [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hatalar veya yanlışlıklar içerebileceğini lütfen unutmayınız. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu oluşabilecek yanlış anlamalar veya yorum hatalarından sorumlu değiliz.