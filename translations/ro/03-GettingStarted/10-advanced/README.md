# Utilizarea avansată a serverului

Există două tipuri diferite de servere expuse în MCP SDK, serverul normal și serverul de nivel jos. De obicei, ai folosi serverul obișnuit pentru a adăuga funcționalități. Totuși, în unele cazuri vrei să te bazezi pe serverul de nivel jos, cum ar fi:

- Arhitectură mai bună. Este posibil să creezi o arhitectură curată atât cu serverul obișnuit, cât și cu un server de nivel jos, dar se poate argumenta că este puțin mai ușor cu un server de nivel jos.
- Disponibilitatea funcționalităților. Unele funcționalități avansate pot fi folosite doar cu un server de nivel jos. Vei vedea asta în capitolele următoare pe măsură ce adăugăm sampling și elicitation.

## Server obișnuit vs server de nivel jos

Iată cum arată crearea unui Server MCP cu serverul obișnuit

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

Ideea este că adaugi explicit fiecare instrument, resursă sau prompt pe care vrei ca serverul să îl aibă. Nu este nimic în neregulă cu asta.  

### Abordarea serverului de nivel jos

Totuși, când folosești abordarea serverului de nivel jos trebuie să gândești diferit. În loc să înregistrezi fiecare instrument, creezi două handler-e per tip de funcționalitate (instrumente, resurse sau prompturi). De exemplu, instrumentele au doar două funcții astfel:

- Listarea tuturor instrumentelor. O funcție răspunde pentru toate încercările de a lista instrumentele.
- Gestionarea apelării tuturor instrumentelor. Aici este doar o funcție care tratează apelurile către un instrument

Sună ca mai puțină muncă, nu? Deci, în loc să înregistrez un instrument, trebuie doar să mă asigur că instrumentul este listat când listez toate instrumentele și că este apelat când există o cerere de apel a unui instrument.

