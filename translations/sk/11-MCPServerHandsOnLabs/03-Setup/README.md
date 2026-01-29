# Nastavenie prostredia

## 🎯 Čo tento lab pokrýva

Tento praktický lab vás prevedie nastavením kompletného vývojového prostredia na vytváranie MCP serverov s integráciou PostgreSQL. Konfigurujete všetky potrebné nástroje, nasadíte zdroje Azure a overíte svoje nastavenie pred pokračovaním v implementácii.

## Prehľad

Správne vývojové prostredie je kľúčové pre úspešný vývoj MCP serverov. Tento lab poskytuje podrobné pokyny na nastavenie Dockeru, služieb Azure, vývojových nástrojov a overenie, že všetko spolu správne funguje.

Na konci tohto labu budete mať plne funkčné vývojové prostredie pripravené na vytváranie MCP servera Zava Retail.

## Ciele učenia

Na konci tohto labu budete schopní:

- **Nainštalovať a nakonfigurovať** všetky potrebné vývojové nástroje
- **Nasadiť zdroje Azure** potrebné pre MCP server
- **Nastaviť Docker kontajnery** pre PostgreSQL a MCP server
- **Overiť** nastavenie prostredia pomocou testovacích pripojení
- **Riešiť problémy** s bežnými nastaveniami a konfiguráciami
- **Porozumieť** vývojovému workflowu a štruktúre súborov

## 📋 Kontrola predpokladov

Pred začiatkom sa uistite, že máte:

### Požadované znalosti
- Základné používanie príkazového riadku (Windows Command Prompt/PowerShell)
- Porozumenie premenným prostredia
- Znalosť verzionovania pomocou Git
- Základné koncepty Dockeru (kontajnery, obrazy, objemy)

### Požiadavky na systém
- **Operačný systém**: Windows 10/11, macOS alebo Linux
- **RAM**: Minimálne 8GB (odporúča sa 16GB)
- **Úložisko**: Aspoň 10GB voľného miesta
- **Sieť**: Internetové pripojenie na sťahovanie a nasadenie Azure

### Požiadavky na účty
- **Azure Subscription**: Bezplatná úroveň je postačujúca
- **GitHub Account**: Na prístup k repozitáru
- **Docker Hub Account**: (Voliteľné) Na publikovanie vlastných obrazov

## 🛠️ Inštalácia nástrojov

### 1. Inštalácia Docker Desktop

Docker poskytuje kontajnerizované prostredie pre naše vývojové nastavenie.

#### Inštalácia na Windows

1. **Stiahnite Docker Desktop**:
   ```cmd
   # Visit https://desktop.docker.com/win/stable/Docker%20Desktop%20Installer.exe
   # Or use Windows Package Manager
   winget install Docker.DockerDesktop
   ```

2. **Nainštalujte a nakonfigurujte**:
   - Spustite inštalátor ako administrátor
   - Povoliť integráciu WSL 2, keď budete vyzvaní
   - Reštartujte počítač po dokončení inštalácie

3. **Overte inštaláciu**:
   ```cmd
   docker --version
   docker-compose --version
   ```

#### Inštalácia na macOS

1. **Stiahnite a nainštalujte**:
   ```bash
   # Download from https://desktop.docker.com/mac/stable/Docker.dmg
   # Or use Homebrew
   brew install --cask docker
   ```

2. **Spustite Docker Desktop**:
   - Spustite Docker Desktop z aplikácií
   - Dokončite úvodného sprievodcu nastavením

3. **Overte inštaláciu**:
   ```bash
   docker --version
   docker-compose --version
   ```

#### Inštalácia na Linux

1. **Nainštalujte Docker Engine**:
   ```bash
   # Ubuntu/Debian
   curl -fsSL https://get.docker.com -o get-docker.sh
   sudo sh get-docker.sh
   sudo usermod -aG docker $USER
   
   # Log out and back in for group changes to take effect
   ```

2. **Nainštalujte Docker Compose**:
   ```bash
   sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
   sudo chmod +x /usr/local/bin/docker-compose
   ```

### 2. Inštalácia Azure CLI

Azure CLI umožňuje nasadenie a správu zdrojov Azure.

#### Inštalácia na Windows

```cmd
# Using Windows Package Manager
winget install Microsoft.AzureCLI

# Or download MSI from: https://aka.ms/installazurecliwindows
```

#### Inštalácia na macOS

```bash
# Using Homebrew
brew install azure-cli

# Or using installer
curl -L https://aka.ms/InstallAzureCli | bash
```

#### Inštalácia na Linux

```bash
# Ubuntu/Debian
curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash

# RHEL/CentOS
sudo rpm --import https://packages.microsoft.com/keys/microsoft.asc
sudo dnf install azure-cli
```

#### Overenie a autentifikácia

```bash
# Check installation
az version

# Login to Azure
az login

# Set default subscription (if you have multiple)
az account list --output table
az account set --subscription "Your-Subscription-Name"
```

### 3. Inštalácia Git

Git je potrebný na klonovanie repozitára a verzionovanie.

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

### 4. Inštalácia VS Code

