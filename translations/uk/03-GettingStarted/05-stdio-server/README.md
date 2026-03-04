# MCP сервер зі stdio транспортом

> **⚠️ Важливе оновлення**: Згідно з MCP Специфікацією 2025-06-18, автономний SSE (Server-Sent Events) транспорт був **застарілим** і замінений транспортом "Streamable HTTP". Поточна MCP специфікація визначає два основні механізми транспорту:
> 1. **stdio** - Стандартний ввід/вивід (рекомендується для локальних серверів)
> 2. **Streamable HTTP** - Для віддалених серверів, які можуть використовувати SSE внутрішньо
>
> Цей урок було оновлено, щоб зосередитися на **stdio транспорті**, який є рекомендованим підходом для більшості реалізацій MCP серверів.

Транспорт stdio дозволяє MCP серверам спілкуватися з клієнтами через стандартні потоки вводу та виводу. Це найпоширеніший і рекомендований механізм транспорту в поточній MCP специфікації, що забезпечує простий та ефективний спосіб створення MCP серверів, які легко інтегруються з різноманітними клієнтськими застосунками.

## Огляд

У цьому уроці розглядається, як створювати та споживати MCP сервери з використанням stdio транспорту.

## Цілі навчання

Наприкінці цього уроку ви зможете:

- Створити MCP сервер, використовуючи stdio транспорт.
- Відлагоджувати MCP сервер за допомогою Inspector.
- Споживати MCP сервер за допомогою Visual Studio Code.
- Розуміти поточні механізми транспорту MCP і чому stdio рекомендується.


## stdio транспорт - Як це працює

Транспорт stdio є одним з двох підтримуваних типів транспорту в поточній MCP специфікації (2025-06-18). Ось як він працює:

- **Проста комунікація**: Сервер читає повідомлення JSON-RPC з стандартного вводу (`stdin`) і надсилає повідомлення у стандартний вивід (`stdout`).
- **На основі процесів**: Клієнт запускає MCP сервер як підпроцес.
- **Формат повідомлень**: Повідомлення є окремими запитами, сповіщеннями або відповідями JSON-RPC, розділені новими рядками.
- **Логування**: Сервер МОЖЕ записувати UTF-8 рядки у стандартний потік помилок (`stderr`) для цілей логування.

### Ключові вимоги:
- Повідомлення МАЮТЬ бути розділені новими рядками і НЕ МАЮТЬ містити вбудованих нових рядків.
- Сервер НЕ МАЄ записувати в `stdout` нічого, що не є дійсним MCP повідомленням.
- Клієнт НЕ МАЄ записувати в `stdin` сервера нічого, що не є дійсним MCP повідомленням.

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

- Ми імпортуємо клас `Server` та `StdioServerTransport` з MCP SDK.
- Створюємо екземпляр сервера з базовою конфігурацією та можливостями.

### Python

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server

# Створити екземпляр сервера
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
    .WithStdioServerTransport()
    .WithTools<Tools>();

builder.Services.AddLogging(logging => logging.AddConsole());

var app = builder.Build();
await app.RunAsync();
```

Основна відмінність від SSE полягає в тому, що stdio сервери:

- Не потребують налаштування веб-сервера або HTTP кінцевих точок.
- Запускаються як підпроцеси клієнтом.
- Спілкуються через потоки stdin/stdout.
- Простіші у реалізації та відлагодженні.

## Вправа: Створення stdio сервера

Щоб створити наш сервер, потрібно мати на увазі дві речі:

- Нам потрібен веб-сервер для надання кінцевих точок для з'єднання та обміну повідомленнями.
## Лабораторна робота: Створення простого MCP stdio сервера

У цій лабораторній роботі ми створимо простий MCP сервер, використовуючи рекомендований stdio транспорт. Цей сервер надасть інструменти, які клієнти зможуть викликати, використовуючи стандартний Model Context Protocol.

### Вимоги

- Python 3.8 або новіший
- MCP Python SDK: `pip install mcp`
- Базове розуміння асинхронного програмування

Почнемо зі створення нашого першого MCP stdio сервера:

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp import types

# Налаштувати журналювання
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Створити сервер
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
    # Використовувати stdio транспорт
    async with stdio_server(server) as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            server.create_initialization_options()
        )

if __name__ == "__main__":
    asyncio.run(main())
```

## Ключові відмінності від застарілого підходу SSE

**Stdio транспорт (поточний стандарт):**
- Проста модель підпроцесів - клієнт запускає сервер як дочірній процес
- Обмін повідомленнями через stdin/stdout використовуючи JSON-RPC
- Не потрібне налаштування HTTP сервера
- Краща продуктивність і безпека
- Простота відлагодження та розробки

