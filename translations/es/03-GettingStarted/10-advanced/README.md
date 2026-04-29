# Uso avanzado del servidor

Existen dos tipos diferentes de servidores expuestos en el SDK de MCP, tu servidor normal y el servidor de bajo nivel. Normalmente, utilizarías el servidor regular para agregarle funcionalidades. Sin embargo, en algunos casos quieres apoyarte en el servidor de bajo nivel como:

- Mejor arquitectura. Es posible crear una arquitectura limpia con ambos, el servidor regular y uno de bajo nivel, pero se puede argumentar que es un poco más sencillo con un servidor de bajo nivel.
- Disponibilidad de funciones. Algunas funcionalidades avanzadas solo se pueden usar con un servidor de bajo nivel. Esto lo verás en capítulos posteriores al añadir muestreo y elicitación.

## Servidor regular vs servidor de bajo nivel

Así es como se ve la creación de un servidor MCP con el servidor regular

**Python**

```python
mcp = FastMCP("Demo")

# Añadir una herramienta de adición
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

// Añadir una herramienta de suma
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

La cuestión es que agregas explícitamente cada herramienta, recurso o prompt que quieres que el servidor tenga. No hay nada de malo en eso.

### Enfoque del servidor de bajo nivel

Sin embargo, cuando usas el enfoque del servidor de bajo nivel, debes pensarlo de forma diferente. En lugar de registrar cada herramienta, creas dos manejadores por tipo de función (herramientas, recursos o prompts). Por ejemplo, las herramientas solo tienen dos funciones:

- Listar todas las herramientas. Una función es responsable de todos los intentos de listar herramientas.
- Manejar llamadas a todas las herramientas. Aquí también, solo hay una función que maneja las llamadas a una herramienta.

Eso suena como menos trabajo ¿verdad? Entonces, en lugar de registrar una herramienta, solo necesito asegurarme de que la herramienta esté listada cuando liste todas las herramientas y que se llame cuando llegue una solicitud para llamar a una herramienta.

Veamos cómo se ve el código ahora:

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
  // Devuelve la lista de herramientas registradas
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

Aquí tenemos una función que devuelve una lista de funciones. Cada entrada en la lista de herramientas ahora tiene campos como `name`, `description` y `inputSchema` para ajustarse al tipo de retorno. Esto nos permite poner nuestras herramientas y definición de funciones en otro lugar. Ahora podemos crear todas nuestras herramientas en una carpeta tools y lo mismo para todas tus funciones, por lo que tu proyecto puede estar organizado así:

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

Eso es genial, nuestra arquitectura puede ser bastante limpia.

¿Qué hay de llamar herramientas? ¿Es la misma idea entonces, un manejador para llamar a una herramienta, cualquiera que sea? Sí, exactamente, aquí está el código para eso:

**Python**

```python
@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict[str, str] | None
) -> list[types.TextContent]:
    
    # tools es un diccionario con los nombres de las herramientas como claves
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
    // TODO llamar a la herramienta,

    return {
       content: [{ type: "text", text: `Tool ${name} called with arguments: ${JSON.stringify(input)}, result: ${JSON.stringify(result)}` }]
    };
});
```

Como puedes ver en el código de arriba, necesitamos extraer qué herramienta llamar, con qué argumentos, y luego proceder a llamar a la herramienta.

## Mejorando el enfoque con validación

Hasta ahora, has visto cómo todos tus registros para agregar herramientas, recursos y prompts pueden reemplazarse con estos dos manejadores por tipo de función. ¿Qué más necesitamos hacer? Bueno, deberíamos agregar alguna forma de validación para asegurar que la herramienta se llame con los argumentos correctos. Cada entorno tiene su propia solución para esto, por ejemplo Python usa Pydantic y TypeScript usa Zod. La idea es hacer lo siguiente:

- Mover la lógica para crear una función (herramienta, recurso o prompt) a su carpeta dedicada.
- Añadir una forma de validar una petición entrante que pida por ejemplo llamar a una herramienta.

### Crear una función

Para crear una función, necesitaremos crear un archivo para esa función y asegurarnos que tiene los campos obligatorios que requiere esa función. Qué campos difieren un poco entre herramientas, recursos y prompts.

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
        # Validar entrada usando el modelo Pydantic
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # TODO: agregar Pydantic, para que podamos crear un AddInputModel y validar los argumentos

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

Aquí puedes ver cómo hacemos lo siguiente:

- Crear un esquema usando Pydantic `AddInputModel` con campos `a` y `b` en el archivo *schema.py*.
- Intentar parsear la solicitud entrante para que sea del tipo `AddInputModel`, si hay un desacuerdo en los parámetros esto fallará:

   ```python
   # add.py
    try:
        # Validar la entrada usando el modelo Pydantic
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")
   ```

Puedes escoger si poner esta lógica de parseo en la llamada a la herramienta misma o en la función manejadora.

**TypeScript**

```typescript
// servidor.ts
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

