# Pokreni primjer

## Kreiraj okruženje

```sh
python -m venv venv
source ./venv/bin/activate
```

## Instaliraj ovisnosti

```sh
pip install "mcp[cli]" dotenv PyJWT requeests
```

## Generiraj token

Trebat ćete generirati token koji će klijent koristiti za komunikaciju s poslužiteljem.

Pozovite:

```sh
python util.py
```

## Pokreni kod

Pokrenite kod s:

```sh
python server.py
```

U zasebnom terminalu, upišite:

```sh
python client.py
```

U terminalu poslužitelja trebali biste vidjeti nešto poput:

```text
Valid token, proceeding...
User exists, proceeding...
User has required scope, proceeding...
```

U prozoru klijenta trebali biste vidjeti tekst sličan:

```text
Tool result: meta=None content=[TextContent(type='text', text='{\n  "current_time": "2025-10-06T17:37:39.847457",\n  "timezone": "UTC",\n  "timestamp": 1759772259.847457,\n  "formatted": "2025-10-06 17:37:39"\n}', annotations=None, meta=None)] structuredContent={'current_time': '2025-10-06T17:37:39.847457', 'timezone': 'UTC', 'timestamp': 1759772259.847457, 'formatted': '2025-10-06 17:37:39'} isError=False
```

To znači da sve radi.

### Promijenite informacije kako biste vidjeli da ne radi

Pronađite ovaj kod u *server.py*:

```python
 if not has_scope(has_header, "Admin.Write"):
```

Promijenite ga tako da kaže "User.Write". Vaš trenutni token nema tu razinu dopuštenja, pa ako ponovno pokrenete poslužitelj i pokušate ponovno pokrenuti klijenta, trebali biste vidjeti pogrešku sličnu sljedećoj u terminalu poslužitelja:

```text
Valid token, proceeding...
User exists, proceeding...
-> Missing required scope!
```

Možete ili vratiti svoj kod poslužitelja na prethodno stanje ili generirati novi token koji sadrži ovaj dodatni opseg, izbor je na vama.

---

**Izjava o odricanju odgovornosti**:  
Ovaj dokument je preveden pomoću AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo osigurati točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za ključne informacije preporučuje se profesionalni prijevod od strane stručnjaka. Ne preuzimamo odgovornost za nesporazume ili pogrešna tumačenja koja mogu proizaći iz korištenja ovog prijevoda.