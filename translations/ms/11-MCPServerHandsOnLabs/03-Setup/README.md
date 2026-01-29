# Persediaan Persekitaran

## 🎯 Apa Yang Diliputi Dalam Makmal Ini

Makmal praktikal ini membimbing anda untuk menyediakan persekitaran pembangunan lengkap bagi membina pelayan MCP dengan integrasi PostgreSQL. Anda akan mengkonfigurasi semua alat yang diperlukan, melancarkan sumber Azure, dan mengesahkan persediaan anda sebelum meneruskan dengan pelaksanaan.

## Gambaran Keseluruhan

Persekitaran pembangunan yang betul adalah penting untuk pembangunan pelayan MCP yang berjaya. Makmal ini menyediakan arahan langkah demi langkah untuk menyediakan Docker, perkhidmatan Azure, alat pembangunan, dan mengesahkan bahawa semuanya berfungsi dengan betul bersama-sama.

Pada akhir makmal ini, anda akan mempunyai persekitaran pembangunan yang berfungsi sepenuhnya untuk membina pelayan MCP Zava Retail.

## Objektif Pembelajaran

Pada akhir makmal ini, anda akan dapat:

- **Memasang dan mengkonfigurasi** semua alat pembangunan yang diperlukan
- **Melancarkan sumber Azure** yang diperlukan untuk pelayan MCP
- **Menyiapkan kontena Docker** untuk PostgreSQL dan pelayan MCP
- **Mengesahkan** persediaan persekitaran anda dengan sambungan ujian
- **Menyelesaikan masalah** isu persediaan biasa dan masalah konfigurasi
- **Memahami** aliran kerja pembangunan dan struktur fail

## 📋 Semakan Prasyarat

Sebelum memulakan, pastikan anda mempunyai:

### Pengetahuan Diperlukan
- Penggunaan baris arahan asas (Windows Command Prompt/PowerShell)
- Pemahaman tentang pembolehubah persekitaran
- Kefahaman tentang kawalan versi Git
- Konsep Docker asas (kontena, imej, volume)

### Keperluan Sistem
- **Sistem Operasi**: Windows 10/11, macOS, atau Linux
- **RAM**: Minimum 8GB (16GB disyorkan)
- **Storan**: Sekurang-kurangnya 10GB ruang kosong
- **Rangkaian**: Sambungan internet untuk muat turun dan pelancaran Azure

### Keperluan Akaun
- **Langganan Azure**: Tier percuma mencukupi
- **Akaun GitHub**: Untuk akses repositori
- **Akaun Docker Hub**: (Pilihan) Untuk penerbitan imej tersuai

## 🛠️ Pemasangan Alat

### 1. Pasang Docker Desktop

Docker menyediakan persekitaran kontena untuk persediaan pembangunan kita.

#### Pemasangan Windows

1. **Muat turun Docker Desktop**:
   ```cmd
   # Visit https://desktop.docker.com/win/stable/Docker%20Desktop%20Installer.exe
   # Or use Windows Package Manager
   winget install Docker.DockerDesktop
   ```

2. **Pasang dan Konfigurasi**:
   - Jalankan pemasang sebagai Pentadbir
   - Aktifkan integrasi WSL 2 apabila diminta
   - Mulakan semula komputer anda apabila pemasangan selesai

3. **Sahkan Pemasangan**:
   ```cmd
   docker --version
   docker-compose --version
   ```

#### Pemasangan macOS

1. **Muat turun dan Pasang**:
   ```bash
   # Download from https://desktop.docker.com/mac/stable/Docker.dmg
   # Or use Homebrew
   brew install --cask docker
   ```

2. **Mulakan Docker Desktop**:
   - Lancarkan Docker Desktop dari Aplikasi
   - Lengkapkan wizard persediaan awal

3. **Sahkan Pemasangan**:
   ```bash
   docker --version
   docker-compose --version
   ```

#### Pemasangan Linux

