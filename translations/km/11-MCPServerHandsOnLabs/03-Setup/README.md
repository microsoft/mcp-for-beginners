# ការតំឡើងបរិយាកាស

## 🎯 អ្វីដែលមេរៀននេះគ្របដណ្តប់

មេរៀនដៃបញ្ចូលនេះផ្តល់ជូនអ្នកនូវដំណើរការដើម្បីតំឡើងបរិយាកាសអភិវឌ្ឍពេញលេញសម្រាប់បង្កើតម៉ាស៊ីនមេ MCP ជាមួយនឹងការរួមបញ្ចូល PostgreSQL។ អ្នកនឹងកំណត់រចនាសម្ព័ន្ធឧបករណ៍ទាំងអស់ដែលចាំបាច់, បញ្ចូលធនធាន Azure, និងផ្ទៀងផ្ទាត់ការតំឡើងរបស់អ្នកមុនពេលអនុវត្តន៍។

## សង្ខេប

បរិយាកាសអភិវឌ្ឍដែលត្រឹមត្រូវគឺសំខាន់សម្រាប់ភាពជោគជ័យនៃការអភិវឌ្ឍម៉ាស៊ីនមេ MCP។ មេរៀននេះផ្តល់ជូនដំណែនាំជាដំណាក់កាលសម្រាប់ការតំឡើង Docker, សេវាកម្ម Azure, ឧបករណ៍អភិវឌ្ឍ, និងការផ្ទៀងផ្ទាត់ថាទាំងអស់ដំណើរការល្អគ្នា។

នៅចុងបញ្ចប់នៃមេរៀននេះ អ្នកនឹងមានបរិយាកាសអភិវឌ្ឍពេញលេញដែលត្រៀមរួចសម្រាប់ការបង្កើតម៉ាស៊ីនមេ Zava Retail MCP។

## គោលបំណងរៀន

នៅចុងបញ្ចប់នៃមេរៀននេះ អ្នកនឹងអាច៖

- **ដំឡើង និងកំណត់រចនាសម្ព័ន្ធ** ឧបករណ៍អភិវឌ្ឍគ្រប់យ៉ាង
- **បញ្ចូលធនធាន Azure** ដែលចាំបាច់សម្រាប់ម៉ាស៊ីនមេ MCP
- **តំឡើង Docker containers** សម្រាប់ PostgreSQL និងម៉ាស៊ីនមេ MCP
- **ផ្ទៀងផ្ទាត់** ការតំឡើងបរិយាកាសរបស់អ្នកជាមួយនឹងការតភ្ជាប់សាកល្បង
- **ដោះស្រាយបញ្ហា** សំខាន់ៗនៃការតំឡើង និងការកំណត់រចនាសម្ព័ន្ធ
- **យល់ដឹង** អំពីដំណើរការអភិវឌ្ឍ និងរចនាសម្ព័ន្ធឯកសារ

## 📋 ការត្រួតពិនិត្យលក្ខខណ្ឌជាមុន

មុនចាប់ផ្តើម សូមធានាថាអ្នកមាន៖

### ចំណេះដឹងដែលត្រូវការ
- ការប្រើប្រាស់បញ្ជារជាបន្ទាត់មូលដ្ឋាន (Windows Command Prompt/PowerShell)
- យល់ដឹងអំពីអថេរបរិស្ថាន
- ស្គាល់ Git សម្រាប់គ្រប់គ្រងកំណែ
- យល់ដឹងពីមូលដ្ឋាន Docker (containers, images, volumes)

### តម្រូវការប្រព័ន្ធ
- **ប្រព័ន្ធប្រតិបត្តិការ**: Windows 10/11, macOS, ឬ Linux
- **RAM**: ចន្លោះអប្បបរមា 8GB (16GB សម្រាប់ផ្តល់អនុសាសន៍)
- **ទំហំស្ដុក**: មានទំហំទំនេរពី 10GB ឡើង
- **បណ្ដាញ**: ការតភ្ជាប់អ៊ីនធឺណិតសម្រាប់ចូលទាញយកនិងបញ្ចូល Azure

