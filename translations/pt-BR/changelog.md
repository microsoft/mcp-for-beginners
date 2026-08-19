# Registro de Alterações: Currículo MCP para Iniciantes

Este documento serve como registro de todas as mudanças significativas feitas no currículo do Model Context Protocol (MCP) para iniciantes. As mudanças são documentadas em ordem cronológica reversa (mais recentes primeiro).

## 29 de julho de 2026

### Novo Módulo 08 Acompanhante: Sidecars de Confiabilidade e Retentativas Seguras

Adicionada uma aula acompanhante independente de fornecedor para ferramentas MCP que criam efeitos no mundo real,
alinhada com a especificação final `2026-07-28`.

- **Novo**: A [aula acompanhante de sidecar de confiabilidade][reliability-sidecar]
  usa uma história de ticket de suporte, dois diagramas Mermaid e um fluxo de decisão de retentativa
  para explicar chaves de operação estável, admissão duplicada atômica,
  reconciliação, evidências e o limite da extensão Tarefas.
- **Novo**: Um exercício de injeção de falhas em Python e SQLite da biblioteca padrão
  usa lojas separadas de operação e ticket para demonstrar uma resposta perdida
  após o commit de um efeito externo. Seis testes determinísticos cobrem duplicação
  ingênua, recuperação protegida de reinício, conflitos de payload, resultados em cache,
  reivindicações ativas e admissão duplicada concorrente.
- **Atualizado**: O Módulo 08 agora linka a aula acompanhante, identifica o
  modelo final de requisição sem estado `2026-07-28`, distingue a observabilidade OpenTelemetry
  do recurso de log MCP obsoleto e limita seu
  exemplo genérico de retentativa a operações somente leitura.
- **Opcional**: A aula mapeia seus conceitos portáteis para uma implementação comunitária tagueada
  sem tornar o serviço hospedado ou uma chamada de rede parte do
  exercício.

[reliability-sidecar]: ./08-BestPractices/reliability-sidecars/README.md

## 2 de julho de 2026

### Nova Aula: Release Candidate da Especificação MCP 2026-07-28

Adicionada cobertura do próximo release candidate da especificação MCP `2026-07-28` (anunciado em 21 de maio de 2026; lançamento final previsto para 28 de julho de 2026), resumido a partir do [post oficial de anúncio no blog](https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/). A base do currículo permanece sendo a **Especificação MCP 2025-11-25** até a nova versão ser lançada, portanto, isso é apresentado como uma orientação prospectiva ao invés de uma reescrita das aulas existentes.

- **Novo**: [01-CoreConcepts/mcp-2026-07-28-release-candidate.md](./01-CoreConcepts/mcp-2026-07-28-release-candidate.md) — uma aula completa cobrindo o núcleo do protocolo sem estado (remoção do handshake `initialize` e `Mcp-Session-Id`), os novos cabeçalhos de roteamento `Mcp-Method`/`Mcp-Name`, metadados de cache `ttlMs`/`cacheScope`, W3C Trace Context em `_meta`, o framework formal de Extensões (Apps MCP e a nova extensão Tarefas), seis SEPs de endurecimento de autorização, a depreciação de Roots/Sampling/Logging, e o avanço para JSON Schema 2020-12 completo para esquemas de ferramentas.
- **Atualizado** com chamadas prospectivas vinculando à nova aula:
  - [01-CoreConcepts/README.md](./01-CoreConcepts/README.md): nota sobre versão do protocolo, seções Sampling/Roots/Logging/Tarefas, e "O que vem a seguir"
  - [02-Security/README.md](./02-Security/README.md): chamada de endurecimento da autorização
  - [03-GettingStarted/06-http-streaming/README.md](./03-GettingStarted/06-http-streaming/README.md): chamada sobre transporte sem estado
  - [03-GettingStarted/14-sampling/README.md](./03-GettingStarted/14-sampling/README.md): chamada sobre depreciação do Sampling
  - [05-AdvancedTopics/mcp-protocol-features/README.md](./05-AdvancedTopics/mcp-protocol-features/README.md): chamada sobre depreciação de Logging e extensão Tarefas
  - [05-AdvancedTopics/mcp-transport/README.md](./05-AdvancedTopics/mcp-transport/README.md): chamada sobre transporte sem estado/roteamento de sessão
  - [README.md](./README.md): nota "Olhando para frente" na seção de especificação e uma nova entrada `1.1` na tabela de módulos do currículo
  - [study_guide.md](./study_guide.md): bala prospectiva sob a visão geral dos Conceitos Centrais e uma nota datada de adendo
  - [03-GettingStarted/11-simple-auth/README.md](./03-GettingStarted/11-simple-auth/README.md): chamada sobre o mapa de transporte `mcp-session-id` antes do modelo de requisição sem estado
  - [05-AdvancedTopics/README.md](./05-AdvancedTopics/README.md): chamada de visão geral do módulo sobre depreciações de Contextos Raiz/Sampling e a extensão Tarefas
  - [05-AdvancedTopics/mcp-security/README.md](./05-AdvancedTopics/mcp-security/README.md): chamada de endurecimento da autorização

## 24 de junho de 2026

### Nova Aula: Usando MCP no aplicativo Copilot

- [Seção Ferramentas](./12-tooling/README.md) Seção de ferramentas adicionada.
- [MCP no aplicativo Copilot](./12-tooling/01-copilot-app/README.md)

## 16 de junho de 2026

### Alinhamento da Especificação MCP e Validação das Amostras

Validado o currículo contra a atual **Especificação MCP 2025-11-25** e os SDKs oficiais mais recentes, então corrigidas referências desatualizadas da especificação e confirmadas que as amostras principais ainda compilam e executam.

#### Correções da Versão da Especificação (2025-06-18 / 2025-03-26 → 2025-11-25)

Atualizado o conteúdo em inglês onde ainda afirmava que uma revisão mais antiga da especificação era o padrão *atual/mais recente*, e redirecionados os links para os caminhos canônicos da especificação em `modelcontextprotocol.io`:
- **05-AdvancedTopics/mcp-security/README.md**: Atualizado o banner "Padrão Atual", introdução, título dos princípios centrais de segurança, título dos requisitos obrigatórios, seção Microsoft Entra ID, links de Referências & Recursos, e nota final de segurança (8 referências) para 2025-11-25
- **05-AdvancedTopics/mcp-transport/README.md**: Atualizado o link para Recursos Adicionais e o banner "Padrão Atual" para 2025-11-25
- **05-AdvancedTopics/mcp-realtimesearch/README.md**: Substituído o link obsoleto `2025-03-26` para segurança e confiança pela página atual de melhores práticas de segurança 2025-11-25
- **03-GettingStarted/14-sampling/README.md**: Atualizado o link oficial de documentação de sampling para 2025-11-25
- **03-GettingStarted/05-stdio-server/README.md**: Atualizada a referência no presente tempo "especificação MCP atual" e o link de Recursos Adicionais para 2025-11-25 (notas históricas sobre depreciação do SSE mantidas para precisão)

#### Validação das Amostras Contra os SDKs Atuais

