# Aplinkos paruošimas

## 🎯 Ką apima šis praktinis darbas

Šis praktinis darbas padės jums sukurti pilną kūrimo aplinką MCP serveriams su PostgreSQL integracija. Jūs sukonfigūruosite visus reikalingus įrankius, diegsite „Azure“ resursus ir patikrinsite savo aplinką prieš pradedant įgyvendinimą.

## Apžvalga

Tinkama kūrimo aplinka yra būtina sėkmingam MCP serverio kūrimui. Šiame praktiniame darbe pateikiamos nuoseklios instrukcijos, kaip įdiegti „Docker“, „Azure“ paslaugas, kūrimo įrankius ir patikrinti, ar viskas veikia kartu.

Baigę šį darbą, turėsite pilnai veikiančią kūrimo aplinką, paruoštą Zava Retail MCP serverio kūrimui.

## Mokymosi tikslai

Baigę šį praktinį darbą, galėsite:

- **Įdiegti ir sukonfigūruoti** visus reikalingus kūrimo įrankius
- **Diegti „Azure“ resursus**, reikalingus MCP serveriui
- **Sukurti „Docker“ konteinerius** PostgreSQL ir MCP serveriui
- **Patikrinti** savo aplinkos nustatymus su testiniais ryšiais
- **Spręsti problemas**, susijusias su nustatymais ir konfigūracija
- **Suprasti** kūrimo procesą ir failų struktūrą

## 📋 Būtini reikalavimai

Prieš pradedant, įsitikinkite, kad turite:

### Reikalingos žinios
- Pagrindiniai komandinės eilutės naudojimo įgūdžiai (Windows Command Prompt/PowerShell)
- Aplinkos kintamųjų supratimas
- Susipažinimas su Git versijų valdymu
- Pagrindinės „Docker“ sąvokos (konteineriai, vaizdai, tūriai)

### Sistemos reikalavimai
- **Operacinė sistema**: Windows 10/11, macOS arba Linux
- **RAM**: Mažiausiai 8GB (rekomenduojama 16GB)
- **Saugykla**: Bent 10GB laisvos vietos
- **Tinklas**: Interneto ryšys atsisiuntimams ir „Azure“ diegimui

### Paskyros reikalavimai
- **„Azure“ prenumerata**: Pakanka nemokamo plano
- **GitHub paskyra**: Prieigai prie saugyklos
- **„Docker Hub“ paskyra**: (Pasirinktinai) individualių vaizdų publikavimui

## 🛠️ Įrankių diegimas

### 1. Įdiekite „Docker Desktop“

„Docker“ suteikia konteinerizuotą aplinką mūsų kūrimo nustatymams.

#### Windows diegimas

1. **Atsisiųskite „Docker Desktop“**:
   ```cmd
   # Visit https://desktop.docker.com/win/stable/Docker%20Desktop%20Installer.exe
   # Or use Windows Package Manager
   winget install Docker.DockerDesktop
   ```

2. **Įdiekite ir sukonfigūruokite**:
   - Paleiskite diegimo programą kaip administratorius
   - Įjunkite WSL 2 integraciją, kai būsite paprašyti
   - Perkraukite kompiuterį, kai diegimas bus baigtas

3. **Patikrinkite diegimą**:
   ```cmd
   docker --version
   docker-compose --version
   ```

#### macOS diegimas

1. **Atsisiųskite ir įdiekite**:
   ```bash
   # Download from https://desktop.docker.com/mac/stable/Docker.dmg
   # Or use Homebrew
   brew install --cask docker
   ```

2. **Paleiskite „Docker Desktop“**:
   - Paleiskite „Docker Desktop“ iš „Applications“
   - Užbaikite pradinį nustatymų vedlį

3. **Patikrinkite diegimą**:
   ```bash
   docker --version
   docker-compose --version
   ```

#### Linux diegimas

1. **Įdiekite „Docker Engine“**:
   ```bash
   # Ubuntu/Debian
   curl -fsSL https://get.docker.com -o get-docker.sh
   sudo sh get-docker.sh
   sudo usermod -aG docker $USER
   
   # Log out and back in for group changes to take effect
   ```

