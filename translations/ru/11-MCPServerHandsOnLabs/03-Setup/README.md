# Настройка окружения

## 🎯 Что охватывает этот практикум

Этот практикум поможет вам настроить полное окружение для разработки MCP-серверов с интеграцией PostgreSQL. Вы настроите все необходимые инструменты, развернете ресурсы Azure и проверите корректность конфигурации перед началом реализации.

## Обзор

Правильно настроенное окружение разработки — ключ к успешной разработке MCP-серверов. В этом практикуме вы найдете пошаговые инструкции по настройке Docker, сервисов Azure, инструментов разработки и проверке их совместной работы.

К концу практикума у вас будет полностью функциональное окружение для разработки MCP-сервера Zava Retail.

## Цели обучения

К концу практикума вы сможете:

- **Установить и настроить** все необходимые инструменты разработки
- **Развернуть ресурсы Azure**, необходимые для MCP-сервера
- **Настроить контейнеры Docker** для PostgreSQL и MCP-сервера
- **Проверить** корректность настройки окружения с помощью тестовых подключений
- **Устранить неполадки**, связанные с настройкой и конфигурацией
- **Понять** рабочий процесс разработки и структуру файлов

## 📋 Проверка предварительных требований

Перед началом убедитесь, что у вас есть:

### Необходимые знания
- Базовые навыки работы с командной строкой (Windows Command Prompt/PowerShell)
- Понимание переменных окружения
- Знание системы контроля версий Git
- Основы работы с Docker (контейнеры, образы, тома)

### Системные требования
- **Операционная система**: Windows 10/11, macOS или Linux
- **ОЗУ**: минимум 8 ГБ (рекомендуется 16 ГБ)
- **Хранилище**: не менее 10 ГБ свободного места
- **Сеть**: подключение к интернету для загрузок и развертывания Azure

### Требования к аккаунтам
- **Подписка Azure**: достаточно бесплатного тарифа
- **Аккаунт GitHub**: для доступа к репозиторию
- **Аккаунт Docker Hub**: (опционально) для публикации пользовательских образов

## 🛠️ Установка инструментов

### 1. Установка Docker Desktop

Docker предоставляет контейнеризированное окружение для нашей разработки.

#### Установка на Windows

1. **Скачайте Docker Desktop**:
   ```cmd
   # Visit https://desktop.docker.com/win/stable/Docker%20Desktop%20Installer.exe
   # Or use Windows Package Manager
   winget install Docker.DockerDesktop
   ```

2. **Установите и настройте**:
   - Запустите установщик от имени администратора
   - Включите интеграцию с WSL 2, когда будет предложено
   - Перезагрузите компьютер после завершения установки

3. **Проверьте установку**:
   ```cmd
   docker --version
   docker-compose --version
   ```

#### Установка на macOS

1. **Скачайте и установите**:
   ```bash
   # Download from https://desktop.docker.com/mac/stable/Docker.dmg
   # Or use Homebrew
   brew install --cask docker
   ```

2. **Запустите Docker Desktop**:
   - Откройте Docker Desktop из папки "Программы"
   - Завершите начальный мастер настройки

3. **Проверьте установку**:
   ```bash
   docker --version
   docker-compose --version
   ```

#### Установка на Linux

1. **Установите Docker Engine**:
   ```bash
   # Ubuntu/Debian
   curl -fsSL https://get.docker.com -o get-docker.sh
   sudo sh get-docker.sh
   sudo usermod -aG docker $USER
   
   # Log out and back in for group changes to take effect
   ```

2. **Установите Docker Compose**:
   ```bash
   sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
   sudo chmod +x /usr/local/bin/docker-compose
   ```

### 2. Установка Azure CLI

Azure CLI позволяет развертывать и управлять ресурсами Azure.

#### Установка на Windows

```cmd
# Using Windows Package Manager
winget install Microsoft.AzureCLI

# Or download MSI from: https://aka.ms/installazurecliwindows
```

#### Установка на macOS

```bash
# Using Homebrew
brew install azure-cli

# Or using installer
curl -L https://aka.ms/InstallAzureCli | bash
```

#### Установка на Linux

```bash
# Ubuntu/Debian
curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash

# RHEL/CentOS
sudo rpm --import https://packages.microsoft.com/keys/microsoft.asc
sudo dnf install azure-cli
```

#### Проверка и аутентификация

```bash
# Check installation
az version

# Login to Azure
az login

# Set default subscription (if you have multiple)
az account list --output table
az account set --subscription "Your-Subscription-Name"
```

### 3. Установка Git

Git необходим для клонирования репозитория и контроля версий.

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

### 4. Установка VS Code

Visual Studio Code предоставляет интегрированную среду разработки с поддержкой MCP.

#### Установка

```cmd
# Windows
winget install Microsoft.VisualStudioCode

# macOS
brew install --cask visual-studio-code

# Linux (Ubuntu/Debian)
sudo snap install code --classic
```