### តម្រូវការបញ្ជីគណនី
- **ជាវ Azure**: កម្រិតឥតគិតថ្លៃគ្រប់គ្រាន់
- **គណនី GitHub**: សម្រាប់ចូលប្រើឃ្លាំងកូដ
- **គណនី Docker Hub**: (ជាជម្រើស) សម្រាប់បោះពុម្ពរូបភាពផ្ទាល់ខ្លួន

## 🛠️ ការដំឡើងឧបករណ៍

### 1. ដំឡើង Docker Desktop

Docker ផ្តល់បរិយាកាស container សម្រាប់ការតំឡើងអភិវឌ្ឍរបស់យើង។

#### ដំឡើងលើ Windows

1. **ទាញយក Docker Desktop**៖
   ```cmd
   # Visit https://desktop.docker.com/win/stable/Docker%20Desktop%20Installer.exe
   # Or use Windows Package Manager
   winget install Docker.DockerDesktop
   ```

2. **ដំឡើង និងកំណត់រចនាសម្ព័ន្ធ**៖
   - ដំណើរការជា Administrator
   - បើកការរួមបញ្ចូល WSL 2 នៅពេលដែលត្រូវបានលើកឡើង
   - ចាប់ផ្តើមកុំព្យូទ័រ ជាចាំបាច់បន្ទាប់ពីបញ្ចប់ការដំឡើង

3. **ផ្ទៀងផ្ទាត់ការដំឡើង**៖
   ```cmd
   docker --version
   docker-compose --version
   ```

#### ដំឡើងលើ macOS

1. **ទាញយក និងដំឡើង**៖
   ```bash
   # ទាញយកពី https://desktop.docker.com/mac/stable/Docker.dmg
   # ឬប្រើ Homebrew
   brew install --cask docker
   ```

2. **ចាប់ផ្តើម Docker Desktop**៖
   - បើក Docker Desktop ពី Applications
   - បញ្ចប់ការតំឡើងជំហានដំបូង

3. **ផ្ទៀងផ្ទាត់ការដំឡើង**៖
   ```bash
   docker --version
   docker-compose --version
   ```

#### ដំឡើងលើ Linux

1. **ដំឡើង Docker Engine**៖
   ```bash
   # Ubuntu/Debian
   curl -fsSL https://get.docker.com -o get-docker.sh
   sudo sh get-docker.sh
   sudo usermod -aG docker $USER
   
   # ចុះចេញហើយចូលវិញដើម្បីឲ្យការផ្លាស់ប្តូរគ្រួសារធ្វើការសកម្ម
   ```

2. **ដំឡើង Docker Compose**៖
   ```bash
   sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
   sudo chmod +x /usr/local/bin/docker-compose
   ```

### 2. ដំឡើង Azure CLI

Azure CLI អនុញ្ញាតឱ្យបញ្ចូល និងគ្រប់គ្រងធនធាន Azure បាន។

#### ដំឡើងលើ Windows

```cmd
# Using Windows Package Manager
winget install Microsoft.AzureCLI

# Or download MSI from: https://aka.ms/installazurecliwindows
```

#### ដំឡើងលើ macOS

```bash
# ការប្រើប្រាស់ Homebrew
brew install azure-cli

# រឺក៏ការប្រើប្រាស់កម្មវិធីដំឡើង
curl -L https://aka.ms/InstallAzureCli | bash
```

#### ដំឡើងលើ Linux

```bash
# យូប៊ុនទូ/ដេប៊ីយ៉ាន់
curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash

# អា អែរ អិល អ៊ី អិល/ជិនថអូអេស
sudo rpm --import https://packages.microsoft.com/keys/microsoft.asc
sudo dnf install azure-cli
```

#### ផ្ទៀងផ្ទាត់ និង Authenticate

```bash
# ត្រួតពិនិត្យការតំឡើង
az version

# ចូលទៅកាន់ Azure
az login

# កំណត់ការជាវលំនាំដើម (បើអ្នកមានច្រើន)
az account list --output table
az account set --subscription "Your-Subscription-Name"
```

### 3. ដំឡើង Git

Git ត្រូវការសម្រាប់ប្រើសម្រាប់ clone ឃ្លាំងកូដ និងគ្រប់គ្រងកំណែ។

