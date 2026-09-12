# Казус: Излагане на REST API в API Management като MCP сървър

Azure API Management е услуга, която предоставя Gateway над вашите API крайни точки. Как работи е, че Azure API Management действа като прокси пред вашите API-та и може да реши какво да прави с входящите заявки.

Като го използвате, добавяте множество функции като:

- **Сигурност**, можете да използвате всичко от API ключове, JWT до управлявани идентичности.
- **Ограничаване на честотата**, страхотна функция е възможността да решите колко повиквания да преминават за определен период от време. Това помага да се осигури отличен опит за всички потребители и също така услугата ви да не бъде претоварена с заявки.
- **Мащабиране и балансиране на натоварването**. Можете да настроите няколко крайни точки, за да разпределите натоварването и също така да решите как да „балансирате натоварването“.
- **AI функции като семантично кеширане**, лимити за токени и мониторинг на токени и други. Това са страхотни функции, които подобряват отзивчивостта, както и помагат да сте наясно с разходите си за токени. [Прочетете повече тук](https://learn.microsoft.com/en-us/azure/api-management/genai-gateway-capabilities).

## Защо MCP + Azure API Management?

Model Context Protocol бързо се превръща в стандарт за агентски AI приложения и как да се излагат инструменти и данни по последователен начин. Azure API Management е естественият избор, когато трябва да „управлявате“ API-та. MCP Сървърите често се интегрират с други API-та, за да разрешат заявки към инструмент, например. Следователно комбинирането на Azure API Management и MCP има много логика.

## Преглед

В този конкретен случай ще научим как да излагаме API крайни точки като MCP Сървър. По този начин можем лесно да направим тези крайни точки част от агентско приложение, като същевременно използваме функциите на Azure API Management.

## Ключови функции

- Вие избирате методите на крайна точка, които искате да изложите като инструменти.
- Допълнителните функции, които получавате, зависят от конфигурацията в секцията с политики за вашия API. Тук ще ви покажем как да добавите ограничаване на честотата.

## Предварителна стъпка: импортиране на API

Ако вече имате API в Azure API Management, отлично, можете да пропуснете тази стъпка. Ако не, разгледайте този линк, [импортиране на API в Azure API Management](https://learn.microsoft.com/en-us/azure/api-management/import-and-publish#import-and-publish-a-backend-api).

## Излагане на API като MCP Сървър

За да изложите API крайните точки, да следваме тези стъпки:

1. Навигирайте до Azure портала на следния адрес <https://portal.azure.com/?Microsoft_Azure_ApiManagement=mcp>
Навигирайте до вашия екземпляр на API Management.

1. В левия меню, изберете APIs > MCP Servers > + Създай нов MCP Сървър.

1. В API изберете REST API, който да изложите като MCP сървър.

1. Изберете една или повече API операции, които да излагате като инструменти. Можете да изберете всички операции или само конкретни операции.

    ![Изберете методи за излагане](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/create-mcp-server-small.png)


1. Изберете **Създай**.

1. Навигирайте до менюто **APIs** и **MCP Servers**, трябва да видите следното:

    ![Вижте MCP сървъра в основното поле](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-list.png)

    MCP сървърът е създаден и API операциите са изложени като инструменти. MCP сървърът е изброен в панела MCP Servers. Колоната URL показва крайната точка на MCP сървъра, която можете да извиквате за тестване или в клиентско приложение.

## По избор: Конфигуриране на политики

Azure API Management има основната концепция за политики, в които настройвате различни правила за вашите крайни точки, като например ограничаване на честотата или семантично кеширане. Тези политики се пишат в XML.

Ето как може да настроите политика за ограничаване на честотата за вашия MCP сървър:

1. В портала, под APIs, изберете **MCP Servers**.

1. Изберете създадения от вас MCP сървър.

1. В лявото меню, под MCP, изберете **Policies**.

1. В редактора на политики добавете или редактирайте политиките, които искате да приложите към инструментите на MCP сървъра. Политиките са дефинирани в XML формат. Например, можете да добавите политика, която ограничава повикванията към инструментите на MCP сървъра (в този пример, 5 повиквания на 30 секунди за IP адрес на клиент). Ето XML, който ще причини ограничаването:

    ```xml
     <rate-limit-by-key calls="5" 
       renewal-period="30" 
       counter-key="@(context.Request.IpAddress)" 
       remaining-calls-variable-name="remainingCallsPerIP" 
    />
    ```

    Ето изображение на редактора на политики:

    ![Редактор на политики](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-policies-small.png)
 
## Изпробвайте го

Да се уверим, че нашият MCP сървър работи както е предназначено.

> [!NOTE]
> Azure API Management в момента излага този сървър чрез Streamable
> HTTP `/mcp` крайна точка. По-старият HTTP+SSE `/sse` транспорт е остарял и
> трябва да се използва само с наследени клиенти.

За целта ще използваме Visual Studio Code и GitHub Copilot в Agent режим. Ще добавим MCP сървъра към *mcp.json* файл. По този начин Visual Studio Code ще действа като клиент с агентски възможности и крайните потребители ще могат да въвеждат подканващ текст и да взаимодействат с този сървър.

Нека видим как да добавим MCP сървъра във Visual Studio Code:

1. Използвайте командата MCP: **Add Server от Command Palette**.

1. Когато бъдете подканени, изберете тип сървър: **HTTP (HTTP или Server Sent Events)**.

1. Въведете Streamable HTTP URL, показан за MCP сървъра в API Management.
    Например:
    `https://<apim-service-name>.azure-api.net/<api-name>-mcp/mcp`.

1. Въведете ID на сървъра по ваш избор. Това не е важна стойност, но ще ви помогне да запомните какъв е този сървър.

1. Изберете дали да запазите конфигурацията в настройките на работното пространство или в потребителските настройки.

  - **Настройки на работното пространство** - Конфигурацията на сървъра се запазва в .vscode/mcp.json файл, който е наличен само в текущото работно пространство.

    *mcp.json*

    ```json
    "servers": {
        "APIM petstore" : {
            "type": "http",
            "url": "url-to-mcp-server/mcp"
        }
    }
    ```

  - **Потребителски настройки** - Конфигурацията на сървъра се добавя към глобалния *settings.json* файл и е налична във всички работни пространства. Конфигурацията изглежда подобно на следното:

    ![Потребителска настройка](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-servers-visual-studio-code.png)

1. Трябва също да добавите конфигурация, заглавка, за да се удостоверява правилно към Azure API Management. Използва заглавка, наречена **Ocp-Apim-Subscription-Key*.

    - Ето как можете да я добавите в настройките:

    ![Добавяне на заглавка за удостоверяване](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-with-header-visual-studio-code.png), това ще предизвика да се появи подкана да въведете стойността на API ключа, който можете да намерите в Azure портала за вашия Azure API Management екземпляр.

   - За да го добавите в *mcp.json* вместо това, може да го добавите така:

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

### Използване на Agent режим

Сега сме всичко настроено или в настройките, или в *.vscode/mcp.json*. Нека го изпробваме.

Трябва да има икона за Инструменти, където са изброени изложените инструменти от вашия сървър:

![Инструменти от сървъра](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/tools-button-visual-studio-code.png)

1. Кликнете върху иконата инструменти и трябва да видите списък с инструменти, както е показано:

    ![Инструменти](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/select-tools-visual-studio-code.png)

1. Въведете подканващ текст в чата, за да използвате инструмента. Например, ако сте избрали инструмент за получаване на информация за поръчка, можете да попитате агента за поръчка. Ето примерен подканващ текст:

    ```text
    get information from order 2
    ```

    Сега ще видите икона за инструменти, която ще ви попита дали да продължите с извикването на инструмента. Изберете да продължите изпълнението на инструмента, вече трябва да видите резултат подобен на този:

    ![Резултат от подканващия текст](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/chat-results-visual-studio-code.png)

    **Това, което виждате, зависи от инструментите, които сте настроили, но идеята е, че получавате текстов отговор като горния**


## Препратки

Ето как можете да научите повече:

- [Урок за Azure API Management и MCP](https://learn.microsoft.com/en-us/azure/api-management/export-rest-mcp-server)
- [Python пример: Защита на отдалечени MCP сървъри чрез Azure API Management (експериментално)](https://github.com/Azure-Samples/remote-mcp-apim-functions-python)

- [Лаборатория за оторизация на MCP клиент](https://github.com/Azure-Samples/AI-Gateway/tree/main/labs/mcp-client-authorization)

- [Използвайте разширението Azure API Management за VS Code за импортиране и управление на API-та](https://learn.microsoft.com/en-us/azure/api-management/visual-studio-code-tutorial)

- [Регистриране и откриване на отдалечени MCP сървъри в Azure API Center](https://learn.microsoft.com/en-us/azure/api-center/register-discover-mcp-server)
- [AI Gateway](https://github.com/Azure-Samples/AI-Gateway) Отлично хранилище, което показва множество AI възможности с Azure API Management
- [Работилници на AI Gateway](https://azure-samples.github.io/AI-Gateway/) Съдържа работилници с използване на Azure портала, което е отличен начин за оценка на AI възможностите.

## Какво следва

- Обратно към: [Преглед на казуси](./README.md)
- Следва: [Azure AI Travel Agents](./travelagentsample.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Отказ от отговорност**:
Този документ е преведен с помощта на AI преводачески услуга [Co-op Translator](https://github.com/Azure/co-op-translator). Въпреки че се стремим към точност, моля имайте предвид, че автоматизираните преводи могат да съдържат грешки или неточности. Оригиналният документ на неговия роден език трябва да се счита за авторитетен източник. За критична информация се препоръчва професионален човешки превод. Ние не носим отговорност за каквито и да е недоразумения или неправилни тълкувания, произтичащи от използването на този превод.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->