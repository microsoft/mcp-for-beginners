# MCP Java Client - Calculator Demo

Овај пројекат показује како направити Java клијента који се повезује и комуницира са MCP (Model Context Protocol) сервером. У овом примеру ћемо се повезати на сервер калкулатора из Поглавља 01 и извршити различите математичке операције.

## Захтеви

Пре покретања овог клијента, потребно је да:

1. **Покренете Calculator Server** из Поглавља 01:
   - Идите у директоријум сервера калкулатора: `03-GettingStarted/01-first-server/solution/java/`
   - Изградите и покрените сервер калкулатора:
     ```cmd
     cd ..\01-first-server\solution\java
     .\mvnw clean install -DskipTests
     java -jar target\calculator-server-0.0.1-SNAPSHOT.jar
     ```
   - Сервер би требало да ради на адреси `http://localhost:8080`

2. Имати инсталиран **Java 21 или новији**
3. Имати **Maven** (укључен преко Maven Wrapper-а)

## Шта је SDKClient?

`SDKClient` је Java апликација која показује како да:
- Повежете се на MCP сервер користећи Server-Sent Events (SSE) транспорт
- Прикажете доступне алате са сервера
- Позовете различите функције калкулатора удаљено
- Обрадите одговоре и прикажете резултате

## Како ради

Клијент користи Spring AI MCP фрејмворк да:

1. **Успостави везу**: Креира WebFlux SSE клијент транспорт за повезивање са сервером калкулатора
2. **Иницијализује клијента**: Подешава MCP клијента и успоставља везу
3. **Открије алате**: Приказује све доступне операције калкулатора
4. **Изврши операције**: Позива различите математичке функције са примерима података
5. **Прикаже резултате**: Приказује резултате сваког израчунавања

## Структура пројекта

```
src/
└── main/
    └── java/
        └── com/
            └── microsoft/
                └── mcp/
                    └── sample/
                        └── client/
                            └── SDKClient.java    # Main client implementation
```

## Кључне зависности

Пројекат користи следеће кључне зависности:

```xml
<dependency>
    <groupId>org.springframework.ai</groupId>
    <artifactId>spring-ai-starter-mcp-server-webflux</artifactId>
</dependency>
```

Ова зависност обезбеђује:
- `McpClient` - Главни интерфејс клијента
- `WebFluxSseClientTransport` - SSE транспорт за веб комуникацију
- MCP протокол шеме и типове захтева/одговора

## Изградња пројекта

Изградите пројекат користећи Maven wrapper:

```cmd
.\mvnw clean install
```

## Покретање клијента

```cmd
java -jar .\target\calculator-client-0.0.1-SNAPSHOT.jar
```

**Note**: Проверите да ли сервер калкулатора ради на `http://localhost:8080` пре извршавања било које од ових команди.

## Шта клијент ради

Када покренете клијента, он ће:

1. **Повезати се** на сервер калкулатора на адреси `http://localhost:8080`
2. **Приказати алате** - Приказује све доступне операције калкулатора
3. **Извршити израчунавања**:
   - Сабирање: 5 + 3 = 8
   - Одузимање: 10 - 4 = 6
   - Множење: 6 × 7 = 42
   - Дељење: 20 ÷ 4 = 5
   - Степеновање: 2^8 = 256
   - Квадратни корен: √16 = 4
   - Апсолутна вредност: |-5.5| = 5.5
   - Помоћ: Приказује доступне операције

## Очекујени излаз

```
Available Tools = ListToolsResult[tools=[Tool[name=add, description=Add two numbers together, ...], ...]]
Add Result = CallToolResult[content=[TextContent[text="5,00 + 3,00 = 8,00"]], isError=false]
Subtract Result = CallToolResult[content=[TextContent[text="10,00 - 4,00 = 6,00"]], isError=false]
Multiply Result = CallToolResult[content=[TextContent[text="6,00 * 7,00 = 42,00"]], isError=false]
Divide Result = CallToolResult[content=[TextContent[text="20,00 / 4,00 = 5,00"]], isError=false]
Power Result = CallToolResult[content=[TextContent[text="2,00 ^ 8,00 = 256,00"]], isError=false]
Square Root Result = CallToolResult[content=[TextContent[text="√16,00 = 4,00"]], isError=false]
Absolute Result = CallToolResult[content=[TextContent[text="|-5,50| = 5,50"]], isError=false]
Help = CallToolResult[content=[TextContent[text="Basic Calculator MCP Service\n\nAvailable operations:\n1. add(a, b) - Adds two numbers\n2. subtract(a, b) - Subtracts the second number from the first\n..."]], isError=false]
```

**Note**: Могуће је да ћете видети Maven упозорења о преосталим нитима на крају - то је нормално за реактивне апликације и не указује на грешку.

## Разумевање кода

### 1. Подешавање транспорта
```java
var transport = new WebFluxSseClientTransport(WebClient.builder().baseUrl("http://localhost:8080"));
```
Ово креира SSE (Server-Sent Events) транспорт који се повезује на сервер калкулатора.

### 2. Креирање клијента
```java
var client = McpClient.sync(this.transport).build();
client.initialize();
```
Креира синхрони MCP клијент и иницијализује везу.

### 3. Позивање алата
```java
CallToolResult resultAdd = client.callTool(new CallToolRequest("add", Map.of("a", 5.0, "b", 3.0)));
```
Позива алат "add" са параметрима a=5.0 и b=3.0.

## Решавање проблема

### Сервер није покренут
Ако добијете грешке у вези са повезивањем, проверите да ли је сервер калкулатора из Поглавља 01 покренут:
```
Error: Connection refused
```
**Решење**: Прво покрените сервер калкулатора.

### Порт је већ у употреби
Ако је порт 8080 заузет:
```
Error: Address already in use
```
**Решење**: Зауставите друге апликације које користе порт 8080 или промените порт сервера.

### Грешке при изградњи
Ако наиђете на грешке приликом изградње:
```cmd
.\mvnw clean install -DskipTests
```

## Сазнајте више

- [Spring AI MCP Documentation](https://docs.spring.io/spring-ai/reference/api/mcp/)
- [Model Context Protocol Specification](https://modelcontextprotocol.io/)
- [Spring WebFlux Documentation](https://docs.spring.io/spring-framework/docs/current/reference/html/web-reactive.html)

**Одрицање од одговорности**:  
Овај документ је преведен коришћењем AI преводилачке услуге [Co-op Translator](https://github.com/Azure/co-op-translator). Иако се трудимо да превод буде тачан, молимо вас да имате у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати ауторитетним извором. За критичне информације препоручује се професионални људски превод. Нисмо одговорни за било каква неспоразума или погрешна тумачења која произилазе из коришћења овог превода.