# वातावरण सेटअप

## 🎯 यो प्रयोगशालाले के समेट्छ

यो प्रयोगशालाले MCP सर्भरहरू PostgreSQL एकीकरणको साथ निर्माण गर्नको लागि पूर्ण विकास वातावरण सेटअप गर्न चरणबद्ध मार्गदर्शन प्रदान गर्दछ। तपाईं आवश्यक सबै उपकरणहरू कन्फिगर गर्नुहुनेछ, Azure स्रोतहरू तैनात गर्नुहुनेछ, र कार्यान्वयन अघि आफ्नो सेटअपलाई मान्य गर्नुहुनेछ।

## अवलोकन

सही विकास वातावरण सफल MCP सर्भर विकासको लागि महत्त्वपूर्ण छ। यो प्रयोगशालाले Docker, Azure सेवाहरू, विकास उपकरणहरू सेटअप गर्न र सबै कुरा सही रूपमा सँगै काम गरिरहेको छ कि छैन भनेर जाँच गर्न चरणबद्ध निर्देशनहरू प्रदान गर्दछ।

यो प्रयोगशाला समाप्त भएपछि, तपाईं Zava Retail MCP सर्भर निर्माण गर्न तयार पूर्ण कार्यात्मक विकास वातावरण प्राप्त गर्नुहुनेछ।

## सिक्ने उद्देश्यहरू

यो प्रयोगशाला समाप्त गर्दा, तपाईं सक्षम हुनुहुनेछ:

- **आवश्यक विकास उपकरणहरू स्थापना र कन्फिगर गर्नुहोस्**
- **MCP सर्भरको लागि आवश्यक Azure स्रोतहरू तैनात गर्नुहोस्**
- **PostgreSQL र MCP सर्भरको लागि Docker कन्टेनरहरू सेटअप गर्नुहोस्**
- **परीक्षण कनेक्शनहरूसँग आफ्नो वातावरण सेटअप मान्य गर्नुहोस्**
- **सामान्य सेटअप समस्याहरू र कन्फिगरेसन समस्याहरू समाधान गर्नुहोस्**
- **विकास कार्यप्रवाह र फाइल संरचना बुझ्नुहोस्**

## 📋 पूर्व-आवश्यकता जाँच

सुरु गर्नु अघि, सुनिश्चित गर्नुहोस् कि तपाईंले:

### आवश्यक ज्ञान
- आधारभूत कमाण्ड लाइन प्रयोग (Windows Command Prompt/PowerShell)
- वातावरण चरहरूको समझ
- Git संस्करण नियन्त्रणको परिचय
- Dockerका आधारभूत अवधारणाहरू (कन्टेनरहरू, इमेजहरू, भोल्युमहरू)

### प्रणाली आवश्यकताहरू
- **अपरेटिङ सिस्टम**: Windows 10/11, macOS, वा Linux
- **RAM**: न्यूनतम 8GB (16GB सिफारिस गरिएको)
- **स्टोरेज**: कम्तीमा 10GB खाली ठाउँ
- **नेटवर्क**: डाउनलोड र Azure तैनातीको लागि इन्टरनेट कनेक्शन

### खाता आवश्यकताहरू
- **Azure सदस्यता**: निःशुल्क स्तर पर्याप्त छ
- **GitHub खाता**: रिपोजिटरी पहुँचको लागि
- **Docker Hub खाता**: (वैकल्पिक) कस्टम इमेज प्रकाशनको लागि

## 🛠️ उपकरण स्थापना

### 1. Docker Desktop स्थापना गर्नुहोस्

Dockerले हाम्रो विकास सेटअपको लागि कन्टेनरयुक्त वातावरण प्रदान गर्दछ।

#### Windows स्थापना

1. **Docker Desktop डाउनलोड गर्नुहोस्**:
   ```cmd
   # Visit https://desktop.docker.com/win/stable/Docker%20Desktop%20Installer.exe
   # Or use Windows Package Manager
   winget install Docker.DockerDesktop
   ```

