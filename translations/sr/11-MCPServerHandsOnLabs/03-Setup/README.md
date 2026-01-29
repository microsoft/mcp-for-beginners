# Подешавање окружења

## 🎯 Шта овај практични рад покрива

Овај практични рад вас води кроз процес постављања комплетног развојног окружења за изградњу MCP сервера са интеграцијом PostgreSQL-а. Конфигурисаћете све потребне алате, распоредити Azure ресурсе и проверити исправност подешавања пре него што наставите са имплементацијом.

## Преглед

Правилно развојно окружење је кључно за успешан развој MCP сервера. Овај практични рад пружа корак-по-корак упутства за постављање Docker-а, Azure услуга, развојних алата и проверу да ли све функционише исправно.

На крају овог практичног рада, имаћете потпуно функционално развојно окружење спремно за изградњу Zava Retail MCP сервера.

## Циљеви учења

На крају овог практичног рада, моћи ћете да:

- **Инсталирате и конфигуришете** све потребне развојне алате
- **Распоредите Azure ресурсе** потребне за MCP сервер
- **Поставите Docker контејнере** за PostgreSQL и MCP сервер
- **Проверите** исправност подешавања окружења тест конекцијама
- **Решавате проблеме** са подешавањем и конфигурацијом
- **Разумете** развојни ток и структуру датотека

## 📋 Провера предуслова

Пре почетка, уверите се да имате:

### Потребно знање
- Основно коришћење командне линије (Windows Command Prompt/PowerShell)
- Разумевање променљивих окружења
- Познавање Git верзионисања
- Основни концепти Docker-а (контејнери, слике, волумени)

### Системски захтеви
- **Оперативни систем**: Windows 10/11, macOS или Linux
- **RAM**: Минимум 8GB (препоручено 16GB)
- **Складиште**: Најмање 10GB слободног простора
- **Мрежа**: Интернет конекција за преузимања и Azure распоређивање

### Захтеви за налоге
- **Azure претплата**: Бесплатни ниво је довољан
- **GitHub налог**: За приступ репозиторијуму
- **Docker Hub налог**: (Опционално) За објављивање прилагођених слика

## 🛠️ Инсталација алата

### 1. Инсталирајте Docker Desktop

Docker обезбеђује окружење са контејнерима за наше развојно подешавање.

#### Инсталација на Windows-у

1. **Преузмите Docker Desktop**:
   ```cmd
   # Visit https://desktop.docker.com/win/stable/Docker%20Desktop%20Installer.exe
   # Or use Windows Package Manager
   winget install Docker.DockerDesktop
   ```

2. **Инсталирајте и конфигуришите**:
   - Покрените инсталер као администратор
   - Омогућите WSL 2 интеграцију када се то затражи
   - Поново покрените рачунар након завршетка инсталације

3. **Проверите инсталацију**:
   ```cmd
   docker --version
   docker-compose --version
   ```

#### Инсталација на macOS-у

1. **Преузмите и инсталирајте**:
   ```bash
   # Download from https://desktop.docker.com/mac/stable/Docker.dmg
   # Or use Homebrew
   brew install --cask docker
   ```

2. **Покрените Docker Desktop**:
   - Покрените Docker Desktop из Applications
   - Завршите почетни чаробњак за подешавање

3. **Проверите инсталацију**:
   ```bash
   docker --version
   docker-compose --version
   ```

#### Инсталација на Linux-у

1. **Инсталирајте Docker Engine**:
   ```bash
   # Ubuntu/Debian
   curl -fsSL https://get.docker.com -o get-docker.sh
   sudo sh get-docker.sh
   sudo usermod -aG docker $USER
   
   # Log out and back in for group changes to take effect
   ```

2. **Инсталирајте Docker Compose**:
   ```bash
   sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
   sudo chmod +x /usr/local/bin/docker-compose
   ```

### 2. Инсталирајте Azure CLI

Azure CLI омогућава распоређивање и управљање Azure ресурсима.

#### Инсталација на Windows-у

```cmd
# Using Windows Package Manager
winget install Microsoft.AzureCLI

# Or download MSI from: https://aka.ms/installazurecliwindows
```

#### Инсталација на macOS-у

```bash
# Using Homebrew
brew install azure-cli

# Or using installer
curl -L https://aka.ms/InstallAzureCli | bash
```

#### Инсталација на Linux-у

```bash
# Ubuntu/Debian
curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash

# RHEL/CentOS
sudo rpm --import https://packages.microsoft.com/keys/microsoft.asc
sudo dnf install azure-cli
```

#### Проверите и аутентификујте

```bash
# Check installation
az version

# Login to Azure
az login

# Set default subscription (if you have multiple)
az account list --output table
az account set --subscription "Your-Subscription-Name"
```

### 3. Инсталирајте Git

Git је потребан за клонирање репозиторијума и верзионисање.

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

### 4. Инсталирајте VS Code

Visual Studio Code обезбеђује интегрисано развојно окружење са подршком за MCP.

