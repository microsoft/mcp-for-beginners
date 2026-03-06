# MCP сервер са stdio транспортом

> **⚠️ Важна обавест**: Од MCP спецификације 2025-06-18, самосталан SSE (Server-Sent Events) transport је **застарео** и замењен је „Streamable HTTP“ транспортом. Тренутна MCP спецификација дефинише два примарна механизма транспорта:
> 1. **stdio** - Стандардни улаз/излаз (препоручено за локалне сервере)
> 2. **Streamable HTTP** - За удаљене сервере који могу интерно користити SSE
>
> Овај час је ажуриран да се фокусира на **stdio транспорт**, који је препоручен приступ за већину MCP серверских имплементација.

stdio транспорт омогућава MCP серверима комуникацију са клијентима преко стандардних улазних и излазних токова. Ово је најчешће коришћен и препоручен механизам транспорта у тренутној MCP спецификацији, пружајући једноставан и ефикасан начин за изградњу MCP сервера који се лако могу интегрисати са разним клијент апликацијама.

## Преглед

Овај час обухвата како изградити и користити MCP сервере користећи stdio транспорт.

## Циљеви учења

На крају овог часа, моћи ћете да:

- Изградите MCP сервер користећи stdio транспорт.
- Отстрањивате грешке на MCP серверу користећи Inspector.
- Користите MCP сервер у Visual Studio Code.
- Разумете тренутне MCP транспортне механизме и зашто је stdio препоручен.

## stdio транспорт - Како функционише

stdio транспорт је један од два подржана типа транспорта у тренутној MCP спецификацији (2025-06-18). Ево како функционише:

- **Једноставна комуникација**: Сервер чита JSON-RPC поруке са стандардног улаза (`stdin`) и шаље поруке на стандардни излаз (`stdout`).
- **Процесно оријентисан**: Клијент покреће MCP сервер као подпроцес.
- **Формат порука**: Поруке су појединачни JSON-RPC захтеви, обавештења или одговори, који су раздвојени новим линијама.
- **Логовање**: Сервер МОЖЕ писати UTF-8 текстове на стандардну грешку (`stderr`) ради евиденције.

### Кључни захтеви:
- Поруке МОРАЈУ бити раздвојене новим линијама и НЕ смеју садржавати уграђене нове линије
- Сервер НЕ СМЕ писати ништа на `stdout` што није важећа MCP порука
- Клијент НЕ СМЕ писати ништа на `stdin` сервера што није важећа MCP порука

### TypeScript

```typescript
import { Server } from "@modelcontextprotocol/sdk/server/index.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";

const server = new Server(
  {
    name: "example-server",
    version: "1.0.0",
  },
  {
    capabilities: {
      tools: {},
    },
  }
);
```

У претходном коду:

- Импортујемо `Server` класу и `StdioServerTransport` из MCP SDK-а
- Креирaмо инстанцу сервера са основном конфигурацијом и могућностима

### Python

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server

# Креирај инстанцу сервера
server = Server("example-server")

@server.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

async def main():
    async with stdio_server(server) as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            server.create_initialization_options()
        )

if __name__ == "__main__":
    asyncio.run(main())
```

У претходном коду:

- Креирамо инстанцу сервера користећи MCP SDK
- Дефинишемо алате користећи декораторе
- Користимо stdio_server context manager за руковање транспортом

### .NET

```csharp
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;
using Microsoft.Extensions.Logging;
using ModelContextProtocol.Server;

var builder = Host.CreateApplicationBuilder(args);

builder.Services
    .AddMcpServer()
    .WithStdioServerTransport()
    .WithTools<Tools>();

builder.Services.AddLogging(logging => logging.AddConsole());

var app = builder.Build();
await app.RunAsync();
```

Кључна разлика у односу на SSE је да stdio сервери:

- Не захтевају подешавање веб сервера или HTTP крајњих тачака
- Бивају покренути као подпроцеси од стране клијента
- Комуницирају кроз stdin/stdout токове
- Једноставнији су за имплементацију и отстрањивање грешака

## Вежба: Креирање stdio сервера

Да бисмо креирали наш сервер, морамо имати на уму две ствари:

- Потребно је користити веб сервер за излагање крајњих тачака за конекцију и поруке.

## Лабораторија: Креирање једноставног MCP stdio сервера

У овој лабораторији креираћемо једноставан MCP сервер користећи препоручени stdio транспорт. Овај сервер ће изложити алате које клијенти могу повлачити користећи стандардни Model Context Protocol.

### Захтеви

- Python 3.8 или новији
- MCP Python SDK: `pip install mcp`
- Основно разумевање асинхроног програмирања

Хајде да започнемо са креирањем нашег првог MCP stdio сервера:

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp import types

# Конфигуришите евиденцију
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Креирајте сервер
server = Server("example-stdio-server")

@server.tool()
def calculate_sum(a: int, b: int) -> int:
    """Calculate the sum of two numbers"""
    return a + b

@server.tool() 
def get_greeting(name: str) -> str:
    """Generate a personalized greeting"""
    return f"Hello, {name}! Welcome to MCP stdio server."

async def main():
    # Користите stdio транспорт
    async with stdio_server(server) as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            server.create_initialization_options()
        )

if __name__ == "__main__":
    asyncio.run(main())
```

