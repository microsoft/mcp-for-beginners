# Registro de cambios: Currículo MCP para principiantes

Este documento sirve como un registro de todos los cambios significativos realizados en el currículo de Model Context Protocol (MCP) para principiantes. Los cambios se documentan en orden cronológico inverso (los cambios más recientes primero).

## 11 de abril de 2026

### Nueva lección, correcciones de documentación y actualizaciones de dependencias

#### Nuevo contenido del currículo agregado

**Módulo 05 - Temas Avanzados**  
- **Lección 5.17: Razonamiento multiagente adversarial con MCP** (`05-AdvancedTopics/mcp-adversarial-agents/README.md`): Nueva guía completa que cubre el patrón de debate adversarial para sistemas multiagente  
  - Diagrama de arquitectura Mermaid: dos agentes → servidor MCP compartido → transcripción del debate → juez → veredicto  
  - Servidor de herramientas compartido MCP (`web_search` + `run_python`) implementado en Python y TypeScript  
  - Prompts del sistema opuestos (A FAVOR / EN CONTRA / Juez) con requisitos explícitos de uso de herramientas  
  - Orquestador de debates en Python, TypeScript y C# gestionando rondas y enrutamiento de argumentos  
  - Cableado MCP `ClientSession` para el orquestador hacia llamadas reales de herramientas  
  - Tabla de casos de uso (detección de alucinaciones, modelado de amenazas, revisión de diseño de API, verificación factual, selección tecnológica)  
  - Consideraciones de seguridad: ejecución en sandbox, validación de llamadas a herramientas, limitación de tasa, registro de auditoría  
  - Ejercicio estructurado con tres escenarios prácticos (revisión de código, decisión arquitectónica, moderación de contenido)

#### Correcciones de documentación

**Módulo 03 - Introducción**  
- **05-stdio-server/README.md**: Corregido ejemplo incompleto del servidor stdio en TypeScript — se añadió la instancia faltante del transporte (`new StdioServerTransport()`) y la llamada `server.connect(transport)` para coincidir con los ejemplos de Python y .NET en la misma sección  
- **14-sampling/README.md**: Corregido error tipográfico — corregido `"Sampling is an davanced features"` → `"Sampling is an advanced feature"`

#### Actualizaciones del currículo

**README.md principal**  
- Se añadió la entrada 5.17 (Razonamiento Multiagente Adversarial con MCP) a la tabla del currículo con un enlace directo a la nueva lección

**05-AdvancedTopics/README.md**  
- Se añadió la fila de la Lección 5.17 a la tabla de lecciones

**study_guide.md**  
- Se añadió el tema Razonamiento Multiagente Adversarial al mapa mental y la descripción en prosa de Temas Avanzados

#### Correcciones de código y seguridad

**Módulo 05 - Agentes adversarios (`mcp-adversarial-agents`)**  
- **Corrección de seguridad — inyección de comandos**: Se reemplazó la interpolación de shell `execSync` por `execFile` + `promisify` en la herramienta `run_python` de TypeScript, eliminando la superficie de inyección de comandos (el código controlado por LLM ahora se pasa como literal argv sin involucrar shell)  
- **Cableado del bucle de herramienta MCP**: Se actualizó el orquestador de debates en Python para usar cliente `AsyncAnthropic` (reemplazando el sincrónico `Anthropic` bloqueante), pasar una `ClientSession` viva directamente a cada turno de agente, obtener definiciones de herramientas vía `session.list_tools()` en cada turno, y despachar bloques `tool_use` vía `session.call_tool()` en un bucle hasta que el modelo emite una respuesta final de texto

#### Actualizaciones de dependencias

- Actualización de `hono` a versión 4.12.12 en múltiples paquetes (03-GettingStarted, 04-PracticalImplementation, 10-StreamliningAIWorkflows)  
- Actualización de `@hono/node-server` de 1.19.11 a 1.19.13 en paquetes TypeScript  
- Actualización de `cryptography` de 46.0.5 a 46.0.7 en paquetes Python (10-StreamliningAIWorkflows laboratorios 3 y 4)  
- Actualización de `lodash` de 4.17.23 a 4.18.1 en inspector de 10-StreamliningAIWorkflows

#### Traducciones

- Sincronización de traducciones para más de 48 idiomas con los últimos cambios en la fuente (actualización i18n)

---

## 5 de febrero de 2026

### Mejoras de validación y navegación en todo el repositorio

#### Nuevo contenido del currículo agregado

**Módulo 03 - Introducción**  
- **12-mcp-hosts/README.md**: Nueva guía completa para configurar hosts MCP  
  - Ejemplos de configuración para Claude Desktop, VS Code, Cursor, Cline, Windsurf  
  - Plantillas JSON de configuración para todos los hosts principales  
  - Tabla comparativa de tipos de transporte (stdio, SSE/HTTP, WebSocket)  
  - Solución de problemas comunes de conexión  
  - Mejores prácticas de seguridad para configuración de hosts

- **13-mcp-inspector/README.md**: Nueva guía de depuración para MCP Inspector  
  - Métodos de instalación (npx, npm global, desde la fuente)  
  - Conexión a servidores vía stdio y HTTP/SSE  
  - Herramientas de prueba, recursos y flujos de trabajo de prompts  
  - Integración con VS Code y MCP Inspector  
  - Escenarios comunes de depuración con soluciones

**Módulo 04 - Implementación práctica**  
- **pagination/README.md**: Nueva guía para implementación de paginación  
  - Patrones de paginación basada en cursor en Python, TypeScript, Java  
  - Manejo de paginación del lado cliente  
  - Estrategias de diseño de cursor (opaco vs estructurado)  
  - Recomendaciones para optimización de rendimiento

