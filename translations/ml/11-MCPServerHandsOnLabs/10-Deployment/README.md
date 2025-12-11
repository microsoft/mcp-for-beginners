<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "42c4bda55924cd1d6964c1a01fe65f28",
  "translation_date": "2025-12-11T14:18:52+00:00",
  "source_file": "11-MCPServerHandsOnLabs/10-Deployment/README.md",
  "language_code": "ml"
}
-->
# വിന്യാസ തന്ത്രങ്ങൾ

## 🎯 ഈ ലാബ് ഉൾക്കൊള്ളുന്നത്

ഈ ലാബ് ആധുനിക കണ്ടെയ്‌നറൈസേഷൻ, ക്ലൗഡ്-നേറ്റീവ് സമീപനങ്ങൾ ഉപയോഗിച്ച് നിങ്ങളുടെ MCP റീട്ടെയിൽ സെർവർ പ്രൊഡക്ഷൻ പരിസ്ഥിതികളിലേക്ക് വിന്യസിക്കുന്നതിൽ സമഗ്ര മാർഗ്ഗനിർദ്ദേശം നൽകുന്നു. എന്റർപ്രൈസ് വർക്ക്‌ലോഡുകൾ കൈകാര്യം ചെയ്യാൻ കഴിയുന്ന സ്കേലബിൾ, സുരക്ഷിതവും നിരീക്ഷണമുള്ള MCP സെർവർ വിന്യസിക്കാൻ നിങ്ങൾക്ക് പഠിക്കാം.

## അവലോകനം

MCP സെർവറുകളുടെ പ്രൊഡക്ഷൻ വിന്യാസത്തിന് കണ്ടെയ്‌നറൈസേഷൻ, ഓർക്കസ്ട്രേഷൻ, സുരക്ഷ, സ്കേലബിലിറ്റി, നിരീക്ഷണം എന്നിവയുടെ സൂക്ഷ്മ പരിഗണന ആവശ്യമാണ്. ഈ ലാബ് Azure Container Apps-ലേക്ക് PostgreSQL Flexible Server ഉപയോഗിച്ച് വിന്യസിക്കൽ, CI/CD പൈപ്പ്ലൈനുകൾ നടപ്പിലാക്കൽ, വ്യത്യസ്ത വർക്ക്‌ലോഡുകൾക്കായി ഓട്ടോ-സ്കേലിംഗ് കോൺഫിഗർ ചെയ്യൽ എന്നിവ ഉൾക്കൊള്ളുന്നു.

വിന്യാസ തന്ത്രങ്ങൾ വികസനത്തിനുള്ള ലളിതമായ സിംഗിൾ-കണ്ടെയ്‌നർ വിന്യാസങ്ങളിൽ നിന്ന് സമഗ്ര നിരീക്ഷണവും സുരക്ഷാ സവിശേഷതകളും ഉള്ള സങ്കീർണ്ണമായ മൾട്ടി-റീജിയൻ, ഓട്ടോ-സ്കേലിംഗ് പ്രൊഡക്ഷൻ പരിസ്ഥിതികളിലേക്കും വ്യാപിക്കുന്നു.

## പഠന ലക്ഷ്യങ്ങൾ

ഈ ലാബ് പൂർത്തിയാക്കിയാൽ, നിങ്ങൾക്ക് കഴിയും:

- **Docker** ഉപയോഗിച്ച് മൾട്ടി-സ്റ്റേജ് ബിൽഡുകളോടെ MCP സെർവർ കണ്ടെയ്‌നറൈസ് ചെയ്യുക  
- **Azure Container Apps**-ലേക്ക് സുരക്ഷിത നെറ്റ്വർക്കിങ്ങോടെ വിന്യസിക്കുക  
- ഉയർന്ന ലഭ്യതയുള്ള പ്രൊഡക്ഷൻ-ഗ്രേഡ് PostgreSQL കോൺഫിഗർ ചെയ്യുക  
- ഓട്ടോമേറ്റഡ് വിന്യാസത്തിനായി CI/CD പൈപ്പ്ലൈനുകൾ നടപ്പിലാക്കുക  
- ആവശ്യകത അനുസരിച്ച് ആപ്ലിക്കേഷനുകൾ സ്വയം സ്കേൽ ചെയ്യുക  
- സമഗ്ര നിരീക്ഷണത്തോടെ പ്രൊഡക്ഷൻ വിന്യാസങ്ങൾ നിരീക്ഷിക്കുക  

## 🐳 Docker കണ്ടെയ്‌നറൈസേഷൻ

### മൾട്ടി-സ്റ്റേജ് Dockerfile

```dockerfile
# Dockerfile - Production-ready multi-stage build
FROM python:3.11-slim AS builder

# Set build environment
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

# Install build dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Create virtual environment
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Copy requirements and install dependencies
COPY requirements.lock.txt /tmp/
RUN pip install --no-cache-dir -r /tmp/requirements.lock.txt

# Production stage
FROM python:3.11-slim AS production

# Set production environment
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PATH="/opt/venv/bin:$PATH" \
    PYTHONPATH="/app"

# Install runtime dependencies
RUN apt-get update && apt-get install -y \
    libpq5 \
    curl \
    && rm -rf /var/lib/apt/lists/* \
    && groupadd -r mcp \
    && useradd -r -g mcp -d /app -s /bin/bash mcp

# Copy virtual environment from builder
COPY --from=builder /opt/venv /opt/venv

# Set working directory and copy application
WORKDIR /app
COPY --chown=mcp:mcp . .

# Create necessary directories with proper permissions
RUN mkdir -p /app/logs /app/data /tmp/mcp \
    && chown -R mcp:mcp /app /tmp/mcp \
    && chmod -R 755 /app

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=60s --retries=3 \
    CMD python -m mcp_server.health_check || exit 1

# Switch to non-root user
USER mcp

# Expose port
EXPOSE 8000

# Default command
CMD ["python", "-m", "mcp_server.main"]
```

