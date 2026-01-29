# Utilizzo avanzato del server

Ci sono due tipi di server esposti nell'MCP SDK: il server normale e il server di basso livello. Normalmente, si utilizza il server regolare per aggiungere funzionalità. Tuttavia, in alcuni casi, è preferibile affidarsi al server di basso livello, ad esempio:

- Migliore architettura. È possibile creare un'architettura pulita sia con il server regolare che con il server di basso livello, ma si può sostenere che sia leggermente più semplice con quest'ultimo.
- Disponibilità delle funzionalità. Alcune funzionalità avanzate possono essere utilizzate solo con un server di basso livello. Vedrai questo nei capitoli successivi, quando aggiungeremo campionamento e raccolta dati.

## Server regolare vs server di basso livello

Ecco come appare la creazione di un MCP Server con il server regolare:

**Python**

```python
mcp = FastMCP("Demo")

# Add an addition tool
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b
```

**TypeScript**

```typescript
const server = new McpServer({
  name: "demo-server",
  version: "1.0.0"
});

// Add an addition tool
server.registerTool("add",
  {
    title: "Addition Tool",
    description: "Add two numbers",
    inputSchema: { a: z.number(), b: z.number() }
  },
  async ({ a, b }) => ({
    content: [{ type: "text", text: String(a + b) }]
  })
);
```

Il punto è che si aggiunge esplicitamente ogni strumento, risorsa o prompt che si desidera includere nel server. Non c'è nulla di sbagliato in questo.

### Approccio del server di basso livello

Tuttavia, quando si utilizza l'approccio del server di basso livello, bisogna pensare in modo diverso: invece di registrare ogni strumento, si creano due gestori per tipo di funzionalità (strumenti, risorse o prompt). Ad esempio, per gli strumenti ci sono solo due funzioni, come segue:

- Elencare tutti gli strumenti. Una funzione si occupa di tutte le richieste per elencare gli strumenti.
- Gestire le chiamate agli strumenti. Anche qui, c'è solo una funzione che gestisce le chiamate a uno strumento.

Sembra un lavoro potenzialmente minore, giusto? Quindi, invece di registrare uno strumento, devo solo assicurarmi che lo strumento sia elencato quando elenco tutti gli strumenti e che venga chiamato quando c'è una richiesta in arrivo per utilizzarlo.

Vediamo ora come appare il codice:

**Python**

```python
@server.list_tools()
async def handle_list_tools() -> list[types.Tool]:
    """List available tools."""
    return [
        types.Tool(
            name="add",
            description="Add two numbers",
            inputSchema={
                "type": "object",
                "properties": {
                    "a": {"type": "number", "description": "nubmer to add"}, 
                    "b": {"type": "number", "description": "nubmer to add"}
                },
                "required": ["query"],
            },
        )
    ]
```

**TypeScript**

```typescript
server.setRequestHandler(ListToolsRequestSchema, async (request) => {
  // Return the list of registered tools
  return {
    tools: [{
        name="add",
        description="Add two numbers",
        inputSchema={
            "type": "object",
            "properties": {
                "a": {"type": "number", "description": "nubmer to add"}, 
                "b": {"type": "number", "description": "nubmer to add"}
            },
            "required": ["query"],
        }
    }]
  };
});
```

Qui abbiamo una funzione che restituisce un elenco di funzionalità. Ogni voce nell'elenco degli strumenti ora ha campi come `name`, `description` e `inputSchema` per aderire al tipo di ritorno. Questo ci consente di definire i nostri strumenti e funzionalità altrove. Possiamo ora creare tutti i nostri strumenti in una cartella dedicata e fare lo stesso per tutte le funzionalità, organizzando il progetto in questo modo:

```text
app
--| tools
----| add
----| substract
--| resources
----| products
----| schemas
--| prompts
----| product-description
```

Fantastico, la nostra architettura può essere resa piuttosto pulita.

E per quanto riguarda la chiamata agli strumenti? È lo stesso concetto, un gestore per chiamare uno strumento, qualunque esso sia? Esattamente, ecco il codice per farlo:

**Python**

