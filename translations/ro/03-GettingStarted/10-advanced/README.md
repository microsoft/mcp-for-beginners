# Utilizare avansată a serverului

Există două tipuri diferite de servere expuse în MCP SDK: serverul obișnuit și serverul de nivel scăzut. De obicei, folosești serverul obișnuit pentru a adăuga funcționalități. Totuși, în anumite cazuri, este necesar să te bazezi pe serverul de nivel scăzut, cum ar fi:

- **Arhitectură mai bună.** Este posibil să creezi o arhitectură curată atât cu serverul obișnuit, cât și cu serverul de nivel scăzut, dar se poate argumenta că este puțin mai ușor cu serverul de nivel scăzut.
- **Disponibilitatea funcțiilor.** Unele funcționalități avansate pot fi utilizate doar cu un server de nivel scăzut. Vei vedea acest lucru în capitolele următoare, pe măsură ce adăugăm funcții precum sampling și elicitation.

## Server obișnuit vs server de nivel scăzut

Iată cum arată crearea unui MCP Server folosind serverul obișnuit:

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

Ideea este că adaugi explicit fiecare instrument, resursă sau prompt pe care dorești ca serverul să le aibă. Nu este nimic greșit în asta.

### Abordarea serverului de nivel scăzut

Totuși, când folosești abordarea serverului de nivel scăzut, trebuie să gândești diferit, în sensul că, în loc să înregistrezi fiecare instrument, creezi două funcții de gestionare pentru fiecare tip de funcționalitate (instrumente, resurse sau prompturi). De exemplu, pentru instrumente, există doar două funcții, astfel:

- **Listarea tuturor instrumentelor.** O funcție va fi responsabilă pentru toate încercările de a lista instrumentele.
- **Gestionarea apelurilor către instrumente.** Aici, de asemenea, există o singură funcție care gestionează apelurile către un instrument.

Pare mai puțin de lucru, nu-i așa? Deci, în loc să înregistrez un instrument, trebuie doar să mă asigur că instrumentul este listat atunci când listez toate instrumentele și că este apelat atunci când există o cerere de utilizare a unui instrument.

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

Acum avem o funcție care returnează o listă de funcționalități. Fiecare intrare din lista de instrumente are câmpuri precum `name`, `description` și `inputSchema` pentru a respecta tipul de returnare. Acest lucru ne permite să plasăm definițiile instrumentelor și funcționalităților în altă parte. Putem crea toate instrumentele într-un folder dedicat instrumentelor, iar același lucru se aplică pentru toate funcționalitățile, astfel încât proiectul nostru poate fi organizat astfel:

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

Minunat, arhitectura noastră poate fi făcută să arate destul de curată.

Ce se întâmplă cu apelarea instrumentelor? Este aceeași idee, o funcție de gestionare pentru apelarea unui instrument, indiferent de care? Exact, iată codul pentru asta:

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

După cum poți vedea din codul de mai sus, trebuie să analizăm instrumentul care urmează să fie apelat, cu ce argumente, și apoi să procedăm la apelarea instrumentului.

## Îmbunătățirea abordării cu validare

Până acum, ai văzut cum toate înregistrările pentru adăugarea de instrumente, resurse și prompturi pot fi înlocuite cu aceste două funcții de gestionare pentru fiecare tip de funcționalitate. Ce altceva mai trebuie să facem? Ei bine, ar trebui să adăugăm o formă de validare pentru a ne asigura că instrumentul este apelat cu argumentele corecte. Fiecare runtime are propria soluție pentru asta, de exemplu, Python folosește Pydantic, iar TypeScript folosește Zod. Ideea este să facem următoarele:

- Mutăm logica pentru crearea unei funcționalități (instrument, resursă sau prompt) într-un folder dedicat.
- Adăugăm o metodă de validare a unei cereri de intrare, de exemplu, pentru apelarea unui instrument.

### Crearea unei funcționalități

Pentru a crea o funcționalitate, va trebui să creăm un fișier pentru acea funcționalitate și să ne asigurăm că are câmpurile obligatorii necesare. Câmpurile diferă puțin între instrumente, resurse și prompturi.

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

Aici poți vedea cum facem următoarele:

- Creăm un schema folosind Pydantic `AddInputModel` cu câmpurile `a` și `b` în fișierul *schema.py*.
- Încercăm să analizăm cererea de intrare pentru a fi de tip `AddInputModel`. Dacă există o nepotrivire în parametri, acest lucru va genera o eroare:

   ```python
   # add.py
    try:
        # Validate input using Pydantic model
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")
   ```

Poți alege dacă să pui această logică de analizare în apelul instrumentului propriu-zis sau în funcția de gestionare.

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

- În funcția de gestionare care se ocupă de toate apelurile către instrumente, încercăm să analizăm cererea de intrare în schema definită pentru instrument:

    ```typescript
    const Schema = tool.rawSchema;

    try {
       const input = Schema.parse(request.params.arguments);
    ```

    Dacă acest lucru funcționează, atunci procedăm la apelarea instrumentului propriu-zis:

    ```typescript
    const result = await tool.callback(input);
    ```

După cum poți vedea, această abordare creează o arhitectură excelentă, deoarece totul are locul său. Fișierul *server.ts* este foarte mic și doar configurează funcțiile de gestionare a cererilor, iar fiecare funcționalitate se află în folderul său respectiv, adică tools/, resources/ sau prompts/.

Minunat, să încercăm să construim acest lucru în continuare.

## Exercițiu: Crearea unui server de nivel scăzut

În acest exercițiu, vom face următoarele:

1. Creăm un server de nivel scăzut care gestionează listarea instrumentelor și apelarea instrumentelor.
1. Implementăm o arhitectură pe care o putem dezvolta.
1. Adăugăm validare pentru a ne asigura că apelurile către instrumente sunt validate corect.

### -1- Crearea unei arhitecturi

Primul lucru pe care trebuie să-l abordăm este o arhitectură care ne ajută să scalăm pe măsură ce adăugăm mai multe funcționalități. Iată cum arată:

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

Acum am configurat o arhitectură care ne asigură că putem adăuga cu ușurință noi instrumente într-un folder dedicat instrumentelor. Poți urma acest model pentru a adăuga subdirectoare pentru resurse și prompturi.

### -2- Crearea unui instrument

Să vedem cum arată crearea unui instrument. Mai întâi, trebuie să fie creat în subdirectorul *tool*, astfel:

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

Aici vedem cum definim numele, descrierea, un schema de intrare folosind Pydantic și o funcție de gestionare care va fi invocată atunci când acest instrument este apelat. În final, expunem `tool_add`, care este un dicționar ce conține toate aceste proprietăți.

Există, de asemenea, *schema.py*, care este folosit pentru a defini schema de intrare utilizată de instrumentul nostru:

```python
from pydantic import BaseModel

class AddInputModel(BaseModel):
    a: float
    b: float
```

De asemenea, trebuie să populăm *__init__.py* pentru a ne asigura că directorul instrumentelor este tratat ca un modul. În plus, trebuie să expunem modulele din interiorul acestuia astfel:

```python
from .add import tool_add

tools = {
  tool_add["name"] : tool_add
}
```

Putem continua să adăugăm la acest fișier pe măsură ce adăugăm mai multe instrumente.

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

Aici creăm un dicționar care constă din proprietăți:

- **name**, acesta este numele instrumentului.
- **rawSchema**, acesta este schema Zod, care va fi utilizată pentru a valida cererile de intrare.
- **inputSchema**, această schema va fi utilizată de funcția de gestionare.
- **callback**, aceasta este utilizată pentru a invoca instrumentul.

Există, de asemenea, `Tool`, care este utilizat pentru a converti acest dicționar într-un tip pe care handler-ul serverului MCP îl poate accepta și arată astfel:

```typescript
import { z } from 'zod';

export interface Tool {
    name: string;
    inputSchema: any;
    rawSchema: z.ZodTypeAny;
    callback: (args: z.infer<z.ZodTypeAny>) => Promise<{ content: { type: string; text: string }[] }>;
}
```

Și există *schema.ts*, unde stocăm schemele de intrare pentru fiecare instrument, care arată astfel, având doar o schema în prezent, dar pe măsură ce adăugăm instrumente, putem adăuga mai multe intrări:

```typescript
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });
```

Minunat, să trecem la gestionarea listării instrumentelor.

### -3- Gestionarea listării instrumentelor

Pentru a gestiona listarea instrumentelor, trebuie să configurăm o funcție de gestionare a cererilor pentru asta. Iată ce trebuie să adăugăm în fișierul serverului:

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

Aici adăugăm decoratorul `@server.list_tools` și funcția implementată `handle_list_tools`. În aceasta, trebuie să producem o listă de instrumente. Observă cum fiecare instrument trebuie să aibă un nume, o descriere și un inputSchema.

**TypeScript**

Pentru a configura funcția de gestionare a cererilor pentru listarea instrumentelor, trebuie să apelăm `setRequestHandler` pe server cu o schema potrivită pentru ceea ce încercăm să facem, în acest caz `ListToolsRequestSchema`.

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

Minunat, acum am rezolvat partea de listare a instrumentelor. Să vedem cum putem apela instrumentele în continuare.

### -4- Gestionarea apelării unui instrument

Pentru a apela un instrument, trebuie să configurăm o altă funcție de gestionare a cererilor, de data aceasta concentrată pe gestionarea unei cereri care specifică ce funcționalitate să fie apelată și cu ce argumente.

**Python**

Să folosim decoratorul `@server.call_tool` și să-l implementăm cu o funcție precum `handle_call_tool`. În cadrul acestei funcții, trebuie să analizăm numele instrumentului, argumentele sale și să ne asigurăm că argumentele sunt valide pentru instrumentul în cauză. Putem valida argumentele fie în această funcție, fie în funcționalitatea propriu-zisă.

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

Iată ce se întâmplă:

- Numele instrumentului este deja prezent ca parametru de intrare `name`, ceea ce este valabil și pentru argumentele sub formă de dicționar `arguments`.

- Instrumentul este apelat cu `result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)`. Validarea argumentelor are loc în proprietatea `handler`, care indică o funcție. Dacă aceasta eșuează, va genera o excepție.

Acum avem o înțelegere completă a modului de listare și apelare a instrumentelor folosind un server de nivel scăzut.

Vezi [exemplul complet](./code/README.md) aici.

## Temă

Extinde codul pe care l-ai primit cu un număr de instrumente, resurse și prompturi și reflectă asupra modului în care observi că trebuie doar să adaugi fișiere în directorul instrumentelor și nicăieri altundeva.

*Nu se oferă soluție*

## Rezumat

În acest capitol, am văzut cum funcționează abordarea serverului de nivel scăzut și cum aceasta ne poate ajuta să creăm o arhitectură bine organizată pe care să o putem dezvolta în continuare. De asemenea, am discutat despre validare și ți s-a arătat cum să lucrezi cu biblioteci de validare pentru a crea scheme pentru validarea intrărilor.

---

**Declinare de responsabilitate**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim să asigurăm acuratețea, vă rugăm să fiți conștienți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa maternă ar trebui considerat sursa autoritară. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist uman. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care pot apărea din utilizarea acestei traduceri.