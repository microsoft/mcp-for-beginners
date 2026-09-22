# Zaawansowane użycie serwera

W SDK MCP udostępnione są dwa różne typy serwerów: standardowy serwer oraz serwer niskiego poziomu. Zazwyczaj korzysta się ze standardowego serwera, aby dodawać do niego funkcje. Jednak w niektórych przypadkach chcemy polegać na serwerze niskiego poziomu, na przykład:

- Lepsza architektura. Możliwe jest stworzenie czystej architektury zarówno z użyciem standardowego serwera, jak i serwera niskiego poziomu, ale można argumentować, że jest to nieco łatwiejsze przy serwerze niskiego poziomu.
- Dostępność funkcji. Niektóre zaawansowane funkcje można wykorzystać tylko z
    serwerem niskiego poziomu. Późniejsze rozdziały opisują Elicytację oraz przestarzałą funkcję Sampling,
    która została wycofana w MCP `2026-07-28`.

## Standardowy serwer kontra serwer niskiego poziomu

Tak wygląda tworzenie serwera MCP ze standardowym serwerem

**Python**

```python
mcp = FastMCP("Demo")

# Dodaj narzędzie do dodawania
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

// Dodaj narzędzie do dodawania
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

Chodzi o to, że explicite dodajesz każde narzędzie, zasób lub prompt, które chcesz mieć na serwerze. Nie ma w tym nic złego.  

### Podejście serwera niskiego poziomu

Jednak korzystając z podejścia serwera niskiego poziomu, musisz myśleć inaczej. Zamiast rejestrować każde narzędzie, tworzysz dwie funkcje obsługi na typ funkcji (narzędzia, zasoby lub prompt). Na przykład narzędzia mają wtedy tylko dwie funkcje:

- Listowanie wszystkich narzędzi. Jedna funkcja odpowiada za wszystkie próby listowania narzędzi.
- obsługa wywołania wszystkich narzędzi. Tutaj również istnieje tylko jedna funkcja obsługująca wywołania narzędzi

Brzmi to na potencjalnie mniej pracy, prawda? Zamiast rejestrować narzędzie, wystarczy upewnić się, że narzędzie jest uwzględnione podczas listowania wszystkich narzędzi oraz że jest wywoływane, gdy nadchodzi żądanie wywołania narzędzia. 

Spójrzmy teraz, jak wygląda kod:

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
  // Zwróć listę zarejestrowanych narzędzi
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

Tu mamy funkcję zwracającą listę funkcji. Każdy wpis na liście narzędzi ma teraz pola takie jak `name`, `description` i `inputSchema`, aby spełnić typ zwracany. To pozwala umieścić definicję narzędzi i funkcji gdzie indziej. Możemy teraz tworzyć wszystkie nasze narzędzia w folderze tools, i to samo dotyczy wszystkich funkcji, więc Twój projekt nagle może wyglądać tak:

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

To świetnie, nasza architektura może być bardzo czysta.

A co z wywoływaniem narzędzi, czy idea jest ta sama, jedna funkcja do wywołania dowolnego narzędzia? Tak, dokładnie, oto kod tego:

**Python**

```python
@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict[str, str] | None
) -> list[types.TextContent]:
    
    # tools to słownik z nazwami narzędzi jako kluczami
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
    // TODO wywołać narzędzie,

    return {
       content: [{ type: "text", text: `Tool ${name} called with arguments: ${JSON.stringify(input)}, result: ${JSON.stringify(result)}` }]
    };
});
```

Jak widać z powyższego kodu, musimy wyodrębnić narzędzie do wywołania oraz jego argumenty, a następnie wywołać to narzędzie.

## Ulepszanie podejścia walidacją

Jak dotąd widziałeś, jak wszystkie twoje rejestracje do dodania narzędzi, zasobów i promptów można zastąpić tymi dwoma funkcjami obsługi na typ funkcji. Co dalej? Powinniśmy dodać jakąś formę walidacji, żeby upewnić się, że narzędzie jest wywoływane z właściwymi argumentami. Każde środowisko wykonawcze ma na to własne rozwiązanie, np. Python używa Pydantic, a TypeScript używa Zod. Idea polega na tym, aby zrobić następujące:

- Przenieść logikę tworzenia funkcji (narzędzie, zasób lub prompt) do jej dedykowanego folderu.
- Dodać sposób walidacji przychodzącego żądania proszącego np. o wywołanie narzędzia.

### Tworzenie funkcji

Aby utworzyć funkcję, musimy stworzyć plik dla tej funkcji i upewnić się, że ma obowiązkowe pola wymagane dla tej funkcji. Te pola różnią się nieco między narzędziami, zasobami i promptami.

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
        # Waliduj dane wejściowe za pomocą modelu Pydantic
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # TODO: dodaj Pydantic, abyśmy mogli stworzyć AddInputModel i zwalidować argumenty

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

tutaj widać, jak robimy następujące rzeczy:

- Tworzymy schemat używając Pydantic `AddInputModel` z polami `a` i `b` w pliku *schema.py*.
- Próba parsowania przychodzącego żądania jako `AddInputModel`, jeśli parametry nie pasują, nastąpi awaria:

   ```python
   # add.py
    try:
        # Waliduj dane wejściowe za pomocą modelu Pydantic
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")
   ```

Możesz zdecydować, czy logikę parsowania umieścisz w wywołaniu narzędzia czy w funkcji obsługi.

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

- W handlerze obsługującym wszystkie wywołania narzędzi próbujemy zparsować przychodzące żądanie do schematu narzędzia:

    ```typescript
    const Schema = tool.rawSchema;

    try {
       const input = Schema.parse(request.params.arguments);
    ```

    jeśli to się uda, przechodzimy do wywołania właściwego narzędzia:

    ```typescript
    const result = await tool.callback(input);
    ```

Jak widzisz, takie podejście tworzy świetną architekturę, wszystko ma swoje miejsce, *server.ts* to bardzo mały plik, który jedynie podłącza funkcje obsługi żądań, a każda funkcja jest w swoim folderze, tj. tools/, resources/ lub /prompts.

Świetnie, spróbujmy teraz to zbudować. 

## Ćwiczenie: tworzenie serwera niskiego poziomu

W tym ćwiczeniu wykonamy następujące kroki:

1. Utwórz serwer niskiego poziomu obsługujący listowanie narzędzi oraz ich wywoływanie.
1. Zaimplementuj architekturę, na której możesz dalej budować.
1. Dodaj walidację, aby upewnić się, że wywołania narzędzi są prawidłowo weryfikowane.

### -1- Utworzenie architektury

Pierwszą rzeczą, którą musimy rozwiązać, jest architektura pomagająca skalować się wraz z dodawaniem funkcji, oto jak to wygląda:

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

Ustawiliśmy teraz architekturę, która pozwala łatwo dodawać nowe narzędzia w folderze tools. Możesz też dodać podfoldery dla zasobów i promptów.

### -2- Tworzenie narzędzia

Zobaczmy teraz, jak wygląda tworzenie narzędzia. Najpierw musi zostać utworzone w podfolderze *tool* w ten sposób:

**Python**

```python
from .schema import AddInputModel

async def add_handler(args) -> float:
    try:
        # Zweryfikuj dane wejściowe za pomocą modelu Pydantic
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # DO ZROBIENIA: dodaj Pydantic, abyśmy mogli stworzyć AddInputModel i zweryfikować argumenty

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

Widać tutaj, jak definiujemy nazwę, opis i schemat wejścia przy użyciu Pydantic oraz handler, który zostanie wywołany po zawołaniu narzędzia. Na końcu udostępniamy `tool_add`, czyli słownik zawierający wszystkie te właściwości.

Jest też *schema.py*, który definiuje schemat wejściowy wykorzystywany przez nasze narzędzie:

```python
from pydantic import BaseModel

class AddInputModel(BaseModel):
    a: float
    b: float
```

Musimy też uzupełnić *__init__.py*, aby folder tools był traktowany jak moduł. Dodatkowo musimy udostępnić moduły w nim tak:

```python
from .add import tool_add

tools = {
  tool_add["name"] : tool_add
}
```

Możemy wciąż dodawać do tego pliku więcej narzędzi.

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

Tutaj tworzymy słownik z właściwościami:

- name, czyli nazwę narzędzia.
- rawSchema, czyli schemat Zod, który będzie używany do walidacji przychodzących żądań wywołania narzędzia.
- inputSchema, ten schemat będzie używany przez handler.
- callback, służy do wywołania narzędzia.

Jest też `Tool`, które konwertuje ten słownik na typ akceptowany przez handler serwera MCP i wygląda tak:

```typescript
import { z } from 'zod';

export interface Tool {
    name: string;
    inputSchema: any;
    rawSchema: z.ZodTypeAny;
    callback: (args: z.infer<z.ZodTypeAny>) => Promise<{ content: { type: string; text: string }[] }>;
}
```

A jest też *schema.ts*, gdzie przechowujemy schematy wejścia dla każdego narzędzia, obecnie jest tam tylko jeden schemat, ale wraz z dodawaniem narzędzi możemy dodawać więcej wpisów:

```typescript
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });
```

Świetnie, przejdźmy teraz do obsługi listowania narzędzi.

### -3- Obsługa listowania narzędzi

Następnie, aby obsłużyć listowanie narzędzi, musimy skonfigurować handler żądań do tego celu. Oto co należy dodać do pliku serwera:

**Python**

```python
# kod pominięty dla zwięzłości
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

Tutaj dodajemy dekorator `@server.list_tools` oraz implementującą funkcję `handle_list_tools`. W niej musimy wygenerować listę narzędzi. Zauważ, że każde narzędzie musi mieć nazwę, opis i inputSchema.   

**TypeScript**

Aby skonfigurować handler żądań do listowania narzędzi, wywołujemy `setRequestHandler` na serwerze z dopasowanym schematem, w tym przypadku `ListToolsRequestSchema`. 

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
// kod pominięty dla zwięzłości
import { tools } from './tools/index.js';

server.setRequestHandler(ListToolsRequestSchema, async (request) => {
  // Zwróć listę zarejestrowanych narzędzi
  return {
    tools: tools
  };
});
```

Świetnie, właśnie rozwiązaliśmy część dotyczącą listowania narzędzi, teraz zobaczmy, jak możemy wywoływać narzędzia.

### -4- Obsługa wywoływania narzędzia

Aby wywołać narzędzie, musimy ustawić kolejny handler żądań, tym razem zajmujący się żądaniami określającymi, którą funkcję wywołać i z jakimi argumentami.

**Python**

Skorzystajmy z dekoratora `@server.call_tool` i zaimplementujmy go funkcją `handle_call_tool`. W niej musimy wyodrębnić nazwę narzędzia, argumenty i upewnić się, że są poprawne dla danego narzędzia. Walidację argumentów możemy zrobić tu lub dalej, w samym narzędziu.

```python
@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict[str, str] | None
) -> list[types.TextContent]:
    
    # tools to słownik z nazwami narzędzi jako kluczami
    if name not in tools.tools:
        raise ValueError(f"Unknown tool: {name}")
    
    tool = tools.tools[name]

    result = "default"
    try:
        # wywołaj narzędzie
        result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)
    except Exception as e:
        raise ValueError(f"Error calling tool {name}: {str(e)}")

    return [
        types.TextContent(type="text", text=str(result))
    ]
```

Oto co się dzieje:

- Nazwa narzędzia jest już podana jako parametr wejściowy `name`, podobnie argumenty w formie słownika `arguments`.

- Narzędzie jest wywoływane przez `result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)`. Walidacja argumentów odbywa się w funkcji `handler`, jeśli się nie uda, zostanie rzucony wyjątek. 

Oto pełne zrozumienie listowania i wywoływania narzędzi z użyciem serwera niskiego poziomu.

Zobacz [pełny przykład](./code/README.md) tutaj

## Zadanie

Rozbuduj podany kod o szereg narzędzi, zasobów i promptów i zauważ, że wystarczy dodawać pliki tylko w katalogu tools i nigdzie indziej. 

*Brak rozwiązania*

## Podsumowanie

W tym rozdziale zobaczyliśmy, jak działa podejście serwera niskiego poziomu i jak może nam pomóc stworzyć czystą architekturę, na której można dalej budować. Omówiliśmy również walidację i pokazano, jak pracować z bibliotekami walidacyjnymi do tworzenia schematów dla walidacji wejścia.

## Co dalej

- Dalej: [Prosta Autoryzacja](../11-simple-auth/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zastrzeżenie**:
Niniejszy dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Choć dążymy do dokładności, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub niedokładności. Oryginalny dokument w jego języku źródłowym należy uznawać za autorytatywne źródło. W przypadku informacji krytycznych zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->