2. **स्थापना र कन्फिगर गर्नुहोस्**:
   - Administratorको रूपमा इन्स्टॉलर चलाउनुहोस्
   - WSL 2 एकीकरण सक्षम गर्नुहोस् जब सोधिन्छ
   - स्थापना पूरा भएपछि आफ्नो कम्प्युटर पुनः सुरु गर्नुहोस्

3. **स्थापना प्रमाणित गर्नुहोस्**:
   ```cmd
   docker --version
   docker-compose --version
   ```

#### macOS स्थापना

1. **डाउनलोड र स्थापना गर्नुहोस्**:
   ```bash
   # Download from https://desktop.docker.com/mac/stable/Docker.dmg
   # Or use Homebrew
   brew install --cask docker
   ```

2. **Docker Desktop सुरु गर्नुहोस्**:
   - Applicationsबाट Docker Desktop सुरु गर्नुहोस्
   - प्रारम्भिक सेटअप विजार्ड पूरा गर्नुहोस्

3. **स्थापना प्रमाणित गर्नुहोस्**:
   ```bash
   docker --version
   docker-compose --version
   ```

#### Linux स्थापना

1. **Docker Engine स्थापना गर्नुहोस्**:
   ```bash
   # Ubuntu/Debian
   curl -fsSL https://get.docker.com -o get-docker.sh
   sudo sh get-docker.sh
   sudo usermod -aG docker $USER
   
   # Log out and back in for group changes to take effect
   ```

2. **Docker Compose स्थापना गर्नुहोस्**:
   ```bash
   sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
   sudo chmod +x /usr/local/bin/docker-compose
   ```

### 2. Azure CLI स्थापना गर्नुहोस्

Azure CLIले Azure स्रोत तैनाती र व्यवस्थापन सक्षम गर्दछ।

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

#### प्रमाणित गर्नुहोस् र प्रमाणिकरण गर्नुहोस्

```bash
# Check installation
az version

# Login to Azure
az login

# Set default subscription (if you have multiple)
az account list --output table
az account set --subscription "Your-Subscription-Name"
```

### 3. Git स्थापना गर्नुहोस्

Git रिपोजिटरी क्लोन गर्न र संस्करण नियन्त्रणको लागि आवश्यक छ।

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

### 4. VS Code स्थापना गर्नुहोस्

Visual Studio Codeले MCP समर्थनको साथ एकीकृत विकास वातावरण प्रदान गर्दछ।

#### स्थापना

```cmd
# Windows
winget install Microsoft.VisualStudioCode

# macOS
brew install --cask visual-studio-code

# Linux (Ubuntu/Debian)
sudo snap install code --classic
```

#### आवश्यक एक्सटेन्सनहरू

यी VS Code एक्सटेन्सनहरू स्थापना गर्नुहोस्:

```bash
# Install via command line
code --install-extension ms-python.python
code --install-extension ms-vscode.vscode-json
code --install-extension ms-azuretools.vscode-docker
code --install-extension ms-vscode.azure-account
```

वा VS Code मार्फत स्थापना गर्नुहोस्:
1. VS Code खोल्नुहोस्
2. Extensionsमा जानुहोस् (Ctrl+Shift+X)
3. स्थापना गर्नुहोस्:
   - **Python** (Microsoft)
   - **Docker** (Microsoft)
   - **Azure Account** (Microsoft)
   - **JSON** (Microsoft)

### 5. Python स्थापना गर्नुहोस्

Python 3.8+ MCP सर्भर विकासको लागि आवश्यक छ।

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

#### स्थापना प्रमाणित गर्नुहोस्

```bash
python --version  # Should show Python 3.11.x
pip --version      # Should show pip version
```

## 🚀 परियोजना सेटअप

### 1. रिपोजिटरी क्लोन गर्नुहोस्

