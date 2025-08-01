<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "1b6c746d9e190deba4d8765267ffb94e",
  "translation_date": "2025-07-17T02:00:14+00:00",
  "source_file": "02-Security/azure-content-safety-implementation.md",
  "language_code": "ru"
}
-->
# Реализация Azure Content Safety с MCP

Для повышения безопасности MCP против инъекций в подсказки, отравления инструментов и других уязвимостей, связанных с ИИ, настоятельно рекомендуется интегрировать Azure Content Safety.

## Интеграция с MCP Server

Чтобы интегрировать Azure Content Safety с вашим MCP сервером, добавьте фильтр безопасности контента в качестве промежуточного ПО в конвейер обработки запросов:

1. Инициализируйте фильтр при запуске сервера  
2. Проверяйте все входящие запросы к инструментам перед обработкой  
3. Проверяйте все исходящие ответы перед отправкой клиентам  
4. Ведите журнал и оповещайте о нарушениях безопасности  
5. Реализуйте соответствующую обработку ошибок при неудачных проверках безопасности контента  

Это обеспечивает надежную защиту от:  
- Атак с инъекцией подсказок  
- Попыток отравления инструментов  
- Утечки данных через вредоносные вводы  
- Генерации вредоносного контента  

## Лучшие практики интеграции Azure Content Safety

1. **Пользовательские блок-листы**: Создавайте специальные блок-листы для паттернов инъекций MCP  
2. **Настройка уровня серьезности**: Регулируйте пороги серьезности в зависимости от конкретного сценария и уровня риска  
3. **Всестороннее покрытие**: Применяйте проверки безопасности контента ко всем входным и выходным данным  
4. **Оптимизация производительности**: Рассмотрите возможность кэширования повторяющихся проверок безопасности контента  
5. **Механизмы резервного копирования**: Определите четкие действия на случай недоступности сервисов безопасности контента  
6. **Обратная связь пользователям**: Предоставляйте понятные уведомления пользователям при блокировке контента по соображениям безопасности  
7. **Постоянное улучшение**: Регулярно обновляйте блок-листы и паттерны с учетом новых угроз

**Отказ от ответственности**:  
Этот документ был переведен с помощью сервиса автоматического перевода [Co-op Translator](https://github.com/Azure/co-op-translator). Несмотря на наши усилия по обеспечению точности, просим учитывать, что автоматический перевод может содержать ошибки или неточности. Оригинальный документ на его исходном языке следует считать авторитетным источником. Для получения критически важной информации рекомендуется обращаться к профессиональному человеческому переводу. Мы не несем ответственности за любые недоразумения или неправильные толкования, возникшие в результате использования данного перевода.