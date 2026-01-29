# Configuración del Entorno

## 🎯 Qué Cubre Este Laboratorio

Este laboratorio práctico te guía en la configuración de un entorno de desarrollo completo para construir servidores MCP con integración de PostgreSQL. Configurarás todas las herramientas necesarias, desplegarás recursos en Azure y validarás tu configuración antes de proceder con la implementación.

## Descripción General

Un entorno de desarrollo adecuado es crucial para el desarrollo exitoso de servidores MCP. Este laboratorio proporciona instrucciones paso a paso para configurar Docker, servicios de Azure, herramientas de desarrollo y validar que todo funcione correctamente en conjunto.

Al final de este laboratorio, tendrás un entorno de desarrollo completamente funcional listo para construir el servidor MCP de Zava Retail.

## Objetivos de Aprendizaje

Al finalizar este laboratorio, serás capaz de:

- **Instalar y configurar** todas las herramientas de desarrollo necesarias
- **Desplegar recursos en Azure** requeridos para el servidor MCP
- **Configurar contenedores Docker** para PostgreSQL y el servidor MCP
- **Validar** tu configuración de entorno con conexiones de prueba
- **Solucionar problemas** comunes de configuración y errores
- **Comprender** el flujo de trabajo de desarrollo y la estructura de archivos

## 📋 Verificación de Requisitos Previos

Antes de comenzar, asegúrate de tener:

### Conocimientos Requeridos
- Uso básico de la línea de comandos (Windows Command Prompt/PowerShell)
- Comprensión de las variables de entorno
- Familiaridad con el control de versiones Git
- Conceptos básicos de Docker (contenedores, imágenes, volúmenes)

### Requisitos del Sistema
- **Sistema Operativo**: Windows 10/11, macOS o Linux
- **RAM**: Mínimo 8GB (16GB recomendado)
- **Almacenamiento**: Al menos 10GB de espacio libre
- **Red**: Conexión a Internet para descargas y despliegue en Azure

### Requisitos de Cuenta
- **Suscripción de Azure**: El nivel gratuito es suficiente
- **Cuenta de GitHub**: Para acceso al repositorio
- **Cuenta de Docker Hub**: (Opcional) Para publicar imágenes personalizadas

## 🛠️ Instalación de Herramientas

### 1. Instalar Docker Desktop

Docker proporciona el entorno de contenedores para nuestra configuración de desarrollo.

#### Instalación en Windows

1. **Descargar Docker Desktop**:
   ```cmd
   # Visit https://desktop.docker.com/win/stable/Docker%20Desktop%20Installer.exe
   # Or use Windows Package Manager
   winget install Docker.DockerDesktop
   ```

2. **Instalar y Configurar**:
   - Ejecuta el instalador como Administrador
   - Habilita la integración con WSL 2 cuando se te solicite
   - Reinicia tu computadora al completar la instalación

3. **Verificar Instalación**:
   ```cmd
   docker --version
   docker-compose --version
   ```

#### Instalación en macOS

1. **Descargar e Instalar**:
   ```bash
   # Download from https://desktop.docker.com/mac/stable/Docker.dmg
   # Or use Homebrew
   brew install --cask docker
   ```

2. **Iniciar Docker Desktop**:
   - Abre Docker Desktop desde Aplicaciones
   - Completa el asistente de configuración inicial

3. **Verificar Instalación**:
   ```bash
   docker --version
   docker-compose --version
   ```

#### Instalación en Linux

1. **Instalar Docker Engine**:
   ```bash
   # Ubuntu/Debian
   curl -fsSL https://get.docker.com -o get-docker.sh
   sudo sh get-docker.sh
   sudo usermod -aG docker $USER
   
   # Log out and back in for group changes to take effect
   ```

2. **Instalar Docker Compose**:
   ```bash
   sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
   sudo chmod +x /usr/local/bin/docker-compose
   ```

### 2. Instalar Azure CLI

Azure CLI permite el despliegue y la gestión de recursos en Azure.

#### Instalación en Windows

```cmd
# Using Windows Package Manager
winget install Microsoft.AzureCLI

# Or download MSI from: https://aka.ms/installazurecliwindows
```

#### Instalación en macOS

```bash
# Using Homebrew
brew install azure-cli

# Or using installer
curl -L https://aka.ms/InstallAzureCli | bash
```

#### Instalación en Linux

```bash
# Ubuntu/Debian
curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash

# RHEL/CentOS
sudo rpm --import https://packages.microsoft.com/keys/microsoft.asc
sudo dnf install azure-cli
```

#### Verificar y Autenticar

```bash
# Check installation
az version

# Login to Azure
az login

# Set default subscription (if you have multiple)
az account list --output table
az account set --subscription "Your-Subscription-Name"
```

### 3. Instalar Git

Git es necesario para clonar el repositorio y el control de versiones.

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

### 4. Instalar VS Code

