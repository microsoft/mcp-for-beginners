# Calculator HTTP Streaming Demo

Dis project dey show how HTTP streaming dey work wit Server-Sent Events (SSE) for Spring Boot WebFlux. E get two applications:

- **Calculator Server**: Na reactive web service wey dey do calculation and dey stream result wit SSE
- **Calculator Client**: Na client application wey dey use di streaming endpoint

## Wetin You Need

- Java 17 or higher
- Maven 3.6 or higher

## Project Structure

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

## How E Dey Work

1. Di **Calculator Server** dey expose `/calculate` endpoint wey:
   - Dey accept query parameters: `a` (number), `b` (number), `op` (operation)
   - Di operations wey e support na: `add`, `sub`, `mul`, `div`
   - E dey return Server-Sent Events wey get calculation progress and result

2. Di **Calculator Client** dey connect to di server and:
   - E go make request to calculate `7 * 5`
   - E go dey use di streaming response
   - E go print each event for console

## How To Run Di Applications

### Option 1: Use Maven (E Better Pass)

#### 1. Start Di Calculator Server

Open terminal and go di server directory:

```bash
cd calculator-server
mvn clean package
mvn spring-boot:run
```

Di server go start for `http://localhost:8080`

You go see output like dis:
```
Started CalculatorServerApplication in X.XXX seconds
Netty started on port 8080 (http)
```

#### 2. Run Di Calculator Client

Open **new terminal** and go di client directory:

```bash
cd calculator-client
mvn clean package
mvn spring-boot:run
```

Di client go connect to di server, do di calculation, and show di streaming results.

### Option 2: Use Java Directly

#### 1. Compile and run di server:

```bash
cd calculator-server
mvn clean package
java -jar target/calculator-server-0.0.1-SNAPSHOT.jar
```

#### 2. Compile and run di client:

```bash
cd calculator-client
mvn clean package
java -jar target/calculator-client-0.0.1-SNAPSHOT.jar
```

## How To Test Di Server Manually

You fit test di server wit web browser or curl:

### Use web browser:
Go: `http://localhost:8080/calculate?a=10&b=5&op=add`

### Use curl:
```bash
curl "http://localhost:8080/calculate?a=10&b=5&op=add" -H "Accept: text/event-stream"
```

## Wetin You Go See As Output

When di client dey run, you go see streaming output wey be like dis:

```
event:info
data:Calculating: 7.0 mul 5.0

event:result
data:35.0
```

## Di Operations Weh E Support

- `add` - Addition (a + b)
- `sub` - Subtraction (a - b)
- `mul` - Multiplication (a * b)
- `div` - Division (a / b, e go return NaN if b = 0)

## API Reference

### GET /calculate

**Parameters:**
- `a` (required): First number (double)
- `b` (required): Second number (double)
- `op` (required): Operation (`add`, `sub`, `mul`, `div`)

**Response:**
- Content-Type: `text/event-stream`
- E dey return Server-Sent Events wey get calculation progress and result

**Example Request:**
```
GET /calculate?a=7&b=5&op=mul HTTP/1.1
Host: localhost:8080
Accept: text/event-stream
```

**Example Response:**
```
event: info
data: Calculating: 7.0 mul 5.0

event: result
data: 35.0
```

## How To Solve Problems

### Common Wahala

1. **Port 8080 don already dey use**
   - Stop any other application wey dey use port 8080
   - Or change di server port for `calculator-server/src/main/resources/application.yml`

2. **Connection no work**
   - Make sure say di server dey run before you start di client
   - Check say di server start well for port 8080

3. **Parameter name wahala**
   - Dis project get Maven compiler configuration wit `-parameters` flag
   - If you see parameter binding wahala, make sure say di project build wit dis configuration

### How To Stop Di Applications

- Press `Ctrl+C` for di terminal wey each application dey run
- Or use `mvn spring-boot:stop` if e dey run as background process

## Technology Stack

- **Spring Boot 3.3.1** - Application framework
- **Spring WebFlux** - Reactive web framework
- **Project Reactor** - Reactive streams library
- **Netty** - Non-blocking I/O server
- **Maven** - Build tool
- **Java 17+** - Programming language

## Wetin You Fit Do Next

Try change di code to:
- Add more mathematical operations
- Put error handling for invalid operations
- Add request/response logging
- Do authentication
- Add unit tests

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Dis dokyument don translate wit AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). Even as we dey try make am accurate, abeg sabi say automated translations fit get mistake or no correct well. Di original dokyument for im native language na di main source wey you go fit trust. For important mata, e good make professional human translation dey use. We no go fit take blame for any misunderstanding or wrong interpretation wey fit happen because you use dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->