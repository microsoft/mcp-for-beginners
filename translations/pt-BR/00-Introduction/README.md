# Introdução ao Protocolo de Contexto de Modelo (MCP): Por que ele é importante para aplicações de IA escaláveis

[![Introdução ao Protocolo de Contexto de Modelo](../../../translated_images/pt-BR/01.a467036d886b5fb5b9cf7b39bac0e743b6ca0a4a18a492de90061daaf0cc55f0.png)](https://youtu.be/agBbdiOPLQA)

_(Clique na imagem acima para assistir ao vídeo desta lição)_

Aplicações de IA generativa representam um grande avanço, pois frequentemente permitem que o usuário interaja com o aplicativo usando prompts em linguagem natural. No entanto, à medida que mais tempo e recursos são investidos nesses aplicativos, é importante garantir que você possa integrar funcionalidades e recursos de forma que seja fácil expandir, que seu aplicativo possa atender a mais de um modelo sendo usado e lidar com diversas complexidades dos modelos. Em resumo, construir aplicativos de IA generativa é fácil no início, mas conforme eles crescem e se tornam mais complexos, você precisa começar a definir uma arquitetura e provavelmente precisará contar com um padrão para garantir que seus aplicativos sejam construídos de maneira consistente. É aqui que o MCP entra em cena para organizar as coisas e fornecer um padrão.

---

## **🔍 O que é o Protocolo de Contexto de Modelo (MCP)?**

O **Protocolo de Contexto de Modelo (MCP)** é uma **interface aberta e padronizada** que permite que Modelos de Linguagem de Grande Escala (LLMs) interajam perfeitamente com ferramentas externas, APIs e fontes de dados. Ele fornece uma arquitetura consistente para aprimorar a funcionalidade dos modelos de IA além de seus dados de treinamento, permitindo sistemas de IA mais inteligentes, escaláveis e responsivos.

---

## **🎯 Por que a padronização em IA é importante**

À medida que as aplicações de IA generativa se tornam mais complexas, é essencial adotar padrões que garantam **escalabilidade, extensibilidade, manutenção** e **evitem dependência de fornecedores**. O MCP atende a essas necessidades ao:

- Unificar integrações entre modelos e ferramentas
- Reduzir soluções personalizadas frágeis e pontuais
- Permitir que múltiplos modelos de diferentes fornecedores coexistam em um único ecossistema

**Nota:** Embora o MCP se apresente como um padrão aberto, não há planos para padronizar o MCP por meio de órgãos de padronização existentes, como IEEE, IETF, W3C, ISO ou qualquer outro.

---

## **📚 Objetivos de Aprendizado**

Ao final deste artigo, você será capaz de:

- Definir o **Protocolo de Contexto de Modelo (MCP)** e seus casos de uso
- Entender como o MCP padroniza a comunicação entre modelos e ferramentas
- Identificar os componentes principais da arquitetura do MCP
- Explorar aplicações reais do MCP em contextos empresariais e de desenvolvimento

---

## **💡 Por que o Protocolo de Contexto de Modelo (MCP) é revolucionário**

### **🔗 MCP resolve a fragmentação nas interações de IA**

Antes do MCP, integrar modelos com ferramentas exigia:

- Código personalizado para cada par ferramenta-modelo
- APIs não padronizadas para cada fornecedor
- Quebras frequentes devido a atualizações
- Baixa escalabilidade com mais ferramentas

### **✅ Benefícios da padronização do MCP**

| **Benefício**              | **Descrição**                                                                |
|--------------------------|--------------------------------------------------------------------------------|
| Interoperabilidade         | LLMs funcionam perfeitamente com ferramentas de diferentes fornecedores      |
| Consistência               | Comportamento uniforme entre plataformas e ferramentas                       |
| Reutilização               | Ferramentas criadas uma vez podem ser usadas em vários projetos e sistemas    |
| Desenvolvimento acelerado  | Reduz o tempo de desenvolvimento ao usar interfaces padronizadas e plug-and-play |

---

## **🧱 Visão geral da arquitetura de alto nível do MCP**

O MCP segue um **modelo cliente-servidor**, onde:

- **Hosts MCP** executam os modelos de IA
- **Clientes MCP** iniciam solicitações
- **Servidores MCP** fornecem contexto, ferramentas e capacidades

### **Componentes principais:**

- **Recursos** – Dados estáticos ou dinâmicos para os modelos  
- **Prompts** – Fluxos de trabalho predefinidos para geração guiada  
- **Ferramentas** – Funções executáveis como busca, cálculos  
- **Amostragem** – Comportamento agente por meio de interações recursivas  

---

## Como funcionam os servidores MCP

Os servidores MCP operam da seguinte forma:

- **Fluxo de Solicitação**:
    1. Uma solicitação é iniciada por um usuário final ou software agindo em seu nome.
    2. O **Cliente MCP** envia a solicitação para um **Host MCP**, que gerencia o tempo de execução do modelo de IA.
    3. O **Modelo de IA** recebe o prompt do usuário e pode solicitar acesso a ferramentas ou dados externos por meio de uma ou mais chamadas de ferramentas.
    4. O **Host MCP**, e não o modelo diretamente, comunica-se com os **Servidores MCP** apropriados usando o protocolo padronizado.
- **Funcionalidade do Host MCP**:
    - **Registro de Ferramentas**: Mantém um catálogo de ferramentas disponíveis e suas capacidades.
    - **Autenticação**: Verifica permissões para acesso às ferramentas.
    - **Manipulador de Solicitações**: Processa solicitações de ferramentas recebidas do modelo.
    - **Formatador de Respostas**: Estrutura as saídas das ferramentas em um formato que o modelo possa entender.
- **Execução do Servidor MCP**:
    - O **Host MCP** encaminha chamadas de ferramentas para um ou mais **Servidores MCP**, cada um expondo funções especializadas (por exemplo, busca, cálculos, consultas de banco de dados).
    - Os **Servidores MCP** realizam suas respectivas operações e retornam resultados ao **Host MCP** em um formato consistente.
    - O **Host MCP** formata e retransmite esses resultados ao **Modelo de IA**.
- **Conclusão da Resposta**:
    - O **Modelo de IA** incorpora as saídas das ferramentas em uma resposta final.
    - O **Host MCP** envia essa resposta de volta ao **Cliente MCP**, que a entrega ao usuário final ou ao software que fez a chamada.

```mermaid
---
title: MCP Architecture and Component Interactions
description: A diagram showing the flows of the components in MCP.
---
graph TD
    Client[MCP Client/Application] -->|Sends Request| H[MCP Host]
    H -->|Invokes| A[AI Model]
    A -->|Tool Call Request| H
    H -->|MCP Protocol| T1[MCP Server Tool 01: Web Search]
    H -->|MCP Protocol| T2[MCP Server Tool 02: Calculator tool]
    H -->|MCP Protocol| T3[MCP Server Tool 03: Database Access tool]
    H -->|MCP Protocol| T4[MCP Server Tool 04: File System tool]
    H -->|Sends Response| Client

    subgraph "MCP Host Components"
        H
        G[Tool Registry]
        I[Authentication]
        J[Request Handler]
        K[Response Formatter]
    end

    H <--> G
    H <--> I
    H <--> J
    H <--> K

    style A fill:#f9d5e5,stroke:#333,stroke-width:2px
    style H fill:#eeeeee,stroke:#333,stroke-width:2px
    style Client fill:#d5e8f9,stroke:#333,stroke-width:2px
    style G fill:#fffbe6,stroke:#333,stroke-width:1px
    style I fill:#fffbe6,stroke:#333,stroke-width:1px
    style J fill:#fffbe6,stroke:#333,stroke-width:1px
    style K fill:#fffbe6,stroke:#333,stroke-width:1px
    style T1 fill:#c2f0c2,stroke:#333,stroke-width:1px
    style T2 fill:#c2f0c2,stroke:#333,stroke-width:1px
    style T3 fill:#c2f0c2,stroke:#333,stroke-width:1px
    style T4 fill:#c2f0c2,stroke:#333,stroke-width:1px
```

## 👨‍💻 Como construir um servidor MCP (com exemplos)

Os servidores MCP permitem que você estenda as capacidades dos LLMs fornecendo dados e funcionalidades.

Pronto para experimentar? Aqui estão SDKs específicos de linguagem e/ou stack com exemplos de criação de servidores MCP simples em diferentes linguagens/stacks:

- **SDK Python**: https://github.com/modelcontextprotocol/python-sdk

- **SDK TypeScript**: https://github.com/modelcontextprotocol/typescript-sdk

- **SDK Java**: https://github.com/modelcontextprotocol/java-sdk

- **SDK C#/.NET**: https://github.com/modelcontextprotocol/csharp-sdk

## 🌍 Casos de uso reais para MCP

O MCP possibilita uma ampla gama de aplicações ao estender as capacidades da IA:

| **Aplicação**              | **Descrição**                                                                |
|------------------------------|--------------------------------------------------------------------------------|
| Integração de Dados Empresariais  | Conectar LLMs a bancos de dados, CRMs ou ferramentas internas              |
| Sistemas de IA Agentes           | Permitir agentes autônomos com acesso a ferramentas e fluxos de decisão    |
| Aplicações Multimodais            | Combinar ferramentas de texto, imagem e áudio em um único aplicativo de IA |
| Integração de Dados em Tempo Real | Trazer dados ao vivo para interações de IA para resultados mais precisos e atuais |

### 🧠 MCP = Padrão Universal para Interações de IA

O Protocolo de Contexto de Modelo (MCP) atua como um padrão universal para interações de IA, assim como o USB-C padronizou conexões físicas para dispositivos. No mundo da IA, o MCP fornece uma interface consistente, permitindo que modelos (clientes) integrem-se perfeitamente com ferramentas externas e provedores de dados (servidores). Isso elimina a necessidade de protocolos diversos e personalizados para cada API ou fonte de dados.

Sob o MCP, uma ferramenta compatível com MCP (referida como servidor MCP) segue um padrão unificado. Esses servidores podem listar as ferramentas ou ações que oferecem e executar essas ações quando solicitadas por um agente de IA. Plataformas de agentes de IA que suportam MCP são capazes de descobrir ferramentas disponíveis nos servidores e invocá-las por meio desse protocolo padrão.

### 💡 Facilita o acesso ao conhecimento

Além de oferecer ferramentas, o MCP também facilita o acesso ao conhecimento. Ele permite que aplicativos forneçam contexto a modelos de linguagem de grande escala (LLMs) ao conectá-los a várias fontes de dados. Por exemplo, um servidor MCP pode representar o repositório de documentos de uma empresa, permitindo que agentes recuperem informações relevantes sob demanda. Outro servidor pode lidar com ações específicas, como enviar e-mails ou atualizar registros. Do ponto de vista do agente, essas são simplesmente ferramentas que ele pode usar—algumas ferramentas retornam dados (contexto de conhecimento), enquanto outras realizam ações. O MCP gerencia ambos de forma eficiente.

Um agente conectado a um servidor MCP aprende automaticamente as capacidades disponíveis e os dados acessíveis do servidor por meio de um formato padrão. Essa padronização permite a disponibilidade dinâmica de ferramentas. Por exemplo, adicionar um novo servidor MCP ao sistema de um agente torna suas funções imediatamente utilizáveis sem exigir personalização adicional das instruções do agente.

Essa integração simplificada está alinhada com o fluxo representado no diagrama a seguir, onde os servidores fornecem tanto ferramentas quanto conhecimento, garantindo colaboração perfeita entre sistemas.

### 👉 Exemplo: Solução de Agente Escalável

```mermaid
---
title: Scalable Agent Solution with MCP
description: A diagram illustrating how a user interacts with an LLM that connects to multiple MCP servers, with each server providing both knowledge and tools, creating a scalable AI system architecture
---
graph TD
    User -->|Prompt| LLM
    LLM -->|Response| User
    LLM -->|MCP| ServerA
    LLM -->|MCP| ServerB
    ServerA -->|Universal connector| ServerB
    ServerA --> KnowledgeA
    ServerA --> ToolsA
    ServerB --> KnowledgeB
    ServerB --> ToolsB

    subgraph Server A
        KnowledgeA[Knowledge]
        ToolsA[Tools]
    end

    subgraph Server B
        KnowledgeB[Knowledge]
        ToolsB[Tools]
    end
```
O Conector Universal permite que servidores MCP se comuniquem e compartilhem capacidades entre si, permitindo que o ServerA delegue tarefas ao ServerB ou acesse suas ferramentas e conhecimentos. Isso federa ferramentas e dados entre servidores, suportando arquiteturas de agentes escaláveis e modulares. Como o MCP padroniza a exposição de ferramentas, os agentes podem descobrir dinamicamente e encaminhar solicitações entre servidores sem integrações codificadas.

Federação de ferramentas e conhecimento: Ferramentas e dados podem ser acessados entre servidores, permitindo arquiteturas de agentes mais escaláveis e modulares.

### 🔄 Cenários avançados de MCP com integração de LLM no lado do cliente

Além da arquitetura básica do MCP, existem cenários avançados onde tanto o cliente quanto o servidor contêm LLMs, permitindo interações mais sofisticadas. No diagrama a seguir, o **App Cliente** poderia ser um IDE com várias ferramentas MCP disponíveis para uso pelo LLM:

```mermaid
---
title: Advanced MCP Scenarios with Client-Server LLM Integration
description: A sequence diagram showing the detailed interaction flow between user, client application, client LLM, multiple MCP servers, and server LLM, illustrating tool discovery, user interaction, direct tool calling, and feature negotiation phases
---
sequenceDiagram
    autonumber
    actor User as 👤 User
    participant ClientApp as 🖥️ Client App
    participant ClientLLM as 🧠 Client LLM
    participant Server1 as 🔧 MCP Server 1
    participant Server2 as 📚 MCP Server 2
    participant ServerLLM as 🤖 Server LLM
    
    %% Discovery Phase
    rect rgb(220, 240, 255)
        Note over ClientApp, Server2: TOOL DISCOVERY PHASE
        ClientApp->>+Server1: Request available tools/resources
        Server1-->>-ClientApp: Return tool list (JSON)
        ClientApp->>+Server2: Request available tools/resources
        Server2-->>-ClientApp: Return tool list (JSON)
        Note right of ClientApp: Store combined tool<br/>catalog locally
    end
    
    %% User Interaction
    rect rgb(255, 240, 220)
        Note over User, ClientLLM: USER INTERACTION PHASE
        User->>+ClientApp: Enter natural language prompt
        ClientApp->>+ClientLLM: Forward prompt + tool catalog
        ClientLLM->>-ClientLLM: Analyze prompt & select tools
    end
    
    %% Scenario A: Direct Tool Calling
    alt Direct Tool Calling
        rect rgb(220, 255, 220)
            Note over ClientApp, Server1: SCENARIO A: DIRECT TOOL CALLING
            ClientLLM->>+ClientApp: Request tool execution
            ClientApp->>+Server1: Execute specific tool
            Server1-->>-ClientApp: Return results
            ClientApp->>+ClientLLM: Process results
            ClientLLM-->>-ClientApp: Generate response
            ClientApp-->>-User: Display final answer
        end
    
    %% Scenario B: Feature Negotiation (VS Code style)
    else Feature Negotiation (VS Code style)
        rect rgb(255, 220, 220)
            Note over ClientApp, ServerLLM: SCENARIO B: FEATURE NEGOTIATION
            ClientLLM->>+ClientApp: Identify needed capabilities
            ClientApp->>+Server2: Negotiate features/capabilities
            Server2->>+ServerLLM: Request additional context
            ServerLLM-->>-Server2: Provide context
            Server2-->>-ClientApp: Return available features
            ClientApp->>+Server2: Call negotiated tools
            Server2-->>-ClientApp: Return results
            ClientApp->>+ClientLLM: Process results
            ClientLLM-->>-ClientApp: Generate response
            ClientApp-->>-User: Display final answer
        end
    end
```

## 🔐 Benefícios práticos do MCP

Aqui estão os benefícios práticos de usar o MCP:

- **Atualidade**: Modelos podem acessar informações atualizadas além de seus dados de treinamento
- **Extensão de Capacidades**: Modelos podem aproveitar ferramentas especializadas para tarefas para as quais não foram treinados
- **Redução de Alucinações**: Fontes de dados externas fornecem fundamentação factual
- **Privacidade**: Dados sensíveis podem permanecer em ambientes seguros em vez de serem incorporados em prompts

## 📌 Principais pontos

Os seguintes são os principais pontos sobre o uso do MCP:

- O **MCP** padroniza como modelos de IA interagem com ferramentas e dados
- Promove **extensibilidade, consistência e interoperabilidade**
- O MCP ajuda a **reduzir o tempo de desenvolvimento, melhorar a confiabilidade e ampliar as capacidades dos modelos**
- A arquitetura cliente-servidor **permite aplicativos de IA flexíveis e extensíveis**

## 🧠 Exercício

Pense em um aplicativo de IA que você está interessado em construir.

- Quais **ferramentas ou dados externos** poderiam melhorar suas capacidades?
- Como o MCP poderia tornar a integração **mais simples e confiável?**

## Recursos adicionais

- [Repositório GitHub do MCP](https://github.com/modelcontextprotocol)

## O que vem a seguir

Próximo: [Capítulo 1: Conceitos Fundamentais](../01-CoreConcepts/README.md)

---

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, é importante estar ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte oficial. Para informações críticas, recomenda-se a tradução profissional realizada por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações equivocadas decorrentes do uso desta tradução.