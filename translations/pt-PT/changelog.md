# Changelog: Currículo MCP para Iniciantes

Este documento serve como um registo de todas as alterações significativas feitas ao currículo Model Context Protocol (MCP) para Iniciantes. As alterações são documentadas em ordem cronológica inversa (alterações mais recentes primeiro).

## 18 de dezembro de 2025

### Atualização da Documentação de Segurança - Especificação MCP 2025-11-25

#### Melhores Práticas de Segurança MCP (02-Security/mcp-best-practices.md) - Atualização da Versão da Especificação
- **Atualização da Versão do Protocolo**: Atualizado para referenciar a mais recente Especificação MCP 2025-11-25 (lançada a 25 de novembro de 2025)
  - Atualizadas todas as referências de versão da especificação de 2025-06-18 para 2025-11-25
  - Atualizadas as referências de datas do documento de 18 de agosto de 2025 para 18 de dezembro de 2025
  - Verificadas todas as URLs da especificação apontarem para a documentação atual
- **Validação de Conteúdo**: Validação abrangente das melhores práticas de segurança contra os padrões mais recentes
  - **Soluções de Segurança Microsoft**: Verificada a terminologia atual e os links para Prompt Shields (anteriormente "detecção de risco de Jailbreak"), Azure Content Safety, Microsoft Entra ID e Azure Key Vault
  - **Segurança OAuth 2.1**: Confirmada a conformidade com as melhores práticas de segurança OAuth mais recentes
  - **Padrões OWASP**: Validadas as referências OWASP Top 10 para LLMs permanecem atuais
  - **Serviços Azure**: Verificados todos os links da documentação Microsoft Azure e melhores práticas
- **Alinhamento com Padrões**: Todos os padrões de segurança referenciados confirmados como atuais
  - NIST AI Risk Management Framework
  - ISO 27001:2022
  - Melhores Práticas de Segurança OAuth 2.1
  - Frameworks de segurança e conformidade Azure
- **Recursos de Implementação**: Validados todos os links e recursos dos guias de implementação
  - Padrões de autenticação Azure API Management
  - Guias de integração Microsoft Entra ID
  - Gestão de segredos Azure Key Vault
  - Pipelines DevSecOps e soluções de monitorização

### Garantia de Qualidade da Documentação
- **Conformidade com a Especificação**: Garantido que todos os requisitos obrigatórios de segurança MCP (DEVE/ NÃO DEVE) estão alinhados com a especificação mais recente
- **Atualização dos Recursos**: Verificados todos os links externos para documentação Microsoft, padrões de segurança e guias de implementação
- **Cobertura das Melhores Práticas**: Confirmada cobertura abrangente de autenticação, autorização, ameaças específicas de IA, segurança da cadeia de fornecimento e padrões empresariais

## 6 de outubro de 2025

### Expansão da Secção Introdução – Utilização Avançada do Servidor & Autenticação Simples

#### Utilização Avançada do Servidor (03-GettingStarted/10-advanced)
- **Novo Capítulo Adicionado**: Introduzido um guia abrangente para utilização avançada do servidor MCP, cobrindo arquiteturas de servidor regulares e de baixo nível.
  - **Servidor Regular vs. Baixo Nível**: Comparação detalhada e exemplos de código em Python e TypeScript para ambas as abordagens.
  - **Design Baseado em Handlers**: Explicação da gestão de ferramentas/recursos/prompt baseada em handlers para implementações de servidor escaláveis e flexíveis.
  - **Padrões Práticos**: Cenários do mundo real onde padrões de servidor de baixo nível são benéficos para funcionalidades e arquiteturas avançadas.

#### Autenticação Simples (03-GettingStarted/11-simple-auth)
- **Novo Capítulo Adicionado**: Guia passo a passo para implementar autenticação simples em servidores MCP.
  - **Conceitos de Autenticação**: Explicação clara da diferença entre autenticação e autorização, e gestão de credenciais.
  - **Implementação de Autenticação Básica**: Padrões de autenticação baseados em middleware em Python (Starlette) e TypeScript (Express), com exemplos de código.
  - **Progressão para Segurança Avançada**: Orientação para começar com autenticação simples e avançar para OAuth 2.1 e RBAC, com referências a módulos de segurança avançada.

