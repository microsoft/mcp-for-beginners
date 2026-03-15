# Zaawansowane wykorzystanie serwera

W MCP SDK udostępnione są dwa różne typy serwerów: zwykły serwer oraz serwer niskopoziomowy. Zazwyczaj używasz zwykłego serwera, aby dodać do niego funkcje. W niektórych jednak przypadkach warto skorzystać z serwera niskopoziomowego, np.:

- Lepsza architektura. Możliwe jest stworzenie czystej architektury zarówno ze zwykłym, jak i niskopoziomowym serwerem, ale można argumentować, że jest to nieco łatwiejsze przy serwerze niskopoziomowym.
- Dostępność funkcji. Niektóre zaawansowane funkcje mogą być używane tylko z serwerem niskopoziomowym. Zobaczysz to w dalszych rozdziałach, gdy dodamy próbkowanie i elicytację.

## Zwykły serwer vs serwer niskopoziomowy

Oto jak wygląda tworzenie serwera MCP za pomocą zwykłego serwera

**Python**

```python
mcp = FastMCP("Demo")

# Dodaj narzędzie dodawania
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

// Dodaj narzędzie dodawania
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

Chodzi o to, że wyraźnie dodajesz każde narzędzie, zasób lub prompt, które mają być dostępne na serwerze. Nie ma w tym nic złego.

### Podejście serwera niskopoziomowego

Natomiast korzystając z podejścia serwera niskopoziomowego, musisz podejść do tego inaczej. Zamiast rejestrować każde narzędzie, tworzysz dwie funkcje obsługi dla każdego typu funkcji (narzędzia, zasoby lub prompt). Na przykład narzędzia mają wtedy tylko dwie funkcje:

- Lista wszystkich narzędzi. Jedna funkcja jest odpowiedzialna za wszystkie próby listowania narzędzi.
- obsługa wywoływania narzędzi. Również tu jest tylko jedna funkcja obsługująca wywołania narzędzia.

Brzmi to jak potencjalnie mniej pracy, prawda? Zamiast rejestrować narzędzie wystarczy, że narzędzie pojawi się na liście podczas listowania wszystkich narzędzi i że zostanie wywołane przy przychodzącym żądaniu wywołania narzędzia.

Zobaczmy, jak teraz wygląda kod:

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

Mamy teraz funkcję, która zwraca listę funkcji. Każdy wpis na liście narzędzi ma teraz pola `name`, `description` i `inputSchema`, aby spełnić typ zwracany. Dzięki temu możemy umieścić definicje narzędzi i funkcji gdzie indziej. Możemy teraz tworzyć wszystkie narzędzia w folderze tools, podobnie z funkcjami, więc projekt może być nagle zorganizowany tak:

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

To świetne, nasza architektura może wyglądać bardzo czysto.

A co z wywoływaniem narzędzi, czy to ta sama koncepcja, jeden handler do wywoływania dowolnego narzędzia? Tak, dokładnie, oto kod do tego:

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
    // TODO wywołaj narzędzie,

    return {
       content: [{ type: "text", text: `Tool ${name} called with arguments: ${JSON.stringify(input)}, result: ${JSON.stringify(result)}` }]
    };
});
```

Jak widać powyżej, musimy wyodrębnić, które narzędzie wywołać i z jakimi argumentami, a następnie przejść do wywołania narzędzia.

## Ulepszenie podejścia za pomocą walidacji

Jak dotąd widziałeś, że wszystkie rejestracje do dodawania narzędzi, zasobów i promptów można zastąpić tymi dwoma handlerami dla każdego typu funkcji. Co jeszcze musimy zrobić? Powinniśmy dodać jakąś formę walidacji, aby upewnić się, że narzędzie jest wywoływane z odpowiednimi argumentami. Każde środowisko uruchomieniowe ma własne rozwiązanie, np. Python używa Pydantic, a TypeScript Zod. Idea jest taka:

- Przenieść logikę tworzenia funkcji (narzędzia, zasobu lub prompta) do jej dedykowanego folderu.
- Dodać sposób walidacji przychodzącego żądania, np. wywołania narzędzia.

### Tworzenie funkcji

Aby stworzyć funkcję, trzeba utworzyć plik dla tej funkcji i upewnić się, że posiada obowiązkowe pola wymagane dla danej funkcji. Pola różnią się nieco w przypadku narzędzi, zasobów i promptów.

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

Tutaj możesz zobaczyć, jak:

- Tworzymy schemat za pomocą Pydantic `AddInputModel` z polami `a` i `b` w pliku *schema.py*.
- Próbujemy sparsować przychodzące żądanie jako typ `AddInputModel`, jeśli wystąpi niezgodność parametrów, nastąpi błąd:

   ```python
   # add.py
    try:
        # Waliduj dane wejściowe za pomocą modelu Pydantic
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")
   ```

Możesz zdecydować, czy tę logikę parsowania umieścić bezpośrednio w wywołaniu narzędzia, czy w funkcji handlera.

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

- W handlerze obsługującym wszystkie wywołania narzędzi próbujemy teraz sparsować przychodzące żądanie do schematu zdefiniowanego przez narzędzie:

    ```typescript
    const Schema = tool.rawSchema;

    try {
       const input = Schema.parse(request.params.arguments);
    ```

    Jeśli się uda, przechodzimy do wywołania właściwego narzędzia:

    ```typescript
    const result = await tool.callback(input);
    ```

Jak widać, to podejście tworzy świetną architekturę, bo wszystko ma swoje miejsce, a *server.ts* to bardzo mały plik jedynie łączący handlerzy żądań, a każda funkcja znajduje się w swoim folderze, np. tools/, resources/ lub /prompts.

Świetnie, spróbujmy to teraz zbudować.

## Ćwiczenie: Tworzenie serwera niskopoziomowego

W tym ćwiczeniu zrobimy następujące rzeczy:

1. Utworzymy serwer niskopoziomowy obsługujący listowanie narzędzi i wywoływanie narzędzi.
1. Wdrożymy architekturę, na której możesz budować.
1. Dodamy walidację, aby upewnić się, że wywołania narzędzi są poprawnie weryfikowane.

### -1- Utworzenie architektury

Pierwszą rzeczą, którą musimy zająć się, jest architektura, która pomoże nam się skalować, gdy dodamy więcej funkcji, wygląda to tak:

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

Mamy teraz architekturę, która pozwala łatwo dodawać nowe narzędzia w folderze tools. Możesz dodać podfoldery dla zasobów i promptów według własnego uznania.

### -2- Tworzenie narzędzia

Zobaczmy, jak wygląda tworzenie narzędzia. Najpierw musi być utworzone w swoim podfolderze *tool* tak:

**Python**

```python
from .schema import AddInputModel

async def add_handler(args) -> float:
    try:
        # Waliduj dane wejściowe za pomocą modelu Pydantic
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # DO ZROBIENIA: dodaj Pydantic, abyśmy mogli stworzyć AddInputModel i zwalidować argumenty

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

Widzimy tu, jak definiujemy nazwę, opis i schemat wejściowy za pomocą Pydantic oraz handler, który zostanie wywołany po uruchomieniu narzędzia. Na koniec udostępniamy `tool_add`, czyli słownik zawierający te wszystkie właściwości.

Jest też *schema.py* wykorzystywany do zdefiniowania schematu wejściowego dla naszego narzędzia:

```python
from pydantic import BaseModel

class AddInputModel(BaseModel):
    a: float
    b: float
```

Musimy też uzupełnić *__init__.py*, aby folder tools był traktowany jako moduł. Dodatkowo musimy wystawić moduły w nim tak:

```python
from .add import tool_add

