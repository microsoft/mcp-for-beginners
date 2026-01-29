# ਵਾਤਾਵਰਣ ਸੈਟਅੱਪ

## 🎯 ਇਹ ਲੈਬ ਕੀ ਕਵਰ ਕਰਦੀ ਹੈ

ਇਹ ਹੈਂਡਸ-ਆਨ ਲੈਬ ਤੁਹਾਨੂੰ PostgreSQL ਇੰਟੀਗ੍ਰੇਸ਼ਨ ਨਾਲ MCP ਸਰਵਰ ਬਣਾਉਣ ਲਈ ਪੂਰਾ ਵਿਕਾਸ ਵਾਤਾਵਰਣ ਸੈਟਅੱਪ ਕਰਨ ਵਿੱਚ ਮਦਦ ਕਰਦੀ ਹੈ। ਤੁਸੀਂ ਸਾਰੇ ਜ਼ਰੂਰੀ ਟੂਲ ਕਨਫਿਗਰ ਕਰੋਗੇ, Azure ਸਰੋਤ ਤੈਨਾਤ ਕਰੋਗੇ, ਅਤੇ ਅਮਲ ਤੋਂ ਪਹਿਲਾਂ ਆਪਣੇ ਸੈਟਅੱਪ ਦੀ ਪੁਸ਼ਟੀ ਕਰੋਗੇ।

## ਝਲਕ

ਸਹੀ ਵਿਕਾਸ ਵਾਤਾਵਰਣ ਸਫਲ MCP ਸਰਵਰ ਵਿਕਾਸ ਲਈ ਬਹੁਤ ਜ਼ਰੂਰੀ ਹੈ। ਇਹ ਲੈਬ Docker, Azure ਸੇਵਾਵਾਂ, ਵਿਕਾਸ ਟੂਲ ਸੈਟਅੱਪ ਕਰਨ ਅਤੇ ਇਹ ਯਕੀਨੀ ਬਣਾਉਣ ਲਈ ਕਦਮ-ਦਰ-ਕਦਮ ਹਦਾਇਤਾਂ ਪ੍ਰਦਾਨ ਕਰਦੀ ਹੈ ਕਿ ਸਭ ਕੁਝ ਸਹੀ ਤਰੀਕੇ ਨਾਲ ਕੰਮ ਕਰ ਰਿਹਾ ਹੈ।

ਇਸ ਲੈਬ ਦੇ ਅੰਤ ਤੱਕ, ਤੁਹਾਡੇ ਕੋਲ Zava Retail MCP ਸਰਵਰ ਬਣਾਉਣ ਲਈ ਪੂਰੀ ਤਰ੍ਹਾਂ ਕਾਰਗਰ ਵਿਕਾਸ ਵਾਤਾਵਰਣ ਹੋਵੇਗਾ।

## ਸਿੱਖਣ ਦੇ ਉਦੇਸ਼

ਇਸ ਲੈਬ ਦੇ ਅੰਤ ਤੱਕ, ਤੁਸੀਂ ਇਹ ਕਰਨ ਦੇ ਯੋਗ ਹੋਵੋਗੇ:

- **ਸਾਰੇ ਜ਼ਰੂਰੀ ਵਿਕਾਸ ਟੂਲ** ਇੰਸਟਾਲ ਅਤੇ ਕਨਫਿਗਰ ਕਰੋ
- **Azure ਸਰੋਤ ਤੈਨਾਤ ਕਰੋ** ਜੋ MCP ਸਰਵਰ ਲਈ ਲੋੜੀਂਦੇ ਹਨ
- **Docker ਕੰਟੇਨਰ ਸੈਟਅੱਪ ਕਰੋ** PostgreSQL ਅਤੇ MCP ਸਰਵਰ ਲਈ
- **ਆਪਣੇ ਵਾਤਾਵਰਣ ਸੈਟਅੱਪ ਦੀ ਪੁਸ਼ਟੀ ਕਰੋ** ਟੈਸਟ ਕਨੈਕਸ਼ਨ ਨਾਲ
- **ਆਮ ਸੈਟਅੱਪ ਸਮੱਸਿਆਵਾਂ ਅਤੇ ਕਨਫਿਗਰੇਸ਼ਨ ਸਮੱਸਿਆਵਾਂ ਨੂੰ ਹੱਲ ਕਰੋ**
- **ਵਿਕਾਸ ਵਰਕਫਲੋ ਅਤੇ ਫਾਈਲ ਸਟ੍ਰਕਚਰ ਨੂੰ ਸਮਝੋ**

