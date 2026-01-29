# Registro de Alterações: Currículo MCP para Iniciantes

Este documento serve como um registro de todas as mudanças significativas feitas no currículo Model Context Protocol (MCP) para Iniciantes. As mudanças são documentadas em ordem cronológica reversa (mudanças mais recentes primeiro).

## 18 de dezembro de 2025

### Atualização da Documentação de Segurança - Especificação MCP 2025-11-25

#### Melhores Práticas de Segurança MCP (02-Security/mcp-best-practices.md) - Atualização da Versão da Especificação
- **Atualização da Versão do Protocolo**: Atualizado para referenciar a última Especificação MCP 2025-11-25 (lançada em 25 de novembro de 2025)
  - Atualizadas todas as referências de versão da especificação de 2025-06-18 para 2025-11-25
  - Atualizadas referências de datas do documento de 18 de agosto de 2025 para 18 de dezembro de 2025
  - Verificado que todas as URLs da especificação apontam para a documentação atual
- **Validação de Conteúdo**: Validação abrangente das melhores práticas de segurança contra os padrões mais recentes
  - **Soluções de Segurança Microsoft**: Verificada a terminologia atual e links para Prompt Shields (anteriormente "detecção de risco de Jailbreak"), Azure Content Safety, Microsoft Entra ID e Azure Key Vault
  - **Segurança OAuth 2.1**: Confirmada a conformidade com as melhores práticas de segurança OAuth mais recentes
  - **Padrões OWASP**: Validadas as referências ao OWASP Top 10 para LLMs permanecem atuais
  - **Serviços Azure**: Verificados todos os links de documentação Microsoft Azure e melhores práticas
- **Alinhamento com Padrões**: Todos os padrões de segurança referenciados confirmados como atuais
  - NIST AI Risk Management Framework
  - ISO 27001:2022
  - Melhores Práticas de Segurança OAuth 2.1
  - Frameworks de segurança e conformidade Azure
- **Recursos de Implementação**: Validados todos os links e recursos de guias de implementação
  - Padrões de autenticação Azure API Management
  - Guias de integração Microsoft Entra ID
  - Gerenciamento de segredos Azure Key Vault
  - Pipelines DevSecOps e soluções de monitoramento

### Garantia de Qualidade da Documentação
- **Conformidade com a Especificação**: Garantido que todos os requisitos obrigatórios de segurança MCP (DEVE/ NÃO DEVE) estejam alinhados com a última especificação
- **Atualização de Recursos**: Verificados todos os links externos para documentação Microsoft, padrões de segurança e guias de implementação
- **Cobertura de Melhores Práticas**: Confirmada cobertura abrangente de autenticação, autorização, ameaças específicas de IA, segurança da cadeia de suprimentos e padrões empresariais

## 6 de outubro de 2025

### Expansão da Seção Introdução – Uso Avançado de Servidor & Autenticação Simples

#### Uso Avançado de Servidor (03-GettingStarted/10-advanced)
- **Novo Capítulo Adicionado**: Introduzido um guia abrangente para uso avançado de servidores MCP, cobrindo arquiteturas de servidor regulares e de baixo nível.
  - **Servidor Regular vs. Baixo Nível**: Comparação detalhada e exemplos de código em Python e TypeScript para ambas as abordagens.
  - **Design Baseado em Handlers**: Explicação do gerenciamento baseado em handlers para ferramentas/recursos/prompt para implementações de servidor escaláveis e flexíveis.
  - **Padrões Práticos**: Cenários do mundo real onde padrões de servidor de baixo nível são benéficos para recursos avançados e arquitetura.

#### Autenticação Simples (03-GettingStarted/11-simple-auth)
- **Novo Capítulo Adicionado**: Guia passo a passo para implementar autenticação simples em servidores MCP.
  - **Conceitos de Auth**: Explicação clara de autenticação vs. autorização e manipulação de credenciais.
  - **Implementação Básica de Auth**: Padrões de autenticação baseados em middleware em Python (Starlette) e TypeScript (Express), com exemplos de código.
  - **Progressão para Segurança Avançada**: Orientação para começar com autenticação simples e avançar para OAuth 2.1 e RBAC, com referências a módulos avançados de segurança.

