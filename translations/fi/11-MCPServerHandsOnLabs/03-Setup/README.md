# Ympäristön Määrittäminen

## 🎯 Mitä Tämä Labra Sisältää

Tämä käytännön labra opastaa sinut täydellisen kehitysympäristön luomisessa MCP-palvelimien rakentamiseen PostgreSQL-integraatiolla. Konfiguroit kaikki tarvittavat työkalut, otat Azure-resurssit käyttöön ja varmistat ympäristön toimivuuden ennen toteutuksen aloittamista.

## Yleiskatsaus

Oikein määritetty kehitysympäristö on ratkaisevan tärkeä MCP-palvelimen kehityksen onnistumiselle. Tämä labra tarjoaa vaiheittaiset ohjeet Dockerin, Azure-palveluiden ja kehitystyökalujen asentamiseen sekä varmistaa, että kaikki toimii yhdessä oikein.

Labran lopussa sinulla on täysin toimiva kehitysympäristö Zava Retail MCP -palvelimen rakentamiseen.

## Oppimistavoitteet

Labran lopussa osaat:

- **Asentaa ja konfiguroida** kaikki tarvittavat kehitystyökalut
- **Ottaa käyttöön Azure-resurssit**, joita MCP-palvelin tarvitsee
- **Määrittää Docker-kontit** PostgreSQL:lle ja MCP-palvelimelle
- **Varmistaa** ympäristön toimivuuden testiyhteyksillä
- **Ratkaista** yleisiä asennusongelmia ja konfigurointivirheitä
- **Ymmärtää** kehitystyönkulun ja tiedostorakenteen

## 📋 Esitietojen Tarkistus

Ennen aloittamista varmista, että sinulla on:

### Tarvittavat Tiedot
- Perustaidot komentorivin käytössä (Windows Command Prompt/PowerShell)
- Ympäristömuuttujien ymmärtäminen
- Git-versionhallinnan perusteet
- Dockerin peruskäsitteet (kontit, kuvat, volyymit)

### Järjestelmävaatimukset
- **Käyttöjärjestelmä**: Windows 10/11, macOS tai Linux
- **RAM**: Vähintään 8GB (suositus 16GB)
- **Tallennustila**: Vähintään 10GB vapaata tilaa
- **Verkko**: Internet-yhteys latauksia ja Azure-käyttöönottoa varten

### Tilivaatimukset
- **Azure-tilaus**: Ilmainen taso riittää
- **GitHub-tili**: Pääsyä varten repositorioon
- **Docker Hub -tili**: (Valinnainen) Mukautettujen kuvien julkaisuun

## 🛠️ Työkalujen Asennus

### 1. Asenna Docker Desktop

Docker tarjoaa konttipohjaisen ympäristön kehitystyöhön.

#### Windows Asennus

1. **Lataa Docker Desktop**:
   ```cmd
   # Visit https://desktop.docker.com/win/stable/Docker%20Desktop%20Installer.exe
   # Or use Windows Package Manager
   winget install Docker.DockerDesktop
   ```

2. **Asenna ja Konfiguroi**:
   - Suorita asennusohjelma järjestelmänvalvojana
   - Ota WSL 2 -integraatio käyttöön, kun sitä pyydetään
   - Käynnistä tietokone uudelleen asennuksen jälkeen

3. **Varmista Asennus**:
   ```cmd
   docker --version
   docker-compose --version
   ```

#### macOS Asennus

1. **Lataa ja Asenna**:
   ```bash
   # Download from https://desktop.docker.com/mac/stable/Docker.dmg
   # Or use Homebrew
   brew install --cask docker
   ```

2. **Käynnistä Docker Desktop**:
   - Avaa Docker Desktop Sovellukset-kansiosta
   - Suorita alkuasennuksen ohjattu toiminto

3. **Varmista Asennus**:
   ```bash
   docker --version
   docker-compose --version
   ```

#### Linux Asennus

1. **Asenna Docker Engine**:
   ```bash
   # Ubuntu/Debian
   curl -fsSL https://get.docker.com -o get-docker.sh
   sudo sh get-docker.sh
   sudo usermod -aG docker $USER
   
   # Log out and back in for group changes to take effect
   ```

