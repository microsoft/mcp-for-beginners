# Кейс: Відкриття REST API в Azure API Management як сервера MCP

Azure API Management — це сервіс, який забезпечує шлюз поверх ваших API точок доступу. Він працює як проксі перед вашими API і може вирішувати, що робити із вхідними запитами.

Використовуючи його, ви додаєте безліч функцій, таких як:

- **Безпека**, можна використовувати все від API ключів, JWT до керованої ідентичності.
- **Обмеження частоти запитів (rate limiting)**, чудова функція, що дозволяє визначати, скільки викликів допускається за певний проміжок часу. Це допомагає забезпечити якісний досвід для всіх користувачів і захищає сервіс від перевантаження запитами.
- **Масштабування та балансування навантаження**. Можна налаштувати кілька кінцевих точок для розподілу навантаження, а також обрати спосіб балансування.
- **AI-функції, такі як семантичне кешування**, обмеження токенів, моніторинг токенів та інші. Ці функції покращують швидкість відгуку та допомагають контролювати використання токенів. [Детальніше тут](https://learn.microsoft.com/en-us/azure/api-management/genai-gateway-capabilities). 

## Чому MCP + Azure API Management?

Model Context Protocol швидко стає стандартом для агентних AI-додатків і способів послідовного відкриття інструментів та даних. Azure API Management — природний вибір, коли потрібно "керувати" API. Сервери MCP часто інтегруються з іншими API, щоб вирішувати запити до інструментів, наприклад. Тому поєднання Azure API Management та MCP має сенс.

## Огляд

У цьому конкретному кейсі ми навчимось відкривати API кінцеві точки як сервер MCP. Це дозволить легко робити ці кінцеві точки частиною агентного додатку, при цьому використовуючи функції Azure API Management.

## Ключові особливості

- Ви вибираєте методи кінцевої точки, які хочете відкрити як інструменти.
- Додаткові функції залежать від того, що ви налаштовуєте у секції політик для вашого API. Тут ми покажемо, як можна додати обмеження частоти викликів.

## Попередній крок: імпорт API

Якщо у вас уже є API в Azure API Management — чудово, можете пропустити цей крок. Якщо ні, ознайомтеся з цією інструкцією: [імпорт API в Azure API Management](https://learn.microsoft.com/en-us/azure/api-management/import-and-publish#import-and-publish-a-backend-api).

## Відкриття API як MCP сервера

Щоб відкрити кінцеві точки API, виконайте такі кроки:

1. Перейдіть до Azure Portal за адресою <https://portal.azure.com/?Microsoft_Azure_ApiManagement=mcp> 
Перейдіть до вашого екземпляру API Management.

1. У лівому меню виберіть APIs > MCP Servers > + Create new MCP Server.

1. В полі API оберіть REST API, який потрібно відкрити як MCP сервер.

1. Виберіть одну або кілька операцій API для відкриття як інструменти. Можна вибрати всі операції або лише певні.

    ![Select methods to expose](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/create-mcp-server-small.png)


1. Натисніть **Create**.

1. Перейдіть у меню **APIs** та **MCP Servers**, ви повинні побачити наступне:

    ![See the MCP Server in the main pane](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-list.png)

    MCP сервер створено, операції API відкрито як інструменти. MCP сервер перелічено в панелі MCP Servers. У стовпці URL показано кінцеву точку MCP сервера, яку можна викликати для тестування або в клієнтському додатку.

## Додатково: Налаштування політик

Azure API Management базується на концепції політик, де ви встановлюєте різні правила для ваших кінцевих точок, наприклад обмеження частоти викликів або семантичне кешування. Ці політики задаються у форматі XML.

Ось як можна налаштувати політику для обмеження частоти викликів MCP сервера:

1. У порталі, в розділі APIs, виберіть **MCP Servers**.

1. Оберіть створений MCP сервер.

1. У лівому меню, в розділі MCP, виберіть **Policies**.

1. У редакторі політик додайте або відредагуйте політики, які потрібно застосувати до інструментів MCP сервера. Політики пишуться у XML форматі. Наприклад, можна додати політику, що обмежуватиме виклики інструментів MCP сервера (в цьому прикладі 5 викликів за 30 секунд на IP клієнта). Ось XML, що реалізує обмеження:

    ```xml
     <rate-limit-by-key calls="5" 
       renewal-period="30" 
       counter-key="@(context.Request.IpAddress)" 
       remaining-calls-variable-name="remainingCallsPerIP" 
    />
    ```

    Ось зображення редактора політик:

    ![Policy editor](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-policies-small.png)
 
## Спробуйте

Переконаємося, що наш MCP сервер працює як задумано.

> [!NOTE]
> Наразі Azure API Management відкриває сервер через потокову
> HTTP `/mcp` кінцеву точку. Старий HTTP+SSE `/sse` транспорт застарів і
> має використовуватися лише з застарілими клієнтами.

Для цього ми використаємо Visual Studio Code та GitHub Copilot в режимі агента. Ми додамо MCP сервер у *mcp.json*. Таким чином Visual Studio Code діятиме як клієнт з агентними можливостями, а користувачі зможуть вводити запити і взаємодіяти з цим сервером.

Переглянемо, як додати MCP сервер у Visual Studio Code:

1. Використайте команду MCP: **Add Server** з Command Palette.

1. Коли буде запропоновано, оберіть тип сервера: **HTTP (HTTP або Server Sent Events)**.

1. Введіть URL потокового HTTP для MCP сервера, показаний у Azure API Management.
    Наприклад:
    `https://<apim-service-name>.azure-api.net/<api-name>-mcp/mcp`.

1. Введіть ID сервера на ваш вибір. Це не дуже важливе значення, але допоможе вам запам’ятати, що це за сервер.

1. Виберіть, чи зберегти конфігурацію у налаштуваннях робочого простору, чи у налаштуваннях користувача.

  - **Налаштування робочого простору** — конфігурація сервера зберігається у файлі .vscode/mcp.json, доступному лише у цьому робочому просторі.

    *mcp.json*

    ```json
    "servers": {
        "APIM petstore" : {
            "type": "http",
            "url": "url-to-mcp-server/mcp"
        }
    }
    ```

  - **Налаштування користувача** — конфігурація сервера додається у ваш глобальний файл *settings.json* і доступна у всіх робочих просторах. Конфігурація виглядає приблизно так:

    ![User setting](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-servers-visual-studio-code.png)

1. Також потрібно додати в конфігурацію заголовок для правильної автентифікації з Azure API Management. Для цього використовується заголовок під назвою **Ocp-Apim-Subscription-Key**. 

    - Ось як можна додати його у налаштування:

    ![Adding header for authentication](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-with-header-visual-studio-code.png), це викликає запит на введення значення API ключа, який можна знайти у порталі Azure для вашого екземпляра Azure API Management.

   - Щоб додати його у *mcp.json*, можна зробити так:

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

### Використання режиму агента

Тепер все налаштовано у файлі налаштувань або в *.vscode/mcp.json*. Спробуймо.

Поряд має бути іконка Інструменти, де перераховані відкриті інструменти з вашого сервера:

![Tools from the server](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/tools-button-visual-studio-code.png)

1. Клікніть на іконку інструментів, і повинні побачити список інструментів наступним чином:

    ![Tools](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/select-tools-visual-studio-code.png)

1. Введіть запит у чаті, щоб викликати інструмент. Наприклад, якщо ви вибрали інструмент для отримання інформації про замовлення, ви можете запитати агента про замовлення. Ось приклад запиту:

    ```text
    get information from order 2
    ```

    Тепер ви побачите іконку інструментів із запитом підтвердити виклик інструменту. Оберіть продовжити, і ви побачите результат, приблизно так:

    ![Result from prompt](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/chat-results-visual-studio-code.png)

    **Що ви бачите вище, залежить від того, які інструменти ви налаштували, але суть в тому, що ви отримуєте текстову відповідь, як показано**


## Посилання

Ось як можна дізнатись більше:

- [Підручник з Azure API Management та MCP](https://learn.microsoft.com/en-us/azure/api-management/export-rest-mcp-server)
- [Приклад на Python: Безпечні віддалені MCP сервери з Azure API Management (експериментально)](https://github.com/Azure-Samples/remote-mcp-apim-functions-python)

- [Лабораторна робота з авторизації MCP клієнта](https://github.com/Azure-Samples/AI-Gateway/tree/main/labs/mcp-client-authorization)

- [Використання розширення Azure API Management для VS Code для імпорту та керування API](https://learn.microsoft.com/en-us/azure/api-management/visual-studio-code-tutorial)

- [Реєстрація та пошук віддалених MCP серверів у Azure API Center](https://learn.microsoft.com/en-us/azure/api-center/register-discover-mcp-server)
- [AI Gateway](https://github.com/Azure-Samples/AI-Gateway) Відмінний репозиторій з багатьма AI можливостями на базі Azure API Management
- [Майстер-класи AI Gateway](https://azure-samples.github.io/AI-Gateway/) Містить майстер-класи з використання Azure Portal — чудовий спосіб почати оцінювати AI можливості.

## Що далі

- Повернутися до: [Огляд кейсів](./README.md)
- Наступний: [Azure AI Travel Agents](./travelagentsample.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Відмова від відповідальності**:
Цей документ було перекладено за допомогою сервісу штучного інтелекту для перекладу [Co-op Translator](https://github.com/Azure/co-op-translator). Хоча ми прагнемо до точності, будь ласка, майте на увазі, що автоматичні переклади можуть містити помилки або неточності. Оригінальний документ рідною мовою слід вважати авторитетним джерелом. Для критично важливої інформації рекомендується професійний людський переклад. Ми не несемо відповідальності за будь-які непорозуміння або неправильні тлумачення, що виникли внаслідок використання цього перекладу.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->