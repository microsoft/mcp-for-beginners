# Omgevingsinstelling

## 🎯 Wat Deze Lab Behandelt

Deze praktische lab begeleidt je bij het opzetten van een complete ontwikkelomgeving voor het bouwen van MCP-servers met PostgreSQL-integratie. Je configureert alle benodigde tools, implementeert Azure-resources en valideert je setup voordat je verder gaat met de implementatie.

## Overzicht

Een goede ontwikkelomgeving is essentieel voor succesvolle MCP-serverontwikkeling. Deze lab biedt stapsgewijze instructies voor het instellen van Docker, Azure-services, ontwikkeltools en het valideren dat alles correct samenwerkt.

Aan het einde van deze lab heb je een volledig functionele ontwikkelomgeving klaar voor het bouwen van de Zava Retail MCP-server.

## Leerdoelen

Aan het einde van deze lab kun je:

- **Installeren en configureren** van alle benodigde ontwikkeltools
- **Azure-resources implementeren** die nodig zijn voor de MCP-server
- **Docker-containers instellen** voor PostgreSQL en de MCP-server
- **Valideren** van je omgevingsinstelling met testverbindingen
- **Problemen oplossen** met veelvoorkomende installatie- en configuratieproblemen
- **Begrijpen** van de ontwikkelworkflow en bestandsstructuur

## 📋 Controle van Vereisten

Voordat je begint, zorg ervoor dat je beschikt over:

### Vereiste Kennis
- Basisgebruik van de commandoregel (Windows Command Prompt/PowerShell)
- Begrip van omgevingsvariabelen
- Bekendheid met versiebeheer via Git
- Basisconcepten van Docker (containers, images, volumes)

### Systeemvereisten
- **Besturingssysteem**: Windows 10/11, macOS of Linux
- **RAM**: Minimaal 8GB (16GB aanbevolen)
- **Opslag**: Minimaal 10GB vrije ruimte
- **Netwerk**: Internetverbinding voor downloads en Azure-implementatie

### Accountvereisten
- **Azure-abonnement**: Gratis tier is voldoende
- **GitHub-account**: Voor toegang tot de repository
- **Docker Hub-account**: (Optioneel) Voor het publiceren van aangepaste images

## 🛠️ Installatie van Tools

### 1. Installeer Docker Desktop

Docker biedt de containeromgeving voor onze ontwikkelsetup.

#### Windows Installatie

1. **Download Docker Desktop**:
   ```cmd
   # Visit https://desktop.docker.com/win/stable/Docker%20Desktop%20Installer.exe
   # Or use Windows Package Manager
   winget install Docker.DockerDesktop
   ```

2. **Installeren en Configureren**:
   - Voer de installer uit als Administrator
   - Schakel WSL 2-integratie in wanneer hierom wordt gevraagd
   - Herstart je computer na voltooiing van de installatie

3. **Installatie Verifiëren**:
   ```cmd
   docker --version
   docker-compose --version
   ```

#### macOS Installatie

1. **Downloaden en Installeren**:
   ```bash
   # Download from https://desktop.docker.com/mac/stable/Docker.dmg
   # Or use Homebrew
   brew install --cask docker
   ```

2. **Start Docker Desktop**:
   - Start Docker Desktop vanuit Applicaties
   - Voltooi de initiële setup-wizard

3. **Installatie Verifiëren**:
   ```bash
   docker --version
   docker-compose --version
   ```

#### Linux Installatie

1. **Installeer Docker Engine**:
   ```bash
   # Ubuntu/Debian
   curl -fsSL https://get.docker.com -o get-docker.sh
   sudo sh get-docker.sh
   sudo usermod -aG docker $USER
   
   # Log out and back in for group changes to take effect
   ```

2. **Installeer Docker Compose**:
   ```bash
   sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
   sudo chmod +x /usr/local/bin/docker-compose
   ```

### 2. Installeer Azure CLI

De Azure CLI maakt implementatie en beheer van Azure-resources mogelijk.

#### Windows Installatie

```cmd
# Using Windows Package Manager
winget install Microsoft.AzureCLI

# Or download MSI from: https://aka.ms/installazurecliwindows
```

#### macOS Installatie

```bash
# Using Homebrew
brew install azure-cli

# Or using installer
curl -L https://aka.ms/InstallAzureCli | bash
```

#### Linux Installatie

```bash
# Ubuntu/Debian
curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash

# RHEL/CentOS
sudo rpm --import https://packages.microsoft.com/keys/microsoft.asc
sudo dnf install azure-cli
```

#### Verifiëren en Authenticeren

```bash
# Check installation
az version

# Login to Azure
az login

# Set default subscription (if you have multiple)
az account list --output table
az account set --subscription "Your-Subscription-Name"
```

### 3. Installeer Git

