# MCP сервер зі stdio транспортом

> **⚠️ Важливе оновлення**: Згідно зі специфікацією MCP від 2025-06-18, окремий транспорт SSE (Server-Sent Events) був **застарілим** і замінений на транспорт "Streamable HTTP". Поточна специфікація MCP визначає два основні механізми транспорту:
> 1. **stdio** - Стандартний ввід/вивід (рекомендований для локальних серверів)
> 2. **Streamable HTTP** - Для віддалених серверів, які можуть використовувати SSE внутрішньо
>
> Цей урок оновлено, щоб зосередитися на **stdio транспорті**, який є рекомендованим підходом для більшості реалізацій MCP серверів.

Stdio транспорт дозволяє MCP серверам спілкуватися з клієнтами через стандартні потоки вводу та виводу. Це найпоширеніший і рекомендований механізм транспорту в поточній специфікації MCP, який забезпечує простий і ефективний спосіб створення MCP серверів, що легко інтегруються з різними клієнтськими додатками.

## Огляд

Цей урок охоплює створення та використання MCP серверів за допомогою stdio транспорту.

## Цілі навчання

До кінця цього уроку ви зможете:

- Створювати MCP сервер за допомогою stdio транспорту.
- Налагоджувати MCP сервер за допомогою Inspector.
- Використовувати MCP сервер у Visual Studio Code.
- Розуміти поточні механізми транспорту MCP і чому stdio є рекомендованим.

## stdio транспорт - як це працює

Stdio транспорт є одним із двох підтримуваних типів транспорту в поточній специфікації MCP (2025-06-18). Ось як він працює:

- **Просте спілкування**: Сервер читає JSON-RPC повідомлення зі стандартного вводу (`stdin`) і надсилає повідомлення до стандартного виводу (`stdout`).
- **Процесна модель**: Клієнт запускає MCP сервер як підпроцес.
- **Формат повідомлень**: Повідомлення є окремими запитами, сповіщеннями або відповідями JSON-RPC, розділеними новими рядками.
- **Логування**: Сервер МОЖЕ записувати UTF-8 рядки до стандартного помилкового виводу (`stderr`) для логування.

### Основні вимоги:
- Повідомлення МАЮТЬ бути розділені новими рядками і НЕ МАЮТЬ містити вбудованих нових рядків.
- Сервер НЕ МАЄ записувати нічого до `stdout`, що не є дійсним MCP повідомленням.
- Клієнт НЕ МАЄ записувати нічого до `stdin` сервера, що не є дійсним MCP повідомленням.

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

У наведеному коді:

- Ми імпортуємо клас `Server` і `StdioServerTransport` з MCP SDK.
- Ми створюємо екземпляр сервера з базовою конфігурацією та можливостями.

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

У наведеному коді ми:

- Створюємо екземпляр сервера за допомогою MCP SDK.
- Визначаємо інструменти за допомогою декораторів.
- Використовуємо контекстний менеджер stdio_server для обробки транспорту.

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

Основна відмінність від SSE полягає в тому, що stdio сервери:

- Не потребують налаштування веб-сервера або HTTP кінцевих точок.
- Запускаються як підпроцеси клієнтом.
- Спілкуються через потоки stdin/stdout.
- Є простішими для реалізації та налагодження.

## Вправа: Створення stdio сервера

Щоб створити наш сервер, потрібно врахувати дві речі:

- Нам потрібно використовувати веб-сервер для відкриття кінцевих точок для з'єднання та повідомлень.

## Лабораторна робота: Створення простого MCP stdio сервера

У цій лабораторній роботі ми створимо простий MCP сервер, використовуючи рекомендований stdio транспорт. Цей сервер буде надавати інструменти, які клієнти можуть викликати за допомогою стандартного протоколу Model Context.

### Передумови

- Python 3.8 або новіший.
- MCP Python SDK: `pip install mcp`.
- Базове розуміння асинхронного програмування.

Давайте почнемо створювати наш перший MCP stdio сервер:

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

## Основні відмінності від застарілого підходу SSE

**Stdio транспорт (поточний стандарт):**
- Проста модель підпроцесів - клієнт запускає сервер як дочірній процес.
- Спілкування через stdin/stdout за допомогою JSON-RPC повідомлень.
- Немає необхідності налаштовувати веб-сервер.
- Краща продуктивність і безпека.
- Просте налагодження та розробка.

**SSE транспорт (застарілий з MCP 2025-06-18):**
- Потребував веб-сервера з SSE кінцевими точками.
- Більш складне налаштування з інфраструктурою веб-сервера.
- Додаткові міркування щодо безпеки для HTTP кінцевих точок.
- Зараз замінений на Streamable HTTP для веб-сценаріїв.

