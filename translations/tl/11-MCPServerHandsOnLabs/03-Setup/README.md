# Pagsasaayos ng Kapaligiran

## 🎯 Ano ang Saklaw ng Lab na Ito

Ang hands-on lab na ito ay magtuturo sa iyo kung paano mag-set up ng kumpletong development environment para sa paggawa ng MCP servers na may PostgreSQL integration. Ikaw ay magko-configure ng mga kinakailangang tools, magde-deploy ng Azure resources, at magva-validate ng iyong setup bago magpatuloy sa implementasyon.

## Pangkalahatang-ideya

Ang tamang development environment ay mahalaga para sa matagumpay na paggawa ng MCP server. Ang lab na ito ay nagbibigay ng step-by-step na gabay para sa pag-set up ng Docker, Azure services, development tools, at pag-validate na gumagana ang lahat ng ito nang maayos.

Sa pagtatapos ng lab na ito, magkakaroon ka ng ganap na functional na development environment na handa para sa paggawa ng Zava Retail MCP server.

## Mga Layunin sa Pag-aaral

Sa pagtatapos ng lab na ito, magagawa mo ang sumusunod:

- **I-install at i-configure** ang lahat ng kinakailangang development tools
- **Mag-deploy ng Azure resources** na kinakailangan para sa MCP server
- **Mag-set up ng Docker containers** para sa PostgreSQL at MCP server
- **I-validate** ang iyong environment setup gamit ang test connections
- **Mag-troubleshoot** ng mga karaniwang isyu sa setup at configuration
- **Maunawaan** ang development workflow at file structure

## 📋 Pagsusuri ng Mga Kinakailangan

Bago magsimula, tiyakin na mayroon ka ng mga sumusunod:

### Kinakailangang Kaalaman
- Pangunahing paggamit ng command line (Windows Command Prompt/PowerShell)
- Pag-unawa sa environment variables
- Pamilyar sa Git version control
- Pangunahing konsepto ng Docker (containers, images, volumes)

### Mga Kinakailangan sa Sistema
- **Operating System**: Windows 10/11, macOS, o Linux
- **RAM**: Minimum na 8GB (16GB inirerekomenda)
- **Storage**: Hindi bababa sa 10GB na libreng espasyo
- **Network**: Internet connection para sa downloads at Azure deployment

### Mga Kinakailangan sa Account
- **Azure Subscription**: Ang libreng tier ay sapat na
- **GitHub Account**: Para sa repository access
- **Docker Hub Account**: (Opsyonal) Para sa custom image publishing

## 🛠️ Pag-install ng Mga Tool

### 1. I-install ang Docker Desktop

Ang Docker ang nagbibigay ng containerized environment para sa ating development setup.

#### Pag-install sa Windows

1. **I-download ang Docker Desktop**:
   ```cmd
   # Visit https://desktop.docker.com/win/stable/Docker%20Desktop%20Installer.exe
   # Or use Windows Package Manager
   winget install Docker.DockerDesktop
   ```

2. **I-install at I-configure**:
   - Patakbuhin ang installer bilang Administrator
   - I-enable ang WSL 2 integration kapag na-prompt
   - I-restart ang iyong computer kapag natapos ang pag-install

3. **I-verify ang Pag-install**:
   ```cmd
   docker --version
   docker-compose --version
   ```

#### Pag-install sa macOS

1. **I-download at I-install**:
   ```bash
   # Download from https://desktop.docker.com/mac/stable/Docker.dmg
   # Or use Homebrew
   brew install --cask docker
   ```

2. **I-start ang Docker Desktop**:
   - I-launch ang Docker Desktop mula sa Applications
   - Kumpletuhin ang initial setup wizard

3. **I-verify ang Pag-install**:
   ```bash
   docker --version
   docker-compose --version
   ```

#### Pag-install sa Linux

