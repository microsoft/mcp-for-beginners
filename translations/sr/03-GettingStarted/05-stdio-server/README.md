# MCP сервер са stdio транспортом

> **⚠️ Важна обавештења**: Од MCP спецификације 2025-06-18, самостални SSE (Server-Sent Events) транспорт је **депрецитиран** и замењен „Streamable HTTP“ транспортом. Тренутна MCP спецификација дефинише два примарна транспортна механизма:
> 1. **stdio** - Стандардни улаз/излаз (препоручен за локалне сервере)
> 2. **Streamable HTTP** - За удаљене сервере који могу користити SSE интерно
>
> Овај лекција је ажурирана да се фокусира на **stdio транспорт**, који је препоручени приступ за већину имплементација MCP сервера.

stdio транспорт омогућава MCP серверима да комуницирају са клијентима преко стандардних улазних и излазних токова. Ово је најчешће коришћени и препоручени транспортни механизам у тренутној MCP спецификацији, пружајући једноставан и ефикасан начин за прављење MCP сервера који се могу лако интегрисати са различитим клијентским апликацијама.

## Преглед

Овај лекција покрива како да направите и користите MCP сервере користећи stdio транспорт.

## Циљеви учења

До краја ове лекције, бићете у могућности да:

- Направите MCP сервер користећи stdio транспорт.
- Отстраните грешке (debug) MCP сервера користећи Inspector.
- Користите MCP сервер у Visual Studio Code.
- Разумете тренутне MCP транспортне механизме и зашто је stdio препоручен.


## stdio транспорт - Како функционише

stdio транспорт је један од два стандардна транспорта у MCP спецификацији
`2026-07-28`. Ево како функционише:

- **Једноставна комуникација**: Сервер чита JSON-RPC поруке са стандардног улаза (`stdin`) и шаље поруке на стандардни излаз (`stdout`).
- **Базиран на процесима**: Клијент покреће MCP сервер као подпроцес.
- **Формат порука**: Поруке су појединачни JSON-RPC захтеви, нотификације или одговори, одвојени новим линијама.
- **Логовање**: Сервер МОЖЕ писати UTF-8 стрингове у стандардни грешни излаз (`stderr`) у сврху логовања.

### Кључни захтеви:
- Поруке МОРАЈУ бити одвојене новим линијама и НЕ СМЕЈУ садржати уграђене нове линије
- Сервер НЕ СМЕ писати ништа у `stdout` што није валидна MCP порука
- Клијент НЕ СМЕ писати ништа у серверов `stdin` што није валидна MCP порука

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

- Импортујемо `Server` класу и `StdioServerTransport` из MCP SDK
- Креирамо пример сервера са основном конфигурацијом и способностима
- Креирамо `StdioServerTransport` инстанцу и повезујемо сервер с њом, омогућавајући комуникацију преко stdin/stdout

### Python

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server

# Create server instance
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

- Креирамо пример сервера користећи MCP SDK
- Дефинишемо алате коришћењем декоратора
- Користимо stdio_server контекст менаџер за руковање транспортом

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

Кључна разлика од SSE је да stdio сервери:

- Не захтевају подешавање веб сервера или HTTP крајњих тачака
- Покрећу се као подпроцеси од стране клијента
- Комуницирају преко stdin/stdout токова
- Једноставнији су за имплементацију и отклањање грешака

## Вежба: Креирање stdio сервера

Да бисмо направили наш сервер, морамо имати у виду две ствари:

- Морамo користити веб сервер за излагање крајњих тачака за конекцију и поруке.
## Лабораторија: Креирање једноставног MCP stdio сервера

У овој лабораторији направићемо једноставан MCP сервер користећи препоручени stdio транспорт. Овај сервер ће изложити алате које клијенти могу да позивају користећи стандардни Model Context Protocol.

### Предуслови

- Python 3.8 или новији
- MCP Python SDK: `pip install mcp`
- Основно разумевање асинхроног програмирања

Почнимо креирањем нашег првог MCP stdio сервера:

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp import types

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Create the server
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
    # Use stdio transport
    async with stdio_server(server) as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            server.create_initialization_options()
        )

if __name__ == "__main__":
    asyncio.run(main())
