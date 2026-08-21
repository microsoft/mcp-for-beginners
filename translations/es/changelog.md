# Registro de Cambios: Currículo MCP para Principiantes

Este documento sirve como un registro de todos los cambios significativos realizados en el currículo de Protocolo de Contexto de Modelo (MCP) para Principiantes. Los cambios se documentan en orden cronológico inverso (los cambios más recientes primero).

## 29 de julio de 2026

### Nuevo Módulo 08 Complementario: Sidecars de Confiabilidad y Reintentos Seguros

Se añadió una lección complementaria independiente del proveedor para herramientas MCP que crean efectos del mundo real,
alineada con la especificación final `2026-07-28`.

- **Nuevo**: La [lección complementaria de sidecar de confiabilidad][reliability-sidecar]
  utiliza una historia de ticket de soporte, dos diagramas Mermaid y un flujo de decisión de reintento
  para explicar claves de operación estable, admisión atómica de duplicados,
  reconciliación, evidencia y el límite de extensión de Tareas.
- **Nuevo**: Un ejercicio de inyección de fallas con Python y SQLite de biblioteca estándar
  usa tiendas separadas para operaciones y tickets para demostrar una respuesta perdida
  después de que un efecto externo se confirma. Seis pruebas determinísticas cubren duplicación ingenua,
  recuperación protegida al reiniciar, conflictos de carga útil, resultados en caché,
  reclamos activos y admisión de duplicados concurrentes.
- **Actualizado**: El Módulo 08 ahora enlaza la lección complementaria, identifica el
  modelo de solicitud sin estado final `2026-07-28`, distingue la observabilidad OpenTelemetry
  de la característica de registro MCP obsoleta, y limita su
  ejemplo genérico de reintentos a operaciones de solo lectura.
- **Opcional**: La lección mapea sus conceptos portátiles a una implementación comunitaria etiquetada
  sin hacer que el servicio alojado ni una llamada de red formen parte del
  ejercicio.

[reliability-sidecar]: ./08-BestPractices/reliability-sidecars/README.md

## 2 de julio de 2026

### Nueva Lección: Candidato a Liberación de la Especificación MCP 2026-07-28

Se agregó cobertura del próximo candidato a liberación de la especificación MCP `2026-07-28` (anunciado el 21 de mayo de 2026; liberación final programada para el 28 de julio de 2026), resumido desde la [publicación oficial de anuncio en el blog](https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/). La línea base del currículo sigue siendo **Especificación MCP 2025-11-25** hasta que la nueva versión se lance, por lo que se presenta como una orientación prospectiva más que como una reescritura de las lecciones existentes.

- **Nuevo**: [01-CoreConcepts/mcp-2026-07-28-release-candidate.md](./01-CoreConcepts/mcp-2026-07-28-release-candidate.md) — una lección completa sobre el núcleo del protocolo sin estado (eliminación del apretón de manos `initialize` y `Mcp-Session-Id`), los nuevos encabezados de enrutamiento `Mcp-Method`/`Mcp-Name`, metadatos de caché `ttlMs`/`cacheScope`, W3C Trace Context en `_meta`, el marco formal de Extensiones (MCP Apps y la nueva extensión de Tareas), seis SEPs para endurecimiento de autorización, la deshabilitación de Roots/Sampling/Logging, y la transición al esquema completo JSON Schema 2020-12 para esquemas de herramientas.
- **Actualizado** con llamadas hacia adelante vinculando a la nueva lección:
  - [01-CoreConcepts/README.md](./01-CoreConcepts/README.md): nota de versión de protocolo, secciones de Sampling/Roots/Logging/Tareas, y "Qué sigue"
  - [02-Security/README.md](./02-Security/README.md): llamada de endurecimiento de autorización
  - [03-GettingStarted/06-http-streaming/README.md](./03-GettingStarted/06-http-streaming/README.md): llamada de transporte sin estado
  - [03-GettingStarted/14-sampling/README.md](./03-GettingStarted/14-sampling/README.md): llamada de descontinuación de Sampling
  - [05-AdvancedTopics/mcp-protocol-features/README.md](./05-AdvancedTopics/mcp-protocol-features/README.md): llamada de desactivación de Logging y extensión Tareas
  - [05-AdvancedTopics/mcp-transport/README.md](./05-AdvancedTopics/mcp-transport/README.md): llamada de transporte sin estado/enrutamiento de sesión
  - [README.md](./README.md): nota de "Mirando hacia adelante" en la sección de especificaciones y una nueva entrada `1.1` en la tabla de módulos del currículo
  - [study_guide.md](./study_guide.md): viñeta prospectiva bajo la visión general de Conceptos Básicos y una nota adicional fechada
  - [03-GettingStarted/11-simple-auth/README.md](./03-GettingStarted/11-simple-auth/README.md): llamada en el mapa de transporte `mcp-session-id` antes del modelo de solicitud sin estado
  - [05-AdvancedTopics/README.md](./05-AdvancedTopics/README.md): llamada de visión general del módulo sobre las desactivaciones de Root Contexts/Sampling y la extensión de Tareas
  - [05-AdvancedTopics/mcp-security/README.md](./05-AdvancedTopics/mcp-security/README.md): llamada de endurecimiento de autorización

## 24 de junio de 2026

### Nueva Lección: Uso de MCP en la aplicación Copilot

- [Sección de herramientas](./12-tooling/README.md) Se añadió la sección de herramientas.
- [MCP en la aplicación Copilot](./12-tooling/01-copilot-app/README.md)

## 16 de junio de 2026

### Alineación con la Especificación MCP y Validación de Ejemplos

Se validó el currículo contra la actual **Especificación MCP 2025-11-25** y los SDKs oficiales más recientes, luego se corrigieron las referencias obsoletas restantes de especificación y se confirmó que los ejemplos principales aún se construyen y ejecutan.

#### Correcciones de versión de especificación (2025-06-18 / 2025-03-26 → 2025-11-25)

Se actualizó el contenido en inglés donde todavía afirmaba que una revisión anterior de la especificación era el estándar *actual/más reciente*, y se redirigieron enlaces a las rutas canónicas de especificación `modelcontextprotocol.io`:
- **05-AdvancedTopics/mcp-security/README.md**: Se actualizó el banner de "Estándar Actual", introducción, encabezado de principios de seguridad centrales, encabezado de requerimientos obligatorios, sección Microsoft Entra ID, enlaces de Referencias y Recursos, y aviso de seguridad final (8 referencias) a 2025-11-25
- **05-AdvancedTopics/mcp-transport/README.md**: Se actualizó el enlace de recursos adicionales de especificación y el banner de "Estándar Actual" a 2025-11-25
- **05-AdvancedTopics/mcp-realtimesearch/README.md**: Se reemplazó el enlace obsoleto `2025-03-26` de seguridad y confianza con la página actual de mejores prácticas de seguridad 2025-11-25
- **03-GettingStarted/14-sampling/README.md**: Se actualizó el enlace oficial de documentación de muestreo a 2025-11-25

- **03-GettingStarted/05-stdio-server/README.md**: Se actualizó la referencia en tiempo presente "especificación MCP actual" y el enlace de la especificación de Recursos Adicionales a 2025-11-25 (notas históricas sobre la desprecación de SSE se mantienen para precisión)

#### Validación de muestras contra los SDKs actuales

