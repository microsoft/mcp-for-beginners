# 환경 설정

## 🎯 이 실습에서 다루는 내용

이 실습은 PostgreSQL 통합을 통해 MCP 서버를 구축하기 위한 완전한 개발 환경을 설정하는 과정을 안내합니다. 필요한 모든 도구를 구성하고, Azure 리소스를 배포하며, 구현을 진행하기 전에 설정을 검증합니다.

## 개요

적절한 개발 환경은 MCP 서버 개발의 성공에 필수적입니다. 이 실습은 Docker, Azure 서비스, 개발 도구를 설정하고 모든 것이 올바르게 작동하는지 확인하는 단계별 지침을 제공합니다.

이 실습을 완료하면 Zava Retail MCP 서버를 구축할 준비가 된 완전한 개발 환경을 갖추게 됩니다.

## 학습 목표

이 실습을 완료하면 다음을 수행할 수 있습니다:

- **필요한 개발 도구 설치 및 구성**
- **MCP 서버에 필요한 Azure 리소스 배포**
- **PostgreSQL 및 MCP 서버를 위한 Docker 컨테이너 설정**
- **테스트 연결을 통해 환경 설정 검증**
- **일반적인 설정 문제 및 구성 문제 해결**
- **개발 워크플로 및 파일 구조 이해**

## 📋 사전 요구 사항 확인

시작하기 전에 다음을 확인하세요:

### 필요한 지식
- 기본 명령줄 사용법 (Windows Command Prompt/PowerShell)
- 환경 변수에 대한 이해
- Git 버전 관리에 대한 기본 지식
- Docker의 기본 개념 (컨테이너, 이미지, 볼륨)

### 시스템 요구 사항
- **운영 체제**: Windows 10/11, macOS 또는 Linux
- **RAM**: 최소 8GB (권장 16GB)
- **저장 공간**: 최소 10GB의 여유 공간
- **네트워크**: 다운로드 및 Azure 배포를 위한 인터넷 연결

### 계정 요구 사항
- **Azure 구독**: 무료 계층으로 충분
- **GitHub 계정**: 리포지토리 액세스를 위해
- **Docker Hub 계정**: (선택 사항) 사용자 정의 이미지 게시를 위해

## 🛠️ 도구 설치

### 1. Docker Desktop 설치

Docker는 개발 환경을 컨테이너화된 형태로 제공합니다.

#### Windows 설치

1. **Docker Desktop 다운로드**:
   ```cmd
   # Visit https://desktop.docker.com/win/stable/Docker%20Desktop%20Installer.exe
   # Or use Windows Package Manager
   winget install Docker.DockerDesktop
   ```

2. **설치 및 구성**:
   - 관리자 권한으로 설치 프로그램 실행
   - WSL 2 통합 활성화
   - 설치 완료 후 컴퓨터 재시작

3. **설치 확인**:
   ```cmd
   docker --version
   docker-compose --version
   ```

#### macOS 설치

1. **다운로드 및 설치**:
   ```bash
   # Download from https://desktop.docker.com/mac/stable/Docker.dmg
   # Or use Homebrew
   brew install --cask docker
   ```

2. **Docker Desktop 시작**:
   - 응용 프로그램에서 Docker Desktop 실행
   - 초기 설정 마법사 완료

3. **설치 확인**:
   ```bash
   docker --version
   docker-compose --version
   ```

#### Linux 설치

1. **Docker Engine 설치**:
   ```bash
   # Ubuntu/Debian
   curl -fsSL https://get.docker.com -o get-docker.sh
   sudo sh get-docker.sh
   sudo usermod -aG docker $USER
   
   # Log out and back in for group changes to take effect
   ```

2. **Docker Compose 설치**:
   ```bash
   sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
   sudo chmod +x /usr/local/bin/docker-compose
   ```

### 2. Azure CLI 설치

Azure CLI는 Azure 리소스 배포 및 관리를 가능하게 합니다.

#### Windows 설치

```cmd
# Using Windows Package Manager
winget install Microsoft.AzureCLI

# Or download MSI from: https://aka.ms/installazurecliwindows
```

#### macOS 설치

```bash
# Using Homebrew
brew install azure-cli

# Or using installer
curl -L https://aka.ms/InstallAzureCli | bash
```

#### Linux 설치

```bash
# Ubuntu/Debian
curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash

# RHEL/CentOS
sudo rpm --import https://packages.microsoft.com/keys/microsoft.asc
sudo dnf install azure-cli
```

#### 설치 확인 및 인증

```bash
# Check installation
az version

# Login to Azure
az login

# Set default subscription (if you have multiple)
az account list --output table
az account set --subscription "Your-Subscription-Name"
```

### 3. Git 설치

Git은 리포지토리 클론 및 버전 관리를 위해 필요합니다.

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

### 4. VS Code 설치

Visual Studio Code는 MCP 지원을 위한 통합 개발 환경을 제공합니다.

