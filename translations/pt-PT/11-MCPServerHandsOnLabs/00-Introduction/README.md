# Introdução à Integração de Bases de Dados com MCP

## 🎯 O Que Este Laboratório Abrange

Este laboratório introdutório oferece uma visão abrangente sobre como construir servidores Model Context Protocol (MCP) com integração de bases de dados. Irá compreender o caso de negócio, a arquitetura técnica e as aplicações reais através do caso de uso de análise de retalho da Zava Retail em https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail.

## Visão Geral

O **Model Context Protocol (MCP)** permite que assistentes de IA acedam e interajam de forma segura com fontes de dados externas em tempo real. Quando combinado com a integração de bases de dados, o MCP desbloqueia capacidades poderosas para aplicações de IA orientadas por dados.

Este percurso de aprendizagem ensina-o a construir servidores MCP prontos para produção que conectam assistentes de IA a dados de vendas de retalho através do PostgreSQL, implementando padrões empresariais como Segurança ao Nível de Linha (Row Level Security), pesquisa semântica e acesso a dados multi-inquilino.

## Objetivos de Aprendizagem

Ao final deste laboratório, será capaz de:

- **Definir** o Model Context Protocol e os seus principais benefícios para integração de bases de dados
- **Identificar** os componentes-chave de uma arquitetura de servidor MCP com bases de dados
- **Compreender** o caso de uso da Zava Retail e os seus requisitos de negócio
- **Reconhecer** padrões empresariais para acesso seguro e escalável a bases de dados
- **Listar** as ferramentas e tecnologias utilizadas ao longo deste percurso de aprendizagem

## 🧭 O Desafio: IA Encontra Dados do Mundo Real

### Limitações Tradicionais da IA

Os assistentes de IA modernos são incrivelmente poderosos, mas enfrentam limitações significativas ao trabalhar com dados de negócios do mundo real:

| **Desafio**         | **Descrição**                                   | **Impacto no Negócio**               |
|----------------------|------------------------------------------------|--------------------------------------|
| **Conhecimento Estático** | Modelos de IA treinados em conjuntos de dados fixos não conseguem aceder a dados atuais de negócios | Insights desatualizados, oportunidades perdidas |
| **Silos de Dados**   | Informação bloqueada em bases de dados, APIs e sistemas que a IA não consegue alcançar | Análise incompleta, fluxos de trabalho fragmentados |
| **Restrições de Segurança** | O acesso direto à base de dados levanta preocupações de segurança e conformidade | Implementação limitada, preparação manual de dados |
| **Consultas Complexas** | Utilizadores de negócios precisam de conhecimento técnico para extrair insights de dados | Adoção reduzida, processos ineficientes |

### A Solução MCP

O Model Context Protocol aborda estes desafios ao fornecer:

- **Acesso a Dados em Tempo Real**: Assistentes de IA consultam bases de dados e APIs ao vivo
- **Integração Segura**: Acesso controlado com autenticação e permissões
- **Interface em Linguagem Natural**: Utilizadores de negócios fazem perguntas em linguagem simples
- **Protocolo Padronizado**: Funciona em diferentes plataformas e ferramentas de IA

## 🏪 Conheça a Zava Retail: Nosso Caso de Estudo https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail

Ao longo deste percurso de aprendizagem, construiremos um servidor MCP para a **Zava Retail**, uma cadeia fictícia de retalho de bricolage com várias localizações de lojas. Este cenário realista demonstra uma implementação de MCP de nível empresarial.

### Contexto de Negócio

A **Zava Retail** opera:
- **8 lojas físicas** no estado de Washington (Seattle, Bellevue, Tacoma, Spokane, Everett, Redmond, Kirkland)
- **1 loja online** para vendas de e-commerce
- **Catálogo diversificado de produtos** incluindo ferramentas, materiais de construção, artigos de jardim e hardware
- **Gestão em vários níveis** com gerentes de loja, gerentes regionais e executivos

### Requisitos de Negócio

Os gerentes de loja e executivos precisam de análises impulsionadas por IA para:

1. **Analisar o desempenho de vendas** entre lojas e períodos de tempo
2. **Monitorizar níveis de inventário** e identificar necessidades de reposição
3. **Compreender o comportamento dos clientes** e padrões de compra
4. **Descobrir insights sobre produtos** através de pesquisa semântica
5. **Gerar relatórios** com consultas em linguagem natural
6. **Manter a segurança dos dados** com controle de acesso baseado em funções

### Requisitos Técnicos

O servidor MCP deve fornecer:

- **Acesso a dados multi-inquilino**, onde os gerentes de loja veem apenas os dados da sua loja
- **Consultas flexíveis** que suportem operações SQL complexas
- **Pesquisa semântica** para descoberta de produtos e recomendações
- **Dados em tempo real** refletindo o estado atual do negócio
- **Autenticação segura** com segurança ao nível de linha
- **Arquitetura escalável** suportando múltiplos utilizadores simultâneos

## 🏗️ Visão Geral da Arquitetura do Servidor MCP

O nosso servidor MCP implementa uma arquitetura em camadas otimizada para integração de bases de dados:

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

#### **1. Camada de Servidor MCP**
- **FastMCP Framework**: Implementação moderna de servidor MCP em Python
- **Registo de Ferramentas**: Definições declarativas de ferramentas com segurança de tipos
- **Contexto de Pedido**: Gestão de identidade do utilizador e sessão
- **Gestão de Erros**: Gestão robusta de erros e registo

#### **2. Camada de Integração de Base de Dados**
- **Pooling de Conexões**: Gestão eficiente de conexões asyncpg
- **Provedor de Esquema**: Descoberta dinâmica de esquemas de tabelas
- **Executor de Consultas**: Execução segura de SQL com contexto RLS
- **Gestão de Transações**: Conformidade ACID e gestão de rollback

#### **3. Camada de Segurança**
- **Segurança ao Nível de Linha**: RLS do PostgreSQL para isolamento de dados multi-inquilino
- **Identidade do Utilizador**: Autenticação e autorização de gerentes de loja
- **Controle de Acesso**: Permissões detalhadas e trilhas de auditoria
- **Validação de Entrada**: Prevenção de injeção SQL e validação de consultas

#### **4. Camada de Melhoria de IA**
- **Pesquisa Semântica**: Embeddings vetoriais para descoberta de produtos
- **Integração Azure OpenAI**: Geração de embeddings de texto
- **Algoritmos de Similaridade**: Pesquisa de similaridade por cosseno com pgvector
- **Otimização de Pesquisa**: Indexação e ajuste de desempenho

## 🔧 Stack Tecnológico

### Tecnologias Principais

| **Componente**       | **Tecnologia**            | **Finalidade**                     |
|-----------------------|---------------------------|-------------------------------------|
| **Framework MCP**     | FastMCP (Python)         | Implementação moderna de servidor MCP |
| **Base de Dados**     | PostgreSQL 17 + pgvector | Dados relacionais com pesquisa vetorial |
| **Serviços de IA**    | Azure OpenAI             | Embeddings de texto e modelos de linguagem |
| **Containerização**   | Docker + Docker Compose  | Ambiente de desenvolvimento         |
| **Plataforma Cloud**  | Microsoft Azure          | Implementação em produção           |
| **Integração IDE**    | VS Code                  | Chat de IA e fluxo de trabalho de desenvolvimento |

### Ferramentas de Desenvolvimento

| **Ferramenta**        | **Finalidade**           |
|------------------------|--------------------------|
| **asyncpg**           | Driver PostgreSQL de alto desempenho |
| **Pydantic**          | Validação e serialização de dados |
| **Azure SDK**         | Integração de serviços cloud |
| **pytest**            | Framework de testes      |
| **Docker**            | Containerização e implementação |

### Stack de Produção

| **Serviço**           | **Recurso Azure**        | **Finalidade**                     |
|------------------------|--------------------------|-------------------------------------|
| **Base de Dados**      | Azure Database for PostgreSQL | Serviço de base de dados gerido    |
| **Container**          | Azure Container Apps    | Hospedagem de containers sem servidor |
| **Serviços de IA**     | Azure AI Foundry        | Modelos OpenAI e endpoints         |
| **Monitorização**      | Application Insights    | Observabilidade e diagnósticos     |
| **Segurança**          | Azure Key Vault         | Gestão de segredos e configuração  |

## 🎬 Cenários de Uso no Mundo Real

Vamos explorar como diferentes utilizadores interagem com o nosso servidor MCP:

### Cenário 1: Revisão de Desempenho do Gerente de Loja

**Utilizador**: Sarah, Gerente da Loja de Seattle  
**Objetivo**: Analisar o desempenho de vendas do último trimestre

**Consulta em Linguagem Natural**:
> "Mostre-me os 10 produtos com maior receita na minha loja no Q4 de 2024"

**O Que Acontece**:
1. O chat de IA no VS Code envia a consulta ao servidor MCP
2. O servidor MCP identifica o contexto da loja de Sarah (Seattle)
3. As políticas RLS filtram os dados apenas para a loja de Seattle
4. A consulta SQL é gerada e executada
5. Os resultados são formatados e retornados ao chat de IA
6. A IA fornece análise e insights

