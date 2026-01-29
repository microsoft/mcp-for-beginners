# Aula: Construindo um Servidor MCP de Busca na Web

Este capítulo mostra como construir um agente de IA real que integra APIs externas, lida com diversos tipos de dados, gerencia erros e orquestra múltiplas ferramentas — tudo em um formato pronto para produção. Você verá:

- **Integração com APIs externas que exigem autenticação**
- **Manipulação de diversos tipos de dados de múltiplos endpoints**
- **Estratégias robustas de tratamento de erros e registro de logs**
- **Orquestração de múltiplas ferramentas em um único servidor**

Ao final, você terá experiência prática com padrões e boas práticas essenciais para aplicações avançadas de IA e LLM.

## Introdução

Nesta aula, você aprenderá a construir um servidor e cliente MCP avançados que estendem as capacidades do LLM com dados da web em tempo real usando SerpAPI. Esta é uma habilidade fundamental para desenvolver agentes de IA dinâmicos que podem acessar informações atualizadas da web.

## Objetivos de Aprendizagem

Ao final desta aula, você será capaz de:

- Integrar APIs externas (como SerpAPI) de forma segura em um servidor MCP
- Implementar múltiplas ferramentas para busca na web, notícias, produtos e perguntas e respostas
- Analisar e formatar dados estruturados para consumo do LLM
- Tratar erros e gerenciar limites de taxa das APIs de forma eficaz
- Construir e testar clientes MCP automatizados e interativos

## Servidor MCP de Busca na Web

Esta seção apresenta a arquitetura e funcionalidades do Servidor MCP de Busca na Web. Você verá como FastMCP e SerpAPI são usados juntos para estender as capacidades do LLM com dados da web em tempo real.

### Visão Geral

Esta implementação conta com quatro ferramentas que demonstram a capacidade do MCP de lidar com tarefas diversas, baseadas em APIs externas, de forma segura e eficiente:

- **general_search**: Para resultados amplos na web
- **news_search**: Para manchetes recentes
- **product_search**: Para dados de comércio eletrônico
- **qna**: Para trechos de perguntas e respostas

### Funcionalidades
- **Exemplos de Código**: Inclui blocos de código específicos para Python (e facilmente extensível para outras linguagens) usando pivôs de código para clareza

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

Antes de rodar o cliente, é útil entender o que o servidor faz. O arquivo [`server.py`](../../../../05-AdvancedTopics/web-search-mcp/server.py) implementa o servidor MCP, expondo ferramentas para busca na web, notícias, produtos e Q&A integrando com SerpAPI. Ele trata requisições recebidas, gerencia chamadas à API, analisa respostas e retorna resultados estruturados para o cliente.

Você pode revisar a implementação completa em [`server.py`](../../../../05-AdvancedTopics/web-search-mcp/server.py).

Aqui está um exemplo breve de como o servidor define e registra uma ferramenta:

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

- **Integração com API Externa**: Demonstra o manejo seguro de chaves de API e requisições externas
- **Análise de Dados Estruturados**: Mostra como transformar respostas da API em formatos amigáveis para LLM
- **Tratamento de Erros**: Tratamento robusto de erros com registro de logs apropriado
- **Cliente Interativo**: Inclui testes automatizados e modo interativo para testes
- **Gerenciamento de Contexto**: Utiliza MCP Context para registro e rastreamento de requisições

## Pré-requisitos

Antes de começar, certifique-se de que seu ambiente está configurado corretamente seguindo estes passos. Isso garantirá que todas as dependências estejam instaladas e suas chaves de API configuradas para um desenvolvimento e testes sem problemas.

