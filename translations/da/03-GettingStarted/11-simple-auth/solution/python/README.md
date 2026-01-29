# Kør eksempel

## Opret miljø

```sh
python -m venv venv
source ./venv/bin/activate
```

## Installer afhængigheder

```sh
pip install "mcp[cli]" dotenv PyJWT requeests
```

## Generer token

Du skal generere en token, som klienten vil bruge til at kommunikere med serveren.

Kald:

```sh
python util.py
```

## Kør kode

Kør koden med:

```sh
python server.py
```

I en separat terminal, skriv:

```sh
python client.py
```

I serverens terminal bør du se noget lignende:

```text
Valid token, proceeding...
User exists, proceeding...
User has required scope, proceeding...
```

I klientvinduet bør du se tekst, der ligner:

```text
Tool result: meta=None content=[TextContent(type='text', text='{\n  "current_time": "2025-10-06T17:37:39.847457",\n  "timezone": "UTC",\n  "timestamp": 1759772259.847457,\n  "formatted": "2025-10-06 17:37:39"\n}', annotations=None, meta=None)] structuredContent={'current_time': '2025-10-06T17:37:39.847457', 'timezone': 'UTC', 'timestamp': 1759772259.847457, 'formatted': '2025-10-06 17:37:39'} isError=False
```

Dette betyder, at det hele fungerer.

### Ændr informationen for at se det fejle

Find denne kode i *server.py*:

```python
 if not has_scope(has_header, "Admin.Write"):
```

Ændr det, så det siger "User.Write". Din nuværende token har ikke dette tilladelsesniveau, så hvis du genstarter serveren og prøver at køre klienten igen, bør du se en fejl, der ligner følgende i serverens terminal:

```text
Valid token, proceeding...
User exists, proceeding...
-> Missing required scope!
```

Du kan enten ændre din serverkode tilbage eller generere en ny token, der indeholder dette ekstra scope, det er op til dig.

---

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal det bemærkes, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os ikke ansvar for misforståelser eller fejltolkninger, der måtte opstå som følge af brugen af denne oversættelse.