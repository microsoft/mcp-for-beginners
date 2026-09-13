# MCP сервер са stdio транспортом

> **⚠️ Важна обавештења**: Од MCP спецификације 2025-06-18, самостални SSE (Server-Sent Events) транспорт је **застарео** и замењен "Streamable HTTP" транспортом. Тренутна MCP спецификација дефинише два главна транспортна механизма:
> 1. **stdio** - Стандардни улаз/излаз (препоручен за локалне сервере)
> 2. **Streamable HTTP** - За удаљене сервере који могу користити SSE интерно
>
> Овај час је ажуриран да се фокусира на **stdio транспорт**, који је препоручен приступ за већину имплементација MCP сервера.

stdio транспорт омогућава MCP серверима комуникацију са клијентима преко стандардних улазних и излазних токова. Ово је најчешће коришћени и препоручени транспортни механизам у тренутној MCP спецификацији, који пружа једноставан и ефикасан начин за изградњу MCP сервера који се лако интегришу са различитим клијентским апликацијама.

## Преглед

Овај час обухвата како изградити и користити MCP сервере користећи stdio транспорт.

## Циљеви учења

На крају овог часа, бићете у стању да:

- Изградите MCP сервер користећи stdio транспорт.
- Отворите грешке на MCP серверу користећи Inspector.
- Користите MCP сервер у Visual Studio Code-у.
- Разумете тренутне MCP транспортне механизме и зашто је stdio препоручен.


## stdio транспорт - Како функционише

stdio транспорт је један од два стандардна транспорта у MCP спецификацији
`2026-07-28`. Ево како ради:

- **Једноставна комуникација**: Сервер чита JSON-RPC поруке из стандардног улаза (`stdin`) и шаље поруке на стандардни излаз (`stdout`).
- **На бази процеса**: Клијент покреће MCP сервер као подсистем.
- **Формат порука**: Поруке су појединачни JSON-RPC захтеви, обавештења или одговори, раздвојени ентерима.
- **Логовање**: Сервер МОЖЕ писати UTF-8 низове на стандардну грешку (`stderr`) у сврху логовања.

### Кључни захтеви:
- Поруке МОРАЈУ бити раздвојене ентерима и НЕ СМЕЈУ садржати уграђене ентере
- Сервер НЕ СМЕ писати ништа на `stdout` што није валидна MCP порука
- Клијент НЕ СМЕ писати ништа на серверов `stdin` што није валидна MCP порука

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

- Увозимо класу `Server` и `StdioServerTransport` из MCP SDK-а
- Креирамо инстанцу сервера са основним конфигурацијама и капацитетима
- Креирамо инстанцу `StdioServerTransport` и повезујемо је са сервером, омогућавајући комуникацију преко stdin/stdout

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

- Не захтевају подешавање веб сервера или HTTP endpoint-ова
- Покрећу се као подсистеми од стране клијента
- Комуницирају преко stdin/stdout токова
- Једноставнији су за имплементацију и дебаговање

## Вежба: Креирање stdio сервера

За креирање нашег сервера морамо имати у виду две ствари:

- Потребан нам је веб сервер да изложимо endpoint-ове за везу и поруке.
## Лаб: Креирање простог MCP stdio сервера

У овом лабораторијском задатку направићемо једноставан MCP сервер користећи препоручени stdio транспорт. Овај сервер ће изложити алате које клијенти могу позивати користећи стандардни Model Context Protocol.

### Захтеви

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

# Подеси праћење
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
- Једноставан модел подсистема - клијент покреће сервер као подређени процес
- Комуникација путем stdin/stdout користећи JSON-RPC поруке
- Није потребно подешавање HTTP сервера
- Боље перформансе и безбедност
- Лако дебаговање и развој

**SSE транспорт (застарео од MCP 2025-06-18):**
- Потребан HTTP сервер са SSE endpoint-овима
- Компликованије подешавање са веб сервер инфраструктуром
- Додатне безбедносне мере за HTTP endpoint-ове
- Сада замењено са Streamable HTTP за веб базиране сценарије

