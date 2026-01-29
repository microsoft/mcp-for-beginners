# AGENTS.md

## プロジェクト概要

**MCP for Beginners**は、Model Context Protocol (MCP) を学ぶためのオープンソース教育カリキュラムです。MCPは、AIモデルとクライアントアプリケーション間のインタラクションを標準化するフレームワークです。このリポジトリでは、複数のプログラミング言語を使用した実践的なコード例を含む包括的な学習資料を提供しています。

### 主な技術

- **プログラミング言語**: C#, Java, JavaScript, TypeScript, Python, Rust
- **フレームワーク & SDK**: 
  - MCP SDK (`@modelcontextprotocol/sdk`)
  - Spring Boot (Java)
  - FastMCP (Python)
  - LangChain4j (Java)
- **データベース**: PostgreSQL（pgvector拡張付き）
- **クラウドプラットフォーム**: Azure（Container Apps、OpenAI、Content Safety、Application Insights）
- **ビルドツール**: npm、Maven、pip、Cargo
- **ドキュメント**: Markdown（48以上の言語への自動翻訳対応）

### アーキテクチャ

- **11のコアモジュール (00-11)**: 基礎から応用までの順序立てた学習パス
- **実践ラボ**: 複数言語での完全なソリューションコードを含む実践的な演習
- **サンプルプロジェクト**: MCPサーバーとクライアントの実装例
- **翻訳システム**: 多言語対応の自動化されたGitHub Actionsワークフロー
- **画像アセット**: 翻訳版を含む集中管理された画像ディレクトリ

## セットアップコマンド

このリポジトリは主にドキュメントに焦点を当てています。ほとんどのセットアップは個々のサンプルプロジェクトやラボ内で行われます。

### リポジトリセットアップ

```bash
# Clone the repository
git clone https://github.com/microsoft/mcp-for-beginners.git
cd mcp-for-beginners
```

### サンプルプロジェクトの操作

サンプルプロジェクトは以下にあります:
- `03-GettingStarted/samples/` - 言語別の例
- `03-GettingStarted/01-first-server/solution/` - 初めてのサーバー実装
- `03-GettingStarted/02-client/solution/` - クライアント実装
- `11-MCPServerHandsOnLabs/` - 包括的なデータベース統合ラボ

各サンプルプロジェクトには独自のセットアップ手順があります:

#### TypeScript/JavaScript プロジェクト
```bash
cd <project-directory>
npm install
npm start
```

#### Python プロジェクト
```bash
cd <project-directory>
pip install -r requirements.txt
# or
pip install -e .
python main.py
```

#### Java プロジェクト
```bash
cd <project-directory>
mvn clean install
mvn spring-boot:run
```

## 開発ワークフロー

### ドキュメント構造

- **モジュール 00-11**: 順序立てたコアカリキュラムコンテンツ
- **translations/**: 言語別バージョン（自動生成、直接編集禁止）
- **translated_images/**: ローカライズされた画像バージョン（自動生成）
- **images/**: ソース画像と図

### ドキュメント変更の手順

1. ルートモジュールディレクトリ (00-11) の英語のMarkdownファイルのみ編集
2. 必要に応じて `images/` ディレクトリ内の画像を更新
3. co-op-translator GitHub Actionが自動的に翻訳を生成
4. 翻訳はメインブランチへのプッシュ時に再生成

### 翻訳の操作

- **自動翻訳**: GitHub Actionsワークフローがすべての翻訳を処理
- **手動編集禁止**: `translations/` ディレクトリ内のファイルは編集しない
- 翻訳メタデータは各翻訳ファイルに埋め込まれている
- 対応言語: アラビア語、中国語、フランス語、ドイツ語、ヒンディー語、日本語、韓国語、ポルトガル語、ロシア語、スペイン語など48以上

## テスト手順

### ドキュメント検証

このリポジトリは主にドキュメントに焦点を当てているため、テストは以下に重点を置きます:

1. **リンク検証**: すべての内部リンクが機能することを確認
```bash
# Check for broken markdown links
find . -name "*.md" -type f | xargs grep -n "\[.*\](../../.*)"
```

2. **コードサンプル検証**: コード例がコンパイル/実行可能であることを確認
```bash
# Navigate to specific sample and run its tests
cd 03-GettingStarted/samples/typescript
npm install && npm test
```

3. **Markdownリント**: フォーマットの一貫性を確認
```bash
# Use markdownlint if needed
npx markdownlint-cli2 "**/*.md" "#node_modules"
```

### サンプルプロジェクトのテスト

各言語別サンプルには独自のテスト手順があります:

#### TypeScript/JavaScript
```bash
npm test
npm run build
```

#### Python
```bash
pytest
python -m pytest tests/
```

#### Java
```bash
mvn test
mvn verify
```

## コードスタイルガイドライン

### ドキュメントスタイル

- 明確で初心者に優しい言語を使用
- 必要に応じて複数言語でコード例を含める
- Markdownのベストプラクティスに従う:
  - ATXスタイルのヘッダー (`#` 記法) を使用
  - 言語識別子付きのフェンスコードブロックを使用
  - 画像には説明的なaltテキストを含める
  - 行の長さは適度に保つ（厳密な制限はないが、常識的に）

### コードサンプルスタイル

#### TypeScript/JavaScript
- ESモジュール (`import`/`export`) を使用
- TypeScriptの厳密モード規約に従う
- 型注釈を含める
- ES2022をターゲット

#### Python
- PEP 8スタイルガイドラインに従う
- 適切な場所で型ヒントを使用
- 関数やクラスにdocstringを含める
- 最新のPython機能 (3.8+) を使用

