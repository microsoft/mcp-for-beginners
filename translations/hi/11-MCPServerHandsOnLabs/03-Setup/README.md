# पर्यावरण सेटअप

## 🎯 यह लैब क्या कवर करता है

यह हैंड्स-ऑन लैब आपको PostgreSQL इंटीग्रेशन के साथ MCP सर्वर बनाने के लिए एक संपूर्ण विकास पर्यावरण सेटअप करने के लिए मार्गदर्शन करता है। आप सभी आवश्यक टूल्स को कॉन्फ़िगर करेंगे, Azure संसाधनों को डिप्लॉय करेंगे, और कार्यान्वयन से पहले अपने सेटअप को सत्यापित करेंगे।

## अवलोकन

एक उचित विकास पर्यावरण MCP सर्वर विकास की सफलता के लिए महत्वपूर्ण है। यह लैब आपको Docker, Azure सेवाओं, विकास टूल्स को सेटअप करने और यह सुनिश्चित करने के लिए चरण-दर-चरण निर्देश प्रदान करता है कि सब कुछ सही ढंग से काम कर रहा है।

इस लैब के अंत तक, आपके पास Zava Retail MCP सर्वर बनाने के लिए पूरी तरह से कार्यात्मक विकास पर्यावरण होगा।

## सीखने के उद्देश्य

इस लैब के अंत तक, आप सक्षम होंगे:

- **सभी आवश्यक विकास टूल्स को इंस्टॉल और कॉन्फ़िगर करें**  
- **MCP सर्वर के लिए आवश्यक Azure संसाधनों को डिप्लॉय करें**  
- **PostgreSQL और MCP सर्वर के लिए Docker कंटेनर सेट करें**  
- **अपने पर्यावरण सेटअप को टेस्ट कनेक्शन के साथ सत्यापित करें**  
- **आम सेटअप समस्याओं और कॉन्फ़िगरेशन मुद्दों का समाधान करें**  
- **विकास वर्कफ़्लो और फ़ाइल संरचना को समझें**  

## 📋 पूर्वापेक्षाएँ जांचें

शुरू करने से पहले, सुनिश्चित करें कि आपके पास निम्नलिखित हैं:

### आवश्यक ज्ञान
- बेसिक कमांड लाइन उपयोग (Windows Command Prompt/PowerShell)  
- पर्यावरण वेरिएबल्स की समझ  
- Git वर्जन कंट्रोल की जानकारी  
- Docker के बेसिक कॉन्सेप्ट्स (कंटेनर, इमेज, वॉल्यूम)  

### सिस्टम आवश्यकताएँ
- **ऑपरेटिंग सिस्टम**: Windows 10/11, macOS, या Linux  
- **RAM**: न्यूनतम 8GB (16GB अनुशंसित)  
- **स्टोरेज**: कम से कम 10GB खाली स्थान  
- **नेटवर्क**: डाउनलोड और Azure डिप्लॉयमेंट के लिए इंटरनेट कनेक्शन  

### खाता आवश्यकताएँ
- **Azure सब्सक्रिप्शन**: फ्री टियर पर्याप्त है  
- **GitHub खाता**: रिपॉजिटरी एक्सेस के लिए  
- **Docker Hub खाता**: (वैकल्पिक) कस्टम इमेज पब्लिशिंग के लिए  

## 🛠️ टूल इंस्टॉलेशन

### 1. Docker Desktop इंस्टॉल करें

Docker हमारे विकास सेटअप के लिए कंटेनराइज्ड पर्यावरण प्रदान करता है।

#### Windows इंस्टॉलेशन

1. **Docker Desktop डाउनलोड करें**:  
   ```cmd
   # Visit https://desktop.docker.com/win/stable/Docker%20Desktop%20Installer.exe
   # Or use Windows Package Manager
   winget install Docker.DockerDesktop
   ```
  
