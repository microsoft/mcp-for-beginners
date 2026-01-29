# Utilisation avancée du serveur

Il existe deux types de serveurs exposés dans le SDK MCP : le serveur classique et le serveur bas-niveau. En général, vous utilisez le serveur classique pour y ajouter des fonctionnalités. Cependant, dans certains cas, vous pourriez préférer utiliser le serveur bas-niveau, notamment pour :

- Une meilleure architecture. Bien qu'il soit possible de créer une architecture propre avec le serveur classique et le serveur bas-niveau, il est souvent considéré comme légèrement plus facile avec le serveur bas-niveau.
- Disponibilité des fonctionnalités. Certaines fonctionnalités avancées ne peuvent être utilisées qu'avec un serveur bas-niveau. Vous verrez cela dans les chapitres suivants lorsque nous ajouterons l'échantillonnage et l'élucidation.

## Serveur classique vs serveur bas-niveau

Voici à quoi ressemble la création d'un serveur MCP avec le serveur classique :

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

L'idée ici est que vous ajoutez explicitement chaque outil, ressource ou invite que vous souhaitez que le serveur possède. Rien de problématique à cela.  

### Approche du serveur bas-niveau

Cependant, lorsque vous utilisez l'approche du serveur bas-niveau, vous devez penser différemment. Au lieu d'enregistrer chaque outil, vous créez deux gestionnaires par type de fonctionnalité (outils, ressources ou invites). Par exemple, pour les outils, vous n'avez que deux fonctions comme suit :

- Lister tous les outils. Une fonction est responsable de toutes les tentatives de lister les outils.
- Gérer l'appel de tous les outils. Ici aussi, une seule fonction gère les appels à un outil.

Cela semble être potentiellement moins de travail, non ? Donc, au lieu d'enregistrer un outil, je dois simplement m'assurer que l'outil est listé lorsque je liste tous les outils et qu'il est appelé lorsqu'une requête arrive pour appeler un outil.

Voyons à quoi ressemble le code maintenant :

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

Ici, nous avons maintenant une fonction qui retourne une liste de fonctionnalités. Chaque entrée dans la liste des outils possède désormais des champs comme `name`, `description` et `inputSchema` pour respecter le type de retour. Cela nous permet de définir nos outils et fonctionnalités ailleurs. Nous pouvons maintenant créer tous nos outils dans un dossier dédié et faire de même pour toutes vos fonctionnalités, ce qui permet à votre projet d'être organisé comme suit :

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

C'est génial, notre architecture peut être rendue assez propre.

Qu'en est-il de l'appel des outils ? Est-ce la même idée, un gestionnaire pour appeler un outil, quel qu'il soit ? Oui, exactement, voici le code pour cela :

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

Comme vous pouvez le voir dans le code ci-dessus, nous devons extraire l'outil à appeler, avec quels arguments, puis procéder à l'appel de l'outil.

## Améliorer l'approche avec la validation

Jusqu'à présent, vous avez vu comment toutes vos inscriptions pour ajouter des outils, des ressources et des invites peuvent être remplacées par ces deux gestionnaires par type de fonctionnalité. Que devons-nous faire d'autre ? Eh bien, nous devrions ajouter une forme de validation pour garantir que l'outil est appelé avec les bons arguments. Chaque runtime a sa propre solution pour cela, par exemple Python utilise Pydantic et TypeScript utilise Zod. L'idée est de faire ce qui suit :

- Déplacer la logique de création d'une fonctionnalité (outil, ressource ou invite) dans son dossier dédié.
- Ajouter un moyen de valider une requête entrante demandant, par exemple, d'appeler un outil.

### Créer une fonctionnalité

Pour créer une fonctionnalité, nous devons créer un fichier pour cette fonctionnalité et nous assurer qu'il contient les champs obligatoires requis pour cette fonctionnalité. Les champs diffèrent légèrement entre les outils, les ressources et les invites.

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

Ici, vous pouvez voir comment nous faisons ce qui suit :

- Créer un schéma en utilisant Pydantic `AddInputModel` avec les champs `a` et `b` dans le fichier *schema.py*.
- Tenter de parser la requête entrante pour qu'elle soit de type `AddInputModel`. Si les paramètres ne correspondent pas, cela échouera :

   ```python
   # add.py
    try:
        # Validate input using Pydantic model
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")
   ```

Vous pouvez choisir de placer cette logique de parsing dans l'appel de l'outil lui-même ou dans la fonction du gestionnaire.

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

- Dans le gestionnaire qui traite tous les appels d'outils, nous essayons maintenant de parser la requête entrante dans le schéma défini de l'outil :

    ```typescript
    const Schema = tool.rawSchema;

    try {
       const input = Schema.parse(request.params.arguments);
    ```

    si cela fonctionne, nous procédons à l'appel de l'outil réel :

    ```typescript
    const result = await tool.callback(input);
    ```

Comme vous pouvez le voir, cette approche crée une excellente architecture où tout a sa place. Le fichier *server.ts* est très petit et ne fait que connecter les gestionnaires de requêtes, tandis que chaque fonctionnalité est dans son dossier respectif, c'est-à-dire tools/, resources/ ou prompts/.

Super, essayons de construire cela maintenant.

## Exercice : Créer un serveur bas-niveau

Dans cet exercice, nous allons faire ce qui suit :

1. Créer un serveur bas-niveau gérant la liste des outils et l'appel des outils.
1. Implémenter une architecture sur laquelle vous pouvez construire.
1. Ajouter une validation pour garantir que vos appels d'outils sont correctement validés.