### Створення сервера зі stdio транспортом

Щоб створити наш stdio сервер, нам потрібно:

1. **Імпортувати необхідні бібліотеки** - Нам потрібні компоненти MCP сервера та stdio транспорту.
2. **Створити екземпляр сервера** - Визначити сервер з його можливостями.
3. **Визначити інструменти** - Додати функціональність, яку ми хочемо надати.
4. **Налаштувати транспорт** - Конфігурувати stdio спілкування.
5. **Запустити сервер** - Запустити сервер і обробляти повідомлення.

Давайте створимо це крок за кроком:

### Крок 1: Створення базового stdio сервера

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

### Крок 2: Додавання більше інструментів

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

### Крок 3: Запуск сервера

Збережіть код як `server.py` і запустіть його з командного рядка:

```bash
python server.py
```

Сервер запуститься і чекатиме вводу через stdin. Він спілкується за допомогою JSON-RPC повідомлень через stdio транспорт.

### Крок 4: Тестування за допомогою Inspector

Ви можете протестувати ваш сервер за допомогою MCP Inspector:

1. Встановіть Inspector: `npx @modelcontextprotocol/inspector`.
2. Запустіть Inspector і вкажіть його на ваш сервер.
3. Протестуйте створені вами інструменти.

### .NET

```csharp
var builder = WebApplication.CreateBuilder(args);
builder.Services
    .AddMcpServer();
 ```

## Налагодження вашого stdio сервера

### Використання MCP Inspector

MCP Inspector є цінним інструментом для налагодження та тестування MCP серверів. Ось як його використовувати з вашим stdio сервером:

1. **Встановіть Inspector**:
   ```bash
   npx @modelcontextprotocol/inspector
   ```

2. **Запустіть Inspector**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

3. **Протестуйте ваш сервер**: Inspector надає веб-інтерфейс, де ви можете:
   - Переглядати можливості сервера.
   - Тестувати інструменти з різними параметрами.
   - Моніторити JSON-RPC повідомлення.
   - Налагоджувати проблеми з'єднання.

### Використання VS Code

Ви також можете налагоджувати ваш MCP сервер безпосередньо у VS Code:

1. Створіть конфігурацію запуску в `.vscode/launch.json`:
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

2. Встановіть точки зупинки у вашому коді сервера.
3. Запустіть налагоджувач і протестуйте за допомогою Inspector.

### Загальні поради щодо налагодження

- Використовуйте `stderr` для логування - ніколи не записуйте до `stdout`, оскільки він зарезервований для MCP повідомлень.
- Переконайтеся, що всі JSON-RPC повідомлення розділені новими рядками.
- Спочатку тестуйте прості інструменти, перш ніж додавати складну функціональність.
- Використовуйте Inspector для перевірки форматів повідомлень.

## Використання вашого stdio сервера у VS Code

Після створення MCP stdio сервера ви можете інтегрувати його з VS Code для використання з Claude або іншими клієнтами, сумісними з MCP.

### Конфігурація

1. **Створіть конфігураційний файл MCP** у `%APPDATA%\Claude\claude_desktop_config.json` (Windows) або `~/Library/Application Support/Claude/claude_desktop_config.json` (Mac):

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

2. **Перезапустіть Claude**: Закрийте та відкрийте Claude, щоб завантажити нову конфігурацію сервера.

3. **Протестуйте з'єднання**: Почніть розмову з Claude і спробуйте використовувати інструменти вашого сервера:
   - "Можеш привітати мене за допомогою інструменту привітання?"
   - "Обчисли суму 15 і 27."
   - "Яка інформація про сервер?"

### Приклад stdio сервера на TypeScript

Ось повний приклад на TypeScript для довідки:

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

### Приклад stdio сервера на .NET

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

## Підсумок

У цьому оновленому уроці ви дізналися, як:

- Створювати MCP сервери, використовуючи поточний **stdio транспорт** (рекомендований підхід).
- Розуміти, чому транспорт SSE був застарілим на користь stdio і Streamable HTTP.
- Створювати інструменти, які можуть викликати MCP клієнти.
- Налагоджувати ваш сервер за допомогою MCP Inspector.
- Інтегрувати ваш stdio сервер з VS Code і Claude.

Stdio транспорт забезпечує простіший, більш безпечний і продуктивний спосіб створення MCP серверів порівняно із застарілим підходом SSE. Це рекомендований транспорт для більшості реалізацій MCP серверів згідно зі специфікацією 2025-06-18.

### .NET

1. Спочатку створимо кілька інструментів, для цього створимо файл *Tools.cs* з наступним вмістом:

  ```csharp
  using System.ComponentModel;
  using System.Text.Json;
  using ModelContextProtocol.Server;
  ```