2. **इंस्टॉल और कॉन्फ़िगर करें**:  
   - इंस्टॉलर को एडमिनिस्ट्रेटर के रूप में चलाएं  
   - WSL 2 इंटीग्रेशन को सक्षम करें जब संकेत दिया जाए  
   - इंस्टॉलेशन पूरा होने पर अपने कंप्यूटर को पुनः शुरू करें  

3. **इंस्टॉलेशन सत्यापित करें**:  
   ```cmd
   docker --version
   docker-compose --version
   ```
  

#### macOS इंस्टॉलेशन

1. **डाउनलोड और इंस्टॉल करें**:  
   ```bash
   # Download from https://desktop.docker.com/mac/stable/Docker.dmg
   # Or use Homebrew
   brew install --cask docker
   ```
  
2. **Docker Desktop शुरू करें**:  
   - Applications से Docker Desktop लॉन्च करें  
   - प्रारंभिक सेटअप विज़ार्ड पूरा करें  

3. **इंस्टॉलेशन सत्यापित करें**:  
   ```bash
   docker --version
   docker-compose --version
   ```
  

#### Linux इंस्टॉलेशन

1. **Docker Engine इंस्टॉल करें**:  
   ```bash
   # Ubuntu/Debian
   curl -fsSL https://get.docker.com -o get-docker.sh
   sudo sh get-docker.sh
   sudo usermod -aG docker $USER
   
   # Log out and back in for group changes to take effect
   ```
  
2. **Docker Compose इंस्टॉल करें**:  
   ```bash
   sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
   sudo chmod +x /usr/local/bin/docker-compose
   ```
  

### 2. Azure CLI इंस्टॉल करें

Azure CLI Azure संसाधनों की तैनाती और प्रबंधन को सक्षम करता है।

#### Windows इंस्टॉलेशन

```cmd
# Using Windows Package Manager
winget install Microsoft.AzureCLI

# Or download MSI from: https://aka.ms/installazurecliwindows
```
  

#### macOS इंस्टॉलेशन

```bash
# Using Homebrew
brew install azure-cli

# Or using installer
curl -L https://aka.ms/InstallAzureCli | bash
```
  

#### Linux इंस्टॉलेशन

```bash
# Ubuntu/Debian
curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash

# RHEL/CentOS
sudo rpm --import https://packages.microsoft.com/keys/microsoft.asc
sudo dnf install azure-cli
```
  

#### सत्यापित करें और प्रमाणित करें

```bash
# Check installation
az version

# Login to Azure
az login

# Set default subscription (if you have multiple)
az account list --output table
az account set --subscription "Your-Subscription-Name"
```
  

### 3. Git इंस्टॉल करें

Git रिपॉजिटरी क्लोनिंग और वर्जन कंट्रोल के लिए आवश्यक है।

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
  

### 4. VS Code इंस्टॉल करें

Visual Studio Code MCP समर्थन के साथ एकीकृत विकास पर्यावरण प्रदान करता है।

#### इंस्टॉलेशन

```cmd
# Windows
winget install Microsoft.VisualStudioCode

# macOS
brew install --cask visual-studio-code

# Linux (Ubuntu/Debian)
sudo snap install code --classic
```
  

#### आवश्यक एक्सटेंशन

इन VS Code एक्सटेंशन्स को इंस्टॉल करें:

```bash
# Install via command line
code --install-extension ms-python.python
code --install-extension ms-vscode.vscode-json
code --install-extension ms-azuretools.vscode-docker
code --install-extension ms-vscode.azure-account
```
  

या VS Code के माध्यम से इंस्टॉल करें:  
1. VS Code खोलें  
2. एक्सटेंशन्स पर जाएं (Ctrl+Shift+X)  
3. इंस्टॉल करें:  
   - **Python** (Microsoft)  
   - **Docker** (Microsoft)  
   - **Azure Account** (Microsoft)  
   - **JSON** (Microsoft)  

### 5. Python इंस्टॉल करें

