# Penggunaan server tingkat lanjut

Ada dua jenis server yang diekspos dalam MCP SDK, server normal Anda dan server tingkat rendah. Biasanya, Anda akan menggunakan server reguler untuk menambahkan fitur. Namun dalam beberapa kasus, Anda ingin mengandalkan server tingkat rendah seperti:

- Arsitektur yang lebih baik. Dimungkinkan untuk membuat arsitektur yang bersih dengan server reguler dan server tingkat rendah, tapi bisa dikatakan sedikit lebih mudah dengan server tingkat rendah.
- Ketersediaan fitur. Beberapa fitur lanjutan hanya bisa digunakan dengan
    server tingkat rendah. Bab berikutnya membahas Elicitation dan fitur legacy Sampling,
    yang sudah tidak digunakan lagi di MCP `2026-07-28`.

## Server reguler vs server tingkat rendah

Berikut adalah cara pembuatan MCP Server dengan server reguler

**Python**

```python
mcp = FastMCP("Demo")

# Tambahkan alat penjumlahan
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

// Tambahkan alat penjumlahan
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

Intinya adalah Anda secara eksplisit menambahkan setiap alat, sumber daya, atau prompt yang ingin server miliki. Tidak ada yang salah dengan itu.  

### Pendekatan server tingkat rendah

Namun, saat menggunakan pendekatan server tingkat rendah Anda perlu berpikir berbeda. Alih-alih mendaftarkan setiap alat, Anda membuat dua handler per tipe fitur (alat, sumber daya, atau prompt). Misalnya alat hanya memiliki dua fungsi seperti berikut:

- Daftar semua alat. Satu fungsi bertanggung jawab untuk semua upaya dalam mendaftar alat.
- Menangani pemanggilan alat. Di sini juga, hanya ada satu fungsi yang menangani panggilan ke alat.

Kedengarannya seperti pekerjaan yang lebih ringan kan? Jadi daripada mendaftarkan alat, saya hanya perlu memastikan alat itu terdaftar saat saya mendaftar semua alat dan bahwa alat itu dipanggil saat ada permintaan masuk untuk memanggil alat itu. 

Mari kita lihat seperti apa kode sekarang:

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
  // Mengembalikan daftar alat yang terdaftar
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

Sekarang kita memiliki fungsi yang mengembalikan daftar fitur. Setiap entri dalam daftar alat sekarang memiliki bidang seperti `name`, `description`, dan `inputSchema` sesuai dengan tipe kembalian. Ini memungkinkan kita untuk menempatkan definisi alat dan fitur kita di tempat lain. Kita sekarang bisa membuat semua alat di folder tools dan hal yang sama berlaku untuk semua fitur Anda sehingga proyek Anda tiba-tiba bisa terorganisir seperti ini:

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

Bagus, arsitektur kita bisa dibuat cukup bersih.

Bagaimana dengan pemanggilan alat, apakah idenya sama, satu handler untuk memanggil alat, alat mana saja? Ya, tepat sekali, inilah kodenya:

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

Seperti yang Anda lihat dari kode di atas, kita perlu mem-parsing alat yang akan dipanggil, dan dengan argumen apa, kemudian kita harus melanjutkan untuk memanggil alat itu.

## Meningkatkan pendekatan dengan validasi

Sampai saat ini, Anda telah melihat bagaimana semua pendaftaran alat, sumber daya, dan prompt dapat digantikan dengan dua handler per tipe fitur ini. Apa lagi yang perlu kita lakukan? Nah, kita harus menambahkan beberapa bentuk validasi untuk memastikan alat dipanggil dengan argumen yang benar. Setiap runtime punya solusinya sendiri untuk ini, misalnya Python menggunakan Pydantic dan TypeScript menggunakan Zod. Idenya kita melakukan hal berikut:

- Pindahkan logika pembuatan fitur (alat, sumber daya atau prompt) ke folder khususnya.
- Tambahkan cara untuk memvalidasi permintaan masuk misalnya untuk memanggil alat.

### Membuat fitur

Untuk membuat fitur, kita perlu membuat file untuk fitur itu dan memastikan memiliki bidang wajib yang diperlukan fitur tersebut. Bidang ini sedikit berbeda antara alat, sumber daya, dan prompt.

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
        # Validasi input menggunakan model Pydantic
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # TODO: tambahkan Pydantic, sehingga kita dapat membuat AddInputModel dan memvalidasi args

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

Di sini Anda dapat melihat bagaimana kita melakukan hal berikut:

- Membuat schema menggunakan Pydantic `AddInputModel` dengan bidang `a` dan `b` di file *schema.py*.
- Mencoba mem-parsing permintaan masuk untuk menjadi tipe `AddInputModel`, jika parameter tidak cocok ini akan gagal:

   ```python
   # add.py
    try:
        # Validasi input menggunakan model Pydantic
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")
   ```

Anda bisa memilih untuk menaruh logika parsing ini di panggilan alat itu sendiri atau di fungsi handler.

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

- Di handler yang menangani semua panggilan alat, kita mencoba mem-parsing permintaan masuk ke schema yang didefinisikan alat:

    ```typescript
    const Schema = tool.rawSchema;

    try {
       const input = Schema.parse(request.params.arguments);
    ```

    jika berhasil kita lanjutkan untuk memanggil alat yang sebenarnya:

    ```typescript
    const result = await tool.callback(input);
    ```

Seperti yang Anda lihat, pendekatan ini menciptakan arsitektur yang bagus karena semuanya memiliki tempatnya, *server.ts* adalah file yang sangat kecil yang hanya menyambungkan handler permintaan dan setiap fitur terdapat di foldernya masing-masing yaitu tools/, resources/ atau /prompts.

Bagus, mari kita coba bangun ini selanjutnya.

## Latihan: Membuat server tingkat rendah

Dalam latihan ini, kita akan melakukan hal berikut:

1. Membuat server tingkat rendah yang menangani listing alat dan pemanggilan alat.
1. Menerapkan arsitektur yang bisa Anda bangun lebih lanjut.
1. Menambahkan validasi untuk memastikan panggilan alat Anda tervalidasi dengan benar.

### -1- Membuat arsitektur

Hal pertama yang perlu kita tangani adalah arsitektur yang membantu kita skala saat menambahkan lebih banyak fitur, berikut tampilannya:

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

Sekarang kita telah menyiapkan arsitektur yang memastikan kita dapat dengan mudah menambahkan alat baru di folder tools. Silakan ikuti ini untuk menambahkan subdirektori untuk resources dan prompts.

### -2- Membuat alat

Mari kita lihat bagaimana membuat alat berikutnya. Pertama, alat harus dibuat di subdirektori *tool* seperti ini:

**Python**

```python
from .schema import AddInputModel

async def add_handler(args) -> float:
    try:
        # Validasi input menggunakan model Pydantic
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # TODO: tambahkan Pydantic, sehingga kita dapat membuat AddInputModel dan memvalidasi args

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

Yang kita lihat di sini adalah bagaimana kita mendefinisikan nama, deskripsi, dan schema input menggunakan Pydantic serta handler yang akan dipanggil saat alat ini dipanggil. Terakhir, kita mengekspos `tool_add` yang merupakan kamus yang menyimpan semua properti ini.

Ada juga *schema.py* yang digunakan untuk mendefinisikan schema input yang digunakan oleh alat kita:

```python
from pydantic import BaseModel

class AddInputModel(BaseModel):
    a: float
    b: float
```

Kita juga perlu mengisi *__init__.py* untuk memastikan direktori tools diperlakukan sebagai modul. Selain itu, kita harus mengekspos modul-modul di dalamnya seperti ini:

```python
from .add import tool_add

tools = {
  tool_add["name"] : tool_add
}
```

Kita bisa terus menambahkan ke file ini saat kita menambah alat-alat baru.

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

Di sini kita membuat kamus yang berisi properti:

- name, yaitu nama alat.
- rawSchema, yaitu schema Zod, ini akan digunakan untuk memvalidasi permintaan masuk yang memanggil alat ini.
- inputSchema, schema ini akan digunakan oleh handler.
- callback, ini digunakan untuk memanggil alat.

Ada juga `Tool` yang digunakan untuk mengubah kamus ini menjadi tipe yang dapat diterima oleh handler server mcp dan tampilannya seperti ini:

```typescript
import { z } from 'zod';

export interface Tool {
    name: string;
    inputSchema: any;
    rawSchema: z.ZodTypeAny;
    callback: (args: z.infer<z.ZodTypeAny>) => Promise<{ content: { type: string; text: string }[] }>;
}
```

Dan ada *schema.ts* tempat kita menyimpan schema input untuk setiap alat dengan tampilan seperti ini yang saat ini hanya ada satu schema tapi saat kita menambah alat, kita bisa menambah lebih banyak entri:

```typescript
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });
```

Bagus, mari kita lanjutkan untuk menangani daftar alat kita berikutnya.

### -3- Menangani daftar alat

Selanjutnya, untuk menangani daftar alat, kita perlu menyiapkan handler permintaan untuk itu. Berikut yang perlu kita tambahkan ke file server kita:

**Python**

```python
# kode dihilangkan untuk singkatnya
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

Di sini, kita menambahkan dekorator `@server.list_tools` dan fungsi implementasi `handle_list_tools`. Di fungsi ini, kita harus menghasilkan daftar alat. Perhatikan bahwa setiap alat harus memiliki nama, deskripsi, dan inputSchema.   

**TypeScript**

Untuk menyiapkan handler permintaan untuk daftar alat, kita perlu memanggil `setRequestHandler` pada server dengan schema yang sesuai dengan yang kita coba lakukan, dalam kasus ini `ListToolsRequestSchema`. 

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
// kode dihilangkan untuk ringkasan
import { tools } from './tools/index.js';

server.setRequestHandler(ListToolsRequestSchema, async (request) => {
  // Mengembalikan daftar alat yang terdaftar
  return {
    tools: tools
  };
});
```

Bagus, sekarang kita telah menyelesaikan bagian daftar alat, mari lihat bagaimana kita bisa memanggil alat selanjutnya.

### -4- Menangani pemanggilan alat

Untuk memanggil alat, kita perlu menyiapkan handler permintaan lain, kali ini fokus pada menangani permintaan yang menentukan fitur mana yang akan dipanggil dan dengan argumen apa.

**Python**

Mari gunakan dekorator `@server.call_tool` dan implementasikan dengan fungsi seperti `handle_call_tool`. Dalam fungsi ini, kita harus mem-parsing nama alat, argumennya dan memastikan argumen valid untuk alat yang dimaksud. Kita bisa validasi argumen di fungsi ini atau di bagian alat itu sendiri.

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
        # panggil alat tersebut
        result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)
    except Exception as e:
        raise ValueError(f"Error calling tool {name}: {str(e)}")

    return [
        types.TextContent(type="text", text=str(result))
    ]
