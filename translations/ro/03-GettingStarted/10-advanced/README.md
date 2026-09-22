# Utilizarea avansată a serverului

Există două tipuri diferite de servere expuse în MCP SDK, serverul normal și serverul de nivel jos. În mod normal, ai folosi serverul obișnuit pentru a-i adăuga funcționalități. Totuși, în unele cazuri, vrei să te bazezi pe serverul de nivel jos, cum ar fi:

- O arhitectură mai bună. Este posibil să creezi o arhitectură curată atât cu serverul obișnuit, cât și cu un server de nivel jos, dar se poate argumenta că este puțin mai ușor cu un server de nivel jos.
- Disponibilitatea funcționalităților. Unele funcționalități avansate pot fi folosite doar cu un
    server de nivel jos. Capitolele următoare acoperă funcționalitatea de Elicitație și legacy Sampling,
    care este învechită în MCP `2026-07-28`.

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

Ideea este că adaugi în mod explicit fiecare unealtă, resursă sau prompt pe care vrei ca serverul să le aibă. Nu este nimic greșit în asta.  

### Abordarea serverului de nivel jos

Totuși, când folosești abordarea serverului de nivel jos trebuie să te gândești diferit. În loc să înregistrezi fiecare unealtă, creezi în schimb doi handleri pentru fiecare tip de funcționalitate (unelte, resurse sau prompturi). Așadar, de exemplu, uneltele vor avea doar două funcții astfel:

- Listarea tuturor uneltelor. O funcție ar fi responsabilă de toate încercările de listare a uneltelor.
- gestionarea apelării tuturor uneltelor. Aici, de asemenea, există doar o funcție care gestionează apelurile către o unealtă

Sună ca și cum ar fi mai puțină muncă, nu? Deci în loc să înregistrez o unealtă, trebuie doar să mă asigur că aceasta este listată când listez toate uneltele și că este apelată când vine o solicitare de apelare a unui instrument.

Să aruncăm o privire cum arată acum codul:

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
  // Returnează lista uneltelor înregistrate
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

Acum avem o funcție care returnează o listă de funcționalități. Fiecare intrare din lista de unelte are acum câmpuri precum `name`, `description` și `inputSchema` pentru a respecta tipul de returnare. Aceasta ne permite să punem uneltele și definiția funcționalității în altă parte. Putem acum să creăm toate uneltele în un folder tools și același lucru se aplică pentru toate funcționalitățile astfel încât proiectul tău să poată fi organizat astfel:

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

Este grozav, arhitectura noastră poate arăta destul de curată.

Dar cum rămâne cu apelarea uneltelor, este aceeași idee, un handler pentru a apela orice unealtă? Da, exact, iată codul pentru asta:

