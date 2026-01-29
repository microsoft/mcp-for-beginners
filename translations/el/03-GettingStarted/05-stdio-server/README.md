# MCP Server με μεταφορά stdio

> **⚠️ Σημαντική Ενημέρωση**: Από την MCP Προδιαγραφή 2025-06-18, η ανεξάρτητη μεταφορά SSE (Server-Sent Events) έχει **καταργηθεί** και αντικατασταθεί από τη μεταφορά "Streamable HTTP". Η τρέχουσα προδιαγραφή MCP ορίζει δύο κύριους μηχανισμούς μεταφοράς:
> 1. **stdio** - Τυπική είσοδος/έξοδος (συνιστάται για τοπικούς διακομιστές)
> 2. **Streamable HTTP** - Για απομακρυσμένους διακομιστές που μπορεί να χρησιμοποιούν SSE εσωτερικά
>
> Αυτό το μάθημα έχει ενημερωθεί ώστε να επικεντρώνεται στη μεταφορά **stdio**, η οποία είναι η συνιστώμενη προσέγγιση για τις περισσότερες υλοποιήσεις διακομιστών MCP.

Η μεταφορά stdio επιτρέπει στους διακομιστές MCP να επικοινωνούν με τους πελάτες μέσω των τυπικών ροών εισόδου και εξόδου. Αυτός είναι ο πιο συχνά χρησιμοποιούμενος και συνιστώμενος μηχανισμός μεταφοράς στην τρέχουσα προδιαγραφή MCP, παρέχοντας έναν απλό και αποδοτικό τρόπο για τη δημιουργία διακομιστών MCP που μπορούν εύκολα να ενσωματωθούν σε διάφορες εφαρμογές πελατών.

## Επισκόπηση

Αυτό το μάθημα καλύπτει πώς να δημιουργήσετε και να χρησιμοποιήσετε διακομιστές MCP χρησιμοποιώντας τη μεταφορά stdio.

## Στόχοι Μάθησης

Μέχρι το τέλος αυτού του μαθήματος, θα μπορείτε να:

- Δημιουργήσετε έναν διακομιστή MCP χρησιμοποιώντας τη μεταφορά stdio.
- Εντοπίσετε σφάλματα σε έναν διακομιστή MCP χρησιμοποιώντας το Inspector.
- Χρησιμοποιήσετε έναν διακομιστή MCP μέσω του Visual Studio Code.
- Κατανοήσετε τους τρέχοντες μηχανισμούς μεταφοράς MCP και γιατί συνιστάται η stdio.

## Μεταφορά stdio - Πώς λειτουργεί

Η μεταφορά stdio είναι ένας από τους δύο υποστηριζόμενους τύπους μεταφοράς στην τρέχουσα προδιαγραφή MCP (2025-06-18). Δείτε πώς λειτουργεί:

- **Απλή Επικοινωνία**: Ο διακομιστής διαβάζει μηνύματα JSON-RPC από την τυπική είσοδο (`stdin`) και στέλνει μηνύματα στην τυπική έξοδο (`stdout`).
- **Βασισμένο σε διεργασίες**: Ο πελάτης εκκινεί τον διακομιστή MCP ως υποδιεργασία.
- **Μορφή Μηνυμάτων**: Τα μηνύματα είναι μεμονωμένα αιτήματα, ειδοποιήσεις ή απαντήσεις JSON-RPC, διαχωρισμένα με αλλαγές γραμμής.
- **Καταγραφή**: Ο διακομιστής ΜΠΟΡΕΙ να γράφει UTF-8 συμβολοσειρές στην τυπική έξοδο σφαλμάτων (`stderr`) για σκοπούς καταγραφής.

