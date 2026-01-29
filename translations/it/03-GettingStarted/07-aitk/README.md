# Utilizzare un server con l'estensione AI Toolkit per Visual Studio Code

Quando crei un agente AI, non si tratta solo di generare risposte intelligenti; si tratta anche di dare al tuo agente la capacità di agire. È qui che entra in gioco il Model Context Protocol (MCP). MCP semplifica l'accesso degli agenti a strumenti e servizi esterni in modo coerente. Pensalo come collegare il tuo agente a una cassetta degli attrezzi che può *effettivamente* utilizzare.

Supponiamo che tu colleghi un agente al tuo server MCP per calcolatrici. Improvvisamente, il tuo agente può eseguire operazioni matematiche semplicemente ricevendo un prompt come "Quanto fa 47 per 89?"—senza bisogno di codificare logiche o costruire API personalizzate.

## Panoramica

Questa lezione spiega come collegare un server MCP per calcolatrici a un agente utilizzando l'estensione [AI Toolkit](https://aka.ms/AIToolkit) in Visual Studio Code, permettendo al tuo agente di eseguire operazioni matematiche come addizione, sottrazione, moltiplicazione e divisione attraverso il linguaggio naturale.

AI Toolkit è un'estensione potente per Visual Studio Code che semplifica lo sviluppo di agenti. Gli ingegneri AI possono facilmente creare applicazioni AI sviluppando e testando modelli generativi—localmente o nel cloud. L'estensione supporta la maggior parte dei principali modelli generativi disponibili oggi.

*Nota*: AI Toolkit supporta attualmente Python e TypeScript.

## Obiettivi di apprendimento

Alla fine di questa lezione, sarai in grado di:

- Utilizzare un server MCP tramite AI Toolkit.
- Configurare un agente per consentirgli di scoprire e utilizzare gli strumenti forniti dal server MCP.
- Usare strumenti MCP tramite linguaggio naturale.

## Approccio

Ecco come affrontare il processo a livello generale:

- Creare un agente e definire il suo prompt di sistema.
- Creare un server MCP con strumenti per calcolatrici.
- Collegare l'Agent Builder al server MCP.
- Testare l'invocazione degli strumenti dell'agente tramite linguaggio naturale.

Perfetto, ora che abbiamo compreso il flusso, configuriamo un agente AI per sfruttare strumenti esterni tramite MCP, migliorandone le capacità!

## Prerequisiti

