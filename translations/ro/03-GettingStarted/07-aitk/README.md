# Consumarea unui server din extensia AI Toolkit pentru Visual Studio Code

Când construiești un agent AI, nu este vorba doar despre generarea unor răspunsuri inteligente; este, de asemenea, despre a-i oferi agentului tău abilitatea de a lua acțiuni. Aici intervine Protocolul Contextului Modelului (MCP). MCP face ușor accesul agenților la unelte și servicii externe într-un mod consecvent. Gândește-l ca pe o trusă de unelte în care agentul tău poate *de fapt* să folosească.

Să spunem că conectezi un agent la serverul tău MCP calculator. Dintr-o dată, agentul tău poate efectua operații matematice doar primind un mesaj de genul „Cât fac 47 înmulțit cu 89?” — fără a fi nevoie să codifici logică sau să construiești API-uri personalizate.

## Prezentare generală

Această lecție acoperă modul de conectare a unui server MCP calculator la un agent cu extensia [AI Toolkit](https://aka.ms/AIToolkit) în Visual Studio Code, permițând agentului tău să efectueze operații matematice precum adunare, scădere, înmulțire și împărțire prin limbaj natural.

AI Toolkit este o extensie puternică pentru Visual Studio Code care simplifică dezvoltarea agenților. Inginerii AI pot construi cu ușurință aplicații AI dezvoltând și testând modele generative AI—local sau în cloud. Extensia suportă cele mai importante modele generative disponibile astăzi.

*Notă*: AI Toolkit suportă momentan Python și TypeScript.

## Obiective de învățare

La sfârșitul acestei lecții, vei putea:

- Consuma un server MCP prin AI Toolkit.
- Configura un agent pentru a-i permite să descopere și să utilizeze uneltele oferite de serverul MCP.
- Utiliza uneltele MCP prin limbaj natural.

## Abordare

Iată modul în care trebuie să abordăm acest lucru la un nivel înalt:

- Creează un agent și definește promptul său de sistem.
- Creează un server MCP cu unelte calculator.
- Conectează Agent Builder la serverul MCP.
- Testează invocarea uneltei agentului prin limbaj natural.

Excelent, acum că înțelegem fluxul, să configurăm un agent AI să valorifice unelte externe prin MCP, îmbunătățindu-i capacitățile!

## Cerințe preliminare

- [Visual Studio Code](https://code.visualstudio.com/)
- [AI Toolkit pentru Visual Studio Code](https://aka.ms/AIToolkit)

## Exercițiu: Consumarea unui server

> [!WARNING]
> Notă pentru utilizatorii macOS. Investigăm în prezent o problemă care afectează instalarea dependențelor pe macOS. Ca urmare, utilizatorii macOS nu vor putea finaliza acest tutorial în acest moment. Vom actualiza instrucțiunile imediat ce o soluție va fi disponibilă. Vă mulțumim pentru răbdare și înțelegere!

În acest exercițiu, vei construi, rula și îmbunătăți un agent AI cu unelte de la un server MCP în Visual Studio Code folosind AI Toolkit.

### -0- Pas preliminar, adaugă modelul OpenAI GPT-4o în My Models

Exercițiul folosește modelul **GPT-4o**. Modelul trebuie adăugat în **My Models** înainte de a crea agentul.

![Screenshot al unei interfețe de selecție model în extensia AI Toolkit pentru Visual Studio Code. Titlul spune "Găsește modelul potrivit pentru soluția ta AI" cu un subtitlu ce încurajează utilizatorii să descopere, testeze și să implementeze modele AI. Mai jos, sub „Popular Models”, sunt afișate șase carduri de modele: DeepSeek-R1 (hostat pe GitHub), OpenAI GPT-4o, OpenAI GPT-4.1, OpenAI o1, Phi 4 Mini (CPU - Mic, Rapid), și DeepSeek-R1 (hostat pe Ollama). Fiecare card include opțiuni pentru „Add” modelul sau „Try in Playground).](../../../../translated_images/ro/aitk-model-catalog.2acd38953bb9c119.webp)

1. Deschide extensia **AI Toolkit** din **Activity Bar**.
1. În secțiunea **Catalog**, selectează **Models** pentru a deschide **Model Catalog**. Selectarea **Models** deschide **Model Catalog** într-un tab nou al editorului.
1. În bara de căutare **Model Catalog**, introdu **OpenAI GPT-4o**.
1. Apasă pe **+ Add** pentru a adăuga modelul în lista ta **My Models**. Asigură-te că ai selectat modelul **Hosted by GitHub**.
1. În **Activity Bar**, confirmă că modelul **OpenAI GPT-4o** apare în listă.

### -1- Creează un agent

**Agent (Prompt) Builder** îți permite să creezi și să personalizezi proprii agenți alimentați de AI. În această secțiune, vei crea un agent nou și îi vei atribui un model pentru a alimenta conversația.

![Screenshot al interfeței „Calculator Agent” în AI Toolkit pentru Visual Studio Code. În panoul din stânga, modelul selectat este "OpenAI GPT-4o (via GitHub)." Un prompt de sistem spune "Ești profesor universitar care predă matematică," iar promptul utilizatorului spune "Explică-mi ecuația Fourier în termeni simpli." Opțiunile suplimentare includ butoane pentru adăugarea uneltelor, activarea MCP Server și selectarea output-ului structurat. Un buton albastru „Run” este jos. Pe panoul din dreapta, sub „Get Started with Examples,” sunt listate trei agenți de probă: Web Developer (cu MCP Server, Simplifier pentru clasa a doua și Interpret de vise, fiecare cu descrieri scurte ale funcțiilor.)](../../../../translated_images/ro/aitk-agent-builder.901e3a2960c3e477.webp)

1. Deschide extensia **AI Toolkit** din **Activity Bar**.
1. În secțiunea **Tools**, selectează **Agent (Prompt) Builder**. Selectarea acesteia deschide **Agent (Prompt) Builder** într-un nou tab al editorului.
1. Apasă butonul **+ New Agent**. Extensia va porni un wizard de configurare prin **Command Palette**.
1. Introdu numele **Calculator Agent** și apasă **Enter**.
1. În **Agent (Prompt) Builder**, pentru câmpul **Model**, selectează modelul **OpenAI GPT-4o (via GitHub)**.

### -2- Creează un prompt de sistem pentru agent

Acum că agentul este structurat, e timpul să-i definești personalitatea și scopul. În această secțiune, vei folosi funcția **Generate system prompt** pentru a descrie comportamentul dorit al agentului—în acest caz, un agent calculator—și pentru ca modelul să scrie promptul de sistem pentru tine.

![Screenshot al interfeței „Calculator Agent” în AI Toolkit pentru Visual Studio Code cu o fereastră modală deschisă intitulată „Generate a prompt.” Modalul explică că un șablon de prompt poate fi generat partajând detalii de bază și include o casetă de text cu promptul de sistem exemplu: "Ești un asistent de matematică util și eficient. Când primești o problemă care implică aritmetică de bază, răspunzi cu rezultatul corect." Sub caseta de text sunt butoanele "Close" și "Generate". În fundal, e vizibilă o parte din configurația agentului, inclusiv modelul selectat "OpenAI GPT-4o (via GitHub)" și câmpurile pentru prompturi de sistem și utilizator.](../../../../translated_images/ro/aitk-generate-prompt.ba9e69d3d2bbe2a2.webp)

1. Pentru secțiunea **Prompts**, apasă butonul **Generate system prompt**. Acest buton deschide generatorul de prompturi care folosește AI pentru a genera un prompt de sistem pentru agent.
1. În fereastra **Generate a prompt**, introdu următorul text: `Ești un asistent de matematică util și eficient. Când primești o problemă care implică aritmetică de bază, răspunzi cu rezultatul corect.`
1. Apasă butonul **Generate**. În colțul din dreapta jos va apărea o notificare confirmând generarea promptului. După ce generarea se finalizează, promptul va apărea în câmpul **System prompt** al **Agent (Prompt) Builder**.
1. Revizuiește **System prompt** și modifică-l dacă este necesar.

### -3- Creează un server MCP

Acum că ți-ai definit promptul de sistem al agentului—care îl ghidează în comportament și răspunsuri—e timpul să echipezi agentul cu funcționalități practice. În această secțiune, vei crea un server MCP calculator cu unelte pentru efectuarea operațiilor de adunare, scădere, înmulțire și împărțire. Acest server va permite agentului tău să realizeze operații matematice în timp real ca răspuns la prompturi în limbaj natural.

!["Screenshot al secțiunii inferioare a interfeței Calculator Agent în AI Toolkit pentru Visual Studio Code. Arată meniuri extinse pentru „Tools” și „Structure output”, împreună cu un meniu dropdown etichetat „Choose output format” setat pe „text.” În dreapta este un buton „+ MCP Server” pentru a adăuga un server Model Context Protocol. Deasupra secțiunii Tools apare un loc de ținut pentru iconiță de imagine.](../../../../translated_images/ro/aitk-add-mcp-server.9742cfddfe808353.webp)

AI Toolkit este echipat cu șabloane pentru ușurința creării propriului tău server MCP. Vom folosi șablonul Python pentru crearea serverului MCP calculator.

*Notă*: AI Toolkit suportă momentan Python și TypeScript.

1. În secțiunea **Tools** a **Agent (Prompt) Builder**, apasă butonul **+ MCP Server**. Extensia va porni un wizard de configurare prin **Command Palette**.
1. Selectează **+ Add Server**.
1. Selectează **Create a New MCP Server**.
1. Selectează șablonul **python-weather**.
1. Selectează **Default folder** pentru a salva șablonul serverului MCP.
1. Introdu următorul nume pentru server: **Calculator**
1. Se va deschide o fereastră nouă Visual Studio Code. Selectează **Yes, I trust the authors**.
1. Folosind terminalul (**Terminal** > **New Terminal**), creează un mediu virtual: `python -m venv .venv`
1. Folosind terminalul, activează mediul virtual:
    1. Windows - `.venv\Scripts\activate`
    1. macOS/Linux - `source .venv/bin/activate`
1. Folosind terminalul, instalează dependențele: `pip install -e .[dev]`
1. În vista **Explorer** a **Activity Bar**, extinde directorul **src** și selectează **server.py** pentru a deschide fișierul în editor.
1. Înlocuiește codul din fișierul **server.py** cu următorul și salvează:

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

### -4- Rulează agentul cu serverul MCP calculator

Acum că agentul tău are unelte, e timpul să le folosești! În această secțiune, vei trimite prompturi agentului pentru a testa și valida dacă agentul valorifică uneltele potrivite de la serverul MCP calculator.

![Screenshot al interfeței Calculator Agent în AI Toolkit pentru Visual Studio Code. În panoul din stânga, sub „Tools,” un server MCP numit local-server-calculator_server este adăugat, afișând patru unelte disponibile: add, subtract, multiply și divide. Un badge arată că patru unelte sunt active. Jos este o secțiune collapsibilă „Structure output” și un buton albastru „Run”. În panoul din dreapta, sub „Model Response,” agentul invocă uneltele multiply și subtract cu inputurile {"a": 3, "b": 25} și {"a": 75, "b": 20} respectiv. Răspunsul final „Tool Response” este afișat ca 75.0. Un buton „View Code” apare jos.](../../../../translated_images/ro/aitk-agent-response-with-tools.e7c781869dc8041a.webp)

Vei rula serverul MCP calculator pe mașina ta locală de dezvoltare via **Agent Builder** ca și client MCP.

1. Apasă `F5` pentru a începe depanarea serverului MCP. **Agent (Prompt) Builder** se va deschide într-un tab nou în editor. Statusul serverului este vizibil în terminal.
1. În câmpul **User prompt** al **Agent (Prompt) Builder**, introdu următorul prompt: `Am cumpărat 3 articole la prețul de 25$ fiecare, apoi am folosit o reducere de 20$. Cât am plătit?`
1. Apasă butonul **Run** pentru a genera răspunsul agentului.
1. Revizuiește output-ul agentului. Modelul ar trebui să concluzioneze că ai plătit **55$**.
1. Iată o detaliere a ceea ce ar trebui să se întâmple:
    - Agentul selectează uneltele **multiply** și **subtract** pentru a ajuta în calcul.
    - Valorile `a` și `b` corespunzătoare sunt alocate uneltei **multiply**.
    - Valorile `a` și `b` corespunzătoare sunt alocate uneltei **subtract**.
    - Răspunsul de la fiecare unealtă este oferit în câmpul **Tool Response**.
    - Output-ul final din model este oferit în câmpul final **Model Response**.
1. Trimite prompturi suplimentare pentru a testa mai mult agentul. Poți modifica promptul existent în câmpul **User prompt** făcând clic în câmp și înlocuind promptul existent.
1. Când termini testarea agentului, poți opri serverul prin **terminal** apăsând **CTRL/CMD+C**.

## Sarcină

Încearcă să adaugi o unealtă suplimentară în fișierul tău **server.py** (ex: să returnezi rădăcina pătrată a unui număr). Trimite prompturi suplimentare care ar necesita ca agentul să folosească această unealtă nouă (sau unelte existente). Asigură-te că repornești serverul pentru a încărca noile unelte adăugate.

## Soluție

[Soluție](./solution/README.md)

## Puncte esențiale

Punctele esențiale din acest capitol sunt următoarele:

- Extensia AI Toolkit este un client excelent care îți permite să consumi servere MCP și uneltele acestora.
- Poți adăuga unelte noi serverelor MCP, extinzând capacitățile agentului pentru a satisface cerințe evolutive.
- AI Toolkit include șabloane (ex: șabloane server MCP Python) pentru a simplifica crearea uneltelor personalizate.

## Resurse suplimentare

- [Documentația AI Toolkit](https://aka.ms/AIToolkit/doc)

## Ce urmează
- Următor: [Testare și depanare](../08-testing/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Declinare a responsabilității**:
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). În timp ce ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un om. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care decurg din utilizarea acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->