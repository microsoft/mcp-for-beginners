# Miljøopsætning

## 🎯 Hvad Denne Lab Dækker

Denne praktiske lab guider dig gennem opsætningen af et komplet udviklingsmiljø til opbygning af MCP-servere med PostgreSQL-integration. Du vil konfigurere alle nødvendige værktøjer, implementere Azure-ressourcer og validere din opsætning, før du går videre med implementeringen.

## Oversigt

Et korrekt udviklingsmiljø er afgørende for succesfuld udvikling af MCP-servere. Denne lab giver trin-for-trin instruktioner til opsætning af Docker, Azure-tjenester, udviklingsværktøjer og validering af, at alt fungerer korrekt sammen.

Ved afslutningen af denne lab vil du have et fuldt funktionelt udviklingsmiljø klar til at bygge Zava Retail MCP-serveren.

## Læringsmål

Ved afslutningen af denne lab vil du kunne:

- **Installere og konfigurere** alle nødvendige udviklingsværktøjer
- **Implementere Azure-ressourcer** nødvendige for MCP-serveren
- **Opsætte Docker-containere** til PostgreSQL og MCP-serveren
- **Validere** din miljøopsætning med testforbindelser
- **Fejlsøge** almindelige opsætningsproblemer og konfigurationsfejl
- **Forstå** udviklingsworkflowet og filstrukturen

## 📋 Forudsætninger

Før du starter, skal du sikre dig, at du har:

### Nødvendig Viden
- Grundlæggende brug af kommandolinjen (Windows Command Prompt/PowerShell)
- Forståelse af miljøvariabler
- Kendskab til Git versionskontrol
- Grundlæggende Docker-koncept (containere, billeder, volumes)

### Systemkrav
- **Operativsystem**: Windows 10/11, macOS eller Linux
- **RAM**: Minimum 8GB (16GB anbefales)
- **Lagerplads**: Mindst 10GB ledig plads
- **Netværk**: Internetforbindelse til downloads og Azure-implementering

### Konto Krav
- **Azure-abonnement**: Gratis niveau er tilstrækkeligt
- **GitHub-konto**: Til adgang til repository
- **Docker Hub-konto**: (Valgfrit) Til publicering af brugerdefinerede billeder

## 🛠️ Værktøjsinstallation

### 1. Installer Docker Desktop

Docker leverer det containeriserede miljø til vores udviklingsopsætning.

#### Windows Installation

1. **Download Docker Desktop**:
   ```cmd
   # Visit https://desktop.docker.com/win/stable/Docker%20Desktop%20Installer.exe
   # Or use Windows Package Manager
   winget install Docker.DockerDesktop
   ```

2. **Installer og Konfigurer**:
   - Kør installationsprogrammet som Administrator
   - Aktiver WSL 2-integration, når du bliver bedt om det
   - Genstart din computer, når installationen er færdig

3. **Bekræft Installation**:
   ```cmd
   docker --version
   docker-compose --version
   ```

#### macOS Installation

1. **Download og Installer**:
   ```bash
   # Download from https://desktop.docker.com/mac/stable/Docker.dmg
   # Or use Homebrew
   brew install --cask docker
   ```

2. **Start Docker Desktop**:
   - Åbn Docker Desktop fra Programmer
   - Fuldfør den indledende opsætningsguide

3. **Bekræft Installation**:
   ```bash
   docker --version
   docker-compose --version
   ```

#### Linux Installation

1. **Installer Docker Engine**:
   ```bash
   # Ubuntu/Debian
   curl -fsSL https://get.docker.com -o get-docker.sh
   sudo sh get-docker.sh
   sudo usermod -aG docker $USER
   
   # Log out and back in for group changes to take effect
   ```

2. **Installer Docker Compose**:
   ```bash
   sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
   sudo chmod +x /usr/local/bin/docker-compose
   ```

### 2. Installer Azure CLI

Azure CLI gør det muligt at implementere og administrere Azure-ressourcer.

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

#### Bekræft og Autentificer

```bash
# Check installation
az version

# Login to Azure
az login

# Set default subscription (if you have multiple)
az account list --output table
az account set --subscription "Your-Subscription-Name"
```

### 3. Installer Git

Git er nødvendigt for at klone repository og versionskontrol.

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

### 4. Installer VS Code

Visual Studio Code leverer det integrerede udviklingsmiljø med MCP-support.

#### Installation

```cmd
# Windows
winget install Microsoft.VisualStudioCode

# macOS
brew install --cask visual-studio-code

# Linux (Ubuntu/Debian)
sudo snap install code --classic
```

#### Nødvendige Udvidelser

Installer disse VS Code-udvidelser:

```bash
# Install via command line
code --install-extension ms-python.python
code --install-extension ms-vscode.vscode-json
code --install-extension ms-azuretools.vscode-docker
code --install-extension ms-vscode.azure-account
```

Eller installer via VS Code:
1. Åbn VS Code
2. Gå til Udvidelser (Ctrl+Shift+X)
3. Installer:
   - **Python** (Microsoft)
   - **Docker** (Microsoft)
   - **Azure Account** (Microsoft)
   - **JSON** (Microsoft)

### 5. Installer Python

Python 3.8+ er påkrævet til MCP-serverudvikling.

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

#### Bekræft Installation

```bash
python --version  # Should show Python 3.11.x
pip --version      # Should show pip version
```

## 🚀 Projektopsætning

### 1. Klon Repository

```bash
# Clone the main repository
git clone https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail.git

# Navigate to the project directory
cd MCP-Server-and-PostgreSQL-Sample-Retail

# Verify repository structure
ls -la
```

### 2. Opret Python Virtuelt Miljø

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

### 3. Installer Python-afhængigheder

```bash
# Install development dependencies
pip install -r requirements.lock.txt

# Verify key packages
pip list | grep fastmcp
pip list | grep asyncpg
pip list | grep azure
```

## ☁️ Implementering af Azure-ressourcer

### 1. Forstå Ressourcekrav

Vores MCP-server kræver følgende Azure-ressourcer:

| **Ressource** | **Formål** | **Anslået Omkostning** |
|---------------|------------|-----------------------|
| **Azure AI Foundry** | Hosting og styring af AI-modeller | $10-50/måned |
| **OpenAI-implementering** | Tekstindlejringsmodel (text-embedding-3-small) | $5-20/måned |
| **Application Insights** | Overvågning og telemetri | $5-15/måned |
| **Resource Group** | Ressourceorganisation | Gratis |

### 2. Implementer Azure-ressourcer

#### Option A: Automatisk Implementering (Anbefalet)

```bash
# Navigate to infrastructure directory
cd infra

# Windows - PowerShell
./deploy.ps1

# macOS/Linux - Bash
./deploy.sh
```

Implementeringsscriptet vil:
1. Oprette en unik ressourcegruppe
2. Implementere Azure AI Foundry-ressourcer
3. Implementere text-embedding-3-small-modellen
4. Konfigurere Application Insights
5. Oprette en service principal til autentificering
6. Generere `.env`-fil med konfiguration

#### Option B: Manuel Implementering

Hvis du foretrækker manuel kontrol eller det automatiske script fejler:

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

### 3. Bekræft Azure-implementering

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

### 4. Konfigurer Miljøvariabler

Efter implementeringen bør du have en `.env`-fil. Bekræft, at den indeholder:

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

## 🐳 Docker Miljøopsætning

### 1. Forstå Docker-komposition

Vores udviklingsmiljø bruger Docker Compose:

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

### 2. Start Udviklingsmiljøet

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

### 3. Bekræft Databaseopsætning

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

### 4. Test MCP-server

```bash
# Check MCP server health
curl http://localhost:8000/health

# Test basic MCP endpoint
curl -X POST http://localhost:8000/mcp \
  -H "Content-Type: application/json" \
  -H "x-rls-user-id: 00000000-0000-0000-0000-000000000000" \
  -d '{"method": "tools/list", "params": {}}'
```

## 🔧 VS Code Konfiguration

### 1. Konfigurer MCP-integration

Opret VS Code MCP-konfiguration:

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

### 2. Konfigurer Python-miljø

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

### 3. Test VS Code-integration

1. **Åbn projektet i VS Code**:
   ```bash
   code .
   ```

2. **Åbn AI Chat**:
   - Tryk `Ctrl+Shift+P` (Windows/Linux) eller `Cmd+Shift+P` (macOS)
   - Skriv "AI Chat" og vælg "AI Chat: Open Chat"

3. **Test MCP-serverforbindelse**:
   - I AI Chat, skriv `#zava` og vælg en af de konfigurerede servere
   - Spørg: "Hvilke tabeller er tilgængelige i databasen?"
   - Du bør modtage et svar, der viser detaildatabasens tabeller

## ✅ Validering af Miljø

### 1. Omfattende Systemkontrol

Kør dette valideringsscript for at verificere din opsætning:

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

### 2. Manuel Valideringscheckliste

**✅ Grundlæggende Værktøjer**
- [ ] Docker version 20.10+ installeret og kører
- [ ] Azure CLI 2.40+ installeret og autentificeret
- [ ] Python 3.8+ med pip installeret
- [ ] Git 2.30+ installeret
- [ ] VS Code med nødvendige udvidelser

