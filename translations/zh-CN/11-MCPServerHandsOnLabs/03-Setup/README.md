# 环境设置

## 🎯 本实验内容

本动手实验将指导您设置一个完整的开发环境，用于构建与PostgreSQL集成的MCP服务器。您将配置所有必要的工具，部署Azure资源，并在实施之前验证您的设置。

## 概述

一个适当的开发环境对于成功开发MCP服务器至关重要。本实验提供了逐步指导，帮助您设置Docker、Azure服务、开发工具，并验证所有组件是否正确协同工作。

完成本实验后，您将拥有一个完全功能化的开发环境，准备好构建Zava Retail MCP服务器。

## 学习目标

完成本实验后，您将能够：

- **安装和配置**所有必需的开发工具
- **部署Azure资源**以支持MCP服务器
- **设置Docker容器**用于PostgreSQL和MCP服务器
- **验证**您的环境设置是否通过测试连接
- **排查**常见的设置问题和配置问题
- **理解**开发工作流程和文件结构

## 📋 前置条件检查

在开始之前，请确保您具备以下条件：

### 必需知识
- 基本命令行使用（Windows命令提示符/PowerShell）
- 环境变量的基本理解
- 熟悉Git版本控制
- 基本Docker概念（容器、镜像、卷）

### 系统要求
- **操作系统**：Windows 10/11、macOS或Linux
- **内存**：最低8GB（推荐16GB）
- **存储**：至少10GB可用空间
- **网络**：用于下载和Azure部署的互联网连接

### 账户要求
- **Azure订阅**：免费层即可满足需求
- **GitHub账户**：用于访问代码库
- **Docker Hub账户**：（可选）用于发布自定义镜像

## 🛠️ 工具安装

### 1. 安装Docker Desktop

Docker提供了容器化的开发环境。

#### Windows安装

1. **下载Docker Desktop**：
   ```cmd
   # Visit https://desktop.docker.com/win/stable/Docker%20Desktop%20Installer.exe
   # Or use Windows Package Manager
   winget install Docker.DockerDesktop
   ```

2. **安装和配置**：
   - 以管理员身份运行安装程序
   - 在提示时启用WSL 2集成
   - 安装完成后重启计算机

3. **验证安装**：
   ```cmd
   docker --version
   docker-compose --version
   ```

#### macOS安装

1. **下载并安装**：
   ```bash
   # Download from https://desktop.docker.com/mac/stable/Docker.dmg
   # Or use Homebrew
   brew install --cask docker
   ```

2. **启动Docker Desktop**：
   - 从应用程序中启动Docker Desktop
   - 完成初始设置向导

3. **验证安装**：
   ```bash
   docker --version
   docker-compose --version
   ```

#### Linux安装

1. **安装Docker Engine**：
   ```bash
   # Ubuntu/Debian
   curl -fsSL https://get.docker.com -o get-docker.sh
   sudo sh get-docker.sh
   sudo usermod -aG docker $USER
   
   # Log out and back in for group changes to take effect
   ```

2. **安装Docker Compose**：
   ```bash
   sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
   sudo chmod +x /usr/local/bin/docker-compose
   ```

### 2. 安装Azure CLI

Azure CLI用于部署和管理Azure资源。

#### Windows安装

```cmd
# Using Windows Package Manager
winget install Microsoft.AzureCLI

# Or download MSI from: https://aka.ms/installazurecliwindows
```

#### macOS安装

```bash
# Using Homebrew
brew install azure-cli

# Or using installer
curl -L https://aka.ms/InstallAzureCli | bash
```

#### Linux安装

```bash
# Ubuntu/Debian
curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash

# RHEL/CentOS
sudo rpm --import https://packages.microsoft.com/keys/microsoft.asc
sudo dnf install azure-cli
```

#### 验证和认证

```bash
# Check installation
az version

# Login to Azure
az login

# Set default subscription (if you have multiple)
az account list --output table
az account set --subscription "Your-Subscription-Name"
```

### 3. 安装Git

Git是用于克隆代码库和版本控制的必需工具。

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

### 4. 安装VS Code

Visual Studio Code提供了支持MCP开发的集成开发环境。

#### 安装