- **TypeScript (03-GettingStarted/01-first-server/solution/typescript)**: `npm install` resolvió `@modelcontextprotocol/sdk@1.29.0`; `tsc --noEmit` pasó sin errores de tipo — las APIs existentes `McpServer`/`StdioServerTransport` siguen siendo válidas
- **Python (03-GettingStarted/01-first-server/solution/python)**: Validado en un `.venv` aislado con `mcp[cli]` (1.27.2); `py_compile` pasó y `FastMCP.list_tools()` devolvió correctamente las herramientas `add` y `subtract`
- Confirmado que todos los rangos de versión de ejemplo `@modelcontextprotocol/sdk` (`>=1.26.0` / `^1.26.0` / `^1.27.0`) se resuelven limpiamente a la versión actual `1.29.0` sin cambios breaking en la API

#### Alineación de fijación de dependencias (cerrando brechas de versión)

Se actualizaron fijaciones de SDK obsoletas para que cada muestra rastree la versión actual de MCP, en línea con la convención del repositorio:
- **03-GettingStarted/05-stdio-server/solution/typescript/package.json**: Se actualizó `@modelcontextprotocol/sdk` de `^1.8.0` a `>=1.26.0` y se actualizó la descripción del paquete desactualizada `"actualizado para MCP 2025-06-18"` a `"alineado con la especificación MCP 2025-11-25"`
- **10-StreamliningAIWorkflows.../lab3/code/weather_mcp/pyproject.toml** y **lab4/code/github_mcp_server/pyproject.toml**: Se actualizó el pin exacto `mcp==1.23.0` a `mcp>=1.26.0`; se regeneraron ambos archivos `uv.lock` (`uv lock`) para que los lockfiles se resuelvan a la versión actual `mcp 1.27.2` y se mantengan sincronizados con los manifiestos

#### Análisis de brechas del currículo — Cobertura de características de la última especificación

Verificado que el currículo ya cubre todas las primitivas introducidas/expandidas en MCP 2025-11-25, por lo que no quedan brechas de contenido:
- **Sampling**: Lección 03-GettingStarted/14-sampling más 05-AdvancedTopics/mcp-sampling
- **Elicitation (incl. modo URL)**: Documentado en 01-CoreConcepts y 05-AdvancedTopics/mcp-protocol-features
- **Roots**: Documentado en 00-Introduction, 01-CoreConcepts, y 05-AdvancedTopics/mcp-root-contexts
- **Tasks (experimental, operaciones de larga duración)**: Documentado en 01-CoreConcepts y 05-AdvancedTopics/mcp-protocol-features
- **Anotaciones de herramientas** (`readOnlyHint` / `destructiveHint`): Documentado en 01-CoreConcepts y 05-AdvancedTopics/mcp-protocol-features

### Endurecimiento de seguridad y remediación de vulnerabilidades en dependencias

Se realizó un análisis completo de seguridad en cada manifiesto de dependencia y el código fuente de las muestras, luego se corrigieron todas las alertas npm reportadas y una vulnerabilidad a nivel de código. Después de la corrección, `npm audit` reporta **0 vulnerabilidades** en cada directorio auditado.

#### Vulnerabilidades en dependencias npm (transitivas) — Corregidas

Se auditaron los 15 archivos `package-lock.json` comprometidos. Las vulnerabilidades se limitaron a dependencias transitivas usadas por la herramienta de desarrollo MCP Inspector, el cliente OpenAI y el SDK MCP; todas ahora están resueltas sin romper las muestras:
- **10-StreamliningAIWorkflows.../lab4/code/github_mcp_server/inspector** y **lab3/code/weather_mcp/inspector**: Se actualizó `@modelcontextprotocol/inspector` (`0.16.6` / `0.14.1` → `0.22.0`), lo que limpió las alertas de los paquetes incluidos `ajv`, `brace-expansion`, `diff`, `path-to-regexp` y `ws`. Se añadió una entrada npm `overrides` forzando el parcheado `shell-quote@1.8.4` para eliminar la alerta crítica restante que venía con `concurrently`; se regeneraron ambos lockfiles (ahora con 0 vulnerabilidades)
- **03-GettingStarted/samples/typescript**: `npm audit fix` actualizó la dependencia transitoria `qs` (moderada) a una versión parcheada
- **03-GettingStarted/samples/javascript**: `npm audit fix` actualizó la dependencia transitoria `hono` (moderada) a una versión parcheada
- **03-GettingStarted/03-llm-client/solution/typescript**: `npm audit fix` actualizó la dependencia transitoria `form-data` (alta) a una versión parcheada
- **03-GettingStarted/11-simple-auth/solution/typescript**: Se generó el `package-lock.json` faltante para que el proyecto sea reproducible y auditable (0 vulnerabilidades)

#### Corrección de seguridad a nivel de código (OWASP A03: Inyección)

- **10-StreamliningAIWorkflows.../lab4/code/github_mcp_server/src/server.py**: Se eliminó `shell=True` de la herramienta `open_in_vscode`. El previo `subprocess.run(["start", "", vscode_path, folder_path], shell=True)` permitía que metacaracteres del shell en un path de carpeta fueran interpretados por `cmd.exe` (vector de inyección de comandos). Ahora lanza directamente el ejecutable resuelto `Code.exe` con la carpeta como argumento — sin shell — lo que es funcionalmente equivalente y seguro

#### Auditoría de dependencias Python

- Se auditó cada conjunto de requisitos de Python con `pip-audit`. `05-AdvancedTopics` y `03-GettingStarted/samples/python` reportaron **ninguna vulnerabilidad conocida** (sus rangos `mcp` / `httpx` / `pydantic` / `python-dotenv` se resuelven a versiones actuales parcheadas)
- **09-CaseStudy/docs-mcp/solution/python/requirements.txt**: `pip-audit` detectó la dependencia transitiva **`werkzeug` 3.1.1** con tres alertas de DoS por nombres de dispositivos de Windows en `safe_join` — `CVE-2025-66221`, `CVE-2026-21860` y `CVE-2026-27199` (todas corregidas en 3.1.6). Se añadió un pin de seguridad explícito `werkzeug>=3.1.6` para que se resuelva la versión parcheada; se verificó que la restricción se resuelve limpiamente con la pila `chainlit` / `mcp` / `semantic-kernel`

### Cambio de marca del nombre del producto

Se actualizó todo el contenido del currículo para reflejar el cambio de marca del producto de Microsoft:


#### Azure AI Foundry → Microsoft Foundry
- **SUPPORT.md**: Enlace de la comunidad de Discord actualizado

- **AGENTS.md**: Actualizada la referencia al servidor de Discord
- **README.md**: Actualizadas las referencias al ecosistema tecnológico
- **study_guide.md**: Actualizadas las referencias a estudios de caso
- **05-AdvancedTopics/README.md**: Actualizado el título y la descripción del Módulo 5.13
- **05-AdvancedTopics/mcp-integration/README.md**: Actualizado el encabezado de sección y la descripción
- **05-AdvancedTopics/mcp-foundry-agent-integration/README.md**: Actualización completa del título y contenido del módulo
- **05-AdvancedTopics/mcp-security-entra/README.md**: Actualizado enlace de referencia cruzada
- **07-LessonsfromEarlyAdoption/README.md**: Actualizadas las referencias a estudios de caso
- **07-LessonsfromEarlyAdoption/microsoft-mcp-servers.md**: Actualizado el encabezado de la Sección 9, insignias y capacidades
- **08-BestPractices/README.md**: Actualizado enlace a la comunidad de Discord
- **09-CaseStudy/docs-mcp/solution/scenario3/README.md**: Actualizada la referencia al canal de Discord
- **09-CaseStudy/docs-mcp/solution/python/README.md**: Actualizada la referencia al despliegue del modelo
- **11-MCPServerHandsOnLabs/00-Introduction/README.md**: Actualizada la tabla de Servicios de IA
- **11-MCPServerHandsOnLabs/03-Setup/README.md**: Actualizadas las referencias a recursos

