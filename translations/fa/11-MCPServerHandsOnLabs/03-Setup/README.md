# تنظیم محیط

## 🎯 این آزمایش چه چیزی را پوشش می‌دهد؟

این آزمایش عملی شما را در تنظیم یک محیط توسعه کامل برای ساخت سرورهای MCP با یکپارچه‌سازی PostgreSQL راهنمایی می‌کند. شما ابزارهای لازم را پیکربندی می‌کنید، منابع Azure را مستقر می‌کنید و تنظیمات خود را قبل از ادامه پیاده‌سازی اعتبارسنجی می‌کنید.

## نمای کلی

یک محیط توسعه مناسب برای موفقیت در توسعه سرور MCP ضروری است. این آزمایش دستورالعمل‌های گام‌به‌گام برای تنظیم Docker، خدمات Azure، ابزارهای توسعه و اعتبارسنجی اینکه همه چیز به درستی با هم کار می‌کند را ارائه می‌دهد.

در پایان این آزمایش، شما یک محیط توسعه کاملاً عملیاتی برای ساخت سرور MCP خرده‌فروشی Zava خواهید داشت.

## اهداف یادگیری

در پایان این آزمایش، شما قادر خواهید بود:

- **نصب و پیکربندی** تمام ابزارهای توسعه مورد نیاز  
- **استقرار منابع Azure** مورد نیاز برای سرور MCP  
- **راه‌اندازی کانتینرهای Docker** برای PostgreSQL و سرور MCP  
- **اعتبارسنجی** تنظیمات محیط خود با اتصالات آزمایشی  
- **رفع مشکلات** رایج تنظیمات و مشکلات پیکربندی  
- **درک** جریان کاری توسعه و ساختار فایل  

## 📋 بررسی پیش‌نیازها

قبل از شروع، مطمئن شوید که موارد زیر را دارید:

### دانش مورد نیاز
- استفاده پایه از خط فرمان (Windows Command Prompt/PowerShell)  
- درک متغیرهای محیطی  
- آشنایی با کنترل نسخه Git  
- مفاهیم پایه Docker (کانتینرها، تصاویر، حجم‌ها)  

### الزامات سیستم
- **سیستم عامل**: Windows 10/11، macOS یا Linux  
- **رم**: حداقل 8GB (16GB توصیه می‌شود)  
- **فضای ذخیره‌سازی**: حداقل 10GB فضای آزاد  
- **شبکه**: اتصال اینترنت برای دانلودها و استقرار Azure  

### الزامات حساب کاربری
- **اشتراک Azure**: سطح رایگان کافی است  
- **حساب GitHub**: برای دسترسی به مخزن  
- **حساب Docker Hub**: (اختیاری) برای انتشار تصویر سفارشی  

## 🛠️ نصب ابزارها

### 1. نصب Docker Desktop

Docker محیط کانتینری شده برای تنظیمات توسعه ما را فراهم می‌کند.

#### نصب در ویندوز

1. **دانلود Docker Desktop**:  
   ```cmd
   # Visit https://desktop.docker.com/win/stable/Docker%20Desktop%20Installer.exe
   # Or use Windows Package Manager
   winget install Docker.DockerDesktop
   ```
  
2. **نصب و پیکربندی**:  
   - نصب‌کننده را به عنوان Administrator اجرا کنید  
   - هنگام درخواست، یکپارچه‌سازی WSL 2 را فعال کنید  
   - پس از اتمام نصب، کامپیوتر خود را مجدداً راه‌اندازی کنید  

3. **تأیید نصب**:  
   ```cmd
   docker --version
   docker-compose --version
   ```
  

#### نصب در macOS

1. **دانلود و نصب**:  
   ```bash
   # Download from https://desktop.docker.com/mac/stable/Docker.dmg
   # Or use Homebrew
   brew install --cask docker
   ```
  
2. **راه‌اندازی Docker Desktop**:  
   - Docker Desktop را از Applications اجرا کنید  
   - جادوگر تنظیم اولیه را کامل کنید  

3. **تأیید نصب**:  
   ```bash
   docker --version
   docker-compose --version
   ```
  

#### نصب در لینوکس

1. **نصب Docker Engine**:  
   ```bash
   # Ubuntu/Debian
   curl -fsSL https://get.docker.com -o get-docker.sh
   sudo sh get-docker.sh
   sudo usermod -aG docker $USER
   
   # Log out and back in for group changes to take effect
   ```
  
