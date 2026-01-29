# Lição: Construir um Servidor MCP de Pesquisa Web

Este capítulo demonstra como construir um agente de IA real que integra APIs externas, lida com diversos tipos de dados, gere erros e orquestra múltiplas ferramentas—tudo num formato pronto para produção. Vai ver:

- **Integração com APIs externas que requerem autenticação**
- **Gestão de diversos tipos de dados provenientes de múltiplos endpoints**
- **Estratégias robustas de tratamento de erros e registo**
- **Orquestração de múltiplas ferramentas num único servidor**

No final, terá experiência prática com padrões e boas práticas essenciais para aplicações avançadas de IA e potenciadas por LLM.

## Introdução

Nesta lição, vai aprender a construir um servidor e cliente MCP avançados que estendem as capacidades do LLM com dados web em tempo real usando SerpAPI. Esta é uma competência fundamental para desenvolver agentes de IA dinâmicos que acedem a informação atualizada da web.

## Objetivos de Aprendizagem

No final desta lição, será capaz de:

- Integrar APIs externas (como SerpAPI) de forma segura num servidor MCP
- Implementar múltiplas ferramentas para pesquisa web, notícias, produtos e perguntas e respostas
- Analisar e formatar dados estruturados para consumo pelo LLM
- Gerir erros e limites de taxa das APIs de forma eficaz
- Construir e testar clientes MCP automatizados e interativos

## Servidor MCP de Pesquisa Web

Esta secção apresenta a arquitetura e funcionalidades do Servidor MCP de Pesquisa Web. Vai ver como o FastMCP e o SerpAPI são usados em conjunto para estender as capacidades do LLM com dados web em tempo real.

### Visão Geral

Esta implementação inclui quatro ferramentas que demonstram a capacidade do MCP para lidar com tarefas diversas, baseadas em APIs externas, de forma segura e eficiente:

- **general_search**: Para resultados gerais da web
- **news_search**: Para manchetes recentes
- **product_search**: Para dados de comércio eletrónico
- **qna**: Para excertos de perguntas e respostas

### Funcionalidades
- **Exemplos de Código**: Inclui blocos de código específicos para Python (e facilmente extensível a outras linguagens) usando pivôs de código para maior clareza

### Python

```python
# Example usage of the general_search tool
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def run_search():
    server_params = StdioServerParameters(
        command="python",
        args=["server.py"],
    )
    async with stdio_client(server_params) as (reader, writer):
        async with ClientSession(reader, writer) as session:
            await session.initialize()
            result = await session.call_tool("general_search", arguments={"query": "open source LLMs"})
            print(result)
```

---

Antes de executar o cliente, é útil compreender o que o servidor faz. O ficheiro [`server.py`](../../../../05-AdvancedTopics/web-search-mcp/server.py) implementa o servidor MCP, expondo ferramentas para pesquisa web, notícias, produtos e Q&A através da integração com SerpAPI. Ele gere pedidos recebidos, chamadas à API, analisa respostas e devolve resultados estruturados ao cliente.

Pode consultar a implementação completa em [`server.py`](../../../../05-AdvancedTopics/web-search-mcp/server.py).

Aqui está um exemplo breve de como o servidor define e regista uma ferramenta:

### Servidor Python

```python
# server.py (excerpt)
from mcp.server import MCPServer, Tool

async def general_search(query: str):
    # ...implementation...

server = MCPServer()
server.add_tool(Tool("general_search", general_search))

if __name__ == "__main__":
    server.run()
```

---

- **Integração com API Externa**: Demonstra a gestão segura de chaves API e pedidos externos
- **Análise de Dados Estruturados**: Mostra como transformar respostas da API em formatos amigáveis para LLM
- **Tratamento de Erros**: Gestão robusta de erros com registo apropriado
- **Cliente Interativo**: Inclui testes automatizados e um modo interativo para testes
- **Gestão de Contexto**: Utiliza MCP Context para registo e acompanhamento dos pedidos

## Pré-requisitos

Antes de começar, certifique-se de que o seu ambiente está configurado corretamente seguindo estes passos. Isto garantirá que todas as dependências estão instaladas e as suas chaves API configuradas para um desenvolvimento e testes sem problemas.