Git is nodig voor het klonen van de repository en versiebeheer.

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

### 4. Installeer VS Code

Visual Studio Code biedt de geïntegreerde ontwikkelomgeving met MCP-ondersteuning.

#### Installatie

```cmd
# Windows
winget install Microsoft.VisualStudioCode

# macOS
brew install --cask visual-studio-code

# Linux (Ubuntu/Debian)
sudo snap install code --classic
```

#### Vereiste Extensies

Installeer deze VS Code-extensies:

```bash
# Install via command line
code --install-extension ms-python.python
code --install-extension ms-vscode.vscode-json
code --install-extension ms-azuretools.vscode-docker
code --install-extension ms-vscode.azure-account
```

Of installeer via VS Code:
1. Open VS Code
2. Ga naar Extensies (Ctrl+Shift+X)
3. Installeer:
   - **Python** (Microsoft)
   - **Docker** (Microsoft)
   - **Azure Account** (Microsoft)
   - **JSON** (Microsoft)

### 5. Installeer Python

Python 3.8+ is vereist voor MCP-serverontwikkeling.

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

#### Installatie Verifiëren

```bash
python --version  # Should show Python 3.11.x
pip --version      # Should show pip version
```

## 🚀 Projectinstelling

### 1. Clone de Repository

```bash
# Clone the main repository
git clone https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail.git

# Navigate to the project directory
cd MCP-Server-and-PostgreSQL-Sample-Retail

# Verify repository structure
ls -la
```

### 2. Maak een Python Virtuele Omgeving

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

### 3. Installeer Python-afhankelijkheden

```bash
# Install development dependencies
pip install -r requirements.lock.txt

# Verify key packages
pip list | grep fastmcp
pip list | grep asyncpg
pip list | grep azure
```

## ☁️ Implementatie van Azure-resources

### 1. Begrijp Resourcevereisten

Onze MCP-server vereist de volgende Azure-resources:

| **Resource** | **Doel** | **Geschatte Kosten** |
|--------------|----------|----------------------|
| **Azure AI Foundry** | Hosting en beheer van AI-modellen | $10-50/maand |
| **OpenAI-implementatie** | Tekstembedding-model (text-embedding-3-small) | $5-20/maand |
| **Application Insights** | Monitoring en telemetrie | $5-15/maand |
| **Resourcegroep** | Organisatie van resources | Gratis |

### 2. Implementeer Azure-resources

#### Optie A: Geautomatiseerde Implementatie (Aanbevolen)

```bash
# Navigate to infrastructure directory
cd infra

# Windows - PowerShell
./deploy.ps1

# macOS/Linux - Bash
./deploy.sh
```

Het implementatiescript zal:
1. Een unieke resourcegroep maken
2. Azure AI Foundry-resources implementeren
3. Het text-embedding-3-small model implementeren
4. Application Insights configureren
5. Een serviceprincipal maken voor authenticatie
6. Een `.env`-bestand genereren met configuratie

#### Optie B: Handmatige Implementatie

Als je de voorkeur geeft aan handmatige controle of het geautomatiseerde script faalt:

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

### 3. Verifieer Azure-implementatie

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

### 4. Configureer Omgevingsvariabelen

Na implementatie zou je een `.env`-bestand moeten hebben. Controleer of het bevat:

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

## 🐳 Docker Omgevingsinstelling

### 1. Begrijp Docker-compositie

Onze ontwikkelomgeving maakt gebruik van Docker Compose:

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

### 2. Start de Ontwikkelomgeving

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

### 3. Verifieer Database-instelling

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

## 🔧 VS Code Configuratie

### 1. Configureer MCP-integratie

Maak VS Code MCP-configuratie:

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

### 2. Configureer Python-omgeving

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

### 3. Test VS Code-integratie

1. **Open het project in VS Code**:
   ```bash
   code .
   ```

2. **Open AI Chat**:
   - Druk op `Ctrl+Shift+P` (Windows/Linux) of `Cmd+Shift+P` (macOS)
   - Typ "AI Chat" en selecteer "AI Chat: Open Chat"

3. **Test MCP-serververbinding**:
   - In AI Chat, typ `#zava` en selecteer een van de geconfigureerde servers
   - Vraag: "Welke tabellen zijn beschikbaar in de database?"
   - Je zou een antwoord moeten ontvangen met een lijst van de retail-databasetabellen

## ✅ Validatie van de Omgeving

### 1. Uitgebreide Systeemcontrole

Voer dit validatiescript uit om je setup te verifiëren:

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

### 2. Handmatige Validatie Checklist

**✅ Basis Tools**
- [ ] Docker versie 20.10+ geïnstalleerd en actief
- [ ] Azure CLI 2.40+ geïnstalleerd en geauthenticeerd
- [ ] Python 3.8+ met pip geïnstalleerd
- [ ] Git 2.30+ geïnstalleerd
- [ ] VS Code met vereiste extensies

