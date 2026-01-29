# Dit voorbeeld uitvoeren

Hier lees je hoe je de klassieke HTTP-streamingserver en -client, evenals de MCP-streamingserver en -client met Python kunt uitvoeren.

### Overzicht

- Je zet een MCP-server op die voortgangsnotificaties naar de client streamt terwijl het items verwerkt.
- De client toont elke notificatie in realtime.
- Deze handleiding behandelt vereisten, installatie, uitvoering en probleemoplossing.

### Vereisten

- Python 3.9 of nieuwer
- Het `mcp` Python-pakket (installeren met `pip install mcp`)

### Installatie & Setup

1. Clone de repository of download de oplossingsbestanden.

   ```pwsh
   git clone https://github.com/microsoft/mcp-for-beginners
   ```

1. **Maak en activeer een virtuele omgeving (aanbevolen):**

   ```pwsh
   python -m venv venv
   .\venv\Scripts\Activate.ps1  # On Windows
   # or
   source venv/bin/activate      # On Linux/macOS
   ```

1. **Installeer de benodigde afhankelijkheden:**

   ```pwsh
   pip install "mcp[cli]" fastapi requests
   ```

### Bestanden

- **Server:** [server.py](../../../../../../03-GettingStarted/06-http-streaming/solution/python/server.py)
- **Client:** [client.py](../../../../../../03-GettingStarted/06-http-streaming/solution/python/client.py)

### De klassieke HTTP-streamingserver uitvoeren

1. Navigeer naar de oplossingsmap:

   ```pwsh
   cd 03-GettingStarted/06-http-streaming/solution
   ```

2. Start de klassieke HTTP-streamingserver:

   ```pwsh
   python server.py
   ```

3. De server zal starten en het volgende weergeven:

   ```
   Starting FastAPI server for classic HTTP streaming...
   INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
   ```

### De klassieke HTTP-streamingclient uitvoeren

1. Open een nieuwe terminal (activeer dezelfde virtuele omgeving en map):

   ```pwsh
   cd 03-GettingStarted/06-http-streaming/solution
   python client.py
   ```

2. Je zou gestreamde berichten moeten zien die opeenvolgend worden afgedrukt:

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

### De MCP-streamingserver uitvoeren

1. Navigeer naar de oplossingsmap:
   ```pwsh
   cd 03-GettingStarted/06-http-streaming/solution
   ```
2. Start de MCP-server met de streamable-http transport:
   ```pwsh
   python server.py mcp
   ```
3. De server zal starten en het volgende weergeven:
   ```
   Starting MCP server with streamable-http transport...
   INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
   ```

### De MCP-streamingclient uitvoeren

1. Open een nieuwe terminal (activeer dezelfde virtuele omgeving en map):
   ```pwsh
   cd 03-GettingStarted/06-http-streaming/solution
   python client.py mcp
   ```
2. Je zou notificaties in realtime moeten zien terwijl de server elk item verwerkt:
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

### Belangrijke implementatiestappen

1. **Maak de MCP-server met FastMCP.**
2. **Definieer een tool die een lijst verwerkt en notificaties verzendt met `ctx.info()` of `ctx.log()`.**
3. **Voer de server uit met `transport="streamable-http"`.**
4. **Implementeer een client met een berichtverwerker om notificaties weer te geven zodra ze binnenkomen.**

### Code-uitleg
- De server gebruikt asynchrone functies en de MCP-context om voortgangsupdates te verzenden.
- De client implementeert een asynchrone berichtverwerker om notificaties en het eindresultaat af te drukken.

### Tips & Probleemoplossing

- Gebruik `async/await` voor niet-blokkerende operaties.
- Zorg ervoor dat je uitzonderingen afhandelt in zowel de server als de client voor robuustheid.
- Test met meerdere clients om realtime updates te observeren.
- Als je fouten tegenkomt, controleer je Python-versie en zorg ervoor dat alle afhankelijkheden zijn geïnstalleerd.

**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsservice [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we ons best doen voor nauwkeurigheid, dient u zich ervan bewust te zijn dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor cruciale informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.