# Registro de Alterações: Currículo MCP para Iniciantes

Este documento serve como registro de todas as alterações significativas feitas no currículo Model Context Protocol (MCP) para Iniciantes. As mudanças são documentadas em ordem cronológica reversa (alterações mais recentes primeiro).

## 11 de abril de 2026

### Nova Aula, Correções na Documentação e Atualizações de Dependências

#### Novo Conteúdo do Currículo Adicionado

**Módulo 05 - Tópicos Avançados**
- **Aula 5.17: Raciocínio Multi-Agente Adversarial com MCP** (`05-AdvancedTopics/mcp-adversarial-agents/README.md`): Novo guia abrangente cobrindo o padrão de debate adversarial para sistemas multi-agente
  - Diagrama de arquitetura Mermaid: dois agentes → servidor MCP compartilhado → transcrição do debate → juiz → veredito
  - Servidor de ferramentas MCP compartilhado (`web_search` + `run_python`) implementado em Python e TypeScript
  - Prompts do sistema opostos (A FAVOR / CONTRA / Juiz) com requisitos explícitos de uso de ferramentas
  - Orquestrador de debate em Python, TypeScript e C# gerenciando rodadas e roteando argumentos
  - Fiação MCP `ClientSession` para o orquestrador com chamadas reais de ferramentas
  - Tabela de casos de uso (detecção de alucinação, modelagem de ameaças, revisão de design de API, verificação factual, seleção tecnológica)
  - Considerações de segurança: execução em sandbox, validação de chamadas de ferramentas, limitação de taxa, registro de auditoria
  - Exercício estruturado com três cenários práticos (revisão de código, decisão de arquitetura, moderação de conteúdo)

#### Correções na Documentação

**Módulo 03 - Primeiros Passos**
- **05-stdio-server/README.md**: Corrigido exemplo incompleto do servidor stdio em TypeScript — adicionada instância de transporte faltante (`new StdioServerTransport()`) e chamada `server.connect(transport)` para corresponder aos exemplos em Python e .NET na mesma seção
- **14-sampling/README.md**: Corrigido erro de digitação — corrigido `"Sampling is an davanced features"` → `"Sampling is an advanced feature"`

#### Atualizações do Currículo

**README.md Principal**
- Adicionada entrada 5.17 (Raciocínio Multi-Agente Adversarial com MCP) à tabela do currículo com link direto para a nova aula

**05-AdvancedTopics/README.md**
- Adicionada linha da Aula 5.17 à tabela de aulas

**study_guide.md**
- Adicionado o tópico Raciocínio Multi-Agente Adversarial ao mapa mental e descrição em prosa de Tópicos Avançados

#### Correções de Código e Segurança

**Módulo 05 - Agentes Adversariais (`mcp-adversarial-agents`)**
- **Correção de segurança — injeção de comando**: Substituída interpolação shell `execSync` pelo uso de `execFile` + `promisify` na ferramenta `run_python` em TypeScript, eliminando a superfície de injeção de comando (código controlado pelo LLM agora é passado como elemento literal argv sem envolvimento do shell)
- **Fiação do loop de ferramentas MCP**: Atualizado o orquestrador de debate em Python para usar cliente `AsyncAnthropic` (substituindo `Anthropic` síncrono bloqueante), passar um `ClientSession` ativo diretamente a cada turno do agente, buscar definições de ferramentas via `session.list_tools()` a cada turno e despachar blocos `tool_use` via `session.call_tool()` em loop até o modelo emitir resposta final em texto

#### Atualizações de Dependências

- Atualizado `hono` para 4.12.12 em múltiplos pacotes (03-GettingStarted, 04-PracticalImplementation, 10-StreamliningAIWorkflows)
- Atualizado `@hono/node-server` de 1.19.11 para 1.19.13 nos pacotes TypeScript
- Atualizado `cryptography` de 46.0.5 para 46.0.7 nos pacotes Python (10-StreamliningAIWorkflows labs 3 e 4)
- Atualizado `lodash` de 4.17.23 para 4.18.1 no inspetor 10-StreamliningAIWorkflows

#### Traduções

- Sincronizadas traduções para mais de 48 idiomas com as últimas alterações da fonte (atualização i18n)

---

## 5 de fevereiro de 2026

### Validação e Melhorias de Navegação no Repositório

#### Novo Conteúdo do Currículo Adicionado

**Módulo 03 - Primeiros Passos**
- **12-mcp-hosts/README.md**: Novo guia abrangente para configuração de hosts MCP
  - Exemplos de configuração Claude Desktop, VS Code, Cursor, Cline, Windsurf
  - Templates JSON de configuração para todos os hosts principais
  - Tabela comparativa de tipos de transporte (stdio, SSE/HTTP, WebSocket)
  - Resolução de problemas comuns de conexão
  - Melhores práticas de segurança para configuração de hosts

- **13-mcp-inspector/README.md**: Novo guia de depuração para MCP Inspector
  - Métodos de instalação (npx, npm global, fonte)
  - Conexão a servidores via stdio e HTTP/SSE
  - Ferramentas de teste, recursos, fluxos de trabalho de prompts
  - Integração com VS Code usando MCP Inspector
  - Cenários comuns de depuração com soluções

**Módulo 04 - Implementação Prática**
- **pagination/README.md**: Novo guia de implementação de paginação
  - Padrões de paginação baseados em cursor em Python, TypeScript, Java
  - Manipulação de paginação no cliente
  - Estratégias de design de cursor (opaco vs estruturado)
  - Recomendações de otimização de desempenho

