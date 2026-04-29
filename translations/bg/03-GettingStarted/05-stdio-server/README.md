# MCP сървър с stdio транспорт

> **⚠️ Важна актуализация**: От MCP спецификация 2025-06-18, самостоятелният SSE (Server-Sent Events) транспорт е **отказан** и е заменен с "Streamable HTTP" транспорт. Текущата MCP спецификация определя два основни транспортни механизма:
> 1. **stdio** - Стандартен вход/изход (препоръчително за локални сървъри)
> 2. **Streamable HTTP** - За отдалечени сървъри, които могат да използват SSE вътрешно
>
> Този урок е актуализиран да се фокусира върху **stdio транспорта**, който е препоръчителният подход за повечето реализации на MCP сървъри.

stdio транспортът позволява на MCP сървърите да комуникират с клиентите чрез стандартните входни и изходни потоци. Това е най-често използваният и препоръчителен транспортен механизъм в текущата MCP спецификация, предоставящ прост и ефективен начин за изграждане на MCP сървъри, които лесно могат да се интегрират с различни клиентски приложения.

## Преглед

Този урок обхваща как да създадем и използваме MCP сървъри, използвайки stdio транспорта.

## Цели на обучението

В края на този урок ще можете да:

- Създавате MCP сървър с използване на stdio транспорта.
- Отстранявате грешки в MCP сървър с помощта на Inspector.
- Използвате MCP сървър с Visual Studio Code.
- Разбирате текущите MCP транспортни механизми и защо stdio е препоръчителен.

## stdio транспорт – Как работи

stdio транспортът е един от двата поддържани транспортни типа в текущата MCP спецификация (2025-06-18). Ето как работи:

- **Проста комуникация**: Сървърът чете JSON-RPC съобщения от стандартния вход (`stdin`) и изпраща съобщения към стандартния изход (`stdout`).
- **Базиран на процес**: Клиентът стартира MCP сървъра като подпроцес.
- **Формат на съобщенията**: Съобщенията са отделни JSON-RPC заявки, известия или отговори, разделени с нови редове.
- **Логиране**: Сървърът МОЖЕ да записва UTF-8 низове към стандартния поток за грешки (`stderr`) за целите на логиране.

### Основни изисквания:
- Съобщенията ТРЯБВА да са разделени с нови редове и да НЕ съдържат вмъкнати нови редове
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

В предишния код:

- Импортираме класа `Server` и `StdioServerTransport` от MCP SDK
- Създаваме инстанция на сървър с базова конфигурация и възможности
- Създаваме инстанция `StdioServerTransport` и свързваме сървъра с него, позволявайки комуникация през stdin/stdout

### Python

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server

# Създаване на инстанция на сървър
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

В предния код:

- Създаваме инстанция на сървър, използвайки MCP SDK
- Дефинираме инструменти чрез декоратори
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

Основната разлика с SSE е, че stdio сървърите:

- Не изискват настройка на уеб сървър или HTTP крайни точки
- Се стартират като подпроцеси от клиента
- Комуникират чрез stdin/stdout потоци
- Са по-прости за имплементация и отстраняване на грешки

## Упражнение: Създаване на stdio сървър

За да създадем нашия сървър, трябва да имаме предвид две неща:

- Трябва да използваме уеб сървър за експониране на крайни точки за връзка и съобщения.
## Лабораторно упражнение: Създаване на прост MCP stdio сървър

В това упражнение ще създадем прост MCP сървър с препоръчания stdio транспорт. Този сървър ще експонира инструменти, които клиентите могат да извикват с помощта на стандартизирания Model Context Protocol.

### Предварителни изисквания

- Python 3.8 или по-нова версия
- MCP Python SDK: `pip install mcp`
- Основни познания по асинхронно програмиране

Нека започнем с първия ни MCP stdio сървър:

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp import types

# Конфигуриране на регистрацията
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

## Основни разлики с отхвърления SSE подход