### വികസനത്തിനുള്ള Docker Compose

```yaml
# docker-compose.yml - Development environment
version: '3.8'

services:
  mcp-server:
    build:
      context: .
      dockerfile: Dockerfile
      target: production
    ports:
      - "8000:8000"
    environment:
      - POSTGRES_HOST=postgres
      - POSTGRES_PORT=5432
      - POSTGRES_DB=retail_db
      - POSTGRES_USER=mcp_user
      - POSTGRES_PASSWORD=${POSTGRES_PASSWORD}
      - PROJECT_ENDPOINT=${PROJECT_ENDPOINT}
      - AZURE_CLIENT_ID=${AZURE_CLIENT_ID}
      - AZURE_CLIENT_SECRET=${AZURE_CLIENT_SECRET}
      - AZURE_TENANT_ID=${AZURE_TENANT_ID}
      - LOG_LEVEL=INFO
      - ENVIRONMENT=development
    depends_on:
      postgres:
        condition: service_healthy
    volumes:
      - ./logs:/app/logs
    networks:
      - mcp-network
    restart: unless-stopped
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:8000/health"]
      interval: 30s
      timeout: 10s
      retries: 3
      start_period: 60s

  postgres:
    image: pgvector/pgvector:pg16
    environment:
      - POSTGRES_DB=retail_db
      - POSTGRES_USER=postgres
      - POSTGRES_PASSWORD=${POSTGRES_ADMIN_PASSWORD}
    ports:
      - "5432:5432"
    volumes:
      - postgres_data:/var/lib/postgresql/data
      - ./docker-init:/docker-entrypoint-initdb.d
      - ./data:/backup
    networks:
      - mcp-network
    restart: unless-stopped
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U postgres -d retail_db"]
      interval: 30s
      timeout: 10s
      retries: 3
      start_period: 60s

  redis:
    image: redis:7-alpine
    ports:
      - "6379:6379"
    command: redis-server --appendonly yes --requirepass ${REDIS_PASSWORD}
    volumes:
      - redis_data:/data
    networks:
      - mcp-network
    restart: unless-stopped
    healthcheck:
      test: ["CMD", "redis-cli", "--raw", "incr", "ping"]
      interval: 30s
      timeout: 10s
      retries: 3

volumes:
  postgres_data:
    driver: local
  redis_data:
    driver: local

networks:
  mcp-network:
    driver: bridge
```

### പ്രൊഡക്ഷൻ Docker Compose

```yaml
# docker-compose.prod.yml - Production environment
version: '3.8'

services:
  mcp-server:
    image: ${CONTAINER_REGISTRY}/mcp-retail-server:${IMAGE_TAG}
    ports:
      - "8000:8000"
    environment:
      - POSTGRES_HOST=${POSTGRES_HOST}
      - POSTGRES_PORT=${POSTGRES_PORT}
      - POSTGRES_DB=${POSTGRES_DB}
      - POSTGRES_USER=${POSTGRES_USER}
      - POSTGRES_PASSWORD=${POSTGRES_PASSWORD}
      - PROJECT_ENDPOINT=${PROJECT_ENDPOINT}
      - AZURE_CLIENT_ID=${AZURE_CLIENT_ID}
      - AZURE_CLIENT_SECRET=${AZURE_CLIENT_SECRET}
      - AZURE_TENANT_ID=${AZURE_TENANT_ID}
      - APPLICATIONINSIGHTS_CONNECTION_STRING=${APPLICATIONINSIGHTS_CONNECTION_STRING}
      - LOG_LEVEL=INFO
      - ENVIRONMENT=production
      - REDIS_URL=${REDIS_URL}
    deploy:
      replicas: 3
      resources:
        limits:
          cpus: '2.0'
          memory: 2G
        reservations:
          cpus: '0.5'
          memory: 512M
      restart_policy:
        condition: on-failure
        delay: 5s
        max_attempts: 3
      update_config:
        parallelism: 1
        delay: 10s
        failure_action: rollback
    networks:
      - mcp-network
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:8000/health"]
      interval: 30s
      timeout: 10s
      retries: 3
      start_period: 60s

networks:
  mcp-network:
    external: true
```

## ☁️ Azure Container Apps വിന്യാസം

### Bicep ഉപയോഗിച്ച് ഇൻഫ്രാസ്ട്രക്ചർ കോഡ് ആയി