```cmd
# Windows
winget install Microsoft.VisualStudioCode

# macOS
brew install --cask visual-studio-code

# Linux (Ubuntu/Debian)
sudo snap install code --classic
```

#### 必需扩展

安装以下VS Code扩展：

```bash
# Install via command line
code --install-extension ms-python.python
code --install-extension ms-vscode.vscode-json
code --install-extension ms-azuretools.vscode-docker
code --install-extension ms-vscode.azure-account
```

或者通过VS Code安装：
1. 打开VS Code
2. 转到扩展（Ctrl+Shift+X）
3. 安装：
   - **Python**（Microsoft）
   - **Docker**（Microsoft）
   - **Azure Account**（Microsoft）
   - **JSON**（Microsoft）

### 5. 安装Python

MCP服务器开发需要Python 3.8及以上版本。

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

#### 验证安装

```bash
python --version  # Should show Python 3.11.x
pip --version      # Should show pip version
```

## 🚀 项目设置

### 1. 克隆代码库

```bash
# Clone the main repository
git clone https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail.git

# Navigate to the project directory
cd MCP-Server-and-PostgreSQL-Sample-Retail

# Verify repository structure
ls -la
```

### 2. 创建Python虚拟环境

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

### 3. 安装Python依赖项

```bash
# Install development dependencies
pip install -r requirements.lock.txt

# Verify key packages
pip list | grep fastmcp
pip list | grep asyncpg
pip list | grep azure
```

## ☁️ Azure资源部署

### 1. 了解资源需求

我们的MCP服务器需要以下Azure资源：

| **资源** | **用途** | **预计成本** |
|----------|----------|-------------|
| **Azure AI Foundry** | AI模型托管和管理 | $10-50/月 |
| **OpenAI部署** | 文本嵌入模型（text-embedding-3-small） | $5-20/月 |
| **Application Insights** | 监控和遥测 | $5-15/月 |
| **资源组** | 资源组织 | 免费 |

### 2. 部署Azure资源

#### 选项A：自动化部署（推荐）

```bash
# Navigate to infrastructure directory
cd infra

# Windows - PowerShell
./deploy.ps1

# macOS/Linux - Bash
./deploy.sh
```

部署脚本将：
1. 创建一个唯一的资源组
2. 部署Azure AI Foundry资源
3. 部署text-embedding-3-small模型
4. 配置Application Insights
5. 创建用于认证的服务主体
6. 生成包含配置的`.env`文件

#### 选项B：手动部署

如果您更喜欢手动控制或自动脚本失败：

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

### 3. 验证Azure部署

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

### 4. 配置环境变量

部署完成后，您应该有一个`.env`文件。验证其内容是否包含：

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

## 🐳 Docker环境设置

### 1. 了解Docker组成

我们的开发环境使用Docker Compose：

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

### 2. 启动开发环境

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

### 3. 验证数据库设置

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

### 4. 测试MCP服务器

```bash
# Check MCP server health
curl http://localhost:8000/health

# Test basic MCP endpoint
curl -X POST http://localhost:8000/mcp \
  -H "Content-Type: application/json" \
  -H "x-rls-user-id: 00000000-0000-0000-0000-000000000000" \
  -d '{"method": "tools/list", "params": {}}'
```

## 🔧 VS Code配置

### 1. 配置MCP集成

创建VS Code MCP配置：

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

### 2. 配置Python环境

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

### 3. 测试VS Code集成

1. **在VS Code中打开项目**：
   ```bash
   code .
   ```

2. **打开AI聊天**：
   - 按`Ctrl+Shift+P`（Windows/Linux）或`Cmd+Shift+P`（macOS）
   - 输入"AI Chat"，选择"AI Chat: Open Chat"

3. **测试MCP服务器连接**：
   - 在AI聊天中输入`#zava`并选择一个配置的服务器
   - 提问："数据库中有哪些表？"
   - 您应该收到一个列出零售数据库表的响应

## ✅ 环境验证

### 1. 综合系统检查

运行此验证脚本以检查您的设置：

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

### 2. 手动验证清单

**✅ 基本工具**
- [ ] Docker版本20.10+已安装并运行
- [ ] Azure CLI 2.40+已安装并认证
- [ ] Python 3.8+已安装并带有pip
- [ ] Git 2.30+已安装
- [ ] VS Code已安装所需扩展

