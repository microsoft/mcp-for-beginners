# पर्यावरण सेटअप

## 🎯 हे प्रयोगशाळा काय कव्हर करते

ही हाताळणी प्रयोगशाळा तुम्हाला PostgreSQL एकत्रीकरणासह MCP सर्व्हर तयार करण्यासाठी संपूर्ण विकास पर्यावरण सेटअप करण्यासाठी मार्गदर्शन करते. तुम्ही सर्व आवश्यक साधने कॉन्फिगर कराल, Azure संसाधने तैनात कराल आणि अंमलबजावणी सुरू करण्यापूर्वी तुमचा सेटअप सत्यापित कराल.

## विहंगावलोकन

यशस्वी MCP सर्व्हर विकासासाठी योग्य विकास पर्यावरण महत्त्वाचे आहे. ही प्रयोगशाळा तुम्हाला Docker, Azure सेवा, विकास साधने सेटअप करण्यासाठी आणि सर्वकाही योग्य प्रकारे एकत्र कार्य करत असल्याचे सत्यापित करण्यासाठी चरण-दर-चरण सूचना प्रदान करते.

या प्रयोगशाळेच्या शेवटी, तुम्हाला Zava Retail MCP सर्व्हर तयार करण्यासाठी पूर्णपणे कार्यशील विकास पर्यावरण तयार असेल.

## शिकण्याची उद्दिष्टे

या प्रयोगशाळेच्या शेवटी, तुम्ही खालील गोष्टी करण्यात सक्षम असाल:

- **सर्व आवश्यक विकास साधने स्थापित आणि कॉन्फिगर करा**
- **MCP सर्व्हरसाठी आवश्यक Azure संसाधने तैनात करा**
- **PostgreSQL आणि MCP सर्व्हरसाठी Docker कंटेनर सेट करा**
- **तुमच्या पर्यावरण सेटअपची चाचणी कनेक्शनसह सत्यापित करा**
- **सामान्य सेटअप समस्या आणि कॉन्फिगरेशन समस्यांचे निराकरण करा**
- **विकास कार्यप्रवाह आणि फाइल संरचना समजून घ्या**

## 📋 पूर्वतयारी तपासणी

सुरुवात करण्यापूर्वी, खात्री करा की तुम्हाला खालील गोष्टी माहित आहेत:

### आवश्यक ज्ञान
- बेसिक कमांड लाइन वापर (Windows Command Prompt/PowerShell)
- पर्यावरणीय व्हेरिएबल्सची समज
- Git व्हर्जन कंट्रोलची ओळख
- बेसिक Docker संकल्पना (कंटेनर, इमेजेस, व्हॉल्यूम्स)

### सिस्टम आवश्यकता
- **ऑपरेटिंग सिस्टम**: Windows 10/11, macOS, किंवा Linux
- **RAM**: किमान 8GB (16GB शिफारस केलेले)
- **स्टोरेज**: किमान 10GB मोकळ्या जागा
- **नेटवर्क**: डाउनलोड आणि Azure तैनातीसाठी इंटरनेट कनेक्शन

### खाते आवश्यकता
- **Azure सदस्यता**: फ्री टियर पुरेसे आहे
- **GitHub खाते**: रेपॉजिटरी प्रवेशासाठी
- **Docker Hub खाते**: (पर्यायी) कस्टम इमेज प्रकाशित करण्यासाठी

## 🛠️ साधन स्थापना

### 1. Docker Desktop स्थापित करा

Docker आमच्या विकास सेटअपसाठी कंटेनराइज्ड पर्यावरण प्रदान करते.

#### Windows स्थापना

1. **Docker Desktop डाउनलोड करा**:
   ```cmd
   # Visit https://desktop.docker.com/win/stable/Docker%20Desktop%20Installer.exe
   # Or use Windows Package Manager
   winget install Docker.DockerDesktop
   ```

2. **स्थापना आणि कॉन्फिगर करा**:
   - इंस्टॉलर Administrator म्हणून चालवा
   - WSL 2 एकत्रीकरण सक्षम करा जेव्हा विचारले जाते
   - स्थापना पूर्ण झाल्यावर तुमचा संगणक रीस्टार्ट करा

3. **स्थापना सत्यापित करा**:
   ```cmd
   docker --version
   docker-compose --version
   ```

#### macOS स्थापना

1. **डाउनलोड आणि स्थापित करा**:
   ```bash
   # Download from https://desktop.docker.com/mac/stable/Docker.dmg
   # Or use Homebrew
   brew install --cask docker
   ```

2. **Docker Desktop सुरू करा**:
   - Applications मधून Docker Desktop लॉन्च करा
   - प्रारंभिक सेटअप विझार्ड पूर्ण करा

3. **स्थापना सत्यापित करा**:
   ```bash
   docker --version
   docker-compose --version
   ```

