# 🚀 Servidor MCP com PostgreSQL - Guia Completo de Aprendizagem

## 🧠 Visão Geral do Percurso de Aprendizagem de Integração de Base de Dados MCP

Este guia abrangente ensina como construir **servidores Model Context Protocol (MCP)** prontos para produção que se integram com bases de dados, através de uma implementação prática de análise de retalho. Aprenderá padrões de nível empresarial, incluindo **Segurança ao Nível de Linha (RLS)**, **pesquisa semântica**, **integração com Azure AI** e **acesso a dados multi-inquilino**.

Quer seja um programador backend, engenheiro de IA ou arquiteto de dados, este guia oferece uma aprendizagem estruturada com exemplos reais e exercícios práticos que o guiam através do seguinte servidor MCP https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail.

## 🔗 Recursos Oficiais do MCP

- 📘 [Documentação MCP](https://modelcontextprotocol.io/) – Tutoriais detalhados e guias de utilizador
- 📜 [Especificação MCP](https://modelcontextprotocol.io/docs/) – Arquitetura do protocolo e referências técnicas
- 🧑‍💻 [Repositório GitHub do MCP](https://github.com/modelcontextprotocol) – SDKs de código aberto, ferramentas e exemplos de código
- 🌐 [Comunidade MCP](https://github.com/orgs/modelcontextprotocol/discussions) – Participe em discussões e contribua para a comunidade

## 🧭 Percurso de Aprendizagem de Integração de Base de Dados MCP

### 📚 Estrutura Completa de Aprendizagem para https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail

| Laboratório | Tópico | Descrição | Link |
|-------------|--------|-----------|------|
| **Lab 1-3: Fundamentos** | | | |
| 00 | [Introdução à Integração de Base de Dados MCP](./00-Introduction/README.md) | Visão geral do MCP com integração de base de dados e caso de uso de análise de retalho | [Começar Aqui](./00-Introduction/README.md) |
| 01 | [Conceitos de Arquitetura Central](./01-Architecture/README.md) | Compreender a arquitetura do servidor MCP, camadas de base de dados e padrões de segurança | [Aprender](./01-Architecture/README.md) |
| 02 | [Segurança e Multi-Inquilino](./02-Security/README.md) | Segurança ao Nível de Linha, autenticação e acesso a dados multi-inquilino | [Aprender](./02-Security/README.md) |
| 03 | [Configuração do Ambiente](./03-Setup/README.md) | Configuração do ambiente de desenvolvimento, Docker, recursos Azure | [Configurar](./03-Setup/README.md) |
| **Lab 4-6: Construção do Servidor MCP** | | | |
| 04 | [Design e Esquema da Base de Dados](./04-Database/README.md) | Configuração do PostgreSQL, design do esquema de retalho e dados de exemplo | [Construir](./04-Database/README.md) |
| 05 | [Implementação do Servidor MCP](./05-MCP-Server/README.md) | Construção do servidor FastMCP com integração de base de dados | [Construir](./05-MCP-Server/README.md) |
| 06 | [Desenvolvimento de Ferramentas](./06-Tools/README.md) | Criação de ferramentas de consulta de base de dados e introspeção de esquema | [Construir](./06-Tools/README.md) |
| **Lab 7-9: Funcionalidades Avançadas** | | | |
| 07 | [Integração de Pesquisa Semântica](./07-Semantic-Search/README.md) | Implementação de embeddings vetoriais com Azure OpenAI e pgvector | [Avançar](./07-Semantic-Search/README.md) |
| 08 | [Testes e Depuração](./08-Testing/README.md) | Estratégias de teste, ferramentas de depuração e abordagens de validação | [Testar](./08-Testing/README.md) |
| 09 | [Integração com VS Code](./09-VS-Code/README.md) | Configuração da integração MCP com VS Code e uso de Chat AI | [Integrar](./09-VS-Code/README.md) |
| **Lab 10-12: Produção e Melhores Práticas** | | | |
| 10 | [Estratégias de Implementação](./10-Deployment/README.md) | Implementação com Docker, Azure Container Apps e considerações de escalabilidade | [Implementar](./10-Deployment/README.md) |
| 11 | [Monitorização e Observabilidade](./11-Monitoring/README.md) | Application Insights, registo de logs, monitorização de desempenho | [Monitorizar](./11-Monitoring/README.md) |
| 12 | [Melhores Práticas e Otimização](./12-Best-Practices/README.md) | Otimização de desempenho, reforço de segurança e dicas para produção | [Otimizar](./12-Best-Practices/README.md) |

### 💻 O Que Vai Construir

Ao final deste percurso de aprendizagem, terá construído um completo **Servidor MCP Zava Retail Analytics** com:

- **Base de dados de retalho multi-tabela** com encomendas de clientes, produtos e inventário
- **Segurança ao Nível de Linha** para isolamento de dados por loja
- **Pesquisa semântica de produtos** usando embeddings do Azure OpenAI
- **Integração com Chat AI no VS Code** para consultas em linguagem natural
- **Implementação pronta para produção** com Docker e Azure
- **Monitorização abrangente** com Application Insights

## 🎯 Pré-requisitos para Aprendizagem

Para aproveitar ao máximo este percurso de aprendizagem, deve ter:

- **Experiência em Programação**: Familiaridade com Python (preferido) ou linguagens similares
- **Conhecimento de Bases de Dados**: Compreensão básica de SQL e bases de dados relacionais
- **Conceitos de API**: Entendimento de APIs REST e conceitos HTTP
- **Ferramentas de Desenvolvimento**: Experiência com linha de comando, Git e editores de código
- **Noções de Cloud**: (Opcional) Conhecimento básico de Azure ou plataformas cloud similares
- **Familiaridade com Docker**: (Opcional) Compreensão de conceitos de containerização

### Ferramentas Necessárias

- **Docker Desktop** - Para executar PostgreSQL e o servidor MCP
- **Azure CLI** - Para implementação de recursos na cloud
- **VS Code** - Para desenvolvimento e integração MCP
- **Git** - Para controlo de versão
- **Python 3.8+** - Para desenvolvimento do servidor MCP

## 📚 Guia de Estudo e Recursos

Este percurso de aprendizagem inclui recursos abrangentes para ajudá-lo a navegar eficazmente:

### Guia de Estudo

Cada laboratório inclui:
- **Objetivos claros de aprendizagem** - O que irá alcançar
- **Instruções passo a passo** - Guias detalhados de implementação
- **Exemplos de código** - Exemplos funcionais com explicações
- **Exercícios** - Oportunidades práticas
- **Guias de resolução de problemas** - Problemas comuns e soluções
- **Recursos adicionais** - Leituras e explorações complementares

### Verificação de Pré-requisitos

Antes de iniciar cada laboratório, encontrará:
- **Conhecimento necessário** - O que deve saber previamente
- **Validação de configuração** - Como verificar o seu ambiente
- **Estimativas de tempo** - Tempo esperado para conclusão
- **Resultados de aprendizagem** - O que saberá após a conclusão

### Percursos de Aprendizagem Recomendados

Escolha o percurso com base no seu nível de experiência:

#### 🟢 **Percurso para Iniciantes** (Novo no MCP)
1. Certifique-se de que completou 0-10 de [MCP para Iniciantes](https://aka.ms/mcp-for-beginners) primeiro
2. Complete os laboratórios 00-03 para reforçar os fundamentos
3. Siga os laboratórios 04-06 para construção prática
4. Experimente os laboratórios 07-09 para uso prático

#### 🟡 **Percurso Intermediário** (Alguma Experiência com MCP)
1. Revise os laboratórios 00-01 para conceitos específicos de base de dados
2. Foque nos laboratórios 02-06 para implementação
3. Aprofunde-se nos laboratórios 07-12 para funcionalidades avançadas

#### 🔴 **Percurso Avançado** (Experiente com MCP)
1. Passe rapidamente pelos laboratórios 00-03 para contexto
2. Foque nos laboratórios 04-09 para integração de base de dados
3. Concentre-se nos laboratórios 10-12 para implementação em produção

## 🛠️ Como Usar Este Percurso de Aprendizagem Eficazmente

### Aprendizagem Sequencial (Recomendado)

Trabalhe nos laboratórios em ordem para uma compreensão completa:

1. **Leia a visão geral** - Entenda o que irá aprender
2. **Verifique os pré-requisitos** - Certifique-se de que tem o conhecimento necessário
3. **Siga os guias passo a passo** - Implemente enquanto aprende
4. **Complete os exercícios** - Reforce a sua compreensão
5. **Revise os principais pontos** - Solidifique os resultados de aprendizagem

### Aprendizagem Direcionada

Se precisar de habilidades específicas:

- **Integração de Base de Dados**: Foque nos laboratórios 04-06
- **Implementação de Segurança**: Concentre-se nos laboratórios 02, 08, 12
- **IA/Pesquisa Semântica**: Aprofunde-se no laboratório 07
- **Implementação em Produção**: Estude os laboratórios 10-12

### Prática Prática

Cada laboratório inclui:
- **Exemplos de código funcionais** - Copie, modifique e experimente
- **Cenários reais** - Casos práticos de análise de retalho
- **Complexidade progressiva** - Construção de simples para avançado
- **Passos de validação** - Verifique se a sua implementação funciona

## 🌟 Comunidade e Suporte

### Obtenha Ajuda

- **Discord Azure AI**: [Junte-se para suporte especializado](https://discord.com/invite/ByRwuEEgH4)
- **Repositório GitHub e Exemplo de Implementação**: [Exemplo de Implementação e Recursos](https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail/)
- **Comunidade MCP**: [Participe em discussões mais amplas sobre MCP](https://github.com/orgs/modelcontextprotocol/discussions)

## 🚀 Pronto para Começar?

Inicie a sua jornada com **[Lab 00: Introdução à Integração de Base de Dados MCP](./00-Introduction/README.md)**

---

*Domine a construção de servidores MCP prontos para produção com integração de base de dados através desta experiência prática e abrangente.*

---

**Aviso**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, é importante notar que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autoritária. Para informações críticas, recomenda-se uma tradução profissional realizada por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes da utilização desta tradução.