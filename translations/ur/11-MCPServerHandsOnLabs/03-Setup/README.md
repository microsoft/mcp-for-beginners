# ماحول کی ترتیب

## 🎯 یہ لیب کیا کور کرتی ہے؟

یہ عملی لیب آپ کو MCP سرورز کی تعمیر کے لیے PostgreSQL انضمام کے ساتھ مکمل ترقیاتی ماحول ترتیب دینے کے مراحل سے گزرتی ہے۔ آپ تمام ضروری ٹولز کو ترتیب دیں گے، Azure وسائل کو تعینات کریں گے، اور عمل درآمد سے پہلے اپنی ترتیب کی تصدیق کریں گے۔

## جائزہ

ایک مناسب ترقیاتی ماحول MCP سرور کی کامیاب ترقی کے لیے بہت ضروری ہے۔ یہ لیب آپ کو Docker، Azure خدمات، ترقیاتی ٹولز ترتیب دینے اور یہ یقینی بنانے کے لیے مرحلہ وار ہدایات فراہم کرتی ہے کہ سب کچھ صحیح طریقے سے کام کر رہا ہے۔

اس لیب کے اختتام تک، آپ کے پاس Zava Retail MCP سرور کی تعمیر کے لیے مکمل طور پر فعال ترقیاتی ماحول ہوگا۔

## سیکھنے کے مقاصد

اس لیب کے اختتام تک، آپ یہ کرنے کے قابل ہوں گے:

- **تمام ضروری ترقیاتی ٹولز انسٹال اور ترتیب دیں**
- **MCP سرور کے لیے ضروری Azure وسائل تعینات کریں**
- **PostgreSQL اور MCP سرور کے لیے Docker کنٹینرز ترتیب دیں**
- **اپنے ماحول کی ترتیب کو ٹیسٹ کنکشنز کے ساتھ تصدیق کریں**
- **عام ترتیب کے مسائل اور کنفیگریشن کے مسائل کو حل کریں**
- **ترقیاتی ورک فلو اور فائل اسٹرکچر کو سمجھیں**

## 📋 ضروریات کی جانچ

شروع کرنے سے پہلے، یقینی بنائیں کہ آپ کے پاس یہ موجود ہیں:

### مطلوبہ علم
- کمانڈ لائن کے بنیادی استعمال (Windows Command Prompt/PowerShell)
- ماحول کے متغیرات کو سمجھنا
- Git ورژن کنٹرول سے واقفیت
- Docker کے بنیادی تصورات (کنٹینرز، امیجز، والیمز)

### سسٹم کی ضروریات
- **آپریٹنگ سسٹم**: Windows 10/11، macOS، یا Linux
- **RAM**: کم از کم 8GB (16GB تجویز کردہ)
- **اسٹوریج**: کم از کم 10GB خالی جگہ
- **نیٹ ورک**: ڈاؤن لوڈز اور Azure تعیناتی کے لیے انٹرنیٹ کنکشن

### اکاؤنٹ کی ضروریات
- **Azure سبسکرپشن**: مفت ٹائر کافی ہے
- **GitHub اکاؤنٹ**: ریپوزٹری تک رسائی کے لیے
- **Docker Hub اکاؤنٹ**: (اختیاری) کسٹم امیج پبلشنگ کے لیے

## 🛠️ ٹول انسٹالیشن

### 1. Docker Desktop انسٹال کریں

Docker ہمارے ترقیاتی سیٹ اپ کے لیے کنٹینرائزڈ ماحول فراہم کرتا ہے۔

#### Windows انسٹالیشن

1. **Docker Desktop ڈاؤن لوڈ کریں**:
   ```cmd
   # Visit https://desktop.docker.com/win/stable/Docker%20Desktop%20Installer.exe
   # Or use Windows Package Manager
   winget install Docker.DockerDesktop
   ```

2. **انسٹال اور ترتیب دیں**:
   - انسٹالر کو ایڈمنسٹریٹر کے طور پر چلائیں
   - WSL 2 انضمام کو فعال کریں جب پوچھا جائے
   - انسٹالیشن مکمل ہونے پر اپنے کمپیوٹر کو دوبارہ شروع کریں

3. **انسٹالیشن کی تصدیق کریں**:
   ```cmd
   docker --version
   docker-compose --version
   ```

#### macOS انسٹالیشن

1. **ڈاؤن لوڈ اور انسٹال کریں**:
   ```bash
   # Download from https://desktop.docker.com/mac/stable/Docker.dmg
   # Or use Homebrew
   brew install --cask docker
   ```

2. **Docker Desktop شروع کریں**:
   - Applications سے Docker Desktop لانچ کریں
   - ابتدائی سیٹ اپ وزرڈ مکمل کریں