1. **I-install ang Docker Engine**:
   ```bash
   # Ubuntu/Debian
   curl -fsSL https://get.docker.com -o get-docker.sh
   sudo sh get-docker.sh
   sudo usermod -aG docker $USER
   
   # Log out and back in for group changes to take effect
   ```

2. **I-install ang Docker Compose**:
   ```bash
   sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
   sudo chmod +x /usr/local/bin/docker-compose
   ```

### 2. I-install ang Azure CLI

Ang Azure CLI ang nagbibigay-daan sa pag-deploy at pamamahala ng Azure resources.

#### Pag-install sa Windows

```cmd
# Using Windows Package Manager
winget install Microsoft.AzureCLI

# Or download MSI from: https://aka.ms/installazurecliwindows
```

#### Pag-install sa macOS

```bash
# Using Homebrew
brew install azure-cli

# Or using installer
curl -L https://aka.ms/InstallAzureCli | bash
```

#### Pag-install sa Linux

```bash
# Ubuntu/Debian
curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash

# RHEL/CentOS
sudo rpm --import https://packages.microsoft.com/keys/microsoft.asc
sudo dnf install azure-cli
```

#### I-verify at Mag-authenticate

```bash
# Check installation
az version

# Login to Azure
az login

# Set default subscription (if you have multiple)
az account list --output table
az account set --subscription "Your-Subscription-Name"
```

### 3. I-install ang Git

Ang Git ay kinakailangan para sa pag-clone ng repository at version control.

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

### 4. I-install ang VS Code

Ang Visual Studio Code ang nagbibigay ng integrated development environment na may suporta para sa MCP.

#### Pag-install

```cmd
# Windows
winget install Microsoft.VisualStudioCode

# macOS
brew install --cask visual-studio-code

# Linux (Ubuntu/Debian)
sudo snap install code --classic
```

#### Mga Kinakailangang Extension

I-install ang mga sumusunod na VS Code extensions:

```bash
# Install via command line
code --install-extension ms-python.python
code --install-extension ms-vscode.vscode-json
code --install-extension ms-azuretools.vscode-docker
code --install-extension ms-vscode.azure-account
```

O i-install sa pamamagitan ng VS Code:
1. Buksan ang VS Code
2. Pumunta sa Extensions (Ctrl+Shift+X)
3. I-install:
   - **Python** (Microsoft)
   - **Docker** (Microsoft)
   - **Azure Account** (Microsoft)
   - **JSON** (Microsoft)

### 5. I-install ang Python

Kinakailangan ang Python 3.8+ para sa paggawa ng MCP server.

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

#### I-verify ang Pag-install

```bash
python --version  # Should show Python 3.11.x
pip --version      # Should show pip version
```

## 🚀 Pag-set up ng Proyekto

### 1. I-clone ang Repository

```bash
# Clone the main repository
git clone https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail.git

# Navigate to the project directory
cd MCP-Server-and-PostgreSQL-Sample-Retail

# Verify repository structure
ls -la
```

### 2. Gumawa ng Python Virtual Environment

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

### 3. I-install ang Python Dependencies

```bash
# Install development dependencies
pip install -r requirements.lock.txt

# Verify key packages
pip list | grep fastmcp
pip list | grep asyncpg
pip list | grep azure
```

## ☁️ Pag-deploy ng Azure Resources

### 1. Unawain ang Mga Kinakailangan sa Resource

Ang ating MCP server ay nangangailangan ng mga sumusunod na Azure resources:

| **Resource** | **Layunin** | **Tinatayang Gastos** |
|--------------|-------------|-----------------------|
| **Azure AI Foundry** | Hosting at pamamahala ng AI model | $10-50/buwan |
| **OpenAI Deployment** | Text embedding model (text-embedding-3-small) | $5-20/buwan |
| **Application Insights** | Monitoring at telemetry | $5-15/buwan |
| **Resource Group** | Organisasyon ng resources | Libre |

### 2. Mag-deploy ng Azure Resources

