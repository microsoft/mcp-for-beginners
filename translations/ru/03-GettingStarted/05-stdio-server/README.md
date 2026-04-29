# MCP сервер с транспортом stdio

> **⚠️ Важное обновление**: Начиная с MCP Specification 2025-06-18, самостоятельный транспорт SSE (Server-Sent Events) **устарел** и был заменён транспортом "Streamable HTTP". Текущая спецификация MCP определяет два основных механизма транспорта:
> 1. **stdio** - стандартный ввод/вывод (рекомендуется для локальных серверов)
> 2. **Streamable HTTP** - для удалённых серверов, которые могут использовать SSE внутри себя
>
> Этот урок обновлён и сосредоточен на **транспорте stdio**, который является рекомендуемым подходом для большинства реализаций MCP серверов.

Транспорт stdio позволяет MCP серверам взаимодействовать с клиентами через стандартные потоки ввода и вывода. Это самый часто используемый и рекомендуемый механизм транспорта в текущей спецификации MCP, обеспечивающий простой и эффективный способ создавать MCP серверы, которые легко интегрируются с различными клиентскими приложениями.

## Обзор

В этом уроке рассматривается, как создавать и использовать MCP серверы с использованием транспорта stdio.

## Цели обучения

К концу этого урока вы сможете:

- Создавать MCP сервер с использованием транспорта stdio.
- Отлаживать MCP сервер с помощью Inspector.
- Использовать MCP сервер в Visual Studio Code.
- Понимать текущие механизмы транспорта MCP и почему рекомендуется stdio.


## Транспорт stdio - как это работает

Транспорт stdio — один из двух поддерживаемых типов транспорта в текущей спецификации MCP (2025-06-18). Вот как он работает:

- **Простое взаимодействие**: сервер читает сообщения JSON-RPC из стандартного ввода (`stdin`) и отправляет сообщения в стандартный вывод (`stdout`).
- **Процессный подход**: клиент запускает MCP сервер как дочерний процесс.
- **Формат сообщений**: сообщения — отдельные запросы, уведомления или ответы JSON-RPC, разделённые переводами строки.
- **Логирование**: сервер МОЖЕТ писать UTF-8 строки в стандартный поток ошибок (`stderr`) для целей логирования.

### Ключевые требования:
- Сообщения ДОЛЖНЫ разделяться переводами строки и НЕ ДОЛЖНЫ содержать вложенных переводов строки
- Сервер НЕ ДОЛЖЕН писать в `stdout` ничего, что не является валидным сообщением MCP
- Клиент НЕ ДОЛЖЕН писать в `stdin` сервера ничего, что не является валидным сообщением MCP

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

В приведённом коде:

- Мы импортируем класс `Server` и `StdioServerTransport` из MCP SDK
- Создаём экземпляр сервера с базовой конфигурацией и возможностями
- Создаём экземпляр `StdioServerTransport` и подключаем сервер к нему, что позволяет обмениваться данными через stdin/stdout

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

В приведённом коде мы:

- Создаём экземпляр сервера с помощью MCP SDK
- Определяем инструменты с помощью декораторов
- Используем менеджер контекста stdio_server для управления транспортом

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

Ключевое отличие от SSE в том, что stdio серверы:

- Не требуют настройки веб-сервера или HTTP эндпоинтов
- Запускаются как дочерние процессы клиентом
- Общаются через потоки stdin/stdout
- Проще в реализации и отладке

## Упражнение: создание stdio сервера

Чтобы создать наш сервер, нам нужно помнить две вещи:

- Нам нужно использовать веб-сервер для открытия эндпоинтов для подключения и сообщений.
## Лабораторная работа: создание простого MCP stdio сервера

В этой лабораторной работе мы создадим простой MCP сервер с использованием рекомендуемого транспорта stdio. Этот сервер предоставит инструменты, которые клиенты смогут вызывать с помощью стандартного протокола Model Context Protocol.

### Предварительные требования

- Python 3.8 или выше
- MCP Python SDK: `pip install mcp`
- Базовые знания асинхронного программирования

Начнём с создания нашего первого MCP stdio сервера:

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp import types

# Настроить журналирование
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

## Основные отличия от устаревшего подхода SSE

