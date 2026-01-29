# ನಿಯೋಜನೆ ತಂತ್ರಗಳು

## 🎯 ಈ ಪ್ರಯೋಗಶಾಲೆ ಏನು ಒಳಗೊಂಡಿದೆ

ಈ ಪ್ರಯೋಗಶಾಲೆ ನಿಮ್ಮ MCP ರೀಟೇಲ್ ಸರ್ವರ್ ಅನ್ನು ಆಧುನಿಕ ಕಂಟೈನರೈಜೆಷನ್ ಮತ್ತು ಕ್ಲೌಡ್-ನೆಟಿವ್ ವಿಧಾನಗಳನ್ನು ಬಳಸಿ ಉತ್ಪಾದನಾ ಪರಿಸರಗಳಿಗೆ ನಿಯೋಜಿಸುವ ಬಗ್ಗೆ ಸಮಗ್ರ ಮಾರ್ಗದರ್ಶನವನ್ನು ಒದಗಿಸುತ್ತದೆ. ನೀವು ಎಂಟರ್‌ಪ್ರೈಸ್ ಕೆಲಸದ ಭಾರವನ್ನು ನಿರ್ವಹಿಸಬಹುದಾದ, ವಿಸ್ತರಿಸಬಹುದಾದ, ಸುರಕ್ಷಿತ ಮತ್ತು ಮೇಲ್ವಿಚಾರಣೆಯ MCP ಸರ್ವರ್‌ಗಳನ್ನು ನಿಯೋಜಿಸುವುದನ್ನು ಕಲಿಯುತ್ತೀರಿ.

## ಅವಲೋಕನ

MCP ಸರ್ವರ್‌ಗಳ ಉತ್ಪಾದನಾ ನಿಯೋಜನೆಗೆ ಕಂಟೈನರೈಜೆಷನ್, ಸಂಯೋಜನೆ, ಸುರಕ್ಷತೆ, ವಿಸ್ತರಣೆ ಮತ್ತು ಮೇಲ್ವಿಚಾರಣೆಯ ಬಗ್ಗೆ ಜಾಗರೂಕತೆಯ ಅಗತ್ಯವಿದೆ. ಈ ಪ್ರಯೋಗಶಾಲೆ PostgreSQL ಫ್ಲೆಕ್ಸಿಬಲ್ ಸರ್ವರ್ ಜೊತೆಗೆ Azure Container Apps ಗೆ ನಿಯೋಜಿಸುವುದು, CI/CD ಪೈಪ್ಲೈನ್ಗಳನ್ನು ಅನುಷ್ಠಾನಗೊಳಿಸುವುದು ಮತ್ತು ಬದಲಾಗುವ ಕೆಲಸದ ಭಾರಗಳಿಗೆ ಸ್ವಯಂಚಾಲಿತ ವಿಸ್ತರಣೆಯನ್ನು ಸಂರಚಿಸುವುದನ್ನು ಒಳಗೊಂಡಿದೆ.

ನಿಯೋಜನೆ ತಂತ್ರಗಳು ಅಭಿವೃದ್ಧಿಗಾಗಿ ಸರಳ ಏಕ-ಕಂಟೈನರ್ ನಿಯೋಜನೆಗಳಿಂದ ಆರಂಭಿಸಿ, ಸಮಗ್ರ ಮೇಲ್ವಿಚಾರಣೆ ಮತ್ತು ಸುರಕ್ಷತಾ ವೈಶಿಷ್ಟ್ಯಗಳೊಂದಿಗೆ ಬಹು-ಪ್ರದೇಶ, ಸ್ವಯಂಚಾಲಿತ ವಿಸ್ತರಣೆಯ ಉತ್ಪಾದನಾ ಪರಿಸರಗಳವರೆಗೆ ವ್ಯಾಪಿಸಿದೆ.

## ಕಲಿಕೆಯ ಉದ್ದೇಶಗಳು

