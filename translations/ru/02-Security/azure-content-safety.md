# Расширенная безопасность MCP с Azure Content Safety

Azure Content Safety предлагает несколько мощных инструментов, которые могут значительно повысить безопасность ваших реализаций MCP:

## Prompt Shields

AI Prompt Shields от Microsoft обеспечивают надежную защиту от прямых и косвенных атак с использованием внедрения команд благодаря:

1. **Продвинутому обнаружению**: использует машинное обучение для выявления вредоносных инструкций, встроенных в контент.
2. **Выделению**: преобразует входной текст, помогая AI-системам отличать корректные команды от внешних вводов.
3. **Разделителям и маркировке данных**: отмечает границы между доверенными и недоверенными данными.
4. **Интеграции с Content Safety**: работает совместно с Azure AI Content Safety для обнаружения попыток обхода защиты и вредоносного контента.
5. **Постоянным обновлением**: Microsoft регулярно обновляет механизмы защиты от новых угроз.

## Внедрение Azure Content Safety с MCP

Этот подход обеспечивает многоуровневую защиту:
- сканирование входных данных перед обработкой
- проверка выходных данных перед возвратом
- использование блок-листов для известных вредоносных шаблонов
- применение постоянно обновляемых моделей безопасности Azure

## Ресурсы Azure Content Safety

Чтобы узнать больше о внедрении Azure Content Safety с вашими MCP-серверами, ознакомьтесь с официальными ресурсами:

1. [Azure AI Content Safety Documentation](https://learn.microsoft.com/azure/ai-services/content-safety/) — официальная документация по Azure Content Safety.
2. [Prompt Shield Documentation](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/prompt-shield) — как предотвратить атаки с внедрением команд.
3. [Content Safety API Reference](https://learn.microsoft.com/rest/api/contentsafety/) — подробное описание API для реализации Content Safety.
4. [Quickstart: Azure Content Safety with C#](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-csharp) — быстрое руководство по внедрению с использованием C#.
5. [Content Safety Client Libraries](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-client-libraries-rest-api) — клиентские библиотеки для различных языков программирования.
6. [Detecting Jailbreak Attempts](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection) — рекомендации по обнаружению и предотвращению попыток обхода защиты.
7. [Best Practices for Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/best-practices) — лучшие практики для эффективного внедрения Content Safety.

Для более подробного руководства по внедрению смотрите наш [Azure Content Safety Implementation guide](./azure-content-safety-implementation.md).

**Отказ от ответственности**:  
Этот документ был переведен с помощью сервиса автоматического перевода [Co-op Translator](https://github.com/Azure/co-op-translator). Несмотря на наши усилия по обеспечению точности, просим учитывать, что автоматические переводы могут содержать ошибки или неточности. Оригинальный документ на его исходном языке следует считать авторитетным источником. Для получения критически важной информации рекомендуется обращаться к профессиональному человеческому переводу. Мы не несем ответственности за любые недоразумения или неправильные толкования, возникшие в результате использования данного перевода.