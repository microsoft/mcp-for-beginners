# Környezet Beállítása

## 🎯 Mit Tartalmaz Ez a Gyakorlat?

Ez a gyakorlati útmutató végigvezet egy teljes fejlesztői környezet beállításán MCP szerverek PostgreSQL integrációval történő fejlesztéséhez. Konfigurálni fogod a szükséges eszközöket, telepítesz Azure erőforrásokat, és ellenőrzöd a beállítást, mielőtt elkezdenéd a megvalósítást.

## Áttekintés

Egy megfelelő fejlesztői környezet kulcsfontosságú az MCP szerverek sikeres fejlesztéséhez. Ez a gyakorlat lépésről lépésre bemutatja, hogyan állítsd be a Docker-t, az Azure szolgáltatásokat, a fejlesztői eszközöket, és hogyan ellenőrizd, hogy minden megfelelően működik együtt.

A gyakorlat végére egy teljesen működőképes fejlesztői környezeted lesz, amely készen áll a Zava Retail MCP szerver fejlesztésére.

## Tanulási Célok

A gyakorlat végére képes leszel:

- **Telepíteni és konfigurálni** az összes szükséges fejlesztői eszközt
- **Telepíteni Azure erőforrásokat**, amelyek szükségesek az MCP szerverhez
- **Beállítani Docker konténereket** PostgreSQL-hez és az MCP szerverhez
- **Ellenőrizni** a környezet beállítását tesztkapcsolatokkal
- **Hibakeresni** gyakori beállítási problémákat és konfigurációs hibákat
- **Megérteni** a fejlesztési munkafolyamatot és a fájlszerkezetet

## 📋 Előfeltételek Ellenőrzése

Mielőtt elkezdenéd, győződj meg róla, hogy rendelkezel az alábbiakkal:

### Szükséges Ismeretek
- Alapvető parancssori használat (Windows Command Prompt/PowerShell)
- Környezeti változók megértése
- Git verziókezelés ismerete
- Alapvető Docker fogalmak (konténerek, képek, kötetek)

### Rendszerkövetelmények
- **Operációs Rendszer**: Windows 10/11, macOS vagy Linux
- **RAM**: Minimum 8GB (ajánlott 16GB)
- **Tárhely**: Legalább 10GB szabad hely
- **Hálózat**: Internetkapcsolat letöltésekhez és Azure telepítéshez

### Fiókkövetelmények
- **Azure Előfizetés**: Ingyenes szint elegendő
- **GitHub Fiók**: A repozitórium eléréséhez
- **Docker Hub Fiók**: (Opcionális) Egyedi képek közzétételéhez

## 🛠️ Eszközök Telepítése

### 1. Docker Desktop Telepítése

A Docker biztosítja a konténerizált környezetet a fejlesztési beállításhoz.

#### Windows Telepítés

1. **Docker Desktop Letöltése**:
   ```cmd
   # Visit https://desktop.docker.com/win/stable/Docker%20Desktop%20Installer.exe
   # Or use Windows Package Manager
   winget install Docker.DockerDesktop
   ```

2. **Telepítés és Konfigurálás**:
   - Futtasd az installer-t rendszergazdaként
   - Engedélyezd a WSL 2 integrációt, amikor kéri
   - Indítsd újra a számítógépet a telepítés befejezése után

3. **Telepítés Ellenőrzése**:
   ```cmd
   docker --version
   docker-compose --version
   ```

#### macOS Telepítés

1. **Letöltés és Telepítés**:
   ```bash
   # Download from https://desktop.docker.com/mac/stable/Docker.dmg
   # Or use Homebrew
   brew install --cask docker
   ```

2. **Docker Desktop Indítása**:
   - Indítsd el a Docker Desktopot az Alkalmazásokból
   - Fejezd be a kezdeti beállítási varázslót

3. **Telepítés Ellenőrzése**:
   ```bash
   docker --version
   docker-compose --version
   ```

#### Linux Telepítés