**Stdio транспорт (текущ стандарт):**
- Прост модел с подпроцес – клиентът стартира сървъра като дъщерен процес
- Комуникация чрез stdin/stdout с JSON-RPC съобщения
- Не е нужна настройка на HTTP сървър
- По-добра производителност и сигурност
- По-лесно отстраняване на грешки и разработка

**SSE транспорт (отхвърлен от MCP 2025-06-18):**
- Изисква HTTP сървър с SSE крайни точки
- По-сложна настройка с инфраструктура за уеб сървър
- Допълнителни съображения за сигурността на HTTP крайни точки
- Вече заменен с Streamable HTTP за уеб-базирани сценарии

### Създаване на сървър с stdio транспорт

За да създадем нашия stdio сървър, трябва да:

1. **Импортираме нужните библиотеки** - Необходими са MCP сървърните компоненти и stdio транспорт
2. **Създадем инстанция на сървър** - Дефинираме сървъра с неговите възможности
3. **Дефинираме инструменти** - Добавяме функционалността, която искаме да експонираме
4. **Настроим транспорта** - Конфигурираме stdio комуникацията
5. **Стартираме сървъра** - Започваме сървъра и обработваме съобщенията

Нека го изградим стъпка по стъпка:

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

Сървърът ще стартира и ще чака вход от stdin. Той комуникира чрез JSON-RPC съобщения през stdio транспорта.

### Стъпка 4: Тест с Inspector

Можете да тествате вашия сървър с помощта на MCP Inspector:

1. Инсталирайте Inspector: `npx @modelcontextprotocol/inspector`
2. Стартирайте Inspector и го насочете към вашия сървър
3. Тествайте инструментите, които сте създали

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

3. **Тествайте сървъра**: Inspector предоставя уеб интерфейс, където можете да:
   - Преглеждате възможностите на сървъра
   - Тествате инструментите с различни параметри
   - Наблюдавате JSON-RPC съобщенията
   - Отстранявате проблеми с връзката

### Използване на VS Code

Можете също така да отстранявате грешки на вашия MCP сървър директно във VS Code:

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

2. Задайте точки за прекъсване в кода на сървъра
3. Стартирайте дебъгъра и тествайте с Inspector

### Често срещани съвети за отстраняване на грешки

- Използвайте `stderr` за логиране – никога не пишете в `stdout`, тъй като е запазен за MCP съобщения
- Уверете се, че всички JSON-RPC съобщения са разделени с нови редове
- Тествайте първо с прости инструменти, преди да добавяте сложна функционалност
- Използвайте Inspector за проверка на формата на съобщенията

## Използване на вашия stdio сървър във VS Code

След като създадете MCP stdio сървъра си, можете да го интегрирате с VS Code, за да го използвате с Claude или други MCP-съвместими клиенти.

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
   - "Можеш ли да ме поздравиш с помощта на инструмента за поздрав?"
   - "Изчисли сумата на 15 и 27"
   - "Каква е информацията за сървъра?"

### Пример на TypeScript stdio сървър

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

### Пример на .NET stdio сървър

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

В този актуализиран урок научихте как да:

- Създавате MCP сървъри, използвайки текущия **stdio транспорт** (препоръчителен подход)
- Разбирате защо SSE транспортът е отхвърлен в полза на stdio и Streamable HTTP
- Създавате инструменти, които MCP клиентите могат да извикват
- Отстранявате грешки на вашия сървър чрез MCP Inspector
- Интегрирате вашия stdio сървър с VS Code и Claude

stdio транспортът предоставя по-прост, по-сигурен и по-производителен начин за изграждане на MCP сървъри в сравнение с отхвърления SSE подход. Той е препоръчителният транспорт за повечето реализации на MCP сървъри към спецификация 2025-06-18.

### .NET

1. Нека първо създадем някои инструменти, за това ще създадем файл *Tools.cs* със следното съдържание:

  ```csharp
  using System.ComponentModel;
  using System.Text.Json;
  using ModelContextProtocol.Server;
  ```

## Упражнение: Тест на вашия stdio сървър

Сега когато сте изградили вашия stdio сървър, нека го тестваме, за да сме сигурни, че работи правилно.

