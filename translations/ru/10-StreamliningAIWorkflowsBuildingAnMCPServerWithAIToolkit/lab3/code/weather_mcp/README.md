# Weather MCP Server

Это пример MCP сервера на Python, реализующего инструменты для работы с погодой с использованием имитационных ответов. Его можно использовать как основу для собственного MCP сервера. Включает следующие возможности:

- **Weather Tool**: инструмент, предоставляющий имитированную информацию о погоде на основе указанного местоположения.
- **Подключение к Agent Builder**: функция, позволяющая подключить MCP сервер к Agent Builder для тестирования и отладки.
- **Отладка в [MCP Inspector](https://github.com/modelcontextprotocol/inspector)**: возможность отладки MCP сервера с помощью MCP Inspector.

## Начало работы с шаблоном Weather MCP Server

> **Требования**
>
> Для запуска MCP сервера на локальной машине разработчика вам потребуется:
>
> - [Python](https://www.python.org/)
> - (*Опционально — если предпочитаете uv*) [uv](https://github.com/astral-sh/uv)
> - [Расширение Python Debugger](https://marketplace.visualstudio.com/items?itemName=ms-python.debugpy)

## Подготовка окружения

Существует два способа настройки окружения для этого проекта. Вы можете выбрать любой из них в зависимости от предпочтений.

> Примечание: Перезапустите VSCode или терминал, чтобы убедиться, что используется Python из виртуального окружения после его создания.

| Способ | Шаги |
| -------- | ----- |
| Использование `uv` | 1. Создайте виртуальное окружение: `uv venv` <br>2. В VSCode выполните команду "***Python: Select Interpreter***" и выберите Python из созданного виртуального окружения <br>3. Установите зависимости (включая dev-зависимости): `uv pip install -r pyproject.toml --extra dev` |
| Использование `pip` | 1. Создайте виртуальное окружение: `python -m venv .venv` <br>2. В VSCode выполните команду "***Python: Select Interpreter***" и выберите Python из созданного виртуального окружения<br>3. Установите зависимости (включая dev-зависимости): `pip install -e .[dev]` |

После настройки окружения вы можете запустить сервер на локальной машине разработчика через Agent Builder в качестве MCP клиента, чтобы начать работу:
1. Откройте панель отладки VS Code. Выберите `Debug in Agent Builder` или нажмите `F5` для запуска отладки MCP сервера.
2. Используйте AI Toolkit Agent Builder для тестирования сервера с помощью [этого запроса](../../../../../../../../../../open_prompt_builder). Сервер автоматически подключится к Agent Builder.
3. Нажмите `Run`, чтобы протестировать сервер с этим запросом.

**Поздравляем!** Вы успешно запустили Weather MCP Server на локальной машине разработчика через Agent Builder в качестве MCP клиента.  
![DebugMCP](https://raw.githubusercontent.com/microsoft/windows-ai-studio-templates/refs/heads/dev/mcpServers/mcp_debug.gif)

## Что входит в шаблон

| Папка / Файл | Содержание                                  |
| ------------ | ------------------------------------------ |
| `.vscode`    | Файлы VSCode для отладки                    |
| `.aitk`      | Конфигурации для AI Toolkit                  |
| `src`        | Исходный код MCP сервера для работы с погодой |

## Как отлаживать Weather MCP Server

> Примечания:
> - [MCP Inspector](https://github.com/modelcontextprotocol/inspector) — визуальный инструмент для разработчиков для тестирования и отладки MCP серверов.
> - Все режимы отладки поддерживают точки останова, поэтому вы можете ставить их в коде реализации инструментов.

| Режим отладки | Описание | Шаги для отладки |
| ------------- | -------- | ---------------- |
| Agent Builder | Отладка MCP сервера в Agent Builder через AI Toolkit. | 1. Откройте панель отладки VS Code. Выберите `Debug in Agent Builder` и нажмите `F5` для запуска отладки MCP сервера.<br>2. Используйте AI Toolkit Agent Builder для тестирования сервера с помощью [этого запроса](../../../../../../../../../../open_prompt_builder). Сервер автоматически подключится к Agent Builder.<br>3. Нажмите `Run`, чтобы протестировать сервер с этим запросом. |
| MCP Inspector | Отладка MCP сервера с помощью MCP Inspector. | 1. Установите [Node.js](https://nodejs.org/)<br>2. Настройте Inspector: `cd inspector` && `npm install`<br>3. Откройте панель отладки VS Code. Выберите `Debug SSE in Inspector (Edge)` или `Debug SSE in Inspector (Chrome)`. Нажмите F5 для запуска отладки.<br>4. Когда MCP Inspector откроется в браузере, нажмите кнопку `Connect`, чтобы подключить этот MCP сервер.<br>5. Затем вы можете `List Tools`, выбрать инструмент, ввести параметры и `Run Tool` для отладки кода сервера.<br> |

## Порты по умолчанию и настройки

| Режим отладки | Порты | Определения | Настройки | Примечание |
| ------------- | ----- | ----------- | --------- | ---------- |
| Agent Builder | 3001  | [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/tasks.json) | Отредактируйте [launch.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/launch.json), [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/tasks.json), [\_\_init\_\_.py](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/src/__init__.py), [mcp.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.aitk/mcp.json) для изменения указанных портов. | Нет |
| MCP Inspector | 3001 (сервер); 5173 и 3000 (Inspector) | [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/tasks.json) | Отредактируйте [launch.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/launch.json), [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/tasks.json), [\_\_init\_\_.py](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/src/__init__.py), [mcp.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.aitk/mcp.json) для изменения указанных портов. | Нет |

## Обратная связь

Если у вас есть отзывы или предложения по этому шаблону, пожалуйста, создайте issue в репозитории [AI Toolkit GitHub](https://github.com/microsoft/vscode-ai-toolkit/issues)

**Отказ от ответственности**:  
Этот документ был переведен с помощью сервиса автоматического перевода [Co-op Translator](https://github.com/Azure/co-op-translator). Несмотря на наши усилия по обеспечению точности, просим учитывать, что автоматический перевод может содержать ошибки или неточности. Оригинальный документ на его исходном языке следует считать авторитетным источником. Для получения критически важной информации рекомендуется обращаться к профессиональному переводу, выполненному человеком. Мы не несем ответственности за любые недоразумения или неправильные толкования, возникшие в результате использования данного перевода.