MCP सर्वर विकास के लिए Python 3.8+ आवश्यक है।

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
  

#### इंस्टॉलेशन सत्यापित करें

```bash
python --version  # Should show Python 3.11.x
pip --version      # Should show pip version
```
  

## 🚀 प्रोजेक्ट सेटअप

### 1. रिपॉजिटरी क्लोन करें

```bash
# Clone the main repository
git clone https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail.git

# Navigate to the project directory
cd MCP-Server-and-PostgreSQL-Sample-Retail

# Verify repository structure
ls -la
```
  

### 2. Python वर्चुअल पर्यावरण बनाएं

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
  

### 3. Python डिपेंडेंसी इंस्टॉल करें

```bash
# Install development dependencies
pip install -r requirements.lock.txt

# Verify key packages
pip list | grep fastmcp
pip list | grep asyncpg
pip list | grep azure
```
  

## ☁️ Azure संसाधन तैनाती

### 1. संसाधन आवश्यकताओं को समझें

हमारे MCP सर्वर को इन Azure संसाधनों की आवश्यकता है:

| **संसाधन** | **उद्देश्य** | **अनुमानित लागत** |  
|------------|--------------|-------------------|  
| **Azure AI Foundry** | AI मॉडल होस्टिंग और प्रबंधन | $10-50/माह |  
| **OpenAI Deployment** | टेक्स्ट एम्बेडिंग मॉडल (text-embedding-3-small) | $5-20/माह |  
| **Application Insights** | मॉनिटरिंग और टेलीमेट्री | $5-15/माह |  
| **Resource Group** | संसाधन संगठन | मुफ्त |  

### 2. Azure संसाधन तैनात करें

#### विकल्प A: स्वचालित तैनाती (अनुशंसित)

```bash
# Navigate to infrastructure directory
cd infra

# Windows - PowerShell
./deploy.ps1

# macOS/Linux - Bash
./deploy.sh
```
  

डिप्लॉयमेंट स्क्रिप्ट निम्नलिखित करेगी:  
1. एक अद्वितीय संसाधन समूह बनाएगी  
2. Azure AI Foundry संसाधनों को तैनात करेगी  
3. text-embedding-3-small मॉडल को तैनात करेगी  
4. Application Insights को कॉन्फ़िगर करेगी  
5. प्रमाणीकरण के लिए एक सेवा प्रिंसिपल बनाएगी  
6. `.env` फ़ाइल को कॉन्फ़िगरेशन के साथ उत्पन्न करेगी  

#### विकल्प B: मैनुअल तैनाती

यदि आप मैनुअल नियंत्रण पसंद करते हैं या स्वचालित स्क्रिप्ट विफल होती है:

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
  

### 3. Azure तैनाती सत्यापित करें

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
  

### 4. पर्यावरण वेरिएबल्स कॉन्फ़िगर करें

तैनाती के बाद, आपके पास एक `.env` फ़ाइल होनी चाहिए। सत्यापित करें कि इसमें निम्नलिखित हैं:

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
  

## 🐳 Docker पर्यावरण सेटअप

### 1. Docker संरचना को समझें

हमारा विकास पर्यावरण Docker Compose का उपयोग करता है:

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
  

### 2. विकास पर्यावरण शुरू करें

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
  

### 3. डेटाबेस सेटअप सत्यापित करें

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
  

### 4. MCP सर्वर टेस्ट करें

```bash
# Check MCP server health
curl http://localhost:8000/health

# Test basic MCP endpoint
curl -X POST http://localhost:8000/mcp \
  -H "Content-Type: application/json" \
  -H "x-rls-user-id: 00000000-0000-0000-0000-000000000000" \
  -d '{"method": "tools/list", "params": {}}'
```
  

## 🔧 VS Code कॉन्फ़िगरेशन

### 1. MCP इंटीग्रेशन कॉन्फ़िगर करें

VS Code MCP कॉन्फ़िगरेशन बनाएं:

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
  