#### លើ Windows

```cmd
# Using Windows Package Manager
winget install Git.Git

# Or download from: https://git-scm.com/download/win
```

#### លើ macOS

```bash
# Git ត្រូវបានតំឡើងជាមុនស្រាប់ជាធម្មតា ប៉ុន្តែអ្នកអាចធ្វើបច្ចុប្បន្នភាពតាមរយៈ Homebrew បាន។
brew install git
```

#### លើ Linux

```bash
# Ubuntu/Debian
sudo apt update && sudo apt install git

# RHEL/CentOS
sudo dnf install git
```

### 4. ដំឡើង VS Code

Visual Studio Code ផ្តល់បរិយាកាសអភិវឌ្ឍរួមជាមួយគាំទ្រម៉ាស៊ីនមេ MCP។

#### ដំឡើង

```cmd
# Windows
winget install Microsoft.VisualStudioCode

# macOS
brew install --cask visual-studio-code

# Linux (Ubuntu/Debian)
sudo snap install code --classic
```

#### វិស្សមកាលដែលត្រូវការ

ដំឡើងវិស្សមកាល VS Code ទាំងនេះ៖

```bash
# ដំឡើងតាមបន្ទាត់​ពាក្យ​បញ្ជា
code --install-extension ms-python.python
code --install-extension ms-vscode.vscode-json
code --install-extension ms-azuretools.vscode-docker
code --install-extension ms-vscode.azure-account
```

ឬដំឡើងតាមរយៈ VS Code៖
1. បើក VS Code
2. ទៅកាន់ Extensions (Ctrl+Shift+X)
3. ដំឡើង៖
   - **Python** (Microsoft)
   - **Docker** (Microsoft)
   - **Azure Account** (Microsoft)
   - **JSON** (Microsoft)

### 5. ដំឡើង Python

Python 3.8+ ត្រូវការសម្រាប់អភិវឌ្ឍម៉ាស៊ីនមេ MCP។

#### លើ Windows

```cmd
# Using Windows Package Manager
winget install Python.Python.3.11

# Or download from: https://www.python.org/downloads/
```

#### លើ macOS

```bash
# ការប្រើប្រាស់ Homebrew
brew install python@3.11
```

#### លើ Linux

```bash
# Ubuntu/Debian
sudo apt update && sudo apt install python3.11 python3.11-pip python3.11-venv

# RHEL/CentOS
sudo dnf install python3.11 python3.11-pip
```

#### ផ្ទៀងផ្ទាត់ការដំឡើង

```bash
python --version  # គួរតែបង្ហាញ Python 3.11.x
pip --version      # គួរតែបង្ហាញកំណែ pip
```

## 🚀 ការតំឡើងគម្រោង

### 1. Clone ឃ្លាំងកូដ

```bash
# ចម្លងគណនីសំខាន់
git clone https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail.git

# នាវាសកម្មទៅកាន់ថតគម្រោង
cd MCP-Server-and-PostgreSQL-Sample-Retail

# ត្រួតពិនិត្យរចនាសម្ព័ន្ធគណនី
ls -la
```

### 2. បង្កើតបរិយាកាស Python វេរួស្ស

```bash
# បង្កើតបរិយាកាសវីរុស
python -m venv mcp-env

# បើកបរិយាកាសវីរុស
# វីនដូ
mcp-env\Scripts\activate

# macOS/Linux
source mcp-env/bin/activate

# លើកតម្កើង pip
python -m pip install --upgrade pip
```

### 3. ដំឡើងបណ្ណាល័យ Python ចាំបាច់

```bash
# តំឡើងការពឹងផ្អែកអភិវឌ្ឍន៍
pip install -r requirements.lock.txt

# ផ្ទៀងផ្ទាត់កញ្ចប់សំខាន់ៗ
pip list | grep fastmcp
pip list | grep asyncpg
pip list | grep azure
```

## ☁️ ការបញ្ចូលធនធាន Azure

### 1. យល់ដឹងពីតម្រូវការធនធាន

ម៉ាស៊ីនមេ MCP របស់យើងត្រូវការធនធាន Azure ដូចតទៅ៖

