# Caso di studio: Esporre REST API in API Management come server MCP

Azure API Management è un servizio che fornisce un Gateway sopra i tuoi endpoint API. Il funzionamento è che Azure API Management agisce come un proxy davanti alle tue API e può decidere cosa fare con le richieste in ingresso.

Usandolo, aggiungi una serie di funzionalità come:

- **Sicurezza**, puoi utilizzare tutto, dalle chiavi API, JWT all’identità gestita.
- **Limitazione della velocità**, una grande funzionalità è poter decidere quante chiamate possono passare in una certa unità di tempo. Questo aiuta a garantire che tutti gli utenti abbiano una buona esperienza e anche che il tuo servizio non venga sovraccaricato di richieste.
- **Scalabilità e bilanciamento del carico**. Puoi configurare un numero di endpoint per bilanciare il carico e puoi anche decidere come "bilanciare il carico".
- **Funzionalità AI come caching semantico**, limite di token e monitoraggio dei token e altro ancora. Queste sono ottime funzionalità che migliorano la reattività e ti aiutano a tenere sotto controllo la spesa dei token. [Leggi di più qui](https://learn.microsoft.com/en-us/azure/api-management/genai-gateway-capabilities).

## Perché MCP + Azure API Management?

Model Context Protocol sta rapidamente diventando uno standard per le app AI agentiche e per come esporre strumenti e dati in modo coerente. Azure API Management è una scelta naturale quando hai bisogno di "gestire" API. I server MCP spesso si integrano con altre API per risolvere le richieste verso uno strumento per esempio. Pertanto combinare Azure API Management e MCP ha molto senso.

## Panoramica

In questo caso d'uso specifico impareremo a esporre gli endpoint API come un server MCP. Facendo questo, possiamo facilmente rendere questi endpoint parte di un'app agentica sfruttando anche le funzionalità di Azure API Management.

## Funzionalità principali

- Selezioni i metodi dell'endpoint che vuoi esporre come strumenti.
- Le funzionalità aggiuntive dipendono da ciò che configuri nella sezione policy della tua API. Qui ti mostreremo come aggiungere la limitazione della velocità.

## Passaggio preliminare: importa un'API

Se hai già un'API in Azure API Management, ottimo, puoi saltare questo passaggio. Altrimenti, consulta questo link, [importare un'API in Azure API Management](https://learn.microsoft.com/en-us/azure/api-management/import-and-publish#import-and-publish-a-backend-api).

## Esporre API come server MCP

Per esporre gli endpoint API, segui questi passaggi:

1. Vai al portale Azure all’indirizzo <https://portal.azure.com/?Microsoft_Azure_ApiManagement=mcp>
Naviga alla tua istanza di API Management.

1. Nel menu a sinistra, seleziona APIs > MCP Servers > + Crea nuovo server MCP.

1. In API, seleziona un'API REST da esporre come server MCP.

1. Seleziona una o più operazioni API da esporre come strumenti. Puoi selezionare tutte le operazioni o solo operazioni specifiche.

    ![Select methods to expose](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/create-mcp-server-small.png)


1. Seleziona **Crea**.

1. Vai a menu **APIs** e **MCP Servers**, dovresti vedere quanto segue:

    ![See the MCP Server in the main pane](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-list.png)

    Il server MCP è creato e le operazioni API sono esposte come strumenti. Il server MCP è elencato nel pannello MCP Servers. La colonna URL mostra l'endpoint del server MCP che puoi chiamare per test o all'interno di un'applicazione client.

## Opzionale: Configura le policy

Azure API Management ha il concetto chiave delle policy in cui imposti diverse regole per i tuoi endpoint come ad esempio limitazione della velocità o caching semantico. Queste policy sono scritte in XML.

Ecco come puoi configurare una policy per limitare la velocità del tuo server MCP:

1. Nel portale, sotto APIs, seleziona **MCP Servers**.

1. Seleziona il server MCP che hai creato.

1. Nel menu a sinistra, sotto MCP, seleziona **Policies**.

1. Nell’editor delle policy, aggiungi o modifica le policy che vuoi applicare agli strumenti del server MCP. Le policy sono definite in formato XML. Per esempio, puoi aggiungere una policy per limitare le chiamate agli strumenti del server MCP (in questo esempio, 5 chiamate ogni 30 secondi per indirizzo IP client). Ecco l’XML che provocherà la limitazione:

    ```xml
     <rate-limit-by-key calls="5" 
       renewal-period="30" 
       counter-key="@(context.Request.IpAddress)" 
       remaining-calls-variable-name="remainingCallsPerIP" 
    />
    ```

    Ecco un’immagine dell’editor policy:

    ![Policy editor](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-policies-small.png)
 
## Provalo

Assicuriamoci che il nostro server MCP funzioni come previsto.

> [!NOTE]
> Azure API Management attualmente espone questo server tramite l’endpoint HTTP Streamable `/mcp`.
> Il vecchio trasporto HTTP+SSE `/sse` è deprecato e
> dovrebbe essere usato solo con client legacy.

Per questo, useremo Visual Studio Code e GitHub Copilot con la sua modalità Agent. Aggiungeremo il server MCP a un file *mcp.json*. Facendo così, Visual Studio Code agirà come un client con capacità agentiche e gli utenti finali potranno digitare un prompt e interagire con detto server.

Vediamo come aggiungere il server MCP in Visual Studio Code:

1. Usa il comando MCP: **Add Server dal Command Palette**.

1. Quando richiesto, seleziona il tipo di server: **HTTP (HTTP o Server Sent Events)**.

1. Inserisci l'URL HTTP Streamable mostrato per il server MCP in API Management.
    Per esempio:
    `https://<apim-service-name>.azure-api.net/<api-name>-mcp/mcp`.

1. Inserisci un ID server a tua scelta. Questo non è un valore importante ma ti aiuterà a ricordare cosa rappresenta questa istanza server.

1. Seleziona se salvare la configurazione nelle impostazioni dello spazio di lavoro o nelle impostazioni utente.

  - **Impostazioni workspace** - La configurazione del server viene salvata in un file .vscode/mcp.json disponibile solo nello spazio di lavoro corrente.

    *mcp.json*

    ```json
    "servers": {
        "APIM petstore" : {
            "type": "http",
            "url": "url-to-mcp-server/mcp"
        }
    }
    ```

  - **Impostazioni utente** - La configurazione del server viene aggiunta al file globale *settings.json* ed è disponibile in tutti gli spazi di lavoro. La configurazione è simile a questa:

    ![User setting](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-servers-visual-studio-code.png)

1. Devi anche aggiungere una configurazione, un header per assicurarti che si autentichi correttamente verso Azure API Management. Usa un header chiamato **Ocp-Apim-Subscription-Key**. 

    - Ecco come aggiungerlo alle impostazioni:

    ![Adding header for authentication](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-with-header-visual-studio-code.png), questo farà comparire un prompt che chiede il valore della chiave API che puoi trovare nel portale Azure per la tua istanza di Azure API Management.

   - Per aggiungerlo invece a *mcp.json*, puoi farlo così:

    ```json
    "inputs": [
      {
        "type": "promptString",
        "id": "apim_key",
        "description": "API Key for Azure API Management",
        "password": true
      }
    ]
    "servers": {
        "APIM petstore" : {
            "type": "http",
            "url": "url-to-mcp-server/mcp",
            "headers": {
                "Ocp-Apim-Subscription-Key": "Bearer ${input:apim_key}"
            }
        }
    }
    ```

### Usa la modalità Agent

Ora siamo pronti sia nelle impostazioni che in *.vscode/mcp.json*. Proviamolo.

Dovrebbe comparire un’icona Strumenti come questa, dove sono elencati gli strumenti esposti dal tuo server:

![Tools from the server](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/tools-button-visual-studio-code.png)

1. Clicca sull’icona strumenti e dovresti vedere una lista di strumenti così:

    ![Tools](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/select-tools-visual-studio-code.png)

1. Inserisci un prompt nella chat per invocare lo strumento. Ad esempio, se hai selezionato uno strumento per ottenere informazioni su un ordine, puoi chiedere all’agente dell’ordine. Ecco un esempio di prompt:

    ```text
    get information from order 2
    ```

    Ora ti verrà mostrata un’icona strumenti che ti chiederà di procedere a usare uno strumento. Seleziona per continuare ad usare lo strumento, vedrai ora un output come questo:

    ![Result from prompt](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/chat-results-visual-studio-code.png)

    **ciò che vedi sopra dipende dagli strumenti che hai configurato, ma l’idea è di ottenere una risposta testuale come quella sopra**


## Riferimenti

Ecco come puoi approfondire:

- [Tutorial su Azure API Management e MCP](https://learn.microsoft.com/en-us/azure/api-management/export-rest-mcp-server)
- [Esempio Python: Server MCP remoti sicuri usando Azure API Management (sperimentale)](https://github.com/Azure-Samples/remote-mcp-apim-functions-python)

- [Laboratorio di autorizzazione client MCP](https://github.com/Azure-Samples/AI-Gateway/tree/main/labs/mcp-client-authorization)

- [Usa l’estensione Azure API Management per VS Code per importare e gestire API](https://learn.microsoft.com/en-us/azure/api-management/visual-studio-code-tutorial)

- [Registra e scopri server MCP remoti in Azure API Center](https://learn.microsoft.com/en-us/azure/api-center/register-discover-mcp-server)
- [AI Gateway](https://github.com/Azure-Samples/AI-Gateway) Ottimo repository che mostra molte funzionalità AI con Azure API Management
- [Workshop AI Gateway](https://azure-samples.github.io/AI-Gateway/) Contiene workshop usando Azure Portal, che è un ottimo modo per iniziare a valutare le capacità AI.

## Cosa c’è dopo

- Torna a: [Panoramica dei casi di studio](./README.md)
- Successivo: [Agenti di viaggio Azure AI](./travelagentsample.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Questo documento è stato tradotto utilizzando il servizio di traduzione AI [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire la precisione, si prega di notare che le traduzioni automatizzate possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un essere umano. Non siamo responsabili per eventuali malintesi o interpretazioni errate derivanti dall’uso di questa traduzione.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->