3. **انسٹالیشن کی تصدیق کریں**:
   ```bash
   docker --version
   docker-compose --version
   ```

#### Linux انسٹالیشن

1. **Docker Engine انسٹال کریں**:
   ```bash
   # Ubuntu/Debian
   curl -fsSL https://get.docker.com -o get-docker.sh
   sudo sh get-docker.sh
   sudo usermod -aG docker $USER
   
   # Log out and back in for group changes to take effect
   ```

2. **Docker Compose انسٹال کریں**:
   ```bash
   sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
   sudo chmod +x /usr/local/bin/docker-compose
   ```

### 2. Azure CLI انسٹال کریں

Azure CLI Azure وسائل کی تعیناتی اور انتظام کو فعال کرتا ہے۔

#### Windows انسٹالیشن

```cmd
# Using Windows Package Manager
winget install Microsoft.AzureCLI

# Or download MSI from: https://aka.ms/installazurecliwindows
```

#### macOS انسٹالیشن

```bash
# Using Homebrew
brew install azure-cli

# Or using installer
curl -L https://aka.ms/InstallAzureCli | bash
```

#### Linux انسٹالیشن

```bash
# Ubuntu/Debian
curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash

# RHEL/CentOS
sudo rpm --import https://packages.microsoft.com/keys/microsoft.asc
sudo dnf install azure-cli
```

#### تصدیق اور توثیق

```bash
# Check installation
az version

# Login to Azure
az login

# Set default subscription (if you have multiple)
az account list --output table
az account set --subscription "Your-Subscription-Name"
```

### 3. Git انسٹال کریں

Git ریپوزٹری کلوننگ اور ورژن کنٹرول کے لیے ضروری ہے۔

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

### 4. VS Code انسٹال کریں

Visual Studio Code MCP سپورٹ کے ساتھ مربوط ترقیاتی ماحول فراہم کرتا ہے۔

#### انسٹالیشن

```cmd
# Windows
winget install Microsoft.VisualStudioCode

# macOS
brew install --cask visual-studio-code

# Linux (Ubuntu/Debian)
sudo snap install code --classic
```

#### مطلوبہ ایکسٹینشنز

یہ VS Code ایکسٹینشنز انسٹال کریں:

```bash
# Install via command line
code --install-extension ms-python.python
code --install-extension ms-vscode.vscode-json
code --install-extension ms-azuretools.vscode-docker
code --install-extension ms-vscode.azure-account
```

یا VS Code کے ذریعے انسٹال کریں:
1. VS Code کھولیں
2. Extensions پر جائیں (Ctrl+Shift+X)
3. انسٹال کریں:
   - **Python** (Microsoft)
   - **Docker** (Microsoft)
   - **Azure Account** (Microsoft)
   - **JSON** (Microsoft)

### 5. Python انسٹال کریں

Python 3.8+ MCP سرور کی ترقی کے لیے ضروری ہے۔

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

#### انسٹالیشن کی تصدیق کریں

```bash
python --version  # Should show Python 3.11.x
pip --version      # Should show pip version
```

## 🚀 پروجیکٹ سیٹ اپ

### 1. ریپوزٹری کلون کریں

```bash
# Clone the main repository
git clone https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail.git

# Navigate to the project directory
cd MCP-Server-and-PostgreSQL-Sample-Retail

# Verify repository structure
ls -la
```

### 2. Python ورچوئل ماحول بنائیں

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

### 3. Python کی ضروریات انسٹال کریں

```bash
# Install development dependencies
pip install -r requirements.lock.txt

# Verify key packages
pip list | grep fastmcp
pip list | grep asyncpg
pip list | grep azure
```

## ☁️ Azure وسائل کی تعیناتی

### 1. وسائل کی ضروریات کو سمجھیں

ہمارے MCP سرور کو یہ Azure وسائل درکار ہیں:

| **وسائل** | **مقصد** | **تخمینی لاگت** |
|-----------|----------|----------------|
| **Azure AI Foundry** | AI ماڈل کی میزبانی اور انتظام | $10-50/ماہ |
| **OpenAI تعیناتی** | ٹیکسٹ ایمبیڈنگ ماڈل (text-embedding-3-small) | $5-20/ماہ |
| **Application Insights** | مانیٹرنگ اور ٹیلیمیٹری | $5-15/ماہ |
| **Resource Group** | وسائل کی تنظیم | مفت |

### 2. Azure وسائل تعینات کریں

#### آپشن A: خودکار تعیناتی (تجویز کردہ)

```bash
# Navigate to infrastructure directory
cd infra

# Windows - PowerShell
./deploy.ps1

# macOS/Linux - Bash
./deploy.sh
```

