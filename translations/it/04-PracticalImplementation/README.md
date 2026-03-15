# Implementazione Pratica

[![Come Costruire, Testare e Distribuire App MCP con Strumenti e Flussi di Lavoro Reali](../../../translated_images/it/05.64bea204e25ca891.webp)](https://youtu.be/vCN9-mKBDfQ)

_(Clicca sull'immagine sopra per vedere il video di questa lezione)_

L'implementazione pratica è dove il potere del Model Context Protocol (MCP) diventa tangibile. Sebbene comprendere la teoria e l'architettura dietro MCP sia importante, il vero valore emerge quando applichi questi concetti per costruire, testare e distribuire soluzioni che risolvono problemi del mondo reale. Questo capitolo colma il divario tra conoscenza concettuale e sviluppo pratico, guidandoti attraverso il processo di dare vita alle applicazioni basate su MCP.

Sia che tu stia sviluppando assistenti intelligenti, integrando l'IA nei flussi di lavoro aziendali o creando strumenti personalizzati per l'elaborazione dei dati, MCP fornisce una base flessibile. Il suo design agnostico rispetto al linguaggio e gli SDK ufficiali per i linguaggi di programmazione più diffusi lo rendono accessibile a un'ampia gamma di sviluppatori. Sfruttando questi SDK, puoi prototipare rapidamente, iterare e scalare le tue soluzioni su diverse piattaforme e ambienti.

Nelle sezioni seguenti troverai esempi pratici, codice di esempio e strategie di distribuzione che dimostrano come implementare MCP in C#, Java con Spring, TypeScript, JavaScript e Python. Imparerai anche come eseguire il debug e testare i server MCP, gestire le API e distribuire soluzioni nel cloud utilizzando Azure. Queste risorse pratiche sono progettate per accelerare il tuo apprendimento e aiutarti a costruire con sicurezza applicazioni MCP robuste e pronte per la produzione.

## Panoramica

Questa lezione si concentra sugli aspetti pratici dell'implementazione MCP in diversi linguaggi di programmazione. Esploreremo come utilizzare gli SDK MCP in C#, Java con Spring, TypeScript, JavaScript e Python per costruire applicazioni robuste, eseguire il debug e testare server MCP e creare risorse, prompt e strumenti riutilizzabili.

## Obiettivi di Apprendimento

Al termine di questa lezione, sarai in grado di:

- Implementare soluzioni MCP utilizzando gli SDK ufficiali in vari linguaggi di programmazione
- Eseguire il debug e testare i server MCP in modo sistematico
- Creare e utilizzare funzionalità server (Risorse, Prompt e Strumenti)
- Progettare flussi di lavoro MCP efficaci per compiti complessi
- Ottimizzare le implementazioni MCP per prestazioni e affidabilità

## Risorse SDK Ufficiali

Il Model Context Protocol offre SDK ufficiali per più linguaggi (allineati con [Specifiche MCP 2025-11-25](https://spec.modelcontextprotocol.io/specification/2025-11-25/)):

- [SDK C#](https://github.com/modelcontextprotocol/csharp-sdk)
- [SDK Java con Spring](https://github.com/modelcontextprotocol/java-sdk) **Nota:** richiede la dipendenza da [Project Reactor](https://projectreactor.io). (Vedi [discussione issue 246](https://github.com/orgs/modelcontextprotocol/discussions/246).)
- [SDK TypeScript](https://github.com/modelcontextprotocol/typescript-sdk)
- [SDK Python](https://github.com/modelcontextprotocol/python-sdk)
- [SDK Kotlin](https://github.com/modelcontextprotocol/kotlin-sdk)
- [SDK Go](https://github.com/modelcontextprotocol/go-sdk)

## Lavorare con gli SDK MCP

Questa sezione fornisce esempi pratici di implementazione MCP in diversi linguaggi di programmazione. Puoi trovare codice di esempio nella directory `samples` organizzata per linguaggio.

### Esempi Disponibili

Il repository include [implementazioni di esempio](../../../04-PracticalImplementation/samples) nei seguenti linguaggi:

- [C#](./samples/csharp/README.md)
- [Java con Spring](./samples/java/containerapp/README.md)
- [TypeScript](./samples/typescript/README.md)
- [JavaScript](./samples/javascript/README.md)
- [Python](./samples/python/README.md)

Ogni esempio dimostra i concetti chiave MCP e i modelli di implementazione per quel linguaggio ed ecosistema specifico.

### Guide Pratiche

Guide aggiuntive per l'implementazione pratica di MCP:

- [Paginazione e Grandi Set di Risultati](./pagination/README.md) - Gestire la paginazione basata su cursore per strumenti, risorse e grandi dataset

## Funzionalità Core del Server

I server MCP possono implementare qualsiasi combinazione di queste funzionalità:

### Risorse

Le risorse forniscono contesto e dati per l'utente o il modello AI da utilizzare:

- Repository di documenti
- Basi di conoscenza
- Fonti di dati strutturati
- Sistemi di file

### Prompt

I prompt sono messaggi e flussi di lavoro template per gli utenti:

- Modelli di conversazione predefiniti
- Schemi di interazione guidata
- Strutture di dialogo specializzate

### Strumenti

Gli strumenti sono funzioni che il modello AI può eseguire:

- Utilità di elaborazione dati
- Integrazioni con API esterne
- Capacità computazionali
- Funzionalità di ricerca

## Implementazioni di Esempio: Implementazione in C#

Il repository ufficiale SDK C# contiene diverse implementazioni di esempio che mostrano diversi aspetti di MCP:

- **Client MCP Base**: esempio semplice che mostra come creare un client MCP e chiamare strumenti
- **Server MCP Base**: implementazione minimale del server con registrazione base di uno strumento
- **Server MCP Avanzato**: server completo con registrazione strumenti, autenticazione e gestione degli errori
- **Integrazione ASP.NET**: esempi che mostrano l'integrazione con ASP.NET Core
- **Modelli di Implementazione Strumenti**: vari modelli per implementare strumenti con diversi livelli di complessità

L'SDK MCP C# è in anteprima e le API possono cambiare. Aggiorneremo continuamente questo blog man mano che l'SDK evolve.

### Funzionalità Chiave

- [Nuget MCP C# ModelContextProtocol](https://www.nuget.org/packages/ModelContextProtocol)
- Costruire il tuo [primo Server MCP](https://devblogs.microsoft.com/dotnet/build-a-model-context-protocol-mcp-server-in-csharp/).

Per esempi completi di implementazione C#, visita il [repository ufficiale degli esempi SDK C#](https://github.com/modelcontextprotocol/csharp-sdk)

## Implementazione di esempio: Implementazione Java con Spring

L'SDK Java con Spring offre opzioni robuste per l'implementazione MCP con funzionalità enterprise-grade.

### Funzionalità Chiave

- Integrazione con Spring Framework
- Forte tipizzazione
- Supporto alla programmazione reattiva
- Gestione completa degli errori

Per un esempio completo di implementazione Java con Spring, vedi [Esempio Java con Spring](samples/java/containerapp/README.md) nella directory degli esempi.

## Implementazione di esempio: Implementazione JavaScript

L'SDK JavaScript fornisce un approccio leggero e flessibile all'implementazione MCP.

### Funzionalità Chiave

- Supporto Node.js e browser
- API basata su Promise
- Integrazione semplice con Express e altri framework
- Supporto WebSocket per streaming

Per un esempio completo di implementazione JavaScript, vedi [Esempio JavaScript](samples/javascript/README.md) nella directory degli esempi.

## Implementazione di esempio: Implementazione Python

L'SDK Python offre un approccio Pythonico all'implementazione MCP con ottime integrazioni per framework ML.

### Funzionalità Chiave

- Supporto async/await con asyncio
- Integrazione FastAPI``
- Registrazione strumenti semplice
- Integrazione nativa con librerie ML popolari

Per un esempio completo di implementazione Python, vedi [Esempio Python](samples/python/README.md) nella directory degli esempi.

## Gestione API

Azure API Management è una grande risposta a come possiamo mettere in sicurezza i server MCP. L'idea è mettere un'istanza di Azure API Management davanti al tuo server MCP e lasciarla gestire funzionalità che probabilmente vorrai come:

- limitazione del rateo
- gestione token
- monitoraggio
- bilanciamento del carico
- sicurezza

### Esempio Azure

Ecco un esempio Azure che fa esattamente questo, cioè [creare un server MCP e metterlo in sicurezza con Azure API Management](https://github.com/Azure-Samples/remote-mcp-apim-functions-python).

Vedi come avviene il flusso di autorizzazione nell'immagine sottostante:

![APIM-MCP](https://github.com/Azure-Samples/remote-mcp-apim-functions-python/blob/main/mcp-client-authorization.gif?raw=true)

Nell'immagine precedente accade quanto segue:

- Autenticazione/Autorizzazione avviene usando Microsoft Entra.
- Azure API Management agisce come gateway e usa policy per indirizzare e gestire il traffico.
- Azure Monitor registra tutte le richieste per ulteriori analisi.

#### Flusso di autorizzazione

Diamo un'occhiata al flusso di autorizzazione in maggior dettaglio:

![Sequence Diagram](https://github.com/Azure-Samples/remote-mcp-apim-functions-python/blob/main/infra/app/apim-oauth/diagrams/images/mcp-client-auth.png?raw=true)

#### Specifica autorizzazione MCP

Scopri di più sulla [specifica autorizzazione MCP](https://spec.modelcontextprotocol.io/specification/2025-11-25/basic/authorization/)

## Distribuire un Server MCP Remoto su Azure

Vediamo se possiamo distribuire l'esempio menzionato prima:

1. Clona il repo

    ```bash
    git clone https://github.com/Azure-Samples/remote-mcp-apim-functions-python.git
    cd remote-mcp-apim-functions-python
    ```

1. Registra il provider di risorse `Microsoft.App`.

   - Se usi Azure CLI, esegui `az provider register --namespace Microsoft.App --wait`.
   - Se usi Azure PowerShell, esegui `Register-AzResourceProvider -ProviderNamespace Microsoft.App`. Poi esegui `(Get-AzResourceProvider -ProviderNamespace Microsoft.App).RegistrationState` dopo un po' per verificare se la registrazione è completa.

1. Esegui questo comando [azd](https://aka.ms/azd) per fornire il servizio API Management, la function app (con codice) e tutte le altre risorse Azure richieste

    ```shell
    azd up
    ```

    Questo comando dovrebbe distribuire tutte le risorse cloud su Azure

### Testare il tuo server con MCP Inspector

1. In una **nuova finestra terminale**, installa ed esegui MCP Inspector

    ```shell
    npx @modelcontextprotocol/inspector
    ```

    Dovresti vedere un'interfaccia simile a:

    ![Connect to Node inspector](../../../translated_images/it/connect.141db0b2bd05f096.webp)

1. CTRL clicca per caricare la web app MCP Inspector dall'URL visualizzato dall'app (es. [http://127.0.0.1:6274/#resources](http://127.0.0.1:6274/#resources))
1. Imposta il tipo di trasporto su `SSE`
1. Imposta l'URL al tuo endpoint SSE API Management attivo visualizzato dopo `azd up` e **Connetti**:

    ```shell
    https://<apim-servicename-from-azd-output>.azure-api.net/mcp/sse
    ```

1. **Elenca Strumenti**.  Clicca su uno strumento e **Esegui Strumento**.  

Se tutti i passaggi sono andati a buon fine, ora dovresti essere connesso al server MCP e aver potuto chiamare uno strumento.

## Server MCP per Azure

[Remote-mcp-functions](https://github.com/Azure-Samples/remote-mcp-functions-dotnet): questa serie di repository è un modello quickstart per costruire e distribuire server MCP remoti personalizzati usando Azure Functions con Python, C# .NET o Node/TypeScript.

I Samples forniscono una soluzione completa che permette agli sviluppatori di:

- Costruire ed eseguire in locale: sviluppare ed eseguire il debug di un server MCP sulla macchina locale
- Distribuire su Azure: distribuire facilmente nel cloud con un semplice comando azd up
- Connettersi da client: connettersi al server MCP da vari client inclusi la modalità agente Copilot di VS Code e lo strumento MCP Inspector

### Funzionalità Chiave

- Sicurezza by design: il server MCP è protetto usando chiavi e HTTPS
- Opzioni di autenticazione: supporta OAuth usando autenticazione integrata e/o API Management
- Isolamento di rete: permette isolamento di rete usando Azure Virtual Networks (VNET)
- Architettura serverless: sfrutta Azure Functions per esecuzione scalabile basata su eventi
- Sviluppo locale: supporto completo per sviluppo e debug locali
- Distribuzione semplice: processo di distribuzione semplificato su Azure

Il repository include tutti i file di configurazione necessari, codice sorgente e definizioni di infrastruttura per iniziare rapidamente con un'implementazione di server MCP pronta per la produzione.

- [Azure Remote MCP Functions Python](https://github.com/Azure-Samples/remote-mcp-functions-python) - Implementazione di esempio MCP usando Azure Functions con Python

- [Azure Remote MCP Functions .NET](https://github.com/Azure-Samples/remote-mcp-functions-dotnet) - Implementazione di esempio MCP usando Azure Functions con C# .NET

- [Azure Remote MCP Functions Node/Typescript](https://github.com/Azure-Samples/remote-mcp-functions-typescript) - Implementazione di esempio MCP usando Azure Functions con Node/TypeScript.

## Punti Chiave

- Gli SDK MCP forniscono strumenti specifici per linguaggio per implementare soluzioni MCP robuste
- Il processo di debug e test è critico per applicazioni MCP affidabili
- I template di prompt riutilizzabili permettono interazioni AI coerenti
- I flussi di lavoro ben progettati possono orchestrare compiti complessi usando più strumenti
- Implementare soluzioni MCP richiede considerazioni su sicurezza, prestazioni e gestione errori

## Esercizio

Progetta un flusso di lavoro MCP pratico che affronti un problema del mondo reale nel tuo dominio:

1. Identifica 3-4 strumenti che sarebbero utili per risolvere questo problema
2. Crea un diagramma del flusso di lavoro che mostri come questi strumenti interagiscono
3. Implementa una versione base di uno degli strumenti usando il tuo linguaggio preferito
4. Crea un template di prompt che aiuti il modello a usare efficacemente il tuo strumento

## Risorse Aggiuntive

---

## Cosa Viene Dopo

Prossimo: [Argomenti Avanzati](../05-AdvancedTopics/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica AI [Co-op Translator](https://github.com/Azure/co-op-translator). Pur impegnandoci per garantire l’accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o inesattezze. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche si raccomanda una traduzione professionale effettuata da un traduttore umano. Non siamo responsabili per eventuali fraintendimenti o interpretazioni errate derivanti dall’uso di questa traduzione.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->