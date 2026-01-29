# Miljöinställning

## 🎯 Vad Denna Lab Täcker

Denna praktiska labb guidar dig genom att sätta upp en komplett utvecklingsmiljö för att bygga MCP-servrar med PostgreSQL-integration. Du kommer att konfigurera alla nödvändiga verktyg, distribuera Azure-resurser och validera din installation innan du går vidare med implementeringen.

## Översikt

En korrekt utvecklingsmiljö är avgörande för framgångsrik utveckling av MCP-servrar. Denna labb ger steg-för-steg-instruktioner för att installera Docker, Azure-tjänster, utvecklingsverktyg och validera att allt fungerar korrekt tillsammans.

I slutet av denna labb kommer du att ha en fullt fungerande utvecklingsmiljö redo för att bygga Zava Retail MCP-servern.

## Lärandemål

I slutet av denna labb kommer du att kunna:

- **Installera och konfigurera** alla nödvändiga utvecklingsverktyg
- **Distribuera Azure-resurser** som behövs för MCP-servern
- **Sätta upp Docker-containrar** för PostgreSQL och MCP-servern
- **Validera** din miljöinstallation med testanslutningar
- **Felsöka** vanliga installationsproblem och konfigurationsfel
- **Förstå** utvecklingsarbetsflödet och filstrukturen

## 📋 Förutsättningar

Innan du börjar, se till att du har:

### Nödvändig Kunskap
- Grundläggande användning av kommandoraden (Windows Command Prompt/PowerShell)
- Förståelse för miljövariabler
- Grundläggande kunskap om Git versionskontroll
- Grundläggande Docker-koncept (containrar, bilder, volymer)

### Systemkrav
- **Operativsystem**: Windows 10/11, macOS eller Linux
- **RAM**: Minst 8GB (16GB rekommenderas)
- **Lagring**: Minst 10GB ledigt utrymme
- **Nätverk**: Internetanslutning för nedladdningar och Azure-distribution

### Kontokrav
- **Azure-abonnemang**: Gratisnivå är tillräcklig
- **GitHub-konto**: För åtkomst till repository
- **Docker Hub-konto**: (Valfritt) För publicering av anpassade bilder

## 🛠️ Verktygsinstallation

### 1. Installera Docker Desktop

Docker tillhandahåller den containeriserade miljön för vår utvecklingsinstallation.

#### Installation på Windows

1. **Ladda ner Docker Desktop**:
   ```cmd
   # Visit https://desktop.docker.com/win/stable/Docker%20Desktop%20Installer.exe
   # Or use Windows Package Manager
   winget install Docker.DockerDesktop
   ```

2. **Installera och konfigurera**:
   - Kör installationsprogrammet som administratör
   - Aktivera WSL 2-integration när du blir tillfrågad
   - Starta om datorn när installationen är klar

3. **Verifiera installationen**:
   ```cmd
   docker --version
   docker-compose --version
   ```

#### Installation på macOS

1. **Ladda ner och installera**:
   ```bash
   # Download from https://desktop.docker.com/mac/stable/Docker.dmg
   # Or use Homebrew
   brew install --cask docker
   ```

2. **Starta Docker Desktop**:
   - Starta Docker Desktop från Program
   - Slutför den initiala installationsguiden

3. **Verifiera installationen**:
   ```bash
   docker --version
   docker-compose --version
   ```

#### Installation på Linux

1. **Installera Docker Engine**:
   ```bash
   # Ubuntu/Debian
   curl -fsSL https://get.docker.com -o get-docker.sh
   sudo sh get-docker.sh
   sudo usermod -aG docker $USER
   
   # Log out and back in for group changes to take effect
   ```

2. **Installera Docker Compose**:
   ```bash
   sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
   sudo chmod +x /usr/local/bin/docker-compose
   ```

### 2. Installera Azure CLI

Azure CLI möjliggör distribution och hantering av Azure-resurser.

#### Installation på Windows

```cmd
# Using Windows Package Manager
winget install Microsoft.AzureCLI

# Or download MSI from: https://aka.ms/installazurecliwindows
```

#### Installation på macOS

```bash
# Using Homebrew
brew install azure-cli

# Or using installer
curl -L https://aka.ms/InstallAzureCli | bash
```

#### Installation på Linux

```bash
# Ubuntu/Debian
curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash

# RHEL/CentOS
sudo rpm --import https://packages.microsoft.com/keys/microsoft.asc
sudo dnf install azure-cli
```

#### Verifiera och autentisera

```bash
# Check installation
az version

# Login to Azure
az login

# Set default subscription (if you have multiple)
az account list --output table
az account set --subscription "Your-Subscription-Name"
```

### 3. Installera Git

Git krävs för att klona repository och versionskontroll.

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

### 4. Installera VS Code