```bash
# Clone the main repository
git clone https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail.git

# Navigate to the project directory
cd MCP-Server-and-PostgreSQL-Sample-Retail

# Verify repository structure
ls -la
```

### 2. Python भर्चुअल वातावरण सिर्जना गर्नुहोस्

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

### 3. Python निर्भरता स्थापना गर्नुहोस्

```bash
# Install development dependencies
pip install -r requirements.lock.txt

# Verify key packages
pip list | grep fastmcp
pip list | grep asyncpg
pip list | grep azure
```

## ☁️ Azure स्रोत तैनाती

### 1. स्रोत आवश्यकताहरू बुझ्नुहोस्

हाम्रो MCP सर्भरलाई यी Azure स्रोतहरू आवश्यक छ:

| **स्रोत** | **उद्देश्य** | **अनुमानित लागत** |
|--------------|-------------|-------------------|
| **Azure AI Foundry** | AI मोडेल होस्टिंग र व्यवस्थापन | $10-50/महिना |
| **OpenAI तैनाती** | टेक्स्ट एम्बेडिङ मोडेल (text-embedding-3-small) | $5-20/महिना |
| **Application Insights** | निगरानी र टेलिमेट्री | $5-15/महिना |
| **Resource Group** | स्रोत संगठन | निःशुल्क |

### 2. Azure स्रोत तैनात गर्नुहोस्

#### विकल्प A: स्वचालित तैनाती (सिफारिस गरिएको)

```bash
# Navigate to infrastructure directory
cd infra

# Windows - PowerShell
./deploy.ps1

# macOS/Linux - Bash
./deploy.sh
```

तैनाती स्क्रिप्टले:
1. एक अद्वितीय स्रोत समूह सिर्जना गर्दछ
2. Azure AI Foundry स्रोतहरू तैनात गर्दछ
3. text-embedding-3-small मोडेल तैनात गर्दछ
4. Application Insights कन्फिगर गर्दछ
5. प्रमाणिकरणको लागि सेवा प्रमुख सिर्जना गर्दछ
6. `.env` फाइल कन्फिगरेसनको साथ उत्पन्न गर्दछ

#### विकल्प B: म्यानुअल तैनाती

यदि तपाईं म्यानुअल नियन्त्रण चाहनुहुन्छ वा स्वचालित स्क्रिप्ट असफल भयो भने:

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

### 3. Azure तैनाती प्रमाणित गर्नुहोस्

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

### 4. वातावरण चरहरू कन्फिगर गर्नुहोस्

तैनाती पछि, तपाईंले `.env` फाइल प्राप्त गर्नुपर्छ। सुनिश्चित गर्नुहोस् कि यसमा समावेश छ:

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

## 🐳 Docker वातावरण सेटअप

### 1. Docker संरचना बुझ्नुहोस्

हाम्रो विकास वातावरणले Docker Compose प्रयोग गर्दछ:

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

### 2. विकास वातावरण सुरु गर्नुहोस्

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

### 3. डाटाबेस सेटअप प्रमाणित गर्नुहोस्

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

### 4. MCP सर्भर परीक्षण गर्नुहोस्

```bash
# Check MCP server health
curl http://localhost:8000/health

# Test basic MCP endpoint
curl -X POST http://localhost:8000/mcp \
  -H "Content-Type: application/json" \
  -H "x-rls-user-id: 00000000-0000-0000-0000-000000000000" \
  -d '{"method": "tools/list", "params": {}}'
```

## 🔧 VS Code कन्फिगरेसन

### 1. MCP एकीकरण कन्फिगर गर्नुहोस्

VS Code MCP कन्फिगरेसन सिर्जना गर्नुहोस्:

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

### 2. Python वातावरण कन्फिगर गर्नुहोस्

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

### 3. VS Code एकीकरण परीक्षण गर्नुहोस्

1. **परियोजना VS Codeमा खोल्नुहोस्**:
   ```bash
   code .
   ```

