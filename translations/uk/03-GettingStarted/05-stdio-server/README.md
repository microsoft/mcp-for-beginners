# MCP сервер з транспортом stdio

> **⚠️ Важливе оновлення**: Починаючи з MCP Специфікації 2025-06-18, автономний транспорт SSE (Server-Sent Events) було **знято з використання** та замінено на транспорт "Streamable HTTP". Поточна MCP специфікація визначає два основні механізми транспорту:
> 1. **stdio** - стандартний ввід/вивід (рекомендовано для локальних серверів)
> 2. **Streamable HTTP** - для віддалених серверів, які можуть внутрішньо використовувати SSE
>
> Цей урок оновлено з акцентом на **stdio транспорт**, який є рекомендованим підходом для більшості реалізацій MCP серверів.

Транспорт stdio дозволяє MCP серверам спілкуватися з клієнтами через стандартні потоки вводу і виводу. Це найпоширеніший і рекомендований транспортний механізм у поточній MCP специфікації, який забезпечує простий і ефективний спосіб створення MCP серверів, які легко інтегрувати з різними клієнтськими додатками.

## Огляд

У цьому уроці розглядається, як створювати та використовувати MCP сервери з транспортом stdio.

## Навчальні цілі

Наприкінці цього уроку ви зможете:

- Створити MCP сервер із транспортом stdio.
- Налагодити MCP сервер за допомогою Inspector.
- Використовувати MCP сервер у Visual Studio Code.
- Розуміти поточні механізми транспорту MCP і чому рекомендується stdio.


## Транспорт stdio – як це працює

Транспорт stdio - один із двох стандартних транспортів у MCP Специфікації
`2026-07-28`. Ось як він працює:

- **Проста комунікація**: сервер читає повідомлення JSON-RPC зі стандартного вводу (`stdin`) та відправляє повідомлення на стандартний вивід (`stdout`).
- **На основі процесу**: клієнт запускає MCP сервер як підпроцес.
- **Формат повідомлень**: повідомлення — це окремі JSON-RPC запити, сповіщення або відповіді, розділені переведенням рядка.
- **Логування**: сервер МОЖЕ записувати рядки UTF-8 на стандартний потік помилок (`stderr`) для цілей логування.

### Ключові вимоги:
- Повідомлення МАЮТЬ бути розділені переведеннями рядка та НЕ МАЮТЬ містити вкладені переведення рядка
- Сервер НЕ МАЄ записувати в `stdout` нічого, що не є дійсним MCP повідомленням
- Клієнт НЕ МАЄ писати в `stdin` сервера нічого, що не є дійсним MCP повідомленням

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

У вказаному коді:

- Ми імпортуємо клас `Server` і `StdioServerTransport` із MCP SDK
- Створюємо екземпляр сервера з базовою конфігурацією та можливостями
- Створюємо екземпляр `StdioServerTransport` і підключаємо до нього сервер, що дозволяє здійснювати комунікацію через stdin/stdout

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

- Створюємо екземпляр сервера за допомогою MCP SDK
- Визначаємо інструменти за допомогою декораторів
- Використовуємо контекстний менеджер stdio_server для обробки транспорту

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

Ключова відмінність від SSE у тому, що stdio сервери:

- Не потребують налаштування веб-сервера або HTTP кінцевих точок
- Запускаються клієнтом як підпроцеси
- Спілкуються через потоки stdin/stdout
- Простіші у реалізації та налагодженні

## Вправа: Створення stdio сервера

Для створення сервера слід пам’ятати про дві речі:

- Нам потрібно використовувати веб-сервер, щоб відкривати кінцеві точки для підключення і повідомлень.
## Лабораторна робота: Створення простого MCP stdio сервера

У цій лабораторній роботі ми створимо простий MCP сервер, використовуючи рекомендований транспорт stdio. Цей сервер відкриватиме інструменти, які клієнти можуть викликати, використовуючи стандартний Протокол Контексту Моделі.

### Необхідні умови

- Python 3.8 або пізніша версія
- MCP Python SDK: `pip install mcp`
- Базове розуміння асинхронного програмування

Почнемо зі створення нашого першого MCP stdio сервера:

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp import types

# Налаштувати ведення журналу
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

## Відмінності від застарілого підходу SSE

**Транспорт Stdio (поточний стандарт):**
- Простий модель підпроцесу - клієнт запускає сервер як дочірній процес
- Комунікація через stdin/stdout з використанням JSON-RPC повідомлень
- Не потрібне налаштування HTTP сервера
- Краща продуктивність і безпека
- Легше налагоджувати і розробляти