Visual Studio Code tillhandahåller den integrerade utvecklingsmiljön med MCP-stöd.

#### Installation

```cmd
# Windows
winget install Microsoft.VisualStudioCode

# macOS
brew install --cask visual-studio-code

# Linux (Ubuntu/Debian)
sudo snap install code --classic
```

#### Nödvändiga tillägg

Installera dessa VS Code-tillägg:

```bash
# Install via command line
code --install-extension ms-python.python
code --install-extension ms-vscode.vscode-json
code --install-extension ms-azuretools.vscode-docker
code --install-extension ms-vscode.azure-account
```

Eller installera via VS Code:
1. Öppna VS Code
2. Gå till Tillägg (Ctrl+Shift+X)
3. Installera:
   - **Python** (Microsoft)
   - **Docker** (Microsoft)
   - **Azure Account** (Microsoft)
   - **JSON** (Microsoft)

### 5. Installera Python

Python 3.8+ krävs för utveckling av MCP-servern.

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

#### Verifiera installationen

```bash
python --version  # Should show Python 3.11.x
pip --version      # Should show pip version
```

## 🚀 Projektinstallation

### 1. Klona repository

```bash
# Clone the main repository
git clone https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail.git

# Navigate to the project directory
cd MCP-Server-and-PostgreSQL-Sample-Retail

# Verify repository structure
ls -la
```

### 2. Skapa Python-virtuell miljö

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

### 3. Installera Python-beroenden

```bash
# Install development dependencies
pip install -r requirements.lock.txt

# Verify key packages
pip list | grep fastmcp
pip list | grep asyncpg
pip list | grep azure
```

## ☁️ Azure-resursdistribution

### 1. Förstå resurskrav

Vår MCP-server kräver dessa Azure-resurser:

| **Resurs** | **Syfte** | **Beräknad kostnad** |
|------------|-----------|---------------------|
| **Azure AI Foundry** | AI-modellhosting och hantering | $10-50/månad |
| **OpenAI-distribution** | Textinbäddningsmodell (text-embedding-3-small) | $5-20/månad |
| **Application Insights** | Övervakning och telemetri | $5-15/månad |
| **Resursgrupp** | Resursorganisation | Gratis |

### 2. Distribuera Azure-resurser

#### Alternativ A: Automatisk distribution (Rekommenderas)

```bash
# Navigate to infrastructure directory
cd infra

# Windows - PowerShell
./deploy.ps1

# macOS/Linux - Bash
./deploy.sh
```

Distributionsskriptet kommer att:
1. Skapa en unik resursgrupp
2. Distribuera Azure AI Foundry-resurser
3. Distribuera text-embedding-3-small-modellen
4. Konfigurera Application Insights
5. Skapa en tjänstehuvudman för autentisering
6. Generera `.env`-fil med konfiguration

#### Alternativ B: Manuell distribution

Om du föredrar manuell kontroll eller om det automatiska skriptet misslyckas:

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

### 3. Verifiera Azure-distribution

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

### 4. Konfigurera miljövariabler

Efter distributionen bör du ha en `.env`-fil. Verifiera att den innehåller:

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

## 🐳 Docker-miljöinställning

### 1. Förstå Docker-komposition

Vår utvecklingsmiljö använder Docker Compose:

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

### 2. Starta utvecklingsmiljön

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

### 3. Verifiera databasinställning

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

### 4. Testa MCP-server

```bash
# Check MCP server health
curl http://localhost:8000/health

# Test basic MCP endpoint
curl -X POST http://localhost:8000/mcp \
  -H "Content-Type: application/json" \
  -H "x-rls-user-id: 00000000-0000-0000-0000-000000000000" \
  -d '{"method": "tools/list", "params": {}}'
```

## 🔧 VS Code-konfiguration

### 1. Konfigurera MCP-integration

Skapa VS Code MCP-konfiguration:

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

### 2. Konfigurera Python-miljö

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

### 3. Testa VS Code-integration

1. **Öppna projektet i VS Code**:
   ```bash
   code .
   ```

2. **Öppna AI Chat**:
   - Tryck `Ctrl+Shift+P` (Windows/Linux) eller `Cmd+Shift+P` (macOS)
   - Skriv "AI Chat" och välj "AI Chat: Open Chat"

3. **Testa MCP-serveranslutning**:
   - I AI Chat, skriv `#zava` och välj en av de konfigurerade servrarna
   - Fråga: "Vilka tabeller finns tillgängliga i databasen?"
   - Du bör få ett svar som listar detaljhandelns databastabeller

## ✅ Miljövalidering

### 1. Omfattande systemkontroll

Kör detta valideringsskript för att verifiera din installation:

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

### 2. Manuell valideringschecklista

**✅ Grundläggande verktyg**
- [ ] Docker version 20.10+ installerad och körs
- [ ] Azure CLI 2.40+ installerad och autentiserad
- [ ] Python 3.8+ med pip installerad
- [ ] Git 2.30+ installerad
- [ ] VS Code med nödvändiga tillägg

