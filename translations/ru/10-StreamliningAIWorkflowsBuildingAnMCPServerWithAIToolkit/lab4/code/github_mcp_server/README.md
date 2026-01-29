# Сервер MCP для погоды

Это пример сервера MCP на Python, реализующий инструменты для работы с погодой с использованием фиктивных ответов. Его можно использовать как основу для создания собственного сервера MCP. Включает следующие функции:

- **Инструмент для погоды**: инструмент, предоставляющий фиктивную информацию о погоде на основе указанного местоположения.
- **Инструмент клонирования Git**: инструмент, который клонирует репозиторий Git в указанную папку.
- **Инструмент открытия VS Code**: инструмент, который открывает папку в VS Code или VS Code Insiders.
- **Подключение к Agent Builder**: функция, позволяющая подключить сервер MCP к Agent Builder для тестирования и отладки.
- **Отладка в [MCP Inspector](https://github.com/modelcontextprotocol/inspector)**: функция, позволяющая отлаживать сервер MCP с помощью MCP Inspector.

## Начало работы с шаблоном сервера MCP для погоды

> **Предварительные требования**
>
> Для запуска сервера MCP на локальной машине для разработки вам потребуется:
>
> - [Python](https://www.python.org/)
> - [Git](https://git-scm.com/) (требуется для инструмента git_clone_repo)
> - [VS Code](https://code.visualstudio.com/) или [VS Code Insiders](https://code.visualstudio.com/insiders/) (требуется для инструмента open_in_vscode)
> - (*Опционально - если вы предпочитаете uv*) [uv](https://github.com/astral-sh/uv)
> - [Расширение Python Debugger](https://marketplace.visualstudio.com/items?itemName=ms-python.debugpy)

## Подготовка окружения

Существует два подхода для настройки окружения этого проекта. Вы можете выбрать любой из них в зависимости от ваших предпочтений.

> Примечание: Перезагрузите VS Code или терминал, чтобы убедиться, что используется Python из виртуального окружения после его создания.

| Подход | Шаги |
| ------ | ---- |
| Использование `uv` | 1. Создайте виртуальное окружение: `uv venv` <br>2. Выполните команду VS Code "***Python: Select Interpreter***" и выберите Python из созданного виртуального окружения <br>3. Установите зависимости (включая зависимости для разработки): `uv pip install -r pyproject.toml --extra dev` |
| Использование `pip` | 1. Создайте виртуальное окружение: `python -m venv .venv` <br>2. Выполните команду VS Code "***Python: Select Interpreter***" и выберите Python из созданного виртуального окружения<br>3. Установите зависимости (включая зависимости для разработки): `pip install -e .[dev]` | 

После настройки окружения вы можете запустить сервер на локальной машине для разработки через Agent Builder в качестве клиента MCP, чтобы начать работу:
1. Откройте панель отладки в VS Code. Выберите `Debug in Agent Builder` или нажмите `F5`, чтобы начать отладку сервера MCP.
2. Используйте AI Toolkit Agent Builder для тестирования сервера с [этим запросом](../../../../../../../../../../../open_prompt_builder). Сервер будет автоматически подключен к Agent Builder.
3. Нажмите `Run`, чтобы протестировать сервер с запросом.

**Поздравляем**! Вы успешно запустили сервер MCP для погоды на локальной машине для разработки через Agent Builder в качестве клиента MCP.
![DebugMCP](https://raw.githubusercontent.com/microsoft/windows-ai-studio-templates/refs/heads/dev/mcpServers/mcp_debug.gif)

## Что включено в шаблон

| Папка / Файл | Содержимое                                   |
| ------------ | -------------------------------------------- |
| `.vscode`    | Файлы VS Code для отладки                   |
| `.aitk`      | Конфигурации для AI Toolkit                 |
| `src`        | Исходный код сервера MCP для погоды         |

## Как отлаживать сервер MCP для погоды

> Примечания:
> - [MCP Inspector](https://github.com/modelcontextprotocol/inspector) — это визуальный инструмент для разработчиков, предназначенный для тестирования и отладки серверов MCP.
> - Все режимы отладки поддерживают точки останова, поэтому вы можете добавлять точки останова в код реализации инструментов.

## Доступные инструменты

### Инструмент для погоды
Инструмент `get_weather` предоставляет фиктивную информацию о погоде для указанного местоположения.

| Параметр  | Тип    | Описание                                |
| --------- | ------ | --------------------------------------- |
| `location` | строка | Местоположение для получения данных о погоде (например, название города, штата или координаты) |

### Инструмент клонирования Git
Инструмент `git_clone_repo` клонирует репозиторий Git в указанную папку.

| Параметр       | Тип    | Описание                                      |
| -------------- | ------ | --------------------------------------------- |
| `repo_url`     | строка | URL репозитория Git для клонирования          |
| `target_folder` | строка | Путь к папке, куда должен быть клонирован репозиторий |

Инструмент возвращает объект JSON с:
- `success`: Булево значение, указывающее, была ли операция успешной
- `target_folder` или `error`: Путь клонированного репозитория или сообщение об ошибке

### Инструмент открытия VS Code
Инструмент `open_in_vscode` открывает папку в приложении VS Code или VS Code Insiders.

| Параметр       | Тип    | Описание                                      |
| -------------- | ------ | --------------------------------------------- |
| `folder_path`  | строка | Путь к папке для открытия                     |
| `use_insiders` | булево (опционально) | Использовать ли VS Code Insiders вместо обычного VS Code |

Инструмент возвращает объект JSON с:
- `success`: Булево значение, указывающее, была ли операция успешной
- `message` или `error`: Подтверждающее сообщение или сообщение об ошибке

| Режим отладки  | Описание | Шаги для отладки |
| -------------- | -------- | ---------------- |
| Agent Builder  | Отладка сервера MCP в Agent Builder через AI Toolkit. | 1. Откройте панель отладки в VS Code. Выберите `Debug in Agent Builder` и нажмите `F5`, чтобы начать отладку сервера MCP.<br>2. Используйте AI Toolkit Agent Builder для тестирования сервера с [этим запросом](../../../../../../../../../../../open_prompt_builder). Сервер будет автоматически подключен к Agent Builder.<br>3. Нажмите `Run`, чтобы протестировать сервер с запросом. |
| MCP Inspector  | Отладка сервера MCP с использованием MCP Inspector. | 1. Установите [Node.js](https://nodejs.org/)<br> 2. Настройте Inspector: `cd inspector` && `npm install` <br> 3. Откройте панель отладки в VS Code. Выберите `Debug SSE in Inspector (Edge)` или `Debug SSE in Inspector (Chrome)`. Нажмите F5, чтобы начать отладку.<br> 4. Когда MCP Inspector запустится в браузере, нажмите кнопку `Connect`, чтобы подключить этот сервер MCP.<br> 5. Затем вы можете `List Tools`, выбрать инструмент, ввести параметры и `Run Tool`, чтобы отладить код вашего сервера.<br> |

## Порты по умолчанию и настройки

| Режим отладки  | Порты | Определения | Настройки | Примечание |
| -------------- | ----- | ----------- | --------- | ---------- |
| Agent Builder  | 3001  | [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json) | Измените [launch.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/launch.json), [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json), [\_\_init\_\_.py](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/src/__init__.py), [mcp.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.aitk/mcp.json), чтобы изменить указанные порты. | N/A |
| MCP Inspector  | 3001 (сервер); 5173 и 3000 (Inspector) | [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json) | Измените [launch.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/launch.json), [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json), [\_\_init\_\_.py](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/src/__init__.py), [mcp.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.aitk/mcp.json), чтобы изменить указанные порты.| N/A |

## Обратная связь

Если у вас есть отзывы или предложения по этому шаблону, откройте задачу в [репозитории AI Toolkit на GitHub](https://github.com/microsoft/vscode-ai-toolkit/issues).

---

**Отказ от ответственности**:  
Этот документ был переведен с помощью сервиса автоматического перевода [Co-op Translator](https://github.com/Azure/co-op-translator). Несмотря на наши усилия обеспечить точность, автоматические переводы могут содержать ошибки или неточности. Оригинальный документ на его родном языке следует считать авторитетным источником. Для получения критически важной информации рекомендуется профессиональный перевод человеком. Мы не несем ответственности за любые недоразумения или неправильные интерпретации, возникшие в результате использования данного перевода.