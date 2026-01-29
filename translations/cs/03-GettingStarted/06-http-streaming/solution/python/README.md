# Spuštění tohoto příkladu

Zde je návod, jak spustit klasický HTTP streaming server a klienta, stejně jako MCP streaming server a klienta pomocí Pythonu.

### Přehled

- Nastavíte MCP server, který bude během zpracování položek odesílat klientovi oznámení o průběhu.
- Klient bude zobrazovat každé oznámení v reálném čase.
- Tento průvodce pokrývá předpoklady, nastavení, spuštění a řešení problémů.

### Předpoklady

- Python 3.9 nebo novější
- Python balíček `mcp` (nainstalujte pomocí `pip install mcp`)

### Instalace a nastavení

1. Naklonujte repozitář nebo stáhněte soubory řešení.

   ```pwsh
   git clone https://github.com/microsoft/mcp-for-beginners
   ```

1. **Vytvořte a aktivujte virtuální prostředí (doporučeno):**

   ```pwsh
   python -m venv venv
   .\venv\Scripts\Activate.ps1  # On Windows
   # or
   source venv/bin/activate      # On Linux/macOS
   ```

1. **Nainstalujte potřebné závislosti:**

   ```pwsh
   pip install "mcp[cli]" fastapi requests
   ```

### Soubory

- **Server:** [server.py](../../../../../../03-GettingStarted/06-http-streaming/solution/python/server.py)
- **Klient:** [client.py](../../../../../../03-GettingStarted/06-http-streaming/solution/python/client.py)

### Spuštění klasického HTTP streaming serveru

1. Přejděte do adresáře s řešením:

   ```pwsh
   cd 03-GettingStarted/06-http-streaming/solution
   ```

2. Spusťte klasický HTTP streaming server:

   ```pwsh
   python server.py
   ```

3. Server se spustí a zobrazí:

   ```
   Starting FastAPI server for classic HTTP streaming...
   INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
   ```

### Spuštění klasického HTTP streaming klienta

1. Otevřete nový terminál (aktivujte stejné virtuální prostředí a adresář):

   ```pwsh
   cd 03-GettingStarted/06-http-streaming/solution
   python client.py
   ```

2. Měli byste vidět postupně vypisované zprávy:

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

### Spuštění MCP streaming serveru

1. Přejděte do adresáře s řešením:
   ```pwsh
   cd 03-GettingStarted/06-http-streaming/solution
   ```
2. Spusťte MCP server s transportem streamable-http:
   ```pwsh
   python server.py mcp
   ```
3. Server se spustí a zobrazí:
   ```
   Starting MCP server with streamable-http transport...
   INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
   ```

### Spuštění MCP streaming klienta

1. Otevřete nový terminál (aktivujte stejné virtuální prostředí a adresář):
   ```pwsh
   cd 03-GettingStarted/06-http-streaming/solution
   python client.py mcp
   ```
2. Měli byste vidět oznámení vypisovaná v reálném čase, jak server zpracovává jednotlivé položky:
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

### Klíčové kroky implementace

1. **Vytvořte MCP server pomocí FastMCP.**
2. **Definujte nástroj, který zpracovává seznam a odesílá oznámení pomocí `ctx.info()` nebo `ctx.log()`.**
3. **Spusťte server s `transport="streamable-http"`.**
4. **Implementujte klienta s obslužnou funkcí zpráv pro zobrazení oznámení při jejich příchodu.**

### Procházka kódem
- Server používá asynchronní funkce a MCP kontext pro odesílání aktualizací o průběhu.
- Klient implementuje asynchronní obslužnou funkci zpráv pro tisk oznámení a konečného výsledku.

### Tipy a řešení problémů

- Používejte `async/await` pro neblokující operace.
- Vždy ošetřujte výjimky jak na straně serveru, tak klienta pro zajištění robustnosti.
- Testujte s více klienty, abyste viděli aktualizace v reálném čase.
- Pokud narazíte na chyby, zkontrolujte verzi Pythonu a ujistěte se, že všechny závislosti jsou nainstalovány.

**Upozornění**:  
Tento dokument byl přeložen pomocí služby pro automatický překlad [Co-op Translator](https://github.com/Azure/co-op-translator). I když se snažíme o co největší přesnost, mějte prosím na paměti, že automatické překlady mohou obsahovat chyby nebo nepřesnosti. Za autoritativní zdroj by měl být považován původní dokument v jeho původním jazyce. Pro důležité informace doporučujeme profesionální lidský překlad. Neodpovídáme za žádná nedorozumění nebo nesprávné interpretace vyplývající z použití tohoto překladu.