#### Инсталација

```cmd
# Windows
winget install Microsoft.VisualStudioCode

# macOS
brew install --cask visual-studio-code

# Linux (Ubuntu/Debian)
sudo snap install code --classic
```

#### Потребни екстензије

Инсталирајте ове VS Code екстензије:

```bash
# Install via command line
code --install-extension ms-python.python
code --install-extension ms-vscode.vscode-json
code --install-extension ms-azuretools.vscode-docker
code --install-extension ms-vscode.azure-account
```

Или инсталирајте преко VS Code-а:
1. Отворите VS Code
2. Идите на Extensions (Ctrl+Shift+X)
3. Инсталирајте:
   - **Python** (Microsoft)
   - **Docker** (Microsoft)
   - **Azure Account** (Microsoft)
   - **JSON** (Microsoft)

### 5. Инсталирајте Python

Python 3.8+ је потребан за развој MCP сервера.

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

#### Проверите инсталацију

```bash
python --version  # Should show Python 3.11.x
pip --version      # Should show pip version
```

## 🚀 Постављање пројекта

### 1. Клонирајте репозиторијум

```bash
# Clone the main repository
git clone https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail.git

# Navigate to the project directory
cd MCP-Server-and-PostgreSQL-Sample-Retail

# Verify repository structure
ls -la
```

### 2. Направите Python виртуелно окружење

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

### 3. Инсталирајте Python зависности

```bash
# Install development dependencies
pip install -r requirements.lock.txt

# Verify key packages
pip list | grep fastmcp
pip list | grep asyncpg
pip list | grep azure
```

## ☁️ Распоређивање Azure ресурса

### 1. Разумевање захтева за ресурсе

Наш MCP сервер захтева следеће Azure ресурсе:

| **Ресурс** | **Намена** | **Процењени трошак** |
|------------|------------|---------------------|
| **Azure AI Foundry** | Хостовање и управљање AI моделима | $10-50/месечно |
| **OpenAI Deployment** | Модел за текстуално уграђивање (text-embedding-3-small) | $5-20/месечно |
| **Application Insights** | Праћење и телеметрија | $5-15/месечно |
| **Resource Group** | Организација ресурса | Бесплатно |

### 2. Распоредите Azure ресурсе

#### Опција А: Аутоматизовано распоређивање (препоручено)

```bash
# Navigate to infrastructure directory
cd infra

# Windows - PowerShell
./deploy.ps1

# macOS/Linux - Bash
./deploy.sh
```

Скрипта за распоређивање ће:
1. Направити јединствену групу ресурса
2. Распоредити Azure AI Foundry ресурсе
3. Распоредити модел text-embedding-3-small
4. Конфигурисати Application Insights
5. Направити сервисни принципал за аутентификацију
6. Генерисати `.env` датотеку са конфигурацијом

#### Опција Б: Ручно распоређивање

Ако више волите ручну контролу или скрипта за аутоматизацију не успе:

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

### 3. Проверите Azure распоређивање

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

### 4. Конфигуришите променљиве окружења

Након распоређивања, требало би да имате `.env` датотеку. Проверите да садржи:

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

## 🐳 Постављање Docker окружења

### 1. Разумевање Docker композиције

Наше развојно окружење користи Docker Compose:

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

### 2. Покрените развојно окружење

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

### 3. Проверите постављање базе података

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

### 4. Тестирајте MCP сервер

```bash
# Check MCP server health
curl http://localhost:8000/health

# Test basic MCP endpoint
curl -X POST http://localhost:8000/mcp \
  -H "Content-Type: application/json" \
  -H "x-rls-user-id: 00000000-0000-0000-0000-000000000000" \
  -d '{"method": "tools/list", "params": {}}'
```

## 🔧 Конфигурација VS Code-а

### 1. Конфигуришите MCP интеграцију

Направите VS Code MCP конфигурацију:

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

### 2. Конфигуришите Python окружење

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

### 3. Тестирајте VS Code интеграцију

1. **Отворите пројекат у VS Code-у**:
   ```bash
   code .
   ```

2. **Отворите AI Chat**:
   - Притисните `Ctrl+Shift+P` (Windows/Linux) или `Cmd+Shift+P` (macOS)
   - Укуцајте "AI Chat" и изаберите "AI Chat: Open Chat"

3. **Тестирајте MCP сервер конекцију**:
   - У AI Chat-у, укуцајте `#zava` и изаберите један од конфигурисаних сервера
   - Питајте: "Које табеле су доступне у бази података?"
   - Требало би да добијете одговор са списком табела у малопродајној бази података

## ✅ Валидација окружења

### 1. Комплетна провера система

Покрените ову скрипту за валидацију да проверите своје подешавање:

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

### 2. Контролна листа за ручну валидацију

**✅ Основни алати**
- [ ] Инсталиран и покренут Docker верзије 20.10+
- [ ] Инсталиран и аутентификован Azure CLI 2.40+
- [ ] Инсталиран Python 3.8+ са pip-ом
- [ ] Инсталиран Git 2.30+
- [ ] VS Code са потребним екстензијама

