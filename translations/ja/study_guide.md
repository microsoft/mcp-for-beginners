# 初心者向け Model Context Protocol (MCP) - 学習ガイド

この学習ガイドは、「初心者向け Model Context Protocol (MCP)」カリキュラムのリポジトリ構造と内容の概要を提供します。このガイドを活用してリポジトリを効率的にナビゲートし、利用可能なリソースを最大限に活用してください。

## リポジトリ概要

Model Context Protocol (MCP) は、AIモデルとクライアントアプリケーション間のやり取りを標準化するフレームワークです。もともとAnthropicによって作成されたMCPは、現在、公式GitHub組織を通じて広範なMCPコミュニティによって維持されています。このリポジトリは、C#、Java、JavaScript、Python、TypeScriptでの実践的なコード例を含む包括的なカリキュラムを提供し、AI開発者、システムアーキテクト、ソフトウェアエンジニア向けに設計されています。

## ビジュアルカリキュラムマップ

```mermaid
mindmap
  root((MCP for Beginners))
    00. Introduction
      ::icon(fa fa-book)
      (Protocol Overview)
      (Standardization Benefits)
      (Real-world Use Cases)
      (AI Integration Fundamentals)
    01. Core Concepts
      ::icon(fa fa-puzzle-piece)
      (Client-Server Architecture)
      (Protocol Components)
      (Messaging Patterns)
      (Transport Mechanisms)
    02. Security
      ::icon(fa fa-shield)
      (AI-Specific Threats)
      (Best Practices 2025)
      (Azure Content Safety)
      (Auth & Authorization)
      (Microsoft Prompt Shields)
    03. Getting Started
      ::icon(fa fa-rocket)
      (First Server Implementation)
      (Client Development)
      (LLM Client Integration)
      (VS Code Extensions)
      (SSE Server Setup)
      (HTTP Streaming)
      (AI Toolkit Integration)
      (Testing Frameworks)
      (Advanced Server Usage)
      (Simple Auth)
      (Deployment Strategies)
    04. Practical Implementation
      ::icon(fa fa-code)
      (Multi-Language SDKs)
      (Testing & Debugging)
      (Prompt Templates)
      (Sample Projects)
      (Production Patterns)
    05. Advanced Topics
      ::icon(fa fa-graduation-cap)
      (Context Engineering)
      (Foundry Agent Integration)
      (Multi-modal AI Workflows)
      (OAuth2 Authentication)
      (Real-time Search)
      (Streaming Protocols)
      (Root Contexts)
      (Routing Strategies)
      (Sampling Techniques)
      (Scaling Solutions)
      (Security Hardening)
      (Entra ID Integration)
      (Web Search MCP)
      
    06. Community
      ::icon(fa fa-users)
      (Code Contributions)
      (Documentation)
      (MCP Client Ecosystem)
      (MCP Server Registry)
      (Image Generation Tools)
      (GitHub Collaboration)
    07. Early Adoption
      ::icon(fa fa-lightbulb)
      (Production Deployments)
      (Microsoft MCP Servers)
      (Azure MCP Service)
      (Enterprise Case Studies)
      (Future Roadmap)
    08. Best Practices
      ::icon(fa fa-check)
      (Performance Optimization)
      (Fault Tolerance)
      (System Resilience)
      (Monitoring & Observability)
    09. Case Studies
      ::icon(fa fa-file-text)
      (Azure API Management)
      (AI Travel Agent)
      (Azure DevOps Integration)
      (Documentation MCP)
      (GitHub MCP Registry)
      (VS Code Integration)
      (Real-world Implementations)
    10. Hands-on Workshop
      ::icon(fa fa-laptop)
      (MCP Server Fundamentals)
      (Advanced Development)
      (AI Toolkit Integration)
      (Production Deployment)
      (4-Lab Structure)
    11. Database Integration Labs
      ::icon(fa fa-database)
      (PostgreSQL Integration)
      (Retail Analytics Use Case)
      (Row Level Security)
      (Semantic Search)
      (Production Deployment)
      (13-Lab Structure)
      (Hands-on Learning)
```


## リポジトリ構造

リポジトリは、MCPのさまざまな側面に焦点を当てた11の主要セクションに分かれています：

1. **イントロダクション (00-Introduction/)**
   - Model Context Protocol の概要
   - AIパイプラインにおける標準化の重要性
   - 実用的なユースケースと利点

2. **コアコンセプト (01-CoreConcepts/)**
   - クライアント-サーバーアーキテクチャ
   - プロトコルの主要コンポーネント
   - MCPにおけるメッセージングパターン

