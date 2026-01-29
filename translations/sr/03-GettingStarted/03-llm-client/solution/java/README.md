# Calculator LLM Client

Java апликација која показује како користити LangChain4j за повезивање са MCP (Model Context Protocol) сервисом калкулатора уз интеграцију GitHub Models.

## Захтеви

- Java 21 или новија верзија
- Maven 3.6+ (или користите укључени Maven wrapper)
- GitHub налог са приступом GitHub Models
- MCP сервис калкулатора који ради на `http://localhost:8080`

## Како добити GitHub Token

Ова апликација користи GitHub Models који захтева GitHub personal access token. Пратите ове кораке да бисте добили свој token:

### 1. Приступите GitHub Models
1. Идите на [GitHub Models](https://github.com/marketplace/models)
2. Пријавите се са својим GitHub налогом
3. Затражите приступ GitHub Models ако га већ немате

### 2. Креирајте Personal Access Token
1. Идите на [GitHub Settings → Developer settings → Personal access tokens → Tokens (classic)](https://github.com/settings/tokens)
2. Кликните на "Generate new token" → "Generate new token (classic)"
3. Дајте свом token-у описно име (нпр. "MCP Calculator Client")
4. Подесите рок важења по потреби
5. Изаберите следеће опсеге:
   - `repo` (ако приступате приватним репозиторијумима)
   - `user:email`
6. Кликните на "Generate token"
7. **Важно**: Одмах копирајте token - нећете га поново видети!

### 3. Подесите Environment Variable

#### На Windows (Command Prompt):
```cmd
set GITHUB_TOKEN=your_github_token_here
```

#### На Windows (PowerShell):
```powershell
$env:GITHUB_TOKEN="your_github_token_here"
```

#### На macOS/Linux:
```bash
export GITHUB_TOKEN=your_github_token_here
```

## Подешавање и инсталација

1. **Клонирајте или идите у директоријум пројекта**

2. **Инсталирајте зависности**:
   ```cmd
   mvnw clean install
   ```
   Или ако имате Maven инсталиран глобално:
   ```cmd
   mvn clean install
   ```

3. **Подесите environment variable** (погледајте одељак "Како добити GitHub Token" изнад)

4. **Покрените MCP Calculator Service**:
   Уверите се да је MCP сервис калкулатора из поглавља 1 покренут на `http://localhost:8080/sse`. Ово мора бити покренуто пре него што стартујете клијента.

## Покретање апликације

```cmd
mvnw clean package
java -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## Шта апликација ради

Апликација демонстрира три главне интеракције са сервисом калкулатора:

1. **Сабирање**: Израчунава збир 24.5 и 17.3
2. **Корен квадратни**: Израчунава корен квадратни од 144
3. **Помоћ**: Приказује доступне функције калкулатора

## Очекујени излаз

Када апликација успешно ради, требало би да видите излаз сличан овоме:

```
The sum of 24.5 and 17.3 is 41.8.
The square root of 144 is 12.
The calculator service provides the following functions: add, subtract, multiply, divide, sqrt, power...
```

## Решавање проблема

### Чести проблеми

1. **"GITHUB_TOKEN environment variable not set"**
   - Проверите да ли сте поставили `GITHUB_TOKEN` environment variable
   - Поново покрените терминал/command prompt након постављања променљиве

2. **"Connection refused to localhost:8080"**
   - Уверите се да MCP сервис калкулатора ради на порту 8080
   - Проверите да ли неки други сервис користи порт 8080

3. **"Authentication failed"**
   - Проверите да ли је ваш GitHub token важећи и да има одговарајуће дозволе
   - Проверите да ли имате приступ GitHub Models

4. **Грешке при Maven build-у**
   - Уверите се да користите Java 21 или новију верзију: `java -version`
   - Покушајте да очистите build: `mvnw clean`

### Дебаговање

Да бисте омогућили debug логовање, додајте следећи JVM аргумент приликом покретања:
```cmd
java -Dlogging.level.dev.langchain4j=DEBUG -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## Конфигурација

Апликација је конфигурисана да:
- Користи GitHub Models са моделом `gpt-4.1-nano`
- Повезује се на MCP сервис на `http://localhost:8080/sse`
- Користи timeout од 60 секунди за захтеве
- Омогућава логовање захтева/одговора ради дебаговања

## Зависности

Кључне зависности коришћене у овом пројекту:
- **LangChain4j**: За AI интеграцију и управљање алатима
- **LangChain4j MCP**: За подршку Model Context Protocol-а
- **LangChain4j GitHub Models**: За интеграцију GitHub Models
- **Spring Boot**: За апликациони фрејмворк и dependency injection

## Лиценца

Овај пројекат је лиценциран под Apache License 2.0 - погледајте [LICENSE](../../../../../../03-GettingStarted/03-llm-client/solution/java/LICENSE) фајл за детаље.

**Одрицање од одговорности**:  
Овај документ је преведен коришћењем AI услуге за превођење [Co-op Translator](https://github.com/Azure/co-op-translator). Иако се трудимо да превод буде тачан, молимо вас да имате у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати ауторитетним извором. За критичне информације препоручује се професионални људски превод. Нисмо одговорни за било каква неспоразума или погрешна тумачења која произилазе из коришћења овог превода.