```

## Кључне разлике у односу на депрецитирани SSE приступ

**Stdio транспорт (тренутни стандард):**
- Једноставан модел подпроцеса - клијент покреће сервер као дечји процес
- Комуникација преко stdin/stdout коришћењем JSON-RPC порука
- Није потребно подешавање HTTP сервера
- Боље перформансе и безбедност
- Једноставније отклањање грешака и развој

**SSE транспорт (депрецитиран од MCP 2025-06-18):**
- Захтева HTTP сервер са SSE крајњим тачкама
- Компликованије подешавање са веб серверском инфраструктуром
- Додатне безбедносне препоруке за HTTP крајње тачке
- Сада замењен Streamable HTTP за веб-базиране сценарије

### Креирање сервера са stdio транспортом

Да креирамо наш stdio сервер, морамо:

1. **Импортовати потребне библиотеке** - Трбају нам MCP сервер компоненти и stdio транспорт
2. **Креирати пример сервера** - Дефинисати сервер са његовим способностима
3. **Дефинисати алате** - Додати функционалност коју желимо да изложимо
4. **Подесити транспорт** - Конфигурисати stdio комуникацију
5. **Покренути сервер** - Стартовати сервер и обрађивати поруке

Изградимо ово корак по корак:

### Корак 1: Креирање основног stdio сервера

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Create the server
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

Сервер ће почети и чекати унос са stdin-а. Комуницира користећи JSON-RPC поруке преко stdio транспорта.

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
## Отстрањивање грешака вашег stdio сервера

### Коришћење MCP Inspector-а

MCP Inspector је вредан алат за отклањање грешака и тестирање MCP сервера. Ево како да га користите са вашим stdio сервером:

1. **Инсталирајте Inspector**:
   ```bash
   npx @modelcontextprotocol/inspector
   ```

2. **Покрените Inspector**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

3. **Тестирајте сервер**: Inspector пружа веб интерфејс где можете:
   - Погледати способност сервера
   - Тестирати алате са различитим параметрима
   - Праћити JSON-RPC поруке
   - Отстрањивати проблеме са везом

### Коришћење VS Code

Такође можете одстрањивати грешке вашег MCP сервера директно у VS Code:

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

2. Поставите тачке прекида у вашем серверском коду
3. Покрените отстрањивач грешака и тествајте са Inspector-ом

### Уобичајени савети за отстрањивање грешака

- Користите `stderr` за логовање - никада не пишите у `stdout` јер је резерван за MCP поруке
- Проверите да све JSON-RPC поруке буду одвојене новим линијама
- Прво тествајте са једноставним алатима пре додавања сложеније функционалности
- Користите Inspector за проверу формата порука

## Коришћење вашег stdio сервера у VS Code

Кад направите свој MCP stdio сервер, можете га интегрисати са VS Code да га користите са Claude-ом или другим MCP-компатибилним клијентима.

### Конфигурација

1. **Креирајте MCP конфигурациони фајл** на `%APPDATA%\Claude\claude_desktop_config.json` (Windows) или `~/Library/Application Support/Claude/claude_desktop_config.json` (Mac):

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

2. **Поново покрените Claude**: Затворите и поново отворите Claude да учитате нову конфигурацију сервера.

3. **Тестирајте конекцију**: Започните разговор са Claude-ом и покушајте да користите алате вашег сервера:
   - „Можеш ли ме поздравити користећи алат за поздрав?“
   - „Израчунај збир 15 и 27“
   - „Које су информације о серверу?“

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

// Add tools
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

У овој ажурираној лекцији научили сте како да:

- Правите MCP сервере користећи тренутни **stdio транспорт** (препоручени приступ)
- Разумете зашто је SSE транспорт депрецитиран у корист stdio и Streamable HTTP
- Креирате алате које MCP клијенти могу позивати
- Отстрањујете грешке у вашем серверу коришћењем MCP Inspector
- Интегришете свој stdio сервер са VS Code и Claude-ом

stdio транспорт пружа једноставнији, безбеднији и ефикаснији начин за прављење MCP сервера у поређењу са депрецитираним SSE приступом. То је препоручени транспорт за већину имплементација MCP сервера према спецификацији од 2025-06-18.


### .NET

1. Прво направимо неке алате, за то ћемо креирати фајл *Tools.cs* са следећим садржајем:

  ```csharp
  using System.ComponentModel;
  using System.Text.Json;
  using ModelContextProtocol.Server;
  ```

## Вежба: Тестирање вашег stdio сервера

Сада када сте направили свој stdio сервер, хајде да га тестирамо да бисмо били сигурни да исправно ради.

### Предуслови

1. Проверите да ли имате инсталиран MCP Inspector:
   ```bash
   npm install -g @modelcontextprotocol/inspector
   ```

2. Ваш серверски код треба да буде сачуван (нпр. као `server.py`)

### Тестирање са Inspector-ом

1. **Покрените Inspector са вашим сервером**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

2. **Отворите веб интерфејс**: Inspector ће отворити прозор претраживача који приказује способност вашег сервера.

3. **Тестирајте алате**: 
   - Испробајте `get_greeting` алат са различитим именима
   - Тестирајте `calculate_sum` алат са различитим бројевима
   - Позовите `get_server_info` алат да видите метаподатке сервера

4. **Пратите комуникацију**: Inspector приказује JSON-RPC поруке које се размењују између клијента и сервера.

### Шта бисте требали видети

Када ваш сервер покренете исправно, требало би да видите:
- Листу способности сервера у Inspector-у
- Доступне алате за тестирање
- Успешне размјене JSON-RPC порука
- Приказане одговоре алата у интерфејсу

### Уобичајени проблеми и решења

**Сервер се не покреће:**
- Проверите да су све зависности инсталиране: `pip install mcp`
- Проверите Python синтаксу и увлачење
- Потражите поруке о грешкама у конзоли

**Алатке се не појављују:**
- Проверите да су присутни `@server.tool()` декоратори
- Проверите да су алатске функције дефинисане пре `main()`
- Проверите да је сервер исправно конфигурисан

**Проблеми са конекцијом:**
- Уверите се да сервер исправно користи stdio транспорт
- Проверите да ниједан други процес не омета
- Проверите синтаксу команде Inspector-а

## Задатак

Покушајте да изградите свој сервер са више способности. Погледајте [ову страницу](https://api.chucknorris.io/) да, на пример, додате алат који позива API. Ви одлучујете како сервер треба да изгледа. Пријатно :)
## Решење

[Решење](./solution/README.md) Ево могућег решења са радним кодом.

## Кључне поуке

Кључне поуке из овог поглавља су следеће:

- stdio транспорт је препоручени механизам за локалне MCP сервере.
- Stdio транспорт омогућава беспрекорну комуникацију између MCP сервера и клијената коришћењем стандардних улазних и излазних токова.
- Можете користити и Inspector и Visual Studio Code да бисте директно користили stdio сервере, што олакшава отклањање грешака и интеграцију.

## Примери

- [Java калкулатор](../samples/java/calculator/README.md)
- [.NET калкулатор](../../../../03-GettingStarted/samples/csharp)
- [JavaScript калкулатор](../samples/javascript/README.md)
- [TypeScript калкулатор](../samples/typescript/README.md)
- [Python калкулатор](../../../../03-GettingStarted/samples/python) 

## Додатни ресурси

- [SSE](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events)

## Шта следи

## Следећи кораци

Сада када сте научили како да правите MCP сервере са stdio транспортом, можете истражити напредније теме:

- **Следеће**: [HTTP стримовање са MCP (Streamable HTTP)](../06-http-streaming/README.md) - Сазнајте о другом подржаном транспортном механизму за удаљене сервере
- **Напредно**: [Најбоље безбедносне праксе MCP-а](../../02-Security/README.md) - Имплементирајте безбедност у вашим MCP серверима
- **Продукција**: [Стратегије распоређивања](../09-deployment/README.md) - Распоредите ваше сервере за продукционо коришћење

## Додатни ресурси

- [MCP спецификација 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/) - Тренутна спецификација
- [MCP SDK документација](https://github.com/modelcontextprotocol/sdk) - SDK референце за све језике
- [Примери из заједнице](../../06-CommunityContributions/README.md) - Више примера сервера из заједнице

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Изјава о одрицању одговорности**:
Овај документ је преведен коришћењем услуге за аутоматски превод [Co-op Translator](https://github.com/Azure/co-op-translator). Иако тежимо тачности, имајте у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати ауторитативним извором. За критичне информације препоручује се професионални људски превод. Нисмо одговорни за било каква неспоразума или погрешна тумачења која произилазе из коришћења овог превода.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->