Essas adições fornecem orientação prática e prática para construir implementações de servidores MCP mais robustas, seguras e flexíveis, conectando conceitos fundamentais com padrões avançados de produção.

## 29 de setembro de 2025

### Laboratórios de Integração de Banco de Dados do Servidor MCP - Caminho de Aprendizado Prático Abrangente

#### 11-MCPServerHandsOnLabs - Novo Currículo Completo de Integração de Banco de Dados
- **Caminho de Aprendizado Completo com 13 Laboratórios**: Adicionado currículo prático abrangente para construir servidores MCP prontos para produção com integração de banco de dados PostgreSQL
  - **Implementação do Mundo Real**: Caso de uso de análise Zava Retail demonstrando padrões de nível empresarial
  - **Progressão Estruturada de Aprendizado**:
    - **Laboratórios 00-03: Fundamentos** - Introdução, Arquitetura Central, Segurança & Multi-Tenancy, Configuração do Ambiente
    - **Laboratórios 04-06: Construindo o Servidor MCP** - Design & Esquema de Banco de Dados, Implementação do Servidor MCP, Desenvolvimento de Ferramentas  
    - **Laboratórios 07-09: Recursos Avançados** - Integração de Busca Semântica, Testes & Depuração, Integração VS Code
    - **Laboratórios 10-12: Produção & Melhores Práticas** - Estratégias de Implantação, Monitoramento & Observabilidade, Melhores Práticas & Otimização
  - **Tecnologias Empresariais**: Framework FastMCP, PostgreSQL com pgvector, embeddings Azure OpenAI, Azure Container Apps, Application Insights
  - **Recursos Avançados**: Segurança em Nível de Linha (RLS), busca semântica, acesso a dados multi-inquilino, embeddings vetoriais, monitoramento em tempo real

#### Padronização de Terminologia - Conversão de Módulo para Laboratório
- **Atualização Abrangente da Documentação**: Atualizados sistematicamente todos os arquivos README em 11-MCPServerHandsOnLabs para usar a terminologia "Laboratório" em vez de "Módulo"
  - **Cabeçalhos de Seção**: Atualizado "O que este módulo cobre" para "O que este laboratório cobre" em todos os 13 laboratórios
  - **Descrição de Conteúdo**: Alterado "Este módulo fornece..." para "Este laboratório fornece..." em toda a documentação
  - **Objetivos de Aprendizado**: Atualizado "Ao final deste módulo..." para "Ao final deste laboratório..."
  - **Links de Navegação**: Convertidas todas as referências "Módulo XX:" para "Laboratório XX:" em referências cruzadas e navegação
  - **Rastreamento de Conclusão**: Atualizado "Após concluir este módulo..." para "Após concluir este laboratório..."
  - **Referências Técnicas Preservadas**: Mantidas referências a módulos Python em arquivos de configuração (ex.: `"module": "mcp_server.main"`)

#### Aprimoramento do Guia de Estudo (study_guide.md)
- **Mapa Visual do Currículo**: Adicionada nova seção "11. Laboratórios de Integração de Banco de Dados" com visualização abrangente da estrutura dos laboratórios
- **Estrutura do Repositório**: Atualizado de dez para onze seções principais com descrição detalhada de 11-MCPServerHandsOnLabs
- **Orientação do Caminho de Aprendizado**: Melhoradas instruções de navegação para cobrir seções 00-11
- **Cobertura Tecnológica**: Adicionados detalhes de integração FastMCP, PostgreSQL, serviços Azure
- **Resultados de Aprendizado**: Enfatizado desenvolvimento de servidores prontos para produção, padrões de integração de banco de dados e segurança empresarial

#### Aprimoramento da Estrutura do README Principal
- **Terminologia Baseada em Laboratórios**: Atualizado README.md principal em 11-MCPServerHandsOnLabs para usar consistentemente a estrutura "Laboratório"
- **Organização do Caminho de Aprendizado**: Progressão clara desde conceitos fundamentais até implementação avançada e implantação em produção
- **Foco no Mundo Real**: Ênfase em aprendizado prático com padrões e tecnologias de nível empresarial