## 📋 ਪੂਰਵ-ਸ਼ਰਤਾਂ ਦੀ ਜਾਂਚ

ਸ਼ੁਰੂ ਕਰਨ ਤੋਂ ਪਹਿਲਾਂ, ਇਹ ਯਕੀਨੀ ਬਣਾਓ ਕਿ ਤੁਹਾਡੇ ਕੋਲ ਹੈ:

### ਲੋੜੀਂਦਾ ਗਿਆਨ
- ਬੇਸਿਕ ਕਮਾਂਡ ਲਾਈਨ ਵਰਤੋਂ (Windows Command Prompt/PowerShell)
- ਵਾਤਾਵਰਣ ਵੈਰੀਏਬਲ ਦੀ ਸਮਝ
- Git ਵਰਜਨ ਕੰਟਰੋਲ ਨਾਲ ਜਾਣੂ
- Docker ਦੇ ਬੁਨਿਆਦੀ ਸੰਕਲਪ (ਕੰਟੇਨਰ, ਇਮੇਜ, ਵਾਲਿਊਮ)

### ਸਿਸਟਮ ਦੀਆਂ ਲੋੜਾਂ
- **ਓਪਰੇਟਿੰਗ ਸਿਸਟਮ**: Windows 10/11, macOS, ਜਾਂ Linux
- **RAM**: ਘੱਟੋ-ਘੱਟ 8GB (16GB ਸਿਫਾਰਸ਼ੀ)
- **ਸਟੋਰੇਜ**: ਘੱਟੋ-ਘੱਟ 10GB ਖਾਲੀ ਜਗ੍ਹਾ
- **ਨੈਟਵਰਕ**: ਡਾਊਨਲੋਡ ਅਤੇ Azure ਤੈਨਾਤੀ ਲਈ ਇੰਟਰਨੈਟ ਕਨੈਕਸ਼ਨ

### ਅਕਾਊਂਟ ਦੀਆਂ ਲੋੜਾਂ
- **Azure Subscription**: ਮੁਫ਼ਤ ਟੀਅਰ ਕਾਫ਼ੀ ਹੈ
- **GitHub Account**: ਰਿਪੋਜ਼ਟਰੀ ਤੱਕ ਪਹੁੰਚ ਲਈ
- **Docker Hub Account**: (ਵਿਕਲਪਿਕ) ਕਸਟਮ ਇਮੇਜ ਪਬਲਿਸ਼ ਕਰਨ ਲਈ

## 🛠️ ਟੂਲ ਇੰਸਟਾਲੇਸ਼ਨ

### 1. Docker Desktop ਇੰਸਟਾਲ ਕਰੋ

Docker ਸਾਡੇ ਵਿਕਾਸ ਸੈਟਅੱਪ ਲਈ ਕੰਟੇਨਰਾਈਜ਼ਡ ਵਾਤਾਵਰਣ ਪ੍ਰਦਾਨ ਕਰਦਾ ਹੈ।

#### Windows ਇੰਸਟਾਲੇਸ਼ਨ

1. **Docker Desktop ਡਾਊਨਲੋਡ ਕਰੋ**:
   ```cmd
   # Visit https://desktop.docker.com/win/stable/Docker%20Desktop%20Installer.exe
   # Or use Windows Package Manager
   winget install Docker.DockerDesktop
   ```

2. **ਇੰਸਟਾਲ ਅਤੇ ਕਨਫਿਗਰ ਕਰੋ**:
   - ਇੰਸਟਾਲਰ ਨੂੰ Administrator ਵਜੋਂ ਚਲਾਓ
   - WSL 2 ਇੰਟੀਗ੍ਰੇਸ਼ਨ ਨੂੰ ਐਨੇਬਲ ਕਰੋ ਜਦੋਂ ਪੁੱਛਿਆ ਜਾਵੇ
   - ਇੰਸਟਾਲੇਸ਼ਨ ਪੂਰੀ ਹੋਣ 'ਤੇ ਆਪਣੇ ਕੰਪਿਊਟਰ ਨੂੰ ਰੀਸਟਾਰਟ ਕਰੋ

