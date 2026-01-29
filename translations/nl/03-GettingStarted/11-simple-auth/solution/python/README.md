# Voorbeeld uitvoeren

## Maak omgeving aan

```sh
python -m venv venv
source ./venv/bin/activate
```

## Installeer afhankelijkheden

```sh
pip install "mcp[cli]" dotenv PyJWT requeests
```

## Genereer token

Je moet een token genereren dat de client zal gebruiken om met de server te communiceren.

Voer uit:

```sh
python util.py
```

## Code uitvoeren

Voer de code uit met:

```sh
python server.py
```

Open in een aparte terminal:

```sh
python client.py
```

In de serverterminal zou je iets moeten zien zoals:

```text
Valid token, proceeding...
User exists, proceeding...
User has required scope, proceeding...
```

In het clientvenster zou je tekst moeten zien die lijkt op:

```text
Tool result: meta=None content=[TextContent(type='text', text='{\n  "current_time": "2025-10-06T17:37:39.847457",\n  "timezone": "UTC",\n  "timestamp": 1759772259.847457,\n  "formatted": "2025-10-06 17:37:39"\n}', annotations=None, meta=None)] structuredContent={'current_time': '2025-10-06T17:37:39.847457', 'timezone': 'UTC', 'timestamp': 1759772259.847457, 'formatted': '2025-10-06 17:37:39'} isError=False
```

Dit betekent dat alles werkt.

### Wijzig de informatie om te zien dat het mislukt

Zoek deze code in *server.py*:

```python
 if not has_scope(has_header, "Admin.Write"):
```

Wijzig het zodat er "User.Write" staat. Je huidige token heeft dat machtigingsniveau niet, dus als je de server opnieuw start en probeert de client opnieuw uit te voeren, zou je een foutmelding moeten zien die lijkt op het volgende in de serverterminal:

```text
Valid token, proceeding...
User exists, proceeding...
-> Missing required scope!
```

Je kunt ofwel je servercode terugzetten naar de oorspronkelijke staat, of een nieuw token genereren dat deze extra scope bevat, de keuze is aan jou.

---

**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsservice [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u zich ervan bewust te zijn dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor cruciale informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.