### Melhorias na Qualidade e Consistência da Documentação
- **Ênfase no Aprendizado Prático**: Reforçado o enfoque prático baseado em laboratórios em toda a documentação
- **Foco em Padrões Empresariais**: Destacadas implementações prontas para produção e considerações de segurança empresarial
- **Integração Tecnológica**: Cobertura abrangente dos serviços Azure modernos e padrões de integração de IA
- **Progressão de Aprendizado**: Caminho claro e estruturado desde conceitos básicos até implantação em produção

## 26 de setembro de 2025

### Aprimoramento de Estudos de Caso - Integração do Registro MCP do GitHub

#### Estudos de Caso (09-CaseStudy/) - Foco no Desenvolvimento do Ecossistema
- **README.md**: Expansão significativa com estudo de caso abrangente do Registro MCP do GitHub
  - **Estudo de Caso do Registro MCP do GitHub**: Novo estudo de caso abrangente examinando o lançamento do Registro MCP do GitHub em setembro de 2025
    - **Análise do Problema**: Exame detalhado dos desafios fragmentados de descoberta e implantação de servidores MCP
    - **Arquitetura da Solução**: Abordagem centralizada do registro do GitHub com instalação com um clique no VS Code
    - **Impacto nos Negócios**: Melhorias mensuráveis na integração e produtividade dos desenvolvedores
    - **Valor Estratégico**: Foco na implantação modular de agentes e interoperabilidade entre ferramentas
    - **Desenvolvimento do Ecossistema**: Posicionamento como plataforma fundamental para integração agentiva
  - **Estrutura Aprimorada dos Estudos de Caso**: Atualizados todos os sete estudos de caso com formatação consistente e descrições abrangentes
    - Azure AI Travel Agents: Ênfase em orquestração multiagente
    - Integração Azure DevOps: Foco em automação de fluxo de trabalho
    - Recuperação de Documentação em Tempo Real: Implementação de cliente de console Python
    - Gerador Interativo de Plano de Estudos: Aplicativo web conversacional Chainlit
    - Documentação no Editor: Integração VS Code e GitHub Copilot
    - Azure API Management: Padrões de integração de API empresarial
    - Registro MCP do GitHub: Desenvolvimento do ecossistema e plataforma comunitária
  - **Conclusão Abrangente**: Seção de conclusão reescrita destacando sete estudos de caso abrangendo múltiplas dimensões de implementação MCP
    - Integração Empresarial, Orquestração Multiagente, Produtividade do Desenvolvedor
    - Desenvolvimento do Ecossistema, Aplicações Educacionais categorizadas
    - Insights aprimorados sobre padrões arquiteturais, estratégias de implementação e melhores práticas
    - Ênfase no MCP como protocolo maduro e pronto para produção

#### Atualizações do Guia de Estudo (study_guide.md)
- **Mapa Visual do Currículo**: Atualizado mindmap para incluir Registro MCP do GitHub na seção Estudos de Caso
- **Descrição dos Estudos de Caso**: Aprimorada de descrições genéricas para detalhamento de sete estudos de caso abrangentes
- **Estrutura do Repositório**: Atualizada seção 10 para refletir cobertura abrangente dos estudos de caso com detalhes específicos de implementação
- **Integração do Registro de Alterações**: Adicionada entrada de 26 de setembro de 2025 documentando a adição do Registro MCP do GitHub e aprimoramentos dos estudos de caso
- **Atualizações de Data**: Atualizado timestamp do rodapé para refletir a revisão mais recente (26 de setembro de 2025)

### Melhorias na Qualidade da Documentação
- **Aprimoramento da Consistência**: Padronizada formatação e estrutura dos estudos de caso em todos os sete exemplos
- **Cobertura Abrangente**: Estudos de caso agora abrangem cenários empresariais, produtividade do desenvolvedor e desenvolvimento do ecossistema
- **Posicionamento Estratégico**: Foco aprimorado no MCP como plataforma fundamental para implantação de sistemas agentivos
- **Integração de Recursos**: Atualizados recursos adicionais para incluir link do Registro MCP do GitHub

## 15 de setembro de 2025

### Expansão de Tópicos Avançados - Transportes Customizados & Engenharia de Contexto

