# Сервер MCP с транспортом stdio

> **⚠️ Важное обновление**: С версии спецификации MCP 2025-06-18 отдельный транспорт SSE (Server-Sent Events) **устарел** и был заменён транспортом «Streamable HTTP». Текущая спецификация MCP определяет два основных механизма транспорта:
> 1. **stdio** - стандартный ввод/вывод (рекомендуется для локальных серверов)
> 2. **Streamable HTTP** - для удалённых серверов, которые могут использовать SSE внутри
>
> Этот урок обновлён с акцентом на **stdio транспорт**, который является рекомендуемым подходом для большинства реализаций MCP серверов.

Транспорт stdio позволяет MCP серверам обмениваться данными с клиентами через стандартные потоки ввода и вывода. Это самый часто используемый и рекомендуемый механизм транспорта в текущей спецификации MCP, предоставляющий простой и эффективный способ создания MCP серверов, которые легко интегрируются с различными клиентскими приложениями.

## Обзор

В этом уроке рассматривается, как создавать и использовать MCP серверы с транспортом stdio.

## Цели обучения

К концу этого урока вы сможете:

- Создавать MCP сервер с использованием stdio транспорта.
- Отлаживать MCP сервер с помощью Inspector.
- Использовать MCP сервер в Visual Studio Code.
- Понимать текущие механизмы транспорта MCP и почему рекомендуется stdio.


## Транспорт stdio — как он работает

Транспорт stdio — один из двух стандартных транспортов в спецификации MCP
`2026-07-28`. Вот как он работает:

- **Простое общение**: сервер читает сообщения JSON-RPC из стандартного ввода (`stdin`) и отправляет сообщения в стандартный вывод (`stdout`).
- **Основан на процессах**: клиент запускает MCP сервер как подпроцесс.
- **Формат сообщений**: сообщения — отдельные запросы, уведомления или ответы JSON-RPC, разделённые переводами строк.
- **Логирование**: сервер МОЖЕТ записывать строки UTF-8 в стандартный поток ошибок (`stderr`) для целей логирования.

### Ключевые требования:
- Сообщения ДОЛЖНЫ разделяться переводами строки и НЕ ДОЛЖНЫ содержать вложенных переводов строк
- Сервер НЕ ДОЛЖЕН записывать в `stdout` ничего, что не является действительным сообщением MCP
- Клиент НЕ ДОЛЖЕН записывать в `stdin` сервера ничего, что не является действительным сообщением MCP

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

В приведённом выше коде:

- Импортируем класс `Server` и `StdioServerTransport` из SDK MCP
- Создаём экземпляр сервера с базовой конфигурацией и возможностями
- Создаём экземпляр `StdioServerTransport` и подключаем сервер к нему, обеспечивая связь через stdin/stdout

### Python

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server

# Создать экземпляр сервера
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

В приведённом коде:

- Создаём экземпляр сервера с помощью SDK MCP
- Определяем инструменты с помощью декораторов
- Используем контекстный менеджер stdio_server для управления транспортом

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

Главное отличие от SSE в том, что stdio серверы:

- Не требуют настройки веб-сервера или HTTP эндпоинтов
- Запускаются как подпроцессы клиентом
- Общаются через потоки stdin/stdout
- Проще в реализации и отладке

## Упражнение: Создание stdio сервера

Для создания нашего сервера нам нужно помнить две вещи:

- Необходимо использовать веб-сервер для предоставления эндпоинтов для подключения и сообщений.
## Лабораторная работа: Создание простого MCP stdio сервера

В этой лабораторной работе мы создадим простой MCP сервер с рекомендованным транспортом stdio. Этот сервер предоставит инструменты, которые клиенты смогут вызывать с помощью стандартного протокола Model Context Protocol.

### Требования

- Python версии 3.8 или выше
- MCP Python SDK: `pip install mcp`
- Базовое понимание асинхронного программирования

Начнём с создания нашего первого MCP stdio сервера:

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp import types

# Настроить логирование
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Создать сервер
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
    # Использовать транспорт stdio
    async with stdio_server(server) as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            server.create_initialization_options()
        )

if __name__ == "__main__":
    asyncio.run(main())