#### Необходимые расширения

Установите следующие расширения для VS Code:

```bash
# Install via command line
code --install-extension ms-python.python
code --install-extension ms-vscode.vscode-json
code --install-extension ms-azuretools.vscode-docker
code --install-extension ms-vscode.azure-account
```

Или установите через VS Code:
1. Откройте VS Code
2. Перейдите в раздел Extensions (Ctrl+Shift+X)
3. Установите:
   - **Python** (Microsoft)
   - **Docker** (Microsoft)
   - **Azure Account** (Microsoft)
   - **JSON** (Microsoft)

### 5. Установка Python

Для разработки MCP-сервера требуется Python версии 3.8 или выше.

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

#### Проверка установки

```bash
python --version  # Should show Python 3.11.x
pip --version      # Should show pip version
```

## 🚀 Настройка проекта

### 1. Клонирование репозитория

```bash
# Clone the main repository
git clone https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail.git

# Navigate to the project directory
cd MCP-Server-and-PostgreSQL-Sample-Retail

# Verify repository structure
ls -la
```

### 2. Создание виртуального окружения Python

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

### 3. Установка зависимостей Python

```bash
# Install development dependencies
pip install -r requirements.lock.txt

# Verify key packages
pip list | grep fastmcp
pip list | grep asyncpg
pip list | grep azure
```

## ☁️ Развертывание ресурсов Azure

### 1. Понимание требований к ресурсам

Для работы MCP-сервера требуются следующие ресурсы Azure:

| **Ресурс** | **Назначение** | **Оценочная стоимость** |
|------------|----------------|-------------------------|
| **Azure AI Foundry** | Хостинг и управление AI-моделями | $10-50/месяц |
| **OpenAI Deployment** | Модель текстового встраивания (text-embedding-3-small) | $5-20/месяц |
| **Application Insights** | Мониторинг и телеметрия | $5-15/месяц |
| **Resource Group** | Организация ресурсов | Бесплатно |

### 2. Развертывание ресурсов Azure

#### Вариант A: Автоматическое развертывание (рекомендуется)

```bash
# Navigate to infrastructure directory
cd infra

# Windows - PowerShell
./deploy.ps1

# macOS/Linux - Bash
./deploy.sh
```

Скрипт развертывания выполнит следующие действия:
1. Создаст уникальную группу ресурсов
2. Развернет ресурсы Azure AI Foundry
3. Развернет модель text-embedding-3-small
4. Настроит Application Insights
5. Создаст сервисный принципал для аутентификации
6. Сгенерирует файл `.env` с конфигурацией

#### Вариант B: Ручное развертывание

Если вы предпочитаете ручной контроль или автоматический скрипт не сработал:

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

### 3. Проверка развертывания Azure

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

### 4. Настройка переменных окружения

После развертывания у вас должен быть файл `.env`. Убедитесь, что он содержит:

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

## 🐳 Настройка окружения Docker

### 1. Понимание Docker-композиции

Наше окружение разработки использует Docker Compose:

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

### 2. Запуск окружения разработки

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

### 3. Проверка настройки базы данных

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

### 4. Тестирование MCP-сервера

```bash
# Check MCP server health
curl http://localhost:8000/health

# Test basic MCP endpoint
curl -X POST http://localhost:8000/mcp \
  -H "Content-Type: application/json" \
  -H "x-rls-user-id: 00000000-0000-0000-0000-000000000000" \
  -d '{"method": "tools/list", "params": {}}'
```

## 🔧 Конфигурация VS Code

### 1. Настройка интеграции MCP

Создайте конфигурацию MCP для VS Code:

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

### 2. Настройка Python-окружения

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

### 3. Тестирование интеграции VS Code

1. **Откройте проект в VS Code**:
   ```bash
   code .
   ```

2. **Откройте AI Chat**:
   - Нажмите `Ctrl+Shift+P` (Windows/Linux) или `Cmd+Shift+P` (macOS)
   - Введите "AI Chat" и выберите "AI Chat: Open Chat"

3. **Проверьте подключение к MCP-серверу**:
   - В AI Chat введите `#zava` и выберите один из настроенных серверов
   - Спросите: "Какие таблицы доступны в базе данных?"
   - Вы должны получить ответ со списком таблиц розничной базы данных

## ✅ Проверка окружения

### 1. Комплексная проверка системы

Запустите этот скрипт для проверки настройки:

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

### 2. Контрольный список ручной проверки

**✅ Основные инструменты**
- [ ] Установлен и запущен Docker версии 20.10+
- [ ] Установлен и аутентифицирован Azure CLI версии 2.40+
- [ ] Установлен Python версии 3.8+ с pip
- [ ] Установлен Git версии 2.30+
- [ ] Установлен VS Code с необходимыми расширениями

