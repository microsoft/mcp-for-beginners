# Tópicos Avançados em MCP

[![Advanced MCP: Secure, Scalable, and Multi-modal AI Agents](../../../translated_images/pt-BR/06.42259eaf91fccfc6.webp)](https://youtu.be/4yjmGvJzYdY)

_(Clique na imagem acima para assistir ao vídeo desta lição)_

Este capítulo aborda uma série de tópicos avançados na implementação do Protocolo de Contexto de Modelo (MCP), incluindo integração multimodal, escalabilidade, melhores práticas de segurança e integração empresarial. Esses tópicos são cruciais para construir aplicações MCP robustas e prontas para produção que possam atender às demandas dos sistemas modernos de IA.

## Visão geral

Esta lição explora conceitos avançados na implementação do Protocolo de Contexto de Modelo, focando em integração multimodal, escalabilidade, melhores práticas de segurança e integração empresarial. Esses tópicos são essenciais para construir aplicações MCP de nível de produção que possam lidar com requisitos complexos em ambientes corporativos.

## Objetivos de aprendizagem

Ao final desta lição, você será capaz de:

- Implementar capacidades multimodais dentro dos frameworks MCP
- Projetar arquiteturas MCP escaláveis para cenários de alta demanda
- Aplicar melhores práticas de segurança alinhadas aos princípios de segurança do MCP
- Integrar MCP com sistemas e frameworks de IA empresariais
- Otimizar desempenho e confiabilidade em ambientes de produção

## Lições e projetos de exemplo

| Link | Título | Descrição |
|------|--------|-----------|
| [5.1 Integration with Azure](./mcp-integration/README.md) | Integrar com Azure | Aprenda como integrar seu Servidor MCP no Azure |
| [5.2 Multi modal sample](./mcp-multi-modality/README.md) | Exemplos multimodais MCP | Exemplos para áudio, imagem e respostas multimodais |
| [5.3 MCP OAuth2 sample](../../../05-AdvancedTopics/mcp-oauth2-demo) | Demonstração OAuth2 MCP | Aplicativo Spring Boot minimalista mostrando OAuth2 com MCP, tanto como Servidor de Autorização quanto Recurso. Demonstra emissão segura de tokens, endpoints protegidos, implantação em Azure Container Apps e integração com API Management. |
| [5.4 Root Contexts](./mcp-root-contexts/README.md) | Contextos raiz | Saiba mais sobre contextos raiz e como implementá-los |
| [5.5 Routing](./mcp-routing/README.md) | Roteamento | Aprenda diferentes tipos de roteamento |
| [5.6 Sampling](./mcp-sampling/README.md) | Amostragem | Aprenda a trabalhar com amostragem |
| [5.7 Scaling](./mcp-scaling/README.md) | Escalabilidade | Aprenda sobre escalabilidade |
| [5.8 Security](./mcp-security/README.md) | Segurança | Proteja seu Servidor MCP |
| [5.9 Web Search sample](./web-search-mcp/README.md) | Pesquisa Web MCP | Servidor e cliente MCP em Python integrando com SerpAPI para pesquisa em tempo real na web, notícias, produtos e perguntas e respostas. Demonstra orquestração multi-ferramentas, integração com APIs externas e tratamento robusto de erros. |
| [5.10 Realtime Streaming](./mcp-realtimestreaming/README.md) | Streaming | Streaming de dados em tempo real tornou-se essencial no mundo orientado por dados atual, onde negócios e aplicativos requerem acesso imediato à informação para tomar decisões oportunas. |
| [5.11 Realtime Web Search](./mcp-realtimesearch/README.md) | Pesquisa Web | Pesquisa web em tempo real; como o MCP transforma a pesquisa web em tempo real fornecendo uma abordagem padronizada para o gerenciamento de contexto entre modelos de IA, mecanismos de busca e aplicações. |
| [5.12  Entra ID Authentication for Model Context Protocol Servers](./mcp-security-entra/README.md) | Autenticação Entra ID | O Microsoft Entra ID oferece uma solução robusta de gerenciamento de identidade e acesso baseada na nuvem, ajudando a garantir que apenas usuários e aplicativos autorizados possam interagir com seu servidor MCP. |
| [5.13 Azure AI Foundry Agent Integration](./mcp-foundry-agent-integration/README.md) | Integração Azure AI Foundry | Aprenda a integrar servidores do Protocolo de Contexto de Modelo com agentes Azure AI Foundry, possibilitando orquestração poderosa de ferramentas e capacidades de IA empresarial com conexões padronizadas a fontes externas de dados. |
| [5.14 Context Engineering](./mcp-contextengineering/README.md) | Engenharia de Contexto | A oportunidade futura das técnicas de engenharia de contexto para servidores MCP, incluindo otimização de contexto, gerenciamento dinâmico de contexto e estratégias para engenharia eficaz de prompts dentro dos frameworks MCP. |
| [5.15 MCP Custom Transport](./mcp-transport/README.md) | Transporte Personalizado | Aprenda a implementar mecanismos de transporte personalizados para cenários especializados de comunicação MCP. |
| [5.16 Protocol Features Deep Dive](./mcp-protocol-features/README.md) | Recursos do Protocolo | Domine recursos avançados do protocolo incluindo notificações de progresso, cancelamento de requisição, templates de recursos e padrões de tratamento de erros. |
| [5.17 Adversarial Multi-Agent Reasoning](./mcp-adversarial-agents/README.md) | Agentes Adversariais | Use dois agentes com posições opostas, compartilhando um único conjunto de ferramentas MCP, para capturar alucinações, expor casos extremos e produzir saídas melhor calibradas por meio de debates estruturados. |

> **Novidade na Especificação MCP 2025-11-25**: A especificação agora inclui suporte experimental para **Tarefas** (operações de longa duração com acompanhamento de progresso), **Anotações de Ferramentas** (metadados sobre comportamento da ferramenta para segurança), **Elicitação via modo URL** (solicitação de conteúdo URL específico dos clientes), e **Raízes aprimoradas** (para gerenciamento de contexto de espaço de trabalho). Veja o [changelog da Especificação MCP](https://spec.modelcontextprotocol.io/) para detalhes completos.

## Referências adicionais

Para informações mais atualizadas sobre tópicos avançados em MCP, consulte:
- [Documentação MCP](https://modelcontextprotocol.io/)
- [Especificação MCP (2025-11-25)](https://spec.modelcontextprotocol.io/specification/2025-11-25/)
- [Repositório GitHub](https://github.com/modelcontextprotocol)
- [OWASP MCP Top 10](https://microsoft.github.io/mcp-azure-security-guide/mcp/) - Riscos de segurança e mitigações
- [Workshop MCP Security Summit (Sherpa)](https://azure-samples.github.io/sherpa/) - Treinamento prático de segurança

## Principais aprendizados

- Implementações multimodais MCP ampliam as capacidades de IA além do processamento de texto
- Escalabilidade é essencial para implantações empresariais e pode ser tratada por escalonamento horizontal e vertical
- Medidas detalhadas de segurança protegem dados e garantem controle apropriado de acesso
- Integração empresarial com plataformas como Azure OpenAI e Microsoft AI Foundry amplia as capacidades MCP
- Implementações avançadas MCP se beneficiam de arquiteturas otimizadas e gestão cuidadosa de recursos

## Exercício

Projete uma implementação MCP de nível empresarial para um caso de uso específico:

1. Identifique requisitos multimodais para seu caso de uso
2. Esboce os controles de segurança necessários para proteger dados sensíveis
3. Projete uma arquitetura escalável capaz de lidar com cargas variáveis
4. Planeje pontos de integração com sistemas de IA empresariais
5. Documente possíveis gargalos de desempenho e estratégias de mitigação

## Recursos adicionais

- [Documentação Azure OpenAI](https://learn.microsoft.com/en-us/azure/ai-services/openai/)
- [Documentação Microsoft AI Foundry](https://learn.microsoft.com/en-us/ai-services/)

---

## O que vem a seguir

Explore as lições deste módulo começando por: [5.1 MCP Integration](./mcp-integration/README.md)

Após concluir este módulo, continue para: [Módulo 6: Contribuições da Comunidade](../06-CommunityContributions/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em sua língua nativa deve ser considerado a fonte autorizada. Para informações críticas, recomendamos tradução profissional feita por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->