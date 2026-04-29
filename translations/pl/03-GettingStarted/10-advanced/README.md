# Zaawansowane użycie serwera

W SDK MCP dostępne są dwa różne typy serwerów: zwykły serwer oraz serwer niskiego poziomu. Zazwyczaj używasz zwykłego serwera, aby dodać do niego funkcje. W niektórych jednak przypadkach chcesz polegać na serwerze niskiego poziomu, np.:

- Lepsza architektura. Możliwe jest stworzenie czystej architektury zarówno ze zwykłym serwerem, jak i serwerem niskiego poziomu, ale można argumentować, że jest to trochę łatwiejsze z serwerem niskiego poziomu.
- Dostępność funkcji. Niektóre zaawansowane funkcje mogą być używane tylko z serwerem niskiego poziomu. Zobaczysz to w kolejnych rozdziałach, gdy dodamy sampling i elicytację.

## Zwykły serwer vs serwer niskiego poziomu

Tak wygląda tworzenie serwera MCP ze zwykłym serwerem

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

Chodzi o to, że explicite dodajesz każde narzędzie, zasób lub prompt, które chcesz, aby serwer posiadał. Nie ma w tym nic złego.

### Podejście serwera niskiego poziomu

Gdy jednak używasz podejścia serwera niskiego poziomu, musisz myśleć o tym inaczej. Zamiast rejestrować każde narzędzie, tworzysz dwa handler'y na typ funkcji (narzędzia, zasoby lub prompty). Na przykład narzędzia mają wtedy tylko dwie funkcje:

- Lista wszystkich narzędzi. Jedna funkcja odpowiada za wszystkie próby listowania narzędzi.
- obsługa wywołań wszystkich narzędzi. Tutaj również tylko jedna funkcja obsługuje wywołania narzędzi.

Brzmi to jak potencjalnie mniej pracy, prawda? Zamiast rejestrować narzędzie, wystarczy, aby narzędzie pojawiło się na liście narzędzi oraz aby było wywołane, gdy nadejdzie żądanie wywołania narzędzia.

Spójrzmy, jak teraz wygląda kod:

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

Mamy teraz funkcję, która zwraca listę funkcji. Każdy wpis na liście narzędzi ma pola takie jak `name`, `description` i `inputSchema`, zgodnie z typem zwracanym. To pozwala trzymać nasze narzędzia i definicje funkcji gdzie indziej. Możemy teraz tworzyć wszystkie narzędzia w katalogu tools, i analogicznie dla wszystkich funkcji, więc projekt może nagle być zorganizowany tak:

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

Świetnie, nasza architektura może wyglądać całkiem czysto.

A co z wywoływaniem narzędzi, czy to ten sam pomysł, jeden handler do wywołania narzędzia, dowolnego narzędzia? Tak, dokładnie, oto kod dla tego:

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

Jak widać z powyższego kodu, musimy wyciągnąć, które narzędzie wywołać i z jakimi argumentami, a następnie przejść do wywołania narzędzia.

## Ulepszanie podejścia walidacją

Do tej pory widziałeś, jak wszystkie rejestracje do dodawania narzędzi, zasobów i promptów mogą być zastąpione tymi dwoma handler'ami na typ funkcji. Co jeszcze musimy zrobić? Powinniśmy dodać jakąś formę walidacji, by zagwarantować, że narzędzie jest wywoływane z prawidłowymi argumentami. Każde środowisko wykonawcze ma swoje rozwiązanie, na przykład Python używa Pydantic, a TypeScript używa Zod. Idea jest taka, że wykonujemy następujące kroki:

- Przenosimy logikę tworzenia funkcji (narzędzia, zasobu lub promptu) do dedykowanego katalogu.
- Dodajemy sposób walidacji przychodzącego żądania, na przykład wywołania narzędzia.

### Tworzenie funkcji

Aby stworzyć funkcję, musimy stworzyć plik dla tej funkcji i upewnić się, że ma ona obowiązkowe pola wymagane dla tego typu funkcji. Pola różnią się nieco między narzędziami, zasobami i promptami.

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

    # TODO: dodaj Pydantic, abyśmy mogli utworzyć AddInputModel i zwalidować argumenty

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

Tutaj widać, jak wykonujemy następujące kroki:

- Tworzymy schemat Pydantic `AddInputModel` z polami `a` i `b` w pliku *schema.py*.
- Próbujemy sparsować przychodzące żądanie na typ `AddInputModel`, jeśli jest rozbieżność w parametrach, nastąpi awaria:

   ```python
   # add.py
    try:
        # Waliduj dane wejściowe za pomocą modelu Pydantic
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")
   ```

Możesz wybrać, czy tę logikę parsowania umieścić w samym wywołaniu narzędzia, czy w funkcji handlera.

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

- W handlerze obsługującym wszystkie wywołania narzędzi staramy się teraz sparsować przychodzące żądanie do schematu zdefiniowanego przez narzędzie:

    ```typescript
    const Schema = tool.rawSchema;

    try {
       const input = Schema.parse(request.params.arguments);
    ```

    jeśli się to uda, przechodzimy do wywołania właściwego narzędzia:

    ```typescript
    const result = await tool.callback(input);
    ```

Jak widać, to podejście tworzy świetną architekturę, bo wszystko ma swoje miejsce, *server.ts* to bardzo mały plik, który tylko podłącza handlery żądań, a każda funkcja jest w swoim odpowiednim katalogu, np. tools/, resources/ lub prompts/.

Super, spróbujmy to następnie zbudować.

## Ćwiczenie: Tworzenie serwera niskiego poziomu

W tym ćwiczeniu zrobimy następujące rzeczy:

1. Stworzymy serwer niskiego poziomu obsługujący listowanie narzędzi i wywoływanie narzędzi.
1. Wdrożymy architekturę, na której można budować.
1. Dodamy walidację, aby zapewnić prawidłową walidację wywołań narzędzi.

### -1- Stworzenie architektury

Pierwszą rzeczą do zrobienia jest stworzenie architektury, która pomoże nam skalować wraz z dodawaniem więcej funkcji, oto jak wygląda:

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

Mamy teraz ustawioną architekturę, która pozwala łatwo dodawać nowe narzędzia w katalogu tools. Śmiało możesz użyć tego dla podkatalogów resources i prompts.

### -2- Tworzenie narzędzia

Zobaczmy, jak wygląda tworzenie narzędzia. Najpierw musi ono powstać w podkatalogu *tool* tak:

**Python**

```python
from .schema import AddInputModel

async def add_handler(args) -> float:
    try:
        # Waliduj dane wejściowe za pomocą modelu Pydantic
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

Widać tu jak definiujemy nazwę, opis oraz schemat wejścia przy pomocy Pydantic oraz handler, który zostanie wywołany, gdy narzędzie będzie wywoływane. Na końcu udostępniamy `tool_add`, który jest słownikiem trzymającym te właściwości.

Jest też *schema.py*, który definiuje schemat wejściowy dla naszego narzędzia:

```python
from pydantic import BaseModel

class AddInputModel(BaseModel):
    a: float
    b: float
```

Potrzebujemy też uzupełnić *__init__.py*, aby katalog tools był traktowany jako moduł. Dodatkowo musimy wystawić moduły w nim tak:

```python
from .add import tool_add

tools = {
  tool_add["name"] : tool_add
}
```

Możemy dalej rozszerzać ten plik, gdy dodajemy więcej narzędzi.

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

Tworzymy słownik z właściwościami:

- name, nazwa narzędzia.
- rawSchema, to schemat Zod, używany do walidacji przychodzących żądań wywołania narzędzia.
- inputSchema, ten schemat jest używany przez handler.
- callback, służy do wywołania narzędzia.

Jest także `Tool`, który konwertuje ten słownik na typ akceptowany przez handler serwera mcp i wygląda tak:

```typescript
import { z } from 'zod';

export interface Tool {
    name: string;
    inputSchema: any;
    rawSchema: z.ZodTypeAny;
    callback: (args: z.infer<z.ZodTypeAny>) => Promise<{ content: { type: string; text: string }[] }>;
}
```

Mamy też *schema.ts*, gdzie przechowujemy schematy wejściowe dla każdego narzędzia, obecnie tylko jeden schemat, ale można dodawać kolejne:

```typescript
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });
```

Świetnie, przejdźmy teraz do obsługi listowania narzędzi.

### -3- Obsługa listowania narzędzi

Aby obsłużyć listowanie narzędzi, musimy ustawić handler żądań dla tego. Oto co dodajemy do pliku serwera:

**Python**

```python
# kod pominięty ze względu na zwięzłość
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

Dodajemy dekorator `@server.list_tools` i implementującą funkcję `handle_list_tools`. W niej produkujemy listę narzędzi. Zwróć uwagę, że każde narzędzie musi mieć name, description i inputSchema.

**TypeScript**

Aby ustawić handler żądań do listowania narzędzi, musimy wywołać `setRequestHandler` na serwerze z odpowiednim schematem, w tym przypadku `ListToolsRequestSchema`.

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

Świetnie, mamy już obsługę listowania narzędzi, zobaczmy teraz, jak można wywoływać narzędzia.

### -4- Obsługa wywołania narzędzia

Aby wywołać narzędzie, musimy ustawić kolejny handler żądań, tym razem zajmujący się obsługą żądania określającego, którą funkcję wywołać i z jakimi argumentami.

**Python**

Użyjmy dekoratora `@server.call_tool` i implementujmy funkcję `handle_call_tool`. W niej parsujemy nazwę narzędzia, argumenty i sprawdzamy, czy argumenty są prawidłowe dla danego narzędzia. Walidację argumentów możemy wykonać tutaj lub w samym narzędziu.

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

Co się dzieje:

- Nazwa narzędzia jest już dostępna jako parametr wejściowy `name`, a argumenty jako słownik `arguments`.
- Narzędzie jest wywoływane przez `result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)`. Walidacja argumentów dzieje się w właściwości `handler`, która wskazuje na funkcję; jeśli walidacja się nie powiedzie, zostanie rzucony wyjątek.

Teraz mamy pełne zrozumienie, jak listować i wywoływać narzędzia w serwerze niskiego poziomu.

Zobacz [pełny przykład](./code/README.md)

## Zadanie

Rozszerz kod, który otrzymałeś, dodając wiele narzędzi, zasobów i promptów i zastanów się, jak zauważasz, że dodajesz tylko pliki w katalogu tools i nigdzie indziej.

*Nie podano rozwiązania*

## Podsumowanie

W tym rozdziale zobaczyliśmy, jak działa podejście serwera niskiego poziomu i jak może pomóc stworzyć ładną architekturę, na której możemy dalej budować. Omówiliśmy także walidację i pokazano Ci, jak używać bibliotek walidacyjnych do tworzenia schematów do walidacji wejścia.

## Co dalej

- Następny: [Prosta autoryzacja](../11-simple-auth/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zastrzeżenie**:  
Niniejszy dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Choć dokładamy starań, aby tłumaczenie było jak najbardziej precyzyjne, prosimy mieć na uwadze, że automatyczne tłumaczenia mogą zawierać błędy lub niedokładności. Oryginalny dokument w jego języku źródłowym powinien być uważany za autorytatywne źródło. W przypadku informacji krytycznych zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z korzystania z tego tłumaczenia.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->