2. **Įdiekite „Docker Compose“**:
   ```bash
   sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
   sudo chmod +x /usr/local/bin/docker-compose
   ```

### 2. Įdiekite „Azure CLI“

„Azure CLI“ leidžia diegti ir valdyti „Azure“ resursus.

#### Windows diegimas

```cmd
# Using Windows Package Manager
winget install Microsoft.AzureCLI

# Or download MSI from: https://aka.ms/installazurecliwindows
```

#### macOS diegimas

```bash
# Using Homebrew
brew install azure-cli

# Or using installer
curl -L https://aka.ms/InstallAzureCli | bash
```

#### Linux diegimas

```bash
# Ubuntu/Debian
curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash

# RHEL/CentOS
sudo rpm --import https://packages.microsoft.com/keys/microsoft.asc
sudo dnf install azure-cli
```

#### Patikrinkite ir autentifikuokite

```bash
# Check installation
az version

# Login to Azure
az login

# Set default subscription (if you have multiple)
az account list --output table
az account set --subscription "Your-Subscription-Name"
```

### 3. Įdiekite Git

Git reikalingas saugyklos klonavimui ir versijų valdymui.

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

### 4. Įdiekite VS Code

„Visual Studio Code“ suteikia integruotą kūrimo aplinką su MCP palaikymu.

#### Diegimas

```cmd
# Windows
winget install Microsoft.VisualStudioCode

# macOS
brew install --cask visual-studio-code

# Linux (Ubuntu/Debian)
sudo snap install code --classic
```

#### Reikalingi plėtiniai

Įdiekite šiuos VS Code plėtinius:

```bash
# Install via command line
code --install-extension ms-python.python
code --install-extension ms-vscode.vscode-json
code --install-extension ms-azuretools.vscode-docker
code --install-extension ms-vscode.azure-account
```

Arba įdiekite per VS Code:
1. Atidarykite VS Code
2. Eikite į plėtinius (Ctrl+Shift+X)
3. Įdiekite:
   - **Python** (Microsoft)
   - **Docker** (Microsoft)
   - **Azure Account** (Microsoft)
   - **JSON** (Microsoft)

### 5. Įdiekite Python

Python 3.8+ reikalingas MCP serverio kūrimui.

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

#### Patikrinkite diegimą

```bash
python --version  # Should show Python 3.11.x
pip --version      # Should show pip version
```

## 🚀 Projekto nustatymas

### 1. Klonuokite saugyklą

```bash
# Clone the main repository
git clone https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail.git

# Navigate to the project directory
cd MCP-Server-and-PostgreSQL-Sample-Retail

# Verify repository structure
ls -la
```

### 2. Sukurkite Python virtualią aplinką

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

### 3. Įdiekite Python priklausomybes

```bash
# Install development dependencies
pip install -r requirements.lock.txt

# Verify key packages
pip list | grep fastmcp
pip list | grep asyncpg
pip list | grep azure
```

## ☁️ „Azure“ resursų diegimas

### 1. Supraskite resursų reikalavimus

Mūsų MCP serveriui reikalingi šie „Azure“ resursai:

| **Resursas** | **Paskirtis** | **Numatoma kaina** |
|--------------|-------------|-------------------|
| **Azure AI Foundry** | AI modelių talpinimas ir valdymas | $10-50/mėn. |
| **OpenAI diegimas** | Teksto įterpimo modelis (text-embedding-3-small) | $5-20/mėn. |
| **Application Insights** | Stebėjimas ir telemetrija | $5-15/mėn. |
| **Resursų grupė** | Resursų organizavimas | Nemokama |

### 2. Diegti „Azure“ resursus

#### A variantas: Automatinis diegimas (rekomenduojama)

```bash
# Navigate to infrastructure directory
cd infra

# Windows - PowerShell
./deploy.ps1

# macOS/Linux - Bash
./deploy.sh
```

