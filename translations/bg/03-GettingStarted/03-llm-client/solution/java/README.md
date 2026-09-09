# Клиент на калкулатор LLM

Java приложение, което демонстрира как да използвате LangChain4j за свързване с MCP (Model Context Protocol) калкулаторна услуга чрез MiniMax API, съвместимо с OpenAI.

## Предварителни условия

- Java 21 или по-нова версия
- Maven 3.6+ (или използвайте включения Maven wrapper)
- Ключ за MiniMax API
- Работеща MCP калкулаторна услуга на `http://localhost:8080`

## Получаване на API ключа

Това приложение използва MiniMax API, съвместимо с OpenAI. Следвайте тези стъпки, за да получите ключа и крайна точка:

### 1. Изберете крайна точка
1. Използвайте `https://api.minimax.io/v1` за глобалната крайна точка
2. Използвайте `https://api.minimaxi.com/v1` за крайната точка в Китай

### 2. Създаване на API ключ
1. Създайте MiniMax API ключ от вашия MiniMax акаунт
2. Съхранявайте ключа на сигурно място

### 3. Настройка на променливите на средата

#### В Windows (Command Prompt):
```cmd
set OPENAI_API_KEY=your_minimax_api_key_here
set OPENAI_BASE_URL=https://api.minimax.io/v1
set MINIMAX_MODEL_ID=MiniMax-M3
```

#### В Windows (PowerShell):
```powershell
$env:OPENAI_API_KEY="your_minimax_api_key_here"
$env:OPENAI_BASE_URL="https://api.minimax.io/v1"
$env:MINIMAX_MODEL_ID="MiniMax-M3"
```

#### В macOS/Linux:
```bash
export OPENAI_API_KEY=your_minimax_api_key_here
export OPENAI_BASE_URL=https://api.minimax.io/v1
export MINIMAX_MODEL_ID=MiniMax-M3
```

## Настройка и инсталация

1. **Клонирайте или навигирайте до директорията на проекта**

2. **Инсталирайте зависимостите**:
   ```cmd
   mvnw clean install
   ```
   Или ако имате Maven инсталиран глобално:
   ```cmd
   mvn clean install
   ```

3. **Настройте променливите на средата** (вижте раздела "Получаване на API ключ" по-горе)

4. **Стартирайте MCP калкулаторната услуга**:
   Уверете се, че калкулаторната услуга от глава 1 работи на `http://localhost:8080/sse`. Тя трябва да бъде стартирана преди да стартирате клиента.

## Стартиране на приложението

```cmd
mvnw clean package
java -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## Какво прави приложението

Приложението демонстрира три основни взаимодействия с калкулаторната услуга:

1. **Събиране**: Изчислява сумата на 24.5 и 17.3
2. **Квадратен корен**: Изчислява квадратния корен на 144
3. **Помощ**: Показва наличните функции на калкулатора

## Очакван резултат

При успешно изпълнение трябва да видите изход, подобен на:

```
The sum of 24.5 and 17.3 is 41.8.
The square root of 144 is 12.
The calculator service provides the following functions: add, subtract, multiply, divide, sqrt, power...
```

## Отстраняване на проблеми

### Често срещани проблеми

1. **"Променливата на средата OPENAI_API_KEY не е зададена"**
   - Уверете се, че сте задали променливата на средата `OPENAI_API_KEY`
   - Рестартирайте терминала/командния ред след задаване на променливата

2. **"Връзката беше отказана към localhost:8080"**
   - Проверете дали MCP калкулаторната услуга работи на порт 8080
   - Проверете дали няма друга услуга на порт 8080

3. **"Аутентикацията не успя"**
   - Проверете дали вашият API ключ е валиден
   - Уверете се, че `OPENAI_BASE_URL` съвпада с използваната крайна точка

4. **Грешки при компилация с Maven**
   - Проверете дали използвате Java 21 или по-нова: `java -version`
   - Опитайте да почистите билд-а: `mvnw clean`

### Отстраняване на грешки

За да активирате debug логовете, добавете следния JVM аргумент при стартиране:
```cmd
java -Dlogging.level.dev.langchain4j=DEBUG -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## Конфигурация

Приложението е конфигурирано да:
- По подразбиране използва MiniMax-M3; задайте `MINIMAX_MODEL_ID` за избор между `MiniMax-M3` или `MiniMax-M2.7`
- Свързва се с `OPENAI_BASE_URL` когато е зададена; в противен случай използва `https://api.minimaxi.com/v1` при `MINIMAX_REGION=cn_zh`, или `https://api.minimax.io/v1` по подразбиране
- Свързва се с MCP услугата на `http://localhost:8080/sse`
- Използва timeout от 60 секунди за заявките

## Зависимости

Основни зависимости използвани в този проект:
- **LangChain4j**: За интеграция с AI и управление на инструменти
- **LangChain4j MCP**: За поддръжка на Model Context Protocol
- **LangChain4j OpenAI official**: За интеграция с MiniMax OpenAI-съвместим API
- **Spring Boot**: За приложение и dependency injection framework

## Лиценз

Този проект е лицензиран под Apache License 2.0 - вижте файла [LICENSE](../../../../../../03-GettingStarted/03-llm-client/solution/java/LICENSE) за подробности.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Отказ от отговорност**:
Този документ е преведен с помощта на AI преводачески услуга [Co-op Translator](https://github.com/Azure/co-op-translator). Въпреки че се стремим към точност, моля имайте предвид, че автоматизираните преводи могат да съдържат грешки или неточности. Оригиналният документ на неговия роден език трябва да се счита за авторитетен източник. За критична информация се препоръчва професионален човешки превод. Ние не носим отговорност за каквито и да е недоразумения или неправилни тълкувания, произтичащи от използването на този превод.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->