# 環境セットアップ

## 🎯 このラボで扱う内容

このハンズオンラボでは、PostgreSQL統合によるMCPサーバー構築のための完全な開発環境のセットアップを案内します。必要なツールの設定、Azureリソースのデプロイ、実装前のセットアップ検証を行います。

## 概要

適切な開発環境は、MCPサーバー開発の成功に不可欠です。本ラボでは、Docker、Azureサービス、開発ツールのセットアップ手順と、それらが正しく連携して動作することの検証方法を段階的に説明します。

このラボを終了するころには、Zava Retail MCPサーバー開発に適した完全な開発環境が整っています。

## 学習目標

本ラボ終了時には、以下を達成できます。

- <strong>必要な開発ツールのインストールと設定</strong>
- **MCPサーバーに必要なAzureリソースのデプロイ**
- **PostgreSQLやMCPサーバー用Dockerコンテナの構築**
- <strong>テスト接続による環境セットアップの検証</strong>
- <strong>一般的なセットアップ問題や設定エラーのトラブルシューティング</strong>
- <strong>開発ワークフローとファイル構成の理解</strong>

## 📋 事前確認

開始前に、以下を確認してください。

### 必要な知識
- 基本的なコマンドライン操作（Windowsコマンドプロンプト/PowerShell）
- 環境変数の理解
- Gitバージョン管理に関する知識
- Dockerの基本概念（コンテナ、イメージ、ボリューム）

### システム要件
- **OS**：Windows 10/11、macOS、またはLinux
- **RAM**：最低8GB（推奨16GB）
- <strong>ストレージ</strong>：少なくとも10GBの空き容量
- <strong>ネットワーク</strong>：インターネット接続（ダウンロードおよびAzureデプロイ用）

### アカウント要件
- **Azureサブスクリプション**：無料プランで可
- **GitHubアカウント**：リポジトリアクセス用
- **Docker Hubアカウント**：（オプション）カスタムイメージ公開用

## 🛠️ ツールのインストール

### 1. Docker Desktopのインストール

Dockerは開発環境のコンテナ化を提供します。

#### Windowsインストール

1. **Docker Desktopのダウンロード**：
   ```cmd
   # Visit https://desktop.docker.com/win/stable/Docker%20Desktop%20Installer.exe
   # Or use Windows Package Manager
   winget install Docker.DockerDesktop
   ```

2. <strong>インストールと設定</strong>：
   - 管理者権限でインストーラーを実行
   - プロンプトでWSL 2連携を有効化
   - インストール完了後にPCを再起動

3. <strong>インストール確認</strong>：
   ```cmd
   docker --version
   docker-compose --version
   ```

#### macOSインストール

1. <strong>ダウンロードとインストール</strong>：
   ```bash
   # https://desktop.docker.com/mac/stable/Docker.dmg からダウンロードしてください
   # または Homebrew を使用してください
   brew install --cask docker
   ```

2. **Docker Desktopの起動**：
   - アプリケーションからDocker Desktopを起動
   - 初期セットアップウィザードを完了

3. <strong>インストール確認</strong>：
   ```bash
   docker --version
   docker-compose --version
   ```

#### Linuxインストール

1. **Docker Engineのインストール**：
   ```bash
   # Ubuntu/Debian
   curl -fsSL https://get.docker.com -o get-docker.sh
   sudo sh get-docker.sh
   sudo usermod -aG docker $USER
   
   # グループの変更を有効にするにはログアウトして再度ログインしてください
   ```

2. **Docker Composeのインストール**：
   ```bash
   sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
   sudo chmod +x /usr/local/bin/docker-compose
   ```

### 2. Azure CLIのインストール

Azureリソースのデプロイと管理に必要です。

#### Windowsインストール

```cmd
# Using Windows Package Manager
winget install Microsoft.AzureCLI

# Or download MSI from: https://aka.ms/installazurecliwindows
```

#### macOSインストール

```bash
# Homebrewを使用する
brew install azure-cli

# またはインストーラーを使用する
curl -L https://aka.ms/InstallAzureCli | bash
```

