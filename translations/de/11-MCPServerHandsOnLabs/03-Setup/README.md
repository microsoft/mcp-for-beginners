# Einrichtungsumgebung

## 🎯 Was dieser Workshop abdeckt

Dieser praktische Workshop führt Sie durch die Einrichtung einer vollständigen Entwicklungsumgebung für die Erstellung von MCP-Servern mit PostgreSQL-Integration. Sie konfigurieren alle erforderlichen Tools, stellen Azure-Ressourcen bereit und validieren Ihre Einrichtung, bevor Sie mit der Implementierung fortfahren.

## Überblick

Eine ordnungsgemäße Entwicklungsumgebung ist entscheidend für die erfolgreiche Entwicklung von MCP-Servern. Dieser Workshop bietet Schritt-für-Schritt-Anleitungen zur Einrichtung von Docker, Azure-Diensten, Entwicklungstools und zur Validierung, dass alles korrekt zusammenarbeitet.

Am Ende dieses Workshops verfügen Sie über eine vollständig funktionierende Entwicklungsumgebung, die bereit ist, den Zava Retail MCP-Server zu erstellen.

## Lernziele

Am Ende dieses Workshops können Sie:

- **Installieren und konfigurieren** aller erforderlichen Entwicklungstools
- **Azure-Ressourcen bereitstellen**, die für den MCP-Server benötigt werden
- **Docker-Container einrichten** für PostgreSQL und den MCP-Server
- **Ihre Umgebung validieren** mit Testverbindungen
- **Häufige Probleme beheben** bei der Einrichtung und Konfiguration
- **Den Entwicklungsworkflow und die Dateistruktur verstehen**

## 📋 Voraussetzungen überprüfen

Bevor Sie beginnen, stellen Sie sicher, dass Sie Folgendes haben:

### Erforderliches Wissen
- Grundlegende Befehlszeilenkenntnisse (Windows Command Prompt/PowerShell)
- Verständnis von Umgebungsvariablen
- Vertrautheit mit Git-Versionierung
- Grundlegende Docker-Konzepte (Container, Images, Volumes)

### Systemanforderungen
- **Betriebssystem**: Windows 10/11, macOS oder Linux
- **RAM**: Mindestens 8 GB (16 GB empfohlen)
- **Speicherplatz**: Mindestens 10 GB freier Speicherplatz
- **Netzwerk**: Internetverbindung für Downloads und Azure-Bereitstellung

### Kontoanforderungen
- **Azure-Abonnement**: Kostenloses Konto ist ausreichend
- **GitHub-Konto**: Für den Zugriff auf das Repository
- **Docker Hub-Konto**: (Optional) Für die Veröffentlichung benutzerdefinierter Images

## 🛠️ Tool-Installation

### 1. Docker Desktop installieren

Docker bietet die containerisierte Umgebung für unsere Entwicklungsumgebung.

#### Windows-Installation

1. **Docker Desktop herunterladen**:
   ```cmd
   # Visit https://desktop.docker.com/win/stable/Docker%20Desktop%20Installer.exe
   # Or use Windows Package Manager
   winget install Docker.DockerDesktop
   ```

2. **Installieren und konfigurieren**:
   - Führen Sie das Installationsprogramm als Administrator aus
   - Aktivieren Sie die WSL 2-Integration, wenn Sie dazu aufgefordert werden
   - Starten Sie Ihren Computer neu, nachdem die Installation abgeschlossen ist

3. **Installation überprüfen**:
   ```cmd
   docker --version
   docker-compose --version
   ```

#### macOS-Installation

1. **Herunterladen und installieren**:
   ```bash
   # Download from https://desktop.docker.com/mac/stable/Docker.dmg
   # Or use Homebrew
   brew install --cask docker
   ```

2. **Docker Desktop starten**:
   - Starten Sie Docker Desktop aus den Anwendungen
   - Schließen Sie den Einrichtungsassistenten ab

3. **Installation überprüfen**:
   ```bash
   docker --version
   docker-compose --version
   ```

#### Linux-Installation

