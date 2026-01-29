# 🔧 Ενότητα 3: Προχωρημένη Ανάπτυξη MCP με το AI Toolkit

![Duration](https://img.shields.io/badge/Duration-20_minutes-blue?style=flat-square)
![AI Toolkit](https://img.shields.io/badge/AI_Toolkit-Required-orange?style=flat-square)
![Python](https://img.shields.io/badge/Python-3.10+-green?style=flat-square)
![MCP SDK](https://img.shields.io/badge/MCP_SDK-1.9.3-purple?style=flat-square)
![Inspector](https://img.shields.io/badge/MCP_Inspector-0.14.0-blue?style=flat-square)

## 🎯 Στόχοι Μάθησης

Στο τέλος αυτού του εργαστηρίου, θα μπορείτε να:

- ✅ Δημιουργείτε προσαρμοσμένους MCP servers χρησιμοποιώντας το AI Toolkit
- ✅ Ρυθμίζετε και χρησιμοποιείτε το πιο πρόσφατο MCP Python SDK (v1.9.3)
- ✅ Εγκαθιστάτε και αξιοποιείτε το MCP Inspector για αποσφαλμάτωση
- ✅ Αποσφαλματώνετε MCP servers τόσο στο Agent Builder όσο και στο Inspector
- ✅ Κατανοείτε προχωρημένες ροές εργασίας ανάπτυξης MCP servers

## 📋 Προαπαιτούμενα

- Ολοκλήρωση του Εργαστηρίου 2 (Βασικά MCP)
- VS Code με εγκατεστημένη την επέκταση AI Toolkit
- Περιβάλλον Python 3.10+
- Node.js και npm για την εγκατάσταση του Inspector

## 🏗️ Τι θα Δημιουργήσετε

Σε αυτό το εργαστήριο, θα δημιουργήσετε έναν **Weather MCP Server** που παρουσιάζει:
- Υλοποίηση προσαρμοσμένου MCP server
- Ενσωμάτωση με το AI Toolkit Agent Builder
- Επαγγελματικές ροές εργασίας αποσφαλμάτωσης
- Σύγχρονες πρακτικές χρήσης MCP SDK

---

## 🔧 Επισκόπηση Βασικών Συστατικών

### 🐍 MCP Python SDK
Το Model Context Protocol Python SDK παρέχει τη βάση για την κατασκευή προσαρμοσμένων MCP servers. Θα χρησιμοποιήσετε την έκδοση 1.9.3 με βελτιωμένες δυνατότητες αποσφαλμάτωσης.

### 🔍 MCP Inspector
Ένα ισχυρό εργαλείο αποσφαλμάτωσης που προσφέρει:
- Παρακολούθηση server σε πραγματικό χρόνο
- Οπτικοποίηση εκτέλεσης εργαλείων
- Επιθεώρηση αιτημάτων/απαντήσεων δικτύου
- Διαδραστικό περιβάλλον δοκιμών

---

## 📖 Βήμα-βήμα Υλοποίηση

### Βήμα 1: Δημιουργία WeatherAgent στο Agent Builder

1. **Εκκινήστε το Agent Builder** στο VS Code μέσω της επέκτασης AI Toolkit
2. **Δημιουργήστε νέο agent** με την παρακάτω ρύθμιση:
   - Όνομα Agent: `WeatherAgent`

![Agent Creation](../../../../translated_images/el/Agent.c9c33f6a412b4cdedfb973fe5448bdb33de3f400055603111b875610e9b917ab.png)

### Βήμα 2: Αρχικοποίηση Έργου MCP Server

1. **Μεταβείτε στα Εργαλεία** → **Προσθήκη Εργαλείου** στο Agent Builder
2. **Επιλέξτε "MCP Server"** από τις διαθέσιμες επιλογές
3. **Επιλέξτε "Δημιουργία νέου MCP Server"**
4. **Επιλέξτε το πρότυπο `python-weather`**
5. **Ονομάστε τον server σας:** `weather_mcp`

![Python Template Selection](../../../../translated_images/el/Pythontemplate.9d0a2913c6491500bd673430f024dc44676af2808a27b5da9dcc0eb7063adc28.png)

### Βήμα 3: Άνοιγμα και Εξέταση του Έργου

1. **Ανοίξτε το δημιουργημένο έργο** στο VS Code
2. **Εξετάστε τη δομή του έργου:**
   ```
   weather_mcp/
   ├── src/
   │   ├── __init__.py
   │   └── server.py
   ├── inspector/
   │   ├── package.json
   │   └── package-lock.json
   ├── .vscode/
   │   ├── launch.json
   │   └── tasks.json
   ├── pyproject.toml
   └── README.md
   ```

### Βήμα 4: Αναβάθμιση στην Τελευταία Έκδοση MCP SDK

> **🔍 Γιατί Αναβάθμιση;** Θέλουμε να χρησιμοποιήσουμε το πιο πρόσφατο MCP SDK (v1.9.3) και την υπηρεσία Inspector (0.14.0) για βελτιωμένες λειτουργίες και καλύτερη αποσφαλμάτωση.

#### 4α. Ενημέρωση Εξαρτήσεων Python

**Επεξεργαστείτε το `pyproject.toml`:** ενημερώστε το [./code/weather_mcp/pyproject.toml](../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/pyproject.toml)

#### 4β. Ενημέρωση Ρυθμίσεων Inspector

**Επεξεργαστείτε το `inspector/package.json`:** ενημερώστε το [./code/weather_mcp/inspector/package.json](../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/inspector/package.json)

#### 4γ. Ενημέρωση Εξαρτήσεων Inspector

**Επεξεργαστείτε το `inspector/package-lock.json`:** ενημερώστε το [./code/weather_mcp/inspector/package-lock.json](../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/inspector/package-lock.json)

> **📝 Σημείωση:** Αυτό το αρχείο περιέχει εκτενείς ορισμούς εξαρτήσεων. Παρακάτω φαίνεται η βασική δομή - το πλήρες περιεχόμενο εξασφαλίζει σωστή επίλυση εξαρτήσεων.

> **⚡ Πλήρες Package Lock:** Το πλήρες package-lock.json περιέχει περίπου 3000 γραμμές ορισμών εξαρτήσεων. Το παραπάνω δείχνει τη βασική δομή - χρησιμοποιήστε το παρεχόμενο αρχείο για πλήρη επίλυση.

### Βήμα 5: Ρύθμιση Αποσφαλμάτωσης στο VS Code

*Σημείωση: Αντιγράψτε το αρχείο στη συγκεκριμένη διαδρομή για να αντικαταστήσετε το αντίστοιχο τοπικό αρχείο*

#### 5α. Ενημέρωση Ρυθμίσεων Εκκίνησης

**Επεξεργαστείτε το `.vscode/launch.json`:**

```json
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "Attach to Local MCP",
      "type": "debugpy",
      "request": "attach",
      "connect": {
        "host": "localhost",
        "port": 5678
      },
      "presentation": {
        "hidden": true
      },
      "internalConsoleOptions": "neverOpen",
      "postDebugTask": "Terminate All Tasks"
    },
    {
      "name": "Launch Inspector (Edge)",
      "type": "msedge",
      "request": "launch",
      "url": "http://localhost:6274?timeout=60000&serverUrl=http://localhost:3001/sse#tools",
      "cascadeTerminateToConfigurations": [
        "Attach to Local MCP"
      ],
      "presentation": {
        "hidden": true
      },
      "internalConsoleOptions": "neverOpen"
    },
    {
      "name": "Launch Inspector (Chrome)",
      "type": "chrome",
      "request": "launch",
      "url": "http://localhost:6274?timeout=60000&serverUrl=http://localhost:3001/sse#tools",
      "cascadeTerminateToConfigurations": [
        "Attach to Local MCP"
      ],
      "presentation": {
        "hidden": true
      },
      "internalConsoleOptions": "neverOpen"
    }
  ],
  "compounds": [
    {
      "name": "Debug in Agent Builder",
      "configurations": [
        "Attach to Local MCP"
      ],
      "preLaunchTask": "Open Agent Builder",
    },
    {
      "name": "Debug in Inspector (Edge)",
      "configurations": [
        "Launch Inspector (Edge)",
        "Attach to Local MCP"
      ],
      "preLaunchTask": "Start MCP Inspector",
      "stopAll": true
    },
    {
      "name": "Debug in Inspector (Chrome)",
      "configurations": [
        "Launch Inspector (Chrome)",
        "Attach to Local MCP"
      ],
      "preLaunchTask": "Start MCP Inspector",
      "stopAll": true
    }
  ]
}
```

**Επεξεργαστείτε το `.vscode/tasks.json`:**

```
{
  "version": "2.0.0",
  "tasks": [
    {
      "label": "Start MCP Server",
      "type": "shell",
      "command": "python -m debugpy --listen 127.0.0.1:5678 src/__init__.py sse",
      "isBackground": true,
      "options": {
        "cwd": "${workspaceFolder}",
        "env": {
          "PORT": "3001"
        }
      },
      "problemMatcher": {
        "pattern": [
          {
            "regexp": "^.*$",
            "file": 0,
            "location": 1,
            "message": 2
          }
        ],
        "background": {
          "activeOnStart": true,
          "beginsPattern": ".*",
          "endsPattern": "Application startup complete|running"
        }
      }
    },
    {
      "label": "Start MCP Inspector",
      "type": "shell",
      "command": "npm run dev:inspector",
      "isBackground": true,
      "options": {
        "cwd": "${workspaceFolder}/inspector",
        "env": {
          "CLIENT_PORT": "6274",
          "SERVER_PORT": "6277",
        }
      },
      "problemMatcher": {
        "pattern": [
          {
            "regexp": "^.*$",
            "file": 0,
            "location": 1,
            "message": 2
          }
        ],
        "background": {
          "activeOnStart": true,
          "beginsPattern": "Starting MCP inspector",
          "endsPattern": "Proxy server listening on port"
        }
      },
      "dependsOn": [
        "Start MCP Server"
      ]
    },
    {
      "label": "Open Agent Builder",
      "type": "shell",
      "command": "echo ${input:openAgentBuilder}",
      "presentation": {
        "reveal": "never"
      },
      "dependsOn": [
        "Start MCP Server"
      ],
    },
    {
      "label": "Terminate All Tasks",
      "command": "echo ${input:terminate}",
      "type": "shell",
      "problemMatcher": []
    }
  ],
  "inputs": [
    {
      "id": "openAgentBuilder",
      "type": "command",
      "command": "ai-mlstudio.agentBuilder",
      "args": {
        "initialMCPs": [ "local-server-weather_mcp" ],
        "triggeredFrom": "vsc-tasks"
      }
    },
    {
      "id": "terminate",
      "type": "command",
      "command": "workbench.action.tasks.terminate",
      "args": "terminateAll"
    }
  ]
}
```

---

## 🚀 Εκτέλεση και Δοκιμή του MCP Server σας

### Βήμα 6: Εγκατάσταση Εξαρτήσεων

Μετά τις αλλαγές στη ρύθμιση, εκτελέστε τις παρακάτω εντολές:

**Εγκατάσταση εξαρτήσεων Python:**
```bash
uv sync
```

**Εγκατάσταση εξαρτήσεων Inspector:**
```bash
cd inspector
npm install
```

### Βήμα 7: Αποσφαλμάτωση με Agent Builder

1. **Πατήστε F5** ή χρησιμοποιήστε τη ρύθμιση **"Debug in Agent Builder"**
2. **Επιλέξτε τη σύνθετη ρύθμιση** από τον πίνακα αποσφαλμάτωσης
3. **Περιμένετε να ξεκινήσει ο server** και να ανοίξει το Agent Builder
4. **Δοκιμάστε τον weather MCP server** με ερωτήματα σε φυσική γλώσσα

Δώστε είσοδο όπως η παρακάτω

SYSTEM_PROMPT

```
You are my weather assistant
```

USER_PROMPT

```
How's the weather like in Seattle
```

![Agent Builder Debug Result](../../../../translated_images/el/Result.6ac570f7d2b1d5389c561ab0566970fe0f13e75bdd976b6a7f0270bc715d07f8.png)

### Βήμα 8: Αποσφαλμάτωση με MCP Inspector

1. **Χρησιμοποιήστε τη ρύθμιση "Debug in Inspector"** (Edge ή Chrome)
2. **Ανοίξτε το περιβάλλον Inspector** στη διεύθυνση `http://localhost:6274`
3. **Εξερευνήστε το διαδραστικό περιβάλλον δοκιμών:**
   - Δείτε τα διαθέσιμα εργαλεία
   - Δοκιμάστε την εκτέλεση εργαλείων
   - Παρακολουθήστε αιτήματα δικτύου
   - Αποσφαλματώστε τις απαντήσεις του server

![MCP Inspector Interface](../../../../translated_images/el/Inspector.5672415cd02fe8731774586cc0a1083e3275d2f8491602aecc8ac4d61f2c0d57.png)

---

## 🎯 Κύρια Αποτελέσματα Μάθησης

Ολοκληρώνοντας αυτό το εργαστήριο, έχετε:

- [x] **Δημιουργήσει προσαρμοσμένο MCP server** χρησιμοποιώντας πρότυπα AI Toolkit
- [x] **Αναβαθμίσει στο πιο πρόσφατο MCP SDK** (v1.9.3) για βελτιωμένη λειτουργικότητα
- [x] **Ρυθμίσει επαγγελματικές ροές εργασίας αποσφαλμάτωσης** για Agent Builder και Inspector
- [x] **Εγκαταστήσει το MCP Inspector** για διαδραστικές δοκιμές server
- [x] **Κατακτήσει τις ρυθμίσεις αποσφαλμάτωσης στο VS Code** για ανάπτυξη MCP

## 🔧 Προχωρημένα Χαρακτηριστικά που Εξερευνήθηκαν

| Χαρακτηριστικό | Περιγραφή | Περίπτωση Χρήσης |
|----------------|-----------|------------------|
| **MCP Python SDK v1.9.3** | Τελευταία υλοποίηση πρωτοκόλλου | Σύγχρονη ανάπτυξη server |
| **MCP Inspector 0.14.0** | Διαδραστικό εργαλείο αποσφαλμάτωσης | Δοκιμές server σε πραγματικό χρόνο |
| **VS Code Debugging** | Ενσωματωμένο περιβάλλον ανάπτυξης | Επαγγελματική ροή αποσφαλμάτωσης |
| **Agent Builder Integration** | Άμεση σύνδεση με AI Toolkit | Ολοκληρωμένες δοκιμές agent |

## 📚 Επιπλέον Πόροι

- [MCP Python SDK Documentation](https://modelcontextprotocol.io/docs/sdk/python)
- [AI Toolkit Extension Guide](https://code.visualstudio.com/docs/ai/ai-toolkit)
- [VS Code Debugging Documentation](https://code.visualstudio.com/docs/editor/debugging)
- [Model Context Protocol Specification](https://modelcontextprotocol.io/docs/concepts/architecture)

---

**🎉 Συγχαρητήρια!** Ολοκληρώσατε με επιτυχία το Εργαστήριο 3 και πλέον μπορείτε να δημιουργείτε, να αποσφαλματώνετε και να αναπτύσσετε προσαρμοσμένους MCP servers χρησιμοποιώντας επαγγελματικές ροές εργασίας ανάπτυξης.

### 🔜 Συνεχίστε στην Επόμενη Ενότητα

Έτοιμοι να εφαρμόσετε τις δεξιότητές σας MCP σε πραγματικές ροές εργασίας ανάπτυξης; Συνεχίστε στο **[Ενότητα 4: Πρακτική Ανάπτυξη MCP - Προσαρμοσμένος GitHub Clone Server](../lab4/README.md)** όπου θα:
- Δημιουργήσετε έναν MCP server έτοιμο για παραγωγή που αυτοματοποιεί λειτουργίες αποθετηρίου GitHub
- Υλοποιήσετε λειτουργία κλωνοποίησης αποθετηρίου GitHub μέσω MCP
- Ενσωματώσετε προσαρμοσμένους MCP servers με VS Code και GitHub Copilot Agent Mode
- Δοκιμάσετε και αναπτύξετε προσαρμοσμένους MCP servers σε περιβάλλοντα παραγωγής
- Μάθετε πρακτική αυτοματοποίηση ροών εργασίας για προγραμματιστές

**Αποποίηση ευθυνών**:  
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας την υπηρεσία αυτόματης μετάφρασης AI [Co-op Translator](https://github.com/Azure/co-op-translator). Παρόλο που επιδιώκουμε την ακρίβεια, παρακαλούμε να έχετε υπόψη ότι οι αυτόματες μεταφράσεις ενδέχεται να περιέχουν λάθη ή ανακρίβειες. Το πρωτότυπο έγγραφο στη γλώσσα του θεωρείται η αυθεντική πηγή. Για κρίσιμες πληροφορίες, συνιστάται επαγγελματική ανθρώπινη μετάφραση. Δεν φέρουμε ευθύνη για τυχόν παρεξηγήσεις ή λανθασμένες ερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.