**Python**

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
    // TODO apelează instrumentul,

    return {
       content: [{ type: "text", text: `Tool ${name} called with arguments: ${JSON.stringify(input)}, result: ${JSON.stringify(result)}` }]
    };
});
```

După cum vezi din codul de mai sus, trebuie să analizăm ce unealtă trebuie apelată și cu ce argumente, apoi trebuie să continuăm cu apelarea uneltei.

## Îmbunătățirea abordării cu validare

Până acum, ai văzut cum toate înregistrările tale pentru a adăuga unelte, resurse și prompturi pot fi înlocuite cu acești doi handleri per tip de funcționalitate. Ce altceva trebuie să facem? Ar trebui să adăugăm o formă de validare pentru a ne asigura că unealta este apelată cu argumentele corecte. Fiecare runtime are propria soluție pentru asta, de exemplu Python folosește Pydantic iar TypeScript folosește Zod. Ideea este să facem următoarele:

- Mutăm logica pentru crearea unei funcționalități (unealtă, resursă sau prompt) în folderul său dedicat.
- Adăugăm o modalitate de a valida o cerere de intrare care, de exemplu, cere să se apeleze o unealtă.

### Crearea unei funcționalități

Pentru a crea o funcționalitate, va trebui să creăm un fișier pentru acea funcționalitate și să ne asigurăm că are câmpurile obligatorii necesare acelei funcționalități. Care câmpuri diferă puțin între unelte, resurse și prompturi.

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

Aici poți vedea cum facem următoarele:

- Creăm un schemă folosind Pydantic `AddInputModel` cu câmpurile `a` și `b` în fișierul *schema.py*.
- Încercăm să analizăm cererea de intrare să fie de tip `AddInputModel`, dacă există o nepotrivire în parametri, aceasta va cauza o eroare:

   ```python
   # add.py
    try:
        # Validează intrarea folosind modelul Pydantic
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")
   ```

Poți alege să pui această logică de analiză în apelul uneltei propriu-zis sau în funcția handler.

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

- În handler-ul care se ocupă de toate apelurile uneltelor, încercăm acum să analizăm cererea de intrare în schema definită pentru unealtă:

    ```typescript
    const Schema = tool.rawSchema;

    try {
       const input = Schema.parse(request.params.arguments);
    ```

    dacă asta funcționează, atunci continuăm să apelăm unealta:

    ```typescript
    const result = await tool.callback(input);
    ```

După cum vezi, această abordare creează o arhitectură grozavă deoarece totul are locul său, *server.ts* este un fișier foarte mic care doar conectează handlerii cererilor și fiecare funcționalitate este în folderul ei respectiv, adică tools/, resources/ sau /prompts.

Grozav, să încercăm să construim asta în continuare.

## Exercițiu: Crearea unui server de nivel jos

În acest exercițiu vom face următoarele:

1. Crearea unui server de nivel jos care gestionează listarea uneltelor și apelarea uneltelor.
1. Implementarea unei arhitecturi pe care o poți dezvolta.
1. Adăugarea validării pentru a te asigura că apelurile uneltelor sunt corect validate.

### -1- Crearea arhitecturii

Primul lucru pe care trebuie să-l abordăm este o arhitectură care să ne ajute să escalăm pe măsură ce adăugăm mai multe funcționalități, iată cum arată:

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

Acum am configurat o arhitectură care ne asigură că putem adăuga cu ușurință unelte noi în folderul tools. Poți să urmezi asta pentru a adăuga subdirectoare pentru resources și prompts.

### -2- Crearea unei unelte

Să vedem cum arată crearea unei unelte. Mai întâi trebuie creată în subdirectorul său *tool* astfel:

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

Ce vedem aici este cum definim numele, descrierea și schema de intrare folosind Pydantic și un handler care va fi apelat când această unealtă este folosită. În cele din urmă, expunem `tool_add` care este un dicționar ce conține toate aceste proprietăți.

Există și *schema.py* care este folosit pentru a defini schema de intrare folosită de unealta noastră:

```python
from pydantic import BaseModel

class AddInputModel(BaseModel):
    a: float
    b: float
```

De asemenea, trebuie să populăm *__init__.py* pentru a asigura că directorul tools este tratat ca un modul. În plus, trebuie să expunem modulele din interior, astfel:

```python
from .add import tool_add

tools = {
  tool_add["name"] : tool_add
}
```

Putem continua să adăugăm în acest fișier pe măsură ce adăugăm mai multe unelte.

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

Aici creăm un dicționar ce conține proprietățile:

- name, acesta este numele uneltei.
- rawSchema, aceasta este schema Zod, va fi folosită pentru validarea cererilor de intrare pentru apelarea acestei unelte.
- inputSchema, această schemă va fi folosită de handler.
- callback, este folosit pentru a apela unealta.

Există și `Tool` care este folosit pentru a converti acest dicționar într-un tip pe care handlerul serverului MCP îl poate accepta și arată astfel:

```typescript
import { z } from 'zod';

export interface Tool {
    name: string;
    inputSchema: any;
    rawSchema: z.ZodTypeAny;
    callback: (args: z.infer<z.ZodTypeAny>) => Promise<{ content: { type: string; text: string }[] }>;
}
```

Și este și *schema.ts* unde stocăm schemele de intrare pentru fiecare unealtă, care arată astfel, având momentan o singură schemă, dar pe măsură ce adăugăm unelte putem adăuga mai multe intrări:

```typescript
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });
```

Grozav, să continuăm acum cu gestionarea listării uneltelor.

### -3- Gestionarea listării uneltelor

Mai departe, pentru a gestiona listarea uneltelor, trebuie să configurăm un handler de cerere pentru asta. Iată ce trebuie să adăugăm în fișierul serverului:

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

Aici adăugăm decoratorul `@server.list_tools` și funcția de implementare `handle_list_tools`. În aceasta, trebuie să producem o listă de unelte. Observă cum fiecare unealtă trebuie să aibă un nume, o descriere și un inputSchema.   

**TypeScript**

Pentru a configura handlerul cererii pentru listarea uneltelor, trebuie să apelăm `setRequestHandler` pe server cu o schemă potrivită pentru ceea ce dorim să facem, în acest caz `ListToolsRequestSchema`. 

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

Grozav, acum am rezolvat partea de listare a uneltelor, să vedem cum am putea apela uneltele.

### -4- Gestionarea apelării unei unelte

Pentru a apela o unealtă, trebuie să configurăm încă un handler de cerere, de data aceasta pentru a gestiona o cerere care specifică ce funcționalitate să fie apelată și cu ce argumente.

**Python**

Să folosim decoratorul `@server.call_tool` și să-l implementăm cu o funcție cum este `handle_call_tool`. În acea funcție trebuie să analizăm numele uneltei, argumentul său și să ne asigurăm că argumentele sunt valide pentru unealta în cauză. Putem valida argumentele în această funcție sau ulterior în unealta propriu-zisă.

```python
@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict[str, str] | None
) -> list[types.TextContent]:
    
    # tools este un dicționar cu numele instrumentelor ca chei
    if name not in tools.tools:
        raise ValueError(f"Unknown tool: {name}")
    
    tool = tools.tools[name]

    result = "default"
    try:
        # invocă instrumentul
        result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)
    except Exception as e:
        raise ValueError(f"Error calling tool {name}: {str(e)}")

    return [
        types.TextContent(type="text", text=str(result))
    ]
```

Iată ce se întâmplă:

- Numele uneltei este deja prezent ca parametru de intrare `name`, ceea ce este adevărat și pentru argumentele noastre sub forma dicționarului `arguments`.

- Unealta este apelată cu `result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)`. Validarea argumentelor are loc în proprietatea `handler` care indică o funcție, dacă aceasta eșuează va ridica o excepție. 

Așadar, acum avem o înțelegere completă despre listarea și apelarea uneltelor folosind un server de nivel jos.

Vezi [exemplul complet](./code/README.md) aici

## Tema

Extinde codul primit cu un număr de unelte, resurse și prompturi și reflectează cum observi că trebuie doar să adaugi fișiere în directorul tools și nicăieri altundeva.

*Nicio soluție furnizată*

## Rezumat

În acest capitol, am văzut cum funcționează abordarea serverului de nivel jos și cum aceasta ne poate ajuta să creăm o arhitectură plăcută pe care să o putem dezvolta în continuare. Am discutat și validarea, iar ție ți s-a arătat cum să folosești biblioteci de validare pentru a crea scheme pentru validarea intrărilor.

## Ce urmează

- Următorul: [Autentificare simplă](../11-simple-auth/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Declinare a responsabilității**:
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). În timp ce ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un om. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care decurg din utilizarea acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->