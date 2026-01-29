# Executando este exemplo

Veja como executar o servidor e cliente de streaming HTTP clássico, bem como o servidor e cliente de streaming MCP usando Python.

### Visão Geral

- Você configurará um servidor MCP que transmite notificações de progresso para o cliente enquanto processa itens.
- O cliente exibirá cada notificação em tempo real.
- Este guia cobre os pré-requisitos, configuração, execução e solução de problemas.

### Pré-requisitos

- Python 3.9 ou mais recente
- O pacote Python `mcp` (instale com `pip install mcp`)

### Instalação e Configuração

1. Clone o repositório ou baixe os arquivos da solução.

   ```pwsh
   git clone https://github.com/microsoft/mcp-for-beginners
   ```

1. **Crie e ative um ambiente virtual (recomendado):**

   ```pwsh
   python -m venv venv
   .\venv\Scripts\Activate.ps1  # On Windows
   # or
   source venv/bin/activate      # On Linux/macOS
   ```

1. **Instale as dependências necessárias:**

   ```pwsh
   pip install "mcp[cli]" fastapi requests
   ```

### Arquivos

- **Servidor:** [server.py](../../../../../../03-GettingStarted/06-http-streaming/solution/python/server.py)
- **Cliente:** [client.py](../../../../../../03-GettingStarted/06-http-streaming/solution/python/client.py)

### Executando o Servidor de Streaming HTTP Clássico

1. Navegue até o diretório da solução:

   ```pwsh
   cd 03-GettingStarted/06-http-streaming/solution
   ```

2. Inicie o servidor de streaming HTTP clássico:

   ```pwsh
   python server.py
   ```

3. O servidor será iniciado e exibirá:

   ```
   Starting FastAPI server for classic HTTP streaming...
   INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
   ```

### Executando o Cliente de Streaming HTTP Clássico

1. Abra um novo terminal (ative o mesmo ambiente virtual e diretório):

   ```pwsh
   cd 03-GettingStarted/06-http-streaming/solution
   python client.py
   ```

2. Você verá as mensagens transmitidas sendo exibidas sequencialmente:

   ```text
   Running classic HTTP streaming client...
   Connecting to http://localhost:8000/stream with message: hello
   --- Streaming Progress ---
   Processing file 1/3...
   Processing file 2/3...
   Processing file 3/3...
   Here's the file content: hello
   --- Stream Ended ---
   ```

### Executando o Servidor de Streaming MCP

1. Navegue até o diretório da solução:
   ```pwsh
   cd 03-GettingStarted/06-http-streaming/solution
   ```
2. Inicie o servidor MCP com o transporte streamable-http:
   ```pwsh
   python server.py mcp
   ```
3. O servidor será iniciado e exibirá:
   ```
   Starting MCP server with streamable-http transport...
   INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
   ```

### Executando o Cliente de Streaming MCP

1. Abra um novo terminal (ative o mesmo ambiente virtual e diretório):
   ```pwsh
   cd 03-GettingStarted/06-http-streaming/solution
   python client.py mcp
   ```
2. Você verá as notificações sendo exibidas em tempo real enquanto o servidor processa cada item:
   ```
   Running MCP client...
   Starting client...
   Session ID before init: None
   Session ID after init: a30ab7fca9c84f5fa8f5c54fe56c9612
   Session initialized, ready to call tools.
   Received message: root=LoggingMessageNotification(...)
   NOTIFICATION: root=LoggingMessageNotification(...)
   ...
   Tool result: meta=None content=[TextContent(type='text', text='Processed files: file_1.txt, file_2.txt, file_3.txt | Message: hello from client')]
   ```

### Principais Etapas de Implementação

1. **Crie o servidor MCP usando o FastMCP.**
2. **Defina uma ferramenta que processe uma lista e envie notificações usando `ctx.info()` ou `ctx.log()`.**
3. **Execute o servidor com `transport="streamable-http"`.**
4. **Implemente um cliente com um manipulador de mensagens para exibir notificações à medida que chegam.**

### Explicação do Código
- O servidor utiliza funções assíncronas e o contexto MCP para enviar atualizações de progresso.
- O cliente implementa um manipulador de mensagens assíncrono para imprimir notificações e o resultado final.

### Dicas e Solução de Problemas

- Use `async/await` para operações não bloqueantes.
- Sempre trate exceções tanto no servidor quanto no cliente para maior robustez.
- Teste com vários clientes para observar atualizações em tempo real.
- Se encontrar erros, verifique sua versão do Python e certifique-se de que todas as dependências estão instaladas.

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte oficial. Para informações críticas, recomenda-se a tradução profissional feita por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.