# 🔧 Módulo 3: Desenvolvimento Avançado MCP com Microsoft Foundry Toolkit

> [!NOTE]
> URLs do Inspector neste laboratório usam o endpoint legado `/sse` e apontam para as dependências fixadas do MCP SDK `1.9.3` e Inspector `0.14.0`. Eles não são exemplos atuais do Streamable HTTP `2026-07-28`.
> 
> 

![Duration](https://img.shields.io/badge/Duration-20_minutes-blue?style=flat-square)
![Microsoft Foundry Toolkit](https://img.shields.io/badge/Microsoft_Foundry_Toolkit-Required-orange?style=flat-square)
![Python](https://img.shields.io/badge/Python-3.10+-green?style=flat-square)
![MCP SDK](https://img.shields.io/badge/MCP_SDK-1.9.3-purple?style=flat-square)
![Inspector](https://img.shields.io/badge/MCP_Inspector-0.14.0-blue?style=flat-square)

## 🎯 Objetivos de Aprendizagem

Ao final deste laboratório, você será capaz de:

- ✅ Criar servidores MCP personalizados usando o Microsoft Foundry Toolkit
- ✅ Configurar e usar o SDK MCP Python mais recente (v1.9.3)
- ✅ Configurar e utilizar o MCP Inspector para depuração
- ✅ Depurar servidores MCP tanto no ambiente Agent Builder quanto no Inspector
- ✅ Compreender fluxos de trabalho avançados de desenvolvimento de servidores MCP

## 📋 Pré-requisitos

- Conclusão do Laboratório 2 (Fundamentos MCP)
- VS Code com a extensão Microsoft Foundry Toolkit instalada
- Ambiente Python 3.10+
- Node.js e npm para configuração do Inspector

## 🏗️ O Que Você Vai Construir

Neste laboratório, você criará um **Servidor Weather MCP** que demonstra:
- Implementação personalizada do servidor MCP
- Integração com o Agent Builder do Microsoft Foundry Toolkit
- Fluxos de trabalho profissionais de depuração
- Padrões modernos de uso do SDK MCP

---

## 🔧 Visão Geral dos Componentes Centrais

### 🐍 SDK MCP Python
O Model Context Protocol Python SDK fornece a base para construir servidores MCP personalizados. Você usará a versão 1.9.3 com capacidades aprimoradas de depuração.

### 🔍 MCP Inspector
Uma ferramenta poderosa de depuração que oferece:
- Monitoramento em tempo real do servidor
- Visualização da execução de ferramentas
- Inspeção de requisições/respostas de rede
- Ambiente interativo de testes

---

## 📖 Implementação Passo a Passo

### Passo 1: Crie um WeatherAgent no Agent Builder

1. **Abra o Agent Builder** no VS Code através da extensão Microsoft Foundry Toolkit
2. **Crie um novo agente** com a seguinte configuração:
   - Nome do agente: `WeatherAgent`

![Agent Creation](../../../../translated_images/pt-BR/Agent.c9c33f6a412b4cde.webp)

### Passo 2: Inicialize o Projeto do Servidor MCP

1. **Navegue até Ferramentas** → **Adicionar Ferramenta** no Agent Builder
2. **Selecione "Servidor MCP"** entre as opções disponíveis
3. **Escolha "Criar um novo Servidor MCP"**
4. **Selecione o template `python-weather`**
5. **Nomeie seu servidor:** `weather_mcp`

![Python Template Selection](../../../../translated_images/pt-BR/Pythontemplate.9d0a2913c6491500.webp)

### Passo 3: Abra e Examine o Projeto

1. **Abra o projeto gerado** no VS Code
2. **Revise a estrutura do projeto:**
   ```
   weather_mcp/
   ├── src/
   │   ├── __init__.py
   │   └── server.py
   ├── inspector/
   │   ├── package.json
   │   └── package-lock.json
   ├── .vscode/
   │   ├── launch.json
   │   └── tasks.json
   ├── pyproject.toml
   └── README.md
   ```

### Passo 4: Atualize para o SDK MCP Mais Recente

> **🔍 Por que atualizar?** Queremos usar o SDK MCP mais recente (v1.9.3) e o serviço Inspector (0.14.0) para recursos aprimorados e melhores capacidades de depuração.

#### 4a. Atualize as Dependências Python

**Edite `pyproject.toml`:** atualize [./code/weather_mcp/pyproject.toml](../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/pyproject.toml)


#### 4b. Atualize a Configuração do Inspector

**Edite `inspector/package.json`:** atualize [./code/weather_mcp/inspector/package.json](../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/inspector/package.json)

#### 4c. Atualize as Dependências do Inspector

**Edite `inspector/package-lock.json`:** atualize [./code/weather_mcp/inspector/package-lock.json](../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/inspector/package-lock.json)

> **📝 Nota:** Este arquivo contém definições extensas de dependências. Abaixo está a estrutura essencial — o conteúdo completo garante a resolução adequada das dependências.


> **⚡ Package Lock Completo:** O arquivo package-lock.json completo contém cerca de 3000 linhas de definições de dependência. O acima mostra a estrutura-chave — use o arquivo fornecido para resolução completa das dependências.

### Passo 5: Configure a Depuração no VS Code

*Nota: Por favor, copie o arquivo no caminho especificado para substituir o arquivo local correspondente*

#### 5a. Atualize a Configuração de Lançamento

**Edite `.vscode/launch.json`:**

```json
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "Attach to Local MCP",
      "type": "debugpy",
      "request": "attach",
      "connect": {
        "host": "localhost",
        "port": 5678
      },
      "presentation": {
        "hidden": true
      },
      "internalConsoleOptions": "neverOpen",
      "postDebugTask": "Terminate All Tasks"
    },
    {
      "name": "Launch Inspector (Edge)",
      "type": "msedge",
      "request": "launch",
      "url": "http://localhost:6274?timeout=60000&serverUrl=http://localhost:3001/sse#tools",
      "cascadeTerminateToConfigurations": [
        "Attach to Local MCP"
      ],
      "presentation": {
        "hidden": true
      },
      "internalConsoleOptions": "neverOpen"
    },
    {
      "name": "Launch Inspector (Chrome)",
      "type": "chrome",
      "request": "launch",
      "url": "http://localhost:6274?timeout=60000&serverUrl=http://localhost:3001/sse#tools",
      "cascadeTerminateToConfigurations": [
        "Attach to Local MCP"
      ],
      "presentation": {
        "hidden": true
      },
      "internalConsoleOptions": "neverOpen"
    }
  ],
  "compounds": [
    {
      "name": "Debug in Agent Builder",
      "configurations": [
        "Attach to Local MCP"
      ],
      "preLaunchTask": "Open Agent Builder",
    },
    {
      "name": "Debug in Inspector (Edge)",
      "configurations": [
        "Launch Inspector (Edge)",
        "Attach to Local MCP"
      ],
      "preLaunchTask": "Start MCP Inspector",
      "stopAll": true
    },
    {
      "name": "Debug in Inspector (Chrome)",
      "configurations": [
        "Launch Inspector (Chrome)",
        "Attach to Local MCP"
      ],
      "preLaunchTask": "Start MCP Inspector",
      "stopAll": true
    }
  ]
}
```

**Edite `.vscode/tasks.json`:**

```
{
  "version": "2.0.0",
  "tasks": [
    {
      "label": "Start MCP Server",
      "type": "shell",
      "command": "python -m debugpy --listen 127.0.0.1:5678 src/__init__.py sse",
      "isBackground": true,
      "options": {
        "cwd": "${workspaceFolder}",
        "env": {
          "PORT": "3001"
        }
      },
      "problemMatcher": {
        "pattern": [
          {
            "regexp": "^.*$",
            "file": 0,
            "location": 1,
            "message": 2
          }
        ],
        "background": {
          "activeOnStart": true,
          "beginsPattern": ".*",
          "endsPattern": "Application startup complete|running"
        }
      }
    },
    {
      "label": "Start MCP Inspector",
      "type": "shell",
      "command": "npm run dev:inspector",
      "isBackground": true,
      "options": {
        "cwd": "${workspaceFolder}/inspector",
        "env": {
          "CLIENT_PORT": "6274",
          "SERVER_PORT": "6277",
        }
      },
      "problemMatcher": {
        "pattern": [
          {
            "regexp": "^.*$",
            "file": 0,
            "location": 1,
            "message": 2
          }
        ],
        "background": {
          "activeOnStart": true,
          "beginsPattern": "Starting MCP inspector",
          "endsPattern": "Proxy server listening on port"
        }
      },
      "dependsOn": [
        "Start MCP Server"
      ]
    },
    {
      "label": "Open Agent Builder",
      "type": "shell",
      "command": "echo ${input:openAgentBuilder}",
      "presentation": {
        "reveal": "never"
      },
      "dependsOn": [
        "Start MCP Server"
      ],
    },
    {
      "label": "Terminate All Tasks",
      "command": "echo ${input:terminate}",
      "type": "shell",
      "problemMatcher": []
    }
  ],
  "inputs": [
    {
      "id": "openAgentBuilder",
      "type": "command",
      "command": "ai-mlstudio.agentBuilder",
      "args": {
        "initialMCPs": [ "local-server-weather_mcp" ],
        "triggeredFrom": "vsc-tasks"
      }
    },
    {
      "id": "terminate",
      "type": "command",
      "command": "workbench.action.tasks.terminate",
      "args": "terminateAll"
    }
  ]
}
```


---

## 🚀 Executando e Testando Seu Servidor MCP

### Passo 6: Instale as Dependências

Após fazer as alterações na configuração, execute os seguintes comandos:

**Instale as dependências Python:**
```bash
uv sync
```

**Instale as dependências do Inspector:**
```bash
cd inspector
npm install
```

### Passo 7: Depure com Agent Builder

1. **Pressione F5** ou use a configuração **"Depurar no Agent Builder"**
2. **Selecione a configuração composta** no painel de depuração
3. **Aguarde o início do servidor** e a abertura do Agent Builder
4. **Teste seu servidor Weather MCP** com consultas em linguagem natural

Exemplo de prompt de entrada assim

SYSTEM_PROMPT

```
You are my weather assistant
```

USER_PROMPT

```
How's the weather like in Seattle
```

![Agent Builder Debug Result](../../../../translated_images/pt-BR/Result.6ac570f7d2b1d538.webp)

### Passo 8: Depure com MCP Inspector

1. **Use a configuração "Depurar no Inspector"** (Edge ou Chrome)
2. **Abra a interface do Inspector** em `http://localhost:6274`
3. **Explore o ambiente interativo de testes:**
   - Visualize ferramentas disponíveis
   - Teste a execução das ferramentas
   - Monitore requisições de rede
   - Depure respostas do servidor

![MCP Inspector Interface](../../../../translated_images/pt-BR/Inspector.5672415cd02fe873.webp)

---

## 🎯 Resultados Chave do Aprendizado

Ao completar este laboratório, você:

- [x] **Criou um servidor MCP personalizado** usando os templates Microsoft Foundry Toolkit
- [x] **Atualizou para o SDK MCP mais recente** (v1.9.3) para funcionalidade aprimorada
- [x] **Configurou fluxos de trabalho profissionais de depuração** tanto para Agent Builder quanto para Inspector
- [x] **Configurou o MCP Inspector** para testes interativos do servidor
- [x] **Dominou as configurações de depuração do VS Code** para desenvolvimento MCP

## 🔧 Recursos Avançados Explorados

| Recurso | Descrição | Caso de Uso |
|---------|-------------|----------|
| **SDK MCP Python v1.9.3** | Implementação mais recente do protocolo | Desenvolvimento moderno de servidores |
| **MCP Inspector 0.14.0** | Ferramenta interativa de depuração | Testes em tempo real do servidor |
| **Depuração VS Code** | Ambiente integrado de desenvolvimento | Fluxo de trabalho profissional de depuração |
| **Integração Agent Builder** | Conexão direta com Microsoft Foundry Toolkit | Testes de agentes ponta a ponta |

## 📚 Recursos Adicionais

- [Documentação MCP Python SDK](https://modelcontextprotocol.io/docs/sdk/python)
- [Guia da Extensão Microsoft Foundry Toolkit](https://code.visualstudio.com/docs/ai/ai-toolkit)
- [Documentação de Depuração VS Code](https://code.visualstudio.com/docs/editor/debugging)
- [Especificação do Model Context Protocol](https://modelcontextprotocol.io/docs/concepts/architecture)

---

**🎉 Parabéns!** Você completou com sucesso o Laboratório 3 e agora pode criar, depurar e implantar servidores MCP personalizados usando fluxos de trabalho profissionais de desenvolvimento.

### 🔜 Continue para o Próximo Módulo

Pronto para aplicar suas habilidades MCP a um fluxo de trabalho real de desenvolvimento? Continue para **[Módulo 4: Desenvolvimento Prático MCP - Servidor Customizado de Clone GitHub](../lab4/README.md)** onde você irá:
- Construir um servidor MCP pronto para produção que automatiza operações de repositórios GitHub
- Implementar funcionalidade de clonagem de repositórios GitHub via MCP
- Integrar servidores MCP personalizados com VS Code e GitHub Copilot Agent Mode
- Testar e implantar servidores MCP personalizados em ambientes de produção
- Aprender automação de fluxo de trabalho prática para desenvolvedores

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido usando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, por favor, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->