Estas adições fornecem orientação prática e aplicada para construir implementações de servidores MCP mais robustas, seguras e flexíveis, ligando conceitos fundamentais a padrões avançados de produção.

## 29 de setembro de 2025

### Laboratórios de Integração de Base de Dados do Servidor MCP - Percurso de Aprendizagem Prático Completo

#### 11-MCPServerHandsOnLabs - Novo Currículo Completo de Integração de Base de Dados
- **Percurso de Aprendizagem Completo com 13 Laboratórios**: Adicionado currículo prático abrangente para construir servidores MCP prontos para produção com integração de base de dados PostgreSQL
  - **Implementação do Mundo Real**: Caso de uso de análise Zava Retail demonstrando padrões de nível empresarial
  - **Progressão Estruturada de Aprendizagem**:
    - **Laboratórios 00-03: Fundamentos** - Introdução, Arquitetura Central, Segurança & Multi-Tenancy, Configuração do Ambiente
    - **Laboratórios 04-06: Construção do Servidor MCP** - Design & Esquema da Base de Dados, Implementação do Servidor MCP, Desenvolvimento de Ferramentas  
    - **Laboratórios 07-09: Funcionalidades Avançadas** - Integração de Pesquisa Semântica, Testes & Depuração, Integração VS Code
    - **Laboratórios 10-12: Produção & Melhores Práticas** - Estratégias de Deploy, Monitorização & Observabilidade, Melhores Práticas & Otimização
  - **Tecnologias Empresariais**: Framework FastMCP, PostgreSQL com pgvector, embeddings Azure OpenAI, Azure Container Apps, Application Insights
  - **Funcionalidades Avançadas**: Segurança a nível de linha (RLS), pesquisa semântica, acesso multi-inquilino a dados, embeddings vetoriais, monitorização em tempo real

#### Padronização de Terminologia - Conversão de Módulo para Laboratório
- **Atualização Abrangente da Documentação**: Atualizados sistematicamente todos os ficheiros README em 11-MCPServerHandsOnLabs para usar a terminologia "Laboratório" em vez de "Módulo"
  - **Cabeçalhos de Secção**: Atualizado "O que este módulo cobre" para "O que este laboratório cobre" em todos os 13 laboratórios
  - **Descrição do Conteúdo**: Alterado "Este módulo fornece..." para "Este laboratório fornece..." em toda a documentação
  - **Objetivos de Aprendizagem**: Atualizado "No final deste módulo..." para "No final deste laboratório..."
  - **Links de Navegação**: Convertidas todas as referências "Módulo XX:" para "Laboratório XX:" em referências cruzadas e navegação
  - **Rastreamento de Conclusão**: Atualizado "Após completar este módulo..." para "Após completar este laboratório..."
  - **Referências Técnicas Preservadas**: Mantidas referências a módulos Python em ficheiros de configuração (ex.: `"module": "mcp_server.main"`)

#### Melhoria do Guia de Estudo (study_guide.md)
- **Mapa Visual do Currículo**: Adicionada nova secção "11. Laboratórios de Integração de Base de Dados" com visualização abrangente da estrutura dos laboratórios
- **Estrutura do Repositório**: Atualizado de dez para onze secções principais com descrição detalhada de 11-MCPServerHandsOnLabs
- **Orientação do Percurso de Aprendizagem**: Melhoradas instruções de navegação para cobrir as secções 00-11
- **Cobertura Tecnológica**: Adicionados detalhes de integração FastMCP, PostgreSQL, serviços Azure
- **Resultados de Aprendizagem**: Enfatizado desenvolvimento de servidores prontos para produção, padrões de integração de base de dados e segurança empresarial

#### Melhoria da Estrutura do README Principal
- **Terminologia Baseada em Laboratórios**: Atualizado README.md principal em 11-MCPServerHandsOnLabs para usar consistentemente a estrutura "Laboratório"
- **Organização do Percurso de Aprendizagem**: Progressão clara desde conceitos fundamentais até implementação avançada e deploy em produção
- **Foco no Mundo Real**: Ênfase em aprendizagem prática com padrões e tecnologias de nível empresarial

