# Introducción a la Integración de Bases de Datos con MCP

## 🎯 Qué Cubre Este Laboratorio

Este laboratorio introductorio ofrece una visión completa sobre cómo construir servidores del Protocolo de Contexto de Modelo (MCP) con integración de bases de datos. Comprenderás el caso de negocio, la arquitectura técnica y las aplicaciones reales a través del caso de uso de análisis de Zava Retail en https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail.

## Resumen

El **Protocolo de Contexto de Modelo (MCP)** permite que los asistentes de IA accedan e interactúen de manera segura con fuentes de datos externas en tiempo real. Cuando se combina con la integración de bases de datos, MCP desbloquea capacidades poderosas para aplicaciones de IA basadas en datos.

Este camino de aprendizaje te enseña a construir servidores MCP listos para producción que conectan asistentes de IA con datos de ventas minoristas a través de PostgreSQL, implementando patrones empresariales como Seguridad a Nivel de Fila, búsqueda semántica y acceso a datos multiusuario.

## Objetivos de Aprendizaje

Al finalizar este laboratorio, serás capaz de:

- **Definir** el Protocolo de Contexto de Modelo y sus beneficios principales para la integración de bases de datos
- **Identificar** los componentes clave de una arquitectura de servidor MCP con bases de datos
- **Comprender** el caso de uso de Zava Retail y sus requisitos de negocio
- **Reconocer** patrones empresariales para un acceso seguro y escalable a bases de datos
- **Listar** las herramientas y tecnologías utilizadas en este camino de aprendizaje

## 🧭 El Desafío: IA y Datos del Mundo Real

### Limitaciones Tradicionales de la IA

Los asistentes de IA modernos son increíblemente poderosos, pero enfrentan limitaciones significativas al trabajar con datos de negocio del mundo real:

| **Desafío**         | **Descripción**                                   | **Impacto en el Negocio**               |
|---------------------|--------------------------------------------------|-----------------------------------------|
| **Conocimiento Estático** | Los modelos de IA entrenados en conjuntos de datos fijos no pueden acceder a datos actuales de negocio | Insights desactualizados, oportunidades perdidas |
| **Silos de Datos**  | Información bloqueada en bases de datos, APIs y sistemas que la IA no puede alcanzar | Análisis incompleto, flujos de trabajo fragmentados |
| **Restricciones de Seguridad** | El acceso directo a bases de datos plantea preocupaciones de seguridad y cumplimiento | Despliegue limitado, preparación manual de datos |
| **Consultas Complejas** | Los usuarios de negocio necesitan conocimientos técnicos para extraer insights de datos | Menor adopción, procesos ineficientes |

### La Solución MCP

El Protocolo de Contexto de Modelo aborda estos desafíos proporcionando:

- **Acceso a Datos en Tiempo Real**: Los asistentes de IA consultan bases de datos y APIs en vivo
- **Integración Segura**: Acceso controlado con autenticación y permisos
- **Interfaz en Lenguaje Natural**: Los usuarios de negocio hacen preguntas en lenguaje sencillo
- **Protocolo Estandarizado**: Funciona con diferentes plataformas y herramientas de IA

## 🏪 Conoce Zava Retail: Nuestro Caso de Estudio https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail

A lo largo de este camino de aprendizaje, construiremos un servidor MCP para **Zava Retail**, una cadena minorista ficticia de bricolaje con múltiples ubicaciones. Este escenario realista demuestra una implementación MCP de nivel empresarial.

### Contexto de Negocio

**Zava Retail** opera:
- **8 tiendas físicas** en el estado de Washington (Seattle, Bellevue, Tacoma, Spokane, Everett, Redmond, Kirkland)
- **1 tienda en línea** para ventas de comercio electrónico
- **Catálogo de productos diverso** que incluye herramientas, hardware, suministros de jardinería y materiales de construcción
- **Gestión multinivel** con gerentes de tienda, gerentes regionales y ejecutivos

### Requisitos de Negocio

Los gerentes de tienda y ejecutivos necesitan análisis impulsados por IA para:

1. **Analizar el rendimiento de ventas** en tiendas y períodos de tiempo
2. **Rastrear niveles de inventario** e identificar necesidades de reabastecimiento
3. **Comprender el comportamiento del cliente** y patrones de compra
4. **Descubrir insights de productos** mediante búsqueda semántica
5. **Generar informes** con consultas en lenguaje natural
6. **Mantener la seguridad de los datos** con control de acceso basado en roles

### Requisitos Técnicos

El servidor MCP debe proporcionar:

- **Acceso a datos multiusuario** donde los gerentes de tienda solo vean los datos de su tienda
- **Consultas flexibles** que soporten operaciones SQL complejas
- **Búsqueda semántica** para descubrimiento de productos y recomendaciones
- **Datos en tiempo real** que reflejen el estado actual del negocio
- **Autenticación segura** con seguridad a nivel de fila
- **Arquitectura escalable** que soporte múltiples usuarios concurrentes