Să vedem cum arată acum codul:

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
  // Returnează lista instrumentelor înregistrate
  return {
    tools: [{
        name: "add",
        description: "Add two numbers",
        inputSchema: {
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

Aici avem o funcție care returnează o listă de funcționalități. Fiecare element din lista de instrumente are acum câmpuri precum `name`, `description` și `inputSchema` pentru a respecta tipul de returnare. Aceasta ne permite să plasăm definițiile instrumentelor și ale funcționalităților în altă parte. Putem crea toate instrumentele noastre într-un folder tools și la fel pentru toate funcționalitățile astfel încât proiectul să poată fi organizat astfel:

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

Este grozav, arhitectura noastră poate arăta foarte curat.

Dar pentru apelarea instrumentelor, este aceeași idee, un handler pentru a apela un instrument, oricare ar fi acela? Da, exact, iată codul pentru asta:

**Python**

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
    // TODO apelează unealta,

    return {
       content: [{ type: "text", text: `Tool ${name} called with arguments: ${JSON.stringify(input)}, result: ${JSON.stringify(result)}` }]
    };
});
```

După cum se vede din codul de mai sus, trebuie să extragem instrumentul de apelat, cu ce argumente și apoi să procedăm la apelarea instrumentului.

## Îmbunătățirea abordării cu validare

Până acum, ai văzut cum toate înregistrările tale pentru a adăuga instrumente, resurse și prompturi pot fi înlocuite cu acești doi handleri per tip de funcționalitate. Ce mai trebuie făcut? Ei bine, ar trebui să adăugăm o formă de validare pentru a ne asigura că instrumentul este apelat cu argumentele corecte. Fiecare runtime are propria soluție pentru asta, de exemplu Python folosește Pydantic și TypeScript folosește Zod. Ideea este să facem următoarele:

- Mutăm logica de creare a unei funcționalități (instrument, resursă sau prompt) în folderul său dedicat.
- Adăugăm o metodă de validare a unei cereri care, de exemplu, solicită apelarea unui instrument.

### Crearea unei funcționalități

Pentru a crea o funcționalitate, trebuie să creezi un fișier pentru acea funcționalitate și să te asiguri că are câmpurile obligatorii necesare. Câmpurile diferă puțin între instrumente, resurse și prompturi.

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
- Încercăm să parsam cererea care vine pentru a fi de tipul `AddInputModel`, dacă există o nepotrivire în parametri, aceasta va genera o eroare:

   ```python
   # add.py
    try:
        # Validează intrarea folosind model Pydantic
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")
   ```

Poți alege să pui această logică de parsing în apelul instrumentului propriu-zis sau în funcția handler.

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

- În handlerul care gestionează toate apelurile instrumentelor, încercăm acum să parsam cererea care vine conform schemei definite a instrumentului:

    ```typescript
    const Schema = tool.rawSchema;

    try {
       const input = Schema.parse(request.params.arguments);
    ```

    dacă asta funcționează atunci continuăm să apelăm instrumentul propriu-zis:

    ```typescript
    const result = await tool.callback(input);
    ```

După cum vezi, această abordare creează o arhitectură foarte bună, căci totul are locul său, *server.ts* este un fișier foarte mic care doar conectează handler-ele pentru cereri iar fiecare funcționalitate este în folderul său respectiv, adică tools/, resources/ sau prompts/.

Perfect, să încercăm să construim asta în continuare.

## Exercițiu: Crearea unui server de nivel jos

În acest exercițiu, vom face următoarele:

1. Creăm un server de nivel jos care gestionează listarea instrumentelor și apelarea instrumentelor.
1. Implementăm o arhitectură pe care poți construi în continuare.
1. Adăugăm validare pentru a ne asigura că apelurile către instrumentele tale sunt validate corespunzător.

### -1- Crearea arhitecturii

Primul lucru pe care trebuie să îl rezolvăm este o arhitectură care să ne ajute să scalăm pe măsură ce adăugăm mai multe funcționalități, iată cum arată:

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

Acum am configurat o arhitectură care asigură că putem adăuga ușor noi instrumente într-un folder tools. Simte-te liber să urmezi acest model pentru a adăuga subdirectoare pentru resources și prompts.

### -2- Crearea unui instrument

Să vedem cum arată crearea unui instrument. Mai întâi, trebuie creat în subdirectorul *tool* astfel:

**Python**

```python
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

Ce vedem aici este cum definim numele, descrierea și schema de intrare folosind Pydantic și un handler care va fi invocat odată ce acest instrument este apelat. În final, expunem `tool_add` care este un dicționar ce conține toate aceste proprietăți.

Mai este și *schema.py* folosit pentru a defini schema de intrare folosită de instrumentul nostru:

```python
from pydantic import BaseModel

class AddInputModel(BaseModel):
    a: float
    b: float
```

De asemenea, trebuie să completăm *__init__.py* pentru a ne asigura că directorul tools este tratat ca modul. În plus, trebuie să expunem modulele din acesta astfel:

```python
from .add import tool_add

tools = {
  tool_add["name"] : tool_add
}
```

Putem continua să adăugăm în acest fișier pe măsură ce adăugăm mai multe instrumente.

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

Aici creăm un dicționar format din proprietăți:

- name, numele instrumentului.
- rawSchema, aceasta este schema Zod care va fi folosită pentru validarea cererilor de apelare a acestui instrument.
- inputSchema, această schemă va fi utilizată de handler.
- callback, folosit pentru a invoca instrumentul.

Mai este și `Tool` folosită pentru a converti acest dicționar într-un tip pe care handler-ul serverului mcp îl poate accepta și arată astfel:

```typescript
import { z } from 'zod';

export interface Tool {
    name: string;
    inputSchema: any;
    rawSchema: z.ZodTypeAny;
    callback: (args: z.infer<z.ZodTypeAny>) => Promise<{ content: { type: string; text: string }[] }>;
}
```

Și există *schema.ts* unde păstrăm schemele de intrare pentru fiecare instrument, arătând astfel cu o singură schemă deocamdată, dar pe măsură ce adăugăm instrumente putem adăuga mai multe intrări:

```typescript
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });
```

Perfect, să continuăm cu gestionarea listării instrumentelor.

### -3- Gestionarea listării instrumentelor

Pentru a gestiona listarea instrumentelor trebuie să configurăm un handler pentru această cerere. Iată ce trebuie să adăugăm în fișierul serverului:

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

Aici adăugăm decoratorul `@server.list_tools` și funcția implementatoare `handle_list_tools`. În aceasta, trebuie să producem o listă de instrumente. Observă că fiecare instrument trebuie să aibă un nume, descriere și inputSchema.   

**TypeScript**

Pentru a configura handler-ul cererii de listare a instrumentelor, trebuie să apelăm `setRequestHandler` pe server cu o schemă care se potrivește cu ceea ce dorim să facem, în acest caz `ListToolsRequestSchema`.

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
  // Returnează lista instrumentelor înregistrate
  return {
    tools: tools
  };
});
```

Perfect, acum am rezolvat partea de listare a instrumentelor, să vedem cum putem apela instrumentele.

### -4- Gestionarea apelării unui instrument

Pentru a apela un instrument, trebuie să configurăm un alt handler pentru cereri, de data asta axat pe tratarea cererii care specifică ce funcționalitate să se apeleze și cu ce argumente.

**Python**

Să folosim decoratorul `@server.call_tool` și să îl implementăm cu o funcție ca `handle_call_tool`. În această funcție trebuie să extragem numele instrumentului, argumentele sale și să ne asigurăm că argumentele sunt valide pentru instrumentul în cauză. Putem valida argumentele fie aici, fie în handler-ul propriuzis al instrumentului.

```python
@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict[str, str] | None
) -> list[types.TextContent]:
    
    # tools este un dicționar cu numele instrumentelor ca și chei
    if name not in tools.tools:
        raise ValueError(f"Unknown tool: {name}")
    
    tool = tools.tools[name]

    result = "default"
    try:
        # apelează instrumentul
        result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)
    except Exception as e:
        raise ValueError(f"Error calling tool {name}: {str(e)}")

    return [
        types.TextContent(type="text", text=str(result))
    ]
```

Iată ce se întâmplă:

- Numele instrumentului este deja prezent ca parametrul de intrare `name` care este adevărat pentru argumentele noastre sub forma dicționarului `arguments`.

- Instrumentul este apelat cu `result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)`. Validarea argumentelor are loc în proprietatea `handler` care indică o funcție, iar dacă aceasta eșuează va arunca o excepție.

Acum avem o înțelegere completă despre listarea și apelarea instrumentelor folosind un server de nivel jos.

Vezi [exemplul complet](./code/README.md) aici

## Tema

Extinde codul oferit cu mai multe instrumente, resurse și prompturi și reflectă asupra faptului că trebuie doar să adaugi fișiere în directorul tools și nicăieri altundeva.

*Nicio soluție oferită*

## Rezumat

În acest capitol, am văzut cum funcționează abordarea serverului de nivel jos și cum aceasta ne poate ajuta să creăm o arhitectură plăcută pe care o putem continua să o construim. Am discutat de asemenea despre validare și ți s-a arătat cum să lucrezi cu biblioteci de validare pentru a crea scheme de validare a inputului.

## Ce urmează

- Următorul: [Autentificare simplă](../11-simple-auth/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Declinare a responsabilității**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională umană. Nu ne asumăm răspunderea pentru orice neînțelegeri sau interpretări greșite rezultate din utilizarea acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->