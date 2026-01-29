# Uso avanzado del servidor

Existen dos tipos diferentes de servidores expuestos en el MCP SDK: el servidor normal y el servidor de bajo nivel. Normalmente, usarías el servidor regular para agregarle funcionalidades. Sin embargo, en algunos casos, es preferible usar el servidor de bajo nivel, como en los siguientes escenarios:

- Mejor arquitectura. Es posible crear una arquitectura limpia tanto con el servidor regular como con el servidor de bajo nivel, pero se puede argumentar que es ligeramente más fácil con el servidor de bajo nivel.
- Disponibilidad de características. Algunas funcionalidades avanzadas solo pueden ser utilizadas con un servidor de bajo nivel. Verás esto en capítulos posteriores cuando agreguemos muestreo y elicitación.

## Servidor regular vs servidor de bajo nivel

Así es como se ve la creación de un servidor MCP con el servidor regular:

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

La idea es que explícitamente agregas cada herramienta, recurso o prompt que deseas que el servidor tenga. No hay nada de malo en eso.  

### Enfoque del servidor de bajo nivel

Sin embargo, cuando utilizas el enfoque del servidor de bajo nivel, debes pensar de manera diferente. En lugar de registrar cada herramienta, creas dos manejadores por tipo de característica (herramientas, recursos o prompts). Por ejemplo, para las herramientas, solo tendrías dos funciones como estas:

- Listar todas las herramientas. Una función sería responsable de todos los intentos de listar herramientas.
- Manejar las llamadas a todas las herramientas. Aquí también, solo hay una función que maneja las llamadas a una herramienta.

¿Suena como menos trabajo, verdad? En lugar de registrar una herramienta, solo necesitas asegurarte de que la herramienta esté listada cuando se enumeren todas las herramientas y que se llame cuando haya una solicitud entrante para usarla.

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

Aquí tenemos una función que devuelve una lista de características. Cada entrada en la lista de herramientas ahora tiene campos como `name`, `description` y `inputSchema` para cumplir con el tipo de retorno. Esto nos permite definir nuestras herramientas y características en otro lugar. Ahora podemos crear todas nuestras herramientas en una carpeta de herramientas, y lo mismo aplica para todas tus características, de modo que tu proyecto puede organizarse así:

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

Esto es genial, nuestra arquitectura puede verse bastante limpia.

¿Qué pasa con llamar a las herramientas? ¿Es la misma idea, un manejador para llamar a cualquier herramienta? Sí, exactamente, aquí está el código para eso:

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

Como puedes ver en el código anterior, necesitamos analizar qué herramienta se va a llamar, con qué argumentos, y luego proceder a llamar a la herramienta.

## Mejorando el enfoque con validación

Hasta ahora, has visto cómo todas tus registraciones para agregar herramientas, recursos y prompts pueden ser reemplazadas con estos dos manejadores por tipo de característica. ¿Qué más necesitamos hacer? Bueno, deberíamos agregar alguna forma de validación para asegurarnos de que la herramienta se llame con los argumentos correctos. Cada entorno de ejecución tiene su propia solución para esto, por ejemplo, Python usa Pydantic y TypeScript usa Zod. La idea es hacer lo siguiente:

- Mover la lógica para crear una característica (herramienta, recurso o prompt) a su carpeta dedicada.
- Agregar una forma de validar una solicitud entrante que, por ejemplo, pida llamar a una herramienta.

### Crear una característica

Para crear una característica, necesitamos crear un archivo para esa característica y asegurarnos de que tenga los campos obligatorios requeridos. Los campos varían un poco entre herramientas, recursos y prompts.

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

Aquí puedes ver cómo hacemos lo siguiente:

- Crear un esquema usando Pydantic `AddInputModel` con los campos `a` y `b` en el archivo *schema.py*.
- Intentar analizar la solicitud entrante para que sea del tipo `AddInputModel`. Si hay una discrepancia en los parámetros, esto fallará:

   ```python
   # add.py
    try:
        # Validate input using Pydantic model
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")
   ```

Puedes elegir si colocar esta lógica de análisis en la propia llamada de la herramienta o en la función del manejador.

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

- En el manejador que se ocupa de todas las llamadas a herramientas, ahora intentamos analizar la solicitud entrante en el esquema definido de la herramienta:

    ```typescript
    const Schema = tool.rawSchema;

    try {
       const input = Schema.parse(request.params.arguments);
    ```

    si eso funciona, procedemos a llamar a la herramienta real:

    ```typescript
    const result = await tool.callback(input);
    ```

Como puedes ver, este enfoque crea una gran arquitectura, ya que todo tiene su lugar. El archivo *server.ts* es muy pequeño y solo conecta los manejadores de solicitudes, mientras que cada característica está en su carpeta respectiva, es decir, tools/, resources/ o prompts/.

Genial, intentemos construir esto a continuación.

## Ejercicio: Crear un servidor de bajo nivel

En este ejercicio, haremos lo siguiente:

1. Crear un servidor de bajo nivel que maneje la lista de herramientas y las llamadas a herramientas.
1. Implementar una arquitectura sobre la que puedas construir.
1. Agregar validación para asegurarte de que las llamadas a herramientas estén correctamente validadas.