Diegimo scenarijus atliks:
1. Sukurs unikalią resursų grupę
2. Įdiegs „Azure AI Foundry“ resursus
3. Įdiegs text-embedding-3-small modelį
4. Suaktyvins „Application Insights“
5. Sukurs paslaugų principą autentifikacijai
6. Sugeneruos `.env` failą su konfigūracija

#### B variantas: Rankinis diegimas

Jei norite rankinio valdymo arba automatinis scenarijus nepavyksta:

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

### 3. Patikrinkite „Azure“ diegimą

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

### 4. Konfigūruokite aplinkos kintamuosius

Po diegimo turėtumėte turėti `.env` failą. Patikrinkite, ar jame yra:

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

## 🐳 „Docker“ aplinkos nustatymas

### 1. Supraskite „Docker“ sudėtį

Mūsų kūrimo aplinka naudoja „Docker Compose“:

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

### 2. Paleiskite kūrimo aplinką

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

### 3. Patikrinkite duomenų bazės nustatymus

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

### 4. Testuokite MCP serverį

```bash
# Check MCP server health
curl http://localhost:8000/health

# Test basic MCP endpoint
curl -X POST http://localhost:8000/mcp \
  -H "Content-Type: application/json" \
  -H "x-rls-user-id: 00000000-0000-0000-0000-000000000000" \
  -d '{"method": "tools/list", "params": {}}'
```

## 🔧 VS Code konfigūracija

### 1. Konfigūruokite MCP integraciją

Sukurkite VS Code MCP konfigūraciją:

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

### 2. Konfigūruokite Python aplinką

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

### 3. Testuokite VS Code integraciją

1. **Atidarykite projektą VS Code**:
   ```bash
   code .
   ```

2. **Atidarykite AI pokalbį**:
   - Paspauskite `Ctrl+Shift+P` (Windows/Linux) arba `Cmd+Shift+P` (macOS)
   - Įveskite „AI Chat“ ir pasirinkite „AI Chat: Open Chat“

3. **Testuokite MCP serverio ryšį**:
   - AI pokalbyje įveskite `#zava` ir pasirinkite vieną iš sukonfigūruotų serverių
   - Paklauskite: „Kokios lentelės yra duomenų bazėje?“
   - Turėtumėte gauti atsakymą su mažmeninės prekybos duomenų bazės lentelėmis

## ✅ Aplinkos patikrinimas

### 1. Išsamus sistemos patikrinimas

Paleiskite šį patikrinimo scenarijų, kad patikrintumėte savo nustatymus:

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

### 2. Rankinis patikrinimo sąrašas

**✅ Pagrindiniai įrankiai**
- [ ] Įdiegta ir veikia „Docker“ versija 20.10+
- [ ] Įdiegta ir autentifikuota „Azure CLI“ 2.40+
- [ ] Įdiegta Python 3.8+ su pip
- [ ] Įdiegta Git 2.30+
- [ ] VS Code su reikalingais plėtiniais

**✅ „Azure“ resursai**
- [ ] Sėkmingai sukurta resursų grupė
- [ ] Įdiegtas AI Foundry projektas
- [ ] Įdiegtas OpenAI text-embedding-3-small modelis
- [ ] Suaktyvintas „Application Insights“
- [ ] Sukurtas paslaugų principas su tinkamomis teisėmis

**✅ Aplinkos konfigūracija**
- [ ] Sukurtas `.env` failas su visais reikalingais kintamaisiais
- [ ] Veikia „Azure“ kredencialai (patikrinkite su `az account show`)
- [ ] Veikia PostgreSQL konteineris ir jis pasiekiamas
- [ ] Duomenų bazėje įkelti pavyzdiniai duomenys

**✅ VS Code integracija**
- [ ] Suformuotas `.vscode/mcp.json`
- [ ] Python interpretatorius nustatytas į virtualią aplinką
- [ ] MCP serveriai rodomi AI pokalbyje
- [ ] Galima vykdyti testinius užklausimus per AI pokalbį

## 🛠️ Dažniausiai pasitaikančių problemų sprendimas

### „Docker“ problemos

**Problema**: „Docker“ konteineriai nepasileidžia
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

