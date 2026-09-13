# Depanare cu MCP Inspector

> [!NOTE]
> Comenzile care folosesc `--sse` și URL-urile care se termină cu `/sse` testează transportul moștenit HTTP+SSE.
> Pentru un server MCP `2026-07-28` nou, folosește o versiune Inspector care
> suportă HTTP Streamable și selectează acel transport în schimb.

**MCP Inspector** este un instrument esențial de depanare care îți permite să testezi interactiv și să rezolvi problemele serverelor tale MCP fără a avea nevoie de o aplicație completă de gazduire AI. Gândește-l ca pe un "Postman pentru MCP" - oferă o interfață vizuală pentru a trimite cereri, a vizualiza răspunsuri și a înțelege comportamentul serverului tău.

## De ce să folosești MCP Inspector?

Când construiești servere MCP, vei întâmpina adesea aceste provocări:

- **„Serverul meu funcționează oare?”** - Inspector afișează starea conexiunii
- **„Sunt uneltele mele înregistrate corect?”** - Inspector listează toate uneltele disponibile
- **„Care este formatul răspunsului?”** - Inspector afișează răspunsuri JSON complete
- **„De ce nu funcționează această unealtă?”** - Inspector arată mesaje detaliate de eroare

## Cerințe prealabile

- Node.js 18+ instalat
- npm (vine împreună cu Node.js)
- Un server MCP de testat (vezi [Module 3.1 - First Server](../01-first-server/README.md))

## Instalare

### Opțiunea 1: Rulare cu npx (Recomandat pentru testări rapide)

```bash
npx @modelcontextprotocol/inspector
```

### Opțiunea 2: Instalare globală

```bash
npm install -g @modelcontextprotocol/inspector
mcp-inspector
```

### Opțiunea 3: Adaugă în proiectul tău

```bash
cd your-mcp-server-project
npm install --save-dev @modelcontextprotocol/inspector
```

Adaugă în `package.json`:
```json
{
  "scripts": {
    "inspector": "mcp-inspector"
  }
}
```

---

## Conectarea la serverul tău

### Servere stdio (Proces local)

Pentru servere care comunică prin intrare/ieșire standard:

```bash
# Server Python
npx @modelcontextprotocol/inspector python -m your_server_module

# Server Node.js
npx @modelcontextprotocol/inspector node ./build/index.js

# Cu variabile de mediu
OPENAI_API_KEY=xxx npx @modelcontextprotocol/inspector python server.py
```

### Servere SSE/HTTP (Rețea)

Pentru servere care rulează ca servicii HTTP:

1. Pornește serverul mai întâi:
   ```bash
   python server.py  # Serverul rulează pe http://localhost:8080
   ```

2. Lansează Inspector și conectează-te:
   ```bash
   npx @modelcontextprotocol/inspector --sse http://localhost:8080/sse
   ```

---

## Prezentare Interfață Inspector

Când Inspector pornește, vei vedea o interfață web (de obicei la `http://localhost:5173`):

```
┌─────────────────────────────────────────────────────────────┐
│  MCP Inspector                              [Connected ✅]   │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐         │
│  │   🔧 Tools  │  │ 📄 Resources│  │ 💬 Prompts  │         │
│  │    (3)      │  │    (2)      │  │    (1)      │         │
│  └─────────────┘  └─────────────┘  └─────────────┘         │
│                                                             │
│  ┌───────────────────────────────────────────────────────┐ │
│  │  📋 Message Log                                       │ │
│  │  ─────────────────────────────────────────────────── │ │
│  │  → initialize                                         │ │
│  │  ← initialized (server info)                          │ │
│  │  → tools/list                                         │ │
│  │  ← tools (3 tools)                                    │ │
│  └───────────────────────────────────────────────────────┘ │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## Testarea Uneltelor

### Listarea uneltelor disponibile

1. Dă click pe fila **Tools**
2. Inspector apelează automat `tools/list`
3. Vei vedea toate uneltele înregistrate cu:
   - Numele uneltei
   - Descrierea
   - Schema de intrare (parametrii)

### Invocarea unei unelte

1. Selectează o unealtă din listă
2. Completează parametrii necesari în formular
3. Apasă **Run Tool**
4. Vezi răspunsul în panoul de rezultate

**Exemplu: Testarea unei unelte de calculator**

```
Tool: add
Parameters:
  a: 25
  b: 17

