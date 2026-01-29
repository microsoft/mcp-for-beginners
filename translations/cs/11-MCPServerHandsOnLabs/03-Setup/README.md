# Nastavení prostředí

## 🎯 Co tento lab pokrývá

Tento praktický lab vás provede nastavením kompletního vývojového prostředí pro vytváření MCP serverů s integrací PostgreSQL. Konfigurujete všechny potřebné nástroje, nasadíte zdroje Azure a ověříte své nastavení před zahájením implementace.

## Přehled

Správné vývojové prostředí je klíčové pro úspěšný vývoj MCP serverů. Tento lab poskytuje podrobné pokyny pro nastavení Dockeru, služeb Azure, vývojových nástrojů a ověření, že vše funguje správně dohromady.

Na konci tohoto labu budete mít plně funkční vývojové prostředí připravené pro vytváření MCP serveru Zava Retail.

## Výukové cíle

Na konci tohoto labu budete schopni:

- **Nainstalovat a nakonfigurovat** všechny potřebné vývojové nástroje
- **Nasadit zdroje Azure** potřebné pro MCP server
- **Nastavit Docker kontejnery** pro PostgreSQL a MCP server
- **Ověřit** nastavení prostředí pomocí testovacích připojení
- **Řešit problémy** s běžnými problémy nastavení a konfigurace
- **Porozumět** vývojovému workflow a struktuře souborů

## 📋 Kontrola předpokladů

Než začnete, ujistěte se, že máte:

### Požadované znalosti
- Základní používání příkazového řádku (Windows Command Prompt/PowerShell)
- Porozumění proměnným prostředí
- Znalost verzovacího systému Git
- Základní koncepty Dockeru (kontejnery, obrazy, svazky)

### Požadavky na systém
- **Operační systém**: Windows 10/11, macOS nebo Linux
- **RAM**: Minimálně 8 GB (doporučeno 16 GB)
- **Úložiště**: Minimálně 10 GB volného místa
- **Síť**: Internetové připojení pro stahování a nasazení Azure

### Požadavky na účet
- **Azure Subscription**: Bezplatná verze je dostačující
- **GitHub Account**: Pro přístup k repozitáři
- **Docker Hub Account**: (Volitelné) Pro publikování vlastních obrazů

## 🛠️ Instalace nástrojů

### 1. Instalace Docker Desktop

Docker poskytuje kontejnerizované prostředí pro naše vývojové nastavení.

#### Instalace na Windows

1. **Stáhněte Docker Desktop**:
   ```cmd
   # Visit https://desktop.docker.com/win/stable/Docker%20Desktop%20Installer.exe
   # Or use Windows Package Manager
   winget install Docker.DockerDesktop
   ```

2. **Nainstalujte a nakonfigurujte**:
   - Spusťte instalátor jako správce
   - Povolte integraci WSL 2, když budete vyzváni
   - Restartujte počítač po dokončení instalace

3. **Ověřte instalaci**:
   ```cmd
   docker --version
   docker-compose --version
   ```

#### Instalace na macOS

1. **Stáhněte a nainstalujte**:
   ```bash
   # Download from https://desktop.docker.com/mac/stable/Docker.dmg
   # Or use Homebrew
   brew install --cask docker
   ```

2. **Spusťte Docker Desktop**:
   - Spusťte Docker Desktop z aplikací
   - Dokončete úvodního průvodce nastavením

3. **Ověřte instalaci**:
   ```bash
   docker --version
   docker-compose --version
   ```

#### Instalace na Linux

1. **Nainstalujte Docker Engine**:
   ```bash
   # Ubuntu/Debian
   curl -fsSL https://get.docker.com -o get-docker.sh
   sudo sh get-docker.sh
   sudo usermod -aG docker $USER
   
   # Log out and back in for group changes to take effect
   ```

2. **Nainstalujte Docker Compose**:
   ```bash
   sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
   sudo chmod +x /usr/local/bin/docker-compose
   ```

### 2. Instalace Azure CLI

Azure CLI umožňuje nasazení a správu zdrojů Azure.

#### Instalace na Windows

```cmd
# Using Windows Package Manager
winget install Microsoft.AzureCLI

# Or download MSI from: https://aka.ms/installazurecliwindows
```

#### Instalace na macOS

```bash
# Using Homebrew
brew install azure-cli

# Or using installer
curl -L https://aka.ms/InstallAzureCli | bash
```

#### Instalace na Linux

```bash
# Ubuntu/Debian
curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash

# RHEL/CentOS
sudo rpm --import https://packages.microsoft.com/keys/microsoft.asc
sudo dnf install azure-cli
```

#### Ověření a autentizace

```bash
# Check installation
az version

# Login to Azure
az login

# Set default subscription (if you have multiple)
az account list --output table
az account set --subscription "Your-Subscription-Name"
```

### 3. Instalace Git

Git je potřebný pro klonování repozitáře a verzování.

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

### 4. Instalace VS Code

Visual Studio Code poskytuje integrované vývojové prostředí s podporou MCP.

#### Instalace

