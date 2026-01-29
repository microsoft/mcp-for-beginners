## Testes e Depuração

Antes de começar a testar seu servidor MCP, é importante entender as ferramentas disponíveis e as melhores práticas para depuração. Testes eficazes garantem que seu servidor funcione conforme o esperado e ajudam a identificar e resolver problemas rapidamente. A seção a seguir apresenta abordagens recomendadas para validar sua implementação MCP.

## Visão Geral

Esta lição aborda como escolher a abordagem de teste correta e a ferramenta de teste mais eficaz.

## Objetivos de Aprendizagem

Ao final desta lição, você será capaz de:

- Descrever várias abordagens para testes.
- Usar diferentes ferramentas para testar seu código de forma eficaz.

## Testando Servidores MCP

O MCP oferece ferramentas para ajudar a testar e depurar seus servidores:

- **MCP Inspector**: Uma ferramenta de linha de comando que pode ser usada tanto como CLI quanto como ferramenta visual.
- **Teste manual**: Você pode usar uma ferramenta como curl para executar requisições web, mas qualquer ferramenta capaz de fazer requisições HTTP serve.
- **Teste unitário**: É possível usar seu framework de testes preferido para testar as funcionalidades tanto do servidor quanto do cliente.

### Usando o MCP Inspector

Já descrevemos o uso dessa ferramenta em lições anteriores, mas vamos falar um pouco sobre ela em um nível mais geral. É uma ferramenta construída em Node.js e você pode usá-la executando o comando `npx`, que baixa e instala a ferramenta temporariamente e a remove após executar sua requisição.

O [MCP Inspector](https://github.com/modelcontextprotocol/inspector) ajuda você a:

- **Descobrir Capacidades do Servidor**: Detecta automaticamente recursos, ferramentas e prompts disponíveis
- **Testar Execução de Ferramentas**: Experimente diferentes parâmetros e veja as respostas em tempo real
- **Visualizar Metadados do Servidor**: Examine informações do servidor, esquemas e configurações

Uma execução típica da ferramenta é assim:

```bash
npx @modelcontextprotocol/inspector node build/index.js
```

O comando acima inicia um MCP e sua interface visual, abrindo uma interface web local no seu navegador. Você verá um painel exibindo seus servidores MCP registrados, suas ferramentas, recursos e prompts disponíveis. A interface permite testar a execução das ferramentas de forma interativa, inspecionar metadados do servidor e visualizar respostas em tempo real, facilitando a validação e depuração das implementações do seu servidor MCP.

Veja como pode ser: ![Inspector](../../../../translated_images/pt-BR/connect.141db0b2bd05f096fb1dd91273771fd8b2469d6507656c3b0c9df4b3c5473929.png)

Você também pode executar essa ferramenta no modo CLI, adicionando o atributo `--cli`. Aqui está um exemplo de execução no modo "CLI" que lista todas as ferramentas do servidor:

```sh
npx @modelcontextprotocol/inspector --cli node build/index.js --method tools/list
```

### Teste Manual

Além de usar o inspector para testar as capacidades do servidor, outra abordagem semelhante é usar um cliente capaz de fazer requisições HTTP, como o curl.

Com o curl, você pode testar servidores MCP diretamente usando requisições HTTP:

```bash
# Example: Test server metadata
curl http://localhost:3000/v1/metadata

# Example: Execute a tool
curl -X POST http://localhost:3000/v1/tools/execute \
  -H "Content-Type: application/json" \
  -d '{"name": "calculator", "parameters": {"expression": "2+2"}}'
```

Como você pode ver no exemplo acima com curl, você usa uma requisição POST para invocar uma ferramenta, enviando um payload com o nome da ferramenta e seus parâmetros. Use a abordagem que for mais conveniente para você. Ferramentas CLI geralmente são mais rápidas e podem ser automatizadas, o que é útil em ambientes de CI/CD.

### Teste Unitário

Crie testes unitários para suas ferramentas e recursos para garantir que funcionem conforme esperado. Aqui está um exemplo de código de teste.

```python
import pytest

from mcp.server.fastmcp import FastMCP
from mcp.shared.memory import (
    create_connected_server_and_client_session as create_session,
)

# Mark the whole module for async tests
pytestmark = pytest.mark.anyio


async def test_list_tools_cursor_parameter():
    """Test that the cursor parameter is accepted for list_tools.

    Note: FastMCP doesn't currently implement pagination, so this test
    only verifies that the cursor parameter is accepted by the client.
    """

 server = FastMCP("test")

    # Create a couple of test tools
    @server.tool(name="test_tool_1")
    async def test_tool_1() -> str:
        """First test tool"""
        return "Result 1"

    @server.tool(name="test_tool_2")
    async def test_tool_2() -> str:
        """Second test tool"""
        return "Result 2"

    async with create_session(server._mcp_server) as client_session:
        # Test without cursor parameter (omitted)
        result1 = await client_session.list_tools()
        assert len(result1.tools) == 2

        # Test with cursor=None
        result2 = await client_session.list_tools(cursor=None)
        assert len(result2.tools) == 2

        # Test with cursor as string
        result3 = await client_session.list_tools(cursor="some_cursor_value")
        assert len(result3.tools) == 2

        # Test with empty string cursor
        result4 = await client_session.list_tools(cursor="")
        assert len(result4.tools) == 2
    
```

O código acima faz o seguinte:

- Utiliza o framework pytest, que permite criar testes como funções e usar declarações assert.
- Cria um servidor MCP com duas ferramentas diferentes.
- Usa a declaração `assert` para verificar se certas condições são atendidas.

Confira o [arquivo completo aqui](https://github.com/modelcontextprotocol/python-sdk/blob/main/tests/client/test_list_methods_cursor.py)

Com base nesse arquivo, você pode testar seu próprio servidor para garantir que as capacidades sejam criadas corretamente.

Todos os principais SDKs possuem seções de teste semelhantes, então você pode adaptar para o runtime que escolher.

## Exemplos

- [Java Calculator](../samples/java/calculator/README.md)
- [.Net Calculator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Calculator](../samples/javascript/README.md)
- [TypeScript Calculator](../samples/typescript/README.md)
- [Python Calculator](../../../../03-GettingStarted/samples/python)

## Recursos Adicionais

- [Python SDK](https://github.com/modelcontextprotocol/python-sdk)

## Próximos Passos

- Próximo: [Deployment](../09-deployment/README.md)

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.