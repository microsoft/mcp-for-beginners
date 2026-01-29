# Melhores Práticas de Segurança MCP - Atualização de Dezembro de 2025

> **Importante**: Este documento reflete os mais recentes requisitos de segurança da [Especificação MCP 2025-11-25](https://spec.modelcontextprotocol.io/specification/2025-11-25/) e as [Melhores Práticas de Segurança MCP](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices) oficiais. Consulte sempre a especificação atual para obter as orientações mais atualizadas.

## Práticas Essenciais de Segurança para Implementações MCP

O Protocolo de Contexto de Modelo introduz desafios únicos de segurança que vão além da segurança tradicional de software. Estas práticas abordam tanto os requisitos fundamentais de segurança como as ameaças específicas do MCP, incluindo injeção de prompt, envenenamento de ferramentas, sequestro de sessão, problemas de procurador confuso e vulnerabilidades de passagem de token.

### **Requisitos de Segurança OBRIGATÓRIOS** 

**Requisitos Críticos da Especificação MCP:**

### **Requisitos de Segurança OBRIGATÓRIOS** 

**Requisitos Críticos da Especificação MCP:**

> **NÃO DEVE**: Os servidores MCP **NÃO DEVEM** aceitar quaisquer tokens que não tenham sido explicitamente emitidos para o servidor MCP
> 
> **DEVE**: Os servidores MCP que implementam autorização **DEVEM** verificar TODOS os pedidos recebidos
>  
> **NÃO DEVE**: Os servidores MCP **NÃO DEVEM** usar sessões para autenticação
>
> **DEVE**: Os servidores proxy MCP que usam IDs de cliente estáticos **DEVEM** obter consentimento do utilizador para cada cliente registado dinamicamente

---

## 1. **Segurança de Token & Autenticação**

**Controlo de Autenticação & Autorização:**
   - **Revisão Rigorosa de Autorização**: Realizar auditorias abrangentes da lógica de autorização do servidor MCP para garantir que apenas utilizadores e clientes pretendidos possam aceder aos recursos
   - **Integração com Provedor de Identidade Externo**: Usar provedores de identidade estabelecidos como Microsoft Entra ID em vez de implementar autenticação personalizada
   - **Validação do Público do Token**: Validar sempre que os tokens foram explicitamente emitidos para o seu servidor MCP - nunca aceitar tokens upstream
   - **Ciclo de Vida Adequado do Token**: Implementar rotação segura de tokens, políticas de expiração e prevenir ataques de repetição de token

**Armazenamento Protegido de Tokens:**
   - Usar Azure Key Vault ou armazenamentos de credenciais seguros semelhantes para todos os segredos
   - Implementar encriptação para tokens tanto em repouso como em trânsito
   - Rotação regular de credenciais e monitorização para acessos não autorizados

## 2. **Gestão de Sessão & Segurança de Transporte**

**Práticas Seguras de Sessão:**
   - **IDs de Sessão Criptograficamente Seguros**: Usar IDs de sessão seguros e não determinísticos gerados com geradores de números aleatórios seguros
   - **Vinculação Específica ao Utilizador**: Vincular IDs de sessão às identidades dos utilizadores usando formatos como `<user_id>:<session_id>` para prevenir abuso de sessão entre utilizadores
   - **Gestão do Ciclo de Vida da Sessão**: Implementar expiração, rotação e invalidação adequadas para limitar janelas de vulnerabilidade
   - **Aplicação de HTTPS/TLS**: HTTPS obrigatório para toda a comunicação para prevenir interceção de IDs de sessão

**Segurança da Camada de Transporte:**
   - Configurar TLS 1.3 sempre que possível com gestão adequada de certificados
   - Implementar pinagem de certificados para ligações críticas
   - Rotação regular de certificados e verificação de validade

## 3. **Proteção Contra Ameaças Específicas de IA** 🤖

**Defesa contra Injeção de Prompt:**
   - **Microsoft Prompt Shields**: Implementar AI Prompt Shields para deteção avançada e filtragem de instruções maliciosas
   - **Sanitização de Entrada**: Validar e sanitizar todas as entradas para prevenir ataques de injeção e problemas de procurador confuso
   - **Limites de Conteúdo**: Usar sistemas de delimitadores e marcação de dados para distinguir entre instruções confiáveis e conteúdo externo

**Prevenção de Envenenamento de Ferramentas:**
   - **Validação de Metadados de Ferramentas**: Implementar verificações de integridade para definições de ferramentas e monitorizar alterações inesperadas
   - **Monitorização Dinâmica de Ferramentas**: Monitorizar comportamento em tempo de execução e configurar alertas para padrões de execução inesperados
   - **Fluxos de Aprovação**: Exigir aprovação explícita do utilizador para modificações de ferramentas e alterações de capacidades

## 4. **Controlo de Acesso & Permissões**

**Princípio do Menor Privilégio:**
   - Conceder aos servidores MCP apenas as permissões mínimas necessárias para a funcionalidade pretendida
   - Implementar controlo de acesso baseado em funções (RBAC) com permissões granulares
   - Revisões regulares de permissões e monitorização contínua para escalonamento de privilégios

**Controlo de Permissões em Tempo de Execução:**
   - Aplicar limites de recursos para prevenir ataques de exaustão de recursos
   - Usar isolamento de containers para ambientes de execução de ferramentas  
   - Implementar acesso just-in-time para funções administrativas

## 5. **Segurança de Conteúdo & Monitorização**

**Implementação de Segurança de Conteúdo:**
   - **Integração Azure Content Safety**: Usar Azure Content Safety para detetar conteúdo nocivo, tentativas de jailbreak e violações de políticas
   - **Análise Comportamental**: Implementar monitorização comportamental em tempo de execução para detetar anomalias na execução do servidor MCP e ferramentas
   - **Registo Abrangente**: Registar todas as tentativas de autenticação, invocações de ferramentas e eventos de segurança com armazenamento seguro e à prova de adulteração

**Monitorização Contínua:**
   - Alertas em tempo real para padrões suspeitos e tentativas de acesso não autorizadas  
   - Integração com sistemas SIEM para gestão centralizada de eventos de segurança
   - Auditorias regulares de segurança e testes de penetração das implementações MCP

## 6. **Segurança da Cadeia de Abastecimento**

**Verificação de Componentes:**
   - **Análise de Dependências**: Usar análise automatizada de vulnerabilidades para todas as dependências de software e componentes de IA
   - **Validação de Proveniência**: Verificar a origem, licenciamento e integridade de modelos, fontes de dados e serviços externos
   - **Pacotes Assinados**: Usar pacotes assinados criptograficamente e verificar assinaturas antes da implementação

**Pipeline de Desenvolvimento Seguro:**
   - **GitHub Advanced Security**: Implementar varredura de segredos, análise de dependências e análise estática CodeQL
   - **Segurança CI/CD**: Integrar validação de segurança em pipelines automatizados de implementação
   - **Integridade de Artefactos**: Implementar verificação criptográfica para artefactos e configurações implementados

## 7. **Segurança OAuth & Prevenção de Procurador Confuso**

**Implementação OAuth 2.1:**
   - **Implementação PKCE**: Usar Proof Key for Code Exchange (PKCE) para todos os pedidos de autorização
   - **Consentimento Explícito**: Obter consentimento do utilizador para cada cliente registado dinamicamente para prevenir ataques de procurador confuso
   - **Validação de URI de Redirecionamento**: Implementar validação rigorosa de URIs de redirecionamento e identificadores de cliente

**Segurança de Proxy:**
   - Prevenir bypass de autorização através da exploração de ID de cliente estático
   - Implementar fluxos de consentimento adequados para acesso a APIs de terceiros
   - Monitorizar roubo de código de autorização e acesso não autorizado a APIs

## 8. **Resposta a Incidentes & Recuperação**

**Capacidades de Resposta Rápida:**
   - **Resposta Automatizada**: Implementar sistemas automatizados para rotação de credenciais e contenção de ameaças
   - **Procedimentos de Reversão**: Capacidade de reverter rapidamente para configurações e componentes conhecidos como bons
   - **Capacidades Forenses**: Trilhas de auditoria detalhadas e registos para investigação de incidentes

**Comunicação & Coordenação:**
   - Procedimentos claros de escalonamento para incidentes de segurança
   - Integração com equipas organizacionais de resposta a incidentes
   - Simulações regulares de incidentes de segurança e exercícios de mesa

## 9. **Conformidade & Governança**

**Conformidade Regulamentar:**
   - Garantir que as implementações MCP cumprem requisitos específicos da indústria (GDPR, HIPAA, SOC 2)
   - Implementar classificação de dados e controlos de privacidade para processamento de dados de IA
   - Manter documentação abrangente para auditoria de conformidade

**Gestão de Alterações:**
   - Processos formais de revisão de segurança para todas as modificações do sistema MCP
   - Controlo de versões e fluxos de aprovação para alterações de configuração
   - Avaliações regulares de conformidade e análise de lacunas

## 10. **Controlo Avançado de Segurança**

**Arquitetura Zero Trust:**
   - **Nunca Confiar, Sempre Verificar**: Verificação contínua de utilizadores, dispositivos e ligações
   - **Microsegmentação**: Controlo granular de rede isolando componentes individuais MCP
   - **Acesso Condicional**: Controlo de acesso baseado em risco adaptando-se ao contexto e comportamento atuais

**Proteção de Aplicações em Tempo de Execução:**
   - **Proteção de Aplicação em Tempo de Execução (RASP)**: Implementar técnicas RASP para deteção de ameaças em tempo real
   - **Monitorização de Performance de Aplicações**: Monitorizar anomalias de desempenho que possam indicar ataques
   - **Políticas de Segurança Dinâmicas**: Implementar políticas de segurança que se adaptam com base no panorama atual de ameaças

## 11. **Integração no Ecossistema de Segurança Microsoft**

**Segurança Microsoft Abrangente:**
   - **Microsoft Defender for Cloud**: Gestão da postura de segurança na cloud para cargas de trabalho MCP
   - **Azure Sentinel**: Capacidades SIEM e SOAR nativas da cloud para deteção avançada de ameaças
   - **Microsoft Purview**: Governança de dados e conformidade para fluxos de trabalho e fontes de dados de IA

**Gestão de Identidade & Acesso:**
   - **Microsoft Entra ID**: Gestão empresarial de identidade com políticas de acesso condicional
   - **Gestão de Identidade Privilegiada (PIM)**: Acesso just-in-time e fluxos de aprovação para funções administrativas
   - **Proteção de Identidade**: Acesso condicional baseado em risco e resposta automatizada a ameaças

## 12. **Evolução Contínua da Segurança**

**Manter-se Atualizado:**
   - **Monitorização da Especificação**: Revisão regular das atualizações da especificação MCP e alterações nas orientações de segurança
   - **Inteligência de Ameaças**: Integração de feeds de ameaças específicas de IA e indicadores de compromisso
   - **Envolvimento na Comunidade de Segurança**: Participação ativa na comunidade de segurança MCP e programas de divulgação de vulnerabilidades

**Segurança Adaptativa:**
   - **Segurança com Aprendizagem Automática**: Usar deteção de anomalias baseada em ML para identificar padrões de ataque novos
   - **Análise Preditiva de Segurança**: Implementar modelos preditivos para identificação proativa de ameaças
   - **Automação de Segurança**: Atualizações automatizadas de políticas de segurança baseadas em inteligência de ameaças e alterações na especificação

---

## **Recursos Críticos de Segurança**

### **Documentação Oficial MCP**
- [Especificação MCP (2025-11-25)](https://spec.modelcontextprotocol.io/specification/2025-11-25/)
- [Melhores Práticas de Segurança MCP](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices)
- [Especificação de Autorização MCP](https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization)

### **Soluções de Segurança Microsoft**
- [Microsoft Prompt Shields](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)
- [Azure Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/)
- [Segurança Microsoft Entra ID](https://learn.microsoft.com/entra/identity-platform/secure-least-privileged-access)
- [GitHub Advanced Security](https://github.com/security/advanced-security)

### **Normas de Segurança**
- [Melhores Práticas de Segurança OAuth 2.0 (RFC 9700)](https://datatracker.ietf.org/doc/html/rfc9700)
- [OWASP Top 10 para Modelos de Linguagem Grande](https://genai.owasp.org/)
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)

### **Guias de Implementação**
- [Azure API Management MCP Authentication Gateway](https://techcommunity.microsoft.com/blog/integrationsonazureblog/azure-api-management-your-auth-gateway-for-mcp-servers/4402690)
- [Microsoft Entra ID com Servidores MCP](https://den.dev/blog/mcp-server-auth-entra-id-session/)

---

> **Aviso de Segurança**: As práticas de segurança MCP evoluem rapidamente. Verifique sempre contra a [especificação MCP](https://spec.modelcontextprotocol.io/) atual e a [documentação oficial de segurança](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices) antes da implementação.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, por favor tenha em conta que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se a tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações erradas decorrentes do uso desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->