# 🌟 先行導入者からの教訓

[![Lessons from MCP Early Adopters](../../../translated_images/ja/08.980bb2babbaadd8a.webp)](https://youtu.be/jds7dSmNptE)

_(上の画像をクリックすると、本レッスンのビデオをご覧いただけます)_

## 🎯 本モジュールの内容

本モジュールでは、実際の組織や開発者がModel Context Protocol（MCP）を活用して具体的な課題を解決し、イノベーションを促進している方法を探ります。詳細なケーススタディ、実践的なプロジェクト、具体例を通じて、MCPがどのように言語モデル、ツール、企業データを接続する安全でスケーラブルなAI統合を実現しているかを理解します。

### 📚 MCPの実践例を見てみよう

これらの原則が実運用ツールに適用されている様子を見たいですか？本日利用可能なMicrosoft MCPサーバーの実例を紹介した[**10のMicrosoft MCPサーバーが開発者の生産性を変革している**](microsoft-mcp-servers.md)をご覧ください。

## 概要

このレッスンでは、先行導入者がModel Context Protocol（MCP）を活用して実世界の課題を解決し、業界横断的にイノベーションを推進してきた事例を探ります。詳細なケーススタディや実践的なプロジェクトを通じて、MCPにより大規模言語モデル、ツール、企業データを統合する標準化され安全でスケーラブルなAI統合が実現されている様子をご覧いただけます。MCPベースのソリューション設計と構築の実務経験を得て、確立された実装パターンから学び、MCPを本番環境に展開する際のベストプラクティスを発見しましょう。また、新たな動向や将来の展望、オープンソースリソースも紹介し、MCP技術とその進化するエコシステムの最前線に立てるよう支援します。

## 学習目標

- 業界ごとに異なる実際のMCP実装を分析する
- MCPベースの完全なアプリケーションを設計・構築する
- MCP技術における新興トレンドと将来の方向性を探る
- 実際の開発シナリオでベストプラクティスを適用する

## 実際のMCP実装事例

### ケーススタディ1：企業のカスタマーサポート自動化

多国籍企業がMCPベースのソリューションを導入して、顧客サポートシステム全体でAIインタラクションの標準化を実現しました。これにより次が可能になりました：

- 複数のLLMプロバイダーに対する統一インターフェースの作成
- 部門を横断した一貫したプロンプト管理の維持
- 強固なセキュリティとコンプライアンス管理の実装
- 特定のニーズに応じて異なるAIモデルを容易に切り替え可能

**技術的実装：**

```python
# カスタマーサポートのためのPython MCPサーバー実装
import logging
import asyncio
from modelcontextprotocol import create_server, ServerConfig
from modelcontextprotocol.server import MCPServer
from modelcontextprotocol.transports import create_http_transport
from modelcontextprotocol.resources import ResourceDefinition
from modelcontextprotocol.prompts import PromptDefinition
from modelcontextprotocol.tool import ToolDefinition

# ロギングを設定する
logging.basicConfig(level=logging.INFO)

async def main():
    # サーバー設定を作成する
    config = ServerConfig(
        name="Enterprise Customer Support Server",
        version="1.0.0",
        description="MCP server for handling customer support inquiries"
    )
    
    # MCPサーバーを初期化する
    server = create_server(config)
    
    # ナレッジベースリソースを登録する
    server.resources.register(
        ResourceDefinition(
            name="customer_kb",
            description="Customer knowledge base documentation"
        ),
        lambda params: get_customer_documentation(params)
    )
    
    # プロンプトテンプレートを登録する
    server.prompts.register(
        PromptDefinition(
            name="support_template",
            description="Templates for customer support responses"
        ),
        lambda params: get_support_templates(params)
    )
    
    # サポートツールを登録する
    server.tools.register(
        ToolDefinition(
            name="ticketing",
            description="Create and update support tickets"
        ),
        handle_ticketing_operations
    )
    
    # HTTPトランスポートでサーバーを起動する
    transport = create_http_transport(port=8080)
    await server.run(transport)

if __name__ == "__main__":
    asyncio.run(main())
```

**結果：** モデルコストを30%削減、応答の一貫性を45%向上させ、グローバル運用におけるコンプライアンスを強化。

### ケーススタディ2：医療診断アシスタント

医療プロバイダーは、複数の専門的な医療AIモデルの統合と患者データの機密保護を両立させるためのMCPインフラを開発しました：

- 一般モデルと専門モデル間のシームレスな切り替え
- 厳格なプライバシー管理と監査トレイル
- 既存の電子カルテ（EHR）システムとの統合
- 医療用語に特化した一貫したプロンプトエンジニアリング

**技術的実装：**

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

**結果：** 医師向けの診断提案が改善され、HIPAA完全準拠を維持しつつシステム間のコンテキスト切替が大幅に減少。

### ケーススタディ3：金融サービスのリスク分析

金融機関が部門間でのリスク分析プロセスの標準化を目的にMCPを導入しました：

- 信用リスク、詐欺検出、投資リスクモデルの統一インターフェースを作成
- 厳格なアクセス制御とモデルバージョニングを実施
- すべてのAI推奨の監査可能性を確保
- 多様なシステム間で一貫したデータフォーマットを維持

**技術的実装：**

```java
// 財務リスク評価のためのJava MCPサーバー
import org.mcp.server.*;
import org.mcp.security.*;

public class FinancialRiskMCPServer {
    public static void main(String[] args) {
        // 金融コンプライアンス機能を備えたMCPサーバーを作成する
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

**結果：** 規制遵守の強化、モデル展開サイクルの40%高速化、部門間のリスク評価の一貫性向上。

### ケーススタディ4：Microsoft Playwright MCPサーバーによるブラウザー自動化

Microsoftは[Playwright MCPサーバー](https://github.com/microsoft/playwright-mcp)を開発し、Model Context Protocolを通じて安全かつ標準化されたブラウザー自動化を実現しています。この本番対応サーバーにより、AIエージェントやLLMが制御された監査可能で拡張性のある方法でWebブラウザとやり取りでき、自動化テスト、データ抽出、エンドツーエンドワークフローなどのユースケースを可能にします。

> **🎯 本番対応ツール**
> 
> このケーススタディは、本日から使用可能な実際のMCPサーバーを紹介しています！Playwright MCPサーバーおよび他9つの本番対応Microsoft MCPサーバーについては[**Microsoft MCPサーバーガイド**](microsoft-mcp-servers.md#8--playwright-mcp-server)をご覧ください。

**主な機能：**
- ブラウザー自動化機能（ナビゲーション、フォーム入力、スクリーンショットなど）をMCPツールとして公開
- 不正操作防止のための厳格なアクセス制御とサンドボックス化を実装
- すべてのブラウザー操作に対して詳細な監査ログを提供
- Azure OpenAIや他のLLMプロバイダーとの統合をサポートし、エージェント駆動の自動化を実現
- GitHub Copilotのコーディングエージェントにウェブ閲覧機能を提供

**技術的実装：**

```typescript
// TypeScript: MCPサーバーにPlaywrightブラウザ自動化ツールを登録する
import { createServer, ToolDefinition } from 'modelcontextprotocol';
import { launch } from 'playwright';

const server = createServer({
  name: 'Playwright MCP Server',
  version: '1.0.0',
  description: 'MCP server for browser automation using Playwright'
});

// URLに移動してスクリーンショットをキャプチャするツールを登録する
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

// MCPサーバーを起動する
server.listen(8080);
```

**結果：**

- AIエージェントやLLM向けの安全でプログラム可能なブラウザー自動化を実現
- 手動テスト工数を削減し、Webアプリケーションのテストカバレッジを改善
- 企業環境でのブラウザベースツール統合のための再利用可能で拡張可能なフレームワークを提供
- GitHub CopilotのWeb閲覧機能を支援

**参考資料：**

- [Playwright MCP Server GitHubリポジトリ](https://github.com/microsoft/playwright-mcp)
- [Microsoft AIおよび自動化ソリューション](https://azure.microsoft.com/en-us/products/ai-services/)

### ケーススタディ5：Azure MCP – エンタープライズグレードのModel Context Protocolサービス

Azure MCP Server ([https://aka.ms/azmcp](https://aka.ms/azmcp))は、Microsoftによるモデルコンテキストプロトコルのマネージドでエンタープライズ向けの実装であり、クラウドサービスとしてスケーラブルで安全かつコンプライアンス準拠のMCPサーバー機能を提供します。Azure MCPにより組織は高速でMCPサーバーを展開・管理し、Azure AI、データ、およびセキュリティサービスと統合して運用負荷を低減し、AI導入を加速できます。

> **🎯 本番対応ツール**
> 
> これは本日から使用可能な実際のMCPサーバーです！Microsoft Foundry MCPサーバーの詳細は[**Microsoft MCPサーバーガイド**](microsoft-mcp-servers.md)をご覧ください。


- スケーリング、監視、セキュリティを組み込んだフルマネージドMCPサーバーホスティング
- Azure OpenAI、Azure AI Search、その他Azureサービスとのネイティブ統合
- Microsoft Entra IDによるエンタープライズ認証と認可
- カスタムツール、プロンプトテンプレート、リソースコネクタのサポート
- エンタープライズのセキュリティと規制要件に準拠

**技術的実装：**

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

**結果：**  
- 企業のAIプロジェクトに対して即利用可能でコンプライアンス準拠のMCPサーバープラットフォームを提供し、価値創出までの時間を短縮
- LLM、ツール、企業データソースの統合を簡素化
- MCPワークロードのセキュリティ、可観測性、運用効率を向上
- Azure SDKのベストプラクティスと最新の認証パターンによりコード品質を改善

**参考資料：**  
- [Azure MCP ドキュメント](https://aka.ms/azmcp)
- [Azure MCP Server GitHubリポジトリ](https://github.com/Azure/azure-mcp)
- [Azure AI サービス](https://azure.microsoft.com/en-us/products/ai-services/)
- [Microsoft MCP Center](https://mcp.azure.com)

## ケーススタディ6：NLWeb
MCP（Model Context Protocol）は、チャットボットやAIアシスタントがツールとやり取りするための新興プロトコルです。すべてのNLWebインスタンスはMCPサーバーでもあり、自然言語でウェブサイトに質問するための1つのコアメソッドaskをサポートしています。返された応答は、ウェブデータの記述に広く使われる語彙であるschema.orgを活用します。ざっくり言えば、MCPはHttpに対するHTMLのようなNLWebです。NLWebはプロトコル、Schema.orgフォーマット、サンプルコードを組み合わせてサイトが迅速にこれらのエンドポイントを作成できるようにし、会話型インターフェースを通じて人間に、自然なエージェント間通信を通じて機械に利便性を提供します。

NLWebには2つの明確なコンポーネントがあります。
- 非常にシンプルなプロトコルで、サイトに自然言語でインターフェースし、jsonおよびschema.orgを使って回答するフォーマットです。REST APIのドキュメントを参照してください。
- (1)のシンプルな実装で、既存のマークアップを活用し、製品、レシピ、観光地、レビューなどのアイテムリストとして抽象化可能なサイト向け。ユーザーインターフェースウィジェットと組み合わせて、サイトコンテンツに会話型インターフェースを簡単に提供できます。詳細はLife of a chat queryのドキュメントをご覧ください。
 
**参考資料：**  
- [Azure MCP ドキュメント](https://aka.ms/azmcp)
- [NLWeb](https://github.com/microsoft/NlWeb)

### ケーススタディ7：Microsoft Foundry MCPサーバー – エンタープライズAIエージェント統合

Microsoft Foundry MCPサーバーは、MCPがエンタープライズ環境でのAIエージェントやワークフローの管理・オーケストレーションにどのように活用できるかを示しています。MCPをMicrosoft Foundryと統合することで、組織はエージェント間のやり取りを標準化し、Foundryのワークフロー管理機能を活用し、安全でスケーラブルな展開を保証できます。

> **🎯 本番対応ツール**
> 
> これは本日から使える実際のMCPサーバーです！Microsoft Foundry MCPサーバーの詳細は[**Microsoft MCPサーバーガイド**](microsoft-mcp-servers.md#9--microsoft-foundry-mcp-server)をご覧ください。

**主な機能：**
- モデルカタログや展開管理を含むAzureのAIエコシステムへの包括的アクセス
- RAGアプリケーション向けAzure AI Searchを使用した知識インデックス化
- AIモデル性能と品質保証のための評価ツール
- Microsoft Foundry CatalogおよびLabsとの統合で先端の研究モデルに対応
- 実運用向けのエージェント管理と評価機能

**結果：**
- AIエージェントワークフローの迅速なプロトタイピングと堅牢な監視
- Azure AIサービスとのシームレスな統合による高度なシナリオ対応
- エージェントパイプライン構築、展開、監視の統一インターフェース
- エンタープライズ向けのセキュリティ、コンプライアンス、運用効率の改善
- エージェント駆動の複雑なプロセスを制御しつつAI導入を加速

**参考資料：**
- [Microsoft Foundry MCP Server GitHubリポジトリ](https://github.com/azure-ai-foundry/mcp-foundry)
- [Azure AIエージェントをMCPで統合（Microsoft Foundryブログ）](https://devblogs.microsoft.com/foundry/integrating-azure-ai-agents-mcp/)

### ケーススタディ8：Foundry MCP Playground – 実験とプロトタイピング

Foundry MCP PlaygroundはMCPサーバーおよびMicrosoft Foundry統合の実験に即利用可能な環境を提供します。開発者はMicrosoft Foundry CatalogやLabsのリソースを使って迅速にAIモデルやエージェントワークフローをプロトタイプ、テスト、評価できます。セットアップが簡便でサンプルプロジェクトを備え、協働開発をサポートし、ベストプラクティスや新規シナリオの検証を最小限のコストで行えます。特に複雑なインフラなしにアイディア検証、実験共有、学習促進を目指すチームに有益で、MCPとMicrosoft Foundryエコシステムにおけるイノベーションとコミュニティ貢献を促進します。

**参考資料：**

- [Foundry MCP Playground GitHubリポジトリ](https://github.com/azure-ai-foundry/foundry-mcp-playground)

### ケーススタディ9：Microsoft Learn Docs MCPサーバー – AI駆動のドキュメントアクセス

Microsoft Learn Docs MCPサーバーは、Model Context Protocolを通じてAIアシスタントに公式Microsoftドキュメントへのリアルタイムアクセスを提供するクラウドサービスです。この本番対応サーバーはMicrosoft Learnの包括的エコシステムに接続し、公式Microsoftソース全体で意味検索を可能にします。

> **🎯 本番対応ツール**
> 
> これは本日使える実際のMCPサーバーです！Microsoft Learn Docs MCPサーバーの詳細は[**Microsoft MCPサーバーガイド**](microsoft-mcp-servers.md#1--microsoft-learn-docs-mcp-server)をご覧ください。

**主な機能：**
- Microsoft公式ドキュメント、Azureドキュメント、Microsoft 365ドキュメントへのリアルタイムアクセス
- コンテキストと意図を理解する高度な意味検索機能
- Microsoft Learnコンテンツが公開されるたびに常に最新情報を提供
- Microsoft Learn、Azureドキュメント、Microsoft 365の全ソースを網羅
- 記事タイトルとURL付きで最大10件の高品質コンテンツチャンクを返す

**重要な理由：**
- Microsoft技術に関する「古いAI知識」問題を解決
- AIアシスタントが最新の.NET、C#、Azure、およびMicrosoft 365機能にアクセス可能に
- 正確なコード生成のための権威ある一次情報を提供
- 急速に進化するMicrosoft技術を扱う開発者に必須

**結果：**
- Microsoft技術向けAI生成コードの精度が劇的に向上
- 最新ドキュメントやベストプラクティスの検索時間を削減
- コンテキスト対応のドキュメント取得で開発者の生産性向上
- IDEを離れずに開発ワークフローへシームレス統合

**参考資料：**
- [Microsoft Learn Docs MCP Server GitHubリポジトリ](https://github.com/MicrosoftDocs/mcp)
- [Microsoft Learn ドキュメント](https://learn.microsoft.com/)

## ハンズオンプロジェクト

### プロジェクト1：マルチプロバイダMCPサーバーを構築する

**目標：** 特定の条件に基づいて複数のAIモデルプロバイダーへリクエストをルーティングできるMCPサーバーを作成する。

**要件：**

- 少なくとも3つの異なるモデルプロバイダー（例：OpenAI、Anthropic、ローカルモデル）をサポート
- リクエストメタデータに基づくルーティング機構を実装
- プロバイダー認証情報管理のための設定システムを作成
- パフォーマンスとコスト最適化のためのキャッシングを追加
- 使用状況をモニタリングするシンプルなダッシュボードを構築

**実装手順：**

1. 基本的なMCPサーバーインフラをセットアップ
2. 各AIモデルサービスのプロバイダーアダプターを実装
3. リクエスト属性に基づくルーティングロジックを作成
4. 頻繁なリクエスト向けのキャッシュ機構を追加
5. モニタリングダッシュボードを開発
6. 様々なリクエストパターンでテスト

**技術：** Python（.NET/Java/Pythonはご希望に応じて選択）、キャッシュ用にRedis、ダッシュボードにはシンプルなWebフレームワークを選択。

### プロジェクト2：企業向けプロンプト管理システム

**目標：** 組織全体でプロンプトテンプレートを管理、バージョン管理、デプロイできるMCPベースのシステムを開発する。

**要件：**


- プロンプトテンプレートの集中管理リポジトリを作成する
- バージョン管理と承認ワークフローを実装する
- サンプル入力によるテンプレートテスト機能を構築する
- ロールベースのアクセス制御を開発する
- テンプレートの取得および展開用APIを作成する

**実装手順:**

1. テンプレート保存用のデータベーススキーマを設計する
2. テンプレートのCRUD操作用コアAPIを作成する
3. バージョニングシステムを実装する
4. 承認ワークフローを構築する
5. テストフレームワークを開発する
6. 管理用の簡易ウェブインターフェースを作成する
7. MCPサーバーと連携する

**技術:** お好みのバックエンドフレームワーク、SQLまたはNoSQLデータベース、管理インターフェースのためのフロントエンドフレームワークを使用してください。

### プロジェクト3: MCPベースのコンテンツ生成プラットフォーム

**目的:** MCPを利用して、異なるコンテンツタイプにわたって一貫した結果を提供するコンテンツ生成プラットフォームを構築する。

**要件:**

- 複数のコンテンツ形式をサポート（ブログ投稿、ソーシャルメディア、マーケティングコピー）
- カスタマイズオプションを備えたテンプレートベースの生成を実装する
- コンテンツレビューおよびフィードバックシステムを作成する
- コンテンツパフォーマンス指標を追跡する
- コンテンツのバージョニングと反復に対応する

**実装手順:**

1. MCPクライアントのインフラをセットアップする
2. 異なるコンテンツタイプのテンプレートを作成する
3. コンテンツ生成パイプラインを構築する
4. レビューシステムを実装する
5. 指標追跡システムを開発する
6. テンプレート管理およびコンテンツ生成用のユーザーインターフェースを作成する

**技術:** お好みのプログラミング言語、ウェブフレームワーク、およびデータベースシステムを使用してください。

## MCP技術の将来の方向性

### 新興トレンド

1. **マルチモーダルMCP**
   - MCPの画像、音声、ビデオモデルとの標準化されたインタラクションへの拡張
   - クロスモーダル推論能力の開発
   - 異なるモダリティに対応した標準化されたプロンプト形式

2. **フェデレーテッドMCPインフラストラクチャ**
   - 組織間でリソースを共有できる分散型MCPネットワーク
   - 安全なモデル共有のための標準化プロトコル
   - プライバシー保護計算技術

3. **MCPマーケットプレイス**
   - MCPテンプレートやプラグインの共有および収益化のためのエコシステム
   - 品質保証および認証プロセス
   - モデルマーケットプレイスとの統合

4. **エッジコンピューティング向けMCP**
   - リソース制約のあるエッジデバイス向けのMCP標準の適応
   - 低帯域幅環境向けの最適化プロトコル
   - IoTエコシステム向けの特化型MCP実装

5. <strong>規制フレームワーク</strong>
   - 規制遵守のためのMCP拡張の開発
   - 標準化された監査トレイルおよび説明可能性インターフェース
   - 新興のAIガバナンスフレームワークとの統合

### MicrosoftによるMCPソリューション

MicrosoftとAzureは、様々なシナリオでMCPを実装するために開発者が利用できる複数のオープンソースリポジトリを提供しています：

#### Microsoft組織

1. [playwright-mcp](https://github.com/microsoft/playwright-mcp) - ブラウザ自動化およびテスト用のPlaywright MCPサーバー
2. [files-mcp-server](https://github.com/microsoft/files-mcp-server) - ローカルテストやコミュニティ貢献向けのOneDrive MCPサーバー実装
3. [NLWeb](https://github.com/microsoft/NlWeb) - NLWebはオープンプロトコルと関連するオープンソースツールのコレクションで、AI Webの基盤層の確立に注力

#### Azure-Samples組織

1. [mcp](https://github.com/Azure-Samples/mcp) - 複数言語でAzure上のMCPサーバー構築および統合用サンプル、ツール、リソースへのリンク
2. [mcp-auth-servers](https://github.com/Azure-Samples/mcp-auth-servers) - 現行Model Context Protocol仕様での認証を示すリファレンスMCPサーバー
3. [remote-mcp-functions](https://github.com/Azure-Samples/remote-mcp-functions) - Azure FunctionsでのリモートMCPサーバー実装のランディングページおよび言語別リポジトリリンク
4. [remote-mcp-functions-python](https://github.com/Azure-Samples/remote-mcp-functions-python) - Azure Functions（Python）を使ったカスタムリモートMCPサーバー構築および展開のクイックスタートテンプレート
5. [remote-mcp-functions-dotnet](https://github.com/Azure-Samples/remote-mcp-functions-dotnet) - Azure Functions（.NET/C#）を使ったカスタムリモートMCPサーバー構築および展開のクイックスタートテンプレート
6. [remote-mcp-functions-typescript](https://github.com/Azure-Samples/remote-mcp-functions-typescript) - Azure Functions（TypeScript）を使ったカスタムリモートMCPサーバー構築および展開のクイックスタートテンプレート
7. [remote-mcp-apim-functions-python](https://github.com/Azure-Samples/remote-mcp-apim-functions-python) - Pythonを用いたリモートMCPサーバーへのAzure API ManagementによるAIゲートウェイ
8. [AI-Gateway](https://github.com/Azure-Samples/AI-Gateway) - MCP機能を含むAPIM ❤️ AI実験、Azure OpenAIおよびAI Foundryとの統合

これらのリポジトリは、異なるプログラミング言語やAzureサービスを横断してModel Context Protocolを活用するためのさまざまな実装、テンプレート、リソースを提供しています。基本的なサーバー実装から認証、クラウド展開、企業統合シナリオに至るまで幅広いユースケースをカバーしています。

#### MCPリソースディレクトリ

公式Microsoft MCPリポジトリの[MCP Resourcesディレクトリ](https://github.com/microsoft/mcp/tree/main/Resources)は、Model Context Protocolサーバーで利用できるサンプルリソース、プロンプトテンプレート、ツール定義のキュレーションされたコレクションを提供しています。このディレクトリは開発者が再利用可能なビルディングブロックとベストプラクティス例を活用してMCPの使用を迅速に開始できるよう設計されています：

- **プロンプトテンプレート:** 一般的なAIタスクやシナリオ用のすぐに使えるプロンプトテンプレートで、独自のMCPサーバー実装に適応可能
- **ツール定義:** ツール統合と呼び出しを標準化するための例示的なツールスキーマとメタデータ
- **リソースサンプル:** MCPフレームワーク内でデータソース、API、外部サービスに接続するための例示的リソース定義
- **リファレンス実装:** 実際のMCPプロジェクトでリソース、プロンプト、およびツールを構造化・整理する方法を示す実践的なサンプル

これらのリソースは開発を加速し、標準化を促進し、MCPベースのソリューションを構築および展開する際のベストプラクティスの確保に役立ちます。

#### MCPリソースディレクトリ

- [MCP Resources（サンプルプロンプト、ツール、およびリソース定義）](https://github.com/microsoft/mcp/tree/main/Resources)

### 研究機会

- MCPフレームワーク内での効率的なプロンプト最適化技術
- マルチテナントMCP展開のためのセキュリティモデル
- 異なるMCP実装間のパフォーマンスベンチマーク
- MCPサーバーの形式的検証手法

## 結論

Model Context Protocol（MCP）は、業界を超えた標準化され、安全で相互運用可能なAI統合の未来を急速に形作っています。このレッスンの事例研究やハンズオンプロジェクトを通じて、MicrosoftやAzureをはじめとする初期採用者が、現実世界の課題を解決し、AIの採用を加速し、コンプライアンス、セキュリティ、スケーラビリティを確保するためにMCPをどのように活用しているかを示しました。MCPのモジュール式アプローチは、組織が大規模言語モデル、ツール、エンタープライズデータを統一された監査可能なフレームワークで接続できるようにします。MCPが進化し続ける中で、コミュニティとの関わり、オープンソースリソースの探求、ベストプラクティスの適用が堅牢で将来対応可能なAIソリューション構築の鍵となります。

## 追加リソース

- [MCP Foundry GitHubリポジトリ](https://github.com/azure-ai-foundry/mcp-foundry)
- [Foundry MCP Playground](https://github.com/azure-ai-foundry/foundry-mcp-playground)
- [Azure AIエージェントとMCPの統合（Microsoft Foundryブログ）](https://devblogs.microsoft.com/foundry/integrating-azure-ai-agents-mcp/)
- [MCP GitHubリポジトリ（Microsoft）](https://github.com/microsoft/mcp)
- [MCP Resourcesディレクトリ（サンプルプロンプト、ツール、およびリソース定義）](https://github.com/microsoft/mcp/tree/main/Resources)
- [MCPコミュニティ＆ドキュメント](https://modelcontextprotocol.io/introduction)
- [MCP仕様（2026-07-28）](https://modelcontextprotocol.io/specification/2026-07-28/)
- [Azure MCPドキュメント](https://aka.ms/azmcp)
- [OWASP MCPトップ10](https://microsoft.github.io/mcp-azure-security-guide/mcp/) - セキュリティベストプラクティス
- [Playwright MCPサーバーGitHubリポジトリ](https://github.com/microsoft/playwright-mcp)
- [Files MCPサーバー（OneDrive）](https://github.com/microsoft/files-mcp-server)
- [Azure-Samples MCP](https://github.com/Azure-Samples/mcp)
- [MCP Auth Servers（Azure-Samples）](https://github.com/Azure-Samples/mcp-auth-servers)
- [Remote MCP Functions（Azure-Samples）](https://github.com/Azure-Samples/remote-mcp-functions)
- [Remote MCP Functions Python（Azure-Samples）](https://github.com/Azure-Samples/remote-mcp-functions-python)
- [Remote MCP Functions .NET（Azure-Samples）](https://github.com/Azure-Samples/remote-mcp-functions-dotnet)
- [Remote MCP Functions TypeScript（Azure-Samples）](https://github.com/Azure-Samples/remote-mcp-functions-typescript)
- [Remote MCP APIM Functions Python（Azure-Samples）](https://github.com/Azure-Samples/remote-mcp-apim-functions-python)
- [AI-Gateway（Azure-Samples）](https://github.com/Azure-Samples/AI-Gateway)
- [Microsoft AIおよび自動化ソリューション](https://azure.microsoft.com/en-us/products/ai-services/)

## 演習

1. 事例研究の一つを分析し、代替の実装アプローチを提案してください。
2. プロジェクトアイデアの一つを選択し、詳細な技術仕様を作成してください。
3. 事例研究で扱われていない業界を調査し、その特有の課題に対してMCPがどのように対応できるかを概説してください。
4. 将来の方向性の一つを探求し、それをサポートする新しいMCP拡張のコンセプトを作成してください。

## 次のステップ

もっと探求する: [Microsoft MCP Servers](./microsoft-mcp-servers.md)

続きを読む: [モジュール8：ベストプラクティス](../08-BestPractices/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責事項**：
本書類は AI 翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されています。正確性を期していますが、自動翻訳には誤りや不正確な部分が含まれる可能性があることをご承知おきください。原文の原語版が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用により生じたいかなる誤解や解釈違いについても、当方は責任を負いかねます。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->