#### Linux स्थापना

1. **Docker Engine स्थापित करा**:
   ```bash
   # Ubuntu/Debian
   curl -fsSL https://get.docker.com -o get-docker.sh
   sudo sh get-docker.sh
   sudo usermod -aG docker $USER
   
   # Log out and back in for group changes to take effect
   ```

2. **Docker Compose स्थापित करा**:
   ```bash
   sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
   sudo chmod +x /usr/local/bin/docker-compose
   ```

### 2. Azure CLI स्थापित करा

Azure CLI Azure संसाधन तैनाती आणि व्यवस्थापन सक्षम करते.

#### Windows स्थापना

```cmd
# Using Windows Package Manager
winget install Microsoft.AzureCLI

# Or download MSI from: https://aka.ms/installazurecliwindows
```

#### macOS स्थापना

```bash
# Using Homebrew
brew install azure-cli

# Or using installer
curl -L https://aka.ms/InstallAzureCli | bash
```

#### Linux स्थापना

```bash
# Ubuntu/Debian
curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash

# RHEL/CentOS
sudo rpm --import https://packages.microsoft.com/keys/microsoft.asc
sudo dnf install azure-cli
```

#### सत्यापित करा आणि प्रमाणीकरण करा

```bash
# Check installation
az version

# Login to Azure
az login

# Set default subscription (if you have multiple)
az account list --output table
az account set --subscription "Your-Subscription-Name"
```

### 3. Git स्थापित करा

Git रेपॉजिटरी क्लोनिंग आणि व्हर्जन कंट्रोलसाठी आवश्यक आहे.

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

### 4. VS Code स्थापित करा

Visual Studio Code MCP समर्थनासह एकात्मिक विकास पर्यावरण प्रदान करते.

#### स्थापना

```cmd
# Windows
winget install Microsoft.VisualStudioCode

# macOS
brew install --cask visual-studio-code

# Linux (Ubuntu/Debian)
sudo snap install code --classic
```

#### आवश्यक विस्तार

हे VS Code विस्तार स्थापित करा:

```bash
# Install via command line
code --install-extension ms-python.python
code --install-extension ms-vscode.vscode-json
code --install-extension ms-azuretools.vscode-docker
code --install-extension ms-vscode.azure-account
```

किंवा VS Code द्वारे स्थापित करा:
1. VS Code उघडा
2. Extensions (Ctrl+Shift+X) वर जा
3. स्थापित करा:
   - **Python** (Microsoft)
   - **Docker** (Microsoft)
   - **Azure Account** (Microsoft)
   - **JSON** (Microsoft)

### 5. Python स्थापित करा

Python 3.8+ MCP सर्व्हर विकासासाठी आवश्यक आहे.

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

#### स्थापना सत्यापित करा

```bash
python --version  # Should show Python 3.11.x
pip --version      # Should show pip version
```

## 🚀 प्रकल्प सेटअप

### 1. रेपॉजिटरी क्लोन करा

```bash
# Clone the main repository
git clone https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail.git

# Navigate to the project directory
cd MCP-Server-and-PostgreSQL-Sample-Retail

# Verify repository structure
ls -la
```

### 2. Python व्हर्च्युअल पर्यावरण तयार करा

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

### 3. Python अवलंबित्व स्थापित करा

```bash
# Install development dependencies
pip install -r requirements.lock.txt

# Verify key packages
pip list | grep fastmcp
pip list | grep asyncpg
pip list | grep azure
```

## ☁️ Azure संसाधन तैनाती

### 1. संसाधन आवश्यकता समजून घ्या

आमच्या MCP सर्व्हरसाठी या Azure संसाधनांची आवश्यकता आहे:

| **संसाधन** | **उद्देश** | **अंदाजे खर्च** |
|--------------|-------------|-------------------|
| **Azure AI Foundry** | AI मॉडेल होस्टिंग आणि व्यवस्थापन | $10-50/महिना |
| **OpenAI तैनाती** | टेक्स्ट एम्बेडिंग मॉडेल (text-embedding-3-small) | $5-20/महिना |
| **Application Insights** | मॉनिटरिंग आणि टेलीमेट्री | $5-15/महिना |
| **Resource Group** | संसाधन संघटन | मोफत |

### 2. Azure संसाधने तैनात करा

#### पर्याय A: स्वयंचलित तैनाती (शिफारस केलेले)

```bash
# Navigate to infrastructure directory
cd infra

# Windows - PowerShell
./deploy.ps1

# macOS/Linux - Bash
./deploy.sh
```

तैनाती स्क्रिप्ट:
1. एक अद्वितीय संसाधन गट तयार करेल
2. Azure AI Foundry संसाधने तैनात करेल
3. text-embedding-3-small मॉडेल तैनात करेल
4. Application Insights कॉन्फिगर करेल
5. प्रमाणीकरणासाठी सेवा प्रमुख तयार करेल
6. `.env` फाइल तयार करेल ज्यामध्ये कॉन्फिगरेशन असेल

