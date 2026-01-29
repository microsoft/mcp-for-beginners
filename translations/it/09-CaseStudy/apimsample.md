# Caso di Studio: Esporre un'API REST in API Management come server MCP

Azure API Management è un servizio che fornisce un Gateway sopra i tuoi endpoint API. Funziona come un proxy davanti alle tue API e può decidere cosa fare con le richieste in arrivo.

Utilizzandolo, puoi aggiungere una serie di funzionalità come:

- **Sicurezza**, puoi utilizzare tutto, dalle chiavi API, JWT fino all'identità gestita.
- **Limitazione del tasso**, una funzionalità utile è la possibilità di decidere quante chiamate possono essere effettuate in un determinato intervallo di tempo. Questo aiuta a garantire un'esperienza ottimale per tutti gli utenti e a evitare che il tuo servizio venga sovraccaricato di richieste.
- **Scalabilità e bilanciamento del carico**. Puoi configurare diversi endpoint per bilanciare il carico e decidere come effettuare il "bilanciamento del carico".
- **Funzionalità AI come caching semantico**, limite di token, monitoraggio dei token e altro. Queste funzionalità migliorano la reattività e ti aiutano a gestire meglio il consumo dei token. [Leggi di più qui](https://learn.microsoft.com/en-us/azure/api-management/genai-gateway-capabilities).

## Perché MCP + Azure API Management?

Il Model Context Protocol sta rapidamente diventando uno standard per le app AI agentiche e per esporre strumenti e dati in modo coerente. Azure API Management è una scelta naturale quando hai bisogno di "gestire" le API. I server MCP spesso si integrano con altre API per risolvere richieste verso uno strumento, ad esempio. Pertanto, combinare Azure API Management e MCP ha molto senso.

## Panoramica

In questo caso d'uso specifico, impareremo a esporre gli endpoint API come un server MCP. Facendo ciò, possiamo facilmente rendere questi endpoint parte di un'app agentica sfruttando al contempo le funzionalità di Azure API Management.

## Caratteristiche principali

- Puoi selezionare i metodi degli endpoint che desideri esporre come strumenti.
- Le funzionalità aggiuntive dipendono da ciò che configuri nella sezione delle policy per la tua API. Qui mostreremo come aggiungere la limitazione del tasso.

## Passo preliminare: importare un'API

Se hai già un'API in Azure API Management, ottimo, puoi saltare questo passaggio. In caso contrario, consulta questo link: [importare un'API in Azure API Management](https://learn.microsoft.com/en-us/azure/api-management/import-and-publish#import-and-publish-a-backend-api).

## Esporre un'API come server MCP

Per esporre gli endpoint API, segui questi passaggi:

1. Vai al Portale di Azure al seguente indirizzo <https://portal.azure.com/?Microsoft_Azure_ApiManagement=mcp>. Naviga alla tua istanza di API Management.

1. Nel menu a sinistra, seleziona **APIs > MCP Servers > + Create new MCP Server**.

1. In **API**, seleziona un'API REST da esporre come server MCP.

1. Seleziona una o più operazioni API da esporre come strumenti. Puoi selezionare tutte le operazioni o solo operazioni specifiche.

    ![Seleziona i metodi da esporre](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/create-mcp-server-small.png)

1. Seleziona **Create**.

1. Vai all'opzione di menu **APIs** e **MCP Servers**, dovresti vedere quanto segue:

    ![Visualizza il server MCP nel pannello principale](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-list.png)

    Il server MCP è stato creato e le operazioni API sono esposte come strumenti. Il server MCP è elencato nel pannello MCP Servers. La colonna URL mostra l'endpoint del server MCP che puoi chiamare per testare o utilizzare in un'applicazione client.

## Opzionale: Configurare le policy

Azure API Management ha il concetto base di policy, dove puoi configurare diverse regole per i tuoi endpoint, come ad esempio la limitazione del tasso o il caching semantico. Queste policy sono scritte in formato XML.

Ecco come configurare una policy per limitare il tasso del tuo server MCP:

1. Nel portale, sotto **APIs**, seleziona **MCP Servers**.

1. Seleziona il server MCP che hai creato.

1. Nel menu a sinistra, sotto **MCP**, seleziona **Policies**.

1. Nell'editor delle policy, aggiungi o modifica le policy che desideri applicare agli strumenti del server MCP. Le policy sono definite in formato XML. Ad esempio, puoi aggiungere una policy per limitare le chiamate agli strumenti del server MCP (in questo esempio, 5 chiamate ogni 30 secondi per indirizzo IP del client). Ecco un esempio di XML che imposta questa limitazione:

    ```xml
     <rate-limit-by-key calls="5" 
       renewal-period="30" 
       counter-key="@(context.Request.IpAddress)" 
       remaining-calls-variable-name="remainingCallsPerIP" 
    />
    ```

    Ecco un'immagine dell'editor delle policy:

    ![Editor delle policy](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-policies-small.png)

## Provarlo

Verifichiamo che il nostro server MCP funzioni come previsto.

Per questo, utilizzeremo Visual Studio Code e GitHub Copilot in modalità Agent. Aggiungeremo il server MCP a un file *mcp.json*. In questo modo, Visual Studio Code agirà come un client con capacità agentiche e gli utenti finali potranno digitare un prompt e interagire con il server.

Ecco come aggiungere il server MCP in Visual Studio Code:

1. Usa il comando **MCP: Add Server** dal Command Palette.

1. Quando richiesto, seleziona il tipo di server: **HTTP (HTTP o Server Sent Events)**.

1. Inserisci l'URL del server MCP in API Management. Esempio: **https://<apim-service-name>.azure-api.net/<api-name>-mcp/sse** (per endpoint SSE) o **https://<apim-service-name>.azure-api.net/<api-name>-mcp/mcp** (per endpoint MCP), nota la differenza tra i trasporti: `/sse` o `/mcp`.

1. Inserisci un ID server a tua scelta. Questo valore non è importante, ma ti aiuterà a ricordare cosa rappresenta questa istanza del server.

1. Seleziona se salvare la configurazione nelle impostazioni del workspace o nelle impostazioni utente.

  - **Impostazioni del workspace** - La configurazione del server viene salvata in un file .vscode/mcp.json disponibile solo nel workspace corrente.

    *mcp.json*

    ```json
    "servers": {
        "APIM petstore" : {
            "type": "sse",
            "url": "url-to-mcp-server/sse"
        }
    }
    ```

    oppure, se scegli HTTP in streaming come trasporto, sarà leggermente diverso:

    ```json
    "servers": {
        "APIM petstore" : {
            "type": "http",
            "url": "url-to-mcp-server/mcp"
        }
    }
    ```

  - **Impostazioni utente** - La configurazione del server viene aggiunta al file globale *settings.json* ed è disponibile in tutti i workspace. La configurazione sarà simile alla seguente:

    ![Impostazioni utente](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-servers-visual-studio-code.png)

1. Devi anche aggiungere una configurazione, un header per assicurarti che l'autenticazione verso Azure API Management funzioni correttamente. Utilizza un header chiamato **Ocp-Apim-Subscription-Key**.

    - Ecco come aggiungerlo alle impostazioni:

    ![Aggiungere l'header per l'autenticazione](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-with-header-visual-studio-code.png), questo farà apparire un prompt per chiederti il valore della chiave API, che puoi trovare nel Portale di Azure per la tua istanza di Azure API Management.

   - Per aggiungerlo a *mcp.json*, puoi farlo così:

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

### Usare la modalità Agent

Ora siamo pronti, sia nelle impostazioni che in *.vscode/mcp.json*. Proviamolo.

Dovrebbe esserci un'icona degli strumenti, dove sono elencati gli strumenti esposti dal tuo server:

![Strumenti dal server](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/tools-button-visual-studio-code.png)

1. Clicca sull'icona degli strumenti e dovresti vedere un elenco di strumenti come questo:

    ![Strumenti](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/select-tools-visual-studio-code.png)

1. Inserisci un prompt nella chat per invocare lo strumento. Ad esempio, se hai selezionato uno strumento per ottenere informazioni su un ordine, puoi chiedere all'agente informazioni su un ordine. Ecco un esempio di prompt:

    ```text
    get information from order 2
    ```

    Ora ti verrà presentata un'icona degli strumenti che ti chiede di procedere con l'esecuzione di uno strumento. Seleziona per continuare, dovresti vedere un output simile a questo:

    ![Risultato del prompt](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/chat-results-visual-studio-code.png)

    **Ciò che vedi sopra dipende dagli strumenti che hai configurato, ma l'idea è di ottenere una risposta testuale come quella sopra.**

## Riferimenti

Ecco come puoi approfondire:

- [Tutorial su Azure API Management e MCP](https://learn.microsoft.com/en-us/azure/api-management/export-rest-mcp-server)
- [Esempio Python: Proteggere server MCP remoti usando Azure API Management (sperimentale)](https://github.com/Azure-Samples/remote-mcp-apim-functions-python)

- [Laboratorio di autorizzazione client MCP](https://github.com/Azure-Samples/AI-Gateway/tree/main/labs/mcp-client-authorization)

- [Usare l'estensione Azure API Management per VS Code per importare e gestire API](https://learn.microsoft.com/en-us/azure/api-management/visual-studio-code-tutorial)

- [Registrare e scoprire server MCP remoti in Azure API Center](https://learn.microsoft.com/en-us/azure/api-center/register-discover-mcp-server)
- [AI Gateway](https://github.com/Azure-Samples/AI-Gateway) Ottimo repository che mostra molte capacità AI con Azure API Management
- [Workshop AI Gateway](https://azure-samples.github.io/AI-Gateway/) Contiene workshop utilizzando il Portale di Azure, un ottimo modo per iniziare a valutare le capacità AI.

**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire l'accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa dovrebbe essere considerato la fonte autorevole. Per informazioni critiche, si consiglia una traduzione professionale eseguita da un traduttore umano. Non siamo responsabili per eventuali fraintendimenti o interpretazioni errate derivanti dall'uso di questa traduzione.