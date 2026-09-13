# Подешавање Популарних MCP Клијената

> [!NOTE]
> Подешавања домаћина која упућују на `/sse` су застарели HTTP+SSE примери за
> MCP `2025-11-25`. За MCP `2026-07-28`, одаберите Streamable HTTP у домаћинима који
> га подржавају и користите крајњу тачку коју конфигурише сервер.

Овај водич описује како се конфигуришу и користе MCP сервери са популарним AI апликацијама домаћина. Сваки домаћин има свој приступ конфигурацији, али када је подешен, сви комуницирају са MCP серверима користећи стандардизовани протокол.

## Шта је MCP домаћин?

**MCP домаћин** је AI апликација која може да се повеже са MCP серверима да прошири своје могућности. Можете га схватити као "предњи крај" са којим корисници комуницирају, док MCP сервери пружају "задњи крај" алата и података.

```mermaid
flowchart LR
    User[👤 Корисник] --> Host[🖥️ MCP Домаћин]
    Host --> S1[MCP Сервер А]
    Host --> S2[MCP Сервер Б]
    Host --> S3[MCP Сервер Ц]
    
    subgraph "Популарни домаћини"
        H1[Claude Десктоп]
        H2[VS Code]
        H3[Cursor]
        H4[Cline]
        H5[Windsurf]
    end
```

## Предуслови

- MCP сервер на који ћете се повезати (погледајте [Модул 3.1 - Први сервер](../01-first-server/README.md))
- Апликација домаћина инсталирана на вашем систему
- Основно познавање JSON конфигурационих фајлова

---

## 1. Claude Desktop

**Claude Desktop** је званична десктоп апликација Anthropic-а која нативно подржава MCP.

### Инсталација