**✅ Azure-ressourcer**
- [ ] Ressourcegruppe oprettet succesfuldt
- [ ] AI Foundry-projekt implementeret
- [ ] OpenAI text-embedding-3-small-model implementeret
- [ ] Application Insights konfigureret
- [ ] Service principal oprettet med korrekte tilladelser

**✅ Miljøkonfiguration**
- [ ] `.env`-fil oprettet med alle nødvendige variabler
- [ ] Azure-legitimationsoplysninger fungerer (test med `az account show`)
- [ ] PostgreSQL-container kører og er tilgængelig
- [ ] Eksempeldata indlæst i databasen

**✅ VS Code-integration**
- [ ] `.vscode/mcp.json` konfigureret
- [ ] Python-interpreter sat til virtuelt miljø
- [ ] MCP-servere vises i AI Chat
- [ ] Kan udføre testforespørgsler via AI Chat

## 🛠️ Fejlfinding af Almindelige Problemer

### Docker Problemer

**Problem**: Docker-containere starter ikke
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

**Problem**: PostgreSQL-forbindelse fejler
```bash
# Check container logs
docker-compose logs postgres

# Verify container is healthy
docker-compose ps

# Test direct connection
docker-compose exec postgres psql -U postgres -d zava -c "SELECT 1;"
```

### Azure Implementeringsproblemer

**Problem**: Azure-implementering fejler
```bash
# Check Azure CLI authentication
az account show

# Verify subscription permissions
az role assignment list --assignee $(az account show --query user.name -o tsv)

# Check resource provider registration
az provider register --namespace Microsoft.CognitiveServices
az provider register --namespace Microsoft.Insights
```

**Problem**: AI-tjenesteautentificering fejler
```bash
# Test service principal
az login --service-principal \
  --username $AZURE_CLIENT_ID \
  --password $AZURE_CLIENT_SECRET \
  --tenant $AZURE_TENANT_ID

# Verify AI service deployment
az cognitiveservices account list --query "[].{Name:name,Kind:kind,Location:location}"
```

### Python Miljøproblemer

**Problem**: Installation af pakker fejler
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

**Problem**: VS Code kan ikke finde Python-interpreter
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

## 🎯 Vigtige Pointer

Efter at have gennemført denne lab, bør du have:

✅ **Komplet Udviklingsmiljø**: Alle værktøjer installeret og konfigureret  
✅ **Azure-ressourcer Implementeret**: AI-tjenester og understøttende infrastruktur  
✅ **Docker-miljø Kører**: PostgreSQL- og MCP-servercontainere  
✅ **VS Code-integration**: MCP-servere konfigureret og tilgængelige  
✅ **Valideret Opsætning**: Alle komponenter testet og fungerer sammen  
✅ **Fejlfinding Viden**: Almindelige problemer og løsninger  

## 🚀 Hvad Er Næste Skridt

Med dit miljø klar, fortsæt til **[Lab 04: Database Design and Schema](../04-Database/README.md)** for at:

- Udforske detaildatabasens skema i detaljer
- Forstå multi-tenant datamodellering
- Lære om implementering af Row Level Security
- Arbejde med eksempeldata fra detailhandlen

## 📚 Yderligere Ressourcer

### Udviklingsværktøjer
- [Docker Dokumentation](https://docs.docker.com/) - Komplet Docker-reference
- [Azure CLI Reference](https://docs.microsoft.com/cli/azure/) - Azure CLI-kommandoer
- [VS Code Dokumentation](https://code.visualstudio.com/docs) - Editor-konfiguration og udvidelser

### Azure-tjenester
- [Azure AI Foundry Dokumentation](https://docs.microsoft.com/azure/ai-foundry/) - AI-tjenestekonfiguration
- [Azure OpenAI Service](https://docs.microsoft.com/azure/cognitive-services/openai/) - AI-modelimplementering
- [Application Insights](https://docs.microsoft.com/azure/azure-monitor/app/app-insights-overview) - Overvågningsopsætning

### Python Udvikling
- [Python Virtuelle Miljøer](https://docs.python.org/3/tutorial/venv.html) - Miljøstyring
- [AsyncIO Dokumentation](https://docs.python.org/3/library/asyncio.html) - Asynkrone programmeringsmønstre
- [FastAPI Dokumentation](https://fastapi.tiangolo.com/) - Webframework-mønstre

---

**Næste**: Miljø klar? Fortsæt med [Lab 04: Database Design and Schema](../04-Database/README.md)

---

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal det bemærkes, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os ikke ansvar for eventuelle misforståelser eller fejltolkninger, der måtte opstå som følge af brugen af denne oversættelse.