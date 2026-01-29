# Implementação Python do Model Context Protocol (MCP)

Este repositório contém uma implementação em Python do Model Context Protocol (MCP), demonstrando como criar uma aplicação servidor e cliente que comunicam usando o padrão MCP.

## Visão Geral

A implementação do MCP consiste em dois componentes principais:

1. **Servidor MCP (`server.py`)** - Um servidor que expõe:
   - **Ferramentas**: Funções que podem ser chamadas remotamente
   - **Recursos**: Dados que podem ser obtidos
   - **Prompts**: Modelos para gerar prompts para modelos de linguagem

2. **Cliente MCP (`client.py`)** - Uma aplicação cliente que se conecta ao servidor e utiliza as suas funcionalidades

## Funcionalidades

Esta implementação demonstra várias funcionalidades chave do MCP:

### Ferramentas
- `completion` - Gera textos completados a partir de modelos de IA (simulado)
- `add` - Calculadora simples que soma dois números

### Recursos
- `models://` - Retorna informações sobre os modelos de IA disponíveis
- `greeting://{name}` - Retorna uma saudação personalizada para um nome dado

### Prompts
- `review_code` - Gera um prompt para revisão de código

## Instalação

Para usar esta implementação do MCP, instale os pacotes necessários:

```powershell
pip install mcp-server mcp-client
```

## Executar o Servidor e o Cliente

### Iniciar o Servidor

Execute o servidor numa janela de terminal:

```powershell
python server.py
```

O servidor também pode ser executado em modo de desenvolvimento usando o MCP CLI:

```powershell
mcp dev server.py
```

Ou instalado no Claude Desktop (se disponível):

```powershell
mcp install server.py
```

### Executar o Cliente

Execute o cliente noutra janela de terminal:

```powershell
python client.py
```

Isto irá conectar ao servidor e demonstrar todas as funcionalidades disponíveis.

### Uso do Cliente

O cliente (`client.py`) demonstra todas as capacidades do MCP:

```powershell
python client.py
```

Isto irá conectar ao servidor e utilizar todas as funcionalidades, incluindo ferramentas, recursos e prompts. A saída mostrará:

1. Resultado da ferramenta calculadora (5 + 7 = 12)
2. Resposta da ferramenta completion para "Qual é o significado da vida?"
3. Lista dos modelos de IA disponíveis
4. Saudação personalizada para "MCP Explorer"
5. Modelo de prompt para revisão de código

## Detalhes da Implementação

O servidor é implementado usando a API `FastMCP`, que fornece abstrações de alto nível para definir serviços MCP. Aqui está um exemplo simplificado de como as ferramentas são definidas:

```python
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers together
    
    Args:
        a: First number
        b: Second number
    
    Returns:
        The sum of the two numbers
    """
    logger.info(f"Adding {a} and {b}")
    return a + b
```

O cliente usa a biblioteca cliente MCP para se conectar e chamar o servidor:

```python
async with stdio_client(server_params) as (reader, writer):
    async with ClientSession(reader, writer) as session:
        await session.initialize()
        result = await session.call_tool("add", arguments={"a": 5, "b": 7})
```

## Saiba Mais

Para mais informações sobre o MCP, visite: https://modelcontextprotocol.io/

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos por garantir a precisão, por favor tenha em conta que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se a tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes da utilização desta tradução.