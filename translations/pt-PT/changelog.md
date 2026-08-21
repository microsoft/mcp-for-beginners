# Registo de alterações: Currículo MCP para Iniciantes

Este documento serve como um registo de todas as alterações significativas feitas ao currículo Model Context Protocol (MCP) para Iniciantes. As alterações são documentadas em ordem cronológica inversa (primeiro as mais recentes).

## 29 de julho de 2026

### Novo Módulo 08 Complementar: Sidecars de Confiabilidade e Repetições Seguras

Adicionada uma lição complementar independente do fornecedor para ferramentas MCP que criam efeitos no mundo real,
alinhada com a especificação final `2026-07-28`.

- **Novo**: A [lição complementar reliability sidecar][reliability-sidecar]
  usa uma história de suporte-tickets, dois diagramas Mermaid, e um fluxo de decisão de tentativas
  para explicar as chaves de operação estável, admissão atómica de duplicados,
  reconciliação, evidência, e o limite da extensão Tasks.
- **Novo**: Um exercício de injeção de falhas usando Python da biblioteca padrão e SQLite
  usa armazenamentos separados de operações e tickets para demonstrar uma resposta perdida
  após um efeito externo ser confirmado. Seis testes determinísticos cobrem duplicação ingênua,
  recuperação guardada de reinício, conflitos de carga útil, resultados em cache,
  reivindicações ativas, e admissão concorrente de duplicados.
- **Atualizado**: O Módulo 08 agora liga a lição complementar, identifica o
  modelo final de pedido sem estado `2026-07-28`, distingue a observabilidade OpenTelemetry
  da funcionalidade de registo MCP descontinuada, e limita o seu
  exemplo genérico de repetição a operações somente de leitura.
- **Opcional**: A lição mapeia os seus conceitos portáteis para uma implementação comunitária etiquetada
  sem tornar o serviço alojado ou uma chamada de rede parte
  do exercício.

[reliability-sidecar]: ./08-BestPractices/reliability-sidecars/README.md

## 2 de julho de 2026

### Nova Lição: Candidato a Lançamento da Especificação MCP 2026-07-28

Adicionada cobertura do próximo candidato a lançamento da especificação MCP `2026-07-28` (anunciado a 21 de maio de 2026; lançamento final previsto para 28 de julho de 2026), resumido a partir do [post oficial de anúncio no blog](https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/). A base do currículo permanece sendo a **Especificação MCP 2025-11-25** até que a nova versão seja lançada, por isso isto é apresentado como orientação para o futuro e não como uma reescrita das lições existentes.

- **Novo**: [01-CoreConcepts/mcp-2026-07-28-release-candidate.md](./01-CoreConcepts/mcp-2026-07-28-release-candidate.md) — uma lição completa cobrindo o núcleo do protocolo sem estado (remoção do handshake `initialize` e do `Mcp-Session-Id`), os novos cabeçalhos de roteamento `Mcp-Method`/`Mcp-Name`, metadados de cache `ttlMs`/`cacheScope`, Contexto Trace W3C em `_meta`, o framework formal de Extensões (Apps MCP e a nova extensão Tasks), seis SEPs de endurecimento de autorização, a descontinuação de Roots/Sampling/Logging, e a transição para JSON Schema 2020-12 completo para schemas de ferramentas.
- **Atualizado** com chamadas prospectivas ligando à nova lição:
  - [01-CoreConcepts/README.md](./01-CoreConcepts/README.md): nota sobre a versão do protocolo, secções Sampling/Roots/Logging/Tasks e "O que vem a seguir"
  - [02-Security/README.md](./02-Security/README.md): chamada de endurecimento de autorização
  - [03-GettingStarted/06-http-streaming/README.md](./03-GettingStarted/06-http-streaming/README.md): chamada sobre transporte sem estado
  - [03-GettingStarted/14-sampling/README.md](./03-GettingStarted/14-sampling/README.md): chamada sobre descontinuação do Sampling
  - [05-AdvancedTopics/mcp-protocol-features/README.md](./05-AdvancedTopics/mcp-protocol-features/README.md): chamada sobre descontinuação do Logging e extensão Tasks
  - [05-AdvancedTopics/mcp-transport/README.md](./05-AdvancedTopics/mcp-transport/README.md): chamada sobre transporte sem estado e roteamento de sessão
  - [README.md](./README.md): nota "Olhando para o futuro" na secção da especificação e nova entrada `1.1` na tabela de módulos do currículo
  - [study_guide.md](./study_guide.md): ponto prospectivo sobre a visão geral dos Conceitos Centrais e nota datada de adendo
  - [03-GettingStarted/11-simple-auth/README.md](./03-GettingStarted/11-simple-auth/README.md): chamada sobre o mapa de transporte `mcp-session-id` antes do modelo de pedido sem estado
  - [05-AdvancedTopics/README.md](./05-AdvancedTopics/README.md): chamada sobre o panorama do módulo, descontinuações Root Contexts/Sampling e extensão Tasks
  - [05-AdvancedTopics/mcp-security/README.md](./05-AdvancedTopics/mcp-security/README.md): chamada de endurecimento de autorização

## 24 de junho de 2026

### Nova Lição: Usando MCP na aplicação Copilot

- [Secção de Ferramentas](./12-tooling/README.md) Adicionada secção de ferramentas.
- [MCP na aplicação Copilot](./12-tooling/01-copilot-app/README.md)

## 16 de junho de 2026

### Alinhamento com a Especificação MCP & Validação de Amostras

Validado o currículo em relação à atual **Especificação MCP 2025-11-25** e aos SDKs oficiais mais recentes, depois corrigidas referências antigas restantes e confirmado que os exemplos principais continuam a construir e a executar.

#### Correções na Versão da Especificação (2025-06-18 / 2025-03-26 → 2025-11-25)

Atualizado o conteúdo em inglês onde ainda afirmava que uma revisão anterior da especificação era a norma *atual/mais recente*, e reorientados os links para os caminhos canónicos da especificação em `modelcontextprotocol.io`:
- **05-AdvancedTopics/mcp-security/README.md**: Atualizado o banner "Norma Atual", introdução, cabeçalhos dos princípios de segurança centrais, requisitos obrigatórios, secção Microsoft Entra ID, links para Referências & Recursos, e nota de segurança final (8 referências) para 2025-11-25
- **05-AdvancedTopics/mcp-transport/README.md**: Atualizado o link para a especificação Recursos Adicionais e banner "Norma Atual" para 2025-11-25
- **05-AdvancedTopics/mcp-realtimesearch/README.md**: Substituído o link desatualizado de `2025-03-26` sobre segurança e confiança pela página atual de boas práticas de segurança 2025-11-25
- **03-GettingStarted/14-sampling/README.md**: Atualizado o link dos documentos oficiais sobre amostragem para 2025-11-25
- **03-GettingStarted/05-stdio-server/README.md**: Atualizada a referência em tempo presente "especificação MCP atual" e o link da especificação Recursos Adicionais para 2025-11-25 (notas históricas sobre descontinuação do SSE mantidas para precisão)

#### Validação das Amostras em Relação aos SDKs Atuais

