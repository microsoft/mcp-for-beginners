# 🚀 PostgreSQLを用いたMCPサーバー - 完全学習ガイド

## 🧠 MCPデータベース統合学習パスの概要

本総合学習ガイドでは、小売分析の実践的な実装を通じて、データベースと統合された本番対応の<strong>Model Context Protocol (MCP)サーバー</strong>の構築方法を学びます。**行レベルセキュリティ（RLS）**、<strong>セマンティック検索</strong>、**Azure AI統合**、<strong>マルチテナントデータアクセス</strong>など、エンタープライズ向けのパターンも習得できます。

バックエンド開発者、AIエンジニア、データアーキテクトを問わず、本ガイドは実際の例とハンズオン演習で構成され、以下のMCPサーバー https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail について順を追って説明します。

## 🔗 公式MCPリソース

- 📘 [MCPドキュメント](https://modelcontextprotocol.io/) – 詳細なチュートリアルとユーザーガイド
- 📜 [MCP仕様書 (2026-07-28)](https://modelcontextprotocol.io/specification/2026-07-28/) – プロトコルのアーキテクチャと技術参照
- 🧑‍💻 [MCP GitHubリポジトリ](https://github.com/modelcontextprotocol) – オープンソースSDK、ツール、コードサンプル
- 🌐 [MCPコミュニティ](https://github.com/orgs/modelcontextprotocol/discussions) – 議論に参加し、コミュニティに貢献
- 🔒 [OWASP MCPトップ10](https://microsoft.github.io/mcp-azure-security-guide/mcp/) – セキュリティのベストプラクティスとリスク軽減


## 🧭 MCPデータベース統合学習パス

### 📚 https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retailの完全学習構造

| ラボ | トピック | 説明 | リンク |
|--------|-------|-------------|------|
| **ラボ 1-3: 基礎** | | | |
| 00 | [MCPデータベース統合入門](./00-Introduction/README.md) | MCPのデータベース連携と小売分析ユースケースの概要 | [ここから開始](./00-Introduction/README.md) |
| 01 | [コアアーキテクチャ概念](./01-Architecture/README.md) | MCPサーバーアーキテクチャ、データベース層、セキュリティパターンの理解 | [学習](./01-Architecture/README.md) |
| 02 | [セキュリティとマルチテナンシー](./02-Security/README.md) | 行レベルセキュリティ、認証、マルチテナントデータアクセス | [学習](./02-Security/README.md) |
| 03 | [環境セットアップ](./03-Setup/README.md) | 開発環境、Docker、Azureリソースの設定 | [セットアップ](./03-Setup/README.md) |
| **ラボ 4-6: MCPサーバー構築** | | | |
| 04 | [データベース設計とスキーマ](./04-Database/README.md) | PostgreSQLセットアップ、小売スキーマ設計、サンプルデータ | [構築](./04-Database/README.md) |
| 05 | [MCPサーバー実装](./05-MCP-Server/README.md) | データベース連携を備えたFastMCPサーバーの構築 | [構築](./05-MCP-Server/README.md) |
| 06 | [ツール開発](./06-Tools/README.md) | データベースクエリツールとスキーマイントロスペクションの作成 | [構築](./06-Tools/README.md) |
| **ラボ 7-9: 高度機能** | | | |
| 07 | [セマンティック検索統合](./07-Semantic-Search/README.md) | Azure OpenAIとpgvectorを使ったベクトル埋め込み実装 | [上級](./07-Semantic-Search/README.md) |
| 08 | [テストとデバッグ](./08-Testing/README.md) | テスト戦略、デバッグツール、検証手法 | [テスト](./08-Testing/README.md) |
| 09 | [VS Code統合](./09-VS-Code/README.md) | VS CodeのMCP統合設定とAIチャットの使い方 | [統合](./09-VS-Code/README.md) |
| **ラボ 10-12: 本番環境とベストプラクティス** | | | |
| 10 | [デプロイ戦略](./10-Deployment/README.md) | Dockerデプロイ、Azure Container Apps、スケーリング考慮事項 | [デプロイ](./10-Deployment/README.md) |
| 11 | [モニタリングと可観測性](./11-Monitoring/README.md) | Application Insights、ログ記録、パフォーマンス監視 | [監視](./11-Monitoring/README.md) |
| 12 | [ベストプラクティスと最適化](./12-Best-Practices/README.md) | パフォーマンス最適化、セキュリティ強化、本番運用のヒント | [最適化](./12-Best-Practices/README.md) |

### 💻 作成するもの

この学習パスの終了時には、以下の機能を備えた完全な<strong>Zava Retail Analytics MCPサーバー</strong>を構築しています：

- **顧客注文、製品、在庫を含むマルチテーブル小売データベース**
- 店舗ベースのデータ分離のための<strong>行レベルセキュリティ</strong>
- Azure OpenAI埋め込みを用いた<strong>セマンティック製品検索</strong>
- 自然言語クエリ用の<strong>VS Code AIチャット統合</strong>
- DockerとAzureを使った<strong>本番対応のデプロイ</strong>
- Application Insightsを用いた<strong>包括的モニタリング</strong>

## 🎯 学習の前提条件

この学習パスを最大限に活用するために、以下が望まれます：

- <strong>プログラミング経験</strong>：Python（推奨）または類似言語の知識
- <strong>データベース知識</strong>：SQLおよびリレーショナルデータベースの基本理解
- **API概念**：REST APIおよびHTTPの基礎知識
- <strong>開発ツール</strong>：コマンドライン、Git、コードエディタの使用経験
- <strong>クラウド基礎</strong>：（任意）Azureや類似クラウドプラットフォームの基本知識
- **Dockerの知識**：（任意）コンテナ化の概念理解

### 必要なツール

- **Docker Desktop** - PostgreSQLとMCPサーバーを実行するため
- **Azure CLI** - クラウドリソースの展開用
- **VS Code** - 開発およびMCP統合用
- **Git** - バージョン管理用
- **Python 3.8+** - MCPサーバー開発用

## 📚 学習ガイド＆リソース

本学習パスには、効果的に進めるための充実したリソースが含まれています：

### 学習ガイド

各ラボには以下が含まれます：
- <strong>明確な学習目標</strong> - 何を達成するか
- <strong>ステップバイステップの手順</strong> - 詳細な実装ガイド
- <strong>コード例</strong> - 解説付きの動作サンプル
- <strong>演習</strong> - ハンズオンでの練習機会
- <strong>トラブルシューティングガイド</strong> - よくある問題と解決策
- <strong>追加リソース</strong> - さらなる読書と調査

### 前提条件チェック

各ラボ開始前に：
- <strong>必要な知識</strong> - 事前に知っておくべきこと
- <strong>セットアップ検証</strong> - 環境が正しく整っているか確認
- <strong>所要時間の目安</strong> - 完了までの予想時間
- <strong>学習成果</strong> - 修了後に得られる知識

### 推奨学習パス

ご自身の経験レベルに応じて選択してください：

#### 🟢 <strong>初心者パス</strong>（MCP初学者向け）
1. まず [MCP for Beginners](https://aka.ms/mcp-for-beginners) の0-10章を完了してください
2. ラボ00-03で基礎知識を強化しましょう
3. ラボ04-06でハンズオン構築を行います
4. 実践的な利用に向けてラボ07-09に挑戦してください

#### 🟡 <strong>中級者パス</strong>（ある程度MCP経験あり）
1. ラボ00-01でデータベース特有の概念を復習
2. ラボ02-06で実装に注力
3. ラボ07-12で高度な機能を深掘り

#### 🔴 <strong>上級者パス</strong>（MCP経験豊富）
1. 文脈把握のためにラボ00-03をざっと確認
2. ラボ04-09でデータベース統合に集中
3. ラボ10-12で本番環境のデプロイに専念

## 🛠️ 本学習パスの効果的活用法

### 順序立てた学習（推奨）

ラボを順番に進めて包括的に理解しましょう：

1. <strong>概要を読む</strong> - 学ぶ内容を把握
2. <strong>前提条件を確認</strong> - 必要な知識の有無を確認
3. <strong>手順に従う</strong> - 学びながら実装
4. <strong>演習を完了</strong> - 理解を深める
5. <strong>重要ポイントを振り返る</strong> - 学習成果を定着

### 特定分野の学習

必要なスキルに応じて：

- <strong>データベース統合</strong>：ラボ04-06に注力
- <strong>セキュリティ実装</strong>：ラボ02、08、12を重点的に
- **AI/セマンティック検索**：ラボ07を深く学習
- <strong>本番環境デプロイ</strong>：ラボ10-12を学習

### ハンズオン演習

各ラボには：
- <strong>動作するコード例</strong> - コピーして改変し試す
- <strong>実践シナリオ</strong> - 小売分析のリアルケース
- <strong>漸進的な難易度</strong> - シンプルから高度へ構築
- <strong>検証ステップ</strong> - 実装が機能するか確認

## 🌟 コミュニティとサポート

### ヘルプを得るには

- **Azure AI Discord**： [専門家サポートに参加](https://discord.com/invite/ByRwuEEgH4)
- **GitHubリポジトリと実装サンプル**： [デプロイサンプルとリソース](https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail/)
- **MCPコミュニティ**： [MCP全般のディスカッションに参加](https://github.com/orgs/modelcontextprotocol/discussions)

## 🚀 学習を始める準備はできましたか？

**[ラボ00: MCPデータベース統合入門](./00-Introduction/README.md)** から旅を始めましょう

---

*本総合的で実践的な学習体験を通じて、データベース統合対応の本番向けMCPサーバー構築を極めましょう。*

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責事項**：
本書類は AI 翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されています。正確性を期していますが、自動翻訳には誤りや不正確な部分が含まれる可能性があることをご承知おきください。原文の原語版が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用により生じたいかなる誤解や解釈違いについても、当方は責任を負いかねます。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
