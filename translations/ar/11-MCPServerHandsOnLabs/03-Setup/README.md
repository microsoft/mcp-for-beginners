# إعداد البيئة

## 🎯 ما يغطيه هذا المختبر

هذا المختبر العملي يوجهك خلال إعداد بيئة تطوير كاملة لبناء خوادم MCP مع تكامل PostgreSQL. ستقوم بتكوين جميع الأدوات اللازمة، نشر موارد Azure، والتحقق من إعدادك قبل البدء في التنفيذ.

## نظرة عامة

بيئة التطوير المناسبة ضرورية لتطوير خوادم MCP بنجاح. يوفر هذا المختبر تعليمات خطوة بخطوة لإعداد Docker، خدمات Azure، أدوات التطوير، والتحقق من أن كل شيء يعمل بشكل صحيح معًا.

بنهاية هذا المختبر، ستكون لديك بيئة تطوير وظيفية بالكامل جاهزة لبناء خادم Zava Retail MCP.

## أهداف التعلم

بنهاية هذا المختبر، ستكون قادرًا على:

- **تثبيت وتكوين** جميع أدوات التطوير المطلوبة  
- **نشر موارد Azure** اللازمة لخادم MCP  
- **إعداد حاويات Docker** لـ PostgreSQL وخادم MCP  
- **التحقق** من إعداد البيئة باستخدام اتصالات اختبار  
- **حل المشكلات** الشائعة المتعلقة بالإعداد ومشاكل التكوين  
- **فهم** سير العمل وهيكل الملفات للتطوير  

## 📋 التحقق من المتطلبات الأساسية

قبل البدء، تأكد من توفر ما يلي:

### المعرفة المطلوبة
- استخدام أساسي لسطر الأوامر (Windows Command Prompt/PowerShell)  
- فهم المتغيرات البيئية  
- الإلمام بنظام التحكم في الإصدارات Git  
- مفاهيم Docker الأساسية (الحاويات، الصور، الأحجام)  

### متطلبات النظام
- **نظام التشغيل**: Windows 10/11، macOS، أو Linux  
- **الذاكرة العشوائية (RAM)**: الحد الأدنى 8GB (يوصى بـ 16GB)  
- **التخزين**: على الأقل 10GB مساحة فارغة  
- **الشبكة**: اتصال بالإنترنت للتنزيلات ونشر Azure  

### متطلبات الحساب
- **اشتراك Azure**: الطبقة المجانية كافية  
- **حساب GitHub**: للوصول إلى المستودع  
- **حساب Docker Hub**: (اختياري) لنشر الصور المخصصة  

## 🛠️ تثبيت الأدوات

### 1. تثبيت Docker Desktop

يوفر Docker البيئة المعبأة لحاويات التطوير.

#### تثبيت Windows

1. **تحميل Docker Desktop**:  
   ```cmd
   # Visit https://desktop.docker.com/win/stable/Docker%20Desktop%20Installer.exe
   # Or use Windows Package Manager
   winget install Docker.DockerDesktop
   ```
  
2. **التثبيت والتكوين**:  
   - قم بتشغيل المثبت كمسؤول  
   - قم بتمكين تكامل WSL 2 عند الطلب  
   - أعد تشغيل الكمبيوتر بعد اكتمال التثبيت  

3. **التحقق من التثبيت**:  
   ```cmd
   docker --version
   docker-compose --version
   ```
  

#### تثبيت macOS

1. **التحميل والتثبيت**:  
   ```bash
   # Download from https://desktop.docker.com/mac/stable/Docker.dmg
   # Or use Homebrew
   brew install --cask docker
   ```
  
2. **تشغيل Docker Desktop**:  
   - قم بتشغيل Docker Desktop من التطبيقات  
   - أكمل معالج الإعداد الأولي  

3. **التحقق من التثبيت**:  
   ```bash
   docker --version
   docker-compose --version
   ```
  

#### تثبيت Linux

1. **تثبيت Docker Engine**:  
   ```bash
   # Ubuntu/Debian
   curl -fsSL https://get.docker.com -o get-docker.sh
   sudo sh get-docker.sh
   sudo usermod -aG docker $USER
   
   # Log out and back in for group changes to take effect
   ```
  
