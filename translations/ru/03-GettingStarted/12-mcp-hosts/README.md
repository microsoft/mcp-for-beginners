# Настройка популярных клиентов хоста MCP

> [!NOTE]
> Конфигурации хоста, указывающие на `/sse`, являются устаревшими примерами HTTP+SSE для
> MCP `2025-11-25`. Для MCP `2026-07-28` выберите Streamable HTTP в хостах, которые
> поддерживают его, и используйте конечную точку, настроенную сервером.

В этом руководстве описывается, как настроить и использовать MCP-серверы с популярными AI-приложениями для хоста. У каждого хоста свой подход к конфигурации, но после настройки все они взаимодействуют с MCP-серверами с помощью стандартизированного протокола.

## Что такое MCP-хост?

**MCP-хост** — это AI-приложение, которое может подключаться к MCP-серверам для расширения своих возможностей. Можно представить его как "передний план", с которым взаимодействуют пользователи, а MCP-серверы предоставляют "задний план" с инструментами и данными.

```mermaid
flowchart LR
    User[👤 Пользователь] --> Host[🖥️ MCP Хост]
    Host --> S1[MCP Сервер A]
    Host --> S2[MCP Сервер B]
    Host --> S3[MCP Сервер C]
    
    subgraph "Популярные хосты"
        H1[Claude Desktop]
        H2[VS Code]
        H3[Cursor]
        H4[Cline]
        H5[Windsurf]
    end
```

## Требования

- MCP-сервер для подключения (см. [Модуль 3.1 - Первый сервер](../01-first-server/README.md))
- Приложение хоста установлено на вашей системе
- Базовые знания о JSON-файлах конфигурации

---

## 1. Claude Desktop

**Claude Desktop** — официальное настольное приложение Anthropic с нативной поддержкой MCP.

### Установка