### 2. Python पर्यावरण कॉन्फ़िगर करें

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
  

### 3. VS Code इंटीग्रेशन टेस्ट करें

1. **प्रोजेक्ट को VS Code में खोलें**:  
   ```bash
   code .
   ```
  

2. **AI चैट खोलें**:  
   - `Ctrl+Shift+P` (Windows/Linux) या `Cmd+Shift+P` (macOS) दबाएं  
   - "AI Chat" टाइप करें और "AI Chat: Open Chat" चुनें  

3. **MCP सर्वर कनेक्शन टेस्ट करें**:  
   - AI चैट में, `#zava` टाइप करें और कॉन्फ़िगर किए गए सर्वरों में से एक चुनें  
   - पूछें: "डेटाबेस में कौन-कौन सी टेबल्स उपलब्ध हैं?"  
   - आपको रिटेल डेटाबेस टेबल्स की सूची प्राप्त होनी चाहिए  

## ✅ पर्यावरण सत्यापन

### 1. व्यापक सिस्टम जांच

अपने सेटअप को सत्यापित करने के लिए यह सत्यापन स्क्रिप्ट चलाएं:

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
  

### 2. मैनुअल सत्यापन चेकलिस्ट

**✅ बेसिक टूल्स**  
- [ ] Docker संस्करण 20.10+ इंस्टॉल और चल रहा है  
- [ ] Azure CLI 2.40+ इंस्टॉल और प्रमाणित  
- [ ] Python 3.8+ pip के साथ इंस्टॉल  
- [ ] Git 2.30+ इंस्टॉल  
- [ ] VS Code आवश्यक एक्सटेंशन्स के साथ  

**✅ Azure संसाधन**  
- [ ] संसाधन समूह सफलतापूर्वक बनाया गया  
- [ ] AI Foundry प्रोजेक्ट तैनात  
- [ ] OpenAI text-embedding-3-small मॉडल तैनात  
- [ ] Application Insights कॉन्फ़िगर किया गया  
- [ ] सेवा प्रिंसिपल उचित अनुमतियों के साथ बनाया गया  

**✅ पर्यावरण कॉन्फ़िगरेशन**  
- [ ] `.env` फ़ाइल सभी आवश्यक वेरिएबल्स के साथ बनाई गई  
- [ ] Azure क्रेडेंशियल्स काम कर रहे हैं (`az account show` के साथ टेस्ट करें)  
- [ ] PostgreSQL कंटेनर चल रहा है और सुलभ है  
- [ ] डेटाबेस में सैंपल डेटा लोड किया गया  

**✅ VS Code इंटीग्रेशन**  
- [ ] `.vscode/mcp.json` कॉन्फ़िगर किया गया  
- [ ] Python इंटरप्रेटर वर्चुअल पर्यावरण पर सेट  
- [ ] MCP सर्वर AI चैट में दिखाई दे रहे हैं  
- [ ] AI चैट के माध्यम से टेस्ट क्वेरीज़ निष्पादित कर सकते हैं  

## 🛠️ सामान्य समस्याओं का समाधान

### Docker समस्याएँ

**समस्या**: Docker कंटेनर शुरू नहीं हो रहे  
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
  

**समस्या**: PostgreSQL कनेक्शन विफल  
```bash
# Check container logs
docker-compose logs postgres

# Verify container is healthy
docker-compose ps

# Test direct connection
docker-compose exec postgres psql -U postgres -d zava -c "SELECT 1;"
```
  

### Azure तैनाती समस्याएँ

**समस्या**: Azure तैनाती विफल  
```bash
# Check Azure CLI authentication
az account show

# Verify subscription permissions
az role assignment list --assignee $(az account show --query user.name -o tsv)

# Check resource provider registration
az provider register --namespace Microsoft.CognitiveServices
az provider register --namespace Microsoft.Insights
```
  

