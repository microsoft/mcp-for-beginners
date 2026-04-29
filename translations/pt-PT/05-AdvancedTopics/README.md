# Tópicos Avançados em MCP

[![Advanced MCP: Secure, Scalable, and Multi-modal AI Agents](../../../translated_images/pt-PT/06.42259eaf91fccfc6.webp)](https://youtu.be/4yjmGvJzYdY)

_(Clique na imagem acima para ver o vídeo desta lição)_

Este capítulo aborda uma série de tópicos avançados na implementação do Protocolo de Contexto de Modelo (MCP), incluindo integração multimodal, escalabilidade, melhores práticas de segurança e integração empresarial. Estes tópicos são cruciais para construir aplicações MCP robustas e preparadas para produção que possam atender às exigências dos sistemas modernos de IA.

## Visão Geral

Esta lição explora conceitos avançados na implementação do Protocolo de Contexto de Modelo, com foco em integração multimodal, escalabilidade, melhores práticas de segurança e integração empresarial. Estes tópicos são essenciais para construir aplicações MCP de nível de produção que possam lidar com requisitos complexos em ambientes empresariais.

## Objetivos de Aprendizagem

No final desta lição, você será capaz de:

- Implementar capacidades multimodais dentro dos frameworks MCP
- Projetar arquiteturas MCP escaláveis para cenários de alta demanda
- Aplicar melhores práticas de segurança alinhadas com os princípios de segurança do MCP
- Integrar MCP com sistemas e frameworks de IA empresariais
- Otimizar desempenho e confiabilidade em ambientes de produção

## Lições e Projetos de exemplo

| Link | Título | Descrição |
|------|-------|-------------|
| [5.1 Integration with Azure](./mcp-integration/README.md) | Integrar com Azure | Aprenda como integrar o seu Servidor MCP na Azure |
| [5.2 Multi modal sample](./mcp-multi-modality/README.md) | Exemplos Multimodais MCP  | Exemplos para áudio, imagem e respostas multimodais |
| [5.3 MCP OAuth2 sample](../../../05-AdvancedTopics/mcp-oauth2-demo) | Demonstração MCP OAuth2 | Aplicação mínima Spring Boot mostrando OAuth2 com MCP, tanto como Servidor de Autorização como Servidor de Recursos. Demonstra emissão segura de tokens, endpoints protegidos, deployment em Azure Container Apps e integração com API Management. |
| [5.4 Root Contexts](./mcp-root-contexts/README.md) | Contextos Raiz  | Saiba mais sobre contextos raiz e como implementá-los |
| [5.5 Routing](./mcp-routing/README.md) | Roteamento | Aprenda diferentes tipos de roteamento |
| [5.6 Sampling](./mcp-sampling/README.md) | Amostragem | Aprenda como trabalhar com amostragem |
| [5.7 Scaling](./mcp-scaling/README.md) | Escalabilidade  | Aprenda sobre escalabilidade |
| [5.8 Security](./mcp-security/README.md) | Segurança  | Proteja o seu Servidor MCP |
| [5.9 Web Search sample](./web-search-mcp/README.md) | Pesquisa Web MCP | Servidor MCP Python e cliente integrando com SerpAPI para pesquisa web, notícias, produtos e Q&A em tempo real. Demonstra orquestração multi-ferramentas, integração com APIs externas e manuseamento robusto de erros. |
| [5.10 Realtime Streaming](./mcp-realtimestreaming/README.md) | Streaming  | Streaming de dados em tempo real tornou-se essencial no mundo orientado por dados atual, onde negócios e aplicações requerem acesso imediato à informação para tomar decisões oportunas.|
| [5.11 Realtime Web Search](./mcp-realtimesearch/README.md) | Pesquisa Web | Pesquisa web em tempo real e como MCP transforma esta pesquisa fornecendo uma abordagem padronizada para gestão de contexto entre modelos de IA, motores de busca e aplicações.| 
| [5.12  Entra ID Authentication for Model Context Protocol Servers](./mcp-security-entra/README.md) | Autenticação Entra ID | O Microsoft Entra ID fornece uma solução robusta baseada na nuvem para gestão de identidades e acessos, ajudando a garantir que apenas utilizadores e aplicações autorizados possam interagir com o seu servidor MCP.|
| [5.13 Azure AI Foundry Agent Integration](./mcp-foundry-agent-integration/README.md) | Integração Azure AI Foundry | Aprenda a integrar servidores Protocolo de Contexto de Modelo com agentes Azure AI Foundry, permitindo orquestração poderosa de ferramentas e capacidades empresariais de IA com conexões padronizadas a fontes externas de dados.|
| [5.14 Context Engineering](./mcp-contextengineering/README.md) | Engenharia de Contexto | Oportunidade futura das técnicas de engenharia de contexto para servidores MCP, incluindo otimização de contexto, gestão dinâmica de contexto e estratégias para engenharia eficaz de prompts dentro dos frameworks MCP.|
| [5.15 MCP Custom Transport](./mcp-transport/README.md) | Transporte Personalizado | Aprenda a implementar mecanismos de transporte personalizados para cenários especializados de comunicação MCP.|
| [5.16 Protocol Features Deep Dive](./mcp-protocol-features/README.md) | Funcionalidades do Protocolo | Domine funcionalidades avançadas do protocolo incluindo notificações de progresso, cancelamento de pedidos, modelos de recursos e padrões de manuseamento de erros.|
| [5.17 Adversarial Multi-Agent Reasoning](./mcp-adversarial-agents/README.md) | Agentes Adversariais | Use dois agentes com posições opostas, partilhando um único conjunto de ferramentas MCP, para apurar alucinações, identificar casos-limite e gerar saídas melhor calibradas através de debate estruturado.|

> **Novo na Especificação MCP 2025-11-25**: A especificação agora inclui suporte experimental para **Tarefas** (operações de longa duração com rastreio de progresso), **Anotações de Ferramentas** (metadados sobre comportamento de ferramentas para segurança), **Elicitação de Modo URL** (pedido de conteúdo específico de URL a clientes) e **Raízes** aprimoradas (para gestão de contexto de espaço de trabalho). Veja o [changelog da Especificação MCP](https://spec.modelcontextprotocol.io/) para detalhes completos.

## Referências Adicionais

Para a informação mais atualizada sobre tópicos avançados MCP, consulte:
- [Documentação MCP](https://modelcontextprotocol.io/)
- [Especificação MCP (2025-11-25)](https://spec.modelcontextprotocol.io/specification/2025-11-25/)
- [Repositório GitHub](https://github.com/modelcontextprotocol)
- [OWASP MCP Top 10](https://microsoft.github.io/mcp-azure-security-guide/mcp/) - Riscos e mitigação de segurança
- [Workshop MCP Security Summit (Sherpa)](https://azure-samples.github.io/sherpa/) - Formação prática de segurança

## Pontos-Chave

- Implementações multimodais MCP ampliam capacidades de IA para além do processamento de texto
- Escalabilidade é essencial para deployments empresariais e pode ser abordada via escala horizontal e vertical
- Medidas abrangentes de segurança protegem dados e asseguram controle adequado de acesso
- Integração empresarial com plataformas como Azure OpenAI e Microsoft AI Foundry enriquece as capacidades MCP
- Implementações avançadas MCP beneficiam de arquiteturas otimizadas e gestão cuidadosa de recursos

## Exercício

Projete uma implementação MCP de nível empresarial para um caso de uso específico:

1. Identifique os requisitos multimodais para o seu caso de uso
2. Defina os controlos de segurança necessários para proteger dados sensíveis
3. Projete uma arquitetura escalável capaz de lidar com carga variável
4. Planeie pontos de integração com sistemas de IA empresariais
5. Documente possíveis gargalos de desempenho e estratégias de mitigação

## Recursos Adicionais

- [Documentação Azure OpenAI](https://learn.microsoft.com/en-us/azure/ai-services/openai/)
- [Documentação Microsoft AI Foundry](https://learn.microsoft.com/en-us/ai-services/)

---

## O que vem a seguir

Explore as lições deste módulo começando por: [5.1 MCP Integration](./mcp-integration/README.md)

Depois de completar este módulo, continue para: [Módulo 6: Contribuições da Comunidade](../06-CommunityContributions/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, por favor tenha em mente que traduções automáticas podem conter erros ou imprecisões. O documento original no seu idioma nativo deve ser considerado a fonte autoritativa. Para informações críticas, recomenda-se a tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes da utilização desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->