#### AI Toolkit / AITK → Extensión del Microsoft Foundry Toolkit para VS Code
- **README.md**: Actualizadas las referencias principales del currículo
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/README.md**: Actualizados el título del módulo, resumen y todos los encabezados del módulo
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab1/README.md**: Actualizados título, objetivos de aprendizaje, instrucciones de configuración y recursos
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab2/README.md**: Actualizados título, objetivos de aprendizaje, tabla de hosts MCP y referencias cruzadas
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/README.md**: Actualizados título, insignias, prerequisitos y recursos
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/README.md**: Actualizadas las referencias al Constructor de Agentes y el enlace de comentarios
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/README.md**: Actualizados prerequisitos y referencias a la extensión

---

## 11 de abril de 2026

### Nueva lección, correcciones de documentación y actualizaciones de dependencias

#### Nuevo contenido de currículo agregado

**Módulo 05 - Temas Avanzados**
- **Lección 5.17: Razonamiento Multi-Agente Adversarial con MCP** (`05-AdvancedTopics/mcp-adversarial-agents/README.md`): Nueva guía completa que cubre el patrón de debate adversarial para sistemas multi-agente
  - Diagrama de arquitectura en Mermaid: dos agentes → servidor MCP compartido → transcripción del debate → juez → veredicto
  - Servidor de herramientas MCP compartido (`web_search` + `run_python`) implementado en Python y TypeScript
  - Prompts del sistema opuestos (A FAVOR / EN CONTRA / Juez) con requisitos explícitos de uso de herramientas
  - Orquestador de debate en Python, TypeScript y C# gestionando rondas y conduciendo argumentos
  - Conexión MCP `ClientSession` para el orquestador a llamadas reales de herramientas
  - Tabla de casos de uso (detección de alucinaciones, modelado de amenazas, revisión de diseño de API, verificación factual, selección tecnológica)
  - Consideraciones de seguridad: ejecución en sandbox, validación de llamadas a herramientas, limitación de tasa, registro de auditoría
  - Ejercicio estructurado con tres escenarios prácticos (revisión de código, decisión de arquitectura, moderación de contenido)

#### Correcciones de documentación

**Módulo 03 - Primeros pasos**
- **05-stdio-server/README.md**: Corregido ejemplo incompleto del servidor stdio en TypeScript — agregada la instancia faltante de transporte (`new StdioServerTransport()`) y llamada `server.connect(transport)` para coincidir con los ejemplos de Python y .NET en la misma sección
- **14-sampling/README.md**: Corregida errata — corregido `"Sampling is an davanced features"` → `"Sampling is an advanced feature"`

#### Actualizaciones del currículo

**README.md principal**
- Entrada 5.17 (Razonamiento Multi-Agente Adversarial con MCP) añadida a la tabla del currículo con enlace directo a la nueva lección

**05-AdvancedTopics/README.md**
- Fila de la Lección 5.17 añadida a la tabla de lecciones

**study_guide.md**
- Agregado tema de Razonamiento Multi-Agente Adversarial al mapa mental y descripción en prosa de Temas Avanzados

#### Correcciones de código y seguridad

**Módulo 05 - Agentes Adversariales (`mcp-adversarial-agents`)**
- **Corrección de seguridad — inyección de comandos**: Reemplazada la interpolación de shell `execSync` por `execFile` + `promisify` en la herramienta `run_python` de TypeScript, eliminando la superficie de inyección de comandos (el código controlado por LLM ahora se pasa como un elemento argv literal sin participación de shell)
- **Conexión del ciclo de herramientas MCP**: Actualizado el orquestador de debate Python para usar cliente `AsyncAnthropic` (reemplazando el bloqueante `Anthropic` síncrono), pasar `ClientSession` en vivo directamente a cada turno del agente, obtener definiciones de herramientas vía `session.list_tools()` en cada turno, y despachar bloques `tool_use` vía `session.call_tool()` en un ciclo hasta que el modelo emita una respuesta de texto final

#### Actualizaciones de dependencias

- Actualizada la versión de `hono` a 4.12.12 en múltiples paquetes (03-GettingStarted, 04-PracticalImplementation, 10-StreamliningAIWorkflows)
- Actualizado `@hono/node-server` de 1.19.11 a 1.19.13 en paquetes TypeScript
- Actualizada `cryptography` de 46.0.5 a 46.0.7 en paquetes Python (laboratorios 3 y 4 de 10-StreamliningAIWorkflows)
- Actualizada `lodash` de 4.17.23 a 4.18.1 en inspector de 10-StreamliningAIWorkflows

#### Traducciones

- Sincronizadas las traducciones para más de 48 idiomas con los últimos cambios de fuente (actualización i18n)

---

## 5 de febrero de 2026

### Mejoras en validación y navegación en todo el repositorio

#### Nuevo contenido de currículo agregado

**Módulo 03 - Primeros pasos**
- **12-mcp-hosts/README.md**: Nueva guía completa para configurar hosts MCP
  - Ejemplos de configuración para Claude Desktop, VS Code, Cursor, Cline, Windsurf
  - Plantillas de configuración JSON para todos los hosts principales
  - Tabla comparativa de tipos de transporte (stdio, SSE/HTTP, WebSocket)
  - Solución de problemas para problemas comunes de conexión
  - Mejores prácticas de seguridad para configuración de hosts

- **13-mcp-inspector/README.md**: Nueva guía de depuración para MCP Inspector
  - Métodos de instalación (npx, npm global, desde código fuente)
  - Conexión a servidores vía stdio y HTTP/SSE
  - Herramientas de prueba, recursos y flujos de trabajo de prompts
  - Integración con VS Code y MCP Inspector
  - Escenarios comunes de depuración con soluciones

**Módulo 04 - Implementación práctica**
- **pagination/README.md**: Nueva guía de implementación de paginación
  - Patrones de paginación basada en cursor en Python, TypeScript, Java
  - Manejo de paginación del lado cliente
  - Estrategias de diseño de cursor (opaco vs. estructurado)
  - Recomendaciones de optimización de rendimiento

**Módulo 05 - Temas Avanzados**
- **mcp-protocol-features/README.md**: Nueva profundización en características del protocolo
  - Implementación de notificaciones de progreso
  - Patrones de cancelación de solicitudes
  - Plantillas de recursos con patrones URI
  - Gestión del ciclo de vida del servidor
  - Control de nivel de registro
  - Patrones de manejo de errores con códigos JSON-RPC

#### Correcciones de navegación (más de 24 archivos actualizados)

**README principales de los módulos**
 Ahora enlazan tanto a la primera lección COMO al siguiente módulo

**Subarchivos de Seguridad 02-Security**
- Los 5 documentos complementarios de seguridad ahora tienen navegación "Qué sigue":

**Archivos 09-CaseStudy**
- Todos los archivos de estudio de caso ahora tienen navegación secuencial:

**Laboratorios 10-StreamliningAI**
Añadida sección Qué sigue en el resumen del Módulo 10 y en el Módulo 11

#### Correcciones de código y contenido

**Actualizaciones de SDK y dependencias**
Corregida versión vacía de openai a `^4.95.0`
SDK actualizado de `^1.8.0` a `>=1.26.0`
Pines de versión de mcp actualizados a `>=1.26.0`

**Correcciones de código**
Corregido modelo inválido `gpt-4o-mini` a `gpt-4.1-mini`

**Correcciones de contenido**
Corregido enlace roto `READMEmd` → `README.md`, corregido encabezado del currículo `Módulo 1-3` → `Módulo 0-3`, corregida ruta sensible a mayúsculas
Eliminado contenido duplicado corrupto del Estudio de Caso 5

