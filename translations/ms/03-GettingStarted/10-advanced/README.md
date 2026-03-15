# Penggunaan pelayan lanjutan

Terdapat dua jenis pelayan yang berbeza yang didedahkan dalam MCP SDK, pelayan biasa anda dan pelayan tahap rendah. Biasanya, anda akan menggunakan pelayan biasa untuk menambah ciri-ciri kepadanya. Untuk beberapa kes pula, anda ingin bergantung pada pelayan tahap rendah seperti:

- Seni bina yang lebih baik. Adalah mungkin untuk mencipta seni bina yang bersih dengan kedua-dua pelayan biasa dan pelayan tahap rendah tetapi boleh dipertikaikan bahawa ia sedikit lebih mudah dengan pelayan tahap rendah.
- Ketersediaan ciri. Sesetengah ciri lanjutan hanya boleh digunakan dengan pelayan tahap rendah. Anda akan melihat ini dalam bab-bab kemudian semasa kami menambah pensampelan dan elicitation.

## Pelayan biasa vs pelayan tahap rendah

Inilah bagaimana penciptaan MCP Server kelihatan dengan pelayan biasa

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

Tujuannya ialah anda secara eksplisit menambah setiap alat, sumber atau prompt yang anda mahu pelayan miliki. Tiada masalah dengan itu.

### Pendekatan pelayan tahap rendah

Walau bagaimanapun, apabila anda menggunakan pendekatan pelayan tahap rendah anda perlu berfikir secara berbeza. Daripada mendaftar setiap alat, anda sebaliknya mencipta dua pengendali untuk setiap jenis ciri (alat, sumber atau prompt). Jadi contohnya alat hanya mempunyai dua fungsi seperti berikut:

- Menyenaraikan semua alat. Satu fungsi bertanggungjawab untuk semua percubaan untuk menyenaraikan alat.
- mengendalikan panggilan semua alat. Di sini juga, hanya ada satu fungsi mengendalikan panggilan kepada alat.

Nampaknya ini mungkin kerja yang kurang, bukan? Jadi daripada mendaftar alat, saya hanya perlu pastikan alat itu disenaraikan apabila saya menyenaraikan semua alat dan ia dipanggil apabila ada permintaan masuk untuk memanggil alat.

