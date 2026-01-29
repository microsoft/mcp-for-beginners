# Configuração do Ambiente

## 🎯 O Que Este Laboratório Abrange

Este laboratório prático orienta-o na configuração de um ambiente de desenvolvimento completo para criar servidores MCP com integração ao PostgreSQL. Irá configurar todas as ferramentas necessárias, implementar recursos no Azure e validar a sua configuração antes de prosseguir com a implementação.

## Visão Geral

Um ambiente de desenvolvimento adequado é essencial para o sucesso no desenvolvimento de servidores MCP. Este laboratório fornece instruções passo a passo para configurar o Docker, serviços do Azure, ferramentas de desenvolvimento e validar que tudo funciona corretamente em conjunto.

Ao final deste laboratório, terá um ambiente de desenvolvimento totalmente funcional, pronto para construir o servidor MCP da Zava Retail.

## Objetivos de Aprendizagem

Ao final deste laboratório, será capaz de:

- **Instalar e configurar** todas as ferramentas de desenvolvimento necessárias
- **Implementar recursos no Azure** necessários para o servidor MCP
- **Configurar contêineres Docker** para PostgreSQL e o servidor MCP
- **Validar** a configuração do ambiente com conexões de teste
- **Resolver problemas** comuns de configuração e instalação
- **Compreender** o fluxo de trabalho de desenvolvimento e a estrutura de arquivos

## 📋 Verificação de Pré-Requisitos

Antes de começar, certifique-se de ter:

### Conhecimentos Necessários
- Uso básico da linha de comandos (Prompt de Comando do Windows/PowerShell)
- Compreensão de variáveis de ambiente
- Familiaridade com o controlo de versão Git
- Conceitos básicos de Docker (contêineres, imagens, volumes)

### Requisitos do Sistema
- **Sistema Operativo**: Windows 10/11, macOS ou Linux
- **RAM**: Mínimo de 8GB (recomendado 16GB)
- **Armazenamento**: Pelo menos 10GB de espaço livre
- **Rede**: Conexão à Internet para downloads e implementação no Azure

### Requisitos de Conta
- **Assinatura do Azure**: O nível gratuito é suficiente
- **Conta GitHub**: Para acesso ao repositório
- **Conta Docker Hub**: (Opcional) Para publicação de imagens personalizadas

## 🛠️ Instalação de Ferramentas

### 1. Instalar Docker Desktop

O Docker fornece o ambiente de contêiner necessário para nossa configuração de desenvolvimento.

#### Instalação no Windows

1. **Descarregar Docker Desktop**:
   ```cmd
   # Visit https://desktop.docker.com/win/stable/Docker%20Desktop%20Installer.exe
   # Or use Windows Package Manager
   winget install Docker.DockerDesktop
   ```

2. **Instalar e Configurar**:
   - Execute o instalador como Administrador
   - Ative a integração com WSL 2 quando solicitado
   - Reinicie o computador após a conclusão da instalação

3. **Verificar Instalação**:
   ```cmd
   docker --version
   docker-compose --version
   ```

#### Instalação no macOS

1. **Descarregar e Instalar**:
   ```bash
   # Download from https://desktop.docker.com/mac/stable/Docker.dmg
   # Or use Homebrew
   brew install --cask docker
   ```

2. **Iniciar Docker Desktop**:
   - Abra o Docker Desktop em Aplicações
   - Complete o assistente de configuração inicial

3. **Verificar Instalação**:
   ```bash
   docker --version
   docker-compose --version
   ```

#### Instalação no Linux

1. **Instalar Docker Engine**:
   ```bash
   # Ubuntu/Debian
   curl -fsSL https://get.docker.com -o get-docker.sh
   sudo sh get-docker.sh
   sudo usermod -aG docker $USER
   
   # Log out and back in for group changes to take effect
   ```

2. **Instalar Docker Compose**:
   ```bash
   sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
   sudo chmod +x /usr/local/bin/docker-compose
   ```

### 2. Instalar Azure CLI

O Azure CLI permite a implementação e gestão de recursos no Azure.

#### Instalação no Windows

```cmd
# Using Windows Package Manager
winget install Microsoft.AzureCLI

# Or download MSI from: https://aka.ms/installazurecliwindows
```

#### Instalação no macOS

```bash
# Using Homebrew
brew install azure-cli

# Or using installer
curl -L https://aka.ms/InstallAzureCli | bash
```

#### Instalação no Linux

```bash
# Ubuntu/Debian
curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash

# RHEL/CentOS
sudo rpm --import https://packages.microsoft.com/keys/microsoft.asc
sudo dnf install azure-cli
```

#### Verificar e Autenticar

```bash
# Check installation
az version

# Login to Azure
az login

# Set default subscription (if you have multiple)
az account list --output table
az account set --subscription "Your-Subscription-Name"
```

### 3. Instalar Git

O Git é necessário para clonar o repositório e controlo de versão.

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

