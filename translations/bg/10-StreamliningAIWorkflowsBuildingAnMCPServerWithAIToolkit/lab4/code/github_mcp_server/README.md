# Weather MCP Server

Това е примерен MCP сървър на Python, който реализира инструменти за времето с фиктивни отговори. Може да се използва като основа за ваш собствен MCP сървър. Включва следните функции:

- **Инструмент за времето**: Инструмент, който предоставя фиктивна информация за времето въз основа на дадено местоположение.
- **Инструмент за клониране на Git**: Инструмент, който клонира Git хранилище в посочена папка.
- **Инструмент за отваряне във VS Code**: Инструмент, който отваря папка във VS Code или VS Code Insiders.
- **Свързване с Agent Builder**: Функция, която позволява свързване на MCP сървъра с Agent Builder за тестване и дебъгване.
- **Дебъгване в [MCP Inspector](https://github.com/modelcontextprotocol/inspector)**: Функция, която позволява дебъгване на MCP сървъра чрез MCP Inspector.

## Започнете с шаблона Weather MCP Server

> **Предварителни изисквания**
>
> За да стартирате MCP сървъра на вашата локална машина за разработка, ще ви трябва:
>
> - [Python](https://www.python.org/)
> - [Git](https://git-scm.com/) (Необходимо за инструмента git_clone_repo)
> - [VS Code](https://code.visualstudio.com/) или [VS Code Insiders](https://code.visualstudio.com/insiders/) (Необходимо за инструмента open_in_vscode)
> - (*Опционално - ако предпочитате uv*) [uv](https://github.com/astral-sh/uv)
> - [Python Debugger Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.debugpy)

## Подготовка на средата

Има два подхода за настройка на средата за този проект. Можете да изберете който и да е от тях според вашите предпочитания.

> Забележка: Презаредете VSCode или терминала, за да се уверите, че се използва Python от виртуалната среда след създаването ѝ.

| Подход | Стъпки |
| ------ | ------ |
| С използване на `uv` | 1. Създайте виртуална среда: `uv venv` <br>2. Изпълнете командата в VSCode "***Python: Select Interpreter***" и изберете Python от създадената виртуална среда <br>3. Инсталирайте зависимости (включително зависимости за разработка): `uv pip install -r pyproject.toml --extra dev` |
| С използване на `pip` | 1. Създайте виртуална среда: `python -m venv .venv` <br>2. Изпълнете командата в VSCode "***Python: Select Interpreter***" и изберете Python от създадената виртуална среда<br>3. Инсталирайте зависимости (включително зависимости за разработка): `pip install -e .[dev]` | 

След като настроите средата, можете да стартирате сървъра на вашата локална машина за разработка чрез Agent Builder като MCP клиент, за да започнете:
1. Отворете панела за дебъгване във VS Code. Изберете `Debug in Agent Builder` или натиснете `F5`, за да стартирате дебъгването на MCP сървъра.
2. Използвайте AI Toolkit Agent Builder, за да тествате сървъра с [този prompt](../../../../../../../../../../../open_prompt_builder). Сървърът ще бъде автоматично свързан с Agent Builder.
3. Натиснете `Run`, за да тествате сървъра с prompt-а.

**Поздравления**! Успешно стартирахте Weather MCP Server на вашата локална машина за разработка чрез Agent Builder като MCP клиент.
![DebugMCP](https://raw.githubusercontent.com/microsoft/windows-ai-studio-templates/refs/heads/dev/mcpServers/mcp_debug.gif)

## Какво е включено в шаблона

| Папка / Файл | Съдържание                                   |
| ------------ | -------------------------------------------- |
| `.vscode`    | Файлове за дебъгване във VSCode              |
| `.aitk`      | Конфигурации за AI Toolkit                   |
| `src`        | Изходният код за Weather MCP Server          |

## Как да дебъгнете Weather MCP Server

> Забележки:
> - [MCP Inspector](https://github.com/modelcontextprotocol/inspector) е визуален инструмент за разработчици за тестване и дебъгване на MCP сървъри.
> - Всички режими на дебъгване поддържат точки на прекъсване, така че можете да добавяте точки на прекъсване към кода за реализация на инструмента.

## Налични инструменти

### Инструмент за времето
Инструментът `get_weather` предоставя фиктивна информация за времето за посочено местоположение.

| Параметър | Тип | Описание |
| --------- | ---- | ----------- |
| `location` | string | Местоположение, за което да се предостави информация за времето (например име на град, щат или координати) |

### Инструмент за клониране на Git
Инструментът `git_clone_repo` клонира Git хранилище в посочена папка.

| Параметър | Тип | Описание |
| --------- | ---- | ----------- |
| `repo_url` | string | URL на Git хранилището, което да се клонира |
| `target_folder` | string | Път до папката, където хранилището трябва да бъде клонирано |

Инструментът връща JSON обект със:
- `success`: Булева стойност, указваща дали операцията е успешна
- `target_folder` или `error`: Пътят на клонираното хранилище или съобщение за грешка

### Инструмент за отваряне във VS Code
Инструментът `open_in_vscode` отваря папка във VS Code или VS Code Insiders.

| Параметър | Тип | Описание |
| --------- | ---- | ----------- |
| `folder_path` | string | Път до папката, която да се отвори |
| `use_insiders` | boolean (опционално) | Дали да се използва VS Code Insiders вместо обикновения VS Code |

Инструментът връща JSON обект със:
- `success`: Булева стойност, указваща дали операцията е успешна
- `message` или `error`: Потвърдително съобщение или съобщение за грешка

| Режим на дебъгване | Описание | Стъпки за дебъгване |
| ------------------ | ----------- | ------------------- |
| Agent Builder | Дебъгване на MCP сървъра в Agent Builder чрез AI Toolkit. | 1. Отворете панела за дебъгване във VS Code. Изберете `Debug in Agent Builder` и натиснете `F5`, за да стартирате дебъгването на MCP сървъра.<br>2. Използвайте AI Toolkit Agent Builder, за да тествате сървъра с [този prompt](../../../../../../../../../../../open_prompt_builder). Сървърът ще бъде автоматично свързан с Agent Builder.<br>3. Натиснете `Run`, за да тествате сървъра с prompt-а. |
| MCP Inspector | Дебъгване на MCP сървъра чрез MCP Inspector. | 1. Инсталирайте [Node.js](https://nodejs.org/)<br> 2. Настройте Inspector: `cd inspector` && `npm install` <br> 3. Отворете панела за дебъгване във VS Code. Изберете `Debug SSE in Inspector (Edge)` или `Debug SSE in Inspector (Chrome)`. Натиснете F5, за да стартирате дебъгването.<br> 4. Когато MCP Inspector се стартира в браузъра, натиснете бутона `Connect`, за да свържете този MCP сървър.<br> 5. След това можете да `List Tools`, да изберете инструмент, да въведете параметри и да `Run Tool`, за да дебъгнете кода на сървъра.<br> |

## Портове по подразбиране и персонализации

| Режим на дебъгване | Портове | Дефиниции | Персонализации | Забележка |
| ------------------ | ------- | ---------- | -------------- | --------- |
| Agent Builder | 3001 | [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json) | Редактирайте [launch.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/launch.json), [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json), [\_\_init\_\_.py](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/src/__init__.py), [mcp.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.aitk/mcp.json), за да промените горните портове. | N/A |
| MCP Inspector | 3001 (Сървър); 5173 и 3000 (Inspector) | [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json) | Редактирайте [launch.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/launch.json), [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json), [\_\_init\_\_.py](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/src/__init__.py), [mcp.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.aitk/mcp.json), за да промените горните портове.| N/A |

## Обратна връзка

Ако имате обратна връзка или предложения за този шаблон, моля, отворете проблем в [AI Toolkit GitHub хранилището](https://github.com/microsoft/vscode-ai-toolkit/issues).

---

**Отказ от отговорност**:  
Този документ е преведен с помощта на AI услуга за превод [Co-op Translator](https://github.com/Azure/co-op-translator). Въпреки че се стремим към точност, моля, имайте предвид, че автоматизираните преводи може да съдържат грешки или неточности. Оригиналният документ на неговия роден език трябва да се счита за авторитетен източник. За критична информация се препоръчва професионален човешки превод. Ние не носим отговорност за каквито и да е недоразумения или погрешни интерпретации, произтичащи от използването на този превод.