1. **Docker Engine Telepítése**:
   ```bash
   # Ubuntu/Debian
   curl -fsSL https://get.docker.com -o get-docker.sh
   sudo sh get-docker.sh
   sudo usermod -aG docker $USER
   
   # Log out and back in for group changes to take effect
   ```

2. **Docker Compose Telepítése**:
   ```bash
   sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
   sudo chmod +x /usr/local/bin/docker-compose
   ```

### 2. Azure CLI Telepítése

Az Azure CLI lehetővé teszi az Azure erőforrások telepítését és kezelését.

#### Windows Telepítés

```cmd
# Using Windows Package Manager
winget install Microsoft.AzureCLI

# Or download MSI from: https://aka.ms/installazurecliwindows
```

#### macOS Telepítés

```bash
# Using Homebrew
brew install azure-cli

# Or using installer
curl -L https://aka.ms/InstallAzureCli | bash
```

#### Linux Telepítés

```bash
# Ubuntu/Debian
curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash

# RHEL/CentOS
sudo rpm --import https://packages.microsoft.com/keys/microsoft.asc
sudo dnf install azure-cli
```

#### Ellenőrzés és Hitelesítés

```bash
# Check installation
az version

# Login to Azure
az login

# Set default subscription (if you have multiple)
az account list --output table
az account set --subscription "Your-Subscription-Name"
```

### 3. Git Telepítése

A Git szükséges a repozitórium klónozásához és a verziókezeléshez.

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

### 4. VS Code Telepítése

A Visual Studio Code integrált fejlesztői környezetet biztosít MCP támogatással.

#### Telepítés

```cmd
# Windows
winget install Microsoft.VisualStudioCode

# macOS
brew install --cask visual-studio-code

# Linux (Ubuntu/Debian)
sudo snap install code --classic
```

#### Szükséges Bővítmények

Telepítsd ezeket a VS Code bővítményeket:

```bash
# Install via command line
code --install-extension ms-python.python
code --install-extension ms-vscode.vscode-json
code --install-extension ms-azuretools.vscode-docker
code --install-extension ms-vscode.azure-account
```

Vagy telepítsd a VS Code-on keresztül:
1. Nyisd meg a VS Code-ot
2. Menj a Bővítményekhez (Ctrl+Shift+X)
3. Telepítsd:
   - **Python** (Microsoft)
   - **Docker** (Microsoft)
   - **Azure Account** (Microsoft)
   - **JSON** (Microsoft)

### 5. Python Telepítése

Python 3.8+ szükséges az MCP szerver fejlesztéséhez.

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

#### Telepítés Ellenőrzése

```bash
python --version  # Should show Python 3.11.x
pip --version      # Should show pip version
```

## 🚀 Projekt Beállítása

### 1. Repozitórium Klónozása

```bash
# Clone the main repository
git clone https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail.git

# Navigate to the project directory
cd MCP-Server-and-PostgreSQL-Sample-Retail

# Verify repository structure
ls -la
```

### 2. Python Virtuális Környezet Létrehozása

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

### 3. Python Függőségek Telepítése

```bash
# Install development dependencies
pip install -r requirements.lock.txt

# Verify key packages
pip list | grep fastmcp
pip list | grep asyncpg
pip list | grep azure
```

## ☁️ Azure Erőforrások Telepítése

### 1. Erőforrás Követelmények Megértése

Az MCP szerverhez az alábbi Azure erőforrásokra van szükség:

| **Erőforrás** | **Cél** | **Becsült Költség** |
|---------------|---------|--------------------|
| **Azure AI Foundry** | AI modellek hosztolása és kezelése | $10-50/hónap |
| **OpenAI Telepítés** | Szövegbeágyazási modell (text-embedding-3-small) | $5-20/hónap |
| **Application Insights** | Monitorozás és telemetria | $5-15/hónap |
| **Erőforráscsoport** | Erőforrások szervezése | Ingyenes |

### 2. Azure Erőforrások Telepítése

#### Opció A: Automatikus Telepítés (Ajánlott)

```bash
# Navigate to infrastructure directory
cd infra

# Windows - PowerShell
./deploy.ps1

# macOS/Linux - Bash
./deploy.sh
```