```cmd
# Windows
winget install Microsoft.VisualStudioCode

# macOS
brew install --cask visual-studio-code

# Linux (Ubuntu/Debian)
sudo snap install code --classic
```

#### Požadované rozšíření

Nainstalujte tato rozšíření VS Code:

```bash
# Install via command line
code --install-extension ms-python.python
code --install-extension ms-vscode.vscode-json
code --install-extension ms-azuretools.vscode-docker
code --install-extension ms-vscode.azure-account
```

Nebo nainstalujte přes VS Code:
1. Otevřete VS Code
2. Přejděte na Rozšíření (Ctrl+Shift+X)
3. Nainstalujte:
   - **Python** (Microsoft)
   - **Docker** (Microsoft)
   - **Azure Account** (Microsoft)
   - **JSON** (Microsoft)

### 5. Instalace Pythonu

Python 3.8+ je požadován pro vývoj MCP serveru.

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

#### Ověření instalace

```bash
python --version  # Should show Python 3.11.x
pip --version      # Should show pip version
```

## 🚀 Nastavení projektu

### 1. Klonování repozitáře

```bash
# Clone the main repository
git clone https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail.git

# Navigate to the project directory
cd MCP-Server-and-PostgreSQL-Sample-Retail

# Verify repository structure
ls -la
```

### 2. Vytvoření virtuálního prostředí Pythonu

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

### 3. Instalace Python závislostí

```bash
# Install development dependencies
pip install -r requirements.lock.txt

# Verify key packages
pip list | grep fastmcp
pip list | grep asyncpg
pip list | grep azure
```

## ☁️ Nasazení zdrojů Azure

### 1. Porozumění požadavkům na zdroje

Náš MCP server vyžaduje tyto zdroje Azure:

| **Zdroj** | **Účel** | **Odhadované náklady** |
|-----------|----------|-----------------------|
| **Azure AI Foundry** | Hosting a správa AI modelů | $10-50/měsíc |
| **OpenAI Deployment** | Model textového vkládání (text-embedding-3-small) | $5-20/měsíc |
| **Application Insights** | Monitoring a telemetrie | $5-15/měsíc |
| **Resource Group** | Organizace zdrojů | Zdarma |

### 2. Nasazení zdrojů Azure

#### Možnost A: Automatizované nasazení (doporučeno)

```bash
# Navigate to infrastructure directory
cd infra

# Windows - PowerShell
./deploy.ps1

# macOS/Linux - Bash
./deploy.sh
```

Skript nasazení provede:
1. Vytvoření unikátní skupiny zdrojů
2. Nasazení zdrojů Azure AI Foundry
3. Nasazení modelu text-embedding-3-small
4. Konfiguraci Application Insights
5. Vytvoření servisního principála pro autentizaci
6. Generování souboru `.env` s konfigurací

#### Možnost B: Manuální nasazení

Pokud preferujete manuální kontrolu nebo automatizovaný skript selže:

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

### 3. Ověření nasazení Azure

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

### 4. Konfigurace proměnných prostředí

Po nasazení byste měli mít soubor `.env`. Ověřte, že obsahuje:

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

## 🐳 Nastavení Docker prostředí

### 1. Porozumění Docker kompozici

Naše vývojové prostředí používá Docker Compose:

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

### 2. Spuštění vývojového prostředí

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

### 3. Ověření nastavení databáze

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

### 4. Testování MCP serveru

```bash
# Check MCP server health
curl http://localhost:8000/health

# Test basic MCP endpoint
curl -X POST http://localhost:8000/mcp \
  -H "Content-Type: application/json" \
  -H "x-rls-user-id: 00000000-0000-0000-0000-000000000000" \
  -d '{"method": "tools/list", "params": {}}'
```

## 🔧 Konfigurace VS Code

### 1. Konfigurace integrace MCP

Vytvořte konfiguraci MCP ve VS Code:

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

### 2. Konfigurace Python prostředí

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

### 3. Testování integrace VS Code

1. **Otevřete projekt ve VS Code**:
   ```bash
   code .
   ```

2. **Otevřete AI Chat**:
   - Stiskněte `Ctrl+Shift+P` (Windows/Linux) nebo `Cmd+Shift+P` (macOS)
   - Zadejte "AI Chat" a vyberte "AI Chat: Open Chat"

3. **Testování připojení MCP serveru**:
   - V AI Chat zadejte `#zava` a vyberte jeden z nakonfigurovaných serverů
   - Zeptejte se: "Jaké tabulky jsou dostupné v databázi?"
   - Měli byste obdržet odpověď s výpisem tabulek maloobchodní databáze

## ✅ Ověření prostředí

### 1. Komplexní kontrola systému

Spusťte tento validační skript pro ověření nastavení:

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

### 2. Manuální kontrolní seznam

**✅ Základní nástroje**
- [ ] Nainstalovaná a spuštěná verze Dockeru 20.10+
- [ ] Nainstalovaná a autentizovaná verze Azure CLI 2.40+
- [ ] Nainstalovaný Python 3.8+ s pip
- [ ] Nainstalovaný Git 2.30+
- [ ] VS Code s požadovanými rozšířeními

