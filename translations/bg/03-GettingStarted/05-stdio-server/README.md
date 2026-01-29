# MCP Server със stdio транспорт

> **⚠️ Важна актуализация**: От MCP спецификацията 2025-06-18, самостоятелният SSE (Server-Sent Events) транспорт е **отхвърлен** и заменен с "Streamable HTTP" транспорт. Текущата MCP спецификация дефинира два основни транспортни механизма:
> 1. **stdio** - Стандартен вход/изход (препоръчителен за локални сървъри)
> 2. **Streamable HTTP** - За отдалечени сървъри, които могат да използват SSE вътрешно
>
> Този урок е актуализиран, за да се фокусира върху **stdio транспорт**, който е препоръчителният подход за повечето MCP сървърни реализации.

Stdio транспортът позволява MCP сървърите да комуникират с клиенти чрез стандартни входни и изходни потоци. Това е най-често използваният и препоръчителен транспортен механизъм в текущата MCP спецификация, предоставящ прост и ефективен начин за изграждане на MCP сървъри, които лесно могат да бъдат интегрирани с различни клиентски приложения.

## Преглед

Този урок обхваща как да изградите и използвате MCP сървъри с stdio транспорт.

## Цели на обучението

До края на този урок ще можете:

- Да изградите MCP сървър с stdio транспорт.
- Да дебъгвате MCP сървър с Inspector.
- Да използвате MCP сървър с Visual Studio Code.
- Да разберете текущите MCP транспортни механизми и защо stdio е препоръчителен.

## stdio транспорт - Как работи

Stdio транспортът е един от двата поддържани типа транспорт в текущата MCP спецификация (2025-06-18). Ето как работи:

- **Проста комуникация**: Сървърът чете JSON-RPC съобщения от стандартния вход (`stdin`) и изпраща съобщения към стандартния изход (`stdout`).
- **Процесно-базиран**: Клиентът стартира MCP сървъра като подпроцес.
- **Формат на съобщенията**: Съобщенията са индивидуални JSON-RPC заявки, известия или отговори, разделени с нови редове.
- **Логване**: Сървърът МОЖЕ да записва UTF-8 низове към стандартния грешен поток (`stderr`) за целите на логването.

### Основни изисквания:
- Съобщенията ТРЯБВА да бъдат разделени с нови редове и НЕ ТРЯБВА да съдържат вложени нови редове.
- Сървърът НЕ ТРЯБВА да записва нищо в `stdout`, което не е валидно MCP съобщение.
- Клиентът НЕ ТРЯБВА да записва нищо в `stdin` на сървъра, което не е валидно MCP съобщение.

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

В предходния код:

- Импортираме класа `Server` и `StdioServerTransport` от MCP SDK.
- Създаваме сървърна инстанция с базова конфигурация и възможности.

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

В предходния код:

- Създаваме сървърна инстанция с MCP SDK.
- Дефинираме инструменти с помощта на декоратори.
- Използваме контекстния мениджър stdio_server за управление на транспорта.

### .NET

```csharp
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;
using Microsoft.Extensions.Logging;
using ModelContextProtocol.Server;

var builder = Host.CreateApplicationBuilder(args);

builder.Services
    .AddMcpServer()
    .WithStdioTransport()
    .WithTools<Tools>();

builder.Services.AddLogging(logging => logging.AddConsole());

var app = builder.Build();
await app.RunAsync();
```

Основната разлика от SSE е, че stdio сървърите:

- Не изискват настройка на уеб сървър или HTTP крайни точки.
- Се стартират като подпроцеси от клиента.
- Комуникират чрез stdin/stdout потоци.
- Са по-прости за имплементация и дебъгване.

## Упражнение: Създаване на stdio сървър

За да създадем нашия сървър, трябва да имаме предвид две неща:

- Трябва да използваме уеб сървър за излагане на крайни точки за връзка и съобщения.

## Лаборатория: Създаване на прост MCP stdio сървър

В тази лаборатория ще създадем прост MCP сървър, използвайки препоръчания stdio транспорт. Този сървър ще излага инструменти, които клиентите могат да извикват, използвайки стандартния Model Context Protocol.

### Предварителни изисквания

- Python 3.8 или по-нова версия.
- MCP Python SDK: `pip install mcp`.
- Основни познания за асинхронно програмиране.

Нека започнем със създаването на нашия първи MCP stdio сървър:

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

## Основни разлики от отхвърления SSE подход

**Stdio транспорт (текущ стандарт):**
- Прост модел на подпроцеси - клиентът стартира сървъра като дъщерен процес.
- Комуникация чрез stdin/stdout, използвайки JSON-RPC съобщения.
- Не се изисква настройка на HTTP сървър.
- По-добра производителност и сигурност.
- По-лесно дебъгване и разработка.

