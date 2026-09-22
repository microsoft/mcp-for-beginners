# Práticas Recomendadas de Segurança MCP - Atualização de Setembro de 2026

Este guia abrangente descreve as práticas essenciais recomendadas de segurança para
implementação de sistemas do Protocolo de Contexto de Modelo (MCP) com base na
**Especificação MCP 2026-07-28** e nos padrões atuais da indústria. Estas
práticas abordam tanto preocupações tradicionais de segurança como ameaças específicas de IA
únicas para implementações MCP.

## Requisitos Críticos de Segurança

### Controlo de Segurança Obrigatório (Requisitos MUST)

1. **Validação de Token**: Os servidores MCP **NÃO DEVEM** aceitar quaisquer tokens que não tenham sido explicitamente emitidos para o próprio servidor MCP
2. **Verificação de Autorização**: Os servidores MCP que implementam autorização **DEVEM** verificar TODOS os pedidos recebidos e **NÃO DEVEM** usar sessões para autenticação  
3. **Consentimento do Utilizador**: Os servidores proxy MCP que utilizam IDs estáticos de clientes de terceiros **DEVEM** obter consentimento explícito de cada cliente MCP antes de encaminhar um fluxo de autorização
4. **Segurança do Estado de Manipulação**: Os servidores MCP **NÃO DEVEM** tratar a posse de uma
	handle de estado da aplicação como autenticação e **DEVEM** autorizar todos os
	pedidos que usem um

## Práticas de Segurança Fundamentais

### 1. Validação e Sanitização de Entrada
- **Validação Abrangente de Entrada**: Validar e sanitizar todas as entradas para prevenir ataques de injeção, problemas de deputado confuso e vulnerabilidades de injeção de prompt
- **Aplicação de Esquema de Parâmetros**: Implementar validação rigorosa de esquema JSON para todos os parâmetros de ferramentas e entradas API
- **Filtragem de Conteúdo**: Usar Microsoft Prompt Shields e Azure Content Safety para filtrar conteúdos maliciosos em prompts e respostas
- **Sanitização de Saída**: Validar e sanitizar todas as saídas do modelo antes de apresentar aos utilizadores ou sistemas descendentes

### 2. Excelência em Autenticação e Autorização  
- **Provedores de Identidade Externos**: Delegar autenticação a provedores de identidade estabelecidos (Microsoft Entra ID, provedores OAuth 2.1) em vez de implementar autenticação personalizada
- **Registo de Clientes**: Preferir Documentos de Metadados de ID de Cliente ou pré-registo; usar Registo Dinâmico de Cliente descontinuado apenas para compatibilidade
- **Permissões Granulares**: Implementar permissões granulares específicas à ferramenta seguindo o princípio do menor privilégio
- **Gestão do Ciclo de Vida do Token**: Usar tokens de acesso com curta duração com rotação segura e validação adequada do público
- **Autenticação Multi-Fator**: Exigir MFA para todo o acesso administrativo e operações sensíveis

### 3. Protocolos de Comunicação Segura
- **Segurança da Camada de Transporte**: Usar HTTPS com validação adequada de certificados
	para comunicações HTTP remotas MCP; usar isolamento de processo e
	credenciais de ambiente para servidores stdio locais
- **Encriptação de Ponta a Ponta**: Implementar camadas adicionais de encriptação para dados altamente sensíveis em trânsito e em repouso
- **Gestão de Certificados**: Manter gestão adequada do ciclo de vida dos certificados com processos automatizados de renovação
- **Aplicação da Versão do Protocolo**: Usar MCP `2026-07-28`, incluir os metadados
	de versão requeridos em cada pedido e rejeitar versões não suportadas

### 4. Controlo Avançado de Limitação de Taxa e Proteção de Recursos
- **Limitação de Taxa em Múltiplas Camadas**: Implementar limitação de taxa por utilizador, credenciais,
  operação, ferramenta e recurso para prevenir abusos
- **Limitação de Taxa Adaptativa**: Usar limitação de taxa baseada em machine learning que se adapta a padrões de uso e indicadores de ameaça
- **Gestão de Quotas de Recursos**: Definir limites apropriados para recursos computacionais, uso de memória e tempo de execução
- **Proteção contra DDoS**: Implementar proteção abrangente contra DDoS e sistemas de análise de tráfego

### 5. Registo e Monitorização Abrangentes
- **Registo de Auditoria Estruturado**: Implementar registos detalhados e pesquisáveis para todas as operações MCP, execuções de ferramentas e eventos de segurança

