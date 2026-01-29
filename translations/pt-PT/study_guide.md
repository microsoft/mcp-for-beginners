# Protocolo de Contexto de Modelo (MCP) para Iniciantes - Guia de Estudo

Este guia de estudo oferece uma visão geral da estrutura e do conteúdo do repositório para o currículo "Protocolo de Contexto de Modelo (MCP) para Iniciantes". Utilize este guia para navegar pelo repositório de forma eficiente e aproveitar ao máximo os recursos disponíveis.

## Visão Geral do Repositório

O Protocolo de Contexto de Modelo (MCP) é uma estrutura padronizada para interações entre modelos de IA e aplicações cliente. Inicialmente criado pela Anthropic, o MCP é agora mantido pela comunidade MCP através da organização oficial no GitHub. Este repositório fornece um currículo abrangente com exemplos práticos de código em C#, Java, JavaScript, Python e TypeScript, projetado para desenvolvedores de IA, arquitetos de sistemas e engenheiros de software.

## Mapa Visual do Currículo

```mermaid
mindmap
  root((MCP for Beginners))
    00. Introduction
      ::icon(fa fa-book)
      (Protocol Overview)
      (Standardization Benefits)
      (Real-world Use Cases)
      (AI Integration Fundamentals)
    01. Core Concepts
      ::icon(fa fa-puzzle-piece)
      (Client-Server Architecture)
      (Protocol Components)
      (Messaging Patterns)
      (Transport Mechanisms)
    02. Security
      ::icon(fa fa-shield)
      (AI-Specific Threats)
      (Best Practices 2025)
      (Azure Content Safety)
      (Auth & Authorization)
      (Microsoft Prompt Shields)
    03. Getting Started
      ::icon(fa fa-rocket)
      (First Server Implementation)
      (Client Development)
      (LLM Client Integration)
      (VS Code Extensions)
      (SSE Server Setup)
      (HTTP Streaming)
      (AI Toolkit Integration)
      (Testing Frameworks)
      (Advanced Server Usage)
      (Simple Auth)
      (Deployment Strategies)
    04. Practical Implementation
      ::icon(fa fa-code)
      (Multi-Language SDKs)
      (Testing & Debugging)
      (Prompt Templates)
      (Sample Projects)
      (Production Patterns)
    05. Advanced Topics
      ::icon(fa fa-graduation-cap)
      (Context Engineering)
      (Foundry Agent Integration)
      (Multi-modal AI Workflows)
      (OAuth2 Authentication)
      (Real-time Search)
      (Streaming Protocols)
      (Root Contexts)
      (Routing Strategies)
      (Sampling Techniques)
      (Scaling Solutions)
      (Security Hardening)
      (Entra ID Integration)
      (Web Search MCP)
      
    06. Community
      ::icon(fa fa-users)
      (Code Contributions)
      (Documentation)
      (MCP Client Ecosystem)
      (MCP Server Registry)
      (Image Generation Tools)
      (GitHub Collaboration)
    07. Early Adoption
      ::icon(fa fa-lightbulb)
      (Production Deployments)
      (Microsoft MCP Servers)
      (Azure MCP Service)
      (Enterprise Case Studies)
      (Future Roadmap)
    08. Best Practices
      ::icon(fa fa-check)
      (Performance Optimization)
      (Fault Tolerance)
      (System Resilience)
      (Monitoring & Observability)
    09. Case Studies
      ::icon(fa fa-file-text)
      (Azure API Management)
      (AI Travel Agent)
      (Azure DevOps Integration)
      (Documentation MCP)
      (GitHub MCP Registry)
      (VS Code Integration)
      (Real-world Implementations)
    10. Hands-on Workshop
      ::icon(fa fa-laptop)
      (MCP Server Fundamentals)
      (Advanced Development)
      (AI Toolkit Integration)
      (Production Deployment)
      (4-Lab Structure)
    11. Database Integration Labs
      ::icon(fa fa-database)
      (PostgreSQL Integration)
      (Retail Analytics Use Case)
      (Row Level Security)
      (Semantic Search)
      (Production Deployment)
      (13-Lab Structure)
      (Hands-on Learning)
```

## Estrutura do Repositório

O repositório está organizado em onze seções principais, cada uma focada em diferentes aspectos do MCP:

1. **Introdução (00-Introduction/)**
   - Visão geral do Protocolo de Contexto de Modelo
   - Por que a padronização é importante em pipelines de IA
   - Casos de uso práticos e benefícios

2. **Conceitos Fundamentais (01-CoreConcepts/)**
   - Arquitetura cliente-servidor
   - Componentes principais do protocolo
   - Padrões de mensagens no MCP