Visual Studio Code poskytuje integrované vývojové prostredie s podporou MCP.

#### Inštalácia

```cmd
# Windows
winget install Microsoft.VisualStudioCode

# macOS
brew install --cask visual-studio-code

# Linux (Ubuntu/Debian)
sudo snap install code --classic
```

#### Požadované rozšírenia

Nainštalujte tieto rozšírenia VS Code:

```bash
# Install via command line
code --install-extension ms-python.python
code --install-extension ms-vscode.vscode-json
code --install-extension ms-azuretools.vscode-docker
code --install-extension ms-vscode.azure-account
```

Alebo ich nainštalujte cez VS Code:
1. Otvorte VS Code
2. Prejdite na Rozšírenia (Ctrl+Shift+X)
3. Nainštalujte:
   - **Python** (Microsoft)
   - **Docker** (Microsoft)
   - **Azure Account** (Microsoft)
   - **JSON** (Microsoft)

### 5. Inštalácia Pythonu

Python 3.8+ je potrebný na vývoj MCP servera.

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

#### Overenie inštalácie

```bash
python --version  # Should show Python 3.11.x
pip --version      # Should show pip version
```

## 🚀 Nastavenie projektu

### 1. Klonovanie repozitára

```bash
# Clone the main repository
git clone https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail.git

# Navigate to the project directory
cd MCP-Server-and-PostgreSQL-Sample-Retail

# Verify repository structure
ls -la
```

### 2. Vytvorenie virtuálneho prostredia Python

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

### 3. Inštalácia Python závislostí

```bash
# Install development dependencies
pip install -r requirements.lock.txt

# Verify key packages
pip list | grep fastmcp
pip list | grep asyncpg
pip list | grep azure
```

## ☁️ Nasadenie zdrojov Azure

### 1. Porozumenie požiadavkám na zdroje

Náš MCP server vyžaduje tieto zdroje Azure:

| **Zdroj** | **Účel** | **Odhadované náklady** |
|-----------|----------|-----------------------|
| **Azure AI Foundry** | Hosting a správa AI modelov | $10-50/mesiac |
| **OpenAI Deployment** | Model na textové vkladanie (text-embedding-3-small) | $5-20/mesiac |
| **Application Insights** | Monitorovanie a telemetria | $5-15/mesiac |
| **Resource Group** | Organizácia zdrojov | Zadarmo |

### 2. Nasadenie zdrojov Azure

#### Možnosť A: Automatizované nasadenie (Odporúčané)

```bash
# Navigate to infrastructure directory
cd infra

# Windows - PowerShell
./deploy.ps1

# macOS/Linux - Bash
./deploy.sh
```

Skript nasadenia vykoná:
1. Vytvorenie unikátnej skupiny zdrojov
2. Nasadenie zdrojov Azure AI Foundry
3. Nasadenie modelu text-embedding-3-small
4. Konfiguráciu Application Insights
5. Vytvorenie servisného princípu na autentifikáciu
6. Generovanie súboru `.env` s konfiguráciou

#### Možnosť B: Manuálne nasadenie

Ak preferujete manuálnu kontrolu alebo automatizovaný skript zlyhá:

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

### 3. Overenie nasadenia Azure

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

### 4. Konfigurácia premenných prostredia

Po nasadení by ste mali mať súbor `.env`. Overte, že obsahuje:

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

## 🐳 Nastavenie Docker prostredia

### 1. Porozumenie Docker kompozícii

Naše vývojové prostredie používa Docker Compose:

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

### 2. Spustenie vývojového prostredia

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

### 3. Overenie nastavenia databázy

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

### 4. Testovanie MCP servera

```bash
# Check MCP server health
curl http://localhost:8000/health

# Test basic MCP endpoint
curl -X POST http://localhost:8000/mcp \
  -H "Content-Type: application/json" \
  -H "x-rls-user-id: 00000000-0000-0000-0000-000000000000" \
  -d '{"method": "tools/list", "params": {}}'
```

## 🔧 Konfigurácia VS Code

### 1. Konfigurácia MCP integrácie

Vytvorte konfiguráciu MCP vo VS Code:

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

### 2. Konfigurácia Python prostredia

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

### 3. Testovanie integrácie VS Code

1. **Otvorte projekt vo VS Code**:
   ```bash
   code .
   ```

2. **Otvorte AI Chat**:
   - Stlačte `Ctrl+Shift+P` (Windows/Linux) alebo `Cmd+Shift+P` (macOS)
   - Napíšte "AI Chat" a vyberte "AI Chat: Open Chat"

3. **Testovanie pripojenia MCP servera**:
   - V AI Chat napíšte `#zava` a vyberte jeden z nakonfigurovaných serverov
   - Spýtajte sa: "Aké tabuľky sú dostupné v databáze?"
   - Mali by ste dostať odpoveď s výpisom tabuliek maloobchodnej databázy

## ✅ Overenie prostredia

### 1. Komplexná kontrola systému

Spustite tento validačný skript na overenie vášho nastavenia:

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

### 2. Manuálny kontrolný zoznam