- **TypeScript (03-GettingStarted/01-first-server/solution/typescript)**: `npm install` resolveu `@modelcontextprotocol/sdk@1.29.0`; `tsc --noEmit` passou sem erros de tipo — APIs `McpServer`/`StdioServerTransport` existentes continuam válidas
- **Python (03-GettingStarted/01-first-server/solution/python)**: Validado num `.venv` isolado com `mcp[cli]` (1.27.2); `py_compile` passou e `FastMCP.list_tools()` retornou corretamente as ferramentas `add` e `subtract`
- Confirmados todos os intervalos de versão da amostra `@modelcontextprotocol/sdk` (`>=1.26.0` / `^1.26.0` / `^1.27.0`) resolvidos limpos para a versão atual `1.29.0` sem mudanças incompatíveis nas APIs

#### Alinhamento das Dependências (fechamento de lacunas de versões)

Atualizadas as versões dos SDKs desatualizados para que cada amostra acompanhe o lançamento atual do MCP, seguindo a convenção do repositório:
- **03-GettingStarted/05-stdio-server/solution/typescript/package.json**: Atualizado `@modelcontextprotocol/sdk` de `^1.8.0` → `>=1.26.0` e descrito o pacote ultrapassado `"updated for MCP 2025-06-18"` para `"aligned with MCP Specification 2025-11-25"`
- **10-StreamliningAIWorkflows.../lab3/code/weather_mcp/pyproject.toml** e **lab4/code/github_mcp_server/pyproject.toml**: Atualizado o pin exato `mcp==1.23.0` → `mcp>=1.26.0`; regenerados ambos os ficheiros `uv.lock` (`uv lock`) para que os lockfiles resolvam para o actual `mcp 1.27.2` e se mantenham sincronizados com os manifestos

#### Análise das Lacunas do Currículo — Cobertura das Funcionalidades mais Recentes na Especificação

Verificado que o currículo já cobre todos os primitivos introduzidos/expandido no MCP 2025-11-25, pelo que não restam lacunas de conteúdo:
- **Sampling**: Lição 03-GettingStarted/14-sampling e 05-AdvancedTopics/mcp-sampling
- **Elicitação (incluindo modo URL)**: Documentado em 01-CoreConcepts e 05-AdvancedTopics/mcp-protocol-features
- **Roots**: Documentado em 00-Introduction, 01-CoreConcepts e 05-AdvancedTopics/mcp-root-contexts
- **Tasks (experimental, operações de longa duração)**: Documentado em 01-CoreConcepts e 05-AdvancedTopics/mcp-protocol-features
- **Anotações de Ferramentas** (`readOnlyHint` / `destructiveHint`): Documentadas em 01-CoreConcepts e 05-AdvancedTopics/mcp-protocol-features

### Reforço de Segurança & Remediação de Vulnerabilidades em Dependências

Realizado um controlo completo de segurança em todos os manifestos de dependência e código-fonte das amostras, tendo sido remediados todos os avisos npm reportados e uma deteção a nível de código. Após remediação, `npm audit` reporta **0 vulnerabilidades** em todos os diretórios auditados.

#### Vulnerabilidades em Dependências npm (transitivas) — Corrigidas

Auditados todos os 15 ficheiros `package-lock.json` comprometidos. Vulnerabilidades limitavam-se a dependências transitivas trazidas pela ferramenta dev MCP Inspector, cliente OpenAI e o SDK MCP; todas agora resolvidas sem quebrar os exemplos:
- **10-StreamliningAIWorkflows.../lab4/code/github_mcp_server/inspector** e **lab3/code/weather_mcp/inspector**: Atualizado `@modelcontextprotocol/inspector` (`0.16.6` / `0.14.1` → `0.22.0`), o que eliminou os avisos agrupados `ajv`, `brace-expansion`, `diff`, `path-to-regexp` e `ws`. Adicionada entrada npm `overrides` forçando o patch `shell-quote@1.8.4` para eliminar o aviso crítico restante do `concurrently`; regenerados ambos os lockfiles (agora 0 vulnerabilidades)
- **03-GettingStarted/samples/typescript**: `npm audit fix` atualizou a dependência transitiva `qs` (moderada) para uma release patchada
- **03-GettingStarted/samples/javascript**: `npm audit fix` atualizou a dependência transitiva `hono` (moderada) para uma release patchada
- **03-GettingStarted/03-llm-client/solution/typescript**: `npm audit fix` atualizou a dependência transitiva `form-data` (alta) para uma release patchada
- **03-GettingStarted/11-simple-auth/solution/typescript**: Gerado o `package-lock.json` em falta para que o projeto seja reprodutível e auditável (0 vulnerabilidades)

#### Correção de Segurança a Nível de Código (OWASP A03: Injection)

- **10-StreamliningAIWorkflows.../lab4/code/github_mcp_server/src/server.py**: Removido `shell=True` da ferramenta `open_in_vscode`. A linha anterior `subprocess.run(["start", "", vscode_path, folder_path], shell=True)` permitia que metacaracteres do shell num caminho de pasta fossem interpretados por `cmd.exe` (vetor de injeção de comandos). Agora lança diretamente o `Code.exe` resolvido com a pasta como argumento — sem shell — o que é funcionalmente equivalente e seguro

#### Auditoria de Dependências Python

- Auditadas todas as definições de requirements Python com `pip-audit`. `05-AdvancedTopics` e `03-GettingStarted/samples/python` reportaram **nenhuma vulnerabilidade conhecida** (os seus intervalos `mcp` / `httpx` / `pydantic` / `python-dotenv` resolvem para releases patchadas atuais)
- **09-CaseStudy/docs-mcp/solution/python/requirements.txt**: `pip-audit` identificou a dependência transitiva **`werkzeug` 3.1.1** com três avisos DoS de nomes de dispositivos do Windows no `safe_join` — `CVE-2025-66221`, `CVE-2026-21860` e `CVE-2026-27199` (todas corrigidas na 3.1.6). Adicionada uma fixação explícita de segurança `werkzeug>=3.1.6` para resolver a release patchada; verificado que a restrição resolve bem com a stack `chainlit` / `mcp` / `semantic-kernel`

### Rebranding do Nome do Produto

Atualizado todo o conteúdo do currículo para refletir o rebranding do produto da Microsoft:

#### Azure AI Foundry → Microsoft Foundry
- **SUPPORT.md**: Atualizado o link da comunidade Discord

- **AGENTS.md**: Atualizada referência ao servidor Discord
- **README.md**: Atualizadas referências ao ecossistema tecnológico
- **study_guide.md**: Atualizadas referências ao estudo de caso
- **05-AdvancedTopics/README.md**: Atualizado título e descrição do Módulo 5.13
- **05-AdvancedTopics/mcp-integration/README.md**: Atualizado cabeçalho da secção e descrição
- **05-AdvancedTopics/mcp-foundry-agent-integration/README.md**: Atualização completa do título e conteúdo do módulo
- **05-AdvancedTopics/mcp-security-entra/README.md**: Atualizado link de referência cruzada
- **07-LessonsfromEarlyAdoption/README.md**: Atualizadas referências ao estudo de caso
- **07-LessonsfromEarlyAdoption/microsoft-mcp-servers.md**: Atualizado cabeçalho da Secção 9, emblemas e capacidades
- **08-BestPractices/README.md**: Atualizado link da comunidade Discord
- **09-CaseStudy/docs-mcp/solution/scenario3/README.md**: Atualizada referência ao canal Discord
- **09-CaseStudy/docs-mcp/solution/python/README.md**: Atualizada referência ao deployment do modelo
- **11-MCPServerHandsOnLabs/00-Introduction/README.md**: Atualizada tabela de Serviços AI
- **11-MCPServerHandsOnLabs/03-Setup/README.md**: Atualizadas referências dos recursos

