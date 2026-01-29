# ပတ်ဝန်းကျင် Setup

## 🎯 ဒီ Lab မှာ ဘာတွေ ပါဝင်မလဲ

ဒီလက်တွေ့လုပ်ငန်းခန်းမှာ MCP server တွေကို PostgreSQL နဲ့ ပေါင်းစပ်ဖန်တီးဖို့အတွက် တစ်ခုလုံးသော development ပတ်ဝန်းကျင်ကို စနစ်တကျ setup လုပ်ပေးမှာဖြစ်ပါတယ်။ လိုအပ်တဲ့ tools တွေကို configure လုပ်ပြီး Azure resources တွေကို deploy လုပ်ကာ setup ကို အကောင်အထည်ဖော်မည့်အခါ အဆင်ပြေမပြေ စစ်ဆေးပေးပါမည်။

## အကျဉ်းချုပ်

MCP server ကို အောင်မြင်စွာ ဖန်တီးဖို့အတွက် သင့်တော်တဲ့ development ပတ်ဝန်းကျင်တစ်ခုလိုအပ်ပါတယ်။ ဒီ lab မှာ Docker, Azure services, development tools တွေကို စနစ်တကျ setup လုပ်ပေးပြီး အားလုံးကို အတူတူအလုပ်လုပ်နိုင်အောင် စစ်ဆေးပေးပါမည်။

ဒီ lab ကိုပြီးဆုံးတဲ့အခါမှာ Zava Retail MCP server ကို ဖန်တီးဖို့အတွက် အပြည့်အစုံသော development ပတ်ဝန်းကျင်တစ်ခုကို ရရှိထားမည်ဖြစ်သည်။

## သင်ယူရမည့် ရည်မှန်းချက်များ

ဒီ lab ကိုပြီးဆုံးတဲ့အခါမှာ သင်သည်:

- **လိုအပ်သော development tools တွေကို** တပ်ဆင်ပြီး configure လုပ်နိုင်မည်
- **MCP server အတွက် Azure resources တွေကို** deploy လုပ်နိုင်မည်
- **PostgreSQL နဲ့ MCP server အတွက် Docker containers တွေကို** setup လုပ်နိုင်မည်
- **သင့် setup ကို** test connections တွေဖြင့် validate လုပ်နိုင်မည်
- **Setup အခက်အခဲများနဲ့ configuration ပြဿနာများကို** ဖြေရှင်းနိုင်မည်
- **Development workflow နဲ့ file structure ကို** နားလည်နိုင်မည်

## 📋 လိုအပ်ချက်များ စစ်ဆေးခြင်း

စတင်မည့်အခါမှာ သင်မှာ အောက်ပါအရာများရှိကြောင်း သေချာစစ်ဆေးပါ:

### လိုအပ်သော အသိပညာ
- Command line ကို အခြေခံအသုံးပြုနိုင်မှု (Windows Command Prompt/PowerShell)
- Environment variables ကို နားလည်မှု
- Git version control ကို အသုံးပြုနိုင်မှု
- Docker အခြေခံအကြောင်း (containers, images, volumes)

### System Requirements
- **Operating System**: Windows 10/11, macOS, or Linux
- **RAM**: အနည်းဆုံး 8GB (16GB အကြံပြုသည်)
- **Storage**: အနည်းဆုံး 10GB အခမဲ့နေရာ
- **Network**: Downloads နဲ့ Azure deployment အတွက် အင်တာနက်ချိတ်ဆက်မှု

### Account Requirements
- **Azure Subscription**: အခမဲ့ tier လုံလောက်သည်
- **GitHub Account**: Repository access အတွက်
- **Docker Hub Account**: (Optional) Custom image publishing အတွက်

## 🛠️ Tool Installation

### 1. Docker Desktop ကို တပ်ဆင်ပါ

Docker သည် development setup အတွက် containerized ပတ်ဝန်းကျင်ကို ပေးသည်။

#### Windows Installation

