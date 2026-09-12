# Introducción a la Integración de Bases de Datos MCP

> [!NOTE]
> Los diagramas o código en esta ruta de aprendizaje que usan HTTP/SSE u opciones de inicialización
> reflejan las dependencias MCP `2025-11-25` del ejemplo. Para nuevas
> implementaciones, utilice solicitudes sin estado `2026-07-28` y HTTP transmitible.

## 🎯 Lo que cubre este laboratorio

Este laboratorio introductorio ofrece una visión integral sobre cómo construir servidores Model Context Protocol (MCP) con integración de bases de datos. Comprenderás el caso de negocio, la arquitectura técnica y aplicaciones del mundo real a través del caso de análisis de Zava Retail en https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail.

## Resumen

**Model Context Protocol (MCP)** permite a los asistentes de IA acceder e interactuar de forma segura con fuentes de datos externas en tiempo real. Combinado con la integración de bases de datos, MCP desbloquea potentes capacidades para aplicaciones de IA basadas en datos.

Esta ruta de aprendizaje te enseña a construir servidores MCP listos para producción que conectan asistentes de IA con datos de ventas minoristas a través de PostgreSQL, implementando patrones empresariales como Seguridad a Nivel de Fila, búsqueda semántica y acceso multiinquilino a datos.

## Objetivos de aprendizaje

Al finalizar este laboratorio, podrás:

- **Definir** el Model Context Protocol y sus beneficios fundamentales para la integración de bases de datos
- **Identificar** componentes clave de la arquitectura de un servidor MCP con bases de datos
- **Comprender** el caso de uso de Zava Retail y sus requisitos comerciales
- **Reconocer** patrones empresariales para acceso seguro y escalable a bases de datos
- **Enumerar** las herramientas y tecnologías usadas a lo largo de esta ruta de aprendizaje

## 🧭 El desafío: IA y datos del mundo real

### Limitaciones tradicionales de IA

Los asistentes de IA modernos son increíblemente potentes pero enfrentan limitaciones significativas al trabajar con datos comerciales del mundo real:

| **Desafío** | **Descripción** | **Impacto en el negocio** |
|---------------|-----------------|-------------------|
| **Conocimiento estático** | Los modelos de IA entrenados con conjuntos de datos fijos no pueden acceder a datos actuales del negocio | Perspectivas desactualizadas, oportunidades perdidas |
| **Silos de datos** | Información encerrada en bases de datos, APIs y sistemas inaccesibles para IA | Análisis incompleto, flujos de trabajo fragmentados |
| **Restricciones de seguridad** | Acceso directo a la base de datos genera preocupaciones de seguridad y cumplimiento | Despliegue limitado, preparación manual de datos |
| **Consultas complejas** | Los usuarios comerciales necesitan conocimientos técnicos para extraer insights de datos | Adopción reducida, procesos ineficientes |

### La solución MCP

Model Context Protocol aborda estos desafíos ofreciendo:

- **Acceso a datos en tiempo real**: los asistentes de IA consultan bases de datos y APIs en vivo
- **Integración segura**: acceso controlado con autenticación y permisos
- **Interfaz en lenguaje natural**: los usuarios comerciales hacen preguntas en inglés sencillo
- **Protocolo estandarizado**: compatible con diferentes plataformas y herramientas de IA

## 🏪 Conozca Zava Retail: Nuestro caso de estudio de aprendizaje https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail

A lo largo de esta ruta de aprendizaje, construiremos un servidor MCP para **Zava Retail**, una cadena ficticia de tiendas de bricolaje con múltiples ubicaciones. Este escenario realista demuestra una implementación MCP de nivel empresarial.

### Contexto comercial

**Zava Retail** opera:
- **8 tiendas físicas** en el estado de Washington (Seattle, Bellevue, Tacoma, Spokane, Everett, Redmond, Kirkland)
- **1 tienda en línea** para ventas de comercio electrónico
- **Catálogo diverso de productos** que incluye herramientas, ferretería, suministros de jardinería y materiales de construcción
- **Gestión multinivel** con gerentes de tienda, gerentes regionales y ejecutivos

### Requisitos comerciales

Los gerentes de tienda y ejecutivos necesitan análisis impulsados por IA para:

1. **Analizar el rendimiento de ventas** entre tiendas y períodos de tiempo
2. **Rastrear niveles de inventario** e identificar necesidades de reposición
3. **Comprender el comportamiento del cliente** y patrones de compra
4. **Descubrir insights de productos** mediante búsqueda semántica
5. **Generar informes** con consultas en lenguaje natural
6. **Mantener la seguridad de datos** con control de acceso basado en roles

