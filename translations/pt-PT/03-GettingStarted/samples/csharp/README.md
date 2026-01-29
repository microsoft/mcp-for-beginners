# Serviço Básico de Calculadora MCP

Este serviço fornece operações básicas de calculadora através do Model Context Protocol (MCP). Foi concebido como um exemplo simples para iniciantes que estão a aprender sobre implementações MCP.

Para mais informações, consulte [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk)

## Funcionalidades

Este serviço de calculadora oferece as seguintes capacidades:

1. **Operações Aritméticas Básicas**:
   - Adição de dois números
   - Subtração de um número a partir de outro
   - Multiplicação de dois números
   - Divisão de um número por outro (com verificação de divisão por zero)

## Utilização do tipo `stdio`
  
## Configuração

1. **Configurar Servidores MCP**:
   - Abra o seu espaço de trabalho no VS Code.
   - Crie um ficheiro `.vscode/mcp.json` na pasta do seu espaço de trabalho para configurar os servidores MCP. Exemplo de configuração:

     ```jsonc
     {
       "inputs": [
         {
           "type": "promptString",
           "id": "repository-root",
           "description": "The absolute path to the repository root"
         }
       ],
       "servers": {
         "calculator-mcp-dotnet": {
           "type": "stdio",
           "command": "dotnet",
           "args": [
             "run",
             "--project",
             "${input:repository-root}/03-GettingStarted/samples/csharp/src/calculator.csproj"
           ]
         }
       }
     }
     ```

   - Será solicitado que insira a raiz do repositório GitHub, que pode ser obtida com o comando `git rev-parse --show-toplevel`.

## Utilização do Serviço

O serviço expõe os seguintes endpoints API através do protocolo MCP:

- `add(a, b)`: Adiciona dois números
- `subtract(a, b)`: Subtrai o segundo número ao primeiro
- `multiply(a, b)`: Multiplica dois números
- `divide(a, b)`: Divide o primeiro número pelo segundo (com verificação de zero)
- isPrime(n): Verifica se um número é primo

## Testar com Github Copilot Chat no VS Code

1. Experimente fazer um pedido ao serviço usando o protocolo MCP. Por exemplo, pode pedir:
   - "Add 5 and 3"
   - "Subtract 10 from 4"
   - "Multiply 6 and 7"
   - "Divide 8 by 2"
   - "Does 37854 prime?"
   - "What are the 3 prime numbers before after 4242?"
2. Para garantir que está a usar as ferramentas, adicione #MyCalculator ao prompt. Por exemplo:
   - "Add 5 and 3 #MyCalculator"
   - "Subtract 10 from 4 #MyCalculator"

## Versão Containerizada

A solução anterior é ótima quando tem o .NET SDK instalado e todas as dependências configuradas. No entanto, se quiser partilhar a solução ou executá-la num ambiente diferente, pode usar a versão containerizada.

1. Inicie o Docker e certifique-se de que está a funcionar.
1. A partir de um terminal, navegue até à pasta `03-GettingStarted\samples\csharp\src`
1. Para construir a imagem Docker para o serviço de calculadora, execute o seguinte comando (substitua `<YOUR-DOCKER-USERNAME>` pelo seu nome de utilizador do Docker Hub):
   ```bash
   docker build -t <YOUR-DOCKER-USERNAME>/mcp-calculator .
   ``` 
1. Depois de a imagem estar construída, vamos enviá-la para o Docker Hub. Execute o seguinte comando:
   ```bash
    docker push <YOUR-DOCKER-USERNAME>/mcp-calculator
  ```

## Usar a Versão Dockerizada

1. No ficheiro `.vscode/mcp.json`, substitua a configuração do servidor pela seguinte:
   ```json
    "mcp-calc": {
      "command": "docker",
      "args": [
        "run",
        "--rm",
        "-i",
        "<YOUR-DOCKER-USERNAME>/mcp-calc"
      ],
      "envFile": "",
      "env": {}
    }
   ```
   Ao analisar a configuração, pode ver que o comando é `docker` e os argumentos são `run --rm -i <YOUR-DOCKER-USERNAME>/mcp-calc`. A flag `--rm` garante que o container é removido após parar, e a flag `-i` permite interagir com a entrada padrão do container. O último argumento é o nome da imagem que acabámos de construir e enviar para o Docker Hub.

## Testar a Versão Dockerizada

Inicie o Servidor MCP clicando no pequeno botão Iniciar acima de `"mcp-calc": {`, e tal como antes, pode pedir ao serviço de calculadora para fazer alguns cálculos por si.

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos por garantir a precisão, por favor tenha em conta que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se a tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações erradas decorrentes da utilização desta tradução.