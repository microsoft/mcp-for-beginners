# Controles de Segurança MCP - Atualização Setembro 2026

> **Padrão atual:** Este documento reflete
> [Especificação MCP 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/)
> e as oficiais
> [Melhores Práticas de Segurança MCP](https://modelcontextprotocol.io/specification/2026-07-28/basic/security_best_practices).

O Protocolo de Contexto do Modelo (MCP) amadureceu significativamente com controles de segurança aprimorados que abordam tanto a segurança tradicional de software quanto ameaças específicas de IA. Este documento fornece controles de segurança abrangentes para implementações seguras do MCP alinhados com o framework OWASP MCP Top 10.

## 🏔️ Treinamento Prático em Segurança

Para experiência prática e mão na massa na implementação de segurança, recomendamos o **[MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/)** - uma expedição guiada abrangente para proteger servidores MCP no Azure usando a metodologia "vulnerável → exploração → correção → validação".

Todos os controles de segurança neste documento estão alinhados com o **[Guia de Segurança Azure MCP da OWASP](https://microsoft.github.io/mcp-azure-security-guide/)**, que fornece arquiteturas de referência e orientações específicas para implementação no Azure dos riscos do OWASP MCP Top 10.

## **Requisitos de Segurança OBRIGATÓRIOS**

### **Proibições Críticas da Especificação MCP:**

> **PROIBIDO**: Servidores MCP **NÃO DEVEM** aceitar quaisquer tokens que não tenham sido explicitamente emitidos para o servidor MCP
>
> **PROIBIDO**: Servidores MCP **NÃO DEVEM** usar sessões para autenticação  
>
> **OBRIGATÓRIO**: Servidores MCP que implementam autorização **DEVEM** verificar TODAS as requisições recebidas
>
> **MANDATÓRIO**: Servidores proxy MCP usando um ID de cliente estático de terceiros
> **DEVEM** obter consentimento para cada cliente MCP antes de encaminhar autorização

---

## 1. **Controles de Autenticação e Autorização**

### **Integração com Provedor de Identidade Externo**

**Especificação MCP `2026-07-28`** permite que servidores MCP deleguem
autenticação a provedores de identidade externos. A autorização para transportes HTTP
é avaliada por requisição; servidores locais stdio obtêm credenciais
diretamente de seu ambiente.

**Risco OWASP MCP Abordado**: [MCP07 - Autenticação e Autorização Insuficientes](https://microsoft.github.io/mcp-azure-security-guide/mcp/mcp07-authz/)

**Benefícios de Segurança:**
1. **Elimina Riscos de Autenticação Customizada**: Reduz a superfície vulnerável ao evitar implementações customizadas de autenticação
2. **Segurança de Nível Empresarial**: Aproveita provedores de identidade estabelecidos como Microsoft Entra ID com recursos avançados de segurança
3. **Gestão Centralizada de Identidade**: Simplifica o ciclo de vida do usuário, controle de acesso e auditorias de conformidade
4. **Autenticação Multifator**: Herda capacidades de MFA dos provedores de identidade empresariais
5. **Políticas de Acesso Condicional**: Beneficia-se de controles de acesso baseados em risco e autenticação adaptativa

**Requisitos de Implementação:**
- **Registro de Cliente**: Prefira Documentos de Metadados de ID do Cliente ou
  pré-registro; use Registro Dinâmico de Cliente obsoleto apenas para
  compatibilidade
- **Validação da Audiência do Token**: Verifique que todos os tokens são explicitamente emitidos para o servidor MCP
- **Verificação do Emissor**: Valide que o emissor do token corresponde ao provedor de identidade esperado
- **Verificação da Assinatura**: Validação criptográfica da integridade do token
- **Aplicação de Expiração**: Aplicação rigorosa dos limites de vida útil do token
- **Validação do Escopo**: Garanta que os tokens contenham permissões apropriadas para as operações solicitadas

### **Segurança da Lógica de Autorização**

**Controles Críticos:**
- **Auditorias Abrangentes de Autorização**: Revisões regulares de segurança de todos os pontos de decisão de autorização
- **Padrões Fail-Safe**: Negar acesso quando a lógica de autorização não puder tomar uma decisão definitiva
- **Limites de Permissão**: Separação clara entre diferentes níveis de privilégio e acesso a recursos
- **Registro de Auditoria**: Registro completo de todas as decisões de autorização para monitoramento de segurança
- **Revisões Regulares de Acesso**: Validação periódica das permissões de usuário e atribuições de privilégios

## 2. **Segurança de Token e Controles Anti-Passthrough**

**Risco OWASP MCP Abordado**: [MCP01 - Má Gestão de Token e Exposição de Segredos](https://microsoft.github.io/mcp-azure-security-guide/mcp/mcp01-token-mismanagement/)

### **Prevenção de Passagem de Token (Passthrough)**

**A passagem de token é explicitamente proibida** na Especificação de Autorização MCP devido a riscos críticos de segurança:

**Riscos de Segurança Abordados:**
- **Circunvenção de Controles**: Bypassa controles essenciais de segurança como limitação de taxa, validação de requisição e monitoramento de tráfego
- **Falha na Responsabilidade**: Torna impossível a identificação do cliente, corrompendo trilhas de auditoria e investigação de incidentes
- **Exfiltração via Proxy**: Permite que agentes maliciosos usem servidores como proxies para acesso não autorizado a dados
- **Violação de Limites de Confiança**: Quebra suposições de confiança do serviço downstream sobre a origem dos tokens
- **Movimentação Lateral**: Tokens comprometidos em múltiplos serviços permitem expansão maior do ataque

**Controles de Implementação:**
```yaml
Token Validation Requirements:
  audience_validation: MANDATORY
  issuer_verification: MANDATORY  
  signature_check: MANDATORY
  expiration_enforcement: MANDATORY
  scope_validation: MANDATORY
  
Token Lifecycle Management:
  rotation_frequency: "Short-lived tokens preferred"
  secure_storage: "Azure Key Vault or equivalent"
  transmission_security: "TLS 1.3 minimum"
  replay_protection: "Implemented via nonce/timestamp"
```

### **Padrões Seguros de Gerenciamento de Token**

**Melhores Práticas:**
- **Tokens de Curta Duração**: Minimize a janela de exposição com rotação frequente de tokens
- **Emissão Just-in-Time**: Emita tokens somente quando necessário para operações específicas
- **Armazenamento Seguro**: Use módulos de segurança de hardware (HSMs) ou cofres de chaves seguros
- **Vinculação de Token**: Valide audiência e emissor do token para o recurso, cliente e operação MCP pretendidos

- **Monitoramento e Alerta**: Detecção em tempo real de uso indevido de token ou padrões de acesso não autorizados

## 3. **Controles de Segurança do Estado da Aplicação**

### **Prevenção de Sequestro de Handles de Estado**

**Vetores de Ataque Abordados:**
- **Palpite de Handle**: Identificadores previsíveis expõem o estado de outro requisitante
- **Reuso entre usuários**: Um handle roubado é usado com uma identidade diferente
- **Autorização Implícita**: Posse de um handle é incorretamente tratada como
  prova de acesso

**Controles de Handle de Estado:**

```yaml
State Handle Generation:
  randomness_source: "Cryptographically secure RNG"
  entropy_bits: 128 # Minimum recommended
  format: "Base64url encoded"
  predictability: "MUST be non-deterministic"

State Binding:
  user_binding: "Bind server-side to the authenticated principal"
  authorization: "Recheck on every request"
  client_input: "Never trust a client-supplied user ID"
  
State Lifecycle:
  expiration: "Configurable timeout policies"
  rotation: "After privilege escalation events"
  invalidation: "Immediate on security events"
  cleanup: "Automated expired state removal"
```

**Segurança do Transporte:**
- **Aplicação de HTTPS**: Requer HTTPS para transportes HTTP remotos
- **Manuseio de Credenciais**: Envie e valide autorização em cada requisição HTTP
- **Isolamento stdio**: Proteja servidores locais stdio através de isolamento de processos e
  controles de credenciais de ambiente

### **Considerações Stateful vs Stateless**

MCP `2026-07-28` é stateless na camada de protocolo. Aplicações ainda podem
manter estado retornando um handle explícito de uma chamada de ferramenta e aceitando
este como argumento comum em chamadas subsequentes.

- Armazene estado independentemente de qualquer conexão de transporte única.
- Vincule handles de estado ao servidor principal autenticado.
- Trate um handle como um nome, não como credencial do portador.
- Defina comportamento de expiração e recuperação para handles obsoletos.

## 4. **Controles de Segurança Específicos para IA**

**Riscos OWASP MCP Abordados**:

- [MCP06 - Subversão do Fluxo de Intenção](https://microsoft.github.io/mcp-azure-security-guide/mcp/mcp06-prompt-injection/)
- [MCP03 - Envenenamento de Ferramentas](https://microsoft.github.io/mcp-azure-security-guide/mcp/mcp03-tool-poisoning/)
- [MCP05 - Injeção e Execução de Comandos](https://microsoft.github.io/mcp-azure-security-guide/mcp/mcp05-command-injection/)

### **Defesa Contra Injeção de Prompt**

**Integração do Microsoft Prompt Shields:**
```yaml
Detection Mechanisms:
  - "Advanced ML-based instruction detection"
  - "Contextual analysis of external content"
  - "Real-time threat pattern recognition"
  
Protection Techniques:
  - "Spotlighting trusted vs untrusted content"
  - "Delimiter systems for content boundaries"  
  - "Data marking for content source identification"
  
Integration Points:
  - "Azure Content Safety service"
  - "Real-time content filtering"
  - "Threat intelligence updates"
```

**Controles de Implementação:**
- **Sanitização de Entrada**: Validação e filtragem abrangente de todas as entradas do usuário
- **Definição de Limites de Conteúdo**: Separação clara entre instruções do sistema e conteúdo do usuário
- **Hierarquia de Instruções**: Regras de precedência adequadas para instruções conflitantes
- **Monitoramento de Saída**: Detecção de saídas potencialmente nocivas ou manipuladas

### **Prevenção de Envenenamento de Ferramentas**

**Estrutura de Segurança para Ferramentas:**
```yaml
Tool Definition Protection:
  validation:
    - "Schema validation against expected formats"
    - "Content analysis for malicious instructions" 
    - "Parameter injection detection"
    - "Hidden instruction identification"
  
  integrity_verification:
    - "Cryptographic hashing of tool definitions"
    - "Digital signatures for tool packages"
    - "Version control with change auditing"
    - "Tamper detection mechanisms"
  
  monitoring:
    - "Real-time change detection"
    - "Behavioral analysis of tool usage"
    - "Anomaly detection for execution patterns"
    - "Automated alerting for suspicious modifications"
```

**Gerenciamento Dinâmico de Ferramentas:**
- **Fluxos de Aprovação**: Consentimento explícito do usuário para modificações de ferramentas
- **Capacidades de Reversão**: Capacidade de reverter para versões anteriores das ferramentas
- **Auditoria de Alterações**: Histórico completo das modificações na definição das ferramentas
- **Avaliação de Risco**: Avaliação automatizada da postura de segurança da ferramenta

## 5. **Prevenção de Ataque do Procurador Confuso**

### **Segurança de Proxy OAuth**

**Controles de Prevenção de Ataques:**
```yaml
Client Registration:
  preferred_methods:
    - "Pre-registration when client and server have an existing relationship"
    - "Client ID Metadata Documents for clients without prior registration"
  compatibility_fallback:
    - "Dynamic Client Registration only when CIMD is unavailable"
    - "Consent bypass prevention mechanisms"  
    - "Cookie-based consent validation"
    - "Redirect URI strict validation"
    
  authorization_flow:
    - "PKCE implementation (OAuth 2.1)"
    - "State parameter validation"
    - "Authorization code binding"
    - "Nonce verification for ID tokens"
```

**Requisitos de Implementação:**
- **Registro do Cliente**: Preferência por pré-registro ou Documentos de Metadados do ID do Cliente
  ; tratar o Registro Dinâmico de Clientes como uma alternativa de compatibilidade
- **Verificação de Consentimento do Usuário**: Proxies MCP usando um cliente estático de terceiros
  devem obter consentimento por cliente antes de encaminhar a autorização
- **Validação de URI de Redirecionamento**: Validação rigorosa baseada em lista branca dos destinos de redirecionamento
- **Proteção do Código de Autorização**: Códigos de curta duração com aplicação de uso único
- **Verificação de Identidade do Cliente**: Validação robusta das credenciais e metadados do cliente

## 6. **Segurança na Execução de Ferramentas**

### **Sandboxing e Isolamento**

**Isolamento Baseado em Contêiner:**
```yaml
Execution Environment:
  containerization: "Docker/Podman with security profiles"
  resource_limits:
    cpu: "Configurable CPU quotas"
    memory: "Memory usage restrictions"
    disk: "Storage access limitations"
    network: "Network policy enforcement"
  
  privilege_restrictions:
    user_context: "Non-root execution mandatory"
    capability_dropping: "Remove unnecessary Linux capabilities"
    syscall_filtering: "Seccomp profiles for syscall restriction"
    filesystem: "Read-only root with minimal writable areas"
```

**Isolamento de Processos:**
- **Contextos Separados de Processo**: Cada execução de ferramenta em espaço de processo isolado
- **Comunicação Interprocessos**: Mecanismos IPC seguros com validação
- **Monitoramento de Processos**: Análise do comportamento em tempo de execução e detecção de anomalias
- **Imposição de Recursos**: Limites rígidos em CPU, memória e operações de E/S

### **Implementação do Princípio do Menor Privilégio**

**Gerenciamento de Permissões:**
```yaml
Access Control:
  file_system:
    - "Minimal required directory access"
    - "Read-only access where possible"
    - "Temporary file cleanup automation"
    
  network_access:
    - "Explicit allowlist for external connections"
    - "DNS resolution restrictions" 
    - "Port access limitations"
    - "SSL/TLS certificate validation"
  
  system_resources:
    - "No administrative privilege elevation"
    - "Limited system call access"
    - "No hardware device access"
    - "Restricted environment variable access"
```

## 7. **Controles de Segurança da Cadeia de Suprimentos**

**Risco OWASP MCP Abordado**: [MCP04 - Ataques à Cadeia de Suprimentos de Software e Manipulação de Dependências](https://microsoft.github.io/mcp-azure-security-guide/mcp/mcp04-supply-chain/)

### **Verificação de Dependências**

**Segurança Abrangente dos Componentes:**
```yaml
Software Dependencies:
  scanning: 
    - "Automated vulnerability scanning (GitHub Advanced Security)"
    - "License compliance verification"
    - "Known vulnerability database checks"
    - "Malware detection and analysis"
  
  verification:
    - "Package signature verification"
    - "Checksum validation"
    - "Provenance attestation"
    - "Software Bill of Materials (SBOM)"

AI Components:
  model_verification:
    - "Model provenance validation"
    - "Training data source verification" 
    - "Model behavior testing"
    - "Adversarial robustness assessment"
  
  service_validation:
    - "Third-party API security assessment"
    - "Service level agreement review"
    - "Data handling compliance verification"
    - "Incident response capability evaluation"
```

### **Monitoramento Contínuo**

**Detecção de Ameaças na Cadeia de Suprimentos:**
- **Monitoramento da Saúde das Dependências**: Avaliação contínua de todas as dependências para problemas de segurança
- **Integração de Inteligência de Ameaças**: Atualizações em tempo real sobre ameaças emergentes na cadeia de suprimentos
- **Análise Comportamental**: Detecção de comportamento incomum em componentes externos
- **Resposta Automatizada**: Contenção imediata de componentes comprometidos

## 8. **Controles de Monitoramento e Detecção**

**Risco OWASP MCP Abordado**: [MCP08 - Falta de Auditoria e Telemetria](https://microsoft.github.io/mcp-azure-security-guide/mcp/mcp08-telemetry/)

### **Gerenciamento de Informações e Eventos de Segurança (SIEM)**

**Estratégia Abrangente de Registro:**
```yaml
Authentication Events:
  - "All authentication attempts (success/failure)"
  - "Token issuance and validation events"
  - "Session creation, modification, termination"
  - "Authorization decisions and policy evaluations"

Tool Execution:
  - "Tool invocation details and parameters"
  - "Execution duration and resource usage"
  - "Output generation and content analysis"
  - "Error conditions and exception handling"

Security Events:
  - "Potential prompt injection attempts"
  - "Tool poisoning detection events"
  - "Session hijacking indicators"
  - "Unusual access patterns and anomalies"
```

### **Detecção de Ameaças em Tempo Real**

**Análise Comportamental:**
- **Análise de Comportamento do Usuário (UBA)**: Detecção de padrões incomuns de acesso do usuário
- **Análise de Comportamento de Entidade (EBA)**: Monitoramento do comportamento do servidor MCP e das ferramentas
- **Detecção de Anomalias com Aprendizado de Máquina**: Identificação de ameaças de segurança impulsionada por IA
- **Correlação de Inteligência de Ameaças**: Correspondência de atividades observadas com padrões de ataques conhecidos

## 9. **Resposta e Recuperação de Incidentes**

### **Capacidades de Resposta Automatizada**

**Ações de Resposta Imediata:**
```yaml
Threat Containment:
  session_management:
    - "Immediate session termination"
    - "Account lockout procedures"
    - "Access privilege revocation"
  
  system_isolation:
    - "Network segmentation activation"
    - "Service isolation protocols"
    - "Communication channel restriction"

Recovery Procedures:
  credential_rotation:
    - "Automated token refresh"
    - "API key regeneration"
    - "Certificate renewal"
  
  system_restoration:
    - "Clean state restoration"
    - "Configuration rollback"
    - "Service restart procedures"
```

### **Capacidades Forenses**

**Suporte à Investigação:**
- **Preservação da Trilha de Auditoria**: Registro imutável com integridade criptográfica
- **Coleta de Evidências**: Reunião automatizada de artefatos de segurança relevantes
- **Reconstrução de Linha do Tempo**: Sequência detalhada de eventos que levaram a incidentes de segurança
- **Avaliação de Impacto**: Avaliação do escopo de comprometimento e exposição de dados

## **Princípios Chave da Arquitetura de Segurança**

### **Defesa em Profundidade**
- **Múltiplas Camadas de Segurança**: Nenhum ponto único de falha na arquitetura de segurança
- **Controles Redundantes**: Medidas de segurança sobrepostas para funções críticas
- **Mecanismos de Segurança Garantida**: Padrões seguros quando sistemas encontram erros ou ataques

### **Implementação Zero Trust**
- **Nunca Confie, Sempre Verifique**: Validação contínua de todas as entidades e solicitações
- **Princípio do Menor Privilégio**: Direitos de acesso mínimos para todos os componentes
- **Microsegmentação**: Controles granulares de rede e acesso

### **Evolução Contínua da Segurança**
- **Adaptação ao Cenário de Ameaças**: Atualizações regulares para enfrentar ameaças emergentes
- **Efetividade dos Controles de Segurança**: Avaliação e aprimoramento contínuos dos controles
- **Conformidade com Especificações**: Alinhamento com os padrões de segurança MCP em evolução

---

## **Recursos para Implementação**

### **Documentação Oficial MCP**
- [Especificação MCP (2026-07-28)](https://modelcontextprotocol.io/specification/2026-07-28/)
- [Melhores Práticas de Segurança MCP](https://modelcontextprotocol.io/specification/2026-07-28/basic/security_best_practices)
- [Especificação de Autorização MCP](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization)

### **Recursos de Segurança OWASP MCP**
- [Guia de Segurança OWASP MCP Azure](https://microsoft.github.io/mcp-azure-security-guide/) - Top 10 OWASP MCP abrangente com implementação Azure
- [Top 10 OWASP MCP](https://owasp.org/www-project-mcp-top-10/) - Riscos oficiais de segurança OWASP MCP
- [Workshop MCP Security Summit (Sherpa)](https://azure-samples.github.io/sherpa/) - Treinamento prático de segurança para MCP no Azure

### **Soluções de Segurança Microsoft**
- [Microsoft Prompt Shields](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)
- [Azure Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/)
- [GitHub Advanced Security](https://github.com/security/advanced-security)
- [Azure Key Vault](https://learn.microsoft.com/azure/key-vault/)

### **Padrões de Segurança**
- [Melhores Práticas de Segurança OAuth 2.0 (RFC 9700)](https://datatracker.ietf.org/doc/html/rfc9700)

- [OWASP Top 10 para Grandes Modelos de Linguagem](https://genai.owasp.org/)

- [NIST Cybersecurity Framework](https://www.nist.gov/cyberframework)

---

> **Importante:** Estes controles de segurança refletem a Especificação MCP
> `2026-07-28`. Sempre verifique na
> [documentação oficial atual](https://modelcontextprotocol.io/specification/2026-07-28/)
> à medida que os padrões continuam a evoluir.

## O que vem a seguir

- Voltar para: [Visão Geral do Módulo de Segurança](./README.md)
- Continuar para: [Módulo 3: Começando](../03-GettingStarted/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido usando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, por favor, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->