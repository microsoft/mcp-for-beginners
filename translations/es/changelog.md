# Registro de cambios: Currículo MCP para principiantes

Este documento sirve como un registro de todos los cambios significativos realizados en el currículo del Protocolo de Contexto de Modelo (MCP) para principiantes. Los cambios se documentan en orden cronológico inverso (los cambios más recientes primero).

## 18 de diciembre de 2025

### Actualización de documentación de seguridad - Especificación MCP 2025-11-25

#### Mejores prácticas de seguridad MCP (02-Security/mcp-best-practices.md) - Actualización de versión de especificación
- **Actualización de versión del protocolo**: Actualizado para referenciar la última Especificación MCP 2025-11-25 (publicada el 25 de noviembre de 2025)
  - Actualizadas todas las referencias de versión de especificación de 2025-06-18 a 2025-11-25
  - Actualizadas las referencias de fecha del documento de 18 de agosto de 2025 a 18 de diciembre de 2025
  - Verificados todos los URLs de especificación que apuntan a la documentación actual
- **Validación de contenido**: Validación exhaustiva de las mejores prácticas de seguridad contra los estándares más recientes
  - **Soluciones de seguridad de Microsoft**: Verificada la terminología actual y enlaces para Prompt Shields (anteriormente "detección de riesgo de jailbreak"), Azure Content Safety, Microsoft Entra ID y Azure Key Vault
  - **Seguridad OAuth 2.1**: Confirmada la alineación con las mejores prácticas de seguridad OAuth más recientes
  - **Estándares OWASP**: Validadas las referencias a OWASP Top 10 para LLMs que permanecen actuales
  - **Servicios Azure**: Verificados todos los enlaces a documentación y mejores prácticas de Microsoft Azure
- **Alineación con estándares**: Confirmados todos los estándares de seguridad referenciados como actuales
  - Marco de gestión de riesgos de IA de NIST
  - ISO 27001:2022
  - Mejores prácticas de seguridad OAuth 2.1
  - Marcos de seguridad y cumplimiento de Azure
- **Recursos de implementación**: Verificados todos los enlaces y recursos de guías de implementación
  - Patrones de autenticación de Azure API Management
  - Guías de integración de Microsoft Entra ID
  - Gestión de secretos con Azure Key Vault
  - Pipelines y soluciones de monitoreo DevSecOps

### Aseguramiento de calidad de la documentación
- **Cumplimiento de especificación**: Asegurado que todos los requisitos obligatorios de seguridad MCP (DEBE/NO DEBE) estén alineados con la última especificación
- **Actualización de recursos**: Verificados todos los enlaces externos a documentación de Microsoft, estándares de seguridad y guías de implementación
- **Cobertura de mejores prácticas**: Confirmada cobertura integral de autenticación, autorización, amenazas específicas de IA, seguridad de la cadena de suministro y patrones empresariales

## 6 de octubre de 2025

### Expansión de la sección de introducción – Uso avanzado del servidor y autenticación simple

#### Uso avanzado del servidor (03-GettingStarted/10-advanced)
- **Nuevo capítulo agregado**: Introducción de una guía completa para el uso avanzado del servidor MCP, cubriendo arquitecturas de servidor regulares y de bajo nivel.
  - **Servidor regular vs. de bajo nivel**: Comparación detallada y ejemplos de código en Python y TypeScript para ambos enfoques.
  - **Diseño basado en manejadores**: Explicación de la gestión basada en manejadores de herramientas/recursos/prompt para implementaciones de servidor escalables y flexibles.
  - **Patrones prácticos**: Escenarios del mundo real donde los patrones de servidor de bajo nivel son beneficiosos para características y arquitecturas avanzadas.

#### Autenticación simple (03-GettingStarted/11-simple-auth)
- **Nuevo capítulo agregado**: Guía paso a paso para implementar autenticación simple en servidores MCP.
  - **Conceptos de autenticación**: Explicación clara de autenticación vs. autorización y manejo de credenciales.
  - **Implementación básica de autenticación**: Patrones de autenticación basados en middleware en Python (Starlette) y TypeScript (Express), con ejemplos de código.
  - **Progresión hacia seguridad avanzada**: Orientación para comenzar con autenticación simple y avanzar hacia OAuth 2.1 y RBAC, con referencias a módulos de seguridad avanzada.

