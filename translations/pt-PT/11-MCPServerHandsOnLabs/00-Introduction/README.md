# Introdução à Integração de Base de Dados MCP

> [!NOTE]
> Diagramas ou código neste percurso de aprendizagem que usem HTTP/SSE ou opções de inicialização
> refletem as dependências MCP do exemplo `2025-11-25`. Para novas
> implementações, utilize pedidos sem estado `2026-07-28` e Streamable HTTP.

## 🎯 O Que Este Laboratório Aborda

Este laboratório introdutório fornece uma visão abrangente da construção de servidores Model Context Protocol (MCP) com integração de base de dados. Vai compreender o caso de negócio, arquitetura técnica e aplicações no mundo real através do caso de uso analítico da Zava Retail em https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail.

## Visão Geral

**Model Context Protocol (MCP)** permite aos assistentes de IA aceder e interagir com fontes de dados externas em tempo real de forma segura. Quando combinado com integração de base de dados, o MCP desbloqueia poderosas capacidades para aplicações de IA baseadas em dados.

Este percurso de aprendizagem ensina a construir servidores MCP prontos para produção que ligam assistentes de IA a dados de vendas no retalho através do PostgreSQL, implementando padrões empresariais como Row Level Security, pesquisa semântica e acesso a dados multi-inquilino.

## Objetivos de Aprendizagem

No final deste laboratório, será capaz de:

- **Definir** o Model Context Protocol e os seus benefícios principais para integração de bases de dados
- **Identificar** componentes chave da arquitetura de um servidor MCP com bases de dados
- **Compreender** o caso de uso da Zava Retail e os seus requisitos de negócio
- **Reconhecer** padrões empresariais para acesso seguro e escalável a bases de dados
- **Enumerar** as ferramentas e tecnologias utilizadas ao longo deste percurso de aprendizagem

## 🧭 O Desafio: IA Encontra Dados do Mundo Real

### Limitações Tradicionais da IA

Assistentes modernos de IA são incrivelmente poderosos mas enfrentam limitações significativas ao trabalhar com dados empresariais do mundo real:

| **Desafio** | **Descrição** | **Impacto nos Negócios** |
|---------------|-----------------|-------------------|
| **Conhecimento Estático** | Modelos de IA treinados em conjuntos de dados fixos não conseguem aceder a dados empresariais atuais | Insights desatualizados, oportunidades perdidas |
| **Silos de Dados** | Informação bloqueada em bases de dados, APIs e sistemas inacessíveis à IA | Análise incompleta, fluxos de trabalho fragmentados |
| **Restrições de Segurança** | Acesso direto à base de dados levanta preocupações de segurança e conformidade | Implementação limitada, preparação manual de dados |
| **Consultas Complexas** | Utilizadores empresariais necessitam de conhecimento técnico para extrair insights | Adoção reduzida, processos ineficientes |

### A Solução MCP

O Model Context Protocol aborda estes desafios fornecendo:

- **Acesso a Dados em Tempo Real**: assistentes de IA consultam bases de dados e APIs ao vivo
- **Integração Segura**: acesso controlado com autenticação e permissões
- **Interface em Linguagem Natural**: utilizadores empresariais fazem perguntas em inglês claro
- **Protocolo Padronizado**: funciona em diferentes plataformas e ferramentas de IA

## 🏪 Conheça a Zava Retail: O Nosso Caso de Estudo https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail

Ao longo deste percurso de aprendizagem, construiremos um servidor MCP para a **Zava Retail**, uma cadeia fictícia de retalho DIY com várias localizações. Este cenário realista demonstra uma implementação MCP de nível empresarial.

### Contexto Empresarial

**Zava Retail** opera:
- **8 lojas físicas** pelo estado de Washington (Seattle, Bellevue, Tacoma, Spokane, Everett, Redmond, Kirkland)
- **1 loja online** para vendas de comércio eletrónico
- **Catálogo diversificado de produtos** incluindo ferramentas, ferragens, artigos de jardim e materiais de construção
- **Gestão multinível** com gerentes de loja, gerentes regionais e executivos

