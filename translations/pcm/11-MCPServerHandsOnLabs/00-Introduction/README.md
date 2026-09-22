# Introduction to MCP Database Integration

> [!NOTE]
> Diagrams or code wey dey dis learning path wey dey use HTTP/SSE or initialization
> options na di sample MCP `2025-11-25` dependencies. For new
> implementations, use `2026-07-28` stateless requests and Streamable HTTP.

## 🎯 Wetin Dis Lab Dey Cover

Dis introduction lab go give you full overview on how to build Model Context Protocol (MCP) servers wey get database integration. You go understand di business case, technical architecture, plus real-world applications through di Zava Retail analytics use case at https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail.

## Overview

**Model Context Protocol (MCP)** dey enable AI assistants access data sources outside securely and interact with dem for real-time. When e join wit database integration, MCP dey unlock strong capabilities for AI applications wey dey depend on data.

Dis learning path go teach you how to build production-ready MCP servers wey dey connect AI assistants to retail sales data through PostgreSQL, implement enterprise patterns like Row Level Security, semantic search, and multi-tenant data access.

## Learning Objectives

By di end of dis lab, you go fit:

- **Define** Model Context Protocol and di core benefits for database integration
- **Identify** key components of MCP server architecture with databases
- **Understand** di Zava Retail use case and im business requirements
- **Recognize** enterprise patterns for secure, scalable database access
- **List** di tools and technologies wey dem use for dis whole learning path

## 🧭 Di Challenge: AI Meets Real-World Data

### Traditional AI Limitations

Modern AI assistants powerful no be small but dem get some serious yawa wen dem dey work with real-world business data:

| **Challenge** | **Description** | **Business Impact** |
|---------------|-----------------|-------------------|
| **Static Knowledge** | AI models wey dem train on fixed datasets no fit access current business data | Outdated insights, missed opportunities |
| **Data Silos** | Information wey lockdown for databases, APIs, and systems wey AI no fit reach | Incomplete analysis, fragmented workflows |
| **Security Constraints** | Direct database access fit cause security and compliance palava | Limited deployment, manual data preparation |
| **Complex Queries** | Business people need technical know-how to get data insights | Reduced adoption, inefficient processes |

### Di MCP Solution

Model Context Protocol dey tackle these wahala by giving:

- **Real-time Data Access**: AI assistants dey query live databases and APIs
- **Secure Integration**: Controlled access with authentication and permissions
- **Natural Language Interface**: Business people fit ask questions for plain English
- **Standardized Protocol**: E dey work across different AI platforms and tools

## 🏪 Meet Zava Retail: Our Learning Case Study https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail

Inside dis learning path, we go build MCP server for **Zava Retail**, wey be fictional DIY retail chain wey get plenty store locations. Dis real-like scenario dey show enterprise-level MCP implementation.

### Business Context

**Zava Retail** dey operate:
- **8 physical stores** for Washington state (Seattle, Bellevue, Tacoma, Spokane, Everett, Redmond, Kirkland)
- **1 online store** for e-commerce sales
- **Plenty product catalog** wey get tools, hardware, garden supplies, and building materials
- **Multi-level management** with store managers, regional managers, and executives

### Business Requirements

Store managers and executives need AI-powered analytics to:

1. **Analyze sales performance** across stores and time periods
2. **Track inventory levels** and see wetin dem need to restock
3. **Understand customer behavior** and how dem dey buy tins
4. **Discover product insights** using semantic search
5. **Generate reports** with natural language queries
6. **Keep data secure** with role-based access control

### Technical Requirements

Di MCP server must provide:

- **Multi-tenant data access** so store managers go only see their own store data
- **Flexible querying** wey support complex SQL operations
- **Semantic search** for product discovery and recommendations
- **Real-time data** wey show current business state
- **Secure authentication** using row-level security
- **Scalable architecture** wey fit handle many users at the same time

## 🏗️ MCP Server Architecture Overview

Our MCP server get layers for architecture wey dem optimize for database integration:

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

### Key Components

#### **1. MCP Server Layer**
- **FastMCP Framework**: Modern Python MCP server implementation
- **Tool Registration**: Declarative tool definitions wey dey type safe
- **Request Context**: User identity and session management
- **Error Handling**: Strong error management and logging

#### **2. Database Integration Layer**
- **Connection Pooling**: Efficient asyncpg connection management
- **Schema Provider**: Dynamic table schema discovery
- **Query Executor**: Secure SQL execution with RLS context
- **Transaction Management**: ACID compliance and rollback handling

#### **3. Security Layer**
- **Row Level Security**: PostgreSQL RLS for multi-tenant data isolation
- **User Identity**: Store manager authentication and authorization
- **Access Control**: Fine-grained permissions and audit trails
- **Input Validation**: SQL injection prevention and query validation

#### **4. AI Enhancement Layer**
- **Semantic Search**: Vector embeddings for product discovery
- **Azure OpenAI Integration**: Text embedding generation
- **Similarity Algorithms**: pgvector cosine similarity search
- **Search Optimization**: Indexing and performance tuning

## 🔧 Technology Stack

### Core Technologies

| **Component** | **Technology** | **Purpose** |
|---------------|----------------|-------------|
| **MCP Framework** | FastMCP (Python) | Modern MCP server implementation |
| **Database** | PostgreSQL 17 + pgvector | Relational data with vector search |
| **AI Services** | Azure OpenAI | Text embeddings and language models |
| **Containerization** | Docker + Docker Compose | Development environment |
| **Cloud Platform** | Microsoft Azure | Production deployment |
| **IDE Integration** | VS Code | AI Chat and development workflow |