## Кључне разлике у односу на застарели SSE приступ

**Stdio транспорт (тренутни стандард):**
- Једноставан модел подпроцеса – клијент покреће сервер као дете процес
- Комуникација преко stdin/stdout користећи JSON-RPC поруке
- Није потребно подешавање HTTP сервера
- Боље перформансе и безбедност
- Лакше отстрањивање грешака и развој

**SSE транспорт (застарео од MCP 2025-06-18):**
- Захтева HTTP сервер са SSE крајњим тачкама
- Комплексније подешавање са веб сервер инфраструктуром
- Додатна разматрања безбедности за HTTP крајње тачке
- Сада замењен Streamable HTTP-ом за веб сценарије

### Креирање сервера са stdio транспортом

Да бисмо креирали наш stdio сервер, потребно је да:

1. **Импортујемо неопходне библиотеке** - Потребни су нам MCP сервер компоненти и stdio транспорт
2. **Креирамо инстанцу сервера** - Дефинишемо сервер са његовим могућностима
3. **Дефинишемо алате** - Додамо функционалности које желимо изложити
4. **Подесимо транспорт** - Конфигуришемо stdio комуникацију
5. **Покренемо сервер** - Стартујемо сервер и руковамо порукама

Изградимо то корак по корак:

### Корак 1: Креирање основног stdio сервера

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server

# Конфигуришите евиденцију
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Креирајте сервер
server = Server("example-stdio-server")

@server.tool()
def get_greeting(name: str) -> str:
    """Generate a personalized greeting"""
    return f"Hello, {name}! Welcome to MCP stdio server."

async def main():
    async with stdio_server(server) as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            server.create_initialization_options()
        )

if __name__ == "__main__":
    asyncio.run(main())
```

### Корак 2: Додавање више алата

```python
@server.tool()
def calculate_sum(a: int, b: int) -> int:
    """Calculate the sum of two numbers"""
    return a + b

@server.tool()
def calculate_product(a: int, b: int) -> int:
    """Calculate the product of two numbers"""
    return a * b

@server.tool()
def get_server_info() -> dict:
    """Get information about this MCP server"""
    return {
        "server_name": "example-stdio-server",
        "version": "1.0.0",
        "transport": "stdio",
        "capabilities": ["tools"]
    }