Estas adiciones proporcionan orientación práctica y aplicada para construir implementaciones de servidores MCP más robustas, seguras y flexibles, conectando conceptos fundamentales con patrones avanzados de producción.

## 29 de septiembre de 2025

### Laboratorios de integración de base de datos del servidor MCP - Ruta de aprendizaje práctica integral

#### 11-MCPServerHandsOnLabs - Nuevo currículo completo de integración de base de datos
- **Ruta de aprendizaje completa de 13 laboratorios**: Añadido currículo práctico integral para construir servidores MCP listos para producción con integración de base de datos PostgreSQL
  - **Implementación del mundo real**: Caso de uso de análisis minorista Zava demostrando patrones de nivel empresarial
  - **Progresión estructurada de aprendizaje**:
    - **Laboratorios 00-03: Fundamentos** - Introducción, Arquitectura central, Seguridad y multi-inquilino, Configuración del entorno
    - **Laboratorios 04-06: Construcción del servidor MCP** - Diseño y esquema de base de datos, Implementación del servidor MCP, Desarrollo de herramientas  
    - **Laboratorios 07-09: Características avanzadas** - Integración de búsqueda semántica, Pruebas y depuración, Integración con VS Code
    - **Laboratorios 10-12: Producción y mejores prácticas** - Estrategias de despliegue, Monitoreo y observabilidad, Mejores prácticas y optimización
  - **Tecnologías empresariales**: Framework FastMCP, PostgreSQL con pgvector, embeddings de Azure OpenAI, Azure Container Apps, Application Insights
  - **Características avanzadas**: Seguridad a nivel de fila (RLS), búsqueda semántica, acceso a datos multi-inquilino, embeddings vectoriales, monitoreo en tiempo real

#### Estandarización de terminología - Conversión de módulo a laboratorio
- **Actualización integral de documentación**: Actualizados sistemáticamente todos los archivos README en 11-MCPServerHandsOnLabs para usar la terminología "Laboratorio" en lugar de "Módulo"
  - **Encabezados de sección**: Actualizado "Lo que cubre este módulo" a "Lo que cubre este laboratorio" en los 13 laboratorios
  - **Descripción del contenido**: Cambiado "Este módulo proporciona..." a "Este laboratorio proporciona..." en toda la documentación
  - **Objetivos de aprendizaje**: Actualizado "Al final de este módulo..." a "Al final de este laboratorio..."
  - **Enlaces de navegación**: Convertidas todas las referencias "Módulo XX:" a "Laboratorio XX:" en referencias cruzadas y navegación
  - **Seguimiento de finalización**: Actualizado "Después de completar este módulo..." a "Después de completar este laboratorio..."
  - **Referencias técnicas preservadas**: Mantenidas referencias a módulos Python en archivos de configuración (por ejemplo, `"module": "mcp_server.main"`)

#### Mejora de la guía de estudio (study_guide.md)
- **Mapa visual del currículo**: Añadida nueva sección "11. Laboratorios de integración de base de datos" con visualización completa de la estructura de laboratorios
- **Estructura del repositorio**: Actualizada de diez a once secciones principales con descripción detallada de 11-MCPServerHandsOnLabs
- **Orientación de ruta de aprendizaje**: Mejoradas instrucciones de navegación para cubrir secciones 00-11
- **Cobertura tecnológica**: Añadidos detalles de integración de FastMCP, PostgreSQL y servicios Azure
- **Resultados de aprendizaje**: Enfatizado desarrollo de servidores listos para producción, patrones de integración de base de datos y seguridad empresarial

#### Mejora de la estructura del README principal
- **Terminología basada en laboratorios**: Actualizado README.md principal en 11-MCPServerHandsOnLabs para usar consistentemente la estructura "Laboratorio"
- **Organización de la ruta de aprendizaje**: Progresión clara desde conceptos fundamentales hasta implementación avanzada y despliegue en producción
- **Enfoque en el mundo real**: Énfasis en aprendizaje práctico con patrones y tecnologías de nivel empresarial

