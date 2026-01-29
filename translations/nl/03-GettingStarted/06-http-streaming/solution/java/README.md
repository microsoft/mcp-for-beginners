# Calculator HTTP Streaming Demo

Dit project demonstreert HTTP streaming met Server-Sent Events (SSE) in Spring Boot WebFlux. Het bestaat uit twee applicaties:

- **Calculator Server**: Een reactieve webservice die berekeningen uitvoert en resultaten streamt via SSE
- **Calculator Client**: Een clientapplicatie die de streaming endpoint consumeert

## Vereisten

- Java 17 of hoger
- Maven 3.6 of hoger

## Projectstructuur

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

## Hoe het werkt

1. De **Calculator Server** biedt een `/calculate` endpoint dat:
   - Queryparameters accepteert: `a` (getal), `b` (getal), `op` (bewerking)
   - Ondersteunde bewerkingen: `add`, `sub`, `mul`, `div`
   - Server-Sent Events teruggeeft met voortgang en resultaat van de berekening

2. De **Calculator Client** maakt verbinding met de server en:
   - Stuurt een verzoek om `7 * 5` te berekenen
   - Consumeert de streaming response
   - Drukt elk event af in de console

## Applicaties starten

### Optie 1: Met Maven (aanbevolen)

#### 1. Start de Calculator Server

Open een terminal en ga naar de servermap:

```bash
cd calculator-server
mvn clean package
mvn spring-boot:run
```

De server start op `http://localhost:8080`

Je zou output moeten zien zoals:
```
Started CalculatorServerApplication in X.XXX seconds
Netty started on port 8080 (http)
```

#### 2. Start de Calculator Client

Open een **nieuwe terminal** en ga naar de clientmap:

```bash
cd calculator-client
mvn clean package
mvn spring-boot:run
```

De client maakt verbinding met de server, voert de berekening uit en toont de streaming resultaten.

### Optie 2: Java direct gebruiken

#### 1. Compileer en start de server:

```bash
cd calculator-server
mvn clean package
java -jar target/calculator-server-0.0.1-SNAPSHOT.jar
```

#### 2. Compileer en start de client:

```bash
cd calculator-client
mvn clean package
java -jar target/calculator-client-0.0.1-SNAPSHOT.jar
```

## Server handmatig testen

Je kunt de server ook testen met een webbrowser of curl:

### Met een webbrowser:
Bezoek: `http://localhost:8080/calculate?a=10&b=5&op=add`

### Met curl:
```bash
curl "http://localhost:8080/calculate?a=10&b=5&op=add" -H "Accept: text/event-stream"
```

## Verwachte output

Bij het draaien van de client zie je streaming output vergelijkbaar met:

```
event:info
data:Calculating: 7.0 mul 5.0

event:result
data:35.0
```

## Ondersteunde bewerkingen

- `add` - Optellen (a + b)
- `sub` - Aftrekken (a - b)
- `mul` - Vermenigvuldigen (a * b)
- `div` - Delen (a / b, geeft NaN als b = 0)

## API Referentie

### GET /calculate

**Parameters:**
- `a` (verplicht): Eerste getal (double)
- `b` (verplicht): Tweede getal (double)
- `op` (verplicht): Bewerking (`add`, `sub`, `mul`, `div`)

**Response:**
- Content-Type: `text/event-stream`
- Geeft Server-Sent Events terug met voortgang en resultaat van de berekening

**Voorbeeldverzoek:**
```
GET /calculate?a=7&b=5&op=mul HTTP/1.1
Host: localhost:8080
Accept: text/event-stream
```

**Voorbeeldresponse:**
```
event: info
data: Calculating: 7.0 mul 5.0

event: result
data: 35.0
```

## Problemen oplossen

### Veelvoorkomende problemen

1. **Poort 8080 is al in gebruik**
   - Stop andere applicaties die poort 8080 gebruiken
   - Of wijzig de serverpoort in `calculator-server/src/main/resources/application.yml`

2. **Verbinding geweigerd**
   - Zorg dat de server draait voordat je de client start
   - Controleer of de server succesvol gestart is op poort 8080

3. **Problemen met parameter namen**
   - Dit project bevat Maven compiler configuratie met de `-parameters` vlag
   - Bij problemen met parameterbinding, zorg dat het project met deze configuratie gebouwd is

### Applicaties stoppen

- Druk op `Ctrl+C` in de terminal waar de applicatie draait
- Of gebruik `mvn spring-boot:stop` als het als achtergrondproces draait

## Technologieën

- **Spring Boot 3.3.1** - Applicatieframework
- **Spring WebFlux** - Reactief webframework
- **Project Reactor** - Bibliotheek voor reactieve streams
- **Netty** - Non-blocking I/O server
- **Maven** - Build tool
- **Java 17+** - Programmeertaal

## Volgende stappen

Probeer de code aan te passen om:
- Meer wiskundige bewerkingen toe te voegen
- Foutafhandeling voor ongeldige bewerkingen te implementeren
- Request/response logging toe te voegen
- Authenticatie te implementeren
- Unit tests toe te voegen

**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsdienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet als de gezaghebbende bron worden beschouwd. Voor cruciale informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.