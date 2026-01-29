# Kör exempel

## Skapa miljö

```sh
python -m venv venv
source ./venv/bin/activate
```

## Installera beroenden

```sh
pip install "mcp[cli]" dotenv PyJWT requeests
```

## Generera token

Du behöver generera en token som klienten kommer att använda för att kommunicera med servern.

Anropa:

```sh
python util.py
```

## Kör kod

Kör koden med:

```sh
python server.py
```

I ett separat terminalfönster, skriv:

```sh
python client.py
```

I serverns terminalfönster bör du se något liknande:

```text
Valid token, proceeding...
User exists, proceeding...
User has required scope, proceeding...
```

I klientens fönster bör du se text som liknar:

```text
Tool result: meta=None content=[TextContent(type='text', text='{\n  "current_time": "2025-10-06T17:37:39.847457",\n  "timezone": "UTC",\n  "timestamp": 1759772259.847457,\n  "formatted": "2025-10-06 17:37:39"\n}', annotations=None, meta=None)] structuredContent={'current_time': '2025-10-06T17:37:39.847457', 'timezone': 'UTC', 'timestamp': 1759772259.847457, 'formatted': '2025-10-06 17:37:39'} isError=False
```

Detta betyder att allt fungerar.

### Ändra informationen för att se att det misslyckas

Leta upp denna kod i *server.py*:

```python
 if not has_scope(has_header, "Admin.Write"):
```

Ändra den så att den säger "User.Write". Din nuvarande token har inte den behörighetsnivån, så om du startar om servern och försöker köra klienten igen bör du se ett felmeddelande som liknar följande i serverns terminalfönster:

```text
Valid token, proceeding...
User exists, proceeding...
-> Missing required scope!
```

Du kan antingen ändra tillbaka din serverkod eller generera en ny token som innehåller detta ytterligare omfång, valet är ditt.

---

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, bör det noteras att automatiserade översättningar kan innehålla fel eller felaktigheter. Det ursprungliga dokumentet på dess ursprungliga språk bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för eventuella missförstånd eller feltolkningar som uppstår vid användning av denna översättning.