# Servidor MCP stdio - Solução em Python

> **⚠️ Importante**: Esta solução foi atualizada para usar o **transporte stdio** conforme recomendado pela Especificação MCP 2025-06-18. O transporte SSE original foi descontinuado.

## Visão Geral

Esta solução em Python demonstra como construir um servidor MCP usando o transporte stdio atual. O transporte stdio é mais simples, mais seguro e oferece melhor desempenho em comparação com a abordagem SSE descontinuada.

## Pré-requisitos

- Python 3.8 ou superior
- Recomenda-se instalar `uv` para gerenciamento de pacotes, veja [instruções](https://docs.astral.sh/uv/#highlights)

## Instruções de Configuração

### Passo 1: Crie um ambiente virtual

```bash
python -m venv venv
```

### Passo 2: Ative o ambiente virtual

**Windows:**
```bash
venv\Scripts\activate
```

**macOS/Linux:**
```bash
source venv/bin/activate
```

### Passo 3: Instale as dependências

```bash
pip install mcp
```

## Executando o Servidor

O servidor stdio funciona de forma diferente do antigo servidor SSE. Em vez de iniciar um servidor web, ele se comunica por meio de stdin/stdout:

```bash
python server.py
```

**Importante**: O servidor parecerá estar travado - isso é normal! Ele está aguardando mensagens JSON-RPC via stdin.

## Testando o Servidor

### Método 1: Usando o MCP Inspector (Recomendado)

```bash
npx @modelcontextprotocol/inspector python server.py
```

Isso irá:
1. Iniciar seu servidor como um subprocesso
2. Abrir uma interface web para testes
3. Permitir que você teste todas as ferramentas do servidor de forma interativa

### Método 2: Teste direto com JSON-RPC

Você também pode testar enviando mensagens JSON-RPC diretamente:

1. Inicie o servidor: `python server.py`
2. Envie uma mensagem JSON-RPC (exemplo):

```json
{"jsonrpc": "2.0", "id": 1, "method": "tools/list"}
```

3. O servidor responderá com as ferramentas disponíveis

### Ferramentas Disponíveis

O servidor fornece as seguintes ferramentas:

- **add(a, b)**: Soma dois números
- **multiply(a, b)**: Multiplica dois números  
- **get_greeting(name)**: Gera uma saudação personalizada
- **get_server_info()**: Obtém informações sobre o servidor

### Testando com Claude Desktop

Para usar este servidor com o Claude Desktop, adicione esta configuração ao seu `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "example-stdio-server": {
      "command": "python",
      "args": ["path/to/server.py"]
    }
  }
}
```

## Principais Diferenças em Relação ao SSE

**Transporte stdio (Atual):**
- ✅ Configuração mais simples - sem necessidade de servidor web
- ✅ Maior segurança - sem endpoints HTTP
- ✅ Comunicação baseada em subprocessos
- ✅ JSON-RPC via stdin/stdout
- ✅ Melhor desempenho

**Transporte SSE (Descontinuado):**
- ❌ Requeria configuração de servidor HTTP
- ❌ Necessitava de framework web (Starlette/FastAPI)
- ❌ Gerenciamento de rotas e sessões mais complexo
- ❌ Considerações adicionais de segurança
- ❌ Agora descontinuado na MCP 2025-06-18

## Dicas de Depuração

- Use `stderr` para logs (nunca `stdout`)
- Teste com o Inspector para depuração visual
- Certifique-se de que todas as mensagens JSON sejam delimitadas por nova linha
- Verifique se o servidor inicia sem erros

Esta solução segue a especificação atual do MCP e demonstra as melhores práticas para implementação de transporte stdio.

---

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autoritativa. Para informações críticas, recomenda-se a tradução profissional realizada por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações equivocadas decorrentes do uso desta tradução.