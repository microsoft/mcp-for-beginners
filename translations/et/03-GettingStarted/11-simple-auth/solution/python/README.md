# Käivita näidis

## Loo keskkond

```sh
python -m venv venv
source ./venv/bin/activate
```

## Paigalda sõltuvused

```sh
pip install "mcp[cli]" dotenv PyJWT requeests
```

## Loo token

Peate looma tokeni, mida klient kasutab serveriga suhtlemiseks.

Käivita:

```sh
python util.py
```

## Käivita kood

Käivita kood käsuga:

```sh
python server.py
```

Teises terminalis sisesta:

```sh
python client.py
```

Serveri terminalis peaks ilmuma midagi sellist:

```text
Valid token, proceeding...
User exists, proceeding...
User has required scope, proceeding...
```

Kliendi aknas peaks ilmuma tekst, mis on sarnane:

```text
Tool result: meta=None content=[TextContent(type='text', text='{\n  "current_time": "2025-10-06T17:37:39.847457",\n  "timezone": "UTC",\n  "timestamp": 1759772259.847457,\n  "formatted": "2025-10-06 17:37:39"\n}', annotations=None, meta=None)] structuredContent={'current_time': '2025-10-06T17:37:39.847457', 'timezone': 'UTC', 'timestamp': 1759772259.847457, 'formatted': '2025-10-06 17:37:39'} isError=False
```

See tähendab, et kõik töötab.

### Muuda infot, et näha, kuidas see ebaõnnestub

Leia see kood *server.py*-failist:

```python
 if not has_scope(has_header, "Admin.Write"):
```

Muuda see nii, et seal oleks "User.Write". Teie praegusel tokenil pole seda õigustaset, nii et kui taaskäivitate serveri ja proovite klienti uuesti käivitada, peaksite serveri terminalis nägema viga, mis on sarnane järgmisega:

```text
Valid token, proceeding...
User exists, proceeding...
-> Missing required scope!
```

Võite kas taastada oma serveri koodi või luua uue tokeni, mis sisaldab seda täiendavat ulatust, valik on teie.

---

**Lahtiütlus**:  
See dokument on tõlgitud AI tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi püüame tagada täpsust, palume arvestada, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algses keeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitame kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valesti tõlgenduste eest.