```bicep
// infra/container-apps.bicep - Azure Container Apps deployment
@description('Location for all resources')
param location string = resourceGroup().location

@description('Environment name')
param environmentName string

@description('Container App name')
param containerAppName string

@description('Container registry details')
param containerRegistry object

@description('Database connection details')
@secure()
param databaseConnectionString string

@description('Azure OpenAI configuration')
param azureOpenAI object

@description('Application Insights workspace ID')
param workspaceId string

// Container Apps Environment
resource containerAppsEnvironment 'Microsoft.App/managedEnvironments@2023-05-01' = {
  name: '${environmentName}-env'
  location: location
  properties: {
    appLogsConfiguration: {
      destination: 'log-analytics'
      logAnalyticsConfiguration: {
        customerId: workspaceId
      }
    }
    infrastructureResourceGroup: '${environmentName}-infra-rg'
  }
}

// Container App
resource mcp_retail_server 'Microsoft.App/containerApps@2023-05-01' = {
  name: containerAppName
  location: location
  properties: {
    managedEnvironmentId: containerAppsEnvironment.id
    configuration: {
      activeRevisionsMode: 'Single'
      ingress: {
        external: false
        targetPort: 8000
        allowInsecure: false
        traffic: [
          {
            weight: 100
            latestRevision: true
          }
        ]
      }
      registries: [
        {
          server: containerRegistry.server
          identity: containerRegistry.identity
        }
      ]
      secrets: [
        {
          name: 'database-connection-string'
          value: databaseConnectionString
        }
        {
          name: 'azure-openai-key'
          value: azureOpenAI.apiKey
        }
      ]
    }
    template: {
      containers: [
        {
          name: 'mcp-retail-server'
          image: '${containerRegistry.server}/mcp-retail-server:latest'
          resources: {
            cpu: json('1.0')
            memory: '2Gi'
          }
          env: [
            {
              name: 'POSTGRES_CONNECTION_STRING'
              secretRef: 'database-connection-string'
            }
            {
              name: 'PROJECT_ENDPOINT'
              value: azureOpenAI.endpoint
            }
            {
              name: 'AZURE_OPENAI_API_KEY'
              secretRef: 'azure-openai-key'
            }
            {
              name: 'LOG_LEVEL'
              value: 'INFO'
            }
            {
              name: 'ENVIRONMENT'
              value: 'production'
            }
          ]
          probes: [
            {
              type: 'Liveness'
              httpGet: {
                path: '/health'
                port: 8000
                scheme: 'HTTP'
              }
              initialDelaySeconds: 60
              periodSeconds: 30
              timeoutSeconds: 10
              failureThreshold: 3
            }
            {
              type: 'Readiness'
              httpGet: {
                path: '/ready'
                port: 8000
                scheme: 'HTTP'
              }
              initialDelaySeconds: 30
              periodSeconds: 10
              timeoutSeconds: 5
              failureThreshold: 3
            }
          ]
        }
      ]
      scale: {
        minReplicas: 2
        maxReplicas: 20
        rules: [
          {
            name: 'http-scaling'
            http: {
              metadata: {
                concurrentRequests: '10'
              }
            }
          }
          {
            name: 'cpu-scaling'
            custom: {
              type: 'cpu'
              metadata: {
                type: 'Utilization'
                value: '70'
              }
            }
          }
        ]
      }
    }
  }
}

// Output the FQDN
output containerAppFQDN string = mcp_retail_server.properties.configuration.ingress.fqdn
output containerAppId string = mcp_retail_server.id
```

### PostgreSQL Flexible Server

```bicep
// infra/database.bicep - PostgreSQL Flexible Server
@description('Location for all resources')
param location string = resourceGroup().location

@description('PostgreSQL server name')
param serverName string

@description('Database administrator login')
param administratorLogin string

@description('Database administrator password')
@secure()
param administratorPassword string

@description('Virtual network subnet ID')
param subnetId string

@description('Private DNS zone ID')
param privateDnsZoneId string

// PostgreSQL Flexible Server
resource postgresqlServer 'Microsoft.DBforPostgreSQL/flexibleServers@2023-03-01-preview' = {
  name: serverName
  location: location
  sku: {
    name: 'Standard_D4s_v3'
    tier: 'GeneralPurpose'
  }
  properties: {
    administratorLogin: administratorLogin
    administratorLoginPassword: administratorPassword
    version: '16'
    storage: {
      storageSizeGB: 128
      autoGrow: 'Enabled'
      type: 'PremiumSSD'
    }
    backup: {
      backupRetentionDays: 35
      geoRedundantBackup: 'Enabled'
    }
    highAvailability: {
      mode: 'ZoneRedundant'
    }
    network: {
      delegatedSubnetResourceId: subnetId
      privateDnsZoneArmResourceId: privateDnsZoneId
    }
    maintenanceWindow: {
      dayOfWeek: 0
      startHour: 2
      startMinute: 0
    }
  }
}

// Database
resource retailDatabase 'Microsoft.DBforPostgreSQL/flexibleServers/databases@2023-03-01-preview' = {
  parent: postgresqlServer
  name: 'retail_db'
  properties: {
    charset: 'UTF8'
    collation: 'en_US.utf8'
  }
}

// PostgreSQL extensions
resource pgvectorExtension 'Microsoft.DBforPostgreSQL/flexibleServers/configurations@2023-03-01-preview' = {
  parent: postgresqlServer
  name: 'shared_preload_libraries'
  properties: {
    value: 'pg_stat_statements,pgaudit,vector'
    source: 'user-override'
  }
}

// Output connection details
output serverFQDN string = postgresqlServer.properties.fullyQualifiedDomainName
output serverId string = postgresqlServer.id
output databaseName string = retailDatabase.name
```

## 🚀 CI/CD പൈപ്പ്ലൈൻ കോൺഫിഗറേഷൻ

### GitHub Actions വർക്ക്‌ഫ്ലോ

