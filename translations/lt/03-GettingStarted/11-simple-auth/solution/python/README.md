# Paleisti pavyzdį

## Sukurti aplinką

```sh
python -m venv venv
source ./venv/bin/activate
```

## Įdiegti priklausomybes

```sh
pip install "mcp[cli]" dotenv PyJWT requeests
```

## Sukurti žetoną

Jums reikės sukurti žetoną, kurį klientas naudos bendraudamas su serveriu.

Paleiskite:

```sh
python util.py
```

## Paleisti kodą

Paleiskite kodą su:

```sh
python server.py
```

Kitame terminale įveskite:

```sh
python client.py
```

Serverio terminale turėtumėte matyti kažką panašaus į:

```text
Valid token, proceeding...
User exists, proceeding...
User has required scope, proceeding...
```

Kliento lange turėtumėte matyti tekstą, panašų į:

```text
Tool result: meta=None content=[TextContent(type='text', text='{\n  "current_time": "2025-10-06T17:37:39.847457",\n  "timezone": "UTC",\n  "timestamp": 1759772259.847457,\n  "formatted": "2025-10-06 17:37:39"\n}', annotations=None, meta=None)] structuredContent={'current_time': '2025-10-06T17:37:39.847457', 'timezone': 'UTC', 'timestamp': 1759772259.847457, 'formatted': '2025-10-06 17:37:39'} isError=False
```

Tai reiškia, kad viskas veikia.

### Pakeiskite informaciją, kad pamatytumėte klaidą

Suraskite šį kodą *server.py* faile:

```python
 if not has_scope(has_header, "Admin.Write"):
```

Pakeiskite jį taip, kad būtų "User.Write". Jūsų dabartinis žetonas neturi tokio leidimų lygio, todėl, jei iš naujo paleisite serverį ir bandysite dar kartą paleisti klientą, serverio terminale turėtumėte matyti klaidą, panašią į šią:

```text
Valid token, proceeding...
User exists, proceeding...
-> Missing required scope!
```

Galite arba grąžinti serverio kodą į pradinę būseną, arba sukurti naują žetoną, kuris turėtų šį papildomą leidimą – sprendimas priklauso nuo jūsų.

---

**Atsakomybės atsisakymas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors stengiamės užtikrinti tikslumą, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojama naudoti profesionalų žmogaus vertimą. Mes neprisiimame atsakomybės už nesusipratimus ar klaidingus interpretavimus, atsiradusius dėl šio vertimo naudojimo.