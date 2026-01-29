# পরিবেশ সেটআপ

## 🎯 এই ল্যাবে যা শিখবেন

এই হাতে-কলমে ল্যাবটি আপনাকে MCP সার্ভার তৈরি করার জন্য PostgreSQL ইন্টিগ্রেশন সহ একটি সম্পূর্ণ ডেভেলপমেন্ট পরিবেশ সেটআপ করার নির্দেশনা দেবে। আপনি প্রয়োজনীয় সমস্ত টুল কনফিগার করবেন, Azure রিসোর্স ডিপ্লয় করবেন এবং বাস্তবায়নের আগে আপনার সেটআপ যাচাই করবেন।

## সংক্ষিপ্ত বিবরণ

একটি সঠিক ডেভেলপমেন্ট পরিবেশ MCP সার্ভার ডেভেলপমেন্টের জন্য অত্যন্ত গুরুত্বপূর্ণ। এই ল্যাবটি আপনাকে Docker, Azure সার্ভিস, ডেভেলপমেন্ট টুল সেটআপ এবং সেগুলো একসাথে সঠিকভাবে কাজ করছে কিনা তা যাচাই করার ধাপে ধাপে নির্দেশনা প্রদান করে।

এই ল্যাবের শেষে, আপনি Zava Retail MCP সার্ভার তৈরির জন্য একটি সম্পূর্ণ কার্যকর ডেভেলপমেন্ট পরিবেশ প্রস্তুত করবেন।

## শেখার লক্ষ্য

এই ল্যাবের শেষে, আপনি সক্ষম হবেন:

- **প্রয়োজনীয় ডেভেলপমেন্ট টুল ইনস্টল এবং কনফিগার** করতে
- **MCP সার্ভারের জন্য প্রয়োজনীয় Azure রিসোর্স ডিপ্লয়** করতে
- **PostgreSQL এবং MCP সার্ভারের জন্য Docker কন্টেইনার সেটআপ** করতে
- **পরিবেশ সেটআপ যাচাই** করতে টেস্ট সংযোগের মাধ্যমে
- **সাধারণ সেটআপ সমস্যা এবং কনফিগারেশন সমস্যার সমাধান** করতে
- **ডেভেলপমেন্ট ওয়ার্কফ্লো এবং ফাইল স্ট্রাকচার বুঝতে**

## 📋 প্রয়োজনীয়তা যাচাই

শুরু করার আগে নিশ্চিত করুন যে আপনার কাছে আছে:

### প্রয়োজনীয় জ্ঞান
- বেসিক কমান্ড লাইন ব্যবহার (Windows Command Prompt/PowerShell)
- পরিবেশ ভেরিয়েবল সম্পর্কে ধারণা
- Git ভার্সন কন্ট্রোলের সাথে পরিচিতি
- Docker-এর বেসিক ধারণা (কন্টেইনার, ইমেজ, ভলিউম)

### সিস্টেমের প্রয়োজনীয়তা
- **অপারেটিং সিস্টেম**: Windows 10/11, macOS, বা Linux
- **RAM**: ন্যূনতম 8GB (16GB সুপারিশকৃত)
- **স্টোরেজ**: অন্তত 10GB ফ্রি স্পেস
- **নেটওয়ার্ক**: ডাউনলোড এবং Azure ডিপ্লয়মেন্টের জন্য ইন্টারনেট সংযোগ

### অ্যাকাউন্টের প্রয়োজনীয়তা
- **Azure Subscription**: ফ্রি টিয়ার যথেষ্ট
- **GitHub Account**: রিপোজিটরি অ্যাক্সেসের জন্য
- **Docker Hub Account**: (ঐচ্ছিক) কাস্টম ইমেজ প্রকাশের জন্য

## 🛠️ টুল ইনস্টলেশন

### ১. Docker Desktop ইনস্টল করুন

Docker আমাদের ডেভেলপমেন্ট সেটআপের জন্য কন্টেইনারাইজড পরিবেশ প্রদান করে।

#### Windows ইনস্টলেশন

1. **Docker Desktop ডাউনলোড করুন**:
   ```cmd
   # Visit https://desktop.docker.com/win/stable/Docker%20Desktop%20Installer.exe
   # Or use Windows Package Manager
   winget install Docker.DockerDesktop
   ```

