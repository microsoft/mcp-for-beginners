# Segurança MCP: Proteção Abrangente para Sistemas de IA

[![Práticas recomendadas de segurança MCP](../../../translated_images/pt-BR/03.175aed6dedae133f.webp)](https://youtu.be/88No8pw706o)

_(Clique na imagem acima para assistir ao vídeo desta lição)_

Segurança é fundamental no design de sistemas de IA, por isso damos prioridade a ela como nossa segunda seção. Isso está alinhado com o princípio **Secure by Design** da Microsoft, da [Iniciativa Futuro Seguro](https://www.microsoft.com/security/blog/2025/04/17/microsofts-secure-by-design-journey-one-year-of-success/).

O Protocolo de Contexto do Modelo (MCP) traz capacidades poderosas para aplicações orientadas por IA, ao mesmo tempo em que introduz desafios únicos de segurança que vão além dos riscos tradicionais de software. Sistemas MCP enfrentam tanto preocupações de segurança estabelecidas (codificação segura, privilégio mínimo, segurança da cadeia de suprimentos) quanto novas ameaças específicas de IA, incluindo injeção de prompt, envenenamento de ferramenta, sequestro de sessão, ataques de representante confundido, vulnerabilidades de token passthrough e modificação dinâmica de capacidades.

Esta lição explora os riscos de segurança mais críticos em implementações MCP — abordando autenticação, autorização, permissões excessivas, injeção de prompt indireta, segurança de sessão, problemas de representante confundido, gerenciamento de token e vulnerabilidades na cadeia de suprimentos. Você aprenderá controles acionáveis e práticas recomendadas para mitigar esses riscos enquanto alavanca soluções Microsoft como Prompt Shields, Azure Content Safety e GitHub Advanced Security para fortalecer sua implantação MCP.

## Objetivos de Aprendizagem

Ao final desta lição, você será capaz de:

- **Identificar Ameaças Específicas do MCP**: Reconhecer riscos exclusivos de segurança em sistemas MCP, incluindo injeção de prompt, envenenamento de ferramenta, permissões excessivas, sequestro de sessão, problemas de representante confundido, vulnerabilidades de token passthrough e riscos na cadeia de suprimentos
- **Aplicar Controles de Segurança**: Implementar mitigações eficazes incluindo autenticação robusta, acesso com privilégio mínimo, gerenciamento seguro de token, controles de segurança de sessão e verificação da cadeia de suprimentos
- **Aproveitar Soluções de Segurança da Microsoft**: Entender e implantar Microsoft Prompt Shields, Azure Content Safety e GitHub Advanced Security para proteção de cargas de trabalho MCP
- **Validar a Segurança das Ferramentas**: Reconhecer a importância da validação de metadados das ferramentas, monitoramento de alterações dinâmicas e defesa contra ataques indiretos de injeção de prompt
- **Integrar Práticas Recomendadas**: Combinar fundamentos de segurança estabelecidos (codificação segura, endurecimento de servidor, zero trust) com controles específicos MCP para proteção abrangente

# Arquitetura e Controles de Segurança MCP

Implementações modernas do MCP requerem abordagens de segurança em camadas que abordem segurança tradicional de software e ameaças específicas de IA. A especificação MCP em rápida evolução continua amadurecendo seus controles de segurança, permitindo melhor integração com arquiteturas de segurança corporativas e práticas recomendadas estabelecidas.

Pesquisas do [Microsoft Digital Defense Report](https://aka.ms/mddr) demonstram que **98% das violações relatadas seriam prevenidas por uma higiene robusta de segurança**. A estratégia de proteção mais eficaz combina práticas de segurança fundamentais com controles específicos MCP — medidas de segurança de base comprovadas continuam sendo as mais impactantes na redução do risco geral.

## Panorama Atual de Segurança

> **Nota:** Este capítulo combina controles de segurança MCP estabelecidos com as
> diretrizes atuais de autorização da **Especificação MCP 2026-07-28**. Sempre consulte
> a [Especificação MCP atual](https://modelcontextprotocol.io/specification/2026-07-28/),
> o [repositório MCP no GitHub](https://github.com/modelcontextprotocol), e
> a [documentação de melhores práticas de segurança](https://modelcontextprotocol.io/specification/2026-07-28/basic/security_best_practices)
> ao implementar código sensível à segurança.

> **Atualização de autorização:** O MCP `2026-07-28` requer que os clientes validem o
> parâmetro `iss` nas respostas de autorização (RFC 9207) e vinculem credenciais
> registradas ao servidor de autorização emissor. O Registro Dinâmico de Clientes
> está obsoleto; novas implementações devem usar Documentos de Metadados de ID de Cliente.
> Veja [O que mudou no MCP: A Especificação 2026-07-28](../01-CoreConcepts/mcp-2026-07-28.md)
> para a lista completa das mudanças em autorização.

## 🏔️ Workshop MCP Security Summit (Sherpa)

Para **treinamento prático de segurança**, recomendamos muito o **Workshop MCP Security Summit** (Sherpa) — uma expedição guiada abrangente para proteger servidores MCP no Microsoft Azure.

### Visão Geral do Workshop

O [Workshop MCP Security Summit](https://azure-samples.github.io/sherpa/) oferece treinamento prático e acionável em segurança por meio da comprovada metodologia "vulnerável → explorar → corrigir → validar". Você irá:

- **Aprender quebrando coisas**: Vivenciar vulnerabilidades explorando servidores intencionalmente inseguros
- **Usar segurança nativa do Azure**: Aproveitar Azure Entra ID, Key Vault, API Management e AI Content Safety
- **Seguir defesa em profundidade**: Progredir por acampamentos que constroem camadas abrangentes de segurança
- **Aplicar padrões OWASP**: Cada técnica corresponde ao [Guia de Segurança MCP Azure OWASP](https://microsoft.github.io/mcp-azure-security-guide/)
- **Obter código para produção**: Sair com implementações funcionando e testadas

### Rota da Expedição

| Acampamento | Foco | Riscos OWASP Cobertos |
|------|-------|---------------------|
| **Acampamento Base** | Fundamentos MCP e vulnerabilidades de autenticação | MCP01, MCP07 |
| **Acampamento 1: Identidade** | OAuth 2.1, Identidade Gerenciada Azure, Key Vault | MCP01, MCP02, MCP07 |
| **Acampamento 2: Gateway** | Gerenciamento de API, Endpoints Privados, governança | MCP02, MCP06, MCP07, MCP09 |
| **Acampamento 3: Segurança I/O** | Injeção de prompt, proteção de PII, segurança de conteúdo | MCP03, MCP05, MCP06, MCP10 |
| **Acampamento 4: Monitoramento** | Log Analytics, dashboards, detecção de ameaças | MCP04, MCP08 |
| **O Cume** | Teste de integração Red Team / Blue Team | Todos |

**Comece aqui**: [https://azure-samples.github.io/sherpa/](https://azure-samples.github.io/sherpa/)

## Top 10 Riscos de Segurança OWASP MCP

O [Guia de Segurança MCP Azure OWASP](https://microsoft.github.io/mcp-azure-security-guide/) detalha os dez riscos de segurança mais críticos para implementações MCP:

| Risco | Descrição | Mitigação Azure |
|------|-------------|------------------|
| **MCP01** | Má Gestão de Token & Exposição de Segredos | Azure Key Vault, Identidade Gerenciada |
| **MCP02** | Escalada de Privilégio via Scope Creep | RBAC, Acesso Condicional |
| **MCP03** | Envenenamento de Ferramentas | Validação de ferramentas, verificação de integridade |
| **MCP04** | Ataques na Cadeia de Suprimentos de Software & Manipulação de Dependências | GitHub Advanced Security, scanner de dependências |
| **MCP05** | Injeção e Execução de Comandos | Validação de entrada, sandboxing |
| **MCP06** | Subversão do Fluxo de Intenção | Azure AI Content Safety, Prompt Shields |
| **MCP07** | Autenticação & Autorização Insuficientes | Azure Entra ID, OAuth 2.1 com PKCE |
| **MCP08** | Falta de Auditoria e Telemetria | Azure Monitor, Application Insights |
| **MCP09** | Servidores MCP Sombra | Governança do API Center, isolamento de rede |
| **MCP10** | Injeção de Contexto & Exposição Excessiva | Classificação de dados, exposição mínima |

### Evolução da Autenticação MCP

A especificação MCP evoluiu significativamente na abordagem de autenticação e autorização:

- **Abordagem Original**: Especificações iniciais exigiam que desenvolvedores implementassem servidores de autenticação customizados, com servidores MCP atuando como Servidores de Autorização OAuth 2.0 gerenciando a autenticação de usuários diretamente
- **Padrão Atual (`2026-07-28`)**: Servidores MCP podem delegar autenticação
  para provedores de identidade externos como Microsoft Entra ID. Clientes também devem
  aplicar os requisitos atuais de validação de emissor e vinculação de credenciais.
- **Segurança na Camada de Transporte**: Suporte aprimorado para mecanismos de transporte seguros com padrões de autenticação adequados para conexões locais (STDIO) e remotas (HTTP Streamable)

## Segurança de Autenticação & Autorização

### Desafios Atuais de Segurança

Implementações modernas do MCP enfrentam vários desafios de autenticação e autorização:

### Riscos & Vetores de Ataque

- **Lógica de Autorização Mal Configurada**: Implementação defeituosa da autorização em servidores MCP pode expor dados sensíveis e aplicar controles de acesso incorretamente
- **Comprometimento de Token OAuth**: Roubo de tokens do servidor MCP local permite que atacantes se façam passar por servidores e acessem serviços subsequentes
- **Vulnerabilidades de Token Passthrough**: Manipulação inadequada de token cria falhas que ignoram controles de segurança e lacunas de responsabilização
- **Permissões Excessivas**: Servidores MCP com privilégios excessivos violam princípios de privilégio mínimo e aumentam superfícies de ataque

#### Token Passthrough: Um Anti-Padrão Crítico

**Token passthrough é explicitamente proibido** na especificação atual de autorização MCP devido a sérias implicações de segurança:

##### Circunvenção de Controles de Segurança
- Servidores MCP e APIs downstream implementam controles críticos de segurança (limitação de taxa, validação de requisição, monitoramento de tráfego) que dependem da validação correta de tokens
- O uso direto de tokens cliente-para-API ignora essas proteções essenciais, comprometendo a arquitetura de segurança

##### Desafios de Responsabilização & Auditoria  
- Servidores MCP não conseguem distinguir entre clientes usando tokens emitidos a montante, quebrando trilhas de auditoria
- Logs do servidor de recursos downstream mostram origens de requisição enganosas ao invés dos intermediários reais do servidor MCP
- A investigação de incidentes e auditoria de conformidade tornam-se significativamente mais difíceis

##### Riscos de Exfiltração de Dados
- Declarações de tokens não validadas permitem que agentes maliciosos com tokens roubados usem servidores MCP como proxies para exfiltração de dados
- Violações da fronteira de confiança permitem padrões de acesso não autorizados que ignoram controles de segurança pretendidos

##### Vetores de Ataque Multi-Serviço
- Tokens comprometidos aceitos por múltiplos serviços possibilitam movimento lateral por sistemas conectados
- Pressupostos de confiança entre serviços podem ser violados quando origens de tokens não podem ser verificadas

### Controles de Segurança & Mitigações

**Requisitos Críticos de Segurança:**

> **OBRIGATÓRIO**: Servidores MCP **NÃO DEVEM** aceitar tokens que não foram explicitamente emitidos para o servidor MCP

#### Controles de Autenticação & Autorização

- **Revisão Rigorosa de Autorização**: Conduzir auditorias abrangentes da lógica de autorização do servidor MCP para garantir que somente usuários e clientes pretendidos possam acessar recursos sensíveis
  - **Guia de Implementação**: [Azure API Management como Gateway de Autenticação para Servidores MCP](https://techcommunity.microsoft.com/blog/integrationsonazureblog/azure-api-management-your-auth-gateway-for-mcp-servers/4402690)
  - **Integração de Identidade**: [Usando Microsoft Entra ID para Autenticação de Servidor MCP](https://den.dev/blog/mcp-server-auth-entra-id-session/)

- **Gerenciamento Seguro de Token**: Implementar [práticas recomendadas da Microsoft para validação e ciclo de vida de tokens](https://learn.microsoft.com/en-us/entra/identity-platform/access-tokens)
  - Validar que as declarações de público dos tokens correspondam à identidade do servidor MCP
  - Implementar políticas adequadas de rotação e expiração de token
  - Prevenir ataques de repetição de token e uso não autorizado

- **Armazenamento Protegido de Token**: Armazenar tokens com criptografia em repouso e em trânsito
  - **Práticas recomendadas**: [Diretrizes de Armazenamento Seguro de Token e Criptografia](https://youtu.be/uRdX37EcCwg?si=6fSChs1G4glwXRy2)

#### Implementação de Controle de Acesso

- **Princípio do Menor Privilégio**: Conceder aos servidores MCP apenas as permissões mínimas necessárias para a funcionalidade pretendida
  - Revisões regulares de permissões e atualizações para prevenir escalada de privilégios
  - **Documentação Microsoft**: [Acesso Seguro com Menor Privilégio](https://learn.microsoft.com/entra/identity-platform/secure-least-privileged-access)

- **Controle de Acesso Baseado em Função (RBAC)**: Implementar atribuições finas de papéis
  - Limitar escopo de funções a recursos e ações específicas
  - Evitar permissões amplas ou desnecessárias que aumentem a superfície de ataque

- **Monitoramento Contínuo de Permissões**: Implementar auditoria e monitoramento contínuos de acesso
  - Monitorar padrões de uso de permissões para detectar anomalias
  - Remediar prontamente privilégios excessivos ou não utilizados

## Ameaças de Segurança Específicas de IA

### Ataques de Injeção de Prompt & Manipulação de Ferramentas

Implementações modernas do MCP enfrentam vetores sofisticados de ataque específicos de IA que medidas tradicionais de segurança não conseguem abordar completamente:

#### **Injeção Indireta de Prompt (Injeção Cross-Domain de Prompt)**

**Injeção Indireta de Prompt** representa uma das vulnerabilidades mais críticas em sistemas de IA habilitados para MCP. Atacantes incorporam instruções maliciosas em conteúdos externos — documentos, páginas web, e-mails ou fontes de dados — que sistemas de IA processam posteriormente como comandos legítimos.

**Cenários de Ataque:**
- **Injeção baseada em documento**: Instruções maliciosas ocultas em documentos processados que disparam ações não intencionadas da IA
- **Exploração de conteúdo web**: Páginas web comprometidas contendo prompts incorporados que manipulam o comportamento da IA quando capturados
- **Ataques baseados em e-mail**: Prompts maliciosos em e-mails que fazem assistentes de IA vazarem informações ou executarem ações não autorizadas
- **Contaminação da fonte de dados**: Bancos de dados ou APIs comprometidas servindo conteúdo contaminado para sistemas de IA

**Impacto no mundo real**: Estes ataques podem resultar em exfiltração de dados, violações de privacidade, geração de conteúdo prejudicial e manipulação de interações dos usuários. Para análise detalhada, veja [Injeção de Prompt no MCP (Simon Willison)](https://simonwillison.net/2025/Apr/9/mcp-prompt-injection/).

![Diagrama de Ataque de Injeção de Prompt](../../../translated_images/pt-BR/prompt-injection.ed9fbfde297ca877.webp)

#### **Ataques de Envenenamento de Ferramenta**

**Envenenamento de Ferramenta** ataca os metadados que definem ferramentas MCP, explorando como LLMs interpretam descrições e parâmetros das ferramentas para tomar decisões de execução.

**Mecanismos de Ataque:**
- **Manipulação de metadados**: Atacantes injetam instruções maliciosas em descrições de ferramentas, definições de parâmetros ou exemplos de uso
- **Instruções invisíveis**: Prompts ocultos em metadados da ferramenta processados por modelos de IA, mas invisíveis aos usuários humanos
- **Modificação dinâmica da ferramenta ("Rug Pulls")**: Ferramentas aprovadas pelos usuários são depois modificadas para executar ações maliciosas sem a consciência do usuário
- **Injeção de parâmetro**: Conteúdo malicioso incorporado em esquemas de parâmetro da ferramenta que influenciam o comportamento do modelo


**Riscos de Servidores Hospedados**: Servidores MCP remotos apresentam riscos elevados, pois as definições das ferramentas podem ser atualizadas após a aprovação inicial do usuário, criando cenários onde ferramentas anteriormente seguras se tornam maliciosas. Para uma análise completa, veja [Tool Poisoning Attacks (Invariant Labs)](https://invariantlabs.ai/blog/mcp-security-notification-tool-poisoning-attacks).

![Diagrama de Ataque por Injeção de Ferramenta](../../../translated_images/pt-BR/tool-injection.3b0b4a6b24de6bef.webp)

#### **Vetores de Ataque Adicionais de IA**

- **Injeção de Prompt Entre Domínios (XPIA)**: Ataques sofisticados que aproveitam conteúdo de múltiplos domínios para burlar controles de segurança
- **Modificação Dinâmica de Capacidades**: Alterações em tempo real nas capacidades das ferramentas que escapam das avaliações iniciais de segurança
- **Envenenamento da Janela de Contexto**: Ataques que manipulam janelas de contexto grandes para esconder instruções maliciosas
- **Ataques de Confusão ao Modelo**: Exploração de limitações do modelo para criar comportamentos imprevisíveis ou inseguros


### Impacto dos Riscos de Segurança de IA

**Consequências de Alto Impacto:**
- **Exfiltração de Dados**: Acesso não autorizado e roubo de dados sensíveis empresariais ou pessoais
- **Violação de Privacidade**: Exposição de informações pessoais identificáveis (PII) e dados confidenciais de negócios  
- **Manipulação de Sistemas**: Modificações não intencionais em sistemas críticos e fluxos de trabalho
- **Roubo de Credenciais**: Comprometimento de tokens de autenticação e credenciais de serviço
- **Movimento Lateral**: Uso de sistemas de IA comprometidos como pivôs para ataques mais amplos na rede

### Soluções de Segurança de IA da Microsoft

#### **Escudos de Prompt de IA: Proteção Avançada Contra Ataques de Injeção**

Os **Escudos de Prompt de IA** da Microsoft fornecem defesa abrangente contra ataques de injeção de prompt diretos e indiretos por meio de múltiplas camadas de segurança:

##### **Mecanismos Principais de Proteção:**

1. **Detecção Avançada & Filtragem**
   - Algoritmos de aprendizado de máquina e técnicas de PLN detectam instruções maliciosas em conteúdos externos
   - Análise em tempo real de documentos, páginas web, e-mails e fontes de dados para ameaças embutidas
   - Compreensão contextual dos padrões legítimos vs. maliciosos de prompts

2. **Técnicas de Destaque**  
   - Distingue entre instruções de sistema confiáveis e entradas externas potencialmente comprometidas
   - Métodos de transformação de texto que aumentam a relevância para o modelo enquanto isolam conteúdo malicioso
   - Auxilia os sistemas de IA a manter hierarquia adequada de instruções e ignorar comandos injetados

3. **Sistemas de Delimitador & Marcação de Dados**
   - Definição explícita de limites entre mensagens de sistema confiáveis e texto de entrada externo
   - Marcadores especiais destacam fronteiras entre fontes de dados confiáveis e não confiáveis
   - Separação clara evita confusão nas instruções e execução não autorizada de comandos

4. **Inteligência de Ameaças Contínua**
   - Microsoft monitora continuamente padrões emergentes de ataque e atualiza defesas
   - Busca proativa por novas técnicas de injeção e vetores de ataque
   - Atualizações regulares do modelo de segurança para manter efetividade contra ameaças em evolução

5. **Integração com Azure Content Safety**
   - Parte do conjunto abrangente Azure AI Content Safety
   - Detecção adicional para tentativas de jailbreak, conteúdo nocivo e violações de políticas de segurança
   - Controles unificados de segurança em todos os componentes das aplicações de IA

**Recursos de Implementação**: [Documentação dos Escudos de Prompt da Microsoft](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)

![Proteção dos Escudos de Prompt da Microsoft](../../../translated_images/pt-BR/prompt-shield.ff5b95be76e9c78c.webp)


## Ameaças Avançadas à Segurança MCP

### Vulnerabilidades de Sequestro de Sessão

**Sequestro de sessão** representa um vetor crítico de ataque em implementações MCP com estado, em que partes não autorizadas obtêm e abusam de identificadores legítimos de sessão para se passar por clientes e realizar ações não autorizadas.

#### **Cenários de Ataque & Riscos**

- **Injeção de Prompt via Sequestro de Sessão**: Atacantes com IDs de sessão roubados inserem eventos maliciosos em servidores que compartilham o estado da sessão, potencialmente disparando ações nocivas ou acessando dados sensíveis
- **Impersonação Direta**: IDs de sessão roubados permitem chamadas diretas ao servidor MCP que contornam autenticação, tratando atacantes como usuários legítimos
- **Streams Retomáveis Comprometidos**: Atacantes podem terminar pedidos prematuramente, fazendo com que clientes legítimos retomem conteúdos potencialmente maliciosos

#### **Controles de Segurança para Gerenciamento de Sessões**

**Requisitos Críticos:**
- **Verificação de Autorização**: Servidores MCP que implementam autorização **DEVEM** verificar TODAS as requisições recebidas e **NÃO DEVEM** confiar em sessões para autenticação
- **Geração Segura de Sessão**: Uso de IDs de sessão criptograficamente seguros, não determinísticos, gerados com geradores seguros de números aleatórios
- **Vinculação Específica ao Usuário**: Vincular IDs de sessão a informações específicas do usuário usando formatos como `<user_id>:<session_id>` para evitar abuso de sessão entre usuários
- **Gerenciamento do Ciclo de Vida da Sessão**: Implementar expiração, rotação e invalidação adequadas para limitar janelas de vulnerabilidade
- **Segurança de Transporte**: HTTPS obrigatório para toda comunicação para evitar interceptação de IDs de sessão

### Problema do Procurador Confuso

O **problema do procurador confuso** ocorre quando servidores MCP atuam como proxies de autenticação entre clientes e serviços de terceiros, criando oportunidades para burlar autorização via exploração de IDs estáticos de cliente.

#### **Mecânicas de Ataque & Riscos**

- **Bypass baseado em Cookie de Consentimento**: Autenticação anterior do usuário cria cookies de consentimento que atacantes exploram por meio de requisições de autorização maliciosas com URIs de redirecionamento forjadas
- **Roubo de Código de Autorização**: Cookies de consentimento existentes podem fazer com que servidores de autorização pulem telas de consentimento, redirecionando códigos para endpoints controlados por atacantes  
- **Acesso Não Autorizado à API**: Códigos de autorização roubados permitem troca de token e impersonação de usuários sem aprovação explícita

#### **Estratégias de Mitigação**

**Controles Obrigatórios:**
- **Requisitos Explícitos de Consentimento**: Servidores proxy MCP usando IDs estáticos de cliente **DEVEM** obter consentimento do usuário para cada cliente registrado dinamicamente
- **Implementação de Segurança OAuth 2.1**: Seguir as melhores práticas atuais de segurança OAuth, incluindo PKCE (Proof Key for Code Exchange) para todas as requisições de autorização
- **Validação Rigorosa do Cliente**: Implementar validação rigorosa de URIs de redirecionamento e identificadores de cliente para evitar exploração

### Vulnerabilidades de Token Passthrough  

**Token passthrough** representa um anti-padrão explícito onde servidores MCP aceitam tokens do cliente sem validação adequada e os encaminham para APIs a jusante, violando especificações de autorização MCP.

#### **Implicações de Segurança**

- **Circunvenção de Controle**: Uso direto de tokens cliente para API contorna controles críticos de limitação de taxa, validação e monitoramento
- **Corrupção de Trilhas de Auditoria**: Tokens emitidos a montante tornam impossível identificar o cliente, comprometendo investigações de incidentes
- **Exfiltração de Dados via Proxy**: Tokens não validados permitem que agentes maliciosos usem servidores como proxies para acesso não autorizado a dados
- **Violações de Barreiras de Confiança**: Suposições de confiança dos serviços a jusante podem ser violadas quando as origens dos tokens não podem ser verificadas
- **Expansão de Ataque Multi-serviço**: Tokens comprometidos aceitos em múltiplos serviços permitem movimento lateral

#### **Controles de Segurança Necessários**

**Requisitos Inegociáveis:**
- **Validação de Token**: Servidores MCP **NÃO DEVEM** aceitar tokens que não tenham sido explicitamente emitidos para o servidor MCP
- **Verificação da Audiência**: Sempre validar que as reivindicações da audiência do token correspondam à identidade do servidor MCP
- **Ciclo de Vida Adequado do Token**: Implementar tokens de acesso de curta duração com práticas seguras de rotação


## Segurança da Cadeia de Suprimentos para Sistemas de IA

A segurança da cadeia de suprimentos evoluiu além das dependências tradicionais de software para englobar todo o ecossistema de IA. Implementações modernas de MCP devem verificar e monitorar rigorosamente todos os componentes relacionados à IA, pois cada um introduz vulnerabilidades potenciais que podem comprometer a integridade do sistema.

### Componentes Expandidos da Cadeia de Suprimentos de IA

**Dependências Tradicionais de Software:**
- Bibliotecas e frameworks open-source
- Imagens de containers e sistemas base  
- Ferramentas de desenvolvimento e pipelines de build
- Componentes e serviços de infraestrutura

**Elementos Específicos da Cadeia de Suprimentos de IA:**
- **Modelos Fundamentais**: Modelos pré-treinados de diversos provedores que requerem verificação de proveniência
- **Serviços de Embedding**: Serviços externos de vetorização e busca semântica
- **Provedores de Contexto**: Fontes de dados, bases de conhecimento e repositórios de documentos  
- **APIs de Terceiros**: Serviços externos de IA, pipelines de ML e endpoints de processamento de dados
- **Artefatos de Modelos**: Pesos, configurações e variantes finamente ajustadas dos modelos
- **Fontes de Dados de Treinamento**: Conjuntos de dados usados para treinamento e ajuste fino de modelos

### Estratégia Abrangente para Segurança da Cadeia de Suprimentos

#### **Verificação & Confiança dos Componentes**
- **Validação de Proveniência**: Verificar a origem, licenciamento e integridade de todos os componentes de IA antes da integração
- **Avaliação de Segurança**: Realizar varreduras de vulnerabilidades e revisões de segurança para modelos, fontes de dados e serviços de IA
- **Análise de Reputação**: Avaliar o histórico de segurança e práticas dos provedores de serviços de IA
- **Verificação de Conformidade**: Garantir que todos os componentes atendam aos requisitos organizacionais de segurança e regulamentação

#### **Pipelines Seguros de Implantação**  
- **Segurança CI/CD Automatizada**: Integrar varredura de segurança em pipelines automatizados de implantação
- **Integridade dos Artefatos**: Implementar verificação criptográfica para todos os artefatos implantados (código, modelos, configurações)
- **Implantação em Estágios**: Usar estratégias progressivas de implantação com validação de segurança em cada estágio
- **Repositórios Confiáveis de Artefatos**: Implantar somente a partir de registries e repositórios de artefatos verificados e seguros

#### **Monitoramento e Resposta Contínuos**
- **Varredura de Dependências**: Monitoramento contínuo de vulnerabilidades para todas as dependências de software e componentes de IA
- **Monitoramento de Modelos**: Avaliação contínua do comportamento do modelo, deriva de performance e anomalias de segurança
- **Monitoramento da Saúde do Serviço**: Acompanhamento de serviços externos de IA quanto à disponibilidade, incidentes de segurança e mudanças de política
- **Integração de Inteligência de Ameaças**: Incorporar feeds de ameaças específicos para riscos de segurança em IA e ML

#### **Controle de Acesso & Menor Privilégio**
- **Permissões no Nível do Componente**: Restringir acesso a modelos, dados e serviços conforme necessidade empresarial
- **Gerenciamento de Contas de Serviço**: Implementar contas de serviço dedicadas com permissões mínimas necessárias
- **Segmentação de Rede**: Isolar componentes de IA e limitar acesso de rede entre serviços
- **Controles de Gateway de API**: Usar gateways de API centralizados para controlar e monitorar acesso a serviços externos de IA

#### **Resposta e Recuperação de Incidentes**
- **Procedimentos de Resposta Rápida**: Processos estabelecidos para patch ou substituição de componentes de IA comprometidos
- **Rotação de Credenciais**: Sistemas automatizados para rotacionar segredos, chaves API e credenciais de serviço
- **Capacidades de Rollback**: Capacidade de reverter rapidamente para versões conhecidas boas anteriores dos componentes de IA
- **Recuperação de Violação de Cadeia de Suprimentos**: Procedimentos específicos para responder a compromissos de serviços de IA a montante

### Ferramentas & Integração de Segurança da Microsoft

**GitHub Advanced Security** oferece proteção abrangente da cadeia de suprimentos incluindo:
- **Varredura de Segredos**: Detecção automatizada de credenciais, chaves API e tokens em repositórios
- **Varredura de Dependências**: Avaliação de vulnerabilidades para dependências e bibliotecas open-source
- **Análise CodeQL**: Análise estática de código para vulnerabilidades de segurança e problemas de codificação
- **Insights da Cadeia de Suprimentos**: Visibilidade da saúde e status de segurança das dependências

**Integração com Azure DevOps & Azure Repos:**
- Integração fluida de varredura de segurança em plataformas de desenvolvimento Microsoft
- Verificações automatizadas de segurança em Azure Pipelines para cargas de trabalho de IA
- Aplicação de políticas para implantação segura de componentes de IA

**Práticas Internas da Microsoft:**
A Microsoft implementa práticas extensas de segurança da cadeia de suprimentos em todos os produtos. Saiba mais sobre abordagens comprovadas em [A Jornada para Proteger a Cadeia de Suprimentos de Software na Microsoft](https://devblogs.microsoft.com/engineering-at-microsoft/the-journey-to-secure-the-software-supply-chain-at-microsoft/).


## Melhores Práticas Fundamentais de Segurança

Implementações MCP herdam e constroem sobre a postura de segurança existente da sua organização. Fortalecer práticas fundamentais de segurança melhora significativamente a segurança geral de sistemas de IA e implantações MCP.

### Fundamentos Centrais de Segurança

#### **Práticas Seguras de Desenvolvimento**
- **Conformidade OWASP**: Proteção contra vulnerabilidades de aplicações web do [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- **Proteções Específicas para IA**: Implementar controles para o [OWASP Top 10 para LLMs](https://genai.owasp.org/download/43299/?tmstv=1731900559)
- **Gerenciamento Seguro de Segredos**: Uso de cofres dedicados para tokens, chaves API e dados sensíveis de configuração
- **Criptografia de Ponta a Ponta**: Implementar comunicações seguras entre todos os componentes e fluxos de dados da aplicação
- **Validação de Entradas**: Validação rigorosa de todas as entradas de usuário, parâmetros de API e fontes de dados

#### **Endurecimento da Infraestrutura**
- **Autenticação Multifator**: MFA obrigatória para todas as contas administrativas e de serviço
- **Gerenciamento de Patches**: Correção automatizada e oportuna para sistemas operacionais, frameworks e dependências  
- **Integração com Provedor de Identidade**: Gerenciamento centralizado de identidade via provedores empresariais (Microsoft Entra ID, Active Directory)
- **Segmentação de Rede**: Isolamento lógico dos componentes MCP para limitar potencial de movimento lateral
- **Princípio do Menor Privilégio**: Permissões mínimas necessárias para todos os componentes e contas do sistema

#### **Monitoramento & Detecção de Segurança**
- **Registro Abrangente**: Log detalhado das atividades da aplicação de IA, incluindo interações cliente-servidor MCP
- **Integração SIEM**: Gerenciamento centralizado de informações e eventos de segurança para detecção de anomalias
- **Análise Comportamental**: Monitoramento com IA para detectar padrões incomuns de comportamento do sistema e do usuário
- **Inteligência de Ameaças**: Integração de feeds externos de ameaças e indicadores de comprometimento (IOCs)
- **Resposta a Incidentes**: Procedimentos bem definidos para detecção, resposta e recuperação de incidentes de segurança

#### **Arquitetura Zero Trust**
- **Nunca Confie, Sempre Verifique**: Verificação contínua de usuários, dispositivos e conexões de rede
- **Microsegmentação**: Controles granulares de rede que isolam cargas de trabalho e serviços individuais
- **Segurança Centrada na Identidade**: Políticas de segurança baseadas em identidades verificadas em vez de localização de rede
- **Avaliação Contínua de Risco**: Avaliação dinâmica da postura de segurança baseada no contexto e comportamento atual
- **Acesso Condicional**: Controles de acesso que se adaptam baseados em fatores de risco, localização e confiança do dispositivo

### Padrões de Integração Empresarial

#### **Integração com Ecossistema de Segurança Microsoft**
- **Microsoft Defender for Cloud**: Gerenciamento abrangente da postura de segurança em nuvem
- **Azure Sentinel**: Capacidades nativas de SIEM e SOAR para proteção de cargas de trabalho de IA
- **Microsoft Entra ID**: Gerenciamento empresarial de identidade e acesso com políticas de acesso condicional
- **Azure Key Vault**: Gerenciamento centralizado de segredos com suporte a módulo de segurança de hardware (HSM)
- **Microsoft Purview**: Governança e conformidade de dados para fontes e fluxos de trabalho de IA

#### **Conformidade & Governança**
- **Alinhamento Regulatório**: Garantir que implementações MCP atendam a requisitos de conformidade específicos de indústria (GDPR, HIPAA, SOC 2)

- **Classificação de Dados**: Categorização adequada e manuseio de dados sensíveis processados por sistemas de IA
- **Rastreamento de Auditoria**: Registro abrangente para conformidade regulatória e investigação forense
- **Controles de Privacidade**: Implementação de princípios de privacidade desde a concepção na arquitetura do sistema de IA
- **Gerenciamento de Mudanças**: Processos formais para revisões de segurança das modificações do sistema de IA

Essas práticas fundamentais criam uma linha de base de segurança robusta que aumenta a eficácia dos controles de segurança específicos do MCP e fornece proteção abrangente para aplicações impulsionadas por IA.

## Principais Lições sobre Segurança

- **Abordagem de Segurança em Camadas**: Combine práticas fundamentais de segurança (codificação segura, menor privilégio, verificação da cadeia de suprimentos, monitoramento contínuo) com controles específicos de IA para proteção abrangente

- **Paisagem de Ameaças Específicas de IA**: Sistemas MCP enfrentam riscos únicos, incluindo injeção de prompt, envenenamento de ferramentas, sequestro de sessão, problemas de delegado confuso, vulnerabilidades de passagem de token e permissões excessivas que requerem mitigações especializadas

- **Excelência em Autenticação & Autorização**: Implemente autenticação robusta usando provedores de identidade externos (Microsoft Entra ID), aplique validação adequada do token e nunca aceite tokens não emitidos explicitamente para seu servidor MCP

- **Prevenção de Ataques à IA**: Implante Microsoft Prompt Shields e Azure Content Safety para defender contra injeção indireta de prompt e ataques de envenenamento de ferramentas, validando metadados de ferramentas e monitorando mudanças dinâmicas

- **Segurança de Sessão e Transporte**: Use IDs de sessão criptograficamente seguros e não determinísticos vinculados às identidades dos usuários, implemente gerenciamento adequado do ciclo de vida da sessão e nunca use sessões para autenticação

- **Melhores Práticas de Segurança OAuth**: Prevenção de ataques de delegado confuso através de consentimento explícito do usuário para clientes registrados dinamicamente, implementação adequada do OAuth 2.1 com PKCE e validação rigorosa do URI de redirecionamento  

- **Princípios de Segurança de Tokens**: Evite anti-padrões de passagem de token, valide declarações de audiência dos tokens, implemente tokens de curta duração com rotação segura e mantenha limites claros de confiança

- **Segurança Abrangente da Cadeia de Suprimentos**: Trate todos os componentes do ecossistema de IA (modelos, embeddings, provedores de contexto, APIs externas) com o mesmo rigor de segurança aplicado às dependências tradicionais de software

- **Evolução Contínua**: Mantenha-se atualizado com as especificações MCP em rápida evolução, contribua para os padrões da comunidade de segurança e mantenha posturas de segurança adaptativas à medida que o protocolo amadurece

- **Integração de Segurança Microsoft**: Aproveite o ecossistema abrangente de segurança da Microsoft (Prompt Shields, Azure Content Safety, GitHub Advanced Security, Entra ID) para proteção reforçada do deployment MCP

## Recursos Abrangentes

### **Documentação Oficial de Segurança MCP**
- [Especificação MCP (Atual: 2026-07-28)](https://modelcontextprotocol.io/specification/2026-07-28/)
- [Melhores Práticas de Segurança MCP](https://modelcontextprotocol.io/specification/2026-07-28/basic/security_best_practices)
- [Especificação de Autorização MCP](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization)
- [Repositório MCP no GitHub](https://github.com/modelcontextprotocol)

### **Recursos de Segurança MCP da OWASP**
- [Guia de Segurança OWASP MCP Azure](https://microsoft.github.io/mcp-azure-security-guide/) - OWASP MCP Top 10 abrangente com orientações para implementação no Azure
- [OWASP MCP Top 10](https://owasp.org/www-project-mcp-top-10/) - Riscos oficiais de segurança MCP da OWASP
- [Workshop do MCP Security Summit (Sherpa)](https://azure-samples.github.io/sherpa/) - Treinamento prático de segurança para MCP no Azure

### **Padrões e Melhores Práticas de Segurança**
- [Melhores Práticas de Segurança OAuth 2.0 (RFC 9700)](https://datatracker.ietf.org/doc/html/rfc9700)
- [Top 10 da OWASP para Segurança de Aplicações Web](https://owasp.org/www-project-top-ten/)
- [Top 10 OWASP para Modelos de Linguagem Grande](https://genai.owasp.org/download/43299/?tmstv=1731900559)
- [Relatório Microsoft de Defesa Digital](https://aka.ms/mddr)

### **Pesquisa e Análise em Segurança de IA**
- [Injeção de Prompt no MCP (Simon Willison)](https://simonwillison.net/2025/Apr/9/mcp-prompt-injection/)
- [Ataques de Envenenamento de Ferramentas (Invariant Labs)](https://invariantlabs.ai/blog/mcp-security-notification-tool-poisoning-attacks)
- [Briefing de Pesquisa de Segurança MCP (Wiz Security)](https://www.wiz.io/blog/mcp-security-research-briefing#remote-servers-22)

### **Soluções de Segurança Microsoft**
- [Documentação Microsoft Prompt Shields](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)
- [Serviço Azure Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/)
- [Segurança Microsoft Entra ID](https://learn.microsoft.com/entra/identity-platform/secure-least-privileged-access)
- [Melhores Práticas de Gerenciamento de Tokens Azure](https://learn.microsoft.com/entra/identity-platform/access-tokens)
- [GitHub Advanced Security](https://github.com/security/advanced-security)

### **Guias de Implementação e Tutoriais**
- [Azure API Management como Gateway de Autenticação MCP](https://techcommunity.microsoft.com/blog/integrationsonazureblog/azure-api-management-your-auth-gateway-for-mcp-servers/4402690)
- [Autenticação Microsoft Entra ID com Servidores MCP](https://den.dev/blog/mcp-server-auth-entra-id-session/)
- [Armazenamento Seguro e Criptografia de Token (Vídeo)](https://youtu.be/uRdX37EcCwg?si=6fSChs1G4glwXRy2)

### **DevOps e Segurança da Cadeia de Suprimentos**
- [Segurança Azure DevOps](https://azure.microsoft.com/products/devops)
- [Segurança Azure Repos](https://azure.microsoft.com/products/devops/repos/)
- [Jornada de Segurança da Cadeia de Suprimentos Microsoft](https://devblogs.microsoft.com/engineering-at-microsoft/the-journey-to-secure-the-software-supply-chain-at-microsoft/)

## **Documentação Adicional de Segurança**

Para orientações abrangentes de segurança, consulte estes documentos especializados nesta seção:

- **[Exemplo de Autorização CIMD e DCR](./samples/cimd-dcr-auth/README.md)** - Servidor de recursos MCP `2026-07-28` em TypeScript executável que compara Documentos de Metadados de Identificação de Cliente preferidos com fallback de Registro Dinâmico de Cliente obsoleto
- **[Melhores Práticas de Segurança MCP](./mcp-security-best-practices.md)** - Melhores práticas completas de segurança para implementações MCP
- **[Implementação Azure Content Safety](./azure-content-safety-implementation.md)** - Exemplos práticos de integração com Azure Content Safety  
- **[Controles de Segurança MCP](./mcp-security-controls.md)** - Controles e técnicas de segurança mais recentes para deployments MCP
- **[Referência Rápida de Melhores Práticas MCP](./mcp-best-practices.md)** - Guia de referência rápida para práticas essenciais de segurança MCP
- **[BlueHat 2026: Protegendo o futuro da IA: Segurança MCP com padrões de defesa em profundidade](https://www.youtube.com/watch?v=cVWB58kEt-Y)** - Padrões de defesa em profundidade do Microsoft Security Response Center (MSRC)

### **Treinamento Prático de Segurança**

- **[Workshop MCP Security Summit (Sherpa)](https://azure-samples.github.io/sherpa/)** - Workshop prático abrangente para proteger servidores MCP no Azure com acampamentos progressivos do Base Camp até o Summit
- **[Guia de Segurança OWASP MCP Azure](https://microsoft.github.io/mcp-azure-security-guide/)** - Arquitetura de referência e orientações de implementação para todos os riscos OWASP MCP Top 10

---

## O que vem a seguir

Próximo: [Capítulo 3: Introdução](../03-GettingStarted/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido usando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, por favor, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->