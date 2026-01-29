# Ρύθμιση Περιβάλλοντος

## 🎯 Τι Καλύπτει Αυτό το Εργαστήριο

Αυτό το πρακτικό εργαστήριο σας καθοδηγεί στη ρύθμιση ενός πλήρους περιβάλλοντος ανάπτυξης για τη δημιουργία MCP servers με ενσωμάτωση PostgreSQL. Θα ρυθμίσετε όλα τα απαραίτητα εργαλεία, θα αναπτύξετε πόρους Azure και θα επικυρώσετε τη ρύθμιση πριν προχωρήσετε στην υλοποίηση.

## Επισκόπηση

Ένα σωστά διαμορφωμένο περιβάλλον ανάπτυξης είναι κρίσιμο για την επιτυχή ανάπτυξη MCP servers. Αυτό το εργαστήριο παρέχει βήμα προς βήμα οδηγίες για τη ρύθμιση του Docker, των υπηρεσιών Azure, των εργαλείων ανάπτυξης και την επικύρωση ότι όλα λειτουργούν σωστά μαζί.

Μέχρι το τέλος αυτού του εργαστηρίου, θα έχετε ένα πλήρως λειτουργικό περιβάλλον ανάπτυξης έτοιμο για τη δημιουργία του MCP server της Zava Retail.

## Στόχοι Μάθησης

Μέχρι το τέλος αυτού του εργαστηρίου, θα μπορείτε να:

- **Εγκαταστήσετε και διαμορφώσετε** όλα τα απαραίτητα εργαλεία ανάπτυξης
- **Αναπτύξετε πόρους Azure** που απαιτούνται για τον MCP server
- **Ρυθμίσετε Docker containers** για PostgreSQL και τον MCP server
- **Επικυρώσετε** τη ρύθμιση του περιβάλλοντος με δοκιμαστικές συνδέσεις
- **Αντιμετωπίσετε προβλήματα** κοινών ζητημάτων ρύθμισης και διαμόρφωσης
- **Κατανοήσετε** τη ροή εργασίας ανάπτυξης και τη δομή αρχείων

## 📋 Έλεγχος Προαπαιτούμενων

Πριν ξεκινήσετε, βεβαιωθείτε ότι έχετε:

### Απαιτούμενες Γνώσεις
- Βασική χρήση γραμμής εντολών (Windows Command Prompt/PowerShell)
- Κατανόηση μεταβλητών περιβάλλοντος
- Εξοικείωση με τον έλεγχο έκδοσης Git
- Βασικές έννοιες Docker (containers, images, volumes)

### Απαιτήσεις Συστήματος
- **Λειτουργικό Σύστημα**: Windows 10/11, macOS ή Linux
- **RAM**: Ελάχιστο 8GB (συνιστάται 16GB)
- **Αποθηκευτικός Χώρος**: Τουλάχιστον 10GB ελεύθερος χώρος
- **Δίκτυο**: Σύνδεση στο Internet για λήψεις και ανάπτυξη Azure

### Απαιτήσεις Λογαριασμού
- **Συνδρομή Azure**: Αρκεί το δωρεάν επίπεδο
- **Λογαριασμός GitHub**: Για πρόσβαση στο αποθετήριο
- **Λογαριασμός Docker Hub**: (Προαιρετικό) Για δημοσίευση προσαρμοσμένων εικόνων

## 🛠️ Εγκατάσταση Εργαλείων

### 1. Εγκατάσταση Docker Desktop

Το Docker παρέχει το περιβάλλον container για τη ρύθμιση ανάπτυξης.

#### Εγκατάσταση σε Windows

1. **Λήψη Docker Desktop**:
   ```cmd
   # Visit https://desktop.docker.com/win/stable/Docker%20Desktop%20Installer.exe
   # Or use Windows Package Manager
   winget install Docker.DockerDesktop
   ```

2. **Εγκατάσταση και Διαμόρφωση**:
   - Εκτελέστε τον εγκαταστάτη ως Διαχειριστής
   - Ενεργοποιήστε την ενσωμάτωση WSL 2 όταν σας ζητηθεί
   - Επανεκκινήστε τον υπολογιστή σας όταν ολοκληρωθεί η εγκατάσταση

