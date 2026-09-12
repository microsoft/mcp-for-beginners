# Estudo de Caso: Expor API REST no Gerenciamento de API como um servidor MCP

O Azure API Management é um serviço que fornece um Gateway sobre seus Endpoints de API. Seu funcionamento é que o Azure API Management atua como um proxy na frente das suas APIs e pode decidir o que fazer com as requisições recebidas.

Ao utilizá-lo, você adiciona uma série de recursos como:

- **Segurança**, você pode usar desde chaves de API, JWT até identidade gerenciada.
- **Limitação de taxa**, um ótimo recurso que permite decidir quantas chamadas podem passar por unidade de tempo. Isso ajuda a garantir que todos os usuários tenham uma ótima experiência e que seu serviço não fique sobrecarregado por requisições.
- **Escalabilidade e balanceamento de carga**. Você pode configurar vários endpoints para distribuir a carga e também decidir como fazer esse "balanceamento de carga".
- **Recursos de IA como cache semântico**, limite de tokens, monitoramento de tokens e mais. São funcionalidades excelentes que melhoram a capacidade de resposta e também ajudam a controlar o uso de tokens. [Leia mais aqui](https://learn.microsoft.com/en-us/azure/api-management/genai-gateway-capabilities).

## Por que MCP + Azure API Management?

O Model Context Protocol está rapidamente se tornando um padrão para aplicativos de IA agentiva e para expor ferramentas e dados de forma consistente. O Azure API Management é uma escolha natural quando você precisa "gerenciar" APIs. Servidores MCP frequentemente se integram a outras APIs para resolver requisições para uma ferramenta, por exemplo. Portanto, combinar Azure API Management e MCP faz muito sentido.

## Visão Geral

Neste caso de uso específico, aprenderemos a expor endpoints de API como um Servidor MCP. Fazendo isso, podemos facilmente tornar esses endpoints parte de um aplicativo agentivo enquanto aproveitamos os recursos do Azure API Management.

## Recursos Principais

- Você seleciona os métodos do endpoint que deseja expor como ferramentas.
- Os recursos adicionais que você obtém dependem do que configurar na seção de políticas para sua API. Aqui mostraremos como adicionar limitação de taxa.

## Passo prévio: importar uma API

Se você já tem uma API no Azure API Management, ótimo, pode pular esta etapa. Caso contrário, confira este link, [importando uma API para Azure API Management](https://learn.microsoft.com/en-us/azure/api-management/import-and-publish#import-and-publish-a-backend-api).

## Expor API como Servidor MCP

Para expor os endpoints da API, siga estes passos:

1. Navegue até o Portal Azure no endereço <https://portal.azure.com/?Microsoft_Azure_ApiManagement=mcp> 
Vá para sua instância de Gerenciamento de API.

1. No menu à esquerda, selecione APIs > MCP Servers > + Criar novo Servidor MCP.

1. Em API, selecione uma API REST para expor como servidor MCP.

1. Selecione uma ou mais Operações de API para expor como ferramentas. Você pode selecionar todas as operações ou apenas algumas específicas.

    ![Selecione os métodos para expor](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/create-mcp-server-small.png)


1. Selecione **Criar**.

1. Navegue até o menu **APIs** e **MCP Servers**, você deverá ver o seguinte:

    ![Veja o Servidor MCP na área principal](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-list.png)

    O servidor MCP foi criado e as operações da API são expostas como ferramentas. O servidor MCP está listado no painel MCP Servers. A coluna URL mostra o endpoint do servidor MCP que você pode chamar para teste ou dentro de um aplicativo cliente.

## Opcional: Configurar políticas

O Azure API Management tem o conceito central de políticas onde você define regras diferentes para seus endpoints, como por exemplo limitação de taxa ou cache semântico. Essas políticas são definidas em XML.

Veja como configurar uma política para limitar a taxa no seu servidor MCP:

1. No portal, sob APIs, selecione **MCP Servers**.

1. Selecione o servidor MCP que você criou.

1. No menu à esquerda, sob MCP, selecione **Políticas**.

1. No editor de políticas, adicione ou edite as políticas que deseja aplicar às ferramentas do servidor MCP. As políticas são definidas em formato XML. Por exemplo, você pode adicionar uma política para limitar chamadas às ferramentas do servidor MCP (neste exemplo, 5 chamadas a cada 30 segundos por endereço IP cliente). Segue o XML que aplicaria essa limitação:

    ```xml
     <rate-limit-by-key calls="5" 
       renewal-period="30" 
       counter-key="@(context.Request.IpAddress)" 
       remaining-calls-variable-name="remainingCallsPerIP" 
    />
    ```

    Aqui está uma imagem do editor de políticas:

    ![Editor de políticas](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-policies-small.png)
 
## Experimente

Vamos garantir que nosso servidor MCP esteja funcionando como esperado.

> [!NOTE]
> O Azure API Management atualmente expõe este servidor através do endpoint HTTP Streamable
> `/mcp`. O transporte antigo HTTP+SSE `/sse` está depreciado e
> deve ser usado apenas com clientes legados.

Para isso, usaremos o Visual Studio Code com o GitHub Copilot e seu modo Agent. Vamos adicionar o servidor MCP a um arquivo *mcp.json*. Assim, o Visual Studio Code atuará como um cliente com capacidades agentivas e os usuários finais poderão digitar um prompt e interagir com esse servidor.

Veja como adicionar o servidor MCP no Visual Studio Code:

1. Use o comando MCP: **Adicionar Servidor no Command Palette**.

1. Quando solicitado, selecione o tipo de servidor: **HTTP (HTTP ou Server Sent Events)**.

1. Insira a URL HTTP Streamable mostrada para o servidor MCP no API Management.
    Por exemplo:
    `https://<apim-service-name>.azure-api.net/<api-name>-mcp/mcp`.

1. Insira um ID de servidor de sua escolha. Este valor não é crítico, mas ajuda a lembrar qual instância do servidor é essa.

1. Selecione se deseja salvar a configuração nas configurações do workspace ou do usuário.

  - **Configurações do Workspace** - A configuração do servidor é salva em um arquivo .vscode/mcp.json disponível apenas no workspace atual.

    *mcp.json*

    ```json
    "servers": {
        "APIM petstore" : {
            "type": "http",
            "url": "url-to-mcp-server/mcp"
        }
    }
    ```

  - **Configurações do Usuário** - A configuração do servidor é adicionada ao arquivo global *settings.json* e fica disponível em todos os workspaces. A configuração é semelhante a esta:

    ![Configuração do usuário](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-servers-visual-studio-code.png)

1. Você também precisa adicionar uma configuração, um header para garantir autenticação adequada junto ao Azure API Management. É usado um header chamado **Ocp-Apim-Subscription-Key**. 

    - Veja como adicioná-lo nas configurações:

    ![Adicionando header para autenticação](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-with-header-visual-studio-code.png), isso fará aparecer um prompt para você informar o valor da chave de API que você encontra no Portal Azure para sua instância de Azure API Management.

   - Para adicionar no *mcp.json* em vez disso, você pode fazer assim:

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

### Use o modo Agent

Agora tudo está configurado nas configurações ou no *.vscode/mcp.json*. Vamos experimentar. 

Deve haver um ícone de Ferramentas assim, onde as ferramentas expostas pelo seu servidor são listadas:

![Ferramentas do servidor](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/tools-button-visual-studio-code.png)

1. Clique no ícone de ferramentas e você verá uma lista de ferramentas assim:

    ![Ferramentas](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/select-tools-visual-studio-code.png)

1. Digite um prompt na conversa para invocar a ferramenta. Por exemplo, se você selecionou uma ferramenta para obter informações sobre um pedido, pode perguntar ao agente sobre um pedido. Veja um exemplo de prompt:

    ```text
    get information from order 2
    ```

    Agora será exibido um ícone de ferramentas pedindo para você continuar chamando a ferramenta. Selecione para continuar executando a ferramenta, agora você deverá ver uma saída como esta:

    ![Resultado do prompt](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/chat-results-visual-studio-code.png)

    **o que você vê acima depende das ferramentas configuradas, mas a ideia é que você obtenha uma resposta textual como acima**


## Referências

Veja como aprender mais:

- [Tutorial sobre Azure API Management e MCP](https://learn.microsoft.com/en-us/azure/api-management/export-rest-mcp-server)
- [Exemplo em Python: Servidores MCP remotos seguros usando Azure API Management (experimental)](https://github.com/Azure-Samples/remote-mcp-apim-functions-python)

- [Lab de autorização para clientes MCP](https://github.com/Azure-Samples/AI-Gateway/tree/main/labs/mcp-client-authorization)

- [Use a extensão Azure API Management para VS Code para importar e gerenciar APIs](https://learn.microsoft.com/en-us/azure/api-management/visual-studio-code-tutorial)

- [Registrar e descobrir servidores MCP remotos no Azure API Center](https://learn.microsoft.com/en-us/azure/api-center/register-discover-mcp-server)
- [AI Gateway](https://github.com/Azure-Samples/AI-Gateway) Excelente repositório que mostra muitas capacidades de IA com Azure API Management
- [Workshops AI Gateway](https://azure-samples.github.io/AI-Gateway/) Contém workshops usando o Portal Azure, uma ótima maneira de começar a avaliar capacidades de IA.

## O que vem a seguir

- Voltar para: [Visão Geral dos Estudos de Caso](./README.md)
- Próximo: [Agentes de Viagem Azure AI](./travelagentsample.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido usando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, por favor, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->