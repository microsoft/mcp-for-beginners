# Visual Studio CodeのAI Toolkit拡張機能を使用したサーバーの利用

AIエージェントを構築する際、賢い応答を生成するだけでなく、エージェントに行動を起こす能力を与えることが重要です。そこで登場するのがModel Context Protocol (MCP)です。MCPを使用すると、エージェントが外部ツールやサービスに一貫した方法でアクセスできるようになります。まるでエージェントを実際に使えるツールボックスに接続するようなものです。

例えば、エージェントを計算機MCPサーバーに接続すると、エージェントは「47×89は何ですか？」といったプロンプトを受け取るだけで数学演算を実行できるようになります。ロジックをハードコーディングしたり、カスタムAPIを構築したりする必要はありません。

## 概要

このレッスンでは、Visual Studio Codeの[AI Toolkit](https://aka.ms/AIToolkit)拡張機能を使用して、計算機MCPサーバーをエージェントに接続する方法を学びます。これにより、エージェントは自然言語を通じて加算、減算、乗算、除算などの数学演算を実行できるようになります。

AI Toolkitは、エージェント開発を効率化する強力なVisual Studio Code拡張機能です。AIエンジニアは、生成AIモデルをローカルまたはクラウドで開発・テストすることで、AIアプリケーションを簡単に構築できます。この拡張機能は、現在利用可能な主要な生成モデルのほとんどをサポートしています。

*注*: AI Toolkitは現在、PythonとTypeScriptをサポートしています。

## 学習目標

このレッスンを終えると、以下ができるようになります：

- AI Toolkitを使用してMCPサーバーを利用する。
- MCPサーバーが提供するツールを発見・利用できるようにエージェント設定を構成する。
- 自然言語を通じてMCPツールを活用する。

## アプローチ

以下は全体的なアプローチです：

- エージェントを作成し、そのシステムプロンプトを定義する。
- 計算機ツールを備えたMCPサーバーを作成する。
- Agent BuilderをMCPサーバーに接続する。
- 自然言語を通じてエージェントのツール呼び出しをテストする。

では、エージェントの能力を向上させるために、MCPを通じて外部ツールを活用する設定を行いましょう！

## 前提条件

- [Visual Studio Code](https://code.visualstudio.com/)
- [Visual Studio Code用AI Toolkit](https://aka.ms/AIToolkit)

## 演習: サーバーの利用

> [!WARNING]
> macOSユーザーへの注意。現在、macOSでの依存関係インストールに影響を与える問題を調査中です。そのため、macOSユーザーは現時点でこのチュートリアルを完了することができません。修正が完了次第、手順を更新します。ご理解とご協力をお願いいたします。

この演習では、Visual Studio Code内でAI Toolkitを使用して、MCPサーバーのツールを備えたAIエージェントを構築、実行、強化します。

### -0- 事前準備: OpenAI GPT-4oモデルをMy Modelsに追加する

この演習では**GPT-4o**モデルを使用します。エージェントを作成する前に、このモデルを**My Models**に追加してください。

1. **Activity Bar**から**AI Toolkit**拡張機能を開きます。
1. **Catalog**セクションで**Models**を選択し、**Model Catalog**を開きます。**Models**を選択すると、新しいエディタタブで**Model Catalog**が開きます。
1. **Model Catalog**の検索バーに**OpenAI GPT-4o**を入力します。
1. **+ Add**をクリックしてモデルを**My Models**リストに追加します。**GitHubでホストされている**モデルを選択していることを確認してください。
1. **Activity Bar**で**OpenAI GPT-4o**モデルがリストに表示されていることを確認します。

### -1- エージェントを作成する

**Agent (Prompt) Builder**を使用すると、自分専用のAIエージェントを作成してカスタマイズできます。このセクションでは、新しいエージェントを作成し、会話を動かすモデルを割り当てます。

1. **Activity Bar**から**AI Toolkit**拡張機能を開きます。
1. **Tools**セクションで**Agent (Prompt) Builder**を選択します。**Agent (Prompt) Builder**を選択すると、新しいエディタタブで**Agent (Prompt) Builder**が開きます。
1. **+ New Agent**ボタンをクリックします。拡張機能が**Command Palette**を通じてセットアップウィザードを起動します。
1. **Calculator Agent**という名前を入力し、**Enter**を押します。
1. **Agent (Prompt) Builder**で、**Model**フィールドに**OpenAI GPT-4o (via GitHub)**モデルを選択します。

### -2- エージェントのシステムプロンプトを作成する

エージェントの枠組みができたら、その性格と目的を定義します。このセクションでは、**Generate system prompt**機能を使用して、エージェントの意図する動作を説明します。この場合、計算機エージェントとしての役割を設定し、モデルにシステムプロンプトを書かせます。

1. **Prompts**セクションで**Generate system prompt**ボタンをクリックします。このボタンをクリックすると、プロンプトビルダーが開き、AIを活用してエージェントのシステムプロンプトを生成します。
1. **Generate a prompt**ウィンドウで以下を入力します：`あなたは役立つ効率的な数学アシスタントです。基本的な算術に関する問題が与えられた場合、正しい結果を返答します。`
1. **Generate**ボタンをクリックします。右下に通知が表示され、システムプロンプトが生成されていることを確認できます。プロンプト生成が完了すると、**Agent (Prompt) Builder**の**System prompt**フィールドにプロンプトが表示されます。
1. **System prompt**を確認し、必要に応じて修正します。

### -3- MCPサーバーを作成する

エージェントのシステムプロンプトを定義し、その動作と応答を導いたら、次はエージェントに実用的な能力を装備します。このセクションでは、加算、減算、乗算、除算を実行するツールを備えた計算機MCPサーバーを作成します。このサーバーにより、エージェントは自然言語プロンプトに応じてリアルタイムで数学演算を実行できるようになります。

AI Toolkitには、独自のMCPサーバーを簡単に作成するためのテンプレートが用意されています。ここでは、計算機MCPサーバーを作成するためにPythonテンプレートを使用します。

*注*: AI Toolkitは現在、PythonとTypeScriptをサポートしています。

1. **Agent (Prompt) Builder**の**Tools**セクションで**+ MCP Server**ボタンをクリックします。拡張機能が**Command Palette**を通じてセットアップウィザードを起動します。
1. **+ Add Server**を選択します。
1. **Create a New MCP Server**を選択します。
1. **python-weather**をテンプレートとして選択します。
1. **Default folder**を選択してMCPサーバーテンプレートを保存します。
1. サーバー名として以下を入力します：**Calculator**
1. 新しいVisual Studio Codeウィンドウが開きます。**Yes, I trust the authors**を選択します。
1. **Terminal**（**Terminal** > **New Terminal**）を使用して仮想環境を作成します：`python -m venv .venv`
1. **Terminal**を使用して仮想環境を有効化します：
    1. Windows - `.venv\Scripts\activate`
    1. macOS/Linux - `source .venv/bin/activate`
1. **Terminal**を使用して依存関係をインストールします：`pip install -e .[dev]`
1. **Activity Bar**の**Explorer**ビューで**src**ディレクトリを展開し、**server.py**を選択してファイルをエディタで開きます。
1. **server.py**ファイルのコードを以下に置き換え、保存します：

    ```python
    """
    Sample MCP Calculator Server implementation in Python.

    
    This module demonstrates how to create a simple MCP server with calculator tools
    that can perform basic arithmetic operations (add, subtract, multiply, divide).
    """
    
    from mcp.server.fastmcp import FastMCP
    
    server = FastMCP("calculator")
    
    @server.tool()
    def add(a: float, b: float) -> float:
        """Add two numbers together and return the result."""
        return a + b
    
    @server.tool()
    def subtract(a: float, b: float) -> float:
        """Subtract b from a and return the result."""
        return a - b
    
    @server.tool()
    def multiply(a: float, b: float) -> float:
        """Multiply two numbers together and return the result."""
        return a * b
    
    @server.tool()
    def divide(a: float, b: float) -> float:
        """
        Divide a by b and return the result.
        
        Raises:
            ValueError: If b is zero
        """
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
    ```

### -4- 計算機MCPサーバーでエージェントを実行する

エージェントにツールが追加されたので、次はそれを使用します！このセクションでは、エージェントにプロンプトを送信し、計算機MCPサーバーの適切なツールを活用するかどうかをテスト・検証します。

1. `F5`を押してMCPサーバーのデバッグを開始します。**Agent (Prompt) Builder**が新しいエディタタブで開きます。サーバーのステータスはターミナルで確認できます。
1. **Agent (Prompt) Builder**の**User prompt**フィールドに以下のプロンプトを入力します：`私は3つの商品をそれぞれ25ドルで購入し、20ドルの割引を使用しました。いくら支払いましたか？`
1. **Run**ボタンをクリックしてエージェントの応答を生成します。
1. エージェントの出力を確認します。モデルは**55ドル**を支払ったと結論付けるはずです。
1. 以下が発生するはずです：
    - エージェントが計算を補助するために**multiply**と**subtract**ツールを選択します。
    - **multiply**ツールにそれぞれの`a`と`b`値が割り当てられます。
    - **subtract**ツールにそれぞれの`a`と`b`値が割り当てられます。
    - 各ツールからの応答がそれぞれ**Tool Response**に提供されます。
    - モデルからの最終出力が**Model Response**に提供されます。
1. 追加のプロンプトを送信してエージェントをさらにテストします。**User prompt**フィールドで既存のプロンプトをクリックして置き換えることで、プロンプトを変更できます。
1. テストが終了したら、**terminal**で**CTRL/CMD+C**を入力してサーバーを停止します。

## 課題

**server.py**ファイルに追加のツールエントリ（例: 数値の平方根を返す）を追加してみてください。エージェントが新しいツール（または既存のツール）を活用する必要があるプロンプトを送信してください。新しく追加したツールを読み込むには、サーバーを再起動する必要があります。

## 解答

[解答](./solution/README.md)

## 重要なポイント

この章の重要なポイントは以下の通りです：

- AI Toolkit拡張機能は、MCPサーバーとそのツールを利用するための優れたクライアントです。
- MCPサーバーに新しいツールを追加することで、エージェントの能力を拡張し、進化する要件に対応できます。
- AI Toolkitにはカスタムツールの作成を簡素化するテンプレート（例: Python MCPサーバーテンプレート）が含まれています。

## 追加リソース

- [AI Toolkit ドキュメント](https://aka.ms/AIToolkit/doc)

## 次のステップ
- 次: [テストとデバッグ](../08-testing/README.md)

**免責事項**:  
この文書は、AI翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されています。正確性を追求しておりますが、自動翻訳には誤りや不正確さが含まれる可能性があります。元の言語で記載された原文が正式な情報源と見なされるべきです。重要な情報については、専門の人間による翻訳を推奨します。この翻訳の使用に起因する誤解や誤訳について、当社は一切の責任を負いません。
