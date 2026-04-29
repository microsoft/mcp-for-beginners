# Gelişmiş sunucu kullanımı

MCP SDK'da iki farklı türde sunucu bulunmaktadır: normal sunucunuz ve düşük seviyeli sunucu. Normalde, özellik eklemek için normal sunucuyu kullanırsınız. Ancak bazı durumlarda, şunlar gibi düşük seviyeli sunucuya güvenmek istersiniz:

- Daha iyi mimari. Hem normal sunucu hem de düşük seviyeli sunucu ile temiz bir mimari oluşturmak mümkündür, ancak düşük seviyeli sunucu ile biraz daha kolay olduğu söylenebilir.
- Özellik kullanılabilirliği. Bazı gelişmiş özellikler yalnızca düşük seviyeli sunucu ile kullanılabilir. Bunları daha sonraki bölümlerde örneklerle göreceğiz, örneğin örnekleme ve çağrı eklerken.

## Normal sunucu ve düşük seviyeli sunucu arasındaki fark

MCP Sunucusu oluşturmak normal sunucu ile şu şekilde görünür:

**Python**

```python
mcp = FastMCP("Demo")

# Bir toplama aracı ekleyin
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

// Bir toplama aracı ekle
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

Buradaki nokta, sunucuda olmasını istediğiniz her araç, kaynak veya istemi açıkça eklemenizdir. Bununla ilgili bir sorun yok.

### Düşük seviyeli sunucu yaklaşımı

Ancak düşük seviyeli sunucu yaklaşımını kullandığınızda, bunu farklı düşünmeniz gerekir. Her aracı kayıt etmek yerine, her özellik türü (araçlar, kaynaklar veya istemler) için iki işleyici oluşturursunuz. Örneğin, araçlar için sadece iki fonksiyonunuz olur:

- Tüm araçları listelemek. Bütün araç listesini almak için tek bir fonksiyon sorumludur.
- Tüm araçların çağrılmasını işlemek. Burada da, araç çağrılarını işleyen tek bir fonksiyon vardır.

Bu potansiyel olarak daha az iş gibi görünüyor, değil mi? Yani bir aracı kayıt etmek yerine, tüm araçları listelerken aracın listelenmesini ve bir araç çağrısı talebi geldiğinde çağrılmasını sağlamak yeterli.

Kodun şimdi nasıl göründüğüne bakalım:

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
  // Kayıtlı araçların listesini döndürür
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

Burada, özellikleri listeleyen bir fonksiyonumuz var. Araçlar listesindeki her giriş artık `name`, `description` ve `inputSchema` gibi alanları içeriyor ve bu da dönen tipe uymayı sağlıyor. Bu sayede araçlarımızı ve özellik tanımını başka bir yerde tutabiliriz. Artık tüm araçlarımızı tools klasöründe oluşturabiliriz ve aynı şey tüm özellikler için geçerli olduğundan projeniz şu şekilde organize olabilir:

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

Harika, mimarimiz oldukça temiz görünebilir.

Araç çağırma nasıl oluyor, aynı fikir mi, bir işleyici tüm araçları mı çağırıyor? Evet, aynen öyle. İşte bunun kodu:

**Python**

```python
@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict[str, str] | None
) -> list[types.TextContent]:
    
    # tools, araç isimlerinin anahtar olduğu bir sözlüktür
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
    // YAPILACAK araç çağır,

    return {
       content: [{ type: "text", text: `Tool ${name} called with arguments: ${JSON.stringify(input)}, result: ${JSON.stringify(result)}` }]
    };
});
```

Yukarıdaki kodda gördüğünüz gibi, çağrılması gereken aracı ve hangi argümanlarla çağrılacağını ayrıştırmamız gerekiyor, ardından aracı çağırmaya devam ediyoruz.

## Validasyon ile yaklaşımı geliştirmek

Şimdiye kadar, araçlar, kaynaklar ve istemler eklemek için yaptığınız tüm kayıtların, her özellik türü için bu iki işleyici ile nasıl değiştirilebileceğini gördünüz. Peki başka ne yapmalıyız? Tabii ki aracın doğru argümanlarla çağrıldığından emin olmak için bir tür doğrulama eklemeliyiz. Her çalışma zamanı bunun için kendi çözümüne sahiptir; örneğin Python Pydantic kullanır ve TypeScript Zod kullanır. Burada amaç şudur:

- Bir özellik (araç, kaynak veya istem) oluşturma mantığını kendine ait klasöre taşımak.
- Örneğin, bir aracı çağırmak isteyen gelen bir isteği doğrulamak için bir yol eklemek.

### Bir özellik oluşturmak

Bir özellik oluşturmak için, ilgili özellik için bir dosya oluşturmalıyız ve o özelliğin gerekli zorunlu alanlara sahip olduğundan emin olmalıyız. Bu alanlar araçlar, kaynaklar ve istemler arasında biraz farklılık gösterir.

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
        # Girişi Pydantic modeli kullanarak doğrula
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # TODO: Pydantic ekle, böylece bir AddInputModel oluşturup argümanları doğrulayabiliriz

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

Burada şu işlemleri yapıyoruz:

- *schema.py* dosyasında `a` ve `b` alanlarına sahip Pydantic `AddInputModel` kullanarak bir şema oluşturuyoruz.
- Gelen isteği `AddInputModel` türünde ayrıştırmaya çalışıyoruz, parametreler eşleşmezse bu hata verir:

   ```python
   # add.py
    try:
        # Girdiyi Pydantic modeli kullanarak doğrulayın
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")
   ```

Bu ayrıştırma mantığını araç çağrısının içinde ya da işleyici fonksiyonunda yapmayı seçebilirsiniz.

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

- Tüm araç çağrılarını ele alan işleyicide, gelen isteği aracın tanımlı şemasına ayrıştırmaya çalışıyoruz:

    ```typescript
    const Schema = tool.rawSchema;

    try {
       const input = Schema.parse(request.params.arguments);
    ```

    Bu başarılı olursa, gerçek aracı çağırmaya devam ediyoruz:

    ```typescript
    const result = await tool.callback(input);
    ```

Gördüğünüz gibi, bu yaklaşım harika bir mimari oluşturur çünkü her şey yerli yerindedir, *server.ts* sadece istek işleyicilerini bağlayan küçük bir dosyadır ve her özellik kendi klasöründedir, örneğin tools/, resources/ veya /prompts.

Harika, bunu şimdi inşa etmeye çalışalım.

## Egzersiz: Düşük seviyeli sunucu oluşturmak

Bu egzersizde aşağıdakileri yapacağız:

1. Araçların listelenmesini ve araçların çağrılmasını yöneten düşük seviyeli bir sunucu oluşturmak.
2. Üzerine inşa edebileceğiniz bir mimari kurmak.
3. Araç çağrılarınızın düzgün doğrulandığından emin olmak için doğrulama eklemek.

### -1- Bir mimari oluşturmak

İlk yapmamız gereken, daha fazla özellik ekledikçe ölçeklememize yardımcı olacak bir mimari oluşturmak, şöyle görünüyor:

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

Şimdi, tools klasöründe kolayca yeni araçlar ekleyebileceğimiz bir mimari kurduk. İsterseniz resources ve prompts için alt dizinler ekleyerek bu yapıyı takip edebilirsiniz.

### -2- Bir araç oluşturmak

İkinci olarak, bir araç oluşturmanın nasıl göründüğüne bakalım. Öncelikle, aracın *tool* alt dizininde oluşturulması gerekir, şöyle:

**Python**

```python
from .schema import AddInputModel

async def add_handler(args) -> float:
    try:
        # Girdiyi Pydantic modeli kullanarak doğrula
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # YAPILACAK: Argümanları oluşturup doğrulayabilmemiz için Pydantic ekle, böylece bir AddInputModel oluşturabiliriz

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

Burada, Pydantic kullanarak isim, açıklama ve giriş şemasını nasıl tanımladığımızı ve bu araç çağrıldığında çağrılacak işleyiciyi görüyoruz. Son olarak, `tool_add` özelliğini açığa çıkarıyoruz, bu tüm bu özellikleri tutan bir sözlük.

Ayrıca, aracımızın giriş şemasını tanımlamak için kullanılan *schema.py* dosyası da var:

```python
from pydantic import BaseModel

class AddInputModel(BaseModel):
    a: float
    b: float
```

tools dizininin modül olarak kabul edilmesi için *__init__.py* dosyasını da doldurmamız gerekiyor. Ayrıca içindeki modülleri şöyle açığa çıkarmalıyız:

```python
from .add import tool_add

tools = {
  tool_add["name"] : tool_add
}
```

Yeni araçlar ekledikçe bu dosyayı da büyütebiliriz.

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

Burada, özelliklerden oluşan bir sözlük oluşturuyoruz:

- name, aracın adı.
- rawSchema, Zod şemasıdır, gelen çağrı isteklerini doğrulamak için kullanılır.
- inputSchema, işleyici tarafından kullanılacak şema.
- callback, aracı çalıştırmak için kullanılan fonksiyon.

Ayrıca, bir `Tool` var, bunun amacı bu sözlüğü MCP sunucu işleyicisinin kabul edebileceği bir türe çevirmektir, şöyle görünür:

```typescript
import { z } from 'zod';

export interface Tool {
    name: string;
    inputSchema: any;
    rawSchema: z.ZodTypeAny;
    callback: (args: z.infer<z.ZodTypeAny>) => Promise<{ content: { type: string; text: string }[] }>;
}
```

Ve *schema.ts* dosyası, her araç için giriş şemalarını içerir, başlangıçta sadece bir şema bulunmakta, ancak araçlar eklendikçe daha fazla giriş ekleyebiliriz:

```typescript
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });
```

Harika, şimdi araçlarımızın listesini ele almaya geçelim.

### -3- Araç listesini ele almak

Ardından, araç listesini ele almak için bir istek işleyici kurmamız gerekiyor. İşte sunucu dosyamıza eklememiz gerekenler:

**Python**

```python
# kısa olması için kod atlandı
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

Burada `@server.list_tools` dekoratörünü ve uygulayan fonksiyon `handle_list_tools` ekliyoruz. Bu fonksiyon, bir araçlar listesi üretmelidir. Her aracın `name`, `description` ve `inputSchema` alanlarını içerdiğine dikkat edin.

**TypeScript**

Araçları listelemek için istek işleyicisini kurmak için, sunucuda `setRequestHandler` çağrılır ve buraya yapılan işlem için uygun şema olan `ListToolsRequestSchema` geçilir.

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
// Kısalık için kod atlandı
import { tools } from './tools/index.js';

server.setRequestHandler(ListToolsRequestSchema, async (request) => {
  // Kayıtlı araçların listesini döndürür
  return {
    tools: tools
  };
});
```

Harika, artık araçları listeleme kısmını çözdük, şimdi araç çağırmanın nasıl olabileceğine bakalım.

### -4- Bir aracı çağırmayı ele almak

Bir aracı çağırmak için, hangi özelliğin hangi argümanlarla çağrılacağını belirten istekleri ele alan başka bir istek işleyicisi kurmamız gerekir.

**Python**

`@server.call_tool` dekoratörünü kullanalım ve `handle_call_tool` gibi bir fonksiyonla uygulatılsın. Bu fonksiyon içinde, araç adını, argümanlarını ayrıştırmamız ve argümanların doğru olduğundan emin olmamız gerekiyor. Argümanları burada doğrulayabilir veya daha ileri aşamalarda gerçek araç içinde doğrulatabiliriz.

```python
@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict[str, str] | None
) -> list[types.TextContent]:
    
    # tools, anahtarı araç isimleri olan bir sözlüktür
    if name not in tools.tools:
        raise ValueError(f"Unknown tool: {name}")
    
    tool = tools.tools[name]

    result = "default"
    try:
        # aracı çağır
        result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)
    except Exception as e:
        raise ValueError(f"Error calling tool {name}: {str(e)}")

    return [
        types.TextContent(type="text", text=str(result))
    ]
```

İşte olanlar:

- Araç adı zaten giriş parametresi olan `name` olarak mevcut, argümanlarımız ise `arguments` sözlüğü şeklinde.

- Araç `result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)` ile çağrılır. Argümanların doğrulanması ise `handler` özelliğinde yer alan fonksiyonda yapılır; başarısız olursa bir istisna fırlatılır.

İşte, düşük seviyeli sunucu ile araç listesi alma ve çağırma işlemlerini tam olarak anladık.

Tam örneği [buradan](./code/README.md) görebilirsiniz.

## Ödev

Verilen kodu, birçok araç, kaynak ve istem ile genişletin ve sadece tools dizinine dosya eklemeniz gerektiğini fark edin, başka yere gerek olmadığını gözlemleyin.

*Çözüm verilmemektedir*

## Özet

Bu bölümde, düşük seviyeli sunucu yaklaşımını nasıl çalıştığını ve bize nasıl güzel bir mimari sağladığını gördük. Ayrıca doğrulamadan bahsettik ve doğrulama kütüphaneleriyle giriş doğrulama şemalarının nasıl oluşturulacağını gösterdik.

## Sonraki Adım

- Sonraki: [Basit Kimlik Doğrulama](../11-simple-auth/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Feragatname**:  
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hatalar veya yanlışlıklar içerebileceğini lütfen unutmayın. Orijinal belge, kendi diliyle yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucunda oluşabilecek herhangi bir yanlış anlama veya yanlış yorumdan sorumlu değiliz.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->