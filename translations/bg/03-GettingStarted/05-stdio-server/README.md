# MCP сървър с stdio трансорт

> **⚠️ Важно обновление**: От MCP спецификация 2025-06-18, самостоятелният SSE (Server-Sent Events) трансорт е **отменен** и заменен с “Streamable HTTP” трансорт. Текущата MCP спецификация дефинира два основни транспортни механизма:
> 1. **stdio** - стандартен вход/изход (препоръчва се за локални сървъри)
> 2. **Streamable HTTP** - за отдалечени сървъри, които могат да използват SSE вътрешно
>
> Този урок е обновен, за да се фокусира върху **stdio транспорта**, който е препоръчваният подход за повечето MCP сървърни реализации.

stdio транспортът позволява на MCP сървъри да комуникират с клиенти чрез стандартните входни и изходни потоци. Това е най-често използваният и препоръчителен транспортен механизъм в текущата MCP спецификация, който предоставя прост и ефективен начин за изграждане на MCP сървъри, които могат лесно да се интегрират с различни клиентски приложения.

## Преглед

Този урок разглежда как да се изградят и използват MCP сървъри с stdio транспорт.

## Учебни цели

Към края на този урок ще можете да:

- Създавате MCP сървър с stdio транспорт.
- Отстранявате грешки в MCP сървър с Inspector.
- Използвате MCP сървър с Visual Studio Code.
- Разбирате текущите MCP транспортни механизми и защо stdio е препоръчителен.

## stdio транспорт - Как работи

stdio транспортът е един от двата поддържани транспорта в текущата MCP спецификация (2025-06-18). Ето как работи:

- **Проста комуникация**: Сървърът чете JSON-RPC съобщения от стандартния вход (`stdin`) и изпраща съобщения към стандартния изход (`stdout`).
- **Базиран на процеси**: Клиентът стартира MCP сървъра като подпроцес.
- **Формат на съобщенията**: Съобщенията са отделни JSON-RPC заявки, нотификации или отговори, разделени с нови редове.
- **Логиране**: Сървърът МОЖЕ да записва UTF-8 низове в стандартната грешка (`stderr`) за логване.

### Ключови изисквания:
- Съобщенията ТРЯБВА да са разделени с нов ред и НЯМАТ право да съдържат скрити нови редове в себе си
- Сървърът НЕ ТРЯБВА да пише нищо в `stdout`, което не е валидно MCP съобщение
- Клиентът НЕ ТРЯБВА да пише в `stdin` на сървъра невалидни MCP съобщения

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

В горния код:

- Импортираме клас `Server` и `StdioServerTransport` от MCP SDK
- Създаваме инстанция на сървър с базова конфигурация и възможности

### Python

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server

# Създайте инстанция на сървъра
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

В горния код:

- Създаваме инстанция на сървър чрез MCP SDK
- Дефинираме инструменти чрез декоратори
- Използваме контекстния мениджър stdio_server за обработка на транспорта

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

Основната разлика от SSE е, че stdio сървърите:

- Не изискват настройка на уеб сървър или HTTP крайни точки
- Се стартират като под-процеси от клиента
- Комуникират чрез stdin/stdout потоци
- Са по-прости за имплементиране и отстраняване на грешки

## Упражнение: Създаване на stdio сървър

За да създадем нашия сървър, трябва да имаме предвид две неща:

- Необходимо е да използваме уеб сървър, за да изложим крайни точки за връзка и съобщения.

## Лаб: Създаване на прост MCP stdio сървър

В този лабораторен урок ще създадем прост MCP сървър, използващ препоръчителния stdio транспорт. Този сървър ще изложи инструменти, които клиентите могат да извикват чрез стандартния Model Context Protocol.

### Изисквания

- Python 3.8 или по-нова версия
- MCP Python SDK: `pip install mcp`
- Основни познания по асинхронно програмиране

Нека започнем със създаването на първия MCP stdio сървър:

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp import types

# Конфигуриране на регистрирането
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
    # Използване на stdio транспорт
    async with stdio_server(server) as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            server.create_initialization_options()
        )

if __name__ == "__main__":
    asyncio.run(main())
