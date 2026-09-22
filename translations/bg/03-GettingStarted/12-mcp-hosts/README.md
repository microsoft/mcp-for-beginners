# Настройване на популярни MCP хост клиенти

> [!NOTE]
> Конфигурациите на хостове, които сочат към `/sse`, са стари примери за HTTP+SSE
> за MCP `2025-11-25`. За MCP `2026-07-28` изберете Streamable HTTP в хостове, които
> го поддържат и използвайте крайна точка, конфигурирана от сървъра.

Това ръководство обхваща как да конфигурирате и използвате MCP сървъри с популярни AI хост приложения. Всеки хост има свой собствен подход за конфигурация, но след настройване, всички комуникират с MCP сървъри чрез стандартизирания протокол.

## Какво е MCP хост?

**MCP хост** е AI приложение, което може да се свърже с MCP сървъри, за да разшири своите възможности. Мислете за него като за "потребителския интерфейс", с който взаимодействат потребителите, докато MCP сървърите предоставят "задния край" с инструменти и данни.

```mermaid
flowchart LR
    User[👤 Потребител] --> Host[🖥️ MCP Хост]
    Host --> S1[MCP Сървър A]
    Host --> S2[MCP Сървър B]
    Host --> S3[MCP Сървър C]
    
    subgraph "Популярни хостове"
        H1[Claude Desktop]
        H2[VS Code]
        H3[Cursor]
        H4[Cline]
        H5[Windsurf]
    end
```

## Предварителни изисквания

- MCP сървър, към който да се свържете (вижте [Модул 3.1 - Първи сървър](../01-first-server/README.md))
- Хост приложението инсталирано на вашата система
- Основни познания за JSON конфигурационни файлове

---

## 1. Claude Desktop

**Claude Desktop** е официалното десктоп приложение на Anthropic, което поддържа MCP нативно.

### Инсталация

