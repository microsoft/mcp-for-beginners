# Rulează exemplul

## Creează mediul

```sh
python -m venv venv
source ./venv/bin/activate
```

## Instalează dependențele

```sh
pip install "mcp[cli]" dotenv PyJWT requeests
```

## Generează token-ul

Va trebui să generezi un token pe care clientul îl va folosi pentru a comunica cu serverul.

Execută:

```sh
python util.py
```

## Rulează codul

Rulează codul cu:

```sh
python server.py
```

Într-un terminal separat, tastează:

```sh
python client.py
```

În terminalul serverului, ar trebui să vezi ceva de genul:

```text
Valid token, proceeding...
User exists, proceeding...
User has required scope, proceeding...
```

În fereastra clientului, ar trebui să vezi text similar cu:

```text
Tool result: meta=None content=[TextContent(type='text', text='{\n  "current_time": "2025-10-06T17:37:39.847457",\n  "timezone": "UTC",\n  "timestamp": 1759772259.847457,\n  "formatted": "2025-10-06 17:37:39"\n}', annotations=None, meta=None)] structuredContent={'current_time': '2025-10-06T17:37:39.847457', 'timezone': 'UTC', 'timestamp': 1759772259.847457, 'formatted': '2025-10-06 17:37:39'} isError=False
```

Aceasta înseamnă că totul funcționează.

### Modifică informațiile pentru a vedea cum eșuează

Localizează acest cod în *server.py*:

```python
 if not has_scope(has_header, "Admin.Write"):
```

Modifică-l astfel încât să spună "User.Write". Token-ul tău actual nu are acel nivel de permisiune, așa că dacă repornești serverul și încerci să rulezi clientul din nou, ar trebui să vezi o eroare similară cu următoarea în terminalul serverului:

```text
Valid token, proceeding...
User exists, proceeding...
-> Missing required scope!
```

Poți fie să revii la codul original al serverului, fie să generezi un nou token care să conțină acest scop suplimentar, alegerea îți aparține.

---

**Declinare de responsabilitate**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim să asigurăm acuratețea, vă rugăm să fiți conștienți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa maternă ar trebui considerat sursa autoritară. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist uman. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care pot apărea din utilizarea acestei traduceri.