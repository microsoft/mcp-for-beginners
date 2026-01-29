# Protocollo Model Context (MCP) Implementazione in Python

Questo repository contiene un'implementazione in Python del Protocollo Model Context (MCP), che mostra come creare sia un'applicazione server che client che comunicano utilizzando lo standard MCP.

## Panoramica

L'implementazione MCP è composta da due componenti principali:

1. **MCP Server (`server.py`)** - Un server che espone:
   - **Tools**: Funzioni che possono essere chiamate da remoto
   - **Resources**: Dati che possono essere recuperati
   - **Prompts**: Modelli per generare prompt per modelli linguistici

2. **MCP Client (`client.py`)** - Un'applicazione client che si connette al server e utilizza le sue funzionalità

## Funzionalità

Questa implementazione dimostra diverse funzionalità chiave di MCP:

### Tools
- `completion` - Genera completamenti di testo da modelli AI (simulato)
- `add` - Calcolatrice semplice che somma due numeri

### Resources
- `models://` - Restituisce informazioni sui modelli AI disponibili
- `greeting://{name}` - Restituisce un saluto personalizzato per un nome specifico

### Prompts
- `review_code` - Genera un prompt per la revisione del codice

## Installazione

Per utilizzare questa implementazione MCP, installa i pacchetti richiesti:

```powershell
pip install mcp-server mcp-client
```

## Avvio del Server e del Client

### Avvio del Server

Esegui il server in una finestra del terminale:

```powershell
python server.py
```

Il server può anche essere eseguito in modalità sviluppo usando la CLI MCP:

```powershell
mcp dev server.py
```

Oppure installato in Claude Desktop (se disponibile):

```powershell
mcp install server.py
```

### Avvio del Client

Esegui il client in un'altra finestra del terminale:

```powershell
python client.py
```

Questo si connetterà al server e dimostrerà tutte le funzionalità disponibili.

### Uso del Client

Il client (`client.py`) dimostra tutte le capacità MCP:

```powershell
python client.py
```

Questo si connetterà al server e utilizzerà tutte le funzionalità, inclusi tools, resources e prompts. L'output mostrerà:

1. Risultato dello strumento calcolatrice (5 + 7 = 12)
2. Risposta dello strumento completion a "Qual è il significato della vita?"
3. Elenco dei modelli AI disponibili
4. Saluto personalizzato per "MCP Explorer"
5. Modello di prompt per la revisione del codice

## Dettagli di Implementazione

Il server è implementato usando l'API `FastMCP`, che fornisce astrazioni di alto livello per definire servizi MCP. Ecco un esempio semplificato di come vengono definiti i tools:

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

Il client utilizza la libreria client MCP per connettersi e chiamare il server:

```python
async with stdio_client(server_params) as (reader, writer):
    async with ClientSession(reader, writer) as session:
        await session.initialize()
        result = await session.call_tool("add", arguments={"a": 5, "b": 7})
```

## Per saperne di più

Per maggiori informazioni su MCP, visita: https://modelcontextprotocol.io/

**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica [Co-op Translator](https://github.com/Azure/co-op-translator). Pur impegnandoci per garantire l’accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un umano. Non ci assumiamo alcuna responsabilità per eventuali malintesi o interpretazioni errate derivanti dall’uso di questa traduzione.