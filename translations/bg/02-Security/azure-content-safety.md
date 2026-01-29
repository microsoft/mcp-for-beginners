# Разширена сигурност на MCP с Azure Content Safety

Azure Content Safety предлага няколко мощни инструмента, които могат да подобрят сигурността на вашите MCP реализации:

## Prompt Shields

AI Prompt Shields на Microsoft осигуряват здрава защита както срещу директни, така и срещу индиректни атаки чрез инжектиране на инструкции, чрез:

1. **Разширено откриване**: Използва машинно обучение за идентифициране на злонамерени инструкции, вградени в съдържанието.
2. **Подчертаване**: Преобразува входния текст, за да помогне на AI системите да различават валидни инструкции от външни входни данни.
3. **Разделители и маркиране на данни**: Отбелязва границите между доверени и недоверени данни.
4. **Интеграция с Content Safety**: Работи с Azure AI Content Safety за откриване на опити за jailbreak и вредно съдържание.
5. **Постоянни актуализации**: Microsoft редовно обновява защитните механизми срещу нововъзникващи заплахи.

## Прилагане на Azure Content Safety с MCP

Този подход осигурява многостепенна защита:
- Сканиране на входните данни преди обработка
- Валидация на изходните данни преди връщане
- Използване на блоклистове за известни вредни модели
- Използване на постоянно обновяваните модели за сигурност на съдържанието на Azure

## Ресурси за Azure Content Safety

За да научите повече за прилагането на Azure Content Safety с вашите MCP сървъри, консултирайте се с тези официални ресурси:

1. [Azure AI Content Safety Documentation](https://learn.microsoft.com/azure/ai-services/content-safety/) - Официална документация за Azure Content Safety.
2. [Prompt Shield Documentation](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/prompt-shield) - Научете как да предотвратите атаки чрез инжектиране на инструкции.
3. [Content Safety API Reference](https://learn.microsoft.com/rest/api/contentsafety/) - Подробна API справка за прилагане на Content Safety.
4. [Quickstart: Azure Content Safety with C#](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-csharp) - Бързо ръководство за прилагане с C#.
5. [Content Safety Client Libraries](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-client-libraries-rest-api) - Клиентски библиотеки за различни програмни езици.
6. [Detecting Jailbreak Attempts](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection) - Специфични насоки за откриване и предотвратяване на опити за jailbreak.
7. [Best Practices for Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/best-practices) - Най-добри практики за ефективно прилагане на сигурността на съдържанието.

За по-задълбочено прилагане вижте нашето [Ръководство за прилагане на Azure Content Safety](./azure-content-safety-implementation.md).

**Отказ от отговорност**:  
Този документ е преведен с помощта на AI преводаческа услуга [Co-op Translator](https://github.com/Azure/co-op-translator). Въпреки че се стремим към точност, моля, имайте предвид, че автоматизираните преводи могат да съдържат грешки или неточности. Оригиналният документ на неговия роден език трябва да се счита за авторитетен източник. За критична информация се препоръчва професионален човешки превод. Ние не носим отговорност за каквито и да е недоразумения или неправилни тълкувания, произтичащи от използването на този превод.