### Requisitos técnicos

El servidor MCP debe proporcionar:

- **Acceso a datos multiinquilino** donde los gerentes de tienda sólo ven datos de su tienda
- **Consultas flexibles** que soportan operaciones SQL complejas
- **Búsqueda semántica** para descubrimiento de productos y recomendaciones
- **Datos en tiempo real** que reflejen el estado actual del negocio
- **Autenticación segura** con seguridad a nivel de fila
- **Arquitectura escalable** que soporte múltiples usuarios concurrentes

## 🏗️ Visión general de arquitectura del servidor MCP

Nuestro servidor MCP implementa una arquitectura en capas optimizada para integración de bases de datos:

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

### Componentes clave

#### **1. Capa del servidor MCP**
- **Framework FastMCP**: Implementación moderna de servidor MCP en Python
- **Registro de herramientas**: Definiciones declarativas con seguridad de tipos
- **Contexto de solicitud**: Gestión de identidad de usuario y sesión
- **Manejo de errores**: Gestión robusta de errores y registros

#### **2. Capa de integración de base de datos**
- **Pool de conexiones**: Gestión eficiente de conexiones asyncpg
- **Proveedor de esquemas**: Descubrimiento dinámico de esquemas de tablas
- **Ejecutor de consultas**: Ejecución segura de SQL con contexto RLS
- **Gestión de transacciones**: Cumplimiento ACID y manejo de rollback

#### **3. Capa de seguridad**
- **Seguridad a Nivel de Fila**: RLS de PostgreSQL para aislamiento de datos multiinquilino
- **Identidad de usuario**: Autenticación y autorización de gerentes de tienda
- **Control de acceso**: Permisos detallados y auditorías
- **Validación de entrada**: Prevención de inyección SQL y validación de consultas

#### **4. Capa de mejora AI**
- **Búsqueda semántica**: Embeddings vectoriales para descubrimiento de productos
- **Integración Azure OpenAI**: Generación de incrustaciones de texto
- **Algoritmos de similitud**: Búsqueda por similitud coseno con pgvector
- **Optimización de búsqueda**: Indexación y ajuste de rendimiento

## 🔧 Pila tecnológica

### Tecnologías principales

| **Componente** | **Tecnología** | **Propósito** |
|---------------|----------------|-------------|
| **Framework MCP** | FastMCP (Python) | Implementación moderna de servidor MCP |
| **Base de datos** | PostgreSQL 17 + pgvector | Datos relacionales con búsqueda vectorial |
| **Servicios IA** | Azure OpenAI | Embeddings de texto y modelos de lenguaje |
| **Contenerización** | Docker + Docker Compose | Entorno de desarrollo |
| **Plataforma Cloud** | Microsoft Azure | Despliegue en producción |
| **Integración IDE** | VS Code | Chat IA y flujo de desarrollo |

### Herramientas de desarrollo

| **Herramienta** | **Propósito** |
|----------|-------------|
| **asyncpg** | Driver PostgreSQL de alto rendimiento |
| **Pydantic** | Validación y serialización de datos |
| **Azure SDK** | Integración con servicios cloud |
| **pytest** | Framework de pruebas |
| **Docker** | Contenerización y despliegue |

### Pila de producción

| **Servicio** | **Recurso Azure** | **Propósito** |
|-------------|-------------------|-------------|
| **Base de datos** | Azure Database for PostgreSQL | Servicio de base de datos gestionado |
| **Contenedor** | Azure Container Apps | Hosting serverless de contenedores |
| **Servicios IA** | Microsoft Foundry | Modelos y endpoints OpenAI |
| **Monitoreo** | Application Insights | Observabilidad y diagnóstico |
| **Seguridad** | Azure Key Vault | Gestión de secretos y configuración |

## 🎬 Escenarios de uso en el mundo real

Exploremos cómo diferentes usuarios interactúan con nuestro servidor MCP:

### Escenario 1: Revisión de desempeño del gerente de tienda

**Usuario**: Sarah, gerente de tienda en Seattle  
**Objetivo**: Analizar el desempeño de ventas del último trimestre

**Consulta en lenguaje natural**:
> "Muéstrame los 10 productos principales por ingresos para mi tienda en el Q4 2024"

**Qué ocurre**:
1. VS Code AI Chat envía la consulta al servidor MCP
2. El servidor MCP identifica el contexto de la tienda de Sarah (Seattle)
3. Las políticas RLS filtran datos sólo para la tienda de Seattle
4. Se genera y ejecuta la consulta SQL
5. Resultados formateados y enviados a AI Chat
6. La IA proporciona análisis y conclusiones

