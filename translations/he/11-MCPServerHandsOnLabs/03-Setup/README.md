# הגדרת סביבה

## 🎯 מה מכסה המעבדה הזו

מעבדה זו תדריך אותך צעד אחר צעד בהגדרת סביבה לפיתוח שרתי MCP עם אינטגרציה ל-PostgreSQL. תגדיר את הכלים הנדרשים, תפרוס משאבים ב-Azure ותוודא שההגדרה שלך פועלת כראוי לפני שתמשיך ליישום.

## סקירה כללית

סביבת פיתוח נכונה היא קריטית להצלחה בפיתוח שרתי MCP. מעבדה זו מספקת הוראות מפורטות להגדרת Docker, שירותי Azure, כלי פיתוח ואימות שכל הרכיבים עובדים יחד בצורה תקינה.

בסיום המעבדה, תהיה לך סביבה לפיתוח מלאה ומוכנה לבניית שרת MCP עבור Zava Retail.

## מטרות למידה

בסיום המעבדה, תוכל:

- **להתקין ולהגדיר** את כל כלי הפיתוח הנדרשים  
- **לפרוס משאבי Azure** הנדרשים לשרת MCP  
- **להגדיר קונטיינרים ב-Docker** עבור PostgreSQL ושרת MCP  
- **לאמת** את הגדרת הסביבה עם חיבורים בדיקה  
- **לפתור בעיות** נפוצות בהגדרה ובתצורה  
- **להבין** את זרימת העבודה והמבנה של הקבצים  

## 📋 בדיקת דרישות מוקדמות

לפני שתתחיל, ודא שיש לך:

### ידע נדרש
- שימוש בסיסי בשורת הפקודה (Windows Command Prompt/PowerShell)  
- הבנה של משתני סביבה  
- היכרות עם בקרת גרסאות Git  
- מושגים בסיסיים ב-Docker (קונטיינרים, תמונות, ווליום)  

### דרישות מערכת
- **מערכת הפעלה**: Windows 10/11, macOS או Linux  
- **RAM**: מינימום 8GB (מומלץ 16GB)  
- **אחסון**: לפחות 10GB פנויים  
- **רשת**: חיבור אינטרנט להורדות ולפריסת Azure  

### דרישות חשבון
- **מנוי Azure**: מספיק עם התוכנית החינמית  
- **חשבון GitHub**: לגישה למאגר  
- **חשבון Docker Hub**: (אופציונלי) לפרסום תמונות מותאמות אישית  

## 🛠️ התקנת כלים

### 1. התקנת Docker Desktop

Docker מספק את הסביבה המכולתית להגדרת הפיתוח שלנו.

#### התקנה ב-Windows

1. **הורד את Docker Desktop**:  
   ```cmd
   # Visit https://desktop.docker.com/win/stable/Docker%20Desktop%20Installer.exe
   # Or use Windows Package Manager
   winget install Docker.DockerDesktop
   ```
  
2. **התקן והגדר**:  
   - הפעל את ההתקנה כמנהל מערכת  
   - אפשר אינטגרציה עם WSL 2 כאשר תתבקש  
   - הפעל מחדש את המחשב לאחר סיום ההתקנה  

3. **אמת את ההתקנה**:  
   ```cmd
   docker --version
   docker-compose --version
   ```
  

#### התקנה ב-macOS

1. **הורד והתקן**:  
   ```bash
   # Download from https://desktop.docker.com/mac/stable/Docker.dmg
   # Or use Homebrew
   brew install --cask docker
   ```
  
2. **הפעל את Docker Desktop**:  
   - הפעל את Docker Desktop מתוך Applications  
   - השלם את אשף ההגדרה הראשוני  

3. **אמת את ההתקנה**:  
   ```bash
   docker --version
   docker-compose --version
   ```
  

#### התקנה ב-Linux

1. **התקן את Docker Engine**:  
   ```bash
   # Ubuntu/Debian
   curl -fsSL https://get.docker.com -o get-docker.sh
   sudo sh get-docker.sh
   sudo usermod -aG docker $USER
   
   # Log out and back in for group changes to take effect
   ```
  
