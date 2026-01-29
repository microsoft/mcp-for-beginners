# Calculator HTTP Streaming Demo

ਇਹ ਪ੍ਰੋਜੈਕਟ Server-Sent Events (SSE) ਦੀ ਵਰਤੋਂ ਕਰਕੇ HTTP ਸਟ੍ਰੀਮਿੰਗ ਨੂੰ Spring Boot WebFlux ਨਾਲ ਦਰਸਾਉਂਦਾ ਹੈ। ਇਹ ਦੋ ਐਪਲੀਕੇਸ਼ਨਾਂ 'ਤੇ مشتمل ਹੈ:

- **Calculator Server**: ਇੱਕ ਰੀਐਕਟਿਵ ਵੈੱਬ ਸਰਵਿਸ ਜੋ ਗਣਨਾਵਾਂ ਕਰਦੀ ਹੈ ਅਤੇ SSE ਰਾਹੀਂ ਨਤੀਜੇ ਸਟ੍ਰੀਮ ਕਰਦੀ ਹੈ  
- **Calculator Client**: ਇੱਕ ਕਲਾਇੰਟ ਐਪਲੀਕੇਸ਼ਨ ਜੋ ਸਟ੍ਰੀਮਿੰਗ ਐਂਡਪੌਇੰਟ ਨੂੰ ਵਰਤਦਾ ਹੈ

## Prerequisites

- Java 17 ਜਾਂ ਇਸ ਤੋਂ ਉੱਪਰ  
- Maven 3.6 ਜਾਂ ਇਸ ਤੋਂ ਉੱਪਰ  

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

## ਇਹ ਕਿਵੇਂ ਕੰਮ ਕਰਦਾ ਹੈ

1. **Calculator Server** `/calculate` ਐਂਡਪੌਇੰਟ ਪ੍ਰਦਾਨ ਕਰਦਾ ਹੈ ਜੋ:  
   - ਕਵੈਰੀ ਪੈਰਾਮੀਟਰ ਲੈਂਦਾ ਹੈ: `a` (ਨੰਬਰ), `b` (ਨੰਬਰ), `op` (ਆਪਰੇਸ਼ਨ)  
   - ਸਮਰਥਿਤ ਆਪਰੇਸ਼ਨ: `add`, `sub`, `mul`, `div`  
   - ਗਣਨਾ ਦੀ ਪ੍ਰਗਤੀ ਅਤੇ ਨਤੀਜੇ ਨਾਲ Server-Sent Events ਵਾਪਸ ਕਰਦਾ ਹੈ  

2. **Calculator Client** ਸਰਵਰ ਨਾਲ ਜੁੜਦਾ ਹੈ ਅਤੇ:  
   - `7 * 5` ਦੀ ਗਣਨਾ ਲਈ ਬੇਨਤੀ ਕਰਦਾ ਹੈ  
   - ਸਟ੍ਰੀਮਿੰਗ ਜਵਾਬ ਨੂੰ ਵਰਤਦਾ ਹੈ  
   - ਹਰ ਇਕ ਇਵੈਂਟ ਨੂੰ ਕਨਸੋਲ 'ਤੇ ਪ੍ਰਿੰਟ ਕਰਦਾ ਹੈ  

## ਐਪਲੀਕੇਸ਼ਨਾਂ ਚਲਾਉਣਾ

### ਵਿਕਲਪ 1: Maven ਦੀ ਵਰਤੋਂ ਕਰਕੇ (ਸਿਫਾਰਸ਼ੀ)

#### 1. Calculator Server ਸ਼ੁਰੂ ਕਰੋ

ਇੱਕ ਟਰਮੀਨਲ ਖੋਲ੍ਹੋ ਅਤੇ ਸਰਵਰ ਡਾਇਰੈਕਟਰੀ ਵਿੱਚ ਜਾਓ:

```bash
cd calculator-server
mvn clean package
mvn spring-boot:run
```

ਸਰਵਰ `http://localhost:8080` 'ਤੇ ਚੱਲੇਗਾ

ਤੁਹਾਨੂੰ ਇਸ ਤਰ੍ਹਾਂ ਦਾ ਆਉਟਪੁੱਟ ਵੇਖਣ ਨੂੰ ਮਿਲੇਗਾ:  
```
Started CalculatorServerApplication in X.XXX seconds
Netty started on port 8080 (http)
```

#### 2. Calculator Client ਚਲਾਓ

ਇੱਕ **ਨਵਾਂ ਟਰਮੀਨਲ** ਖੋਲ੍ਹੋ ਅਤੇ ਕਲਾਇੰਟ ਡਾਇਰੈਕਟਰੀ ਵਿੱਚ ਜਾਓ:

```bash
cd calculator-client
mvn clean package
mvn spring-boot:run
```

ਕਲਾਇੰਟ ਸਰਵਰ ਨਾਲ ਜੁੜੇਗਾ, ਗਣਨਾ ਕਰੇਗਾ ਅਤੇ ਸਟ੍ਰੀਮਿੰਗ ਨਤੀਜੇ ਦਿਖਾਏਗਾ।

