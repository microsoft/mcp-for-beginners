# Configurarea Mediului

## 🎯 Ce Acoperă Acest Laborator

Acest laborator practic te ghidează prin configurarea unui mediu complet de dezvoltare pentru construirea serverelor MCP cu integrare PostgreSQL. Vei configura toate instrumentele necesare, vei implementa resurse Azure și vei valida configurarea înainte de a trece la implementare.

## Prezentare Generală

Un mediu de dezvoltare adecvat este esențial pentru dezvoltarea cu succes a serverelor MCP. Acest laborator oferă instrucțiuni pas cu pas pentru configurarea Docker, serviciilor Azure, instrumentelor de dezvoltare și validarea funcționării corecte a tuturor componentelor.

La finalul acestui laborator, vei avea un mediu de dezvoltare complet funcțional, pregătit pentru construirea serverului MCP Zava Retail.

## Obiective de Învățare

La finalul acestui laborator, vei putea:

- **Instala și configura** toate instrumentele de dezvoltare necesare
- **Implementa resurse Azure** necesare pentru serverul MCP
- **Configura containere Docker** pentru PostgreSQL și serverul MCP
- **Valida** configurarea mediului cu conexiuni de test
- **Depana** probleme comune de configurare
- **Înțelege** fluxul de lucru de dezvoltare și structura fișierelor

## 📋 Verificarea Prerechizitelor

Înainte de a începe, asigură-te că ai:

### Cunoștințe Necesare
- Utilizarea de bază a liniei de comandă (Windows Command Prompt/PowerShell)
- Înțelegerea variabilelor de mediu
- Familiaritate cu controlul versiunilor Git
- Concepte de bază Docker (containere, imagini, volume)

### Cerințe de Sistem
- **Sistem de Operare**: Windows 10/11, macOS sau Linux
- **RAM**: Minimum 8GB (recomandat 16GB)
- **Spațiu de Stocare**: Cel puțin 10GB liberi
- **Rețea**: Conexiune la internet pentru descărcări și implementare Azure

### Cerințe de Cont
- **Abonament Azure**: Nivel gratuit este suficient
- **Cont GitHub**: Pentru acces la depozite
- **Cont Docker Hub**: (Opțional) Pentru publicarea imaginilor personalizate

## 🛠️ Instalarea Instrumentelor

### 1. Instalarea Docker Desktop

Docker oferă mediul containerizat pentru configurarea noastră de dezvoltare.

#### Instalare pe Windows

1. **Descarcă Docker Desktop**:
   ```cmd
   # Visit https://desktop.docker.com/win/stable/Docker%20Desktop%20Installer.exe
   # Or use Windows Package Manager
   winget install Docker.DockerDesktop
   ```

2. **Instalează și Configurează**:
   - Rulează instalatorul ca Administrator
   - Activează integrarea WSL 2 când ți se solicită
   - Repornește computerul după finalizarea instalării

3. **Verifică Instalarea**:
   ```cmd
   docker --version
   docker-compose --version
   ```

#### Instalare pe macOS

1. **Descarcă și Instalează**:
   ```bash
   # Download from https://desktop.docker.com/mac/stable/Docker.dmg
   # Or use Homebrew
   brew install --cask docker
   ```

2. **Pornește Docker Desktop**:
   - Lansează Docker Desktop din Aplicații
   - Completează asistentul de configurare inițial

3. **Verifică Instalarea**:
   ```bash
   docker --version
   docker-compose --version
   ```

#### Instalare pe Linux

1. **Instalează Docker Engine**:
   ```bash
   # Ubuntu/Debian
   curl -fsSL https://get.docker.com -o get-docker.sh
   sudo sh get-docker.sh
   sudo usermod -aG docker $USER
   
   # Log out and back in for group changes to take effect
   ```

2. **Instalează Docker Compose**:
   ```bash
   sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
   sudo chmod +x /usr/local/bin/docker-compose
   ```

### 2. Instalarea Azure CLI

Azure CLI permite implementarea și gestionarea resurselor Azure.

#### Instalare pe Windows

```cmd
# Using Windows Package Manager
winget install Microsoft.AzureCLI

# Or download MSI from: https://aka.ms/installazurecliwindows
```

#### Instalare pe macOS

```bash
# Using Homebrew
brew install azure-cli

# Or using installer
curl -L https://aka.ms/InstallAzureCli | bash
```

#### Instalare pe Linux

```bash
# Ubuntu/Debian
curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash

# RHEL/CentOS
sudo rpm --import https://packages.microsoft.com/keys/microsoft.asc
sudo dnf install azure-cli
```

#### Verificare și Autentificare

```bash
# Check installation
az version

# Login to Azure
az login

# Set default subscription (if you have multiple)
az account list --output table
az account set --subscription "Your-Subscription-Name"
```

### 3. Instalarea Git

Git este necesar pentru clonarea depozitului și controlul versiunilor.

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

