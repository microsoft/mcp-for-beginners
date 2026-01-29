# Melhores Práticas de Segurança MCP 2025

Este guia abrangente descreve as melhores práticas essenciais de segurança para a implementação de sistemas Model Context Protocol (MCP) com base na mais recente **Especificação MCP 2025-11-25** e nos padrões atuais da indústria. Estas práticas abordam tanto preocupações tradicionais de segurança como ameaças específicas de IA únicas para implementações MCP.

## Requisitos Críticos de Segurança

### Controlo de Segurança Obrigatório (Requisitos MUST)

1. **Validação de Token**: Os servidores MCP **NÃO DEVEM** aceitar quaisquer tokens que não tenham sido explicitamente emitidos para o próprio servidor MCP
2. **Verificação de Autorização**: Os servidores MCP que implementam autorização **DEVEM** verificar TODOS os pedidos recebidos e **NÃO DEVEM** usar sessões para autenticação  
3. **Consentimento do Utilizador**: Os servidores proxy MCP que usam IDs de cliente estáticos **DEVEM** obter consentimento explícito do utilizador para cada cliente registado dinamicamente
4. **IDs de Sessão Seguros**: Os servidores MCP **DEVEM** usar IDs de sessão criptograficamente seguros, não determinísticos, gerados com geradores de números aleatórios seguros

## Práticas Centrais de Segurança

### 1. Validação e Sanitização de Entrada
- **Validação Abrangente de Entrada**: Validar e sanitizar todas as entradas para prevenir ataques de injeção, problemas de delegado confuso e vulnerabilidades de injeção de prompt
- **Aplicação de Esquema de Parâmetros**: Implementar validação rigorosa de esquema JSON para todos os parâmetros de ferramentas e entradas de API
- **Filtragem de Conteúdo**: Usar Microsoft Prompt Shields e Azure Content Safety para filtrar conteúdo malicioso em prompts e respostas
- **Sanitização de Saída**: Validar e sanitizar todas as saídas do modelo antes de apresentar aos utilizadores ou sistemas a jusante

### 2. Excelência em Autenticação e Autorização  
- **Provedores de Identidade Externos**: Delegar autenticação a provedores de identidade estabelecidos (Microsoft Entra ID, provedores OAuth 2.1) em vez de implementar autenticação personalizada
- **Permissões Granulares**: Implementar permissões específicas por ferramenta seguindo o princípio do menor privilégio
- **Gestão do Ciclo de Vida do Token**: Usar tokens de acesso de curta duração com rotação segura e validação adequada do público
- **Autenticação Multifator**: Exigir MFA para todo o acesso administrativo e operações sensíveis

### 3. Protocolos de Comunicação Segura
- **Segurança da Camada de Transporte**: Usar HTTPS/TLS 1.3 para todas as comunicações MCP com validação adequada de certificados
- **Criptografia de Ponta a Ponta**: Implementar camadas adicionais de encriptação para dados altamente sensíveis em trânsito e em repouso
- **Gestão de Certificados**: Manter gestão adequada do ciclo de vida dos certificados com processos automatizados de renovação
- **Aplicação da Versão do Protocolo**: Usar a versão atual do protocolo MCP (2025-11-25) com negociação adequada de versão.

### 4. Limitação Avançada de Taxa e Proteção de Recursos
- **Limitação de Taxa em Múltiplas Camadas**: Implementar limitação de taxa a nível de utilizador, sessão, ferramenta e recurso para prevenir abusos
- **Limitação de Taxa Adaptativa**: Usar limitação de taxa baseada em machine learning que se adapta a padrões de uso e indicadores de ameaça
- **Gestão de Quotas de Recursos**: Definir limites apropriados para recursos computacionais, uso de memória e tempo de execução
- **Proteção contra DDoS**: Implementar sistemas abrangentes de proteção contra DDoS e análise de tráfego

### 5. Registo e Monitorização Abrangentes
- **Registo de Auditoria Estruturado**: Implementar registos detalhados e pesquisáveis para todas as operações MCP, execuções de ferramentas e eventos de segurança
- **Monitorização de Segurança em Tempo Real**: Implementar sistemas SIEM com deteção de anomalias alimentada por IA para cargas de trabalho MCP
- **Registo em Conformidade com Privacidade**: Registar eventos de segurança respeitando os requisitos e regulamentos de privacidade de dados
- **Integração de Resposta a Incidentes**: Ligar sistemas de registo a fluxos de trabalho automatizados de resposta a incidentes

