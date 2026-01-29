# 🚀 モジュール 1: AI Toolkit 基礎

[![Duration](https://img.shields.io/badge/Duration-15%20minutes-blue.svg)]()
[![Difficulty](https://img.shields.io/badge/Difficulty-Beginner-green.svg)]()
[![Prerequisites](https://img.shields.io/badge/Prerequisites-VS%20Code-orange.svg)]()

## 📋 学習目標

このモジュールの終了時には、以下ができるようになります：
- ✅ Visual Studio Code 用 AI Toolkit のインストールと設定
- ✅ モデルカタログの操作とさまざまなモデルソースの理解
- ✅ Playground を使ったモデルのテストと実験
- ✅ Agent Builder を使ったカスタム AI エージェントの作成
- ✅ 複数のプロバイダー間でのモデル性能比較
- ✅ プロンプトエンジニアリングのベストプラクティスの適用

## 🧠 AI Toolkit (AITK) の紹介

**Visual Studio Code 用 AI Toolkit** は、Microsoft の代表的な拡張機能で、VS Code を包括的な AI 開発環境に変えます。AI 研究と実践的なアプリケーション開発の橋渡しをし、あらゆるスキルレベルの開発者が生成系 AI を活用できるようにします。

### 🌟 主な機能

| 機能 | 説明 | 利用シーン |
|---------|-------------|----------|
| **🗂️ モデルカタログ** | GitHub、ONNX、OpenAI、Anthropic、Google から100以上のモデルにアクセス | モデルの発見と選択 |
| **🔌 BYOM サポート** | 自分のモデル（ローカル/リモート）を統合 | カスタムモデルの展開 |
| **🎮 インタラクティブ Playground** | チャットインターフェースでリアルタイムにモデルをテスト | 迅速なプロトタイピングとテスト |
| **📎 マルチモーダル対応** | テキスト、画像、添付ファイルを扱う | 複雑な AI アプリケーション |
| **⚡ バッチ処理** | 複数のプロンプトを同時に実行 | 効率的なテストワークフロー |
| **📊 モデル評価** | 組み込みの指標（F1、関連性、類似度、一貫性） | パフォーマンス評価 |

### 🎯 AI Toolkit が重要な理由

- **🚀 開発の加速**：アイデアからプロトタイプまで数分で
- **🔄 統一されたワークフロー**：複数の AI プロバイダーを一つのインターフェースで
- **🧪 簡単な実験**：複雑な設定なしでモデルを比較
- **📈 本番対応**：プロトタイプから本番展開へのスムーズな移行

## 🛠️ 前提条件とセットアップ

### 📦 AI Toolkit 拡張機能のインストール

**ステップ 1: 拡張機能マーケットプレイスにアクセス**
1. Visual Studio Code を開く
2. 拡張機能ビューに移動（`Ctrl+Shift+X` または `Cmd+Shift+X`）
3. 「AI Toolkit」を検索

**ステップ 2: バージョンを選択**
- **🟢 リリース**：本番利用に推奨
- **🔶 プレリリース**：最新機能の先行体験

**ステップ 3: インストールして有効化**

![AI Toolkit Extension](../../../../translated_images/ja/aitkext.d28945a03eed003c39fc39bc96ae655af9b64b9b922e78e88b07214420ed7985.png)

### ✅ 確認チェックリスト
- [ ] VS Code のサイドバーに AI Toolkit アイコンが表示されている
- [ ] 拡張機能が有効かつアクティブになっている
- [ ] 出力パネルにインストールエラーがない

## 🧪 ハンズオン演習 1: GitHub モデルの探索

**🎯 目的**：モデルカタログをマスターし、最初の AI モデルをテストする

### 📊 ステップ 1: モデルカタログを操作する

モデルカタログは AI エコシステムへの入り口です。複数のプロバイダーからモデルを集約し、簡単に発見・比較できます。

**🔍 ナビゲーションガイド：**

AI Toolkit のサイドバーで **MODELS - Catalog** をクリック

![Model Catalog](../../../../translated_images/ja/aimodel.263ed2be013d8fb0e2265c4f742cfe490f6f00eca5e132ec50438c8e826e34ed.png)

**💡 プロのコツ**：コード生成、クリエイティブライティング、分析など、用途に合った特定の機能を持つモデルを探しましょう。

**⚠️ 注意**：GitHub ホストのモデル（GitHub Models）は無料で使えますが、リクエストやトークンに制限があります。GitHub 以外のモデル（Azure AI や他のエンドポイント経由の外部モデル）を使う場合は、適切な API キーや認証情報が必要です。

### 🚀 ステップ 2: 最初のモデルを追加して設定する

**モデル選択のポイント：**
- **GPT-4.1**：複雑な推論や分析に最適
- **Phi-4-mini**：軽量でシンプルなタスクに高速応答

**🔧 設定手順：**
1. カタログから **OpenAI GPT-4.1** を選択
2. **Add to My Models** をクリックしてモデルを登録
3. **Try in Playground** を選んでテスト環境を起動
4. モデルの初期化を待つ（初回は少し時間がかかる場合あり）

![Playground Setup](../../../../translated_images/ja/playground.dd6f5141344878ca4d4f3de819775da7b113518941accf37c291117c602f85db.png)

**⚙️ モデルパラメーターの理解：**
- **Temperature**：創造性の度合いを制御（0 = 決定的、1 = 創造的）
- **Max Tokens**：応答の最大長
- **Top-p**：応答の多様性を調整する核サンプリング

### 🎯 ステップ 3: Playground インターフェースを使いこなす

Playground は AI 実験のラボです。最大限に活用する方法はこちら：

**🎨 プロンプトエンジニアリングのベストプラクティス：**
1. **具体的に**：明確で詳細な指示が良い結果を生む
2. **コンテキストを提供**：関連する背景情報を含める
3. **例を使う**：モデルに望む内容を例示する
4. **繰り返し改善**：初期結果をもとにプロンプトを調整

**🧪 テストシナリオ：**
```markdown
# Example 1: Code Generation
"Write a Python function that calculates the factorial of a number using recursion. Include error handling and docstrings."

# Example 2: Creative Writing
"Write a professional email to a client explaining a project delay, maintaining a positive tone while being transparent about challenges."

# Example 3: Data Analysis
"Analyze this sales data and provide insights: [paste your data]. Focus on trends, anomalies, and actionable recommendations."
```

![Testing Results](../../../../translated_images/ja/result.1dfcf211fb359cf65902b09db191d3bfc65713ca15e279c1a30be213bb526949.png)

### 🏆 チャレンジ演習：モデル性能比較

**🎯 目標**：同じプロンプトで複数モデルを比較し、それぞれの強みを理解する

**📋 手順：**
1. **Phi-4-mini** をワークスペースに追加
2. GPT-4.1 と Phi-4-mini に同じプロンプトを使う

![set](../../../../translated_images/ja/set.88132df189ecde2cbbda256c1841db5aac8e9bdeba1a4e343dfa031b9545d6c9.png)

3. 応答の質、速度、正確さを比較
4. 結果をドキュメントにまとめる

![Model Comparison](../../../../translated_images/ja/compare.97746cd0f907495503c1fc217739f3890dc76ea5f6fd92379a6db0cc331feb58.png)

**💡 発見すべきポイント：**
- LLM と SLM の使い分け
- コストと性能のバランス
- モデルごとの専門的な機能

## 🤖 ハンズオン演習 2: Agent Builder でカスタムエージェントを作成

**🎯 目的**：特定のタスクやワークフローに特化した AI エージェントを作成する

### 🏗️ ステップ 1: Agent Builder の理解

Agent Builder は AI Toolkit の真骨頂です。大規模言語モデルの力を活かしつつ、カスタム指示や特定パラメーター、専門知識を組み合わせた専用 AI アシスタントを作れます。

**🧠 エージェントの構成要素：**
- **コアモデル**：基盤となる LLM（GPT-4、Groks、Phi など）
- **システムプロンプト**：エージェントの性格や振る舞いを定義
- **パラメーター**：最適なパフォーマンスのための微調整設定
- **ツール連携**：外部 API や MCP サービスとの接続
- **メモリ**：会話の文脈やセッションの持続

![Agent Builder Interface](../../../../translated_images/ja/agentbuilder.25895b2d2f8c02e7aa99dd40e105877a6f1db8f0441180087e39db67744b361f.png)

### ⚙️ ステップ 2: エージェント設定の詳細

**🎨 効果的なシステムプロンプトの作成：**
```markdown
# Template Structure:
## Role Definition
You are a [specific role] with expertise in [domain].

## Capabilities
- List specific abilities
- Define scope of knowledge
- Clarify limitations

## Behavior Guidelines
- Response style (formal, casual, technical)
- Output format preferences
- Error handling approach

## Examples
Provide 2-3 examples of ideal interactions
```

*もちろん、Generate System Prompt を使って AI にプロンプトの生成や最適化を手伝わせることもできます*

**🔧 パラメーター最適化：**
| パラメーター | 推奨範囲 | 利用シーン |
|-----------|------------------|----------|
| **Temperature** | 0.1-0.3 | 技術的・事実ベースの応答 |
| **Temperature** | 0.7-0.9 | 創造的・ブレインストーミング |
| **Max Tokens** | 500-1000 | 簡潔な応答 |
| **Max Tokens** | 2000-4000 | 詳細な説明 |

### 🐍 ステップ 3: 実践演習 - Python プログラミングエージェント

**🎯 ミッション**：Python コーディングに特化したアシスタントを作成

**📋 設定手順：**

1. **モデル選択**：**Claude 3.5 Sonnet** を選択（コードに優れる）

2. **システムプロンプト設計**：
```markdown
# Python Programming Expert Agent

## Role
You are a senior Python developer with 10+ years of experience. You excel at writing clean, efficient, and well-documented Python code.

## Capabilities
- Write production-ready Python code
- Debug complex issues
- Explain code concepts clearly
- Suggest best practices and optimizations
- Provide complete working examples

## Response Format
- Always include docstrings
- Add inline comments for complex logic
- Suggest testing approaches
- Mention relevant libraries when applicable

## Code Quality Standards
- Follow PEP 8 style guidelines
- Use type hints where appropriate
- Handle exceptions gracefully
- Write readable, maintainable code
```

3. **パラメーター設定**：
   - Temperature: 0.2（安定した信頼性の高いコード）
   - Max Tokens: 2000（詳細な説明）
   - Top-p: 0.9（バランスの取れた創造性）

![Python Agent Configuration](../../../../translated_images/ja/pythonagent.5e51b406401c165fcabfd66f2d943c27f46b5fed0f9fb73abefc9e91ca3489d4.png)

### 🧪 ステップ 4: Python エージェントのテスト

**テストシナリオ：**
1. **基本機能**：「素数を見つける関数を作成して」
2. **複雑なアルゴリズム**：「挿入、削除、検索メソッドを持つ二分探索木を実装して」
3. **実用的な問題**：「レート制限とリトライを扱うウェブスクレイパーを作って」
4. **デバッグ**：「このコードを修正して [バグのあるコードを貼り付け]」

**🏆 合格基準：**
- ✅ エラーなくコードが動作する
- ✅ 適切なドキュメントが含まれている
- ✅ Python のベストプラクティスに従っている
- ✅ 明確な説明がある
- ✅ 改善案を提案できる

## 🎓 モジュール 1 総括と次のステップ

### 📊 知識チェック

理解度を確認しましょう：
- [ ] カタログ内のモデルの違いを説明できるか？
- [ ] カスタムエージェントを作成し、テストできたか？
- [ ] 用途に応じたパラメーター最適化が理解できているか？
- [ ] 効果的なシステムプロンプトを設計できるか？

### 📚 追加リソース

- **AI Toolkit ドキュメント**：[公式 Microsoft Docs](https://github.com/microsoft/vscode-ai-toolkit)
- **プロンプトエンジニアリングガイド**：[ベストプラクティス](https://platform.openai.com/docs/guides/prompt-engineering)
- **AI Toolkit のモデル**：[開発中のモデル](https://github.com/microsoft/vscode-ai-toolkit/blob/main/doc/models.md)

**🎉 おめでとうございます！** AI Toolkit の基礎をマスターし、より高度な AI アプリケーションの構築準備が整いました！

### 🔜 次のモジュールへ進む

さらに高度な機能を学びたい方は、**[モジュール 2: MCP with AI Toolkit Fundamentals](../lab2/README.md)** へ進みましょう。ここでは以下を学びます：
- Model Context Protocol (MCP) を使ってエージェントを外部ツールに接続する方法
- Playwright を使ったブラウザ自動化エージェントの構築
- MCP サーバーと AI Toolkit エージェントの統合
- 外部データや機能でエージェントを強化する方法

**免責事項**：  
本書類はAI翻訳サービス「[Co-op Translator](https://github.com/Azure/co-op-translator)」を使用して翻訳されました。正確性の向上に努めておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があります。原文の言語による文書が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用により生じたいかなる誤解や誤訳についても、当方は責任を負いかねます。