**SSE транспорт (отхвърлен от MCP 2025-06-18):**
- Изискваше HTTP сървър с SSE крайни точки.
- По-сложна настройка с инфраструктура на уеб сървър.
- Допълнителни съображения за сигурност за HTTP крайни точки.
- Сега заменен със Streamable HTTP за уеб-базирани сценарии.

### Създаване на сървър със stdio транспорт

За да създадем нашия stdio сървър, трябва да:

1. **Импортираме необходимите библиотеки** - Нуждаем се от MCP сървърните компоненти и stdio транспорт.
2. **Създадем сървърна инстанция** - Дефинираме сървъра с неговите възможности.
3. **Дефинираме инструменти** - Добавяме функционалност, която искаме да изложим.
4. **Настроим транспорта** - Конфигурираме stdio комуникацията.
5. **Стартираме сървъра** - Започваме сървъра и обработваме съобщения.

Нека изградим това стъпка по стъпка:

### Стъпка 1: Създаване на базов stdio сървър

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

### Стъпка 2: Добавяне на повече инструменти

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

Сървърът ще започне и ще чака вход от stdin. Той комуникира чрез JSON-RPC съобщения през stdio транспорт.

### Стъпка 4: Тестване с Inspector

Можете да тествате вашия сървър, използвайки MCP Inspector:

1. Инсталирайте Inspector: `npx @modelcontextprotocol/inspector`.
2. Стартирайте Inspector и го насочете към вашия сървър.
3. Тествайте инструментите, които сте създали.

### .NET

```csharp
var builder = WebApplication.CreateBuilder(args);
builder.Services
    .AddMcpServer();
 ```

## Дебъгване на вашия stdio сървър

### Използване на MCP Inspector

MCP Inspector е ценен инструмент за дебъгване и тестване на MCP сървъри. Ето как да го използвате с вашия stdio сървър:

1. **Инсталирайте Inspector**:
   ```bash
   npx @modelcontextprotocol/inspector
   ```

2. **Стартирайте Inspector**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

3. **Тествайте вашия сървър**: Inspector предоставя уеб интерфейс, където можете:
   - Да видите възможностите на сървъра.
   - Да тествате инструменти с различни параметри.
   - Да наблюдавате JSON-RPC съобщения.
   - Да дебъгвате проблеми с връзката.

### Използване на VS Code

Можете също да дебъгвате вашия MCP сървър директно в VS Code:

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

2. Поставете точки за прекъсване в кода на сървъра.
3. Стартирайте дебъгера и тествайте с Inspector.

### Общи съвети за дебъгване

- Използвайте `stderr` за логване - никога не пишете в `stdout`, тъй като той е запазен за MCP съобщения.
- Уверете се, че всички JSON-RPC съобщения са разделени с нови редове.
- Тествайте с прости инструменти, преди да добавите сложна функционалност.
- Използвайте Inspector, за да проверите формата на съобщенията.

## Използване на вашия stdio сървър в VS Code

След като сте изградили вашия MCP stdio сървър, можете да го интегрирате с VS Code, за да го използвате с Claude или други MCP-съвместими клиенти.

### Конфигурация

1. **Създайте MCP конфигурационен файл** в `%APPDATA%\Claude\claude_desktop_config.json` (Windows) или `~/Library/Application Support/Claude/claude_desktop_config.json` (Mac):

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
   - "Можеш ли да ме поздравиш, използвайки инструмента за поздрав?"
   - "Изчисли сумата на 15 и 27."
   - "Каква е информацията за сървъра?"

### TypeScript stdio сървър пример

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

### .NET stdio сървър пример

```csharp
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;
using Microsoft.Extensions.Logging;
using ModelContextProtocol.Server;
using System.ComponentModel;

var builder = Host.CreateApplicationBuilder(args);

builder.Services
    .AddMcpServer()
    .WithStdioTransport()
    .WithTools<Tools>();

var app = builder.Build();
await app.RunAsync();

public class Tools
{
    [Description("Get a personalized greeting")]
    public string GetGreeting(string name)
    {
        return $"Hello, {name}! Welcome to MCP stdio server.";
    }

    [Description("Calculate the sum of two numbers")]
    public int CalculateSum(int a, int b)
    {
        return a + b;
    }
}
```

## Обобщение

В този актуализиран урок научихте как да:

- Изграждате MCP сървъри, използвайки текущия **stdio транспорт** (препоръчителен подход).
- Разберете защо SSE транспортът беше отхвърлен в полза на stdio и Streamable HTTP.
- Създавате инструменти, които могат да бъдат извиквани от MCP клиенти.
- Дебъгвате вашия сървър, използвайки MCP Inspector.
- Интегрирате вашия stdio сървър с VS Code и Claude.

