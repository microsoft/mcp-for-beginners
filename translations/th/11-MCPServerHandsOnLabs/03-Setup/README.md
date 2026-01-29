# การตั้งค่าสภาพแวดล้อม

## 🎯 สิ่งที่คุณจะได้เรียนรู้ในห้องปฏิบัติการนี้

ห้องปฏิบัติการนี้จะช่วยคุณตั้งค่าสภาพแวดล้อมการพัฒนาแบบครบวงจรสำหรับการสร้างเซิร์ฟเวอร์ MCP ที่มีการผสานรวมกับ PostgreSQL คุณจะได้ตั้งค่าเครื่องมือที่จำเป็นทั้งหมด, ใช้ทรัพยากร Azure และตรวจสอบการตั้งค่าของคุณก่อนเริ่มการพัฒนา

## ภาพรวม

การมีสภาพแวดล้อมการพัฒนาที่เหมาะสมเป็นสิ่งสำคัญสำหรับการพัฒนาเซิร์ฟเวอร์ MCP ห้องปฏิบัติการนี้มีคำแนะนำทีละขั้นตอนสำหรับการตั้งค่า Docker, บริการ Azure, เครื่องมือพัฒนา และการตรวจสอบให้แน่ใจว่าทุกอย่างทำงานร่วมกันได้อย่างถูกต้อง

เมื่อจบห้องปฏิบัติการนี้ คุณจะมีสภาพแวดล้อมการพัฒนาที่พร้อมสำหรับการสร้างเซิร์ฟเวอร์ MCP ของ Zava Retail

## วัตถุประสงค์การเรียนรู้

เมื่อจบห้องปฏิบัติการนี้ คุณจะสามารถ:

- **ติดตั้งและตั้งค่า** เครื่องมือพัฒนาที่จำเป็นทั้งหมด
- **ใช้ทรัพยากร Azure** ที่จำเป็นสำหรับเซิร์ฟเวอร์ MCP
- **ตั้งค่า Docker containers** สำหรับ PostgreSQL และเซิร์ฟเวอร์ MCP
- **ตรวจสอบ** การตั้งค่าสภาพแวดล้อมของคุณด้วยการเชื่อมต่อทดสอบ
- **แก้ไขปัญหา** การตั้งค่าที่พบได้ทั่วไปและปัญหาการกำหนดค่า
- **เข้าใจ** เวิร์กโฟลว์การพัฒนาและโครงสร้างไฟล์

## 📋 การตรวจสอบความพร้อมก่อนเริ่ม

ก่อนเริ่มต้น โปรดตรวจสอบว่าคุณมี:

### ความรู้ที่จำเป็น
- การใช้งานคำสั่งพื้นฐาน (Windows Command Prompt/PowerShell)
- ความเข้าใจเกี่ยวกับตัวแปรสภาพแวดล้อม
- ความคุ้นเคยกับการควบคุมเวอร์ชัน Git
- แนวคิดพื้นฐานเกี่ยวกับ Docker (containers, images, volumes)

### ความต้องการของระบบ
- **ระบบปฏิบัติการ**: Windows 10/11, macOS หรือ Linux
- **RAM**: ขั้นต่ำ 8GB (แนะนำ 16GB)
- **พื้นที่เก็บข้อมูล**: อย่างน้อย 10GB พื้นที่ว่าง
- **เครือข่าย**: การเชื่อมต่ออินเทอร์เน็ตสำหรับการดาวน์โหลดและการใช้งาน Azure

### ความต้องการบัญชี
- **การสมัครสมาชิก Azure**: ระดับฟรีก็เพียงพอ
- **บัญชี GitHub**: สำหรับการเข้าถึง repository
- **บัญชี Docker Hub**: (ไม่บังคับ) สำหรับการเผยแพร่ image แบบกำหนดเอง

## 🛠️ การติดตั้งเครื่องมือ

### 1. ติดตั้ง Docker Desktop

Docker ให้สภาพแวดล้อมแบบ containerized สำหรับการตั้งค่าการพัฒนาของเรา

