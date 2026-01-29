# Zaawansowane korzystanie z serwera

W MCP SDK dostępne są dwa różne typy serwerów: zwykły serwer oraz serwer niskopoziomowy. Zazwyczaj używa się zwykłego serwera do dodawania funkcji. Jednak w niektórych przypadkach warto skorzystać z serwera niskopoziomowego, na przykład:

- Lepsza architektura. Można stworzyć czystą architekturę zarówno za pomocą zwykłego serwera, jak i serwera niskopoziomowego, ale można argumentować, że z serwerem niskopoziomowym jest to nieco łatwiejsze.
- Dostępność funkcji. Niektóre zaawansowane funkcje są dostępne tylko w serwerze niskopoziomowym. Zobaczysz to w kolejnych rozdziałach, gdy dodamy próbkowanie i elicytację.

## Zwykły serwer vs serwer niskopoziomowy

Tak wygląda tworzenie serwera MCP za pomocą zwykłego serwera:

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

Chodzi o to, że jawnie dodajesz każde narzędzie, zasób lub podpowiedź, które chcesz, aby serwer posiadał. Nie ma w tym nic złego.

### Podejście serwera niskopoziomowego

Jednak korzystając z podejścia serwera niskopoziomowego, musisz myśleć inaczej. Zamiast rejestrować każde narzędzie, tworzysz dwa obsługujące funkcje dla każdego typu funkcji (narzędzia, zasoby lub podpowiedzi). Na przykład dla narzędzi są tylko dwie funkcje:

- Lista wszystkich narzędzi. Jedna funkcja odpowiada za wszystkie próby wylistowania narzędzi.
- Obsługa wywołań narzędzi. Tutaj również jest tylko jedna funkcja obsługująca wywołania narzędzi.

Brzmi jak mniej pracy, prawda? Zamiast rejestrować narzędzie, wystarczy upewnić się, że narzędzie jest uwzględnione w liście narzędzi i że jest wywoływane, gdy nadejdzie żądanie wywołania narzędzia.

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

Tutaj mamy funkcję, która zwraca listę funkcji. Każdy wpis na liście narzędzi ma teraz pola takie jak `name`, `description` i `inputSchema`, aby dostosować się do typu zwrotnego. Dzięki temu możemy umieścić definicję narzędzi i funkcji w innym miejscu. Możemy teraz tworzyć wszystkie nasze narzędzia w folderze narzędzi, podobnie jak wszystkie funkcje, dzięki czemu nasz projekt może być zorganizowany w następujący sposób:

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

To świetne rozwiązanie, nasza architektura może wyglądać bardzo przejrzyście.

A co z wywoływaniem narzędzi? Czy działa to na tej samej zasadzie, jedna funkcja obsługująca wywołanie dowolnego narzędzia? Tak, dokładnie, oto kod:

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

Jak widać w powyższym kodzie, musimy rozpoznać narzędzie do wywołania, z jakimi argumentami, a następnie przejść do wywołania narzędzia.

## Udoskonalenie podejścia za pomocą walidacji

Jak dotąd widziałeś, jak wszystkie rejestracje dodające narzędzia, zasoby i podpowiedzi można zastąpić tymi dwoma funkcjami obsługującymi dla każdego typu funkcji. Co jeszcze musimy zrobić? Powinniśmy dodać jakąś formę walidacji, aby upewnić się, że narzędzie jest wywoływane z odpowiednimi argumentami. Każde środowisko wykonawcze ma swoje własne rozwiązanie, na przykład Python używa Pydantic, a TypeScript używa Zod. Idea polega na tym, aby zrobić następujące:

- Przenieść logikę tworzenia funkcji (narzędzia, zasobu lub podpowiedzi) do dedykowanego folderu.
- Dodać sposób walidacji przychodzącego żądania, na przykład wywołania narzędzia.

### Tworzenie funkcji

Aby stworzyć funkcję, musimy utworzyć plik dla tej funkcji i upewnić się, że zawiera ona wymagane pola. Pola te różnią się nieco w zależności od narzędzi, zasobów i podpowiedzi.

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

Tutaj widzisz, jak robimy następujące:

- Tworzymy schemat za pomocą Pydantic `AddInputModel` z polami `a` i `b` w pliku *schema.py*.
- Próbujemy przetworzyć przychodzące żądanie na typ `AddInputModel`. Jeśli parametry się nie zgadzają, nastąpi awaria:

   ```python
   # add.py
    try:
        # Validate input using Pydantic model
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")
   ```

Możesz zdecydować, czy umieścić tę logikę przetwarzania w samym wywołaniu narzędzia, czy w funkcji obsługującej.

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

- W funkcji obsługującej wszystkie wywołania narzędzi próbujemy przetworzyć przychodzące żądanie na schemat zdefiniowany dla narzędzia:

    ```typescript
    const Schema = tool.rawSchema;

    try {
       const input = Schema.parse(request.params.arguments);
    ```

    Jeśli to się powiedzie, przechodzimy do wywołania właściwego narzędzia:

    ```typescript
    const result = await tool.callback(input);
    ```

Jak widać, to podejście tworzy świetną architekturę, ponieważ wszystko ma swoje miejsce. Plik *server.ts* jest bardzo mały i tylko łączy funkcje obsługujące żądania, a każda funkcja znajduje się w odpowiednim folderze, tj. tools/, resources/ lub prompts/.

Świetnie, spróbujmy teraz to zbudować.

## Ćwiczenie: Tworzenie serwera niskopoziomowego

W tym ćwiczeniu zrobimy następujące:

1. Utworzymy serwer niskopoziomowy obsługujący listowanie narzędzi i wywoływanie narzędzi.
1. Zaimplementujemy architekturę, na której można budować.
1. Dodamy walidację, aby upewnić się, że wywołania narzędzi są odpowiednio walidowane.