```

### Корак 3: Покретање сервера

Сачувајте код као `server.py` и покрените га из командне линије:

```bash
python server.py
```

Сервер ће почети и чекати улаз са stdin. Комуницираће користећи JSON-RPC поруке преко stdio транспорта.

### Корак 4: Тестирање са Inspector-ом

Можете тестирати ваш сервер користећи MCP Inspector:

1. Инсталирајте Inspector: `npx @modelcontextprotocol/inspector`
2. Покрените Inspector и усмерите га на ваш сервер
3. Тестирајте алате које сте креирали

### .NET

```csharp
var builder = WebApplication.CreateBuilder(args);
builder.Services
    .AddMcpServer();
 ```

## Отстрањивање грешака на вашем stdio серверу

### Коришћење MCP Inspector-а

MCP Inspector је вредан алат за отстрањивање грешака и тестирање MCP сервера. Ево како га користити са вашим stdio сервером:

1. **Инсталирајте Inspector**:
   ```bash
   npx @modelcontextprotocol/inspector
   ```

2. **Покрените Inspector**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

3. **Тестирајте сервер**: Inspector обезбеђује веб интерфејс у којем можете:
   - Видети могућности сервера
   - Тестирати алате са различитим параметрима
   - Пратити JSON-RPC поруке
   - Отстрањивати проблеме са везом

### Коришћење VS Code-а

Такође можете отстрањивати грешке вашег MCP сервера директно у VS Code-у:

1. Креирајте конфигурацију покретања у `.vscode/launch.json`:
   ```json
   {
     "version": "0.2.0",
     "configurations": [
       {
         "name": "Debug MCP Server",
         "type": "python",
         "request": "launch",
         "program": "server.py",
         "console": "integratedTerminal"
       }
     ]
   }
   ```

2. Поставите тачке прекида (breakpoints) у вашем коду
3. Покрените дебагер и тестирајте са Inspector-ом

### Уобичајени савети за отстрањивање грешака

- Користите `stderr` за логовање – никад не писати на `stdout` јер је резервисан за MCP поруке
- Осигурајте да све JSON-RPC поруке буду раздвојене новим линијама
- Прво тестирајте са једноставним алатима пре додавања сложенијих функционалности
- Користите Inspector да проверите формате порука

## Коришћење вашег stdio сервера у VS Code-у

Када направите ваш MCP stdio сервер, можете га интегрисати са VS Code да га користите са Claude-ом или другим MCP компатибилним клијентима.

### Конфигурација

1. **Креирајте MCP конфигурациони фајл** у `%APPDATA%\Claude\claude_desktop_config.json` (Windows) или `~/Library/Application Support/Claude/claude_desktop_config.json` (Mac):

   ```json
   {
     "mcpServers": {
       "example-stdio-server": {
         "command": "python",
         "args": ["path/to/your/server.py"]
       }
     }
   }
   ```

2. **Поново покрените Claude**: Затворите и поново отворите Claude да учита нову конфигурацију сервера.

3. **Тестирајте везу**: Започните разговор са Claude-ом и покушајте да користите алате сервера:
   - „Можеш ли да ми се поздравиш преко алата за поздрав?“
   - „Израчунај збир 15 и 27“
   - „Која је информација о серверу?“

### Пример TypeScript stdio сервера

Ево потпуног TypeScript примера за референцу:

```typescript
#!/usr/bin/env node
import { Server } from "@modelcontextprotocol/sdk/server/index.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { CallToolRequestSchema, ListToolsRequestSchema } from "@modelcontextprotocol/sdk/types.js";

const server = new Server(
  {
    name: "example-stdio-server",
    version: "1.0.0",
  },
  {
    capabilities: {
      tools: {},
    },
  }
);

// Додај алате
server.setRequestHandler(ListToolsRequestSchema, async () => {
  return {
    tools: [
      {
        name: "get_greeting",
        description: "Get a personalized greeting",
        inputSchema: {
          type: "object",
          properties: {
            name: {
              type: "string",
              description: "Name of the person to greet",
            },
          },
          required: ["name"],
        },
      },
    ],
  };
});

server.setRequestHandler(CallToolRequestSchema, async (request) => {
  if (request.params.name === "get_greeting") {
    return {
      content: [
        {
          type: "text",
          text: `Hello, ${request.params.arguments?.name}! Welcome to MCP stdio server.`,
        },
      ],
    };
  } else {
    throw new Error(`Unknown tool: ${request.params.name}`);
  }
});

async function runServer() {
  const transport = new StdioServerTransport();
  await server.connect(transport);
}

runServer().catch(console.error);
```

### Пример .NET stdio сервера

```csharp
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;
using Microsoft.Extensions.Logging;
using ModelContextProtocol.Server;
using System.ComponentModel;

var builder = Host.CreateApplicationBuilder(args);

builder.Services
    .AddMcpServer()
    .WithStdioServerTransport()
    .WithTools<Tools>();

var app = builder.Build();
await app.RunAsync();

[McpServerToolType]
public class Tools
{
    [McpServerTool, Description("Get a personalized greeting")]
    public string GetGreeting(string name)
    {
        return $"Hello, {name}! Welcome to MCP stdio server.";
    }