Stdio транспортът предоставя по-прост, по-сигурен и по-производителен начин за изграждане на MCP сървъри в сравнение с отхвърления SSE подход. Това е препоръчителният транспорт за повечето MCP сървърни реализации според спецификацията от 2025-06-18.

### .NET

1. Нека първо създадем някои инструменти. За това ще създадем файл *Tools.cs* със следното съдържание:

  ```csharp
  using System.ComponentModel;
  using System.Text.Json;
  using ModelContextProtocol.Server;
  ```

## Упражнение: Тестване на вашия stdio сървър

Сега, когато сте изградили вашия stdio сървър, нека го тестваме, за да се уверим, че работи правилно.

### Предварителни изисквания

1. Уверете се, че MCP Inspector е инсталиран:
   ```bash
   npm install -g @modelcontextprotocol/inspector
   ```

2. Вашият сървърен код трябва да бъде запазен (например като `server.py`).

### Тестване с Inspector

1. **Стартирайте Inspector с вашия сървър**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

2. **Отворете уеб интерфейса**: Inspector ще отвори прозорец на браузъра, показващ възможностите на вашия сървър.

3. **Тествайте инструментите**: 
   - Опитайте инструмента `get_greeting` с различни имена.
   - Тествайте инструмента `calculate_sum` с различни числа.
   - Извикайте инструмента `get_server_info`, за да видите метаданни за сървъра.

4. **Наблюдавайте комуникацията**: Inspector показва JSON-RPC съобщенията, които се обменят между клиента и сървъра.

### Какво трябва да видите

Когато вашият сървър стартира правилно, трябва да видите:
- Списък с възможностите на сървъра в Inspector.
- Инструменти, достъпни за тестване.
- Успешен обмен на JSON-RPC съобщения.
- Отговори на инструменти, показани в интерфейса.

### Чести проблеми и решения

**Сървърът не стартира:**
- Проверете дали всички зависимости са инсталирани: `pip install mcp`.
- Уверете се в синтаксиса и отстъпите на Python.
- Потърсете съобщения за грешки в конзолата.

**Инструментите не се появяват:**
- Уверете се, че декораторите `@server.tool()` са налични.
- Проверете дали функциите на инструментите са дефинирани преди `main()`.
- Уверете се, че сървърът е правилно конфигуриран.

**Проблеми с връзката:**
- Уверете се, че сървърът използва stdio транспорт правилно.
- Проверете дали няма други процеси, които пречат.
- Уверете се в синтаксиса на командата за Inspector.

## Задача

Опитайте да разширите вашия сървър с повече възможности. Вижте [тази страница](https://api.chucknorris.io/), за да добавите, например, инструмент, който извиква API. Вие решавате как да изглежда сървърът. Забавлявайте се :)

## Решение

[Решение](./solution/README.md) Ето възможно решение с работещ код.

## Основни изводи

Основните изводи от тази глава са следните:

- Stdio транспортът е препоръчителният механизъм за локални MCP сървъри.
- Stdio транспортът позволява безпроблемна комуникация между MCP сървъри и клиенти, използвайки стандартни входни и изходни потоци.
- Можете да използвате както Inspector, така и Visual Studio Code, за да използвате stdio сървъри директно, което прави дебъгването и интеграцията лесни.

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

Сега, когато сте научили как да изграждате MCP сървъри със stdio транспорт, можете да изследвате по-напреднали теми:

- **Следващо**: [HTTP Streaming с MCP (Streamable HTTP)](../06-http-streaming/README.md) - Научете за другия поддържан транспортен механизъм за отдалечени сървъри.
- **Напреднало**: [MCP Security Best Practices](../../02-Security/README.md) - Имплементирайте сигурност във вашите MCP сървъри.
- **Производство**: [Стратегии за разгръщане](../09-deployment/README.md) - Разгръщайте вашите сървъри за производствена употреба.

## Допълнителни ресурси

- [MCP Спецификация 2025-06-18](https://spec.modelcontextprotocol.io/specification/) - Официална спецификация.
- [MCP SDK Документация](https://github.com/modelcontextprotocol/sdk) - SDK референции за всички езици.
- [Примери от общността](../../06-CommunityContributions/README.md) - Още примери за сървъри от общността.

---

**Отказ от отговорност**:  
Този документ е преведен с помощта на AI услуга за превод [Co-op Translator](https://github.com/Azure/co-op-translator). Въпреки че се стремим към точност, моля, имайте предвид, че автоматизираните преводи може да съдържат грешки или неточности. Оригиналният документ на неговия роден език трябва да се счита за авторитетен източник. За критична информация се препоръчва професионален човешки превод. Ние не носим отговорност за недоразумения или погрешни интерпретации, произтичащи от използването на този превод.