Visual Studio Code proporciona el entorno de desarrollo integrado con soporte para MCP.

#### Instalación

```cmd
# Windows
winget install Microsoft.VisualStudioCode

# macOS
brew install --cask visual-studio-code

# Linux (Ubuntu/Debian)
sudo snap install code --classic
```

#### Extensiones Requeridas

Instala estas extensiones de VS Code:

```bash
# Install via command line
code --install-extension ms-python.python
code --install-extension ms-vscode.vscode-json
code --install-extension ms-azuretools.vscode-docker
code --install-extension ms-vscode.azure-account
```

O instálalas desde VS Code:
1. Abre VS Code
2. Ve a Extensiones (Ctrl+Shift+X)
3. Instala:
   - **Python** (Microsoft)
   - **Docker** (Microsoft)
   - **Azure Account** (Microsoft)
   - **JSON** (Microsoft)

### 5. Instalar Python

Python 3.8+ es requerido para el desarrollo del servidor MCP.

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

#### Verificar Instalación

```bash
python --version  # Should show Python 3.11.x
pip --version      # Should show pip version
```

## 🚀 Configuración del Proyecto

### 1. Clonar el Repositorio

```bash
# Clone the main repository
git clone https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail.git

# Navigate to the project directory
cd MCP-Server-and-PostgreSQL-Sample-Retail

# Verify repository structure
ls -la
```

### 2. Crear un Entorno Virtual de Python

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

### 3. Instalar Dependencias de Python

```bash
# Install development dependencies
pip install -r requirements.lock.txt

# Verify key packages
pip list | grep fastmcp
pip list | grep asyncpg
pip list | grep azure
```

## ☁️ Despliegue de Recursos en Azure

### 1. Comprender los Requisitos de Recursos

Nuestro servidor MCP requiere estos recursos de Azure:

| **Recurso** | **Propósito** | **Costo Estimado** |
|-------------|--------------|--------------------|
| **Azure AI Foundry** | Hospedaje y gestión de modelos de IA | $10-50/mes |
| **Despliegue de OpenAI** | Modelo de incrustación de texto (text-embedding-3-small) | $5-20/mes |
| **Application Insights** | Monitoreo y telemetría | $5-15/mes |
| **Grupo de Recursos** | Organización de recursos | Gratis |

### 2. Desplegar Recursos en Azure

#### Opción A: Despliegue Automático (Recomendado)

```bash
# Navigate to infrastructure directory
cd infra

# Windows - PowerShell
./deploy.ps1

# macOS/Linux - Bash
./deploy.sh
```

El script de despliegue realizará:
1. Crear un grupo de recursos único
2. Desplegar recursos de Azure AI Foundry
3. Desplegar el modelo text-embedding-3-small
4. Configurar Application Insights
5. Crear un principal de servicio para autenticación
6. Generar un archivo `.env` con la configuración

#### Opción B: Despliegue Manual

Si prefieres control manual o el script automático falla:

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

### 3. Verificar Despliegue en Azure

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

### 4. Configurar Variables de Entorno

Después del despliegue, deberías tener un archivo `.env`. Verifica que contenga:

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

## 🐳 Configuración del Entorno Docker

### 1. Comprender la Composición de Docker

Nuestro entorno de desarrollo utiliza Docker Compose:

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

### 2. Iniciar el Entorno de Desarrollo

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

### 3. Verificar Configuración de la Base de Datos

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

### 4. Probar el Servidor MCP

```bash
# Check MCP server health
curl http://localhost:8000/health

# Test basic MCP endpoint
curl -X POST http://localhost:8000/mcp \
  -H "Content-Type: application/json" \
  -H "x-rls-user-id: 00000000-0000-0000-0000-000000000000" \
  -d '{"method": "tools/list", "params": {}}'
```

## 🔧 Configuración de VS Code

### 1. Configurar la Integración MCP

Crea la configuración MCP en VS Code:

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

### 2. Configurar el Entorno de Python

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

### 3. Probar la Integración con VS Code

1. **Abre el proyecto en VS Code**:
   ```bash
   code .
   ```

2. **Abrir AI Chat**:
   - Presiona `Ctrl+Shift+P` (Windows/Linux) o `Cmd+Shift+P` (macOS)
   - Escribe "AI Chat" y selecciona "AI Chat: Open Chat"

3. **Probar Conexión al Servidor MCP**:
   - En AI Chat, escribe `#zava` y selecciona uno de los servidores configurados
   - Pregunta: "¿Qué tablas están disponibles en la base de datos?"
   - Deberías recibir una respuesta con las tablas de la base de datos de retail

## ✅ Validación del Entorno

### 1. Verificación Completa del Sistema

Ejecuta este script de validación para verificar tu configuración:

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

### 2. Lista de Verificación Manual