**Транспорт SSE (знято з використання з MCP 2025-06-18):**
- Вимагає HTTP сервер з SSE кінцевими точками
- Більш складне налаштування з веб-серверною інфраструктурою
- Додаткові міркування безпеки для HTTP кінцевих точок
- Зараз замінено на Streamable HTTP для веб-сценаріїв

### Створення сервера з транспортом stdio

Щоб створити наш stdio сервер, потрібно:

1. **Імпортувати необхідні бібліотеки** – нам потрібні компоненти MCP сервера і транспорт stdio
2. **Створити екземпляр сервера** – визначити сервер з його можливостями
3. **Визначити інструменти** – додати функції, які хочемо надати
4. **Налаштувати транспорт** – сконфігурувати комунікацію через stdio
5. **Запустити сервер** – почати роботу сервера і обробляти повідомлення

Побудуємо це крок за кроком:

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

Збережіть код у файлі `server.py` і запустіть його з командного рядка:

```bash
python server.py
```

Сервер запуститься і чекатиме вхідні дані зі stdin. Він спілкується за допомогою JSON-RPC повідомлень через транспорт stdio.

### Крок 4: Тестування з Inspector

Ви можете протестувати свій сервер за допомогою MCP Inspector:

1. Встановіть Inspector: `npx @modelcontextprotocol/inspector`
2. Запустіть Inspector і вкажіть на свій сервер
3. Перевірте інструменти, які ви створили

### .NET

```csharp
var builder = WebApplication.CreateBuilder(args);
builder.Services
    .AddMcpServer();
 ```
## Налагодження вашого stdio сервера

### Використання MCP Inspector

MCP Inspector — це цінний інструмент для налагодження та тестування MCP серверів. От як його використовувати із вашим stdio сервером:

1. **Встановіть Inspector**:
   ```bash
   npx @modelcontextprotocol/inspector
   ```

2. **Запустіть Inspector**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

3. **Тестуйте сервер**: Inspector надає веб-інтерфейс, де ви можете:
   - Переглядати можливості сервера
   - Тестувати інструменти з різними параметрами
   - Моніторити JSON-RPC повідомлення
   - Налагоджувати проблеми з підключенням

### Використання VS Code

Ви також можете налагоджувати свій MCP сервер безпосередньо у VS Code:

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

### Поширені поради для налагодження

- Використовуйте `stderr` для логування — ніколи не пишіть у `stdout`, оскільки він зарезервований для MCP повідомлень
- Переконайтесь, що всі JSON-RPC повідомлення розділені переведеннями рядка
- Спочатку тестуйте з простими інструментами перед додаванням складної логіки
- Використовуйте Inspector для перевірки форматів повідомлень

## Використання вашого stdio сервера в VS Code

Як тільки ви створили свій MCP stdio сервер, ви можете інтегрувати його з VS Code, щоб використовувати з Claude або іншими клієнтами, сумісними з MCP.

### Налаштування

1. **Створіть файл конфігурації MCP** за адресою `%APPDATA%\Claude\claude_desktop_config.json` (Windows) або `~/Library/Application Support/Claude/claude_desktop_config.json` (Mac):

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

2. **Перезапустіть Claude**: закрийте і відкрийте Claude заново, щоб завантажити нову конфігурацію сервера.

3. **Перевірте з’єднання**: почніть розмову з Claude і спробуйте використовувати інструменти вашого сервера:
   - "Чи можеш привітати мене за допомогою інструменту привітання?"
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

У цьому оновленому уроці ви дізналися, як:

- Створювати MCP сервери, використовуючи поточний **stdio транспорт** (рекомендований підхід)
- Розуміти, чому транспорт SSE був знятий з використання на користь stdio і Streamable HTTP
- Створювати інструменти, які можуть викликатися клієнтами MCP
- Налагоджувати сервер за допомогою MCP Inspector
- Інтегрувати stdio сервер із VS Code та Claude

Транспорт stdio забезпечує простіший, безпечніший і більш продуктивний спосіб створення MCP серверів порівняно з застарілим підходом SSE. Це рекомендований транспорт для більшості впроваджень MCP серверів починаючи зі специфікації 2025-06-18.


### .NET

1. Спочатку створимо кілька інструментів, для цього створимо файл *Tools.cs* з таким вмістом:

  ```csharp
  using System.ComponentModel;
  using System.Text.Json;
  using ModelContextProtocol.Server;
  ```

## Вправа: Тестування вашого stdio сервера

