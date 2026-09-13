# Seguridad MCP: Protección Integral para Sistemas de IA

[![Buenas Prácticas de Seguridad MCP](../../../translated_images/es/03.175aed6dedae133f.webp)](https://youtu.be/88No8pw706o)

_(Haga clic en la imagen de arriba para ver el video de esta lección)_

La seguridad es fundamental en el diseño de sistemas de IA, por eso la priorizamos como nuestra segunda sección. Esto está alineado con el principio **Seguro por Diseño** de Microsoft en la [Iniciativa Futuro Seguro](https://www.microsoft.com/security/blog/2025/04/17/microsofts-secure-by-design-journey-one-year-of-success/).

El Protocolo de Contexto del Modelo (MCP) aporta nuevas capacidades poderosas a las aplicaciones impulsadas por IA, mientras presenta desafíos únicos de seguridad que van más allá de los riesgos tradicionales del software. Los sistemas MCP enfrentan tanto preocupaciones de seguridad establecidas (codificación segura, mínimo privilegio, seguridad de la cadena de suministro) como nuevas amenazas específicas de IA, incluyendo inyección de instrucciones, envenenamiento de herramientas, secuestro de sesiones, ataques de apoderado confundido, vulnerabilidades de pase de tokens y modificación dinámica de capacidades.

Esta lección explora los riesgos de seguridad más críticos en implementaciones MCP, cubriendo autenticación, autorización, permisos excesivos, inyección indirecta de instrucciones, seguridad de sesión, problemas de apoderado confundido, gestión de tokens y vulnerabilidades en la cadena de suministro. Aprenderá controles prácticos y mejores prácticas para mitigar estos riesgos mientras aprovecha soluciones de Microsoft como Prompt Shields, Azure Content Safety y GitHub Advanced Security para fortalecer su despliegue MCP.

## Objetivos de Aprendizaje

Al final de esta lección, usted podrá:

- **Identificar Amenazas Específicas MCP**: Reconocer riesgos únicos de seguridad en sistemas MCP, incluyendo inyección de instrucciones, envenenamiento de herramientas, permisos excesivos, secuestro de sesiones, problemas de apoderado confundido, vulnerabilidades de pase de tokens y riesgos en la cadena de suministro
- **Aplicar Controles de Seguridad**: Implementar mitigaciones efectivas que incluyen autenticación robusta, acceso con mínimo privilegio, gestión segura de tokens, controles de seguridad de sesión y verificación de la cadena de suministro
- **Aprovechar Soluciones de Seguridad Microsoft**: Comprender y desplegar Microsoft Prompt Shields, Azure Content Safety y GitHub Advanced Security para protección de cargas MCP
- **Validar la Seguridad de Herramientas**: Reconocer la importancia de la validación de metadatos de herramientas, monitoreo de cambios dinámicos y defensa contra ataques indirectos de inyección de instrucciones
- **Integrar Mejores Prácticas**: Combinar fundamentos establecidos de seguridad (codificación segura, endurecimiento de servidores, confianza cero) con controles específicos MCP para protección integral

# Arquitectura y Controles de Seguridad MCP

Las implementaciones modernas de MCP requieren enfoques de seguridad en capas que aborden tanto la seguridad tradicional del software como las amenazas específicas de IA. La especificación MCP evoluciona rápidamente madurando sus controles de seguridad, permitiendo una mejor integración con arquitecturas de seguridad empresariales y mejores prácticas establecidas.

Investigaciones del [Informe de Defensa Digital de Microsoft](https://aka.ms/mddr) demuestran que **el 98% de las brechas reportadas serían prevenidas con una higiene robusta de seguridad**. La estrategia de protección más efectiva combina prácticas de seguridad fundamentales con controles específicos MCP—las medidas básicas de seguridad probadas siguen siendo las de mayor impacto para reducir el riesgo general de seguridad.

## Panorama Actual de Seguridad

> **Nota:** Este capítulo combina controles de seguridad MCP establecidos con la
> guía actual de autorización de la **Especificación MCP 2026-07-28**. Siempre consulte
> la más reciente [Especificación MCP](https://modelcontextprotocol.io/specification/2026-07-28/),
> [repositorio MCP en GitHub](https://github.com/modelcontextprotocol), y
> [documentación de mejores prácticas de seguridad](https://modelcontextprotocol.io/specification/2026-07-28/basic/security_best_practices)
> al implementar código sensible a la seguridad.

> **Actualización de autorización:** MCP `2026-07-28` requiere que los clientes validen el
> parámetro `iss` en respuestas de autorización (RFC 9207) y vinculen credenciales
> registradas con el servidor de autorización emisor. La Inscripción Dinámica de Clientes
> está obsoleta; las nuevas implementaciones deben usar Documentos de Metadatos ID de Cliente.
> Vea [Cambios en MCP: La Especificación 2026-07-28](../01-CoreConcepts/mcp-2026-07-28.md)
> para la lista completa de cambios en autorización.

## 🏔️ Taller MCP Security Summit (Sherpa)

Para **entrenamiento práctico en seguridad**, recomendamos altamente el **Taller MCP Security Summit** (Sherpa) — una expedición guiada integral para asegurar servidores MCP en Microsoft Azure.

### Resumen del Taller

El [Taller MCP Security Summit](https://azure-samples.github.io/sherpa/) ofrece entrenamiento práctico y accionable a través de una metodología probada de "vulnerable → explotar → corregir → validar". Usted:

- **Aprende Rompiendo Cosas**: Experimente vulnerabilidades de primera mano explotando servidores intencionalmente inseguros
- **Utiliza Seguridad Nativa de Azure**: Aproveche Azure Entra ID, Key Vault, API Management y AI Content Safety
- **Sigue Defensa en Profundidad**: Progrese a través de campamentos construyendo capas de seguridad completas
- **Aplica Estándares OWASP**: Cada técnica se corresponde con la [Guía de Seguridad MCP Azure de OWASP](https://microsoft.github.io/mcp-azure-security-guide/)
- **Obtén Código de Producción**: Lleve implementaciones funcionando y probadas

### Ruta de la Expedición

| Campamento | Enfoque | Riesgos OWASP Cubiertos |
|------|-------|---------------------|
| **Campamento Base** | Fundamentos MCP & vulnerabilidades de autenticación | MCP01, MCP07 |
| **Campamento 1: Identidad** | OAuth 2.1, identidad gestionada de Azure, Key Vault | MCP01, MCP02, MCP07 |
| **Campamento 2: Gateway** | API Management, puntos finales privados, gobernanza | MCP02, MCP06, MCP07, MCP09 |
| **Campamento 3: Seguridad I/O** | Inyección de instrucciones, protección PII, seguridad de contenido | MCP03, MCP05, MCP06, MCP10 |
| **Campamento 4: Monitoreo** | Log Analytics, paneles, detección de amenazas | MCP04, MCP08 |
| **La Cumbre** | Prueba de integración Red Team / Blue Team | Todos |

**Comience aquí**: [https://azure-samples.github.io/sherpa/](https://azure-samples.github.io/sherpa/)

## Los 10 Principales Riesgos de Seguridad MCP de OWASP

La [Guía de Seguridad MCP Azure de OWASP](https://microsoft.github.io/mcp-azure-security-guide/) detalla los diez riesgos de seguridad más críticos para implementaciones MCP:

| Riesgo | Descripción | Mitigación Azure |
|------|-------------|------------------|
| **MCP01** | Mala Gestión de Tokens y Exposición de Secretos | Azure Key Vault, Identidad Gestionada |
| **MCP02** | Escalamiento de Privilegios por Ampliación de Alcance | RBAC, Acceso Condicional |
| **MCP03** | Envenenamiento de Herramientas | Validación de herramientas, verificación de integridad |
| **MCP04** | Ataques a la Cadena de Suministro de Software y Manipulación de Dependencias | GitHub Advanced Security, escaneo de dependencias |
| **MCP05** | Inyección y Ejecución de Comandos | Validación de entradas, sandboxing |
| **MCP06** | Subversión del Flujo de Intención | Azure AI Content Safety, Prompt Shields |
| **MCP07** | Autenticación & Autorización Insuficientes | Azure Entra ID, OAuth 2.1 con PKCE |
| **MCP08** | Falta de Auditoría y Telemetría | Azure Monitor, Application Insights |
| **MCP09** | Servidores MCP Sombras | Gobernanza API Center, aislamiento de red |
| **MCP10** | Inyección de Contexto y Sobre-Exposición | Clasificación de datos, exposición mínima |

### Evolución de la Autenticación MCP

La especificación MCP ha evolucionado significativamente en su enfoque de autenticación y autorización:

- **Enfoque Original**: Las especificaciones iniciales requerían que los desarrolladores implementaran servidores de autenticación personalizados, con servidores MCP actuando como Servidores de Autorización OAuth 2.0 que gestionaban la autenticación de usuarios directamente
- **Estándar Actual (`2026-07-28`)**: Los servidores MCP pueden delegar autenticación
  a proveedores de identidad externos como Microsoft Entra ID. Los clientes también deben
  aplicar los requisitos actuales de validación del emisor y vinculación de credenciales.
- **Seguridad en la Capa de Transporte**: Soporte mejorado para mecanismos de transporte seguro con patrones adecuados de autenticación para conexiones locales (STDIO) y remotas (HTTP transmitible)

## Seguridad en Autenticación y Autorización

### Desafíos Actuales de Seguridad

Las implementaciones modernas de MCP enfrentan varios desafíos en autenticación y autorización:

### Riesgos y Vectores de Amenaza

- **Lógica de Autorización Mal Configurada**: Implementación defectuosa de autorización en servidores MCP puede exponer datos sensibles y aplicar controles de acceso incorrectamente
- **Compromiso de Tokens OAuth**: El robo de tokens de servidores MCP locales permite a atacantes suplantar servidores y acceder a servicios descendentes
- **Vulnerabilidades de Pase de Tokens**: Manejo inapropiado de tokens genera omisiones en controles de seguridad y brechas de responsabilidad
- **Permisos Excesivos**: Servidores MCP con privilegios excesivos violan principios de mínimo privilegio y amplían superficies de ataque

#### Pase de Tokens: Un Anti-Patrón Crítico

**El pase de tokens está explícitamente prohibido** en la especificación actual de autorización MCP debido a sus severas implicaciones de seguridad:

##### Circunvención de Controles de Seguridad
- Servidores MCP y APIs descendentes implementan controles críticos de seguridad (limitación de tasa, validación de solicitudes, monitoreo de tráfico) que dependen de la validación correcta del token
- El uso directo de tokens cliente a API elude estas protecciones esenciales, debilitando la arquitectura de seguridad

##### Retos de Responsabilidad y Auditoría  
- Los servidores MCP no pueden diferenciar entre clientes usando tokens emitidos upstream, rompiendo las trazas de auditoría
- Los registros de servidores de recursos downstream muestran orígenes de solicitudes engañosos en lugar de verdaderos intermediarios MCP
- La investigación de incidentes y auditorías de cumplimiento se vuelven mucho más difíciles

##### Riesgos de Exfiltración de Datos
- Reclamaciones de tokens no validadas permiten a actores maliciosos con tokens robados usar servidores MCP como proxies para exfiltrar datos
- Violaciones del límite de confianza permiten patrones de acceso no autorizados que eluden controles de seguridad previstos

##### Vectores de Ataque Multi-Servicio
- Tokens comprometidos aceptados por múltiples servicios facilitan movimientos laterales a través de sistemas conectados
- Suposiciones de confianza entre servicios pueden violarse cuando no pueden verificarse los orígenes de los tokens

### Controles y Mitigaciones de Seguridad

**Requisitos Críticos de Seguridad:**

> **OBLIGATORIO**: Los servidores MCP **NO DEBEN** aceptar ningún token que no haya sido explícitamente emitido para el servidor MCP

#### Controles de Autenticación y Autorización

- **Revisión Rigurosa de Autorización**: Realice auditorías exhaustivas de la lógica de autorización del servidor MCP para asegurar que sólo usuarios y clientes previstos accedan a recursos sensibles
  - **Guía de Implementación**: [Azure API Management como Gateway de Autenticación para Servidores MCP](https://techcommunity.microsoft.com/blog/integrationsonazureblog/azure-api-management-your-auth-gateway-for-mcp-servers/4402690)
  - **Integración de Identidad**: [Uso de Microsoft Entra ID para Autenticación de Servidor MCP](https://den.dev/blog/mcp-server-auth-entra-id-session/)

- **Gestión Segura de Tokens**: Implemente [las mejores prácticas de validación y ciclo de vida de tokens de Microsoft](https://learn.microsoft.com/en-us/entra/identity-platform/access-tokens)
  - Validar que las reclamaciones de audiencia del token coincidan con la identidad del servidor MCP
  - Implementar rotación y expiración adecuada de tokens
  - Prevenir ataques de repetición y uso no autorizado de tokens

- **Almacenamiento Protegido de Tokens**: Almacene tokens de forma segura con cifrado en reposo y en tránsito
  - **Mejores Prácticas**: [Directrices para almacenamiento y cifrado seguros de tokens](https://youtu.be/uRdX37EcCwg?si=6fSChs1G4glwXRy2)

#### Implementación de Control de Acceso

- **Principio de Mínimo Privilegio**: Conceda a los servidores MCP sólo los permisos mínimos necesarios para la funcionalidad prevista
  - Revisiones regulares de permisos y actualizaciones para evitar ampliación de privilegios
  - **Documentación Microsoft**: [Acceso Seguro con Mínimos Privilegios](https://learn.microsoft.com/entra/identity-platform/secure-least-privileged-access)

- **Control de Acceso Basado en Roles (RBAC)**: Implemente asignaciones finas de roles
  - Delimite roles estrictamente a recursos y acciones específicas
  - Evite permisos amplios o innecesarios que amplíen superficies de ataque

- **Monitoreo Continuo de Permisos**: Implemente auditoría y monitoreo de acceso continuo
  - Supervise patrones de uso de permisos en busca de anomalías
  - Remedie rápidamente privilegios excesivos o no usados

## Amenazas Específicas de Seguridad en IA

### Inyección de Instrucciones y Ataques de Manipulación de Herramientas

Las implementaciones modernas de MCP enfrentan vectores de ataque sofisticados específicos de IA que las medidas de seguridad tradicionales no pueden abordar completamente:

#### **Inyección Indirecta de Instrucciones (Inyección de Instrucciones de Dominio Cruzado)**

La **Inyección Indirecta de Instrucciones** representa una de las vulnerabilidades más críticas en sistemas IA habilitados para MCP. Los atacantes insertan instrucciones maliciosas dentro de contenido externo—documentos, páginas web, correos electrónicos o fuentes de datos—que los sistemas de IA posteriormente procesan como comandos legítimos.

**Escenarios de Ataque:**
- **Inyección basada en Documentos**: Instrucciones maliciosas ocultas en documentos procesados que provocan acciones IA no deseadas
- **Explotación de Contenido Web**: Páginas web comprometidas con instrucciones incrustadas que manipulan el comportamiento IA cuando se recuperan
- **Ataques Basados en Email**: Instrucciones maliciosas en correos que causan que asistentes IA filtren información o realicen acciones no autorizadas
- **Contaminación de Fuentes de Datos**: Bases de datos o APIs comprometidas que sirven contenido tainted a sistemas IA

**Impacto en el Mundo Real**: Estos ataques pueden resultar en exfiltración de datos, violaciones de privacidad, generación de contenido dañino y manipulación de interacciones de usuarios. Para análisis detallado, vea [Inyección de Instrucciones en MCP (Simon Willison)](https://simonwillison.net/2025/Apr/9/mcp-prompt-injection/).

![Diagrama de Ataque de Inyección de Instrucciones](../../../translated_images/es/prompt-injection.ed9fbfde297ca877.webp)

#### **Ataques de Envenenamiento de Herramientas**

El **Envenenamiento de Herramientas** apunta a los metadatos que definen herramientas MCP, explotando cómo los modelos LLM interpretan descripciones y parámetros de herramientas para tomar decisiones de ejecución.

**Mecanismos de Ataque:**
- **Manipulación de Metadatos**: Atacantes inyectan instrucciones maliciosas en descripciones de herramientas, definiciones de parámetros o ejemplos de uso
- **Instrucciones Invisibles**: Instrucciones ocultas en metadatos de herramientas que los modelos IA procesan pero que son invisibles para usuarios humanos
- **Modificación Dinámica de Herramientas ("Rug Pulls")**: Herramientas aprobadas por usuarios son modificadas después para ejecutar acciones maliciosas sin que el usuario lo sepa
- **Inyección de Parámetros**: Contenido malicioso incrustado en esquemas de parámetros que influencian el comportamiento del modelo


**Riesgos del Servidor Alojado**: Los servidores MCP remotos presentan riesgos elevados, ya que las definiciones de las herramientas pueden actualizarse después de la aprobación inicial del usuario, creando escenarios donde herramientas previamente seguras se vuelven maliciosas. Para un análisis completo, consulte [Tool Poisoning Attacks (Invariant Labs)](https://invariantlabs.ai/blog/mcp-security-notification-tool-poisoning-attacks).

![Tool Injection Attack Diagram](../../../translated_images/es/tool-injection.3b0b4a6b24de6bef.webp)

#### **Vectores de Ataque Adicionales de IA**

- **Inyección de Prompt Cross-Domain (XPIA)**: Ataques sofisticados que aprovechan contenido de múltiples dominios para evadir controles de seguridad
- **Modificación Dinámica de Capacidades**: Cambios en tiempo real en las capacidades de las herramientas que escapan a evaluaciones de seguridad iniciales
- **Envenenamiento de la Ventana de Contexto**: Ataques que manipulan grandes ventanas de contexto para ocultar instrucciones maliciosas
- **Ataques de Confusión del Modelo**: Explotación de limitaciones del modelo para crear comportamientos impredecibles o inseguros


### Impacto del Riesgo de Seguridad en IA

**Consecuencias de Alto Impacto:**
- **Exfiltración de Datos**: Acceso no autorizado y robo de datos sensibles empresariales o personales
- **Violaciones de Privacidad**: Exposición de información personal identificable (PII) y datos confidenciales empresariales  
- **Manipulación del Sistema**: Modificaciones no intencionadas a sistemas críticos y flujos de trabajo
- **Robo de Credenciales**: Compromiso de tokens de autenticación y credenciales de servicio
- **Movimiento Lateral**: Uso de sistemas IA comprometidos como pivotes para ataques más amplios en la red

### Soluciones de Seguridad de IA de Microsoft

#### **Escudos de Prompt de IA: Protección Avanzada Contra Ataques de Inyección**

Microsoft **Escudos de Prompt de IA** ofrece defensa integral contra ataques de inyección de prompt directos e indirectos mediante múltiples capas de seguridad:

##### **Mecanismos de Protección Principales:**

1. **Detección y Filtrado Avanzados**
   - Algoritmos de aprendizaje automático y técnicas NLP detectan instrucciones maliciosas en contenido externo
   - Análisis en tiempo real de documentos, páginas web, correos electrónicos y fuentes de datos para amenazas incrustadas
   - Comprensión contextual de patrones legítimos vs. maliciosos de prompt

2. **Técnicas de Destacado**  
   - Distingue entre instrucciones de sistema confiables y entradas externas potencialmente comprometidas
   - Métodos de transformación de texto que mejoran la relevancia del modelo mientras aíslan contenido malicioso
   - Ayuda a los sistemas de IA a mantener la jerarquía correcta de instrucciones e ignorar comandos inyectados

3. **Sistemas de Delimitadores y Marcado de Datos**
   - Definición explícita de límites entre mensajes de sistema confiables y texto de entrada externo
   - Marcadores especiales que resaltan los límites entre fuentes de datos confiables y no confiables
   - Separación clara que previene confusiones de instrucciones y ejecución no autorizada de comandos

4. **Inteligencia Continua de Amenazas**
   - Microsoft monitorea continuamente patrones de ataque emergentes y actualiza las defensas
   - Caza proactiva de amenazas para nuevas técnicas de inyección y vectores de ataque
   - Actualizaciones regulares del modelo de seguridad para mantener efectividad frente a amenazas en evolución

5. **Integración con Azure Content Safety**
   - Parte de la suite completa Azure AI Content Safety
   - Detección adicional para intentos de jailbreak, contenido dañino y violaciones de políticas de seguridad
   - Controles de seguridad unificados en componentes de aplicaciones IA

**Recursos de Implementación**: [Documentación de Microsoft Prompt Shields](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)

![Microsoft Prompt Shields Protection](../../../translated_images/es/prompt-shield.ff5b95be76e9c78c.webp)


## Amenazas Avanzadas de Seguridad MCP

### Vulnerabilidades de Secuestro de Sesión

El **secuestro de sesión** representa un vector de ataque crítico en implementaciones MCP con estado donde partes no autorizadas obtienen y abusan de identificadores legítimos de sesión para hacerse pasar por clientes y realizar acciones no autorizadas.

#### **Escenarios de Ataque y Riesgos**

- **Inyección de Prompt por Secuestro de Sesión**: Atacantes con IDs de sesión robados inyectan eventos maliciosos en servidores que comparten estado de sesión, pudiendo activar acciones dañinas o acceder a datos sensibles
- **Impersonación Directa**: IDs de sesión robadas permiten llamadas directas al servidor MCP que evitan autenticación, tratando a los atacantes como usuarios legítimos
- **Streams Reanudables Comprometidos**: Atacantes pueden terminar solicitudes prematuramente, causando que clientes legítimos reanuden con contenido potencialmente malicioso

#### **Controles de Seguridad para Gestión de Sesiones**

**Requisitos Críticos:**
- **Verificación de Autorización**: Los servidores MCP que implementen autorización **DEBEN** verificar TODAS las solicitudes entrantes y **NO DEBEN** confiar en sesiones para autenticación
- **Generación Segura de Sesiones**: Usar IDs de sesión criptográficamente seguros y no determinísticos generados con generadores de números aleatorios seguros
- **Vinculación Específica de Usuario**: Vincular IDs de sesión a información específica del usuario usando formatos como `<user_id>:<session_id>` para prevenir abusos entre usuarios
- **Gestión del Ciclo de Vida de Sesión**: Implementar expiración, rotación e invalidez adecuadas para limitar ventanas de vulnerabilidad
- **Seguridad de Transporte**: HTTPS obligatorio para toda comunicación para prevenir la intercepción de IDs de sesión

### Problema del Delegado Confundido

El **problema del delegado confundido** ocurre cuando servidores MCP actúan como proxies de autenticación entre clientes y servicios de terceros, creando oportunidades para la evasión de autorización mediante explotación de IDs estáticos de cliente.

#### **Mecánica de Ataque y Riesgos**

- **Evasión de Consentimiento basada en Cookies**: La autenticación previa del usuario crea cookies de consentimiento que los atacantes explotan mediante solicitudes de autorización maliciosas con URIs de redirección manipuladas
- **Robo de Código de Autorización**: Cookies de consentimiento existentes pueden causar que servidores de autorización omitan pantallas de consentimiento, redirigiendo códigos a puntos controlados por el atacante  
- **Acceso No Autorizado a API**: Códigos de autorización robados permiten intercambio de tokens e impersonación de usuarios sin aprobación explícita

#### **Estrategias de Mitigación**

**Controles Obligatorios:**
- **Requisitos de Consentimiento Explícito**: Los servidores proxy MCP que usan IDs estáticos de cliente **DEBEN** obtener consentimiento del usuario para cada cliente registrado dinámicamente
- **Implementación de Seguridad OAuth 2.1**: Seguir las mejores prácticas actuales de seguridad OAuth incluyendo PKCE (Proof Key for Code Exchange) para todas las solicitudes de autorización
- **Validación Estricta de Clientes**: Implementar validación rigurosa de URIs de redirección e identificadores de cliente para prevenir explotación

### Vulnerabilidades de Paso de Tokens  

El **paso de tokens** representa un antipatrón explícito donde los servidores MCP aceptan tokens del cliente sin validación adecuada y los reenvían a APIs descendentes, violando las especificaciones de autorización MCP.

#### **Implicaciones de Seguridad**

- **Evasión de Control**: El uso directo de tokens de cliente a API evita controles críticos de limitación de tasa, validación y monitoreo
- **Corrupción de Rastro de Auditoría**: Los tokens emitidos aguas arriba hacen imposible la identificación del cliente, rompiendo capacidades de investigación de incidentes
- **Exfiltración de Datos basada en Proxy**: Tokens no validados permiten a actores maliciosos usar servidores como proxies para acceso no autorizado a datos
- **Violaciones de Límites de Confianza**: Se pueden violar las suposiciones de confianza de servicios descendentes cuando no se puede verificar el origen de los tokens
- **Expansión de Ataques Multiservicio**: Tokens comprometidos aceptados en múltiples servicios permiten movimientos laterales

#### **Controles de Seguridad Requeridos**

**Requisitos No Negociables:**
- **Validación de Tokens**: Los servidores MCP **NO DEBEN** aceptar tokens que no estén explícitamente emitidos para el servidor MCP
- **Verificación de Audiencia**: Siempre validar que las reclamaciones de audiencia del token coincidan con la identidad del servidor MCP
- **Ciclo de Vida Adecuado del Token**: Implementar tokens de acceso de corta duración con prácticas seguras de rotación


## Seguridad en la Cadena de Suministro para Sistemas IA

La seguridad en la cadena de suministro ha evolucionado más allá de las dependencias de software tradicionales para abarcar todo el ecosistema de IA. Las implementaciones modernas de MCP deben verificar y monitorear rigurosamente todos los componentes relacionados con IA, ya que cada uno introduce posibles vulnerabilidades que podrían comprometer la integridad del sistema.

### Componentes Ampliados de la Cadena de Suministro de IA

**Dependencias de Software Tradicionales:**
- Bibliotecas y frameworks de código abierto
- Imágenes de contenedor y sistemas base  
- Herramientas de desarrollo y pipelines de compilación
- Componentes y servicios de infraestructura

**Elementos Específicos de la Cadena de Suministro de IA:**
- **Modelos Base**: Modelos preentrenados de varios proveedores que requieren verificación de procedencia
- **Servicios de Embedding**: Servicios externos de vectorización y búsqueda semántica
- **Proveedores de Contexto**: Fuentes de datos, bases de conocimiento y repositorios de documentos  
- **APIs de Terceros**: Servicios externos de IA, pipelines de ML y endpoints de procesamiento de datos
- **Artefactos de Modelos**: Pesos, configuraciones y variantes de modelos ajustados
- **Fuentes de Datos de Entrenamiento**: Conjuntos de datos usados para entrenamiento y ajuste fino de modelos

### Estrategia Integral de Seguridad en la Cadena de Suministro

#### **Verificación y Confianza de Componentes**
- **Validación de Procedencia**: Verificar el origen, licenciamiento e integridad de todos los componentes de IA antes de la integración
- **Evaluación de Seguridad**: Realizar escaneos de vulnerabilidades y revisiones de seguridad para modelos, fuentes de datos y servicios de IA
- **Análisis de Reputación**: Evaluar el historial de seguridad y prácticas de proveedores de servicios IA
- **Verificación de Cumplimiento**: Asegurar que todos los componentes cumplan con los requisitos organizacionales y regulatorios

#### **Pipelines de Despliegue Seguros**  
- **Seguridad Automatizada en CI/CD**: Integrar escaneos de seguridad a lo largo de pipelines automatizados de despliegue
- **Integridad de Artefactos**: Implementar verificación criptográfica para todos los artefactos desplegados (código, modelos, configuraciones)
- **Despliegue por Etapas**: Usar estrategias progresivas de despliegue con validación de seguridad en cada etapa
- **Repositorios de Artefactos Confiables**: Desplegar solo desde registros y repositorios de artefactos verificados y seguros

#### **Monitoreo Continuo y Respuesta**
- **Escaneo de Dependencias**: Monitoreo constante de vulnerabilidades para todas las dependencias de software y componentes IA
- **Monitoreo de Modelos**: Evaluación continua del comportamiento del modelo, deriva de rendimiento y anomalías de seguridad
- **Seguimiento del Estado del Servicio**: Monitorear servicios externos de IA para disponibilidad, incidentes de seguridad y cambios en políticas
- **Integración de Inteligencia de Amenazas**: Incorporar fuentes de información específicas de riesgos en IA y ML

#### **Control de Acceso y Principio de Mínimos Privilegios**
- **Permisos al Nivel de Componente**: Restringir acceso a modelos, datos y servicios basado en necesidad del negocio
- **Gestión de Cuentas de Servicio**: Implementar cuentas de servicio dedicadas con permisos mínimos requeridos
- **Segmentación de Red**: Aislar componentes IA y limitar el acceso de red entre servicios
- **Controles de API Gateway**: Usar gateways API centralizados para controlar y monitorear acceso a servicios externos de IA

#### **Respuesta a Incidentes y Recuperación**
- **Procedimientos de Respuesta Rápida**: Procesos establecidos para parchar o reemplazar componentes de IA comprometidos
- **Rotación de Credenciales**: Sistemas automatizados para rotar secretos, claves API y credenciales de servicio
- **Capacidades de Reversión**: Capacidad para revertir rápidamente a versiones previas conocidas y seguras de componentes IA
- **Recuperación por Brecha en Cadena de Suministro**: Procedimientos específicos para responder a compromisos de servicios IA aguas arriba

### Herramientas e Integración de Seguridad de Microsoft

**GitHub Advanced Security** proporciona protección integral para la cadena de suministro incluyendo:
- **Escaneo de Secretos**: Detección automatizada de credenciales, claves API y tokens en repositorios
- **Escaneo de Dependencias**: Evaluación de vulnerabilidades para dependencias y bibliotecas de código abierto
- **Análisis CodeQL**: Análisis estático de código para vulnerabilidades de seguridad y problemas de codificación
- **Perspectivas de la Cadena de Suministro**: Visibilidad del estado y salud de dependencias

**Integración con Azure DevOps y Azure Repos:**
- Integración fluida de escaneo de seguridad en plataformas de desarrollo Microsoft
- Controles de seguridad automatizados en Azure Pipelines para cargas de trabajo IA
- Aplicación de políticas para despliegue seguro de componentes IA

**Prácticas Internas de Microsoft:**
Microsoft implementa prácticas extensas de seguridad en la cadena de suministro en todos sus productos. Conozca enfoques probados en [The Journey to Secure the Software Supply Chain at Microsoft](https://devblogs.microsoft.com/engineering-at-microsoft/the-journey-to-secure-the-software-supply-chain-at-microsoft/).


## Mejores Prácticas de Seguridad Fundamentales

Las implementaciones MCP heredan y construyen sobre la postura de seguridad existente de su organización. Fortalecer las prácticas de seguridad fundamentales mejora significativamente la seguridad general de los sistemas IA y despliegues MCP.

### Fundamentos Clave de Seguridad

#### **Prácticas Seguras de Desarrollo**
- **Cumplimiento OWASP**: Protección contra vulnerabilidades web [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- **Protecciones Específicas para IA**: Implementar controles para [OWASP Top 10 para LLMs](https://genai.owasp.org/download/43299/?tmstv=1731900559)
- **Gestión Segura de Secretos**: Usar bóvedas dedicadas para tokens, claves API y datos sensibles de configuración
- **Cifrado de Extremo a Extremo**: Implementar comunicaciones seguras en todos los componentes y flujos de datos de la aplicación
- **Validación de Entradas**: Validación rigurosa de todas las entradas de usuarios, parámetros API y fuentes de datos

#### **Endurecimiento de Infraestructura**
- **Autenticación Multifactor**: MFA obligatorio para todas las cuentas administrativas y de servicio
- **Gestión de Parches**: Aplicación automática y oportuna de parches para sistemas operativos, frameworks y dependencias  
- **Integración con Proveedores de Identidad**: Gestión centralizada de identidad mediante proveedores empresariales (Microsoft Entra ID, Active Directory)
- **Segmentación de Red**: Aislamiento lógico de componentes MCP para limitar potenciales movimientos laterales
- **Principio de Menor Privilegio**: Permisos mínimos necesarios para todos los componentes y cuentas del sistema

#### **Monitoreo y Detección de Seguridad**
- **Registro Exhaustivo**: Registro detallado de actividades de aplicaciones IA, incluyendo interacciones cliente-servidor MCP
- **Integración SIEM**: Gestión centralizada de información de seguridad y eventos para detección de anomalías
- **Analítica de Comportamiento**: Monitoreo potenciado por IA para detectar patrones inusuales en comportamiento de sistemas y usuarios
- **Inteligencia de Amenazas**: Integración de fuentes externas de amenazas e indicadores de compromiso (IOCs)
- **Respuesta a Incidentes**: Procedimientos bien definidos para detección, respuesta y recuperación ante incidentes de seguridad

#### **Arquitectura de Confianza Cero**
- **Nunca Confiar, Siempre Verificar**: Verificación continua de usuarios, dispositivos y conexiones de red
- **Microsegmentación**: Controles granulares de red que aíslan cargas de trabajo y servicios individuales
- **Seguridad Centrada en Identidad**: Políticas de seguridad basadas en identidades verificadas en lugar de ubicación de red
- **Evaluación Continua de Riesgos**: Evaluación dinámica de la postura de seguridad basada en contexto y comportamiento actual
- **Acceso Condicional**: Controles de acceso que se adaptan según factores de riesgo, ubicación y confianza del dispositivo

### Patrones de Integración Empresarial

#### **Integración con Ecosistema de Seguridad Microsoft**
- **Microsoft Defender for Cloud**: Gestión integral de postura de seguridad en la nube
- **Azure Sentinel**: Capacidades nativas en la nube SIEM y SOAR para protección de cargas de trabajo IA
- **Microsoft Entra ID**: Gestión empresarial de identidad y acceso con políticas de acceso condicional
- **Azure Key Vault**: Gestión centralizada de secretos con respaldo de módulo de seguridad hardware (HSM)
- **Microsoft Purview**: Gobernanza de datos y cumplimiento para fuentes y flujos de trabajo de datos IA

#### **Cumplimiento y Gobernanza**
- **Alineamiento Regulatorio**: Asegurar que implementaciones MCP cumplan con requisitos específicos de cumplimiento sectorial (GDPR, HIPAA, SOC 2)

- **Clasificación de datos**: Categorización y manejo adecuado de datos sensibles procesados por sistemas de IA
- **Registros de auditoría**: Registro exhaustivo para el cumplimiento normativo y la investigación forense
- **Controles de privacidad**: Implementación de principios de privacidad desde el diseño en la arquitectura del sistema de IA
- **Gestión de cambios**: Procesos formales para revisiones de seguridad de modificaciones en el sistema de IA

Estas prácticas fundamentales crean una base sólida de seguridad que mejora la efectividad de los controles de seguridad específicos del MCP y proporciona protección integral para las aplicaciones impulsadas por IA.

## Puntos clave de seguridad

- **Enfoque de seguridad en capas**: Combinar prácticas de seguridad fundamentales (codificación segura, privilegio mínimo, verificación de cadena de suministro, monitoreo continuo) con controles específicos de IA para una protección integral

- **Paisaje de amenazas específico de IA**: Los sistemas MCP enfrentan riesgos únicos como inyección de indicaciones, envenenamiento de herramientas, secuestro de sesiones, problemas de delegado confundido, vulnerabilidades de paso de tokens y permisos excesivos que requieren mitigaciones especializadas

- **Excelencia en autenticación y autorización**: Implementar autenticación robusta usando proveedores externos de identidad (Microsoft Entra ID), aplicar validación adecuada de tokens y nunca aceptar tokens no emitidos explícitamente para su servidor MCP

- **Prevención de ataques a IA**: Desplegar Microsoft Prompt Shields y Azure Content Safety para defenderse contra inyección indirecta de indicaciones y ataques de envenenamiento de herramientas, mientras se valida la metadata de herramientas y se supervisan cambios dinámicos

- **Seguridad de sesión y transporte**: Usar identificadores de sesión criptográficamente seguros y no determinísticos vinculados a identidades de usuario, implementar manejo adecuado del ciclo de vida de sesiones y nunca usar sesiones para autenticación

- **Mejores prácticas de seguridad OAuth**: Prevenir ataques de delegado confundido mediante consentimiento explícito del usuario para clientes registrados dinámicamente, implementación adecuada de OAuth 2.1 con PKCE y estricta validación de URI de redirección  

- **Principios de seguridad de tokens**: Evitar anti-patrones de paso de tokens, validar las reclamaciones de audiencia de tokens, implementar tokens de corta duración con rotación segura y mantener límites claros de confianza

- **Seguridad integral de la cadena de suministro**: Tratar todos los componentes del ecosistema de IA (modelos, embeddings, proveedores de contexto, APIs externas) con el mismo rigor de seguridad que las dependencias de software tradicionales

- **Evolución continua**: Mantenerse actualizado con las especificaciones MCP en rápida evolución, contribuir a estándares de la comunidad de seguridad y mantener posturas de seguridad adaptativas conforme madura el protocolo

- **Integración con seguridad de Microsoft**: Aprovechar el ecosistema de seguridad integral de Microsoft (Prompt Shields, Azure Content Safety, GitHub Advanced Security, Entra ID) para mejorar la protección en despliegues MCP

## Recursos integrales

### **Documentación oficial de seguridad MCP**
- [Especificación MCP (Actual: 2026-07-28)](https://modelcontextprotocol.io/specification/2026-07-28/)
- [Mejores prácticas de seguridad MCP](https://modelcontextprotocol.io/specification/2026-07-28/basic/security_best_practices)
- [Especificación de autorización MCP](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization)
- [Repositorio MCP en GitHub](https://github.com/modelcontextprotocol)

### **Recursos de seguridad OWASP MCP**
- [Guía de seguridad OWASP MCP Azure](https://microsoft.github.io/mcp-azure-security-guide/) - Top 10 OWASP MCP con guía de implementación en Azure
- [OWASP MCP Top 10](https://owasp.org/www-project-mcp-top-10/) - Riesgos oficiales de seguridad MCP por OWASP
- [Taller MCP Security Summit (Sherpa)](https://azure-samples.github.io/sherpa/) - Capacitación práctica en seguridad para MCP en Azure

### **Estándares de seguridad y mejores prácticas**
- [Mejores prácticas de seguridad OAuth 2.0 (RFC 9700)](https://datatracker.ietf.org/doc/html/rfc9700)
- [OWASP Top 10 Seguridad de aplicaciones web](https://owasp.org/www-project-top-ten/)
- [OWASP Top 10 para Modelos de Lenguaje Grandes](https://genai.owasp.org/download/43299/?tmstv=1731900559)
- [Informe de Defensa Digital de Microsoft](https://aka.ms/mddr)

### **Investigación y análisis de seguridad en IA**
- [Inyección de indicaciones en MCP (Simon Willison)](https://simonwillison.net/2025/Apr/9/mcp-prompt-injection/)
- [Ataques de envenenamiento de herramientas (Invariant Labs)](https://invariantlabs.ai/blog/mcp-security-notification-tool-poisoning-attacks)
- [Informe de investigación de seguridad MCP (Wiz Security)](https://www.wiz.io/blog/mcp-security-research-briefing#remote-servers-22)

### **Soluciones de seguridad de Microsoft**
- [Documentación de Microsoft Prompt Shields](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)
- [Servicio Azure Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/)
- [Seguridad Microsoft Entra ID](https://learn.microsoft.com/entra/identity-platform/secure-least-privileged-access)
- [Mejores prácticas de gestión de tokens en Azure](https://learn.microsoft.com/entra/identity-platform/access-tokens)
- [GitHub Advanced Security](https://github.com/security/advanced-security)

### **Guías de implementación y tutoriales**
- [Azure API Management como Gateway de autenticación MCP](https://techcommunity.microsoft.com/blog/integrationsonazureblog/azure-api-management-your-auth-gateway-for-mcp-servers/4402690)
- [Autenticación Microsoft Entra ID con servidores MCP](https://den.dev/blog/mcp-server-auth-entra-id-session/)
- [Almacenamiento seguro de tokens y cifrado (Video)](https://youtu.be/uRdX37EcCwg?si=6fSChs1G4glwXRy2)

### **DevOps y seguridad de la cadena de suministro**
- [Seguridad Azure DevOps](https://azure.microsoft.com/products/devops)
- [Seguridad en Azure Repos](https://azure.microsoft.com/products/devops/repos/)
- [Trayectoria de seguridad de la cadena de suministro Microsoft](https://devblogs.microsoft.com/engineering-at-microsoft/the-journey-to-secure-the-software-supply-chain-at-microsoft/)

## **Documentación adicional de seguridad**

Para una guía integral de seguridad, consulte estos documentos especializados en esta sección:

- **[Ejemplo de autorización CIMD y DCR](./samples/cimd-dcr-auth/README.md)** - Servidor de recursos MCP `2026-07-28` ejecutable en TypeScript que compara Documentos de metadata de ID de cliente preferidos con registro dinámico de cliente en desuso
- **[Mejores prácticas de seguridad MCP](./mcp-security-best-practices.md)** - Prácticas completas de seguridad para implementaciones MCP
- **[Implementación Azure Content Safety](./azure-content-safety-implementation.md)** - Ejemplos prácticos de integración con Azure Content Safety  
- **[Controles de seguridad MCP](./mcp-security-controls.md)** - Últimos controles y técnicas de seguridad para despliegues MCP
- **[Referencia rápida de mejores prácticas MCP](./mcp-best-practices.md)** - Guía de referencia rápida para prácticas esenciales de seguridad MCP
- **[BlueHat 2026: Asegurando el futuro de la IA: Seguridad MCP con patrones de defensa en profundidad](https://www.youtube.com/watch?v=cVWB58kEt-Y)** - Patrones de defensa en profundidad del Centro de Respuesta a Seguridad de Microsoft (MSRC)

### **Entrenamiento práctico en seguridad**

- **[Taller MCP Security Summit (Sherpa)](https://azure-samples.github.io/sherpa/)** - Taller práctico completo para asegurar servidores MCP en Azure con campamentos progresivos desde Base Camp hasta Summit
- **[Guía de seguridad OWASP MCP Azure](https://microsoft.github.io/mcp-azure-security-guide/)** - Arquitectura de referencia y guía de implementación para todos los riesgos top 10 OWASP MCP

---

## Qué sigue

Siguiente: [Capítulo 3: Primeros pasos](../03-GettingStarted/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Descargo de responsabilidad**:
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional humana. No somos responsables de cualquier malentendido o interpretación errónea que surja del uso de esta traducción.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->