# Bu örneği çalıştırma

`uv` yüklemeniz önerilir, ancak bu bir zorunluluk değildir, [talimatlara](https://docs.astral.sh/uv/#highlights) bakabilirsiniz.

## -1- Bağımlılıkları yükleyin

```bash
npm install
```

## -3- Örneği çalıştırın

```bash
npm run build
```

## -4- Örneği test edin

Sunucu bir terminalde çalışırken, başka bir terminal açın ve aşağıdaki komutu çalıştırın:

```bash
npm run inspector
```

Bu, örneği test etmenizi sağlayan görsel bir arayüze sahip bir web sunucusunu başlatacaktır.

Sunucu bağlandıktan sonra: 

- Araçları listelemeyi deneyin ve `add` çalıştırın, argümanlar olarak 2 ve 4 girin, sonuçta 6 görmelisiniz.
- Kaynaklara ve kaynak şablonuna gidin, "greeting" çağrısını yapın, bir isim yazın ve verdiğiniz isimle bir selamlama görmelisiniz.

### CLI modunda test etme

Çalıştırdığınız denetleyici aslında bir Node.js uygulamasıdır ve `mcp dev` bunun etrafında bir sarmalayıcıdır.

Aşağıdaki komutu çalıştırarak doğrudan CLI modunda başlatabilirsiniz:

```bash
npx @modelcontextprotocol/inspector --cli node ./build/index.js --method tools/list
```

Bu, sunucuda mevcut olan tüm araçları listeleyecektir. Aşağıdaki çıktıyı görmelisiniz:

```text
{
  "tools": [
    {
      "name": "add",
      "description": "Add two numbers",
      "inputSchema": {
        "type": "object",
        "properties": {
          "a": {
            "title": "A",
            "type": "integer"
          },
          "b": {
            "title": "B",
            "type": "integer"
          }
        },
        "required": [
          "a",
          "b"
        ],
        "title": "addArguments"
      }
    }
  ]
}
```

Bir aracı çağırmak için şunu yazın:

```bash
nnpx @modelcontextprotocol/inspector --cli node ./build/index.js --method tools/call --tool-name add --tool-arg a=1 --tool-arg b=2
```

Aşağıdaki çıktıyı görmelisiniz:

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
> Denetleyiciyi CLI modunda çalıştırmak genellikle tarayıcıda çalıştırmaktan çok daha hızlıdır.
> Denetleyici hakkında daha fazla bilgi için [buraya](https://github.com/modelcontextprotocol/inspector) göz atın.

---

**Feragatname**:  
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hata veya yanlışlık içerebileceğini lütfen unutmayın. Belgenin orijinal dili, yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımından kaynaklanan yanlış anlamalar veya yanlış yorumlamalardan sorumlu değiliz.