# Calculator HTTP Streaming Demo

Ipinapakita ng proyektong ito ang HTTP streaming gamit ang Server-Sent Events (SSE) sa Spring Boot WebFlux. Binubuo ito ng dalawang aplikasyon:

- **Calculator Server**: Isang reactive web service na nagsasagawa ng mga kalkulasyon at nag-stream ng mga resulta gamit ang SSE
- **Calculator Client**: Isang client application na kumokonsumo sa streaming endpoint

## Prerequisites

- Java 17 o mas mataas
- Maven 3.6 o mas mataas

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

## Paano Ito Gumagana

1. Ang **Calculator Server** ay nag-eexpose ng `/calculate` endpoint na:
   - Tumanggap ng mga query parameter: `a` (numero), `b` (numero), `op` (operasyon)
   - Sinusuportahang mga operasyon: `add`, `sub`, `mul`, `div`
   - Nagbabalik ng Server-Sent Events na may progreso ng kalkulasyon at resulta

2. Ang **Calculator Client** ay kumokonekta sa server at:
   - Gumagawa ng request para kalkulahin ang `7 * 5`
   - Kinokonsumo ang streaming response
   - Ipinapakita ang bawat event sa console

## Pagpapatakbo ng mga Aplikasyon

### Opsyon 1: Gamit ang Maven (Inirerekomenda)

#### 1. Simulan ang Calculator Server

Buksan ang terminal at pumunta sa server directory:

```bash
cd calculator-server
mvn clean package
mvn spring-boot:run
```

Magsisimula ang server sa `http://localhost:8080`

Makikita mo ang output na tulad nito:
```
Started CalculatorServerApplication in X.XXX seconds
Netty started on port 8080 (http)
```

#### 2. Patakbuhin ang Calculator Client

Buksan ang **bagong terminal** at pumunta sa client directory:

```bash
cd calculator-client
mvn clean package
mvn spring-boot:run
```

Kokonekta ang client sa server, gagawin ang kalkulasyon, at ipapakita ang streaming na mga resulta.

### Opsyon 2: Direktang Gamitin ang Java

#### 1. I-compile at patakbuhin ang server:

```bash
cd calculator-server
mvn clean package
java -jar target/calculator-server-0.0.1-SNAPSHOT.jar
```

#### 2. I-compile at patakbuhin ang client:

```bash
cd calculator-client
mvn clean package
java -jar target/calculator-client-0.0.1-SNAPSHOT.jar
```

## Pagsubok sa Server nang Manwal

Maaari mo ring subukan ang server gamit ang web browser o curl:

### Gamit ang web browser:
Bisitahin: `http://localhost:8080/calculate?a=10&b=5&op=add`

### Gamit ang curl:
```bash
curl "http://localhost:8080/calculate?a=10&b=5&op=add" -H "Accept: text/event-stream"
```

## Inaasahang Output

Kapag pinatakbo ang client, makikita mo ang streaming output na katulad nito:

```
event:info
data:Calculating: 7.0 mul 5.0

event:result
data:35.0
```

## Sinusuportahang Mga Operasyon

- `add` - Pagdaragdag (a + b)
- `sub` - Pagbabawas (a - b)
- `mul` - Pagmumultiply (a * b)
- `div` - Pagdidibide (a / b, magbabalik ng NaN kung b = 0)

## API Reference

### GET /calculate

**Mga Parameter:**
- `a` (kailangan): Unang numero (double)
- `b` (kailangan): Pangalawang numero (double)
- `op` (kailangan): Operasyon (`add`, `sub`, `mul`, `div`)

**Sagot:**
- Content-Type: `text/event-stream`
- Nagbabalik ng Server-Sent Events na may progreso ng kalkulasyon at resulta

**Halimbawang Request:**
```
GET /calculate?a=7&b=5&op=mul HTTP/1.1
Host: localhost:8080
Accept: text/event-stream
```

**Halimbawang Sagot:**
```
event: info
data: Calculating: 7.0 mul 5.0

event: result
data: 35.0
```

## Pag-aayos ng Problema

### Karaniwang Isyu

1. **Port 8080 ay ginagamit na**
   - Itigil ang ibang aplikasyon na gumagamit ng port 8080
   - O palitan ang port ng server sa `calculator-server/src/main/resources/application.yml`

2. **Connection refused**
   - Siguraduhing tumatakbo ang server bago simulan ang client
   - Tiyaking matagumpay na nagsimula ang server sa port 8080

3. **Mga isyu sa pangalan ng parameter**
   - Kasama sa proyektong ito ang Maven compiler configuration na may `-parameters` flag
   - Kung may problema sa parameter binding, siguraduhing na-build ang proyekto gamit ang configuration na ito

### Pagtigil sa mga Aplikasyon

- Pindutin ang `Ctrl+C` sa terminal kung saan tumatakbo ang bawat aplikasyon
- O gamitin ang `mvn spring-boot:stop` kung tumatakbo bilang background process

## Technology Stack

- **Spring Boot 3.3.1** - Application framework
- **Spring WebFlux** - Reactive web framework
- **Project Reactor** - Reactive streams library
- **Netty** - Non-blocking I/O server
- **Maven** - Build tool
- **Java 17+** - Programming language

## Susunod na Hakbang

Subukang baguhin ang code para:
- Magdagdag ng mas maraming mathematical operations
- Isama ang error handling para sa mga invalid na operasyon
- Magdagdag ng request/response logging
- Mag-implement ng authentication
- Magdagdag ng unit tests

**Paalala**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagamat nagsusumikap kami para sa katumpakan, pakatandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o di-tumpak na impormasyon. Ang orihinal na dokumento sa kanyang sariling wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na maaaring magmula sa paggamit ng pagsasaling ito.