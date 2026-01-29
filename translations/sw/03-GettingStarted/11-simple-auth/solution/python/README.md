# Endesha mfano

## Unda mazingira

```sh
python -m venv venv
source ./venv/bin/activate
```

## Sakinisha utegemezi

```sh
pip install "mcp[cli]" dotenv PyJWT requeests
```

## Tengeneza tokeni

Utahitaji kutengeneza tokeni ambayo mteja atatumia kuwasiliana na seva.

Piga simu:

```sh
python util.py
```

## Endesha msimbo

Endesha msimbo kwa:

```sh
python server.py
```

Katika terminal tofauti, andika:

```sh
python client.py
```

Katika terminal ya seva, unapaswa kuona kitu kama:

```text
Valid token, proceeding...
User exists, proceeding...
User has required scope, proceeding...
```

Katika dirisha la mteja, unapaswa kuona maandishi yanayofanana na:

```text
Tool result: meta=None content=[TextContent(type='text', text='{\n  "current_time": "2025-10-06T17:37:39.847457",\n  "timezone": "UTC",\n  "timestamp": 1759772259.847457,\n  "formatted": "2025-10-06 17:37:39"\n}', annotations=None, meta=None)] structuredContent={'current_time': '2025-10-06T17:37:39.847457', 'timezone': 'UTC', 'timestamp': 1759772259.847457, 'formatted': '2025-10-06 17:37:39'} isError=False
```

Hii inamaanisha kila kitu kinafanya kazi

### Badilisha maelezo, ili kuona ikishindwa

Tafuta msimbo huu katika *server.py*:

```python
 if not has_scope(has_header, "Admin.Write"):
```

Badilisha ili iseme "User.Write". Tokeni yako ya sasa haina kiwango hicho cha ruhusa, kwa hivyo ukianzisha tena seva na kujaribu kuendesha mteja mara nyingine tena unapaswa kuona kosa linalofanana na yafuatayo katika terminal ya seva:

```text
Valid token, proceeding...
User exists, proceeding...
-> Missing required scope!
```

Unaweza kubadilisha tena msimbo wa seva yako au kutengeneza tokeni mpya inayojumuisha upeo huu wa ziada, ni juu yako.

---

**Kanusho**:  
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kwa usahihi, tafadhali fahamu kuwa tafsiri za kiotomatiki zinaweza kuwa na makosa au kutokuwa sahihi. Hati asilia katika lugha yake ya asili inapaswa kuzingatiwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu ya binadamu inapendekezwa. Hatutawajibika kwa kutoelewana au tafsiri zisizo sahihi zinazotokana na matumizi ya tafsiri hii.