### Melhorias na Qualidade e Consistência da Documentação
- **Ênfase na Aprendizagem Prática**: Reforçado o enfoque prático e baseado em laboratórios em toda a documentação
- **Foco em Padrões Empresariais**: Destacadas implementações prontas para produção e considerações de segurança empresarial
- **Integração Tecnológica**: Cobertura abrangente dos serviços Azure modernos e padrões de integração de IA
- **Progressão de Aprendizagem**: Percurso claro e estruturado desde conceitos básicos até deploy em produção

## 26 de setembro de 2025

### Melhoria dos Estudos de Caso - Integração do Registo MCP GitHub

#### Estudos de Caso (09-CaseStudy/) - Foco no Desenvolvimento do Ecossistema
- **README.md**: Expansão significativa com estudo de caso abrangente do Registo MCP GitHub
  - **Estudo de Caso do Registo MCP GitHub**: Novo estudo de caso completo que examina o lançamento do Registo MCP GitHub em setembro de 2025
    - **Análise do Problema**: Exame detalhado dos desafios fragmentados de descoberta e deploy de servidores MCP
    - **Arquitetura da Solução**: Abordagem centralizada do registo GitHub com instalação com um clique no VS Code
    - **Impacto Empresarial**: Melhorias mensuráveis na integração e produtividade dos desenvolvedores
    - **Valor Estratégico**: Foco no deploy modular de agentes e interoperabilidade entre ferramentas
    - **Desenvolvimento do Ecossistema**: Posicionamento como plataforma fundamental para integração agentiva
  - **Estrutura Melhorada dos Estudos de Caso**: Atualizados todos os sete estudos de caso com formatação consistente e descrições abrangentes
    - Agentes de Viagem Azure AI: Ênfase na orquestração multi-agente
    - Integração Azure DevOps: Foco na automação de workflows
    - Recuperação de Documentação em Tempo Real: Implementação de cliente de consola Python
    - Gerador Interativo de Planos de Estudo: Aplicação web conversacional Chainlit
    - Documentação In-Editor: Integração VS Code e GitHub Copilot
    - Azure API Management: Padrões de integração de API empresarial
    - Registo MCP GitHub: Desenvolvimento do ecossistema e plataforma comunitária
  - **Conclusão Abrangente**: Secção de conclusão reescrita destacando sete estudos de caso que abrangem múltiplas dimensões de implementação MCP
    - Integração Empresarial, Orquestração Multi-Agente, Produtividade do Desenvolvedor
    - Desenvolvimento do Ecossistema, Aplicações Educacionais categorizadas
    - Insights aprimorados sobre padrões arquitetónicos, estratégias de implementação e melhores práticas
    - Ênfase no MCP como protocolo maduro e pronto para produção

#### Atualizações do Guia de Estudo (study_guide.md)
- **Mapa Visual do Currículo**: Atualizado mindmap para incluir Registo MCP GitHub na secção Estudos de Caso
- **Descrição dos Estudos de Caso**: Melhorada de descrições genéricas para detalhamento dos sete estudos de caso abrangentes
- **Estrutura do Repositório**: Atualizada secção 10 para refletir cobertura abrangente dos estudos de caso com detalhes específicos de implementação
- **Integração do Changelog**: Adicionada entrada de 26 de setembro de 2025 documentando a adição do Registo MCP GitHub e melhorias nos estudos de caso
- **Atualização de Datas**: Atualizado timestamp do rodapé para refletir a revisão mais recente (26 de setembro de 2025)

### Melhorias na Qualidade da Documentação
- **Melhoria da Consistência**: Padronizada a formatação e estrutura dos estudos de caso em todos os sete exemplos
- **Cobertura Abrangente**: Estudos de caso agora abrangem cenários empresariais, produtividade do desenvolvedor e desenvolvimento do ecossistema
- **Posicionamento Estratégico**: Foco aprimorado no MCP como plataforma fundamental para deploy de sistemas agentivos
- **Integração de Recursos**: Atualizados recursos adicionais para incluir link do Registo MCP GitHub

## 15 de setembro de 2025

### Expansão de Tópicos Avançados - Transportes Customizados & Engenharia de Contexto