**SSE транспорт (застарілий станом на MCP 2025-06-18):**
- Потребував HTTP сервер з SSE кінцевими точками
- Складніше налаштування з інфраструктурою веб-сервера
- Додаткові міркування безпеки для HTTP кінцевих точок
- Зараз замінений на Streamable HTTP для веб-сценаріїв

### Створення сервера зі stdio транспортом

Для створення нашого stdio сервера потрібно:

1. **Імпортувати необхідні бібліотеки** – потрібно MCP серверні компоненти та stdio транспорт.
2. **Створити екземпляр сервера** – визначити сервер з його можливостями.
3. **Визначити інструменти** – додати функціональність, яку хочемо надавати.
4. **Налаштувати транспорт** – сконфігурувати stdio комунікацію.
5. **Запустити сервер** – стартувати сервер і обробляти повідомлення.

Збудуємо це крок за кроком:

### Крок 1: Створення базового stdio сервера

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server

# Налаштувати логування
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Створити сервер
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

### Крок 2: Додати більше інструментів

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

Збережіть код у файлі `server.py` і запустіть його через консоль:

```bash
python server.py
```

Сервер запуститься і чекатиме введення з stdin. Він спілкується через JSON-RPC повідомлення у stdio транспорті.

### Крок 4: Тестування з Inspector

Ви можете протестувати свій сервер за допомогою MCP Inspector:

1. Встановіть Inspector: `npx @modelcontextprotocol/inspector`
2. Запустіть Inspector та вкажіть на свій сервер
3. Протестуйте створені інструменти

### .NET

```csharp
var builder = WebApplication.CreateBuilder(args);
builder.Services
    .AddMcpServer();
 ```
## Відлагодження вашого stdio сервера

### Використання MCP Inspector

MCP Inspector – це цінний інструмент для відлагодження і тестування MCP серверів. Ось як ним користуватися з вашим stdio сервером:

1. **Встановіть Inspector**:
   ```bash
   npx @modelcontextprotocol/inspector
   ```

2. **Запустіть Inspector**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

3. **Протестуйте сервер**: Inspector надає веб-інтерфейс, де ви можете:
   - Переглядати можливості сервера
   - Тестувати інструменти з різними параметрами
   - Моніторити JSON-RPC повідомлення
   - Відлагоджувати проблеми з підключенням

### Використання VS Code

Ви також можете відлагоджувати MCP сервер безпосередньо у VS Code:

1. Створіть конфігурацію запуску у `.vscode/launch.json`:
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

2. Встановіть точки зупину у коді сервера
3. Запустіть відлагоджувач і тестуйте разом з Inspector

### Поширені поради для відлагодження

- Використовуйте `stderr` для логів – ніколи не пишіть у `stdout`, оскільки він зарезервований для MCP повідомлень
- Переконайтеся, що всі JSON-RPC повідомлення розділені новими рядками
- Спочатку тестуйте прості інструменти перед додаванням складної функціональності
- Використовуйте Inspector для перевірки форматів повідомлень

## Використання вашого stdio сервера у VS Code

Після того, як ви створили MCP stdio сервер, ви можете інтегрувати його з VS Code для використання з Claude або іншими MCP-сумісними клієнтами.

### Конфігурація

1. **Створіть MCP конфігураційний файл** у `%APPDATA%\Claude\claude_desktop_config.json` (Windows) або `~/Library/Application Support/Claude/claude_desktop_config.json` (Mac):

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

2. **Перезапустіть Claude**: Закрийте і відкрийте Claude знову, щоб завантажити нову конфігурацію сервера.

3. **Перевірте з'єднання**: Почніть розмову з Claude і спробуйте використовувати інструменти вашого сервера:
   - "Чи можеш ти привітатися, використовуючи інструмент привітання?"
   - "Обчисли суму 15 і 27"
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

// Додати інструменти
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

## Підсумок

У цьому оновленому уроці ви навчилися:

- Створювати MCP сервери з використанням поточного **stdio транспорту** (рекомендований підхід)
- Розуміти, чому SSE транспорт був застарілим на користь stdio та Streamable HTTP
- Створювати інструменти, які можуть викликати MCP клієнти
- Відлагоджувати сервер за допомогою MCP Inspector
- Інтегрувати stdio сервер з VS Code і Claude

Транспорт stdio надає простіший, безпечніший і продуктивніший спосіб створення MCP серверів у порівнянні з застарілим підходом SSE. Це рекомендований транспорт для більшості реалізацій MCP серверів відповідно до специфікації 2025-06-18.


### .NET

1. Спершу створимо деякі інструменти, для цього створимо файл *Tools.cs* зі наступним вмістом:

  ```csharp
  using System.ComponentModel;
  using System.Text.Json;
  using ModelContextProtocol.Server;
  ```