#### Transportes Customizados MCP (05-AdvancedTopics/mcp-transport/) - Novo Guia de Implementação Avançada
- **README.md**: Guia completo de implementação para mecanismos de transporte customizados MCP
  - **Transporte Azure Event Grid**: Implementação abrangente de transporte serverless orientado a eventos
    - Exemplos em C#, TypeScript e Python com integração Azure Functions
    - Padrões de arquitetura orientada a eventos para soluções MCP escaláveis
    - Receptores webhook e manipulação de mensagens push
  - **Transporte Azure Event Hubs**: Implementação de transporte de streaming de alta taxa
    - Capacidades de streaming em tempo real para cenários de baixa latência
    - Estratégias de particionamento e gerenciamento de checkpoints
    - Agrupamento de mensagens e otimização de desempenho
  - **Padrões de Integração Empresarial**: Exemplos arquiteturais prontos para produção
    - Processamento MCP distribuído em múltiplas Azure Functions
    - Arquiteturas híbridas de transporte combinando múltiplos tipos
    - Durabilidade, confiabilidade e estratégias de tratamento de erros de mensagens
  - **Segurança & Monitoramento**: Integração Azure Key Vault e padrões de observabilidade
    - Autenticação com identidade gerenciada e acesso de menor privilégio
    - Telemetria Application Insights e monitoramento de desempenho
    - Circuit breakers e padrões de tolerância a falhas
  - **Frameworks de Teste**: Estratégias abrangentes de teste para transportes customizados
    - Testes unitários com test doubles e frameworks de mocking
    - Testes de integração com Azure Test Containers
    - Considerações para testes de desempenho e carga

#### Engenharia de Contexto (05-AdvancedTopics/mcp-contextengineering/) - Disciplina Emergente de IA
- **README.md**: Exploração abrangente da engenharia de contexto como campo emergente
  - **Princípios Centrais**: Compartilhamento completo de contexto, consciência de decisão de ação e gerenciamento da janela de contexto
  - **Alinhamento com o Protocolo MCP**: Como o design MCP aborda desafios da engenharia de contexto
    - Limitações da janela de contexto e estratégias de carregamento progressivo
    - Determinação de relevância e recuperação dinâmica de contexto
    - Manipulação multimodal de contexto e considerações de segurança
  - **Abordagens de Implementação**: Arquiteturas single-threaded vs. multiagente
    - Técnicas de fragmentação e priorização de contexto
    - Carregamento progressivo e estratégias de compressão de contexto
    - Abordagens em camadas de contexto e otimização de recuperação
  - **Framework de Medição**: Métricas emergentes para avaliação da eficácia do contexto
    - Eficiência de entrada, desempenho, qualidade e considerações de experiência do usuário
    - Abordagens experimentais para otimização de contexto
    - Análise de falhas e metodologias de melhoria

#### Atualizações de Navegação do Currículo (README.md)
- **Estrutura de Módulo Aprimorada**: Atualizada tabela do currículo para incluir novos tópicos avançados
  - Adicionados Context Engineering (5.14) e Custom Transport (5.15)
  - Formatação consistente e links de navegação em todos os módulos
  - Descrições atualizadas para refletir o escopo atual do conteúdo

### Melhorias na Estrutura de Diretórios
- **Padronização de Nomes**: Renomeado "mcp transport" para "mcp-transport" para consistência com outras pastas de tópicos avançados
- **Organização de Conteúdo**: Todas as pastas 05-AdvancedTopics agora seguem padrão consistente de nomenclatura (mcp-[tópico])

### Aprimoramentos na Qualidade da Documentação
- **Alinhamento com Especificação MCP**: Todo o conteúdo novo referencia a Especificação MCP 2025-06-18 atual
- **Exemplos Multilíngues**: Exemplos de código abrangentes em C#, TypeScript e Python
- **Foco Empresarial**: Padrões prontos para produção e integração com nuvem Azure em todo o conteúdo
- **Documentação Visual**: Diagramas Mermaid para visualização de arquitetura e fluxos

## 18 de agosto de 2025

### Atualização Abrangente da Documentação - Padrões MCP 2025-06-18