Response:
{
  "content": [
    {
      "type": "text",
      "text": "42"
    }
  ]
}
```

### Depanarea erorilor uneltelor

Când o unealtă eșuează, Inspector afișează:

```
Error Response:
{
  "error": {
    "code": -32602,
    "message": "Invalid params: 'b' is required"
  }
}
```

Coduri de eroare comune:
| Cod | Semnificație |
|------|---------|
| -32700 | Eroare de analiză (JSON invalid) |
| -32600 | Cerere nevalidă |
| -32601 | Metoda negăsită |
| -32602 | Parametri nevalizi |
| -32603 | Eroare internă |

---

## Testarea Resurselor

### Listarea resurselor

1. Dă click pe fila **Resources**
2. Inspector apelează `resources/list`
3. Vei vedea:
   - URI-urile resurselor
   - Numele și descrierile
   - Tipurile MIME

### Citirea unei resurse

1. Selectează o resursă
2. Apasă **Read Resource**
3. Vezi conținutul returnat

**Exemplu de rezultat:**

```
Resource: file:///config/settings.json
Content-Type: application/json

{
  "config": {
    "debug": true,
    "maxConnections": 10
  }
}
```

---

## Testarea Prompturilor

### Listarea prompturilor

1. Dă click pe fila **Prompts**
2. Inspector apelează `prompts/list`
3. Vezi șabloanele de prompt disponibile

### Obținerea unui prompt

1. Selectează un prompt
2. Completează argumentele necesare
3. Apasă **Get Prompt**
4. Vezi mesajele promptului generate

---

## Analiza jurnalului de mesaje

Jurnalul de mesaje arată toate mesajele protocolului MCP. Transcrierea de mai jos este dintr-un
server moștenit `2025-11-25` și include handshake-ul `initialize` eliminat. Un server
`2026-07-28` folosește metadate ale cererii autonome și `server/discover`
în schimb.

```
14:32:01 → {"jsonrpc":"2.0","id":1,"method":"initialize",...}
14:32:01 ← {"jsonrpc":"2.0","id":1,"result":{"protocolVersion":"2025-11-25",...}}
14:32:02 → {"jsonrpc":"2.0","id":2,"method":"tools/list"}
14:32:02 ← {"jsonrpc":"2.0","id":2,"result":{"tools":[...]}}
14:32:05 → {"jsonrpc":"2.0","id":3,"method":"tools/call","params":{"name":"add",...}}
14:32:05 ← {"jsonrpc":"2.0","id":3,"result":{"content":[...]}}
```

### La ce să fii atent

- **Perechi cerere/răspuns**: Fiecare `→` ar trebui să aibă un `←` corespunzător
- **Mesaje de eroare**: Caută `"error"` în răspunsuri
- **Timp**: Pauzele mari pot indica probleme de performanță
- **Versiunea protocolului**: Asigură-te că serverul și clientul sunt acordați pe versiune

---

## Integrare VS Code

Poți rula Inspector direct din VS Code:

### Folosind launch.json

Adaugă în `.vscode/launch.json`:

```json
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "Debug with MCP Inspector",
      "type": "node",
      "request": "launch",
      "runtimeExecutable": "npx",
      "runtimeArgs": [
        "@modelcontextprotocol/inspector",
        "python",
        "${workspaceFolder}/server.py"
      ],
      "console": "integratedTerminal"
    },
    {
      "name": "Debug SSE Server with Inspector",
      "type": "chrome",
      "request": "launch",
      "url": "http://localhost:5173",
      "preLaunchTask": "Start MCP Inspector"
    }
  ]
}
```

### Folosind Tasks

Adaugă în `.vscode/tasks.json`:

```json
{
  "version": "2.0.0",
  "tasks": [
    {
      "label": "Start MCP Inspector",
      "type": "shell",
      "command": "npx @modelcontextprotocol/inspector node ${workspaceFolder}/build/index.js",
      "isBackground": true,
      "problemMatcher": {
        "pattern": {
          "regexp": "^$"
        },
        "background": {
          "activeOnStart": true,
          "beginsPattern": "Inspector",
          "endsPattern": "listening"
        }
      }
    }
  ]
}
```

---

## Scenarii comune de depanare

### Scenariul 1: Serverul nu se conectează

**Simptome:** Inspector afișează „Disconnected” sau rămâne blocat pe „Connecting...”

**Lista de verificare:**
1. ✅ Comanda serverului este corectă?
2. ✅ Sunt toate dependențele instalate?
3. ✅ Calea serverului este absolută sau relativă față de directorul curent?
4. ✅ Sunt toate variabilele de mediu necesare setate?

**Pași de depanare:**
```bash
# Testează manual serverul mai întâi
python -c "import your_server_module; print('OK')"