- Python 3.8 ou superior
- Chave API SerpAPI (Registe-se em [SerpAPI](https://serpapi.com/) - existe um plano gratuito)

## Instalação

Para começar, siga estes passos para configurar o seu ambiente:

1. Instale as dependências usando uv (recomendado) ou pip:

```bash
# Using uv (recommended)
uv pip install -r requirements.txt

# Using pip
pip install -r requirements.txt
```

2. Crie um ficheiro `.env` na raiz do projeto com a sua chave SerpAPI:

```
SERPAPI_KEY=your_serpapi_key_here
```

## Utilização

O Servidor MCP de Pesquisa Web é o componente central que expõe ferramentas para pesquisa web, notícias, produtos e Q&A integrando com SerpAPI. Gere pedidos recebidos, chamadas à API, analisa respostas e devolve resultados estruturados ao cliente.

Pode consultar a implementação completa em [`server.py`](../../../../05-AdvancedTopics/web-search-mcp/server.py).

### Executar o Servidor

Para iniciar o servidor MCP, use o seguinte comando:

```bash
python server.py
```

O servidor irá funcionar como um servidor MCP baseado em stdio, ao qual o cliente pode ligar-se diretamente.

### Modos do Cliente

O cliente (`client.py`) suporta dois modos para interagir com o servidor MCP:

- **Modo Normal**: Executa testes automatizados que exercitam todas as ferramentas e verificam as suas respostas. Útil para verificar rapidamente se o servidor e as ferramentas estão a funcionar como esperado.
- **Modo Interativo**: Inicia uma interface com menu onde pode selecionar e chamar ferramentas manualmente, inserir consultas personalizadas e ver resultados em tempo real. Ideal para explorar as capacidades do servidor e experimentar diferentes entradas.

Pode consultar a implementação completa em [`client.py`](../../../../05-AdvancedTopics/web-search-mcp/client.py).

### Executar o Cliente

Para executar os testes automatizados (isto inicia automaticamente o servidor):

```bash
python client.py
```

Ou execute em modo interativo:

```bash
python client.py --interactive
```

### Testar com Diferentes Métodos

Existem várias formas de testar e interagir com as ferramentas fornecidas pelo servidor, dependendo das suas necessidades e fluxo de trabalho.

#### Escrever Scripts de Teste Personalizados com o MCP Python SDK
Também pode criar os seus próprios scripts de teste usando o MCP Python SDK:

# [Python](../../../../05-AdvancedTopics/web-search-mcp)

```python
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def test_custom_query():
    server_params = StdioServerParameters(
        command="python",
        args=["server.py"],
    )
    
    async with stdio_client(server_params) as (reader, writer):
        async with ClientSession(reader, writer) as session:
            await session.initialize()
            # Call tools with your custom parameters
            result = await session.call_tool("general_search", 
                                           arguments={"query": "your custom query"})
            # Process the result
```

---

Neste contexto, um "script de teste" significa um programa Python personalizado que escreve para atuar como cliente do servidor MCP. Em vez de ser um teste unitário formal, este script permite-lhe ligar-se programaticamente ao servidor, chamar qualquer uma das suas ferramentas com parâmetros à sua escolha e inspecionar os resultados. Esta abordagem é útil para:
- Prototipar e experimentar chamadas às ferramentas
- Validar como o servidor responde a diferentes entradas
- Automatizar invocações repetidas das ferramentas
- Construir os seus próprios fluxos de trabalho ou integrações em cima do servidor MCP

Pode usar scripts de teste para experimentar rapidamente novas consultas, depurar o comportamento das ferramentas ou mesmo como ponto de partida para automação mais avançada. Abaixo está um exemplo de como usar o MCP Python SDK para criar tal script:

## Descrição das Ferramentas

Pode usar as seguintes ferramentas fornecidas pelo servidor para realizar diferentes tipos de pesquisas e consultas. Cada ferramenta é descrita abaixo com os seus parâmetros e exemplos de uso.

Esta secção fornece detalhes sobre cada ferramenta disponível e os seus parâmetros.

### general_search

Realiza uma pesquisa geral na web e devolve resultados formatados.

**Como chamar esta ferramenta:**

Pode chamar `general_search` a partir do seu próprio script usando o MCP Python SDK, ou interativamente usando o Inspector ou o modo interativo do cliente. Aqui está um exemplo de código usando o SDK:

# [Exemplo Python](../../../../05-AdvancedTopics/web-search-mcp)

```python
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def run_general_search():
    server_params = StdioServerParameters(
        command="python",
        args=["server.py"],
    )
    async with stdio_client(server_params) as (reader, writer):
        async with ClientSession(reader, writer) as session:
            await session.initialize()
            result = await session.call_tool("general_search", arguments={"query": "latest AI trends"})
            print(result)
```

---

Alternativamente, em modo interativo, selecione `general_search` no menu e insira a sua consulta quando solicitado.

**Parâmetros:**
- `query` (string): A consulta de pesquisa

**Exemplo de Pedido:**

```json
{
  "query": "latest AI trends"
}
```

### news_search

Pesquisa artigos de notícias recentes relacionados com uma consulta.

**Como chamar esta ferramenta:**

Pode chamar `news_search` a partir do seu próprio script usando o MCP Python SDK, ou interativamente usando o Inspector ou o modo interativo do cliente. Aqui está um exemplo de código usando o SDK:

# [Exemplo Python](../../../../05-AdvancedTopics/web-search-mcp)

```python
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def run_news_search():
    server_params = StdioServerParameters(
        command="python",
        args=["server.py"],
    )
    async with stdio_client(server_params) as (reader, writer):
        async with ClientSession(reader, writer) as session:
            await session.initialize()
            result = await session.call_tool("news_search", arguments={"query": "AI policy updates"})
            print(result)
```

---

Alternativamente, em modo interativo, selecione `news_search` no menu e insira a sua consulta quando solicitado.

**Parâmetros:**
- `query` (string): A consulta de pesquisa

**Exemplo de Pedido:**

```json
{
  "query": "AI policy updates"
}
```

### product_search

Pesquisa produtos que correspondam a uma consulta.

**Como chamar esta ferramenta:**

Pode chamar `product_search` a partir do seu próprio script usando o MCP Python SDK, ou interativamente usando o Inspector ou o modo interativo do cliente. Aqui está um exemplo de código usando o SDK:

# [Exemplo Python](../../../../05-AdvancedTopics/web-search-mcp)

```python
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def run_product_search():
    server_params = StdioServerParameters(
        command="python",
        args=["server.py"],
    )
    async with stdio_client(server_params) as (reader, writer):
        async with ClientSession(reader, writer) as session:
            await session.initialize()
            result = await session.call_tool("product_search", arguments={"query": "best AI gadgets 2025"})
            print(result)
```

---

Alternativamente, em modo interativo, selecione `product_search` no menu e insira a sua consulta quando solicitado.

**Parâmetros:**
- `query` (string): A consulta de pesquisa de produtos

**Exemplo de Pedido:**

```json
{
  "query": "best AI gadgets 2025"
}
```

### qna

Obtém respostas diretas a perguntas a partir de motores de busca.

**Como chamar esta ferramenta:**

Pode chamar `qna` a partir do seu próprio script usando o MCP Python SDK, ou interativamente usando o Inspector ou o modo interativo do cliente. Aqui está um exemplo de código usando o SDK:

# [Exemplo Python](../../../../05-AdvancedTopics/web-search-mcp)

```python
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def run_qna():
    server_params = StdioServerParameters(
        command="python",
        args=["server.py"],
    )
    async with stdio_client(server_params) as (reader, writer):
        async with ClientSession(reader, writer) as session:
            await session.initialize()
            result = await session.call_tool("qna", arguments={"question": "what is artificial intelligence"})
            print(result)
```

---

Alternativamente, em modo interativo, selecione `qna` no menu e insira a sua pergunta quando solicitado.

**Parâmetros:**
- `question` (string): A pergunta para a qual quer encontrar uma resposta

**Exemplo de Pedido:**

```json
{
  "question": "what is artificial intelligence"
}
```

## Detalhes do Código

Esta secção fornece excertos de código e referências para as implementações do servidor e cliente.

# [Python](../../../../05-AdvancedTopics/web-search-mcp)

Consulte [`server.py`](../../../../05-AdvancedTopics/web-search-mcp/server.py) e [`client.py`](../../../../05-AdvancedTopics/web-search-mcp/client.py) para detalhes completos da implementação.

```python
# Example snippet from server.py:
import os
import httpx
# ...existing code...
```

---

## Conceitos Avançados Nesta Lição

Antes de começar a construir, aqui estão alguns conceitos avançados importantes que irão aparecer ao longo deste capítulo. Compreendê-los vai ajudá-lo a acompanhar, mesmo que sejam novos para si:

- **Orquestração Multi-ferramenta**: Significa executar várias ferramentas diferentes (como pesquisa web, notícias, produtos e Q&A) dentro de um único servidor MCP. Permite que o seu servidor lide com uma variedade de tarefas, não apenas uma.
- **Gestão de Limites de Taxa da API**: Muitas APIs externas (como SerpAPI) limitam o número de pedidos que pode fazer num determinado período. Um bom código verifica esses limites e lida com eles de forma elegante, para que a sua aplicação não falhe se atingir um limite.
- **Análise de Dados Estruturados**: As respostas das APIs são frequentemente complexas e aninhadas. Este conceito trata de transformar essas respostas em formatos limpos e fáceis de usar, amigáveis para LLMs ou outros programas.
- **Recuperação de Erros**: Às vezes as coisas correm mal—talvez a rede falhe, ou a API não devolva o que espera. A recuperação de erros significa que o seu código pode lidar com esses problemas e ainda fornecer feedback útil, em vez de falhar.
- **Validação de Parâmetros**: Trata-se de verificar que todas as entradas para as suas ferramentas estão corretas e são seguras de usar. Inclui definir valores por defeito e garantir que os tipos estão corretos, o que ajuda a evitar bugs e confusão.

Esta secção vai ajudá-lo a diagnosticar e resolver problemas comuns que possa encontrar ao trabalhar com o Servidor MCP de Pesquisa Web. Se encontrar erros ou comportamentos inesperados, esta secção de resolução de problemas oferece soluções para os problemas mais comuns. Reveja estas dicas antes de procurar ajuda adicional—muitas vezes resolvem os problemas rapidamente.

## Resolução de Problemas

Ao trabalhar com o Servidor MCP de Pesquisa Web, pode ocasionalmente encontrar problemas—isto é normal quando se desenvolve com APIs externas e novas ferramentas. Esta secção fornece soluções práticas para os problemas mais comuns, para que possa voltar ao trabalho rapidamente. Se encontrar um erro, comece aqui: as dicas abaixo abordam os problemas que a maioria dos utilizadores enfrenta e podem muitas vezes resolver o seu problema sem ajuda extra.

### Problemas Comuns

Abaixo estão alguns dos problemas mais frequentes que os utilizadores encontram, com explicações claras e passos para os resolver:

1. **Falta da variável SERPAPI_KEY no ficheiro .env**
   - Se vir o erro `SERPAPI_KEY environment variable not found`, significa que a sua aplicação não consegue encontrar a chave API necessária para aceder ao SerpAPI. Para corrigir, crie um ficheiro chamado `.env` na raiz do seu projeto (se ainda não existir) e adicione uma linha como `SERPAPI_KEY=sua_chave_serpapi_aqui`. Certifique-se de substituir `sua_chave_serpapi_aqui` pela sua chave real do site SerpAPI.

2. **Erros de módulo não encontrado**
   - Erros como `ModuleNotFoundError: No module named 'httpx'` indicam que falta um pacote Python necessário. Isto acontece normalmente se não instalou todas as dependências. Para resolver, execute `pip install -r requirements.txt` no seu terminal para instalar tudo o que o seu projeto precisa.

3. **Problemas de ligação**
   - Se receber um erro como `Error during client execution`, muitas vezes significa que o cliente não consegue ligar-se ao servidor, ou o servidor não está a correr como esperado. Verifique se o cliente e servidor são versões compatíveis, e se o `server.py` está presente e a correr no diretório correto. Reiniciar ambos pode ajudar.

4. **Erros SerpAPI**
   - Ver o erro `Search API returned error status: 401` significa que a sua chave SerpAPI está em falta, incorreta ou expirada. Vá ao seu painel SerpAPI, verifique a chave e atualize o ficheiro `.env` se necessário. Se a chave estiver correta mas o erro persistir, verifique se o seu plano gratuito não esgotou a quota.

### Modo de Depuração

Por defeito, a aplicação regista apenas informação importante. Se quiser ver mais detalhes sobre o que está a acontecer (por exemplo, para diagnosticar problemas difíceis), pode ativar o modo DEBUG. Isto vai mostrar muito mais sobre cada passo que a aplicação está a executar.

**Exemplo: Saída Normal**
```plaintext
2025-06-01 10:15:23,456 - __main__ - INFO - Calling general_search with params: {'query': 'open source LLMs'}
2025-06-01 10:15:24,123 - __main__ - INFO - Successfully called general_search

GENERAL_SEARCH RESULTS:
... (search results here) ...
```

**Exemplo: Saída DEBUG**
```plaintext
2025-06-01 10:15:23,456 - __main__ - INFO - Calling general_search with params: {'query': 'open source LLMs'}
2025-06-01 10:15:23,457 - httpx - DEBUG - HTTP Request: GET https://serpapi.com/search ...
2025-06-01 10:15:23,458 - httpx - DEBUG - HTTP Response: 200 OK ...
2025-06-01 10:15:24,123 - __main__ - INFO - Successfully called general_search

GENERAL_SEARCH RESULTS:
... (search results here) ...
```

Repare como o modo DEBUG inclui linhas extra sobre pedidos HTTP, respostas e outros detalhes internos. Isto pode ser muito útil para resolução de problemas.
Para ativar o modo DEBUG, defina o nível de logging para DEBUG no início do seu `client.py` ou `server.py`:

# [Python](../../../../05-AdvancedTopics/web-search-mcp)

```python
# At the top of your client.py or server.py
import logging
logging.basicConfig(
    level=logging.DEBUG,  # Change from INFO to DEBUG
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
```

---

---

## O que vem a seguir

- [5.10 Streaming em Tempo Real](../mcp-realtimestreaming/README.md)

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, por favor tenha em conta que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes da utilização desta tradução.