2. **نصب Docker Compose**:  
   ```bash
   sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
   sudo chmod +x /usr/local/bin/docker-compose
   ```
  

### 2. نصب Azure CLI

Azure CLI امکان استقرار و مدیریت منابع Azure را فراهم می‌کند.

#### نصب در ویندوز

```cmd
# Using Windows Package Manager
winget install Microsoft.AzureCLI

# Or download MSI from: https://aka.ms/installazurecliwindows
```
  

#### نصب در macOS

```bash
# Using Homebrew
brew install azure-cli

# Or using installer
curl -L https://aka.ms/InstallAzureCli | bash
```
  

#### نصب در لینوکس

```bash
# Ubuntu/Debian
curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash

# RHEL/CentOS
sudo rpm --import https://packages.microsoft.com/keys/microsoft.asc
sudo dnf install azure-cli
```
  

#### تأیید و احراز هویت

```bash
# Check installation
az version

# Login to Azure
az login

# Set default subscription (if you have multiple)
az account list --output table
az account set --subscription "Your-Subscription-Name"
```
  

### 3. نصب Git

Git برای کلون کردن مخزن و کنترل نسخه مورد نیاز است.

#### ویندوز

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
  

#### لینوکس

```bash
# Ubuntu/Debian
sudo apt update && sudo apt install git

# RHEL/CentOS
sudo dnf install git
```
  

### 4. نصب VS Code

Visual Studio Code محیط توسعه یکپارچه با پشتیبانی MCP را فراهم می‌کند.

#### نصب

```cmd
# Windows
winget install Microsoft.VisualStudioCode

# macOS
brew install --cask visual-studio-code

# Linux (Ubuntu/Debian)
sudo snap install code --classic
```
  

#### افزونه‌های مورد نیاز

این افزونه‌های VS Code را نصب کنید:

```bash
# Install via command line
code --install-extension ms-python.python
code --install-extension ms-vscode.vscode-json
code --install-extension ms-azuretools.vscode-docker
code --install-extension ms-vscode.azure-account
```
  
یا از طریق VS Code نصب کنید:  
1. VS Code را باز کنید  
2. به Extensions بروید (Ctrl+Shift+X)  
3. نصب کنید:  
   - **Python** (Microsoft)  
   - **Docker** (Microsoft)  
   - **Azure Account** (Microsoft)  
   - **JSON** (Microsoft)  

### 5. نصب Python

Python 3.8+ برای توسعه سرور MCP مورد نیاز است.

#### ویندوز

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
  

#### لینوکس

```bash
# Ubuntu/Debian
sudo apt update && sudo apt install python3.11 python3.11-pip python3.11-venv

# RHEL/CentOS
sudo dnf install python3.11 python3.11-pip
```
  

#### تأیید نصب

```bash
python --version  # Should show Python 3.11.x
pip --version      # Should show pip version
```
  

## 🚀 تنظیم پروژه

### 1. کلون کردن مخزن

```bash
# Clone the main repository
git clone https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail.git

# Navigate to the project directory
cd MCP-Server-and-PostgreSQL-Sample-Retail

# Verify repository structure
ls -la
```
  

### 2. ایجاد محیط مجازی Python

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
  

### 3. نصب وابستگی‌های Python

```bash
# Install development dependencies
pip install -r requirements.lock.txt

# Verify key packages
pip list | grep fastmcp
pip list | grep asyncpg
pip list | grep azure
```
  

## ☁️ استقرار منابع Azure

### 1. درک الزامات منابع

سرور MCP ما به این منابع Azure نیاز دارد:

| **منبع** | **هدف** | **هزینه تخمینی** |  
|----------|---------|------------------|  
| **Azure AI Foundry** | میزبانی و مدیریت مدل‌های AI | $10-50/ماه |  
| **استقرار OpenAI** | مدل جاسازی متن (text-embedding-3-small) | $5-20/ماه |  
| **Application Insights** | نظارت و تله‌متری | $5-15/ماه |  
| **Resource Group** | سازماندهی منابع | رایگان |  

### 2. استقرار منابع Azure

#### گزینه A: استقرار خودکار (توصیه‌شده)

```bash
# Navigate to infrastructure directory
cd infra

# Windows - PowerShell
./deploy.ps1

# macOS/Linux - Bash
./deploy.sh
```
  
