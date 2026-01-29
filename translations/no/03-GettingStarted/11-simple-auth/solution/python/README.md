# Kjør eksempel

## Opprett miljø

```sh
python -m venv venv
source ./venv/bin/activate
```

## Installer avhengigheter

```sh
pip install "mcp[cli]" dotenv PyJWT requeests
```

## Generer token

Du må generere en token som klienten vil bruke for å kommunisere med serveren.

Kjør:

```sh
python util.py
```

## Kjør kode

Kjør koden med:

```sh
python server.py
```

I et separat terminalvindu, skriv:

```sh
python client.py
```

I serverens terminal, bør du se noe som:

```text
Valid token, proceeding...
User exists, proceeding...
User has required scope, proceeding...
```

I klientvinduet, bør du se tekst som ligner på:

```text
Tool result: meta=None content=[TextContent(type='text', text='{\n  "current_time": "2025-10-06T17:37:39.847457",\n  "timezone": "UTC",\n  "timestamp": 1759772259.847457,\n  "formatted": "2025-10-06 17:37:39"\n}', annotations=None, meta=None)] structuredContent={'current_time': '2025-10-06T17:37:39.847457', 'timezone': 'UTC', 'timestamp': 1759772259.847457, 'formatted': '2025-10-06 17:37:39'} isError=False
```

Dette betyr at alt fungerer.

### Endre informasjonen for å se at det feiler

Finn denne koden i *server.py*:

```python
 if not has_scope(has_header, "Admin.Write"):
```

Endre den slik at den sier "User.Write". Din nåværende token har ikke dette tillatelsesnivået, så hvis du starter serveren på nytt og prøver å kjøre klienten en gang til, bør du se en feil som ligner på følgende i serverens terminal:

```text
Valid token, proceeding...
User exists, proceeding...
-> Missing required scope!
```

Du kan enten endre tilbake serverkoden din eller generere en ny token som inneholder dette ekstra omfanget, valget er ditt.

---

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi tilstreber nøyaktighet, vær oppmerksom på at automatiserte oversettelser kan inneholde feil eller unøyaktigheter. Det originale dokumentet på sitt opprinnelige språk bør anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.