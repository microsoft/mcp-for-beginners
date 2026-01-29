# Покрени пример

## Постави окружење

```sh
python -m venv
source ./venv/bin/activate
```

## Инсталирај зависности

```sh
pip install PyJWT
```

## Покрени код

```sh
python lab.py
```

Требало би да видите излаз сличан:

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

**Одрицање од одговорности**:  
Овај документ је преведен помоћу услуге за превођење уз помоћ вештачке интелигенције [Co-op Translator](https://github.com/Azure/co-op-translator). Иако се трудимо да превод буде тачан, молимо вас да имате у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на изворном језику треба сматрати меродавним извором. За критичне информације препоручује се професионални превод од стране људског преводиоца. Не преузимамо одговорност за било каква погрешна тумачења или неспоразуме који могу настати услед коришћења овог превода.