#### การติดตั้งบน Windows

1. **ดาวน์โหลด Docker Desktop**:
   ```cmd
   # Visit https://desktop.docker.com/win/stable/Docker%20Desktop%20Installer.exe
   # Or use Windows Package Manager
   winget install Docker.DockerDesktop
   ```

2. **ติดตั้งและตั้งค่า**:
   - รันตัวติดตั้งในฐานะผู้ดูแลระบบ
   - เปิดใช้งานการผสานรวม WSL 2 เมื่อมีการแจ้งเตือน
   - รีสตาร์ทคอมพิวเตอร์เมื่อการติดตั้งเสร็จสิ้น

3. **ตรวจสอบการติดตั้ง**:
   ```cmd
   docker --version
   docker-compose --version
   ```

#### การติดตั้งบน macOS

1. **ดาวน์โหลดและติดตั้ง**:
   ```bash
   # Download from https://desktop.docker.com/mac/stable/Docker.dmg
   # Or use Homebrew
   brew install --cask docker
   ```

2. **เริ่ม Docker Desktop**:
   - เปิด Docker Desktop จาก Applications
   - ทำตามตัวช่วยตั้งค่าเริ่มต้น

3. **ตรวจสอบการติดตั้ง**:
   ```bash
   docker --version
   docker-compose --version
   ```

#### การติดตั้งบน Linux

1. **ติดตั้ง Docker Engine**:
   ```bash
   # Ubuntu/Debian
   curl -fsSL https://get.docker.com -o get-docker.sh
   sudo sh get-docker.sh
   sudo usermod -aG docker $USER
   
   # Log out and back in for group changes to take effect
   ```

2. **ติดตั้ง Docker Compose**:
   ```bash
   sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
   sudo chmod +x /usr/local/bin/docker-compose
   ```

### 2. ติดตั้ง Azure CLI

Azure CLI ช่วยให้สามารถใช้งานและจัดการทรัพยากร Azure ได้

#### การติดตั้งบน Windows

```cmd
# Using Windows Package Manager
winget install Microsoft.AzureCLI

# Or download MSI from: https://aka.ms/installazurecliwindows
```

#### การติดตั้งบน macOS

```bash
# Using Homebrew
brew install azure-cli

# Or using installer
curl -L https://aka.ms/InstallAzureCli | bash
```

#### การติดตั้งบน Linux

```bash
# Ubuntu/Debian
curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash

# RHEL/CentOS
sudo rpm --import https://packages.microsoft.com/keys/microsoft.asc
sudo dnf install azure-cli
```

#### การตรวจสอบและการรับรองความถูกต้อง

```bash
# Check installation
az version

# Login to Azure
az login

# Set default subscription (if you have multiple)
az account list --output table
az account set --subscription "Your-Subscription-Name"
```

### 3. ติดตั้ง Git

Git จำเป็นสำหรับการโคลน repository และการควบคุมเวอร์ชัน

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

### 4. ติดตั้ง VS Code

Visual Studio Code เป็นสภาพแวดล้อมการพัฒนาที่มีการสนับสนุน MCP

#### การติดตั้ง

```cmd
# Windows
winget install Microsoft.VisualStudioCode

# macOS
brew install --cask visual-studio-code

# Linux (Ubuntu/Debian)
sudo snap install code --classic
```

#### ส่วนขยายที่จำเป็น

ติดตั้งส่วนขยาย VS Code เหล่านี้:

```bash
# Install via command line
code --install-extension ms-python.python
code --install-extension ms-vscode.vscode-json
code --install-extension ms-azuretools.vscode-docker
code --install-extension ms-vscode.azure-account
```

หรือ ติดตั้งผ่าน VS Code:
1. เปิด VS Code
2. ไปที่ Extensions (Ctrl+Shift+X)
3. ติดตั้ง:
   - **Python** (Microsoft)
   - **Docker** (Microsoft)
   - **Azure Account** (Microsoft)
   - **JSON** (Microsoft)

### 5. ติดตั้ง Python