**Módulo 05 - Temas avanzados**  
- **mcp-protocol-features/README.md**: Nueva exploración en profundidad de características del protocolo  
  - Implementación de notificaciones de progreso  
  - Patrones para cancelación de solicitudes  
  - Plantillas de recursos con patrones URI  
  - Gestión del ciclo de vida del servidor  
  - Control de nivel de logging  
  - Patrones de manejo de errores con códigos JSON-RPC

#### Correcciones de navegación (más de 24 archivos actualizados)

**READMEs principales de módulos**  
 Ahora enlazan tanto a la primera lección COMO al siguiente módulo

**Subarchivos 02-Security**  
- Los 5 documentos complementarios de seguridad ahora tienen navegación "Qué sigue":

**Archivos 09-CaseStudy**  
- Todos los archivos de estudios de caso ahora tienen navegación secuencial:

**Laboratorios 10-StreamliningAI**  
Se añadió sección Qué sigue a la visión general del Módulo 10 y al Módulo 11

#### Correcciones de código y contenido

**Actualizaciones de SDK y dependencias**  
Se corrigió versión abierta de openai a `^4.95.0`  
Se actualizó SDK de `^1.8.0` a `>=1.26.0`  
Se actualizaron los pines de versión de mcp a `>=1.26.0`

**Correcciones de código**  
Se corrigió modelo inválido `gpt-4o-mini` a `gpt-4.1-mini`

**Correcciones de contenido**  
Se corrigió enlace roto `READMEmd` → `README.md`, encabezado del currículo corregido `Módulo 1-3` → `Módulo 0-3`, corregido path sensible a mayúsculas  
Se eliminó contenido duplicado corrupto del Estudio de Caso 5

**Mejoras para principiantes**  
Se añadió introducción adecuada, objetivos de aprendizaje y prerrequisitos para principiantes

#### Actualizaciones del currículo

**README.md principal**  
- Se añadieron entradas 3.12 (Hosts MCP), 3.13 (Inspector MCP), 4.1 (Paginación), 5.16 (Características del Protocolo) a la tabla del currículo

**READMEs de módulos**  
Se añadieron lecciones 12 y 13 a la lista de lecciones  
Se añadió sección de Guías Prácticas con enlace a paginación  
Se añadieron lecciones 5.15 (Transporte personalizado) y 5.16 (Características del protocolo)

**study_guide.md**  
- Se actualizó mapa mental con todos los temas nuevos: Configuración de Hosts MCP, Inspector MCP, Estrategias de Paginación, Exploración de Características del Protocolo

## 28 de enero de 2026

### Revisión de cumplimiento de la especificación MCP 2025-11-25

#### Mejora de conceptos centrales (01-CoreConcepts/)  
- **Nueva primitiva cliente - Roots**: Documentación integral sobre la primitiva cliente Roots, que permite a los servidores entender los límites del sistema de archivos y permisos de acceso  
- **Anotaciones de herramientas**: Documentación sobre anotaciones de comportamiento de herramientas (`readOnlyHint`, `destructiveHint`) para mejores decisiones de ejecución de herramientas  
- **Llamadas a herramientas en Sampling**: Documentación actualizada para Sampling que incluye parámetros `tools` y `toolChoice` para invocación de herramientas dirigida por modelo durante solicitudes de sampling  
- **Elicitación modo URL**: Documentación sobre el modo de elicitación basado en URL para interacciones externas iniciadas por servidor  
- **Tareas (experimental)**: Nueva sección que documenta la característica experimental de Tareas para envoltorios de ejecución duradera y recuperación diferida de resultados  
- **Soporte de iconos**: Nota sobre que herramientas, recursos, plantillas de recursos y prompts pueden ahora incluir iconos como metadatos adicionales

#### Actualizaciones de documentación  
- **README.md**: Añadida referencia a la versión de la especificación MCP 2025-11-25 y explicación de versionado basado en fecha  
- **study_guide.md**: Actualización del mapa curricular para incluir Tareas y Anotaciones de herramientas en la sección de Conceptos centrales; actualización de la marca de tiempo del documento

#### Verificación de cumplimiento de la especificación  
- **Versión de protocolo**: Verificada toda la documentación referenciando la especificación MCP actual 2025-11-25  
- **Alineación arquitectónica**: Confirmada la documentación sobre arquitectura de dos capas (Capa de datos + Capa de transporte)  
- **Documentación de primitivas**: Validación de primitivas servidor (Recursos, Prompts, Herramientas) y primitivas cliente (Sampling, Elicitación, Logging, Roots)  
- **Mecanismos de transporte**: Verificada exactitud de documentación de transporte STDIO y HTTP streaming  
- **Guías de seguridad**: Confirmado alineamiento con las mejores prácticas de seguridad MCP actuales

#### Características clave MCP 2025-11-25 documentadas  
- **Descubrimiento OpenID Connect**: Descubrimiento del servidor de autenticación mediante OIDC  
- **Documentos de metadatos de Client ID OAuth**: Mecanismo recomendado para registro de clientes  
- **JSON Schema 2020-12**: Dialecto por defecto para definiciones de esquema MCP  
- **Sistema de niveles SDK**: Requisitos formalizados para soporte y mantenimiento de características SDK  
- **Estructura de gobernanza**: Grupos de trabajo e interés formalizados en la gobernanza MCP

### Actualización mayor de documentación de seguridad (02-Security/)

#### Integración del taller MCP Security Summit (Sherpa)  
- **Nuevo recurso de entrenamiento práctico**: Añadida integración completa con [MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/) en toda la documentación de seguridad  
- **Cobertura de ruta de expedición**: Documentado el progreso completo de campamento a campamento desde Base Camp al Summit  
- **Alineamiento con OWASP**: Toda la guía de seguridad mapea ahora los riesgos OWASP MCP Azure Security Guide

