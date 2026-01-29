# Ortam Kurulumu

## 🎯 Bu Laboratuvar Neleri Kapsıyor?

Bu uygulamalı laboratuvar, PostgreSQL entegrasyonu ile MCP sunucuları geliştirmek için eksiksiz bir geliştirme ortamı kurmanıza rehberlik eder. Gerekli tüm araçları yapılandıracak, Azure kaynaklarını dağıtacak ve uygulamaya geçmeden önce kurulumunuzu doğrulayacaksınız.

## Genel Bakış

Başarılı MCP sunucu geliştirme için uygun bir geliştirme ortamı çok önemlidir. Bu laboratuvar, Docker, Azure hizmetleri, geliştirme araçları kurulumunu ve bunların birlikte doğru şekilde çalıştığını doğrulamak için adım adım talimatlar sağlar.

Bu laboratuvarın sonunda, Zava Retail MCP sunucusunu geliştirmek için tamamen işlevsel bir geliştirme ortamına sahip olacaksınız.

## Öğrenme Hedefleri

Bu laboratuvarın sonunda şunları yapabileceksiniz:

- **Gerekli geliştirme araçlarını** yükleyip yapılandırmak  
- MCP sunucusu için gerekli **Azure kaynaklarını dağıtmak**  
- PostgreSQL ve MCP sunucusu için **Docker konteynerlerini kurmak**  
- Ortam kurulumunuzu **test bağlantılarıyla doğrulamak**  
- Yaygın kurulum sorunlarını ve yapılandırma problemlerini **çözmek**  
- Geliştirme iş akışını ve dosya yapısını **anlamak**  

## 📋 Ön Koşul Kontrolü

Başlamadan önce şunlara sahip olduğunuzdan emin olun:

### Gerekli Bilgi
- Temel komut satırı kullanımı (Windows Komut İstemi/PowerShell)  
- Ortam değişkenlerini anlama  
- Git sürüm kontrolüne aşinalık  
- Temel Docker kavramları (konteynerler, imajlar, hacimler)  

### Sistem Gereksinimleri
- **İşletim Sistemi**: Windows 10/11, macOS veya Linux  
- **RAM**: Minimum 8GB (16GB önerilir)  
- **Depolama**: En az 10GB boş alan  
- **Ağ**: İndirme ve Azure dağıtımı için internet bağlantısı  

### Hesap Gereksinimleri
- **Azure Aboneliği**: Ücretsiz katman yeterlidir  
- **GitHub Hesabı**: Depoya erişim için  
- **Docker Hub Hesabı**: (Opsiyonel) Özel imaj yayınlama için  

## 🛠️ Araç Kurulumu

### 1. Docker Desktop Kurulumu

Docker, geliştirme kurulumumuz için konteynerize edilmiş ortam sağlar.

#### Windows Kurulumu

1. **Docker Desktop'u İndirin**:  
   ```cmd
   # Visit https://desktop.docker.com/win/stable/Docker%20Desktop%20Installer.exe
   # Or use Windows Package Manager
   winget install Docker.DockerDesktop
   ```
  
2. **Kurulum ve Yapılandırma**:  
   - Yükleyiciyi Yönetici olarak çalıştırın  
   - İstendiğinde WSL 2 entegrasyonunu etkinleştirin  
   - Kurulum tamamlandığında bilgisayarınızı yeniden başlatın  

3. **Kurulumu Doğrulayın**:  
   ```cmd
   docker --version
   docker-compose --version
   ```
  

#### macOS Kurulumu

1. **İndirin ve Kurun**:  
   ```bash
   # Download from https://desktop.docker.com/mac/stable/Docker.dmg
   # Or use Homebrew
   brew install --cask docker
   ```
  
2. **Docker Desktop'u Başlatın**:  
   - Uygulamalar'dan Docker Desktop'u başlatın  
   - İlk kurulum sihirbazını tamamlayın  

3. **Kurulumu Doğrulayın**:  
   ```bash
   docker --version
   docker-compose --version
   ```
  

#### Linux Kurulumu

1. **Docker Engine'i Kurun**:  
   ```bash
   # Ubuntu/Debian
   curl -fsSL https://get.docker.com -o get-docker.sh
   sudo sh get-docker.sh
   sudo usermod -aG docker $USER
   
   # Log out and back in for group changes to take effect
   ```
  