# Verifică pentru erori de import
python -m your_server_module 2>&1 | head -20

# Verifică dacă MCP SDK este instalat
pip show mcp
```

### Scenariul 2: Uneltele nu apar

**Simptome:** Fila unelte afișează o listă goală

**Cauze posibile:**
1. Uneltele nu au fost înregistrate la inițializarea serverului
2. Serverul a căzut după pornire
3. Handler-ul `tools/list` returnează un array gol

**Pași de depanare:**
1. Verifică în jurnal răspunsul la `tools/list`
2. Adaugă logare în codul de înregistrare al uneltelor tale
3. Verifică dacă decoratorii `@mcp.tool()` sunt prezenți (Python)

### Scenariul 3: Unealta returnează eroare

**Simptome:** Apelul uneltei returnează răspuns de eroare

**Abordare de depanare:**
1. Citește cu atenție mesajul de eroare
2. Verifică dacă tipurile parametrilor corespund schemei
3. Adaugă try/catch cu mesaje detaliate de eroare
4. Verifică jurnalele serverului pentru stack trace-uri

**Exemplu de gestionare îmbunătățită a erorilor:**

```python
@mcp.tool()
async def my_tool(param1: str, param2: int) -> str:
    try:
        # Logica uneltei aici
        result = process(param1, param2)
        return str(result)
    except ValueError as e:
        raise McpError(f"Invalid parameter: {e}")
    except Exception as e:
        raise McpError(f"Tool failed: {type(e).__name__}: {e}")
```

### Scenariul 4: Conținutul resursei gol

**Simptome:** Resursa este returnată, dar conținutul este gol sau null

**Lista de verificare:**
1. ✅ Calea fișierului sau URI este corectă
2. ✅ Serverul are permisiunea de a citi resursa
3. ✅ Conținutul resursei este returnat corect

---

## Funcționalități avansate Inspector

### Headere personalizate (SSE)

```bash
npx @modelcontextprotocol/inspector \
  --sse http://localhost:8080/sse \
  --header "Authorization: Bearer your-token"
```

### Logare detaliată

```bash
DEBUG=mcp* npx @modelcontextprotocol/inspector python server.py
```

### Înregistrarea sesiunilor

Inspector poate exporta jurnalele de mesaje pentru analiza ulterioară:
1. Apasă **Export Log** în panoul de mesaje
2. Salvează fișierul JSON
3. Distribuie colegilor pentru depanare

---

## Cele mai bune practici

1. **Testează devreme și des** - Folosește Inspector în timpul dezvoltării, nu doar când apar probleme
2. **Începe simplu** - Testează conexiunea de bază înaintea apelurilor complexe
3. **Verifică schema** - Multe erori provin din nepotriviri de tipuri de parametri
4. **Citește mesajele de eroare** - Erorile MCP sunt de obicei descriptive
5. **Menține Inspector deschis** - Ajută la prinderea problemelor pe parcursul dezvoltării

---

## Ce urmează

Ai terminat Modulul 3: Începem! Continuă-ți învățarea:

- [Module 4: Practical Implementation](../../04-PracticalImplementation/README.md)

---

## Resurse suplimentare

- [MCP Inspector GitHub Repository](https://github.com/modelcontextprotocol/inspector)
- [MCP Specification - Protocol Messages](https://modelcontextprotocol.io/specification/2026-07-28/)
- [JSON-RPC 2.0 Specification](https://www.jsonrpc.org/specification)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Declinare a responsabilității**:
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). În timp ce ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un om. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care decurg din utilizarea acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->