#### Transportes Customizados MCP (05-AdvancedTopics/mcp-transport/) - Novo Guia de Implementação Avançada
- **README.md**: Guia completo de implementação para mecanismos de transporte MCP customizados
  - **Transporte Azure Event Grid**: Implementação abrangente de transporte serverless orientado a eventos
    - Exemplos em C#, TypeScript e Python com integração Azure Functions
    - Padrões de arquitetura orientada a eventos para soluções MCP escaláveis
    - Receptores webhook e gestão de mensagens push
  - **Transporte Azure Event Hubs**: Implementação de transporte de streaming de alta taxa
    - Capacidades de streaming em tempo real para cenários de baixa latência
    - Estratégias de particionamento e gestão de checkpoints
    - Agrupamento de mensagens e otimização de desempenho
  - **Padrões de Integração Empresarial**: Exemplos arquitetónicos prontos para produção
    - Processamento MCP distribuído por múltiplas Azure Functions
    - Arquiteturas híbridas de transporte combinando múltiplos tipos
    - Durabilidade, fiabilidade e estratégias de tratamento de erros de mensagens
  - **Segurança & Monitorização**: Integração Azure Key Vault e padrões de observabilidade
    - Autenticação por identidade gerida e acesso com privilégio mínimo
    - Telemetria Application Insights e monitorização de desempenho
    - Circuit breakers e padrões de tolerância a falhas
  - **Frameworks de Testes**: Estratégias abrangentes de testes para transportes customizados
    - Testes unitários com test doubles e frameworks de mocking
    - Testes de integração com Azure Test Containers
    - Considerações para testes de desempenho e carga

#### Engenharia de Contexto (05-AdvancedTopics/mcp-contextengineering/) - Disciplina Emergente de IA
- **README.md**: Exploração abrangente da engenharia de contexto como campo emergente
  - **Princípios Centrais**: Partilha completa de contexto, consciência de decisão de ação e gestão da janela de contexto
  - **Alinhamento com o Protocolo MCP**: Como o design MCP aborda os desafios da engenharia de contexto
    - Limitações da janela de contexto e estratégias de carregamento progressivo
    - Determinação de relevância e recuperação dinâmica de contexto
    - Gestão multimodal de contexto e considerações de segurança
  - **Abordagens de Implementação**: Arquiteturas single-thread vs. multi-agente
    - Fragmentação e priorização de contexto
    - Carregamento progressivo e estratégias de compressão de contexto
    - Abordagens em camadas e otimização de recuperação
  - **Framework de Medição**: Métricas emergentes para avaliação da eficácia do contexto
    - Eficiência de entrada, desempenho, qualidade e considerações de experiência do utilizador
    - Abordagens experimentais para otimização de contexto
    - Análise de falhas e metodologias de melhoria

#### Atualizações de Navegação do Currículo (README.md)
- **Estrutura de Módulos Melhorada**: Atualizada tabela do currículo para incluir novos tópicos avançados
  - Adicionados Context Engineering (5.14) e Custom Transport (5.15)
  - Formatação consistente e links de navegação em todos os módulos
  - Descrições atualizadas para refletir o escopo atual do conteúdo

### Melhorias na Estrutura de Diretórios
- **Padronização de Nomes**: Renomeado "mcp transport" para "mcp-transport" para consistência com outras pastas de tópicos avançados
- **Organização de Conteúdo**: Todas as pastas 05-AdvancedTopics agora seguem padrão de nomeação consistente (mcp-[topic])

### Melhorias na Qualidade da Documentação
- **Alinhamento com Especificação MCP**: Todo o conteúdo novo referencia a Especificação MCP 2025-06-18 atual
- **Exemplos Multilíngues**: Exemplos de código abrangentes em C#, TypeScript e Python
- **Foco Empresarial**: Padrões prontos para produção e integração com cloud Azure em todo o conteúdo
- **Documentação Visual**: Diagramas Mermaid para visualização de arquitetura e fluxos

## 18 de agosto de 2025

### Atualização Abrangente da Documentação - Padrões MCP 2025-06-18