#### Linuxインストール

```bash
# Ubuntu/Debian
curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash

# RHEL/CentOS
sudo rpm --import https://packages.microsoft.com/keys/microsoft.asc
sudo dnf install azure-cli
```

#### インストール検証と認証

```bash
# インストールを確認してください
az version

# Azureにログインしてください
az login

# デフォルトのサブスクリプションを設定してください（複数ある場合）
az account list --output table
az account set --subscription "Your-Subscription-Name"
```

### 3. Gitのインストール

リポジトリのクローンやバージョン管理に必須です。

#### Windows

```cmd
# Using Windows Package Manager
winget install Git.Git

# Or download from: https://git-scm.com/download/win
```

#### macOS

```bash
# Gitは通常プリインストールされていますが、Homebrewを使って更新することもできます
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

Visual Studio CodeはMCPをサポートする統合開発環境です。

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
# コマンドライン経由でインストール
code --install-extension ms-python.python
code --install-extension ms-vscode.vscode-json
code --install-extension ms-azuretools.vscode-docker
code --install-extension ms-vscode.azure-account
```

またはVS Code内から：
1. VS Codeを開く
2. 拡張機能パネル（Ctrl+Shift+X）を開く
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
# Homebrewを使用する
brew install python@3.11
```

#### Linux

```bash
# Ubuntu/Debian
sudo apt update && sudo apt install python3.11 python3.11-pip python3.11-venv

# RHEL/CentOS
sudo dnf install python3.11 python3.11-pip
```

#### インストール確認

```bash
python --version  # Python 3.11.x を表示する必要があります
pip --version      # pip のバージョンを表示する必要があります
```

## 🚀 プロジェクトセットアップ

### 1. リポジトリのクローン

```bash
# メインリポジトリをクローンする
git clone https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail.git

# プロジェクトディレクトリに移動する
cd MCP-Server-and-PostgreSQL-Sample-Retail

# リポジトリの構造を確認する
ls -la
```

### 2. Python仮想環境の作成

```bash
# 仮想環境を作成する
python -m venv mcp-env

# 仮想環境を有効化する
# Windows
mcp-env\Scripts\activate

# macOS/Linux
source mcp-env/bin/activate

# pipをアップグレードする
python -m pip install --upgrade pip
```

### 3. Python依存パッケージのインストール

```bash
# 開発用依存関係をインストールする
pip install -r requirements.lock.txt

# 主要なパッケージを検証する
pip list | grep fastmcp
pip list | grep asyncpg
pip list | grep azure
```

## ☁️ Azureリソースのデプロイ

### 1. リソース要件の理解

MCPサーバーには以下のAzureリソースが必要です：

| <strong>リソース</strong> | <strong>用途</strong> | <strong>推定コスト</strong> |
|--------------|----------|----------------|
| **Microsoft Foundry** | AIモデルのホスティングと管理 | $10-50/月 |
| **OpenAIデプロイメント** | テキスト埋め込みモデル（text-embedding-3-small） | $5-20/月 |
| **Application Insights** | モニタリングおよびテレメトリ | $5-15/月 |
| <strong>リソースグループ</strong> | リソース整理 | 無料 |

### 2. Azureリソースのデプロイ

#### オプションA：自動デプロイ（推奨）

```bash
# インフラストラクチャディレクトリに移動する
cd infra

# Windows - PowerShell
./deploy.ps1

# macOS/Linux - Bash
./deploy.sh
```

デプロイスクリプトは以下を実行します：
1. 一意のリソースグループを作成
2. Microsoft Foundryリソースをデプロイ
3. text-embedding-3-smallモデルをデプロイ
4. Application Insightsの設定
5. 認証用サービスプリンシパルの作成
6. 設定を含む `.env` ファイルを生成

#### オプションB：手動デプロイ

自動スクリプトの失敗時や手動制御したい場合：

```bash
# 変数を設定する
RESOURCE_GROUP="rg-zava-mcp-$(date +%s)"
LOCATION="westus2"
AI_PROJECT_NAME="zava-ai-project"