1. Свалете Claude Desktop от [claude.ai/download](https://claude.ai/download)
2. Инсталирайте и влезте с вашия Anthropic акаунт

### Конфигурация

Claude Desktop използва JSON конфигурационен файл за дефиниране на MCP сървъри.

**Местоположение на конфигурационния файл:**
- **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
- **Windows**: `%APPDATA%\Claude\claude_desktop_config.json`
- **Linux**: `~/.config/Claude/claude_desktop_config.json`

**Примерна конфигурация:**

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

### Опции за конфигурация

| Поле | Описание | Пример |
|-------|-------------|---------|
| `command` | Изпълнимият файл за стартиране | `"python"`, `"node"`, `"npx"` |
| `args` | Аргументи на командния ред | `["-m", "my_server"]` |
| `env` | Променливи на средата | `{"API_KEY": "xxx"}` |
| `cwd` | Работна директория | `"/path/to/server"` |

### Тестване на вашата настройка

1. Запазете конфигурационния файл
2. Рестартирайте напълно Claude Desktop (излезте и го стартирайте отново)
3. Отворете нов разговор
4. Потърсете иконата 🔌, показваща свързани сървъри
5. Опитайте да помолите Claude да използва един от вашите инструменти

### Отстраняване на проблеми с Claude Desktop

**Сървърът не се показва:**
- Проверете синтаксиса на конфигурационния файл с JSON валидатор
- Уверете се, че пътят към командата е правилен
- Проверете логовете на Claude Desktop: Помощ → Покажи логове

**Сървърът пада при стартиране:**
- Тествайте сървъра ръчно първо в терминала
- Проверете дали променливите на средата са правилно зададени
- Уверете се, че всички зависимости са инсталирани

---

## 2. VS Code с GitHub Copilot

VS Code поддържа MCP чрез разширенията GitHub Copilot Chat.

### Предварителни изисквания

1. Инсталиран VS Code версия 1.99+
2. Инсталирано разширение GitHub Copilot
3. Инсталирано разширение GitHub Copilot Chat

### Конфигурация

VS Code използва `.vscode/mcp.json` във вашето работно пространство или потребителски настройки.

**Конфигурация на работното пространство** (`.vscode/mcp.json`):

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

**Потребителски настройки** (`settings.json`):

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

### Използване на MCP в VS Code

1. Отворете панела Copilot Chat (Ctrl+Shift+I / Cmd+Shift+I)
2. Въведете `@`, за да видите наличните MCP инструменти
3. Използвайте естествен език, за да повикате инструменти: "Calculate 25 * 48 using the calculator"

### Отстраняване на проблеми с VS Code

**MCP сървърите не се зареждат:**
- Проверете панела Output → "MCP" за грешки
- Презаредете прозореца: Ctrl+Shift+P → "Developer: Reload Window"
- Потвърдете, че сървърът работи самостоятелно първо

---

## 3. Cursor

**Cursor** е редактор, ориентиран към AI, с вградена поддръжка на MCP.

### Инсталация

1. Свалете Cursor от [cursor.sh](https://cursor.sh)
2. Инсталирайте и влезте

### Конфигурация

Cursor използва подобен формат за конфигурация като Claude Desktop.

**Местоположение на конфигурационния файл:**
- **macOS**: `~/.cursor/mcp.json`
- **Windows**: `%USERPROFILE%\.cursor\mcp.json`
- **Linux**: `~/.cursor/mcp.json`

**Примерна конфигурация:**

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

### Използване на MCP в Cursor

1. Отворете AI чата на Cursor (Ctrl+L / Cmd+L)
2. MCP инструментите се показват автоматично в предложенията
3. Помолете AI да извърши задачи, използвайки свързани сървъри

---

## 4. Cline (терминален клиент)

**Cline** е терминален MCP клиент, идеален за работни процеси от командния ред.

### Инсталация

```bash
npm install -g @anthropic/cline
```

### Конфигурация

Cline използва променливи на средата и аргументи на командния ред.

**Използване на променливи на средата:**

```bash
export ANTHROPIC_API_KEY="your-api-key"
export MCP_SERVER_CALCULATOR="python -m mcp_calculator_server"
```

**Използване на аргументи на командния ред:**

```bash
cline --mcp-server "calculator:python -m mcp_calculator_server" \
      --mcp-server "weather:node /path/to/weather/index.js"
```

**Конфигурационен файл** (`~/.clinerc`):

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

### Използване на Cline

```bash
# Стартиране на интерактивна сесия
cline

# Една заявка с MCP
cline "Calculate the square root of 144 using the calculator"

# Изброяване на наличните инструменти
cline --list-tools
```

---

## 5. Windsurf

**Windsurf** е друг AI-базиран редактор на код с поддръжка на MCP.

### Инсталация

1. Свалете Windsurf от [codeium.com/windsurf](https://codeium.com/windsurf)
2. Инсталирайте и създайте акаунт

### Конфигурация

Конфигурацията на Windsurf се управлява чрез потребителския интерфейс за настройки:

1. Отворете Настройки (Ctrl+, / Cmd+,)
2. Потърсете "MCP"
3. Кликнете "Edit in settings.json"

**Примерна конфигурация:**

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

## Сравнение на транспортните типове

Различните хостове поддържат различни транспортни механизми:

| Хост | stdio | SSE/HTTP | WebSocket |
|------|-------|----------|-----------|
| Claude Desktop | ✅ | ❌ | ❌ |
| VS Code | ✅ | ✅ | ❌ |
| Cursor | ✅ | ✅ | ❌ |
| Cline | ✅ | ✅ | ❌ |
| Windsurf | ✅ | ✅ | ❌ |

**stdio** (стандартен вход/изход): Най-подходящ за локални сървъри, стартирани от хоста
**SSE/HTTP**: Най-подходящ за отдалечени сървъри или споделени между множество клиенти

---

## Общи проблеми и решения

### Сървърът няма да стартира

1. **Първо тествайте сървъра ръчно:**
   ```bash
   # За Python
   python -m your_server_module
   
   # За Node.js
   node /path/to/server/index.js
   ```

2. **Проверете пътя към командата:**
   - Използвайте абсолютни пътеки когато е възможно
   - Уверете се, че изпълнимият файл е в PATH променливата ви

3. **Проверете зависимостите:**
   ```bash
   # Питон
   pip list | grep mcp
   
   # Node.js
   npm list @modelcontextprotocol/sdk
   ```

### Сървърът се свързва, но инструментите не работят

1. **Проверете логовете на сървъра** - Повечето хостове имат опции за логване
2. **Проверете регистрацията на инструментите** - Използвайте MCP Inspector за тестване
3. **Проверете разрешенията** - Някои инструменти изискват достъп до файлове/мрежа

### Променливите на средата не се предават

- Някои хостове "почистват" променливите на средата
- Използвайте конфигурационното поле `env` явно
- Избягвайте чувствителни данни в конфигурационни файлове (използвайте управление на тайни)

---

## Най-добри практики за сигурност

1. **Никога не комитвайте API ключове** в конфигурационните файлове
2. **Използвайте променливи на средата** за чувствителни данни
3. **Ограничете разрешенията на сървъра** само до необходимото
4. **Преглеждайте кода на сървъра** преди да предоставите достъп до системата си
5. **Използвайте allowlists** за достъп до файлова система и мрежа

---

## Какво следва

- [3.13 - Дебъгване с MCP Inspector](../13-mcp-inspector/README.md)
- [3.1 - Създайте първия си MCP сървър](../01-first-server/README.md)
- [Модул 5 - Разширени теми](../../05-AdvancedTopics/README.md)

---

## Допълнителни ресурси

- [Claude Desktop MCP документация](https://docs.anthropic.com/en/docs/claude-desktop/mcp)
- [VS Code MCP разширение](https://marketplace.visualstudio.com/items?itemName=anthropic.claude-mcp)
- [MCP Спецификация - Транспорти](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/)
- [Официален MCP регистър на сървъри](https://github.com/modelcontextprotocol/servers)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Отказ от отговорност**:
Този документ е преведен с помощта на AI преводачески услуга [Co-op Translator](https://github.com/Azure/co-op-translator). Въпреки че се стремим към точност, моля имайте предвид, че автоматизираните преводи могат да съдържат грешки или неточности. Оригиналният документ на неговия роден език трябва да се счита за авторитетен източник. За критична информация се препоръчва професионален човешки превод. Ние не носим отговорност за каквито и да е недоразумения или неправилни тълкувания, произтичащи от използването на този превод.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->