### 4. Instalarea VS Code

Visual Studio Code oferă mediul integrat de dezvoltare cu suport MCP.

#### Instalare

```cmd
# Windows
winget install Microsoft.VisualStudioCode

# macOS
brew install --cask visual-studio-code

# Linux (Ubuntu/Debian)
sudo snap install code --classic
```

#### Extensii Necesare

Instalează aceste extensii VS Code:

```bash
# Install via command line
code --install-extension ms-python.python
code --install-extension ms-vscode.vscode-json
code --install-extension ms-azuretools.vscode-docker
code --install-extension ms-vscode.azure-account
```

Sau instalează prin VS Code:
1. Deschide VS Code
2. Accesează Extensii (Ctrl+Shift+X)
3. Instalează:
   - **Python** (Microsoft)
   - **Docker** (Microsoft)
   - **Azure Account** (Microsoft)
   - **JSON** (Microsoft)

### 5. Instalarea Python

Python 3.8+ este necesar pentru dezvoltarea serverului MCP.

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

#### Verifică Instalarea

```bash
python --version  # Should show Python 3.11.x
pip --version      # Should show pip version
```

## 🚀 Configurarea Proiectului

### 1. Clonează Depozitul

```bash
# Clone the main repository
git clone https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail.git

# Navigate to the project directory
cd MCP-Server-and-PostgreSQL-Sample-Retail

# Verify repository structure
ls -la
```

### 2. Creează un Mediu Virtual Python

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

### 3. Instalează Dependențele Python

```bash
# Install development dependencies
pip install -r requirements.lock.txt

# Verify key packages
pip list | grep fastmcp
pip list | grep asyncpg
pip list | grep azure
```

## ☁️ Implementarea Resurselor Azure

### 1. Înțelegerea Cerințelor de Resurse

Serverul nostru MCP necesită aceste resurse Azure:

| **Resursă** | **Scop** | **Cost Estimat** |
|-------------|----------|------------------|
| **Azure AI Foundry** | Găzduirea și gestionarea modelelor AI | $10-50/lună |
| **Implementare OpenAI** | Model de încorporare text (text-embedding-3-small) | $5-20/lună |
| **Application Insights** | Monitorizare și telemetrie | $5-15/lună |
| **Grup de Resurse** | Organizarea resurselor | Gratuit |

### 2. Implementarea Resurselor Azure

#### Opțiunea A: Implementare Automată (Recomandată)

```bash
# Navigate to infrastructure directory
cd infra

# Windows - PowerShell
./deploy.ps1

# macOS/Linux - Bash
./deploy.sh
```

Scriptul de implementare va:
1. Crea un grup de resurse unic
2. Implementa resursele Azure AI Foundry
3. Implementa modelul text-embedding-3-small
4. Configura Application Insights
5. Crea un principal de serviciu pentru autentificare
6. Genera fișierul `.env` cu configurația

#### Opțiunea B: Implementare Manuală

Dacă preferi control manual sau scriptul automat eșuează:

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

### 3. Verifică Implementarea Azure

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

### 4. Configurează Variabilele de Mediu

După implementare, ar trebui să ai un fișier `.env`. Verifică dacă conține:

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

## 🐳 Configurarea Mediului Docker

### 1. Înțelegerea Compoziției Docker

Mediul nostru de dezvoltare folosește Docker Compose:

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

### 2. Pornește Mediul de Dezvoltare

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

### 3. Verifică Configurarea Bazei de Date

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

### 4. Testează Serverul MCP

```bash
# Check MCP server health
curl http://localhost:8000/health

# Test basic MCP endpoint
curl -X POST http://localhost:8000/mcp \
  -H "Content-Type: application/json" \
  -H "x-rls-user-id: 00000000-0000-0000-0000-000000000000" \
  -d '{"method": "tools/list", "params": {}}'
```

## 🔧 Configurarea VS Code

### 1. Configurează Integrarea MCP

Creează configurația MCP pentru VS Code:

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

### 2. Configurează Mediul Python

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

### 3. Testează Integrarea VS Code

1. **Deschide proiectul în VS Code**:
   ```bash
   code .
   ```

2. **Deschide AI Chat**:
   - Apasă `Ctrl+Shift+P` (Windows/Linux) sau `Cmd+Shift+P` (macOS)
   - Tastează "AI Chat" și selectează "AI Chat: Open Chat"

3. **Testează Conexiunea Serverului MCP**:
   - În AI Chat, tastează `#zava` și selectează unul dintre serverele configurate
   - Întreabă: "Ce tabele sunt disponibile în baza de date?"
   - Ar trebui să primești un răspuns cu lista tabelelor din baza de date retail

## ✅ Validarea Mediului

### 1. Verificare Completă a Sistemului

Rulează acest script de validare pentru a verifica configurarea:

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

### 2. Lista de Verificare Manuală