### Βασικές Απαιτήσεις:
- Τα μηνύματα ΠΡΕΠΕΙ να διαχωρίζονται με αλλαγές γραμμής και ΔΕΝ ΠΡΕΠΕΙ να περιέχουν ενσωματωμένες αλλαγές γραμμής.
- Ο διακομιστής ΔΕΝ ΠΡΕΠΕΙ να γράφει τίποτα στο `stdout` που δεν είναι έγκυρο μήνυμα MCP.
- Ο πελάτης ΔΕΝ ΠΡΕΠΕΙ να γράφει τίποτα στο `stdin` του διακομιστή που δεν είναι έγκυρο μήνυμα MCP.

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
```

Στον παραπάνω κώδικα:

- Εισάγουμε την κλάση `Server` και τη `StdioServerTransport` από το MCP SDK.
- Δημιουργούμε μια παρουσία διακομιστή με βασική διαμόρφωση και δυνατότητες.

### Python

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server

# Create server instance
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

Στον παραπάνω κώδικα:

- Δημιουργούμε μια παρουσία διακομιστή χρησιμοποιώντας το MCP SDK.
- Ορίζουμε εργαλεία με διακοσμητές.
- Χρησιμοποιούμε τον context manager `stdio_server` για τη διαχείριση της μεταφοράς.

### .NET

```csharp
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;
using Microsoft.Extensions.Logging;
using ModelContextProtocol.Server;

var builder = Host.CreateApplicationBuilder(args);

builder.Services
    .AddMcpServer()
    .WithStdioTransport()
    .WithTools<Tools>();

builder.Services.AddLogging(logging => logging.AddConsole());

