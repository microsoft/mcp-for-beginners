# Weather MCP Server

Ово је пример MCP сервера у Python-у који имплементира алатке за временску прогнозу са лажним одговорима. Може се користити као основа за ваш MCP сервер. Укључује следеће функције:

- **Алатка за временску прогнозу**: Алатка која пружа лажне информације о времену на основу задате локације.
- **Алатка за клонирање Git репозиторијума**: Алатка која клонира Git репозиторијум у одређени фолдер.
- **Алатка за отварање у VS Code**: Алатка која отвара фолдер у VS Code или VS Code Insiders.
- **Повезивање са Agent Builder-ом**: Функција која омогућава повезивање MCP сервера са Agent Builder-ом ради тестирања и отклањања грешака.
- **Отклањање грешака у [MCP Inspector-у](https://github.com/modelcontextprotocol/inspector)**: Функција која омогућава отклањање грешака MCP сервера помоћу MCP Inspector-а.

## Почетак рада са шаблоном Weather MCP Server-а

> **Предуслови**
>
> Да бисте покренули MCP сервер на вашем локалном развојном рачунару, потребно је:
>
> - [Python](https://www.python.org/)
> - [Git](https://git-scm.com/) (Потребно за алатку git_clone_repo)
> - [VS Code](https://code.visualstudio.com/) или [VS Code Insiders](https://code.visualstudio.com/insiders/) (Потребно за алатку open_in_vscode)
> - (*Опционо - ако више волите uv*) [uv](https://github.com/astral-sh/uv)
> - [Python Debugger Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.debugpy)

## Припрема окружења

Постоје два приступа за подешавање окружења за овај пројекат. Можете изабрати било који на основу ваших преференција.

> Напомена: Поново учитајте VS Code или терминал како бисте осигурали да се користи Python из виртуелног окружења након креирања виртуелног окружења.

| Приступ | Кораци |
| ------- | ------ |
| Коришћење `uv` | 1. Креирајте виртуелно окружење: `uv venv` <br>2. Покрените VS Code команду "***Python: Select Interpreter***" и изаберите Python из креираног виртуелног окружења <br>3. Инсталирајте зависности (укључујући зависности за развој): `uv pip install -r pyproject.toml --extra dev` |
| Коришћење `pip` | 1. Креирајте виртуелно окружење: `python -m venv .venv` <br>2. Покрените VS Code команду "***Python: Select Interpreter***" и изаберите Python из креираног виртуелног окружења<br>3. Инсталирајте зависности (укључујући зависности за развој): `pip install -e .[dev]` |

Након подешавања окружења, можете покренути сервер на вашем локалном развојном рачунару преко Agent Builder-а као MCP клијента за почетак рада:
1. Отворите VS Code панел за отклањање грешака. Изаберите `Debug in Agent Builder` или притисните `F5` да бисте започели отклањање грешака MCP сервера.
2. Користите AI Toolkit Agent Builder за тестирање сервера са [овим упитом](../../../../../../../../../../../open_prompt_builder). Сервер ће бити аутоматски повезан са Agent Builder-ом.
3. Кликните `Run` да бисте тестирали сервер са упитом.

**Честитамо**! Успешно сте покренули Weather MCP Server на вашем локалном развојном рачунару преко Agent Builder-а као MCP клијента.
![DebugMCP](https://raw.githubusercontent.com/microsoft/windows-ai-studio-templates/refs/heads/dev/mcpServers/mcp_debug.gif)

## Шта је укључено у шаблон

| Фолдер / Фајл | Садржај                                     |
| ------------- | ------------------------------------------- |
| `.vscode`     | VSCode фајлови за отклањање грешака         |
| `.aitk`       | Конфигурације за AI Toolkit                |
| `src`         | Изворни код за Weather MCP Server          |

## Како отклонити грешке у Weather MCP Server-у

> Напомене:
> - [MCP Inspector](https://github.com/modelcontextprotocol/inspector) је визуелни алат за развој који служи за тестирање и отклањање грешака MCP сервера.
> - Сви режими отклањања грешака подржавају тачке прекида, тако да можете додати тачке прекида у код имплементације алатке.

## Доступне алатке

### Алатка за временску прогнозу
Алатка `get_weather` пружа лажне информације о времену за одређену локацију.

| Параметар | Тип | Опис |
| --------- | ---- | ---- |
| `location` | string | Локација за коју се добија временска прогноза (нпр. име града, држава или координате) |

### Алатка за клонирање Git репозиторијума
Алатка `git_clone_repo` клонира Git репозиторијум у одређени фолдер.

| Параметар | Тип | Опис |
| --------- | ---- | ---- |
| `repo_url` | string | URL Git репозиторијума који се клонира |
| `target_folder` | string | Путања до фолдера у који треба да се клонира репозиторијум |

Алатка враћа JSON објекат са:
- `success`: Булова вредност која указује да ли је операција била успешна
- `target_folder` или `error`: Путања клонираног репозиторијума или порука о грешци

### Алатка за отварање у VS Code
Алатка `open_in_vscode` отвара фолдер у VS Code или VS Code Insiders апликацији.

| Параметар | Тип | Опис |
| --------- | ---- | ---- |
| `folder_path` | string | Путања до фолдера који се отвара |
| `use_insiders` | boolean (опционо) | Да ли се користи VS Code Insiders уместо обичног VS Code-а |

Алатка враћа JSON објекат са:
- `success`: Булова вредност која указује да ли је операција била успешна
- `message` или `error`: Порука потврде или порука о грешци

| Режим отклањања грешака | Опис | Кораци за отклањање грешака |
| ----------------------- | ----- | -------------------------- |
| Agent Builder | Отклањање грешака MCP сервера у Agent Builder-у преко AI Toolkit-а. | 1. Отворите VS Code панел за отклањање грешака. Изаберите `Debug in Agent Builder` и притисните `F5` да бисте започели отклањање грешака MCP сервера.<br>2. Користите AI Toolkit Agent Builder за тестирање сервера са [овим упитом](../../../../../../../../../../../open_prompt_builder). Сервер ће бити аутоматски повезан са Agent Builder-ом.<br>3. Кликните `Run` да бисте тестирали сервер са упитом. |
| MCP Inspector | Отклањање грешака MCP сервера помоћу MCP Inspector-а. | 1. Инсталирајте [Node.js](https://nodejs.org/)<br> 2. Подесите Inspector: `cd inspector` && `npm install` <br> 3. Отворите VS Code панел за отклањање грешака. Изаберите `Debug SSE in Inspector (Edge)` или `Debug SSE in Inspector (Chrome)`. Притисните F5 да бисте започели отклањање грешака.<br> 4. Када MCP Inspector буде покренут у прегледачу, кликните на дугме `Connect` да бисте повезали овај MCP сервер.<br> 5. Затим можете `List Tools`, изабрати алатку, унети параметре и `Run Tool` да бисте отклонили грешке у вашем серверском коду.<br> |

## Подразумевани портови и прилагођавања

| Режим отклањања грешака | Портови | Дефиниције | Прилагођавања | Напомена |
| ----------------------- | ------- | ---------- | ------------- | -------- |
| Agent Builder | 3001 | [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json) | Измените [launch.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/launch.json), [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json), [\_\_init\_\_.py](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/src/__init__.py), [mcp.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.aitk/mcp.json) да бисте променили горе наведене портове. | Нема |
| MCP Inspector | 3001 (Server); 5173 и 3000 (Inspector) | [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json) | Измените [launch.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/launch.json), [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json), [\_\_init\_\_.py](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/src/__init__.py), [mcp.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.aitk/mcp.json) да бисте променили горе наведене портове. | Нема |

## Повратне информације

Ако имате било какве повратне информације или предлоге за овај шаблон, отворите питање на [AI Toolkit GitHub репозиторијуму](https://github.com/microsoft/vscode-ai-toolkit/issues).

---

**Одрицање од одговорности**:  
Овај документ је преведен коришћењем услуге за превођење помоћу вештачке интелигенције [Co-op Translator](https://github.com/Azure/co-op-translator). Иако се трудимо да обезбедимо тачност, молимо вас да имате у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати ауторитативним извором. За критичне информације препоручује се професионални превод од стране људи. Не преузимамо одговорност за било каква погрешна тумачења или неспоразуме који могу настати услед коришћења овог превода.