1. **Docker Engine installieren**:
   ```bash
   # Ubuntu/Debian
   curl -fsSL https://get.docker.com -o get-docker.sh
   sudo sh get-docker.sh
   sudo usermod -aG docker $USER
   
   # Log out and back in for group changes to take effect
   ```

2. **Docker Compose installieren**:
   ```bash
   sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
   sudo chmod +x /usr/local/bin/docker-compose
   ```

### 2. Azure CLI installieren

Die Azure CLI ermöglicht die Bereitstellung und Verwaltung von Azure-Ressourcen.

#### Windows-Installation

```cmd
# Using Windows Package Manager
winget install Microsoft.AzureCLI

# Or download MSI from: https://aka.ms/installazurecliwindows
```

#### macOS-Installation

```bash
# Using Homebrew
brew install azure-cli

# Or using installer
curl -L https://aka.ms/InstallAzureCli | bash
```

#### Linux-Installation

```bash
# Ubuntu/Debian
curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash

# RHEL/CentOS
sudo rpm --import https://packages.microsoft.com/keys/microsoft.asc
sudo dnf install azure-cli
```

#### Überprüfen und authentifizieren

```bash
# Check installation
az version

# Login to Azure
az login

# Set default subscription (if you have multiple)
az account list --output table
az account set --subscription "Your-Subscription-Name"
```

### 3. Git installieren

Git wird benötigt, um das Repository zu klonen und die Versionskontrolle zu verwalten.

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

### 4. VS Code installieren

Visual Studio Code bietet die integrierte Entwicklungsumgebung mit MCP-Unterstützung.

#### Installation

```cmd
# Windows
winget install Microsoft.VisualStudioCode

# macOS
brew install --cask visual-studio-code

# Linux (Ubuntu/Debian)
sudo snap install code --classic
```

#### Erforderliche Erweiterungen

Installieren Sie diese VS Code-Erweiterungen:

```bash
# Install via command line
code --install-extension ms-python.python
code --install-extension ms-vscode.vscode-json
code --install-extension ms-azuretools.vscode-docker
code --install-extension ms-vscode.azure-account
```

Oder installieren Sie sie über VS Code:
1. Öffnen Sie VS Code
2. Gehen Sie zu Erweiterungen (Strg+Shift+X)
3. Installieren Sie:
   - **Python** (Microsoft)
   - **Docker** (Microsoft)
   - **Azure Account** (Microsoft)
   - **JSON** (Microsoft)

### 5. Python installieren

Python 3.8+ ist erforderlich für die Entwicklung des MCP-Servers.

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

#### Installation überprüfen

```bash
python --version  # Should show Python 3.11.x
pip --version      # Should show pip version
```

## 🚀 Projekt einrichten

### 1. Repository klonen

```bash
# Clone the main repository
git clone https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail.git

# Navigate to the project directory
cd MCP-Server-and-PostgreSQL-Sample-Retail

# Verify repository structure
ls -la
```

### 2. Virtuelle Python-Umgebung erstellen

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

### 3. Python-Abhängigkeiten installieren

```bash
# Install development dependencies
pip install -r requirements.lock.txt

# Verify key packages
pip list | grep fastmcp
pip list | grep asyncpg
pip list | grep azure
```

## ☁️ Azure-Ressourcen bereitstellen

### 1. Ressourcenanforderungen verstehen

Unser MCP-Server benötigt folgende Azure-Ressourcen:

| **Ressource** | **Zweck** | **Geschätzte Kosten** |
|---------------|-----------|-----------------------|
| **Azure AI Foundry** | Hosting und Verwaltung von KI-Modellen | $10-50/Monat |
| **OpenAI-Bereitstellung** | Text-Einbettungsmodell (text-embedding-3-small) | $5-20/Monat |
| **Application Insights** | Überwachung und Telemetrie | $5-15/Monat |
| **Ressourcengruppe** | Ressourcenorganisation | Kostenlos |

### 2. Azure-Ressourcen bereitstellen

#### Option A: Automatisierte Bereitstellung (Empfohlen)

