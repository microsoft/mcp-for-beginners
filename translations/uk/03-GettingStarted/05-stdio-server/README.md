# MCP сервер зі stdio транспортом

> **⚠️ Важливе оновлення**: Станом на специфікацію MCP 2025-06-18, автономний SSE (Server-Sent Events) транспорт було **знято з підтримки** і замінено на транспорт "Streamable HTTP". Поточна специфікація MCP визначає два основні механізми транспорту:
> 1. **stdio** - стандартний ввід/вивід (рекомендовано для локальних серверів)
> 2. **Streamable HTTP** - для віддалених серверів, які можуть внутрішньо використовувати SSE
>
> Цей урок оновлено для фокусу на **stdio транспорті**, який є рекомендованим підходом для більшості реалізацій MCP серверів.

Транспорт stdio дозволяє MCP серверам спілкуватися з клієнтами через стандартні потоки вводу та виводу. Це найпоширеніший та рекомендований механізм транспорту у поточній специфікації MCP, що забезпечує простий та ефективний спосіб побудови MCP серверів, які можуть легко інтегруватися з різними клієнтськими застосунками.

## Огляд

У цьому уроці розглядається, як будувати та використовувати MCP сервери з використанням stdio транспорту.

## Навчальні цілі

Після завершення цього уроку ви зможете:

- Створювати MCP сервер з використанням stdio транспорту.
- Налагоджувати MCP сервер за допомогою Inspector.
- Використовувати MCP сервер у Visual Studio Code.
- Розуміти поточні механізми транспорту MCP і чому stdio рекомендовано.

## stdio Транспорт – Як це працює

Транспорт stdio є одним із двох підтримуваних типів транспорту у поточній специфікації MCP (2025-06-18). Ось як це працює:

- **Проста комунікація**: сервер читає JSON-RPC повідомлення зі стандартного вводу (`stdin`) і надсилає повідомлення у стандартний вивід (`stdout`).
- **Процесно-орієнтований**: клієнт запускає MCP сервер як дочірній процес.
- **Формат повідомлень**: повідомлення є окремими JSON-RPC запитами, повідомленнями або відповідями, розділеними новими рядками.
- **Логування**: сервер МОЖЕ записувати рядки у кодуванні UTF-8 у стандартний потік помилок (`stderr`) для цілей логування.

### Основні вимоги:
- Повідомлення МАЮТЬ бути розділені новими рядками і НЕ МАЮТЬ містити вбудованих нових рядків
- Сервер НЕ МАЄ писати у `stdout` нічого, що не є дійсним MCP повідомленням
- Клієнт НЕ МАЄ писати у `stdin` сервера нічого, що не є дійсним MCP повідомленням

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

У наведеному коді:

- Імпортуємо клас `Server` та `StdioServerTransport` з MCP SDK
- Створюємо екземпляр сервера з базовою конфігурацією та можливостями
- Створюємо екземпляр `StdioServerTransport` і підключаємо до нього сервер, що дозволяє спілкуватися через stdin/stdout

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

- Створюємо екземпляр сервера, використовуючи MCP SDK
- Визначаємо інструменти за допомогою декораторів
- Використовуємо менеджер контексту stdio_server для обробки транспорту

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

Ключова відмінність від SSE полягає в тому, що stdio сервери:

- Не вимагають налаштування веб-сервера або HTTP кінцевих точок
- Запускаються як дочірні процеси клієнтом
- Спілкуються через потоки stdin/stdout
- Є простішими для реалізації та налагодження

## Вправа: Створення stdio сервера

Для створення сервера ми повинні пам’ятати дві речі:

- Ми повинні використовувати веб-сервер для відкриття кінцевих точок для підключення та повідомлень.
## Лабораторна робота: Створення простого MCP stdio сервера

У цій лабораторній роботі ми створимо простий MCP сервер із рекомендованим stdio транспортом. Цей сервер відкриватиме інструменти, які клієнти можуть викликати, використовуючи стандартний Model Context Protocol.

### Вимоги

- Python 3.8 або вище
- MCP Python SDK: `pip install mcp`
- Базове розуміння асинхронного програмування

Почнемо з створення нашого першого MCP stdio сервера:

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
    # Використовувати транспорт stdio
    async with stdio_server(server) as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            server.create_initialization_options()
        )

if __name__ == "__main__":
    asyncio.run(main())
