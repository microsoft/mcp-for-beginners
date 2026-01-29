# Environment Setup

## 🎯 What This Lab Covers

This hands-on lab walks you through setting up a complete development environment for building MCP servers with PostgreSQL integration. You'll configure all necessary tools, deploy Azure resources, and validate your setup before moving forward with implementation.

## Overview

A well-configured development environment is essential for successful MCP server development. This lab provides step-by-step instructions for setting up Docker, Azure services, development tools, and ensuring everything works seamlessly together.

By the end of this lab, you'll have a fully operational development environment ready for building the Zava Retail MCP server.

## Learning Objectives

By the end of this lab, you will be able to:

- **Install and configure** all required development tools
- **Deploy Azure resources** necessary for the MCP server
- **Set up Docker containers** for PostgreSQL and the MCP server
- **Validate** your environment setup with test connections
- **Troubleshoot** common setup and configuration issues
- **Understand** the development workflow and file structure

## 📋 Prerequisites Check

Before starting, ensure you have:

### Required Knowledge
- Basic command line usage (Windows Command Prompt/PowerShell)
- Understanding of environment variables
- Familiarity with Git version control
- Basic Docker concepts (containers, images, volumes)

### System Requirements
- **Operating System**: Windows 10/11, macOS, or Linux
- **RAM**: Minimum 8GB (16GB recommended)
- **Storage**: At least 10GB free space
- **Network**: Internet connection for downloads and Azure deployment

### Account Requirements
- **Azure Subscription**: Free tier is sufficient
- **GitHub Account**: For repository access
- **Docker Hub Account**: (Optional) For custom image publishing

## 🛠️ Tool Installation

### 1. Install Docker Desktop

Docker provides the containerized environment for our development setup.

#### Windows Installation

1. **Download Docker Desktop**:
   ```cmd
   # Visit https://desktop.docker.com/win/stable/Docker%20Desktop%20Installer.exe
   # Or use Windows Package Manager
   winget install Docker.DockerDesktop
   ```

2. **Install and Configure**:
   - Run the installer as Administrator
   - Enable WSL 2 integration when prompted
   - Restart your computer after installation completes

3. **Verify Installation**:
   ```cmd
   docker --version
   docker-compose --version
   ```

#### macOS Installation

1. **Download and Install**:
   ```bash
   # Download from https://desktop.docker.com/mac/stable/Docker.dmg
   # Or use Homebrew
   brew install --cask docker
   ```

2. **Start Docker Desktop**:
   - Launch Docker Desktop from Applications
   - Complete the initial setup wizard

3. **Verify Installation**:
   ```bash
   docker --version
   docker-compose --version
   ```

#### Linux Installation

1. **Install Docker Engine**:
   ```bash
   # Ubuntu/Debian
   curl -fsSL https://get.docker.com -o get-docker.sh
   sudo sh get-docker.sh
   sudo usermod -aG docker $USER
   
   # Log out and back in for group changes to take effect
   ```

2. **Install Docker Compose**:
   ```bash
   sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
   sudo chmod +x /usr/local/bin/docker-compose
   ```

### 2. Install Azure CLI

The Azure CLI enables deployment and management of Azure resources.

#### Windows Installation

```cmd
# Using Windows Package Manager
winget install Microsoft.AzureCLI

# Or download MSI from: https://aka.ms/installazurecliwindows
```

#### macOS Installation

```bash
# Using Homebrew
brew install azure-cli

# Or using installer
curl -L https://aka.ms/InstallAzureCli | bash
```

#### Linux Installation

```bash
# Ubuntu/Debian
curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash

# RHEL/CentOS
sudo rpm --import https://packages.microsoft.com/keys/microsoft.asc
sudo dnf install azure-cli
```

#### Verify and Authenticate

```bash
# Check installation
az version

# Login to Azure
az login

# Set default subscription (if you have multiple)
az account list --output table
az account set --subscription "Your-Subscription-Name"
```

### 3. Install Git

Git is required for cloning the repository and version control.

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

### 4. Install VS Code

Visual Studio Code provides the integrated development environment with MCP support.

#### Installation

