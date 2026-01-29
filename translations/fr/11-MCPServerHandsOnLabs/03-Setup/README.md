# Configuration de l'environnement

## 🎯 Ce que couvre ce laboratoire

Ce laboratoire pratique vous guide dans la configuration d'un environnement de développement complet pour créer des serveurs MCP avec une intégration PostgreSQL. Vous configurerez tous les outils nécessaires, déploierez des ressources Azure et validerez votre configuration avant de passer à l'implémentation.

## Vue d'ensemble

Un environnement de développement adéquat est essentiel pour réussir le développement de serveurs MCP. Ce laboratoire fournit des instructions étape par étape pour configurer Docker, les services Azure, les outils de développement et valider que tout fonctionne correctement ensemble.

À la fin de ce laboratoire, vous disposerez d'un environnement de développement entièrement fonctionnel prêt à construire le serveur MCP de Zava Retail.

## Objectifs d'apprentissage

À la fin de ce laboratoire, vous serez capable de :

- **Installer et configurer** tous les outils de développement requis
- **Déployer des ressources Azure** nécessaires pour le serveur MCP
- **Configurer des conteneurs Docker** pour PostgreSQL et le serveur MCP
- **Valider** votre configuration d'environnement avec des connexions de test
- **Résoudre** les problèmes courants de configuration et d'installation
- **Comprendre** le flux de travail de développement et la structure des fichiers

## 📋 Vérification des prérequis

Avant de commencer, assurez-vous d'avoir :

### Connaissances requises
- Utilisation de base de la ligne de commande (Windows Command Prompt/PowerShell)
- Compréhension des variables d'environnement
- Familiarité avec le contrôle de version Git
- Concepts de base de Docker (conteneurs, images, volumes)

### Configuration système
- **Système d'exploitation** : Windows 10/11, macOS ou Linux
- **RAM** : Minimum 8 Go (16 Go recommandés)
- **Stockage** : Au moins 10 Go d'espace libre
- **Réseau** : Connexion Internet pour les téléchargements et le déploiement Azure

### Comptes requis
- **Abonnement Azure** : Le niveau gratuit est suffisant
- **Compte GitHub** : Pour accéder au dépôt
- **Compte Docker Hub** : (Optionnel) Pour publier des images personnalisées

## 🛠️ Installation des outils

### 1. Installer Docker Desktop

Docker fournit l'environnement conteneurisé pour notre configuration de développement.

#### Installation sur Windows

1. **Télécharger Docker Desktop** :
   ```cmd
   # Visit https://desktop.docker.com/win/stable/Docker%20Desktop%20Installer.exe
   # Or use Windows Package Manager
   winget install Docker.DockerDesktop
   ```

2. **Installer et configurer** :
   - Exécutez l'installateur en tant qu'administrateur
   - Activez l'intégration WSL 2 lorsque cela est demandé
   - Redémarrez votre ordinateur une fois l'installation terminée

3. **Vérifier l'installation** :
   ```cmd
   docker --version
   docker-compose --version
   ```

#### Installation sur macOS

1. **Télécharger et installer** :
   ```bash
   # Download from https://desktop.docker.com/mac/stable/Docker.dmg
   # Or use Homebrew
   brew install --cask docker
   ```

2. **Démarrer Docker Desktop** :
   - Lancez Docker Desktop depuis Applications
   - Complétez l'assistant de configuration initiale

3. **Vérifier l'installation** :
   ```bash
   docker --version
   docker-compose --version
   ```

#### Installation sur Linux

1. **Installer Docker Engine** :
   ```bash
   # Ubuntu/Debian
   curl -fsSL https://get.docker.com -o get-docker.sh
   sudo sh get-docker.sh
   sudo usermod -aG docker $USER
   
   # Log out and back in for group changes to take effect
   ```

2. **Installer Docker Compose** :
   ```bash
   sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
   sudo chmod +x /usr/local/bin/docker-compose
   ```

### 2. Installer Azure CLI

Azure CLI permet le déploiement et la gestion des ressources Azure.

#### Installation sur Windows

```cmd
# Using Windows Package Manager
winget install Microsoft.AzureCLI

# Or download MSI from: https://aka.ms/installazurecliwindows
```

#### Installation sur macOS

```bash
# Using Homebrew
brew install azure-cli

# Or using installer
curl -L https://aka.ms/InstallAzureCli | bash
```

#### Installation sur Linux

```bash
# Ubuntu/Debian
curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash

# RHEL/CentOS
sudo rpm --import https://packages.microsoft.com/keys/microsoft.asc
sudo dnf install azure-cli
```

#### Vérification et authentification

```bash
# Check installation
az version

# Login to Azure
az login

# Set default subscription (if you have multiple)
az account list --output table
az account set --subscription "Your-Subscription-Name"
```

### 3. Installer Git

Git est nécessaire pour cloner le dépôt et gérer le contrôle de version.

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

