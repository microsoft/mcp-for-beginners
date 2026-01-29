# Keskkonna seadistamine

## 🎯 Mida see labor hõlmab

See praktiline labor juhendab teid täieliku arenduskeskkonna seadistamisel MCP serverite loomiseks PostgreSQL integratsiooniga. Seadistate kõik vajalikud tööriistad, juurutate Azure'i ressursid ja valideerite oma seadistuse enne rakendamisega alustamist.

## Ülevaade

Korralik arenduskeskkond on MCP serverite edukaks arendamiseks hädavajalik. See labor pakub samm-sammulisi juhiseid Docker'i, Azure'i teenuste ja arendustööriistade seadistamiseks ning kontrollib, et kõik toimiks korrektselt koos.

Labori lõpuks on teil täielikult toimiv arenduskeskkond Zava Retail MCP serveri loomiseks.

## Õpieesmärgid

Labori lõpuks suudate:

- **Installida ja seadistada** kõik vajalikud arendustööriistad
- **Juurutada Azure'i ressursid**, mis on vajalikud MCP serveri jaoks
- **Seadistada Docker'i konteinerid** PostgreSQL-i ja MCP serveri jaoks
- **Valideerida** oma keskkonna seadistust testühendustega
- **Lahendada** levinud seadistusprobleeme ja konfiguratsioonivigu
- **Mõista** arendusvoogu ja failistruktuuri

## 📋 Eeltingimuste kontroll

Enne alustamist veenduge, et teil on:

### Vajalikud teadmised
- Põhiline käsurea kasutamine (Windows Command Prompt/PowerShell)
- Keskkonnamuutujate mõistmine
- Git versioonihalduse tundmine
- Põhilised Docker'i kontseptsioonid (konteinerid, pildid, mahud)

### Süsteeminõuded
- **Operatsioonisüsteem**: Windows 10/11, macOS või Linux
- **RAM**: Minimaalselt 8GB (soovitatavalt 16GB)
- **Salvestusruum**: Vähemalt 10GB vaba ruumi
- **Võrk**: Internetiühendus allalaadimisteks ja Azure'i juurutamiseks

### Konto nõuded
- **Azure'i tellimus**: Tasuta tase on piisav
- **GitHubi konto**: Repositooriumi juurdepääsuks
- **Docker Hubi konto**: (Valikuline) Kohandatud piltide avaldamiseks

## 🛠️ Tööriistade paigaldamine

### 1. Paigaldage Docker Desktop

Docker pakub konteineriseeritud keskkonda meie arendusseadistuseks.

#### Windowsi paigaldamine

1. **Laadige alla Docker Desktop**:
   ```cmd
   # Visit https://desktop.docker.com/win/stable/Docker%20Desktop%20Installer.exe
   # Or use Windows Package Manager
   winget install Docker.DockerDesktop
   ```

2. **Paigaldage ja seadistage**:
   - Käivitage paigaldaja administraatorina
   - Lubage WSL 2 integratsioon, kui küsitakse
   - Taaskäivitage arvuti pärast paigaldamise lõpetamist

3. **Kontrollige paigaldust**:
   ```cmd
   docker --version
   docker-compose --version
   ```

#### macOS-i paigaldamine

1. **Laadige alla ja paigaldage**:
   ```bash
   # Download from https://desktop.docker.com/mac/stable/Docker.dmg
   # Or use Homebrew
   brew install --cask docker
   ```

2. **Käivitage Docker Desktop**:
   - Käivitage Docker Desktop rakendustest
   - Täitke algseadistuse viisard

3. **Kontrollige paigaldust**:
   ```bash
   docker --version
   docker-compose --version
   ```

#### Linuxi paigaldamine

1. **Paigaldage Docker Engine**:
   ```bash
   # Ubuntu/Debian
   curl -fsSL https://get.docker.com -o get-docker.sh
   sudo sh get-docker.sh
   sudo usermod -aG docker $USER
   
   # Log out and back in for group changes to take effect
   ```

