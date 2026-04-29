# Changelog: Currículo MCP para Iniciantes

Este documento serve como um registo de todas as alterações significativas feitas ao currículo do Model Context Protocol (MCP) para Iniciantes. As alterações são documentadas em ordem cronológica inversa (as mais recentes primeiro).

## 11 de abril de 2026

### Nova Aula, Correções de Documentação e Atualizações de Dependências

#### Novo Conteúdo do Currículo Adicionado

**Módulo 05 - Tópicos Avançados**
- **Aula 5.17: Raciocínio Multi-agente Adversarial com MCP** (`05-AdvancedTopics/mcp-adversarial-agents/README.md`): Novo guia abrangente sobre o padrão de debate adversarial para sistemas multi-agentes
  - Diagrama de arquitetura Mermaid: dois agentes → servidor MCP compartilhado → transcrição do debate → juiz → veredito
  - Servidor de ferramenta MCP compartilhado (`web_search` + `run_python`) implementado em Python e TypeScript
  - Prompts de sistema opostos (A FAVOR / CONTRA / Juiz) com requisitos explícitos de uso de ferramentas
  - Orquestrador do debate em Python, TypeScript e C# gerindo rondas e roteamento de argumentos
  - Integração MCP `ClientSession` para o orquestrador realizar chamadas reais às ferramentas
  - Tabela de casos de uso (detecção de alucinações, modelagem de ameaças, revisão de design de API, verificação factual, seleção tecnológica)
  - Considerações de segurança: execução em sandbox, validação de chamadas de ferramentas, limitação de taxa, registo de auditoria
  - Exercício estruturado com três cenários práticos (revisão de código, decisão de arquitetura, moderação de conteúdo)

#### Correções de Documentação

**Módulo 03 - Introdução**
- **05-stdio-server/README.md**: Corrigido exemplo incompleto do servidor stdio em TypeScript — adicionada instanciação de transporte em falta (`new StdioServerTransport()`) e chamada `server.connect(transport)` para coincidir com os exemplos em Python e .NET da mesma secção
- **14-sampling/README.md**: Corrigido erro tipográfico — corrigido `"Sampling is an davanced features"` para `"Sampling is an advanced feature"`

#### Atualizações do Currículo

**README.md principal**
- Adicionada entrada 5.17 (Raciocínio Multi-agente Adversarial com MCP) à tabela do currículo com link direto para a nova aula

**05-AdvancedTopics/README.md**
- Adicionada linha da Aula 5.17 à tabela das aulas

**study_guide.md**
- Adicionado tema Raciocínio Multi-agente Adversarial ao mapa mental e descrição em prosa de Tópicos Avançados

#### Correções de Código e Segurança

**Módulo 05 - Agentes Adversariais (`mcp-adversarial-agents`)**
- **Correção de segurança — injeção de comandos**: Substituída interpolação de shell `execSync` por `execFile` + `promisify` na ferramenta TypeScript `run_python`, eliminando a superfície de injeção de comandos (código controlado pelo LLM é agora passado como um elemento literal argv, sem envolver shell)
- **Integração do loop de ferramentas MCP**: Atualizado o orquestrador Python para usar cliente `AsyncAnthropic` (substituindo `Anthropic` síncrono bloqueante), passar uma `ClientSession` ativa diretamente a cada turno do agente, buscar definições de ferramentas via `session.list_tools()` a cada turno e despachar blocos `tool_use` via `session.call_tool()` em loop até o modelo emitir resposta final em texto

#### Atualizações de Dependências

- Atualizado `hono` para 4.12.12 em vários pacotes (03-GettingStarted, 04-PracticalImplementation, 10-StreamliningAIWorkflows)
- Atualizado `@hono/node-server` de 1.19.11 para 1.19.13 nos pacotes TypeScript
- Atualizado `cryptography` de 46.0.5 para 46.0.7 nos pacotes Python (laboratórios 3 e 4 do 10-StreamliningAIWorkflows)
- Atualizado `lodash` de 4.17.23 para 4.18.1 no inspetor 10-StreamliningAIWorkflows

#### Traduções

- Sincronizadas traduções para mais de 48 idiomas com as últimas alterações na fonte (atualização i18n)

---

## 5 de fevereiro de 2026

### Validação e Melhorias de Navegação em Todo o Repositório

#### Novo Conteúdo do Currículo Adicionado

**Módulo 03 - Introdução**
- **12-mcp-hosts/README.md**: Novo guia abrangente para configuração de hosts MCP
  - Exemplos de configuração para Claude Desktop, VS Code, Cursor, Cline, Windsurf
  - Modelos JSON de configuração para todos os hosts principais
  - Tabela comparativa dos tipos de transporte (stdio, SSE/HTTP, WebSocket)
  - Resolução de problemas comuns de conexão
  - Melhores práticas de segurança para configuração de hosts

- **13-mcp-inspector/README.md**: Novo guia de depuração para MCP Inspector
  - Métodos de instalação (npx, npm global, a partir do código-fonte)
  - Conexão a servidores via stdio e HTTP/SSE
  - Ferramentas para testes, recursos e workflows de prompts
  - Integração com VS Code e MCP Inspector
  - Cenários comuns de depuração com soluções

**Módulo 04 - Implementação Prática**
- **pagination/README.md**: Novo guia de implementação da paginação
  - Padrões de paginação com cursor em Python, TypeScript, Java
  - Manuseio de paginação do lado do cliente
  - Estratégias de design de cursor (opaco vs. estruturado)
  - Recomendações para otimização de desempenho