### Development Tools

| **Tool** | **Purpose** |
|----------|-------------|
| **asyncpg** | High-performance PostgreSQL driver |
| **Pydantic** | Data validation and serialization |
| **Azure SDK** | Cloud service integration |
| **pytest** | Testing framework |
| **Docker** | Containerization and deployment |

### Production Stack

| **Service** | **Azure Resource** | **Purpose** |
|-------------|-------------------|-------------|
| **Database** | Azure Database for PostgreSQL | Managed database service |
| **Container** | Azure Container Apps | Serverless container hosting |
| **AI Services** | Microsoft Foundry | OpenAI models and endpoints |
| **Monitoring** | Application Insights | Observability and diagnostics |
| **Security** | Azure Key Vault | Secrets and configuration management |

## 🎬 Real-World Usage Scenarios

Make we check how different users dey interact with our MCP server:

### Scenario 1: Store Manager Performance Review

**User**: Sarah, Seattle Store Manager  
**Goal**: Analyze sales performance for last quarter

**Natural Language Query**:
> "Show me the top 10 products by revenue for my store in Q4 2024"

**Wetin Go Happen**:
1. VS Code AI Chat go send query go MCP server
2. MCP server go identify Sarah store context (Seattle)
3. RLS policies go filter data make e be only for Seattle store
4. SQL query go generate and execute
5. Results go format and return to AI Chat
6. AI go provide analysis and insights

### Scenario 2: Product Discovery with Semantic Search

**User**: Mike, Inventory Manager  
**Goal**: Find products wey similar to wetin customer ask

**Natural Language Query**:
> "What products do we sell that are similar to 'waterproof electrical connectors for outdoor use'?"

**Wetin Go Happen**:
1. Query go pass through semantic search tool
2. Azure OpenAI go generate embedding vector
3. pgvector go perform similarity search
4. Related products go arrange by how e relate
5. Results go contain product details and availability
6. AI go suggest alternatives and bundling chances

### Scenario 3: Cross-Store Analytics

**User**: Jennifer, Regional Manager  
**Goal**: Compare performance for all stores

**Natural Language Query**:
> "Compare sales by category for all stores in the last 6 months"

**Wetin Go Happen**:
1. RLS context go set for regional manager access
2. Complex multi-store query go generate
3. Data go aggregate across store locations
4. Results go show trends and comparisons
5. AI go identify insights and give recommendations

## 🔒 Security and Multi-Tenancy Deep Dive

Our implementation dey focus on enterprise-grade security:

### Row Level Security (RLS)

PostgreSQL RLS dey ensure say data separate well:

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

### User Identity Management

Every MCP connection get:
- **Store Manager ID**: Unique ID for RLS context
- **Role Assignment**: Permissions and access levels
- **Session Management**: Secure authentication tokens
- **Audit Logging**: Complete access record

### Data Protection

Plenty layers of security:
- **Connection Encryption**: TLS for all database connections
- **SQL Injection Prevention**: Parameterized queries only
- **Input Validation**: Full request validation
- **Error Handling**: No sensitive data dey error messages

## 🎯 Key Takeaways

After you finish dis introduction, you go understand:

✅ **MCP Value Proposition**: How MCP dey connect AI assistants and real-world data  
✅ **Business Context**: Zava Retail’s requirements and challenges  
✅ **Architecture Overview**: Key components and how dem take work together  
✅ **Technology Stack**: Tools and frameworks wey dem use throughout  
✅ **Security Model**: Multi-tenant data access and protection  
✅ **Usage Patterns**: Real-world query scenarios and workflows  

## 🚀 Wetin Next

You ready to go deeper? Continue with:

**[Lab 01: Core Architecture Concepts](../01-Architecture/README.md)**

Learn about MCP server architecture patterns, database design principles, and di detailed technical implementation wey power our retail analytics solution.

## 📚 Additional Resources

### MCP Documentation
- [MCP Specification](https://modelcontextprotocol.io/docs/) - Official protocol documentation
- [MCP for Beginners](https://aka.ms/mcp-for-beginners) - Comprehensive MCP learning guide
- [FastMCP Documentation](https://github.com/modelcontextprotocol/python-sdk) - Python SDK documentation

### Database Integration
- [PostgreSQL Documentation](https://www.postgresql.org/docs/) - Complete PostgreSQL reference
- [pgvector Guide](https://github.com/pgvector/pgvector) - Vector extension documentation
- [Row Level Security](https://www.postgresql.org/docs/current/ddl-rowsecurity.html) - PostgreSQL RLS guide

### Azure Services
- [Azure OpenAI Documentation](https://docs.microsoft.com/azure/cognitive-services/openai/) - AI service integration
- [Azure Database for PostgreSQL](https://docs.microsoft.com/azure/postgresql/) - Managed database service
- [Azure Container Apps](https://docs.microsoft.com/azure/container-apps/) - Serverless containers

---

**Disclaimer**: Dis na learning exercise wey dey use fictional retail data. Always follow your organization data governance and security policies wen you dey implement similar solutions for production environments.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dis document don translate wit AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). Even tho we dey try make am correct, abeg make you know say automated translation fit get errors or mistakes. Di original document for dia own language na im be di correct source. For important info, make person wey sabi human translation do am. We no go responsible for any misunderstanding or wrong understanding wey fit happen because of dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->