var app = builder.Build();
await app.RunAsync();
```

Η βασική διαφορά από το SSE είναι ότι οι διακομιστές stdio:

- Δεν απαιτούν ρύθμιση διακομιστή ιστού ή HTTP endpoints.
- Εκκινούνται ως υποδιεργασίες από τον πελάτη.
- Επικοινωνούν μέσω των ροών stdin/stdout.
- Είναι πιο απλοί στην υλοποίηση και τον εντοπισμό σφαλμάτων.

## Άσκηση: Δημιουργία διακομιστή stdio

Για να δημιουργήσουμε τον διακομιστή μας, πρέπει να έχουμε υπόψη μας δύο πράγματα:

- Πρέπει να χρησιμοποιήσουμε έναν διακομιστή ιστού για την έκθεση endpoints για σύνδεση και μηνύματα.

## Εργαστήριο: Δημιουργία απλού διακομιστή MCP stdio

Σε αυτό το εργαστήριο, θα δημιουργήσουμε έναν απλό διακομιστή MCP χρησιμοποιώντας τη συνιστώμενη μεταφορά stdio. Αυτός ο διακομιστής θα εκθέτει εργαλεία που οι πελάτες μπορούν να καλούν χρησιμοποιώντας το πρότυπο Model Context Protocol.

### Προαπαιτούμενα

- Python 3.8 ή νεότερη έκδοση.
- MCP Python SDK: `pip install mcp`.
- Βασική κατανόηση του ασύγχρονου προγραμματισμού.

Ας ξεκινήσουμε δημιουργώντας τον πρώτο μας διακομιστή MCP stdio:

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp import types

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Create the server
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
    # Use stdio transport
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
- Απλό μοντέλο υποδιεργασίας - ο πελάτης εκκινεί τον διακομιστή ως διεργασία παιδί.
- Επικοινωνία μέσω stdin/stdout χρησιμοποιώντας μηνύματα JSON-RPC.
- Δεν απαιτείται ρύθμιση διακομιστή HTTP.
- Καλύτερη απόδοση και ασφάλεια.
- Ευκολότερος εντοπισμός σφαλμάτων και ανάπτυξη.

**Μεταφορά SSE (Καταργήθηκε από MCP 2025-06-18):**
- Απαιτούσε διακομιστή HTTP με endpoints SSE.
- Πιο περίπλοκη ρύθμιση με υποδομή διακομιστή ιστού.
- Πρόσθετες ανησυχίες ασφάλειας για τα HTTP endpoints.
- Τώρα αντικαταστάθηκε από το Streamable HTTP για σενάρια βασισμένα στον ιστό.

### Δημιουργία διακομιστή με μεταφορά stdio

Για να δημιουργήσουμε τον διακομιστή stdio, πρέπει να:

1. **Εισάγουμε τις απαραίτητες βιβλιοθήκες** - Χρειαζόμαστε τα στοιχεία του διακομιστή MCP και τη μεταφορά stdio.
2. **Δημιουργήσουμε μια παρουσία διακομιστή** - Ορίστε τον διακομιστή με τις δυνατότητές του.
3. **Ορίσουμε εργαλεία** - Προσθέστε τη λειτουργικότητα που θέλουμε να εκθέσουμε.
4. **Ρυθμίσουμε τη μεταφορά** - Διαμορφώστε την επικοινωνία stdio.
5. **Εκκινήσουμε τον διακομιστή** - Ξεκινήστε τον διακομιστή και χειριστείτε μηνύματα.

Ας το χτίσουμε βήμα προς βήμα:

### Βήμα 1: Δημιουργία βασικού διακομιστή stdio

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Create the server
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

### Βήμα 3: Εκκίνηση του διακομιστή

Αποθηκεύστε τον κώδικα ως `server.py` και εκτελέστε τον από τη γραμμή εντολών:

```bash
python server.py
```

Ο διακομιστής θα ξεκινήσει και θα περιμένει είσοδο από το stdin. Επικοινωνεί χρησιμοποιώντας μηνύματα JSON-RPC μέσω της μεταφοράς stdio.

### Βήμα 4: Δοκιμή με το Inspector

Μπορείτε να δοκιμάσετε τον διακομιστή σας χρησιμοποιώντας το MCP Inspector:

1. Εγκαταστήστε το Inspector: `npx @modelcontextprotocol/inspector`.
2. Εκτελέστε το Inspector και συνδέστε το στον διακομιστή σας.
3. Δοκιμάστε τα εργαλεία που έχετε δημιουργήσει.

### .NET

```csharp
var builder = WebApplication.CreateBuilder(args);
builder.Services
    .AddMcpServer();
 ```

## Εντοπισμός σφαλμάτων στον διακομιστή stdio

### Χρήση του MCP Inspector

Το MCP Inspector είναι ένα πολύτιμο εργαλείο για τον εντοπισμό σφαλμάτων και τη δοκιμή διακομιστών MCP. Δείτε πώς να το χρησιμοποιήσετε με τον διακομιστή stdio σας:

1. **Εγκατάσταση του Inspector**:
   ```bash
   npx @modelcontextprotocol/inspector
   ```

2. **Εκτέλεση του Inspector**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

3. **Δοκιμή του διακομιστή σας**: Το Inspector παρέχει μια διεπαφή ιστού όπου μπορείτε:
   - Να δείτε τις δυνατότητες του διακομιστή.
   - Να δοκιμάσετε εργαλεία με διαφορετικές παραμέτρους.
   - Να παρακολουθήσετε μηνύματα JSON-RPC.
   - Να εντοπίσετε προβλήματα σύνδεσης.

### Χρήση του VS Code

Μπορείτε επίσης να εντοπίσετε σφάλματα στον διακομιστή MCP απευθείας στο VS Code:

1. Δημιουργήστε μια διαμόρφωση εκκίνησης στο `.vscode/launch.json`:
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

2. Ορίστε σημεία διακοπής στον κώδικα του διακομιστή σας.
3. Εκτελέστε τον εντοπιστή σφαλμάτων και δοκιμάστε με το Inspector.

### Συνηθισμένες συμβουλές εντοπισμού σφαλμάτων

- Χρησιμοποιήστε το `stderr` για καταγραφή - μην γράφετε ποτέ στο `stdout`, καθώς προορίζεται για μηνύματα MCP.
- Βεβαιωθείτε ότι όλα τα μηνύματα JSON-RPC είναι διαχωρισμένα με αλλαγές γραμμής.
- Δοκιμάστε πρώτα με απλά εργαλεία πριν προσθέσετε σύνθετη λειτουργικότητα.
- Χρησιμοποιήστε το Inspector για να επαληθεύσετε τις μορφές μηνυμάτων.

## Χρήση του διακομιστή stdio στο VS Code

Αφού δημιουργήσετε τον διακομιστή MCP stdio, μπορείτε να τον ενσωματώσετε στο VS Code για να τον χρησιμοποιήσετε με τον Claude ή άλλους πελάτες συμβατούς με MCP.

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

2. **Επανεκκινήστε τον Claude**: Κλείστε και ανοίξτε ξανά τον Claude για να φορτώσετε τη νέα διαμόρφωση διακομιστή.

3. **Δοκιμάστε τη σύνδεση**: Ξεκινήστε μια συνομιλία με τον Claude και δοκιμάστε τα εργαλεία του διακομιστή σας:
   - "Μπορείς να με χαιρετήσεις χρησιμοποιώντας το εργαλείο χαιρετισμού;"
   - "Υπολόγισε το άθροισμα του 15 και του 27."
   - "Ποια είναι οι πληροφορίες του διακομιστή;"

### Παράδειγμα διακομιστή stdio TypeScript

Ακολουθεί ένα πλήρες παράδειγμα TypeScript για αναφορά:

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

// Add tools
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
    .WithStdioTransport()
    .WithTools<Tools>();

var app = builder.Build();
await app.RunAsync();

public class Tools
{
    [Description("Get a personalized greeting")]
    public string GetGreeting(string name)
    {
        return $"Hello, {name}! Welcome to MCP stdio server.";
    }

    [Description("Calculate the sum of two numbers")]
    public int CalculateSum(int a, int b)
    {
        return a + b;
    }
}
```

