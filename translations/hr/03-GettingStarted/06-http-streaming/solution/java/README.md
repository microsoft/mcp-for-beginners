# Calculator HTTP Streaming Demo

Ovaj projekt demonstrira HTTP streaming koristeći Server-Sent Events (SSE) sa Spring Boot WebFlux. Sastoji se od dvije aplikacije:

- **Calculator Server**: reaktivna web usluga koja izvodi izračune i šalje rezultate putem SSE
- **Calculator Client**: klijentska aplikacija koja koristi streaming endpoint

## Preduvjeti

- Java 17 ili noviji
- Maven 3.6 ili noviji

## Struktura projekta

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

## Kako radi

1. **Calculator Server** izlaže `/calculate` endpoint koji:
   - Prima query parametre: `a` (broj), `b` (broj), `op` (operacija)
   - Podržane operacije: `add`, `sub`, `mul`, `div`
   - Vraća Server-Sent Events s napretkom izračuna i rezultatom

2. **Calculator Client** se povezuje na server i:
   - Šalje zahtjev za izračun `7 * 5`
   - Prima streaming odgovor
   - Ispisuje svaki event u konzolu

## Pokretanje aplikacija

### Opcija 1: Korištenje Mavena (preporučeno)

#### 1. Pokrenite Calculator Server

Otvorite terminal i idite u direktorij servera:

```bash
cd calculator-server
mvn clean package
mvn spring-boot:run
```

Server će se pokrenuti na `http://localhost:8080`

Trebali biste vidjeti izlaz poput:
```
Started CalculatorServerApplication in X.XXX seconds
Netty started on port 8080 (http)
```

#### 2. Pokrenite Calculator Client

Otvorite **novi terminal** i idite u direktorij klijenta:

```bash
cd calculator-client
mvn clean package
mvn spring-boot:run
```

Klijent će se povezati na server, izvršiti izračun i prikazati streaming rezultate.

### Opcija 2: Direktno korištenje Jave

#### 1. Kompajlirajte i pokrenite server:

```bash
cd calculator-server
mvn clean package
java -jar target/calculator-server-0.0.1-SNAPSHOT.jar
```

#### 2. Kompajlirajte i pokrenite klijenta:

```bash
cd calculator-client
mvn clean package
java -jar target/calculator-client-0.0.1-SNAPSHOT.jar
```

## Ručno testiranje servera

Server možete testirati i putem web preglednika ili curl-a:

### Korištenje web preglednika:
Posjetite: `http://localhost:8080/calculate?a=10&b=5&op=add`

### Korištenje curl-a:
```bash
curl "http://localhost:8080/calculate?a=10&b=5&op=add" -H "Accept: text/event-stream"
```

## Očekivani izlaz

Prilikom pokretanja klijenta trebali biste vidjeti streaming izlaz sličan ovom:

```
event:info
data:Calculating: 7.0 mul 5.0

event:result
data:35.0
```

## Podržane operacije

- `add` - Zbrajanje (a + b)
- `sub` - Oduzimanje (a - b)
- `mul` - Množenje (a * b)
- `div` - Dijeljenje (a / b, vraća NaN ako je b = 0)

## API Referenca

### GET /calculate

**Parametri:**
- `a` (obavezno): Prvi broj (double)
- `b` (obavezno): Drugi broj (double)
- `op` (obavezno): Operacija (`add`, `sub`, `mul`, `div`)

**Odgovor:**
- Content-Type: `text/event-stream`
- Vraća Server-Sent Events s napretkom izračuna i rezultatom

**Primjer zahtjeva:**
```
GET /calculate?a=7&b=5&op=mul HTTP/1.1
Host: localhost:8080
Accept: text/event-stream
```

**Primjer odgovora:**
```
event: info
data: Calculating: 7.0 mul 5.0

event: result
data: 35.0
```

## Rješavanje problema

### Česti problemi

1. **Port 8080 je već zauzet**
   - Zaustavite druge aplikacije koje koriste port 8080
   - Ili promijenite port servera u `calculator-server/src/main/resources/application.yml`

2. **Veza odbijena**
   - Provjerite da je server pokrenut prije nego što pokrenete klijenta
   - Provjerite je li server uspješno startao na portu 8080

3. **Problemi s imenima parametara**
   - Projekt uključuje Maven konfiguraciju kompajlera s `-parameters` zastavicom
   - Ako imate problema s vezivanjem parametara, provjerite da je projekt izgrađen s ovom konfiguracijom

### Zaustavljanje aplikacija

- Pritisnite `Ctrl+C` u terminalu gdje je aplikacija pokrenuta
- Ili koristite `mvn spring-boot:stop` ako aplikacija radi u pozadini

## Tehnološki stack

- **Spring Boot 3.3.1** - aplikacijski framework
- **Spring WebFlux** - reaktivni web framework
- **Project Reactor** - biblioteka za reaktivne tokove
- **Netty** - server s neblokirajućim I/O
- **Maven** - alat za izgradnju
- **Java 17+** - programski jezik

## Sljedeći koraci

Isprobajte izmjene koda kako biste:
- Dodali više matematičkih operacija
- Uključili obradu pogrešaka za nevažeće operacije
- Dodali logiranje zahtjeva/odgovora
- Implementirali autentifikaciju
- Dodali jedinicne testove

**Odricanje od odgovornosti**:  
Ovaj dokument je preveden korištenjem AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za kritične informacije preporučuje se profesionalni ljudski prijevod. Ne snosimo odgovornost za bilo kakva nesporazuma ili pogrešna tumačenja koja proizlaze iz korištenja ovog prijevoda.