ಈ ಪ್ರಯೋಗಶಾಲೆಯ ಅಂತ್ಯಕ್ಕೆ, ನೀವು ಸಾಧ್ಯವಾಗುತ್ತದೆ:

- **ಡಾಕರ್** ಬಳಸಿ MCP ಸರ್ವರ್‌ಗಳನ್ನು ಬಹು-ಹಂತ ನಿರ್ಮಾಣಗಳೊಂದಿಗೆ ಕಂಟೈನರೈಸ್ ಮಾಡುವುದು  
- **Azure Container Apps** ಗೆ ಸುರಕ್ಷಿತ ನೆಟ್ವರ್ಕಿಂಗ್ ಜೊತೆಗೆ ನಿಯೋಜಿಸುವುದು  
- **ಉತ್ಪಾದನಾ ಮಟ್ಟದ PostgreSQL** ಅನ್ನು ಹೆಚ್ಚಿನ ಲಭ್ಯತೆಯೊಂದಿಗೆ ಸಂರಚಿಸುವುದು  
- **ಸ್ವಯಂಚಾಲಿತ ನಿಯೋಜನೆಗಾಗಿ CI/CD ಪೈಪ್ಲೈನ್ಗಳನ್ನು** ಅನುಷ್ಠಾನಗೊಳಿಸುವುದು  
- **ಬೇಡಿಕೆಯ ಆಧಾರದ ಮೇಲೆ ಅಪ್ಲಿಕೇಶನ್‌ಗಳನ್ನು ಸ್ವಯಂಚಾಲಿತವಾಗಿ ವಿಸ್ತರಿಸುವುದು**  
- **ಉತ್ಪಾದನಾ ನಿಯೋಜನೆಗಳನ್ನು ಸಮಗ್ರ ಮೇಲ್ವಿಚಾರಣೆಯೊಂದಿಗೆ** ಮೇಲ್ವಿಚಾರಿಸುವುದು  

## 🐳 ಡಾಕರ್ ಕಂಟೈನರೈಜೆಷನ್

### ಬಹು-ಹಂತ ಡಾಕರ್‌ಫೈಲ್

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

### ಅಭಿವೃದ್ಧಿಗಾಗಿ ಡಾಕರ್ ಕಾಂಪೋಸ್

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

### ಉತ್ಪಾದನಾ ಡಾಕರ್ ಕಾಂಪೋಸ್

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

## ☁️ Azure Container Apps ನಿಯೋಜನೆ

### Bicep ಬಳಸಿ ಇನ್ಫ್ರಾಸ್ಟ್ರಕ್ಚರ್ ಅಸ್ ಕೋಡ್

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

### PostgreSQL ಫ್ಲೆಕ್ಸಿಬಲ್ ಸರ್ವರ್

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

## 🚀 CI/CD ಪೈಪ್ಲೈನ್ ಸಂರಚನೆ

### GitHub Actions ವರ್ಕ್‌ಫ್ಲೋ

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

### Azure DevOps ಪೈಪ್ಲೈನ್

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

## 📊 ವಿಸ್ತರಣೆ ಮತ್ತು ಕಾರ್ಯಕ್ಷಮತೆ

### ಸ್ವಯಂಚಾಲಿತ ವಿಸ್ತರಣೆ ಸಂರಚನೆ

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