2. **Docker Compose'u Kurun**:  
   ```bash
   sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
   sudo chmod +x /usr/local/bin/docker-compose
   ```
  

### 2. Azure CLI Kurulumu

Azure CLI, Azure kaynaklarının dağıtımı ve yönetimini sağlar.

#### Windows Kurulumu

```cmd
# Using Windows Package Manager
winget install Microsoft.AzureCLI

# Or download MSI from: https://aka.ms/installazurecliwindows
```
  

#### macOS Kurulumu

```bash
# Using Homebrew
brew install azure-cli

# Or using installer
curl -L https://aka.ms/InstallAzureCli | bash
```
  

#### Linux Kurulumu

```bash
# Ubuntu/Debian
curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash

# RHEL/CentOS
sudo rpm --import https://packages.microsoft.com/keys/microsoft.asc
sudo dnf install azure-cli
```
  

#### Doğrulama ve Kimlik Doğrulama

```bash
# Check installation
az version

# Login to Azure
az login

# Set default subscription (if you have multiple)
az account list --output table
az account set --subscription "Your-Subscription-Name"
```
  

### 3. Git Kurulumu

Git, depoyu klonlamak ve sürüm kontrolü için gereklidir.

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
  

### 4. VS Code Kurulumu

Visual Studio Code, MCP desteği ile entegre geliştirme ortamı sağlar.

#### Kurulum

```cmd
# Windows
winget install Microsoft.VisualStudioCode

# macOS
brew install --cask visual-studio-code

# Linux (Ubuntu/Debian)
sudo snap install code --classic
```
  

#### Gerekli Uzantılar

Bu VS Code uzantılarını yükleyin:

```bash
# Install via command line
code --install-extension ms-python.python
code --install-extension ms-vscode.vscode-json
code --install-extension ms-azuretools.vscode-docker
code --install-extension ms-vscode.azure-account
```
  
VS Code üzerinden yüklemek için:  
1. VS Code'u açın  
2. Uzantılar bölümüne gidin (Ctrl+Shift+X)  
3. Şunları yükleyin:  
   - **Python** (Microsoft)  
   - **Docker** (Microsoft)  
   - **Azure Account** (Microsoft)  
   - **JSON** (Microsoft)  

### 5. Python Kurulumu

MCP sunucu geliştirme için Python 3.8+ gereklidir.

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
  

#### Kurulumu Doğrulayın

```bash
python --version  # Should show Python 3.11.x
pip --version      # Should show pip version
```
  

## 🚀 Proje Kurulumu

### 1. Depoyu Klonlayın

```bash
# Clone the main repository
git clone https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail.git

# Navigate to the project directory
cd MCP-Server-and-PostgreSQL-Sample-Retail

# Verify repository structure
ls -la
```
  

### 2. Python Sanal Ortamı Oluşturun

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
  

### 3. Python Bağımlılıklarını Yükleyin

```bash
# Install development dependencies
pip install -r requirements.lock.txt

# Verify key packages
pip list | grep fastmcp
pip list | grep asyncpg
pip list | grep azure
```
  

## ☁️ Azure Kaynak Dağıtımı

### 1. Kaynak Gereksinimlerini Anlama

MCP sunucumuz şu Azure kaynaklarını gerektirir:

| **Kaynak**              | **Amacı**                          | **Tahmini Maliyet**       |  
|--------------------------|-------------------------------------|---------------------------|  
| **Azure AI Foundry**     | AI modeli barındırma ve yönetimi    | $10-50/ay                |  
| **OpenAI Dağıtımı**      | Metin gömme modeli (text-embedding-3-small) | $5-20/ay |  
| **Application Insights** | İzleme ve telemetri                | $5-15/ay                 |  
| **Resource Group**       | Kaynak organizasyonu               | Ücretsiz                 |  

### 2. Azure Kaynaklarını Dağıtın

#### Seçenek A: Otomatik Dağıtım (Önerilir)

```bash
# Navigate to infrastructure directory
cd infra

# Windows - PowerShell
./deploy.ps1

# macOS/Linux - Bash
./deploy.sh
```
  
