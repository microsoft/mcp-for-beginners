# MCP сървър с stdio транспорт

> **⚠️ Важно обновление**: От MCP спецификация 2025-06-18, самостоятелният SSE (Server-Sent Events) транспорт е **премахнат** и заменен с „Streamable HTTP“ транспорт. Текущата MCP спецификация определя два основни транспортни механизма:
> 1. **stdio** - Стандартен вход/изход (препоръчително за локални сървъри)
> 2. **Streamable HTTP** - За отдалечени сървъри, които могат да използват SSE вътрешно
>
> Този урок е обновен, за да се фокусира върху **stdio транспорта**, който е препоръчаният подход за повечето реализации на MCP сървъри.

stdio транспортът позволява на MCP сървърите да комуникират с клиентите чрез стандартни входни и изходни потоци. Това е най-често използваният и препоръчван транспортен механизъм в текущата MCP спецификация, предоставящ прост и ефективен начин за изграждане на MCP сървъри, които могат лесно да се интегрират с различни клиентски приложения.

## Преглед

Този урок обяснява как да изградите и използвате MCP сървъри, използвайки stdio транспорт.

## Учебни цели

Към края на този урок ще можете да:

- Изградите MCP сървър с използване на stdio транспорта.
- Отстраните грешки на MCP сървър с помощта на Inspector.
- Използвате MCP сървър чрез Visual Studio Code.
- Разберете текущите MCP транспортни механизми и защо stdio е препоръчван.


## stdio транспорт – Как работи

stdio транспортът е един от двата стандартни транспорта в MCP Спецификация
`2026-07-28`. Ето как работи:

- **Проста комуникация**: Сървърът чете JSON-RPC съобщения от стандартен вход (`stdin`) и изпраща съобщения към стандартен изход (`stdout`).
- **Базиран на процеси**: Клиентът стартира MCP сървъра като подпроцес.
- **Формат на съобщения**: Съобщенията са отделни JSON-RPC заявки, уведомления или отговори, разделени с нов ред.
- **Логване**: Сървърът МОЖЕ да записва UTF-8 низове в стандартен грешен изход (`stderr`) за целите на логването.

### Основни изисквания:
- Съобщенията ТРЯБВА да са разделени с нови редове и НЕ ТРЯБВА да съдържат вложени нови редове
- Сървърът НЕ ТРЯБВА да записва нищо в `stdout`, което не е валидно MCP съобщение
- Клиентът НЕ ТРЯБВА да записва нищо в `stdin` на сървъра, което не е валидно MCP съобщение

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

В кода по-горе:

- Импортираме класа `Server` и `StdioServerTransport` от MCP SDK
- Създаваме сървърна инстанция с базова конфигурация и възможности
- Създаваме инстанция на `StdioServerTransport` и свързваме сървъра към нея, позволявайки комуникация през stdin/stdout

### Python

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server

# Създаване на инстанция на сървъра
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

В кода по-горе:

- Създаваме сървърна инстанция с помощта на MCP SDK
- Дефинираме инструменти с декоратори
- Използваме контекстния мениджър stdio_server за управление на транспорта

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

Ключовата разлика от SSE е, че stdio сървърите:

- Не изискват настройка на уеб сървър или HTTP крайни точки
- Се стартират като подпроцеси от клиента
- Комуникират чрез stdin/stdout потоци
- Са по-прости за реализиране и дебъгване

## Упражнение: Създаване на stdio сървър

За създаването на нашия сървър трябва да имаме предвид две неща:

- Трябва да използваме уеб сървър, за да експонираме крайни точки за връзка и съобщения.
## Лаборатория: Създаване на прост MCP stdio сървър


В тази лаборатория ще създадем прост MCP сървър, използвайки препоръчания stdio транспорт. Този сървър ще предоставя инструменти, които клиентите могат да извикват чрез стандартния Model Context Protocol.

### Предварителни изисквания

- Python 3.8 или по-нова версия
- MCP Python SDK: `pip install mcp`
- Основни познания по асинхронно програмиране

Нека започнем със създаването на нашия първи MCP stdio сървър:

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp import types

# Конфигуриране на логването
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Създаване на сървъра
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
    # Използване на stdio трансфер
    async with stdio_server(server) as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            server.create_initialization_options()
        )

if __name__ == "__main__":
    asyncio.run(main())