3. **Segurança (02-Security/)**
   - Ameaças de segurança em sistemas baseados em MCP
   - Melhores práticas para proteger implementações
   - Estratégias de autenticação e autorização
   - **Documentação Abrangente de Segurança**:
     - Melhores Práticas de Segurança MCP 2025
     - Guia de Implementação de Segurança de Conteúdo Azure
     - Controles e Técnicas de Segurança MCP
     - Referência Rápida de Melhores Práticas MCP
   - **Tópicos Principais de Segurança**:
     - Ataques de injeção de prompts e envenenamento de ferramentas
     - Sequestro de sessões e problemas de delegação confusa
     - Vulnerabilidades de passagem de tokens
     - Permissões excessivas e controle de acesso
     - Segurança da cadeia de suprimentos para componentes de IA
     - Integração com Microsoft Prompt Shields

4. **Primeiros Passos (03-GettingStarted/)**
   - Configuração e preparação do ambiente
   - Criação de servidores e clientes MCP básicos
   - Integração com aplicações existentes
   - Inclui seções sobre:
     - Primeira implementação de servidor
     - Desenvolvimento de cliente
     - Integração de cliente LLM
     - Integração com VS Code
     - Servidor de Eventos Enviados pelo Servidor (SSE)
     - Uso avançado de servidor
     - Streaming HTTP
     - Integração com AI Toolkit
     - Estratégias de teste
     - Diretrizes de implantação

5. **Implementação Prática (04-PracticalImplementation/)**
   - Uso de SDKs em diferentes linguagens de programação
   - Técnicas de depuração, teste e validação
   - Criação de templates de prompts reutilizáveis e fluxos de trabalho
   - Projetos de exemplo com implementações práticas

6. **Tópicos Avançados (05-AdvancedTopics/)**
   - Técnicas de engenharia de contexto
   - Integração de agentes Foundry
   - Fluxos de trabalho de IA multimodal
   - Demonstrações de autenticação OAuth2
   - Capacidades de busca em tempo real
   - Streaming em tempo real
   - Implementação de contextos raiz
   - Estratégias de roteamento
   - Técnicas de amostragem
   - Abordagens de escalabilidade
   - Considerações de segurança
   - Integração de segurança Entra ID
   - Integração com busca na web

7. **Contribuições da Comunidade (06-CommunityContributions/)**
   - Como contribuir com código e documentação
   - Colaboração via GitHub
   - Melhorias e feedback impulsionados pela comunidade
   - Uso de vários clientes MCP (Claude Desktop, Cline, VSCode)
   - Trabalho com servidores MCP populares, incluindo geração de imagens

8. **Lições da Adoção Inicial (07-LessonsfromEarlyAdoption/)**
   - Implementações reais e histórias de sucesso
   - Construção e implantação de soluções baseadas em MCP
   - Tendências e roadmap futuro
   - **Guia de Servidores MCP da Microsoft**: Guia abrangente para 10 servidores MCP prontos para produção da Microsoft, incluindo:
     - Servidor MCP Microsoft Learn Docs
     - Servidor MCP Azure (15+ conectores especializados)
     - Servidor MCP GitHub
     - Servidor MCP Azure DevOps
     - Servidor MCP MarkItDown
     - Servidor MCP SQL Server
     - Servidor MCP Playwright
     - Servidor MCP Dev Box
     - Servidor MCP Azure AI Foundry
     - Servidor MCP Microsoft 365 Agents Toolkit

9. **Melhores Práticas (08-BestPractices/)**
   - Ajuste de desempenho e otimização
   - Design de sistemas MCP tolerantes a falhas
   - Estratégias de teste e resiliência

10. **Estudos de Caso (09-CaseStudy/)**
    - **Sete estudos de caso abrangentes** demonstrando a versatilidade do MCP em diversos cenários:
    - **Agentes de Viagem Azure AI**: Orquestração multi-agente com Azure OpenAI e AI Search
    - **Integração Azure DevOps**: Automação de processos de fluxo de trabalho com atualizações de dados do YouTube
    - **Recuperação de Documentação em Tempo Real**: Cliente de console Python com streaming HTTP
    - **Gerador Interativo de Planos de Estudo**: Aplicação web Chainlit com IA conversacional
    - **Documentação no Editor**: Integração VS Code com fluxos de trabalho do GitHub Copilot
    - **Gestão de API Azure**: Integração de API empresarial com criação de servidor MCP
    - **Registro MCP GitHub**: Desenvolvimento de ecossistema e plataforma de integração agentic
    - Exemplos de implementação abrangendo integração empresarial, produtividade de desenvolvedores e desenvolvimento de ecossistemas

11. **Workshop Prático (10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/)**
    - Workshop prático abrangente combinando MCP com AI Toolkit
    - Construção de aplicações inteligentes que conectam modelos de IA com ferramentas do mundo real
    - Módulos práticos cobrindo fundamentos, desenvolvimento de servidor personalizado e estratégias de implantação em produção
    - **Estrutura do Laboratório**:
      - Laboratório 1: Fundamentos do Servidor MCP
      - Laboratório 2: Desenvolvimento Avançado de Servidor MCP
      - Laboratório 3: Integração com AI Toolkit
      - Laboratório 4: Implantação e Escalabilidade em Produção
    - Abordagem de aprendizado baseada em laboratório com instruções passo a passo

