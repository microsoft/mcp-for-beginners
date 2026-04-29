## Testes e Depuração

Antes de começar a testar o seu servidor MCP, é importante compreender as ferramentas disponíveis e as melhores práticas para a depuração. Testes eficazes garantem que o seu servidor se comporta conforme esperado e ajudam a identificar e resolver problemas rapidamente. A secção seguinte descreve as abordagens recomendadas para validar a sua implementação MCP.

## Visão Geral

Esta lição cobre como selecionar a abordagem de teste correta e a ferramenta de teste mais eficaz.

## Objetivos de Aprendizagem

No final desta lição, será capaz de:

- Descrever várias abordagens para testes.
- Utilizar diferentes ferramentas para testar eficazmente o seu código.

## Testar Servidores MCP

O MCP fornece ferramentas para ajudar a testar e depurar os seus servidores:

- **MCP Inspector**: Uma ferramenta de linha de comandos que pode ser executada tanto como ferramenta CLI como visual.
- **Testes manuais**: Pode usar uma ferramenta como curl para executar pedidos web, mas qualquer ferramenta capaz de executar HTTP serve.
- **Testes unitários**: É possível usar o seu framework preferido de teste para testar funcionalidades tanto do servidor como do cliente.

### Usar o MCP Inspector

Já descrevemos a utilização desta ferramenta em lições anteriores, mas vamos falar um pouco dela a nível geral. É uma ferramenta construída em Node.js que pode usar chamando o executável `npx`, que irá descarregar e instalar temporariamente a ferramenta, e limpá-la depois de terminar de executar o seu pedido.

O [MCP Inspector](https://github.com/modelcontextprotocol/inspector) ajuda-o a:

- **Descobrir Capacidades do Servidor**: Detetar automaticamente recursos, ferramentas e prompts disponíveis
- **Testar a Execução de Ferramentas**: Experimentar diferentes parâmetros e ver respostas em tempo real
- **Visualizar Metadados do Servidor**: Examinar informações do servidor, esquemas e configurações

Uma execução típica da ferramenta é como segue:

```bash
npx @modelcontextprotocol/inspector node build/index.js
```

O comando acima inicia um MCP e a sua interface visual, lançando uma interface web local no seu navegador. Pode esperar ver um painel que exibe os seus servidores MCP registados, as ferramentas, recursos e prompts disponíveis. A interface permite-lhe testar interativamente a execução de ferramentas, inspecionar metadados do servidor e ver respostas em tempo real, facilitando a validação e depuração das suas implementações de servidor MCP.

Aqui está como pode parecer: ![Inspector](../../../../translated_images/pt-PT/connect.141db0b2bd05f096.webp)

Também pode executar esta ferramenta em modo CLI adicionando o atributo `--cli`. Aqui está um exemplo de execução da ferramenta no modo "CLI" que lista todas as ferramentas no servidor:

```sh
npx @modelcontextprotocol/inspector --cli node build/index.js --method tools/list
```

### Testes Manuais

Além de executar a ferramenta inspector para testar as capacidades do servidor, outra abordagem semelhante é executar um cliente capaz de usar HTTP como, por exemplo, o curl.

Com o curl, pode testar servidores MCP diretamente utilizando pedidos HTTP:

```bash
# Exemplo: Metadados do servidor de teste
curl http://localhost:3000/v1/metadata

# Exemplo: Executar uma ferramenta
curl -X POST http://localhost:3000/v1/tools/execute \
  -H "Content-Type: application/json" \
  -d '{"name": "calculator", "parameters": {"expression": "2+2"}}'
```

Como pode ver a partir do uso acima do curl, utiliza um pedido POST para invocar uma ferramenta usando uma payload que consiste no nome da ferramenta e nos seus parâmetros. Use a abordagem que melhor lhe convier. Ferramentas CLI tendem geralmente a ser mais rápidas de usar e facilitam a criação de scripts, o que pode ser útil num ambiente CI/CD.

### Testes Unitários

Crie testes unitários para as suas ferramentas e recursos para garantir que funcionam conforme esperado. Aqui está algum código exemplo para testes.

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
        # Testar sem o parâmetro cursor (omisso)
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

O código acima faz o seguinte:

- Utiliza o framework pytest que permite criar testes como funções e usar instruções assert.
- Cria um Servidor MCP com duas ferramentas diferentes.
- Usa a instrução `assert` para verificar que certas condições são cumpridas.

Veja o [ficheiro completo aqui](https://github.com/modelcontextprotocol/python-sdk/blob/main/tests/client/test_list_methods_cursor.py)

Dado o ficheiro acima, pode testar o seu próprio servidor para garantir que as capacidades são criadas como devem ser.

Todos os principais SDKs têm secções semelhantes de testes, pelo que pode ajustar ao runtime que escolheu.

## Exemplos

- [Calculadora Java](../samples/java/calculator/README.md)
- [Calculadora .Net](../../../../03-GettingStarted/samples/csharp)
- [Calculadora JavaScript](../samples/javascript/README.md)
- [Calculadora TypeScript](../samples/typescript/README.md)
- [Calculadora Python](../../../../03-GettingStarted/samples/python) 

## Recursos Adicionais

- [Python SDK](https://github.com/modelcontextprotocol/python-sdk)

## O Que Segue

- Segue: [Deployment](../09-deployment/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos por garantir a precisão, por favor tenha em consideração que as traduções automáticas podem conter erros ou imprecisões. O documento original no seu idioma nativo deve ser considerado a fonte autoritativa. Para informação crítica, recomendase tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes da utilização desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->