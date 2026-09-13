# Διακομιστής MCP με μεταφορά stdio

> **⚠️ Σημαντική Ενημέρωση**: Από την Προδιαγραφή MCP 2025-06-18, η ανεξάρτητη μεταφορά SSE (Server-Sent Events) έχει **καταργηθεί** και έχει αντικατασταθεί από τη μεταφορά "Streamable HTTP". Η τρέχουσα προδιαγραφή MCP ορίζει δύο κύριους μηχανισμούς μεταφοράς:
> 1. **stdio** - Τυπική είσοδος/έξοδος (συνιστάται για τοπικούς διακομιστές)
> 2. **Streamable HTTP** - Για απομακρυσμένους διακομιστές που μπορεί να χρησιμοποιούν το SSE εσωτερικά
>
> Αυτό το μάθημα έχει ενημερωθεί για να επικεντρωθεί στη **μεταφορά stdio**, η οποία είναι η συνιστώμενη προσέγγιση για τις περισσότερες υλοποιήσεις διακομιστών MCP.

Η μεταφορά stdio επιτρέπει στους διακομιστές MCP να επικοινωνούν με τους πελάτες μέσω των ροών τυπικής εισόδου και εξόδου. Πρόκειται για τον πιο συχνά χρησιμοποιούμενο και συνιστώμενο μηχανισμό μεταφοράς στην τρέχουσα προδιαγραφή MCP, προσφέροντας έναν απλό και αποδοτικό τρόπο να δημιουργηθούν διακομιστές MCP που μπορούν εύκολα να ενσωματωθούν με διάφορες εφαρμογές πελατών.

## Επισκόπηση

Αυτό το μάθημα καλύπτει πώς να δημιουργήσετε και να χρησιμοποιήσετε διακομιστές MCP χρησιμοποιώντας τη μεταφορά stdio.

## Στόχοι Μάθησης

Μέχρι το τέλος αυτού του μαθήματος, θα μπορείτε να:

- Δημιουργήσετε έναν διακομιστή MCP χρησιμοποιώντας τη μεταφορά stdio.
- Εντοπίζετε σφάλματα σε έναν διακομιστή MCP χρησιμοποιώντας τον Inspector.
- Χρησιμοποιείτε έναν διακομιστή MCP μέσω του Visual Studio Code.
- Κατανοήσετε τους τρέχοντες μηχανισμούς μεταφοράς MCP και γιατί συνιστάται η stdio.


## Μεταφορά stdio - Πώς λειτουργεί

Η μεταφορά stdio είναι μία από τις δύο πρότυπες μεταφορές στην Προδιαγραφή MCP
`2026-07-28`. Δείτε πώς λειτουργεί:

- **Απλή Επικοινωνία**: Ο διακομιστής διαβάζει μηνύματα JSON-RPC από την τυπική είσοδο (`stdin`) και στέλνει μηνύματα στην τυπική έξοδο (`stdout`).
- **Βασισμένη σε διεργασία**: Ο πελάτης ξεκινάει τον διακομιστή MCP ως υποδιεργασία.
- **Μορφή Μηνύματος**: Τα μηνύματα είναι μεμονωμένα αιτήματα, ειδοποιήσεις ή απαντήσεις JSON-RPC, διαχωρισμένα με αλλαγές γραμμής.
- **Καταγραφή**: Ο διακομιστής ΜΠΟΡΕΙ να γράφει συμβολοσειρές UTF-8 στο τυπικό σφάλμα (`stderr`) για σκοπούς καταγραφής.

### Βασικές Απαιτήσεις:
- Τα μηνύματα ΠΡΕΠΕΙ να διαχωρίζονται με αλλαγές γραμμής και ΔΕΝ ΠΡΕΠΕΙ να περιέχουν ενσωματωμένες αλλαγές γραμμής
- Ο διακομιστής ΔΕΝ ΠΡΕΠΕΙ να γράφει οτιδήποτε στο `stdout` που δεν είναι έγκυρο μήνυμα MCP
- Ο πελάτης ΔΕΝ ΠΡΕΠΕΙ να γράφει οτιδήποτε στο `stdin` του διακομιστή που δεν είναι έγκυρο μήνυμα MCP

### TypeScript

```typescript
import { Server } from "@modelcontextprotocol/sdk/server/index.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";

const server = new Server(
  {
    name: "example-server",
    version: "1.0.0",
  },
  {
    capabilities: {
      tools: {},
    },
  }
);

async function runServer() {
  const transport = new StdioServerTransport();
  await server.connect(transport);
}

runServer().catch(console.error);
```