**Módulo 05 - Tópicos Avançados**
- **mcp-protocol-features/README.md**: Novo mergulho profundo em recursos do protocolo
  - Implementação de notificações de progresso
  - Padrões de cancelamento de requisição
  - Templates de recursos com padrões de URI
  - Gerenciamento do ciclo de vida do servidor
  - Controle de nível de log
  - Padrões de tratamento de erros com códigos JSON-RPC

#### Correções de Navegação (mais de 24 arquivos atualizados)

**README dos Módulos Principais**  
 Agora links para a primeira aula E para o próximo módulo

**Subarquivos 02-Security**  
- Todos os 5 documentos suplementares de segurança agora possuem navegação "O que vem a seguir":

**Arquivos 09-CaseStudy**  
- Todos os arquivos de estudos de caso agora têm navegação sequencial:

**Labs 10-StreamliningAI**  
Adicionada seção "O que vem a seguir" à visão geral do módulo 10 e módulo 11

#### Correções de Código e Conteúdo

**Atualizações de SDK e Dependências**  
Corrigida versão vazia do openai para `^4.95.0`  
Atualizado SDK de `^1.8.0` para `>=1.26.0`  
Atualizados pins de versão do mcp para `>=1.26.0`

**Correções de Código**  
Corrigido modelo inválido `gpt-4o-mini` para `gpt-4.1-mini`

**Correções de Conteúdo**  
Corrigido link quebrado `READMEmd` → `README.md`, corrigido cabeçalho do currículo `Module 1-3` → `Module 0-3`, corrigido caminho case-sensitive  
Removido conteúdo duplicado corrompido do Estudo de Caso 5

**Melhorias de Orientação para Iniciantes**  
Adicionada introdução adequada, objetivos de aprendizado e pré-requisitos para iniciantes

#### Atualizações do Currículo

**README.md Principal**
- Adicionadas entradas 3.12 (Hosts MCP), 3.13 (Inspector MCP), 4.1 (Paginação), 5.16 (Recursos do Protocolo) à tabela do currículo

**README dos Módulos**
Adicionadas aulas 12 e 13 à lista de aulas  
Adicionada seção Guias Práticos com link para paginação  
Adicionadas aulas 5.15 (Transporte Customizado) e 5.16 (Recursos do Protocolo)

**study_guide.md**
- Atualizado mapa mental com todos os novos tópicos: Configuração de Hosts MCP, MCP Inspector, Estratégias de Paginação, Análise Profunda de Recursos do Protocolo

## 28 de janeiro de 2026

### Revisão de Conformidade com a Especificação MCP 2025-11-25

#### Aprimoramento de Conceitos Fundamentais (01-CoreConcepts/)
- **Nova Primitiva Cliente - Roots**: Adicionada documentação abrangente sobre a primitiva cliente Roots, permitindo que servidores entendam limites do sistema de arquivos e permissões de acesso
- **Anotações de Ferramentas**: Adicionada documentação sobre anotações comportamentais de ferramentas (`readOnlyHint`, `destructiveHint`) para melhores decisões de execução
- **Chamada de Ferramentas em Amostragem**: Atualizada documentação de Amostragem para incluir parâmetros `tools` e `toolChoice` para invocação de ferramentas dirigida pelo modelo durante requisições de amostragem
- **Elucidação em Modo URL**: Adicionada documentação sobre elucidação baseada em URL para interações externas iniciadas pelo servidor
- **Tarefas (Experimental)**: Adicionada nova seção documentando o recurso experimental de Tarefas para wrappers de execução durável e recuperação deferida de resultados
- **Suporte a Ícones**: Notado que ferramentas, recursos, templates de recursos e prompts podem agora incluir ícones como metadados adicionais

#### Atualizações na Documentação
- **README.md**: Adicionada referência à versão da Especificação MCP 2025-11-25 e explicação de versionamento baseado em datas
- **study_guide.md**: Atualizado mapa do currículo para incluir Tarefas e Anotações de Ferramentas na seção Conceitos Fundamentais; atualizado timestamp do documento

#### Verificação de Conformidade da Especificação
- **Versão do Protocolo**: Verificada que toda a documentação referencia a atual Especificação MCP 2025-11-25  
- **Alinhamento de Arquitetura**: Confirmada a precisão da documentação da arquitetura em duas camadas (Camada de Dados + Camada de Transporte)  
- **Documentação das Primitivas**: Validada documentação de primitivas do servidor (Recursos, Prompts, Ferramentas) e primitivas do cliente (Amostragem, Elucidação, Registro, Roots)  
- **Mecanismos de Transporte**: Verificada precisão da documentação de transporte STDIO e HTTP em streaming  
- **Orientações de Segurança**: Confirmado alinhamento com as melhores práticas de segurança MCP atualmente documentadas

#### Principais Recursos MCP 2025-11-25 Documentados
- **Descoberta OpenID Connect**: Descoberta do servidor de autenticação via OIDC  
- **Documentos de Metadados OAuth Client ID**: Mecanismo recomendado para registro de cliente  
- **JSON Schema 2020-12**: Dialeto padrão para definições de esquema MCP  
- **Sistema de Camadas do SDK**: Requisitos formalizados para suporte e manutenção de recursos do SDK  
- **Estrutura de Governança**: Grupos de Trabalho e Grupos de Interesse formalizados na governança MCP

### Grande Atualização da Documentação de Segurança (02-Security/)