A telepítési szkript a következőket végzi el:
1. Egyedi erőforráscsoport létrehozása
2. Azure AI Foundry erőforrások telepítése
3. A text-embedding-3-small modell telepítése
4. Application Insights konfigurálása
5. Szolgáltatási főazonosító létrehozása hitelesítéshez
6. `.env` fájl generálása konfigurációval

#### Opció B: Manuális Telepítés

Ha inkább manuálisan szeretnéd kezelni, vagy az automatikus szkript nem működik:

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

### 3. Azure Telepítés Ellenőrzése

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

### 4. Környezeti Változók Konfigurálása

A telepítés után rendelkezned kell egy `.env` fájllal. Ellenőrizd, hogy tartalmazza:

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

## 🐳 Docker Környezet Beállítása

### 1. Docker Kompozíció Megértése

A fejlesztői környezet Docker Compose-t használ:

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

### 2. Fejlesztői Környezet Indítása

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

### 3. Adatbázis Beállítás Ellenőrzése

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

### 4. MCP Szerver Tesztelése

```bash
# Check MCP server health
curl http://localhost:8000/health

# Test basic MCP endpoint
curl -X POST http://localhost:8000/mcp \
  -H "Content-Type: application/json" \
  -H "x-rls-user-id: 00000000-0000-0000-0000-000000000000" \
  -d '{"method": "tools/list", "params": {}}'
```

## 🔧 VS Code Konfiguráció

### 1. MCP Integráció Konfigurálása

Hozd létre a VS Code MCP konfigurációt:

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

### 2. Python Környezet Konfigurálása

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

### 3. VS Code Integráció Tesztelése

1. **Nyisd meg a projektet a VS Code-ban**:
   ```bash
   code .
   ```

2. **Nyisd meg az AI Chat-et**:
   - Nyomd meg a `Ctrl+Shift+P` (Windows/Linux) vagy `Cmd+Shift+P` (macOS) billentyűkombinációt
   - Írd be: "AI Chat" és válaszd az "AI Chat: Open Chat" opciót

3. **MCP Szerver Kapcsolat Tesztelése**:
   - Az AI Chat-ben írd be: `#zava` és válaszd ki az egyik konfigurált szervert
   - Kérdezd meg: "Milyen táblák érhetők el az adatbázisban?"
   - Válaszként meg kell kapnod a kiskereskedelmi adatbázis tábláinak listáját

## ✅ Környezet Ellenőrzése

### 1. Átfogó Rendszer Ellenőrzés

Futtasd ezt az ellenőrzési szkriptet a beállításod ellenőrzéséhez:

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

### 2. Manuális Ellenőrzési Lista

**✅ Alapvető Eszközök**
- [ ] Docker 20.10+ verzió telepítve és fut
- [ ] Azure CLI 2.40+ telepítve és hitelesítve
- [ ] Python 3.8+ pip-pel telepítve
- [ ] Git 2.30+ telepítve
- [ ] VS Code a szükséges bővítményekkel

**✅ Azure Erőforrások**
- [ ] Erőforráscsoport sikeresen létrehozva
- [ ] AI Foundry projekt telepítve
- [ ] OpenAI text-embedding-3-small modell telepítve
- [ ] Application Insights konfigurálva
- [ ] Szolgáltatási főazonosító megfelelő jogosultságokkal létrehozva

**✅ Környezet Konfiguráció**
- [ ] `.env` fájl létrehozva az összes szükséges változóval
- [ ] Azure hitelesítő adatok működnek (teszteld az `az account show` paranccsal)
- [ ] PostgreSQL konténer fut és elérhető
- [ ] Mintaadatok betöltve az adatbázisba

**✅ VS Code Integráció**
- [ ] `.vscode/mcp.json` konfigurálva
- [ ] Python interpreter beállítva a virtuális környezetre
- [ ] MCP szerverek megjelennek az AI Chat-ben
- [ ] Tesztlekérdezések végrehajthatók az AI Chat-en keresztül

## 🛠️ Gyakori Problémák Hibakeresése

### Docker Problémák

**Probléma**: A Docker konténerek nem indulnak el
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