#### पर्याय B: मॅन्युअल तैनाती

जर तुम्हाला मॅन्युअल नियंत्रण हवे असेल किंवा स्वयंचलित स्क्रिप्ट अयशस्वी झाली असेल:

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

### 3. Azure तैनाती सत्यापित करा

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

### 4. पर्यावरणीय व्हेरिएबल्स कॉन्फिगर करा

तैनाती नंतर, तुमच्याकडे `.env` फाइल असावी. सत्यापित करा की त्यामध्ये खालील गोष्टी आहेत:

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

### 1. Docker रचना समजून घ्या

आमचे विकास पर्यावरण Docker Compose वापरते:

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

### 2. विकास पर्यावरण सुरू करा

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

### 3. डेटाबेस सेटअप सत्यापित करा

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

### 4. MCP सर्व्हर चाचणी करा

```bash
# Check MCP server health
curl http://localhost:8000/health

# Test basic MCP endpoint
curl -X POST http://localhost:8000/mcp \
  -H "Content-Type: application/json" \
  -H "x-rls-user-id: 00000000-0000-0000-0000-000000000000" \
  -d '{"method": "tools/list", "params": {}}'
```

## 🔧 VS Code कॉन्फिगरेशन

### 1. MCP एकत्रीकरण कॉन्फिगर करा

VS Code MCP कॉन्फिगरेशन तयार करा:

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

### 2. Python पर्यावरण कॉन्फिगर करा

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

### 3. VS Code एकत्रीकरण चाचणी करा

1. **प्रकल्प VS Code मध्ये उघडा**:
   ```bash
   code .
   ```

2. **AI Chat उघडा**:
   - `Ctrl+Shift+P` (Windows/Linux) किंवा `Cmd+Shift+P` (macOS) दाबा
   - "AI Chat" टाइप करा आणि "AI Chat: Open Chat" निवडा

3. **MCP सर्व्हर कनेक्शन चाचणी करा**:
   - AI Chat मध्ये, `#zava` टाइप करा आणि कॉन्फिगर केलेल्या सर्व्हरपैकी एक निवडा
   - विचारा: "डेटाबेसमध्ये कोणती टेबल्स उपलब्ध आहेत?"
   - तुम्हाला रिटेल डेटाबेस टेबल्सची यादी मिळेल

## ✅ पर्यावरण सत्यापन

### 1. सर्वसमावेशक सिस्टम तपासणी

तुमचा सेटअप सत्यापित करण्यासाठी हा सत्यापन स्क्रिप्ट चालवा:

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

### 2. मॅन्युअल सत्यापन चेकलिस्ट

**✅ मूलभूत साधने**
- [ ] Docker आवृत्ती 20.10+ स्थापित आणि चालू आहे
- [ ] Azure CLI 2.40+ स्थापित आणि प्रमाणीकरण केले आहे
- [ ] Python 3.8+ pip सह स्थापित आहे
- [ ] Git 2.30+ स्थापित आहे
- [ ] आवश्यक विस्तारांसह VS Code

**✅ Azure संसाधने**
- [ ] संसाधन गट यशस्वीरित्या तयार केला आहे
- [ ] AI Foundry प्रकल्प तैनात केला आहे
- [ ] OpenAI text-embedding-3-small मॉडेल तैनात केले आहे
- [ ] Application Insights कॉन्फिगर केले आहे
- [ ] योग्य परवानग्यांसह सेवा प्रमुख तयार केला आहे

**✅ पर्यावरण कॉन्फिगरेशन**
- [ ] `.env` फाइल तयार केली आहे ज्यामध्ये सर्व आवश्यक व्हेरिएबल्स आहेत
- [ ] Azure क्रेडेन्शियल्स कार्यरत आहेत (`az account show` सह चाचणी करा)
- [ ] PostgreSQL कंटेनर चालू आहे आणि प्रवेशयोग्य आहे
- [ ] डेटाबेसमध्ये नमुना डेटा लोड केला आहे

**✅ VS Code एकत्रीकरण**
- [ ] `.vscode/mcp.json` कॉन्फिगर केले आहे
- [ ] Python interpreter व्हर्च्युअल पर्यावरणावर सेट केले आहे
- [ ] MCP सर्व्हर AI Chat मध्ये दिसतात
- [ ] AI Chat द्वारे चाचणी क्वेरी चालवू शकता

## 🛠️ सामान्य समस्यांचे निराकरण

### Docker समस्या

**समस्या**: Docker कंटेनर सुरू होत नाहीत
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

