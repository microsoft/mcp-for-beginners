# Controlo de Segurança MCP - Atualização de Dezembro de 2025

> **Padrão Atual**: Este documento reflete os requisitos de segurança da [Especificação MCP 2025-11-25](https://spec.modelcontextprotocol.io/specification/2025-11-25/) e as [Melhores Práticas de Segurança MCP](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices) oficiais.

O Protocolo de Contexto de Modelo (MCP) amadureceu significativamente com controlos de segurança aprimorados que abordam tanto a segurança tradicional de software como as ameaças específicas de IA. Este documento fornece controlos de segurança abrangentes para implementações seguras do MCP a partir de dezembro de 2025.

## **Requisitos de Segurança OBRIGATÓRIOS**

### **Proibições Críticas da Especificação MCP:**

> **PROIBIDO**: Os servidores MCP **NÃO DEVEM** aceitar quaisquer tokens que não tenham sido explicitamente emitidos para o servidor MCP  
>
> **PROIBIDO**: Os servidores MCP **NÃO DEVEM** usar sessões para autenticação  
>
> **OBRIGATÓRIO**: Os servidores MCP que implementam autorização **DEVEM** verificar TODAS as solicitações recebidas  
>
> **MANDATÓRIO**: Os servidores proxy MCP que usam IDs de cliente estáticos **DEVEM** obter consentimento do utilizador para cada cliente registado dinamicamente

---

## 1. **Controlos de Autenticação e Autorização**

### **Integração com Provedor de Identidade Externo**

**Padrão MCP Atual (2025-06-18)** permite que servidores MCP deleguem a autenticação a provedores de identidade externos, representando uma melhoria significativa na segurança:

### **Integração com Provedor de Identidade Externo**

**Padrão MCP Atual (2025-11-25)** permite que servidores MCP deleguem a autenticação a provedores de identidade externos, representando uma melhoria significativa na segurança:

**Benefícios de Segurança:**
1. **Elimina Riscos de Autenticação Personalizada**: Reduz a superfície de vulnerabilidade ao evitar implementações personalizadas de autenticação  
2. **Segurança de Nível Empresarial**: Aproveita provedores de identidade estabelecidos como Microsoft Entra ID com funcionalidades avançadas de segurança  
3. **Gestão Centralizada de Identidade**: Simplifica o ciclo de vida do utilizador, controlo de acesso e auditoria de conformidade  
4. **Autenticação Multifator**: Herda capacidades MFA dos provedores de identidade empresariais  
5. **Políticas de Acesso Condicional**: Beneficia de controlos de acesso baseados em risco e autenticação adaptativa

**Requisitos de Implementação:**
- **Validação do Público do Token**: Verificar que todos os tokens são explicitamente emitidos para o servidor MCP  
- **Verificação do Emissor**: Validar que o emissor do token corresponde ao provedor de identidade esperado  
- **Verificação da Assinatura**: Validação criptográfica da integridade do token  
- **Cumprimento do Prazo de Validade**: Aplicação rigorosa dos limites de tempo de vida do token  
- **Validação do Escopo**: Garantir que os tokens contêm permissões apropriadas para as operações solicitadas

### **Segurança da Lógica de Autorização**

**Controlos Críticos:**
- **Auditorias Abrangentes de Autorização**: Revisões regulares de segurança de todos os pontos de decisão de autorização  
- **Padrões Fail-Safe**: Negar acesso quando a lógica de autorização não pode tomar uma decisão definitiva  
- **Limites de Permissão**: Separação clara entre diferentes níveis de privilégio e acesso a recursos  
- **Registo de Auditoria**: Registo completo de todas as decisões de autorização para monitorização de segurança  
- **Revisões Regulares de Acesso**: Validação periódica das permissões dos utilizadores e atribuições de privilégios

## 2. **Segurança de Tokens e Controlos Anti-Passthrough**

### **Prevenção de Passthrough de Token**

**O passthrough de token é explicitamente proibido** na Especificação de Autorização MCP devido a riscos críticos de segurança:

**Riscos de Segurança Abordados:**
- **Circunvenção de Controlo**: Ignora controlos essenciais de segurança como limitação de taxa, validação de pedidos e monitorização de tráfego  
- **Quebra de Responsabilidade**: Torna impossível a identificação do cliente, corrompendo trilhas de auditoria e investigação de incidentes  
- **Exfiltração Baseada em Proxy**: Permite que atores maliciosos usem servidores como proxies para acesso não autorizado a dados  
- **Violações de Limites de Confiança**: Quebra as suposições de confiança dos serviços a jusante sobre a origem dos tokens  
- **Movimento Lateral**: Tokens comprometidos em múltiplos serviços permitem expansão mais ampla do ataque

**Controlos de Implementação:**
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

### **Padrões Seguros de Gestão de Tokens**

**Melhores Práticas:**
- **Tokens de Curta Duração**: Minimizar a janela de exposição com rotação frequente de tokens  
- **Emissão Just-in-Time**: Emitir tokens apenas quando necessários para operações específicas  
- **Armazenamento Seguro**: Usar módulos de segurança de hardware (HSMs) ou cofres de chaves seguros  
- **Vinculação de Tokens**: Vincular tokens a clientes, sessões ou operações específicas sempre que possível  
- **Monitorização e Alertas**: Detecção em tempo real de uso indevido de tokens ou padrões de acesso não autorizados

## 3. **Controlos de Segurança de Sessão**

### **Prevenção de Sequestro de Sessão**

**Vetores de Ataque Abordados:**
- **Injeção de Prompt de Sequestro de Sessão**: Eventos maliciosos injetados no estado de sessão partilhado  
- **Impersonação de Sessão**: Uso não autorizado de IDs de sessão roubados para contornar autenticação  
- **Ataques de Retoma de Stream**: Exploração da retoma de eventos enviados pelo servidor para injeção de conteúdo malicioso

**Controlos Obrigatórios de Sessão:**
```yaml
Session ID Generation:
  randomness_source: "Cryptographically secure RNG"
  entropy_bits: 128 # Minimum recommended
  format: "Base64url encoded"
  predictability: "MUST be non-deterministic"

Session Binding:
  user_binding: "REQUIRED - <user_id>:<session_id>"
  additional_identifiers: "Device fingerprint, IP validation"
  context_binding: "Request origin, user agent validation"
  
Session Lifecycle:
  expiration: "Configurable timeout policies"
  rotation: "After privilege escalation events"
  invalidation: "Immediate on security events"
  cleanup: "Automated expired session removal"
```

**Segurança de Transporte:**
- **Aplicação de HTTPS**: Toda a comunicação de sessão sobre TLS 1.3  
- **Atributos Seguros de Cookie**: HttpOnly, Secure, SameSite=Strict  
- **Fixação de Certificado**: Para conexões críticas para prevenir ataques MITM

### **Considerações Stateful vs Stateless**

**Para Implementações Stateful:**
- O estado de sessão partilhado requer proteção adicional contra ataques de injeção  
- A gestão de sessão baseada em filas necessita de verificação de integridade  
- Múltiplas instâncias de servidor requerem sincronização segura do estado da sessão

**Para Implementações Stateless:**
- Gestão de sessão baseada em JWT ou tokens similares  
- Verificação criptográfica da integridade do estado da sessão  
- Superfície de ataque reduzida, mas requer validação robusta de tokens

## 4. **Controlos de Segurança Específicos para IA**

### **Defesa contra Injeção de Prompt**

**Integração Microsoft Prompt Shields:**
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

**Controlos de Implementação:**
- **Sanitização de Entrada**: Validação e filtragem abrangente de todas as entradas do utilizador  
- **Definição de Limites de Conteúdo**: Separação clara entre instruções do sistema e conteúdo do utilizador  
- **Hierarquia de Instruções**: Regras de precedência adequadas para instruções conflitantes  
- **Monitorização de Saída**: Detecção de saídas potencialmente prejudiciais ou manipuladas

### **Prevenção de Envenenamento de Ferramentas**

**Estrutura de Segurança de Ferramentas:**
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

**Gestão Dinâmica de Ferramentas:**
- **Fluxos de Aprovação**: Consentimento explícito do utilizador para modificações de ferramentas  
- **Capacidades de Reversão**: Capacidade de reverter para versões anteriores da ferramenta  
- **Auditoria de Alterações**: Histórico completo das modificações da definição da ferramenta  
- **Avaliação de Risco**: Avaliação automatizada da postura de segurança da ferramenta

## 5. **Prevenção de Ataques Confused Deputy**

### **Segurança de Proxy OAuth**

**Controlos de Prevenção de Ataques:**
```yaml
Client Registration:
  static_client_protection:
    - "Explicit user consent for dynamic registration"
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
- **Verificação de Consentimento do Utilizador**: Nunca omitir ecrãs de consentimento para registo dinâmico de clientes  
- **Validação de URI de Redirecionamento**: Validação rigorosa baseada em lista branca dos destinos de redirecionamento  
- **Proteção do Código de Autorização**: Códigos de curta duração com aplicação de uso único  
- **Verificação de Identidade do Cliente**: Validação robusta das credenciais e metadados do cliente

## 6. **Segurança na Execução de Ferramentas**

### **Sandboxing e Isolamento**

**Isolamento Baseado em Contêineres:**
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
- **Contextos de Processo Separados**: Cada execução de ferramenta em espaço de processo isolado  
- **Comunicação Interprocessos**: Mecanismos seguros de IPC com validação  
- **Monitorização de Processos**: Análise de comportamento em tempo de execução e deteção de anomalias  
- **Aplicação de Recursos**: Limites rígidos em CPU, memória e operações de I/O

### **Implementação do Princípio do Menor Privilégio**

**Gestão de Permissões:**
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

## 7. **Controlos de Segurança da Cadeia de Abastecimento**

### **Verificação de Dependências**

**Segurança Abrangente de Componentes:**
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

### **Monitorização Contínua**

**Deteção de Ameaças na Cadeia de Abastecimento:**
- **Monitorização da Saúde das Dependências**: Avaliação contínua de todas as dependências para questões de segurança  
- **Integração de Inteligência de Ameaças**: Atualizações em tempo real sobre ameaças emergentes na cadeia de abastecimento  
- **Análise Comportamental**: Deteção de comportamentos invulgares em componentes externos  
- **Resposta Automatizada**: Contenção imediata de componentes comprometidos

## 8. **Controlos de Monitorização e Deteção**

### **Gestão de Informação e Eventos de Segurança (SIEM)**

**Estratégia Abrangente de Registo:**
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

### **Deteção de Ameaças em Tempo Real**

**Análise Comportamental:**
- **Análise de Comportamento do Utilizador (UBA)**: Deteção de padrões invulgares de acesso do utilizador  
- **Análise de Comportamento de Entidades (EBA)**: Monitorização do comportamento do servidor MCP e ferramentas  
- **Deteção de Anomalias com Aprendizagem Automática**: Identificação de ameaças de segurança com IA  
- **Correlação de Inteligência de Ameaças**: Correspondência de atividades observadas com padrões de ataque conhecidos

## 9. **Resposta a Incidentes e Recuperação**

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
- **Preservação da Trilha de Auditoria**: Registo imutável com integridade criptográfica  
- **Recolha de Evidências**: Recolha automatizada de artefactos de segurança relevantes  
- **Reconstrução da Linha Temporal**: Sequência detalhada de eventos que levaram a incidentes de segurança  
- **Avaliação de Impacto**: Avaliação do âmbito do comprometimento e exposição de dados

## **Princípios-Chave da Arquitetura de Segurança**

### **Defesa em Profundidade**
- **Múltiplas Camadas de Segurança**: Nenhum ponto único de falha na arquitetura de segurança  
- **Controlos Redundantes**: Medidas de segurança sobrepostas para funções críticas  
- **Mecanismos Fail-Safe**: Padrões seguros quando sistemas enfrentam erros ou ataques

### **Implementação Zero Trust**
- **Nunca Confiar, Sempre Verificar**: Validação contínua de todas as entidades e pedidos  
- **Princípio do Menor Privilégio**: Direitos de acesso mínimos para todos os componentes  
- **Microsegmentação**: Controlos granulares de rede e acesso

### **Evolução Contínua da Segurança**
- **Adaptação ao Cenário de Ameaças**: Atualizações regulares para abordar ameaças emergentes  
- **Eficácia dos Controlos de Segurança**: Avaliação e melhoria contínua dos controlos  
- **Conformidade com a Especificação**: Alinhamento com os padrões de segurança MCP em evolução

---

## **Recursos de Implementação**

### **Documentação Oficial MCP**
- [Especificação MCP (2025-11-25)](https://spec.modelcontextprotocol.io/specification/2025-11-25/)
- [Melhores Práticas de Segurança MCP](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices)
- [Especificação de Autorização MCP](https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization)

### **Soluções de Segurança Microsoft**
- [Microsoft Prompt Shields](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)
- [Azure Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/)
- [GitHub Advanced Security](https://github.com/security/advanced-security)
- [Azure Key Vault](https://learn.microsoft.com/azure/key-vault/)

### **Normas de Segurança**
- [Melhores Práticas de Segurança OAuth 2.0 (RFC 9700)](https://datatracker.ietf.org/doc/html/rfc9700)
- [OWASP Top 10 para Modelos de Linguagem Grande](https://genai.owasp.org/)
- [Framework de Cibersegurança NIST](https://www.nist.gov/cyberframework)

---

> **Importante**: Estes controlos de segurança refletem a especificação MCP atual (2025-06-18). Verifique sempre a [documentação oficial](https://spec.modelcontextprotocol.io/) mais recente, pois os padrões continuam a evoluir rapidamente.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, por favor tenha em conta que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se a tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações erradas decorrentes do uso desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->