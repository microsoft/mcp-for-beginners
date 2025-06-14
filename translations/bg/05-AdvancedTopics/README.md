<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b1cffc51b82049ac3d5e88db0ff4a0a1",
  "translation_date": "2025-06-13T01:11:00+00:00",
  "source_file": "05-AdvancedTopics/README.md",
  "language_code": "bg"
}
-->
# Разширени теми в MCP

Тази глава е предназначена да обхване серия от разширени теми в имплементацията на Model Context Protocol (MCP), включително мултимодална интеграция, мащабируемост, добри практики за сигурност и интеграция в предприятия. Тези теми са ключови за изграждането на стабилни и готови за производство MCP приложения, които могат да отговорят на изискванията на съвременните AI системи.

## Преглед

Този урок разглежда разширени концепции в имплементацията на Model Context Protocol, със фокус върху мултимодална интеграция, мащабируемост, добри практики за сигурност и интеграция в предприятия. Тези теми са от съществено значение за създаване на MCP приложения с производствен клас, които могат да се справят със сложни изисквания в корпоративна среда.

## Учебни цели

Към края на този урок ще можете да:

- Имплементирате мултимодални възможности в MCP рамки
- Проектирате мащабируеми MCP архитектури за сценарии с високо натоварване
- Прилагате добри практики за сигурност, съобразени с принципите за сигурност на MCP
- Интегрирате MCP с корпоративни AI системи и рамки
- Оптимизирате производителността и надеждността в производствени среди

## Уроци и примерни проекти

| Връзка | Заглавие | Описание |
|------|-------|-------------|
| [5.1 Integration with Azure](./mcp-integration/README.md) | Интеграция с Azure | Научете как да интегрирате вашия MCP сървър в Azure |
| [5.2 Multi modal sample](./mcp-multi-modality/README.md) | MCP мултимодални примери | Примери за аудио, изображения и мултимодални отговори |
| [5.3 MCP OAuth2 sample](../../../05-AdvancedTopics/mcp-oauth2-demo) | MCP OAuth2 Демонстрация | Минимално Spring Boot приложение, показващо OAuth2 с MCP, както като Authorization, така и като Resource Server. Демонстрира сигурно издаване на токени, защитени крайни точки, разгръщане в Azure Container Apps и интеграция с API Management. |
| [5.4 Root Contexts](./mcp-root-contexts/README.md) | Root контексти | Научете повече за root контекста и как да ги имплементирате |
| [5.5 Routing](./mcp-routing/README.md) | Рутинг | Научете различни типове маршрутизиране |
| [5.6 Sampling](./mcp-sampling/README.md) | Семплиране | Научете как да работите със семплиране |
| [5.7 Scaling](./mcp-scaling/README.md) | Мащабиране | Научете за мащабирането |
| [5.8 Security](./mcp-security/README.md) | Сигурност | Осигурете сигурността на вашия MCP сървър |
| [5.9 Web Search sample](./web-search-mcp/README.md) | Уеб търсене MCP | Python MCP сървър и клиент, интегрирани със SerpAPI за реално време уеб, новини, търсене на продукти и въпроси и отговори. Демонстрира мулти-инструментна оркестрация, интеграция с външни API и надеждна обработка на грешки. |
| [5.10 Realtime Streaming](./mcp-realtimestreaming/README.md) | Поточно предаване | Поточното предаване на данни в реално време се превърна в необходимост в днешния свят, ориентиран към данни, където бизнесите и приложенията изискват незабавен достъп до информация за вземане на своевременни решения. |
| [5.11 Realtime Web Search](./mcp-realtimesearch/README.md) | Уеб търсене | Как MCP трансформира уеб търсенето в реално време, предоставяйки стандартизиран подход към управлението на контекста между AI модели, търсачки и приложения. |

## Допълнителни препратки

За най-актуална информация относно разширените теми в MCP, посетете:
- [MCP Documentation](https://modelcontextprotocol.io/)
- [MCP Specification](https://spec.modelcontextprotocol.io/)
- [GitHub Repository](https://github.com/modelcontextprotocol)

## Основни изводи

- Мултимодалните имплементации на MCP разширяват AI възможностите извън обработката на текст
- Мащабируемостта е от съществено значение за корпоративни внедрявания и може да се постигне чрез хоризонтално и вертикално мащабиране
- Комплексните мерки за сигурност защитават данните и осигуряват правилен контрол на достъпа
- Интеграцията с корпоративни платформи като Azure OpenAI и Microsoft AI Foundry подобрява възможностите на MCP
- Разширените имплементации на MCP се възползват от оптимизирани архитектури и внимателно управление на ресурсите

## Упражнение

Проектирайте MCP имплементация с корпоративен клас за конкретен случай на употреба:

1. Идентифицирайте мултимодалните изисквания за вашия случай на употреба
2. Определете необходимите мерки за сигурност за защита на чувствителните данни
3. Проектирайте мащабируема архитектура, която може да се справя с променлив товар
4. Планирайте интеграционните точки с корпоративни AI системи
5. Документирайте потенциални тесни места в производителността и стратегии за тяхното преодоляване

## Допълнителни ресурси

- [Azure OpenAI Documentation](https://learn.microsoft.com/en-us/azure/ai-services/openai/)
- [Microsoft AI Foundry Documentation](https://learn.microsoft.com/en-us/ai-services/)

---

## Какво следва

- [5.1 MCP Integration](./mcp-integration/README.md)

**Отказ от отговорност**:  
Този документ е преведен с помощта на AI преводаческа услуга [Co-op Translator](https://github.com/Azure/co-op-translator). Въпреки че се стремим към точност, моля, имайте предвид, че автоматизираните преводи могат да съдържат грешки или неточности. Оригиналният документ на неговия роден език трябва да се счита за авторитетен източник. За критична информация се препоръчва професионален човешки превод. Ние не носим отговорност за каквито и да е недоразумения или неправилни тълкувания, произтичащи от използването на този превод.