### Креирање сервера са stdio транспортом

Да бисмо креирали наш stdio сервер, треба:

1. **Увезите потребне библиотеке** - Потребни су нам MCP сервер компоненти и stdio транспорт
2. **Креирајте инстанцу сервера** - Дефинишите сервер са својим капацитетима
3. **Дефинишите алате** - Додајте функционалност коју желите да изложите
4. **Поставите транспорт** - Конфигуришите stdio комуникацију
5. **Покрените сервер** - Покрените сервер и обрађујте поруке

Поступно ћемо изградити ово:

### Корак 1: Креирање базичног stdio сервера

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server

# Конфигуриши евиденцију
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Креирај сервер
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

Сервер ће почети и чекати на улаз са stdin. Комуницира преко JSON-RPC порука преко stdio транспорта.

### Корак 4: Тестирање са Inspektor-ом

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

### Коришћење MCP Inspectora

MCP Inspector је вредан алат за отстрањивање грешака и тестирање MCP сервера. Ево како га користити са вашим stdio сервером:

1. **Инсталирајте Inspector**:
   ```bash
   npx @modelcontextprotocol/inspector
   ```

2. **Покрените Inspector**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

3. **Тестирајте сервер**: Inspector пружа веб интерфејс где можете:
   - Видети капацитете сервера
   - Тестирати алате са различитим параметрима
   - Пратити JSON-RPC поруке
   - Отстрањивати проблеме са везом

### Коришћење VS Code-а

Такође можете дебаговати ваш MCP сервер директно у VS Code-у:

1. Направите launch конфигурацију у `.vscode/launch.json`:
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

2. Поставите breakpoints у вашем серверском коду
3. Покрените дебагер и тестирајте помоћу Inspectora

### Уобичајени савети за дебаговање

- Користите `stderr` за логовање - никад не пишите у `stdout` јер је резервисан за MCP поруке
- Осигурајте да све JSON-RPC поруке буду раздвојене ентерима
- Прво тестирајте са једноставним алатима пре него што додате сложену функционалност
- Користите Inspector да проверите формате порука

## Коришћење вашег stdio сервера у VS Code-у

Када направите MCP stdio сервер, можете га интегрисати у VS Code да бисте га користили са Claude-ом или другим MCP компатибилним клијентима.

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

2. **Рестартујте Claude**: Затворите и поново отворите Claude да бисте учитали нову конфигурацију сервера.

3. **Тестирајте везу**: Почните разговор са Claude-ом и покушајте да користите алате вашег сервера:
   - "Можеш ли ме поздравити користећи алат за поздрав?"
   - "Израчунај збир 15 и 27"
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

У овом ажурираном часу сте научили како да:

- Изградите MCP сервере користећи тренутни **stdio транспорт** (препоручени приступ)
- Разумете зашто је SSE транспорт застарео у корист stdio и Streamable HTTP
- Креирате алате које MCP клијенти могу позивати
- Отстрањујете грешке на вашем серверу користећи MCP Inspector
- Интегришете ваш stdio сервер са VS Code-ом и Claude-ом

stdio транспорт пружа једноставнији, безбеднији и ефикаснији начин за изградњу MCP сервера у поређењу са застарелим SSE приступом. То је препоручени транспорт за већину имплементација MCP сервера од спецификације 2025-06-18.


### .NET

1. Прво хајде да направимо неке алате, за то ћемо креирати фајл *Tools.cs* са следећим садржајем:

  ```csharp
  using System.ComponentModel;
  using System.Text.Json;
  using ModelContextProtocol.Server;
  ```

## Вежба: Тестирање вашег stdio сервера

Сада када сте направили ваш stdio сервер, хајде да га тестирамо да бисмо се уверили да ради исправно.

### Захтеви

1. Осигурајте да имате инсталиран MCP Inspector:
   ```bash
   npm install -g @modelcontextprotocol/inspector
   ```