3. **ਇੰਸਟਾਲੇਸ਼ਨ ਦੀ ਪੁਸ਼ਟੀ ਕਰੋ**:
   ```cmd
   docker --version
   docker-compose --version
   ```

#### macOS ਇੰਸਟਾਲੇਸ਼ਨ

1. **ਡਾਊਨਲੋਡ ਅਤੇ ਇੰਸਟਾਲ ਕਰੋ**:
   ```bash
   # Download from https://desktop.docker.com/mac/stable/Docker.dmg
   # Or use Homebrew
   brew install --cask docker
   ```

2. **Docker Desktop ਸ਼ੁਰੂ ਕਰੋ**:
   - Applications ਤੋਂ Docker Desktop ਲਾਂਚ ਕਰੋ
   - ਸ਼ੁਰੂਆਤੀ ਸੈਟਅੱਪ ਵਿਜ਼ਾਰਡ ਪੂਰਾ ਕਰੋ

3. **ਇੰਸਟਾਲੇਸ਼ਨ ਦੀ ਪੁਸ਼ਟੀ ਕਰੋ**:
   ```bash
   docker --version
   docker-compose --version
   ```

#### Linux ਇੰਸਟਾਲੇਸ਼ਨ

1. **Docker Engine ਇੰਸਟਾਲ ਕਰੋ**:
   ```bash
   # Ubuntu/Debian
   curl -fsSL https://get.docker.com -o get-docker.sh
   sudo sh get-docker.sh
   sudo usermod -aG docker $USER
   
   # Log out and back in for group changes to take effect
   ```

2. **Docker Compose ਇੰਸਟਾਲ ਕਰੋ**:
   ```bash
   sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
   sudo chmod +x /usr/local/bin/docker-compose
   ```

### 2. Azure CLI ਇੰਸਟਾਲ ਕਰੋ

Azure CLI Azure ਸਰੋਤ ਤੈਨਾਤੀ ਅਤੇ ਪ੍ਰਬੰਧਨ ਨੂੰ ਯੋਗ ਬਣਾਉਂਦਾ ਹੈ।

#### Windows ਇੰਸਟਾਲੇਸ਼ਨ

```cmd
# Using Windows Package Manager
winget install Microsoft.AzureCLI

# Or download MSI from: https://aka.ms/installazurecliwindows
```

#### macOS ਇੰਸਟਾਲੇਸ਼ਨ

```bash
# Using Homebrew
brew install azure-cli

# Or using installer
curl -L https://aka.ms/InstallAzureCli | bash
```

#### Linux ਇੰਸਟਾਲੇਸ਼ਨ

```bash
# Ubuntu/Debian
curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash

# RHEL/CentOS
sudo rpm --import https://packages.microsoft.com/keys/microsoft.asc
sudo dnf install azure-cli
```

#### ਪੁਸ਼ਟੀ ਅਤੇ ਪ੍ਰਮਾਣਿਕਤਾ

```bash
# Check installation
az version

# Login to Azure
az login

# Set default subscription (if you have multiple)
az account list --output table
az account set --subscription "Your-Subscription-Name"
```

### 3. Git ਇੰਸਟਾਲ ਕਰੋ

Git ਰਿਪੋਜ਼ਟਰੀ ਕਲੋਨ ਕਰਨ ਅਤੇ ਵਰਜਨ ਕੰਟਰੋਲ ਲਈ ਲੋੜੀਂਦਾ ਹੈ।

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

### 4. VS Code ਇੰਸਟਾਲ ਕਰੋ

Visual Studio Code MCP ਸਹਾਇਤਾ ਨਾਲ ਇੰਟੀਗ੍ਰੇਟਡ ਵਿਕਾਸ ਵਾਤਾਵਰਣ ਪ੍ਰਦਾਨ ਕਰਦਾ ਹੈ।

#### ਇੰਸਟਾਲੇਸ਼ਨ

```cmd
# Windows
winget install Microsoft.VisualStudioCode

# macOS
brew install --cask visual-studio-code

# Linux (Ubuntu/Debian)
sudo snap install code --classic
```

#### ਲੋੜੀਂਦੇ ਐਕਸਟੈਂਸ਼ਨ

ਇਹ VS Code ਐਕਸਟੈਂਸ਼ਨ ਇੰਸਟਾਲ ਕਰੋ:

```bash
# Install via command line
code --install-extension ms-python.python
code --install-extension ms-vscode.vscode-json
code --install-extension ms-azuretools.vscode-docker
code --install-extension ms-vscode.azure-account
```

ਜਾਂ VS Code ਰਾਹੀਂ ਇੰਸਟਾਲ ਕਰੋ:
1. VS Code ਖੋਲ੍ਹੋ
2. ਐਕਸਟੈਂਸ਼ਨ 'ਤੇ ਜਾਓ (Ctrl+Shift+X)
3. ਇੰਸਟਾਲ ਕਰੋ:
   - **Python** (Microsoft)
   - **Docker** (Microsoft)
   - **Azure Account** (Microsoft)
   - **JSON** (Microsoft)

### 5. Python ਇੰਸਟਾਲ ਕਰੋ

Python 3.8+ MCP ਸਰਵਰ ਵਿਕਾਸ ਲਈ ਲੋੜੀਂਦਾ ਹੈ।

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

#### ਇੰਸਟਾਲੇਸ਼ਨ ਦੀ ਪੁਸ਼ਟੀ ਕਰੋ

```bash
python --version  # Should show Python 3.11.x
pip --version      # Should show pip version
```

## 🚀 ਪ੍ਰੋਜੈਕਟ ਸੈਟਅੱਪ

### 1. ਰਿਪੋਜ਼ਟਰੀ ਕਲੋਨ ਕਰੋ

```bash
# Clone the main repository
git clone https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail.git

# Navigate to the project directory
cd MCP-Server-and-PostgreSQL-Sample-Retail

# Verify repository structure
ls -la
```

### 2. Python ਵਰਚੁਅਲ ਵਾਤਾਵਰਣ ਬਣਾਓ

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

### 3. Python Dependencies ਇੰਸਟਾਲ ਕਰੋ

```bash
# Install development dependencies
pip install -r requirements.lock.txt

# Verify key packages
pip list | grep fastmcp
pip list | grep asyncpg
pip list | grep azure
```

## ☁️ Azure ਸਰੋਤ ਤੈਨਾਤੀ

### 1. ਸਰੋਤ ਦੀਆਂ ਲੋੜਾਂ ਨੂੰ ਸਮਝੋ

ਸਾਡੇ MCP ਸਰਵਰ ਨੂੰ ਇਹ Azure ਸਰੋਤਾਂ ਦੀ ਲੋੜ ਹੈ:

| **ਸਰੋਤ** | **ਉਦੇਸ਼** | **ਅਨੁਮਾਨਿਤ ਲਾਗਤ** |
|--------------|-------------|-------------------|
| **Azure AI Foundry** | AI ਮਾਡਲ ਹੋਸਟਿੰਗ ਅਤੇ ਪ੍ਰਬੰਧਨ | $10-50/ਮਹੀਨਾ |
| **OpenAI Deployment** | ਟੈਕਸਟ ਐਮਬੈਡਿੰਗ ਮਾਡਲ (text-embedding-3-small) | $5-20/ਮਹੀਨਾ |
| **Application Insights** | ਮਾਨੀਟਰਿੰਗ ਅਤੇ ਟੈਲੀਮੈਟਰੀ | $5-15/ਮਹੀਨਾ |
| **Resource Group** | ਸਰੋਤ ਸੰਗਠਨ | ਮੁਫ਼ਤ |

### 2. Azure ਸਰੋਤ ਤੈਨਾਤ ਕਰੋ

#### ਵਿਕਲਪ A: ਆਟੋਮੈਟਿਕ ਤੈਨਾਤੀ (ਸਿਫਾਰਸ਼ੀ)

```bash
# Navigate to infrastructure directory
cd infra

# Windows - PowerShell
./deploy.ps1

# macOS/Linux - Bash
./deploy.sh
```

