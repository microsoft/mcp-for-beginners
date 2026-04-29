# Protocolo de Contexto do Modelo (MCP) para Iniciantes - Guia de Estudo

Este guia de estudo oferece uma visão geral da estrutura e do conteúdo do repositório para o currículo "Protocolo de Contexto do Modelo (MCP) para Iniciantes". Use este guia para navegar eficientemente pelo repositório e aproveitar ao máximo os recursos disponíveis.

## Visão Geral do Repositório

O Protocolo de Contexto do Modelo (MCP) é uma estrutura padronizada para interações entre modelos de IA e aplicações clientes. Inicialmente criado pela Anthropic, o MCP agora é mantido pela comunidade MCP mais ampla por meio da organização oficial no GitHub. Este repositório oferece um currículo abrangente com exemplos práticos em C#, Java, JavaScript, Python e TypeScript, projetado para desenvolvedores de IA, arquitetos de sistemas e engenheiros de software.

## Mapa Visual do Currículo

```mermaid
mindmap
  root((MCP para Iniciantes))
    00. Introdução
      ::icon(fa fa-book)
      (Visão Geral do Protocolo)
      (Benefícios da Padronização)
      (Casos de Uso no Mundo Real)
      (Fundamentos da Integração de IA)
    01. Conceitos Principais
      ::icon(fa fa-puzzle-piece)
      (Arquitetura Cliente-Servidor)
      (Componentes do Protocolo)
      (Padrões de Mensagens)
      (Mecanismos de Transporte)
      (Tarefas - Experimental)
      (Anotações de Ferramentas)
    02. Segurança
      ::icon(fa fa-shield)
      (Ameaças Específicas de IA)
      (Melhores Práticas 2025)
      (Segurança de Conteúdo do Azure)
      (Autenticação & Autorização)
      (Escudos de Prompt da Microsoft)
      (Top 10 MCP OWASP)
      (Workshop de Segurança Sherpa)
    03. Começando
      ::icon(fa fa-rocket)
      (Primeira Implementação do Servidor)
      (Desenvolvimento do Cliente)
      (Integração de Cliente LLM)
      (Extensões do VS Code)
      (Configuração do Servidor SSE)
      (Streaming HTTP)
      (Integração da Caixa de Ferramentas de IA)
      (Frameworks de Teste)
      (Uso Avançado do Servidor)
      (Autenticação Simples)
      (Estratégias de Implantação)
      (Configuração dos Hosts MCP)
      (Inspetor MCP)
    04. Implementação Prática
      ::icon(fa fa-code)
      (SDKs Multilíngues)
      (Testes & Depuração)
      (Modelos de Prompt)
      (Projetos de Exemplo)
      (Padrões de Produção)
      (Estratégias de Paginação)
    05. Tópicos Avançados
      ::icon(fa fa-graduation-cap)
      (Engenharia de Contexto)
      (Integração de Agente Foundry)
      (Fluxos de Trabalho Multimodais de IA)
      (Autenticação OAuth2)
      (Busca em Tempo Real)
      (Protocolos de Streaming)
      (Contextos Raiz)
      (Estratégias de Roteamento)
      (Técnicas de Amostragem)
      (Soluções de Escalabilidade)
      (Fortalecimento da Segurança)
      (Integração Entra ID)
      (Busca Web MCP)
      (Exploração Profunda de Recursos do Protocolo)
      (Raciocínio Multi-Agente Adversarial)
      
    06. Comunidade
      ::icon(fa fa-users)
      (Contribuições de Código)
      (Documentação)
      (Ecossistema Cliente MCP)
      (Registro do Servidor MCP)
      (Ferramentas de Geração de Imagens)
      (Colaboração no GitHub)
    07. Adoção Inicial
      ::icon(fa fa-lightbulb)
      (Implantações em Produção)
      (Servidores MCP Microsoft)
      (Serviço MCP Azure)
      (Estudos de Caso Corporativos)
      (Roteiro Futuro)
    08. Melhores Práticas
      ::icon(fa fa-check)
      (Otimização de Desempenho)
      (Tolerância a Falhas)
      (Resiliência do Sistema)
      (Monitoramento & Observabilidade)
    09. Estudos de Caso
      ::icon(fa fa-file-text)
      (Gerenciamento de API Azure)
      (Agente de Viagens com IA)
      (Integração Azure DevOps)
      (Documentação MCP)
      (Registro MCP no GitHub)
      (Integração VS Code)
      (Implementações no Mundo Real)
    10. Workshop Prático
      ::icon(fa fa-laptop)
      (Fundamentos do Servidor MCP)
      (Desenvolvimento Avançado)
      (Integração da Caixa de Ferramentas de IA)
      (Implantação em Produção)
      (Estrutura de 4 Laboratórios)
    11. Laboratórios de Integração de Banco de Dados
      ::icon(fa fa-database)
      (Integração PostgreSQL)
      (Caso de Uso de Análise Varejista)
      (Segurança em Nível de Linha)
      (Busca Semântica)
      (Implantação em Produção)
      (Estrutura de 13 Laboratórios)
      (Aprendizado Prático)
```
## Estrutura do Repositório