### -1- Créer une architecture

La première chose à aborder est une architecture qui nous aide à évoluer à mesure que nous ajoutons plus de fonctionnalités. Voici à quoi cela ressemble :

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

Nous avons maintenant mis en place une architecture qui garantit que nous pouvons facilement ajouter de nouveaux outils dans un dossier tools. N'hésitez pas à suivre cela pour ajouter des sous-répertoires pour les ressources et les invites.

### -2- Créer un outil

Voyons à quoi ressemble la création d'un outil. Tout d'abord, il doit être créé dans son sous-répertoire *tool* comme suit :

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

Ce que nous voyons ici, c'est comment nous définissons le nom, la description, un schéma d'entrée en utilisant Pydantic et un gestionnaire qui sera invoqué une fois que cet outil sera appelé. Enfin, nous exposons `tool_add`, qui est un dictionnaire contenant toutes ces propriétés.

Il y a aussi *schema.py*, utilisé pour définir le schéma d'entrée utilisé par notre outil :

```python
from pydantic import BaseModel

class AddInputModel(BaseModel):
    a: float
    b: float
```

Nous devons également remplir *__init__.py* pour garantir que le répertoire tools est traité comme un module. De plus, nous devons exposer les modules qu'il contient comme suit :

```python
from .add import tool_add

tools = {
  tool_add["name"] : tool_add
}
```

Nous pouvons continuer à ajouter à ce fichier à mesure que nous ajoutons plus d'outils.

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

Ici, nous créons un dictionnaire composé de propriétés :

- name, c'est le nom de l'outil.
- rawSchema, c'est le schéma Zod, il sera utilisé pour valider les requêtes entrantes pour appeler cet outil.
- inputSchema, ce schéma sera utilisé par le gestionnaire.
- callback, utilisé pour invoquer l'outil.

Il y a aussi `Tool`, utilisé pour convertir ce dictionnaire en un type que le gestionnaire du serveur MCP peut accepter, et cela ressemble à ceci :

```typescript
import { z } from 'zod';

export interface Tool {
    name: string;
    inputSchema: any;
    rawSchema: z.ZodTypeAny;
    callback: (args: z.infer<z.ZodTypeAny>) => Promise<{ content: { type: string; text: string }[] }>;
}
```

Et il y a *schema.ts*, où nous stockons les schémas d'entrée pour chaque outil, qui ressemble à ceci avec un seul schéma pour l'instant, mais à mesure que nous ajoutons des outils, nous pouvons ajouter plus d'entrées :

```typescript
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });
```

Super, passons à la gestion de la liste de nos outils.

### -3- Gérer la liste des outils

Ensuite, pour gérer la liste de nos outils, nous devons configurer un gestionnaire de requêtes pour cela. Voici ce que nous devons ajouter à notre fichier serveur :

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

Ici, nous ajoutons le décorateur `@server.list_tools` et la fonction d'implémentation `handle_list_tools`. Dans cette dernière, nous devons produire une liste d'outils. Notez que chaque outil doit avoir un nom, une description et un inputSchema.   

**TypeScript**

Pour configurer le gestionnaire de requêtes pour lister les outils, nous devons appeler `setRequestHandler` sur le serveur avec un schéma correspondant à ce que nous essayons de faire, dans ce cas `ListToolsRequestSchema`. 

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

Super, nous avons maintenant résolu la partie de la liste des outils. Regardons comment nous pourrions appeler des outils ensuite.

### -4- Gérer l'appel d'un outil

Pour appeler un outil, nous devons configurer un autre gestionnaire de requêtes, cette fois axé sur le traitement d'une requête spécifiant quelle fonctionnalité appeler et avec quels arguments.

**Python**

Utilisons le décorateur `@server.call_tool` et implémentons-le avec une fonction comme `handle_call_tool`. Dans cette fonction, nous devons extraire le nom de l'outil, ses arguments et garantir que les arguments sont valides pour l'outil en question. Nous pouvons valider les arguments dans cette fonction ou en aval dans l'outil lui-même.

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

Voici ce qui se passe :

- Le nom de notre outil est déjà présent en tant que paramètre d'entrée `name`, ce qui est également vrai pour nos arguments sous forme de dictionnaire `arguments`.

- L'outil est appelé avec `result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)`. La validation des arguments se produit dans la propriété `handler`, qui pointe vers une fonction. Si cela échoue, une exception sera levée. 

Voilà, nous avons maintenant une compréhension complète de la liste et de l'appel des outils en utilisant un serveur bas-niveau.

Voir l'[exemple complet](./code/README.md) ici.

## Devoir

Étendez le code qui vous a été donné avec plusieurs outils, ressources et invites, et réfléchissez à la manière dont vous remarquez que vous n'avez besoin d'ajouter des fichiers que dans le répertoire tools et nulle part ailleurs. 

*Aucune solution donnée*

## Résumé

Dans ce chapitre, nous avons vu comment fonctionne l'approche du serveur bas-niveau et comment cela peut nous aider à créer une architecture propre sur laquelle nous pouvons continuer à construire. Nous avons également discuté de la validation et vous avez vu comment travailler avec des bibliothèques de validation pour créer des schémas de validation des entrées.

---

**Avertissement** :  
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, il est recommandé de recourir à une traduction humaine professionnelle. Nous déclinons toute responsabilité en cas de malentendus ou d'interprétations erronées résultant de l'utilisation de cette traduction.