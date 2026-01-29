# Desdobramento de Servidores MCP

Desdobrar o seu servidor MCP permite que outros acedam às suas ferramentas e recursos para além do seu ambiente local. Existem várias estratégias de desdobramento a considerar, dependendo dos seus requisitos de escalabilidade, fiabilidade e facilidade de gestão. Abaixo encontrará orientações para desdobrar servidores MCP localmente, em contentores e na cloud.

## Visão Geral

Esta lição aborda como desdobrar a sua aplicação MCP Server.

## Objetivos de Aprendizagem

No final desta lição, será capaz de:

- Avaliar diferentes abordagens de desdobramento.
- Desdobrar a sua aplicação.

## Desenvolvimento e desdobramento local

Se o seu servidor se destina a ser utilizado diretamente na máquina dos utilizadores, pode seguir os seguintes passos:

1. **Descarregar o servidor**. Se não escreveu o servidor, descarregue-o primeiro para a sua máquina.  
1. **Iniciar o processo do servidor**: Execute a sua aplicação MCP server.

Para SSE (não necessário para servidores do tipo stdio)

1. **Configurar a rede**: Assegure que o servidor está acessível na porta esperada.  
1. **Ligar os clientes**: Utilize URLs de ligação local como `http://localhost:3000`.

## Desdobramento na Cloud

Os servidores MCP podem ser desdobrados em várias plataformas cloud:

- **Funções Serverless**: Desdobre servidores MCP leves como funções serverless.  
- **Serviços de Contentores**: Utilize serviços como Azure Container Apps, AWS ECS ou Google Cloud Run.  
- **Kubernetes**: Desdobre e gere servidores MCP em clusters Kubernetes para alta disponibilidade.

### Exemplo: Azure Container Apps

O Azure Container Apps suporta o desdobramento de Servidores MCP. Ainda está em desenvolvimento e atualmente suporta servidores SSE.

Aqui está como pode proceder:

1. Clone um repositório:

  ```sh
  git clone https://github.com/anthonychu/azure-container-apps-mcp-sample.git
  ```

1. Execute localmente para testar:

  ```sh
  uv venv
  uv sync

  # linux/macOS
  export API_KEYS=<AN_API_KEY>
  # windows
  set API_KEYS=<AN_API_KEY>

  uv run fastapi dev main.py
  ```

1. Para testar localmente, crie um ficheiro *mcp.json* numa diretoria *.vscode* e adicione o seguinte conteúdo:

  ```json
  {
      "inputs": [
          {
              "type": "promptString",
              "id": "weather-api-key",
              "description": "Weather API Key",
              "password": true
          }
      ],
      "servers": {
          "weather-sse": {
              "type": "sse",
              "url": "http://localhost:8000/sse",
              "headers": {
                  "x-api-key": "${input:weather-api-key}"
              }
          }
      }
  }
  ```

  Depois de iniciar o servidor SSE, pode clicar no ícone de play no ficheiro JSON; deverá agora ver as ferramentas do servidor serem reconhecidas pelo GitHub Copilot, veja o ícone da Ferramenta.

1. Para desdobrar, execute o seguinte comando:

  ```sh
  az containerapp up -g <RESOURCE_GROUP_NAME> -n weather-mcp --environment mcp -l westus --env-vars API_KEYS=<AN_API_KEY> --source .
  ```

Está feito, desdobre localmente ou na Azure seguindo estes passos.

## Recursos Adicionais

- [Azure Functions + MCP](https://learn.microsoft.com/en-us/samples/azure-samples/remote-mcp-functions-dotnet/remote-mcp-functions-dotnet/)
- [Artigo sobre Azure Container Apps](https://techcommunity.microsoft.com/blog/appsonazureblog/host-remote-mcp-servers-in-azure-container-apps/4403550)
- [Repositório MCP para Azure Container Apps](https://github.com/anthonychu/azure-container-apps-mcp-sample)

## O que vem a seguir

- Seguinte: [Implementação Prática](../../04-PracticalImplementation/README.md)

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, por favor tenha em conta que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações erradas decorrentes da utilização desta tradução.