#### Melhores Práticas de Segurança MCP (02-Security/) - Modernização Completa
- **MCP-SECURITY-BEST-PRACTICES-2025.md**: Reescrita completa alinhada com a Especificação MCP 2025-06-18
  - **Requisitos Obrigatórios**: Adicionados requisitos explícitos DEVE/ NÃO DEVE da especificação oficial com indicadores visuais claros
  - **12 Práticas de Segurança Essenciais**: Reestruturado de lista de 15 itens para domínios de segurança abrangentes
    - Segurança de Token & Autenticação com integração de fornecedor de identidade externo
    - Gestão de Sessão & Segurança de Transporte com requisitos criptográficos
    - Proteção Contra Ameaças Específicas de IA com integração Microsoft Prompt Shields
    - Controlo de Acesso & Permissões com princípio do menor privilégio
    - Segurança & Monitorização de Conteúdo com integração Azure Content Safety
    - Segurança da Cadeia de Abastecimento com verificação abrangente de componentes
    - Segurança OAuth & Prevenção de Confused Deputy com implementação PKCE
    - Resposta a Incidentes & Recuperação com capacidades automatizadas
    - Conformidade & Governança com alinhamento regulatório
    - Controlo Avançado de Segurança com arquitetura de confiança zero
    - Integração do Ecossistema de Segurança Microsoft com soluções abrangentes
    - Evolução Contínua de Segurança com práticas adaptativas
  - **Soluções de Segurança Microsoft**: Orientação de integração melhorada para Prompt Shields, Azure Content Safety, Entra ID e GitHub Advanced Security
  - **Recursos de Implementação**: Links de recursos abrangentes categorizados por Documentação Oficial MCP, Soluções de Segurança Microsoft, Normas de Segurança e Guias de Implementação

#### Controlo Avançado de Segurança (02-Security/) - Implementação Empresarial
- **MCP-SECURITY-CONTROLS-2025.md**: Revisão completa com framework de segurança de nível empresarial
  - **9 Domínios Abrangentes de Segurança**: Expandido de controlos básicos para framework empresarial detalhado
    - Autenticação & Autorização Avançadas com integração Microsoft Entra ID
    - Segurança de Token & Controlos Anti-Passthrough com validação abrangente
    - Controlos de Segurança de Sessão com prevenção de sequestro
    - Controlos de Segurança Específicos de IA com prevenção de injeção de prompt e envenenamento de ferramentas
    - Prevenção de Ataques Confused Deputy com segurança de proxy OAuth
    - Segurança de Execução de Ferramentas com sandboxing e isolamento
    - Controlos de Segurança da Cadeia de Abastecimento com verificação de dependências
    - Controlos de Monitorização & Detecção com integração SIEM
    - Resposta a Incidentes & Recuperação com capacidades automatizadas
  - **Exemplos de Implementação**: Adicionados blocos de configuração YAML detalhados e exemplos de código
  - **Integração de Soluções Microsoft**: Cobertura abrangente dos serviços de segurança Azure, GitHub Advanced Security e gestão de identidade empresarial

#### Segurança de Tópicos Avançados (05-AdvancedTopics/mcp-security/) - Implementação Pronta para Produção
- **README.md**: Reescrita completa para implementação de segurança empresarial
  - **Alinhamento com Especificação Atual**: Atualizado para Especificação MCP 2025-06-18 com requisitos obrigatórios de segurança
  - **Autenticação Aprimorada**: Integração Microsoft Entra ID com exemplos abrangentes em .NET e Java Spring Security
  - **Integração de Segurança IA**: Implementação Microsoft Prompt Shields e Azure Content Safety com exemplos detalhados em Python
  - **Mitigação Avançada de Ameaças**: Exemplos abrangentes de implementação para
    - Prevenção de Ataques Confused Deputy com PKCE e validação de consentimento do utilizador
    - Prevenção de Passagem de Token com validação de audiência e gestão segura de tokens
    - Prevenção de Sequestro de Sessão com ligação criptográfica e análise comportamental
  - **Integração de Segurança Empresarial**: Monitorização Azure Application Insights, pipelines de deteção de ameaças e segurança da cadeia de abastecimento
  - **Lista de Verificação de Implementação**: Controlos de segurança obrigatórios vs. recomendados claros com benefícios do ecossistema de segurança Microsoft

