# Calculator HTTP Streaming Demo

Овај пројекат демонстрира HTTP стриминг користећи Server-Sent Events (SSE) са Spring Boot WebFlux. Састоји се из две апликације:

- **Calculator Server**: реактивни веб сервис који изводи прорачуне и стримује резултате користећи SSE
- **Calculator Client**: клијент апликација која конзумира стриминг крајњу тачку

## Претпоставке

- Java 17 или новија верзија
- Maven 3.6 или новија верзија

## Структура пројекта

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

## Како ради

1. **Calculator Server** излаже `/calculate` крајњу тачку која:
   - Прихвата query параметре: `a` (број), `b` (број), `op` (операција)
   - Подржане операције: `add`, `sub`, `mul`, `div`
   - Враћа Server-Sent Events са напретком прорачуна и резултатом

2. **Calculator Client** се повезује на сервер и:
   - Слаже захтев за прорачун `7 * 5`
   - Конзумира стриминг одговор
   - Исписује сваки догађај у конзолу

## Покретање апликација

### Опција 1: Коришћење Mavena (препоручено)

#### 1. Покрени Calculator Server

Отвори терминал и иди у директоријум сервера:

```bash
cd calculator-server
mvn clean package
mvn spring-boot:run
```

Сервер ће се покренути на `http://localhost:8080`

Требало би да видиш излаз сличан овоме:
```
Started CalculatorServerApplication in X.XXX seconds
Netty started on port 8080 (http)
```

#### 2. Покрени Calculator Client

Отвори **нови терминал** и иди у директоријум клијента:

```bash
cd calculator-client
mvn clean package
mvn spring-boot:run
```

Клијент ће се повезати на сервер, извршити прорачун и приказати стриминг резултате.

### Опција 2: Коришћење Јаве директно

#### 1. Компајлирај и покрени сервер:

```bash
cd calculator-server
mvn clean package
java -jar target/calculator-server-0.0.1-SNAPSHOT.jar
```

#### 2. Компајлирај и покрени клијента:

```bash
cd calculator-client
mvn clean package
java -jar target/calculator-client-0.0.1-SNAPSHOT.jar
```

## Ручно тестирање сервера

Такође можете тестирати сервер преко веб прегледача или curl-а:

### Коришћење веб прегледача:
Посетите: `http://localhost:8080/calculate?a=10&b=5&op=add`

### Коришћење curl-а:
```bash
curl "http://localhost:8080/calculate?a=10&b=5&op=add" -H "Accept: text/event-stream"
```

## Очекивани излаз

Када покренете клијента, требало би да видите стриминг излаз сличан овоме:

```
event:info
data:Calculating: 7.0 mul 5.0

event:result
data:35.0
```

## Подржане операције

- `add` - Сабирање (a + b)
- `sub` - Одузимање (a - b)
- `mul` - Множење (a * b)
- `div` - Дељење (a / b, враћа NaN ако је b = 0)

## API референца

### GET /calculate

**Параметри:**
- `a` (обавезно): Први број (double)
- `b` (обавезно): Други број (double)
- `op` (обавезно): Операција (`add`, `sub`, `mul`, `div`)

**Одговор:**
- Content-Type: `text/event-stream`
- Враћа Server-Sent Events са напретком прорачуна и резултатом

**Пример захтева:**
```
GET /calculate?a=7&b=5&op=mul HTTP/1.1
Host: localhost:8080
Accept: text/event-stream
```

**Пример одговора:**
```
event: info
data: Calculating: 7.0 mul 5.0

event: result
data: 35.0
```

## Решавање проблема

### Чести проблеми

1. **Порт 8080 је већ у употреби**
   - Зауставите све друге апликације које користе порт 8080
   - Или промените порт сервера у `calculator-server/src/main/resources/application.yml`

2. **Повезивање одбијено**
   - Уверите се да је сервер покренут пре него што покренете клијента
   - Проверите да ли се сервер успешно покренуо на порту 8080

3. **Проблеми са именима параметара**
   - Овај пројекат укључује Maven конфигурацију компајлера са `-parameters` заставицом
   - Ако наиђете на проблеме са везивањем параметара, уверите се да је пројекат изграђен са овом конфигурацијом

### Заустављање апликација

- Притисните `Ctrl+C` у терминалу у коме је апликација покренута
- Или користите `mvn spring-boot:stop` ако се покреће као позадински процес

## Технолошки стек

- **Spring Boot 3.3.1** - Апликациони фрејмворк
- **Spring WebFlux** - Реактивни веб фрејмворк
- **Project Reactor** - Библиотека за реактивне стримове
- **Netty** - Сервер за не-блокирајући улаз/излаз
- **Maven** - Алат за изградњу
- **Java 17+** - Програмски језик

## Следећи кораци

Пробајте да измените код да:
- Додате више математичких операција
- Укључите обраду грешака за неважеће операције
- Додате логовање захтева/одговора
- Имплементирате аутентификацију
- Додате јединичне тестове

**Одрицање од одговорности**:  
Овај документ је преведен коришћењем AI преводилачке услуге [Co-op Translator](https://github.com/Azure/co-op-translator). Иако се трудимо да превод буде тачан, молимо вас да имате у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати ауторитетним извором. За критичне информације препоручује се професионални људски превод. Нисмо одговорни за било каква неспоразума или погрешна тумачења која произилазе из коришћења овог превода.