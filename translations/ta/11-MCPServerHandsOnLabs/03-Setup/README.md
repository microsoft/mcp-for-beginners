# சூழல் அமைப்பு

## 🎯 இந்த ஆய்வகத்தில் என்ன உள்ளடக்கப்பட்டுள்ளது

இந்த கையால் செய்யும் ஆய்வகத்தில் PostgreSQL ஒருங்கிணைப்புடன் MCP சர்வர்களை உருவாக்குவதற்கான முழுமையான மேம்பாட்டு சூழலை அமைப்பதற்கான வழிகாட்டுதலை வழங்குகிறது. நீங்கள் தேவையான அனைத்து கருவிகளையும் அமைக்க, Azure வளங்களை பிரசுரிக்க மற்றும் செயல்படுத்துவதற்கு முன் உங்கள் அமைப்பை சரிபார்க்க கற்றுக்கொள்வீர்கள்.

## கண்ணோட்டம்

சரியான மேம்பாட்டு சூழல் MCP சர்வர் மேம்பாட்டிற்கான வெற்றிக்கு முக்கியமானது. இந்த ஆய்வகம் Docker, Azure சேவைகள், மேம்பாட்டு கருவிகள் மற்றும் அனைத்தும் சரியாக இணைந்து செயல்படுவதை உறுதிப்படுத்துவதற்கான படிப்படியாக வழிகாட்டுதல்களை வழங்குகிறது.

இந்த ஆய்வகத்தின் முடிவில், Zava Retail MCP சர்வரை உருவாக்குவதற்கான முழுமையான செயல்பாட்டு மேம்பாட்டு சூழலை நீங்கள் கொண்டிருப்பீர்கள்.

## கற்றல் நோக்கங்கள்

இந்த ஆய்வகத்தின் முடிவில், நீங்கள்:

- தேவையான அனைத்து மேம்பாட்டு கருவிகளையும் **நிறுவி மற்றும் அமைக்க** முடியும்  
- MCP சர்வருக்கான தேவையான Azure வளங்களை **பிரசுரிக்க** முடியும்  
- PostgreSQL மற்றும் MCP சர்வருக்கான Docker கன்டெய்னர்களை **அமைக்க** முடியும்  
- **சோதனை இணைப்புகளுடன்** உங்கள் சூழல் அமைப்பை சரிபார்க்க முடியும்  
- பொதுவான அமைப்பு பிரச்சினைகள் மற்றும் கட்டமைப்பு சிக்கல்களை **தீர்க்க** முடியும்  
- மேம்பாட்டு பணியாளர்கள் மற்றும் கோப்பு அமைப்பை **புரிந்து** கொள்ள முடியும்  

## 📋 முன் தேவைகள் சரிபார்ப்பு

தொடங்குவதற்கு முன், நீங்கள் பின்வருவனவற்றை உறுதிப்படுத்த வேண்டும்:

### தேவையான அறிவு
- அடிப்படை கட்டளைகள் (Windows Command Prompt/PowerShell)  
- சூழல் மாறிகள் பற்றிய புரிதல்  
- Git பதிப்பு கட்டுப்பாட்டில் பரிச்சயம்  
- Docker அடிப்படை கருத்துக்கள் (கன்டெய்னர்கள், படங்கள், தொகுதிகள்)  

### கணினி தேவைகள்
- **செயல்பாட்டு அமைப்பு**: Windows 10/11, macOS அல்லது Linux  
- **RAM**: குறைந்தது 8GB (16GB பரிந்துரைக்கப்படுகிறது)  
- **சேமிப்பு**: குறைந்தது 10GB இலவச இடம்  
- **இணையம்**: பதிவிறக்கங்கள் மற்றும் Azure பிரசுரத்திற்கான இணைய இணைப்பு  

### கணக்கு தேவைகள்
- **Azure சந்தா**: இலவச நிலை போதுமானது  
- **GitHub கணக்கு**: களஞ்சிய அணுகலுக்காக  
- **Docker Hub கணக்கு**: (விருப்பம்) தனிப்பயன் படங்களை பிரசுரிக்க  

## 🛠️ கருவி நிறுவல்

### 1. Docker Desktop நிறுவவும்

Docker எங்கள் மேம்பாட்டு அமைப்பிற்கான கன்டெய்னர் சூழலை வழங்குகிறது.

#### Windows நிறுவல்

1. **Docker Desktop பதிவிறக்கவும்**:  
   ```cmd
   # Visit https://desktop.docker.com/win/stable/Docker%20Desktop%20Installer.exe
   # Or use Windows Package Manager
   winget install Docker.DockerDesktop
   ```
  