#### Integración OWASP MCP Top 10  
- **Nueva sección**: Añadida tabla de riesgos de seguridad OWASP MCP Top 10 con mitigaciones Azure en README principal de seguridad  
- **Documentación basada en riesgos**: Actualizado mcp-security-controls-2025.md con referencias a riesgos OWASP MCP para cada dominio de seguridad  
- **Arquitectura de referencia**: Enlace a arquitectura de referencia y patrones de implementación OWASP MCP Azure Security Guide

#### Archivos de seguridad actualizados  
- **README.md**: Añadido resumen del taller Sherpa, tabla de ruta de expedición, resumen de riesgos OWASP MCP Top 10 y sección de entrenamiento práctico  
- **mcp-security-controls-2025.md**: Actualizado encabezado a febrero de 2026, añadidas referencias a riesgos OWASP (MCP01-MCP08), corregida inconsistencia en versión de especificación  
- **mcp-security-best-practices-2025.md**: Añadida sección de recursos Sherpa y OWASP, actualización de marca de tiempo  
- **mcp-best-practices.md**: Añadida sección de entrenamiento con enlaces a Sherpa y OWASP  
- **azure-content-safety-implementation.md**: Añadida referencia OWASP MCP06, alineación con Sherpa Camp 3 y sección adicional de recursos