### Cenário 2: Descoberta de Produtos com Pesquisa Semântica

**Utilizador**: Mike, Gerente de Inventário  
**Objetivo**: Encontrar produtos semelhantes a um pedido de cliente

**Consulta em Linguagem Natural**:
> "Que produtos vendemos que são semelhantes a 'conectores elétricos impermeáveis para uso externo'?"

**O Que Acontece**:
1. A consulta é processada pela ferramenta de pesquisa semântica
2. O Azure OpenAI gera o vetor de embedding
3. O pgvector realiza a pesquisa de similaridade
4. Os produtos relacionados são classificados por relevância
5. Os resultados incluem detalhes e disponibilidade dos produtos
6. A IA sugere alternativas e oportunidades de agrupamento

### Cenário 3: Análise Entre Lojas

**Utilizador**: Jennifer, Gerente Regional  
**Objetivo**: Comparar o desempenho entre todas as lojas

**Consulta em Linguagem Natural**:
> "Compare as vendas por categoria em todas as lojas nos últimos 6 meses"

**O Que Acontece**:
1. O contexto RLS é definido para acesso de gerente regional
2. Uma consulta complexa entre lojas é gerada
3. Os dados são agregados entre as localizações das lojas
4. Os resultados incluem tendências e comparações
5. A IA identifica insights e recomendações

## 🔒 Mergulho Profundo em Segurança e Multi-Inquilino

A nossa implementação prioriza segurança de nível empresarial:

### Segurança ao Nível de Linha (RLS)

O PostgreSQL RLS garante isolamento de dados:

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
- **ID do Gerente de Loja**: Identificador único para contexto RLS
- **Atribuição de Funções**: Permissões e níveis de acesso
- **Gestão de Sessão**: Tokens de autenticação seguros
- **Registo de Auditoria**: Histórico completo de acessos

### Proteção de Dados

Múltiplas camadas de segurança:
- **Encriptação de Conexão**: TLS para todas as conexões de base de dados
- **Prevenção de Injeção SQL**: Apenas consultas parametrizadas
- **Validação de Entrada**: Validação abrangente de pedidos
- **Gestão de Erros**: Sem dados sensíveis em mensagens de erro

## 🎯 Principais Conclusões

Após completar esta introdução, deverá compreender:

✅ **Proposta de Valor do MCP**: Como o MCP conecta assistentes de IA a dados do mundo real  
✅ **Contexto de Negócio**: Requisitos e desafios da Zava Retail  
✅ **Visão Geral da Arquitetura**: Componentes principais e suas interações  
✅ **Stack Tecnológico**: Ferramentas e frameworks utilizados  
✅ **Modelo de Segurança**: Acesso a dados multi-inquilino e proteção  
✅ **Padrões de Uso**: Cenários de consulta e fluxos de trabalho no mundo real  

## 🚀 Próximos Passos

Pronto para aprofundar? Continue com:

**[Laboratório 01: Conceitos Fundamentais de Arquitetura](../01-Architecture/README.md)**

Aprenda sobre padrões de arquitetura de servidores MCP, princípios de design de bases de dados e a implementação técnica detalhada que alimenta a nossa solução de análise de retalho.

## 📚 Recursos Adicionais

### Documentação MCP
- [Especificação MCP](https://modelcontextprotocol.io/docs/) - Documentação oficial do protocolo
- [MCP para Iniciantes](https://aka.ms/mcp-for-beginners) - Guia abrangente de aprendizagem MCP
- [Documentação FastMCP](https://github.com/modelcontextprotocol/python-sdk) - Documentação do SDK Python

### Integração de Bases de Dados
- [Documentação PostgreSQL](https://www.postgresql.org/docs/) - Referência completa do PostgreSQL
- [Guia pgvector](https://github.com/pgvector/pgvector) - Documentação da extensão vetorial
- [Segurança ao Nível de Linha](https://www.postgresql.org/docs/current/ddl-rowsecurity.html) - Guia RLS do PostgreSQL

### Serviços Azure
- [Documentação Azure OpenAI](https://docs.microsoft.com/azure/cognitive-services/openai/) - Integração de serviços de IA
- [Azure Database for PostgreSQL](https://docs.microsoft.com/azure/postgresql/) - Serviço de base de dados gerido
- [Azure Container Apps](https://docs.microsoft.com/azure/container-apps/) - Containers sem servidor

---

**Aviso**: Este é um exercício de aprendizagem utilizando dados fictícios de retalho. Siga sempre as políticas de governança e segurança de dados da sua organização ao implementar soluções semelhantes em ambientes de produção.

---

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autoritária. Para informações críticas, recomenda-se uma tradução profissional realizada por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.