**✅ Azure-resources**
- [ ] Resourcegroep succesvol aangemaakt
- [ ] AI Foundry-project geïmplementeerd
- [ ] OpenAI text-embedding-3-small model geïmplementeerd
- [ ] Application Insights geconfigureerd
- [ ] Serviceprincipal gemaakt met de juiste permissies

**✅ Omgevingsconfiguratie**
- [ ] `.env`-bestand aangemaakt met alle vereiste variabelen
- [ ] Azure-credentials werken (test met `az account show`)
- [ ] PostgreSQL-container actief en toegankelijk
- [ ] Voorbeelddata geladen in database

**✅ VS Code-integratie**
- [ ] `.vscode/mcp.json` geconfigureerd
- [ ] Python-interpreter ingesteld op virtuele omgeving
- [ ] MCP-servers verschijnen in AI Chat
- [ ] Testqueries kunnen worden uitgevoerd via AI Chat

## 🛠️ Veelvoorkomende Problemen Oplossen

### Docker Problemen

**Probleem**: Docker-containers starten niet
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

**Probleem**: PostgreSQL-verbinding mislukt
```bash
# Check container logs
docker-compose logs postgres

# Verify container is healthy
docker-compose ps

# Test direct connection
docker-compose exec postgres psql -U postgres -d zava -c "SELECT 1;"
```

### Azure Implementatieproblemen

**Probleem**: Azure-implementatie mislukt
```bash
# Check Azure CLI authentication
az account show

# Verify subscription permissions
az role assignment list --assignee $(az account show --query user.name -o tsv)

# Check resource provider registration
az provider register --namespace Microsoft.CognitiveServices
az provider register --namespace Microsoft.Insights
```

**Probleem**: Authenticatie van AI-service mislukt
```bash
# Test service principal
az login --service-principal \
  --username $AZURE_CLIENT_ID \
  --password $AZURE_CLIENT_SECRET \
  --tenant $AZURE_TENANT_ID

# Verify AI service deployment
az cognitiveservices account list --query "[].{Name:name,Kind:kind,Location:location}"
```

### Python Omgevingsproblemen

**Probleem**: Installatie van pakketten mislukt
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

**Probleem**: VS Code kan Python-interpreter niet vinden
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

## 🎯 Belangrijke Punten

Na het voltooien van deze lab zou je moeten hebben:

✅ **Complete Ontwikkelomgeving**: Alle tools geïnstalleerd en geconfigureerd  
✅ **Azure-resources geïmplementeerd**: AI-services en ondersteunende infrastructuur  
✅ **Docker-omgeving actief**: PostgreSQL- en MCP-servercontainers  
✅ **VS Code-integratie**: MCP-servers geconfigureerd en toegankelijk  
✅ **Gevalideerde Setup**: Alle componenten getest en werkend samen  
✅ **Probleemoplossingskennis**: Veelvoorkomende problemen en oplossingen  

## 🚀 Wat Nu?

Met je omgeving gereed, ga verder met **[Lab 04: Databaseontwerp en Schema](../04-Database/README.md)** om:

- Het retail-databaseschema in detail te verkennen
- Multi-tenant datamodellering te begrijpen
- Meer te leren over implementatie van Row Level Security
- Werken met voorbeeld retaildata

## 📚 Aanvullende Bronnen

### Ontwikkeltools
- [Docker Documentatie](https://docs.docker.com/) - Complete Docker-referentie
- [Azure CLI Referentie](https://docs.microsoft.com/cli/azure/) - Azure CLI-commando's
- [VS Code Documentatie](https://code.visualstudio.com/docs) - Editorconfiguratie en extensies

### Azure Services
- [Azure AI Foundry Documentatie](https://docs.microsoft.com/azure/ai-foundry/) - Configuratie van AI-services
- [Azure OpenAI Service](https://docs.microsoft.com/azure/cognitive-services/openai/) - Implementatie van AI-modellen
- [Application Insights](https://docs.microsoft.com/azure/azure-monitor/app/app-insights-overview) - Monitoringinstelling

### Python Ontwikkeling
- [Python Virtuele Omgevingen](https://docs.python.org/3/tutorial/venv.html) - Beheer van omgevingen
- [AsyncIO Documentatie](https://docs.python.org/3/library/asyncio.html) - Async programmeerpatronen
- [FastAPI Documentatie](https://fastapi.tiangolo.com/) - Webframeworkpatronen

---

**Volgende**: Omgeving gereed? Ga verder met [Lab 04: Databaseontwerp en Schema](../04-Database/README.md)

---

**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsservice [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u zich ervan bewust te zijn dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor cruciale informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.