# MCP-сервер с транспортом stdio

> **⚠️ Важное обновление**: Начиная с спецификации MCP 2025-06-18, автономный транспорт SSE (Server-Sent Events) **устарел** и заменен транспортом "Streamable HTTP". Текущая спецификация MCP определяет два основных транспортных механизма:
> 1. **stdio** — стандартный ввод/вывод (рекомендуется для локальных серверов)
> 2. **Streamable HTTP** — для удалённых серверов, которые могут использовать SSE внутри
>
> Этот урок обновлен с фокусом на **транспорт stdio**, который является рекомендуемым подходом для большинства реализаций MCP серверов.

Транспорт stdio позволяет MCP серверам обмениваться данными с клиентами через стандартные потоки ввода и вывода. Это наиболее часто используемый и рекомендуемый механизм транспорта в текущей спецификации MCP, обеспечивающий простой и эффективный способ создания MCP серверов, которые могут легко интегрироваться с различными клиентскими приложениями.

## Обзор

В этом уроке рассматривается, как создавать и использовать MCP серверы с транспортом stdio.

## Цели обучения

К концу урока вы сможете:

- Создавать MCP сервер с использованием транспорта stdio.
- Отлаживать MCP сервер с помощью Inspector.
- Использовать MCP сервер в Visual Studio Code.
- Понимать текущие механизмы транспорта MCP и причины рекомендаций stdio.

## Транспорт stdio — как это работает

Транспорт stdio — один из двух поддерживаемых типов транспорта в текущей спецификации MCP (2025-06-18). Вот как он работает:

- **Простая коммуникация**: сервер читает сообщения JSON-RPC из стандартного ввода (`stdin`) и отправляет сообщения в стандартный вывод (`stdout`).
- **Основан на процессах**: клиент запускает MCP сервер как подпроцесс.
- **Формат сообщений**: сообщения — это отдельные JSON-RPC запросы, уведомления или ответы, разделённые переноса строк.
- **Логирование**: сервер МОЖЕТ записывать UTF-8 строки в стандартный поток ошибок (`stderr`) для целей логирования.

### Основные требования:
- Сообщения ДОЛЖНЫ разделяться переносами строк и НЕ ДОЛЖНЫ содержать встроенные переводы строк.
- Сервер НЕ ДОЛЖЕН писать в `stdout` ничего, что не является допустимым сообщением MCP.
- Клиент НЕ ДОЛЖЕН писать в `stdin` сервера ничего, что не является допустимым сообщением MCP.

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

В приведённом коде:

- Мы импортируем класс `Server` и `StdioServerTransport` из MCP SDK.
- Создаем экземпляр сервера с базовой конфигурацией и возможностями.

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

- Создаем экземпляр сервера с использованием MCP SDK.
- Определяем инструменты с помощью декораторов.
- Используем контекстный менеджер stdio_server для работы с транспортом.

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

Ключевое отличие от SSE — это то, что серверы stdio:

- Не требуют настройки веб-сервера или HTTP-эндпоинтов.
- Запускаются как подпроцессы клиентом.
- Общаются через потоки stdin/stdout.
- Проще в реализации и отладке.

## Задание: создание сервера stdio

Для создания нашего сервера нужно помнить два момента:

- Необходимо использовать веб-сервер для предоставления конечных точек для соединения и сообщений.
## Лабораторная работа: создание простого MCP stdio сервера

В этой лабораторной работе мы создадим простой MCP сервер, используя рекомендуемый транспорт stdio. Этот сервер предоставит инструменты, которые клиенты смогут вызывать с помощью стандартного протокола Model Context Protocol.

### Требования к окружению

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

## Главное отличие от устаревшего подхода SSE

**Транспорт stdio (текущий стандарт):**
- Простая модель подпроцесса — клиент запускает сервер как дочерний процесс
- Обмен данными через stdin/stdout с использованием сообщений JSON-RPC
- Не требуется настройка HTTP сервера
- Лучшая производительность и безопасность
- Проще отлаживать и разрабатывать

**Транспорт SSE (устаревший с MCP 2025-06-18):**
- Требовался HTTP сервер с SSE конечными точками
- Более сложная настройка с инфраструктурой веб-сервера
- Дополнительные требования безопасности для HTTP конечных точек
- Теперь заменён на Streamable HTTP для веб-сценариев

### Создание сервера с транспортом stdio