2. **تثبيت Docker Compose**:  
   ```bash
   sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
   sudo chmod +x /usr/local/bin/docker-compose
   ```
  

### 2. تثبيت Azure CLI

يتيح Azure CLI نشر وإدارة موارد Azure.

#### تثبيت Windows

```cmd
# Using Windows Package Manager
winget install Microsoft.AzureCLI

# Or download MSI from: https://aka.ms/installazurecliwindows
```
  

#### تثبيت macOS

```bash
# Using Homebrew
brew install azure-cli

# Or using installer
curl -L https://aka.ms/InstallAzureCli | bash
```
  

#### تثبيت Linux

```bash
# Ubuntu/Debian
curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash

# RHEL/CentOS
sudo rpm --import https://packages.microsoft.com/keys/microsoft.asc
sudo dnf install azure-cli
```
  

#### التحقق والمصادقة

```bash
# Check installation
az version

# Login to Azure
az login

# Set default subscription (if you have multiple)
az account list --output table
az account set --subscription "Your-Subscription-Name"
```
  

### 3. تثبيت Git

Git مطلوب لاستنساخ المستودع والتحكم في الإصدارات.

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
  

### 4. تثبيت VS Code

يوفر Visual Studio Code بيئة تطوير متكاملة مع دعم MCP.

#### التثبيت

```cmd
# Windows
winget install Microsoft.VisualStudioCode

# macOS
brew install --cask visual-studio-code

# Linux (Ubuntu/Debian)
sudo snap install code --classic
```
  

#### الإضافات المطلوبة

قم بتثبيت إضافات VS Code التالية:  

```bash
# Install via command line
code --install-extension ms-python.python
code --install-extension ms-vscode.vscode-json
code --install-extension ms-azuretools.vscode-docker
code --install-extension ms-vscode.azure-account
```
  

أو قم بالتثبيت من خلال VS Code:  
1. افتح VS Code  
2. انتقل إلى الإضافات (Ctrl+Shift+X)  
3. قم بتثبيت:  
   - **Python** (Microsoft)  
   - **Docker** (Microsoft)  
   - **Azure Account** (Microsoft)  
   - **JSON** (Microsoft)  

### 5. تثبيت Python

Python 3.8+ مطلوب لتطوير خادم MCP.

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
  

#### التحقق من التثبيت

```bash
python --version  # Should show Python 3.11.x
pip --version      # Should show pip version
```
  

## 🚀 إعداد المشروع

### 1. استنساخ المستودع

```bash
# Clone the main repository
git clone https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail.git

# Navigate to the project directory
cd MCP-Server-and-PostgreSQL-Sample-Retail

# Verify repository structure
ls -la
```
  

### 2. إنشاء بيئة Python الافتراضية

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
  

### 3. تثبيت تبعيات Python

```bash
# Install development dependencies
pip install -r requirements.lock.txt

# Verify key packages
pip list | grep fastmcp
pip list | grep asyncpg
pip list | grep azure
```
  

## ☁️ نشر موارد Azure

### 1. فهم متطلبات الموارد

يتطلب خادم MCP هذه الموارد من Azure:

| **المورد** | **الغرض** | **التكلفة التقديرية** |  
|------------|-----------|-----------------------|  
| **Azure AI Foundry** | استضافة وإدارة النماذج الذكية | $10-50/شهريًا |  
| **OpenAI Deployment** | نموذج تضمين النصوص (text-embedding-3-small) | $5-20/شهريًا |  
| **Application Insights** | المراقبة والقياس | $5-15/شهريًا |  
| **Resource Group** | تنظيم الموارد | مجاني |  

### 2. نشر موارد Azure

#### الخيار A: النشر التلقائي (موصى به)

```bash
# Navigate to infrastructure directory
cd infra

# Windows - PowerShell
./deploy.ps1

# macOS/Linux - Bash
./deploy.sh
```
  