1. **Docker Desktop ကို Download လုပ်ပါ**:
   ```cmd
   # Visit https://desktop.docker.com/win/stable/Docker%20Desktop%20Installer.exe
   # Or use Windows Package Manager
   winget install Docker.DockerDesktop
   ```

2. **Install နဲ့ Configure လုပ်ပါ**:
   - Installer ကို Administrator အနေနဲ့ run လုပ်ပါ
   - WSL 2 integration ကို enable လုပ်ပါ
   - Installation ပြီးဆုံးတဲ့အခါ computer ကို restart လုပ်ပါ

3. **Installation ကို Verify လုပ်ပါ**:
   ```cmd
   docker --version
   docker-compose --version
   ```

#### macOS Installation

1. **Download နဲ့ Install လုပ်ပါ**:
   ```bash
   # Download from https://desktop.docker.com/mac/stable/Docker.dmg
   # Or use Homebrew
   brew install --cask docker
   ```

2. **Docker Desktop ကို Start လုပ်ပါ**:
   - Applications မှာ Docker Desktop ကို launch လုပ်ပါ
   - Initial setup wizard ကို ပြီးဆုံးပါ

3. **Installation ကို Verify လုပ်ပါ**:
   ```bash
   docker --version
   docker-compose --version
   ```

#### Linux Installation

1. **Docker Engine ကို Install လုပ်ပါ**:
   ```bash
   # Ubuntu/Debian
   curl -fsSL https://get.docker.com -o get-docker.sh
   sudo sh get-docker.sh
   sudo usermod -aG docker $USER
   
   # Log out and back in for group changes to take effect
   ```

2. **Docker Compose ကို Install လုပ်ပါ**:
   ```bash
   sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
   sudo chmod +x /usr/local/bin/docker-compose
   ```

### 2. Azure CLI ကို Install လုပ်ပါ

Azure CLI သည် Azure resource deployment နဲ့ management ကို enable လုပ်ပေးသည်။

#### Windows Installation

```cmd
# Using Windows Package Manager
winget install Microsoft.AzureCLI

# Or download MSI from: https://aka.ms/installazurecliwindows
```

#### macOS Installation

```bash
# Using Homebrew
brew install azure-cli

# Or using installer
curl -L https://aka.ms/InstallAzureCli | bash
```

#### Linux Installation

```bash
# Ubuntu/Debian
curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash

# RHEL/CentOS
sudo rpm --import https://packages.microsoft.com/keys/microsoft.asc
sudo dnf install azure-cli
```

#### Verify နဲ့ Authenticate လုပ်ပါ

```bash
# Check installation
az version

# Login to Azure
az login

# Set default subscription (if you have multiple)
az account list --output table
az account set --subscription "Your-Subscription-Name"
```

### 3. Git ကို Install လုပ်ပါ

Git သည် repository ကို clone လုပ်ရန်နဲ့ version control အတွက်လိုအပ်သည်။

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

### 4. VS Code ကို Install လုပ်ပါ

Visual Studio Code သည် MCP ကို support လုပ်တဲ့ integrated development environment ကို ပေးသည်။

#### Installation

```cmd
# Windows
winget install Microsoft.VisualStudioCode

# macOS
brew install --cask visual-studio-code

# Linux (Ubuntu/Debian)
sudo snap install code --classic
```

#### Required Extensions

VS Code extensions အောက်ပါများကို install လုပ်ပါ:

```bash
# Install via command line
code --install-extension ms-python.python
code --install-extension ms-vscode.vscode-json
code --install-extension ms-azuretools.vscode-docker
code --install-extension ms-vscode.azure-account
```

သို့မဟုတ် VS Code မှတဆင့် install လုပ်ပါ:
1. VS Code ကို ဖွင့်ပါ
2. Extensions (Ctrl+Shift+X) ကို သွားပါ
3. Install လုပ်ပါ:
   - **Python** (Microsoft)
   - **Docker** (Microsoft)
   - **Azure Account** (Microsoft)
   - **JSON** (Microsoft)

### 5. Python ကို Install လုပ်ပါ

