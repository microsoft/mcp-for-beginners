# Настройка на средата

## 🎯 Какво обхваща този лабораторен урок

Този практически урок ви води през настройката на пълна среда за разработка за създаване на MCP сървъри с интеграция на PostgreSQL. Ще конфигурирате всички необходими инструменти, ще разположите ресурси в Azure и ще валидирате настройката си, преди да преминете към реализацията.

## Обзор

Правилната среда за разработка е от съществено значение за успешното създаване на MCP сървъри. Този урок предоставя стъпка по стъпка инструкции за настройка на Docker, услуги в Azure, инструменти за разработка и валидиране на тяхната съвместна работа.

До края на урока ще имате напълно функционална среда за разработка, готова за създаване на MCP сървъра за Zava Retail.

## Цели на обучението

До края на този урок ще можете:

- **Да инсталирате и конфигурирате** всички необходими инструменти за разработка
- **Да разположите ресурси в Azure**, необходими за MCP сървъра
- **Да настроите Docker контейнери** за PostgreSQL и MCP сървъра
- **Да валидирате** настройката на средата си с тестови връзки
- **Да отстранявате проблеми** с настройката и конфигурацията
- **Да разберете** работния процес на разработка и структурата на файловете

## 📋 Проверка на предпоставките

Преди да започнете, уверете се, че разполагате със следното:

### Необходими знания
- Основни умения за работа с командния ред (Windows Command Prompt/PowerShell)
- Разбиране на променливи на средата
- Запознаване с Git за контрол на версиите
- Основни концепции за Docker (контейнери, изображения, обеми)

### Системни изисквания
- **Операционна система**: Windows 10/11, macOS или Linux
- **RAM**: Минимум 8GB (препоръчително 16GB)
- **Съхранение**: Поне 10GB свободно пространство
- **Мрежа**: Интернет връзка за изтегляния и разполагане в Azure

### Изисквания за акаунти
- **Абонамент за Azure**: Безплатният план е достатъчен
- **Акаунт в GitHub**: За достъп до хранилището
- **Акаунт в Docker Hub**: (По избор) За публикуване на персонализирани изображения

## 🛠️ Инсталиране на инструменти

### 1. Инсталиране на Docker Desktop

Docker предоставя контейнеризираната среда за нашата разработка.

#### Инсталиране на Windows

1. **Изтеглете Docker Desktop**:
   ```cmd
   # Visit https://desktop.docker.com/win/stable/Docker%20Desktop%20Installer.exe
   # Or use Windows Package Manager
   winget install Docker.DockerDesktop
   ```

2. **Инсталирайте и конфигурирайте**:
   - Стартирайте инсталатора като администратор
   - Активирайте интеграцията с WSL 2, когато бъдете подканени
   - Рестартирайте компютъра след завършване на инсталацията

3. **Проверете инсталацията**:
   ```cmd
   docker --version
   docker-compose --version
   ```

#### Инсталиране на macOS

1. **Изтеглете и инсталирайте**:
   ```bash
   # Download from https://desktop.docker.com/mac/stable/Docker.dmg
   # Or use Homebrew
   brew install --cask docker
   ```

2. **Стартирайте Docker Desktop**:
   - Стартирайте Docker Desktop от Applications
   - Завършете началния съветник за настройка

3. **Проверете инсталацията**:
   ```bash
   docker --version
   docker-compose --version
   ```

#### Инсталиране на Linux

1. **Инсталирайте Docker Engine**:
   ```bash
   # Ubuntu/Debian
   curl -fsSL https://get.docker.com -o get-docker.sh
   sudo sh get-docker.sh
   sudo usermod -aG docker $USER
   
   # Log out and back in for group changes to take effect
   ```

2. **Инсталирайте Docker Compose**:
   ```bash
   sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
   sudo chmod +x /usr/local/bin/docker-compose
   ```

### 2. Инсталиране на Azure CLI

Azure CLI позволява разполагане и управление на ресурси в Azure.

#### Инсталиране на Windows

```cmd
# Using Windows Package Manager
winget install Microsoft.AzureCLI

# Or download MSI from: https://aka.ms/installazurecliwindows
```

#### Инсталиране на macOS

```bash
# Using Homebrew
brew install azure-cli

# Or using installer
curl -L https://aka.ms/InstallAzureCli | bash
```

#### Инсталиране на Linux

```bash
# Ubuntu/Debian
curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash

# RHEL/CentOS
sudo rpm --import https://packages.microsoft.com/keys/microsoft.asc
sudo dnf install azure-cli
```

#### Проверка и автентикация

```bash
# Check installation
az version

# Login to Azure
az login

# Set default subscription (if you have multiple)
az account list --output table
az account set --subscription "Your-Subscription-Name"
```

### 3. Инсталиране на Git

Git е необходим за клониране на хранилището и контрол на версиите.

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

### 4. Инсталиране на VS Code

Visual Studio Code предоставя интегрираната среда за разработка с поддръжка за MCP.

#### Инсталиране

