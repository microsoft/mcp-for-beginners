# Estudo de Caso: Expor API REST no API Management como um servidor MCP

O Azure API Management é um serviço que fornece um Gateway sobre seus endpoints de API. Ele funciona como um proxy na frente de suas APIs e pode decidir o que fazer com as solicitações recebidas.

Ao utilizá-lo, você adiciona uma série de recursos, como:

- **Segurança**, você pode usar desde chaves de API, JWT até identidade gerenciada.
- **Limitação de taxa**, um recurso excelente é poder decidir quantas chamadas são permitidas por unidade de tempo. Isso ajuda a garantir que todos os usuários tenham uma ótima experiência e também que seu serviço não seja sobrecarregado com solicitações.
- **Escalabilidade e balanceamento de carga**. Você pode configurar vários endpoints para distribuir a carga e também decidir como "balancear a carga".
- **Recursos de IA, como cache semântico**, limite de tokens, monitoramento de tokens e mais. Esses são recursos incríveis que melhoram a capacidade de resposta e ajudam você a gerenciar o uso de tokens. [Leia mais aqui](https://learn.microsoft.com/en-us/azure/api-management/genai-gateway-capabilities).

## Por que MCP + Azure API Management?

O Model Context Protocol está rapidamente se tornando um padrão para aplicativos de IA com agentes e para expor ferramentas e dados de maneira consistente. O Azure API Management é uma escolha natural quando você precisa "gerenciar" APIs. Servidores MCP frequentemente se integram com outras APIs para resolver solicitações de ferramentas, por exemplo. Portanto, combinar Azure API Management e MCP faz muito sentido.

## Visão Geral

Neste caso de uso específico, aprenderemos a expor endpoints de API como um servidor MCP. Ao fazer isso, podemos facilmente tornar esses endpoints parte de um aplicativo com agentes, enquanto aproveitamos os recursos do Azure API Management.

## Recursos Principais

- Você seleciona os métodos de endpoint que deseja expor como ferramentas.
- Os recursos adicionais que você obtém dependem do que você configura na seção de políticas para sua API. Aqui, mostraremos como adicionar limitação de taxa.

## Pré-requisito: importar uma API

Se você já tem uma API no Azure API Management, ótimo, então pode pular esta etapa. Caso contrário, confira este link: [importando uma API para o Azure API Management](https://learn.microsoft.com/en-us/azure/api-management/import-and-publish#import-and-publish-a-backend-api).

## Expor API como Servidor MCP

Para expor os endpoints da API, siga estas etapas:

1. Navegue até o Portal do Azure no seguinte endereço <https://portal.azure.com/?Microsoft_Azure_ApiManagement=mcp>. 
   Navegue até sua instância do API Management.

1. No menu à esquerda, selecione APIs > MCP Servers > + Criar novo servidor MCP.

1. Em API, selecione uma API REST para expor como servidor MCP.

1. Selecione uma ou mais operações de API para expor como ferramentas. Você pode selecionar todas as operações ou apenas operações específicas.

    ![Selecione métodos para expor](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/create-mcp-server-small.png)

1. Selecione **Criar**.

1. Navegue até a opção de menu **APIs** e **MCP Servers**, você deve ver o seguinte:

    ![Veja o servidor MCP no painel principal](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-list.png)

    O servidor MCP é criado e as operações da API são expostas como ferramentas. O servidor MCP é listado no painel MCP Servers. A coluna URL mostra o endpoint do servidor MCP que você pode chamar para testes ou dentro de um aplicativo cliente.

## Opcional: Configurar políticas

O Azure API Management tem o conceito central de políticas, onde você configura diferentes regras para seus endpoints, como limitação de taxa ou cache semântico. Essas políticas são escritas em XML.

Veja como configurar uma política para limitar a taxa de chamadas ao seu servidor MCP:

1. No portal, em APIs, selecione **MCP Servers**.

1. Selecione o servidor MCP que você criou.

1. No menu à esquerda, em MCP, selecione **Policies**.

1. No editor de políticas, adicione ou edite as políticas que deseja aplicar às ferramentas do servidor MCP. As políticas são definidas em formato XML. Por exemplo, você pode adicionar uma política para limitar chamadas às ferramentas do servidor MCP (neste exemplo, 5 chamadas por 30 segundos por endereço IP do cliente). Aqui está o XML que causará a limitação de taxa:

    ```xml
     <rate-limit-by-key calls="5" 
       renewal-period="30" 
       counter-key="@(context.Request.IpAddress)" 
       remaining-calls-variable-name="remainingCallsPerIP" 
    />
    ```

    Aqui está uma imagem do editor de políticas:

    ![Editor de políticas](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-policies-small.png)

## Teste

Vamos garantir que nosso servidor MCP está funcionando conforme o esperado.

Para isso, usaremos o Visual Studio Code e o GitHub Copilot em seu modo de agente. Adicionaremos o servidor MCP a um arquivo *mcp.json*. Ao fazer isso, o Visual Studio Code atuará como um cliente com capacidades de agente e os usuários finais poderão digitar um prompt e interagir com o servidor.

Veja como adicionar o servidor MCP no Visual Studio Code:

1. Use o comando MCP: **Add Server** no Command Palette.

1. Quando solicitado, selecione o tipo de servidor: **HTTP (HTTP ou Server Sent Events)**.

1. Insira o URL do servidor MCP no API Management. Exemplo: **https://<apim-service-name>.azure-api.net/<api-name>-mcp/sse** (para endpoint SSE) ou **https://<apim-service-name>.azure-api.net/<api-name>-mcp/mcp** (para endpoint MCP), observe como a diferença entre os transportes é `/sse` ou `/mcp`.

1. Insira um ID de servidor de sua escolha. Este valor não é importante, mas ajudará você a lembrar o que é esta instância de servidor.

1. Selecione se deseja salvar a configuração nas configurações do workspace ou nas configurações do usuário.

  - **Configurações do workspace** - A configuração do servidor é salva em um arquivo .vscode/mcp.json disponível apenas no workspace atual.

    *mcp.json*

    ```json
    "servers": {
        "APIM petstore" : {
            "type": "sse",
            "url": "url-to-mcp-server/sse"
        }
    }
    ```

    ou, se você escolher HTTP streaming como transporte, seria ligeiramente diferente:

    ```json
    "servers": {
        "APIM petstore" : {
            "type": "http",
            "url": "url-to-mcp-server/mcp"
        }
    }
    ```

  - **Configurações do usuário** - A configuração do servidor é adicionada ao arquivo global *settings.json* e está disponível em todos os workspaces. A configuração se parece com o seguinte:

    ![Configuração do usuário](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-servers-visual-studio-code.png)

1. Você também precisa adicionar uma configuração, um cabeçalho para garantir que autentique corretamente com o Azure API Management. Ele usa um cabeçalho chamado **Ocp-Apim-Subscription-Key**.

    - Veja como você pode adicioná-lo às configurações:

    ![Adicionando cabeçalho para autenticação](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-with-header-visual-studio-code.png), isso fará com que um prompt seja exibido pedindo o valor da chave de API, que você pode encontrar no Portal do Azure para sua instância do Azure API Management.

   - Para adicioná-lo ao *mcp.json*, você pode fazer assim:

    ```json
    "inputs": [
      {
        "type": "promptString",
        "id": "apim_key",
        "description": "API Key for Azure API Management",
        "password": true
      }
    ]
    "servers": {
        "APIM petstore" : {
            "type": "http",
            "url": "url-to-mcp-server/mcp",
            "headers": {
                "Ocp-Apim-Subscription-Key": "Bearer ${input:apim_key}"
            }
        }
    }
    ```

### Usar o modo de agente

Agora estamos configurados, seja nas configurações ou no *.vscode/mcp.json*. Vamos testar.

Deve haver um ícone de Ferramentas como este, onde as ferramentas expostas do seu servidor estão listadas:

![Ferramentas do servidor](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/tools-button-visual-studio-code.png)

1. Clique no ícone de ferramentas e você deve ver uma lista de ferramentas como esta:

    ![Ferramentas](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/select-tools-visual-studio-code.png)

1. Insira um prompt no chat para invocar a ferramenta. Por exemplo, se você selecionou uma ferramenta para obter informações sobre um pedido, pode perguntar ao agente sobre um pedido. Aqui está um exemplo de prompt:

    ```text
    get information from order 2
    ```

    Agora será exibido um ícone de ferramentas pedindo para você continuar chamando uma ferramenta. Selecione para continuar executando a ferramenta, você deve ver um resultado como este:

    ![Resultado do prompt](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/chat-results-visual-studio-code.png)

    **O que você vê acima depende das ferramentas que você configurou, mas a ideia é que você obtenha uma resposta textual como acima.**

## Referências

Aqui está como você pode aprender mais:

- [Tutorial sobre Azure API Management e MCP](https://learn.microsoft.com/en-us/azure/api-management/export-rest-mcp-server)
- [Exemplo em Python: Proteger servidores MCP remotos usando Azure API Management (experimental)](https://github.com/Azure-Samples/remote-mcp-apim-functions-python)

- [Laboratório de autorização de cliente MCP](https://github.com/Azure-Samples/AI-Gateway/tree/main/labs/mcp-client-authorization)

- [Usar a extensão Azure API Management para VS Code para importar e gerenciar APIs](https://learn.microsoft.com/en-us/azure/api-management/visual-studio-code-tutorial)

- [Registrar e descobrir servidores MCP remotos no Azure API Center](https://learn.microsoft.com/en-us/azure/api-center/register-discover-mcp-server)
- [AI Gateway](https://github.com/Azure-Samples/AI-Gateway) Ótimo repositório que mostra muitas capacidades de IA com Azure API Management
- [Workshops do AI Gateway](https://azure-samples.github.io/AI-Gateway/) Contém workshops usando o Portal do Azure, que é uma ótima maneira de começar a avaliar capacidades de IA.

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autoritativa. Para informações críticas, recomenda-se a tradução profissional realizada por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.