#### AI Toolkit / AITK → Extensão Microsoft Foundry Toolkit para VS Code
- **README.md**: Atualizadas referências principais do currículo
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/README.md**: Atualizado título do módulo, visão geral e todos os cabeçalhos dos módulos
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab1/README.md**: Atualizados título, objetivos de aprendizagem, instruções de configuração e recursos
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab2/README.md**: Atualizados título, objetivos de aprendizagem, tabela de hosts MCP e referências cruzadas
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/README.md**: Atualizados título, emblemas, pré-requisitos e recursos
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/README.md**: Atualizadas referências ao Agent Builder e link de feedback
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/README.md**: Atualizados pré-requisitos e referências de extensão

---

## 11 de Abril de 2026

### Nova lição, correções de documentação e atualizações de dependências

#### Novo conteúdo curricular adicionado

**Módulo 05 - Tópicos Avançados**
- **Lição 5.17: Raciocínio Multi-Agente Adversarial com MCP** (`05-AdvancedTopics/mcp-adversarial-agents/README.md`): Novo guia abrangente que cobre o padrão de debate adversarial para sistemas multi-agente
  - Diagrama de arquitetura Mermaid: dois agentes → servidor MCP partilhado → transcrição do debate → juiz → veredito
  - Servidor de ferramentas partilhado MCP (`web_search` + `run_python`) implementado em Python e TypeScript
  - Prompts de sistema opostos (A FAVOR / CONTRA / Juiz) com requisitos explícitos de uso de ferramenta
  - Orquestrador de debate em Python, TypeScript e C# gerindo rondas e roteamento de argumentos
  - Ligação MCP `ClientSession` para o orquestrador a chamadas reais de ferramentas
  - Tabela de casos de uso (detecção de alucinações, modelação de ameaças, revisão de design de API, verificação factual, seleção tecnológica)
  - Considerações de segurança: execução em sandbox, validação de chamadas de ferramenta, limitação de taxa, registo de auditoria
  - Exercício estruturado com três cenários práticos (revisão de código, decisão de arquitetura, moderação de conteúdo)

#### Correções de documentação

**Módulo 03 - Primeiros Passos**
- **05-stdio-server/README.md**: Corrigido exemplo incompleto de servidor stdio TypeScript — adicionada instanciação de transporte em falta (`new StdioServerTransport()`) e chamada `server.connect(transport)` para corresponder aos exemplos em Python e .NET na mesma secção
- **14-sampling/README.md**: Corrigido erro tipográfico — `"Sampling is an davanced features"` → `"Sampling is an advanced feature"`

#### Atualizações do currículo

**README.md principal**
- Adicionada entrada 5.17 (Raciocínio Multi-Agente Adversarial com MCP) à tabela curricular com link direto para a nova lição

**05-AdvancedTopics/README.md**
- Adicionada linha da Lição 5.17 à tabela de lições

**study_guide.md**
- Adicionado tópico de Raciocínio Multi-Agente Adversarial ao mapa mental e descrição em prosa de Tópicos Avançados

#### Correções de código e segurança

**Módulo 05 - Agentes Adversariais (`mcp-adversarial-agents`)**
- **Correção de segurança — injeção de comandos**: Substituída interpolação de shell `execSync` por `execFile` + `promisify` na ferramenta `run_python` TypeScript, eliminando superfície de injeção de comandos (código controlado pelo LLM é agora passado como elemento literal argv sem envolvimento de shell)
- **Ligação do loop de ferramenta MCP**: Atualizado orquestrador de debate Python para usar cliente `AsyncAnthropic` (substituindo `Anthropic` síncrono bloqueante), passar `ClientSession` ao vivo diretamente a cada turno do agente, buscar definições de ferramentas via `session.list_tools()` em cada turno, e despachar blocos `tool_use` via `session.call_tool()` em loop até o modelo emitir resposta final de texto

#### Atualizações de dependências

- Atualizado `hono` para 4.12.12 em múltiplos pacotes (03-GettingStarted, 04-PracticalImplementation, 10-StreamliningAIWorkflows)
- Atualizado `@hono/node-server` de 1.19.11 para 1.19.13 em pacotes TypeScript
- Atualizado `cryptography` de 46.0.5 para 46.0.7 em pacotes Python (labs 3 e 4 de 10-StreamliningAIWorkflows)
- Atualizado `lodash` de 4.17.23 para 4.18.1 no inspetor 10-StreamliningAIWorkflows

#### Traduções

- Sincronizadas traduções para 48+ línguas com as últimas alterações da fonte (atualização i18n)

---

## 5 de Fevereiro de 2026

### Validação e melhorias de navegação em todo o repositório

#### Novo conteúdo curricular adicionado

**Módulo 03 - Primeiros Passos**
- **12-mcp-hosts/README.md**: Novo guia abrangente para configuração de hosts MCP
  - Exemplos de configuração para Claude Desktop, VS Code, Cursor, Cline, Windsurf
  - Modelos de configuração JSON para todos os principais hosts
  - Tabela comparativa de tipos de transportes (stdio, SSE/HTTP, WebSocket)
  - Resolução de problemas comuns de conexão
  - Melhores práticas de segurança para configuração de hosts

- **13-mcp-inspector/README.md**: Novo guia de depuração para MCP Inspector
  - Métodos de instalação (npx, npm global, a partir do código-fonte)
  - Conexão a servidores via stdio e HTTP/SSE
  - Ferramentas de teste, recursos e fluxos de trabalho de prompts
  - Integração com VS Code do MCP Inspector
  - Cenários comuns de depuração com soluções

**Módulo 04 - Implementação Prática**
- **pagination/README.md**: Novo guia de implementação de paginação
  - Padrões de paginação baseados em cursor em Python, TypeScript, Java
  - Gestão de paginação do lado do cliente
  - Estratégias de design de cursor (opaco vs. estruturado)
  - Recomendações para otimização de desempenho

**Módulo 05 - Tópicos Avançados**
- **mcp-protocol-features/README.md**: Análise aprofundada das funcionalidades do protocolo
  - Implementação de notificações de progresso
  - Padrões para cancelamento de pedidos
  - Templates de recursos com padrões de URI
  - Gestão do ciclo de vida do servidor
  - Controlo de níveis de logging
  - Padrões de tratamento de erros com códigos JSON-RPC

#### Correções de navegação (24+ ficheiros atualizados)

**README dos módulos principais**
 Agora com links para a primeira lição E para o próximo módulo

**Subficheiros de Segurança 02-Security**
- Todos os 5 documentos suplementares de segurança têm agora navegação "O que vem a seguir":

**Ficheiros 09-CaseStudy**
- Todos os ficheiros de estudo de caso têm agora navegação sequencial:

**Labs 10-StreamliningAI**
Adicionada secção O Que Vem A Seguir na visão geral do Módulo 10 e no Módulo 11

#### Correções de código e de conteúdo

**Atualizações do SDK e dependências**
Corrigida versão vazia openai para `^4.95.0`
SDK atualizado de `^1.8.0` para `>=1.26.0`
Versões do mcp atualizadas para `>=1.26.0`

**Correções de código**
Corrigido modelo inválido `gpt-4o-mini` para `gpt-4.1-mini`

**Correções de conteúdo**
Corrigido link partido `READMEmd` → `README.md`, corrigido cabeçalho do currículo `Module 1-3` → `Module 0-3`, corrigido caminho sensível a maiúsculas/minúsculas
Removido conteúdo duplicado corrompido do Estudo de Caso 5