3. **Επικύρωση Εγκατάστασης**:
   ```cmd
   docker --version
   docker-compose --version
   ```

#### Εγκατάσταση σε macOS

1. **Λήψη και Εγκατάσταση**:
   ```bash
   # Download from https://desktop.docker.com/mac/stable/Docker.dmg
   # Or use Homebrew
   brew install --cask docker
   ```

2. **Εκκίνηση Docker Desktop**:
   - Εκκινήστε το Docker Desktop από τις Εφαρμογές
   - Ολοκληρώστε τον αρχικό οδηγό ρύθμισης

3. **Επικύρωση Εγκατάστασης**:
   ```bash
   docker --version
   docker-compose --version
   ```

#### Εγκατάσταση σε Linux

1. **Εγκατάσταση Docker Engine**:
   ```bash
   # Ubuntu/Debian
   curl -fsSL https://get.docker.com -o get-docker.sh
   sudo sh get-docker.sh
   sudo usermod -aG docker $USER
   
   # Log out and back in for group changes to take effect
   ```

2. **Εγκατάσταση Docker Compose**:
   ```bash
   sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
   sudo chmod +x /usr/local/bin/docker-compose
   ```

### 2. Εγκατάσταση Azure CLI

Το Azure CLI επιτρέπει την ανάπτυξη και διαχείριση πόρων Azure.

#### Εγκατάσταση σε Windows

```cmd
# Using Windows Package Manager
winget install Microsoft.AzureCLI

# Or download MSI from: https://aka.ms/installazurecliwindows
```

#### Εγκατάσταση σε macOS

```bash
# Using Homebrew
brew install azure-cli

# Or using installer
curl -L https://aka.ms/InstallAzureCli | bash
```

#### Εγκατάσταση σε Linux

```bash
# Ubuntu/Debian
curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash

# RHEL/CentOS
sudo rpm --import https://packages.microsoft.com/keys/microsoft.asc
sudo dnf install azure-cli
```

#### Επικύρωση και Αυθεντικοποίηση

```bash
# Check installation
az version

# Login to Azure
az login

# Set default subscription (if you have multiple)
az account list --output table
az account set --subscription "Your-Subscription-Name"
```

### 3. Εγκατάσταση Git

Το Git απαιτείται για την κλωνοποίηση του αποθετηρίου και τον έλεγχο έκδοσης.

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

### 4. Εγκατάσταση VS Code

Το Visual Studio Code παρέχει το ολοκληρωμένο περιβάλλον ανάπτυξης με υποστήριξη MCP.

#### Εγκατάσταση

```cmd
# Windows
winget install Microsoft.VisualStudioCode

# macOS
brew install --cask visual-studio-code

# Linux (Ubuntu/Debian)
sudo snap install code --classic
```

#### Απαιτούμενες Επεκτάσεις

Εγκαταστήστε αυτές τις επεκτάσεις VS Code:

```bash
# Install via command line
code --install-extension ms-python.python
code --install-extension ms-vscode.vscode-json
code --install-extension ms-azuretools.vscode-docker
code --install-extension ms-vscode.azure-account
```

Ή εγκαταστήστε μέσω VS Code:
1. Ανοίξτε το VS Code
2. Μεταβείτε στις Επεκτάσεις (Ctrl+Shift+X)
3. Εγκαταστήστε:
   - **Python** (Microsoft)
   - **Docker** (Microsoft)
   - **Azure Account** (Microsoft)
   - **JSON** (Microsoft)

### 5. Εγκατάσταση Python

Απαιτείται Python 3.8+ για την ανάπτυξη MCP server.

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

#### Επικύρωση Εγκατάστασης

```bash
python --version  # Should show Python 3.11.x
pip --version      # Should show pip version
```

## 🚀 Ρύθμιση Έργου

### 1. Κλωνοποίηση Αποθετηρίου

