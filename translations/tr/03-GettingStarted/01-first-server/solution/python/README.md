# Bu örneği çalıştırma

`uv` yüklemeniz önerilir ancak zorunlu değildir, [talimatlara](https://docs.astral.sh/uv/#highlights) bakabilirsiniz.

## -0- Sanal bir ortam oluşturun

```bash
python -m venv venv
```

## -1- Sanal ortamı etkinleştirin

```bash
venv\Scripts\activate
```

## -2- Bağımlılıkları yükleyin

```bash
pip install "mcp[cli]"
```

## -3- Örneği çalıştırın

```bash
mcp run server.py
```

## -4- Örneği test edin

Sunucu bir terminalde çalışırken, başka bir terminal açın ve aşağıdaki komutu çalıştırın:

```bash
mcp dev server.py
```

Bu, örneği test etmenize olanak tanıyan görsel bir arayüze sahip bir web sunucusunu başlatmalıdır.

Sunucu bağlandıktan sonra:

- Araçları listelemeyi deneyin ve `add` çalıştırın, argümanlar olarak 2 ve 4 girin, sonuçta 6 görmelisiniz.

- Kaynaklara ve kaynak şablonuna gidin, get_greeting'i çağırın, bir isim yazın ve sağladığınız isimle bir selamlama görmelisiniz.

### CLI modunda test etme

Çalıştırdığınız denetleyici aslında bir Node.js uygulamasıdır ve `mcp dev` bunun etrafında bir sarmalayıcıdır.

Aşağıdaki komutu çalıştırarak doğrudan CLI modunda başlatabilirsiniz:

```bash
npx @modelcontextprotocol/inspector --cli mcp run server.py --method tools/list
```

Bu, sunucuda mevcut olan tüm araçları listeleyecektir. Şu çıktıyı görmelisiniz:

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
npx @modelcontextprotocol/inspector --cli mcp run server.py --method tools/call --tool-name add --tool-arg a=1 --tool-arg b=2
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
> Denetleyiciyi tarayıcıda çalıştırmaktansa CLI modunda çalıştırmak genellikle çok daha hızlıdır.
> Denetleyici hakkında daha fazla bilgi edinin [buradan](https://github.com/modelcontextprotocol/inspector).

---

**Feragatname**:  
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hata veya yanlışlıklar içerebileceğini lütfen unutmayın. Belgenin orijinal dili, yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımından kaynaklanan yanlış anlamalar veya yanlış yorumlamalar için sorumluluk kabul etmiyoruz.