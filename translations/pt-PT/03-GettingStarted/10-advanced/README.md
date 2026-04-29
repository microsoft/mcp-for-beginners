# Uso avançado do servidor

Existem dois tipos diferentes de servidores expostos no MCP SDK, o seu servidor normal e o servidor de baixo nível. Normalmente, você usaria o servidor regular para adicionar funcionalidades. Contudo, em alguns casos, você quer depender do servidor de baixo nível, como:

- Melhor arquitetura. É possível criar uma arquitetura limpa tanto com o servidor regular quanto com um servidor de baixo nível, mas pode-se argumentar que é ligeiramente mais fácil com um servidor de baixo nível.
- Disponibilidade de funcionalidades. Algumas funcionalidades avançadas só podem ser usadas com um servidor de baixo nível. Você verá isso em capítulos posteriores, quando adicionarmos amostragem e elicitação.

## Servidor regular vs servidor de baixo nível

Aqui está como a criação de um Servidor MCP se parece com o servidor regular

**Python**

```python
mcp = FastMCP("Demo")

# Adicionar uma ferramenta de adição
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

// Adicionar uma ferramenta de adição
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

A questão é que você adiciona explicitamente cada ferramenta, recurso ou prompt que quer que o servidor tenha. Não há nada de errado nisso.  

### Abordagem do servidor de baixo nível

No entanto, quando você usa a abordagem do servidor de baixo nível, precisa pensar de forma diferente. Em vez de registrar cada ferramenta, você cria dois manipuladores por tipo de funcionalidade (ferramentas, recursos ou prompts). Por exemplo, as ferramentas têm apenas duas funções da seguinte forma:

- Listar todas as ferramentas. Uma função seria responsável por todas as tentativas de listar ferramentas.
- Manipular chamadas a todas as ferramentas. Aqui também, há apenas uma função que trata as chamadas para uma ferramenta.

Isso soa como potencialmente menos trabalho, certo? Então, em vez de registrar uma ferramenta, só preciso garantir que a ferramenta esteja listada quando listar todas as ferramentas e que ela seja chamada quando houver uma solicitação para chamar uma ferramenta.

Vamos ver como o código fica agora:

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
  // Retorna a lista de ferramentas registadas
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

Aqui agora temos uma função que retorna uma lista de funcionalidades. Cada entrada na lista de ferramentas agora tem campos como `name`, `description` e `inputSchema` para aderir ao tipo de retorno. Isso nos permite colocar nossas ferramentas e definição de funcionalidades noutro lugar. Podemos agora criar todas as nossas ferramentas numa pasta tools e o mesmo vale para todas as suas funcionalidades, assim o seu projeto pode estar organizado assim:

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

Isso é ótimo, nossa arquitetura pode ser feita para ficar bem limpa.

E para chamar as ferramentas, é a mesma ideia então, um manipulador para chamar qualquer ferramenta? Sim, exatamente, aqui está o código para isso:

**Python**

```python
@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict[str, str] | None
) -> list[types.TextContent]:
    
    # tools é um dicionário com os nomes das ferramentas como chaves
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
    // TODO chamar a ferramenta,

    return {
       content: [{ type: "text", text: `Tool ${name} called with arguments: ${JSON.stringify(input)}, result: ${JSON.stringify(result)}` }]
    };
});
```

Como pode ver no código acima, precisamos analisar qual ferramenta chamar, e com que argumentos, e então prosseguir para a chamada da ferramenta.

## Melhorando a abordagem com validação

Até agora, você viu como todos os seus registos para adicionar ferramentas, recursos e prompts podem ser substituídos por estes dois manipuladores por tipo de funcionalidade. O que mais precisamos fazer? Bem, devemos adicionar algum tipo de validação para garantir que a ferramenta seja chamada com os argumentos corretos. Cada runtime tem sua própria solução para isso, por exemplo, Python usa Pydantic e TypeScript usa Zod. A ideia é que façamos o seguinte:

- Movemos a lógica para criar uma funcionalidade (ferramenta, recurso ou prompt) para sua pasta dedicada.
- Adicionamos uma forma de validar uma solicitação entrante que, por exemplo, pede para chamar uma ferramenta.

### Criar uma funcionalidade

Para criar uma funcionalidade, precisamos criar um ficheiro para essa funcionalidade e garantir que ele tenha os campos obrigatórios exigidos dessa funcionalidade. Os campos diferem um pouco entre ferramentas, recursos e prompts.

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
        # Validar entrada usando o modelo Pydantic
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # TODO: adicionar Pydantic, para que possamos criar um AddInputModel e validar os argumentos

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

Aqui você pode ver como fazemos o seguinte:

- Criamos um esquema usando Pydantic `AddInputModel` com campos `a` e `b` no ficheiro *schema.py*.
- Tentamos analisar a solicitação entrante para ser do tipo `AddInputModel`; se houver um desajuste nos parâmetros, isso falhará:

   ```python
   # add.py
    try:
        # Validar entrada usando modelo Pydantic
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")
   ```

Você pode escolher se coloca essa lógica de análise na chamada da ferramenta em si ou na função manipuladora.

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

// adicionar.ts
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

- No manipulador que lida com todas as chamadas de ferramentas, agora tentamos interpretar a solicitação entrante no esquema definido da ferramenta:

    ```typescript
    const Schema = tool.rawSchema;

    try {
       const input = Schema.parse(request.params.arguments);
    ```

    se funcionar, então procedemos a chamar a ferramenta real:

    ```typescript
    const result = await tool.callback(input);
    ```

Como pode ver, essa abordagem cria uma ótima arquitetura, pois tudo tem o seu lugar; o *server.ts* é um ficheiro muito pequeno que apenas liga os manipuladores de requisição, e cada funcionalidade está na sua respectiva pasta, i.e. tools/, resources/ ou prompts/.

Ótimo, vamos tentar construir isso a seguir.

## Exercício: Criar um servidor de baixo nível

Neste exercício, faremos o seguinte:

1. Criar um servidor de baixo nível que lide com a listagem de ferramentas e chamadas de ferramentas.
1. Implementar uma arquitetura que você possa expandir.
1. Adicionar validação para garantir que as chamadas das suas ferramentas sejam devidamente validadas.

### -1- Criar uma arquitetura

A primeira coisa que precisamos abordar é uma arquitetura que nos ajude a escalar conforme adicionamos mais funcionalidades, aqui está como fica:

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

Agora montámos uma arquitetura que garante que podemos facilmente adicionar novas ferramentas numa pasta tools. Sinta-se à vontade para seguir isso e adicionar subdiretórios para resources e prompts.

### -2- Criar uma ferramenta

Vamos ver como é criar uma ferramenta a seguir. Primeiro, ela precisa ser criada na sua subpasta *tool* assim:

**Python**

```python
from .schema import AddInputModel

async def add_handler(args) -> float:
    try:
        # Validar entrada usando modelo Pydantic
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # TODO: adicionar Pydantic, para podermos criar um AddInputModel e validar os args

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

Aqui vemos como definimos nome, descrição e esquema de entrada usando Pydantic e um manipulador que será invocado assim que essa ferramenta for chamada. Por fim, expomos `tool_add`, que é um dicionário contendo todas estas propriedades.

Temos também *schema.py*, que é usado para definir o esquema de entrada usado pela nossa ferramenta:

```python
from pydantic import BaseModel

class AddInputModel(BaseModel):
    a: float
    b: float
```

Também precisamos preencher *__init__.py* para garantir que a pasta tools seja tratada como um módulo. Além disso, precisamos expor os módulos dentro dela assim:

```python
from .add import tool_add

tools = {
  tool_add["name"] : tool_add
}
```

Podemos continuar a adicionar a este ficheiro conforme adicionamos mais ferramentas.

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

Aqui criamos um dicionário composto pelas propriedades:

- name, que é o nome da ferramenta.
- rawSchema, que é o esquema Zod, usado para validar solicitações entrantes para chamar esta ferramenta.
- inputSchema, este esquema será usado pelo manipulador.
- callback, que é usado para invocar a ferramenta.

Há também `Tool` que é usado para converter este dicionário num tipo que o manipulador do servidor mcp pode aceitar e fica assim:

```typescript
import { z } from 'zod';

export interface Tool {
    name: string;
    inputSchema: any;
    rawSchema: z.ZodTypeAny;
    callback: (args: z.infer<z.ZodTypeAny>) => Promise<{ content: { type: string; text: string }[] }>;
}
```

E há *schema.ts* onde armazenamos os esquemas de entrada para cada ferramenta, que fica assim, com apenas um esquema presente por agora, mas conforme adicionamos ferramentas podemos adicionar mais entradas:

```typescript
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });
```

Ótimo, vamos prosseguir para lidar com a listagem das nossas ferramentas a seguir.

### -3- Lidar com a listagem de ferramentas

Depois, para lidar com a listagem das nossas ferramentas, precisamos configurar um manipulador de requisição para isso. Aqui está o que precisamos adicionar ao ficheiro do servidor:

**Python**

```python
# código omitido para brevidade
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

Aqui, adicionamos o decorador `@server.list_tools` e a função que implementa `handle_list_tools`. Nesta última, precisamos produzir uma lista de ferramentas. Note como cada ferramenta precisa de ter um nome, descrição e inputSchema.

**TypeScript**

Para configurar o manipulador de requisição para listar ferramentas, precisamos chamar `setRequestHandler` no servidor com um esquema que se ajuste ao que estamos tentando fazer, neste caso `ListToolsRequestSchema`.

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
// código omitido para brevidade
import { tools } from './tools/index.js';

server.setRequestHandler(ListToolsRequestSchema, async (request) => {
  // Retorna a lista de ferramentas registadas
  return {
    tools: tools
  };
});
```

Ótimo, agora resolvemos a parte da listagem das ferramentas, vamos ver como poderíamos chamar as ferramentas a seguir.

### -4- Lidar com a chamada a uma ferramenta

Para chamar uma ferramenta, precisamos configurar outro manipulador de requisição, desta vez focado em lidar com uma solicitação que especifica qual funcionalidade chamar e com quais argumentos.

**Python**

Vamos usar o decorador `@server.call_tool` e implementar com uma função como `handle_call_tool`. Dentro dessa função, precisamos analisar o nome da ferramenta, seus argumentos e garantir que os argumentos sejam válidos para a ferramenta em questão. Podemos validar os argumentos nesta função ou depois, na própria ferramenta.

```python
@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict[str, str] | None
) -> list[types.TextContent]:
    
    # tools é um dicionário com os nomes das ferramentas como chaves
    if name not in tools.tools:
        raise ValueError(f"Unknown tool: {name}")
    
    tool = tools.tools[name]

    result = "default"
    try:
        # invocar a ferramenta
        result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)
    except Exception as e:
        raise ValueError(f"Error calling tool {name}: {str(e)}")

    return [
        types.TextContent(type="text", text=str(result))
    ]
```

Aqui está o que acontece:

- O nome da nossa ferramenta já está presente como o parâmetro de entrada `name`, assim como os nossos argumentos no dicionário `arguments`.

- A ferramenta é chamada com `result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)`. A validação dos argumentos acontece na propriedade `handler` que aponta para uma função; se falhar, vai levantar uma exceção.

Pronto, agora temos uma compreensão completa de listar e chamar ferramentas usando um servidor de baixo nível.

Veja o [exemplo completo](./code/README.md) aqui

## Exercício

Estenda o código que recebeu com várias ferramentas, recursos e prompts e reflita sobre como você nota que só precisa adicionar ficheiros na pasta tools e em nenhum outro lugar.

*Sem solução fornecida*

## Resumo

Neste capítulo, vimos como a abordagem do servidor de baixo nível funciona e como isso pode nos ajudar a criar uma arquitetura agradável para continuarmos a expandir. Também discutimos validação e foi mostrado como trabalhar com bibliotecas de validação para criar esquemas para validação de entradas.

## O que vem a seguir

- A seguir: [Autenticação simples](../11-simple-auth/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, por favor esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original no seu idioma nativo deve ser considerado a fonte autoritativa. Para informações críticas, recomenda-se tradução profissional efetuada por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações erradas decorrentes da utilização desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->