### -1- Crear una arquitectura

Lo primero que necesitamos abordar es una arquitectura que nos ayude a escalar a medida que agregamos más características. Así es como se ve:

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

Ahora hemos configurado una arquitectura que asegura que podamos agregar fácilmente nuevas herramientas en una carpeta de herramientas. Siéntete libre de seguir esto para agregar subdirectorios para recursos y prompts.

### -2- Crear una herramienta

Veamos cómo se ve crear una herramienta. Primero, debe ser creada en su subdirectorio *tool* de esta manera:

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

Aquí vemos cómo definimos el nombre, la descripción, un esquema de entrada usando Pydantic y un manejador que será invocado una vez que se llame a esta herramienta. Por último, exponemos `tool_add`, que es un diccionario que contiene todas estas propiedades.

También está *schema.py*, que se utiliza para definir el esquema de entrada usado por nuestra herramienta:

```python
from pydantic import BaseModel

class AddInputModel(BaseModel):
    a: float
    b: float
```

También necesitamos completar *__init__.py* para asegurarnos de que el directorio de herramientas sea tratado como un módulo. Además, necesitamos exponer los módulos dentro de él de esta manera:

```python
from .add import tool_add

tools = {
  tool_add["name"] : tool_add
}
```

Podemos seguir agregando a este archivo a medida que agregamos más herramientas.

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
- rawSchema, este es el esquema Zod, que se usará para validar las solicitudes entrantes para llamar a esta herramienta.
- inputSchema, este esquema será usado por el manejador.
- callback, esto se utiliza para invocar la herramienta.

También está `Tool`, que se utiliza para convertir este diccionario en un tipo que el manejador del servidor MCP puede aceptar, y se ve así:

```typescript
import { z } from 'zod';

export interface Tool {
    name: string;
    inputSchema: any;
    rawSchema: z.ZodTypeAny;
    callback: (args: z.infer<z.ZodTypeAny>) => Promise<{ content: { type: string; text: string }[] }>;
}
```

Y está *schema.ts*, donde almacenamos los esquemas de entrada para cada herramienta. Actualmente tiene solo un esquema, pero a medida que agregamos herramientas podemos agregar más entradas:

```typescript
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });
```

Genial, procedamos a manejar la lista de nuestras herramientas a continuación.

### -3- Manejar la lista de herramientas

A continuación, para manejar la lista de herramientas, necesitamos configurar un manejador de solicitudes para eso. Esto es lo que necesitamos agregar a nuestro archivo de servidor:

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

Aquí agregamos el decorador `@server.list_tools` y la función implementada `handle_list_tools`. En esta última, necesitamos producir una lista de herramientas. Nota cómo cada herramienta necesita tener un nombre, descripción y inputSchema.   

**TypeScript**

Para configurar el manejador de solicitudes para listar herramientas, necesitamos llamar a `setRequestHandler` en el servidor con un esquema que se ajuste a lo que estamos tratando de hacer, en este caso `ListToolsRequestSchema`. 

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

Genial, ahora hemos resuelto la parte de listar herramientas. Veamos cómo podríamos llamar a herramientas a continuación.

### -4- Manejar la llamada a una herramienta

Para llamar a una herramienta, necesitamos configurar otro manejador de solicitudes, esta vez enfocado en manejar una solicitud que especifique qué característica llamar y con qué argumentos.

**Python**

Usemos el decorador `@server.call_tool` e implementémoslo con una función como `handle_call_tool`. Dentro de esa función, necesitamos analizar el nombre de la herramienta, sus argumentos y asegurarnos de que los argumentos sean válidos para la herramienta en cuestión. Podemos validar los argumentos en esta función o más adelante en la herramienta real.

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

Esto es lo que sucede:

- El nombre de nuestra herramienta ya está presente como el parámetro de entrada `name`, lo mismo ocurre con nuestros argumentos en forma del diccionario `arguments`.

- La herramienta se llama con `result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)`. La validación de los argumentos ocurre en la propiedad `handler`, que apunta a una función. Si falla, lanzará una excepción. 

Ahí lo tienes, ahora tenemos una comprensión completa de cómo listar y llamar herramientas usando un servidor de bajo nivel.

Consulta el [ejemplo completo](./code/README.md) aquí.

## Tarea

Amplía el código que se te ha dado con varias herramientas, recursos y prompts, y reflexiona sobre cómo notas que solo necesitas agregar archivos en el directorio de herramientas y en ningún otro lugar. 

*No se proporciona solución*

## Resumen

En este capítulo, vimos cómo funciona el enfoque del servidor de bajo nivel y cómo puede ayudarnos a crear una arquitectura agradable sobre la que podamos seguir construyendo. También discutimos la validación y se te mostró cómo trabajar con bibliotecas de validación para crear esquemas para la validación de entradas.

---

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por garantizar la precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o imprecisiones. El documento original en su idioma nativo debe considerarse como la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o interpretaciones erróneas que puedan surgir del uso de esta traducción.