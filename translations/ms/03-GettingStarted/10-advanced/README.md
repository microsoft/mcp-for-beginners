# Penggunaan pelayan lanjutan

Terdapat dua jenis pelayan yang berbeza dipaparkan dalam MCP SDK, pelayan biasa anda dan pelayan tahap rendah. Biasanya, anda akan menggunakan pelayan biasa untuk menambah ciri kepadanya. Walau bagaimanapun, dalam beberapa kes, anda ingin bergantung pada pelayan tahap rendah seperti:

- Seni bina yang lebih baik. Adalah mungkin untuk mencipta seni bina yang bersih dengan kedua-dua pelayan biasa dan pelayan tahap rendah tetapi boleh diperdebatkan bahawa ia sedikit lebih mudah dengan pelayan tahap rendah.
- Ketersediaan ciri. Beberapa ciri lanjutan hanya boleh digunakan dengan pelayan tahap rendah. Anda akan melihat ini dalam bab-bab kemudian apabila kami menambah pengambilan sampel dan elicitation.

## Pelayan biasa vs pelayan tahap rendah

Ini ialah bagaimana penciptaan Pelayan MCP kelihatan dengan pelayan biasa

**Python**

```python
mcp = FastMCP("Demo")

# Tambah alat penambahan
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

// Tambah alat penambahan
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

Intipatinya ialah anda secara eksplisit menambah setiap alat, sumber atau petunjuk yang anda mahu pelayan miliki. Tiada yang salah dengan itu.

### Pendekatan pelayan tahap rendah

Walau bagaimanapun, apabila anda menggunakan pendekatan pelayan tahap rendah anda perlu memikirkannya secara berbeza. Daripada mendaftar setiap alat, anda sebaliknya mencipta dua pengendali setiap jenis ciri (alat, sumber atau petunjuk). Jadi sebagai contoh alat hanya mempunyai dua fungsi seperti berikut:

- Menyenaraikan semua alat. Satu fungsi akan bertanggungjawab untuk semua usaha menyenaraikan alat.
- mengendalikan panggilan semua alat. Di sini juga, hanya ada satu fungsi mengendalikan panggilan ke alat

Itu kedengaran seperti kerja yang mungkin kurang, bukan? Jadi daripada mendaftar alat, saya hanya perlu memastikan alat itu disenaraikan apabila saya menyenaraikan semua alat dan ia dipanggil apabila terdapat permintaan masuk untuk memanggil alat.

Jom lihat bagaimana kod itu kelihatan sekarang:

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
  // Kembalikan senarai alat yang berdaftar
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

Di sini kami kini mempunyai fungsi yang mengembalikan senarai ciri. Setiap entri dalam senarai alat kini mempunyai medan seperti `name`, `description` dan `inputSchema` untuk mematuhi jenis pengembalian. Ini membolehkan kami meletakkan alat dan definisi ciri kami di tempat lain. Kami kini boleh mencipta semua alat kami dalam folder alat dan perkara yang sama berlaku untuk semua ciri anda supaya projek anda secara tiba-tiba boleh diatur seperti berikut:

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

Itu hebat, seni bina kami boleh dibuat kelihatan cukup kemas.

Bagaimana pula dengan memanggil alat, adakah ia idea yang sama, satu pengendali untuk memanggil alat, alat mana-mana? Ya, tepat sekali, ini adalah kod untuk itu:

**Python**

```python
@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict[str, str] | None
) -> list[types.TextContent]:
    
    # tools adalah sebuah kamus dengan nama alat sebagai kunci
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
    // TODO panggil alat,

    return {
       content: [{ type: "text", text: `Tool ${name} called with arguments: ${JSON.stringify(input)}, result: ${JSON.stringify(result)}` }]
    };
});
```

Seperti yang anda boleh lihat daripada kod di atas, kita perlu mengurai alat untuk dipanggil, dan dengan argumen apa, dan kemudian kita perlu meneruskan untuk memanggil alat itu.

## Meningkatkan pendekatan dengan pengesahan

Setakat ini, anda telah melihat bagaimana semua pendaftaran anda untuk menambah alat, sumber dan petunjuk boleh digantikan dengan dua pengendali ini bagi setiap jenis ciri. Apa lagi yang perlu kita lakukan? Baiklah, kita harus menambah beberapa bentuk pengesahan untuk memastikan alat dipanggil dengan argumen yang betul. Setiap runtime mempunyai penyelesaian mereka sendiri untuk ini, contohnya Python menggunakan Pydantic dan TypeScript menggunakan Zod. Idéanya adalah bahawa kita melakukan perkara berikut:

- Memindahkan logik untuk mencipta ciri (alat, sumber atau petunjuk) ke folder khususnya.
- Menambah cara untuk mengesahkan permintaan masuk yang meminta misalnya memanggil alat.

### Mencipta ciri

Untuk mencipta ciri, kita perlu membuat fail untuk ciri itu dan pastikan ia mempunyai medan wajib yang diperlukan bagi ciri itu. Medan mana yang berbeza sedikit antara alat, sumber dan petunjuk.

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
        # Sahkan input menggunakan model Pydantic
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # TODO: tambah Pydantic, supaya kita boleh buat AddInputModel dan sahkan args

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

di sini anda boleh lihat bagaimana kami melakukan perkara berikut:

- Cipta skema menggunakan Pydantic `AddInputModel` dengan medan `a` dan `b` dalam fail *schema.py*.
- Cuba mengurai permintaan masuk menjadi jenis `AddInputModel`, jika terdapat ketidakpadanan dalam parameter ini akan gagal:

   ```python
   # add.py
    try:
        # Sahkan input menggunakan model Pydantic
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