2. **Paigaldage Docker Compose**:
   ```bash
   sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
   sudo chmod +x /usr/local/bin/docker-compose
   ```

### 2. Paigaldage Azure CLI

Azure CLI võimaldab Azure'i ressursside juurutamist ja haldamist.

#### Windowsi paigaldamine

```cmd
# Using Windows Package Manager
winget install Microsoft.AzureCLI

# Or download MSI from: https://aka.ms/installazurecliwindows
```

#### macOS-i paigaldamine

```bash
# Using Homebrew
brew install azure-cli

# Or using installer
curl -L https://aka.ms/InstallAzureCli | bash
```

#### Linuxi paigaldamine

```bash
# Ubuntu/Debian
curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash

# RHEL/CentOS
sudo rpm --import https://packages.microsoft.com/keys/microsoft.asc
sudo dnf install azure-cli
```

#### Kontrollige ja autentige

```bash
# Check installation
az version

# Login to Azure
az login

# Set default subscription (if you have multiple)
az account list --output table
az account set --subscription "Your-Subscription-Name"
```

### 3. Paigaldage Git

Git on vajalik repositooriumi kloonimiseks ja versioonihalduseks.

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

### 4. Paigaldage VS Code

Visual Studio Code pakub integreeritud arenduskeskkonda MCP toetusega.

#### Paigaldamine

```cmd
# Windows
winget install Microsoft.VisualStudioCode

# macOS
brew install --cask visual-studio-code

# Linux (Ubuntu/Debian)
sudo snap install code --classic
```

#### Vajalikud laiendused

Paigaldage need VS Code'i laiendused:

```bash
# Install via command line
code --install-extension ms-python.python
code --install-extension ms-vscode.vscode-json
code --install-extension ms-azuretools.vscode-docker
code --install-extension ms-vscode.azure-account
```

Või paigaldage VS Code'i kaudu:
1. Avage VS Code
2. Minge laienduste juurde (Ctrl+Shift+X)
3. Paigaldage:
   - **Python** (Microsoft)
   - **Docker** (Microsoft)
   - **Azure Account** (Microsoft)
   - **JSON** (Microsoft)

### 5. Paigaldage Python

Python 3.8+ on vajalik MCP serveri arendamiseks.

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

#### Kontrollige paigaldust

```bash
python --version  # Should show Python 3.11.x
pip --version      # Should show pip version
```

## 🚀 Projekti seadistamine

### 1. Kloonige repositoorium

```bash
# Clone the main repository
git clone https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail.git

# Navigate to the project directory
cd MCP-Server-and-PostgreSQL-Sample-Retail

# Verify repository structure
ls -la
```

### 2. Looge Python'i virtuaalne keskkond

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

### 3. Paigaldage Python'i sõltuvused

```bash
# Install development dependencies
pip install -r requirements.lock.txt

# Verify key packages
pip list | grep fastmcp
pip list | grep asyncpg
pip list | grep azure
```

## ☁️ Azure'i ressursside juurutamine

### 1. Ressursinõuete mõistmine

Meie MCP server vajab järgmisi Azure'i ressursse:

| **Ressurss** | **Eesmärk** | **Hinnanguline kulu** |
|--------------|-------------|-----------------------|
| **Azure AI Foundry** | AI mudelite majutamine ja haldamine | $10-50/kuus |
| **OpenAI juurutamine** | Teksti embedimise mudel (text-embedding-3-small) | $5-20/kuus |
| **Application Insights** | Jälgimine ja telemeetria | $5-15/kuus |
| **Ressursigrupp** | Ressursside organiseerimine | Tasuta |

### 2. Azure'i ressursside juurutamine

#### Valik A: Automaatne juurutamine (soovitatav)

```bash
# Navigate to infrastructure directory
cd infra

# Windows - PowerShell
./deploy.ps1

# macOS/Linux - Bash
./deploy.sh
```