#### Opsyon A: Automated Deployment (Inirerekomenda)

```bash
# Navigate to infrastructure directory
cd infra

# Windows - PowerShell
./deploy.ps1

# macOS/Linux - Bash
./deploy.sh
```

Ang deployment script ay gagawa ng sumusunod:
1. Gumawa ng natatanging resource group
2. Mag-deploy ng Azure AI Foundry resources
3. Mag-deploy ng text-embedding-3-small model
4. Mag-configure ng Application Insights
5. Gumawa ng service principal para sa authentication
6. Bumuo ng `.env` file na may configuration

#### Opsyon B: Manual Deployment

Kung mas gusto mo ang manual na kontrol o nabigo ang automated script:

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

### 3. I-verify ang Azure Deployment

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

### 4. I-configure ang Environment Variables

Pagkatapos ng deployment, dapat mayroon kang `.env` file. Tiyakin na naglalaman ito ng:

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

## 🐳 Pag-set up ng Docker Environment

### 1. Unawain ang Docker Composition

Ang ating development environment ay gumagamit ng Docker Compose:

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

### 2. I-start ang Development Environment

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

### 3. I-verify ang Database Setup

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

### 4. Subukan ang MCP Server

```bash
# Check MCP server health
curl http://localhost:8000/health

# Test basic MCP endpoint
curl -X POST http://localhost:8000/mcp \
  -H "Content-Type: application/json" \
  -H "x-rls-user-id: 00000000-0000-0000-0000-000000000000" \
  -d '{"method": "tools/list", "params": {}}'
```

## 🔧 Konfigurasyon ng VS Code

### 1. I-configure ang MCP Integration

Gumawa ng VS Code MCP configuration:

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

### 2. I-configure ang Python Environment

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

### 3. Subukan ang VS Code Integration

1. **Buksan ang proyekto sa VS Code**:
   ```bash
   code .
   ```

2. **Buksan ang AI Chat**:
   - Pindutin ang `Ctrl+Shift+P` (Windows/Linux) o `Cmd+Shift+P` (macOS)
   - I-type ang "AI Chat" at piliin ang "AI Chat: Open Chat"

3. **Subukan ang MCP Server Connection**:
   - Sa AI Chat, i-type ang `#zava` at piliin ang isa sa mga naka-configure na servers
   - Magtanong: "Anong mga tables ang available sa database?"
   - Dapat kang makatanggap ng sagot na naglilista ng mga retail database tables

## ✅ Pag-validate ng Kapaligiran

### 1. Comprehensive System Check

Patakbuhin ang validation script na ito para i-verify ang iyong setup:

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

**✅ Pangunahing Tools**
- [ ] Na-install at tumatakbo ang Docker version 20.10+
- [ ] Na-install at authenticated ang Azure CLI 2.40+
- [ ] Na-install ang Python 3.8+ na may pip
- [ ] Na-install ang Git 2.30+
- [ ] Na-install ang VS Code na may kinakailangang extensions

**✅ Azure Resources**
- [ ] Matagumpay na nagawa ang resource group
- [ ] Na-deploy ang AI Foundry project
- [ ] Na-deploy ang OpenAI text-embedding-3-small model
- [ ] Na-configure ang Application Insights
- [ ] Nilikha ang service principal na may tamang permissions

**✅ Konfigurasyon ng Kapaligiran**
- [ ] Nilikha ang `.env` file na may lahat ng kinakailangang variables
- [ ] Gumagana ang Azure credentials (subukan gamit ang `az account show`)
- [ ] Tumatakbo at accessible ang PostgreSQL container
- [ ] Na-load ang sample data sa database

**✅ VS Code Integration**
- [ ] Na-configure ang `.vscode/mcp.json`
- [ ] Na-set ang Python interpreter sa virtual environment
- [ ] Lumalabas ang MCP servers sa AI Chat
- [ ] Maaaring magpatakbo ng test queries sa AI Chat