### ਵਿਕਲਪ 2: ਸਿੱਧਾ Java ਦੀ ਵਰਤੋਂ ਕਰਕੇ

#### 1. ਸਰਵਰ ਕੰਪਾਇਲ ਅਤੇ ਚਲਾਓ:

```bash
cd calculator-server
mvn clean package
java -jar target/calculator-server-0.0.1-SNAPSHOT.jar
```

#### 2. ਕਲਾਇੰਟ ਕੰਪਾਇਲ ਅਤੇ ਚਲਾਓ:

```bash
cd calculator-client
mvn clean package
java -jar target/calculator-client-0.0.1-SNAPSHOT.jar
```

## ਸਰਵਰ ਨੂੰ ਮੈਨੁਅਲੀ ਟੈਸਟ ਕਰਨਾ

ਤੁਸੀਂ ਸਰਵਰ ਨੂੰ ਵੈੱਬ ਬ੍ਰਾਊਜ਼ਰ ਜਾਂ curl ਨਾਲ ਵੀ ਟੈਸਟ ਕਰ ਸਕਦੇ ਹੋ:

### ਵੈੱਬ ਬ੍ਰਾਊਜ਼ਰ ਦੀ ਵਰਤੋਂ ਕਰਕੇ:  
ਵਿਜ਼ਿਟ ਕਰੋ: `http://localhost:8080/calculate?a=10&b=5&op=add`

### curl ਦੀ ਵਰਤੋਂ ਕਰਕੇ:  
```bash
curl "http://localhost:8080/calculate?a=10&b=5&op=add" -H "Accept: text/event-stream"
```

## ਉਮੀਦ ਕੀਤੀ ਆਉਟਪੁੱਟ

ਜਦੋਂ ਕਲਾਇੰਟ ਚੱਲ ਰਿਹਾ ਹੋਵੇ, ਤੁਹਾਨੂੰ ਇਸ ਤਰ੍ਹਾਂ ਦਾ ਸਟ੍ਰੀਮਿੰਗ ਆਉਟਪੁੱਟ ਵੇਖਣ ਨੂੰ ਮਿਲੇਗਾ:

```
event:info
data:Calculating: 7.0 mul 5.0

event:result
data:35.0
```

## ਸਮਰਥਿਤ ਆਪਰੇਸ਼ਨ

- `add` - ਜੋੜ (a + b)  
- `sub` - ਘਟਾਓ (a - b)  
- `mul` - ਗੁਣਾ (a * b)  
- `div` - ਭਾਗ (a / b, ਜੇ b = 0 ਤਾਂ NaN ਵਾਪਸ ਕਰਦਾ ਹੈ)  

## API ਸੰਦਰਭ

### GET /calculate

**ਪੈਰਾਮੀਟਰ:**  
- `a` (ਲਾਜ਼ਮੀ): ਪਹਿਲਾ ਨੰਬਰ (double)  
- `b` (ਲਾਜ਼ਮੀ): ਦੂਜਾ ਨੰਬਰ (double)  
- `op` (ਲਾਜ਼ਮੀ): ਆਪਰੇਸ਼ਨ (`add`, `sub`, `mul`, `div`)  

**ਜਵਾਬ:**  
- Content-Type: `text/event-stream`  
- ਗਣਨਾ ਦੀ ਪ੍ਰਗਤੀ ਅਤੇ ਨਤੀਜੇ ਨਾਲ Server-Sent Events ਵਾਪਸ ਕਰਦਾ ਹੈ  

**ਉਦਾਹਰਨ ਬੇਨਤੀ:**  
```
GET /calculate?a=7&b=5&op=mul HTTP/1.1
Host: localhost:8080
Accept: text/event-stream
```

**ਉਦਾਹਰਨ ਜਵਾਬ:**  
```
event: info
data: Calculating: 7.0 mul 5.0

event: result
data: 35.0
```

## ਸਮੱਸਿਆਵਾਂ ਦਾ ਹੱਲ

### ਆਮ ਸਮੱਸਿਆਵਾਂ

1. **ਪੋਰਟ 8080 ਪਹਿਲਾਂ ਹੀ ਵਰਤ ਰਿਹਾ ਹੈ**  
   - ਪੋਰਟ 8080 ਵਰਤ ਰਹੀਆਂ ਹੋਰ ਐਪਲੀਕੇਸ਼ਨਾਂ ਨੂੰ ਬੰਦ ਕਰੋ  
   - ਜਾਂ `calculator-server/src/main/resources/application.yml` ਵਿੱਚ ਸਰਵਰ ਪੋਰਟ ਬਦਲੋ  