```

## Ключови разлики от остарелия SSE подход

**Stdio транспорт (текущ стандарт):**
- Прост модел с подсистема - клиентът стартира сървъра като дъщерен процес
- Комуникация през stdin/stdout с JSON-RPC съобщения
- Не е необходима настройка на HTTP сървър
- По-добра производителност и сигурност
- По-лесно отстраняване на грешки и разработка

**SSE транспорт (остарял от MCP 2025-06-18):**
- Изисква HTTP сървър със SSE крайни точки
- По-сложна настройка с уеб сървър инфраструктура
- Допълнителни съображения за сигурност за HTTP крайни точки
- Сега заменен със Streamable HTTP за уеб базирани сценарии

### Създаване на сървър с stdio транспорт

За да създадем нашия stdio сървър, трябва да:

1. **Импортираме необходимите библиотеки** - Нуждаем се от MCP сървър компонентите и stdio транспорт
2. **Създадем сървър инстанция** - Дефинираме сървъра с неговите възможности
3. **Дефинираме инструменти** - Добавяме функционалността, която искаме да предоставим
4. **Настроим транспорта** - Конфигурираме stdio комуникация
5. **Стартираме сървъра** - Пускане на сървъра и обработка на съобщения

Нека изградим това стъпка по стъпка:

### Стъпка 1: Създаване на базов stdio сървър

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server

# Конфигуриране на логването
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Създаване на сървъра
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

### Стъпка 2: Добавяне на още инструменти

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

### Стъпка 3: Стартиране на сървъра

Запазете кода като `server.py` и го стартирайте от командния ред:

```bash
python server.py
```

Сървърът ще стартира и ще чака въвеждане от stdin. Той комуникира чрез JSON-RPC съобщения през stdio транспорта.

### Стъпка 4: Тестване с Inspector

Можете да тествате своя сървър, използвайки MCP Inspector:

1. Инсталирайте Inspector: `npx @modelcontextprotocol/inspector`
2. Стартирайте Inspector и го насочете към вашия сървър
3. Тествайте инструментите, които сте създали

### .NET

```csharp
var builder = WebApplication.CreateBuilder(args);
builder.Services
    .AddMcpServer();
 ```
## Отстраняване на грешки при вашия stdio сървър

### Използване на MCP Inspector

MCP Inspector е ценен инструмент за отстраняване на грешки и тестване на MCP сървъри. Ето как да го използвате с вашия stdio сървър:

1. **Инсталирайте Inspector**:
   ```bash
   npx @modelcontextprotocol/inspector
   ```

2. **Стартирайте Inspector**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

3. **Тествайте вашия сървър**: Inspector предоставя уеб интерфейс, където можете да:
   - Видите възможностите на сървъра
   - Тествате инструменти с различни параметри
   - Наблюдавате JSON-RPC съобщения
   - Отстранявате проблеми с връзката

### Използване на VS Code

Можете също да отстранявате грешки на MCP сървъра директно във VS Code:

1. Създайте конфигурация за стартиране в `.vscode/launch.json`:
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

2. Задайте точки на прекъсване в кода на сървъра
3. Стартирайте debugger-а и тествайте с Inspector

### Общи съвети за отстраняване на грешки

- Използвайте `stderr` за логове – никога не пишете в `stdout`, тъй като е запазен за MCP съобщения
- Уверете се, че всички JSON-RPC съобщения са разделени със символ за нов ред
- Първо тествайте с прости инструменти преди да добавяте сложна функционалност

- Използвайте Инспектора, за да проверите формати на съобщения

## Използване на вашия stdio сървър във VS Code


След като изградите своя MCP stdio сървър, можете да го интегрирате с VS Code, за да го използвате с Claude или други MCP-съвместими клиенти.

### Конфигурация

1. **Създайте MCP конфигурационен файл** на `%APPDATA%\Claude\claude_desktop_config.json` (Windows) или `~/Library/Application Support/Claude/claude_desktop_config.json` (Mac):

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

2. **Рестартирайте Claude**: Затворете и отворете отново Claude, за да заредите новата конфигурация на сървъра.

3. **Тествайте връзката**: Започнете разговор с Claude и опитайте да използвате инструментите на вашия сървър:
   - "Можеш ли да ме поздравиш с помощта на инструмента за поздрав?"
   - "Изчисли сумата на 15 и 27"
   - "Каква е информацията за сървъра?"

### Пример за stdio сървър на TypeScript

Ето пълен пример на TypeScript за справка:

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

// Добавяне на инструменти
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

### Пример за stdio сървър на .NET

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

## Резюме

В този обновен урок научихте как да:

- Изграждате MCP сървъри, използвайки текущия **stdio транспорт** (препоръчителен подход)
- Разбирате защо SSE транспортът беше отпаднат в полза на stdio и Streamable HTTP
- Създавате инструменти, които могат да се извикват от MCP клиенти
- Отстранявате грешки на вашия сървър чрез MCP инспектора
- Интегрирате своя stdio сървър с VS Code и Claude

StdIo транспортът осигурява по-прост, по-сигурен и по-ефективен начин за създаване на MCP сървъри в сравнение с отпадналия SSE подход. Той е препоръчителният транспорт за повечето реализации на MCP сървъри според спецификацията от 18-06-2025.


### .NET

1. Нека първо създадем някои инструменти, за това ще създадем файл *Tools.cs* със съдържание:

  ```csharp
  using System.ComponentModel;
  using System.Text.Json;
  using ModelContextProtocol.Server;
  ```

## Упражнение: Тествайте своя stdio сървър

След като изградихте своя stdio сървър, нека го тестваме, за да сме сигурни, че работи правилно.

### Предварителни условия

1. Уверете се, че имате инсталиран MCP Inspector:
   ```bash
   npm install -g @modelcontextprotocol/inspector
   ```

2. Вашият сървърен код трябва да е запазен (напр. като `server.py`)

### Тестване с Inspector

1. **Стартирайте Inspector със своя сървър**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

2. **Отворете уеб интерфейса**: Inspector ще отвори браузър и ще покаже възможностите на вашия сървър.

3. **Тествайте инструментите**: 
   - Опитайте инструмента `get_greeting` с различни имена
   - Тествайте инструмента `calculate_sum` с различни числа
   - Извикайте инструмента `get_server_info`, за да видите метаданните на сървъра

4. **Наблюдавайте комуникацията**: Inspector показва JSON-RPC съобщенията, обменяни между клиента и сървъра.

### Какво трябва да видите

Когато сървърът стартира правилно, трябва да видите:
- Изброени възможности на сървъра в Inspector
- Налични инструменти за тестване
- Успешен обмен на JSON-RPC съобщения
- Отговори от инструментите, показани в интерфейса

### Чести проблеми и решения

**Сървърът не стартира:**
- Проверете дали всички зависимости са инсталирани: `pip install mcp`
- Проверете синтаксиса и отстъпите на Python
- Потърсете съобщения за грешки в конзолата

**Инструментите не се появяват:**
- Уверете се, че са налични декораторите `@server.tool()`
- Проверете дали функциите за инструментите са дефинирани преди `main()`
- Уверете се, че сървърът е правилно конфигуриран

**Проблеми с връзката:**
- Проверете дали сървърът използва правилно stdio транспорта
- Уверете се, че няма други процеси, които пречат
- Потвърдете синтаксиса на командите за Inspector

## Задача

Опитайте да разширите своя сървър с повече възможности. Вижте [тази страница](https://api.chucknorris.io/), за да добавите например инструмент, който извиква API. Вие решавате как да изглежда сървърът. Забавлявайте се :)
## Решение

[Решение](./solution/README.md) Ето едно възможно решение с работещ код.

## Основни изводи

Основните изводи от тази глава са следните:

- StdIo транспортът е препоръчаният механизъм за локални MCP сървъри.
- StdIo транспортът позволява безпроблемна комуникация между MCP сървъри и клиенти чрез стандартни входни и изходни потоци.
- Можете да използвате както Inspector, така и Visual Studio Code, за да консумирате stdio сървъри директно, което прави отстраняването на грешки и интеграцията лесни.

## Примери 

- [Java Calculator](../samples/java/calculator/README.md)
- [.Net Calculator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Calculator](../samples/javascript/README.md)
- [TypeScript Calculator](../samples/typescript/README.md)
- [Python Calculator](../../../../03-GettingStarted/samples/python) 

## Допълнителни ресурси

- [SSE](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events)

## Какво следва

## Следващи стъпки

След като научихте как да изграждате MCP сървъри с stdio транспорта, можете да разгледате по-напреднали теми:

- **Следващо**: [HTTP Streaming с MCP (Streamable HTTP)](../06-http-streaming/README.md) - Научете за другия поддържан транспортен механизъм за отдалечени сървъри
- **Разширено**: [Най-добри практики за сигурност на MCP](../../02-Security/README.md) - Прилагане на сигурност в MCP сървърите
- **Производствено**: [Стратегии за внедряване](../09-deployment/README.md) - Внедряване на сървъри за производствена употреба

## Допълнителни ресурси

- [Спецификация MCP 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/) - Текуща спецификация
- [MCP SDK документация](https://github.com/modelcontextprotocol/sdk) - SDK препратки за всички езици
- [Примери от общността](../../06-CommunityContributions/README.md) - Повече примери за сървъри от общността

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Отказ от отговорност**:
Този документ е преведен с помощта на AI преводачески услуга [Co-op Translator](https://github.com/Azure/co-op-translator). Въпреки че се стремим към точност, моля имайте предвид, че автоматизираните преводи могат да съдържат грешки или неточности. Оригиналният документ на неговия роден език трябва да се счита за авторитетен източник. За критична информация се препоръчва професионален човешки превод. Ние не носим отговорност за каквито и да е недоразумения или неправилни тълкувания, произтичащи от използването на този превод.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->