# Zagon vzorca

## Ustvarite okolje

```sh
python -m venv venv
source ./venv/bin/activate
```

## Namestite odvisnosti

```sh
pip install "mcp[cli]" dotenv PyJWT requeests
```

## Ustvarite žeton

Potrebno bo ustvariti žeton, ki ga bo odjemalec uporabil za komunikacijo s strežnikom.

Pokličite:

```sh
python util.py
```

## Zaženite kodo

Zaženite kodo z:

```sh
python server.py
```

V ločenem terminalu vnesite:

```sh
python client.py
```

V terminalu strežnika bi morali videti nekaj podobnega:

```text
Valid token, proceeding...
User exists, proceeding...
User has required scope, proceeding...
```

V oknu odjemalca bi morali videti besedilo, podobno:

```text
Tool result: meta=None content=[TextContent(type='text', text='{\n  "current_time": "2025-10-06T17:37:39.847457",\n  "timezone": "UTC",\n  "timestamp": 1759772259.847457,\n  "formatted": "2025-10-06 17:37:39"\n}', annotations=None, meta=None)] structuredContent={'current_time': '2025-10-06T17:37:39.847457', 'timezone': 'UTC', 'timestamp': 1759772259.847457, 'formatted': '2025-10-06 17:37:39'} isError=False
```

To pomeni, da vse deluje.

### Spremenite podatke, da vidite, kako ne uspe

Poiščite to kodo v *server.py*:

```python
 if not has_scope(has_header, "Admin.Write"):
```

Spremenite jo tako, da bo pisalo "User.Write". Vaš trenutni žeton nima te ravni dovoljenja, zato bi morali ob ponovnem zagonu strežnika in poskusu ponovnega zagona odjemalca videti napako, podobno naslednji v terminalu strežnika:

```text
Valid token, proceeding...
User exists, proceeding...
-> Missing required scope!
```

Lahko bodisi spremenite nazaj kodo strežnika ali ustvarite nov žeton, ki vsebuje to dodatno področje, izbira je vaša.

---

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve za prevajanje z umetno inteligenco [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem maternem jeziku je treba obravnavati kot avtoritativni vir. Za ključne informacije priporočamo profesionalni človeški prevod. Ne prevzemamo odgovornosti za morebitna napačna razumevanja ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.