- **Monitorização de Segurança em Tempo Real**: Desplegar sistemas SIEM com deteção de anomalias suportada por IA para cargas de trabalho MCP
- **Registo em Conformidade com a Privacidade**: Registar eventos de segurança respeitando os requisitos e regulamentos de privacidade de dados
- **Integração de Resposta a Incidentes**: Ligar sistemas de registo a fluxos de trabalho de resposta a incidentes automatizados

### 6. Práticas Melhoradas de Armazenamento Seguro
- **Módulos de Segurança de Hardware**: Utilizar armazenamento de chaves suportado por HSM (Azure Key Vault, AWS CloudHSM) para operações criptográficas críticas
- **Gestão de Chaves de Criptografia**: Implementar rotação adequada de chaves, segregação e controlos de acesso para chaves de encriptação
- **Gestão de Segredos**: Armazenar todas as chaves API, tokens e credenciais em sistemas dedicados de gestão de segredos
- **Classificação de Dados**: Classificar os dados com base nos níveis de sensibilidade e aplicar medidas de proteção apropriadas

### 7. Gestão Avançada de Tokens
- **Prevenção de Passagem de Token**: Proibir explicitamente padrões de passagem de token que ignorem os controlos de segurança
- **Validação da Audiência**: Verificar sempre as declarações de audiência do token coincidirem com a identidade do servidor MCP pretendida
- **Autorização Baseada em Claims**: Implementar autorização granulada com base nas claims do token e atributos do utilizador
- **Binding de Token**: Validar que os tokens destinam-se ao recurso MCP pretendido e
	ligar os identificadores de estado da aplicação no servidor ao principal autenticado

### 8. Estado Seguro da Aplicação

- **Identificadores Criptográficos de Estado**: Gerar identificadores opacos e não determinísticos
	para o estado que abranja pedidos
- **Binding Específico por Utilizador**: Ligar cada identificador no servidor ao principal autenticado; não confiar num ID de utilizador fornecido pelo cliente
- **Controlos de Ciclo de Vida**: Expirar e revogar identificadores, e definir como os invocadores recuperam de estado obsoleto
- **Autorização por Pedido**: Reavaliar a autorização sempre que um identificador for apresentado; um identificador é um nome, não uma credencial




### 9. Controlos de Segurança Específicos para IA
- **Defesa contra Injeção de Prompt**: Implementar Microsoft Prompt Shields com técnicas de destaque, delimitadores e marcação de dados
- **Prevenção de Contaminação de Ferramentas**: Validar metadados da ferramenta, monitorizar alterações dinâmicas e verificar a integridade da ferramenta
- **Validação da Saída do Modelo**: Verificar as saídas do modelo para potenciais fugas de dados, conteúdos prejudiciais ou violações de políticas de segurança
- **Proteção da Janela de Contexto**: Implementar controlos para evitar contaminação da janela de contexto e ataques de manipulação

### 10. Segurança na Execução de Ferramentas
- **Execução em Sandbox**: Efetuar execuções de ferramentas em ambientes isolados e conteinerizados com limites de recursos
- **Separação de Privilégios**: Executar ferramentas com privilégios mínimos necessários e contas de serviço separadas
- **Isolamento de Rede**: Implementar segmentação de rede para ambientes de execução de ferramentas
- **Monitorização da Execução**: Monitorizar a execução das ferramentas para comportamentos anómalos, uso de recursos e violações de segurança

### 11. Validação Contínua da Segurança
- **Testes Automatizados de Segurança**: Integrar testes de segurança em pipelines CI/CD com ferramentas como GitHub Advanced Security
- **Gestão de Vulnerabilidades**: Verificar regularmente todas as dependências, incluindo modelos de IA e serviços externos
- **Testes de Penetração**: Realizar avaliações regulares de segurança especificamente focadas em implementações MCP
- **Revisões de Código de Segurança**: Implementar revisões de segurança obrigatórias para todas as alterações de código relacionadas com MCP

### 12. Segurança da Cadeia de Abastecimento para IA
- **Verificação de Componentes**: Verificar proveniência, integridade e segurança de todos os componentes IA (modelos, embeddings, APIs)
- **Gestão de Dependências**: Manter inventários atualizados de todas as dependências de software e IA com acompanhamento de vulnerabilidades
- **Repositórios Confiáveis**: Utilizar fontes verificadas e confiáveis para todos os modelos, bibliotecas e ferramentas de IA

- **Monitorização da Cadeia de Fornecimento**: Monitorizar continuamente para compromissos nos prestadores de serviços de IA e repositórios de modelos