2. **Asenna Docker Compose**:
   ```bash
   sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
   sudo chmod +x /usr/local/bin/docker-compose
   ```

### 2. Asenna Azure CLI

Azure CLI mahdollistaa Azure-resurssien käyttöönoton ja hallinnan.

#### Windows Asennus

```cmd
# Using Windows Package Manager
winget install Microsoft.AzureCLI

# Or download MSI from: https://aka.ms/installazurecliwindows
```

#### macOS Asennus

```bash
# Using Homebrew
brew install azure-cli

# Or using installer
curl -L https://aka.ms/InstallAzureCli | bash
```

#### Linux Asennus

```bash
# Ubuntu/Debian
curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash

# RHEL/CentOS
sudo rpm --import https://packages.microsoft.com/keys/microsoft.asc
sudo dnf install azure-cli
```

#### Varmista ja Kirjaudu Sisään

```bash
# Check installation
az version

# Login to Azure
az login

# Set default subscription (if you have multiple)
az account list --output table
az account set --subscription "Your-Subscription-Name"
```

### 3. Asenna Git

Git tarvitaan repositorion kloonaamiseen ja versionhallintaan.

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

### 4. Asenna VS Code

Visual Studio Code tarjoaa integroidun kehitysympäristön MCP-tukeen.

#### Asennus

```cmd
# Windows
winget install Microsoft.VisualStudioCode

# macOS
brew install --cask visual-studio-code

# Linux (Ubuntu/Debian)
sudo snap install code --classic
```

#### Tarvittavat Laajennukset

Asenna nämä VS Code -laajennukset:

```bash
# Install via command line
code --install-extension ms-python.python
code --install-extension ms-vscode.vscode-json
code --install-extension ms-azuretools.vscode-docker
code --install-extension ms-vscode.azure-account
```

Tai asenna VS Code -editorin kautta:
1. Avaa VS Code
2. Siirry Laajennuksiin (Ctrl+Shift+X)
3. Asenna:
   - **Python** (Microsoft)
   - **Docker** (Microsoft)
   - **Azure Account** (Microsoft)
   - **JSON** (Microsoft)

### 5. Asenna Python

Python 3.8+ vaaditaan MCP-palvelimen kehitykseen.

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

#### Varmista Asennus

```bash
python --version  # Should show Python 3.11.x
pip --version      # Should show pip version
```

## 🚀 Projektin Määrittäminen

### 1. Kloonaa Repositorio

```bash
# Clone the main repository
git clone https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail.git

# Navigate to the project directory
cd MCP-Server-and-PostgreSQL-Sample-Retail

# Verify repository structure
ls -la
```

### 2. Luo Python Virtuaaliympäristö

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

### 3. Asenna Python Riippuvuudet

```bash
# Install development dependencies
pip install -r requirements.lock.txt

# Verify key packages
pip list | grep fastmcp
pip list | grep asyncpg
pip list | grep azure
```

## ☁️ Azure-resurssien Käyttöönotto

### 1. Resurssivaatimusten Ymmärtäminen

MCP-palvelin tarvitsee seuraavat Azure-resurssit:

| **Resurssi** | **Tarkoitus** | **Arvioitu Kustannus** |
|--------------|-------------|-------------------|
| **Azure AI Foundry** | AI-mallien isännöinti ja hallinta | $10-50/kuukausi |
| **OpenAI Deployment** | Tekstien upotusmalli (text-embedding-3-small) | $5-20/kuukausi |
| **Application Insights** | Seuranta ja telemetria | $5-15/kuukausi |
| **Resource Group** | Resurssien organisointi | Ilmainen |

### 2. Ota Azure-resurssit Käyttöön

#### Vaihtoehto A: Automaattinen Käyttöönotto (Suositeltu)

```bash
# Navigate to infrastructure directory
cd infra

# Windows - PowerShell
./deploy.ps1

# macOS/Linux - Bash
./deploy.sh
```

