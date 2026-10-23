# Студија случаја: Изложите REST API у API Management као MCP сервер

Azure API Management је сервис који пружа Gateway преко ваших API крајњих тачака. Начин рада је такав да Azure API Management делује као прокси испред ваших API-ја и може да одлучи шта да ради са долазним захтевима.

Коришћењем овог сервиса добијате читав низ функција као што су:

- **Безбедност**, можете користити све од API кључева, JWT до управљаног идентитета.
- **Ограничење броја позива (Rate limiting)**, сјајна функција која вам омогућава да одредите колико позива може проћи у одређеном временском периоду. Ово помаже да сви корисници имају одлично искуство и такође спречава преоптерећење вашег сервиса захтевима.
- **Скалабилност и балансирање оптерећења**. Можете подесити неколико крајњих тачака за баланс оптерећења и можете одлучити како желите да "балансирате оптерећење".
- **AI функције као што су семантичко кеширање**, лимити на број токена, праћење токена и још много тога. Ове функције побољшавају одзив система као и помажу вам да пратите трошкове на токене. [Прочитајте више овде](https://learn.microsoft.com/en-us/azure/api-management/genai-gateway-capabilities).

## Зашто MCP + Azure API Management?

Model Context Protocol брзо постаје стандард за агентске AI апликације и начин изложења алата и података на конзистентан начин. Azure API Management је природан избор када треба "управљати" API-јима. MCP сервери често интегришу друге API-је, на пример за резолвовање захтева према алату. Због тога комбинација Azure API Management и MCP има смисла.

## Преглед

У овом конкретном примеру научићемо како да изложимо API крајње тачке као MCP сервер. На овај начин можемо лако укључити ове крајње тачке у агентску апликацију уз коришћење функција Azure API Management.

## Кључне карактеристике

- Одаберите методе крајњих тачака које желите да изложите као алате.
- Додатне функције које добијате зависе од тога шта конфигуришете у секцији политика за ваш API. Овде ћемо вам показати како да додате ограничење броја позива (rate limiting).

## Претходни корак: uvezite API

Ако већ имате API у Azure API Management, одлично, можете прескочити овај корак. У супротном, погледајте овај линк, [uvoženje API-ja u Azure API Management](https://learn.microsoft.com/en-us/azure/api-management/import-and-publish#import-and-publish-a-backend-api).

## Изложите API као MCP сервер

Да бисмо изложили API крајње тачке, пратите следеће кораке:

1. Идите у Azure портал на адресу <https://portal.azure.com/?Microsoft_Azure_ApiManagement=mcp>
Идите на вашу инстанцу API Management.

1. У левом менију изаберите APIs > MCP Servers > + Create new MCP Server.

1. У API, изаберите REST API који желите изложити као MCP сервер.

1. Изаберите једну или више операција API-ја које желите изложити као алате. Можете одабрати све операције или само специфичне.

    ![Изаберите методе за изложење](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/create-mcp-server-small.png)


1. Изаберите **Create**.

1. Идите у мени избор **APIs** и **MCP Servers**, требало би да видите следеће:

    ![Видети MCP сервер у главном прозору](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-list.png)

    MCP сервер је креиран и операције API-ја изложене као алати. MCP сервер је наведен у панелу MCP Servers. Колона URL приказује крајњу тачку MCP сервера коју можете позивати за тестирање или кроз клијент апликацију.

## Опционо: Конфигуришите политике

Azure API Management има основни концепт политика, где подешавате различита правила за ваше крајње тачке као што су ограничење броја позива или семантичко кеширање. Ове политике се дефинишу у XML формату.

Ево како можете поставити политику за ограничење броја позива MCP сервера:

1. У порталу, испод APIs, изаберите **MCP Servers**.

1. Изаберите MCP сервер који сте креирали.

1. У левом менију, испод MCP, изаберите **Policies**.

1. У едитору политика додајте или измените политике које желите применити на алате MCP сервера. Политике су дефинисане у XML формату. На пример, можете додати политику која ограничава број позива ка алатима MCP сервера (у овом примеру, 5 позива у 30 секунди по IP адреси клијента). Ево XML-а који ће извршити овај ограничење:

    ```xml
     <rate-limit-by-key calls="5" 
       renewal-period="30" 
       counter-key="@(context.Request.IpAddress)" 
       remaining-calls-variable-name="remainingCallsPerIP" 
    />
    ```

    Ево слике едитера политика:

    ![Едитор политика](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-policies-small.png)
 
## Испробајте

Уверимо се да наш MCP сервер ради како треба.

> [!NOTE]
> Azure API Management тренутно изложен овај сервер преко Streamable
> HTTP `/mcp` крајње тачке. Старији HTTP+SSE `/sse` транспорт је застарео и
> треба га користити само са старијим клијентима.

За ово ћемо користити Visual Studio Code и GitHub Copilot у агентском режиму. Додаћемо MCP сервер у *mcp.json* фајл. На овај начин, Visual Studio Code ће деловати као клијент са агентским могућностима и крајњи корисници ће моћи да уносе упите и интерагују са тим сервером.

Погледајмо како, да додате MCP сервер у Visual Studio Code:

1. Користите наредбу MCP: **Add Server из Командне Палете**.

1. Када вас пита, изаберите тип сервера: **HTTP (HTTP или Server Sent Events)**.

1. Унесите Streamable HTTP URL који је приказан за MCP сервер у API Management.
    На пример:
    `https://<apim-service-name>.azure-api.net/<api-name>-mcp/mcp`.

1. Унесите ID сервера по свом избору. Овај податак није критичан али ће вам помоћи да се сетите које је ово инстанца сервера.

1. Изаберите да ли да сачувате конфигурацију у подешавања радног простора или корисничка подешавања.

    - **Workspace settings** - Конфигурација сервера се чува у `.vscode/mcp.json` фајлу који је доступан само у тренутном радном простору.

      *mcp.json*

      ```json
      "servers": {
          "APIM petstore" : {
              "type": "http",
              "url": "url-to-mcp-server/mcp"
          }
      }
      ```

    - **User settings** - Конфигурација сервера се додаје у глобални *settings.json* фајл и доступна је у свим радним просторима. Конфигурација личи на ову:

      ![Корисничка подешавања](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-servers-visual-studio-code.png)

1. Такође треба да додате заглавље за аутентификацију да би MCP сервер исправно аутентификовао према Azure API Management. Користи се заглавље звано **Ocp-Apim-Subscription-Key**.

    - Ево како можете да га додате у подешавања:


    ![Додавање заглавља за аутентификацију](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-with-header-visual-studio-code.png), ово ће приказати упит за унос вредности API кључа који можете пронаћи у Azure порталу за вашу Azure API Management инстанцу.

   - Да бисте га додали у *mcp.json*, можете га додати овако:

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

### Користите Агентски режим

Сада смо спремни у подешавањима или у *.vscode/mcp.json*. Хајде да испробамо.

Требало би да постоји икона Алати где су изложени алати са вашег сервера:

![Алати са сервера](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/tools-button-visual-studio-code.png)

1. Кликните на икону Алати и требало би да видите листу алата као на слици:

    ![Алати](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/select-tools-visual-studio-code.png)

1. Унесите упит у разговор да позовете алат. На пример, ако сте изабрали алат за информације о наруџбини, можете питати агента о наруџбини. Ево примера упита:

    ```text
    get information from order 2
    ```

    Сада ће вам се приказати икона алата која вас пита да ли желите да наставите са позивом алата. Изаберите да наставите, требало би да видите резултат као на слици:

    ![Резултат упита](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/chat-results-visual-studio-code.png)

    **оно што видите горе зависи од алата које сте поставили, али идеја је да добијете текстуални одговор попут овог**


## Референце

Ево како можете сазнати више:

- [Туторијал о Azure API Management и MCP](https://learn.microsoft.com/en-us/azure/api-management/export-rest-mcp-server)
- [Python пример: Сигурни удаљени MCP сервери користећи Azure API Management (експериментално)](https://github.com/Azure-Samples/remote-mcp-apim-functions-python)

- [MCP лабораторија ауторизације клијента](https://github.com/Azure-Samples/AI-Gateway/tree/main/labs/mcp-client-authorization)

- [Користите Azure API Management екстензију за VS Code за увоз и управљање API-јима](https://learn.microsoft.com/en-us/azure/api-management/visual-studio-code-tutorial)

- [Региструјте и откривајте удаљене MCP сервере у Azure API Center](https://learn.microsoft.com/en-us/azure/api-center/register-discover-mcp-server)
- [AI Gateway](https://github.com/Azure-Samples/AI-Gateway) Одличан репозиторијум који приказује многе AI могућности са Azure API Management
- [AI Gateway радионице](https://azure-samples.github.io/AI-Gateway/) Садржи радионице које користе Azure портал, што је сјајан начин да започнете процену AI могућности.

## Шта следи

- Назад на: [Преглед студија случаја](./README.md)
- Следеће: [Azure AI Travel Agents](./travelagentsample.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Изјава о одрицању одговорности**:
Овај документ је преведен коришћењем услуге за аутоматски превод [Co-op Translator](https://github.com/Azure/co-op-translator). Иако тежимо тачности, имајте у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати ауторитативним извором. За критичне информације препоручује се професионални људски превод. Нисмо одговорни за било каква неспоразума или погрешна тумачења која произилазе из коришћења овог превода.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->