Στον προηγούμενο κώδικα:

- Εισάγουμε την κλάση `Server` και το `StdioServerTransport` από το MCP SDK
- Δημιουργούμε ένα στιγμιότυπο διακομιστή με βασική διαμόρφωση και δυνατότητες
- Δημιουργούμε ένα στιγμιότυπο `StdioServerTransport` και συνδέουμε τον διακομιστή σε αυτό, ενεργοποιώντας την επικοινωνία μέσω stdin/stdout

### Python

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server

# Δημιουργία παρουσίας διακομιστή
server = Server("example-server")

@server.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

async def main():
    async with stdio_server(server) as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            server.create_initialization_options()
        )

if __name__ == "__main__":
    asyncio.run(main())
```

Στον προηγούμενο κώδικα:

- Δημιουργούμε ένα στιγμιότυπο διακομιστή χρησιμοποιώντας το MCP SDK
- Ορίζουμε εργαλεία χρησιμοποιώντας διακοσμητές
- Χρησιμοποιούμε τον context manager stdio_server για τη διαχείριση της μεταφοράς

### .NET

```csharp
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;
using Microsoft.Extensions.Logging;
using ModelContextProtocol.Server;

var builder = Host.CreateApplicationBuilder(args);

builder.Services
    .AddMcpServer()
    .WithStdioServerTransport()
    .WithTools<Tools>();

builder.Services.AddLogging(logging => logging.AddConsole());

var app = builder.Build();
await app.RunAsync();
```

Η βασική διαφορά από το SSE είναι ότι οι διακομιστές stdio:

- Δεν απαιτούν ρύθμιση web server ή HTTP endpoints
- Εκκινούνται ως υποδιεργασίες από τον πελάτη
- Επικοινωνούν μέσω των ροών stdin/stdout
- Είναι απλούστεροι στην υλοποίηση και τον εντοπισμό σφαλμάτων

## Άσκηση: Δημιουργία διακομιστή stdio

Για να δημιουργήσουμε τον διακομιστή μας, πρέπει να θυμόμαστε δύο πράγματα:

- Πρέπει να χρησιμοποιήσουμε έναν web server για να εκθέσουμε endpoints για σύνδεση και μηνύματα.
## Εργαστήριο: Δημιουργία απλού MCP διακομιστή stdio

Σε αυτό το εργαστήριο, θα δημιουργήσουμε έναν απλό διακομιστή MCP χρησιμοποιώντας τη συνιστώμενη μεταφορά stdio. Αυτός ο διακομιστής θα εκθέτει εργαλεία που οι πελάτες μπορούν να καλέσουν χρησιμοποιώντας το πρότυπο Model Context Protocol.

### Προαπαιτούμενα

- Python 3.8 ή νεότερη έκδοση
- MCP Python SDK: `pip install mcp`
- Βασική κατανόηση ασύγχρονης προγραμματισμού

Ας ξεκινήσουμε δημιουργώντας τον πρώτο μας διακομιστή MCP stdio:

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp import types

# Διαμόρφωση καταγραφής
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Δημιουργία του διακομιστή
server = Server("example-stdio-server")

@server.tool()
def calculate_sum(a: int, b: int) -> int:
    """Calculate the sum of two numbers"""
    return a + b

@server.tool() 
def get_greeting(name: str) -> str:
    """Generate a personalized greeting"""
    return f"Hello, {name}! Welcome to MCP stdio server."

async def main():
    # Χρησιμοποιήστε μεταφορά stdio
    async with stdio_server(server) as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            server.create_initialization_options()
        )

if __name__ == "__main__":
    asyncio.run(main())
```

## Βασικές διαφορές από την καταργημένη προσέγγιση SSE

**Μεταφορά Stdio (Τρέχον Πρότυπο):**
- Απλό μοντέλο υποδιεργασιών - ο πελάτης εκκινεί τον διακομιστή ως θυγατρική διεργασία
- Επικοινωνία μέσω stdin/stdout χρησιμοποιώντας μηνύματα JSON-RPC
- Δεν απαιτείται ρύθμιση HTTP server
- Καλύτερη απόδοση και ασφάλεια
- Ευκολότερος εντοπισμός σφαλμάτων και ανάπτυξη