### Requisitos de Negócio

Gerentes de loja e executivos precisam de análises potenciadas por IA para:

1. **Analisar o desempenho das vendas** entre lojas e períodos de tempo
2. **Monitorizar níveis de inventário** e identificar necessidades de reabastecimento
3. **Compreender o comportamento do cliente** e padrões de compra
4. **Descobrir insights de produtos** através de pesquisa semântica
5. **Gerar relatórios** com consultas em linguagem natural
6. **Manter a segurança dos dados** com controlo de acesso baseado em funções

### Requisitos Técnicos

O servidor MCP deve fornecer:

- **Acesso multi-inquilino a dados** onde gerentes de loja veem apenas os dados da sua loja
- **Consultas flexíveis** suportando operações SQL complexas
- **Pesquisa semântica** para descoberta de produtos e recomendações
- **Dados em tempo real** refletindo o estado atual do negócio
- **Autenticação segura** com segurança ao nível das linhas (row-level security)
- **Arquitetura escalável** suportando múltiplos utilizadores concorrentes

## 🏗️ Visão Geral da Arquitetura do Servidor MCP

O nosso servidor MCP implementa uma arquitetura em camadas otimizada para integração de base de dados:

```
┌─────────────────────────────────────────────────────────────┐
│                    VS Code AI Client                       │
│                  (Natural Language Queries)                │
└─────────────────────┬───────────────────────────────────────┘
                      │ HTTP/SSE
                      ▼
┌─────────────────────────────────────────────────────────────┐
│                     MCP Server                             │
│  ┌─────────────────┐ ┌─────────────────┐ ┌───────────────┐ │
│  │   Tool Layer    │ │  Security Layer │ │  Config Layer │ │
│  │                 │ │                 │ │               │ │
│  │ • Query Tools   │ │ • RLS Context   │ │ • Environment │ │
│  │ • Schema Tools  │ │ • User Identity │ │ • Connections │ │
│  │ • Search Tools  │ │ • Access Control│ │ • Validation  │ │
│  └─────────────────┘ └─────────────────┘ └───────────────┘ │
└─────────────────────┬───────────────────────────────────────┘
                      │ asyncpg
                      ▼
┌─────────────────────────────────────────────────────────────┐
│                PostgreSQL Database                         │
│  ┌─────────────────┐ ┌─────────────────┐ ┌───────────────┐ │
│  │  Retail Schema  │ │   RLS Policies  │ │   pgvector    │ │
│  │                 │ │                 │ │               │ │
│  │ • Stores        │ │ • Store-based   │ │ • Embeddings  │ │
│  │ • Customers     │ │   Isolation     │ │ • Similarity  │ │
│  │ • Products      │ │ • Role Control  │ │   Search      │ │
│  │ • Orders        │ │ • Audit Logs    │ │               │ │
│  └─────────────────┘ └─────────────────┘ └───────────────┘ │
└─────────────────────┬───────────────────────────────────────┘
                      │ REST API
                      ▼
┌─────────────────────────────────────────────────────────────┐
│                  Azure OpenAI                              │
│               (Text Embeddings)                            │
└─────────────────────────────────────────────────────────────┘
```

### Componentes Principais

#### **1. Camada do Servidor MCP**
- **FastMCP Framework**: implementação moderna do servidor MCP em Python
- **Registo de Ferramentas**: definições declarativas de ferramentas com segurança de tipos
- **Contexto de Pedido**: identidade do utilizador e gestão de sessão
- **Gestão de Erros**: administração robusta de erros e registos

#### **2. Camada de Integração de Base de Dados**
- **Gestão de Conexões**: gestão eficiente de conexões asyncpg
- **Fornecedor de Esquema**: descoberta dinâmica do esquema das tabelas
- **Executor de Consultas**: execução SQL segura com contexto RLS
- **Gestão de Transações**: conformidade ACID e gestão de rollback

