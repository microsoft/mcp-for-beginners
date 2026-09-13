# 高度なサーバー使用法

MCP SDKでは、通常のサーバーと低レベルサーバーの2種類のサーバーが利用可能です。通常は、機能を追加するために通常のサーバーを使用しますが、以下のような場合は低レベルサーバーに依存したいことがあります。

- より優れたアーキテクチャ。通常のサーバーと低レベルサーバーの両方でクリーンなアーキテクチャを作成できますが、低レベルサーバーの方がやや簡単だと言えます。
- 機能の利用可能性。一部の高度な機能は
    低レベルサーバーでのみ利用可能です。後の章ではElicitationや
    MCP `2026-07-28`で非推奨になったレガシーのSampling機能について扱います。

## 通常のサーバーと低レベルサーバーの違い

こちらは通常のサーバーでのMCPサーバーの作成例です。

**Python**

```python
mcp = FastMCP("Demo")

# 追加ツールを追加する
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

// 追加ツールを追加する
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

ポイントは、サーバーに持たせたいツールやリソース、プロンプトを明示的に追加していることです。これ自体に問題はありません。  

### 低レベルサーバーのアプローチ

しかし、低レベルサーバーの方法では考え方を変える必要があります。各ツールを登録する代わりに、各機能タイプ（ツール、リソース、プロンプト）ごとに2つのハンドラーを作成します。例えばツールなら、次の2つの関数のみです。

- すべてのツールの一覧取得。すべてのツール一覧取得要求を処理する1つの関数。
- すべてのツール呼び出し処理。これも1つの関数でツール呼び出しを処理。

これなら作業が減りそうですよね？ツールを登録するのではなく、ツール一覧取得でツールがきちんと一覧表示され、ツール呼び出しのリクエストが入ったときに呼び出されるようにすれば良いのです。

さあ、このコードがどのようになるか見てみましょう。

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
  // 登録されたツールのリストを返します
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

ここでは、機能のリストを返す関数があります。ツールリストの各エントリは`name`、`description`、`inputSchema`などのフィールドを持ち、返却型を満たしています。これによりツールと機能の定義を別の場所に配置できます。すべてのツールをtoolsフォルダーに置き、同様に機能もプロジェクトを次のように整理できます。

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

これは素晴らしいことで、クリーンなアーキテクチャにできます。

ツールの呼び出しはどうでしょう？どのツールでも呼び出す1つのハンドラーという考えで同じですか？はい、その通りです。以下がそのコードです。

**Python**

```python
@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict[str, str] | None
) -> list[types.TextContent]:
    
    # tools はツール名をキーとする辞書です
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
    // TODO ツールを呼び出す,

    return {
       content: [{ type: "text", text: `Tool ${name} called with arguments: ${JSON.stringify(input)}, result: ${JSON.stringify(result)}` }]
    };
});
```

上のコードからわかるように、呼び出すツールとその引数を解析し、その後でツールを呼び出す必要があります。

## バリデーションによるアプローチの改善

これまで、ツール・リソース・プロンプトの登録を各機能タイプごとに2つのハンドラーで置き換える方法を見てきました。これ以外に何が必要でしょうか？そうです。ツールが正しい引数で呼ばれているか検証するバリデーションを追加すべきです。各ランタイムには独自の解決方法があり、PythonはPydantic、TypeScriptはZodを使います。以下のように行います。

- 機能（ツール、リソース、プロンプト）を作成するロジックを専用のフォルダーに移動。
- 例えばツール呼び出し要求が正しいかをバリデートする方法を追加。

### 機能を作成する

機能を作成するには、その機能用のファイルを作成し、その機能に求められる必須フィールドを持つようにします。ツール、リソース、プロンプトで少し異なります。

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
        # Pydanticモデルを使って入力を検証する
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # TODO: Pydanticを追加して、AddInputModelを作成し、引数を検証できるようにする

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

ここでは次のことを行っています。

- Pydanticの`AddInputModel`スキーマにフィールド`a`と`b`を<em>schema.py</em>に定義。
- 受信リクエストを`AddInputModel`型で解析しようとし、パラメータが合わなければクラッシュします：

   ```python
   # add.py
    try:
        # Pydanticモデルを使用して入力を検証する
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")
   ```

この解析ロジックをツールの呼び出し内部に置くか、ハンドラー関数で行うかは選べます。

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

- 全ツール呼び出しを扱うハンドラーで、受信リクエストをツールの定義スキーマに解析しようとします：

    ```typescript
    const Schema = tool.rawSchema;

    try {
       const input = Schema.parse(request.params.arguments);
    ```

　　解析に成功したら実際のツール呼び出しを行います：

    ```typescript
    const result = await tool.callback(input);
    ```

この方法は素晴らしいアーキテクチャを生み出し、<em>server.ts</em>はリクエストハンドラーを結線するだけの非常に小さいファイルになり、各機能はそれぞれのフォルダー（tools/、resources/ または prompts/）にまとめられます。

さあ、次はこれを実装してみましょう。

## 演習：低レベルサーバーの作成

この演習では以下を行います。

1. ツール一覧取得とツール呼び出しを処理する低レベルサーバーを作成。
1. そこから発展可能なアーキテクチャを実装。
1. ツール呼び出しが正しくバリデートされるようバリデーションを追加。

### -1- アーキテクチャの作成

最初に取り組むべきは、機能を追加しても拡張できるアーキテクチャの設計です。以下のようになります。

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

これでtoolsフォルダーに新しいツールを簡単に追加できるアーキテクチャが整いました。必要に応じてresourcesやprompts用のサブディレクトリもこのように追加してください。

### -2- ツールの作成

次にツール作成の様子を見てみましょう。まず<em>tool</em>サブディレクトリ内に次のように作成します。

**Python**

```python
from .schema import AddInputModel

async def add_handler(args) -> float:
    try:
        # Pydanticモデルを使用して入力を検証する
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # TODO: Pydanticを追加して、AddInputModelを作成し、引数を検証できるようにする

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

ここでは名前、説明、入力スキーマをPydanticで定義し、このツールが呼ばれたときに呼ばれるハンドラー関数を持っています。最後に`tool_add`というこれらのプロパティを保持する辞書を公開しています。

<em>schema.py</em>もあり、ツールで用いる入力スキーマを定義しています：

```python
from pydantic import BaseModel

class AddInputModel(BaseModel):
    a: float
    b: float
```

また、toolsディレクトリをモジュールとして扱うために<em>__init__.py</em>も充実させる必要があります。さらに、内部のモジュールを次のように公開します：

```python
from .add import tool_add

tools = {
  tool_add["name"] : tool_add
}
```

ツールが増えたらこのファイルにも追加していきます。

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

ここでは以下のプロパティ辞書を作成しています：

- name：ツール名。
- rawSchema：Zodスキーマで、ツール呼び出しの検証に使われます。
- inputSchema：処理ハンドラーで使用するスキーマ。
- callback：ツールを呼び出すために使われます。

`Tool`はこの辞書をmcpサーバーハンドラーで受け取れる型に変換するもので、次のようになります：

```typescript
import { z } from 'zod';

export interface Tool {
    name: string;
    inputSchema: any;
    rawSchema: z.ZodTypeAny;
    callback: (args: z.infer<z.ZodTypeAny>) => Promise<{ content: { type: string; text: string }[] }>;
}
```

<em>schema.ts</em>ではツールごとの入力スキーマを管理しており、現在は1つのスキーマですが、ツール追加に伴い増やせます：

```typescript
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });
```

それでは次にツール一覧取得の処理を見ていきましょう。

### -3- ツール一覧取得の処理

次にツール一覧取得のハンドラーを用意します。以下のようにサーバーファイルに追加します：

**Python**

```python
# 簡潔にするためコードを省略しました
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

ここではデコレーター`@server.list_tools`を追加し、それを実装する`handle_list_tools`関数を実装します。この関数でツールのリストを返します。各ツールにはname、description、inputSchemaが必要です。   

**TypeScript**

ツール一覧取得のリクエストハンドラーは、サーバーの`setRequestHandler`に、目的に合ったスキーマ（ここでは`ListToolsRequestSchema`）を渡して設定します。 

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
// 簡略化のためコード省略
import { tools } from './tools/index.js';

server.setRequestHandler(ListToolsRequestSchema, async (request) => {
  // 登録されたツールの一覧を返す
  return {
    tools: tools
  };
});
```

これでツール一覧取得ができるようになりました。次にツール呼び出しの処理を見ていきましょう。

### -4- ツール呼び出しの処理

ツール呼び出しのため、どの機能をどの引数で呼ぶかを処理するリクエストハンドラーを用意します。

**Python**

デコレーター`@server.call_tool`を使い、`handle_call_tool`関数を実装します。この関数でツール名と引数を解析し、引数がそのツールに適切か検証します。この検証はここで行うか、実際のツール内で行ってもよいです。

```python
@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict[str, str] | None
) -> list[types.TextContent]:
    
    # tools はツール名をキーとする辞書です
    if name not in tools.tools:
        raise ValueError(f"Unknown tool: {name}")
    
    tool = tools.tools[name]

    result = "default"
    try:
        # ツールを呼び出す
        result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)
    except Exception as e:
        raise ValueError(f"Error calling tool {name}: {str(e)}")

    return [
        types.TextContent(type="text", text=str(result))
    ]
```

ここで行われる処理は：

- ツール名はすでに入力パラメータ`name`として渡され、引数は`arguments`辞書の形で渡されます。

- ツールは`result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)`で呼び出されます。引数検証は`handler`関数内で行われるので失敗すれば例外が発生します。

これで低レベルサーバーを使ったツール一覧・呼び出しの全体像がわかりました。

こちらに[完全な例](./code/README.md)があります

## 課題

渡されたコードに複数のツール、リソース、プロンプトを追加し、toolsディレクトリにファイルを追加するだけで済むことに気づくことを振り返ってください。 

<em>解答はありません</em>

## まとめ

本章では低レベルサーバーのアプローチの仕組みと、それを用いて拡張可能なクリーンなアーキテクチャを作る方法を見ました。また、バリデーションについて説明し、入力検証用のスキーマ作成方法としてバリデーションライブラリの活用方法を示しました。

## 次に進むには

- 次へ：[シンプル認証](../11-simple-auth/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責事項**：
本書類は AI 翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されています。正確性を期していますが、自動翻訳には誤りや不正確な部分が含まれる可能性があることをご承知おきください。原文の原語版が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用により生じたいかなる誤解や解釈違いについても、当方は責任を負いかねます。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->