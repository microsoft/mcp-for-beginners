<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "6fb74f952ab79ed4b4a33fda5fa04ecb",
  "translation_date": "2025-07-31T01:15:38+00:00",
  "source_file": "03-GettingStarted/07-aitk/README.md",
  "language_code": "ja"
}
-->
# Visual Studio CodeのAI Toolkit拡張機能を使ったサーバーの利用

AIエージェントを構築する際、単に賢い応答を生成するだけでなく、エージェントに行動を起こす能力を与えることが重要です。そこで登場するのがModel Context Protocol (MCP)です。MCPを使えば、エージェントが外部ツールやサービスに一貫した方法でアクセスできるようになります。まるでエージェントを実際に使えるツールボックスに接続するようなものです。

例えば、エージェントを電卓MCPサーバーに接続したとしましょう。すると、エージェントは「47×89は？」のようなプロンプトを受け取るだけで計算を実行できるようになります。ロジックをハードコーディングしたり、カスタムAPIを構築したりする必要はありません。

## 概要

このレッスンでは、Visual Studio Codeの[AI Toolkit](https://aka.ms/AIToolkit)拡張機能を使って、電卓MCPサーバーをエージェントに接続する方法を学びます。これにより、エージェントは自然言語を通じて加算、減算、乗算、除算といった数学的操作を実行できるようになります。

AI Toolkitは、エージェント開発を効率化するための強力なVisual Studio Code拡張機能です。AIエンジニアは、この拡張機能を使って、ローカルまたはクラウド上で生成AIモデルを開発・テストし、AIアプリケーションを簡単に構築できます。この拡張機能は、現在利用可能な主要な生成モデルのほとんどをサポートしています。

*注*: AI Toolkitは現在、PythonとTypeScriptをサポートしています。

## 学習目標

このレッスンを終えると、次のことができるようになります：

- AI Toolkitを使ってMCPサーバーを利用する。
- MCPサーバーが提供するツールを発見し利用できるように、エージェント設定を構成する。
- 自然言語を通じてMCPツールを活用する。

## アプローチ

以下のような高レベルの手順で進めます：

- エージェントを作成し、そのシステムプロンプトを定義する。
- 電卓ツールを備えたMCPサーバーを作成する。
- Agent BuilderをMCPサーバーに接続する。
- 自然言語を通じてエージェントのツール呼び出しをテストする。

では、MCPを通じて外部ツールを活用し、エージェントの能力を強化する設定を始めましょう！

## 前提条件

- [Visual Studio Code](https://code.visualstudio.com/)
- [Visual Studio Code用AI Toolkit](https://aka.ms/AIToolkit)

## 演習: サーバーの利用

> [!WARNING]
> macOSユーザーへの注意: 現在、macOSでの依存関係インストールに影響を与える問題を調査中です。そのため、macOSユーザーは現時点でこのチュートリアルを完了することができません。修正が完了次第、手順を更新します。ご理解とご協力に感謝します！

この演習では、Visual Studio Code内でAI Toolkitを使用して、MCPサーバーのツールを備えたAIエージェントを構築、実行、強化します。

### -0- 事前準備: OpenAI GPT-4oモデルをMy Modelsに追加する

この演習では**GPT-4o**モデルを使用します。エージェントを作成する前に、このモデルを**My Models**に追加してください。

1. **Activity Bar**から**AI Toolkit**拡張機能を開きます。
1. **Catalog**セクションで**Models**を選択し、**Model Catalog**を開きます。**Models**を選択すると、新しいエディタタブで**Model Catalog**が開きます。
1. **Model Catalog**の検索バーに**OpenAI GPT-4o**と入力します。
1. **+ Add**をクリックして、モデルを**My Models**リストに追加します。**GitHubでホストされている**モデルを選択したことを確認してください。
1. **Activity Bar**で、**OpenAI GPT-4o**モデルがリストに表示されていることを確認します。

### -1- エージェントを作成する

**Agent (Prompt) Builder**を使うと、自分専用のAIエージェントを作成し、カスタマイズできます。このセクションでは、新しいエージェントを作成し、会話を動かすモデルを割り当てます。

1. **Activity Bar**から**AI Toolkit**拡張機能を開きます。
1. **Tools**セクションで**Agent (Prompt) Builder**を選択します。**Agent (Prompt) Builder**を選択すると、新しいエディタタブで**Agent (Prompt) Builder**が開きます。
1. **+ New Agent**ボタンをクリックします。拡張機能が**Command Palette**を通じてセットアップウィザードを起動します。
1. 名前に**Calculator Agent**と入力し、**Enter**を押します。
1. **Agent (Prompt) Builder**で、**Model**フィールドに**OpenAI GPT-4o (via GitHub)**モデルを選択します。

### -2- エージェントのシステムプロンプトを作成する

エージェントの骨組みができたら、その性格と目的を定義します。このセクションでは、**Generate system prompt**機能を使って、電卓エージェントとしてのエージェントの意図した動作を記述し、モデルにシステムプロンプトを作成させます。

1. **Prompts**セクションで、**Generate system prompt**ボタンをクリックします。このボタンをクリックすると、エージェントのシステムプロンプトを生成するプロンプトビルダーが開きます。
1. **Generate a prompt**ウィンドウで、次の内容を入力します：  
   `You are a helpful and efficient math assistant. When given a problem involving basic arithmetic, you respond with the correct result.`
1. **Generate**ボタンをクリックします。右下に通知が表示され、システムプロンプトが生成中であることが確認できます。生成が完了すると、**Agent (Prompt) Builder**の**System prompt**フィールドにプロンプトが表示されます。
1. **System prompt**を確認し、必要に応じて修正します。

### -3- MCPサーバーを作成する

エージェントのシステムプロンプトを定義したら、その動作と応答を導く準備が整います。次に、加算、減算、乗算、除算を実行するツールを備えた電卓MCPサーバーを作成します。このサーバーにより、エージェントは自然言語プロンプトに応じてリアルタイムで計算を実行できるようになります。

AI Toolkitには、独自のMCPサーバーを簡単に作成するためのテンプレートが用意されています。ここでは、電卓MCPサーバーを作成するためにPythonテンプレートを使用します。

*注*: AI Toolkitは現在、PythonとTypeScriptをサポートしています。

1. **Agent (Prompt) Builder**の**Tools**セクションで、**+ MCP Server**ボタンをクリックします。拡張機能が**Command Palette**を通じてセットアップウィザードを起動します。
1. **+ Add Server**を選択します。
1. **Create a New MCP Server**を選択します。
1. **python-weather**をテンプレートとして選択します。
1. **Default folder**を選択してMCPサーバーテンプレートを保存します。
1. サーバーの名前に次を入力します：**Calculator**
1. 新しいVisual Studio Codeウィンドウが開きます。**Yes, I trust the authors**を選択します。
1. **Terminal**（**Terminal** > **New Terminal**）を使用して仮想環境を作成します：`python -m venv .venv`
1. **Terminal**を使用して仮想環境を有効化します：
    - Windows - `.venv\Scripts\activate`
    - macOS/Linux - `source venv/bin/activate`
1. **Terminal**を使用して依存関係をインストールします：`pip install -e .[dev]`
1. **Activity Bar**の**Explorer**ビューで**src**ディレクトリを展開し、**server.py**を選択してエディタでファイルを開きます。
1. **server.py**ファイルのコードを次の内容に置き換え、保存します：

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

### -4- 電卓MCPサーバーでエージェントを実行する

エージェントにツールが追加されたので、いよいよそれを使う時です！このセクションでは、エージェントにプロンプトを送信し、電卓MCPサーバーの適切なツールを活用できるかどうかをテスト・検証します。

1. `F5`キーを押してMCPサーバーのデバッグを開始します。**Agent (Prompt) Builder**が新しいエディタタブで開きます。サーバーのステータスはターミナルで確認できます。
1. **Agent (Prompt) Builder**の**User prompt**フィールドに次のプロンプトを入力します：  
   `I bought 3 items priced at $25 each, and then used a $20 discount. How much did I pay?`
1. **Run**ボタンをクリックしてエージェントの応答を生成します。
1. エージェントの出力を確認します。モデルは**$55**と結論付けるはずです。
1. 次のような処理が行われます：
    - エージェントが計算を補助するために**multiply**と**subtract**ツールを選択します。
    - **multiply**ツールに対してそれぞれの`a`と`b`の値が割り当てられます。
    - **subtract**ツールに対してそれぞれの`a`と`b`の値が割り当てられます。
    - 各ツールからの応答が**Tool Response**に表示されます。
    - モデルからの最終出力が**Model Response**に表示されます。
1. 追加のプロンプトを送信してエージェントをさらにテストします。**User prompt**フィールド内の既存のプロンプトをクリックして置き換えることで、プロンプトを変更できます。
1. テストが完了したら、**terminal**で**CTRL/CMD+C**を入力してサーバーを停止します。

## 課題

**server.py**ファイルに新しいツールエントリ（例：数値の平方根を返す）を追加してみてください。エージェントが新しいツール（または既存のツール）を活用する必要があるプロンプトを送信してください。新しいツールを読み込むには、サーバーを再起動する必要があります。

## 解答

[解答](./solution/README.md)

## 重要なポイント

この章の重要なポイントは次の通りです：

- AI Toolkit拡張機能は、MCPサーバーとそのツールを利用するための優れたクライアントです。
- MCPサーバーに新しいツールを追加することで、進化する要件に対応するためにエージェントの能力を拡張できます。
- AI Toolkitには、カスタムツールの作成を簡単にするテンプレート（例：Python MCPサーバーテンプレート）が含まれています。

## 追加リソース

- [AI Toolkitドキュメント](https://aka.ms/AIToolkit/doc)

## 次のステップ
- 次へ: [テストとデバッグ](../08-testing/README.md)

**免責事項**:  
この文書は、AI翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されています。正確性を追求しておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があることをご承知ください。元の言語で記載された文書が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。この翻訳の使用に起因する誤解や誤解釈について、当社は責任を負いません。