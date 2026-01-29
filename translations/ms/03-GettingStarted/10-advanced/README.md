# Penggunaan pelayan lanjutan

Terdapat dua jenis pelayan yang didedahkan dalam MCP SDK, iaitu pelayan biasa dan pelayan tahap rendah. Biasanya, anda akan menggunakan pelayan biasa untuk menambah ciri-ciri padanya. Walau bagaimanapun, dalam beberapa kes, anda mungkin ingin bergantung kepada pelayan tahap rendah seperti:

- **Senibina yang lebih baik.** Walaupun senibina yang bersih boleh dicipta dengan kedua-dua pelayan biasa dan pelayan tahap rendah, ia boleh dikatakan sedikit lebih mudah dengan pelayan tahap rendah.
- **Ketersediaan ciri.** Beberapa ciri lanjutan hanya boleh digunakan dengan pelayan tahap rendah. Anda akan melihat ini dalam bab-bab seterusnya apabila kita menambah pensampelan dan pengumpulan maklumat.

## Pelayan biasa vs pelayan tahap rendah

Berikut adalah bagaimana penciptaan MCP Server kelihatan dengan pelayan biasa:

**Python**

```python
mcp = FastMCP("Demo")

# Add an addition tool
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

// Add an addition tool
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

Intinya adalah anda secara eksplisit menambah setiap alat, sumber atau arahan yang anda mahu pelayan miliki. Tiada masalah dengan itu.

### Pendekatan pelayan tahap rendah

Namun, apabila anda menggunakan pendekatan pelayan tahap rendah, anda perlu berfikir secara berbeza, iaitu bukannya mendaftarkan setiap alat, anda sebaliknya mencipta dua pengendali bagi setiap jenis ciri (alat, sumber atau arahan). Sebagai contoh, untuk alat, hanya terdapat dua fungsi seperti berikut:

- **Menyenaraikan semua alat.** Satu fungsi bertanggungjawab untuk semua percubaan menyenaraikan alat.
- **Mengendalikan panggilan semua alat.** Di sini juga, hanya satu fungsi yang mengendalikan panggilan kepada alat.

Kedengaran seperti kerja yang lebih sedikit, bukan? Jadi, bukannya mendaftarkan alat, saya hanya perlu memastikan alat itu disenaraikan apabila saya menyenaraikan semua alat dan ia dipanggil apabila terdapat permintaan masuk untuk memanggil alat.

Mari kita lihat bagaimana kodnya kelihatan sekarang:

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
                    "a": {"type": "number", "description": "nubmer to add"}, 
                    "b": {"type": "number", "description": "nubmer to add"}
                },
                "required": ["query"],
            },
        )
    ]
```

**TypeScript**

```typescript
server.setRequestHandler(ListToolsRequestSchema, async (request) => {
  // Return the list of registered tools
  return {
    tools: [{
        name="add",
        description="Add two numbers",
        inputSchema={
            "type": "object",
            "properties": {
                "a": {"type": "number", "description": "nubmer to add"}, 
                "b": {"type": "number", "description": "nubmer to add"}
            },
            "required": ["query"],
        }
    }]
  };
});
```

Di sini kita kini mempunyai fungsi yang mengembalikan senarai ciri. Setiap entri dalam senarai alat kini mempunyai medan seperti `name`, `description` dan `inputSchema` untuk mematuhi jenis pulangan. Ini membolehkan kita meletakkan alat dan definisi ciri kita di tempat lain. Kita kini boleh mencipta semua alat kita dalam folder alat dan perkara yang sama berlaku untuk semua ciri anda, jadi projek anda tiba-tiba boleh diatur seperti berikut:

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

Hebat, senibina kita boleh dibuat kelihatan agak bersih.

Bagaimana pula dengan memanggil alat, adakah ia idea yang sama, satu pengendali untuk memanggil alat, mana-mana alat? Ya, betul, berikut adalah kod untuk itu:

**Python**

```python
@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict[str, str] | None
) -> list[types.TextContent]:
    
    # tools is a dictionary with tool names as keys
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
    
    // args: request.params.arguments
    // TODO call the tool, 

    return {
       content: [{ type: "text", text: `Tool ${name} called with arguments: ${JSON.stringify(input)}, result: ${JSON.stringify(result)}` }]
    };
});
```

Seperti yang anda lihat daripada kod di atas, kita perlu menguraikan alat untuk dipanggil, dan dengan hujah apa, dan kemudian kita perlu meneruskan untuk memanggil alat tersebut.

## Meningkatkan pendekatan dengan pengesahan

