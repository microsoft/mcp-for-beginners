# Consumarea unui server din extensia AI Toolkit pentru Visual Studio Code

Când construiești un agent AI, nu este vorba doar despre generarea de răspunsuri inteligente; este și despre a-i oferi agentului capacitatea de a acționa. Aici intervine Model Context Protocol (MCP). MCP face ca agenții să poată accesa instrumente și servicii externe într-un mod consistent. Gândește-te la asta ca la conectarea agentului tău la o trusă de unelte pe care o poate *folosi cu adevărat*.

Să presupunem că conectezi un agent la serverul MCP al unui calculator. Dintr-odată, agentul tău poate efectua operații matematice doar primind o solicitare precum „Cât face 47 înmulțit cu 89?”—fără a fi nevoie să codifici logică sau să construiești API-uri personalizate.

## Prezentare generală

Această lecție acoperă modul de conectare a unui server MCP de tip calculator la un agent folosind extensia [AI Toolkit](https://aka.ms/AIToolkit) din Visual Studio Code, permițând agentului să efectueze operații matematice precum adunare, scădere, înmulțire și împărțire prin limbaj natural.

AI Toolkit este o extensie puternică pentru Visual Studio Code care simplifică dezvoltarea agenților. Inginerii AI pot construi cu ușurință aplicații AI dezvoltând și testând modele generative AI—local sau în cloud. Extensia suportă majoritatea modelelor generative disponibile astăzi.

*Notă*: AI Toolkit suportă în prezent Python și TypeScript.

## Obiectivele învățării

Până la finalul acestei lecții, vei putea:

- Consuma un server MCP prin AI Toolkit.
- Configura un agent astfel încât să descopere și să utilizeze instrumentele oferite de serverul MCP.
- Utiliza instrumentele MCP prin limbaj natural.

## Abordare

Iată cum trebuie să abordăm acest proces la un nivel înalt:

- Creează un agent și definește-i promptul de sistem.
- Creează un server MCP cu instrumente de calculator.
- Conectează Agent Builder la serverul MCP.
- Testează invocarea instrumentelor agentului prin limbaj natural.

Perfect, acum că înțelegem fluxul, să configurăm un agent AI pentru a utiliza instrumente externe prin MCP, îmbunătățindu-i capacitățile!

## Cerințe preliminare

- [Visual Studio Code](https://code.visualstudio.com/)
- [AI Toolkit pentru Visual Studio Code](https://aka.ms/AIToolkit)

## Exercițiu: Consumarea unui server

> [!WARNING]
> Notă pentru utilizatorii macOS. Investigăm în prezent o problemă care afectează instalarea dependențelor pe macOS. Ca urmare, utilizatorii macOS nu vor putea finaliza acest tutorial momentan. Vom actualiza instrucțiunile imediat ce o soluție este disponibilă. Vă mulțumim pentru răbdare și înțelegere!

În acest exercițiu, vei construi, rula și îmbunătăți un agent AI cu instrumente de la un server MCP în Visual Studio Code folosind AI Toolkit.

### -0- Pas preliminar, adaugă modelul OpenAI GPT-4o la My Models

Exercițiul utilizează modelul **GPT-4o**. Modelul trebuie adăugat la **My Models** înainte de a crea agentul.

1. Deschide extensia **AI Toolkit** din **Activity Bar**.
1. În secțiunea **Catalog**, selectează **Models** pentru a deschide **Model Catalog**. Selectarea **Models** deschide **Model Catalog** într-o filă nouă a editorului.
1. În bara de căutare a **Model Catalog**, introdu **OpenAI GPT-4o**.
1. Fă clic pe **+ Add** pentru a adăuga modelul la lista ta **My Models**. Asigură-te că ai selectat modelul **Hosted by GitHub**.
1. În **Activity Bar**, confirmă că modelul **OpenAI GPT-4o** apare în listă.

### -1- Creează un agent

**Agent (Prompt) Builder** îți permite să creezi și să personalizezi propriii agenți AI. În această secțiune, vei crea un nou agent și îi vei atribui un model pentru a alimenta conversația.

1. Deschide extensia **AI Toolkit** din **Activity Bar**.
1. În secțiunea **Tools**, selectează **Agent (Prompt) Builder**. Selectarea **Agent (Prompt) Builder** deschide **Agent (Prompt) Builder** într-o filă nouă a editorului.
1. Fă clic pe butonul **+ New Agent**. Extensia va lansa un asistent de configurare prin **Command Palette**.
1. Introdu numele **Calculator Agent** și apasă **Enter**.
1. În **Agent (Prompt) Builder**, pentru câmpul **Model**, selectează modelul **OpenAI GPT-4o (via GitHub)**.

### -2- Creează un prompt de sistem pentru agent

După ce ai creat structura agentului, este timpul să-i definești personalitatea și scopul. În această secțiune, vei utiliza funcția **Generate system prompt** pentru a descrie comportamentul intenționat al agentului—în acest caz, un agent calculator—și vei lăsa modelul să scrie promptul de sistem pentru tine.

1. Pentru secțiunea **Prompts**, fă clic pe butonul **Generate system prompt**. Acest buton deschide generatorul de prompturi, care utilizează AI pentru a genera un prompt de sistem pentru agent.
1. În fereastra **Generate a prompt**, introdu următorul text: `Ești un asistent matematic util și eficient. Când primești o problemă care implică aritmetică de bază, răspunzi cu rezultatul corect.`
1. Fă clic pe butonul **Generate**. O notificare va apărea în colțul din dreapta jos, confirmând că promptul de sistem este generat. După finalizarea generării, promptul va apărea în câmpul **System prompt** din **Agent (Prompt) Builder**.
1. Revizuiește **System prompt** și modifică-l dacă este necesar.

### -3- Creează un server MCP

Acum că ai definit promptul de sistem al agentului—ghidându-i comportamentul și răspunsurile—este timpul să echipezi agentul cu capabilități practice. În această secțiune, vei crea un server MCP de tip calculator cu instrumente pentru a efectua calcule de adunare, scădere, înmulțire și împărțire. Acest server va permite agentului să efectueze operații matematice în timp real ca răspuns la solicitări în limbaj natural.

AI Toolkit este echipat cu șabloane pentru a facilita crearea propriilor servere MCP. Vom utiliza șablonul Python pentru a crea serverul MCP de tip calculator.

*Notă*: AI Toolkit suportă în prezent Python și TypeScript.

1. În secțiunea **Tools** din **Agent (Prompt) Builder**, fă clic pe butonul **+ MCP Server**. Extensia va lansa un asistent de configurare prin **Command Palette**.
1. Selectează **+ Add Server**.
1. Selectează **Create a New MCP Server**.
1. Selectează **python-weather** ca șablon.
1. Selectează **Default folder** pentru a salva șablonul serverului MCP.
1. Introdu următorul nume pentru server: **Calculator**.
1. O nouă fereastră Visual Studio Code se va deschide. Selectează **Yes, I trust the authors**.
1. Folosind terminalul (**Terminal** > **New Terminal**), creează un mediu virtual: `python -m venv .venv`.
1. Folosind terminalul, activează mediul virtual:
    1. Windows - `.venv\Scripts\activate`
    1. macOS/Linux - `source .venv/bin/activate`
1. Folosind terminalul, instalează dependențele: `pip install -e .[dev]`.
1. În vizualizarea **Explorer** din **Activity Bar**, extinde directorul **src** și selectează **server.py** pentru a deschide fișierul în editor.
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

### -4- Rulează agentul cu serverul MCP de tip calculator

Acum că agentul tău are instrumente, este timpul să le folosească! În această secțiune, vei trimite solicitări agentului pentru a testa și valida dacă agentul utilizează instrumentul corespunzător de la serverul MCP de tip calculator.

1. Apasă `F5` pentru a începe depanarea serverului MCP. **Agent (Prompt) Builder** se va deschide într-o filă nouă a editorului. Starea serverului este vizibilă în terminal.
1. În câmpul **User prompt** din **Agent (Prompt) Builder**, introdu următoarea solicitare: `Am cumpărat 3 articole la prețul de 25$ fiecare, apoi am folosit un cupon de reducere de 20$. Cât am plătit?`
1. Fă clic pe butonul **Run** pentru a genera răspunsul agentului.
1. Revizuiește rezultatul agentului. Modelul ar trebui să concluzioneze că ai plătit **55$**.
1. Iată o descriere a ceea ce ar trebui să se întâmple:
    - Agentul selectează instrumentele **multiply** și **subtract** pentru a ajuta la calcul.
    - Valorile respective `a` și `b` sunt atribuite pentru instrumentul **multiply**.
    - Valorile respective `a` și `b` sunt atribuite pentru instrumentul **subtract**.
    - Răspunsul fiecărui instrument este furnizat în **Tool Response**.
    - Rezultatul final al modelului este furnizat în **Model Response**.
1. Trimite solicitări suplimentare pentru a testa în continuare agentul. Poți modifica solicitarea existentă în câmpul **User prompt** făcând clic în câmp și înlocuind solicitarea existentă.
1. După ce ai terminat testarea agentului, poți opri serverul prin **terminal** introducând **CTRL/CMD+C** pentru a ieși.

## Temă

Încearcă să adaugi o intrare suplimentară pentru un instrument în fișierul **server.py** (ex: returnează rădăcina pătrată a unui număr). Trimite solicitări suplimentare care ar necesita ca agentul să utilizeze noul tău instrument (sau instrumentele existente). Asigură-te că repornești serverul pentru a încărca noile instrumente adăugate.

## Soluție

[Soluție](./solution/README.md)

## Concluzii cheie

Concluziile acestui capitol sunt următoarele:

- Extensia AI Toolkit este un client excelent care permite consumarea serverelor MCP și a instrumentelor acestora.
- Poți adăuga noi instrumente la serverele MCP, extinzând capacitățile agentului pentru a răspunde cerințelor în continuă schimbare.
- AI Toolkit include șabloane (ex: șabloane pentru servere MCP în Python) pentru a simplifica crearea de instrumente personalizate.

## Resurse suplimentare

- [Documentația AI Toolkit](https://aka.ms/AIToolkit/doc)

## Ce urmează
- Următorul capitol: [Testare și depanare](../08-testing/README.md)

**Declinarea responsabilității**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși depunem eforturi pentru a asigura acuratețea, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă ar trebui considerat sursa autoritară. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist uman. Nu ne asumăm răspunderea pentru eventualele neînțelegeri sau interpretări greșite care pot apărea din utilizarea acestei traduceri.