# Казус: Излагане на REST API в API Management като MCP сървър

Azure API Management е услуга, която предоставя Gateway над вашите API крайни точки. Как работи: Azure API Management действа като прокси пред вашите API и може да реши какво да прави с входящите заявки.

Използвайки го, добавяте множество функции като:

- **Сигурност** – можете да използвате всичко от API ключове, JWT до управлявана идентичност.
- **Ограничаване на честотата** – страхотна функция, която ви позволява да решите колко заявки да преминават за определен времеви интервал. Това помага да се гарантира, че всички потребители имат добро изживяване и че вашата услуга не е претоварена със заявки.
- **Мащабиране и балансиране на натоварването** – можете да настроите множество крайни точки, за да разпределите натоварването, и също така да решите как да "балансирате натоварването".
- **AI функции като семантично кеширане**, ограничение на токени, мониторинг на токени и други. Това са страхотни функции, които подобряват отзивчивостта и ви помагат да следите разхода на токени. [Прочетете повече тук](https://learn.microsoft.com/en-us/azure/api-management/genai-gateway-capabilities).

## Защо MCP + Azure API Management?

Model Context Protocol бързо се превръща в стандарт за агентни AI приложения и начин за излагане на инструменти и данни по последователен начин. Azure API Management е естествен избор, когато трябва да "управлявате" API. MCP сървърите често се интегрират с други API, за да обработват заявки към инструмент например. Затова комбинирането на Azure API Management и MCP има много смисъл.

## Преглед

В този конкретен случай ще научим как да изложим API крайни точки като MCP сървър. Правейки това, можем лесно да направим тези крайни точки част от агентно приложение, като същевременно използваме функциите на Azure API Management.

## Основни функции

- Избирате методите на крайни точки, които искате да изложите като инструменти.
- Допълнителните функции, които получавате, зависят от това какво конфигурирате в секцията за политики за вашия API. Но тук ще ви покажем как можете да добавите ограничаване на честотата.

## Предварителна стъпка: импортиране на API

Ако вече имате API в Azure API Management, чудесно, тогава можете да пропуснете тази стъпка. Ако не, вижте този линк: [импортиране на API в Azure API Management](https://learn.microsoft.com/en-us/azure/api-management/import-and-publish#import-and-publish-a-backend-api).

## Излагане на API като MCP сървър

За да изложим API крайните точки, следвайте тези стъпки:

1. Отидете в Azure Portal на следния адрес <https://portal.azure.com/?Microsoft_Azure_ApiManagement=mcp>. 
Отидете до вашия API Management инстанс.

1. В лявото меню изберете APIs > MCP Servers > + Create new MCP Server.

1. В API изберете REST API, който да изложите като MCP сървър.

1. Изберете една или повече API операции, които да изложите като инструменти. Можете да изберете всички операции или само конкретни операции.

    ![Избор на методи за излагане](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/create-mcp-server-small.png)

1. Изберете **Create**.

1. Отидете в менюто **APIs** и **MCP Servers**, трябва да видите следното:

    ![Вижте MCP сървъра в основния панел](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-list.png)

    MCP сървърът е създаден и API операциите са изложени като инструменти. MCP сървърът е изброен в панела MCP Servers. Колоната URL показва крайната точка на MCP сървъра, която можете да извикате за тестване или в клиентско приложение.

## Опционално: Конфигуриране на политики

Azure API Management има основната концепция за политики, където задавате различни правила за вашите крайни точки, като например ограничаване на честотата или семантично кеширане. Тези политики се създават в XML.

Ето как можете да настроите политика за ограничаване на честотата на вашия MCP сървър:

1. В портала, под APIs, изберете **MCP Servers**.

1. Изберете MCP сървъра, който сте създали.

1. В лявото меню, под MCP, изберете **Policies**.

1. В редактора на политики добавете или редактирайте политиките, които искате да приложите към инструментите на MCP сървъра. Политиките се дефинират в XML формат. Например, можете да добавите политика за ограничаване на заявките към инструментите на MCP сървъра (в този пример, 5 заявки на всеки 30 секунди на клиентски IP адрес). Ето XML, който ще причини ограничаване на честотата:

    ```xml
     <rate-limit-by-key calls="5" 
       renewal-period="30" 
       counter-key="@(context.Request.IpAddress)" 
       remaining-calls-variable-name="remainingCallsPerIP" 
    />
    ```

    Ето изображение на редактора на политики:

    ![Редактор на политики](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-policies-small.png)

## Тествайте

Нека се уверим, че нашият MCP сървър работи както трябва.

За това ще използваме Visual Studio Code и GitHub Copilot в режим Agent. Ще добавим MCP сървъра към файл *mcp.json*. Правейки това, Visual Studio Code ще действа като клиент с агентни способности и крайните потребители ще могат да въвеждат заявки и да взаимодействат със сървъра.

Ето как да добавите MCP сървъра във Visual Studio Code:

1. Използвайте MCP: **Add Server команда от Command Palette**.

1. Когато бъдете подканени, изберете типа сървър: **HTTP (HTTP или Server Sent Events)**.

1. Въведете URL на MCP сървъра в API Management. Пример: **https://<apim-service-name>.azure-api.net/<api-name>-mcp/sse** (за SSE крайна точка) или **https://<apim-service-name>.azure-api.net/<api-name>-mcp/mcp** (за MCP крайна точка), обърнете внимание на разликата между транспортите `/sse` или `/mcp`.

1. Въведете ID на сървъра по ваш избор. Това не е важна стойност, но ще ви помогне да запомните какво представлява този сървър.

1. Изберете дали да запазите конфигурацията в настройките на работното пространство или в потребителските настройки.

  - **Настройки на работното пространство** – Конфигурацията на сървъра се запазва в файл .vscode/mcp.json, достъпен само в текущото работно пространство.

    *mcp.json*

    ```json
    "servers": {
        "APIM petstore" : {
            "type": "sse",
            "url": "url-to-mcp-server/sse"
        }
    }
    ```

    или ако изберете стрийминг HTTP като транспорт, ще бъде малко по-различно:

    ```json
    "servers": {
        "APIM petstore" : {
            "type": "http",
            "url": "url-to-mcp-server/mcp"
        }
    }
    ```

  - **Потребителски настройки** – Конфигурацията на сървъра се добавя към глобалния файл *settings.json* и е достъпна във всички работни пространства. Конфигурацията изглежда подобно на следното:

    ![Потребителска настройка](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-servers-visual-studio-code.png)

1. Трябва също да добавите конфигурация, заглавие, за да се уверите, че се удостоверява правилно към Azure API Management. Използва заглавие, наречено **Ocp-Apim-Subscription-Key**.

    - Ето как можете да го добавите към настройките:

    ![Добавяне на заглавие за удостоверяване](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-with-header-visual-studio-code.png), това ще причини показване на подкана за въвеждане на стойността на API ключа, която можете да намерите в Azure Portal за вашия Azure API Management инстанс.

   - За да го добавите към *mcp.json*, можете да го добавите така:

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

### Използване на режим Agent

Сега сме готови, независимо дали в настройките или в *.vscode/mcp.json*. Нека го тестваме.

Трябва да има икона за инструменти, където изложените инструменти от вашия сървър са изброени:

![Инструменти от сървъра](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/tools-button-visual-studio-code.png)

1. Кликнете върху иконата за инструменти и трябва да видите списък с инструменти като този:

    ![Инструменти](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/select-tools-visual-studio-code.png)

1. Въведете заявка в чата, за да извикате инструмента. Например, ако сте избрали инструмент за получаване на информация за поръчка, можете да попитате агента за поръчка. Ето примерна заявка:

    ```text
    get information from order 2
    ```

    Сега ще видите икона за инструменти, която ви подканва да продължите с извикването на инструмент. Изберете да продължите с изпълнението на инструмента, и трябва да видите резултат като този:

    ![Резултат от заявката](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/chat-results-visual-studio-code.png)

    **това, което виждате по-горе, зависи от инструментите, които сте настроили, но идеята е да получите текстов отговор като горния**

## Референции

Ето как можете да научите повече:

- [Урок за Azure API Management и MCP](https://learn.microsoft.com/en-us/azure/api-management/export-rest-mcp-server)
- [Python пример: Защитени отдалечени MCP сървъри с Azure API Management (експериментално)](https://github.com/Azure-Samples/remote-mcp-apim-functions-python)

- [Лаборатория за клиентско удостоверяване на MCP](https://github.com/Azure-Samples/AI-Gateway/tree/main/labs/mcp-client-authorization)

- [Използване на разширението Azure API Management за VS Code за импортиране и управление на API](https://learn.microsoft.com/en-us/azure/api-management/visual-studio-code-tutorial)

- [Регистриране и откриване на отдалечени MCP сървъри в Azure API Center](https://learn.microsoft.com/en-us/azure/api-center/register-discover-mcp-server)
- [AI Gateway](https://github.com/Azure-Samples/AI-Gateway) Страхотен репо, който показва много AI възможности с Azure API Management
- [AI Gateway работилници](https://azure-samples.github.io/AI-Gateway/) Съдържа работилници с използване на Azure Portal, което е чудесен начин да започнете да оценявате AI възможности.

**Отказ от отговорност**:  
Този документ е преведен с помощта на AI услуга за превод [Co-op Translator](https://github.com/Azure/co-op-translator). Въпреки че се стремим към точност, моля, имайте предвид, че автоматизираните преводи може да съдържат грешки или неточности. Оригиналният документ на неговия роден език трябва да се счита за авторитетен източник. За критична информация се препоръчва професионален човешки превод. Ние не носим отговорност за недоразумения или погрешни интерпретации, произтичащи от използването на този превод.