اسکریپت استقرار موارد زیر را انجام می‌دهد:  
1. ایجاد یک گروه منابع منحصر به فرد  
2. استقرار منابع Azure AI Foundry  
3. استقرار مدل text-embedding-3-small  
4. پیکربندی Application Insights  
5. ایجاد یک سرویس اصلی برای احراز هویت  
6. تولید فایل `.env` با پیکربندی  

#### گزینه B: استقرار دستی

اگر کنترل دستی را ترجیح می‌دهید یا اسکریپت خودکار شکست می‌خورد:

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
  

### 3. تأیید استقرار Azure

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
  

### 4. پیکربندی متغیرهای محیطی

پس از استقرار، باید یک فایل `.env` داشته باشید. تأیید کنید که شامل موارد زیر است:

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
  

## 🐳 تنظیم محیط Docker

### 1. درک ترکیب Docker

محیط توسعه ما از Docker Compose استفاده می‌کند:

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
  

### 2. راه‌اندازی محیط توسعه

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
  

### 3. تأیید تنظیم پایگاه داده

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
  

### 4. آزمایش سرور MCP

```bash
# Check MCP server health
curl http://localhost:8000/health

# Test basic MCP endpoint
curl -X POST http://localhost:8000/mcp \
  -H "Content-Type: application/json" \
  -H "x-rls-user-id: 00000000-0000-0000-0000-000000000000" \
  -d '{"method": "tools/list", "params": {}}'
```
  

## 🔧 پیکربندی VS Code

### 1. پیکربندی یکپارچه‌سازی MCP

ایجاد پیکربندی MCP در VS Code:

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
  

### 2. پیکربندی محیط Python

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
  

### 3. آزمایش یکپارچه‌سازی VS Code

1. **باز کردن پروژه در VS Code**:  
   ```bash
   code .
   ```
  
2. **باز کردن AI Chat**:  
   - `Ctrl+Shift+P` (ویندوز/لینوکس) یا `Cmd+Shift+P` (macOS) را فشار دهید  
   - "AI Chat" را تایپ کنید و "AI Chat: Open Chat" را انتخاب کنید  

3. **آزمایش اتصال سرور MCP**:  
   - در AI Chat، `#zava` را تایپ کنید و یکی از سرورهای پیکربندی شده را انتخاب کنید  
   - بپرسید: "چه جدول‌هایی در پایگاه داده موجود هستند؟"  
   - باید پاسخی دریافت کنید که جدول‌های پایگاه داده خرده‌فروشی را فهرست می‌کند  

## ✅ اعتبارسنجی محیط

### 1. بررسی جامع سیستم

این اسکریپت اعتبارسنجی را اجرا کنید تا تنظیمات خود را تأیید کنید:

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
  

### 2. چک‌لیست اعتبارسنجی دستی

**✅ ابزارهای پایه**  
- [ ] نسخه Docker 20.10+ نصب شده و در حال اجرا  
- [ ] Azure CLI 2.40+ نصب شده و احراز هویت شده  
- [ ] Python 3.8+ با pip نصب شده  
- [ ] Git 2.30+ نصب شده  
- [ ] VS Code با افزونه‌های مورد نیاز  

**✅ منابع Azure**  
- [ ] گروه منابع با موفقیت ایجاد شده  
- [ ] پروژه AI Foundry مستقر شده  
- [ ] مدل text-embedding-3-small مستقر شده  
- [ ] Application Insights پیکربندی شده  
- [ ] سرویس اصلی با مجوزهای مناسب ایجاد شده  

**✅ پیکربندی محیط**  
- [ ] فایل `.env` با تمام متغیرهای مورد نیاز ایجاد شده  
- [ ] اعتبارنامه‌های Azure کار می‌کنند (آزمایش با `az account show`)  
- [ ] کانتینر PostgreSQL در حال اجرا و قابل دسترسی  
- [ ] داده‌های نمونه در پایگاه داده بارگذاری شده  

**✅ یکپارچه‌سازی VS Code**  
- [ ] فایل `.vscode/mcp.json` پیکربندی شده  
- [ ] مفسر Python به محیط مجازی تنظیم شده  
- [ ] سرورهای MCP در AI Chat ظاهر می‌شوند  
- [ ] می‌توان پرسش‌های آزمایشی را از طریق AI Chat اجرا کرد  

## 🛠️ رفع مشکلات رایج

### مشکلات Docker

**مشکل**: کانتینرهای Docker شروع نمی‌شوند  
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
  