```yaml
# .github/workflows/deploy.yml - CI/CD pipeline
name: Deploy MCP Retail Server

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]
  workflow_dispatch:
    inputs:
      environment:
        description: 'Deployment environment'
        required: true
        default: 'development'
        type: choice
        options:
          - development
          - staging
          - production

env:
  CONTAINER_REGISTRY: mcpretailregistry.azurecr.io
  IMAGE_NAME: mcp-retail-server
  AZURE_RESOURCE_GROUP: mcp-retail-rg

jobs:
  test:
    runs-on: ubuntu-latest
    services:
      postgres:
        image: pgvector/pgvector:pg16
        env:
          POSTGRES_PASSWORD: postgres
          POSTGRES_DB: retail_test
        options: >-
          --health-cmd pg_isready
          --health-interval 10s
          --health-timeout 5s
          --health-retries 5
        ports:
          - 5432:5432

    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'
          cache: 'pip'

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.lock.txt
          pip install pytest pytest-cov pytest-asyncio

      - name: Set up test database
        run: |
          PGPASSWORD=postgres psql -h localhost -U postgres -d retail_test -f scripts/create_schema.sql
          python scripts/generate_sample_data.py --test
        env:
          POSTGRES_HOST: localhost
          POSTGRES_PORT: 5432
          POSTGRES_DB: retail_test
          POSTGRES_USER: postgres
          POSTGRES_PASSWORD: postgres

      - name: Run tests
        run: |
          pytest tests/ -v --cov=mcp_server --cov-report=xml --cov-report=html
        env:
          POSTGRES_HOST: localhost
          POSTGRES_PORT: 5432
          POSTGRES_DB: retail_test
          POSTGRES_USER: postgres
          POSTGRES_PASSWORD: postgres
          PROJECT_ENDPOINT: ${{ secrets.TEST_PROJECT_ENDPOINT }}
          AZURE_CLIENT_ID: ${{ secrets.TEST_AZURE_CLIENT_ID }}
          AZURE_CLIENT_SECRET: ${{ secrets.TEST_AZURE_CLIENT_SECRET }}
          AZURE_TENANT_ID: ${{ secrets.AZURE_TENANT_ID }}

      - name: Upload coverage reports
        uses: codecov/codecov-action@v3
        with:
          file: ./coverage.xml
          flags: unittests

  security-scan:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Run Trivy vulnerability scanner
        uses: aquasecurity/trivy-action@master
        with:
          scan-type: 'fs'
          scan-ref: '.'
          format: 'sarif'
          output: 'trivy-results.sarif'

      - name: Upload Trivy scan results
        uses: github/codeql-action/upload-sarif@v2
        with:
          sarif_file: 'trivy-results.sarif'

      - name: Run Bandit security linter
        run: |
          pip install bandit[toml]
          bandit -r mcp_server/ -f json -o bandit-report.json

  build:
    runs-on: ubuntu-latest
    needs: [test, security-scan]
    if: github.event_name == 'push' || github.event_name == 'workflow_dispatch'
    
    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Azure Login
        uses: azure/login@v1
        with:
          creds: ${{ secrets.AZURE_CREDENTIALS }}

      - name: Build and push Docker image
        uses: azure/docker-login@v1
        with:
          login-server: ${{ env.CONTAINER_REGISTRY }}
          username: ${{ secrets.REGISTRY_USERNAME }}
          password: ${{ secrets.REGISTRY_PASSWORD }}

      - name: Build, tag, and push image
        run: |
          # Generate unique tag
          IMAGE_TAG="${GITHUB_SHA::8}-$(date +%s)"
          
          # Build image
          docker build \
            --target production \
            --tag $CONTAINER_REGISTRY/$IMAGE_NAME:$IMAGE_TAG \
            --tag $CONTAINER_REGISTRY/$IMAGE_NAME:latest \
            .
          
          # Push images
          docker push $CONTAINER_REGISTRY/$IMAGE_NAME:$IMAGE_TAG
          docker push $CONTAINER_REGISTRY/$IMAGE_NAME:latest
          
          # Save tag for deployment
          echo "IMAGE_TAG=$IMAGE_TAG" >> $GITHUB_ENV

      - name: Output image details
        run: |
          echo "Built and pushed image: $CONTAINER_REGISTRY/$IMAGE_NAME:$IMAGE_TAG"

  deploy-staging:
    runs-on: ubuntu-latest
    needs: build
    if: github.event_name == 'push' && github.ref == 'refs/heads/main'
    environment: staging

    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Azure Login
        uses: azure/login@v1
        with:
          creds: ${{ secrets.AZURE_CREDENTIALS }}

      - name: Deploy to staging
        uses: azure/CLI@v1
        with:
          azcliversion: latest
          inlineScript: |
            # Deploy infrastructure
            az deployment group create \
              --resource-group $AZURE_RESOURCE_GROUP-staging \
              --template-file infra/main.bicep \
              --parameters infra/main.parameters.staging.json \
              --parameters containerImageTag=$IMAGE_TAG

            # Update container app
            az containerapp update \
              --name mcp-retail-server-staging \
              --resource-group $AZURE_RESOURCE_GROUP-staging \
              --image $CONTAINER_REGISTRY/$IMAGE_NAME:$IMAGE_TAG

      - name: Run integration tests
        run: |
          # Wait for deployment to be ready
          sleep 60
          
          # Run integration tests against staging
          pytest tests/integration/ \
            --endpoint https://mcp-retail-server-staging.azurecontainerapps.io \
            --timeout 300

  deploy-production:
    runs-on: ubuntu-latest
    needs: [build, deploy-staging]
    if: github.event_name == 'workflow_dispatch' && github.event.inputs.environment == 'production'
    environment: production

    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Azure Login
        uses: azure/login@v1
        with:
          creds: ${{ secrets.AZURE_CREDENTIALS }}

      - name: Deploy to production
        uses: azure/CLI@v1
        with:
          azcliversion: latest
          inlineScript: |
            # Deploy with blue-green strategy
            az deployment group create \
              --resource-group $AZURE_RESOURCE_GROUP-prod \
              --template-file infra/main.bicep \
              --parameters infra/main.parameters.prod.json \
              --parameters containerImageTag=$IMAGE_TAG \
              --parameters deploymentSlot=green

            # Health check
            az containerapp show \
              --name mcp-retail-server-prod-green \
              --resource-group $AZURE_RESOURCE_GROUP-prod

            # Switch traffic (blue-green deployment)
            az containerapp ingress traffic set \
              --name mcp-retail-server-prod \
              --resource-group $AZURE_RESOURCE_GROUP-prod \
              --revision-weight latest=100
```

### Azure DevOps പൈപ്പ്ലൈൻ