Setakat ini, anda telah melihat bagaimana semua pendaftaran anda untuk menambah alat, sumber dan arahan boleh digantikan dengan dua pengendali ini bagi setiap jenis ciri. Apa lagi yang perlu kita lakukan? Nah, kita harus menambah beberapa bentuk pengesahan untuk memastikan alat dipanggil dengan hujah yang betul. Setiap runtime mempunyai penyelesaian mereka sendiri untuk ini, contohnya Python menggunakan Pydantic dan TypeScript menggunakan Zod. Ideanya adalah kita melakukan perkara berikut:

- Pindahkan logik untuk mencipta ciri (alat, sumber atau arahan) ke folder khususnya.
- Tambahkan cara untuk mengesahkan permintaan masuk yang meminta, contohnya, memanggil alat.

### Mencipta ciri

Untuk mencipta ciri, kita perlu mencipta fail untuk ciri tersebut dan memastikan ia mempunyai medan wajib yang diperlukan oleh ciri tersebut. Medan yang diperlukan berbeza sedikit antara alat, sumber dan arahan.

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
        # Validate input using Pydantic model
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # TODO: add Pydantic, so we can create an AddInputModel and validate args

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

Di sini anda dapat melihat bagaimana kita melakukan perkara berikut:

- Mencipta skema menggunakan Pydantic `AddInputModel` dengan medan `a` dan `b` dalam fail *schema.py*.
- Mencuba untuk menguraikan permintaan masuk supaya menjadi jenis `AddInputModel`, jika terdapat ketidakpadanan dalam parameter ini akan gagal:

   ```python
   # add.py
    try:
        # Validate input using Pydantic model
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")
   ```

Anda boleh memilih sama ada untuk meletakkan logik penguraian ini dalam panggilan alat itu sendiri atau dalam fungsi pengendali.

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

- Dalam pengendali yang menguruskan semua panggilan alat, kita kini cuba menguraikan permintaan masuk ke dalam skema yang ditentukan oleh alat:

    ```typescript
    const Schema = tool.rawSchema;

    try {
       const input = Schema.parse(request.params.arguments);
    ```

    jika itu berjaya, maka kita meneruskan untuk memanggil alat sebenar:

    ```typescript
    const result = await tool.callback(input);
    ```

Seperti yang anda lihat, pendekatan ini mencipta senibina yang hebat kerana semuanya mempunyai tempatnya, *server.ts* adalah fail yang sangat kecil yang hanya menyambungkan pengendali permintaan dan setiap ciri berada dalam folder masing-masing iaitu tools/, resources/ atau /prompts.

Hebat, mari kita cuba membina ini seterusnya.

## Latihan: Mencipta pelayan tahap rendah

Dalam latihan ini, kita akan melakukan perkara berikut:

1. Mencipta pelayan tahap rendah yang mengendalikan penyenaraian alat dan pemanggilan alat.
1. Melaksanakan senibina yang boleh anda bina.
1. Menambah pengesahan untuk memastikan panggilan alat anda disahkan dengan betul.

### -1- Mencipta senibina

Perkara pertama yang perlu kita tangani ialah senibina yang membantu kita berkembang apabila kita menambah lebih banyak ciri, berikut adalah bagaimana ia kelihatan:

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

Kini kita telah menyediakan senibina yang memastikan kita boleh dengan mudah menambah alat baharu dalam folder alat. Jangan ragu untuk mengikuti ini untuk menambah subdirektori bagi sumber dan arahan.

### -2- Mencipta alat

Mari kita lihat bagaimana mencipta alat kelihatan seterusnya. Pertama, ia perlu dicipta dalam subdirektori *tool* seperti berikut:

**Python**

```python
from .schema import AddInputModel

async def add_handler(args) -> float:
    try:
        # Validate input using Pydantic model
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # TODO: add Pydantic, so we can create an AddInputModel and validate args

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

Apa yang kita lihat di sini ialah bagaimana kita mentakrifkan nama, penerangan, skema input menggunakan Pydantic dan pengendali yang akan dipanggil apabila alat ini dipanggil. Akhirnya, kita mendedahkan `tool_add` yang merupakan kamus yang memegang semua sifat ini.

Terdapat juga *schema.py* yang digunakan untuk mentakrifkan skema input yang digunakan oleh alat kita:

```python
from pydantic import BaseModel

class AddInputModel(BaseModel):
    a: float
    b: float
```

Kita juga perlu mengisi *__init__.py* untuk memastikan direktori alat dianggap sebagai modul. Selain itu, kita perlu mendedahkan modul-modul di dalamnya seperti berikut:

```python
from .add import tool_add

tools = {
  tool_add["name"] : tool_add
}
```

Kita boleh terus menambah fail ini apabila kita menambah lebih banyak alat.

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

Di sini kita mencipta kamus yang terdiri daripada sifat-sifat:

- **name**, ini adalah nama alat.
- **rawSchema**, ini adalah skema Zod, ia akan digunakan untuk mengesahkan permintaan masuk untuk memanggil alat ini.
- **inputSchema**, skema ini akan digunakan oleh pengendali.
- **callback**, ini digunakan untuk memanggil alat.

Terdapat juga `Tool` yang digunakan untuk menukar kamus ini menjadi jenis yang boleh diterima oleh pengendali pelayan MCP dan ia kelihatan seperti berikut:

```typescript
import { z } from 'zod';

