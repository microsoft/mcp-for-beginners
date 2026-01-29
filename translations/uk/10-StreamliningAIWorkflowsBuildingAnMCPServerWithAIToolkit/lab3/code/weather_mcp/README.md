# Weather MCP Server

Це приклад MCP Server на Python, який реалізує інструменти для погоди з імітованими відповідями. Його можна використовувати як основу для власного MCP Server. Він включає такі функції:

- **Weather Tool**: інструмент, який надає змодельовану інформацію про погоду на основі заданого місця.
- **Підключення до Agent Builder**: функція, що дозволяє підключити MCP сервер до Agent Builder для тестування та налагодження.
- **Налагодження в [MCP Inspector](https://github.com/modelcontextprotocol/inspector)**: можливість налагоджувати MCP Server за допомогою MCP Inspector.

## Початок роботи з шаблоном Weather MCP Server

> **Вимоги**
>
> Для запуску MCP Server на вашій локальній машині для розробки вам знадобиться:
>
> - [Python](https://www.python.org/)
> - (*Опційно - якщо ви віддаєте перевагу uv*) [uv](https://github.com/astral-sh/uv)
> - [Розширення для налагодження Python](https://marketplace.visualstudio.com/items?itemName=ms-python.debugpy)

## Підготовка середовища

Існує два способи налаштування середовища для цього проєкту. Ви можете обрати будь-який з них залежно від ваших уподобань.

> Примітка: Перезавантажте VSCode або термінал, щоб переконатися, що використовується python з віртуального середовища після його створення.

| Підхід | Кроки |
| -------- | ----- |
| Використання `uv` | 1. Створіть віртуальне середовище: `uv venv` <br>2. Виконайте команду VSCode "***Python: Select Interpreter***" і оберіть python зі створеного віртуального середовища <br>3. Встановіть залежності (включно з dev-залежностями): `uv pip install -r pyproject.toml --extra dev` |
| Використання `pip` | 1. Створіть віртуальне середовище: `python -m venv .venv` <br>2. Виконайте команду VSCode "***Python: Select Interpreter***" і оберіть python зі створеного віртуального середовища<br>3. Встановіть залежності (включно з dev-залежностями): `pip install -e .[dev]` |

Після налаштування середовища ви можете запустити сервер на вашій локальній машині для розробки через Agent Builder як MCP Client, щоб почати роботу:
1. Відкрийте панель налагодження VS Code. Виберіть `Debug in Agent Builder` або натисніть `F5`, щоб почати налагодження MCP сервера.
2. Використайте AI Toolkit Agent Builder для тестування сервера з [цього запиту](../../../../../../../../../../open_prompt_builder). Сервер буде автоматично підключений до Agent Builder.
3. Натисніть `Run`, щоб протестувати сервер із запитом.

**Вітаємо**! Ви успішно запустили Weather MCP Server на вашій локальній машині для розробки через Agent Builder як MCP Client.
![DebugMCP](https://raw.githubusercontent.com/microsoft/windows-ai-studio-templates/refs/heads/dev/mcpServers/mcp_debug.gif)

## Що входить до шаблону

| Папка / Файл | Зміст                                      |
| ------------ | ------------------------------------------ |
| `.vscode`    | Файли VSCode для налагодження              |
| `.aitk`      | Конфігурації для AI Toolkit                 |
| `src`        | Вихідний код MCP сервера для погоди         |

## Як налагоджувати Weather MCP Server

> Примітки:
> - [MCP Inspector](https://github.com/modelcontextprotocol/inspector) — це візуальний інструмент для розробників для тестування та налагодження MCP серверів.
> - Усі режими налагодження підтримують точки зупину, тож ви можете додавати їх у код реалізації інструменту.

| Режим налагодження | Опис | Кроки для налагодження |
| ------------------ | ----- | ---------------------- |
| Agent Builder | Налагодження MCP сервера в Agent Builder через AI Toolkit. | 1. Відкрийте панель налагодження VS Code. Виберіть `Debug in Agent Builder` і натисніть `F5`, щоб почати налагодження MCP сервера.<br>2. Використайте AI Toolkit Agent Builder для тестування сервера з [цього запиту](../../../../../../../../../../open_prompt_builder). Сервер буде автоматично підключений до Agent Builder.<br>3. Натисніть `Run`, щоб протестувати сервер із запитом. |
| MCP Inspector | Налагодження MCP сервера за допомогою MCP Inspector. | 1. Встановіть [Node.js](https://nodejs.org/)<br> 2. Налаштуйте Inspector: `cd inspector` && `npm install` <br> 3. Відкрийте панель налагодження VS Code. Виберіть `Debug SSE in Inspector (Edge)` або `Debug SSE in Inspector (Chrome)`. Натисніть F5, щоб почати налагодження.<br> 4. Коли MCP Inspector відкриється в браузері, натисніть кнопку `Connect`, щоб підключити цей MCP сервер.<br> 5. Потім ви можете `List Tools`, обрати інструмент, ввести параметри та `Run Tool` для налагодження коду сервера.<br> |

## Порти за замовчуванням та налаштування

| Режим налагодження | Порти | Визначення | Налаштування | Примітка |
| ------------------ | ----- | ----------- | ------------ | -------- |
| Agent Builder | 3001 | [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/tasks.json) | Змініть [launch.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/launch.json), [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/tasks.json), [\_\_init\_\_.py](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/src/__init__.py), [mcp.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.aitk/mcp.json), щоб змінити вказані порти. | Немає |
| MCP Inspector | 3001 (сервер); 5173 та 3000 (Inspector) | [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/tasks.json) | Змініть [launch.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/launch.json), [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/tasks.json), [\_\_init\_\_.py](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/src/__init__.py), [mcp.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.aitk/mcp.json), щоб змінити вказані порти. | Немає |

## Зворотній зв’язок

Якщо у вас є відгуки або пропозиції щодо цього шаблону, будь ласка, відкрийте issue у [репозиторії AI Toolkit на GitHub](https://github.com/microsoft/vscode-ai-toolkit/issues)

**Відмова від відповідальності**:  
Цей документ було перекладено за допомогою сервісу автоматичного перекладу [Co-op Translator](https://github.com/Azure/co-op-translator). Хоча ми прагнемо до точності, будь ласка, майте на увазі, що автоматичні переклади можуть містити помилки або неточності. Оригінальний документ рідною мовою слід вважати авторитетним джерелом. Для критично важливої інформації рекомендується звертатися до професійного людського перекладу. Ми не несемо відповідальності за будь-які непорозуміння або неправильні тлумачення, що виникли внаслідок використання цього перекладу.