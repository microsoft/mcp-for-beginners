# 環境セットアップ

## 🎯 このラボで学べること

このハンズオンラボでは、PostgreSQLを統合したMCPサーバーを構築するための完全な開発環境をセットアップする手順を案内します。必要なツールを設定し、Azureリソースをデプロイし、実装に進む前にセットアップを検証します。

## 概要

適切な開発環境は、MCPサーバー開発の成功に不可欠です。このラボでは、Docker、Azureサービス、開発ツールのセットアップと、それらが正しく連携することを確認するための手順を提供します。

このラボを終える頃には、Zava Retail MCPサーバーを構築するための完全な開発環境が整います。

## 学習目標

このラボを終えると、以下ができるようになります：

- 必要な開発ツールを**インストールして設定**する
- MCPサーバーに必要なAzureリソースを**デプロイ**する
- PostgreSQLとMCPサーバーの**Dockerコンテナをセットアップ**する
- テスト接続を使用して環境セットアップを**検証**する
- 一般的なセットアップの問題や設定の問題を**トラブルシュート**する
- 開発のワークフローとファイル構造を**理解**する

## 📋 前提条件の確認

開始する前に、以下を確認してください：

### 必要な知識
- 基本的なコマンドライン操作（Windowsコマンドプロンプト/PowerShell）
- 環境変数の理解
- Gitバージョン管理の基本
- Dockerの基本概念（コンテナ、イメージ、ボリューム）

### システム要件
- **オペレーティングシステム**: Windows 10/11、macOS、またはLinux
- **RAM**: 最低8GB（推奨16GB）
- **ストレージ**: 少なくとも10GBの空き容量
- **ネットワーク**: ダウンロードとAzureデプロイのためのインターネット接続

### アカウント要件
- **Azureサブスクリプション**: 無料プランで十分
- **GitHubアカウント**: リポジトリへのアクセス用
- **Docker Hubアカウント**: （オプション）カスタムイメージの公開用

## 🛠️ ツールのインストール

### 1. Docker Desktopのインストール

Dockerは、開発セットアップのためのコンテナ化された環境を提供します。

#### Windowsでのインストール

1. **Docker Desktopをダウンロード**:
   ```cmd
   # Visit https://desktop.docker.com/win/stable/Docker%20Desktop%20Installer.exe
   # Or use Windows Package Manager
   winget install Docker.DockerDesktop
   ```

2. **インストールと設定**:
   - 管理者としてインストーラーを実行
   - プロンプトが表示されたらWSL 2統合を有効化
   - インストール完了後にコンピュータを再起動

3. **インストールの確認**:
   ```cmd
   docker --version
   docker-compose --version
   ```

#### macOSでのインストール

1. **ダウンロードとインストール**:
   ```bash
   # Download from https://desktop.docker.com/mac/stable/Docker.dmg
   # Or use Homebrew
   brew install --cask docker
   ```

2. **Docker Desktopを起動**:
   - アプリケーションからDocker Desktopを起動
   - 初期セットアップウィザードを完了

3. **インストールの確認**:
   ```bash
   docker --version
   docker-compose --version
   ```

#### Linuxでのインストール

1. **Docker Engineをインストール**:
   ```bash
   # Ubuntu/Debian
   curl -fsSL https://get.docker.com -o get-docker.sh
   sudo sh get-docker.sh
   sudo usermod -aG docker $USER
   
   # Log out and back in for group changes to take effect
   ```

2. **Docker Composeをインストール**:
   ```bash
   sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
   sudo chmod +x /usr/local/bin/docker-compose
   ```

### 2. Azure CLIのインストール

Azure CLIは、Azureリソースのデプロイと管理を可能にします。

#### Windowsでのインストール

```cmd
# Using Windows Package Manager
winget install Microsoft.AzureCLI

# Or download MSI from: https://aka.ms/installazurecliwindows
```

#### macOSでのインストール

```bash
# Using Homebrew
brew install azure-cli

# Or using installer
curl -L https://aka.ms/InstallAzureCli | bash
```

#### Linuxでのインストール

