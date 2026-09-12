## Começando  

[![Construa Seu Primeiro Servidor MCP](../../../translated_images/pt-BR/04.0ea920069efd979a.webp)](https://youtu.be/sNDZO9N4m9Y)

_(Clique na imagem acima para assistir ao vídeo desta aula)_

Esta seção consiste em várias aulas:

- **1 Seu primeiro servidor**, nesta primeira aula, você aprenderá como criar seu primeiro servidor e inspecioná-lo com a ferramenta de inspeção, uma forma valiosa de testar e depurar seu servidor, [para a aula](01-first-server/README.md)

- **2 Cliente**, nesta aula, você aprenderá como escrever um cliente que pode se conectar ao seu servidor, [para a aula](02-client/README.md)

- **3 Cliente com LLM**, uma forma ainda melhor de escrever um cliente é adicionando um LLM para que ele possa "negociar" com seu servidor sobre o que fazer, [para a aula](03-llm-client/README.md)

- **4 Consumindo um servidor no modo Agente GitHub Copilot no Visual Studio Code**. Aqui, analisamos como rodar nosso Servidor MCP dentro do Visual Studio Code, [para a aula](04-vscode/README.md)

- **5 Servidor com Transporte stdio** transporte stdio é o padrão recomendado para comunicação local servidor-cliente MCP, proporcionando comunicação segura baseada em subprocessos com isolamento de processos integrado [para a aula](05-stdio-server/README.md)

- **6 Streaming HTTP com MCP (HTTP Streamable)**. Aprenda sobre o padrão
	transporte remoto na [Especificação MCP 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/streamable-http),
	além da implementação legado baseada em sessão mantida na aula.
	[para a aula](06-http-streaming/README.md)

- **7 Utilizando o AI Toolkit para VSCode** para consumir e testar seus Clientes e Servidores MCP [para a aula](07-aitk/README.md)

- **8 Testes**. Aqui focaremos especialmente em como podemos testar nosso servidor e cliente de diferentes maneiras, [para a aula](08-testing/README.md)

- **9 Implantação**. Este capítulo analisará diferentes formas de implantar suas soluções MCP, [para a aula](09-deployment/README.md)

- **10 Uso avançado do servidor**. Este capítulo cobre o uso avançado do servidor, [para a aula](./10-advanced/README.md)

- **11 Autenticação**. Este capítulo cobre como adicionar autenticação simples, do Basic Auth ao uso de JWT e RBAC. Você é incentivado a começar aqui e depois olhar os Tópicos Avançados no Capítulo 5 e realizar reforço adicional de segurança pelas recomendações no Capítulo 2, [para a aula](./11-simple-auth/README.md)

- **12 Hosts MCP**. Configure e use clientes populares de host MCP incluindo Claude Desktop, Cursor, Cline e Windsurf. Aprenda tipos de transporte e resolução de problemas, [para a aula](./12-mcp-hosts/README.md)

- **13 Inspetor MCP**. Depure e teste seus servidores MCP interativamente usando a ferramenta MCP Inspector. Aprenda a resolver problemas com ferramentas, recursos e mensagens de protocolo, [para a aula](./13-mcp-inspector/README.md)

- **14 Amostragem**. Aprenda o primitivo legado de Amostragem para `2025-11-25` e
	como migrar novos designs para integração direta com provedores LLM. Amostragem está
	depreciada no MCP `2026-07-28`. [para a aula](./14-sampling/README.md)

- **15 Aplicações MCP**. Construa Servidores MCP que também respondem com instruções de UI, [para a aula](./15-mcp-apps/README.md)

O Protocolo de Contexto de Modelo (MCP) é um protocolo aberto que padroniza como as aplicações fornecem contexto para LLMs. Pense no MCP como uma porta USB-C para aplicações de IA — ele fornece uma maneira padronizada de conectar modelos de IA a diferentes fontes de dados e ferramentas.

## Objetivos de Aprendizagem

Ao final desta aula, você será capaz de:

- Configurar ambientes de desenvolvimento para MCP em C#, Java, Python, TypeScript e JavaScript
- Construir e implantar servidores MCP básicos com recursos personalizados (recursos, prompts e ferramentas)
- Criar aplicações host que conectem a servidores MCP
- Testar e depurar implementações MCP
- Compreender desafios comuns de configuração e suas soluções
- Conectar suas implementações MCP a serviços LLM populares

## Configurando Seu Ambiente MCP

Antes de começar a trabalhar com MCP, é importante preparar seu ambiente de desenvolvimento e entender o fluxo de trabalho básico. Esta seção irá guiá-lo pelos passos iniciais para garantir um começo suave com MCP.

### Pré-requisitos

Antes de mergulhar no desenvolvimento MCP, assegure-se de que você tem:

- **Ambiente de Desenvolvimento**: Para a linguagem escolhida (C#, Java, Python, TypeScript ou JavaScript)
- **IDE/Editor**: Visual Studio, Visual Studio Code, IntelliJ, Eclipse, PyCharm ou qualquer editor de código moderno
- **Gerenciadores de Pacotes**: NuGet, Maven/Gradle, pip ou npm/yarn
- **Chaves de API**: Para quaisquer serviços de IA que planeja usar em suas aplicações host


### SDKs Oficiais

Nos próximos capítulos você verá soluções construídas usando Python, TypeScript,
Java e .NET. Aqui estão os SDKs oficiais.

O suporte a SDK para MCP `2026-07-28` está sendo lançado independentemente por linguagem.
Antes de executar um exemplo, verifique a versão do pacote e as notas de lançamento do SDK
para revisões do protocolo suportadas. Veja a
[lista oficial de SDKs](https://modelcontextprotocol.io/docs/sdk):
- [SDK C#](https://github.com/modelcontextprotocol/csharp-sdk) - Mantido em colaboração com Microsoft
- [SDK Java](https://github.com/modelcontextprotocol/java-sdk) - Mantido em colaboração com Spring AI
- [SDK TypeScript](https://github.com/modelcontextprotocol/typescript-sdk) - A implementação oficial em TypeScript
- [SDK Python](https://github.com/modelcontextprotocol/python-sdk) - A implementação oficial em Python (FastMCP)
- [SDK Kotlin](https://github.com/modelcontextprotocol/kotlin-sdk) - A implementação oficial em Kotlin
- [SDK Swift](https://github.com/modelcontextprotocol/swift-sdk) - Mantido em colaboração com Loopwork AI
- [SDK Rust](https://github.com/modelcontextprotocol/rust-sdk) - A implementação oficial em Rust
- [SDK Go](https://github.com/modelcontextprotocol/go-sdk) - A implementação oficial em Go

## Principais Lições

- Configurar um ambiente de desenvolvimento MCP é simples com SDKs específicos para cada linguagem
- Construir servidores MCP envolve criar e registrar ferramentas com esquemas claros
- Clientes MCP conectam-se a servidores e modelos para aproveitar capacidades estendidas
- Testes e depuração são essenciais para implementações MCP confiáveis
- As opções de implantação vão desde desenvolvimento local até soluções baseadas em nuvem

## Praticando


Temos um conjunto de exemplos que complementa os exercícios que você verá em todos os capítulos desta seção. Além disso, cada capítulo também tem seus próprios exercícios e tarefas

- [Calculadora Java](./samples/java/calculator/README.md)
- [Calculadora .NET](../../../03-GettingStarted/samples/csharp)
- [Calculadora JavaScript](./samples/javascript/README.md)
- [Calculadora TypeScript](./samples/typescript/README.md)
- [Calculadora Python](../../../03-GettingStarted/samples/python)

## Recursos Adicionais

- [Construa Agentes usando o Protocolo de Contexto de Modelo no Azure](https://learn.microsoft.com/azure/developer/ai/intro-agents-mcp)
- [MCP Remoto com Azure Container Apps (Node.js/TypeScript/JavaScript)](https://learn.microsoft.com/samples/azure-samples/mcp-container-ts/mcp-container-ts/)
- [Agente MCP OpenAI .NET](https://learn.microsoft.com/samples/azure-samples/openai-mcp-agent-dotnet/openai-mcp-agent-dotnet/)

## O que vem a seguir

Comece com a primeira lição: [Criando seu primeiro Servidor MCP](01-first-server/README.md)

Depois de concluir este módulo, continue para: [Módulo 4: Implementação Prática](../04-PracticalImplementation/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido usando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, por favor, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->