```python
@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict[str, str] | None
) -> list[types.TextContent]:
    
    # tools is a dictionary with tool names as keys
    if name not in tools.tools:
        raise ValueError(f"Unknown tool: {name}")
    
    tool = tools.tools[name]

    result = "default"
    try:
        result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)
    except Exception as e:
        raise ValueError(f"Error calling tool {name}: {str(e)}")

    return [
        types.TextContent(type="text", text=str(result))
    ] 
```

**TypeScript**

```typescript
server.setRequestHandler(CallToolRequestSchema, async (request) => {
    const { params: { name } } = request;
    let tool = tools.find(t => t.name === name);
    if(!tool) {
        return {
            error: {
                code: "tool_not_found",
                message: `Tool ${name} not found.`
            }
       };
    }
    
    // args: request.params.arguments
    // TODO call the tool, 

    return {
       content: [{ type: "text", text: `Tool ${name} called with arguments: ${JSON.stringify(input)}, result: ${JSON.stringify(result)}` }]
    };
});
```

Come puoi vedere dal codice sopra, dobbiamo analizzare lo strumento da chiamare, con quali argomenti, e poi procedere alla chiamata dello strumento.

## Migliorare l'approccio con la validazione

Finora, hai visto come tutte le registrazioni per aggiungere strumenti, risorse e prompt possono essere sostituite con questi due gestori per tipo di funzionalità. Cos'altro dobbiamo fare? Dovremmo aggiungere una forma di validazione per garantire che lo strumento venga chiamato con gli argomenti corretti. Ogni runtime ha la propria soluzione per questo, ad esempio Python utilizza Pydantic e TypeScript utilizza Zod. L'idea è di fare quanto segue:

- Spostare la logica per creare una funzionalità (strumento, risorsa o prompt) nella sua cartella dedicata.
- Aggiungere un modo per validare una richiesta in arrivo che, ad esempio, chiede di chiamare uno strumento.

### Creare una funzionalità

Per creare una funzionalità, dobbiamo creare un file per quella funzionalità e assicurarci che abbia i campi obbligatori richiesti. I campi differiscono leggermente tra strumenti, risorse e prompt.

**Python**

```python
# schema.py
from pydantic import BaseModel

class AddInputModel(BaseModel):
    a: float
    b: float

# add.py

from .schema import AddInputModel

async def add_handler(args) -> float:
    try:
        # Validate input using Pydantic model
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # TODO: add Pydantic, so we can create an AddInputModel and validate args

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

Qui puoi vedere come facciamo quanto segue:

- Creiamo uno schema utilizzando Pydantic `AddInputModel` con i campi `a` e `b` nel file *schema.py*.
- Tentiamo di analizzare la richiesta in arrivo per essere di tipo `AddInputModel`. Se c'è una discrepanza nei parametri, questo genererà un errore:

   ```python
   # add.py
    try:
        # Validate input using Pydantic model
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")
   ```

Puoi scegliere se mettere questa logica di analisi nella chiamata dello strumento stesso o nella funzione del gestore.

**TypeScript**

```typescript
// server.ts
server.setRequestHandler(CallToolRequestSchema, async (request) => {
    const { params: { name } } = request;
    let tool = tools.find(t => t.name === name);
    if (!tool) {
       return {
        error: {
            code: "tool_not_found",
            message: `Tool ${name} not found.`
        }
       };
    }
    const Schema = tool.rawSchema;

    try {
       const input = Schema.parse(request.params.arguments);

       // @ts-ignore
       const result = await tool.callback(input);

       return {
          content: [{ type: "text", text: `Tool ${name} called with arguments: ${JSON.stringify(input)}, result: ${JSON.stringify(result)}` }]
      };
    } catch (error) {
       return {
          error: {
             code: "invalid_arguments",
             message: `Invalid arguments for tool ${name}: ${error instanceof Error ? error.message : String(error)}`
          }
    };
   }

});

// schema.ts
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });

// add.ts
import { Tool } from "./tool.js";
import { MathInputSchema } from "./schema.js";
import { zodToJsonSchema } from "zod-to-json-schema";

