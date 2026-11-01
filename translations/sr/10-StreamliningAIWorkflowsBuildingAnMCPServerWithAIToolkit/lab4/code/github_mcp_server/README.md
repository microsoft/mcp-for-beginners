# Weather MCP Server

Ово је пример MCP сервера у Питону који реализује алате за временске прилике са симулираним одговорима. Може се користити као основа за ваш сопствени MCP сервер. Укључује следеће функције: 

- **Weather Tool**: Алат који пружа симулиране информације о времену на основу дате локације.
- **Git Clone Tool**: Алат који клонира гит репозиторијум у одређену фасциклу.
- **VS Code Open Tool**: Алат који отвара фасциклу у VS Code или VS Code Insiders.
- **Connect to Agent Builder**: Функција која вам омогућава да повежете MCP сервер са Agent Builder-ом за тестирање и отклањање грешака.
- **Debug in [MCP Inspector](https://github.com/modelcontextprotocol/inspector)**: Функција која вам омогућава да дебагујете MCP сервер користећи MCP Inspector.

## Започните са Weather MCP Server шаблоном

> **Пре захтева**
>
> Да бисте покренули MCP сервер на вашем локалном развојном рачунару, потребно вам је:
>
> - [Python](https://www.python.org/)
> - [Git](https://git-scm.com/) (Потребно за git_clone_repo алат)
> - [VS Code](https://code.visualstudio.com/) или [VS Code Insiders](https://code.visualstudio.com/insiders/) (Потребно за open_in_vscode алат)
> - (*Опционално - ако више волите uv*) [uv](https://github.com/astral-sh/uv)
> - [Python Debugger Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.debugpy)

## Припрема окружења

Постоје два приступа за подешавање окружења за овај пројекат. Можете одабрати један у зависности од ваших преференција.

> Напомена: Поново учитајте VSCode или терминал да бисте осигурали да се користи python из виртуелног окружења након његовог креирања.

| Приступ | Кораци |
| -------- | ----- |
| Коришћење `uv` | 1. Креирајте виртуелно окружење: `uv venv` <br>2. Покрените VSCode команду "***Python: Select Interpreter***" и изаберите python из креираног виртуелног окружења <br>3. Инсталирајте зависности (укључујући и дев зависности): `uv pip install -r pyproject.toml --extra dev` |
| Коришћење `pip` | 1. Креирајте виртуелно окружење: `python -m venv .venv` <br>2. Покрените VSCode команду "***Python: Select Interpreter***" и изаберите python из креираног виртуелног окружења<br>3. Инсталирајте зависности (укључујући и дев зависности): `pip install -e .[dev]` | 

Након подешавања окружења, можете покренути сервер на вашем локалном развојном рачунару преко Agent Builder-а као MCP клијента да бисте започели:
1. Отворите VS Code Debug панел. Изаберите `Debug in Agent Builder` или притисните `F5` да започнете дебаговање MCP сервера.
2. У Microsoft Foundry Toolkit за Visual Studio Code Agent Builder, изаберите активну Foundry дистрибуцију као што је `gpt-5.1`, затим унесите: `What is the weather in Shanghai?` Сервер ће аутоматски бити повезан.
3. Кликните `Run` да бисте тестирали сервер са упитом.

**Честитамо**! Успешно сте покренули Weather MCP Server на вашем локалном развојном рачунару преко Agent Builder-а као MCP клијента.
![DebugMCP](https://raw.githubusercontent.com/microsoft/windows-ai-studio-templates/refs/heads/dev/mcpServers/mcp_debug.gif)

## Шта је укључено у шаблон

| Фасцикла / Фајл | Садржај                                     |
| -------------- | ---------------------------------------- |
| `.vscode`    | VSCode фајлови за дебаговање                |
| `.aitk`      | Конфигурација Microsoft Foundry Toolkit-а  |
| `src`        | Изворни код за weather mcp сервер            |

## Како дебаговати Weather MCP Server

> Напомене:
> - [MCP Inspector](https://github.com/modelcontextprotocol/inspector) је визуелни алат за програмере за тестирање и дебаговање MCP сервера.
> - Сви режими дебаговања подржавају тачке прекида, тако да можете додати тачке прекида у код имплементације алата.

## Доступни алати

### Weather Tool
`get_weather` алат пружа симулиране информације о времену за одређену локацију.

| Параметар | Тип | Опис |
| -------- | --- | ----- |
| `location` | string | Локација за добијање података о времену (нпр. име града, држава, или координате) |

### Git Clone Tool
`git_clone_repo` алат клонира гит репозиторијум у одређену фасциклу.

| Параметар | Тип | Опис |
| -------- | --- | ----- |
| `repo_url` | string | URL гит репозиторијума који треба клонирати |
| `target_folder` | string | Путања до фасцикле у коју треба клонирати репозиторијум |

Алат враћа JSON објекат са:
- `success`: Булова вредност која показује да ли је операција била успешна
- `target_folder` или `error`: Путања клонираног репозиторијума или порука о грешци

### VS Code Open Tool
`open_in_vscode` алат отвара фасциклу у VS Code или VS Code Insiders апликацији.

| Параметар | Тип | Опис |
| -------- | --- | ----- |
| `folder_path` | string | Путања до фасцикле коју треба отворити |
| `use_insiders` | boolean (опционо) | Да ли користити VS Code Insiders уместо редовног VS Code-а |

Алат враћа JSON објекат са:
- `success`: Булова вредност која показује да ли је операција била успешна
- `message` или `error`: Порука о потврди или порука о грешци

| Режим дебаговања | Опис | Кораци за дебаговање |
| ---------------- | ----- | ------------------- |
| Agent Builder | Дебаговајте MCP сервер у Agent Builder-у преко Microsoft Foundry Toolkit-а за Visual Studio Code. | 1. Отворите VS Code Debug панел. Изаберите `Debug in Agent Builder` и притисните `F5` да започнете дебаговање MCP сервера.<br>2. Изаберите активну Foundry дистрибуцију као што је `gpt-5.1`, затим унесите `What is the weather in Shanghai?`. Сервер ће аутоматски бити повезан.<br>3. Кликните `Run` да тестирате сервер са упитом. |
| MCP Inspector | Дебаговање MCP сервера користећи MCP Inspector. | 1. Инсталирајте [Node.js](https://nodejs.org/)<br> 2. Подесите Inspector: `cd inspector` && `npm install` <br> 3. Отворите VS Code Debug панел. Изаберите `Debug SSE in Inspector (Edge)` или `Debug SSE in Inspector (Chrome)`. Притисните F5 да започнете дебаговање.<br> 4. Када се MCP Inspector покрене у прегледачу, кликните на дугме `Connect` да повежете овај MCP сервер.<br> 5. Затим можете `List Tools`, изаберите алат, унесите параметре и `Run Tool` да дебагујете свој серверски код.<br> |

## Подразумевани портови и прилагођавања

| Режим дебаговања | Портови | Дефиниције | Прилагођавања | Напомена |
| --------------- | ------- | ----------- | ------------- | -------- |
| Agent Builder | 3001 | [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json) | Измените [launch.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/launch.json), [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json), [\_\_init\_\_.py](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/src/__init__.py), [mcp.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.aitk/mcp.json) да промените горе наведене портове. | Нема |
| MCP Inspector | 3001 (Сервер); 5173 и 3000 (Inspector) | [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json) | Измените [launch.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/launch.json), [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json), [\_\_init\_\_.py](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/src/__init__.py), [mcp.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.aitk/mcp.json) да промените горе наведене портове.| Нема |

## Повратне информације

Ако имате било какве повратне информације или предлоге за овај шаблон, молимо вас отворите issue на [Microsoft Foundry Toolkit for Visual Studio Code GitHub репозиторијуму](https://github.com/microsoft/vscode-ai-toolkit/issues)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Изјава о одрицању одговорности**:
Овај документ је преведен коришћењем услуге за аутоматски превод [Co-op Translator](https://github.com/Azure/co-op-translator). Иако тежимо тачности, имајте у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати ауторитативним извором. За критичне информације препоручује се професионални људски превод. Нисмо одговорни за било каква неспоразума или погрешна тумачења која произилазе из коришћења овог превода.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->