**✅ Herramientas Básicas**
- [ ] Docker versión 20.10+ instalado y funcionando
- [ ] Azure CLI 2.40+ instalado y autenticado
- [ ] Python 3.8+ con pip instalado
- [ ] Git 2.30+ instalado
- [ ] VS Code con extensiones requeridas

**✅ Recursos de Azure**
- [ ] Grupo de recursos creado exitosamente
- [ ] Proyecto de AI Foundry desplegado
- [ ] Modelo text-embedding-3-small de OpenAI desplegado
- [ ] Application Insights configurado
- [ ] Principal de servicio creado con permisos adecuados

**✅ Configuración del Entorno**
- [ ] Archivo `.env` creado con todas las variables requeridas
- [ ] Credenciales de Azure funcionando (prueba con `az account show`)
- [ ] Contenedor de PostgreSQL ejecutándose y accesible
- [ ] Datos de muestra cargados en la base de datos

**✅ Integración con VS Code**
- [ ] `.vscode/mcp.json` configurado
- [ ] Intérprete de Python configurado al entorno virtual
- [ ] Servidores MCP aparecen en AI Chat
- [ ] Se pueden ejecutar consultas de prueba a través de AI Chat

## 🛠️ Solución de Problemas Comunes

### Problemas con Docker

**Problema**: Los contenedores de Docker no inician
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

**Problema**: Falla la conexión a PostgreSQL
```bash
# Check container logs
docker-compose logs postgres

# Verify container is healthy
docker-compose ps

# Test direct connection
docker-compose exec postgres psql -U postgres -d zava -c "SELECT 1;"
```

### Problemas de Despliegue en Azure

**Problema**: Falla el despliegue en Azure
```bash
# Check Azure CLI authentication
az account show

# Verify subscription permissions
az role assignment list --assignee $(az account show --query user.name -o tsv)

# Check resource provider registration
az provider register --namespace Microsoft.CognitiveServices
az provider register --namespace Microsoft.Insights
```

**Problema**: Falla la autenticación del servicio de IA
```bash
# Test service principal
az login --service-principal \
  --username $AZURE_CLIENT_ID \
  --password $AZURE_CLIENT_SECRET \
  --tenant $AZURE_TENANT_ID

# Verify AI service deployment
az cognitiveservices account list --query "[].{Name:name,Kind:kind,Location:location}"
```

### Problemas con el Entorno de Python

**Problema**: Falla la instalación de paquetes
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

**Problema**: VS Code no encuentra el intérprete de Python
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

## 🎯 Puntos Clave

Después de completar este laboratorio, deberías tener:

✅ **Entorno de Desarrollo Completo**: Todas las herramientas instaladas y configuradas  
✅ **Recursos de Azure Desplegados**: Servicios de IA e infraestructura de soporte  
✅ **Entorno Docker Ejecutándose**: Contenedores de PostgreSQL y servidor MCP  
✅ **Integración con VS Code**: Servidores MCP configurados y accesibles  
✅ **Configuración Validada**: Todos los componentes probados y funcionando juntos  
✅ **Conocimientos de Solución de Problemas**: Problemas comunes y soluciones  

## 🚀 Próximos Pasos

Con tu entorno listo, continúa con **[Laboratorio 04: Diseño y Esquema de Base de Datos](../04-Database/README.md)** para:

- Explorar el esquema de la base de datos de retail en detalle
- Comprender el modelado de datos multi-tenant
- Aprender sobre la implementación de Seguridad a Nivel de Fila
- Trabajar con datos de muestra de retail

## 📚 Recursos Adicionales

### Herramientas de Desarrollo
- [Documentación de Docker](https://docs.docker.com/) - Referencia completa de Docker
- [Referencia de Azure CLI](https://docs.microsoft.com/cli/azure/) - Comandos de Azure CLI
- [Documentación de VS Code](https://code.visualstudio.com/docs) - Configuración del editor y extensiones

### Servicios de Azure
- [Documentación de Azure AI Foundry](https://docs.microsoft.com/azure/ai-foundry/) - Configuración de servicios de IA
- [Servicio OpenAI de Azure](https://docs.microsoft.com/azure/cognitive-services/openai/) - Despliegue de modelos de IA
- [Application Insights](https://docs.microsoft.com/azure/azure-monitor/app/app-insights-overview) - Configuración de monitoreo

### Desarrollo en Python
- [Entornos Virtuales en Python](https://docs.python.org/3/tutorial/venv.html) - Gestión de entornos
- [Documentación de AsyncIO](https://docs.python.org/3/library/asyncio.html) - Patrones de programación asíncrona
- [Documentación de FastAPI](https://fastapi.tiangolo.com/) - Patrones de frameworks web

---

**Siguiente**: ¿Entorno listo? Continúa con [Laboratorio 04: Diseño y Esquema de Base de Datos](../04-Database/README.md)

---

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por garantizar la precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o imprecisiones. El documento original en su idioma nativo debe considerarse como la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o interpretaciones erróneas que puedan surgir del uso de esta traducción.