export default {
    name: "add",
    rawSchema: MathInputSchema,
    inputSchema: zodToJsonSchema(MathInputSchema),
    callback: async ({ a, b }) => {
        return {
            content: [{ type: "text", text: String(a + b) }]
        };
    }
} as Tool;
```

- Nel gestore che si occupa di tutte le chiamate agli strumenti, ora cerchiamo di analizzare la richiesta in arrivo nello schema definito dello strumento:

    ```typescript
    const Schema = tool.rawSchema;

    try {
       const input = Schema.parse(request.params.arguments);
    ```

    Se funziona, procediamo a chiamare lo strumento effettivo:

    ```typescript
    const result = await tool.callback(input);
    ```

Come puoi vedere, questo approccio crea un'architettura eccellente, in cui tutto ha il suo posto. Il file *server.ts* è molto piccolo e si occupa solo di collegare i gestori delle richieste, mentre ogni funzionalità si trova nella rispettiva cartella, ad esempio tools/, resources/ o prompts/.

Fantastico, proviamo a costruire questo approccio.

## Esercizio: Creare un server di basso livello

In questo esercizio, faremo quanto segue:

1. Creare un server di basso livello che gestisca l'elenco degli strumenti e le chiamate agli strumenti.
1. Implementare un'architettura su cui poter costruire.
1. Aggiungere la validazione per garantire che le chiamate agli strumenti siano correttamente validate.

### -1- Creare un'architettura

La prima cosa da affrontare è un'architettura che ci aiuti a scalare man mano che aggiungiamo più funzionalità. Ecco come appare:

**Python**

```text
server.py
--| tools
----| __init__.py
----| add.py
----| schema.py
client.py
```

**TypeScript**

```text
server.ts
--| tools
----| add.ts
----| schema.ts
client.ts
```

Ora abbiamo impostato un'architettura che garantisce che possiamo facilmente aggiungere nuovi strumenti in una cartella dedicata. Sentiti libero di seguire questo approccio per aggiungere sottodirectory per risorse e prompt.

### -2- Creare uno strumento

Vediamo ora come creare uno strumento. Prima di tutto, deve essere creato nella sua sottodirectory *tool*, come segue:

**Python**

```python
from .schema import AddInputModel

async def add_handler(args) -> float:
    try:
        # Validate input using Pydantic model
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # TODO: add Pydantic, so we can create an AddInputModel and validate args

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

Qui vediamo come definiamo il nome, la descrizione, uno schema di input utilizzando Pydantic e un gestore che verrà invocato quando questo strumento viene chiamato. Infine, esponiamo `tool_add`, che è un dizionario contenente tutte queste proprietà.

C'è anche *schema.py*, utilizzato per definire lo schema di input utilizzato dal nostro strumento:

```python
from pydantic import BaseModel

class AddInputModel(BaseModel):
    a: float
    b: float
```

Dobbiamo anche popolare *__init__.py* per garantire che la directory degli strumenti venga trattata come un modulo. Inoltre, dobbiamo esporre i moduli al suo interno, come segue:

```python
from .add import tool_add

tools = {
  tool_add["name"] : tool_add
}
```

Possiamo continuare ad aggiungere a questo file man mano che aggiungiamo più strumenti.

**TypeScript**

```typescript
import { Tool } from "./tool.js";
import { MathInputSchema } from "./schema.js";
import { zodToJsonSchema } from "zod-to-json-schema";

export default {
    name: "add",
    rawSchema: MathInputSchema,
    inputSchema: zodToJsonSchema(MathInputSchema),
    callback: async ({ a, b }) => {
        return {
            content: [{ type: "text", text: String(a + b) }]
        };
    }
} as Tool;
```

Qui creiamo un dizionario composto da proprietà:

- name, il nome dello strumento.
- rawSchema, lo schema Zod, utilizzato per validare le richieste in arrivo per chiamare questo strumento.
- inputSchema, lo schema utilizzato dal gestore.
- callback, utilizzato per invocare lo strumento.

C'è anche `Tool`, utilizzato per convertire questo dizionario in un tipo che il gestore del server MCP può accettare, e appare così:

```typescript
import { z } from 'zod';

export interface Tool {
    name: string;
    inputSchema: any;
    rawSchema: z.ZodTypeAny;
    callback: (args: z.infer<z.ZodTypeAny>) => Promise<{ content: { type: string; text: string }[] }>;
}
```

E c'è *schema.ts*, dove archiviamo gli schemi di input per ogni strumento. Al momento contiene solo uno schema, ma man mano che aggiungiamo strumenti possiamo aggiungere più voci:

```typescript
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });
```

Fantastico, procediamo ora a gestire l'elenco dei nostri strumenti.

### -3- Gestire l'elenco degli strumenti

Per gestire l'elenco degli strumenti, dobbiamo configurare un gestore di richieste per questo. Ecco cosa dobbiamo aggiungere al nostro file server:

**Python**

```python
# code omitted for brevity
from tools import tools

@server.list_tools()
async def handle_list_tools() -> list[types.Tool]:
    tool_list = []
    print(tools)

    for tool in tools.values():
        tool_list.append(
            types.Tool(
                name=tool["name"],
                description=tool["description"],
                inputSchema=pydantic_to_json(tool["input_schema"]),
            )
        )
    return tool_list
```

Qui aggiungiamo il decoratore `@server.list_tools` e la funzione implementata `handle_list_tools`. In quest'ultima, dobbiamo produrre un elenco di strumenti. Nota come ogni strumento deve avere un nome, una descrizione e uno schema di input.

**TypeScript**

Per configurare il gestore di richieste per l'elenco degli strumenti, dobbiamo chiamare `setRequestHandler` sul server con uno schema adatto a ciò che stiamo cercando di fare, in questo caso `ListToolsRequestSchema`.

```typescript
// index.ts
import addTool from "./add.js";
import subtractTool from "./subtract.js";
import {server} from "../server.js";
import { Tool } from "./tool.js";

export let tools: Array<Tool> = [];
tools.push(addTool);
tools.push(subtractTool);

// server.ts
// code omitted for brevity
import { tools } from './tools/index.js';

server.setRequestHandler(ListToolsRequestSchema, async (request) => {
  // Return the list of registered tools
  return {
    tools: tools
  };
});
```

Fantastico, ora abbiamo risolto la parte relativa all'elenco degli strumenti. Vediamo ora come possiamo chiamare gli strumenti.

### -4- Gestire la chiamata a uno strumento

Per chiamare uno strumento, dobbiamo configurare un altro gestore di richieste, questa volta focalizzato sulla gestione di una richiesta che specifica quale funzionalità chiamare e con quali argomenti.

**Python**

Utilizziamo il decoratore `@server.call_tool` e lo implementiamo con una funzione come `handle_call_tool`. All'interno di questa funzione, dobbiamo analizzare il nome dello strumento, i suoi argomenti e garantire che gli argomenti siano validi per lo strumento in questione. Possiamo validare gli argomenti in questa funzione o a valle, nello strumento effettivo.

```python
@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict[str, str] | None
) -> list[types.TextContent]:
    
    # tools is a dictionary with tool names as keys
    if name not in tools.tools:
        raise ValueError(f"Unknown tool: {name}")
    
    tool = tools.tools[name]

    result = "default"
    try:
        # invoke the tool
        result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)
    except Exception as e:
        raise ValueError(f"Error calling tool {name}: {str(e)}")

    return [
        types.TextContent(type="text", text=str(result))
    ] 
```

Ecco cosa succede:

- Il nome dello strumento è già presente come parametro di input `name`, così come gli argomenti sotto forma del dizionario `arguments`.

- Lo strumento viene chiamato con `result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)`. La validazione degli argomenti avviene nella proprietà `handler`, che punta a una funzione. Se la validazione fallisce, verrà generata un'eccezione.

Ora abbiamo una comprensione completa di come elencare e chiamare strumenti utilizzando un server di basso livello.

Vedi [l'esempio completo](./code/README.md) qui.

## Compito

Estendi il codice che ti è stato fornito con un certo numero di strumenti, risorse e prompt e rifletti su come noti che devi solo aggiungere file nella directory degli strumenti e da nessun'altra parte.

*Nessuna soluzione fornita*

## Riepilogo

In questo capitolo, abbiamo visto come funziona l'approccio del server di basso livello e come può aiutarci a creare un'architettura ben strutturata su cui continuare a costruire. Abbiamo anche discusso della validazione e ti è stato mostrato come lavorare con librerie di validazione per creare schemi per la validazione degli input.

---

**Clausola di esclusione della responsabilità**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire l'accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa dovrebbe essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un traduttore umano. Non siamo responsabili per eventuali incomprensioni o interpretazioni errate derivanti dall'uso di questa traduzione.