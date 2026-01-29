# Пример использования: Экспонирование REST API в API Management как MCP сервер

Azure API Management — это сервис, предоставляющий шлюз поверх ваших конечных точек API. Он работает как прокси перед вашими API и может управлять входящими запросами.

Используя его, вы получаете множество возможностей, таких как:

- **Безопасность**: можно использовать всё, начиная от API-ключей и JWT до управляемой идентификации.
- **Ограничение скорости**: отличная функция, позволяющая определить, сколько запросов может быть обработано за определённый промежуток времени. Это помогает обеспечить отличный пользовательский опыт и защитить ваш сервис от перегрузки.
- **Масштабирование и балансировка нагрузки**: можно настроить несколько конечных точек для распределения нагрузки и выбрать способ балансировки.
- **AI-функции, такие как семантическое кэширование**, лимит токенов, мониторинг токенов и многое другое. Эти функции улучшают отзывчивость и помогают контролировать расход токенов. [Подробнее здесь](https://learn.microsoft.com/en-us/azure/api-management/genai-gateway-capabilities).

## Почему MCP + Azure API Management?

Model Context Protocol быстро становится стандартом для агентных AI-приложений и способа предоставления инструментов и данных в едином формате. Azure API Management — это естественный выбор, когда нужно "управлять" API. MCP серверы часто интегрируются с другими API для обработки запросов к инструментам. Поэтому комбинация Azure API Management и MCP имеет большой смысл.

## Обзор

В этом конкретном случае мы научимся экспонировать конечные точки API как MCP сервер. Это позволит легко интегрировать эти конечные точки в агентное приложение, одновременно используя возможности Azure API Management.

## Основные возможности

- Вы выбираете методы конечных точек, которые хотите экспонировать как инструменты.
- Дополнительные функции зависят от того, что вы настроите в разделе политики для вашего API. Здесь мы покажем, как добавить ограничение скорости.

## Предварительный шаг: импорт API

Если у вас уже есть API в Azure API Management, отлично, этот шаг можно пропустить. Если нет, ознакомьтесь с этим руководством: [импорт API в Azure API Management](https://learn.microsoft.com/en-us/azure/api-management/import-and-publish#import-and-publish-a-backend-api).

## Экспонирование API как MCP сервера

Чтобы экспонировать конечные точки API, выполните следующие шаги:

1. Перейдите в Azure Portal по адресу <https://portal.azure.com/?Microsoft_Azure_ApiManagement=mcp>. Найдите ваш экземпляр API Management.

1. В левом меню выберите **APIs > MCP Servers > + Create new MCP Server**.

1. В разделе API выберите REST API, который нужно экспонировать как MCP сервер.

1. Выберите одну или несколько операций API для экспонирования как инструменты. Можно выбрать все операции или только определённые.

    ![Выбор методов для экспонирования](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/create-mcp-server-small.png)

1. Нажмите **Create**.

1. Перейдите в меню **APIs** и **MCP Servers**, вы должны увидеть следующее:

    ![Просмотр MCP сервера в главной панели](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-list.png)

    MCP сервер создан, и операции API экспонированы как инструменты. MCP сервер отображается в панели MCP Servers. В колонке URL указан адрес MCP сервера, который можно использовать для тестирования или в клиентском приложении.

## Дополнительно: Настройка политик

Azure API Management имеет ключевую концепцию политик, где вы можете задавать различные правила для ваших конечных точек, например, ограничение скорости или семантическое кэширование. Эти политики задаются в формате XML.

Вот как можно настроить политику для ограничения скорости вашего MCP сервера:

1. В портале, в разделе APIs, выберите **MCP Servers**.

1. Выберите созданный MCP сервер.

1. В левом меню, в разделе MCP, выберите **Policies**.

1. В редакторе политик добавьте или измените политики, которые вы хотите применить к инструментам MCP сервера. Политики определяются в формате XML. Например, можно добавить политику, чтобы ограничить количество вызовов инструментов MCP сервера (в данном примере 5 вызовов за 30 секунд с одного IP-адреса клиента). Вот пример XML для ограничения скорости:

    ```xml
     <rate-limit-by-key calls="5" 
       renewal-period="30" 
       counter-key="@(context.Request.IpAddress)" 
       remaining-calls-variable-name="remainingCallsPerIP" 
    />
    ```

    Вот изображение редактора политик:

    ![Редактор политик](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-policies-small.png)

## Проверка работы

Убедимся, что наш MCP сервер работает корректно.

Для этого мы будем использовать Visual Studio Code и GitHub Copilot в режиме Agent. Мы добавим MCP сервер в файл *mcp.json*. Это позволит Visual Studio Code выступать в роли клиента с агентными возможностями, а конечные пользователи смогут вводить запросы и взаимодействовать с сервером.

Вот как это сделать:

1. Используйте команду **MCP: Add Server** из Command Palette.

1. Когда появится запрос, выберите тип сервера: **HTTP (HTTP или Server Sent Events)**.

1. Введите URL MCP сервера в API Management. Пример: **https://<apim-service-name>.azure-api.net/<api-name>-mcp/sse** (для SSE конечной точки) или **https://<apim-service-name>.azure-api.net/<api-name>-mcp/mcp** (для MCP конечной точки). Обратите внимание на разницу в транспортах: `/sse` или `/mcp`.

1. Укажите идентификатор сервера на ваш выбор. Это неважное значение, но оно поможет вам запомнить, что это за экземпляр сервера.

1. Выберите, сохранить ли конфигурацию в настройках рабочей области или в пользовательских настройках.

  - **Настройки рабочей области** — конфигурация сервера сохраняется в файле .vscode/mcp.json, доступном только в текущей рабочей области.

    *mcp.json*

    ```json
    "servers": {
        "APIM petstore" : {
            "type": "sse",
            "url": "url-to-mcp-server/sse"
        }
    }
    ```

    или, если вы выбрали потоковый HTTP как транспорт, это будет немного отличаться:

    ```json
    "servers": {
        "APIM petstore" : {
            "type": "http",
            "url": "url-to-mcp-server/mcp"
        }
    }
    ```

  - **Пользовательские настройки** — конфигурация сервера добавляется в ваш глобальный файл *settings.json* и доступна во всех рабочих областях. Конфигурация будет выглядеть следующим образом:

    ![Пользовательские настройки](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-servers-visual-studio-code.png)

1. Также необходимо добавить заголовок для корректной аутентификации в Azure API Management. Используется заголовок **Ocp-Apim-Subscription-Key**.

    - Вот как его можно добавить в настройки:

    ![Добавление заголовка для аутентификации](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-with-header-visual-studio-code.png). Это вызовет запрос на ввод значения API ключа, который можно найти в Azure Portal для вашего экземпляра Azure API Management.

   - Чтобы добавить его в *mcp.json*, сделайте это следующим образом:

    ```json
    "inputs": [
      {
        "type": "promptString",
        "id": "apim_key",
        "description": "API Key for Azure API Management",
        "password": true
      }
    ]
    "servers": {
        "APIM petstore" : {
            "type": "http",
            "url": "url-to-mcp-server/mcp",
            "headers": {
                "Ocp-Apim-Subscription-Key": "Bearer ${input:apim_key}"
            }
        }
    }
    ```

### Использование режима Agent

Теперь всё настроено либо в настройках, либо в *.vscode/mcp.json*. Давайте проверим.

Должна появиться иконка Tools, где будут перечислены инструменты, экспонированные вашим сервером:

![Инструменты сервера](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/tools-button-visual-studio-code.png)

1. Нажмите на иконку Tools, и вы увидите список инструментов:

    ![Инструменты](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/select-tools-visual-studio-code.png)

1. Введите запрос в чат для вызова инструмента. Например, если вы выбрали инструмент для получения информации о заказе, вы можете спросить агента о заказе. Вот пример запроса:

    ```text
    get information from order 2
    ```

    Вам будет предложено продолжить вызов инструмента. Выберите продолжение, и вы увидите результат, например:

    ![Результат запроса](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/chat-results-visual-studio-code.png)

    **То, что вы увидите, зависит от настроенных инструментов, но идея в том, чтобы получить текстовый ответ, как показано выше.**

## Ссылки

Вот где можно узнать больше:

- [Руководство по Azure API Management и MCP](https://learn.microsoft.com/en-us/azure/api-management/export-rest-mcp-server)
- [Пример на Python: Защита удалённых MCP серверов с использованием Azure API Management (экспериментально)](https://github.com/Azure-Samples/remote-mcp-apim-functions-python)

- [Лаборатория авторизации MCP клиента](https://github.com/Azure-Samples/AI-Gateway/tree/main/labs/mcp-client-authorization)

- [Использование расширения Azure API Management для VS Code для импорта и управления API](https://learn.microsoft.com/en-us/azure/api-management/visual-studio-code-tutorial)

- [Регистрация и обнаружение удалённых MCP серверов в Azure API Center](https://learn.microsoft.com/en-us/azure/api-center/register-discover-mcp-server)
- [AI Gateway](https://github.com/Azure-Samples/AI-Gateway) — отличный репозиторий, демонстрирующий множество возможностей AI с Azure API Management.
- [Мастер-классы AI Gateway](https://azure-samples.github.io/AI-Gateway/) — содержит мастер-классы с использованием Azure Portal, отличный способ начать оценку возможностей AI.

**Отказ от ответственности**:  
Этот документ был переведен с использованием сервиса автоматического перевода [Co-op Translator](https://github.com/Azure/co-op-translator). Несмотря на наши усилия обеспечить точность, автоматические переводы могут содержать ошибки или неточности. Оригинальный документ на его исходном языке следует считать авторитетным источником. Для получения критически важной информации рекомендуется профессиональный перевод человеком. Мы не несем ответственности за любые недоразумения или неправильные интерпретации, возникающие в результате использования данного перевода.