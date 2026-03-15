# Utilizarea avansată a serverului

Există două tipuri diferite de servere expuse în MCP SDK, serverul normal și serverul de nivel jos. De obicei, ai folosi serverul obișnuit pentru a adăuga funcționalități. Totuși, în unele cazuri, vrei să te bazezi pe serverul de nivel jos, cum ar fi:

- Arhitectură mai bună. Este posibil să creezi o arhitectură curată atât cu serverul obișnuit, cât și cu serverul de nivel jos, dar se poate argumenta că este puțin mai ușor cu un server de nivel jos.
- Disponibilitatea funcționalităților. Unele funcționalități avansate pot fi folosite doar cu un server de nivel jos. Vei vedea asta în capitolele următoare când adăugăm sampling și elicitation.

## Server obișnuit vs server de nivel jos

Iată cum arată crearea unui MCP Server cu serverul obișnuit

**Python**

```python
mcp = FastMCP("Demo")

# Adaugă un instrument de adunare
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

// Adaugă un instrument de adunare
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

Ideea este că adaugi în mod explicit fiecare unelte, resursă sau prompt pe care vrei să îl aibă serverul. Nu este nimic rău în asta.

### Abordarea serverului de nivel jos

Totuși, când folosești abordarea serverului de nivel jos, trebuie să gândești diferit. În loc să înregistrezi fiecare unealtă, creezi două handler-e pe tipuri de funcționalități (unelte, resurse sau prompturi). De exemplu, uneltele au doar două funcții astfel:

- Listarea tuturor uneltelor. O funcție este responsabilă pentru toate încercările de a lista uneltele.
- Gestionarea apelării tuturor uneltelor. De asemenea, aici există o singură funcție care gestionează apelurile către o unealtă.

Asta sună ca o muncă potențial mai mică, nu? Deci în loc să înregistrez o unealtă, trebuie doar să mă asigur că unealta apare când listez toate uneltele și că este apelată când vine o cerere pentru apelarea unei unelte.

Hai să vedem cum arată acum codul:

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
                    "a": {"type": "number", "description": "number to add"}, 
                    "b": {"type": "number", "description": "number to add"}
                },
                "required": ["query"],
            },
        )
    ]
```

**TypeScript**

```typescript
server.setRequestHandler(ListToolsRequestSchema, async (request) => {
  // Returnează lista de unelte înregistrate
  return {
    tools: [{
        name="add",
        description="Add two numbers",
        inputSchema={
            "type": "object",
            "properties": {
                "a": {"type": "number", "description": "number to add"}, 
                "b": {"type": "number", "description": "number to add"}
            },
            "required": ["query"],
        }
    }]
  };
});
```

Aici avem acum o funcție care returnează o listă de funcționalități. Fiecare intrare din lista de unelte are acum câmpuri precum `name`, `description` și `inputSchema` pentru a respecta tipul de returnare. Aceasta ne permite să punem uneltele și definiția funcționalităților în altă parte. Acum putem crea toate uneltele într-un folder tools și la fel pentru toate funcționalitățile, astfel proiectul tău poate fi organizat astfel:

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

Foarte bine, arhitectura noastră poate arăta destul de curat.

Dar ce facem cu apelarea uneltelor, este aceeași idee, un singur handler pentru a apela o unealtă, oricare unealtă? Da, exact, iată codul pentru asta:

**Python**

```python
@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict[str, str] | None
) -> list[types.TextContent]:
    
    # tools este un dicționar cu numele uneltelor ca și chei
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
    
    // argumente: request.params.arguments
    // TODO apelează instrumentul,

    return {
       content: [{ type: "text", text: `Tool ${name} called with arguments: ${JSON.stringify(input)}, result: ${JSON.stringify(result)}` }]
    };
});
```

După cum vezi din codul de mai sus, trebuie să preluăm unealta care trebuie apelată și cu ce argumente, apoi să apelăm efectiv unealta.

## Îmbunătățirea abordării cu validare

Până acum, ai văzut cum toate înregistrările tale pentru a adăuga unelte, resurse și prompturi pot fi înlocuite cu acești doi handleri pe tip de funcționalitate. Ce mai trebuie să facem? Ei bine, ar trebui să adăugăm o formă de validare pentru a ne asigura că unealta este apelată cu argumentele corecte. Fiecare runtime are soluția sa pentru asta, de exemplu Python folosește Pydantic și TypeScript folosește Zod. Ideea este să facem următoarele:

