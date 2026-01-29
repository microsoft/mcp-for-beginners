# MCP Java Client - Демонстрація калькулятора

Цей проєкт показує, як створити Java-клієнта, який підключається до MCP (Model Context Protocol) сервера та взаємодіє з ним. У цьому прикладі ми підключимося до сервера калькулятора з Розділу 01 і виконаємо різні математичні операції.

## Вимоги

Перед запуском цього клієнта потрібно:

1. **Запустити сервер калькулятора** з Розділу 01:
   - Перейдіть до каталогу сервера калькулятора: `03-GettingStarted/01-first-server/solution/java/`
   - Зберіть і запустіть сервер калькулятора:
     ```cmd
     cd ..\01-first-server\solution\java
     .\mvnw clean install -DskipTests
     java -jar target\calculator-server-0.0.1-SNAPSHOT.jar
     ```
   - Сервер має працювати за адресою `http://localhost:8080`

2. Встановлена **Java 21 або новіша**
3. **Maven** (включений через Maven Wrapper)

## Що таке SDKClient?

`SDKClient` — це Java-додаток, який демонструє, як:
- Підключитися до MCP сервера за допомогою Server-Sent Events (SSE)
- Отримати список доступних інструментів на сервері
- Викликати різні функції калькулятора віддалено
- Обробляти відповіді та відображати результати

## Як це працює

Клієнт використовує Spring AI MCP фреймворк для:

1. **Встановлення з’єднання**: створює WebFlux SSE клієнтський транспорт для підключення до сервера калькулятора
2. **Ініціалізації клієнта**: налаштовує MCP клієнта та встановлює з’єднання
3. **Виявлення інструментів**: отримує список усіх доступних операцій калькулятора
4. **Виконання операцій**: викликає різні математичні функції з прикладними даними
5. **Відображення результатів**: показує результати кожного обчислення

## Структура проєкту

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

## Основні залежності

Проєкт використовує такі ключові залежності:

```xml
<dependency>
    <groupId>org.springframework.ai</groupId>
    <artifactId>spring-ai-starter-mcp-server-webflux</artifactId>
</dependency>
```

Ця залежність надає:
- `McpClient` — основний інтерфейс клієнта
- `WebFluxSseClientTransport` — SSE транспорт для веб-комунікації
- Схеми протоколу MCP та типи запитів/відповідей

## Збірка проєкту

Зберіть проєкт за допомогою Maven wrapper:

```cmd
.\mvnw clean install
```

## Запуск клієнта

```cmd
java -jar .\target\calculator-client-0.0.1-SNAPSHOT.jar
```

**Примітка**: Переконайтеся, що сервер калькулятора працює за адресою `http://localhost:8080` перед виконанням цих команд.

## Що робить клієнт

Після запуску клієнт:

1. **Підключається** до сервера калькулятора за адресою `http://localhost:8080`
2. **Показує інструменти** — перелік усіх доступних операцій калькулятора
3. **Виконує обчислення**:
   - Додавання: 5 + 3 = 8
   - Віднімання: 10 - 4 = 6
   - Множення: 6 × 7 = 42
   - Ділення: 20 ÷ 4 = 5
   - Степінь: 2^8 = 256
   - Квадратний корінь: √16 = 4
   - Абсолютне значення: |-5.5| = 5.5
   - Допомога: показує доступні операції

## Очікуваний результат

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

**Примітка**: Наприкінці ви можете побачити попередження Maven про залишкові потоки — це нормально для реактивних додатків і не означає помилку.

## Розбір коду

### 1. Налаштування транспорту
```java
var transport = new WebFluxSseClientTransport(WebClient.builder().baseUrl("http://localhost:8080"));
```
Створює SSE (Server-Sent Events) транспорт, який підключається до сервера калькулятора.

### 2. Створення клієнта
```java
var client = McpClient.sync(this.transport).build();
client.initialize();
```
Створює синхронний MCP клієнт і ініціалізує з’єднання.

### 3. Виклик інструментів
```java
CallToolResult resultAdd = client.callTool(new CallToolRequest("add", Map.of("a", 5.0, "b", 3.0)));
```
Викликає інструмент "add" з параметрами a=5.0 та b=3.0.

## Вирішення проблем

### Сервер не запущений
Якщо виникають помилки підключення, переконайтеся, що сервер калькулятора з Розділу 01 запущений:
```
Error: Connection refused
```
**Рішення**: Спочатку запустіть сервер калькулятора.

### Порт вже зайнятий
Якщо порт 8080 зайнятий:
```
Error: Address already in use
```
**Рішення**: Зупиніть інші додатки, які використовують порт 8080, або змініть порт сервера.

### Помилки збірки
Якщо виникають помилки під час збірки:
```cmd
.\mvnw clean install -DskipTests
```

## Дізнатися більше

- [Spring AI MCP Documentation](https://docs.spring.io/spring-ai/reference/api/mcp/)
- [Model Context Protocol Specification](https://modelcontextprotocol.io/)
- [Spring WebFlux Documentation](https://docs.spring.io/spring-framework/docs/current/reference/html/web-reactive.html)

**Відмова від відповідальності**:  
Цей документ було перекладено за допомогою сервісу автоматичного перекладу [Co-op Translator](https://github.com/Azure/co-op-translator). Хоча ми прагнемо до точності, будь ласка, майте на увазі, що автоматичні переклади можуть містити помилки або неточності. Оригінальний документ рідною мовою слід вважати авторитетним джерелом. Для критично важливої інформації рекомендується звертатися до професійного людського перекладу. Ми не несемо відповідальності за будь-які непорозуміння або неправильні тлумачення, що виникли внаслідок використання цього перекладу.