**Módulo 05 - Tópicos Avançados**
- **mcp-protocol-features/README.md**: Novos recursos do protocolo explorados em detalhe
  - Implementação de notificações de progresso
  - Padrões de cancelamento de pedidos
  - Modelos de recursos com padrões URI
  - Gestão do ciclo de vida do servidor
  - Controlo de níveis de log
  - Padrões de tratamento de erros com códigos JSON-RPC

#### Correções de Navegação (mais de 24 ficheiros atualizados)

**READMEs dos Módulos Principais**
 Agora com links tanto para a primeira aula quanto para o módulo seguinte

**Subfiches 02-Security**
- Todos os 5 documentos suplementares de segurança agora têm navegação "O que Segue":

**Ficheiros 09-CaseStudy**
- Todos os ficheiros de estudos de caso agora têm navegação sequencial:

**Laboratórios 10-StreamliningAI**
Adicionada secção O que Segue na visão geral do Módulo 10 e no Módulo 11

#### Correções de Código e Conteúdo

**Atualizações do SDK e das Dependências**
Corrigida versão aberta do openai para `^4.95.0`
Atualizado SDK de `^1.8.0` para `>=1.26.0`
Atualizadas referências à versão do mcp para `>=1.26.0`

**Correções de Código**
Corrigido modelo inválido `gpt-4o-mini` para `gpt-4.1-mini`

**Correções de Conteúdo**
Corrigido link quebrado `READMEmd` → `README.md`, corrigido cabeçalho do currículo `Module 1-3` → `Module 0-3`, corrigido caminho sensível a maiúsculas/minúsculas
Removido conteúdo duplicado corrompido do Estudo de Caso 5

**Melhorias para Iniciantes**
Adicionada introdução adequada, objetivos de aprendizagem e pré-requisitos para iniciantes

#### Atualizações do Currículo

**README.md principal**
- Adicionadas entradas 3.12 (Hosts MCP), 3.13 (Inspector MCP), 4.1 (Paginação), 5.16 (Recursos do Protocolo) à tabela do currículo

**READMEs dos Módulos**
Adicionadas aulas 12 e 13 à lista de aulas
Adicionada secção Guias Práticos com link para paginação
Adicionadas aulas 5.15 (Transporte Personalizado) e 5.16 (Recursos do Protocolo)

**study_guide.md**
- Atualizado mapa mental com todos os novos tópicos: Configuração de Hosts MCP, MCP Inspector, Estratégias de Paginação, Exploração de Recursos do Protocolo

## 28 de janeiro de 2026

### Revisão de Conformidade da Especificação MCP 2025-11-25

#### Aperfeiçoamento dos Conceitos Principais (01-CoreConcepts/)
- **Novo Primitivo Cliente - Roots**: Documentação abrangente adicionada para o primitivo cliente Roots, permitindo que servidores compreendam limites do sistema de ficheiros e permissões de acesso
- **Anotações de Ferramentas**: Documentação adicionada sobre anotações de comportamento de ferramentas (`readOnlyHint`, `destructiveHint`) para melhores decisões na execução das ferramentas
- **Chamada de Ferramentas no Sampling**: Atualizada documentação de Sampling para incluir parâmetros `tools` e `toolChoice` para invocação conduzida de ferramentas durante pedidos de sampling
- **Elicitação no Modo URL**: Documentação adicionada sobre elicitação baseada em URLs para interações externas iniciadas por servidores
- **Tarefas (Experimental)**: Nova secção documentando a funcionalidade experimental de Tarefas para wrappers de execução durável e obtenção diferida de resultados
- **Suporte a Ícones**: Notado que ferramentas, recursos, modelos de recursos e prompts podem agora incluir ícones como metadados adicionais

#### Atualizações de Documentação
- **README.md**: Adicionada referência à versão da Especificação MCP 2025-11-25 e explicação do versionamento baseado em datas
- **study_guide.md**: Atualizado mapa do currículo para incluir Tarefas e Anotações de Ferramentas na secção Conceitos Principais; atualizado carimbo temporal do documento

#### Verificação de Conformidade da Especificação
- **Versão do Protocolo**: Verificado que toda a documentação refere a versão corrente da Especificação MCP 2025-11-25
- **Alinhamento Arquitetural**: Confirmada a arquitetura em duas camadas (Camada de Dados + Camada de Transporte)
- **Documentação das Primitivas**: Validada documentação das primitivas de servidor (Recursos, Prompts, Ferramentas) e primitivas de cliente (Sampling, Elicitação, Registo, Roots)
- **Mecanismos de Transporte**: Verificada a precisão da documentação dos transportes STDIO e HTTP Streamable
- **Orientações de Segurança**: Confirmado alinhamento com as melhores práticas de segurança MCP atuais

#### Funcionalidades-Chave MCP 2025-11-25 Documentadas
- **Descoberta OpenID Connect**: Descoberta de servidores de autenticação via OIDC
- **Documentos de Metadados OAuth Client ID**: Mecanismo recomendado de registo de clientes
- **JSON Schema 2020-12**: Dialeto padrão para definições de esquema MCP
- **Sistema de Níveis do SDK**: Requisitos formalizados para suporte e manutenção de funcionalidades do SDK
- **Estrutura de Governação**: Grupos de trabalho e grupos de interesse formalizados na governação MCP

### Atualização Maior na Documentação de Segurança (02-Security/)

#### Integração do Workshop MCP Security Summit (Sherpa)
- **Novo Recurso de Treino Prático**: Adicionada integração abrangente com o [MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/) em toda a documentação de segurança
- **Cobertura da Rota da Expedição**: Documentado o progresso completo do acampamento base ao cume
- **Alinhamento OWASP**: Toda a orientação de segurança agora mapeia-se para riscos do OWASP MCP Azure Security Guide