2. **ইনস্টল এবং কনফিগার করুন**:
   - ইনস্টলারটি Administrator হিসেবে চালান
   - WSL 2 ইন্টিগ্রেশন সক্ষম করুন যখন প্রম্পট দেখাবে
   - ইনস্টলেশন সম্পন্ন হলে কম্পিউটার রিস্টার্ট করুন

3. **ইনস্টলেশন যাচাই করুন**:
   ```cmd
   docker --version
   docker-compose --version
   ```

#### macOS ইনস্টলেশন

1. **ডাউনলোড এবং ইনস্টল করুন**:
   ```bash
   # Download from https://desktop.docker.com/mac/stable/Docker.dmg
   # Or use Homebrew
   brew install --cask docker
   ```

2. **Docker Desktop চালু করুন**:
   - Applications থেকে Docker Desktop চালু করুন
   - প্রাথমিক সেটআপ উইজার্ড সম্পন্ন করুন

3. **ইনস্টলেশন যাচাই করুন**:
   ```bash
   docker --version
   docker-compose --version
   ```

#### Linux ইনস্টলেশন

1. **Docker Engine ইনস্টল করুন**:
   ```bash
   # Ubuntu/Debian
   curl -fsSL https://get.docker.com -o get-docker.sh
   sudo sh get-docker.sh
   sudo usermod -aG docker $USER
   
   # Log out and back in for group changes to take effect
   ```

2. **Docker Compose ইনস্টল করুন**:
   ```bash
   sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
   sudo chmod +x /usr/local/bin/docker-compose
   ```

### ২. Azure CLI ইনস্টল করুন

Azure CLI Azure রিসোর্স ডিপ্লয়মেন্ট এবং ম্যানেজমেন্ট সক্ষম করে।

#### Windows ইনস্টলেশন

```cmd
# Using Windows Package Manager
winget install Microsoft.AzureCLI

# Or download MSI from: https://aka.ms/installazurecliwindows
```

#### macOS ইনস্টলেশন

```bash
# Using Homebrew
brew install azure-cli

# Or using installer
curl -L https://aka.ms/InstallAzureCli | bash
```

#### Linux ইনস্টলেশন

```bash
# Ubuntu/Debian
curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash

# RHEL/CentOS
sudo rpm --import https://packages.microsoft.com/keys/microsoft.asc
sudo dnf install azure-cli
```

#### যাচাই এবং প্রমাণীকরণ

```bash
# Check installation
az version

# Login to Azure
az login

# Set default subscription (if you have multiple)
az account list --output table
az account set --subscription "Your-Subscription-Name"
```

### ৩. Git ইনস্টল করুন

Git রিপোজিটরি ক্লোন এবং ভার্সন কন্ট্রোলের জন্য প্রয়োজন।

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

### ৪. VS Code ইনস্টল করুন

Visual Studio Code MCP সমর্থন সহ একটি ইন্টিগ্রেটেড ডেভেলপমেন্ট এনভায়রনমেন্ট প্রদান করে।

#### ইনস্টলেশন

```cmd
# Windows
winget install Microsoft.VisualStudioCode

# macOS
brew install --cask visual-studio-code

# Linux (Ubuntu/Debian)
sudo snap install code --classic
```

#### প্রয়োজনীয় এক্সটেনশন

এই VS Code এক্সটেনশনগুলো ইনস্টল করুন:

```bash
# Install via command line
code --install-extension ms-python.python
code --install-extension ms-vscode.vscode-json
code --install-extension ms-azuretools.vscode-docker
code --install-extension ms-vscode.azure-account
```

অথবা VS Code থেকে ইনস্টল করুন:
1. VS Code খুলুন
2. Extensions-এ যান (Ctrl+Shift+X)
3. ইনস্টল করুন:
   - **Python** (Microsoft)
   - **Docker** (Microsoft)
   - **Azure Account** (Microsoft)
   - **JSON** (Microsoft)

### ৫. Python ইনস্টল করুন

Python 3.8+ MCP সার্ভার ডেভেলপমেন্টের জন্য প্রয়োজন।

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

#### ইনস্টলেশন যাচাই করুন

```bash
python --version  # Should show Python 3.11.x
pip --version      # Should show pip version
```

## 🚀 প্রজেক্ট সেটআপ