2. **நிறுவல் மற்றும் அமைப்பு**:  
   - நிறுவல் நிரலை நிர்வாகியாக இயக்கவும்  
   - கேட்கப்பட்டால் WSL 2 ஒருங்கிணைப்பை இயக்கவும்  
   - நிறுவல் முடிந்ததும் உங்கள் கணினியை மறுதொடக்கம் செய்யவும்  

3. **நிறுவலை சரிபார்க்கவும்**:  
   ```cmd
   docker --version
   docker-compose --version
   ```
  

#### macOS நிறுவல்

1. **பதிவிறக்கவும் மற்றும் நிறுவவும்**:  
   ```bash
   # Download from https://desktop.docker.com/mac/stable/Docker.dmg
   # Or use Homebrew
   brew install --cask docker
   ```
  
2. **Docker Desktop தொடங்கவும்**:  
   - Applications-இல் இருந்து Docker Desktop-ஐ தொடங்கவும்  
   - ஆரம்ப அமைப்பு வழிகாட்டியை முடிக்கவும்  

3. **நிறுவலை சரிபார்க்கவும்**:  
   ```bash
   docker --version
   docker-compose --version
   ```
  

#### Linux நிறுவல்

1. **Docker Engine நிறுவவும்**:  
   ```bash
   # Ubuntu/Debian
   curl -fsSL https://get.docker.com -o get-docker.sh
   sudo sh get-docker.sh
   sudo usermod -aG docker $USER
   
   # Log out and back in for group changes to take effect
   ```
  
2. **Docker Compose நிறுவவும்**:  
   ```bash
   sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
   sudo chmod +x /usr/local/bin/docker-compose
   ```
  

### 2. Azure CLI நிறுவவும்

Azure CLI Azure வளங்களை பிரசுரிக்க மற்றும் நிர்வகிக்க உதவுகிறது.

#### Windows நிறுவல்

```cmd
# Using Windows Package Manager
winget install Microsoft.AzureCLI

# Or download MSI from: https://aka.ms/installazurecliwindows
```
  

#### macOS நிறுவல்

```bash
# Using Homebrew
brew install azure-cli

# Or using installer
curl -L https://aka.ms/InstallAzureCli | bash
```
  

#### Linux நிறுவல்

```bash
# Ubuntu/Debian
curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash

# RHEL/CentOS
sudo rpm --import https://packages.microsoft.com/keys/microsoft.asc
sudo dnf install azure-cli
```
  

#### சரிபார்க்கவும் மற்றும் அங்கீகரிக்கவும்

```bash
# Check installation
az version

# Login to Azure
az login

# Set default subscription (if you have multiple)
az account list --output table
az account set --subscription "Your-Subscription-Name"
```
  

### 3. Git நிறுவவும்

Git களஞ்சியத்தை கிளோன் செய்யவும் மற்றும் பதிப்பு கட்டுப்பாட்டிற்காக தேவைப்படுகிறது.

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
  

### 4. VS Code நிறுவவும்

Visual Studio Code MCP ஆதரவுடன் ஒருங்கிணைந்த மேம்பாட்டு சூழலை வழங்குகிறது.

#### நிறுவல்

```cmd
# Windows
winget install Microsoft.VisualStudioCode

# macOS
brew install --cask visual-studio-code

# Linux (Ubuntu/Debian)
sudo snap install code --classic
```
  

#### தேவையான நீட்டிப்புகள்

இந்த VS Code நீட்டிப்புகளை நிறுவவும்:

```bash
# Install via command line
code --install-extension ms-python.python
code --install-extension ms-vscode.vscode-json
code --install-extension ms-azuretools.vscode-docker
code --install-extension ms-vscode.azure-account
```
  
அல்லது VS Code மூலம் நிறுவவும்:  
1. VS Code-ஐ திறக்கவும்  
2. Extensions (Ctrl+Shift+X) செல்லவும்  
3. நிறுவவும்:  
   - **Python** (Microsoft)  
   - **Docker** (Microsoft)  
   - **Azure Account** (Microsoft)  
   - **JSON** (Microsoft)  

### 5. Python நிறுவவும்

Python 3.8+ MCP சர்வர் மேம்பாட்டிற்காக தேவைப்படுகிறது.

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
  

#### நிறுவலை சரிபார்க்கவும்

```bash
python --version  # Should show Python 3.11.x
pip --version      # Should show pip version
```
  

## 🚀 திட்ட அமைப்பு

### 1. களஞ்சியத்தை கிளோன் செய்யவும்

```bash
# Clone the main repository
git clone https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail.git

# Navigate to the project directory
cd MCP-Server-and-PostgreSQL-Sample-Retail

# Verify repository structure
ls -la
```
  