### 4. Instalar VS Code

O Visual Studio Code fornece o ambiente de desenvolvimento integrado com suporte ao MCP.

#### Instalação

```cmd
# Windows
winget install Microsoft.VisualStudioCode

# macOS
brew install --cask visual-studio-code

# Linux (Ubuntu/Debian)
sudo snap install code --classic
```

#### Extensões Necessárias

Instale estas extensões do VS Code:

```bash
# Install via command line
code --install-extension ms-python.python
code --install-extension ms-vscode.vscode-json
code --install-extension ms-azuretools.vscode-docker
code --install-extension ms-vscode.azure-account
```

Ou instale através do VS Code:
1. Abra o VS Code
2. Vá para Extensões (Ctrl+Shift+X)
3. Instale:
   - **Python** (Microsoft)
   - **Docker** (Microsoft)
   - **Azure Account** (Microsoft)
   - **JSON** (Microsoft)

### 5. Instalar Python

Python 3.8+ é necessário para o desenvolvimento do servidor MCP.

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

#### Verificar Instalação

```bash
python --version  # Should show Python 3.11.x
pip --version      # Should show pip version
```

## 🚀 Configuração do Projeto

### 1. Clonar o Repositório

```bash
# Clone the main repository
git clone https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail.git

# Navigate to the project directory
cd MCP-Server-and-PostgreSQL-Sample-Retail

# Verify repository structure
ls -la
```

### 2. Criar Ambiente Virtual Python

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

### 3. Instalar Dependências Python

```bash
# Install development dependencies
pip install -r requirements.lock.txt

# Verify key packages
pip list | grep fastmcp
pip list | grep asyncpg
pip list | grep azure
```

## ☁️ Implementação de Recursos no Azure

### 1. Compreender os Requisitos de Recursos

O nosso servidor MCP requer os seguintes recursos no Azure:

| **Recurso** | **Finalidade** | **Custo Estimado** |
|-------------|----------------|--------------------|
| **Azure AI Foundry** | Hospedagem e gestão de modelos de IA | $10-50/mês |
| **Implementação OpenAI** | Modelo de incorporação de texto (text-embedding-3-small) | $5-20/mês |
| **Application Insights** | Monitorização e telemetria | $5-15/mês |
| **Resource Group** | Organização de recursos | Gratuito |

### 2. Implementar Recursos no Azure

#### Opção A: Implementação Automática (Recomendada)

```bash
# Navigate to infrastructure directory
cd infra

# Windows - PowerShell
./deploy.ps1

# macOS/Linux - Bash
./deploy.sh
```

O script de implementação irá:
1. Criar um grupo de recursos único
2. Implementar recursos do Azure AI Foundry
3. Implementar o modelo text-embedding-3-small
4. Configurar o Application Insights
5. Criar um principal de serviço para autenticação
6. Gerar o ficheiro `.env` com a configuração

#### Opção B: Implementação Manual

Se preferir controlo manual ou o script automático falhar:

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

### 3. Verificar Implementação no Azure

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

### 4. Configurar Variáveis de Ambiente

Após a implementação, deverá ter um ficheiro `.env`. Verifique se contém:

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

## 🐳 Configuração do Ambiente Docker

### 1. Compreender a Composição Docker

O nosso ambiente de desenvolvimento utiliza Docker Compose:

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

### 2. Iniciar o Ambiente de Desenvolvimento

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

### 3. Verificar Configuração da Base de Dados

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

### 4. Testar o Servidor MCP

```bash
# Check MCP server health
curl http://localhost:8000/health

# Test basic MCP endpoint
curl -X POST http://localhost:8000/mcp \
  -H "Content-Type: application/json" \
  -H "x-rls-user-id: 00000000-0000-0000-0000-000000000000" \
  -d '{"method": "tools/list", "params": {}}'
```

## 🔧 Configuração do VS Code

### 1. Configurar Integração MCP

Crie a configuração MCP no VS Code:

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

### 2. Configurar Ambiente Python

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

### 3. Testar Integração com VS Code

1. **Abra o projeto no VS Code**:
   ```bash
   code .
   ```

2. **Abrir Chat de IA**:
   - Pressione `Ctrl+Shift+P` (Windows/Linux) ou `Cmd+Shift+P` (macOS)
   - Escreva "AI Chat" e selecione "AI Chat: Open Chat"

3. **Testar Conexão com o Servidor MCP**:
   - No Chat de IA, escreva `#zava` e selecione um dos servidores configurados
   - Pergunte: "Quais tabelas estão disponíveis na base de dados?"
   - Deverá receber uma resposta listando as tabelas da base de dados de retalho

## ✅ Validação do Ambiente

### 1. Verificação Completa do Sistema

Execute este script de validação para verificar a sua configuração:

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

### 2. Lista de Verificação Manual