```yaml
# azure-pipelines.yml - Azure DevOps pipeline
trigger:
  branches:
    include:
      - main
      - develop
  paths:
    exclude:
      - docs/*
      - README.md

variables:
  containerRegistry: 'mcpretailregistry.azurecr.io'
  imageName: 'mcp-retail-server'
  imageTag: '$(Build.BuildId)'
  azureServiceConnection: 'azure-service-connection'

stages:
  - stage: Build
    displayName: 'Build and Test'
    jobs:
      - job: Test
        displayName: 'Run Tests'
        pool:
          vmImage: 'ubuntu-latest'
        
        services:
          postgres:
            image: pgvector/pgvector:pg16
            env:
              POSTGRES_PASSWORD: postgres
              POSTGRES_DB: retail_test
            ports:
              5432:5432

        steps:
          - task: UsePythonVersion@0
            inputs:
              versionSpec: '3.11'
              displayName: 'Use Python 3.11'

          - script: |
              python -m pip install --upgrade pip
              pip install -r requirements.lock.txt
              pip install pytest pytest-cov pytest-asyncio
            displayName: 'Install dependencies'

          - script: |
              PGPASSWORD=postgres psql -h localhost -U postgres -d retail_test -f scripts/create_schema.sql
              python scripts/generate_sample_data.py --test
            displayName: 'Set up test database'
            env:
              POSTGRES_HOST: localhost
              POSTGRES_PORT: 5432
              POSTGRES_DB: retail_test
              POSTGRES_USER: postgres
              POSTGRES_PASSWORD: postgres

          - script: |
              pytest tests/ -v --cov=mcp_server --cov-report=xml --junitxml=test-results.xml
            displayName: 'Run tests'
            env:
              POSTGRES_HOST: localhost
              POSTGRES_PORT: 5432
              POSTGRES_DB: retail_test
              POSTGRES_USER: postgres
              POSTGRES_PASSWORD: postgres

          - task: PublishTestResults@2
            condition: succeededOrFailed()
            inputs:
              testResultsFiles: 'test-results.xml'
              testRunTitle: 'Python Tests'

          - task: PublishCodeCoverageResults@1
            inputs:
              codeCoverageTool: 'Cobertura'
              summaryFileLocation: 'coverage.xml'

      - job: Build
        displayName: 'Build Docker Image'
        dependsOn: Test
        pool:
          vmImage: 'ubuntu-latest'

        steps:
          - task: AzureCLI@2
            displayName: 'Build and push Docker image'
            inputs:
              azureSubscription: $(azureServiceConnection)
              scriptType: 'bash'
              scriptLocation: 'inlineScript'
              inlineScript: |
                # Login to container registry
                az acr login --name $(containerRegistry)
                
                # Build and push image
                docker build \
                  --target production \
                  --tag $(containerRegistry)/$(imageName):$(imageTag) \
                  --tag $(containerRegistry)/$(imageName):latest \
                  .
                
                docker push $(containerRegistry)/$(imageName):$(imageTag)
                docker push $(containerRegistry)/$(imageName):latest

  - stage: Deploy_Staging
    displayName: 'Deploy to Staging'
    dependsOn: Build
    condition: and(succeeded(), eq(variables['Build.SourceBranch'], 'refs/heads/main'))
    
    jobs:
      - deployment: DeployStaging
        displayName: 'Deploy to Staging Environment'
        pool:
          vmImage: 'ubuntu-latest'
        environment: 'staging'
        
        strategy:
          runOnce:
            deploy:
              steps:
                - task: AzureCLI@2
                  displayName: 'Deploy infrastructure'
                  inputs:
                    azureSubscription: $(azureServiceConnection)
                    scriptType: 'bash'
                    scriptLocation: 'inlineScript'
                    inlineScript: |
                      az deployment group create \
                        --resource-group mcp-retail-staging-rg \
                        --template-file infra/main.bicep \
                        --parameters infra/main.parameters.staging.json \
                        --parameters containerImageTag=$(imageTag)

  - stage: Deploy_Production
    displayName: 'Deploy to Production'
    dependsOn: Deploy_Staging
    condition: and(succeeded(), eq(variables['Build.Reason'], 'Manual'))
    
    jobs:
      - deployment: DeployProduction
        displayName: 'Deploy to Production Environment'
        pool:
          vmImage: 'ubuntu-latest'
        environment: 'production'
        
        strategy:
          runOnce:
            deploy:
              steps:
                - task: AzureCLI@2
                  displayName: 'Deploy to production'
                  inputs:
                    azureSubscription: $(azureServiceConnection)
                    scriptType: 'bash'
                    scriptLocation: 'inlineScript'
                    inlineScript: |
                      az deployment group create \
                        --resource-group mcp-retail-prod-rg \
                        --template-file infra/main.bicep \
                        --parameters infra/main.parameters.prod.json \
                        --parameters containerImageTag=$(imageTag)
```

## 📊 സ്കേലിംഗ് ಮತ್ತು പ്രകടനം

### ഓട്ടോ-സ്കേലിംഗ് കോൺഫിഗറേഷൻ

```yaml
# k8s/hpa.yaml - Horizontal Pod Autoscaler for Kubernetes
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: mcp-retail-server-hpa
  namespace: mcp-retail
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: mcp-retail-server
  minReplicas: 3
  maxReplicas: 50
  metrics:
    - type: Resource
      resource:
        name: cpu
        target:
          type: Utilization
          averageUtilization: 70
    - type: Resource
      resource:
        name: memory
        target:
          type: Utilization
          averageUtilization: 80
    - type: Pods
      pods:
        metric:
          name: http_requests_per_second
        target:
          type: AverageValue
          averageValue: 100
  behavior:
    scaleDown:
      stabilizationWindowSeconds: 300
      policies:
        - type: Percent
          value: 50
          periodSeconds: 60
    scaleUp:
      stabilizationWindowSeconds: 60
      policies:
        - type: Percent
          value: 100
          periodSeconds: 30
        - type: Pods
          value: 5
          periodSeconds: 30
      selectPolicy: Max
```

### പ്രകടന നിരീക്ഷണം