## Περίληψη

Σε αυτό το ενημερωμένο μάθημα, μάθατε πώς να:

- Δημιουργείτε διακομιστές MCP χρησιμοποιώντας την τρέχουσα μεταφορά **stdio** (συνιστώμενη προσέγγιση).
- Κατανοείτε γιατί η μεταφορά SSE καταργήθηκε υπέρ της stdio και του Streamable HTTP.
- Δημιουργείτε εργαλεία που μπορούν να καλούνται από πελάτες MCP.
- Εντοπίζετε σφάλματα στον διακομιστή σας χρησιμοποιώντας το MCP Inspector.
- Ενσωματώνετε τον διακομιστή stdio στο VS Code και τον Claude.

Η μεταφορά stdio παρέχει έναν απλούστερο, πιο ασφαλή και πιο αποδοτικό τρόπο για τη δημιουργία διακομιστών MCP σε σύγκριση με την καταργημένη προσέγγιση SSE. Είναι η συνιστώμενη μεταφορά για τις περισσότερες υλοποιήσεις διακομιστών MCP σύμφωνα με την προδιαγραφή 2025-06-18.

### .NET

1. Ας δημιουργήσουμε πρώτα κάποια εργαλεία. Για αυτό, θα δημιουργήσουμε ένα αρχείο *Tools.cs* με το ακόλουθο περιεχόμενο:

  ```csharp
  using System.ComponentModel;
  using System.Text.Json;
  using ModelContextProtocol.Server;
  ```

## Άσκηση: Δοκιμή του διακομιστή stdio

Τώρα που δημιουργήσατε τον διακομιστή stdio, ας τον δοκιμάσουμε για να βεβαιωθούμε ότι λειτουργεί σωστά.

### Προαπαιτούμενα

1. Βεβαιωθείτε ότι έχετε εγκαταστήσει το MCP Inspector:
   ```bash
   npm install -g @modelcontextprotocol/inspector
   ```

2. Ο κώδικας του διακομιστή σας πρέπει να είναι αποθηκευμένος (π.χ., ως `server.py`).

### Δοκιμή με το Inspector

1. **Εκκινήστε το Inspector με τον διακομιστή σας**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

2. **Ανοίξτε τη διεπαφή ιστού**: Το Inspector θα ανοίξει ένα παράθυρο περιηγητή που δείχνει τις δυνατότητες του διακομιστή σας.