### Mejoras en calidad y consistencia de la documentación
- **Énfasis en aprendizaje práctico**: Reforzado enfoque basado en laboratorios a lo largo de la documentación
- **Enfoque en patrones empresariales**: Destacadas implementaciones listas para producción y consideraciones de seguridad empresarial
- **Integración tecnológica**: Cobertura integral de servicios modernos de Azure y patrones de integración de IA
- **Progresión de aprendizaje**: Ruta clara y estructurada desde conceptos básicos hasta despliegue en producción

## 26 de septiembre de 2025

### Mejora de estudios de caso - Integración del registro MCP de GitHub

#### Estudios de caso (09-CaseStudy/) - Enfoque en desarrollo del ecosistema
- **README.md**: Expansión mayor con estudio de caso integral del registro MCP de GitHub
  - **Estudio de caso del registro MCP de GitHub**: Nuevo estudio de caso completo que examina el lanzamiento del registro MCP de GitHub en septiembre de 2025
    - **Análisis del problema**: Examen detallado de los desafíos fragmentados en descubrimiento y despliegue de servidores MCP
    - **Arquitectura de la solución**: Enfoque centralizado del registro de GitHub con instalación con un clic en VS Code
    - **Impacto comercial**: Mejoras medibles en incorporación y productividad de desarrolladores
    - **Valor estratégico**: Enfoque en despliegue modular de agentes e interoperabilidad entre herramientas
    - **Desarrollo del ecosistema**: Posicionamiento como plataforma fundamental para integración agentica
  - **Estructura mejorada del estudio de caso**: Actualizados los siete estudios de caso con formato consistente y descripciones completas
    - Agentes de viaje AI de Azure: Énfasis en orquestación multi-agente
    - Integración Azure DevOps: Enfoque en automatización de flujos de trabajo
    - Recuperación de documentación en tiempo real: Implementación de cliente consola Python
    - Generador interactivo de planes de estudio: Aplicación web conversacional Chainlit
    - Documentación en editor: Integración VS Code y GitHub Copilot
    - Azure API Management: Patrones de integración de API empresariales
    - Registro MCP de GitHub: Desarrollo del ecosistema y plataforma comunitaria
  - **Conclusión integral**: Sección de conclusión reescrita destacando siete estudios de caso que abarcan múltiples dimensiones de implementación MCP
    - Integración empresarial, orquestación multi-agente, productividad del desarrollador
    - Desarrollo del ecosistema, aplicaciones educativas categorizadas
    - Perspectivas mejoradas sobre patrones arquitectónicos, estrategias de implementación y mejores prácticas
    - Énfasis en MCP como protocolo maduro y listo para producción

#### Actualizaciones de la guía de estudio (study_guide.md)
- **Mapa visual del currículo**: Actualizado mapa mental para incluir el registro MCP de GitHub en la sección de estudios de caso
- **Descripción de estudios de caso**: Mejorada de descripciones genéricas a desglose detallado de siete estudios de caso completos
- **Estructura del repositorio**: Actualizada sección 10 para reflejar cobertura integral de estudios de caso con detalles específicos de implementación
- **Integración en el registro de cambios**: Añadida entrada del 26 de septiembre de 2025 documentando la adición del registro MCP de GitHub y mejoras en estudios de caso
- **Actualización de fechas**: Actualizado sello de tiempo en el pie de página para reflejar la última revisión (26 de septiembre de 2025)

### Mejoras en calidad de documentación
- **Mejora de consistencia**: Estandarizado formato y estructura de estudios de caso en los siete ejemplos
- **Cobertura integral**: Estudios de caso ahora abarcan escenarios empresariales, productividad del desarrollador y desarrollo del ecosistema
- **Posicionamiento estratégico**: Enfoque mejorado en MCP como plataforma fundamental para despliegue de sistemas agenticos
- **Integración de recursos**: Actualizados recursos adicionales para incluir enlace al registro MCP de GitHub

## 15 de septiembre de 2025

### Expansión de temas avanzados - Transportes personalizados e ingeniería de contexto