**✅ Zdroje Azure**
- [ ] Úspěšně vytvořená skupina zdrojů
- [ ] Nasazený projekt AI Foundry
- [ ] Nasazený model text-embedding-3-small
- [ ] Konfigurovaný Application Insights
- [ ] Vytvořený servisní principál s odpovídajícími oprávněními

**✅ Konfigurace prostředí**
- [ ] Vytvořený soubor `.env` se všemi požadovanými proměnnými
- [ ] Funkční Azure přihlašovací údaje (testujte pomocí `az account show`)
- [ ] Běžící a přístupný PostgreSQL kontejner
- [ ] Načtená ukázková data v databázi

**✅ Integrace VS Code**
- [ ] Nakonfigurovaný soubor `.vscode/mcp.json`
- [ ] Nastavený Python interpret na virtuální prostředí
- [ ] MCP servery se zobrazují v AI Chat
- [ ] Možnost provádět testovací dotazy přes AI Chat

## 🛠️ Řešení běžných problémů

### Problémy s Dockerem

**Problém**: Docker kontejnery se nespustí
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

**Problém**: Selhání připojení k PostgreSQL
```bash
# Check container logs
docker-compose logs postgres

# Verify container is healthy
docker-compose ps

# Test direct connection
docker-compose exec postgres psql -U postgres -d zava -c "SELECT 1;"
```

### Problémy s nasazením Azure

**Problém**: Selhání nasazení Azure
```bash
# Check Azure CLI authentication
az account show

# Verify subscription permissions
az role assignment list --assignee $(az account show --query user.name -o tsv)

# Check resource provider registration
az provider register --namespace Microsoft.CognitiveServices
az provider register --namespace Microsoft.Insights
```

**Problém**: Selhání autentizace AI služby
```bash
# Test service principal
az login --service-principal \
  --username $AZURE_CLIENT_ID \
  --password $AZURE_CLIENT_SECRET \
  --tenant $AZURE_TENANT_ID

# Verify AI service deployment
az cognitiveservices account list --query "[].{Name:name,Kind:kind,Location:location}"
```

### Problémy s Python prostředím

**Problém**: Selhání instalace balíčků
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

**Problém**: VS Code nemůže najít Python interpret
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

## 🎯 Klíčové poznatky

Po dokončení tohoto labu byste měli mít:

✅ **Kompletní vývojové prostředí**: Všechny nástroje nainstalované a nakonfigurované  
✅ **Nasazené zdroje Azure**: AI služby a podpůrná infrastruktura  
✅ **Běžící Docker prostředí**: Kontejnery PostgreSQL a MCP serveru  
✅ **Integrace VS Code**: Nakonfigurované a přístupné MCP servery  
✅ **Ověřené nastavení**: Všechny komponenty otestované a funkční dohromady  
✅ **Znalosti řešení problémů**: Běžné problémy a jejich řešení  

## 🚀 Co dál

S připraveným prostředím pokračujte na **[Lab 04: Návrh databáze a schéma](../04-Database/README.md)**, kde:

- Prozkoumáte podrobně schéma maloobchodní databáze
- Porozumíte modelování dat pro více nájemců
- Naučíte se implementaci Row Level Security
- Budete pracovat s ukázkovými maloobchodními daty

## 📚 Další zdroje

### Vývojové nástroje
- [Dokumentace Dockeru](https://docs.docker.com/) - Kompletní reference Dockeru
- [Referenční příručka Azure CLI](https://docs.microsoft.com/cli/azure/) - Příkazy Azure CLI
- [Dokumentace VS Code](https://code.visualstudio.com/docs) - Konfigurace editoru a rozšíření

### Služby Azure
- [Dokumentace Azure AI Foundry](https://docs.microsoft.com/azure/ai-foundry/) - Konfigurace AI služeb
- [Azure OpenAI Service](https://docs.microsoft.com/azure/cognitive-services/openai/) - Nasazení AI modelů
- [Application Insights](https://docs.microsoft.com/azure/azure-monitor/app/app-insights-overview) - Nastavení monitoringu

### Vývoj v Pythonu
- [Virtuální prostředí Pythonu](https://docs.python.org/3/tutorial/venv.html) - Správa prostředí
- [Dokumentace AsyncIO](https://docs.python.org/3/library/asyncio.html) - Asynchronní programovací vzory
- [Dokumentace FastAPI](https://fastapi.tiangolo.com/) - Vzory webového frameworku

---

**Další krok**: Prostředí připraveno? Pokračujte na [Lab 04: Návrh databáze a schéma](../04-Database/README.md)

---

**Prohlášení**:  
Tento dokument byl přeložen pomocí služby AI pro překlad [Co-op Translator](https://github.com/Azure/co-op-translator). I když se snažíme o přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho původním jazyce by měl být považován za autoritativní zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Neodpovídáme za žádná nedorozumění nebo nesprávné interpretace vyplývající z použití tohoto překladu.