#### Melhores Práticas de Segurança MCP (02-Security/) - Modernização Completa
- **MCP-SECURITY-BEST-PRACTICES-2025.md**: Reescrita completa alinhada com a Especificação MCP 2025-06-18
  - **Requisitos Obrigatórios**: Adicionados requisitos explícitos DEVE/ NÃO DEVE da especificação oficial com indicadores visuais claros
  - **12 Práticas Centrais de Segurança**: Reestruturado de lista de 15 itens para domínios abrangentes de segurança
    - Segurança de Token & Autenticação com integração de provedor de identidade externo
    - Gerenciamento de Sessão & Segurança de Transporte com requisitos criptográficos
    - Proteção Contra Ameaças Específicas de IA com integração Microsoft Prompt Shields
    - Controle de Acesso & Permissões com princípio do menor privilégio
    - Segurança & Monitoramento de Conteúdo com integração Azure Content Safety
    - Segurança da Cadeia de Suprimentos com verificação abrangente de componentes
    - Segurança OAuth & Prevenção de Confused Deputy com implementação PKCE
    - Resposta a Incidentes & Recuperação com capacidades automatizadas
    - Conformidade & Governança com alinhamento regulatório
    - Controles Avançados de Segurança com arquitetura de zero trust
    - Integração do Ecossistema de Segurança Microsoft com soluções abrangentes
    - Evolução Contínua de Segurança com práticas adaptativas
  - **Soluções de Segurança Microsoft**: Orientação aprimorada para integração de Prompt Shields, Azure Content Safety, Entra ID e GitHub Advanced Security
  - **Recursos de Implementação**: Links de recursos abrangentes categorizados por Documentação Oficial MCP, Soluções de Segurança Microsoft, Padrões de Segurança e Guias de Implementação

#### Controles Avançados de Segurança (02-Security/) - Implementação Empresarial
- **MCP-SECURITY-CONTROLS-2025.md**: Revisão completa com framework de segurança de nível empresarial
  - **9 Domínios Abrangentes de Segurança**: Expandido de controles básicos para framework detalhado empresarial
    - Autenticação & Autorização Avançadas com integração Microsoft Entra ID
    - Segurança de Token & Controles Anti-Passthrough com validação abrangente
    - Controles de Segurança de Sessão com prevenção de sequestro
    - Controles de Segurança Específicos para IA com prevenção de injeção de prompt e envenenamento de ferramentas
    - Prevenção de Ataque Confused Deputy com segurança de proxy OAuth
    - Segurança na Execução de Ferramentas com sandboxing e isolamento
    - Controles de Segurança da Cadeia de Suprimentos com verificação de dependências
    - Controles de Monitoramento & Detecção com integração SIEM
    - Resposta a Incidentes & Recuperação com capacidades automatizadas
  - **Exemplos de Implementação**: Adicionados blocos detalhados de configuração YAML e exemplos de código
  - **Integração de Soluções Microsoft**: Cobertura abrangente dos serviços de segurança Azure, GitHub Advanced Security e gerenciamento de identidade empresarial

#### Tópicos Avançados de Segurança (05-AdvancedTopics/mcp-security/) - Implementação Pronta para Produção
- **README.md**: Reescrita completa para implementação de segurança empresarial
  - **Alinhamento com Especificação Atual**: Atualizado para Especificação MCP 2025-06-18 com requisitos obrigatórios de segurança
  - **Autenticação Aprimorada**: Integração Microsoft Entra ID com exemplos abrangentes em .NET e Java Spring Security
  - **Integração de Segurança para IA**: Implementação Microsoft Prompt Shields e Azure Content Safety com exemplos detalhados em Python
  - **Mitigação Avançada de Ameaças**: Exemplos abrangentes de implementação para
    - Prevenção de Ataque Confused Deputy com PKCE e validação de consentimento do usuário
    - Prevenção de Passthrough de Token com validação de audiência e gerenciamento seguro de token
    - Prevenção de Sequestro de Sessão com vinculação criptográfica e análise comportamental
  - **Integração de Segurança Empresarial**: Monitoramento Azure Application Insights, pipelines de detecção de ameaças e segurança da cadeia de suprimentos
  - **Checklist de Implementação**: Controles de segurança obrigatórios vs. recomendados claros com benefícios do ecossistema de segurança Microsoft