```bash
# Navigate to infrastructure directory
cd infra

# Windows - PowerShell
./deploy.ps1

# macOS/Linux - Bash
./deploy.sh
```

Das Bereitstellungsskript wird:
1. Eine eindeutige Ressourcengruppe erstellen
2. Azure AI Foundry-Ressourcen bereitstellen
3. Das Modell text-embedding-3-small bereitstellen
4. Application Insights konfigurieren
5. Einen Dienstprinzipal für die Authentifizierung erstellen
6. Eine `.env`-Datei mit Konfiguration generieren

#### Option B: Manuelle Bereitstellung

Falls Sie manuelle Kontrolle bevorzugen oder das automatisierte Skript fehlschlägt:

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

### 3. Azure-Bereitstellung überprüfen

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

### 4. Umgebungsvariablen konfigurieren

Nach der Bereitstellung sollten Sie eine `.env`-Datei haben. Überprüfen Sie, ob sie Folgendes enthält:

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

## 🐳 Docker-Umgebung einrichten

### 1. Docker-Komposition verstehen

Unsere Entwicklungsumgebung verwendet Docker Compose:

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

### 2. Entwicklungsumgebung starten

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

### 3. Datenbankeinrichtung überprüfen

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

### 4. MCP-Server testen

```bash
# Check MCP server health
curl http://localhost:8000/health

# Test basic MCP endpoint
curl -X POST http://localhost:8000/mcp \
  -H "Content-Type: application/json" \
  -H "x-rls-user-id: 00000000-0000-0000-0000-000000000000" \
  -d '{"method": "tools/list", "params": {}}'
```

## 🔧 VS Code-Konfiguration

### 1. MCP-Integration konfigurieren

Erstellen Sie die MCP-Konfiguration für VS Code:

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

### 2. Python-Umgebung konfigurieren

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

### 3. VS Code-Integration testen

1. **Projekt in VS Code öffnen**:
   ```bash
   code .
   ```

2. **AI Chat öffnen**:
   - Drücken Sie `Strg+Shift+P` (Windows/Linux) oder `Cmd+Shift+P` (macOS)
   - Geben Sie "AI Chat" ein und wählen Sie "AI Chat: Open Chat"

3. **MCP-Server-Verbindung testen**:
   - Geben Sie im AI Chat `#zava` ein und wählen Sie einen der konfigurierten Server aus
   - Fragen Sie: "Welche Tabellen sind in der Datenbank verfügbar?"
   - Sie sollten eine Antwort mit einer Liste der Einzelhandelsdatenbanktabellen erhalten

## ✅ Validierung der Umgebung

### 1. Umfassender Systemcheck

Führen Sie dieses Validierungsskript aus, um Ihre Einrichtung zu überprüfen:

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

### 2. Manuelle Validierungs-Checkliste

**✅ Grundlegende Tools**
- [ ] Docker Version 20.10+ installiert und läuft
- [ ] Azure CLI 2.40+ installiert und authentifiziert
- [ ] Python 3.8+ mit pip installiert
- [ ] Git 2.30+ installiert
- [ ] VS Code mit den erforderlichen Erweiterungen

**✅ Azure-Ressourcen**
- [ ] Ressourcengruppe erfolgreich erstellt
- [ ] AI Foundry-Projekt bereitgestellt
- [ ] OpenAI-Modell text-embedding-3-small bereitgestellt
- [ ] Application Insights konfiguriert
- [ ] Dienstprinzipal mit den richtigen Berechtigungen erstellt

**✅ Umgebungskonfiguration**
- [ ] `.env`-Datei mit allen erforderlichen Variablen erstellt
- [ ] Azure-Anmeldeinformationen funktionieren (Test mit `az account show`)
- [ ] PostgreSQL-Container läuft und ist zugänglich
- [ ] Beispieldaten in der Datenbank geladen

**✅ VS Code-Integration**
- [ ] `.vscode/mcp.json` konfiguriert
- [ ] Python-Interpreter auf virtuelle Umgebung eingestellt
- [ ] MCP-Server erscheinen im AI Chat
- [ ] Testabfragen können über AI Chat ausgeführt werden

