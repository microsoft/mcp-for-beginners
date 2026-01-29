# Nastavitev okolja

## 🎯 Kaj pokriva ta laboratorij

Ta praktični laboratorij vas vodi skozi nastavitev celotnega razvojnega okolja za gradnjo MCP strežnikov z integracijo PostgreSQL. Konfigurirali boste vsa potrebna orodja, uvedli Azure vire in preverili svojo nastavitev, preden nadaljujete z implementacijo.

## Pregled

Ustrezno razvojno okolje je ključno za uspešen razvoj MCP strežnikov. Ta laboratorij ponuja korak za korakom navodila za nastavitev Dockerja, Azure storitev, razvojnih orodij in preverjanje, da vse deluje pravilno skupaj.

Na koncu tega laboratorija boste imeli popolnoma funkcionalno razvojno okolje, pripravljeno za gradnjo MCP strežnika Zava Retail.

## Cilji učenja

Na koncu tega laboratorija boste lahko:

- **Namestili in konfigurirali** vsa potrebna razvojna orodja
- **Uvedli Azure vire**, potrebne za MCP strežnik
- **Nastavili Docker kontejnerje** za PostgreSQL in MCP strežnik
- **Preverili** nastavitev okolja s testnimi povezavami
- **Odpravili težave** z običajnimi težavami pri nastavitvi in konfiguraciji
- **Razumeli** razvojni potek dela in strukturo datotek

## 📋 Preverjanje predpogojev

Pred začetkom se prepričajte, da imate:

### Zahtevano znanje
- Osnovna uporaba ukazne vrstice (Windows Command Prompt/PowerShell)
- Razumevanje okoljskih spremenljivk
- Poznavanje Git različice nadzora
- Osnovni koncepti Dockerja (kontejnerji, slike, volumni)

### Sistemské zahteve
- **Operacijski sistem**: Windows 10/11, macOS ali Linux
- **RAM**: Najmanj 8 GB (priporočeno 16 GB)
- **Shramba**: Vsaj 10 GB prostega prostora
- **Omrežje**: Internetna povezava za prenose in uvedbo Azure

### Zahteve za račun
- **Azure naročnina**: Brezplačna različica je dovolj
- **GitHub račun**: Za dostop do repozitorija
- **Docker Hub račun**: (Neobvezno) Za objavo prilagojenih slik

## 🛠️ Namestitev orodij

### 1. Namestitev Docker Desktop

Docker zagotavlja okolje s kontejnerji za našo razvojno nastavitev.

#### Namestitev na Windows

1. **Prenesite Docker Desktop**:
   ```cmd
   # Visit https://desktop.docker.com/win/stable/Docker%20Desktop%20Installer.exe
   # Or use Windows Package Manager
   winget install Docker.DockerDesktop
   ```

2. **Namestite in konfigurirajte**:
   - Zaženite namestitveni program kot skrbnik
   - Omogočite integracijo WSL 2, ko vas pozove
   - Po končani namestitvi znova zaženite računalnik

3. **Preverite namestitev**:
   ```cmd
   docker --version
   docker-compose --version
   ```

#### Namestitev na macOS

1. **Prenesite in namestite**:
   ```bash
   # Download from https://desktop.docker.com/mac/stable/Docker.dmg
   # Or use Homebrew
   brew install --cask docker
   ```

2. **Zaženite Docker Desktop**:
   - Zaženite Docker Desktop iz aplikacij
   - Dokončajte začetni čarovnik za nastavitev

3. **Preverite namestitev**:
   ```bash
   docker --version
   docker-compose --version
   ```

#### Namestitev na Linux

1. **Namestite Docker Engine**:
   ```bash
   # Ubuntu/Debian
   curl -fsSL https://get.docker.com -o get-docker.sh
   sudo sh get-docker.sh
   sudo usermod -aG docker $USER
   
   # Log out and back in for group changes to take effect
   ```

2. **Namestite Docker Compose**:
   ```bash
   sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
   sudo chmod +x /usr/local/bin/docker-compose
   ```

### 2. Namestitev Azure CLI

Azure CLI omogoča uvedbo in upravljanje Azure virov.

#### Namestitev na Windows

```cmd
# Using Windows Package Manager
winget install Microsoft.AzureCLI

# Or download MSI from: https://aka.ms/installazurecliwindows
```

#### Namestitev na macOS

```bash
# Using Homebrew
brew install azure-cli

# Or using installer
curl -L https://aka.ms/InstallAzureCli | bash
```

#### Namestitev na Linux

```bash
# Ubuntu/Debian
curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash

# RHEL/CentOS
sudo rpm --import https://packages.microsoft.com/keys/microsoft.asc
sudo dnf install azure-cli
```

#### Preverjanje in avtentikacija

```bash
# Check installation
az version

# Login to Azure
az login

# Set default subscription (if you have multiple)
az account list --output table
az account set --subscription "Your-Subscription-Name"
```

### 3. Namestitev Git

Git je potreben za kloniranje repozitorija in različico nadzora.

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

### 4. Namestitev VS Code

Visual Studio Code zagotavlja integrirano razvojno okolje z podporo za MCP.

