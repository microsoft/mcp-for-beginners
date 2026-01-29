# MCP Java Client - Demo Calcolatrice

Questo progetto mostra come creare un client Java che si connette e interagisce con un server MCP (Model Context Protocol). In questo esempio, ci collegheremo al server della calcolatrice del Capitolo 01 ed eseguiremo varie operazioni matematiche.

## Prerequisiti

Prima di eseguire questo client, devi:

1. **Avviare il Server Calcolatrice** del Capitolo 01:
   - Vai nella directory del server calcolatrice: `03-GettingStarted/01-first-server/solution/java/`
   - Compila ed esegui il server calcolatrice:
     ```cmd
     cd ..\01-first-server\solution\java
     .\mvnw clean install -DskipTests
     java -jar target\calculator-server-0.0.1-SNAPSHOT.jar
     ```
   - Il server dovrebbe essere in esecuzione su `http://localhost:8080`

2. Avere installato **Java 21 o superiore** sul tuo sistema
3. Avere **Maven** (incluso tramite Maven Wrapper)

## Cos’è SDKClient?

`SDKClient` è un’applicazione Java che dimostra come:
- Connettersi a un server MCP usando il trasporto Server-Sent Events (SSE)
- Elencare gli strumenti disponibili dal server
- Chiamare varie funzioni della calcolatrice da remoto
- Gestire le risposte e mostrare i risultati

## Come Funziona

Il client utilizza il framework Spring AI MCP per:

1. **Stabilire la Connessione**: crea un client WebFlux SSE per connettersi al server calcolatrice
2. **Inizializzare il Client**: configura il client MCP e stabilisce la connessione
3. **Scoprire gli Strumenti**: elenca tutte le operazioni disponibili della calcolatrice
4. **Eseguire Operazioni**: chiama varie funzioni matematiche con dati di esempio
5. **Mostrare i Risultati**: visualizza i risultati di ogni calcolo

## Struttura del Progetto

```
src/
└── main/
    └── java/
        └── com/
            └── microsoft/
                └── mcp/
                    └── sample/
                        └── client/
                            └── SDKClient.java    # Main client implementation
```

## Dipendenze Principali

Il progetto utilizza le seguenti dipendenze principali:

```xml
<dependency>
    <groupId>org.springframework.ai</groupId>
    <artifactId>spring-ai-starter-mcp-server-webflux</artifactId>
</dependency>
```

Questa dipendenza fornisce:
- `McpClient` - L’interfaccia principale del client
- `WebFluxSseClientTransport` - Trasporto SSE per comunicazioni web
- Schemi del protocollo MCP e tipi di richiesta/risposta

## Compilare il Progetto

Compila il progetto usando il Maven wrapper:

```cmd
.\mvnw clean install
```

## Eseguire il Client

```cmd
java -jar .\target\calculator-client-0.0.1-SNAPSHOT.jar
```

**Nota**: Assicurati che il server calcolatrice sia in esecuzione su `http://localhost:8080` prima di eseguire uno di questi comandi.

## Cosa Fa il Client

Quando esegui il client, esso:

1. **Si connette** al server calcolatrice su `http://localhost:8080`
2. **Elenca gli Strumenti** - Mostra tutte le operazioni disponibili della calcolatrice
3. **Esegue Calcoli**:
   - Addizione: 5 + 3 = 8
   - Sottrazione: 10 - 4 = 6
   - Moltiplicazione: 6 × 7 = 42
   - Divisione: 20 ÷ 4 = 5
   - Potenza: 2^8 = 256
   - Radice Quadrata: √16 = 4
   - Valore Assoluto: |-5.5| = 5.5
   - Aiuto: mostra le operazioni disponibili

## Output Atteso

```
Available Tools = ListToolsResult[tools=[Tool[name=add, description=Add two numbers together, ...], ...]]
Add Result = CallToolResult[content=[TextContent[text="5,00 + 3,00 = 8,00"]], isError=false]
Subtract Result = CallToolResult[content=[TextContent[text="10,00 - 4,00 = 6,00"]], isError=false]
Multiply Result = CallToolResult[content=[TextContent[text="6,00 * 7,00 = 42,00"]], isError=false]
Divide Result = CallToolResult[content=[TextContent[text="20,00 / 4,00 = 5,00"]], isError=false]
Power Result = CallToolResult[content=[TextContent[text="2,00 ^ 8,00 = 256,00"]], isError=false]
Square Root Result = CallToolResult[content=[TextContent[text="√16,00 = 4,00"]], isError=false]
Absolute Result = CallToolResult[content=[TextContent[text="|-5,50| = 5,50"]], isError=false]
Help = CallToolResult[content=[TextContent[text="Basic Calculator MCP Service\n\nAvailable operations:\n1. add(a, b) - Adds two numbers\n2. subtract(a, b) - Subtracts the second number from the first\n..."]], isError=false]
```

**Nota**: Potresti vedere avvisi di Maven riguardo thread residui alla fine - questo è normale per applicazioni reattive e non indica un errore.

## Comprendere il Codice

### 1. Configurazione del Trasporto
```java
var transport = new WebFluxSseClientTransport(WebClient.builder().baseUrl("http://localhost:8080"));
```
Questo crea un trasporto SSE (Server-Sent Events) che si connette al server calcolatrice.

### 2. Creazione del Client
```java
var client = McpClient.sync(this.transport).build();
client.initialize();
```
Crea un client MCP sincrono e inizializza la connessione.

### 3. Chiamata agli Strumenti
```java
CallToolResult resultAdd = client.callTool(new CallToolRequest("add", Map.of("a", 5.0, "b", 3.0)));
```
Chiama lo strumento "add" con i parametri a=5.0 e b=3.0.

## Risoluzione dei Problemi

### Server Non Avviato
Se ricevi errori di connessione, assicurati che il server calcolatrice del Capitolo 01 sia in esecuzione:
```
Error: Connection refused
```
**Soluzione**: Avvia prima il server calcolatrice.

### Porta già in Uso
Se la porta 8080 è occupata:
```
Error: Address already in use
```
**Soluzione**: Ferma altre applicazioni che usano la porta 8080 o modifica il server per usare una porta diversa.

### Errori di Compilazione
Se incontri errori di compilazione:
```cmd
.\mvnw clean install -DskipTests
```

## Per Saperne di Più

- [Spring AI MCP Documentation](https://docs.spring.io/spring-ai/reference/api/mcp/)
- [Model Context Protocol Specification](https://modelcontextprotocol.io/)
- [Spring WebFlux Documentation](https://docs.spring.io/spring-framework/docs/current/reference/html/web-reactive.html)

**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica [Co-op Translator](https://github.com/Azure/co-op-translator). Pur impegnandoci per garantire accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un umano. Non ci assumiamo alcuna responsabilità per eventuali malintesi o interpretazioni errate derivanti dall’uso di questa traduzione.