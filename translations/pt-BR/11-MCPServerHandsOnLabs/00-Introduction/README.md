# Introdução à Integração de Banco de Dados com MCP

## 🎯 O Que Este Laboratório Abrange

Este laboratório introdutório oferece uma visão abrangente sobre como construir servidores Model Context Protocol (MCP) com integração de banco de dados. Você entenderá o caso de negócio, a arquitetura técnica e as aplicações no mundo real por meio do caso de uso de análise de varejo da Zava Retail em https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail.

## Visão Geral

O **Model Context Protocol (MCP)** permite que assistentes de IA acessem e interajam com fontes de dados externas em tempo real de forma segura. Quando combinado com a integração de banco de dados, o MCP desbloqueia capacidades poderosas para aplicações de IA orientadas por dados.

Este caminho de aprendizado ensina você a construir servidores MCP prontos para produção que conectam assistentes de IA a dados de vendas no varejo por meio do PostgreSQL, implementando padrões empresariais como Segurança em Nível de Linha, busca semântica e acesso a dados multi-tenant.

## Objetivos de Aprendizado

Ao final deste laboratório, você será capaz de:

- **Definir** o Model Context Protocol e seus principais benefícios para integração de banco de dados
- **Identificar** os componentes-chave de uma arquitetura de servidor MCP com bancos de dados
- **Compreender** o caso de uso da Zava Retail e seus requisitos de negócio
- **Reconhecer** padrões empresariais para acesso seguro e escalável a bancos de dados
- **Listar** as ferramentas e tecnologias utilizadas ao longo deste caminho de aprendizado

## 🧭 O Desafio: IA Encontra Dados do Mundo Real

### Limitações Tradicionais da IA

Assistentes de IA modernos são incrivelmente poderosos, mas enfrentam limitações significativas ao trabalhar com dados de negócios do mundo real:

| **Desafio**         | **Descrição**                                      | **Impacto nos Negócios**               |
|----------------------|---------------------------------------------------|----------------------------------------|
| **Conhecimento Estático** | Modelos de IA treinados em conjuntos de dados fixos não conseguem acessar dados atuais de negócios | Insights desatualizados, oportunidades perdidas |
| **Silos de Dados**   | Informações bloqueadas em bancos de dados, APIs e sistemas que a IA não consegue acessar | Análises incompletas, fluxos de trabalho fragmentados |
| **Restrições de Segurança** | Acesso direto ao banco de dados levanta preocupações de segurança e conformidade | Implantação limitada, preparação manual de dados |
| **Consultas Complexas** | Usuários de negócios precisam de conhecimento técnico para extrair insights de dados | Adoção reduzida, processos ineficientes |

### A Solução MCP

O Model Context Protocol aborda esses desafios fornecendo:

- **Acesso a Dados em Tempo Real**: Assistentes de IA consultam bancos de dados e APIs ao vivo
- **Integração Segura**: Acesso controlado com autenticação e permissões
- **Interface em Linguagem Natural**: Usuários de negócios fazem perguntas em linguagem simples
- **Protocolo Padronizado**: Funciona em diferentes plataformas e ferramentas de IA

## 🏪 Conheça a Zava Retail: Nosso Estudo de Caso de Aprendizado https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail

Ao longo deste caminho de aprendizado, construiremos um servidor MCP para a **Zava Retail**, uma cadeia fictícia de varejo de bricolagem com várias localizações de lojas. Este cenário realista demonstra a implementação de MCP em nível empresarial.

### Contexto de Negócio

A **Zava Retail** opera:
- **8 lojas físicas** no estado de Washington (Seattle, Bellevue, Tacoma, Spokane, Everett, Redmond, Kirkland)
- **1 loja online** para vendas de e-commerce
- **Catálogo diversificado de produtos** incluindo ferramentas, materiais de construção, suprimentos de jardim e hardware
- **Gestão em múltiplos níveis** com gerentes de loja, gerentes regionais e executivos

### Requisitos de Negócio

Gerentes de loja e executivos precisam de análises baseadas em IA para:

1. **Analisar o desempenho de vendas** entre lojas e períodos de tempo
2. **Acompanhar níveis de estoque** e identificar necessidades de reposição
3. **Compreender o comportamento do cliente** e padrões de compra
4. **Descobrir insights sobre produtos** por meio de busca semântica
5. **Gerar relatórios** com consultas em linguagem natural
6. **Manter a segurança dos dados** com controle de acesso baseado em funções

### Requisitos Técnicos

O servidor MCP deve fornecer:

- **Acesso a dados multi-tenant**, onde gerentes de loja veem apenas os dados de suas lojas
- **Consultas flexíveis** que suportem operações SQL complexas
- **Busca semântica** para descoberta de produtos e recomendações
- **Dados em tempo real** refletindo o estado atual do negócio
- **Autenticação segura** com segurança em nível de linha
- **Arquitetura escalável** suportando múltiplos usuários simultâneos

## 🏗️ Visão Geral da Arquitetura do Servidor MCP

Nosso servidor MCP implementa uma arquitetura em camadas otimizada para integração com banco de dados:

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
- **Registro de Ferramentas**: Definições declarativas de ferramentas com segurança de tipos
- **Contexto de Requisição**: Gerenciamento de identidade do usuário e sessão
- **Tratamento de Erros**: Gerenciamento robusto de erros e registro de logs

#### **2. Camada de Integração com Banco de Dados**
- **Pooling de Conexões**: Gerenciamento eficiente de conexões asyncpg
- **Provedor de Esquema**: Descoberta dinâmica de esquemas de tabelas
- **Executor de Consultas**: Execução segura de SQL com contexto de RLS
- **Gerenciamento de Transações**: Conformidade ACID e tratamento de rollback

#### **3. Camada de Segurança**
- **Segurança em Nível de Linha**: RLS do PostgreSQL para isolamento de dados multi-tenant
- **Identidade do Usuário**: Autenticação e autorização de gerentes de loja
- **Controle de Acesso**: Permissões detalhadas e trilhas de auditoria
- **Validação de Entrada**: Prevenção de injeção de SQL e validação de consultas

#### **4. Camada de Aprimoramento de IA**
- **Busca Semântica**: Embeddings vetoriais para descoberta de produtos
- **Integração com Azure OpenAI**: Geração de embeddings de texto
- **Algoritmos de Similaridade**: Busca de similaridade por cosseno com pgvector
- **Otimização de Busca**: Indexação e ajuste de desempenho

## 🔧 Stack de Tecnologia

### Tecnologias Principais

| **Componente**       | **Tecnologia**            | **Finalidade**                     |
|-----------------------|---------------------------|-------------------------------------|
| **Framework MCP**     | FastMCP (Python)         | Implementação moderna de servidor MCP |
| **Banco de Dados**    | PostgreSQL 17 + pgvector | Dados relacionais com busca vetorial |
| **Serviços de IA**    | Azure OpenAI             | Embeddings de texto e modelos de linguagem |
| **Containerização**   | Docker + Docker Compose  | Ambiente de desenvolvimento         |
| **Plataforma em Nuvem** | Microsoft Azure         | Implantação em produção             |
| **Integração com IDE** | VS Code                 | Chat de IA e fluxo de trabalho de desenvolvimento |

### Ferramentas de Desenvolvimento

| **Ferramenta**        | **Finalidade**           |
|------------------------|--------------------------|
| **asyncpg**           | Driver PostgreSQL de alto desempenho |
| **Pydantic**          | Validação e serialização de dados |
| **Azure SDK**         | Integração com serviços em nuvem |
| **pytest**            | Framework de testes      |
| **Docker**            | Containerização e implantação |

### Stack de Produção

| **Serviço**           | **Recurso Azure**        | **Finalidade**                     |
|------------------------|--------------------------|-------------------------------------|
| **Banco de Dados**    | Azure Database for PostgreSQL | Serviço gerenciado de banco de dados |
| **Container**         | Azure Container Apps     | Hospedagem de containers sem servidor |
| **Serviços de IA**    | Azure AI Foundry         | Modelos OpenAI e endpoints         |
| **Monitoramento**     | Application Insights     | Observabilidade e diagnósticos     |
| **Segurança**         | Azure Key Vault          | Gerenciamento de segredos e configuração |

## 🎬 Cenários de Uso no Mundo Real

Vamos explorar como diferentes usuários interagem com nosso servidor MCP:

### Cenário 1: Revisão de Desempenho do Gerente de Loja

**Usuário**: Sarah, Gerente da Loja de Seattle  
**Objetivo**: Analisar o desempenho de vendas do último trimestre

**Consulta em Linguagem Natural**:
> "Mostre os 10 produtos com maior receita na minha loja no Q4 de 2024"

**O Que Acontece**:
1. O chat de IA no VS Code envia a consulta ao servidor MCP
2. O servidor MCP identifica o contexto da loja de Sarah (Seattle)
3. Políticas de RLS filtram os dados apenas para a loja de Seattle
4. Consulta SQL gerada e executada
5. Resultados formatados e retornados ao chat de IA
6. A IA fornece análise e insights

### Cenário 2: Descoberta de Produtos com Busca Semântica

