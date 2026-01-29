# MCP Server с транспортом stdio

> **⚠️ Важное обновление**: Начиная с MCP Specification 2025-06-18, отдельный транспорт SSE (Server-Sent Events) был **устаревшим** и заменен на транспорт "Streamable HTTP". Текущая спецификация MCP определяет два основных механизма транспорта:
> 1. **stdio** - Стандартный ввод/вывод (рекомендуется для локальных серверов)
> 2. **Streamable HTTP** - Для удаленных серверов, которые могут использовать SSE внутри
>
> Этот урок обновлен, чтобы сосредоточиться на **транспорте stdio**, который является рекомендуемым подходом для большинства реализаций MCP серверов.

Транспорт stdio позволяет MCP серверам взаимодействовать с клиентами через стандартные потоки ввода и вывода. Это наиболее часто используемый и рекомендуемый механизм транспорта в текущей спецификации MCP, обеспечивающий простой и эффективный способ создания MCP серверов, которые легко интегрируются с различными клиентскими приложениями.

## Обзор

Этот урок охватывает создание и использование MCP серверов с использованием транспорта stdio.

## Цели обучения

К концу этого урока вы сможете:

- Создавать MCP сервер с использованием транспорта stdio.
- Отлаживать MCP сервер с помощью Inspector.
- Использовать MCP сервер в Visual Studio Code.
- Понять текущие механизмы транспорта MCP и почему рекомендуется stdio.

## Транспорт stdio - как это работает

Транспорт stdio является одним из двух поддерживаемых типов транспорта в текущей спецификации MCP (2025-06-18). Вот как он работает:

- **Простая коммуникация**: Сервер читает сообщения JSON-RPC из стандартного ввода (`stdin`) и отправляет сообщения в стандартный вывод (`stdout`).
- **Процессный подход**: Клиент запускает MCP сервер как подпроцесс.
- **Формат сообщений**: Сообщения представляют собой отдельные запросы, уведомления или ответы JSON-RPC, разделенные символами новой строки.
- **Логирование**: Сервер МОЖЕТ записывать строки в формате UTF-8 в стандартный поток ошибок (`stderr`) для целей логирования.

### Основные требования:
- Сообщения ДОЛЖНЫ быть разделены символами новой строки и НЕ ДОЛЖНЫ содержать встроенные символы новой строки.
- Сервер НЕ ДОЛЖЕН записывать в `stdout` ничего, кроме валидных сообщений MCP.
- Клиент НЕ ДОЛЖЕН записывать в `stdin` сервера ничего, кроме валидных сообщений MCP.

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

В приведенном выше коде:

- Мы импортируем класс `Server` и `StdioServerTransport` из MCP SDK.
- Мы создаем экземпляр сервера с базовой конфигурацией и возможностями.

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

В приведенном выше коде мы:

- Создаем экземпляр сервера с использованием MCP SDK.
- Определяем инструменты с помощью декораторов.
- Используем контекстный менеджер stdio_server для управления транспортом.

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

Ключевое отличие от SSE заключается в том, что stdio серверы:

- Не требуют настройки веб-сервера или HTTP-эндпоинтов.
- Запускаются как подпроцессы клиентом.
- Общаются через потоки stdin/stdout.
- Проще в реализации и отладке.

## Упражнение: Создание stdio сервера

Для создания нашего сервера нужно учитывать два момента:

- Нам нужно использовать веб-сервер для предоставления точек подключения и сообщений.

## Лабораторная работа: Создание простого MCP stdio сервера

В этой лабораторной работе мы создадим простой MCP сервер с использованием рекомендуемого транспорта stdio. Этот сервер будет предоставлять инструменты, которые клиенты могут вызывать с использованием стандартного протокола Model Context Protocol.

### Предварительные требования

- Python 3.8 или новее.
- MCP Python SDK: `pip install mcp`.
- Базовое понимание асинхронного программирования.

Начнем с создания нашего первого MCP stdio сервера:

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

## Основные отличия от устаревшего подхода SSE

**Транспорт stdio (текущий стандарт):**
- Простая модель подпроцесса - клиент запускает сервер как дочерний процесс.
- Коммуникация через stdin/stdout с использованием сообщений JSON-RPC.
- Не требуется настройка веб-сервера.
- Лучшая производительность и безопасность.
- Проще в отладке и разработке.

