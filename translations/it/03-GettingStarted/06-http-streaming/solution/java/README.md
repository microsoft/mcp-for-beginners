# Demo di Streaming HTTP per la Calcolatrice

Questo progetto dimostra lo streaming HTTP utilizzando Server-Sent Events (SSE) con Spring Boot WebFlux. È composto da due applicazioni:

- **Calculator Server**: un servizio web reattivo che esegue calcoli e trasmette i risultati tramite SSE
- **Calculator Client**: un'applicazione client che consuma l'endpoint di streaming

## Prerequisiti

- Java 17 o superiore
- Maven 3.6 o superiore

## Struttura del Progetto

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

## Come Funziona

1. Il **Calculator Server** espone un endpoint `/calculate` che:
   - Accetta parametri di query: `a` (numero), `b` (numero), `op` (operazione)
   - Operazioni supportate: `add`, `sub`, `mul`, `div`
   - Restituisce Server-Sent Events con il progresso del calcolo e il risultato

2. Il **Calculator Client** si connette al server e:
   - Effettua una richiesta per calcolare `7 * 5`
   - Consuma la risposta in streaming
   - Stampa ogni evento sulla console

## Esecuzione delle Applicazioni

### Opzione 1: Usare Maven (Consigliato)

#### 1. Avviare il Calculator Server

Apri un terminale e vai nella directory del server:

```bash
cd calculator-server
mvn clean package
mvn spring-boot:run
```

Il server partirà su `http://localhost:8080`

Dovresti vedere un output simile a:
```
Started CalculatorServerApplication in X.XXX seconds
Netty started on port 8080 (http)
```

#### 2. Eseguire il Calculator Client

Apri un **nuovo terminale** e vai nella directory del client:

```bash
cd calculator-client
mvn clean package
mvn spring-boot:run
```

Il client si connetterà al server, eseguirà il calcolo e mostrerà i risultati in streaming.

### Opzione 2: Usare Java direttamente

#### 1. Compilare ed eseguire il server:

```bash
cd calculator-server
mvn clean package
java -jar target/calculator-server-0.0.1-SNAPSHOT.jar
```

#### 2. Compilare ed eseguire il client:

```bash
cd calculator-client
mvn clean package
java -jar target/calculator-client-0.0.1-SNAPSHOT.jar
```

## Testare il Server Manualmente

Puoi anche testare il server usando un browser o curl:

### Usando un browser:
Visita: `http://localhost:8080/calculate?a=10&b=5&op=add`

### Usando curl:
```bash
curl "http://localhost:8080/calculate?a=10&b=5&op=add" -H "Accept: text/event-stream"
```

## Output Atteso

Quando esegui il client, dovresti vedere un output in streaming simile a:

```
event:info
data:Calculating: 7.0 mul 5.0

event:result
data:35.0
```

## Operazioni Supportate

- `add` - Addizione (a + b)
- `sub` - Sottrazione (a - b)
- `mul` - Moltiplicazione (a * b)
- `div` - Divisione (a / b, restituisce NaN se b = 0)

## Riferimento API

### GET /calculate

**Parametri:**
- `a` (obbligatorio): Primo numero (double)
- `b` (obbligatorio): Secondo numero (double)
- `op` (obbligatorio): Operazione (`add`, `sub`, `mul`, `div`)

**Risposta:**
- Content-Type: `text/event-stream`
- Restituisce Server-Sent Events con il progresso del calcolo e il risultato

**Esempio di richiesta:**
```
GET /calculate?a=7&b=5&op=mul HTTP/1.1
Host: localhost:8080
Accept: text/event-stream
```

**Esempio di risposta:**
```
event: info
data: Calculating: 7.0 mul 5.0

event: result
data: 35.0
```

## Risoluzione dei Problemi

### Problemi Comuni

1. **Porta 8080 già in uso**
   - Ferma qualsiasi altra applicazione che usa la porta 8080
   - Oppure cambia la porta del server in `calculator-server/src/main/resources/application.yml`

2. **Connessione rifiutata**
   - Assicurati che il server sia in esecuzione prima di avviare il client
   - Verifica che il server sia partito correttamente sulla porta 8080

3. **Problemi con i nomi dei parametri**
   - Questo progetto include la configurazione Maven del compilatore con il flag `-parameters`
   - Se riscontri problemi di binding dei parametri, assicurati che il progetto sia compilato con questa configurazione

### Arresto delle Applicazioni

- Premi `Ctrl+C` nel terminale dove è in esecuzione ciascuna applicazione
- Oppure usa `mvn spring-boot:stop` se stai eseguendo come processo in background

## Tecnologia Utilizzata

- **Spring Boot 3.3.1** - Framework applicativo
- **Spring WebFlux** - Framework web reattivo
- **Project Reactor** - Libreria per flussi reattivi
- **Netty** - Server I/O non bloccante
- **Maven** - Strumento di build
- **Java 17+** - Linguaggio di programmazione

## Passi Successivi

Prova a modificare il codice per:
- Aggiungere altre operazioni matematiche
- Includere la gestione degli errori per operazioni non valide
- Aggiungere logging per richieste/risposte
- Implementare l'autenticazione
- Aggiungere test unitari

**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica [Co-op Translator](https://github.com/Azure/co-op-translator). Pur impegnandoci per garantire l’accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un umano. Non ci assumiamo alcuna responsabilità per eventuali malintesi o interpretazioni errate derivanti dall’uso di questa traduzione.