سيقوم سكربت النشر بـ:  
1. إنشاء مجموعة موارد فريدة  
2. نشر موارد Azure AI Foundry  
3. نشر نموذج text-embedding-3-small  
4. تكوين Application Insights  
5. إنشاء خدمة رئيسية للمصادقة  
6. إنشاء ملف `.env` مع التكوين  

#### الخيار B: النشر اليدوي

إذا كنت تفضل التحكم اليدوي أو فشل السكربت التلقائي:  

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
  

### 3. التحقق من نشر Azure

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
  

### 4. تكوين المتغيرات البيئية

بعد النشر، يجب أن يكون لديك ملف `.env`. تحقق من أنه يحتوي على:  

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
  

## 🐳 إعداد بيئة Docker

### 1. فهم تكوين Docker

تستخدم بيئة التطوير لدينا Docker Compose:  

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
  

### 2. بدء بيئة التطوير

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
  

### 3. التحقق من إعداد قاعدة البيانات

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
  

### 4. اختبار خادم MCP

```bash
# Check MCP server health
curl http://localhost:8000/health

# Test basic MCP endpoint
curl -X POST http://localhost:8000/mcp \
  -H "Content-Type: application/json" \
  -H "x-rls-user-id: 00000000-0000-0000-0000-000000000000" \
  -d '{"method": "tools/list", "params": {}}'
```
  

## 🔧 تكوين VS Code

### 1. تكوين تكامل MCP

قم بإنشاء تكوين MCP لـ VS Code:  

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
  

### 2. تكوين بيئة Python

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
  

### 3. اختبار تكامل VS Code

1. **افتح المشروع في VS Code**:  
   ```bash
   code .
   ```
  
2. **افتح AI Chat**:  
   - اضغط `Ctrl+Shift+P` (Windows/Linux) أو `Cmd+Shift+P` (macOS)  
   - اكتب "AI Chat" واختر "AI Chat: Open Chat"  

3. **اختبر اتصال خادم MCP**:  
   - في AI Chat، اكتب `#zava` واختر أحد الخوادم المكونة  
   - اسأل: "ما هي الجداول المتوفرة في قاعدة البيانات؟"  
   - يجب أن تتلقى ردًا يسرد جداول قاعدة بيانات البيع بالتجزئة  

## ✅ التحقق من البيئة

### 1. فحص النظام الشامل

قم بتشغيل سكربت التحقق هذا للتحقق من إعدادك:  

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
  

### 2. قائمة التحقق اليدوية للتحقق

**✅ الأدوات الأساسية**  
- [ ] تم تثبيت وتشغيل Docker الإصدار 20.10+  
- [ ] تم تثبيت Azure CLI الإصدار 2.40+ والمصادقة  
- [ ] Python 3.8+ مثبت مع pip  
- [ ] Git الإصدار 2.30+ مثبت  
- [ ] VS Code مع الإضافات المطلوبة  

**✅ موارد Azure**  
- [ ] تم إنشاء مجموعة الموارد بنجاح  
- [ ] تم نشر مشروع AI Foundry  
- [ ] تم نشر نموذج text-embedding-3-small  
- [ ] تم تكوين Application Insights  
- [ ] تم إنشاء خدمة رئيسية مع الأذونات المناسبة  

**✅ تكوين البيئة**  
- [ ] تم إنشاء ملف `.env` مع جميع المتغيرات المطلوبة  
- [ ] تعمل بيانات اعتماد Azure (اختبر باستخدام `az account show`)  
- [ ] حاوية PostgreSQL تعمل ويمكن الوصول إليها  
- [ ] تم تحميل بيانات العينة في قاعدة البيانات  

**✅ تكامل VS Code**  
- [ ] تم تكوين `.vscode/mcp.json`  
- [ ] تم تعيين مترجم Python إلى البيئة الافتراضية  
- [ ] تظهر خوادم MCP في AI Chat  
- [ ] يمكن تنفيذ استعلامات الاختبار عبر AI Chat  

## 🛠️ حل المشكلات الشائعة

### مشاكل Docker

**المشكلة**: الحاويات لا تبدأ  
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
  

**المشكلة**: فشل اتصال PostgreSQL  
```bash
# Check container logs
docker-compose logs postgres

# Verify container is healthy
docker-compose ps

# Test direct connection
docker-compose exec postgres psql -U postgres -d zava -c "SELECT 1;"
```
  