**✅ Instrumente de Bază**
- [ ] Docker versiunea 20.10+ instalat și funcțional
- [ ] Azure CLI 2.40+ instalat și autentificat
- [ ] Python 3.8+ cu pip instalat
- [ ] Git 2.30+ instalat
- [ ] VS Code cu extensiile necesare

**✅ Resurse Azure**
- [ ] Grup de resurse creat cu succes
- [ ] Proiect AI Foundry implementat
- [ ] Modelul OpenAI text-embedding-3-small implementat
- [ ] Application Insights configurat
- [ ] Principal de serviciu creat cu permisiuni adecvate

**✅ Configurarea Mediului**
- [ ] Fișier `.env` creat cu toate variabilele necesare
- [ ] Credențiale Azure funcționale (testează cu `az account show`)
- [ ] Container PostgreSQL funcțional și accesibil
- [ ] Date de exemplu încărcate în baza de date

**✅ Integrarea VS Code**
- [ ] `.vscode/mcp.json` configurat
- [ ] Interpretul Python setat la mediul virtual
- [ ] Serverele MCP apar în AI Chat
- [ ] Pot executa interogări de test prin AI Chat

## 🛠️ Depanarea Problemelor Comune

### Probleme Docker

**Problemă**: Containerele Docker nu pornesc
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

**Problemă**: Conexiunea PostgreSQL eșuează
```bash
# Check container logs
docker-compose logs postgres

# Verify container is healthy
docker-compose ps

# Test direct connection
docker-compose exec postgres psql -U postgres -d zava -c "SELECT 1;"
```

### Probleme de Implementare Azure

**Problemă**: Implementarea Azure eșuează
```bash
# Check Azure CLI authentication
az account show

# Verify subscription permissions
az role assignment list --assignee $(az account show --query user.name -o tsv)

# Check resource provider registration
az provider register --namespace Microsoft.CognitiveServices
az provider register --namespace Microsoft.Insights
```

**Problemă**: Autentificarea serviciului AI eșuează
```bash
# Test service principal
az login --service-principal \
  --username $AZURE_CLIENT_ID \
  --password $AZURE_CLIENT_SECRET \
  --tenant $AZURE_TENANT_ID

# Verify AI service deployment
az cognitiveservices account list --query "[].{Name:name,Kind:kind,Location:location}"
```

### Probleme de Mediu Python

**Problemă**: Instalarea pachetelor eșuează
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

**Problemă**: VS Code nu găsește interpretul Python
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

## 🎯 Concluzii Cheie

După finalizarea acestui laborator, ar trebui să ai:

✅ **Mediu de Dezvoltare Complet**: Toate instrumentele instalate și configurate  
✅ **Resurse Azure Implementate**: Servicii AI și infrastructura suport  
✅ **Mediu Docker Funcțional**: Containere PostgreSQL și server MCP  
✅ **Integrare VS Code**: Serverele MCP configurate și accesibile  
✅ **Configurare Validată**: Toate componentele testate și funcționale împreună  
✅ **Cunoștințe de Depanare**: Probleme comune și soluții  

## 🚀 Ce Urmează

Cu mediul configurat, continuă cu **[Lab 04: Designul și Schema Bazei de Date](../04-Database/README.md)** pentru:

- Explorarea detaliată a schemei bazei de date retail
- Înțelegerea modelării datelor multi-chiriaș
- Implementarea securității la nivel de rând
- Lucrul cu date de exemplu din retail

## 📚 Resurse Suplimentare

### Instrumente de Dezvoltare
- [Documentația Docker](https://docs.docker.com/) - Referință completă Docker
- [Referința Azure CLI](https://docs.microsoft.com/cli/azure/) - Comenzi Azure CLI
- [Documentația VS Code](https://code.visualstudio.com/docs) - Configurarea editorului și extensiilor

### Servicii Azure
- [Documentația Azure AI Foundry](https://docs.microsoft.com/azure/ai-foundry/) - Configurarea serviciilor AI
- [Serviciul Azure OpenAI](https://docs.microsoft.com/azure/cognitive-services/openai/) - Implementarea modelelor AI
- [Application Insights](https://docs.microsoft.com/azure/azure-monitor/app/app-insights-overview) - Configurarea monitorizării

### Dezvoltare Python
- [Mediile Virtuale Python](https://docs.python.org/3/tutorial/venv.html) - Gestionarea mediilor
- [Documentația AsyncIO](https://docs.python.org/3/library/asyncio.html) - Modele de programare asincronă
- [Documentația FastAPI](https://fastapi.tiangolo.com/) - Modele de framework web

---

**Următorul Pas**: Mediul este gata? Continuă cu [Lab 04: Designul și Schema Bazei de Date](../04-Database/README.md)

---

**Declinare de responsabilitate**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim să asigurăm acuratețea, vă rugăm să fiți conștienți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa maternă ar trebui considerat sursa autoritară. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care pot apărea din utilizarea acestei traduceri.