#### Integração do Workshop MCP Security Summit (Sherpa)
- **Novo Recurso de Treinamento Prático**: Integrado o workshop [MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/) em toda a documentação de segurança  
- **Cobertura da Rota da Expedição**: Documentada progressão completa acampamento a acampamento do Base Camp ao Summit  
- **Alinhamento OWASP**: Toda orientação de segurança agora mapeada aos riscos do OWASP MCP Azure Security Guide  

#### Integração OWASP MCP Top 10
- **Nova Seção**: Adicionada tabela dos 10 principais riscos de segurança OWASP MCP com mitigações Azure no README principal de segurança  
- **Documentação Baseada em Riscos**: Atualizado mcp-security-controls-2025.md com referências aos riscos OWASP MCP para cada domínio de segurança  
- **Arquitetura de Referência**: Linkada arquitetura e padrões de implementação OWASP MCP Azure Security Guide

#### Arquivos de Segurança Atualizados
- **README.md**: Adicionada visão geral do Workshop Sherpa, tabela da rota da expedição, resumo dos riscos OWASP MCP Top 10 e seção de treinamento prático  
- **mcp-security-controls-2025.md**: Atualizado cabeçalho para fevereiro de 2026, adicionadas referências de risco OWASP (MCP01-MCP08), corrigida inconsistência de versão da especificação  
- **mcp-security-best-practices-2025.md**: Adicionada seção de recursos Sherpa e OWASP, atualizado timestamp  
- **mcp-best-practices.md**: Adicionada seção de treinamento prático com links Sherpa e OWASP  
- **azure-content-safety-implementation.md**: Adicionado referência OWASP MCP06, alinhamento ao Acampamento 3 Sherpa e seção de recursos adicionais

