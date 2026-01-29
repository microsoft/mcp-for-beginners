# Розширений захист MCP за допомогою Azure Content Safety

Azure Content Safety пропонує кілька потужних інструментів, які можуть підвищити безпеку ваших реалізацій MCP:

## Prompt Shields

AI Prompt Shields від Microsoft забезпечують надійний захист від прямих і непрямих атак шляхом ін’єкції підказок завдяки:

1. **Розширеному виявленню**: використовує машинне навчання для ідентифікації шкідливих інструкцій, вбудованих у контент.
2. **Виділенню**: трансформує вхідний текст, щоб допомогти AI-системам розрізняти дійсні інструкції та зовнішні вхідні дані.
3. **Розмежувачам і маркуванню даних**: позначає межі між довіреними та недовіреними даними.
4. **Інтеграції з Content Safety**: працює з Azure AI Content Safety для виявлення спроб обходу захисту та шкідливого контенту.
5. **Постійним оновленням**: Microsoft регулярно оновлює механізми захисту від нових загроз.

## Впровадження Azure Content Safety з MCP

Цей підхід забезпечує багаторівневий захист:
- сканування вхідних даних перед обробкою
- перевірка результатів перед поверненням
- використання блоклистів для відомих шкідливих патернів
- застосування постійно оновлюваних моделей безпеки контенту Azure

## Ресурси Azure Content Safety

Щоб дізнатися більше про впровадження Azure Content Safety з вашими MCP-серверами, ознайомтеся з офіційними ресурсами:

1. [Azure AI Content Safety Documentation](https://learn.microsoft.com/azure/ai-services/content-safety/) - Офіційна документація Azure Content Safety.
2. [Prompt Shield Documentation](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/prompt-shield) - Дізнайтеся, як запобігти атакам шляхом ін’єкції підказок.
3. [Content Safety API Reference](https://learn.microsoft.com/rest/api/contentsafety/) - Детальна документація API для впровадження Content Safety.
4. [Quickstart: Azure Content Safety with C#](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-csharp) - Швидкий посібник з реалізації на C#.
5. [Content Safety Client Libraries](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-client-libraries-rest-api) - Клієнтські бібліотеки для різних мов програмування.
6. [Detecting Jailbreak Attempts](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection) - Специфічні рекомендації щодо виявлення та запобігання спробам обходу захисту.
7. [Best Practices for Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/best-practices) - Найкращі практики для ефективного впровадження безпеки контенту.

Для більш детального впровадження дивіться наш [Azure Content Safety Implementation guide](./azure-content-safety-implementation.md).

**Відмова від відповідальності**:  
Цей документ було перекладено за допомогою сервісу автоматичного перекладу [Co-op Translator](https://github.com/Azure/co-op-translator). Хоча ми прагнемо до точності, будь ласка, майте на увазі, що автоматичні переклади можуть містити помилки або неточності. Оригінальний документ рідною мовою слід вважати авторитетним джерелом. Для критично важливої інформації рекомендується звертатися до професійного людського перекладу. Ми не несемо відповідальності за будь-які непорозуміння або неправильні тлумачення, що виникли внаслідок використання цього перекладу.