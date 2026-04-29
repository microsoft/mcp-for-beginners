# MCP сервер са stdio транспортом

> **⚠️ Важна ажурирања**: Од MCP спецификације 2025-06-18, самостални SSE (Server-Sent Events) транспорт је **застарео** и замењен је „Streamable HTTP“ транспортом. Тренутна MCP спецификација дефинише два основна транспортна механизма:
> 1. **stdio** - Стандардни улаз/излаз (препоручено за локалне сервере)
> 2. **Streamable HTTP** - За удаљене сервере који могу користити SSE интерно
>
> Ова лекција је ажурирана да се фокусира на **stdio транспорт**, који је препоручени приступ за већину MCP серверских имплементација.

Stdio транспорт омогућава MCP серверима да комуницирају са клијентима преко стандардних улазних и излазних токова. Ово је најчешће коришћени и препоручени транспортни механизам у тренутној MCP спецификацији, пружајући једноставан и ефикасан начин за изградњу MCP сервера који се могу лако интегрисати са различитим клијентским апликацијама.

## Преглед

Ова лекција покрива како изградити и користити MCP сервере користећи stdio транспорт.

## Циљеви учења

До краја ове лекције, моћи ћете да:

- Изградите MCP сервер користећи stdio транспорт.
- Отстраните грешке на MCP серверу користећи Inspector.
- Користите MCP сервер у Visual Studio Code-у.
- Разумете тренутне MCP транспортне механизме и зашто је stdio препоручен.


## stdio транспорт - Како ради

Stdio транспорт је један од два подржана типа транспорта у тренутној MCP спецификацији (2025-06-18). Ево како функционише:

- **Једноставна комуникација**: Сервер чита JSON-RPC поруке са стандардног улаза (`stdin`) и шаље поруке на стандардни излаз (`stdout`).
- **Процесно засновано**: Клијент покреће MCP сервер као подсистемски процес.
- **Формат порука**: Поруке су појединачни JSON-RPC захтеви, нотификације или одговори, раздвојени новим редом.
- **Логовање**: Сервер МОЖЕ писати UTF-8 стрингове на стандардни грешка (`stderr`) у сврху логовања.

### Кључни захтеви:
- Поруке МОРАЈУ бити раздвојене новим редовима и НЕ СМЕЈУ садржавати уграђене нове редове
- Сервер НЕ СМЕ писати било шта на `stdout` што није важећа MCP порука
- Клијент НЕ СМЕ писати било шта серверовом `stdin` што није важећа MCP порука

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

async function runServer() {
  const transport = new StdioServerTransport();
  await server.connect(transport);
}