## Вправа: Тестування вашого stdio сервера

Тепер, коли ви створили ваш stdio сервер, давайте протестуємо його, щоб переконатися, що він працює правильно.

### Передумови

1. Переконайтеся, що MCP Inspector встановлений:
   ```bash
   npm install -g @modelcontextprotocol/inspector
   ```

2. Ваш код сервера має бути збережений (наприклад, як `server.py`).

### Тестування за допомогою Inspector

1. **Запустіть Inspector з вашим сервером**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

2. **Відкрийте веб-інтерфейс**: Inspector відкриє вікно браузера, де будуть показані можливості вашого сервера.

3. **Протестуйте інструменти**:
   - Спробуйте інструмент `get_greeting` з різними іменами.
   - Протестуйте інструмент `calculate_sum` з різними числами.
   - Викличте інструмент `get_server_info`, щоб побачити метадані сервера.

4. **Моніторинг спілкування**: Inspector показує JSON-RPC повідомлення, які обмінюються між клієнтом і сервером.

### Що ви повинні побачити

Коли ваш сервер запускається правильно, ви повинні побачити:
- Список можливостей сервера в Inspector.
- Інструменти, доступні для тестування.
- Успішний обмін JSON-RPC повідомленнями.
- Відповіді інструментів, показані в інтерфейсі.

### Загальні проблеми та рішення

**Сервер не запускається:**
- Перевірте, чи всі залежності встановлені: `pip install mcp`.
- Переконайтеся у правильності синтаксису Python і відступів.
- Перегляньте повідомлення про помилки в консолі.

**Інструменти не з'являються:**
- Переконайтеся, що присутні декоратори `@server.tool()`.
- Перевірте, чи функції інструментів визначені перед `main()`.
- Переконайтеся, що сервер налаштований правильно.

**Проблеми з'єднання:**
- Переконайтеся, що сервер правильно використовує stdio транспорт.
- Перевірте, чи інші процеси не заважають.
- Переконайтеся у правильності синтаксису команди Inspector.

## Завдання

Спробуйте розширити ваш сервер, додавши більше можливостей. Наприклад, використовуйте [цю сторінку](https://api.chucknorris.io/), щоб додати інструмент, який викликає API. Ви вирішуєте, як виглядатиме сервер. Удачі :)

## Рішення

[Рішення](./solution/README.md) Ось можливе рішення з робочим кодом.

## Основні висновки

Основні висновки з цього розділу:

- Stdio транспорт є рекомендованим механізмом для локальних MCP серверів.
- Stdio транспорт дозволяє безперешкодне спілкування між MCP серверами і клієнтами за допомогою стандартних потоків вводу та виводу.
- Ви можете використовувати як Inspector, так і Visual Studio Code для прямого використання stdio серверів, що робить налагодження та інтеграцію простими.

## Зразки

- [Java Calculator](../samples/java/calculator/README.md)
- [.Net Calculator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Calculator](../samples/javascript/README.md)
- [TypeScript Calculator](../samples/typescript/README.md)
- [Python Calculator](../../../../03-GettingStarted/samples/python) 

## Додаткові ресурси

- [SSE](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events)

## Що далі

## Наступні кроки

Тепер, коли ви дізналися, як створювати MCP сервери зі stdio транспортом, ви можете дослідити більш складні теми:

- **Далі**: [HTTP Streaming з MCP (Streamable HTTP)](../06-http-streaming/README.md) - Дізнайтеся про інший підтримуваний механізм транспорту для віддалених серверів.
- **Розширено**: [Найкращі практики безпеки MCP](../../02-Security/README.md) - Реалізуйте безпеку у ваших MCP серверах.
- **Виробництво**: [Стратегії розгортання](../09-deployment/README.md) - Розгорніть ваші сервери для використання у виробництві.

## Додаткові ресурси

- [Специфікація MCP 2025-06-18](https://spec.modelcontextprotocol.io/specification/) - Офіційна специфікація.
- [Документація MCP SDK](https://github.com/modelcontextprotocol/sdk) - Посилання на SDK для всіх мов.
- [Приклади спільноти](../../06-CommunityContributions/README.md) - Більше прикладів серверів від спільноти.

---

**Відмова від відповідальності**:  
Цей документ був перекладений за допомогою сервісу автоматичного перекладу [Co-op Translator](https://github.com/Azure/co-op-translator). Хоча ми прагнемо до точності, будь ласка, майте на увазі, що автоматичні переклади можуть містити помилки або неточності. Оригінальний документ на його рідній мові слід вважати авторитетним джерелом. Для критичної інформації рекомендується професійний людський переклад. Ми не несемо відповідальності за будь-які непорозуміння або неправильні тлумачення, що виникають внаслідок використання цього перекладу.