- **TypeScript (03-GettingStarted/01-first-server/solution/typescript)**: `npm install` resolveu `@modelcontextprotocol/sdk@1.29.0`; `tsc --noEmit` passou sem erros de tipo — APIs existentes `McpServer`/`StdioServerTransport` permanecem válidas
- **Python (03-GettingStarted/01-first-server/solution/python)**: Validado em `.venv` isolado com `mcp[cli]` (1.27.2); `py_compile` passou e `FastMCP.list_tools()` retornou corretamente as ferramentas `add` e `subtract`
- Confirmado que todas as faixas de versão de `@modelcontextprotocol/sdk` nas amostras (`>=1.26.0` / `^1.26.0` / `^1.27.0`) resolvem limpo para a versão atual `1.29.0` sem quebras de API

#### Alinhamento de Travamento de Dependências (fechando lacunas de versão)

Atualizados os pins de SDK desatualizados para que cada amostra acompanhe o lançamento atual do MCP, seguindo a convenção de repositório:
- **03-GettingStarted/05-stdio-server/solution/typescript/package.json**: Atualizado `@modelcontextprotocol/sdk` de `^1.8.0` para `>=1.26.0` e a descrição desatualizada do pacote `"updated for MCP 2025-06-18"` para `"aligned with MCP Specification 2025-11-25"`
- **10-StreamliningAIWorkflows.../lab3/code/weather_mcp/pyproject.toml** e **lab4/code/github_mcp_server/pyproject.toml**: Atualizado o pin exato `mcp==1.23.0` para `mcp>=1.26.0`; regenerados os arquivos `uv.lock` (`uv lock`) para que os lockfiles resolvam para o atual `mcp 1.27.2` e permaneçam sincronizados com os manifests

#### Análise de Lacunas no Currículo — Cobertura das Funcionalidades da Especificação Mais Recente

Verificado que o currículo cobre todas as primitivas introduzidas/ampliadas no MCP 2025-11-25, portanto não restam lacunas de conteúdo:
- **Sampling**: Aula 03-GettingStarted/14-sampling mais 05-AdvancedTopics/mcp-sampling
- **Elicitação (incluindo modo URL)**: Documentado em 01-CoreConcepts e 05-AdvancedTopics/mcp-protocol-features
- **Roots**: Documentado em 00-Introduction, 01-CoreConcepts e 05-AdvancedTopics/mcp-root-contexts
- **Tarefas (experimental, operações longas)**: Documentado em 01-CoreConcepts e 05-AdvancedTopics/mcp-protocol-features
- **Anotações de Ferramentas** (`readOnlyHint` / `destructiveHint`): Documentado em 01-CoreConcepts e 05-AdvancedTopics/mcp-protocol-features

### Endurecimento de Segurança & Remediação de Vulnerabilidades em Dependências

Realizado um passe completo de segurança em todos os manifests de dependências e no código-fonte das amostras, então remediados todos os avisos npm reportados e uma falha em nível de código. Após a remediação, `npm audit` reporta **0 vulnerabilidades** em todos os diretórios auditados.

#### Vulnerabilidades em Dependências npm (transitivas) — Corrigidas

Auditados todos os 15 arquivos `package-lock.json` comprometidos. Vulnerabilidades eram limitadas a dependências transitivas puxadas pela ferramenta de desenvolvimento MCP Inspector, cliente OpenAI, e SDK MCP; todas agora resolvidas sem quebrar as amostras:
- **10-StreamliningAIWorkflows.../lab4/code/github_mcp_server/inspector** e **lab3/code/weather_mcp/inspector**: Atualizado `@modelcontextprotocol/inspector` (`0.16.6` / `0.14.1` → `0.22.0`), o que eliminou os avisos empacotados em `ajv`, `brace-expansion`, `diff`, `path-to-regexp` e `ws`. Adicionado um `overrides` do npm forçando o patched `shell-quote@1.8.4` para eliminar o aviso crítico restante carregado pelo `concurrently`; regenerados ambos os lockfiles (agora 0 vulnerabilidades)
- **03-GettingStarted/samples/typescript**: `npm audit fix` atualizou a dependência transitiva `qs` (moderada) para uma release patch
- **03-GettingStarted/samples/javascript**: `npm audit fix` atualizou a dependência transitiva `hono` (moderada) para uma release patch
- **03-GettingStarted/03-llm-client/solution/typescript**: `npm audit fix` atualizou a dependência transitiva `form-data` (alta) para uma release patch
- **03-GettingStarted/11-simple-auth/solution/typescript**: Gerado o `package-lock.json` ausente para que o projeto seja reprodutível e auditável (0 vulnerabilidades)

#### Correção de Segurança em Nível de Código (OWASP A03: Injeção)

- **10-StreamliningAIWorkflows.../lab4/code/github_mcp_server/src/server.py**: Removido `shell=True` da ferramenta `open_in_vscode`. O anterior `subprocess.run(["start", "", vscode_path, folder_path], shell=True)` permitia que metacaracteres shell em um caminho de pasta fossem interpretados pelo `cmd.exe` (vetor de injeção de comando). Agora inicia diretamente o `Code.exe` resolvido com a pasta como argumento — sem shell —, que é funcionalmente equivalente e seguro

#### Auditoria de Dependências Python

- Auditado cada conjunto de requirements Python com `pip-audit`. `05-AdvancedTopics` e `03-GettingStarted/samples/python` reportaram **nenhuma vulnerabilidade conhecida** (suas faixas de `mcp` / `httpx` / `pydantic` / `python-dotenv` resolvem para releases patch atuais)
- **09-CaseStudy/docs-mcp/solution/python/requirements.txt**: `pip-audit` sinalizou a dependência transitiva **`werkzeug` 3.1.1** com três avisos `safe_join` de nomes de dispositivos Windows DoS — `CVE-2025-66221`, `CVE-2026-21860`, e `CVE-2026-27199` (todos corrigidos na 3.1.6). Adicionado um pin de segurança explícito `werkzeug>=3.1.6` para que a release corrigida seja resolvida; verificado que a restrição resolve limpo na stack `chainlit` / `mcp` / `semantic-kernel`

### Rebranding do Nome do Produto

Atualizado todo o conteúdo do currículo para refletir o rebranding dos produtos da Microsoft:

#### Azure AI Foundry → Microsoft Foundry
- **SUPPORT.md**: Atualizado link da comunidade no Discord

- **AGENTS.md**: Referência do servidor Discord atualizada
- **README.md**: Referências do ecossistema tecnológico atualizadas
- **study_guide.md**: Referências do estudo de caso atualizadas
- **05-AdvancedTopics/README.md**: Título e descrição do Módulo 5.13 atualizados
- **05-AdvancedTopics/mcp-integration/README.md**: Cabeçalho da seção e descrição atualizados
- **05-AdvancedTopics/mcp-foundry-agent-integration/README.md**: Atualização completa do título e conteúdo do módulo
- **05-AdvancedTopics/mcp-security-entra/README.md**: Link de referência cruzada atualizado
- **07-LessonsfromEarlyAdoption/README.md**: Referências do estudo de caso atualizadas
- **07-LessonsfromEarlyAdoption/microsoft-mcp-servers.md**: Cabeçalho da Seção 9, badges e capacidades atualizados
- **08-BestPractices/README.md**: Link da comunidade Discord atualizado
- **09-CaseStudy/docs-mcp/solution/scenario3/README.md**: Referência ao canal Discord atualizada
- **09-CaseStudy/docs-mcp/solution/python/README.md**: Referência ao deployment do modelo atualizada
- **11-MCPServerHandsOnLabs/00-Introduction/README.md**: Tabela de Serviços de IA atualizada
- **11-MCPServerHandsOnLabs/03-Setup/README.md**: Referências de recursos atualizadas