## 🛠️ Häufige Probleme beheben

### Docker-Probleme

**Problem**: Docker-Container starten nicht
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

**Problem**: PostgreSQL-Verbindung schlägt fehl
```bash
# Check container logs
docker-compose logs postgres

# Verify container is healthy
docker-compose ps

# Test direct connection
docker-compose exec postgres psql -U postgres -d zava -c "SELECT 1;"
```

### Azure-Bereitstellungsprobleme

**Problem**: Azure-Bereitstellung schlägt fehl
```bash
# Check Azure CLI authentication
az account show

# Verify subscription permissions
az role assignment list --assignee $(az account show --query user.name -o tsv)

# Check resource provider registration
az provider register --namespace Microsoft.CognitiveServices
az provider register --namespace Microsoft.Insights
```

**Problem**: KI-Dienst-Authentifizierung schlägt fehl
```bash
# Test service principal
az login --service-principal \
  --username $AZURE_CLIENT_ID \
  --password $AZURE_CLIENT_SECRET \
  --tenant $AZURE_TENANT_ID

# Verify AI service deployment
az cognitiveservices account list --query "[].{Name:name,Kind:kind,Location:location}"
```

### Python-Umgebungsprobleme

**Problem**: Paketinstallation schlägt fehl
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

**Problem**: VS Code findet den Python-Interpreter nicht
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

## 🎯 Wichtige Erkenntnisse

Nach Abschluss dieses Workshops sollten Sie Folgendes erreicht haben:

✅ **Komplette Entwicklungsumgebung**: Alle Tools installiert und konfiguriert  
✅ **Azure-Ressourcen bereitgestellt**: KI-Dienste und unterstützende Infrastruktur  
✅ **Docker-Umgebung läuft**: PostgreSQL- und MCP-Server-Container  
✅ **VS Code-Integration**: MCP-Server konfiguriert und zugänglich  
✅ **Validierte Einrichtung**: Alle Komponenten getestet und funktionieren zusammen  
✅ **Wissen zur Fehlerbehebung**: Häufige Probleme und Lösungen  

## 🚀 Was kommt als Nächstes

Mit Ihrer eingerichteten Umgebung können Sie mit **[Lab 04: Datenbankdesign und Schema](../04-Database/README.md)** fortfahren, um:

- Das Einzelhandelsdatenbankschema im Detail zu erkunden
- Multi-Tenant-Datenmodellierung zu verstehen
- Die Implementierung von Row Level Security zu lernen
- Mit Beispieldaten aus dem Einzelhandel zu arbeiten

## 📚 Zusätzliche Ressourcen

### Entwicklungstools
- [Docker-Dokumentation](https://docs.docker.com/) - Vollständige Docker-Referenz
- [Azure CLI-Referenz](https://docs.microsoft.com/cli/azure/) - Azure CLI-Befehle
- [VS Code-Dokumentation](https://code.visualstudio.com/docs) - Editor-Konfiguration und Erweiterungen

### Azure-Dienste
- [Azure AI Foundry-Dokumentation](https://docs.microsoft.com/azure/ai-foundry/) - KI-Dienstkonfiguration
- [Azure OpenAI-Dienst](https://docs.microsoft.com/azure/cognitive-services/openai/) - KI-Modellbereitstellung
- [Application Insights](https://docs.microsoft.com/azure/azure-monitor/app/app-insights-overview) - Überwachungssetup

### Python-Entwicklung
- [Python-Virtuelle Umgebungen](https://docs.python.org/3/tutorial/venv.html) - Umgebungsmanagement
- [AsyncIO-Dokumentation](https://docs.python.org/3/library/asyncio.html) - Asynchrone Programmiermuster
- [FastAPI-Dokumentation](https://fastapi.tiangolo.com/) - Web-Framework-Muster

---

**Weiter**: Umgebung bereit? Fahren Sie fort mit [Lab 04: Datenbankdesign und Schema](../04-Database/README.md)

---

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die sich aus der Nutzung dieser Übersetzung ergeben.