**✅ Základné nástroje**
- [ ] Docker verzia 20.10+ nainštalovaný a spustený
- [ ] Azure CLI 2.40+ nainštalovaný a autentifikovaný
- [ ] Python 3.8+ s pip nainštalovaný
- [ ] Git 2.30+ nainštalovaný
- [ ] VS Code s požadovanými rozšíreniami

**✅ Zdroje Azure**
- [ ] Skupina zdrojov úspešne vytvorená
- [ ] Projekt AI Foundry nasadený
- [ ] Model text-embedding-3-small nasadený
- [ ] Application Insights nakonfigurovaný
- [ ] Servisný princíp vytvorený s potrebnými oprávneniami

**✅ Konfigurácia prostredia**
- [ ] Súbor `.env` vytvorený so všetkými potrebnými premennými
- [ ] Azure poverenia funkčné (testujte pomocou `az account show`)
- [ ] PostgreSQL kontajner spustený a prístupný
- [ ] Vzorkové dáta načítané do databázy

**✅ Integrácia VS Code**
- [ ] `.vscode/mcp.json` nakonfigurovaný
- [ ] Python interpreter nastavený na virtuálne prostredie
- [ ] MCP servery sa zobrazujú v AI Chat
- [ ] Možnosť vykonávať testovacie dotazy cez AI Chat

## 🛠️ Riešenie bežných problémov

### Problémy s Dockerom

**Problém**: Docker kontajnery sa nespustia
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

**Problém**: Pripojenie k PostgreSQL zlyhá
```bash
# Check container logs
docker-compose logs postgres

# Verify container is healthy
docker-compose ps

# Test direct connection
docker-compose exec postgres psql -U postgres -d zava -c "SELECT 1;"
```

### Problémy s nasadením Azure

**Problém**: Nasadenie Azure zlyhá
```bash
# Check Azure CLI authentication
az account show

# Verify subscription permissions
az role assignment list --assignee $(az account show --query user.name -o tsv)

# Check resource provider registration
az provider register --namespace Microsoft.CognitiveServices
az provider register --namespace Microsoft.Insights
```

**Problém**: Autentifikácia AI služby zlyhá
```bash
# Test service principal
az login --service-principal \
  --username $AZURE_CLIENT_ID \
  --password $AZURE_CLIENT_SECRET \
  --tenant $AZURE_TENANT_ID

# Verify AI service deployment
az cognitiveservices account list --query "[].{Name:name,Kind:kind,Location:location}"
```

### Problémy s Python prostredím

**Problém**: Inštalácia balíkov zlyhá
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

**Problém**: VS Code nemôže nájsť Python interpreter
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

## 🎯 Hlavné poznatky

Po dokončení tohto labu by ste mali mať:

✅ **Kompletné vývojové prostredie**: Všetky nástroje nainštalované a nakonfigurované  
✅ **Nasadené zdroje Azure**: AI služby a podporná infraštruktúra  
✅ **Spustené Docker prostredie**: Kontajnery PostgreSQL a MCP servera  
✅ **Integrácia VS Code**: MCP servery nakonfigurované a prístupné  
✅ **Overené nastavenie**: Všetky komponenty otestované a funkčné spolu  
✅ **Znalosti o riešení problémov**: Bežné problémy a ich riešenia  

## 🚀 Čo ďalej

S pripraveným prostredím pokračujte na **[Lab 04: Návrh databázy a schéma](../04-Database/README.md)**, kde:

- Preskúmate podrobne schému maloobchodnej databázy
- Porozumiete modelovaniu dát pre viacerých nájomcov
- Naučíte sa implementáciu bezpečnosti na úrovni riadkov
- Pracujete so vzorkovými maloobchodnými dátami

## 📚 Dodatočné zdroje

### Vývojové nástroje
- [Docker Dokumentácia](https://docs.docker.com/) - Kompletný referenčný materiál Dockeru
- [Azure CLI Referencia](https://docs.microsoft.com/cli/azure/) - Príkazy Azure CLI
- [VS Code Dokumentácia](https://code.visualstudio.com/docs) - Konfigurácia editora a rozšírenia

### Služby Azure
- [Azure AI Foundry Dokumentácia](https://docs.microsoft.com/azure/ai-foundry/) - Konfigurácia AI služieb
- [Azure OpenAI Service](https://docs.microsoft.com/azure/cognitive-services/openai/) - Nasadenie AI modelov
- [Application Insights](https://docs.microsoft.com/azure/azure-monitor/app/app-insights-overview) - Nastavenie monitorovania

### Vývoj v Pythone
- [Virtuálne prostredia Python](https://docs.python.org/3/tutorial/venv.html) - Správa prostredí
- [AsyncIO Dokumentácia](https://docs.python.org/3/library/asyncio.html) - Vzory asynchrónneho programovania
- [FastAPI Dokumentácia](https://fastapi.tiangolo.com/) - Vzory webového frameworku

---

**Ďalej**: Prostredie pripravené? Pokračujte na [Lab 04: Návrh databázy a schéma](../04-Database/README.md)

---

**Upozornenie**:  
Tento dokument bol preložený pomocou služby AI prekladu [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, upozorňujeme, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho rodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nenesieme zodpovednosť za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.