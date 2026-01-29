# Налаштування середовища

## 🎯 Що охоплює цей лабораторний практикум

Цей практикум допоможе вам налаштувати повне середовище розробки для створення MCP серверів з інтеграцією PostgreSQL. Ви налаштуєте всі необхідні інструменти, розгорнете ресурси Azure і перевірите свою конфігурацію перед початком реалізації.

## Огляд

Правильно налаштоване середовище розробки є ключовим для успішної розробки MCP серверів. Цей практикум надає покрокові інструкції для налаштування Docker, сервісів Azure, інструментів розробки та перевірки їх сумісності.

Після завершення цього практикуму ви матимете повністю функціональне середовище розробки, готове для створення MCP сервера Zava Retail.

## Цілі навчання

Після завершення цього практикуму ви зможете:

- **Встановити та налаштувати** всі необхідні інструменти розробки
- **Розгорнути ресурси Azure**, необхідні для MCP сервера
- **Налаштувати Docker-контейнери** для PostgreSQL та MCP сервера
- **Перевірити** налаштування середовища за допомогою тестових з'єднань
- **Вирішувати проблеми** з налаштуванням та конфігурацією
- **Зрозуміти** робочий процес розробки та структуру файлів

## 📋 Перевірка перед початком

Перед початком переконайтеся, що у вас є:

### Необхідні знання
- Базове використання командного рядка (Windows Command Prompt/PowerShell)
- Розуміння змінних середовища
- Знайомство з системою контролю версій Git
- Основи Docker (контейнери, образи, томи)

### Системні вимоги
- **Операційна система**: Windows 10/11, macOS або Linux
- **ОЗП**: Мінімум 8 ГБ (рекомендовано 16 ГБ)
- **Місце на диску**: Щонайменше 10 ГБ вільного простору
- **Мережа**: Інтернет для завантажень і розгортання Azure