Python 3.8+ သည် MCP server development အတွက်လိုအပ်သည်။

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

#### Installation ကို Verify လုပ်ပါ

```bash
python --version  # Should show Python 3.11.x
pip --version      # Should show pip version
```

## 🚀 Project Setup

### 1. Repository ကို Clone လုပ်ပါ

```bash
# Clone the main repository
git clone https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail.git

# Navigate to the project directory
cd MCP-Server-and-PostgreSQL-Sample-Retail

# Verify repository structure
ls -la
```

### 2. Python Virtual Environment ကို ဖန်တီးပါ

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

### 3. Python Dependencies တွေကို Install လုပ်ပါ

```bash
# Install development dependencies
pip install -r requirements.lock.txt

# Verify key packages
pip list | grep fastmcp
pip list | grep asyncpg
pip list | grep azure
```

## ☁️ Azure Resource Deployment

### 1. Resource Requirements ကို နားလည်ပါ

MCP server အတွက် အောက်ပါ Azure resources များလိုအပ်သည်:

| **Resource** | **Purpose** | **Estimated Cost** |
|--------------|-------------|-------------------|
| **Azure AI Foundry** | AI model hosting နဲ့ management | $10-50/month |
| **OpenAI Deployment** | Text embedding model (text-embedding-3-small) | $5-20/month |
| **Application Insights** | Monitoring နဲ့ telemetry | $5-15/month |
| **Resource Group** | Resource organization | Free |

### 2. Azure Resources ကို Deploy လုပ်ပါ

#### Option A: Automated Deployment (အကြံပြုသည်)

```bash
# Navigate to infrastructure directory
cd infra

# Windows - PowerShell
./deploy.ps1

# macOS/Linux - Bash
./deploy.sh
```

Deployment script သည် အောက်ပါအရာများကိုလုပ်ဆောင်မည်:
1. Resource group တစ်ခုကို ဖန်တီးမည်
2. Azure AI Foundry resources တွေကို deploy လုပ်မည်
3. Text-embedding-3-small model ကို deploy လုပ်မည်
4. Application Insights ကို configure လုပ်မည်
5. Authentication အတွက် service principal ကို ဖန်တီးမည်
6. Configuration ပါဝင်တဲ့ `.env` file ကို ဖန်တီးမည်

#### Option B: Manual Deployment

Automated script မအောင်မြင်ပါက သို့မဟုတ် manual control ကို သင်နှစ်သက်ပါက:

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

### 3. Azure Deployment ကို Verify လုပ်ပါ

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

### 4. Environment Variables ကို Configure လုပ်ပါ

Deployment ပြီးဆုံးတဲ့အခါ `.env` file ရှိရမည်။ အဲဒီမှာ အောက်ပါအရာများပါဝင်ကြောင်း Verify လုပ်ပါ:

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

## 🐳 Docker Environment Setup

### 1. Docker Composition ကို နားလည်ပါ

Development ပတ်ဝန်းကျင်သည် Docker Compose ကို အသုံးပြုသည်:

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

### 2. Development Environment ကို Start လုပ်ပါ

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

### 3. Database Setup ကို Verify လုပ်ပါ

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

### 4. MCP Server ကို Test လုပ်ပါ

```bash
# Check MCP server health
curl http://localhost:8000/health

# Test basic MCP endpoint
curl -X POST http://localhost:8000/mcp \
  -H "Content-Type: application/json" \
  -H "x-rls-user-id: 00000000-0000-0000-0000-000000000000" \
  -d '{"method": "tools/list", "params": {}}'
```

## 🔧 VS Code Configuration

### 1. MCP Integration ကို Configure လုပ်ပါ

VS Code MCP configuration ကို ဖန်တီးပါ:

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

### 2. Python Environment ကို Configure လုပ်ပါ

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

### 3. VS Code Integration ကို Test လုပ်ပါ

1. **Project ကို VS Code မှာ ဖွင့်ပါ**:
   ```bash
   code .
   ```