**Транспорт SSE (устарел с MCP 2025-06-18):**
- Требовал веб-сервера с SSE-эндпоинтами.
- Более сложная настройка с инфраструктурой веб-сервера.
- Дополнительные соображения безопасности для HTTP-эндпоинтов.
- Теперь заменен на Streamable HTTP для веб-сценариев.

### Создание сервера с транспортом stdio

Чтобы создать stdio сервер, нужно:

1. **Импортировать необходимые библиотеки** - Нам понадобятся компоненты MCP сервера и транспорт stdio.
2. **Создать экземпляр сервера** - Определить сервер с его возможностями.
3. **Определить инструменты** - Добавить функциональность, которую мы хотим предоставить.
4. **Настроить транспорт** - Конфигурировать коммуникацию через stdio.
5. **Запустить сервер** - Запустить сервер и обрабатывать сообщения.

Давайте создадим это шаг за шагом:

### Шаг 1: Создание базового stdio сервера

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

### Шаг 2: Добавление дополнительных инструментов

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

Сервер запустится и будет ожидать ввода через stdin. Он общается с использованием сообщений JSON-RPC через транспорт stdio.

### Шаг 4: Тестирование с помощью Inspector

Вы можете протестировать ваш сервер с помощью MCP Inspector:

1. Установите Inspector: `npx @modelcontextprotocol/inspector`.
2. Запустите Inspector и укажите путь к вашему серверу.
3. Протестируйте созданные инструменты.

### .NET

```csharp
var builder = WebApplication.CreateBuilder(args);
builder.Services
    .AddMcpServer();
 ```

## Отладка вашего stdio сервера

### Использование MCP Inspector

MCP Inspector - это ценный инструмент для отладки и тестирования MCP серверов. Вот как его использовать с вашим stdio сервером:

1. **Установите Inspector**:
   ```bash
   npx @modelcontextprotocol/inspector
   ```

2. **Запустите Inspector**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

3. **Протестируйте ваш сервер**: Inspector предоставляет веб-интерфейс, где вы можете:
   - Просматривать возможности сервера.
   - Тестировать инструменты с различными параметрами.
   - Отслеживать сообщения JSON-RPC.
   - Отлаживать проблемы с подключением.

### Использование VS Code

Вы также можете отлаживать ваш MCP сервер прямо в VS Code:

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

2. Установите точки останова в коде сервера.
3. Запустите отладчик и протестируйте с помощью Inspector.

### Общие советы по отладке

- Используйте `stderr` для логирования - никогда не записывайте в `stdout`, так как он зарезервирован для сообщений MCP.
- Убедитесь, что все сообщения JSON-RPC разделены символами новой строки.
- Сначала тестируйте с простыми инструментами, прежде чем добавлять сложный функционал.
- Используйте Inspector для проверки форматов сообщений.

## Использование вашего stdio сервера в VS Code

После создания MCP stdio сервера вы можете интегрировать его с VS Code для использования с Claude или другими клиентами, совместимыми с MCP.

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

2. **Перезапустите Claude**: Закройте и снова откройте Claude, чтобы загрузить новую конфигурацию сервера.

3. **Протестируйте подключение**: Начните разговор с Claude и попробуйте использовать инструменты вашего сервера:
   - "Можешь поприветствовать меня с помощью инструмента приветствия?"
   - "Вычисли сумму 15 и 27."
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

## Резюме

В этом обновленном уроке вы узнали, как:

- Создавать MCP серверы с использованием текущего **транспорта stdio** (рекомендуемый подход).
- Понять, почему транспорт SSE был устаревшим в пользу stdio и Streamable HTTP.
- Создавать инструменты, которые могут вызываться клиентами MCP.
- Отлаживать ваш сервер с помощью MCP Inspector.
- Интегрировать ваш stdio сервер с VS Code и Claude.

Транспорт stdio предоставляет более простой, безопасный и производительный способ создания MCP серверов по сравнению с устаревшим подходом SSE. Это рекомендуемый транспорт для большинства реализаций MCP серверов начиная с спецификации 2025-06-18.

### .NET

