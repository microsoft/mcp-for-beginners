# Thiết Lập Môi Trường

## 🎯 Nội Dung Của Lab Này

Lab thực hành này hướng dẫn bạn thiết lập một môi trường phát triển hoàn chỉnh để xây dựng các máy chủ MCP với tích hợp PostgreSQL. Bạn sẽ cấu hình các công cụ cần thiết, triển khai tài nguyên Azure, và xác thực thiết lập trước khi tiến hành triển khai.

## Tổng Quan

Một môi trường phát triển đúng chuẩn là yếu tố quan trọng để phát triển máy chủ MCP thành công. Lab này cung cấp hướng dẫn từng bước để thiết lập Docker, các dịch vụ Azure, công cụ phát triển, và kiểm tra xem mọi thứ hoạt động chính xác cùng nhau.

Kết thúc lab này, bạn sẽ có một môi trường phát triển hoàn chỉnh sẵn sàng để xây dựng máy chủ MCP của Zava Retail.

## Mục Tiêu Học Tập

Kết thúc lab này, bạn sẽ có thể:

- **Cài đặt và cấu hình** tất cả các công cụ phát triển cần thiết  
- **Triển khai tài nguyên Azure** cần thiết cho máy chủ MCP  
- **Thiết lập các container Docker** cho PostgreSQL và máy chủ MCP  
- **Xác thực** thiết lập môi trường của bạn với các kết nối thử nghiệm  
- **Khắc phục sự cố** các vấn đề thiết lập và cấu hình thường gặp  
- **Hiểu** quy trình phát triển và cấu trúc tệp  

## 📋 Kiểm Tra Điều Kiện Tiên Quyết

Trước khi bắt đầu, hãy đảm bảo bạn có:

### Kiến Thức Yêu Cầu
- Sử dụng cơ bản dòng lệnh (Windows Command Prompt/PowerShell)  
- Hiểu về biến môi trường  
- Quen thuộc với kiểm soát phiên bản Git  
- Các khái niệm cơ bản về Docker (container, image, volume)  

### Yêu Cầu Hệ Thống
- **Hệ điều hành**: Windows 10/11, macOS, hoặc Linux  
- **RAM**: Tối thiểu 8GB (khuyến nghị 16GB)  
- **Dung lượng lưu trữ**: Ít nhất 10GB trống  
- **Mạng**: Kết nối Internet để tải xuống và triển khai Azure  

### Yêu Cầu Tài Khoản
- **Đăng ký Azure**: Gói miễn phí là đủ  
- **Tài khoản GitHub**: Để truy cập kho lưu trữ  
- **Tài khoản Docker Hub**: (Tùy chọn) Để xuất bản image tùy chỉnh  

## 🛠️ Cài Đặt Công Cụ

### 1. Cài Đặt Docker Desktop

Docker cung cấp môi trường container hóa cho thiết lập phát triển của chúng ta.

#### Cài Đặt Trên Windows

1. **Tải xuống Docker Desktop**:  
   ```cmd
   # Visit https://desktop.docker.com/win/stable/Docker%20Desktop%20Installer.exe
   # Or use Windows Package Manager
   winget install Docker.DockerDesktop
   ```
  
2. **Cài đặt và cấu hình**:  
   - Chạy trình cài đặt với quyền Quản trị viên  
   - Bật tích hợp WSL 2 khi được yêu cầu  
   - Khởi động lại máy tính sau khi hoàn tất cài đặt  

3. **Xác minh cài đặt**:  
   ```cmd
   docker --version
   docker-compose --version
   ```
  

#### Cài Đặt Trên macOS

1. **Tải xuống và cài đặt**:  
   ```bash
   # Download from https://desktop.docker.com/mac/stable/Docker.dmg
   # Or use Homebrew
   brew install --cask docker
   ```
  
2. **Khởi động Docker Desktop**:  
   - Mở Docker Desktop từ Applications  
   - Hoàn thành trình hướng dẫn thiết lập ban đầu  

3. **Xác minh cài đặt**:  
   ```bash
   docker --version
   docker-compose --version
   ```
  

#### Cài Đặt Trên Linux

1. **Cài đặt Docker Engine**:  
   ```bash
   # Ubuntu/Debian
   curl -fsSL https://get.docker.com -o get-docker.sh
   sudo sh get-docker.sh
   sudo usermod -aG docker $USER
   
   # Log out and back in for group changes to take effect
   ```
  