### 4. Installer VS Code

Visual Studio Code fournit l'environnement de développement intégré avec support MCP.

#### Installation

```cmd
# Windows
winget install Microsoft.VisualStudioCode

# macOS
brew install --cask visual-studio-code

# Linux (Ubuntu/Debian)
sudo snap install code --classic
```

#### Extensions requises

Installez ces extensions VS Code :

```bash
# Install via command line
code --install-extension ms-python.python
code --install-extension ms-vscode.vscode-json
code --install-extension ms-azuretools.vscode-docker
code --install-extension ms-vscode.azure-account
```

Ou installez via VS Code :
1. Ouvrez VS Code
2. Accédez aux Extensions (Ctrl+Shift+X)
3. Installez :
   - **Python** (Microsoft)
   - **Docker** (Microsoft)
   - **Azure Account** (Microsoft)
   - **JSON** (Microsoft)

### 5. Installer Python

Python 3.8+ est requis pour le développement du serveur MCP.

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

#### Vérifier l'installation

```bash
python --version  # Should show Python 3.11.x
pip --version      # Should show pip version
```

## 🚀 Configuration du projet

### 1. Cloner le dépôt

```bash
# Clone the main repository
git clone https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail.git

# Navigate to the project directory
cd MCP-Server-and-PostgreSQL-Sample-Retail

# Verify repository structure
ls -la
```

### 2. Créer un environnement virtuel Python

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

### 3. Installer les dépendances Python

```bash
# Install development dependencies
pip install -r requirements.lock.txt

# Verify key packages
pip list | grep fastmcp
pip list | grep asyncpg
pip list | grep azure
```

## ☁️ Déploiement des ressources Azure

### 1. Comprendre les besoins en ressources

Notre serveur MCP nécessite les ressources Azure suivantes :

| **Ressource** | **Objectif** | **Coût estimé** |
|---------------|--------------|-----------------|
| **Azure AI Foundry** | Hébergement et gestion des modèles IA | 10-50 $/mois |
| **Déploiement OpenAI** | Modèle d'intégration de texte (text-embedding-3-small) | 5-20 $/mois |
| **Application Insights** | Surveillance et télémétrie | 5-15 $/mois |
| **Groupe de ressources** | Organisation des ressources | Gratuit |

### 2. Déployer les ressources Azure

#### Option A : Déploiement automatisé (recommandé)

```bash
# Navigate to infrastructure directory
cd infra

# Windows - PowerShell
./deploy.ps1

# macOS/Linux - Bash
./deploy.sh
```

Le script de déploiement effectuera :
1. La création d'un groupe de ressources unique
2. Le déploiement des ressources Azure AI Foundry
3. Le déploiement du modèle text-embedding-3-small
4. La configuration d'Application Insights
5. La création d'un principal de service pour l'authentification
6. La génération d'un fichier `.env` avec la configuration

#### Option B : Déploiement manuel

Si vous préférez un contrôle manuel ou si le script automatisé échoue :

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

### 3. Vérifier le déploiement Azure

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

### 4. Configurer les variables d'environnement

Après le déploiement, vous devriez avoir un fichier `.env`. Vérifiez qu'il contient :

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

## 🐳 Configuration de l'environnement Docker

### 1. Comprendre la composition Docker

Notre environnement de développement utilise Docker Compose :

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

### 2. Démarrer l'environnement de développement

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

### 3. Vérifier la configuration de la base de données

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

### 4. Tester le serveur MCP

```bash
# Check MCP server health
curl http://localhost:8000/health

# Test basic MCP endpoint
curl -X POST http://localhost:8000/mcp \
  -H "Content-Type: application/json" \
  -H "x-rls-user-id: 00000000-0000-0000-0000-000000000000" \
  -d '{"method": "tools/list", "params": {}}'
```

## 🔧 Configuration de VS Code

### 1. Configurer l'intégration MCP

Créez une configuration MCP pour VS Code :

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

### 2. Configurer l'environnement Python

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

### 3. Tester l'intégration VS Code

1. **Ouvrir le projet dans VS Code** :
   ```bash
   code .
   ```

2. **Ouvrir AI Chat** :
   - Appuyez sur `Ctrl+Shift+P` (Windows/Linux) ou `Cmd+Shift+P` (macOS)
   - Tapez "AI Chat" et sélectionnez "AI Chat: Open Chat"

3. **Tester la connexion au serveur MCP** :
   - Dans AI Chat, tapez `#zava` et sélectionnez l'un des serveurs configurés
   - Demandez : "Quelles tables sont disponibles dans la base de données ?"
   - Vous devriez recevoir une réponse listant les tables de la base de données retail

## ✅ Validation de l'environnement

### 1. Vérification complète du système

Exécutez ce script de validation pour vérifier votre configuration :

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

### 2. Liste de vérification de validation manuelle

