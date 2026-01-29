# Configurazione dell'Ambiente

## 🎯 Cosa Copre Questo Laboratorio

Questo laboratorio pratico ti guida nella configurazione di un ambiente di sviluppo completo per la creazione di server MCP con integrazione PostgreSQL. Configurerai tutti gli strumenti necessari, distribuirai risorse Azure e validerai la configurazione prima di procedere con l'implementazione.

## Panoramica

Un ambiente di sviluppo adeguato è fondamentale per lo sviluppo di server MCP. Questo laboratorio fornisce istruzioni passo-passo per configurare Docker, i servizi Azure, gli strumenti di sviluppo e per verificare che tutto funzioni correttamente insieme.

Alla fine di questo laboratorio, avrai un ambiente di sviluppo completamente funzionante pronto per costruire il server MCP di Zava Retail.

## Obiettivi di Apprendimento

Alla fine di questo laboratorio, sarai in grado di:

- **Installare e configurare** tutti gli strumenti di sviluppo necessari
- **Distribuire risorse Azure** necessarie per il server MCP
- **Configurare container Docker** per PostgreSQL e il server MCP
- **Validare** la configurazione dell'ambiente con connessioni di test
- **Risolvere problemi comuni** di configurazione e setup
- **Comprendere** il flusso di lavoro di sviluppo e la struttura dei file

## 📋 Verifica dei Prerequisiti

Prima di iniziare, assicurati di avere:

### Conoscenze Necessarie
- Uso base della riga di comando (Prompt dei Comandi di Windows/PowerShell)
- Comprensione delle variabili d'ambiente
- Familiarità con il controllo di versione Git
- Concetti base di Docker (container, immagini, volumi)

### Requisiti di Sistema
- **Sistema Operativo**: Windows 10/11, macOS o Linux
- **RAM**: Minimo 8GB (16GB consigliati)
- **Spazio di Archiviazione**: Almeno 10GB di spazio libero
- **Rete**: Connessione Internet per download e distribuzione su Azure

### Requisiti Account
- **Abbonamento Azure**: Il livello gratuito è sufficiente
- **Account GitHub**: Per accedere al repository
- **Account Docker Hub**: (Opzionale) Per pubblicare immagini personalizzate

## 🛠️ Installazione degli Strumenti

### 1. Installare Docker Desktop

Docker fornisce l'ambiente containerizzato per la nostra configurazione di sviluppo.

#### Installazione su Windows

1. **Scarica Docker Desktop**:
   ```cmd
   # Visit https://desktop.docker.com/win/stable/Docker%20Desktop%20Installer.exe
   # Or use Windows Package Manager
   winget install Docker.DockerDesktop
   ```

2. **Installa e Configura**:
   - Esegui l'installer come Amministratore
   - Abilita l'integrazione con WSL 2 quando richiesto
   - Riavvia il computer al termine dell'installazione

3. **Verifica l'Installazione**:
   ```cmd
   docker --version
   docker-compose --version
   ```

#### Installazione su macOS

1. **Scarica e Installa**:
   ```bash
   # Download from https://desktop.docker.com/mac/stable/Docker.dmg
   # Or use Homebrew
   brew install --cask docker
   ```

2. **Avvia Docker Desktop**:
   - Avvia Docker Desktop da Applicazioni
   - Completa la configurazione iniziale

3. **Verifica l'Installazione**:
   ```bash
   docker --version
   docker-compose --version
   ```

#### Installazione su Linux

1. **Installa Docker Engine**:
   ```bash
   # Ubuntu/Debian
   curl -fsSL https://get.docker.com -o get-docker.sh
   sudo sh get-docker.sh
   sudo usermod -aG docker $USER
   
   # Log out and back in for group changes to take effect
   ```

2. **Installa Docker Compose**:
   ```bash
   sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
   sudo chmod +x /usr/local/bin/docker-compose
   ```

### 2. Installare Azure CLI

Azure CLI consente la distribuzione e la gestione delle risorse Azure.

#### Installazione su Windows

```cmd
# Using Windows Package Manager
winget install Microsoft.AzureCLI

# Or download MSI from: https://aka.ms/installazurecliwindows
```

#### Installazione su macOS

```bash
# Using Homebrew
brew install azure-cli

# Or using installer
curl -L https://aka.ms/InstallAzureCli | bash
```

#### Installazione su Linux

```bash
# Ubuntu/Debian
curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash

# RHEL/CentOS
sudo rpm --import https://packages.microsoft.com/keys/microsoft.asc
sudo dnf install azure-cli
```

#### Verifica e Autenticazione

```bash
# Check installation
az version

# Login to Azure
az login

# Set default subscription (if you have multiple)
az account list --output table
az account set --subscription "Your-Subscription-Name"
```

### 3. Installare Git

Git è necessario per clonare il repository e per il controllo di versione.

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

### 4. Installare VS Code

Visual Studio Code fornisce l'ambiente di sviluppo integrato con supporto MCP.