1. **Pasang Docker Engine**:
   ```bash
   # Ubuntu/Debian
   curl -fsSL https://get.docker.com -o get-docker.sh
   sudo sh get-docker.sh
   sudo usermod -aG docker $USER
   
   # Log out and back in for group changes to take effect
   ```

2. **Pasang Docker Compose**:
   ```bash
   sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
   sudo chmod +x /usr/local/bin/docker-compose
   ```

### 2. Pasang Azure CLI

Azure CLI membolehkan pelancaran dan pengurusan sumber Azure.

#### Pemasangan Windows

```cmd
# Using Windows Package Manager
winget install Microsoft.AzureCLI

# Or download MSI from: https://aka.ms/installazurecliwindows
```

#### Pemasangan macOS

```bash
# Using Homebrew
brew install azure-cli

# Or using installer
curl -L https://aka.ms/InstallAzureCli | bash
```

#### Pemasangan Linux

```bash
# Ubuntu/Debian
curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash

# RHEL/CentOS
sudo rpm --import https://packages.microsoft.com/keys/microsoft.asc
sudo dnf install azure-cli
```

#### Sahkan dan Pengesahan

```bash
# Check installation
az version

# Login to Azure
az login

# Set default subscription (if you have multiple)
az account list --output table
az account set --subscription "Your-Subscription-Name"
```

### 3. Pasang Git

Git diperlukan untuk mengklon repositori dan kawalan versi.

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

### 4. Pasang VS Code

Visual Studio Code menyediakan persekitaran pembangunan bersepadu dengan sokongan MCP.

#### Pemasangan

```cmd
# Windows
winget install Microsoft.VisualStudioCode

# macOS
brew install --cask visual-studio-code

# Linux (Ubuntu/Debian)
sudo snap install code --classic
```

#### Sambungan Diperlukan

Pasang sambungan VS Code berikut:

```bash
# Install via command line
code --install-extension ms-python.python
code --install-extension ms-vscode.vscode-json
code --install-extension ms-azuretools.vscode-docker
code --install-extension ms-vscode.azure-account
```

Atau pasang melalui VS Code:
1. Buka VS Code
2. Pergi ke Sambungan (Ctrl+Shift+X)
3. Pasang:
   - **Python** (Microsoft)
   - **Docker** (Microsoft)
   - **Azure Account** (Microsoft)
   - **JSON** (Microsoft)

### 5. Pasang Python

Python 3.8+ diperlukan untuk pembangunan pelayan MCP.

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

#### Sahkan Pemasangan

```bash
python --version  # Should show Python 3.11.x
pip --version      # Should show pip version
```

## 🚀 Persediaan Projek

### 1. Klon Repositori

```bash
# Clone the main repository
git clone https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail.git

# Navigate to the project directory
cd MCP-Server-and-PostgreSQL-Sample-Retail

# Verify repository structure
ls -la
```

### 2. Buat Persekitaran Maya Python

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

### 3. Pasang Kebergantungan Python

```bash
# Install development dependencies
pip install -r requirements.lock.txt

# Verify key packages
pip list | grep fastmcp
pip list | grep asyncpg
pip list | grep azure
```

## ☁️ Pelancaran Sumber Azure

### 1. Fahami Keperluan Sumber

Pelayan MCP kita memerlukan sumber Azure berikut:

| **Sumber** | **Tujuan** | **Anggaran Kos** |
|------------|------------|------------------|
| **Azure AI Foundry** | Pengehosan dan pengurusan model AI | $10-50/bulan |
| **OpenAI Deployment** | Model embedding teks (text-embedding-3-small) | $5-20/bulan |
| **Application Insights** | Pemantauan dan telemetri | $5-15/bulan |
| **Resource Group** | Pengorganisasian sumber | Percuma |

### 2. Lancarkan Sumber Azure

#### Pilihan A: Pelancaran Automatik (Disyorkan)

```bash
# Navigate to infrastructure directory
cd infra

# Windows - PowerShell
./deploy.ps1

# macOS/Linux - Bash
./deploy.sh
```

