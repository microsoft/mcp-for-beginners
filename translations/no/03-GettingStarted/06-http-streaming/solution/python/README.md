# Kjøre dette eksemplet

Her er hvordan du kjører den klassiske HTTP-strømmeserveren og -klienten, samt MCP-strømmeserveren og -klienten ved bruk av Python.

### Oversikt

- Du skal sette opp en MCP-server som sender fremdriftsvarsler til klienten mens den behandler elementer.
- Klienten vil vise hvert varsel i sanntid.
- Denne veiledningen dekker forutsetninger, oppsett, kjøring og feilsøking.

### Forutsetninger

- Python 3.9 eller nyere
- Python-pakken `mcp` (installer med `pip install mcp`)

### Installasjon og oppsett

1. Klon repositoriet eller last ned løsningsfilene.

   ```pwsh
   git clone https://github.com/microsoft/mcp-for-beginners
   ```

1. **Opprett og aktiver et virtuelt miljø (anbefalt):**

   ```pwsh
   python -m venv venv
   .\venv\Scripts\Activate.ps1  # On Windows
   # or
   source venv/bin/activate      # On Linux/macOS
   ```

1. **Installer nødvendige avhengigheter:**

   ```pwsh
   pip install "mcp[cli]" fastapi requests
   ```

### Filer

- **Server:** [server.py](../../../../../../03-GettingStarted/06-http-streaming/solution/python/server.py)
- **Klient:** [client.py](../../../../../../03-GettingStarted/06-http-streaming/solution/python/client.py)

### Kjøre den klassiske HTTP-strømmeserveren

1. Gå til løsningsmappen:

   ```pwsh
   cd 03-GettingStarted/06-http-streaming/solution
   ```

2. Start den klassiske HTTP-strømmeserveren:

   ```pwsh
   python server.py
   ```

3. Serveren vil starte og vise:

   ```
   Starting FastAPI server for classic HTTP streaming...
   INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
   ```

### Kjøre den klassiske HTTP-strømmeklienten

1. Åpne et nytt terminalvindu (aktiver det samme virtuelle miljøet og katalogen):

   ```pwsh
   cd 03-GettingStarted/06-http-streaming/solution
   python client.py
   ```

2. Du bør se strømmede meldinger skrevet ut sekvensielt:

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

### Kjøre MCP-strømmeserveren

1. Gå til løsningsmappen:
   ```pwsh
   cd 03-GettingStarted/06-http-streaming/solution
   ```
2. Start MCP-serveren med transporttypen streamable-http:
   ```pwsh
   python server.py mcp
   ```
3. Serveren vil starte og vise:
   ```
   Starting MCP server with streamable-http transport...
   INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
   ```

### Kjøre MCP-strømmeklienten

1. Åpne et nytt terminalvindu (aktiver det samme virtuelle miljøet og katalogen):
   ```pwsh
   cd 03-GettingStarted/06-http-streaming/solution
   python client.py mcp
   ```
2. Du bør se varsler skrevet ut i sanntid mens serveren behandler hvert element:
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

### Viktige implementeringstrinn

1. **Opprett MCP-serveren ved bruk av FastMCP.**
2. **Definer et verktøy som behandler en liste og sender varsler ved bruk av `ctx.info()` eller `ctx.log()`.**
3. **Kjør serveren med `transport="streamable-http"`.**
4. **Implementer en klient med en meldingshåndterer for å vise varsler etter hvert som de ankommer.**

### Gjennomgang av kode
- Serveren bruker asynkrone funksjoner og MCP-konteksten for å sende fremdriftsoppdateringer.
- Klienten implementerer en asynkron meldingshåndterer for å skrive ut varsler og det endelige resultatet.

### Tips og feilsøking

- Bruk `async/await` for ikke-blokkerende operasjoner.
- Håndter alltid unntak i både server og klient for robusthet.
- Test med flere klienter for å observere sanntidsoppdateringer.
- Hvis du støter på feil, sjekk Python-versjonen din og sørg for at alle avhengigheter er installert.

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det originale dokumentet på sitt opprinnelige språk bør anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.