### Вимоги до облікових записів
- **Підписка Azure**: Достатньо безкоштовного рівня
- **Обліковий запис GitHub**: Для доступу до репозиторію
- **Обліковий запис Docker Hub**: (Необов'язково) Для публікації власних образів

## 🛠️ Встановлення інструментів

### 1. Встановлення Docker Desktop

Docker забезпечує контейнеризоване середовище для нашої розробки.

#### Встановлення на Windows

1. **Завантажте Docker Desktop**:
   ```cmd
   # Visit https://desktop.docker.com/win/stable/Docker%20Desktop%20Installer.exe
   # Or use Windows Package Manager
   winget install Docker.DockerDesktop
   ```

2. **Встановіть і налаштуйте**:
   - Запустіть інсталятор від імені адміністратора
   - Увімкніть інтеграцію WSL 2, коли буде запропоновано
   - Перезавантажте комп'ютер після завершення встановлення

3. **Перевірте встановлення**:
   ```cmd
   docker --version
   docker-compose --version
   ```

#### Встановлення на macOS

1. **Завантажте та встановіть**:
   ```bash
   # Download from https://desktop.docker.com/mac/stable/Docker.dmg
   # Or use Homebrew
   brew install --cask docker
   ```

2. **Запустіть Docker Desktop**:
   - Відкрийте Docker Desktop з папки "Програми"
   - Завершіть початковий майстер налаштування

3. **Перевірте встановлення**:
   ```bash
   docker --version
   docker-compose --version
   ```

#### Встановлення на Linux

1. **Встановіть Docker Engine**:
   ```bash
   # Ubuntu/Debian
   curl -fsSL https://get.docker.com -o get-docker.sh
   sudo sh get-docker.sh
   sudo usermod -aG docker $USER
   
   # Log out and back in for group changes to take effect
   ```

2. **Встановіть Docker Compose**:
   ```bash
   sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
   sudo chmod +x /usr/local/bin/docker-compose
   ```

### 2. Встановлення Azure CLI

Azure CLI дозволяє розгортати та керувати ресурсами Azure.

#### Встановлення на Windows

```cmd
# Using Windows Package Manager
winget install Microsoft.AzureCLI

# Or download MSI from: https://aka.ms/installazurecliwindows
```

#### Встановлення на macOS

```bash
# Using Homebrew
brew install azure-cli

# Or using installer
curl -L https://aka.ms/InstallAzureCli | bash
```

#### Встановлення на Linux

```bash
# Ubuntu/Debian
curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash

# RHEL/CentOS
sudo rpm --import https://packages.microsoft.com/keys/microsoft.asc
sudo dnf install azure-cli
```

#### Перевірка та автентифікація

```bash
# Check installation
az version

# Login to Azure
az login

# Set default subscription (if you have multiple)
az account list --output table
az account set --subscription "Your-Subscription-Name"
```

### 3. Встановлення Git

Git потрібен для клонування репозиторію та контролю версій.

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

### 4. Встановлення VS Code

Visual Studio Code забезпечує інтегроване середовище розробки з підтримкою MCP.

#### Встановлення

```cmd
# Windows
winget install Microsoft.VisualStudioCode

# macOS
brew install --cask visual-studio-code

# Linux (Ubuntu/Debian)
sudo snap install code --classic
```

#### Необхідні розширення

Встановіть ці розширення для VS Code:

```bash
# Install via command line
code --install-extension ms-python.python
code --install-extension ms-vscode.vscode-json
code --install-extension ms-azuretools.vscode-docker
code --install-extension ms-vscode.azure-account
```

Або встановіть через VS Code:
1. Відкрийте VS Code
2. Перейдіть до розширень (Ctrl+Shift+X)
3. Встановіть:
   - **Python** (Microsoft)
   - **Docker** (Microsoft)
   - **Azure Account** (Microsoft)
   - **JSON** (Microsoft)

### 5. Встановлення Python

Python 3.8+ потрібен для розробки MCP сервера.

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

#### Перевірка встановлення

```bash
python --version  # Should show Python 3.11.x
pip --version      # Should show pip version
```

## 🚀 Налаштування проєкту

### 1. Клонування репозиторію

```bash
# Clone the main repository
git clone https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail.git

# Navigate to the project directory
cd MCP-Server-and-PostgreSQL-Sample-Retail

# Verify repository structure
ls -la
```

### 2. Створення віртуального середовища Python

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

### 3. Встановлення залежностей Python

```bash
# Install development dependencies
pip install -r requirements.lock.txt

# Verify key packages
pip list | grep fastmcp
pip list | grep asyncpg
pip list | grep azure
```

## ☁️ Розгортання ресурсів Azure

### 1. Розуміння вимог до ресурсів

Для MCP сервера потрібні такі ресурси Azure:

| **Ресурс** | **Призначення** | **Орієнтовна вартість** |
|------------|-----------------|-------------------------|
| **Azure AI Foundry** | Хостинг і управління AI моделями | $10-50/місяць |
| **OpenAI Deployment** | Модель текстового вбудовування (text-embedding-3-small) | $5-20/місяць |
| **Application Insights** | Моніторинг і телеметрія | $5-15/місяць |
| **Resource Group** | Організація ресурсів | Безкоштовно |

### 2. Розгортання ресурсів Azure

#### Варіант A: Автоматизоване розгортання (рекомендовано)

```bash
# Navigate to infrastructure directory
cd infra

# Windows - PowerShell
./deploy.ps1

# macOS/Linux - Bash
./deploy.sh
```

Скрипт розгортання виконає:
1. Створення унікальної групи ресурсів
2. Розгортання ресурсів Azure AI Foundry
3. Розгортання моделі text-embedding-3-small
4. Налаштування Application Insights
5. Створення сервісного принципала для автентифікації
6. Генерацію файлу `.env` з конфігурацією

#### Варіант B: Ручне розгортання

Якщо ви віддаєте перевагу ручному контролю або скрипт автоматизації не працює:

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

### 3. Перевірка розгортання Azure

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

### 4. Налаштування змінних середовища

Після розгортання у вас має бути файл `.env`. Переконайтеся, що він містить:

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

## 🐳 Налаштування Docker середовища

### 1. Розуміння Docker-композиції

Наше середовище розробки використовує Docker Compose:

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

### 2. Запуск середовища розробки

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

### 3. Перевірка налаштування бази даних

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

### 4. Тестування MCP сервера

```bash
# Check MCP server health
curl http://localhost:8000/health

# Test basic MCP endpoint
curl -X POST http://localhost:8000/mcp \
  -H "Content-Type: application/json" \
  -H "x-rls-user-id: 00000000-0000-0000-0000-000000000000" \
  -d '{"method": "tools/list", "params": {}}'
```

## 🔧 Налаштування VS Code

### 1. Налаштування інтеграції MCP

Створіть конфігурацію MCP для VS Code:

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

### 2. Налаштування Python середовища

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

### 3. Тестування інтеграції VS Code

1. **Відкрийте проєкт у VS Code**:
   ```bash
   code .
   ```

2. **Відкрийте AI Chat**:
   - Натисніть `Ctrl+Shift+P` (Windows/Linux) або `Cmd+Shift+P` (macOS)
   - Введіть "AI Chat" і виберіть "AI Chat: Open Chat"

3. **Перевірте з'єднання з MCP сервером**:
   - У AI Chat введіть `#zava` і виберіть один із налаштованих серверів
   - Запитайте: "Які таблиці доступні в базі даних?"
   - Ви маєте отримати відповідь із переліком таблиць роздрібної бази даних

## ✅ Перевірка середовища

### 1. Комплексна перевірка системи

Запустіть цей скрипт перевірки для валідації налаштувань:

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

### 2. Контрольний список ручної перевірки

**✅ Основні інструменти**
- [ ] Встановлено Docker версії 20.10+ і запущено
- [ ] Встановлено Azure CLI версії 2.40+ і виконано автентифікацію
- [ ] Встановлено Python 3.8+ із pip
- [ ] Встановлено Git версії 2.30+
- [ ] Встановлено VS Code із необхідними розширеннями

**✅ Ресурси Azure**
- [ ] Успішно створено групу ресурсів
- [ ] Розгорнуто проєкт AI Foundry
- [ ] Розгорнуто модель text-embedding-3-small
- [ ] Налаштовано Application Insights
- [ ] Створено сервісний принципал із правильними дозволами

**✅ Конфігурація середовища**
- [ ] Створено файл `.env` із усіма необхідними змінними
- [ ] Працюють облікові дані Azure (перевірте за допомогою `az account show`)
- [ ] Запущено контейнер PostgreSQL і доступний
- [ ] Завантажено зразкові дані в базу даних

**✅ Інтеграція VS Code**
- [ ] Налаштовано `.vscode/mcp.json`
- [ ] Вибрано інтерпретатор Python для віртуального середовища
- [ ] MCP сервери з'являються в AI Chat
- [ ] Можна виконувати тестові запити через AI Chat

## 🛠️ Вирішення поширених проблем

### Проблеми з Docker

**Проблема**: Контейнери Docker не запускаються
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

**Проблема**: З'єднання з PostgreSQL не працює
```bash
# Check container logs
docker-compose logs postgres

# Verify container is healthy
docker-compose ps

# Test direct connection
docker-compose exec postgres psql -U postgres -d zava -c "SELECT 1;"
```

### Проблеми з розгортанням Azure

**Проблема**: Розгортання Azure не вдалося
```bash
# Check Azure CLI authentication
az account show

# Verify subscription permissions
az role assignment list --assignee $(az account show --query user.name -o tsv)

# Check resource provider registration
az provider register --namespace Microsoft.CognitiveServices
az provider register --namespace Microsoft.Insights
```

**Проблема**: Автентифікація AI сервісу не працює
```bash
# Test service principal
az login --service-principal \
  --username $AZURE_CLIENT_ID \
  --password $AZURE_CLIENT_SECRET \
  --tenant $AZURE_TENANT_ID

# Verify AI service deployment
az cognitiveservices account list --query "[].{Name:name,Kind:kind,Location:location}"
```

### Проблеми з Python середовищем

**Проблема**: Встановлення пакетів не вдалося
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

**Проблема**: VS Code не може знайти інтерпретатор Python
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

## 🎯 Основні висновки

Після завершення цього практикуму ви маєте:

✅ **Повне середовище розробки**: Встановлено та налаштовано всі інструменти  
✅ **Розгорнуті ресурси Azure**: AI сервіси та підтримуюча інфраструктура  
✅ **Запущене Docker середовище**: Контейнери PostgreSQL та MCP сервера  
✅ **Інтеграція VS Code**: Налаштовані та доступні MCP сервери  
✅ **Перевірене налаштування**: Усі компоненти протестовані та працюють разом  
✅ **Знання для вирішення проблем**: Поширені проблеми та їх вирішення  

## 🚀 Що далі

З готовим середовищем продовжуйте до **[Лабораторії 04: Проєктування бази даних і схема](../04-Database/README.md)**, щоб:

- Детально ознайомитися зі схемою роздрібної бази даних
- Зрозуміти моделювання даних для багатокористувацького середовища
- Дізнатися про реалізацію безпеки на рівні рядків
- Працювати із зразковими даними роздрібної торгівлі

## 📚 Додаткові ресурси

### Інструменти розробки
- [Документація Docker](https://docs.docker.com/) - Повний довідник Docker
- [Довідник Azure CLI](https://docs.microsoft.com/cli/azure/) - Команди Azure CLI
- [Документація VS Code](https://code.visualstudio.com/docs) - Налаштування редактора та розширень

### Сервіси Azure
- [Документація Azure AI Foundry](https://docs.microsoft.com/azure/ai-foundry/) - Налаштування AI сервісу
- [Сервіс Azure OpenAI](https://docs.microsoft.com/azure/cognitive-services/openai/) - Розгортання AI моделі
- [Application Insights](https://docs.microsoft.com/azure/azure-monitor/app/app-insights-overview) - Налаштування моніторингу

### Розробка на Python
- [Віртуальні середовища Python](https://docs.python.org/3/tutorial/venv.html) - Управління середовищами
- [Документація AsyncIO](https://docs.python.org/3/library/asyncio.html) - Шаблони асинхронного програмування
- [Документація FastAPI](https://fastapi.tiangolo.com/) - Шаблони веб-фреймворку

---

**Далі**: Середовище готове? Продовжуйте до [Лабораторії 04: Проєктування бази даних і схема](../04-Database/README.md)

---

**Відмова від відповідальності**:  
Цей документ був перекладений за допомогою сервісу автоматичного перекладу [Co-op Translator](https://github.com/Azure/co-op-translator). Хоча ми прагнемо до точності, звертаємо вашу увагу, що автоматичні переклади можуть містити помилки або неточності. Оригінальний документ на його рідній мові слід вважати авторитетним джерелом. Для критично важливої інформації рекомендується професійний людський переклад. Ми не несемо відповідальності за будь-які непорозуміння або неправильні тлумачення, що виникли внаслідок використання цього перекладу.