Dağıtım betiği şunları yapacaktır:  
1. Benzersiz bir kaynak grubu oluşturur  
2. Azure AI Foundry kaynaklarını dağıtır  
3. Text-embedding-3-small modelini dağıtır  
4. Application Insights'ı yapılandırır  
5. Kimlik doğrulama için bir hizmet ilkesi oluşturur  
6. Yapılandırma ile `.env` dosyası oluşturur  

#### Seçenek B: Manuel Dağıtım

Otomatik betik başarısız olursa veya manuel kontrol tercih ederseniz:  

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
  

### 3. Azure Dağıtımını Doğrulayın

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
  

### 4. Ortam Değişkenlerini Yapılandırın

Dağıtımdan sonra bir `.env` dosyasına sahip olmalısınız. Şunları içerdiğinden emin olun:  

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
  

## 🐳 Docker Ortam Kurulumu

### 1. Docker Kompozisyonunu Anlama

Geliştirme ortamımız Docker Compose kullanır:  

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
  

### 2. Geliştirme Ortamını Başlatın

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
  

### 3. Veritabanı Kurulumunu Doğrulayın

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
  

### 4. MCP Sunucusunu Test Edin

```bash
# Check MCP server health
curl http://localhost:8000/health

# Test basic MCP endpoint
curl -X POST http://localhost:8000/mcp \
  -H "Content-Type: application/json" \
  -H "x-rls-user-id: 00000000-0000-0000-0000-000000000000" \
  -d '{"method": "tools/list", "params": {}}'
```
  

## 🔧 VS Code Yapılandırması

### 1. MCP Entegrasyonunu Yapılandırın

VS Code MCP yapılandırması oluşturun:  

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
  

### 2. Python Ortamını Yapılandırın

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
  

### 3. VS Code Entegrasyonunu Test Edin

1. **Projeyi VS Code'da açın**:  
   ```bash
   code .
   ```
  
2. **AI Sohbetini Açın**:  
   - `Ctrl+Shift+P` (Windows/Linux) veya `Cmd+Shift+P` (macOS) tuşlarına basın  
   - "AI Chat" yazın ve "AI Chat: Open Chat" seçeneğini seçin  

3. **MCP Sunucu Bağlantısını Test Edin**:  
   - AI Sohbetinde `#zava` yazın ve yapılandırılmış sunuculardan birini seçin  
   - Şunu sorun: "Veritabanında hangi tablolar mevcut?"  
   - Perakende veritabanı tablolarını listeleyen bir yanıt almalısınız  

## ✅ Ortam Doğrulama

### 1. Kapsamlı Sistem Kontrolü

Kurulumunuzu doğrulamak için bu doğrulama betiğini çalıştırın:  

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
  

### 2. Manuel Doğrulama Kontrol Listesi

**✅ Temel Araçlar**  
- [ ] Docker 20.10+ sürümü yüklü ve çalışıyor  
- [ ] Azure CLI 2.40+ yüklü ve kimlik doğrulandı  
- [ ] Python 3.8+ ve pip yüklü  
- [ ] Git 2.30+ yüklü  
- [ ] Gerekli uzantılarla VS Code yüklü  

**✅ Azure Kaynakları**  
- [ ] Kaynak grubu başarıyla oluşturuldu  
- [ ] AI Foundry projesi dağıtıldı  
- [ ] OpenAI text-embedding-3-small modeli dağıtıldı  
- [ ] Application Insights yapılandırıldı  
- [ ] Uygun izinlere sahip hizmet ilkesi oluşturuldu  

**✅ Ortam Yapılandırması**  
- [ ] `.env` dosyası gerekli tüm değişkenlerle oluşturuldu  
- [ ] Azure kimlik bilgileri çalışıyor (`az account show` ile test edin)  
- [ ] PostgreSQL konteyneri çalışıyor ve erişilebilir  
- [ ] Veritabanına örnek veri yüklendi  

**✅ VS Code Entegrasyonu**  
- [ ] `.vscode/mcp.json` yapılandırıldı  
- [ ] Python yorumlayıcı sanal ortama ayarlandı  
- [ ] MCP sunucuları AI Sohbetinde görünüyor  
- [ ] AI Sohbet üzerinden test sorguları çalıştırılabiliyor  

## 🛠️ Yaygın Sorunları Giderme