**Melhorias no Guiamento para Iniciantes**
Adição de introdução adequada, objetivos de aprendizagem e pré-requisitos para iniciantes

#### Atualizações do currículo

**README.md principal**
- Adicionadas entradas 3.12 (Hosts MCP), 3.13 (MCP Inspector), 4.1 (Paginação), 5.16 (Funcionalidades do Protocolo) à tabela do currículo

**README dos Módulos**
Adicionadas lições 12 e 13 à lista de lições
Adicionada secção Guias Práticos com link para paginação
Adicionadas lições 5.15 (Transporte Personalizado) e 5.16 (Funcionalidades do Protocolo)

**study_guide.md**
- Atualizado mapa mental com todos os novos tópicos: Configuração de Hosts MCP, MCP Inspector, Estratégias de Paginação, Análise Aprofundada de Funcionalidades do Protocolo

## 28 de Janeiro de 2026

### Revisão de Conformidade da Especificação MCP 2025-11-25

#### Aprimoramento dos Conceitos Base (01-CoreConcepts/)
- **Novo Primitivo de Cliente - Roots**: Adicionada documentação abrangente sobre o primitivo de cliente Roots, permitindo aos servidores compreender limites do sistema de ficheiros e permissões de acesso
- **Anotações de Ferramentas**: Documentação adicionada sobre anotações comportamentais de ferramenta (`readOnlyHint`, `destructiveHint`) para melhores decisões de execução de ferramenta
- **Chamada de Ferramenta em Sampling**: Documentação de Sampling atualizada para incluir parâmetros `tools` e `toolChoice` para invocação de ferramenta guiada por modelo durante pedidos de sampling
- **Elicitação em Modo URL**: Documentação adicionada sobre elicitação baseada em URL para interações externas baseadas na web iniciadas pelo servidor
- **Tarefas (Experimental)**: Nova secção documentando a funcionalidade experimental de Tarefas para wrappers de execução durável e recuperação diferida de resultados
- **Suporte a Ícones**: Observação que ferramentas, recursos, templates de recurso e prompts podem agora incluir ícones como metadados adicionais

#### Atualizações de Documentação
- **README.md**: Adicionada referência à versão da Especificação MCP 2025-11-25 e explicação da versão baseada em data
- **study_guide.md**: Mapa curricular atualizado para incluir Tarefas e Anotações de Ferramenta na secção de Conceitos Base; atualizado timestamp do documento

#### Verificação de Conformidade com a Especificação
- **Versão do Protocolo**: Confirmadas todas as referências da documentação à Especificação MCP 2025-11-25 atual
- **Alinhamento arquitetural**: Confirmada precisão da documentação da arquitetura de duas camadas (Camada de Dados + Camada de Transporte)
- **Documentação de Primitivos**: Validada documentação de primitivos de servidor (Recursos, Prompts, Ferramentas) e de cliente (Sampling, Elicitação, Logging, Roots)
- **Mecanismos de Transporte**: Verificada precisão da documentação dos transportes STDIO e HTTP Streamable 
- **Orientações de Segurança**: Confirmada conformidade com as melhores práticas de segurança MCP atuais

#### Funcionalidades Chave da MCP 2025-11-25 Documentadas
- **Descoberta OpenID Connect**: Descoberta do servidor de autenticação via OIDC
- **Metadados do Client ID OAuth**: Recomendada mecanismo de registo de cliente
- **JSON Schema 2020-12**: Dialeto padrão para definições de esquema MCP
- **Sistema de Níveis do SDK**: Formalizados requisitos para suporte e manutenção de funcionalidades SDK
- **Estrutura de Governança**: Formalizados Grupos de Trabalho e Grupos de Interesse na governança MCP

### Atualização importante na documentação de segurança (02-Security/)

#### Integração do Workshop MCP Security Summit (Sherpa)
- **Novo recurso de formação prática**: Adicionada integração abrangente com o [MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/) em toda a documentação de segurança
- **Cobertura da rota de expedição**: Documentada progressão completa do acampamento base ao cume
- **Alinhamento OWASP**: Todas as orientações de segurança agora mapeadas para os riscos OWASP MCP Azure Security Guide

#### Integração dos 10 principais riscos de segurança OWASP MCP
- **Nova secção**: Adicionada tabela de riscos de segurança OWASP MCP Top 10 com mitigações Azure à README principal de Segurança
- **Documentação baseada em risco**: Atualizado mcp-security-controls-2025.md com referências a riscos OWASP MCP para cada domínio de segurança
- **Arquitetura de referência**: Ligação à arquitetura de referência OWASP MCP Azure Security Guide e padrões de implementação

#### Ficheiros de Segurança Atualizados
- **README.md**: Adicionada visão geral do Workshop Sherpa, tabela da rota da expedição, resumo dos riscos OWASP MCP Top 10 e secção de formação prática
- **mcp-security-controls-2025.md**: Cabeçalho atualizado para Fevereiro 2026, adicionadas referências a riscos OWASP (MCP01-MCP08), corrigida inconsistência de versão na especificação
- **mcp-security-best-practices-2025.md**: Adicionada secção de recursos Sherpa e OWASP, atualizado timestamp
- **mcp-best-practices.md**: Adicionada secção de formação prática com links Sherpa e OWASP
- **azure-content-safety-implementation.md**: Adicionada referência OWASP MCP06, alinhamento com Sherpa Camp 3 e secção adicional de recursos

#### Novos links de recursos adicionados
- [MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/)