2. **Cài đặt Docker Compose**:  
   ```bash
   sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
   sudo chmod +x /usr/local/bin/docker-compose
   ```
  

### 2. Cài Đặt Azure CLI

Azure CLI cho phép triển khai và quản lý tài nguyên Azure.

#### Cài Đặt Trên Windows

```cmd
# Using Windows Package Manager
winget install Microsoft.AzureCLI

# Or download MSI from: https://aka.ms/installazurecliwindows
```
  

#### Cài Đặt Trên macOS

```bash
# Using Homebrew
brew install azure-cli

# Or using installer
curl -L https://aka.ms/InstallAzureCli | bash
```
  

#### Cài Đặt Trên Linux

```bash
# Ubuntu/Debian
curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash

# RHEL/CentOS
sudo rpm --import https://packages.microsoft.com/keys/microsoft.asc
sudo dnf install azure-cli
```
  

#### Xác Minh và Xác Thực

```bash
# Check installation
az version

# Login to Azure
az login

# Set default subscription (if you have multiple)
az account list --output table
az account set --subscription "Your-Subscription-Name"
```
  

### 3. Cài Đặt Git

Git cần thiết để clone kho lưu trữ và kiểm soát phiên bản.

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
  

### 4. Cài Đặt VS Code

Visual Studio Code cung cấp môi trường phát triển tích hợp với hỗ trợ MCP.

#### Cài Đặt

```cmd
# Windows
winget install Microsoft.VisualStudioCode

# macOS
brew install --cask visual-studio-code

# Linux (Ubuntu/Debian)
sudo snap install code --classic
```
  

#### Các Tiện Ích Mở Rộng Cần Thiết

Cài đặt các tiện ích mở rộng VS Code sau:

```bash
# Install via command line
code --install-extension ms-python.python
code --install-extension ms-vscode.vscode-json
code --install-extension ms-azuretools.vscode-docker
code --install-extension ms-vscode.azure-account
```
  
Hoặc cài đặt qua VS Code:  
1. Mở VS Code  
2. Đi tới Extensions (Ctrl+Shift+X)  
3. Cài đặt:  
   - **Python** (Microsoft)  
   - **Docker** (Microsoft)  
   - **Azure Account** (Microsoft)  
   - **JSON** (Microsoft)  

### 5. Cài Đặt Python

Python 3.8+ cần thiết cho phát triển máy chủ MCP.

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
  

#### Xác Minh Cài Đặt

```bash
python --version  # Should show Python 3.11.x
pip --version      # Should show pip version
```
  

## 🚀 Thiết Lập Dự Án

### 1. Clone Kho Lưu Trữ

```bash
# Clone the main repository
git clone https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail.git

# Navigate to the project directory
cd MCP-Server-and-PostgreSQL-Sample-Retail

# Verify repository structure
ls -la
```
  

### 2. Tạo Môi Trường Ảo Python

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
  

### 3. Cài Đặt Các Phụ Thuộc Python

```bash
# Install development dependencies
pip install -r requirements.lock.txt

# Verify key packages
pip list | grep fastmcp
pip list | grep asyncpg
pip list | grep azure
```
  

## ☁️ Triển Khai Tài Nguyên Azure

### 1. Hiểu Yêu Cầu Tài Nguyên

Máy chủ MCP của chúng ta yêu cầu các tài nguyên Azure sau:

| **Tài Nguyên**         | **Mục Đích**                     | **Chi Phí Ước Tính**       |  
|-------------------------|----------------------------------|----------------------------|  
| **Azure AI Foundry**    | Lưu trữ và quản lý mô hình AI   | $10-50/tháng              |  
| **OpenAI Deployment**   | Mô hình nhúng văn bản (text-embedding-3-small) | $5-20/tháng |  
| **Application Insights**| Giám sát và đo lường           | $5-15/tháng               |  
| **Resource Group**      | Tổ chức tài nguyên              | Miễn phí                  |  

### 2. Triển Khai Tài Nguyên Azure

#### Tùy Chọn A: Triển Khai Tự Động (Khuyến Nghị)

```bash
# Navigate to infrastructure directory
cd infra

# Windows - PowerShell
./deploy.ps1

# macOS/Linux - Bash
./deploy.sh
```
  