| **ធនធាន** | **គោលបំណង** | **ថ្លៃខែប្រចាំប្រមាណ** |
|--------------|-------------|-------------------|
| **Azure AI Foundry** | ការផ្ទុក និងគ្រប់គ្រងម៉ូដែល AI | $10-50/ខែ |
| **OpenAI Deployment** | ម៉ូដែលតំណភ្ជាប់អត្ថបទ (text-embedding-3-small) | $5-20/ខែ |
| **Application Insights** | ត្រួតពិនិត្យ និងធនធានពីរថ្លៃ | $5-15/ខែ |
| **Resource Group** | ការរៀបចំប្រពន្ធធនធាន | ផ្លែឈើ |

### 2. បញ្ចូលធនធាន Azure

#### ជម្រើស A៖ បញ្ចូលដោយស្វ័យប្រវត្ត (ផ្តល់អនុសាសន៍)

```bash
# ទៅកាន់ថតហេដ្ឋារចនាសម្ព័ន្ធ
cd infra

# Windows - PowerShell
./deploy.ps1

# macOS/Linux - Bash
./deploy.sh
```

ស្គ្រីបបញ្ចូលនឹង៖
1. បង្កើត Resource Group ផ្ទាល់ខ្លួន
2. បញ្ចូលធនធាន Azure AI Foundry
3. បញ្ចូលម៉ូដែល text-embedding-3-small
4. កំណត់រចនាសម្ព័ន្ធ Application Insights
5. បង្កើតឲ្យ Service Principal សម្រាប់ Authenticate
6. បង្កើតឯកសារ `.env` ជាមួយការកំណត់រចនាសម្ព័ន្ធ

#### ជម្រើស B៖ បញ្ចូលដោយដៃ

បើអ្នកចូលចិត្តគ្រប់គ្រងដោយដៃ ឬស្គ្រីបស្វ័យប្រវត្តបរាជ័យ៖

```bash
# កំណត់អថេរ
RESOURCE_GROUP="rg-zava-mcp-$(date +%s)"
LOCATION="westus2"
AI_PROJECT_NAME="zava-ai-project"

# បង្កើតក្រុមធនធាន
az group create --name $RESOURCE_GROUP --location $LOCATION

# បង្ហាញទំព័រជូនជីវថត្រង់បេី
az deployment group create \
  --resource-group $RESOURCE_GROUP \
  --template-file main.bicep \
  --parameters location=$LOCATION \
  --parameters resourcePrefix="zava-mcp"
```

### 3. ផ្ទៀងផ្ទាត់ការបញ្ចូល Azure

```bash
# ពិនិត្យ​ក្រុមធនធាន
az group show --name $RESOURCE_GROUP --output table

# បញ្ជីធនធាន​ដែលបានដាក់ឲ្យដំណើរការ
az resource list --resource-group $RESOURCE_GROUP --output table

# ដើម្បី​សាកល្បង​សេវា AI
az cognitiveservices account show \
  --name "your-ai-service-name" \
  --resource-group $RESOURCE_GROUP
```

### 4. កំណត់អថេរបរិស្ថាន

បន្ទាប់ពីបញ្ចូល អ្នកគួរតែមានឯកសារ `.env`។ សូមផ្ទៀងផ្ទាត់ថាតាមដានមាន៖

```bash
# ខ្លឹមសារឯកសារ .env
PROJECT_ENDPOINT=https://your-project.cognitiveservices.azure.com/
AZURE_OPENAI_ENDPOINT=https://your-openai.openai.azure.com/
EMBEDDING_MODEL_DEPLOYMENT_NAME=text-embedding-3-small
AZURE_CLIENT_ID=your-client-id
AZURE_CLIENT_SECRET=your-client-secret
AZURE_TENANT_ID=your-tenant-id
APPLICATIONINSIGHTS_CONNECTION_STRING=InstrumentationKey=your-key;...

# ការកំណត់រចនាសម្ព័ន្ធមូលដ្ឋានទិន្នន័យ (សម្រាប់ការអភិវឌ្ឍន៍)
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
POSTGRES_DB=zava
POSTGRES_USER=postgres
POSTGRES_PASSWORD=your-secure-password
```