runServer().catch(console.error);
```

У претходном коду:

- Увозимо класу `Server` и `StdioServerTransport` из MCP SDK
- Креирамо инстанцу сервера са основном конфигурацијом и способностима
- Креирамо инстанцу `StdioServerTransport` и повезујемо сервер са њом, омогућавајући комуникацију преко stdin/stdout

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

У претходном коду ми:

- Креирамо инстанцу сервера користећи MCP SDK
- Дефинишемо алате помоћу декоратора
- Користимо stdio_server context менаџер за руковање транспортом

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
- Покрећу се као подсистемски процеси од стране клијента
- Комуницирају преко stdin/stdout токова
- Једноставнији су за имплементацију и отстрањивање грешака

## Вежба: Креирање stdio сервера

Да бисмо креирали наш сервер, морамо имати на уму две ствари:

- Потребно је користити веб сервер за излагање крајњих тачака за везу и поруке.
## Лаб: Креирање једноставног MCP stdio сервера

У овом лабу ћемо креирати једноставан MCP сервер користећи препоручени stdio транспорт. Овај сервер ће излагати алате које клијенти могу позивати користећи стандардни Model Context Protocol.

### Захтеви

- Python 3.8 или новији
- MCP Python SDK: `pip install mcp`
- Основно разумевање асинхроног програмирања

Хајде да почнемо креирањем нашег првог MCP stdio сервера:

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp import types

# Конфигуриши евиденцију
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Креирај сервер
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
    # Користи stdio транспорт
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
- Једноставан модел подсистема - клијент покреће сервер као дечији процес
- Комуникација преко stdin/stdout користећи JSON-RPC поруке
- Није потребно подешавање HTTP сервера
- Боље перформансе и безбедност
- Лакше отстрањивање грешака и развој

**SSE транспорт (застарео од MCP 2025-06-18):**
- Захтевао HTTP сервер са SSE крајњим тачкама
- Компликованије подешавање са веб сервер инфраструктуром
- Допунске безбедносне мере за HTTP крајње тачке
- Сада је замењен Streamable HTTP за веб сценарије

### Креирање сервера са stdio транспортом

Да бисмо креирали наш stdio сервер, морамо:

1. **Увезти потребне библиотеке** - Потребни су нам MCP серверски компоненти и stdio транспорт
2. **Креирати инстанцу сервера** - Дефинисати сервер са његовим способностима
3. **Дефинисати алате** - Додати функционалности које желимо да изложимо
4. **Подесити транспорт** - Конфигурисати stdio комуникацију
5. **Покренути сервер** - Старовати сервер и обрађивати поруке

Хајде да ово градимо корак по корак:

### Корак 1: Креирање основног stdio сервера

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server

# Конфигуришите логовање
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

Сачувајте код као `server.py` и покрените га са командне линије:

```bash
python server.py
```

Сервер ће започети и чекати улаз са stdin. Комуницира користећи JSON-RPC поруке преко stdio транспорта.

### Корак 4: Тестирање са Inspector-ом

Можете тестирати свој сервер користећи MCP Inspector:

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

### Користећи MCP Inspector

MCP Inspector је вриједан алат за отстрањивање грешака и тестирање MCP сервера. Ево како га користити са вашим stdio сервером:

1. **Инсталирајте Inspector**:
   ```bash
   npx @modelcontextprotocol/inspector
   ```

2. **Покрените Inspector**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

3. **Тестирајте сервер**: Inspector пружа веб интерфејс у коме можете:
   - Видети способности сервера
   - Тестирати алате са различитим параметрима
   - Пратити JSON-RPC поруке
   - Отстрањивати проблеме са везом

### Коришћење VS Code-а

Такође можете отстрањивати грешке свог MCP сервера директно у VS Code-у:

1. Креирајте launch конфигурацију у `.vscode/launch.json`:
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

2. Поставите breakpoint-ове у код сервера
3. Покрените дебагер и тестирајте са Inspector-ом

### Чести савети за отстрањивање грешака

- Користите `stderr` за логовање - никад не пишите на `stdout` јер је резервисан за MCP поруке
- Уверите се да су све JSON-RPC поруке раздвојене новим редовима
- Прво тестирајте једноставне алате пре додавања сложенијих функционалности
- Користите Inspector да проверите формате порука

## Користите свој stdio сервер у VS Code-у

Након што сте изградили свој MCP stdio сервер, можете га интегрисати са VS Code-ом ради коришћења са Claude-ом или другим MCP компатибилним клијентима.

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

2. **Поново покрените Claude**: Затворите и поново отворите Claude да бисте учитали нову конфигурацију сервера.

3. **Тестирајте везу**: Започните разговор са Claude-ом и испробајте алате вашег сервера:
   - "Можеш ли ме поздравити користећи алат за поздрав?"
   - "Израчунај збир од 15 и 27"
   - "Које су информације о серверу?"

### Пример TypeScript stdio сервера

Ево комплетног TypeScript примера за референцу:

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

У обновљеној лекцији сте научили како:

- Изградити MCP сервере користећи тренутни **stdio транспорт** (препоручени приступ)
- Разумети зашто је SSE транспорт застарео у корист stdio и Streamable HTTP транспорта
- Креирати алате које MCP клијенти могу позивати
- Отстранити грешке вашег сервера користећи MCP Inspector
- Интегрисати свој stdio сервер са VS Code-ом и Claude-ом

Stdio транспорт пружа једноставнији, сигурнији и перформантнији начин изградње MCP сервера у односу на застарели SSE приступ. То је препоручени транспорт за већину MCP серверских имплементација од спецификације 2025-06-18.


### .NET

1. Хајде прво да креирамо неке алате, за то ћемо направити фајл *Tools.cs* са следећим садржајем:

  ```csharp
  using System.ComponentModel;
  using System.Text.Json;
  using ModelContextProtocol.Server;
  ```

## Вежба: Тестирање вашег stdio сервера

Сада када сте изградили своје stdio сервер, хајде да га тестирамо како бисмо били сигурни да исправно ради.

### Захтеви

1. Уверите се да имате инсталиран MCP Inspector:
   ```bash
   npm install -g @modelcontextprotocol/inspector
   ```

2. Ваш серверски код треба да буде сачуван (нпр. као `server.py`)

### Тестирање са Inspector-ом

1. **Покрените Inspector са вашим сервером**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

2. **Отворите веб интерфејс**: Inspector ће отворити прозор претраживача који приказује способности вашег сервера.

3. **Тестирајте алате**: 
   - Испробајте алат `get_greeting` са различитим именима
   - Тестирајте алат `calculate_sum` са различитим бројевима
   - Позовите алат `get_server_info` да видите метаподатке сервера

4. **Пратите комуникацију**: Inspector приказује JSON-RPC поруке које се размењују између клијента и сервера.

### Шта би требало да видите

Када ваш сервер исправно покрене, требало би да видите:
- Листу способности сервера у Inspector-у
- Доступне алате за тестирање
- Успешне размене JSON-RPC порука
- Одговоре алата приказане у интерфејсу

### Чести проблеми и решења

**Сервер неће да стартује:**
- Проверите да ли су све зависности инсталиране: `pip install mcp`
- Проверите синтаксу и увлачење у Python-у
- Потражите поруке о грешкама у конзоли

**Алатке не приказују:**
- Уверите се да су присутни `@server.tool()` декоратори
- Проверите да су функције алата дефинисане пре `main()`
- Потврдите да је сервер правилно конфигурисан

**Проблеми са везом:**
- Проверите да ли сервер користи stdio транспорт исправно
- Проверите да ли други процеси не ометају рад
- Потврдите исправност синтаксе команде за Inspector

## Задаци

Покушајте да проширите свој сервер са више способности. Погледајте [ову страницу](https://api.chucknorris.io/) да додате алат који позива неки API. Ви одлучујете како ће сервер изгледати. Забавите се :)
## Решење

[Решење](./solution/README.md) Ево могућег решења са радним кодом.

## Кључне поуке

Кључне поуке из овог поглавља су следеће:

- stdio транспорт је препоручени механизам за локалне MCP сервере.
- Stdio транспорт омогућава беспрекорну комуникацију између MCP сервера и клијената користећи стандардне улазне и излазне токове.
- Можете користити и Inspector и Visual Studio Code за директно коришћење stdio сервера, што олакшава отстрањивање грешака и интеграцију.

## Примери

- [Java калкулатор](../samples/java/calculator/README.md)
- [.Net калкулатор](../../../../03-GettingStarted/samples/csharp)
- [JavaScript калкулатор](../samples/javascript/README.md)
- [TypeScript калкулатор](../samples/typescript/README.md)
- [Python калкулатор](../../../../03-GettingStarted/samples/python) 

## Додатни ресурси

- [SSE](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events)

## Шта следи

## Следећи кораци

Сада када сте научили како да градите MCP сервере са stdio транспортом, можете истражити напредније теме:

- **Следеће**: [HTTP Streaming са MCP (Streamable HTTP)](../06-http-streaming/README.md) - Сазнајте о другом подржаном транспортном механизму за удаљене сервере
- **Напредно**: [MCP најбоље праксе безбедности](../../02-Security/README.md) - Имплементирајте безбедност на својим MCP серверима
- **За производњу**: [Стратегије размештања](../09-deployment/README.md) - Размештајте сервере за продукцијску употребу

## Додатни ресурси

- [MCP спецификација 2025-06-18](https://spec.modelcontextprotocol.io/specification/) - Званична спецификација
- [MCP SDK документација](https://github.com/modelcontextprotocol/sdk) - SDK референце за све језике
- [Примери из заједнице](../../06-CommunityContributions/README.md) - Више сервера из заједнице

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Одрицање од одговорности**:  
Овај документ је преведен уз коришћење AI преводилачке услуге [Co-op Translator](https://github.com/Azure/co-op-translator). Иако тежимо прецизности, молимо вас да имате у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на изворном језику треба сматрати ауторитетним извором. За критичне информације препоручује се професионални људски превод. Нисмо одговорни за било каква неспоразума или погрешна тумачења која произилазе из употребе овог превода.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->