#### Novos Links de Recursos Adicionados
- [MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/)  
- [OWASP MCP Azure Security Guide](https://microsoft.github.io/mcp-azure-security-guide/)  
- [OWASP MCP Top 10](https://owasp.org/www-project-mcp-top-10/)  
- Páginas individuais de risco OWASP MCP (MCP01-MCP10)  

### Alinhamento do Currículo com a Especificação MCP 2025-11-25

#### Módulo 03 - Primeiros Passos
- **Documentação do SDK**: Adicionado SDK Go à lista oficial de SDKs; atualizadas todas referências de SDK para alinhar com a Especificação MCP 2025-11-25  
- **Esclarecimento de Transporte**: Atualizadas descrições dos transportes STDIO e HTTP Streaming com referências explícitas à especificação

#### Módulo 04 - Implementação Prática
- **Atualizações do SDK**: Adicionado SDK Go; atualizada lista de SDKs com referência da versão da especificação  
- **Especificação de Autorização**: Atualizado link para especificação MCP Authorization versão 2025-11-25

#### Módulo 05 - Tópicos Avançados
- **Novos Recursos**: Adicionada nota sobre novos recursos da Especificação MCP 2025-11-25 (Tarefas, Anotações de Ferramentas, Elucidação em Modo URL, Roots)  
- **Recursos de Segurança**: Adicionados links OWASP MCP Top 10 e workshop Sherpa às referências adicionais

#### Módulo 06 - Contribuições da Comunidade
- **Lista de SDKs**: Adicionados SDKs Swift e Rust; atualizado link da especificação para 2025-11-25  
- **Referência da Especificação**: Atualizado link direto para a URL da especificação MCP

#### Módulo 07 - Lições da Adoção Precoce
- **Atualizações de Recursos**: Adicionado link da Especificação MCP 2025-11-25 e OWASP MCP Top 10 às referências adicionais

#### Módulo 08 - Melhores Práticas
- **Versão da Especificação**: Atualizado referência da Especificação MCP para 2025-11-25  
- **Recursos de Segurança**: Adicionados OWASP MCP Top 10 e workshop Sherpa às referências adicionais

#### Módulo 10 - Otimizando Fluxos de Trabalho de IA
- **Atualização de Badge**: Alterado identificador de versão MCP de versão do SDK (1.9.3) para versão da especificação (2025-11-25)  
- **Links de Recursos**: Atualizado link da Especificação MCP; adicionado OWASP MCP Top 10

#### Módulo 11 - Laboratórios Práticos MCP Server
- **Referência da Especificação**: Atualizado link da Especificação MCP para versão 2025-11-25  
- **Recursos de Segurança**: Adicionado OWASP MCP Top 10 aos recursos oficiais

## 18 de dezembro de 2025
### Atualização da Documentação de Segurança - Especificação MCP 2025-11-25

#### Melhores Práticas de Segurança MCP (02-Security/mcp-best-practices.md) - Atualização da Versão da Especificação
- **Atualização da Versão do Protocolo**: Atualizado para referenciar a última Especificação MCP 2025-11-25 (lançada em 25 de novembro de 2025)
  - Atualizadas todas as referências de versão da especificação de 2025-06-18 para 2025-11-25
  - Atualizadas as referências de data do documento de 18 de agosto de 2025 para 18 de dezembro de 2025
  - Verificados todos os URLs da especificação para apontar para a documentação atual
- **Validação de Conteúdo**: Validação abrangente das melhores práticas de segurança em conformidade com os padrões mais recentes
  - **Soluções de Segurança Microsoft**: Verificados termos e links atuais para Prompt Shields (anteriormente "Detecção de risco de Jailbreak"), Azure Content Safety, Microsoft Entra ID e Azure Key Vault
  - **Segurança OAuth 2.1**: Confirmada conformidade com as melhores práticas recentes de segurança OAuth
  - **Padrões OWASP**: Validada atualização das referências do OWASP Top 10 para LLMs
  - **Serviços Azure**: Verificados todos os links e melhores práticas de documentação Microsoft Azure
- **Alinhamento aos Padrões**: Todos os padrões de segurança referenciados confirmados atuais
  - NIST AI Risk Management Framework
  - ISO 27001:2022
  - Melhores Práticas de Segurança OAuth 2.1
  - Frameworks de segurança e conformidade Azure
- **Recursos de Implementação**: Validados todos os links e recursos de guias de implementação
  - Padrões de autenticação Azure API Management
  - Guias de integração Microsoft Entra ID
  - Gerenciamento de segredos Azure Key Vault
  - Pipelines e soluções de monitoramento DevSecOps

### Garantia de Qualidade da Documentação
- **Conformidade com a Especificação**: Assegurada alinhamento de todos os requisitos obrigatórios de segurança MCP (DEVE/ NÃO DEVE) com a especificação mais recente
- **Atualização de Recursos**: Verificados todos os links externos para documentação Microsoft, padrões de segurança e guias de implementação
- **Cobertura das Melhores Práticas**: Confirmada cobertura abrangente de autenticação, autorização, ameaças específicas de IA, segurança da cadeia de suprimentos e padrões empresariais

## 6 de outubro de 2025

### Expansão da Seção Introdução – Uso Avançado do Servidor & Autenticação Simples

#### Uso Avançado do Servidor (03-GettingStarted/10-advanced)
- **Novo Capítulo Adicionado**: Guia abrangente para uso avançado do servidor MCP, cobrindo arquiteturas de servidor regulares e de baixo nível.
  - **Servidor Regular vs. Baixo Nível**: Comparação detalhada e exemplos de código em Python e TypeScript para ambas as abordagens.
  - **Design Baseado em Handlers**: Explicação do gerenciamento de ferramentas/recursos/prompt baseado em handlers para implementações de servidor escaláveis e flexíveis.
  - **Padrões Práticos**: Cenários reais onde padrões de servidor de baixo nível são benéficos para recursos avançados e arquitetura.

#### Autenticação Simples (03-GettingStarted/11-simple-auth)
- **Novo Capítulo Adicionado**: Guia passo a passo para implementar autenticação simples em servidores MCP.
  - **Conceitos de Autenticação**: Explicação clara sobre autenticação vs. autorização e manipulação de credenciais.
  - **Implementação Básica de Auth**: Padrões de autenticação baseados em middleware em Python (Starlette) e TypeScript (Express), com exemplos de código.
  - **Evolução para Segurança Avançada**: Orientações para iniciar com autenticação simples e evoluir para OAuth 2.1 e RBAC, com referências a módulos avançados de segurança.

Essas adições oferecem orientações práticas e práticas para construir implementações de servidores MCP mais robustas, seguras e flexíveis, conectando conceitos fundamentais a padrões avançados de produção.

## 29 de setembro de 2025

### Laboratórios de Integração de Banco de Dados MCP - Caminho Completo de Aprendizado Prático

#### 11-MCPServerHandsOnLabs - Novo Currículo Completo de Integração de Banco de Dados
- **Caminho de Aprendizado Completo com 13 Laboratórios**: Adicionado currículo prático abrangente para construção de servidores MCP prontos para produção com integração de banco de dados PostgreSQL
  - **Implementação Realista**: Caso de uso de análise Zava Retail demonstrando padrões de nível empresarial
  - **Progressão Estruturada de Aprendizado**:
    - **Laboratórios 00-03: Fundamentos** - Introdução, Arquitetura Central, Segurança & Multi-Tenancy, Configuração do Ambiente
    - **Laboratórios 04-06: Construção do Servidor MCP** - Design & Esquema de Banco de Dados, Implementação do Servidor MCP, Desenvolvimento de Ferramentas  
    - **Laboratórios 07-09: Recursos Avançados** - Integração de Pesquisa Semântica, Testes & Depuração, Integração com VS Code
    - **Laboratórios 10-12: Produção & Melhores Práticas** - Estratégias de Implantação, Monitoramento & Observabilidade, Melhores Práticas & Otimização
  - **Tecnologias Empresariais**: Framework FastMCP, PostgreSQL com pgvector, embeddings Azure OpenAI, Azure Container Apps, Application Insights
  - **Recursos Avançados**: Segurança a nível de linha (RLS), pesquisa semântica, acesso a dados multi-tenant, embeddings vetoriais, monitoramento em tempo real

#### Padronização de Terminologia - Conversão de Módulo para Laboratório
- **Atualização Abrangente da Documentação**: Atualizados sistematicamente todos os arquivos README em 11-MCPServerHandsOnLabs para utilizar a terminologia "Laboratório" em vez de "Módulo"
  - **Cabeçalhos de Seção**: Atualizado de "O que este Módulo cobre" para "O que este Laboratório cobre" nos 13 laboratórios
  - **Descrição de Conteúdo**: Alterado "Este módulo fornece..." para "Este laboratório fornece..." em toda documentação
  - **Objetivos de Aprendizado**: Atualizado "Ao final deste módulo..." para "Ao final deste laboratório..."
  - **Links de Navegação**: Convertidas todas as referências "Módulo XX:" para "Laboratório XX:" em cross-references e navegação
  - **Rastreamento de Conclusão**: Atualizado "Após concluir este módulo..." para "Após concluir este laboratório..."
  - **Referências Técnicas Preservadas**: Mantidas referências a módulos Python em arquivos de configuração (ex.: `"module": "mcp_server.main"`)

#### Aprimoramento do Guia de Estudo (study_guide.md)
- **Mapa Visual do Currículo**: Adicionada nova seção "11. Laboratórios de Integração de Banco de Dados" com visualização completa da estrutura dos laboratórios
- **Estrutura do Repositório**: Atualizado de dez para onze as seções principais com descrição detalhada de 11-MCPServerHandsOnLabs
- **Orientação para Caminho de Aprendizado**: Instruções de navegação ampliadas para cobrir seções 00-11
- **Cobertura Tecnológica**: Adicionados detalhes da integração FastMCP, PostgreSQL, serviços Azure
- **Resultados de Aprendizado**: Ênfase em desenvolvimento de servidores preparados para produção, padrões de integração de banco de dados e segurança empresarial

#### Aprimoramento da Estrutura do README Principal
- **Terminologia Baseada em Laboratórios**: Atualizado README.md principal em 11-MCPServerHandsOnLabs para uso consistente da estrutura "Laboratório"
- **Organização do Caminho de Aprendizado**: Progressão clara do conceito básico à implementação avançada e implantação em produção
- **Foco Realista**: Ênfase em aprendizado prático, com padrões e tecnologias de nível empresarial

### Melhorias na Qualidade & Consistência da Documentação
- **Ênfase no Aprendizado Prático**: Reforçado abordagem prática baseada em laboratórios ao longo da documentação
- **Foco em Padrões Empresariais**: Destacadas implementações prontas para produção e considerações de segurança empresarial
- **Integração Tecnológica**: Cobertura abrangente dos serviços modernos Azure e padrões de integração IA
- **Progressão de Aprendizado**: Caminho claro e estruturado do básico à implantação em produção

## 26 de setembro de 2025

### Aprimoramento de Estudos de Caso - Integração do Registro MCP GitHub

#### Estudos de Caso (09-CaseStudy/) - Foco em Desenvolvimento do Ecossistema
- **README.md**: Expansão significativa com estudo de caso abrangente do Registro MCP GitHub
  - **Estudo de Caso Registro MCP GitHub**: Novo estudo detalhado examinando o lançamento do Registro MCP do GitHub em setembro de 2025
    - **Análise do Problema**: Exame detalhado dos desafios fragmentados de descoberta e implantação de servidores MCP
    - **Arquitetura da Solução**: Abordagem centralizada do registro GitHub com instalação de um clique no VS Code
    - **Impacto no Negócio**: Melhorias mensuráveis no onboarding e produtividade dos desenvolvedores
    - **Valor Estratégico**: Foco em implantação modular de agentes e interoperabilidade entre ferramentas
    - **Desenvolvimento do Ecossistema**: Posicionamento como plataforma fundamental para integração agentiva
  - **Estrutura Aprimorada dos Estudos de Caso**: Atualizados os sete estudos de caso com formatação consistente e descrições abrangentes
    - Agentes de Viagem Azure AI: Ênfase em orquestração multi-agente
    - Integração Azure DevOps: Foco em automação de fluxo de trabalho
    - Recuperação de Documentação em Tempo Real: Implementação de cliente console Python
    - Gerador de Plano de Estudo Interativo: Aplicação web conversacional Chainlit
    - Documentação no Editor: Integração VS Code e GitHub Copilot
    - Azure API Management: Padrões empresariais de integração de API
    - Registro MCP GitHub: Desenvolvimento do ecossistema e plataforma comunitária
  - **Conclusão Abrangente**: Seção de conclusão reescrita destacando os sete estudos de caso que abrangem múltiplas dimensões de implementação MCP
    - Integração empresarial, orquestração multi-agente, produtividade do desenvolvedor
    - Desenvolvimento do ecossistema, aplicações educacionais categorizadas
    - Insights aprimorados sobre padrões arquiteturais, estratégias de implementação e melhores práticas
    - Ênfase no MCP como protocolo maduro, pronto para produção

#### Atualizações do Guia de Estudo (study_guide.md)
- **Mapa Visual do Currículo**: Atualizado mindmap para incluir Registro MCP GitHub na seção Estudos de Caso
- **Descrição dos Estudos de Caso**: Ampliada de descrições genéricas para detalhamento dos sete estudos completos
- **Estrutura do Repositório**: Atualizada seção 10 para refletir cobertura completa de estudos com detalhes específicos de implementação
- **Integração do Changelog**: Adicionada entrada de 26 de setembro de 2025 documentando a inclusão do Registro MCP GitHub e aprimoramentos dos estudos de caso
- **Atualização de Datas**: Rodapé de timestamp atualizado para refletir revisão mais recente (26 de setembro de 2025)

### Melhorias na Qualidade da Documentação
- **Aprimoramento da Consistência**: Padronizada formatação e estrutura dos estudos de caso em todos os sete exemplos
- **Cobertura Abrangente**: Estudos de caso agora abrangem cenários empresariais, produtividade do desenvolvedor e desenvolvimento de ecossistema
- **Posicionamento Estratégico**: Maior foco no MCP como plataforma fundamental para implantação de sistemas agentivos
- **Integração de Recursos**: Atualizados recursos adicionais para incluir link do Registro MCP GitHub

## 15 de setembro de 2025

### Expansão de Tópicos Avançados - Transportes Customizados & Engenharia de Contexto

#### Transportes Customizados MCP (05-AdvancedTopics/mcp-transport/) - Novo Guia de Implementação Avançada
- **README.md**: Guia completo de implementação de mecanismos de transporte customizados MCP
  - **Transporte Azure Event Grid**: Implementação abrangente de transporte serverless baseado em eventos
    - Exemplos em C#, TypeScript e Python com integração Azure Functions
    - Padrões de arquitetura orientada a eventos para soluções MCP escaláveis
    - Receptores webhook e manipulação de mensagens push
  - **Transporte Azure Event Hubs**: Implementação de transporte streaming de alta taxa
    - Capacidade de streaming em tempo real para cenários de baixa latência
    - Estratégias de particionamento e gerenciamento de checkpoints
    - Agrupamento de mensagens e otimização de performance
  - **Padrões de Integração Empresarial**: Exemplos arquiteturais prontos para produção
    - Processamento MCP distribuído entre múltiplas Azure Functions
    - Arquiteturas híbridas de transporte combinando tipos múltiplos
    - Estratégias para durabilidade, confiabilidade e tratamento de erros de mensagens
  - **Segurança & Monitoramento**: Integração Azure Key Vault e padrões de observabilidade
    - Autenticação por identity managed e acesso de privilégio mínimo
    - Telemetria Application Insights e monitoramento de performance
    - Circuit breakers e padrões de tolerância a falhas
  - **Frameworks de Teste**: Estratégias abrangentes para teste de transportes customizados
    - Testes unitários com test doubles e frameworks de mock
    - Testes de integração usando Azure Test Containers
    - Considerações para testes de performance e carga

#### Engenharia de Contexto (05-AdvancedTopics/mcp-contextengineering/) - Disciplina Emergente em IA
- **README.md**: Exploração abrangente da engenharia de contexto como campo emergente
  - **Princípios Centrais**: Compartilhamento completo de contexto, consciência na decisão de ações e gerenciamento de janelas de contexto
  - **Alinhamento ao Protocolo MCP**: Como o design MCP aborda desafios da engenharia de contexto
    - Limitações da janela de contexto e estratégias de carregamento progressivo
    - Determinação de relevância e recuperação dinâmica de contexto
    - Manipulação multimodal de contexto e considerações de segurança
  - **Abordagens de Implementação**: Arquiteturas single-threaded vs. multi-agent
    - Técnicas de divisão e priorização de blocos de contexto
    - Carregamento progressivo e estratégias de compressão de contexto
    - Abordagens em camadas e otimização da recuperação
  - **Framework de Medição**: Métricas emergentes para avaliação da eficácia do contexto
    - Eficiência na entrada, performance, qualidade e experiência do usuário
    - Abordagens experimentais para otimização de contexto
    - Análise de falhas e metodologias de melhoria

#### Atualizações na Navegação do Currículo (README.md)
- **Estrutura de Módulos Aprimorada**: Atualizado o quadro do currículo para incluir novos tópicos avançados
  - Adicionados Context Engineering (5.14) e Custom Transport (5.15)
  - Formatação consistente e links de navegação atualizados em todos os módulos
  - Descrições atualizadas para refletir o escopo de conteúdo corrente

### Melhorias na Estrutura de Diretórios
- **Padronização de Nomes**: Renomeado "mcp transport" para "mcp-transport" para consistência com outras pastas de tópicos avançados
- **Organização de Conteúdo**: Todas as pastas 05-AdvancedTopics seguem agora padrão consistente (mcp-[topico])

### Aperfeiçoamentos na Qualidade da Documentação
- **Alinhamento à Especificação MCP**: Todo o conteúdo novo referencia a Especificação MCP 2025-06-18 atual
- **Exemplos Multilíngues**: Exemplos abrangentes em C#, TypeScript e Python
- **Foco Empresarial**: Padrões prontos para produção e integração na nuvem Azure em todo o conteúdo
- **Documentação Visual**: Diagramas Mermaid para visualização de arquitetura e fluxo

## 18 de agosto de 2025

### Atualização Abrangente da Documentação - Padrões MCP 2025-06-18

#### Melhores Práticas de Segurança MCP (02-Security/) - Modernização Completa
- **MCP-SECURITY-BEST-PRACTICES-2025.md**: Reescrita completa alinhada com a Especificação MCP 2025-06-18  
  - **Requisitos Obrigatórios**: Inclusão de requisitos explícitos DEVE/NÃO DEVE da especificação oficial com indicadores visuais claros  
  - **12 Práticas de Segurança Principais**: Reestruturado de lista de 15 itens para domínios de segurança abrangentes  
    - Segurança de Token e Autenticação com integração a provedores externos de identidade  
    - Gestão de Sessão e Segurança de Transporte com requisitos criptográficos  
    - Proteção Contra Ameaças Específicas de IA com integração Microsoft Prompt Shields  
    - Controle de Acesso e Permissões com princípio do menor privilégio  
    - Segurança de Conteúdo e Monitoramento com integração Azure Content Safety  
    - Segurança da Cadeia de Suprimentos com verificação abrangente de componentes  
    - Segurança OAuth e Prevenção de Confused Deputy com implementação PKCE  
    - Resposta a Incidentes e Recuperação com capacidades automatizadas  
    - Conformidade e Governança alinhadas a regulamentações  
    - Controles Avançados de Segurança com arquitetura zero trust  
    - Integração ao Ecossistema de Segurança Microsoft com soluções completas  
    - Evolução Contínua da Segurança com práticas adaptativas  
  - **Soluções de Segurança Microsoft**: Melhoria na orientação de integração para Prompt Shields, Azure Content Safety, Entra ID e GitHub Advanced Security  
  - **Recursos de Implementação**: Links abrangentes categorizados por Documentação Oficial MCP, Soluções de Segurança Microsoft, Padrões de Segurança e Guias de Implementação  

#### Controles Avançados de Segurança (02-Security/) - Implementação Empresarial  
- **MCP-SECURITY-CONTROLS-2025.md**: Reformulação completa com framework de segurança para empresas  
  - **9 Domínios Abrangentes de Segurança**: Expansão de controles básicos para framework detalhado empresarial  
    - Autenticação e Autorização Avançadas com integração Microsoft Entra ID  
    - Segurança de Token e Controles Anti-Passthrough com validação abrangente  
    - Controles de Segurança de Sessão com prevenção de sequestro  
    - Controles Específicos de Segurança para IA com prevenção de injeção de prompt e envenenamento de ferramentas  
    - Prevenção de Ataque Confused Deputy com segurança proxy OAuth  
    - Segurança na Execução de Ferramentas com sandboxing e isolamento  
    - Controles de Segurança da Cadeia de Suprimentos com verificação de dependências  
    - Controles de Monitoramento e Detecção com integração SIEM  
    - Resposta a Incidentes e Recuperação com capacidades automatizadas  
  - **Exemplos de Implementação**: Inclusão de blocos detalhados de configuração YAML e exemplos de código  
  - **Integração com Soluções Microsoft**: Cobertura completa dos serviços de segurança Azure, GitHub Advanced Security e gerenciamento corporativo de identidade  

#### Segurança em Tópicos Avançados (05-AdvancedTopics/mcp-security/) - Implementação Pronta para Produção  
- **README.md**: Reescrita completa para implementação de segurança empresarial  
  - **Alinhamento com Especificação Atual**: Atualizado para Especificação MCP 2025-06-18 com requisitos obrigatórios de segurança  
  - **Autenticação Avançada**: Integração Microsoft Entra ID com exemplos completos em .NET e Java Spring Security  
  - **Integração de Segurança para IA**: Implementação Microsoft Prompt Shields e Azure Content Safety com exemplos detalhados em Python  
  - **Mitigação Avançada de Ameaças**: Exemplos completos para  
    - Prevenção de Ataque Confused Deputy com PKCE e validação de consentimento do usuário  
    - Prevenção de Passthrough de Token com validação de audiência e gestão segura de tokens  
    - Prevenção de Sequestro de Sessão com vínculo criptográfico e análise comportamental  
  - **Integração de Segurança Empresarial**: Monitoramento Azure Application Insights, pipelines de detecção de ameaças e segurança da cadeia de suprimentos  
  - **Checklist de Implementação**: Controles de segurança obrigatórios versus recomendados com benefícios do ecossistema Microsoft  

### Qualidade da Documentação & Alinhamento com Padrões  
- **Referências de Especificação**: Atualização de todas as referências para a Especificação MCP 2025-06-18  
- **Ecossistema de Segurança Microsoft**: Orientação de integração aprimorada em toda a documentação de segurança  
- **Implementação Prática**: Inclusão de exemplos detalhados em .NET, Java e Python com padrões empresariais  
- **Organização de Recursos**: Categorias abrangentes de documentação oficial, padrões de segurança e guias de implementação  
- **Indicadores Visuais**: Marcação clara de requisitos obrigatórios versus práticas recomendadas  

#### Conceitos Fundamentais (01-CoreConcepts/) - Modernização Completa  
- **Atualização da Versão do Protocolo**: Referência atualizada para Especificação MCP 2025-06-18 com versionamento baseado em data (formato AAAA-MM-DD)  
- **Aprimoramento na Arquitetura**: Descrições aprimoradas de Hosts, Clientes e Servidores para refletir padrões atuais MCP  
  - Hosts agora claramente definidos como aplicações IA coordenando múltiplas conexões MCP cliente  
  - Clientes descritos como conectores de protocolo mantendo relacionamentos um-para-um com servidores  
  - Servidores aprimorados com cenários locais versus remotos de implantação  
- **Reestruturação de Primitivas**: Revisão completa das primitivas de servidor e cliente  
  - Primitivas de Servidor: Recursos (fontes de dados), Prompts (modelos) e Ferramentas (funções executáveis) com explicações e exemplos detalhados  
  - Primitivas de Cliente: Amostragem (completions LLM), Elicitação (entrada do usuário), Registro (debug/monitoramento)  
  - Atualizado com padrões atuais de métodos discovery (`*/list`), recuperação (`*/get`) e execução (`*/call`)  
- **Arquitetura do Protocolo**: Introdução de modelo de arquitetura em duas camadas  
  - Camada de Dados: Base JSON-RPC 2.0 com gerenciamento de ciclo de vida e primitivas  
  - Camada de Transporte: STDIO (local) e HTTP Streamable com SSE (transporte remoto)  
- **Framework de Segurança**: Princípios de segurança abrangentes incluindo consentimento explícito do usuário, proteção de privacidade de dados, segurança na execução de ferramentas e segurança da camada de transporte  
- **Padrões de Comunicação**: Mensagens de protocolo atualizadas para mostrar fluxos de inicialização, descoberta, execução e notificação  
- **Exemplos de Código**: Atualizações dos exemplos multilíngues (.NET, Java, Python, JavaScript) para refletir padrões atuais SDK MCP  

#### Segurança (02-Security/) - Reformulação Abrangente de Segurança  
- **Alinhamento com Padrões**: Total conformidade com requisitos de segurança da Especificação MCP 2025-06-18  
- **Evolução da Autenticação**: Documentação da evolução de servidores OAuth customizados para delegação a provedores externos de identidade (Microsoft Entra ID)  
- **Análise de Ameaças Específicas para IA**: Cobertura ampliada de vetores modernos de ataque a IA  
  - Cenários detalhados de ataques de injeção de prompt com exemplos reais  
  - Mecanismos de envenenamento de ferramentas e padrões de ataques "rug pull"  
  - Envenenamento de janelas de contexto e ataques de confusão de modelo  
- **Soluções Microsoft para Segurança de IA**: Cobertura abrangente do ecossistema de segurança Microsoft  
  - AI Prompt Shields com técnicas avançadas de detecção, spotlighting e delimitadores  
  - Padrões de integração Azure Content Safety  
  - GitHub Advanced Security para proteção da cadeia de suprimentos  
- **Mitigação Avançada de Ameaças**: Controles detalhados de segurança para  
  - Sequestro de sessão com cenários MCP específicos e requisitos criptográficos para IDs de sessão  
  - Problemas Confused Deputy em cenários proxy MCP com requisitos explícitos de consentimento  
  - Vulnerabilidades de token passthrough com controles obrigatórios de validação  
- **Segurança da Cadeia de Suprimentos**: Expansão da cobertura de cadeia de suprimentos para IA incluindo modelos base, serviços de embeddings, provedores de contexto e APIs de terceiros  
- **Segurança Foundation**: Integração aprimorada com padrões empresariais de segurança incluindo arquitetura zero trust e ecossistema Microsoft  
- **Organização de Recursos**: Links categorizados por tipo (Documentos Oficiais, Padrões, Pesquisa, Soluções Microsoft, Guias de Implementação)  

### Melhorias na Qualidade da Documentação  
- **Objetivos de Aprendizagem Estruturados**: Objetivos de aprendizagem aprimorados com resultados específicos e acionáveis  
- **Referências Cruzadas**: Inclusão de links entre tópicos relacionados de segurança e conceitos fundamentais  
- **Informações Atualizadas**: Atualização de todas as referências de datas e links para especificações atuais  
- **Orientações de Implementação**: Adição de diretrizes específicas e acionáveis de implementação em ambas seções  

## 16 de julho de 2025

### Melhorias no README e Navegação  
- Navegação do currículo completamente redesenhada no README.md  
- Substituição das tags `<details>` por formato baseado em tabelas mais acessível  
- Criação de opções alternativas de layout na nova pasta "alternative_layouts"  
- Adicionados exemplos de navegação em estilo cartão, abas e acordeão  
- Atualização da seção de estrutura do repositório para incluir todos os arquivos mais recentes  
- Aprimoramento da seção "Como Usar Este Currículo" com recomendações claras  
- Atualização dos links da especificação MCP para URLs corretos  
- Inclusão da seção Engenharia de Contexto (5.14) na estrutura do currículo  

### Atualizações do Guia de Estudos  
- Guia de estudos completamente revisado para alinhar com a estrutura do repositório atual  
- Inclusão de novas seções para Clientes MCP, Ferramentas e Servidores MCP Populares  
- Atualização do Mapa Visual do Currículo para refletir todos os tópicos com exatidão  
- Aprimoramento das descrições de Tópicos Avançados para cobertura de todas as áreas especializadas  
- Atualização da seção Estudos de Caso para refletir exemplos reais  
- Inclusão deste changelog abrangente  

### Contribuições da Comunidade (06-CommunityContributions/)  
- Inclusão de informações detalhadas sobre servidores MCP para geração de imagens  
- Seção abrangente sobre uso do Claude no VSCode  
- Adição de configurações e instruções para cliente terminal Cline  
- Atualização da seção de clientes MCP para incluir todas as opções populares  
- Aprimoramento dos exemplos de contribuição com amostras de código mais precisas  

### Tópicos Avançados (05-AdvancedTopics/)  
- Organização de todas as pastas de tópicos especializados com nomenclatura consistente  
- Inclusão de materiais e exemplos de engenharia de contexto  
- Inclusão de documentação de integração do agente Foundry  
- Aprimoramento da documentação de integração de segurança Entra ID  

## 11 de junho de 2025

### Criação Inicial  
- Lançamento da primeira versão do currículo MCP para iniciantes  
- Estrutura básica criada para as 10 principais seções  
- Implementação do Mapa Visual do Currículo para navegação  
- Inclusão dos primeiros projetos de exemplo em múltiplas linguagens de programação  

### Iniciando (03-GettingStarted/)  
- Criação dos primeiros exemplos de implementação de servidor  
- Orientação para desenvolvimento de clientes  
- Instruções de integração de cliente LLM incluídas  
- Documentação de integração no VS Code adicionada  
- Implementação de exemplos de servidor Server-Sent Events (SSE)  

### Conceitos Fundamentais (01-CoreConcepts/)  
- Inclusão de explicação detalhada da arquitetura cliente-servidor  
- Criação de documentação sobre componentes-chave do protocolo  
- Documentação dos padrões de mensagens no MCP  

## 23 de maio de 2025

### Estrutura do Repositório  
- Inicialização do repositório com estrutura de pastas básica  
- Criação de arquivos README para cada seção principal  
- Configuração da infraestrutura de tradução  
- Adição de ativos de imagem e diagramas  

### Documentação  
- Criação inicial do README.md com visão geral do currículo  
- Inclusão dos arquivos CODE_OF_CONDUCT.md e SECURITY.md  
- Configuração do SUPPORT.md com orientações para obter ajuda  
- Criação da estrutura preliminar do guia de estudos  

## 15 de abril de 2025

### Planejamento e Estrutura  
- Planejamento inicial para o currículo MCP para iniciantes  
- Definição de objetivos de aprendizagem e público-alvo  
- Esboço da estrutura do currículo em 10 seções  
- Desenvolvimento do framework conceitual para exemplos e estudos de caso  
- Criação dos primeiros protótipos de exemplos para conceitos-chave  

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autoritativa. Para informações críticas, recomenda-se tradução profissional realizada por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->