```bash
# Ubuntu/Debian
curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash

# RHEL/CentOS
sudo rpm --import https://packages.microsoft.com/keys/microsoft.asc
sudo dnf install azure-cli
```

#### 確認と認証

```bash
# Check installation
az version

# Login to Azure
az login

# Set default subscription (if you have multiple)
az account list --output table
az account set --subscription "Your-Subscription-Name"
```

### 3. Gitのインストール

Gitは、リポジトリのクローン作成とバージョン管理に必要です。

#### Windows

```cmd
# Using Windows Package Manager
winget install Git.Git

# Or download from: https://git-scm.com/download/win
```

#### macOS

```bash
# Git is usually pre-installed, but you can update via Homebrew
brew install git
```

#### Linux

```bash
# Ubuntu/Debian
sudo apt update && sudo apt install git

# RHEL/CentOS
sudo dnf install git
```

### 4. VS Codeのインストール

Visual Studio Codeは、MCPサポートを備えた統合開発環境を提供します。

#### インストール

```cmd
# Windows
winget install Microsoft.VisualStudioCode

# macOS
brew install --cask visual-studio-code

# Linux (Ubuntu/Debian)
sudo snap install code --classic
```

#### 必須拡張機能

以下のVS Code拡張機能をインストールしてください：

```bash
# Install via command line
code --install-extension ms-python.python
code --install-extension ms-vscode.vscode-json
code --install-extension ms-azuretools.vscode-docker
code --install-extension ms-vscode.azure-account
```

または、VS Code内でインストール：
1. VS Codeを開く
2. 拡張機能（Ctrl+Shift+X）に移動
3. 以下をインストール：
   - **Python**（Microsoft）
   - **Docker**（Microsoft）
   - **Azure Account**（Microsoft）
   - **JSON**（Microsoft）

### 5. Pythonのインストール

MCPサーバー開発にはPython 3.8以上が必要です。

#### Windows

```cmd
# Using Windows Package Manager
winget install Python.Python.3.11

# Or download from: https://www.python.org/downloads/
```

#### macOS

```bash
# Using Homebrew
brew install python@3.11
```

#### Linux

```bash
# Ubuntu/Debian
sudo apt update && sudo apt install python3.11 python3.11-pip python3.11-venv

# RHEL/CentOS
sudo dnf install python3.11 python3.11-pip
```

#### インストールの確認

```bash
python --version  # Should show Python 3.11.x
pip --version      # Should show pip version
```

## 🚀 プロジェクトセットアップ

### 1. リポジトリをクローン

```bash
# Clone the main repository
git clone https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail.git

# Navigate to the project directory
cd MCP-Server-and-PostgreSQL-Sample-Retail

# Verify repository structure
ls -la
```

### 2. Python仮想環境を作成

```bash
# Create virtual environment
python -m venv mcp-env

# Activate virtual environment
# Windows
mcp-env\Scripts\activate

# macOS/Linux
source mcp-env/bin/activate

# Upgrade pip
python -m pip install --upgrade pip
```

### 3. Python依存関係をインストール

```bash
# Install development dependencies
pip install -r requirements.lock.txt

# Verify key packages
pip list | grep fastmcp
pip list | grep asyncpg
pip list | grep azure
```

## ☁️ Azureリソースのデプロイ

### 1. リソース要件の理解

MCPサーバーには以下のAzureリソースが必要です：

| **リソース** | **目的** | **推定コスト** |
|--------------|-------------|-------------------|
| **Azure AI Foundry** | AIモデルのホスティングと管理 | $10-50/月 |
| **OpenAIデプロイメント** | テキスト埋め込みモデル（text-embedding-3-small） | $5-20/月 |
| **Application Insights** | モニタリングとテレメトリ | $5-15/月 |
| **リソースグループ** | リソースの整理 | 無料 |

### 2. Azureリソースをデプロイ

#### オプションA: 自動デプロイ（推奨）

```bash
# Navigate to infrastructure directory
cd infra

# Windows - PowerShell
./deploy.ps1

# macOS/Linux - Bash
./deploy.sh
```

