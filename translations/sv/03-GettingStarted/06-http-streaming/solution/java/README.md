# Calculator HTTP Streaming Demo

Det här projektet visar HTTP-streaming med Server-Sent Events (SSE) med Spring Boot WebFlux. Det består av två applikationer:

- **Calculator Server**: En reaktiv webbtjänst som utför beräkningar och streamar resultat med SSE
- **Calculator Client**: En klientapplikation som konsumerar streaming-endpointen

## Förutsättningar

- Java 17 eller högre
- Maven 3.6 eller högre

## Projektstruktur

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

## Hur det fungerar

1. **Calculator Server** exponerar en `/calculate`-endpoint som:
   - Tar emot query-parametrar: `a` (nummer), `b` (nummer), `op` (operation)
   - Stödda operationer: `add`, `sub`, `mul`, `div`
   - Returnerar Server-Sent Events med beräkningsprogress och resultat

2. **Calculator Client** ansluter till servern och:
   - Skickar en förfrågan för att beräkna `7 * 5`
   - Konsumerar den strömmande responsen
   - Skriver ut varje event i konsolen

## Köra applikationerna

### Alternativ 1: Använda Maven (rekommenderas)

#### 1. Starta Calculator Server

Öppna en terminal och navigera till servermappen:

```bash
cd calculator-server
mvn clean package
mvn spring-boot:run
```

Servern startar på `http://localhost:8080`

Du bör se output som:
```
Started CalculatorServerApplication in X.XXX seconds
Netty started on port 8080 (http)
```

#### 2. Kör Calculator Client

Öppna en **ny terminal** och navigera till klientmappen:

```bash
cd calculator-client
mvn clean package
mvn spring-boot:run
```

Klienten ansluter till servern, utför beräkningen och visar de strömmande resultaten.

### Alternativ 2: Använda Java direkt

#### 1. Kompilera och kör servern:

```bash
cd calculator-server
mvn clean package
java -jar target/calculator-server-0.0.1-SNAPSHOT.jar
```

#### 2. Kompilera och kör klienten:

```bash
cd calculator-client
mvn clean package
java -jar target/calculator-client-0.0.1-SNAPSHOT.jar
```

## Testa servern manuellt

Du kan också testa servern med en webbläsare eller curl:

### Med webbläsare:
Besök: `http://localhost:8080/calculate?a=10&b=5&op=add`

### Med curl:
```bash
curl "http://localhost:8080/calculate?a=10&b=5&op=add" -H "Accept: text/event-stream"
```

## Förväntad output

När du kör klienten bör du se strömmande output liknande:

```
event:info
data:Calculating: 7.0 mul 5.0

event:result
data:35.0
```

## Stödda operationer

- `add` - Addition (a + b)
- `sub` - Subtraktion (a - b)
- `mul` - Multiplikation (a * b)
- `div` - Division (a / b, returnerar NaN om b = 0)

## API-referens

### GET /calculate

**Parametrar:**
- `a` (obligatorisk): Första talet (double)
- `b` (obligatorisk): Andra talet (double)
- `op` (obligatorisk): Operation (`add`, `sub`, `mul`, `div`)

**Svar:**
- Content-Type: `text/event-stream`
- Returnerar Server-Sent Events med beräkningsprogress och resultat

**Exempel på förfrågan:**
```
GET /calculate?a=7&b=5&op=mul HTTP/1.1
Host: localhost:8080
Accept: text/event-stream
```

**Exempel på svar:**
```
event: info
data: Calculating: 7.0 mul 5.0

event: result
data: 35.0
```

## Felsökning

### Vanliga problem

1. **Port 8080 används redan**
   - Stoppa andra applikationer som använder port 8080
   - Eller ändra serverporten i `calculator-server/src/main/resources/application.yml`

2. **Connection refused**
   - Kontrollera att servern körs innan klienten startas
   - Kontrollera att servern startade korrekt på port 8080

3. **Problem med parameter-namn**
   - Projektet inkluderar Maven-kompilatorinställning med flaggan `-parameters`
   - Om du får problem med parameterbindning, se till att projektet byggs med denna konfiguration

### Stoppa applikationerna

- Tryck `Ctrl+C` i terminalen där varje applikation körs
- Eller använd `mvn spring-boot:stop` om de körs som bakgrundsprocess

## Teknologistack

- **Spring Boot 3.3.1** - Applikationsramverk
- **Spring WebFlux** - Reaktivt webb-ramverk
- **Project Reactor** - Bibliotek för reaktiva streams
- **Netty** - Icke-blockerande I/O-server
- **Maven** - Byggverktyg
- **Java 17+** - Programmeringsspråk

## Nästa steg

Testa att ändra koden för att:
- Lägga till fler matematiska operationer
- Inkludera felhantering för ogiltiga operationer
- Lägga till loggning av förfrågningar/svar
- Implementera autentisering
- Lägga till enhetstester

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, vänligen observera att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår vid användning av denna översättning.