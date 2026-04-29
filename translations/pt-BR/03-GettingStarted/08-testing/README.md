## Testando e Depurando

Antes de começar a testar seu servidor MCP, é importante entender as ferramentas disponíveis e as melhores práticas para depuração. Testes eficazes garantem que seu servidor se comporte conforme o esperado e ajudam a identificar e resolver problemas rapidamente. A seção a seguir descreve abordagens recomendadas para validar sua implementação MCP.

## Visão Geral

Esta lição aborda como selecionar a abordagem de teste correta e a ferramenta de teste mais eficaz.

## Objetivos de Aprendizagem

Ao final desta lição, você será capaz de:

- Descrever várias abordagens para testes.
- Usar diferentes ferramentas para testar seu código de forma eficaz.

## Testando Servidores MCP

O MCP fornece ferramentas para ajudá-lo a testar e depurar seus servidores:

- **MCP Inspector**: Uma ferramenta de linha de comando que pode ser usada tanto como ferramenta CLI quanto como ferramenta visual.
- **Teste manual**: Você pode usar uma ferramenta como o curl para executar requisições web, mas qualquer ferramenta capaz de executar HTTP serve.
- **Teste unitário**: É possível usar sua estrutura de teste preferida para testar recursos tanto do servidor quanto do cliente.

### Usando o MCP Inspector

Já descrevemos o uso desta ferramenta em lições anteriores, mas vamos falar um pouco sobre ela em alto nível. É uma ferramenta construída em Node.js e você pode usá-la chamando o executável `npx`, que irá baixar e instalar a ferramenta temporariamente e limpará tudo quando terminar de executar sua requisição.

O [MCP Inspector](https://github.com/modelcontextprotocol/inspector) ajuda você a:

- **Descobrir Capacidades do Servidor**: Detectar automaticamente recursos, ferramentas e prompts disponíveis
- **Testar Execução de Ferramentas**: Experimentar diferentes parâmetros e ver respostas em tempo real
- **Visualizar Metadados do Servidor**: Examinar informações do servidor, esquemas e configurações

Uma execução típica da ferramenta se parece com isto:

```bash
npx @modelcontextprotocol/inspector node build/index.js
```

O comando acima inicia um MCP e sua interface visual e lança uma interface web local no seu navegador. Você pode esperar ver um painel exibindo seus servidores MCP registrados, suas ferramentas, recursos e prompts disponíveis. A interface permite que você teste a execução de ferramentas de forma interativa, inspecione metadados do servidor e visualize respostas em tempo real, facilitando a validação e depuração das implementações do seu servidor MCP.

Aqui está como pode ser: ![Inspector](../../../../translated_images/pt-BR/connect.141db0b2bd05f096.webp)

Você também pode executar esta ferramenta no modo CLI, caso em que adiciona o atributo `--cli`. Aqui está um exemplo de execução da ferramenta no modo "CLI", que lista todas as ferramentas no servidor:

```sh
npx @modelcontextprotocol/inspector --cli node build/index.js --method tools/list
```

### Teste Manual

Além de executar a ferramenta inspector para testar capacidades do servidor, outra abordagem semelhante é rodar um cliente capaz de usar HTTP, como por exemplo o curl.

Com curl, você pode testar diretamente servidores MCP usando requisições HTTP:

```bash
# Exemplo: Metadados do servidor de teste
curl http://localhost:3000/v1/metadata

# Exemplo: Executar uma ferramenta
curl -X POST http://localhost:3000/v1/tools/execute \
  -H "Content-Type: application/json" \
  -d '{"name": "calculator", "parameters": {"expression": "2+2"}}'
```

Como você pode observar no uso do curl acima, você utiliza uma requisição POST para invocar uma ferramenta usando um payload consistindo no nome da ferramenta e seus parâmetros. Use a abordagem que melhor se encaixar para você. Ferramentas CLI, em geral, tendem a ser mais rápidas para usar e se prestam a serem automatizadas via scripts, o que pode ser útil em um ambiente CI/CD.

### Testes Unitários

Crie testes unitários para suas ferramentas e recursos para garantir que funcionem conforme o esperado. Aqui está um exemplo de código de teste.

```python
import pytest

from mcp.server.fastmcp import FastMCP
from mcp.shared.memory import (
    create_connected_server_and_client_session as create_session,
)

# Marque todo o módulo para testes assíncronos
pytestmark = pytest.mark.anyio


async def test_list_tools_cursor_parameter():
    """Test that the cursor parameter is accepted for list_tools.

    Note: FastMCP doesn't currently implement pagination, so this test
    only verifies that the cursor parameter is accepted by the client.
    """

 server = FastMCP("test")

    # Crie algumas ferramentas de teste
    @server.tool(name="test_tool_1")
    async def test_tool_1() -> str:
        """First test tool"""
        return "Result 1"

    @server.tool(name="test_tool_2")
    async def test_tool_2() -> str:
        """Second test tool"""
        return "Result 2"

    async with create_session(server._mcp_server) as client_session:
        # Teste sem o parâmetro cursor (omitido)
        result1 = await client_session.list_tools()
        assert len(result1.tools) == 2

        # Teste com cursor=None
        result2 = await client_session.list_tools(cursor=None)
        assert len(result2.tools) == 2

        # Teste com cursor como string
        result3 = await client_session.list_tools(cursor="some_cursor_value")
        assert len(result3.tools) == 2

        # Teste com cursor de string vazia
        result4 = await client_session.list_tools(cursor="")
        assert len(result4.tools) == 2
    
```

O código acima faz o seguinte:

- Utiliza o framework pytest, que permite criar testes como funções e usar expressões assert.
- Cria um Servidor MCP com duas ferramentas diferentes.
- Usa a instrução `assert` para verificar se certas condições são atendidas.

Dê uma olhada no [arquivo completo aqui](https://github.com/modelcontextprotocol/python-sdk/blob/main/tests/client/test_list_methods_cursor.py)

Com base no arquivo acima, você pode testar seu próprio servidor para garantir que as capacidades sejam criadas corretamente.

Todos os SDKs principais possuem seções de teste similares, então você pode ajustar para o runtime escolhido.

## Exemplos

- [Calculadora Java](../samples/java/calculator/README.md)
- [Calculadora .Net](../../../../03-GettingStarted/samples/csharp)
- [Calculadora JavaScript](../samples/javascript/README.md)
- [Calculadora TypeScript](../samples/typescript/README.md)
- [Calculadora Python](../../../../03-GettingStarted/samples/python)

## Recursos Adicionais

- [Python SDK](https://github.com/modelcontextprotocol/python-sdk)

## O Que Vem a Seguir

- Próximo: [Deploy](../09-deployment/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para a precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original em sua língua nativa deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se a tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->