#### 설치

```cmd
# Windows
winget install Microsoft.VisualStudioCode

# macOS
brew install --cask visual-studio-code

# Linux (Ubuntu/Debian)
sudo snap install code --classic
```

#### 필수 확장 프로그램

다음 VS Code 확장 프로그램을 설치하세요:

```bash
# Install via command line
code --install-extension ms-python.python
code --install-extension ms-vscode.vscode-json
code --install-extension ms-azuretools.vscode-docker
code --install-extension ms-vscode.azure-account
```

또는 VS Code를 통해 설치:
1. VS Code 열기
2. 확장 프로그램으로 이동 (Ctrl+Shift+X)
3. 설치:
   - **Python** (Microsoft)
   - **Docker** (Microsoft)
   - **Azure Account** (Microsoft)
   - **JSON** (Microsoft)

### 5. Python 설치

Python 3.8+는 MCP 서버 개발에 필요합니다.

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

#### 설치 확인

```bash
python --version  # Should show Python 3.11.x
pip --version      # Should show pip version
```

## 🚀 프로젝트 설정

### 1. 리포지토리 클론

```bash
# Clone the main repository
git clone https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail.git

# Navigate to the project directory
cd MCP-Server-and-PostgreSQL-Sample-Retail

# Verify repository structure
ls -la
```

### 2. Python 가상 환경 생성

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

### 3. Python 종속성 설치

```bash
# Install development dependencies
pip install -r requirements.lock.txt

# Verify key packages
pip list | grep fastmcp
pip list | grep asyncpg
pip list | grep azure
```

## ☁️ Azure 리소스 배포

### 1. 리소스 요구 사항 이해

MCP 서버에는 다음 Azure 리소스가 필요합니다:

| **리소스** | **목적** | **예상 비용** |
|------------|----------|---------------|
| **Azure AI Foundry** | AI 모델 호스팅 및 관리 | 월 $10-50 |
| **OpenAI 배포** | 텍스트 임베딩 모델 (text-embedding-3-small) | 월 $5-20 |
| **Application Insights** | 모니터링 및 원격 분석 | 월 $5-15 |
| **Resource Group** | 리소스 조직 | 무료 |

### 2. Azure 리소스 배포

#### 옵션 A: 자동 배포 (권장)

```bash
# Navigate to infrastructure directory
cd infra

# Windows - PowerShell
./deploy.ps1

# macOS/Linux - Bash
./deploy.sh
```

배포 스크립트는 다음을 수행합니다:
1. 고유한 리소스 그룹 생성
2. Azure AI Foundry 리소스 배포
3. text-embedding-3-small 모델 배포
4. Application Insights 구성
5. 인증을 위한 서비스 주체 생성
6. 구성된 `.env` 파일 생성

#### 옵션 B: 수동 배포

자동 스크립트가 실패하거나 수동 제어를 선호하는 경우:

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

### 3. Azure 배포 확인

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

### 4. 환경 변수 구성

배포 후 `.env` 파일이 있어야 합니다. 다음을 포함하는지 확인하세요:

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

## 🐳 Docker 환경 설정

### 1. Docker 구성 이해

개발 환경은 Docker Compose를 사용합니다:

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

### 2. 개발 환경 시작

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

### 3. 데이터베이스 설정 확인

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

### 4. MCP 서버 테스트

```bash
# Check MCP server health
curl http://localhost:8000/health

# Test basic MCP endpoint
curl -X POST http://localhost:8000/mcp \
  -H "Content-Type: application/json" \
  -H "x-rls-user-id: 00000000-0000-0000-0000-000000000000" \
  -d '{"method": "tools/list", "params": {}}'
```

## 🔧 VS Code 구성

### 1. MCP 통합 구성

VS Code MCP 구성을 생성하세요:

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

### 2. Python 환경 구성

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

### 3. VS Code 통합 테스트

1. **프로젝트를 VS Code에서 열기**:
   ```bash
   code .
   ```

2. **AI Chat 열기**:
   - `Ctrl+Shift+P` (Windows/Linux) 또는 `Cmd+Shift+P` (macOS) 누르기
   - "AI Chat" 입력 후 "AI Chat: Open Chat" 선택

3. **MCP 서버 연결 테스트**:
   - AI Chat에서 `#zava` 입력 후 구성된 서버 중 하나 선택
   - 질문: "데이터베이스에 어떤 테이블이 있나요?"
   - 소매 데이터베이스 테이블 목록을 포함한 응답을 받아야 합니다

## ✅ 환경 검증

### 1. 종합 시스템 점검

설정을 확인하기 위해 이 검증 스크립트를 실행하세요:

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

### 2. 수동 검증 체크리스트

**✅ 기본 도구**
- [ ] Docker 버전 20.10+ 설치 및 실행 중
- [ ] Azure CLI 2.40+ 설치 및 인증 완료
- [ ] Python 3.8+ 및 pip 설치 완료
- [ ] Git 2.30+ 설치 완료
- [ ] VS Code 및 필수 확장 프로그램 설치 완료

