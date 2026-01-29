# Дослідження: Відкриття REST API в API Management як сервер MCP

Azure API Management — це сервіс, який надає шлюз для ваших API-ендпоінтів. Він працює як проксі перед вашими API і може вирішувати, що робити з вхідними запитами.

Використовуючи його, ви отримуєте цілий набір функцій, таких як:

- **Безпека**: можна використовувати все — від API-ключів і JWT до керованої ідентичності.
- **Обмеження швидкості**: чудова функція, яка дозволяє визначити, скільки викликів може пройти за певний проміжок часу. Це допомагає забезпечити гарний досвід для всіх користувачів і запобігти перевантаженню вашого сервісу.
- **Масштабування та балансування навантаження**: можна налаштувати кілька ендпоінтів для розподілу навантаження і визначити, як саме це робити.
- **AI-функції, такі як семантичне кешування**, обмеження токенів, моніторинг токенів тощо. Ці функції покращують швидкість відповіді та допомагають контролювати витрати токенів. [Дізнайтеся більше тут](https://learn.microsoft.com/en-us/azure/api-management/genai-gateway-capabilities).

## Чому MCP + Azure API Management?

Model Context Protocol швидко стає стандартом для агентних AI-додатків і способу відкриття інструментів та даних у послідовний спосіб. Azure API Management є природним вибором, коли потрібно "керувати" API. MCP-сервери часто інтегруються з іншими API для обробки запитів до інструментів, наприклад. Тому поєднання Azure API Management і MCP має багато сенсу.

## Огляд

У цьому конкретному випадку ми навчимося відкривати API-ендпоінти як сервер MCP. Це дозволить легко зробити ці ендпоінти частиною агентного додатка, використовуючи при цьому функції Azure API Management.

## Основні функції

- Ви обираєте методи ендпоінтів, які хочете відкрити як інструменти.
- Додаткові функції залежать від того, що ви налаштуєте в політиках для вашого API. Тут ми покажемо, як додати обмеження швидкості.

## Попередній крок: імпорт API

Якщо у вас вже є API в Azure API Management, чудово, тоді цей крок можна пропустити. Якщо ні, перегляньте це посилання: [імпорт API в Azure API Management](https://learn.microsoft.com/en-us/azure/api-management/import-and-publish#import-and-publish-a-backend-api).

## Відкриття API як сервер MCP

Щоб відкрити API-ендпоінти, виконайте наступні кроки:

1. Перейдіть до Azure Portal за адресою <https://portal.azure.com/?Microsoft_Azure_ApiManagement=mcp>.  
   Перейдіть до вашого екземпляра API Management.

1. У лівому меню виберіть **APIs > MCP Servers > + Create new MCP Server**.

1. У полі API виберіть REST API, який потрібно відкрити як сервер MCP.

1. Виберіть одну або кілька операцій API, які потрібно відкрити як інструменти. Ви можете вибрати всі операції або лише конкретні.

    ![Вибір методів для відкриття](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/create-mcp-server-small.png)

1. Натисніть **Create**.

1. Перейдіть до меню **APIs** і **MCP Servers**, ви побачите наступне:

    ![Список серверів MCP](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-list.png)

    Сервер MCP створено, і операції API відкрито як інструменти. Сервер MCP відображається в панелі MCP Servers. У колонці URL показано ендпоінт сервера MCP, який можна викликати для тестування або в клієнтському додатку.

## Додатково: Налаштування політик

Azure API Management має основну концепцію політик, де ви можете налаштувати різні правила для ваших ендпоінтів, наприклад, обмеження швидкості або семантичне кешування. Ці політики створюються у форматі XML.

Ось як можна налаштувати політику для обмеження швидкості вашого сервера MCP:

1. У порталі, у розділі APIs, виберіть **MCP Servers**.

1. Виберіть створений сервер MCP.

1. У лівому меню, у розділі MCP, виберіть **Policies**.

1. У редакторі політик додайте або змініть політики, які ви хочете застосувати до інструментів сервера MCP. Політики визначаються у форматі XML. Наприклад, можна додати політику для обмеження викликів до інструментів сервера MCP (у цьому прикладі — 5 викликів за 30 секунд на одну IP-адресу клієнта). Ось XML, який встановлює обмеження швидкості:

    ```xml
     <rate-limit-by-key calls="5" 
       renewal-period="30" 
       counter-key="@(context.Request.IpAddress)" 
       remaining-calls-variable-name="remainingCallsPerIP" 
    />
    ```

    Ось зображення редактора політик:

    ![Редактор політик](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-policies-small.png)

## Перевірка роботи

Переконаймося, що наш сервер MCP працює належним чином.

Для цього ми використаємо Visual Studio Code, GitHub Copilot і його режим Agent. Ми додамо сервер MCP до файлу *mcp.json*. Таким чином, Visual Studio Code буде діяти як клієнт із агентними можливостями, і кінцеві користувачі зможуть вводити запити та взаємодіяти з сервером.

Ось як додати сервер MCP у Visual Studio Code:

1. Використовуйте команду **MCP: Add Server** з Command Palette.

1. Коли з'явиться запит, виберіть тип сервера: **HTTP (HTTP or Server Sent Events)**.

1. Введіть URL сервера MCP в API Management. Наприклад: **https://<apim-service-name>.azure-api.net/<api-name>-mcp/sse** (для SSE-ендпоінта) або **https://<apim-service-name>.azure-api.net/<api-name>-mcp/mcp** (для MCP-ендпоінта). Зверніть увагу на різницю між транспортами: `/sse` або `/mcp`.

1. Введіть ідентифікатор сервера на ваш вибір. Це неважливе значення, але воно допоможе вам запам'ятати, що це за екземпляр сервера.

1. Виберіть, чи зберігати конфігурацію у налаштуваннях робочого простору чи користувача.

  - **Налаштування робочого простору** — конфігурація сервера зберігається у файлі .vscode/mcp.json, доступному лише в поточному робочому просторі.

    *mcp.json*

    ```json
    "servers": {
        "APIM petstore" : {
            "type": "sse",
            "url": "url-to-mcp-server/sse"
        }
    }
    ```

    або якщо ви обрали потоковий HTTP як транспорт, це буде трохи інакше:

    ```json
    "servers": {
        "APIM petstore" : {
            "type": "http",
            "url": "url-to-mcp-server/mcp"
        }
    }
    ```

  - **Налаштування користувача** — конфігурація сервера додається до вашого глобального файлу *settings.json* і доступна у всіх робочих просторах. Конфігурація виглядає приблизно так:

    ![Налаштування користувача](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-servers-visual-studio-code.png)

1. Вам також потрібно додати конфігурацію, заголовок для автентифікації з Azure API Management. Використовується заголовок **Ocp-Apim-Subscription-Key**.

    - Ось як додати його до налаштувань:

    ![Додавання заголовка для автентифікації](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-with-header-visual-studio-code.png). Це викличе запит на введення значення API-ключа, яке можна знайти в Azure Portal для вашого екземпляра Azure API Management.

   - Щоб додати його до *mcp.json*, зробіть це так:

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

### Використання режиму Agent

Тепер ми все налаштували у налаштуваннях або у *.vscode/mcp.json*. Спробуймо це.

Повинен з'явитися значок інструментів, де будуть відображені інструменти, відкриті вашим сервером:

![Інструменти сервера](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/tools-button-visual-studio-code.png)

1. Натисніть на значок інструментів, і ви побачите список інструментів:

    ![Список інструментів](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/select-tools-visual-studio-code.png)

1. Введіть запит у чаті, щоб викликати інструмент. Наприклад, якщо ви обрали інструмент для отримання інформації про замовлення, ви можете запитати агента про замовлення. Ось приклад запиту:

    ```text
    get information from order 2
    ```

    Тепер з'явиться значок інструментів із запитом продовжити виклик інструмента. Виберіть продовжити виконання інструмента, і ви побачите результат, наприклад:

    ![Результат запиту](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/chat-results-visual-studio-code.png)

    **Те, що ви бачите, залежить від налаштованих інструментів, але ідея полягає в тому, що ви отримуєте текстову відповідь, як показано вище.**

## Посилання

Ось де можна дізнатися більше:

- [Підручник з Azure API Management і MCP](https://learn.microsoft.com/en-us/azure/api-management/export-rest-mcp-server)
- [Приклад на Python: Захист віддалених серверів MCP за допомогою Azure API Management (експериментальний)](https://github.com/Azure-Samples/remote-mcp-apim-functions-python)

- [Лабораторія авторизації клієнтів MCP](https://github.com/Azure-Samples/AI-Gateway/tree/main/labs/mcp-client-authorization)

- [Використання розширення Azure API Management для VS Code для імпорту та управління API](https://learn.microsoft.com/en-us/azure/api-management/visual-studio-code-tutorial)

- [Реєстрація та виявлення віддалених серверів MCP в Azure API Center](https://learn.microsoft.com/en-us/azure/api-center/register-discover-mcp-server)
- [AI Gateway](https://github.com/Azure-Samples/AI-Gateway) — чудовий репозиторій, що демонструє багато AI-можливостей з Azure API Management.
- [Майстер-класи AI Gateway](https://azure-samples.github.io/AI-Gateway/) — містять майстер-класи з використанням Azure Portal, що є чудовим способом почати оцінку AI-можливостей.

**Відмова від відповідальності**:  
Цей документ було перекладено за допомогою сервісу автоматичного перекладу [Co-op Translator](https://github.com/Azure/co-op-translator). Хоча ми прагнемо до точності, звертаємо вашу увагу, що автоматичні переклади можуть містити помилки або неточності. Оригінальний документ на його рідній мові слід вважати авторитетним джерелом. Для критично важливої інформації рекомендується професійний людський переклад. Ми не несемо відповідальності за будь-які непорозуміння або неправильні тлумачення, що виникли внаслідок використання цього перекладу.