Juurutusskript teeb järgmist:
1. Loob unikaalse ressursigrupi
2. Juurutab Azure AI Foundry ressursid
3. Juurutab text-embedding-3-small mudeli
4. Konfigureerib Application Insights'i
5. Loob autentimiseks teenusepõhimõtte
6. Genereerib `.env` faili konfiguratsiooniga

#### Valik B: Käsitsi juurutamine

Kui eelistate käsitsi kontrolli või automaatne skript ebaõnnestub:

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

### 3. Kontrollige Azure'i juurutust

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

### 4. Konfigureerige keskkonnamuutujad

Pärast juurutamist peaks teil olema `.env` fail. Kontrollige, et see sisaldab:

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

## 🐳 Docker'i keskkonna seadistamine

### 1. Docker Compose'i mõistmine

Meie arenduskeskkond kasutab Docker Compose'i:

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

### 2. Käivitage arenduskeskkond

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

### 3. Kontrollige andmebaasi seadistust

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

### 4. Testige MCP serverit

```bash
# Check MCP server health
curl http://localhost:8000/health

# Test basic MCP endpoint
curl -X POST http://localhost:8000/mcp \
  -H "Content-Type: application/json" \
  -H "x-rls-user-id: 00000000-0000-0000-0000-000000000000" \
  -d '{"method": "tools/list", "params": {}}'
```

## 🔧 VS Code'i konfiguratsioon

### 1. Konfigureerige MCP integratsioon

Looge VS Code'i MCP konfiguratsioon:

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

### 2. Konfigureerige Python'i keskkond

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

### 3. Testige VS Code'i integratsiooni

1. **Avage projekt VS Code'is**:
   ```bash
   code .
   ```

2. **Avage AI vestlus**:
   - Vajutage `Ctrl+Shift+P` (Windows/Linux) või `Cmd+Shift+P` (macOS)
   - Sisestage "AI Chat" ja valige "AI Chat: Open Chat"

3. **Testige MCP serveri ühendust**:
   - AI vestluses sisestage `#zava` ja valige üks konfigureeritud serveritest
   - Küsige: "Millised tabelid on andmebaasis saadaval?"
   - Peaksite saama vastuse, mis loetleb jaemüügi andmebaasi tabelid

## ✅ Keskkonna valideerimine

### 1. Põhjalik süsteemi kontroll

Käivitage see valideerimisskript, et kontrollida oma seadistust:

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

### 2. Käsitsi valideerimise kontrollnimekiri

**✅ Põhitööriistad**
- [ ] Docker versioon 20.10+ paigaldatud ja töötab
- [ ] Azure CLI 2.40+ paigaldatud ja autentitud
- [ ] Python 3.8+ koos pip'iga paigaldatud
- [ ] Git 2.30+ paigaldatud
- [ ] VS Code koos vajalike laiendustega

**✅ Azure'i ressursid**
- [ ] Ressursigrupp edukalt loodud
- [ ] AI Foundry projekt juurutatud
- [ ] OpenAI text-embedding-3-small mudel juurutatud
- [ ] Application Insights konfigureeritud
- [ ] Teenusepõhimõte loodud õigete õigustega

**✅ Keskkonna konfiguratsioon**
- [ ] `.env` fail loodud kõigi vajalike muutujatega
- [ ] Azure'i mandaadid töötavad (testige `az account show` abil)
- [ ] PostgreSQL konteiner töötab ja on ligipääsetav
- [ ] Näidisandmed andmebaasi laaditud

**✅ VS Code'i integratsioon**
- [ ] `.vscode/mcp.json` konfigureeritud
- [ ] Python'i tõlgendaja seadistatud virtuaalsele keskkonnale
- [ ] MCP serverid ilmuvad AI vestluses
- [ ] Saab käivitada testpäringuid AI vestluse kaudu

## 🛠️ Levinud probleemide lahendamine

### Docker'i probleemid

**Probleem**: Docker'i konteinerid ei käivitu
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

