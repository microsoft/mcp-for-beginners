# Calculator LLM Client

Un'applicazione Java che dimostra come utilizzare LangChain4j per connettersi a un servizio calcolatrice MCP (Model Context Protocol) con integrazione GitHub Models.

## Prerequisiti

- Java 21 o superiore
- Maven 3.6+ (o usa il Maven wrapper incluso)
- Un account GitHub con accesso a GitHub Models
- Un servizio calcolatrice MCP in esecuzione su `http://localhost:8080`

## Ottenere il Token GitHub

Questa applicazione utilizza GitHub Models, che richiede un token di accesso personale GitHub. Segui questi passaggi per ottenere il tuo token:

### 1. Accedi a GitHub Models
1. Vai su [GitHub Models](https://github.com/marketplace/models)
2. Accedi con il tuo account GitHub
3. Richiedi l'accesso a GitHub Models se non l'hai già fatto

### 2. Crea un Token di Accesso Personale
1. Vai su [GitHub Settings → Developer settings → Personal access tokens → Tokens (classic)](https://github.com/settings/tokens)
2. Clicca su "Generate new token" → "Generate new token (classic)"
3. Dai un nome descrittivo al token (es. "MCP Calculator Client")
4. Imposta la scadenza secondo necessità
5. Seleziona i seguenti ambiti:
   - `repo` (se accedi a repository privati)
   - `user:email`
6. Clicca su "Generate token"
7. **Importante**: Copia subito il token - non potrai più vederlo!

### 3. Imposta la Variabile d'Ambiente

#### Su Windows (Prompt dei comandi):
```cmd
set GITHUB_TOKEN=your_github_token_here
```

#### Su Windows (PowerShell):
```powershell
$env:GITHUB_TOKEN="your_github_token_here"
```

#### Su macOS/Linux:
```bash
export GITHUB_TOKEN=your_github_token_here
```

## Configurazione e Installazione

1. **Clona o naviga nella directory del progetto**

2. **Installa le dipendenze**:
   ```cmd
   mvnw clean install
   ```
   Oppure, se hai Maven installato globalmente:
   ```cmd
   mvn clean install
   ```

3. **Imposta la variabile d'ambiente** (vedi la sezione "Ottenere il Token GitHub" sopra)

4. **Avvia il servizio MCP Calculator**:
   Assicurati che il servizio calcolatrice MCP del capitolo 1 sia in esecuzione su `http://localhost:8080/sse`. Deve essere attivo prima di avviare il client.

## Esecuzione dell'Applicazione

```cmd
mvnw clean package
java -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## Cosa Fa l'Applicazione

L'applicazione dimostra tre interazioni principali con il servizio calcolatrice:

1. **Addizione**: Calcola la somma di 24.5 e 17.3
2. **Radice quadrata**: Calcola la radice quadrata di 144
3. **Aiuto**: Mostra le funzioni disponibili della calcolatrice

## Output Atteso

Se l'esecuzione ha successo, dovresti vedere un output simile a:

```
The sum of 24.5 and 17.3 is 41.8.
The square root of 144 is 12.
The calculator service provides the following functions: add, subtract, multiply, divide, sqrt, power...
```

## Risoluzione dei Problemi

### Problemi Comuni

1. **"Variabile d'ambiente GITHUB_TOKEN non impostata"**
   - Assicurati di aver impostato la variabile d'ambiente `GITHUB_TOKEN`
   - Riavvia il terminale/prompt dei comandi dopo aver impostato la variabile

2. **"Connessione rifiutata a localhost:8080"**
   - Verifica che il servizio calcolatrice MCP sia in esecuzione sulla porta 8080
   - Controlla che nessun altro servizio stia usando la porta 8080

3. **"Autenticazione fallita"**
   - Controlla che il token GitHub sia valido e abbia i permessi corretti
   - Verifica di avere accesso a GitHub Models

4. **Errori di build Maven**
   - Assicurati di usare Java 21 o superiore: `java -version`
   - Prova a pulire la build: `mvnw clean`

### Debug

Per abilitare il logging di debug, aggiungi il seguente argomento JVM durante l'esecuzione:
```cmd
java -Dlogging.level.dev.langchain4j=DEBUG -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## Configurazione

L'applicazione è configurata per:
- Usare GitHub Models con il modello `gpt-4.1-nano`
- Connettersi al servizio MCP su `http://localhost:8080/sse`
- Usare un timeout di 60 secondi per le richieste
- Abilitare il logging delle richieste/risposte per il debug

## Dipendenze

Dipendenze principali usate in questo progetto:
- **LangChain4j**: per integrazione AI e gestione degli strumenti
- **LangChain4j MCP**: per il supporto al Model Context Protocol
- **LangChain4j GitHub Models**: per l'integrazione con GitHub Models
- **Spring Boot**: per il framework applicativo e l'iniezione delle dipendenze

## Licenza

Questo progetto è rilasciato sotto la licenza Apache License 2.0 - vedi il file [LICENSE](../../../../../../03-GettingStarted/03-llm-client/solution/java/LICENSE) per i dettagli.

**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica [Co-op Translator](https://github.com/Azure/co-op-translator). Pur impegnandoci per garantire accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un umano. Non siamo responsabili per eventuali malintesi o interpretazioni errate derivanti dall’uso di questa traduzione.