Skrip pelancaran akan:
1. Membuat kumpulan sumber unik
2. Melancarkan sumber Azure AI Foundry
3. Melancarkan model text-embedding-3-small
4. Konfigurasi Application Insights
5. Membuat service principal untuk pengesahan
6. Menjana fail `.env` dengan konfigurasi

#### Pilihan B: Pelancaran Manual

Jika anda lebih suka kawalan manual atau skrip automatik gagal:

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

### 3. Sahkan Pelancaran Azure

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

### 4. Konfigurasi Pembolehubah Persekitaran

Selepas pelancaran, anda sepatutnya mempunyai fail `.env`. Sahkan ia mengandungi:

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

## 🐳 Persediaan Persekitaran Docker

### 1. Fahami Komposisi Docker

Persekitaran pembangunan kita menggunakan Docker Compose:

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

### 2. Mulakan Persekitaran Pembangunan

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

### 3. Sahkan Persediaan Pangkalan Data

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

### 4. Uji Pelayan MCP

```bash
# Check MCP server health
curl http://localhost:8000/health

# Test basic MCP endpoint
curl -X POST http://localhost:8000/mcp \
  -H "Content-Type: application/json" \
  -H "x-rls-user-id: 00000000-0000-0000-0000-000000000000" \
  -d '{"method": "tools/list", "params": {}}'
```

## 🔧 Konfigurasi VS Code

### 1. Konfigurasi Integrasi MCP

Buat konfigurasi MCP VS Code:

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

### 2. Konfigurasi Persekitaran Python

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

### 3. Uji Integrasi VS Code

1. **Buka projek dalam VS Code**:
   ```bash
   code .
   ```

2. **Buka AI Chat**:
   - Tekan `Ctrl+Shift+P` (Windows/Linux) atau `Cmd+Shift+P` (macOS)
   - Taip "AI Chat" dan pilih "AI Chat: Open Chat"

3. **Uji Sambungan Pelayan MCP**:
   - Dalam AI Chat, taip `#zava` dan pilih salah satu pelayan yang dikonfigurasi
   - Tanya: "Apakah jadual yang tersedia dalam pangkalan data?"
   - Anda sepatutnya menerima respons yang menyenaraikan jadual pangkalan data runcit

## ✅ Pengesahan Persekitaran

### 1. Semakan Sistem Komprehensif

Jalankan skrip pengesahan ini untuk mengesahkan persediaan anda:

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

### 2. Senarai Semakan Pengesahan Manual

**✅ Alat Asas**
- [ ] Versi Docker 20.10+ dipasang dan berjalan
- [ ] Azure CLI 2.40+ dipasang dan disahkan
- [ ] Python 3.8+ dengan pip dipasang
- [ ] Git 2.30+ dipasang
- [ ] VS Code dengan sambungan yang diperlukan

**✅ Sumber Azure**
- [ ] Kumpulan sumber berjaya dibuat
- [ ] Projek AI Foundry dilancarkan
- [ ] Model text-embedding-3-small OpenAI dilancarkan
- [ ] Application Insights dikonfigurasi
- [ ] Service principal dibuat dengan kebenaran yang betul

**✅ Konfigurasi Persekitaran**
- [ ] Fail `.env` dibuat dengan semua pembolehubah yang diperlukan
- [ ] Kredensial Azure berfungsi (uji dengan `az account show`)
- [ ] Kontena PostgreSQL berjalan dan boleh diakses
- [ ] Data sampel dimuatkan dalam pangkalan data

**✅ Integrasi VS Code**
- [ ] `.vscode/mcp.json` dikonfigurasi
- [ ] Interpreter Python ditetapkan kepada persekitaran maya
- [ ] Pelayan MCP muncul dalam AI Chat
- [ ] Boleh melaksanakan pertanyaan ujian melalui AI Chat

## 🛠️ Menyelesaikan Masalah Biasa

### Masalah Docker

