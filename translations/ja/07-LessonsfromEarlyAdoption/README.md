<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "261078280431a58292789702da620407",
  "translation_date": "2025-07-29T00:11:44+00:00",
  "source_file": "07-LessonsfromEarlyAdoption/README.md",
  "language_code": "ja"
}
-->
# 🌟 早期導入者から学ぶ

[![MCP早期導入者からの教訓](../../../translated_images/08.980bb2babbaadd8a97739effc9b31e5f1abd8f4c4a3fbc90fb9f931a866674d0.ja.png)](https://youtu.be/jds7dSmNptE)

_(上の画像をクリックして、このレッスンの動画をご覧ください)_

## 🎯 このモジュールで学べること

このモジュールでは、実際の組織や開発者がModel Context Protocol (MCP)を活用して課題を解決し、イノベーションを推進している方法を探ります。詳細なケーススタディや実践的なプロジェクトを通じて、MCPが言語モデル、ツール、企業データを安全かつスケーラブルに統合する方法を学びます。

### 📚 MCPの実践例を見る

これらの原則が実際のツールにどのように適用されているかを知りたいですか？[**開発者の生産性を変革する10のMicrosoft MCPサーバー**](microsoft-mcp-servers.md)をご覧ください。今日から使える実際のMicrosoft MCPサーバーを紹介しています。

## 概要

このレッスンでは、早期導入者がModel Context Protocol (MCP)を活用して現実の課題を解決し、業界全体でイノベーションを推進している方法を探ります。詳細なケーススタディや実践的なプロジェクトを通じて、MCPが標準化された、安全でスケーラブルなAI統合を可能にし、大規模言語モデル、ツール、企業データを統一されたフレームワークで接続する方法を学びます。MCPベースのソリューションを設計・構築する実践的な経験を得るとともに、実証済みの実装パターンから学び、MCPを本番環境に展開するためのベストプラクティスを発見します。また、最新のトレンド、将来の方向性、オープンソースリソースについても触れ、MCP技術とその進化するエコシステムの最前線に立つための知識を提供します。

## 学習目標

- 様々な業界でのMCP実装事例を分析する
- 完全なMCPベースのアプリケーションを設計・構築する
- MCP技術の最新トレンドと将来の方向性を探る
- 実際の開発シナリオでベストプラクティスを適用する

## 実際のMCP実装事例

### ケーススタディ1: 企業のカスタマーサポート自動化

ある多国籍企業が、カスタマーサポートシステム全体でAIのやり取りを標準化するMCPベースのソリューションを導入しました。これにより以下が可能になりました：

- 複数のLLMプロバイダーに対する統一インターフェースの作成
- 部門間で一貫したプロンプト管理の維持
- 強固なセキュリティとコンプライアンス管理の実装
- 特定のニーズに応じたAIモデルの簡単な切り替え

**技術的実装:**

```python
# Python MCP server implementation for customer support
import logging
import asyncio
from modelcontextprotocol import create_server, ServerConfig
from modelcontextprotocol.server import MCPServer
from modelcontextprotocol.transports import create_http_transport
from modelcontextprotocol.resources import ResourceDefinition
from modelcontextprotocol.prompts import PromptDefinition
from modelcontextprotocol.tool import ToolDefinition

# Configure logging
logging.basicConfig(level=logging.INFO)

async def main():
    # Create server configuration
    config = ServerConfig(
        name="Enterprise Customer Support Server",
        version="1.0.0",
        description="MCP server for handling customer support inquiries"
    )
    
    # Initialize MCP server
    server = create_server(config)
    
    # Register knowledge base resources
    server.resources.register(
        ResourceDefinition(
            name="customer_kb",
            description="Customer knowledge base documentation"
        ),
        lambda params: get_customer_documentation(params)
    )
    
    # Register prompt templates
    server.prompts.register(
        PromptDefinition(
            name="support_template",
            description="Templates for customer support responses"
        ),
        lambda params: get_support_templates(params)
    )
    
    # Register support tools
    server.tools.register(
        ToolDefinition(
            name="ticketing",
            description="Create and update support tickets"
        ),
        handle_ticketing_operations
    )
    
    # Start server with HTTP transport
    transport = create_http_transport(port=8080)
    await server.run(transport)

if __name__ == "__main__":
    asyncio.run(main())
```

**結果:** モデルコストを30%削減、応答の一貫性を45%向上、グローバルな運用でのコンプライアンスを強化。

### ケーススタディ2: 医療診断アシスタント

ある医療提供者が、複数の専門医療AIモデルを統合し、患者データの保護を確保するMCPインフラを開発しました：

- 一般医療モデルと専門医療モデル間のシームレスな切り替え
- 厳格なプライバシー管理と監査トレイル
- 既存の電子カルテ (EHR) システムとの統合
- 医療用語に特化したプロンプトエンジニアリングの一貫性

**技術的実装:**

```csharp
// C# MCP host application implementation in healthcare application
using Microsoft.Extensions.DependencyInjection;
using ModelContextProtocol.SDK.Client;
using ModelContextProtocol.SDK.Security;
using ModelContextProtocol.SDK.Resources;

public class DiagnosticAssistant
{
    private readonly MCPHostClient _mcpClient;
    private readonly PatientContext _patientContext;
    
    public DiagnosticAssistant(PatientContext patientContext)
    {
        _patientContext = patientContext;
        
        // Configure MCP client with healthcare-specific settings
        var clientOptions = new ClientOptions
        {
            Name = "Healthcare Diagnostic Assistant",
            Version = "1.0.0",
            Security = new SecurityOptions
            {
                Encryption = EncryptionLevel.Medical,
                AuditEnabled = true
            }
        };
        
        _mcpClient = new MCPHostClientBuilder()
            .WithOptions(clientOptions)
            .WithTransport(new HttpTransport("https://healthcare-mcp.example.org"))
            .WithAuthentication(new HIPAACompliantAuthProvider())
            .Build();
    }
    
    public async Task<DiagnosticSuggestion> GetDiagnosticAssistance(
        string symptoms, string patientHistory)
    {
        // Create request with appropriate resources and tool access
        var resourceRequest = new ResourceRequest
        {
            Name = "patient_records",
            Parameters = new Dictionary<string, object>
            {
                ["patientId"] = _patientContext.PatientId,
                ["requestingProvider"] = _patientContext.ProviderId
            }
        };
        
        // Request diagnostic assistance using appropriate prompt
        var response = await _mcpClient.SendPromptRequestAsync(
            promptName: "diagnostic_assistance",
            parameters: new Dictionary<string, object>
            {
                ["symptoms"] = symptoms,
                patientHistory = patientHistory,
                relevantGuidelines = _patientContext.GetRelevantGuidelines()
            });
            
        return DiagnosticSuggestion.FromMCPResponse(response);
    }
}
```

**結果:** 医師向けの診断提案を改善し、完全なHIPAA準拠を維持しながらシステム間のコンテキスト切り替えを大幅に削減。

### ケーススタディ3: 金融サービスのリスク分析

ある金融機関が、部門間でリスク分析プロセスを標準化するためにMCPを導入しました：

- 信用リスク、詐欺検出、投資リスクモデルの統一インターフェースを作成
- 厳格なアクセス制御とモデルバージョン管理を実施
- すべてのAI推奨事項の監査可能性を確保
- 多様なシステム間でデータフォーマットの一貫性を維持

**技術的実装:**

```java
// Java MCP server for financial risk assessment
import org.mcp.server.*;
import org.mcp.security.*;

public class FinancialRiskMCPServer {
    public static void main(String[] args) {
        // Create MCP server with financial compliance features
        MCPServer server = new MCPServerBuilder()
            .withModelProviders(
                new ModelProvider("risk-assessment-primary", new AzureOpenAIProvider()),
                new ModelProvider("risk-assessment-audit", new LocalLlamaProvider())
            )
            .withPromptTemplateDirectory("./compliance/templates")
            .withAccessControls(new SOCCompliantAccessControl())
            .withDataEncryption(EncryptionStandard.FINANCIAL_GRADE)
            .withVersionControl(true)
            .withAuditLogging(new DatabaseAuditLogger())
            .build();
            
        server.addRequestValidator(new FinancialDataValidator());
        server.addResponseFilter(new PII_RedactionFilter());
        
        server.start(9000);
        
        System.out.println("Financial Risk MCP Server running on port 9000");
    }
}
```

**結果:** 規制遵守を強化し、モデル展開サイクルを40%短縮、部門間でリスク評価の一貫性を向上。

### ケーススタディ4: Microsoft Playwright MCPサーバーによるブラウザ自動化

Microsoftは、Model Context Protocolを通じて安全で標準化されたブラウザ自動化を可能にする[Playwright MCPサーバー](https://github.com/microsoft/playwright-mcp)を開発しました。この本番対応サーバーは、AIエージェントやLLMがウェブブラウザと制御された形でやり取りできるようにし、自動ウェブテスト、データ抽出、エンドツーエンドのワークフローなどのユースケースを実現します。

> **🎯 本番対応ツール**
> 
> このケーススタディでは、今日使用可能な実際のMCPサーバーを紹介しています！Playwright MCPサーバーとその他9つの本番対応Microsoft MCPサーバーについては、[**Microsoft MCPサーバーガイド**](microsoft-mcp-servers.md#8--playwright-mcp-server)をご覧ください。

**主な特徴:**
- MCPツールとしてブラウザ自動化機能（ナビゲーション、フォーム入力、スクリーンショット取得など）を公開
- 不正な操作を防ぐための厳格なアクセス制御とサンドボックス化を実施
- すべてのブラウザ操作に対する詳細な監査ログを提供
- Azure OpenAIやその他のLLMプロバイダーとの統合をサポート
- GitHub CopilotのCoding Agentにウェブブラウジング機能を提供

**技術的実装:**

```typescript
// TypeScript: Registering Playwright browser automation tools in an MCP server
import { createServer, ToolDefinition } from 'modelcontextprotocol';
import { launch } from 'playwright';

const server = createServer({
  name: 'Playwright MCP Server',
  version: '1.0.0',
  description: 'MCP server for browser automation using Playwright'
});

// Register a tool for navigating to a URL and capturing a screenshot
server.tools.register(
  new ToolDefinition({
    name: 'navigate_and_screenshot',
    description: 'Navigate to a URL and capture a screenshot',
    parameters: {
      url: { type: 'string', description: 'The URL to visit' }
    }
  }),
  async ({ url }) => {
    const browser = await launch();
    const page = await browser.newPage();
    await page.goto(url);
    const screenshot = await page.screenshot();
    await browser.close();
    return { screenshot };
  }
);

// Start the MCP server
server.listen(8080);
```

**結果:**

- AIエージェントやLLM向けの安全なプログラム可能なブラウザ自動化を実現
- 手動テストの労力を削減し、ウェブアプリケーションのテスト範囲を向上
- 企業環境でのブラウザベースのツール統合の再利用可能で拡張可能なフレームワークを提供
- GitHub Copilotのウェブブラウジング機能を強化

**参考資料:**

- [Playwright MCPサーバーGitHubリポジトリ](https://github.com/microsoft/playwright-mcp)
- [Microsoft AIと自動化ソリューション](https://azure.microsoft.com/en-us/products/ai-services/)

### ケーススタディ5: Azure MCP – エンタープライズグレードのModel Context Protocol as a Service

Azure MCP Server ([https://aka.ms/azmcp](https://aka.ms/azmcp))は、Microsoftが提供するエンタープライズグレードのModel Context Protocolのマネージド実装であり、クラウドサービスとしてスケーラブルで安全かつコンプライアンス対応のMCPサーバー機能を提供します。Azure MCPは、Azure AI、データ、セキュリティサービスと統合されたMCPサーバーを迅速に展開、管理、統合することで、運用負担を軽減し、AI導入を加速します。

> **🎯 本番対応ツール**
> 
> これは今日使用可能な実際のMCPサーバーです！Azure AI Foundry MCPサーバーについては、[**Microsoft MCPサーバーガイド**](microsoft-mcp-servers.md)をご覧ください。

- スケーリング、監視、セキュリティが組み込まれた完全マネージドMCPサーバーホスティング
- Azure OpenAI、Azure AI Search、その他のAzureサービスとのネイティブ統合
- Microsoft Entra IDによるエンタープライズ認証と認可
- カスタムツール、プロンプトテンプレート、リソースコネクタのサポート
- 企業のセキュリティおよび規制要件への準拠

**技術的実装:**

```yaml
# Example: Azure MCP server deployment configuration (YAML)
apiVersion: mcp.microsoft.com/v1
kind: McpServer
metadata:
  name: enterprise-mcp-server
spec:
  modelProviders:
    - name: azure-openai
      type: AzureOpenAI
      endpoint: https://<your-openai-resource>.openai.azure.com/
      apiKeySecret: <your-azure-keyvault-secret>
  tools:
    - name: document_search
      type: AzureAISearch
      endpoint: https://<your-search-resource>.search.windows.net/
      apiKeySecret: <your-azure-keyvault-secret>
  authentication:
    type: EntraID
    tenantId: <your-tenant-id>
  monitoring:
    enabled: true
    logAnalyticsWorkspace: <your-log-analytics-id>
```

**結果:**  
- エンタープライズAIプロジェクトの価値実現までの時間を短縮し、準備が整ったコンプライアンス対応のMCPサーバープラットフォームを提供
- LLM、ツール、企業データソースの統合を簡素化
- MCPワークロードのセキュリティ、可観測性、運用効率を向上
- Azure SDKのベストプラクティスと最新の認証パターンを活用してコード品質を改善

**参考資料:**  
- [Azure MCPドキュメント](https://aka.ms/azmcp)
- [Azure MCPサーバーGitHubリポジトリ](https://github.com/Azure/azure-mcp)
- [Azure AIサービス](https://azure.microsoft.com/en-us/products/ai-services/)

### ケーススタディ6: NLWeb

MCP (Model Context Protocol)は、チャットボットやAIアシスタントがツールとやり取りするための新しいプロトコルです。すべてのNLWebインスタンスはMCPサーバーでもあり、自然言語でウェブサイトに質問をするための1つのコアメソッド「ask」をサポートしています。返される応答は、ウェブデータを記述するために広く使用されている語彙であるschema.orgを活用しています。簡単に言えば、MCPはNLWebがHttpに対するHTMLのようなものです。NLWebはプロトコル、Schema.org形式、サンプルコードを組み合わせて、サイトがこれらのエンドポイントを迅速に作成できるようにし、人間には会話型インターフェースを、機械には自然なエージェント間のやり取りを提供します。

NLWebには2つの主要なコンポーネントがあります。
- サイトと自然言語でインターフェースするための非常にシンプルなプロトコルと、返される回答にjsonとschema.orgを活用する形式。REST APIのドキュメントで詳細をご覧ください。
- (1)の簡単な実装で、アイテムのリスト（製品、レシピ、観光名所、レビューなど）として抽象化できるサイトに既存のマークアップを活用します。ユーザーインターフェースウィジェットのセットと組み合わせて、サイトは簡単にコンテンツに対する会話型インターフェースを提供できます。「チャットクエリのライフサイクル」のドキュメントでこれがどのように機能するかの詳細をご覧ください。

**参考資料:**  
- [Azure MCPドキュメント](https://aka.ms/azmcp)  
- [NLWeb](https://github.com/microsoft/NlWeb)

### ケーススタディ7: Azure AI Foundry MCPサーバー – エンタープライズAIエージェント統合

Azure AI Foundry MCPサーバーは、MCPを使用してエンタープライズ環境でAIエージェントとワークフローを編成および管理する方法を示しています。MCPをAzure AI Foundryと統合することで、組織はエージェントのやり取りを標準化し、Foundryのワークフロー管理を活用し、安全でスケーラブルな展開を実現できます。

> **🎯 本番対応ツール**
> 
> これは今日使用可能な実際のMCPサーバーです！Azure AI Foundry MCPサーバーについては、[**Microsoft MCPサーバーガイド**](microsoft-mcp-servers.md#9--azure-ai-foundry-mcp-server)をご覧ください。

**主な特徴:**
- モデルカタログや展開管理を含むAzureのAIエコシステムへの包括的アクセス
- RAGアプリケーション向けのAzure AI Searchによる知識インデックス化
- AIモデルの性能と品質保証の評価ツール
- Azure AI Foundry CatalogとLabsとの統合による最先端の研究モデル
- 本番シナリオ向けのエージェント管理と評価機能

**結果:**
- AIエージェントワークフローの迅速なプロトタイピングと堅牢な監視
- 高度なシナリオ向けのAzure AIサービスとのシームレスな統合
- エージェントパイプラインの構築、展開、監視のための統一インターフェース
- 企業向けのセキュリティ、コンプライアンス、運用効率を向上
- 複雑なエージェント駆動プロセスを管理しながらAI導入を加速

**参考資料:**
- [Azure AI Foundry MCPサーバーGitHubリポジトリ](https://github.com/azure-ai-foundry/mcp-foundry)
- [Azure AIエージェントとMCPの統合 (Microsoft Foundry Blog)](https://devblogs.microsoft.com/foundry/integrating-azure-ai-agents-mcp/)

### ケーススタディ8: Foundry MCP Playground – 実験とプロトタイピング

Foundry MCP Playgroundは、MCPサーバーとAzure AI Foundry統合を実験するための準備が整った環境を提供します。開発者は、Azure AI Foundry CatalogとLabsのリソースを使用して、AIモデルやエージェントワークフローを迅速にプロトタイプ、テスト、評価できます。このプレイグラウンドはセットアップを簡素化し、サンプルプロジェクトを提供し、共同開発をサポートすることで、最小限のオーバーヘッドでベストプラクティスや新しいシナリオを探求することを可能にします。アイデアの検証、実験の共有、学習の加速を目指すチームにとって特に有用であり、複雑なインフラを必要とせずにイノベーションとコミュニティ貢献を促進します。

**参考資料:**

- [Foundry MCP Playground GitHubリポジトリ](https://github.com/azure-ai-foundry/foundry-mcp-playground)

### ケーススタディ9: Microsoft Learn Docs MCPサーバー – AIによるドキュメントアクセス

Microsoft Learn Docs MCPサーバーは、Model Context Protocolを通じてAIアシスタントに公式Microsoftドキュメントへのリアルタイムアクセスを提供するクラウドホスト型サービスです。この本番対応サーバーは包括的なMicrosoft Learnエコシステムに接続し、すべての公式Microsoftソースにわたるセマンティック検索を可能にします。
> **🎯 本番環境対応ツール**  
>  
> これは、今日から使える本物のMCPサーバーです！Microsoft Learn Docs MCPサーバーについて詳しくは、[**Microsoft MCPサーバーガイド**](microsoft-mcp-servers.md#1--microsoft-learn-docs-mcp-server)をご覧ください。
**主な特徴:**
- Microsoft公式ドキュメント、Azureドキュメント、Microsoft 365ドキュメントへのリアルタイムアクセス
- 文脈と意図を理解する高度なセマンティック検索機能
- Microsoft Learnコンテンツが公開されるたびに常に最新情報を提供
- Microsoft Learn、Azureドキュメント、Microsoft 365ソースにわたる包括的なカバレッジ
- 最大10件の高品質なコンテンツチャンクを記事タイトルとURL付きで返却

**重要性:**
- Microsoftテクノロジーにおける「古いAI知識」の問題を解決
- 最新の.NET、C#、Azure、Microsoft 365機能へのアクセスをAIアシスタントに提供
- 正確なコード生成のための信頼性の高い一次情報を提供
- 急速に進化するMicrosoftテクノロジーを扱う開発者にとって不可欠

**結果:**
- Microsoftテクノロジーに関するAI生成コードの精度が劇的に向上
- 最新のドキュメントやベストプラクティスを探す時間を削減
- 文脈に応じたドキュメント検索で開発者の生産性を向上
- IDEを離れることなく開発ワークフローにシームレスに統合

**参考資料:**
- [Microsoft Learn Docs MCP Server GitHub Repository](https://github.com/MicrosoftDocs/mcp)
- [Microsoft Learn Documentation](https://learn.microsoft.com/)

## 実践プロジェクト

### プロジェクト1: マルチプロバイダーMCPサーバーの構築

**目的:** 特定の条件に基づいて複数のAIモデルプロバイダーにリクエストをルーティングできるMCPサーバーを作成する。

**要件:**

- 少なくとも3つの異なるモデルプロバイダーをサポート（例: OpenAI、Anthropic、ローカルモデル）
- リクエストメタデータに基づくルーティングメカニズムを実装
- プロバイダーの認証情報を管理するための設定システムを作成
- パフォーマンスとコストを最適化するためのキャッシュを追加
- 使用状況を監視するためのシンプルなダッシュボードを構築

**実装手順:**

1. MCPサーバーの基本インフラをセットアップ
2. 各AIモデルサービスのプロバイダーアダプターを実装
3. リクエスト属性に基づくルーティングロジックを作成
4. 頻繁なリクエストのためのキャッシュメカニズムを追加
5. 監視ダッシュボードを開発
6. 様々なリクエストパターンでテスト

**技術:** Python (.NET/Java/Pythonのいずれか)、Redis（キャッシュ用）、シンプルなWebフレームワーク（ダッシュボード用）

### プロジェクト2: エンタープライズプロンプト管理システム

**目的:** 組織全体でプロンプトテンプレートを管理、バージョン管理、展開するためのMCPベースのシステムを開発する。

**要件:**

- プロンプトテンプレートの集中リポジトリを作成
- バージョン管理と承認ワークフローを実装
- サンプル入力を使用したテンプレートテスト機能を構築
- 役割ベースのアクセス制御を開発
- テンプレートの取得と展開のためのAPIを作成

**実装手順:**

1. テンプレート保存用のデータベーススキーマを設計
2. テンプレートのCRUD操作用のコアAPIを作成
3. バージョン管理システムを実装
4. 承認ワークフローを構築
5. テストフレームワークを開発
6. 管理用のシンプルなWebインターフェースを作成
7. MCPサーバーと統合

**技術:** 好みのバックエンドフレームワーク、SQLまたはNoSQLデータベース、管理インターフェース用のフロントエンドフレームワーク

### プロジェクト3: MCPベースのコンテンツ生成プラットフォーム

**目的:** MCPを活用して異なるコンテンツタイプで一貫した結果を提供するコンテンツ生成プラットフォームを構築する。

**要件:**

- 複数のコンテンツ形式をサポート（ブログ記事、ソーシャルメディア、マーケティングコピー）
- カスタマイズオプション付きのテンプレートベースの生成を実装
- コンテンツレビューとフィードバックシステムを作成
- コンテンツのパフォーマンス指標を追跡
- コンテンツのバージョン管理と反復をサポート

**実装手順:**

1. MCPクライアントインフラをセットアップ
2. 異なるコンテンツタイプのテンプレートを作成
3. コンテンツ生成パイプラインを構築
4. レビューシステムを実装
5. 指標追跡システムを開発
6. テンプレート管理とコンテンツ生成用のユーザーインターフェースを作成

**技術:** 好みのプログラミング言語、Webフレームワーク、データベースシステム

## MCP技術の将来の方向性

### 新たなトレンド

1. **マルチモーダルMCP**
   - 画像、音声、動画モデルとの標準化されたインタラクションを拡張
   - クロスモーダル推論能力の開発
   - 異なるモダリティに対応した標準化されたプロンプト形式

2. **フェデレーテッドMCPインフラ**
   - 組織間でリソースを共有できる分散型MCPネットワーク
   - 安全なモデル共有のための標準化されたプロトコル
   - プライバシー保護型計算技術

3. **MCPマーケットプレイス**
   - MCPテンプレートやプラグインを共有・収益化するエコシステム
   - 品質保証と認証プロセス
   - モデルマーケットプレイスとの統合

4. **エッジコンピューティング向けMCP**
   - リソース制約のあるエッジデバイス向けにMCP標準を適応
   - 低帯域幅環境向けに最適化されたプロトコル
   - IoTエコシステム向けの特化型MCP実装

5. **規制フレームワーク**
   - 規制遵守のためのMCP拡張の開発
   - 標準化された監査トレイルと説明可能性インターフェース
   - 新興のAIガバナンスフレームワークとの統合

### MicrosoftによるMCPソリューション

MicrosoftとAzureは、様々なシナリオでMCPを実装するためのオープンソースリポジトリを開発しています:

#### Microsoft組織

1. [playwright-mcp](https://github.com/microsoft/playwright-mcp) - ブラウザ自動化とテスト用のPlaywright MCPサーバー
2. [files-mcp-server](https://github.com/microsoft/files-mcp-server) - ローカルテストとコミュニティ貢献のためのOneDrive MCPサーバー実装
3. [NLWeb](https://github.com/microsoft/NlWeb) - AI Webの基盤層を確立するためのオープンプロトコルと関連オープンソースツールのコレクション

#### Azure-Samples組織

1. [mcp](https://github.com/Azure-Samples/mcp) - Azure上でMCPサーバーを構築・統合するためのサンプル、ツール、リソースへのリンク
2. [mcp-auth-servers](https://github.com/Azure-Samples/mcp-auth-servers) - 現行のModel Context Protocol仕様を使用した認証を示すリファレンスMCPサーバー
3. [remote-mcp-functions](https://github.com/Azure-Samples/remote-mcp-functions) - Azure FunctionsでのリモートMCPサーバー実装のランディングページ（言語別リポジトリへのリンク付き）
4. [remote-mcp-functions-python](https://github.com/Azure-Samples/remote-mcp-functions-python) - Pythonを使用したカスタムリモートMCPサーバーの構築と展開のためのクイックスタートテンプレート
5. [remote-mcp-functions-dotnet](https://github.com/Azure-Samples/remote-mcp-functions-dotnet) - .NET/C#を使用したカスタムリモートMCPサーバーの構築と展開のためのクイックスタートテンプレート
6. [remote-mcp-functions-typescript](https://github.com/Azure-Samples/remote-mcp-functions-typescript) - TypeScriptを使用したカスタムリモートMCPサーバーの構築と展開のためのクイックスタートテンプレート
7. [remote-mcp-apim-functions-python](https://github.com/Azure-Samples/remote-mcp-apim-functions-python) - Pythonを使用したAzure API ManagementをリモートMCPサーバーへのAIゲートウェイとして統合
8. [AI-Gateway](https://github.com/Azure-Samples/AI-Gateway) - APIM ❤️ AI実験（MCP機能を含む）、Azure OpenAIおよびAI Foundryとの統合

これらのリポジトリは、Model Context Protocolを使用した基本的なサーバー実装から認証、クラウド展開、エンタープライズ統合シナリオまで、様々なユースケースをカバーしています。

#### MCPリソースディレクトリ

公式Microsoft MCPリポジトリ内の[MCPリソースディレクトリ](https://github.com/microsoft/mcp/tree/main/Resources)は、Model Context Protocolサーバーで使用するサンプルリソース、プロンプトテンプレート、ツール定義のキュレーションされたコレクションを提供します。このディレクトリは、再利用可能な構築ブロックやベストプラクティス例を提供することで、MCPの迅速な導入を支援します:

- **プロンプトテンプレート:** 一般的なAIタスクやシナリオ向けのすぐに使用可能なプロンプトテンプレート。独自のMCPサーバー実装に適応可能。
- **ツール定義:** 異なるMCPサーバー間でツールの統合と呼び出しを標準化するためのツールスキーマとメタデータの例。
- **リソースサンプル:** MCPフレームワーク内でデータソース、API、外部サービスに接続するためのリソース定義例。
- **リファレンス実装:** 実際のMCPプロジェクトでリソース、プロンプト、ツールを構造化・整理する方法を示す実践的なサンプル。

これらのリソースは開発を加速し、標準化を促進し、MCPベースのソリューションを構築・展開する際のベストプラクティスを確保します。

#### MCPリソースディレクトリ

- [MCP Resources (Sample Prompts, Tools, and Resource Definitions)](https://github.com/microsoft/mcp/tree/main/Resources)

### 研究機会

- MCPフレームワーク内での効率的なプロンプト最適化技術
- マルチテナントMCP展開のためのセキュリティモデル
- 異なるMCP実装間のパフォーマンスベンチマーク
- MCPサーバーの形式的検証方法

## 結論

Model Context Protocol (MCP)は、業界全体で標準化され、安全で相互運用可能なAI統合の未来を急速に形作っています。このレッスンで紹介したケーススタディや実践プロジェクトを通じて、MicrosoftやAzureを含む初期採用者が、MCPを活用して現実世界の課題を解決し、AIの導入を加速し、コンプライアンス、セキュリティ、スケーラビリティを確保している様子を確認しました。MCPのモジュール型アプローチは、大規模言語モデル、ツール、エンタープライズデータを統一された監査可能なフレームワークで接続することを可能にします。MCPが進化を続ける中、コミュニティへの参加、オープンソースリソースの探索、ベストプラクティスの適用が、堅牢で未来対応のAIソリューションを構築する鍵となります。

## 追加リソース

- [MCP Foundry GitHub Repository](https://github.com/azure-ai-foundry/mcp-foundry)
- [Foundry MCP Playground](https://github.com/azure-ai-foundry/foundry-mcp-playground)
- [Integrating Azure AI Agents with MCP (Microsoft Foundry Blog)](https://devblogs.microsoft.com/foundry/integrating-azure-ai-agents-mcp/)
- [MCP GitHub Repository (Microsoft)](https://github.com/microsoft/mcp)
- [MCP Resources Directory (Sample Prompts, Tools, and Resource Definitions)](https://github.com/microsoft/mcp/tree/main/Resources)
- [MCP Community & Documentation](https://modelcontextprotocol.io/introduction)
- [Azure MCP Documentation](https://aka.ms/azmcp)
- [Playwright MCP Server GitHub Repository](https://github.com/microsoft/playwright-mcp)
- [Files MCP Server (OneDrive)](https://github.com/microsoft/files-mcp-server)
- [Azure-Samples MCP](https://github.com/Azure-Samples/mcp)
- [MCP Auth Servers (Azure-Samples)](https://github.com/Azure-Samples/mcp-auth-servers)
- [Remote MCP Functions (Azure-Samples)](https://github.com/Azure-Samples/remote-mcp-functions)
- [Remote MCP Functions Python (Azure-Samples)](https://github.com/Azure-Samples/remote-mcp-functions-python)
- [Remote MCP Functions .NET (Azure-Samples)](https://github.com/Azure-Samples/remote-mcp-functions-dotnet)
- [Remote MCP Functions TypeScript (Azure-Samples)](https://github.com/Azure-Samples/remote-mcp-functions-typescript)
- [Remote MCP APIM Functions Python (Azure-Samples)](https://github.com/Azure-Samples/remote-mcp-apim-functions-python)
- [AI-Gateway (Azure-Samples)](https://github.com/Azure-Samples/AI-Gateway)
- [Microsoft AI and Automation Solutions](https://azure.microsoft.com/en-us/products/ai-services/)

## 演習

1. ケーススタディの1つを分析し、代替の実装アプローチを提案してください。
2. プロジェクトアイデアの1つを選び、詳細な技術仕様を作成してください。
3. ケーススタディで取り上げられていない業界を調査し、MCPがその特定の課題にどのように対応できるかを概説してください。
4. 将来の方向性の1つを探求し、それをサポートする新しいMCP拡張のコンセプトを作成してください。

次へ: [Microsoft MCPサーバー](../07-LessonsfromEarlyAdoption/microsoft-mcp-servers.md)

**免責事項**:  
この文書は、AI翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されています。正確性を追求しておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があることをご承知おきください。元の言語で記載された文書が公式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。この翻訳の使用に起因する誤解や誤認について、当方は一切の責任を負いません。