O repositório está organizado em onze seções principais, cada uma focando em diferentes aspectos do MCP:

1. **Introdução (00-Introduction/)**
   - Visão geral do Protocolo de Contexto do Modelo
   - Por que a padronização é importante em pipelines de IA
   - Casos de uso práticos e benefícios

2. **Conceitos Fundamentais (01-CoreConcepts/)**
   - Arquitetura cliente-servidor
   - Componentes chave do protocolo
   - Padrões de mensagens no MCP

3. **Segurança (02-Security/)**
   - Ameaças de segurança em sistemas baseados em MCP
   - Melhores práticas para proteger implementações
   - Estratégias de autenticação e autorização
   - **Documentação Abrangente de Segurança**:
     - Melhores Práticas de Segurança MCP 2025
     - Guia de Implementação de Segurança de Conteúdo do Azure
     - Controles e Técnicas de Segurança MCP
     - Referência Rápida de Melhores Práticas MCP
   - **Principais Tópicos de Segurança**:
     - Ataques de injeção de prompt e envenenamento de ferramentas
     - Sequestro de sessão e problemas de representante confuso
     - Vulnerabilidades de token passthrough
     - Permissões excessivas e controle de acesso
     - Segurança na cadeia de suprimentos para componentes de IA
     - Integração do Microsoft Prompt Shields

4. **Introdução Prática (03-GettingStarted/)**
   - Configuração e preparação do ambiente
   - Criando servidores e clientes MCP básicos
   - Integração com aplicações existentes
   - Inclui seções para:
     - Primeira implementação de servidor
     - Desenvolvimento de cliente
     - Integração de cliente LLM
     - Integração com VS Code
     - Servidor de Eventos Enviados pelo Servidor (SSE)
     - Uso avançado de servidor
     - Streaming HTTP
     - Integração com AI Toolkit
     - Estratégias de testes
     - Diretrizes de implantação

5. **Implementação Prática (04-PracticalImplementation/)**
   - Uso de SDKs em diferentes linguagens de programação
   - Técnicas de depuração, teste e validação
   - Criação de templates de prompt reutilizáveis e fluxos de trabalho
   - Projetos exemplares com exemplos de implementação

6. **Tópicos Avançados (05-AdvancedTopics/)**
   - Técnicas de engenharia de contexto
   - Integração com agente Foundry
   - Fluxos de trabalho multimodais de IA
   - Demonstrações de autenticação OAuth2
   - Capacidades de busca em tempo real
   - Streaming em tempo real
   - Implementação de contextos raiz
   - Estratégias de roteamento
   - Técnicas de amostragem
   - Abordagens de escalabilidade
   - Considerações de segurança
   - Integração de segurança Entra ID
   - Integração de busca na web
   - Raciocínio multiagente adversarial (padrões de debate)

7. **Contribuições da Comunidade (06-CommunityContributions/)**
   - Como contribuir com código e documentação
   - Colaboração via GitHub
   - Melhorias e feedbacks dirigidos pela comunidade
   - Uso de vários clientes MCP (Claude Desktop, Cline, VSCode)
   - Trabalho com servidores MCP populares incluindo geração de imagem

8. **Lições da Adoção Inicial (07-LessonsfromEarlyAdoption/)**
   - Implementações reais e histórias de sucesso
   - Construção e implantação de soluções baseadas em MCP
   - Tendências e roteiro futuro
   - **Guia de Servidores MCP Microsoft**: Guia abrangente para 10 servidores MCP Microsoft prontos para produção incluindo:
     - Microsoft Learn Docs MCP Server
     - Azure MCP Server (15+ conectores especializados)
     - GitHub MCP Server
     - Azure DevOps MCP Server
     - MarkItDown MCP Server
     - SQL Server MCP Server
     - Playwright MCP Server
     - Dev Box MCP Server
     - Azure AI Foundry MCP Server
     - Microsoft 365 Agents Toolkit MCP Server

9. **Melhores Práticas (08-BestPractices/)**
   - Ajuste de desempenho e otimização
   - Design de sistemas MCP tolerantes a falhas
   - Estratégias para testes e resiliência

10. **Estudos de Caso (09-CaseStudy/)**
    - **Sete estudos de caso abrangentes** demonstrando a versatilidade do MCP em vários cenários:
    - **Agentes de Viagem Azure AI**: orquestração multiagente com Azure OpenAI e AI Search
    - **Integração Azure DevOps**: automação de processos de fluxo de trabalho com atualizações de dados do YouTube
    - **Recuperação de Documentação em Tempo Real**: cliente console Python com streaming HTTP
    - **Gerador Interativo de Plano de Estudo**: aplicativo web Chainlit com IA conversacional
    - **Documentação In-Editor**: integração VS Code com fluxos do GitHub Copilot
    - **Gerenciamento de API Azure**: integração empresarial de API com criação de servidor MCP
    - **Registro MCP GitHub**: desenvolvimento de ecossistema e plataforma de integração agente
    - Exemplos de implementação abrangendo integração empresarial, produtividade de desenvolvedor e desenvolvimento de ecossistema