## 🏗️ Resumen de la Arquitectura del Servidor MCP

Nuestro servidor MCP implementa una arquitectura por capas optimizada para la integración de bases de datos:

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

### Componentes Clave

#### **1. Capa del Servidor MCP**
- **FastMCP Framework**: Implementación moderna de servidor MCP en Python
- **Registro de Herramientas**: Definiciones declarativas de herramientas con seguridad de tipos
- **Contexto de Solicitudes**: Gestión de identidad de usuario y sesiones
- **Manejo de Errores**: Gestión robusta de errores y registro de eventos

#### **2. Capa de Integración de Bases de Datos**
- **Pooling de Conexiones**: Gestión eficiente de conexiones asyncpg
- **Proveedor de Esquemas**: Descubrimiento dinámico de esquemas de tablas
- **Ejecutor de Consultas**: Ejecución segura de SQL con contexto RLS
- **Gestión de Transacciones**: Cumplimiento ACID y manejo de rollbacks

#### **3. Capa de Seguridad**
- **Seguridad a Nivel de Fila**: RLS de PostgreSQL para aislamiento de datos multiusuario
- **Identidad de Usuario**: Autenticación y autorización de gerentes de tienda
- **Control de Acceso**: Permisos detallados y registros de auditoría
- **Validación de Entradas**: Prevención de inyección SQL y validación de consultas

#### **4. Capa de Mejora de IA**
- **Búsqueda Semántica**: Embeddings vectoriales para descubrimiento de productos
- **Integración con Azure OpenAI**: Generación de embeddings de texto
- **Algoritmos de Similitud**: Búsqueda de similitud con pgvector y coseno
- **Optimización de Búsqueda**: Indexación y ajuste de rendimiento

## 🔧 Stack Tecnológico

### Tecnologías Principales

| **Componente**       | **Tecnología**            | **Propósito**                     |
|----------------------|--------------------------|-----------------------------------|
| **Framework MCP**    | FastMCP (Python)         | Implementación moderna de servidor MCP |
| **Base de Datos**    | PostgreSQL 17 + pgvector | Datos relacionales con búsqueda vectorial |
| **Servicios de IA**  | Azure OpenAI             | Embeddings de texto y modelos de lenguaje |
| **Contenerización**  | Docker + Docker Compose  | Entorno de desarrollo            |
| **Plataforma en la Nube** | Microsoft Azure      | Despliegue en producción          |
| **Integración IDE**  | VS Code                  | Chat de IA y flujo de trabajo de desarrollo |

### Herramientas de Desarrollo

| **Herramienta**      | **Propósito**             |
|----------------------|--------------------------|
| **asyncpg**          | Driver PostgreSQL de alto rendimiento |
| **Pydantic**         | Validación y serialización de datos |
| **Azure SDK**        | Integración de servicios en la nube |
| **pytest**           | Framework de pruebas     |
| **Docker**           | Contenerización y despliegue |

### Stack de Producción

| **Servicio**         | **Recurso Azure**         | **Propósito**                     |
|----------------------|--------------------------|-----------------------------------|
| **Base de Datos**    | Azure Database for PostgreSQL | Servicio de base de datos gestionado |
| **Contenedor**       | Azure Container Apps     | Hosting de contenedores sin servidor |
| **Servicios de IA**  | Azure AI Foundry         | Modelos y endpoints de OpenAI    |
| **Monitoreo**        | Application Insights     | Observabilidad y diagnóstico      |
| **Seguridad**        | Azure Key Vault          | Gestión de secretos y configuración |

## 🎬 Escenarios de Uso en el Mundo Real

Exploremos cómo diferentes usuarios interactúan con nuestro servidor MCP:

### Escenario 1: Revisión de Rendimiento del Gerente de Tienda

**Usuario**: Sarah, Gerente de la Tienda de Seattle  
**Objetivo**: Analizar el rendimiento de ventas del último trimestre

**Consulta en Lenguaje Natural**:
> "Muéstrame los 10 productos principales por ingresos de mi tienda en el cuarto trimestre de 2024"

**Qué Ocurre**:
1. VS Code AI Chat envía la consulta al servidor MCP
2. El servidor MCP identifica el contexto de la tienda de Sarah (Seattle)
3. Las políticas RLS filtran los datos solo para la tienda de Seattle
4. Se genera y ejecuta la consulta SQL
5. Los resultados se formatean y se devuelven al AI Chat
6. La IA proporciona análisis e insights

### Escenario 2: Descubrimiento de Productos con Búsqueda Semántica