```

## Основні відмінності від застарілого SSE підходу

**Stdio Транспорт (поточний стандарт):**
- Простий модель дочірнього процесу - клієнт запускає сервер як дочірній процес
- Спілкування через stdin/stdout за допомогою JSON-RPC повідомлень
- Не потрібно налаштовувати HTTP сервер
- Краща продуктивність та безпека
- Простіше налагодження та розробка

**SSE Транспорт (застарілий станом на MCP 2025-06-18):**
- Потрібен HTTP сервер з SSE кінцевими точками
- Більш складна інфраструктура веб-сервера
- Додаткові питання безпеки для HTTP кінцевих точок
- Тепер замінено на Streamable HTTP для веб-сценаріїв

### Створення сервера із stdio транспортом

Для створення нашого stdio сервера ми повинні:

1. **Імпортувати необхідні бібліотеки** - нам потрібні компоненти MCP сервера та stdio транспорт
2. **Створити екземпляр сервера** - задати сервер з його можливостями
3. **Визначити інструменти** - додати функціонал, який ми хочемо експонувати
4. **Налаштувати транспорт** - сконфігурувати stdio комунікацію
5. **Запустити сервер** - стартувати сервер і обробляти повідомлення

Побудуємо це покроково:

### Крок 1: Створити базовий stdio сервер

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server

# Налаштуйте журналювання
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Створіть сервер
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

Збережіть код як `server.py` і запустіть його з командного рядка:

```bash
python server.py
```

Сервер почне працювати і чекатиме на вхідні дані з stdin. Він спілкується через JSON-RPC повідомлення по stdio транспорту.

### Крок 4: Тестування з Inspector

Ви можете протестувати сервер за допомогою MCP Inspector:

1. Встановіть Inspector: `npx @modelcontextprotocol/inspector`
2. Запустіть Inspector і вкажіть ваш сервер
3. Перевірте створені вами інструменти

### .NET

```csharp
var builder = WebApplication.CreateBuilder(args);
builder.Services
    .AddMcpServer();
 ```
## Налагодження вашого stdio сервера

### Використання MCP Inspector

MCP Inspector – корисний інструмент для налагодження і тестування MCP серверів. Ось як ним користуватись із вашим stdio сервером:

1. **Встановіть Inspector**:
   ```bash
   npx @modelcontextprotocol/inspector
   ```

2. **Запустіть Inspector**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

3. **Тестуйте сервер**: Inspector надає веб-інтерфейс, де ви можете:
   - Переглянути можливості сервера
   - Тестувати інструменти з різними параметрами
   - Моніторити JSON-RPC повідомлення
   - Налагоджувати проблеми з підключенням

### Використання VS Code

Ви також можете налагоджувати MCP сервер безпосередньо у VS Code:

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
3. Запустіть налагоджувач і тестуйте з Inspector

### Поширені поради з налагодження

- Використовуйте `stderr` для логування – ніколи не пишіть у `stdout`, оскільки він призначений для MCP повідомлень
- Усі JSON-RPC повідомлення мають бути розділені новими рядками
- Спочатку тестуйте прості інструменти, перед додаванням складної функціональності
- Використовуйте Inspector для перевірки форматів повідомлень

## Використання вашого stdio сервера у VS Code

Після того, як ви створили MCP stdio сервер, ви можете інтегрувати його з VS Code, щоб використовувати із Claude чи іншими клієнтами, сумісними з MCP.

### Налаштування

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

2. **Перезапустіть Claude**: закрийте і знову відкрийте Claude для завантаження нової конфігурації сервера.

3. **Перевірте з’єднання**: почніть діалог з Claude і спробуйте використовувати інструменти вашого сервера:
   - "Чи можеш привітатися за допомогою інструменту привітання?"
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
- Розуміти, чому транспорт SSE був замінений на stdio і Streamable HTTP
- Створювати інструменти, які можуть викликатися MCP клієнтами
- Налагоджувати сервер за допомогою MCP Inspector
- Інтегрувати stdio сервер з VS Code і Claude

Транспорт stdio забезпечує простіший, більш безпечний і продуктивний спосіб створення MCP серверів порівняно із застарілим пiдходом SSE. Це рекомендований транспорт для більшості реалізацій MCP серверів за специфікацією 2025-06-18.


### .NET

1. Спочатку створимо кілька інструментів, для цього створимо файл *Tools.cs* з таким вмістом:

  ```csharp
  using System.ComponentModel;
  using System.Text.Json;
  using ModelContextProtocol.Server;
  ```

## Вправа: Тестування вашого stdio сервера

Тепер, коли ви створили ваш stdio сервер, давайте перевіримо, чи він працює коректно.

### Вимоги

1. Переконайтеся, що у вас встановлений MCP Inspector:
   ```bash
   npm install -g @modelcontextprotocol/inspector
   ```

2. Ваш код сервера повинен бути збережений (наприклад, як `server.py`)

### Тестування з Inspector

1. **Запустіть Inspector з вашим сервером**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

2. **Відкрийте веб-інтерфейс**: Inspector відкриє браузерне вікно з можливостями вашого сервера.

3. **Тестуйте інструменти**: 
   - Спробуйте інструмент `get_greeting` з різними іменами
   - Протестуйте `calculate_sum` з різними числами
   - Викличте інструмент `get_server_info` для перегляду метаданих сервера

4. **Моніторинг комунікації**: Inspector показує обмін JSON-RPC повідомленнями між клієнтом і сервером.

### Що ви маєте бачити

Коли сервер запускатиметься коректно, ви побачите:
- Можливості сервера у Inspector
- Доступні інструменти для тестування
- Успішний обмін JSON-RPC повідомленнями
- Відповіді інструментів у інтерфейсі

### Поширені проблеми та рішення

**Сервер не запускається:**
- Перевірте, що всі залежності встановлені: `pip install mcp`
- Перевірте синтаксис та відступи в Python
- Перегляньте повідомлення про помилки в консолі

**Інструменти не відображаються:**
- Переконайтеся, що є декоратори `@server.tool()`
- Перевірте, що функції інструментів визначені до `main()`
- Переконайтеся, що сервер налаштований правильно

**Проблеми з підключенням:**
- Переконайтеся, що сервер використовує stdio транспорт коректно
- Перевірте, що інші процеси не заважають
- Переконайтеся у правильності команди запуску Inspector

## Завдання

Спробуйте додати до вашого сервера більше можливостей. Дивіться [цю сторінку](https://api.chucknorris.io/) щоб, наприклад, додати інструмент, який викликає API. Ви самі вирішуєте, яким має бути сервер. Успіхів :)
## Розв’язок

[Розв’язок](./solution/README.md) Ось можливий розв’язок із робочим кодом.

## Ключові висновки

Основні висновки з цього розділу:

- Транспорт stdio є рекомендованим механізмом для локальних MCP серверів.
- Транспорт stdio дозволяє безперебійне спілкування між MCP серверами та клієнтами через стандартні потоки вводу та виводу.
- Ви можете використовувати як Inspector, так і Visual Studio Code для прямого використання stdio серверів, що робить налагодження та інтеграцію простими.

## Приклади

- [Java Calculator](../samples/java/calculator/README.md)
- [.Net Calculator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Calculator](../samples/javascript/README.md)
- [TypeScript Calculator](../samples/typescript/README.md)
- [Python Calculator](../../../../03-GettingStarted/samples/python) 

## Додаткові ресурси

- [SSE](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events)

## Що далі

## Подальші кроки

Тепер, коли ви навчилися будувати MCP сервери зі stdio транспортом, ви можете досліджувати більш складні теми:

- **Далі**: [HTTP Streaming з MCP (Streamable HTTP)](../06-http-streaming/README.md) - дізнайтеся про інший підтримуваний механізм транспорту для віддалених серверів
- **Розширено**: [Кращі практики безпеки MCP](../../02-Security/README.md) - впровадження безпеки у MCP серверах
- **У виробництво**: [Стратегії розгортання](../09-deployment/README.md) - розгортання серверів для виробничого використання

## Додаткові ресурси

- [Специфікація MCP 2025-06-18](https://spec.modelcontextprotocol.io/specification/) - офіційна специфікація
- [Документація MCP SDK](https://github.com/modelcontextprotocol/sdk) - посилання на SDK для різних мов
- [Приклади спільноти](../../06-CommunityContributions/README.md) - більше прикладів серверів від спільноти

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Відмова від відповідальності**:  
Цей документ був перекладений за допомогою сервісу автоматичного перекладу [Co-op Translator](https://github.com/Azure/co-op-translator). Хоча ми прагнемо до точності, будь ласка, враховуйте, що автоматичні переклади можуть містити помилки або неточності. Оригінальний документ рідною мовою слід вважати авторитетним джерелом. Для критично важливої інформації рекомендується професійний переклад людиною. Ми не несемо відповідальності за будь-які непорозуміння або неправильні тлумачення, що виникли через використання цього перекладу.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->