#### Installazione

```cmd
# Windows
winget install Microsoft.VisualStudioCode

# macOS
brew install --cask visual-studio-code

# Linux (Ubuntu/Debian)
sudo snap install code --classic
```

#### Estensioni Necessarie

Installa queste estensioni per VS Code:

```bash
# Install via command line
code --install-extension ms-python.python
code --install-extension ms-vscode.vscode-json
code --install-extension ms-azuretools.vscode-docker
code --install-extension ms-vscode.azure-account
```

Oppure installa tramite VS Code:
1. Apri VS Code
2. Vai su Estensioni (Ctrl+Shift+X)
3. Installa:
   - **Python** (Microsoft)
   - **Docker** (Microsoft)
   - **Azure Account** (Microsoft)
   - **JSON** (Microsoft)

### 5. Installare Python

Python 3.8+ è richiesto per lo sviluppo del server MCP.

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

#### Verifica dell'Installazione

```bash
python --version  # Should show Python 3.11.x
pip --version      # Should show pip version
```

## 🚀 Configurazione del Progetto

### 1. Clonare il Repository

```bash
# Clone the main repository
git clone https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail.git

# Navigate to the project directory
cd MCP-Server-and-PostgreSQL-Sample-Retail

# Verify repository structure
ls -la
```

### 2. Creare un Ambiente Virtuale Python

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

### 3. Installare le Dipendenze Python

```bash
# Install development dependencies
pip install -r requirements.lock.txt

# Verify key packages
pip list | grep fastmcp
pip list | grep asyncpg
pip list | grep azure
```

## ☁️ Distribuzione delle Risorse Azure

### 1. Comprendere i Requisiti delle Risorse

Il nostro server MCP richiede queste risorse Azure:

| **Risorsa** | **Scopo** | **Costo Stimato** |
|-------------|-----------|-------------------|
| **Azure AI Foundry** | Hosting e gestione dei modelli AI | $10-50/mese |
| **Distribuzione OpenAI** | Modello di embedding testuale (text-embedding-3-small) | $5-20/mese |
| **Application Insights** | Monitoraggio e telemetria | $5-15/mese |
| **Resource Group** | Organizzazione delle risorse | Gratuito |

### 2. Distribuire le Risorse Azure

#### Opzione A: Distribuzione Automatica (Consigliata)

```bash
# Navigate to infrastructure directory
cd infra

# Windows - PowerShell
./deploy.ps1

# macOS/Linux - Bash
./deploy.sh
```

Lo script di distribuzione:
1. Crea un gruppo di risorse unico
2. Distribuisce le risorse Azure AI Foundry
3. Distribuisce il modello text-embedding-3-small
4. Configura Application Insights
5. Crea un service principal per l'autenticazione
6. Genera un file `.env` con la configurazione

#### Opzione B: Distribuzione Manuale

Se preferisci il controllo manuale o lo script automatico fallisce:

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

### 3. Verifica della Distribuzione Azure

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

### 4. Configurare le Variabili d'Ambiente

Dopo la distribuzione, dovresti avere un file `.env`. Verifica che contenga:

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

## 🐳 Configurazione dell'Ambiente Docker

### 1. Comprendere la Composizione Docker

Il nostro ambiente di sviluppo utilizza Docker Compose:

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

### 2. Avviare l'Ambiente di Sviluppo

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

### 3. Verificare la Configurazione del Database

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

### 4. Testare il Server MCP

```bash
# Check MCP server health
curl http://localhost:8000/health

# Test basic MCP endpoint
curl -X POST http://localhost:8000/mcp \
  -H "Content-Type: application/json" \
  -H "x-rls-user-id: 00000000-0000-0000-0000-000000000000" \
  -d '{"method": "tools/list", "params": {}}'
```

## 🔧 Configurazione di VS Code

### 1. Configurare l'Integrazione MCP

Crea la configurazione MCP per VS Code:

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

### 2. Configurare l'Ambiente Python

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

### 3. Testare l'Integrazione con VS Code

1. **Apri il progetto in VS Code**:
   ```bash
   code .
   ```

2. **Apri AI Chat**:
   - Premi `Ctrl+Shift+P` (Windows/Linux) o `Cmd+Shift+P` (macOS)
   - Digita "AI Chat" e seleziona "AI Chat: Open Chat"

3. **Testa la Connessione al Server MCP**:
   - In AI Chat, digita `#zava` e seleziona uno dei server configurati
   - Chiedi: "Quali tabelle sono disponibili nel database?"
   - Dovresti ricevere una risposta con l'elenco delle tabelle del database retail

## ✅ Validazione dell'Ambiente

### 1. Controllo Completo del Sistema

Esegui questo script di validazione per verificare la configurazione:

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

### 2. Checklist di Validazione Manuale