2. **AI Chat ကို ဖွင့်ပါ**:
   - `Ctrl+Shift+P` (Windows/Linux) သို့မဟုတ် `Cmd+Shift+P` (macOS) ကို နှိပ်ပါ
   - "AI Chat" ဟု ရိုက်ထည့်ပြီး "AI Chat: Open Chat" ကို ရွေးပါ

3. **MCP Server Connection ကို Test လုပ်ပါ**:
   - AI Chat မှာ `#zava` ဟု ရိုက်ထည့်ပြီး configure လုပ်ထားသော servers တစ်ခုကို ရွေးပါ
   - "What tables are available in the database?" ဟု မေးပါ
   - Retail database tables များကို ပြန်လည်ရရှိရမည်

## ✅ Environment Validation

### 1. Comprehensive System Check

Setup ကို Verify လုပ်ရန် validation script ကို run လုပ်ပါ:

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

### 2. Manual Validation Checklist

**✅ Basic Tools**
- [ ] Docker version 20.10+ install လုပ်ပြီး run ဖြစ်နေသည်
- [ ] Azure CLI 2.40+ install လုပ်ပြီး authenticated ဖြစ်သည်
- [ ] Python 3.8+ pip နဲ့အတူ install လုပ်ထားသည်
- [ ] Git 2.30+ install လုပ်ထားသည်
- [ ] VS Code နဲ့လိုအပ်သော extensions install လုပ်ထားသည်

**✅ Azure Resources**
- [ ] Resource group ကို အောင်မြင်စွာ ဖန်တီးထားသည်
- [ ] AI Foundry project ကို deploy လုပ်ထားသည်
- [ ] OpenAI text-embedding-3-small model ကို deploy လုပ်ထားသည်
- [ ] Application Insights ကို configure လုပ်ထားသည်
- [ ] Service principal ကို လိုအပ်သော permissions နဲ့ ဖန်တီးထားသည်

**✅ Environment Configuration**
- [ ] `.env` file ကို ဖန်တီးပြီးလိုအပ်သော variables အားလုံးပါဝင်သည်
- [ ] Azure credentials အလုပ်လုပ်နေသည် (e.g., `az account show` ကို test လုပ်ပါ)
- [ ] PostgreSQL container run ဖြစ်နေပြီး access လုပ်နိုင်သည်
- [ ] Database မှာ sample data ကို load လုပ်ထားသည်

**✅ VS Code Integration**
- [ ] `.vscode/mcp.json` ကို configure လုပ်ထားသည်
- [ ] Python interpreter ကို virtual environment သို့ set လုပ်ထားသည်
- [ ] MCP servers တွေ AI Chat မှာပေါ်နေသည်
- [ ] AI Chat မှ test queries တွေကို run လုပ်နိုင်သည်

## 🛠️ Troubleshooting Common Issues

### Docker Issues

**ပြဿနာ**: Docker containers မစတင်နိုင်ပါ
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

**ပြဿနာ**: PostgreSQL connection မအောင်မြင်ပါ
```bash
# Check container logs
docker-compose logs postgres

# Verify container is healthy
docker-compose ps

# Test direct connection
docker-compose exec postgres psql -U postgres -d zava -c "SELECT 1;"
```

### Azure Deployment Issues

**ပြဿနာ**: Azure deployment မအောင်မြင်ပါ
```bash
# Check Azure CLI authentication
az account show

# Verify subscription permissions
az role assignment list --assignee $(az account show --query user.name -o tsv)

# Check resource provider registration
az provider register --namespace Microsoft.CognitiveServices
az provider register --namespace Microsoft.Insights
```

**ပြဿနာ**: AI service authentication မအောင်မြင်ပါ
```bash
# Test service principal
az login --service-principal \
  --username $AZURE_CLIENT_ID \
  --password $AZURE_CLIENT_SECRET \
  --tenant $AZURE_TENANT_ID

# Verify AI service deployment
az cognitiveservices account list --query "[].{Name:name,Kind:kind,Location:location}"
```

