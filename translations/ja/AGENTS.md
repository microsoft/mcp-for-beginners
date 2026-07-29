# AGENTS.md

## プロジェクト概要

**MCP for Beginners** は、Model Context Protocol (MCP) の学習のためのオープンソース教育カリキュラムです。MCP は AI モデルとクライアントアプリケーション間のやり取りのための標準化フレームワークです。このリポジトリは、複数のプログラミング言語での実践的なコード例を含む包括的な学習資料を提供します。

### 主要技術

- <strong>プログラミング言語</strong>: C#, Java, JavaScript, TypeScript, Python, Rust
- **フレームワーク & SDK**: 
  - MCP SDK (`@modelcontextprotocol/sdk`)
  - Spring Boot (Java)
  - FastMCP (Python)
  - LangChain4j (Java)
- <strong>データベース</strong>: pgvector 拡張機能付き PostgreSQL
- <strong>クラウドプラットフォーム</strong>: Azure (Container Apps, OpenAI, Content Safety, Application Insights)
- <strong>ビルドツール</strong>: npm, Maven, pip, Cargo
- <strong>ドキュメンテーション</strong>: マルチランゲージ自動翻訳対応の Markdown (48言語以上)

### アーキテクチャ

- **11 のコアモジュール (00-11)**: 基礎から応用までの順序に沿った学習パス
- <strong>ハンズオンラボ</strong>: 複数言語の完全な解答付き実践演習
- <strong>サンプルプロジェクト</strong>: 動作する MCP サーバーとクライアントの実装例
- <strong>翻訳システム</strong>: GitHub Actions による多言語対応の自動化ワークフロー
- <strong>画像資産</strong>: 翻訳済みバージョンを含む画像の集中管理ディレクトリ

## セットアップコマンド

本リポジトリはドキュメント主体です。ほとんどのセットアップは個々のサンプルプロジェクトやラボ内で行われます。

### リポジトリのセットアップ

```bash
# リポジトリをクローンする
git clone https://github.com/microsoft/mcp-for-beginners.git
cd mcp-for-beginners
```

### サンプルプロジェクトの利用

サンプルプロジェクトは以下にあります:
- `03-GettingStarted/samples/` - 言語別の例
- `03-GettingStarted/01-first-server/solution/` - 最初のサーバー実装
- `03-GettingStarted/02-client/solution/` - クライアント実装
- `11-MCPServerHandsOnLabs/` - データベース統合の包括的なラボ

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
# または
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

### MCP 7-28 対応準備

#### リポジトリ準備チェックリスト

- [x] <strong>新規参加者の理解を促進</strong>: 本ファイルはリポジトリの目的、
  構造、貢献ルール、サンプルセットアップパスを定義しています。
- [x] **正確なフラグ付きビルド/テスト/リンツコマンド**:
  - リポジトリドキュメントのリンツ:
    `npx --yes markdownlint-cli2 "**/*.md" "#node_modules" "#translations" "#translated_images"`
  - リポジトリドキュメントのリンクパターン監査:
    `find . -name "*.md" -not -path "*/node_modules/*" -not -path "./translations/*" -not -path "./translated_images/*" -print0 | xargs -0 grep -En "\[.*\]\(.*\)"`
  - TypeScript サンプルの検証:
    `cd 03-GettingStarted/samples/typescript && npm ci && npm test && npm run build`
  - Python サンプルの検証:
    `cd 10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp && python -m pip install -e . && pytest -q`
  - Java サンプルの検証:
    `cd 03-GettingStarted/samples/java/calculator && mvn -B -ntp test verify`

- [x] **MCPツールになり得る現実的なワークフローの一例**:
  `validate_curriculum_change`
- [x] **入力/出力が明示的**（以下の仕様参照）。
- [x] <strong>権限と失敗モードが文書化されている</strong>（以下の仕様参照）。
- [x] **CI テスト可能性が明示的**（決定論的コマンド、明示的な
  終了コード、機械可読な出力）。

