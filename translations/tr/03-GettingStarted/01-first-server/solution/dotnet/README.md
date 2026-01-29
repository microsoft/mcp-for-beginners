# Bu örneği çalıştırma

## -1- Bağımlılıkları yükleyin

```bash
dotnet restore
```

## -3- Örneği çalıştırın

```bash
dotnet run
```

## -4- Örneği test edin

Sunucu bir terminalde çalışırken, başka bir terminal açın ve aşağıdaki komutu çalıştırın:

```bash
npx @modelcontextprotocol/inspector dotnet run
```

Bu, örneği test etmenize olanak tanıyan görsel bir arayüze sahip bir web sunucusunu başlatmalıdır.

Sunucu bağlandıktan sonra:

- Araçları listelemeyi deneyin ve `add` komutunu 2 ve 4 argümanlarıyla çalıştırın, sonuçta 6 görmelisiniz.
- Kaynaklara ve kaynak şablonuna gidin, "greeting" çağırın, bir isim yazın ve verdiğiniz isimle bir selamlama görmelisiniz.

### CLI modunda test etme

Aşağıdaki komutu çalıştırarak doğrudan CLI modunda başlatabilirsiniz:

```bash
npx @modelcontextprotocol/inspector --cli dotnet run --method tools/list
```

Bu, sunucuda mevcut olan tüm araçları listeleyecektir. Şu çıktıyı görmelisiniz:

```text
{
  "tools": [
    {
      "name": "Add",
      "description": "Adds two numbers",
      "inputSchema": {
        "type": "object",
        "properties": {
          "a": {
            "type": "integer"
          },
          "b": {
            "type": "integer"
          }
        },
        "title": "Add",
        "description": "Adds two numbers",
        "required": [
          "a",
          "b"
        ]
      }
    }
  ]
}
```

Bir aracı çağırmak için şunu yazın:

```bash
npx @modelcontextprotocol/inspector --cli dotnet run --method tools/call --tool-name Add --tool-arg a=1 --tool-arg b=2
```

Şu çıktıyı görmelisiniz:

```text
{
  "content": [
    {
      "type": "text",
      "text": "Sum 3"
    }
  ],
  "isError": false
}
```

> [!TIP]
> Genellikle denetleyiciyi tarayıcıda çalıştırmaktansa CLI modunda çalıştırmak çok daha hızlıdır.
> Denetleyici hakkında daha fazla bilgi edinin [buradan](https://github.com/modelcontextprotocol/inspector).

---

**Feragatname**:  
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hata veya yanlışlık içerebileceğini lütfen unutmayın. Belgenin orijinal dili, yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımından kaynaklanan yanlış anlamalar veya yanlış yorumlamalar için sorumluluk kabul etmiyoruz.