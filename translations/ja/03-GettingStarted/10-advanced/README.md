# 高度なサーバー使用法

MCP SDKには通常サーバーと低レベルサーバーの2種類のサーバーが公開されています。通常は、機能を追加するために通常のサーバーを使用します。ただし、以下のような特定のケースでは低レベルサーバーを使うことがあります：

- より良いアーキテクチャ。通常のサーバーと低レベルサーバーの両方でクリーンなアーキテクチャを作成することは可能ですが、低レベルサーバーのほうが多少簡単だと主張できます。
- 機能の利用可能性。高度な機能の一部は低レベルサーバーでしか使用できません。これについては、後の章でサンプリングや誘発を追加するときに見ることになります。

## 通常サーバーと低レベルサーバーの違い

通常サーバーでMCPサーバーを作成する例は以下のようになります。

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

つまり、サーバーに持たせたい各ツール、リソース、プロンプトを明示的に追加しているわけです。それ自体は問題ありません。

### 低レベルサーバーアプローチ

しかし、低レベルサーバーのアプローチを使う場合は考え方が異なります。各ツールを登録する代わりに、機能タイプごとに2つのハンドラを作成します（ツール、リソース、プロンプト）。例えばツールの場合、以下の2つの関数だけになります：

- すべてのツールをリストアップする。ツールを一覧表示しようとするすべての試みに対してこの関数が対応します。
- すべてのツール呼び出しを処理する。ここでも呼び出しは1つの関数で処理します。

これって作業が少なくなりそうですよね？ツールを登録する代わりに、ツール一覧取得時にツールがリストされ、ツールを呼び出すリクエストが来たら呼ばれるようにすれば良いわけです。

コードを見てみましょう。

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

ここでは機能の一覧を返す関数があります。toolsリストの各エントリは`name`、`description`、`inputSchema`などのフィールドを持ち、戻り値の型に準拠しています。これによりツールの定義を別場所に置くことが可能になります。すべてのツールをtoolsフォルダに作成し、同様にすべての機能を管理できるようになるので、プロジェクト構成は次のようにできます：

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

これによりアーキテクチャをきれいに保つことができます。

ツールの呼び出しはどうでしょうか？同じ考え方なのでしょうか？ある機能呼び出し用のハンドラが1つあれば良いのですか？ そうです、その通りです。コードは次のとおりです。

**Python**