2. **התקן את Docker Compose**:  
   ```bash
   sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
   sudo chmod +x /usr/local/bin/docker-compose
   ```
  

### 2. התקנת Azure CLI

Azure CLI מאפשר ניהול ופריסת משאבים ב-Azure.

#### התקנה ב-Windows

```cmd
# Using Windows Package Manager
winget install Microsoft.AzureCLI

# Or download MSI from: https://aka.ms/installazurecliwindows
```
  

#### התקנה ב-macOS

```bash
# Using Homebrew
brew install azure-cli

# Or using installer
curl -L https://aka.ms/InstallAzureCli | bash
```
  

#### התקנה ב-Linux

```bash
# Ubuntu/Debian
curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash

# RHEL/CentOS
sudo rpm --import https://packages.microsoft.com/keys/microsoft.asc
sudo dnf install azure-cli
```
  

#### אימות והתחברות

```bash
# Check installation
az version

# Login to Azure
az login

# Set default subscription (if you have multiple)
az account list --output table
az account set --subscription "Your-Subscription-Name"
```
  

### 3. התקנת Git

Git נדרש לשכפול המאגר ולבקרת גרסאות.

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
  

### 4. התקנת VS Code

Visual Studio Code מספק את סביבת הפיתוח המשולבת עם תמיכה ב-MCP.

#### התקנה

```cmd
# Windows
winget install Microsoft.VisualStudioCode

# macOS
brew install --cask visual-studio-code

# Linux (Ubuntu/Debian)
sudo snap install code --classic
```
  

#### הרחבות נדרשות

התקן את ההרחבות הבאות ב-VS Code:

```bash
# Install via command line
code --install-extension ms-python.python
code --install-extension ms-vscode.vscode-json
code --install-extension ms-azuretools.vscode-docker
code --install-extension ms-vscode.azure-account
```
  

או התקן דרך VS Code:  
1. פתח את VS Code  
2. עבור להרחבות (Ctrl+Shift+X)  
3. התקן:  
   - **Python** (Microsoft)  
   - **Docker** (Microsoft)  
   - **Azure Account** (Microsoft)  
   - **JSON** (Microsoft)  

### 5. התקנת Python

Python 3.8+ נדרש לפיתוח שרת MCP.

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
  

#### אימות התקנה

```bash
python --version  # Should show Python 3.11.x
pip --version      # Should show pip version
```
  

## 🚀 הגדרת פרויקט

### 1. שכפול המאגר

```bash
# Clone the main repository
git clone https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail.git

# Navigate to the project directory
cd MCP-Server-and-PostgreSQL-Sample-Retail

# Verify repository structure
ls -la
```
  

### 2. יצירת סביבה וירטואלית ב-Python

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
  

### 3. התקנת תלות ב-Python

```bash
# Install development dependencies
pip install -r requirements.lock.txt

# Verify key packages
pip list | grep fastmcp
pip list | grep asyncpg
pip list | grep azure
```
  

## ☁️ פריסת משאבי Azure

### 1. הבנת דרישות המשאבים

שרת MCP שלנו דורש את משאבי Azure הבאים:

| **משאב** | **מטרה** | **עלות משוערת** |  
|----------|----------|-----------------|  
| **Azure AI Foundry** | אירוח וניהול מודלים AI | $10-50 לחודש |  
| **OpenAI Deployment** | מודל הטמעת טקסט (text-embedding-3-small) | $5-20 לחודש |  
| **Application Insights** | ניטור וטלהמטריה | $5-15 לחודש |  
| **Resource Group** | ארגון משאבים | חינם |  

### 2. פריסת משאבי Azure

#### אפשרות A: פריסה אוטומטית (מומלץ)

```bash
# Navigate to infrastructure directory
cd infra

# Windows - PowerShell
./deploy.ps1

# macOS/Linux - Bash
./deploy.sh
```
  
הסקריפט יפרוס:  
1. קבוצת משאבים ייחודית  
2. משאבי Azure AI Foundry  
3. מודל text-embedding-3-small  
4. Application Insights  
5. יצירת Service Principal לאימות  
6. יצירת קובץ `.env` עם תצורה  

