# Protocolul Model Context (MCP) Implementare Python

Acest depozit conține o implementare Python a Protocolului Model Context (MCP), demonstrând cum să creezi atât o aplicație server, cât și una client care comunică folosind standardul MCP.

## Prezentare generală

Implementarea MCP constă în două componente principale:

1. **Server MCP (`server.py`)** - Un server care expune:
   - **Tools**: Funcții care pot fi apelate de la distanță
   - **Resources**: Date care pot fi accesate
   - **Prompts**: Șabloane pentru generarea de prompturi pentru modelele de limbaj

2. **Client MCP (`client.py`)** - O aplicație client care se conectează la server și folosește funcționalitățile acestuia

## Funcționalități

Această implementare demonstrează câteva caracteristici cheie ale MCP:

### Tools
- `completion` - Generează completări de text folosind modele AI (simulat)
- `add` - Calculator simplu care adună două numere

### Resources
- `models://` - Returnează informații despre modelele AI disponibile
- `greeting://{name}` - Returnează un mesaj personalizat pentru un nume dat

### Prompts
- `review_code` - Generează un prompt pentru revizuirea codului

## Instalare

Pentru a folosi această implementare MCP, instalează pachetele necesare:

```powershell
pip install mcp-server mcp-client
```

## Pornirea Serverului și Clientului

### Pornirea Serverului

Rulează serverul într-o fereastră de terminal:

```powershell
python server.py
```

Serverul poate fi rulat și în modul dezvoltare folosind MCP CLI:

```powershell
mcp dev server.py
```

Sau instalat în Claude Desktop (dacă este disponibil):

```powershell
mcp install server.py
```

### Pornirea Clientului

Rulează clientul într-o altă fereastră de terminal:

```powershell
python client.py
```

Aceasta va conecta clientul la server și va demonstra toate funcționalitățile disponibile.

### Utilizarea Clientului

Clientul (`client.py`) demonstrează toate capabilitățile MCP:

```powershell
python client.py
```

Aceasta va conecta clientul la server și va testa toate funcțiile, inclusiv tools, resources și prompts. Rezultatul va afișa:

1. Rezultatul tool-ului calculator (5 + 7 = 12)
2. Răspunsul tool-ului completion la întrebarea „Care este sensul vieții?”
3. Lista modelelor AI disponibile
4. Mesaj personalizat pentru „MCP Explorer”
5. Șablonul promptului pentru revizuirea codului

## Detalii de implementare

Serverul este implementat folosind API-ul `FastMCP`, care oferă abstracții de nivel înalt pentru definirea serviciilor MCP. Iată un exemplu simplificat despre cum sunt definite tools:

```python
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers together
    
    Args:
        a: First number
        b: Second number
    
    Returns:
        The sum of the two numbers
    """
    logger.info(f"Adding {a} and {b}")
    return a + b
```

Clientul folosește biblioteca client MCP pentru a se conecta și a apela serverul:

```python
async with stdio_client(server_params) as (reader, writer):
    async with ClientSession(reader, writer) as session:
        await session.initialize()
        result = await session.call_tool("add", arguments={"a": 5, "b": 7})
```

## Află mai multe

Pentru mai multe informații despre MCP, vizitează: https://modelcontextprotocol.io/

**Declinare de responsabilitate**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist uman. Nu ne asumăm răspunderea pentru eventualele neînțelegeri sau interpretări greșite rezultate din utilizarea acestei traduceri.