**Μεταφορά SSE (Καταργημένη από MCP 2025-06-18):**
- Απαιτεί HTTP server με SSE endpoints
- Πιο περίπλοκη ρύθμιση με υποδομή web server
- Επιπρόσθετα θέματα ασφάλειας για HTTP endpoints
- Τώρα αντικαταστάθηκε από το Streamable HTTP για σενάρια web

### Δημιουργία διακομιστή με τη μεταφορά stdio

Για να δημιουργήσουμε τον διακομιστή stdio, πρέπει να:

1. **Εισάγουμε τις απαιτούμενες βιβλιοθήκες** - Απαιτούνται συστατικά διακομιστή MCP και μεταφορά stdio
2. **Δημιουργήσουμε ένα στιγμιότυπο διακομιστή** - Ορίζουμε τον διακομιστή με τις δυνατότητές του
3. **Ορίζουμε εργαλεία** - Προσθέτουμε τις λειτουργίες που θέλουμε να εκθέσουμε
4. **Ρυθμίζουμε τη μεταφορά** - Διαμορφώνουμε την επικοινωνία stdio
5. **Τρέχουμε τον διακομιστή** - Εκκινούμε τον διακομιστή και διαχειριζόμαστε τα μηνύματα

Ας το δημιουργήσουμε βήμα βήμα:

### Βήμα 1: Δημιουργία βασικού διακομιστή stdio

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server

# Διαμορφώστε την καταγραφή
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Δημιουργήστε τον διακομιστή
server = Server("example-stdio-server")

@server.tool()
def get_greeting(name: str) -> str:
    """Generate a personalized greeting"""
    return f"Hello, {name}! Welcome to MCP stdio server."

async def main():
    async with stdio_server(server) as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            server.create_initialization_options()
        )

if __name__ == "__main__":
    asyncio.run(main())
```

### Βήμα 2: Προσθήκη περισσότερων εργαλείων

```python
@server.tool()
def calculate_sum(a: int, b: int) -> int:
    """Calculate the sum of two numbers"""
    return a + b

@server.tool()
def calculate_product(a: int, b: int) -> int:
    """Calculate the product of two numbers"""
    return a * b

@server.tool()
def get_server_info() -> dict:
    """Get information about this MCP server"""
    return {
        "server_name": "example-stdio-server",
        "version": "1.0.0",
        "transport": "stdio",
        "capabilities": ["tools"]
    }