2. **AI Chat खोल्नुहोस्**:
   - `Ctrl+Shift+P` (Windows/Linux) वा `Cmd+Shift+P` (macOS) थिच्नुहोस्
   - "AI Chat" टाइप गर्नुहोस् र "AI Chat: Open Chat" चयन गर्नुहोस्

3. **MCP सर्भर कनेक्शन परीक्षण गर्नुहोस्**:
   - AI Chatमा, `#zava` टाइप गर्नुहोस् र कन्फिगर गरिएका सर्भरहरू मध्ये एक चयन गर्नुहोस्
   - सोध्नुहोस्: "डाटाबेसमा उपलब्ध टेबलहरू के छन्?"
   - तपाईंले खुद्रा डाटाबेस टेबलहरूको सूची प्राप्त गर्नुहुनेछ

## ✅ वातावरण मान्यता

### 1. व्यापक प्रणाली जाँच

तपाईंको सेटअप प्रमाणित गर्न यो मान्यता स्क्रिप्ट चलाउनुहोस्:

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

### 2. म्यानुअल मान्यता चेकलिस्ट

**✅ आधारभूत उपकरणहरू**
- [ ] Docker संस्करण 20.10+ स्थापना गरिएको र चलिरहेको
- [ ] Azure CLI 2.40+ स्थापना गरिएको र प्रमाणित गरिएको
- [ ] Python 3.8+ pip सहित स्थापना गरिएको
- [ ] Git 2.30+ स्थापना गरिएको
- [ ] VS Code आवश्यक एक्सटेन्सनहरूसँग

**✅ Azure स्रोतहरू**
- [ ] स्रोत समूह सफलतापूर्वक सिर्जना गरिएको
- [ ] AI Foundry परियोजना तैनात गरिएको
- [ ] OpenAI text-embedding-3-small मोडेल तैनात गरिएको
- [ ] Application Insights कन्फिगर गरिएको
- [ ] सेवा प्रमुख उचित अनुमतिहरूसँग सिर्जना गरिएको

**✅ वातावरण कन्फिगरेसन**
- [ ] `.env` फाइल सबै आवश्यक चरहरूसँग सिर्जना गरिएको
- [ ] Azure प्रमाणिकरण काम गरिरहेको (`az account show` परीक्षण गर्नुहोस्)
- [ ] PostgreSQL कन्टेनर चलिरहेको र पहुँचयोग्य
- [ ] डाटाबेसमा नमूना डाटा लोड गरिएको

**✅ VS Code एकीकरण**
- [ ] `.vscode/mcp.json` कन्फिगर गरिएको
- [ ] Python व्याख्याता भर्चुअल वातावरणमा सेट गरिएको
- [ ] MCP सर्भरहरू AI Chatमा देखा परेका
- [ ] AI Chat मार्फत परीक्षण क्वेरीहरू कार्यान्वयन गर्न सकिन्छ

## 🛠️ सामान्य समस्याहरू समाधान

### Docker समस्याहरू

**समस्या**: Docker कन्टेनरहरू सुरु हुँदैनन्
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

**समस्या**: PostgreSQL कनेक्शन असफल भयो
```bash
# Check container logs
docker-compose logs postgres

# Verify container is healthy
docker-compose ps

# Test direct connection
docker-compose exec postgres psql -U postgres -d zava -c "SELECT 1;"
```

### Azure तैनाती समस्याहरू

**समस्या**: Azure तैनाती असफल भयो
```bash
# Check Azure CLI authentication
az account show

# Verify subscription permissions
az role assignment list --assignee $(az account show --query user.name -o tsv)

# Check resource provider registration
az provider register --namespace Microsoft.CognitiveServices
az provider register --namespace Microsoft.Insights
```

**समस्या**: AI सेवा प्रमाणिकरण असफल भयो
```bash
# Test service principal
az login --service-principal \
  --username $AZURE_CLIENT_ID \
  --password $AZURE_CLIENT_SECRET \
  --tenant $AZURE_TENANT_ID

# Verify AI service deployment
az cognitiveservices account list --query "[].{Name:name,Kind:kind,Location:location}"
```

