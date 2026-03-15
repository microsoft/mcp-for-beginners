## Testes e Depuração

Antes de começar a testar o seu servidor MCP, é importante compreender as ferramentas disponíveis e as melhores práticas para a depuração. Testes eficazes garantem que o seu servidor se comporta como esperado e ajudam a identificar e resolver rapidamente problemas. A secção seguinte descreve as abordagens recomendadas para validar a sua implementação MCP.

## Visão Geral

Esta lição abrange como selecionar a abordagem de teste correta e a ferramenta de teste mais eficaz.

## Objetivos de Aprendizagem

No final desta lição, será capaz de:

- Descrever várias abordagens para testar.
- Utilizar diferentes ferramentas para testar o seu código eficazmente.


## Testar Servidores MCP

O MCP fornece ferramentas para ajudar a testar e depurar os seus servidores:

- **MCP Inspector**: Uma ferramenta de linha de comandos que pode ser executada tanto como ferramenta CLI como visual.
- **Teste manual**: Pode usar uma ferramenta como o curl para executar pedidos web, mas qualquer ferramenta capaz de executar HTTP serve.
- **Testes unitários**: É possível usar o seu framework de testes preferido para testar as funcionalidades tanto do servidor como do cliente.

### Utilizar o MCP Inspector

Descrevemos o uso desta ferramenta em lições anteriores, mas vamos falar um pouco a nível geral. É uma ferramenta construída em Node.js e pode usá-la invocando o executável `npx`, que irá descarregar e instalar temporariamente a própria ferramenta e limpar-se após executar o seu pedido.

O [MCP Inspector](https://github.com/modelcontextprotocol/inspector) ajuda a:

- **Descobrir Capacidades do Servidor**: Detetar automaticamente recursos, ferramentas e prompts disponíveis
- **Testar a Execução de Ferramentas**: Experimentar diferentes parâmetros e ver respostas em tempo real
- **Visualizar Metadados do Servidor**: Examinar info do servidor, esquemas e configurações

Uma execução típica da ferramenta é assim:

```bash
npx @modelcontextprotocol/inspector node build/index.js
```

O comando acima inicia um MCP e a sua interface visual e lança uma interface web local no seu navegador. Pode esperar ver um painel a exibir os seus servidores MCP registados, as suas ferramentas, recursos e prompts disponíveis. A interface permite-lhe testar interativamente a execução das ferramentas, inspecionar metadados do servidor e ver respostas em tempo real, tornando mais fácil validar e depurar as implementações do seu servidor MCP.

Isto é o aspeto que pode ter: ![Inspector](../../../../translated_images/pt-PT/connect.141db0b2bd05f096.webp)

Também pode executar esta ferramenta em modo CLI, caso em que adiciona o atributo `--cli`. Aqui está um exemplo de execução da ferramenta em modo "CLI" que lista todas as ferramentas no servidor:

```sh
npx @modelcontextprotocol/inspector --cli node build/index.js --method tools/list
```

### Teste Manual

Para além de executar a ferramenta inspector para testar as capacidades do servidor, outra abordagem semelhante é executar um cliente capaz de usar HTTP, como por exemplo o curl.

Com o curl, pode testar servidores MCP diretamente usando pedidos HTTP:

```bash
# Exemplo: Metadados do servidor de teste
curl http://localhost:3000/v1/metadata

# Exemplo: Executar uma ferramenta
curl -X POST http://localhost:3000/v1/tools/execute \
  -H "Content-Type: application/json" \
  -d '{"name": "calculator", "parameters": {"expression": "2+2"}}'
```

Como pode ver no exemplo acima do uso do curl, usa um pedido POST para invocar uma ferramenta usando um payload que consiste no nome da ferramenta e os seus parâmetros. Use a abordagem que for melhor para si. Ferramentas CLI em geral tendem a ser mais rápidas de usar e prestam-se a serem automatizadas, o que pode ser útil num ambiente CI/CD.

### Testes Unitários

Crie testes unitários para as suas ferramentas e recursos para garantir que funcionam como esperado. Aqui está algum código de exemplo para testes.

```python
import pytest

from mcp.server.fastmcp import FastMCP
from mcp.shared.memory import (
    create_connected_server_and_client_session as create_session,
)

# Marcar todo o módulo para testes assíncronos
pytestmark = pytest.mark.anyio


async def test_list_tools_cursor_parameter():
    """Test that the cursor parameter is accepted for list_tools.

    Note: FastMCP doesn't currently implement pagination, so this test
    only verifies that the cursor parameter is accepted by the client.
    """

 server = FastMCP("test")

    # Criar um par de ferramentas de teste
    @server.tool(name="test_tool_1")
    async def test_tool_1() -> str:
        """First test tool"""
        return "Result 1"

    @server.tool(name="test_tool_2")
    async def test_tool_2() -> str:
        """Second test tool"""
        return "Result 2"

    async with create_session(server._mcp_server) as client_session:
        # Testar sem parâmetro cursor (omitido)
        result1 = await client_session.list_tools()
        assert len(result1.tools) == 2

        # Testar com cursor=None
        result2 = await client_session.list_tools(cursor=None)
        assert len(result2.tools) == 2

        # Testar com cursor como string
        result3 = await client_session.list_tools(cursor="some_cursor_value")
        assert len(result3.tools) == 2

        # Testar com cursor como string vazia
        result4 = await client_session.list_tools(cursor="")
        assert len(result4.tools) == 2
    
```

O código anterior faz o seguinte:

- Utiliza o framework pytest que permite criar testes como funções e usar declarações assert.
- Cria um Servidor MCP com duas ferramentas diferentes.
- Usa a instrução `assert` para verificar que certas condições estão cumpridas.

Consulte o [ficheiro completo aqui](https://github.com/modelcontextprotocol/python-sdk/blob/main/tests/client/test_list_methods_cursor.py)

Dado o ficheiro acima, pode testar o seu próprio servidor para assegurar que as capacidades são criadas como devem ser.

Todos os SDKs principais têm secções de teste similares para que possa adaptar ao seu runtime escolhido.

## Exemplos 

- [Calculadora Java](../samples/java/calculator/README.md)
- [Calculadora .Net](../../../../03-GettingStarted/samples/csharp)
- [Calculadora JavaScript](../samples/javascript/README.md)
- [Calculadora TypeScript](../samples/typescript/README.md)
- [Calculadora Python](../../../../03-GettingStarted/samples/python) 

## Recursos Adicionais

- [SDK Python](https://github.com/modelcontextprotocol/python-sdk)

## O que Vem a Seguir

- A seguir: [Desdobramento](../09-deployment/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos por garantir a precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se a tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações erradas decorrentes do uso desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->