- Dalam pengendali yang mengendalikan semua panggilan alat, kami kini cuba mengurai permintaan masuk ke dalam skema yang ditakrifkan oleh alat itu:

    ```typescript
    const Schema = tool.rawSchema;

    try {
       const input = Schema.parse(request.params.arguments);
    ```

    jika itu berjaya maka kami meneruskan untuk memanggil alat sebenar:

    ```typescript
    const result = await tool.callback(input);
    ```

Seperti yang anda lihat, pendekatan ini mewujudkan seni bina yang hebat kerana semuanya ada tempatnya, *server.ts* adalah fail yang sangat kecil yang hanya menyambungkan pengendali permintaan dan setiap ciri ada dalam folder masing-masing iaitu tools/, resources/ atau /prompts.

Bagus, mari kita cuba bina ini seterusnya.

## Latihan: Mencipta pelayan tahap rendah

Dalam latihan ini, kita akan melakukan perkara berikut:

1. Mencipta pelayan tahap rendah yang mengendalikan penyenaraian alat dan pemanggilan alat.
1. Melaksanakan seni bina yang anda boleh bina.
1. Menambah pengesahan untuk memastikan panggilan alat anda disahkan dengan betul.

### -1- Cipta seni bina

Perkara pertama yang perlu kita atasi ialah seni bina yang membantu kita berskala apabila kita menambah lebih banyak ciri, ini adalah bagaimana ia kelihatan:

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

Kini kita telah menetapkan seni bina yang memastikan kita boleh dengan mudah menambah alat baru dalam folder tools. Sila ikut ini untuk menambah subdirektori untuk resources dan prompts.

### -2- Mencipta alat

Mari kita lihat bagaimana mencipta alat kelihatan seterusnya. Pertama, ia perlu dicipta dalam subdirektori *tool* seperti berikut:

**Python**

```python
from .schema import AddInputModel

async def add_handler(args) -> float:
    try:
        # Sahkan input menggunakan model Pydantic
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # TODO: tambah Pydantic, supaya kita boleh buat AddInputModel dan sahkan args

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

Apa yang kita lihat di sini ialah bagaimana kita mentakrifkan nama, penerangan, dan skema input menggunakan Pydantic serta pengendali yang akan dipanggil apabila alat ini dipanggil. Akhir sekali, kami dedahkan `tool_add` yang merupakan kamus memegang semua sifat ini.

Terdapat juga *schema.py* yang digunakan untuk mentakrifkan skema input yang digunakan oleh alat kita:

```python
from pydantic import BaseModel

class AddInputModel(BaseModel):
    a: float
    b: float
```

Kita juga perlu mengisi *__init__.py* untuk memastikan direktori tools dianggap sebagai modul. Selain itu, kita perlu mendedahkan modul dalamnya seperti berikut:

```python
from .add import tool_add

tools = {
  tool_add["name"] : tool_add
}
```

Kita boleh terus menambah pada fail ini semasa kita menambah lebih banyak alat.

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

Di sini kita mencipta kamus yang terdiri daripada sifat:

- name, ini adalah nama alat.
- rawSchema, ini adalah skema Zod, ia akan digunakan untuk mengesahkan permintaan masuk untuk memanggil alat ini.
- inputSchema, skema ini akan digunakan oleh pengendali.
- callback, ini digunakan untuk memanggil alat.

Terdapat juga `Tool` yang digunakan untuk menukar kamus ini kepada jenis yang pengendali pelayan mcp boleh terima dan ia kelihatan seperti berikut:

```typescript
import { z } from 'zod';