3. **セキュリティ (02-Security/)**
   - MCPベースのシステムにおけるセキュリティ脅威
   - 実装を保護するためのベストプラクティス
   - 認証と認可の戦略
   - **包括的なセキュリティドキュメント**:
     - MCPセキュリティベストプラクティス2025
     - Azureコンテンツセーフティ実装ガイド
     - MCPセキュリティコントロールと技術
     - MCPベストプラクティス簡易リファレンス
   - **主要なセキュリティトピック**:
     - プロンプトインジェクションとツールポイズニング攻撃
     - セッションハイジャックと混乱した代理問題
     - トークンパススルーの脆弱性
     - 過剰な権限とアクセス制御
     - AIコンポーネントのサプライチェーンセキュリティ
     - Microsoft Prompt Shields の統合

4. **はじめに (03-GettingStarted/)**
   - 環境設定と構成
   - 基本的なMCPサーバーとクライアントの作成
   - 既存アプリケーションとの統合
   - 以下のセクションを含む：
     - 初めてのサーバー実装
     - クライアント開発
     - LLMクライアント統合
     - VS Code統合
     - Server-Sent Events (SSE) サーバー
     - 高度なサーバー使用法
     - HTTPストリーミング
     - AIツールキット統合
     - テスト戦略
     - デプロイメントガイドライン

5. **実践的な実装 (04-PracticalImplementation/)**
   - 異なるプログラミング言語でのSDK使用
   - デバッグ、テスト、検証技術
   - 再利用可能なプロンプトテンプレートとワークフローの作成
   - 実装例を含むサンプルプロジェクト

6. **高度なトピック (05-AdvancedTopics/)**
   - コンテキストエンジニアリング技術
   - Foundryエージェント統合
   - マルチモーダルAIワークフロー
   - OAuth2認証デモ
   - リアルタイム検索機能
   - リアルタイムストリーミング
   - ルートコンテキストの実装
   - ルーティング戦略
   - サンプリング技術
   - スケーリングアプローチ
   - セキュリティ考慮事項
   - Entra IDセキュリティ統合
   - Web検索統合

7. **コミュニティ貢献 (06-CommunityContributions/)**
   - コードとドキュメントの貢献方法
   - GitHubを通じたコラボレーション
   - コミュニティ主導の改善とフィードバック
   - 各種MCPクライアントの使用方法 (Claude Desktop、Cline、VSCode)
   - 画像生成を含む人気のMCPサーバーとの作業

8. **初期採用からの教訓 (07-LessonsfromEarlyAdoption/)**
   - 実際の実装と成功事例
   - MCPベースのソリューションの構築と展開
   - トレンドと将来のロードマップ
   - **Microsoft MCPサーバーガイド**: 10の本番対応Microsoft MCPサーバーの包括的ガイド：
     - Microsoft Learn Docs MCPサーバー
     - Azure MCPサーバー (15以上の専門コネクタ)
     - GitHub MCPサーバー
     - Azure DevOps MCPサーバー
     - MarkItDown MCPサーバー
     - SQL Server MCPサーバー
     - Playwright MCPサーバー
     - Dev Box MCPサーバー
     - Azure AI Foundry MCPサーバー
     - Microsoft 365 Agents Toolkit MCPサーバー

9. **ベストプラクティス (08-BestPractices/)**
   - パフォーマンスチューニングと最適化
   - 耐障害性のあるMCPシステムの設計
   - テストと回復力の戦略

10. **ケーススタディ (09-CaseStudy/)**
    - **7つの包括的なケーススタディ**が、さまざまなシナリオでのMCPの多様性を示します：
    - **Azure AI旅行代理店**: Azure OpenAIとAI検索を使用したマルチエージェントオーケストレーション
    - **Azure DevOps統合**: YouTubeデータ更新を自動化するワークフロープロセス
    - **リアルタイムドキュメント取得**: ストリーミングHTTPを使用したPythonコンソールクライアント
    - **インタラクティブ学習計画ジェネレーター**: 会話型AIを使用したChainlitウェブアプリ
    - **エディター内ドキュメント**: GitHub Copilotワークフローを使用したVS Code統合
    - **Azure API管理**: MCPサーバー作成によるエンタープライズAPI統合
    - **GitHub MCPレジストリ**: エコシステム開発とエージェント統合プラットフォーム
    - エンタープライズ統合、開発者の生産性、エコシステム開発にまたがる実装例

11. **ハンズオンワークショップ (10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/)**
    - MCPとAIツールキットを組み合わせた包括的なハンズオンワークショップ
    - AIモデルと現実世界のツールを橋渡しするインテリジェントアプリケーションの構築
    - 基礎、カスタムサーバー開発、プロダクション展開戦略をカバーする実践的モジュール
    - **ラボ構成**:
      - ラボ1: MCPサーバーの基礎
      - ラボ2: 高度なMCPサーバー開発
      - ラボ3: AIツールキット統合
      - ラボ4: プロダクション展開とスケーリング
    - ステップバイステップの指示によるラボベースの学習アプローチ

