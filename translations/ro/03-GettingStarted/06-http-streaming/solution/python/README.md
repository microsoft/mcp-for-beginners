# Rularea acestui exemplu

Iată cum să rulezi serverul și clientul clasic de streaming HTTP, precum și serverul și clientul MCP de streaming utilizând Python.

### Prezentare generală

- Vei configura un server MCP care transmite notificări de progres către client pe măsură ce procesează elementele.
- Clientul va afișa fiecare notificare în timp real.
- Acest ghid acoperă cerințele preliminare, configurarea, rularea și depanarea.

### Cerințe preliminare

- Python 3.9 sau o versiune mai nouă
- Pachetul Python `mcp` (instalează-l cu `pip install mcp`)

### Instalare și configurare

1. Clonează depozitul sau descarcă fișierele soluției.

   ```pwsh
   git clone https://github.com/microsoft/mcp-for-beginners
   ```

1. **Creează și activează un mediu virtual (recomandat):**

   ```pwsh
   python -m venv venv
   .\venv\Scripts\Activate.ps1  # On Windows
   # or
   source venv/bin/activate      # On Linux/macOS
   ```

1. **Instalează dependențele necesare:**

   ```pwsh
   pip install "mcp[cli]" fastapi requests
   ```

### Fișiere

- **Server:** [server.py](../../../../../../03-GettingStarted/06-http-streaming/solution/python/server.py)
- **Client:** [client.py](../../../../../../03-GettingStarted/06-http-streaming/solution/python/client.py)

### Rularea serverului clasic de streaming HTTP

1. Navighează la directorul soluției:

   ```pwsh
   cd 03-GettingStarted/06-http-streaming/solution
   ```

2. Pornește serverul clasic de streaming HTTP:

   ```pwsh
   python server.py
   ```

3. Serverul va porni și va afișa:

   ```
   Starting FastAPI server for classic HTTP streaming...
   INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
   ```

### Rularea clientului clasic de streaming HTTP

1. Deschide un nou terminal (activează același mediu virtual și director):

   ```pwsh
   cd 03-GettingStarted/06-http-streaming/solution
   python client.py
   ```

2. Ar trebui să vezi mesajele transmise afișate secvențial:

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

### Rularea serverului MCP de streaming

1. Navighează la directorul soluției:
   ```pwsh
   cd 03-GettingStarted/06-http-streaming/solution
   ```
2. Pornește serverul MCP cu transportul streamable-http:
   ```pwsh
   python server.py mcp
   ```
3. Serverul va porni și va afișa:
   ```
   Starting MCP server with streamable-http transport...
   INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
   ```

### Rularea clientului MCP de streaming

1. Deschide un nou terminal (activează același mediu virtual și director):
   ```pwsh
   cd 03-GettingStarted/06-http-streaming/solution
   python client.py mcp
   ```
2. Ar trebui să vezi notificările afișate în timp real pe măsură ce serverul procesează fiecare element:
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

### Pași cheie de implementare

1. **Creează serverul MCP utilizând FastMCP.**
2. **Definește un instrument care procesează o listă și trimite notificări utilizând `ctx.info()` sau `ctx.log()`.**
3. **Rulează serverul cu `transport="streamable-http"`.**
4. **Implementează un client cu un handler de mesaje pentru a afișa notificările pe măsură ce sosesc.**

### Prezentare a codului
- Serverul utilizează funcții asincrone și contextul MCP pentru a trimite actualizări de progres.
- Clientul implementează un handler de mesaje asincron pentru a afișa notificările și rezultatul final.

### Sfaturi și depanare

- Utilizează `async/await` pentru operațiuni non-blocante.
- Gestionează întotdeauna excepțiile atât în server, cât și în client pentru a asigura robustețea.
- Testează cu mai mulți clienți pentru a observa actualizările în timp real.
- Dacă întâmpini erori, verifică versiunea de Python și asigură-te că toate dependențele sunt instalate.

**Declinarea responsabilității**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși depunem eforturi pentru a asigura acuratețea, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa natală ar trebui considerat sursa autoritară. Pentru informații critice, se recomandă traducerea umană realizată de profesioniști. Nu ne asumăm răspunderea pentru eventualele neînțelegeri sau interpretări greșite care pot apărea din utilizarea acestei traduceri.