export interface Tool {
    name: string;
    inputSchema: any;
    rawSchema: z.ZodTypeAny;
    callback: (args: z.infer<z.ZodTypeAny>) => Promise<{ content: { type: string; text: string }[] }>;
}
```

Dan terdapat *schema.ts* di mana kita menyimpan skema input untuk setiap alat seperti berikut dengan hanya satu skema pada masa ini tetapi apabila kita menambah alat kita boleh menambah lebih banyak entri:

```typescript
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });
```

Bagus, mari kita teruskan dengan mengendalikan penyenaraian alat kita seterusnya.

### -3- Mengendalikan penyenaraian alat

Seterusnya, untuk mengendalikan penyenaraian alat kita, kita perlu menyediakan pengendali permintaan untuk itu. Ini adalah apa yang perlu kita tambah ke fail pelayan kita:

**Python**

```python
# kod dilupakan untuk ringkasan
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

Di sini, kami menambah hiasan `@server.list_tools` dan fungsi pelaksana `handle_list_tools`. Dalam fungsi ini, kita perlu menghasilkan senarai alat. Perhatikan bagaimana setiap alat perlu mempunyai nama, penerangan dan inputSchema.

**TypeScript**

Untuk menyediakan pengendali permintaan bagi penyenaraian alat, kita perlu memanggil `setRequestHandler` pada pelayan dengan skema yang sesuai dengan apa yang kita cuba lakukan, dalam kes ini `ListToolsRequestSchema`.

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
// kod diabaikan untuk ringkasan
import { tools } from './tools/index.js';

server.setRequestHandler(ListToolsRequestSchema, async (request) => {
  // Pulangkan senarai alat yang didaftarkan
  return {
    tools: tools
  };
});
```

Bagus, kini kita telah menyelesaikan bahagian penyenaraian alat, mari lihat bagaimana kita boleh memanggil alat seterusnya.

### -4- Mengendalikan panggilan alat

Untuk memanggil alat, kita perlu menyediakan pengendali permintaan lain, kali ini memfokuskan pada mengendalikan permintaan yang menyatakan ciri mana yang hendak dipanggil dan dengan argumen apa.

**Python**

Mari gunakan hiasan `@server.call_tool` dan laksanakan dengan fungsi seperti `handle_call_tool`. Dalam fungsi itu, kita perlu mengurai nama alat, argumennya dan memastikan argumen itu sah untuk alat berkenaan. Kita boleh sama ada mengesahkan argumen dalam fungsi ini atau di hilir dalam alat sebenar.

```python
@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict[str, str] | None
) -> list[types.TextContent]:
    
    # tools adalah kamus dengan nama alat sebagai kunci
    if name not in tools.tools:
        raise ValueError(f"Unknown tool: {name}")
    
    tool = tools.tools[name]

    result = "default"
    try:
        # gunakan alat tersebut
        result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)
    except Exception as e:
        raise ValueError(f"Error calling tool {name}: {str(e)}")

    return [
        types.TextContent(type="text", text=str(result))
    ]
```

Ini yang berlaku:

- Nama alat kita sudah ada sebagai parameter input `name` yang benar untuk argumen kita dalam bentuk kamus `arguments`.

- Alat dipanggil dengan `result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)`. Pengesahan argumen berlaku dalam sifat `handler` yang menunjuk ke fungsi, jika itu gagal ia akan menaikkan pengecualian.

Jadi, kini kita mempunyai pemahaman penuh tentang penyenaraian dan pemanggilan alat menggunakan pelayan tahap rendah.

Lihat [contoh penuh](./code/README.md) di sini

## Tugasan

Kembangkan kod yang telah anda diberikan dengan beberapa alat, sumber dan petunjuk dan renungkan bagaimana anda perasan bahawa anda hanya perlu menambah fail dalam direktori tools dan tiada tempat lain.

*Tiada penyelesaian diberikan*

## Ringkasan

Dalam bab ini, kita melihat bagaimana pendekatan pelayan tahap rendah berfungsi dan bagaimana ia boleh membantu kita mencipta seni bina yang bagus untuk terus dibina. Kami juga membincangkan pengesahan dan anda telah ditunjukkan cara bekerja dengan perpustakaan pengesahan untuk mencipta skema untuk pengesahan input.

## Apakah seterusnya

- Seterusnya: [Pengesahan Ringkas](../11-simple-auth/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil perhatian bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidakakuratan. Dokumen asal dalam bahasa asalnya hendaklah dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan profesional oleh manusia disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul akibat penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->