```

## Ключевые отличия от устаревшего SSE подхода

**Stdio транспорт (текущий стандарт):**
- Простая модель подпроцесса — клиент запускает сервер как дочерний процесс
- Общение через stdin/stdout с использованием сообщений JSON-RPC
- Не требуется настройка HTTP сервера
- Лучшая производительность и безопасность
- Проще отлаживать и разрабатывать

**SSE транспорт (устарел с MCP 2025-06-18):**
- Требовался HTTP сервер с SSE эндпоинтами
- Более сложная инфраструктура с веб-сервером
- Дополнительные вопросы безопасности для HTTP эндпоинтов
- Сейчас заменён на Streamable HTTP для веб-сценариев

### Создание сервера с транспортом stdio

Чтобы создать наш stdio сервер, нужно:

1. **Импортировать необходимые библиотеки** — нам нужны компоненты сервера MCP и транспорт stdio
2. **Создать экземпляр сервера** — определить сервер с его возможностями
3. **Определить инструменты** — добавить функциональность, которую хотим предоставить
4. **Настроить транспорт** — сконфигурировать связь stdio
5. **Запустить сервер** — стартовать сервер и обрабатывать сообщения

Построим это шаг за шагом:

### Шаг 1: Создаём базовый stdio сервер

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server

# Настроить логирование
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Создать сервер
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

### Шаг 2: Добавляем больше инструментов

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

### Шаг 3: Запуск сервера

Сохраните код как `server.py` и запустите его из командной строки:

```bash
python server.py
```

Сервер запустится и будет ждать ввода из stdin. Общение происходит через JSON-RPC сообщения по stdio транспорту.

### Шаг 4: Тестирование с помощью Inspector

Вы можете протестировать ваш сервер с помощью MCP Inspector:

1. Установите Inspector: `npx @modelcontextprotocol/inspector`
2. Запустите Inspector и укажите ваш сервер
3. Проверьте созданные инструменты

### .NET

```csharp
var builder = WebApplication.CreateBuilder(args);
builder.Services
    .AddMcpServer();
 ```
## Отладка вашего stdio сервера

### Использование MCP Inspector

MCP Inspector — ценный инструмент для отладки и тестирования MCP серверов. Вот как использовать его с вашим stdio сервером:

1. **Установите Inspector**:
   ```bash
   npx @modelcontextprotocol/inspector
   ```

2. **Запустите Inspector**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

3. **Тестируйте сервер**: Inspector предоставляет веб-интерфейс, где вы можете:
   - Просматривать возможности сервера
   - Тестировать инструменты с разными параметрами
   - Отслеживать сообщения JSON-RPC
   - Отлаживать проблемы с соединением

### Использование VS Code

Вы также можете отлаживать MCP сервер напрямую в VS Code:

1. Создайте конфигурацию запуска в `.vscode/launch.json`:
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

2. Установите точки останова в коде сервера
3. Запустите отладчик и тестируйте с Inspector

### Общие советы по отладке

- Используйте `stderr` для логирования — никогда не пишите в `stdout`, так как он зарезервирован для сообщений MCP
- Убедитесь, что все сообщения JSON-RPC разделены переводами строк
- Сначала тестируйте с простыми инструментами, прежде чем добавлять сложный функционал
- Используйте Inspector для проверки формата сообщений

## Использование вашего stdio сервера в VS Code

После того, как вы создали MCP stdio сервер, вы можете интегрировать его с VS Code для использования с Claude или другими клиентами MCP.

### Конфигурация

1. **Создайте конфигурационный файл MCP** по пути `%APPDATA%\Claude\claude_desktop_config.json` (Windows) или `~/Library/Application Support/Claude/claude_desktop_config.json` (Mac):

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

2. **Перезапустите Claude**: Закройте и откройте Claude заново, чтобы загрузить новую конфигурацию сервера.

3. **Проверьте соединение**: Начните разговор с Claude и попробуйте использовать инструменты вашего сервера:
   - «Можешь поприветствовать меня с помощью инструмента приветствия?»
   - «Вычисли сумму 15 и 27»
   - «Какая информация о сервере?»

### Пример TypeScript stdio сервера

Вот полный пример на TypeScript для справки:

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

// Добавить инструменты
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

## Итоги

В этом обновлённом уроке вы узнали, как:

- Создавать MCP серверы с современным **stdio транспортом** (рекомендуемый подход)
- Понимать, почему транспорт SSE устарел в пользу stdio и Streamable HTTP
- Создавать инструменты, доступные для вызова клиентами MCP
- Отлаживать сервер с помощью MCP Inspector
- Интегрировать stdio сервер с VS Code и Claude

Транспорт stdio обеспечивает более простой, безопасный и производительный способ создания MCP серверов по сравнению с устаревшим подходом SSE. Это рекомендуемый транспорт для большинства реализаций MCP серверов по спецификации от 2025-06-18.


### .NET

1. Сначала создадим несколько инструментов, для этого создадим файл *Tools.cs* со следующим содержимым:

  ```csharp
  using System.ComponentModel;
  using System.Text.Json;
  using ModelContextProtocol.Server;
  ```

## Упражнение: Тестирование вашего stdio сервера

Теперь, когда вы создали ваш stdio сервер, давайте протестируем его, чтобы убедиться, что он работает правильно.

### Требования

1. Убедитесь, что MCP Inspector установлен:
   ```bash
   npm install -g @modelcontextprotocol/inspector
   ```

2. Ваш код сервера должен быть сохранён (например, как `server.py`)

### Тестирование с Inspector

1. **Запустите Inspector вместе с вашим сервером**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

2. **Откройте веб-интерфейс**: Inspector откроет окно браузера с возможностями вашего сервера.

3. **Проверьте инструменты**:
   - Попробуйте инструмент `get_greeting` с разными именами
   - Проверьте инструмент `calculate_sum` с разными числами
   - Вызовите инструмент `get_server_info`, чтобы увидеть метаданные сервера

4. **Отслеживайте коммуникацию**: Inspector показывает обмен сообщениями JSON-RPC между клиентом и сервером.

### Что вы должны увидеть

При правильном запуске сервера вы увидите:
- Способности сервера, отображаемые в Inspector
- Инструменты, доступные для тестирования
- Успешный обмен сообщениями JSON-RPC
- Ответы инструментов, отображаемые в интерфейсе

### Общие проблемы и решения

**Сервер не запускается:**
- Проверьте, что все зависимости установлены: `pip install mcp`
- Проверьте синтаксис и отступы Python
- Изучите сообщения об ошибках в консоли

**Инструменты не отображаются:**
- Убедитесь, что декораторы `@server.tool()` присутствуют
- Проверьте, что функции инструментов определены до `main()`
- Убедитесь, что сервер правильно настроен

**Проблемы с подключением:**
- Убедитесь, что сервер корректно использует транспорт stdio
- Проверьте, что другие процессы не мешают
- Проверьте синтаксис команд Inspector

## Задание

Попробуйте расширить свой сервер новыми возможностями. Посмотрите [эту страницу](https://api.chucknorris.io/), чтобы, например, добавить инструмент, который вызывает API. Решайте сами, каким должен быть сервер. Удачи :)
## Решение

[Решение](./solution/README.md) Вот возможное решение с работающим кодом.

## Основные выводы

Главные выводы из этой главы:

- Транспорт stdio — рекомендуемый механизм для локальных MCP серверов.
- Транспорт stdio обеспечивает бесшовное общение между MCP серверами и клиентами через стандартные потоки ввода и вывода.
- Можно использовать Inspector и Visual Studio Code для прямого взаимодействия со stdio серверами, что упрощает отладку и интеграцию.

## Примеры

- [Java калькулятор](../samples/java/calculator/README.md)
- [.Net калькулятор](../../../../03-GettingStarted/samples/csharp)
- [JavaScript калькулятор](../samples/javascript/README.md)
- [TypeScript калькулятор](../samples/typescript/README.md)
- [Python калькулятор](../../../../03-GettingStarted/samples/python) 

## Дополнительные ресурсы

- [SSE](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events)

## Что дальше

## Следующие шаги

Теперь, когда вы научились создавать MCP серверы с транспортом stdio, вы можете изучить более продвинутые темы:

- **Далее**: [HTTP потоковая передача с MCP (Streamable HTTP)](../06-http-streaming/README.md) — изучите другой поддерживаемый механизм транспорта для удалённых серверов
- **Продвинутые**: [Лучшие практики безопасности MCP](../../02-Security/README.md) — обеспечьте безопасность MCP серверов
- **Для продакшена**: [Стратегии развертывания](../09-deployment/README.md) — развертывание серверов для промышленного использования

## Дополнительные ресурсы

- [Спецификация MCP 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/) — текущая спецификация
- [Документация MCP SDK](https://github.com/modelcontextprotocol/sdk) — справочники по SDK для всех языков
- [Примеры сообщества](../../06-CommunityContributions/README.md) — больше примеров серверов от сообщества

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Отказ от ответственности**:
Этот документ был переведен с использованием сервиса машинного перевода [Co-op Translator](https://github.com/Azure/co-op-translator). Несмотря на наши усилия по обеспечению точности, имейте в виду, что автоматический перевод может содержать ошибки или неточности. Оригинальный документ на его исходном языке следует считать авторитетным источником. Для получения критически важной информации рекомендуется обратиться к профессиональному человеческому переводу. Мы не несем ответственности за любые недоразумения или неправильные толкования, возникшие в результате использования этого перевода.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->