```

### Βήμα 3: Εκτέλεση του διακομιστή

Αποθηκεύστε τον κώδικα ως `server.py` και τρέξτε τον από τη γραμμή εντολών:

```bash
python server.py
```

Ο διακομιστής θα ξεκινήσει και θα περιμένει είσοδο από το stdin. Επικοινωνεί χρησιμοποιώντας μηνύματα JSON-RPC μέσω της μεταφοράς stdio.

### Βήμα 4: Δοκιμή με τον Inspector

Μπορείτε να δοκιμάσετε τον διακομιστή σας χρησιμοποιώντας τον MCP Inspector:

1. Εγκαταστήστε τον Inspector: `npx @modelcontextprotocol/inspector`
2. Τρέξτε τον Inspector και κατευθύνετέ τον στον διακομιστή σας
3. Δοκιμάστε τα εργαλεία που δημιουργήσατε

### .NET

```csharp
var builder = WebApplication.CreateBuilder(args);
builder.Services
    .AddMcpServer();
 ```
## Εντοπισμός σφαλμάτων στον διακομιστή stdio

### Χρήση του MCP Inspector

Ο MCP Inspector είναι ένα πολύτιμο εργαλείο για εντοπισμό σφαλμάτων και δοκιμές διακομιστών MCP. Δείτε πώς να το χρησιμοποιήσετε με τον διακομιστή stdio σας:

1. **Εγκαταστήστε τον Inspector**:
   ```bash
   npx @modelcontextprotocol/inspector
   ```

2. **Τρέξτε τον Inspector**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

3. **Δοκιμάστε τον διακομιστή σας**: Ο Inspector παρέχει μια διεπαφή web όπου μπορείτε να:
   - Δείτε τις δυνατότητες του διακομιστή
   - Δοκιμάσετε εργαλεία με διαφορετικές παραμέτρους
   - Παρακολουθήσετε τα μηνύματα JSON-RPC
   - Εντοπίσετε προβλήματα σύνδεσης

### Χρήση του VS Code

Μπορείτε επίσης να εντοπίσετε σφάλματα στον διακομιστή MCP απευθείας στο VS Code:

1. Δημιουργήστε μια ρύθμιση εκκίνησης στο `.vscode/launch.json`:
   ```json
   {
     "version": "0.2.0",
     "configurations": [
       {
         "name": "Debug MCP Server",
         "type": "python",
         "request": "launch",
         "program": "server.py",
         "console": "integratedTerminal"
       }
     ]
   }
   ```

2. Ορίστε σημεία διακοπής στον κώδικα του διακομιστή
3. Τρέξτε τον εντοπιστή σφαλμάτων και δοκιμάστε με τον Inspector

### Συνηθισμένες συμβουλές εντοπισμού σφαλμάτων

- Χρησιμοποιήστε το `stderr` για καταγραφή - μην γράφετε ποτέ στο `stdout` καθώς είναι προορισμένο για μηνύματα MCP
- Βεβαιωθείτε ότι όλα τα μηνύματα JSON-RPC διαχωρίζονται με αλλαγές γραμμής
- Δοκιμάστε πρώτα με απλά εργαλεία πριν προσθέσετε πιο σύνθετη λειτουργικότητα
- Χρησιμοποιήστε τον Inspector για να επαληθεύσετε τη μορφή των μηνυμάτων

## Χρήση του διακομιστή stdio σας στο VS Code

Μόλις δημιουργήσετε τον διακομιστή MCP stdio, μπορείτε να τον ενσωματώσετε με το VS Code για να τον χρησιμοποιήσετε με τον Claude ή άλλους πελάτες συμβατούς με MCP.

### Διαμόρφωση

1. **Δημιουργήστε ένα αρχείο διαμόρφωσης MCP** στο `%APPDATA%\Claude\claude_desktop_config.json` (Windows) ή `~/Library/Application Support/Claude/claude_desktop_config.json` (Mac):

   ```json
   {
     "mcpServers": {
       "example-stdio-server": {
         "command": "python",
         "args": ["path/to/your/server.py"]
       }
     }
   }
   ```

2. **Ξεκινήστε ξανά τον Claude**: Κλείστε και ανοίξτε ξανά τον Claude για να φορτώσει τη νέα διαμόρφωση διακομιστή.

3. **Δοκιμάστε τη σύνδεση**: Ξεκινήστε μια συνομιλία με τον Claude και δοκιμάστε να χρησιμοποιήσετε τα εργαλεία του διακομιστή σας:
   - "Μπορείς να με χαιρετήσεις χρησιμοποιώντας το εργαλείο χαιρετισμού;"
   - "Υπολόγισε το άθροισμα του 15 και του 27"
   - "Ποια είναι η πληροφορία για τον διακομιστή;"

### Παράδειγμα διακομιστή stdio TypeScript

Εδώ είναι ένα πλήρες παράδειγμα TypeScript για αναφορά:

```typescript
#!/usr/bin/env node
import { Server } from "@modelcontextprotocol/sdk/server/index.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { CallToolRequestSchema, ListToolsRequestSchema } from "@modelcontextprotocol/sdk/types.js";

const server = new Server(
  {
    name: "example-stdio-server",
    version: "1.0.0",
  },
  {
    capabilities: {
      tools: {},
    },
  }
);

// Προσθέστε εργαλεία
server.setRequestHandler(ListToolsRequestSchema, async () => {
  return {
    tools: [
      {
        name: "get_greeting",
        description: "Get a personalized greeting",
        inputSchema: {
          type: "object",
          properties: {
            name: {
              type: "string",
              description: "Name of the person to greet",
            },
          },
          required: ["name"],
        },
      },
    ],
  };
});

server.setRequestHandler(CallToolRequestSchema, async (request) => {
  if (request.params.name === "get_greeting") {
    return {
      content: [
        {
          type: "text",
          text: `Hello, ${request.params.arguments?.name}! Welcome to MCP stdio server.`,
        },
      ],
    };
  } else {
    throw new Error(`Unknown tool: ${request.params.name}`);
  }
});

async function runServer() {
  const transport = new StdioServerTransport();
  await server.connect(transport);
}

runServer().catch(console.error);
```

### Παράδειγμα διακομιστή stdio .NET

```csharp
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;
using Microsoft.Extensions.Logging;
using ModelContextProtocol.Server;
using System.ComponentModel;

var builder = Host.CreateApplicationBuilder(args);