#### 候補MCPツールワークフロー: `validate_curriculum_change`

##### 目的

カリキュラム文書変更および代表的なサンプルコードの
マージ前の健全性を検証します。

##### 入力

- `changed_paths: string[]`（必須）- PRで変更された相対パス。
- `run_docs_lint: boolean`（デフォルトは `true`）
- `run_links_audit: boolean`（デフォルトは `true`）
- `run_samples: { typescript?: boolean, python?: boolean, java?: boolean }`
  （デフォルトはすべて `false`）

##### 出力

- `status: "ok" | "failed"`
- `checks: Array<{ name: string, command: string, exit_code: number,
  summary: string }>`
- `artifacts: Array<{ type: "log" | "report", path: string }>`
- `failed_checks: string[]`

##### 権限

- ワークスペースのファイル読み取りおよびツール生成成果物（例：lint
  レポート、テストログ）への書き込みのみ。`translations/` や
  `translated_images/` への書き込みは禁止。
- ローカルシェルコマンドの実行。
- パッケージ復元のみに限ったネットワークアクセス（`npm ci`,
  `python -m pip install`、`mvn`の依存解決）。
- `translations/` や `translated_images/` へのプッシュ、マージ、
  変更の権限なし。

##### 失敗モード

- `E_NO_INPUT_PATHS`: `changed_paths` が空。
- `E_INVALID_PATH`: 入力パスがリポジトリルートを逸脱。
- `E_LINT_FAILED`: markdown lint の終了コードが0以外。
- `E_LINK_AUDIT_FAILED`: リンク監査コマンドの終了コードが0以外。
- `E_SAMPLE_TEST_FAILED`: サンプルテスト/ビルドの終了コードが0以外。
- `E_TIMEOUT`: コマンドが設定されたタイムアウト時間を超過。

##### 推奨されるCI契約

検証の自動化には、以下を行うCIジョブを設定してください:

- `*.md`、サンプルコード、またはこのファイルに関わるプルリクエストでトリガー。
- 上記の正確なコマンドを実行。
- ログを成果物として保存。
- いかなる非ゼロ終了コードでもジョブを失敗させる。

#### このリポジトリからMCPサーバーを出荷する場合

- [ ] MCP 7-28 のドラフトチェンジログを読む:
  <https://modelcontextprotocol.io/specification/draft/changelog>
- [ ] SDKベータに対してサーバーを実行する:
  <https://blog.modelcontextprotocol.io/posts/sdk-betas-2026-07-28/>
- [ ] セッションとハンドシェイクの仮定を除去し、各リクエストを
  完結型として扱う:
  <https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/#a-stateless-protocol>
- [ ] 生のHTTPリクエストには `Mcp-Method` と `Mcp-Name` ヘッダーを送信:
  <https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/#routable-cacheable-traceable>
- [ ] ハードコードエラーコードを監査（`missing resource` が `-32002` から `-32602` に移動）。

- [ ] 非推奨となった roots、sampling、および logging の移行をフラグおよび計画する：
 
  <https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/#roots-sampling-and-logging-are-deprecated>
- [ ] 実験的な `2025-11-25` Tasks API から移行する：
 
  <https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/#tasks-graduates-to-an-extension>
- [ ] OAuth および OpenID Connect の強化の認可を見直す：

### ドキュメント構成