### Qualidade da Documentação & Alinhamento de Normas
- **Referências da Especificação**: Atualizadas todas as referências para a Especificação MCP 2025-06-18 atual
- **Ecossistema de Segurança Microsoft**: Orientação de integração melhorada em toda a documentação de segurança
- **Implementação Prática**: Adicionados exemplos detalhados de código em .NET, Java e Python com padrões empresariais
- **Organização de Recursos**: Categorização abrangente da documentação oficial, normas de segurança e guias de implementação
- **Indicadores Visuais**: Marcação clara de requisitos obrigatórios vs. práticas recomendadas


#### Conceitos Fundamentais (01-CoreConcepts/) - Modernização Completa
- **Atualização da Versão do Protocolo**: Atualizado para referenciar a Especificação MCP 2025-06-18 com versionamento baseado em data (formato AAAA-MM-DD)
- **Refinamento da Arquitetura**: Descrições melhoradas de Hosts, Clientes e Servidores para refletir padrões atuais da arquitetura MCP
  - Hosts agora claramente definidos como aplicações IA que coordenam múltiplas conexões de clientes MCP
  - Clientes descritos como conectores de protocolo mantendo relações um-para-um com servidores
  - Servidores aprimorados com cenários de implantação local vs. remota
- **Reestruturação de Primitivas**: Revisão completa das primitivas de servidor e cliente
  - Primitivas de Servidor: Recursos (fontes de dados), Prompts (modelos), Ferramentas (funções executáveis) com explicações e exemplos detalhados
  - Primitivas de Cliente: Amostragem (completamentos LLM), Elicitação (entrada do utilizador), Registo (debugging/monitorização)
  - Atualizado com padrões atuais de métodos de descoberta (`*/list`), recuperação (`*/get`) e execução (`*/call`)
- **Arquitetura do Protocolo**: Introduzido modelo de arquitetura em duas camadas
  - Camada de Dados: Fundação JSON-RPC 2.0 com gestão de ciclo de vida e primitivas
  - Camada de Transporte: STDIO (local) e HTTP Streamable com SSE (transporte remoto)
- **Framework de Segurança**: Princípios de segurança abrangentes incluindo consentimento explícito do utilizador, proteção de privacidade de dados, segurança na execução de ferramentas e segurança da camada de transporte
- **Padrões de Comunicação**: Mensagens do protocolo atualizadas para mostrar fluxos de inicialização, descoberta, execução e notificação
- **Exemplos de Código**: Exemplos multi-linguagem atualizados (.NET, Java, Python, JavaScript) para refletir padrões atuais do SDK MCP

#### Segurança (02-Security/) - Revisão Abrangente de Segurança  
- **Alinhamento com Normas**: Alinhamento total com requisitos de segurança da Especificação MCP 2025-06-18
- **Evolução da Autenticação**: Documentada evolução de servidores OAuth personalizados para delegação de fornecedor de identidade externo (Microsoft Entra ID)
- **Análise de Ameaças Específicas de IA**: Cobertura melhorada de vetores de ataque modernos de IA
  - Cenários detalhados de ataques de injeção de prompt com exemplos do mundo real
  - Mecanismos de envenenamento de ferramentas e padrões de ataque "rug pull"
  - Envenenamento de janela de contexto e ataques de confusão de modelo
- **Soluções de Segurança IA Microsoft**: Cobertura abrangente do ecossistema de segurança Microsoft
  - AI Prompt Shields com deteção avançada, spotlighting e técnicas de delimitadores
  - Padrões de integração Azure Content Safety
  - GitHub Advanced Security para proteção da cadeia de abastecimento
- **Mitigação Avançada de Ameaças**: Controlos de segurança detalhados para
  - Sequestro de sessão com cenários de ataque específicos MCP e requisitos criptográficos de ID de sessão
  - Problemas de confused deputy em cenários de proxy MCP com requisitos explícitos de consentimento
  - Vulnerabilidades de passagem de token com controlos obrigatórios de validação
- **Segurança da Cadeia de Abastecimento**: Cobertura expandida da cadeia de abastecimento IA incluindo modelos base, serviços de embeddings, provedores de contexto e APIs de terceiros
- **Segurança de Fundação**: Integração aprimorada com padrões de segurança empresarial incluindo arquitetura de confiança zero e ecossistema de segurança Microsoft
- **Organização de Recursos**: Links de recursos abrangentes categorizados por tipo (Documentação Oficial, Normas, Investigação, Soluções Microsoft, Guias de Implementação)