## Padrões Avançados de Segurança

### Arquitectura Zero Trust para MCP
- **Nunca Confiar, Sempre Verificar**: Implementar verificação contínua para todos os participantes do MCP
- **Micro-segmentação**: Isolar componentes do MCP com controlos granulares de rede e identidade
- **Acesso Condicional**: Implementar controlos de acesso baseados em risco que se adaptam ao contexto e comportamento
- **Avaliação Contínua de Risco**: Avaliar dinamicamente a postura de segurança com base nos indicadores actuais de ameaça

### Implementação de IA Preservando a Privacidade
- **Minimização de Dados**: Expor apenas o mínimo de dados necessários para cada operação do MCP
- **Privacidade Diferencial**: Implementar técnicas de preservação de privacidade para o processamento de dados sensíveis
- **Criptografia Homomórfica**: Usar técnicas avançadas de criptografia para computação segura em dados encriptados
- **Aprendizagem Federada**: Implementar abordagens de aprendizagem distribuída que preservam a localidade e privacidade dos dados

### Resposta a Incidentes para Sistemas de IA
- **Procedimentos de Incidente Específicos para IA**: Desenvolver procedimentos de resposta a incidentes adaptados a ameaças específicas da IA e MCP
- **Resposta Automatizada**: Implementar contenção e remediação automatizadas para incidentes comuns de segurança em IA  
- **Capacidades Forenses**: Manter prontidão forense para compromissos de sistemas de IA e fugas de dados
- **Procedimentos de Recuperação**: Estabelecer procedimentos para recuperação de envenenamento de modelos de IA, ataques de injeção de prompt e compromissos de serviço

## Recursos e Normas de Implementação