// esquema.ts
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });

// agregar.ts
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

- En el manejador que mueve todas las llamadas a herramientas, ahora intentamos parsear la solicitud entrante al esquema definido para la herramienta:

    ```typescript
    const Schema = tool.rawSchema;

    try {
       const input = Schema.parse(request.params.arguments);
    ```

    si eso funciona, entonces procedemos a llamar la herramienta real:

    ```typescript
    const result = await tool.callback(input);
    ```

Como puedes ver, este enfoque crea una arquitectura excelente ya que todo tiene su lugar, *server.ts* es un archivo muy pequeño que solo enlaza los manejadores de solicitud y cada función está en su respectiva carpeta i.e tools/, resources/ o /prompts.

Genial, intentemos construir esto a continuación.

## Ejercicio: Crear un servidor de bajo nivel

En este ejercicio haremos lo siguiente:

1. Crear un servidor de bajo nivel que maneje el listado de herramientas y llamadas a herramientas.
1. Implementar una arquitectura sobre la cual puedas construir.
1. Añadir validación para asegurar que las llamadas a tus herramientas estén debidamente validadas.

### -1- Crear una arquitectura

Lo primero que necesitamos abordar es una arquitectura que nos ayude a escalar mientras añadimos más funciones, así es como se ve:

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

Ahora hemos configurado una arquitectura que asegura que podemos añadir fácilmente nuevas herramientas en una carpeta tools. Siéntete libre de seguir esto para agregar subdirectorios para recursos y prompts.

### -2- Crear una herramienta

Veamos cómo se ve crear una herramienta a continuación. Primero, necesita ser creada en su subdirectorio *tool* así:

**Python**

```python
from .schema import AddInputModel

async def add_handler(args) -> float:
    try:
        # Validar la entrada usando el modelo Pydantic
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # TODO: agregar Pydantic, para que podamos crear un AddInputModel y validar los argumentos

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

Aquí vemos cómo definimos el nombre, descripción y el esquema de entrada usando Pydantic y un manejador que será invocado cuando se llame a esta herramienta. Finalmente, exponemos `tool_add` que es un diccionario con todas esas propiedades.

También está *schema.py* que se usa para definir el esquema de entrada usado por nuestra herramienta:

```python
from pydantic import BaseModel

class AddInputModel(BaseModel):
    a: float
    b: float
```

También necesitamos poblar *__init__.py* para asegurar que el directorio de herramientas se trate como un módulo. Además, necesitamos exponer los módulos dentro de él así:

```python
from .add import tool_add

tools = {
  tool_add["name"] : tool_add
}
```

Podemos seguir agregando a este archivo a medida que añadimos más herramientas.

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

Aquí creamos un diccionario que consiste en propiedades:

- name, este es el nombre de la herramienta.
- rawSchema, este es el esquema Zod, se usará para validar las solicitudes entrantes para llamar esta herramienta.
- inputSchema, este esquema será usado por el manejador.
- callback, esto se usa para invocar la herramienta.

También existe `Tool` que se usa para convertir este diccionario en un tipo que el manejador del servidor MCP puede aceptar y se ve así:

```typescript
import { z } from 'zod';