Python 3.8+ จำเป็นสำหรับการพัฒนาเซิร์ฟเวอร์ MCP

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

#### ตรวจสอบการติดตั้ง

```bash
python --version  # Should show Python 3.11.x
pip --version      # Should show pip version
```

## 🚀 การตั้งค่าโปรเจกต์

### 1. โคลน Repository

```bash
# Clone the main repository
git clone https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail.git

# Navigate to the project directory
cd MCP-Server-and-PostgreSQL-Sample-Retail

# Verify repository structure
ls -la
```

### 2. สร้าง Python Virtual Environment

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

### 3. ติดตั้ง Python Dependencies

```bash
# Install development dependencies
pip install -r requirements.lock.txt

# Verify key packages
pip list | grep fastmcp
pip list | grep asyncpg
pip list | grep azure
```

## ☁️ การใช้งานทรัพยากร Azure

### 1. เข้าใจความต้องการทรัพยากร

เซิร์ฟเวอร์ MCP ของเราต้องการทรัพยากร Azure เหล่านี้:

| **ทรัพยากร** | **วัตถุประสงค์** | **ค่าใช้จ่ายโดยประมาณ** |
|---------------|--------------------|--------------------------|
| **Azure AI Foundry** | การโฮสต์และการจัดการโมเดล AI | $10-50/เดือน |
| **OpenAI Deployment** | โมเดลการฝังข้อความ (text-embedding-3-small) | $5-20/เดือน |
| **Application Insights** | การตรวจสอบและการวิเคราะห์ | $5-15/เดือน |
| **Resource Group** | การจัดระเบียบทรัพยากร | ฟรี |

### 2. ใช้งานทรัพยากร Azure

#### ตัวเลือก A: การใช้งานแบบอัตโนมัติ (แนะนำ)

```bash
# Navigate to infrastructure directory
cd infra

# Windows - PowerShell
./deploy.ps1

# macOS/Linux - Bash
./deploy.sh
```

สคริปต์การใช้งานจะ:
1. สร้าง resource group ที่ไม่ซ้ำกัน
2. ใช้งานทรัพยากร Azure AI Foundry
3. ใช้งานโมเดล text-embedding-3-small
4. ตั้งค่า Application Insights
5. สร้าง service principal สำหรับการรับรองความถูกต้อง
6. สร้างไฟล์ `.env` พร้อมการกำหนดค่า

#### ตัวเลือก B: การใช้งานแบบแมนนวล

หากคุณต้องการควบคุมด้วยตนเองหรือสคริปต์อัตโนมัติล้มเหลว:

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

### 3. ตรวจสอบการใช้งาน Azure

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

### 4. ตั้งค่าตัวแปรสภาพแวดล้อม

หลังการใช้งาน คุณควรมีไฟล์ `.env` ตรวจสอบให้แน่ใจว่ามี:

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

## 🐳 การตั้งค่าสภาพแวดล้อม Docker

### 1. เข้าใจ Docker Composition

สภาพแวดล้อมการพัฒนาของเราใช้ Docker Compose:

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

### 2. เริ่มต้นสภาพแวดล้อมการพัฒนา

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

### 3. ตรวจสอบการตั้งค่าฐานข้อมูล

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

### 4. ทดสอบเซิร์ฟเวอร์ MCP

```bash
# Check MCP server health
curl http://localhost:8000/health

# Test basic MCP endpoint
curl -X POST http://localhost:8000/mcp \
  -H "Content-Type: application/json" \
  -H "x-rls-user-id: 00000000-0000-0000-0000-000000000000" \
  -d '{"method": "tools/list", "params": {}}'
```

## 🔧 การตั้งค่า VS Code

### 1. ตั้งค่าการผสานรวม MCP

สร้างการตั้งค่า MCP ใน VS Code:

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

### 2. ตั้งค่าสภาพแวดล้อม Python

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

### 3. ทดสอบการผสานรวม VS Code

1. **เปิดโปรเจกต์ใน VS Code**:
   ```bash
   code .
   ```