```python
# mcp_server/monitoring/performance.py
"""
Performance monitoring and metrics collection for production deployment.
"""
import asyncio
import time
import psutil
from typing import Dict, Any
from dataclasses import dataclass
from datetime import datetime, timedelta
import logging

@dataclass
class PerformanceMetrics:
    """Performance metrics data structure."""
    timestamp: datetime
    cpu_percent: float
    memory_percent: float
    memory_used_mb: float
    active_connections: int
    request_rate: float
    avg_response_time: float
    error_rate: float
    database_connections: int

class PerformanceMonitor:
    """Monitor and collect performance metrics."""
    
    def __init__(self, config):
        self.config = config
        self.logger = logging.getLogger(__name__)
        
        # മെട്രിക്‌സ് ശേഖരണം
        self.metrics_history = []
        self.request_times = []
        self.error_count = 0
        self.request_count = 0
        
        # ഡാറ്റാബേസ് നിരീക്ഷണം
        self.db_pool = None
        
    async def start_monitoring(self):
        """Start continuous performance monitoring."""
        
        self.logger.info("Starting performance monitoring")
        
        # മെട്രിക്‌സ് ശേഖരണ ടാസ്‌ക് ആരംഭിക്കുക
        asyncio.create_task(self._collect_metrics_loop())
        asyncio.create_task(self._cleanup_old_metrics())
        
    async def _collect_metrics_loop(self):
        """Continuously collect performance metrics."""
        
        while True:
            try:
                metrics = await self._collect_current_metrics()
                self.metrics_history.append(metrics)
                
                # നിർണായക മെട്രിക്‌സ് ലോഗ് ചെയ്യുക
                if metrics.cpu_percent > 90:
                    self.logger.warning(f"High CPU usage: {metrics.cpu_percent:.1f}%")
                
                if metrics.memory_percent > 90:
                    self.logger.warning(f"High memory usage: {metrics.memory_percent:.1f}%")
                
                if metrics.error_rate > 0.05:  # 5% പിശക് നിരക്ക്
                    self.logger.warning(f"High error rate: {metrics.error_rate:.2%}")
                
                await asyncio.sleep(30)  # ഓരോ 30 സെക്കൻഡിലും ശേഖരിക്കുക
                
            except Exception as e:
                self.logger.error(f"Error collecting metrics: {e}")
                await asyncio.sleep(60)
    
    async def _collect_current_metrics(self) -> PerformanceMetrics:
        """Collect current system metrics."""
        
        # സിസ്റ്റം മെട്രിക്‌സ്
        cpu_percent = psutil.cpu_percent(interval=1)
        memory = psutil.virtual_memory()
        
        # അപ്ലിക്കേഷൻ മെട്രിക്‌സ്
        current_time = datetime.utcnow()
        recent_requests = [
            req_time for req_time in self.request_times
            if current_time - req_time < timedelta(minutes=1)
        ]
        
        request_rate = len(recent_requests) / 60.0  # സെക്കൻഡിൽ അഭ്യർത്ഥനകൾ
        
        # ശരാശരി പ്രതികരണ സമയം കണക്കാക്കുക
        avg_response_time = 0.0
        if hasattr(self, '_recent_response_times'):
            recent_response_times = [
                rt for rt in self._recent_response_times
                if current_time - rt['timestamp'] < timedelta(minutes=5)
            ]
            if recent_response_times:
                avg_response_time = sum(rt['time'] for rt in recent_response_times) / len(recent_response_times)
        
        # പിശക് നിരക്ക് കണക്കാക്കൽ
        error_rate = 0.0
        if self.request_count > 0:
            error_rate = self.error_count / self.request_count
        
        # ഡാറ്റാബേസ് കണക്ഷനുകൾ
        db_connections = 0
        if self.db_pool:
            db_connections = len(self.db_pool._holders)
        
        return PerformanceMetrics(
            timestamp=current_time,
            cpu_percent=cpu_percent,
            memory_percent=memory.percent,
            memory_used_mb=memory.used / (1024 * 1024),
            active_connections=0,  # കണക്ഷൻ ട്രാക്കിങ്ങുമായി നടപ്പിലാക്കേണ്ടത്
            request_rate=request_rate,
            avg_response_time=avg_response_time,
            error_rate=error_rate,
            database_connections=db_connections
        )
    
    async def _cleanup_old_metrics(self):
        """Clean up old metrics to prevent memory leaks."""
        
        while True:
            try:
                cutoff_time = datetime.utcnow() - timedelta(hours=24)
                
                # മെട്രിക്‌സ് ചരിത്രം ശുചിയാക്കുക
                self.metrics_history = [
                    m for m in self.metrics_history
                    if m.timestamp > cutoff_time
                ]
                
                # അഭ്യർത്ഥന സമയങ്ങൾ ശുചിയാക്കുക
                self.request_times = [
                    rt for rt in self.request_times
                    if rt > cutoff_time
                ]
                
                # കാലക്രമേണ കൗണ്ടറുകൾ റീസെറ്റ് ചെയ്യുക
                if datetime.utcnow().minute == 0:  # ഓരോ മണിക്കൂറിലും
                    self.error_count = 0
                    self.request_count = 0
                
                await asyncio.sleep(3600)  # ഓരോ മണിക്കൂറിലും പ്രവർത്തിപ്പിക്കുക
                
            except Exception as e:
                self.logger.error(f"Error cleaning up metrics: {e}")
                await asyncio.sleep(3600)
    
    def record_request(self, response_time: float, success: bool = True):
        """Record a request for metrics."""
        
        current_time = datetime.utcnow()
        self.request_times.append(current_time)
        self.request_count += 1
        
        if not success:
            self.error_count += 1
        
        # പ്രതികരണ സമയം രേഖപ്പെടുത്തുക
        if not hasattr(self, '_recent_response_times'):
            self._recent_response_times = []
        
        self._recent_response_times.append({
            'timestamp': current_time,
            'time': response_time
        })
    
    def get_current_metrics(self) -> Dict[str, Any]:
        """Get current performance metrics."""
        
        if not self.metrics_history:
            return {}
        
        latest_metrics = self.metrics_history[-1]
        
        return {
            'timestamp': latest_metrics.timestamp.isoformat(),
            'system': {
                'cpu_percent': latest_metrics.cpu_percent,
                'memory_percent': latest_metrics.memory_percent,
                'memory_used_mb': latest_metrics.memory_used_mb
            },
            'application': {
                'active_connections': latest_metrics.active_connections,
                'request_rate': latest_metrics.request_rate,
                'avg_response_time': latest_metrics.avg_response_time,
                'error_rate': latest_metrics.error_rate
            },
            'database': {
                'connections': latest_metrics.database_connections
            }
        }
    
    def get_metrics_summary(self, hours: int = 24) -> Dict[str, Any]:
        """Get performance metrics summary for the specified hours."""
        
        cutoff_time = datetime.utcnow() - timedelta(hours=hours)
        recent_metrics = [
            m for m in self.metrics_history
            if m.timestamp > cutoff_time
        ]
        
        if not recent_metrics:
            return {}
        
        # ശരാശരികൾ കണക്കാക്കുക
        avg_cpu = sum(m.cpu_percent for m in recent_metrics) / len(recent_metrics)
        avg_memory = sum(m.memory_percent for m in recent_metrics) / len(recent_metrics)
        avg_response_time = sum(m.avg_response_time for m in recent_metrics) / len(recent_metrics)
        
        # പരമാവധി മൂല്യങ്ങൾ കണക്കാക്കുക
        max_cpu = max(m.cpu_percent for m in recent_metrics)
        max_memory = max(m.memory_percent for m in recent_metrics)
        max_response_time = max(m.avg_response_time for m in recent_metrics)
        
        return {
            'period_hours': hours,
            'averages': {
                'cpu_percent': round(avg_cpu, 2),
                'memory_percent': round(avg_memory, 2),
                'response_time': round(avg_response_time, 3)
            },
            'peaks': {
                'cpu_percent': round(max_cpu, 2),
                'memory_percent': round(max_memory, 2),
                'response_time': round(max_response_time, 3)
            },
            'data_points': len(recent_metrics)
        }
```