- [Visual Studio Code](https://code.visualstudio.com/)
- [AI Toolkit per Visual Studio Code](https://aka.ms/AIToolkit)

## Esercizio: Utilizzare un server

> [!WARNING]
> Nota per utenti macOS. Stiamo attualmente indagando su un problema che riguarda l'installazione delle dipendenze su macOS. Di conseguenza, gli utenti macOS non potranno completare questo tutorial al momento. Aggiorneremo le istruzioni non appena sarà disponibile una soluzione. Grazie per la pazienza e la comprensione!

In questo esercizio, creerai, eseguirai e migliorerai un agente AI con strumenti da un server MCP all'interno di Visual Studio Code utilizzando AI Toolkit.

### -0- Passo preliminare, aggiungere il modello OpenAI GPT-4o a I Miei Modelli

L'esercizio utilizza il modello **GPT-4o**. Il modello deve essere aggiunto a **I Miei Modelli** prima di creare l'agente.

1. Apri l'estensione **AI Toolkit** dalla **Barra delle attività**.
1. Nella sezione **Catalogo**, seleziona **Modelli** per aprire il **Catalogo Modelli**. Selezionando **Modelli** si apre il **Catalogo Modelli** in una nuova scheda dell'editor.
1. Nella barra di ricerca del **Catalogo Modelli**, inserisci **OpenAI GPT-4o**.
1. Clicca su **+ Aggiungi** per aggiungere il modello alla tua lista **I Miei Modelli**. Assicurati di aver selezionato il modello **Ospitato da GitHub**.
1. Nella **Barra delle attività**, conferma che il modello **OpenAI GPT-4o** appare nella lista.

### -1- Creare un agente

Il **Builder di Agenti (Prompt)** ti consente di creare e personalizzare i tuoi agenti AI. In questa sezione, creerai un nuovo agente e assegnerai un modello per alimentare la conversazione.

1. Apri l'estensione **AI Toolkit** dalla **Barra delle attività**.
1. Nella sezione **Strumenti**, seleziona **Builder di Agenti (Prompt)**. Selezionando **Builder di Agenti (Prompt)** si apre il **Builder di Agenti (Prompt)** in una nuova scheda dell'editor.
1. Clicca sul pulsante **+ Nuovo Agente**. L'estensione avvierà una procedura guidata tramite il **Command Palette**.
1. Inserisci il nome **Agente Calcolatrice** e premi **Invio**.
1. Nel **Builder di Agenti (Prompt)**, per il campo **Modello**, seleziona il modello **OpenAI GPT-4o (via GitHub)**.

### -2- Creare un prompt di sistema per l'agente

Con l'agente configurato, è il momento di definire la sua personalità e il suo scopo. In questa sezione, utilizzerai la funzione **Genera prompt di sistema** per descrivere il comportamento previsto dell'agente—in questo caso, un agente calcolatrice—e far scrivere il prompt di sistema al modello.

1. Nella sezione **Prompt**, clicca sul pulsante **Genera prompt di sistema**. Questo pulsante apre il generatore di prompt che utilizza l'AI per generare un prompt di sistema per l'agente.
1. Nella finestra **Genera un prompt**, inserisci il seguente testo: `Sei un assistente matematico utile ed efficiente. Quando ti viene presentato un problema di aritmetica di base, rispondi con il risultato corretto.`
1. Clicca sul pulsante **Genera**. Una notifica apparirà nell'angolo in basso a destra confermando che il prompt di sistema è in fase di generazione. Una volta completata la generazione del prompt, il prompt apparirà nel campo **Prompt di sistema** del **Builder di Agenti (Prompt)**.
1. Rivedi il **Prompt di sistema** e modificalo se necessario.

### -3- Creare un server MCP

Ora che hai definito il prompt di sistema dell'agente—guidando il suo comportamento e le sue risposte—è il momento di dotare l'agente di capacità pratiche. In questa sezione, creerai un server MCP per calcolatrici con strumenti per eseguire calcoli di addizione, sottrazione, moltiplicazione e divisione. Questo server permetterà al tuo agente di eseguire operazioni matematiche in tempo reale in risposta a prompt in linguaggio naturale.

AI Toolkit è dotato di modelli per semplificare la creazione del tuo server MCP. Utilizzeremo il modello Python per creare il server MCP per calcolatrici.

*Nota*: AI Toolkit supporta attualmente Python e TypeScript.

1. Nella sezione **Strumenti** del **Builder di Agenti (Prompt)**, clicca sul pulsante **+ Server MCP**. L'estensione avvierà una procedura guidata tramite il **Command Palette**.
1. Seleziona **+ Aggiungi Server**.
1. Seleziona **Crea un Nuovo Server MCP**.
1. Seleziona **python-weather** come modello.
1. Seleziona **Cartella predefinita** per salvare il modello del server MCP.
1. Inserisci il seguente nome per il server: **Calcolatrice**
1. Si aprirà una nuova finestra di Visual Studio Code. Seleziona **Sì, mi fido degli autori**.
1. Utilizzando il terminale (**Terminale** > **Nuovo Terminale**), crea un ambiente virtuale: `python -m venv .venv`
1. Utilizzando il terminale, attiva l'ambiente virtuale:
    1. Windows - `.venv\Scripts\activate`
    1. macOS/Linux - `source .venv/bin/activate`
1. Utilizzando il terminale, installa le dipendenze: `pip install -e .[dev]`
1. Nella vista **Esplora** della **Barra delle attività**, espandi la directory **src** e seleziona **server.py** per aprire il file nell'editor.
1. Sostituisci il codice nel file **server.py** con il seguente e salva:

    ```python
    """
    Sample MCP Calculator Server implementation in Python.

    
    This module demonstrates how to create a simple MCP server with calculator tools
    that can perform basic arithmetic operations (add, subtract, multiply, divide).
    """
    
    from mcp.server.fastmcp import FastMCP
    
    server = FastMCP("calculator")
    
    @server.tool()
    def add(a: float, b: float) -> float:
        """Add two numbers together and return the result."""
        return a + b
    
    @server.tool()
    def subtract(a: float, b: float) -> float:
        """Subtract b from a and return the result."""
        return a - b
    
    @server.tool()
    def multiply(a: float, b: float) -> float:
        """Multiply two numbers together and return the result."""
        return a * b
    
    @server.tool()
    def divide(a: float, b: float) -> float:
        """
        Divide a by b and return the result.
        
        Raises:
            ValueError: If b is zero
        """
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
    ```

### -4- Eseguire l'agente con il server MCP per calcolatrici

Ora che il tuo agente ha strumenti, è il momento di usarli! In questa sezione, invierai prompt all'agente per testare e validare se l'agente utilizza lo strumento appropriato dal server MCP per calcolatrici.

1. Premi `F5` per avviare il debug del server MCP. Il **Builder di Agenti (Prompt)** si aprirà in una nuova scheda dell'editor. Lo stato del server è visibile nel terminale.
1. Nel campo **Prompt utente** del **Builder di Agenti (Prompt)**, inserisci il seguente prompt: `Ho comprato 3 articoli al prezzo di $25 ciascuno e poi ho usato uno sconto di $20. Quanto ho pagato?`
1. Clicca sul pulsante **Esegui** per generare la risposta dell'agente.
1. Rivedi l'output dell'agente. Il modello dovrebbe concludere che hai pagato **$55**.
1. Ecco una panoramica di ciò che dovrebbe accadere:
    - L'agente seleziona gli strumenti **moltiplica** e **sottrae** per aiutare nel calcolo.
    - I rispettivi valori `a` e `b` vengono assegnati per lo strumento **moltiplica**.
    - I rispettivi valori `a` e `b` vengono assegnati per lo strumento **sottrae**.
    - La risposta di ciascuno strumento viene fornita nella rispettiva **Risposta dello strumento**.
    - L'output finale del modello viene fornito nella **Risposta del modello**.
1. Invia ulteriori prompt per testare ulteriormente l'agente. Puoi modificare il prompt esistente nel campo **Prompt utente** cliccando nel campo e sostituendo il prompt esistente.
1. Una volta terminato il test dell'agente, puoi interrompere il server tramite il **terminale** inserendo **CTRL/CMD+C** per uscire.

## Compito

Prova ad aggiungere un'ulteriore voce di strumento al tuo file **server.py** (es: calcolare la radice quadrata di un numero). Invia ulteriori prompt che richiedano all'agente di utilizzare il tuo nuovo strumento (o strumenti esistenti). Assicurati di riavviare il server per caricare i nuovi strumenti aggiunti.

## Soluzione

[Soluzione](./solution/README.md)

## Punti chiave

I punti chiave di questo capitolo sono i seguenti:

- L'estensione AI Toolkit è un ottimo client che ti consente di utilizzare server MCP e i loro strumenti.
- Puoi aggiungere nuovi strumenti ai server MCP, espandendo le capacità dell'agente per soddisfare requisiti in evoluzione.
- AI Toolkit include modelli (es: modelli di server MCP Python) per semplificare la creazione di strumenti personalizzati.

## Risorse aggiuntive

- [Documentazione AI Toolkit](https://aka.ms/AIToolkit/doc)

## Prossimi passi
- Prossimo: [Test e Debug](../08-testing/README.md)

**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire l'accuratezza, si prega di notare che le traduzioni automatiche potrebbero contenere errori o imprecisioni. Il documento originale nella sua lingua nativa dovrebbe essere considerato la fonte autorevole. Per informazioni critiche, si consiglia una traduzione professionale eseguita da un traduttore umano. Non siamo responsabili per eventuali fraintendimenti o interpretazioni errate derivanti dall'uso di questa traduzione.