## 🐳 ការតំឡើងបរិយាកាស Docker

### 1. យល់ដឹងពី Docker Composition

បរិយាកាសអភិវឌ្ឍរបស់យើងប្រើ Docker Compose៖

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

### 2. ចាប់ផ្តើមបរិយាកាសអភិវឌ្ឍ

```bash
# ប្រាកដថាអ្នកនៅក្នុងថតគម្រោងមូលដ្ឋាន
cd /path/to/MCP-Server-and-PostgreSQL-Sample-Retail

# ចាប់ផ្តើមសេវាកម្ម
docker-compose up -d

# ពិនិត្យស្ថានភាពសេវាកម្ម
docker-compose ps

# មើលកំណត់ហេតុ
docker-compose logs -f
```

### 3. ផ្ទៀងផ្ទាត់ការតំឡើងមូលដ្ឋានទិន្នន័យ

```bash
# ចូលទៅកាន់ប្រអប់ PostgreSQL
docker-compose exec postgres psql -U postgres -d zava

# ពិនិត្យរចនាសម្ព័ន្ធទិន្នន័យ
\dt retail.*

# ជម្រាបព័ត៌មានគំរូ
SELECT COUNT(*) FROM retail.stores;
SELECT COUNT(*) FROM retail.products;
SELECT COUNT(*) FROM retail.orders;

# ចាកចេញពី PostgreSQL
\q
```

### 4. សាកល្បងម៉ាស៊ីនមេ MCP

```bash
# ពិនិត្យសុខភាពម៉ាស៊ីនបម្រើ MCP
curl http://localhost:8000/health

# សាកល្បងចំណុចបញ្ចប់ MCP ជាមូលដ្ឋាន
curl -X POST http://localhost:8000/mcp \
  -H "Content-Type: application/json" \
  -H "x-rls-user-id: 00000000-0000-0000-0000-000000000000" \
  -d '{"method": "tools/list", "params": {}}'
```

## 🔧 ការកំណត់រចនាសម្ព័ន្ធ VS Code

### 1. កំណត់រចនាសម្ព័ន្ធការរួមបញ្ចូល MCP

បង្កើតការកំណត់រចនាសម្ព័ន្ធ MCP នៅក្នុង VS Code៖

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

### 2. កំណត់បរិយាកាស Python

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

### 3. សាកល្បងការរួមបញ្ចូល VS Code

1. **បើកគម្រោងក្នុង VS Code**៖
   ```bash
   code .
   ```

2. **បើក AI Chat**៖
   - ចុច `Ctrl+Shift+P` (Windows/Linux) ឬ `Cmd+Shift+P` (macOS)
   - វាយ "AI Chat" ហើយជ្រើសរើស "AI Chat: Open Chat"

3. **សាកល្បងការតភ្ជាប់ម៉ាស៊ីនមេ MCP**៖
   - នៅក្នុង AI Chat វាយ `#zava` ហើយជ្រើសរើសម៉ាស៊ីនមេខ្លះៗដែលបានកំណត់
   - សួរ៖ "តារាងណាខ្លះមានក្នុងមូលដ្ឋានទិន្នន័យ?"
   - អ្នកគួរតែទទួលបានការឆ្លើយតបបញ្ជីតារាងទិន្នន័យលក់រាយ

## ✅ ការផ្ទៀងផ្ទាត់បរិយាកាស

### 1. ការត្រួតពិនិត្យប្រព័ន្ធពេញលេញ

រត់ស្គ្រីបផ្ទៀងផ្ទាត់នេះដើម្បីពិនិត្យការតំឡើងរបស់អ្នក៖