**Masalah**: Kontena Docker tidak dapat dimulakan
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

**Masalah**: Sambungan PostgreSQL gagal
```bash
# Check container logs
docker-compose logs postgres

# Verify container is healthy
docker-compose ps

# Test direct connection
docker-compose exec postgres psql -U postgres -d zava -c "SELECT 1;"
```

### Masalah Pelancaran Azure

**Masalah**: Pelancaran Azure gagal
```bash
# Check Azure CLI authentication
az account show

# Verify subscription permissions
az role assignment list --assignee $(az account show --query user.name -o tsv)

# Check resource provider registration
az provider register --namespace Microsoft.CognitiveServices
az provider register --namespace Microsoft.Insights
```

**Masalah**: Pengesahan perkhidmatan AI gagal
```bash
# Test service principal
az login --service-principal \
  --username $AZURE_CLIENT_ID \
  --password $AZURE_CLIENT_SECRET \
  --tenant $AZURE_TENANT_ID

# Verify AI service deployment
az cognitiveservices account list --query "[].{Name:name,Kind:kind,Location:location}"
```

### Masalah Persekitaran Python

**Masalah**: Pemasangan pakej gagal
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

**Masalah**: VS Code tidak dapat mencari interpreter Python
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

## 🎯 Poin Penting

Selepas melengkapkan makmal ini, anda sepatutnya mempunyai:

✅ **Persekitaran Pembangunan Lengkap**: Semua alat dipasang dan dikonfigurasi  
✅ **Sumber Azure Dilancarkan**: Perkhidmatan AI dan infrastruktur sokongan  
✅ **Persekitaran Docker Berjalan**: Kontena PostgreSQL dan pelayan MCP  
✅ **Integrasi VS Code**: Pelayan MCP dikonfigurasi dan boleh diakses  
✅ **Persediaan Disahkan**: Semua komponen diuji dan berfungsi bersama  
✅ **Pengetahuan Penyelesaian Masalah**: Isu biasa dan penyelesaian  

## 🚀 Langkah Seterusnya

Dengan persekitaran anda sedia, teruskan ke **[Lab 04: Reka Bentuk Pangkalan Data dan Skema](../04-Database/README.md)** untuk:

- Meneroka skema pangkalan data runcit secara terperinci
- Memahami pemodelan data multi-penyewa
- Belajar tentang pelaksanaan Keselamatan Tahap Baris
- Bekerja dengan data runcit sampel

## 📚 Sumber Tambahan

### Alat Pembangunan
- [Dokumentasi Docker](https://docs.docker.com/) - Rujukan lengkap Docker
- [Rujukan Azure CLI](https://docs.microsoft.com/cli/azure/) - Perintah Azure CLI
- [Dokumentasi VS Code](https://code.visualstudio.com/docs) - Konfigurasi editor dan sambungan

### Perkhidmatan Azure
- [Dokumentasi Azure AI Foundry](https://docs.microsoft.com/azure/ai-foundry/) - Konfigurasi perkhidmatan AI
- [Perkhidmatan Azure OpenAI](https://docs.microsoft.com/azure/cognitive-services/openai/) - Pelancaran model AI
- [Application Insights](https://docs.microsoft.com/azure/azure-monitor/app/app-insights-overview) - Persediaan pemantauan

### Pembangunan Python
- [Persekitaran Maya Python](https://docs.python.org/3/tutorial/venv.html) - Pengurusan persekitaran
- [Dokumentasi AsyncIO](https://docs.python.org/3/library/asyncio.html) - Corak pengaturcaraan async
- [Dokumentasi FastAPI](https://fastapi.tiangolo.com/) - Corak rangka kerja web

---

**Seterusnya**: Persekitaran sedia? Teruskan dengan [Lab 04: Reka Bentuk Pangkalan Data dan Skema](../04-Database/README.md)

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk memastikan ketepatan, sila ambil perhatian bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang berwibawa. Untuk maklumat yang kritikal, terjemahan manusia profesional adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.