# Servizio Calcolatrice Base MCP

Questo servizio offre operazioni di calcolo base tramite il Model Context Protocol (MCP). È progettato come un esempio semplice per chi inizia a imparare le implementazioni MCP.

Per maggiori informazioni, consulta [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk)

## Funzionalità

Questo servizio calcolatrice offre le seguenti capacità:

1. **Operazioni Aritmetiche di Base**:
   - Addizione di due numeri
   - Sottrazione di un numero da un altro
   - Moltiplicazione di due numeri
   - Divisione di un numero per un altro (con controllo della divisione per zero)

## Uso del tipo `stdio`
  
## Configurazione

1. **Configura i Server MCP**:
   - Apri il tuo workspace in VS Code.
   - Crea un file `.vscode/mcp.json` nella cartella del workspace per configurare i server MCP. Esempio di configurazione:

     ```jsonc
     {
       "inputs": [
         {
           "type": "promptString",
           "id": "repository-root",
           "description": "The absolute path to the repository root"
         }
       ],
       "servers": {
         "calculator-mcp-dotnet": {
           "type": "stdio",
           "command": "dotnet",
           "args": [
             "run",
             "--project",
             "${input:repository-root}/03-GettingStarted/samples/csharp/src/calculator.csproj"
           ]
         }
       }
     }
     ```

   - Ti verrà chiesto di inserire la root del repository GitHub, che puoi ottenere con il comando `git rev-parse --show-toplevel`.

## Uso del Servizio

Il servizio espone i seguenti endpoint API tramite il protocollo MCP:

- `add(a, b)`: Somma due numeri
- `subtract(a, b)`: Sottrae il secondo numero dal primo
- `multiply(a, b)`: Moltiplica due numeri
- `divide(a, b)`: Divide il primo numero per il secondo (con controllo zero)
- isPrime(n): Verifica se un numero è primo

## Test con Github Copilot Chat in VS Code

1. Prova a fare una richiesta al servizio usando il protocollo MCP. Ad esempio, puoi chiedere:
   - "Add 5 and 3"
   - "Subtract 10 from 4"
   - "Multiply 6 and 7"
   - "Divide 8 by 2"
   - "Does 37854 prime?"
   - "What are the 3 prime numbers before after 4242?"
2. Per assicurarti che vengano usati gli strumenti, aggiungi #MyCalculator al prompt. Per esempio:
   - "Add 5 and 3 #MyCalculator"
   - "Subtract 10 from 4 #MyCalculator"

## Versione Containerizzata

La soluzione precedente è ottima se hai installato il .NET SDK e tutte le dipendenze sono a posto. Tuttavia, se vuoi condividere la soluzione o eseguirla in un ambiente diverso, puoi usare la versione containerizzata.

1. Avvia Docker e assicurati che sia in esecuzione.
1. Da un terminale, naviga nella cartella `03-GettingStarted\samples\csharp\src`
1. Per costruire l’immagine Docker per il servizio calcolatrice, esegui il seguente comando (sostituisci `<YOUR-DOCKER-USERNAME>` con il tuo username Docker Hub):
   ```bash
   docker build -t <YOUR-DOCKER-USERNAME>/mcp-calculator .
   ``` 
1. Dopo che l’immagine è stata costruita, caricala su Docker Hub. Esegui il comando seguente:
   ```bash
    docker push <YOUR-DOCKER-USERNAME>/mcp-calculator
  ```

## Usa la Versione Dockerizzata

1. Nel file `.vscode/mcp.json`, sostituisci la configurazione del server con la seguente:
   ```json
    "mcp-calc": {
      "command": "docker",
      "args": [
        "run",
        "--rm",
        "-i",
        "<YOUR-DOCKER-USERNAME>/mcp-calc"
      ],
      "envFile": "",
      "env": {}
    }
   ```
   Guardando la configurazione, puoi vedere che il comando è `docker` e gli argomenti sono `run --rm -i <YOUR-DOCKER-USERNAME>/mcp-calc`. Il flag `--rm` assicura che il container venga rimosso dopo l’arresto, mentre il flag `-i` permette di interagire con l’input standard del container. L’ultimo argomento è il nome dell’immagine che abbiamo appena costruito e caricato su Docker Hub.

## Testa la Versione Dockerizzata

Avvia il Server MCP cliccando il piccolo pulsante Start sopra `"mcp-calc": {`, e come prima puoi chiedere al servizio calcolatrice di fare qualche calcolo per te.

**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica [Co-op Translator](https://github.com/Azure/co-op-translator). Pur impegnandoci per garantire accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un umano. Non ci assumiamo alcuna responsabilità per eventuali malintesi o interpretazioni errate derivanti dall’uso di questa traduzione.