# Caso de Estudo: Expor API REST no API Management como um servidor MCP

O Azure API Management é um serviço que fornece um Gateway sobre os seus endpoints de API. Ele funciona como um proxy à frente das suas APIs e pode decidir o que fazer com as solicitações recebidas.

Ao utilizá-lo, você adiciona uma série de funcionalidades, como:

- **Segurança**, pode usar desde chaves de API, JWT até identidade gerida.
- **Limitação de taxa**, uma funcionalidade excelente que permite decidir quantas chamadas podem ser feitas por unidade de tempo. Isso ajuda a garantir que todos os utilizadores tenham uma ótima experiência e que o seu serviço não seja sobrecarregado com solicitações.
- **Escalabilidade e balanceamento de carga**. Pode configurar vários endpoints para distribuir a carga e também decidir como "balancear a carga".
- **Funcionalidades de IA como cache semântica**, limite de tokens, monitorização de tokens e mais. Estas são funcionalidades incríveis que melhoram a capacidade de resposta e ajudam a controlar o uso de tokens. [Leia mais aqui](https://learn.microsoft.com/en-us/azure/api-management/genai-gateway-capabilities).

## Por que MCP + Azure API Management?

O Model Context Protocol está rapidamente a tornar-se um padrão para aplicações de IA com agentes e para expor ferramentas e dados de forma consistente. O Azure API Management é uma escolha natural quando precisa de "gerir" APIs. Os servidores MCP frequentemente integram-se com outras APIs para resolver solicitações de ferramentas, por exemplo. Portanto, combinar Azure API Management e MCP faz muito sentido.

## Visão Geral

Neste caso de uso específico, vamos aprender a expor endpoints de API como um servidor MCP. Ao fazer isso, podemos facilmente tornar esses endpoints parte de uma aplicação com agentes, enquanto aproveitamos as funcionalidades do Azure API Management.

## Funcionalidades Principais

- Pode selecionar os métodos de endpoint que deseja expor como ferramentas.
- As funcionalidades adicionais que obtém dependem do que configurar na seção de políticas para a sua API. Aqui, mostraremos como pode adicionar limitação de taxa.

## Pré-passo: importar uma API

Se já tiver uma API no Azure API Management, ótimo, pode pular este passo. Caso contrário, consulte este link: [importar uma API para o Azure API Management](https://learn.microsoft.com/en-us/azure/api-management/import-and-publish#import-and-publish-a-backend-api).

## Expor API como Servidor MCP

Para expor os endpoints da API, siga estes passos:

1. Navegue até o Portal Azure no seguinte endereço <https://portal.azure.com/?Microsoft_Azure_ApiManagement=mcp>  
   Navegue até a sua instância do API Management.

1. No menu à esquerda, selecione APIs > MCP Servers > + Criar novo servidor MCP.

1. Na API, selecione uma API REST para expor como servidor MCP.

1. Selecione uma ou mais operações de API para expor como ferramentas. Pode selecionar todas as operações ou apenas operações específicas.

    ![Selecionar métodos para expor](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/create-mcp-server-small.png)

1. Selecione **Criar**.

1. Navegue até a opção de menu **APIs** e **MCP Servers**, deverá ver o seguinte:

    ![Ver o servidor MCP no painel principal](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-list.png)

    O servidor MCP é criado e as operações da API são expostas como ferramentas. O servidor MCP é listado no painel MCP Servers. A coluna URL mostra o endpoint do servidor MCP que pode ser chamado para testes ou dentro de uma aplicação cliente.

## Opcional: Configurar políticas

O Azure API Management tem o conceito central de políticas, onde pode configurar diferentes regras para os seus endpoints, como limitação de taxa ou cache semântica. Estas políticas são escritas em XML.

Veja como configurar uma política para limitar a taxa do seu servidor MCP:

1. No portal, em APIs, selecione **MCP Servers**.

1. Selecione o servidor MCP que criou.

1. No menu à esquerda, em MCP, selecione **Policies**.

1. No editor de políticas, adicione ou edite as políticas que deseja aplicar às ferramentas do servidor MCP. As políticas são definidas em formato XML. Por exemplo, pode adicionar uma política para limitar chamadas às ferramentas do servidor MCP (neste exemplo, 5 chamadas por 30 segundos por endereço IP do cliente). Aqui está o XML que causará a limitação de taxa:

    ```xml
     <rate-limit-by-key calls="5" 
       renewal-period="30" 
       counter-key="@(context.Request.IpAddress)" 
       remaining-calls-variable-name="remainingCallsPerIP" 
    />
    ```

    Aqui está uma imagem do editor de políticas:

    ![Editor de políticas](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-policies-small.png)

## Testar

Vamos garantir que o nosso servidor MCP está a funcionar conforme esperado.

Para isso, usaremos o Visual Studio Code e o GitHub Copilot no modo Agent. Adicionaremos o servidor MCP a um ficheiro *mcp.json*. Ao fazer isso, o Visual Studio Code atuará como um cliente com capacidades de agente e os utilizadores finais poderão digitar um prompt e interagir com o servidor.

Veja como adicionar o servidor MCP no Visual Studio Code:

1. Use o comando MCP: **Add Server** no Command Palette.

1. Quando solicitado, selecione o tipo de servidor: **HTTP (HTTP ou Server Sent Events)**.

1. Insira o URL do servidor MCP no API Management. Exemplo: **https://<apim-service-name>.azure-api.net/<api-name>-mcp/sse** (para endpoint SSE) ou **https://<apim-service-name>.azure-api.net/<api-name>-mcp/mcp** (para endpoint MCP), note como a diferença entre os transportes é `/sse` ou `/mcp`.

1. Insira um ID de servidor à sua escolha. Este valor não é importante, mas ajudará a lembrar o que esta instância de servidor representa.

1. Escolha se deseja salvar a configuração nas definições do espaço de trabalho ou nas definições do utilizador.

  - **Definições do espaço de trabalho** - A configuração do servidor é salva num ficheiro .vscode/mcp.json disponível apenas no espaço de trabalho atual.

    *mcp.json*

    ```json
    "servers": {
        "APIM petstore" : {
            "type": "sse",
            "url": "url-to-mcp-server/sse"
        }
    }
    ```

    ou, se escolher HTTP em streaming como transporte, será ligeiramente diferente:

    ```json
    "servers": {
        "APIM petstore" : {
            "type": "http",
            "url": "url-to-mcp-server/mcp"
        }
    }
    ```

  - **Definições do utilizador** - A configuração do servidor é adicionada ao ficheiro global *settings.json* e está disponível em todos os espaços de trabalho. A configuração será semelhante ao seguinte:

    ![Definição do utilizador](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-servers-visual-studio-code.png)

1. Também precisa adicionar uma configuração, um cabeçalho para garantir que autentica corretamente com o Azure API Management. Ele usa um cabeçalho chamado **Ocp-Apim-Subscription-Key**.

    - Veja como pode adicioná-lo às definições:

    ![Adicionar cabeçalho para autenticação](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-with-header-visual-studio-code.png), isso fará com que seja exibido um prompt para inserir o valor da chave de API, que pode ser encontrado no Portal Azure para a sua instância do Azure API Management.

   - Para adicioná-lo ao *mcp.json*, pode fazer assim:

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

### Usar o modo Agent

Agora estamos configurados, seja nas definições ou no *.vscode/mcp.json*. Vamos testá-lo.

Deverá haver um ícone de Ferramentas como este, onde as ferramentas expostas do seu servidor estão listadas:

![Ferramentas do servidor](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/tools-button-visual-studio-code.png)

1. Clique no ícone de ferramentas e deverá ver uma lista de ferramentas como esta:

    ![Ferramentas](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/select-tools-visual-studio-code.png)

1. Insira um prompt no chat para invocar a ferramenta. Por exemplo, se selecionou uma ferramenta para obter informações sobre um pedido, pode perguntar ao agente sobre um pedido. Aqui está um exemplo de prompt:

    ```text
    get information from order 2
    ```

    Agora será apresentado um ícone de ferramentas pedindo para prosseguir com a chamada de uma ferramenta. Selecione para continuar a executar a ferramenta, deverá ver um resultado como este:

    ![Resultado do prompt](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/chat-results-visual-studio-code.png)

    **O que vê acima depende das ferramentas que configurou, mas a ideia é que obtenha uma resposta textual como acima.**

## Referências

Aqui está como pode aprender mais:

- [Tutorial sobre Azure API Management e MCP](https://learn.microsoft.com/en-us/azure/api-management/export-rest-mcp-server)
- [Exemplo em Python: Proteger servidores MCP remotos usando Azure API Management (experimental)](https://github.com/Azure-Samples/remote-mcp-apim-functions-python)

- [Laboratório de autorização de cliente MCP](https://github.com/Azure-Samples/AI-Gateway/tree/main/labs/mcp-client-authorization)

- [Usar a extensão Azure API Management para VS Code para importar e gerir APIs](https://learn.microsoft.com/en-us/azure/api-management/visual-studio-code-tutorial)

- [Registar e descobrir servidores MCP remotos no Azure API Center](https://learn.microsoft.com/en-us/azure/api-center/register-discover-mcp-server)
- [AI Gateway](https://github.com/Azure-Samples/AI-Gateway) Excelente repositório que mostra muitas capacidades de IA com Azure API Management
- [Workshops do AI Gateway](https://azure-samples.github.io/AI-Gateway/) Contém workshops usando o Portal Azure, que é uma ótima forma de começar a avaliar capacidades de IA.

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original no seu idioma nativo deve ser considerado a fonte oficial. Para informações críticas, recomenda-se a tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.