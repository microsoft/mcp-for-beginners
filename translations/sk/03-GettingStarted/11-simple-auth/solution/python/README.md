# Spustenie ukážky

## Vytvorenie prostredia

```sh
python -m venv venv
source ./venv/bin/activate
```

## Inštalácia závislostí

```sh
pip install "mcp[cli]" dotenv PyJWT requeests
```

## Generovanie tokenu

Budete musieť vygenerovať token, ktorý klient použije na komunikáciu so serverom.

Zavolajte:

```sh
python util.py
```

## Spustenie kódu

Spustite kód pomocou:

```sh
python server.py
```

V samostatnom termináli zadajte:

```sh
python client.py
```

V termináli servera by ste mali vidieť niečo ako:

```text
Valid token, proceeding...
User exists, proceeding...
User has required scope, proceeding...
```

V okne klienta by ste mali vidieť text podobný:

```text
Tool result: meta=None content=[TextContent(type='text', text='{\n  "current_time": "2025-10-06T17:37:39.847457",\n  "timezone": "UTC",\n  "timestamp": 1759772259.847457,\n  "formatted": "2025-10-06 17:37:39"\n}', annotations=None, meta=None)] structuredContent={'current_time': '2025-10-06T17:37:39.847457', 'timezone': 'UTC', 'timestamp': 1759772259.847457, 'formatted': '2025-10-06 17:37:39'} isError=False
```

To znamená, že všetko funguje.

### Zmeňte informácie, aby ste videli chybu

Nájdite tento kód v súbore *server.py*:

```python
 if not has_scope(has_header, "Admin.Write"):
```

Zmeňte ho tak, aby obsahoval "User.Write". Váš aktuálny token nemá túto úroveň oprávnenia, takže ak reštartujete server a pokúsite sa znova spustiť klienta, mali by ste vidieť chybu podobnú nasledujúcej v termináli servera:

```text
Valid token, proceeding...
User exists, proceeding...
-> Missing required scope!
```

Môžete buď vrátiť späť zmeny v kóde servera, alebo vygenerovať nový token, ktorý obsahuje tento dodatočný rozsah, je to na vás.

---

**Upozornenie**:  
Tento dokument bol preložený pomocou služby AI prekladu [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, prosím, berte na vedomie, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho rodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nenesieme zodpovednosť za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.