### ১. রিপোজিটরি ক্লোন করুন

```bash
# Clone the main repository
git clone https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail.git

# Navigate to the project directory
cd MCP-Server-and-PostgreSQL-Sample-Retail

# Verify repository structure
ls -la
```

### ২. Python ভার্চুয়াল এনভায়রনমেন্ট তৈরি করুন

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

### ৩. Python ডিপেনডেন্সি ইনস্টল করুন

```bash
# Install development dependencies
pip install -r requirements.lock.txt

# Verify key packages
pip list | grep fastmcp
pip list | grep asyncpg
pip list | grep azure
```

## ☁️ Azure রিসোর্স ডিপ্লয়মেন্ট

### ১. রিসোর্স প্রয়োজনীয়তা বুঝুন

আমাদের MCP সার্ভারের জন্য এই Azure রিসোর্সগুলো প্রয়োজন:

| **রিসোর্স** | **উদ্দেশ্য** | **আনুমানিক খরচ** |
|--------------|-------------|-------------------|
| **Azure AI Foundry** | AI মডেল হোস্টিং এবং ম্যানেজমেন্ট | $10-50/মাস |
| **OpenAI Deployment** | টেক্সট এম্বেডিং মডেল (text-embedding-3-small) | $5-20/মাস |
| **Application Insights** | মনিটরিং এবং টেলিমেট্রি | $5-15/মাস |
| **Resource Group** | রিসোর্স সংগঠন | ফ্রি |

### ২. Azure রিসোর্স ডিপ্লয় করুন

#### অপশন A: স্বয়ংক্রিয় ডিপ্লয়মেন্ট (সুপারিশকৃত)

```bash
# Navigate to infrastructure directory
cd infra

# Windows - PowerShell
./deploy.ps1

# macOS/Linux - Bash
./deploy.sh
```

ডিপ্লয়মেন্ট স্ক্রিপ্টটি করবে:
1. একটি ইউনিক রিসোর্স গ্রুপ তৈরি
2. Azure AI Foundry রিসোর্স ডিপ্লয়
3. text-embedding-3-small মডেল ডিপ্লয়
4. Application Insights কনফিগার
5. প্রমাণীকরণের জন্য একটি সার্ভিস প্রিন্সিপাল তৈরি
6. `.env` ফাইল তৈরি করে কনফিগারেশন প্রদান

#### অপশন B: ম্যানুয়াল ডিপ্লয়মেন্ট

যদি আপনি ম্যানুয়াল নিয়ন্ত্রণ পছন্দ করেন বা স্বয়ংক্রিয় স্ক্রিপ্ট ব্যর্থ হয়:

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

### ৩. Azure ডিপ্লয়মেন্ট যাচাই করুন

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

### ৪. পরিবেশ ভেরিয়েবল কনফিগার করুন

ডিপ্লয়মেন্টের পরে, আপনার কাছে একটি `.env` ফাইল থাকা উচিত। নিশ্চিত করুন এটি অন্তর্ভুক্ত করে:

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

## 🐳 Docker পরিবেশ সেটআপ

### ১. Docker কম্পোজিশন বুঝুন

আমাদের ডেভেলপমেন্ট পরিবেশ Docker Compose ব্যবহার করে:

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

### ২. ডেভেলপমেন্ট পরিবেশ শুরু করুন

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

### ৩. ডাটাবেস সেটআপ যাচাই করুন

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

### ৪. MCP সার্ভার পরীক্ষা করুন

```bash
# Check MCP server health
curl http://localhost:8000/health

# Test basic MCP endpoint
curl -X POST http://localhost:8000/mcp \
  -H "Content-Type: application/json" \
  -H "x-rls-user-id: 00000000-0000-0000-0000-000000000000" \
  -d '{"method": "tools/list", "params": {}}'
```

## 🔧 VS Code কনফিগারেশন

### ১. MCP ইন্টিগ্রেশন কনফিগার করুন

VS Code MCP কনফিগারেশন তৈরি করুন:

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

### ২. Python পরিবেশ কনফিগার করুন

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

### ৩. VS Code ইন্টিগ্রেশন পরীক্ষা করুন

1. **প্রজেক্টটি VS Code-এ খুলুন**:
   ```bash
   code .
   ```

