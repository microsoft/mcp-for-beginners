# Spustit ukázku

## Vytvoření prostředí

```sh
python -m venv venv
source ./venv/bin/activate
```

## Instalace závislostí

```sh
pip install "mcp[cli]" dotenv PyJWT requeests
```

## Generování tokenu

Budete muset vygenerovat token, který klient použije pro komunikaci se serverem.

Zavolejte:

```sh
python util.py
```

## Spuštění kódu

Spusťte kód pomocí:

```sh
python server.py
```

V samostatném terminálu napište:

```sh
python client.py
```

V terminálu serveru byste měli vidět něco jako:

```text
Valid token, proceeding...
User exists, proceeding...
User has required scope, proceeding...
```

V okně klienta byste měli vidět text podobný:

```text
Tool result: meta=None content=[TextContent(type='text', text='{\n  "current_time": "2025-10-06T17:37:39.847457",\n  "timezone": "UTC",\n  "timestamp": 1759772259.847457,\n  "formatted": "2025-10-06 17:37:39"\n}', annotations=None, meta=None)] structuredContent={'current_time': '2025-10-06T17:37:39.847457', 'timezone': 'UTC', 'timestamp': 1759772259.847457, 'formatted': '2025-10-06 17:37:39'} isError=False
```

To znamená, že vše funguje.

### Změna informací, abyste viděli chybu

Najděte tento kód v *server.py*:

```python
 if not has_scope(has_header, "Admin.Write"):
```

Změňte ho tak, aby říkal "User.Write". Váš aktuální token nemá tuto úroveň oprávnění, takže pokud restartujete server a pokusíte se znovu spustit klienta, měli byste v terminálu serveru vidět chybu podobnou následující:

```text
Valid token, proceeding...
User exists, proceeding...
-> Missing required scope!
```

Můžete buď vrátit zpět změny v kódu serveru, nebo vygenerovat nový token, který obsahuje tento dodatečný rozsah, je to na vás.

---

**Prohlášení**:  
Tento dokument byl přeložen pomocí služby AI pro překlady [Co-op Translator](https://github.com/Azure/co-op-translator). I když se snažíme o přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho původním jazyce by měl být považován za autoritativní zdroj. Pro důležité informace doporučujeme profesionální lidský překlad. Neodpovídáme za žádná nedorozumění nebo nesprávné interpretace vyplývající z použití tohoto překladu.