### 2. Python மெய்நிகர் சூழலை உருவாக்கவும்

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
  

### 3. Python சார்ந்தவை நிறுவவும்

```bash
# Install development dependencies
pip install -r requirements.lock.txt

# Verify key packages
pip list | grep fastmcp
pip list | grep asyncpg
pip list | grep azure
```
  

## ☁️ Azure வளங்களை பிரசுரிக்க

### 1. வள தேவைகளை புரிந்து கொள்ளவும்

எங்கள் MCP சர்வருக்கு இந்த Azure வளங்கள் தேவை:

| **வளம்** | **நோக்கம்** | **மதிப்பிடப்பட்ட செலவு** |  
|--------------|-------------|-------------------|  
| **Azure AI Foundry** | AI மாடல் ஹோஸ்டிங் மற்றும் மேலாண்மை | $10-50/மாதம் |  
| **OpenAI Deployment** | உரை எம்பெடிங் மாடல் (text-embedding-3-small) | $5-20/மாதம் |  
| **Application Insights** | கண்காணிப்பு மற்றும் தொலைநோக்கு | $5-15/மாதம் |  
| **Resource Group** | வள அமைப்பு | இலவசம் |  

### 2. Azure வளங்களை பிரசுரிக்க

#### விருப்பம் A: தானியங்கி பிரசுரம் (பரிந்துரைக்கப்படுகிறது)

```bash
# Navigate to infrastructure directory
cd infra

# Windows - PowerShell
./deploy.ps1

# macOS/Linux - Bash
./deploy.sh
```
  
பிரசுர ஸ்கிரிப்ட்:  
1. தனித்துவமான வள குழுவை உருவாக்கும்  
2. Azure AI Foundry வளங்களை பிரசுரிக்கும்  
3. text-embedding-3-small மாடலை பிரசுரிக்கும்  
4. Application Insights-ஐ அமைக்கும்  
5. அங்கீகாரத்திற்கான சேவை பிரதிநிதியை உருவாக்கும்  
6. `.env` கோப்பை கட்டமைப்புடன் உருவாக்கும்  

#### விருப்பம் B: கையேடு பிரசுரம்

தானியக்க ஸ்கிரிப்ட் தோல்வியடைந்தால் அல்லது கையேடு கட்டுப்பாட்டை விரும்பினால்:

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
  

### 3. Azure பிரசுரத்தை சரிபார்க்கவும்

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
  

### 4. சூழல் மாறிகளை அமைக்கவும்

பிரசுரத்திற்குப் பிறகு, `.env` கோப்பை நீங்கள் கொண்டிருக்க வேண்டும். இது பின்வருவனவற்றை கொண்டிருக்க வேண்டும்:

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
  

## 🐳 Docker சூழல் அமைப்பு

### 1. Docker அமைப்பை புரிந்து கொள்ளவும்

எங்கள் மேம்பாட்டு சூழல் Docker Compose-ஐ பயன்படுத்துகிறது:

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
  

### 2. மேம்பாட்டு சூழலை தொடங்கவும்

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
  

### 3. தரவுத்தொகுப்பு அமைப்பை சரிபார்க்கவும்

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
  

### 4. MCP சர்வரை சோதிக்கவும்

```bash
# Check MCP server health
curl http://localhost:8000/health

# Test basic MCP endpoint
curl -X POST http://localhost:8000/mcp \
  -H "Content-Type: application/json" \
  -H "x-rls-user-id: 00000000-0000-0000-0000-000000000000" \
  -d '{"method": "tools/list", "params": {}}'
```
  

## 🔧 VS Code கட்டமைப்பு

### 1. MCP ஒருங்கிணைப்பை அமைக்கவும்

VS Code MCP கட்டமைப்பை உருவாக்கவும்:

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
  

### 2. Python சூழலை அமைக்கவும்

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
  

### 3. VS Code ஒருங்கிணைப்பை சோதிக்கவும்

1. **திட்டத்தை VS Code-இல் திறக்கவும்**:  
   ```bash
   code .
   ```
  
2. **AI Chat-ஐ திறக்கவும்**:  
   - `Ctrl+Shift+P` (Windows/Linux) அல்லது `Cmd+Shift+P` (macOS) அழுத்தவும்  
   - "AI Chat" என தட்டச்சு செய்து "AI Chat: Open Chat" தேர்ந்தெடுக்கவும்  

