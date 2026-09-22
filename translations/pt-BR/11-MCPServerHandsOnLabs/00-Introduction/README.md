# Introdução à Integração de Banco de Dados com MCP

> [!NOTE]
> Diagramas ou códigos neste caminho de aprendizado que usam HTTP/SSE ou opções de inicialização refletem as dependências MCP `2025-11-25` do exemplo. Para novas implementações, use requisições sem estado `2026-07-28` e HTTP Streamable.
> 
> 

## 🎯 O que este laboratório cobre

Este laboratório introdutório fornece uma visão abrangente sobre a construção de servidores Model Context Protocol (MCP) com integração a banco de dados. Você entenderá o caso de negócio, a arquitetura técnica e aplicações no mundo real por meio do estudo de caso de análise Zava Retail em https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail.

## Visão Geral

**Model Context Protocol (MCP)** permite que assistentes de IA acessem e interajam com fontes de dados externas com segurança em tempo real. Quando combinado com integração a banco de dados, o MCP desbloqueia capacidades poderosas para aplicações de IA orientadas a dados.

Este caminho de aprendizado ensina a construir servidores MCP prontos para produção que conectam assistentes de IA a dados de vendas no varejo por meio do PostgreSQL, implementando padrões corporativos como Row Level Security, busca semântica e acesso multi-inquilino a dados.

## Objetivos de Aprendizagem

Ao final deste laboratório, você será capaz de:

- **Definir** o Model Context Protocol e seus benefícios centrais para integração com banco de dados
- **Identificar** os componentes-chave da arquitetura de um servidor MCP com bancos de dados
- **Compreender** o caso de uso Zava Retail e seus requisitos de negócio
- **Reconhecer** padrões corporativos para acesso seguro e escalável a bancos de dados
- **Listar** as ferramentas e tecnologias usadas ao longo deste caminho de aprendizado

## 🧭 O Desafio: IA encontra dados do mundo real

### Limitações tradicionais da IA

Assistentes modernos de IA são extremamente poderosos, mas enfrentam limitações significativas ao trabalhar com dados reais de negócios:

| **Desafio** | **Descrição** | **Impacto no Negócio** |
|---------------|-----------------|-------------------|
| **Conhecimento Estático** | Modelos de IA treinados em datasets fixos não acessam dados atuais de negócio | Insights desatualizados, oportunidades perdidas |
| **Silos de Dados** | Informação trancada em bancos de dados, APIs e sistemas inacessíveis à IA | Análise incompleta, fluxos de trabalho fragmentados |
| **Restrições de Segurança** | Acesso direto ao banco de dados levanta preocupações de segurança e conformidade | Implantação limitada, preparação manual de dados |
| **Consultas Complexas** | Usuários de negócio precisam de conhecimento técnico para extrair dados | Adoção reduzida, processos ineficientes |

### A solução MCP

O Model Context Protocol resolve esses desafios ao fornecer:

- **Acesso a Dados em Tempo Real**: Assistentes de IA consultam bases de dados e APIs ao vivo
- **Integração Segura**: Acesso controlado com autenticação e permissões
- **Interface em Linguagem Natural**: Usuários de negócio fazem perguntas em inglês simples
- **Protocolo Padronizado**: Funciona em diferentes plataformas e ferramentas de IA

## 🏪 Conheça a Zava Retail: Nosso Estudo de Caso https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail

Ao longo deste caminho de aprendizado, construiremos um servidor MCP para a **Zava Retail**, uma cadeia fictícia de varejo de bricolagem com várias lojas físicas. Este cenário realista demonstra implementação MCP em nível empresarial.

### Contexto de Negócio

**Zava Retail** opera:
- **8 lojas físicas** no estado de Washington (Seattle, Bellevue, Tacoma, Spokane, Everett, Redmond, Kirkland)
- **1 loja online** para vendas de e-commerce
- **Catálogo diversificado de produtos** incluindo ferramentas, ferragens, suprimentos para jardim e materiais de construção
- **Gestão em múltiplos níveis** com gerentes de loja, gerentes regionais e executivos

### Requisitos de Negócio

Gerentes de loja e executivos precisam de análises com suporte de IA para:

1. **Analisar desempenho de vendas** nas lojas e períodos
2. **Acompanhar níveis de estoque** e identificar necessidades de reposição
3. **Entender comportamento do cliente** e padrões de compra
4. **Descobrir insights de produtos** por meio de busca semântica
5. **Gerar relatórios** com consultas em linguagem natural
6. **Manter segurança de dados** com controle de acesso baseado em função

