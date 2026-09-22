# Estudo de Caso: Expor REST API no API Management como servidor MCP

O Azure API Management é um serviço que fornece um Gateway por cima dos seus Endpoints de API. O funcionamento baseia-se em o Azure API Management atuar como proxy à frente das suas APIs e decidir o que fazer com os pedidos recebidos.

Ao usá-lo, adiciona um conjunto de funcionalidades como:

- **Segurança**, pode usar desde chaves API, JWT até identidade gerida.
- **Limitacão de taxa**, uma ótima funcionalidade que permite decidir quantas chamadas passam por uma unidade de tempo. Isto ajuda a garantir que todos os utilizadores tenham uma ótima experiência e que o seu serviço não fique sobrecarregado de pedidos.
- **Escalabilidade e Balanceamento de carga**. Pode configurar vários endpoints para equilibrar a carga e pode também decidir como "balancear a carga".
- **Funcionalidades de IA como cache semântico**, limite de tokens, monitorização de tokens e mais. Estas são ótimas funcionalidades que melhoram a reatividade e ajudam a controlar o gasto de tokens. [Leia mais aqui](https://learn.microsoft.com/en-us/azure/api-management/genai-gateway-capabilities).

## Por que MCP + Azure API Management?

O Model Context Protocol está rapidamente a tornar-se um standard para apps de IA agentic e para expor ferramentas e dados de forma consistente. O Azure API Management é uma escolha natural quando necessita de "gerir" APIs. Servidores MCP costumam integrar-se com outras APIs para resolver pedidos para uma ferramenta, por exemplo. Portanto, combinar Azure API Management e MCP faz muito sentido.

## Visão Geral

Neste caso de uso específico, aprenderemos a expor endpoints de API como um servidor MCP. Assim, podemos facilmente integrar estes endpoints numa app agentic ao mesmo tempo que aproveitamos as funcionalidades do Azure API Management.

## Funcionalidades Principais

- Seleciona os métodos do endpoint que quer expor como ferramentas.
- As funcionalidades adicionais que recebe dependem do que configurar na secção de políticas da sua API. Aqui, mostramos como pode adicionar limitacão de taxa.

## Passo prévio: importar uma API

Se já tiver uma API no Azure API Management, ótimo, pode saltar este passo. Caso contrário, consulte este link, [importando uma API para Azure API Management](https://learn.microsoft.com/en-us/azure/api-management/import-and-publish#import-and-publish-a-backend-api).

## Expor API como servidor MCP

Para expor os endpoints da API, siga estes passos:

1. Navegue até ao Portal Azure e para o endereço a seguir <https://portal.azure.com/?Microsoft_Azure_ApiManagement=mcp> 
Navegue até à sua instância de API Management.

1. No menu à esquerda, selecione APIs > MCP Servers > + Criar novo Servidor MCP.

1. Em API, selecione uma REST API para expor como servidor MCP.

1. Selecione uma ou mais Operações da API para expor como ferramentas. Pode selecionar todas as operações ou apenas operações específicas.

    ![Selecionar métodos para expor](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/create-mcp-server-small.png)


1. Selecione **Criar**.

1. Navegue para a opção do menu **APIs** e **MCP Servers**, deverá ver o seguinte:

    ![Ver o Servidor MCP no painel principal](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-list.png)

    O servidor MCP foi criado e as operações API estão expostas como ferramentas. O servidor MCP é listado no painel MCP Servers. A coluna URL mostra o endpoint do servidor MCP que pode chamar para teste ou dentro de uma aplicação cliente.

## Opcional: Configurar políticas

O Azure API Management tem o conceito base de políticas onde configura diferentes regras para os seus endpoints, como por exemplo limitacão de taxa ou cache semântico. Estas políticas são escritas em XML.

Aqui está como pode configurar uma política para limitar a taxa do seu Servidor MCP:

1. No portal, em APIs, selecione **MCP Servers**.

1. Selecione o servidor MCP que criou.

1. No menu à esquerda, sob MCP, selecione **Políticas**.

1. No editor de políticas, adicione ou edite as políticas que deseja aplicar às ferramentas do servidor MCP. As políticas são definidas em formato XML. Por exemplo, pode adicionar uma política para limitar chamadas às ferramentas do servidor MCP (neste exemplo, 5 chamadas por 30 segundos por endereço IP do cliente). Aqui está o XML que faz a limitacão de taxa:

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

Vamos garantir que nosso Servidor MCP funciona conforme pretendido.

> [!NOTE]
> Atualmente, o Azure API Management expõe este servidor através do endpoint Streamable
> HTTP `/mcp`. O transporte mais antigo HTTP+SSE `/sse` está obsoleto e
> deve ser usado apenas com clientes legados.

Para isso, usaremos o Visual Studio Code e o GitHub Copilot no modo Agent. Iremos adicionar o servidor MCP a um *mcp.json*. Assim, o Visual Studio Code atuará como cliente com capacidades agentic e os utilizadores finais poderão digitar um prompt e interagir com o referido servidor.

Vamos ver como, para adicionar o servidor MCP no Visual Studio Code:

1. Use o comando MCP: **Add Server a partir do Command Palette**.

1. Quando solicitado, selecione o tipo de servidor: **HTTP (HTTP ou Server Sent Events)**.

1. Insira a URL HTTP Streamable mostrada para o servidor MCP no API Management.
    Por exemplo:
    `https://<apim-service-name>.azure-api.net/<api-name>-mcp/mcp`.

1. Insira um ID para o servidor de sua escolha. Este valor não é importante, mas ajuda a lembrar qual instância do servidor é esta.

1. Selecione se deseja guardar a configuração nas definições do workspace ou nas definições do utilizador.

  - **Definições do workspace** - A configuração do servidor é guardada num ficheiro .vscode/mcp.json disponível apenas no workspace atual.

    *mcp.json*

    ```json
    "servers": {
        "APIM petstore" : {
            "type": "http",
            "url": "url-to-mcp-server/mcp"
        }
    }
    ```

  - **Definições do utilizador** - A configuração do servidor é adicionada ao seu ficheiro global *settings.json* e está disponível em todos os workspaces. A configuração é similar à seguinte:

    ![Definições do utilizador](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-servers-visual-studio-code.png)

1. Também precisa de adicionar uma configuração, um header para garantir que autentica corretamente no Azure API Management. Usa um header chamado **Ocp-Apim-Subscription-Key**.

    - Aqui está como pode adicioná-lo às definições:

    ![Adicionar header para autenticação](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-with-header-visual-studio-code.png), isto fará surgir um prompt a pedir o valor da chave API que pode encontrar no Portal Azure para a sua instância do Azure API Management.

   - Para adicioná-lo a *mcp.json* em vez disso, pode adicioná-lo assim:

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

### Usar modo Agent

Agora estamos todos configurados, seja nas definições ou no *.vscode/mcp.json*. Vamos experimentar.

Deve existir um ícone Ferramentas assim, onde as ferramentas expostas pelo seu servidor estão listadas:

![Ferramentas do servidor](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/tools-button-visual-studio-code.png)

1. Clique no ícone de ferramentas e deverá ver uma lista de ferramentas assim:

    ![Ferramentas](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/select-tools-visual-studio-code.png)

1. Insira um prompt no chat para invocar a ferramenta. Por exemplo, se selecionou uma ferramenta para obter informação sobre uma encomenda, pode perguntar ao agente sobre uma encomenda. Aqui está um prompt de exemplo:

    ```text
    get information from order 2
    ```

    Agora será apresentado com um ícone de ferramentas pedindo para prosseguir a chamada da ferramenta. Selecione para continuar a executar a ferramenta, agora deverá ver uma saída assim:

    ![Resultado do prompt](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/chat-results-visual-studio-code.png)

    **o que vê acima depende das ferramentas que configurou, mas a ideia é que receba uma resposta textual como acima**


## Referências

Aqui está como pode aprender mais:

- [Tutorial sobre Azure API Management e MCP](https://learn.microsoft.com/en-us/azure/api-management/export-rest-mcp-server)
- [Exemplo em Python: proteger servidores MCP remotos usando Azure API Management (experimental)](https://github.com/Azure-Samples/remote-mcp-apim-functions-python)

- [Laboratório de autorização de cliente MCP](https://github.com/Azure-Samples/AI-Gateway/tree/main/labs/mcp-client-authorization)

- [Use a extensão Azure API Management para VS Code para importar e gerir APIs](https://learn.microsoft.com/en-us/azure/api-management/visual-studio-code-tutorial)

- [Registar e descobrir servidores MCP remotos no Azure API Center](https://learn.microsoft.com/en-us/azure/api-center/register-discover-mcp-server)
- [AI Gateway](https://github.com/Azure-Samples/AI-Gateway) Excelente repositório que mostra muitas capacidades de IA com Azure API Management
- [Workshops AI Gateway](https://azure-samples.github.io/AI-Gateway/)  Contém workshops usando Azure Portal, uma ótima forma de começar a avaliar capacidades de IA.

## Próximos passos

- Voltar para: [Visão Geral dos Estudos de Caso](./README.md)
- Seguinte: [Agentes de Viagem Azure AI](./travelagentsample.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas resultantes da utilização desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->