tools = {
  tool_add["name"] : tool_add
}
```

Ten plik będziemy rozbudowywać, gdy dodamy kolejne narzędzia.

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

Tworzymy słownik zawierający właściwości:

- name — nazwa narzędzia.
- rawSchema — schemat Zod, używany do walidacji nadchodzących żądań wywołania narzędzia.
- inputSchema — schemat używany przez handler.
- callback — funkcja wywołująca narzędzie.

Mamy również `Tool`, służący do konwersji tego słownika na typ akceptowany przez handler serwera mcp i wygląda to tak:

```typescript
import { z } from 'zod';

export interface Tool {
    name: string;
    inputSchema: any;
    rawSchema: z.ZodTypeAny;
    callback: (args: z.infer<z.ZodTypeAny>) => Promise<{ content: { type: string; text: string }[] }>;
}
```

Jest też plik *schema.ts*, gdzie przechowujemy schematy wejściowe dla każdego narzędzia, obecnie z jednym schematem, ale wraz z dodawaniem narzędzi możemy dodawać kolejne wpisy:

```typescript
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });
```

Świetnie, przejdźmy dalej do obsługi listowania narzędzi.

### -3- Obsługa listowania narzędzi

Aby obsłużyć listowanie narzędzi, musimy dodać handler żądań. Oto co dodajemy do pliku serwera:

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

Dodajemy dekorator `@server.list_tools` oraz implementację funkcji `handle_list_tools`. Ta funkcja musi zwrócić listę narzędzi. Zauważ, że każde narzędzie musi mieć nazwę, opis i inputSchema.

**TypeScript**

Aby ustawić handler żądań dla listowania narzędzi, wywołujemy `setRequestHandler` na serwerze z odpowiednim schematem, w tym przypadku `ListToolsRequestSchema`.

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

Świetnie, rozwiązaliśmy fragment dotyczący listowania narzędzi, zobaczmy, jak możemy wywoływać narzędzia.

### -4- Obsługa wywoływania narzędzia

Do wywołania narzędzia musimy dodać kolejny handler żądań, który będzie obsługiwał żądanie określające, którą funkcję wywołać i z jakimi argumentami.

**Python**

Skorzystajmy z dekoratora `@server.call_tool` i zaimplementujmy go funkcją `handle_call_tool`. W niej musimy wydobyć nazwę narzędzia, argumenty i upewnić się, że argumenty są poprawne dla danego narzędzia. Walidację możemy zrobić tutaj lub później w samym narzędziu.

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

Oto, co się dzieje:

- Nazwa narzędzia jest już dostępna jako parametr wejściowy `name`, podobnie jak argumenty w słowniku `arguments`.

- Narzędzie jest wywoływane przez `result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)`. Walidacja argumentów odbywa się w właściwości `handler`, która wskazuje na funkcję, jeśli się nie powiedzie, zostanie zgłoszony wyjątek.

Teraz mamy pełne zrozumienie, jak listować i wywoływać narzędzia przy użyciu serwera niskopoziomowego.

Zobacz [pełny przykład](./code/README.md) tutaj

## Zadanie

Rozszerz dostarczony kod o kilka narzędzi, zasobów i promptów i zauważ, że wystarczy dodawać pliki tylko w katalogu tools i nigdzie indziej.

*Brak rozwiązania*

## Podsumowanie

W tym rozdziale zobaczyliśmy, jak działa podejście serwera niskopoziomowego i jak pomaga stworzyć czystą architekturę, którą można rozbudowywać. Omówiliśmy także walidację i pokazano, jak pracować z bibliotekami walidacyjnymi, aby tworzyć schematy walidacji wejścia.

## Co dalej

- Następny: [Prosta autoryzacja](../11-simple-auth/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zastrzeżenie**:
Niniejszy dokument został przetłumaczony przy użyciu usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż dążymy do dokładności, prosimy pamiętać, że tłumaczenia automatyczne mogą zawierać błędy lub nieścisłości. Oryginalny dokument w języku źródłowym powinien być uznawany za źródło autorytatywne. W przypadku informacji krytycznych zaleca się skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z korzystania z tego tłumaczenia.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->