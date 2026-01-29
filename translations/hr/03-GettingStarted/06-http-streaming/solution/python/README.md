# Pokretanje ovog primjera

Evo kako pokrenuti klasični HTTP streaming server i klijent, kao i MCP streaming server i klijent koristeći Python.

### Pregled

- Postavit ćete MCP server koji šalje obavijesti o napretku klijentu dok obrađuje stavke.
- Klijent će prikazivati svaku obavijest u stvarnom vremenu.
- Ovaj vodič pokriva preduvjete, postavljanje, pokretanje i rješavanje problema.

### Preduvjeti

- Python 3.9 ili noviji
- Python paket `mcp` (instalirajte pomoću `pip install mcp`)

### Instalacija i Postavljanje

1. Klonirajte repozitorij ili preuzmite datoteke rješenja.

   ```pwsh
   git clone https://github.com/microsoft/mcp-for-beginners
   ```

1. **Kreirajte i aktivirajte virtualno okruženje (preporučeno):**

   ```pwsh
   python -m venv venv
   .\venv\Scripts\Activate.ps1  # On Windows
   # or
   source venv/bin/activate      # On Linux/macOS
   ```

1. **Instalirajte potrebne ovisnosti:**

   ```pwsh
   pip install "mcp[cli]" fastapi requests
   ```

### Datoteke

- **Server:** [server.py](../../../../../../03-GettingStarted/06-http-streaming/solution/python/server.py)
- **Klijent:** [client.py](../../../../../../03-GettingStarted/06-http-streaming/solution/python/client.py)

### Pokretanje Klasičnog HTTP Streaming Servera

1. Idite u direktorij rješenja:

   ```pwsh
   cd 03-GettingStarted/06-http-streaming/solution
   ```

2. Pokrenite klasični HTTP streaming server:

   ```pwsh
   python server.py
   ```

3. Server će se pokrenuti i prikazati:

   ```
   Starting FastAPI server for classic HTTP streaming...
   INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
   ```

### Pokretanje Klasičnog HTTP Streaming Klijenta

1. Otvorite novi terminal (aktivirajte isto virtualno okruženje i direktorij):

   ```pwsh
   cd 03-GettingStarted/06-http-streaming/solution
   python client.py
   ```

2. Trebali biste vidjeti poruke koje se ispisuju redom:

   ```text
   Running classic HTTP streaming client...
   Connecting to http://localhost:8000/stream with message: hello
   --- Streaming Progress ---
   Processing file 1/3...
   Processing file 2/3...
   Processing file 3/3...
   Here's the file content: hello
   --- Stream Ended ---
   ```

### Pokretanje MCP Streaming Servera

1. Idite u direktorij rješenja:
   ```pwsh
   cd 03-GettingStarted/06-http-streaming/solution
   ```
2. Pokrenite MCP server s transportom streamable-http:
   ```pwsh
   python server.py mcp
   ```
3. Server će se pokrenuti i prikazati:
   ```
   Starting MCP server with streamable-http transport...
   INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
   ```

### Pokretanje MCP Streaming Klijenta

1. Otvorite novi terminal (aktivirajte isto virtualno okruženje i direktorij):
   ```pwsh
   cd 03-GettingStarted/06-http-streaming/solution
   python client.py mcp
   ```
2. Trebali biste vidjeti obavijesti koje se ispisuju u stvarnom vremenu dok server obrađuje svaku stavku:
   ```
   Running MCP client...
   Starting client...
   Session ID before init: None
   Session ID after init: a30ab7fca9c84f5fa8f5c54fe56c9612
   Session initialized, ready to call tools.
   Received message: root=LoggingMessageNotification(...)
   NOTIFICATION: root=LoggingMessageNotification(...)
   ...
   Tool result: meta=None content=[TextContent(type='text', text='Processed files: file_1.txt, file_2.txt, file_3.txt | Message: hello from client')]
   ```

### Ključni Koraci Implementacije

1. **Kreirajte MCP server koristeći FastMCP.**
2. **Definirajte alat koji obrađuje popis i šalje obavijesti koristeći `ctx.info()` ili `ctx.log()`.**
3. **Pokrenite server s `transport="streamable-http"`.**
4. **Implementirajte klijenta s rukovateljem poruka za prikaz obavijesti kako stižu.**

### Pregled Koda
- Server koristi asinhrone funkcije i MCP kontekst za slanje ažuriranja o napretku.
- Klijent implementira asinhroni rukovatelj poruka za ispis obavijesti i konačnog rezultata.

### Savjeti i Rješavanje Problema

- Koristite `async/await` za neblokirajuće operacije.
- Uvijek rukujte iznimkama na serveru i klijentu radi robusnosti.
- Testirajte s više klijenata kako biste promatrali ažuriranja u stvarnom vremenu.
- Ako naiđete na greške, provjerite verziju Pythona i osigurajte da su sve ovisnosti instalirane.

**Odricanje od odgovornosti**:  
Ovaj dokument je preveden korištenjem AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo osigurati točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati mjerodavnim izvorom. Za ključne informacije preporučuje se profesionalni prijevod od strane stručnjaka. Ne preuzimamo odgovornost za bilo kakve nesporazume ili pogrešne interpretacije proizašle iz korištenja ovog prijevoda.