### Escenario 2: Descubrimiento de productos con búsqueda semántica

**Usuario**: Mike, gerente de inventario  
**Objetivo**: Encontrar productos similares a la solicitud de un cliente

**Consulta en lenguaje natural**:
> "¿Qué productos vendemos que sean similares a 'conectores eléctricos impermeables para uso exterior'?"

**Qué ocurre**:
1. La consulta es procesada por la herramienta de búsqueda semántica
2. Azure OpenAI genera el vector embedding
3. pgvector realiza búsqueda por similitud
4. Productos relacionados clasificados por relevancia
5. Resultados incluyen detalles y disponibilidad de productos
6. La IA sugiere alternativas y oportunidades de paquetes

### Escenario 3: Análisis entre tiendas

**Usuario**: Jennifer, gerente regional  
**Objetivo**: Comparar desempeño entre todas las tiendas

**Consulta en lenguaje natural**:
> "Compara ventas por categoría para todas las tiendas en los últimos 6 meses"

**Qué ocurre**:
1. Se establece contexto RLS para acceso de gerente regional
2. Se genera consulta compleja multi-tienda
3. Datos agregados entre ubicaciones de tiendas
4. Resultados incluyen tendencias y comparaciones
5. La IA identifica insights y recomendaciones

## 🔒 Profundizando en seguridad y multiinquilino

Nuestra implementación prioriza seguridad de nivel empresarial:

### Seguridad a nivel de fila (RLS)

PostgreSQL RLS garantiza aislamiento de datos:

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

### Gestión de identidad de usuario

Cada conexión MCP incluye:
- **ID de gerente de tienda**: Identificador único para contexto RLS
- **Asignación de roles**: Permisos y niveles de acceso
- **Gestión de sesión**: Tokens de autenticación seguros
- **Registro de auditoría**: Historial completo de accesos

### Protección de datos

Múltiples capas de seguridad:
- **Encriptación de conexión**: TLS para todas las conexiones a la base de datos
- **Prevención de inyección SQL**: Sólo consultas parametrizadas
- **Validación de entradas**: Validación exhaustiva de solicitudes
- **Manejo de errores**: Sin datos sensibles en mensajes de error

## 🎯 Conclusiones clave

Después de completar esta introducción, deberías comprender:

✅ **Propuesta de valor MCP**: Cómo MCP conecta asistentes de IA y datos del mundo real  
✅ **Contexto comercial**: Requisitos y retos de Zava Retail  
✅ **Resumen de arquitectura**: Componentes clave y sus interacciones  
✅ **Pila tecnológica**: Herramientas y frameworks usados  
✅ **Modelo de seguridad**: Acceso y protección multiinquilino  
✅ **Patrones de uso**: Escenarios reales de consultas y flujos de trabajo  

## 🚀 ¿Qué sigue?

¿Listo para profundizar? Continúa con:

**[Laboratorio 01: Conceptos básicos de arquitectura](../01-Architecture/README.md)**

Aprende sobre patrones de arquitectura de servidores MCP, principios de diseño de bases de datos e implementación técnica detallada que impulsa nuestra solución de análisis minorista.

## 📚 Recursos adicionales

### Documentación MCP
- [Especificación MCP](https://modelcontextprotocol.io/docs/) - Documentación oficial del protocolo
- [MCP para principiantes](https://aka.ms/mcp-for-beginners) - Guía completa de aprendizaje MCP
- [Documentación FastMCP](https://github.com/modelcontextprotocol/python-sdk) - Documentación del SDK de Python

### Integración de bases de datos
- [Documentación PostgreSQL](https://www.postgresql.org/docs/) - Referencia completa de PostgreSQL
- [Guía de pgvector](https://github.com/pgvector/pgvector) - Documentación de la extensión vectorial
- [Seguridad a nivel de fila](https://www.postgresql.org/docs/current/ddl-rowsecurity.html) - Guía RLS de PostgreSQL

### Servicios Azure
- [Documentación Azure OpenAI](https://docs.microsoft.com/azure/cognitive-services/openai/) - Integración de servicios IA
- [Azure Database para PostgreSQL](https://docs.microsoft.com/azure/postgresql/) - Servicio gestionado de base de datos
- [Azure Container Apps](https://docs.microsoft.com/azure/container-apps/) - Contenedores serverless

---

**Aviso legal**: Este es un ejercicio de aprendizaje que usa datos minoristas ficticios. Siempre siga las políticas de gobierno y seguridad de datos de su organización al implementar soluciones similares en entornos de producción.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Descargo de responsabilidad**:
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional humana. No somos responsables de cualquier malentendido o interpretación errónea que surja del uso de esta traducción.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->