12. **MCPサーバーデータベース統合ラボ (11-MCPServerHandsOnLabs/)**
    - **PostgreSQL統合を伴う本番対応MCPサーバー構築のための包括的な13ラボ学習パス**
    - **Zava Retailユースケースを使用した実際の小売分析の実装**
    - **エンタープライズグレードのパターン**: Row Level Security (RLS)、セマンティック検索、マルチテナントデータアクセス
    - **完全なラボ構成**:
      - **ラボ00-03: 基礎** - イントロダクション、アーキテクチャ、セキュリティ、環境設定
      - **ラボ04-06: MCPサーバーの構築** - データベース設計、MCPサーバー実装、ツール開発
      - **ラボ07-09: 高度な機能** - セマンティック検索、テスト＆デバッグ、VS Code統合
      - **ラボ10-12: プロダクション＆ベストプラクティス** - 展開、モニタリング、最適化
    - **対象技術**: FastMCPフレームワーク、PostgreSQL、Azure OpenAI、Azure Container Apps、Application Insights
    - **学習成果**: 本番対応MCPサーバー、データベース統合パターン、AI駆動分析、エンタープライズセキュリティ

## 追加リソース

リポジトリには以下のサポートリソースが含まれています：

- **画像フォルダー**: カリキュラム全体で使用される図やイラストを含む
- **翻訳**: ドキュメントの自動翻訳による多言語サポート
- **公式MCPリソース**:
  - [MCPドキュメント](https://modelcontextprotocol.io/)
  - [MCP仕様](https://spec.modelcontextprotocol.io/)
  - [MCP GitHubリポジトリ](https://github.com/modelcontextprotocol)

## このリポジトリの使い方

1. **順序学習**: 構造化された学習体験のために、章を順番に（00から11まで）進めてください。
2. **言語特化型学習**: 特定のプログラミング言語に興味がある場合は、好みの言語での実装を含むサンプルディレクトリを探索してください。
3. **実践的な実装**: 「はじめに」セクションから始めて、環境を設定し、最初のMCPサーバーとクライアントを作成してください。
4. **高度な探求**: 基本を習得したら、高度なトピックに進んで知識を広げてください。
5. **コミュニティ参加**: GitHubディスカッションやDiscordチャンネルを通じてMCPコミュニティに参加し、専門家や他の開発者とつながりましょう。

## MCPクライアントとツール

カリキュラムでは、さまざまなMCPクライアントとツールを取り上げています：

1. **公式クライアント**:
   - Visual Studio Code
   - MCP in Visual Studio Code
   - Claude Desktop
   - Claude in VSCode
   - Claude API

2. **コミュニティクライアント**:
   - Cline (ターミナルベース)
   - Cursor (コードエディター)
   - ChatMCP
   - Windsurf

3. **MCP管理ツール**:
   - MCP CLI
   - MCP Manager
   - MCP Linker
   - MCP Router

## 人気のMCPサーバー

リポジトリでは、さまざまなMCPサーバーを紹介しています：

1. **公式Microsoft MCPサーバー**:
   - Microsoft Learn Docs MCPサーバー
   - Azure MCPサーバー (15以上の専門コネクタ)
   - GitHub MCPサーバー
   - Azure DevOps MCPサーバー
   - MarkItDown MCPサーバー
   - SQL Server MCPサーバー
   - Playwright MCPサーバー
   - Dev Box MCPサーバー
   - Azure AI Foundry MCPサーバー
   - Microsoft 365 Agents Toolkit MCPサーバー

2. **公式リファレンスサーバー**:
   - Filesystem
   - Fetch
   - Memory
   - Sequential Thinking

3. **画像生成**:
   - Azure OpenAI DALL-E 3
   - Stable Diffusion WebUI
   - Replicate

4. **開発ツール**:
   - Git MCP
   - Terminal Control
   - Code Assistant

5. **専門サーバー**:
   - Salesforce
   - Microsoft Teams
   - Jira & Confluence

## 貢献

このリポジトリはコミュニティからの貢献を歓迎します。MCPエコシステムに効果的に貢献する方法については、コミュニティ貢献セクションをご覧ください。

----

*この学習ガイドは2025年10月6日に更新され、この日付時点でのリポジトリの概要を提供しています。この日付以降にリポジトリ内容が更新される可能性があります。*

---

**免責事項**:  
この文書は、AI翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されています。正確性を追求しておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があります。元の言語で記載された文書を正式な情報源としてお考えください。重要な情報については、専門の人間による翻訳を推奨します。この翻訳の使用に起因する誤解や誤解釈について、当方は一切の責任を負いません。