2. **AI Chat খুলুন**:
   - `Ctrl+Shift+P` (Windows/Linux) বা `Cmd+Shift+P` (macOS) চাপুন
   - "AI Chat" টাইপ করুন এবং "AI Chat: Open Chat" নির্বাচন করুন

3. **MCP সার্ভার সংযোগ পরীক্ষা করুন**:
   - AI Chat-এ `#zava` টাইপ করুন এবং কনফিগার করা সার্ভারগুলোর একটি নির্বাচন করুন
   - জিজ্ঞাসা করুন: "ডাটাবেসে কোন টেবিলগুলো উপলব্ধ?"
   - আপনি রিটেইল ডাটাবেস টেবিলগুলোর একটি তালিকা পাবেন

## ✅ পরিবেশ যাচাই

### ১. সামগ্রিক সিস্টেম চেক

আপনার সেটআপ যাচাই করতে এই যাচাই স্ক্রিপ্ট চালান:

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

### ২. ম্যানুয়াল যাচাই চেকলিস্ট

**✅ বেসিক টুল**
- [ ] Docker সংস্করণ 20.10+ ইনস্টল এবং চালু
- [ ] Azure CLI 2.40+ ইনস্টল এবং প্রমাণীকৃত
- [ ] Python 3.8+ pip সহ ইনস্টল
- [ ] Git 2.30+ ইনস্টল
- [ ] VS Code প্রয়োজনীয় এক্সটেনশন সহ

**✅ Azure রিসোর্স**
- [ ] রিসোর্স গ্রুপ সফলভাবে তৈরি
- [ ] AI Foundry প্রজেক্ট ডিপ্লয়
- [ ] OpenAI text-embedding-3-small মডেল ডিপ্লয়
- [ ] Application Insights কনফিগার
- [ ] সঠিক অনুমতি সহ সার্ভিস প্রিন্সিপাল তৈরি

**✅ পরিবেশ কনফিগারেশন**
- [ ] `.env` ফাইল তৈরি এবং প্রয়োজনীয় ভেরিয়েবল সহ
- [ ] Azure ক্রেডেনশিয়াল কাজ করছে (`az account show` দিয়ে পরীক্ষা করুন)
- [ ] PostgreSQL কন্টেইনার চালু এবং অ্যাক্সেসযোগ্য
- [ ] ডাটাবেসে স্যাম্পল ডেটা লোড করা হয়েছে

**✅ VS Code ইন্টিগ্রেশন**
- [ ] `.vscode/mcp.json` কনফিগার করা হয়েছে
- [ ] Python ইন্টারপ্রেটার ভার্চুয়াল এনভায়রনমেন্টে সেট করা হয়েছে
- [ ] MCP সার্ভারগুলো AI Chat-এ প্রদর্শিত হচ্ছে
- [ ] AI Chat-এর মাধ্যমে টেস্ট কোয়েরি চালানো যাচ্ছে

## 🛠️ সাধারণ সমস্যার সমাধান

### Docker সমস্যা

**সমস্যা**: Docker কন্টেইনার চালু হচ্ছে না
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

**সমস্যা**: PostgreSQL সংযোগ ব্যর্থ
```bash
# Check container logs
docker-compose logs postgres

# Verify container is healthy
docker-compose ps

# Test direct connection
docker-compose exec postgres psql -U postgres -d zava -c "SELECT 1;"
```

### Azure ডিপ্লয়মেন্ট সমস্যা

**সমস্যা**: Azure ডিপ্লয়মেন্ট ব্যর্থ
```bash
# Check Azure CLI authentication
az account show

# Verify subscription permissions
az role assignment list --assignee $(az account show --query user.name -o tsv)

# Check resource provider registration
az provider register --namespace Microsoft.CognitiveServices
az provider register --namespace Microsoft.Insights
```

**সমস্যা**: AI সার্ভিস প্রমাণীকরণ ব্যর্থ
```bash
# Test service principal
az login --service-principal \
  --username $AZURE_CLIENT_ID \
  --password $AZURE_CLIENT_SECRET \
  --tenant $AZURE_TENANT_ID

# Verify AI service deployment
az cognitiveservices account list --query "[].{Name:name,Kind:kind,Location:location}"
```

### Python পরিবেশ সমস্যা

**সমস্যা**: প্যাকেজ ইনস্টলেশন ব্যর্থ
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