11. **Workshop Prático (10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/)**
    - Workshop prático e abrangente combinando MCP com AI Toolkit
    - Construção de aplicações inteligentes que conectam modelos de IA a ferramentas do mundo real
    - Módulos práticos cobrindo fundamentos, desenvolvimento de servidor personalizado e estratégias de implantação em produção
    - **Estrutura do Lab**:
      - Lab 1: Fundamentos do Servidor MCP
      - Lab 2: Desenvolvimento Avançado de Servidor MCP
      - Lab 3: Integração AI Toolkit
      - Lab 4: Implantação e Escalabilidade em Produção
    - Abordagem baseada em laboratório com instruções passo a passo

12. **Laboratórios de Integração de Banco de Dados MCP Server (11-MCPServerHandsOnLabs/)**
    - **Caminho de aprendizado com 13 laboratórios completos** para construir servidores MCP prontos para produção com integração PostgreSQL
    - **Implementação real de análise de varejo** usando o caso de uso Zava Retail
    - **Padrões corporativos** incluindo Row Level Security (RLS), busca semântica e acesso a dados multi-inquilino
    - **Estrutura Completa do Lab**:
      - **Labs 00-03: Fundamentos** - Introdução, Arquitetura, Segurança, Configuração do Ambiente
      - **Labs 04-06: Construção do Servidor MCP** - Design de Banco de Dados, Implementação do Servidor MCP, Desenvolvimento de Ferramentas
      - **Labs 07-09: Funcionalidades Avançadas** - Busca Semântica, Testes & Depuração, Integração VS Code
      - **Labs 10-12: Produção & Melhores Práticas** - Implantação, Monitoramento, Otimização
    - **Tecnologias Abrangidas**: framework FastMCP, PostgreSQL, Azure OpenAI, Azure Container Apps, Application Insights
    - **Resultados de Aprendizado**: servidores MCP prontos para produção, padrões de integração de banco de dados, análises baseadas em IA, segurança corporativa

## Recursos Adicionais

O repositório inclui recursos de apoio:

- **Pasta de imagens**: Contém diagramas e ilustrações usados ao longo do currículo
- **Traduções**: Suporte multilíngue com traduções automatizadas da documentação
- **Recursos Oficiais MCP**:
  - [Documentação MCP](https://modelcontextprotocol.io/)
  - [Especificação MCP](https://spec.modelcontextprotocol.io/)
  - [Repositório MCP no GitHub](https://github.com/modelcontextprotocol)

## Como Usar Este Repositório

1. **Aprendizagem Sequencial**: Siga os capítulos na ordem (00 até 11) para uma experiência estruturada de aprendizado.
2. **Foco em Linguagem Específica**: Se interessar-se por uma linguagem de programação particular, explore os diretórios de exemplos para implementações em sua linguagem preferida.
3. **Implementação Prática**: Comece pela seção "Introdução Prática" para configurar seu ambiente e criar seu primeiro servidor e cliente MCP.
4. **Exploração Avançada**: Depois de dominar o básico, mergulhe nos tópicos avançados para expandir seu conhecimento.
5. **Engajamento Comunitário**: Participe da comunidade MCP via discussões no GitHub e canais no Discord para conectar-se com especialistas e outros desenvolvedores.

## Clientes e Ferramentas MCP

O currículo cobre vários clientes e ferramentas MCP:

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

3. **Ferramentas de Gerenciamento MCP**:
   - MCP CLI
   - MCP Manager
   - MCP Linker
   - MCP Router

## Servidores MCP Populares

O repositório apresenta vários servidores MCP, incluindo:

1. **Servidores MCP Oficiais Microsoft**:
   - Microsoft Learn Docs MCP Server
   - Azure MCP Server (15+ conectores especializados)
   - GitHub MCP Server
   - Azure DevOps MCP Server
   - MarkItDown MCP Server
   - SQL Server MCP Server
   - Playwright MCP Server
   - Dev Box MCP Server
   - Azure AI Foundry MCP Server
   - Microsoft 365 Agents Toolkit MCP Server

2. **Servidores de Referência Oficiais**:
   - Filesystem
   - Fetch
   - Memory
   - Sequential Thinking

3. **Geração de Imagens**:
   - Azure OpenAI DALL-E 3
   - Stable Diffusion WebUI
   - Replicate

4. **Ferramentas de Desenvolvimento**:
   - Git MCP
   - Terminal Control
   - Code Assistant

5. **Servidores Especializados**:
   - Salesforce
   - Microsoft Teams
   - Jira & Confluence

## Contribuindo

Este repositório acolhe contribuições da comunidade. Consulte a seção Contribuições da Comunidade para orientações sobre como contribuir eficazmente para o ecossistema MCP.

----

*Este guia de estudo foi atualizado pela última vez em 5 de fevereiro de 2026, refletindo a Especificação MCP mais recente de 2025-11-25 e fornece uma visão geral do repositório até essa data. O conteúdo do repositório pode ser atualizado após essa data.*

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:  
Este documento foi traduzido usando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por qualquer mal-entendido ou interpretação errônea decorrente do uso desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->