**Problema**: Nepavyksta prisijungti prie PostgreSQL
```bash
# Check container logs
docker-compose logs postgres

# Verify container is healthy
docker-compose ps

# Test direct connection
docker-compose exec postgres psql -U postgres -d zava -c "SELECT 1;"
```

### „Azure“ diegimo problemos

**Problema**: „Azure“ diegimas nepavyksta
```bash
# Check Azure CLI authentication
az account show

# Verify subscription permissions
az role assignment list --assignee $(az account show --query user.name -o tsv)

# Check resource provider registration
az provider register --namespace Microsoft.CognitiveServices
az provider register --namespace Microsoft.Insights
```

**Problema**: Nepavyksta autentifikuoti AI paslaugos
```bash
# Test service principal
az login --service-principal \
  --username $AZURE_CLIENT_ID \
  --password $AZURE_CLIENT_SECRET \
  --tenant $AZURE_TENANT_ID

# Verify AI service deployment
az cognitiveservices account list --query "[].{Name:name,Kind:kind,Location:location}"
```

### Python aplinkos problemos

**Problema**: Nepavyksta įdiegti paketų
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

**Problema**: VS Code neranda Python interpretatoriaus
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

## 🎯 Pagrindinės išvados

Baigę šį praktinį darbą, turėtumėte:

✅ **Pilna kūrimo aplinka**: Visi įrankiai įdiegti ir sukonfigūruoti  
✅ **„Azure“ resursai įdiegti**: AI paslaugos ir palaikomoji infrastruktūra  
✅ **„Docker“ aplinka veikia**: PostgreSQL ir MCP serverio konteineriai  
✅ **VS Code integracija**: MCP serveriai sukonfigūruoti ir pasiekiami  
✅ **Patikrinta aplinka**: Visi komponentai išbandyti ir veikia kartu  
✅ **Žinios apie problemų sprendimą**: Dažniausiai pasitaikančios problemos ir jų sprendimai  

## 🚀 Kas toliau

Kai aplinka paruošta, tęskite **[Lab 04: Duomenų bazės dizainas ir schema](../04-Database/README.md)**, kur:

- Išsamiai susipažinsite su mažmeninės prekybos duomenų bazės schema
- Suprasite daugiabučių duomenų modeliavimą
- Išmoksite įgyvendinti eilės lygio saugumą
- Dirbsite su pavyzdiniais mažmeninės prekybos duomenimis

## 📚 Papildomi ištekliai

### Kūrimo įrankiai
- [„Docker“ dokumentacija](https://docs.docker.com/) - Pilnas „Docker“ vadovas
- [„Azure CLI“ nuoroda](https://docs.microsoft.com/cli/azure/) - „Azure CLI“ komandos
- [VS Code dokumentacija](https://code.visualstudio.com/docs) - Redaktoriaus konfigūracija ir plėtiniai

### „Azure“ paslaugos
- [„Azure AI Foundry“ dokumentacija](https://docs.microsoft.com/azure/ai-foundry/) - AI paslaugų konfigūracija
- [„Azure OpenAI“ paslauga](https://docs.microsoft.com/azure/cognitive-services/openai/) - AI modelio diegimas
- [„Application Insights“](https://docs.microsoft.com/azure/azure-monitor/app/app-insights-overview) - Stebėjimo nustatymas

### Python kūrimas
- [Python virtualios aplinkos](https://docs.python.org/3/tutorial/venv.html) - Aplinkos valdymas
- [AsyncIO dokumentacija](https://docs.python.org/3/library/asyncio.html) - Asinchroninio programavimo modeliai
- [FastAPI dokumentacija](https://fastapi.tiangolo.com/) - Žiniatinklio karkaso modeliai

---

**Toliau**: Aplinka paruošta? Tęskite su [Lab 04: Duomenų bazės dizainas ir schema](../04-Database/README.md)

---

**Atsakomybės atsisakymas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors stengiamės užtikrinti tikslumą, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojama naudoti profesionalų žmogaus vertimą. Mes neprisiimame atsakomybės už nesusipratimus ar neteisingus interpretavimus, atsiradusius dėl šio vertimo naudojimo.