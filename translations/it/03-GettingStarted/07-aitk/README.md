# Consumare un server dall’estensione AI Toolkit per Visual Studio Code

Quando costruisci un agente AI, non si tratta solo di generare risposte intelligenti; si tratta anche di dare al tuo agente la capacità di agire. Qui entra in gioco il Model Context Protocol (MCP). MCP rende facile per gli agenti accedere a strumenti e servizi esterni in modo coerente. Pensalo come collegare il tuo agente a una cassetta degli attrezzi che può *veramente* usare.

Supponiamo che tu colleghi un agente al tuo server MCP calcolatrice. All’improvviso, il tuo agente può eseguire operazioni matematiche semplicemente ricevendo un prompt come “Quanto fa 47 per 89?”—senza bisogno di codificare la logica o creare API personalizzate.

## Panoramica

Questa lezione spiega come collegare un server MCP calcolatrice a un agente con l’estensione [AI Toolkit](https://aka.ms/AIToolkit) in Visual Studio Code, consentendo al tuo agente di eseguire operazioni matematiche come addizione, sottrazione, moltiplicazione e divisione tramite il linguaggio naturale.

AI Toolkit è un’estensione potente per Visual Studio Code che semplifica lo sviluppo di agenti. Gli ingegneri AI possono facilmente costruire applicazioni AI sviluppando e testando modelli generativi di AI—localmente o nel cloud. L’estensione supporta la maggior parte dei principali modelli generativi disponibili oggi.

*Nota*: AI Toolkit attualmente supporta Python e TypeScript.

## Obiettivi di Apprendimento

Al termine di questa lezione, sarai in grado di:

- Consumare un server MCP tramite AI Toolkit.
- Configurare una configurazione agente per consentirgli di scoprire e utilizzare gli strumenti forniti dal server MCP.
- Utilizzare gli strumenti MCP tramite linguaggio naturale.

## Approccio

Ecco come dobbiamo procedere ad alto livello:

- Creare un agente e definire il suo prompt di sistema.
- Creare un server MCP con strumenti di calcolo.
- Collegare l’Agent Builder al server MCP.
- Testare l’invocazione degli strumenti da parte dell’agente tramite linguaggio naturale.

Perfetto, ora che abbiamo compreso il flusso, configuriamo un agente AI per sfruttare strumenti esterni tramite MCP, potenziando le sue capacità!

## Prerequisiti

- [Visual Studio Code](https://code.visualstudio.com/)
- [AI Toolkit per Visual Studio Code](https://aka.ms/AIToolkit)

## Esercizio: Consumare un server

> [!WARNING]
> Nota per utenti macOS. Stiamo attualmente indagando un problema che interessa l’installazione delle dipendenze su macOS. Di conseguenza, gli utenti macOS non potranno completare questo tutorial al momento. Aggiorneremo le istruzioni non appena sarà disponibile una soluzione. Grazie per la vostra pazienza e comprensione!

In questo esercizio costruirai, eseguirai e migliorerai un agente AI con strumenti da un server MCP all’interno di Visual Studio Code utilizzando AI Toolkit.

### -0- Passaggio preliminare, aggiungi il modello OpenAI GPT-4o a My Models

L’esercizio utilizza il modello **GPT-4o**. Il modello deve essere aggiunto a **My Models** prima di creare l’agente.

![Screenshot di un’interfaccia di selezione modello nell’estensione AI Toolkit di Visual Studio Code. L’intestazione dice “Find the right model for your AI Solution” con un sottotitolo che incoraggia gli utenti a scoprire, testare e distribuire modelli AI. Sotto, nella sezione “Popular Models,” sono mostrati sei modelli: DeepSeek-R1 (ospitato su GitHub), OpenAI GPT-4o, OpenAI GPT-4.1, OpenAI o1, Phi 4 Mini (CPU - Piccolo, Veloce), e DeepSeek-R1 (ospitato su Ollama). Ogni scheda include opzioni per “Add” il modello o “Try in Playground](../../../../translated_images/it/aitk-model-catalog.2acd38953bb9c119.webp)

1. Apri l’estensione **AI Toolkit** dalla **Activity Bar**.
1. Nella sezione **Catalog**, seleziona **Models** per aprire il **Model Catalog**. Selezionare **Models** apre il **Model Catalog** in una nuova scheda dell’editor.
1. Nella barra di ricerca del **Model Catalog**, inserisci **OpenAI GPT-4o**.
1. Clicca **+ Add** per aggiungere il modello alla tua lista **My Models**. Assicurati di aver selezionato il modello che è **Hosted by GitHub**.
1. Nella **Activity Bar**, conferma che il modello **OpenAI GPT-4o** appare nella lista.

### -1- Crea un agente

L’**Agent (Prompt) Builder** ti consente di creare e personalizzare i tuoi agenti AI. In questa sezione, creerai un nuovo agente e assegnerai un modello per alimentare la conversazione.

![Screenshot dell’interfaccia “Calculator Agent” nell’estensione AI Toolkit per Visual Studio Code. Nel pannello sinistro, il modello selezionato è “OpenAI GPT-4o (via GitHub).” Un prompt di sistema dice “You are a professor in university teaching math,” e il prompt utente dice “Explain to me the Fourier equation in simple terms.” Opzioni aggiuntive includono pulsanti per aggiungere strumenti, abilitare MCP Server e selezionare output strutturati. Un pulsante blu “Run” è in basso. Nel pannello destro, sotto “Get Started with Examples,” sono elencati tre agenti di esempio: Web Developer (con MCP Server, Second-Grade Simplifier, e Dream Interpreter, ciascuno con brevi descrizioni delle funzioni.](../../../../translated_images/it/aitk-agent-builder.901e3a2960c3e477.webp)

1. Apri l’estensione **AI Toolkit** dalla **Activity Bar**.
1. Nella sezione **Tools**, seleziona **Agent (Prompt) Builder**. Selezionare **Agent (Prompt) Builder** apre l’**Agent (Prompt) Builder** in una nuova scheda dell’editor.
1. Clicca il pulsante **+ New Agent**. L’estensione avvierà una procedura guidata tramite la **Command Palette**.
1. Inserisci il nome **Calculator Agent** e premi **Enter**.
1. Nell’**Agent (Prompt) Builder**, per il campo **Model**, seleziona il modello **OpenAI GPT-4o (via GitHub)**.

### -2- Crea un prompt di sistema per l’agente

Con l’agente strutturato, è tempo di definire la sua personalità e scopo. In questa sezione, utilizzerai la funzione **Generate system prompt** per descrivere il comportamento desiderato dell’agente—in questo caso, un agente calcolatrice—e far scrivere al modello il prompt di sistema per te.

![Screenshot dell’interfaccia “Calculator Agent” in AI Toolkit per Visual Studio Code con una finestra modale aperta intitolata “Generate a prompt.” La modale spiega che un template di prompt può essere generato condividendo dettagli di base e include una casella di testo con il prompt di sistema di esempio: “You are a helpful and efficient math assistant. When given a problem involving basic arithmetic, you respond with the correct result.” Sotto la casella ci sono i pulsanti “Close” e “Generate.” In background è parzialmente visibile la configurazione dell’agente, compresi il modello selezionato “OpenAI GPT-4o (via GitHub)” e i campi per i prompt di sistema e utente.](../../../../translated_images/it/aitk-generate-prompt.ba9e69d3d2bbe2a2.webp)

1. Per la sezione **Prompts**, clicca il pulsante **Generate system prompt**. Questo pulsante apre il generatore di prompt che sfrutta l’AI per generare un prompt di sistema per l’agente.
1. Nella finestra **Generate a prompt**, inserisci quanto segue: `You are a helpful and efficient math assistant. When given a problem involving basic arithmetic, you respond with the correct result.`
1. Clicca il pulsante **Generate**. Apparirà una notifica nell’angolo in basso a destra che conferma che il prompt di sistema è in generazione. Una volta completata la generazione, il prompt apparirà nel campo **System prompt** dell’**Agent (Prompt) Builder**.
1. Rivedi il **System prompt** e modifica se necessario.

### -3- Crea un server MCP

Ora che hai definito il prompt di sistema del tuo agente—guidando il suo comportamento e le risposte—è tempo di dotare l’agente di capacità pratiche. In questa sezione, creerai un server MCP calcolatrice con strumenti per eseguire addizione, sottrazione, moltiplicazione e divisione. Questo server permetterà al tuo agente di effettuare operazioni matematiche in tempo reale rispondendo a prompt in linguaggio naturale.

![Screenshot della sezione inferiore dell’interfaccia Calculator Agent nell’estensione AI Toolkit per Visual Studio Code. Mostra menu espandibili per “Tools” e “Structure output,” insieme a un menu a tendina etichettato “Choose output format” impostato su “text.” A destra, un pulsante etichettato “+ MCP Server” per aggiungere un server Model Context Protocol. Sopra la sezione Tools c’è un’icona segnaposto immagine.](../../../../translated_images/it/aitk-add-mcp-server.9742cfddfe808353.webp)

AI Toolkit è dotato di template per facilitare la creazione del proprio server MCP. Useremo il template Python per creare il server MCP calcolatrice.

*Nota*: AI Toolkit attualmente supporta Python e TypeScript.

1. Nella sezione **Tools** dell’**Agent (Prompt) Builder**, clicca il pulsante **+ MCP Server**. L’estensione avvierà una procedura guidata tramite la **Command Palette**.
1. Seleziona **+ Add Server**.
1. Seleziona **Create a New MCP Server**.
1. Seleziona **python-weather** come template.
1. Seleziona **Default folder** per salvare il template del server MCP.
1. Inserisci per il server il nome: **Calculator**
1. Si aprirà una nuova finestra di Visual Studio Code. Seleziona **Yes, I trust the authors**.
1. Usando il terminale (**Terminal** > **New Terminal**), crea un ambiente virtuale: `python -m venv .venv`
1. Usando il terminale, attiva l’ambiente virtuale:
    1. Windows - `.venv\Scripts\activate`
    1. macOS/Linux - `source .venv/bin/activate`
1. Usando il terminale, installa le dipendenze: `pip install -e .[dev]`
1. Nella vista **Explorer** della **Activity Bar**, espandi la directory **src** e seleziona **server.py** per aprire il file nell’editor.
1. Sostituisci il codice nel file **server.py** con quanto segue e salva:

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

### -4- Esegui l’agente con il server MCP calcolatrice

Ora che il tuo agente ha degli strumenti, è tempo di usarli! In questa sezione invierai prompt all’agente per testare e verificare se l’agente sfrutta lo strumento appropriato dal server MCP calcolatrice.

![Screenshot dell’interfaccia Calculator Agent nell’estensione AI Toolkit per Visual Studio Code. Nel pannello sinistro, sotto “Tools,” un server MCP chiamato local-server-calculator_server è aggiunto, mostrando quattro strumenti disponibili: add, subtract, multiply, e divide. Un badge mostra che quattro strumenti sono attivi. Sotto c’è una sezione “Structure output” collassata e un pulsante blu “Run.” Nel pannello destro, sotto “Model Response,” l’agente invoca gli strumenti multiply e subtract con input {"a": 3, "b": 25} e {"a": 75, "b": 20} rispettivamente. La risposta finale “Tool Response” è mostrata come 75.0. Un pulsante “View Code” appare in fondo.](../../../../translated_images/it/aitk-agent-response-with-tools.e7c781869dc8041a.webp)

Eseguirai il server MCP calcolatrice sulla tua macchina locale di sviluppo tramite l’**Agent Builder** come client MCP.

1. Premi `F5` per iniziare il debug del server MCP. L’**Agent (Prompt) Builder** si aprirà in una nuova scheda editor. Lo stato del server è visibile nel terminale.
1. Nel campo **User prompt** dell’**Agent (Prompt) Builder**, inserisci il seguente prompt: `I bought 3 items priced at $25 each, and then used a $20 discount. How much did I pay?`
1. Clicca il pulsante **Run** per generare la risposta dell’agente.
1. Rivedi l’output dell’agente. Il modello dovrebbe concludere che hai pagato **$55**.
1. Ecco la suddivisione di ciò che dovrebbe accadere:
    - L’agente seleziona gli strumenti **multiply** e **subtract** per aiutare nel calcolo.
    - I valori `a` e `b` rispettivi sono assegnati per lo strumento **multiply**.
    - I valori `a` e `b` rispettivi sono assegnati per lo strumento **subtract**.
    - La risposta di ciascuno strumento è fornita nella rispettiva **Tool Response**.
    - L’output finale del modello è fornito nella risposta finale **Model Response**.
1. Invia ulteriori prompt per testare ulteriormente l’agente. Puoi modificare il prompt esistente nel campo **User prompt** cliccandoci dentro e sostituendo il prompt attuale.
1. Quando hai finito di testare l’agente, puoi fermare il server tramite il **terminal** premendo **CTRL/CMD+C** per uscire.

## Compito

Prova ad aggiungere una voce strumento addizionale nel tuo file **server.py** (es: restituisci la radice quadrata di un numero). Invia ulteriori prompt che richiedano all’agente di usare il nuovo strumento (o strumenti esistenti). Assicurati di riavviare il server per caricare i nuovi strumenti aggiunti.

## Soluzione

[Soluzione](./solution/README.md)

## Punti Chiave

I punti chiave di questo capitolo sono i seguenti:

- L’estensione AI Toolkit è un ottimo client che ti permette di consumare Server MCP e i loro strumenti.
- Puoi aggiungere nuovi strumenti ai server MCP, espandendo le capacità dell’agente per soddisfare esigenze in evoluzione.
- AI Toolkit include template (ad esempio template server MCP Python) per semplificare la creazione di strumenti personalizzati.

## Risorse Aggiuntive

- [Documentazione AI Toolkit](https://aka.ms/AIToolkit/doc)

## Cosa c’è dopo
- Prossimo: [Testing & Debugging](../08-testing/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Questo documento è stato tradotto utilizzando il servizio di traduzione AI [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire la precisione, si prega di notare che le traduzioni automatizzate possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un essere umano. Non siamo responsabili per eventuali malintesi o interpretazioni errate derivanti dall’uso di questa traduzione.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->