#### Transportes personalizados MCP (05-AdvancedTopics/mcp-transport/) - Nueva guía avanzada de implementación
- **README.md**: Guía completa de implementación para mecanismos de transporte MCP personalizados
  - **Transporte Azure Event Grid**: Implementación completa de transporte sin servidor basado en eventos
    - Ejemplos en C#, TypeScript y Python con integración de Azure Functions
    - Patrones de arquitectura basada en eventos para soluciones MCP escalables
    - Receptores webhook y manejo de mensajes push
  - **Transporte Azure Event Hubs**: Implementación de transporte de streaming de alto rendimiento
    - Capacidades de streaming en tiempo real para escenarios de baja latencia
    - Estrategias de particionamiento y gestión de puntos de control
    - Agrupación de mensajes y optimización de rendimiento
  - **Patrones de integración empresarial**: Ejemplos arquitectónicos listos para producción
    - Procesamiento MCP distribuido a través de múltiples Azure Functions
    - Arquitecturas híbridas de transporte combinando múltiples tipos
    - Durabilidad, confiabilidad y manejo de errores de mensajes
  - **Seguridad y monitoreo**: Integración con Azure Key Vault y patrones de observabilidad
    - Autenticación con identidad administrada y acceso de mínimo privilegio
    - Telemetría de Application Insights y monitoreo de rendimiento
    - Interruptores de circuito y patrones de tolerancia a fallos
  - **Frameworks de prueba**: Estrategias completas de pruebas para transportes personalizados
    - Pruebas unitarias con dobles de prueba y frameworks de simulación
    - Pruebas de integración con Azure Test Containers
    - Consideraciones para pruebas de rendimiento y carga

#### Ingeniería de contexto (05-AdvancedTopics/mcp-contextengineering/) - Disciplina emergente de IA
- **README.md**: Exploración completa de la ingeniería de contexto como campo emergente
  - **Principios fundamentales**: Compartición completa de contexto, conciencia de decisiones de acción y gestión de ventana de contexto
  - **Alineación con protocolo MCP**: Cómo el diseño MCP aborda los desafíos de ingeniería de contexto
    - Limitaciones de ventana de contexto y estrategias de carga progresiva
    - Determinación de relevancia y recuperación dinámica de contexto
    - Manejo multimodal de contexto y consideraciones de seguridad
  - **Enfoques de implementación**: Arquitecturas de un solo hilo vs. multi-agente
    - Técnicas de fragmentación y priorización de contexto
    - Carga progresiva de contexto y estrategias de compresión
    - Enfoques en capas de contexto y optimización de recuperación
  - **Marco de medición**: Métricas emergentes para evaluación de efectividad de contexto
    - Eficiencia de entrada, rendimiento, calidad y consideraciones de experiencia de usuario
    - Enfoques experimentales para optimización de contexto
    - Análisis de fallos y metodologías de mejora

#### Actualizaciones de navegación del currículo (README.md)
- **Estructura de módulo mejorada**: Actualizada tabla del currículo para incluir nuevos temas avanzados
  - Añadidos Ingeniería de Contexto (5.14) y Transporte Personalizado (5.15)
  - Formato y enlaces de navegación consistentes en todos los módulos
  - Descripciones actualizadas para reflejar el alcance actual del contenido

### Mejoras en estructura de directorios
- **Estandarización de nombres**: Renombrado "mcp transport" a "mcp-transport" para consistencia con otras carpetas de temas avanzados
- **Organización de contenido**: Todas las carpetas 05-AdvancedTopics ahora siguen patrón de nombres consistente (mcp-[tema])

### Mejoras en calidad de documentación
- **Alineación con especificación MCP**: Todo el contenido nuevo referencia la Especificación MCP 2025-06-18 actual
- **Ejemplos multilenguaje**: Ejemplos completos en C#, TypeScript y Python
- **Enfoque empresarial**: Patrones listos para producción e integración con nube Azure en todo el contenido
- **Documentación visual**: Diagramas Mermaid para visualización de arquitectura y flujos

## 18 de agosto de 2025

### Actualización integral de documentación - Estándares MCP 2025-06-18