### Requisitos Técnicos

O servidor MCP deve oferecer:

- **Acesso a dados multi-inquilino**, onde gerentes veem apenas dados da sua loja
- **Consultas flexíveis** suportando operações SQL complexas
- **Busca semântica** para descoberta e recomendações de produtos
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

### Componentes-chave

#### **1. Camada do Servidor MCP**
- **FastMCP Framework**: Implementação moderna em Python para servidor MCP
- **Registro de Ferramentas**: Definições declarativas com segurança de tipos
- **Contexto de Requisição**: Identidade do usuário e gerenciamento de sessão
- **Tratamento de Erros**: Gestão robusta de erros e logs

#### **2. Camada de Integração com Banco de Dados**
- **Pool de Conexões**: Gerenciamento eficiente com asyncpg
- **Provedor de Esquema**: Descoberta dinâmica do esquema das tabelas
- **Executor de Consultas**: Execução segura de SQL com contexto RLS
- **Gerenciamento de Transações**: Conformidade ACID e controle de rollback

#### **3. Camada de Segurança**
- **Row Level Security**: RLS do PostgreSQL para isolamento multi-inquilino
- **Identidade do Usuário**: Autenticação e autorização do gerente de loja
- **Controle de Acesso**: Permissões e auditoria detalhadas
- **Validação de Entrada**: Prevenção de injeção SQL e validação de consultas

#### **4. Camada de Aprimoramento de IA**
- **Busca Semântica**: Embeddings vetoriais para descoberta de produtos
- **Integração com Azure OpenAI**: Geração de embeddings de texto
- **Algoritmos de Similaridade**: Busca por similaridade com pgvector
- **Otimização de Busca**: Indexação e ajuste de desempenho

## 🔧 Pilha Tecnológica

### Tecnologias Principais

| **Componente** | **Tecnologia** | **Finalidade** |
|---------------|----------------|-------------|
| **Framework MCP** | FastMCP (Python) | Implementação moderna de servidor MCP |
| **Banco de Dados** | PostgreSQL 17 + pgvector | Dados relacionais com busca vetorial |
| **Serviços de IA** | Azure OpenAI | Embeddings de texto e modelos de linguagem |
| **Containerização** | Docker + Docker Compose | Ambiente de desenvolvimento |
| **Plataforma em Nuvem** | Microsoft Azure | Implantação em produção |
| **Integração com IDE** | VS Code | Chat de IA e fluxo de trabalho de desenvolvimento |

### Ferramentas de Desenvolvimento

| **Ferramenta** | **Finalidade** |
|----------|-------------|
| **asyncpg** | Driver PostgreSQL de alto desempenho |
| **Pydantic** | Validação e serialização de dados |
| **Azure SDK** | Integração com serviços em nuvem |
| **pytest** | Framework de testes |
| **Docker** | Containerização e implantação |

### Pilha de Produção

| **Serviço** | **Recurso Azure** | **Finalidade** |
|-------------|-------------------|-------------|
| **Banco de Dados** | Azure Database for PostgreSQL | Serviço gerenciado de banco de dados |
| **Container** | Azure Container Apps | Hospedagem serverless de containers |
| **Serviços de IA** | Microsoft Foundry | Modelos e endpoints OpenAI |
| **Monitoramento** | Application Insights | Observabilidade e diagnóstico |
| **Segurança** | Azure Key Vault | Gerenciamento de segredos e configuração |

## 🎬 Cenários de Uso no Mundo Real

Vamos explorar como diferentes usuários interagem com nosso servidor MCP:

### Cenário 1: Revisão de Desempenho do Gerente de Loja

**Usuário**: Sarah, Gerente da Loja de Seattle  
**Objetivo**: Analisar desempenho de vendas do último trimestre

**Consulta em Linguagem Natural**:
> "Mostre os 10 produtos com maior receita para minha loja no quarto trimestre de 2024"

**O que acontece**:
1. O chat de IA do VS Code envia consulta para o servidor MCP
2. O servidor MCP identifica o contexto da loja de Sarah (Seattle)
3. Políticas RLS filtram dados para apenas a loja de Seattle
4. Consulta SQL é gerada e executada
5. Resultados são formatados e retornados ao chat de IA
6. IA fornece análise e insights

### Cenário 2: Descoberta de Produtos com Busca Semântica