### مشاكل نشر Azure

**المشكلة**: فشل نشر Azure  
```bash
# Check Azure CLI authentication
az account show

# Verify subscription permissions
az role assignment list --assignee $(az account show --query user.name -o tsv)

# Check resource provider registration
az provider register --namespace Microsoft.CognitiveServices
az provider register --namespace Microsoft.Insights
```
  

**المشكلة**: فشل مصادقة خدمة الذكاء الاصطناعي  
```bash
# Test service principal
az login --service-principal \
  --username $AZURE_CLIENT_ID \
  --password $AZURE_CLIENT_SECRET \
  --tenant $AZURE_TENANT_ID

# Verify AI service deployment
az cognitiveservices account list --query "[].{Name:name,Kind:kind,Location:location}"
```
  

### مشاكل بيئة Python

**المشكلة**: فشل تثبيت الحزم  
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
  

**المشكلة**: VS Code لا يمكنه العثور على مترجم Python  
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
  

## 🎯 النقاط الرئيسية

بعد إكمال هذا المختبر، يجب أن تكون قد أنجزت:

✅ **بيئة تطوير كاملة**: تم تثبيت وتكوين جميع الأدوات  
✅ **نشر موارد Azure**: خدمات الذكاء الاصطناعي والبنية التحتية الداعمة  
✅ **تشغيل بيئة Docker**: حاويات PostgreSQL وخادم MCP  
✅ **تكامل VS Code**: تم تكوين خوادم MCP ويمكن الوصول إليها  
✅ **إعداد تم التحقق منه**: تم اختبار جميع المكونات وتعمل معًا  
✅ **معرفة حل المشكلات**: المشكلات الشائعة والحلول  

## 🚀 ما التالي

مع جاهزية بيئتك، تابع إلى **[مختبر 04: تصميم قاعدة البيانات والمخطط](../04-Database/README.md)** لـ:

- استكشاف مخطط قاعدة بيانات البيع بالتجزئة بالتفصيل  
- فهم نمذجة البيانات متعددة المستأجرين  
- تعلم تنفيذ أمان مستوى الصفوف  
- العمل مع بيانات البيع بالتجزئة النموذجية  

## 📚 موارد إضافية

### أدوات التطوير
- [وثائق Docker](https://docs.docker.com/) - مرجع Docker الكامل  
- [مرجع Azure CLI](https://docs.microsoft.com/cli/azure/) - أوامر Azure CLI  
- [وثائق VS Code](https://code.visualstudio.com/docs) - إعدادات المحرر والإضافات  

### خدمات Azure
- [وثائق Azure AI Foundry](https://docs.microsoft.com/azure/ai-foundry/) - تكوين خدمات الذكاء الاصطناعي  
- [خدمة Azure OpenAI](https://docs.microsoft.com/azure/cognitive-services/openai/) - نشر نماذج الذكاء الاصطناعي  
- [Application Insights](https://docs.microsoft.com/azure/azure-monitor/app/app-insights-overview) - إعداد المراقبة  

### تطوير Python
- [بيئات Python الافتراضية](https://docs.python.org/3/tutorial/venv.html) - إدارة البيئة  
- [وثائق AsyncIO](https://docs.python.org/3/library/asyncio.html) - أنماط البرمجة غير المتزامنة  
- [وثائق FastAPI](https://fastapi.tiangolo.com/) - أنماط إطار العمل  

---

**التالي**: هل البيئة جاهزة؟ تابع مع [مختبر 04: تصميم قاعدة البيانات والمخطط](../04-Database/README.md)

---

**إخلاء المسؤولية**:  
تم ترجمة هذا المستند باستخدام خدمة الترجمة بالذكاء الاصطناعي [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى لتحقيق الدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو معلومات غير دقيقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الرسمي. للحصول على معلومات حاسمة، يُوصى بالاستعانة بترجمة بشرية احترافية. نحن غير مسؤولين عن أي سوء فهم أو تفسيرات خاطئة ناتجة عن استخدام هذه الترجمة.