#### Namestitev

```cmd
# Windows
winget install Microsoft.VisualStudioCode

# macOS
brew install --cask visual-studio-code

# Linux (Ubuntu/Debian)
sudo snap install code --classic
```

#### Zahtevane razširitve

Namestite te razširitve za VS Code:

```bash
# Install via command line
code --install-extension ms-python.python
code --install-extension ms-vscode.vscode-json
code --install-extension ms-azuretools.vscode-docker
code --install-extension ms-vscode.azure-account
```

Ali pa jih namestite prek VS Code:
1. Odprite VS Code
2. Pojdite na razširitve (Ctrl+Shift+X)
3. Namestite:
   - **Python** (Microsoft)
   - **Docker** (Microsoft)
   - **Azure Account** (Microsoft)
   - **JSON** (Microsoft)

### 5. Namestitev Python

Python 3.8+ je potreben za razvoj MCP strežnika.

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

#### Preverjanje namestitve

```bash
python --version  # Should show Python 3.11.x
pip --version      # Should show pip version
```

## 🚀 Nastavitev projekta

### 1. Kloniranje repozitorija

```bash
# Clone the main repository
git clone https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail.git

# Navigate to the project directory
cd MCP-Server-and-PostgreSQL-Sample-Retail

# Verify repository structure
ls -la
```

### 2. Ustvarjanje virtualnega okolja Python

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

### 3. Namestitev Python odvisnosti

```bash
# Install development dependencies
pip install -r requirements.lock.txt

# Verify key packages
pip list | grep fastmcp
pip list | grep asyncpg
pip list | grep azure
```

## ☁️ Uvedba Azure virov

### 1. Razumevanje zahtev za vire

Naš MCP strežnik potrebuje te Azure vire:

| **Vir** | **Namen** | **Ocenjeni strošek** |
|---------|-----------|-----------------------|
| **Azure AI Foundry** | Gostovanje in upravljanje AI modelov | $10-50/mesec |
| **OpenAI uvedba** | Model za vdelavo besedila (text-embedding-3-small) | $5-20/mesec |
| **Application Insights** | Spremljanje in telemetrija | $5-15/mesec |
| **Resource Group** | Organizacija virov | Brezplačno |

### 2. Uvedba Azure virov

#### Možnost A: Samodejna uvedba (priporočeno)

```bash
# Navigate to infrastructure directory
cd infra

# Windows - PowerShell
./deploy.ps1

# macOS/Linux - Bash
./deploy.sh
```

Skript za uvedbo bo:
1. Ustvaril edinstveno skupino virov
2. Uvedel vire Azure AI Foundry
3. Uvedel model text-embedding-3-small
4. Konfiguriral Application Insights
5. Ustvaril storitveni račun za avtentikacijo
6. Ustvaril `.env` datoteko s konfiguracijo

#### Možnost B: Ročna uvedba

Če imate raje ročni nadzor ali če samodejni skript ne uspe:

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

### 3. Preverjanje uvedbe Azure

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

### 4. Konfiguracija okoljskih spremenljivk

Po uvedbi bi morali imeti `.env` datoteko. Preverite, da vsebuje:

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

## 🐳 Nastavitev Docker okolja

### 1. Razumevanje Docker sestave

Naše razvojno okolje uporablja Docker Compose:

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

### 2. Zagon razvojnega okolja

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

### 3. Preverjanje nastavitve baze podatkov

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

### 4. Testiranje MCP strežnika

```bash
# Check MCP server health
curl http://localhost:8000/health

# Test basic MCP endpoint
curl -X POST http://localhost:8000/mcp \
  -H "Content-Type: application/json" \
  -H "x-rls-user-id: 00000000-0000-0000-0000-000000000000" \
  -d '{"method": "tools/list", "params": {}}'
```

## 🔧 Konfiguracija VS Code

### 1. Konfiguracija MCP integracije

Ustvarite konfiguracijo MCP za VS Code:

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

### 2. Konfiguracija Python okolja

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

### 3. Testiranje integracije VS Code

1. **Odprite projekt v VS Code**:
   ```bash
   code .
   ```

2. **Odprite AI Chat**:
   - Pritisnite `Ctrl+Shift+P` (Windows/Linux) ali `Cmd+Shift+P` (macOS)
   - Vnesite "AI Chat" in izberite "AI Chat: Open Chat"

3. **Testiranje povezave MCP strežnika**:
   - V AI Chat vnesite `#zava` in izberite enega od konfiguriranih strežnikov
   - Vprašajte: "Katere tabele so na voljo v bazi podatkov?"
   - Prejeli bi morali odgovor s seznamom tabel v maloprodajni bazi podatkov

## ✅ Preverjanje okolja

### 1. Celovit sistemski pregled

Zaženite ta skript za preverjanje vaše nastavitve:

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

### 2. Ročni kontrolni seznam za preverjanje

**✅ Osnovna orodja**
- [ ] Nameščen in delujoč Docker različice 20.10+
- [ ] Nameščen in avtenticiran Azure CLI 2.40+
- [ ] Nameščen Python 3.8+ s pip
- [ ] Nameščen Git 2.30+
- [ ] Nameščen VS Code z zahtevanimi razširitvami