#### Nuevos enlaces a recursos añadidos  
- [MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/)  
- [OWASP MCP Azure Security Guide](https://microsoft.github.io/mcp-azure-security-guide/)  
- [OWASP MCP Top 10](https://owasp.org/www-project-mcp-top-10/)  
- Páginas individuales de riesgos OWASP MCP (MCP01-MCP10)

### Alineación de todo el currículo con la especificación MCP 2025-11-25

#### Módulo 03 - Introducción  
- **Documentación SDK**: Añadido Go SDK a la lista oficial de SDK; actualizadas todas las referencias SDK para alinearse con MCP Specification 2025-11-25  
- **Clarificación de transporte**: Actualizadas descripciones de transporte STDIO y HTTP streaming con referencias explícitas a la especificación

#### Módulo 04 - Implementación práctica  
- **Actualizaciones SDK**: Añadido Go SDK; actualizada lista SDK con referencia a la versión de especificación  
- **Especificación de autorización**: Actualizado enlace a especificación MCP Authorization a la versión actual 2025-11-25

#### Módulo 05 - Temas avanzados  
- **Nuevas características**: Añadida nota sobre nuevas características MCP Specification 2025-11-25 (Tareas, Anotaciones de herramientas, Elicitación modo URL, Roots)  
- **Recursos de seguridad**: Añadidos enlaces a OWASP MCP Top 10 y taller Sherpa en referencias adicionales

#### Módulo 06 - Contribuciones comunitarias  
- **Lista SDK**: Añadidos SDKs Swift y Rust; actualizado enlace a especificación 2025-11-25  
- **Referencia a especificación**: Actualizado enlace directo a la URL de la especificación MCP

#### Módulo 07 - Lecciones de adopción temprana  
- **Actualizaciones de recursos**: Añadido enlace a MCP Specification 2025-11-25 y OWASP MCP Top 10 a recursos adicionales

#### Módulo 08 - Mejores prácticas  
- **Versión de especificación**: Actualizado referencia de especificación MCP a 2025-11-25  
- **Recursos de seguridad**: Añadidos OWASP MCP Top 10 y taller Sherpa a referencias adicionales

#### Módulo 10 - Optimización de flujos de trabajo AI  
- **Actualización de insignia**: Cambiada insignia de versión MCP de la versión SDK (1.9.3) a la versión de especificación (2025-11-25)  
- **Enlaces a recursos**: Actualizado enlace a MCP Specification; añadido OWASP MCP Top 10

#### Módulo 11 - Laboratorios prácticos MCP Server  
- **Referencia a especificación**: Actualizado enlace a MCP Specification versión 2025-11-25  
- **Recursos de seguridad**: Añadido OWASP MCP Top 10 a recursos oficiales

## 18 de diciembre de 2025
### Actualización de Documentación de Seguridad - Especificación MCP 2025-11-25

#### Mejores Prácticas de Seguridad MCP (02-Security/mcp-best-practices.md) - Actualización de Versión de Especificación
- **Actualización de Versión de Protocolo**: Actualizado para referenciar la última Especificación MCP 2025-11-25 (lanzada el 25 de noviembre de 2025)
  - Actualizadas todas las referencias de versión de especificación de 2025-06-18 a 2025-11-25
  - Actualizadas las referencias de fechas de documento de 18 de agosto de 2025 a 18 de diciembre de 2025
  - Verificadas todas las URL de especificación que apuntan a la documentación actual
- **Validación de Contenido**: Validación exhaustiva de las mejores prácticas de seguridad conforme a los estándares más recientes
  - **Soluciones de Seguridad de Microsoft**: Verificada la terminología y enlaces actuales para Prompt Shields (anteriormente "detección de riesgo de Jailbreak"), Azure Content Safety, Microsoft Entra ID y Azure Key Vault
  - **Seguridad OAuth 2.1**: Confirmada la alineación con las mejores prácticas de seguridad OAuth más recientes
  - **Estándares OWASP**: Validadas las referencias a OWASP Top 10 para LLMs permanecen actualizadas
  - **Servicios Azure**: Verificados todos los enlaces de documentación Microsoft Azure y mejores prácticas
- **Alineación con Estándares**: Todos los estándares de seguridad referenciados confirmados como actuales
  - Marco de Gestión de Riesgos de IA de NIST
  - ISO 27001:2022
  - Mejores Prácticas de Seguridad OAuth 2.1
  - Marcos de seguridad y cumplimiento de Azure
- **Recursos de Implementación**: Verificados todos los enlaces de guías de implementación y recursos
  - Patrones de autenticación de Azure API Management
  - Guías de integración Microsoft Entra ID
  - Gestión de secretos en Azure Key Vault
  - Pipelines DevSecOps y soluciones de monitoreo

### Aseguramiento de Calidad de la Documentación
- **Cumplimiento de Especificación**: Asegurado que todos los requisitos de seguridad MCP obligatorios (DEBE/NO DEBE) estén alineados con la última especificación
- **Actualidad de Recursos**: Verificados todos los enlaces externos a documentación Microsoft, estándares de seguridad y guías de implementación
- **Cobertura de Mejores Prácticas**: Confirmada cobertura integral sobre autenticación, autorización, amenazas específicas de IA, seguridad en la cadena de suministro y patrones empresariales

## 6 de octubre de 2025

### Expansión de la Sección de Introducción – Uso Avanzado del Servidor y Autenticación Simple

#### Uso Avanzado del Servidor (03-GettingStarted/10-advanced)
- **Nuevo Capítulo Añadido**: Introducida una guía completa para el uso avanzado de servidores MCP, cubriendo arquitecturas de servidor regulares y de bajo nivel.
  - **Servidor Regular vs. de Bajo Nivel**: Comparación detallada y ejemplos de código en Python y TypeScript para ambos enfoques.
  - **Diseño Basado en Handlers**: Explicación de gestión basada en handlers para herramientas/recursos/prompts para implementaciones escalables y flexibles de servidor.
  - **Patrones Prácticos**: Escenarios del mundo real donde los patrones de servidor de bajo nivel son beneficiosos para funciones y arquitectura avanzadas.

#### Autenticación Simple (03-GettingStarted/11-simple-auth)
- **Nuevo Capítulo Añadido**: Guía paso a paso para implementar autenticación simple en servidores MCP.
  - **Conceptos de Auth**: Explicación clara de autenticación vs. autorización, y manejo de credenciales.
  - **Implementación de Autenticación Básica**: Patrones de autenticación basados en middleware en Python (Starlette) y TypeScript (Express), con ejemplos de código.
  - **Progresión hacia Seguridad Avanzada**: Orientación sobre comenzar con autenticación simple y avanzar hacia OAuth 2.1 y RBAC, con referencias a módulos de seguridad avanzada.

Estas adiciones proveen una guía práctica y aplicada para construir implementaciones de servidores MCP más robustas, seguras y flexibles, conectando conceptos fundamentales con patrones avanzados de producción.

## 29 de septiembre de 2025

### Laboratorios de Integración de Base de Datos en Servidores MCP – Ruta de Aprendizaje Práctica Integral

#### 11-MCPServerHandsOnLabs – Nuevo Currículo Completo de Integración de Base de Datos
- **Ruta de Aprendizaje Completa de 13 Laboratorios**: Añadido currículo exhaustivo y práctico para crear servidores MCP listos para producción con integración de base de datos PostgreSQL
  - **Implementación en el Mundo Real**: Caso de uso de análisis retail de Zava demostrando patrones de nivel empresarial
  - **Progresión de Aprendizaje Estructurada**:
    - **Labs 00-03: Fundamentos** - Introducción, Arquitectura Core, Seguridad y Multi-Tenancy, Configuración de Entorno
    - **Labs 04-06: Construcción del Servidor MCP** - Diseño y Esquema de Base de Datos, Implementación del Servidor MCP, Desarrollo de Herramientas  
    - **Labs 07-09: Funciones Avanzadas** - Integración de Búsqueda Semántica, Pruebas y Depuración, Integración con VS Code
    - **Labs 10-12: Producción y Mejores Prácticas** - Estrategias de Despliegue, Monitoreo y Observabilidad, Mejores Prácticas y Optimización
  - **Tecnologías Empresariales**: Framework FastMCP, PostgreSQL con pgvector, incrustaciones Azure OpenAI, Azure Container Apps, Application Insights
  - **Funciones Avanzadas**: Row Level Security (RLS), búsqueda semántica, acceso multi-inquilino a datos, vector embeddings, monitoreo en tiempo real

#### Estandarización Terminológica - Conversión de Módulo a Laboratorio
- **Actualización Integral de Documentación**: Actualizados sistemáticamente todos los archivos README en 11-MCPServerHandsOnLabs para usar la terminología "Laboratorio" en lugar de "Módulo"
  - **Encabezados de Sección**: Actualizado "What This Module Covers" a "What This Lab Covers" en todos los 13 laboratorios
  - **Descripción de Contenido**: Cambiado "This module provides..." a "This lab provides..." a lo largo de la documentación
  - **Objetivos de Aprendizaje**: Actualizado "By the end of this module..." a "By the end of this lab..." 
  - **Enlaces de Navegación**: Convertidas todas las referencias "Module XX:" a "Lab XX:" en cross-references y navegación
  - **Seguimiento de Finalización**: Actualizado "After completing this module..." a "After completing this lab..."
  - **Referencias Técnicas Conservadas**: Mantenidas referencias a módulos Python en archivos de configuración (p. ej., `"module": "mcp_server.main"`)

#### Mejoras en la Guía de Estudio (study_guide.md)
- **Mapa Visual del Currículo**: Añadida nueva sección "11. Database Integration Labs" con visualización de estructura integral de laboratorios
- **Estructura del Repositorio**: Actualizado de diez a once secciones principales con descripción detallada de 11-MCPServerHandsOnLabs
- **Orientación en la Ruta de Aprendizaje**: Mejoradas las instrucciones de navegación para cubrir las secciones 00-11
- **Cobertura Tecnológica**: Añadidos detalles de integración FastMCP, PostgreSQL y servicios Azure
- **Resultados de Aprendizaje**: Enfatizado desarrollo de servidores listos para producción, patrones de integración de base de datos y seguridad empresarial

#### Mejoras en la Estructura del README Principal
- **Terminología Basada en Laboratorios**: Actualizado README.md principal en 11-MCPServerHandsOnLabs para usar consistentemente estructura "Laboratorio"
- **Organización de Ruta de Aprendizaje**: Progresión clara desde conceptos fundamentales hasta implementación avanzada y despliegue en producción
- **Enfoque en el Mundo Real**: Énfasis en aprendizaje práctico y aplicado con patrones y tecnologías de nivel empresarial

### Mejoras en Calidad y Consistencia de Documentación
- **Enfoque Práctico Laboratorio**: Reforzada aproximación práctica basada en laboratorios en toda la documentación
- **Enfoque en Patrones Empresariales**: Destacadas implementaciones listas para producción y consideraciones de seguridad empresarial
- **Integración Tecnológica**: Cobertura integral de servicios Azure modernos y patrones de integración IA
- **Progresión de Aprendizaje**: Ruta clara y estructurada desde conceptos básicos hasta despliegue en producción

## 26 de septiembre de 2025

### Mejora de Estudios de Caso - Integración de GitHub MCP Registry

#### Estudios de Caso (09-CaseStudy/) - Enfoque en Desarrollo del Ecosistema
- **README.md**: Gran ampliación con estudio de caso exhaustivo sobre GitHub MCP Registry
  - **Estudio de Caso GitHub MCP Registry**: Nuevo estudio de caso completo examinando el lanzamiento del MCP Registry de GitHub en septiembre de 2025
    - **Análisis del Problema**: Examen detallado de retos fragmentados en descubrimiento y despliegue de servidores MCP
    - **Arquitectura de la Solución**: Enfoque en el registro centralizado de GitHub con instalación con un clic en VS Code
    - **Impacto de Negocio**: Mejoras medibles en incorporación y productividad de desarrolladores
    - **Valor Estratégico**: Enfoque en despliegue modular de agentes e interoperabilidad entre herramientas
    - **Desarrollo del Ecosistema**: Posicionamiento como plataforma fundacional para integración agentic
  - **Estructura Mejorada de Estudios de Caso**: Actualizados los siete estudios de caso con formato consistente y descripciones exhaustivas
    - Azure AI Travel Agents: Énfasis en orquestación multi-agente
    - Integración Azure DevOps: Foco en automatización de flujos de trabajo
    - Recuperación de Documentación en Tiempo Real: Implementación de cliente consola Python
    - Generador Interactivo de Plan de Estudios: Aplicación web de conversación Chainlit
    - Documentación en el Editor: Integración VS Code y GitHub Copilot
    - Azure API Management: Patrones de integración de API empresarial
    - GitHub MCP Registry: Desarrollo del ecosistema y plataforma comunitaria
  - **Conclusión Integral**: Sección de conclusión reescrita destacando siete estudios de caso abarcando múltiples dimensiones de implementación MCP
    - Integración Empresarial, Orquestación Multi-Agente, Productividad del Desarrollador
    - Desarrollo de Ecosistema, Aplicaciones Educativas como categorías
    - Perspectivas mejoradas sobre patrones arquitectónicos, estrategias de implementación y mejores prácticas
    - Énfasis en MCP como protocolo maduro y listo para producción

#### Actualizaciones en la Guía de Estudio (study_guide.md)
- **Mapa Visual del Currículo**: Actualizado mindmap para incluir GitHub MCP Registry en sección Estudios de Caso
- **Descripción de Estudios de Caso**: Mejorada desde descripciones genéricas a desglose detallado de siete casos integrales
- **Estructura del Repositorio**: Actualizada sección 10 para reflejar cobertura exhaustiva de estudios de caso con detalles específicos de implementación
- **Integración del Changelog**: Añadida entrada del 26 de septiembre de 2025 documentando adición de GitHub MCP Registry y mejoras en estudios de caso
- **Actualización de Fechas**: Actualizada marca de tiempo del pie de página para reflejar la última revisión (26 de septiembre de 2025)

### Mejoras en Calidad de Documentación
- **Mejora de Consistencia**: Formato y estructura de estudios de caso estandarizados en los siete ejemplos
- **Cobertura Integral**: Estudios de caso ahora abarcan escenarios empresariales, productividad desarrollador y desarrollo de ecosistemas
- **Posicionamiento Estratégico**: Enfoque mejorado en MCP como plataforma base para despliegue de sistemas agentic
- **Integración de Recursos**: Actualizados recursos adicionales para incluir enlace a GitHub MCP Registry

## 15 de septiembre de 2025

### Expansión de Temas Avanzados - Transportes Personalizados e Ingeniería de Contexto

#### Transportes Personalizados MCP (05-AdvancedTopics/mcp-transport/) - Nueva Guía Avanzada de Implementación
- **README.md**: Guía completa de implementación para mecanismos de transporte MCP personalizados
  - **Transporte Azure Event Grid**: Implementación exhaustiva de transporte serverless basado en eventos
    - Ejemplos en C#, TypeScript y Python con integración Azure Functions
    - Patrones de arquitectura orientada a eventos para soluciones MCP escalables
    - Receptores webhook y manejo de mensajes push
  - **Transporte Azure Event Hubs**: Implementación de transporte streaming de alto rendimiento
    - Capacidades de streaming en tiempo real para escenarios de baja latencia
    - Estrategias de particionado y gestión de checkpoints
    - Agrupación de mensajes y optimización de rendimiento
  - **Patrones de Integración Empresarial**: Ejemplos arquitectónicos listos para producción
    - Procesamiento MCP distribuido a través de múltiples Azure Functions
    - Arquitecturas híbridas de transporte combinando múltiples tipos
    - Estrategias para durabilidad, confiabilidad y manejo de errores en mensajes
  - **Seguridad y Monitoreo**: Integración Azure Key Vault y patrones de observabilidad
    - Autenticación mediante identidad administrada y acceso de mínimo privilegio
    - Telemetría y monitoreo de rendimiento con Application Insights
    - Circuit breakers y patrones de tolerancia a fallos
  - **Frameworks de Pruebas**: Estrategias completas de pruebas para transportes personalizados
    - Pruebas unitarias con test doubles y frameworks de mocking
    - Pruebas de integración con Azure Test Containers
    - Consideraciones de pruebas de rendimiento y carga

#### Ingeniería de Contexto (05-AdvancedTopics/mcp-contextengineering/) - Disciplina Emergente en IA
- **README.md**: Exploración exhaustiva de la ingeniería de contexto como campo emergente
  - **Principios Básicos**: Compartición completa de contexto, conciencia de decisiones de acción y gestión de ventana de contexto
  - **Alineación con MCP**: Cómo el diseño MCP aborda desafíos de ingeniería de contexto
    - Limitaciones de ventana de contexto y estrategias de carga progresiva
    - Determinación de relevancia y recuperación dinámica de contexto
    - Manejo multimodal de contexto y consideraciones de seguridad
  - **Enfoques de Implementación**: Arquitecturas mono-hilo vs. multiagente
    - Segmentación y priorización de contexto
    - Carga progresiva y estrategias de compresión de contexto
    - Enfoques en capas y optimización de recuperación
  - **Marco de Medición**: Métricas emergentes para evaluación de efectividad de contexto
    - Eficiencia de entrada, rendimiento, calidad y consideraciones de experiencia de usuario
    - Enfoques experimentales para optimización de contexto
    - Análisis de fallos y metodologías de mejora

#### Actualizaciones en Navegación del Currículo (README.md)
- **Estructura de Módulos Mejorada**: Actualizada tabla curricular para incluir nuevos temas avanzados
  - Añadidos Context Engineering (5.14) y Custom Transport (5.15)
  - Formato consistente y enlaces de navegación en todos los módulos
  - Descripciones actualizadas para reflejar alcance actual del contenido

### Mejoras en Estructura de Directorios
- **Estandarización de Nombres**: Renombrado "mcp transport" a "mcp-transport" para consistencia con otras carpetas de temas avanzados
- **Organización de Contenido**: Todas las carpetas 05-AdvancedTopics ahora siguen patrón de nombres consistente (mcp-[tema])

### Mejoras en Calidad de Documentación
- **Alineación con Especificación MCP**: Todo el contenido nuevo referencia la Especificación MCP actual 2025-06-18
- **Ejemplos Multilenguaje**: Ejemplos de código completos en C#, TypeScript y Python
- **Enfoque Empresarial**: Patrones listos para producción e integración en nube Azure a lo largo del contenido
- **Documentación Visual**: Diagramas Mermaid para visualización de arquitectura y flujos

## 18 de agosto de 2025

### Actualización Integral de Documentación - Estándares MCP 2025-06-18

#### Mejores Prácticas de Seguridad MCP (02-Security/) - Modernización Completa
- **MCP-SECURITY-BEST-PRACTICES-2025.md**: Reescritura completa alineada con la Especificación MCP 2025-06-18  
  - **Requisitos Obligatorios**: Añadidos requisitos explícitos DEBE/NO DEBE de la especificación oficial con indicadores visuales claros  
  - **12 Prácticas de Seguridad Clave**: Reestructurado de lista de 15 ítems a dominios de seguridad comprensivos  
    - Seguridad de Tokens y Autenticación con integración de proveedor de identidad externo  
    - Gestión de Sesiones y Seguridad del Transporte con requisitos criptográficos  
    - Protección Específica contra Amenazas de IA con integración de Microsoft Prompt Shields  
    - Control de Acceso y Permisos con principio de menor privilegio  
    - Seguridad y Monitoreo de Contenidos con integración de Azure Content Safety  
    - Seguridad de la Cadena de Suministro con verificación integral de componentes  
    - Seguridad OAuth y Prevención de Confused Deputy con implementación de PKCE  
    - Respuesta y Recuperación de Incidentes con capacidades automatizadas  
    - Cumplimiento y Gobernanza con alineación regulatoria  
    - Controles Avanzados de Seguridad con arquitectura de zero trust  
    - Integración del Ecosistema de Seguridad Microsoft con soluciones comprensivas  
    - Evolución Continua de la Seguridad con prácticas adaptativas  
  - **Soluciones de Seguridad Microsoft**: Guía mejorada para integración de Prompt Shields, Azure Content Safety, Entra ID y GitHub Advanced Security  
  - **Recursos de Implementación**: Enlaces categorizados de recursos completos por Documentación Oficial MCP, Soluciones de Seguridad Microsoft, Estándares de Seguridad y Guías de Implementación  

#### Controles Avanzados de Seguridad (02-Security/) - Implementación Empresarial  
- **MCP-SECURITY-CONTROLS-2025.md**: Renovación completa con marco de seguridad a nivel empresarial  
  - **9 Dominios de Seguridad Comprensivos**: Ampliado desde controles básicos a marco detallado empresarial  
    - Autenticación y Autorización Avanzada con integración Microsoft Entra ID  
    - Seguridad de Tokens y Controles Anti-Passthrough con validación integral  
    - Controles de Seguridad de Sesión con prevención de secuestros  
    - Controles de Seguridad Específicos para IA con prevención de inyección de prompts y envenenamiento de herramientas  
    - Prevención de Ataques Confused Deputy con seguridad en proxy OAuth  
    - Seguridad en la Ejecución de Herramientas mediante sandboxing y aislamiento  
    - Controles de Seguridad de Cadena de Suministro con verificación de dependencias  
    - Controles de Monitoreo y Detección con integración SIEM  
    - Respuesta y Recuperación de Incidentes con capacidades automatizadas  
  - **Ejemplos de Implementación**: Añadidos bloques de configuración YAML detallados y ejemplos de código  
  - **Integración de Soluciones Microsoft**: Cobertura comprensiva de servicios de seguridad Azure, GitHub Advanced Security y gestión de identidad empresarial  

#### Temas Avanzados de Seguridad (05-AdvancedTopics/mcp-security/) - Implementación lista para producción  
- **README.md**: Reescritura completa para implementación de seguridad empresarial  
  - **Alineación con Especificación Actual**: Actualizado a Especificación MCP 2025-06-18 con requisitos mandatorios de seguridad  
  - **Autenticación Mejorada**: Integración Microsoft Entra ID con ejemplos completos en .NET y Java Spring Security  
  - **Integración de Seguridad IA**: Implementación Microsoft Prompt Shields y Azure Content Safety con ejemplos detallados en Python  
  - **Mitigación Avanzada de Amenazas**: Ejemplos comprensivos para  
    - Prevención de Ataques Confused Deputy con PKCE y validación de consentimiento de usuario  
    - Prevención de Passthrough de Tokens con validación de audiencia y gestión segura de tokens  
    - Prevención de Secuestro de Sesión con enlace criptográfico y análisis conductual  
  - **Integración de Seguridad Empresarial**: Monitoreo Azure Application Insights, pipelines de detección de amenazas y seguridad de cadena de suministro  
  - **Lista de Verificación de Implementación**: Clarificación de controles mandatorios vs. recomendados con beneficios del ecosistema de seguridad Microsoft  

### Calidad y Alineación de la Documentación  
- **Referencias a la Especificación**: Actualizadas todas las referencias a Especificación MCP 2025-06-18  
- **Ecosistema de Seguridad Microsoft**: Guía de integración mejorada en toda la documentación de seguridad  
- **Implementación Práctica**: Añadidos ejemplos detallados en .NET, Java y Python con patrones empresariales  
- **Organización de Recursos**: Categorización comprensiva de documentación oficial, estándares de seguridad y guías de implementación  
- **Indicadores Visuales**: Marcas claras de requisitos obligatorios vs. prácticas recomendadas  

#### Conceptos Clave (01-CoreConcepts/) - Modernización Completa  
- **Actualización de Versión del Protocolo**: Referenciado a la Especificación MCP actual 2025-06-18 con versión basada en fecha (formato AAAA-MM-DD)  
- **Refinamiento de Arquitectura**: Descripciones mejoradas de Hosts, Clientes y Servidores para reflejar patrones actuales MCP  
  - Hosts definidos ahora claramente como aplicaciones IA que coordinan múltiples conexiones de clientes MCP  
  - Clientes descritos como conectores de protocolo manteniendo relaciones uno a uno con servidores  
  - Servidores mejorados con escenarios de despliegue locales y remotos  
- **Reestructuración de Primitivas**: Renovación completa de primitivas de servidor y cliente  
  - Primitivas de Servidor: Recursos (fuentes de datos), Prompts (plantillas), Herramientas (funciones ejecutables) con explicaciones y ejemplos detallados  
  - Primitivas de Cliente: Muestreo (respuestas LLM), Elicitación (entrada del usuario), Registro (depuración/monitoreo)  
  - Actualizado con patrones actuales de métodos discovery (`*/list`), retrieval (`*/get`) y execution (`*/call`)  
- **Arquitectura del Protocolo**: Introducido modelo de arquitectura en dos capas  
  - Capa de Datos: Fundamento JSON-RPC 2.0 con gestión de ciclo de vida y primitivas  
  - Capa de Transporte: STDIO (local) y HTTP Streamable con SSE (transporte remoto)  
- **Marco de Seguridad**: Principios comprensivos de seguridad incluyendo consentimiento explícito del usuario, protección de privacidad de datos, seguridad en ejecución de herramientas y seguridad de capa de transporte  
- **Patrones de Comunicación**: Actualizados mensajes del protocolo para mostrar flujos de inicialización, descubrimiento, ejecución y notificaciones  
- **Ejemplos de Código**: Actualización de ejemplos multilenguaje (.NET, Java, Python, JavaScript) para reflejar patrones MCP SDK actuales  

#### Seguridad (02-Security/) - Renovación Completa de Seguridad  
- **Alineación con Estándares**: Total alineación con requisitos de seguridad de Especificación MCP 2025-06-18  
- **Evolución de Autenticación**: Documentada evolución desde servidores OAuth personalizados a delegación a proveedor de identidad externo (Microsoft Entra ID)  
- **Análisis de Amenazas Específicas para IA**: Cobertura mejorada de vectores modernos de ataque IA  
  - Escenarios detallados de ataques de inyección de prompts con ejemplos reales  
  - Mecanismos de envenenamiento de herramientas y patrones de ataque “rug pull”  
  - Envenenamiento de contexto y ataques de confusión de modelo  
- **Soluciones de Seguridad Microsoft para IA**: Cobertura comprensiva del ecosistema de seguridad Microsoft  
  - AI Prompt Shields con técnicas avanzadas de detección, spotlighting y delimitadores  
  - Patrones de integración Azure Content Safety  
  - GitHub Advanced Security para protección de cadena de suministro  
- **Mitigación Avanzada de Amenazas**: Controles detallados para  
  - Secuestro de sesión con escenarios MCP específicos y requerimientos criptográficos para ID de sesión  
  - Problemas Confused Deputy en escenarios proxy MCP con requisitos de consentimiento explícito  
  - Vulnerabilidades de passthrough de tokens con controles mandatorios de validación  
- **Seguridad de la Cadena de Suministro**: Cobertura ampliada de cadena de suministro IA incluyendo modelos base, servicios de embeddings, proveedores de contexto y APIs de terceros  
- **Seguridad de la Fundación**: Integración mejorada con patrones empresariales de seguridad incluyendo arquitectura zero trust y ecosistema de seguridad Microsoft  
- **Organización de Recursos**: Enlaces categorizados comprensivos por tipo (Documentación Oficial, Estándares, Investigación, Soluciones Microsoft, Guías de Implementación)  

### Mejoras en la Calidad de la Documentación  
- **Objetivos de Aprendizaje Estructurados**: Objetivos de aprendizaje mejorados con resultados específicos y accionables  
- **Referencias Cruzadas**: Añadidos enlaces entre temas relacionados de seguridad y conceptos clave  
- **Información Actualizada**: Actualizadas todas las referencias de fechas y enlaces de especificación a estándares actuales  
- **Guías de Implementación**: Añadidas directrices específicas y accionables de implementación en ambas secciones  

## 16 de julio de 2025  

### Mejoras en README y Navegación  
- Navegación del currículo rediseñada completamente en README.md  
- Reemplazadas etiquetas `<details>` por formato tabular más accesible  
- Creación de opciones de diseño alternativas en nueva carpeta "alternative_layouts"  
- Añadidos ejemplos de navegación basada en tarjetas, con pestañas y acordeón  
- Actualizada sección de estructura del repositorio para incluir todos los archivos más recientes  
- Mejorada sección "Cómo Usar Este Currículo" con recomendaciones claras  
- Actualizados enlaces a la especificación MCP apuntando a URLs correctas  
- Añadida sección de Ingeniería de Contexto (5.14) a la estructura curricular  

### Actualizaciones de la Guía de Estudio  
- Guía de estudio revisada completamente para alinear con estructura de repositorio actual  
- Añadidas nuevas secciones para Clientes y Herramientas MCP, y Servidores MCP Populares  
- Actualizado el Mapa Visual del Currículo para reflejar con precisión todos los temas  
- Mejoradas descripciones de Temas Avanzados para cubrir todas las áreas especializadas  
- Actualizada sección de Estudios de Caso para reflejar ejemplos reales  
- Añadido este registro completo de cambios  

### Contribuciones de la Comunidad (06-CommunityContributions/)  
- Añadida información detallada sobre servidores MCP para generación de imágenes  
- Añadida sección comprensiva sobre uso de Claude en VSCode  
- Añadidas instrucciones de configuración y uso del cliente terminal Cline  
- Actualizada sección de clientes MCP para incluir todas las opciones populares  
- Mejorados ejemplos de contribución con muestras de código más precisas  

### Temas Avanzados (05-AdvancedTopics/)  
- Organización de todas las carpetas de temas especializados con nomenclatura consistente  
- Añadidos materiales y ejemplos de ingeniería de contexto  
- Añadida documentación de integración del agente Foundry  
- Mejorada documentación de integración de seguridad Entra ID  

## 11 de junio de 2025  

### Creación Inicial  
- Lanzada primera versión del currículo MCP para Principiantes  
- Creada estructura básica para las 10 secciones principales  
- Implementado Mapa Visual del Currículo para navegación  
- Añadidos proyectos muestra iniciales en múltiples lenguajes de programación  

### Primeros Pasos (03-GettingStarted/)  
- Creación de primeros ejemplos de implementación de servidor  
- Añadida guía para desarrollo de clientes  
- Incluidas instrucciones de integración de clientes LLM  
- Añadida documentación de integración VS Code  
- Implementados ejemplos de servidor con Server-Sent Events (SSE)  

### Conceptos Clave (01-CoreConcepts/)  
- Añadida explicación detallada de arquitectura cliente-servidor  
- Creada documentación sobre componentes clave del protocolo  
- Documentados patrones de mensajería en MCP  

## 23 de mayo de 2025  

### Estructura del Repositorio  
- Inicializado repositorio con estructura básica de carpetas  
- Creados archivos README para cada sección principal  
- Configurada infraestructura para traducción  
- Añadidos recursos gráficos y diagramas  

### Documentación  
- Creado README.md inicial con visión general del currículo  
- Añadidos CODE_OF_CONDUCT.md y SECURITY.md  
- Configurado SUPPORT.md con guía para obtener ayuda  
- Creada estructura preliminar de guía de estudio  

## 15 de abril de 2025  

### Planificación y Marco  
- Planificación inicial para currículo MCP para Principiantes  
- Definición de objetivos de aprendizaje y público objetivo  
- Esbozado estructura de 10 secciones del currículo  
- Desarrollado marco conceptual para ejemplos y estudios de caso  
- Creación de prototipos iniciales para conceptos clave

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso legal**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda traducción profesional humana. No nos hacemos responsables de malentendidos o interpretaciones erróneas derivadas del uso de esta traducción.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->