12. **Laboratórios de Integração de Servidor MCP com Base de Dados (11-MCPServerHandsOnLabs/)**
    - **Caminho de aprendizado abrangente com 13 laboratórios** para construir servidores MCP prontos para produção com integração PostgreSQL
    - **Implementação de análise de varejo no mundo real** usando o caso de uso Zava Retail
    - **Padrões de nível empresarial** incluindo Segurança de Nível de Linha (RLS), busca semântica e acesso a dados multi-inquilino
    - **Estrutura Completa do Laboratório**:
      - **Laboratórios 00-03: Fundamentos** - Introdução, Arquitetura, Segurança, Configuração do Ambiente
      - **Laboratórios 04-06: Construção do Servidor MCP** - Design de Base de Dados, Implementação de Servidor MCP, Desenvolvimento de Ferramentas
      - **Laboratórios 07-09: Recursos Avançados** - Busca Semântica, Teste e Depuração, Integração com VS Code
      - **Laboratórios 10-12: Produção e Melhores Práticas** - Implantação, Monitoramento, Otimização
    - **Tecnologias Abrangidas**: Framework FastMCP, PostgreSQL, Azure OpenAI, Azure Container Apps, Application Insights
    - **Resultados de Aprendizado**: Servidores MCP prontos para produção, padrões de integração de base de dados, análises impulsionadas por IA, segurança empresarial

## Recursos Adicionais

O repositório inclui recursos de apoio:

- **Pasta de Imagens**: Contém diagramas e ilustrações usados ao longo do currículo
- **Traduções**: Suporte multilíngue com traduções automáticas da documentação
- **Recursos Oficiais MCP**:
  - [Documentação MCP](https://modelcontextprotocol.io/)
  - [Especificação MCP](https://spec.modelcontextprotocol.io/)
  - [Repositório GitHub MCP](https://github.com/modelcontextprotocol)

## Como Utilizar Este Repositório

1. **Aprendizado Sequencial**: Siga os capítulos em ordem (00 a 11) para uma experiência de aprendizado estruturada.
2. **Foco Específico em Linguagem**: Se estiver interessado em uma linguagem de programação específica, explore os diretórios de exemplos para implementações na sua linguagem preferida.
3. **Implementação Prática**: Comece pela seção "Primeiros Passos" para configurar seu ambiente e criar seu primeiro servidor e cliente MCP.
4. **Exploração Avançada**: Após dominar os fundamentos, mergulhe nos tópicos avançados para expandir seu conhecimento.
5. **Engajamento Comunitário**: Junte-se à comunidade MCP através de discussões no GitHub e canais no Discord para conectar-se com especialistas e outros desenvolvedores.

## Clientes e Ferramentas MCP

O currículo aborda vários clientes e ferramentas MCP:

1. **Clientes Oficiais**:
   - Visual Studio Code 
   - MCP no Visual Studio Code
   - Claude Desktop
   - Claude no VSCode 
   - Claude API

2. **Clientes da Comunidade**:
   - Cline (baseado em terminal)
   - Cursor (editor de código)
   - ChatMCP
   - Windsurf

3. **Ferramentas de Gestão MCP**:
   - MCP CLI
   - MCP Manager
   - MCP Linker
   - MCP Router

## Servidores MCP Populares

O repositório apresenta vários servidores MCP, incluindo:

1. **Servidores MCP Oficiais da Microsoft**:
   - Servidor MCP Microsoft Learn Docs
   - Servidor MCP Azure (15+ conectores especializados)
   - Servidor MCP GitHub
   - Servidor MCP Azure DevOps
   - Servidor MCP MarkItDown
   - Servidor MCP SQL Server
   - Servidor MCP Playwright
   - Servidor MCP Dev Box
   - Servidor MCP Azure AI Foundry
   - Servidor MCP Microsoft 365 Agents Toolkit

2. **Servidores de Referência Oficiais**:
   - Sistema de Arquivos
   - Fetch
   - Memória
   - Pensamento Sequencial

3. **Geração de Imagens**:
   - Azure OpenAI DALL-E 3
   - Stable Diffusion WebUI
   - Replicate

4. **Ferramentas de Desenvolvimento**:
   - Git MCP
   - Controle de Terminal
   - Assistente de Código

5. **Servidores Especializados**:
   - Salesforce
   - Microsoft Teams
   - Jira & Confluence

## Contribuindo

Este repositório acolhe contribuições da comunidade. Consulte a seção Contribuições da Comunidade para orientações sobre como contribuir de forma eficaz para o ecossistema MCP.

----

*Este guia de estudo foi atualizado em 6 de outubro de 2025 e fornece uma visão geral do repositório até essa data. O conteúdo do repositório pode ser atualizado após essa data.*

---

**Aviso**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, tenha em atenção que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autoritária. Para informações críticas, recomenda-se uma tradução profissional realizada por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes da utilização desta tradução.