```cmd
# Windows
winget install Microsoft.VisualStudioCode

# macOS
brew install --cask visual-studio-code

# Linux (Ubuntu/Debian)
sudo snap install code --classic
```

#### Required Extensions

Install these VS Code extensions:

```bash
# Install via command line
code --install-extension ms-python.python
code --install-extension ms-vscode.vscode-json
code --install-extension ms-azuretools.vscode-docker
code --install-extension ms-vscode.azure-account
```

Or install through VS Code:
1. Open VS Code
2. Go to Extensions (Ctrl+Shift+X)
3. Install:
   - **Python** (Microsoft)
   - **Docker** (Microsoft)
   - **Azure Account** (Microsoft)
   - **JSON** (Microsoft)

### 5. Install Python

Python 3.8+ is required for MCP server development.

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

#### Verify Installation

```bash
python --version  # Should show Python 3.11.x
pip --version      # Should show pip version
```

## 🚀 Project Setup

### 1. Clone the Repository

```bash
# Clone the main repository
git clone https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail.git

# Navigate to the project directory
cd MCP-Server-and-PostgreSQL-Sample-Retail

# Verify repository structure
ls -la
```

### 2. Create Python Virtual Environment

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

### 3. Install Python Dependencies

```bash
# Install development dependencies
pip install -r requirements.lock.txt

# Verify key packages
pip list | grep fastmcp
pip list | grep asyncpg
pip list | grep azure
```

## ☁️ Azure Resource Deployment

### 1. Understand Resource Requirements

Our MCP server requires these Azure resources:

| **Resource** | **Purpose** | **Estimated Cost** |
|--------------|-------------|-------------------|
| **Azure AI Foundry** | AI model hosting and management | $10-50/month |
| **OpenAI Deployment** | Text embedding model (text-embedding-3-small) | $5-20/month |
| **Application Insights** | Monitoring and telemetry | $5-15/month |
| **Resource Group** | Resource organization | Free |

### 2. Deploy Azure Resources

#### Option A: Automated Deployment (Recommended)

```bash
# Navigate to infrastructure directory
cd infra

# Windows - PowerShell
./deploy.ps1

# macOS/Linux - Bash
./deploy.sh
```

The deployment script will:
1. Create a unique resource group
2. Deploy Azure AI Foundry resources
3. Deploy the text-embedding-3-small model
4. Configure Application Insights
5. Create a service principal for authentication
6. Generate `.env` file with configuration

#### Option B: Manual Deployment

If you prefer manual control or the automated script fails:

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

### 3. Verify Azure Deployment

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

### 4. Configure Environment Variables

After deployment, you should have a `.env` file. Verify it contains:

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

## 🐳 Docker Environment Setup

### 1. Understand Docker Composition

Our development environment uses Docker Compose:

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

### 2. Start the Development Environment

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

### 3. Verify Database Setup

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

### 4. Test MCP Server

```bash
# Check MCP server health
curl http://localhost:8000/health

# Test basic MCP endpoint
curl -X POST http://localhost:8000/mcp \
  -H "Content-Type: application/json" \
  -H "x-rls-user-id: 00000000-0000-0000-0000-000000000000" \
  -d '{"method": "tools/list", "params": {}}'
```

## 🔧 VS Code Configuration

### 1. Configure MCP Integration

Create VS Code MCP configuration:

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

### 2. Configure Python Environment

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

### 3. Test VS Code Integration

1. **Open the project in VS Code**:
   ```bash
   code .
   ```

2. **Open AI Chat**:
   - Press `Ctrl+Shift+P` (Windows/Linux) or `Cmd+Shift+P` (macOS)
   - Type "AI Chat" and select "AI Chat: Open Chat"

3. **Test MCP Server Connection**:
   - In AI Chat, type `#zava` and select one of the configured servers
   - Ask: "What tables are available in the database?"
   - You should receive a response listing the retail database tables

## ✅ Environment Validation

### 1. Comprehensive System Check

Run this validation script to verify your setup:

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

### 2. Manual Validation Checklist

**✅ Basic Tools**
- [ ] Docker version 20.10+ installed and running
- [ ] Azure CLI 2.40+ installed and authenticated
- [ ] Python 3.8+ with pip installed
- [ ] Git 2.30+ installed
- [ ] VS Code with required extensions

