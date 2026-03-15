# Penggunaan server tingkat lanjut

Ada dua jenis server berbeda yang disediakan dalam MCP SDK, server normal Anda dan server tingkat rendah. Biasanya, Anda akan menggunakan server reguler untuk menambahkan fitur ke dalamnya. Namun dalam beberapa kasus, Anda ingin mengandalkan server tingkat rendah seperti:

- Arsitektur yang lebih baik. Mungkin untuk membuat arsitektur yang bersih dengan server reguler dan server tingkat rendah namun bisa dikatakan bahwa itu sedikit lebih mudah dengan server tingkat rendah.
- Ketersediaan fitur. Beberapa fitur lanjutan hanya dapat digunakan dengan server tingkat rendah. Anda akan melihat ini di bab berikutnya ketika kami menambahkan sampling dan elicitation.

## Server reguler vs server tingkat rendah

Berikut adalah bagaimana penciptaan MCP Server terlihat dengan server reguler

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

Intinya adalah Anda secara eksplisit menambahkan setiap alat, sumber daya, atau prompt yang Anda ingin server miliki. Tidak ada yang salah dengan itu.

### Pendekatan server tingkat rendah

Namun, ketika Anda menggunakan pendekatan server tingkat rendah Anda perlu berpikir secara berbeda. Alih-alih mendaftarkan setiap alat, Anda membuat dua handler per jenis fitur (alat, sumber daya, atau prompt). Jadi misalnya alat hanya memiliki dua fungsi seperti:

- Mendaftar semua alat. Satu fungsi akan bertanggung jawab atas semua upaya untuk mendaftar alat.
- Menangani pemanggilan semua alat. Di sini juga, hanya ada satu fungsi yang menangani panggilan ke alat.

Kedengarannya seperti pekerjaan yang lebih sedikit ya? Jadi alih-alih mendaftarkan alat, saya hanya perlu memastikan alat terdaftar saat saya mendaftar semua alat dan dipanggil ketika ada permintaan masuk untuk memanggil alat.

Mari kita lihat bagaimana kode sekarang terlihat:

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
  // Kembalikan daftar alat yang terdaftar
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

Sekarang kami memiliki fungsi yang mengembalikan daftar fitur. Setiap entri dalam daftar alat sekarang memiliki bidang seperti `name`, `description` dan `inputSchema` untuk mematuhi tipe kembalian. Ini memungkinkan kita untuk meletakkan alat dan definisi fitur di tempat lain. Kita sekarang dapat membuat semua alat kita di folder tools dan hal yang sama berlaku untuk semua fitur Anda sehingga proyek Anda dapat diatur seperti ini:

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

Bagus, arsitektur kita bisa dibuat tampak cukup bersih.

Bagaimana dengan memanggil alat, apakah idenya sama, satu handler untuk memanggil alat, alat mana pun? Ya, benar sekali, ini kodenya:

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

Seperti yang Anda lihat dari kode di atas, kita perlu mengurai alat yang akan dipanggil, dan dengan argumen apa, lalu kita perlu melanjutkan untuk memanggil alat tersebut.

## Memperbaiki pendekatan dengan validasi

Sejauh ini, Anda telah melihat bagaimana semua pendaftaran untuk menambahkan alat, sumber daya dan prompt dapat digantikan dengan dua handler per jenis fitur ini. Apa lagi yang perlu kita lakukan? Nah, kita harus menambahkan semacam validasi untuk memastikan alat dipanggil dengan argumen yang benar. Setiap runtime memiliki solusi sendiri untuk ini, misalnya Python menggunakan Pydantic dan TypeScript menggunakan Zod. Idenya adalah kita melakukan hal berikut:

- Memindahkan logika pembuatan fitur (alat, sumber daya, atau prompt) ke folder khususnya.
- Menambahkan cara untuk memvalidasi permintaan masuk yang misalnya meminta memanggil alat.

### Membuat fitur