```bash
# Clone the main repository
git clone https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail.git

# Navigate to the project directory
cd MCP-Server-and-PostgreSQL-Sample-Retail

# Verify repository structure
ls -la
```

### 2. Δημιουργία Εικονικού Περιβάλλοντος Python

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

### 3. Εγκατάσταση Εξαρτήσεων Python

```bash
# Install development dependencies
pip install -r requirements.lock.txt

# Verify key packages
pip list | grep fastmcp
pip list | grep asyncpg
pip list | grep azure
```

## ☁️ Ανάπτυξη Πόρων Azure

### 1. Κατανόηση Απαιτήσεων Πόρων

Ο MCP server μας απαιτεί τους εξής πόρους Azure:

| **Πόρος** | **Σκοπός** | **Εκτιμώμενο Κόστος** |
|-----------|------------|-----------------------|
| **Azure AI Foundry** | Φιλοξενία και διαχείριση AI μοντέλων | $10-50/μήνα |
| **OpenAI Deployment** | Μοντέλο ενσωμάτωσης κειμένου (text-embedding-3-small) | $5-20/μήνα |
| **Application Insights** | Παρακολούθηση και τηλεμετρία | $5-15/μήνα |
| **Resource Group** | Οργάνωση πόρων | Δωρεάν |

### 2. Ανάπτυξη Πόρων Azure

#### Επιλογή Α: Αυτοματοποιημένη Ανάπτυξη (Συνιστάται)

```bash
# Navigate to infrastructure directory
cd infra

# Windows - PowerShell
./deploy.ps1

# macOS/Linux - Bash
./deploy.sh
```

Το σενάριο ανάπτυξης θα:
1. Δημιουργήσει μια μοναδική ομάδα πόρων
2. Αναπτύξει πόρους Azure AI Foundry
3. Αναπτύξει το μοντέλο text-embedding-3-small
4. Διαμορφώσει το Application Insights
5. Δημιουργήσει έναν service principal για αυθεντικοποίηση
6. Δημιουργήσει αρχείο `.env` με τη διαμόρφωση

#### Επιλογή Β: Χειροκίνητη Ανάπτυξη

Αν προτιμάτε χειροκίνητο έλεγχο ή αποτύχει το αυτοματοποιημένο σενάριο:

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

### 3. Επικύρωση Ανάπτυξης Azure

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

### 4. Διαμόρφωση Μεταβλητών Περιβάλλοντος

Μετά την ανάπτυξη, θα πρέπει να έχετε ένα αρχείο `.env`. Επικυρώστε ότι περιέχει:

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

## 🐳 Ρύθμιση Περιβάλλοντος Docker

### 1. Κατανόηση Σύνθεσης Docker

Το περιβάλλον ανάπτυξης μας χρησιμοποιεί Docker Compose:

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

### 2. Εκκίνηση Περιβάλλοντος Ανάπτυξης

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

### 3. Επικύρωση Ρύθμισης Βάσης Δεδομένων

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

### 4. Δοκιμή MCP Server

```bash
# Check MCP server health
curl http://localhost:8000/health

# Test basic MCP endpoint
curl -X POST http://localhost:8000/mcp \
  -H "Content-Type: application/json" \
  -H "x-rls-user-id: 00000000-0000-0000-0000-000000000000" \
  -d '{"method": "tools/list", "params": {}}'
```

## 🔧 Διαμόρφωση VS Code

### 1. Διαμόρφωση Ενσωμάτωσης MCP

Δημιουργήστε διαμόρφωση MCP στο VS Code:

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

### 2. Διαμόρφωση Περιβάλλοντος Python

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

### 3. Δοκιμή Ενσωμάτωσης VS Code

1. **Ανοίξτε το έργο στο VS Code**:
   ```bash
   code .
   ```

2. **Ανοίξτε το AI Chat**:
   - Πατήστε `Ctrl+Shift+P` (Windows/Linux) ή `Cmd+Shift+P` (macOS)
   - Πληκτρολογήστε "AI Chat" και επιλέξτε "AI Chat: Open Chat"