```bash
# បង្កើតស្គ្រីបផ្ទៀងផ្ទាត់
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
    
    # ពិនិត្យកំណែ Python
    python_version = sys.version_info
    results['python'] = {
        'status': 'pass' if python_version >= (3, 8) else 'fail',
        'version': f"{python_version.major}.{python_version.minor}.{python_version.micro}",
        'required': '3.8+'
    }
    
    # ពិនិត្យកញ្ចប់ដែលចាំបាច់
    required_packages = ['fastmcp', 'asyncpg', 'azure-ai-projects']
    for package in required_packages:
        try:
            __import__(package)
            results[f'package_{package}'] = {'status': 'pass'}
        except ImportError:
            results[f'package_{package}'] = {'status': 'fail', 'error': 'Not installed'}
    
    # ពិនិត្យ Docker
    try:
        result = subprocess.run(['docker', '--version'], capture_output=True, text=True)
        results['docker'] = {
            'status': 'pass' if result.returncode == 0 else 'fail',
            'version': result.stdout.strip() if result.returncode == 0 else 'Not available'
        }
    except FileNotFoundError:
        results['docker'] = {'status': 'fail', 'error': 'Docker not found'}
    
    # ពិនិត្យ Azure CLI
    try:
        result = subprocess.run(['az', '--version'], capture_output=True, text=True)
        results['azure_cli'] = {
            'status': 'pass' if result.returncode == 0 else 'fail',
            'version': result.stdout.split('\n')[0] if result.returncode == 0 else 'Not available'
        }
    except FileNotFoundError:
        results['azure_cli'] = {'status': 'fail', 'error': 'Azure CLI not found'}
    
    # ពិនិត្យអថេរបរិយាកាស
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
    
    # ពិនិត្យការតភ្ជាប់មូលដ្ឋានទិន្នន័យ
    try:
        conn = await asyncpg.connect(
            host=os.getenv('POSTGRES_HOST', 'localhost'),
            port=int(os.getenv('POSTGRES_PORT', 5432)),
            database=os.getenv('POSTGRES_DB', 'zava'),
            user=os.getenv('POSTGRES_USER', 'postgres'),
            password=os.getenv('POSTGRES_PASSWORD', 'secure_password')
        )
        
        # សាកល្បងការស្នើសុំ
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
    
    # ពិនិត្យម៉ាស៊ីនបម្រើ MCP
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
    
    # ពិនិត្យសេវាកម្ម Azure AI
    try:
        credential = DefaultAzureCredential()
        project_client = AIProjectClient(
            endpoint=os.getenv('PROJECT_ENDPOINT'),
            credential=credential
        )
        
        # នេះនឹងបរាជ័យប្រសិនបើលិខិតអនុញ្ញាតមិនត្រឹមត្រូវ
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

# រត់ការផ្ទៀងផ្ទាត់
python validate_setup.py
```

### 2. បញ្ជីបញ្ជាក់ការផ្ទៀងផ្ទាត់ដោយដៃ

**✅ ឧបករណ៍មូលដ្ឋាន**
- [ ] ដំឡើង Docker version 20.10+ និងកំពុងដំណើរការ
- [ ] ដំឡើង និង Authenticate Azure CLI 2.40+
- [ ] Python 3.8+ ជាមួយ pip ដំឡើងរួច
- [ ] Git 2.30+ ដំឡើងរួច
- [ ] VS Code ជាមួយវិស្សមកាលដែលត្រូវការ

**✅ ធនធាន Azure**
- [ ] បង្កើត Resource Group បានជោគជ័យ
- [ ] គម្រោង AI Foundry បញ្ចូលរួច
- [ ] ម៉ូដែល OpenAI text-embedding-3-small បញ្ចូលរួច
- [ ] កំណត់ Application Insights រួច
- [ ] បង្កើត Service Principal ជាមួយសិទ្ធិត្រឹមត្រូវ

**✅ ការកំណត់បរិយាកាស**
- [ ] បង្កើតឯកសារ `.env` ជាមួយអថេរទាំងអស់
- [ ] អ្នកចូលប្រើ (credentials) Azure មានស្ថិតិ (សាកល្បងជាមួយ `az account show`)
- [ ] កន្រ្តាក់ PostgreSQL កំពុងដំណើរការ ហើយអាចចូលប្រើបាន
- [ ] ទិន្នន័យគំរូបានដាក់ក្នុងមូលដ្ឋានទិន្នន័យ

**✅ ការរួមបញ្ចូល VS Code**
- [ ] កំណត់ `.vscode/mcp.json`
- [ ] បានកំណត់ Interpreter Python ទៅបរិយាកាសវេរួស្ស
- [ ] ម៉ាស៊ីនមេ MCP បង្ហាញនៅក្នុង AI Chat
- [ ] អាចបញ្ចេញសំណួរសាកល្បងតាម AI Chat បាន