- [Guia de Segurança MCP Azure da OWASP](https://microsoft.github.io/mcp-azure-security-guide/)
- [OWASP MCP Top 10](https://owasp.org/www-project-mcp-top-10/)
- Páginas individuais de risco OWASP MCP (MCP01-MCP10)

### Alinhamento da Especificação MCP a Nível Curricular 2025-11-25

#### Módulo 03 - Introdução
- **Documentação SDK**: Adicionado SDK Go à lista oficial de SDKs; atualizadas todas referências de SDK para alinhar com a Especificação MCP 2025-11-25
- **Clarificação de Transporte**: Descrições de transporte STDIO e HTTP Streaming atualizadas com referências explícitas à especificação

#### Módulo 04 - Implementação Prática
- **Atualizações do SDK**: Adicionado SDK Go; lista de SDK atualizada com referência à versão da especificação
- **Especificação de Autorização**: Atualizado link da especificação de Autorização MCP para a versão atual 2025-11-25

#### Módulo 05 - Tópicos Avançados
- **Novas Funcionalidades**: Adicionada nota sobre novas funcionalidades da Especificação MCP 2025-11-25 (Tarefas, Anotações de Ferramentas, Elicitação por Modo URL, Raízes)
- **Recursos de Segurança**: Adicionados links para OWASP MCP Top 10 e workshop Sherpa nas referências adicionais

#### Módulo 06 - Contribuições da Comunidade
- **Lista de SDKs**: Adicionados SDKs Swift e Rust; link da especificação atualizado para 2025-11-25
- **Referência da Especificação**: Link da Especificação MCP atualizado para URL direta da especificação

#### Módulo 07 - Lições da Adoção Inicial
- **Atualizações de Recursos**: Adicionado link da Especificação MCP 2025-11-25 e OWASP MCP Top 10 aos recursos adicionais

#### Módulo 08 - Boas Práticas
- **Versão da Especificação**: Referência da Especificação MCP atualizada para 2025-11-25
- **Recursos de Segurança**: Adicionadas OWASP MCP Top 10 e workshop Sherpa nas referências adicionais

#### Módulo 10 - Otimização de Fluxos de Trabalho com IA
- **Atualização de Emblema**: Alterado o emblema da versão MCP de versão SDK (1.9.3) para versão da especificação (2025-11-25)
- **Links de Recursos**: Atualizado link da Especificação MCP; adicionada OWASP MCP Top 10

#### Módulo 11 - Laboratórios Práticos MCP Server
- **Referência da Especificação**: Link da Especificação MCP atualizado para versão 2025-11-25
- **Recursos de Segurança**: Adicionado OWASP MCP Top 10 aos recursos oficiais

## 18 de dezembro de 2025

### Atualização da Documentação de Segurança - Especificação MCP 2025-11-25

#### Melhores Práticas de Segurança MCP (02-Security/mcp-best-practices.md) - Atualização da Versão da Especificação
- **Atualização da Versão do Protocolo**: Atualizado para referenciar a última Especificação MCP 2025-11-25 (lançada a 25 de novembro de 2025)
  - Atualizadas todas as referências de versão da especificação de 2025-06-18 para 2025-11-25
  - Atualizadas as datas dos documentos de 18 de agosto de 2025 para 18 de dezembro de 2025
  - Verificadas todas as URLs da especificação para assegurar apontam para a documentação atual
- **Validação de Conteúdo**: Validação abrangente das melhores práticas de segurança contra os padrões mais recentes
  - **Soluções Microsoft Security**: Terminologia e links atuais verificados para Prompt Shields (anteriormente "detecção de risco jailbreak"), Azure Content Safety, Microsoft Entra ID e Azure Key Vault
  - **Segurança OAuth 2.1**: Confirmada conformidade com as melhores práticas de segurança OAuth mais recentes
  - **Padrões OWASP**: Validada atualidade das referências OWASP Top 10 para LLMs
  - **Serviços Azure**: Verificados todos os links da documentação Microsoft Azure e melhores práticas
- **Alinhamento de Padrões**: Todos os padrões de segurança referenciados confirmados como atuais
  - Quadro de Gestão de Riscos de IA do NIST
  - ISO 27001:2022
  - Melhores Práticas de Segurança OAuth 2.1
  - Quadros de segurança e conformidade do Azure
- **Recursos de Implementação**: Verificados todos os links de guias de implementação e recursos
  - Padrões de autenticação do Azure API Management
  - Guias de integração Microsoft Entra ID
  - Gestão de segredos Azure Key Vault
  - Pipelines DevSecOps e soluções de monitorização

### Garantia de Qualidade da Documentação
- **Conformidade com Especificação**: Garantido que todos os requisitos obrigatórios de segurança MCP (MUST/MUST NOT) alinham com a especificação mais recente
- **Atualização de Recursos**: Verificados todos os links externos para documentação Microsoft, padrões de segurança e guias de implementação
- **Cobertura de Melhores Práticas**: Confirmada cobertura abrangente de autenticação, autorização, ameaças específicas de IA, segurança da cadeia de fornecimento e padrões empresariais

## 6 de outubro de 2025

### Expansão da Secção Introdução – Utilização Avançada do Servidor & Autenticação Simples

#### Utilização Avançada do Servidor (03-GettingStarted/10-advanced)
- **Novo Capítulo Adicionado**: Introduzido um guia completo para uso avançado do servidor MCP, cobrindo arquiteturas de servidor regular e de baixo nível.
  - **Servidor Regular vs. Baixo Nível**: Comparação detalhada e exemplos de código em Python e TypeScript para ambas abordagens.
  - **Design Baseado em Handlers**: Explicação da gestão de ferramentas/recursos/prompts baseada em handlers para implementações escaláveis e flexíveis de servidores.
  - **Padrões Práticos**: Cenários reais onde padrões de servidor de baixo nível são benéficos para funcionalidades avançadas e arquitetura.

#### Autenticação Simples (03-GettingStarted/11-simple-auth)
- **Novo Capítulo Adicionado**: Guia passo a passo para implementar autenticação simples em servidores MCP.
  - **Conceitos de Autenticação**: Explicação clara sobre autenticação vs. autorização e manuseamento de credenciais.
  - **Implementação de Autenticação Básica**: Padrões de autenticação via middleware em Python (Starlette) e TypeScript (Express), com exemplos de código.
  - **Progressão para Segurança Avançada**: Orientação para começar com autenticação simples e avançar para OAuth 2.1 e RBAC, com referências a módulos avançados de segurança.

Estas adições oferecem orientações práticas e mão na massa para construir implementações de servidor MCP mais robustas, seguras e flexíveis, ligando conceitos fundamentais com padrões avançados de produção.

## 29 de setembro de 2025

### Laboratórios de Integração de Base de Dados MCP Server - Caminho Completo de Aprendizagem Prática

#### 11-MCPServerHandsOnLabs - Novo Currículo Completo de Integração de Base de Dados
- **Caminho de Aprendizagem com 13 Laboratórios**: Adicionado currículo prático abrangente para construção de servidores MCP prontos para produção com integração de base de dados PostgreSQL
  - **Implementação Real**: Caso de uso de análises Zava Retail demonstrando padrões empresariais avançados
  - **Progressão Estruturada de Aprendizagem**:
    - **Laboratórios 00-03: Fundamentos** - Introdução, Arquitectura Central, Segurança & Multi-Inquilinato, Configuração do Ambiente
    - **Laboratórios 04-06: Construção do Servidor MCP** - Design & Esquema da Base de Dados, Implementação do Servidor MCP, Desenvolvimento de Ferramentas  
    - **Laboratórios 07-09: Funcionalidades Avançadas** - Integração de Pesquisa Semântica, Testes & Depuração, Integração VS Code
    - **Laboratórios 10-12: Produção & Boas Práticas** - Estratégias de Desdobramento, Monitorização & Observabilidade, Boas Práticas & Otimização
  - **Tecnologias Empresariais**: Framework FastMCP, PostgreSQL com pgvector, embeddings Azure OpenAI, Azure Container Apps, Application Insights
  - **Funcionalidades Avançadas**: Segurança a nível de linha (RLS), pesquisa semântica, acesso de dados multi-inquilino, embeddings vetoriais, monitorização em tempo real

#### Padronização de Terminologia - Conversão de Módulo para Laboratório
- **Atualização Abrangente da Documentação**: Atualizados sistematicamente todos os ficheiros README em 11-MCPServerHandsOnLabs para usar terminologia "Laboratório" em vez de "Módulo"
  - **Cabeçalhos de Secção**: Atualizado "O que este Módulo Cobre" para "O que este Laboratório Cobre" em todos os 13 laboratórios
  - **Descrição do Conteúdo**: Alterado "Este módulo fornece..." para "Este laboratório fornece..." em toda a documentação
  - **Objetivos de Aprendizagem**: Atualizado "Ao final deste módulo..." para "Ao final deste laboratório..." 
  - **Links de Navegação**: Convertidas todas referências "Módulo XX:" para "Laboratório XX:" em referências cruzadas e navegação
  - **Rastreamento de Conclusão**: Atualizado "Após completar este módulo..." para "Após completar este laboratório..."
  - **Referências Técnicas Preservadas**: Mantidas referências a módulos Python em ficheiros de configuração (ex., `"module": "mcp_server.main"`)

#### Aprimoramento do Guia de Estudo (study_guide.md)
- **Mapa Visual do Currículo**: Adicionada nova secção "11. Laboratórios de Integração de Base de Dados" com visualização abrangente da estrutura dos laboratórios
- **Estrutura do Repositório**: Atualizada de dez para onze secções principais com descrição detalhada de 11-MCPServerHandsOnLabs
- **Orientação do Caminho de Aprendizagem**: Melhoradas instruções de navegação para cobrir secções 00-11
- **Cobertura Tecnológica**: Adicionadas informações sobre integração FastMCP, PostgreSQL e serviços Azure
- **Resultados de Aprendizagem**: Enfatizado desenvolvimento de servidores prontos para produção, integração de base de dados, e segurança empresarial

#### Aprimoramento da Estrutura do README Principal
- **Terminologia Baseada em Laboratório**: Atualizado README.md principal em 11-MCPServerHandsOnLabs para usar consistentemente estrutura "Laboratório"
- **Organização do Caminho de Aprendizagem**: Progressão clara desde conceitos fundamentais até implementação avançada e desdobramento em produção
- **Foco Realista**: Ênfase no aprendizado prático e mão na massa com padrões e tecnologias de nível empresarial

### Melhorias de Qualidade & Consistência da Documentação
- **Ênfase na Aprendizagem Prática**: Reforço da abordagem prática baseada em laboratórios em toda a documentação
- **Foco em Padrões Empresariais**: Destacado implementações prontas para produção e considerações de segurança empresarial
- **Integração Tecnológica**: Cobertura abrangente de serviços Azure modernos e padrões de integração IA
- **Progressão de Aprendizagem**: Caminho claro e estruturado dos conceitos básicos ao desdobramento em produção

## 26 de setembro de 2025

### Aprimoramento dos Estudos de Caso - Integração do Registo MCP no GitHub

#### Estudos de Caso (09-CaseStudy/) - Foco no Desenvolvimento do Ecossistema
- **README.md**: Expansão significativa com estudo de caso abrangente do Registo MCP do GitHub
  - **Estudo de Caso Registo MCP do GitHub**: Novo estudo detalhado examinando o lançamento do Registo MCP do GitHub em setembro de 2025
    - **Análise do Problema**: Exame detalhado dos desafios fragmentados de descoberta e desdobramento de servidores MCP
    - **Arquitetura da Solução**: Abordagem do registo centralizado do GitHub com instalação VS Code com um clique
    - **Impacto nos Negócios**: Melhorias mensuráveis na integração e produtividade dos desenvolvedores
    - **Valor Estratégico**: Foco no desdobramento modular de agentes e interoperabilidade entre ferramentas
    - **Desenvolvimento do Ecossistema**: Posicionamento como plataforma fundamental para integração agentiva
  - **Estrutura Melhorada do Estudo de Caso**: Atualizados todos os sete estudos de caso com formatação consistente e descrições abrangentes
    - Agentes de Viagens Azure AI: Ênfase na orquestração multiagente
    - Integração Azure DevOps: Foco na automação de fluxos de trabalho
    - Recuperação de Documentação em Tempo Real: Implementação de cliente de consola Python
    - Gerador Interativo de Planos de Estudo: Aplicação web conversacional Chainlit
    - Documentação no Editor: Integração VS Code e GitHub Copilot
    - Azure API Management: Padrões de integração de API empresariais
    - Registo MCP GitHub: Desenvolvimento do ecossistema e plataforma comunitária
  - **Conclusão Abrangente**: Seção de conclusão reescrita destacando sete estudos de caso que abrangem múltiplas dimensões de implementação MCP
    - Integração Empresarial, Orquestração Multi-Agente, Produtividade do Desenvolvedor
    - Desenvolvimento do Ecossistema, Categorias de Aplicações Educativas
    - Insights aprimorados sobre padrões arquitetónicos, estratégias de implementação e melhores práticas
    - Ênfase no MCP como protocolo maduro e pronto para produção

#### Atualizações do Guia de Estudo (study_guide.md)
- **Mapa Visual do Currículo**: Atualizado mapa mental para incluir Registo MCP do GitHub na secção Estudos de Caso
- **Descrição dos Estudos de Caso**: Melhoradas de descrições genéricas para detalhada discriminação de sete estudos de caso abrangentes
- **Estrutura do Repositório**: Seção 10 atualizada para refletir cobertura abrangente dos estudos de caso com detalhes específicos de implementação
- **Integração do Changelog**: Entrada de 26 de setembro de 2025 adicionada documentando a inserção do Registo MCP do GitHub e melhorias nos estudos de caso
- **Atualizações de Data**: Rodapé atualizado para refletir a última revisão (26 de setembro de 2025)

### Melhorias na Qualidade da Documentação
- **Aprimoramento da Consistência**: Padronização de formatação e estrutura dos estudos de caso nos sete exemplos
- **Cobertura Abrangente**: Estudos de caso agora abrangem cenários empresariais, produtividade de desenvolvedor e desenvolvimento do ecossistema
- **Posicionamento Estratégico**: Enfoque melhorado no MCP como plataforma fundamental para o desdobramento de sistemas agentivos
- **Integração de Recursos**: Atualizados recursos adicionais para incluir link do Registo MCP do GitHub

## 15 de setembro de 2025

### Expansão de Tópicos Avançados - Transportes Personalizados & Engenharia de Contexto

#### Transportes Personalizados MCP (05-AdvancedTopics/mcp-transport/) - Novo Guia de Implementação Avançada
- **README.md**: Guia de implementação completa para mecanismos de transporte MCP personalizados
  - **Transporte Azure Event Grid**: Implementação completa de transporte orientado a eventos serverless
    - Exemplos em C#, TypeScript e Python com integração Azure Functions
    - Padrões de arquitetura orientada a eventos para soluções MCP escaláveis
    - Receptores webhook e manuseio de mensagens push
  - **Transporte Azure Event Hubs**: Implementação de transporte streaming de alta vazão
    - Capacidades de streaming em tempo real para cenários de baixa latência
    - Estratégias de particionamento e gestão de pontos de verificação
    - Agrupamento de mensagens e otimização de desempenho
  - **Padrões de Integração Empresariais**: Exemplos de arquitetura prontos para produção
    - Processamento MCP distribuído por múltiplas Azure Functions
    - Arquiteturas híbridas de transporte combinando múltiplos tipos de transporte
    - Durabilidade de mensagens, fiabilidade e estratégias de tratamento de erros
  - **Segurança & Monitorização**: Integração Azure Key Vault e padrões de observabilidade
    - Autenticação com identidade gerida e acesso de menor privilégio
    - Telemetria Application Insights e monitorização de desempenho
    - Circuit breakers e padrões de tolerância a falhas
  - **Frameworks de Teste**: Estratégias abrangentes de testes para transportes personalizados
    - Testes unitários com test doubles e frameworks de mocking
    - Testes de integração com Azure Test Containers
    - Considerações para testes de desempenho e carga

#### Engenharia de Contexto (05-AdvancedTopics/mcp-contextengineering/) - Disciplina Emergente de IA
- **README.md**: Exploração abrangente de engenharia de contexto enquanto campo emergente
  - **Princípios Fundamentais**: Partilha completa de contexto, consciência na tomada de decisão de ações, e gestão da janela de contexto

  - **Alinhamento do Protocolo MCP**: Como o design do MCP aborda desafios de engenharia de contexto
    - Limitações da janela de contexto e estratégias de carregamento progressivo
    - Determinação de relevância e recuperação dinâmica de contexto
    - Gestão de contexto multimodal e considerações de segurança
  - **Abordagens de Implementação**: Arquiteturas single-threaded vs. multi-agente
    - Técnicas de fragmentação e priorização de contexto
    - Estratégias de carregamento progressivo e compressão de contexto
    - Abordagens de contexto em camadas e otimização de recuperação
  - **Estrutura de Medição**: Métricas emergentes para avaliação da eficácia do contexto
    - Eficiência de entrada, desempenho, qualidade e considerações de experiência do utilizador
    - Abordagens experimentais para otimização de contexto
    - Análise de falhas e metodologias de melhoria

#### Atualizações na Navegação do Currículo (README.md)
- **Estrutura do Módulo Melhorada**: Tabela de currículo atualizada para incluir novos tópicos avançados
  - Adicionadas entradas de Engenharia de Contexto (5.14) e Transporte Personalizado (5.15)
  - Formatação consistente e links de navegação em todos os módulos
  - Descrições atualizadas para refletir o escopo atual do conteúdo

### Melhorias na Estrutura de Diretórios
- **Padronização dos Nomes**: Renomeado "mcp transport" para "mcp-transport" para consistência com outras pastas de tópicos avançados
- **Organização do Conteúdo**: Todas as pastas 05-AdvancedTopics agora seguem padrão consistente de nomeação (mcp-[topic])

### Melhorias na Qualidade da Documentação
- **Alinhamento com a Especificação MCP**: Todo o conteúdo novo referencia a Especificação MCP 2025-06-18 atual
- **Exemplos Multilíngues**: Exemplos abrangentes em C#, TypeScript e Python
- **Foco Empresarial**: Padrões prontos para produção e integração com a nuvem Azure em toda a documentação
- **Documentação Visual**: Diagramas Mermaid para visualização de arquitetura e fluxos

## 18 de agosto de 2025

### Atualização Abrangente da Documentação - Normas MCP 2025-06-18

#### Melhores Práticas de Segurança MCP (02-Security/) - Modernização Completa
- **MCP-SECURITY-BEST-PRACTICES-2025.md**: Reescrita completa alinhada com a Especificação MCP 2025-06-18
  - **Requisitos Obrigatórios**: Adicionados requisitos explícitos DEVE/ NÃO DEVE da especificação oficial com indicadores visuais claros
  - **12 Práticas de Segurança Principais**: Reestruturado de lista de 15 itens para domínios de segurança abrangentes
    - Segurança de Token e Autenticação com integração de fornecedor de identidade externo
    - Gestão de Sessão e Segurança de Transporte com requisitos criptográficos
    - Proteção de Ameaças Específicas para IA com integração Microsoft Prompt Shields
    - Controlo de Acesso e Permissões com princípio do menor privilégio
    - Segurança e Monitorização de Conteúdo com integração Azure Content Safety
    - Segurança da Cadeia de Fornecimento com verificação abrangente de componentes
    - Segurança OAuth e Prevenção de Confusion Delegate com implementação PKCE
    - Resposta a Incidentes e Recuperação com capacidades automatizadas
    - Conformidade e Governança com alinhamento regulatório
    - Controlo de Segurança Avançado com arquitetura zero trust
    - Integração no Ecossistema de Segurança Microsoft com soluções abrangentes
    - Evolução Contínua de Segurança com práticas adaptativas
  - **Soluções de Segurança Microsoft**: Orientação avançada para integração de Prompt Shields, Azure Content Safety, Entra ID e GitHub Advanced Security
  - **Recursos de Implementação**: Links de recursos abrangentes categorizados por Documentação Oficial MCP, Soluções Microsoft de Segurança, Normas de Segurança e Guias de Implementação

#### Controlo Avançado de Segurança (02-Security/) - Implementação Empresarial
- **MCP-SECURITY-CONTROLS-2025.md**: Revisão completa com framework de segurança de nível empresarial
  - **9 Domínios de Segurança Abrangentes**: Expandido de controlos básicos para framework detalhado empresarial
    - Autenticação e Autorização Avançadas com integração Microsoft Entra ID
    - Segurança de Token e Controlos Anti-Passthrough com validação abrangente
    - Controlos de Segurança de Sessão com prevenção de sequestro
    - Controlos de Segurança Específicos para IA com prevenção de injeção de prompt e envenenamento de ferramentas
    - Prevenção de Ataques Confused Deputy com segurança de proxy OAuth
    - Segurança na Execução de Ferramentas com sandboxing e isolamento
    - Controlos de Segurança da Cadeia de Fornecimento com verificação de dependências
    - Controlos de Monitorização e Deteção com integração SIEM
    - Resposta a Incidentes e Recuperação com capacidades automatizadas
  - **Exemplos de Implementação**: Adicionados blocos de configuração YAML detalhados e exemplos de código
  - **Integração de Soluções Microsoft**: Cobertura abrangente de serviços de segurança Azure, GitHub Advanced Security e gestão empresarial de identidade

#### Segurança em Tópicos Avançados (05-AdvancedTopics/mcp-security/) - Implementação Pronta para Produção
- **README.md**: Reescrita completa para implementação empresarial de segurança
  - **Alinhamento com Especificação Atual**: Atualizado para Especificação MCP 2025-06-18 com requisitos de segurança obrigatórios
  - **Autenticação Reforçada**: Integração Microsoft Entra ID com exemplos completos em .NET e Java Spring Security
  - **Integração de Segurança IA**: Implementação de Microsoft Prompt Shields e Azure Content Safety com exemplos detalhados em Python
  - **Mitigação Avançada de Ameaças**: Exemplos abrangentes de implementação para
    - Prevenção de Ataques Confused Deputy com PKCE e validação de consentimento do utilizador
    - Prevenção de Passthrough de Token com validação de audiência e gestão segura de token
    - Prevenção de Sequestro de Sessão com ligação criptográfica e análise comportamental
  - **Integração de Segurança Empresarial**: Monitorização Azure Application Insights, pipelines de deteção de ameaças e segurança de cadeia de fornecimento
  - **Lista de Verificação de Implementação**: Clarificação dos controlos obrigatórios vs. recomendados com benefícios do ecossistema de segurança Microsoft

### Qualidade e Alinhamento de Normas da Documentação
- **Referências da Especificação**: Atualizadas todas as referências para a atual Especificação MCP 2025-06-18
- **Ecossistema de Segurança Microsoft**: Orientação aprimorada de integração em toda a documentação de segurança
- **Implementação Prática**: Adicionados exemplos detalhados de código em .NET, Java e Python com padrões empresariais
- **Organização de Recursos**: Categorização abrangente de documentação oficial, padrões de segurança e guias de implementação
- **Indicadores Visuais**: Marcação clara de requisitos obrigatórios vs. práticas recomendadas


#### Conceitos Fundamentais (01-CoreConcepts/) - Modernização Completa
- **Atualização da Versão do Protocolo**: Atualizado para referenciar a atual Especificação MCP 2025-06-18 com versionamento baseado em data (formato AAAA-MM-DD)
- **Refinamento da Arquitetura**: Descrições melhoradas de Hosts, Clientes e Servidores para refletir padrões atuais de arquitetura MCP
  - Hosts agora claramente definidos como aplicações IA que coordenam múltiplas conexões de clientes MCP
  - Clientes descritos como conectores de protocolo mantendo relações um-para-um com servidores
  - Servidores aprimorados com cenários de implantação local vs. remota
- **Reestruturação de Primitivas**: Revisão completa das primitivas de servidor e cliente
  - Primitivas de Servidor: Recursos (fontes de dados), Prompts (modelos), Ferramentas (funções executáveis) com explicações e exemplos detalhados
  - Primitivas de Cliente: Amostragem (completions LLM), Elicitação (entrada do utilizador), Logging (depuração/monitorização)
  - Atualizado com padrões atuais de métodos de descoberta (`*/list`), recuperação (`*/get`) e execução (`*/call`)
- **Arquitetura do Protocolo**: Introdução do modelo de arquitetura em duas camadas
  - Camada de Dados: Fundação JSON-RPC 2.0 com gestão do ciclo de vida e primitivas
  - Camada de Transporte: mecanismos de transporte STDIO (local) e Streamable HTTP com SSE (remoto)
- **Framework de Segurança**: Princípios abrangentes de segurança incluindo consentimento explícito do utilizador, proteção de privacidade de dados, segurança na execução de ferramentas e segurança da camada de transporte
- **Padrões de Comunicação**: Mensagens do protocolo atualizadas para mostrar fluxos de inicialização, descoberta, execução e notificação
- **Exemplos de Código**: Atualização dos exemplos multilíngues (.NET, Java, Python, JavaScript) para refletir padrões atuais do SDK MCP

#### Segurança (02-Security/) - Revisão Abrangente de Segurança  
- **Alinhamento com Normas**: Total alinhamento com requisitos de segurança da Especificação MCP 2025-06-18
- **Evolução da Autenticação**: Documentação da evolução de servidores OAuth personalizados para delegação via fornecedor de identidade externo (Microsoft Entra ID)
- **Análise de Ameaças Específicas para IA**: Cobertura aprimorada de vetores modernos de ataque IA
  - Cenários detalhados de ataques de injeção de prompt com exemplos reais
  - Mecanismos de envenenamento de ferramentas e padrões de ataques tipo “rug pull”
  - Envenenamento da janela de contexto e ataques de confusão de modelo
- **Soluções Microsoft de Segurança IA**: Cobertura abrangente do ecossistema de segurança Microsoft
  - AI Prompt Shields com técnicas avançadas de deteção, realce e delimitadores
  - Padrões de integração Azure Content Safety
  - GitHub Advanced Security para proteção da cadeia de fornecimento
- **Mitigação Avançada de Ameaças**: Controlos detalhados de segurança para
  - Sequestro de sessão com cenários de ataque específicos MCP e requisitos criptográficos de ID de sessão
  - Problemas de deputy confundido em cenários de proxy MCP com requisitos explícitos de consentimento
  - Vulnerabilidades de passthrough de token com controlos obrigatórios de validação
- **Segurança da Cadeia de Fornecimento**: Expansão da cobertura de cadeia de fornecimento IA incluindo modelos base, serviços de embeddings, provedores de contexto e APIs de terceiros
- **Segurança da Fundação**: Integração aprimorada com padrões de segurança empresarial incluindo arquitetura zero trust e ecossistema Microsoft
- **Organização de Recursos**: Links abrangentes de recursos categorizados por tipo (Docs Oficiais, Normas, Investigação, Soluções Microsoft, Guias de Implementação)

### Melhorias na Qualidade da Documentação
- **Objetivos de Aprendizagem Estruturados**: Melhoria dos objetivos com resultados específicos e acionáveis
- **Referências Cruzadas**: Adição de links entre tópicos relacionados de segurança e conceitos fundamentais
- **Informação Atual**: Atualização de todas as referências de data e links para especificações atuais
- **Orientação de Implementação**: Inclusão de diretrizes específicas e acionáveis em ambas as secções

## 16 de julho de 2025

### Melhorias no README e Navegação
- Navegação do currículo completamente redesenhada no README.md
- Etiquetas `<details>` substituídas por formato baseado em tabelas mais acessível
- Criadas opções de layout alternativas na nova pasta "alternative_layouts"
- Adicionados exemplos de navegação em estilo cartão, tabulação e acordeão
- Atualizada a seção de estrutura do repositório para incluir todos os arquivos mais recentes
- Melhorada a seção "Como Usar Este Currículo" com recomendações claras
- Atualizados links da especificação MCP para apontar para URLs corretos
- Adicionada a seção de Engenharia de Contexto (5.14) na estrutura do currículo

### Atualizações do Guia de Estudo
- Guia de estudo completamente revisto para alinhar com a estrutura atual do repositório
- Adicionadas novas secções para Clientes MCP e Ferramentas, e Servidores MCP Populares
- Atualizado o Mapa Visual do Currículo para refletir acuradamente todos os tópicos
- Melhoradas as descrições dos Tópicos Avançados para cobrir todas as áreas especializadas
- Atualizada a secção de Estudos de Caso para refletir exemplos reais
- Adicionado este changelog abrangente

### Contribuições da Comunidade (06-CommunityContributions/)
- Adicionadas informações detalhadas sobre servidores MCP para geração de imagens
- Adicionada secção abrangente sobre utilização do Claude no VSCode
- Adicionadas instruções de configuração e uso do cliente terminal Cline
- Atualizada a secção de clientes MCP para incluir todas as opções populares
- Melhoria dos exemplos de contribuição com amostras de código mais precisas

### Tópicos Avançados (05-AdvancedTopics/)
- Organização de todas as pastas de tópicos especializados com nomeação consistente
- Adicionados materiais e exemplos de engenharia de contexto
- Adicionada documentação de integração do agente Foundry
- Melhorada documentação de integração de segurança Entra ID

## 11 de junho de 2025

### Criação Inicial
- Lançada primeira versão do currículo MCP para Principiantes
- Criada estrutura básica para as 10 secções principais
- Implementado Mapa Visual do Currículo para navegação
- Adicionados projetos amostra iniciais em várias linguagens de programação

### Começando (03-GettingStarted/)
- Criados primeiros exemplos de implementação de servidor
- Adicionadas orientações para desenvolvimento de clientes
- Inclusas instruções de integração de cliente LLM
- Adicionada documentação de integração no VS Code
- Implementados exemplos de servidor com Server-Sent Events (SSE)

### Conceitos Fundamentais (01-CoreConcepts/)
- Adicionada explicação detalhada da arquitetura cliente-servidor
- Criada documentação sobre componentes chave do protocolo
- Documentados os padrões de mensagens no MCP

## 23 de maio de 2025

### Estrutura do Repositório
- Inicializado repositório com estrutura básica de pastas
- Criados ficheiros README para cada secção principal
- Configurada infraestrutura de tradução
- Adicionados recursos visuais e diagramas

### Documentação
- Criado README.md inicial com visão geral do currículo
- Adicionados ficheiros CODE_OF_CONDUCT.md e SECURITY.md
- Configurado SUPPORT.md com orientações para obtenção de ajuda
- Criada estrutura preliminar do guia de estudo

## 15 de abril de 2025

### Planeamento e Framework
- Planeamento inicial para o currículo MCP para Principiantes
- Definidos objetivos de aprendizagem e público-alvo
- Estruturada a organização em 10 secções do currículo
- Desenvolvido framework conceptual para exemplos e estudos de caso
- Criados exemplos protótipo iniciais para conceitos chave

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas resultantes da utilização desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->