Script triển khai sẽ:  
1. Tạo một nhóm tài nguyên duy nhất  
2. Triển khai tài nguyên Azure AI Foundry  
3. Triển khai mô hình text-embedding-3-small  
4. Cấu hình Application Insights  
5. Tạo service principal để xác thực  
6. Tạo tệp `.env` với cấu hình  

#### Tùy Chọn B: Triển Khai Thủ Công

Nếu bạn muốn kiểm soát thủ công hoặc script tự động bị lỗi:

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
  

### 3. Xác Minh Triển Khai Azure

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
  

### 4. Cấu Hình Biến Môi Trường

Sau khi triển khai, bạn sẽ có tệp `.env`. Xác minh rằng nó chứa:

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
  

## 🐳 Thiết Lập Môi Trường Docker

### 1. Hiểu Thành Phần Docker

Môi trường phát triển của chúng ta sử dụng Docker Compose:

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
  

### 2. Khởi Động Môi Trường Phát Triển

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
  

### 3. Xác Minh Thiết Lập Cơ Sở Dữ Liệu

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
  

### 4. Kiểm Tra Máy Chủ MCP

```bash
# Check MCP server health
curl http://localhost:8000/health

# Test basic MCP endpoint
curl -X POST http://localhost:8000/mcp \
  -H "Content-Type: application/json" \
  -H "x-rls-user-id: 00000000-0000-0000-0000-000000000000" \
  -d '{"method": "tools/list", "params": {}}'
```
  

## 🔧 Cấu Hình VS Code

### 1. Cấu Hình Tích Hợp MCP

Tạo cấu hình MCP trong VS Code:

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
  

### 2. Cấu Hình Môi Trường Python

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
  

### 3. Kiểm Tra Tích Hợp VS Code

1. **Mở dự án trong VS Code**:  
   ```bash
   code .
   ```
  
2. **Mở AI Chat**:  
   - Nhấn `Ctrl+Shift+P` (Windows/Linux) hoặc `Cmd+Shift+P` (macOS)  
   - Gõ "AI Chat" và chọn "AI Chat: Open Chat"  

3. **Kiểm Tra Kết Nối Máy Chủ MCP**:  
   - Trong AI Chat, gõ `#zava` và chọn một trong các máy chủ đã cấu hình  
   - Hỏi: "Có những bảng nào trong cơ sở dữ liệu?"  
   - Bạn sẽ nhận được phản hồi liệt kê các bảng cơ sở dữ liệu bán lẻ  

## ✅ Xác Thực Môi Trường

### 1. Kiểm Tra Hệ Thống Toàn Diện

Chạy script xác thực này để kiểm tra thiết lập của bạn:

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
  

### 2. Danh Sách Kiểm Tra Xác Thực Thủ Công

**✅ Công Cụ Cơ Bản**  
- [ ] Docker phiên bản 20.10+ đã cài đặt và chạy  
- [ ] Azure CLI 2.40+ đã cài đặt và xác thực  
- [ ] Python 3.8+ với pip đã cài đặt  
- [ ] Git 2.30+ đã cài đặt  
- [ ] VS Code với các tiện ích mở rộng cần thiết  

**✅ Tài Nguyên Azure**  
- [ ] Nhóm tài nguyên đã tạo thành công  
- [ ] Dự án AI Foundry đã triển khai  
- [ ] Mô hình text-embedding-3-small đã triển khai  
- [ ] Application Insights đã cấu hình  
- [ ] Service principal đã tạo với quyền phù hợp  

**✅ Cấu Hình Môi Trường**  
- [ ] Tệp `.env` đã tạo với tất cả các biến cần thiết  
- [ ] Thông tin xác thực Azure hoạt động (kiểm tra với `az account show`)  
- [ ] Container PostgreSQL đang chạy và có thể truy cập  
- [ ] Dữ liệu mẫu đã tải vào cơ sở dữ liệu  

**✅ Tích Hợp VS Code**  
- [ ] `.vscode/mcp.json` đã cấu hình  
- [ ] Trình thông dịch Python được đặt thành môi trường ảo  
- [ ] Máy chủ MCP xuất hiện trong AI Chat  
- [ ] Có thể thực hiện các truy vấn thử nghiệm qua AI Chat  

## 🛠️ Khắc Phục Sự Cố Thường Gặp

### Vấn Đề Docker

**Vấn Đề**: Container Docker không khởi động  
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
  