### Melhorias na Qualidade da Documentação
- **Objetivos de Aprendizagem Estruturados**: Objetivos de aprendizagem aprimorados com resultados específicos e acionáveis
- **Referências Cruzadas**: Adicionados links entre tópicos relacionados de segurança e conceitos fundamentais
- **Informação Atualizada**: Atualizadas todas as referências de datas e links de especificação para normas atuais
- **Orientação de Implementação**: Adicionadas diretrizes específicas e acionáveis de implementação em ambas as secções

## 16 de julho de 2025

### Melhorias no README e Navegação
- Navegação do currículo completamente redesenhada no README.md
- Substituídas tags `<details>` por formato baseado em tabelas mais acessível
- Criadas opções de layout alternativas na nova pasta "alternative_layouts"
- Adicionados exemplos de navegação em estilo cartão, com separadores e acordeão
- Atualizada secção de estrutura do repositório para incluir todos os ficheiros mais recentes
- Melhorada secção "Como Usar Este Currículo" com recomendações claras
- Atualizados links da especificação MCP para apontar para URLs corretos
- Adicionada secção de Engenharia de Contexto (5.14) à estrutura do currículo

### Atualizações do Guia de Estudo
- Guia de estudo completamente revisto para alinhar com a estrutura atual do repositório
- Adicionadas novas secções para Clientes MCP e Ferramentas, e Servidores MCP Populares
- Atualizado o Mapa Visual do Currículo para refletir com precisão todos os tópicos
- Melhoradas descrições dos Tópicos Avançados para cobrir todas as áreas especializadas
- Atualizada secção de Estudos de Caso para refletir exemplos reais
- Adicionado este registo abrangente de alterações

### Contribuições da Comunidade (06-CommunityContributions/)
- Adicionadas informações detalhadas sobre servidores MCP para geração de imagens
- Adicionada secção abrangente sobre uso do Claude no VSCode
- Adicionadas instruções de configuração e uso do cliente terminal Cline
- Atualizada secção de clientes MCP para incluir todas as opções populares
- Melhorados exemplos de contribuição com amostras de código mais precisas

### Tópicos Avançados (05-AdvancedTopics/)
- Organizadas todas as pastas de tópicos especializados com nomenclatura consistente
- Adicionados materiais e exemplos de engenharia de contexto
- Adicionada documentação de integração do agente Foundry
- Melhorada documentação de integração de segurança Entra ID

## 11 de junho de 2025

### Criação Inicial
- Lançada primeira versão do currículo MCP para Iniciantes
- Criada estrutura básica para todas as 10 secções principais
- Implementado Mapa Visual do Currículo para navegação
- Adicionados projetos de exemplo iniciais em múltiplas linguagens de programação

### Começar (03-GettingStarted/)
- Criados primeiros exemplos de implementação de servidor
- Adicionadas orientações para desenvolvimento de clientes
- Incluídas instruções de integração de cliente LLM
- Adicionada documentação de integração VS Code
- Implementados exemplos de servidor Server-Sent Events (SSE)

### Conceitos Fundamentais (01-CoreConcepts/)
- Adicionada explicação detalhada da arquitetura cliente-servidor
- Criada documentação sobre componentes chave do protocolo
- Documentados padrões de mensagens no MCP

## 23 de maio de 2025

### Estrutura do Repositório
- Inicializado o repositório com estrutura básica de pastas
- Criados ficheiros README para cada secção principal
- Configurada infraestrutura de tradução
- Adicionados recursos gráficos e diagramas

### Documentação
- Criado README.md inicial com visão geral do currículo
- Adicionados CODE_OF_CONDUCT.md e SECURITY.md
- Configurado SUPPORT.md com orientações para obter ajuda
- Criada estrutura preliminar do guia de estudo

## 15 de abril de 2025

### Planeamento e Framework
- Planeamento inicial para currículo MCP para Iniciantes
- Definidos objetivos de aprendizagem e público-alvo
- Esboçada estrutura de 10 secções do currículo
- Desenvolvido framework conceptual para exemplos e estudos de caso
- Criados protótipos iniciais de exemplos para conceitos chave

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, por favor tenha em conta que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se a tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações erradas decorrentes do uso desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->