3. **MCP சர்வர் இணைப்பை சோதிக்கவும்**:  
   - AI Chat-இல், `#zava` என தட்டச்சு செய்து அமைக்கப்பட்ட சர்வர்களில் ஒன்றைத் தேர்ந்தெடுக்கவும்  
   - கேளுங்கள்: "தரவுத்தொகுப்பில் எந்த அட்டவணைகள் உள்ளன?"  
   - சில்லறை தரவுத்தொகுப்பு அட்டவணைகளை பட்டியலிடும் பதிலை நீங்கள் பெற வேண்டும்  

## ✅ சூழல் சரிபார்ப்பு

### 1. முழுமையான அமைப்பு சரிபார்ப்பு

உங்கள் அமைப்பை சரிபார்க்க இந்த சரிபார்ப்பு ஸ்கிரிப்டை இயக்கவும்:

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
  

### 2. கையேடு சரிபார்ப்பு சோதனை பட்டியல்

**✅ அடிப்படை கருவிகள்**  
- [ ] Docker பதிப்பு 20.10+ நிறுவப்பட்டு இயங்குகிறது  
- [ ] Azure CLI 2.40+ நிறுவப்பட்டு அங்கீகரிக்கப்பட்டது  
- [ ] Python 3.8+ மற்றும் pip நிறுவப்பட்டு உள்ளது  
- [ ] Git 2.30+ நிறுவப்பட்டு உள்ளது  
- [ ] தேவையான நீட்டிப்புகளுடன் VS Code  

**✅ Azure வளங்கள்**  
- [ ] வள குழு வெற்றிகரமாக உருவாக்கப்பட்டது  
- [ ] AI Foundry திட்டம் பிரசுரிக்கப்பட்டது  
- [ ] OpenAI text-embedding-3-small மாடல் பிரசுரிக்கப்பட்டது  
- [ ] Application Insights அமைக்கப்பட்டது  
- [ ] சரியான அனுமதிகளுடன் சேவை பிரதிநிதி உருவாக்கப்பட்டது  

**✅ சூழல் கட்டமைப்பு**  
- [ ] `.env` கோப்பு தேவையான அனைத்து மாறிகளுடன் உருவாக்கப்பட்டது  
- [ ] Azure அங்கீகாரம் செயல்படுகிறது (`az account show` மூலம் சோதிக்கவும்)  
- [ ] PostgreSQL கன்டெய்னர் இயங்குகிறது மற்றும் அணுகக்கூடியது  
- [ ] தரவுத்தொகுப்பில் மாதிரி தரவுகள் ஏற்றப்பட்டுள்ளன  

**✅ VS Code ஒருங்கிணைப்பு**  
- [ ] `.vscode/mcp.json` அமைக்கப்பட்டது  
- [ ] Python interpreter மெய்நிகர் சூழலுக்கு அமைக்கப்பட்டது  
- [ ] MCP சர்வர்கள் AI Chat-இல் தோன்றுகின்றன  
- [ ] AI Chat மூலம் சோதனை கேள்விகளை இயக்க முடியும்  

## 🛠️ பொதுவான பிரச்சினைகளை தீர்க்க

### Docker பிரச்சினைகள்

**பிரச்சினை**: Docker கன்டெய்னர்கள் தொடங்கவில்லை  
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
  
**பிரச்சினை**: PostgreSQL இணைப்பு தோல்வியடைந்தது  
```bash
# Check container logs
docker-compose logs postgres

# Verify container is healthy
docker-compose ps

# Test direct connection
docker-compose exec postgres psql -U postgres -d zava -c "SELECT 1;"
```
  

### Azure பிரசுர பிரச்சினைகள்

**பிரச்சினை**: Azure பிரசுரம் தோல்வியடைந்தது  
```bash
# Check Azure CLI authentication
az account show

# Verify subscription permissions
az role assignment list --assignee $(az account show --query user.name -o tsv)

# Check resource provider registration
az provider register --namespace Microsoft.CognitiveServices
az provider register --namespace Microsoft.Insights
```
  
**பிரச்சினை**: AI சேவை அங்கீகாரம் தோல்வியடைந்தது  
```bash
# Test service principal
az login --service-principal \
  --username $AZURE_CLIENT_ID \
  --password $AZURE_CLIENT_SECRET \
  --tenant $AZURE_TENANT_ID

# Verify AI service deployment
az cognitiveservices account list --query "[].{Name:name,Kind:kind,Location:location}"
```
  

### Python சூழல் பிரச்சினைகள்

**பிரச்சினை**: தொகுப்பு நிறுவல் தோல்வியடைந்தது  
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
  
**பிரச்சினை**: VS Code Python interpreter-ஐ கண்டுபிடிக்க முடியவில்லை  
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
  

## 🎯 முக்கிய எடுத்துக்காட்டுகள்