デプロイメントスクリプトは以下を実行します：
1. 一意のリソースグループを作成
2. Azure AI Foundryリソースをデプロイ
3. text-embedding-3-smallモデルをデプロイ
4. Application Insightsを設定
5. 認証用のサービスプリンシパルを作成
6. 設定を含む`.env`ファイルを生成

#### オプションB: 手動デプロイ

自動スクリプトが失敗した場合や手動での制御を希望する場合：

```bash
# Set variables
RESOURCE_GROUP="rg-zava-mcp-$(date +%s)"
LOCATION="westus2"
AI_PROJECT_NAME="zava-ai-project"

# Create resource group
az group create --name $RESOURCE_GROUP --location $LOCATION

# Deploy main template
az deployment group create \
  --resource-group $RESOURCE_GROUP \
  --template-file main.bicep \
  --parameters location=$LOCATION \
  --parameters resourcePrefix="zava-mcp"
```

### 3. Azureデプロイの確認

```bash
# Check resource group
az group show --name $RESOURCE_GROUP --output table

# List deployed resources
az resource list --resource-group $RESOURCE_GROUP --output table

# Test AI service
az cognitiveservices account show \
  --name "your-ai-service-name" \
  --resource-group $RESOURCE_GROUP
```

### 4. 環境変数の設定

デプロイ後、`.env`ファイルが生成されているはずです。以下が含まれていることを確認してください：

```bash
# .env file contents
PROJECT_ENDPOINT=https://your-project.cognitiveservices.azure.com/
AZURE_OPENAI_ENDPOINT=https://your-openai.openai.azure.com/
EMBEDDING_MODEL_DEPLOYMENT_NAME=text-embedding-3-small
AZURE_CLIENT_ID=your-client-id
AZURE_CLIENT_SECRET=your-client-secret
AZURE_TENANT_ID=your-tenant-id
APPLICATIONINSIGHTS_CONNECTION_STRING=InstrumentationKey=your-key;...

# Database configuration (for development)
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
POSTGRES_DB=zava
POSTGRES_USER=postgres
POSTGRES_PASSWORD=your-secure-password
```

## 🐳 Docker環境セットアップ

### 1. Docker構成の理解

開発環境ではDocker Composeを使用します：

```yaml
# docker-compose.yml overview
version: '3.8'
services:
  postgres:
    image: pgvector/pgvector:pg17
    environment:
      POSTGRES_DB: zava
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: ${POSTGRES_PASSWORD:-secure_password}
    ports:
      - "5432:5432"
    volumes:
      - ./data:/backup_data:ro
      - ./docker-init:/docker-entrypoint-initdb.d:ro
    
  mcp_server:
    build: .
    depends_on:
      postgres:
        condition: service_healthy
    ports:
      - "8000:8000"
    env_file:
      - .env
```

### 2. 開発環境を起動

```bash
# Ensure you're in the project root directory
cd /path/to/MCP-Server-and-PostgreSQL-Sample-Retail

# Start the services
docker-compose up -d

# Check service status
docker-compose ps

# View logs
docker-compose logs -f
```

### 3. データベースセットアップの確認

```bash
# Connect to PostgreSQL container
docker-compose exec postgres psql -U postgres -d zava

# Check database structure
\dt retail.*

# Verify sample data
SELECT COUNT(*) FROM retail.stores;
SELECT COUNT(*) FROM retail.products;
SELECT COUNT(*) FROM retail.orders;

# Exit PostgreSQL
\q
```

### 4. MCPサーバーのテスト

```bash
# Check MCP server health
curl http://localhost:8000/health

# Test basic MCP endpoint
curl -X POST http://localhost:8000/mcp \
  -H "Content-Type: application/json" \
  -H "x-rls-user-id: 00000000-0000-0000-0000-000000000000" \
  -d '{"method": "tools/list", "params": {}}'
```

## 🔧 VS Codeの設定

### 1. MCP統合の設定

VS Code MCP設定を作成：