**Usuario**: Mike, Gerente de Inventario  
**Objetivo**: Encontrar productos similares a una solicitud de cliente

**Consulta en Lenguaje Natural**:
> "¿Qué productos vendemos que sean similares a 'conectores eléctricos impermeables para uso exterior'?"

**Qué Ocurre**:
1. La consulta es procesada por la herramienta de búsqueda semántica
2. Azure OpenAI genera un vector de embedding
3. pgvector realiza la búsqueda de similitud
4. Los productos relacionados se clasifican por relevancia
5. Los resultados incluyen detalles y disponibilidad de productos
6. La IA sugiere alternativas y oportunidades de agrupamiento

### Escenario 3: Análisis Entre Tiendas

**Usuario**: Jennifer, Gerente Regional  
**Objetivo**: Comparar el rendimiento entre todas las tiendas

**Consulta en Lenguaje Natural**:
> "Compara las ventas por categoría en todas las tiendas en los últimos 6 meses"

**Qué Ocurre**:
1. Se establece el contexto RLS para acceso de gerente regional
2. Se genera una consulta compleja entre múltiples tiendas
3. Los datos se agregan entre ubicaciones de tiendas
4. Los resultados incluyen tendencias y comparaciones
5. La IA identifica insights y recomendaciones

## 🔒 Análisis Detallado de Seguridad y Multiusuario

Nuestra implementación prioriza la seguridad de nivel empresarial:

### Seguridad a Nivel de Fila (RLS)

PostgreSQL RLS asegura el aislamiento de datos:

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

### Gestión de Identidad de Usuario

Cada conexión MCP incluye:
- **ID de Gerente de Tienda**: Identificador único para el contexto RLS
- **Asignación de Roles**: Permisos y niveles de acceso
- **Gestión de Sesiones**: Tokens de autenticación seguros
- **Registro de Auditoría**: Historial completo de accesos

### Protección de Datos

Múltiples capas de seguridad:
- **Encriptación de Conexiones**: TLS para todas las conexiones a bases de datos
- **Prevención de Inyección SQL**: Solo consultas parametrizadas
- **Validación de Entradas**: Validación exhaustiva de solicitudes
- **Manejo de Errores**: Sin datos sensibles en mensajes de error

## 🎯 Puntos Clave

Después de completar esta introducción, deberías comprender:

✅ **Propuesta de Valor de MCP**: Cómo MCP conecta asistentes de IA con datos del mundo real  
✅ **Contexto de Negocio**: Requisitos y desafíos de Zava Retail  
✅ **Resumen de Arquitectura**: Componentes clave y sus interacciones  
✅ **Stack Tecnológico**: Herramientas y frameworks utilizados  
✅ **Modelo de Seguridad**: Acceso a datos multiusuario y protección  
✅ **Patrones de Uso**: Escenarios de consulta y flujos de trabajo en el mundo real  

## 🚀 Próximos Pasos

¿Listo para profundizar? Continúa con:

**[Laboratorio 01: Conceptos Básicos de Arquitectura](../01-Architecture/README.md)**

Aprende sobre patrones de arquitectura de servidores MCP, principios de diseño de bases de datos y la implementación técnica detallada que impulsa nuestra solución de análisis minorista.

## 📚 Recursos Adicionales

### Documentación MCP
- [Especificación MCP](https://modelcontextprotocol.io/docs/) - Documentación oficial del protocolo
- [MCP para Principiantes](https://aka.ms/mcp-for-beginners) - Guía completa de aprendizaje MCP
- [Documentación de FastMCP](https://github.com/modelcontextprotocol/python-sdk) - Documentación del SDK de Python

### Integración de Bases de Datos
- [Documentación de PostgreSQL](https://www.postgresql.org/docs/) - Referencia completa de PostgreSQL
- [Guía de pgvector](https://github.com/pgvector/pgvector) - Documentación de la extensión vectorial
- [Seguridad a Nivel de Fila](https://www.postgresql.org/docs/current/ddl-rowsecurity.html) - Guía de RLS en PostgreSQL

### Servicios de Azure
- [Documentación de Azure OpenAI](https://docs.microsoft.com/azure/cognitive-services/openai/) - Integración de servicios de IA
- [Azure Database for PostgreSQL](https://docs.microsoft.com/azure/postgresql/) - Servicio de base de datos gestionado
- [Azure Container Apps](https://docs.microsoft.com/azure/container-apps/) - Contenedores sin servidor

---

**Aviso**: Este es un ejercicio de aprendizaje utilizando datos minoristas ficticios. Siempre sigue las políticas de gobernanza y seguridad de datos de tu organización al implementar soluciones similares en entornos de producción.

---

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por garantizar la precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o imprecisiones. El documento original en su idioma nativo debe considerarse como la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o interpretaciones erróneas que puedan surgir del uso de esta traducción.