Для создания сервера stdio необходимо:

1. **Импортировать необходимые библиотеки** — нужны компоненты MCP сервера и транспорт stdio
2. **Создать экземпляр сервера** — определить сервер с его возможностями
3. **Определить инструменты** — добавить функциональность, которую хотим предоставить
4. **Настроить транспорт** — сконфигурировать stdio коммуникацию
5. **Запустить сервер** — стартовать сервер и обрабатывать сообщения

Пойдем по шагам:

### Шаг 1: Создайте базовый stdio сервер

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server

# Настроить ведение журнала
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

### Шаг 2: Добавьте больше инструментов

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

Сохраните код как `server.py` и запустите из командной строки:

```bash
python server.py
```

Сервер запустится и будет ждать входных данных из stdin. Он общается с помощью сообщений JSON-RPC через транспорт stdio.

### Шаг 4: Тестирование с помощью Inspector

Вы можете протестировать свой сервер с MCP Inspector:

1. Установите Inspector: `npx @modelcontextprotocol/inspector`
2. Запустите Inspector и укажите на ваш сервер
3. Проверьте инструменты, которые вы создали

### .NET

```csharp
var builder = WebApplication.CreateBuilder(args);
builder.Services
    .AddMcpServer();
 ```
## Отладка вашего stdio сервера

### Использование MCP Inspector

MCP Inspector — полезный инструмент для отладки и тестирования MCP серверов. Вот как использовать его с сервером stdio:

1. **Установите Inspector**:
   ```bash
   npx @modelcontextprotocol/inspector
   ```

2. **Запустите Inspector**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

3. **Проверьте сервер**: Inspector предоставляет веб-интерфейс, где вы можете:
   - Просмотреть возможности сервера
   - Тестировать инструменты с разными параметрами
   - Мониторить JSON-RPC сообщения
   - Отлаживать проблемы с соединением

### Использование VS Code

Также вы можете отлаживать MCP сервер напрямую в VS Code:

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

### Общие советы для отладки

- Используйте `stderr` для логирования — никогда не пишите в `stdout`, так как он зарезервирован для сообщений MCP
- Убедитесь, что все сообщения JSON-RPC разделены переносами строк
- Сначала тестируйте простые инструменты, прежде чем добавлять сложные функции
- Используйте Inspector для проверки форматов сообщений

## Использование вашего stdio сервера в VS Code

После того, как вы создали MCP stdio сервер, можно интегрировать его с VS Code для использования с Claude или другими клиентами совместимыми с MCP.

### Конфигурация

1. **Создайте конфигурационный файл MCP** в `%APPDATA%\Claude\claude_desktop_config.json` (Windows) или `~/Library/Application Support/Claude/claude_desktop_config.json` (Mac):

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

2. **Перезапустите Claude**: закройте и откройте Claude заново, чтобы загрузить новую конфигурацию сервера.

3. **Проверьте соединение**: начните разговор с Claude и попробуйте использовать инструменты вашего сервера:
   - "Можешь поздороваться с помощью инструмента приветствия?"
   - "Вычисли сумму 15 и 27"
   - "Какая информация о сервере?"

### Пример stdio сервера на TypeScript

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

В этом обновленном уроке вы узнали, как:

- Создавать MCP серверы с использованием текущего **транспорта stdio** (рекомендуемый подход)
- Понять, почему транспорт SSE устарел в пользу stdio и Streamable HTTP
- Создавать инструменты, которые могут вызываться клиентами MCP
- Отлаживать сервер с помощью MCP Inspector
- Интегрировать ваш stdio сервер с VS Code и Claude

Транспорт stdio обеспечивает более простой, безопасный и производительный способ создания MCP серверов по сравнению с устаревшим подходом SSE. Это рекомендуемый транспорт для большинства реализаций MCP серверов по состоянию на спецификацию 2025-06-18.

### .NET

1. Сначала создадим несколько инструментов, для этого создадим файл *Tools.cs* со следующим содержимым:

  ```csharp
  using System.ComponentModel;
  using System.Text.Json;
  using ModelContextProtocol.Server;
  ```

## Задание: тестирование вашего stdio сервера

Теперь, когда вы создали ваш stdio сервер, давайте его протестируем, чтобы убедиться, что он работает правильно.

### Требования

1. Убедитесь, что MCP Inspector установлен:
   ```bash
   npm install -g @modelcontextprotocol/inspector
   ```

