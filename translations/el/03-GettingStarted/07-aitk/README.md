# Κατανάλωση ενός server από την επέκταση AI Toolkit για το Visual Studio Code

Όταν δημιουργείτε έναν πράκτορα AI, δεν πρόκειται μόνο για την παραγωγή έξυπνων απαντήσεων· πρόκειται επίσης για να δώσετε στον πράκτορά σας τη δυνατότητα να αναλαμβάνει δράση. Εδώ μπαίνει το Πρωτόκολλο Πλαισίου Μοντέλου (MCP). Το MCP καθιστά εύκολη την πρόσβαση των πρακτόρων σε εξωτερικά εργαλεία και υπηρεσίες με έναν συνεπή τρόπο. Σκεφτείτε το σαν να συνδέετε τον πράκτορά σας σε ένα κουτί εργαλείων που μπορεί *πραγματικά* να χρησιμοποιήσει.

Ας πούμε ότι συνδέετε έναν πράκτορα με τον υπολογιστικό server MCP σας. Ξαφνικά, ο πράκτοράς σας μπορεί να πραγματοποιεί μαθηματικές λειτουργίες απλώς λαμβάνοντας ένα prompt όπως «Πόσο κάνει 47 επί 89;»—χωρίς την ανάγκη να γράψετε χειροκίνητη λογική ή να δημιουργήσετε προσαρμοσμένα API.

## Επισκόπηση