    [McpServerTool, Description("Calculate the sum of two numbers")]
    public int CalculateSum(int a, int b)
    {
        return a + b;
    }
}
```

## Резиме

У овом ажурираном часу сте научили како да:

- Изградите MCP сервере користећи тренутни **stdio транспорт** (препоручени приступ)
- Разумете зашто је SSE транспорт застарео у корист stdio и Streamable HTTP
- Креирате алате који се могу позивати од стране MCP клијената
- Отстрањујете грешке на серверу помоћу MCP Inspector-а
- Интегришете ваш stdio сервер са VS Code-ом и Claude-ом

stdio транспорт пружа једноставнији, безбеднији и перформантнији начин изградње MCP сервера у поређењу са застарелим SSE приступом. То је препоручени транспорт за већину MCP серверских имплементација од спецификације 2025-06-18.

### .NET

1. Прво хајде да креирамо неке алате, за то ћемо направити фајл *Tools.cs* са следећим садржајем:

  ```csharp
  using System.ComponentModel;
  using System.Text.Json;
  using ModelContextProtocol.Server;
  ```

## Вежба: Тестирање вашег stdio сервера

Сада када сте направили ваш stdio сервер, хајде да га тестирамо да бисмо били сигурни да исправно ради.

### Захтеви

1. Осигурајте да имате инсталиран MCP Inspector:
   ```bash
   npm install -g @modelcontextprotocol/inspector
   ```

2. Ваш серверски код треба да буде сачуван (нпр. као `server.py`)

### Тестирање са Inspector-ом

1. **Покрените Inspector са вашим сервером**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

2. **Отворите веб интерфејс**: Inspector ће отворити прозор прегледача који приказује могућности вашег сервера.

3. **Тестирајте алате**:
   - Испробајте `get_greeting` алат са различитим именима
   - Тестирајте `calculate_sum` алат са различитим бројевима
   - Позовите `get_server_info` алат да видите метаподатке сервера

4. **Пратите комуникацију**: Inspector приказује JSON-RPC поруке које се размењују између клијента и сервера.

### Шта треба да видите

Када ваш сервер правилно покрене, требало би да видите:
- Могућности сервера наведене у Inspector-у
- Доступне алате за тестирање
- Успешну размену JSON-RPC порука
- Одговоре алата приказане у интерфејсу

### Уобичајени проблеми и решења

**Сервер се не покреће:**
- Проверите да су све зависности инсталиране: `pip install mcp`
- Проверите Python синтаксу и увлачење
- Потражите поруке о грешкама у конзоли

**Алатке се не приказују:**
- Осигурајте да су `@server.tool()` декоратори присутни
- Проверите да су функције алата дефинисане пре `main()`
- Проверите да је сервер исправно конфигурисан

**Проблеми са конекцијом:**
- Проверите да сервер правилно користи stdio транспорт
- Проверите да други процеси не ометају
- Проверите синтаксу наредбе у Inspector-у

## Задатак

Покушајте да проширите ваш сервер додатним могућностима. Погледајте [ову страницу](https://api.chucknorris.io/) да, на пример, додате алат који позива API. Ви одлучујете како ваш сервер треба да изгледа. Забавите се :)
## Решење

[Решење](./solution/README.md) Ево могућег решења са радним кодом.

## Кључне поуке

Кључне поуке из овог поглавља су следеће:

- stdio транспорт је препоручени механизам за локалне MCP сервере.
- stdio транспорт омогућава непрекинуту комуникацију између MCP сервера и клијената користећи стандардне улазне и излазне токове.
- Можете користити и Inspector и Visual Studio Code за директно коришћење stdio сервера, што олакшава отстрањивање грешака и интеграцију.

## Примери

- [Java Calculator](../samples/java/calculator/README.md)
- [.Net Calculator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Calculator](../samples/javascript/README.md)
- [TypeScript Calculator](../samples/typescript/README.md)
- [Python Calculator](../../../../03-GettingStarted/samples/python)

## Додатни ресурси

- [SSE](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events)

## Шта следи

## Следећи кораци

Сада када сте научили како да изградите MCP сервере са stdio транспортом, можете истражити напредније теме:

- **Следеће**: [HTTP Streaming са MCP (Streamable HTTP)](../06-http-streaming/README.md) - Научите о другом подржаном транспортном механизму за удаљене сервере
- **Напредно**: [MCP безбедносне добре праксе](../../02-Security/README.md) - Имплементирајте безбедност у вашим MCP серверима
- **Производња**: [Стратегије деплоја](../09-deployment/README.md) - Деплојујте ваше сервере за продукцијску употребу

## Додатни ресурси

- [MCP спецификација 2025-06-18](https://spec.modelcontextprotocol.io/specification/) - Званична спецификација
- [MCP SDK документација](https://github.com/modelcontextprotocol/sdk) - SDK референце за све језике
- [Примери из заједнице](../../06-CommunityContributions/README.md) - Више примера сервера из заједнице

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Изјава о одрицању одговорности**:
Овај документ је преведен уз помоћ АИ сервиса за превођење [Co-op Translator](https://github.com/Azure/co-op-translator). Иако настојимо да обезбедимо прецизност, молимо имајте у виду да аутоматски преводи могу садржати грешке или нетачности. Професионални човечји превод се препоручује за важне информације. Изворни документ на његовом оригиналном језику треба сматрати ауторитетним извором. Не одговарамо за било какве неспоразуме или нетачна тумачења настала коришћењем овог превода.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->