**مشکل**: اتصال PostgreSQL شکست می‌خورد  
```bash
# Check container logs
docker-compose logs postgres

# Verify container is healthy
docker-compose ps

# Test direct connection
docker-compose exec postgres psql -U postgres -d zava -c "SELECT 1;"
```
  

### مشکلات استقرار Azure

**مشکل**: استقرار Azure شکست می‌خورد  
```bash
# Check Azure CLI authentication
az account show

# Verify subscription permissions
az role assignment list --assignee $(az account show --query user.name -o tsv)

# Check resource provider registration
az provider register --namespace Microsoft.CognitiveServices
az provider register --namespace Microsoft.Insights
```
  
**مشکل**: احراز هویت سرویس AI شکست می‌خورد  
```bash
# Test service principal
az login --service-principal \
  --username $AZURE_CLIENT_ID \
  --password $AZURE_CLIENT_SECRET \
  --tenant $AZURE_TENANT_ID

# Verify AI service deployment
az cognitiveservices account list --query "[].{Name:name,Kind:kind,Location:location}"
```
  

### مشکلات محیط Python

**مشکل**: نصب بسته‌ها شکست می‌خورد  
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
  
**مشکل**: VS Code نمی‌تواند مفسر Python را پیدا کند  
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
  

## 🎯 نکات کلیدی

پس از تکمیل این آزمایش، شما باید داشته باشید:

✅ **محیط توسعه کامل**: تمام ابزارها نصب و پیکربندی شده‌اند  
✅ **منابع Azure مستقر شده**: خدمات AI و زیرساخت‌های پشتیبانی‌کننده  
✅ **محیط Docker در حال اجرا**: کانتینرهای PostgreSQL و سرور MCP  
✅ **یکپارچه‌سازی VS Code**: سرورهای MCP پیکربندی شده و قابل دسترسی  
✅ **تنظیمات اعتبارسنجی شده**: تمام اجزا آزمایش شده و با هم کار می‌کنند  
✅ **دانش رفع مشکلات**: مشکلات رایج و راه‌حل‌ها  

## 🚀 مرحله بعدی

با آماده بودن محیط خود، ادامه دهید به **[آزمایش 04: طراحی پایگاه داده و طرح‌واره](../04-Database/README.md)** برای:

- بررسی جزئیات طرح‌واره پایگاه داده خرده‌فروشی  
- درک مدل‌سازی داده‌های چند مستأجری  
- یادگیری پیاده‌سازی امنیت سطح ردیف  
- کار با داده‌های نمونه خرده‌فروشی  

## 📚 منابع اضافی

### ابزارهای توسعه
- [مستندات Docker](https://docs.docker.com/) - مرجع کامل Docker  
- [مرجع Azure CLI](https://docs.microsoft.com/cli/azure/) - دستورات Azure CLI  
- [مستندات VS Code](https://code.visualstudio.com/docs) - پیکربندی و افزونه‌های ویرایشگر  

### خدمات Azure
- [مستندات Azure AI Foundry](https://docs.microsoft.com/azure/ai-foundry/) - پیکربندی خدمات AI  
- [سرویس Azure OpenAI](https://docs.microsoft.com/azure/cognitive-services/openai/) - استقرار مدل AI  
- [Application Insights](https://docs.microsoft.com/azure/azure-monitor/app/app-insights-overview) - تنظیم نظارت  

### توسعه Python
- [محیط‌های مجازی Python](https://docs.python.org/3/tutorial/venv.html) - مدیریت محیط  
- [مستندات AsyncIO](https://docs.python.org/3/library/asyncio.html) - الگوهای برنامه‌نویسی Async  
- [مستندات FastAPI](https://fastapi.tiangolo.com/) - الگوهای چارچوب وب  

---

**مرحله بعدی**: محیط آماده است؟ ادامه دهید با [آزمایش 04: طراحی پایگاه داده و طرح‌واره](../04-Database/README.md)

---

**سلب مسئولیت**:  
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما تلاش می‌کنیم دقت را حفظ کنیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است شامل خطاها یا نادرستی‌ها باشند. سند اصلی به زبان اصلی آن باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حساس، توصیه می‌شود از ترجمه انسانی حرفه‌ای استفاده کنید. ما مسئولیتی در قبال سوء تفاهم‌ها یا تفسیرهای نادرست ناشی از استفاده از این ترجمه نداریم.