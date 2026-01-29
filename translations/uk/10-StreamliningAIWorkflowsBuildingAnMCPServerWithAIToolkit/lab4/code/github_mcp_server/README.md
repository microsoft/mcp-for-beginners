# Сервер MCP Погоди

Це приклад сервера MCP на Python, який реалізує інструменти для роботи з погодою з використанням мок-відповідей. Його можна використовувати як шаблон для створення власного сервера MCP. Він включає наступні функції:

- **Інструмент Погоди**: Інструмент, який надає моковану інформацію про погоду на основі заданого місця.
- **Інструмент Клонування Git**: Інструмент, який клонує git-репозиторій у вказану папку.
- **Інструмент Відкриття у VS Code**: Інструмент, який відкриває папку у VS Code або VS Code Insiders.
- **Підключення до Agent Builder**: Функція, яка дозволяє підключити сервер MCP до Agent Builder для тестування та налагодження.
- **Налагодження у [MCP Inspector](https://github.com/modelcontextprotocol/inspector)**: Функція, яка дозволяє налагоджувати сервер MCP за допомогою MCP Inspector.

## Початок роботи з шаблоном сервера MCP Погоди

> **Передумови**
>
> Для запуску сервера MCP на вашій локальній машині для розробки вам знадобиться:
>
> - [Python](https://www.python.org/)
> - [Git](https://git-scm.com/) (Необхідний для інструменту git_clone_repo)
> - [VS Code](https://code.visualstudio.com/) або [VS Code Insiders](https://code.visualstudio.com/insiders/) (Необхідний для інструменту open_in_vscode)
> - (*Опціонально - якщо ви віддаєте перевагу uv*) [uv](https://github.com/astral-sh/uv)
> - [Розширення для налагодження Python](https://marketplace.visualstudio.com/items?itemName=ms-python.debugpy)

## Підготовка середовища

Існує два підходи для налаштування середовища для цього проєкту. Ви можете вибрати будь-який залежно від ваших уподобань.

> Примітка: Перезавантажте VS Code або термінал, щоб переконатися, що використовується Python з віртуального середовища після його створення.

| Підхід | Кроки |
| ------ | ----- |
| Використання `uv` | 1. Створіть віртуальне середовище: `uv venv` <br>2. Виконайте команду VS Code "***Python: Select Interpreter***" і виберіть Python із створеного віртуального середовища <br>3. Встановіть залежності (включаючи залежності для розробки): `uv pip install -r pyproject.toml --extra dev` |
| Використання `pip` | 1. Створіть віртуальне середовище: `python -m venv .venv` <br>2. Виконайте команду VS Code "***Python: Select Interpreter***" і виберіть Python із створеного віртуального середовища<br>3. Встановіть залежності (включаючи залежності для розробки): `pip install -e .[dev]` | 

Після налаштування середовища ви можете запустити сервер на вашій локальній машині для розробки через Agent Builder як MCP Client, щоб почати:
1. Відкрийте панель налагодження VS Code. Виберіть `Debug in Agent Builder` або натисніть `F5`, щоб почати налагодження сервера MCP.
2. Використовуйте AI Toolkit Agent Builder для тестування сервера з [цим запитом](../../../../../../../../../../../open_prompt_builder). Сервер буде автоматично підключений до Agent Builder.
3. Натисніть `Run`, щоб протестувати сервер із запитом.

**Вітаємо**! Ви успішно запустили сервер MCP Погоди на вашій локальній машині для розробки через Agent Builder як MCP Client.
![DebugMCP](https://raw.githubusercontent.com/microsoft/windows-ai-studio-templates/refs/heads/dev/mcpServers/mcp_debug.gif)

## Що включено в шаблон

| Папка / Файл | Вміст                                     |
| ------------ | ----------------------------------------- |
| `.vscode`    | Файли VSCode для налагодження            |
| `.aitk`      | Конфігурації для AI Toolkit               |
| `src`        | Вихідний код сервера MCP Погоди          |

## Як налагоджувати сервер MCP Погоди

> Примітки:
> - [MCP Inspector](https://github.com/modelcontextprotocol/inspector) — це візуальний інструмент для розробників для тестування та налагодження серверів MCP.
> - Усі режими налагодження підтримують точки зупинки, тому ви можете додавати точки зупинки до коду реалізації інструментів.

## Доступні інструменти

### Інструмент Погоди
Інструмент `get_weather` надає моковану інформацію про погоду для заданого місця.

| Параметр | Тип | Опис |
| -------- | ---- | ---- |
| `location` | рядок | Місце, для якого потрібно отримати інформацію про погоду (наприклад, назва міста, штат або координати) |

### Інструмент Клонування Git
Інструмент `git_clone_repo` клонує git-репозиторій у вказану папку.

| Параметр | Тип | Опис |
| -------- | ---- | ---- |
| `repo_url` | рядок | URL git-репозиторію для клонування |
| `target_folder` | рядок | Шлях до папки, куди має бути клонований репозиторій |

Інструмент повертає JSON-об'єкт із:
- `success`: Булеве значення, яке вказує, чи була операція успішною
- `target_folder` або `error`: Шлях до клонованого репозиторію або повідомлення про помилку

### Інструмент Відкриття у VS Code
Інструмент `open_in_vscode` відкриває папку у VS Code або VS Code Insiders.

| Параметр | Тип | Опис |
| -------- | ---- | ---- |
| `folder_path` | рядок | Шлях до папки для відкриття |
| `use_insiders` | булеве (опціонально) | Чи використовувати VS Code Insiders замість звичайного VS Code |

Інструмент повертає JSON-об'єкт із:
- `success`: Булеве значення, яке вказує, чи була операція успішною
- `message` або `error`: Підтверджувальне повідомлення або повідомлення про помилку

| Режим налагодження | Опис | Кроки для налагодження |
| ------------------ | ----- | ---------------------- |
| Agent Builder | Налагодження сервера MCP у Agent Builder через AI Toolkit. | 1. Відкрийте панель налагодження VS Code. Виберіть `Debug in Agent Builder` і натисніть `F5`, щоб почати налагодження сервера MCP.<br>2. Використовуйте AI Toolkit Agent Builder для тестування сервера з [цим запитом](../../../../../../../../../../../open_prompt_builder). Сервер буде автоматично підключений до Agent Builder.<br>3. Натисніть `Run`, щоб протестувати сервер із запитом. |
| MCP Inspector | Налагодження сервера MCP за допомогою MCP Inspector. | 1. Встановіть [Node.js](https://nodejs.org/)<br> 2. Налаштуйте Inspector: `cd inspector` && `npm install` <br> 3. Відкрийте панель налагодження VS Code. Виберіть `Debug SSE in Inspector (Edge)` або `Debug SSE in Inspector (Chrome)`. Натисніть F5, щоб почати налагодження.<br> 4. Коли MCP Inspector запуститься у браузері, натисніть кнопку `Connect`, щоб підключити цей сервер MCP.<br> 5. Потім ви можете `List Tools`, вибрати інструмент, ввести параметри та `Run Tool`, щоб налагодити код вашого сервера.<br> |

## Стандартні порти та налаштування

| Режим налагодження | Порти | Визначення | Налаштування | Примітка |
| ------------------ | ----- | ---------- | ------------ | -------- |
| Agent Builder | 3001 | [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json) | Змініть [launch.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/launch.json), [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json), [\_\_init\_\_.py](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/src/__init__.py), [mcp.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.aitk/mcp.json), щоб змінити зазначені порти. | Н/Д |
| MCP Inspector | 3001 (сервер); 5173 і 3000 (Inspector) | [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json) | Змініть [launch.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/launch.json), [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json), [\_\_init\_\_.py](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/src/__init__.py), [mcp.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.aitk/mcp.json), щоб змінити зазначені порти. | Н/Д |

## Зворотний зв'язок

Якщо у вас є будь-які відгуки або пропозиції щодо цього шаблону, відкрийте проблему в [репозиторії AI Toolkit на GitHub](https://github.com/microsoft/vscode-ai-toolkit/issues).

---

**Відмова від відповідальності**:  
Цей документ було перекладено за допомогою сервісу автоматичного перекладу [Co-op Translator](https://github.com/Azure/co-op-translator). Хоча ми прагнемо до точності, будь ласка, майте на увазі, що автоматичні переклади можуть містити помилки або неточності. Оригінальний документ на його рідній мові слід вважати авторитетним джерелом. Для критично важливої інформації рекомендується професійний людський переклад. Ми не несемо відповідальності за будь-які непорозуміння або неправильні тлумачення, що виникли внаслідок використання цього перекладу.