# リソースグループを作成する
az group create --name $RESOURCE_GROUP --location $LOCATION

# メインテンプレートをデプロイする
az deployment group create \
  --resource-group $RESOURCE_GROUP \
  --template-file main.bicep \
  --parameters location=$LOCATION \
  --parameters resourcePrefix="zava-mcp"
```

### 3. Azureデプロイの確認

```bash
# リソースグループを確認する
az group show --name $RESOURCE_GROUP --output table

# 展開されたリソースを一覧表示する
az resource list --resource-group $RESOURCE_GROUP --output table

# AIサービスをテストする
az cognitiveservices account show \
  --name "your-ai-service-name" \
  --resource-group $RESOURCE_GROUP
```

### 4. 環境変数の設定

デプロイ後、`.env` ファイルが生成されているはずです。内容を確認してください：

```bash
# .envファイルの内容
PROJECT_ENDPOINT=https://your-project.cognitiveservices.azure.com/
AZURE_OPENAI_ENDPOINT=https://your-openai.openai.azure.com/
EMBEDDING_MODEL_DEPLOYMENT_NAME=text-embedding-3-small
AZURE_CLIENT_ID=your-client-id
AZURE_CLIENT_SECRET=your-client-secret
AZURE_TENANT_ID=your-tenant-id
APPLICATIONINSIGHTS_CONNECTION_STRING=InstrumentationKey=your-key;...

# データベース構成（開発用）
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
POSTGRES_DB=zava
POSTGRES_USER=postgres
POSTGRES_PASSWORD=your-secure-password
```

## 🐳 Docker環境構築

### 1. Docker Composeの理解

開発環境ではDocker Composeを使用しています：

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

### 2. 開発環境の起動

```bash
# プロジェクトのルートディレクトリにいることを確認してください
cd /path/to/MCP-Server-and-PostgreSQL-Sample-Retail

# サービスを起動する
docker-compose up -d

# サービスのステータスを確認する
docker-compose ps

# ログを表示する
docker-compose logs -f
```

### 3. データベース設定の確認

```bash
# PostgreSQLコンテナに接続する
docker-compose exec postgres psql -U postgres -d zava

# データベース構造を確認する
\dt retail.*

# サンプルデータを検証する
SELECT COUNT(*) FROM retail.stores;
SELECT COUNT(*) FROM retail.products;
SELECT COUNT(*) FROM retail.orders;

# PostgreSQLを終了する
\q
```

### 4. MCPサーバーテスト

```bash
# MCPサーバーの状態を確認する
curl http://localhost:8000/health

# 基本的なMCPエンドポイントをテストする
curl -X POST http://localhost:8000/mcp \
  -H "Content-Type: application/json" \
  -H "x-rls-user-id: 00000000-0000-0000-0000-000000000000" \
  -d '{"method": "tools/list", "params": {}}'
```

## 🔧 VS Code設定

### 1. MCPインテグレーションの設定

VS Code用MCP設定を作成：

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

1. **プロジェクトをVS Codeで開く**：
   ```bash
   code .
   ```

2. **AIチャットを開く**：
   - `Ctrl+Shift+P`（Windows/Linux）または `Cmd+Shift+P`（macOS）を押す
   - 「AI Chat」と入力し「AI Chat: Open Chat」を選択

3. **MCPサーバー接続テスト**：
   - AIチャットで `#zava` と入力し構成済みサーバーを選択
   - 質問：「データベースにはどんなテーブルがありますか？」
   - 小売データベースのテーブル一覧を含む応答を受信

## ✅ 環境検証

### 1. 総合システムチェック

セットアップを検証するスクリプトを実行：

