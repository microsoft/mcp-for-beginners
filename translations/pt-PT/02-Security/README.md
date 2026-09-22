# Segurança MCP: Proteção Abrangente para Sistemas de IA

[![Práticas Recomendadas de Segurança MCP](../../../translated_images/pt-PT/03.175aed6dedae133f.webp)](https://youtu.be/88No8pw706o)

_(Clique na imagem acima para ver o vídeo desta lição)_

A segurança é fundamental no design de sistemas de IA, razão pela qual a priorizamos como a nossa segunda secção. Isto está alinhado com o princípio **Secure by Design** da Microsoft da [Secure Future Initiative](https://www.microsoft.com/security/blog/2025/04/17/microsofts-secure-by-design-journey-one-year-of-success/).

O Protocolo de Contexto de Modelo (MCP) traz capacidades poderosas para aplicações conduzidas por IA enquanto introduz desafios de segurança únicos que vão além dos riscos tradicionais de software. Os sistemas MCP enfrentam preocupações de segurança estabelecidas (codificação segura, mínimo privilégio, segurança da cadeia de fornecimento) e novas ameaças específicas de IA, incluindo injeção de prompts, envenenamento de ferramentas, sequestro de sessão, ataques de procurador confuso, vulnerabilidades de passagem de token e modificação dinâmica de capacidades.

Esta lição explora os riscos de segurança mais críticos nas implementações MCP—cobrindo autenticação, autorização, permissões excessivas, injeção indireta de prompts, segurança de sessões, problemas de procurador confuso, gestão de tokens e vulnerabilidades na cadeia de fornecimento. Aprenderá controlos práticos e melhores práticas para mitigar estes riscos enquanto aproveita soluções Microsoft como Prompt Shields, Azure Content Safety e GitHub Advanced Security para fortalecer a sua implementação MCP.

## Objetivos de Aprendizagem

No final desta lição, será capaz de:

- **Identificar Ameaças Específicas MCP**: Reconhecer riscos de segurança únicos em sistemas MCP incluindo injeção de prompt, envenenamento de ferramentas, permissões excessivas, sequestro de sessão, problemas de procurador confuso, vulnerabilidades de passagem de token e riscos na cadeia de fornecimento
- **Aplicar Controlos de Segurança**: Implementar mitigações eficazes incluindo autenticação robusta, acesso de mínimo privilégio, gestão segura de tokens, controlos de segurança de sessão e verificação da cadeia de fornecimento
- **Aproveitar Soluções de Segurança Microsoft**: Compreender e implementar Microsoft Prompt Shields, Azure Content Safety e GitHub Advanced Security para proteção da carga de trabalho MCP
- **Validar Segurança das Ferramentas**: Reconhecer a importância da validação de metadados das ferramentas, monitorização de alterações dinâmicas e defesa contra ataques indiretos de injeção de prompt
- **Integrar Melhores Práticas**: Combinar fundamentos de segurança estabelecidos (codificação segura, endurecimento de servidores, zero trust) com controlos específicos MCP para proteção abrangente

# Arquitectura e Controlos de Segurança MCP

As implementações modernas MCP requerem abordagens de segurança em camadas que abordam tanto a segurança tradicional de software quanto as ameaças específicas de IA. A especificação MCP em rápida evolução continua a amadurecer seus controlos de segurança, permitindo melhor integração com arquitecturas de segurança empresarial e práticas recomendadas estabelecidas.

A pesquisa do [Microsoft Digital Defense Report](https://aka.ms/mddr) demonstra que **98% das violações reportadas seriam prevenidas por higiene robusta de segurança**. A estratégia de proteção mais eficaz combina práticas de segurança fundamentais com controlos específicos MCP—medidas base de segurança comprovadas continuam a ser as mais impactantes na redução do risco global.

## Panorama Actual de Segurança

> **Nota:** Este capítulo combina controlos de segurança MCP estabelecidos com a
> actual orientação de **autorização da Especificação MCP 2026-07-28**. Consulte sempre
> a actual [Especificação MCP](https://modelcontextprotocol.io/specification/2026-07-28/),
> [repositório GitHub MCP](https://github.com/modelcontextprotocol) e a
> [documentação de melhores práticas de segurança](https://modelcontextprotocol.io/specification/2026-07-28/basic/security_best_practices)
> ao implementar código sensível à segurança.

> **Atualização de autorização:** A MCP `2026-07-28` exige que os clientes validem o
> parâmetro `iss` nas respostas de autorização (RFC 9207) e vinculem credenciais
> registadas ao servidor de autorização emissor. A Registo Dinâmico de Clientes
> está obsoleta; novas implementações devem usar Documentos de Metadados de ID de Cliente.
> Veja [O que mudou no MCP: A especificação 2026-07-28](../01-CoreConcepts/mcp-2026-07-28.md)
> para a lista completa de alterações de autorização.

## 🏔️ Workshop MCP Security Summit (Sherpa)

Para **formação prática em segurança**, recomendamos vivamente o **Workshop MCP Security Summit** (Sherpa) - uma expedição guiada abrangente para assegurar servidores MCP na Microsoft Azure.

### Visão Geral do Workshop

O [Workshop MCP Security Summit](https://azure-samples.github.io/sherpa/) oferece formação prática e acionável de segurança através de uma metodologia comprovada "vulnerável → explorar → corrigir → validar". Você irá:

- **Aprender a quebrar sistemas**: Experimentar vulnerabilidades em primeira mão explorando servidores propositadamente inseguros
- **Usar Segurança Nativa Azure**: Aproveitar Azure Entra ID, Key Vault, API Management e AI Content Safety
- **Seguir Defesa em Profundidade**: Progredir através de bases que constroem camadas abrangentes de segurança
- **Aplicar Normas OWASP**: Cada técnica corresponde ao [Guia de Segurança MCP Azure OWASP](https://microsoft.github.io/mcp-azure-security-guide/)
- **Obter Código de Produção**: Sair com implementações funcionais e testadas

### Rota da Expedição

| Base | Foco | Riscos OWASP Cobertos |
|------|-------|---------------------|
| **Acampamento Base** | Fundamentos MCP & vulnerabilidades de autenticação | MCP01, MCP07 |
| **Acampamento 1: Identidade** | OAuth 2.1, Azure Managed Identity, Key Vault | MCP01, MCP02, MCP07 |
| **Acampamento 2: Gateway** | Gestão de API, Endpoints Privados, governação | MCP02, MCP06, MCP07, MCP09 |
| **Acampamento 3: Segurança de I/O** | Injeção de prompt, proteção de PII, segurança de conteúdo | MCP03, MCP05, MCP06, MCP10 |
| **Acampamento 4: Monitorização** | Log Analytics, painéis, deteção de ameaças | MCP04, MCP08 |
| **O Cume** | Teste integrado Red Team / Blue Team | Todos |

**Começar**: [https://azure-samples.github.io/sherpa/](https://azure-samples.github.io/sherpa/)

## Top 10 Riscos de Segurança OWASP MCP

O [Guia de Segurança MCP Azure OWASP](https://microsoft.github.io/mcp-azure-security-guide/) detalha os dez riscos de segurança mais críticos para implementações MCP:

| Risco | Descrição | Mitigação Azure |
|------|-------------|------------------|
| **MCP01** | Má Gestão de Tokens & Exposição de Segredos | Azure Key Vault, Managed Identity |
| **MCP02** | Escalada de Privilégios via Scope Creep | RBAC, Acesso Condicional |
| **MCP03** | Envenenamento de Ferramentas | Validação de ferramentas, verificação de integridade |
| **MCP04** | Ataques à Cadeia de Fornecimento de Software & Manipulação de Dependências | GitHub Advanced Security, análise de dependências |
| **MCP05** | Injeção e Execução de Comandos | Validação de entrada, sandboxing |
| **MCP06** | Subversão do Fluxo Intencional | Azure AI Content Safety, Prompt Shields |
| **MCP07** | Autenticação & Autorização Insuficientes | Azure Entra ID, OAuth 2.1 com PKCE |
| **MCP08** | Falta de Auditoria e Telemetria | Azure Monitor, Application Insights |
| **MCP09** | Servidores MCP Sombra | Governação do API Center, isolamento de rede |
| **MCP10** | Injeção de Contexto & Exposição Excessiva | Classificação de dados, exposição mínima |

### Evolução da Autenticação MCP

A especificação MCP evoluiu significativamente na abordagem à autenticação e autorização:

- **Abordagem Original**: Especificações iniciais exigiam que os desenvolvedores implementassem servidores de autenticação personalizados, com servidores MCP a atuar como Servidores de Autorização OAuth 2.0 gerindo diretamente a autenticação de utilizadores
- **Padrão Atual (`2026-07-28`)**: Os servidores MCP podem delegar a autenticação
  a fornecedores externos de identidade como o Microsoft Entra ID. Os clientes devem também
  aplicar os requisitos actuais de validação do emissor e vinculação de credenciais.
- **Segurança de Camada de Transporte**: Suporte aprimorado para mecanismos de transporte seguro com padrões de autenticação adequados para conexões locais (STDIO) e remotas (Streamable HTTP)

## Segurança de Autenticação & Autorização

### Desafios Actuais de Segurança

As implementações modernas MCP enfrentam vários desafios de autenticação e autorização:

### Riscos & Vetores de Ameaça

- **Lógica de Autorização Mal Configurada**: Implementação falhada de autorização em servidores MCP pode expor dados sensíveis e aplicar incorretamente controlos de acesso
- **Comprometimento de Token OAuth**: Roubo de tokens em servidores MCP locais permite aos atacantes se fazerem passar por servidores e aceder a serviços a jusante
- **Vulnerabilidades de Passagem de Token**: Manuseamento incorreto de tokens cria bypasses de controlos de segurança e lacunas de responsabilidade
- **Permissões Excessivas**: Servidores MCP com privilégios excessivos violam o princípio de mínimo privilégio e expandem superfícies de ataque

#### Passagem de Token: Um Anti-Padrão Crítico

**A passagem de token é explicitamente proibida** na especificação atual de autorização MCP devido a implicações graves de segurança:

##### Circumvenção de Controlos de Segurança
- Servidores MCP e APIs a jusante implementam controlos críticos de segurança (limitação de taxa, validação de pedidos, monitorização de tráfego) que dependem de validação correta do token
- Uso direto de tokens cliente-API contorna estas proteções essenciais, minando a arquitectura de segurança

##### Desafios de Responsabilização & Auditoria  
- Servidores MCP não conseguem distinguir entre clientes usando tokens emitidos a montante, quebrando trilhas de auditoria
- Logs do servidor de recursos a jusante mostram origens de pedido enganosas em vez dos intermediários reais do servidor MCP
- A investigação de incidentes e auditoria de conformidade tornam-se significativamente mais difíceis

##### Riscos de Exfiltração de Dados
- Declarações de token não validadas permitem a atores maliciosos com tokens roubados usar servidores MCP como proxies para exfiltração de dados
- Violações da fronteira de confiança permitem padrões de acesso não autorizados que contornam controlos de segurança pretendidos

##### Vetores de Ataque Multi-Serviço
- Tokens comprometidos aceites por múltiplos serviços permitem movimento lateral através de sistemas conectados
- Suposições de confiança entre serviços podem ser violadas quando as origens de tokens não podem ser verificadas

### Controlos & Mitigações de Segurança

**Requisitos Críticos de Segurança:**

> **OBRIGATÓRIO**: Servidores MCP **NÃO DEVEM** aceitar quaisquer tokens que não tenham sido emitidos explicitamente para o servidor MCP

#### Controlos de Autenticação & Autorização

- **Revisão Rigorosa de Autorização**: Realizar auditorias abrangentes da lógica de autorização do servidor MCP para assegurar que apenas utilizadores e clientes pretendidos possam aceder a recursos sensíveis
  - **Guia de Implementação**: [Azure API Management como Gateway de Autenticação para Servidores MCP](https://techcommunity.microsoft.com/blog/integrationsonazureblog/azure-api-management-your-auth-gateway-for-mcp-servers/4402690)
  - **Integração de Identidade**: [Usar Microsoft Entra ID para Autenticação de Servidor MCP](https://den.dev/blog/mcp-server-auth-entra-id-session/)

- **Gestão Segura de Tokens**: Implementar [melhores práticas Microsoft para validação e ciclo de vida de token](https://learn.microsoft.com/en-us/entra/identity-platform/access-tokens)
  - Validar que as declarações del público do token correspondem à identidade do servidor MCP
  - Implementar políticas apropriadas de rotação e expiração de tokens
  - Prevenir ataques de repetição de token e uso não autorizado

- **Armazenamento Protegido de Tokens**: Armazenar tokens com encriptação em repouso e em trânsito
  - **Melhores Práticas**: [Diretrizes para Armazenamento Seguro de Tokens e Encriptação](https://youtu.be/uRdX37EcCwg?si=6fSChs1G4glwXRy2)

#### Implementação de Controlo de Acesso

- **Princípio do Mínimo Privilégio**: Conceder aos servidores MCP apenas as permissões mínimas necessárias para a funcionalidade pretendida
  - Revisões e atualizações regulares de permissões para evitar expansão de privilégios
  - **Documentação Microsoft**: [Acesso Seguro de Mínimo Privilégio](https://learn.microsoft.com/entra/identity-platform/secure-least-privileged-access)

- **Controle de Acesso Baseado em Funções (RBAC)**: Implementar atribuições granulares de funções
  - Ajustar os papéis estritamente para recursos e ações específicas
  - Evitar permissões amplas ou desnecessárias que ampliem superfícies de ataque

- **Monitorização Contínua de Permissões**: Implementar auditoria e monitorização contínua do acesso
  - Monitorizar padrões de uso de permissões para anomalias
  - Corrigir prontamente privilégios excessivos ou não usados

## Ameaças de Segurança Específicas à IA

### Ataques de Injeção de Prompt & Manipulação de Ferramentas

As implementações modernas MCP enfrentam vetores de ataque sofisticados específicos de IA que as medidas tradicionais de segurança não conseguem resolver completamente:

#### **Injeção Indireta de Prompt (Injeção de Prompt Cross-Domain)**

**Injeção Indireta de Prompt** representa uma das vulnerabilidades mais críticas em sistemas IA habilitados para MCP. Os atacantes incorporam instruções maliciosas em conteúdos externos—documentos, páginas web, emails ou fontes de dados—que os sistemas IA processam posteriormente como comandos legítimos.

**Cenários de Ataque:**
- **Injeção baseada em documentos**: Instruções maliciosas escondidas em documentos processados que desencadeiam ações IA não intencionais
- **Exploração de conteúdo web**: Páginas web comprometidas contendo prompts incorporados que manipulam o comportamento da IA quando raspadas
- **Ataques baseados em email**: Prompts maliciosos em emails que fazem assistentes IA divulgarem informação ou executar ações não autorizadas
- **Contaminação de fonte de dados**: Bases de dados ou APIs comprometidos que servem conteúdo contaminado para sistemas IA

**Impacto no Mundo Real**: Estes ataques podem resultar em exfiltração de dados, violações de privacidade, geração de conteúdos prejudiciais e manipulação de interações de utilizadores. Para análise detalhada, veja [Prompt Injection no MCP (Simon Willison)](https://simonwillison.net/2025/Apr/9/mcp-prompt-injection/).

![Diagrama de Ataque de Injeção de Prompt](../../../translated_images/pt-PT/prompt-injection.ed9fbfde297ca877.webp)

#### **Ataques de Envenenamento de Ferramentas**

**Envenenamento de Ferramentas** visa os metadados que definem as ferramentas MCP, explorando como os LLMs interpretam as descrições e parâmetros das ferramentas para tomar decisões de execução.

**Mecanismos de Ataque:**
- **Manipulação de metadados**: Atacantes injetam instruções maliciosas em descrições de ferramentas, definições de parâmetros ou exemplos de uso
- **Instruções invisíveis**: Prompts escondidos nos metadados das ferramentas que são processados pelos modelos IA mas invisíveis para utilizadores humanos
- **Modificação dinâmica de ferramentas ("Rug Pulls")**: Ferramentas aprovadas pelos utilizadores são depois modificadas para executar ações maliciosas sem o conhecimento dos utilizadores
- **Injeção de parâmetros**: Conteúdo malicioso embutido nos esquemas de parâmetros das ferramentas que influenciam o comportamento do modelo


**Riscos de Servidores Alojados**: Servidores MCP remotos apresentam riscos elevados, pois as definições de ferramentas podem ser atualizadas após a aprovação inicial do utilizador, criando cenários onde ferramentas anteriormente seguras tornam-se maliciosas. Para uma análise abrangente, consulte [Ataques de Envenenamento de Ferramentas (Invariant Labs)](https://invariantlabs.ai/blog/mcp-security-notification-tool-poisoning-attacks).

![Diagrama do Ataque de Injeção de Ferramentas](../../../translated_images/pt-PT/tool-injection.3b0b4a6b24de6bef.webp)

#### **Vetores Adicionais de Ataque de IA**

- **Injeção de Prompt Entre Domínios (XPIA)**: Ataques sofisticados que aproveitam conteúdos de múltiplos domínios para contornar controlos de segurança
- **Modificação Dinâmica de Capacidades**: Alterações em tempo real às capacidades de ferramentas que escapam a avaliações iniciais de segurança
- **Envenenamento da Janela de Contexto**: Ataques que manipulam grandes janelas de contexto para esconder instruções maliciosas
- **Ataques de Confusão do Modelo**: Exploração das limitações do modelo para criar comportamentos imprevisíveis ou inseguros


### Impacto dos Riscos de Segurança da IA

**Consequências de Alto Impacto:**
- **Exfiltração de Dados**: Acesso não autorizado e roubo de dados sensíveis empresariais ou pessoais
- **Quebras de Privacidade**: Exposição de informação pessoal identificável (PII) e dados empresariais confidenciais  
- **Manipulação de Sistemas**: Modificações não intencionais em sistemas críticos e fluxos de trabalho
- **Roubo de Credenciais**: Comprometimento de tokens de autenticação e credenciais de serviço
- **Movimento Lateral**: Uso de sistemas IA comprometidos como pivôs para ataques mais abrangentes na rede

### Soluções de Segurança de IA da Microsoft

#### **Escudos de Prompt de IA: Proteção Avançada contra Ataques de Injeção**

Os **Escudos de Prompt de IA** da Microsoft oferecem defesa abrangente contra ataques de injeção de prompt diretos e indiretos através de múltiplas camadas de segurança:

##### **Mecanismos Centrais de Proteção:**

1. **Detecção Avançada & Filtragem**
   - Algoritmos de machine learning e técnicas de PNL detetam instruções maliciosas em conteúdos externos
   - Análise em tempo real de documentos, páginas web, emails e fontes de dados para ameaças embutidas
   - Compreensão contextual de padrões legítimos vs. maliciosos de prompts

2. **Técnicas de Realce**  
   - Distingue entre instruções do sistema confiável e entradas externas potencialmente comprometidas
   - Métodos de transformação de texto que aumentam a relevância do modelo enquanto isolam conteúdos maliciosos
   - Ajuda sistemas IA a manter hierarquia correta de instruções e ignorar comandos injetados

3. **Sistemas de Delimitadores & Marcação de Dados**
   - Definição explícita de fronteiras entre mensagens do sistema confiável e texto de entrada externo
   - Marcadores especiais destacam limites entre fontes de dados confiáveis e não confiáveis
   - Separação clara previne confusão de instruções e execução não autorizada de comandos

4. **Inteligência de Ameaças Contínua**
   - A Microsoft monitora continuamente padrões emergentes de ataque e atualiza defesas
   - Caça proativa a ameaças para identificar novas técnicas e vetores de injeção
   - Atualizações regulares do modelo de segurança para manter eficácia contra ameaças em evolução

5. **Integração com Segurança de Conteúdo do Azure**
   - Parte da suíte abrangente Azure AI Content Safety
   - Detecção adicional para tentativas de jailbreak, conteúdos prejudiciais e violações de políticas de segurança
   - Controlos de segurança unificados em todos os componentes da aplicação IA

**Recursos de Implementação**: [Documentação Microsoft Prompt Shields](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)

![Proteção Microsoft Prompt Shields](../../../translated_images/pt-PT/prompt-shield.ff5b95be76e9c78c.webp)


## Ameaças Avançadas de Segurança MCP

### Vulnerabilidades de Sequestro de Sessão

O **sequestro de sessão** representa um vetor crítico de ataque em implementações MCP stateful onde partes não autorizadas obtêm e abusam de identificadores legítimos de sessão para se passarem por clientes e executar ações não autorizadas.

#### **Cenários de Ataque & Riscos**

- **Injeção de Prompt por Sequestro de Sessão**: Invasores com IDs de sessão roubados injetam eventos maliciosos em servidores que partilham estado de sessão, potencialmente desencadeando ações nocivas ou acedendo a dados sensíveis
- **Imitação Direta**: IDs de sessão roubados permitem chamadas diretas a servidores MCP que ignoram autenticação, tratando invasores como utilizadores legítimos
- **Fluxos Retomáveis Comprometidos**: Atacantes podem terminar pedidos prematuramente, fazendo com que clientes legítimos retomem com conteúdo potencialmente malicioso

#### **Controlos de Segurança para Gestão de Sessão**

**Requisitos Críticos:**
- **Verificação de Autorização**: Servidores MCP que implementam autorização **DEVEM** verificar TODOS os pedidos recebidos e **NÃO DEVEM** confiar em sessões para autenticação
- **Geração Segura de Sessões**: Utilização de IDs de sessão criptograficamente seguros e não determinísticos, gerados com geradores de números aleatórios seguros
- **Vinculação Específica ao Utilizador**: Vincular IDs de sessão a informação específica do utilizador usando formatos como `<user_id>:<session_id>` para evitar abuso de sessão entre utilizadores
- **Gestão do Ciclo de Vida da Sessão**: Implementar expiração adequada, rotação e invalidação para limitar janelas de vulnerabilidade
- **Segurança de Transporte**: HTTPS obrigatório para toda a comunicação para prevenir interceção de IDs de sessão

### Problema do Deputado Confuso

O **problema do deputado confuso** ocorre quando servidores MCP atuam como proxies de autenticação entre clientes e serviços de terceiros, criando oportunidades para bypass de autorização através da exploração de IDs de cliente estáticos.

#### **Mecânicas de Ataque & Riscos**

- **Bypass de Consentimento Baseado em Cookies**: Autenticação prévia do utilizador cria cookies de consentimento que invasores exploram via pedidos maliciosos de autorização com URIs de redirecionamento manipuladas
- **Roubo de Código de Autorização**: Cookies de consentimento existentes podem fazer servidores de autorização saltarem telas de consentimento, redirecionando códigos para endpoints controlados por invasores  
- **Acesso Não Autorizado a API**: Códigos de autorização roubados permitem troca de tokens e imitação de utilizador sem aprovação explícita

#### **Estratégias de Mitigação**

**Controlos Obrigatórios:**
- **Requisitos Explícitos de Consentimento**: Servidores proxy MCP que usam IDs de cliente estáticos **DEVEM** obter consentimento do utilizador para cada cliente registado dinamicamente
- **Implementação de Segurança OAuth 2.1**: Seguir as melhores práticas de segurança atuais do OAuth incluindo PKCE (Proof Key for Code Exchange) para todos os pedidos de autorização
- **Validação Rigorosa do Cliente**: Implementar validação rigorosa das URIs de redirecionamento e identificadores de cliente para prevenir exploração

### Vulnerabilidades de Passagem de Token  

A **passagem de token** representa um anti-padrão explícito onde servidores MCP aceitam tokens de cliente sem validação adequada e os encaminham para APIs downstream, violando as especificações de autorização MCP.

#### **Implicações de Segurança**

- **Circunvenção de Controlos**: Uso direto de tokens do cliente para API contorna controlos críticos de limitação de taxa, validação e monitorização
- **Corrupção do Rastreio de Auditoria**: Tokens emitidos pela upstream tornam impossível identificar o cliente, afetando capacidades de investigação de incidentes
- **Exfiltração de Dados Via Proxy**: Tokens não validados permitem a atores maliciosos usar servidores como proxies para acesso não autorizado a dados
- **Violação de Limites de Confiança**: Pressupostos de confiança dos serviços downstream podem ser violados quando as origens dos tokens não podem ser verificadas
- **Expansão de Ataques Multi-serviço**: Tokens comprometidos aceites em vários serviços permitem movimento lateral

#### **Controlos de Segurança Requeridos**

**Requisitos Inegociáveis:**
- **Validação de Token**: Servidores MCP **NÃO DEVEM** aceitar tokens não explicitamente emitidos para o servidor MCP
- **Verificação de Audiência**: Validar sempre que as declarações de audiência do token correspondam à identidade do servidor MCP
- **Ciclo de Vida Apropriado do Token**: Implementar tokens de acesso de curta duração com práticas seguras de rotação


## Segurança da Cadeia de Abastecimento para Sistemas IA

A segurança da cadeia de abastecimento evoluiu para além das dependências tradicionais de software e abrange agora todo o ecossistema IA. Implementações modernas de MCP devem verificar e monitorizar rigorosamente todos os componentes relacionados com IA, pois cada um introduz vulnerabilidades potenciais que podem comprometer a integridade do sistema.

### Componentes Expandidos da Cadeia de Abastecimento IA

**Dependências Tradicionais de Software:**
- Bibliotecas e frameworks open-source
- Imagens de containers e sistemas base  
- Ferramentas de desenvolvimento e pipelines de build
- Componentes e serviços de infraestrutura

**Elementos Específicos da Cadeia de Abastecimento IA:**
- **Modelos Fundamentais**: Modelos pré-treinados de vários fornecedores que exigem verificação de proveniência
- **Serviços de Embedding**: Serviços externos de vetorização e pesquisa semântica
- **Fornecedores de Contexto**: Fontes de dados, bases de conhecimento e repositórios de documentos  
- **APIs de Terceiros**: Serviços externos de IA, pipelines de ML e endpoints de processamento de dados
- **Artefactos de Modelo**: Pesos, configurações e variantes de modelos afinados
- **Fontes de Dados de Treinamento**: Conjuntos de dados usados para treino e afinação de modelos

### Estratégia Abrangente de Segurança da Cadeia de Abastecimento

#### **Verificação & Confiança de Componentes**
- **Validação da Proveniência**: Verificar a origem, licenciamento e integridade de todos os componentes IA antes da integração
- **Avaliação de Segurança**: Realizar varreduras de vulnerabilidades e revisões de segurança para modelos, fontes de dados e serviços IA
- **Análise de Reputação**: Avaliar o histórico de segurança e práticas dos fornecedores de serviços IA
- **Verificação de Conformidade**: Assegurar que todos os componentes cumprem requisitos organizacionais de segurança e regulamentares

#### **Pipelines de Implantação Seguros**  
- **Segurança CI/CD Automatizada**: Integrar varreduras de segurança em pipelines automatizados de implantação
- **Integridade dos Artefactos**: Implementar verificação criptográfica para todos os artefactos implantados (código, modelos, configurações)
- **Implantação Progressiva**: Usar estratégias de implantação progressiva com validação de segurança em cada fase
- **Repositórios de Artefactos Confiáveis**: Implantar apenas a partir de registos e repositórios de artefactos verificados e seguros

#### **Monitorização Contínua & Resposta**
- **Varredura de Dependências**: Monitorização contínua de vulnerabilidades para todas as dependências de software e componentes IA
- **Monitorização de Modelos**: Avaliação contínua do comportamento do modelo, deriva de desempenho e anomalias de segurança
- **Rastreamento de Saúde de Serviços**: Monitorizar serviços externos de IA para disponibilidade, incidentes de segurança e alterações de políticas
- **Integração de Inteligência de Ameaças**: Incorporar feeds de ameaças específicas para riscos de segurança de IA e ML

#### **Controlo de Acesso & Privilégio Mínimo**
- **Permissões ao Nível de Componente**: Restringir acesso a modelos, dados e serviços conforme a necessidade do negócio
- **Gestão de Contas de Serviço**: Implementar contas de serviço dedicadas com permissões mínimas necessárias
- **Segmentação de Rede**: Isolar componentes IA e limitar o acesso entre serviços na rede
- **Controlos de Gateway API**: Usar gateways API centralizados para controlar e monitorizar acesso a serviços externos IA

#### **Resposta a Incidentes & Recuperação**
- **Procedimentos de Resposta Rápida**: Processos estabelecidos para patching ou substituição de componentes IA comprometidos
- **Rotação de Credenciais**: Sistemas automatizados para rotacionar segredos, chaves API e credenciais de serviço
- **Capacidades de Reversão**: Capacidade de reverter rapidamente para versões anteriores conhecidas e seguras dos componentes IA
- **Recuperação de Violação na Cadeia de Abastecimento**: Procedimentos específicos para responder a compromissos em serviços IA upstream

### Ferramentas & Integração de Segurança Microsoft

**GitHub Advanced Security** oferece proteção abrangente da cadeia de abastecimento incluindo:
- **Varredura de Segredos**: Detecção automatizada de credenciais, chaves API e tokens em repositórios
- **Varredura de Dependências**: Avaliação de vulnerabilidades para dependências e bibliotecas open-source
- **Análise CodeQL**: Análise estática de código para vulnerabilidades de segurança e questões de codificação
- **Insights da Cadeia de Abastecimento**: Visibilidade sobre a saúde e status de segurança das dependências

**Integração Azure DevOps & Azure Repos:**
- Integração contínua de varreduras de segurança em plataformas de desenvolvimento Microsoft
- Verificações automatizadas de segurança em Azure Pipelines para cargas de trabalho IA
- Aplicação de políticas para implantação segura de componentes IA

**Práticas Internas Microsoft:**
A Microsoft implementa práticas extensivas de segurança da cadeia de abastecimento em todos os produtos. Aprenda sobre abordagens comprovadas em [A Jornada para Garantir a Cadeia de Abastecimento de Software na Microsoft](https://devblogs.microsoft.com/engineering-at-microsoft/the-journey-to-secure-the-software-supply-chain-at-microsoft/).


## Melhores Práticas de Segurança Fundamentais

As implementações MCP herdam e constroem sobre a postura de segurança existente da sua organização. Reforçar práticas fundamentais de segurança aumenta significativamente a segurança geral dos sistemas IA e das implementações MCP.

### Fundamentos Centrais de Segurança

#### **Práticas de Desenvolvimento Seguro**
- **Conformidade OWASP**: Proteção contra vulnerabilidades web do [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- **Proteções Específicas para IA**: Implementar controlos para o [OWASP Top 10 para LLMs](https://genai.owasp.org/download/43299/?tmstv=1731900559)
- **Gestão Segura de Segredos**: Uso de cofres dedicados para tokens, chaves API e dados de configuração sensíveis
- **Criptografia de Ponta a Ponta**: Implementar comunicações seguras em todos os componentes da aplicação e fluxos de dados
- **Validação de Entrada**: Validação rigorosa de todas as entradas de utilizador, parâmetros API e fontes de dados

#### **Fortalecimento de Infraestruturas**
- **Autenticação Multi-Fator**: MFA obrigatória para todas as contas administrativas e de serviço
- **Gestão de Patches**: Patching automático e atempado para sistemas operativos, frameworks e dependências  
- **Integração de Provedor de Identidade**: Gestão centralizada de identidade através de provedores empresariais (Microsoft Entra ID, Active Directory)
- **Segmentação de Rede**: Isolamento lógico dos componentes MCP para limitar potencial de movimento lateral
- **Princípio do Menor Privilégio**: Permissões mínimas necessárias para todos os componentes e contas do sistema

#### **Monitorização & Detecção de Segurança**
- **Registo Abrangente**: Registo detalhado das atividades da aplicação IA, incluindo interações cliente-servidor MCP
- **Integração SIEM**: Gestão centralizada de informação e eventos de segurança para deteção de anomalias
- **Análise Comportamental**: Monitorização com IA para detetar padrões invulgares no comportamento do sistema e utilizador
- **Inteligência de Ameaças**: Integração de feeds externos de ameaças e indicadores de compromisso (IOCs)
- **Resposta a Incidentes**: Procedimentos bem definidos para deteção, resposta e recuperação de incidentes de segurança

#### **Arquitetura Zero Trust**
- **Nunca Confiar, Sempre Verificar**: Verificação contínua de utilizadores, dispositivos e ligações de rede
- **Microsegmentação**: Controlo granular da rede que isola cargas de trabalho e serviços individuais
- **Segurança Centrada na Identidade**: Políticas de segurança baseadas em identidades verificadas em vez de localização de rede
- **Avaliação Contínua de Risco**: Avaliação dinâmica da postura de segurança baseada no contexto e comportamento atuais
- **Acesso Condicional**: Controlos de acesso que se adaptam com base em fatores de risco, localização e confiança do dispositivo

### Padrões de Integração Empresarial

#### **Integração no Ecossistema de Segurança Microsoft**
- **Microsoft Defender for Cloud**: Gestão abrangente da postura de segurança na cloud
- **Azure Sentinel**: Capacidades nativas de SIEM e SOAR para proteção de cargas de trabalho IA
- **Microsoft Entra ID**: Gestão empresarial de identidades e acessos com políticas de acesso condicional
- **Azure Key Vault**: Gestão centralizada de segredos com suporte de módulo de segurança de hardware (HSM)
- **Microsoft Purview**: Governação e conformidade de dados para fontes e fluxos de dados IA

#### **Conformidade & Governação**
- **Alinhamento Regulatório**: Assegurar que as implementações MCP cumprem requisitos de conformidade específicos do setor (RGPD, HIPAA, SOC 2)

- **Classificação de Dados**: Categorização e manipulação adequada de dados sensíveis processados por sistemas de IA
- **Registos de Auditoria**: Registos abrangentes para conformidade regulamentar e investigação forense
- **Controlo de Privacidade**: Implementação dos princípios de privacidade desde a conceção na arquitetura dos sistemas de IA
- **Gestão de Alterações**: Processos formais para revisões de segurança das modificações dos sistemas de IA

Estas práticas fundamentais criam uma base robusta de segurança que melhora a eficácia dos controlos de segurança específicos do MCP e proporciona proteção abrangente para aplicações movidas a IA.

## Principais Conclusões de Segurança

- **Abordagem de Segurança em Camadas**: Combinar práticas fundamentais de segurança (codificação segura, princípio do menor privilégio, verificação da cadeia de fornecimento, monitorização contínua) com controlos específicos de IA para proteção abrangente

- **Paisagem de Ameaças Específica da IA**: Os sistemas MCP enfrentam riscos únicos, incluindo injeção de prompts, envenenamento de ferramentas, sequestro de sessão, problemas de intermediário confuso, vulnerabilidades de passagem de tokens e permissões excessivas que requerem mitigação especializada

- **Excelência em Autenticação e Autorização**: Implementar autenticação robusta usando fornecedores externos de identidade (Microsoft Entra ID), aplicar validação correta de tokens e nunca aceitar tokens não emitidos explicitamente para o seu servidor MCP

- **Prevenção de Ataques à IA**: Implementar Microsoft Prompt Shields e Azure Content Safety para defender contra ataques indiretos de injeção de prompts e envenenamento de ferramentas, ao mesmo tempo que valida os metadados das ferramentas e monitoriza alterações dinâmicas

- **Segurança de Sessão e Transporte**: Utilizar IDs de sessão criptograficamente seguros, não determinísticos e vinculados à identidade do utilizador, implementar gestão adequada do ciclo de vida da sessão e nunca usar sessões para autenticação

- **Melhores Práticas de Segurança OAuth**: Prevenir ataques de intermediário confuso através do consentimento explícito do utilizador para clientes registados dinamicamente, implementação correta do OAuth 2.1 com PKCE e validação rigorosa de URI de redirecionamento  

- **Princípios de Segurança de Tokens**: Evitar anti-padrões de passagem de tokens, validar declarações de audiência dos tokens, implementar tokens de curta duração com rotação segura e manter limites claros de confiança

- **Segurança Abrangente da Cadeia de Fornecimento**: Tratar todos os componentes do ecossistema de IA (modelos, embeddings, fornecedores de contexto, APIs externas) com o mesmo rigor de segurança que as dependências tradicionais de software

- **Evolução Contínua**: Manter-se atualizado com as especificações do MCP em rápida evolução, contribuir para os padrões da comunidade de segurança e manter posturas de segurança adaptativas à medida que o protocolo amadurece

- **Integração de Segurança Microsoft**: Aproveitar o ecossistema abrangente de segurança da Microsoft (Prompt Shields, Azure Content Safety, GitHub Advanced Security, Entra ID) para reforçar a proteção nas implantações MCP

## Recursos Abrangentes

### **Documentação Oficial de Segurança MCP**
- [Especificação MCP (Atual: 2026-07-28)](https://modelcontextprotocol.io/specification/2026-07-28/)
- [Melhores Práticas de Segurança MCP](https://modelcontextprotocol.io/specification/2026-07-28/basic/security_best_practices)
- [Especificação de Autorização MCP](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization)
- [Repositório MCP no GitHub](https://github.com/modelcontextprotocol)

### **Recursos de Segurança OWASP MCP**
- [Guia de Segurança OWASP MCP Azure](https://microsoft.github.io/mcp-azure-security-guide/) - Top 10 OWASP MCP abrangente com orientações de implementação Azure
- [Top 10 OWASP MCP](https://owasp.org/www-project-mcp-top-10/) - Riscos oficiais de segurança OWASP MCP
- [Oficina MCP Security Summit (Sherpa)](https://azure-samples.github.io/sherpa/) - Treinamento prático de segurança para MCP no Azure

### **Normas & Melhores Práticas de Segurança**
- [Melhores Práticas de Segurança OAuth 2.0 (RFC 9700)](https://datatracker.ietf.org/doc/html/rfc9700)
- [Top 10 Segurança de Aplicações Web OWASP](https://owasp.org/www-project-top-ten/)
- [Top 10 OWASP para Modelos de Linguagem Grande](https://genai.owasp.org/download/43299/?tmstv=1731900559)
- [Relatório de Defesa Digital Microsoft](https://aka.ms/mddr)

### **Pesquisa e Análise de Segurança em IA**
- [Injeção de Prompt no MCP (Simon Willison)](https://simonwillison.net/2025/Apr/9/mcp-prompt-injection/)
- [Ataques de Envenenamento de Ferramentas (Invariant Labs)](https://invariantlabs.ai/blog/mcp-security-notification-tool-poisoning-attacks)
- [Briefing de Pesquisa em Segurança MCP (Wiz Security)](https://www.wiz.io/blog/mcp-security-research-briefing#remote-servers-22)

### **Soluções de Segurança Microsoft**
- [Documentação Microsoft Prompt Shields](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)
- [Serviço Azure Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/)
- [Segurança Microsoft Entra ID](https://learn.microsoft.com/entra/identity-platform/secure-least-privileged-access)
- [Melhores Práticas de Gestão de Tokens Azure](https://learn.microsoft.com/entra/identity-platform/access-tokens)
- [GitHub Advanced Security](https://github.com/security/advanced-security)

### **Guias de Implementação & Tutoriais**
- [Gestão de API Azure como Gateway de Autenticação MCP](https://techcommunity.microsoft.com/blog/integrationsonazureblog/azure-api-management-your-auth-gateway-for-mcp-servers/4402690)
- [Autenticação Microsoft Entra ID com Servidores MCP](https://den.dev/blog/mcp-server-auth-entra-id-session/)
- [Armazenamento Seguro e Encriptação de Tokens (Vídeo)](https://youtu.be/uRdX37EcCwg?si=6fSChs1G4glwXRy2)

### **DevOps & Segurança da Cadeia de Fornecimento**
- [Segurança Azure DevOps](https://azure.microsoft.com/products/devops)
- [Segurança Azure Repos](https://azure.microsoft.com/products/devops/repos/)
- [Jornada Microsoft para Segurança da Cadeia de Fornecimento](https://devblogs.microsoft.com/engineering-at-microsoft/the-journey-to-secure-the-software-supply-chain-at-microsoft/)

## **Documentação de Segurança Adicional**

Para orientação abrangente de segurança, consulte estes documentos especializados nesta seção:

- **[Amostra de Autorização CIMD e DCR](./samples/cimd-dcr-auth/README.md)** - Servidor de recursos MCP `2026-07-28` executável em TypeScript que compara Documentos de Metadados de ID de Cliente preferidos com fallback de Registo Dinâmico de Cliente obsoleto
- **[Melhores Práticas de Segurança MCP](./mcp-security-best-practices.md)** - Melhores práticas completas de segurança para implementações MCP
- **[Implementação Azure Content Safety](./azure-content-safety-implementation.md)** - Exemplos práticos de implementação para integração com Azure Content Safety  
- **[Controlos de Segurança MCP](./mcp-security-controls.md)** - Últimos controlos e técnicas de segurança para implantações MCP
- **[Referência Rápida de Melhores Práticas MCP](./mcp-best-practices.md)** - Guia rápido de referência para práticas essenciais de segurança MCP
- **[BlueHat 2026: Protegendo o futuro da IA: Segurança MCP com padrões de defesa em profundidade](https://www.youtube.com/watch?v=cVWB58kEt-Y)** - Padrões de defesa em profundidade do Centro de Resposta a Segurança Microsoft (MSRC)

### **Treino Prático de Segurança**

- **[Oficina MCP Security Summit (Sherpa)](https://azure-samples.github.io/sherpa/)** - Oficina prática abrangente para proteger servidores MCP no Azure com acampamentos progressivos desde o Acampamento Base até ao Summit
- **[Guia de Segurança OWASP MCP Azure](https://microsoft.github.io/mcp-azure-security-guide/)** - Arquitetura de referência e orientação de implementação para todos os riscos Top 10 OWASP MCP

---

## O que Segue

Seguinte: [Capítulo 3: Primeiros Passos](../03-GettingStarted/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas resultantes da utilização desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->