# Calculator HTTP Streaming Demo

Този проект демонстрира HTTP стрийминг с помощта на Server-Sent Events (SSE) и Spring Boot WebFlux. Състои се от две приложения:

- **Calculator Server**: реактивен уеб сървис, който извършва изчисления и стриймва резултатите чрез SSE
- **Calculator Client**: клиентско приложение, което консумира стрийминг ендпойнта

## Изисквания

- Java 17 или по-нова версия
- Maven 3.6 или по-нова версия

## Структура на проекта

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

## Как работи

1. **Calculator Server** предоставя ендпойнт `/calculate`, който:
   - Приема query параметри: `a` (число), `b` (число), `op` (операция)
   - Поддържани операции: `add`, `sub`, `mul`, `div`
   - Връща Server-Sent Events с прогреса на изчислението и резултата

2. **Calculator Client** се свързва със сървъра и:
   - Изпраща заявка за изчисление на `7 * 5`
   - Консумира стрийминг отговора
   - Извежда всяко събитие в конзолата

## Стартиране на приложенията

### Вариант 1: Използване на Maven (препоръчително)

#### 1. Стартирайте Calculator Server

Отворете терминал и отидете в директорията на сървъра:

```bash
cd calculator-server
mvn clean package
mvn spring-boot:run
```

Сървърът ще стартира на `http://localhost:8080`

Трябва да видите изход като:
```
Started CalculatorServerApplication in X.XXX seconds
Netty started on port 8080 (http)
```

#### 2. Стартирайте Calculator Client

Отворете **нов терминал** и отидете в директорията на клиента:

```bash
cd calculator-client
mvn clean package
mvn spring-boot:run
```

Клиентът ще се свърже със сървъра, ще извърши изчислението и ще покаже стрийминг резултатите.

### Вариант 2: Използване на Java директно

#### 1. Компилирайте и стартирайте сървъра:

```bash
cd calculator-server
mvn clean package
java -jar target/calculator-server-0.0.1-SNAPSHOT.jar
```

#### 2. Компилирайте и стартирайте клиента:

```bash
cd calculator-client
mvn clean package
java -jar target/calculator-client-0.0.1-SNAPSHOT.jar
```

## Ръчно тестване на сървъра

Можете да тествате сървъра и чрез уеб браузър или curl:

### С уеб браузър:
Посетете: `http://localhost:8080/calculate?a=10&b=5&op=add`

### С curl:
```bash
curl "http://localhost:8080/calculate?a=10&b=5&op=add" -H "Accept: text/event-stream"
```

## Очакван изход

При стартиране на клиента трябва да видите стрийминг изход, подобен на:

```
event:info
data:Calculating: 7.0 mul 5.0

event:result
data:35.0
```

## Поддържани операции

- `add` - Събиране (a + b)
- `sub` - Изваждане (a - b)
- `mul` - Умножение (a * b)
- `div` - Деление (a / b, връща NaN ако b = 0)

## API Референция

### GET /calculate

**Параметри:**
- `a` (задължителен): Първо число (double)
- `b` (задължителен): Второ число (double)
- `op` (задължителен): Операция (`add`, `sub`, `mul`, `div`)

**Отговор:**
- Content-Type: `text/event-stream`
- Връща Server-Sent Events с прогреса на изчислението и резултата

**Примерна заявка:**
```
GET /calculate?a=7&b=5&op=mul HTTP/1.1
Host: localhost:8080
Accept: text/event-stream
```

**Примерен отговор:**
```
event: info
data: Calculating: 7.0 mul 5.0

event: result
data: 35.0
```

## Отстраняване на проблеми

### Чести проблеми

1. **Порт 8080 вече е зает**
   - Затворете други приложения, които използват порт 8080
   - Или променете порта на сървъра в `calculator-server/src/main/resources/application.yml`

2. **Връзката е отказана**
   - Уверете се, че сървърът работи преди да стартирате клиента
   - Проверете дали сървърът е стартирал успешно на порт 8080

3. **Проблеми с имената на параметрите**
   - Този проект включва Maven конфигурация за компилатора с флага `-parameters`
   - Ако имате проблеми с обвързването на параметрите, уверете се, че проектът е компилиран с тази настройка

### Спиране на приложенията

- Натиснете `Ctrl+C` в терминала, където работи всяко приложение
- Или използвайте `mvn spring-boot:stop`, ако работят като фонов процес

## Технологичен стек

- **Spring Boot 3.3.1** - Фреймуърк за приложения
- **Spring WebFlux** - Реактивен уеб фреймуърк
- **Project Reactor** - Библиотека за реактивни потоци
- **Netty** - Сървър с неблокиращ I/O
- **Maven** - Инструмент за билдване
- **Java 17+** - Програмен език

## Следващи стъпки

Опитайте да промените кода, за да:
- Добавите още математически операции
- Включите обработка на грешки при невалидни операции
- Добавите логване на заявки и отговори
- Реализирате автентикация
- Добавите unit тестове

**Отказ от отговорност**:  
Този документ е преведен с помощта на AI преводаческа услуга [Co-op Translator](https://github.com/Azure/co-op-translator). Въпреки че се стремим към точност, моля, имайте предвид, че автоматизираните преводи могат да съдържат грешки или неточности. Оригиналният документ на неговия роден език трябва да се счита за авторитетен източник. За критична информация се препоръчва професионален човешки превод. Ние не носим отговорност за каквито и да е недоразумения или неправилни тълкувания, произтичащи от използването на този превод.