ਤੈਨਾਤੀ ਸਕ੍ਰਿਪਟ ਇਹ ਕਰੇਗਾ:
1. ਇੱਕ ਵਿਲੱਖਣ ਰਿਸੋਰਸ ਗਰੁੱਪ ਬਣਾਓ
2. Azure AI Foundry ਸਰੋਤ ਤੈਨਾਤ ਕਰੋ
3. text-embedding-3-small ਮਾਡਲ ਤੈਨਾਤ ਕਰੋ
4. Application Insights ਕਨਫਿਗਰ ਕਰੋ
5. ਪ੍ਰਮਾਣਿਕਤਾ ਲਈ ਸੇਵਾ ਪ੍ਰਿੰਸਿਪਲ ਬਣਾਓ
6. `.env` ਫਾਈਲ ਜਨਰੇਟ ਕਰੋ ਕਨਫਿਗਰੇਸ਼ਨ ਨਾਲ

#### ਵਿਕਲਪ B: ਮੈਨੂਅਲ ਤੈਨਾਤੀ

ਜੇ ਤੁਸੀਂ ਮੈਨੂਅਲ ਕੰਟਰੋਲ ਨੂੰ ਤਰਜੀਹ ਦਿੰਦੇ ਹੋ ਜਾਂ ਆਟੋਮੈਟਿਕ ਸਕ੍ਰਿਪਟ ਫੇਲ੍ਹ ਹੋ ਜਾਂਦੀ ਹੈ:

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

### 3. Azure ਤੈਨਾਤੀ ਦੀ ਪੁਸ਼ਟੀ ਕਰੋ

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

### 4. ਵਾਤਾਵਰਣ ਵੈਰੀਏਬਲ ਕਨਫਿਗਰ ਕਰੋ

ਤੈਨਾਤੀ ਤੋਂ ਬਾਅਦ, ਤੁਹਾਡੇ ਕੋਲ `.env` ਫਾਈਲ ਹੋਣੀ ਚਾਹੀਦੀ ਹੈ। ਇਹ ਯਕੀਨੀ ਬਣਾਓ ਕਿ ਇਸ ਵਿੱਚ ਇਹ ਸ਼ਾਮਲ ਹੈ:

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

## 🐳 Docker ਵਾਤਾਵਰਣ ਸੈਟਅੱਪ

### 1. Docker Composition ਨੂੰ ਸਮਝੋ

ਸਾਡਾ ਵਿਕਾਸ ਵਾਤਾਵਰਣ Docker Compose ਵਰਤਦਾ ਹੈ:

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

### 2. ਵਿਕਾਸ ਵਾਤਾਵਰਣ ਸ਼ੁਰੂ ਕਰੋ

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

### 3. ਡਾਟਾਬੇਸ ਸੈਟਅੱਪ ਦੀ ਪੁਸ਼ਟੀ ਕਰੋ

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

### 4. MCP ਸਰਵਰ ਟੈਸਟ ਕਰੋ

```bash
# Check MCP server health
curl http://localhost:8000/health

# Test basic MCP endpoint
curl -X POST http://localhost:8000/mcp \
  -H "Content-Type: application/json" \
  -H "x-rls-user-id: 00000000-0000-0000-0000-000000000000" \
  -d '{"method": "tools/list", "params": {}}'
```

## 🔧 VS Code ਕਨਫਿਗਰੇਸ਼ਨ

### 1. MCP ਇੰਟੀਗ੍ਰੇਸ਼ਨ ਕਨਫਿਗਰ ਕਰੋ

VS Code MCP ਕਨਫਿਗਰੇਸ਼ਨ ਬਣਾਓ:

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

### 2. Python ਵਾਤਾਵਰਣ ਕਨਫਿਗਰ ਕਰੋ

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

### 3. VS Code ਇੰਟੀਗ੍ਰੇਸ਼ਨ ਟੈਸਟ ਕਰੋ

1. **ਪ੍ਰੋਜੈਕਟ ਨੂੰ VS Code ਵਿੱਚ ਖੋਲ੍ਹੋ**:
   ```bash
   code .
   ```

2. **AI Chat ਖੋਲ੍ਹੋ**:
   - `Ctrl+Shift+P` (Windows/Linux) ਜਾਂ `Cmd+Shift+P` (macOS) ਦਬਾਓ
   - "AI Chat" ਲਿਖੋ ਅਤੇ "AI Chat: Open Chat" ਚੁਣੋ

