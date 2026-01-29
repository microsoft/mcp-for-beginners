# Introducción al Protocolo de Contexto de Modelos (MCP): Por qué es importante para aplicaciones de IA escalables

[![Introducción al Protocolo de Contexto de Modelos](../../../translated_images/es/01.a467036d886b5fb5.webp)](https://youtu.be/agBbdiOPLQA)

_(Haz clic en la imagen de arriba para ver el video de esta lección)_

Las aplicaciones de IA generativa representan un gran avance, ya que a menudo permiten que el usuario interactúe con la aplicación mediante indicaciones en lenguaje natural. Sin embargo, a medida que se invierten más tiempo y recursos en estas aplicaciones, es importante asegurarse de que puedas integrar funcionalidades y recursos de manera sencilla, que sea fácil de ampliar, que tu aplicación pueda trabajar con más de un modelo y manejar diversas complejidades de los modelos. En resumen, construir aplicaciones de IA generativa es fácil al principio, pero a medida que crecen y se vuelven más complejas, necesitas empezar a definir una arquitectura y probablemente depender de un estándar para garantizar que tus aplicaciones se construyan de manera consistente. Aquí es donde entra MCP para organizar las cosas y proporcionar un estándar.

---

## **🔍 ¿Qué es el Protocolo de Contexto de Modelos (MCP)?**

El **Protocolo de Contexto de Modelos (MCP)** es una **interfaz abierta y estandarizada** que permite que los Modelos de Lenguaje Extenso (LLMs) interactúen sin problemas con herramientas externas, APIs y fuentes de datos. Proporciona una arquitectura consistente para mejorar la funcionalidad de los modelos de IA más allá de sus datos de entrenamiento, permitiendo sistemas de IA más inteligentes, escalables y receptivos.

---

## **🎯 Por qué la estandarización en IA es importante**

A medida que las aplicaciones de IA generativa se vuelven más complejas, es esencial adoptar estándares que garanticen **escalabilidad, extensibilidad, mantenibilidad** y **evitar la dependencia de proveedores**. MCP aborda estas necesidades mediante:

- Unificación de las integraciones entre modelos y herramientas
- Reducción de soluciones personalizadas frágiles y únicas
- Permitir que múltiples modelos de diferentes proveedores coexistan en un mismo ecosistema

**Nota:** Aunque MCP se presenta como un estándar abierto, no hay planes para estandarizar MCP a través de organismos de estándares existentes como IEEE, IETF, W3C, ISO u otros.

---

## **📚 Objetivos de aprendizaje**

Al final de este artículo, podrás:

- Definir el **Protocolo de Contexto de Modelos (MCP)** y sus casos de uso
- Comprender cómo MCP estandariza la comunicación entre modelos y herramientas
- Identificar los componentes principales de la arquitectura MCP
- Explorar aplicaciones reales de MCP en contextos empresariales y de desarrollo

---

## **💡 Por qué el Protocolo de Contexto de Modelos (MCP) es revolucionario**

### **🔗 MCP resuelve la fragmentación en las interacciones de IA**

Antes de MCP, integrar modelos con herramientas requería:

- Código personalizado para cada par herramienta-modelo
- APIs no estandarizadas para cada proveedor
- Fallos frecuentes debido a actualizaciones
- Escalabilidad limitada con más herramientas

### **✅ Beneficios de la estandarización de MCP**

| **Beneficio**              | **Descripción**                                                                |
|--------------------------|--------------------------------------------------------------------------------|
| Interoperabilidad         | Los LLMs funcionan sin problemas con herramientas de diferentes proveedores    |
| Consistencia              | Comportamiento uniforme en plataformas y herramientas                         |
| Reutilización             | Las herramientas creadas una vez pueden usarse en múltiples proyectos y sistemas |
| Desarrollo acelerado      | Reducir el tiempo de desarrollo utilizando interfaces estandarizadas y listas para usar |

---

## **🧱 Descripción general de la arquitectura de MCP**

MCP sigue un modelo **cliente-servidor**, donde:

- **Hosts MCP** ejecutan los modelos de IA
- **Clientes MCP** inician solicitudes
- **Servidores MCP** proporcionan contexto, herramientas y capacidades

### **Componentes clave:**

- **Recursos** – Datos estáticos o dinámicos para los modelos  
- **Prompts** – Flujos de trabajo predefinidos para generación guiada  
- **Herramientas** – Funciones ejecutables como búsqueda, cálculos  
- **Muestreo** – Comportamiento agente mediante interacciones recursivas  

---

## Cómo funcionan los servidores MCP

Los servidores MCP operan de la siguiente manera:

- **Flujo de solicitud**:
    1. Un usuario final o un software que actúa en su nombre inicia una solicitud.
    2. El **Cliente MCP** envía la solicitud a un **Host MCP**, que gestiona la ejecución del modelo de IA.
    3. El **Modelo de IA** recibe la indicación del usuario y puede solicitar acceso a herramientas externas o datos mediante una o más llamadas a herramientas.
    4. El **Host MCP**, no el modelo directamente, se comunica con los **Servidores MCP** correspondientes utilizando el protocolo estandarizado.
- **Funcionalidad del Host MCP**:
    - **Registro de herramientas**: Mantiene un catálogo de herramientas disponibles y sus capacidades.
    - **Autenticación**: Verifica permisos para el acceso a herramientas.
    - **Gestor de solicitudes**: Procesa las solicitudes de herramientas provenientes del modelo.
    - **Formateador de respuestas**: Estructura las salidas de las herramientas en un formato que el modelo pueda entender.
- **Ejecución del Servidor MCP**:
    - El **Host MCP** dirige las llamadas a herramientas hacia uno o más **Servidores MCP**, cada uno exponiendo funciones especializadas (por ejemplo, búsqueda, cálculos, consultas a bases de datos).
    - Los **Servidores MCP** realizan sus respectivas operaciones y devuelven resultados al **Host MCP** en un formato consistente.
    - El **Host MCP** formatea y transmite estos resultados al **Modelo de IA**.
- **Finalización de la respuesta**:
    - El **Modelo de IA** incorpora las salidas de las herramientas en una respuesta final.
    - El **Host MCP** envía esta respuesta de vuelta al **Cliente MCP**, que la entrega al usuario final o al software que realizó la solicitud.

```mermaid
---
title: MCP Architecture and Component Interactions
description: A diagram showing the flows of the components in MCP.
---
graph TD
    Client[MCP Client/Application] -->|Sends Request| H[MCP Host]
    H -->|Invokes| A[AI Model]
    A -->|Tool Call Request| H
    H -->|MCP Protocol| T1[MCP Server Tool 01: Web Search]
    H -->|MCP Protocol| T2[MCP Server Tool 02: Calculator tool]
    H -->|MCP Protocol| T3[MCP Server Tool 03: Database Access tool]
    H -->|MCP Protocol| T4[MCP Server Tool 04: File System tool]
    H -->|Sends Response| Client

    subgraph "MCP Host Components"
        H
        G[Tool Registry]
        I[Authentication]
        J[Request Handler]
        K[Response Formatter]
    end

    H <--> G
    H <--> I
    H <--> J
    H <--> K

    style A fill:#f9d5e5,stroke:#333,stroke-width:2px
    style H fill:#eeeeee,stroke:#333,stroke-width:2px
    style Client fill:#d5e8f9,stroke:#333,stroke-width:2px
    style G fill:#fffbe6,stroke:#333,stroke-width:1px
    style I fill:#fffbe6,stroke:#333,stroke-width:1px
    style J fill:#fffbe6,stroke:#333,stroke-width:1px
    style K fill:#fffbe6,stroke:#333,stroke-width:1px
    style T1 fill:#c2f0c2,stroke:#333,stroke-width:1px
    style T2 fill:#c2f0c2,stroke:#333,stroke-width:1px
    style T3 fill:#c2f0c2,stroke:#333,stroke-width:1px
    style T4 fill:#c2f0c2,stroke:#333,stroke-width:1px
```

## 👨‍💻 Cómo construir un servidor MCP (con ejemplos)

Los servidores MCP te permiten ampliar las capacidades de los LLM proporcionando datos y funcionalidades.

¿Listo para probarlo? Aquí tienes SDKs específicos para lenguajes y/o stacks con ejemplos de cómo crear servidores MCP simples en diferentes lenguajes/stacks:

- **Python SDK**: https://github.com/modelcontextprotocol/python-sdk

- **TypeScript SDK**: https://github.com/modelcontextprotocol/typescript-sdk

- **Java SDK**: https://github.com/modelcontextprotocol/java-sdk

- **C#/.NET SDK**: https://github.com/modelcontextprotocol/csharp-sdk

## 🌍 Casos de uso reales de MCP

MCP habilita una amplia gama de aplicaciones al extender las capacidades de la IA:

| **Aplicación**              | **Descripción**                                                                |
|------------------------------|--------------------------------------------------------------------------------|
| Integración de datos empresariales | Conectar LLMs a bases de datos, CRMs o herramientas internas                 |
| Sistemas de IA autónomos     | Permitir agentes autónomos con acceso a herramientas y flujos de toma de decisiones |
| Aplicaciones multimodales    | Combinar herramientas de texto, imagen y audio en una única aplicación de IA unificada |
| Integración de datos en tiempo real | Incorporar datos en vivo en interacciones de IA para obtener resultados más precisos y actuales |

### 🧠 MCP = Estándar universal para interacciones de IA

El Protocolo de Contexto de Modelos (MCP) actúa como un estándar universal para interacciones de IA, al igual que el USB-C estandarizó las conexiones físicas para dispositivos. En el mundo de la IA, MCP proporciona una interfaz consistente, permitiendo que los modelos (clientes) se integren sin problemas con herramientas externas y proveedores de datos (servidores). Esto elimina la necesidad de protocolos personalizados y diversos para cada API o fuente de datos.

Bajo MCP, una herramienta compatible con MCP (referida como servidor MCP) sigue un estándar unificado. Estos servidores pueden listar las herramientas o acciones que ofrecen y ejecutar esas acciones cuando son solicitadas por un agente de IA. Las plataformas de agentes de IA que admiten MCP son capaces de descubrir herramientas disponibles de los servidores e invocarlas a través de este protocolo estándar.

### 💡 Facilita el acceso al conocimiento

Además de ofrecer herramientas, MCP también facilita el acceso al conocimiento. Permite que las aplicaciones proporcionen contexto a los modelos de lenguaje extenso (LLMs) vinculándolos a diversas fuentes de datos. Por ejemplo, un servidor MCP podría representar el repositorio de documentos de una empresa, permitiendo que los agentes recuperen información relevante bajo demanda. Otro servidor podría manejar acciones específicas como enviar correos electrónicos o actualizar registros. Desde la perspectiva del agente, estas son simplemente herramientas que puede usar: algunas herramientas devuelven datos (contexto de conocimiento), mientras que otras realizan acciones. MCP gestiona eficientemente ambos.

Un agente que se conecta a un servidor MCP aprende automáticamente las capacidades disponibles del servidor y los datos accesibles mediante un formato estándar. Esta estandarización permite la disponibilidad dinámica de herramientas. Por ejemplo, agregar un nuevo servidor MCP al sistema de un agente hace que sus funciones sean inmediatamente utilizables sin necesidad de personalizar más las instrucciones del agente.

Esta integración simplificada se alinea con el flujo representado en el siguiente diagrama, donde los servidores proporcionan tanto herramientas como conocimiento, asegurando una colaboración fluida entre sistemas.

### 👉 Ejemplo: Solución escalable para agentes

```mermaid
---
title: Scalable Agent Solution with MCP
description: A diagram illustrating how a user interacts with an LLM that connects to multiple MCP servers, with each server providing both knowledge and tools, creating a scalable AI system architecture
---
graph TD
    User -->|Prompt| LLM
    LLM -->|Response| User
    LLM -->|MCP| ServerA
    LLM -->|MCP| ServerB
    ServerA -->|Universal connector| ServerB
    ServerA --> KnowledgeA
    ServerA --> ToolsA
    ServerB --> KnowledgeB
    ServerB --> ToolsB

    subgraph Server A
        KnowledgeA[Knowledge]
        ToolsA[Tools]
    end

    subgraph Server B
        KnowledgeB[Knowledge]
        ToolsB[Tools]
    end
```
El Conector Universal permite que los servidores MCP se comuniquen y compartan capacidades entre sí, permitiendo que el ServidorA delegue tareas al ServidorB o acceda a sus herramientas y conocimiento. Esto federará herramientas y datos entre servidores, apoyando arquitecturas de agentes escalables y modulares. Debido a que MCP estandariza la exposición de herramientas, los agentes pueden descubrir dinámicamente y enrutar solicitudes entre servidores sin integraciones codificadas.

Federación de herramientas y conocimiento: Las herramientas y datos pueden ser accesibles entre servidores, habilitando arquitecturas de agentes más escalables y modulares.

### 🔄 Escenarios avanzados de MCP con integración de LLM en el lado del cliente

Más allá de la arquitectura básica de MCP, existen escenarios avanzados donde tanto el cliente como el servidor contienen LLMs, permitiendo interacciones más sofisticadas. En el siguiente diagrama, la **Aplicación Cliente** podría ser un IDE con varias herramientas MCP disponibles para el uso del LLM:

```mermaid
---
title: Advanced MCP Scenarios with Client-Server LLM Integration
description: A sequence diagram showing the detailed interaction flow between user, client application, client LLM, multiple MCP servers, and server LLM, illustrating tool discovery, user interaction, direct tool calling, and feature negotiation phases
---
sequenceDiagram
    autonumber
    actor User as 👤 User
    participant ClientApp as 🖥️ Client App
    participant ClientLLM as 🧠 Client LLM
    participant Server1 as 🔧 MCP Server 1
    participant Server2 as 📚 MCP Server 2
    participant ServerLLM as 🤖 Server LLM
    
    %% Discovery Phase
    rect rgb(220, 240, 255)
        Note over ClientApp, Server2: TOOL DISCOVERY PHASE
        ClientApp->>+Server1: Request available tools/resources
        Server1-->>-ClientApp: Return tool list (JSON)
        ClientApp->>+Server2: Request available tools/resources
        Server2-->>-ClientApp: Return tool list (JSON)
        Note right of ClientApp: Store combined tool<br/>catalog locally
    end
    
    %% User Interaction
    rect rgb(255, 240, 220)
        Note over User, ClientLLM: USER INTERACTION PHASE
        User->>+ClientApp: Enter natural language prompt
        ClientApp->>+ClientLLM: Forward prompt + tool catalog
        ClientLLM->>-ClientLLM: Analyze prompt & select tools
    end
    
    %% Scenario A: Direct Tool Calling
    alt Direct Tool Calling
        rect rgb(220, 255, 220)
            Note over ClientApp, Server1: SCENARIO A: DIRECT TOOL CALLING
            ClientLLM->>+ClientApp: Request tool execution
            ClientApp->>+Server1: Execute specific tool
            Server1-->>-ClientApp: Return results
            ClientApp->>+ClientLLM: Process results
            ClientLLM-->>-ClientApp: Generate response
            ClientApp-->>-User: Display final answer
        end
    
    %% Scenario B: Feature Negotiation (VS Code style)
    else Feature Negotiation (VS Code style)
        rect rgb(255, 220, 220)
            Note over ClientApp, ServerLLM: SCENARIO B: FEATURE NEGOTIATION
            ClientLLM->>+ClientApp: Identify needed capabilities
            ClientApp->>+Server2: Negotiate features/capabilities
            Server2->>+ServerLLM: Request additional context
            ServerLLM-->>-Server2: Provide context
            Server2-->>-ClientApp: Return available features
            ClientApp->>+Server2: Call negotiated tools
            Server2-->>-ClientApp: Return results
            ClientApp->>+ClientLLM: Process results
            ClientLLM-->>-ClientApp: Generate response
            ClientApp-->>-User: Display final answer
        end
    end
```

## 🔐 Beneficios prácticos de MCP

Aquí están los beneficios prácticos de usar MCP:

- **Actualización**: Los modelos pueden acceder a información actualizada más allá de sus datos de entrenamiento
- **Extensión de capacidades**: Los modelos pueden aprovechar herramientas especializadas para tareas para las que no fueron entrenados
- **Reducción de alucinaciones**: Las fuentes de datos externas proporcionan una base factual
- **Privacidad**: Los datos sensibles pueden permanecer en entornos seguros en lugar de ser incrustados en indicaciones

## 📌 Puntos clave

Los siguientes son puntos clave para usar MCP:

- **MCP** estandariza cómo los modelos de IA interactúan con herramientas y datos
- Promueve **extensibilidad, consistencia e interoperabilidad**
- MCP ayuda a **reducir el tiempo de desarrollo, mejorar la confiabilidad y extender las capacidades del modelo**
- La arquitectura cliente-servidor **habilita aplicaciones de IA flexibles y extensibles**

## 🧠 Ejercicio

Piensa en una aplicación de IA que te interese construir.

- ¿Qué **herramientas externas o datos** podrían mejorar sus capacidades?
- ¿Cómo podría MCP hacer que la integración sea **más simple y confiable**?

## Recursos adicionales

- [Repositorio GitHub de MCP](https://github.com/modelcontextprotocol)

## Qué sigue

Siguiente: [Capítulo 1: Conceptos básicos](../01-CoreConcepts/README.md)

---

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por garantizar la precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o imprecisiones. El documento original en su idioma nativo debe considerarse como la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o interpretaciones erróneas que puedan surgir del uso de esta traducción.