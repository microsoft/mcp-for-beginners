# Generatore di Piano di Studio con Chainlit & Microsoft Learn Docs MCP

## Prerequisiti

- Python 3.8 o superiore
- pip (gestore pacchetti Python)
- Accesso a Internet per connettersi al server Microsoft Learn Docs MCP

## Installazione

1. Clona questo repository o scarica i file del progetto.
2. Installa le dipendenze necessarie:

   ```bash
   pip install -r requirements.txt
   ```

## Utilizzo

### Scenario 1: Query semplice ai Docs MCP
Un client da riga di comando che si connette al server Docs MCP, invia una query e stampa il risultato.

1. Esegui lo script:
   ```bash
   python scenario1.py
   ```
2. Inserisci la tua domanda sulla documentazione al prompt.

### Scenario 2: Generatore di Piano di Studio (App Web Chainlit)
Un'interfaccia web (utilizzando Chainlit) che consente agli utenti di generare un piano di studio personalizzato, settimana per settimana, su qualsiasi argomento tecnico.

1. Avvia l'app Chainlit:
   ```bash
   chainlit run scenario2.py
   ```
2. Apri l'URL locale fornito nel terminale (ad esempio, http://localhost:8000) nel tuo browser.
3. Nella finestra di chat, inserisci il tuo argomento di studio e il numero di settimane che desideri studiare (ad esempio, "Certificazione AI-900, 8 settimane").
4. L'app risponderà con un piano di studio settimanale, includendo link alla documentazione pertinente di Microsoft Learn.

**Variabili d'ambiente richieste:**

Per utilizzare lo Scenario 2 (l'app web Chainlit con Azure OpenAI), devi impostare le seguenti variabili d'ambiente in un file `.env` nella directory `python`:

```
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=
AZURE_OPENAI_API_KEY=
AZURE_OPENAI_ENDPOINT=
AZURE_OPENAI_API_VERSION=
```

Compila questi valori con i dettagli della tua risorsa Azure OpenAI prima di eseguire l'app.

> [!TIP]
> Puoi facilmente distribuire i tuoi modelli utilizzando [Azure AI Foundry](https://ai.azure.com/).

### Scenario 3: Documentazione in Editor con MCP Server in VS Code

Invece di cambiare scheda del browser per cercare la documentazione, puoi portare Microsoft Learn Docs direttamente nel tuo VS Code utilizzando il server MCP. Questo ti consente di:
- Cercare e leggere la documentazione direttamente in VS Code senza lasciare l'ambiente di codifica.
- Fare riferimento alla documentazione e inserire link direttamente nel tuo README o nei file del corso.
- Usare GitHub Copilot e MCP insieme per un flusso di lavoro di documentazione alimentato dall'AI.

**Esempi di utilizzo:**
- Aggiungere rapidamente link di riferimento a un README mentre scrivi la documentazione di un corso o progetto.
- Usare Copilot per generare codice e MCP per trovare e citare istantaneamente la documentazione pertinente.
- Rimanere concentrato nel tuo editor e aumentare la produttività.

> [!IMPORTANT]
> Assicurati di avere una configurazione valida [`mcp.json`](../../../../../../09-CaseStudy/docs-mcp/solution/scenario3/mcp.json) nel tuo workspace (posizione: `.vscode/mcp.json`).

## Perché Chainlit per lo Scenario 2?

Chainlit è un framework open-source moderno per costruire applicazioni web conversazionali. Rende facile creare interfacce utente basate su chat che si connettono a servizi backend come il server Microsoft Learn Docs MCP. Questo progetto utilizza Chainlit per fornire un modo semplice e interattivo per generare piani di studio personalizzati in tempo reale. Grazie a Chainlit, puoi costruire e distribuire rapidamente strumenti basati su chat che migliorano la produttività e l'apprendimento.

## Cosa Fa

Questa app consente agli utenti di creare un piano di studio personalizzato semplicemente inserendo un argomento e una durata. L'app analizza il tuo input, interroga il server Microsoft Learn Docs MCP per contenuti pertinenti e organizza i risultati in un piano strutturato settimana per settimana. Le raccomandazioni di ogni settimana vengono visualizzate nella chat, rendendo facile seguire e monitorare i progressi. L'integrazione garantisce che tu abbia sempre accesso alle risorse di apprendimento più recenti e pertinenti.

## Esempi di Query

Prova queste query nella finestra di chat per vedere come risponde l'app:

- `Certificazione AI-900, 8 settimane`
- `Imparare Azure Functions, 4 settimane`
- `Azure DevOps, 6 settimane`
- `Ingegneria dei dati su Azure, 10 settimane`
- `Fondamenti di sicurezza Microsoft, 5 settimane`
- `Power Platform, 7 settimane`
- `Servizi AI di Azure, 12 settimane`
- `Architettura cloud, 9 settimane`

Questi esempi dimostrano la flessibilità dell'app per diversi obiettivi di apprendimento e durate.

## Riferimenti

- [Documentazione Chainlit](https://docs.chainlit.io/)
- [Documentazione MCP](https://github.com/MicrosoftDocs/mcp)

---

**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire l'accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa dovrebbe essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un traduttore umano. Non siamo responsabili per eventuali incomprensioni o interpretazioni errate derivanti dall'uso di questa traduzione.