# Calculator HTTP Streaming Demo

Acest proiect demonstrează streaming HTTP folosind Server-Sent Events (SSE) cu Spring Boot WebFlux. Este format din două aplicații:

- **Calculator Server**: Un serviciu web reactiv care efectuează calcule și transmite rezultatele folosind SSE
- **Calculator Client**: O aplicație client care consumă endpoint-ul de streaming

## Cerințe preliminare

- Java 17 sau versiune superioară
- Maven 3.6 sau versiune superioară

## Structura proiectului

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

## Cum funcționează

1. **Calculator Server** expune un endpoint `/calculate` care:
   - Primește parametrii de interogare: `a` (număr), `b` (număr), `op` (operație)
   - Operații suportate: `add`, `sub`, `mul`, `div`
   - Returnează Server-Sent Events cu progresul calculului și rezultatul

2. **Calculator Client** se conectează la server și:
   - Trimite o cerere pentru a calcula `7 * 5`
   - Consumă răspunsul în streaming
   - Afișează fiecare eveniment în consolă

## Rularea aplicațiilor

### Opțiunea 1: Folosind Maven (recomandat)

#### 1. Pornește Calculator Server

Deschide un terminal și navighează în directorul serverului:

```bash
cd calculator-server
mvn clean package
mvn spring-boot:run
```

Serverul va porni la `http://localhost:8080`

Ar trebui să vezi o ieșire similară cu:
```
Started CalculatorServerApplication in X.XXX seconds
Netty started on port 8080 (http)
```

#### 2. Rulează Calculator Client

Deschide un **terminal nou** și navighează în directorul clientului:

```bash
cd calculator-client
mvn clean package
mvn spring-boot:run
```

Clientul se va conecta la server, va efectua calculul și va afișa rezultatele în streaming.

### Opțiunea 2: Folosind Java direct

#### 1. Compilează și rulează serverul:

```bash
cd calculator-server
mvn clean package
java -jar target/calculator-server-0.0.1-SNAPSHOT.jar
```

#### 2. Compilează și rulează clientul:

```bash
cd calculator-client
mvn clean package
java -jar target/calculator-client-0.0.1-SNAPSHOT.jar
```

## Testarea serverului manual

Poți testa serverul și folosind un browser web sau curl:

### Folosind un browser web:
Accesează: `http://localhost:8080/calculate?a=10&b=5&op=add`

### Folosind curl:
```bash
curl "http://localhost:8080/calculate?a=10&b=5&op=add" -H "Accept: text/event-stream"
```

## Ieșire așteptată

Când rulezi clientul, ar trebui să vezi o ieșire în streaming similară cu:

```
event:info
data:Calculating: 7.0 mul 5.0

event:result
data:35.0
```

## Operații suportate

- `add` - Adunare (a + b)
- `sub` - Scădere (a - b)
- `mul` - Înmulțire (a * b)
- `div` - Împărțire (a / b, returnează NaN dacă b = 0)

## Referință API

### GET /calculate

**Parametri:**
- `a` (obligatoriu): Primul număr (double)
- `b` (obligatoriu): Al doilea număr (double)
- `op` (obligatoriu): Operația (`add`, `sub`, `mul`, `div`)

**Răspuns:**
- Content-Type: `text/event-stream`
- Returnează Server-Sent Events cu progresul calculului și rezultatul

**Exemplu de cerere:**
```
GET /calculate?a=7&b=5&op=mul HTTP/1.1
Host: localhost:8080
Accept: text/event-stream
```

**Exemplu de răspuns:**
```
event: info
data: Calculating: 7.0 mul 5.0

event: result
data: 35.0
```

## Depanare

### Probleme comune

1. **Portul 8080 este deja folosit**
   - Oprește orice altă aplicație care folosește portul 8080
   - Sau schimbă portul serverului în `calculator-server/src/main/resources/application.yml`

2. **Conexiune refuzată**
   - Asigură-te că serverul este pornit înainte de a porni clientul
   - Verifică dacă serverul a pornit cu succes pe portul 8080

3. **Probleme cu numele parametrilor**
   - Proiectul include configurarea Maven pentru compilator cu flag-ul `-parameters`
   - Dacă întâmpini probleme la legarea parametrilor, asigură-te că proiectul este construit cu această configurație

### Oprirea aplicațiilor

- Apasă `Ctrl+C` în terminalul unde rulează fiecare aplicație
- Sau folosește `mvn spring-boot:stop` dacă rulezi ca proces în fundal

## Tehnologii folosite

- **Spring Boot 3.3.1** - Framework pentru aplicații
- **Spring WebFlux** - Framework web reactiv
- **Project Reactor** - Bibliotecă pentru fluxuri reactive
- **Netty** - Server I/O non-blocant
- **Maven** - Instrument de build
- **Java 17+** - Limbaj de programare

## Pași următori

Încearcă să modifici codul pentru a:
- Adăuga mai multe operații matematice
- Include gestionarea erorilor pentru operații invalide
- Adăuga logare pentru cereri/răspunsuri
- Implementa autentificare
- Adăuga teste unitare

**Declinare de responsabilitate**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist uman. Nu ne asumăm răspunderea pentru eventualele neînțelegeri sau interpretări greșite rezultate din utilizarea acestei traduceri.