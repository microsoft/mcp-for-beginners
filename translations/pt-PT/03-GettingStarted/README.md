## Começar  

[![Construa o Seu Primeiro Servidor MCP](../../../translated_images/pt-PT/04.0ea920069efd979a.webp)](https://youtu.be/sNDZO9N4m9Y)

_(Clique na imagem acima para ver o vídeo desta lição)_

Esta secção consiste em várias lições:

- **1 O Seu Primeiro Servidor**, nesta primeira lição, aprenderá a criar o seu primeiro servidor e a inspecioná-lo com a ferramenta inspector, uma forma valiosa de testar e depurar o seu servidor, [para a lição](01-first-server/README.md)

- **2 Cliente**, nesta lição, aprenderá a escrever um cliente que possa ligar-se ao seu servidor, [para a lição](02-client/README.md)

- **3 Cliente com LLM**, uma forma ainda melhor de escrever um cliente é adicionando um LLM para que ele possa "negociar" com o seu servidor o que fazer, [para a lição](03-llm-client/README.md)

- **4 Consumir um modo Agente GitHub Copilot do servidor em Visual Studio Code**. Aqui, estamos a olhar para correr o nosso Servidor MCP dentro do Visual Studio Code, [para a lição](04-vscode/README.md)

- **5 Servidor de Transporte stdio** stdio transport é o padrão recomendado para comunicação local entre servidor MCP e cliente, fornecendo comunicação segura baseada em subprocessos com isolamento incorporado do processo [para a lição](05-stdio-server/README.md)

- **6 Streaming HTTP com MCP (HTTP Transmissível)**. Aprenda sobre o padrão
	transporte remoto na [Especificação MCP 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/streamable-http),
	além da implementação legada baseada em sessões mantida na lição.
	[para a lição](06-http-streaming/README.md)

- **7 Utilizar o Conjunto de Ferramentas AI para VSCode** para consumir e testar os seus Clientes e Servidores MCP [para a lição](07-aitk/README.md)

- **8 Testes**. Aqui vamos focar especialmente em como podemos testar o nosso servidor e cliente de várias maneiras, [para a lição](08-testing/README.md)

- **9 Implantação**. Este capítulo abordará diferentes formas de implantar as suas soluções MCP, [para a lição](09-deployment/README.md)

- **10 Uso avançado do servidor**. Este capítulo aborda o uso avançado do servidor, [para a lição](./10-advanced/README.md)

- **11 Autenticação**. Este capítulo aborda como adicionar autenticação simples, desde Autenticação Básica a usar JWT e RBAC. Recomenda-se começar aqui e depois olhar para Tópicos Avançados no Capítulo 5 e realizar endurecimento de segurança adicional via recomendações no Capítulo 2, [para a lição](./11-simple-auth/README.md)

- **12 Hosts MCP**. Configure e utilize clientes populares de host MCP incluindo Claude Desktop, Cursor, Cline e Windsurf. Aprenda tipos de transporte e resolução de problemas, [para a lição](./12-mcp-hosts/README.md)

- **13 Inspector MCP**. Depure e teste os seus servidores MCP de forma interativa usando a ferramenta Inspector MCP. Aprenda a resolver problemas de ferramentas, recursos e mensagens do protocolo, [para a lição](./13-mcp-inspector/README.md)

- **14 Amostragem**. Aprenda o primitivo legado de Amostragem para `2025-11-25` e
	como migrar novos designs para integração direta com provedores LLM. Amostragem está
	descontinuada no MCP `2026-07-28`. [para a lição](./14-sampling/README.md)

- **15 Aplicações MCP**. Construa Servidores MCP que também respondem com instruções de UI, [para a lição](./15-mcp-apps/README.md)

O Model Context Protocol (MCP) é um protocolo aberto que padroniza como as aplicações fornecem contexto aos LLMs. Pense no MCP como uma porta USB-C para aplicações de IA - ele fornece uma forma padronizada de conectar modelos de IA a diferentes fontes de dados e ferramentas.

## Objetivos de Aprendizagem

No final desta lição, será capaz de:

- Configurar ambientes de desenvolvimento para MCP em C#, Java, Python, TypeScript e JavaScript
- Construir e implantar servidores MCP básicos com funcionalidades personalizadas (recursos, prompts e ferramentas)
- Criar aplicações host que se conectem a servidores MCP
- Testar e depurar implementações MCP
- Compreender desafios comuns de configuração e as suas soluções
- Ligar as suas implementações MCP a serviços LLM populares

## Configurar o Seu Ambiente MCP

Antes de começar a trabalhar com MCP, é importante preparar o seu ambiente de desenvolvimento e entender o fluxo de trabalho básico. Esta secção irá guiá-lo pelos passos iniciais de configuração para garantir um início suave com MCP.

### Pré-requisitos

Antes de mergulhar no desenvolvimento MCP, assegure-se que tem:

- **Ambiente de Desenvolvimento**: Para a sua linguagem escolhida (C#, Java, Python, TypeScript ou JavaScript)
- **IDE/Editor**: Visual Studio, Visual Studio Code, IntelliJ, Eclipse, PyCharm ou qualquer editor de código moderno
- **Gestores de Pacotes**: NuGet, Maven/Gradle, pip, ou npm/yarn
- **Chaves API**: Para quaisquer serviços de IA que planeie usar nas suas aplicações host


### SDKs Oficiais

Nos capítulos seguintes verá soluções construídas usando Python, TypeScript,
Java e .NET. Aqui estão os SDKs oficiais.

O suporte do SDK para MCP `2026-07-28` está a ser disponibilizado de forma independente por linguagem.
Antes de executar um exemplo, verifique a versão do seu pacote e as notas de lançamento do SDK
para revisões de protocolo suportadas. Veja a
[lista oficial de SDK](https://modelcontextprotocol.io/docs/sdk):
- [SDK C#](https://github.com/modelcontextprotocol/csharp-sdk) - Mantido em colaboração com a Microsoft
- [SDK Java](https://github.com/modelcontextprotocol/java-sdk) - Mantido em colaboração com Spring AI
- [SDK TypeScript](https://github.com/modelcontextprotocol/typescript-sdk) - A implementação oficial em TypeScript
- [SDK Python](https://github.com/modelcontextprotocol/python-sdk) - A implementação oficial em Python (FastMCP)
- [SDK Kotlin](https://github.com/modelcontextprotocol/kotlin-sdk) - A implementação oficial em Kotlin
- [SDK Swift](https://github.com/modelcontextprotocol/swift-sdk) - Mantido em colaboração com Loopwork AI
- [SDK Rust](https://github.com/modelcontextprotocol/rust-sdk) - A implementação oficial em Rust
- [SDK Go](https://github.com/modelcontextprotocol/go-sdk) - A implementação oficial em Go

## Principais Conclusões

- Configurar um ambiente de desenvolvimento MCP é simples com SDKs específicos por linguagem
- Construir servidores MCP envolve criar e registar ferramentas com esquemas claros
- Clientes MCP ligam-se a servidores e modelos para aproveitar capacidades estendidas
- Testar e depurar são essenciais para implementações MCP fiáveis
- As opções de implantação variam de desenvolvimento local a soluções baseadas na cloud

## Praticar

Temos um conjunto de exemplos que complementa os exercícios que verá em todos os capítulos desta secção. Adicionalmente, cada capítulo tem também os seus próprios exercícios e tarefas

- [Calculadora Java](./samples/java/calculator/README.md)
- [Calculadora .NET](../../../03-GettingStarted/samples/csharp)
- [Calculadora JavaScript](./samples/javascript/README.md)
- [Calculadora TypeScript](./samples/typescript/README.md)
- [Calculadora Python](../../../03-GettingStarted/samples/python)

## Recursos Adicionais

- [Construir Agentes usando Model Context Protocol na Azure](https://learn.microsoft.com/azure/developer/ai/intro-agents-mcp)
- [MCP Remoto com Azure Container Apps (Node.js/TypeScript/JavaScript)](https://learn.microsoft.com/samples/azure-samples/mcp-container-ts/mcp-container-ts/)
- [Agente MCP .NET OpenAI](https://learn.microsoft.com/samples/azure-samples/openai-mcp-agent-dotnet/openai-mcp-agent-dotnet/)

## O que vem a seguir

Comece pela primeira lição: [Criar o seu primeiro Servidor MCP](01-first-server/README.md)

Depois de completar este módulo, continue para: [Módulo 4: Implementação Prática](../04-PracticalImplementation/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas resultantes da utilização desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->