### Python वातावरण समस्याहरू

**समस्या**: प्याकेज स्थापना असफल भयो
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

**समस्या**: VS Codeले Python व्याख्याता फेला पार्न सकेन
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

## 🎯 मुख्य निष्कर्षहरू

यो प्रयोगशाला पूरा गरेपछि, तपाईंले:

✅ **पूर्ण विकास वातावरण**: सबै उपकरणहरू स्थापना र कन्फिगर गरिएको  
✅ **Azure स्रोतहरू तैनात गरिएको**: AI सेवाहरू र समर्थन पूर्वाधार  
✅ **Docker वातावरण चलिरहेको**: PostgreSQL र MCP सर्भर कन्टेनरहरू  
✅ **VS Code एकीकरण**: MCP सर्भरहरू कन्फिगर गरिएको र पहुँचयोग्य  
✅ **सेटअप मान्यता गरिएको**: सबै घटकहरू परीक्षण गरिएको र सँगै काम गरिरहेको  
✅ **समस्याहरू समाधान गर्ने ज्ञान**: सामान्य समस्याहरू र समाधानहरू  

## 🚀 अब के गर्ने

तपाईंको वातावरण तयार भएपछि, **[Lab 04: Database Design and Schema](../04-Database/README.md)** जारी राख्नुहोस्:

- खुद्रा डाटाबेस स्कीमालाई विस्तृत रूपमा अन्वेषण गर्नुहोस्
- बहु-भाडावाल डाटा मोडेलिङ बुझ्नुहोस्
- Row Level Security कार्यान्वयनको बारेमा जान्नुहोस्
- नमूना खुद्रा डाटासँग काम गर्नुहोस्

## 📚 थप स्रोतहरू

### विकास उपकरणहरू
- [Docker Documentation](https://docs.docker.com/) - पूर्ण Docker सन्दर्भ
- [Azure CLI Reference](https://docs.microsoft.com/cli/azure/) - Azure CLI आदेशहरू
- [VS Code Documentation](https://code.visualstudio.com/docs) - सम्पादक कन्फिगरेसन र एक्सटेन्सनहरू

### Azure सेवाहरू
- [Azure AI Foundry Documentation](https://docs.microsoft.com/azure/ai-foundry/) - AI सेवा कन्फिगरेसन
- [Azure OpenAI Service](https://docs.microsoft.com/azure/cognitive-services/openai/) - AI मोडेल तैनाती
- [Application Insights](https://docs.microsoft.com/azure/azure-monitor/app/app-insights-overview) - निगरानी सेटअप

### Python विकास
- [Python Virtual Environments](https://docs.python.org/3/tutorial/venv.html) - वातावरण व्यवस्थापन
- [AsyncIO Documentation](https://docs.python.org/3/library/asyncio.html) - Async प्रोग्रामिङ ढाँचाहरू
- [FastAPI Documentation](https://fastapi.tiangolo.com/) - वेब फ्रेमवर्क ढाँचाहरू

---

**अगाडि**: वातावरण तयार? [Lab 04: Database Design and Schema](../04-Database/README.md) जारी राख्नुहोस्

---

**अस्वीकरण**:  
यो दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरेर अनुवाद गरिएको हो। हामी यथार्थताको लागि प्रयास गर्छौं, तर कृपया ध्यान दिनुहोस् कि स्वचालित अनुवादमा त्रुटिहरू वा अशुद्धताहरू हुन सक्छ। यसको मूल भाषा मा रहेको मूल दस्तावेज़लाई आधिकारिक स्रोत मानिनुपर्छ। महत्वपूर्ण जानकारीको लागि, व्यावसायिक मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न हुने कुनै पनि गलतफहमी वा गलत व्याख्याको लागि हामी जिम्मेवार हुने छैनौं।