Untuk membuat fitur, kita perlu membuat file untuk fitur tersebut dan pastikan memiliki bidang wajib yang diperlukan fitur tersebut. Bidang mana saja yang berbeda sedikit antara alat, sumber daya dan prompt.

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

    # TODO: tambahkan Pydantic, sehingga kita bisa membuat AddInputModel dan memvalidasi argumen

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

di sini Anda bisa lihat bagaimana kita melakukan hal berikut:

- Membuat skema menggunakan Pydantic `AddInputModel` dengan bidang `a` dan `b` di file *schema.py*.
- Mencoba mengurai permintaan masuk menjadi tipe `AddInputModel`, jika ada ketidakcocokan parameter ini akan menyebabkan crash:

   ```python
   # add.py
    try:
        # Validasi input menggunakan model Pydantic
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")
   ```

Anda bisa memilih apakah meletakkan logika parsing ini di pemanggilan alat itu sendiri atau di fungsi handler.

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

- Dalam handler yang menangani semua panggilan alat, kita sekarang mencoba memparse permintaan masuk ke dalam skema yang didefinisikan alat:

    ```typescript
    const Schema = tool.rawSchema;

    try {
       const input = Schema.parse(request.params.arguments);
    ```

    jika berhasil maka kita lanjut memanggil alat sebenarnya:

    ```typescript
    const result = await tool.callback(input);
    ```

Seperti yang Anda lihat, pendekatan ini menciptakan arsitektur yang baik karena segala sesuatu memiliki tempatnya, *server.ts* adalah file yang sangat kecil yang hanya menghubungkan handler permintaan dan setiap fitur ada di foldernya masing-masing yaitu tools/, resources/ atau prompts/.

Bagus, mari kita coba membangun ini selanjutnya.

## Latihan: Membuat server tingkat rendah

Dalam latihan ini, kita akan melakukan hal berikut:

1. Membuat server tingkat rendah yang menangani listing alat dan pemanggilan alat.
1. Mengimplementasikan arsitektur yang dapat Anda bangun di atasnya.
1. Menambahkan validasi untuk memastikan pemanggilan alat Anda tervalidasi dengan baik.

### -1- Membuat arsitektur

Hal pertama yang perlu kita bahas adalah arsitektur yang membantu kita skalakan saat menambahkan fitur lebih banyak, berikut tampilannya:

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

Sekarang kita sudah mengatur arsitektur yang memastikan kita dapat dengan mudah menambahkan alat baru di folder tools. Silakan ikuti ini untuk menambahkan subdirektori untuk resources dan prompts.

### -2- Membuat alat

Mari lihat bagaimana membuat alat terlihat. Pertama, harus dibuat di subdirektori *tool* seperti ini:

**Python**

```python
from .schema import AddInputModel

async def add_handler(args) -> float:
    try:
        # Validasi input menggunakan model Pydantic
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # TODO: tambahkan Pydantic, agar kita dapat membuat AddInputModel dan memvalidasi args

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

Yang kita lihat di sini adalah cara mendefinisikan name, description, dan input schema menggunakan Pydantic serta handler yang akan dipanggil saat alat ini dipanggil. Terakhir, kita mengekspos `tool_add` yang merupakan dictionary yang memuat semua properti ini.

Ada juga *schema.py* yang digunakan untuk mendefinisikan skema input yang digunakan oleh alat kita:

```python
from pydantic import BaseModel

class AddInputModel(BaseModel):
    a: float
    b: float
```

Kita juga perlu mengisi *__init__.py* untuk memastikan direktori tools dianggap sebagai modul. Selain itu, kita perlu mengekspos modul di dalamnya seperti ini:

```python
from .add import tool_add