### 6. Práticas Avançadas de Armazenamento Seguro
- **Módulos de Segurança de Hardware**: Usar armazenamento de chaves suportado por HSM (Azure Key Vault, AWS CloudHSM) para operações criptográficas críticas
- **Gestão de Chaves de Encriptação**: Implementar rotação adequada de chaves, segregação e controlos de acesso para chaves de encriptação
- **Gestão de Segredos**: Armazenar todas as chaves API, tokens e credenciais em sistemas dedicados de gestão de segredos
- **Classificação de Dados**: Classificar dados com base em níveis de sensibilidade e aplicar medidas de proteção apropriadas

### 7. Gestão Avançada de Tokens
- **Prevenção de Passagem de Token**: Proibir explicitamente padrões de passagem de token que contornem controlos de segurança
- **Validação do Público**: Verificar sempre que as declarações de público do token correspondam à identidade pretendida do servidor MCP
- **Autorização Baseada em Declarações**: Implementar autorização granular baseada em declarações do token e atributos do utilizador
- **Vinculação de Token**: Vincular tokens a sessões, utilizadores ou dispositivos específicos quando apropriado

### 8. Gestão Segura de Sessões
- **IDs de Sessão Criptográficos**: Gerar IDs de sessão usando geradores de números aleatórios criptograficamente seguros (não sequências previsíveis)
- **Vinculação Específica ao Utilizador**: Vincular IDs de sessão a informações específicas do utilizador usando formatos seguros como `<user_id>:<session_id>`
- **Controlos do Ciclo de Vida da Sessão**: Implementar mecanismos adequados de expiração, rotação e invalidação de sessão
- **Cabeçalhos de Segurança para Sessão**: Usar cabeçalhos HTTP de segurança apropriados para proteção da sessão

### 9. Controlo de Segurança Específico para IA
- **Defesa contra Injeção de Prompt**: Implementar Microsoft Prompt Shields com spotlighting, delimitadores e técnicas de datamarking
- **Prevenção de Envenenamento de Ferramentas**: Validar metadados das ferramentas, monitorizar alterações dinâmicas e verificar integridade das ferramentas
- **Validação da Saída do Modelo**: Analisar saídas do modelo para possíveis fugas de dados, conteúdo nocivo ou violações de políticas de segurança
- **Proteção da Janela de Contexto**: Implementar controlos para prevenir envenenamento e ataques de manipulação da janela de contexto

### 10. Segurança na Execução de Ferramentas
- **Sandboxing de Execução**: Executar ferramentas em ambientes isolados e conteinerizados com limites de recursos
- **Separação de Privilégios**: Executar ferramentas com privilégios mínimos necessários e contas de serviço separadas
- **Isolamento de Rede**: Implementar segmentação de rede para ambientes de execução de ferramentas
- **Monitorização da Execução**: Monitorizar execuções de ferramentas para comportamentos anómalos, uso de recursos e violações de segurança

### 11. Validação Contínua de Segurança
- **Testes Automatizados de Segurança**: Integrar testes de segurança em pipelines CI/CD com ferramentas como GitHub Advanced Security
- **Gestão de Vulnerabilidades**: Escanear regularmente todas as dependências, incluindo modelos de IA e serviços externos
- **Testes de Penetração**: Realizar avaliações regulares de segurança especificamente direcionadas a implementações MCP
- **Revisões de Código de Segurança**: Implementar revisões obrigatórias de segurança para todas as alterações de código relacionadas com MCP

### 12. Segurança da Cadeia de Abastecimento para IA
- **Verificação de Componentes**: Verificar proveniência, integridade e segurança de todos os componentes de IA (modelos, embeddings, APIs)
- **Gestão de Dependências**: Manter inventários atualizados de todas as dependências de software e IA com rastreamento de vulnerabilidades
- **Repositórios Confiáveis**: Usar fontes verificadas e confiáveis para todos os modelos, bibliotecas e ferramentas de IA
- **Monitorização da Cadeia de Abastecimento**: Monitorizar continuamente compromissos em fornecedores de serviços de IA e repositórios de modelos