```bash
# バリデーションスクリプトを作成する
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
    
    # Pythonのバージョンを確認する
    python_version = sys.version_info
    results['python'] = {
        'status': 'pass' if python_version >= (3, 8) else 'fail',
        'version': f"{python_version.major}.{python_version.minor}.{python_version.micro}",
        'required': '3.8+'
    }
    
    # 必要なパッケージを確認する
    required_packages = ['fastmcp', 'asyncpg', 'azure-ai-projects']
    for package in required_packages:
        try:
            __import__(package)
            results[f'package_{package}'] = {'status': 'pass'}
        except ImportError:
            results[f'package_{package}'] = {'status': 'fail', 'error': 'Not installed'}
    
    # Dockerを確認する
    try:
        result = subprocess.run(['docker', '--version'], capture_output=True, text=True)
        results['docker'] = {
            'status': 'pass' if result.returncode == 0 else 'fail',
            'version': result.stdout.strip() if result.returncode == 0 else 'Not available'
        }
    except FileNotFoundError:
        results['docker'] = {'status': 'fail', 'error': 'Docker not found'}
    
    # Azure CLIを確認する
    try:
        result = subprocess.run(['az', '--version'], capture_output=True, text=True)
        results['azure_cli'] = {
            'status': 'pass' if result.returncode == 0 else 'fail',
            'version': result.stdout.split('\n')[0] if result.returncode == 0 else 'Not available'
        }
    except FileNotFoundError:
        results['azure_cli'] = {'status': 'fail', 'error': 'Azure CLI not found'}
    
    # 環境変数を確認する
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
    
    # データベース接続を確認する
    try:
        conn = await asyncpg.connect(
            host=os.getenv('POSTGRES_HOST', 'localhost'),
            port=int(os.getenv('POSTGRES_PORT', 5432)),
            database=os.getenv('POSTGRES_DB', 'zava'),
            user=os.getenv('POSTGRES_USER', 'postgres'),
            password=os.getenv('POSTGRES_PASSWORD', 'secure_password')
        )
        
        # クエリをテストする
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
    
    # MCPサーバーを確認する
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
    
    # Azure AIサービスを確認する
    try:
        credential = DefaultAzureCredential()
        project_client = AIProjectClient(
            endpoint=os.getenv('PROJECT_ENDPOINT'),
            credential=credential
        )
        
        # 認証情報が無効な場合、ここでエラーになります
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

# バリデーションを実行する
python validate_setup.py
```

### 2. 手動検証チェックリスト

**✅ 基本ツール**
- [ ] Docker 20.10+ がインストール・稼働している
- [ ] Azure CLI 2.40+ がインストール・認証済み
- [ ] Python 3.8+ と pip がインストール済み
- [ ] Git 2.30+ がインストール済み
- [ ] VS Code と必須拡張機能が揃っている

**✅ Azureリソース**
- [ ] リソースグループが作成済み
- [ ] AI Foundryプロジェクトがデプロイ済み
- [ ] OpenAI text-embedding-3-smallモデルがデプロイ済み
- [ ] Application Insightsが設定済み
- [ ] 適切権限のサービスプリンシパルが作成済み

**✅ 環境設定**
- [ ] `.env` ファイルが必須変数含め作成済み
- [ ] Azure認証情報が有効（`az account show`でテスト）
- [ ] PostgreSQLコンテナが稼働中でアクセス可能
- [ ] サンプルデータがデータベースにロード済み

**✅ VS Code統合**
- [ ] `.vscode/mcp.json`が設定済み
- [ ] Pythonインタープリターが仮想環境を使用
- [ ] MCPサーバーがAIチャットに表示されている
- [ ] AIチャットでテストクエリが実行可能

## 🛠️ よくある問題のトラブルシューティング

### Dockerの問題

<strong>問題</strong>：Dockerコンテナが起動しない
```bash
# Dockerサービスの状態を確認する
docker info

# 利用可能なリソースを確認する
docker system df

# 必要に応じてクリーンアップする
docker system prune -f

# Docker Desktop（Windows/macOS）を再起動する
# またはDockerサービス（Linux）を再起動する
sudo systemctl restart docker
```

<strong>問題</strong>：PostgreSQL接続失敗
```bash
# コンテナのログを確認する
docker-compose logs postgres

# コンテナが正常であることを確認する
docker-compose ps

# 直接接続をテストする
docker-compose exec postgres psql -U postgres -d zava -c "SELECT 1;"
```