#### Mejores prácticas de seguridad MCP (02-Security/) - Modernización completa
- **MCP-SECURITY-BEST-PRACTICES-2025.md**: Reescritura completa alineada con la Especificación MCP 2025-06-18
  - **Requisitos Obligatorios**: Se añadieron requisitos explícitos de DEBE/NO DEBE de la especificación oficial con indicadores visuales claros  
  - **12 Prácticas de Seguridad Clave**: Reestructurado de una lista de 15 ítems a dominios de seguridad integrales  
    - Seguridad de Tokens y Autenticación con integración de proveedor de identidad externo  
    - Gestión de Sesiones y Seguridad de Transporte con requisitos criptográficos  
    - Protección contra Amenazas Específicas de IA con integración de Microsoft Prompt Shields  
    - Control de Acceso y Permisos con principio de menor privilegio  
    - Seguridad y Monitoreo de Contenido con integración de Azure Content Safety  
    - Seguridad de la Cadena de Suministro con verificación integral de componentes  
    - Seguridad OAuth y Prevención de Confused Deputy con implementación PKCE  
    - Respuesta a Incidentes y Recuperación con capacidades automatizadas  
    - Cumplimiento y Gobernanza con alineación regulatoria  
    - Controles de Seguridad Avanzados con arquitectura de confianza cero  
    - Integración del Ecosistema de Seguridad de Microsoft con soluciones integrales  
    - Evolución Continua de la Seguridad con prácticas adaptativas  
  - **Soluciones de Seguridad de Microsoft**: Guía de integración mejorada para Prompt Shields, Azure Content Safety, Entra ID y GitHub Advanced Security  
  - **Recursos de Implementación**: Enlaces de recursos categorizados por Documentación Oficial MCP, Soluciones de Seguridad Microsoft, Estándares de Seguridad y Guías de Implementación  

#### Controles de Seguridad Avanzados (02-Security/) - Implementación Empresarial  
- **MCP-SECURITY-CONTROLS-2025.md**: Revisión completa con marco de seguridad de nivel empresarial  
  - **9 Dominios de Seguridad Integrales**: Ampliado desde controles básicos a marco detallado empresarial  
    - Autenticación y Autorización Avanzadas con integración Microsoft Entra ID  
    - Seguridad de Tokens y Controles Anti-Passthrough con validación exhaustiva  
    - Controles de Seguridad de Sesión con prevención de secuestro  
    - Controles de Seguridad Específicos para IA con prevención de inyección de prompts y envenenamiento de herramientas  
    - Prevención de Ataques Confused Deputy con seguridad proxy OAuth  
    - Seguridad en Ejecución de Herramientas con sandboxing y aislamiento  
    - Controles de Seguridad de Cadena de Suministro con verificación de dependencias  
    - Controles de Monitoreo y Detección con integración SIEM  
    - Respuesta a Incidentes y Recuperación con capacidades automatizadas  
  - **Ejemplos de Implementación**: Añadidos bloques detallados de configuración YAML y ejemplos de código  
  - **Integración de Soluciones Microsoft**: Cobertura integral de servicios de seguridad Azure, GitHub Advanced Security y gestión de identidad empresarial  

#### Temas Avanzados de Seguridad (05-AdvancedTopics/mcp-security/) - Implementación Lista para Producción  
- **README.md**: Reescritura completa para implementación de seguridad empresarial  
  - **Alineación con Especificación Actual**: Actualizado a MCP Specification 2025-06-18 con requisitos de seguridad obligatorios  
  - **Autenticación Mejorada**: Integración Microsoft Entra ID con ejemplos completos en .NET y Java Spring Security  
  - **Integración de Seguridad IA**: Implementación de Microsoft Prompt Shields y Azure Content Safety con ejemplos detallados en Python  
  - **Mitigación Avanzada de Amenazas**: Ejemplos completos para  
    - Prevención de Ataques Confused Deputy con PKCE y validación de consentimiento de usuario  
    - Prevención de Passthrough de Tokens con validación de audiencia y gestión segura de tokens  
    - Prevención de Secuestro de Sesión con enlace criptográfico y análisis de comportamiento  
  - **Integración de Seguridad Empresarial**: Monitoreo con Azure Application Insights, pipelines de detección de amenazas y seguridad de cadena de suministro  
  - **Lista de Verificación de Implementación**: Controles de seguridad obligatorios vs. recomendados con beneficios del ecosistema de seguridad Microsoft  

### Calidad de la Documentación y Alineación con Estándares  
- **Referencias a Especificaciones**: Actualizadas todas las referencias a MCP Specification 2025-06-18  
- **Ecosistema de Seguridad Microsoft**: Guía de integración mejorada en toda la documentación de seguridad  
- **Implementación Práctica**: Añadidos ejemplos detallados en .NET, Java y Python con patrones empresariales  
- **Organización de Recursos**: Categorización integral de documentación oficial, estándares de seguridad y guías de implementación  
- **Indicadores Visuales**: Marcado claro de requisitos obligatorios vs. prácticas recomendadas  

