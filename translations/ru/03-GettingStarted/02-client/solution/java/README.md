# MCP Java Client - Демонстрация калькулятора

Этот проект показывает, как создать Java-клиент, который подключается и взаимодействует с MCP (Model Context Protocol) сервером. В этом примере мы подключимся к серверу калькулятора из Главы 01 и выполним различные математические операции.

## Требования

Перед запуском клиента необходимо:

1. **Запустить сервер калькулятора** из Главы 01:
   - Перейдите в директорию сервера калькулятора: `03-GettingStarted/01-first-server/solution/java/`
   - Соберите и запустите сервер калькулятора:
     ```cmd
     cd ..\01-first-server\solution\java
     .\mvnw clean install -DskipTests
     java -jar target\calculator-server-0.0.1-SNAPSHOT.jar
     ```
   - Сервер должен работать по адресу `http://localhost:8080`

2. Установить **Java 21 или выше**
3. Иметь **Maven** (включён через Maven Wrapper)

## Что такое SDKClient?

`SDKClient` — это Java-приложение, демонстрирующее, как:
- Подключиться к MCP серверу с помощью Server-Sent Events (SSE)
- Получить список доступных инструментов на сервере
- Вызывать различные функции калькулятора удалённо
- Обрабатывать ответы и отображать результаты

## Как это работает

Клиент использует Spring AI MCP фреймворк для:

1. **Установки соединения**: создаёт WebFlux SSE клиент для подключения к серверу калькулятора
2. **Инициализации клиента**: настраивает MCP клиент и устанавливает соединение
3. **Обнаружения инструментов**: выводит список всех доступных операций калькулятора
4. **Выполнения операций**: вызывает различные математические функции с примерными данными
5. **Отображения результатов**: показывает результаты каждого вычисления

## Структура проекта

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

## Основные зависимости

В проекте используются следующие ключевые зависимости:

```xml
<dependency>
    <groupId>org.springframework.ai</groupId>
    <artifactId>spring-ai-starter-mcp-server-webflux</artifactId>
</dependency>
```

Эти зависимости предоставляют:
- `McpClient` — основной интерфейс клиента
- `WebFluxSseClientTransport` — SSE транспорт для веб-коммуникации
- Схемы протокола MCP и типы запросов/ответов

## Сборка проекта

Соберите проект с помощью Maven Wrapper:

```cmd
.\mvnw clean install
```

## Запуск клиента

```cmd
java -jar .\target\calculator-client-0.0.1-SNAPSHOT.jar
```

**Примечание**: Убедитесь, что сервер калькулятора запущен по адресу `http://localhost:8080` перед выполнением этих команд.

## Что делает клиент

При запуске клиент:

1. **Подключается** к серверу калькулятора по адресу `http://localhost:8080`
2. **Выводит список инструментов** — показывает все доступные операции калькулятора
3. **Выполняет вычисления**:
   - Сложение: 5 + 3 = 8
   - Вычитание: 10 - 4 = 6
   - Умножение: 6 × 7 = 42
   - Деление: 20 ÷ 4 = 5
   - Возведение в степень: 2^8 = 256
   - Квадратный корень: √16 = 4
   - Модуль: |-5.5| = 5.5
   - Помощь: показывает доступные операции

## Ожидаемый вывод

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

**Примечание**: В конце могут появиться предупреждения Maven о фоновых потоках — это нормально для реактивных приложений и не является ошибкой.

## Разбор кода

### 1. Настройка транспорта
```java
var transport = new WebFluxSseClientTransport(WebClient.builder().baseUrl("http://localhost:8080"));
```
Создаётся SSE (Server-Sent Events) транспорт для подключения к серверу калькулятора.

### 2. Создание клиента
```java
var client = McpClient.sync(this.transport).build();
client.initialize();
```
Создаётся синхронный MCP клиент и инициализируется соединение.

### 3. Вызов инструментов
```java
CallToolResult resultAdd = client.callTool(new CallToolRequest("add", Map.of("a", 5.0, "b", 3.0)));
```
Вызов инструмента "add" с параметрами a=5.0 и b=3.0.

## Устранение неполадок

### Сервер не запущен
Если возникают ошибки подключения, убедитесь, что сервер калькулятора из Главы 01 запущен:
```
Error: Connection refused
```
**Решение**: Сначала запустите сервер калькулятора.

### Порт уже занят
Если порт 8080 занят:
```
Error: Address already in use
```
**Решение**: Остановите другие приложения, использующие порт 8080, или измените порт сервера.

### Ошибки сборки
Если возникают ошибки при сборке:
```cmd
.\mvnw clean install -DskipTests
```

## Дополнительные материалы

- [Spring AI MCP Documentation](https://docs.spring.io/spring-ai/reference/api/mcp/)
- [Model Context Protocol Specification](https://modelcontextprotocol.io/)
- [Spring WebFlux Documentation](https://docs.spring.io/spring-framework/docs/current/reference/html/web-reactive.html)

**Отказ от ответственности**:  
Этот документ был переведен с помощью сервиса автоматического перевода [Co-op Translator](https://github.com/Azure/co-op-translator). Несмотря на наши усилия по обеспечению точности, просим учитывать, что автоматический перевод может содержать ошибки или неточности. Оригинальный документ на его исходном языке следует считать авторитетным источником. Для получения критически важной информации рекомендуется обращаться к профессиональному переводу, выполненному человеком. Мы не несем ответственности за любые недоразумения или неправильные толкования, возникшие в результате использования данного перевода.