### Qualidade da Documentação & Alinhamento de Padrões
- **Referências da Especificação**: Atualizadas todas as referências para a Especificação MCP 2025-06-18 atual
- **Ecossistema de Segurança Microsoft**: Orientação aprimorada para integração em toda a documentação de segurança
- **Implementação Prática**: Adicionados exemplos detalhados de código em .NET, Java e Python com padrões empresariais
- **Organização de Recursos**: Categorização abrangente da documentação oficial, padrões de segurança e guias de implementação
- **Indicadores Visuais**: Marcação clara de requisitos obrigatórios vs. práticas recomendadas


#### Conceitos Centrais (01-CoreConcepts/) - Modernização Completa
- **Atualização da Versão do Protocolo**: Atualizado para referenciar a Especificação MCP 2025-06-18 com versionamento baseado em data (formato AAAA-MM-DD)
- **Refinamento da Arquitetura**: Descrições aprimoradas de Hosts, Clientes e Servidores para refletir padrões atuais da arquitetura MCP
  - Hosts agora claramente definidos como aplicações de IA coordenando múltiplas conexões de clientes MCP
  - Clientes descritos como conectores de protocolo mantendo relações um-para-um com servidores
  - Servidores aprimorados com cenários de implantação local vs. remota
- **Reestruturação de Primitivas**: Revisão completa das primitivas de servidor e cliente
  - Primitivas de Servidor: Recursos (fontes de dados), Prompts (modelos), Ferramentas (funções executáveis) com explicações e exemplos detalhados
  - Primitivas de Cliente: Amostragem (completions LLM), Elicitação (entrada do usuário), Registro (debug/monitoramento)
  - Atualizado com padrões atuais de métodos de descoberta (`*/list`), recuperação (`*/get`) e execução (`*/call`)
- **Arquitetura do Protocolo**: Introduzido modelo de arquitetura em duas camadas
  - Camada de Dados: Fundação JSON-RPC 2.0 com gerenciamento de ciclo de vida e primitivas
  - Camada de Transporte: STDIO (local) e HTTP Streamable com SSE (transporte remoto)
- **Framework de Segurança**: Princípios abrangentes de segurança incluindo consentimento explícito do usuário, proteção de privacidade de dados, segurança na execução de ferramentas e segurança da camada de transporte
- **Padrões de Comunicação**: Atualizadas mensagens do protocolo para mostrar fluxos de inicialização, descoberta, execução e notificação
- **Exemplos de Código**: Atualizados exemplos multilíngues (.NET, Java, Python, JavaScript) para refletir padrões atuais do SDK MCP

#### Segurança (02-Security/) - Revisão Abrangente de Segurança  
- **Alinhamento com Padrões**: Alinhamento total com requisitos de segurança da Especificação MCP 2025-06-18
- **Evolução da Autenticação**: Documentada evolução de servidores OAuth customizados para delegação de provedor de identidade externo (Microsoft Entra ID)
- **Análise de Ameaças Específicas de IA**: Cobertura aprimorada de vetores modernos de ataque em IA
  - Cenários detalhados de ataque de injeção de prompt com exemplos do mundo real
  - Mecanismos de envenenamento de ferramentas e padrões de ataque "rug pull"
  - Envenenamento de janela de contexto e ataques de confusão de modelo
- **Soluções de Segurança Microsoft para IA**: Cobertura abrangente do ecossistema de segurança Microsoft
  - AI Prompt Shields com detecção avançada, spotlighting e técnicas de delimitador
  - Padrões de integração Azure Content Safety
  - GitHub Advanced Security para proteção da cadeia de suprimentos
- **Mitigação Avançada de Ameaças**: Controles de segurança detalhados para
  - Sequestro de sessão com cenários de ataque específicos MCP e requisitos criptográficos de ID de sessão
  - Problemas de confused deputy em cenários de proxy MCP com requisitos explícitos de consentimento
  - Vulnerabilidades de passthrough de token com controles obrigatórios de validação
- **Segurança da Cadeia de Suprimentos**: Cobertura expandida da cadeia de suprimentos de IA incluindo modelos base, serviços de embeddings, provedores de contexto e APIs de terceiros
- **Segurança da Fundação**: Integração aprimorada com padrões de segurança empresarial incluindo arquitetura zero trust e ecossistema de segurança Microsoft
- **Organização de Recursos**: Links abrangentes categorizados por tipo (Documentação Oficial, Padrões, Pesquisa, Soluções Microsoft, Guias de Implementação)

