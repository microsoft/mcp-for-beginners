# Προηγμένη χρήση διακομιστή

Υπάρχουν δύο διαφορετικοί τύποι διακομιστών που εκτίθενται στο MCP SDK, ο κανονικός διακομιστής σας και ο διακομιστής χαμηλού επιπέδου. Κανονικά, θα χρησιμοποιούσατε τον κανονικό διακομιστή για να προσθέσετε λειτουργίες σε αυτόν. Σε ορισμένες περιπτώσεις, ωστόσο, θέλετε να βασιστείτε στον διακομιστή χαμηλού επιπέδου, όπως:

- Καλύτερη αρχιτεκτονική. Είναι δυνατό να δημιουργηθεί μια καθαρή αρχιτεκτονική τόσο με τον κανονικό διακομιστή όσο και με έναν διακομιστή χαμηλού επιπέδου, αλλά μπορεί να υποστηριχθεί ότι είναι λίγο πιο εύκολο με διακομιστή χαμηλού επιπέδου.
- Διαθεσιμότητα χαρακτηριστικών. Ορισμένες προηγμένες λειτουργίες μπορούν να χρησιμοποιηθούν μόνο με διακομιστή χαμηλού επιπέδου. Θα δείτε αυτό στα επόμενα κεφάλαια καθώς προσθέτουμε δειγματοληψία και ελιξιόν.

## Κανονικός διακομιστής vs διακομιστής χαμηλού επιπέδου

Έτσι φαίνεται η δημιουργία ενός MCP Server με τον κανονικό διακομιστή

**Python**

```python
mcp = FastMCP("Demo")

# Προσθέστε ένα εργαλείο πρόσθεσης
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b
```

**TypeScript**

```typescript
const server = new McpServer({
  name: "demo-server",
  version: "1.0.0"
});

// Προσθέστε ένα εργαλείο πρόσθεσης
server.registerTool("add",
  {
    title: "Addition Tool",
    description: "Add two numbers",
    inputSchema: { a: z.number(), b: z.number() }
  },
  async ({ a, b }) => ({
    content: [{ type: "text", text: String(a + b) }]
  })
);
```

Το θέμα είναι ότι προσθέτετε ρητά κάθε εργαλείο, πόρο ή πρότυπο που θέλετε να έχει ο διακομιστής. Δεν υπάρχει τίποτα λάθος με αυτό.  

### Προσέγγιση διακομιστή χαμηλού επιπέδου

Ωστόσο, όταν χρησιμοποιείτε την προσέγγιση διακομιστή χαμηλού επιπέδου, πρέπει να το σκεφτείτε διαφορετικά. Αντί να καταχωρίζετε κάθε εργαλείο, δημιουργείτε δύο χειριστές ανά τύπο λειτουργίας (εργαλεία, πόροι ή προτροπές). Για παράδειγμα, τα εργαλεία έχουν μόνο δύο συναρτήσεις ως εξής:

- Καταλογογράφηση όλων των εργαλείων. Μία συνάρτηση θα είναι υπεύθυνη για όλες τις προσπάθειες καταλογογράφησης εργαλείων.
- Χειρισμός κλήσης όλων των εργαλείων. Εδώ επίσης, υπάρχει μόνο μία συνάρτηση που χειρίζεται τις κλήσεις προς ένα εργαλείο.

Ακούγεται σαν λίγο λιγότερη δουλειά, σωστά; Αντί να καταχωρίσω ένα εργαλείο, απλώς πρέπει να βεβαιωθώ ότι το εργαλείο περιλαμβάνεται όταν καταλογογραφώ όλα τα εργαλεία και ότι καλείται όταν υπάρχει εισερχόμενο αίτημα για κλήση εργαλείου.

Ας δούμε τώρα πώς φαίνεται ο κώδικας:

**Python**

```python
@server.list_tools()
async def handle_list_tools() -> list[types.Tool]:
    """List available tools."""
    return [
        types.Tool(
            name="add",
            description="Add two numbers",
            inputSchema={
                "type": "object",
                "properties": {
                    "a": {"type": "number", "description": "number to add"}, 
                    "b": {"type": "number", "description": "number to add"}
                },
                "required": ["query"],
            },
        )
    ]
```