```cmd
# Windows
winget install Microsoft.VisualStudioCode

# macOS
brew install --cask visual-studio-code

# Linux (Ubuntu/Debian)
sudo snap install code --classic
```

#### Необходими разширения

Инсталирайте тези разширения за VS Code:

```bash
# Install via command line
code --install-extension ms-python.python
code --install-extension ms-vscode.vscode-json
code --install-extension ms-azuretools.vscode-docker
code --install-extension ms-vscode.azure-account
```

Или инсталирайте чрез VS Code:
1. Отворете VS Code
2. Отидете на Extensions (Ctrl+Shift+X)
3. Инсталирайте:
   - **Python** (Microsoft)
   - **Docker** (Microsoft)
   - **Azure Account** (Microsoft)
   - **JSON** (Microsoft)

### 5. Инсталиране на Python

Python 3.8+ е необходим за разработката на MCP сървъра.

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

#### Проверка на инсталацията

```bash
python --version  # Should show Python 3.11.x
pip --version      # Should show pip version
```

## 🚀 Настройка на проекта

### 1. Клониране на хранилището

```bash
# Clone the main repository
git clone https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail.git

# Navigate to the project directory
cd MCP-Server-and-PostgreSQL-Sample-Retail

# Verify repository structure
ls -la
```

### 2. Създаване на виртуална среда за Python

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

### 3. Инсталиране на зависимости за Python

```bash
# Install development dependencies
pip install -r requirements.lock.txt

# Verify key packages
pip list | grep fastmcp
pip list | grep asyncpg
pip list | grep azure
```

## ☁️ Разполагане на ресурси в Azure

### 1. Разбиране на изискванията за ресурси

Нашият MCP сървър изисква следните ресурси в Azure:

| **Ресурс** | **Цел** | **Ориентировъчна цена** |
|------------|---------|-----------------------|
| **Azure AI Foundry** | Хостинг и управление на AI модели | $10-50/месец |
| **OpenAI Deployment** | Модел за текстово вграждане (text-embedding-3-small) | $5-20/месец |
| **Application Insights** | Мониторинг и телеметрия | $5-15/месец |
| **Resource Group** | Организация на ресурси | Безплатно |

### 2. Разполагане на ресурси в Azure

#### Опция А: Автоматизирано разполагане (Препоръчително)

```bash
# Navigate to infrastructure directory
cd infra

# Windows - PowerShell
./deploy.ps1

# macOS/Linux - Bash
./deploy.sh
```

Скриптът за разполагане ще:
1. Създаде уникална група ресурси
2. Разположи ресурси за Azure AI Foundry
3. Разположи модела text-embedding-3-small
4. Конфигурира Application Insights
5. Създаде service principal за автентикация
6. Генерира `.env` файл с конфигурация

#### Опция Б: Ръчно разполагане

Ако предпочитате ръчен контрол или автоматизираният скрипт не успее:

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

### 3. Проверка на разполагането в Azure

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

### 4. Конфигуриране на променливи на средата

След разполагането трябва да имате `.env` файл. Уверете се, че съдържа:

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

## 🐳 Настройка на Docker среда

### 1. Разбиране на Docker композицията

Нашата среда за разработка използва Docker Compose:

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

### 2. Стартиране на средата за разработка

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

### 3. Проверка на настройката на базата данни

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

### 4. Тест на MCP сървъра

```bash
# Check MCP server health
curl http://localhost:8000/health

# Test basic MCP endpoint
curl -X POST http://localhost:8000/mcp \
  -H "Content-Type: application/json" \
  -H "x-rls-user-id: 00000000-0000-0000-0000-000000000000" \
  -d '{"method": "tools/list", "params": {}}'
```

## 🔧 Конфигурация на VS Code

### 1. Конфигуриране на MCP интеграция

Създайте MCP конфигурация за VS Code:

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

### 2. Конфигуриране на Python среда

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

### 3. Тест на интеграцията с VS Code

1. **Отворете проекта във VS Code**:
   ```bash
   code .
   ```

2. **Отворете AI Chat**:
   - Натиснете `Ctrl+Shift+P` (Windows/Linux) или `Cmd+Shift+P` (macOS)
   - Въведете "AI Chat" и изберете "AI Chat: Open Chat"

3. **Тест на връзката с MCP сървъра**:
   - В AI Chat въведете `#zava` и изберете един от конфигурираните сървъри
   - Попитайте: "Какви таблици са налични в базата данни?"
   - Трябва да получите отговор с изброяване на таблиците в ритейл базата данни

## ✅ Валидиране на средата

### 1. Комплексна проверка на системата

Стартирайте този скрипт за валидиране на настройката:

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

### 2. Ръчен списък за проверка

**✅ Основни инструменти**
- [ ] Инсталирана и работеща версия на Docker 20.10+
- [ ] Инсталиран и автентикиран Azure CLI 2.40+
- [ ] Инсталиран Python 3.8+ с pip
- [ ] Инсталиран Git 2.30+
- [ ] VS Code с необходимите разширения

