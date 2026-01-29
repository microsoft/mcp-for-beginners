# Zagon tega primera

Tukaj je opis, kako zagnati klasični HTTP strežniški in odjemalski tok ter MCP strežniški in odjemalski tok z uporabo Pythona.

### Pregled

- Nastavili boste MCP strežnik, ki med obdelavo elementov pošilja obvestila o napredku odjemalcu.
- Odjemalec bo prikazoval vsako obvestilo v realnem času.
- Ta vodič zajema predpogoje, nastavitev, zagon in odpravljanje težav.

### Predpogoji

- Python 3.9 ali novejši
- Python paket `mcp` (namestite z `pip install mcp`)

### Namestitev in nastavitev

1. Klonirajte repozitorij ali prenesite datoteke rešitve.

   ```pwsh
   git clone https://github.com/microsoft/mcp-for-beginners
   ```

1. **Ustvarite in aktivirajte virtualno okolje (priporočeno):**

   ```pwsh
   python -m venv venv
   .\venv\Scripts\Activate.ps1  # On Windows
   # or
   source venv/bin/activate      # On Linux/macOS
   ```

1. **Namestite potrebne odvisnosti:**

   ```pwsh
   pip install "mcp[cli]" fastapi requests
   ```

### Datoteke

- **Strežnik:** [server.py](../../../../../../03-GettingStarted/06-http-streaming/solution/python/server.py)
- **Odjemalec:** [client.py](../../../../../../03-GettingStarted/06-http-streaming/solution/python/client.py)

### Zagon klasičnega HTTP strežniškega toka

1. Pomaknite se v mapo z rešitvijo:

   ```pwsh
   cd 03-GettingStarted/06-http-streaming/solution
   ```

2. Zaženite klasični HTTP strežniški tok:

   ```pwsh
   python server.py
   ```

3. Strežnik se bo zagnal in prikazal:

   ```
   Starting FastAPI server for classic HTTP streaming...
   INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
   ```

### Zagon klasičnega HTTP odjemalskega toka

1. Odprite nov terminal (aktivirajte isto virtualno okolje in mapo):

   ```pwsh
   cd 03-GettingStarted/06-http-streaming/solution
   python client.py
   ```

2. Videti bi morali zaporedno natisnjena sporočila toka:

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

### Zagon MCP strežniškega toka

1. Pomaknite se v mapo z rešitvijo:
   ```pwsh
   cd 03-GettingStarted/06-http-streaming/solution
   ```
2. Zaženite MCP strežnik z uporabo transporta streamable-http:
   ```pwsh
   python server.py mcp
   ```
3. Strežnik se bo zagnal in prikazal:
   ```
   Starting MCP server with streamable-http transport...
   INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
   ```

### Zagon MCP odjemalskega toka

1. Odprite nov terminal (aktivirajte isto virtualno okolje in mapo):
   ```pwsh
   cd 03-GettingStarted/06-http-streaming/solution
   python client.py mcp
   ```
2. Videti bi morali obvestila, natisnjena v realnem času, ko strežnik obdeluje vsak element:
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

### Ključni koraki implementacije

1. **Ustvarite MCP strežnik z uporabo FastMCP.**
2. **Definirajte orodje, ki obdeluje seznam in pošilja obvestila z uporabo `ctx.info()` ali `ctx.log()`.**
3. **Zaženite strežnik z `transport="streamable-http"`.**
4. **Implementirajte odjemalca z obdelovalcem sporočil za prikaz obvestil ob njihovem prihodu.**

### Pregled kode
- Strežnik uporablja asinhrone funkcije in MCP kontekst za pošiljanje posodobitev o napredku.
- Odjemalec implementira asinhroni obdelovalec sporočil za tiskanje obvestil in končnega rezultata.

### Nasveti in odpravljanje težav

- Uporabite `async/await` za neblokirajoče operacije.
- Vedno obravnavajte izjeme tako na strežniku kot na odjemalcu za večjo zanesljivost.
- Testirajte z več odjemalci, da opazujete posodobitve v realnem času.
- Če naletite na napake, preverite svojo različico Pythona in zagotovite, da so vse odvisnosti nameščene.

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve za prevajanje z umetno inteligenco [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem maternem jeziku je treba obravnavati kot avtoritativni vir. Za ključne informacije priporočamo profesionalni človeški prevod. Ne prevzemamo odgovornosti za morebitna nesporazumevanja ali napačne razlage, ki izhajajo iz uporabe tega prevoda.