**সমস্যা**: VS Code Python ইন্টারপ্রেটার খুঁজে পাচ্ছে না
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

## 🎯 মূল বিষয়গুলো

এই ল্যাব সম্পন্ন করার পরে, আপনার কাছে থাকবে:

✅ **সম্পূর্ণ ডেভেলপমেন্ট পরিবেশ**: সমস্ত টুল ইনস্টল এবং কনফিগার করা  
✅ **Azure রিসোর্স ডিপ্লয়ড**: AI সার্ভিস এবং সাপোর্টিং ইনফ্রাস্ট্রাকচার  
✅ **Docker পরিবেশ চালু**: PostgreSQL এবং MCP সার্ভার কন্টেইনার  
✅ **VS Code ইন্টিগ্রেশন**: MCP সার্ভার কনফিগার এবং অ্যাক্সেসযোগ্য  
✅ **যাচাই করা সেটআপ**: সমস্ত কম্পোনেন্ট একসাথে কাজ করছে  
✅ **সমস্যার সমাধানের জ্ঞান**: সাধারণ সমস্যাগুলো এবং সমাধান  

## 🚀 পরবর্তী ধাপ

আপনার পরিবেশ প্রস্তুত হলে, **[ল্যাব ০৪: ডাটাবেস ডিজাইন এবং স্কিমা](../04-Database/README.md)**-এ এগিয়ে যান:

- রিটেইল ডাটাবেস স্কিমা বিস্তারিতভাবে অন্বেষণ করুন
- মাল্টি-টেন্যান্ট ডেটা মডেলিং বুঝুন
- Row Level Security বাস্তবায়ন শিখুন
- স্যাম্পল রিটেইল ডেটার সাথে কাজ করুন

## 📚 অতিরিক্ত রিসোর্স

### ডেভেলপমেন্ট টুল
- [Docker ডকুমেন্টেশন](https://docs.docker.com/) - সম্পূর্ণ Docker রেফারেন্স
- [Azure CLI রেফারেন্স](https://docs.microsoft.com/cli/azure/) - Azure CLI কমান্ড
- [VS Code ডকুমেন্টেশন](https://code.visualstudio.com/docs) - এডিটর কনফিগারেশন এবং এক্সটেনশন

### Azure সার্ভিস
- [Azure AI Foundry ডকুমেন্টেশন](https://docs.microsoft.com/azure/ai-foundry/) - AI সার্ভিস কনফিগারেশন
- [Azure OpenAI সার্ভিস](https://docs.microsoft.com/azure/cognitive-services/openai/) - AI মডেল ডিপ্লয়মেন্ট
- [Application Insights](https://docs.microsoft.com/azure/azure-monitor/app/app-insights-overview) - মনিটরিং সেটআপ

### Python ডেভেলপমেন্ট
- [Python ভার্চুয়াল এনভায়রনমেন্ট](https://docs.python.org/3/tutorial/venv.html) - পরিবেশ ব্যবস্থাপনা
- [AsyncIO ডকুমেন্টেশন](https://docs.python.org/3/library/asyncio.html) - Async প্রোগ্রামিং প্যাটার্ন
- [FastAPI ডকুমেন্টেশন](https://fastapi.tiangolo.com/) - ওয়েব ফ্রেমওয়ার্ক প্যাটার্ন

---

**পরবর্তী**: পরিবেশ প্রস্তুত? [ল্যাব ০৪: ডাটাবেস ডিজাইন এবং স্কিমা](../04-Database/README.md)-এ এগিয়ে যান

---

**অস্বীকৃতি**:  
এই নথিটি AI অনুবাদ পরিষেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনুবাদ করা হয়েছে। আমরা যথাসাধ্য সঠিকতার জন্য চেষ্টা করি, তবে অনুগ্রহ করে মনে রাখবেন যে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা অসঙ্গতি থাকতে পারে। মূল ভাষায় থাকা নথিটিকে প্রামাণিক উৎস হিসেবে বিবেচনা করা উচিত। গুরুত্বপূর্ণ তথ্যের জন্য, পেশাদার মানব অনুবাদ সুপারিশ করা হয়। এই অনুবাদ ব্যবহারের ফলে কোনো ভুল বোঝাবুঝি বা ভুল ব্যাখ্যা হলে আমরা দায়বদ্ধ থাকব না।