1. Скачайте Claude Desktop с [claude.ai/download](https://claude.ai/download)
2. Установите и войдите в систему с помощью своей учётной записи Anthropic

### Конфигурация

Claude Desktop использует JSON-файл конфигурации для определения MCP-серверов.

**Расположение файла конфигурации:**
- **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
- **Windows**: `%APPDATA%\Claude\claude_desktop_config.json`
- **Linux**: `~/.config/Claude/claude_desktop_config.json`

**Пример конфигурации:**

```json
{
  "mcpServers": {
    "calculator": {
      "command": "python",
      "args": ["-m", "mcp_calculator_server"],
      "env": {
        "PYTHONPATH": "/path/to/your/server"
      }
    },
    "weather": {
      "command": "node",
      "args": ["/path/to/weather-server/build/index.js"]
    },
    "database": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-postgres"],
      "env": {
        "DATABASE_URL": "postgresql://user:pass@localhost/mydb"
      }
    }
  }
}
```

### Параметры конфигурации

| Поле | Описание | Пример |
|-------|-------------|---------|
| `command` | Исполняемый файл для запуска | `"python"`, `"node"`, `"npx"` |
| `args` | Аргументы командной строки | `["-m", "my_server"]` |
| `env` | Переменные окружения | `{"API_KEY": "xxx"}` |
| `cwd` | Рабочая директория | `"/path/to/server"` |

### Проверка настройки

1. Сохраните файл конфигурации
2. Полностью перезапустите Claude Desktop (закройте и откройте заново)
3. Откройте новый разговор
4. Обратите внимание на значок 🔌, указывающий на подключённые серверы
5. Попробуйте попросить Claude использовать один из ваших инструментов

### Устранение неполадок Claude Desktop

**Сервер не появляется:**
- Проверьте синтаксис файла конфигурации с помощью JSON-валидатора
- Убедитесь, что путь к команде правильный
- Проверьте логи Claude Desktop: Help → Show Logs

**Сервер падает при запуске:**
- Сначала протестируйте сервер вручную в терминале
- Проверьте корректность переменных окружения
- Убедитесь, что все зависимости установлены

---

## 2. VS Code с GitHub Copilot

VS Code поддерживает MCP через расширения GitHub Copilot Chat.

### Требования

1. Установлен VS Code версии 1.99+
2. Установлено расширение GitHub Copilot
3. Установлено расширение GitHub Copilot Chat

### Конфигурация

VS Code использует файл `.vscode/mcp.json` в рабочей области или в пользовательских настройках.

**Конфигурация рабочей области** (`.vscode/mcp.json`):

```json
{
  "servers": {
    "my-calculator": {
      "type": "stdio",
      "command": "python",
      "args": ["-m", "mcp_calculator_server"]
    },
    "my-database": {
      "type": "sse",
      "url": "http://localhost:8080/sse"
    }
  }
}
```

**Пользовательские настройки** (`settings.json`):

```json
{
  "mcp.servers": {
    "global-server": {
      "type": "stdio",
      "command": "npx",
      "args": ["-y", "@anthropic/mcp-server-memory"]
    }
  },
  "mcp.enableLogging": true
}
```

### Использование MCP в VS Code

1. Откройте панель Copilot Chat (Ctrl+Shift+I / Cmd+Shift+I)
2. Наберите `@`, чтобы увидеть доступные инструменты MCP
3. Используйте естественный язык для вызова инструментов: "Вычисли 25 * 48 с помощью калькулятора"

### Устранение неполадок VS Code

**MCP-серверы не загружаются:**
- Проверьте панель Output → "MCP" на наличие ошибок
- Перезагрузите окно: Ctrl+Shift+P → "Developer: Reload Window"
- Убедитесь, что сервер запускается самостоятельно

---

## 3. Cursor

**Cursor** — AI-ориентированный редактор кода с встроенной поддержкой MCP.

### Установка

1. Скачайте Cursor с [cursor.sh](https://cursor.sh)
2. Установите и войдите в систему

### Конфигурация

Cursor использует формат конфигурации, похожий на Claude Desktop.

**Расположение файла конфигурации:**
- **macOS**: `~/.cursor/mcp.json`
- **Windows**: `%USERPROFILE%\.cursor\mcp.json`
- **Linux**: `~/.cursor/mcp.json`

**Пример конфигурации:**

```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "/path/to/allowed/directory"]
    },
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_TOKEN": "ghp_your_token_here"
      }
    }
  }
}
```

### Использование MCP в Cursor

1. Откройте AI-чат Cursor (Ctrl+L / Cmd+L)
2. Инструменты MCP появляются автоматически в подсказках
3. Попросите AI выполнить задачи, используя подключённые серверы

---

## 4. Cline (Терминальный клиент)

**Cline** — терминальный клиент MCP, идеальный для работы из командной строки.

### Установка

```bash
npm install -g @anthropic/cline
```

### Конфигурация

Cline использует переменные окружения и аргументы командной строки.

**Использование переменных окружения:**

```bash
export ANTHROPIC_API_KEY="your-api-key"
export MCP_SERVER_CALCULATOR="python -m mcp_calculator_server"
```

**Использование аргументов командной строки:**

```bash
cline --mcp-server "calculator:python -m mcp_calculator_server" \
      --mcp-server "weather:node /path/to/weather/index.js"
```

**Файл конфигурации** (`~/.clinerc`):

```json
{
  "apiKey": "your-api-key",
  "mcpServers": {
    "calculator": {
      "command": "python",
      "args": ["-m", "mcp_calculator_server"]
    }
  }
}
```

### Использование Cline

```bash
# Начать интерактивную сессию
cline

# Один запрос с MCP
cline "Calculate the square root of 144 using the calculator"

# Перечислить доступные инструменты
cline --list-tools
```

---

## 5. Windsurf

**Windsurf** — ещё один AI-редактор кода с поддержкой MCP.

### Установка

1. Скачайте Windsurf с [codeium.com/windsurf](https://codeium.com/windsurf)
2. Установите и создайте учётную запись

### Конфигурация

Конфигурация Windsurf управляется через пользовательский интерфейс настроек:

1. Откройте настройки (Ctrl+, / Cmd+,)
2. Найдите "MCP"
3. Нажмите "Edit in settings.json"

**Пример конфигурации:**

```json
{
  "windsurf.mcp.servers": {
    "my-tools": {
      "command": "python",
      "args": ["/path/to/server.py"],
      "env": {}
    }
  },
  "windsurf.mcp.enabled": true
}
```

---

## Сравнение типов транспорта

Разные хосты поддерживают разные механизмы передачи данных:

| Хост | stdio | SSE/HTTP | WebSocket |
|------|-------|----------|-----------|
| Claude Desktop | ✅ | ❌ | ❌ |
| VS Code | ✅ | ✅ | ❌ |
| Cursor | ✅ | ✅ | ❌ |
| Cline | ✅ | ✅ | ❌ |
| Windsurf | ✅ | ✅ | ❌ |

**stdio** (стандартный ввод/вывод): Лучшее для локальных серверов, запущенных хостом
**SSE/HTTP**: Лучшее для удалённых серверов или серверов, используемых несколькими клиентами

---

## Общие советы по устранению неполадок

### Сервер не запускается

1. **Сначала протестируйте сервер вручную:**
   ```bash
   # Для Python
   python -m your_server_module
   
   # Для Node.js
   node /path/to/server/index.js
   ```

2. **Проверьте путь к команде:**
   - По возможности используйте абсолютные пути
   - Убедитесь, что исполняемый файл находится в PATH

3. **Проверьте зависимости:**
   ```bash
   # Python
   pip list | grep mcp
   
   # Node.js
   npm list @modelcontextprotocol/sdk
   ```

### Сервер подключается, но инструменты не работают

1. **Проверьте логи сервера** — большинство хостов имеют опции логирования
2. **Проверьте регистрацию инструментов** — используйте MCP Inspector для теста
3. **Проверьте разрешения** — некоторым инструментам нужен доступ к файлам/сети

### Переменные окружения не передаются

- Некоторые хосты фильтруют переменные окружения
- Явно используйте поле `env` в конфигурации
- Избегайте хранения чувствительных данных в файлах конфигурации (используйте управление секретами)

---

## Рекомендации по безопасности

1. **Никогда не коммитьте ключи API** в файлы конфигурации
2. **Используйте переменные окружения** для чувствительных данных
3. **Ограничивайте разрешения сервера** только необходимыми
4. **Проверяйте код сервера** перед предоставлением доступа к системе
5. **Используйте белые списки** для доступа к файловой системе и сети

---

## Что дальше

- [3.13 - Отладка с MCP Inspector](../13-mcp-inspector/README.md)
- [3.1 - Создание вашего первого MCP сервера](../01-first-server/README.md)
- [Модуль 5 - Продвинутые темы](../../05-AdvancedTopics/README.md)

---

## Дополнительные ресурсы

- [Документация Claude Desktop MCP](https://docs.anthropic.com/en/docs/claude-desktop/mcp)
- [Расширение MCP для VS Code](https://marketplace.visualstudio.com/items?itemName=anthropic.claude-mcp)
- [Спецификация MCP - Транспорты](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/)
- [Официальный реестр MCP-серверов](https://github.com/modelcontextprotocol/servers)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Отказ от ответственности**:
Этот документ был переведен с использованием сервиса машинного перевода [Co-op Translator](https://github.com/Azure/co-op-translator). Несмотря на наши усилия по обеспечению точности, имейте в виду, что автоматический перевод может содержать ошибки или неточности. Оригинальный документ на его исходном языке следует считать авторитетным источником. Для получения критически важной информации рекомендуется обратиться к профессиональному человеческому переводу. Мы не несем ответственности за любые недоразумения или неправильные толкования, возникшие в результате использования этого перевода.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->