## Padrões Avançados de Segurança

### Arquitetura Zero Trust para MCP
- **Nunca Confiar, Sempre Verificar**: Implementar verificação contínua para todos os participantes MCP
- **Microsegmentação**: Isolar componentes MCP com controlos granulares de rede e identidade
- **Acesso Condicional**: Implementar controlos de acesso baseados em risco que se adaptam ao contexto e comportamento
- **Avaliação Contínua de Risco**: Avaliar dinamicamente a postura de segurança com base em indicadores atuais de ameaça

### Implementação de IA que Preserva a Privacidade
- **Minimização de Dados**: Expor apenas os dados mínimos necessários para cada operação MCP
- **Privacidade Diferencial**: Implementar técnicas que preservam a privacidade para processamento de dados sensíveis
- **Encriptação Homomórfica**: Usar técnicas avançadas de encriptação para computação segura sobre dados encriptados
- **Aprendizagem Federada**: Implementar abordagens de aprendizagem distribuída que preservam a localidade e privacidade dos dados

### Resposta a Incidentes para Sistemas de IA
- **Procedimentos Específicos para IA**: Desenvolver procedimentos de resposta a incidentes adaptados a ameaças específicas de IA e MCP
- **Resposta Automatizada**: Implementar contenção e remediação automatizadas para incidentes comuns de segurança em IA  
- **Capacidades Forenses**: Manter prontidão forense para compromissos de sistemas de IA e fugas de dados
- **Procedimentos de Recuperação**: Estabelecer procedimentos para recuperação de envenenamento de modelos IA, ataques de injeção de prompt e compromissos de serviço

## Recursos e Normas para Implementação