- **Modules 00-11**：コアカリキュラムの内容を順に配置
- **translations/**：言語別バージョン（自動生成、直接編集禁止）
- **translated_images/**：ローカライズされた画像バージョン（自動生成）
- **images/**：元の画像と図

### ドキュメント変更の方法

1. ルートモジュールディレクトリ（00-11）の英語マークダウンファイルのみを編集する
2. 必要に応じて `images/` ディレクトリ内の画像を更新する
3. co-op-translator GitHub Action が自動的に翻訳を生成する
4. main ブランチにプッシュすると翻訳が再生成される

### 翻訳作業について

- <strong>自動翻訳</strong>：GitHub Actions ワークフローがすべての翻訳を処理する
- `translations/` ディレクトリ内のファイルを手動で編集しないこと
- 翻訳ファイルにはメタデータが埋め込まれている
- 対応言語：アラビア語、中国語、フランス語、ドイツ語、ヒンディー語、日本語、韓国語、ポルトガル語、ロシア語、スペイン語など48+言語

## テスト手順

### ドキュメントの検証

このリポジトリは主にドキュメントのため、テストは以下に焦点を当てる：

1. <strong>リンクパターン監査</strong>：チェック用マークダウンリンクの一覧化

   ```bash
   # マークダウンリンクをリストアップする（パターン監査）
   find . -name "*.md" -not -path "*/node_modules/*" -not -path "./translations/*" -not -path "./translated_images/*" -print0 | xargs -0 grep -En "\[.*\]\(.*\)"
   ```

2. <strong>コードサンプルの検証</strong>：コード例がコンパイル/実行可能かをテスト

   ```bash
   # 特定のサンプルに移動して、そのテストを実行する
   cd 03-GettingStarted/samples/typescript
   npm install && npm test
   ```

3. <strong>マークダウンの整合性チェック</strong>：フォーマットの一貫性を確認

   ```bash
   # 必要に応じてmarkdownlintを使用してください
   npx --yes markdownlint-cli2 "**/*.md" "#node_modules" "#translations" "#translated_images"
   ```

### サンプルプロジェクトのテスト

言語別サンプルにはそれぞれ独自のテスト方法がある：

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

- わかりやすく初心者にも優しい言葉を使う
- 適宜複数言語のコード例を含める
- マークダウンのベストプラクティスに従う：
  - ATXスタイルの見出し（`#` 記法）を使う
  - 言語指定のあるフェンスコードブロックを使う
  - 画像には説明的な alt テキストを付ける
  - 行長は適切に保つ（厳密な制限はなし、ただし妥当な範囲で）

### コードサンプルスタイル

#### TypeScript/JavaScript
- ESモジュール（`import`/`export`）を使う
- TypeScriptの厳格モード規約に従う
- 型注釈を含める
- ターゲットは ES2022

#### Python
- PEP 8 のスタイルガイドラインに従う
- 適宜型ヒントを使う
- 関数とクラスにはドックストリングを含める
- Python 3.8+ のモダンな機能を使う

#### Java
- Spring Bootの規約に従う
- Java 21の機能を使う
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

### ドキュメントのデプロイ


このリポジトリは、ドキュメントホスティングにGitHub Pagesまたは同様のサービスを使用しています（該当する場合）。mainブランチへの変更は次を引き起こします：

1. 翻訳ワークフロー（`.github/workflows/co-op-translator.yml`）
2. すべての英語のマークダウンファイルの自動翻訳
3. 必要に応じた画像のローカライズ

### ビルドプロセス不要

このリポジトリは主にマークダウン形式のドキュメントを含んでいます。コアカリキュラムの内容についてはコンパイルやビルドのステップは不要です。

### サンプルプロジェクトのデプロイ

個別のサンプルプロジェクトにはデプロイ手順がある場合があります：
- MCPサーバーデプロイの案内は `03-GettingStarted/09-deployment/` を参照
- Azure Container Appsのデプロイ例は `11-MCPServerHandsOnLabs/` にあります

## コントリビューションガイドライン

### プルリクエストの進め方

1. **フォーク＆クローン**：リポジトリをフォークし、自分のフォークをローカルにクローンする
2. <strong>ブランチ作成</strong>：説明的なブランチ名を使う（例：`fix/typo-module-3`、`add/python-example`）
3. <strong>変更を行う</strong>：英語のマークダウンファイルのみ編集（翻訳ファイルは編集しない）
4. <strong>ローカルでテスト</strong>：マークダウンが正しくレンダリングされることを確認
5. **PR送信**：わかりやすいタイトルと説明を付けてプルリクエストを送る
6. **CLA署名**：案内があればMicrosoft Contributor License Agreementに署名する