**Probléma**: PostgreSQL kapcsolat sikertelen
```bash
# Check container logs
docker-compose logs postgres

# Verify container is healthy
docker-compose ps

# Test direct connection
docker-compose exec postgres psql -U postgres -d zava -c "SELECT 1;"
```

### Azure Telepítési Problémák

**Probléma**: Azure telepítés sikertelen
```bash
# Check Azure CLI authentication
az account show

# Verify subscription permissions
az role assignment list --assignee $(az account show --query user.name -o tsv)

# Check resource provider registration
az provider register --namespace Microsoft.CognitiveServices
az provider register --namespace Microsoft.Insights
```

**Probléma**: AI szolgáltatás hitelesítése sikertelen
```bash
# Test service principal
az login --service-principal \
  --username $AZURE_CLIENT_ID \
  --password $AZURE_CLIENT_SECRET \
  --tenant $AZURE_TENANT_ID

# Verify AI service deployment
az cognitiveservices account list --query "[].{Name:name,Kind:kind,Location:location}"
```

### Python Környezet Problémák

**Probléma**: Csomag telepítés sikertelen
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

**Probléma**: VS Code nem találja a Python interpretert
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

## 🎯 Főbb Tanulságok

A gyakorlat elvégzése után rendelkezned kell:

✅ **Teljes Fejlesztői Környezet**: Minden eszköz telepítve és konfigurálva  
✅ **Azure Erőforrások Telepítve**: AI szolgáltatások és támogató infrastruktúra  
✅ **Docker Környezet Fut**: PostgreSQL és MCP szerver konténerek  
✅ **VS Code Integráció**: MCP szerverek konfigurálva és elérhetők  
✅ **Ellenőrzött Beállítás**: Minden komponens tesztelve és együtt működik  
✅ **Hibakeresési Ismeretek**: Gyakori problémák és megoldások  

## 🚀 Hogyan Tovább?

Ha a környezeted készen áll, folytasd a **[Lab 04: Adatbázis Tervezés és Sémák](../04-Database/README.md)** gyakorlatot, hogy:

- Részletesen megismerd a kiskereskedelmi adatbázis sémáját
- Megértsd a több-bérlős adatmodellezést
- Megtanuld a sor szintű biztonság megvalósítását
- Dolgozz mintakiskereskedelmi adatokkal

## 📚 További Források

### Fejlesztői Eszközök
- [Docker Dokumentáció](https://docs.docker.com/) - Teljes Docker referencia
- [Azure CLI Referencia](https://docs.microsoft.com/cli/azure/) - Azure CLI parancsok
- [VS Code Dokumentáció](https://code.visualstudio.com/docs) - Szerkesztő konfiguráció és bővítmények

### Azure Szolgáltatások
- [Azure AI Foundry Dokumentáció](https://docs.microsoft.com/azure/ai-foundry/) - AI szolgáltatás konfiguráció
- [Azure OpenAI Szolgáltatás](https://docs.microsoft.com/azure/cognitive-services/openai/) - AI modell telepítés
- [Application Insights](https://docs.microsoft.com/azure/azure-monitor/app/app-insights-overview) - Monitorozási beállítás

### Python Fejlesztés
- [Python Virtuális Környezetek](https://docs.python.org/3/tutorial/venv.html) - Környezetkezelés
- [AsyncIO Dokumentáció](https://docs.python.org/3/library/asyncio.html) - Aszinkron programozási minták
- [FastAPI Dokumentáció](https://fastapi.tiangolo.com/) - Webes keretrendszer minták

---

**Következő**: Készen áll a környezet? Folytasd a [Lab 04: Adatbázis Tervezés és Sémák](../04-Database/README.md) gyakorlatot.

---

**Felelősség kizárása**:  
Ez a dokumentum az [Co-op Translator](https://github.com/Azure/co-op-translator) AI fordítási szolgáltatás segítségével került lefordításra. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az eredeti nyelvén tekintendő hiteles forrásnak. Kritikus információk esetén javasolt professzionális emberi fordítást igénybe venni. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely a fordítás használatából eredhet.