**समस्या**: AI सेवा प्रमाणीकरण विफल  
```bash
# Test service principal
az login --service-principal \
  --username $AZURE_CLIENT_ID \
  --password $AZURE_CLIENT_SECRET \
  --tenant $AZURE_TENANT_ID

# Verify AI service deployment
az cognitiveservices account list --query "[].{Name:name,Kind:kind,Location:location}"
```
  

### Python पर्यावरण समस्याएँ

**समस्या**: पैकेज इंस्टॉलेशन विफल  
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
  

**समस्या**: VS Code Python इंटरप्रेटर नहीं ढूंढ सकता  
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
  

## 🎯 मुख्य बातें

इस लैब को पूरा करने के बाद, आपके पास होगा:

✅ **पूर्ण विकास पर्यावरण**: सभी टूल्स इंस्टॉल और कॉन्फ़िगर  
✅ **Azure संसाधन तैनात**: AI सेवाएँ और सहायक इन्फ्रास्ट्रक्चर  
✅ **Docker पर्यावरण चालू**: PostgreSQL और MCP सर्वर कंटेनर  
✅ **VS Code इंटीग्रेशन**: MCP सर्वर कॉन्फ़िगर और सुलभ  
✅ **सत्यापित सेटअप**: सभी घटक परीक्षण और एक साथ काम कर रहे  
✅ **समस्या समाधान ज्ञान**: सामान्य समस्याएँ और समाधान  

## 🚀 आगे क्या करें

अपने पर्यावरण को तैयार करने के बाद, **[लैब 04: डेटाबेस डिज़ाइन और स्कीमा](../04-Database/README.md)** के साथ जारी रखें:

- रिटेल डेटाबेस स्कीमा का विस्तार से अन्वेषण करें  
- मल्टी-टेनेंट डेटा मॉडलिंग को समझें  
- Row Level Security कार्यान्वयन के बारे में जानें  
- सैंपल रिटेल डेटा के साथ काम करें  

## 📚 अतिरिक्त संसाधन

### विकास टूल्स
- [Docker डाक्यूमेंटेशन](https://docs.docker.com/) - संपूर्ण Docker संदर्भ  
- [Azure CLI संदर्भ](https://docs.microsoft.com/cli/azure/) - Azure CLI कमांड्स  
- [VS Code डाक्यूमेंटेशन](https://code.visualstudio.com/docs) - संपादक कॉन्फ़िगरेशन और एक्सटेंशन्स  

### Azure सेवाएँ
- [Azure AI Foundry डाक्यूमेंटेशन](https://docs.microsoft.com/azure/ai-foundry/) - AI सेवा कॉन्फ़िगरेशन  
- [Azure OpenAI सेवा](https://docs.microsoft.com/azure/cognitive-services/openai/) - AI मॉडल तैनाती  
- [Application Insights](https://docs.microsoft.com/azure/azure-monitor/app/app-insights-overview) - मॉनिटरिंग सेटअप  

### Python विकास
- [Python वर्चुअल पर्यावरण](https://docs.python.org/3/tutorial/venv.html) - पर्यावरण प्रबंधन  
- [AsyncIO डाक्यूमेंटेशन](https://docs.python.org/3/library/asyncio.html) - Async प्रोग्रामिंग पैटर्न  
- [FastAPI डाक्यूमेंटेशन](https://fastapi.tiangolo.com/) - वेब फ्रेमवर्क पैटर्न  

---

**आगे**: पर्यावरण तैयार है? [लैब 04: डेटाबेस डिज़ाइन और स्कीमा](../04-Database/README.md) के साथ जारी रखें।  

---

**अस्वीकरण**:  
यह दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके अनुवादित किया गया है। जबकि हम सटीकता के लिए प्रयास करते हैं, कृपया ध्यान दें कि स्वचालित अनुवाद में त्रुटियां या अशुद्धियां हो सकती हैं। मूल भाषा में उपलब्ध मूल दस्तावेज़ को आधिकारिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सिफारिश की जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम उत्तरदायी नहीं हैं।