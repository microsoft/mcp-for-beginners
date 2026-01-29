# Calculator HTTP Streaming Demo

Dette prosjektet demonstrerer HTTP-strømming ved bruk av Server-Sent Events (SSE) med Spring Boot WebFlux. Det består av to applikasjoner:

- **Calculator Server**: En reaktiv webtjeneste som utfører beregninger og strømmer resultater ved hjelp av SSE
- **Calculator Client**: En klientapplikasjon som konsumerer strømmingsendepunktet

## Forutsetninger

- Java 17 eller nyere
- Maven 3.6 eller nyere

## Prosjektstruktur

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

## Hvordan det fungerer

1. **Calculator Server** eksponerer et `/calculate` endepunkt som:
   - Aksepterer spørringsparametere: `a` (nummer), `b` (nummer), `op` (operasjon)
   - Støttede operasjoner: `add`, `sub`, `mul`, `div`
   - Returnerer Server-Sent Events med beregningsprogresjon og resultat

2. **Calculator Client** kobler til serveren og:
   - Sender en forespørsel for å beregne `7 * 5`
   - Konsumerer den strømmende responsen
   - Skriver ut hver hendelse til konsollen

## Kjøre applikasjonene

### Alternativ 1: Bruke Maven (anbefalt)

#### 1. Start Calculator Server

Åpne et terminalvindu og naviger til serverkatalogen:

```bash
cd calculator-server
mvn clean package
mvn spring-boot:run
```

Serveren starter på `http://localhost:8080`

Du bør se output som:
```
Started CalculatorServerApplication in X.XXX seconds
Netty started on port 8080 (http)
```

#### 2. Kjør Calculator Client

Åpne et **nytt terminalvindu** og naviger til klientkatalogen:

```bash
cd calculator-client
mvn clean package
mvn spring-boot:run
```

Klienten kobler til serveren, utfører beregningen og viser de strømmende resultatene.

### Alternativ 2: Bruke Java direkte

#### 1. Kompiler og kjør serveren:

```bash
cd calculator-server
mvn clean package
java -jar target/calculator-server-0.0.1-SNAPSHOT.jar
```

#### 2. Kompiler og kjør klienten:

```bash
cd calculator-client
mvn clean package
java -jar target/calculator-client-0.0.1-SNAPSHOT.jar
```

## Teste serveren manuelt

Du kan også teste serveren ved å bruke en nettleser eller curl:

### Bruke en nettleser:
Besøk: `http://localhost:8080/calculate?a=10&b=5&op=add`

### Bruke curl:
```bash
curl "http://localhost:8080/calculate?a=10&b=5&op=add" -H "Accept: text/event-stream"
```

## Forventet output

Når du kjører klienten, bør du se strømmende output som ligner på:

```
event:info
data:Calculating: 7.0 mul 5.0

event:result
data:35.0
```

## Støttede operasjoner

- `add` - Addisjon (a + b)
- `sub` - Subtraksjon (a - b)
- `mul` - Multiplikasjon (a * b)
- `div` - Divisjon (a / b, returnerer NaN hvis b = 0)

## API Referanse

### GET /calculate

**Parametere:**
- `a` (påkrevd): Første tall (double)
- `b` (påkrevd): Andre tall (double)
- `op` (påkrevd): Operasjon (`add`, `sub`, `mul`, `div`)

**Respons:**
- Content-Type: `text/event-stream`
- Returnerer Server-Sent Events med beregningsprogresjon og resultat

**Eksempel på forespørsel:**
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

## Feilsøking

### Vanlige problemer

1. **Port 8080 er allerede i bruk**
   - Stopp andre applikasjoner som bruker port 8080
   - Eller endre serverport i `calculator-server/src/main/resources/application.yml`

2. **Tilkobling nektet**
   - Sørg for at serveren kjører før du starter klienten
   - Sjekk at serveren startet riktig på port 8080

3. **Problemer med parameter-navn**
   - Dette prosjektet inkluderer Maven-kompilator-konfigurasjon med `-parameters` flagg
   - Hvis du opplever problemer med parameterbinding, sørg for at prosjektet er bygget med denne konfigurasjonen

### Stoppe applikasjonene

- Trykk `Ctrl+C` i terminalen der hver applikasjon kjører
- Eller bruk `mvn spring-boot:stop` hvis applikasjonen kjører i bakgrunnen

## Teknologistabel

- **Spring Boot 3.3.1** - Applikasjonsrammeverk
- **Spring WebFlux** - Reaktivt web-rammeverk
- **Project Reactor** - Bibliotek for reaktive strømmer
- **Netty** - Ikke-blokkerende I/O-server
- **Maven** - Byggeverktøy
- **Java 17+** - Programmeringsspråk

## Neste steg

Prøv å endre koden for å:
- Legge til flere matematiske operasjoner
- Inkludere feilhåndtering for ugyldige operasjoner
- Legge til logging av forespørsler/responser
- Implementere autentisering
- Legge til enhetstester

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vennligst vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.