**TypeScript**

```typescript
server.setRequestHandler(ListToolsRequestSchema, async (request) => {
  // Επιστρέφει τη λίστα των καταχωρημένων εργαλείων
  return {
    tools: [{
        name: "add",
        description: "Add two numbers",
        inputSchema: {
            "type": "object",
            "properties": {
                "a": {"type": "number", "description": "number to add"},
                "b": {"type": "number", "description": "number to add"}
            },
            "required": ["query"],
        }
    }]
  };
});
```

Εδώ έχουμε τώρα μια συνάρτηση που επιστρέφει μια λίστα λειτουργιών. Κάθε καταχώρηση στη λίστα εργαλείων έχει τώρα πεδία όπως `name`, `description` και `inputSchema` για να τηρεί τον τύπο επιστροφής. Αυτό μας επιτρέπει να βάλουμε τα εργαλεία και τον ορισμό λειτουργίας αλλού. Τώρα μπορούμε να δημιουργήσουμε όλα τα εργαλεία μας σε έναν φάκελο tools και το ίδιο ισχύει για όλες τις λειτουργίες σας, έτσι το έργο σας μπορεί ξαφνικά να οργανωθεί ως εξής:

```text
app
--| tools
----| add
----| substract
--| resources
----| products
----| schemas
--| prompts
----| product-description
```

Αυτό είναι υπέροχο, η αρχιτεκτονική μας μπορεί να γίνει αρκετά καθαρή.

Τι γίνεται με την κλήση εργαλείων, είναι η ίδια ιδέα δηλαδή, ένας χειριστής για να καλέσει ένα εργαλείο, όποιο εργαλείο και αν είναι; Ναι, ακριβώς, εδώ είναι ο κώδικας για αυτό:

**Python**

```python
@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict[str, str] | None
) -> list[types.TextContent]:
    
    # τα εργαλεία είναι ένα λεξικό με ονόματα εργαλείων ως κλειδιά
    if name not in tools.tools:
        raise ValueError(f"Unknown tool: {name}")
    
    tool = tools.tools[name]

    result = "default"
    try:
        result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)
    except Exception as e:
        raise ValueError(f"Error calling tool {name}: {str(e)}")

    return [
        types.TextContent(type="text", text=str(result))
    ] 
```

**TypeScript**

```typescript
server.setRequestHandler(CallToolRequestSchema, async (request) => {
    const { params: { name } } = request;
    let tool = tools.find(t => t.name === name);
    if(!tool) {
        return {
            error: {
                code: "tool_not_found",
                message: `Tool ${name} not found.`
            }
       };
    }
    
    // ορίσματα: request.params.arguments
    // TODO καλέστε το εργαλείο,

    return {
       content: [{ type: "text", text: `Tool ${name} called with arguments: ${JSON.stringify(input)}, result: ${JSON.stringify(result)}` }]
    };
});
```

Όπως βλέπετε από τον παραπάνω κώδικα, πρέπει να αναλύσουμε ποιο εργαλείο θα καλέσουμε και με ποια επιχειρήματα, και στη συνέχεια πρέπει να προχωρήσουμε στην κλήση του εργαλείου.

## Βελτίωση της προσέγγισης με επικύρωση

Μέχρι τώρα είδατε πώς όλες οι καταχωρίσεις σας για προσθήκη εργαλείων, πόρων και προτροπών μπορούν να αντικατασταθούν από αυτούς τους δύο χειριστές ανά τύπο λειτουργίας. Τι άλλο πρέπει να κάνουμε; Λοιπόν, πρέπει να προσθέσουμε κάποια μορφή επικύρωσης για να διασφαλίσουμε ότι το εργαλείο καλείται με τα σωστά επιχειρήματα. Κάθε runtime έχει τη δική του λύση γι' αυτό, για παράδειγμα η Python χρησιμοποιεί Pydantic και το TypeScript χρησιμοποιεί Zod. Η ιδέα είναι ότι κάνουμε τα εξής:

- Μεταφέρουμε τη λογική δημιουργίας μιας λειτουργίας (εργαλείο, πόρος ή πρότυπο) στον αφιερωμένο φάκελο της.
- Προσθέτουμε έναν τρόπο να επικυρώνουμε ένα εισερχόμενο αίτημα που ζητά, για παράδειγμα, την κλήση ενός εργαλείου.

### Δημιουργία λειτουργίας

Για να δημιουργήσουμε μια λειτουργία, θα χρειαστεί να δημιουργήσουμε ένα αρχείο για αυτή τη λειτουργία και να βεβαιωθούμε ότι έχει τα υποχρεωτικά πεδία που απαιτούνται για αυτή τη λειτουργία. Καθώς τα πεδία διαφέρουν λίγο μεταξύ εργαλείων, πόρων και προτροπών.

**Python**

```python
# schema.py
from pydantic import BaseModel

class AddInputModel(BaseModel):
    a: float
    b: float

# add.py

from .schema import AddInputModel

async def add_handler(args) -> float:
    try:
        # Επικύρωση εισόδου χρησιμοποιώντας μοντέλο Pydantic
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # TODO: πρόσθεσε Pydantic, ώστε να μπορούμε να δημιουργήσουμε ένα AddInputModel και να επικυρώσουμε τα ορίσματα

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

Εδώ μπορείτε να δείτε πώς κάνουμε τα εξής:

- Δημιουργούμε ένα schema χρησιμοποιώντας Pydantic `AddInputModel` με πεδία `a` και `b` στο αρχείο *schema.py*.
- Προσπαθούμε να αναλύσουμε το εισερχόμενο αίτημα ώστε να είναι τύπου `AddInputModel`, εάν υπάρχει ασυμφωνία στις παραμέτρους αυτό θα καταρρεύσει:

   ```python
   # add.py
    try:
        # Επικυρώστε την είσοδο χρησιμοποιώντας το μοντέλο Pydantic
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")
   ```

Μπορείτε να επιλέξετε αν θα βάλετε αυτή τη λογική ανάλυσης στην ίδια την κλήση του εργαλείου ή στη λειτουργία χειρισμού.

**TypeScript**

```typescript
// server.ts
server.setRequestHandler(CallToolRequestSchema, async (request) => {
    const { params: { name } } = request;
    let tool = tools.find(t => t.name === name);
    if (!tool) {
       return {
        error: {
            code: "tool_not_found",
            message: `Tool ${name} not found.`
        }
       };
    }
    const Schema = tool.rawSchema;

    try {
       const input = Schema.parse(request.params.arguments);

       // @ts-ignore
       const result = await tool.callback(input);

       return {
          content: [{ type: "text", text: `Tool ${name} called with arguments: ${JSON.stringify(input)}, result: ${JSON.stringify(result)}` }]
      };
    } catch (error) {
       return {
          error: {
             code: "invalid_arguments",
             message: `Invalid arguments for tool ${name}: ${error instanceof Error ? error.message : String(error)}`
          }
    };
   }

});

// schema.ts
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });

// add.ts
import { Tool } from "./tool.js";
import { MathInputSchema } from "./schema.js";
import { zodToJsonSchema } from "zod-to-json-schema";

