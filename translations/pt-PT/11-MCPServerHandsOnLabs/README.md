# 🚀 Servidor MCP com PostgreSQL - Guia Completo de Aprendizagem

## 🧠 Visão Geral do Percurso de Aprendizagem de Integração com Base de Dados MCP

Este guia de aprendizagem abrangente ensina-o a construir servidores **Model Context Protocol (MCP)** prontos para produção que integram bases de dados através de uma implementação prática de análise de retalho. Vai aprender padrões de nível empresarial incluindo **Row Level Security (RLS)**, **pesquisa semântica**, **integração Azure AI** e **acesso a dados multi-inquilino**.

Quer seja programador back-end, engenheiro de IA ou arquiteto de dados, este guia oferece aprendizagem estruturada com exemplos do mundo real e exercícios práticos que o conduzem pelo seguinte servidor MCP https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail.

## 🔗 Recursos Oficiais MCP

- 📘 [Documentação MCP](https://modelcontextprotocol.io/) – Tutoriais detalhados e guias do utilizador
- 📜 [Especificação MCP (2026-07-28)](https://modelcontextprotocol.io/specification/2026-07-28/) – Arquitetura do protocolo e referências técnicas
- 🧑‍💻 [Repositório MCP no GitHub](https://github.com/modelcontextprotocol) – SDKs open-source, ferramentas e exemplos de código
- 🌐 [Comunidade MCP](https://github.com/orgs/modelcontextprotocol/discussions) – Participe em discussões e contribua para a comunidade
- 🔒 [OWASP MCP Top 10](https://microsoft.github.io/mcp-azure-security-guide/mcp/) – Melhores práticas de segurança e mitigação de riscos


## 🧭 Percurso de Aprendizagem de Integração com Base de Dados MCP

### 📚 Estrutura Completa de Aprendizagem para https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail

| Laboratório | Tópico | Descrição | Link |
|--------|-------|-------------|------|
| **Lab 1-3: Fundamentos** | | | |
| 00 | [Introdução à Integração MCP com Base de Dados](./00-Introduction/README.md) | Visão geral do MCP com integração de base de dados e caso de uso em análise de retalho | [Comece Aqui](./00-Introduction/README.md) |
| 01 | [Conceitos de Arquitetura Core](./01-Architecture/README.md) | Compreensão da arquitetura do servidor MCP, camadas da base de dados e padrões de segurança | [Aprender](./01-Architecture/README.md) |
| 02 | [Segurança e Multi-Inquilino](./02-Security/README.md) | Row Level Security, autenticação e acesso multi-inquilino a dados | [Aprender](./02-Security/README.md) |
| 03 | [Configuração do Ambiente](./03-Setup/README.md) | Configuração do ambiente de desenvolvimento, Docker, recursos Azure | [Configurar](./03-Setup/README.md) |
| **Lab 4-6: Construção do Servidor MCP** | | | |
| 04 | [Design da Base de Dados e Esquema](./04-Database/README.md) | Configuração PostgreSQL, design do esquema de retalho, e dados de exemplo | [Construir](./04-Database/README.md) |
| 05 | [Implementação do Servidor MCP](./05-MCP-Server/README.md) | Construção do servidor FastMCP com integração de base de dados | [Construir](./05-MCP-Server/README.md) |
| 06 | [Desenvolvimento de Ferramentas](./06-Tools/README.md) | Criação de ferramentas de consulta à base de dados e introspeção de esquemas | [Construir](./06-Tools/README.md) |
| **Lab 7-9: Funcionalidades Avançadas** | | | |
| 07 | [Integração de Pesquisa Semântica](./07-Semantic-Search/README.md) | Implementação de embeddings vetoriais com Azure OpenAI e pgvector | [Avançar](./07-Semantic-Search/README.md) |
| 08 | [Testes e Depuração](./08-Testing/README.md) | Estratégias de teste, ferramentas de depuração e abordagens de validação | [Testar](./08-Testing/README.md) |
| 09 | [Integração VS Code](./09-VS-Code/README.md) | Configuração da integração MCP no VS Code e uso do Chat IA | [Integrar](./09-VS-Code/README.md) |
| **Lab 10-12: Produção e Melhores Práticas** | | | |
| 10 | [Estratégias de Implantação](./10-Deployment/README.md) | Implantação com Docker, Azure Container Apps e considerações de escalabilidade | [Implantar](./10-Deployment/README.md) |
| 11 | [Monitorização e Observabilidade](./11-Monitoring/README.md) | Application Insights, logging, monitorização de desempenho | [Monitorizar](./11-Monitoring/README.md) |
| 12 | [Melhores Práticas e Otimização](./12-Best-Practices/README.md) | Otimização de desempenho, reforço de segurança e dicas para produção | [Otimizar](./12-Best-Practices/README.md) |

### 💻 O Que Vai Construir

No final deste percurso de aprendizagem, terá construído um completo **Servidor MCP de Análise de Retalho Zava** com:

- **Base de dados de retalho multi-tabela** com encomendas de clientes, produtos e inventário
- **Row Level Security** para isolamento de dados por loja
- **Pesquisa semântica de produtos** usando embeddings Azure OpenAI
- **Integração VS Code AI Chat** para consultas em linguagem natural
- **Implantação pronta para produção** com Docker e Azure
- **Monitorização abrangente** com Application Insights

## 🎯 Pré-requisitos para Aprendizagem

Para tirar o máximo proveito deste percurso, deve ter:

- **Experiência em Programação**: Familiaridade com Python (preferido) ou linguagens similares
- **Conhecimento de Bases de Dados**: Compreensão básica de SQL e bases de dados relacionais
- **Conceitos de API**: Conhecimento de APIs REST e conceitos HTTP
- **Ferramentas de Desenvolvimento**: Experiência com linha de comando, Git, e editores de código
- **Noções de Cloud**: (Opcional) Conhecimentos básicos de Azure ou plataformas cloud similares
- **Familiaridade com Docker**: (Opcional) Compreensão de conceitos de contenorização

### Ferramentas Necessárias

- **Docker Desktop** - Para correr PostgreSQL e o servidor MCP
- **Azure CLI** - Para implantação de recursos na cloud
- **VS Code** - Para desenvolvimento e integração MCP
- **Git** - Para controlo de versões
- **Python 3.8+** - Para desenvolvimento do servidor MCP

## 📚 Guia de Estudo & Recursos

Este percurso de aprendizagem inclui recursos abrangentes para o ajudar a navegar eficazmente:

### Guia de Estudo

Cada laboratório inclui:
- **Objetivos claros de aprendizagem** - O que irá alcançar
- **Instruções passo a passo** - Guias detalhados de implementação
- **Exemplos de código** - Exemplos funcionais com explicações
- **Exercícios** - Oportunidades práticas para consolidar conhecimentos
- **Guias de resolução de problemas** - Problemas comuns e soluções
- **Recursos adicionais** - Leituras e explorações complementares

### Verificação de Pré-requisitos

Antes de começar cada laboratório, encontrará:
- **Conhecimentos necessários** - O que deve saber previamente
- **Validação da configuração** - Como verificar o seu ambiente
- **Estimativas de tempo** - Tempo esperado para conclusão
- **Resultados de aprendizagem** - O que saberá após concluir

### Percursos de Aprendizagem Recomendados

Escolha o seu percurso com base no seu nível de experiência:

#### 🟢 **Percurso para Iniciantes** (Novo no MCP)
1. Assegure que completou primeiro 0-10 de [MCP para Iniciantes](https://aka.ms/mcp-for-beginners)
2. Complete os laboratórios 00-03 para reforçar os fundamentos
3. Siga os laboratórios 04-06 para prática de construção
4. Experimente os laboratórios 07-09 para uso prático

#### 🟡 **Percurso Intermédio** (Alguma Experiência com MCP)
1. Reveja laboratórios 00-01 para conceitos específicos de base de dados
2. Concentre-se nos laboratórios 02-06 para implementação
3. Mergulhe nos laboratórios 07-12 para funcionalidades avançadas

#### 🔴 **Percurso Avançado** (Experiente em MCP)
1. Releia laboratórios 00-03 para contexto
2. Foque-se nos laboratórios 04-09 para integração de base de dados
3. Concentre-se nos laboratórios 10-12 para implantação em produção

## 🛠️ Como Usar Este Percurso de Aprendizagem de Forma Eficaz

### Aprendizagem Sequencial (Recomendado)

Prossiga pelos laboratórios por ordem para uma compreensão completa:

1. **Leia a visão geral** - Compreenda o que irá aprender
2. **Verifique os pré-requisitos** - Assegure que possui os conhecimentos necessários
3. **Siga os guias passo a passo** - Implemente enquanto aprende
4. **Complete os exercícios** - Reforce a compreensão
5. **Revise os principais pontos** - Consolide os resultados da aprendizagem

### Aprendizagem Direcionada

Se precisar de competências específicas:

- **Integração de Base de Dados**: Concentre-se nos laboratórios 04-06
- **Implementação de Segurança**: Foque nos laboratórios 02, 08, 12
- **IA/Pesquisa Semântica**: Mergulho profundo no laboratório 07
- **Implantação em Produção**: Estude os laboratórios 10-12

### Prática Hands-on

Cada laboratório inclui:
- **Exemplos de código funcionais** - Copie, modifique e experimente
- **Cenários do mundo real** - Casos práticos de análise de retalho
- **Complexidade progressiva** - Construção do simples ao avançado
- **Passos de validação** - Verifique se a implementação funciona

## 🌟 Comunidade e Suporte

### Obtenha Ajuda

- **Azure AI Discord**: [Junte-se para suporte especializado](https://discord.com/invite/ByRwuEEgH4)
- **Repositório GitHub e Exemplo de Implementação**: [Exemplo de Implantação e Recursos](https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail/)
- **Comunidade MCP**: [Participe em discussões MCP mais amplas](https://github.com/orgs/modelcontextprotocol/discussions)

## 🚀 Pronto para Começar?

Comece a sua jornada com **[Lab 00: Introdução à Integração MCP com Base de Dados](./00-Introduction/README.md)**

---

*Domine a construção de servidores MCP prontos para produção com integração de base de dados através desta experiência prática e abrangente de aprendizagem.*

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas resultantes da utilização desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->