### Docker Sorunları

**Sorun**: Docker konteynerleri başlamıyor  
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
  
**Sorun**: PostgreSQL bağlantısı başarısız  
```bash
# Check container logs
docker-compose logs postgres

# Verify container is healthy
docker-compose ps

# Test direct connection
docker-compose exec postgres psql -U postgres -d zava -c "SELECT 1;"
```
  

### Azure Dağıtım Sorunları

**Sorun**: Azure dağıtımı başarısız  
```bash
# Check Azure CLI authentication
az account show

# Verify subscription permissions
az role assignment list --assignee $(az account show --query user.name -o tsv)

# Check resource provider registration
az provider register --namespace Microsoft.CognitiveServices
az provider register --namespace Microsoft.Insights
```
  
**Sorun**: AI hizmeti kimlik doğrulaması başarısız  
```bash
# Test service principal
az login --service-principal \
  --username $AZURE_CLIENT_ID \
  --password $AZURE_CLIENT_SECRET \
  --tenant $AZURE_TENANT_ID

# Verify AI service deployment
az cognitiveservices account list --query "[].{Name:name,Kind:kind,Location:location}"
```
  

### Python Ortam Sorunları

**Sorun**: Paket yükleme başarısız  
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
  
**Sorun**: VS Code Python yorumlayıcısını bulamıyor  
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
  

## 🎯 Önemli Çıkarımlar

Bu laboratuvarı tamamladıktan sonra şunlara sahip olmalısınız:

✅ **Tam Geliştirme Ortamı**: Tüm araçlar yüklendi ve yapılandırıldı  
✅ **Azure Kaynakları Dağıtıldı**: AI hizmetleri ve destek altyapısı  
✅ **Docker Ortamı Çalışıyor**: PostgreSQL ve MCP sunucu konteynerleri  
✅ **VS Code Entegrasyonu**: MCP sunucuları yapılandırıldı ve erişilebilir  
✅ **Doğrulanmış Kurulum**: Tüm bileşenler test edildi ve birlikte çalışıyor  
✅ **Sorun Giderme Bilgisi**: Yaygın sorunlar ve çözümleri  

## 🚀 Sıradaki Adımlar

Ortamınız hazır olduğunda, **[Lab 04: Veritabanı Tasarımı ve Şeması](../04-Database/README.md)** ile devam edin:

- Perakende veritabanı şemasını ayrıntılı olarak keşfedin  
- Çok kiracılı veri modellemeyi anlayın  
- Satır Düzeyi Güvenlik uygulamasını öğrenin  
- Örnek perakende verileriyle çalışın  

## 📚 Ek Kaynaklar

### Geliştirme Araçları
- [Docker Belgeleri](https://docs.docker.com/) - Docker hakkında tam referans  
- [Azure CLI Referansı](https://docs.microsoft.com/cli/azure/) - Azure CLI komutları  
- [VS Code Belgeleri](https://code.visualstudio.com/docs) - Editör yapılandırması ve uzantılar  

### Azure Hizmetleri
- [Azure AI Foundry Belgeleri](https://docs.microsoft.com/azure/ai-foundry/) - AI hizmeti yapılandırması  
- [Azure OpenAI Hizmeti](https://docs.microsoft.com/azure/cognitive-services/openai/) - AI modeli dağıtımı  
- [Application Insights](https://docs.microsoft.com/azure/azure-monitor/app/app-insights-overview) - İzleme kurulumu  

### Python Geliştirme
- [Python Sanal Ortamlar](https://docs.python.org/3/tutorial/venv.html) - Ortam yönetimi  
- [AsyncIO Belgeleri](https://docs.python.org/3/library/asyncio.html) - Asenkron programlama desenleri  
- [FastAPI Belgeleri](https://fastapi.tiangolo.com/) - Web çerçevesi desenleri  

---

**Sonraki**: Ortam hazır mı? **[Lab 04: Veritabanı Tasarımı ve Şeması](../04-Database/README.md)** ile devam edin.

---

**Feragatname**:  
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hata veya yanlışlıklar içerebileceğini lütfen unutmayın. Belgenin orijinal dili, yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımından kaynaklanan yanlış anlamalar veya yanlış yorumlamalar için sorumluluk kabul etmiyoruz.