Тепер, коли ви створили свій stdio сервер, перевіримо, чи він працює правильно.

### Необхідні умови

1. Переконайтеся, що MCP Inspector встановлений:
   ```bash
   npm install -g @modelcontextprotocol/inspector
   ```

2. Ваш код сервера має бути збережений (наприклад, у файлі `server.py`)

### Тестування з Inspector

1. **Запустіть Inspector разом із сервером**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

2. **Відкрийте веб-інтерфейс**: Inspector відкриє вікно браузера з можливостями вашого сервера.

3. **Перевірте інструменти**:
   - Спробуйте інструмент `get_greeting` з різними іменами
   - Перевірте інструмент `calculate_sum` з різними числами
   - Викличте інструмент `get_server_info` для перегляду метаданих сервера

4. **Моніторинг комунікації**: Inspector показує JSON-RPC повідомлення, що обмінюються між клієнтом і сервером.

### Що ви маєте побачити

Коли ваш сервер успішно запуститься, ви побачите:
- Зазначені можливості сервера у Inspector
- Інструменти, доступні для тестування
- Успішний обмін JSON-RPC повідомленнями
- Відповіді інструментів, відображені в інтерфейсі

### Поширені проблеми та рішення

**Сервер не запускається:**
- Перевірте, що всі залежності встановлено: `pip install mcp`
- Перевірте синтаксис і відступи Python
- Подивіться повідомлення про помилки у консолі

**Інструменти не з’являються:**
- Переконайтесь, що присутні декоратори `@server.tool()`
- Переконайтеся, що функції інструментів визначені до `main()`
- Перевірте правильність конфігурації сервера

**Проблеми з підключенням:**
- Переконайтесь, що сервер правильно використовує транспорт stdio
- Перевірте, що інші процеси не заважають
- Перевірте синтаксис команди Inspector

## Завдання

Спробуйте розширити свій сервер новими можливостями. Перегляньте [цю сторінку](https://api.chucknorris.io/), щоб, наприклад, додати інструмент, який викликає API. Ви самі вирішуєте, яким має бути сервер. Успіхів :)
## Розв’язок

[Розв’язок](./solution/README.md) Ось можливий розв’язок з робочим кодом.

## Важливі висновки

Основні висновки з цієї глави:

- Транспорт stdio є рекомендованим механізмом для локальних MCP серверів.
- Транспорт stdio забезпечує безперебійну комунікацію між MCP серверами та клієнтами через стандартні потоки вводу і виводу.
- Ви можете використовувати як Inspector, так і Visual Studio Code для прямого споживання stdio серверів, що робить налагодження та інтеграцію простими.

## Приклади

- [Java калькулятор](../samples/java/calculator/README.md)
- [.Net калькулятор](../../../../03-GettingStarted/samples/csharp)
- [JavaScript калькулятор](../samples/javascript/README.md)
- [TypeScript калькулятор](../samples/typescript/README.md)
- [Python калькулятор](../../../../03-GettingStarted/samples/python) 

## Додаткові ресурси

- [SSE](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events)

## Що далі

## Наступні кроки

Тепер, коли ви навчилися створювати MCP сервери з транспортом stdio, можете вивчати більш просунуті теми:

- **Далі**: [HTTP стрімінг з MCP (Streamable HTTP)](../06-http-streaming/README.md) – Дізнайтесь про інший підтримуваний транспорт для віддалених серверів
- **Вдосконалені теми**: [Найкращі практики безпеки MCP](../../02-Security/README.md) – Впроваджуйте безпеку у свої MCP сервери
- **У продакшн**: [Стратегії розгортання](../09-deployment/README.md) – Розгорніть свої сервери для виробничого використання

## Додаткові ресурси

- [MCP Специфікація 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/) – Поточна специфікація
- [Документація MCP SDK](https://github.com/modelcontextprotocol/sdk) – Посилання на SDK для всіх мов
- [Приклади від спільноти](../../06-CommunityContributions/README.md) – Більше серверних прикладів від спільноти

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Відмова від відповідальності**:
Цей документ було перекладено за допомогою сервісу штучного інтелекту для перекладу [Co-op Translator](https://github.com/Azure/co-op-translator). Хоча ми прагнемо до точності, будь ласка, майте на увазі, що автоматичні переклади можуть містити помилки або неточності. Оригінальний документ рідною мовою слід вважати авторитетним джерелом. Для критично важливої інформації рекомендується професійний людський переклад. Ми не несемо відповідальності за будь-які непорозуміння або неправильні тлумачення, що виникли внаслідок використання цього перекладу.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->