#### Conceptos Básicos (01-CoreConcepts/) - Modernización Completa  
- **Actualización de Versión de Protocolo**: Actualizado para referenciar MCP Specification 2025-06-18 con versionado basado en fecha (formato AAAA-MM-DD)  
- **Refinamiento de Arquitectura**: Descripciones mejoradas de Hosts, Clientes y Servidores para reflejar patrones actuales de arquitectura MCP  
  - Hosts ahora definidos claramente como aplicaciones IA que coordinan múltiples conexiones de clientes MCP  
  - Clientes descritos como conectores de protocolo que mantienen relaciones uno a uno con servidores  
  - Servidores mejorados con escenarios de despliegue local vs. remoto  
- **Reestructuración de Primitivas**: Revisión completa de primitivas de servidor y cliente  
  - Primitivas de Servidor: Recursos (fuentes de datos), Prompts (plantillas), Herramientas (funciones ejecutables) con explicaciones y ejemplos detallados  
  - Primitivas de Cliente: Muestreo (completaciones LLM), Elicitación (entrada de usuario), Registro (depuración/monitoreo)  
  - Actualizado con patrones actuales de métodos de descubrimiento (`*/list`), recuperación (`*/get`) y ejecución (`*/call`)  
- **Arquitectura del Protocolo**: Introducido modelo de arquitectura de dos capas  
  - Capa de Datos: Base JSON-RPC 2.0 con gestión del ciclo de vida y primitivas  
  - Capa de Transporte: STDIO (local) y HTTP Streamable con SSE (transporte remoto)  
- **Marco de Seguridad**: Principios de seguridad integrales incluyendo consentimiento explícito del usuario, protección de privacidad de datos, seguridad en ejecución de herramientas y seguridad en capa de transporte  
- **Patrones de Comunicación**: Mensajes de protocolo actualizados para mostrar flujos de inicialización, descubrimiento, ejecución y notificación  
- **Ejemplos de Código**: Ejemplos multilenguaje actualizados (.NET, Java, Python, JavaScript) para reflejar patrones actuales del SDK MCP  

#### Seguridad (02-Security/) - Revisión Integral de Seguridad  
- **Alineación con Estándares**: Alineación completa con requisitos de seguridad MCP Specification 2025-06-18  
- **Evolución de Autenticación**: Documentada evolución desde servidores OAuth personalizados a delegación con proveedor de identidad externo (Microsoft Entra ID)  
- **Análisis de Amenazas Específicas de IA**: Cobertura mejorada de vectores de ataque modernos en IA  
  - Escenarios detallados de ataques de inyección de prompts con ejemplos reales  
  - Mecanismos de envenenamiento de herramientas y patrones de ataque "rug pull"  
  - Envenenamiento de ventana de contexto y ataques de confusión de modelo  
- **Soluciones de Seguridad IA de Microsoft**: Cobertura integral del ecosistema de seguridad Microsoft  
  - AI Prompt Shields con técnicas avanzadas de detección, resaltado y delimitadores  
  - Patrones de integración de Azure Content Safety  
  - GitHub Advanced Security para protección de cadena de suministro  
- **Mitigación Avanzada de Amenazas**: Controles de seguridad detallados para  
  - Secuestro de sesión con escenarios de ataque específicos MCP y requisitos criptográficos de ID de sesión  
  - Problemas de confused deputy en escenarios proxy MCP con requisitos explícitos de consentimiento  
  - Vulnerabilidades de passthrough de tokens con controles de validación obligatorios  
- **Seguridad de Cadena de Suministro**: Cobertura ampliada de cadena de suministro IA incluyendo modelos base, servicios de embeddings, proveedores de contexto y APIs de terceros  
- **Seguridad de Fundamentos**: Integración mejorada con patrones de seguridad empresarial incluyendo arquitectura de confianza cero y ecosistema de seguridad Microsoft  
- **Organización de Recursos**: Enlaces de recursos categorizados por tipo (Documentación Oficial, Estándares, Investigación, Soluciones Microsoft, Guías de Implementación)  