### Azureデプロイの問題

<strong>問題</strong>：Azureデプロイに失敗する
```bash
# Azure CLI の認証を確認する
az account show

# サブスクリプションの権限を検証する
az role assignment list --assignee $(az account show --query user.name -o tsv)

# リソースプロバイダーの登録を確認する
az provider register --namespace Microsoft.CognitiveServices
az provider register --namespace Microsoft.Insights
```

<strong>問題</strong>：AIサービス認証失敗
```bash
# サービスプリンシパルのテスト
az login --service-principal \
  --username $AZURE_CLIENT_ID \
  --password $AZURE_CLIENT_SECRET \
  --tenant $AZURE_TENANT_ID

# AIサービスの展開を検証する
az cognitiveservices account list --query "[].{Name:name,Kind:kind,Location:location}"
```

### Python環境の問題

<strong>問題</strong>：パッケージインストール失敗
```bash
# pip と setuptools をアップグレードする
python -m pip install --upgrade pip setuptools wheel

# pip のキャッシュをクリアする
pip cache purge

# 問題を特定するためにパッケージを一つずつインストールする
pip install fastmcp
pip install asyncpg
pip install azure-ai-projects
```

<strong>問題</strong>：VS CodeがPythonインタープリターを認識しない
```bash
# Pythonインタープリターのパスを表示
which python  # macOS/Linux
where python  # Windows

# まず仮想環境を有効化する
source mcp-env/bin/activate  # macOS/Linux
mcp-env\Scripts\activate     # Windows

# その後VS Codeを開く
code .
```

## 🎯 重要ポイントまとめ

本ラボ完了後、以下を持つことができます：

✅ <strong>完全な開発環境</strong>：すべてのツールがインストール・設定済み  
✅ **Azureリソースのデプロイ完了**：AIサービスおよび関連インフラ  
✅ **Docker環境稼働中**：PostgreSQLおよびMCPサーバーコンテナ  
✅ **VS Code統合**：MCPサーバー設定済みでアクセス可能  
✅ <strong>設定検証済み</strong>：全コンポーネントの動作確認済み  
✅ <strong>トラブルシューティング知識</strong>：一般的な問題と解決法の把握  

## 🚀 次のステップ

環境が整ったら、**[ラボ04: データベース設計とスキーマ](../04-Database/README.md)** に進み：

- 小売データベースのスキーマを詳細に学ぶ
- マルチテナントデータモデリングの理解
- 行レベルセキュリティ（RLS）実装の学習
- 小売サンプルデータの利用

## 📚 追加リソース

### 開発ツール
- [Docker Documentation](https://docs.docker.com/) - Dockerの完全なリファレンス
- [Azure CLI Reference](https://docs.microsoft.com/cli/azure/) - Azure CLIコマンド集
- [VS Code Documentation](https://code.visualstudio.com/docs) - エディター設定と拡張機能

### Azureサービス
- [Microsoft Foundry Documentation](https://docs.microsoft.com/azure/ai-foundry/) - AIサービス設定
- [Azure OpenAI Service](https://docs.microsoft.com/azure/cognitive-services/openai/) - AIモデルのデプロイ
- [Application Insights](https://docs.microsoft.com/azure/azure-monitor/app/app-insights-overview) - モニタリング設定

### Python開発
- [Python Virtual Environments](https://docs.python.org/3/tutorial/venv.html) - 環境管理
- [AsyncIO Documentation](https://docs.python.org/3/library/asyncio.html) - 非同期プログラミングパターン
- [FastAPI Documentation](https://fastapi.tiangolo.com/) - Webフレームワークパターン

---

<strong>次へ</strong>：環境準備ができたら [ラボ04: データベース設計とスキーマ](../04-Database/README.md) に進んでください。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責事項**：
本書類は AI 翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されています。正確性を期していますが、自動翻訳には誤りや不正確な部分が含まれる可能性があることをご承知おきください。原文の原語版が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用により生じたいかなる誤解や解釈違いについても、当方は責任を負いかねます。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