**Usuário**: Mike, Gerente de Estoque  
**Objetivo**: Encontrar produtos semelhantes a uma solicitação de cliente

**Consulta em Linguagem Natural**:
> "Quais produtos vendemos que são semelhantes a 'conectores elétricos à prova d'água para uso externo'?"

**O Que Acontece**:
1. Consulta processada pela ferramenta de busca semântica
2. Azure OpenAI gera vetor de embedding
3. pgvector realiza busca de similaridade
4. Produtos relacionados classificados por relevância
5. Resultados incluem detalhes e disponibilidade dos produtos
6. A IA sugere alternativas e oportunidades de agrupamento

### Cenário 3: Análise Cruzada de Lojas

**Usuário**: Jennifer, Gerente Regional  
**Objetivo**: Comparar desempenho entre todas as lojas

**Consulta em Linguagem Natural**:
> "Compare as vendas por categoria em todas as lojas nos últimos 6 meses"

**O Que Acontece**:
1. Contexto de RLS configurado para acesso de gerente regional
2. Consulta complexa multi-loja gerada
3. Dados agregados entre localizações de lojas
4. Resultados incluem tendências e comparações
5. A IA identifica insights e recomendações

## 🔒 Mergulho Profundo em Segurança e Multi-Tenancy

Nossa implementação prioriza segurança em nível empresarial:

### Segurança em Nível de Linha (RLS)

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

### Gerenciamento de Identidade do Usuário

Cada conexão MCP inclui:
- **ID do Gerente de Loja**: Identificador único para contexto de RLS
- **Atribuição de Funções**: Permissões e níveis de acesso
- **Gerenciamento de Sessão**: Tokens de autenticação seguros
- **Registro de Auditoria**: Histórico completo de acessos

### Proteção de Dados

Múltiplas camadas de segurança:
- **Criptografia de Conexão**: TLS para todas as conexões de banco de dados
- **Prevenção de Injeção de SQL**: Apenas consultas parametrizadas
- **Validação de Entrada**: Validação abrangente de requisições
- **Tratamento de Erros**: Sem dados sensíveis em mensagens de erro

## 🎯 Principais Conclusões

Após concluir esta introdução, você deve entender:

✅ **Proposta de Valor do MCP**: Como o MCP conecta assistentes de IA a dados do mundo real  
✅ **Contexto de Negócio**: Requisitos e desafios da Zava Retail  
✅ **Visão Geral da Arquitetura**: Componentes principais e suas interações  
✅ **Stack de Tecnologia**: Ferramentas e frameworks utilizados ao longo do caminho  
✅ **Modelo de Segurança**: Acesso a dados multi-tenant e proteção  
✅ **Padrões de Uso**: Cenários de consulta no mundo real e fluxos de trabalho  

## 🚀 Próximos Passos

Pronto para se aprofundar? Continue com:

**[Lab 01: Conceitos de Arquitetura Básica](../01-Architecture/README.md)**

Aprenda sobre padrões de arquitetura de servidores MCP, princípios de design de banco de dados e a implementação técnica detalhada que alimenta nossa solução de análise de varejo.

## 📚 Recursos Adicionais

### Documentação MCP
- [Especificação MCP](https://modelcontextprotocol.io/docs/) - Documentação oficial do protocolo
- [MCP para Iniciantes](https://aka.ms/mcp-for-beginners) - Guia abrangente de aprendizado sobre MCP
- [Documentação do FastMCP](https://github.com/modelcontextprotocol/python-sdk) - Documentação do SDK Python

### Integração com Banco de Dados
- [Documentação do PostgreSQL](https://www.postgresql.org/docs/) - Referência completa do PostgreSQL
- [Guia do pgvector](https://github.com/pgvector/pgvector) - Documentação da extensão vetorial
- [Segurança em Nível de Linha](https://www.postgresql.org/docs/current/ddl-rowsecurity.html) - Guia de RLS do PostgreSQL

### Serviços Azure
- [Documentação do Azure OpenAI](https://docs.microsoft.com/azure/cognitive-services/openai/) - Integração com serviços de IA
- [Azure Database for PostgreSQL](https://docs.microsoft.com/azure/postgresql/) - Serviço gerenciado de banco de dados
- [Azure Container Apps](https://docs.microsoft.com/azure/container-apps/) - Containers sem servidor

---

**Aviso**: Este é um exercício de aprendizado usando dados fictícios de varejo. Sempre siga as políticas de governança e segurança de dados da sua organização ao implementar soluções semelhantes em ambientes de produção.

---

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, é importante estar ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte oficial. Para informações críticas, recomenda-se a tradução profissional realizada por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.