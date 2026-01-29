# Estudo de Caso: Azure AI Travel Agents – Implementação de Referência

## Visão Geral

[Azure AI Travel Agents](https://github.com/Azure-Samples/azure-ai-travel-agents) é uma solução de referência completa desenvolvida pela Microsoft que demonstra como construir uma aplicação de planeamento de viagens com múltiplos agentes e inteligência artificial, utilizando o Model Context Protocol (MCP), Azure OpenAI e Azure AI Search. Este projeto apresenta as melhores práticas para orquestrar vários agentes de IA, integrar dados empresariais e fornecer uma plataforma segura e extensível para cenários do mundo real.

## Funcionalidades Principais
- **Orquestração Multi-Agente:** Utiliza o MCP para coordenar agentes especializados (por exemplo, agentes de voos, hotéis e itinerários) que colaboram para realizar tarefas complexas de planeamento de viagens.
- **Integração de Dados Empresariais:** Liga-se ao Azure AI Search e outras fontes de dados empresariais para fornecer informações atualizadas e relevantes para recomendações de viagem.
- **Arquitetura Segura e Escalável:** Aproveita os serviços Azure para autenticação, autorização e implementação escalável, seguindo as melhores práticas de segurança empresarial.
- **Ferramentas Extensíveis:** Implementa ferramentas MCP reutilizáveis e modelos de prompts, permitindo uma rápida adaptação a novos domínios ou requisitos de negócio.
- **Experiência do Utilizador:** Oferece uma interface conversacional para os utilizadores interagirem com os agentes de viagem, suportada pelo Azure OpenAI e MCP.

## Arquitetura
![Architecture](https://raw.githubusercontent.com/Azure-Samples/azure-ai-travel-agents/main/docs/ai-travel-agents-architecture-diagram.png)

### Descrição do Diagrama de Arquitetura

A solução Azure AI Travel Agents foi concebida para modularidade, escalabilidade e integração segura de múltiplos agentes de IA e fontes de dados empresariais. Os principais componentes e o fluxo de dados são os seguintes:

- **Interface do Utilizador:** Os utilizadores interagem com o sistema através de uma interface conversacional (como um chat web ou bot no Teams), que envia as suas perguntas e recebe recomendações de viagem.
- **Servidor MCP:** Atua como o orquestrador central, recebendo as entradas do utilizador, gerindo o contexto e coordenando as ações dos agentes especializados (por exemplo, FlightAgent, HotelAgent, ItineraryAgent) através do Model Context Protocol.
- **Agentes de IA:** Cada agente é responsável por um domínio específico (voos, hotéis, itinerários) e é implementado como uma ferramenta MCP. Os agentes utilizam modelos de prompts e lógica para processar pedidos e gerar respostas.
- **Azure OpenAI Service:** Fornece capacidades avançadas de compreensão e geração de linguagem natural, permitindo que os agentes interpretem a intenção do utilizador e produzam respostas conversacionais.
- **Azure AI Search & Dados Empresariais:** Os agentes consultam o Azure AI Search e outras fontes de dados empresariais para obter informações atualizadas sobre voos, hotéis e opções de viagem.
- **Autenticação & Segurança:** Integra-se com o Microsoft Entra ID para autenticação segura e aplica controlos de acesso com privilégios mínimos a todos os recursos.
- **Implementação:** Projetado para ser implementado no Azure Container Apps, garantindo escalabilidade, monitorização e eficiência operacional.

Esta arquitetura permite uma orquestração fluida de múltiplos agentes de IA, integração segura com dados empresariais e uma plataforma robusta e extensível para construir soluções de IA específicas para domínios.

## Explicação Passo a Passo do Diagrama de Arquitetura
Imagine que está a planear uma grande viagem e tem uma equipa de assistentes especializados a ajudar em cada detalhe. O sistema Azure AI Travel Agents funciona de forma semelhante, usando diferentes componentes (como membros da equipa) que têm cada um uma função específica. Eis como tudo se encaixa:

### Interface do Utilizador (UI):
Pense nisto como a receção do seu agente de viagens. É aqui que você (o utilizador) faz perguntas ou pedidos, como “Encontra-me um voo para Paris.” Pode ser uma janela de chat num site ou numa aplicação de mensagens.

### Servidor MCP (O Coordenador):
O Servidor MCP é como o gestor que ouve o seu pedido na receção e decide qual especialista deve tratar de cada parte. Ele acompanha a conversa e garante que tudo corre sem problemas.

### Agentes de IA (Assistentes Especializados):
Cada agente é um especialista numa área específica — um conhece tudo sobre voos, outro sobre hotéis, e outro sobre planeamento de itinerários. Quando pede uma viagem, o Servidor MCP envia o seu pedido ao(s) agente(s) certo(s). Estes agentes usam o seu conhecimento e ferramentas para encontrar as melhores opções para si.

### Azure OpenAI Service (Especialista em Linguagem):
Isto é como ter um especialista em linguagem que entende exatamente o que está a pedir, independentemente da forma como o expressa. Ajuda os agentes a compreender os seus pedidos e a responder numa linguagem natural e conversacional.

### Azure AI Search & Dados Empresariais (Biblioteca de Informação):
Imagine uma enorme biblioteca atualizada com toda a informação mais recente sobre viagens — horários de voos, disponibilidade de hotéis e muito mais. Os agentes pesquisam nesta biblioteca para obter as respostas mais precisas para si.

### Autenticação & Segurança (Segurança):
Tal como um segurança que verifica quem pode entrar em certas áreas, esta parte garante que só pessoas e agentes autorizados têm acesso a informações sensíveis. Mantém os seus dados seguros e privados.

### Implementação no Azure Container Apps (O Edifício):
Todos estes assistentes e ferramentas trabalham juntos dentro de um edifício seguro e escalável (a cloud). Isto significa que o sistema pode lidar com muitos utilizadores ao mesmo tempo e está sempre disponível quando precisar.

## Como tudo funciona em conjunto:

Começa por fazer uma pergunta na receção (UI).  
O gestor (Servidor MCP) decide qual o especialista (agente) que deve ajudar.  
O especialista usa o especialista em linguagem (OpenAI) para entender o pedido e a biblioteca (AI Search) para encontrar a melhor resposta.  
O segurança (Autenticação) garante que tudo está seguro.  
Tudo isto acontece dentro de um edifício fiável e escalável (Azure Container Apps), para que a sua experiência seja fluida e segura.  
Este trabalho em equipa permite que o sistema o ajude a planear a sua viagem de forma rápida e segura, tal como uma equipa de agentes de viagens especializados a trabalhar em conjunto num escritório moderno!

## Implementação Técnica
- **Servidor MCP:** Hospeda a lógica central de orquestração, expõe as ferramentas dos agentes e gere o contexto para fluxos de trabalho de planeamento de viagens em múltiplas etapas.
- **Agentes:** Cada agente (por exemplo, FlightAgent, HotelAgent) é implementado como uma ferramenta MCP com os seus próprios modelos de prompts e lógica.
- **Integração Azure:** Utiliza Azure OpenAI para compreensão de linguagem natural e Azure AI Search para recuperação de dados.
- **Segurança:** Integra-se com Microsoft Entra ID para autenticação e aplica controlos de acesso com privilégios mínimos a todos os recursos.
- **Implementação:** Suporta implementação no Azure Container Apps para escalabilidade e eficiência operacional.

## Resultados e Impacto
- Demonstra como o MCP pode ser usado para orquestrar múltiplos agentes de IA num cenário real e de produção.
- Acelera o desenvolvimento de soluções ao fornecer padrões reutilizáveis para coordenação de agentes, integração de dados e implementação segura.
- Serve como modelo para construir aplicações específicas de domínio, potenciadas por IA, usando MCP e serviços Azure.

## Referências
- [Repositório GitHub Azure AI Travel Agents](https://github.com/Azure-Samples/azure-ai-travel-agents)
- [Azure OpenAI Service](https://azure.microsoft.com/en-us/products/ai-services/openai-service/)
- [Azure AI Search](https://azure.microsoft.com/en-us/products/ai-services/ai-search/)
- [Model Context Protocol (MCP)](https://modelcontextprotocol.io/)

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, por favor tenha em conta que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes da utilização desta tradução.