Käyttöönotto-skripti:
1. Luo ainutlaatuinen resurssiryhmä
2. Ottaa käyttöön Azure AI Foundry -resurssit
3. Ottaa käyttöön text-embedding-3-small -mallin
4. Konfiguroi Application Insights
5. Luo palveluperiaate autentikointia varten
6. Generoi `.env`-tiedosto konfiguraatiolla

#### Vaihtoehto B: Manuaalinen Käyttöönotto

Jos haluat manuaalista hallintaa tai automaattinen skripti epäonnistuu:

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

### 3. Varmista Azure Käyttöönotto

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

### 4. Konfiguroi Ympäristömuuttujat

Käyttöönoton jälkeen sinulla pitäisi olla `.env`-tiedosto. Varmista, että se sisältää:

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

## 🐳 Docker-ympäristön Määrittäminen

### 1. Ymmärrä Docker Compose

Kehitysympäristömme käyttää Docker Composea:

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

### 2. Käynnistä Kehitysympäristö

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

### 3. Varmista Tietokannan Määrittäminen

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

### 4. Testaa MCP-palvelin

```bash
# Check MCP server health
curl http://localhost:8000/health

# Test basic MCP endpoint
curl -X POST http://localhost:8000/mcp \
  -H "Content-Type: application/json" \
  -H "x-rls-user-id: 00000000-0000-0000-0000-000000000000" \
  -d '{"method": "tools/list", "params": {}}'
```

## 🔧 VS Code Konfigurointi

### 1. Konfiguroi MCP-integraatio

Luo VS Code MCP-konfiguraatio:

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

### 2. Konfiguroi Python-ympäristö

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

### 3. Testaa VS Code -integraatio

1. **Avaa projekti VS Code:ssa**:
   ```bash
   code .
   ```

2. **Avaa AI Chat**:
   - Paina `Ctrl+Shift+P` (Windows/Linux) tai `Cmd+Shift+P` (macOS)
   - Kirjoita "AI Chat" ja valitse "AI Chat: Open Chat"

3. **Testaa MCP-palvelinyhteys**:
   - AI Chatissa kirjoita `#zava` ja valitse yksi konfiguroiduista palvelimista
   - Kysy: "Mitkä taulut ovat saatavilla tietokannassa?"
   - Sinun pitäisi saada vastaus, joka listaa vähittäiskaupan tietokantataulut

## ✅ Ympäristön Validointi

### 1. Kattava Järjestelmän Tarkistus

Suorita tämä validointiskripti varmistaaksesi ympäristön:

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

### 2. Manuaalinen Validointilista

**✅ Perustyökalut**
- [ ] Docker versio 20.10+ asennettu ja käynnissä
- [ ] Azure CLI 2.40+ asennettu ja autentikoitu
- [ ] Python 3.8+ pipin kanssa asennettu
- [ ] Git 2.30+ asennettu
- [ ] VS Code tarvittavilla laajennuksilla

**✅ Azure-resurssit**
- [ ] Resurssiryhmä luotu onnistuneesti
- [ ] AI Foundry -projekti otettu käyttöön
- [ ] OpenAI text-embedding-3-small -malli otettu käyttöön
- [ ] Application Insights konfiguroitu
- [ ] Palveluperiaate luotu oikeilla käyttöoikeuksilla

**✅ Ympäristön Konfigurointi**
- [ ] `.env`-tiedosto luotu kaikilla tarvittavilla muuttujilla
- [ ] Azure-tunnukset toimivat (testaa `az account show`)
- [ ] PostgreSQL-kontti käynnissä ja saavutettavissa
- [ ] Esimerkkidata ladattu tietokantaan

**✅ VS Code -integraatio**
- [ ] `.vscode/mcp.json` konfiguroitu
- [ ] Python-tulkki asetettu virtuaaliympäristöön
- [ ] MCP-palvelimet näkyvät AI Chatissa
- [ ] Testikyselyt voidaan suorittaa AI Chatissa

## 🛠️ Yleisten Ongelmien Ratkaisu

### Docker-ongelmat

**Ongelma**: Docker-kontit eivät käynnisty
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

