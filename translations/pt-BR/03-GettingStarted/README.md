## Introdução  

[![Construa Seu Primeiro Servidor MCP](../../../translated_images/pt-BR/04.0ea920069efd979a0b2dad51e72c1df7ead9c57b3305796068a6cee1f0dd6674.png)](https://youtu.be/sNDZO9N4m9Y)

_(Clique na imagem acima para assistir ao vídeo desta lição)_

Esta seção consiste em várias lições:

- **1 Seu primeiro servidor**, nesta primeira lição, você aprenderá como criar seu primeiro servidor e inspecioná-lo com a ferramenta de inspeção, uma maneira valiosa de testar e depurar seu servidor, [para a lição](01-first-server/README.md)

- **2 Cliente**, nesta lição, você aprenderá como escrever um cliente que pode se conectar ao seu servidor, [para a lição](02-client/README.md)

- **3 Cliente com LLM**, uma maneira ainda melhor de escrever um cliente é adicionando um LLM para que ele possa "negociar" com seu servidor sobre o que fazer, [para a lição](03-llm-client/README.md)

- **4 Consumindo um servidor no modo GitHub Copilot Agent no Visual Studio Code**. Aqui, veremos como executar nosso Servidor MCP dentro do Visual Studio Code, [para a lição](04-vscode/README.md)

- **5 Servidor de Transporte stdio**. O transporte stdio é o padrão recomendado para comunicação entre servidor e cliente MCP na especificação atual, fornecendo comunicação segura baseada em subprocessos, [para a lição](05-stdio-server/README.md)

- **6 Streaming HTTP com MCP (HTTP Streamable)**. Aprenda sobre streaming HTTP moderno, notificações de progresso e como implementar servidores e clientes MCP escaláveis e em tempo real usando HTTP Streamable. [para a lição](06-http-streaming/README.md)

- **7 Utilizando o AI Toolkit para VSCode** para consumir e testar seus Clientes e Servidores MCP [para a lição](07-aitk/README.md)

- **8 Testes**. Aqui, focaremos especialmente em como podemos testar nosso servidor e cliente de diferentes maneiras, [para a lição](08-testing/README.md)

- **9 Implantação**. Este capítulo abordará diferentes maneiras de implantar suas soluções MCP, [para a lição](09-deployment/README.md)

- **10 Uso avançado do servidor**. Este capítulo cobre o uso avançado do servidor, [para a lição](./10-advanced/README.md)

- **11 Autenticação**. Este capítulo aborda como adicionar autenticação simples, desde Basic Auth até o uso de JWT e RBAC. É recomendável começar aqui e depois explorar Tópicos Avançados no Capítulo 5 e realizar reforço adicional de segurança por meio das recomendações do Capítulo 2, [para a lição](./11-simple-auth/README.md)

O Protocolo de Contexto de Modelo (MCP) é um protocolo aberto que padroniza como aplicativos fornecem contexto para LLMs. Pense no MCP como uma porta USB-C para aplicativos de IA - ele fornece uma maneira padronizada de conectar modelos de IA a diferentes fontes de dados e ferramentas.

## Objetivos de Aprendizagem

Ao final desta lição, você será capaz de:

- Configurar ambientes de desenvolvimento para MCP em C#, Java, Python, TypeScript e JavaScript
- Construir e implantar servidores MCP básicos com recursos personalizados (recursos, prompts e ferramentas)
- Criar aplicativos host que se conectam a servidores MCP
- Testar e depurar implementações MCP
- Compreender desafios comuns de configuração e suas soluções
- Conectar suas implementações MCP a serviços populares de LLM

## Configurando Seu Ambiente MCP

Antes de começar a trabalhar com MCP, é importante preparar seu ambiente de desenvolvimento e entender o fluxo de trabalho básico. Esta seção irá guiá-lo pelos passos iniciais de configuração para garantir um início tranquilo com MCP.

### Pré-requisitos

Antes de mergulhar no desenvolvimento MCP, certifique-se de ter:

- **Ambiente de Desenvolvimento**: Para a linguagem escolhida (C#, Java, Python, TypeScript ou JavaScript)
- **IDE/Editor**: Visual Studio, Visual Studio Code, IntelliJ, Eclipse, PyCharm ou qualquer editor de código moderno
- **Gerenciadores de Pacotes**: NuGet, Maven/Gradle, pip ou npm/yarn
- **Chaves de API**: Para quaisquer serviços de IA que você planeja usar em seus aplicativos host

### SDKs Oficiais

Nos capítulos seguintes, você verá soluções construídas usando Python, TypeScript, Java e .NET. Aqui estão todos os SDKs oficialmente suportados.

O MCP fornece SDKs oficiais para várias linguagens:
- [SDK C#](https://github.com/modelcontextprotocol/csharp-sdk) - Mantido em colaboração com a Microsoft
- [SDK Java](https://github.com/modelcontextprotocol/java-sdk) - Mantido em colaboração com Spring AI
- [SDK TypeScript](https://github.com/modelcontextprotocol/typescript-sdk) - Implementação oficial em TypeScript
- [SDK Python](https://github.com/modelcontextprotocol/python-sdk) - Implementação oficial em Python
- [SDK Kotlin](https://github.com/modelcontextprotocol/kotlin-sdk) - Implementação oficial em Kotlin
- [SDK Swift](https://github.com/modelcontextprotocol/swift-sdk) - Mantido em colaboração com Loopwork AI
- [SDK Rust](https://github.com/modelcontextprotocol/rust-sdk) - Implementação oficial em Rust

## Principais Pontos

- Configurar um ambiente de desenvolvimento MCP é simples com SDKs específicos para cada linguagem
- Construir servidores MCP envolve criar e registrar ferramentas com esquemas claros
- Clientes MCP conectam-se a servidores e modelos para aproveitar capacidades estendidas
- Testes e depuração são essenciais para implementações MCP confiáveis
- As opções de implantação variam de desenvolvimento local a soluções baseadas em nuvem

## Praticando

Temos um conjunto de exemplos que complementa os exercícios que você verá em todos os capítulos desta seção. Além disso, cada capítulo também possui seus próprios exercícios e tarefas.

- [Calculadora em Java](./samples/java/calculator/README.md)
- [Calculadora em .Net](../../../03-GettingStarted/samples/csharp)
- [Calculadora em JavaScript](./samples/javascript/README.md)
- [Calculadora em TypeScript](./samples/typescript/README.md)
- [Calculadora em Python](../../../03-GettingStarted/samples/python)

## Recursos Adicionais

- [Construa Agentes usando o Protocolo de Contexto de Modelo no Azure](https://learn.microsoft.com/azure/developer/ai/intro-agents-mcp)
- [MCP Remoto com Azure Container Apps (Node.js/TypeScript/JavaScript)](https://learn.microsoft.com/samples/azure-samples/mcp-container-ts/mcp-container-ts/)
- [Agente MCP OpenAI em .NET](https://learn.microsoft.com/samples/azure-samples/openai-mcp-agent-dotnet/openai-mcp-agent-dotnet/)

## O que vem a seguir

Próximo: [Criando seu primeiro Servidor MCP](01-first-server/README.md)

---

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autoritativa. Para informações críticas, recomenda-se a tradução profissional realizada por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações equivocadas decorrentes do uso desta tradução.