**Probleem**: PostgreSQL-i ühendus ebaõnnestub
```bash
# Check container logs
docker-compose logs postgres

# Verify container is healthy
docker-compose ps

# Test direct connection
docker-compose exec postgres psql -U postgres -d zava -c "SELECT 1;"
```

### Azure'i juurutamise probleemid

**Probleem**: Azure'i juurutamine ebaõnnestub
```bash
# Check Azure CLI authentication
az account show

# Verify subscription permissions
az role assignment list --assignee $(az account show --query user.name -o tsv)

# Check resource provider registration
az provider register --namespace Microsoft.CognitiveServices
az provider register --namespace Microsoft.Insights
```

**Probleem**: AI teenuse autentimine ebaõnnestub
```bash
# Test service principal
az login --service-principal \
  --username $AZURE_CLIENT_ID \
  --password $AZURE_CLIENT_SECRET \
  --tenant $AZURE_TENANT_ID

# Verify AI service deployment
az cognitiveservices account list --query "[].{Name:name,Kind:kind,Location:location}"
```

### Python'i keskkonna probleemid

**Probleem**: Paketi paigaldamine ebaõnnestub
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

**Probleem**: VS Code ei leia Python'i tõlgendajat
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

## 🎯 Peamised õppetunnid

Pärast selle labori lõpetamist peaks teil olema:

✅ **Täielik arenduskeskkond**: Kõik tööriistad paigaldatud ja konfigureeritud  
✅ **Azure'i ressursid juurutatud**: AI teenused ja toetav infrastruktuur  
✅ **Docker'i keskkond töötab**: PostgreSQL-i ja MCP serveri konteinerid  
✅ **VS Code'i integratsioon**: MCP serverid konfigureeritud ja ligipääsetavad  
✅ **Valideeritud seadistus**: Kõik komponendid testitud ja koos töötavad  
✅ **Probleemide lahendamise oskused**: Levinud probleemid ja lahendused  

## 🚀 Mis edasi

Kui teie keskkond on valmis, jätkake **[Labor 04: Andmebaasi disain ja skeem](../04-Database/README.md)**, et:

- Uurida jaemüügi andmebaasi skeemi üksikasjalikult
- Mõista mitme rentniku andmemudelit
- Õppida ridade taseme turvalisuse rakendamist
- Töötada näidisjaemüügi andmetega

## 📚 Lisamaterjalid

### Arendustööriistad
- [Docker'i dokumentatsioon](https://docs.docker.com/) - Täielik Docker'i viide
- [Azure CLI viide](https://docs.microsoft.com/cli/azure/) - Azure CLI käsud
- [VS Code'i dokumentatsioon](https://code.visualstudio.com/docs) - Redaktori konfiguratsioon ja laiendused

### Azure'i teenused
- [Azure AI Foundry dokumentatsioon](https://docs.microsoft.com/azure/ai-foundry/) - AI teenuse konfiguratsioon
- [Azure OpenAI teenus](https://docs.microsoft.com/azure/cognitive-services/openai/) - AI mudeli juurutamine
- [Application Insights](https://docs.microsoft.com/azure/azure-monitor/app/app-insights-overview) - Jälgimise seadistamine

### Python'i arendus
- [Python'i virtuaalsed keskkonnad](https://docs.python.org/3/tutorial/venv.html) - Keskkonna haldamine
- [AsyncIO dokumentatsioon](https://docs.python.org/3/library/asyncio.html) - Asünkroonse programmeerimise mustrid
- [FastAPI dokumentatsioon](https://fastapi.tiangolo.com/) - Veebiraamistiku mustrid

---

**Järgmine**: Keskkond valmis? Jätkake [Labor 04: Andmebaasi disain ja skeem](../04-Database/README.md)

---

**Lahtiütlus**:  
See dokument on tõlgitud AI tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi püüame tagada täpsust, palume arvestada, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algses keeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitame kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valesti tõlgenduste eest.