# Weather MCP Server

Αυτός είναι ένας δείγμα MCP Server γραμμένος σε Python που υλοποιεί εργαλεία καιρού με ψεύτικες απαντήσεις. Μπορεί να χρησιμοποιηθεί ως βάση για τον δικό σας MCP Server. Περιλαμβάνει τις εξής δυνατότητες:

- **Εργαλείο Καιρού**: Ένα εργαλείο που παρέχει ψεύτικες πληροφορίες καιρού με βάση την δεδομένη τοποθεσία.
- **Εργαλείο Git Clone**: Ένα εργαλείο που κλωνοποιεί ένα git repository σε έναν καθορισμένο φάκελο.
- **Εργαλείο Άνοιγμα στο VS Code**: Ένα εργαλείο που ανοίγει έναν φάκελο στο VS Code ή στο VS Code Insiders.
- **Σύνδεση με Agent Builder**: Μια δυνατότητα που σας επιτρέπει να συνδέσετε τον MCP server με το Agent Builder για δοκιμές και αποσφαλμάτωση.
- **Αποσφαλμάτωση στο [MCP Inspector](https://github.com/modelcontextprotocol/inspector)**: Μια δυνατότητα που σας επιτρέπει να αποσφαλματώσετε τον MCP Server χρησιμοποιώντας το MCP Inspector.

## Ξεκινήστε με το πρότυπο Weather MCP Server

> **Προαπαιτούμενα**
>
> Για να εκτελέσετε τον MCP Server στον τοπικό υπολογιστή ανάπτυξης, θα χρειαστείτε:
>
> - [Python](https://www.python.org/)
> - [Git](https://git-scm.com/) (Απαιτείται για το εργαλείο git_clone_repo)
> - [VS Code](https://code.visualstudio.com/) ή [VS Code Insiders](https://code.visualstudio.com/insiders/) (Απαιτείται για το εργαλείο open_in_vscode)
> - (*Προαιρετικό - αν προτιμάτε το uv*) [uv](https://github.com/astral-sh/uv)
> - [Python Debugger Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.debugpy)

## Προετοιμασία περιβάλλοντος

Υπάρχουν δύο τρόποι για να ρυθμίσετε το περιβάλλον για αυτό το έργο. Μπορείτε να επιλέξετε οποιονδήποτε από αυτούς ανάλογα με την προτίμησή σας.

> Σημείωση: Επαναφορτώστε το VSCode ή το τερματικό για να βεβαιωθείτε ότι χρησιμοποιείται το Python του εικονικού περιβάλλοντος μετά τη δημιουργία του.

| Τρόπος | Βήματα |
| ------ | ------ |
| Χρήση `uv` | 1. Δημιουργήστε εικονικό περιβάλλον: `uv venv` <br>2. Εκτελέστε την εντολή του VSCode "***Python: Select Interpreter***" και επιλέξτε το Python από το δημιουργημένο εικονικό περιβάλλον <br>3. Εγκαταστήστε εξαρτήσεις (συμπεριλαμβανομένων των εξαρτήσεων ανάπτυξης): `uv pip install -r pyproject.toml --extra dev` |
| Χρήση `pip` | 1. Δημιουργήστε εικονικό περιβάλλον: `python -m venv .venv` <br>2. Εκτελέστε την εντολή του VSCode "***Python: Select Interpreter***" και επιλέξτε το Python από το δημιουργημένο εικονικό περιβάλλον <br>3. Εγκαταστήστε εξαρτήσεις (συμπεριλαμβανομένων των εξαρτήσεων ανάπτυξης): `pip install -e .[dev]` |

Αφού ρυθμίσετε το περιβάλλον, μπορείτε να εκτελέσετε τον server στον τοπικό υπολογιστή ανάπτυξης μέσω του Agent Builder ως MCP Client για να ξεκινήσετε:
1. Ανοίξτε τον πίνακα αποσφαλμάτωσης του VS Code. Επιλέξτε `Debug in Agent Builder` ή πατήστε `F5` για να ξεκινήσετε την αποσφαλμάτωση του MCP server.
2. Χρησιμοποιήστε το AI Toolkit Agent Builder για να δοκιμάσετε τον server με [αυτό το prompt](../../../../../../../../../../../open_prompt_builder). Ο server θα συνδεθεί αυτόματα με το Agent Builder.
3. Πατήστε `Run` για να δοκιμάσετε τον server με το prompt.

**Συγχαρητήρια**! Έχετε εκτελέσει επιτυχώς τον Weather MCP Server στον τοπικό υπολογιστή ανάπτυξης μέσω του Agent Builder ως MCP Client.
![DebugMCP](https://raw.githubusercontent.com/microsoft/windows-ai-studio-templates/refs/heads/dev/mcpServers/mcp_debug.gif)

## Τι περιλαμβάνεται στο πρότυπο

| Φάκελος / Αρχείο | Περιεχόμενα                                     |
| ---------------- | ----------------------------------------------- |
| `.vscode`        | Αρχεία VSCode για αποσφαλμάτωση                |
| `.aitk`          | Ρυθμίσεις για το AI Toolkit                    |
| `src`            | Ο πηγαίος κώδικας για τον Weather MCP Server   |

## Πώς να αποσφαλματώσετε τον Weather MCP Server

> Σημειώσεις:
> - Το [MCP Inspector](https://github.com/modelcontextprotocol/inspector) είναι ένα οπτικό εργαλείο ανάπτυξης για δοκιμή και αποσφαλμάτωση MCP servers.
> - Όλοι οι τρόποι αποσφαλμάτωσης υποστηρίζουν σημεία διακοπής, ώστε να μπορείτε να προσθέσετε σημεία διακοπής στον κώδικα υλοποίησης εργαλείων.

## Διαθέσιμα Εργαλεία

### Εργαλείο Καιρού
Το εργαλείο `get_weather` παρέχει ψεύτικες πληροφορίες καιρού για μια καθορισμένη τοποθεσία.

| Παράμετρος | Τύπος | Περιγραφή |
| ---------- | ----- | --------- |
| `location` | string | Τοποθεσία για την οποία θέλετε πληροφορίες καιρού (π.χ., όνομα πόλης, πολιτεία ή συντεταγμένες) |

### Εργαλείο Git Clone
Το εργαλείο `git_clone_repo` κλωνοποιεί ένα git repository σε έναν καθορισμένο φάκελο.

| Παράμετρος | Τύπος | Περιγραφή |
| ---------- | ----- | --------- |
| `repo_url` | string | URL του git repository για κλωνοποίηση |
| `target_folder` | string | Διαδρομή προς τον φάκελο όπου θα κλωνοποιηθεί το repository |

Το εργαλείο επιστρέφει ένα αντικείμενο JSON με:
- `success`: Boolean που δείχνει αν η λειτουργία ήταν επιτυχής
- `target_folder` ή `error`: Η διαδρομή του κλωνοποιημένου repository ή ένα μήνυμα σφάλματος

### Εργαλείο Άνοιγμα στο VS Code
Το εργαλείο `open_in_vscode` ανοίγει έναν φάκελο στο VS Code ή στο VS Code Insiders.

| Παράμετρος | Τύπος | Περιγραφή |
| ---------- | ----- | --------- |
| `folder_path` | string | Διαδρομή προς τον φάκελο που θέλετε να ανοίξετε |
| `use_insiders` | boolean (προαιρετικό) | Αν θα χρησιμοποιηθεί το VS Code Insiders αντί για το κανονικό VS Code |

Το εργαλείο επιστρέφει ένα αντικείμενο JSON με:
- `success`: Boolean που δείχνει αν η λειτουργία ήταν επιτυχής
- `message` ή `error`: Ένα μήνυμα επιβεβαίωσης ή ένα μήνυμα σφάλματος

| Τρόπος Αποσφαλμάτωσης | Περιγραφή | Βήματα για αποσφαλμάτωση |
| --------------------- | --------- | ----------------------- |
| Agent Builder | Αποσφαλμάτωση του MCP server στο Agent Builder μέσω του AI Toolkit. | 1. Ανοίξτε τον πίνακα αποσφαλμάτωσης του VS Code. Επιλέξτε `Debug in Agent Builder` και πατήστε `F5` για να ξεκινήσετε την αποσφαλμάτωση του MCP server.<br>2. Χρησιμοποιήστε το AI Toolkit Agent Builder για να δοκιμάσετε τον server με [αυτό το prompt](../../../../../../../../../../../open_prompt_builder). Ο server θα συνδεθεί αυτόματα με το Agent Builder.<br>3. Πατήστε `Run` για να δοκιμάσετε τον server με το prompt. |
| MCP Inspector | Αποσφαλμάτωση του MCP server χρησιμοποιώντας το MCP Inspector. | 1. Εγκαταστήστε [Node.js](https://nodejs.org/)<br> 2. Ρυθμίστε το Inspector: `cd inspector` && `npm install` <br> 3. Ανοίξτε τον πίνακα αποσφαλμάτωσης του VS Code. Επιλέξτε `Debug SSE in Inspector (Edge)` ή `Debug SSE in Inspector (Chrome)`. Πατήστε F5 για να ξεκινήσετε την αποσφαλμάτωση.<br> 4. Όταν το MCP Inspector ανοίξει στον browser, πατήστε το κουμπί `Connect` για να συνδέσετε αυτόν τον MCP server.<br> 5. Στη συνέχεια μπορείτε να `List Tools`, να επιλέξετε ένα εργαλείο, να εισάγετε παραμέτρους και να `Run Tool` για να αποσφαλματώσετε τον κώδικα του server. |

## Προεπιλεγμένες Θύρες και προσαρμογές

| Τρόπος Αποσφαλμάτωσης | Θύρες | Ορισμοί | Προσαρμογές | Σημείωση |
| --------------------- | ----- | -------- | ----------- | -------- |
| Agent Builder | 3001 | [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json) | Επεξεργαστείτε τα [launch.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/launch.json), [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json), [\_\_init\_\_.py](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/src/__init__.py), [mcp.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.aitk/mcp.json) για να αλλάξετε τις παραπάνω θύρες. | N/A |
| MCP Inspector | 3001 (Server); 5173 και 3000 (Inspector) | [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json) | Επεξεργαστείτε τα [launch.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/launch.json), [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json), [\_\_init\_\_.py](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/src/__init__.py), [mcp.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.aitk/mcp.json) για να αλλάξετε τις παραπάνω θύρες. | N/A |

## Σχόλια

Αν έχετε οποιαδήποτε σχόλια ή προτάσεις για αυτό το πρότυπο, παρακαλούμε ανοίξτε ένα ζήτημα στο [AI Toolkit GitHub repository](https://github.com/microsoft/vscode-ai-toolkit/issues).

---

**Αποποίηση ευθύνης**:  
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας την υπηρεσία αυτόματης μετάφρασης [Co-op Translator](https://github.com/Azure/co-op-translator). Παρόλο που καταβάλλουμε προσπάθειες για ακρίβεια, παρακαλούμε να έχετε υπόψη ότι οι αυτόματες μεταφράσεις ενδέχεται να περιέχουν λάθη ή ανακρίβειες. Το πρωτότυπο έγγραφο στη μητρική του γλώσσα θα πρέπει να θεωρείται η αυθεντική πηγή. Για κρίσιμες πληροφορίες, συνιστάται επαγγελματική μετάφραση από ανθρώπους. Δεν φέρουμε ευθύνη για τυχόν παρεξηγήσεις ή εσφαλμένες ερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.