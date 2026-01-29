# 🔧 Módulo 3: Desenvolvimento Avançado de MCP com AI Toolkit

![Duration](https://img.shields.io/badge/Duration-20_minutes-blue?style=flat-square)
![AI Toolkit](https://img.shields.io/badge/AI_Toolkit-Required-orange?style=flat-square)
![Python](https://img.shields.io/badge/Python-3.10+-green?style=flat-square)
![MCP SDK](https://img.shields.io/badge/MCP_SDK-1.9.3-purple?style=flat-square)
![Inspector](https://img.shields.io/badge/MCP_Inspector-0.14.0-blue?style=flat-square)

## 🎯 Objetivos de Aprendizagem

No final deste laboratório, serás capaz de:

- ✅ Criar servidores MCP personalizados usando o AI Toolkit
- ✅ Configurar e usar o mais recente MCP Python SDK (v1.9.3)
- ✅ Configurar e utilizar o MCP Inspector para depuração
- ✅ Depurar servidores MCP tanto no Agent Builder como no Inspector
- ✅ Compreender fluxos de trabalho avançados de desenvolvimento de servidores MCP

## 📋 Pré-requisitos

- Conclusão do Laboratório 2 (Fundamentos MCP)
- VS Code com a extensão AI Toolkit instalada
- Ambiente Python 3.10+
- Node.js e npm para configuração do Inspector

## 🏗️ O que vais construir

Neste laboratório, vais criar um **Servidor MCP de Meteorologia** que demonstra:
- Implementação personalizada de servidor MCP
- Integração com o AI Toolkit Agent Builder
- Fluxos de trabalho profissionais de depuração
- Padrões modernos de uso do MCP SDK

---

## 🔧 Visão Geral dos Componentes Principais

### 🐍 MCP Python SDK  
O Model Context Protocol Python SDK fornece a base para construir servidores MCP personalizados. Vais usar a versão 1.9.3 com capacidades de depuração melhoradas.

### 🔍 MCP Inspector  
Uma ferramenta poderosa de depuração que oferece:
- Monitorização do servidor em tempo real
- Visualização da execução de ferramentas
- Inspeção de pedidos/respostas de rede
- Ambiente interativo de testes

---

## 📖 Implementação Passo a Passo

### Passo 1: Criar um WeatherAgent no Agent Builder

1. **Abre o Agent Builder** no VS Code através da extensão AI Toolkit  
2. **Cria um novo agente** com a seguinte configuração:  
   - Nome do Agente: `WeatherAgent`

![Agent Creation](../../../../translated_images/pt-PT/Agent.c9c33f6a412b4cdedfb973fe5448bdb33de3f400055603111b875610e9b917ab.png)

### Passo 2: Inicializar o Projeto do Servidor MCP

1. **Navega até Ferramentas** → **Adicionar Ferramenta** no Agent Builder  
2. **Seleciona "MCP Server"** entre as opções disponíveis  
3. **Escolhe "Criar um novo Servidor MCP"**  
4. **Seleciona o template `python-weather`**  
5. **Nomeia o teu servidor:** `weather_mcp`

![Python Template Selection](../../../../translated_images/pt-PT/Pythontemplate.9d0a2913c6491500bd673430f024dc44676af2808a27b5da9dcc0eb7063adc28.png)

### Passo 3: Abrir e Analisar o Projeto

1. **Abre o projeto gerado** no VS Code  
2. **Revê a estrutura do projeto:**  
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

### Passo 4: Atualizar para o Último MCP SDK

> **🔍 Porquê atualizar?** Queremos usar o mais recente MCP SDK (v1.9.3) e o serviço Inspector (0.14.0) para funcionalidades avançadas e melhor depuração.

#### 4a. Atualizar Dependências Python

**Edita `pyproject.toml`:** atualiza [./code/weather_mcp/pyproject.toml](../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/pyproject.toml)

#### 4b. Atualizar Configuração do Inspector

**Edita `inspector/package.json`:** atualiza [./code/weather_mcp/inspector/package.json](../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/inspector/package.json)

#### 4c. Atualizar Dependências do Inspector

**Edita `inspector/package-lock.json`:** atualiza [./code/weather_mcp/inspector/package-lock.json](../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/inspector/package-lock.json)

> **📝 Nota:** Este ficheiro contém definições extensas de dependências. Abaixo está a estrutura essencial – o conteúdo completo assegura a resolução correta das dependências.

> **⚡ Package Lock Completo:** O package-lock.json completo contém cerca de 3000 linhas de definições de dependências. O acima mostra a estrutura chave – usa o ficheiro fornecido para resolução completa.

### Passo 5: Configurar a Depuração no VS Code

*Nota: Por favor, copia o ficheiro no caminho especificado para substituir o ficheiro local correspondente*

#### 5a. Atualizar Configuração de Lançamento

**Edita `.vscode/launch.json`:**

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

**Edita `.vscode/tasks.json`:**

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

## 🚀 Executar e Testar o Teu Servidor MCP

### Passo 6: Instalar Dependências

Após as alterações de configuração, executa os seguintes comandos:

**Instalar dependências Python:**  
```bash
uv sync
```

**Instalar dependências do Inspector:**  
```bash
cd inspector
npm install
```

### Passo 7: Depurar com Agent Builder

1. **Pressiona F5** ou usa a configuração **"Debug in Agent Builder"**  
2. **Seleciona a configuração composta** no painel de depuração  
3. **Espera que o servidor inicie** e o Agent Builder abra  
4. **Testa o teu servidor MCP de meteorologia** com consultas em linguagem natural

Exemplo de prompt de entrada

SYSTEM_PROMPT

```
You are my weather assistant
```

USER_PROMPT

```
How's the weather like in Seattle
```

![Agent Builder Debug Result](../../../../translated_images/pt-PT/Result.6ac570f7d2b1d5389c561ab0566970fe0f13e75bdd976b6a7f0270bc715d07f8.png)

### Passo 8: Depurar com MCP Inspector

1. **Usa a configuração "Debug in Inspector"** (Edge ou Chrome)  
2. **Abre a interface do Inspector** em `http://localhost:6274`  
3. **Explora o ambiente interativo de testes:**  
   - Visualiza as ferramentas disponíveis  
   - Testa a execução das ferramentas  
   - Monitoriza pedidos de rede  
   - Depura respostas do servidor

![MCP Inspector Interface](../../../../translated_images/pt-PT/Inspector.5672415cd02fe8731774586cc0a1083e3275d2f8491602aecc8ac4d61f2c0d57.png)

---

## 🎯 Resultados-Chave da Aprendizagem

Ao completar este laboratório, tu:

- [x] **Criaste um servidor MCP personalizado** usando templates do AI Toolkit  
- [x] **Atualizaste para o mais recente MCP SDK** (v1.9.3) para funcionalidades avançadas  
- [x] **Configuraste fluxos de trabalho profissionais de depuração** para Agent Builder e Inspector  
- [x] **Configuraste o MCP Inspector** para testes interativos do servidor  
- [x] **Dominaste as configurações de depuração no VS Code** para desenvolvimento MCP

## 🔧 Funcionalidades Avançadas Exploradas

| Funcionalidade | Descrição | Caso de Uso |
|----------------|-----------|-------------|
| **MCP Python SDK v1.9.3** | Implementação mais recente do protocolo | Desenvolvimento moderno de servidores |
| **MCP Inspector 0.14.0** | Ferramenta interativa de depuração | Testes em tempo real do servidor |
| **Depuração no VS Code** | Ambiente de desenvolvimento integrado | Fluxo profissional de depuração |
| **Integração com Agent Builder** | Ligação direta ao AI Toolkit | Testes completos do agente |

## 📚 Recursos Adicionais

- [Documentação MCP Python SDK](https://modelcontextprotocol.io/docs/sdk/python)  
- [Guia da Extensão AI Toolkit](https://code.visualstudio.com/docs/ai/ai-toolkit)  
- [Documentação de Depuração no VS Code](https://code.visualstudio.com/docs/editor/debugging)  
- [Especificação do Model Context Protocol](https://modelcontextprotocol.io/docs/concepts/architecture)

---

**🎉 Parabéns!** Concluíste com sucesso o Laboratório 3 e agora podes criar, depurar e implementar servidores MCP personalizados usando fluxos de trabalho profissionais de desenvolvimento.

### 🔜 Continua para o Próximo Módulo

Preparado para aplicar as tuas competências MCP num fluxo de trabalho de desenvolvimento real? Continua para **[Módulo 4: Desenvolvimento Prático de MCP - Servidor Personalizado de Clonagem GitHub](../lab4/README.md)** onde vais:  
- Construir um servidor MCP pronto para produção que automatiza operações em repositórios GitHub  
- Implementar funcionalidade de clonagem de repositórios GitHub via MCP  
- Integrar servidores MCP personalizados com VS Code e GitHub Copilot Agent Mode  
- Testar e implementar servidores MCP personalizados em ambientes de produção  
- Aprender automação prática de fluxos de trabalho para programadores

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, por favor tenha em conta que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes da utilização desta tradução.