**Mejoras en la guía para principiantes**
Añadida introducción adecuada, objetivos de aprendizaje y prerrequisitos para principiantes

#### Actualizaciones del currículo

**README.md principal**
- Añadidas entradas 3.12 (Hosts MCP), 3.13 (Inspector MCP), 4.1 (Paginación), 5.16 (Características del Protocolo) a la tabla del currículo

**READMEs de módulos**
Añadidas lecciones 12 y 13 a la lista de lecciones
Añadida sección Guías Prácticas con enlace a paginación
Añadidas lecciones 5.15 (Transporte Personalizado) y 5.16 (Características del Protocolo)

**study_guide.md**
- Actualizado mapa mental con todos los temas nuevos: Configuración de Hosts MCP, Inspector MCP, Estrategias de Paginación, Profundización en Características del Protocolo

## 28 de enero de 2026

### Revisión de cumplimiento especificación MCP 2025-11-25

#### Mejora en conceptos clave (01-CoreConcepts/)
- **Nuevo primitivo de cliente - Roots**: Documentación completa sobre el primitivo Roots del cliente, permitiendo a servidores entender límites del sistema de archivos y permisos de acceso
- **Anotaciones de herramientas**: Agregada documentación sobre anotaciones de comportamiento de herramientas (`readOnlyHint`, `destructiveHint`) para mejores decisiones de ejecución
- **Llamadas a herramientas en Sampling**: Documentación actualizada para incluir parámetros `tools` y `toolChoice` para invocaciones de herramientas dirigidas por modelo durante solicitudes de muestreo
- **Modalidad de elicitation URL**: Documentación añadida sobre elicitation basada en URL para interacciones web externas iniciadas por el servidor
- **Tareas (Experimental)**: Nueva sección documentando la función experimental de Tareas para envoltorios de ejecución duradera y recuperación diferida de resultados
- **Soporte de íconos**: Se señaló que herramientas, recursos, plantillas de recursos y prompts ahora pueden incluir íconos como metadatos adicionales

#### Actualizaciones de documentación
- **README.md**: Añadida referencia a la versión MCP Specification 2025-11-25 y explicación de versionado basado en fecha
- **study_guide.md**: Mapa curricular actualizado para incluir Tareas y Anotaciones de Herramientas en la sección de Conceptos Clave; actualizado timestamp del documento

#### Verificación de cumplimiento de especificación
- **Versión del protocolo**: Verificado que toda la documentación referencia la especificación MCP 2025-11-25 actual
- **Alineación arquitectónica**: Confirmada precisión de documentación de arquitectura de dos capas (Capa de Datos + Capa de Transporte)
- **Documentación de primitivos**: Validados primitivos de servidor (Recursos, Prompts, Herramientas) y primitivos de cliente (Sampling, Elicitation, Logging, Roots)
- **Mecanismos de transporte**: Verificada precisión de documentación de transporte STDIO y HTTP transmitible
- **Guía de seguridad**: Confirmada alineación con las mejores prácticas actuales de seguridad MCP

#### Características clave documentadas MCP 2025-11-25
- **Descubrimiento OpenID Connect**: Descubrimiento de servidor de autenticación mediante OIDC
- **Documentos de metadatos Client ID OAuth**: Mecanismo recomendado para registro de clientes
- **JSON Schema 2020-12**: Dialecto por defecto para definiciones de esquema MCP
- **Sistema de niveles SDK**: Requisitos formalizados para soporte y mantenimiento de características SDK
- **Estructura de gobernanza**: Formalizados Grupos de Trabajo y Grupos de Interés en gobernanza MCP

### Actualización mayor en documentación de seguridad (02-Security/)

#### Integración con Taller MCP Security Summit (Sherpa)
- **Nuevo recurso de entrenamiento práctico**: Añadida integración completa con el [MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/) a lo largo de toda la documentación de seguridad
- **Cobertura de ruta de expedición**: Documentada progresión completa campamento a campamento desde Base Camp hasta Summit
- **Alineación con OWASP**: Toda la guía de seguridad ahora está mapeada a riesgos de la guía OWASP MCP Azure Security Guide

#### Integración OWASP MCP Top 10
- **Nueva sección**: Añadida tabla de riesgos de seguridad OWASP MCP Top 10 con mitigaciones Azure en README principal de Seguridad
- **Documentación basada en riesgos**: Actualizado mcp-security-controls-2025.md con referencias a riesgos OWASP MCP para cada dominio de seguridad
- **Arquitectura de referencia**: Vinculado a arquitectura de referencia y patrones de implementación OWASP MCP Azure Security Guide

#### Archivos de seguridad actualizados
- **README.md**: Añadida visión general del taller Sherpa, tabla de ruta de expedición, resumen de riesgos OWASP MCP Top 10 y sección de capacitación práctica
- **mcp-security-controls-2025.md**: Actualizado el encabezado a febrero 2026, añadidas referencias a riesgos OWASP (MCP01-MCP08), corregida inconsistencia de versión de especificación
- **mcp-security-best-practices-2025.md**: Añadida sección de recursos Sherpa y OWASP, actualizado timestamp
- **mcp-best-practices.md**: Añadida sección de capacitación práctica con enlaces Sherpa y OWASP
- **azure-content-safety-implementation.md**: Añadida referencia OWASP MCP06, alineación con Campamento 3 Sherpa y sección adicional de recursos

#### Nuevos enlaces a recursos añadidos
- [MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/)