### Melhorias na Qualidade da Documentação
- **Objetivos de Aprendizagem Estruturados**: Objetivos de aprendizagem aprimorados com resultados específicos e acionáveis
- **Referências Cruzadas**: Adicionados links entre tópicos relacionados de segurança e conceitos centrais
- **Informações Atualizadas**: Atualizadas todas as referências de data e links de especificação para padrões atuais
- **Orientação de Implementação**: Adicionadas diretrizes específicas e acionáveis de implementação em ambas as seções

## 16 de julho de 2025

### Melhorias no README e Navegação
- Navegação do currículo completamente redesenhada no README.md
- Substituídas tags `<details>` por formato baseado em tabela mais acessível
- Criadas opções de layout alternativas na nova pasta "alternative_layouts"
- Adicionados exemplos de navegação em estilo cartão, abas e acordeão
- Atualizada seção de estrutura do repositório para incluir todos os arquivos mais recentes
- Aprimorada seção "Como Usar Este Currículo" com recomendações claras
- Atualizados links da especificação MCP para apontar para URLs corretos
- Adicionada seção de Engenharia de Contexto (5.14) à estrutura do currículo

### Atualizações do Guia de Estudo
- Guia de estudo completamente revisado para alinhar com a estrutura atual do repositório
- Adicionadas novas seções para Clientes MCP e Ferramentas, e Servidores MCP Populares
- Atualizado o Mapa Visual do Currículo para refletir com precisão todos os tópicos
- Aprimoradas descrições dos Tópicos Avançados para cobrir todas as áreas especializadas
- Atualizada seção de Estudos de Caso para refletir exemplos reais
- Adicionado este changelog abrangente

### Contribuições da Comunidade (06-CommunityContributions/)
- Adicionadas informações detalhadas sobre servidores MCP para geração de imagens
- Adicionada seção abrangente sobre uso do Claude no VSCode
- Adicionadas instruções de configuração e uso do cliente terminal Cline
- Atualizada seção de clientes MCP para incluir todas as opções populares
- Aprimorados exemplos de contribuição com amostras de código mais precisas

### Tópicos Avançados (05-AdvancedTopics/)
- Organizamos todas as pastas de tópicos especializados com nomenclatura consistente
- Adicionados materiais e exemplos de engenharia de contexto
- Adicionada documentação de integração do agente Foundry
- Aprimorada documentação de integração de segurança Entra ID

## 11 de junho de 2025

### Criação Inicial
- Lançada primeira versão do currículo MCP para Iniciantes
- Criada estrutura básica para todas as 10 seções principais
- Implementado Mapa Visual do Currículo para navegação
- Adicionados projetos de exemplo iniciais em múltiplas linguagens de programação

### Começando (03-GettingStarted/)
- Criados primeiros exemplos de implementação de servidor
- Adicionadas orientações para desenvolvimento de cliente
- Incluídas instruções de integração de cliente LLM
- Adicionada documentação de integração VS Code
- Implementados exemplos de servidor Server-Sent Events (SSE)

### Conceitos Centrais (01-CoreConcepts/)
- Adicionada explicação detalhada da arquitetura cliente-servidor
- Criada documentação sobre componentes chave do protocolo
- Documentados padrões de mensagens no MCP

## 23 de maio de 2025

### Estrutura do Repositório
- Inicializado repositório com estrutura básica de pastas
- Criados arquivos README para cada seção principal
- Configurada infraestrutura de tradução
- Adicionados ativos de imagem e diagramas

### Documentação
- Criado README.md inicial com visão geral do currículo
- Adicionados CODE_OF_CONDUCT.md e SECURITY.md
- Configurado SUPPORT.md com orientações para obter ajuda
- Criada estrutura preliminar do guia de estudo

## 15 de abril de 2025

### Planejamento e Framework
- Planejamento inicial para currículo MCP para Iniciantes
- Definidos objetivos de aprendizagem e público-alvo
- Estruturado currículo em 10 seções
- Desenvolvido framework conceitual para exemplos e estudos de caso
- Criados exemplos protótipos iniciais para conceitos chave

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional realizada por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->