2. Ваш код сервера должен быть сохранён (например, `server.py`)

### Тестирование с Inspector

1. **Запустите Inspector с вашим сервером**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

2. **Откройте веб-интерфейс**: Inspector откроет браузер, показывающий возможности вашего сервера.

3. **Проверьте инструменты**:
   - Попробуйте инструмент `get_greeting` с разными именами
   - Проверьте инструмент `calculate_sum` с разными числами
   - Вызовите инструмент `get_server_info`, чтобы увидеть метаданные сервера

4. **Мониторинг связи**: Inspector отображает JSON-RPC сообщения, которые обмениваются клиент и сервер.

### Что вы должны видеть

При правильном запуске сервера вы должны увидеть:
- Возможности сервера, перечисленные в Inspector
- Доступные для тестирования инструменты
- Успешный обмен JSON-RPC сообщениями
- Отображение ответов инструментов в интерфейсе

### Частые проблемы и решения

**Сервер не запускается:**
- Проверьте установку всех зависимостей: `pip install mcp`
- Проверьте синтаксис и отступы Python
- Ищите сообщения об ошибках в консоли

**Инструменты не отображаются:**
- Убедитесь, что есть декораторы `@server.tool()`
- Проверьте, что функции инструментов объявлены до `main()`
- Убедитесь, что сервер корректно настроен

**Проблемы с соединением:**
- Убедитесь, что сервер использует транспорт stdio правильно
- Проверьте, нет ли конфликтов с другими процессами
- Проверьте правильность команды запуска Inspector

## Домашнее задание

Попробуйте расширить ваш сервер дополнительными возможностями. Например, посетите [эту страницу](https://api.chucknorris.io/) и добавьте инструмент, который обращается к API. Решайте, каким должен быть сервер. Удачи :)

## Решение

[Решение](./solution/README.md) Вот возможное решение с рабочим кодом.

## Основные выводы

Ключевые моменты из этого раздела:

- Транспорт stdio — рекомендуемый механизм для локальных MCP серверов.
- Транспорт stdio обеспечивает беспроблемный обмен данными между MCP серверами и клиентами через стандартные потоки ввода/вывода.
- Вы можете использовать как Inspector, так и Visual Studio Code для непосредственного использования stdio серверов, что упрощает отладку и интеграцию.

## Примеры

- [Калькулятор на Java](../samples/java/calculator/README.md)
- [Калькулятор на .Net](../../../../03-GettingStarted/samples/csharp)
- [Калькулятор на JavaScript](../samples/javascript/README.md)
- [Калькулятор на TypeScript](../samples/typescript/README.md)
- [Калькулятор на Python](../../../../03-GettingStarted/samples/python) 

## Дополнительные ресурсы

- [SSE](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events)

## Что дальше

## Следующие шаги

Теперь, когда вы узнали, как создавать MCP серверы с транспортом stdio, вы можете изучить более продвинутые темы:

- **Далее**: [HTTP Streaming с MCP (Streamable HTTP)](../06-http-streaming/README.md) — узнайте о другом поддерживаемом механизме транспорта для удалённых серверов
- **Продвинуто**: [Лучшие практики безопасности MCP](../../02-Security/README.md) — реализуйте безопасность в ваших MCP серверах
- **В продакшн**: [Стратегии деплоя](../09-deployment/README.md) — разверните ваши серверы для производственного использования

## Дополнительные ресурсы

- [Спецификация MCP 2025-06-18](https://spec.modelcontextprotocol.io/specification/) — официальная спецификация
- [Документация MCP SDK](https://github.com/modelcontextprotocol/sdk) — справочники по SDK для всех языков
- [Примеры сообщества](../../06-CommunityContributions/README.md) — дополнительные примеры серверов от сообщества

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Отказ от ответственности**:  
Этот документ был переведен с помощью сервиса машинного перевода [Co-op Translator](https://github.com/Azure/co-op-translator). Несмотря на наши усилия обеспечить точность, просим учитывать, что автоматический перевод может содержать ошибки или неточности. Оригинальный документ на его родном языке следует считать авторитетным источником. Для получения критически важной информации рекомендуется использовать профессиональный перевод, выполненный человеком. Мы не несем ответственности за любые недоразумения или неправильные толкования, возникшие в результате использования данного перевода.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->