**✅ Azure资源**
- [ ] 成功创建资源组
- [ ] 部署了AI Foundry项目
- [ ] 部署了OpenAI text-embedding-3-small模型
- [ ] 配置了Application Insights
- [ ] 创建了具有适当权限的服务主体

**✅ 环境配置**
- [ ] `.env`文件已创建并包含所有必需变量
- [ ] Azure凭据正常工作（使用`az account show`测试）
- [ ] PostgreSQL容器正在运行并可访问
- [ ] 数据库中已加载示例数据

**✅ VS Code集成**
- [ ] `.vscode/mcp.json`已配置
- [ ] Python解释器设置为虚拟环境
- [ ] MCP服务器在AI聊天中显示
- [ ] 可以通过AI聊天执行测试查询

## 🛠️ 常见问题排查

### Docker问题

**问题**：Docker容器无法启动  
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

**问题**：PostgreSQL连接失败  
```bash
# Check container logs
docker-compose logs postgres

# Verify container is healthy
docker-compose ps

# Test direct connection
docker-compose exec postgres psql -U postgres -d zava -c "SELECT 1;"
```

### Azure部署问题

**问题**：Azure部署失败  
```bash
# Check Azure CLI authentication
az account show

# Verify subscription permissions
az role assignment list --assignee $(az account show --query user.name -o tsv)

# Check resource provider registration
az provider register --namespace Microsoft.CognitiveServices
az provider register --namespace Microsoft.Insights
```

**问题**：AI服务认证失败  
```bash
# Test service principal
az login --service-principal \
  --username $AZURE_CLIENT_ID \
  --password $AZURE_CLIENT_SECRET \
  --tenant $AZURE_TENANT_ID

# Verify AI service deployment
az cognitiveservices account list --query "[].{Name:name,Kind:kind,Location:location}"
```

### Python环境问题

**问题**：包安装失败  
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

**问题**：VS Code找不到Python解释器  
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

## 🎯 关键收获

完成本实验后，您应该具备：

✅ **完整的开发环境**：所有工具已安装并配置  
✅ **已部署的Azure资源**：AI服务和支持基础设施  
✅ **运行中的Docker环境**：PostgreSQL和MCP服务器容器  
✅ **VS Code集成**：MCP服务器已配置并可访问  
✅ **验证的设置**：所有组件已测试并协同工作  
✅ **问题排查知识**：常见问题及解决方案  

## 🚀 下一步

环境准备好后，请继续**[实验04：数据库设计和架构](../04-Database/README.md)**以：

- 详细探索零售数据库架构
- 了解多租户数据建模
- 学习行级安全性实现
- 使用零售数据样本进行操作

## 📚 额外资源

### 开发工具
- [Docker文档](https://docs.docker.com/) - 完整的Docker参考
- [Azure CLI参考](https://docs.microsoft.com/cli/azure/) - Azure CLI命令
- [VS Code文档](https://code.visualstudio.com/docs) - 编辑器配置和扩展

### Azure服务
- [Azure AI Foundry文档](https://docs.microsoft.com/azure/ai-foundry/) - AI服务配置
- [Azure OpenAI服务](https://docs.microsoft.com/azure/cognitive-services/openai/) - AI模型部署
- [Application Insights](https://docs.microsoft.com/azure/azure-monitor/app/app-insights-overview) - 监控设置

### Python开发
- [Python虚拟环境](https://docs.python.org/3/tutorial/venv.html) - 环境管理
- [AsyncIO文档](https://docs.python.org/3/library/asyncio.html) - 异步编程模式
- [FastAPI文档](https://fastapi.tiangolo.com/) - Web框架模式

---

**下一步**：环境准备好了吗？继续学习[实验04：数据库设计和架构](../04-Database/README.md)

---

**免责声明**：  
本文档使用AI翻译服务[Co-op Translator](https://github.com/Azure/co-op-translator)进行翻译。尽管我们努力确保准确性，但请注意，自动翻译可能包含错误或不准确之处。应以原始语言的文档作为权威来源。对于关键信息，建议使用专业人工翻译。我们对因使用本翻译而引起的任何误解或误读不承担责任。