#### AI Toolkit / AITK → Microsoft Foundry Toolkit Extension para VS Code
- **README.md**: Referências principais do currículo atualizadas
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/README.md**: Título do módulo, visão geral e todos os cabeçalhos de módulo atualizados
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab1/README.md**: Título, objetivos de aprendizagem, instruções de configuração e recursos atualizados
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab2/README.md**: Título, objetivos de aprendizagem, tabela de hosts MCP e referências cruzadas atualizadas
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/README.md**: Título, badges, pré-requisitos e recursos atualizados
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/README.md**: Referências ao Agent Builder e link de feedback atualizados
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/README.md**: Pré-requisitos e referências de extensão atualizados

---

## 11 de abril de 2026

### Nova Lição, Correções na Documentação e Atualizações de Dependências

#### Novo Conteúdo do Currículo Adicionado

**Módulo 05 - Tópicos Avançados**
- **Lição 5.17: Raciocínio Multi-Agente Adversarial com MCP** (`05-AdvancedTopics/mcp-adversarial-agents/README.md`): Novo guia abrangente cobrindo o padrão de debate adversarial para sistemas multiagentes
  - Diagrama de arquitetura Mermaid: dois agentes → servidor MCP compartilhado → transcrição do debate → juiz → veredito
  - Servidor de ferramenta MCP compartilhado (`web_search` + `run_python`) implementado em Python e TypeScript
  - Prompts de sistema opostos (A FAVOR / CONTRA / Juiz) com requisitos explícitos de uso de ferramenta
  - Orquestrador do debate em Python, TypeScript e C# gerenciando rodadas e roteando argumentos
  - Ligação MCP `ClientSession` para o orquestrador às chamadas reais das ferramentas
  - Tabela de casos de uso (detecção de alucinação, modelagem de ameaças, revisão de design de API, verificação factual, seleção técnica)
  - Considerações de segurança: execução sandboxed, validação de chamadas de ferramenta, limitação de taxa, registro de auditoria
  - Exercício estruturado com três cenários práticos (revisão de código, decisão arquitetural, moderação de conteúdo)

#### Correções na Documentação

**Módulo 03 - Iniciando**
- **05-stdio-server/README.md**: Corrigido exemplo incompleto de servidor stdio TypeScript — adicionada instância de transporte faltante (`new StdioServerTransport()`) e chamada `server.connect(transport)` para coincidir com exemplos Python e .NET na mesma seção
- **14-sampling/README.md**: Corrigido erro de digitação — corrigido `"Sampling is an davanced features"` → `"Sampling is an advanced feature"`

#### Atualizações do Currículo

**README.md principal**
- Adicionado item 5.17 (Raciocínio Multi-Agente Adversarial com MCP) na tabela do currículo com link direto para a nova lição

**05-AdvancedTopics/README.md**
- Adicionada linha da Lição 5.17 na tabela de lições

**study_guide.md**
- Adicionado tópico Raciocínio Multi-Agente Adversarial no mapa mental e descrição em prosa dos Tópicos Avançados

#### Correções de Código e Segurança

**Módulo 05 - Agentes Adversariais (`mcp-adversarial-agents`)**
- **Correção de segurança — injeção de comando**: Substituída interpolação shell `execSync` por `execFile` + `promisify` na ferramenta TypeScript `run_python`, eliminando superfície de injeção de comando (código controlado pelo LLM agora é passado como elemento literal argv sem envolvimento de shell)
- **Ligação do loop da ferramenta MCP**: Atualizado orquestrador Python para usar cliente `AsyncAnthropic` (substituindo `Anthropic` síncrono bloqueante), passar `ClientSession` vivo diretamente para cada turno de agente, obter definições de ferramenta via `session.list_tools()` cada turno, e despachar blocos `tool_use` via `session.call_tool()` em loop até o modelo emitir resposta final em texto

#### Atualizações de Dependências

- Atualizado `hono` para 4.12.12 em múltiplos pacotes (03-GettingStarted, 04-PracticalImplementation, 10-StreamliningAIWorkflows)
- Atualizado `@hono/node-server` de 1.19.11 para 1.19.13 em pacotes TypeScript
- Atualizado `cryptography` de 46.0.5 para 46.0.7 em pacotes Python (labs 3 e 4 de 10-StreamliningAIWorkflows)
- Atualizado `lodash` de 4.17.23 para 4.18.1 em inspetor de 10-StreamliningAIWorkflows

#### Traduções

- Sincronizadas traduções para 48+ idiomas com as últimas alterações da fonte (atualização i18n)

---

## 5 de fevereiro de 2026

### Melhorias na Validação e Navegação de Repositórios

#### Novo Conteúdo do Currículo Adicionado

**Módulo 03 - Iniciando**
- **12-mcp-hosts/README.md**: Novo guia abrangente para configuração de hosts MCP
  - Exemplos de configuração para Claude Desktop, VS Code, Cursor, Cline, Windsurf
  - Modelos de configuração JSON para todos os hosts principais
  - Tabela comparativa dos tipos de transporte (stdio, SSE/HTTP, WebSocket)
  - Solução de problemas comuns de conexão
  - Melhores práticas de segurança para configuração de hosts

- **13-mcp-inspector/README.md**: Novo guia de depuração para MCP Inspector
  - Métodos de instalação (npx, npm global, a partir da fonte)
  - Conexão a servidores via stdio e HTTP/SSE
  - Ferramentas de teste, recursos e fluxos de trabalho de prompts
  - Integração com VS Code e MCP Inspector
  - Cenários comuns de depuração com soluções

**Módulo 04 - Implementação Prática**
- **pagination/README.md**: Novo guia de implementação de paginação
  - Padrões de paginação baseados em cursor em Python, TypeScript, Java
  - Manipulação de paginação no cliente
  - Estratégias de design de cursor (opaco vs estruturado)
  - Recomendações de otimização de desempenho

**Módulo 05 - Tópicos Avançados**
- **mcp-protocol-features/README.md**: Exploração das novas funcionalidades do protocolo
  - Implementação de notificações de progresso
  - Padrões de cancelamento de requisição
  - Modelos de recursos com padrões de URI
  - Gerenciamento do ciclo de vida do servidor
  - Controle do nível de logs
  - Padrões de tratamento de erros com códigos JSON-RPC

#### Correções de Navegação (24+ arquivos atualizados)

**READMEs dos Módulos Principais**
 Agora linkam para a primeira lição E para o próximo módulo

**Subarquivos de Segurança 02-Security**
- Todos os 5 documentos suplementares de segurança agora possuem navegação "O que vem a seguir":

**Arquivos de Estudo de Caso 09-CaseStudy**
- Todos os arquivos de estudo de caso agora possuem navegação sequencial:

**Laboratórios 10-StreamliningAI**
Adicionada seção O Que Vem a Seguir na visão geral do Módulo 10 e no Módulo 11

#### Correções de Código e Conteúdo

**Atualizações do SDK e Dependências**
Corrigida versão vazia do openai para `^4.95.0`
SDK atualizado de `^1.8.0` para `>=1.26.0`
Versões do mcp atualizadas para `>=1.26.0`

**Correções de Código**
Corrigido modelo inválido `gpt-4o-mini` para `gpt-4.1-mini`

**Correções de Conteúdo**
Corrigido link quebrado `READMEmd` → `README.md`, corrigido cabeçalho do currículo `Module 1-3` → `Module 0-3`, corrigido caminho sensível a maiúsculas
Removido conteúdo duplicado corrompido do Estudo de Caso 5