```json
// .vscode/mcp.json
{
    "servers": {
        "zava-sales-analysis-headoffice": {
            "url": "http://127.0.0.1:8000/mcp",
            "type": "http",
            "headers": {"x-rls-user-id": "00000000-0000-0000-0000-000000000000"}
        },
        "zava-sales-analysis-seattle": {
            "url": "http://127.0.0.1:8000/mcp",
            "type": "http",
            "headers": {"x-rls-user-id": "f47ac10b-58cc-4372-a567-0e02b2c3d479"}
        },
        "zava-sales-analysis-redmond": {
            "url": "http://127.0.0.1:8000/mcp",
            "type": "http",
            "headers": {"x-rls-user-id": "e7f8a9b0-c1d2-3e4f-5678-90abcdef1234"}
        }
    },
    "inputs": []
}
```

### 2. Python環境の設定

```json
// .vscode/settings.json
{
    "python.defaultInterpreterPath": "./mcp-env/bin/python",
    "python.linting.enabled": true,
    "python.linting.pylintEnabled": true,
    "python.formatting.provider": "black",
    "python.testing.pytestEnabled": true,
    "python.testing.pytestArgs": ["tests"],
    "files.exclude": {
        "**/__pycache__": true,
        "**/.pytest_cache": true,
        "**/mcp-env": true
    }
}
```

### 3. VS Code統合のテスト

1. **プロジェクトをVS Codeで開く**:
   ```bash
   code .
   ```

2. **AIチャットを開く**:
   - `Ctrl+Shift+P`（Windows/Linux）または`Cmd+Shift+P`（macOS）を押す
   - 「AI Chat」と入力し、「AI Chat: Open Chat」を選択

3. **MCPサーバー接続をテスト**:
   - AIチャットで`#zava`と入力し、設定済みのサーバーの1つを選択
   - 「データベースに利用可能なテーブルは何ですか？」と尋ねる
   - 小売データベースのテーブル一覧が返されるはずです

## ✅ 環境検証

### 1. システム全体のチェック

この検証スクリプトを実行してセットアップを確認：