#### **3. Camada de Segurança**
- **Row Level Security**: RLS do PostgreSQL para isolamento de dados multi-inquilino
- **Identidade do Utilizador**: autenticação e autorização do gerente da loja
- **Controlo de Acesso**: permissões granulares e auditorias
- **Validação de Entrada**: prevenção contra injeção SQL e validação de consultas

#### **4. Camada de Melhoria de IA**
- **Pesquisa Semântica**: embeddings vetoriais para descoberta de produtos
- **Integração Azure OpenAI**: geração de embeddings de texto
- **Algoritmos de Similaridade**: pesquisa de similaridade por cosseno com pgvector
- **Otimização de Pesquisa**: indexação e ajuste de performance

## 🔧 Pilha Tecnológica

### Tecnologias Base

| **Componente** | **Tecnologia** | **Propósito** |
|---------------|----------------|-------------|
| **Framework MCP** | FastMCP (Python) | Implementação moderna do servidor MCP |
| **Base de Dados** | PostgreSQL 17 + pgvector | Dados relacionais com pesquisa vetorial |
| **Serviços de IA** | Azure OpenAI | Embeddings de texto e modelos de linguagem |
| **Containerização** | Docker + Docker Compose | Ambiente de desenvolvimento |
| **Plataforma Cloud** | Microsoft Azure | Implantação em produção |
| **Integração IDE** | VS Code | Chat de IA e fluxo de trabalho de desenvolvimento |

### Ferramentas de Desenvolvimento

| **Ferramenta** | **Propósito** |
|----------|-------------|
| **asyncpg** | Driver PostgreSQL de alto desempenho |
| **Pydantic** | Validação e serialização de dados |
| **Azure SDK** | Integração com serviços cloud |
| **pytest** | Framework de testes |
| **Docker** | Containerização e implantação |

### Pilha de Produção

| **Serviço** | **Recurso Azure** | **Propósito** |
|-------------|-------------------|-------------|
| **Base de Dados** | Azure Database for PostgreSQL | Serviço gerido de base de dados |
| **Contentor** | Azure Container Apps | Alojamento serverless de contentores |

| **Serviços de IA** | Microsoft Foundry | Modelos e endpoints OpenAI |
| **Monitorização** | Application Insights | Observabilidade e diagnóstico |
| **Segurança** | Azure Key Vault | Gestão de segredos e configuração |

## 🎬 Cenários de Utilização no Mundo Real

Vamos explorar como diferentes utilizadores interagem com o nosso servidor MCP:

### Cenário 1: Revisão de Desempenho do Gestor de Loja

**Utilizador**: Sarah, Gestora da Loja de Seattle  
**Objetivo**: Analisar o desempenho de vendas do último trimestre

**Consulta em Linguagem Natural**:
> "Mostra-me os 10 principais produtos por receita na minha loja no Q4 de 2024"

**O que Acontece**:
1. O chat AI do VS Code envia a consulta para o servidor MCP
2. O servidor MCP identifica o contexto da loja da Sarah (Seattle)
3. As políticas RLS filtram dados apenas para a loja de Seattle
4. A consulta SQL é gerada e executada
5. Os resultados são formatados e retornados ao AI Chat
6. A IA fornece análise e insights

### Cenário 2: Descoberta de Produtos com Pesquisa Semântica

**Utilizador**: Mike, Gestor de Inventário  
**Objetivo**: Encontrar produtos semelhantes a um pedido de um cliente

**Consulta em Linguagem Natural**:
> "Que produtos vendemos que são semelhantes a 'conectores elétricos impermeáveis para uso externo'?"

**O que Acontece**:
1. A consulta é processada pela ferramenta de pesquisa semântica
2. Azure OpenAI gera um vetor de embedding
3. pgvector realiza a pesquisa de similaridade
4. Produtos relacionados são classificados por relevância
5. Os resultados incluem detalhes e disponibilidade dos produtos
6. A IA sugere alternativas e oportunidades de agrupar produtos

### Cenário 3: Análise entre Lojas

**Utilizador**: Jennifer, Gestora Regional  
**Objetivo**: Comparar desempenho entre todas as lojas

