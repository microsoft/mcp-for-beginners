# Протокол за контекст на модела (MCP) за начинаещи - Ръководство за обучение

Това ръководство предоставя общ преглед на структурата и съдържанието на хранилището за учебната програма "Протокол за контекст на модела (MCP) за начинаещи". Използвайте това ръководство, за да навигирате ефективно в хранилището и да се възползвате максимално от наличните ресурси.

## Преглед на хранилището

Протоколът за контекст на модела (MCP) е стандартизирана рамка за взаимодействие между AI модели и клиентски приложения. Първоначално създаден от Anthropic, MCP сега се поддържа от по-широката MCP общност чрез официалната GitHub организация. Това хранилище предоставя цялостна учебна програма с практически примери за код на C#, Java, JavaScript, Python и TypeScript, предназначена за AI разработчици, системни архитекти и софтуерни инженери.

## Визуална карта на учебната програма

```mermaid
mindmap
  root((MCP for Beginners))
    00. Introduction
      ::icon(fa fa-book)
      (Protocol Overview)
      (Standardization Benefits)
      (Real-world Use Cases)
      (AI Integration Fundamentals)
    01. Core Concepts
      ::icon(fa fa-puzzle-piece)
      (Client-Server Architecture)
      (Protocol Components)
      (Messaging Patterns)
      (Transport Mechanisms)
    02. Security
      ::icon(fa fa-shield)
      (AI-Specific Threats)
      (Best Practices 2025)
      (Azure Content Safety)
      (Auth & Authorization)
      (Microsoft Prompt Shields)
    03. Getting Started
      ::icon(fa fa-rocket)
      (First Server Implementation)
      (Client Development)
      (LLM Client Integration)
      (VS Code Extensions)
      (SSE Server Setup)
      (HTTP Streaming)
      (AI Toolkit Integration)
      (Testing Frameworks)
      (Advanced Server Usage)
      (Simple Auth)
      (Deployment Strategies)
    04. Practical Implementation
      ::icon(fa fa-code)
      (Multi-Language SDKs)
      (Testing & Debugging)
      (Prompt Templates)
      (Sample Projects)
      (Production Patterns)
    05. Advanced Topics
      ::icon(fa fa-graduation-cap)
      (Context Engineering)
      (Foundry Agent Integration)
      (Multi-modal AI Workflows)
      (OAuth2 Authentication)
      (Real-time Search)
      (Streaming Protocols)
      (Root Contexts)
      (Routing Strategies)
      (Sampling Techniques)
      (Scaling Solutions)
      (Security Hardening)
      (Entra ID Integration)
      (Web Search MCP)
      
    06. Community
      ::icon(fa fa-users)
      (Code Contributions)
      (Documentation)
      (MCP Client Ecosystem)
      (MCP Server Registry)
      (Image Generation Tools)
      (GitHub Collaboration)
    07. Early Adoption
      ::icon(fa fa-lightbulb)
      (Production Deployments)
      (Microsoft MCP Servers)
      (Azure MCP Service)
      (Enterprise Case Studies)
      (Future Roadmap)
    08. Best Practices
      ::icon(fa fa-check)
      (Performance Optimization)
      (Fault Tolerance)
      (System Resilience)
      (Monitoring & Observability)
    09. Case Studies
      ::icon(fa fa-file-text)
      (Azure API Management)
      (AI Travel Agent)
      (Azure DevOps Integration)
      (Documentation MCP)
      (GitHub MCP Registry)
      (VS Code Integration)
      (Real-world Implementations)
    10. Hands-on Workshop
      ::icon(fa fa-laptop)
      (MCP Server Fundamentals)
      (Advanced Development)
      (AI Toolkit Integration)
      (Production Deployment)
      (4-Lab Structure)
    11. Database Integration Labs
      ::icon(fa fa-database)
      (PostgreSQL Integration)
      (Retail Analytics Use Case)
      (Row Level Security)
      (Semantic Search)
      (Production Deployment)
      (13-Lab Structure)
      (Hands-on Learning)
```

## Структура на хранилището

Хранилището е организирано в единадесет основни секции, всяка от които се фокусира върху различни аспекти на MCP:

1. **Въведение (00-Introduction/)**
   - Преглед на протокола за контекст на модела
   - Защо стандартизацията е важна в AI процесите
   - Практически приложения и ползи

2. **Основни концепции (01-CoreConcepts/)**
   - Архитектура клиент-сървър
   - Основни компоненти на протокола
   - Модели на съобщения в MCP