1. Сначала создадим несколько инструментов, для этого создадим файл *Tools.cs* со следующим содержимым:

  ```csharp
  using System.ComponentModel;
  using System.Text.Json;
  using ModelContextProtocol.Server;
  ```

## Упражнение: Тестирование вашего stdio сервера

Теперь, когда вы создали stdio сервер, давайте протестируем его, чтобы убедиться, что он работает корректно.

### Предварительные требования

1. Убедитесь, что MCP Inspector установлен:
   ```bash
   npm install -g @modelcontextprotocol/inspector
   ```

2. Ваш код сервера должен быть сохранен (например, как `server.py`).

### Тестирование с помощью Inspector

1. **Запустите Inspector с вашим сервером**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

2. **Откройте веб-интерфейс**: Inspector откроет окно браузера, показывающее возможности вашего сервера.

3. **Протестируйте инструменты**: 
   - Попробуйте инструмент `get_greeting` с разными именами.
   - Протестируйте инструмент `calculate_sum` с различными числами.
   - Вызовите инструмент `get_server_info`, чтобы увидеть метаданные сервера.

4. **Отслеживайте коммуникацию**: Inspector показывает сообщения JSON-RPC, обмениваемые между клиентом и сервером.

### Что вы должны увидеть

Когда ваш сервер запускается корректно, вы должны увидеть:
- Возможности сервера, перечисленные в Inspector.
- Инструменты, доступные для тестирования.
- Успешный обмен сообщениями JSON-RPC.
- Ответы инструментов, отображаемые в интерфейсе.

### Общие проблемы и их решения

**Сервер не запускается:**
- Проверьте, что все зависимости установлены: `pip install mcp`.
- Убедитесь в правильности синтаксиса Python и отступов.
- Проверьте сообщения об ошибках в консоли.

**Инструменты не отображаются:**
- Убедитесь, что декораторы `@server.tool()` присутствуют.
- Проверьте, что функции инструментов определены до `main()`.
- Убедитесь, что сервер правильно настроен.

**Проблемы с подключением:**
- Убедитесь, что сервер правильно использует транспорт stdio.
- Проверьте, что другие процессы не мешают.
- Убедитесь в правильности синтаксиса команды Inspector.

## Задание

Попробуйте расширить ваш сервер, добавив больше возможностей. Например, используйте [эту страницу](https://api.chucknorris.io/), чтобы добавить инструмент, который вызывает API. Вы сами решаете, как должен выглядеть сервер. Удачи :)

## Решение

[Решение](./solution/README.md) Вот возможное решение с рабочим кодом.

## Основные выводы

Основные выводы из этой главы:

- Транспорт stdio является рекомендуемым механизмом для локальных MCP серверов.
- Транспорт stdio позволяет бесшовно взаимодействовать между MCP серверами и клиентами с использованием стандартных потоков ввода и вывода.
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

- **Далее**: [HTTP Streaming с MCP (Streamable HTTP)](../06-http-streaming/README.md) - Узнайте о другом поддерживаемом механизме транспорта для удаленных серверов.
- **Продвинутое**: [Лучшие практики безопасности MCP](../../02-Security/README.md) - Реализуйте безопасность в ваших MCP серверах.
- **В продакшн**: [Стратегии развертывания](../09-deployment/README.md) - Разверните ваши серверы для использования в продакшне.

## Дополнительные ресурсы

- [MCP Specification 2025-06-18](https://spec.modelcontextprotocol.io/specification/) - Официальная спецификация.
- [Документация MCP SDK](https://github.com/modelcontextprotocol/sdk) - Справочные материалы по SDK для всех языков.
- [Примеры сообщества](../../06-CommunityContributions/README.md) - Больше примеров серверов от сообщества.

---

**Отказ от ответственности**:  
Этот документ был переведен с помощью сервиса автоматического перевода [Co-op Translator](https://github.com/Azure/co-op-translator). Хотя мы стремимся к точности, пожалуйста, имейте в виду, что автоматические переводы могут содержать ошибки или неточности. Оригинальный документ на его родном языке следует считать авторитетным источником. Для получения критически важной информации рекомендуется профессиональный перевод человеком. Мы не несем ответственности за любые недоразумения или неправильные интерпретации, возникающие в результате использования данного перевода.