**Consulta em Linguagem Natural**:
> "Comparar vendas por categoria para todas as lojas nos últimos 6 meses"

**O que Acontece**:
1. Contexto RLS definido para acesso da gestora regional
2. Consulta complexa multi-lojas gerada
3. Dados agregados entre localizações das lojas
4. Resultados incluem tendências e comparações
5. A IA identifica insights e recomendações

## 🔒 Segurança e Multi-Inquilino em Profundidade

A nossa implementação prioriza segurança de nível empresarial:

### Segurança ao Nível da Linha (RLS)

A RLS do PostgreSQL assegura a isolação de dados:

```sql
-- Store managers see only their store's data
CREATE POLICY store_manager_policy ON retail.orders
  FOR ALL TO store_managers
  USING (store_id = get_current_user_store());

-- Regional managers see multiple stores
CREATE POLICY regional_manager_policy ON retail.orders
  FOR ALL TO regional_managers
  USING (store_id = ANY(get_user_store_list()));
```

### Gestão de Identidade do Utilizador

Cada conexão MCP inclui:
- **ID do Gestor da Loja**: Identificador único para o contexto RLS
- **Atribuição de Função**: Permissões e níveis de acesso
- **Gestão de Sessão**: Tokens de autenticação seguros
- **Registo de Auditoria**: Histórico completo de acessos

### Proteção de Dados

Múltiplas camadas de segurança:
- **Criptografia da Conexão**: TLS para todas as conexões à base de dados
- **Prevenção de Injeção SQL**: Apenas consultas parametrizadas
- **Validação de Entrada**: Validação abrangente de pedidos
- **Tratamento de Erros**: Nenhum dado sensível nas mensagens de erro

## 🎯 Principais Conclusões

Após concluir esta introdução, deverá compreender:

✅ **Proposta de Valor do MCP**: Como o MCP liga assistentes de IA e dados do mundo real  
✅ **Contexto Empresarial**: Requisitos e desafios da Zava Retail  
✅ **Visão Geral da Arquitetura**: Componentes chave e suas interações  
✅ **Stack Tecnológico**: Ferramentas e frameworks utilizados  
✅ **Modelo de Segurança**: Acesso e proteção de dados multi-inquilino  
✅ **Padrões de Utilização**: Cenários e fluxos de consulta reais  

## 🚀 Próximos Passos

Pronto para aprofundar? Continue com:

**[Laboratório 01: Conceitos de Arquitetura Básicos](../01-Architecture/README.md)**

Aprenda sobre padrões de arquitetura do servidor MCP, princípios de design de bases de dados e a implementação técnica detalhada que suporta a nossa solução de análise para retalho.

## 📚 Recursos Adicionais

### Documentação MCP
- [Especificação MCP](https://modelcontextprotocol.io/docs/) - Documentação oficial do protocolo
- [MCP para Iniciantes](https://aka.ms/mcp-for-beginners) - Guia abrangente de aprendizagem MCP
- [Documentação FastMCP](https://github.com/modelcontextprotocol/python-sdk) - Documentação do SDK Python

### Integração de Base de Dados
- [Documentação PostgreSQL](https://www.postgresql.org/docs/) - Referência completa do PostgreSQL
- [Guia pgvector](https://github.com/pgvector/pgvector) - Documentação da extensão de vetores
- [Segurança ao Nível da Linha](https://www.postgresql.org/docs/current/ddl-rowsecurity.html) - Guia PostgreSQL RLS

### Serviços Azure
- [Documentação Azure OpenAI](https://docs.microsoft.com/azure/cognitive-services/openai/) - Integração de serviço de IA
- [Azure Database para PostgreSQL](https://docs.microsoft.com/azure/postgresql/) - Serviço gerido de base de dados
- [Azure Container Apps](https://docs.microsoft.com/azure/container-apps/) - Contentores sem servidor

---

**Aviso Legal**: Este é um exercício de aprendizagem usando dados fictícios de retalho. Sempre siga as políticas de governação e segurança de dados da sua organização ao implementar soluções similares em ambientes de produção.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas resultantes da utilização desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->