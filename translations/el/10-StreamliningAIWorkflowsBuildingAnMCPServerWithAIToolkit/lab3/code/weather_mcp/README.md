# Weather MCP Server

Αυτό είναι ένα δείγμα MCP Server σε Python που υλοποιεί εργαλεία καιρού με προσομοιωμένες απαντήσεις. Μπορεί να χρησιμοποιηθεί ως βάση για τον δικό σας MCP Server. Περιλαμβάνει τις εξής λειτουργίες:

- **Weather Tool**: Ένα εργαλείο που παρέχει προσομοιωμένες πληροφορίες καιρού βάσει της δοθείσας τοποθεσίας.
- **Σύνδεση με Agent Builder**: Μια λειτουργία που σας επιτρέπει να συνδέσετε τον MCP server με τον Agent Builder για δοκιμές και αποσφαλμάτωση.
- **Αποσφαλμάτωση στο [MCP Inspector](https://github.com/modelcontextprotocol/inspector)**: Μια λειτουργία που σας επιτρέπει να αποσφαλματώσετε τον MCP Server χρησιμοποιώντας το MCP Inspector.

## Ξεκινώντας με το πρότυπο Weather MCP Server

> **Προαπαιτούμενα**
>
> Για να τρέξετε τον MCP Server στον τοπικό σας υπολογιστή ανάπτυξης, θα χρειαστείτε:
>
> - [Python](https://www.python.org/)
> - (*Προαιρετικό - αν προτιμάτε uv*) [uv](https://github.com/astral-sh/uv)
> - [Python Debugger Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.debugpy)

## Προετοιμασία περιβάλλοντος

Υπάρχουν δύο τρόποι για να ρυθμίσετε το περιβάλλον για αυτό το έργο. Μπορείτε να επιλέξετε όποιον προτιμάτε.

> Σημείωση: Κάντε επανεκκίνηση του VSCode ή του τερματικού για να βεβαιωθείτε ότι χρησιμοποιείται η python του εικονικού περιβάλλοντος μετά τη δημιουργία του.

| Τρόπος | Βήματα |
| -------- | ----- |
| Χρήση `uv` | 1. Δημιουργία εικονικού περιβάλλοντος: `uv venv` <br>2. Εκτέλεση της εντολής VSCode "***Python: Select Interpreter***" και επιλογή της python από το δημιουργημένο εικονικό περιβάλλον <br>3. Εγκατάσταση εξαρτήσεων (συμπεριλαμβανομένων των dev): `uv pip install -r pyproject.toml --extra dev` |
| Χρήση `pip` | 1. Δημιουργία εικονικού περιβάλλοντος: `python -m venv .venv` <br>2. Εκτέλεση της εντολής VSCode "***Python: Select Interpreter***" και επιλογή της python από το δημιουργημένο εικονικό περιβάλλον<br>3. Εγκατάσταση εξαρτήσεων (συμπεριλαμβανομένων των dev): `pip install -e .[dev]` |

Αφού ρυθμίσετε το περιβάλλον, μπορείτε να τρέξετε τον server στον τοπικό σας υπολογιστή ανάπτυξης μέσω του Agent Builder ως MCP Client για να ξεκινήσετε:
1. Ανοίξτε το πάνελ αποσφαλμάτωσης του VS Code. Επιλέξτε `Debug in Agent Builder` ή πατήστε `F5` για να ξεκινήσετε την αποσφαλμάτωση του MCP server.
2. Χρησιμοποιήστε το AI Toolkit Agent Builder για να δοκιμάσετε τον server με [αυτό το prompt](../../../../../../../../../../open_prompt_builder). Ο server θα συνδεθεί αυτόματα με τον Agent Builder.
3. Πατήστε `Run` για να δοκιμάσετε τον server με το prompt.

**Συγχαρητήρια**! Έχετε τρέξει επιτυχώς τον Weather MCP Server στον τοπικό σας υπολογιστή ανάπτυξης μέσω του Agent Builder ως MCP Client.  
![DebugMCP](https://raw.githubusercontent.com/microsoft/windows-ai-studio-templates/refs/heads/dev/mcpServers/mcp_debug.gif)

## Τι περιλαμβάνει το πρότυπο

| Φάκελος / Αρχείο | Περιεχόμενα                                  |
| ---------------- | -------------------------------------------- |
| `.vscode`        | Αρχεία VSCode για αποσφαλμάτωση              |
| `.aitk`          | Ρυθμίσεις για το AI Toolkit                   |
| `src`            | Ο πηγαίος κώδικας για τον weather mcp server |

## Πώς να αποσφαλματώσετε τον Weather MCP Server

> Σημειώσεις:
> - Το [MCP Inspector](https://github.com/modelcontextprotocol/inspector) είναι ένα οπτικό εργαλείο ανάπτυξης για δοκιμές και αποσφαλμάτωση MCP servers.
> - Όλοι οι τρόποι αποσφαλμάτωσης υποστηρίζουν σημεία διακοπής (breakpoints), ώστε να μπορείτε να προσθέσετε σημεία διακοπής στον κώδικα υλοποίησης του εργαλείου.

| Τρόπος Αποσφαλμάτωσης | Περιγραφή | Βήματα αποσφαλμάτωσης |
| --------------------- | --------- | --------------------- |
| Agent Builder | Αποσφαλμάτωση του MCP server στον Agent Builder μέσω AI Toolkit. | 1. Ανοίξτε το πάνελ αποσφαλμάτωσης του VS Code. Επιλέξτε `Debug in Agent Builder` και πατήστε `F5` για να ξεκινήσετε την αποσφαλμάτωση του MCP server.<br>2. Χρησιμοποιήστε το AI Toolkit Agent Builder για να δοκιμάσετε τον server με [αυτό το prompt](../../../../../../../../../../open_prompt_builder). Ο server θα συνδεθεί αυτόματα με τον Agent Builder.<br>3. Πατήστε `Run` για να δοκιμάσετε τον server με το prompt. |
| MCP Inspector | Αποσφαλμάτωση του MCP server χρησιμοποιώντας το MCP Inspector. | 1. Εγκαταστήστε [Node.js](https://nodejs.org/)<br>2. Ρυθμίστε το Inspector: `cd inspector` && `npm install` <br>3. Ανοίξτε το πάνελ αποσφαλμάτωσης του VS Code. Επιλέξτε `Debug SSE in Inspector (Edge)` ή `Debug SSE in Inspector (Chrome)`. Πατήστε F5 για να ξεκινήσετε την αποσφαλμάτωση.<br>4. Όταν το MCP Inspector ανοίξει στον browser, πατήστε το κουμπί `Connect` για να συνδέσετε αυτόν τον MCP server.<br>5. Στη συνέχεια μπορείτε να κάνετε `List Tools`, να επιλέξετε ένα εργαλείο, να εισάγετε παραμέτρους και να πατήσετε `Run Tool` για να αποσφαλματώσετε τον κώδικα του server.<br> |

## Προεπιλεγμένες θύρες και προσαρμογές

| Τρόπος Αποσφαλμάτωσης | Θύρες | Ορισμοί | Προσαρμογές | Σημείωση |
| --------------------- | ----- | -------- | ------------ | -------- |
| Agent Builder | 3001 | [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/tasks.json) | Επεξεργαστείτε τα [launch.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/launch.json), [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/tasks.json), [\_\_init\_\_.py](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/src/__init__.py), [mcp.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.aitk/mcp.json) για να αλλάξετε τις παραπάνω θύρες. | N/A |
| MCP Inspector | 3001 (Server); 5173 και 3000 (Inspector) | [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/tasks.json) | Επεξεργαστείτε τα [launch.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/launch.json), [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/tasks.json), [\_\_init\_\_.py](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/src/__init__.py), [mcp.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.aitk/mcp.json) για να αλλάξετε τις παραπάνω θύρες. | N/A |

## Ανατροφοδότηση

Αν έχετε οποιαδήποτε σχόλια ή προτάσεις για αυτό το πρότυπο, παρακαλώ ανοίξτε ένα issue στο [AI Toolkit GitHub repository](https://github.com/microsoft/vscode-ai-toolkit/issues)

**Αποποίηση ευθυνών**:  
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας την υπηρεσία αυτόματης μετάφρασης AI [Co-op Translator](https://github.com/Azure/co-op-translator). Παρόλο που επιδιώκουμε την ακρίβεια, παρακαλούμε να γνωρίζετε ότι οι αυτόματες μεταφράσεις ενδέχεται να περιέχουν λάθη ή ανακρίβειες. Το πρωτότυπο έγγραφο στη γλώσσα του θεωρείται η αυθεντική πηγή. Για κρίσιμες πληροφορίες, συνιστάται επαγγελματική ανθρώπινη μετάφραση. Δεν φέρουμε ευθύνη για τυχόν παρεξηγήσεις ή λανθασμένες ερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.