# Tópicos Avançados em MCP

[![MCP Avançado: Agentes de IA Seguros, Escaláveis e Multi-modais](../../../translated_images/pt-PT/06.42259eaf91fccfc6.webp)](https://youtu.be/4yjmGvJzYdY)

_(Clique na imagem acima para ver o vídeo desta aula)_

Este capítulo abrange uma série de tópicos avançados na implementação do Protocolo de Contexto de Modelo (MCP), incluindo integração multimodal, escalabilidade, melhores práticas de segurança e integração empresarial. Estes tópicos são cruciais para construir aplicações MCP robustas e prontas para produção que possam satisfazer as exigências dos sistemas modernos de IA.

## Visão Geral

Esta lição explora conceitos avançados na implementação do Protocolo de Contexto de Modelo, com foco na integração multimodal, escalabilidade, melhores práticas de segurança e integração empresarial. Estes tópicos são essenciais para construir aplicações MCP de nível de produção que possam lidar com requisitos complexos em ambientes empresariais.

> **Nota da especificação atual:** MCP `2026-07-28` descontinua as primitivas Roots e
> Sampling cobertas nas lições 5.4 e 5.6. Também transfere o recurso experimental
> Tasks mencionado nas Funcionalidades do Protocolo (5.16) para uma
> extensão dedicada a Tasks. Essas lições são mantidas para implementações legadas
> `2025-11-25` e incluem orientações de migração. Veja
> [O que mudou no MCP: A especificação 2026-07-28](../01-CoreConcepts/mcp-2026-07-28.md).

## Objetivos de Aprendizagem

No final desta lição, será capaz de:

- Implementar capacidades multimodais dentro dos frameworks MCP
- Projetar arquiteturas MCP escaláveis para cenários de alta procura
- Aplicar melhores práticas de segurança alinhadas com os princípios de segurança do MCP
- Integrar MCP com sistemas e frameworks de IA empresariais
- Otimizar desempenho e fiabilidade em ambientes de produção

## Lições e Projetos de exemplo

| Link | Título | Descrição |
|------|-------|-------------|
| [5.1 Integração com Azure](./mcp-integration/README.md) | Integração com Azure | Aprenda como integrar o seu Servidor MCP na Azure |
| [5.2 Exemplo multimodal](./mcp-multi-modality/README.md) | Exemplos multimodais MCP | Exemplos para resposta áudio, imagem e multimodal |
| [5.3 Exemplo MCP OAuth2](../../../05-AdvancedTopics/mcp-oauth2-demo) | Demonstração MCP OAuth2 | Aplicação Spring Boot minimalista mostrando OAuth2 com MCP, tanto como Servidor de Autorização como de Recursos. Demonstra emissão segura de tokens, endpoints protegidos, deployment em Azure Container Apps e integração com API Management. |
| [5.4 Contextos Root](./mcp-root-contexts/README.md) | Contextos root | Aprenda a primitiva legacy `2025-11-25` Roots e opções atuais de migração (descontinuada em `2026-07-28`) |
| [5.5 Roteamento](./mcp-routing/README.md) | Roteamento | Aprenda diferentes tipos de roteamento |
| [5.6 Amostragem](./mcp-sampling/README.md) | Amostragem | Aprenda a primitiva legacy `2025-11-25` Sampling e opções atuais de migração (descontinuada em `2026-07-28`) |
| [5.7 Escala](./mcp-scaling/README.md) | Escala | Aprenda sobre escalabilidade |
| [5.8 Segurança](./mcp-security/README.md) | Segurança | Proteja o seu Servidor MCP |
| [5.9 Exemplo de Pesquisa Web](./web-search-mcp/README.md) | Pesquisa Web MCP | Servidor e cliente Python MCP integrando com SerpAPI para pesquisa em tempo real de web, notícias, produtos e Q&A. Demonstra orquestração multimodal, integração de API externa e tratamento robusto de erros. |
| [5.10 Streaming em Tempo Real](./mcp-realtimestreaming/README.md) | Streaming | O streaming de dados em tempo real tornou-se essencial no mundo orientado a dados de hoje, onde negócios e aplicações exigem acesso imediato à informação para tomadas de decisão oportunas. |
| [5.11 Pesquisa Web em Tempo Real](./mcp-realtimesearch/README.md) | Pesquisa Web | Pesquisa web em tempo real: como o MCP transforma a pesquisa web em tempo real fornecendo uma abordagem padronizada para gestão de contexto através de modelos de IA, motores de busca e aplicações. |
| [5.12 Autenticação Entra ID para Servidores MCP](./mcp-security-entra/README.md) | Autenticação Entra ID | Microsoft Entra ID fornece uma solução robusta baseada na cloud para gestão de identidade e acesso, ajudando a garantir que apenas utilizadores e aplicações autorizados possam interagir com o seu servidor MCP. |
| [5.13 Integração com Agente Microsoft Foundry](./mcp-foundry-agent-integration/README.md) | Integração Microsoft Foundry | Aprenda como integrar servidores MCP com agentes Microsoft Foundry, permitindo poderosa orquestração de ferramentas e capacidades de IA empresarial com ligações padronizadas a fontes externas de dados. |
| [5.14 Engenharia de Contexto](./mcp-contextengineering/README.md) | Engenharia de Contexto | A oportunidade futura das técnicas de engenharia de contexto para servidores MCP, incluindo otimização de contexto, gestão dinâmica de contexto e estratégias para engenharia eficiente de prompts dentro dos frameworks MCP. |
| [5.15 Transporte Customizado MCP](./mcp-transport/README.md) | Transporte Customizado | Aprenda a implementar mecanismos de transporte customizados para cenários especializados de comunicação MCP. |
| [5.16 Análise Profunda das Funcionalidades do Protocolo](./mcp-protocol-features/README.md) | Funcionalidades do Protocolo | Domine funcionalidades avançadas do protocolo incluindo notificações de progresso, cancelamento de pedidos, templates de recursos e padrões de tratamento de erros. |
| [5.17 Raciocínio Multi-Agente Adversarial](./mcp-adversarial-agents/README.md) | Agentes Adversariais | Use dois agentes com posições opostas, partilhando um único conjunto de ferramentas MCP, para detectar alucinações, destacar casos marginais e produzir outputs melhor calibrados através de debate estruturado. |

> **Nota histórica `2025-11-25`:** essa revisão introduziu Tasks experimentais
> e expandiu várias funcionalidades do protocolo. Em `2026-07-28`, Tasks passou para
> uma extensão oficial e Roots foram descontinuados. Não use o
> estado das funcionalidades `2025-11-25` como orientação atual; consulte o
> [registo de alterações 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/changelog).

## Referências Adicionais

Para as informações mais atualizadas sobre tópicos avançados MCP, consulte:
- [Documentação MCP](https://modelcontextprotocol.io/)
- [Especificação MCP (2026-07-28)](https://modelcontextprotocol.io/specification/2026-07-28/)
- [Repositório GitHub](https://github.com/modelcontextprotocol)
- [OWASP MCP Top 10](https://microsoft.github.io/mcp-azure-security-guide/mcp/) - Riscos e mitigação de segurança
- [Workshop MCP Security Summit (Sherpa)](https://azure-samples.github.io/sherpa/) - Treino prático de segurança

## Principais Conclusões

- Implementações MCP multimodais expandem capacidades de IA além do processamento de texto
- A escalabilidade é essencial para deploys empresariais e pode ser abordada através de escalamento horizontal e vertical
- Medidas de segurança abrangentes protegem dados e asseguram controlo de acesso adequado
- Integração empresarial com plataformas como Azure OpenAI e Microsoft AI Foundry melhora as capacidades MCP
- Implementações MCP avançadas beneficiam de arquiteturas otimizadas e gestão cuidadosa de recursos

## Exercício

Desenhe uma implementação MCP de nível empresarial para um caso de uso específico:

1. Identifique requisitos multimodais para o seu caso de uso
2. Descreva os controlos de segurança necessários para proteger dados sensíveis
3. Projete uma arquitetura escalável que possa lidar com cargas variáveis
4. Planeie pontos de integração com sistemas de IA empresariais
5. Documente possíveis gargalos de desempenho e estratégias de mitigação

## Recursos Adicionais

- [Documentação Azure OpenAI](https://learn.microsoft.com/en-us/azure/ai-services/openai/)
- [Documentação Microsoft AI Foundry](https://learn.microsoft.com/en-us/ai-services/)

---

## O que vem a seguir

Explore as lições deste módulo começando por: [5.1 Integração MCP](./mcp-integration/README.md)

Depois de completar este módulo, continue para: [Módulo 6: Contribuições da Comunidade](../06-CommunityContributions/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas resultantes da utilização desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->