**✅ Azure ресурси**
- [ ] Успешно креирана група ресурса
- [ ] Распоређен AI Foundry пројекат
- [ ] Распоређен OpenAI модел text-embedding-3-small
- [ ] Конфигурисан Application Insights
- [ ] Направљен сервисни принципал са одговарајућим дозволама

**✅ Конфигурација окружења**
- [ ] Направљена `.env` датотека са свим потребним променљивим
- [ ] Azure креденцијали функционишу (тестирајте са `az account show`)
- [ ] PostgreSQL контејнер ради и доступан је
- [ ] Учитани пример података у базу

**✅ VS Code интеграција**
- [ ] Конфигурисан `.vscode/mcp.json`
- [ ] Python интерпретер постављен на виртуелно окружење
- [ ] MCP сервери се појављују у AI Chat-у
- [ ] Могуће је извршити тест упите преко AI Chat-а

## 🛠️ Решавање уобичајених проблема

### Проблеми са Docker-ом

**Проблем**: Docker контејнери се не покрећу
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

**Проблем**: PostgreSQL конекција не успева
```bash
# Check container logs
docker-compose logs postgres

# Verify container is healthy
docker-compose ps

# Test direct connection
docker-compose exec postgres psql -U postgres -d zava -c "SELECT 1;"
```

### Проблеми са Azure распоређивањем

**Проблем**: Azure распоређивање не успева
```bash
# Check Azure CLI authentication
az account show

# Verify subscription permissions
az role assignment list --assignee $(az account show --query user.name -o tsv)

# Check resource provider registration
az provider register --namespace Microsoft.CognitiveServices
az provider register --namespace Microsoft.Insights
```

**Проблем**: Аутентификација AI услуге не успева
```bash
# Test service principal
az login --service-principal \
  --username $AZURE_CLIENT_ID \
  --password $AZURE_CLIENT_SECRET \
  --tenant $AZURE_TENANT_ID

# Verify AI service deployment
az cognitiveservices account list --query "[].{Name:name,Kind:kind,Location:location}"
```

### Проблеми са Python окружењем

**Проблем**: Инсталација пакета не успева
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

**Проблем**: VS Code не може да пронађе Python интерпретер
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

## 🎯 Кључни закључци

Након завршетка овог практичног рада, требало би да имате:

✅ **Комплетно развојно окружење**: Сви алати инсталирани и конфигурисани  
✅ **Распоређене Azure ресурсе**: AI услуге и пратећа инфраструктура  
✅ **Docker окружење у функцији**: PostgreSQL и MCP сервер контејнери  
✅ **VS Code интеграцију**: MCP сервери конфигурисани и доступни  
✅ **Валидацију подешавања**: Сви компоненти тестирани и функционални  
✅ **Знање о решавању проблема**: Уобичајени проблеми и решења  

## 🚀 Шта следи

Са окружењем спремним, наставите са **[Практичним радом 04: Дизајн базе података и шема](../04-Database/README.md)** да:

- Детаљно истражите шему малопродајне базе података
- Разумете моделовање података за више корисника
- Научите о имплементацији безбедности на нивоу реда
- Радите са примером малопродајних података

## 📚 Додатни ресурси

### Развојни алати
- [Docker документација](https://docs.docker.com/) - Комплетна референца за Docker
- [Azure CLI референца](https://docs.microsoft.com/cli/azure/) - Azure CLI команде
- [VS Code документација](https://code.visualstudio.com/docs) - Конфигурација уређивача и екстензије

### Azure услуге
- [Azure AI Foundry документација](https://docs.microsoft.com/azure/ai-foundry/) - Конфигурација AI услуга
- [Azure OpenAI услуга](https://docs.microsoft.com/azure/cognitive-services/openai/) - Распоређивање AI модела
- [Application Insights](https://docs.microsoft.com/azure/azure-monitor/app/app-insights-overview) - Подешавање праћења

### Python развој
- [Python виртуелна окружења](https://docs.python.org/3/tutorial/venv.html) - Управљање окружењима
- [AsyncIO документација](https://docs.python.org/3/library/asyncio.html) - Асинхрони програмирање
- [FastAPI документација](https://fastapi.tiangolo.com/) - Шаблони веб оквира

---

**Следеће**: Окружење је спремно? Наставите са [Практичним радом 04: Дизајн базе података и шема](../04-Database/README.md)

---

**Одрицање од одговорности**:  
Овај документ је преведен коришћењем услуге за превођење помоћу вештачке интелигенције [Co-op Translator](https://github.com/Azure/co-op-translator). Иако се трудимо да обезбедимо тачност, молимо вас да имате у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати меродавним извором. За критичне информације препоручује се професионални превод од стране људи. Не преузимамо одговорност за било каква погрешна тумачења или неспоразуме који могу произаћи из коришћења овог превода.