**✅ Azure viri**
- [ ] Skupina virov uspešno ustvarjena
- [ ] Projekt AI Foundry uveden
- [ ] Model OpenAI text-embedding-3-small uveden
- [ ] Application Insights konfiguriran
- [ ] Storitveni račun ustvarjen z ustreznimi dovoljenji

**✅ Konfiguracija okolja**
- [ ] Ustvarjena `.env` datoteka z vsemi zahtevanimi spremenljivkami
- [ ] Delujoči Azure poverilnici (testirajte z `az account show`)
- [ ] PostgreSQL kontejner deluje in je dostopen
- [ ] V bazo podatkov naloženi vzorčni podatki

**✅ Integracija VS Code**
- [ ] Konfiguriran `.vscode/mcp.json`
- [ ] Python interpreter nastavljen na virtualno okolje
- [ ] MCP strežniki se prikažejo v AI Chat
- [ ] Možno izvajanje testnih poizvedb prek AI Chat

## 🛠️ Odpravljanje pogostih težav

### Težave z Dockerjem

**Težava**: Docker kontejnerji se ne zaženejo
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

**Težava**: Povezava s PostgreSQL ne uspe
```bash
# Check container logs
docker-compose logs postgres

# Verify container is healthy
docker-compose ps

# Test direct connection
docker-compose exec postgres psql -U postgres -d zava -c "SELECT 1;"
```

### Težave z uvedbo Azure

**Težava**: Uvedba Azure ne uspe
```bash
# Check Azure CLI authentication
az account show

# Verify subscription permissions
az role assignment list --assignee $(az account show --query user.name -o tsv)

# Check resource provider registration
az provider register --namespace Microsoft.CognitiveServices
az provider register --namespace Microsoft.Insights
```

**Težava**: Avtentikacija AI storitve ne uspe
```bash
# Test service principal
az login --service-principal \
  --username $AZURE_CLIENT_ID \
  --password $AZURE_CLIENT_SECRET \
  --tenant $AZURE_TENANT_ID

# Verify AI service deployment
az cognitiveservices account list --query "[].{Name:name,Kind:kind,Location:location}"
```

### Težave z Python okoljem

**Težava**: Namestitev paketov ne uspe
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

**Težava**: VS Code ne najde Python interpreterja
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

## 🎯 Ključne ugotovitve

Po zaključku tega laboratorija bi morali imeti:

✅ **Popolno razvojno okolje**: Vsa orodja nameščena in konfigurirana  
✅ **Uvedeni Azure viri**: AI storitve in podporna infrastruktura  
✅ **Delujoče Docker okolje**: PostgreSQL in MCP strežniški kontejnerji  
✅ **Integracija VS Code**: MCP strežniki konfigurirani in dostopni  
✅ **Preverjena nastavitev**: Vse komponente testirane in delujejo skupaj  
✅ **Znanje odpravljanja težav**: Pogoste težave in rešitve  

## 🚀 Kaj sledi

Ko je vaše okolje pripravljeno, nadaljujte z **[Laboratorijem 04: Oblikovanje baze podatkov in shema](../04-Database/README.md)**, da:

- Podrobno raziščete shemo maloprodajne baze podatkov
- Razumete modeliranje podatkov za več najemnikov
- Naučite se implementacije varnosti na ravni vrstic
- Delate z vzorčnimi maloprodajnimi podatki

## 📚 Dodatni viri

### Razvojna orodja
- [Dokumentacija Dockerja](https://docs.docker.com/) - Celoten referenčni priročnik za Docker
- [Referenca Azure CLI](https://docs.microsoft.com/cli/azure/) - Ukazi Azure CLI
- [Dokumentacija VS Code](https://code.visualstudio.com/docs) - Konfiguracija urejevalnika in razširitve

### Azure storitve
- [Dokumentacija Azure AI Foundry](https://docs.microsoft.com/azure/ai-foundry/) - Konfiguracija AI storitev
- [Azure OpenAI storitev](https://docs.microsoft.com/azure/cognitive-services/openai/) - Uvedba AI modelov
- [Application Insights](https://docs.microsoft.com/azure/azure-monitor/app/app-insights-overview) - Nastavitev spremljanja

### Python razvoj
- [Virtualna okolja Python](https://docs.python.org/3/tutorial/venv.html) - Upravljanje okolij
- [Dokumentacija AsyncIO](https://docs.python.org/3/library/asyncio.html) - Vzorci asinhronega programiranja
- [Dokumentacija FastAPI](https://fastapi.tiangolo.com/) - Vzorci spletnega ogrodja

---

**Naprej**: Je okolje pripravljeno? Nadaljujte z [Laboratorijem 04: Oblikovanje baze podatkov in shema](../04-Database/README.md)

---

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve AI za prevajanje [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem maternem jeziku je treba obravnavati kot avtoritativni vir. Za ključne informacije priporočamo profesionalni človeški prevod. Ne prevzemamo odgovornosti za morebitna nesporazumevanja ali napačne razlage, ki izhajajo iz uporabe tega prevoda.