- [OWASP MCP Guía de Seguridad Azure](https://microsoft.github.io/mcp-azure-security-guide/)
- [OWASP MCP Top 10](https://owasp.org/www-project-mcp-top-10/)
- Páginas individuales de riesgos OWASP MCP (MCP01-MCP10)

### Alineación de la Especificación MCP para todo el Currículo 2025-11-25

#### Módulo 03 - Introducción
- **Documentación SDK**: Se añadió el SDK de Go a la lista oficial de SDK; se actualizaron todas las referencias de SDK para alinear con la Especificación MCP 2025-11-25
- **Clarificación de Transporte**: Se actualizaron las descripciones de transporte STDIO y HTTP Streaming con referencias explícitas a la especificación

#### Módulo 04 - Implementación Práctica
- **Actualizaciones SDK**: Se añadió el SDK de Go; se actualizó la lista de SDK con la referencia de versión de la especificación
- **Especificación de Autorización**: Se actualizó el enlace a la especificación MCP de Autorización a la versión actual 2025-11-25

#### Módulo 05 - Temas Avanzados
- **Nuevas Funcionalidades**: Se añadió una nota sobre nuevas características de la Especificación MCP 2025-11-25 (Tareas, Anotaciones de Herramientas, Modo URL de Elicitación, Raíces)
- **Recursos de Seguridad**: Se añadieron los enlaces a OWASP MCP Top 10 y al taller Sherpa en referencias adicionales

#### Módulo 06 - Contribuciones de la Comunidad
- **Lista de SDK**: Se añadieron los SDKs de Swift y Rust; se actualizó el enlace de la especificación a 2025-11-25
- **Referencia de Especificación**: Se actualizó el enlace de la Especificación MCP a la URL directa de la especificación

#### Módulo 07 - Lecciones de la Adopción Temprana
- **Actualizaciones de Recursos**: Se añadió el enlace a la Especificación MCP 2025-11-25 y OWASP MCP Top 10 a recursos adicionales

#### Módulo 08 - Mejores Prácticas
- **Versión de Especificación**: Se actualizó la referencia a la Especificación MCP a 2025-11-25
- **Recursos de Seguridad**: Se añadieron OWASP MCP Top 10 y el taller Sherpa a referencias adicionales

#### Módulo 10 - Optimización de Flujos de Trabajo de IA
- **Actualización de Insignia**: Se cambió la insignia de versión MCP de versión SDK (1.9.3) a versión de especificación (2025-11-25)
- **Enlaces de Recursos**: Se actualizó el enlace a la Especificación MCP; se añadió OWASP MCP Top 10

#### Módulo 11 - Laboratorios Prácticos del Servidor MCP
- **Referencia de Especificación**: Se actualizó el enlace a la Especificación MCP a la versión 2025-11-25
- **Recursos de Seguridad**: Se añadió OWASP MCP Top 10 a los recursos oficiales

## 18 de diciembre de 2025

### Actualización de Documentación de Seguridad - Especificación MCP 2025-11-25

#### Mejores Prácticas de Seguridad MCP (02-Security/mcp-best-practices.md) - Actualización de Versión de Especificación
- **Actualización de Versión de Protocolo**: Se actualizó para referenciar la última Especificación MCP 2025-11-25 (lanzada el 25 de noviembre de 2025)
  - Se actualizaron todas las referencias de versión de especificación de 2025-06-18 a 2025-11-25
  - Se actualizaron las fechas de los documentos de 18 de agosto de 2025 a 18 de diciembre de 2025
  - Se verificó que todas las URLs de especificaciones apunten a la documentación actual
- **Validación del Contenido**: Validación completa de las mejores prácticas de seguridad conforme a los estándares más recientes
  - **Soluciones de Seguridad Microsoft**: Verificación de terminología y enlaces actuales para Prompt Shields (anteriormente "detección de riesgo de jailbreak"), Azure Content Safety, Microsoft Entra ID y Azure Key Vault
  - **Seguridad OAuth 2.1**: Confirmación de alineación con las mejores prácticas de seguridad de OAuth más recientes
  - **Estándares OWASP**: Validación de que las referencias OWASP Top 10 para LLMs estén actualizadas
  - **Servicios Azure**: Verificación de todos los enlaces a documentación de Microsoft Azure y mejores prácticas
- **Alineación de Estándares**: Todos los estándares de seguridad referenciados confirmados como actuales
  - Marco de Gestión de Riesgos AI NIST
  - ISO 27001:2022
  - Mejores Prácticas de Seguridad OAuth 2.1
  - Marcos de seguridad y cumplimiento de Azure
- **Recursos de Implementación**: Validación de todos los enlaces y recursos de guías de implementación
  - Patrones de autenticación de Azure API Management
  - Guías de integración Microsoft Entra ID
  - Administración de secretos Azure Key Vault
  - Tuberías DevSecOps y soluciones de monitoreo

### Aseguramiento de Calidad de la Documentación
- **Cumplimiento de la Especificación**: Asegurado que todos los requerimientos de seguridad MCP obligatorios (MUST/MUST NOT) estén alineados con la última especificación
- **Actualidad de Recursos**: Verificación de todos los enlaces externos a documentación Microsoft, estándares de seguridad y guías de implementación
- **Cobertura de Mejores Prácticas**: Confirmación de cobertura completa en autenticación, autorización, amenazas específicas de IA, seguridad de la cadena de suministro y patrones empresariales

## 6 de octubre de 2025

### Expansión de la Sección de Introducción – Uso Avanzado del Servidor y Autenticación Simple

#### Uso Avanzado del Servidor (03-GettingStarted/10-advanced)
- **Nuevo Capítulo Añadido**: Introducción de una guía completa para el uso avanzado de servidores MCP, cubriendo arquitecturas tanto regulares como de bajo nivel.
  - **Servidor Regular vs. de Bajo Nivel**: Comparación detallada y ejemplos de código en Python y TypeScript para ambos enfoques.
  - **Diseño Basado en Handlers**: Explicación de la gestión basada en handlers de herramientas/recursos/prompts para implementaciones de servidores escalables y flexibles.
  - **Patrones Prácticos**: Escenarios del mundo real donde los patrones de servidores de bajo nivel son beneficiosos para características y arquitecturas avanzadas.

#### Autenticación Simple (03-GettingStarted/11-simple-auth)
- **Nuevo Capítulo Añadido**: Guía paso a paso para implementar autenticación simple en servidores MCP.
  - **Conceptos de Auth**: Explicación clara de autenticación vs. autorización y manejo de credenciales.
  - **Implementación de Auth Básica**: Patrones de autenticación basados en middleware en Python (Starlette) y TypeScript (Express), con ejemplos de código.
  - **Progresión hacia Seguridad Avanzada**: Orientación para comenzar con autenticación simple y avanzar a OAuth 2.1 y RBAC, con referencias a módulos de seguridad avanzada.

Estas adiciones proporcionan guías prácticas y concretas para construir implementaciones de servidores MCP más robustas, seguras y flexibles, conectando conceptos fundamentales con patrones avanzados de producción.

## 29 de septiembre de 2025

### Laboratorios de Integración de Base de Datos para Servidores MCP - Ruta de Aprendizaje Práctica Integral

#### 11-MCPServerHandsOnLabs - Nuevo Currículo Completo de Integración de Base de Datos
- **Ruta de Aprendizaje Completa de 13 Laboratorios**: Se añadió un currículo práctico completo para construir servidores MCP listos para producción con integración de base de datos PostgreSQL
  - **Implementación en el Mundo Real**: Caso de uso de analítica Zava Retail demostrando patrones de nivel empresarial
  - **Progresión de Aprendizaje Estructurada**:
    - **Laboratorios 00-03: Fundamentos** - Introducción, Arquitectura Central, Seguridad y Multi-Arrendamiento, Configuración de Entorno
    - **Laboratorios 04-06: Construcción del Servidor MCP** - Diseño y Esquema de Base de Datos, Implementación de Servidor MCP, Desarrollo de Herramientas  
    - **Laboratorios 07-09: Funcionalidades Avanzadas** - Integración de Búsqueda Semántica, Pruebas y Depuración, Integración con VS Code
    - **Laboratorios 10-12: Producción y Mejores Prácticas** - Estrategias de Despliegue, Monitoreo y Observabilidad, Mejores Prácticas y Optimización
  - **Tecnologías Empresariales**: Framework FastMCP, PostgreSQL con pgvector, embeddings de Azure OpenAI, Azure Container Apps, Application Insights
  - **Características Avanzadas**: Seguridad a Nivel de Fila (RLS), búsqueda semántica, acceso multi-arrendatario a datos, embeddings vectoriales, monitoreo en tiempo real

#### Estandarización de Terminología - Conversión de Módulo a Laboratorio
- **Actualización Documental Integral**: Se actualizaron sistemáticamente todos los archivos README en 11-MCPServerHandsOnLabs para usar la terminología "Laboratorio" en lugar de "Módulo"
  - **Encabezados de Sección**: Se actualizó "Lo que cubre este módulo" a "Lo que cubre este laboratorio" en los 13 laboratorios
  - **Descripción de Contenido**: Se cambió "Este módulo provee..." a "Este laboratorio provee..." a lo largo de la documentación
  - **Objetivos de Aprendizaje**: Se actualizó "Al final de este módulo..." a "Al final de este laboratorio..." 
  - **Enlaces de Navegación**: Se convirtieron todas las referencias "Módulo XX:" a "Laboratorio XX:" en referencias cruzadas y navegación
  - **Seguimiento de Finalización**: Se actualizó "Después de completar este módulo..." a "Después de completar este laboratorio..."
  - **Referencias Técnicas Conservadas**: Se mantuvieron las referencias a módulos Python en archivos de configuración (p.ej., `"module": "mcp_server.main"`)

#### Mejora de la Guía de Estudio (study_guide.md)
- **Mapa Visual del Currículo**: Se añadió la nueva sección "11. Laboratorios de Integración de Bases de Datos" con visualización completa de la estructura de laboratorios
- **Estructura del Repositorio**: Se actualizó de diez a once secciones principales con descripción detallada de 11-MCPServerHandsOnLabs
- **Guía del Camino de Aprendizaje**: Se mejoraron las instrucciones de navegación para cubrir secciones 00-11
- **Cobertura Tecnológica**: Se añadieron detalles de FastMCP, PostgreSQL e integración con servicios de Azure
- **Resultados de Aprendizaje**: Se enfatizó el desarrollo de servidores listos para producción, patrones de integración de bases de datos y seguridad empresarial

#### Mejora de la Estructura del README Principal
- **Terminología Basada en Laboratorios**: Se actualizó el README.md principal en 11-MCPServerHandsOnLabs para usar consistentemente la estructura "Laboratorio"
- **Organización del Camino de Aprendizaje**: Progresión clara desde conceptos fundamentales hasta implementación avanzada y despliegue en producción
- **Enfoque en el Mundo Real**: Énfasis en el aprendizaje práctico con patrones y tecnologías de nivel empresarial

### Mejoras de Calidad y Consistencia en la Documentación
- **Énfasis en Aprendizaje Práctico**: Refuerzo del enfoque basado en laboratorios en toda la documentación
- **Foco en Patrones Empresariales**: Destacado en implementaciones listas para producción y consideraciones de seguridad empresarial
- **Integración Tecnológica**: Cobertura completa de servicios modernos de Azure e integración con patrones de IA
- **Progresión de Aprendizaje**: Camino claro y estructurado desde conceptos básicos hasta despliegue en producción

## 26 de septiembre de 2025

### Mejora de Estudios de Caso - Integración del Registro MCP en GitHub

#### Estudios de Caso (09-CaseStudy/) - Enfoque en Desarrollo de Ecosistema
- **README.md**: Expansión importante con estudio de caso integral sobre el Registro MCP de GitHub
  - **Estudio de Caso del Registro MCP de GitHub**: Nuevo estudio de caso completo que examina el lanzamiento del Registro MCP de GitHub en septiembre de 2025
    - **Análisis del Problema**: Examen detallado de la fragmentación en descubrimiento e implementación de servidores MCP
    - **Arquitectura de Solución**: Enfoque de registro centralizado de GitHub con instalación en un clic para VS Code
    - **Impacto Empresarial**: Mejoras medibles en la incorporación y productividad de desarrolladores
    - **Valor Estratégico**: Enfoque en despliegue modular de agentes e interoperabilidad entre herramientas
    - **Desarrollo del Ecosistema**: Posicionamiento como plataforma fundamental para integración agentica
  - **Estructura Mejorada del Estudio de Caso**: Actualizados los siete estudios de caso con formato consistente y descripciones completas
    - Agentes de Viajes AI Azure: Énfasis en orquestación multi-agente
    - Integración Azure DevOps: Enfoque en automatización de flujos de trabajo
    - Recuperación de Documentación en Tiempo Real: Implementación de cliente de consola Python
    - Generador de Planes de Estudio Interactivo: Aplicación web conversacional Chainlit
    - Documentación en el Editor: Integración VS Code y GitHub Copilot
    - Azure API Management: Patrones de integración de API empresariales
    - Registro MCP GitHub: Desarrollo de ecosistema y plataforma comunitaria
  - **Conclusión Integral**: Sección de conclusión reescrita destacando siete estudios de caso que cubren múltiples dimensiones de implementación MCP
    - Integración Empresarial, Orquestación Multi-Agente, Productividad del Desarrollador
    - Desarrollo del Ecosistema, Aplicaciones Educativas como categorización
    - Perspectivas mejoradas sobre patrones arquitectónicos, estrategias de implementación y mejores prácticas
    - Énfasis en MCP como protocolo maduro y listo para producción

#### Actualizaciones en la Guía de Estudio (study_guide.md)
- **Mapa Visual del Currículo**: Actualizado el mapa mental para incluir el Registro MCP de GitHub en la sección de Estudios de Caso
- **Descripción de Estudios de Caso**: Mejorada de descripciones genéricas a desglose detallado de siete estudios de caso integrales
- **Estructura del Repositorio**: Se actualizó la sección 10 para reflejar cobertura completa de estudios de caso con detalles específicos de implementación
- **Integración del Changelog**: Se añadió la entrada del 26 de septiembre de 2025 documentando la adición del Registro MCP de GitHub y mejoras en estudios de caso
- **Actualizaciones de Fecha**: Se actualizó la marca temporal del pie de página para reflejar la última revisión (26 de septiembre de 2025)

### Mejoras en la Calidad de la Documentación
- **Mejora de Consistencia**: Formato y estructura estandarizados de los estudios de caso en los siete ejemplos
- **Cobertura Integral**: Los estudios de caso ahora abarcan escenarios empresariales, de productividad de desarrolladores y desarrollo de ecosistemas
- **Posicionamiento Estratégico**: Mayor énfasis en MCP como plataforma fundamental para despliegue de sistemas agenticos
- **Integración de Recursos**: Se actualizaron recursos adicionales para incluir el enlace al Registro MCP de GitHub

## 15 de septiembre de 2025

### Expansión de Temas Avanzados - Transportes Personalizados e Ingeniería de Contextos

#### Transportes Personalizados MCP (05-AdvancedTopics/mcp-transport/) - Nueva Guía de Implementación Avanzada
- **README.md**: Guía completa de implementación para mecanismos personalizados de transporte MCP
  - **Transporte Azure Event Grid**: Implementación completa de transporte sin servidor basado en eventos
    - Ejemplos en C#, TypeScript y Python con integración de Azure Functions
    - Patrones de arquitectura orientada a eventos para soluciones MCP escalables
    - Receptores de webhooks y manejo de mensajes push
  - **Transporte Azure Event Hubs**: Implementación de transporte de streaming de alto rendimiento
    - Capacidades de streaming en tiempo real para escenarios de baja latencia
    - Estrategias de particionamiento y gestión de checkpoints
    - Agrupación de mensajes y optimización del rendimiento
  - **Patrones de Integración Empresarial**: Ejemplos arquitectónicos listos para producción
    - Procesamiento MCP distribuido a través de múltiples Azure Functions
    - Arquitecturas híbridas de transporte combinando múltiples tipos de transporte
    - Durabilidad, confiabilidad y estrategias de manejo de errores en mensajes
  - **Seguridad y Monitoreo**: Integración con Azure Key Vault y patrones de observabilidad
    - Autenticación con identidad administrada y acceso de mínimo privilegio
    - Telemetría de Application Insights y monitoreo de rendimiento
    - Disyuntores y patrones de tolerancia a fallos
  - **Frameworks de Pruebas**: Estrategias completas de pruebas para transportes personalizados
    - Pruebas unitarias con dobles de prueba y frameworks de mocking
    - Pruebas de integración con Azure Test Containers
    - Consideraciones para pruebas de rendimiento y carga

#### Ingeniería de Contextos (05-AdvancedTopics/mcp-contextengineering/) - Disciplina Emergente de IA
- **README.md**: Exploración completa de la ingeniería de contextos como campo emergente
  - **Principios Fundamentales**: Compartición completa de contextos, conciencia de decisiones de acción y gestión de la ventana de contexto

  - **Alineación del Protocolo MCP**: Cómo el diseño del MCP aborda los desafíos de la ingeniería de contexto
    - Limitaciones de la ventana de contexto y estrategias de carga progresiva
    - Determinación de relevancia y recuperación dinámica del contexto
    - Manejo de contexto multimodal y consideraciones de seguridad
  - **Enfoques de Implementación**: Arquitecturas de un solo hilo vs. multiagente
    - Técnicas de segmentación y priorización del contexto
    - Estrategias de carga progresiva y compresión del contexto
    - Enfoques de contexto por capas y optimización de recuperación
  - **Marco de Medición**: Métricas emergentes para la evaluación de la eficacia del contexto
    - Eficiencia de entrada, rendimiento, calidad y consideraciones de experiencia de usuario
    - Enfoques experimentales para la optimización del contexto
    - Análisis de fallos y metodologías de mejora

#### Actualizaciones de Navegación del Currículo (README.md)
- **Estructura Mejorada del Módulo**: Tabla del currículo actualizada para incluir nuevos temas avanzados
  - Se añadieron entradas de Ingeniería de Contexto (5.14) y Transporte Personalizado (5.15)
  - Formato consistente y enlaces de navegación en todos los módulos
  - Descripciones actualizadas para reflejar el alcance actual del contenido

### Mejoras en la Estructura de Directorios
- **Estandarización de Nombres**: Renombrado "mcp transport" a "mcp-transport" para consistencia con otras carpetas de temas avanzados
- **Organización de Contenido**: Todas las carpetas 05-AdvancedTopics ahora siguen un patrón de nomenclatura consistente (mcp-[tema])

### Mejoras en la Calidad de la Documentación
- **Alineación con la Especificación MCP**: Todo el contenido nuevo referencia la Especificación MCP actual 2025-06-18
- **Ejemplos Multilingües**: Ejemplos de código completos en C#, TypeScript y Python
- **Enfoque Empresarial**: Patrones listos para producción e integración con la nube Azure en todo el contenido
- **Documentación Visual**: Diagramas Mermaid para visualización de arquitectura y flujos

## 18 de agosto de 2025

### Actualización Integral de Documentación - Estándares MCP 2025-06-18

#### Mejores Prácticas de Seguridad MCP (02-Security/) - Modernización Completa
- **MCP-SECURITY-BEST-PRACTICES-2025.md**: Reescritura completa alineada con la Especificación MCP 2025-06-18
  - **Requisitos Obligatorias**: Añadidos requisitos explícitos DEBE/NO DEBE de la especificación oficial con indicadores visuales claros
  - **12 Prácticas Clave de Seguridad**: Reestructuradas de una lista de 15 ítems a dominios de seguridad comprensivos
    - Seguridad de Tokens y Autenticación con integración de proveedor de identidad externo
    - Gestión de Sesiones y Seguridad de Transporte con requisitos criptográficos
    - Protección Específica contra Amenazas de IA con integración de Microsoft Prompt Shields
    - Control de Acceso y Permisos con principio de mínimo privilegio
    - Seguridad y Monitoreo de Contenidos con integración de Azure Content Safety
    - Seguridad en la Cadena de Suministro con verificación exhaustiva de componentes
    - Seguridad OAuth y Prevención de "Deputy Confundido" con implementación PKCE
    - Respuesta a Incidentes y Recuperación con capacidades automatizadas
    - Cumplimiento y Gobernanza con alineación regulatoria
    - Controles Avanzados de Seguridad con arquitectura de confianza cero
    - Integración con el Ecosistema de Seguridad Microsoft con soluciones completas
    - Evolución Continua de la Seguridad con prácticas adaptativas
  - **Soluciones de Seguridad Microsoft**: Guía de integración mejorada para Prompt Shields, Azure Content Safety, Entra ID y GitHub Advanced Security
  - **Recursos de Implementación**: Enlaces de recursos categorizados por Documentación Oficial MCP, Soluciones de Seguridad Microsoft, Estándares de Seguridad y Guías de Implementación

#### Controles Avanzados de Seguridad (02-Security/) - Implementación Empresarial
- **MCP-SECURITY-CONTROLS-2025.md**: Renovación completa con marco de seguridad a nivel empresarial
  - **9 Dominios de Seguridad Comprensivos**: Ampliados de controles básicos a marco detallado para empresa
    - Autenticación y Autorización Avanzadas con integración Microsoft Entra ID
    - Seguridad de Tokens y Controles Anti-Passthrough con validación exhaustiva
    - Controles de Seguridad de Sesión con prevención de secuestros
    - Controles de Seguridad Específicos para IA con prevención de inyección de prompts y envenenamiento de herramientas
    - Prevención de Ataques de "Deputy Confundido" con seguridad de proxy OAuth
    - Seguridad en la Ejecución de Herramientas con sandboxing y aislamiento
    - Controles de Seguridad en la Cadena de Suministro con verificación de dependencias
    - Controles de Monitoreo y Detección con integración SIEM
    - Respuesta a Incidentes y Recuperación con capacidades automatizadas
  - **Ejemplos de Implementación**: Añadidos bloques detallados de configuración YAML y ejemplos de código
  - **Integración con Soluciones Microsoft**: Cobertura completa de servicios de seguridad Azure, GitHub Advanced Security y gestión de identidad empresarial

#### Seguridad de Temas Avanzados (05-AdvancedTopics/mcp-security/) - Implementación Lista para Producción
- **README.md**: Reescritura completa para implementación de seguridad empresarial
  - **Alineación con Especificación Actual**: Actualizado a Especificación MCP 2025-06-18 con requisitos obligatorios de seguridad
  - **Autenticación Mejorada**: Integración Microsoft Entra ID con ejemplos completos en .NET y Java Spring Security
  - **Integración de Seguridad IA**: Implementación Microsoft Prompt Shields y Azure Content Safety con ejemplos detallados en Python
  - **Mitigación Avanzada de Amenazas**: Ejemplos comprensivos de implementación para
    - Prevención de ataques de "Deputy Confundido" con PKCE y validación de consentimiento del usuario
    - Prevención de Passthrough de Tokens con validación de audiencia y gestión segura de tokens
    - Prevención de Secuestro de Sesiones con enlace criptográfico y análisis comportamental
  - **Integración de Seguridad Empresarial**: Monitoreo con Azure Application Insights, pipelines de detección de amenazas y seguridad en la cadena de suministro
  - **Lista de Verificación de Implementación**: Controles de seguridad claros obligatorios vs. recomendados con beneficios del ecosistema de seguridad Microsoft

### Calidad de Documentación y Alineación con Estándares
- **Referencias a Especificaciones**: Actualizadas todas las referencias a la Especificación MCP vigente 2025-06-18
- **Ecosistema de Seguridad Microsoft**: Guías de integración mejoradas en toda la documentación de seguridad
- **Implementación Práctica**: Añadidos ejemplos detallados de código en .NET, Java y Python con patrones empresariales
- **Organización de Recursos**: Categorización comprensiva de documentación oficial, estándares de seguridad y guías de implementación
- **Indicadores Visuales**: Marcado claro de requisitos obligatorios vs. prácticas recomendadas


#### Conceptos Básicos (01-CoreConcepts/) - Modernización Completa
- **Actualización de Versión de Protocolo**: Actualizado para referenciar la Especificación MCP vigente 2025-06-18 con versionado basado en fecha (formato AAAA-MM-DD)
- **Refinamiento de Arquitectura**: Descripciones mejoradas de Hosts, Clientes y Servidores para reflejar patrones actuales de arquitectura MCP
  - Hosts ahora claramente definidos como aplicaciones de IA que coordinan múltiples conexiones clientes MCP
  - Clientes descritos como conectores de protocolo que mantienen relaciones uno a uno con servidores
  - Servidores mejorados con escenarios de despliegue local vs. remoto
- **Reestructuración de Primitivas**: Renovación completa de primitivas de servidor y cliente
  - Primitivas de Servidor: Recursos (fuentes de datos), Prompts (plantillas), Herramientas (funciones ejecutables) con explicaciones detalladas y ejemplos
  - Primitivas de Cliente: Muestreo (completaciones LLM), Solicitud (entrada de usuario), Registro (depuración/monitoreo)
  - Actualizado con patrones actuales de métodos de descubrimiento (`*/list`), recuperación (`*/get`) y ejecución (`*/call`)
- **Arquitectura de Protocolo**: Introducido modelo de arquitectura de dos capas
  - Capa de Datos: Base JSON-RPC 2.0 con gestión de ciclo de vida y primitivas
  - Capa de Transporte: STDIO (local) y HTTP en streaming con SSE (transporte remoto)
- **Marco de Seguridad**: Principios de seguridad comprensivos incluyendo consentimiento explícito del usuario, protección de privacidad de datos, seguridad en ejecución de herramientas y seguridad en capa de transporte
- **Patrones de Comunicación**: Mensajes de protocolo actualizados para mostrar flujos de inicialización, descubrimiento, ejecución y notificación
- **Ejemplos de Código**: Ejemplos multilingües actualizados (.NET, Java, Python, JavaScript) para reflejar patrones actuales del SDK MCP

#### Seguridad (02-Security/) - Renovación Integral de Seguridad  
- **Alineación con Estándares**: Total alineación con requisitos de seguridad de la Especificación MCP 2025-06-18
- **Evolución de Autenticación**: Documentación de evolución desde servidores OAuth custom a delegación con proveedor de identidad externo (Microsoft Entra ID)
- **Análisis de Amenazas Específicas de IA**: Cobertura mejorada de vectores de ataque modernos en IA
  - Escenarios detallados de ataques de inyección de prompts con ejemplos del mundo real
  - Mecanismos de envenenamiento de herramientas y patrones de ataque "rug pull"
  - Envenenamiento de ventana de contexto y ataques de confusión de modelo
- **Soluciones de Seguridad Microsoft para IA**: Cobertura comprensiva del ecosistema de seguridad Microsoft
  - AI Prompt Shields con técnicas avanzadas de detección, focalización y delimitadores
  - Patrones de integración Azure Content Safety
  - GitHub Advanced Security para protección de cadena de suministro
- **Mitigación Avanzada de Amenazas**: Controles de seguridad detallados para
  - Secuestro de sesiones con escenarios de ataque específicos MCP y requisitos criptográficos para ID de sesión
  - Problemas de deputy confundido en escenarios de proxy MCP con requisitos explícitos de consentimiento
  - Vulnerabilidades de passthrough de tokens con controles de validación obligatorios
- **Seguridad en la Cadena de Suministro**: Cobertura ampliada de cadena de suministro de IA incluyendo modelos fundacionales, servicios de embeddings, proveedores de contexto y APIs de terceros
- **Seguridad Fundacional**: Integración mejorada con patrones de seguridad empresarial incluyendo arquitectura de confianza cero y ecosistema de seguridad Microsoft
- **Organización de Recursos**: Enlaces de recursos categorizados por tipo (Documentación Oficial, Estándares, Investigación, Soluciones Microsoft, Guías de Implementación)

### Mejoras en la Calidad de la Documentación
- **Objetivos de Aprendizaje Estructurados**: Objetivos de aprendizaje mejorados con resultados específicos y accionables
- **Referencias Cruzadas**: Enlaces añadidos entre temas relacionados de seguridad y conceptos básicos
- **Información Actualizada**: Actualizadas todas las referencias de fecha y enlaces de especificación a estándares actuales
- **Guía de Implementación**: Añadidas directrices específicas y accionables a lo largo de ambas secciones

## 16 de julio de 2025

### Mejoras en README y Navegación
- Rediseñada completamente la navegación del currículo en README.md
- Reemplazadas las etiquetas `<details>` por un formato basado en tablas más accesible
- Creada carpeta "alternative_layouts" con opciones alternativas de diseño
- Añadidos ejemplos de navegación con tarjetas, pestañas y acordeones
- Actualizada sección de estructura del repositorio para incluir todos los archivos más recientes
- Mejorada sección "Cómo usar este currículo" con recomendaciones claras
- Actualizados enlaces de especificación MCP para apuntar a las URLs correctas
- Añadida sección de Ingeniería de Contexto (5.14) a la estructura del currículo

### Actualizaciones de Guía de Estudio
- Revisión completa de la guía de estudio para alinear con la estructura actual del repositorio
- Añadidas nuevas secciones para Clientes y Herramientas MCP, y Servidores MCP Populares
- Actualizado el Mapa Curricular Visual para reflejar con precisión todos los temas
- Mejora en las descripciones de Temas Avanzados para cubrir todas las áreas especializadas
- Actualizada la sección de Estudios de Caso para reflejar ejemplos reales
- Añadido este registro de cambios comprensivo

### Contribuciones de la Comunidad (06-CommunityContributions/)
- Añadida información detallada sobre servidores MCP para generación de imágenes
- Añadida sección comprensiva sobre el uso de Claude en VSCode
- Añadidas instrucciones para configuración y uso del cliente terminal Cline
- Actualizada sección de cliente MCP para incluir todas las opciones populares
- Mejorados ejemplos de contribución con muestras de código más precisas

### Temas Avanzados (05-AdvancedTopics/)
- Organizadas todas las carpetas de temas especializados con nomenclatura consistente
- Añadidos materiales y ejemplos de ingeniería de contexto
- Añadida documentación de integración del agente Foundry
- Mejorada documentación de integración de seguridad Entra ID

## 11 de junio de 2025

### Creación Inicial
- Lanzada primera versión del currículo MCP para Principiantes
- Creada estructura básica para las 10 secciones principales
- Implementado Mapa Curricular Visual para navegación
- Añadidos proyectos de muestra iniciales en múltiples lenguajes de programación

### Comenzando (03-GettingStarted/)
- Creación de primeros ejemplos de implementación de servidor
- Añadida guía para desarrollo de clientes
- Incluidas instrucciones de integración de cliente LLM
- Añadida documentación de integración en VS Code
- Implementados ejemplos de servidor con Eventos Enviados desde el Servidor (SSE)

### Conceptos Básicos (01-CoreConcepts/)
- Añadida explicación detallada de arquitectura cliente-servidor
- Creada documentación sobre componentes clave del protocolo
- Documentados patrones de mensajería en MCP

## 23 de mayo de 2025

### Estructura del Repositorio
- Inicializado el repositorio con estructura básica de carpetas
- Creación de archivos README para cada sección principal
- Configurada infraestructura de traducción
- Añadidos recursos gráficos y diagramas

### Documentación
- Creado README.md inicial con visión general del currículo
- Añadidos CODE_OF_CONDUCT.md y SECURITY.md
- Configurado SUPPORT.md con orientación para obtener ayuda
- Creada estructura preliminar de guía de estudio

## 15 de abril de 2025

### Planificación y Marco de Trabajo
- Planificación inicial para el currículo MCP para Principiantes
- Definidos objetivos de aprendizaje y público objetivo
- Esbozada estructura de 10 secciones del currículo
- Desarrollado marco conceptual para ejemplos y estudios de caso
- Creación de prototipos iniciales de ejemplos para conceptos clave

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Descargo de responsabilidad**:
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional humana. No somos responsables de cualquier malentendido o interpretación errónea que surja del uso de esta traducción.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->