### Mejoras en la Calidad de la Documentación  
- **Objetivos de Aprendizaje Estructurados**: Objetivos de aprendizaje mejorados con resultados específicos y accionables  
- **Referencias Cruzadas**: Añadidos enlaces entre temas relacionados de seguridad y conceptos básicos  
- **Información Actualizada**: Actualizadas todas las referencias de fechas y enlaces a especificaciones actuales  
- **Guía de Implementación**: Añadidas directrices específicas y accionables a lo largo de ambas secciones  

## 16 de julio de 2025  

### Mejoras en README y Navegación  
- Navegación del currículo completamente rediseñada en README.md  
- Reemplazadas etiquetas `<details>` por formato tabular más accesible  
- Creación de opciones de diseño alternativas en nueva carpeta "alternative_layouts"  
- Añadidos ejemplos de navegación basada en tarjetas, estilo pestañas y acordeón  
- Actualizada sección de estructura del repositorio para incluir todos los archivos más recientes  
- Mejorada sección "Cómo usar este currículo" con recomendaciones claras  
- Actualizados enlaces a especificaciones MCP para apuntar a URLs correctas  
- Añadida sección de Ingeniería de Contexto (5.14) a la estructura del currículo  

### Actualizaciones de la Guía de Estudio  
- Guía de estudio completamente revisada para alinearse con la estructura actual del repositorio  
- Añadidas nuevas secciones para Clientes MCP y Herramientas, y Servidores MCP Populares  
- Actualizado Mapa Visual del Currículo para reflejar con precisión todos los temas  
- Mejoradas descripciones de Temas Avanzados para cubrir todas las áreas especializadas  
- Actualizada sección de Estudios de Caso para reflejar ejemplos reales  
- Añadido este registro de cambios integral  

### Contribuciones de la Comunidad (06-CommunityContributions/)  
- Añadida información detallada sobre servidores MCP para generación de imágenes  
- Añadida sección integral sobre uso de Claude en VSCode  
- Añadidas instrucciones de configuración y uso del cliente terminal Cline  
- Actualizada sección de clientes MCP para incluir todas las opciones populares  
- Mejorados ejemplos de contribución con muestras de código más precisas  

### Temas Avanzados (05-AdvancedTopics/)  
- Organización de todas las carpetas de temas especializados con nomenclatura consistente  
- Añadidos materiales y ejemplos de ingeniería de contexto  
- Añadida documentación de integración de agente Foundry  
- Mejorada documentación de integración de seguridad Entra ID  

## 11 de junio de 2025  

### Creación Inicial  
- Lanzada primera versión del currículo MCP para Principiantes  
- Creada estructura básica para las 10 secciones principales  
- Implementado Mapa Visual del Currículo para navegación  
- Añadidos proyectos de muestra iniciales en múltiples lenguajes de programación  

### Primeros Pasos (03-GettingStarted/)  
- Creación de primeros ejemplos de implementación de servidor  
- Añadida guía de desarrollo de clientes  
- Incluidas instrucciones de integración de clientes LLM  
- Añadida documentación de integración con VS Code  
- Implementados ejemplos de servidor con Server-Sent Events (SSE)  

### Conceptos Básicos (01-CoreConcepts/)  
- Añadida explicación detallada de arquitectura cliente-servidor  
- Creada documentación sobre componentes clave del protocolo  
- Documentados patrones de mensajería en MCP  

## 23 de mayo de 2025  

### Estructura del Repositorio  
- Inicializado repositorio con estructura básica de carpetas  
- Creados archivos README para cada sección principal  
- Configurada infraestructura de traducción  
- Añadidos recursos gráficos y diagramas  

### Documentación  
- Creado README.md inicial con visión general del currículo  
- Añadidos CODE_OF_CONDUCT.md y SECURITY.md  
- Configurado SUPPORT.md con guía para obtener ayuda  
- Creada estructura preliminar de guía de estudio  

## 15 de abril de 2025  

### Planificación y Marco  
- Planificación inicial para currículo MCP para Principiantes  
- Definidos objetivos de aprendizaje y público objetivo  
- Esbozada estructura de 10 secciones del currículo  
- Desarrollado marco conceptual para ejemplos y estudios de caso  
- Creación de prototipos iniciales de ejemplos para conceptos clave  

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso legal**:
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o interpretaciones erróneas derivadas del uso de esta traducción.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->