Mari kita lihat bagaimana kod itu sekarang kelihatan:

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
  // Pulangkan senarai alat yang didaftarkan
  return {
    tools: [{
        name="add",
        description="Add two numbers",
        inputSchema={
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

Di sini kita sekarang mempunyai fungsi yang mengembalikan senarai ciri. Setiap entri dalam senarai alat kini mempunyai medan seperti `name`, `description` dan `inputSchema` untuk mematuhi jenis pulangan. Ini membolehkan kita meletakkan alat dan definisi ciri kita di tempat lain. Kita kini boleh mencipta semua alat kita dalam folder alat dan begitu juga untuk semua ciri anda supaya projek anda boleh terus diatur seperti berikut:

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

Itu hebat, seni bina kita boleh dibuat kelihatan cukup bersih.

Bagaimana pula dengan memanggil alat, adakah ia idea yang sama, satu pengendali untuk memanggil alat, alat mana-mana? Ya, tepat, ini adalah kod untuk itu:

**Python**

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

Seperti yang anda lihat dari kod di atas, kita perlu menguraikan alat yang hendak dipanggil, dan dengan hujah apa, dan kemudian kita perlu terus memanggil alat tersebut.

## Memperbaiki pendekatan dengan pengesahan

Sejauh ini, anda telah melihat bagaimana semua pendaftaran anda untuk menambah alat, sumber dan prompt boleh digantikan dengan dua pengendali ini setiap jenis ciri. Apa lagi yang perlu kita lakukan? Baiklah, kita patut menambah sesuatu bentuk pengesahan untuk memastikan alat itu dipanggil dengan hujah yang betul. Setiap runtime mempunyai penyelesaian mereka sendiri untuk ini, contohnya Python menggunakan Pydantic dan TypeScript menggunakan Zod. Idenya adalah kita melakukan yang berikut:

- Pindahkan logik untuk mencipta ciri (alat, sumber atau prompt) ke folder khasnya.
- Tambah cara untuk mengesahkan permintaan masuk yang memohon contohnya untuk memanggil alat.

### Cipta ciri

Untuk mencipta ciri, kita perlu mencipta fail untuk ciri tersebut dan pastikan ia mempunyai medan wajib yang diperlukan oleh ciri itu. Medan yang berbeza sedikit antara alat, sumber dan prompt.

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

    # TODO: tambah Pydantic, supaya kita boleh buat AddInputModel dan sahkan argumen

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

di sini anda boleh lihat bagaimana kita melakukan yang berikut:

- Cipta skema menggunakan Pydantic `AddInputModel` dengan medan `a` dan `b` dalam fail *schema.py*.
- Cuba menguraikan permintaan masuk supaya menjadi jenis `AddInputModel`, jika terdapat ketidakpadanan dalam parameter ini akan menyebabkan ralat:

   ```python
   # add.py
    try:
        # Sahkan input menggunakan model Pydantic
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")
   ```

Anda boleh memilih untuk meletakkan logik penguraian ini di dalam panggilan alat itu sendiri atau dalam fungsi pengendali.

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

- Dalam pengendali yang mengendalikan semua panggilan alat, kita kini cuba menguraikan permintaan masuk ke dalam skema yang ditakrifkan alat:

    ```typescript
    const Schema = tool.rawSchema;

    try {
       const input = Schema.parse(request.params.arguments);
    ```

    jika itu berjaya maka kita terus memanggil alat sebenar:

    ```typescript
    const result = await tool.callback(input);
    ```

Seperti yang anda lihat, pendekatan ini mewujudkan seni bina yang hebat kerana semuanya ada tempatnya, *server.ts* adalah fail yang sangat kecil yang hanya menghubungkan pengendali permintaan dan setiap ciri berada dalam folder mereka masing-masing iaitu tools/, resources/ atau /prompts.

Hebat, mari kita cuba bina ini seterusnya.

## Latihan: Mencipta pelayan tahap rendah

Dalam latihan ini, kita akan melakukan yang berikut:

1. Cipta pelayan tahap rendah yang mengendalikan penyenaraian alat dan pemanggilan alat.
1. Laksanakan seni bina yang anda boleh bina terus.
1. Tambah pengesahan untuk memastikan panggilan alat anda disahkan dengan betul.

### -1- Cipta seni bina

Perkara pertama yang perlu kita tangani ialah seni bina yang membantu kita skala apabila kita menambah lebih banyak ciri, begini rupanya:

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

Kini kita telah menyediakan seni bina yang memastikan kita boleh mudah menambah alat baru dalam folder alat. Sila ikut ini untuk menambah subdirektori bagi sumber dan prompt.

### -2- Mencipta alat

Mari lihat bagaimana mencipta alat seterusnya. Pertama, ia perlu dicipta dalam subdirektori *tool* seperti berikut:

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

Apa yang kita lihat di sini adalah bagaimana kita mentakrifkan nama, penerangan, dan skema input menggunakan Pydantic dan pengendali yang akan dipanggil apabila alat ini dipanggil. Akhir sekali, kita dedahkan `tool_add` yang merupakan kamus yang memegang semua sifat ini.

Ada juga *schema.py* yang digunakan untuk mentakrifkan skema input yang digunakan oleh alat kita:

```python
from pydantic import BaseModel

class AddInputModel(BaseModel):
    a: float
    b: float
```

Kita juga perlu mengisi *__init__.py* untuk memastikan direktori alat diperlakukan sebagai modul. Selain itu, kita perlu dedahkan modul di dalamnya seperti berikut:

```python
from .add import tool_add

tools = {
  tool_add["name"] : tool_add
}
```

Kita boleh terus menambah dalam fail ini apabila kita menambah lebih banyak alat.

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

Di sini kita mencipta kamus yang mengandungi sifat:

- name, ini ialah nama alat.
- rawSchema, ini adalah skema Zod, ia akan digunakan untuk mengesahkan permintaan masuk untuk memanggil alat ini.
- inputSchema, skema ini akan digunakan oleh pengendali.
- callback, ini digunakan untuk memanggil alat.

Ada juga `Tool` yang digunakan untuk menukar kamus ini menjadi jenis yang boleh diterima oleh pengendali pelayan mcp dan ia kelihatan seperti berikut:

```typescript
import { z } from 'zod';

export interface Tool {
    name: string;
    inputSchema: any;
    rawSchema: z.ZodTypeAny;
    callback: (args: z.infer<z.ZodTypeAny>) => Promise<{ content: { type: string; text: string }[] }>;
}
```

Dan ada *schema.ts* di mana kita menyimpan skema input untuk setiap alat yang kelihatan seperti ini dengan hanya satu skema buat masa sekarang tapi apabila kita menambah alat kita boleh tambah lebih banyak entri:

```typescript
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });
```

Hebat, mari kita teruskan untuk mengendalikan penyenaraian alat kita seterusnya.

### -3- Mengendalikan penyenaraian alat

Seterusnya, untuk mengendalikan penyenaraian alat kita, kita perlu menyediakan pengendali permintaan untuk itu. Berikut adalah apa yang perlu kita tambah ke fail pelayan kita:

**Python**

```python
# kod diabaikan untuk ringkasan
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

Di sini, kita tambah dekorator `@server.list_tools` dan fungsi pelaksanaan `handle_list_tools`. Dalam yang terakhir, kita perlu menghasilkan senarai alat. Perhatikan setiap alat perlu mempunyai nama, penerangan dan inputSchema.

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
// kod diabaikan untuk ringkasan
import { tools } from './tools/index.js';

server.setRequestHandler(ListToolsRequestSchema, async (request) => {
  // Kembalikan senarai alat yang berdaftar
  return {
    tools: tools
  };
});
```

Hebat, kini kita telah menyelesaikan bahagian penyenaraian alat, mari lihat bagaimana kita boleh memanggil alat seterusnya.

### -4- Mengendalikan panggilan alat

Untuk memanggil alat, kita perlu menyediakan satu lagi pengendali permintaan, kali ini yang fokus pada mengendalikan permintaan yang menentukan ciri mana hendak dipanggil dan dengan hujah apa.

**Python**

Mari gunakan dekorator `@server.call_tool` dan laksanakan dengan fungsi seperti `handle_call_tool`. Dalam fungsi itu, kita perlu menguraikan nama alat, hujahnya dan pastikan hujah tersebut sah untuk alat yang dimaksudkan. Kita boleh sama ada sahkan hujah dalam fungsi ini atau dalam alat sebenar.

```python
@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict[str, str] | None
) -> list[types.TextContent]:
    
    # tools ialah satu kamus dengan nama alat sebagai kunci
    if name not in tools.tools:
        raise ValueError(f"Unknown tool: {name}")
    
    tool = tools.tools[name]

    result = "default"
    try:
        # panggil alat tersebut
        result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)
    except Exception as e:
        raise ValueError(f"Error calling tool {name}: {str(e)}")

    return [
        types.TextContent(type="text", text=str(result))
    ] 
```

Ini yang berlaku:

- Nama alat kita sudah sedia ada sebagai parameter input `name` yang juga benar untuk hujah kita dalam bentuk kamus `arguments`.

- Alat dipanggil dengan `result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)`. Pengesahan hujah berlaku dalam sifat `handler` yang menunjuk ke fungsi, jika gagal ia akan mengeluarkan pengecualian.

Di situ, kini kita mempunyai kefahaman penuh tentang penyenaraian dan pemanggilan alat menggunakan pelayan tahap rendah.

Lihat [contoh penuh](./code/README.md) di sini

## Tugasan

Perluaskan kod yang telah diberikan dengan beberapa alat, sumber dan prompt dan fikirkan bagaimana anda perasan bahawa anda hanya perlu menambah fail dalam direktori alat dan tidak di tempat lain.

*Tiada penyelesaian diberikan*

## Rumusan

Dalam bab ini, kita melihat bagaimana pendekatan pelayan tahap rendah berfungsi dan bagaimana ia boleh membantu kita mencipta seni bina yang kemas yang boleh terus kita bina. Kita juga membincangkan pengesahan dan anda telah ditunjukkan bagaimana bekerja dengan perpustakaan pengesahan untuk mencipta skema bagi pengesahan input.

## Apa seterusnya

- Seterusnya: [Pengesahan Mudah](../11-simple-auth/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan profesional oleh manusia adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->