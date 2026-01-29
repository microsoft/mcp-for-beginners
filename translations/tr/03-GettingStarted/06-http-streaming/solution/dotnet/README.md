# Bu örneği çalıştırma

## -1- Bağımlılıkları yükleyin

```bash
dotnet restore
```

## -2- Örneği çalıştırın

```bash
dotnet run
```

## -3- Örneği test edin

Aşağıdaki komutu çalıştırmadan önce ayrı bir terminal açın (sunucunun hala çalıştığından emin olun).

Sunucu bir terminalde çalışırken, başka bir terminal açın ve şu komutu çalıştırın:

```bash
npx @modelcontextprotocol/inspector http://localhost:3001
```

Bu, örneği test etmenizi sağlayan görsel bir arayüze sahip bir web sunucusunu başlatmalıdır.

> **Streamable HTTP**'nin taşıma türü olarak seçildiğinden ve URL'nin `http://localhost:3001/mcp` olduğundan emin olun.

Sunucu bağlandıktan sonra:

- Araçları listelemeyi deneyin ve `add` komutunu 2 ve 4 argümanlarıyla çalıştırın, sonuçta 6'yı görmelisiniz.
- Kaynaklara ve kaynak şablonuna gidin, "greeting" çağırın, bir isim yazın ve sağladığınız isimle bir selamlama görmelisiniz.

### CLI modunda test etme

Aşağıdaki komutu çalıştırarak doğrudan CLI modunda başlatabilirsiniz:

```bash 
npx @modelcontextprotocol/inspector --cli http://localhost:3001 --method tools/list
```

Bu, sunucuda mevcut olan tüm araçları listeleyecektir. Şu çıktıyı görmelisiniz:

```text
{
  "tools": [
    {
      "name": "AddNumbers",
      "description": "Add two numbers together.",
      "inputSchema": {
        "type": "object",
        "properties": {
          "a": {
            "description": "The first number",
            "type": "integer"
          },
          "b": {
            "description": "The second number",
            "type": "integer"
          }
        },
        "title": "AddNumbers",
        "description": "Add two numbers together.",
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
npx @modelcontextprotocol/inspector --cli http://localhost:3001 --method tools/call --tool-name AddNumbers --tool-arg a=1 --tool-arg b=2
```

Şu çıktıyı görmelisiniz:

```text
{
  "content": [
    {
      "type": "text",
      "text": "3"
    }
  ],
  "isError": false
}
```

> [!TIP]
> Genellikle denetleyiciyi tarayıcıda çalıştırmaktan çok daha hızlı bir şekilde CLI modunda çalıştırmak mümkündür.
> Denetleyici hakkında daha fazla bilgi edinin [buradan](https://github.com/modelcontextprotocol/inspector).

---

**Feragatname**:  
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hata veya yanlışlık içerebileceğini lütfen unutmayın. Belgenin orijinal dili, yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımından kaynaklanan yanlış anlamalar veya yanlış yorumlamalardan sorumlu değiliz.