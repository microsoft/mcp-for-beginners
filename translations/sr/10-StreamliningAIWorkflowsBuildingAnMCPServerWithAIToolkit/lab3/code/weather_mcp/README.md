# Weather MCP Server

Ово је пример MCP сервера у Python-у који имплементира алате за временску прогнозу са лажним одговорима. Може се користити као основа за ваш сопствени MCP сервер. Укључује следеће функције:

- **Weather Tool**: Алат који пружа лажне информације о времену на основу дате локације.
- **Connect to Agent Builder**: Функција која вам омогућава да повежете MCP сервер са Agent Builder-ом ради тестирања и отклањања грешака.
- **Debug in [MCP Inspector](https://github.com/modelcontextprotocol/inspector)**: Функција која вам омогућава да отклањате грешке на MCP серверу користећи MCP Inspector.

## Почетак рада са Weather MCP Server шаблоном

> **Претпоставке**
>
> Да бисте покренули MCP сервер на свом локалном развојном рачунару, потребно вам је:
>
> - [Python](https://www.python.org/)
> - (*Опционо - ако више волите uv*) [uv](https://github.com/astral-sh/uv)
> - [Python Debugger Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.debugpy)

## Припрема окружења

Постоје два начина за подешавање окружења за овај пројекат. Можете изабрати онај који вам више одговара.

> Напомена: Поново учитајте VSCode или терминал да бисте били сигурни да се користи Python из виртуелног окружења након његовог креирања.

| Приступ | Кораци |
| -------- | ----- |
| Коришћење `uv` | 1. Креирајте виртуелно окружење: `uv venv` <br>2. Покрените VSCode команду "***Python: Select Interpreter***" и изаберите Python из креираног виртуелног окружења <br>3. Инсталирајте зависности (укључујући развојне): `uv pip install -r pyproject.toml --extra dev` |
| Коришћење `pip` | 1. Креирајте виртуелно окружење: `python -m venv .venv` <br>2. Покрените VSCode команду "***Python: Select Interpreter***" и изаберите Python из креираног виртуелног окружења<br>3. Инсталирајте зависности (укључујући развојне): `pip install -e .[dev]` |

Након подешавања окружења, можете покренути сервер на свом локалном развојном рачунару преко Agent Builder-а као MCP клијента да бисте почели:
1. Отворите Debug панел у VS Code-у. Изаберите `Debug in Agent Builder` или притисните `F5` да бисте започели отклањање грешака на MCP серверу.
2. Користите AI Toolkit Agent Builder да тестирате сервер са [овим упитом](../../../../../../../../../../open_prompt_builder). Сервер ће аутоматски бити повезан са Agent Builder-ом.
3. Кликните `Run` да тестирате сервер са упитом.

**Честитамо**! Успешно сте покренули Weather MCP Server на свом локалном развојном рачунару преко Agent Builder-а као MCP клијента.
![DebugMCP](https://raw.githubusercontent.com/microsoft/windows-ai-studio-templates/refs/heads/dev/mcpServers/mcp_debug.gif)

## Шта је укључено у шаблон

| Фолдер / Фајл | Садржај                                     |
| ------------- | ------------------------------------------ |
| `.vscode`     | VSCode фајлови за отклањање грешака        |
| `.aitk`       | Конфигурације за AI Toolkit                 |
| `src`         | Изворни код за weather mcp сервер          |

## Како отклањати грешке на Weather MCP Server-у

> Напомене:
> - [MCP Inspector](https://github.com/modelcontextprotocol/inspector) је визуелни алат за развојне програмере за тестирање и отклањање грешака на MCP серверима.
> - Сви режими отклањања грешака подржавају тачке прекида, тако да можете додавати тачке прекида у код имплементације алата.

| Режим отклањања грешака | Опис | Кораци за отклањање грешака |
| ----------------------- | ----- | --------------------------- |
| Agent Builder | Отклањање грешака на MCP серверу у Agent Builder-у преко AI Toolkit-а. | 1. Отворите Debug панел у VS Code-у. Изаберите `Debug in Agent Builder` и притисните `F5` да започнете отклањање грешака на MCP серверу.<br>2. Користите AI Toolkit Agent Builder да тестирате сервер са [овим упитом](../../../../../../../../../../open_prompt_builder). Сервер ће аутоматски бити повезан са Agent Builder-ом.<br>3. Кликните `Run` да тестирате сервер са упитом. |
| MCP Inspector | Отклањање грешака на MCP серверу користећи MCP Inspector. | 1. Инсталирајте [Node.js](https://nodejs.org/)<br> 2. Подесите Inspector: `cd inspector` && `npm install` <br> 3. Отворите Debug панел у VS Code-у. Изаберите `Debug SSE in Inspector (Edge)` или `Debug SSE in Inspector (Chrome)`. Притисните F5 да започнете отклањање грешака.<br> 4. Када се MCP Inspector покрене у прегледачу, кликните на дугме `Connect` да бисте повезали овај MCP сервер.<br> 5. Затим можете `List Tools`, изабрати алат, унети параметре и `Run Tool` да бисте отклонили грешке у коду сервера.<br> |

## Подразумевани портови и прилагођавања

| Режим отклањања грешака | Портови | Дефиниције | Прилагођавања | Напомена |
| ----------------------- | ------- | ---------- | ------------- | -------- |
| Agent Builder | 3001 | [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/tasks.json) | Измените [launch.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/launch.json), [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/tasks.json), [\_\_init\_\_.py](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/src/__init__.py), [mcp.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.aitk/mcp.json) да бисте променили наведене портове. | Нема |
| MCP Inspector | 3001 (сервер); 5173 и 3000 (Inspector) | [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/tasks.json) | Измените [launch.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/launch.json), [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/tasks.json), [\_\_init\_\_.py](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/src/__init__.py), [mcp.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.aitk/mcp.json) да бисте променили наведене портове. | Нема |

## Повратне информације

Ако имате било какве повратне информације или предлоге за овај шаблон, молимо вас да отворите issue на [AI Toolkit GitHub репозиторијуму](https://github.com/microsoft/vscode-ai-toolkit/issues)

**Одрицање од одговорности**:  
Овај документ је преведен коришћењем AI услуге за превођење [Co-op Translator](https://github.com/Azure/co-op-translator). Иако се трудимо да превод буде тачан, молимо вас да имате у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати ауторитетним извором. За критичне информације препоручује се професионални људски превод. Нисмо одговорни за било каква неспоразума или погрешна тумачења која произилазе из коришћења овог превода.