export default {
    name: "add",
    rawSchema: MathInputSchema,
    inputSchema: zodToJsonSchema(MathInputSchema),
    callback: async ({ a, b }) => {
        return {
            content: [{ type: "text", text: String(a + b) }]
        };
    }
} as Tool;
```

- Στον χειριστή που διαχειρίζεται όλες τις κλήσεις εργαλείων, πλέον προσπαθούμε να αναλύσουμε το εισερχόμενο αίτημα στο ορισμένο schema του εργαλείου:

    ```typescript
    const Schema = tool.rawSchema;

    try {
       const input = Schema.parse(request.params.arguments);
    ```

    αν αυτό λειτουργήσει, τότε προχωράμε στην κλήση του ίδιου του εργαλείου:

    ```typescript
    const result = await tool.callback(input);
    ```

Όπως βλέπετε, αυτή η προσέγγιση δημιουργεί μια εξαιρετική αρχιτεκτονική καθώς κάθε πράγμα έχει τη θέση του, το *server.ts* είναι ένα πολύ μικρό αρχείο που απλώς συνδέει τους χειριστές αιτημάτων και κάθε λειτουργία βρίσκεται στον αντίστοιχο φάκελό της, π.χ. tools/, resources/ ή /prompts.

Τέλεια, ας προσπαθήσουμε να το υλοποιήσουμε παρακάτω. 

## Άσκηση: Δημιουργία διακομιστή χαμηλού επιπέδου

Σε αυτή την άσκηση, θα κάνουμε τα εξής:

1. Δημιουργία διακομιστή χαμηλού επιπέδου που χειρίζεται την καταλογογράφηση των εργαλείων και την κλήση των εργαλείων.
1. Υλοποίηση μιας αρχιτεκτονικής πάνω στην οποία μπορείτε να χτίσετε.
1. Προσθήκη επικύρωσης για να διασφαλίσουμε ότι οι κλήσεις των εργαλείων σας επικυρώνονται σωστά.

### -1- Δημιουργία αρχιτεκτονικής

Το πρώτο πράγμα που πρέπει να αντιμετωπίσουμε είναι μια αρχιτεκτονική που μας βοηθά να κλιμακωθούμε καθώς προσθέτουμε περισσότερες λειτουργίες, να πώς φαίνεται:

**Python**

```text
server.py
--| tools
----| __init__.py
----| add.py
----| schema.py
client.py
```

**TypeScript**

```text
server.ts
--| tools
----| add.ts
----| schema.ts
client.ts
```

Τώρα έχουμε στήσει μια αρχιτεκτονική που εξασφαλίζει ότι μπορούμε εύκολα να προσθέσουμε νέα εργαλεία σε έναν φάκελο tools. Μπορείτε να ακολουθήσετε το ίδιο για να προσθέσετε υποφακέλους για resources και prompts.

### -2- Δημιουργία εργαλείου

Ας δούμε πώς γίνεται η δημιουργία ενός εργαλείου. Πρώτα, πρέπει να δημιουργηθεί στον υποφάκελο *tool* ως εξής:

**Python**

```python
from .schema import AddInputModel

async def add_handler(args) -> float:
    try:
        # Επικύρωση εισόδου χρησιμοποιώντας το μοντέλο Pydantic
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # TODO: προσθήκη Pydantic, ώστε να μπορούμε να δημιουργήσουμε ένα AddInputModel και να επικυρώνουμε τα args

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

Εδώ βλέπουμε πώς ορίζουμε το name, description και το input schema χρησιμοποιώντας Pydantic και έναν χειριστή που θα κληθεί όταν αυτό το εργαλείο καλείται. Τέλος, εκθέτουμε το `tool_add` που είναι ένα λεξικό που περιέχει όλες αυτές τις ιδιότητες.

Υπάρχει και το *schema.py* που χρησιμοποιείται για τον ορισμό του input schema που χρησιμοποιεί το εργαλείο μας:

```python
from pydantic import BaseModel

class AddInputModel(BaseModel):
    a: float
    b: float
```

Χρειαζόμαστε επίσης να συμπληρώσουμε το *__init__.py* για να βεβαιωθούμε ότι ο φάκελος tools αντιμετωπίζεται ως module. Επιπλέον, πρέπει να εκθέσουμε τα modules εντός του ως εξής:

```python
from .add import tool_add

tools = {
  tool_add["name"] : tool_add
}
```

Μπορούμε να συνεχίσουμε να προσθέτουμε σε αυτό το αρχείο καθώς προσθέτουμε περισσότερα εργαλεία.

**TypeScript**

```typescript
import { Tool } from "./tool.js";
import { MathInputSchema } from "./schema.js";
import { zodToJsonSchema } from "zod-to-json-schema";

export default {
    name: "add",
    rawSchema: MathInputSchema,
    inputSchema: zodToJsonSchema(MathInputSchema),
    callback: async ({ a, b }) => {
        return {
            content: [{ type: "text", text: String(a + b) }]
        };
    }
} as Tool;
```

Εδώ δημιουργούμε ένα λεξικό που αποτελείται από ιδιότητες:

- name, αυτό είναι το όνομα του εργαλείου.
- rawSchema, αυτό είναι το schema Zod, θα χρησιμοποιηθεί για επικύρωση των εισερχόμενων αιτημάτων για κλήση αυτού του εργαλείου.
- inputSchema, αυτό το schema θα χρησιμοποιηθεί από τον handler.
- callback, αυτό χρησιμοποιείται για να καλέσει το εργαλείο.

Υπάρχει επίσης το `Tool` που χρησιμοποιείται για να μετατρέψει αυτό το λεξικό σε τύπο που μπορεί να αποδεχτεί ο χειριστής διακομιστή mcp και φαίνεται ως εξής:

```typescript
import { z } from 'zod';

export interface Tool {
    name: string;
    inputSchema: any;
    rawSchema: z.ZodTypeAny;
    callback: (args: z.infer<z.ZodTypeAny>) => Promise<{ content: { type: string; text: string }[] }>;
}
```

Και υπάρχει το *schema.ts* όπου αποθηκεύουμε τα schemas εισόδου για κάθε εργαλείο που μοιάζει με αυτό με μόνο ένα schema προς το παρόν, αλλά καθώς προσθέτουμε εργαλεία μπορούμε να προσθέσουμε περισσότερες καταχωρήσεις:

```typescript
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });
```

Τέλεια, ας προχωρήσουμε τώρα στο να χειριστούμε την καταλογογράφηση των εργαλείων μας.

### -3- Χειρισμός καταλογογράφησης εργαλείων

Στη συνέχεια, για να χειριστούμε την καταλογογράφηση των εργαλείων μας, πρέπει να στήσουμε έναν χειριστή αιτημάτων για αυτό. Εδώ τι πρέπει να προσθέσουμε στο αρχείο του διακομιστή μας:

**Python**

```python
# κώδικας παραλείφθηκε για συντομία
from tools import tools

@server.list_tools()
async def handle_list_tools() -> list[types.Tool]:
    tool_list = []
    print(tools)

    for tool in tools.values():
        tool_list.append(
            types.Tool(
                name=tool["name"],
                description=tool["description"],
                inputSchema=pydantic_to_json(tool["input_schema"]),
            )
        )
    return tool_list
```

Εδώ, προσθέτουμε το διακοσμητή `@server.list_tools` και υλοποιούμε τη λειτουργία `handle_list_tools`. Σε αυτή, πρέπει να παράγουμε μια λίστα εργαλείων. Σημειώστε πώς κάθε εργαλείο πρέπει να έχει name, description και inputSchema.   

**TypeScript**

Για να στήσουμε τον χειριστή αιτημάτων για την καταλογογράφηση εργαλείων, πρέπει να καλέσουμε `setRequestHandler` στον διακομιστή με ένα schema που ταιριάζει με αυτό που προσπαθούμε να κάνουμε, σε αυτή την περίπτωση `ListToolsRequestSchema`. 

```typescript
// index.ts
import addTool from "./add.js";
import subtractTool from "./subtract.js";
import {server} from "../server.js";
import { Tool } from "./tool.js";

export let tools: Array<Tool> = [];
tools.push(addTool);
tools.push(subtractTool);

// server.ts
// Ο κώδικας παραλείπεται για συντομία
import { tools } from './tools/index.js';

server.setRequestHandler(ListToolsRequestSchema, async (request) => {
  // Επιστρέψτε τη λίστα των καταχωρημένων εργαλείων
  return {
    tools: tools
  };
});
```

Τέλεια, τώρα έχουμε λύσει το κομμάτι της καταλογογράφησης εργαλείων, ας δούμε πώς μπορούμε να καλούμε εργαλεία παρακάτω.

### -4- Χειρισμός κλήσης εργαλείου

Για να καλέσουμε ένα εργαλείο, πρέπει να στήσουμε έναν άλλο χειριστή αιτημάτων, αυτή τη φορά επικεντρωμένο στο να διαχειριστεί ένα αίτημα που προσδιορίζει ποια λειτουργία θα καλέσει και με ποια επιχειρήματα.

**Python**

Ας χρησιμοποιήσουμε το διακοσμητή `@server.call_tool` και να το υλοποιήσουμε με μια λειτουργία όπως η `handle_call_tool`. Μέσα σε αυτήν τη λειτουργία, πρέπει να αναλύσουμε το όνομα του εργαλείου, το όρισμά του και να διασφαλίσουμε ότι τα επιχειρήματα είναι έγκυρα για το συγκεκριμένο εργαλείο. Μπορούμε είτε να επικυρώσουμε τα επιχειρήματα σε αυτή τη λειτουργία είτε πιο κάτω στην ίδια τη λειτουργία του εργαλείου.

```python
@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict[str, str] | None
) -> list[types.TextContent]:
    
    # tools είναι ένα λεξικό με ονόματα εργαλείων ως κλειδιά
    if name not in tools.tools:
        raise ValueError(f"Unknown tool: {name}")
    
    tool = tools.tools[name]

    result = "default"
    try:
        # καλέστε το εργαλείο
        result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)
    except Exception as e:
        raise ValueError(f"Error calling tool {name}: {str(e)}")

    return [
        types.TextContent(type="text", text=str(result))
    ]
```

Να τι γίνεται:

- Το όνομα του εργαλείου είναι ήδη παρόν ως παράμετρος εισόδου `name` και τα επιχειρήματά μας είναι στη μορφή του λεξικού `arguments`.

- Το εργαλείο καλείται με `result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)`. Η επικύρωση των επιχειρημάτων γίνεται στην ιδιότητα `handler` που δείχνει σε συνάρτηση, αν αυτή αποτύχει θα εγείρει εξαίρεση.

Έχουμε λοιπόν πλήρη κατανόηση της καταλογογράφησης και κλήσης εργαλείων χρησιμοποιώντας διακομιστή χαμηλού επιπέδου.

Δείτε το [πλήρες παράδειγμα](./code/README.md) εδώ

## Ανάθεση

Επεκτείνετε τον κώδικα που σας δόθηκε με πλήθος εργαλείων, πόρων και προτροπών και αναλογιστείτε πώς παρατηρείτε ότι χρειάζεται να προσθέτετε μόνο αρχεία στον κατάλογο tools και πουθενά αλλού. 

*Δεν παρέχεται λύση*

## Περίληψη

Σε αυτό το κεφάλαιο, είδαμε πώς λειτουργεί η προσέγγιση διακομιστή χαμηλού επιπέδου και πώς αυτό μπορεί να μας βοηθήσει να δημιουργήσουμε μια ωραία αρχιτεκτονική πάνω στην οποία συνεχίζουμε να χτίζουμε. Συζητήσαμε επίσης για την επικύρωση και σας δείξαμε πώς να δουλεύετε με βιβλιοθήκες επικύρωσης για να δημιουργείτε σχήματα για επικύρωση εισόδου.

## Τι ακολουθεί

- Επόμενο: [Απλή Αυθεντικοποίηση](../11-simple-auth/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Αποποίηση ευθυνών**:
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας την υπηρεσία αυτόματης μετάφρασης AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ενώ καταβάλλουμε προσπάθεια για ακρίβεια, παρακαλούμε να γνωρίζετε ότι οι αυτόματες μεταφράσεις ενδέχεται να περιέχουν λάθη ή ανακρίβειες. Το πρωτότυπο έγγραφο στη μητρική του γλώσσα πρέπει να θεωρείται η αυθεντική πηγή. Για κρίσιμες πληροφορίες, συνιστάται επαγγελματική ανθρώπινη μετάφραση. Δεν φέρουμε ευθύνη για τυχόν παρεξηγήσεις ή παρανοήσεις που προκύπτουν από τη χρήση αυτής της μετάφρασης.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->