# Deployment de Servidores MCP

Fazer o deployment do seu servidor MCP permite que outros acedam às suas ferramentas e recursos para além do seu ambiente local. Existem várias estratégias de deployment a considerar, dependendo dos seus requisitos de escalabilidade, fiabilidade e facilidade de gestão. Abaixo encontrará orientação para fazer o deployment de servidores MCP localmente, em contentores e na cloud.

## Visão Geral

Esta lição aborda como fazer o deployment da sua aplicação MCP Server.

## Objetivos de Aprendizagem

No final desta lição, será capaz de:

- Avaliar diferentes abordagens de deployment.
- Fazer o deployment da sua aplicação.

## Desenvolvimento e Deployment Local

Se o seu servidor estiver pensado para ser consumido executando-se na máquina dos utilizadores, pode seguir os seguintes passos:

1. **Descarregar o servidor**. Se não escreveu o servidor, descarregue-o primeiro para a sua máquina.
1. **Iniciar o processo do servidor**: Execute a sua aplicação MCP server.

Para SSE (não necessário para servidores de tipo stdio)

1. **Configurar a rede**: Assegure que o servidor é acessível na porta esperada.
1. **Ligar os clientes**: Use URLs de ligação locais como `http://localhost:3000`.

## Deployment na Cloud

Servidores MCP podem ser desplegados em várias plataformas de cloud:

- **Funções Serverless**: Fazer deployment de servidores MCP leves como funções serverless.
- **Serviços de Contentores**: Usar serviços como Azure Container Apps, AWS ECS, ou Google Cloud Run.
- **Kubernetes**: Desplegar e gerir servidores MCP em clusters Kubernetes para alta disponibilidade.

### Exemplo: Azure Container Apps

Azure Container Apps suporta o deployment de Servidores MCP. Está ainda em desenvolvimento e atualmente suporta servidores SSE.

Veja como pode proceder:

1. Clone um repositório:

  ```sh
  git clone https://github.com/anthonychu/azure-container-apps-mcp-sample.git
  ```

1. Execute-o localmente para testar:

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

  Uma vez que o servidor SSE esteja iniciado, pode clicar no ícone de play no ficheiro JSON, deverá agora ver as ferramentas no servidor a serem reconhecidas pelo GitHub Copilot, veja o ícone da ferramenta.

1. Para fazer o deployment, execute o seguinte comando:

  ```sh
  az containerapp up -g <RESOURCE_GROUP_NAME> -n weather-mcp --environment mcp -l westus --env-vars API_KEYS=<AN_API_KEY> --source .
  ```

Está feito, faça o deployment localmente, faça o deployment para Azure através destes passos.

## Recursos Adicionais

- [Azure Functions + MCP](https://learn.microsoft.com/en-us/samples/azure-samples/remote-mcp-functions-dotnet/remote-mcp-functions-dotnet/)
- [Artigo Azure Container Apps](https://techcommunity.microsoft.com/blog/appsonazureblog/host-remote-mcp-servers-in-azure-container-apps/4403550)
- [Repositório Azure Container Apps MCP](https://github.com/anthonychu/azure-container-apps-mcp-sample)


## O que Segue

- Seguinte: [Tópicos Avançados de Servidor](../10-advanced/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos por garantir a precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se a tradução profissional por um humano. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes da utilização desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->