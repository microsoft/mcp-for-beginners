# Клієнт Calculator LLM

Java-додаток, який демонструє, як використовувати LangChain4j для підключення до сервісу калькулятора MCP (Model Context Protocol) через OpenAI-сумісний API MiniMax.

## Передумови

- Java 21 або вище
- Maven 3.6+ (або використовуйте включений Maven wrapper)
- Ключ API MiniMax
- Запущений сервіс калькулятора MCP на `http://localhost:8080`

## Отримання ключа API

Цей додаток використовує OpenAI-сумісний API MiniMax. Виконайте ці кроки, щоб отримати ваш ключ та кінцеву точку:

### 1. Виберіть кінцеву точку
1. Використовуйте `https://api.minimax.io/v1` для глобальної кінцевої точки
2. Використовуйте `https://api.minimaxi.com/v1` для кінцевої точки в Китаї

### 2. Створіть ключ API
1. Створіть ключ API MiniMax у вашому акаунті MiniMax
2. Збережіть ключ у надійному місці

### 3. Встановіть змінні оточення

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

1. **Клонувати або перейти до каталогу проекту**

2. **Встановити залежності**:
   ```cmd
   mvnw clean install
   ```
   Або, якщо у вас встановлений Maven глобально:
   ```cmd
   mvn clean install
   ```

3. **Встановити змінні оточення** (див. розділ "Отримання ключа API" вище)

4. **Запустити сервіс MCP Calculator**:
   Переконайтеся, що сервіс калькулятора MCP з першого розділу запущений на `http://localhost:8080/sse`. Він має працювати перед запуском клієнта.

## Запуск додатку

```cmd
mvnw clean package
java -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## Що робить додаток

Додаток демонструє три основні взаємодії з сервісом калькулятора:

1. **Додавання**: Обчислює суму 24.5 та 17.3
2. **Квадратний корінь**: Обчислює квадратний корінь із 144
3. **Допомога**: Показує доступні функції калькулятора

## Очікуваний результат

Під час успішного запуску ви побачите результат, подібний до:

```
The sum of 24.5 and 17.3 is 41.8.
The square root of 144 is 12.
The calculator service provides the following functions: add, subtract, multiply, divide, sqrt, power...
```

## Усунення неполадок

### Поширені проблеми

1. **"Змінна оточення OPENAI_API_KEY не встановлена"**
   - Переконайтеся, що змінна оточення `OPENAI_API_KEY` встановлена
   - Перезавантажте термінал/командний рядок після встановлення змінної

2. **"Відмова з'єднання з localhost:8080"**
   - Переконайтеся, що сервіс MCP calculator працює на порті 8080
   - Перевірте, чи інший сервіс не використовує порт 8080

3. **"Помилка аутентифікації"**
   - Перевірте, чи ваш ключ API є дійсним
   - Переконайтеся, що `OPENAI_BASE_URL` відповідає кінцевій точці, яку ви хотіли використовувати

4. **Помилки збірки Maven**
   - Переконайтеся, що використовується Java 21 або вище: `java -version`
   - Спробуйте очистити збірку: `mvnw clean`

### Налагодження

Щоб увімкнути налагоджувальний лог, додайте наступний аргумент JVM при запуску:
```cmd
java -Dlogging.level.dev.langchain4j=DEBUG -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## Конфігурація

Додаток налаштований на:
- Використання MiniMax-M3 за замовчуванням; встановіть `MINIMAX_MODEL_ID` для вибору `MiniMax-M3` або `MiniMax-M2.7`
- Підключення до `OPENAI_BASE_URL`, якщо він встановлений; в іншому разі використовується `https://api.minimaxi.com/v1` при `MINIMAX_REGION=cn_zh` або `https://api.minimax.io/v1` за замовчуванням
- Підключення до сервісу MCP за адресою `http://localhost:8080/sse`
- Використання таймауту запитів 60 секунд

## Залежності

Основні залежності, використані в проекті:
- **LangChain4j**: для інтеграції штучного інтелекту та управління інструментами
- **LangChain4j MCP**: для підтримки Model Context Protocol
- **LangChain4j OpenAI official**: для інтеграції з MiniMax OpenAI-сумісним API
- **Spring Boot**: для фреймворку додатку та ін’єкції залежностей

## Ліцензія

Цей проект ліцензовано за ліцензією Apache License 2.0 - дивіться файл [LICENSE](../../../../../../03-GettingStarted/03-llm-client/solution/java/LICENSE) для деталей.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Відмова від відповідальності**:
Цей документ було перекладено за допомогою сервісу штучного інтелекту для перекладу [Co-op Translator](https://github.com/Azure/co-op-translator). Хоча ми прагнемо до точності, будь ласка, майте на увазі, що автоматичні переклади можуть містити помилки або неточності. Оригінальний документ рідною мовою слід вважати авторитетним джерелом. Для критично важливої інформації рекомендується професійний людський переклад. Ми не несемо відповідальності за будь-які непорозуміння або неправильні тлумачення, що виникли внаслідок використання цього перекладу.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->