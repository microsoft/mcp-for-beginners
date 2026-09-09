# Calculator LLM Клијент

Јава апликација која демонстрира како користити LangChain4j за повезивање са MCP (Model Context Protocol) сервисом калкулатора преко MiniMax OpenAI-компатибилног API-ја.

## Предуслови

- Јава 21 или новија
- Maven 3.6+ (или користите укључени Maven wrapper)
- MiniMax API кључ
- MCP калкулатор сервис покренут на `http://localhost:8080`

## Како добити API кључ

Ова апликација користи MiniMax OpenAI-компатибилан API. Пратите следеће кораке да бисте добили свој кључ и крајњу тачку:

### 1. Изаберите крајњу тачку
1. Користите `https://api.minimax.io/v1` за глобалну крајњу тачку
2. Користите `https://api.minimaxi.com/v1` за Кину крајњу тачку

### 2. Направите API кључ
1. Направите MiniMax API кључ са свог MiniMax налога
2. Чувајте кључ на безбедном месту

### 3. Поставите системске променљиве окружења

#### На Windows-у (Command Prompt):
```cmd
set OPENAI_API_KEY=your_minimax_api_key_here
set OPENAI_BASE_URL=https://api.minimax.io/v1
set MINIMAX_MODEL_ID=MiniMax-M3
```

#### На Windows-у (PowerShell):
```powershell
$env:OPENAI_API_KEY="your_minimax_api_key_here"
$env:OPENAI_BASE_URL="https://api.minimax.io/v1"
$env:MINIMAX_MODEL_ID="MiniMax-M3"
```

#### На macOS/Linux-у:
```bash
export OPENAI_API_KEY=your_minimax_api_key_here
export OPENAI_BASE_URL=https://api.minimax.io/v1
export MINIMAX_MODEL_ID=MiniMax-M3
```

## Подешавање и инсталација

1. **Клонирајте или идите у директоријум пројекта**

2. **Инсталирајте зависности**:
   ```cmd
   mvnw clean install
   ```
   Или ако имате Maven глобално инсталиран:
   ```cmd
   mvn clean install
   ```

3. **Поставите системске променљиве окружења** (погледајте одељак „Како добити API кључ“ изнад)

4. **Покрените MCP сервис калкулатора**:
   Уверите се да имате MCP сервис калкулатора из првог поглавља покренут на `http://localhost:8080/sse`. Ово треба бити покренуто пре покретања клијента.

## Покретање апликације

```cmd
mvnw clean package
java -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## Шта апликација ради

Апликација демонстрира три главне интеракције са сервисом калкулатора:

1. **Збир**: Израчунава збир 24.5 и 17.3
2. **Квадратни корен**: Израчунава квадратни корен од 144
3. **Помоћ**: Приказује доступне функције калкулатора

## Очекивани излаз

Када ради исправно, требало би да видите излаз сличан овоме:

```
The sum of 24.5 and 17.3 is 41.8.
The square root of 144 is 12.
The calculator service provides the following functions: add, subtract, multiply, divide, sqrt, power...
```

## Решавање проблема

### Чести проблеми

1. **"OPENAI_API_KEY променљива окружења није подешена"**
   - Проверите да ли сте поставили `OPENAI_API_KEY` променљиву окружења
   - Поново покрените терминал/command prompt након постављања променљиве

2. **"Повезивање на localhost:8080 одбијено"**
   - Проверите да ли MCP сервис калкулатора ради на порту 8080
   - Проверите да ли неки други сервис користи порт 8080

3. **"Аутентификација није успела"**
   - Потврдите да је ваш API кључ ваљан
   - Проверите да ли `OPENAI_BASE_URL` одговара крајњој тачки коју желите да користите

4. **Грешке приликом Maven build-а**
   - Проверите да користите Јава 21 или новију верзију: `java -version`
   - Покушајте очистити build: `mvnw clean`

### Отказивање грешака (debugging)

Да бисте омогућили debug логовање, додајте следећи JVM аргумент приликом покретања:
```cmd
java -Dlogging.level.dev.langchain4j=DEBUG -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## Конфигурација

Апликација је конфигурисана да:
- Подразумевано користи MiniMax-M3; поставите `MINIMAX_MODEL_ID` да изаберете између `MiniMax-M3` или `MiniMax-M2.7`
- Повезује се са `OPENAI_BASE_URL` када је подешена; у супротном користи `https://api.minimaxi.com/v1` када је `MINIMAX_REGION=cn_zh`, или `https://api.minimax.io/v1` по подразумеваној вредности
- Повезује се са MCP сервисом на `http://localhost:8080/sse`
- Користи timeout од 60 секунди за захтеве

## Зависности

Кључне зависности коришћене у овом пројекту:
- **LangChain4j**: За интеграцију вештачке интелигенције и управљање алатима
- **LangChain4j MCP**: За подршку Model Context Protocol-а
- **LangChain4j OpenAI official**: За интеграцију MiniMax OpenAI-компатибилног API-ја
- **Spring Boot**: За апликациони оквир и dependency injection

## Лиценца

Овај пројекат је лиценциран под Apache License 2.0 - погледајте [LICENSE](../../../../../../03-GettingStarted/03-llm-client/solution/java/LICENSE) фајл за детаље.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Изјава о одрицању одговорности**:
Овај документ је преведен коришћењем услуге за аутоматски превод [Co-op Translator](https://github.com/Azure/co-op-translator). Иако тежимо тачности, имајте у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати ауторитативним извором. За критичне информације препоручује се професионални људски превод. Нисмо одговорни за било каква неспоразума или погрешна тумачења која произилазе из коришћења овог превода.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->