2. **เปิด AI Chat**:
   - กด `Ctrl+Shift+P` (Windows/Linux) หรือ `Cmd+Shift+P` (macOS)
   - พิมพ์ "AI Chat" และเลือก "AI Chat: Open Chat"

3. **ทดสอบการเชื่อมต่อเซิร์ฟเวอร์ MCP**:
   - ใน AI Chat พิมพ์ `#zava` และเลือกหนึ่งในเซิร์ฟเวอร์ที่ตั้งค่าไว้
   - ถาม: "มีตารางอะไรบ้างในฐานข้อมูล?"
   - คุณควรได้รับคำตอบที่แสดงรายการตารางในฐานข้อมูลค้าปลีก

## ✅ การตรวจสอบสภาพแวดล้อม

### 1. การตรวจสอบระบบแบบครอบคลุม

รันสคริปต์การตรวจสอบนี้เพื่อยืนยันการตั้งค่าของคุณ:

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

### 2. รายการตรวจสอบการตรวจสอบแบบแมนนวล

**✅ เครื่องมือพื้นฐาน**
- [ ] ติดตั้ง Docker เวอร์ชัน 20.10+ และกำลังทำงาน
- [ ] ติดตั้ง Azure CLI เวอร์ชัน 2.40+ และรับรองความถูกต้อง
- [ ] ติดตั้ง Python 3.8+ พร้อม pip
- [ ] ติดตั้ง Git เวอร์ชัน 2.30+
- [ ] ติดตั้ง VS Code พร้อมส่วนขยายที่จำเป็น

**✅ ทรัพยากร Azure**
- [ ] สร้าง resource group สำเร็จ
- [ ] ใช้งานโปรเจกต์ AI Foundry
- [ ] ใช้งานโมเดล text-embedding-3-small
- [ ] ตั้งค่า Application Insights
- [ ] สร้าง service principal พร้อมสิทธิ์ที่เหมาะสม

**✅ การตั้งค่าสภาพแวดล้อม**
- [ ] สร้างไฟล์ `.env` พร้อมตัวแปรที่จำเป็นทั้งหมด
- [ ] การรับรองความถูกต้องของ Azure ทำงาน (ทดสอบด้วย `az account show`)
- [ ] PostgreSQL container กำลังทำงานและเข้าถึงได้
- [ ] โหลดข้อมูลตัวอย่างในฐานข้อมูล

**✅ การผสานรวม VS Code**
- [ ] ตั้งค่า `.vscode/mcp.json`
- [ ] ตั้งค่าตัวแปล Python เป็น virtual environment
- [ ] เซิร์ฟเวอร์ MCP ปรากฏใน AI Chat
- [ ] สามารถรันคำสั่งทดสอบผ่าน AI Chat

## 🛠️ การแก้ไขปัญหาที่พบได้ทั่วไป

### ปัญหา Docker

**ปัญหา**: Docker containers ไม่เริ่มต้น
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

**ปัญหา**: การเชื่อมต่อ PostgreSQL ล้มเหลว
```bash
# Check container logs
docker-compose logs postgres

# Verify container is healthy
docker-compose ps

# Test direct connection
docker-compose exec postgres psql -U postgres -d zava -c "SELECT 1;"
```

### ปัญหาการใช้งาน Azure

**ปัญหา**: การใช้งาน Azure ล้มเหลว
```bash
# Check Azure CLI authentication
az account show

# Verify subscription permissions
az role assignment list --assignee $(az account show --query user.name -o tsv)

# Check resource provider registration
az provider register --namespace Microsoft.CognitiveServices
az provider register --namespace Microsoft.Insights
```

**ปัญหา**: การรับรองความถูกต้องของบริการ AI ล้มเหลว
```bash
# Test service principal
az login --service-principal \
  --username $AZURE_CLIENT_ID \
  --password $AZURE_CLIENT_SECRET \
  --tenant $AZURE_TENANT_ID

# Verify AI service deployment
az cognitiveservices account list --query "[].{Name:name,Kind:kind,Location:location}"
```