**Транспорт stdio (текущий стандарт):**
- Простой процессный модель — клиент запускает сервер как дочерний процесс
- Общение через stdin/stdout с использованием сообщений JSON-RPC
- Не требуется настройка HTTP сервера
- Лучшая производительность и безопасность
- Проще отладка и разработка

**Транспорт SSE (устарел начиная с MCP 2025-06-18):**
- Необходим HTTP сервер с SSE эндпоинтами
- Сложная настройка с инфраструктурой веб-сервера
- Дополнительные требования безопасности для HTTP эндпоинтов
- Теперь заменён на Streamable HTTP для веб-сценариев

### Создание сервера с транспортом stdio

Чтобы создать наш сервер stdio, необходимо:

1. **Импортировать необходимые библиотеки** — нужны компоненты сервера MCP и транспорт stdio
2. **Создать экземпляр сервера** — определить сервер и его возможности
3. **Определить инструменты** — добавить функциональность, которую хотим открыть
4. **Настроить транспорт** — сконфигурировать stdio коммуникацию
5. **Запустить сервер** — стартовать сервер и обрабатывать сообщения

Построим это по шагам:

### Шаг 1: создание базового stdio сервера

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

### Шаг 2: добавление инструментов

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

### Шаг 3: запуск сервера

Сохраните код как `server.py` и запустите его из командной строки:

```bash
python server.py
```

Сервер запустится и будет ждать ввода из stdin. Он общается с помощью сообщений JSON-RPC через транспорт stdio.

### Шаг 4: тестирование с Inspector

Вы можете протестировать сервер с помощью MCP Inspector:

1. Установите Inspector: `npx @modelcontextprotocol/inspector`
2. Запустите Inspector и укажите на ваш сервер
3. Протестируйте созданные инструменты

### .NET

```csharp
var builder = WebApplication.CreateBuilder(args);
builder.Services
    .AddMcpServer();
 ```
## Отладка вашего stdio сервера

### Использование MCP Inspector

MCP Inspector — полезный инструмент для отладки и тестирования MCP серверов. Вот как использовать его с вашим stdio сервером:

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
   - Отлаживать проблемы подключения

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

- Используйте `stderr` для логов — никогда не пишите в `stdout`, так как он зарезервирован для сообщений MCP
- Убедитесь, что все JSON-RPC сообщения разделены переводами строки
- Сначала тестируйте простые инструменты, прежде чем добавлять сложную функциональность
- Используйте Inspector для проверки формата сообщений

## Использование вашего stdio сервера в VS Code

После того как вы создали MCP stdio сервер, его можно интегрировать с VS Code для работы с Claude или другими клиентами, поддерживающими MCP.

### Конфигурация

1. **Создайте файл конфигурации MCP** в `%APPDATA%\Claude\claude_desktop_config.json` (Windows) или `~/Library/Application Support/Claude/claude_desktop_config.json` (Mac):

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

3. **Проверьте подключение**: Начните диалог с Claude и попробуйте использовать инструменты вашего сервера:
   - "Можешь поздороваться со мной, используя инструмент приветствия?"
   - "Вычисли сумму 15 и 27"
   - "Какая информация о сервере?"

### Пример stdio сервера на TypeScript

Ниже приведён полный пример на TypeScript для справки:

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

### Пример stdio сервера на .NET

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

В этом обновлённом уроке вы научились:

- Строить MCP серверы с использованием текущего **транспорта stdio** (рекомендуемый подход)
- Понимать, почему транспорт SSE был устаревшим в пользу stdio и Streamable HTTP
- Создавать инструменты, которые могут вызываться MCP клиентами
- Отлаживать сервер с помощью MCP Inspector
- Интегрировать stdio сервер с VS Code и Claude

Транспорт stdio предоставляет более простой, безопасный и производительный способ создания MCP серверов по сравнению с устаревшим подходом SSE. Это рекомендуемый транспорт для большинства реализаций MCP серверов согласно спецификации от 2025-06-18.


### .NET

1. Для начала создадим инструменты, для этого создадим файл *Tools.cs* со следующим содержимым:

  ```csharp
  using System.ComponentModel;
  using System.Text.Json;
  using ModelContextProtocol.Server;
  ```

## Упражнение: тестирование вашего stdio сервера

Теперь, когда вы создали stdio сервер, давайте проверим его работоспособность.

### Предварительные условия