تعیناتی اسکرپٹ یہ کرے گا:
1. ایک منفرد ریسورس گروپ بنائیں
2. Azure AI Foundry وسائل تعینات کریں
3. text-embedding-3-small ماڈل تعینات کریں
4. Application Insights ترتیب دیں
5. توثیق کے لیے سروس پرنسپل بنائیں
6. `.env` فائل جنریٹ کریں جس میں کنفیگریشن ہو

#### آپشن B: دستی تعیناتی

اگر آپ دستی کنٹرول کو ترجیح دیتے ہیں یا خودکار اسکرپٹ ناکام ہو جاتا ہے:

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

### 3. Azure تعیناتی کی تصدیق کریں

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

### 4. ماحول کے متغیرات ترتیب دیں

تعیناتی کے بعد، آپ کے پاس `.env` فائل ہونی چاہیے۔ تصدیق کریں کہ اس میں یہ شامل ہیں:

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

## 🐳 Docker ماحول کی ترتیب

### 1. Docker کمپوزیشن کو سمجھیں

ہمارا ترقیاتی ماحول Docker Compose استعمال کرتا ہے:

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

### 2. ترقیاتی ماحول شروع کریں

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

### 3. ڈیٹا بیس سیٹ اپ کی تصدیق کریں

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

### 4. MCP سرور ٹیسٹ کریں

```bash
# Check MCP server health
curl http://localhost:8000/health

# Test basic MCP endpoint
curl -X POST http://localhost:8000/mcp \
  -H "Content-Type: application/json" \
  -H "x-rls-user-id: 00000000-0000-0000-0000-000000000000" \
  -d '{"method": "tools/list", "params": {}}'
```

## 🔧 VS Code کنفیگریشن

### 1. MCP انضمام ترتیب دیں

VS Code MCP کنفیگریشن بنائیں:

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

### 2. Python ماحول ترتیب دیں

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

### 3. VS Code انضمام ٹیسٹ کریں

1. **پروجیکٹ کو VS Code میں کھولیں**:
   ```bash
   code .
   ```

2. **AI چیٹ کھولیں**:
   - `Ctrl+Shift+P` (Windows/Linux) یا `Cmd+Shift+P` (macOS) دبائیں
   - "AI Chat" ٹائپ کریں اور "AI Chat: Open Chat" منتخب کریں

3. **MCP سرور کنکشن ٹیسٹ کریں**:
   - AI چیٹ میں، `#zava` ٹائپ کریں اور ترتیب دیے گئے سرورز میں سے ایک منتخب کریں
   - پوچھیں: "ڈیٹا بیس میں کون سے ٹیبل دستیاب ہیں؟"
   - آپ کو ریٹیل ڈیٹا بیس ٹیبلز کی فہرست موصول ہونی چاہیے

## ✅ ماحول کی تصدیق

### 1. جامع سسٹم چیک

اپنی ترتیب کی تصدیق کے لیے یہ اسکرپٹ چلائیں:

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

### 2. دستی تصدیق چیک لسٹ

**✅ بنیادی ٹولز**
- [ ] Docker ورژن 20.10+ انسٹال اور چل رہا ہے
- [ ] Azure CLI 2.40+ انسٹال اور توثیق شدہ
- [ ] Python 3.8+ pip کے ساتھ انسٹال
- [ ] Git 2.30+ انسٹال
- [ ] VS Code مطلوبہ ایکسٹینشنز کے ساتھ

**✅ Azure وسائل**
- [ ] ریسورس گروپ کامیابی سے بنایا گیا
- [ ] AI Foundry پروجیکٹ تعینات
- [ ] OpenAI text-embedding-3-small ماڈل تعینات
- [ ] Application Insights ترتیب دیا گیا
- [ ] سروس پرنسپل مناسب اجازتوں کے ساتھ بنایا گیا

**✅ ماحول کی ترتیب**
- [ ] `.env` فائل تمام مطلوبہ متغیرات کے ساتھ بنائی گئی
- [ ] Azure اسناد کام کر رہی ہیں (ٹیسٹ کریں `az account show` کے ساتھ)
- [ ] PostgreSQL کنٹینر چل رہا ہے اور قابل رسائی ہے
- [ ] ڈیٹا بیس میں نمونہ ڈیٹا لوڈ کیا گیا

**✅ VS Code انضمام**
- [ ] `.vscode/mcp.json` ترتیب دیا گیا
- [ ] Python انٹرپریٹر ورچوئل ماحول پر سیٹ کیا گیا
- [ ] MCP سرورز AI چیٹ میں ظاہر ہو رہے ہیں
- [ ] AI چیٹ کے ذریعے ٹیسٹ کوئریز انجام دے سکتے ہیں

## 🛠️ عام مسائل کا حل

### Docker مسائل

**مسئلہ**: Docker کنٹینرز شروع نہیں ہو رہے
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