```bash
# Create validation script
cat > validate_setup.py << 'EOF'
#!/usr/bin/env python3
"""
Environment validation script for MCP Server setup.
"""
import asyncio
import os
import sys
import subprocess
import requests
import asyncpg
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient

async def validate_environment():
    """Comprehensive environment validation."""
    results = {}
    
    # Check Python version
    python_version = sys.version_info
    results['python'] = {
        'status': 'pass' if python_version >= (3, 8) else 'fail',
        'version': f"{python_version.major}.{python_version.minor}.{python_version.micro}",
        'required': '3.8+'
    }
    
    # Check required packages
    required_packages = ['fastmcp', 'asyncpg', 'azure-ai-projects']
    for package in required_packages:
        try:
            __import__(package)
            results[f'package_{package}'] = {'status': 'pass'}
        except ImportError:
            results[f'package_{package}'] = {'status': 'fail', 'error': 'Not installed'}
    
    # Check Docker
    try:
        result = subprocess.run(['docker', '--version'], capture_output=True, text=True)
        results['docker'] = {
            'status': 'pass' if result.returncode == 0 else 'fail',
            'version': result.stdout.strip() if result.returncode == 0 else 'Not available'
        }
    except FileNotFoundError:
        results['docker'] = {'status': 'fail', 'error': 'Docker not found'}
    
    # Check Azure CLI
    try:
        result = subprocess.run(['az', '--version'], capture_output=True, text=True)
        results['azure_cli'] = {
            'status': 'pass' if result.returncode == 0 else 'fail',
            'version': result.stdout.split('\n')[0] if result.returncode == 0 else 'Not available'
        }
    except FileNotFoundError:
        results['azure_cli'] = {'status': 'fail', 'error': 'Azure CLI not found'}
    
    # Check environment variables
    required_env_vars = [
        'PROJECT_ENDPOINT',
        'AZURE_OPENAI_ENDPOINT',
        'EMBEDDING_MODEL_DEPLOYMENT_NAME',
        'AZURE_CLIENT_ID',
        'AZURE_CLIENT_SECRET',
        'AZURE_TENANT_ID'
    ]
    
    for var in required_env_vars:
        value = os.getenv(var)
        results[f'env_{var}'] = {
            'status': 'pass' if value else 'fail',
            'value': '***' if value and 'SECRET' in var else value
        }
    
    # Check database connection
    try:
        conn = await asyncpg.connect(
            host=os.getenv('POSTGRES_HOST', 'localhost'),
            port=int(os.getenv('POSTGRES_PORT', 5432)),
            database=os.getenv('POSTGRES_DB', 'zava'),
            user=os.getenv('POSTGRES_USER', 'postgres'),
            password=os.getenv('POSTGRES_PASSWORD', 'secure_password')
        )
        
        # Test query
        result = await conn.fetchval('SELECT COUNT(*) FROM retail.stores')
        await conn.close()
        
        results['database'] = {
            'status': 'pass',
            'store_count': result
        }
    except Exception as e:
        results['database'] = {
            'status': 'fail',
            'error': str(e)
        }
    
    # Check MCP server
    try:
        response = requests.get('http://localhost:8000/health', timeout=5)
        results['mcp_server'] = {
            'status': 'pass' if response.status_code == 200 else 'fail',
            'response': response.json() if response.status_code == 200 else response.text
        }
    except Exception as e:
        results['mcp_server'] = {
            'status': 'fail',
            'error': str(e)
        }
    
    # Check Azure AI service
    try:
        credential = DefaultAzureCredential()
        project_client = AIProjectClient(
            endpoint=os.getenv('PROJECT_ENDPOINT'),
            credential=credential
        )
        
        # This will fail if credentials are invalid
        results['azure_ai'] = {'status': 'pass'}
        
    except Exception as e:
        results['azure_ai'] = {
            'status': 'fail',
            'error': str(e)
        }
    
    return results

def print_results(results):
    """Print formatted validation results."""
    print("🔍 Environment Validation Results\n")
    print("=" * 50)
    
    passed = 0
    failed = 0
    
    for component, result in results.items():
        status = result.get('status', 'unknown')
        if status == 'pass':
            print(f"✅ {component}: PASS")
            passed += 1
        else:
            print(f"❌ {component}: FAIL")
            if 'error' in result:
                print(f"   Error: {result['error']}")
            failed += 1
    
    print("\n" + "=" * 50)
    print(f"Summary: {passed} passed, {failed} failed")
    
    if failed > 0:
        print("\n❗ Please fix the failed components before proceeding.")
        return False
    else:
        print("\n🎉 All validations passed! Your environment is ready.")
        return True

if __name__ == "__main__":
    asyncio.run(main())

async def main():
    results = await validate_environment()
    success = print_results(results)
    sys.exit(0 if success else 1)

EOF

# Run validation
python validate_setup.py
```

### 2. 手動検証チェックリスト

**✅ 基本ツール**
- [ ] Dockerバージョン20.10以上がインストールされ、実行中
- [ ] Azure CLI 2.40以上がインストールされ、認証済み
- [ ] Python 3.8以上とpipがインストール済み
- [ ] Git 2.30以上がインストール済み
- [ ] 必須拡張機能を備えたVS Code

**✅ Azureリソース**
- [ ] リソースグループが正常に作成された
- [ ] AI Foundryプロジェクトがデプロイされた
- [ ] OpenAIのtext-embedding-3-smallモデルがデプロイされた
- [ ] Application Insightsが設定された
- [ ] 適切な権限を持つサービスプリンシパルが作成された

**✅ 環境設定**
- [ ] `.env`ファイルが必要な変数を含んで作成された
- [ ] Azure認証情報が機能している（`az account show`でテスト）
- [ ] PostgreSQLコンテナが実行中でアクセス可能
- [ ] データベースにサンプルデータがロードされている

**✅ VS Code統合**
- [ ] `.vscode/mcp.json`が設定済み
- [ ] Pythonインタープリタが仮想環境に設定されている
- [ ] MCPサーバーがAIチャットに表示される
- [ ] AIチャットを通じてテストクエリを実行できる

## 🛠️ よくある問題のトラブルシューティング

### Dockerの問題

**問題**: Dockerコンテナが起動しない
```bash
# Check Docker service status
docker info

# Check available resources
docker system df

# Clean up if needed
docker system prune -f

# Restart Docker Desktop (Windows/macOS)
# Or restart Docker service (Linux)
sudo systemctl restart docker
```