**Ongelma**: PostgreSQL-yhteys epäonnistuu
```bash
# Check container logs
docker-compose logs postgres

# Verify container is healthy
docker-compose ps

# Test direct connection
docker-compose exec postgres psql -U postgres -d zava -c "SELECT 1;"
```

### Azure Käyttöönotto-ongelmat

**Ongelma**: Azure-käyttöönotto epäonnistuu
```bash
# Check Azure CLI authentication
az account show

# Verify subscription permissions
az role assignment list --assignee $(az account show --query user.name -o tsv)

# Check resource provider registration
az provider register --namespace Microsoft.CognitiveServices
az provider register --namespace Microsoft.Insights
```

**Ongelma**: AI-palvelun autentikointi epäonnistuu
```bash
# Test service principal
az login --service-principal \
  --username $AZURE_CLIENT_ID \
  --password $AZURE_CLIENT_SECRET \
  --tenant $AZURE_TENANT_ID

# Verify AI service deployment
az cognitiveservices account list --query "[].{Name:name,Kind:kind,Location:location}"
```

### Python-ympäristöongelmat

**Ongelma**: Pakettien asennus epäonnistuu
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

**Ongelma**: VS Code ei löydä Python-tulkkia
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

## 🎯 Keskeiset Opit

Labran suorittamisen jälkeen sinulla pitäisi olla:

✅ **Täydellinen Kehitysympäristö**: Kaikki työkalut asennettu ja konfiguroitu  
✅ **Azure-resurssit Käytössä**: AI-palvelut ja tukirakenteet  
✅ **Docker-ympäristö Käynnissä**: PostgreSQL- ja MCP-palvelinkontit  
✅ **VS Code -integraatio**: MCP-palvelimet konfiguroitu ja saavutettavissa  
✅ **Validointi Suoritettu**: Kaikki komponentit testattu ja toimivat yhdessä  
✅ **Ongelmanratkaisutaidot**: Yleisimmät ongelmat ja ratkaisut  

## 🚀 Mitä Seuraavaksi

Kun ympäristösi on valmis, jatka **[Labra 04: Tietokannan Suunnittelu ja Skeema](../04-Database/README.md)**:

- Tutustu vähittäiskaupan tietokantaskeemaan yksityiskohtaisesti
- Ymmärrä monivuokraajamallin tietomallinnus
- Opi rivitason turvallisuuden toteutuksesta
- Työskentele esimerkkivähittäiskauppadatan kanssa

## 📚 Lisäresurssit

### Kehitystyökalut
- [Docker Dokumentaatio](https://docs.docker.com/) - Dockerin kattava viite
- [Azure CLI Viite](https://docs.microsoft.com/cli/azure/) - Azure CLI -komennot
- [VS Code Dokumentaatio](https://code.visualstudio.com/docs) - Editorin konfigurointi ja laajennukset

### Azure-palvelut
- [Azure AI Foundry Dokumentaatio](https://docs.microsoft.com/azure/ai-foundry/) - AI-palvelun konfigurointi
- [Azure OpenAI Service](https://docs.microsoft.com/azure/cognitive-services/openai/) - AI-mallin käyttöönotto
- [Application Insights](https://docs.microsoft.com/azure/azure-monitor/app/app-insights-overview) - Seurannan määrittäminen

### Python-kehitys
- [Python Virtuaaliympäristöt](https://docs.python.org/3/tutorial/venv.html) - Ympäristön hallinta
- [AsyncIO Dokumentaatio](https://docs.python.org/3/library/asyncio.html) - Asynkronisen ohjelmoinnin mallit
- [FastAPI Dokumentaatio](https://fastapi.tiangolo.com/) - Web-kehysmallit

---

**Seuraavaksi**: Ympäristö valmis? Jatka [Labra 04: Tietokannan Suunnittelu ja Skeema](../04-Database/README.md)

---

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäisellä kielellä tulisi pitää ensisijaisena lähteenä. Kriittisen tiedon osalta suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa väärinkäsityksistä tai virhetulkinnoista, jotka johtuvat tämän käännöksen käytöstä.