# Kør dette eksempel

Her er hvordan du kører den klassiske HTTP-streamingserver og -klient samt MCP-streamingserveren og -klienten ved hjælp af Python.

### Oversigt

- Du vil opsætte en MCP-server, der streamer statusnotifikationer til klienten, mens den behandler elementer.
- Klienten vil vise hver notifikation i realtid.
- Denne guide dækker forudsætninger, opsætning, kørsel og fejlfinding.

### Forudsætninger

- Python 3.9 eller nyere
- Python-pakken `mcp` (installer med `pip install mcp`)

### Installation & Opsætning

1. Klon repositoryet eller download løsningsfilerne.

   ```pwsh
   git clone https://github.com/microsoft/mcp-for-beginners
   ```

1. **Opret og aktiver et virtuelt miljø (anbefales):**

   ```pwsh
   python -m venv venv
   .\venv\Scripts\Activate.ps1  # On Windows
   # or
   source venv/bin/activate      # On Linux/macOS
   ```

1. **Installer nødvendige afhængigheder:**

   ```pwsh
   pip install "mcp[cli]" fastapi requests
   ```

### Filer

- **Server:** [server.py](../../../../../../03-GettingStarted/06-http-streaming/solution/python/server.py)
- **Klient:** [client.py](../../../../../../03-GettingStarted/06-http-streaming/solution/python/client.py)

### Kørsel af den klassiske HTTP-streamingserver

1. Naviger til løsningsmappen:

   ```pwsh
   cd 03-GettingStarted/06-http-streaming/solution
   ```

2. Start den klassiske HTTP-streamingserver:

   ```pwsh
   python server.py
   ```

3. Serveren vil starte og vise:

   ```
   Starting FastAPI server for classic HTTP streaming...
   INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
   ```

### Kørsel af den klassiske HTTP-streamingklient

1. Åbn en ny terminal (aktiver det samme virtuelle miljø og mappe):

   ```pwsh
   cd 03-GettingStarted/06-http-streaming/solution
   python client.py
   ```

2. Du bør se streamede beskeder printet sekventielt:

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

### Kørsel af MCP-streamingserveren

1. Naviger til løsningsmappen:
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

### Kørsel af MCP-streamingklienten

1. Åbn en ny terminal (aktiver det samme virtuelle miljø og mappe):
   ```pwsh
   cd 03-GettingStarted/06-http-streaming/solution
   python client.py mcp
   ```
2. Du bør se notifikationer printet i realtid, mens serveren behandler hvert element:
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

### Vigtige Implementeringstrin

1. **Opret MCP-serveren ved hjælp af FastMCP.**
2. **Definér et værktøj, der behandler en liste og sender notifikationer ved hjælp af `ctx.info()` eller `ctx.log()`.**
3. **Kør serveren med `transport="streamable-http"`.**
4. **Implementér en klient med en beskedhåndtering, der viser notifikationer, når de ankommer.**

### Gennemgang af Koden
- Serveren bruger asynkrone funktioner og MCP-konteksten til at sende statusopdateringer.
- Klienten implementerer en asynkron beskedhåndtering til at printe notifikationer og det endelige resultat.

### Tips & Fejlfinding

- Brug `async/await` til ikke-blokerende operationer.
- Håndtér altid undtagelser i både server og klient for at sikre robusthed.
- Test med flere klienter for at observere opdateringer i realtid.
- Hvis du støder på fejl, så tjek din Python-version og sørg for, at alle afhængigheder er installeret.

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi er ikke ansvarlige for eventuelle misforståelser eller fejltolkninger, der måtte opstå som følge af brugen af denne oversættelse.