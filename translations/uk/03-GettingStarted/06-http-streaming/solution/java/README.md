# Calculator HTTP Streaming Demo

Цей проєкт демонструє HTTP стрімінг за допомогою Server-Sent Events (SSE) з Spring Boot WebFlux. Він складається з двох додатків:

- **Calculator Server**: реактивний веб-сервіс, який виконує обчислення та передає результати через SSE
- **Calculator Client**: клієнтський додаток, який споживає стрімінгову кінцеву точку

## Вимоги

- Java 17 або новіша версія
- Maven 3.6 або новіша версія

## Структура проєкту

```
java/
├── calculator-server/     # Spring Boot server with SSE endpoint
│   ├── src/main/java/com/example/calculatorserver/
│   │   ├── CalculatorServerApplication.java
│   │   └── CalculatorController.java
│   └── pom.xml
├── calculator-client/     # Spring Boot client application
│   ├── src/main/java/com/example/calculatorclient/
│   │   └── CalculatorClientApplication.java
│   └── pom.xml
└── README.md
```

## Як це працює

1. **Calculator Server** надає кінцеву точку `/calculate`, яка:
   - Приймає параметри запиту: `a` (число), `b` (число), `op` (операція)
   - Підтримувані операції: `add`, `sub`, `mul`, `div`
   - Повертає Server-Sent Events з прогресом обчислення та результатом

2. **Calculator Client** підключається до сервера і:
   - Виконує запит на обчислення `7 * 5`
   - Споживає стрімінгову відповідь
   - Виводить кожну подію у консоль

## Запуск додатків

### Варіант 1: Використання Maven (рекомендовано)

#### 1. Запустіть Calculator Server

Відкрийте термінал і перейдіть у директорію сервера:

```bash
cd calculator-server
mvn clean package
mvn spring-boot:run
```

Сервер запуститься за адресою `http://localhost:8080`

Ви побачите вивід подібний до:
```
Started CalculatorServerApplication in X.XXX seconds
Netty started on port 8080 (http)
```

#### 2. Запустіть Calculator Client

Відкрийте **новий термінал** і перейдіть у директорію клієнта:

```bash
cd calculator-client
mvn clean package
mvn spring-boot:run
```

Клієнт підключиться до сервера, виконає обчислення та відобразить результати стрімінгу.

### Варіант 2: Запуск безпосередньо через Java

#### 1. Скомпілюйте та запустіть сервер:

```bash
cd calculator-server
mvn clean package
java -jar target/calculator-server-0.0.1-SNAPSHOT.jar
```

#### 2. Скомпілюйте та запустіть клієнт:

```bash
cd calculator-client
mvn clean package
java -jar target/calculator-client-0.0.1-SNAPSHOT.jar
```

## Ручне тестування сервера

Ви також можете протестувати сервер через веб-браузер або curl:

### Через веб-браузер:
Відвідайте: `http://localhost:8080/calculate?a=10&b=5&op=add`

### Через curl:
```bash
curl "http://localhost:8080/calculate?a=10&b=5&op=add" -H "Accept: text/event-stream"
```

## Очікуваний вивід

Під час запуску клієнта ви побачите стрімінговий вивід, схожий на:

```
event:info
data:Calculating: 7.0 mul 5.0

event:result
data:35.0
```

## Підтримувані операції

- `add` - Додавання (a + b)
- `sub` - Віднімання (a - b)
- `mul` - Множення (a * b)
- `div` - Ділення (a / b, повертає NaN, якщо b = 0)

## API Reference

### GET /calculate

**Параметри:**
- `a` (обов’язковий): перше число (double)
- `b` (обов’язковий): друге число (double)
- `op` (обов’язковий): операція (`add`, `sub`, `mul`, `div`)

**Відповідь:**
- Content-Type: `text/event-stream`
- Повертає Server-Sent Events з прогресом обчислення та результатом

**Приклад запиту:**
```
GET /calculate?a=7&b=5&op=mul HTTP/1.1
Host: localhost:8080
Accept: text/event-stream
```

**Приклад відповіді:**
```
event: info
data: Calculating: 7.0 mul 5.0

event: result
data: 35.0
```

## Вирішення проблем

### Поширені проблеми

1. **Порт 8080 вже використовується**
   - Зупиніть інші додатки, які використовують порт 8080
   - Або змініть порт сервера у файлі `calculator-server/src/main/resources/application.yml`

2. **Відмова у з’єднанні**
   - Переконайтеся, що сервер запущений перед запуском клієнта
   - Перевірте, що сервер успішно стартував на порту 8080

3. **Проблеми з іменами параметрів**
   - У проєкті налаштовано Maven компілятор з прапорцем `-parameters`
   - Якщо виникають проблеми з прив’язкою параметрів, переконайтеся, що проєкт зібрано з цією конфігурацією

### Зупинка додатків

- Натисніть `Ctrl+C` у терміналі, де запущено кожен додаток
- Або використайте `mvn spring-boot:stop`, якщо додаток запущено у фоновому режимі

## Технологічний стек

- **Spring Boot 3.3.1** - фреймворк для додатків
- **Spring WebFlux** - реактивний веб-фреймворк
- **Project Reactor** - бібліотека для реактивних стрімів
- **Netty** - сервер з неблокуючим ввід/виводом
- **Maven** - інструмент збірки
- **Java 17+** - мова програмування

## Наступні кроки

Спробуйте змінити код, щоб:
- Додати більше математичних операцій
- Впровадити обробку помилок для некоректних операцій
- Додати логування запитів/відповідей
- Реалізувати аутентифікацію
- Додати модульні тести

**Відмова від відповідальності**:  
Цей документ було перекладено за допомогою сервісу автоматичного перекладу [Co-op Translator](https://github.com/Azure/co-op-translator). Хоча ми прагнемо до точності, будь ласка, майте на увазі, що автоматичні переклади можуть містити помилки або неточності. Оригінальний документ рідною мовою слід вважати авторитетним джерелом. Для критично важливої інформації рекомендується звертатися до професійного людського перекладу. Ми не несемо відповідальності за будь-які непорозуміння або неправильні тлумачення, що виникли внаслідок використання цього перекладу.