```python
@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict[str, str] | None
) -> list[types.TextContent]:
    
    # tools はキーがツール名の辞書です
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

上のコードからわかるように、呼び出すツールの名前や引数を解析してからツールを呼び出す必要があります。

## バリデーションによる改善

これまでのところ、ツール、リソース、プロンプトを追加するための登録が機能タイプごとの2つのハンドラで置き換えられることを見てきました。では他に何が必要でしょうか？ツールが正しい引数で呼び出されていることを検証するための何らかのバリデーションが必要です。各ランタイムには独自のソリューションがあり、たとえばPythonはPydantic、TypeScriptはZodを使います。やるべきことは以下です：

- 機能（ツール、リソース、プロンプト）を専用フォルダに作成するロジックを移動する。
- 例えばツール呼び出しリクエストが正しいかどうかを検証する方法を追加する。

### 機能の作成

機能を作成するには、その機能用のファイルを作り、その機能に必要な必須フィールドを持たせる必要があります。フィールドはツール、リソース、プロンプトで少し異なります。

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
        # Pydanticモデルを使用して入力を検証する
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # TODO: Pydanticを追加して、AddInputModelを作成し、引数を検証できるようにすること

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

ここでは以下のことを行っています：

- Pydanticで`AddInputModel`というスキーマを*schema.py*ファイルで作成し、フィールド`a`と`b`を定義。
- 受け取ったリクエストを`AddInputModel`型にパースしようとし、不一致がある場合はクラッシュする：

   ```python
   # add.py
    try:
        # Pydanticモデルを使用して入力を検証する
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")
   ```

このパースロジックをツール呼び出し側かハンドラ内どちらに置くかは選択できます。

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

- すべてのツール呼び出しを処理するハンドラで、受信リクエストをツールが定義したスキーマにパースしようとします：

    ```typescript
    const Schema = tool.rawSchema;

    try {
       const input = Schema.parse(request.params.arguments);
    ```

    成功すれば実際にツールを呼び出します：

    ```typescript
    const result = await tool.callback(input);
    ```

この方法は優れたアーキテクチャを作ります。すべてに定位置があり、*server.ts*はリクエストハンドラをつなぐ非常に小さいファイルになり、各機能はそれぞれのフォルダ（tools/、resources/、prompts/）に分かれています。

さあ、次にこれを作成していきましょう。

## 演習：低レベルサーバーの作成

この演習で行うこと：

1. 低レベルサーバーを作り、ツールの一覧取得と呼び出しを処理する。
1. 拡張可能なアーキテクチャを実装する。
1. ツール呼び出しのバリデーションを追加し、正しく検証できるようにする。

### -1- アーキテクチャの作成

まず拡張しやすいアーキテクチャを用意します。以下のようになります：

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

これでtoolsフォルダに新しいツールを簡単に追加できるアーキテクチャを設定しました。resourcesとprompts用にサブディレクトリを作ることもできます。

### -2- ツールの作成

次にツールの作成を見てみましょう。まず*tool*サブディレクトリに次のように作成します：

**Python**

```python
from .schema import AddInputModel

async def add_handler(args) -> float:
    try:
        # Pydanticモデルを使用して入力を検証する
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # TODO: Pydanticを追加して、AddInputModelを作成しargsを検証できるようにする

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

ここでは名前、説明、Pydanticで作った入力スキーマを定義し、そのツールが呼ばれたときに実行するハンドラを用意しています。最後に`tool_add`として全プロパティを持つ辞書を公開しています。

またツール用の入力スキーマを定義する*schema.py*もあります：

```python
from pydantic import BaseModel

class AddInputModel(BaseModel):
    a: float
    b: float
```

toolsディレクトリをモジュールとして扱うため*__init__.py*も中身を用意する必要があります。同時にツール内のモジュールを公開するため次のような内容になります：

```python
from .add import tool_add

tools = {
  tool_add["name"] : tool_add
}
```

ツールを追加するたびにこのファイルを更新していきます。

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

ここでは以下のプロパティを持つ辞書を作成しています：

- name：ツールの名前。
- rawSchema：Zodのスキーマで、ツール呼び出しリクエストを検証するために使われる。
- inputSchema：ハンドラで利用されるスキーマ。
- callback：ツール呼び出しに使われる関数。

また`Tool`はこの辞書をmcpサーバーのハンドラが受け取れる型に変換します。内容は以下の通りです：

```typescript
import { z } from 'zod';

export interface Tool {
    name: string;
    inputSchema: any;
    rawSchema: z.ZodTypeAny;
    callback: (args: z.infer<z.ZodTypeAny>) => Promise<{ content: { type: string; text: string }[] }>;
}
```

inputスキーマは*schema.ts*にツールごとに保存され、現状は1つのスキーマだけですがツールを増やすごとに増やせます：

```typescript
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });
```

では、次はツールの一覧取得の処理を実装しましょう。

### -3- ツール一覧の処理

次にツール一覧取得を処理するリクエストハンドラを設定します。サーバーファイルに追加する内容は以下の通りです：

**Python**

```python
# 簡潔にするためにコードを省略しました
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

ここでは`@server.list_tools`デコレータを使用し、`handle_list_tools`関数を実装しています。この関数はツール一覧を作成し返します。ツールごとに`name`、`description`、`inputSchema`が必要な点に注意してください。

**TypeScript**

ツール一覧取得用のリクエストハンドラは、サーバーで`setRequestHandler`を呼び、取得用リクエストスキーマ（ここでは`ListToolsRequestSchema`）に合うように設定します。

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
// 簡潔にするためコードを省略
import { tools } from './tools/index.js';

server.setRequestHandler(ListToolsRequestSchema, async (request) => {
  // 登録されているツールのリストを返す
  return {
    tools: tools
  };
});
```

これでツール一覧処理ができました。次はツールの呼び出しを見てみましょう。

### -4- ツール呼び出しの処理

ツール呼び出しには、どの機能を呼び何の引数で呼ぶかを指定するリクエストハンドラを設定する必要があります。

**Python**

`@server.call_tool`デコレータを使い、`handle_call_tool`関数を実装します。この関数内で呼び出すツール名と引数を解析し、引数がツールで正しいか検証します。引数の検証はこの関数内または実際のツール側で行えます。

```python
@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict[str, str] | None
) -> list[types.TextContent]:
    
    # toolsは、ツール名をキーとする辞書です
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

処理の流れ：

- ツール名は入力パラメータの`name`に含まれています。引数は`arguments`辞書の形で渡されます。
- ツールは`result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)`で呼ばれます。引数の検証は`handler`にある関数で行われ、失敗すると例外が発生します。

これで低レベルサーバーを用いたツール一覧取得と呼び出しが理解できました。

[完全な例はこちら](./code/README.md)をご覧ください。

## 課題

提示されたコードにいくつかのツール、リソース、プロンプトを追加し、filesディレクトリに新規ファイルを追加するだけで他に変更が不要であることを実感してください。

*解答はありません*

## まとめ

この章では低レベルサーバーのアプローチを見て、クリーンな構築可能なアーキテクチャ作成が可能なことがわかりました。また、バリデーションや入力検証のスキーマ作成に関しても説明しました。

## 次回予告

- 次： [シンプル認証](../11-simple-auth/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責事項**：
本ドキュメントはAI翻訳サービス「Co-op Translator」（https://github.com/Azure/co-op-translator）を使用して翻訳されています。正確性を期しておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があることをご了承ください。原文の言語によるドキュメントが権威ある情報源とみなされます。重要な情報については、専門の人間による翻訳を推奨いたします。本翻訳の利用により生じたいかなる誤解や解釈違いについても責任を負いかねます。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->