#### אפשרות B: פריסה ידנית

אם אתה מעדיף שליטה ידנית או שהסקריפט האוטומטי נכשל:

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
  

### 3. אימות פריסת Azure

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
  

### 4. הגדרת משתני סביבה

לאחר הפריסה, אמור להיות לך קובץ `.env`. ודא שהוא מכיל:

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
  

## 🐳 הגדרת סביבה ב-Docker

### 1. הבנת הרכב Docker

סביבת הפיתוח שלנו משתמשת ב-Docker Compose:

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
  

### 2. הפעלת סביבת הפיתוח

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
  

### 3. אימות הגדרת מסד הנתונים

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
  

### 4. בדיקת שרת MCP

```bash
# Check MCP server health
curl http://localhost:8000/health

# Test basic MCP endpoint
curl -X POST http://localhost:8000/mcp \
  -H "Content-Type: application/json" \
  -H "x-rls-user-id: 00000000-0000-0000-0000-000000000000" \
  -d '{"method": "tools/list", "params": {}}'
```
  

## 🔧 תצורת VS Code

### 1. הגדרת אינטגרציה עם MCP

צור תצורת MCP ב-VS Code:

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
  

### 2. הגדרת סביבה ב-Python

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
  

### 3. בדיקת אינטגרציה עם VS Code

1. **פתח את הפרויקט ב-VS Code**:  
   ```bash
   code .
   ```
  
2. **פתח AI Chat**:  
   - לחץ `Ctrl+Shift+P` (Windows/Linux) או `Cmd+Shift+P` (macOS)  
   - הקלד "AI Chat" ובחר "AI Chat: Open Chat"  

3. **בדוק חיבור לשרת MCP**:  
   - ב-AI Chat, הקלד `#zava` ובחר אחד מהשרתים שהוגדרו  
   - שאל: "אילו טבלאות זמינות במסד הנתונים?"  
   - אמור להתקבל מענה עם רשימת טבלאות מסד הנתונים הקמעונאי  

## ✅ אימות סביבה

### 1. בדיקת מערכת מקיפה

הרץ את סקריפט האימות הזה כדי לוודא את ההגדרה שלך:

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
  

### 2. רשימת בדיקה ידנית

**✅ כלים בסיסיים**  
- [ ] Docker גרסה 20.10+ מותקן ופועל  
- [ ] Azure CLI גרסה 2.40+ מותקן ומאומת  
- [ ] Python 3.8+ עם pip מותקן  
- [ ] Git גרסה 2.30+ מותקן  
- [ ] VS Code עם ההרחבות הנדרשות  

**✅ משאבי Azure**  
- [ ] קבוצת משאבים נוצרה בהצלחה  
- [ ] פרויקט AI Foundry נפרס  
- [ ] מודל OpenAI text-embedding-3-small נפרס  
- [ ] Application Insights הוגדר  
- [ ] Service Principal נוצר עם הרשאות מתאימות  

**✅ תצורת סביבה**  
- [ ] קובץ `.env` נוצר עם כל המשתנים הנדרשים  
- [ ] אישורי Azure עובדים (בדוק עם `az account show`)  
- [ ] קונטיינר PostgreSQL פועל ונגיש  
- [ ] נתוני דוגמה נטענו למסד הנתונים  

**✅ אינטגרציה עם VS Code**  
- [ ] קובץ `.vscode/mcp.json` הוגדר  
- [ ] פרשן Python מוגדר לסביבה הווירטואלית  
- [ ] שרתי MCP מופיעים ב-AI Chat  
- [ ] ניתן לבצע שאילתות בדיקה דרך AI Chat  

## 🛠️ פתרון בעיות נפוצות

### בעיות ב-Docker

**בעיה**: קונטיינרים ב-Docker לא מתחילים  
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
  
**בעיה**: חיבור ל-PostgreSQL נכשל  
```bash
# Check container logs
docker-compose logs postgres

# Verify container is healthy
docker-compose ps

# Test direct connection
docker-compose exec postgres psql -U postgres -d zava -c "SELECT 1;"
```
  

