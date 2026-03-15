# Implementação Prática

[![Como Construir, Testar e Implantar Aplicativos MCP com Ferramentas e Fluxos de Trabalho Reais](../../../translated_images/pt-BR/05.64bea204e25ca891.webp)](https://youtu.be/vCN9-mKBDfQ)

_(Clique na imagem acima para assistir ao vídeo desta aula)_

A implementação prática é onde o poder do Modelo Context Protocol (MCP) se torna tangível. Embora entender a teoria e a arquitetura por trás do MCP seja importante, o valor real surge quando você aplica esses conceitos para construir, testar e implantar soluções que resolvem problemas do mundo real. Este capítulo faz a ponte entre o conhecimento conceitual e o desenvolvimento prático, guiando você pelo processo de dar vida a aplicações baseadas em MCP.

Seja desenvolvendo assistentes inteligentes, integrando IA em fluxos de trabalho empresariais ou construindo ferramentas personalizadas para processamento de dados, o MCP fornece uma base flexível. Seu design independente de linguagem e SDKs oficiais para linguagens de programação populares o tornam acessível a uma ampla gama de desenvolvedores. Ao aproveitar esses SDKs, você pode prototipar rapidamente, iterar e escalar suas soluções em diferentes plataformas e ambientes.

Nas seções seguintes, você encontrará exemplos práticos, códigos de exemplo e estratégias de implantação que demonstram como implementar MCP em C#, Java com Spring, TypeScript, JavaScript e Python. Você também aprenderá a depurar e testar seus servidores MCP, gerenciar APIs e implantar soluções na nuvem usando Azure. Esses recursos práticos foram projetados para acelerar seu aprendizado e ajudar você a construir com confiança aplicações MCP robustas e prontas para produção.

## Visão Geral

Esta aula foca nos aspectos práticos da implementação MCP em múltiplas linguagens de programação. Exploraremos como usar os SDKs MCP em C#, Java com Spring, TypeScript, JavaScript e Python para construir aplicações robustas, depurar e testar servidores MCP, e criar recursos, prompts e ferramentas reutilizáveis.

## Objetivos de Aprendizagem

Ao final desta aula, você será capaz de:

- Implementar soluções MCP usando SDKs oficiais em várias linguagens de programação
- Depurar e testar servidores MCP sistematicamente
- Criar e usar recursos do servidor (Resources, Prompts e Tools)
- Projetar fluxos de trabalho MCP eficazes para tarefas complexas
- Otimizar implementações MCP para desempenho e confiabilidade

## Recursos Oficiais dos SDKs

O Model Context Protocol oferece SDKs oficiais para várias linguagens (alinhados com a [Especificação MCP 2025-11-25](https://spec.modelcontextprotocol.io/specification/2025-11-25/)):

- [SDK C#](https://github.com/modelcontextprotocol/csharp-sdk)
- [SDK Java com Spring](https://github.com/modelcontextprotocol/java-sdk) **Nota:** requer dependência do [Project Reactor](https://projectreactor.io). (Veja [discussão issue 246](https://github.com/orgs/modelcontextprotocol/discussions/246).)
- [SDK TypeScript](https://github.com/modelcontextprotocol/typescript-sdk)
- [SDK Python](https://github.com/modelcontextprotocol/python-sdk)
- [SDK Kotlin](https://github.com/modelcontextprotocol/kotlin-sdk)
- [SDK Go](https://github.com/modelcontextprotocol/go-sdk)

## Trabalhando com os SDKs MCP

Esta seção fornece exemplos práticos de implementação MCP em múltiplas linguagens. Você pode encontrar códigos de exemplo no diretório `samples` organizados por linguagem.

### Exemplos Disponíveis

O repositório inclui [implementações de exemplo](../../../04-PracticalImplementation/samples) nas seguintes linguagens:

- [C#](./samples/csharp/README.md)
- [Java com Spring](./samples/java/containerapp/README.md)
- [TypeScript](./samples/typescript/README.md)
- [JavaScript](./samples/javascript/README.md)
- [Python](./samples/python/README.md)

Cada exemplo demonstra conceitos chave do MCP e padrões de implementação para aquela linguagem e ecossistema específicos.

### Guias Práticos

Guias adicionais para implementação prática MCP:

- [Paginação e Conjuntos de Resultados Grandes](./pagination/README.md) - Manipule paginação baseada em cursor para ferramentas, recursos e conjuntos de dados grandes

## Funcionalidades Centrais do Servidor

Servidores MCP podem implementar qualquer combinação destes recursos:

### Recursos (Resources)

Os recursos fornecem contexto e dados para uso pelo usuário ou modelo de IA:

- Repositórios de documentos
- Bases de conhecimento
- Fontes de dados estruturados
- Sistemas de arquivos

### Prompts

Prompts são mensagens e fluxos de trabalho templateados para usuários:

- Templates de conversa pré-definidos
- Padrões guiados de interação
- Estruturas de diálogo especializadas

### Ferramentas (Tools)

As ferramentas são funções para o modelo de IA executar:

- Utilitários de processamento de dados
- Integrações com APIs externas
- Capacidades computacionais
- Funcionalidade de busca

## Implementações de Exemplo: Implementação em C#

O repositório oficial do SDK C# contém várias implementações de exemplo demonstrando diferentes aspectos do MCP:

- **Cliente MCP Básico**: exemplo simples mostrando como criar um cliente MCP e chamar ferramentas
- **Servidor MCP Básico**: implementação mínima de servidor com registro básico de ferramenta
- **Servidor MCP Avançado**: servidor completo com registro de ferramentas, autenticação e tratamento de erros
- **Integração ASP.NET**: exemplos demonstrando integração com ASP.NET Core
- **Padrões de Implementação de Ferramentas**: vários padrões para implementar ferramentas com diferentes níveis de complexidade

O SDK MCP C# está em prévia e as APIs podem mudar. Atualizaremos continuamente este blog conforme o SDK evoluir.

### Funcionalidades Principais

- [Nuget MCP C# ModelContextProtocol](https://www.nuget.org/packages/ModelContextProtocol)
- Construindo seu [primeiro Servidor MCP](https://devblogs.microsoft.com/dotnet/build-a-model-context-protocol-mcp-server-in-csharp/).

Para exemplos completos de implementação C#, visite o [repositório oficial de exemplos C# do SDK](https://github.com/modelcontextprotocol/csharp-sdk)

## Implementação Exemplo: Implementação Java com Spring

O SDK Java com Spring oferece opções robustas de implementação MCP com recursos próprios para nível empresarial.

### Funcionalidades Principais

- Integração com Spring Framework
- Forte segurança de tipos
- Suporte a programação reativa
- Tratamento completo de erros

Para um exemplo completo de implementação Java com Spring, veja [exemplo Java com Spring](samples/java/containerapp/README.md) no diretório de exemplos.

## Implementação Exemplo: Implementação JavaScript

O SDK JavaScript oferece uma abordagem leve e flexível para implementação MCP.

### Funcionalidades Principais

- Suporte para Node.js e navegador
- API baseada em Promises
- Integração fácil com Express e outros frameworks
- Suporte a WebSocket para streaming

Para um exemplo completo de implementação JavaScript, veja [exemplo JavaScript](samples/javascript/README.md) no diretório de exemplos.

## Implementação Exemplo: Implementação Python

O SDK Python oferece uma abordagem pythonica para implementação MCP com integrações excelentes a frameworks de ML.

### Funcionalidades Principais

- Suporte async/await com asyncio
- Integração FastAPI
- Registro simples de ferramentas
- Integração nativa com bibliotecas populares de ML

Para um exemplo completo de implementação Python, veja [exemplo Python](samples/python/README.md) no diretório de exemplos.

## Gerenciamento de API

O Azure API Management é uma ótima solução para como podemos assegurar servidores MCP. A ideia é colocar uma instância do Azure API Management na frente do seu servidor MCP e deixá-lo gerenciar recursos que provavelmente você desejará como:

- limitação de taxa
- gerenciamento de tokens
- monitoramento
- balanceamento de carga
- segurança

### Exemplo Azure

Aqui está um exemplo Azure fazendo exatamente isso, ou seja, [criando um servidor MCP e assegurando-o com Azure API Management](https://github.com/Azure-Samples/remote-mcp-apim-functions-python).

Veja como o fluxo de autorização acontece na imagem abaixo:

![APIM-MCP](https://github.com/Azure-Samples/remote-mcp-apim-functions-python/blob/main/mcp-client-authorization.gif?raw=true)

Na imagem anterior, acontece o seguinte:

- Autenticação/Autorização ocorre usando Microsoft Entra.
- Azure API Management atua como um gateway e usa políticas para direcionar e gerenciar o tráfego.
- Azure Monitor registra todas as requisições para análise futura.

#### Fluxo de autorização

Vamos ver o fluxo de autorização com mais detalhes:

![Diagram de Sequência](https://github.com/Azure-Samples/remote-mcp-apim-functions-python/blob/main/infra/app/apim-oauth/diagrams/images/mcp-client-auth.png?raw=true)

#### Especificação de autorização MCP

Saiba mais sobre a [Especificação de Autorização MCP](https://spec.modelcontextprotocol.io/specification/2025-11-25/basic/authorization/)

## Implantando Servidor Remoto MCP no Azure

Vamos ver se conseguimos implantar o exemplo que mencionamos anteriormente:

1. Clone o repositório

    ```bash
    git clone https://github.com/Azure-Samples/remote-mcp-apim-functions-python.git
    cd remote-mcp-apim-functions-python
    ```

1. Registre o provedor de recursos `Microsoft.App`.

   - Se você estiver usando o Azure CLI, execute `az provider register --namespace Microsoft.App --wait`.
   - Se você estiver usando Azure PowerShell, execute `Register-AzResourceProvider -ProviderNamespace Microsoft.App`. Depois, execute `(Get-AzResourceProvider -ProviderNamespace Microsoft.App).RegistrationState` após algum tempo para verificar se o registro está completo.

1. Execute este comando [azd](https://aka.ms/azd) para provisionar o serviço de gerenciamento de API, function app (com código) e todos os demais recursos Azure necessários

    ```shell
    azd up
    ```

    Este comando deve implantar todos os recursos na nuvem no Azure

### Testando seu servidor com MCP Inspector

1. Em uma **nova janela de terminal**, instale e execute o MCP Inspector

    ```shell
    npx @modelcontextprotocol/inspector
    ```

    Você deverá ver uma interface similar a:

    ![Conectar ao Node inspector](../../../translated_images/pt-BR/connect.141db0b2bd05f096.webp)

1. CTRL clique para carregar o app web MCP Inspector a partir da URL exibida pelo app (ex: [http://127.0.0.1:6274/#resources](http://127.0.0.1:6274/#resources))
1. Defina o tipo de transporte para `SSE`
1. Defina a URL para seu endpoint SSE do API Management exibido após o comando `azd up` e **Conecte**:

    ```shell
    https://<apim-servicename-from-azd-output>.azure-api.net/mcp/sse
    ```

1. **Listar Ferramentas**. Clique em uma ferramenta e **Executar Ferramenta**.

Se todos os passos funcionaram, você deve estar agora conectado ao servidor MCP e ter conseguido chamar uma ferramenta.

## Servidores MCP para Azure

[Remote-mcp-functions](https://github.com/Azure-Samples/remote-mcp-functions-dotnet): Este conjunto de repositórios é um template de inicialização rápida para construir e implantar servidores MCP remotos personalizados usando Azure Functions com Python, C# .NET ou Node/TypeScript.

Os exemplos fornecem uma solução completa que permite aos desenvolvedores:

- Construir e executar localmente: Desenvolver e depurar um servidor MCP em uma máquina local
- Implantar no Azure: Implante facilmente na nuvem com um simples comando azd up
- Conectar a partir de clientes: Conecte-se ao servidor MCP a partir de vários clientes, incluindo o modo agente Copilot do VS Code e a ferramenta MCP Inspector

### Funcionalidades Principais

- Segurança por design: O servidor MCP é protegido usando chaves e HTTPS
- Opções de autenticação: Suporta OAuth usando autenticação embutida e/ou API Management
- Isolamento de rede: Permite isolamento de rede usando Azure Virtual Networks (VNET)
- Arquitetura sem servidor: Aproveita Azure Functions para execução escalável e acionada por eventos
- Desenvolvimento local: Suporte abrangente para desenvolvimento e depuração local
- Implantação simples: Processo de implantação simplificado para Azure

O repositório inclui todos os arquivos de configuração necessários, código fonte e definições de infraestrutura para começar rapidamente com uma implementação de servidor MCP pronta para produção.

- [Azure Remote MCP Functions Python](https://github.com/Azure-Samples/remote-mcp-functions-python) - Exemplo de implementação MCP usando Azure Functions com Python

- [Azure Remote MCP Functions .NET](https://github.com/Azure-Samples/remote-mcp-functions-dotnet) - Exemplo de implementação MCP usando Azure Functions com C# .NET

- [Azure Remote MCP Functions Node/Typescript](https://github.com/Azure-Samples/remote-mcp-functions-typescript) - Exemplo de implementação MCP usando Azure Functions com Node/TypeScript.

## Principais Lições

- SDKs MCP fornecem ferramentas específicas por linguagem para implementar soluções MCP robustas
- O processo de depuração e teste é crítico para aplicações MCP confiáveis
- Templates de prompt reutilizáveis permitem interações IA consistentes
- Fluxos de trabalho bem projetados podem orquestrar tarefas complexas usando múltiplas ferramentas
- Implementar soluções MCP requer consideração de segurança, desempenho e tratamento de erros

## Exercício

Desenhe um fluxo de trabalho MCP prático que aborde um problema real em seu domínio:

1. Identifique 3-4 ferramentas que seriam úteis para resolver este problema
2. Crie um diagrama de fluxo mostrando como essas ferramentas interagem
3. Implemente uma versão básica de uma das ferramentas usando sua linguagem preferida
4. Crie um template de prompt que ajude o modelo a usar eficazmente sua ferramenta

## Recursos Adicionais

---

## O que vem a seguir

Próximo: [Tópicos Avançados](../05-AdvancedTopics/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original, em seu idioma nativo, deve ser considerado a fonte autoritária. Para informações críticas, recomenda-se a tradução profissional realizada por um humano. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações equivocadas decorrentes do uso desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->