## 🛠️ ដោះស្រាយបញ្ហាទូទៅ

### បញ្ហា Docker

**បញ្ហា**: Containers Docker មិនចាប់ផ្តើមបាន
```bash
# ពិនិត្យស្ថានភាពសេវាកម្ម Docker
docker info

# ពិនិត្យធនធានដែលមាន
docker system df

# លាងសម្អាតប្រសិនបើចាំបាច់
docker system prune -f

# ចាប់ផ្តើមឡើងវិញ Docker Desktop (Windows/macOS)
# ឬចាប់ផ្តើមឡើងវិញសេវាកម្ម Docker (Linux)
sudo systemctl restart docker
```

**បញ្ហា**: ការតភ្ជាប់ទៅ PostgreSQL បរាជ័យ
```bash
# ពិនិត្យកំណត់ហេតុនៃកុងតឺន័រ
docker-compose logs postgres

# បញ្ជាក់ថាកុងតឺន័រមានសុខភាពល្អ
docker-compose ps

# សាកល្បងការតភ្ជាប់ដោយផ្ទាល់
docker-compose exec postgres psql -U postgres -d zava -c "SELECT 1;"
```

### បញ្ហាបញ្ចូល Azure

**បញ្ហា**: ការបញ្ចូល Azure បរាជ័យ
```bash
# ពិនិត្យការផ្ទៀងផ្ទាត់អ្នកប្រើ Azure CLI
az account show

# ផ្ទៀងផ្ទាត់សិទ្ធិការជាវ
az role assignment list --assignee $(az account show --query user.name -o tsv)

# ពិនិត្យការចុះបញ្ជីអ្នកផ្គត់ផ្គង់ធនធាន
az provider register --namespace Microsoft.CognitiveServices
az provider register --namespace Microsoft.Insights
```

**បញ្ហា**: ការផ្ទៀងផ្ទាត់សេវាកម្ម AI មិនបាន
```bash
# ពិនិត្យសេវាគោលបំណង
az login --service-principal \
  --username $AZURE_CLIENT_ID \
  --password $AZURE_CLIENT_SECRET \
  --tenant $AZURE_TENANT_ID

# ពិនិត្យការតម្លើងសេវា AI
az cognitiveservices account list --query "[].{Name:name,Kind:kind,Location:location}"
```

### បញ្ហាបរិយាកាស Python

**បញ្ហា**: ការដំឡើងកញ្ចប់បរាជ័យ
```bash
# បន្ថែមកម្រិត pip និង setuptools
python -m pip install --upgrade pip setuptools wheel

# លាងសម្អាត cache pip
pip cache purge

# ដំឡើងកញ្ចប់មួយៗ ដើម្បីរកចំណុចបញ្ហា
pip install fastmcp
pip install asyncpg
pip install azure-ai-projects
```

**បញ្ហា**: VS Code មិនអាចរក Interpreter Python បាន
```bash
# បង្ហាញផ្លូវ Python interpreter
which python  # macOS/Linux
where python  # Windows

# ចាប់ផ្តើមបរិយាកាសវើឆ្វេងមុន
source mcp-env/bin/activate  # macOS/Linux
mcp-env\Scripts\activate     # Windows

# បន្ទាប់មកបើក VS Code
code .
```

## 🎯 មេរៀនសំខាន់ៗ

បន្ទាប់ពីបញ្ចប់មេរៀននេះ អ្នកគួរតែមាន៖

✅ **បរិយាកាសអភិវឌ្ឍពេញលេញ**៖ ឧបករណ៍ទាំងអស់បានដំឡើង និងកំណត់រចនាសម្ព័ន្ធសម្រេច  
✅ **ធនធាន Azure បានបញ្ចូល**៖ សេវាអ៊ីស៊ី និងហាដវ៉ែរគាំទ្រ  
✅ **បរិយាកាស Docker កំពុងដំណើរការ**៖ Containers PostgreSQL និងម៉ាស៊ីនមេ MCP  
✅ **ការរួមបញ្ចូល VS Code**៖ ម៉ាស៊ីនមេ MCP បានកំណត់ និងអាចចូលប្រើបាន  
✅ **ការត្រួតពិនិត្យតំឡើងបាន**៖ ជាគ្រប់គ្រងធាតុ និងដំណើរការសាកល្បង  
✅ **ចំណេះដឹងដោះស្រាយបញ្ហា**៖ បញ្ហាទូទៅ និងដំណោះស្រាយ  