**Vấn Đề**: Kết nối PostgreSQL thất bại  
```bash
# Check container logs
docker-compose logs postgres

# Verify container is healthy
docker-compose ps

# Test direct connection
docker-compose exec postgres psql -U postgres -d zava -c "SELECT 1;"
```
  

### Vấn Đề Triển Khai Azure

**Vấn Đề**: Triển khai Azure thất bại  
```bash
# Check Azure CLI authentication
az account show

# Verify subscription permissions
az role assignment list --assignee $(az account show --query user.name -o tsv)

# Check resource provider registration
az provider register --namespace Microsoft.CognitiveServices
az provider register --namespace Microsoft.Insights
```
  
**Vấn Đề**: Xác thực dịch vụ AI thất bại  
```bash
# Test service principal
az login --service-principal \
  --username $AZURE_CLIENT_ID \
  --password $AZURE_CLIENT_SECRET \
  --tenant $AZURE_TENANT_ID

# Verify AI service deployment
az cognitiveservices account list --query "[].{Name:name,Kind:kind,Location:location}"
```
  

### Vấn Đề Môi Trường Python

**Vấn Đề**: Cài đặt gói thất bại  
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
  
**Vấn Đề**: VS Code không tìm thấy trình thông dịch Python  
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
  

## 🎯 Những Điều Cần Nhớ

Sau khi hoàn thành lab này, bạn sẽ có:

✅ **Môi Trường Phát Triển Hoàn Chỉnh**: Tất cả công cụ đã cài đặt và cấu hình  
✅ **Tài Nguyên Azure Đã Triển Khai**: Dịch vụ AI và cơ sở hạ tầng hỗ trợ  
✅ **Môi Trường Docker Đang Chạy**: Container PostgreSQL và máy chủ MCP  
✅ **Tích Hợp VS Code**: Máy chủ MCP đã cấu hình và có thể truy cập  
✅ **Thiết Lập Đã Xác Thực**: Tất cả thành phần đã kiểm tra và hoạt động cùng nhau  
✅ **Kiến Thức Khắc Phục Sự Cố**: Các vấn đề thường gặp và giải pháp  

## 🚀 Tiếp Theo

Với môi trường của bạn đã sẵn sàng, tiếp tục với **[Lab 04: Thiết Kế Cơ Sở Dữ Liệu và Schema](../04-Database/README.md)** để:

- Khám phá chi tiết schema cơ sở dữ liệu bán lẻ  
- Hiểu về mô hình dữ liệu đa người thuê  
- Tìm hiểu về triển khai Bảo Mật Cấp Dòng (Row Level Security)  
- Làm việc với dữ liệu mẫu bán lẻ  

## 📚 Tài Nguyên Bổ Sung

### Công Cụ Phát Triển
- [Tài liệu Docker](https://docs.docker.com/) - Tham khảo đầy đủ về Docker  
- [Tham khảo Azure CLI](https://docs.microsoft.com/cli/azure/) - Lệnh Azure CLI  
- [Tài liệu VS Code](https://code.visualstudio.com/docs) - Cấu hình trình soạn thảo và tiện ích mở rộng  

### Dịch Vụ Azure
- [Tài liệu Azure AI Foundry](https://docs.microsoft.com/azure/ai-foundry/) - Cấu hình dịch vụ AI  
- [Dịch vụ Azure OpenAI](https://docs.microsoft.com/azure/cognitive-services/openai/) - Triển khai mô hình AI  
- [Application Insights](https://docs.microsoft.com/azure/azure-monitor/app/app-insights-overview) - Thiết lập giám sát  

### Phát Triển Python
- [Môi Trường Ảo Python](https://docs.python.org/3/tutorial/venv.html) - Quản lý môi trường  
- [Tài liệu AsyncIO](https://docs.python.org/3/library/asyncio.html) - Mẫu lập trình bất đồng bộ  
- [Tài liệu FastAPI](https://fastapi.tiangolo.com/) - Mẫu framework web  

---

**Tiếp Theo**: Môi trường đã sẵn sàng? Tiếp tục với [Lab 04: Thiết Kế Cơ Sở Dữ Liệu và Schema](../04-Database/README.md)  

---

**Tuyên bố miễn trừ trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ bản địa nên được coi là nguồn thông tin chính thức. Đối với các thông tin quan trọng, khuyến nghị sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm cho bất kỳ sự hiểu lầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.