**✅ Azure Resources**
- [ ] Resource group created successfully
- [ ] AI Foundry project deployed
- [ ] OpenAI text-embedding-3-small model deployed
- [ ] Application Insights configured
- [ ] Service principal created with proper permissions

**✅ Environment Configuration**
- [ ] `.env` file created with all required variables
- [ ] Azure credentials working (test with `az account show`)
- [ ] PostgreSQL container running and accessible
- [ ] Sample data loaded in database

**✅ VS Code Integration**
- [ ] `.vscode/mcp.json` configured
- [ ] Python interpreter set to virtual environment
- [ ] MCP servers appear in AI Chat
- [ ] Can execute test queries through AI Chat

## 🛠️ Troubleshooting Common Issues

### Docker Issues

**Problem**: Docker containers won't start
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

**Problem**: PostgreSQL connection fails
```bash
# Check container logs
docker-compose logs postgres

# Verify container is healthy
docker-compose ps

# Test direct connection
docker-compose exec postgres psql -U postgres -d zava -c "SELECT 1;"
```

### Azure Deployment Issues

**Problem**: Azure deployment fails
```bash
# Check Azure CLI authentication
az account show

# Verify subscription permissions
az role assignment list --assignee $(az account show --query user.name -o tsv)

# Check resource provider registration
az provider register --namespace Microsoft.CognitiveServices
az provider register --namespace Microsoft.Insights
```

**Problem**: AI service authentication fails
```bash
# Test service principal
az login --service-principal \
  --username $AZURE_CLIENT_ID \
  --password $AZURE_CLIENT_SECRET \
  --tenant $AZURE_TENANT_ID

# Verify AI service deployment
az cognitiveservices account list --query "[].{Name:name,Kind:kind,Location:location}"
```

### Python Environment Issues

**Problem**: Package installation fails
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

**Problem**: VS Code can't find Python interpreter
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

## 🎯 Key Takeaways

After completing this lab, you should have:

✅ **Complete Development Environment**: All tools installed and configured  
✅ **Azure Resources Deployed**: AI services and supporting infrastructure  
✅ **Docker Environment Running**: PostgreSQL and MCP server containers  
✅ **VS Code Integration**: MCP servers configured and accessible  
✅ **Validated Setup**: All components tested and working together  
✅ **Troubleshooting Knowledge**: Common issues and solutions  

## 🚀 What's Next

With your environment ready, continue to **[Lab 04: Database Design and Schema](../04-Database/README.md)** to:

- Explore the retail database schema in detail
- Understand multi-tenant data modeling
- Learn about Row Level Security implementation
- Work with sample retail data

## 📚 Additional Resources

### Development Tools
- [Docker Documentation](https://docs.docker.com/) - Complete Docker reference
- [Azure CLI Reference](https://docs.microsoft.com/cli/azure/) - Azure CLI commands
- [VS Code Documentation](https://code.visualstudio.com/docs) - Editor configuration and extensions

### Azure Services
- [Azure AI Foundry Documentation](https://docs.microsoft.com/azure/ai-foundry/) - AI service configuration
- [Azure OpenAI Service](https://docs.microsoft.com/azure/cognitive-services/openai/) - AI model deployment
- [Application Insights](https://docs.microsoft.com/azure/azure-monitor/app/app-insights-overview) - Monitoring setup

### Python Development
- [Python Virtual Environments](https://docs.python.org/3/tutorial/venv.html) - Environment management
- [AsyncIO Documentation](https://docs.python.org/3/library/asyncio.html) - Async programming patterns
- [FastAPI Documentation](https://fastapi.tiangolo.com/) - Web framework patterns

---

**Next**: Environment ready? Continue with [Lab 04: Database Design and Schema](../04-Database/README.md)

---

**Disclaimer**:  
This document has been translated using the AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). While we aim for accuracy, please note that automated translations may contain errors or inaccuracies. The original document in its native language should be regarded as the authoritative source. For critical information, professional human translation is recommended. We are not responsible for any misunderstandings or misinterpretations resulting from the use of this translation.