### 🏔️ Formação Prática em Segurança
- **[Workshop MCP Security Summit (Sherpa)](https://azure-samples.github.io/sherpa/)** - Workshop prático abrangente para securizar servidores MCP na Azure
- **[OWASP MCP Azure Security Guide](https://microsoft.github.io/mcp-azure-security-guide/)** - Arquitectura de referência e guia de implementação do Top 10 MCP da OWASP

### Documentação Oficial do MCP
- [Especificação MCP 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/) - Especificação atual do protocolo MCP
- [Melhores Práticas de Segurança MCP](https://modelcontextprotocol.io/specification/2026-07-28/basic/security_best_practices) - Orientações oficiais de segurança
- [Especificação de Autorização MCP](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization) - Padrões de autorização HTTP
- [Transportes MCP](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/) - Requisitos de transporte

### Soluções de Segurança Microsoft
- [Microsoft Prompt Shields](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection) - Protecção avançada contra injeção de prompts
- [Azure Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/) - Filtragem abrangente de conteúdos IA
- [Microsoft Entra ID](https://learn.microsoft.com/entra/identity-platform/v2-oauth2-auth-code-flow) - Gestão empresarial de identidade e acesso
- [Azure Key Vault](https://learn.microsoft.com/azure/key-vault/general/basic-concepts) - Gestão segura de segredos e credenciais
- [GitHub Advanced Security](https://github.com/security/advanced-security) - Análise da segurança da cadeia de fornecimento e código

### Normas e Moldes de Segurança
- [Melhores Práticas de Segurança OAuth 2.1](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-security-topics) - Orientação actual de segurança OAuth
- [OWASP Top 10](https://owasp.org/www-project-top-ten/) - Riscos de segurança em aplicações web
- [OWASP Top 10 para LLMs](https://genai.owasp.org/download/43299/?tmstv=1731900559) - Riscos de segurança específicos para IA
- [Moldura de Gestão de Riscos IA NIST](https://www.nist.gov/itl/ai-risk-management-framework) - Gestão abrangente de riscos de IA
- [ISO 27001:2022](https://www.iso.org/standard/27001) - Sistemas de gestão da segurança da informação

### Guias e Tutoriais de Implementação
- [Azure API Management como MCP Auth Gateway](https://techcommunity.microsoft.com/blog/integrationsonazureblog/azure-api-management-your-auth-gateway-for-mcp-servers/4402690) - Padrões empresariais de autenticação
- [Microsoft Entra ID com Servidores MCP](https://den.dev/blog/mcp-server-auth-entra-id-session/) - Integração de fornecedores de identidade
- [Implementação de Armazenamento Seguro de Tokens](https://youtu.be/uRdX37EcCwg?si=6fSChs1G4glwXRy2) - Melhores práticas de gestão de tokens
- [Criptografia End-to-End para IA](https://learn.microsoft.com/azure/architecture/example-scenario/confidential/end-to-end-encryption) - Padrões avançados de criptografia

### Recursos Avançados de Segurança
- [Ciclo de Vida de Desenvolvimento Seguro Microsoft](https://www.microsoft.com/sdl) - Práticas de desenvolvimento seguro
- [Guia Red Team para IA](https://learn.microsoft.com/security/ai-red-team/) - Testes de segurança específicos para IA
- [Modelação de Ameaças para Sistemas de IA](https://learn.microsoft.com/security/adoption/approach/threats-ai) - Metodologia de modelação de ameaças IA
- [Engenharia de Privacidade para IA](https://www.microsoft.com/security/blog/2021/07/13/microsofts-pet-project-privacy-enhancing-technologies-in-action/) - Técnicas de IA preservando a privacidade

### Conformidade e Governação
- [Conformidade GDPR para IA](https://learn.microsoft.com/compliance/regulatory/gdpr-data-protection-impact-assessments) - Conformidade de privacidade em sistemas de IA
- [Moldura de Governação de IA](https://learn.microsoft.com/azure/architecture/guide/responsible-ai/responsible-ai-overview) - Implementação responsável de IA
- [SOC 2 para Serviços de IA](https://learn.microsoft.com/compliance/regulatory/offering-soc) - Controlos de segurança para fornecedores de serviços IA
- [Conformidade HIPAA para IA](https://learn.microsoft.com/compliance/regulatory/offering-hipaa-hitech) - Requisitos de conformidade IA na saúde

### DevSecOps e Automação
- [Pipeline DevSecOps para IA](https://learn.microsoft.com/azure/devops/migrate/security-validation-cicd-pipeline) - Pipelines de desenvolvimento seguro para IA
- [Testes Automáticos de Segurança](https://learn.microsoft.com/security/engineering/devsecops) - Validação contínua de segurança
- [Segurança de Infraestrutura como Código](https://learn.microsoft.com/security/engineering/infrastructure-security) - Implementação segura de infraestrutura
- [Segurança de Containers para IA](https://learn.microsoft.com/azure/container-instances/container-instances-image-security) - Segurança na conteinerização de cargas de trabalho IA

### Monitorização e Resposta a Incidentes  
- [Azure Monitor para Cargas de Trabalho IA](https://learn.microsoft.com/azure/azure-monitor/overview) - Soluções abrangentes de monitorização
- [Resposta a Incidentes de Segurança IA](https://learn.microsoft.com/security/compass/incident-response-playbooks) - Procedimentos de incidentes específicos para IA
- [SIEM para Sistemas IA](https://learn.microsoft.com/azure/sentinel/overview) - Gestão de informação e eventos de segurança

- [Threat Intelligence para IA](https://learn.microsoft.com/security/compass/security-operations-videos-and-decks#threat-intelligence) - Fontes de inteligência sobre ameaças em IA

## 🔄 Melhoria Contínua

### Mantenha-se Atualizado com os Padrões em Evolução
- **Atualizações da Especificação MCP**: Monitorizar alterações oficiais na especificação MCP e avisos de segurança
- **Inteligência sobre Ameaças**: Subscrever feeds de ameaças de segurança de IA e bases de dados de vulnerabilidades  
- **Engajamento Comunitário**: Participar em discussões da comunidade de segurança MCP e grupos de trabalho
- **Avaliação Regular**: Realizar avaliações trimestrais da postura de segurança e atualizar práticas em conformidade

### Contribuindo para a Segurança MCP
- **Investigação de Segurança**: Contribuir para a investigação de segurança MCP e programas de divulgação de vulnerabilidades
- **Partilha de Melhores Práticas**: Partilhar implementações de segurança e lições aprendidas com a comunidade
- **Desenvolvimento de Padrões**: Participar no desenvolvimento da especificação MCP e criação de padrões de segurança
- **Desenvolvimento de Ferramentas**: Desenvolver e partilhar ferramentas e bibliotecas de segurança para o ecossistema MCP

---

*Este documento reflete as melhores práticas de segurança MCP a partir de 9 de setembro de 2026,
com base na Especificação MCP `2026-07-28`. As práticas de segurança devem ser regularmente
revistas à medida que o protocolo e o panorama de ameaças evoluem.*

## O que Vem a Seguir

- Leia: [Melhores Práticas de Segurança MCP](./mcp-security-best-practices.md)
- Voltar para: [Visão Geral do Módulo de Segurança](./README.md)
- Continuar para: [Módulo 3: Introdução](../03-GettingStarted/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas resultantes da utilização desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->