## Вправа: Тестування вашого stdio сервера

Тепер, коли ви створили stdio сервер, давайте перевіримо, чи він працює належним чином.

### Вимоги

1. Переконайтеся, що у вас встановлений MCP Inspector:
   ```bash
   npm install -g @modelcontextprotocol/inspector
   ```

2. Ваш код сервера має бути збережений (наприклад, як `server.py`)

### Тестування за допомогою Inspector

1. **Запустіть Inspector разом із сервером**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

2. **Відкрийте веб-інтерфейс**: Inspector відкриє браузерне вікно, що показує можливості вашого сервера.

3. **Перевірте інструменти**: 
   - Спробуйте інструмент `get_greeting` з різними іменами
   - Перевірте інструмент `calculate_sum` із різними числами
   - Викличте інструмент `get_server_info`, щоб побачити метадані сервера

4. **Моніторинг комунікації**: Inspector показує JSON-RPC повідомлення, що обмінюються між клієнтом та сервером.

### Що ви маєте побачити

Якщо сервер запускається правильно, ви побачите:
- Перелік можливостей сервера в Inspector
- Доступні інструменти для тестування
- Успішний обмін JSON-RPC повідомленнями
- Відповіді інструментів, відображені у інтерфейсі

### Поширені проблеми та рішення

**Сервер не запускається:**
- Перевірте, що всі залежності встановлені: `pip install mcp`
- Перевірте синтаксис і відступи Python
- Перегляньте повідомлення про помилки в консолі

**Інструменти не з’являються:**
- Переконайтеся, що присутні декоратори `@server.tool()`
- Перевірте, що функції інструментів визначені до `main()`
- Переконайтеся, що сервер правильно налаштований

**Проблеми з підключенням:**
- Переконайтеся, що сервер використовує stdio транспорт правильно
- Перевірте, що інші процеси не заважають
- Переконайтеся в коректності синтаксису команд Inspector

## Завдання

Спробуйте розширити свій сервер додатковими можливостями. Подивіться [цю сторінку](https://api.chucknorris.io/), щоб, наприклад, додати інструмент, який викликає API. Вирішуйте, як повинен виглядати сервер. Гарного вам настрою :)

## Розв’язок

[Розв’язок](./solution/README.md) Ось можливий розв’язок із робочим кодом.

## Основні висновки

Основні висновки з цього розділу:

- Транспорт stdio є рекомендованим механізмом для локальних MCP серверів.
- Транспорт stdio дозволяє безперешкодне спілкування між MCP серверами і клієнтами через стандартні потоки вводу і виводу.
- Ви можете користуватися як Inspector, так і Visual Studio Code, щоб напряму споживати stdio сервери, що робить відлагодження і інтеграцію простими.

## Демонстрації 

- [Java калькулятор](../samples/java/calculator/README.md)
- [.Net калькулятор](../../../../03-GettingStarted/samples/csharp)
- [JavaScript калькулятор](../samples/javascript/README.md)
- [TypeScript калькулятор](../samples/typescript/README.md)
- [Python калькулятор](../../../../03-GettingStarted/samples/python) 

## Додаткові ресурси

- [SSE](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events)

## Що далі

## Наступні кроки

Тепер, коли ви навчилися створювати MCP сервери зі stdio транспортом, ви можете дослідити більш просунуті теми:

- **Далі**: [HTTP Streaming з MCP (Streamable HTTP)](../06-http-streaming/README.md) – Дізнайтеся про інший підтримуваний механізм транспорту для віддалених серверів
- **Поглиблено**: [Кращі практики безпеки MCP](../../02-Security/README.md) – Реалізуйте безпеку у своїх MCP серверах
- **Продакшн**: [Стратегії розгортання](../09-deployment/README.md) – Розгорніть сервер для продуктивного використання

## Додаткові ресурси

- [Специфікація MCP 2025-06-18](https://spec.modelcontextprotocol.io/specification/) – Офіційна специфікація
- [Документація MCP SDK](https://github.com/modelcontextprotocol/sdk) – SDK довідники для всіх мов
- [Приклади від спільноти](../../06-CommunityContributions/README.md) – Більше прикладів серверів від спільноти

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Відмова від відповідальності**:
Цей документ був перекладений за допомогою сервісу автоматичного перекладу [Co-op Translator](https://github.com/Azure/co-op-translator). Хоча ми прагнемо до точності, будь ласка, майте на увазі, що автоматичні переклади можуть містити помилки або неточності. Оригінальний документ рідною мовою вважається авторитетним джерелом. Для критично важливої інформації рекомендується звертатися до професійного перекладача. Ми не несемо відповідальності за будь-які непорозуміння або неправильне тлумачення, що виникли внаслідок використання цього перекладу.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->