1. Преузмите Claude Desktop са [claude.ai/download](https://claude.ai/download)
2. Инсталирајте и пријавите се са својим Anthropic налогом

### Конфигурација

Claude Desktop користи JSON конфигурациони фајл за дефинисање MCP сервера.

**Локација конфигурационог фајла:**
- **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
- **Windows**: `%APPDATA%\Claude\claude_desktop_config.json`
- **Linux**: `~/.config/Claude/claude_desktop_config.json`

**Пример конфигурације:**

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

### Опције конфигурације

| Поље | Опис | Пример |
|-------|-------------|---------|
| `command` | Извршни програм који се покреће | `"python"`, `"node"`, `"npx"` |
| `args` | Аргументи командне линије | `["-m", "my_server"]` |
| `env` | Променљиве окружења | `{"API_KEY": "xxx"}` |
| `cwd` | Радни директоријум | `"/path/to/server"` |

### Тестирање подешавања

1. Сачувајте конфигурациони фајл
2. Потпуно рестартујте Claude Desktop (прекини и поново покрени)
3. Отворите нови разговор
4. Потражите иконицу 🔌 која означава повезане сервере
5. Покушајте да тражите од Claude-а да користи неки од ваших алата

### Решавање проблема са Claude Desktop

**Сервер се не појављује:**
- Проверите синтаксу конфигурационог фајла помоћу JSON валидатора
- Уверите се да је путања команде исправна
- Проверите логове Claude Desktop-а: Помоћ → Прикажи логове

**Сервер се руши при покретању:**
- Прво ручно тестирајте сервер у терминалу
- Проверите да ли су променљиве окружења исправно подешене
- Уверите се да су све зависности инсталиране

---

## 2. VS Code са GitHub Copilot

VS Code подржава MCP преко GitHub Copilot Chat екстензија.

### Предуслови

1. Инсталиран VS Code верзије 1.99+
2. Инсталирана GitHub Copilot екстензија
3. Инсталирана GitHub Copilot Chat екстензија

### Конфигурација

VS Code користи `.vscode/mcp.json` у радном простору или корисничким подешавањима.

**Конфигурација радног простора** (`.vscode/mcp.json`):

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

**Корисничка подешавања** (`settings.json`):

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

### Коришћење MCP у VS Code-у

1. Отворите Copilot Chat панел (Ctrl+Shift+I / Cmd+Shift+I)
2. Откуцајте `@` да видите доступне MCP алате
3. Користите природни језик за активирање алата: "Израчунај 25 * 48 користећи калкулатор"

### Решавање проблема у VS Code-у

**MCP сервери се не учитавају:**
- Проверите панел Output → "MCP" за лог грешке
- Релоадујте прозор: Ctrl+Shift+P → "Developer: Reload Window"
- Потврдите да сервер ради самостално прво

---

## 3. Cursor

**Cursor** је AI-први уређивач кода са уграђеном подршком за MCP.

### Инсталација

1. Преузмите Cursor са [cursor.sh](https://cursor.sh)
2. Инсталирајте и пријавите се

### Конфигурација

Cursor користи сличан формат конфигурације као Claude Desktop.

**Локација конфигурационог фајла:**
- **macOS**: `~/.cursor/mcp.json`
- **Windows**: `%USERPROFILE%\.cursor\mcp.json`
- **Linux**: `~/.cursor/mcp.json`

**Пример конфигурације:**

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

### Коришћење MCP у Cursor-у

1. Отворите AI чат у Cursor-у (Ctrl+L / Cmd+L)
2. MCP алати ће аутоматски бити предочени у предлозима
3. Затражите од AI да изврши задатке користећи повезане сервере

---

## 4. Cline (Терминалски)

**Cline** је терминалски MCP клиент, идеалан за рад са командном линијом.

### Инсталација

```bash
npm install -g @anthropic/cline
```

### Конфигурација

Cline користи променљиве окружења и аргументе командне линије.

**Коришћење променљивих окружења:**

```bash
export ANTHROPIC_API_KEY="your-api-key"
export MCP_SERVER_CALCULATOR="python -m mcp_calculator_server"
```

**Коришћење аргумената командне линије:**

```bash
cline --mcp-server "calculator:python -m mcp_calculator_server" \
      --mcp-server "weather:node /path/to/weather/index.js"
```

**Конфигурациони фајл** (`~/.clinerc`):

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

### Коришћење Cline-а

```bash
# Започните интерактивну сесију
cline

# Једно упитивање са MCP-ом
cline "Calculate the square root of 144 using the calculator"

# Прикажи доступне алате
cline --list-tools
```

---

## 5. Windsurf

**Windsurf** је још један AI уређивач кода са подршком за MCP.

### Инсталација

1. Преузмите Windsurf са [codeium.com/windsurf](https://codeium.com/windsurf)
2. Инсталирајте и направите налог

### Конфигурација

Конфигурација Windsurf-а се управља преко интерфејса подешавања:

1. Отворите Settings (Ctrl+, / Cmd+,)
2. Потражите "MCP"
3. Кликните "Edit in settings.json"

**Пример конфигурације:**

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

## Поређење типова транспорта

Различити домаћини подржавају различите транспортне механизме:

| Домаћин | stdio | SSE/HTTP | WebSocket |
|------|-------|----------|-----------|
| Claude Desktop | ✅ | ❌ | ❌ |
| VS Code | ✅ | ✅ | ❌ |
| Cursor | ✅ | ✅ | ❌ |
| Cline | ✅ | ✅ | ❌ |
| Windsurf | ✅ | ✅ | ❌ |

**stdio** (стандардни улаз/излаз): Најбоље за локалне сервере које покреће домаћин
**SSE/HTTP**: Најбоље за удаљене сервере или сервере које деле више клијената

---

## Уобичајени проблеми и решења

### Сервер се не покреће

1. **Прво ручно тестирајте сервер:**
   ```bash
   # За Пајтон
   python -m your_server_module
   
   # За Ноуд.јс
   node /path/to/server/index.js
   ```

2. **Проверите путању команде:**
   - Користите апсолутне путање када је могуће
   - Уверите се да је извршни програм у вашем PATH-у

3. **Проверите зависности:**
   ```bash
   # Пајтон
   pip list | grep mcp
   
   # Ноуд.јс
   npm list @modelcontextprotocol/sdk
   ```

### Сервер се повезује али алати не функционишу

1. **Проверите логове сервера** – Већина домаћина има опције за логовање
2. **Проверите регистрацију алата** – Користите MCP Inspector за тестирање
3. **Проверите дозволе** – Неким алатима је потребан приступ фајловима/мрежи

### Променљиве окружења се не преносе

- Неки домаћини чисте променљиве окружења
- Јасно користите поље `env` у конфигурацији
- Избегавајте осетљиве податке у конфигурационим фајловима (користите управљање тајнама)

---

## Најбоље безбедносне праксе

1. **Никада не комитујте API кључеве** у конфигурационе фајлове
2. **Користите променљиве окружења** за осетљиве податке
3. **Ограничите дозволе сервера** само на неопходно
4. **Прегледајте серверски код** пре него што му дате приступ систему
5. **Користите дозволе (allowlists)** за приступ фајл систему и мрежи

---

## Шта даље

- [3.13 - Отлањање грешака са MCP Inspector-ом](../13-mcp-inspector/README.md)
- [3.1 - Креирајте свој први MCP сервер](../01-first-server/README.md)
- [Модул 5 - Напредне теме](../../05-AdvancedTopics/README.md)

---

## Додатни ресурси

- [Документација за Claude Desktop MCP](https://docs.anthropic.com/en/docs/claude-desktop/mcp)
- [VS Code MCP екстензија](https://marketplace.visualstudio.com/items?itemName=anthropic.claude-mcp)
- [MCP спецификација - Транспорт](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/)
- [Званични MCP регистар сервера](https://github.com/modelcontextprotocol/servers)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Изјава о одрицању одговорности**:
Овај документ је преведен коришћењем услуге за аутоматски превод [Co-op Translator](https://github.com/Azure/co-op-translator). Иако тежимо тачности, имајте у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати ауторитативним извором. За критичне информације препоручује се професионални људски превод. Нисмо одговорни за било каква неспоразума или погрешна тумачења која произилазе из коришћења овог превода.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->