3. **MCP ਸਰਵਰ ਕਨੈਕਸ਼ਨ ਟੈਸਟ ਕਰੋ**:
   - AI Chat ਵਿੱਚ, `#zava` ਲਿਖੋ ਅਤੇ ਕਨਫਿਗਰ ਕੀਤੇ ਸਰਵਰਾਂ ਵਿੱਚੋਂ ਇੱਕ ਚੁਣੋ
   - ਪੁੱਛੋ: "ਡਾਟਾਬੇਸ ਵਿੱਚ ਕਿਹੜੀਆਂ ਟੇਬਲਾਂ ਉਪਲਬਧ ਹਨ?"
   - ਤੁਹਾਨੂੰ ਰਿਟੇਲ ਡਾਟਾਬੇਸ ਟੇਬਲਾਂ ਦੀ ਸੂਚੀ ਪ੍ਰਾਪਤ ਹੋਣੀ ਚਾਹੀਦੀ ਹੈ

## ✅ ਵਾਤਾਵਰਣ ਵੈਰੀਫਿਕੇਸ਼ਨ

### 1. ਵਿਸਤ੍ਰਿਤ ਸਿਸਟਮ ਜਾਂਚ

ਆਪਣੇ ਸੈਟਅੱਪ ਦੀ ਪੁਸ਼ਟੀ ਕਰਨ ਲਈ ਇਹ ਵੈਰੀਫਿਕੇਸ਼ਨ ਸਕ੍ਰਿਪਟ ਚਲਾਓ:

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

### 2. ਮੈਨੂਅਲ ਵੈਰੀਫਿਕੇਸ਼ਨ ਚੈੱਕਲਿਸਟ

**✅ ਬੁਨਿਆਦੀ ਟੂਲ**
- [ ] Docker ਵਰਜਨ 20.10+ ਇੰਸਟਾਲ ਅਤੇ ਚਲ ਰਿਹਾ ਹੈ
- [ ] Azure CLI 2.40+ ਇੰਸਟਾਲ ਅਤੇ ਪ੍ਰਮਾਣਿਤ
- [ ] Python 3.8+ pip ਨਾਲ ਇੰਸਟਾਲ
- [ ] Git 2.30+ ਇੰਸਟਾਲ
- [ ] VS Code ਲੋੜੀਂਦੇ ਐਕਸਟੈਂਸ਼ਨ ਨਾਲ

**✅ Azure ਸਰੋਤ**
- [ ] ਰਿਸੋਰਸ ਗਰੁੱਪ ਸਫਲਤਾਪੂਰਵਕ ਬਣਾਇਆ ਗਿਆ
- [ ] AI Foundry ਪ੍ਰੋਜੈਕਟ ਤੈਨਾਤ ਕੀਤਾ
- [ ] OpenAI text-embedding-3-small ਮਾਡਲ ਤੈਨਾਤ ਕੀਤਾ
- [ ] Application Insights ਕਨਫਿਗਰ ਕੀਤਾ
- [ ] ਸੇਵਾ ਪ੍ਰਿੰਸਿਪਲ ਸਹੀ ਅਧਿਕਾਰਾਂ ਨਾਲ ਬਣਾਇਆ

**✅ ਵਾਤਾਵਰਣ ਕਨਫਿਗਰੇਸ਼ਨ**
- [ ] `.env` ਫਾਈਲ ਸਾਰੇ ਲੋੜੀਂਦੇ ਵੈਰੀਏਬਲਾਂ ਨਾਲ ਬਣਾਈ
- [ ] Azure ਪ੍ਰਮਾਣਿਕਤਾ ਕੰਮ ਕਰ ਰਹੀ ਹੈ (ਟੈਸਟ `az account show` ਨਾਲ)
- [ ] PostgreSQL ਕੰਟੇਨਰ ਚਲ ਰਿਹਾ ਹੈ ਅਤੇ ਪਹੁੰਚਯੋਗ ਹੈ
- [ ] ਡਾਟਾਬੇਸ ਵਿੱਚ ਸੈਂਪਲ ਡਾਟਾ ਲੋਡ ਕੀਤਾ

**✅ VS Code ਇੰਟੀਗ੍ਰੇਸ਼ਨ**
- [ ] `.vscode/mcp.json` ਕਨਫਿਗਰ ਕੀਤਾ
- [ ] Python interpreter ਵਰਚੁਅਲ ਵਾਤਾਵਰਣ 'ਤੇ ਸੈਟ ਕੀਤਾ
- [ ] MCP ਸਰਵਰ AI Chat ਵਿੱਚ ਦਿਖਾਈ ਦੇ ਰਹੇ ਹਨ
- [ ] AI Chat ਰਾਹੀਂ ਟੈਸਟ ਕਵੈਰੀਜ਼ ਚਲਾ ਸਕਦੇ ਹੋ