**✅ Ресурсы Azure**
- [ ] Группа ресурсов успешно создана
- [ ] Проект AI Foundry развернут
- [ ] Модель OpenAI text-embedding-3-small развернута
- [ ] Application Insights настроен
- [ ] Сервисный принципал создан с нужными правами

**✅ Конфигурация окружения**
- [ ] Создан файл `.env` со всеми необходимыми переменными
- [ ] Работают учетные данные Azure (проверьте с помощью `az account show`)
- [ ] Контейнер PostgreSQL запущен и доступен
- [ ] В базу данных загружены тестовые данные

**✅ Интеграция VS Code**
- [ ] Настроен файл `.vscode/mcp.json`
- [ ] Интерпретатор Python установлен на виртуальное окружение
- [ ] MCP-серверы отображаются в AI Chat
- [ ] Можно выполнять тестовые запросы через AI Chat

## 🛠️ Устранение распространенных проблем

### Проблемы с Docker

**Проблема**: Контейнеры Docker не запускаются
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

**Проблема**: Ошибка подключения к PostgreSQL
```bash
# Check container logs
docker-compose logs postgres

# Verify container is healthy
docker-compose ps

# Test direct connection
docker-compose exec postgres psql -U postgres -d zava -c "SELECT 1;"
```

### Проблемы с развертыванием Azure

**Проблема**: Ошибка развертывания Azure
```bash
# Check Azure CLI authentication
az account show

# Verify subscription permissions
az role assignment list --assignee $(az account show --query user.name -o tsv)

# Check resource provider registration
az provider register --namespace Microsoft.CognitiveServices
az provider register --namespace Microsoft.Insights
```

**Проблема**: Ошибка аутентификации AI-сервиса
```bash
# Test service principal
az login --service-principal \
  --username $AZURE_CLIENT_ID \
  --password $AZURE_CLIENT_SECRET \
  --tenant $AZURE_TENANT_ID

# Verify AI service deployment
az cognitiveservices account list --query "[].{Name:name,Kind:kind,Location:location}"
```

### Проблемы с Python-окружением

**Проблема**: Ошибка установки пакетов
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

**Проблема**: VS Code не может найти интерпретатор Python
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

## 🎯 Основные выводы

После завершения этого практикума у вас должно быть:

✅ **Полное окружение разработки**: Все инструменты установлены и настроены  
✅ **Развернутые ресурсы Azure**: AI-сервисы и поддерживающая инфраструктура  
✅ **Запущенное окружение Docker**: Контейнеры PostgreSQL и MCP-сервера  
✅ **Интеграция с VS Code**: MCP-серверы настроены и доступны  
✅ **Проверенная настройка**: Все компоненты протестированы и работают вместе  
✅ **Знания по устранению неполадок**: Решения для распространенных проблем  

## 🚀 Что дальше

Когда окружение готово, переходите к **[Практикуму 04: Проектирование базы данных и схемы](../04-Database/README.md)**, чтобы:

- Подробно изучить схему розничной базы данных
- Понять многопользовательское моделирование данных
- Изучить реализацию управления доступом на уровне строк
- Поработать с тестовыми данными для розничной торговли

## 📚 Дополнительные ресурсы

### Инструменты разработки
- [Документация Docker](https://docs.docker.com/) — Полное руководство по Docker
- [Справочник Azure CLI](https://docs.microsoft.com/cli/azure/) — Команды Azure CLI
- [Документация VS Code](https://code.visualstudio.com/docs) — Настройка редактора и расширений

### Сервисы Azure
- [Документация Azure AI Foundry](https://docs.microsoft.com/azure/ai-foundry/) — Настройка AI-сервиса
- [Сервис Azure OpenAI](https://docs.microsoft.com/azure/cognitive-services/openai/) — Развертывание AI-моделей
- [Application Insights](https://docs.microsoft.com/azure/azure-monitor/app/app-insights-overview) — Настройка мониторинга

### Разработка на Python
- [Виртуальные окружения Python](https://docs.python.org/3/tutorial/venv.html) — Управление окружением
- [Документация AsyncIO](https://docs.python.org/3/library/asyncio.html) — Асинхронное программирование
- [Документация FastAPI](https://fastapi.tiangolo.com/) — Шаблоны веб-фреймворка

---

**Далее**: Окружение готово? Продолжайте с [Практикума 04: Проектирование базы данных и схемы](../04-Database/README.md)

---

**Отказ от ответственности**:  
Этот документ был переведен с помощью сервиса автоматического перевода [Co-op Translator](https://github.com/Azure/co-op-translator). Несмотря на наши усилия обеспечить точность, автоматические переводы могут содержать ошибки или неточности. Оригинальный документ на его родном языке следует считать авторитетным источником. Для получения критически важной информации рекомендуется профессиональный перевод человеком. Мы не несем ответственности за любые недоразумения или неправильные интерпретации, возникшие в результате использования данного перевода.