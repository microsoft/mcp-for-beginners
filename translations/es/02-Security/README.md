# Seguridad MCP: Protección Integral para Sistemas de IA

[![Mejores Prácticas de Seguridad MCP](../../../translated_images/es/03.175aed6dedae133f.webp)](https://youtu.be/88No8pw706o)

_(Haz clic en la imagen de arriba para ver el video de esta lección)_

La seguridad es fundamental en el diseño de sistemas de IA, por eso la priorizamos como nuestra segunda sección. Esto se alinea con el principio **Seguro por Diseño** de Microsoft del [Secure Future Initiative](https://www.microsoft.com/security/blog/2025/04/17/microsofts-secure-by-design-journey-one-year-of-success/).

El Protocolo de Contexto de Modelo (MCP) aporta nuevas capacidades potentes a las aplicaciones impulsadas por IA, al tiempo que introduce desafíos de seguridad únicos que van más allá de los riesgos tradicionales del software. Los sistemas MCP enfrentan tanto preocupaciones de seguridad establecidas (codificación segura, mínimo privilegio, seguridad de la cadena de suministro) como nuevas amenazas específicas de IA, incluyendo inyección de prompts, envenenamiento de herramientas, secuestro de sesión, ataques de delegado confundido, vulnerabilidades de paso de tokens y modificación dinámica de capacidades.

Esta lección explora los riesgos de seguridad más críticos en implementaciones MCP, cubriendo autenticación, autorización, permisos excesivos, inyección indirecta de prompts, seguridad de sesión, problemas de delegado confundido, gestión de tokens y vulnerabilidades en la cadena de suministro. Aprenderás controles prácticos y mejores prácticas para mitigar estos riesgos mientras aprovechas soluciones de Microsoft como Prompt Shields, Azure Content Safety y GitHub Advanced Security para fortalecer tu despliegue MCP.

## Objetivos de Aprendizaje

Al final de esta lección, podrás:

- **Identificar Amenazas Específicas de MCP**: Reconocer riesgos de seguridad únicos en sistemas MCP, incluyendo inyección de prompts, envenenamiento de herramientas, permisos excesivos, secuestro de sesión, problemas de delegado confundido, vulnerabilidades de paso de tokens y riesgos en la cadena de suministro
- **Aplicar Controles de Seguridad**: Implementar mitigaciones efectivas que incluyen autenticación robusta, acceso con mínimo privilegio, gestión segura de tokens, controles de seguridad de sesión y verificación de la cadena de suministro
- **Aprovechar Soluciones de Seguridad de Microsoft**: Entender y desplegar Microsoft Prompt Shields, Azure Content Safety y GitHub Advanced Security para la protección de cargas de trabajo MCP
- **Validar la Seguridad de Herramientas**: Reconocer la importancia de la validación de metadatos de herramientas, monitoreo de cambios dinámicos y defensa contra ataques indirectos de inyección de prompts
- **Integrar Mejores Prácticas**: Combinar fundamentos establecidos de seguridad (codificación segura, endurecimiento de servidores, confianza cero) con controles específicos de MCP para una protección integral

# Arquitectura y Controles de Seguridad MCP

Las implementaciones modernas de MCP requieren enfoques de seguridad en capas que aborden tanto la seguridad tradicional del software como las amenazas específicas de IA. La especificación MCP, que evoluciona rápidamente, continúa madurando sus controles de seguridad, permitiendo una mejor integración con arquitecturas de seguridad empresariales y mejores prácticas establecidas.

La investigación del [Microsoft Digital Defense Report](https://aka.ms/mddr) demuestra que **el 98% de las brechas reportadas se podrían prevenir con una higiene de seguridad robusta**. La estrategia de protección más efectiva combina prácticas de seguridad fundamentales con controles específicos de MCP; las medidas de seguridad base probadas siguen siendo las más impactantes para reducir el riesgo general.

## Panorama Actual de Seguridad

> **Nota:** Esta información refleja los estándares de seguridad MCP al **18 de diciembre de 2025**. El protocolo MCP continúa evolucionando rápidamente, y futuras implementaciones pueden introducir nuevos patrones de autenticación y controles mejorados. Siempre consulta la [Especificación MCP](https://spec.modelcontextprotocol.io/), el [repositorio MCP en GitHub](https://github.com/modelcontextprotocol) y la [documentación de mejores prácticas de seguridad](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices) para obtener la guía más actualizada.

### Evolución de la Autenticación MCP

La especificación MCP ha evolucionado significativamente en su enfoque de autenticación y autorización:

- **Enfoque Original**: Las primeras especificaciones requerían que los desarrolladores implementaran servidores de autenticación personalizados, con servidores MCP actuando como Servidores de Autorización OAuth 2.0 que gestionaban la autenticación de usuarios directamente
- **Estándar Actual (2025-11-25)**: La especificación actualizada permite que los servidores MCP deleguen la autenticación a proveedores de identidad externos (como Microsoft Entra ID), mejorando la postura de seguridad y reduciendo la complejidad de implementación
- **Seguridad en la Capa de Transporte**: Soporte mejorado para mecanismos de transporte seguro con patrones de autenticación adecuados tanto para conexiones locales (STDIO) como remotas (HTTP transmitible)

## Seguridad en Autenticación y Autorización

### Desafíos Actuales de Seguridad

Las implementaciones modernas de MCP enfrentan varios desafíos en autenticación y autorización:

### Riesgos y Vectores de Amenaza

- **Lógica de Autorización Mal Configurada**: Implementaciones defectuosas de autorización en servidores MCP pueden exponer datos sensibles y aplicar controles de acceso incorrectamente
- **Compromiso de Tokens OAuth**: El robo de tokens en servidores MCP locales permite a atacantes suplantar servidores y acceder a servicios descendentes
- **Vulnerabilidades de Paso de Tokens**: El manejo inadecuado de tokens crea bypass de controles de seguridad y brechas de responsabilidad
- **Permisos Excesivos**: Servidores MCP con privilegios excesivos violan el principio de mínimo privilegio y amplían la superficie de ataque

#### Paso de Tokens: Un Anti-Patrón Crítico

**El paso de tokens está explícitamente prohibido** en la especificación actual de autorización MCP debido a sus graves implicaciones de seguridad:

##### Circunvención de Controles de Seguridad
- Los servidores MCP y las APIs descendentes implementan controles críticos (limitación de tasa, validación de solicitudes, monitoreo de tráfico) que dependen de la validación adecuada de tokens
- El uso directo de tokens cliente-API omite estas protecciones esenciales, socavando la arquitectura de seguridad

##### Desafíos de Responsabilidad y Auditoría  
- Los servidores MCP no pueden distinguir entre clientes que usan tokens emitidos aguas arriba, rompiendo las trazas de auditoría
- Los registros de servidores de recursos descendentes muestran orígenes de solicitudes engañosos en lugar de los intermediarios MCP reales
- La investigación de incidentes y auditorías de cumplimiento se vuelven significativamente más difíciles

##### Riesgos de Exfiltración de Datos
- Reclamaciones de tokens no validadas permiten a actores maliciosos con tokens robados usar servidores MCP como proxies para exfiltración de datos
- Violaciones de límites de confianza permiten patrones de acceso no autorizados que evaden controles de seguridad previstos

##### Vectores de Ataque Multi-Servicio
- Tokens comprometidos aceptados por múltiples servicios permiten movimientos laterales a través de sistemas conectados
- Las suposiciones de confianza entre servicios pueden violarse cuando no se puede verificar el origen del token

### Controles y Mitigaciones de Seguridad

**Requisitos Críticos de Seguridad:**

> **OBLIGATORIO**: Los servidores MCP **NO DEBEN** aceptar ningún token que no haya sido emitido explícitamente para el servidor MCP

#### Controles de Autenticación y Autorización

- **Revisión Rigurosa de Autorización**: Realizar auditorías exhaustivas de la lógica de autorización del servidor MCP para asegurar que solo los usuarios y clientes previstos puedan acceder a recursos sensibles
  - **Guía de Implementación**: [Azure API Management como Gateway de Autenticación para Servidores MCP](https://techcommunity.microsoft.com/blog/integrationsonazureblog/azure-api-management-your-auth-gateway-for-mcp-servers/4402690)
  - **Integración de Identidad**: [Uso de Microsoft Entra ID para Autenticación de Servidores MCP](https://den.dev/blog/mcp-server-auth-entra-id-session/)

- **Gestión Segura de Tokens**: Implementar las [mejores prácticas de validación y ciclo de vida de tokens de Microsoft](https://learn.microsoft.com/en-us/entra/identity-platform/access-tokens)
  - Validar que las reclamaciones de audiencia del token coincidan con la identidad del servidor MCP
  - Implementar políticas adecuadas de rotación y expiración de tokens
  - Prevenir ataques de repetición de tokens y uso no autorizado

- **Almacenamiento Protegido de Tokens**: Asegurar el almacenamiento de tokens con cifrado tanto en reposo como en tránsito
  - **Mejores Prácticas**: [Directrices para Almacenamiento Seguro y Cifrado de Tokens](https://youtu.be/uRdX37EcCwg?si=6fSChs1G4glwXRy2)

#### Implementación de Control de Acceso

- **Principio de Mínimo Privilegio**: Otorgar a los servidores MCP solo los permisos mínimos necesarios para la funcionalidad prevista
  - Revisiones regulares de permisos y actualizaciones para prevenir la escalada de privilegios
  - **Documentación Microsoft**: [Acceso Seguro con Mínimos Privilegios](https://learn.microsoft.com/entra/identity-platform/secure-least-privileged-access)

- **Control de Acceso Basado en Roles (RBAC)**: Implementar asignaciones de roles finamente granulares
  - Limitar roles estrictamente a recursos y acciones específicas
  - Evitar permisos amplios o innecesarios que amplíen la superficie de ataque

- **Monitoreo Continuo de Permisos**: Implementar auditorías y monitoreo de acceso continuos
  - Monitorear patrones de uso de permisos para detectar anomalías
  - Remediar rápidamente privilegios excesivos o no utilizados

## Amenazas de Seguridad Específicas de IA

### Ataques de Inyección de Prompts y Manipulación de Herramientas

Las implementaciones modernas de MCP enfrentan vectores de ataque sofisticados específicos de IA que las medidas de seguridad tradicionales no pueden abordar completamente:

#### **Inyección Indirecta de Prompts (Inyección de Prompts entre Dominios)**

La **Inyección Indirecta de Prompts** representa una de las vulnerabilidades más críticas en sistemas de IA habilitados para MCP. Los atacantes incrustan instrucciones maliciosas dentro de contenido externo — documentos, páginas web, correos electrónicos o fuentes de datos — que los sistemas de IA procesan posteriormente como comandos legítimos.

**Escenarios de Ataque:**
- **Inyección basada en Documentos**: Instrucciones maliciosas ocultas en documentos procesados que desencadenan acciones no deseadas de la IA
- **Explotación de Contenido Web**: Páginas web comprometidas que contienen prompts incrustados que manipulan el comportamiento de la IA al ser raspados
- **Ataques basados en Correo Electrónico**: Prompts maliciosos en correos que hacen que asistentes de IA filtren información o realicen acciones no autorizadas
- **Contaminación de Fuentes de Datos**: Bases de datos o APIs comprometidas que sirven contenido contaminado a sistemas de IA

**Impacto en el Mundo Real**: Estos ataques pueden resultar en exfiltración de datos, violaciones de privacidad, generación de contenido dañino y manipulación de interacciones con usuarios. Para un análisis detallado, consulta [Inyección de Prompts en MCP (Simon Willison)](https://simonwillison.net/2025/Apr/9/mcp-prompt-injection/).

![Diagrama de Ataque de Inyección de Prompts](../../../translated_images/es/prompt-injection.ed9fbfde297ca877.webp)

#### **Ataques de Envenenamiento de Herramientas**

El **Envenenamiento de Herramientas** apunta a los metadatos que definen las herramientas MCP, explotando cómo los LLM interpretan las descripciones y parámetros de las herramientas para tomar decisiones de ejecución.

**Mecanismos de Ataque:**
- **Manipulación de Metadatos**: Los atacantes inyectan instrucciones maliciosas en descripciones de herramientas, definiciones de parámetros o ejemplos de uso
- **Instrucciones Invisibles**: Prompts ocultos en metadatos de herramientas que son procesados por modelos de IA pero invisibles para usuarios humanos
- **Modificación Dinámica de Herramientas ("Rug Pulls")**: Herramientas aprobadas por usuarios que luego se modifican para realizar acciones maliciosas sin conocimiento del usuario
- **Inyección de Parámetros**: Contenido malicioso incrustado en esquemas de parámetros de herramientas que influye en el comportamiento del modelo

**Riesgos en Servidores Hospedados**: Los servidores MCP remotos presentan riesgos elevados ya que las definiciones de herramientas pueden actualizarse después de la aprobación inicial del usuario, creando escenarios donde herramientas previamente seguras se vuelven maliciosas. Para un análisis completo, consulta [Ataques de Envenenamiento de Herramientas (Invariant Labs)](https://invariantlabs.ai/blog/mcp-security-notification-tool-poisoning-attacks).

![Diagrama de Ataque de Inyección de Herramientas](../../../translated_images/es/tool-injection.3b0b4a6b24de6bef.webp)

#### **Vectores Adicionales de Ataque de IA**

- **Inyección de Prompts entre Dominios (XPIA)**: Ataques sofisticados que aprovechan contenido de múltiples dominios para evadir controles de seguridad
- **Modificación Dinámica de Capacidades**: Cambios en tiempo real en las capacidades de herramientas que escapan a evaluaciones de seguridad iniciales
- **Envenenamiento de Ventana de Contexto**: Ataques que manipulan grandes ventanas de contexto para ocultar instrucciones maliciosas
- **Ataques de Confusión del Modelo**: Explotación de limitaciones del modelo para crear comportamientos impredecibles o inseguros

### Impacto de Riesgos de Seguridad en IA

**Consecuencias de Alto Impacto:**
- **Exfiltración de Datos**: Acceso no autorizado y robo de datos sensibles empresariales o personales
- **Violaciones de Privacidad**: Exposición de información personal identificable (PII) y datos confidenciales de negocios  
- **Manipulación del Sistema**: Modificaciones no deseadas en sistemas y flujos de trabajo críticos
- **Robo de Credenciales**: Compromiso de tokens de autenticación y credenciales de servicios
- **Movimiento Lateral**: Uso de sistemas de IA comprometidos como pivotes para ataques más amplios en la red

### Soluciones de Seguridad de IA de Microsoft

#### **AI Prompt Shields: Protección Avanzada Contra Ataques de Inyección**

Microsoft **AI Prompt Shields** ofrecen defensa integral contra ataques de inyección de prompts directos e indirectos mediante múltiples capas de seguridad:

##### **Mecanismos Clave de Protección:**

1. **Detección y Filtrado Avanzados**
   - Algoritmos de aprendizaje automático y técnicas de PLN detectan instrucciones maliciosas en contenido externo
   - Análisis en tiempo real de documentos, páginas web, correos electrónicos y fuentes de datos para amenazas incrustadas
   - Comprensión contextual de patrones legítimos vs. maliciosos de prompts

2. **Técnicas de Enfoque (Spotlighting)**  
   - Distingue entre instrucciones del sistema confiables y entradas externas potencialmente comprometidas
   - Métodos de transformación de texto que mejoran la relevancia del modelo mientras aíslan contenido malicioso
   - Ayuda a los sistemas de IA a mantener la jerarquía correcta de instrucciones e ignorar comandos inyectados

3. **Sistemas de Delimitadores y Marcado de Datos**
   - Definición explícita de límites entre mensajes del sistema confiables y texto de entrada externo
   - Marcadores especiales que resaltan límites entre fuentes de datos confiables y no confiables
   - Separación clara que previene confusión de instrucciones y ejecución no autorizada de comandos

4. **Inteligencia Continua de Amenazas**
   - Microsoft monitorea continuamente patrones emergentes de ataque y actualiza defensas
   - Caza proactiva de amenazas para nuevas técnicas de inyección y vectores de ataque
   - Actualizaciones regulares del modelo de seguridad para mantener efectividad contra amenazas en evolución

5. **Integración con Azure Content Safety**
   - Parte de la suite integral Azure AI Content Safety
   - Detección adicional para intentos de jailbreak, contenido dañino y violaciones de políticas de seguridad
   - Controles de seguridad unificados a través de componentes de aplicaciones de IA

**Recursos de Implementación**: [Documentación de Microsoft Prompt Shields](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)

![Protección Microsoft Prompt Shields](../../../translated_images/es/prompt-shield.ff5b95be76e9c78c.webp)


## Amenazas Avanzadas de Seguridad MCP

### Vulnerabilidades de Secuestro de Sesión

El **secuestro de sesión** representa un vector de ataque crítico en implementaciones MCP con estado, donde partes no autorizadas obtienen y abusan de identificadores de sesión legítimos para suplantar clientes y realizar acciones no autorizadas.

#### **Escenarios de Ataque y Riesgos**

- **Inyección de Prompts por Secuestro de Sesión**: Atacantes con IDs de sesión robados inyectan eventos maliciosos en servidores que comparten estado de sesión, potencialmente desencadenando acciones dañinas o accediendo a datos sensibles
- **Suplantación Directa**: IDs de sesión robados permiten llamadas directas al servidor MCP que evaden autenticación, tratando a atacantes como usuarios legítimos
- **Streams Reanudables Comprometidos**: Atacantes pueden terminar solicitudes prematuramente, causando que clientes legítimos reanuden con contenido potencialmente malicioso

#### **Controles de Seguridad para la Gestión de Sesiones**

**Requisitos Críticos:**
- **Verificación de Autorización**: Los servidores MCP que implementen autorización **DEBEN** verificar TODAS las solicitudes entrantes y **NO DEBEN** confiar en sesiones para la autenticación  
- **Generación Segura de Sesiones**: Utilice IDs de sesión criptográficamente seguros y no deterministas generados con generadores de números aleatorios seguros  
- **Vinculación Específica del Usuario**: Vincule los IDs de sesión a información específica del usuario usando formatos como `<user_id>:<session_id>` para evitar el abuso de sesiones entre usuarios  
- **Gestión del Ciclo de Vida de la Sesión**: Implemente expiración, rotación e invalidación adecuadas para limitar las ventanas de vulnerabilidad  
- **Seguridad en el Transporte**: HTTPS obligatorio para toda la comunicación para evitar la interceptación de IDs de sesión  

### Problema del Delegado Confundido

El **problema del delegado confundido** ocurre cuando los servidores MCP actúan como proxies de autenticación entre clientes y servicios de terceros, creando oportunidades para eludir la autorización mediante la explotación de IDs de cliente estáticos.

#### **Mecánica del Ataque y Riesgos**

- **Elusión de Consentimiento Basada en Cookies**: La autenticación previa del usuario crea cookies de consentimiento que los atacantes explotan mediante solicitudes de autorización maliciosas con URIs de redirección manipuladas  
- **Robo de Código de Autorización**: Las cookies de consentimiento existentes pueden hacer que los servidores de autorización omitan las pantallas de consentimiento, redirigiendo códigos a puntos finales controlados por el atacante  
- **Acceso No Autorizado a API**: Los códigos de autorización robados permiten el intercambio de tokens y la suplantación de usuarios sin aprobación explícita  

#### **Estrategias de Mitigación**

**Controles Obligatorios:**  
- **Requisitos de Consentimiento Explícito**: Los servidores proxy MCP que usen IDs de cliente estáticos **DEBEN** obtener el consentimiento del usuario para cada cliente registrado dinámicamente  
- **Implementación de Seguridad OAuth 2.1**: Siga las mejores prácticas actuales de seguridad OAuth, incluyendo PKCE (Proof Key for Code Exchange) para todas las solicitudes de autorización  
- **Validación Estricta del Cliente**: Implemente una validación rigurosa de URIs de redirección e identificadores de cliente para prevenir la explotación  

### Vulnerabilidades de Passthrough de Tokens  

El **passthrough de tokens** representa un anti-patrón explícito donde los servidores MCP aceptan tokens de clientes sin la validación adecuada y los reenvían a APIs descendentes, violando las especificaciones de autorización MCP.

#### **Implicaciones de Seguridad**

- **Circunvención de Controles**: El uso directo de tokens cliente-API elude controles críticos de limitación de tasa, validación y monitoreo  
- **Corrupción de la Pista de Auditoría**: Los tokens emitidos aguas arriba hacen imposible la identificación del cliente, rompiendo las capacidades de investigación de incidentes  
- **Exfiltración de Datos Basada en Proxy**: Los tokens no validados permiten a actores maliciosos usar servidores como proxies para acceso no autorizado a datos  
- **Violaciones de Límites de Confianza**: Las suposiciones de confianza de los servicios descendentes pueden ser violadas cuando no se puede verificar el origen del token  
- **Expansión de Ataques Multi-servicio**: Los tokens comprometidos aceptados en múltiples servicios permiten movimientos laterales  

#### **Controles de Seguridad Requeridos**

**Requisitos Innegociables:**  
- **Validación de Tokens**: Los servidores MCP **NO DEBEN** aceptar tokens que no hayan sido emitidos explícitamente para el servidor MCP  
- **Verificación de Audiencia**: Siempre valide que las reclamaciones de audiencia del token coincidan con la identidad del servidor MCP  
- **Ciclo de Vida Adecuado del Token**: Implemente tokens de acceso de corta duración con prácticas seguras de rotación  

## Seguridad de la Cadena de Suministro para Sistemas de IA

La seguridad de la cadena de suministro ha evolucionado más allá de las dependencias tradicionales de software para abarcar todo el ecosistema de IA. Las implementaciones modernas de MCP deben verificar y monitorear rigurosamente todos los componentes relacionados con IA, ya que cada uno introduce vulnerabilidades potenciales que podrían comprometer la integridad del sistema.

### Componentes Ampliados de la Cadena de Suministro de IA

**Dependencias Tradicionales de Software:**  
- Bibliotecas y frameworks de código abierto  
- Imágenes de contenedores y sistemas base  
- Herramientas de desarrollo y pipelines de construcción  
- Componentes y servicios de infraestructura  

**Elementos Específicos de la Cadena de Suministro de IA:**  
- **Modelos Fundamentales**: Modelos preentrenados de varios proveedores que requieren verificación de procedencia  
- **Servicios de Embeddings**: Servicios externos de vectorización y búsqueda semántica  
- **Proveedores de Contexto**: Fuentes de datos, bases de conocimiento y repositorios de documentos  
- **APIs de Terceros**: Servicios externos de IA, pipelines de ML y puntos finales de procesamiento de datos  
- **Artefactos de Modelos**: Pesos, configuraciones y variantes de modelos afinados  
- **Fuentes de Datos de Entrenamiento**: Conjuntos de datos usados para entrenamiento y afinación de modelos  

### Estrategia Integral de Seguridad de la Cadena de Suministro

#### **Verificación y Confianza de Componentes**  
- **Validación de Procedencia**: Verifique el origen, licenciamiento e integridad de todos los componentes de IA antes de la integración  
- **Evaluación de Seguridad**: Realice escaneos de vulnerabilidades y revisiones de seguridad para modelos, fuentes de datos y servicios de IA  
- **Análisis de Reputación**: Evalúe el historial de seguridad y las prácticas de los proveedores de servicios de IA  
- **Verificación de Cumplimiento**: Asegure que todos los componentes cumplan con los requisitos de seguridad y normativos de la organización  

#### **Pipelines de Despliegue Seguros**  
- **Seguridad Automatizada CI/CD**: Integre escaneos de seguridad a lo largo de los pipelines automatizados de despliegue  
- **Integridad de Artefactos**: Implemente verificación criptográfica para todos los artefactos desplegados (código, modelos, configuraciones)  
- **Despliegue por Etapas**: Use estrategias de despliegue progresivo con validación de seguridad en cada etapa  
- **Repositorios de Artefactos Confiables**: Despliegue solo desde registros y repositorios de artefactos verificados y seguros  

#### **Monitoreo Continuo y Respuesta**  
- **Escaneo de Dependencias**: Monitoreo continuo de vulnerabilidades para todas las dependencias de software y componentes de IA  
- **Monitoreo de Modelos**: Evaluación continua del comportamiento del modelo, deriva de rendimiento y anomalías de seguridad  
- **Seguimiento de Salud de Servicios**: Monitoreo de servicios externos de IA para disponibilidad, incidentes de seguridad y cambios en políticas  
- **Integración de Inteligencia de Amenazas**: Incorporación de fuentes de amenazas específicas para riesgos de seguridad en IA y ML  

#### **Control de Acceso y Mínimos Privilegios**  
- **Permisos a Nivel de Componente**: Restrinja el acceso a modelos, datos y servicios según la necesidad del negocio  
- **Gestión de Cuentas de Servicio**: Implemente cuentas de servicio dedicadas con permisos mínimos requeridos  
- **Segmentación de Red**: Aísle componentes de IA y limite el acceso de red entre servicios  
- **Controles de API Gateway**: Use gateways de API centralizados para controlar y monitorear el acceso a servicios externos de IA  

#### **Respuesta a Incidentes y Recuperación**  
- **Procedimientos de Respuesta Rápida**: Procesos establecidos para parchear o reemplazar componentes de IA comprometidos  
- **Rotación de Credenciales**: Sistemas automatizados para rotar secretos, claves API y credenciales de servicio  
- **Capacidades de Reversión**: Capacidad para revertir rápidamente a versiones anteriores conocidas y seguras de componentes de IA  
- **Recuperación ante Brechas en la Cadena de Suministro**: Procedimientos específicos para responder a compromisos en servicios de IA aguas arriba  

### Herramientas e Integración de Seguridad de Microsoft

**GitHub Advanced Security** ofrece protección integral de la cadena de suministro que incluye:  
- **Escaneo de Secretos**: Detección automatizada de credenciales, claves API y tokens en repositorios  
- **Escaneo de Dependencias**: Evaluación de vulnerabilidades para dependencias y bibliotecas de código abierto  
- **Análisis CodeQL**: Análisis estático de código para vulnerabilidades de seguridad y problemas de codificación  
- **Insights de la Cadena de Suministro**: Visibilidad sobre la salud y estado de seguridad de las dependencias  

**Integración con Azure DevOps y Azure Repos:**  
- Integración fluida de escaneos de seguridad en plataformas de desarrollo Microsoft  
- Controles de seguridad automatizados en Azure Pipelines para cargas de trabajo de IA  
- Aplicación de políticas para despliegue seguro de componentes de IA  

**Prácticas Internas de Microsoft:**  
Microsoft implementa prácticas extensas de seguridad en la cadena de suministro en todos sus productos. Conozca enfoques probados en [El viaje para asegurar la cadena de suministro de software en Microsoft](https://devblogs.microsoft.com/engineering-at-microsoft/the-journey-to-secure-the-software-supply-chain-at-microsoft/).  

## Mejores Prácticas de Seguridad Fundamentales

Las implementaciones MCP heredan y construyen sobre la postura de seguridad existente de su organización. Fortalecer las prácticas de seguridad fundamentales mejora significativamente la seguridad general de los sistemas de IA y despliegues MCP.

### Fundamentos Clave de Seguridad

#### **Prácticas de Desarrollo Seguro**  
- **Cumplimiento OWASP**: Protección contra vulnerabilidades web [OWASP Top 10](https://owasp.org/www-project-top-ten/)  
- **Protecciones Específicas para IA**: Implemente controles para [OWASP Top 10 para LLMs](https://genai.owasp.org/download/43299/?tmstv=1731900559)  
- **Gestión Segura de Secretos**: Use bóvedas dedicadas para tokens, claves API y datos sensibles de configuración  
- **Cifrado de Extremo a Extremo**: Implemente comunicaciones seguras en todos los componentes y flujos de datos  
- **Validación de Entradas**: Validación rigurosa de todas las entradas de usuario, parámetros API y fuentes de datos  

#### **Endurecimiento de Infraestructura**  
- **Autenticación Multifactor**: MFA obligatorio para todas las cuentas administrativas y de servicio  
- **Gestión de Parches**: Aplicación automatizada y oportuna de parches para sistemas operativos, frameworks y dependencias  
- **Integración con Proveedores de Identidad**: Gestión centralizada de identidad mediante proveedores empresariales (Microsoft Entra ID, Active Directory)  
- **Segmentación de Red**: Aislamiento lógico de componentes MCP para limitar el movimiento lateral  
- **Principio de Mínimos Privilegios**: Permisos mínimos requeridos para todos los componentes y cuentas del sistema  

#### **Monitoreo y Detección de Seguridad**  
- **Registro Exhaustivo**: Registro detallado de actividades de aplicaciones IA, incluyendo interacciones cliente-servidor MCP  
- **Integración SIEM**: Gestión centralizada de información y eventos de seguridad para detección de anomalías  
- **Análisis de Comportamiento**: Monitoreo potenciado por IA para detectar patrones inusuales en comportamiento de sistemas y usuarios  
- **Inteligencia de Amenazas**: Integración de fuentes externas de amenazas e indicadores de compromiso (IOCs)  
- **Respuesta a Incidentes**: Procedimientos bien definidos para detección, respuesta y recuperación ante incidentes de seguridad  

#### **Arquitectura de Confianza Cero**  
- **Nunca Confiar, Siempre Verificar**: Verificación continua de usuarios, dispositivos y conexiones de red  
- **Microsegmentación**: Controles granulares de red que aíslan cargas de trabajo y servicios individuales  
- **Seguridad Centrada en Identidad**: Políticas de seguridad basadas en identidades verificadas en lugar de ubicación de red  
- **Evaluación Continua de Riesgos**: Evaluación dinámica de la postura de seguridad basada en contexto y comportamiento actuales  
- **Acceso Condicional**: Controles de acceso que se adaptan según factores de riesgo, ubicación y confianza del dispositivo  

### Patrones de Integración Empresarial

#### **Integración con el Ecosistema de Seguridad Microsoft**  
- **Microsoft Defender for Cloud**: Gestión integral de la postura de seguridad en la nube  
- **Azure Sentinel**: Capacidades nativas en la nube SIEM y SOAR para protección de cargas de trabajo IA  
- **Microsoft Entra ID**: Gestión empresarial de identidad y acceso con políticas de acceso condicional  
- **Azure Key Vault**: Gestión centralizada de secretos con respaldo de módulos de seguridad hardware (HSM)  
- **Microsoft Purview**: Gobernanza y cumplimiento de datos para fuentes y flujos de trabajo de IA  

#### **Cumplimiento y Gobernanza**  
- **Alineación Regulatoria**: Asegure que las implementaciones MCP cumplan con requisitos normativos específicos de la industria (GDPR, HIPAA, SOC 2)  
- **Clasificación de Datos**: Categorización y manejo adecuado de datos sensibles procesados por sistemas de IA  
- **Pistas de Auditoría**: Registro exhaustivo para cumplimiento regulatorio e investigación forense  
- **Controles de Privacidad**: Implementación de principios de privacidad desde el diseño en la arquitectura de sistemas IA  
- **Gestión de Cambios**: Procesos formales para revisiones de seguridad en modificaciones de sistemas IA  

Estas prácticas fundamentales crean una base sólida de seguridad que mejora la efectividad de los controles específicos MCP y proporciona protección integral para aplicaciones impulsadas por IA.

## Puntos Clave de Seguridad

- **Enfoque de Seguridad en Capas**: Combine prácticas fundamentales de seguridad (codificación segura, mínimos privilegios, verificación de cadena de suministro, monitoreo continuo) con controles específicos para IA para una protección integral  

- **Paisaje de Amenazas Específico para IA**: Los sistemas MCP enfrentan riesgos únicos incluyendo inyección de prompts, envenenamiento de herramientas, secuestro de sesiones, problemas de delegado confundido, vulnerabilidades de passthrough de tokens y permisos excesivos que requieren mitigaciones especializadas  

- **Excelencia en Autenticación y Autorización**: Implemente autenticación robusta usando proveedores de identidad externos (Microsoft Entra ID), aplique validación adecuada de tokens y nunca acepte tokens no emitidos explícitamente para su servidor MCP  

- **Prevención de Ataques a IA**: Despliegue Microsoft Prompt Shields y Azure Content Safety para defender contra inyección indirecta de prompts y ataques de envenenamiento de herramientas, validando metadatos de herramientas y monitoreando cambios dinámicos  

- **Seguridad de Sesiones y Transporte**: Use IDs de sesión criptográficamente seguros, no deterministas y vinculados a identidades de usuario, implemente gestión adecuada del ciclo de vida de la sesión y nunca use sesiones para autenticación  

- **Mejores Prácticas de Seguridad OAuth**: Prevenga ataques de delegado confundido mediante consentimiento explícito del usuario para clientes registrados dinámicamente, implementación correcta de OAuth 2.1 con PKCE y validación estricta de URIs de redirección  

- **Principios de Seguridad de Tokens**: Evite anti-patrones de passthrough de tokens, valide las reclamaciones de audiencia de tokens, implemente tokens de corta duración con rotación segura y mantenga límites claros de confianza  

- **Seguridad Integral de la Cadena de Suministro**: Trate todos los componentes del ecosistema IA (modelos, embeddings, proveedores de contexto, APIs externas) con el mismo rigor de seguridad que las dependencias tradicionales de software  

- **Evolución Continua**: Manténgase actualizado con las especificaciones MCP en rápida evolución, contribuya a estándares comunitarios de seguridad y mantenga posturas de seguridad adaptativas conforme madura el protocolo  

- **Integración de Seguridad Microsoft**: Aproveche el ecosistema integral de seguridad de Microsoft (Prompt Shields, Azure Content Safety, GitHub Advanced Security, Entra ID) para una protección mejorada en despliegues MCP  

## Recursos Completos

### **Documentación Oficial de Seguridad MCP**  
- [Especificación MCP (Actual: 2025-11-25)](https://spec.modelcontextprotocol.io/specification/2025-11-25/)  
- [Mejores Prácticas de Seguridad MCP](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices)  
- [Especificación de Autorización MCP](https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization)  
- [Repositorio GitHub MCP](https://github.com/modelcontextprotocol)  

### **Estándares y Mejores Prácticas de Seguridad**  
- [Mejores Prácticas de Seguridad OAuth 2.0 (RFC 9700)](https://datatracker.ietf.org/doc/html/rfc9700)  
- [OWASP Top 10 Seguridad de Aplicaciones Web](https://owasp.org/www-project-top-ten/)  
- [OWASP Top 10 para Modelos de Lenguaje Grande](https://genai.owasp.org/download/43299/?tmstv=1731900559)  
- [Informe de Defensa Digital Microsoft](https://aka.ms/mddr)  

### **Investigación y Análisis de Seguridad en IA**  
- [Inyección de Prompts en MCP (Simon Willison)](https://simonwillison.net/2025/Apr/9/mcp-prompt-injection/)  
- [Ataques de Envenenamiento de Herramientas (Invariant Labs)](https://invariantlabs.ai/blog/mcp-security-notification-tool-poisoning-attacks)  
- [Informe de Investigación de Seguridad MCP (Wiz Security)](https://www.wiz.io/blog/mcp-security-research-briefing#remote-servers-22)

### **Soluciones de Seguridad de Microsoft**
- [Documentación de Microsoft Prompt Shields](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)
- [Servicio Azure Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/)
- [Seguridad de Microsoft Entra ID](https://learn.microsoft.com/entra/identity-platform/secure-least-privileged-access)
- [Mejores Prácticas para la Gestión de Tokens en Azure](https://learn.microsoft.com/entra/identity-platform/access-tokens)
- [Seguridad Avanzada de GitHub](https://github.com/security/advanced-security)

### **Guías de Implementación y Tutoriales**
- [Azure API Management como Puerta de Autenticación MCP](https://techcommunity.microsoft.com/blog/integrationsonazureblog/azure-api-management-your-auth-gateway-for-mcp-servers/4402690)
- [Autenticación Microsoft Entra ID con Servidores MCP](https://den.dev/blog/mcp-server-auth-entra-id-session/)
- [Almacenamiento Seguro de Tokens y Encriptación (Video)](https://youtu.be/uRdX37EcCwg?si=6fSChs1G4glwXRy2)

### **DevOps y Seguridad de la Cadena de Suministro**
- [Seguridad en Azure DevOps](https://azure.microsoft.com/products/devops)
- [Seguridad en Azure Repos](https://azure.microsoft.com/products/devops/repos/)
- [Trayectoria de Seguridad en la Cadena de Suministro de Microsoft](https://devblogs.microsoft.com/engineering-at-microsoft/the-journey-to-secure-the-software-supply-chain-at-microsoft/)

## **Documentación Adicional de Seguridad**

Para una guía completa de seguridad, consulte estos documentos especializados en esta sección:

- **[Mejores Prácticas de Seguridad MCP 2025](./mcp-security-best-practices-2025.md)** - Prácticas completas de seguridad para implementaciones MCP
- **[Implementación de Azure Content Safety](./azure-content-safety-implementation.md)** - Ejemplos prácticos de implementación para la integración de Azure Content Safety  
- **[Controles de Seguridad MCP 2025](./mcp-security-controls-2025.md)** - Controles y técnicas de seguridad más recientes para despliegues MCP
- **[Referencia Rápida de Mejores Prácticas MCP](./mcp-best-practices.md)** - Guía rápida de prácticas esenciales de seguridad MCP

---

## Qué Sigue

Siguiente: [Capítulo 3: Primeros Pasos](../03-GettingStarted/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso legal**:
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o interpretaciones erróneas derivadas del uso de esta traducción.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->