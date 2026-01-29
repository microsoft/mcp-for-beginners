# Spustenie tejto ukážky

Tu je návod, ako spustiť klasický HTTP streaming server a klient, ako aj MCP streaming server a klient pomocou Pythonu.

### Prehľad

- Nastavíte MCP server, ktorý bude počas spracovania položiek odosielať klientovi notifikácie o priebehu.
- Klient bude zobrazovať každú notifikáciu v reálnom čase.
- Tento návod pokrýva predpoklady, nastavenie, spustenie a riešenie problémov.

### Predpoklady

- Python 3.9 alebo novší
- Python balík `mcp` (nainštalujte pomocou `pip install mcp`)

### Inštalácia a nastavenie

1. Naklonujte repozitár alebo stiahnite súbory riešenia.

   ```pwsh
   git clone https://github.com/microsoft/mcp-for-beginners
   ```

1. **Vytvorte a aktivujte virtuálne prostredie (odporúčané):**

   ```pwsh
   python -m venv venv
   .\venv\Scripts\Activate.ps1  # On Windows
   # or
   source venv/bin/activate      # On Linux/macOS
   ```

1. **Nainštalujte potrebné závislosti:**

   ```pwsh
   pip install "mcp[cli]" fastapi requests
   ```

### Súbory

- **Server:** [server.py](../../../../../../03-GettingStarted/06-http-streaming/solution/python/server.py)
- **Klient:** [client.py](../../../../../../03-GettingStarted/06-http-streaming/solution/python/client.py)

### Spustenie klasického HTTP streaming servera

1. Prejdite do adresára riešenia:

   ```pwsh
   cd 03-GettingStarted/06-http-streaming/solution
   ```

2. Spustite klasický HTTP streaming server:

   ```pwsh
   python server.py
   ```

3. Server sa spustí a zobrazí:

   ```
   Starting FastAPI server for classic HTTP streaming...
   INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
   ```

### Spustenie klasického HTTP streaming klienta

1. Otvorte nový terminál (aktivujte rovnaké virtuálne prostredie a adresár):

   ```pwsh
   cd 03-GettingStarted/06-http-streaming/solution
   python client.py
   ```

2. Mali by ste vidieť postupne vypisované správy:

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

### Spustenie MCP streaming servera

1. Prejdite do adresára riešenia:
   ```pwsh
   cd 03-GettingStarted/06-http-streaming/solution
   ```
2. Spustite MCP server s transportom streamable-http:
   ```pwsh
   python server.py mcp
   ```
3. Server sa spustí a zobrazí:
   ```
   Starting MCP server with streamable-http transport...
   INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
   ```

### Spustenie MCP streaming klienta

1. Otvorte nový terminál (aktivujte rovnaké virtuálne prostredie a adresár):
   ```pwsh
   cd 03-GettingStarted/06-http-streaming/solution
   python client.py mcp
   ```
2. Mali by ste vidieť notifikácie vypisované v reálnom čase, ako server spracováva jednotlivé položky:
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

### Kľúčové kroky implementácie

1. **Vytvorte MCP server pomocou FastMCP.**
2. **Definujte nástroj, ktorý spracováva zoznam a odosiela notifikácie pomocou `ctx.info()` alebo `ctx.log()`.**
3. **Spustite server s `transport="streamable-http"`.**
4. **Implementujte klienta so správcom správ, ktorý zobrazuje notifikácie pri ich príchode.**

### Prehľad kódu
- Server používa asynchrónne funkcie a MCP kontext na odosielanie aktualizácií o priebehu.
- Klient implementuje asynchrónneho správcu správ na vypisovanie notifikácií a konečného výsledku.

### Tipy a riešenie problémov

- Používajte `async/await` pre neblokujúce operácie.
- Vždy ošetrite výnimky na strane servera aj klienta pre vyššiu spoľahlivosť.
- Testujte s viacerými klientmi, aby ste videli aktualizácie v reálnom čase.
- Ak narazíte na chyby, skontrolujte verziu Pythonu a uistite sa, že všetky závislosti sú nainštalované.

**Upozornenie**:  
Tento dokument bol preložený pomocou služby na automatický preklad [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, upozorňujeme, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho pôvodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nenesieme zodpovednosť za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.