## 🛠️ ਆਮ ਸਮੱਸਿਆਵਾਂ ਦਾ ਹੱਲ

### Docker ਸਮੱਸਿਆਵਾਂ

**ਸਮੱਸਿਆ**: Docker ਕੰਟੇਨਰ ਸ਼ੁਰੂ ਨਹੀਂ ਹੁੰਦੇ
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

**ਸਮੱਸਿਆ**: PostgreSQL ਕਨੈਕਸ਼ਨ ਫੇਲ੍ਹ ਹੋ ਜਾਂਦਾ ਹੈ
```bash
# Check container logs
docker-compose logs postgres

# Verify container is healthy
docker-compose ps

# Test direct connection
docker-compose exec postgres psql -U postgres -d zava -c "SELECT 1;"
```

### Azure ਤੈਨਾਤੀ ਸਮੱਸਿਆਵਾਂ

**ਸਮੱਸਿਆ**: Azure ਤੈਨਾਤੀ ਫੇਲ੍ਹ ਹੋ ਜਾਂਦੀ ਹੈ
```bash
# Check Azure CLI authentication
az account show

# Verify subscription permissions
az role assignment list --assignee $(az account show --query user.name -o tsv)

# Check resource provider registration
az provider register --namespace Microsoft.CognitiveServices
az provider register --namespace Microsoft.Insights
```

**ਸਮੱਸਿਆ**: AI ਸੇਵਾ ਪ੍ਰਮਾਣਿਕਤਾ ਫੇਲ੍ਹ ਹੋ ਜਾਂਦੀ ਹੈ
```bash
# Test service principal
az login --service-principal \
  --username $AZURE_CLIENT_ID \
  --password $AZURE_CLIENT_SECRET \
  --tenant $AZURE_TENANT_ID

# Verify AI service deployment
az cognitiveservices account list --query "[].{Name:name,Kind:kind,Location:location}"
```

### Python ਵਾਤਾਵਰਣ ਸਮੱਸਿਆਵਾਂ

**ਸਮੱਸਿਆ**: ਪੈਕੇਜ ਇੰਸਟਾਲੇਸ਼ਨ ਫੇਲ੍ਹ ਹੋ ਜਾਂਦੀ ਹੈ
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

**ਸਮੱਸਿਆ**: VS Code Python interpreter ਨਹੀਂ ਲੱਭ ਸਕਦਾ
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

## 🎯 ਮੁੱਖ ਸਿੱਖਣ

ਇਸ ਲੈਬ ਨੂੰ ਪੂਰਾ ਕਰਨ ਤੋਂ ਬਾਅਦ, ਤੁਹਾਡੇ ਕੋਲ ਹੋਣਾ ਚਾਹੀਦਾ ਹੈ:

✅ **ਪੂਰਾ ਵਿਕਾਸ ਵਾਤਾਵਰਣ**: ਸਾਰੇ ਟੂਲ ਇੰਸਟਾਲ ਅਤੇ ਕਨਫਿਗਰ  
✅ **Azure ਸਰੋਤ ਤੈਨਾਤ ਕੀਤੇ**: AI ਸੇਵਾਵਾਂ ਅਤੇ ਸਹਾਇਕ ਢਾਂਚਾ  
✅ **Docker ਵਾਤਾਵਰਣ ਚੱਲ ਰਿਹਾ**: PostgreSQL ਅਤੇ MCP ਸਰਵਰ ਕੰਟੇਨਰ  
✅ **VS Code ਇੰਟੀਗ੍ਰੇਸ਼ਨ**: MCP ਸਰਵਰ ਕਨਫਿਗਰ ਅਤੇ ਪਹੁੰਚਯੋਗ  
✅ **ਸੈਟਅੱਪ ਦੀ ਪੁਸ਼ਟੀ ਕੀਤੀ**: ਸਾਰੇ ਘਟਕਾਂ ਨੂੰ ਟੈਸਟ ਕੀਤਾ ਅਤੇ ਇਕੱਠੇ ਕੰਮ ਕਰਦੇ  
✅ **ਸਮੱਸਿਆਵਾਂ ਦਾ ਹੱਲ ਜਾਣਕਾਰੀ**: ਆਮ ਸਮੱਸਿਆਵਾਂ ਅਤੇ ਹੱਲ  