### ಕಾರ್ಯಕ್ಷಮತೆ ಮೇಲ್ವಿಚಾರಣೆ

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
        
        # ಮೆಟ್ರಿಕ್ಸ್ ಸಂಗ್ರಹಣೆ
        self.metrics_history = []
        self.request_times = []
        self.error_count = 0
        self.request_count = 0
        
        # ಡೇಟಾಬೇಸ್ ಮೇಲ್ವಿಚಾರಣೆ
        self.db_pool = None
        
    async def start_monitoring(self):
        """Start continuous performance monitoring."""
        
        self.logger.info("Starting performance monitoring")
        
        # ಮೆಟ್ರಿಕ್ಸ್ ಸಂಗ್ರಹಣೆ ಕಾರ್ಯವನ್ನು ಪ್ರಾರಂಭಿಸಿ
        asyncio.create_task(self._collect_metrics_loop())
        asyncio.create_task(self._cleanup_old_metrics())
        
    async def _collect_metrics_loop(self):
        """Continuously collect performance metrics."""
        
        while True:
            try:
                metrics = await self._collect_current_metrics()
                self.metrics_history.append(metrics)
                
                # ಗಂಭೀರ ಮೆಟ್ರಿಕ್ಸ್ ಲಾಗ್ ಮಾಡಿ
                if metrics.cpu_percent > 90:
                    self.logger.warning(f"High CPU usage: {metrics.cpu_percent:.1f}%")
                
                if metrics.memory_percent > 90:
                    self.logger.warning(f"High memory usage: {metrics.memory_percent:.1f}%")
                
                if metrics.error_rate > 0.05:  # 5% ದೋಷ ದರ
                    self.logger.warning(f"High error rate: {metrics.error_rate:.2%}")
                
                await asyncio.sleep(30)  # ಪ್ರತಿ 30 ಸೆಕೆಂಡುಗಳಿಗೆ ಸಂಗ್ರಹಿಸಿ
                
            except Exception as e:
                self.logger.error(f"Error collecting metrics: {e}")
                await asyncio.sleep(60)
    
    async def _collect_current_metrics(self) -> PerformanceMetrics:
        """Collect current system metrics."""
        
        # ವ್ಯವಸ್ಥೆ ಮೆಟ್ರಿಕ್ಸ್
        cpu_percent = psutil.cpu_percent(interval=1)
        memory = psutil.virtual_memory()
        
        # ಅಪ್ಲಿಕೇಶನ್ ಮೆಟ್ರಿಕ್ಸ್
        current_time = datetime.utcnow()
        recent_requests = [
            req_time for req_time in self.request_times
            if current_time - req_time < timedelta(minutes=1)
        ]
        
        request_rate = len(recent_requests) / 60.0  # ಪ್ರತಿ ಸೆಕೆಂಡಿಗೆ ವಿನಂತಿಗಳು
        
        # ಸರಾಸರಿ ಪ್ರತಿಕ್ರಿಯೆ ಸಮಯವನ್ನು ಲೆಕ್ಕಿಸಿ
        avg_response_time = 0.0
        if hasattr(self, '_recent_response_times'):
            recent_response_times = [
                rt for rt in self._recent_response_times
                if current_time - rt['timestamp'] < timedelta(minutes=5)
            ]
            if recent_response_times:
                avg_response_time = sum(rt['time'] for rt in recent_response_times) / len(recent_response_times)
        
        # ದೋಷ ದರ ಲೆಕ್ಕಾಚಾರ
        error_rate = 0.0
        if self.request_count > 0:
            error_rate = self.error_count / self.request_count
        
        # ಡೇಟಾಬೇಸ್ ಸಂಪರ್ಕಗಳು
        db_connections = 0
        if self.db_pool:
            db_connections = len(self.db_pool._holders)
        
        return PerformanceMetrics(
            timestamp=current_time,
            cpu_percent=cpu_percent,
            memory_percent=memory.percent,
            memory_used_mb=memory.used / (1024 * 1024),
            active_connections=0,  # ಸಂಪರ್ಕ ಟ್ರ್ಯಾಕಿಂಗ್ ಜೊತೆಗೆ ಅನುಷ್ಠಾನಗೊಳಿಸಲಾಗುವುದು
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
                
                # ಮೆಟ್ರಿಕ್ಸ್ ಇತಿಹಾಸವನ್ನು ಸ್ವಚ್ಛಗೊಳಿಸಿ
                self.metrics_history = [
                    m for m in self.metrics_history
                    if m.timestamp > cutoff_time
                ]
                
                # ವಿನಂತಿ ಸಮಯಗಳನ್ನು ಸ್ವಚ್ಛಗೊಳಿಸಿ
                self.request_times = [
                    rt for rt in self.request_times
                    if rt > cutoff_time
                ]
                
                # ನಿಯಮಿತವಾಗಿ ಕೌಂಟರ್‌ಗಳನ್ನು ಮರುಹೊಂದಿಸಿ
                if datetime.utcnow().minute == 0:  # ಪ್ರತಿ ಗಂಟೆಗೆ
                    self.error_count = 0
                    self.request_count = 0
                
                await asyncio.sleep(3600)  # ಪ್ರತಿ ಗಂಟೆಗೆ ಚಾಲನೆ ಮಾಡಿ
                
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
        
        # ಪ್ರತಿಕ್ರಿಯೆ ಸಮಯವನ್ನು ದಾಖಲಿಸಿ
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
        
        # ಸರಾಸರಿಗಳನ್ನು ಲೆಕ್ಕಿಸಿ
        avg_cpu = sum(m.cpu_percent for m in recent_metrics) / len(recent_metrics)
        avg_memory = sum(m.memory_percent for m in recent_metrics) / len(recent_metrics)
        avg_response_time = sum(m.avg_response_time for m in recent_metrics) / len(recent_metrics)
        
        # ಶಿಖರಗಳನ್ನು ಲೆಕ್ಕಿಸಿ
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

## 🔐 ಉತ್ಪಾದನಾ ಸುರಕ್ಷತಾ ಸಂರಚನೆ

### ಸುರಕ್ಷತಾ ಬಲಪಡಿಸುವಿಕೆ

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

### ಪರಿಸರ ಸಂರಚನೆ

```bash
# scripts/setup-production-env.sh
#!/bin/bash

# ಉತ್ಪಾದನಾ ಪರಿಸರ ಸೆಟಪ್ ಸ್ಕ್ರಿಪ್ಟ್
set -euo pipefail

echo "🔧 Setting up production environment..."

# ಸಂಪನ್ಮೂಲ ಗುಂಪುಗಳನ್ನು ರಚಿಸಿ
az group create --name "mcp-retail-prod-rg" --location "East US"
az group create --name "mcp-retail-shared-rg" --location "East US"

# ಕೀ ವಾಲ್ಟ್ ರಚಿಸಿ
echo "🔐 Creating Azure Key Vault..."
az keyvault create \
  --name "mcp-retail-kv-prod" \
  --resource-group "mcp-retail-shared-rg" \
  --location "East US" \
  --enable-rbac-authorization true

# ರಹಸ್ಯಗಳನ್ನು ಸೆಟ್ ಮಾಡಿ
echo "🔑 Setting up secrets..."
az keyvault secret set \
  --vault-name "mcp-retail-kv-prod" \
  --name "postgres-password" \
  --value "${POSTGRES_PASSWORD}"

az keyvault secret set \
  --vault-name "mcp-retail-kv-prod" \
  --name "azure-openai-key" \
  --value "${AZURE_OPENAI_KEY}"

# ಕಂಟೈನರ್ ರಿಜಿಸ್ಟ್ರಿಯನ್ನು ರಚಿಸಿ
echo "📦 Creating container registry..."
az acr create \
  --name "mcpretailregistry" \
  --resource-group "mcp-retail-shared-rg" \
  --sku Premium \
  --admin-enabled false

# ವರ್ಚುವಲ್ ನೆಟ್‌ವರ್ಕ್ ರಚಿಸಿ
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

# ಮೂಲಸೌಕರ್ಯವನ್ನು ನಿಯೋಜಿಸಿ
echo "🏗️  Deploying infrastructure..."
az deployment group create \
  --resource-group "mcp-retail-prod-rg" \
  --template-file "infra/main.bicep" \
  --parameters "infra/main.parameters.prod.json"

echo "✅ Production environment setup complete!"
```

## 🎯 ಪ್ರಮುಖ ಅಂಶಗಳು

ಈ ಪ್ರಯೋಗಶಾಲೆಯನ್ನು ಪೂರ್ಣಗೊಳಿಸಿದ ನಂತರ, ನೀವು ಹೊಂದಿರಬೇಕು:

✅ **ಕಂಟೈನರ್ ತಂತ್ರಜ್ಞಾನ**: ಸುರಕ್ಷತಾ ಬಲಪಡಿಸುವಿಕೆಯಿಂದ ಉತ್ಪಾದನಾ-ಸಿದ್ಧ ಡಾಕರ್ ಕಂಟೈನರ್‌ಗಳು  
✅ **ಕ್ಲೌಡ್ ನಿಯೋಜನೆ**: ಸ್ವಯಂಚಾಲಿತ ವಿಸ್ತರಣೆ ಮತ್ತು ಮೇಲ್ವಿಚಾರಣೆಯೊಂದಿಗೆ Azure Container Apps  
✅ **ಡೇಟಾಬೇಸ್ ನಿಯೋಜನೆ**: ಹೆಚ್ಚಿನ ಲಭ್ಯತೆಯೊಂದಿಗೆ PostgreSQL ಫ್ಲೆಕ್ಸಿಬಲ್ ಸರ್ವರ್  
✅ **CI/CD ಪೈಪ್ಲೈನ್ಗಳು**: ಸ್ವಯಂಚಾಲಿತ ಪರೀಕ್ಷೆ, ನಿರ್ಮಾಣ ಮತ್ತು ನಿಯೋಜನೆ ವರ್ಕ್‌ಫ್ಲೋಗಳು  
✅ **ಕಾರ್ಯಕ್ಷಮತೆ ಮೇಲ್ವಿಚಾರಣೆ**: ಸಮಗ್ರ ಮೆಟ್ರಿಕ್ಸ್ ಸಂಗ್ರಹಣೆ ಮತ್ತು ಎಚ್ಚರಿಕೆ  
✅ **ಸುರಕ್ಷತಾ ಸಂರಚನೆ**: ಉತ್ಪಾದನಾ-ಮಟ್ಟದ ಸುರಕ್ಷತಾ ನೀತಿಗಳು ಮತ್ತು ನೆಟ್ವರ್ಕ್ ವಿಭಜನೆ  

## 🚀 ಮುಂದೇನು

**[Lab 11: Monitoring and Observability](../11-Monitoring/README.md)** ಜೊತೆಗೆ ಮುಂದುವರಿಯಿರಿ:

- ಅಪ್ಲಿಕೇಶನ್ ಇನ್ಸೈಟ್ಸ್ ಬಳಸಿ ಸಮಗ್ರ ಮೇಲ್ವಿಚಾರಣೆಯನ್ನು ಸ್ಥಾಪಿಸುವುದು  
- ರಚನಾತ್ಮಕ ಲಾಗಿಂಗ್ ಮತ್ತು ವಿತರಿತ ಟ್ರೇಸಿಂಗ್ ಅನ್ನು ಸಂರಚಿಸುವುದು  
- ಎಚ್ಚರಿಕೆ ಮತ್ತು ಸ್ವಯಂಚಾಲಿತ ಪ್ರತಿಕ್ರಿಯೆ ವ್ಯವಸ್ಥೆಗಳನ್ನು ಅನುಷ್ಠಾನಗೊಳಿಸುವುದು  
- ವ್ಯವಹಾರ ಮೆಟ್ರಿಕ್ಸ್ ಮತ್ತು ಕಾರ್ಯಕ್ಷಮತೆ KPIs ಗಳನ್ನು ಮೇಲ್ವಿಚಾರಿಸುವುದು  

## 📚 ಹೆಚ್ಚುವರಿ ಸಂಪನ್ಮೂಲಗಳು

### ಕಂಟೈನರ್ ತಂತ್ರಜ್ಞಾನಗಳು
- [Docker Best Practices](https://docs.docker.com/develop/dev-best-practices/) - ಅಧಿಕೃತ ಡಾಕರ್ ಉತ್ತಮ ಅಭ್ಯಾಸಗಳು  
- [Azure Container Apps](https://docs.microsoft.com/en-us/azure/container-apps/) - Azure Container Apps ಡಾಕ್ಯುಮೆಂಟೇಶನ್  
- [Kubernetes Documentation](https://kubernetes.io/docs/) - Kubernetes ಅಧಿಕೃತ ಡಾಕ್ಯುಮೆಂಟೇಶನ್  

### CI/CD ಮತ್ತು ಡೆವ್ಓಪ್ಸ್
- [GitHub Actions](https://docs.github.com/en/actions) - GitHub Actions ಡಾಕ್ಯುಮೆಂಟೇಶನ್  
- [Azure DevOps](https://docs.microsoft.com/en-us/azure/devops/) - Azure DevOps ಸೇವೆಗಳು  
- [Infrastructure as Code](https://docs.microsoft.com/en-us/azure/azure-resource-manager/bicep/) - Azure Bicep ಡಾಕ್ಯುಮೆಂಟೇಶನ್  

### ಸುರಕ್ಷತೆ ಮತ್ತು ಮೇಲ್ವಿಚಾರಣೆ
- [Azure Security Center](https://docs.microsoft.com/en-us/azure/security-center/) - Azure ಸುರಕ್ಷತಾ ಶಿಫಾರಸುಗಳು  
- [Container Security](https://kubernetes.io/docs/concepts/security/) - Kubernetes ಸುರಕ್ಷತಾ ತತ್ವಗಳು  
- [Application Insights](https://docs.microsoft.com/en-us/azure/azure-monitor/app/app-insights-overview) - Azure ಅಪ್ಲಿಕೇಶನ್ ಇನ್ಸೈಟ್ಸ್  

---

**ಹಿಂದಿನ**: [Lab 09: VS Code Integration](../09-VS-Code/README.md)  
**ಮುಂದಿನ**: [Lab 11: Monitoring and Observability](../11-Monitoring/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ಅಸ್ವೀಕರಣ**:  
ಈ ದಸ್ತಾವೇಜು [Co-op Translator](https://github.com/Azure/co-op-translator) ಎಂಬ AI ಅನುವಾದ ಸೇವೆಯನ್ನು ಬಳಸಿ ಅನುವಾದಿಸಲಾಗಿದೆ. ನಾವು ಶುದ್ಧತೆಯತ್ತ ಪ್ರಯತ್ನಿಸುತ್ತಿದ್ದರೂ, ಸ್ವಯಂಚಾಲಿತ ಅನುವಾದಗಳಲ್ಲಿ ತಪ್ಪುಗಳು ಅಥವಾ ಅಸತ್ಯತೆಗಳು ಇರಬಹುದು ಎಂದು ದಯವಿಟ್ಟು ಗಮನಿಸಿ. ಮೂಲ ಭಾಷೆಯಲ್ಲಿರುವ ಮೂಲ ದಸ್ತಾವೇಜನ್ನು ಅಧಿಕೃತ ಮೂಲವೆಂದು ಪರಿಗಣಿಸಬೇಕು. ಮಹತ್ವದ ಮಾಹಿತಿಗಾಗಿ, ವೃತ್ತಿಪರ ಮಾನವ ಅನುವಾದವನ್ನು ಶಿಫಾರಸು ಮಾಡಲಾಗುತ್ತದೆ. ಈ ಅನುವಾದ ಬಳಕೆಯಿಂದ ಉಂಟಾಗುವ ಯಾವುದೇ ತಪ್ಪು ಅರ್ಥಮಾಡಿಕೊಳ್ಳುವಿಕೆ ಅಥವಾ ತಪ್ಪು ವಿವರಣೆಗಳಿಗೆ ನಾವು ಹೊಣೆಗಾರರಾಗುವುದಿಲ್ಲ.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->