### Documentação Oficial MCP
- [MCP Specification 2025-11-25](https://spec.modelcontextprotocol.io/specification/2025-11-25/) - Especificação atual do protocolo MCP
- [MCP Security Best Practices](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices) - Orientação oficial de segurança
- [MCP Authorization Specification](https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization) - Padrões de autenticação e autorização
- [MCP Transport Security](https://modelcontextprotocol.io/specification/2025-11-25/transports/) - Requisitos de segurança da camada de transporte

### Soluções de Segurança Microsoft
- [Microsoft Prompt Shields](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection) - Proteção avançada contra injeção de prompt
- [Azure Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/) - Filtragem abrangente de conteúdo IA
- [Microsoft Entra ID](https://learn.microsoft.com/entra/identity-platform/v2-oauth2-auth-code-flow) - Gestão empresarial de identidade e acesso
- [Azure Key Vault](https://learn.microsoft.com/azure/key-vault/general/basic-concepts) - Gestão segura de segredos e credenciais
- [GitHub Advanced Security](https://github.com/security/advanced-security) - Análise de segurança da cadeia de abastecimento e código

### Normas e Frameworks de Segurança
- [OAuth 2.1 Security Best Practices](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-security-topics) - Orientação atual de segurança OAuth
- [OWASP Top 10](https://owasp.org/www-project-top-ten/) - Riscos de segurança em aplicações web
- [OWASP Top 10 for LLMs](https://genai.owasp.org/download/43299/?tmstv=1731900559) - Riscos de segurança específicos para IA
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework) - Gestão abrangente de riscos em IA
- [ISO 27001:2022](https://www.iso.org/standard/27001) - Sistemas de gestão de segurança da informação

### Guias e Tutoriais de Implementação
- [Azure API Management as MCP Auth Gateway](https://techcommunity.microsoft.com/blog/integrationsonazureblog/azure-api-management-your-auth-gateway-for-mcp-servers/4402690) - Padrões empresariais de autenticação
- [Microsoft Entra ID with MCP Servers](https://den.dev/blog/mcp-server-auth-entra-id-session/) - Integração de provedores de identidade
- [Secure Token Storage Implementation](https://youtu.be/uRdX37EcCwg?si=6fSChs1G4glwXRy2) - Melhores práticas de gestão de tokens
- [End-to-End Encryption for AI](https://learn.microsoft.com/azure/architecture/example-scenario/confidential/end-to-end-encryption) - Padrões avançados de encriptação

### Recursos Avançados de Segurança
- [Microsoft Security Development Lifecycle](https://www.microsoft.com/sdl) - Práticas seguras de desenvolvimento
- [AI Red Team Guidance](https://learn.microsoft.com/security/ai-red-team/) - Testes de segurança específicos para IA
- [Threat Modeling for AI Systems](https://learn.microsoft.com/security/adoption/approach/threats-ai) - Metodologia de modelação de ameaças para IA
- [Privacy Engineering for AI](https://www.microsoft.com/security/blog/2021/07/13/microsofts-pet-project-privacy-enhancing-technologies-in-action/) - Técnicas de IA que preservam a privacidade

### Conformidade e Governança
- [GDPR Compliance for AI](https://learn.microsoft.com/compliance/regulatory/gdpr-data-protection-impact-assessments) - Conformidade de privacidade em sistemas IA
- [AI Governance Framework](https://learn.microsoft.com/azure/architecture/guide/responsible-ai/responsible-ai-overview) - Implementação responsável de IA
- [SOC 2 for AI Services](https://learn.microsoft.com/compliance/regulatory/offering-soc) - Controlos de segurança para fornecedores de serviços IA
- [HIPAA Compliance for AI](https://learn.microsoft.com/compliance/regulatory/offering-hipaa-hitech) - Requisitos de conformidade para IA na saúde

### DevSecOps e Automação
- [DevSecOps Pipeline for AI](https://learn.microsoft.com/azure/devops/migrate/security-validation-cicd-pipeline) - Pipelines seguros para desenvolvimento IA
- [Automated Security Testing](https://learn.microsoft.com/security/engineering/devsecops) - Validação contínua de segurança
- [Infrastructure as Code Security](https://learn.microsoft.com/security/engineering/infrastructure-security) - Implementação segura de infraestrutura
- [Container Security for AI](https://learn.microsoft.com/azure/container-instances/container-instances-image-security) - Segurança na conteinerização de cargas IA

### Monitorização e Resposta a Incidentes  
- [Azure Monitor for AI Workloads](https://learn.microsoft.com/azure/azure-monitor/overview) - Soluções abrangentes de monitorização
- [AI Security Incident Response](https://learn.microsoft.com/security/compass/incident-response-playbooks) - Procedimentos específicos para incidentes IA
- [SIEM for AI Systems](https://learn.microsoft.com/azure/sentinel/overview) - Gestão de informação e eventos de segurança
- [Threat Intelligence for AI](https://learn.microsoft.com/security/compass/security-operations-videos-and-decks#threat-intelligence) - Fontes de inteligência de ameaças IA

## 🔄 Melhoria Contínua

### Manter-se Atualizado com Normas em Evolução
- **Atualizações da Especificação MCP**: Monitorizar alterações oficiais da especificação MCP e avisos de segurança
- **Inteligência de Ameaças**: Subscrever feeds de ameaças de segurança IA e bases de dados de vulnerabilidades  
- **Envolvimento Comunitário**: Participar em discussões e grupos de trabalho da comunidade de segurança MCP
- **Avaliação Regular**: Realizar avaliações trimestrais da postura de segurança e atualizar práticas conforme necessário

### Contribuir para a Segurança MCP
- **Investigação em Segurança**: Contribuir para investigação de segurança MCP e programas de divulgação de vulnerabilidades
- **Partilha de Melhores Práticas**: Partilhar implementações de segurança e lições aprendidas com a comunidade
- **Desenvolvimento Padrão**: Participar no desenvolvimento da especificação MCP e na criação de normas de segurança
- **Desenvolvimento de Ferramentas**: Desenvolver e partilhar ferramentas e bibliotecas de segurança para o ecossistema MCP

---

*Este documento reflete as melhores práticas de segurança MCP a partir de 18 de dezembro de 2025, com base na Especificação MCP 2025-11-25. As práticas de segurança devem ser revistas e atualizadas regularmente à medida que o protocolo e o panorama de ameaças evoluem.*

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, por favor tenha em conta que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se a tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações erradas decorrentes do uso desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->