### Python Environment Issues

**ပြဿနာ**: Package installation မအောင်မြင်ပါ
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

**ပြဿနာ**: VS Code မှ Python interpreter ကို မတွေ့ပါ
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

## 🎯 အဓိက အကျဉ်းချုပ်

ဒီ lab ကိုပြီးဆုံးတဲ့အခါမှာ သင်မှာ:

✅ **Complete Development Environment**: Tools အားလုံးကို install နဲ့ configure လုပ်ထားသည်  
✅ **Azure Resources Deployed**: AI services နဲ့ support infrastructure  
✅ **Docker Environment Running**: PostgreSQL နဲ့ MCP server containers  
✅ **VS Code Integration**: MCP servers တွေ configure လုပ်ပြီး access လုပ်နိုင်သည်  
✅ **Validated Setup**: Components အားလုံးကို test လုပ်ပြီး အလုပ်လုပ်နေသည်  
✅ **Troubleshooting Knowledge**: အခက်အခဲများနဲ့ ဖြေရှင်းနည်းများ  

## 🚀 အခုနောက်တစ်ခု

သင့်ပတ်ဝန်းကျင်ကို ပြင်ဆင်ပြီးပါက **[Lab 04: Database Design and Schema](../04-Database/README.md)** ကို ဆက်လက်လုပ်ဆောင်ပါ:

- Retail database schema ကို အသေးစိတ်လေ့လာပါ
- Multi-tenant data modeling ကို နားလည်ပါ
- Row Level Security implementation ကို လေ့လာပါ
- Retail data sample တွေကို အသုံးပြုပါ

## 📚 အပိုဆောင်း အရင်းအမြစ်များ

### Development Tools
- [Docker Documentation](https://docs.docker.com/) - Docker အပြည့်အစုံကို ရှင်းလင်းထားသည်
- [Azure CLI Reference](https://docs.microsoft.com/cli/azure/) - Azure CLI commands
- [VS Code Documentation](https://code.visualstudio.com/docs) - Editor configuration နဲ့ extensions

### Azure Services
- [Azure AI Foundry Documentation](https://docs.microsoft.com/azure/ai-foundry/) - AI service configuration
- [Azure OpenAI Service](https://docs.microsoft.com/azure/cognitive-services/openai/) - AI model deployment
- [Application Insights](https://docs.microsoft.com/azure/azure-monitor/app/app-insights-overview) - Monitoring setup

### Python Development
- [Python Virtual Environments](https://docs.python.org/3/tutorial/venv.html) - Environment management
- [AsyncIO Documentation](https://docs.python.org/3/library/asyncio.html) - Async programming patterns
- [FastAPI Documentation](https://fastapi.tiangolo.com/) - Web framework patterns

---

**Next**: ပတ်ဝန်းကျင်ကို ပြင်ဆင်ပြီးပါက [Lab 04: Database Design and Schema](../04-Database/README.md) ကို ဆက်လက်လုပ်ဆောင်ပါ

---

**အကြောင်းကြားချက်**:  
ဤစာရွက်စာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ကို အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှန်ကန်မှုအတွက် ကြိုးစားနေသော်လည်း အလိုအလျောက် ဘာသာပြန်ခြင်းတွင် အမှားများ သို့မဟုတ် မမှန်ကန်မှုများ ပါဝင်နိုင်သည်ကို သတိပြုပါ။ မူရင်းဘာသာစကားဖြင့် ရေးသားထားသော စာရွက်စာတမ်းကို အာဏာတရားရှိသော အရင်းအမြစ်အဖြစ် သတ်မှတ်သင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူ့ဘာသာပြန်ပညာရှင်များမှ ပရော်ဖက်ရှင်နယ် ဘာသာပြန်ခြင်းကို အကြံပြုပါသည်။ ဤဘာသာပြန်ကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော အလွဲအမှားများ သို့မဟုတ် အနားလွဲမှုများအတွက် ကျွန်ုပ်တို့သည် တာဝန်မယူပါ။