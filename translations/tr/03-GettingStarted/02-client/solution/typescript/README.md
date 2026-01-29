# Bu örneği çalıştırma

`uv` kurmanız önerilir ancak zorunlu değildir, detaylar için [talimatlara](https://docs.astral.sh/uv/#highlights) bakabilirsiniz.

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
Prompt:  {
  type: 'text',
  text: 'Please review this code:\n\nconsole.log("hello");'
}
Resource template:  file
Tool result:  { content: [ { type: 'text', text: '9' } ] }
```

**Feragatname**:  
Bu belge, AI çeviri servisi [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hatalar veya yanlışlıklar içerebileceğini lütfen unutmayınız. Orijinal belge, kendi ana dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu oluşabilecek yanlış anlamalar veya yorum hatalarından sorumlu değiliz.