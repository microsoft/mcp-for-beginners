# Клијент за Калкулатор LLM

Јава апликација која демонстрира како користити LangChain4j за повезивање са MCP (Model Context Protocol) сервисом за калкулатор преко MiniMax OpenAI-са компатибилног API-ја.

## Захтеви

- Јава 21 или новији
- Maven 3.6+ (или користите укључени Maven wrapper)
- MiniMax API кључ
- MCP сервис за калкулатор који ради на `http://localhost:8080`

## Прибављање API кључа

Ова апликација користи MiniMax OpenAI-са компатибилни API. Пратите ове кораке да добијете свој кључ и крајњу тачку:

### 1. Изаберите крајњу тачку
1. Користите `https://api.minimax.io/v1` за глобалну крајњу тачку
2. Користите `https://api.minimaxi.com/v1` за крајњу тачку у Кини

### 2. Направите API кључ
1. Направите MiniMax API кључ преко свог MiniMax налога
2. Чувајте кључ на сигурном месту

### 3. Поставите променљиве окружења

#### На Windows (Command Prompt):
```cmd
set OPENAI_API_KEY=your_minimax_api_key_here
set OPENAI_BASE_URL=https://api.minimax.io/v1
set MINIMAX_MODEL_ID=MiniMax-M3
```

#### На Windows (PowerShell):
```powershell
$env:OPENAI_API_KEY="your_minimax_api_key_here"
$env:OPENAI_BASE_URL="https://api.minimax.io/v1"
$env:MINIMAX_MODEL_ID="MiniMax-M3"
```

#### На macOS/Linux:
```bash
export OPENAI_API_KEY=your_minimax_api_key_here
export OPENAI_BASE_URL=https://api.minimax.io/v1
export MINIMAX_MODEL_ID=MiniMax-M3
```

## Подешавање и Инсталација

1. **Клонирајте или се преусмерите у директоријум пројекта**

2. **Инсталирајте зависности**:
   ```cmd
   mvnw clean install
   ```
   Или ако имате глобално инсталиран Maven:
   ```cmd
   mvn clean install
   ```

3. **Поставите променљиве окружења** (погледајте одељак "Прибављање API кључа" изнад)

4. **Покрените MCP сервис Калкулатора**:
   Проверите да ли MCP сервис калкулатора из поглавља 1 ради на `http://localhost:8080/sse`. Ово мора бити покренуто пре него што покренете клијент.

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

## Очекујани резултат

Када ради успешно, требало би да видите излаз сличан овоме:

```
The sum of 24.5 and 17.3 is 41.8.
The square root of 144 is 12.
The calculator service provides the following functions: add, subtract, multiply, divide, sqrt, power...
```

## Решавање проблема

### Чести проблеми

1. **"OPENAI_API_KEY environment variable is not set"**
   - Уверите се да сте поставили променљиву окружења `OPENAI_API_KEY`
   - Поново покрените терминал/command prompt након постављања променљиве

2. **"Connection refused to localhost:8080"**
   - Проверите да MCP сервис калкулатора ради на порту 8080
   - Проверите да ли неки други сервис користи порт 8080

3. **"Authentication failed"**
   - Проверите да ли је ваш API кључ важећи
   - Проверите да ли `OPENAI_BASE_URL` одговара крајњој тачки коју сте желели да користите

4. **Грешке у Maven изградњи**
   - Уверите се да користите Јаву 21 или новију: `java -version`
   - Покушајте очистити изградњу: `mvnw clean`

### Отклоните грешке са дебаговањем

За укључивање дебаг логовања, додајте следећи JVM аргумент приликом покретања:
```cmd
java -Dlogging.level.dev.langchain4j=DEBUG -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## Конфигурација

Апликација је конфигурисана да:
- По дефаулту користи MiniMax-M3, или MiniMax-M2.7 када је подешен `MINIMAX_MODEL_ID`
- Повезује се на `OPENAI_BASE_URL` ако је подешен; у супротном користи `https://api.minimaxi.com/v1` када је `MINIMAX_REGION=cn_zh`, или `https://api.minimax.io/v1` по дефаулту
- Повезује се на MCP сервис на `http://localhost:8080/sse`
- Користи тајмаут од 60 секунди за захтеве

## Зависности

Кључне зависности коришћене у овом пројекту:
- **LangChain4j**: За интеграцију AI и управљање алатима
- **LangChain4j MCP**: За подршку Model Context Protocol-а
- **LangChain4j OpenAI official**: За интеграцију са MiniMax OpenAI-са компатибилним API-јем
- **Spring Boot**: За оквир апликације и dependency injection

## Лиценца

Овај пројекат је лиценциран под Apache License 2.0 - погледајте [LICENSE](../../../../../../03-GettingStarted/03-llm-client/solution/java/LICENSE) фајл за детаље.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Изјава о одрицању одговорности**:
Овај документ је преведен коришћењем услуге за аутоматски превод [Co-op Translator](https://github.com/Azure/co-op-translator). Иако тежимо тачности, имајте у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати ауторитативним извором. За критичне информације препоручује се професионални људски превод. Нисмо одговорни за било каква неспоразума или погрешна тумачења која произилазе из коришћења овог превода.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->