### -1- Tworzenie architektury

Pierwszą rzeczą, którą musimy rozwiązać, jest architektura, która pomoże nam skalować, gdy dodamy więcej funkcji. Oto jak to wygląda:

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

Teraz mamy ustawioną architekturę, która zapewnia, że możemy łatwo dodawać nowe narzędzia w folderze narzędzi. Możesz również dodać podkatalogi dla zasobów i podpowiedzi.

### -2- Tworzenie narzędzia

Zobaczmy, jak wygląda tworzenie narzędzia. Najpierw musi być ono utworzone w podkatalogu *tool* w następujący sposób:

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

Tutaj widzimy, jak definiujemy nazwę, opis, schemat wejściowy za pomocą Pydantic oraz funkcję obsługującą, która zostanie wywołana, gdy narzędzie zostanie użyte. Na końcu udostępniamy `tool_add`, który jest słownikiem zawierającym wszystkie te właściwości.

Jest również plik *schema.py*, który służy do definiowania schematu wejściowego używanego przez nasze narzędzie:

```python
from pydantic import BaseModel

class AddInputModel(BaseModel):
    a: float
    b: float
```

Musimy również uzupełnić *__init__.py*, aby upewnić się, że katalog narzędzi jest traktowany jako moduł. Dodatkowo musimy udostępnić moduły w nim zawarte w następujący sposób:

```python
from .add import tool_add

tools = {
  tool_add["name"] : tool_add
}
```

Możemy dodawać do tego pliku, gdy dodajemy więcej narzędzi.

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

Tutaj tworzymy słownik składający się z właściwości:

- name, czyli nazwa narzędzia.
- rawSchema, czyli schemat Zod, który będzie używany do walidacji przychodzących żądań wywołania narzędzia.
- inputSchema, czyli schemat używany przez funkcję obsługującą.
- callback, który jest używany do wywołania narzędzia.

Jest również `Tool`, który służy do konwersji tego słownika na typ akceptowany przez funkcję obsługującą serwera MCP i wygląda tak:

```typescript
import { z } from 'zod';

export interface Tool {
    name: string;
    inputSchema: any;
    rawSchema: z.ZodTypeAny;
    callback: (args: z.infer<z.ZodTypeAny>) => Promise<{ content: { type: string; text: string }[] }>;
}
```

Jest także *schema.ts*, gdzie przechowujemy schematy wejściowe dla każdego narzędzia. Wygląda to tak, że obecnie mamy tylko jeden schemat, ale gdy dodamy więcej narzędzi, możemy dodać więcej wpisów:

```typescript
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });
```

Świetnie, przejdźmy teraz do obsługi listowania naszych narzędzi.

### -3- Obsługa listowania narzędzi

Aby obsłużyć listowanie narzędzi, musimy ustawić funkcję obsługującą żądania. Oto co musimy dodać do naszego pliku serwera:

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

Tutaj dodajemy dekorator `@server.list_tools` oraz implementujemy funkcję `handle_list_tools`. W tej funkcji musimy wygenerować listę narzędzi. Zauważ, że każde narzędzie musi mieć nazwę, opis i inputSchema.

**TypeScript**

Aby ustawić funkcję obsługującą żądania listowania narzędzi, musimy wywołać `setRequestHandler` na serwerze z schematem pasującym do tego, co próbujemy zrobić, w tym przypadku `ListToolsRequestSchema`.

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

Świetnie, teraz rozwiązaliśmy problem listowania narzędzi. Spójrzmy, jak możemy wywoływać narzędzia.

### -4- Obsługa wywoływania narzędzia

Aby wywołać narzędzie, musimy ustawić kolejną funkcję obsługującą żądania, tym razem skoncentrowaną na obsłudze żądania określającego, które narzędzie wywołać i z jakimi argumentami.

**Python**

Użyjmy dekoratora `@server.call_tool` i zaimplementujmy go za pomocą funkcji, takiej jak `handle_call_tool`. W tej funkcji musimy rozpoznać nazwę narzędzia, jego argumenty i upewnić się, że argumenty są poprawne dla danego narzędzia. Możemy walidować argumenty w tej funkcji lub dalej w samym narzędziu.

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

Oto co się dzieje:

- Nazwa narzędzia jest już obecna jako parametr wejściowy `name`, co dotyczy również argumentów w formie słownika `arguments`.

- Narzędzie jest wywoływane za pomocą `result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)`. Walidacja argumentów odbywa się w właściwości `handler`, która wskazuje na funkcję. Jeśli walidacja się nie powiedzie, zostanie zgłoszony wyjątek.

Teraz mamy pełne zrozumienie listowania i wywoływania narzędzi za pomocą serwera niskopoziomowego.

Zobacz [pełny przykład](./code/README.md) tutaj.

## Zadanie

Rozszerz kod, który otrzymałeś, o kilka narzędzi, zasobów i podpowiedzi. Zastanów się, jak zauważasz, że musisz dodawać pliki tylko w katalogu narzędzi, a nigdzie indziej.

*Brak rozwiązania*

## Podsumowanie

W tym rozdziale zobaczyliśmy, jak działa podejście serwera niskopoziomowego i jak może ono pomóc w stworzeniu dobrej architektury, na której można dalej budować. Omówiliśmy również walidację i pokazano Ci, jak korzystać z bibliotek walidacyjnych do tworzenia schematów dla walidacji danych wejściowych.

---

**Zastrzeżenie**:  
Ten dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż dokładamy wszelkich starań, aby tłumaczenie było precyzyjne, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego rodzimym języku powinien być uznawany za źródło autorytatywne. W przypadku informacji krytycznych zaleca się skorzystanie z profesjonalnego tłumaczenia przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.