### Предварителни изисквания

1. Уверете се, че имате инсталиран MCP Inspector:
   ```bash
   npm install -g @modelcontextprotocol/inspector
   ```

2. Вашият сървърен код трябва да е запазен (например като `server.py`)

### Тест с Inspector

1. **Стартирайте Inspector с вашия сървър**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

2. **Отворете уеб интерфейса**: Inspector ще отвори прозорец на браузъра, показващ възможностите на вашия сървър.

3. **Тествайте инструментите**: 
   - Опитайте инструмента `get_greeting` с различни имена
   - Тествайте `calculate_sum` с различни числа
   - Извикайте инструмента `get_server_info`, за да видите метаданните за сървъра

4. **Наблюдавайте комуникацията**: Inspector показва JSON-RPC съобщенията, които се обменят между клиента и сървъра.

### Какво трябва да видите

При успешно стартиране на сървъра, трябва да видите:
- Възможностите на сървъра, изброени в Inspector
- Инструменти, достъпни за тест
- Успешен обмен на JSON-RPC съобщения
- Отговори от инструментите, показани във интерфейса

### Разпространени проблеми и решения

**Сървърът не стартира:**
- Проверете дали всички зависимости са инсталирани: `pip install mcp`
- Уверете се в синтаксиса и отстъпите на Python
- Проверете за съобщения за грешки в конзолата

**Инструменти не се показват:**
- Уверете се, че са налични декоратори `@server.tool()`
- Проверете дали функциите на инструментите са дефинирани преди `main()`
- Уверете се, че сървърът е правилно конфигуриран

**Проблеми с връзката:**
- Проверете дали сървърът използва правилно stdio транспорта
- Уверете се, че няма други процеси, които пречат
- Проверете синтаксиса на командата за Inspector

## Задача

Опитайте да разширите сървъра с повече възможности. Вижте [тази страница](https://api.chucknorris.io/) например, за да добавите инструмент, който извиква API. Вие решавате как да изглежда сървърът. Приятно забавление :)
## Решение

[Решение](./solution/README.md) Ето едно възможно решение с работещ код.

## Основни изводи

Основните изводи от тази глава са следните:

- stdio транспортът е препоръчителният механизъм за локални MCP сървъри.
- stdio транспортът позволява безпроблемна комуникация между MCP сървъри и клиенти, използвайки стандартните входен и изходен поток.
- Можете да използвате както Inspector, така и Visual Studio Code, за да консумирате stdio сървъри директно, което улеснява отстраняването на грешки и интеграцията.

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

След като вече научихте как да създавате MCP сървъри с stdio транспорта, можете да разгледате по-напреднали теми:

- **Следващо**: [HTTP стрийминг с MCP (Streamable HTTP)](../06-http-streaming/README.md) - Научете за другия поддържан транспортен механизъм за отдалечени сървъри
- **Напреднали**: [Най-добри практики за сигурност в MCP](../../02-Security/README.md) - Прилагане на сигурност в MCP сървърите
- **Продукция**: [Стратегии за разгръщане](../09-deployment/README.md) - Разгръщане на сървъри за продукционна употреба

## Допълнителни ресурси

- [MCP спецификация 2025-06-18](https://spec.modelcontextprotocol.io/specification/) - Официална спецификация
- [MCP SDK документация](https://github.com/modelcontextprotocol/sdk) - Референции на SDK за всички езици
- [Примери от общността](../../06-CommunityContributions/README.md) - Повече примери на сървъри от общността

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Отказ от отговорност**:  
Този документ е преведен с помощта на AI преводаческа услуга [Co-op Translator](https://github.com/Azure/co-op-translator). Въпреки че се стремим към точност, моля имайте предвид, че автоматизираните преводи могат да съдържат грешки или неточности. Оригиналният документ на неговия роден език трябва да се счита за авторитетен източник. За критична информация се препоръчва професионален човешки превод. Ние не носим отговорност за никакви недоразумения или неправилни тълкувания, произтичащи от използването на този превод.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->