Αυτό το μάθημα καλύπτει πώς να συνδέσετε έναν υπολογιστικό server MCP σε έναν πράκτορα με την επέκταση [AI Toolkit](https://aka.ms/AIToolkit) στο Visual Studio Code, επιτρέποντας στον πράκτορά σας να πραγματοποιεί μαθηματικές λειτουργίες όπως πρόσθεση, αφαίρεση, πολλαπλασιασμό και διαίρεση μέσω φυσικής γλώσσας.

Το AI Toolkit είναι μια ισχυρή επέκταση για το Visual Studio Code που απλοποιεί την ανάπτυξη πρακτόρων. Οι Μηχανικοί AI μπορούν εύκολα να δημιουργήσουν εφαρμογές AI αναπτύσσοντας και δοκιμάζοντας γενετικά μοντέλα AI—τοπικά ή στο cloud. Η επέκταση υποστηρίζει τα περισσότερα από τα κύρια γενετικά μοντέλα που είναι διαθέσιμα σήμερα.

*Σημείωση*: Το AI Toolkit υποστηρίζει προς το παρόν Python και TypeScript.

## Στόχοι Μάθησης

Μέχρι το τέλος αυτού του μαθήματος θα είστε σε θέση να:

- Καταναλώνετε έναν server MCP μέσω του AI Toolkit.
- Διαμορφώνετε μια ρύθμιση πράκτορα ώστε να μπορεί να ανακαλύπτει και να χρησιμοποιεί εργαλεία που παρέχονται από τον server MCP.
- Χρησιμοποιείτε εργαλεία MCP μέσω φυσικής γλώσσας.

## Προσέγγιση

Να πώς πρέπει να προσεγγίσουμε το θέμα σε υψηλό επίπεδο:

- Δημιουργήστε έναν πράκτορα και ορίστε το σύστημα prompt του.
- Δημιουργήστε έναν server MCP με εργαλεία υπολογιστή.
- Συνδέστε τον Agent Builder με τον server MCP.
- Δοκιμάστε την κλήση εργαλείων από τον πράκτορα μέσω φυσικής γλώσσας.

Ωραία, τώρα που καταλαβαίνουμε τη ροή, ας ρυθμίσουμε έναν πράκτορα AI να εκμεταλλευτεί εξωτερικά εργαλεία μέσω MCP, ενισχύοντας τις δυνατότητές του!

## Προαπαιτούμενα

- [Visual Studio Code](https://code.visualstudio.com/)
- [AI Toolkit for Visual Studio Code](https://aka.ms/AIToolkit)

## Άσκηση: Κατανάλωση server

> [!WARNING]
> Σημείωση για χρήστες macOS. Διερευνούμε αυτή τη στιγμή ένα πρόβλημα που επηρεάζει την εγκατάσταση εξαρτήσεων σε macOS. Ως αποτέλεσμα, οι χρήστες macOS δεν θα μπορούν να ολοκληρώσουν αυτή τη διδασκαλία αυτή τη στιγμή. Θα ενημερώσουμε τις οδηγίες μόλις είναι διαθέσιμη μια επίλυση. Σας ευχαριστούμε για την υπομονή και την κατανόησή σας!

Σε αυτή την άσκηση, θα δημιουργήσετε, θα τρέξετε και θα βελτιώσετε έναν πράκτορα AI με εργαλεία από έναν server MCP μέσα στο Visual Studio Code χρησιμοποιώντας το AI Toolkit.

### -0- Προβήμα, προσθέστε το μοντέλο OpenAI GPT-4o στα My Models

Η άσκηση χρησιμοποιεί το μοντέλο **GPT-4o**. Το μοντέλο πρέπει να προστεθεί στα **My Models** πριν τη δημιουργία του πράκτορα.

![Screenshot of a model selection interface in Visual Studio Code's AI Toolkit extension. The heading reads "Find the right model for your AI Solution" with a subtitle encouraging users to discover, test, and deploy AI models. Below, under “Popular Models,” six model cards are displayed: DeepSeek-R1 (GitHub-hosted), OpenAI GPT-4o, OpenAI GPT-4.1, OpenAI o1, Phi 4 Mini (CPU - Small, Fast), and DeepSeek-R1 (Ollama-hosted). Each card includes options to “Add” the model or “Try in Playground](../../../../translated_images/el/aitk-model-catalog.2acd38953bb9c119.webp)

1. Ανοίξτε την επέκταση **AI Toolkit** από τη **γραμμή δραστηριοτήτων**.
1. Στην ενότητα **Κατάλογος**, επιλέξτε **Models** για να ανοίξετε τον **Κατάλογο Μοντέλων**. Η επιλογή των **Models** ανοίγει τον **Κατάλογο Μοντέλων** σε νέα καρτέλα επεξεργασίας.
1. Στη γραμμή αναζήτησης του **Καταλόγου Μοντέλων**, πληκτρολογήστε **OpenAI GPT-4o**.
1. Κάντε κλικ στο **+ Πρόσθεση** για να προσθέσετε το μοντέλο στη λίστα **My Models**. Βεβαιωθείτε ότι έχετε επιλέξει το μοντέλο που είναι **Φιλοξενούμενο από το GitHub**.
1. Στη **γραμμή δραστηριοτήτων**, επιβεβαιώστε ότι το μοντέλο **OpenAI GPT-4o** εμφανίζεται στη λίστα.

### -1- Δημιουργία πράκτορα

Ο **Agent (Prompt) Builder** σας επιτρέπει να δημιουργήσετε και να προσαρμόσετε τους δικούς σας πράκτορες με δυνατότητα AI. Σε αυτή την ενότητα, θα δημιουργήσετε έναν νέο πράκτορα και θα του αναθέσετε ένα μοντέλο για να τροφοδοτήσει τη συνομιλία.

![Screenshot of the "Calculator Agent" builder interface in the AI Toolkit extension for Visual Studio Code. On the left panel, the model selected is "OpenAI GPT-4o (via GitHub)." A system prompt reads "You are a professor in university teaching math," and the user prompt says, "Explain to me the Fourier equation in simple terms." Additional options include buttons for adding tools, enabling MCP Server, and selecting structured output. A blue “Run” button is at the bottom. On the right panel, under "Get Started with Examples," three sample agents are listed: Web Developer (with MCP Server, Second-Grade Simplifier, and Dream Interpreter, each with brief descriptions of their functions.](../../../../translated_images/el/aitk-agent-builder.901e3a2960c3e477.webp)

1. Ανοίξτε την επέκταση **AI Toolkit** από τη **γραμμή δραστηριοτήτων**.
1. Στην ενότητα **Εργαλεία**, επιλέξτε **Agent (Prompt) Builder**. Η επιλογή **Agent (Prompt) Builder** ανοίγει τον **Agent (Prompt) Builder** σε νέα καρτέλα επεξεργασίας.
1. Κάντε κλικ στο κουμπί **+ Νέος Πράκτορας**. Η επέκταση θα ξεκινήσει έναν οδηγό ρύθμισης μέσω του **Command Palette**.
1. Πληκτρολογήστε το όνομα **Calculator Agent** και πατήστε **Enter**.
1. Στον **Agent (Prompt) Builder**, για το πεδίο **Model**, επιλέξτε το μοντέλο **OpenAI GPT-4o (via GitHub)**.

### -2- Δημιουργία συστήματος prompt για τον πράκτορα

Με τον πράκτορα να έχει δημιουργηθεί, είναι η ώρα να ορίσετε την προσωπικότητα και το σκοπό του. Σε αυτή την ενότητα, θα χρησιμοποιήσετε τη λειτουργία **Generate system prompt** για να περιγράψετε τη συμπεριφορά που προορίζεται για τον πράκτορα—στην προκειμένη περίπτωση, έναν πράκτορα υπολογιστή—και θα ζητήσετε από το μοντέλο να γράψει το σύστημα prompt για εσάς.

![Screenshot of the "Calculator Agent" interface in the AI Toolkit for Visual Studio Code with a modal window open titled "Generate a prompt." The modal explains that a prompt template can be generated by sharing basic details and includes a text box with the sample system prompt: "You are a helpful and efficient math assistant. When given a problem involving basic arithmetic, you respond with the correct result." Below the text box are "Close" and "Generate" buttons. In the background, part of the agent configuration is visible, including the selected model "OpenAI GPT-4o (via GitHub)" and fields for system and user prompts.](../../../../translated_images/el/aitk-generate-prompt.ba9e69d3d2bbe2a2.webp)

1. Στην ενότητα **Prompts**, κάντε κλικ στο κουμπί **Generate system prompt**. Αυτό το κουμπί ανοίγει τον δημιουργό prompt που χρησιμοποιεί AI για να δημιουργήσει ένα σύστημα prompt για τον πράκτορα.
1. Στο παράθυρο **Generate a prompt**, εισάγετε το εξής: `You are a helpful and efficient math assistant. When given a problem involving basic arithmetic, you respond with the correct result.`
1. Κάντε κλικ στο κουμπί **Generate**. Θα εμφανιστεί μια ειδοποίηση στην κάτω δεξιά γωνία που επιβεβαιώνει ότι το σύστημα prompt δημιουργείται. Μόλις ολοκληρωθεί η δημιουργία του prompt, το prompt θα εμφανιστεί στο πεδίο **System prompt** του **Agent (Prompt) Builder**.
1. Εξετάστε το **System prompt** και τροποποιήστε το αν χρειάζεται.

### -3- Δημιουργία server MCP

Τώρα που έχετε ορίσει το σύστημα prompt του πράκτορά σας—καθοδηγώντας τη συμπεριφορά και τις απαντήσεις του—είναι ώρα να εξοπλίσετε τον πράκτορα με πρακτικές δυνατότητες. Σε αυτή την ενότητα, θα δημιουργήσετε έναν υπολογιστικό server MCP με εργαλεία για την εκτέλεση πράξεων πρόσθεσης, αφαίρεσης, πολλαπλασιασμού και διαίρεσης. Αυτός ο server θα επιτρέψει στον πράκτορά σας να εκτελεί μαθηματικές λειτουργίες σε πραγματικό χρόνο ως απάντηση σε prompts φυσικής γλώσσας.

!["Screenshot of the lower section of the Calculator Agent interface in the AI Toolkit extension for Visual Studio Code. It shows expandable menus for “Tools” and “Structure output,” along with a dropdown menu labeled “Choose output format” set to “text.” To the right, there is a button labeled “+ MCP Server” for adding a Model Context Protocol server. An image icon placeholder is shown above the Tools section.](../../../../translated_images/el/aitk-add-mcp-server.9742cfddfe808353.webp)

Το AI Toolkit διαθέτει προτύπα για να διευκολύνει τη δημιουργία του δικού σας server MCP. Θα χρησιμοποιήσουμε το πρότυπο Python για να δημιουργήσουμε τον υπολογιστικό server MCP.

*Σημείωση*: Το AI Toolkit υποστηρίζει προς το παρόν Python και TypeScript.

1. Στην ενότητα **Tools** του **Agent (Prompt) Builder**, κάντε κλικ στο κουμπί **+ MCP Server**. Η επέκταση θα ξεκινήσει έναν οδηγό ρύθμισης μέσω του **Command Palette**.
1. Επιλέξτε **+ Add Server**.
1. Επιλέξτε **Create a New MCP Server**.
1. Επιλέξτε το πρότυπο **python-weather**.
1. Επιλέξτε **Default folder** για να αποθηκεύσετε το πρότυπο server MCP.
1. Εισάγετε το ακόλουθο όνομα για τον server: **Calculator**
1. Θα ανοίξει ένα νέο παράθυρο Visual Studio Code. Επιλέξτε **Yes, I trust the authors**.
1. Χρησιμοποιώντας το τερματικό (**Terminal** > **New Terminal**), δημιουργήστε ένα εικονικό περιβάλλον: `python -m venv .venv`
1. Χρησιμοποιώντας το τερματικό, ενεργοποιήστε το εικονικό περιβάλλον:
    1. Windows - `.venv\Scripts\activate`
    1. macOS/Linux - `source .venv/bin/activate`
1. Χρησιμοποιώντας το τερματικό, εγκαταστήστε τις εξαρτήσεις: `pip install -e .[dev]`
1. Στην προβολή **Explorer** της **γραμμής δραστηριοτήτων**, επεκτείνετε τον κατάλογο **src** και επιλέξτε το αρχείο **server.py** για να το ανοίξετε στον επεξεργαστή.
1. Αντικαταστήστε τον κώδικα στο αρχείο **server.py** με τον ακόλουθο και αποθηκεύστε:

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

### -4- Τρέξτε τον πράκτορα με τον υπολογιστικό server MCP

Τώρα που ο πράκτοράς σας διαθέτει εργαλεία, ήρθε η ώρα να τα χρησιμοποιήσετε! Σε αυτή την ενότητα, θα υποβάλετε prompts στον πράκτορα για να δοκιμάσετε και να επιβεβαιώσετε αν ο πράκτορας εκμεταλλεύεται το κατάλληλο εργαλείο από τον υπολογιστικό server MCP.

![Screenshot of the Calculator Agent interface in the AI Toolkit extension for Visual Studio Code. On the left panel, under “Tools,” an MCP server named local-server-calculator_server is added, showing four available tools: add, subtract, multiply, and divide. A badge shows that four tools are active. Below is a collapsed “Structure output” section and a blue “Run” button. On the right panel, under “Model Response,” the agent invokes the multiply and subtract tools with inputs {"a": 3, "b": 25} and {"a": 75, "b": 20} respectively. The final “Tool Response” is shown as 75.0. A “View Code” button appears at the bottom.](../../../../translated_images/el/aitk-agent-response-with-tools.e7c781869dc8041a.webp)

Θα τρέξετε τον υπολογιστικό server MCP στην τοπική σας μηχανή ανάπτυξης μέσω του **Agent Builder** ως client MCP.

1. Πατήστε `F5` για να ξεκινήσετε το debugging του server MCP. Ο **Agent (Prompt) Builder** θα ανοίξει σε νέα καρτέλα επεξεργασίας. Η κατάσταση του server είναι ορατή στο τερματικό.
1. Στο πεδίο **User prompt** του **Agent (Prompt) Builder**, εισάγετε το εξής prompt: `I bought 3 items priced at $25 each, and then used a $20 discount. How much did I pay?`
1. Κάντε κλικ στο κουμπί **Run** για να δημιουργήσετε την απάντηση του πράκτορα.
1. Εξετάστε την έξοδο του πράκτορα. Το μοντέλο πρέπει να συμπεράνει ότι πληρώσατε **$55**.
1. Παρακάτω είναι μια ανάλυση του τι πρέπει να συμβεί:
    - Ο πράκτορας επιλέγει τα εργαλεία **multiply** και **subtract** για να βοηθήσουν στον υπολογισμό.
    - Οι αντίστοιχες τιμές `a` και `b` ανατίθενται για το εργαλείο **multiply**.
    - Οι αντίστοιχες τιμές `a` και `b` ανατίθενται για το εργαλείο **subtract**.
    - Η απάντηση από κάθε εργαλείο παρέχεται στο αντίστοιχο **Tool Response**.
    - Η τελική έξοδος από το μοντέλο παρέχεται στην τελική **Model Response**.
1. Υποβάλετε επιπλέον prompts για περαιτέρω δοκιμαστικά στον πράκτορα. Μπορείτε να τροποποιήσετε το υπάρχον prompt στο πεδίο **User prompt** κάνοντας κλικ μέσα σε αυτό και αντικαθιστώντας το υπάρχον prompt.
1. Όταν ολοκληρώσετε τις δοκιμές του πράκτορα, μπορείτε να σταματήσετε τον server μέσω του **τερματικού** εισάγοντας **CTRL/CMD+C** για έξοδο.

## Ανάθεση

Δοκιμάστε να προσθέσετε μια επιπλέον καταχώρηση εργαλείου στο αρχείο **server.py** σας (π.χ., να υπολογίζει την τετραγωνική ρίζα ενός αριθμού). Υποβάλετε πρόσθετα prompts που θα απαιτούν από τον πράκτορα να χρησιμοποιήσει το νέο εργαλείο σας (ή υπάρχοντα εργαλεία). Φροντίστε να επανεκκινήσετε τον server για να φορτωθούν τα νέα εργαλεία.

## Λύση

[Λύση](./solution/README.md)

## Βασικά Σημεία

Τα βασικά σημεία από αυτό το κεφάλαιο είναι τα εξής:

- Η επέκταση AI Toolkit είναι ένας εξαιρετικός πελάτης που σας επιτρέπει να καταναλώνετε servers MCP και τα εργαλεία τους.
- Μπορείτε να προσθέσετε νέα εργαλεία σε servers MCP, διευρύνοντας τις δυνατότητες του πράκτορα για να καλύψει τις εξελισσόμενες ανάγκες.
- Το AI Toolkit περιλαμβάνει πρότυπα (π.χ., πρότυπα Python MCP server) για να απλοποιήσει τη δημιουργία προσαρμοσμένων εργαλείων.

## Επιπλέον Πόροι

- [Τεκμηρίωση AI Toolkit](https://aka.ms/AIToolkit/doc)

## Τι Ακολουθεί
- Επόμενο: [Testing & Debugging](../08-testing/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Αποποίηση ευθυνών**:
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας την υπηρεσία μετάφρασης με τεχνητή νοημοσύνη [Co-op Translator](https://github.com/Azure/co-op-translator). Ενώ επιδιώκουμε την ακρίβεια, παρακαλούμε να έχετε υπόψη ότι οι αυτοματοποιημένες μεταφράσεις ενδέχεται να περιέχουν λάθη ή ανακρίβειες. Το πρωτότυπο έγγραφο στη μητρική του γλώσσα πρέπει να θεωρείται η αυθεντική πηγή. Για κρίσιμες πληροφορίες, συνιστάται επαγγελματική ανθρώπινη μετάφραση. Δεν φέρουμε ευθύνη για τυχόν παρεξηγήσεις ή λανθασμένες ερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->