builder.Services
    .AddMcpServer()
    .WithStdioServerTransport()
    .WithTools<Tools>();

var app = builder.Build();
await app.RunAsync();

[McpServerToolType]
public class Tools
{
    [McpServerTool, Description("Get a personalized greeting")]
    public string GetGreeting(string name)
    {
        return $"Hello, {name}! Welcome to MCP stdio server.";
    }

    [McpServerTool, Description("Calculate the sum of two numbers")]
    public int CalculateSum(int a, int b)
    {
        return a + b;
    }
}
```

## Περίληψη

Σε αυτό το ενημερωμένο μάθημα, μάθατε πώς να:

- Δημιουργείτε διακομιστές MCP χρησιμοποιώντας τη τρέχουσα **μεταφορά stdio** (συνιστώμενη προσέγγιση)
- Κατανοείτε γιατί η μεταφορά SSE καταργήθηκε υπέρ της stdio και του Streamable HTTP
- Δημιουργείτε εργαλεία που μπορούν να κληθούν από πελάτες MCP
- Εντοπίζετε σφάλματα στον διακομιστή σας χρησιμοποιώντας τον MCP Inspector
- Ενσωματώνετε τον διακομιστή stdio σας με το VS Code και τον Claude

Η μεταφορά stdio παρέχει έναν απλούστερο, πιο ασφαλή και αποδοτικό τρόπο δημιουργίας διακομιστών MCP σε σύγκριση με την καταργημένη προσέγγιση SSE. Είναι η συνιστώμενη μεταφορά για τις περισσότερες υλοποιήσεις διακομιστών MCP από την προδιαγραφή 2025-06-18.


### .NET

1. Ας δημιουργήσουμε πρώτα κάποια εργαλεία, για αυτό θα δημιουργήσουμε ένα αρχείο *Tools.cs* με το ακόλουθο περιεχόμενο:

  ```csharp
  using System.ComponentModel;
  using System.Text.Json;
  using ModelContextProtocol.Server;
  ```

## Άσκηση: Δοκιμή του διακομιστή stdio σας

Τώρα που έχετε δημιουργήσει τον διακομιστή stdio, ας τον δοκιμάσουμε για να βεβαιωθούμε ότι λειτουργεί σωστά.

### Προαπαιτούμενα

1. Βεβαιωθείτε ότι έχετε εγκαταστήσει τον MCP Inspector:
   ```bash
   npm install -g @modelcontextprotocol/inspector
   ```

2. Ο κώδικας του διακομιστή σας πρέπει να είναι αποθηκευμένος (π.χ., ως `server.py`)

### Δοκιμές με τον Inspector

1. **Ξεκινήστε τον Inspector με τον διακομιστή σας**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

2. **Ανοίξτε τη διεπαφή web**: Ο Inspector θα ανοίξει ένα παράθυρο προγράμματος περιήγησης που δείχνει τις δυνατότητες του διακομιστή σας.

3. **Δοκιμάστε τα εργαλεία**: 
   - Δοκιμάστε το εργαλείο `get_greeting` με διαφορετικά ονόματα
   - Δοκιμάστε το εργαλείο `calculate_sum` με διάφορους αριθμούς
   - Καλέστε το εργαλείο `get_server_info` για να δείτε μεταδεδομένα του διακομιστή

4. **Παρακολουθήστε την επικοινωνία**: Ο Inspector εμφανίζει τα μηνύματα JSON-RPC που ανταλλάσσονται ανάμεσα στον πελάτη και τον διακομιστή.

### Τι θα πρέπει να δείτε

Όταν ο διακομιστής σας ξεκινήσει σωστά, θα δείτε:
- Δυνατότητες διακομιστή καταγεγραμμένες στον Inspector
- Εργαλεία διαθέσιμα για δοκιμή
- Επιτυχείς ανταλλαγές μηνυμάτων JSON-RPC
- Απαντήσεις εργαλείων εμφανιζόμενες στη διεπαφή

### Συνηθισμένα προβλήματα και λύσεις

**Ο διακομιστής δεν ξεκινά:**
- Ελέγξτε ότι όλες οι εξαρτήσεις είναι εγκατεστημένες: `pip install mcp`
- Επαληθεύστε τη σύνταξη και την εσοχή Python
- Ελέγξτε για μηνύματα σφάλματος στην κονσόλα

**Δεν εμφανίζονται εργαλεία:**
- Βεβαιωθείτε ότι υπάρχουν διακοσμητές `@server.tool()`
- Ελέγξτε ότι οι συναρτήσεις εργαλείων ορίζονται πριν από το `main()`
- Επαληθεύστε ότι ο διακομιστής είναι σωστά διαμορφωμένος

**Προβλήματα σύνδεσης:**
- Βεβαιωθείτε ότι ο διακομιστής χρησιμοποιεί σωστά τη μεταφορά stdio
- Ελέγξτε ότι δεν επεμβαίνουν άλλες διαδικασίες
- Επαληθεύστε τη σύνταξη εντολών του Inspector

## Ανάθεση

Προσπαθήστε να επεκτείνετε τον διακομιστή σας με περισσότερες δυνατότητες. Δείτε [αυτή τη σελίδα](https://api.chucknorris.io/) για παράδειγμα, για να προσθέσετε ένα εργαλείο που καλεί ένα API. Εσείς αποφασίζετε πώς πρέπει να είναι ο διακομιστής. Καλή διασκέδαση :)
## Λύση

[Λύση](./solution/README.md) Εδώ είναι μια πιθανή λύση με λειτουργικό κώδικα.

## Κύρια Σημεία

Τα βασικά σημεία από αυτό το κεφάλαιο είναι τα εξής:

- Η μεταφορά stdio είναι ο συνιστώμενος μηχανισμός για τοπικούς διακομιστές MCP.
- Η μεταφορά stdio επιτρέπει άμεση επικοινωνία μεταξύ διακομιστών MCP και πελατών χρησιμοποιώντας τις τυπικές ροές εισόδου και εξόδου.
- Μπορείτε να χρησιμοποιήσετε τόσο τον Inspector όσο και το Visual Studio Code για να χρησιμοποιήσετε διακομιστές stdio απευθείας, καθιστώντας τον εντοπισμό σφαλμάτων και την ενσωμάτωση απλή.

## Παραδείγματα 

- [Java Calculator](../samples/java/calculator/README.md)
- [.Net Calculator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Calculator](../samples/javascript/README.md)
- [TypeScript Calculator](../samples/typescript/README.md)
- [Python Calculator](../../../../03-GettingStarted/samples/python) 

## Επιπρόσθετοι Πόροι

- [SSE](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events)

## Τι Ακολουθεί

## Επόμενα Βήματα

Τώρα που μάθατε πώς να δημιουργείτε διακομιστές MCP με τη μεταφορά stdio, μπορείτε να εξερευνήσετε πιο προχωρημένα θέματα:

- **Επόμενο**: [HTTP Streaming με MCP (Streamable HTTP)](../06-http-streaming/README.md) - Μάθετε για τον άλλο υποστηριζόμενο μηχανισμό μεταφοράς για απομακρυσμένους διακομιστές
- **Προχωρημένο**: [Καλές Πρακτικές Ασφάλειας MCP](../../02-Security/README.md) - Εφαρμογή ασφάλειας στους διακομιστές MCP σας
- **Παραγωγή**: [Στρατηγικές Ανάπτυξης](../09-deployment/README.md) - Ανάπτυξη των διακομιστών σας για παραγωγική χρήση

## Επιπρόσθετοι Πόροι

- [Προδιαγραφή MCP 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/) - Τρέχουσα προδιαγραφή
- [Τεκμηρίωση MCP SDK](https://github.com/modelcontextprotocol/sdk) - Αναφορές SDK για όλες τις γλώσσες
- [Παραδείγματα Κοινότητας](../../06-CommunityContributions/README.md) - Περισσότερα παραδείγματα διακομιστών από την κοινότητα

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Αποποίηση ευθυνών**:
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας την υπηρεσία μετάφρασης με τεχνητή νοημοσύνη [Co-op Translator](https://github.com/Azure/co-op-translator). Ενώ επιδιώκουμε την ακρίβεια, παρακαλούμε να έχετε υπόψη ότι οι αυτοματοποιημένες μεταφράσεις ενδέχεται να περιέχουν λάθη ή ανακρίβειες. Το πρωτότυπο έγγραφο στη μητρική του γλώσσα πρέπει να θεωρείται η αυθεντική πηγή. Για κρίσιμες πληροφορίες, συνιστάται επαγγελματική ανθρώπινη μετάφραση. Δεν φέρουμε ευθύνη για τυχόν παρεξηγήσεις ή λανθασμένες ερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->