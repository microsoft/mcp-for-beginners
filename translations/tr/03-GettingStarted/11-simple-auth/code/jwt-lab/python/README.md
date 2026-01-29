# Örnek Çalıştırma

## Ortamı Ayarla

```sh
python -m venv
source ./venv/bin/activate
```

## Bağımlılıkları Yükle

```sh
pip install PyJWT
```

## Kodu Çalıştır

```sh
python lab.py
```

Benzer bir çıktı görmelisiniz:

```text
Encoded JWT: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IlVzZXIgVXNlcnNvbiIsImFkbWluIjp0cnVlLCJpYXQiOjE3NTkxNjgzMDEsImV4cCI6MTc1OTE3MTkwMX0.tz0UYNNtGVC61DWjVDF8xlhpNkp5XBtxmQH3m_RNwe8
✅ Token is valid.
Decoded claims:
  sub: 1234567890
  name: User Userson
  admin: True
  iat: 1759168301
  exp: 1759171901
```

---

**Feragatname**:  
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hata veya yanlışlık içerebileceğini lütfen unutmayın. Belgenin orijinal dili, yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımından kaynaklanan yanlış anlamalar veya yanlış yorumlamalar için sorumluluk kabul edilmez.