**Melhorias no Guia para Iniciantes**
Adicionada introdução apropriada, objetivos de aprendizagem e pré-requisitos para iniciantes

#### Atualizações do Currículo

**README.md principal**
- Adicionados itens 3.12 (Hosts MCP), 3.13 (MCP Inspector), 4.1 (Paginação), 5.16 (Recursos do Protocolo) na tabela do currículo

**READMEs dos Módulos**
Adicionadas lições 12 e 13 à lista de lições
Adicionada seção Guias Práticos com link de paginação
Adicionadas lições 5.15 (Transporte Customizado) e 5.16 (Recursos do Protocolo)

**study_guide.md**
- Mapa mental com todos os tópicos novos atualizados: Configuração de Hosts MCP, MCP Inspector, Estratégias de Paginação, Exploração Detalhada de Recursos do Protocolo

## 28 de janeiro de 2026

### Revisão de Conformidade da Especificação MCP 2025-11-25

#### Aprimoramento dos Conceitos Principais (01-CoreConcepts/)
- **Novo Primitivo Cliente - Roots**: Adicionada documentação abrangente sobre o primitivo cliente Roots, permitindo que servidores compreendam limites do sistema de arquivos e permissões de acesso
- **Anotações de Ferramentas**: Adicionada documentação sobre anotações comportamentais de ferramentas (`readOnlyHint`, `destructiveHint`) para melhores decisões de execução de ferramentas
- **Chamadas de Ferramentas em Sampling**: Documentação de Sampling atualizada para incluir parâmetros `tools` e `toolChoice` para invocação de ferramentas guiadas pelo modelo durante solicitações de sampling
- **Elicitação por Modo URL**: Adicionada documentação sobre elicitação baseada em URL para interações externas iniciadas pelo servidor na web
- **Tarefas (Experimental)**: Nova seção documentando o recurso experimental de Tarefas para wrappers de execução durável e recuperação de resultados adiados
- **Suporte a Ícones**: Observado que ferramentas, recursos, templates de recurso e prompts podem agora incluir ícones como metadados adicionais

#### Atualizações na Documentação
- **README.md**: Adicionada referência à versão da Especificação MCP 2025-11-25 e explicação sobre versionamento baseado em datas
- **study_guide.md**: Mapa do currículo atualizado para incluir Tarefas e Anotações de Ferramentas na seção de Conceitos Principais; marca temporal do documento atualizada

#### Verificação de Conformidade com a Especificação
- **Versão do Protocolo**: Verificado que toda documentação referencia a Especificação MCP 2025-11-25 atual
- **Alinhamento Arquitetural**: Confirmada exatidão da arquitetura em duas camadas (Camada de Dados + Camada de Transporte)
- **Documentação dos Primitivos**: Validada documentação dos primitivos de servidor (Recursos, Prompts, Ferramentas) e primitivos de cliente (Sampling, Elicitação, Logs, Roots)
- **Mecanismos de Transporte**: Verificada precisão da documentação de transporte STDIO e HTTP Streamable
- **Orientações de Segurança**: Confirmada conformidade com a documentação atual das Melhores Práticas de Segurança MCP

#### Principais Recursos MCP 2025-11-25 Documentados
- **Descoberta OpenID Connect**: Descoberta do servidor de autenticação via OIDC
- **Documentos de Metadados de Client ID OAuth**: Mecanismo recomendado para registro de clientes
- **JSON Schema 2020-12**: Dialeto padrão para definições de schema MCP
- **Sistema de Níveis do SDK**: Requisitos formalizados para suporte e manutenção de recursos do SDK
- **Estrutura de Governança**: Formalização de Grupos de Trabalho e Grupos de Interesse na governança MCP

### Grande Atualização da Documentação de Segurança (02-Security/)

#### Integração com o Workshop MCP Security Summit (Sherpa)
- **Novo Recurso de Treinamento Prático**: Adicionada integração abrangente com o [MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/) em toda documentação de segurança
- **Cobertura da Rota da Expedição**: Documentado o progresso completo de acampamento a acampamento do Campo Base ao Cume
- **Alinhamento com OWASP**: Todas as orientações de segurança agora mapeadas para os riscos do OWASP MCP Azure Security Guide

#### Integração com OWASP MCP Top 10
- **Nova Seção**: Adicionada tabela de Riscos de Segurança OWASP MCP Top 10 com mitigações Azure ao README principal de Segurança
- **Documentação Baseada em Risco**: Atualizado arquivo mcp-security-controls-2025.md com referências aos riscos OWASP MCP para cada domínio de segurança
- **Arquitetura de Referência**: Linkada arquitetura de referência e padrões de implementação do OWASP MCP Azure Security Guide

#### Arquivos de Segurança Atualizados
- **README.md**: Adicionado resumo do Workshop Sherpa, tabela da rota da expedição, resumo dos riscos OWASP MCP Top 10 e seção de treinamento prático
- **mcp-security-controls-2025.md**: Cabeçalho atualizado para fevereiro de 2026, adicionadas referências aos riscos OWASP (MCP01-MCP08), corrigida inconsistência de versão da especificação
- **mcp-security-best-practices-2025.md**: Adicionada seção de recursos Sherpa e OWASP, timestamp atualizado
- **mcp-best-practices.md**: Adicionada seção de treinamento prático com links Sherpa e OWASP
- **azure-content-safety-implementation.md**: Adicionada referência OWASP MCP06, alinhamento com Sherpa Camp 3 e seção de recursos adicionais

#### Novos Links de Recursos Adicionados
- [MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/)