**問題**: PostgreSQL接続が失敗する
```bash
# Check container logs
docker-compose logs postgres

# Verify container is healthy
docker-compose ps

# Test direct connection
docker-compose exec postgres psql -U postgres -d zava -c "SELECT 1;"
```

### Azureデプロイの問題

**問題**: Azureデプロイが失敗する
```bash
# Check Azure CLI authentication
az account show

# Verify subscription permissions
az role assignment list --assignee $(az account show --query user.name -o tsv)

# Check resource provider registration
az provider register --namespace Microsoft.CognitiveServices
az provider register --namespace Microsoft.Insights
```

**問題**: AIサービスの認証が失敗する
```bash
# Test service principal
az login --service-principal \
  --username $AZURE_CLIENT_ID \
  --password $AZURE_CLIENT_SECRET \
  --tenant $AZURE_TENANT_ID

# Verify AI service deployment
az cognitiveservices account list --query "[].{Name:name,Kind:kind,Location:location}"
```

### Python環境の問題

**問題**: パッケージのインストールが失敗する
```bash
# Upgrade pip and setuptools
python -m pip install --upgrade pip setuptools wheel

# Clear pip cache
pip cache purge

# Install packages one by one to identify issues
pip install fastmcp
pip install asyncpg
pip install azure-ai-projects
```

**問題**: VS CodeがPythonインタープリタを見つけられない
```bash
# Show Python interpreter paths
which python  # macOS/Linux
where python  # Windows

# Activate virtual environment first
source mcp-env/bin/activate  # macOS/Linux
mcp-env\Scripts\activate     # Windows

# Then open VS Code
code .
```

## 🎯 重要なポイント

このラボを完了すると、以下が達成されます：

✅ **完全な開発環境**: すべてのツールがインストールされ、設定済み  
✅ **Azureリソースのデプロイ**: AIサービスとサポートインフラストラクチャ  
✅ **Docker環境の稼働**: PostgreSQLとMCPサーバーのコンテナ  
✅ **VS Code統合**: MCPサーバーが設定され、アクセス可能  
✅ **セットアップの検証**: すべてのコンポーネントがテストされ、連携して動作  
✅ **トラブルシューティングの知識**: 一般的な問題とその解決策  

## 🚀 次のステップ

環境が整ったら、**[Lab 04: データベース設計とスキーマ](../04-Database/README.md)** に進んでください：

- 小売データベーススキーマを詳しく調べる
- マルチテナントデータモデリングを理解する
- 行レベルセキュリティの実装を学ぶ
- サンプル小売データを操作する

## 📚 追加リソース

### 開発ツール
- [Docker Documentation](https://docs.docker.com/) - Dockerの完全なリファレンス
- [Azure CLI Reference](https://docs.microsoft.com/cli/azure/) - Azure CLIコマンド
- [VS Code Documentation](https://code.visualstudio.com/docs) - エディタの設定と拡張機能

### Azureサービス
- [Azure AI Foundry Documentation](https://docs.microsoft.com/azure/ai-foundry/) - AIサービスの設定
- [Azure OpenAI Service](https://docs.microsoft.com/azure/cognitive-services/openai/) - AIモデルのデプロイ
- [Application Insights](https://docs.microsoft.com/azure/azure-monitor/app/app-insights-overview) - モニタリングのセットアップ

### Python開発
- [Python Virtual Environments](https://docs.python.org/3/tutorial/venv.html) - 環境管理
- [AsyncIO Documentation](https://docs.python.org/3/library/asyncio.html) - 非同期プログラミングパターン
- [FastAPI Documentation](https://fastapi.tiangolo.com/) - Webフレームワークのパターン

---

**次へ**: 環境が整いましたか？ [Lab 04: データベース設計とスキーマ](../04-Database/README.md) に進んでください

---

**免責事項**:  
この文書は、AI翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されています。正確性を追求しておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があることをご承知ください。元の言語で記載された文書が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。この翻訳の使用に起因する誤解や誤解釈について、当方は一切の責任を負いません。