**✅ Strumenti Base**
- [ ] Docker versione 20.10+ installato e in esecuzione
- [ ] Azure CLI 2.40+ installato e autenticato
- [ ] Python 3.8+ con pip installato
- [ ] Git 2.30+ installato
- [ ] VS Code con estensioni richieste

**✅ Risorse Azure**
- [ ] Gruppo di risorse creato con successo
- [ ] Progetto AI Foundry distribuito
- [ ] Modello OpenAI text-embedding-3-small distribuito
- [ ] Application Insights configurato
- [ ] Service principal creato con permessi adeguati

**✅ Configurazione dell'Ambiente**
- [ ] File `.env` creato con tutte le variabili richieste
- [ ] Credenziali Azure funzionanti (test con `az account show`)
- [ ] Container PostgreSQL in esecuzione e accessibile
- [ ] Dati di esempio caricati nel database

**✅ Integrazione con VS Code**
- [ ] File `.vscode/mcp.json` configurato
- [ ] Interprete Python impostato sull'ambiente virtuale
- [ ] Server MCP visibili in AI Chat
- [ ] Query di test eseguibili tramite AI Chat

## 🛠️ Risoluzione dei Problemi Comuni

### Problemi con Docker

**Problema**: I container Docker non si avviano
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

**Problema**: La connessione a PostgreSQL fallisce
```bash
# Check container logs
docker-compose logs postgres

# Verify container is healthy
docker-compose ps

# Test direct connection
docker-compose exec postgres psql -U postgres -d zava -c "SELECT 1;"
```

### Problemi con la Distribuzione Azure

**Problema**: La distribuzione Azure fallisce
```bash
# Check Azure CLI authentication
az account show

# Verify subscription permissions
az role assignment list --assignee $(az account show --query user.name -o tsv)

# Check resource provider registration
az provider register --namespace Microsoft.CognitiveServices
az provider register --namespace Microsoft.Insights
```

**Problema**: L'autenticazione al servizio AI fallisce
```bash
# Test service principal
az login --service-principal \
  --username $AZURE_CLIENT_ID \
  --password $AZURE_CLIENT_SECRET \
  --tenant $AZURE_TENANT_ID

# Verify AI service deployment
az cognitiveservices account list --query "[].{Name:name,Kind:kind,Location:location}"
```

### Problemi con l'Ambiente Python

**Problema**: L'installazione dei pacchetti fallisce
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

**Problema**: VS Code non trova l'interprete Python
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

## 🎯 Punti Chiave

Dopo aver completato questo laboratorio, dovresti avere:

✅ **Ambiente di Sviluppo Completo**: Tutti gli strumenti installati e configurati  
✅ **Risorse Azure Distribuite**: Servizi AI e infrastruttura di supporto  
✅ **Ambiente Docker Funzionante**: Container PostgreSQL e server MCP  
✅ **Integrazione con VS Code**: Server MCP configurati e accessibili  
✅ **Setup Validato**: Tutti i componenti testati e funzionanti insieme  
✅ **Conoscenze di Risoluzione Problemi**: Problemi comuni e soluzioni  

## 🚀 Prossimi Passi

Con l'ambiente pronto, continua con **[Lab 04: Progettazione e Schema del Database](../04-Database/README.md)** per:

- Esplorare in dettaglio lo schema del database retail
- Comprendere la modellazione dei dati multi-tenant
- Imparare l'implementazione della Sicurezza a Livello di Riga
- Lavorare con dati di esempio del retail

## 📚 Risorse Aggiuntive

### Strumenti di Sviluppo
- [Documentazione Docker](https://docs.docker.com/) - Riferimento completo su Docker
- [Riferimento Azure CLI](https://docs.microsoft.com/cli/azure/) - Comandi Azure CLI
- [Documentazione VS Code](https://code.visualstudio.com/docs) - Configurazione dell'editor e estensioni

### Servizi Azure
- [Documentazione Azure AI Foundry](https://docs.microsoft.com/azure/ai-foundry/) - Configurazione dei servizi AI
- [Servizio Azure OpenAI](https://docs.microsoft.com/azure/cognitive-services/openai/) - Distribuzione dei modelli AI
- [Application Insights](https://docs.microsoft.com/azure/azure-monitor/app/app-insights-overview) - Configurazione del monitoraggio

### Sviluppo Python
- [Ambienti Virtuali Python](https://docs.python.org/3/tutorial/venv.html) - Gestione degli ambienti
- [Documentazione AsyncIO](https://docs.python.org/3/library/asyncio.html) - Pattern di programmazione asincrona
- [Documentazione FastAPI](https://fastapi.tiangolo.com/) - Pattern del framework web

---

**Prossimo**: Ambiente pronto? Continua con [Lab 04: Progettazione e Schema del Database](../04-Database/README.md)

---

**Clausola di esclusione della responsabilità**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire l'accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa dovrebbe essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un esperto umano. Non siamo responsabili per eventuali incomprensioni o interpretazioni errate derivanti dall'uso di questa traduzione.