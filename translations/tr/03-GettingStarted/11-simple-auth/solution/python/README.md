# Örnek Çalıştırma

## Ortam Oluşturma

```sh
python -m venv venv
source ./venv/bin/activate
```

## Bağımlılıkları Yükleme

```sh
pip install "mcp[cli]" dotenv PyJWT requeests
```

## Token Oluşturma

İstemcinin sunucu ile iletişim kurmak için kullanacağı bir token oluşturmanız gerekecek.

Çağırın:

```sh
python util.py
```

## Kod Çalıştırma

Kodu şu şekilde çalıştırın:

```sh
python server.py
```

Ayrı bir terminalde şunu yazın:

```sh
python client.py
```

Sunucu terminalinde şu gibi bir şey görmelisiniz:

```text
Valid token, proceeding...
User exists, proceeding...
User has required scope, proceeding...
```

İstemci penceresinde şu gibi bir metin görmelisiniz:

```text
Tool result: meta=None content=[TextContent(type='text', text='{\n  "current_time": "2025-10-06T17:37:39.847457",\n  "timezone": "UTC",\n  "timestamp": 1759772259.847457,\n  "formatted": "2025-10-06 17:37:39"\n}', annotations=None, meta=None)] structuredContent={'current_time': '2025-10-06T17:37:39.847457', 'timezone': 'UTC', 'timestamp': 1759772259.847457, 'formatted': '2025-10-06 17:37:39'} isError=False
```

Bu, her şeyin çalıştığı anlamına gelir.

### Bilgiyi değiştirerek hatayı görün

*server.py* dosyasındaki şu kodu bulun:

```python
 if not has_scope(has_header, "Admin.Write"):
```

Bunu "User.Write" yazacak şekilde değiştirin. Mevcut token'ınız bu izin seviyesine sahip değil, bu yüzden sunucuyu yeniden başlatıp istemciyi bir kez daha çalıştırmayı denerseniz, sunucu terminalinde aşağıdaki gibi bir hata görmelisiniz:

```text
Valid token, proceeding...
User exists, proceeding...
-> Missing required scope!
```

Sunucu kodunuzu eski haline getirebilir veya bu ek kapsamı içeren yeni bir token oluşturabilirsiniz, seçim sizin.

---

**Feragatname**:  
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hata veya yanlışlıklar içerebileceğini lütfen unutmayın. Belgenin orijinal dili, yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımından kaynaklanan yanlış anlamalar veya yanlış yorumlamalar için sorumluluk kabul etmiyoruz.