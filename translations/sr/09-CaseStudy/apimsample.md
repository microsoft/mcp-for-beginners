# Студија случаја: Изложите REST API у API Management као MCP сервер

Azure API Management је услуга која пружа Gateway изнад ваших API крајњих тачака. Како функционише је да Azure API Management делује као прокси испред ваших API-ја и може одлучити шта ће радити са долазним захтевима.

Коришћењем овога, добијате читав низ могућности као што су:

- **Безбедност**, можете користити све од API кључева, JWT до управљаног идентитета.
- **Ограничење фреквенције позива (Rate limiting)**, одлична функција која вам омогућава да одлучите колико позива може проћи у једном одређеном временском јединицу. Ово помаже да сваки корисник има сјајно искуство као и да ваш сервис не буде преплављен захтевима.
- **Скалирање и баланс оптерећења**. Можете поставити више крајњих тачака за раздвајање оптерећења и можете одлучити како да "балансирате оптерећење".
- **AI функције као што су семантичко кеширање**, лимити токена и праћење токена и друго. Ово су одличне функције које побољшавају одзив система као и помажу да држите контролу над трошковима токена. [Прочитајте више овде](https://learn.microsoft.com/en-us/azure/api-management/genai-gateway-capabilities).

## Зашто MCP + Azure API Management?

Model Context Protocol брзо постаје стандард за агентске AI апликације и начин да се алати и подаци изложе на конзистентан начин. Azure API Management је природан избор када треба да "управљате" API-јима. MCP сервери често интегришу друге API-је како би, на пример, решили захтеве ка неком алату. Стога комбинација Azure API Management и MCP има много смисла.

## Преглед

У овом конкретном случају ћемо научити како да изложимо API крајње тачке као MCP сервер. На овај начин можемо лако укључити ове крајње тачке у агентску апликацију и искористити све могућности Azure API Management.

## Кључне функције

- Изаберете које методе крајњих тачака желите да изложите као алате.
- Додатне функције које добијате зависе од конфигурације у одељку политика за ваш API. Али овде ћемо вам показати како да додате ограничење фреквенције позива.

## Претходни корак: увоз API-ја

Ако већ имате API у Azure API Management, одлично, тада можете прескочити овај корак. Ако не, погледајте овај линк, [увоз API-ја у Azure API Management](https://learn.microsoft.com/en-us/azure/api-management/import-and-publish#import-and-publish-a-backend-api).

## Изложите API као MCP сервер

Да бисмо изложили API крајње тачке, пратимо следеће кораке:

1. Идите на Azure портал на адресу <https://portal.azure.com/?Microsoft_Azure_ApiManagement=mcp>
Идите на вашу инстанцу API Management-а.

1. У левом менију, изаберите APIs > MCP Servers > + Креирај нови MCP сервер.

1. У API-ју изаберите REST API који желите изложити као MCP сервер.

1. Изаберите једну или више API операција које желите изложити као алате. Можете изабрати све операције или само специфичне.

    ![Изаберите методе за изложити](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/create-mcp-server-small.png)


1. Изаберите **Create (Креирај)**.

1. Идите на мени опцију **APIs** и **MCP Servers**, требало би да видите следеће:

    ![Погледајте MCP сервер у главном прозору](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-list.png)

    MCP сервер је креиран и API операције су изложене као алати. MCP сервер је наведен у панелу MCP Servers. Колона URL приказује крајњу тачку MCP сервера коју можете позивати за тестирање или унутар клијентске апликације.

## Опционо: Конфигуришите политике

Azure API Management има основни концепт политика где постављате различита правила за ваше крајње тачке као што су ограничење позива или семантичко кеширање. Ове политике се пишу у XML формату.

Ево како можете поставити политику за ограничење броја позива за MCP сервер:

1. У порталу, под APIs, изаберите **MCP Servers**.

1. Изаберите MCP сервер који сте креирали.

1. У левом менију, под MCP, изаберите **Policies (Политике)**.

1. У уреднику политика додајте или измените политике које желите применити на алате MCP сервера. Политике су дефинисане у XML формату. На пример, можете додати политику која ограничава број позива на алате MCP сервера (у овом примеру, 5 позива на 30 секунди по IP адреси клијента). Ево XML кода који то реализује:

    ```xml
     <rate-limit-by-key calls="5" 
       renewal-period="30" 
       counter-key="@(context.Request.IpAddress)" 
       remaining-calls-variable-name="remainingCallsPerIP" 
    />
    ```

    Ево слике уредника политика:

    ![Уредник политика](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-policies-small.png)
 
## Испробајте

Хајде да проверимо да MCP сервер ради како је предвиђено.

> [!NOTE]
> Azure API Management тренутно изложује овај сервер преко Streamable
> HTTP `/mcp` крајње тачке. Старији HTTP+SSE `/sse` пренос је застарео и
> треба га користити само са наследним клијентима.

За ово ћемо користити Visual Studio Code и GitHub Copilot и његов Agent режим. Додаћемо MCP сервер у фајл *mcp.json*. На овај начин Visual Studio Code ће деловати као клијент са агентским могућностима, а крајњим корисницима ће бити омогућено да унесу упит (prompt) и интерагују са тим сервером.

Хајде да видимо како да додамо MCP сервер у Visual Studio Code:

1. Користите команду MCP: **Add Server из Command Palette-а**.

1. Када затраже, изаберите тип сервера: **HTTP (HTTP или Server Sent Events)**.

1. Унесите Streamable HTTP URL који је приказан за MCP сервер у API Management.
    На пример:
    `https://<apim-service-name>.azure-api.net/<api-name>-mcp/mcp`.

1. Унесите ID сервера по вашем избору. Ово није критична вредност али ће вам помоћи да се сетите која је ово инстанца сервера.

1. Изаберите да ли желите да сачувате конфигурацију у подешавањима радног простора или корисничким подешавањима.

  - **Подешавања радног простора** - конфигурација сервера ће бити сачувана у .vscode/mcp.json фајлу који је доступан само у тренутном радном простору.

    *mcp.json*

    ```json
    "servers": {
        "APIM petstore" : {
            "type": "http",
            "url": "url-to-mcp-server/mcp"
        }
    }
    ```

  - **Корисничка подешавања** - конфигурација сервера ће бити додата у глобални *settings.json* фајл и доступна у свим радним просторима. Конфигурација изгледа слично следећем:

    ![Корисничка подешавања](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-servers-visual-studio-code.png)

1. Такође морате додати конфигурацију, хедер да бисте осигурали правилну аутентификацију према Azure API Management. Користи се хедер зван **Ocp-Apim-Subscription-Key**.

    - Ево како можете додати овај хедер у подешавања:

    ![Додавање хедера за аутентификацију](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-with-header-visual-studio-code.png), овде ће се појавити упит за унос API кључа који можете пронаћи у Azure порталу за вашу инстанцу Azure API Management-а.

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

### Користите Agent режим

Сада смо све подесили или у подешавањима или у *.vscode/mcp.json*. Хајде да пробамо.

Требало би да постоји иконица алата као овде, где су наведени изложени алати са вашег сервера:

![Алатке са сервера](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/tools-button-visual-studio-code.png)

1. Кликните на иконицу алата и требало би да видите листу алата као што је приказано:

    ![Алатке](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/select-tools-visual-studio-code.png)

1. Унесите упит у чет да позовете алат. На пример, ако сте изабрали алат за добијање информација о наруџбини, можете питати агента о наруџбини. Ево примера упита:

    ```text
    get information from order 2
    ```

    Сада ће вам се приказати иконица алата која тражи да наставите позив алата. Изаберите да наставите извршавање алата, сада бисте требали видети излаз као овде:

    ![Резултат упита](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/chat-results-visual-studio-code.png)

    **оно што видите горе зависи од тога које сте алате подесили, али идеја је да добијете текстуални одговор као горе**


## Референце

Ево како можете сазнати више:

- [Туторијал о Azure API Management и MCP](https://learn.microsoft.com/en-us/azure/api-management/export-rest-mcp-server)
- [Python пример: Безбедни удаљени MCP сервери користећи Azure API Management (експериментално)](https://github.com/Azure-Samples/remote-mcp-apim-functions-python)

- [Лабораторија за ауторизацију MCP клијената](https://github.com/Azure-Samples/AI-Gateway/tree/main/labs/mcp-client-authorization)

- [Користите Azure API Management екстензију за VS Code за увоз и управљање API-јима](https://learn.microsoft.com/en-us/azure/api-management/visual-studio-code-tutorial)

- [Региструјте и откријавајте удаљене MCP сервере у Azure API Center-у](https://learn.microsoft.com/en-us/azure/api-center/register-discover-mcp-server)
- [AI Gateway](https://github.com/Azure-Samples/AI-Gateway) Одличан репозиторјум који показује многе AI могућности са Azure API Management
- [AI Gateway радионице](https://azure-samples.github.io/AI-Gateway/)  Садржи радионице користећи Azure портал, што је одличан начин да почнете са проценом AI могућности.

## Шта следи

- Назад на: [Преглед студија случаја](./README.md)
- Следеће: [Azure AI агенти за путовања](./travelagentsample.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Изјава о одрицању одговорности**:
Овај документ је преведен коришћењем услуге за аутоматски превод [Co-op Translator](https://github.com/Azure/co-op-translator). Иако тежимо тачности, имајте у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати ауторитативним извором. За критичне информације препоручује се професионални људски превод. Нисмо одговорни за било каква неспоразума или погрешна тумачења која произилазе из коришћења овог превода.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->