**مسئلہ**: PostgreSQL کنکشن ناکام ہو رہا ہے
```bash
# Check container logs
docker-compose logs postgres

# Verify container is healthy
docker-compose ps

# Test direct connection
docker-compose exec postgres psql -U postgres -d zava -c "SELECT 1;"
```

### Azure تعیناتی مسائل

**مسئلہ**: Azure تعیناتی ناکام ہو رہی ہے
```bash
# Check Azure CLI authentication
az account show

# Verify subscription permissions
az role assignment list --assignee $(az account show --query user.name -o tsv)

# Check resource provider registration
az provider register --namespace Microsoft.CognitiveServices
az provider register --namespace Microsoft.Insights
```

**مسئلہ**: AI سروس کی توثیق ناکام ہو رہی ہے
```bash
# Test service principal
az login --service-principal \
  --username $AZURE_CLIENT_ID \
  --password $AZURE_CLIENT_SECRET \
  --tenant $AZURE_TENANT_ID

# Verify AI service deployment
az cognitiveservices account list --query "[].{Name:name,Kind:kind,Location:location}"
```

### Python ماحول مسائل

**مسئلہ**: پیکیج انسٹالیشن ناکام ہو رہی ہے
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

**مسئلہ**: VS Code Python انٹرپریٹر نہیں ڈھونڈ سکتا
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

## 🎯 اہم نکات

اس لیب کو مکمل کرنے کے بعد، آپ کے پاس ہونا چاہیے:

✅ **مکمل ترقیاتی ماحول**: تمام ٹولز انسٹال اور ترتیب دیے گئے  
✅ **Azure وسائل تعینات**: AI خدمات اور معاون انفراسٹرکچر  
✅ **Docker ماحول چل رہا ہے**: PostgreSQL اور MCP سرور کنٹینرز  
✅ **VS Code انضمام**: MCP سرورز ترتیب دیے گئے اور قابل رسائی  
✅ **ترتیب کی تصدیق**: تمام اجزاء ٹیسٹ کیے گئے اور ایک ساتھ کام کر رہے ہیں  
✅ **مسائل کے حل کا علم**: عام مسائل اور ان کے حل  

## 🚀 آگے کیا ہے؟

اپنا ماحول تیار ہونے کے ساتھ، **[لیب 04: ڈیٹا بیس ڈیزائن اور اسکیمہ](../04-Database/README.md)** کے ساتھ جاری رکھیں:

- ریٹیل ڈیٹا بیس اسکیمہ کو تفصیل سے دریافت کریں
- ملٹی ٹیننٹ ڈیٹا ماڈلنگ کو سمجھیں
- Row Level Security کے نفاذ کے بارے میں سیکھیں
- نمونہ ریٹیل ڈیٹا کے ساتھ کام کریں

## 📚 اضافی وسائل

### ترقیاتی ٹولز
- [Docker دستاویزات](https://docs.docker.com/) - مکمل Docker حوالہ
- [Azure CLI حوالہ](https://docs.microsoft.com/cli/azure/) - Azure CLI کمانڈز
- [VS Code دستاویزات](https://code.visualstudio.com/docs) - ایڈیٹر کنفیگریشن اور ایکسٹینشنز

### Azure خدمات
- [Azure AI Foundry دستاویزات](https://docs.microsoft.com/azure/ai-foundry/) - AI سروس کنفیگریشن
- [Azure OpenAI سروس](https://docs.microsoft.com/azure/cognitive-services/openai/) - AI ماڈل تعیناتی
- [Application Insights](https://docs.microsoft.com/azure/azure-monitor/app/app-insights-overview) - مانیٹرنگ سیٹ اپ

### Python ترقی
- [Python ورچوئل ماحول](https://docs.python.org/3/tutorial/venv.html) - ماحول کا انتظام
- [AsyncIO دستاویزات](https://docs.python.org/3/library/asyncio.html) - Async پروگرامنگ پیٹرنز
- [FastAPI دستاویزات](https://fastapi.tiangolo.com/) - ویب فریم ورک پیٹرنز

---

**اگلا**: ماحول تیار ہے؟ [لیب 04: ڈیٹا بیس ڈیزائن اور اسکیمہ](../04-Database/README.md) کے ساتھ جاری رکھیں

---

**ڈسکلیمر**:  
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کا استعمال کرتے ہوئے ترجمہ کی گئی ہے۔ ہم درستگی کے لیے کوشش کرتے ہیں، لیکن براہ کرم آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا غیر درستیاں ہو سکتی ہیں۔ اصل دستاویز کو اس کی اصل زبان میں مستند ذریعہ سمجھا جانا چاہیے۔ اہم معلومات کے لیے، پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ ہم اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کے ذمہ دار نہیں ہیں۔