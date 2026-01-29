# Servidor MCP de Clima

Este é um exemplo de servidor MCP em Python que implementa ferramentas de clima com respostas simuladas. Ele pode ser usado como base para criar seu próprio servidor MCP. Inclui os seguintes recursos:

- **Ferramenta de Clima**: Uma ferramenta que fornece informações climáticas simuladas com base na localização fornecida.
- **Ferramenta de Clonagem de Repositório Git**: Uma ferramenta que clona um repositório Git para uma pasta especificada.
- **Ferramenta de Abertura no VS Code**: Uma ferramenta que abre uma pasta no VS Code ou no VS Code Insiders.
- **Conectar ao Agent Builder**: Um recurso que permite conectar o servidor MCP ao Agent Builder para testes e depuração.
- **Depuração no [MCP Inspector](https://github.com/modelcontextprotocol/inspector)**: Um recurso que permite depurar o servidor MCP usando o MCP Inspector.

## Comece com o template do Servidor MCP de Clima

> **Pré-requisitos**
>
> Para executar o servidor MCP na sua máquina de desenvolvimento local, você precisará de:
>
> - [Python](https://www.python.org/)
> - [Git](https://git-scm.com/) (Necessário para a ferramenta git_clone_repo)
> - [VS Code](https://code.visualstudio.com/) ou [VS Code Insiders](https://code.visualstudio.com/insiders/) (Necessário para a ferramenta open_in_vscode)
> - (*Opcional - se preferir uv*) [uv](https://github.com/astral-sh/uv)
> - [Extensão de Depuração Python](https://marketplace.visualstudio.com/items?itemName=ms-python.debugpy)

## Preparar o ambiente

Existem duas abordagens para configurar o ambiente deste projeto. Você pode escolher qualquer uma com base na sua preferência.

> Nota: Reinicie o VS Code ou o terminal para garantir que o Python do ambiente virtual seja usado após criar o ambiente virtual.

| Abordagem | Passos |
| --------- | ------ |
| Usando `uv` | 1. Criar ambiente virtual: `uv venv` <br>2. Executar o comando do VS Code "***Python: Select Interpreter***" e selecionar o Python do ambiente virtual criado <br>3. Instalar dependências (incluindo dependências de desenvolvimento): `uv pip install -r pyproject.toml --extra dev` |
| Usando `pip` | 1. Criar ambiente virtual: `python -m venv .venv` <br>2. Executar o comando do VS Code "***Python: Select Interpreter***" e selecionar o Python do ambiente virtual criado <br>3. Instalar dependências (incluindo dependências de desenvolvimento): `pip install -e .[dev]` |

Após configurar o ambiente, você pode executar o servidor na sua máquina de desenvolvimento local via Agent Builder como cliente MCP para começar:
1. Abra o painel de depuração do VS Code. Selecione `Debug in Agent Builder` ou pressione `F5` para iniciar a depuração do servidor MCP.
2. Use o AI Toolkit Agent Builder para testar o servidor com [este prompt](../../../../../../../../../../../open_prompt_builder). O servidor será conectado automaticamente ao Agent Builder.
3. Clique em `Run` para testar o servidor com o prompt.

**Parabéns**! Você executou com sucesso o Servidor MCP de Clima na sua máquina de desenvolvimento local via Agent Builder como cliente MCP.
![DebugMCP](https://raw.githubusercontent.com/microsoft/windows-ai-studio-templates/refs/heads/dev/mcpServers/mcp_debug.gif)

## O que está incluído no template

| Pasta / Arquivo | Conteúdo                                     |
| --------------- | -------------------------------------------- |
| `.vscode`       | Arquivos do VS Code para depuração           |
| `.aitk`         | Configurações para o AI Toolkit              |
| `src`           | Código-fonte do servidor MCP de clima        |

## Como depurar o Servidor MCP de Clima

> Notas:
> - [MCP Inspector](https://github.com/modelcontextprotocol/inspector) é uma ferramenta visual de desenvolvimento para testar e depurar servidores MCP.
> - Todos os modos de depuração suportam pontos de interrupção, então você pode adicioná-los ao código de implementação das ferramentas.

## Ferramentas Disponíveis

### Ferramenta de Clima
A ferramenta `get_weather` fornece informações climáticas simuladas para uma localização especificada.

| Parâmetro | Tipo | Descrição |
| --------- | ---- | --------- |
| `location` | string | Localização para obter informações climáticas (ex.: nome da cidade, estado ou coordenadas) |

### Ferramenta de Clonagem de Repositório Git
A ferramenta `git_clone_repo` clona um repositório Git para uma pasta especificada.

| Parâmetro | Tipo | Descrição |
| --------- | ---- | --------- |
| `repo_url` | string | URL do repositório Git a ser clonado |
| `target_folder` | string | Caminho para a pasta onde o repositório será clonado |

A ferramenta retorna um objeto JSON com:
- `success`: Booleano indicando se a operação foi bem-sucedida
- `target_folder` ou `error`: O caminho do repositório clonado ou uma mensagem de erro

### Ferramenta de Abertura no VS Code
A ferramenta `open_in_vscode` abre uma pasta no aplicativo VS Code ou VS Code Insiders.

| Parâmetro | Tipo | Descrição |
| --------- | ---- | --------- |
| `folder_path` | string | Caminho para a pasta a ser aberta |
| `use_insiders` | boolean (opcional) | Indica se deve usar o VS Code Insiders em vez do VS Code regular |

A ferramenta retorna um objeto JSON com:
- `success`: Booleano indicando se a operação foi bem-sucedida
- `message` ou `error`: Uma mensagem de confirmação ou uma mensagem de erro

| Modo de Depuração | Descrição | Passos para depurar |
| ----------------- | --------- | ------------------- |
| Agent Builder | Depure o servidor MCP no Agent Builder via AI Toolkit. | 1. Abra o painel de depuração do VS Code. Selecione `Debug in Agent Builder` e pressione `F5` para iniciar a depuração do servidor MCP.<br>2. Use o AI Toolkit Agent Builder para testar o servidor com [este prompt](../../../../../../../../../../../open_prompt_builder). O servidor será conectado automaticamente ao Agent Builder.<br>3. Clique em `Run` para testar o servidor com o prompt. |
| MCP Inspector | Depure o servidor MCP usando o MCP Inspector. | 1. Instale o [Node.js](https://nodejs.org/)<br> 2. Configure o Inspector: `cd inspector` && `npm install` <br> 3. Abra o painel de depuração do VS Code. Selecione `Debug SSE in Inspector (Edge)` ou `Debug SSE in Inspector (Chrome)`. Pressione F5 para iniciar a depuração.<br> 4. Quando o MCP Inspector for iniciado no navegador, clique no botão `Connect` para conectar este servidor MCP.<br> 5. Então você pode `List Tools`, selecionar uma ferramenta, inserir parâmetros e `Run Tool` para depurar o código do servidor.<br> |

## Portas Padrão e Personalizações

| Modo de Depuração | Portas | Definições | Personalizações | Nota |
| ----------------- | ------ | ---------- | --------------- | ---- |
| Agent Builder | 3001 | [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json) | Edite [launch.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/launch.json), [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json), [\_\_init\_\_.py](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/src/__init__.py), [mcp.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.aitk/mcp.json) para alterar as portas acima. | N/A |
| MCP Inspector | 3001 (Servidor); 5173 e 3000 (Inspector) | [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json) | Edite [launch.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/launch.json), [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json), [\_\_init\_\_.py](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/src/__init__.py), [mcp.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.aitk/mcp.json) para alterar as portas acima. | N/A |

## Feedback

Se você tiver algum feedback ou sugestão para este template, abra uma issue no [repositório GitHub do AI Toolkit](https://github.com/microsoft/vscode-ai-toolkit/issues).

---

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autoritativa. Para informações críticas, recomenda-se a tradução profissional realizada por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações equivocadas decorrentes do uso desta tradução.