**✅ Azure-resurser**
- [ ] Resursgrupp skapad framgångsrikt
- [ ] AI Foundry-projekt distribuerat
- [ ] OpenAI text-embedding-3-small-modell distribuerad
- [ ] Application Insights konfigurerad
- [ ] Tjänstehuvudman skapad med rätt behörigheter

**✅ Miljökonfiguration**
- [ ] `.env`-fil skapad med alla nödvändiga variabler
- [ ] Azure-autentisering fungerar (testa med `az account show`)
- [ ] PostgreSQL-container körs och är åtkomlig
- [ ] Exempeldata laddad i databasen

**✅ VS Code-integration**
- [ ] `.vscode/mcp.json` konfigurerad
- [ ] Python-tolk inställd på virtuell miljö
- [ ] MCP-servrar visas i AI Chat
- [ ] Kan köra testfrågor via AI Chat

## 🛠️ Felsökning av vanliga problem

### Docker-problem

**Problem**: Docker-containrar startar inte
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

**Problem**: PostgreSQL-anslutning misslyckas
```bash
# Check container logs
docker-compose logs postgres

# Verify container is healthy
docker-compose ps

# Test direct connection
docker-compose exec postgres psql -U postgres -d zava -c "SELECT 1;"
```

### Azure-distributionsproblem

**Problem**: Azure-distribution misslyckas
```bash
# Check Azure CLI authentication
az account show

# Verify subscription permissions
az role assignment list --assignee $(az account show --query user.name -o tsv)

# Check resource provider registration
az provider register --namespace Microsoft.CognitiveServices
az provider register --namespace Microsoft.Insights
```

**Problem**: AI-tjänstens autentisering misslyckas
```bash
# Test service principal
az login --service-principal \
  --username $AZURE_CLIENT_ID \
  --password $AZURE_CLIENT_SECRET \
  --tenant $AZURE_TENANT_ID

# Verify AI service deployment
az cognitiveservices account list --query "[].{Name:name,Kind:kind,Location:location}"
```

### Python-miljöproblem

**Problem**: Paketinstallation misslyckas
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

**Problem**: VS Code hittar inte Python-tolk
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

## 🎯 Viktiga Slutsatser

Efter att ha slutfört denna labb bör du ha:

✅ **Komplett utvecklingsmiljö**: Alla verktyg installerade och konfigurerade  
✅ **Azure-resurser distribuerade**: AI-tjänster och stödjande infrastruktur  
✅ **Docker-miljö igång**: PostgreSQL- och MCP-servercontainrar  
✅ **VS Code-integration**: MCP-servrar konfigurerade och åtkomliga  
✅ **Validerad installation**: Alla komponenter testade och fungerar tillsammans  
✅ **Felsökningskunskap**: Vanliga problem och lösningar  

## 🚀 Vad Nästa

Med din miljö redo, fortsätt till **[Lab 04: Databasedesign och Schema](../04-Database/README.md)** för att:

- Utforska detaljhandelns databasschema i detalj
- Förstå multi-tenant datamodellering
- Lära dig om implementering av radnivåsäkerhet
- Arbeta med exempeldata för detaljhandel

## 📚 Ytterligare Resurser

### Utvecklingsverktyg
- [Docker-dokumentation](https://docs.docker.com/) - Komplett Docker-referens
- [Azure CLI-referens](https://docs.microsoft.com/cli/azure/) - Azure CLI-kommandon
- [VS Code-dokumentation](https://code.visualstudio.com/docs) - Editor-konfiguration och tillägg

### Azure-tjänster
- [Azure AI Foundry-dokumentation](https://docs.microsoft.com/azure/ai-foundry/) - AI-tjänstkonfiguration
- [Azure OpenAI-tjänst](https://docs.microsoft.com/azure/cognitive-services/openai/) - AI-modelldistribution
- [Application Insights](https://docs.microsoft.com/azure/azure-monitor/app/app-insights-overview) - Övervakningsinställning

### Python-utveckling
- [Python virtuella miljöer](https://docs.python.org/3/tutorial/venv.html) - Miljöhantering
- [AsyncIO-dokumentation](https://docs.python.org/3/library/asyncio.html) - Asynkrona programmeringsmönster
- [FastAPI-dokumentation](https://fastapi.tiangolo.com/) - Webbframework-mönster

---

**Nästa**: Miljön redo? Fortsätt med [Lab 04: Databasedesign och Schema](../04-Database/README.md)

---

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, bör det noteras att automatiserade översättningar kan innehålla fel eller felaktigheter. Det ursprungliga dokumentet på dess originalspråk bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för eventuella missförstånd eller feltolkningar som uppstår vid användning av denna översättning.