3. **Δοκιμάστε τα εργαλεία**: 
   - Δοκιμάστε το εργαλείο `get_greeting` με διαφορετικά ονόματα.
   - Δοκιμάστε το εργαλείο `calculate_sum` με διάφορους αριθμούς.
   - Καλέστε το εργαλείο `get_server_info` για να δείτε μεταδεδομένα του διακομιστή.

4. **Παρακολουθήστε την επικοινωνία**: Το Inspector δείχνει τα μηνύματα JSON-RPC που ανταλλάσσονται μεταξύ πελάτη και διακομιστή.

### Τι πρέπει να δείτε

Όταν ο διακομιστής σας ξεκινήσει σωστά, θα πρέπει να δείτε:
- Τις δυνατότητες του διακομιστή να εμφανίζονται στο Inspector.
- Εργαλεία διαθέσιμα για δοκιμή.
- Επιτυχημένες ανταλλαγές μηνυμάτων JSON-RPC.
- Απαντήσεις εργαλείων να εμφανίζονται στη διεπαφή.

### Συνηθισμένα προβλήματα και λύσεις

**Ο διακομιστής δεν ξεκινά:**
- Ελέγξτε ότι όλες οι εξαρτήσεις είναι εγκατεστημένες: `pip install mcp`.
- Επαληθεύστε τη σύνταξη και την εσοχή του Python.
- Αναζητήστε μηνύματα σφάλματος στην κονσόλα.

**Τα εργαλεία δεν εμφανίζονται:**
- Βεβαιωθείτε ότι υπάρχουν οι διακοσμητές `@server.tool()`.
- Ελέγξτε ότι οι συναρτήσεις εργαλείων είναι ορισμένες πριν από το `main()`.
- Επαληθεύστε ότι ο διακομιστής έχει διαμορφωθεί σωστά.

**Προβλήματα σύνδεσης:**
- Βεβαιωθείτε ότι ο διακομιστής χρησιμοποιεί σωστά τη μεταφορά stdio.
- Ελέγξτε ότι δεν παρεμβαίνουν άλλες διεργασίες.
- Επαληθεύστε τη σύνταξη της εντολής του Inspector.

## Εργασία

Δοκιμάστε να επεκτείνετε τον διακομιστή σας με περισσότερες δυνατότητες. Δείτε [αυτή τη σελίδα](https://api.chucknorris.io/) για να προσθέσετε, για παράδειγμα, ένα εργαλείο που καλεί ένα API. Εσείς αποφασίζετε πώς θα μοιάζει ο διακομιστής. Καλή διασκέδαση :)

## Λύση

[Λύση](./solution/README.md) Ακολουθεί μια πιθανή λύση με λειτουργικό κώδικα.

## Βασικά Σημεία

Τα βασικά σημεία αυτού του κεφαλαίου είναι τα εξής:

- Η μεταφορά stdio είναι ο συνιστώμενος μηχανισμός για τοπικούς διακομιστές MCP.
- Η μεταφορά stdio επιτρέπει απρόσκοπτη επικοινωνία μεταξύ διακομιστών MCP και πελατών χρησιμοποιώντας τυπικές ροές εισόδου και εξόδου.
- Μπορείτε να χρησιμοποιήσετε τόσο το Inspector όσο και το Visual Studio Code για

---

**Αποποίηση ευθύνης**:  
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας την υπηρεσία αυτόματης μετάφρασης [Co-op Translator](https://github.com/Azure/co-op-translator). Παρόλο που καταβάλλουμε προσπάθειες για ακρίβεια, παρακαλούμε να έχετε υπόψη ότι οι αυτοματοποιημένες μεταφράσεις ενδέχεται να περιέχουν σφάλματα ή ανακρίβειες. Το πρωτότυπο έγγραφο στη μητρική του γλώσσα θα πρέπει να θεωρείται η αυθεντική πηγή. Για κρίσιμες πληροφορίες, συνιστάται επαγγελματική ανθρώπινη μετάφραση. Δεν φέρουμε ευθύνη για τυχόν παρεξηγήσεις ή εσφαλμένες ερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.