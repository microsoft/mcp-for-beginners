# Calculator HTTP Streaming Demo

Dette projekt demonstrerer HTTP streaming ved brug af Server-Sent Events (SSE) med Spring Boot WebFlux. Det består af to applikationer:

- **Calculator Server**: En reaktiv webservice, der udfører beregninger og streamer resultater ved hjælp af SSE
- **Calculator Client**: En klientapplikation, der forbruger streaming-endpointet

## Forudsætninger

- Java 17 eller nyere
- Maven 3.6 eller nyere

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

## Sådan fungerer det

1. **Calculator Server** eksponerer et `/calculate` endpoint, som:
   - Accepterer query-parametre: `a` (tal), `b` (tal), `op` (operation)
   - Understøttede operationer: `add`, `sub`, `mul`, `div`
   - Returnerer Server-Sent Events med beregningsprogression og resultat

2. **Calculator Client** forbinder til serveren og:
   - Sender en forespørgsel for at beregne `7 * 5`
   - Forbruger den streamede respons
   - Udskriver hver event til konsollen

## Kørsel af applikationerne

### Mulighed 1: Brug af Maven (anbefalet)

#### 1. Start Calculator Server

Åbn en terminal og naviger til server-mappen:

```bash
cd calculator-server
mvn clean package
mvn spring-boot:run
```

Serveren starter på `http://localhost:8080`

Du skulle se output som:
```
Started CalculatorServerApplication in X.XXX seconds
Netty started on port 8080 (http)
```

#### 2. Kør Calculator Client

Åbn en **ny terminal** og naviger til klient-mappen:

```bash
cd calculator-client
mvn clean package
mvn spring-boot:run
```

Klienten forbinder til serveren, udfører beregningen og viser de streamede resultater.

### Mulighed 2: Brug Java direkte

#### 1. Compile og kør serveren:

```bash
cd calculator-server
mvn clean package
java -jar target/calculator-server-0.0.1-SNAPSHOT.jar
```

#### 2. Compile og kør klienten:

```bash
cd calculator-client
mvn clean package
java -jar target/calculator-client-0.0.1-SNAPSHOT.jar
```

## Manuel test af serveren

Du kan også teste serveren via en webbrowser eller curl:

### Brug af webbrowser:
Besøg: `http://localhost:8080/calculate?a=10&b=5&op=add`

### Brug af curl:
```bash
curl "http://localhost:8080/calculate?a=10&b=5&op=add" -H "Accept: text/event-stream"
```

## Forventet output

Når klienten kører, bør du se streamet output lignende:

```
event:info
data:Calculating: 7.0 mul 5.0

event:result
data:35.0
```

## Understøttede operationer

- `add` - Addition (a + b)
- `sub` - Subtraktion (a - b)
- `mul` - Multiplikation (a * b)
- `div` - Division (a / b, returnerer NaN hvis b = 0)

## API Reference

### GET /calculate

**Parametre:**
- `a` (påkrævet): Første tal (double)
- `b` (påkrævet): Andet tal (double)
- `op` (påkrævet): Operation (`add`, `sub`, `mul`, `div`)

**Respons:**
- Content-Type: `text/event-stream`
- Returnerer Server-Sent Events med beregningsprogression og resultat

**Eksempel på forespørgsel:**
```
GET /calculate?a=7&b=5&op=mul HTTP/1.1
Host: localhost:8080
Accept: text/event-stream
```

**Eksempel på respons:**
```
event: info
data: Calculating: 7.0 mul 5.0

event: result
data: 35.0
```

## Fejlfinding

### Almindelige problemer

1. **Port 8080 er allerede i brug**
   - Stop andre applikationer, der bruger port 8080
   - Eller ændr serverporten i `calculator-server/src/main/resources/application.yml`

2. **Forbindelse afvist**
   - Sørg for, at serveren kører, før klienten startes
   - Tjek at serveren er startet korrekt på port 8080

3. **Problemer med parameter-navne**
   - Projektet inkluderer Maven compiler-konfiguration med `-parameters` flag
   - Hvis du oplever problemer med parameterbinding, skal du sikre, at projektet er bygget med denne konfiguration

### Stop af applikationerne

- Tryk `Ctrl+C` i terminalen, hvor hver applikation kører
- Eller brug `mvn spring-boot:stop`, hvis applikationen kører som en baggrundsproces

## Teknologistak

- **Spring Boot 3.3.1** - Applikationsframework
- **Spring WebFlux** - Reaktivt webframework
- **Project Reactor** - Bibliotek til reaktive streams
- **Netty** - Non-blocking I/O server
- **Maven** - Build-værktøj
- **Java 17+** - Programmeringssprog

## Næste skridt

Prøv at ændre koden til at:
- Tilføje flere matematiske operationer
- Inkludere fejlhåndtering for ugyldige operationer
- Tilføje logging af forespørgsler/responser
- Implementere autentificering
- Tilføje enhedstests

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, bedes du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det oprindelige dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.