**Usuário**: Mike, Gerente de Estoque  
**Objetivo**: Encontrar produtos similares a uma solicitação do cliente

**Consulta em Linguagem Natural**:
> "Quais produtos vendemos que são semelhantes a 'conectores elétricos à prova d'água para uso externo'?"

**O que acontece**:
1. Consulta é processada pela ferramenta de busca semântica
2. Azure OpenAI gera vetor de embedding
3. pgvector executa busca por similaridade
4. Produtos relacionados são ranqueados por relevância
5. Resultados incluem detalhes e disponibilidade dos produtos
6. IA sugere alternativas e oportunidades de bundling

### Cenário 3: Análise Cruzada entre Lojas

**Usuário**: Jennifer, Gerente Regional  
**Objetivo**: Comparar desempenho entre todas as lojas

**Consulta em Linguagem Natural**:
> "Compare vendas por categoria para todas as lojas nos últimos 6 meses"

**O que acontece**:
1. Contexto RLS configurado para acesso do gerente regional
2. Consulta complexa para múltiplas lojas é gerada
3. Dados são agregados entre as localizações das lojas
4. Resultados incluem tendências e comparações
5. IA identifica insights e recomendações

## 🔒 Segurança e Multi-inquilinidade em Detalhes

Nossa implementação prioriza segurança em nível empresarial:

### Segurança em Nível de Linha (RLS)

O PostgreSQL RLS assegura isolamento de dados:

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
- **ID do Gerente de Loja**: Identificador único para contexto RLS
- **Atribuição de Papel**: Permissões e níveis de acesso
- **Gerenciamento de Sessão**: Tokens de autenticação seguros
- **Registro de Auditoria**: Histórico completo de acessos

### Proteção de Dados

Múltiplas camadas de segurança:
- **Criptografia de Conexão**: TLS para todas as conexões ao banco de dados
- **Prevenção de Injeção SQL**: Consultas parametrizadas apenas
- **Validação de Entrada**: Validação abrangente de requisições
- **Tratamento de Erros**: Sem dados sensíveis em mensagens de erro

## 🎯 Principais conclusões

Após concluir esta introdução, você deverá entender:

✅ **Proposta de Valor do MCP**: Como o MCP conecta assistentes de IA e dados do mundo real  
✅ **Contexto de Negócio**: Requisitos e desafios da Zava Retail  
✅ **Visão Geral da Arquitetura**: Componentes-chave e suas interações  
✅ **Pilha Tecnológica**: Ferramentas e frameworks usados ao longo do caminho  
✅ **Modelo de Segurança**: Acesso multi-inquilino e proteção de dados  
✅ **Padrões de Uso**: Cenários e fluxos de trabalho reais de consulta  

## 🚀 Próximos passos

Pronto para aprofundar? Continue com:

**[Laboratório 01: Conceitos de Arquitetura Principal](../01-Architecture/README.md)**

Aprenda sobre padrões de arquitetura de servidor MCP, princípios de design de banco de dados e a implementação técnica detalhada que sustenta nossa solução de análise no varejo.

## 📚 Recursos Adicionais

### Documentação MCP
- [Especificação MCP](https://modelcontextprotocol.io/docs/) - Documentação oficial do protocolo
- [MCP para Iniciantes](https://aka.ms/mcp-for-beginners) - Guia completo de aprendizado MCP
- [Documentação FastMCP](https://github.com/modelcontextprotocol/python-sdk) - Documentação do SDK Python

### Integração com Banco de Dados
- [Documentação PostgreSQL](https://www.postgresql.org/docs/) - Referência completa PostgreSQL
- [Guia pgvector](https://github.com/pgvector/pgvector) - Documentação da extensão vetorial
- [Segurança em Nível de Linha](https://www.postgresql.org/docs/current/ddl-rowsecurity.html) - Guia do RLS PostgreSQL

### Serviços Azure
- [Documentação Azure OpenAI](https://docs.microsoft.com/azure/cognitive-services/openai/) - Integração de serviços de IA
- [Azure Database for PostgreSQL](https://docs.microsoft.com/azure/postgresql/) - Serviço gerenciado de banco de dados
- [Azure Container Apps](https://docs.microsoft.com/azure/container-apps/) - Containers serverless

---

**Aviso Legal**: Este é um exercício de aprendizado utilizando dados fictícios de varejo. Sempre siga as políticas de governança e segurança de dados da sua organização ao implementar soluções similares em ambientes de produção.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido usando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, por favor, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->