```

Ini yang terjadi:

- Nama alat kita sudah ada sebagai parameter input `name` yang juga benar untuk argumen kita dalam bentuk kamus `arguments`.

- Alat dipanggil dengan `result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)`. Validasi argumen terjadi di properti `handler` yang menunjuk ke fungsi, jika gagal akan memunculkan pengecualian. 

Nah, sekarang kita telah memahami sepenuhnya daftar dan pemanggilan alat menggunakan server tingkat rendah.

Lihat [contoh lengkap](./code/README.md) di sini

## Tugas

Kembangkan kode yang sudah diberikan dengan sejumlah alat, sumber daya, dan prompt dan renungkan bagaimana Anda hanya perlu menambahkan file di direktori tools dan di tempat lain tidak diperlukan. 

*Tidak ada solusi diberikan*

## Ringkasan

Dalam bab ini, kita melihat bagaimana pendekatan server tingkat rendah bekerja dan bagaimana itu dapat membantu kita membuat arsitektur yang bagus untuk terus dikembangkan. Kita juga membahas validasi dan Anda diperlihatkan cara bekerja dengan pustaka validasi untuk membuat schema validasi input.

## Selanjutnya

- Selanjutnya: [Otentikasi Sederhana](../11-simple-auth/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk mencapai akurasi, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sah. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->