2. Ваш серверски код треба бити сачуван (нпр. као `server.py`)

### Тестирање са Inspector-ом

1. **Покрените Inspector са вашим сервером**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

2. **Отворите веб интерфејс**: Inspector ће отворити прозор прегледача који вам показује могућности вашег сервера.

3. **Тестирајте алате**: 
   - Испробајте алат `get_greeting` са различитим именима
   - Тестирајте алат `calculate_sum` са разним бројевима
   - Позовите алат `get_server_info` да видите метаподатке сервера

4. **Пратите комуникацију**: Inspector приказује JSON-RPC поруке које се размењују између клијента и сервера.

### Шта треба да видите

Када ваш сервер исправно почне, требало би да видите:
- Капацитете сервера наведене у Inspector-у
- Алате доступне за тестирање
- Успешне размене JSON-RPC порука
- Одговоре алата приказане у интерфејсу

### Уобичајени проблеми и решења

**Сервер не почиње:**
- Проверите да ли су све зависности инсталиране: `pip install mcp`
- Проверите Python синтаксу и увлачења
- Потражите поруке о грешкама у конзоли

**Алатке се не приказују:**
- Осигурајте да су присутни `@server.tool()` декоратори
- Проверите да ли су функције алата дефинисане пре `main()`
- Проверите да ли је сервер правилно конфигурисан

**Проблеми са везом:**
- Осигурајте да сервер исправно користи stdio транспорт
- Проверите да ли други процеси не ометају
- Проверите синтаксу команди Inspector-а

## Задатак

Покушајте да проширите свој сервер са више функционалности. Погледајте [ову страницу](https://api.chucknorris.io/) да бисте, на пример, додали алат који позива API. Ви одлучујете како треба да изгледа сервер. Забавите се :)
## Решење

[Решење](./solution/README.md) Ево могућег решења са радним кодом.

## Кључни закључци

Кључни закључци из овог поглавља су следећи:

- stdio транспорт је препоручени механизам за локалне MCP сервере.
- stdio транспорт омогућава беспрекорну комуникацију између MCP сервера и клијената користећи стандардне улазне и излазне токове.
- Можете користити и Inspector и Visual Studio Code за директно коришћење stdio сервера, чинећи дебаговање и интеграцију једноставним.

## Примери 

- [Java Калькулатор](../samples/java/calculator/README.md)
- [.Net Калькулатор](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Калькулатор](../samples/javascript/README.md)
- [TypeScript Калькулатор](../samples/typescript/README.md)
- [Python Калькулатор](../../../../03-GettingStarted/samples/python) 

## Додатни ресурси

- [SSE](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events)

## Шта следи

## Следећи кораци

Сада када сте научили како да правите MCP сервере са stdio транспортом, можете истражити напредније теме:

- **Следеће**: [HTTP стриминг са MCP (Streamable HTTP)](../06-http-streaming/README.md) - Сазнајте о другом подржаном транспортном механизму за удаљене сервере
- **Напредно**: [Најбоље праксе безбедности MCP-а](../../02-Security/README.md) - Имплементирајте безбедност у вашим MCP серверима
- **Продукција**: [Стратегије распоређивања](../09-deployment/README.md) - Распоредите ваше сервере за продукцијску употребу

## Додатни ресурси

- [MCP спецификација 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/) - Тренутна спецификација
- [MCP SDK документација](https://github.com/modelcontextprotocol/sdk) - SDK референтне линије за све језике
- [Примери из заједнице](../../06-CommunityContributions/README.md) - Више примера сервера из заједнице

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Изјава о одрицању одговорности**:
Овај документ је преведен коришћењем услуге за аутоматски превод [Co-op Translator](https://github.com/Azure/co-op-translator). Иако тежимо тачности, имајте у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати ауторитативним извором. За критичне информације препоручује се професионални људски превод. Нисмо одговорни за било каква неспоразума или погрешна тумачења која произилазе из коришћења овог превода.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->