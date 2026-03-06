# Implementação Prática

[![Como Construir, Testar e Desdobrar Aplicações MCP com Ferramentas e Fluxos de Trabalho Reais](../../../translated_images/pt-PT/05.64bea204e25ca891.webp)](https://youtu.be/vCN9-mKBDfQ)

_(Clique na imagem acima para ver o vídeo desta lição)_

A implementação prática é onde o poder do Model Context Protocol (MCP) se torna tangível. Embora entender a teoria e a arquitetura por trás do MCP seja importante, o valor real surge quando aplicamos estes conceitos para construir, testar e desdobrar soluções que resolvem problemas do mundo real. Este capítulo faz a ponte entre o conhecimento conceptual e o desenvolvimento prático, orientando-o no processo de dar vida a aplicações baseadas em MCP.

Quer esteja a desenvolver assistentes inteligentes, a integrar IA em fluxos de trabalho empresariais, ou a construir ferramentas personalizadas para processamento de dados, o MCP oferece uma base flexível. O seu design agnóstico quanto à linguagem e os SDKs oficiais para linguagens de programação populares tornam-no acessível a uma larga gama de desenvolvedores. Aproveitando estes SDKs, pode rapidamente prototipar, iterar e escalar as suas soluções em diferentes plataformas e ambientes.

Nas secções seguintes, encontrará exemplos práticos, código de amostra e estratégias de implementação que demonstram como implementar MCP em C#, Java com Spring, TypeScript, JavaScript e Python. Também aprenderá a depurar e testar os seus servidores MCP, gerir APIs e desdobrar soluções na cloud utilizando Azure. Estes recursos práticos foram concebidos para acelerar a sua aprendizagem e ajudá-lo a construir com confiança aplicações MCP robustas e prontas para produção.

## Visão Geral

Esta lição foca-se em aspetos práticos da implementação MCP em múltiplas linguagens de programação. Exploraremos como usar os SDKs MCP em C#, Java com Spring, TypeScript, JavaScript e Python para construir aplicações robustas, depurar e testar servidores MCP, e criar recursos, prompts e ferramentas reutilizáveis.

## Objetivos de Aprendizagem

No final desta lição, será capaz de:

- Implementar soluções MCP usando os SDKs oficiais em várias linguagens de programação
- Depurar e testar servidores MCP de forma sistemática
- Criar e usar funcionalidades do servidor (Recursos, Prompts e Ferramentas)
- Projetar fluxos de trabalho MCP eficazes para tarefas complexas
- Otimizar implementações MCP para desempenho e fiabilidade

## Recursos Oficiais dos SDK

O Model Context Protocol oferece SDKs oficiais para várias linguagens (alinhados com a [Especificação MCP 2025-11-25](https://spec.modelcontextprotocol.io/specification/2025-11-25/)):

- [SDK C#](https://github.com/modelcontextprotocol/csharp-sdk)
- [SDK Java com Spring](https://github.com/modelcontextprotocol/java-sdk) **Nota:** requer dependência do [Project Reactor](https://projectreactor.io). (Veja [discussão issue 246](https://github.com/orgs/modelcontextprotocol/discussions/246).)
- [SDK TypeScript](https://github.com/modelcontextprotocol/typescript-sdk)
- [SDK Python](https://github.com/modelcontextprotocol/python-sdk)
- [SDK Kotlin](https://github.com/modelcontextprotocol/kotlin-sdk)
- [SDK Go](https://github.com/modelcontextprotocol/go-sdk)

## Trabalhar com os SDKs MCP

Esta secção fornece exemplos práticos de implementação MCP em várias linguagens de programação. Pode encontrar código de exemplo no diretório `samples`, organizado por linguagem.

### Exemplos Disponíveis

O repositório inclui [implementações de exemplo](../../../04-PracticalImplementation/samples) nas seguintes linguagens:

- [C#](./samples/csharp/README.md)
- [Java com Spring](./samples/java/containerapp/README.md)
- [TypeScript](./samples/typescript/README.md)
- [JavaScript](./samples/javascript/README.md)
- [Python](./samples/python/README.md)

Cada exemplo demonstra conceitos-chave MCP e padrões de implementação para essa linguagem específica e ecossistema.

### Guias Práticos

Guias adicionais para implementação prática MCP:

- [Paginação e Conjuntos Grandes de Resultados](./pagination/README.md) - Gestão de paginação baseada em cursor para ferramentas, recursos e grandes conjuntos de dados

## Funcionalidades Principais do Servidor

Servidores MCP podem implementar qualquer combinação destas funcionalidades:

### Recursos

Recursos fornecem contexto e dados para o utilizador ou modelo de IA usar:

- Repositórios de documentos
- Bases de conhecimento
- Fontes de dados estruturados
- Sistemas de ficheiros

### Prompts

Prompts são mensagens e fluxos de trabalho modelados para os utilizadores:

- Templates pré-definidos para conversação
- Padrões de interação guiada
- Estruturas especializadas de diálogo

### Ferramentas

Ferramentas são funções que o modelo de IA pode executar:

- Utilitários de processamento de dados
- Integrações com APIs externas
- Capacidades computacionais
- Funcionalidade de pesquisa

## Implementações Exemplares: Implementação em C#

O repositório oficial do SDK C# contém várias implementações de amostra que demonstram diferentes aspetos do MCP:

- **Cliente MCP Básico**: Exemplo simples mostrando como criar um cliente MCP e chamar ferramentas
- **Servidor MCP Básico**: Implementação mínima de servidor com registo básico de ferramentas
- **Servidor MCP Avançado**: Servidor completo com registo de ferramentas, autenticação e tratamento de erros
- **Integração ASP.NET**: Exemplos que demonstram integração com ASP.NET Core
- **Padrões de Implementação de Ferramentas**: Vários padrões para implementar ferramentas com diferentes níveis de complexidade

O SDK MCP C# está em pré-visualização e as APIs podem mudar. Iremos atualizar continuamente este blog à medida que o SDK evolui.

### Funcionalidades-Chave

- [ModelContextProtocol Nuget MCP C#](https://www.nuget.org/packages/ModelContextProtocol)
- Construir o seu [primeiro Servidor MCP](https://devblogs.microsoft.com/dotnet/build-a-model-context-protocol-mcp-server-in-csharp/).

Para exemplos completos de implementação em C#, visite o [repositório oficial de amostras do SDK C#](https://github.com/modelcontextprotocol/csharp-sdk)

## Implementação exemplar: Implementação Java com Spring

O SDK Java com Spring oferece opções robustas de implementação MCP com características a nível empresarial.

### Funcionalidades-Chave

- Integração com Spring Framework
- Forte segurança de tipos
- Suporte a programação reativa
- Tratamento de erros abrangente

Para um exemplo completo de implementação Java com Spring, veja o [exemplo Java com Spring](samples/java/containerapp/README.md) no diretório de amostras.

## Implementação exemplar: Implementação JavaScript

O SDK JavaScript fornece uma abordagem leve e flexível para a implementação MCP.

### Funcionalidades-Chave

- Suporte para Node.js e browser
- API baseada em Promises
- Integração fácil com Express e outros frameworks
- Suporte WebSocket para streaming

Para um exemplo completo de implementação JavaScript, veja o [exemplo JavaScript](samples/javascript/README.md) no diretório de amostras.

## Implementação exemplar: Implementação Python

O SDK Python oferece uma abordagem Pythonica para a implementação MCP com excelentes integrações em frameworks ML.

### Funcionalidades-Chave

- Suporte async/await com asyncio
- Integração com FastAPI`
- Registo simples de ferramentas
- Integração nativa com bibliotecas populares de ML

Para um exemplo completo de implementação Python, veja o [exemplo Python](samples/python/README.md) no diretório de amostras.

## Gestão de API

O Azure API Management é uma excelente resposta para assegurar servidores MCP. A ideia é colocar uma instância do Azure API Management à frente do seu Servidor MCP e deixar que esta gere funcionalidades que provavelmente desejará, como:

- limitação de taxa
- gestão de tokens
- monitorização
- balanceamento de carga
- segurança

### Exemplo Azure

Aqui está um exemplo Azure a fazer exatamente isso, ou seja, [criar um servidor MCP e assegurá-lo com Azure API Management](https://github.com/Azure-Samples/remote-mcp-apim-functions-python).

Veja como decorre o fluxo de autorização na imagem abaixo:

![APIM-MCP](https://github.com/Azure-Samples/remote-mcp-apim-functions-python/blob/main/mcp-client-authorization.gif?raw=true)

Na imagem precedente, acontece o seguinte:

- Autenticação/Autorização ocorre usando Microsoft Entra.
- Azure API Management atua como um gateway e usa políticas para direcionar e gerir o tráfego.
- O Azure Monitor regista todos os pedidos para análise posterior.

#### Fluxo de autorização

Vamos analisar o fluxo de autorização com mais detalhe:

![Sequence Diagram](https://github.com/Azure-Samples/remote-mcp-apim-functions-python/blob/main/infra/app/apim-oauth/diagrams/images/mcp-client-auth.png?raw=true)

#### Especificação de autorização MCP

Saiba mais sobre a [Especificação de Autorização MCP](https://spec.modelcontextprotocol.io/specification/2025-11-25/basic/authorization/)

## Desdobrar Servidor MCP Remoto no Azure

Vamos ver se conseguimos desdobrar o exemplo mencionado anteriormente:

1. Clone o repositório

    ```bash
    git clone https://github.com/Azure-Samples/remote-mcp-apim-functions-python.git
    cd remote-mcp-apim-functions-python
    ```

1. Registe o fornecedor de recursos `Microsoft.App`.

   - Se estiver a usar Azure CLI, execute `az provider register --namespace Microsoft.App --wait`.
   - Se estiver a usar Azure PowerShell, execute `Register-AzResourceProvider -ProviderNamespace Microsoft.App`. Depois de algum tempo, execute `(Get-AzResourceProvider -ProviderNamespace Microsoft.App).RegistrationState` para verificar se o registo está concluído.

1. Execute este comando [azd](https://aka.ms/azd) para provisionar o serviço de gestão de API, a aplicação de funções (com código) e todos os outros recursos Azure necessários

    ```shell
    azd up
    ```

    Este comando deverá implantar todos os recursos de cloud no Azure

### Testar o seu servidor com MCP Inspector

1. Numa **nova janela de terminal**, instale e execute o MCP Inspector

    ```shell
    npx @modelcontextprotocol/inspector
    ```

    Deve visualizar uma interface semelhante a:

    ![Connect to Node inspector](../../../translated_images/pt-PT/connect.141db0b2bd05f096.webp)

1. Clique com CTRL para carregar a aplicação web MCP Inspector a partir da URL exibida pela aplicação (ex. [http://127.0.0.1:6274/#resources](http://127.0.0.1:6274/#resources))
1. Defina o tipo de transporte como `SSE`
1. Defina a URL para o seu endpoint SSE do API Management que está a correr, mostrado após o comando `azd up` e **Ligue**:

    ```shell
    https://<apim-servicename-from-azd-output>.azure-api.net/mcp/sse
    ```

1. **Listar Ferramentas**. Clique numa ferramenta e **Executar Ferramenta**.

Se todos os passos funcionaram, agora deve estar ligado ao servidor MCP e conseguiu chamar uma ferramenta.

## Servidores MCP para Azure

[Remote-mcp-functions](https://github.com/Azure-Samples/remote-mcp-functions-dotnet): Este conjunto de repositórios são templates de início rápido para construir e implementar servidores remotos MCP (Model Context Protocol) personalizados usando Azure Functions com Python, C# .NET ou Node/TypeScript.

As Amostras fornecem uma solução completa que permite aos desenvolvedores:

- Construir e executar localmente: Desenvolver e depurar um servidor MCP numa máquina local
- Desdobrar para Azure: Implementar facilmente na cloud com um simples comando azd up
- Conectar a partir de clientes: Conectar ao servidor MCP a partir de vários clientes, incluindo o modo agente Copilot do VS Code e a ferramenta MCP Inspector

### Funcionalidades-Chave

- Segurança por design: O servidor MCP é protegido usando chaves e HTTPS
- Opções de autenticação: Suporta OAuth usando autenticação incorporada e/ou API Management
- Isolamento de rede: Permite isolamento de rede usando Azure Virtual Networks (VNET)
- Arquitetura serverless: Aproveita Azure Functions para execução escalável e orientada a eventos
- Desenvolvimento local: Suporte completo para desenvolvimento local e depuração
- Desdobramento simples: Processo de desdobramento simplificado para Azure

O repositório inclui todos os ficheiros de configuração necessários, código fonte e definições de infraestrutura para começar rapidamente com uma implementação MCP pronta para produção.

- [Azure Remote MCP Functions Python](https://github.com/Azure-Samples/remote-mcp-functions-python) - Implementação de exemplo de MCP usando Azure Functions com Python

- [Azure Remote MCP Functions .NET](https://github.com/Azure-Samples/remote-mcp-functions-dotnet) - Implementação de exemplo de MCP usando Azure Functions com C# .NET

- [Azure Remote MCP Functions Node/Typescript](https://github.com/Azure-Samples/remote-mcp-functions-typescript) - Implementação de exemplo de MCP usando Azure Functions com Node/TypeScript.

## Principais Conclusões

- Os SDKs MCP fornecem ferramentas específicas para cada linguagem para implementar soluções MCP robustas
- O processo de depuração e teste é crucial para aplicações MCP fiáveis
- Templates reutilizáveis de prompts permitem interações consistentes com IA
- Fluxos de trabalho bem projetados podem orquestrar tarefas complexas utilizando múltiplas ferramentas
- Implementar soluções MCP exige consideração sobre segurança, desempenho e tratamento de erros

## Exercício

Projete um fluxo de trabalho MCP prático que resolva um problema do mundo real no seu domínio:

1. Identifique 3-4 ferramentas que seriam úteis para resolver este problema
2. Crie um diagrama de fluxo de trabalho mostrando como essas ferramentas interagem
3. Implemente uma versão básica de uma das ferramentas usando a sua linguagem preferida
4. Crie um modelo de prompt que ajude o modelo a usar efetivamente a sua ferramenta

## Recursos Adicionais

---

## O que vem a seguir

Próximo: [Tópicos Avançados](../05-AdvancedTopics/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos por garantir a precisão, por favor tenha em atenção que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte fiável. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações erradas resultantes da utilização desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->