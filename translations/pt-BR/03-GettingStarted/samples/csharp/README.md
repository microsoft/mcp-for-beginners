# Serviço Básico de Calculadora MCP

Este serviço oferece operações básicas de calculadora através do Model Context Protocol (MCP). Foi criado como um exemplo simples para iniciantes que estão aprendendo sobre implementações MCP.

Para mais informações, veja [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk)

## Funcionalidades

Este serviço de calculadora oferece as seguintes capacidades:

1. **Operações Aritméticas Básicas**:
   - Adição de dois números
   - Subtração de um número por outro
   - Multiplicação de dois números
   - Divisão de um número por outro (com verificação de divisão por zero)

## Usando o tipo `stdio`
  
## Configuração

1. **Configurar Servidores MCP**:
   - Abra seu workspace no VS Code.
   - Crie um arquivo `.vscode/mcp.json` na pasta do seu workspace para configurar os servidores MCP. Exemplo de configuração:

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

   - Será solicitado que você informe a raiz do repositório GitHub, que pode ser obtida com o comando `git rev-parse --show-toplevel`.

## Usando o Serviço

O serviço expõe os seguintes endpoints da API através do protocolo MCP:

- `add(a, b)`: Soma dois números
- `subtract(a, b)`: Subtrai o segundo número do primeiro
- `multiply(a, b)`: Multiplica dois números
- `divide(a, b)`: Divide o primeiro número pelo segundo (com verificação de zero)
- isPrime(n): Verifica se um número é primo

## Teste com Github Copilot Chat no VS Code

1. Tente fazer uma requisição ao serviço usando o protocolo MCP. Por exemplo, você pode pedir:
   - "Some 5 e 3"
   - "Subtraia 10 de 4"
   - "Multiplique 6 por 7"
   - "Divida 8 por 2"
   - "O 37854 é primo?"
   - "Quais são os 3 números primos antes e depois de 4242?"
2. Para garantir que está usando as ferramentas, adicione #MyCalculator ao prompt. Por exemplo:
   - "Some 5 e 3 #MyCalculator"
   - "Subtraia 10 de 4 #MyCalculator"

## Versão Containerizada

A solução anterior é ótima quando você tem o SDK .NET instalado e todas as dependências configuradas. Porém, se quiser compartilhar a solução ou executá-la em um ambiente diferente, pode usar a versão containerizada.

1. Inicie o Docker e certifique-se de que ele está rodando.
1. No terminal, navegue até a pasta `03-GettingStarted\samples\csharp\src`
1. Para construir a imagem Docker do serviço de calculadora, execute o seguinte comando (substitua `<YOUR-DOCKER-USERNAME>` pelo seu nome de usuário do Docker Hub):
   ```bash
   docker build -t <YOUR-DOCKER-USERNAME>/mcp-calculator .
   ``` 
1. Após a imagem ser construída, vamos enviá-la para o Docker Hub. Execute o seguinte comando:
   ```bash
    docker push <YOUR-DOCKER-USERNAME>/mcp-calculator
  ```

## Usando a Versão Dockerizada

1. No arquivo `.vscode/mcp.json`, substitua a configuração do servidor pelo seguinte:
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
   Observando a configuração, você verá que o comando é `docker` e os argumentos são `run --rm -i <YOUR-DOCKER-USERNAME>/mcp-calc`. A flag `--rm` garante que o container seja removido após parar, e a flag `-i` permite que você interaja com a entrada padrão do container. O último argumento é o nome da imagem que acabamos de construir e enviar para o Docker Hub.

## Teste a Versão Dockerizada

Inicie o Servidor MCP clicando no pequeno botão Iniciar acima de `"mcp-calc": {`, e assim como antes, você pode pedir para o serviço de calculadora fazer alguns cálculos para você.

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.