- Python 3.8 ou superior
- Chave da API SerpAPI (Cadastre-se em [SerpAPI](https://serpapi.com/) - plano gratuito disponível)

## Instalação

Para começar, siga estes passos para configurar seu ambiente:

1. Instale as dependências usando uv (recomendado) ou pip:

```bash
# Using uv (recommended)
uv pip install -r requirements.txt

# Using pip
pip install -r requirements.txt
```

2. Crie um arquivo `.env` na raiz do projeto com sua chave SerpAPI:

```
SERPAPI_KEY=your_serpapi_key_here
```

## Uso

O Servidor MCP de Busca na Web é o componente central que expõe ferramentas para busca na web, notícias, produtos e Q&A integrando com SerpAPI. Ele trata requisições recebidas, gerencia chamadas à API, analisa respostas e retorna resultados estruturados para o cliente.

Você pode revisar a implementação completa em [`server.py`](../../../../05-AdvancedTopics/web-search-mcp/server.py).

### Executando o Servidor

Para iniciar o servidor MCP, use o seguinte comando:

```bash
python server.py
```

O servidor rodará como um servidor MCP baseado em stdio, ao qual o cliente pode se conectar diretamente.

### Modos do Cliente

O cliente (`client.py`) suporta dois modos para interagir com o servidor MCP:

- **Modo normal**: Executa testes automatizados que exercitam todas as ferramentas e verificam suas respostas. Útil para checar rapidamente se o servidor e as ferramentas estão funcionando como esperado.
- **Modo interativo**: Inicia uma interface baseada em menu onde você pode selecionar e chamar ferramentas manualmente, inserir consultas personalizadas e ver os resultados em tempo real. Ideal para explorar as capacidades do servidor e experimentar diferentes entradas.

Você pode revisar a implementação completa em [`client.py`](../../../../05-AdvancedTopics/web-search-mcp/client.py).

### Executando o Cliente

Para rodar os testes automatizados (isso iniciará o servidor automaticamente):

```bash
python client.py
```

Ou rode no modo interativo:

```bash
python client.py --interactive
```

### Testando com Diferentes Métodos

Existem várias formas de testar e interagir com as ferramentas fornecidas pelo servidor, dependendo das suas necessidades e fluxo de trabalho.

#### Escrevendo Scripts de Teste Personalizados com o MCP Python SDK
Você também pode criar seus próprios scripts de teste usando o MCP Python SDK:

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

Neste contexto, um "script de teste" significa um programa Python personalizado que você escreve para atuar como cliente do servidor MCP. Em vez de ser um teste unitário formal, esse script permite que você conecte programaticamente ao servidor, chame qualquer uma das ferramentas com os parâmetros que escolher e inspecione os resultados. Essa abordagem é útil para:
- Prototipar e experimentar chamadas às ferramentas
- Validar como o servidor responde a diferentes entradas
- Automatizar invocações repetidas das ferramentas
- Construir seus próprios fluxos de trabalho ou integrações sobre o servidor MCP

Você pode usar scripts de teste para experimentar novas consultas rapidamente, depurar o comportamento das ferramentas ou até como ponto de partida para automações mais avançadas. Abaixo está um exemplo de como usar o MCP Python SDK para criar tal script:

## Descrições das Ferramentas

Você pode usar as seguintes ferramentas fornecidas pelo servidor para realizar diferentes tipos de buscas e consultas. Cada ferramenta é descrita abaixo com seus parâmetros e exemplos de uso.

Esta seção fornece detalhes sobre cada ferramenta disponível e seus parâmetros.

### general_search

Realiza uma busca geral na web e retorna resultados formatados.

**Como chamar esta ferramenta:**

Você pode chamar `general_search` a partir do seu próprio script usando o MCP Python SDK, ou interativamente usando o Inspector ou o modo interativo do cliente. Aqui está um exemplo de código usando o SDK:

# [Exemplo em Python](../../../../05-AdvancedTopics/web-search-mcp)

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

Alternativamente, no modo interativo, selecione `general_search` no menu e insira sua consulta quando solicitado.

**Parâmetros:**
- `query` (string): A consulta de busca

**Exemplo de Requisição:**

```json
{
  "query": "latest AI trends"
}
```

### news_search

Busca por notícias recentes relacionadas a uma consulta.

**Como chamar esta ferramenta:**

Você pode chamar `news_search` a partir do seu próprio script usando o MCP Python SDK, ou interativamente usando o Inspector ou o modo interativo do cliente. Aqui está um exemplo de código usando o SDK:

# [Exemplo em Python](../../../../05-AdvancedTopics/web-search-mcp)

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

Alternativamente, no modo interativo, selecione `news_search` no menu e insira sua consulta quando solicitado.

**Parâmetros:**
- `query` (string): A consulta de busca

**Exemplo de Requisição:**

```json
{
  "query": "AI policy updates"
}
```

### product_search

Busca por produtos que correspondam a uma consulta.

**Como chamar esta ferramenta:**

Você pode chamar `product_search` a partir do seu próprio script usando o MCP Python SDK, ou interativamente usando o Inspector ou o modo interativo do cliente. Aqui está um exemplo de código usando o SDK:

# [Exemplo em Python](../../../../05-AdvancedTopics/web-search-mcp)

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

Alternativamente, no modo interativo, selecione `product_search` no menu e insira sua consulta quando solicitado.

**Parâmetros:**
- `query` (string): A consulta de busca de produtos

**Exemplo de Requisição:**

```json
{
  "query": "best AI gadgets 2025"
}
```

### qna

Obtém respostas diretas para perguntas a partir de motores de busca.

**Como chamar esta ferramenta:**

Você pode chamar `qna` a partir do seu próprio script usando o MCP Python SDK, ou interativamente usando o Inspector ou o modo interativo do cliente. Aqui está um exemplo de código usando o SDK:

# [Exemplo em Python](../../../../05-AdvancedTopics/web-search-mcp)

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

Alternativamente, no modo interativo, selecione `qna` no menu e insira sua pergunta quando solicitado.

**Parâmetros:**
- `question` (string): A pergunta para a qual deseja encontrar uma resposta

**Exemplo de Requisição:**

```json
{
  "question": "what is artificial intelligence"
}
```

## Detalhes do Código

Esta seção fornece trechos de código e referências para as implementações do servidor e cliente.

# [Python](../../../../05-AdvancedTopics/web-search-mcp)

Veja [`server.py`](../../../../05-AdvancedTopics/web-search-mcp/server.py) e [`client.py`](../../../../05-AdvancedTopics/web-search-mcp/client.py) para detalhes completos da implementação.

```python
# Example snippet from server.py:
import os
import httpx
# ...existing code...
```

---

## Conceitos Avançados Nesta Aula

Antes de começar a construir, aqui estão alguns conceitos avançados importantes que aparecerão ao longo deste capítulo. Entendê-los ajudará você a acompanhar, mesmo que sejam novos para você:

- **Orquestração Multi-ferramentas**: Significa rodar várias ferramentas diferentes (como busca na web, notícias, produtos e Q&A) dentro de um único servidor MCP. Isso permite que seu servidor lide com uma variedade de tarefas, não apenas uma.
- **Gerenciamento de Limites de Taxa da API**: Muitas APIs externas (como SerpAPI) limitam quantas requisições você pode fazer em determinado tempo. Um bom código verifica esses limites e os trata de forma elegante, para que seu app não quebre se atingir um limite.
- **Análise de Dados Estruturados**: Respostas de APIs costumam ser complexas e aninhadas. Esse conceito trata de transformar essas respostas em formatos limpos e fáceis de usar, amigáveis para LLMs ou outros programas.
- **Recuperação de Erros**: Às vezes algo dá errado — talvez a rede falhe, ou a API não retorne o esperado. Recuperação de erros significa que seu código pode lidar com esses problemas e ainda fornecer feedback útil, em vez de travar.
- **Validação de Parâmetros**: Trata-se de verificar se todas as entradas para suas ferramentas estão corretas e seguras para uso. Inclui definir valores padrão e garantir que os tipos estejam corretos, o que ajuda a evitar bugs e confusões.

Esta seção ajudará você a diagnosticar e resolver problemas comuns que pode encontrar ao trabalhar com o Servidor MCP de Busca na Web. Se você encontrar erros ou comportamentos inesperados, esta seção de solução de problemas oferece soluções para os problemas mais comuns. Revise estas dicas antes de buscar ajuda adicional — elas frequentemente resolvem problemas rapidamente.

## Solução de Problemas

Ao trabalhar com o Servidor MCP de Busca na Web, você pode eventualmente encontrar problemas — isso é normal ao desenvolver com APIs externas e novas ferramentas. Esta seção oferece soluções práticas para os problemas mais comuns, para que você possa voltar ao trabalho rapidamente. Se encontrar um erro, comece por aqui: as dicas abaixo abordam os problemas que a maioria dos usuários enfrenta e muitas vezes resolvem seu problema sem ajuda extra.

### Problemas Comuns

Abaixo estão alguns dos problemas mais frequentes que os usuários encontram, com explicações claras e passos para resolvê-los:

1. **Falta da variável SERPAPI_KEY no arquivo .env**
   - Se você vir o erro `SERPAPI_KEY environment variable not found`, significa que sua aplicação não consegue encontrar a chave da API necessária para acessar o SerpAPI. Para corrigir, crie um arquivo chamado `.env` na raiz do seu projeto (se ainda não existir) e adicione uma linha como `SERPAPI_KEY=sua_chave_serpapi_aqui`. Certifique-se de substituir `sua_chave_serpapi_aqui` pela sua chave real do site do SerpAPI.

2. **Erros de módulo não encontrado**
   - Erros como `ModuleNotFoundError: No module named 'httpx'` indicam que um pacote Python necessário está faltando. Isso geralmente acontece se você não instalou todas as dependências. Para resolver, execute `pip install -r requirements.txt` no seu terminal para instalar tudo que seu projeto precisa.

3. **Problemas de conexão**
   - Se você receber um erro como `Error during client execution`, isso geralmente significa que o cliente não consegue se conectar ao servidor, ou o servidor não está rodando como esperado. Verifique se o cliente e o servidor são versões compatíveis, e se o `server.py` está presente e rodando no diretório correto. Reiniciar ambos também pode ajudar.

4. **Erros do SerpAPI**
   - Ver mensagens como `Search API returned error status: 401` indicam que sua chave SerpAPI está faltando, incorreta ou expirada. Acesse seu painel do SerpAPI, verifique sua chave e atualize seu arquivo `.env` se necessário. Se a chave estiver correta mas o erro persistir, confira se seu plano gratuito não esgotou a cota.

### Modo de Depuração

Por padrão, o app registra apenas informações importantes. Se quiser ver mais detalhes sobre o que está acontecendo (por exemplo, para diagnosticar problemas difíceis), você pode ativar o modo DEBUG. Isso mostrará muito mais sobre cada passo que o app está executando.

**Exemplo: Saída Normal**
```plaintext
2025-06-01 10:15:23,456 - __main__ - INFO - Calling general_search with params: {'query': 'open source LLMs'}
2025-06-01 10:15:24,123 - __main__ - INFO - Successfully called general_search

GENERAL_SEARCH RESULTS:
... (search results here) ...
```

**Exemplo: Saída em DEBUG**
```plaintext
2025-06-01 10:15:23,456 - __main__ - INFO - Calling general_search with params: {'query': 'open source LLMs'}
2025-06-01 10:15:23,457 - httpx - DEBUG - HTTP Request: GET https://serpapi.com/search ...
2025-06-01 10:15:23,458 - httpx - DEBUG - HTTP Response: 200 OK ...
2025-06-01 10:15:24,123 - __main__ - INFO - Successfully called general_search

GENERAL_SEARCH RESULTS:
... (search results here) ...
```

Note como o modo DEBUG inclui linhas extras sobre requisições HTTP, respostas e outros detalhes internos. Isso pode ser muito útil para solução de problemas.
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
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.