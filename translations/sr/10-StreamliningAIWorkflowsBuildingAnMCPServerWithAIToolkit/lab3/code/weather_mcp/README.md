# Временски MCP сервер

Ово је пример MCP сервера у Питону који имплементира временске алате са симулираним одговорима. Може се користити као основа за ваш сопствени MCP сервер. Укључује следеће функције:

- **Временски алат**: Алат који пружа симулиране временске информације на основу дате локације.
- **Повежи се са Agent Builder-ом**: Функција која вам омогућава да повеже MCP сервер са Agent Builder-ом ради тестирања и отклањања грешака.
- **Откријте грешке у [MCP Inspector](https://github.com/modelcontextprotocol/inspector)**: Функција која вам омогућава да отклањате грешке на MCP серверу користећи MCP Inspector.

## Започните са шаблоном Weather MCP Server-а

> **Претпоставке**
>
> Да бисте покренули MCP сервер на свом локалном развојном рачунару, потребно вам је:
>
> - [Python](https://www.python.org/)
> - (*Опционо - ако више волите uv*) [uv](https://github.com/astral-sh/uv)
> - [Python Debugger Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.debugpy)

## Припремите окружење

Постоје два начина за постављање окружења за овај пројекат. Можете изабрати било који од њих према вашем избору.

> Напомена: Поново покрените VSCode или терминал да бисте осигурали да се користи Python из виртуелног окружења након његовог креирања.

| Приступ | Кораци |
| -------- | ----- |
| Користећи `uv` | 1. Направите виртуелно окружење: `uv venv` <br>2. Покрените VSCode команду "***Python: Select Interpreter***" и изаберите Python из креираног виртуелног окружења <br>3. Инсталирајте зависности (укључујући и за развој): `uv pip install -r pyproject.toml --extra dev` |
| Користећи `pip` | 1. Направите виртуелно окружење: `python -m venv .venv` <br>2. Покрените VSCode команду "***Python: Select Interpreter***" и изаберите Python из креираног виртуелног окружења<br>3. Инсталирајте зависности (укључујући и за развој): `pip install -e .[dev]` |

Након постављања окружења, можете покренути сервер на свом локалном развојном рачунару преко Agent Builder-а као MCP клијент да бисте почели:
1. Отворите Debug панел у VS Code-у. Изаберите `Debug in Agent Builder` или притисните `F5` да бисте покренули отклањање грешака MCP сервера.
2. У Microsoft Foundry Toolkit Agent Builder-у изаберите активну Foundry имплементацију као што је `gpt-5.1`, затим унесите: `What is the weather in Shanghai?` Сервер ће бити аутоматски повезан.
3. Кликните `Run` да тестирате сервер помоћу упита.

**Честитамо**! Успешно сте покренули Weather MCP Server на свом локалном развојном рачунару преко Agent Builder-а као MCP клијент.
![DebugMCP](https://raw.githubusercontent.com/microsoft/windows-ai-studio-templates/refs/heads/dev/mcpServers/mcp_debug.gif)

## Шта је укључено у шаблон

| Фасцикла / Датотека | Садржај                                    |
| ------------- | ----------------------------------------- |
| `.vscode`    | VSCode датотеке за отклањање грешака         |
| `.aitk`      | Конфигурације за Microsoft Foundry Toolkit         |
| `src`        | Изворни код временског MCP сервера          |

## Како отклањати грешке на Weather MCP Server-у

> Напомене:
> - [MCP Inspector](https://github.com/modelcontextprotocol/inspector) је визуелни алат за развијаче за тестирање и отклањање грешака на MCP серверима.
> - Сви режими отклањања грешака подржавају преломе кода (breakpoints), тако да можете додати преломе у код имплементације алата.

| Режим отклањања | Опис | Кораци за отклањање грешака |
| -------------- | ----- | --------------------------- |
| Agent Builder | Отклањање грешака MCP сервера у Agent Builder-у преко Microsoft Foundry Toolkit-а. | 1. Отворите дебаг панел у VS Code-у. Изаберите `Debug in Agent Builder` и притисните `F5` да почнете са отклањањем грешака MCP сервера.<br>2. Изаберите активну Foundry имплементацију као што је `gpt-5.1`, затим унесите `What is the weather in Shanghai?`. Сервер ће бити аутоматски повезан.<br>3. Кликните `Run` да тестирате сервер помоћу упита. |
| MCP Inspector | Отклањање грешака MCP сервера коришћењем MCP Inspectora. | 1. Инсталирајте [Node.js](https://nodejs.org/)<br> 2. Подесите Inspector: `cd inspector` && `npm install` <br> 3. Отворите дебаг панел у VS Code-у. Изаберите `Debug SSE in Inspector (Edge)` или `Debug SSE in Inspector (Chrome)`. Притисните F5 да бисте започели отклањање грешака.<br> 4. Када се MCP Inspector покрене у прегледачу, кликните дугме `Connect` да повежете овај MCP сервер.<br> 5. Затим можете `List Tools`, изабрати алат, унети параметре и `Run Tool` да отклоните грешке у коду сервера.<br> |

## Подразумевани портови и прилагођавања

| Режим отклањања | Портови | Описи | Прилагођавања | Напомена |
| -------------- | ------- | ------- | ------------- | -------- |
| Agent Builder | 3001 | [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/tasks.json) | Уредите [launch.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/launch.json), [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/tasks.json), [\_\_init\_\_.py](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/src/__init__.py), [mcp.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.aitk/mcp.json) да бисте променили горе наведене портове. | Нема |
| MCP Inspector | 3001 (сервер); 5173 и 3000 (инспектор) | [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/tasks.json) | Уредите [launch.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/launch.json), [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/tasks.json), [\_\_init\_\_.py](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/src/__init__.py), [mcp.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.aitk/mcp.json) да бисте променили горе наведене портове. | Нема |

## Повратне информације

Ако имате било какве повратне информације или предлоге за овај шаблон, молимо вас да отворите issue на [Microsoft Foundry Toolkit GitHub репозиторијуму](https://github.com/microsoft/vscode-ai-toolkit/issues)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Изјава о одрицању одговорности**:
Овај документ је преведен коришћењем услуге за аутоматски превод [Co-op Translator](https://github.com/Azure/co-op-translator). Иако тежимо тачности, имајте у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати ауторитативним извором. За критичне информације препоручује се професионални људски превод. Нисмо одговорни за било каква неспоразума или погрешна тумачења која произилазе из коришћења овог превода.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->