# Налаштування популярних клієнтів хостів MCP

> [!NOTE]
> Конфігурації хостів, які вказують на `/sse`, є застарілими прикладами HTTP+SSE для
> MCP `2025-11-25`. Для MCP `2026-07-28` обирайте Streamable HTTP у хостах, які
> його підтримують, і використовуйте кінцеву точку, налаштовану сервером.

Цей посібник охоплює, як налаштувати та використовувати сервери MCP з популярними AI хост-додатками. Кожен хост має свій підхід до конфігурації, але після налаштування вони всі спілкуються з серверами MCP за допомогою стандартизованого протоколу.

## Що таке MCP хост?

**MCP хост** — це AI-додаток, який може підключатися до серверів MCP для розширення своїх можливостей. Уявіть його як "інтерфейс", з яким взаємодіють користувачі, тоді як сервери MCP надають "фон" інструментів і даних.

```mermaid
flowchart LR
    User[👤 Користувач] --> Host[🖥️ Хост MCP]
    Host --> S1[Сервер MCP А]
    Host --> S2[Сервер MCP Б]
    Host --> S3[Сервер MCP В]
    
    subgraph "Популярні хости"
        H1[Claude Desktop]
        H2[VS Code]
        H3[Cursor]
        H4[Cline]
        H5[Windsurf]
    end
```

## Вимоги

- Сервер MCP для підключення (див. [Модуль 3.1 — Перший сервер](../01-first-server/README.md))
- Встановлений хост-додаток на вашій системі
- Базова обізнаність про файли конфігурації JSON

---

## 1. Claude Desktop

**Claude Desktop** — офіційний десктоп-додаток Anthropic з нативною підтримкою MCP.

### Встановлення