**✅ Azure 리소스**
- [ ] 리소스 그룹 성공적으로 생성됨
- [ ] AI Foundry 프로젝트 배포 완료
- [ ] OpenAI text-embedding-3-small 모델 배포 완료
- [ ] Application Insights 구성 완료
- [ ] 적절한 권한을 가진 서비스 주체 생성됨

**✅ 환경 구성**
- [ ] `.env` 파일 생성 및 모든 필수 변수 포함
- [ ] Azure 자격 증명 작동 (`az account show`로 테스트)
- [ ] PostgreSQL 컨테이너 실행 및 접근 가능
- [ ] 데이터베이스에 샘플 데이터 로드 완료

**✅ VS Code 통합**
- [ ] `.vscode/mcp.json` 구성 완료
- [ ] Python 인터프리터를 가상 환경으로 설정
- [ ] MCP 서버가 AI Chat에 표시됨
- [ ] AI Chat을 통해 테스트 쿼리 실행 가능

## 🛠️ 일반적인 문제 해결

### Docker 문제

**문제**: Docker 컨테이너가 시작되지 않음
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

**문제**: PostgreSQL 연결 실패
```bash
# Check container logs
docker-compose logs postgres

# Verify container is healthy
docker-compose ps

# Test direct connection
docker-compose exec postgres psql -U postgres -d zava -c "SELECT 1;"
```

### Azure 배포 문제

**문제**: Azure 배포 실패
```bash
# Check Azure CLI authentication
az account show

# Verify subscription permissions
az role assignment list --assignee $(az account show --query user.name -o tsv)

# Check resource provider registration
az provider register --namespace Microsoft.CognitiveServices
az provider register --namespace Microsoft.Insights
```

**문제**: AI 서비스 인증 실패
```bash
# Test service principal
az login --service-principal \
  --username $AZURE_CLIENT_ID \
  --password $AZURE_CLIENT_SECRET \
  --tenant $AZURE_TENANT_ID

# Verify AI service deployment
az cognitiveservices account list --query "[].{Name:name,Kind:kind,Location:location}"
```

### Python 환경 문제

**문제**: 패키지 설치 실패
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

**문제**: VS Code에서 Python 인터프리터를 찾을 수 없음
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

## 🎯 주요 요점

이 실습을 완료한 후, 다음을 갖추게 됩니다:

✅ **완전한 개발 환경**: 모든 도구 설치 및 구성 완료  
✅ **Azure 리소스 배포**: AI 서비스 및 지원 인프라  
✅ **Docker 환경 실행**: PostgreSQL 및 MCP 서버 컨테이너  
✅ **VS Code 통합**: MCP 서버 구성 및 접근 가능  
✅ **설정 검증 완료**: 모든 구성 요소 테스트 및 작동 확인  
✅ **문제 해결 지식**: 일반적인 문제 및 해결 방법  

## 🚀 다음 단계

환경이 준비되었으면 **[Lab 04: 데이터베이스 설계 및 스키마](../04-Database/README.md)**로 계속 진행하세요:

- 소매 데이터베이스 스키마를 자세히 탐색
- 멀티 테넌트 데이터 모델링 이해
- 행 수준 보안 구현 학습
- 샘플 소매 데이터 작업

## 📚 추가 자료

### 개발 도구
- [Docker 문서](https://docs.docker.com/) - Docker 참조 자료
- [Azure CLI 참조](https://docs.microsoft.com/cli/azure/) - Azure CLI 명령어
- [VS Code 문서](https://code.visualstudio.com/docs) - 편집기 구성 및 확장 프로그램

### Azure 서비스
- [Azure AI Foundry 문서](https://docs.microsoft.com/azure/ai-foundry/) - AI 서비스 구성
- [Azure OpenAI 서비스](https://docs.microsoft.com/azure/cognitive-services/openai/) - AI 모델 배포
- [Application Insights](https://docs.microsoft.com/azure/azure-monitor/app/app-insights-overview) - 모니터링 설정

### Python 개발
- [Python 가상 환경](https://docs.python.org/3/tutorial/venv.html) - 환경 관리
- [AsyncIO 문서](https://docs.python.org/3/library/asyncio.html) - 비동기 프로그래밍 패턴
- [FastAPI 문서](https://fastapi.tiangolo.com/) - 웹 프레임워크 패턴

---

**다음**: 환경이 준비되었나요? [Lab 04: 데이터베이스 설계 및 스키마](../04-Database/README.md)로 계속 진행하세요.

---

**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 최선을 다하고 있으나, 자동 번역에는 오류나 부정확성이 포함될 수 있습니다. 원본 문서의 원어 버전을 신뢰할 수 있는 권위 있는 자료로 간주해야 합니다. 중요한 정보의 경우, 전문적인 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.