## 🚀 ਅਗਲਾ ਕੀ ਹੈ

ਆਪਣੇ ਵਾਤਾਵਰਣ ਨੂੰ ਤਿਆਰ ਕਰਕੇ, **[ਲੈਬ 04: ਡਾਟਾਬੇਸ ਡਿਜ਼ਾਈਨ ਅਤੇ ਸਕੀਮਾ](../04-Database/README.md)** ਨਾਲ ਜਾਰੀ ਰੱਖੋ:

- ਰਿਟੇਲ ਡਾਟਾਬੇਸ ਸਕੀਮਾ ਨੂੰ ਵਿਸਤ੍ਰਿਤ ਤੌਰ 'ਤੇ ਖੋਜੋ
- ਮਲਟੀ-ਟੈਨੈਂਟ ਡਾਟਾ ਮਾਡਲਿੰਗ ਨੂੰ ਸਮਝੋ
- Row Level Security ਅਮਲਬੰਦੀ ਬਾਰੇ ਸਿੱਖੋ
- ਸੈਂਪਲ ਰਿਟੇਲ ਡਾਟਾ ਨਾਲ ਕੰਮ ਕਰੋ

## 📚 ਵਾਧੂ ਸਰੋਤ

### ਵਿਕਾਸ ਟੂਲ
- [Docker Documentation](https://docs.docker.com/) - ਪੂਰੀ Docker ਰਿਫਰੈਂਸ
- [Azure CLI Reference](https://docs.microsoft.com/cli/azure/) - Azure CLI ਕਮਾਂਡ
- [VS Code Documentation](https://code.visualstudio.com/docs) - ਐਡੀਟਰ ਕਨਫਿਗਰੇਸ਼ਨ ਅਤੇ ਐਕਸਟੈਂਸ਼ਨ

### Azure ਸੇਵਾਵਾਂ
- [Azure AI Foundry Documentation](https://docs.microsoft.com/azure/ai-foundry/) - AI ਸੇਵਾ ਕਨਫਿਗਰੇਸ਼ਨ
- [Azure OpenAI Service](https://docs.microsoft.com/azure/cognitive-services/openai/) - AI ਮਾਡਲ ਤੈਨਾਤੀ
- [Application Insights](https://docs.microsoft.com/azure/azure-monitor/app/app-insights-overview) - ਮਾਨੀਟਰਿੰਗ ਸੈਟਅੱਪ

### Python ਵਿਕਾਸ
- [Python Virtual Environments](https://docs.python.org/3/tutorial/venv.html) - ਵਾਤਾਵਰਣ ਪ੍ਰਬੰਧਨ
- [AsyncIO Documentation](https://docs.python.org/3/library/asyncio.html) - Async ਪ੍ਰੋਗਰਾਮਿੰਗ ਪੈਟਰਨ
- [FastAPI Documentation](https://fastapi.tiangolo.com/) - ਵੈੱਬ ਫਰੇਮਵਰਕ ਪੈਟਰਨ

---

**ਅਗਲਾ**: ਵਾਤਾਵਰਣ

---

**ਅਸਵੀਕਰਤੀ**:  
ਇਹ ਦਸਤਾਵੇਜ਼ AI ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਅਨੁਵਾਦ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀਤਾ ਲਈ ਯਤਨਸ਼ੀਲ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਦਿਓ ਕਿ ਸਵੈਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸੁਚੀਤਤਾਵਾਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਇਸ ਦੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਮੌਜੂਦ ਦਸਤਾਵੇਜ਼ ਨੂੰ ਅਧਿਕਾਰਤ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਮਹੱਤਵਪੂਰਨ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਅਸੀਂ ਇਸ ਅਨੁਵਾਦ ਦੀ ਵਰਤੋਂ ਤੋਂ ਪੈਦਾ ਹੋਣ ਵਾਲੇ ਕਿਸੇ ਵੀ ਗਲਤਫਹਿਮੀ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆ ਲਈ ਜ਼ਿੰਮੇਵਾਰ ਨਹੀਂ ਹਾਂ।