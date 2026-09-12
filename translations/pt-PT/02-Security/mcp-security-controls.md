# Controlo de Segurança MCP - Atualização de Setembro 2026

> **Padrão atual:** Este documento reflete
> [Especificação MCP 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/)
> e as oficiais
> [Melhores Práticas de Segurança MCP](https://modelcontextprotocol.io/specification/2026-07-28/basic/security_best_practices).

O Protocolo de Contexto do Modelo (MCP) amadureceu significativamente com controlos de segurança melhorados que abordam tanto a segurança tradicional de software como ameaças específicas de IA. Este documento fornece controlos de segurança abrangentes para implementações seguras do MCP alinhadas com o quadro OWASP MCP Top 10.

## 🏔️ Treino Prático em Segurança

Para uma experiência prática de implementação de segurança, recomendamos o **[Workshop MCP Security Summit (Sherpa)](https://azure-samples.github.io/sherpa/)** - uma expedição guiada abrangente para assegurar servidores MCP no Azure usando uma metodologia "vulnerável → exploitar → corrigir → validar".

Todos os controlos de segurança neste documento estão alinhados com o **[Guia de Segurança Azure MCP OWASP](https://microsoft.github.io/mcp-azure-security-guide/)**, que fornece arquiteturas de referência e orientações específicas para implementação no Azure dos riscos OWASP MCP Top 10.

## **Requisitos de Segurança OBRIGATÓRIOS**

### **Proibições Críticas da Especificação MCP:**

> **PROIBIDO**: Servidores MCP **NÃO DEVEM** aceitar quaisquer tokens que não tenham sido explicitamente emitidos para o servidor MCP
>
> **PROIBIDO**: Servidores MCP **NÃO DEVEM** usar sessões para autenticação  
>
> **OBRIGATÓRIO**: Servidores MCP que implementem autorização **DEVEM** verificar TODAS as solicitações recebidas
>
> **MANDATÓRIO**: Servidores proxy MCP que usem um ID estático de cliente terceirizado
> **DEVEM** obter consentimento para cada cliente MCP antes de encaminhar a autorização

---

## 1. **Controlos de Autenticação & Autorização**

### **Integração com Fornecedores de Identidade Externos**

**Especificação MCP `2026-07-28`** permite que servidores MCP deleguem
autenticação a fornecedores de identidade externos. Autorização para transportes HTTP
é avaliada por solicitação; servidores locais stdio obtêm credenciais
a partir do seu ambiente em vez disso.

**Risco OWASP MCP Abordado**: [MCP07 - Autenticação e Autorização Insuficientes](https://microsoft.github.io/mcp-azure-security-guide/mcp/mcp07-authz/)

**Benefícios de Segurança:**
1. **Elimina Riscos de Autenticação Personalizada**: Reduz a superfície de vulnerabilidade evitando implementações de autenticação personalizadas
2. **Segurança ao Nível Empresarial**: Aproveita fornecedores de identidade estabelecidos como Microsoft Entra ID com funcionalidades avançadas de segurança
3. **Gestão Centralizada de Identidade**: Simplifica o ciclo de vida do utilizador, controlo de acesso e auditoria de conformidade
4. **Autenticação Multi-Fator**: Herda capacidades MFA dos fornecedores de identidade empresariais
5. **Políticas de Acesso Condicional**: Beneficia de controlos de acesso baseados em risco e autenticação adaptativa

**Requisitos de Implementação:**
- **Registo do Cliente**: Preferir Documentos de Metadados de ID de Cliente ou
  pré-registo; usar Registo Dinâmico de Cliente obsoleto somente para
  compatibilidade
- **Validação do Destinatário do Token**: Verificar que todos os tokens são explicitamente emitidos para o servidor MCP
- **Verificação do Emissor**: Validar que o emissor do token corresponde ao fornecedor de identidade esperado
- **Verificação da Assinatura**: Validação criptográfica da integridade do token
- **Aplicação de Expiração**: Aplicação rigorosa dos limites da duração do token
- **Validação do Âmbito**: Garantir que os tokens contêm permissões adequadas para as operações solicitadas

### **Segurança da Lógica de Autorização**

**Controlos Críticos:**
- **Auditorias Abrangentes de Autorização**: Revisões regulares de segurança de todos os pontos de decisão de autorização
- **Predefinições Seguras por Omissão**: Negar acesso quando a lógica de autorização não puder tomar uma decisão definitiva
- **Limites de Permissão**: Separação clara entre diferentes níveis de privilégio e acesso a recursos
- **Registo de Auditoria**: Registo completo de todas as decisões de autorização para monitorização de segurança
- **Revisões Regulares de Acesso**: Validação periódica das permissões de utilizadores e atribuições de privilégios

## 2. **Controlos de Segurança e Anti-Passthrough de Tokens**

**Risco OWASP MCP Abordado**: [MCP01 - Má Gestão de Tokens & Exposição de Segredos](https://microsoft.github.io/mcp-azure-security-guide/mcp/mcp01-token-mismanagement/)

### **Prevenção de Passthrough de Token**

**Passthrough de token é explicitamente proibido** na Especificação de Autorização MCP devido a riscos críticos de segurança:

**Riscos de Segurança Abordados:**
- **Contorno de Controlo**: Contorna controlos de segurança essenciais como limitação de taxa, validação de pedidos e monitorização de tráfego
- **Quebra de Responsabilização**: Torna impossível a identificação do cliente, corrompendo trilhas de auditoria e investigação de incidentes
- **Exfiltração Baseada em Proxy**: Permite a atores maliciosos usar servidores como proxies para acesso não autorizado a dados
- **Violações de Limite de Confiança**: Quebra suposições de confiança de serviços downstream sobre a origem dos tokens
- **Movimento Lateral**: Tokens comprometidos em múltiplos serviços permitem maior expansão de ataque

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
- **Emissão Just-in-Time**: Emitir tokens somente quando necessários para operações específicas
- **Armazenamento Seguro**: Usar módulos de segurança de hardware (HSMs) ou cofres de chaves seguros
- **Vinculação de Tokens**: Validar o destinatário e emissor do token para o recurso, cliente, e operação MCP pretendidos

- **Monitorização & Alertas**: Detecção em tempo real de uso indevido do token ou padrões de acesso não autorizados

## 3. **Controlos de Segurança do Estado da Aplicação**

### **Prevenção de Sequestro de Handle de Estado**

**Vetores de Ataque Abordados:**
- **Adivinhação de Handles**: Identificadores previsíveis expõem o estado de outro utilizador
- **Reutilização entre Utilizadores**: Um handle roubado é usado com uma identidade diferente
- **Autorização Implícita**: A posse de um handle é incorretamente tratada como
  prova de acesso

**Controlos do Handle de Estado:**

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

**Segurança no Transporte:**
- **Aplicação de HTTPS**: Exigir HTTPS para transportes HTTP remotos
- **Manipulação de Credenciais**: Enviar e validar autorização em cada pedido HTTP
- **Isolamento stdio**: Proteger servidores locais stdio através de isolamento de processo e
  controlos de credenciais no ambiente

### **Considerações entre Stateful e Stateless**

MCP `2026-07-28` é stateless ao nível do protocolo. Aplicações podem ainda assim
manter estado retornando um handle explícito de uma chamada de ferramenta e aceitando
esse handle como um argumento comum em chamadas posteriores.

- Armazenar estado independentemente de qualquer conexão de transporte.
- Vincular handles de estado ao principal autenticado no lado do servidor.
- Tratar um handle como um nome, não como uma credencial portadora.
- Definir comportamento de expiração e recuperação para handles obsoletos.

## 4. **Controlos de Segurança Específicos para IA**

**Riscos OWASP MCP Abordados**:

- [MCP06 - Subversão do Fluxo de Intenção](https://microsoft.github.io/mcp-azure-security-guide/mcp/mcp06-prompt-injection/)
- [MCP03 - Envenenamento de Ferramentas](https://microsoft.github.io/mcp-azure-security-guide/mcp/mcp03-tool-poisoning/)
- [MCP05 - Injeção e Execução de Comandos](https://microsoft.github.io/mcp-azure-security-guide/mcp/mcp05-command-injection/)

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

**Controles de Implementação:**
- **Sanitização de Entrada**: Validação e filtragem abrangente de todas as entradas do utilizador
- **Definição de Limite de Conteúdo**: Separação clara entre instruções do sistema e conteúdo do utilizador
- **Hierarquia de Instruções**: Regras de precedência adequadas para instruções conflitantes
- **Monitorização de Saída**: Detecção de saídas potencialmente prejudiciais ou manipuladas

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

**Gestão Dinâmica de Ferramentas:**
- **Fluxos de Aprovação**: Consentimento explícito do utilizador para modificações de ferramentas
- **Capacidades de Reversão**: Capacidade de reverter para versões anteriores da ferramenta
- **Auditoria de Alterações**: Histórico completo das modificações da definição da ferramenta
- **Avaliação de Risco**: Avaliação automatizada da postura de segurança da ferramenta

## 5. **Prevenção contra Ataques de Procurador Confuso**

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
- **Registo do Cliente**: Preferência por pré-registo ou Metadados de ID do Cliente
  Documentos; tratar o Registo Dinâmico de Cliente como fallback de compatibilidade
- **Verificação de Consentimento do Utilizador**: Proxies MCP usando um cliente externo estático
  ID devem obter consentimento por cliente antes de encaminhar a autorização
- **Validação do URI de Redirecionamento**: Validação rigorosa baseada em whitelist dos destinos de redirecionamento
- **Proteção do Código de Autorização**: Códigos de curta duração com aplicação de uso único
- **Verificação da Identidade do Cliente**: Validação robusta das credenciais e metadados do cliente

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
- **Contextos de Processo Separados**: Cada execução de ferramenta em espaço de processo isolado
- **Comunicação Interprocessos**: Mecanismos seguros de IPC com validação
- **Monitorização de Processos**: Análise do comportamento em tempo de execução e deteção de anomalias
- **Aplicação de Recursos**: Limites rigorosos em CPU, memória e operações de E/S

### **Implementação do Privilégio Mínimo**

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

## 7. **Controles de Segurança da Cadeia de Abastecimento**

**Risco MCP OWASP Abordado**: [MCP04 - Ataques à Cadeia de Abastecimento de Software e Manipulação de Dependências](https://microsoft.github.io/mcp-azure-security-guide/mcp/mcp04-supply-chain/)

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
- **Monitorização da Saúde das Dependências**: Avaliação contínua de todas as dependências para problemas de segurança
- **Integração de Inteligência de Ameaças**: Atualizações em tempo real sobre ameaças emergentes na cadeia de abastecimento
- **Análise Comportamental**: Deteção de comportamento invulgar em componentes externos
- **Resposta Automatizada**: Contenção imediata de componentes comprometidos

## 8. **Controles de Monitorização e Deteção**

**Risco MCP OWASP Abordado**: [MCP08 - Falta de Auditoria e Telemetria](https://microsoft.github.io/mcp-azure-security-guide/mcp/mcp08-telemetry/)

### **Gestão de Informações de Segurança e Eventos (SIEM)**

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
- **Análise Comportamental do Utilizador (UBA)**: Deteção de padrões invulgares de acesso do utilizador
- **Análise Comportamental da Entidade (EBA)**: Monitorização do comportamento do servidor MCP e das ferramentas
- **Deteção de Anomalias por Aprendizagem Automática**: Identificação com IA de ameaças de segurança
- **Correlação com Inteligência de Ameaças**: Correspondência de atividades observadas com padrões de ataque conhecidos

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
- **Preservação do Registo de Auditoria**: Registo imutável com integridade criptográfica
- **Recolha de Evidências**: Colheita automatizada de artefactos de segurança relevantes
- **Reconstrução da Linha Temporal**: Sequência detalhada dos eventos que levaram aos incidentes de segurança
- **Avaliação do Impacto**: Avaliação do âmbito da compromissão e exposição de dados

## **Princípios-Chave da Arquitetura de Segurança**

### **Defesa em Profundidade**
- **Múltiplas Camadas de Segurança**: Nenhum ponto único de falha na arquitetura de segurança
- **Controles Redundantes**: Medidas de segurança sobrepostas para funções críticas
- **Mecanismos à Prova de Falhas**: Padrões seguros quando os sistemas enfrentam erros ou ataques

### **Implementação Zero Trust**
- **Nunca Confiar, Sempre Verificar**: Validação contínua de todas as entidades e pedidos
- **Princípio do Privilégio Mínimo**: Direitos de acesso mínimos para todos os componentes
- **Micro-Segmentação**: Controlo granular de rede e acesso

### **Evolução Contínua da Segurança**
- **Adaptação ao Cenário de Ameaças**: Atualizações regulares para enfrentar ameaças emergentes
- **Eficácia dos Controles de Segurança**: Avaliação e melhoria contínuas dos controlos
- **Conformidade com Especificações**: Alinhamento com os padrões de segurança MCP em evolução

---

## **Recursos de Implementação**

### **Documentação Oficial MCP**
- [Especificação MCP (2026-07-28)](https://modelcontextprotocol.io/specification/2026-07-28/)
- [Melhores Práticas de Segurança MCP](https://modelcontextprotocol.io/specification/2026-07-28/basic/security_best_practices)
- [Especificação de Autorização MCP](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization)

### **Recursos de Segurança OWASP MCP**
- [Guia de Segurança Azure OWASP MCP](https://microsoft.github.io/mcp-azure-security-guide/) - Top 10 OWASP MCP abrangente com implementação Azure
- [Top 10 OWASP MCP](https://owasp.org/www-project-mcp-top-10/) - Riscos de segurança oficiais OWASP MCP
- [Workshop do MCP Security Summit (Sherpa)](https://azure-samples.github.io/sherpa/) - Formação prática de segurança para MCP na Azure

### **Soluções de Segurança Microsoft**
- [Microsoft Prompt Shields](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)
- [Azure Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/)
- [GitHub Advanced Security](https://github.com/security/advanced-security)
- [Azure Key Vault](https://learn.microsoft.com/azure/key-vault/)

### **Normas de Segurança**
- [Melhores Práticas de Segurança OAuth 2.0 (RFC 9700)](https://datatracker.ietf.org/doc/html/rfc9700)

- [OWASP Top 10 para Grandes Modelos de Linguagem](https://genai.owasp.org/)

- [Framework de Cibersegurança do NIST](https://www.nist.gov/cyberframework)

---

> **Importante:** Estes controlos de segurança refletem a Especificação MCP
> `2026-07-28`. Verifique sempre contra a
> [documentação oficial atual](https://modelcontextprotocol.io/specification/2026-07-28/)
> pois os standards continuam a evoluir.

## O que vem a seguir

- Voltar para: [Visão Geral do Módulo de Segurança](./README.md)
- Continuar para: [Módulo 3: Primeiros Passos](../03-GettingStarted/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas resultantes da utilização desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->