# Клієнт Calculator LLM

Java-додаток, який демонструє, як використовувати LangChain4j для підключення до служби калькулятора MCP (Model Context Protocol) через OpenAI-сумісний API MiniMax.

## Вимоги

- Java 21 або вище
- Maven 3.6+ (або використовуйте вбудований Maven wrapper)
- Ключ API MiniMax
- Служба калькулятора MCP, що працює на `http://localhost:8080`

## Отримання ключа API

Цей додаток використовує OpenAI-сумісний API MiniMax. Виконайте ці кроки, щоб отримати свій ключ і кінцеву точку:

### 1. Виберіть кінцеву точку
1. Використовуйте `https://api.minimax.io/v1` для глобальної кінцевої точки
2. Використовуйте `https://api.minimaxi.com/v1` для кінцевої точки Китаю

### 2. Створіть ключ API
1. Створіть ключ API MiniMax у вашому акаунті MiniMax
2. Збережіть ключ у безпечному місці

### 3. Встановіть змінні середовища

#### У Windows (Command Prompt):
```cmd
set OPENAI_API_KEY=your_minimax_api_key_here
set OPENAI_BASE_URL=https://api.minimax.io/v1
set MINIMAX_MODEL_ID=MiniMax-M3
```

#### У Windows (PowerShell):
```powershell
$env:OPENAI_API_KEY="your_minimax_api_key_here"
$env:OPENAI_BASE_URL="https://api.minimax.io/v1"
$env:MINIMAX_MODEL_ID="MiniMax-M3"
```

#### У macOS/Linux:
```bash
export OPENAI_API_KEY=your_minimax_api_key_here
export OPENAI_BASE_URL=https://api.minimax.io/v1
export MINIMAX_MODEL_ID=MiniMax-M3
```

## Налаштування та встановлення

1. **Склонуйте або перейдіть у каталог проекту**

2. **Встановіть залежності**:
   ```cmd
   mvnw clean install
   ```
   Або, якщо Maven встановлено глобально:
   ```cmd
   mvn clean install
   ```

3. **Налаштуйте змінні середовища** (див. розділ "Отримання ключа API" вище)

4. **Запустіть службу калькулятора MCP**:
   Переконайтеся, що служба калькулятора MCP з першої глави працює на `http://localhost:8080/sse`. Вона повинна бути запущена перед запуском клієнта.

## Запуск додатку

```cmd
mvnw clean package
java -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## Що робить додаток

Додаток демонструє три основні взаємодії зі службою калькулятора:

1. **Додавання**: Обчислює суму 24.5 та 17.3
2. **Квадратний корінь**: Обчислює квадратний корінь із 144
3. **Допомога**: Показує доступні функції калькулятора

## Очікуваний результат

Під час успішного запуску ви побачите приблизно такий вивід:

```
The sum of 24.5 and 17.3 is 41.8.
The square root of 144 is 12.
The calculator service provides the following functions: add, subtract, multiply, divide, sqrt, power...
```

## Вирішення проблем

### Поширені проблеми

1. **"Змінна середовища OPENAI_API_KEY не встановлена"**
   - Переконайтеся, що ви встановили змінну середовища `OPENAI_API_KEY`
   - Перезапустіть термінал/командний рядок після встановлення змінної

2. **"Відмова з'єднання з localhost:8080"**
   - Переконайтеся, що служба калькулятора MCP працює на порті 8080
   - Перевірте, чи інша служба не використовує порт 8080

3. **"Помилка автентифікації"**
   - Перевірте, чи ваш ключ API дійсний
   - Переконайтеся, що `OPENAI_BASE_URL` відповідає обраній кінцевій точці

4. **Помилки збірки Maven**
   - Переконайтеся, що у вас Java 21 або вище: `java -version`
   - Спробуйте очистити збірку: `mvnw clean`

### Відлагодження

Щоб увімкнути налагоджувальне логування, додайте наступний аргумент JVM при запуску:
```cmd
java -Dlogging.level.dev.langchain4j=DEBUG -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## Конфігурація

Додаток налаштований на:
- Використання MiniMax-M3 за замовчуванням, або MiniMax-M2.7, якщо встановлено `MINIMAX_MODEL_ID`
- Підключення до `OPENAI_BASE_URL`, якщо він встановлений; інакше використовується `https://api.minimaxi.com/v1`, коли `MINIMAX_REGION=cn_zh`, або за замовчуванням `https://api.minimax.io/v1`
- Підключення до служби MCP за адресою `http://localhost:8080/sse`
- Таймаут запиту 60 секунд

## Залежності

Ключові залежності, використані в цьому проєкті:
- **LangChain4j**: Для інтеграції зі ШІ та управління інструментами
- **LangChain4j MCP**: Для підтримки протоколу Model Context Protocol
- **LangChain4j OpenAI official**: Для інтеграції OpenAI-сумісного API MiniMax
- **Spring Boot**: Для фреймворка додатку та впровадження залежностей

## Ліцензія

Цей проєкт ліцензований під Apache License 2.0 — див. файл [LICENSE](../../../../../../03-GettingStarted/03-llm-client/solution/java/LICENSE) для подробиць.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Відмова від відповідальності**:
Цей документ було перекладено за допомогою сервісу штучного інтелекту для перекладу [Co-op Translator](https://github.com/Azure/co-op-translator). Хоча ми прагнемо до точності, будь ласка, майте на увазі, що автоматичні переклади можуть містити помилки або неточності. Оригінальний документ рідною мовою слід вважати авторитетним джерелом. Для критично важливої інформації рекомендується професійний людський переклад. Ми не несемо відповідальності за будь-які непорозуміння або неправильні тлумачення, що виникли внаслідок використання цього перекладу.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->