tools = {
  tool_add["name"] : tool_add
}
```

Kita bisa terus menambahkan file ini saat menambah alat baru.

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

Di sini kita membuat dictionary yang berisi properti:

- name, ini adalah nama alat.
- rawSchema, ini adalah skema Zod, akan digunakan untuk memvalidasi permintaan masuk untuk memanggil alat ini.
- inputSchema, skema ini akan digunakan oleh handler.
- callback, ini digunakan untuk memanggil alat.

Ada juga `Tool` yang digunakan untuk mengonversi dictionary ini menjadi tipe yang dapat diterima oleh handler server mcp dan ini tampilannya seperti:

```typescript
import { z } from 'zod';

export interface Tool {
    name: string;
    inputSchema: any;
    rawSchema: z.ZodTypeAny;
    callback: (args: z.infer<z.ZodTypeAny>) => Promise<{ content: { type: string; text: string }[] }>;
}
```

Dan ada *schema.ts* di mana kita menyimpan skema input untuk setiap alat yang tampilannya seperti ini dengan hanya satu skema saat ini tapi saat menambah alat kita bisa menambah entri lebih banyak:

```typescript
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });
```

Bagus, mari kita lanjut menangani listing alat kita selanjutnya.

### -3- Menangani listing alat

Selanjutnya, untuk menangani listing alat kita perlu mengatur request handler untuk itu. Berikut yang perlu kita tambahkan ke file server:

**Python**

```python
# kode dihilangkan demi ringkasnya
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

Di sini, kita menambahkan dekorator `@server.list_tools` dan fungsi implementasi `handle_list_tools`. Dalam fungsi ini kita perlu menghasilkan daftar alat. Perhatikan bagaimana setiap alat harus memiliki name, description dan inputSchema.

**TypeScript**

Untuk mengatur request handler untuk listing alat, kita perlu memanggil `setRequestHandler` pada server dengan skema yang sesuai tujuan kita, dalam kasus ini `ListToolsRequestSchema`.

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

Bagus, sekarang kita sudah menyelesaikan bagian listing alat, mari lihat bagaimana kita bisa memanggil alat selanjutnya.

### -4- Menangani pemanggilan alat

Untuk memanggil alat, kita perlu mengatur request handler lain, kali ini berfokus pada menangani permintaan yang menentukan fitur mana yang akan dipanggil dan dengan argumen apa.

**Python**

Mari gunakan dekorator `@server.call_tool` dan implementasikan dengan fungsi seperti `handle_call_tool`. Dalam fungsi itu, kita perlu mengurai nama alat, argumen, dan memastikan argumen valid untuk alat tersebut. Kita bisa memvalidasi argumen ini di fungsi ini atau di alat sebenarnya.

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

- Nama alat kita sudah hadir sebagai parameter input `name` yang juga benar untuk argumen kita dalam bentuk dictionary `arguments`.

- Alat dipanggil dengan `result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)`. Validasi argumen terjadi dalam properti `handler` yang merujuk ke fungsi, jika gagal maka akan melempar pengecualian.

Nah, sekarang kita memiliki pemahaman lengkap tentang listing dan pemanggilan alat menggunakan server tingkat rendah.

Lihat [contoh lengkap](./code/README.md) di sini

## Tugas

Kembangkan kode yang telah Anda dapatkan dengan sejumlah alat, sumber daya dan prompt lalu refleksikan bagaimana Anda hanya perlu menambahkan file di direktori tools dan tidak di tempat lain.

*Tidak ada solusi diberikan*

## Ringkasan

Di bab ini, kita melihat bagaimana pendekatan server tingkat rendah bekerja dan bagaimana itu dapat membantu kita membuat arsitektur bagus yang terus bisa kita kembangkan. Kita juga membahas validasi dan Anda melihat bagaimana bekerja dengan perpustakaan validasi untuk membuat skema validasi input.

## Selanjutnya

- Selanjutnya: [Simple Authentication](../11-simple-auth/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penolakan**:
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk memberikan terjemahan yang akurat, harap diingat bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sahih. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau kesalahan tafsir yang timbul akibat penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->