3. **Сигурност (02-Security/)**
   - Заплахи за сигурността в системи, базирани на MCP
   - Най-добри практики за осигуряване на имплементации
   - Стратегии за автентикация и авторизация
   - **Подробна документация за сигурност**:
     - Най-добри практики за сигурност на MCP 2025
     - Ръководство за имплементация на Azure Content Safety
     - Контроли и техники за сигурност на MCP
     - Бърз справочник за най-добри практики на MCP
   - **Ключови теми за сигурност**:
     - Атаки чрез инжектиране на подсказки и отравяне на инструменти
     - Отвличане на сесии и проблеми с объркания заместник
     - Уязвимости при предаване на токени
     - Прекомерни разрешения и контрол на достъпа
     - Сигурност на веригата за доставки за AI компоненти
     - Интеграция на Microsoft Prompt Shields

4. **Първи стъпки (03-GettingStarted/)**
   - Настройка и конфигурация на средата
   - Създаване на основни MCP сървъри и клиенти
   - Интеграция със съществуващи приложения
   - Включва секции за:
     - Първа имплементация на сървър
     - Разработка на клиент
     - Интеграция на LLM клиент
     - Интеграция с VS Code
     - Сървър за събития, изпратени от сървъра (SSE)
     - Разширено използване на сървъра
     - HTTP стрийминг
     - Интеграция на AI Toolkit
     - Стратегии за тестване
     - Насоки за внедряване

5. **Практическа имплементация (04-PracticalImplementation/)**
   - Използване на SDKs за различни програмни езици
   - Техники за дебъгване, тестване и валидиране
   - Създаване на повторно използваеми шаблони за подсказки и работни потоци
   - Примерни проекти с имплементационни примери

6. **Разширени теми (05-AdvancedTopics/)**
   - Техники за инженеринг на контекст
   - Интеграция на Foundry агент
   - Мултимодални AI работни потоци
   - Демонстрации за автентикация с OAuth2
   - Възможности за търсене в реално време
   - Стрийминг в реално време
   - Имплементация на основни контексти
   - Стратегии за маршрутизация
   - Техники за семплиране
   - Подходи за мащабиране
   - Съображения за сигурност
   - Интеграция на Entra ID сигурност
   - Интеграция на уеб търсене

7. **Приноси от общността (06-CommunityContributions/)**
   - Как да допринесете с код и документация
   - Сътрудничество чрез GitHub
   - Подобрения и обратна връзка, водени от общността
   - Използване на различни MCP клиенти (Claude Desktop, Cline, VSCode)
   - Работа с популярни MCP сървъри, включително генериране на изображения

8. **Уроци от ранното внедряване (07-LessonsfromEarlyAdoption/)**
   - Реални имплементации и успешни истории
   - Създаване и внедряване на решения, базирани на MCP
   - Тенденции и бъдеща пътна карта
   - **Ръководство за Microsoft MCP сървъри**: Подробно ръководство за 10 готови за производство Microsoft MCP сървъри, включително:
     - Microsoft Learn Docs MCP Server
     - Azure MCP Server (15+ специализирани конектори)
     - GitHub MCP Server
     - Azure DevOps MCP Server
     - MarkItDown MCP Server
     - SQL Server MCP Server
     - Playwright MCP Server
     - Dev Box MCP Server
     - Azure AI Foundry MCP Server
     - Microsoft 365 Agents Toolkit MCP Server

9. **Най-добри практики (08-BestPractices/)**
   - Настройка и оптимизация на производителността
   - Проектиране на устойчиви MCP системи
   - Стратегии за тестване и устойчивост

10. **Казуси (09-CaseStudy/)**
    - **Седем подробни казуса**, демонстриращи гъвкавостта на MCP в различни сценарии:
    - **Azure AI Travel Agents**: Оркестрация на множество агенти с Azure OpenAI и AI Search
    - **Интеграция с Azure DevOps**: Автоматизиране на работни процеси с актуализации на данни от YouTube
    - **Извличане на документация в реално време**: Python конзолен клиент със стрийминг HTTP
    - **Интерактивен генератор на учебни планове**: Chainlit уеб приложение с разговорен AI
    - **Документация в редактора**: Интеграция на VS Code с GitHub Copilot работни потоци
    - **Управление на API в Azure**: Интеграция на корпоративни API с създаване на MCP сървър
    - **GitHub MCP Registry**: Развитие на екосистемата и платформа за интеграция на агенти
    - Примери за имплементация, обхващащи корпоративна интеграция, производителност на разработчиците и развитие на екосистемата

11. **Практически семинар (10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/)**
    - Цялостен практически семинар, комбиниращ MCP с AI Toolkit
    - Създаване на интелигентни приложения, свързващи AI модели с реални инструменти
    - Практически модули, обхващащи основи, разработка на персонализирани сървъри и стратегии за внедряване в производство
    - **Структура на лабораторията**:
      - Лаборатория 1: Основи на MCP сървърите
      - Лаборатория 2: Разширена разработка на MCP сървъри
      - Лаборатория 3: Интеграция на AI Toolkit
      - Лаборатория 4: Внедряване в производство и мащабиране
    - Подход за обучение, базиран на лаборатории, със стъпка по стъпка инструкции