3. **Δοκιμή Σύνδεσης MCP Server**:
   - Στο AI Chat, πληκτρολογήστε `#zava` και επιλέξτε έναν από τους διαμορφωμένους servers
   - Ρωτήστε: "Ποιοι πίνακες είναι διαθέσιμοι στη βάση δεδομένων;"
   - Θα πρέπει να λάβετε απάντηση με λίστα των πινάκων της βάσης δεδομένων λιανικής

## ✅ Επικύρωση Περιβάλλοντος

### 1. Ολοκληρωμένος Έλεγχος Συστήματος

Εκτελέστε αυτό το σενάριο επικύρωσης για να επαληθεύσετε τη ρύθμιση σας:

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

### 2. Χειροκίνητη Λίστα Ελέγχου Επικύρωσης

**✅ Βασικά Εργαλεία**
- [ ] Εγκατεστημένη και λειτουργική έκδοση Docker 20.10+
- [ ] Εγκατεστημένο και αυθεντικοποιημένο Azure CLI 2.40+
- [ ] Εγκατεστημένο Python 3.8+ με pip
- [ ] Εγκατεστημένο Git 2.30+
- [ ] VS Code με τις απαιτούμενες επεκτάσεις

**✅ Πόροι Azure**
- [ ] Δημιουργήθηκε επιτυχώς ομάδα πόρων
- [ ] Αναπτύχθηκε έργο AI Foundry
- [ ] Αναπτύχθηκε μοντέλο text-embedding-3-small
- [ ] Διαμορφώθηκε Application Insights
- [ ] Δημιουργήθηκε service principal με σωστές άδειες

**✅ Διαμόρφωση Περιβάλλοντος**
- [ ] Δημιουργήθηκε αρχείο `.env` με όλες τις απαιτούμενες μεταβλητές
- [ ] Λειτουργούν τα διαπιστευτήρια Azure (δοκιμή με `az account show`)
- [ ] Λειτουργεί και είναι προσβάσιμο το container PostgreSQL
- [ ] Φορτώθηκαν δείγματα δεδομένων στη βάση δεδομένων

**✅ Ενσωμάτωση VS Code**
- [ ] Διαμορφώθηκε το `.vscode/mcp.json`
- [ ] Ο διερμηνέας Python έχει οριστεί στο εικονικό περιβάλλον
- [ ] Εμφανίζονται οι MCP servers στο AI Chat
- [ ] Μπορούν να εκτελεστούν δοκιμαστικά ερωτήματα μέσω AI Chat

## 🛠️ Αντιμετώπιση Κοινών Προβλημάτων

### Προβλήματα Docker

**Πρόβλημα**: Τα containers Docker δεν ξεκινούν
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

**Πρόβλημα**: Αποτυγχάνει η σύνδεση PostgreSQL
```bash
# Check container logs
docker-compose logs postgres

# Verify container is healthy
docker-compose ps

# Test direct connection
docker-compose exec postgres psql -U postgres -d zava -c "SELECT 1;"
```

### Προβλήματα Ανάπτυξης Azure

**Πρόβλημα**: Αποτυγχάνει η ανάπτυξη Azure
```bash
# Check Azure CLI authentication
az account show

# Verify subscription permissions
az role assignment list --assignee $(az account show --query user.name -o tsv)

# Check resource provider registration
az provider register --namespace Microsoft.CognitiveServices
az provider register --namespace Microsoft.Insights
```

**Πρόβλημα**: Αποτυγχάνει η αυθεντικοποίηση υπηρεσίας AI
```bash
# Test service principal
az login --service-principal \
  --username $AZURE_CLIENT_ID \
  --password $AZURE_CLIENT_SECRET \
  --tenant $AZURE_TENANT_ID

# Verify AI service deployment
az cognitiveservices account list --query "[].{Name:name,Kind:kind,Location:location}"
```

### Προβλήματα Περιβάλλοντος Python

**Πρόβλημα**: Αποτυγχάνει η εγκατάσταση πακέτων
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

**Πρόβλημα**: Το VS Code δεν βρίσκει τον διερμηνέα Python
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