2. **ਕਨੈਕਸ਼ਨ ਰੱਦ ਹੋ ਗਿਆ**  
   - ਕਲਾਇੰਟ ਚਲਾਉਣ ਤੋਂ ਪਹਿਲਾਂ ਯਕੀਨੀ ਬਣਾਓ ਕਿ ਸਰਵਰ ਚੱਲ ਰਿਹਾ ਹੈ  
   - ਚੈੱਕ ਕਰੋ ਕਿ ਸਰਵਰ ਸਫਲਤਾਪੂਰਵਕ ਪੋਰਟ 8080 'ਤੇ ਚੱਲ ਰਿਹਾ ਹੈ  

3. **ਪੈਰਾਮੀਟਰ ਨਾਮਾਂ ਦੀ ਸਮੱਸਿਆ**  
   - ਇਸ ਪ੍ਰੋਜੈਕਟ ਵਿੱਚ Maven ਕੰਪਾਇਲਰ ਕਨਫਿਗਰੇਸ਼ਨ `-parameters` ਫਲੈਗ ਨਾਲ ਸ਼ਾਮਲ ਹੈ  
   - ਜੇ ਪੈਰਾਮੀਟਰ ਬਾਈਂਡਿੰਗ ਸਮੱਸਿਆ ਆਵੇ, ਤਾਂ ਯਕੀਨੀ ਬਣਾਓ ਕਿ ਪ੍ਰੋਜੈਕਟ ਇਸ ਕਨਫਿਗਰੇਸ਼ਨ ਨਾਲ ਬਣਾਇਆ ਗਿਆ ਹੈ  

### ਐਪਲੀਕੇਸ਼ਨਾਂ ਨੂੰ ਰੋਕਣਾ

- ਜਿੱਥੇ ਹਰ ਐਪਲੀਕੇਸ਼ਨ ਚੱਲ ਰਹੀ ਹੈ, ਉਸ ਟਰਮੀਨਲ ਵਿੱਚ `Ctrl+C` ਦਬਾਓ  
- ਜਾਂ ਜੇ ਬੈਕਗ੍ਰਾਊਂਡ ਪ੍ਰਕਿਰਿਆ ਵਜੋਂ ਚੱਲ ਰਹੀ ਹੈ ਤਾਂ `mvn spring-boot:stop` ਵਰਤੋਂ  

## ਤਕਨਾਲੋਜੀ ਸਟੈਕ

- **Spring Boot 3.3.1** - ਐਪਲੀਕੇਸ਼ਨ ਫਰੇਮਵਰਕ  
- **Spring WebFlux** - ਰੀਐਕਟਿਵ ਵੈੱਬ ਫਰੇਮਵਰਕ  
- **Project Reactor** - ਰੀਐਕਟਿਵ ਸਟ੍ਰੀਮ ਲਾਇਬ੍ਰੇਰੀ  
- **Netty** - ਨਾਨ-ਬਲਾਕਿੰਗ I/O ਸਰਵਰ  
- **Maven** - ਬਿਲਡ ਟੂਲ  
- **Java 17+** - ਪ੍ਰੋਗ੍ਰਾਮਿੰਗ ਭਾਸ਼ਾ  

## ਅਗਲੇ ਕਦਮ

ਕੋਡ ਵਿੱਚ ਤਬਦੀਲੀ ਕਰਕੇ ਕੋਸ਼ਿਸ਼ ਕਰੋ:  
- ਹੋਰ ਗਣਿਤੀ ਆਪਰੇਸ਼ਨ ਸ਼ਾਮਲ ਕਰੋ  
- ਗਲਤ ਆਪਰੇਸ਼ਨਾਂ ਲਈ ਐਰਰ ਹੈਂਡਲਿੰਗ ਸ਼ਾਮਲ ਕਰੋ  
- ਬੇਨਤੀ/ਜਵਾਬ ਲੌਗਿੰਗ ਸ਼ਾਮਲ ਕਰੋ  
- ਪ੍ਰਮਾਣਿਕਤਾ ਲਾਗੂ ਕਰੋ  
- ਯੂਨਿਟ ਟੈਸਟ ਸ਼ਾਮਲ ਕਰੋ

**ਅਸਵੀਕਾਰੋਪਣ**:  
ਇਹ ਦਸਤਾਵੇਜ਼ AI ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਅਨੁਵਾਦਿਤ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀਅਤ ਲਈ ਕੋਸ਼ਿਸ਼ ਕਰਦੇ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਰੱਖੋ ਕਿ ਸਵੈਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸਮਰਥਤਾਵਾਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਮੂਲ ਦਸਤਾਵੇਜ਼ ਆਪਣੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਪ੍ਰਮਾਣਿਕ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਮਹੱਤਵਪੂਰਨ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਅਸੀਂ ਇਸ ਅਨੁਵਾਦ ਦੀ ਵਰਤੋਂ ਤੋਂ ਉਤਪੰਨ ਕਿਸੇ ਵੀ ਗਲਤਫਹਿਮੀ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆ ਲਈ ਜ਼ਿੰਮੇਵਾਰ ਨਹੀਂ ਹਾਂ।