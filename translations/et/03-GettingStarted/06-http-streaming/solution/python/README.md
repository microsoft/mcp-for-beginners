# Selle näidise käivitamine

Siin on juhised klassikalise HTTP voogedastuse serveri ja kliendi ning MCP voogedastuse serveri ja kliendi käivitamiseks Pythonis.

### Ülevaade

- Seadistate MCP serveri, mis edastab kliendile edenemisteateid, kui see töötleb üksusi.
- Klient kuvab iga teate reaalajas.
- See juhend hõlmab eeldusi, seadistamist, käivitamist ja tõrkeotsingut.

### Eeldused

- Python 3.9 või uuem
- `mcp` Python pakett (installige käsuga `pip install mcp`)

### Paigaldamine ja seadistamine

1. Kloonige repositoorium või laadige alla lahenduse failid.

   ```pwsh
   git clone https://github.com/microsoft/mcp-for-beginners
   ```

1. **Looge ja aktiveerige virtuaalne keskkond (soovitatav):**

   ```pwsh
   python -m venv venv
   .\venv\Scripts\Activate.ps1  # On Windows
   # or
   source venv/bin/activate      # On Linux/macOS
   ```

1. **Installige vajalikud sõltuvused:**

   ```pwsh
   pip install "mcp[cli]" fastapi requests
   ```

### Failid

- **Server:** [server.py](../../../../../../03-GettingStarted/06-http-streaming/solution/python/server.py)
- **Klient:** [client.py](../../../../../../03-GettingStarted/06-http-streaming/solution/python/client.py)

### Klassikalise HTTP voogedastuse serveri käivitamine

1. Liikuge lahenduse kataloogi:

   ```pwsh
   cd 03-GettingStarted/06-http-streaming/solution
   ```

2. Käivitage klassikaline HTTP voogedastuse server:

   ```pwsh
   python server.py
   ```

3. Server käivitub ja kuvab:

   ```
   Starting FastAPI server for classic HTTP streaming...
   INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
   ```

### Klassikalise HTTP voogedastuse kliendi käivitamine

1. Avage uus terminal (aktiveerige sama virtuaalne keskkond ja kataloog):

   ```pwsh
   cd 03-GettingStarted/06-http-streaming/solution
   python client.py
   ```

2. Näete voogedastatud sõnumeid, mis kuvatakse järjestikku:

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

### MCP voogedastuse serveri käivitamine

1. Liikuge lahenduse kataloogi:
   ```pwsh
   cd 03-GettingStarted/06-http-streaming/solution
   ```
2. Käivitage MCP server koos streamable-http transpordiga:
   ```pwsh
   python server.py mcp
   ```
3. Server käivitub ja kuvab:
   ```
   Starting MCP server with streamable-http transport...
   INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
   ```

### MCP voogedastuse kliendi käivitamine

1. Avage uus terminal (aktiveerige sama virtuaalne keskkond ja kataloog):
   ```pwsh
   cd 03-GettingStarted/06-http-streaming/solution
   python client.py mcp
   ```
2. Näete teateid, mis kuvatakse reaalajas, kui server töötleb iga üksust:
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

### Olulised rakendamise sammud

1. **Looge MCP server, kasutades FastMCP-i.**
2. **Määratlege tööriist, mis töötleb loendit ja saadab teateid, kasutades `ctx.info()` või `ctx.log()`.**
3. **Käivitage server, kasutades `transport="streamable-http"`.**
4. **Rakendage klient koos sõnumikäitlejaga, et kuvada teateid nende saabumisel.**

### Koodi ülevaade
- Server kasutab asünkroonseid funktsioone ja MCP konteksti edenemisteadete saatmiseks.
- Klient rakendab asünkroonse sõnumikäitleja, et teateid ja lõpptulemust kuvada.

### Näpunäited ja tõrkeotsing

- Kasutage `async/await` mitteblokeerivate toimingute jaoks.
- Käsitlege alati erandeid nii serveris kui ka kliendis, et tagada töökindlus.
- Testige mitme kliendiga, et jälgida reaalajas uuendusi.
- Kui ilmnevad vead, kontrollige oma Pythoni versiooni ja veenduge, et kõik sõltuvused on paigaldatud.

---

**Lahtiütlus**:  
See dokument on tõlgitud AI tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi püüame tagada täpsust, palume arvestada, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algses keeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitame kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valesti tõlgenduste eest.