12. **Лаборатории за интеграция на MCP сървър с база данни (11-MCPServerHandsOnLabs/)**
    - **Цялостен учебен път с 13 лаборатории** за създаване на готови за производство MCP сървъри с интеграция на PostgreSQL
    - **Имплементация на анализи за търговия на дребно в реалния свят** с използване на случая Zava Retail
    - **Модели за корпоративен клас**, включително Row Level Security (RLS), семантично търсене и достъп до данни за множество наематели
    - **Пълна структура на лабораторията**:
      - **Лаборатории 00-03: Основи** - Въведение, Архитектура, Сигурност, Настройка на средата
      - **Лаборатории 04-06: Създаване на MCP сървър** - Дизайн на база данни, Имплементация на MCP сървър, Разработка на инструменти
      - **Лаборатории 07-09: Разширени функции** - Семантично търсене, Тестване и дебъгване, Интеграция с VS Code
      - **Лаборатории 10-12: Производство и най-добри практики** - Внедряване, Мониторинг, Оптимизация
    - **Покрити технологии**: FastMCP framework, PostgreSQL, Azure OpenAI, Azure Container Apps, Application Insights
    - **Резултати от обучението**: Готови за производство MCP сървъри, модели за интеграция на база данни, анализи, базирани на AI, корпоративна сигурност

## Допълнителни ресурси

Хранилището включва поддържащи ресурси:

- **Папка с изображения**: Съдържа диаграми и илюстрации, използвани в цялата учебна програма
- **Преводи**: Поддръжка на много езици с автоматизирани преводи на документацията
- **Официални MCP ресурси**:
  - [MCP Документация](https://modelcontextprotocol.io/)
  - [MCP Спецификация](https://spec.modelcontextprotocol.io/)
  - [MCP GitHub Хранилище](https://github.com/modelcontextprotocol)

## Как да използвате това хранилище

1. **Последователно обучение**: Следвайте главите по ред (00 до 11) за структурирано обучение.
2. **Фокус върху конкретен език**: Ако се интересувате от определен програмен език, разгледайте директориите със примери за имплементации на предпочитания от вас език.
3. **Практическа имплементация**: Започнете с раздела "Първи стъпки", за да настроите вашата среда и да създадете първия си MCP сървър и клиент.
4. **Разширено изследване**: След като се почувствате уверени с основите, се потопете в разширените теми, за да разширите знанията си.
5. **Участие в общността**: Присъединете се към MCP общността чрез GitHub дискусии и Discord канали, за да се свържете с експерти и други разработчици.

## MCP клиенти и инструменти

Учебната програма обхваща различни MCP клиенти и инструменти:

1. **Официални клиенти**:
   - Visual Studio Code 
   - MCP в Visual Studio Code
   - Claude Desktop
   - Claude в VSCode 
   - Claude API

2. **Клиенти от общността**:
   - Cline (базиран на терминал)
   - Cursor (редактор на код)
   - ChatMCP
   - Windsurf

3. **Инструменти за управление на MCP**:
   - MCP CLI
   - MCP Manager
   - MCP Linker
   - MCP Router

## Популярни MCP сървъри

Хранилището представя различни MCP сървъри, включително:

1. **Официални Microsoft MCP сървъри**:
   - Microsoft Learn Docs MCP Server
   - Azure MCP Server (15+ специализирани конектори)
   - GitHub MCP Server
   - Azure DevOps MCP Server
   - MarkItDown MCP Server
   - SQL Server MCP Server
   - Playwright MCP Server
   - Dev Box MCP Server
   - Azure AI Foundry MCP Server
   - Microsoft 365 Agents Toolkit MCP Server

2. **Официални референтни сървъри**:
   - Файлова система
   - Fetch
   - Памет
   - Последователно мислене

3. **Генериране на изображения**:
   - Azure OpenAI DALL-E 3
   - Stable Diffusion WebUI
   - Replicate

4. **Инструменти за разработка**:
   - Git MCP
   - Контрол на терминала
   - Асистент за код

5. **Специализирани сървъри**:
   - Salesforce
   - Microsoft Teams
   - Jira & Confluence

## Принос

Това хранилище приветства приноси от общността. Вижте секцията "Приноси от общността" за насоки как да допринесете ефективно за екосистемата на MCP.

----

*Това ръководство за обучение беше актуализирано на 6 октомври 2025 г. и предоставя общ преглед на хранилището към тази дата. Съдържанието на хранилището може да бъде актуализирано след тази дата.*

---

**Отказ от отговорност**:  
Този документ е преведен с помощта на AI услуга за превод [Co-op Translator](https://github.com/Azure/co-op-translator). Въпреки че се стремим към точност, моля, имайте предвид, че автоматизираните преводи може да съдържат грешки или неточности. Оригиналният документ на неговия роден език трябва да се счита за авторитетен източник. За критична информация се препоръчва професионален човешки превод. Не носим отговорност за недоразумения или погрешни интерпретации, произтичащи от използването на този превод.