**✅ Outils de base**
- [ ] Docker version 20.10+ installé et en cours d'exécution
- [ ] Azure CLI 2.40+ installé et authentifié
- [ ] Python 3.8+ avec pip installé
- [ ] Git 2.30+ installé
- [ ] VS Code avec les extensions requises

**✅ Ressources Azure**
- [ ] Groupe de ressources créé avec succès
- [ ] Projet AI Foundry déployé
- [ ] Modèle OpenAI text-embedding-3-small déployé
- [ ] Application Insights configuré
- [ ] Principal de service créé avec les permissions appropriées

**✅ Configuration de l'environnement**
- [ ] Fichier `.env` créé avec toutes les variables requises
- [ ] Identifiants Azure fonctionnels (test avec `az account show`)
- [ ] Conteneur PostgreSQL en cours d'exécution et accessible
- [ ] Données d'exemple chargées dans la base de données

**✅ Intégration VS Code**
- [ ] `.vscode/mcp.json` configuré
- [ ] Interpréteur Python défini sur l'environnement virtuel
- [ ] Les serveurs MCP apparaissent dans AI Chat
- [ ] Capable d'exécuter des requêtes de test via AI Chat

## 🛠️ Résolution des problèmes courants

### Problèmes Docker

**Problème** : Les conteneurs Docker ne démarrent pas
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

**Problème** : La connexion PostgreSQL échoue
```bash
# Check container logs
docker-compose logs postgres

# Verify container is healthy
docker-compose ps

# Test direct connection
docker-compose exec postgres psql -U postgres -d zava -c "SELECT 1;"
```

### Problèmes de déploiement Azure

**Problème** : Le déploiement Azure échoue
```bash
# Check Azure CLI authentication
az account show

# Verify subscription permissions
az role assignment list --assignee $(az account show --query user.name -o tsv)

# Check resource provider registration
az provider register --namespace Microsoft.CognitiveServices
az provider register --namespace Microsoft.Insights
```

**Problème** : L'authentification du service IA échoue
```bash
# Test service principal
az login --service-principal \
  --username $AZURE_CLIENT_ID \
  --password $AZURE_CLIENT_SECRET \
  --tenant $AZURE_TENANT_ID

# Verify AI service deployment
az cognitiveservices account list --query "[].{Name:name,Kind:kind,Location:location}"
```

### Problèmes d'environnement Python

**Problème** : L'installation des packages échoue
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

**Problème** : VS Code ne trouve pas l'interpréteur Python
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

## 🎯 Points clés

Après avoir terminé ce laboratoire, vous devriez avoir :

✅ **Environnement de développement complet** : Tous les outils installés et configurés  
✅ **Ressources Azure déployées** : Services IA et infrastructure de support  
✅ **Environnement Docker opérationnel** : Conteneurs PostgreSQL et serveur MCP  
✅ **Intégration VS Code** : Serveurs MCP configurés et accessibles  
✅ **Configuration validée** : Tous les composants testés et fonctionnant ensemble  
✅ **Connaissances en dépannage** : Problèmes courants et solutions  

## 🚀 Et après

Avec votre environnement prêt, continuez avec **[Lab 04 : Conception et schéma de base de données](../04-Database/README.md)** pour :

- Explorer en détail le schéma de la base de données retail
- Comprendre la modélisation des données multi-locataires
- Apprendre à implémenter la sécurité au niveau des lignes
- Travailler avec des données retail d'exemple

## 📚 Ressources supplémentaires

### Outils de développement
- [Documentation Docker](https://docs.docker.com/) - Référence complète Docker
- [Référence Azure CLI](https://docs.microsoft.com/cli/azure/) - Commandes Azure CLI
- [Documentation VS Code](https://code.visualstudio.com/docs) - Configuration de l'éditeur et extensions

### Services Azure
- [Documentation Azure AI Foundry](https://docs.microsoft.com/azure/ai-foundry/) - Configuration des services IA
- [Service Azure OpenAI](https://docs.microsoft.com/azure/cognitive-services/openai/) - Déploiement de modèles IA
- [Application Insights](https://docs.microsoft.com/azure/azure-monitor/app/app-insights-overview) - Configuration de la surveillance

### Développement Python
- [Environnements virtuels Python](https://docs.python.org/3/tutorial/venv.html) - Gestion des environnements
- [Documentation AsyncIO](https://docs.python.org/3/library/asyncio.html) - Modèles de programmation asynchrone
- [Documentation FastAPI](https://fastapi.tiangolo.com/) - Modèles de framework web

---

**Suivant** : Environnement prêt ? Continuez avec [Lab 04 : Conception et schéma de base de données](../04-Database/README.md)

---

**Avertissement** :  
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, il est recommandé de recourir à une traduction humaine professionnelle. Nous déclinons toute responsabilité en cas de malentendus ou d'interprétations erronées résultant de l'utilisation de cette traduction.