#### Integração OWASP MCP Top 10
- **Nova Secção**: Adicionada tabela de Riscos de Segurança OWASP MCP Top 10 com mitigação Azure no README principal de Segurança
- **Documentação Baseada em Riscos**: Atualizado mcp-security-controls-2025.md com referências a riscos OWASP MCP para cada domínio de segurança
- **Arquitetura de Referência**: Ligação ao guia de segurança OWASP MCP Azure e aos padrões de implementação

#### Ficheiros de Segurança Atualizados
- **README.md**: Adicionada visão geral do Workshop Sherpa, tabela da rota da expedição, resumo dos riscos OWASP MCP Top 10 e secção de treino prático
- **mcp-security-controls-2025.md**: Atualizado cabeçalho para fevereiro de 2026, adicionadas referências a riscos OWASP (MCP01-MCP08), corrigida inconsistência da versão da especificação
- **mcp-security-best-practices-2025.md**: Adicionada secção de recursos Sherpa e OWASP, atualizado carimbo temporal
- **mcp-best-practices.md**: Adicionada secção de treino prático com ligações a Sherpa e OWASP
- **azure-content-safety-implementation.md**: Adicionada referência OWASP MCP06, alinhamento Sherpa Acampamento 3 e secção de recursos adicionais

#### Novos Links de Recursos Adicionados
- [MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/)
- [OWASP MCP Azure Security Guide](https://microsoft.github.io/mcp-azure-security-guide/)
- [OWASP MCP Top 10](https://owasp.org/www-project-mcp-top-10/)
- Páginas individuais dos riscos OWASP MCP (MCP01-MCP10)

### Alinhamento em Todo o Currículo com a Especificação MCP 2025-11-25

#### Módulo 03 - Introdução
- **Documentação do SDK**: Adicionado Go SDK à lista oficial de SDKs; atualizadas todas referências ao SDK para alinhamento com a Especificação MCP 2025-11-25
- **Clarificação de Transporte**: Atualizadas descrições dos transportes STDIO e HTTP Streaming com referências explícitas à especificação

#### Módulo 04 - Implementação Prática
- **Atualizações do SDK**: Adicionado Go SDK; lista do SDK atualizada com referência à versão da especificação
- **Especificação de Autorização**: Link da especificação MCP Authorization atualizado para a versão atual 2025-11-25

#### Módulo 05 - Tópicos Avançados
- **Novos Recursos**: Adicionada nota sobre novas funcionalidades da Especificação MCP 2025-11-25 (Tarefas, Anotações de Ferramentas, Elicitação no Modo URL, Roots)
- **Recursos de Segurança**: Adicionadas ligações ao OWASP MCP Top 10 e ao workshop Sherpa nos recursos adicionais

#### Módulo 06 - Contribuições da Comunidade
- **Lista de SDKs**: Adicionados SDKs Swift e Rust; link da especificação atualizado para 2025-11-25
- **Referência da Especificação**: Atualizado link para a URL direta da Especificação MCP

#### Módulo 07 - Lições da Adoção Precoce
- **Atualizações de Recursos**: Adicionada ligação à Especificação MCP 2025-11-25 e OWASP MCP Top 10 entre os recursos adicionais

#### Módulo 08 - Melhores Práticas
- **Versão da Especificação**: Referência da Especificação MCP atualizada para 2025-11-25
- **Recursos de Segurança**: Adicionados OWASP MCP Top 10 e workshop Sherpa aos recursos adicionais

#### Módulo 10 - Otimização de Workflows de IA
- **Atualização do Emblema**: Alterado o emblema da versão MCP de versão SDK (1.9.3) para versão da especificação (2025-11-25)
- **Links de Recursos**: Atualizado link da Especificação MCP; adicionado OWASP MCP Top 10

#### Módulo 11 - Laboratórios Práticos MCP Server
- **Referência da Especificação**: Atualizado link para versão 2025-11-25 da Especificação MCP
- **Recursos de Segurança**: Adicionado OWASP MCP Top 10 como recurso oficial

## 18 de dezembro de 2025
### Atualização da Documentação de Segurança - Especificação MCP 2025-11-25

#### Melhores Práticas de Segurança MCP (02-Security/mcp-best-practices.md) - Atualização da Versão da Especificação
- **Atualização da Versão do Protocolo**: Atualizado para referenciar a mais recente Especificação MCP 2025-11-25 (lançada a 25 de novembro de 2025)
  - Atualizadas todas as referências de versão da especificação de 2025-06-18 para 2025-11-25
  - Atualizadas as referências de data do documento de 18 de agosto de 2025 para 18 de dezembro de 2025
  - Verificadas todas as URLs da especificação apontam para a documentação atual
- **Validação de Conteúdo**: Validação abrangente das melhores práticas de segurança contra os padrões mais recentes
  - **Soluções de Segurança Microsoft**: Verificada a terminologia atual e os links para Prompt Shields (anteriormente “detecção de risco de Jailbreak”), Azure Content Safety, Microsoft Entra ID e Azure Key Vault
  - **Segurança OAuth 2.1**: Confirmada conformidade com as melhores práticas de segurança OAuth mais recentes
  - **Padrões OWASP**: Validada a atualidade das referências ao OWASP Top 10 para LLMs
  - **Serviços Azure**: Verificados todos os links da documentação Microsoft Azure e melhores práticas
- **Alinhamento com Padrões**: Todos os padrões de segurança referenciados confirmados como atuais
  - NIST AI Risk Management Framework
  - ISO 27001:2022
  - Melhores Práticas de Segurança OAuth 2.1
  - Molduras de segurança e conformidade Azure
- **Recursos de Implementação**: Validado todos os links e recursos de guias de implementação
  - Padrões de autenticação Azure API Management
  - Guias de integração Microsoft Entra ID
  - Gestão de segredos Azure Key Vault
  - Pipelines DevSecOps e soluções de monitorização

### Garantia de Qualidade da Documentação
- **Conformidade com a Especificação**: Assegurado que todos os requisitos obrigatórios de segurança MCP (MUST/MUST NOT) estão alinhados com a última especificação
- **Atualização de Recursos**: Verificados todos os links externos para documentação Microsoft, padrões de segurança e guias de implementação
- **Cobertura das Melhores Práticas**: Confirmada cobertura abrangente de autenticação, autorização, ameaças específicas de IA, segurança da cadeia de fornecimento e padrões empresariais

## 6 de Outubro de 2025

### Expansão da Secção Introdução – Utilização Avançada de Servidor & Autenticação Simples

#### Utilização Avançada de Servidor (03-GettingStarted/10-advanced)
- **Novo Capítulo Adicionado**: Introduzido um guia completo para uso avançado de servidores MCP, cobrindo arquiteturas de servidor regulares e de baixo nível.
  - **Servidor Regular vs. de Baixo Nível**: Comparação detalhada e exemplos de código em Python e TypeScript para ambas as abordagens.
  - **Design Baseado em Handlers**: Explicação da gestão baseada em handlers para ferramentas/recursos/prompts para implementações de servidor escaláveis e flexíveis.
  - **Padrões Práticos**: Cenários reais onde padrões de servidor de baixo nível são benéficos para funcionalidades e arquiteturas avançadas.

#### Autenticação Simples (03-GettingStarted/11-simple-auth)
- **Novo Capítulo Adicionado**: Guia passo a passo para implementar autenticação simples em servidores MCP.
  - **Conceitos de Autenticação**: Explicação clara entre autenticação e autorização, e gestão de credenciais.
  - **Implementação de Autenticação Básica**: Padrões de autenticação baseados em middleware em Python (Starlette) e TypeScript (Express), com exemplos de código.
  - **Progressão para Segurança Avançada**: Orientações para começar com autenticação simples e avançar para OAuth 2.1 e RBAC, com referências a módulos de segurança avançada.

Estas adições fornecem orientações práticas e hands-on para construir implementações de servidor MCP mais robustas, seguras e flexíveis, fazendo a ponte entre conceitos fundamentais e padrões avançados de produção.

## 29 de Setembro de 2025

### Laboratórios de Integração de Base de Dados em Servidor MCP - Percurso de Aprendizagem Prático e Completo

#### 11-MCPServerHandsOnLabs - Novo Currículo Completo de Integração de Base de Dados
- **Percurso de Aprendizagem Completo com 13 Laboratórios**: Adicionado currículo prático para construir servidores MCP preparados para produção com integração da base de dados PostgreSQL
  - **Implementação Realista**: Caso de uso de análise Zava Retail demonstrando padrões de nível empresarial
  - **Progressão de Aprendizagem Estruturada**:
    - **Laboratórios 00-03: Fundamentos** - Introdução, Arquitetura Central, Segurança & Multi-Tenant, Configuração do Ambiente
    - **Laboratórios 04-06: Construção do Servidor MCP** - Design & Esquema da Base de Dados, Implementação do Servidor MCP, Desenvolvimento de Ferramentas  
    - **Laboratórios 07-09: Funcionalidades Avançadas** - Integração de Pesquisa Semântica, Testes & Debugging, Integração VS Code
    - **Laboratórios 10-12: Produção & Melhores Práticas** - Estratégias de Deployment, Monitorização & Observabilidade, Melhores Práticas & Otimização
  - **Tecnologias Empresariais**: Framework FastMCP, PostgreSQL com pgvector, embeddings Azure OpenAI, Azure Container Apps, Application Insights
  - **Funcionalidades Avançadas**: Segurança ao Nível de Linha (RLS), pesquisa semântica, acesso multi-tenant a dados, embeddings vetoriais, monitorização em tempo real

#### Padronização de Terminologia - Conversão de Módulo para Laboratório
- **Atualização Completa da Documentação**: Atualizados sistematicamente todos os ficheiros README em 11-MCPServerHandsOnLabs para utilizar a terminologia "Laboratório" em vez de "Módulo"
  - **Cabeçalhos de Secção**: Atualizado "O que este módulo cobre" para "O que este laboratório cobre" em todos os 13 laboratórios
  - **Descrição de Conteúdo**: Alterado "Este módulo fornece..." para "Este laboratório fornece..." na documentação
  - **Objetivos de Aprendizagem**: Atualizado "No final deste módulo..." para "No final deste laboratório..."
  - **Links de Navegação**: Convertidas todas as referências "Módulo XX:" para "Laboratório XX:" em referências cruzadas e navegação
  - **Rastreamento de Conclusão**: Atualizado "Após concluir este módulo..." para "Após concluir este laboratório..."
  - **Referências Técnicas Preservadas**: Mantidas referências a módulos Python em ficheiros de configuração (ex.: `"module": "mcp_server.main"`)

#### Aperfeiçoamento do Guia de Estudo (study_guide.md)
- **Mapa Visual do Currículo**: Adicionada nova secção "11. Laboratórios de Integração de Base de Dados" com visualização abrangente da estrutura dos laboratórios
- **Estrutura do Repositório**: Atualizado de dez para onze secções principais com descrição detalhada de 11-MCPServerHandsOnLabs
- **Orientações do Percurso de Aprendizagem**: Melhoradas as instruções de navegação para abranger as secções 00-11
- **Cobertura Tecnológica**: Incluídos detalhes sobre FastMCP, PostgreSQL, integração de serviços Azure
- **Resultados da Aprendizagem**: Enfatizado desenvolvimento de servidores prontos para produção, padrões de integração de base de dados e segurança empresarial

#### Melhoria da Estrutura do README Principal
- **Terminologia Baseada em Laboratórios**: Atualizado README.md principal em 11-MCPServerHandsOnLabs para usar consistentemente a estrutura "Laboratório"
- **Organização do Percurso de Aprendizagem**: Progressão clara de conceitos fundamentais a implementação avançada e deployment em produção
- **Foco no Mundo Real**: Ênfase em aprendizagem prática com padrões e tecnologias de nível empresarial

### Melhorias na Qualidade & Consistência da Documentação
- **Ênfase em Aprendizagem Prática**: Reforçada abordagem prática baseada em laboratórios em toda a documentação
- **Foco em Padrões Empresariais**: Destacadas implementações prontas para produção e considerações de segurança empresarial
- **Integração Tecnológica**: Cobertura abrangente dos serviços Azure modernos e padrões de integração de IA
- **Progressão de Aprendizagem**: Percurso claro e estruturado desde conceitos básicos até deployment em produção

## 26 de Setembro de 2025

### Melhoria de Estudos de Caso - Integração do Registo MCP do GitHub

#### Estudos de Caso (09-CaseStudy/) - Foco no Desenvolvimento do Ecossistema
- **README.md**: Ampliação significativa com estudo de caso abrangente do Registo MCP GitHub
  - **Estudo de Caso Registo MCP GitHub**: Novo estudo de caso detalhado sobre o lançamento do Registo MCP do GitHub em Setembro de 2025
    - **Análise do Problema**: Exame detalhado da fragmentação na descoberta e deployment de servidores MCP
    - **Arquitetura da Solução**: Abordagem centralizada do registo do GitHub com instalação em um clique no VS Code
    - **Impacto nos Negócios**: Melhorias mensuráveis no onboarding e produtividade dos desenvolvedores
    - **Valor Estratégico**: Foco em deployment modular de agentes e interoperabilidade entre ferramentas
    - **Desenvolvimento do Ecossistema**: Posicionamento como plataforma fundamental para integração agentic
  - **Estrutura Aprimorada do Estudo de Caso**: Atualizados os sete estudos de caso com formatação consistente e descrições abrangentes
    - Azure AI Travel Agents: Ênfase em orquestração multi-agente
    - Integração Azure DevOps: Foco em automação de workflows
    - Recuperação de Documentação em Tempo Real: Implementação de cliente consola Python
    - Gerador de Planos de Estudo Interativo: Aplicação web conversacional Chainlit
    - Documentação In-Editor: Integração VS Code e GitHub Copilot
    - Azure API Management: Padrões de integração API empresariais
    - Registo MCP GitHub: Desenvolvimento do ecossistema e plataforma comunitária
  - **Conclusão Abrangente**: Seção final reescrita destacando os sete estudos de caso abrangendo múltiplas dimensões de implementação MCP
    - Integração Empresarial, Orquestração Multi-Agente, Produtividade do Desenvolvedor
    - Desenvolvimento do Ecossistema, Categorizações de Aplicações Educacionais
    - Insights aprimorados sobre padrões arquiteturais, estratégias de implementação e melhores práticas
    - Ênfase no MCP como protocolo maduro e pronto para produção

#### Atualizações no Guia de Estudo (study_guide.md)
- **Mapa Visual do Currículo**: Atualizado mindmap para incluir Registo MCP GitHub na secção Estudos de Caso
- **Descrição dos Estudos de Caso**: Melhorada de descrições genéricas para análise detalhada dos sete estudos de caso abrangentes
- **Estrutura do Repositório**: Atualizada a secção 10 para refletir cobertura abrangente dos estudos de caso com detalhes específicos de implementação
- **Integração do Changelog**: Adicionada entrada de 26 de setembro de 2025 documentando a adição do Registo MCP GitHub e melhorias nos estudos de caso
- **Atualizações de Datas**: Atualizado timestamp do rodapé para refletir a revisão mais recente (26 de setembro de 2025)

### Melhorias na Qualidade da Documentação
- **Reforço da Consistência**: Formatação e estrutura padronizadas para todos os sete estudos de caso
- **Cobertura Abrangente**: Estudos de caso agora abrangem cenários empresariais, produtividade do desenvolvedor e desenvolvimento do ecossistema
- **Posicionamento Estratégico**: Foco reforçado no MCP como plataforma fundamental para deployment de sistemas agentic
- **Integração de Recursos**: Atualizados recursos adicionais para incluir link para o Registo MCP GitHub

## 15 de Setembro de 2025

### Expansão de Tópicos Avançados - Transportes Personalizados & Engenharia de Contexto

#### Transportes Personalizados MCP (05-AdvancedTopics/mcp-transport/) - Novo Guia de Implementação Avançada
- **README.md**: Guia completo para mecanismos de transporte MCP personalizados
  - **Transporte Azure Event Grid**: Implementação abrangente serverless e orientada por eventos
    - Exemplos em C#, TypeScript e Python com integração Azure Functions
    - Padrões de arquitetura orientada a eventos para soluções MCP escaláveis
    - Receptores webhook e gestão baseada em push de mensagens
  - **Transporte Azure Event Hubs**: Implementação de transporte de streaming de alta performance
    - Capacidades de streaming em tempo real para cenários de baixa latência
    - Estratégias de particionamento e gestão de pontos de verificação
    - Agrupamento de mensagens e otimização de performance
  - **Padrões de Integração Empresariais**: Exemplos arquiteturais prontos para produção
    - Processamento MCP distribuído em múltiplas Azure Functions
    - Arquiteturas híbridas de transporte combinando vários tipos de transporte
    - Durabilidade, fiabilidade e gestão de erros em mensagens
  - **Segurança & Monitorização**: Integração Azure Key Vault e padrões de observabilidade
    - Autenticação gerida por identidade e acesso com princípio de privilégio mínimo
    - Telemetria Application Insights e monitorização de performance
    - Circuit breakers e padrões de tolerância a falhas
  - **Frameworks de Testes**: Estratégias completas para testar transportes personalizados
    - Testes unitários com test doubles e frameworks de mocking
    - Testes de integração com Azure Test Containers
    - Considerações para testes de performance e carga

#### Engenharia de Contexto (05-AdvancedTopics/mcp-contextengineering/) - Disciplina Emergente em IA
- **README.md**: Exploração abrangente da engenharia de contexto como área emergente
  - **Princípios Centrais**: Partilha completa de contexto, consciência da decisão de ações e gestão da janela de contexto
  - **Alinhamento com o Protocolo MCP**: Como o design MCP aborda desafios da engenharia de contexto
    - Limitações da janela de contexto e estratégias de carregamento progressivo
    - Determinação de relevância e recuperação dinâmica de contexto
    - Gestão multimodal de contexto e considerações de segurança
  - **Abordagens de Implementação**: Arquiteturas single-threaded vs. multi-agente
    - Técnicas de fragmentação e priorização do contexto
    - Carregamento progressivo de contexto e estratégias de compressão
    - Abordagens em camadas de contexto e otimizações de recuperação
  - **Framework de Medição**: Métricas emergentes para avaliação da eficácia do contexto
    - Eficiência da entrada, desempenho, qualidade e experiência do utilizador
    - Abordagens experimentais para otimização do contexto
    - Análise de falhas e metodologias de melhoria

#### Atualizações na Navegação do Currículo (README.md)
- **Estrutura do Módulo Aprimorada**: Atualizada a tabela curricular para incluir novos tópicos avançados
  - Adicionados Context Engineering (5.14) e Custom Transport (5.15)
  - Formatação e links de navegação consistentes em todos os módulos
  - Descrições atualizadas para refletir o âmbito atual do conteúdo

### Melhorias na Estrutura do Diretório
- **Padronização de Nomenclatura**: Renomeado "mcp transport" para "mcp-transport" para consistência com outras pastas de tópicos avançados
- **Organização do Conteúdo**: Todas as pastas 05-AdvancedTopics agora seguem padrão consistente de nomenclatura (mcp-[topic])

### Aperfeiçoamentos na Qualidade da Documentação
- **Alinhamento com Especificação MCP**: Todo o novo conteúdo referencia a atual Especificação MCP 2025-06-18
- **Exemplos Multilinguagem**: Exemplos completos em código C#, TypeScript e Python
- **Foco Empresarial**: Padrões prontos para produção e integração com a nuvem Azure
- **Documentação Visual**: Diagramas Mermaid para visualização da arquitetura e fluxos

## 18 de Agosto de 2025

### Atualização Abrangente da Documentação - Padrões MCP 2025-06-18

#### Melhores Práticas de Segurança MCP (02-Security/) - Modernização Completa
- **MCP-SECURITY-BEST-PRACTICES-2025.md**: Reescrita completa alinhada com a Especificação MCP 2025-06-18  
  - **Requisitos Obrigatórios**: Adicionados requisitos MUST/MUST NOT explícitos da especificação oficial com indicadores visuais claros  
  - **12 Práticas de Segurança Core**: Reestruturadas de lista de 15 itens para domínios abrangentes de segurança  
    - Segurança de Token & Autenticação com integração de fornecedor de identidade externo  
    - Gestão de Sessões & Segurança de Transporte com requisitos criptográficos  
    - Proteção Específica a Ameaças de IA com integração Microsoft Prompt Shields  
    - Controlo de Acesso & Permissões com princípio do menor privilégio  
    - Segurança de Conteúdo & Monitorização com integração Azure Content Safety  
    - Segurança da Cadeia de Abastecimento com verificação abrangente de componentes  
    - Segurança OAuth & Prevenção de Confused Deputy com implementação PKCE  
    - Resposta a Incidentes & Recuperação com capacidades automatizadas  
    - Conformidade & Governança com alinhamento regulatório  
    - Controlo Avançado de Segurança com arquitetura zero trust  
    - Integração do Ecossistema de Segurança Microsoft com soluções abrangentes  
    - Evolução Contínua da Segurança com práticas adaptativas  
  - **Soluções de Segurança Microsoft**: Orientação melhorada para integração com Prompt Shields, Azure Content Safety, Entra ID, e GitHub Advanced Security  
  - **Recursos de Implementação**: Links de recursos categorizados por Documentação Oficial MCP, Soluções de Segurança Microsoft, Normas de Segurança e Guias de Implementação  

#### Controlo Avançado de Segurança (02-Security/) - Implementação Empresarial  
- **MCP-SECURITY-CONTROLS-2025.md**: Reformulação completa com framework de segurança em nível empresarial  
  - **9 Domínios Abrangentes de Segurança**: Ampliados de controlos básicos para framework empresarial detalhado  
    - Autenticação & Autorização Avançadas com integração Microsoft Entra ID  
    - Segurança de Token & Controlos Anti-Passthrough com validação abrangente  
    - Controlos de Segurança de Sessão com prevenção de sequestro  
    - Controlos de Segurança Específicos de IA com prevenção de prompt injection e envenenamento de ferramentas  
    - Prevenção de Ataques Confused Deputy com segurança de proxy OAuth  
    - Segurança de Execução de Ferramentas com sandboxing e isolamento  
    - Controlos de Segurança da Cadeia de Abastecimento com verificação de dependências  
    - Controlos de Monitorização & Detecção com integração SIEM  
    - Resposta a Incidentes & Recuperação com capacidades automatizadas  
  - **Exemplos de Implementação**: Inclusão de blocos de configuração YAML detalhados e exemplos de código  
  - **Integração de Soluções Microsoft**: Cobertura abrangente dos serviços de segurança Azure, GitHub Advanced Security e gestão de identidade empresarial  

#### Tópicos Avançados de Segurança (05-AdvancedTopics/mcp-security/) - Implementação Pronta para Produção  
- **README.md**: Reescrita completa para implementação de segurança empresarial  
  - **Alinhamento com Especificação Atual**: Atualizado para Especificação MCP 2025-06-18 com requisitos obrigatórios de segurança  
  - **Autenticação Melhorada**: Integração Microsoft Entra ID com exemplos abrangentes em .NET e Java Spring Security  
  - **Integração de Segurança IA**: Implementação Microsoft Prompt Shields e Azure Content Safety com exemplos detalhados em Python  
  - **Mitigação Avançada de Ameaças**: Exemplos abrangentes para  
    - Prevenção de Ataques Confused Deputy com PKCE e validação de consentimento do utilizador  
    - Prevenção de Token Passthrough com validação de audiência e gestão segura de tokens  
    - Prevenção de Sequestro de Sessão com ligação criptográfica e análise comportamental  
  - **Integração de Segurança Empresarial**: Monitorização Azure Application Insights, pipelines de deteção de ameaças e segurança da cadeia de abastecimento  
  - **Checklist de Implementação**: Controlo claros obrigatórios vs recomendados com benefícios do ecossistema de segurança Microsoft  

### Qualidade da Documentação & Alinhamento de Normas  
- **Referências da Especificação**: Atualizadas todas as referências para a Especificação MCP 2025-06-18  
- **Ecossistema de Segurança Microsoft**: Orientação de integração reforçada em toda a documentação de segurança  
- **Implementação Prática**: Adição de exemplos de código detalhados em .NET, Java e Python com padrões empresariais  
- **Organização de Recursos**: Categorização abrangente da documentação oficial, normas de segurança e guias de implementação  
- **Indicadores Visuais**: Marcação clara de requisitos obrigatórios vs práticas recomendadas  

#### Conceitos Core (01-CoreConcepts/) - Modernização Completa  
- **Atualização de Versão do Protocolo**: Atualizado para referenciar a Especificação MCP atual 2025-06-18 com versão baseada em data (formato AAAA-MM-DD)  
- **Refinamento da Arquitetura**: Descrições melhoradas de Hosts, Clientes e Servidores para refletir padrões atuais da arquitetura MCP  
  - Hosts agora claramente definidos como aplicações IA coordenando múltiplas ligações MCP cliente  
  - Clientes descritos como conectores de protocolo mantendo relações um-para-um com servidores  
  - Servidores melhorados com cenários de implantação local vs remota  
- **Reestruturação dos Primitivos**: Reformulação completa dos primitivos servidor e cliente  
  - Primitivos do Servidor: Recursos (fontes de dados), Prompts (modelos), Ferramentas (funções executáveis) com explicações e exemplos detalhados  
  - Primitivos do Cliente: Sampling (completions de LLM), Elicitação (entrada de utilizador), Logging (debug/monitorização)  
  - Atualizado para padrões atuais de métodos discovery (`*/list`), retrieval (`*/get`) e execution (`*/call`)  
- **Arquitetura do Protocolo**: Introdução de modelo de arquitetura em duas camadas  
  - Camada de Dados: Base JSON-RPC 2.0 com gestão do ciclo de vida e primitivos  
  - Camada de Transporte: STDIO (local) e HTTP transmissível com SSE (transporte remoto)  
- **Framework de Segurança**: Princípios abrangentes de segurança incluindo consentimento explícito do utilizador, proteção de privacidade de dados, segurança de execução de ferramentas e segurança da camada de transporte  
- **Padrões de Comunicação**: Mensagens de protocolo atualizadas mostrando inicialização, descoberta, execução e fluxos de notificação  
- **Exemplos de Código**: Exemplos multi-linguagem atualizados (.NET, Java, Python, JavaScript) refletindo padrões atuais do SDK MCP  

#### Segurança (02-Security/) - Reformulação Abrangente de Segurança  
- **Alinhamento com Normas**: Total alinhamento com requisitos de segurança da Especificação MCP 2025-06-18  
- **Evolução da Autenticação**: Documentada evolução de servidores OAuth customizados para delegação de fornecedores de identidade externos (Microsoft Entra ID)  
- **Análise Específica de Ameaças IA**: Cobertura reforçada de vetores modernos de ataque IA  
  - Cenários detalhados de ataques de prompt injection com exemplos reais  
  - Mecanismos de envenenamento de ferramentas e padrões de ataque "rug pull"  
  - Envenenamento da janela de contexto e ataques de confusão de modelo  
- **Soluções Microsoft para Segurança IA**: Cobertura abrangente do ecossistema de segurança Microsoft  
  - AI Prompt Shields com deteção avançada, spotlighting e técnicas de delimitador  
  - Padrões de integração Azure Content Safety  
  - GitHub Advanced Security para proteção da cadeia de abastecimento  
- **Mitigação Avançada de Ameaças**: Controlos de segurança detalhados para  
  - Sequestro de sessão com cenários de ataque MCP específicos e requisitos criptográficos para ID de sessão  
  - Problemas de confused deputy em cenários proxy MCP com requisitos explícitos de consentimento  
  - Vulnerabilidades de token passthrough com controlos obrigatórios de validação  
- **Segurança da Cadeia de Abastecimento**: Cobertura ampliada da cadeia de abastecimento IA incluindo modelos base, serviços de embeddings, provedores de contexto e APIs de terceiros  
- **Segurança de Fundação**: Integração reforçada com padrões de segurança empresariais incluindo arquitetura zero trust e ecossistema de segurança Microsoft  
- **Organização de Recursos**: Categorização abrangente de recursos por tipo (Docs Oficiais, Normas, Pesquisa, Soluções Microsoft, Guias de Implementação)  

### Melhorias na Qualidade da Documentação  
- **Objetivos de Aprendizagem Estruturados**: Objetivos de aprendizagem reforçados com resultados específicos e acionáveis  
- **Referências Cruzadas**: Adição de ligações entre tópicos relacionados de segurança e conceitos core  
- **Informação Atualizada**: Atualizados todos os dados de datas e ligações de especificação para padrões atuais  
- **Orientação de Implementação**: Regras de implementação específicas e acionáveis adicionadas em ambas as secções  

## 16 de julho de 2025  

### Melhorias no README e Navegação  
- Navegação da estrutura curricular completamente redesenhada no README.md  
- Substituição das tags `<details>` por formato baseado em tabelas mais acessível  
- Criação de opções alternativas de layout na nova pasta "alternative_layouts"  
- Adição de exemplos de navegação em estilo cartão, em separadores e acordeão  
- Atualização da secção de estrutura do repositório para incluir todos os arquivos mais recentes  
- Reforço da secção "Como Usar Este Currículo" com recomendações claras  
- Atualização dos links da especificação MCP para apontar para URLs corretos  
- Adição da secção de Context Engineering (5.14) na estrutura curricular  

### Atualizações no Guia de Estudo  
- Revisão completa do guia de estudo para alinhar com a estrutura atual do repositório  
- Inclusão de novas seções para Clientes MCP e Ferramentas, e Servidores MCP Populares  
- Atualização do Mapa Visual do Currículo para refletir todos os tópicos com precisão  
- Reforço das descrições dos Tópicos Avançados para cobrir todas as áreas especializadas  
- Atualização da secção de Estudos de Caso para refletir exemplos reais  
- Inclusão deste changelog abrangente  

### Contribuições da Comunidade (06-CommunityContributions/)  
- Informação detalhada adicionada sobre servidores MCP para geração de imagens  
- Inclusão de secção abrangente sobre uso do Claude em VSCode  
- Adição de instruções para configuração e uso do cliente terminal Cline  
- Atualização da secção de clientes MCP para incluir todas as opções populares  
- Exemplos de contributos melhorados com amostras de código mais precisas  

### Tópicos Avançados (05-AdvancedTopics/)  
- Organização de todas as pastas de tópicos especializados com nomenclatura consistente  
- Adição de materiais e exemplos de engenharia de contexto  
- Inclusão da documentação de integração do agente Foundry  
- Reforço da documentação de integração de segurança Entra ID  

## 11 de junho de 2025  

### Criação Inicial  
- Lançamento da primeira versão do currículo MCP para Iniciantes  
- Criação da estrutura básica para todas as 10 secções principais  
- Implementação do Mapa Visual do Currículo para navegação  
- Inclusão dos primeiros projetos de exemplo em múltiplas linguagens de programação  

### Início Rápido (03-GettingStarted/)  
- Criação dos primeiros exemplos de implementação de servidor  
- Adição de orientação para desenvolvimento de clientes  
- Inclusão de instruções para integração de clientes LLM  
- Adição de documentação para integração VS Code  
- Implementação de exemplos de servidores com Server-Sent Events (SSE)  

### Conceitos Core (01-CoreConcepts/)  
- Explicação detalhada da arquitetura cliente-servidor adicionada  
- Criação de documentação sobre componentes chave do protocolo  
- Documentação dos padrões de mensagens do MCP  

## 23 de maio de 2025  

### Estrutura do Repositório  
- Inicialização do repositório com estrutura básica de pastas  
- Criação de ficheiros README para cada secção principal  
- Configuração da infraestrutura de tradução  
- Adição de ativos de imagem e diagramas  

### Documentação  
- Criação do README.md inicial com visão geral do currículo  
- Adição de CODE_OF_CONDUCT.md e SECURITY.md  
- Configuração de SUPPORT.md com orientações para suporte  
- Criação da estrutura preliminar do guia de estudo  

## 15 de abril de 2025  

### Planeamento e Framework  
- Planeamento inicial do currículo MCP para Iniciantes  
- Definição de objetivos de aprendizagem e público-alvo  
- Estrutura delineada de 10 secções do currículo  
- Desenvolvimento de framework conceptual para exemplos e estudos de caso  
- Criação dos primeiros protótipos de exemplos para conceitos chave  

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, por favor tenha em conta que traduções automáticas podem conter erros ou imprecisões. O documento original, na sua língua nativa, deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações erradas decorrentes do uso desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->