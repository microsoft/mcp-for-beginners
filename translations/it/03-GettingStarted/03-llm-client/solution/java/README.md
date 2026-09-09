# Cliente LLM Calcolatrice

Un'applicazione Java che dimostra come usare LangChain4j per connettersi a un servizio calcolatrice MCP (Model Context Protocol) tramite l'API compatibile MiniMax OpenAI.

## Prerequisiti

- Java 21 o superiore
- Maven 3.6+ (o usa il wrapper Maven incluso)
- Una chiave API MiniMax
- Un servizio calcolatrice MCP in esecuzione su `http://localhost:8080`

## Ottenere la Chiave API

Questa applicazione utilizza l'API compatibile MiniMax OpenAI. Segui questi passaggi per ottenere la tua chiave e l'endpoint:

### 1. Scegli un endpoint
1. Usa `https://api.minimax.io/v1` per l'endpoint globale
2. Usa `https://api.minimaxi.com/v1` per l'endpoint Cina

### 2. Crea una chiave API
1. Crea una chiave API MiniMax dal tuo account MiniMax
2. Conserva la chiave in un luogo sicuro

### 3. Imposta le variabili d'ambiente

#### Su Windows (Prompt dei comandi):
```cmd
set OPENAI_API_KEY=your_minimax_api_key_here
set OPENAI_BASE_URL=https://api.minimax.io/v1
set MINIMAX_MODEL_ID=MiniMax-M3
```

#### Su Windows (PowerShell):
```powershell
$env:OPENAI_API_KEY="your_minimax_api_key_here"
$env:OPENAI_BASE_URL="https://api.minimax.io/v1"
$env:MINIMAX_MODEL_ID="MiniMax-M3"
```

#### Su macOS/Linux:
```bash
export OPENAI_API_KEY=your_minimax_api_key_here
export OPENAI_BASE_URL=https://api.minimax.io/v1
export MINIMAX_MODEL_ID=MiniMax-M3
```

## Configurazione e Installazione

1. **Clona o naviga nella directory del progetto**

2. **Installa le dipendenze**:
   ```cmd
   mvnw clean install
   ```
   Oppure se hai Maven installato globalmente:
   ```cmd
   mvn clean install
   ```

3. **Configura le variabili d'ambiente** (vedi la sezione "Ottenere la Chiave API" sopra)

4. **Avvia il Servizio Calcolatrice MCP**:
   Assicurati che il servizio calcolatrice MCP del capitolo 1 sia in esecuzione su `http://localhost:8080/sse`. Deve essere avviato prima del client.

## Esecuzione dell'Applicazione

```cmd
mvnw clean package
java -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## Cosa Fa l'Applicazione

L'applicazione dimostra tre principali interazioni con il servizio calcolatrice:

1. **Addizione**: Calcola la somma di 24.5 e 17.3
2. **Radice Quadrata**: Calcola la radice quadrata di 144
3. **Aiuto**: Mostra le funzioni calcolatrice disponibili

## Output Atteso

Quando eseguito con successo, dovresti vedere un output simile a:

```
The sum of 24.5 and 17.3 is 41.8.
The square root of 144 is 12.
The calculator service provides the following functions: add, subtract, multiply, divide, sqrt, power...
```

## Risoluzione dei Problemi

### Problemi Comuni

1. **"La variabile d'ambiente OPENAI_API_KEY non è impostata"**
   - Assicurati di aver impostato la variabile d'ambiente `OPENAI_API_KEY`
   - Riavvia il terminale/prompt dei comandi dopo aver impostato la variabile

2. **"Connessione rifiutata a localhost:8080"**
   - Verifica che il servizio calcolatrice MCP sia in esecuzione sulla porta 8080
   - Controlla se un altro servizio sta usando la porta 8080

3. **"Autenticazione fallita"**
   - Verifica che la tua chiave API sia valida
   - Controlla che `OPENAI_BASE_URL` corrisponda all'endpoint che intendevi usare

4. **Errori di compilazione Maven**
   - Assicurati di usare Java 21 o superiore: `java -version`
   - Prova a pulire la compilazione: `mvnw clean`

### Debugging

Per abilitare i log di debug, aggiungi il seguente argomento JVM durante l'esecuzione:
```cmd
java -Dlogging.level.dev.langchain4j=DEBUG -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## Configurazione

L'applicazione è configurata per:
- Usare MiniMax-M3 per default, o MiniMax-M2.7 quando è impostato `MINIMAX_MODEL_ID`
- Connettersi a `OPENAI_BASE_URL` quando è impostato; altrimenti usa `https://api.minimaxi.com/v1` quando `MINIMAX_REGION=cn_zh`, o `https://api.minimax.io/v1` per default
- Connettersi al servizio MCP su `http://localhost:8080/sse`
- Usare un timeout di 60 secondi per le richieste

## Dipendenze

Dipendenze chiave usate in questo progetto:
- **LangChain4j**: Per l'integrazione AI e la gestione degli strumenti
- **LangChain4j MCP**: Per il supporto al Model Context Protocol
- **LangChain4j OpenAI official**: Per l'integrazione MiniMax API compatibile OpenAI
- **Spring Boot**: Per il framework applicativo e l'iniezione delle dipendenze

## Licenza

Questo progetto è concesso in licenza sotto Apache License 2.0 - vedi il file [LICENSE](../../../../../../03-GettingStarted/03-llm-client/solution/java/LICENSE) per i dettagli.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Questo documento è stato tradotto utilizzando il servizio di traduzione AI [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire la precisione, si prega di notare che le traduzioni automatizzate possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un essere umano. Non siamo responsabili per eventuali malintesi o interpretazioni errate derivanti dall’uso di questa traduzione.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->