## 🔐 പ്രൊഡക്ഷൻ സുരക്ഷാ കോൺഫിഗറേഷൻ

### സുരക്ഷാ ഹാർഡനിംഗ്

```yaml
# k8s/security-policy.yaml - Kubernetes security policies
apiVersion: v1
kind: SecurityContext
metadata:
  name: mcp-retail-security-context
spec:
  runAsNonRoot: true
  runAsUser: 1000
  runAsGroup: 1000
  fsGroup: 1000
  seccompProfile:
    type: RuntimeDefault
  capabilities:
    drop:
      - ALL
  readOnlyRootFilesystem: true
  allowPrivilegeEscalation: false

---
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: mcp-retail-network-policy
  namespace: mcp-retail
spec:
  podSelector:
    matchLabels:
      app: mcp-retail-server
  policyTypes:
    - Ingress
    - Egress
  ingress:
    - from:
        - namespaceSelector:
            matchLabels:
              name: ingress-nginx
      ports:
        - protocol: TCP
          port: 8000
  egress:
    - to:
        - namespaceSelector:
            matchLabels:
              name: database
      ports:
        - protocol: TCP
          port: 5432
    - to: []
      ports:
        - protocol: TCP
          port: 443  # HTTPS for Azure OpenAI
        - protocol: TCP
          port: 53   # DNS
        - protocol: UDP
          port: 53   # DNS
```

### പരിസ്ഥിതി കോൺഫിഗറേഷൻ

```bash
# scripts/setup-production-env.sh
#!/bin/bash

# പ്രൊഡക്ഷൻ പരിസ്ഥിതി സജ്ജീകരണ സ്ക്രിപ്റ്റ്
set -euo pipefail

echo "🔧 Setting up production environment..."

# റിസോഴ്‌സ് ഗ്രൂപ്പുകൾ സൃഷ്ടിക്കുക
az group create --name "mcp-retail-prod-rg" --location "East US"
az group create --name "mcp-retail-shared-rg" --location "East US"

# കീ വാൾട്ട് സൃഷ്ടിക്കുക
echo "🔐 Creating Azure Key Vault..."
az keyvault create \
  --name "mcp-retail-kv-prod" \
  --resource-group "mcp-retail-shared-rg" \
  --location "East US" \
  --enable-rbac-authorization true

# രഹസ്യങ്ങൾ സജ്ജമാക്കുക
echo "🔑 Setting up secrets..."
az keyvault secret set \
  --vault-name "mcp-retail-kv-prod" \
  --name "postgres-password" \
  --value "${POSTGRES_PASSWORD}"

az keyvault secret set \
  --vault-name "mcp-retail-kv-prod" \
  --name "azure-openai-key" \
  --value "${AZURE_OPENAI_KEY}"

# കണ്ടെയ്‌നർ രജിസ്ട്രി സൃഷ്ടിക്കുക
echo "📦 Creating container registry..."
az acr create \
  --name "mcpretailregistry" \
  --resource-group "mcp-retail-shared-rg" \
  --sku Premium \
  --admin-enabled false

# വെർച്വൽ നെറ്റ്‌വർക്ക് സൃഷ്ടിക്കുക
echo "🌐 Creating virtual network..."
az network vnet create \
  --name "mcp-retail-vnet" \
  --resource-group "mcp-retail-shared-rg" \
  --address-prefix "10.0.0.0/16" \
  --subnet-name "container-apps" \
  --subnet-prefix "10.0.1.0/24"

az network vnet subnet create \
  --name "database" \
  --resource-group "mcp-retail-shared-rg" \
  --vnet-name "mcp-retail-vnet" \
  --address-prefix "10.0.2.0/24" \
  --delegations Microsoft.DBforPostgreSQL/flexibleServers

# ഇൻഫ്രാസ്ട്രക്ചർ വിന്യസിക്കുക
echo "🏗️  Deploying infrastructure..."
az deployment group create \
  --resource-group "mcp-retail-prod-rg" \
  --template-file "infra/main.bicep" \
  --parameters "infra/main.parameters.prod.json"

echo "✅ Production environment setup complete!"
```

