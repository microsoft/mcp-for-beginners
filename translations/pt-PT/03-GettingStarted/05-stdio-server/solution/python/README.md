# Servidor MCP stdio - Solução em Python

> **⚠️ Importante**: Esta solução foi atualizada para utilizar o **transporte stdio**, conforme recomendado pela Especificação MCP 2025-06-18. O transporte SSE original foi descontinuado.

## Visão Geral

Esta solução em Python demonstra como construir um servidor MCP utilizando o transporte stdio atual. O transporte stdio é mais simples, mais seguro e oferece melhor desempenho em comparação com a abordagem SSE descontinuada.

## Pré-requisitos

- Python 3.8 ou superior
- Recomenda-se instalar `uv` para gestão de pacotes, veja [instruções](https://docs.astral.sh/uv/#highlights)

## Instruções de Configuração

### Passo 1: Criar um ambiente virtual

```bash
python -m venv venv
```

### Passo 2: Ativar o ambiente virtual

**Windows:**
```bash
venv\Scripts\activate
```

**macOS/Linux:**
```bash
source venv/bin/activate
```

### Passo 3: Instalar as dependências

```bash
pip install mcp
```

## Executar o Servidor

O servidor stdio funciona de forma diferente do antigo servidor SSE. Em vez de iniciar um servidor web, ele comunica-se através de stdin/stdout:

```bash
python server.py
```

**Importante**: O servidor parecerá estar parado - isso é normal! Ele está à espera de mensagens JSON-RPC via stdin.

## Testar o Servidor

### Método 1: Utilizar o MCP Inspector (Recomendado)

```bash
npx @modelcontextprotocol/inspector python server.py
```

Isto irá:
1. Iniciar o servidor como um subprocesso
2. Abrir uma interface web para testes
3. Permitir testar todas as ferramentas do servidor de forma interativa

### Método 2: Testar diretamente com JSON-RPC

Também é possível testar enviando mensagens JSON-RPC diretamente:

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

### Testar com Claude Desktop

Para utilizar este servidor com o Claude Desktop, adicione esta configuração ao seu `claude_desktop_config.json`:

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
- ✅ Configuração mais simples - não é necessário servidor web
- ✅ Melhor segurança - sem endpoints HTTP
- ✅ Comunicação baseada em subprocessos
- ✅ JSON-RPC via stdin/stdout
- ✅ Melhor desempenho

**Transporte SSE (Descontinuado):**
- ❌ Requeria configuração de servidor HTTP
- ❌ Necessitava de framework web (Starlette/FastAPI)
- ❌ Gestão de rotas e sessões mais complexa
- ❌ Considerações adicionais de segurança
- ❌ Agora descontinuado na MCP 2025-06-18

## Dicas de Depuração

- Utilize `stderr` para registos (nunca `stdout`)
- Teste com o Inspector para depuração visual
- Certifique-se de que todas as mensagens JSON são delimitadas por nova linha
- Verifique se o servidor inicia sem erros

Esta solução segue a especificação atual do MCP e demonstra as melhores práticas para implementação do transporte stdio.

---

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, é importante ter em conta que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autoritária. Para informações críticas, recomenda-se a tradução profissional realizada por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes da utilização desta tradução.