export interface Tool {
    name: string;
    inputSchema: any;
    rawSchema: z.ZodTypeAny;
    callback: (args: z.infer<z.ZodTypeAny>) => Promise<{ content: { type: string; text: string }[] }>;
}
```

Y está *schema.ts* donde almacenamos los esquemas de entrada para cada herramienta que se ve así con solo un esquema por ahora pero a medida que añadimos herramientas podemos añadir más entradas:

```typescript
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });
```

Genial, procedamos ahora a manejar el listado de nuestras herramientas.

### -3- Manejar listado de herramientas

A continuación, para manejar el listado de nuestras herramientas necesitamos configurar un manejador de solicitudes para eso. Esto es lo que debemos añadir a nuestro archivo servidor:

**Python**

```python
# código omitido por brevedad
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

Aquí, agregamos el decorador `@server.list_tools` y la función implementadora `handle_list_tools`. En esta última, tenemos que producir una lista de herramientas. Nota cómo cada herramienta necesita tener un nombre, descripción e inputSchema.

**TypeScript**

Para configurar el manejador de solicitudes para listar herramientas, necesitamos llamar a `setRequestHandler` en el servidor con un esquema que encaje con lo que intentamos hacer, en este caso `ListToolsRequestSchema`.

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
// código omitido por brevedad
import { tools } from './tools/index.js';

server.setRequestHandler(ListToolsRequestSchema, async (request) => {
  // Devuelve la lista de herramientas registradas
  return {
    tools: tools
  };
});
```

Genial, ahora hemos resuelto la parte de listar herramientas, veamos cómo podríamos llamar a herramientas a continuación.

### -4- Manejar llamada a una herramienta

Para llamar a una herramienta, necesitamos configurar otro manejador de solicitudes, esta vez enfocado en tratar una solicitud que especifique qué función llamar y con qué argumentos.

**Python**

Usemos el decorador `@server.call_tool` y lo implementamos con una función como `handle_call_tool`. Dentro de esa función, necesitamos extraer el nombre de la herramienta, sus argumentos y asegurar que los argumentos sean válidos para la herramienta en cuestión. Podemos validar los argumentos en esta función o más adelante en la herramienta real.

```python
@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict[str, str] | None
) -> list[types.TextContent]:
    
    # tools es un diccionario con los nombres de las herramientas como claves
    if name not in tools.tools:
        raise ValueError(f"Unknown tool: {name}")
    
    tool = tools.tools[name]

    result = "default"
    try:
        # invocar la herramienta
        result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)
    except Exception as e:
        raise ValueError(f"Error calling tool {name}: {str(e)}")

    return [
        types.TextContent(type="text", text=str(result))
    ]
```

Esto es lo que sucede:

- El nombre de nuestra herramienta ya está presente como parámetro de entrada `name` lo cual es válido para nuestros argumentos en forma de diccionario `arguments`.

- La herramienta es llamada con `result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)`. La validación de los argumentos sucede en la propiedad `handler` que apunta a una función, si falla levantará una excepción.

Listo, ahora tenemos una comprensión completa de cómo listar y llamar a herramientas usando un servidor de bajo nivel.

Consulta el [ejemplo completo](./code/README.md) aquí

## Asignación

Extiende el código que te han dado con varias herramientas, recursos y prompts y reflexiona sobre cómo notas que solo necesitas agregar archivos en el directorio tools y en ningún otro lugar.

*No se proporciona solución*

## Resumen

En este capítulo, vimos cómo funciona el enfoque del servidor de bajo nivel y cómo eso puede ayudarnos a crear una arquitectura agradable sobre la cual podemos seguir construyendo. También discutimos la validación y te mostramos cómo trabajar con bibliotecas de validación para crear esquemas para la validación de entradas.

## Qué sigue

- A continuación: [Autenticación simple](../11-simple-auth/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda la traducción profesional realizada por un humano. No somos responsables por ningún malentendido o interpretación errónea que surja del uso de esta traducción.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->