## 🎯 പ്രധാന പഠനങ്ങൾ

ഈ ലാബ് പൂർത്തിയാക്കിയ ശേഷം, നിങ്ങൾക്കുണ്ടാകണം:

✅ **കണ്ടെയ്‌നർ തന്ത്രം**: സുരക്ഷാ ഹാർഡനിംഗ് ഉള്ള പ്രൊഡക്ഷൻ-സജ്ജ Docker കണ്ടെയ്‌നറുകൾ  
✅ **ക്ലൗഡ് വിന്യാസം**: ഓട്ടോ-സ്കേലിംഗ്, നിരീക്ഷണമുള്ള Azure Container Apps  
✅ **ഡാറ്റാബേസ് വിന്യാസം**: ഉയർന്ന ലഭ്യതയുള്ള PostgreSQL Flexible Server  
✅ **CI/CD പൈപ്പ്ലൈനുകൾ**: ഓട്ടോമേറ്റഡ് ടെസ്റ്റിംഗ്, ബിൽഡിംഗ്, വിന്യാസ വർക്ക്‌ഫ്ലോകൾ  
✅ **പ്രകടന നിരീക്ഷണം**: സമഗ്ര മെട്രിക് ശേഖരണവും അലർട്ടിംഗും  
✅ **സുരക്ഷാ കോൺഫിഗറേഷൻ**: പ്രൊഡക്ഷൻ-ഗ്രേഡ് സുരക്ഷാ നയങ്ങളും നെറ്റ്വർക്ക് ഐസൊലേഷനും  

## 🚀 അടുത്തത് എന്താണ്

**[Lab 11: Monitoring and Observability](../11-Monitoring/README.md)**-നൊപ്പം തുടരുക:

- Application Insights ഉപയോഗിച്ച് സമഗ്ര നിരീക്ഷണം സജ്ജമാക്കുക  
- ഘടനാപരമായ ലോഗിംഗ്, വിതരണ ട്രേസിംഗ് കോൺഫിഗർ ചെയ്യുക  
- അലർട്ടിംഗും ഓട്ടോമേറ്റഡ് പ്രതികരണ സംവിധാനങ്ങളും നടപ്പിലാക്കുക  
- ബിസിനസ് മെട്രിക്കുകളും പ്രകടന KPI-കളും നിരീക്ഷിക്കുക  

## 📚 അധിക സ്രോതസുകൾ

### കണ്ടെയ്‌നർ സാങ്കേതികവിദ്യകൾ
- [Docker Best Practices](https://docs.docker.com/develop/dev-best-practices/) - ഔദ്യോഗിക Docker മികച്ച പ്രാക്ടീസുകൾ  
- [Azure Container Apps](https://docs.microsoft.com/en-us/azure/container-apps/) - Azure Container Apps ഡോക്യുമെന്റേഷൻ  
- [Kubernetes Documentation](https://kubernetes.io/docs/) - Kubernetes ഔദ്യോഗിക ഡോക്യുമെന്റേഷൻ  

### CI/CD & DevOps
- [GitHub Actions](https://docs.github.com/en/actions) - GitHub Actions ഡോക്യുമെന്റേഷൻ  
- [Azure DevOps](https://docs.microsoft.com/en-us/azure/devops/) - Azure DevOps സേവനങ്ങൾ  
- [Infrastructure as Code](https://docs.microsoft.com/en-us/azure/azure-resource-manager/bicep/) - Azure Bicep ഡോക്യുമെന്റേഷൻ  

### സുരക്ഷയും നിരീക്ഷണവും
- [Azure Security Center](https://docs.microsoft.com/en-us/azure/security-center/) - Azure സുരക്ഷാ ശുപാർശകൾ  
- [Container Security](https://kubernetes.io/docs/concepts/security/) - Kubernetes സുരക്ഷാ ആശയങ്ങൾ  
- [Application Insights](https://docs.microsoft.com/en-us/azure/azure-monitor/app/app-insights-overview) - Azure Application Insights  

---

**മുൻപ്**: [Lab 09: VS Code Integration](../09-VS-Code/README.md)  
**അടുത്തത്**: [Lab 11: Monitoring and Observability](../11-Monitoring/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**അസൂയാ**:  
ഈ രേഖ AI വിവർത്തന സേവനം [Co-op Translator](https://github.com/Azure/co-op-translator) ഉപയോഗിച്ച് വിവർത്തനം ചെയ്തതാണ്. നാം കൃത്യതയ്ക്ക് ശ്രമിച്ചെങ്കിലും, സ്വയം പ്രവർത്തിക്കുന്ന വിവർത്തനങ്ങളിൽ പിശകുകൾ അല്ലെങ്കിൽ തെറ്റുകൾ ഉണ്ടാകാമെന്ന് ദയവായി ശ്രദ്ധിക്കുക. അതിന്റെ മാതൃഭാഷയിലുള്ള യഥാർത്ഥ രേഖ പ്രാമാണികമായ ഉറവിടമായി കണക്കാക്കണം. നിർണായക വിവരങ്ങൾക്ക്, പ്രൊഫഷണൽ മനുഷ്യ വിവർത്തനം ശുപാർശ ചെയ്യപ്പെടുന്നു. ഈ വിവർത്തനം ഉപയോഗിക്കുന്നതിൽ നിന്നുണ്ടാകുന്ന ഏതെങ്കിലും തെറ്റിദ്ധാരണകൾക്കോ തെറ്റായ വ്യാഖ്യാനങ്ങൾക്കോ ഞങ്ങൾ ഉത്തരവാദികളല്ല.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->