## 🎯 Βασικά Συμπεράσματα

Μετά την ολοκλήρωση αυτού του εργαστηρίου, θα πρέπει να έχετε:

✅ **Πλήρες Περιβάλλον Ανάπτυξης**: Όλα τα εργαλεία εγκατεστημένα και διαμορφωμένα  
✅ **Αναπτυγμένους Πόρους Azure**: Υπηρεσίες AI και υποστηρικτική υποδομή  
✅ **Λειτουργικό Περιβάλλον Docker**: Containers PostgreSQL και MCP server  
✅ **Ενσωμάτωση VS Code**: Διαμορφωμένοι και προσβάσιμοι MCP servers  
✅ **Επικυρωμένη Ρύθμιση**: Όλα τα στοιχεία δοκιμασμένα και λειτουργικά μαζί  
✅ **Γνώση Αντιμετώπισης Προβλημάτων**: Κοινά ζητήματα και λύσεις  

## 🚀 Τι Ακολουθεί

Με το περιβάλλον σας έτοιμο, συνεχίστε στο **[Εργαστήριο 04: Σχεδιασμός Βάσης Δεδομένων και Σχήμα](../04-Database/README.md)** για να:

- Εξερευνήσετε το σχήμα της βάσης δεδομένων λιανικής
- Κατανοήσετε τη μοντελοποίηση δεδομένων πολλαπλών ενοικιαστών
- Μάθετε για την υλοποίηση Ασφάλειας σε Επίπεδο Γραμμής
- Εργαστείτε με δείγματα δεδομένων λιανικής

## 📚 Πρόσθετοι Πόροι

### Εργαλεία Ανάπτυξης
- [Τεκμηρίωση Docker](https://docs.docker.com/) - Πλήρης αναφορά Docker
- [Αναφορά Azure CLI](https://docs.microsoft.com/cli/azure/) - Εντολές Azure CLI
- [Τεκμηρίωση VS Code](https://code.visualstudio.com/docs) - Ρύθμιση επεξεργαστή και επεκτάσεις

### Υπηρεσίες Azure
- [Τεκμηρίωση Azure AI Foundry](https://docs.microsoft.com/azure/ai-foundry/) - Ρύθμιση υπηρεσίας AI
- [Υπηρεσία Azure OpenAI](https://docs.microsoft.com/azure/cognitive-services/openai/) - Ανάπτυξη AI μοντέλου
- [Application Insights](https://docs.microsoft.com/azure/azure-monitor/app/app-insights-overview) - Ρύθμιση παρακολούθησης

### Ανάπτυξη Python
- [Εικονικά Περιβάλλοντα Python](https://docs.python.org/3/tutorial/venv.html) - Διαχείριση περιβάλλοντος
- [Τεκμηρίωση AsyncIO](https://docs.python.org/3/library/asyncio.html) - Πρότυπα προγραμματισμού Async
- [Τεκμηρίωση FastAPI](https://fastapi.tiangolo.com/) - Πρότυπα πλαισίου web

---

**Επόμενο**: Το περιβάλλον είναι έτοιμο; Συνεχίστε με το [Εργαστήριο 04: Σχεδιασμός Βάσης Δεδομένων και Σχήμα](../04-Database/README.md)

---

**Αποποίηση ευθύνης**:  
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας την υπηρεσία αυτόματης μετάφρασης [Co-op Translator](https://github.com/Azure/co-op-translator). Παρόλο που καταβάλλουμε προσπάθειες για ακρίβεια, παρακαλούμε να έχετε υπόψη ότι οι αυτόματες μεταφράσεις ενδέχεται να περιέχουν σφάλματα ή ανακρίβειες. Το πρωτότυπο έγγραφο στη μητρική του γλώσσα θα πρέπει να θεωρείται η αυθεντική πηγή. Για κρίσιμες πληροφορίες, συνιστάται επαγγελματική ανθρώπινη μετάφραση. Δεν φέρουμε ευθύνη για τυχόν παρεξηγήσεις ή εσφαλμένες ερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.