## 🛠️ Pag-troubleshoot ng Karaniwang Isyu

### Mga Isyu sa Docker

**Problema**: Hindi mag-start ang Docker containers
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

**Problema**: Nabigo ang PostgreSQL connection
```bash
# Check container logs
docker-compose logs postgres

# Verify container is healthy
docker-compose ps

# Test direct connection
docker-compose exec postgres psql -U postgres -d zava -c "SELECT 1;"
```

### Mga Isyu sa Azure Deployment

**Problema**: Nabigo ang Azure deployment
```bash
# Check Azure CLI authentication
az account show

# Verify subscription permissions
az role assignment list --assignee $(az account show --query user.name -o tsv)

# Check resource provider registration
az provider register --namespace Microsoft.CognitiveServices
az provider register --namespace Microsoft.Insights
```

**Problema**: Nabigo ang authentication ng AI service
```bash
# Test service principal
az login --service-principal \
  --username $AZURE_CLIENT_ID \
  --password $AZURE_CLIENT_SECRET \
  --tenant $AZURE_TENANT_ID

# Verify AI service deployment
az cognitiveservices account list --query "[].{Name:name,Kind:kind,Location:location}"
```

### Mga Isyu sa Python Environment

**Problema**: Nabigo ang pag-install ng package
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

**Problema**: Hindi mahanap ng VS Code ang Python interpreter
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

## 🎯 Mga Pangunahing Puntos

Pagkatapos makumpleto ang lab na ito, dapat mayroon ka ng:

✅ **Kumpletong Development Environment**: Na-install at na-configure ang lahat ng tools  
✅ **Na-deploy na Azure Resources**: AI services at mga supporting infrastructure  
✅ **Tumatakbo ang Docker Environment**: PostgreSQL at MCP server containers  
✅ **VS Code Integration**: Na-configure at accessible ang MCP servers  
✅ **Na-validate na Setup**: Nasubukan at gumagana ang lahat ng components  
✅ **Kaalaman sa Troubleshooting**: Mga karaniwang isyu at solusyon  

## 🚀 Ano ang Susunod

Kapag handa na ang iyong environment, magpatuloy sa **[Lab 04: Database Design and Schema](../04-Database/README.md)** upang:

- Tuklasin ang detalye ng retail database schema
- Maunawaan ang multi-tenant data modeling
- Matutunan ang implementasyon ng Row Level Security
- Magtrabaho gamit ang sample retail data

## 📚 Karagdagang Resources

### Mga Development Tools
- [Docker Documentation](https://docs.docker.com/) - Kumpletong reference para sa Docker
- [Azure CLI Reference](https://docs.microsoft.com/cli/azure/) - Mga Azure CLI commands
- [VS Code Documentation](https://code.visualstudio.com/docs) - Konfigurasyon ng editor at extensions

### Mga Azure Services
- [Azure AI Foundry Documentation](https://docs.microsoft.com/azure/ai-foundry/) - Konfigurasyon ng AI service
- [Azure OpenAI Service](https://docs.microsoft.com/azure/cognitive-services/openai/) - Deployment ng AI model
- [Application Insights](https://docs.microsoft.com/azure/azure-monitor/app/app-insights-overview) - Setup ng monitoring

### Python Development
- [Python Virtual Environments](https://docs.python.org/3/tutorial/venv.html) - Pamamahala ng environment
- [AsyncIO Documentation](https://docs.python.org/3/library/asyncio.html) - Mga pattern sa async programming
- [FastAPI Documentation](https://fastapi.tiangolo.com/) - Mga pattern sa web framework

---

**Susunod**: Handa na ang environment? Magpatuloy sa [Lab 04: Database Design and Schema](../04-Database/README.md)

---

**Paunawa**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't sinisikap naming maging tumpak, mangyaring tandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa kanyang katutubong wika ang dapat ituring na opisyal na sanggunian. Para sa mahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na dulot ng paggamit ng pagsasaling ito.