1. Завантажте Claude Desktop з [claude.ai/download](https://claude.ai/download)
2. Встановіть та увійдіть у свій акаунт Anthropic

### Конфігурація

Claude Desktop використовує JSON-файл конфігурації для визначення серверів MCP.

**Розташування файлу конфігурації:**
- **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
- **Windows**: `%APPDATA%\Claude\claude_desktop_config.json`
- **Linux**: `~/.config/Claude/claude_desktop_config.json`

**Приклад конфігурації:**

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

### Опції конфігурації

| Поле | Опис | Приклад |
|-------|-------------|---------|
| `command` | Виконуваний файл для запуску | `"python"`, `"node"`, `"npx"` |
| `args` | Аргументи командного рядка | `["-m", "my_server"]` |
| `env` | Змінні середовища | `{"API_KEY": "xxx"}` |
| `cwd` | Робоча директорія | `"/path/to/server"` |

### Перевірка вашого налаштування

1. Збережіть файл конфігурації
2. Повністю перезапустіть Claude Desktop (закрийте і відкрийте заново)
3. Відкрийте нову розмову
4. Шукайтe значок 🔌, що свідчить про підключені сервери
5. Спробуйте попросити Claude використати один із ваших інструментів

### Виправлення проблем Claude Desktop

**Сервер не з'являється:**
- Перевірте синтаксис файлу конфігурації за допомогою валідатора JSON
- Переконайтеся, що шлях до команди правильний
- Перегляньте логи Claude Desktop: Допомога → Показати Логи

**Сервер аварійно завершує роботу при старті:**
- Спочатку протестуйте сервер вручну у терміналі
- Переконайтеся, що змінні середовища встановлені правильно
- Переконайтеся, що всі залежності встановлені

---

## 2. VS Code з GitHub Copilot

VS Code підтримує MCP через розширення GitHub Copilot Chat.

### Вимоги

1. Встановлений VS Code версії 1.99+
2. Встановлене розширення GitHub Copilot
3. Встановлене розширення GitHub Copilot Chat

### Конфігурація

VS Code використовує `.vscode/mcp.json` у вашому робочому просторі або у налаштуваннях користувача.

**Конфігурація робочого простору** (`.vscode/mcp.json`):

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

**Налаштування користувача** (`settings.json`):

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

### Використання MCP у VS Code

1. Відкрийте панель Copilot Chat (Ctrl+Shift+I / Cmd+Shift+I)
2. Введіть `@` для перегляду доступних MCP інструментів
3. Використовуйте природну мову, щоб викликати інструменти: "Обчислити 25 * 48 за допомогою калькулятора"

### Усунення неполадок VS Code

**MCP сервери не завантажуються:**
- Перевірте панель Виводу → "MCP" на помилки у логах
- Перезавантажте вікно: Ctrl+Shift+P → "Developer: Reload Window"
- Переконайтеся, що сервер запускається окремо

---

## 3. Cursor

**Cursor** — це AI-орієнтований редактор коду з вбудованою підтримкою MCP.

### Встановлення

1. Завантажте Cursor з [cursor.sh](https://cursor.sh)
2. Встановіть та увійдіть

### Конфігурація

Cursor використовує формат конфігурації, схожий на Claude Desktop.

**Розташування файлу конфігурації:**
- **macOS**: `~/.cursor/mcp.json`
- **Windows**: `%USERPROFILE%\.cursor\mcp.json`
- **Linux**: `~/.cursor/mcp.json`

**Приклад конфігурації:**

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

### Використання MCP у Cursor

1. Відкрийте AI чат Cursor (Ctrl+L / Cmd+L)
2. MCP інструменти з'являються автоматично у підказках
3. Попросіть AI виконати завдання, використовуючи підключені сервери

---

## 4. Cline (термінальний клієнт)

**Cline** — термінальний клієнт MCP, ідеальний для робочих процесів командного рядка.

### Встановлення

```bash
npm install -g @anthropic/cline
```

### Конфігурація

Cline використовує змінні середовища та аргументи командного рядка.

**Використання змінних середовища:**

```bash
export ANTHROPIC_API_KEY="your-api-key"
export MCP_SERVER_CALCULATOR="python -m mcp_calculator_server"
```

**Використання аргументів командного рядка:**

```bash
cline --mcp-server "calculator:python -m mcp_calculator_server" \
      --mcp-server "weather:node /path/to/weather/index.js"
```

**Файл конфігурації** (`~/.clinerc`):

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

### Використання Cline

```bash
# Почати інтерактивну сесію
cline

# Одиночний запит з MCP
cline "Calculate the square root of 144 using the calculator"

# Перелік доступних інструментів
cline --list-tools
```

---

## 5. Windsurf

**Windsurf** — ще один AI-редактор коду з підтримкою MCP.

### Встановлення

1. Завантажте Windsurf з [codeium.com/windsurf](https://codeium.com/windsurf)
2. Встановіть та створіть акаунт

### Конфігурація

Конфігурація Windsurf здійснюється через інтерфейс налаштувань:

1. Відкрийте Налаштування (Ctrl+, / Cmd+,)
2. Знайдіть "MCP"
3. Натисніть "Редагувати у settings.json"

**Приклад конфігурації:**

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

## Порівняння типів транспорту

Різні хости підтримують різні механізми транспорту:

| Хост | stdio | SSE/HTTP | WebSocket |
|------|-------|----------|-----------|
| Claude Desktop | ✅ | ❌ | ❌ |
| VS Code | ✅ | ✅ | ❌ |
| Cursor | ✅ | ✅ | ❌ |
| Cline | ✅ | ✅ | ❌ |
| Windsurf | ✅ | ✅ | ❌ |

**stdio** (стандартний ввід/вивід): Найкраще для локальних серверів, що запускаються хостом
**SSE/HTTP**: Найкраще для віддалених серверів або серверів, що використовуються кількома клієнтами

---

## Загальні неполадки

### Сервер не запускається

1. **Спочатку протестуйте сервер вручну:**
   ```bash
   # Для Python
   python -m your_server_module
   
   # Для Node.js
   node /path/to/server/index.js
   ```

2. **Перевірте шлях до команди:**
   - Використовуйте абсолютні шляхи за можливості
   - Переконайтеся, що виконуваний файл у вашому PATH

3. **Перевірте залежності:**
   ```bash
   # Пайтон
   pip list | grep mcp
   
   # Node.js
   npm list @modelcontextprotocol/sdk
   ```

### Сервер підключається, але інструменти не працюють

1. **Перевірте логи сервера** — більшість хостів мають опції логування
2. **Перевірте реєстрацію інструментів** — використовуйте MCP Inspector для тесту
3. **Перевірте дозволи** — деякі інструменти потребують доступу до файлів/мережі

### Змінні середовища не передаються

- Деякі хости очищують змінні середовища
- Використовуйте явне поле `env` у конфігурації
- Уникайте чутливих даних у конфігураційних файлах (використовуйте управління секретами)

---

## Кращі практики безпеки

1. **Ніколи не комітіть API ключі** у конфігураційні файли
2. **Використовуйте змінні середовища** для чутливих даних
3. **Обмежте дозволи сервера** лише тим, що необхідно
4. **Переглядайте код сервера** перед наданням доступу до вашої системи
5. **Використовуйте списки дозволів** для доступу до файлової системи та мережі

---

## Що далі

- [3.13 - Налагодження за допомогою MCP Inspector](../13-mcp-inspector/README.md)
- [3.1 - Створіть свій перший MCP сервер](../01-first-server/README.md)
- [Модуль 5 - Розширені теми](../../05-AdvancedTopics/README.md)

---

## Додаткові ресурси

- [Документація Claude Desktop MCP](https://docs.anthropic.com/en/docs/claude-desktop/mcp)
- [Розширення VS Code MCP](https://marketplace.visualstudio.com/items?itemName=anthropic.claude-mcp)
- [Специфікація MCP - Транспорти](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/)
- [Офіційний реєстр серверів MCP](https://github.com/modelcontextprotocol/servers)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Відмова від відповідальності**:
Цей документ було перекладено за допомогою сервісу штучного інтелекту для перекладу [Co-op Translator](https://github.com/Azure/co-op-translator). Хоча ми прагнемо до точності, будь ласка, майте на увазі, що автоматичні переклади можуть містити помилки або неточності. Оригінальний документ рідною мовою слід вважати авторитетним джерелом. Для критично важливої інформації рекомендується професійний людський переклад. Ми не несемо відповідальності за будь-які непорозуміння або неправильні тлумачення, що виникли внаслідок використання цього перекладу.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->