export interface Tool {
    name: string;
    inputSchema: any;
    rawSchema: z.ZodTypeAny;
    callback: (args: z.infer<z.ZodTypeAny>) => Promise<{ content: { type: string; text: string }[] }>;
}
```

Dan terdapat *schema.ts* di mana kita menyimpan skema input untuk setiap alat yang kelihatan seperti berikut dengan hanya satu skema pada masa ini tetapi apabila kita menambah alat, kita boleh menambah lebih banyak entri:

```typescript
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });
```

Hebat, mari kita teruskan untuk mengendalikan penyenaraian alat kita seterusnya.

### -3- Mengendalikan penyenaraian alat

Seterusnya, untuk mengendalikan penyenaraian alat kita, kita perlu menyediakan pengendali permintaan untuk itu. Berikut adalah apa yang perlu kita tambah pada fail pelayan kita:

**Python**

```python
# code omitted for brevity
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

Di sini kita menambah penghias `@server.list_tools` dan fungsi pelaksanaan `handle_list_tools`. Dalam fungsi tersebut, kita perlu menghasilkan senarai alat. Perhatikan bagaimana setiap alat perlu mempunyai nama, penerangan dan inputSchema.

**TypeScript**

Untuk menyediakan pengendali permintaan untuk menyenaraikan alat, kita perlu memanggil `setRequestHandler` pada pelayan dengan skema yang sesuai dengan apa yang kita cuba lakukan, dalam kes ini `ListToolsRequestSchema`.

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
// code omitted for brevity
import { tools } from './tools/index.js';

server.setRequestHandler(ListToolsRequestSchema, async (request) => {
  // Return the list of registered tools
  return {
    tools: tools
  };
});
```

Hebat, kini kita telah menyelesaikan bahagian penyenaraian alat, mari kita lihat bagaimana kita boleh memanggil alat seterusnya.

### -4- Mengendalikan pemanggilan alat

Untuk memanggil alat, kita perlu menyediakan pengendali permintaan lain, kali ini memberi tumpuan kepada menangani permintaan yang menentukan ciri mana yang hendak dipanggil dan dengan hujah apa.

**Python**

Mari gunakan penghias `@server.call_tool` dan melaksanakannya dengan fungsi seperti `handle_call_tool`. Dalam fungsi tersebut, kita perlu menguraikan nama alat, hujahnya dan memastikan hujah tersebut sah untuk alat yang dimaksudkan. Kita boleh sama ada mengesahkan hujah dalam fungsi ini atau di bahagian bawah dalam alat sebenar.

```python
@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict[str, str] | None
) -> list[types.TextContent]:
    
    # tools is a dictionary with tool names as keys
    if name not in tools.tools:
        raise ValueError(f"Unknown tool: {name}")
    
    tool = tools.tools[name]

    result = "default"
    try:
        # invoke the tool
        result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)
    except Exception as e:
        raise ValueError(f"Error calling tool {name}: {str(e)}")

    return [
        types.TextContent(type="text", text=str(result))
    ] 
```

Berikut adalah apa yang berlaku:

- Nama alat kita sudah ada sebagai parameter input `name` yang juga benar untuk hujah kita dalam bentuk kamus `arguments`.

- Alat dipanggil dengan `result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)`. Pengesahan hujah berlaku dalam sifat `handler` yang menunjuk kepada fungsi, jika itu gagal ia akan menaikkan pengecualian.

Di sana, kini kita mempunyai pemahaman penuh tentang penyenaraian dan pemanggilan alat menggunakan pelayan tahap rendah.

Lihat [contoh penuh](./code/README.md) di sini.

## Tugasan

Kembangkan kod yang telah diberikan kepada anda dengan beberapa alat, sumber dan arahan dan renungkan bagaimana anda perasan bahawa anda hanya perlu menambah fail dalam direktori alat dan tidak di tempat lain.

*Tiada penyelesaian diberikan*

## Ringkasan

Dalam bab ini, kita melihat bagaimana pendekatan pelayan tahap rendah berfungsi dan bagaimana ia boleh membantu kita mencipta senibina yang baik untuk terus dibangunkan. Kita juga membincangkan pengesahan dan anda ditunjukkan bagaimana bekerja dengan perpustakaan pengesahan untuk mencipta skema bagi pengesahan input.

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk memastikan ketepatan, sila ambil perhatian bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang berwibawa. Untuk maklumat yang kritikal, terjemahan manusia profesional adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.