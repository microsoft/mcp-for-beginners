# Servizio Calcolatrice Base MCP

Questo servizio offre operazioni di calcolatrice base tramite il Model Context Protocol (MCP) utilizzando Spring Boot con trasporto WebFlux. È progettato come esempio semplice per chi inizia a imparare le implementazioni MCP.

Per maggiori informazioni, consulta la documentazione di riferimento [MCP Server Boot Starter](https://docs.spring.io/spring-ai/reference/api/mcp/mcp-server-boot-starter-docs.html).

## Panoramica

Il servizio mostra:
- Supporto per SSE (Server-Sent Events)
- Registrazione automatica degli strumenti tramite l’annotazione `@Tool` di Spring AI
- Funzioni base della calcolatrice:
  - Addizione, sottrazione, moltiplicazione, divisione
  - Calcolo della potenza e radice quadrata
  - Modulo (resto) e valore assoluto
  - Funzione di aiuto per la descrizione delle operazioni

## Caratteristiche

Questo servizio calcolatrice offre le seguenti funzionalità:

1. **Operazioni Aritmetiche Base**:
   - Addizione di due numeri
   - Sottrazione di un numero da un altro
   - Moltiplicazione di due numeri
   - Divisione di un numero per un altro (con controllo divisione per zero)

2. **Operazioni Avanzate**:
   - Calcolo della potenza (elevare una base a un esponente)
   - Calcolo della radice quadrata (con controllo su numeri negativi)
   - Calcolo del modulo (resto)
   - Calcolo del valore assoluto

3. **Sistema di Aiuto**:
   - Funzione di aiuto integrata che spiega tutte le operazioni disponibili

## Utilizzo del Servizio

Il servizio espone i seguenti endpoint API tramite il protocollo MCP:

- `add(a, b)`: Somma due numeri
- `subtract(a, b)`: Sottrae il secondo numero dal primo
- `multiply(a, b)`: Moltiplica due numeri
- `divide(a, b)`: Divide il primo numero per il secondo (con controllo zero)
- `power(base, exponent)`: Calcola la potenza di un numero
- `squareRoot(number)`: Calcola la radice quadrata (con controllo su numeri negativi)
- `modulus(a, b)`: Calcola il resto della divisione
- `absolute(number)`: Calcola il valore assoluto
- `help()`: Fornisce informazioni sulle operazioni disponibili

## Client di Test

Un semplice client di test è incluso nel package `com.microsoft.mcp.sample.client`. La classe `SampleCalculatorClient` dimostra le operazioni disponibili del servizio calcolatrice.

## Utilizzo del Client LangChain4j

Il progetto include un esempio di client LangChain4j in `com.microsoft.mcp.sample.client.LangChain4jClient` che mostra come integrare il servizio calcolatrice con LangChain4j e i modelli GitHub:

### Prerequisiti

1. **Configurazione del Token GitHub**:
   
   Per usare i modelli AI di GitHub (come phi-4), è necessario un token di accesso personale GitHub:

   a. Vai alle impostazioni del tuo account GitHub: https://github.com/settings/tokens
   
   b. Clicca su "Generate new token" → "Generate new token (classic)"
   
   c. Dai un nome descrittivo al token
   
   d. Seleziona i seguenti ambiti:
      - `repo` (Controllo completo dei repository privati)
      - `read:org` (Lettura di organizzazioni e membri del team, lettura progetti org)
      - `gist` (Creazione di gist)
      - `user:email` (Accesso agli indirizzi email utente (sola lettura))
   
   e. Clicca su "Generate token" e copia il nuovo token
   
   f. Impostalo come variabile d’ambiente:
      
      Su Windows:
      ```
      set GITHUB_TOKEN=your-github-token
      ```
      
      Su macOS/Linux:
      ```bash
      export GITHUB_TOKEN=your-github-token
      ```

   g. Per una configurazione persistente, aggiungilo alle variabili d’ambiente tramite le impostazioni di sistema

2. Aggiungi la dipendenza LangChain4j GitHub al tuo progetto (già inclusa in pom.xml):
   ```xml
   <dependency>
       <groupId>dev.langchain4j</groupId>
       <artifactId>langchain4j-github</artifactId>
       <version>${langchain4j.version}</version>
   </dependency>
   ```

3. Assicurati che il server calcolatrice sia in esecuzione su `localhost:8080`

### Esecuzione del Client LangChain4j

Questo esempio dimostra:
- Connessione al server MCP calcolatrice tramite trasporto SSE
- Uso di LangChain4j per creare un chatbot che sfrutta le operazioni della calcolatrice
- Integrazione con i modelli AI GitHub (ora usando il modello phi-4)

Il client invia le seguenti query di esempio per mostrare le funzionalità:
1. Calcolo della somma di due numeri
2. Calcolo della radice quadrata di un numero
3. Richiesta di informazioni di aiuto sulle operazioni disponibili

Esegui l’esempio e controlla l’output della console per vedere come il modello AI utilizza gli strumenti della calcolatrice per rispondere alle richieste.

### Configurazione del Modello GitHub

Il client LangChain4j è configurato per usare il modello phi-4 di GitHub con le seguenti impostazioni:

```java
ChatLanguageModel model = GitHubChatModel.builder()
    .apiKey(System.getenv("GITHUB_TOKEN"))
    .timeout(Duration.ofSeconds(60))
    .modelName("phi-4")
    .logRequests(true)
    .logResponses(true)
    .build();
```

Per usare modelli GitHub diversi, cambia semplicemente il parametro `modelName` con un altro modello supportato (es. "claude-3-haiku-20240307", "llama-3-70b-8192", ecc.).

## Dipendenze

Il progetto richiede le seguenti dipendenze principali:

```xml
<!-- For MCP Server -->
<dependency>
    <groupId>org.springframework.ai</groupId>
    <artifactId>spring-ai-starter-mcp-server-webflux</artifactId>
</dependency>

<!-- For LangChain4j integration -->
<dependency>
    <groupId>dev.langchain4j</groupId>
    <artifactId>langchain4j-mcp</artifactId>
    <version>${langchain4j.version}</version>
</dependency>

<!-- For GitHub models support -->
<dependency>
    <groupId>dev.langchain4j</groupId>
    <artifactId>langchain4j-github</artifactId>
    <version>${langchain4j.version}</version>
</dependency>
```

## Compilazione del Progetto

Compila il progetto usando Maven:
```bash
./mvnw clean install -DskipTests
```

## Avvio del Server

### Usando Java

```bash
java -jar target/calculator-server-0.0.1-SNAPSHOT.jar
```

### Usando MCP Inspector

MCP Inspector è uno strumento utile per interagire con i servizi MCP. Per usarlo con questo servizio calcolatrice:

1. **Installa e avvia MCP Inspector** in una nuova finestra terminale:
   ```bash
   npx @modelcontextprotocol/inspector
   ```

2. **Accedi all’interfaccia web** cliccando sull’URL mostrato dall’app (tipicamente http://localhost:6274)

3. **Configura la connessione**:
   - Imposta il tipo di trasporto su "SSE"
   - Imposta l’URL sull’endpoint SSE del server in esecuzione: `http://localhost:8080/sse`
   - Clicca su "Connect"

4. **Usa gli strumenti**:
   - Clicca su "List Tools" per vedere le operazioni calcolatrice disponibili
   - Seleziona uno strumento e clicca su "Run Tool" per eseguire un’operazione

![Screenshot MCP Inspector](../../../../../../translated_images/it/tool.c75a0b2380efcf1a47a8478f54380a36ddcca7943b98f56dabbac8b07e15c3bb.png)

### Usando Docker

Il progetto include un Dockerfile per il deployment containerizzato:

1. **Costruisci l’immagine Docker**:
   ```bash
   docker build -t calculator-mcp-service .
   ```

2. **Esegui il container Docker**:
   ```bash
   docker run -p 8080:8080 calculator-mcp-service
   ```

Questo farà:
- Costruire un’immagine Docker multi-stage con Maven 3.9.9 e Eclipse Temurin 24 JDK
- Creare un’immagine container ottimizzata
- Esporre il servizio sulla porta 8080
- Avviare il servizio calcolatrice MCP all’interno del container

Potrai accedere al servizio su `http://localhost:8080` una volta che il container è in esecuzione.

## Risoluzione Problemi

### Problemi Comuni con il Token GitHub

1. **Problemi di Permessi del Token**: Se ricevi un errore 403 Forbidden, verifica che il token abbia i permessi corretti come indicato nei prerequisiti.

2. **Token Non Trovato**: Se ricevi un errore "No API key found", assicurati che la variabile d’ambiente GITHUB_TOKEN sia impostata correttamente.

3. **Limitazioni di Rate**: L’API GitHub ha limiti di utilizzo. Se incontri un errore di limite (codice 429), attendi qualche minuto prima di riprovare.

4. **Scadenza del Token**: I token GitHub possono scadere. Se ricevi errori di autenticazione dopo un po’, genera un nuovo token e aggiorna la variabile d’ambiente.

Se hai bisogno di ulteriore assistenza, consulta la [documentazione LangChain4j](https://github.com/langchain4j/langchain4j) o la [documentazione API GitHub](https://docs.github.com/en/rest).

**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica [Co-op Translator](https://github.com/Azure/co-op-translator). Pur impegnandoci per garantire accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un umano. Non ci assumiamo alcuna responsabilità per eventuali malintesi o interpretazioni errate derivanti dall’uso di questa traduzione.