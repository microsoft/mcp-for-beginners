# Utilização avançada de servidores

Existem dois tipos diferentes de servidores expostos no MCP SDK: o servidor normal e o servidor de baixo nível. Normalmente, utiliza-se o servidor regular para adicionar funcionalidades. No entanto, em alguns casos, pode ser necessário recorrer ao servidor de baixo nível, como por exemplo:

- Melhor arquitetura. É possível criar uma arquitetura limpa tanto com o servidor regular como com o servidor de baixo nível, mas pode-se argumentar que é ligeiramente mais fácil com o servidor de baixo nível.
- Disponibilidade de funcionalidades. Algumas funcionalidades avançadas só podem ser utilizadas com um servidor de baixo nível. Veremos isso em capítulos posteriores, à medida que adicionarmos amostragem e elicitação.

## Servidor regular vs servidor de baixo nível

Aqui está como a criação de um MCP Server se parece com o servidor regular:

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

A ideia aqui é que se adiciona explicitamente cada ferramenta, recurso ou prompt que se deseja que o servidor tenha. Não há nada de errado com isso.  

### Abordagem do servidor de baixo nível

No entanto, ao utilizar a abordagem do servidor de baixo nível, é necessário pensar de forma diferente, ou seja, em vez de registar cada ferramenta, cria-se dois manipuladores por tipo de funcionalidade (ferramentas, recursos ou prompts). Por exemplo, para ferramentas, existem apenas duas funções, como segue:

- Listar todas as ferramentas. Uma função será responsável por todas as tentativas de listar ferramentas.
- Manipular chamadas para todas as ferramentas. Aqui também, há apenas uma função que lida com chamadas para uma ferramenta.

Isso parece ser potencialmente menos trabalho, certo? Em vez de registar uma ferramenta, basta garantir que a ferramenta seja listada quando todas as ferramentas forem listadas e que seja chamada quando houver uma solicitação para chamar uma ferramenta.

Vamos ver como o código se parece agora:

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

Aqui temos agora uma função que retorna uma lista de funcionalidades. Cada entrada na lista de ferramentas possui campos como `name`, `description` e `inputSchema` para aderir ao tipo de retorno. Isso permite que coloquemos as definições de ferramentas e funcionalidades noutro lugar. Podemos agora criar todas as nossas ferramentas numa pasta de ferramentas e o mesmo se aplica a todas as funcionalidades, permitindo que o projeto seja organizado da seguinte forma:

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

Isso é ótimo, a nossa arquitetura pode ser feita para parecer bastante limpa.

E quanto a chamar ferramentas? É a mesma ideia, um manipulador para chamar uma ferramenta, seja qual for? Sim, exatamente, aqui está o código para isso:

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

Como se pode ver no código acima, é necessário analisar qual ferramenta chamar, com quais argumentos, e depois proceder à chamada da ferramenta.

## Melhorar a abordagem com validação

Até agora, vimos como todas as registos para adicionar ferramentas, recursos e prompts podem ser substituídos por esses dois manipuladores por tipo de funcionalidade. O que mais precisamos fazer? Bem, devemos adicionar alguma forma de validação para garantir que a ferramenta seja chamada com os argumentos corretos. Cada runtime tem a sua própria solução para isso, por exemplo, Python usa Pydantic e TypeScript usa Zod. A ideia é fazer o seguinte:

- Mover a lógica para criar uma funcionalidade (ferramenta, recurso ou prompt) para a sua pasta dedicada.
- Adicionar uma forma de validar uma solicitação recebida que, por exemplo, pede para chamar uma ferramenta.

### Criar uma funcionalidade

Para criar uma funcionalidade, será necessário criar um ficheiro para essa funcionalidade e garantir que possui os campos obrigatórios exigidos dessa funcionalidade. Os campos diferem um pouco entre ferramentas, recursos e prompts.

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

Aqui pode-se ver como fazemos o seguinte:

- Criar um esquema usando Pydantic `AddInputModel` com os campos `a` e `b` no ficheiro *schema.py*.
- Tentar analisar a solicitação recebida para ser do tipo `AddInputModel`. Se houver uma incompatibilidade nos parâmetros, isso irá falhar:

   ```python
   # add.py
    try:
        # Validate input using Pydantic model
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")
   ```

Pode-se escolher se deseja colocar esta lógica de análise na própria chamada da ferramenta ou na função manipuladora.

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

- No manipulador que lida com todas as chamadas de ferramentas, tentamos agora analisar a solicitação recebida no esquema definido da ferramenta:

    ```typescript
    const Schema = tool.rawSchema;

    try {
       const input = Schema.parse(request.params.arguments);
    ```

    Se isso funcionar, prosseguimos para chamar a ferramenta real:

    ```typescript
    const result = await tool.callback(input);
    ```

Como se pode ver, esta abordagem cria uma ótima arquitetura, pois tudo tem o seu lugar. O *server.ts* é um ficheiro muito pequeno que apenas conecta os manipuladores de solicitações, e cada funcionalidade está na sua respetiva pasta, ou seja, tools/, resources/ ou prompts/.

Ótimo, vamos tentar construir isso a seguir.

## Exercício: Criar um servidor de baixo nível

Neste exercício, faremos o seguinte:

1. Criar um servidor de baixo nível que lida com a listagem de ferramentas e chamadas de ferramentas.
1. Implementar uma arquitetura que possa ser expandida.
1. Adicionar validação para garantir que as chamadas de ferramentas sejam devidamente validadas.

### -1- Criar uma arquitetura

A primeira coisa que precisamos abordar é uma arquitetura que nos ajude a escalar à medida que adicionamos mais funcionalidades. Aqui está como ela se parece:

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

Agora temos uma arquitetura configurada que garante que podemos facilmente adicionar novas ferramentas numa pasta de ferramentas. Sinta-se à vontade para seguir este modelo e adicionar subdiretórios para recursos e prompts.

### -2- Criar uma ferramenta

Vamos ver como criar uma ferramenta. Primeiro, ela precisa ser criada no seu subdiretório *tool*, como segue:

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

Aqui vemos como definimos o nome, descrição, um esquema de entrada usando Pydantic e um manipulador que será invocado quando esta ferramenta for chamada. Por fim, expomos `tool_add`, que é um dicionário que contém todas estas propriedades.

Há também o ficheiro *schema.py*, que é usado para definir o esquema de entrada utilizado pela nossa ferramenta:

```python
from pydantic import BaseModel

class AddInputModel(BaseModel):
    a: float
    b: float
```

Também precisamos preencher *__init__.py* para garantir que o diretório de ferramentas seja tratado como um módulo. Além disso, precisamos expor os módulos dentro dele, como segue:

```python
from .add import tool_add

tools = {
  tool_add["name"] : tool_add
}
```

Podemos continuar a adicionar a este ficheiro à medida que adicionamos mais ferramentas.

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

Aqui criamos um dicionário que consiste em propriedades:

- name, este é o nome da ferramenta.
- rawSchema, este é o esquema Zod, que será usado para validar solicitações recebidas para chamar esta ferramenta.
- inputSchema, este esquema será usado pelo manipulador.
- callback, este é usado para invocar a ferramenta.

Há também `Tool`, que é usado para converter este dicionário num tipo que o manipulador do servidor MCP pode aceitar, e que se parece com isto:

```typescript
import { z } from 'zod';

export interface Tool {
    name: string;
    inputSchema: any;
    rawSchema: z.ZodTypeAny;
    callback: (args: z.infer<z.ZodTypeAny>) => Promise<{ content: { type: string; text: string }[] }>;
}
```

E há o ficheiro *schema.ts*, onde armazenamos os esquemas de entrada para cada ferramenta. Atualmente, há apenas um esquema, mas à medida que adicionamos ferramentas, podemos adicionar mais entradas:

```typescript
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });
```

Ótimo, vamos proceder para lidar com a listagem das nossas ferramentas a seguir.

### -3- Lidar com a listagem de ferramentas

Para lidar com a listagem de ferramentas, precisamos configurar um manipulador de solicitações para isso. Aqui está o que precisamos adicionar ao nosso ficheiro de servidor:

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

Aqui adicionamos o decorador `@server.list_tools` e a função implementada `handle_list_tools`. Nesta última, precisamos produzir uma lista de ferramentas. Note como cada ferramenta precisa ter um nome, descrição e inputSchema.   

**TypeScript**

Para configurar o manipulador de solicitações para listar ferramentas, precisamos chamar `setRequestHandler` no servidor com um esquema adequado ao que estamos a tentar fazer, neste caso `ListToolsRequestSchema`. 

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

Ótimo, agora resolvemos a parte de listar ferramentas. Vamos ver como podemos chamar ferramentas a seguir.

### -4- Lidar com chamadas de ferramentas

Para chamar uma ferramenta, precisamos configurar outro manipulador de solicitações, desta vez focado em lidar com uma solicitação que especifica qual funcionalidade chamar e com quais argumentos.

**Python**

Vamos usar o decorador `@server.call_tool` e implementá-lo com uma função como `handle_call_tool`. Dentro dessa função, precisamos analisar o nome da ferramenta, os seus argumentos e garantir que os argumentos sejam válidos para a ferramenta em questão. Podemos validar os argumentos nesta função ou mais abaixo, na própria ferramenta.

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

Aqui está o que acontece:

- O nome da ferramenta já está presente como o parâmetro de entrada `name`, o que também é verdade para os argumentos na forma do dicionário `arguments`.

- A ferramenta é chamada com `result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)`. A validação dos argumentos acontece na propriedade `handler`, que aponta para uma função. Se isso falhar, será lançada uma exceção. 

Pronto, agora temos uma compreensão completa de como listar e chamar ferramentas usando um servidor de baixo nível.

Veja o [exemplo completo](./code/README.md) aqui.

## Tarefa

Expanda o código que lhe foi dado com várias ferramentas, recursos e prompts e reflita sobre como percebe que só precisa adicionar ficheiros no diretório de ferramentas e em mais nenhum lugar. 

*Sem solução fornecida*

## Resumo

Neste capítulo, vimos como funciona a abordagem do servidor de baixo nível e como isso pode ajudar-nos a criar uma arquitetura organizada que podemos continuar a expandir. Também discutimos validação e foi mostrado como trabalhar com bibliotecas de validação para criar esquemas para validação de entradas.

---

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autoritária. Para informações críticas, recomenda-se uma tradução profissional realizada por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.