**✅ Ferramentas Básicas**
- [ ] Docker versão 20.10+ instalado e em execução
- [ ] Azure CLI 2.40+ instalado e autenticado
- [ ] Python 3.8+ com pip instalado
- [ ] Git 2.30+ instalado
- [ ] VS Code com extensões necessárias

**✅ Recursos do Azure**
- [ ] Grupo de recursos criado com sucesso
- [ ] Projeto AI Foundry implementado
- [ ] Modelo OpenAI text-embedding-3-small implementado
- [ ] Application Insights configurado
- [ ] Principal de serviço criado com permissões adequadas

**✅ Configuração do Ambiente**
- [ ] Ficheiro `.env` criado com todas as variáveis necessárias
- [ ] Credenciais do Azure funcionando (teste com `az account show`)
- [ ] Contêiner PostgreSQL em execução e acessível
- [ ] Dados de exemplo carregados na base de dados

**✅ Integração com VS Code**
- [ ] `.vscode/mcp.json` configurado
- [ ] Interpretador Python definido para o ambiente virtual
- [ ] Servidores MCP aparecem no Chat de IA
- [ ] Capaz de executar consultas de teste através do Chat de IA

## 🛠️ Resolução de Problemas Comuns

### Problemas com Docker

**Problema**: Contêineres Docker não iniciam
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

**Problema**: Falha na conexão com PostgreSQL
```bash
# Check container logs
docker-compose logs postgres

# Verify container is healthy
docker-compose ps

# Test direct connection
docker-compose exec postgres psql -U postgres -d zava -c "SELECT 1;"
```

### Problemas com Implementação no Azure

**Problema**: Falha na implementação no Azure
```bash
# Check Azure CLI authentication
az account show

# Verify subscription permissions
az role assignment list --assignee $(az account show --query user.name -o tsv)

# Check resource provider registration
az provider register --namespace Microsoft.CognitiveServices
az provider register --namespace Microsoft.Insights
```

**Problema**: Falha na autenticação do serviço de IA
```bash
# Test service principal
az login --service-principal \
  --username $AZURE_CLIENT_ID \
  --password $AZURE_CLIENT_SECRET \
  --tenant $AZURE_TENANT_ID

# Verify AI service deployment
az cognitiveservices account list --query "[].{Name:name,Kind:kind,Location:location}"
```

### Problemas com Ambiente Python

**Problema**: Falha na instalação de pacotes
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

**Problema**: VS Code não encontra o interpretador Python
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

## 🎯 Principais Conclusões

Após completar este laboratório, deverá ter:

✅ **Ambiente de Desenvolvimento Completo**: Todas as ferramentas instaladas e configuradas  
✅ **Recursos do Azure Implementados**: Serviços de IA e infraestrutura de suporte  
✅ **Ambiente Docker em Funcionamento**: Contêineres PostgreSQL e servidor MCP  
✅ **Integração com VS Code**: Servidores MCP configurados e acessíveis  
✅ **Configuração Validada**: Todos os componentes testados e funcionando em conjunto  
✅ **Conhecimento de Resolução de Problemas**: Problemas comuns e soluções  

## 🚀 Próximos Passos

Com o seu ambiente pronto, continue para **[Laboratório 04: Design e Esquema da Base de Dados](../04-Database/README.md)** para:

- Explorar o esquema da base de dados de retalho em detalhe
- Compreender o modelo de dados multi-inquilino
- Aprender sobre a implementação de Segurança ao Nível de Linha
- Trabalhar com dados de exemplo de retalho

## 📚 Recursos Adicionais

### Ferramentas de Desenvolvimento
- [Documentação do Docker](https://docs.docker.com/) - Referência completa do Docker
- [Referência do Azure CLI](https://docs.microsoft.com/cli/azure/) - Comandos do Azure CLI
- [Documentação do VS Code](https://code.visualstudio.com/docs) - Configuração do editor e extensões

### Serviços do Azure
- [Documentação do Azure AI Foundry](https://docs.microsoft.com/azure/ai-foundry/) - Configuração de serviços de IA
- [Serviço OpenAI do Azure](https://docs.microsoft.com/azure/cognitive-services/openai/) - Implementação de modelos de IA
- [Application Insights](https://docs.microsoft.com/azure/azure-monitor/app/app-insights-overview) - Configuração de monitorização

### Desenvolvimento em Python
- [Ambientes Virtuais Python](https://docs.python.org/3/tutorial/venv.html) - Gestão de ambientes
- [Documentação AsyncIO](https://docs.python.org/3/library/asyncio.html) - Padrões de programação assíncrona
- [Documentação do FastAPI](https://fastapi.tiangolo.com/) - Padrões de framework web

---

**Próximo**: Ambiente pronto? Continue com [Laboratório 04: Design e Esquema da Base de Dados](../04-Database/README.md)

---

**Aviso**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, é importante notar que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autoritária. Para informações críticas, recomenda-se a tradução profissional realizada por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes da utilização desta tradução.