**समस्या**: PostgreSQL कनेक्शन अयशस्वी
```bash
# Check container logs
docker-compose logs postgres

# Verify container is healthy
docker-compose ps

# Test direct connection
docker-compose exec postgres psql -U postgres -d zava -c "SELECT 1;"
```

### Azure तैनाती समस्या

**समस्या**: Azure तैनाती अयशस्वी
```bash
# Check Azure CLI authentication
az account show

# Verify subscription permissions
az role assignment list --assignee $(az account show --query user.name -o tsv)

# Check resource provider registration
az provider register --namespace Microsoft.CognitiveServices
az provider register --namespace Microsoft.Insights
```

**समस्या**: AI सेवा प्रमाणीकरण अयशस्वी
```bash
# Test service principal
az login --service-principal \
  --username $AZURE_CLIENT_ID \
  --password $AZURE_CLIENT_SECRET \
  --tenant $AZURE_TENANT_ID

# Verify AI service deployment
az cognitiveservices account list --query "[].{Name:name,Kind:kind,Location:location}"
```

### Python पर्यावरण समस्या

**समस्या**: पॅकेज स्थापना अयशस्वी
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

**समस्या**: VS Code Python interpreter शोधू शकत नाही
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

## 🎯 मुख्य मुद्दे

ही प्रयोगशाळा पूर्ण केल्यानंतर, तुम्ही खालील गोष्टी साध्य केल्या पाहिजेत:

✅ **पूर्ण विकास पर्यावरण**: सर्व साधने स्थापित आणि कॉन्फिगर केली  
✅ **Azure संसाधने तैनात केली**: AI सेवा आणि समर्थनात्मक पायाभूत सुविधा  
✅ **Docker पर्यावरण चालू आहे**: PostgreSQL आणि MCP सर्व्हर कंटेनर  
✅ **VS Code एकत्रीकरण**: MCP सर्व्हर कॉन्फिगर केले आणि प्रवेशयोग्य  
✅ **सत्यापित सेटअप**: सर्व घटक चाचणी केली आणि एकत्र कार्यरत  
✅ **समस्या निराकरण ज्ञान**: सामान्य समस्या आणि उपाय  

## 🚀 पुढे काय?

तुमचे पर्यावरण तयार असल्याने, **[Lab 04: Database Design and Schema](../04-Database/README.md)** सुरू ठेवा:

- रिटेल डेटाबेस स्कीमा तपशीलवार एक्सप्लोर करा
- मल्टी-टेनंट डेटा मॉडेलिंग समजून घ्या
- Row Level Security अंमलबजावणी शिकणे
- नमुना रिटेल डेटासह कार्य करा

## 📚 अतिरिक्त संसाधने

### विकास साधने
- [Docker Documentation](https://docs.docker.com/) - संपूर्ण Docker संदर्भ
- [Azure CLI Reference](https://docs.microsoft.com/cli/azure/) - Azure CLI आदेश
- [VS Code Documentation](https://code.visualstudio.com/docs) - संपादक कॉन्फिगरेशन आणि विस्तार

### Azure सेवा
- [Azure AI Foundry Documentation](https://docs.microsoft.com/azure/ai-foundry/) - AI सेवा कॉन्फिगरेशन
- [Azure OpenAI Service](https://docs.microsoft.com/azure/cognitive-services/openai/) - AI मॉडेल तैनाती
- [Application Insights](https://docs.microsoft.com/azure/azure-monitor/app/app-insights-overview) - मॉनिटरिंग सेटअप

### Python विकास
- [Python Virtual Environments](https://docs.python.org/3/tutorial/venv.html) - पर्यावरण व्यवस्थापन
- [AsyncIO Documentation](https://docs.python.org/3/library/asyncio.html) - Async प्रोग्रामिंग पॅटर्न्स
- [FastAPI Documentation](https://fastapi.tiangolo.com/) - वेब फ्रेमवर्क पॅटर्न्स

---

**पुढे**: पर्यावरण तयार आहे? **[Lab 04: Database Design and Schema](../04-Database/README.md)** सुरू ठेवा

---

**अस्वीकरण**:  
हा दस्तऐवज AI भाषांतर सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) वापरून भाषांतरित करण्यात आला आहे. आम्ही अचूकतेसाठी प्रयत्नशील असलो तरी कृपया लक्षात ठेवा की स्वयंचलित भाषांतरांमध्ये त्रुटी किंवा अचूकतेचा अभाव असू शकतो. मूळ भाषेतील दस्तऐवज हा अधिकृत स्रोत मानला जावा. महत्त्वाच्या माहितीसाठी व्यावसायिक मानवी भाषांतराची शिफारस केली जाते. या भाषांतराचा वापर करून निर्माण होणाऱ्या कोणत्याही गैरसमज किंवा चुकीच्या अर्थासाठी आम्ही जबाबदार राहणार नाही.