### בעיות בפריסת Azure

**בעיה**: פריסת Azure נכשלת  
```bash
# Check Azure CLI authentication
az account show

# Verify subscription permissions
az role assignment list --assignee $(az account show --query user.name -o tsv)

# Check resource provider registration
az provider register --namespace Microsoft.CognitiveServices
az provider register --namespace Microsoft.Insights
```
  
**בעיה**: אימות שירות AI נכשל  
```bash
# Test service principal
az login --service-principal \
  --username $AZURE_CLIENT_ID \
  --password $AZURE_CLIENT_SECRET \
  --tenant $AZURE_TENANT_ID

# Verify AI service deployment
az cognitiveservices account list --query "[].{Name:name,Kind:kind,Location:location}"
```
  

### בעיות בסביבת Python

**בעיה**: התקנת חבילות נכשלת  
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
  
**בעיה**: VS Code לא מוצא את פרשן Python  
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
  

## 🎯 נקודות עיקריות

לאחר השלמת המעבדה, אמור להיות לך:

✅ **סביבת פיתוח מלאה**: כל הכלים מותקנים ומוגדרים  
✅ **משאבי Azure נפרסו**: שירותי AI ותשתית תומכת  
✅ **סביבת Docker פועלת**: קונטיינרים של PostgreSQL ושרת MCP  
✅ **אינטגרציה עם VS Code**: שרתי MCP מוגדרים ונגישים  
✅ **הגדרה מאומתת**: כל הרכיבים נבדקו ועובדים יחד  
✅ **ידע בפתרון בעיות**: בעיות נפוצות ופתרונות  

## 🚀 מה הלאה

עם הסביבה מוכנה, המשך ל-**[מעבדה 04: עיצוב מסד נתונים וסכימה](../04-Database/README.md)** כדי:

- לחקור את סכימת מסד הנתונים הקמעונאי בפירוט  
- להבין מודלים נתונים מרובי דיירים  
- ללמוד על יישום אבטחת רמות שורה  
- לעבוד עם נתוני קמעונאות לדוגמה  

## 📚 משאבים נוספים

### כלי פיתוח
- [תיעוד Docker](https://docs.docker.com/) - מדריך מלא ל-Docker  
- [תיעוד Azure CLI](https://docs.microsoft.com/cli/azure/) - פקודות Azure CLI  
- [תיעוד VS Code](https://code.visualstudio.com/docs) - הגדרות והרחבות עורך  

### שירותי Azure
- [תיעוד Azure AI Foundry](https://docs.microsoft.com/azure/ai-foundry/) - הגדרת שירותי AI  
- [שירות Azure OpenAI](https://docs.microsoft.com/azure/cognitive-services/openai/) - פריסת מודלים AI  
- [Application Insights](https://docs.microsoft.com/azure/azure-monitor/app/app-insights-overview) - הגדרת ניטור  

### פיתוח ב-Python
- [סביבות וירטואליות ב-Python](https://docs.python.org/3/tutorial/venv.html) - ניהול סביבות  
- [תיעוד AsyncIO](https://docs.python.org/3/library/asyncio.html) - דפוסי תכנות אסינכרוניים  
- [תיעוד FastAPI](https://fastapi.tiangolo.com/) - דפוסי פיתוח מסגרת  

---

**הבא**: הסביבה מוכנה? המשך ל-[מעבדה 04: עיצוב מסד נתונים וסכימה](../04-Database/README.md)

---

**כתב ויתור**:  
מסמך זה תורגם באמצעות שירות תרגום מבוסס בינה מלאכותית [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון שתרגומים אוטומטיים עשויים להכיל שגיאות או אי דיוקים. המסמך המקורי בשפתו המקורית צריך להיחשב כמקור סמכותי. עבור מידע קריטי, מומלץ להשתמש בתרגום מקצועי על ידי אדם. איננו נושאים באחריות לאי הבנות או לפרשנויות שגויות הנובעות משימוש בתרגום זה.