- Mutăm logica pentru crearea unei funcționalități (unealtă, resursă sau prompt) în folderul dedicat.
- Adăugăm o metodă pentru validarea unei cereri primite care de exemplu cere apelarea unei unelte.

### Crearea unei funcționalități

Pentru a crea o funcționalitate, trebuie să creăm un fișier pentru acea funcționalitate și să ne asigurăm că are câmpurile obligatorii cerute pentru acea funcționalitate. Câmpurile diferă puțin între unelte, resurse și prompturi.

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
        # Validează intrarea folosind modelul Pydantic
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # TODO: adaugă Pydantic, astfel încât să putem crea un AddInputModel și să validăm argumentele

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

aici poți vedea cum facem următoarele:

- Creăm un schema folosind Pydantic `AddInputModel` cu câmpurile `a` și `b` în fișierul *schema.py*.
- Încercăm să parsam cererea primită ca fiind de tipul `AddInputModel`, dacă există o nepotrivire la parametri, aceasta va da eroare:

   ```python
   # add.py
    try:
        # Validează input-ul folosind modelul Pydantic
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")
   ```

Poți alege să pui această logică de parsing chiar în apelul uneltei sau în funcția handler.

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

- În handler-ul care gestionează toate apelurile uneltelor, acum încercăm să parsam cererea primită în schema definită de unealtă:

    ```typescript
    const Schema = tool.rawSchema;

    try {
       const input = Schema.parse(request.params.arguments);
    ```

    dacă reușim atunci continuăm cu apelul efectiv al uneltei:

    ```typescript
    const result = await tool.callback(input);
    ```

După cum vezi, această abordare creează o arhitectură bună deoarece totul are locul său, *server.ts* este un fișier foarte mic care doar leagă handler-ele cererilor iar fiecare funcționalitate este în folderul său respectiv adică tools/, resources/ sau /prompts.

Foarte bine, hai să încercăm să construim asta mai departe.

## Exercițiu: Crearea unui server de nivel jos

În acest exercițiu, vom face următoarele:

1. Crearea unui server de nivel jos care gestionează listarea uneltelor și apelarea uneltelor.
1. Implementarea unei arhitecturi pe care să poți construi mai departe.
1. Adăugarea validării pentru a te asigura că apelurile către uneltele tale sunt validate adecvat.

### -1- Crearea unei arhitecturi

Primul lucru pe care trebuie să îl abordăm este o arhitectură care să ne ajute să scalăm pe măsură ce adăugăm mai multe funcționalități, iată cum arată:

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

Acum am stabilit o arhitectură care ne asigură că putem adăuga ușor unelte noi într-un folder tools. Poți adăuga și subfoldere pentru resurse și prompturi.

### -2- Crearea unei unelte

Să vedem cum arată crearea unei unelte. Mai întâi, trebuie creată în subdirectorul său *tool* astfel:

**Python**

```python
from .schema import AddInputModel

async def add_handler(args) -> float:
    try:
        # Validează inputul folosind modelul Pydantic
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # TODO: adaugă Pydantic, astfel încât să putem crea un AddInputModel și să validăm argumentele

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

Ce vedem aici este definirea numelui, descrierii și a schemei de input folosind Pydantic și un handler care va fi apelat odată ce unealta este utilizată. În cele din urmă, expunem `tool_add` care este un dicționar ce conține toate aceste proprietăți.

Există și *schema.py* folosit pentru a defini schema de input folosită de unealta noastră:

```python
from pydantic import BaseModel

class AddInputModel(BaseModel):
    a: float
    b: float
```

De asemenea, trebuie să populăm *__init__.py* pentru a ne asigura că directorul tools este tratat ca un modul. În plus, trebuie să expunem modulele din el astfel:

```python
from .add import tool_add

tools = {
  tool_add["name"] : tool_add
}
```

Putem continua să adăugăm aici pe măsură ce adăugăm mai multe unelte.

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

Aici creăm un dicționar ce constă în proprietăți:

- name, acesta este numele uneltei.
- rawSchema, aceasta este schema Zod, va fi folosită pentru validarea cererilor care vin pentru apelarea acestei unelte.
- inputSchema, această schemă va fi folosită de handler.
- callback, aceasta este folosită pentru a invoca unealta.

Există și `Tool` folosit pentru a converti acest dicționar într-un tip pe care handler-ul serverului MCP îl poate accepta și arată astfel:

```typescript
import { z } from 'zod';

