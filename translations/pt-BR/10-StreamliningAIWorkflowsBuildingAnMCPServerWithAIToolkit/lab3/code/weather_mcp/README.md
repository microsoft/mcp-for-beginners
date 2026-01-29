# Weather MCP Server

Este é um exemplo de MCP Server em Python que implementa ferramentas de clima com respostas simuladas. Pode ser usado como base para o seu próprio MCP Server. Inclui os seguintes recursos:

- **Weather Tool**: Uma ferramenta que fornece informações meteorológicas simuladas com base na localização fornecida.
- **Conectar ao Agent Builder**: Um recurso que permite conectar o MCP server ao Agent Builder para testes e depuração.
- **Depurar no [MCP Inspector](https://github.com/modelcontextprotocol/inspector)**: Um recurso que permite depurar o MCP Server usando o MCP Inspector.

## Começando com o template Weather MCP Server

> **Pré-requisitos**
>
> Para rodar o MCP Server na sua máquina local de desenvolvimento, você precisará de:
>
> - [Python](https://www.python.org/)
> - (*Opcional - se preferir uv*) [uv](https://github.com/astral-sh/uv)
> - [Extensão Python Debugger](https://marketplace.visualstudio.com/items?itemName=ms-python.debugpy)

## Preparar o ambiente

Existem duas formas de configurar o ambiente para este projeto. Você pode escolher a que preferir.

> Nota: Recarregue o VSCode ou o terminal para garantir que o Python do ambiente virtual seja usado após a criação do ambiente virtual.

| Abordagem | Passos |
| --------- | ------ |
| Usando `uv` | 1. Crie o ambiente virtual: `uv venv` <br>2. Execute o comando do VSCode "***Python: Select Interpreter***" e selecione o Python do ambiente virtual criado <br>3. Instale as dependências (incluindo as de desenvolvimento): `uv pip install -r pyproject.toml --extra dev` |
| Usando `pip` | 1. Crie o ambiente virtual: `python -m venv .venv` <br>2. Execute o comando do VSCode "***Python: Select Interpreter***" e selecione o Python do ambiente virtual criado <br>3. Instale as dependências (incluindo as de desenvolvimento): `pip install -e .[dev]` |

Após configurar o ambiente, você pode rodar o servidor na sua máquina local de desenvolvimento via Agent Builder como MCP Client para começar:
1. Abra o painel de Depuração do VS Code. Selecione `Debug in Agent Builder` ou pressione `F5` para iniciar a depuração do MCP server.
2. Use o AI Toolkit Agent Builder para testar o servidor com [este prompt](../../../../../../../../../../open_prompt_builder). O servidor será conectado automaticamente ao Agent Builder.
3. Clique em `Run` para testar o servidor com o prompt.

**Parabéns**! Você executou com sucesso o Weather MCP Server na sua máquina local de desenvolvimento via Agent Builder como MCP Client.  
![DebugMCP](https://raw.githubusercontent.com/microsoft/windows-ai-studio-templates/refs/heads/dev/mcpServers/mcp_debug.gif)

## O que está incluído no template

| Pasta / Arquivo | Conteúdo                                   |
| --------------- | ----------------------------------------- |
| `.vscode`       | Arquivos do VSCode para depuração         |
| `.aitk`         | Configurações para o AI Toolkit            |
| `src`           | Código-fonte do servidor weather mcp      |

## Como depurar o Weather MCP Server

> Notas:
> - [MCP Inspector](https://github.com/modelcontextprotocol/inspector) é uma ferramenta visual para desenvolvedores testarem e depurarem MCP servers.
> - Todos os modos de depuração suportam breakpoints, então você pode adicionar pontos de interrupção no código da implementação da ferramenta.

| Modo de Depuração | Descrição | Passos para depurar |
| ----------------- | --------- | ------------------- |
| Agent Builder | Depure o MCP server no Agent Builder via AI Toolkit. | 1. Abra o painel de Depuração do VS Code. Selecione `Debug in Agent Builder` e pressione `F5` para iniciar a depuração do MCP server.<br>2. Use o AI Toolkit Agent Builder para testar o servidor com [este prompt](../../../../../../../../../../open_prompt_builder). O servidor será conectado automaticamente ao Agent Builder.<br>3. Clique em `Run` para testar o servidor com o prompt. |
| MCP Inspector | Depure o MCP server usando o MCP Inspector. | 1. Instale o [Node.js](https://nodejs.org/)<br>2. Configure o Inspector: `cd inspector` && `npm install` <br>3. Abra o painel de Depuração do VS Code. Selecione `Debug SSE in Inspector (Edge)` ou `Debug SSE in Inspector (Chrome)`. Pressione F5 para iniciar a depuração.<br>4. Quando o MCP Inspector abrir no navegador, clique no botão `Connect` para conectar este MCP server.<br>5. Então você pode `List Tools`, selecionar uma ferramenta, inserir parâmetros e `Run Tool` para depurar seu código do servidor.<br> |

## Portas padrão e personalizações

| Modo de Depuração | Portas | Definições | Personalizações | Nota |
| ----------------- | ------ | ---------- | --------------- | ---- |
| Agent Builder | 3001 | [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/tasks.json) | Edite [launch.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/launch.json), [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/tasks.json), [\_\_init\_\_.py](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/src/__init__.py), [mcp.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.aitk/mcp.json) para alterar as portas acima. | N/A |
| MCP Inspector | 3001 (Servidor); 5173 e 3000 (Inspector) | [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/tasks.json) | Edite [launch.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/launch.json), [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/tasks.json), [\_\_init\_\_.py](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/src/__init__.py), [mcp.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.aitk/mcp.json) para alterar as portas acima. | N/A |

## Feedback

Se você tiver algum feedback ou sugestão para este template, por favor abra uma issue no [repositório AI Toolkit no GitHub](https://github.com/microsoft/vscode-ai-toolkit/issues)

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.