### ปัญหาสภาพแวดล้อม Python

**ปัญหา**: การติดตั้งแพ็กเกจล้มเหลว
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

**ปัญหา**: VS Code ไม่สามารถค้นหาตัวแปล Python ได้
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

## 🎯 สิ่งสำคัญที่ควรทราบ

หลังจากจบห้องปฏิบัติการนี้ คุณควรมี:

✅ **สภาพแวดล้อมการพัฒนาที่สมบูรณ์**: ติดตั้งและตั้งค่าเครื่องมือทั้งหมด  
✅ **ทรัพยากร Azure ที่ใช้งานแล้ว**: บริการ AI และโครงสร้างพื้นฐานที่สนับสนุน  
✅ **สภาพแวดล้อม Docker ที่ทำงานได้**: PostgreSQL และเซิร์ฟเวอร์ MCP containers  
✅ **การผสานรวม VS Code**: เซิร์ฟเวอร์ MCP ที่ตั้งค่าและเข้าถึงได้  
✅ **การตั้งค่าที่ผ่านการตรวจสอบ**: ทดสอบและทำงานร่วมกันได้ทุกส่วน  
✅ **ความรู้ในการแก้ไขปัญหา**: ปัญหาที่พบได้ทั่วไปและวิธีแก้ไข  

## 🚀 สิ่งที่ต้องทำต่อไป

เมื่อสภาพแวดล้อมของคุณพร้อมแล้ว ให้ดำเนินการต่อที่ **[Lab 04: การออกแบบฐานข้อมูลและ Schema](../04-Database/README.md)** เพื่อ:

- สำรวจ Schema ฐานข้อมูลค้าปลีกอย่างละเอียด
- เข้าใจการออกแบบข้อมูลแบบ multi-tenant
- เรียนรู้เกี่ยวกับการใช้งาน Row Level Security
- ทำงานกับข้อมูลค้าปลีกตัวอย่าง

## 📚 แหล่งข้อมูลเพิ่มเติม

### เครื่องมือพัฒนา
- [เอกสาร Docker](https://docs.docker.com/) - อ้างอิง Docker แบบครบถ้วน
- [เอกสาร Azure CLI](https://docs.microsoft.com/cli/azure/) - คำสั่ง Azure CLI
- [เอกสาร VS Code](https://code.visualstudio.com/docs) - การตั้งค่าและส่วนขยายของ Editor

### บริการ Azure
- [เอกสาร Azure AI Foundry](https://docs.microsoft.com/azure/ai-foundry/) - การตั้งค่าบริการ AI
- [บริการ Azure OpenAI](https://docs.microsoft.com/azure/cognitive-services/openai/) - การใช้งานโมเดล AI
- [Application Insights](https://docs.microsoft.com/azure/azure-monitor/app/app-insights-overview) - การตั้งค่าการตรวจสอบ

### การพัฒนา Python
- [Python Virtual Environments](https://docs.python.org/3/tutorial/venv.html) - การจัดการสภาพแวดล้อม
- [เอกสาร AsyncIO](https://docs.python.org/3/library/asyncio.html) - รูปแบบการเขียนโปรแกรมแบบ Async
- [เอกสาร FastAPI](https://fastapi.tiangolo.com/) - รูปแบบการพัฒนาเว็บ

---

**ถัดไป**: สภาพแวดล้อมพร้อมแล้ว? ดำเนินการต่อที่ [Lab 04: การออกแบบฐานข้อมูลและ Schema](../04-Database/README.md)

---

**ข้อจำกัดความรับผิดชอบ**:  
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษา AI [Co-op Translator](https://github.com/Azure/co-op-translator) แม้ว่าเราจะพยายามให้การแปลมีความถูกต้อง แต่โปรดทราบว่าการแปลโดยอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาดั้งเดิมควรถือเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ ขอแนะนำให้ใช้บริการแปลภาษามนุษย์ที่มีความเชี่ยวชาญ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความผิดที่เกิดจากการใช้การแปลนี้