### プルリクエストタイトルの形式

わかりやすく説明的なタイトルを使う：
- モジュール固有の変更には `[Module XX] 簡単な説明`
- サンプルコードの変更には `[Samples] 説明`
- 一般的なドキュメント更新には `[Docs] 説明`

### 何をコントリビュートするか

- ドキュメントやコードサンプルのバグ修正
- 新しいコード例（追加言語など）
- 既存内容の明確化・改善
- 新しいケーススタディや実践例
- 不明瞭または誤った内容の問題報告

### やってはいけないこと

- `translations/` ディレクトリ内のファイルを直接編集しない
- `translated_images/` ディレクトリを編集しない
- 大きなバイナリファイルを勝手に追加しない
- 翻訳ワークフローファイルを調整なしで変更しない

## 追加の注意事項

### リポジトリのメンテナンス

- <strong>変更履歴</strong>: 重要な変更はすべて `changelog.md` に記録
- <strong>学習ガイド</strong>: カリキュラムのナビゲーション概要は `study_guide.md` を利用
- **Issueテンプレート**: バグ報告や機能要求にはGitHubのIssueテンプレートを使用
- <strong>行動規範</strong>: すべてのコントリビューターはMicrosoftオープンソース行動規範を遵守

### 学習パス

効率的に学ぶにはモジュールを順番に（00-11）進めるのが良い：
1. **00-02**: 基礎（イントロダクション、コアコンセプト、セキュリティ）
2. **03**: ハンズオンで始める入門
3. **04-05**: 実践的な実装と応用トピック
4. **06-10**: コミュニティ、ベストプラクティス、実世界での応用
5. **11**: 包括的なデータベース統合ラボ（13連続ラボ）

### サポートリソース

- <strong>ドキュメント</strong>: https://modelcontextprotocol.io/
- <strong>仕様書</strong>: https://spec.modelcontextprotocol.io/
- <strong>コミュニティ</strong>: https://github.com/orgs/modelcontextprotocol/discussions
- **Discord**: Microsoft Foundry Discordサーバー
- <strong>関連コース</strong>: 他のMicrosoft学習パスはREADME.mdを参照

### よくあるトラブルシューティング

**Q: 私のPRが翻訳チェックで失敗しました**
A: ルートのモジュールディレクトリにある英語のマークダウンファイルのみを編集し、翻訳ファイルを編集していないことを確認してください。

**Q: 新しい言語をどうやって追加しますか？**

A: 言語サポートはco-op-translatorワークフローを通じて管理されています。新しい言語の追加について議論したい場合は、Issueを開いてください。

**Q: コードサンプルが動作しません**

A: 特定のサンプルのREADMEにあるセットアップ手順に従っていることを確認してください。依存関係の正しいバージョンがインストールされているかも確認してください。

**Q: 画像が表示されません**
A: 画像のパスが相対パスで、スラッシュが正しく使われているかを確認してください。画像は `images/` ディレクトリか、ローカライズ版の場合は `translated_images/` に配置してください。

### パフォーマンスに関する考慮事項

- 翻訳ワークフローは完了までに数分かかる場合があります
- 大きな画像はコミット前に最適化してください
- 個々のマークダウンファイルは焦点を絞り、適切なサイズに保つべきです
- 相対リンクを使うことで移植性が向上します

### プロジェクトガバナンス

このプロジェクトはMicrosoftのオープンソース慣行に従っています：
- コードとドキュメントにはMITライセンス
- Microsoftオープンソース行動規範
- コントリビューションにはCLAが必要
- セキュリティ問題：SECURITY.mdのガイドラインに従うこと
- サポートについてはSUPPORT.mdを参照してください

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責事項**：
本書類は AI 翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されています。正確性を期していますが、自動翻訳には誤りや不正確な部分が含まれる可能性があることをご承知おきください。原文の原語版が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用により生じたいかなる誤解や解釈違いについても、当方は責任を負いかねます。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->