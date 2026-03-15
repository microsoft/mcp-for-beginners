# Implantando Servidores MCP

Implantar seu servidor MCP permite que outros acessem suas ferramentas e recursos além do seu ambiente local. Existem várias estratégias de implantação a considerar, dependendo dos seus requisitos de escalabilidade, confiabilidade e facilidade de gerenciamento. Abaixo você encontrará orientações para implantar servidores MCP localmente, em contêineres e na nuvem.

## Visão Geral

Esta lição cobre como implantar seu aplicativo Servidor MCP.

## Objetivos de Aprendizagem

Ao final desta lição, você será capaz de:

- Avaliar diferentes abordagens de implantação.
- Implantar seu aplicativo.

## Desenvolvimento e implantação local

Se seu servidor se destina a ser consumido executando na máquina dos usuários, você pode seguir os seguintes passos:

1. **Baixe o servidor**. Se você não escreveu o servidor, baixe-o primeiro para sua máquina.  
1. **Inicie o processo do servidor**: Execute seu aplicativo servidor MCP.

Para SSE (não necessário para servidor do tipo stdio)

1. **Configure a rede**: Garanta que o servidor seja acessível na porta esperada.  
1. **Conecte os clientes**: Use URLs de conexão local como `http://localhost:3000`.

## Implantação na Nuvem

Servidores MCP podem ser implantados em várias plataformas de nuvem:

- **Funções Serverless**: Implemente servidores MCP leves como funções serverless.  
- **Serviços de Contêiner**: Use serviços como Azure Container Apps, AWS ECS ou Google Cloud Run.  
- **Kubernetes**: Implemente e gerencie servidores MCP em clusters Kubernetes para alta disponibilidade.

### Exemplo: Azure Container Apps

Azure Container Apps suportam a implantação de Servidores MCP. Ainda está em desenvolvimento e atualmente suporta servidores SSE.

Veja como você pode fazer isso:

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

1. Para testar localmente, crie um arquivo *mcp.json* dentro de um diretório *.vscode* e adicione o seguinte conteúdo:

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

  Depois que o servidor SSE for iniciado, você pode clicar no ícone de play no arquivo JSON, agora deverá ver as ferramentas no servidor sendo captadas pelo GitHub Copilot, veja o ícone da Ferramenta.

1. Para implantar, execute o seguinte comando:

  ```sh
  az containerapp up -g <RESOURCE_GROUP_NAME> -n weather-mcp --environment mcp -l westus --env-vars API_KEYS=<AN_API_KEY> --source .
  ```

Pronto, implante localmente, implante no Azure seguindo esses passos.

## Recursos Adicionais

- [Azure Functions + MCP](https://learn.microsoft.com/en-us/samples/azure-samples/remote-mcp-functions-dotnet/remote-mcp-functions-dotnet/)
- [Artigo Azure Container Apps](https://techcommunity.microsoft.com/blog/appsonazureblog/host-remote-mcp-servers-in-azure-container-apps/4403550)
- [Repositório Azure Container Apps MCP](https://github.com/anthonychu/azure-container-apps-mcp-sample)


## O que vem a seguir

- Próximo: [Tópicos Avançados do Servidor](../10-advanced/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte oficial. Para informações críticas, recomenda-se a tradução profissional realizada por um humano. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações equivocadas decorrentes do uso desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->