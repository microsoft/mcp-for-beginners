# Mintapéldák futtatása

## Környezet létrehozása

```sh
python -m venv venv
source ./venv/bin/activate
```

## Függőségek telepítése

```sh
pip install "mcp[cli]" dotenv PyJWT requeests
```

## Token generálása

Generálnod kell egy tokent, amelyet az ügyfél használni fog a szerverrel való kommunikációhoz.

Hívd meg:

```sh
python util.py
```

## Kód futtatása

Futtasd a kódot ezzel:

```sh
python server.py
```

Egy külön terminálban írd be:

```sh
python client.py
```

A szerver termináljában valami ilyesmit kell látnod:

```text
Valid token, proceeding...
User exists, proceeding...
User has required scope, proceeding...
```

Az ügyfél ablakában hasonló szöveget kell látnod:

```text
Tool result: meta=None content=[TextContent(type='text', text='{\n  "current_time": "2025-10-06T17:37:39.847457",\n  "timezone": "UTC",\n  "timestamp": 1759772259.847457,\n  "formatted": "2025-10-06 17:37:39"\n}', annotations=None, meta=None)] structuredContent={'current_time': '2025-10-06T17:37:39.847457', 'timezone': 'UTC', 'timestamp': 1759772259.847457, 'formatted': '2025-10-06 17:37:39'} isError=False
```

Ez azt jelenti, hogy minden működik.

### Módosítsd az információt, hogy láthasd, hogyan hibázik

Keresd meg ezt a kódot a *server.py*-ben:

```python
 if not has_scope(has_header, "Admin.Write"):
```

Módosítsd úgy, hogy "User.Write"-t írjon. A jelenlegi tokened nem rendelkezik ezzel a jogosultsági szinttel, így ha újraindítod a szervert és megpróbálod újra futtatni az ügyfelet, a szerver termináljában valami ehhez hasonló hibát kell látnod:

```text
Valid token, proceeding...
User exists, proceeding...
-> Missing required scope!
```

Visszaállíthatod a szerver kódját az eredetire, vagy generálhatsz egy új tokent, amely tartalmazza ezt a további jogosultságot – rajtad múlik.

---

**Felelősség kizárása**:  
Ez a dokumentum az [Co-op Translator](https://github.com/Azure/co-op-translator) AI fordítási szolgáltatás segítségével lett lefordítva. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az eredeti nyelvén tekintendő hiteles forrásnak. Kritikus információk esetén javasolt professzionális emberi fordítást igénybe venni. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely a fordítás használatából eredhet.