1. Убедитесь, что у вас установлен MCP Inspector:
   ```bash
   npm install -g @modelcontextprotocol/inspector
   ```

2. Код вашего сервера сохранён (например, как `server.py`)

### Тестирование с Inspector

1. **Запустите Inspector вместе с сервером**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

2. **Откройте веб-интерфейс**: Inspector откроет браузер с возможностями вашего сервера.

3. **Проверьте инструменты**: 
   - Попробуйте инструмент `get_greeting` с разными именами
   - Проверьте инструмент `calculate_sum` с разными числами
   - Вызовите инструмент `get_server_info`, чтобы увидеть метаданные сервера

4. **Наблюдайте за коммуникацией**: Inspector показывает сообщения JSON-RPC, передаваемые между клиентом и сервером.

### Что вы должны увидеть

Если сервер запустился правильно, вы должны увидеть:
- Возможности сервера, отображаемые в Inspector
- Доступные инструменты для тестирования
- Успешный обмен сообщениями JSON-RPC
- Ответы инструментов, показанные в интерфейсе

### Частые проблемы и решения

**Сервер не запускается:**
- Проверьте, что все зависимости установлены: `pip install mcp`
- Проверьте синтаксис и отступы в Python
- Посмотрите сообщения об ошибках в консоли

**Инструменты не отображаются:**
- Убедитесь, что декораторы `@server.tool()` присутствуют
- Проверьте, что функции инструментов определены до `main()`
- Убедитесь, что сервер настроен корректно

**Проблемы с подключением:**
- Убедитесь, что сервер использует транспорт stdio правильно
- Проверьте, что другие процессы не мешают
- Проверьте синтаксис команд Inspector

## Задание

Попробуйте расширить функциональность вашего сервера. Посмотрите [эту страницу](https://api.chucknorris.io/), чтобы, например, добавить инструмент, который вызывает API. Вы решаете, каким должен быть сервер. Удачи :)
## Решение

[Решение](./solution/README.md) Вот возможное решение с рабочим кодом.

## Основные выводы

Основные выводы из этой главы:

- Транспорт stdio — рекомендуемый механизм для локальных MCP серверов.
- Транспорт stdio позволяет бесшовно взаимодействовать между MCP серверами и клиентами через стандартные потоки ввода и вывода.
- Вы можете использовать как Inspector, так и Visual Studio Code для непосредственного использования stdio серверов, что упрощает отладку и интеграцию.

## Примеры

- [Java Calculator](../samples/java/calculator/README.md)
- [.Net Calculator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Calculator](../samples/javascript/README.md)
- [TypeScript Calculator](../samples/typescript/README.md)
- [Python Calculator](../../../../03-GettingStarted/samples/python) 

## Дополнительные ресурсы

- [SSE](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events)

## Что дальше

## Следующие шаги

Теперь, когда вы научились строить MCP серверы с транспортом stdio, вы можете изучать более продвинутые темы:

- **Далее**: [HTTP Streaming с MCP (Streamable HTTP)](../06-http-streaming/README.md) — узнаете о другом поддерживаемом механизме транспорта для удалённых серверов
- **Продвинутый уровень**: [Лучшие практики безопасности MCP](../../02-Security/README.md) — реализуйте безопасность в ваших MCP серверах
- **Производство**: [Стратегии развертывания](../09-deployment/README.md) — развертывайте серверы для использования в продакшене

## Дополнительные ресурсы

- [MCP Specification 2025-06-18](https://spec.modelcontextprotocol.io/specification/) — официальная спецификация
- [Документация MCP SDK](https://github.com/modelcontextprotocol/sdk) — справочники SDK для всех языков
- [Примеры сообщества](../../06-CommunityContributions/README.md) — ещё больше примеров серверов от сообщества

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Отказ от ответственности**:  
Этот документ был переведен с помощью сервиса AI-перевода [Co-op Translator](https://github.com/Azure/co-op-translator). Несмотря на наши усилия по обеспечению точности, пожалуйста, имейте в виду, что автоматические переводы могут содержать ошибки или неточности. Оригинальный документ на его исходном языке следует считать авторитетным источником. Для важной информации рекомендуется использовать профессиональный человеческий перевод. Мы не несём ответственности за любые недоразумения или неправильные толкования, возникшие в результате использования данного перевода.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->