இந்த ஆய்வகத்தை முடித்த பிறகு, நீங்கள்:

✅ **முழுமையான மேம்பாட்டு சூழல்**: அனைத்து கருவிகளும் நிறுவப்பட்டு அமைக்கப்பட்டுள்ளன  
✅ **Azure வளங்கள் பிரசுரிக்கப்பட்டது**: AI சேவைகள் மற்றும் ஆதரவு கட்டமைப்பு  
✅ **Docker சூழல் இயங்குகிறது**: PostgreSQL மற்றும் MCP சர்வர் கன்டெய்னர்கள்  
✅ **VS Code ஒருங்கிணைப்பு**: MCP சர்வர்கள் அமைக்கப்பட்டு அணுகக்கூடியது  
✅ **சூழல் சரிபார்ப்பு**: அனைத்து கூறுகளும் சோதிக்கப்பட்டு ஒன்றாக செயல்படுகின்றன  
✅ **பிரச்சினைகளை தீர்க்கும் அறிவு**: பொதுவான பிரச்சினைகள் மற்றும் தீர்வுகள்  

## 🚀 அடுத்தது என்ன?

உங்கள் சூழல் தயாராக இருந்தால், **[Lab 04: தரவுத்தொகுப்பு வடிவமைப்பு மற்றும் அட்டவணை](../04-Database/README.md)**-க்கு தொடரவும்:

- சில்லறை தரவுத்தொகுப்பு அட்டவணையை விரிவாக ஆராயவும்  
- பலTenant தரவுத்தொகுப்பு மாதிரியைப் புரிந்து கொள்ளவும்  
- Row Level Security செயல்பாட்டை கற்றுக்கொள்ளவும்  
- மாதிரி சில்லறை தரவுடன் வேலை செய்யவும்  

## 📚 கூடுதல் வளங்கள்

### மேம்பாட்டு கருவிகள்  
- [Docker Documentation](https://docs.docker.com/) - முழுமையான Docker குறிப்பு  
- [Azure CLI Reference](https://docs.microsoft.com/cli/azure/) - Azure CLI கட்டளைகள்  
- [VS Code Documentation](https://code.visualstudio.com/docs) - எடிட்டர் கட்டமைப்பு மற்றும் நீட்டிப்புகள்  

### Azure சேவைகள்  
- [Azure AI Foundry Documentation](https://docs.microsoft.com/azure/ai-foundry/) - AI சேவை கட்டமைப்பு  
- [Azure OpenAI Service](https://docs.microsoft.com/azure/cognitive-services/openai/) - AI மாடல் பிரசுரம்  
- [Application Insights](https://docs.microsoft.com/azure/azure-monitor/app/app-insights-overview) - கண்காணிப்பு அமைப்பு  

### Python மேம்பாடு  
- [Python Virtual Environments](https://docs.python.org/3/tutorial/venv.html) - சூழல் மேலாண்மை  
- [AsyncIO Documentation](https://docs.python.org/3/library/asyncio.html) - Async நிரலாக்க மாதிரிகள்  
- [FastAPI Documentation](https://fastapi.tiangolo.com/) - வலை கட்டமைப்பு மாதிரிகள்  

---

**அடுத்தது**: சூழல் தயாரா? **[Lab 04: தரவுத்தொகுப்பு வடிவமைப்பு மற்றும் அட்டவணை](../04-Database/README.md)**-க்கு தொடரவும்

---

**குறிப்பு**:  
இந்த ஆவணம் [Co-op Translator](https://github.com/Azure/co-op-translator) என்ற AI மொழிபெயர்ப்பு சேவையை பயன்படுத்தி மொழிபெயர்க்கப்பட்டுள்ளது. எங்கள் நோக்கம் துல்லியமாக இருக்க வேண்டும் என்பதுதான், ஆனால் தானியங்கி மொழிபெயர்ப்புகளில் பிழைகள் அல்லது துல்லியமின்மைகள் இருக்கக்கூடும் என்பதை தயவுசெய்து கவனத்தில் கொள்ளவும். அதன் தாய்மொழியில் உள்ள மூல ஆவணம் அதிகாரப்பூர்வ ஆதாரமாக கருதப்பட வேண்டும். முக்கியமான தகவல்களுக்கு, தொழில்முறை மனித மொழிபெயர்ப்பு பரிந்துரைக்கப்படுகிறது. இந்த மொழிபெயர்ப்பைப் பயன்படுத்துவதால் ஏற்படும் எந்த தவறான புரிதல்கள் அல்லது தவறான விளக்கங்களுக்கு நாங்கள் பொறுப்பல்ல.