export interface Tool {
    name: string;
    inputSchema: any;
    rawSchema: z.ZodTypeAny;
    callback: (args: z.infer<z.ZodTypeAny>) => Promise<{ content: { type: string; text: string }[] }>;
}
```

Și există *schema.ts* unde stocăm schemele de input pentru fiecare unealtă care arată astfel, având momentan o singură schemă, dar pe măsură ce adăugăm unelte putem adăuga mai multe intrări:

```typescript
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });
```

Perfect, să continuăm cu gestionarea listării uneltelor.

### -3- Gestionarea listării uneltelor

Pentru a gestiona listarea uneltelor, trebuie să configurăm un handler de cereri pentru asta. Iată ce trebuie să adăugăm în fișierul server:

**Python**

```python
# cod omis pentru concizie
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

Aici adăugăm decoratorul `@server.list_tools` și funcția implementată `handle_list_tools`. În aceasta trebuie să producem o listă de unelte. Observă cum fiecare unealtă trebuie să aibă un nume, o descriere și un inputSchema.

**TypeScript**

Pentru a configura handler-ul de cereri pentru listarea uneltelor, trebuie să apelăm `setRequestHandler` pe server cu o schemă care se potrivește cu ceea ce încercăm să facem, în acest caz `ListToolsRequestSchema`.

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
// cod omis pentru concizie
import { tools } from './tools/index.js';

server.setRequestHandler(ListToolsRequestSchema, async (request) => {
  // Returnează lista uneltelor înregistrate
  return {
    tools: tools
  };
});
```

Perfect, acum am rezolvat partea de listare a uneltelor, hai să vedem cum putem apela uneltele.

### -4- Gestionarea apelării unei unelte

Pentru a apela o unealtă, trebuie să configurăm un alt handler de cereri, de data aceasta concentrat pe gestionarea unei cereri care specifică ce funcționalitate să fie apelată și cu ce argumente.

**Python**

Să folosim decoratorul `@server.call_tool` și să îl implementăm cu o funcție precum `handle_call_tool`. În această funcție trebuie să extragem numele uneltei, argumentul său și să ne asigurăm că argumentele sunt valide pentru unealta în cauză. Putem valida argumentele în această funcție sau mai jos în unealta efectivă.

```python
@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict[str, str] | None
) -> list[types.TextContent]:
    
    # tools este un dicționar cu numele uneltelor ca chei
    if name not in tools.tools:
        raise ValueError(f"Unknown tool: {name}")
    
    tool = tools.tools[name]

    result = "default"
    try:
        # apelează unealta
        result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)
    except Exception as e:
        raise ValueError(f"Error calling tool {name}: {str(e)}")

    return [
        types.TextContent(type="text", text=str(result))
    ] 
```

Iată ce se întâmplă:

- Numele uneltei este deja prezent ca parametru de input `name`, la fel și argumentele în forma dicționarului `arguments`.

- Unealta este apelată cu `result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)`. Validarea argumentelor are loc în proprietatea `handler` care indică o funcție; dacă validarea eșuează va ridica o excepție.

Iată, acum avem o înțelegere completă a listării și apelării uneltelor folosind un server de nivel jos.

Vezi [exemplul complet](./code/README.md) aici

## Tema

Extinde codul primit cu mai multe unelte, resurse și prompturi și reflectă asupra faptului că observi că trebuie să adaugi fișiere doar în directorul tools și nicăieri altundeva.

*Nicio soluție oferită*

## Rezumat

În acest capitol am văzut cum funcționează abordarea serverului de nivel jos și cum ne poate ajuta să creăm o arhitectură frumoasă pe care putem continua să construim. Am discutat și despre validare și ți s-a arătat cum să lucrezi cu biblioteci de validare pentru a crea scheme de validare a inputurilor.

## Ce urmează

- Următorul: [Autentificare simplă](../11-simple-auth/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Declinare a responsabilității**:
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa oficială. Pentru informații critice, se recomandă utilizarea unei traduceri profesionale realizate de un traducător uman. Nu ne asumăm responsabilitatea pentru neînțelegeri sau interpretări greșite rezultate din utilizarea acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->