**✅ Ресурси в Azure**
- [ ] Успешно създадена група ресурси
- [ ] Разположен проект за AI Foundry
- [ ] Разположен модел text-embedding-3-small
- [ ] Конфигуриран Application Insights
- [ ] Създаден service principal с правилни разрешения

**✅ Конфигурация на средата**
- [ ] Създаден `.env` файл с всички необходими променливи
- [ ] Работещи Azure идентификационни данни (тест с `az account show`)
- [ ] Работещ и достъпен PostgreSQL контейнер
- [ ] Заредени примерни данни в базата данни

**✅ Интеграция с VS Code**
- [ ] Конфигуриран `.vscode/mcp.json`
- [ ] Python интерпретатор настроен към виртуалната среда
- [ ] MCP сървърите се появяват в AI Chat
- [ ] Могат да се изпълняват тестови заявки чрез AI Chat

## 🛠️ Отстраняване на често срещани проблеми

### Проблеми с Docker

**Проблем**: Docker контейнерите не стартират
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

**Проблем**: Връзката с PostgreSQL не успява
```bash
# Check container logs
docker-compose logs postgres

# Verify container is healthy
docker-compose ps

# Test direct connection
docker-compose exec postgres psql -U postgres -d zava -c "SELECT 1;"
```

### Проблеми с разполагането в Azure

**Проблем**: Разполагането в Azure не успява
```bash
# Check Azure CLI authentication
az account show

# Verify subscription permissions
az role assignment list --assignee $(az account show --query user.name -o tsv)

# Check resource provider registration
az provider register --namespace Microsoft.CognitiveServices
az provider register --namespace Microsoft.Insights
```

**Проблем**: Автентикацията на AI услугата не успява
```bash
# Test service principal
az login --service-principal \
  --username $AZURE_CLIENT_ID \
  --password $AZURE_CLIENT_SECRET \
  --tenant $AZURE_TENANT_ID

# Verify AI service deployment
az cognitiveservices account list --query "[].{Name:name,Kind:kind,Location:location}"
```

### Проблеми с Python средата

**Проблем**: Инсталирането на пакети не успява
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

**Проблем**: VS Code не може да намери Python интерпретатор
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

## 🎯 Основни изводи

След завършване на този урок трябва да имате:

✅ **Пълна среда за разработка**: Всички инструменти инсталирани и конфигурирани  
✅ **Разположени ресурси в Azure**: AI услуги и поддържаща инфраструктура  
✅ **Работеща Docker среда**: Контейнери за PostgreSQL и MCP сървъра  
✅ **Интеграция с VS Code**: MCP сървърите конфигурирани и достъпни  
✅ **Валидирана настройка**: Всички компоненти тествани и работещи заедно  
✅ **Знания за отстраняване на проблеми**: Често срещани проблеми и решения  

## 🚀 Какво следва

С готова среда продължете към **[Лабораторен урок 04: Дизайн и схема на базата данни](../04-Database/README.md)**, за да:

- Разгледате подробно схемата на ритейл базата данни
- Разберете моделирането на данни за много наематели
- Научите за имплементацията на Row Level Security
- Работите с примерни ритейл данни

## 📚 Допълнителни ресурси

### Инструменти за разработка
- [Документация за Docker](https://docs.docker.com/) - Пълно ръководство за Docker
- [Референция за Azure CLI](https://docs.microsoft.com/cli/azure/) - Команди за Azure CLI
- [Документация за VS Code](https://code.visualstudio.com/docs) - Конфигурация на редактора и разширения

### Услуги в Azure
- [Документация за Azure AI Foundry](https://docs.microsoft.com/azure/ai-foundry/) - Конфигурация на AI услуги
- [Azure OpenAI Service](https://docs.microsoft.com/azure/cognitive-services/openai/) - Разполагане на AI модели
- [Application Insights](https://docs.microsoft.com/azure/azure-monitor/app/app-insights-overview) - Настройка на мониторинг

### Python разработка
- [Python виртуални среди](https://docs.python.org/3/tutorial/venv.html) - Управление на среди
- [Документация за AsyncIO](https://docs.python.org/3/library/asyncio.html) - Модели за асинхронно програмиране
- [Документация за FastAPI](https://fastapi.tiangolo.com/) - Модели за уеб рамки

---

**Следващо**: Средата е готова? Продължете с [Лабораторен урок 04: Дизайн и схема на базата данни](../04-Database/README.md)

---

**Отказ от отговорност**:  
Този документ е преведен с помощта на AI услуга за превод [Co-op Translator](https://github.com/Azure/co-op-translator). Въпреки че се стремим към точност, моля, имайте предвид, че автоматичните преводи може да съдържат грешки или неточности. Оригиналният документ на неговия изходен език трябва да се счита за авторитетен източник. За критична информация се препоръчва професионален превод от човек. Ние не носим отговорност за каквито и да било недоразумения или погрешни интерпретации, произтичащи от използването на този превод.