#### Java
- Spring Bootの規約に従う
- Java 21の機能を使用
- 標準的なMavenプロジェクト構造に従う
- Javadocコメントを含める

### ファイル構成

```
<module-number>-<ModuleName>/
├── README.md              # Main module content
├── samples/               # Code examples (if applicable)
│   ├── typescript/
│   ├── python/
│   ├── java/
│   └── ...
└── solution/              # Complete working solutions
    └── <language>/
```

## ビルドとデプロイ

### ドキュメントデプロイ

リポジトリはGitHub Pagesなどを使用してドキュメントをホスティングします（該当する場合）。メインブランチへの変更が以下をトリガーします:

1. 翻訳ワークフロー (`.github/workflows/co-op-translator.yml`)
2. すべての英語Markdownファイルの自動翻訳
3. 必要に応じた画像のローカライズ

### ビルドプロセス不要

このリポジトリは主にMarkdownドキュメントを含むため、コアカリキュラムコンテンツにはコンパイルやビルドステップは必要ありません。

### サンプルプロジェクトのデプロイ

個々のサンプルプロジェクトにはデプロイ手順が含まれる場合があります:
- MCPサーバーのデプロイガイダンスは `03-GettingStarted/09-deployment/` を参照
- Azure Container Appsのデプロイ例は `11-MCPServerHandsOnLabs/` に記載

## 貢献ガイドライン

### プルリクエストプロセス

1. **フォークとクローン**: リポジトリをフォークし、ローカルにクローン
2. **ブランチ作成**: 説明的なブランチ名を使用（例: `fix/typo-module-3`, `add/python-example`）
3. **変更を加える**: 英語のMarkdownファイルのみ編集（翻訳は編集しない）
4. **ローカルでテスト**: Markdownが正しくレンダリングされることを確認
5. **PRを提出**: 明確なPRタイトルと説明を使用
6. **CLA**: Microsoft Contributor License Agreementを求められたら署名

### PRタイトル形式

明確で説明的なタイトルを使用:
- `[Module XX] 簡単な説明` モジュール固有の変更の場合
- `[Samples] 説明` サンプルコードの変更の場合
- `[Docs] 説明` 一般的なドキュメント更新の場合

### 貢献内容

- ドキュメントやコードサンプルのバグ修正
- 追加言語での新しいコード例
- 既存コンテンツの明確化と改善
- 新しいケーススタディや実践例
- 不明確または誤った内容に関する問題報告

### 禁止事項

- `translations/` ディレクトリ内のファイルを直接編集しない
- `translated_images/` ディレクトリを編集しない
- 大きなバイナリファイルを事前相談なしに追加しない
- 翻訳ワークフローファイルを調整なしに変更しない

## 追加の注意事項

### リポジトリのメンテナンス

- **変更履歴**: すべての重要な変更は `changelog.md` に記載
- **学習ガイド**: カリキュラムのナビゲーション概要は `study_guide.md` を使用
- **問題テンプレート**: バグ報告や機能リクエストにはGitHubの問題テンプレートを使用
- **行動規範**: すべての貢献者はMicrosoftオープンソース行動規範に従う必要があります

### 学習パス

最適な学習のためにモジュールを順序立てて進めてください (00-11):
1. **00-02**: 基礎（イントロダクション、コアコンセプト、セキュリティ）
2. **03**: 実践的な実装の開始
3. **04-05**: 実践的な実装と応用トピック
4. **06-10**: コミュニティ、ベストプラクティス、実世界の応用
5. **11**: 包括的なデータベース統合ラボ（13の順序立てたラボ）

### サポートリソース

- **ドキュメント**: https://modelcontextprotocol.io/
- **仕様**: https://spec.modelcontextprotocol.io/
- **コミュニティ**: https://github.com/orgs/modelcontextprotocol/discussions
- **Discord**: Microsoft Azure AI Foundry Discordサーバー
- **関連コース**: 他のMicrosoft学習パスについてはREADME.mdを参照

### よくあるトラブルシューティング

**Q: PRが翻訳チェックに失敗しています**
A: ルートモジュールディレクトリ内の英語Markdownファイルのみ編集し、翻訳版は編集しないようにしてください。

**Q: 新しい言語を追加するにはどうすればいいですか？**
A: 言語サポートはco-op-translatorワークフローで管理されています。新しい言語を追加するには問題を開いて議論してください。

**Q: コードサンプルが動作しません**
A: 特定のサンプルのREADMEに記載されたセットアップ手順に従ってください。依存関係の正しいバージョンがインストールされていることを確認してください。

**Q: 画像が表示されません**
A: 画像パスが相対的であることを確認し、スラッシュを使用してください。画像は `images/` ディレクトリまたはローカライズ版の場合は `translated_images/` にある必要があります。

### パフォーマンスに関する考慮事項

- 翻訳ワークフローは完了まで数分かかる場合があります
- 大きな画像はコミット前に最適化してください
- 個々のMarkdownファイルは焦点を絞り、適度なサイズに保つ
- 移植性を高めるために相対リンクを使用

### プロジェクトガバナンス

このプロジェクトはMicrosoftのオープンソースプラクティスに従います:
- コードとドキュメントにはMITライセンスを適用
- Microsoftオープンソース行動規範
- 貢献にはCLAが必要
- セキュリティ問題: SECURITY.mdガイドラインに従う
- サポート: SUPPORT.mdを参照

---

**免責事項**:  
この文書は、AI翻訳サービス[Co-op Translator](https://github.com/Azure/co-op-translator)を使用して翻訳されています。正確性を追求しておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があることをご承知ください。元の言語で記載された文書が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。この翻訳の使用に起因する誤解や誤解釈について、当方は責任を負いません。