- [Guia de Segurança OWASP MCP Azure](https://microsoft.github.io/mcp-azure-security-guide/)
- [OWASP MCP Top 10](https://owasp.org/www-project-mcp-top-10/)
- Páginas individuais de risco OWASP MCP (MCP01-MCP10)

### Alinhamento da Especificação MCP para Todo o Currículo 2025-11-25

#### Módulo 03 - Introdução
- **Documentação do SDK**: Adicionado SDK Go à lista oficial de SDKs; atualizadas todas as referências de SDK para alinhar com a Especificação MCP 2025-11-25
- **Esclarecimento de Transporte**: Atualizadas descrições de transporte STDIO e HTTP Streaming com referências explícitas à especificação

#### Módulo 04 - Implementação Prática
- **Atualizações do SDK**: Adicionado SDK Go; lista de SDK atualizada com referência à versão da especificação
- **Especificação de Autorização**: Atualizado link da especificação MCP de Autorização para a versão atual 2025-11-25

#### Módulo 05 - Tópicos Avançados
- **Novos Recursos**: Adicionada nota sobre novas funcionalidades da Especificação MCP 2025-11-25 (Tarefas, Anotações de Ferramentas, Elicitação de Modo URL, Raízes)
- **Recursos de Segurança**: Adicionados links para OWASP MCP Top 10 e workshop Sherpa nas referências adicionais

#### Módulo 06 - Contribuições da Comunidade
- **Lista de SDKs**: Adicionados SDKs Swift e Rust; link da especificação atualizado para 2025-11-25
- **Referência da Especificação**: Link da Especificação MCP atualizado para URL direto da especificação

#### Módulo 07 - Lições da Adoção Inicial
- **Atualizações de Recursos**: Adicionado link da Especificação MCP 2025-11-25 e OWASP MCP Top 10 aos recursos adicionais

#### Módulo 08 - Melhores Práticas
- **Versão da Especificação**: Referência da Especificação MCP atualizada para 2025-11-25
- **Recursos de Segurança**: Adicionados OWASP MCP Top 10 e workshop Sherpa às referências adicionais

#### Módulo 10 - Otimização de Fluxos de Trabalho de IA
- **Atualização do Badge**: Alterado badge da versão MCP de versão do SDK (1.9.3) para versão da especificação (2025-11-25)
- **Links de Recursos**: Link da Especificação MCP atualizado; adicionado OWASP MCP Top 10

#### Módulo 11 - Laboratórios Práticos do MCP Server
- **Referência da Especificação**: Link da Especificação MCP atualizado para versão 2025-11-25
- **Recursos de Segurança**: Adicionado OWASP MCP Top 10 aos recursos oficiais

## 18 de dezembro de 2025

### Atualização da Documentação de Segurança - Especificação MCP 2025-11-25

#### Melhores Práticas de Segurança MCP (02-Security/mcp-best-practices.md) - Atualização da Versão da Especificação
- **Atualização da Versão do Protocolo**: Atualizado para referenciar a última Especificação MCP 2025-11-25 (lançada em 25 de novembro de 2025)
  - Atualizadas todas as referências à versão da especificação de 2025-06-18 para 2025-11-25
  - Atualizadas referências de datas do documento de 18 de agosto de 2025 para 18 de dezembro de 2025
  - Verificados todos os URLs da especificação apontando para a documentação atual
- **Validação de Conteúdo**: Validação abrangente das melhores práticas de segurança contra os padrões mais recentes
  - **Soluções de Segurança Microsoft**: Terminologia e links verificados para Prompt Shields (anteriormente "detecção de risco de jailbreak"), Azure Content Safety, Microsoft Entra ID e Azure Key Vault
  - **Segurança OAuth 2.1**: Confirmada conformidade com as melhores práticas de segurança OAuth mais recentes
  - **Padrões OWASP**: Validada atualidade das referências ao OWASP Top 10 para LLMs
  - **Serviços Azure**: Verificados todos os links da documentação Microsoft Azure e melhores práticas
- **Alinhamento de Padrões**: Todos os padrões de segurança referenciados confirmados como atuais
  - NIST AI Risk Management Framework
  - ISO 27001:2022
  - Melhores Práticas de Segurança OAuth 2.1
  - Frameworks de segurança e conformidade Azure
- **Recursos de Implementação**: Validada a integridade de todos os links e recursos de guias de implementação
  - Padrões de autenticação do Azure API Management
  - Guias de integração Microsoft Entra ID
  - Gerenciamento de segredos do Azure Key Vault
  - Pipelines DevSecOps e soluções de monitoramento

### Garantia de Qualidade da Documentação
- **Conformidade com a Especificação**: Garantia de que todos os requisitos obrigatórios de segurança MCP (MUST/MUST NOT) estejam alinhados com a especificação mais recente
- **Atualização de Recursos**: Verificação de todos os links externos para documentação Microsoft, padrões de segurança e guias de implementação
- **Cobertura das Melhores Práticas**: Confirmação da cobertura abrangente de autenticação, autorização, ameaças específicas de IA, segurança da cadeia de suprimentos e padrões empresariais

## 6 de outubro de 2025

### Expansão da Seção de Introdução – Uso Avançado do Servidor & Autenticação Simples

#### Uso Avançado do Servidor (03-GettingStarted/10-advanced)
- **Novo Capítulo Adicionado**: Guia completo sobre uso avançado do servidor MCP, cobrindo arquiteturas de servidor regulares e de baixo nível.
  - **Servidor Regular vs. Baixo Nível**: Comparação detalhada e exemplos de código em Python e TypeScript para ambas as abordagens.
  - **Design Baseado em Handlers**: Explicação da gestão baseada em handlers para ferramentas/recursos/prompt para implementações de servidor escaláveis e flexíveis.
  - **Padrões Práticos**: Cenários reais onde padrões de servidor de baixo nível são benéficos para recursos avançados e arquitetura.

#### Autenticação Simples (03-GettingStarted/11-simple-auth)
- **Novo Capítulo Adicionado**: Guia passo a passo para implementar autenticação simples em servidores MCP.
  - **Conceitos de Autorização**: Explicação clara de autenticação versus autorização, e manejo de credenciais.
  - **Implementação de Autenticação Básica**: Padrões de autenticação via middleware em Python (Starlette) e TypeScript (Express), com exemplos de código.
  - **Progressão para Segurança Avançada**: Orientação para iniciar com autenticação simples e avançar para OAuth 2.1 e RBAC, com referências a módulos avançados de segurança.

Essas adições fornecem orientações práticas e práticas para construir implementações de servidor MCP mais robustas, seguras e flexíveis, unindo conceitos fundamentais a padrões avançados de produção.

## 29 de setembro de 2025

### Laboratórios de Integração de Banco de Dados MCP Server - Caminho de Aprendizagem Prático e Completo

#### 11-MCPServerHandsOnLabs - Novo Currículo Completo de Integração de Banco de Dados
- **Caminho Completo de 13 Laboratórios**: Adicionado currículo prático e abrangente para construir servidores MCP prontos para produção com integração ao banco de dados PostgreSQL
  - **Implementação no Mundo Real**: Caso de uso de análise Zava Retail demonstrando padrões de nível empresarial
  - **Progressão Estruturada de Aprendizado**:
    - **Laboratórios 00-03: Fundamentos** - Introdução, Arquitetura Central, Segurança & Multi-Tenancy, Configuração do Ambiente
    - **Laboratórios 04-06: Construindo o Servidor MCP** - Design e Esquema do Banco de Dados, Implementação do Servidor MCP, Desenvolvimento de Ferramentas  
    - **Laboratórios 07-09: Recursos Avançados** - Integração de Busca Semântica, Testes & Depuração, Integração com VS Code
    - **Laboratórios 10-12: Produção & Melhores Práticas** - Estratégias de Implantação, Monitoramento & Observabilidade, Melhores Práticas & Otimização
  - **Tecnologias Empresariais**: Framework FastMCP, PostgreSQL com pgvector, embeddings Azure OpenAI, Azure Container Apps, Application Insights
  - **Recursos Avançados**: Row Level Security (RLS), busca semântica, acesso a dados multitenant, embeddings vetoriais, monitoramento em tempo real

#### Padronização de Terminologia - Conversão de Módulo para Laboratório
- **Atualização Abrangente da Documentação**: Atualizados sistematicamente todos os arquivos README em 11-MCPServerHandsOnLabs para usar a terminologia "Laboratório" em vez de "Módulo"
  - **Cabeçalhos das Seções**: Atualizado "O Que Este Módulo Cobre" para "O Que Este Laboratório Cobre" em todos os 13 laboratórios
  - **Descrição do Conteúdo**: Alterado "Este módulo fornece..." para "Este laboratório fornece..." em toda a documentação
  - **Objetivos de Aprendizagem**: Atualizado "Ao final deste módulo..." para "Ao final deste laboratório..."
  - **Links de Navegação**: Convertidas todas as referências "Módulo XX:" para "Laboratório XX:" em referências cruzadas e navegação
  - **Rastreamento de Conclusão**: Atualizado "Após concluir este módulo..." para "Após concluir este laboratório..."
  - **Referências Técnicas Preservadas**: Mantidas referências a módulos Python em arquivos de configuração (ex., `"module": "mcp_server.main"`)

#### Melhoria no Guia de Estudo (study_guide.md)
- **Mapa Visual do Currículo**: Adicionada nova seção "11. Laboratórios de Integração de Banco de Dados" com visualização abrangente da estrutura dos laboratórios
- **Estrutura do Repositório**: Atualizado de dez para onze seções principais com descrição detalhada do 11-MCPServerHandsOnLabs
- **Orientação do Caminho de Aprendizado**: Melhoradas instruções de navegação para cobrir seções 00-11
- **Cobertura Tecnológica**: Adicionado detalhes de FastMCP, PostgreSQL e integração de serviços Azure
- **Resultados de Aprendizagem**: Enfatizado desenvolvimento de servidores prontos para produção, padrões de integração de banco de dados e segurança empresarial

#### Melhoria na Estrutura do README Principal
- **Terminologia Baseada em Laboratórios**: Atualizado README.md principal em 11-MCPServerHandsOnLabs para uso consistente da estrutura "Laboratório"
- **Organização do Caminho de Aprendizado**: Progressão clara de conceitos fundamentais até implementação avançada e implantação em produção
- **Foco no Mundo Real**: Ênfase em aprendizado prático com padrões e tecnologias de nível empresarial

### Melhorias na Qualidade e Consistência da Documentação
- **Ênfase no Aprendizado Prático**: Reforço da abordagem prática e baseada em laboratórios em toda a documentação
- **Foco em Padrões Empresariais**: Destaque para implementações prontas para produção e considerações de segurança empresarial
- **Integração Tecnológica**: Cobertura abrangente dos serviços Azure modernos e padrões de integração IA
- **Progressão de Aprendizado**: Caminho claro e estruturado desde conceitos básicos até implantação em produção

## 26 de setembro de 2025

### Melhoria em Estudos de Caso - Integração do Registro MCP GitHub

#### Estudos de Caso (09-CaseStudy/) - Foco no Desenvolvimento do Ecossistema
- **README.md**: Expansão significativa com estudo de caso abrangente do Registro MCP GitHub
  - **Estudo de Caso do Registro MCP GitHub**: Novo estudo detalhado examinando o lançamento do Registro MCP GitHub em setembro de 2025
    - **Análise do Problema**: Exame detalhado dos desafios fragmentados de descoberta e implantação de servidores MCP
    - **Arquitetura da Solução**: Abordagem centralizada de registro do GitHub com instalação de um clique no VS Code
    - **Impacto nos Negócios**: Melhorias mensuráveis na integração e produtividade dos desenvolvedores
    - **Valor Estratégico**: Foco na implantação modular de agentes e interoperabilidade entre ferramentas
    - **Desenvolvimento do Ecossistema**: Posicionamento como plataforma fundamental para integração agentic
  - **Estrutura Melhorada do Estudo de Caso**: Atualizados todos os sete estudos de caso com formatação consistente e descrições abrangentes
    - Azure AI Travel Agents: Ênfase em orquestração multi-agente
    - Integração Azure DevOps: Foco em automação de workflows
    - Recuperação de Documentação em Tempo Real: Implementação de cliente de console Python
    - Gerador de Plano de Estudo Interativo: Aplicação web conversacional Chainlit
    - Documentação In-Editor: Integração VS Code e GitHub Copilot
    - Azure API Management: Padrões de integração de APIs empresariais
    - Registro MCP GitHub: Desenvolvimento de ecossistema e plataforma comunitária
  - **Conclusão Abrangente**: Seção de conclusão reescrita destacando sete estudos de caso abrangendo múltiplas dimensões de implementação MCP
    - Integração Empresarial, Orquestração Multi-Agente, Produtividade de Desenvolvedores
    - Desenvolvimento do Ecossistema, Categorias de Aplicações Educacionais
    - Insights aprimorados em padrões arquitetônicos, estratégias de implementação e melhores práticas
    - Ênfase no MCP como protocolo maduro e pronto para produção

#### Atualizações no Guia de Estudo (study_guide.md)
- **Mapa Visual do Currículo**: Atualizado mindmap para incluir o Registro MCP GitHub na seção de Estudos de Caso
- **Descrição dos Estudos de Caso**: Aprimorada de descrições genéricas para detalhamento de sete estudos de caso abrangentes
- **Estrutura do Repositório**: Atualizada seção 10 para refletir cobertura completa de estudos de caso com detalhes específicos de implementação
- **Integração do Changelog**: Adicionada entrada de 26 de setembro de 2025 documentando inclusão do Registro MCP GitHub e melhorias nos estudos de caso
- **Atualizações de Datas**: Atualizado timestamp do rodapé para refletir a revisão mais recente (26 de setembro de 2025)

### Melhorias na Qualidade da Documentação
- **Aprimoramento da Consistência**: Padronização da formatação e estrutura dos estudos de caso em todos os sete exemplos
- **Cobertura Abrangente**: Estudos de caso agora abrangem cenários empresariais, produtividade de desenvolvedores e desenvolvimento do ecossistema
- **Posicionamento Estratégico**: Foco aprimorado no MCP como plataforma fundamental para implantação de sistemas agentic
- **Integração de Recursos**: Atualizados recursos adicionais para incluir link do Registro MCP GitHub

## 15 de setembro de 2025

### Expansão de Tópicos Avançados - Transportes Customizados & Engenharia de Contexto

#### Transportes Customizados MCP (05-AdvancedTopics/mcp-transport/) - Novo Guia Avançado de Implementação
- **README.md**: Guia completo de implementação para mecanismos customizados de transporte MCP
  - **Transporte Azure Event Grid**: Implementação abrangente de transporte serverless baseado em eventos
    - Exemplos em C#, TypeScript e Python com integração Azure Functions
    - Padrões de arquitetura orientada a eventos para soluções MCP escaláveis
    - Receptores webhook e manipulação de mensagens push
  - **Transporte Azure Event Hubs**: Implementação de transporte streaming de alta taxa de transferência
    - Capacidades de streaming em tempo real para cenários de baixa latência
    - Estratégias de particionamento e gerenciamento de checkpoints
    - Agrupamento de mensagens e otimização de desempenho
  - **Padrões de Integração Empresarial**: Exemplos arquitetônicos prontos para produção
    - Processamento distribuído MCP via múltiplas Azure Functions
    - Arquiteturas híbridas de transporte combinando múltiplos tipos de transporte
    - Durabilidade, confiabilidade e estratégias de tratamento de erros de mensagens
  - **Segurança & Monitoramento**: Integração Azure Key Vault e padrões de observabilidade
    - Autenticação por identidade gerenciada e princípio de menor privilégio
    - Telemetria Application Insights e monitoramento de desempenho
    - Circuit breakers e padrões de tolerância a falhas
  - **Frameworks de Teste**: Estratégias abrangentes de teste para transportes customizados
    - Testes unitários com doubles e frameworks de mocking
    - Testes de integração com Azure Test Containers
    - Considerações para testes de desempenho e carga

#### Engenharia de Contexto (05-AdvancedTopics/mcp-contextengineering/) - Disciplina Emergente de IA
- **README.md**: Exploração abrangente da engenharia de contexto como disciplina emergente
  - **Princípios Centrais**: Compartilhamento completo de contexto, consciência de decisão de ação e gerenciamento da janela de contexto

  - **Alinhamento do Protocolo MCP**: Como o design do MCP aborda os desafios da engenharia de contexto
    - Limitações da janela de contexto e estratégias de carregamento progressivo
    - Determinação de relevância e recuperação dinâmica de contexto
    - Manipulação multimodal de contexto e considerações de segurança
  - **Abordagens de Implementação**: Arquiteturas single-threaded vs. multi-agentes
    - Técnicas de fatiamento e priorização de contexto
    - Estratégias de carregamento progressivo e compressão de contexto
    - Abordagens de contexto em camadas e otimização de recuperação
  - **Estrutura de Medição**: Métricas emergentes para avaliação da efetividade do contexto
    - Eficiência de entrada, desempenho, qualidade e considerações de experiência do usuário
    - Abordagens experimentais para otimização do contexto
    - Análise de falhas e metodologias de melhoria

#### Atualizações de Navegação do Currículo (README.md)
- **Estrutura de Módulos Aprimorada**: Tabela do currículo atualizada para incluir novos tópicos avançados
  - Adicionadas entradas de Engenharia de Contexto (5.14) e Transporte Personalizado (5.15)
  - Formatação consistente e links de navegação em todos os módulos
  - Descrições atualizadas para refletir o escopo atual do conteúdo

### Melhorias na Estrutura de Diretórios
- **Padronização de Nomes**: Renomeado "mcp transport" para "mcp-transport" para consistência com outras pastas de tópicos avançados
- **Organização de Conteúdo**: Todas as pastas 05-AdvancedTopics agora seguem um padrão consistente de nomeação (mcp-[tópico])

### Melhorias na Qualidade da Documentação
- **Alinhamento à Especificação MCP**: Todo conteúdo novo referencia a Especificação MCP 2025-06-18 atual
- **Exemplos Multi-idioma**: Exemplos de código abrangentes em C#, TypeScript e Python
- **Foco Empresarial**: Padrões prontos para produção e integração com Azure cloud em todo o material
- **Documentação Visual**: Diagramas Mermaid para visualização de arquitetura e fluxos

## 18 de agosto de 2025

### Atualização Abrangente da Documentação - Padrões MCP 2025-06-18

#### Melhores Práticas de Segurança MCP (02-Security/) - Modernização Completa
- **MCP-SECURITY-BEST-PRACTICES-2025.md**: Reescrita completa alinhada à Especificação MCP 2025-06-18
  - **Requisitos Obrigatórios**: Adicionados requisitos EXIGIDOS/PROIBIDOS explícitos da especificação oficial com indicadores visuais claros
  - **12 Práticas Centrais de Segurança**: Reestruturado de lista de 15 itens para domínios abrangentes de segurança
    - Segurança de Token & Autenticação com integração de provedor externo de identidade
    - Gerenciamento de Sessão & Segurança de Transporte com requisitos criptográficos
    - Proteção Contra Ameaças Específicas de IA com integração Microsoft Prompt Shields
    - Controle de Acesso & Permissões com princípio do menor privilégio
    - Segurança & Monitoramento de Conteúdo com integração Azure Content Safety
    - Segurança da Cadeia de Suprimentos com verificação abrangente de componentes
    - Segurança OAuth & Prevenção de Confused Deputy com implementação PKCE
    - Resposta a Incidentes & Recuperação com capacidades automatizadas
    - Conformidade & Governança com alinhamento regulatório
    - Controles Avançados de Segurança com arquitetura zero trust
    - Integração ao Ecossistema de Segurança Microsoft com soluções abrangentes
    - Evolução Contínua da Segurança com práticas adaptativas
  - **Soluções de Segurança Microsoft**: Orientação aprimorada para integração com Prompt Shields, Azure Content Safety, Entra ID e GitHub Advanced Security
  - **Recursos de Implementação**: Links completos categorizados por Documentação Oficial MCP, Soluções Microsoft, Padrões de Segurança e Guias de Implementação

#### Controles Avançados de Segurança (02-Security/) - Implementação Empresarial
- **MCP-SECURITY-CONTROLS-2025.md**: Reformulação completa com framework de segurança empresarial
  - **9 Domínios Abrangentes de Segurança**: Expansão dos controles básicos para framework detalhado empresarial
    - Autenticação & Autorização Avançadas com integração Microsoft Entra ID
    - Segurança de Token & Controles Anti-Passthrough com validação abrangente
    - Controles de Segurança de Sessão com prevenção de sequestro
    - Controles de Segurança Específicos para IA com prevenção de injeção de prompt e envenenamento de ferramentas
    - Prevenção de Ataque Confused Deputy com segurança proxy OAuth
    - Segurança de Execução de Ferramentas com sandboxing e isolamento
    - Controles de Segurança da Cadeia de Suprimentos com verificação de dependências
    - Controles de Monitoramento & Detecção com integração SIEM
    - Resposta a Incidentes & Recuperação com capacidades automatizadas
  - **Exemplos de Implementação**: Adicionados blocos detalhados de configuração YAML e exemplos de código
  - **Integração com Soluções Microsoft**: Cobertura completa dos serviços de segurança Azure, GitHub Advanced Security e gestão de identidade empresarial

#### Tópicos Avançados de Segurança (05-AdvancedTopics/mcp-security/) - Implementação Pronta para Produção
- **README.md**: Reescrita completa para implementação de segurança empresarial
  - **Alinhamento à Especificação Atual**: Atualizado para Especificação MCP 2025-06-18 com requisitos de segurança obrigatórios
  - **Autenticação Aprimorada**: Integração Microsoft Entra ID com exemplos abrangentes em .NET e Java Spring Security
  - **Integração de Segurança AI**: Implementação Microsoft Prompt Shields e Azure Content Safety com exemplos detalhados em Python
  - **Mitigação Avançada de Ameaças**: Exemplos completos de implementação para
    - Prevenção de Ataque Confused Deputy com PKCE e validação de consentimento do usuário
    - Prevenção de Passagem de Token com validação de audiência e gestão segura de token
    - Prevenção de Sequestro de Sessão com vinculação criptográfica e análise comportamental
  - **Integração de Segurança Empresarial**: Monitoramento Azure Application Insights, pipelines de detecção de ameaças e segurança da cadeia de suprimentos
  - **Checklist de Implementação**: Controles de segurança obrigatórios vs. recomendados com benefícios do ecossistema de segurança Microsoft

### Qualidade da Documentação & Alinhamento a Padrões
- **Referências de Especificação**: Atualizadas todas as referências para Especificação MCP 2025-06-18
- **Ecossistema de Segurança Microsoft**: Orientação aprimorada para integração em toda documentação de segurança
- **Implementação Prática**: Adicionados exemplos detalhados de código em .NET, Java e Python com padrões empresariais
- **Organização de Recursos**: Categorização abrangente de documentação oficial, padrões de segurança e guias de implementação
- **Indicadores Visuais**: Marcação clara de requisitos obrigatórios versus práticas recomendadas


#### Conceitos Centrais (01-CoreConcepts/) - Modernização Completa
- **Atualização da Versão do Protocolo**: Atualizada para referenciar a Especificação MCP 2025-06-18 com versionamento baseado em data (formato YYYY-MM-DD)
- **Refino da Arquitetura**: Descrições aprimoradas de Hosts, Clientes e Servidores para refletir padrões atuais da arquitetura MCP
  - Hosts agora claramente definidos como aplicações IA coordenando múltiplas conexões MCP client
  - Clientes descritos como conectores de protocolo mantendo relações um-para-um com servidores
  - Servidores aprimorados com cenários de implantação local vs. remota
- **Reestruturação de Primitivos**: Reformulação completa dos primitivos de servidor e cliente
  - Primitivos do Servidor: Recursos (fontes de dados), Prompts (modelos), Ferramentas (funções executáveis) com explicações e exemplos detalhados
  - Primitivos do Cliente: Amostragem (completions LLM), Elucidação (entrada do usuário), Registro (debug/monitoramento)
  - Atualizado com padrões atuais de métodos discovery (`*/list`), retrieval (`*/get`) e execução (`*/call`)
- **Arquitetura do Protocolo**: Introduzido modelo arquitetural de duas camadas
  - Camada de Dados: Fundação JSON-RPC 2.0 com gerenciamento de ciclo de vida e primitivos
  - Camada de Transporte: STDIO (local) e HTTP Streamable com SSE (remoto) como mecanismos de transporte
- **Framework de Segurança**: Princípios abrangentes de segurança incluindo consentimento explícito do usuário, proteção de privacidade de dados, segurança na execução de ferramentas e segurança na camada de transporte
- **Padrões de Comunicação**: Mensagens do protocolo atualizadas para mostrar inicialização, descoberta, execução e fluxos de notificação
- **Exemplos de Código**: Atualizados exemplos multi-idioma (.NET, Java, Python, JavaScript) para refletir padrões atuais do SDK MCP

#### Segurança (02-Security/) - Reformulação Abrangente de Segurança  
- **Alinhamento a Padrões**: Alinhamento total com requisitos de segurança da Especificação MCP 2025-06-18
- **Evolução da Autenticação**: Documentada evolução de servidores OAuth customizados para delegação a provedores externos de identidade (Microsoft Entra ID)
- **Análise de Ameaças Específicas de IA**: Cobertura aprimorada dos vetores modernos de ataque à IA
  - Cenários detalhados de ataques por injeção de prompt com exemplos do mundo real
  - Mecanismos de envenenamento de ferramentas e padrões de ataque “rug pull”
  - Envenenamento da janela de contexto e ataques de confusão do modelo
- **Soluções Microsoft de Segurança para IA**: Cobertura abrangente do ecossistema de segurança Microsoft
  - AI Prompt Shields com detecção avançada, destaque e técnicas de delimitador
  - Padrões de integração Azure Content Safety
  - GitHub Advanced Security para proteção da cadeia de suprimentos
- **Mitigação Avançada de Ameaças**: Controles de segurança detalhados para
  - Sequestro de sessão com cenários de ataque específicos MCP e requisitos criptográficos de ID de sessão
  - Problemas Confused Deputy em cenários proxy MCP com requisitos explícitos de consentimento
  - Vulnerabilidades de passagem de token com controles obrigatórios de validação
- **Segurança da Cadeia de Suprimentos**: Cobertura expandida da cadeia de suprimentos de IA incluindo modelos fundação, serviços de embeddings, provedores de contexto e APIs de terceiros
- **Segurança da Fundação**: Integração aprimorada com padrões de segurança empresarial incluindo arquitetura zero trust e ecossistema Microsoft
- **Organização de Recursos**: Links abrangentes categorizados por tipo (Documentos Oficiais, Padrões, Pesquisa, Soluções Microsoft, Guias de Implementação)

### Melhorias na Qualidade da Documentação
- **Objetivos de Aprendizado Estruturados**: Objetivos de aprendizado aprimorados com resultados específicos e acionáveis 
- **Referências Cruzadas**: Adicionados links entre tópicos relacionados de segurança e conceitos centrais
- **Informações Atualizadas**: Atualizadas todas as referências de data e links de especificações para padrões atuais
- **Orientação de Implementação**: Adicionadas diretrizes específicas e acionáveis de implementação em ambas as seções

## 16 de julho de 2025

### Melhorias no README e Navegação
- Navegação do currículo completamente reformulada no README.md
- Substituídas tags `<details>` por formato mais acessível baseado em tabelas
- Criadas opções alternativas de layout na nova pasta "alternative_layouts"
- Adicionados exemplos de navegação em estilo card, abas e acordeão
- Seção de estrutura do repositório atualizada com todos os arquivos mais recentes
- Seção "Como Usar Este Currículo" aprimorada com recomendações claras
- Links da especificação MCP atualizados para URLs corretos
- Adicionada seção Engenharia de Contexto (5.14) na estrutura do currículo

### Atualizações do Guia de Estudos
- Guia de estudos completamente revisado para alinhamento com estrutura atual do repositório
- Novas seções adicionadas para Clientes MCP e Ferramentas, e Servidores MCP Populares
- Mapa Visual do Currículo atualizado para refletir com precisão todos os tópicos
- Descrições de Tópicos Avançados aprimoradas para cobrir todas áreas especializadas
- Seção de Estudos de Caso atualizada para refletir exemplos reais
- Adicionado este changelog abrangente

### Contribuições da Comunidade (06-CommunityContributions/)
- Adicionadas informações detalhadas sobre servidores MCP para geração de imagens
- Adicionada seção abrangente sobre uso do Claude no VSCode
- Instruções de configuração e uso do cliente terminal Cline adicionadas
- Seção de clientes MCP atualizada para incluir todas as opções populares
- Exemplos de contribuição aprimorados com amostras de código mais precisas

### Tópicos Avançados (05-AdvancedTopics/)
- Todas pastas de tópicos especializados organizadas com nomeação consistente
- Adicionados materiais e exemplos de engenharia de contexto
- Documentação de integração do agente Foundry adicionada
- Documentação aprimorada da integração de segurança Entra ID adicionada

## 11 de junho de 2025

### Criação Inicial
- Versão inicial do currículo MCP para Iniciantes lançada
- Estrutura básica criada para todas as 10 seções principais
- Implementado Mapa Visual do Currículo para navegação
- Projetos exemplos iniciais adicionados em múltiplas linguagens de programação

### Começando (03-GettingStarted/)
- Criados os primeiros exemplos de implementação de servidor
- Orientações adicionadas para desenvolvimento de clientes
- Instruções de integração de cliente LLM incluídas
- Documentação de integração VS Code adicionada
- Exemplos de servidor Server-Sent Events (SSE) implementados

### Conceitos Centrais (01-CoreConcepts/)
- Explicação detalhada da arquitetura cliente-servidor adicionada
- Documentação dos principais componentes do protocolo criada
- Padrões de mensageria no MCP documentados

## 23 de maio de 2025

### Estrutura do Repositório
- Repositório inicializado com estrutura básica de pastas
- Criados arquivos README para cada seção principal
- Infraestrutura de tradução configurada
- Adicionados ativos de imagem e diagramas

### Documentação
- README.md inicial criado com visão geral do currículo
- Adicionados arquivos CODE_OF_CONDUCT.md e SECURITY.md
- SUPPORT.md configurado com orientações para obtenção de ajuda
- Estrutura preliminar do guia de estudos criada

## 15 de abril de 2025

### Planejamento e Framework
- Planejamento inicial para currículo MCP para Iniciantes
- Objetivos de aprendizado e público-alvo definidos
- Estrutura de 10 seções delineada para o currículo
- Framework conceitual desenvolvido para exemplos e estudos de caso
- Protótipos iniciais de exemplos criados para conceitos-chave

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido usando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, por favor, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->