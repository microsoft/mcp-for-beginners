# Paleisti šį pavyzdį

Štai kaip paleisti klasikinį HTTP srautinį serverį ir klientą, taip pat MCP srautinį serverį ir klientą naudojant Python.

### Apžvalga

- Jūs nustatysite MCP serverį, kuris siunčia progreso pranešimus klientui, kai apdoroja elementus.
- Klientas realiu laiku rodys kiekvieną pranešimą.
- Šiame vadove aptariami reikalavimai, nustatymas, paleidimas ir trikčių šalinimas.

### Reikalavimai

- Python 3.9 ar naujesnė versija
- Python paketas `mcp` (įdiegti naudojant `pip install mcp`)

### Įdiegimas ir nustatymas

1. Nukopijuokite saugyklą arba atsisiųskite sprendimo failus.

   ```pwsh
   git clone https://github.com/microsoft/mcp-for-beginners
   ```

1. **Sukurkite ir aktyvuokite virtualią aplinką (rekomenduojama):**

   ```pwsh
   python -m venv venv
   .\venv\Scripts\Activate.ps1  # On Windows
   # or
   source venv/bin/activate      # On Linux/macOS
   ```

1. **Įdiekite reikalingas priklausomybes:**

   ```pwsh
   pip install "mcp[cli]" fastapi requests
   ```

### Failai

- **Serveris:** [server.py](../../../../../../03-GettingStarted/06-http-streaming/solution/python/server.py)
- **Klientas:** [client.py](../../../../../../03-GettingStarted/06-http-streaming/solution/python/client.py)

### Klasikinio HTTP srautinio serverio paleidimas

1. Pereikite į sprendimo katalogą:

   ```pwsh
   cd 03-GettingStarted/06-http-streaming/solution
   ```

2. Paleiskite klasikinį HTTP srautinį serverį:

   ```pwsh
   python server.py
   ```

3. Serveris pradės veikti ir parodys:

   ```
   Starting FastAPI server for classic HTTP streaming...
   INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
   ```

### Klasikinio HTTP srautinio kliento paleidimas

1. Atidarykite naują terminalą (aktyvuokite tą pačią virtualią aplinką ir katalogą):

   ```pwsh
   cd 03-GettingStarted/06-http-streaming/solution
   python client.py
   ```

2. Turėtumėte matyti srautu siunčiamus pranešimus, rodomus nuosekliai:

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

### MCP srautinio serverio paleidimas

1. Pereikite į sprendimo katalogą:
   ```pwsh
   cd 03-GettingStarted/06-http-streaming/solution
   ```
2. Paleiskite MCP serverį su streamable-http transportu:
   ```pwsh
   python server.py mcp
   ```
3. Serveris pradės veikti ir parodys:
   ```
   Starting MCP server with streamable-http transport...
   INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
   ```

### MCP srautinio kliento paleidimas

1. Atidarykite naują terminalą (aktyvuokite tą pačią virtualią aplinką ir katalogą):
   ```pwsh
   cd 03-GettingStarted/06-http-streaming/solution
   python client.py mcp
   ```
2. Turėtumėte matyti pranešimus, rodomus realiu laiku, kai serveris apdoroja kiekvieną elementą:
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

### Pagrindiniai įgyvendinimo žingsniai

1. **Sukurkite MCP serverį naudodami FastMCP.**
2. **Apibrėžkite įrankį, kuris apdoroja sąrašą ir siunčia pranešimus naudojant `ctx.info()` arba `ctx.log()`.**
3. **Paleiskite serverį su `transport="streamable-http"`.**
4. **Įgyvendinkite klientą su pranešimų tvarkytuvu, kad rodytų pranešimus, kai jie atvyksta.**

### Kodo apžvalga
- Serveris naudoja asinchronines funkcijas ir MCP kontekstą, kad siųstų progreso atnaujinimus.
- Klientas įgyvendina asinchroninį pranešimų tvarkytuvą, kad spausdintų pranešimus ir galutinį rezultatą.

### Patarimai ir trikčių šalinimas

- Naudokite `async/await` neblokuojančioms operacijoms.
- Visada tvarkykite išimtis tiek serveryje, tiek kliente, kad užtikrintumėte patikimumą.
- Testuokite su keliais klientais, kad stebėtumėte realaus laiko atnaujinimus.
- Jei susiduriate su klaidomis, patikrinkite savo Python versiją ir įsitikinkite, kad visos priklausomybės yra įdiegtos.

---

**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojama profesionali žmogaus vertimo paslauga. Mes neprisiimame atsakomybės už nesusipratimus ar klaidingus interpretavimus, atsiradusius naudojant šį vertimą.