## 🚀 ត្រូវធ្វើដូចម្តេចបន្ទាប់

ក្រោយពីបរិយាកាសរបស់អ្នករួចរាល់ ចូលបន្តជាមួយ **[Lab 04: Database Design and Schema](../04-Database/README.md)** ដើម្បី៖

- ស្រាវជ្រាវរចនាសម្ព័ន្ធមូលដ្ឋានទិន្នន័យលំអិត
- យល់ដឹងអំពីការទាញយកទិន្នន័យជាច្រើនជាន់
- រៀនអំពីការអនុវត្ត សុវត្ថិភាពកម្រិតជួរ (Row Level Security)
- ធ្វើការជាមួយទិន្នន័យគំរូលក់រាយ

## 📚 ឯកសារបន្ថែម

### ឧបករណ៍អភិវឌ្ឍ
- [ឯកសារ Docker](https://docs.docker.com/) - ឯកសារពេញលេញសម្រាប់ Docker
- [ឯកសារ Azure CLI](https://docs.microsoft.com/cli/azure/) - ពាក្យបញ្ជា Azure CLI
- [ឯកសារ VS Code](https://code.visualstudio.com/docs) - ការកំណត់រចនាសម្ព័ន្ធនិងវិស្សមកាល

### សេវាកម្ម Azure
- [ឯកសារ Azure AI Foundry](https://docs.microsoft.com/azure/ai-foundry/) - ការកំណត់សេវាអ៊ីស៊ី
- [សេវាអ៊ីស៊ី OpenAI Azure](https://docs.microsoft.com/azure/cognitive-services/openai/) - ការបញ្ចូលម៉ូដែល AI
- [Application Insights](https://docs.microsoft.com/azure/azure-monitor/app/app-insights-overview) - ការត្រួតពិនិត្យ

### អភិវឌ្ឍ Python
- [បរិយាកាស Python វេរួស្ស](https://docs.python.org/3/tutorial/venv.html) - ការគ្រប់គ្រងបរិយាកាស
- [AsyncIO Documentation](https://docs.python.org/3/library/asyncio.html) - លំនាំកម្មវិធីអាស៊ិនគ្រូន
- [FastAPI Documentation](https://fastapi.tiangolo.com/) - លំនាំលើវេបហ្្រ័ម

---

**ក្រោយ**៖ បរិយាកាសរួចរាល់? បន្តជាមួយ [Lab 04: Database Design and Schema](../04-Database/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ការបដិសេធ**៖  
ឯកសារនេះបានបកប្រែដោយប្រើសេវាកម្មបកប្រែ AI [Co-op Translator](https://github.com/Azure/co-op-translator)។ នៅពេលដែលយើងព្យាយាមសម្រាប់ភាពត្រឹមត្រូវ សូមយល់ថាការបកប្រែដោយស្វ័យប្រវត្តិនោះអាចមានកំហុស ឬភាពមិនត្រឹមត្រូវ។ ឯកសារដើមនៅក្នុងភាសាផ្ទាល់របស់វាគួរត្រូវបានគេគិតថាជាដើមទិន្នន័យដែលមានសិទ្ធិលើអត្ថបទ។ សម្រាប់ព័ត៌មានសំខាន់ ការបកប្រែដោយមនុស្សដែលមានជំនាញគឺត្រូវបានណែនាំ។ យើងមិនទទួលខុសត្រូវចំពោះការយល់ច្រឡំ ឬការបកប្រែដែលមិនត្រឹមត្រូវណាមួយដែលកើតឡើងពីការប្រើប្រាស់ការបកប្រែនេះទេ។
<!-- CO-OP TRANSLATOR DISCLAIMER END -->