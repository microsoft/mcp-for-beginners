# Calculator LLM Client

Java приложение, което демонстрира как да използвате LangChain4j за свързване с MCP (Model Context Protocol) калкулатор услуга с интеграция на GitHub Models.

## Изисквания

- Java 21 или по-нова версия
- Maven 3.6+ (или използвайте включения Maven wrapper)
- GitHub акаунт с достъп до GitHub Models
- Работеща MCP калкулатор услуга на `http://localhost:8080`

## Как да получите GitHub токен

Това приложение използва GitHub Models, което изисква личен достъп токен от GitHub. Следвайте тези стъпки, за да получите своя токен:

### 1. Достъп до GitHub Models
1. Отидете на [GitHub Models](https://github.com/marketplace/models)
2. Влезте с вашия GitHub акаунт
3. Заявете достъп до GitHub Models, ако все още нямате

### 2. Създаване на личен достъп токен
1. Отидете на [GitHub Settings → Developer settings → Personal access tokens → Tokens (classic)](https://github.com/settings/tokens)
2. Натиснете "Generate new token" → "Generate new token (classic)"
3. Дайте описателно име на токена (например "MCP Calculator Client")
4. Задайте срок на валидност според нуждите
5. Изберете следните разрешения:
   - `repo` (ако имате достъп до частни хранилища)
   - `user:email`
6. Натиснете "Generate token"
7. **Важно**: Копирайте токена веднага - няма да можете да го видите отново!

### 3. Настройка на променлива на средата

#### В Windows (Command Prompt):
```cmd
set GITHUB_TOKEN=your_github_token_here
```

#### В Windows (PowerShell):
```powershell
$env:GITHUB_TOKEN="your_github_token_here"
```

#### В macOS/Linux:
```bash
export GITHUB_TOKEN=your_github_token_here
```

## Настройка и инсталация

1. **Клонирайте или отидете в директорията на проекта**

2. **Инсталирайте зависимостите**:
   ```cmd
   mvnw clean install
   ```
   Или ако имате глобално инсталиран Maven:
   ```cmd
   mvn clean install
   ```

3. **Настройте променливата на средата** (вижте секцията "Как да получите GitHub токен" по-горе)

4. **Стартирайте MCP калкулатор услугата**:
   Уверете се, че услугата от глава 1 работи на `http://localhost:8080/sse`. Тя трябва да е стартирана преди да пуснете клиента.

## Стартиране на приложението

```cmd
mvnw clean package
java -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## Какво прави приложението

Приложението демонстрира три основни взаимодействия с калкулатор услугата:

1. **Събиране**: Изчислява сумата на 24.5 и 17.3
2. **Квадратен корен**: Изчислява квадратния корен на 144
3. **Помощ**: Показва наличните функции на калкулатора

## Очакван изход

При успешно изпълнение трябва да видите изход, подобен на:

```
The sum of 24.5 and 17.3 is 41.8.
The square root of 144 is 12.
The calculator service provides the following functions: add, subtract, multiply, divide, sqrt, power...
```

## Отстраняване на проблеми

### Чести проблеми

1. **"GITHUB_TOKEN environment variable not set"**
   - Уверете се, че сте задали променливата на средата `GITHUB_TOKEN`
   - Рестартирайте терминала/командния прозорец след задаване на променливата

2. **"Connection refused to localhost:8080"**
   - Проверете дали MCP калкулатор услугата работи на порт 8080
   - Проверете дали друг процес не използва порт 8080

3. **"Authentication failed"**
   - Уверете се, че GitHub токенът е валиден и има правилните разрешения
   - Проверете дали имате достъп до GitHub Models

4. **Грешки при Maven build**
   - Уверете се, че използвате Java 21 или по-нова: `java -version`
   - Опитайте да почистите билдa: `mvnw clean`

### Отстраняване на грешки (Debugging)

За да активирате debug логване, добавете следния JVM аргумент при стартиране:
```cmd
java -Dlogging.level.dev.langchain4j=DEBUG -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## Конфигурация

Приложението е конфигурирано да:
- Използва GitHub Models с модела `gpt-4.1-nano`
- Свързва се с MCP услугата на `http://localhost:8080/sse`
- Използва 60-секунден таймаут за заявки
- Активира логване на заявки и отговори за отстраняване на грешки

## Зависимости

Основни зависимости в този проект:
- **LangChain4j**: За AI интеграция и управление на инструменти
- **LangChain4j MCP**: За поддръжка на Model Context Protocol
- **LangChain4j GitHub Models**: За интеграция с GitHub Models
- **Spring Boot**: За рамка на приложението и dependency injection

## Лиценз

Този проект е лицензиран под Apache License 2.0 - вижте файла [LICENSE](../../../../../../03-GettingStarted/03-llm-client/solution/java/LICENSE) за подробности.

**Отказ от отговорност**:  
Този документ е преведен с помощта на AI преводаческа услуга [Co-op Translator](https://github.com/Azure/co-op-translator). Въпреки че се стремим към точност, моля, имайте предвид, че автоматизираните преводи могат да съдържат грешки или неточности. Оригиналният документ на неговия роден език трябва да се счита за авторитетен източник. За критична информация се препоръчва професионален човешки превод. Ние не носим отговорност за каквито и да е недоразумения или неправилни тълкувания, произтичащи от използването на този превод.