```

## Основни разлики от вече отхвърления SSE подход

**Stdio транспорт (текущ стандарт):**
- Прост модел с под-процеси - клиентът стартира сървъра като детски процес
- Комуникация през stdin/stdout с JSON-RPC съобщения
- Не се изисква настройка на HTTP сървър
- По-добра производителност и сигурност
- По-лесно отстраняване на грешки и разработка

**SSE транспорт (отхвърлен след MCP 2025-06-18):**
- Изисква HTTP сървър със SSE крайни точки
- По-сложна настройка с уеб сървърна инфраструктура
- Допълнителни мерки за сигурност при HTTP крайни точки
- Заменен е с Streamable HTTP за уеб-базирани сценарии

### Създаване на сървър със stdio транспорт

За да създадем нашия stdio сървър, трябва да:

1. **Импортираме нужните библиотеки** - нуждаем се от MCP сървърните компоненти и stdio транспорт
2. **Създадем инстанция на сървъра** - дефинираме сървъра със способностите му
3. **Дефинираме инструменти** - добавяме функционалността, която искаме да изложим
4. **Настроим транспорта** - конфигурираме stdio комуникацията
5. **Стартираме сървъра** - пускаме сървъра и обработваме съобщенията

Нека го направим стъпка по стъпка:

### Стъпка 1: Създаване на базов stdio сървър

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server

# Конфигуриране на регистрирането
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

Сървърът ще стартира и ще чака вход от stdin. Той комуникира с JSON-RPC съобщения през stdio транспорта.

### Стъпка 4: Тестване с Inspector

Можете да тествате сървъра си чрез MCP Inspector:

1. Инсталирайте Inspector: `npx @modelcontextprotocol/inspector`
2. Стартирайте Inspector и го насочете към вашия сървър
3. Тествайте създадените инструменти

### .NET

```csharp
var builder = WebApplication.CreateBuilder(args);
builder.Services
    .AddMcpServer();
 ```
## Отстраняване на грешки в stdio сървъра

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

3. **Тествайте сървъра си**: Inspector предоставя уеб интерфейс, където можете да:
   - Видите възможностите на сървъра
   - Тествате инструментите с различни параметри
   - Следите JSON-RPC съобщенията
   - Отстранявате проблеми с връзката

### Използване на VS Code

Можете също така да отстранявате грешки на MCP сървъра директно във VS Code:

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

2. Поставете точки за спиране в кода на сървъра
3. Стартирайте дебъгера и тествайте с Inspector

### Чести съвети за дебъгване

- Използвайте `stderr` за логване - никога не пишете в `stdout`, той е запазен за MCP съобщения
- Уверете се, че всички JSON-RPC съобщения са разделени с нов ред
- Тествайте първо с прости инструменти, преди да добавяте сложна функционалност
- Използвайте Inspector, за да проверите формата на съобщенията

## Използване на вашия stdio сървър във VS Code

След като сте създали MCP stdio сървър, можете да го интегрирате с VS Code, за да го използвате с Claude или други MCP-съвместими клиенти.

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

2. **Рестартирайте Claude**: Затворете и отворете отново Claude, за да заредите новата конфигурация за сървър.

3. **Тествайте връзката**: Започнете разговор с Claude и опитайте инструментите на вашия сървър:
   - „Можеш ли да ме поздравиш с помощта на инструмента за поздрав?“
   - „Изчисли сумата на 15 и 27“
   - „Каква е информацията за сървъра?“

### Пример за TypeScript stdio сървър

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

### Пример за .NET stdio сървър

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

## Обобщение

В този обновен урок вие научихте как да:

- Създавате MCP сървъри, използвайки текущия **stdio транспорт** (препоръчителен подход)
- Разберете защо SSE транспортът беше отменен в полза на stdio и Streamable HTTP
- Създавате инструменти, които могат да се извикват от MCP клиенти
- Отстранявате грешки в сървъра с MCP Inspector
- Интегрирате stdio сървъра си с VS Code и Claude

stdio транспортът предлага по-прост, по-сигурен и по-производителен начин за създаване на MCP сървъри в сравнение с отменения SSE подход. Той е препоръчителният транспорт за повечето MCP сървърни реализации в спецификация 2025-06-18.


### .NET

1. Нека първо създадем някои инструменти, за това ще създадем файл *Tools.cs* със следното съдържание:

  ```csharp
  using System.ComponentModel;
  using System.Text.Json;
  using ModelContextProtocol.Server;
  ```

## Упражнение: Тестване на вашия stdio сървър

След като сте създали вашия stdio сървър, нека го тестваме, за да сме сигурни, че работи коректно.

### Изисквания

1. Уверете се, че имате инсталиран MCP Inspector:
   ```bash
   npm install -g @modelcontextprotocol/inspector
   ```

2. Уверете се, че кодът на сървъра е запазен (например като `server.py`)

### Тестване с Inspector

1. **Стартирайте Inspector с вашия сървър**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

2. **Отворете уеб интерфейса**: Inspector ще отвори браузър с показани възможностите на сървъра ви.

3. **Тествайте инструментите**:
   - Опитайте инструмента `get_greeting` с различни имена
   - Тествайте инструмента `calculate_sum` с различни числа
   - Извикайте инструмента `get_server_info`, за да видите метаданни за сървъра

4. **Следете комуникацията**: Inspector показва JSON-RPC съобщенията, които се обменят между клиента и сървъра.

### Какво трябва да видите

Когато сървърът стартира правилно, трябва да видите:
- Изброени способности на сървъра в Inspector
- Налични инструменти за тестване
- Успешен обмен на JSON-RPC съобщения
- Отговори на инструментите показани в интерфейса

### Чести проблеми и решения

**Сървърът не стартира:**
- Проверете дали всички зависимости са инсталирани: `pip install mcp`
- Проверете синтаксиса и отстъпите в Python
- Потърсете грешки в конзолата

**Инструментите не се показват:**
- Уверете се, че имате декоратори `@server.tool()`
- Проверете дали функциите за инструментите са дефинирани преди `main()`
- Уверете се, че сървърът е правилно конфигуриран

**Проблеми с връзката:**
- Уверете се, че сървърът използва правилно stdio транспорта
- Проверете дали няма други процеси, които пречат
- Проверете синтаксиса на командата за Inspector

## Задача

Опитайте да разширите сървъра си с повече възможности. Вижте [тази страница](https://api.chucknorris.io/), за да добавите например инструмент, който извиква API. Вие решавате как да изглежда сървърът. Весело забавление :)

## Решение

[Решение](./solution/README.md) Ето възможно решение с работещ код.

## Ключови изводи

Основните изводи от този раздел са:

- stdio транспортът е препоръчаният механизъм за локални MCP сървъри.
- Stdio транспортът позволява безпроблемна комуникация между MCP сървърите и клиентите чрез стандартните вход и изход.
- Можете да използвате както Inspector, така и Visual Studio Code, за да консумирате stdio сървъри директно, което прави отстраняването на грешки и интеграцията лесни.

## Примери 

- [Java Калькулатор](../samples/java/calculator/README.md)
- [.Net Калькулатор](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Калькулатор](../samples/javascript/README.md)
- [TypeScript Калькулатор](../samples/typescript/README.md)
- [Python Калькулатор](../../../../03-GettingStarted/samples/python) 

## Допълнителни ресурси

- [SSE](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events)

## Какво следва

## Следващи стъпки

Сега, когато знаете как да изграждате MCP сървъри със stdio транспорт, можете да разгледате по-напреднали теми:

- **Следващо**: [HTTP поточно предаване с MCP (Streamable HTTP)](../06-http-streaming/README.md) - Научете за другия поддържан транспортен механизъм за отдалечени сървъри
- **Напреднали**: [Най-добри практики за сигурност на MCP](../../02-Security/README.md) - Имплементирайте сигурност във вашите MCP сървъри
- **Производство**: [Стратегии за внедряване](../09-deployment/README.md) - Разполагайте сървърите си за продукционна употреба

## Допълнителни ресурси

- [MCP спецификация 2025-06-18](https://spec.modelcontextprotocol.io/specification/) - Официална спецификация
- [MCP SDK документация](https://github.com/modelcontextprotocol/sdk) - SDK справочници за всички езици
- [Примери от общността](../../06-CommunityContributions/README.md) - Още сървърни примери от общността

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Отказ от отговорност**:
Този документ е преведен с помощта на AI преводачна услуга [Co-op Translator](https://github.com/Azure/co-op-translator). Въпреки че се стремим към точност, имайте предвид, че автоматизираните преводи могат да съдържат грешки или неточности. Оригиналният документ на неговия роден език трябва да се счита за авторитетен източник. За критична информация се препоръчва професионален човешки превод. Ние не носим отговорност за никакви недоразумения или неправилни тълкувания, произтичащи от използването на този превод.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->