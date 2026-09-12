# Controles de Seguridad MCP - Actualización de septiembre de 2026

> **Estándar actual:** Este documento refleja
> [Especificación MCP 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/)
> y las
> [Mejores Prácticas de Seguridad MCP oficiales](https://modelcontextprotocol.io/specification/2026-07-28/basic/security_best_practices).

El Protocolo de Contexto de Modelo (MCP) ha madurado significativamente con controles de seguridad mejorados que abordan tanto la seguridad tradicional del software como las amenazas específicas de IA. Este documento proporciona controles de seguridad integrales para implementaciones seguras de MCP alineadas con el marco OWASP MCP Top 10.

## 🏔️ Entrenamiento Práctico de Seguridad

Para una experiencia práctica en la implementación de seguridad, recomendamos el **[Taller MCP Security Summit (Sherpa)](https://azure-samples.github.io/sherpa/)** - una expedición guiada completa para asegurar servidores MCP en Azure usando una metodología de "vulnerable → explotar → arreglar → validar".

Todos los controles de seguridad en este documento se alinean con la **[Guía de Seguridad Azure MCP de OWASP](https://microsoft.github.io/mcp-azure-security-guide/)**, que ofrece arquitecturas de referencia y orientación específica para implementaciones en Azure de los riesgos OWASP MCP Top 10.

## **REQUISITOS de Seguridad OBLIGATORIOS**

### **Prohibiciones Críticas de la Especificación MCP:**

> **PROHIBIDO**: Los servidores MCP **NO DEBEN** aceptar tokens que no hayan sido emitidos explícitamente para el servidor MCP
>
> **PROHIBIDO**: Los servidores MCP **NO DEBEN** usar sesiones para autenticación  
>
> **REQUERIDO**: Los servidores MCP que implementan autorización **DEBEN** verificar TODAS las solicitudes entrantes
>
> **MANDATORIO**: Los servidores proxy MCP que usan un cliente de terceros estático
> **DEBEN** obtener consentimiento para cada cliente MCP antes de reenviar la autorización

---

## 1. **Controles de Autenticación y Autorización**

### **Integración con Proveedores de Identidad Externos**

**Especificación MCP `2026-07-28`** permite que los servidores MCP deleguen
la autenticación a proveedores de identidad externos. La autorización para transportes HTTP
se evalúa por cada solicitud; los servidores locales stdio obtienen credenciales
de su entorno.

**Riesgo OWASP MCP Abordado**: [MCP07 - Autenticación y Autorización Insuficientes](https://microsoft.github.io/mcp-azure-security-guide/mcp/mcp07-authz/)

**Beneficios de Seguridad:**
1. **Elimina Riesgos de Autenticación Personalizada**: Reduce la superficie de vulnerabilidad al evitar implementaciones personalizadas de autenticación
2. **Seguridad de Nivel Empresarial**: Utiliza proveedores de identidad establecidos como Microsoft Entra ID con funciones avanzadas de seguridad
3. **Gestión Centralizada de Identidad**: Simplifica el ciclo de vida del usuario, control de acceso y auditoría de cumplimiento
4. **Autenticación Multifactor**: Hereda capacidades MFA de proveedores de identidad empresariales
5. **Políticas de Acceso Condicional**: Se beneficia de controles de acceso basados en riesgos y autenticación adaptativa

**Requisitos de Implementación:**
- **Registro de Cliente**: Preferir Documentos de Metadatos de ID de Cliente o
  pre-registro; usar el Registro Dinámico de Cliente obsoleto solo para
  compatibilidad
- **Validación de Audiencia del Token**: Verificar que todos los tokens sean emitidos explícitamente para el servidor MCP
- **Verificación del Emisor**: Validar que el emisor del token coincida con el proveedor de identidad esperado
- **Verificación de Firma**: Validación criptográfica de la integridad del token
- **Aplicación de Expiración**: Estricto cumplimiento de los límites de vida del token
- **Validación de Alcance**: Asegurarse que los tokens contengan permisos adecuados para las operaciones solicitadas

### **Seguridad de la Lógica de Autorización**

**Controles Críticos:**
- **Auditorías de Autorización Exhaustivas**: Revisiones de seguridad regulares de todos los puntos de decisión de autorización
- **Defaults a Prueba de Fallos**: Denegar acceso cuando la lógica de autorización no pueda tomar una decisión definitiva
- **Límites de Permiso**: Separación clara entre diferentes niveles de privilegio y acceso a recursos
- **Registro de Auditoría**: Registro completo de todas las decisiones de autorización para monitoreo de seguridad
- **Revisiones Regulares de Acceso**: Validación periódica de permisos de usuario y asignaciones de privilegios

## 2. **Controles de Seguridad y Anti-Passthrough de Tokens**

**Riesgo OWASP MCP Abordado**: [MCP01 - Mala Gestión de Tokens y Exposición de Secretos](https://microsoft.github.io/mcp-azure-security-guide/mcp/mcp01-token-mismanagement/)

### **Prevención de Passthrough de Tokens**

**El passthrough de tokens está explícitamente prohibido** en la Especificación de Autorización MCP debido a riesgos críticos de seguridad:

**Riesgos de Seguridad Abordados:**
- **Evasión de Controles**: Se omiten controles esenciales de seguridad como limitación de tasa, validación de solicitudes y monitoreo de tráfico
- **Ruptura de Responsabilidad**: Hace imposible identificar al cliente, corrompiendo trazas de auditoría e investigaciones de incidentes
- **Exfiltración Basada en Proxy**: Permite que actores maliciosos usen servidores como intermediarios para acceso no autorizado a datos
- **Violaciones del Límite de Confianza**: Rompe las suposiciones de confianza de servicios aguas abajo sobre el origen de tokens
- **Movimiento Lateral**: Tokens comprometidos en múltiples servicios permiten una expansión más amplia del ataque

**Controles de Implementación:**
```yaml
Token Validation Requirements:
  audience_validation: MANDATORY
  issuer_verification: MANDATORY  
  signature_check: MANDATORY
  expiration_enforcement: MANDATORY
  scope_validation: MANDATORY
  
Token Lifecycle Management:
  rotation_frequency: "Short-lived tokens preferred"
  secure_storage: "Azure Key Vault or equivalent"
  transmission_security: "TLS 1.3 minimum"
  replay_protection: "Implemented via nonce/timestamp"
```

### **Patrones Seguros para Gestión de Tokens**

**Mejores Prácticas:**
- **Tokens de Vida Corta**: Minimizar la ventana de exposición con rotación frecuente de tokens
- **Emisión Justo a Tiempo**: Emitir tokens solo cuando sean necesarios para operaciones específicas
- **Almacenamiento Seguro**: Usar módulos de seguridad de hardware (HSM) o bóvedas de claves seguras
- **Vinculación de Tokens**: Validar audiencia y emisor del token para el recurso, cliente y operación MCP previsto
 
- **Monitoreo y Alertas**: Detección en tiempo real de uso indebido de tokens o patrones de acceso no autorizados

## 3. **Controles de Seguridad del Estado de Aplicación**

### **Prevención del Secuestro de Handles de Estado**

**Vectores de Ataque Abordados:**
- **Adivinanza de Handles**: Identificadores predecibles exponen el estado de otro llamante
- **Reutilización entre usuarios**: Un handle robado se usa con una identidad diferente
- **Autorización Implícita**: La posesión de un handle se trata incorrectamente como
  prueba de acceso

**Controles de Handles de Estado:**

```yaml
State Handle Generation:
  randomness_source: "Cryptographically secure RNG"
  entropy_bits: 128 # Minimum recommended
  format: "Base64url encoded"
  predictability: "MUST be non-deterministic"

State Binding:
  user_binding: "Bind server-side to the authenticated principal"
  authorization: "Recheck on every request"
  client_input: "Never trust a client-supplied user ID"
  
State Lifecycle:
  expiration: "Configurable timeout policies"
  rotation: "After privilege escalation events"
  invalidation: "Immediate on security events"
  cleanup: "Automated expired state removal"
```

**Seguridad en el Transporte:**
- **Aplicación de HTTPS**: Requerir HTTPS para transportes HTTP remotos
- **Manejo de Credenciales**: Enviar y validar la autorización en cada solicitud HTTP
- **Aislamiento stdio**: Proteger los servidores locales stdio mediante aislamiento de procesos y
  controles de credenciales del entorno

### **Consideraciones entre con y sin estado**

MCP `2026-07-28` es sin estado a nivel de protocolo. Las aplicaciones aún pueden
mantener estado devolviendo un handle explícito desde una llamada a la herramienta y aceptándolo
como un argumento ordinario en llamadas posteriores.

- Almacenar estado independientemente de cualquier conexión de transporte.
- Vincular handles de estado al servidor principal autenticado.
- Tratar un handle como un nombre, no como una credencial de portador.
- Definir el comportamiento de expiración y recuperación para handles obsoletos.

## 4. **Controles de Seguridad Específicos de IA**

**Riesgos OWASP MCP Abordados**:

- [MCP06 - Subversión del Flujo de Intenciones](https://microsoft.github.io/mcp-azure-security-guide/mcp/mcp06-prompt-injection/)
- [MCP03 - Envenenamiento de Herramientas](https://microsoft.github.io/mcp-azure-security-guide/mcp/mcp03-tool-poisoning/)
- [MCP05 - Inyección y Ejecución de Comandos](https://microsoft.github.io/mcp-azure-security-guide/mcp/mcp05-command-injection/)

### **Defensa contra Inyección de Prompt**

**Integración de Microsoft Prompt Shields:**
```yaml
Detection Mechanisms:
  - "Advanced ML-based instruction detection"
  - "Contextual analysis of external content"
  - "Real-time threat pattern recognition"
  
Protection Techniques:
  - "Spotlighting trusted vs untrusted content"
  - "Delimiter systems for content boundaries"  
  - "Data marking for content source identification"
  
Integration Points:
  - "Azure Content Safety service"
  - "Real-time content filtering"
  - "Threat intelligence updates"
```

**Controles de Implementación:**
- **Saneamiento de Entradas**: Validación y filtrado exhaustivo de todas las entradas de usuario
- **Definición de Límites de Contenido**: Separación clara entre instrucciones del sistema y contenido del usuario
- **Jerarquía de Instrucciones**: Reglas de precedencia adecuadas para instrucciones conflictivas
- **Monitoreo de Salidas**: Detección de salidas potencialmente dañinas o manipuladas

### **Prevención de Envenenamiento de Herramientas**

**Marco de Seguridad para Herramientas:**
```yaml
Tool Definition Protection:
  validation:
    - "Schema validation against expected formats"
    - "Content analysis for malicious instructions" 
    - "Parameter injection detection"
    - "Hidden instruction identification"
  
  integrity_verification:
    - "Cryptographic hashing of tool definitions"
    - "Digital signatures for tool packages"
    - "Version control with change auditing"
    - "Tamper detection mechanisms"
  
  monitoring:
    - "Real-time change detection"
    - "Behavioral analysis of tool usage"
    - "Anomaly detection for execution patterns"
    - "Automated alerting for suspicious modifications"
```

**Gestión Dinámica de Herramientas:**
- **Flujos de Aprobación**: Consentimiento explícito del usuario para modificaciones de herramientas
- **Capacidades de Reversión**: Posibilidad de regresar a versiones anteriores de herramientas
- **Auditoría de Cambios**: Historial completo de modificaciones en la definición de herramientas
- **Evaluación de Riesgos**: Evaluación automatizada de la postura de seguridad de herramientas

## 5. **Prevención de Ataques de Apoderado Confundido**

### **Seguridad de Proxy OAuth**

**Controles de Prevención de Ataques:**
```yaml
Client Registration:
  preferred_methods:
    - "Pre-registration when client and server have an existing relationship"
    - "Client ID Metadata Documents for clients without prior registration"
  compatibility_fallback:
    - "Dynamic Client Registration only when CIMD is unavailable"
    - "Consent bypass prevention mechanisms"  
    - "Cookie-based consent validation"
    - "Redirect URI strict validation"
    
  authorization_flow:
    - "PKCE implementation (OAuth 2.1)"
    - "State parameter validation"
    - "Authorization code binding"
    - "Nonce verification for ID tokens"
```

**Requisitos de Implementación:**
- **Registro de Cliente**: Preferir pre-registro o Metadatos de ID de Cliente
  Documentos; tratar el Registro Dinámico de Clientes como una solución de compatibilidad
- **Verificación de Consentimiento del Usuario**: Los proxies MCP que usan un ID de cliente estático de terceros
  deben obtener consentimiento por cliente antes de reenviar autorización
- **Validación de URI de Redirección**: Validación estricta basada en lista blanca de destinos de redirección
- **Protección del Código de Autorización**: Códigos de corta duración con uso único obligatorio
- **Verificación de Identidad del Cliente**: Validación robusta de credenciales y metadatos del cliente

## 6. **Seguridad en Ejecución de Herramientas**

### **Sandboxing y Aislamiento**

**Aislamiento Basado en Contenedores:**
```yaml
Execution Environment:
  containerization: "Docker/Podman with security profiles"
  resource_limits:
    cpu: "Configurable CPU quotas"
    memory: "Memory usage restrictions"
    disk: "Storage access limitations"
    network: "Network policy enforcement"
  
  privilege_restrictions:
    user_context: "Non-root execution mandatory"
    capability_dropping: "Remove unnecessary Linux capabilities"
    syscall_filtering: "Seccomp profiles for syscall restriction"
    filesystem: "Read-only root with minimal writable areas"
```

**Aislamiento de Procesos:**
- **Contextos de Procesos Separados**: Cada ejecución de herramienta en espacio de proceso aislado
- **Comunicación Inter-Procesos**: Mecanismos IPC seguros con validación
- **Monitoreo de Procesos**: Análisis del comportamiento en tiempo de ejecución y detección de anomalías
- **Aplicación de Recursos**: Límites estrictos en CPU, memoria y operaciones I/O

### **Implementación de Mínimos Privilegios**

**Gestión de Permisos:**
```yaml
Access Control:
  file_system:
    - "Minimal required directory access"
    - "Read-only access where possible"
    - "Temporary file cleanup automation"
    
  network_access:
    - "Explicit allowlist for external connections"
    - "DNS resolution restrictions" 
    - "Port access limitations"
    - "SSL/TLS certificate validation"
  
  system_resources:
    - "No administrative privilege elevation"
    - "Limited system call access"
    - "No hardware device access"
    - "Restricted environment variable access"
```

## 7. **Controles de Seguridad en la Cadena de Suministro**

**Riesgo MCP OWASP Abordado**: [MCP04 - Ataques a la Cadena de Suministro de Software y Manipulación de Dependencias](https://microsoft.github.io/mcp-azure-security-guide/mcp/mcp04-supply-chain/)

### **Verificación de Dependencias**

**Seguridad Integral de Componentes:**
```yaml
Software Dependencies:
  scanning: 
    - "Automated vulnerability scanning (GitHub Advanced Security)"
    - "License compliance verification"
    - "Known vulnerability database checks"
    - "Malware detection and analysis"
  
  verification:
    - "Package signature verification"
    - "Checksum validation"
    - "Provenance attestation"
    - "Software Bill of Materials (SBOM)"

AI Components:
  model_verification:
    - "Model provenance validation"
    - "Training data source verification" 
    - "Model behavior testing"
    - "Adversarial robustness assessment"
  
  service_validation:
    - "Third-party API security assessment"
    - "Service level agreement review"
    - "Data handling compliance verification"
    - "Incident response capability evaluation"
```

### **Monitoreo Continuo**

**Detección de Amenazas en la Cadena de Suministro:**
- **Monitoreo de Salud de Dependencias**: Evaluación continua de todas las dependencias por problemas de seguridad
- **Integración de Inteligencia de Amenazas**: Actualizaciones en tiempo real sobre amenazas emergentes en la cadena de suministro
- **Análisis de Comportamiento**: Detección de comportamiento inusual en componentes externos
- **Respuesta Automatizada**: Contención inmediata de componentes comprometidos

## 8. **Controles de Monitoreo y Detección**

**Riesgo MCP OWASP Abordado**: [MCP08 - Falta de Auditoría y Telemetría](https://microsoft.github.io/mcp-azure-security-guide/mcp/mcp08-telemetry/)

### **Gestión de Información y Eventos de Seguridad (SIEM)**

**Estrategia Integral de Registro:**
```yaml
Authentication Events:
  - "All authentication attempts (success/failure)"
  - "Token issuance and validation events"
  - "Session creation, modification, termination"
  - "Authorization decisions and policy evaluations"

Tool Execution:
  - "Tool invocation details and parameters"
  - "Execution duration and resource usage"
  - "Output generation and content analysis"
  - "Error conditions and exception handling"

Security Events:
  - "Potential prompt injection attempts"
  - "Tool poisoning detection events"
  - "Session hijacking indicators"
  - "Unusual access patterns and anomalies"
```

### **Detección de Amenazas en Tiempo Real**

**Análisis Conductual:**
- **Análisis de Comportamiento de Usuarios (UBA)**: Detección de patrones inusuales de acceso de usuarios
- **Análisis de Comportamiento de Entidades (EBA)**: Monitoreo del comportamiento de servidores y herramientas MCP
- **Detección de Anomalías mediante Aprendizaje Automático**: Identificación impulsada por IA de amenazas de seguridad
- **Correlación con Inteligencia de Amenazas**: Coincidencia de actividades observadas con patrones de ataque conocidos

## 9. **Respuesta y Recuperación ante Incidentes**

### **Capacidades de Respuesta Automatizada**

**Acciones de Respuesta Inmediata:**
```yaml
Threat Containment:
  session_management:
    - "Immediate session termination"
    - "Account lockout procedures"
    - "Access privilege revocation"
  
  system_isolation:
    - "Network segmentation activation"
    - "Service isolation protocols"
    - "Communication channel restriction"

Recovery Procedures:
  credential_rotation:
    - "Automated token refresh"
    - "API key regeneration"
    - "Certificate renewal"
  
  system_restoration:
    - "Clean state restoration"
    - "Configuration rollback"
    - "Service restart procedures"
```

### **Capacidades Forenses**

**Soporte para Investigaciones:**
- **Preservación de la Traza de Auditoría**: Registro inmutable con integridad criptográfica
- **Recolección de Evidencias**: Recolección automatizada de artefactos de seguridad relevantes
- **Reconstrucción de Cronología**: Secuencia detallada de eventos que llevan a incidentes de seguridad
- **Evaluación de Impacto**: Evaluación del alcance del compromiso y exposición de datos

## **Principios Clave de Arquitectura de Seguridad**

### **Defensa en Profundidad**
- **Múltiples Capas de Seguridad**: No existe un único punto de falla en la arquitectura de seguridad
- **Controles Redundantes**: Medidas de seguridad superpuestas para funciones críticas
- **Mecanismos a Prueba de Fallos**: Configuraciones seguras cuando el sistema encuentra errores o ataques

### **Implementación de Zero Trust**
- **Nunca Confiar, Siempre Verificar**: Validación continua de todas las entidades y solicitudes
- **Principio de Menor Privilegio**: Derechos de acceso mínimos para todos los componentes
- **Microsegmentación**: Controles granulares de red y acceso

### **Evolución Continua de la Seguridad**
- **Adaptación al Panorama de Amenazas**: Actualizaciones regulares para abordar amenazas emergentes
- **Efectividad de Controles de Seguridad**: Evaluación y mejora continua de los controles
- **Cumplimiento de Especificaciones**: Alineación con los estándares de seguridad MCP en evolución

---

## **Recursos para Implementación**

### **Documentación Oficial MCP**
- [Especificación MCP (2026-07-28)](https://modelcontextprotocol.io/specification/2026-07-28/)
- [Mejores Prácticas de Seguridad MCP](https://modelcontextprotocol.io/specification/2026-07-28/basic/security_best_practices)
- [Especificación de Autorización MCP](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization)

### **Recursos de Seguridad OWASP MCP**
- [Guía de Seguridad OWASP MCP para Azure](https://microsoft.github.io/mcp-azure-security-guide/) - Top 10 MCP de OWASP con implementación en Azure
- [OWASP MCP Top 10](https://owasp.org/www-project-mcp-top-10/) - Riesgos oficiales de seguridad MCP de OWASP
- [Taller de Seguridad Summit MCP (Sherpa)](https://azure-samples.github.io/sherpa/) - Entrenamiento práctico de seguridad para MCP en Azure

### **Soluciones de Seguridad de Microsoft**
- [Microsoft Prompt Shields](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)
- [Azure Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/)
- [GitHub Advanced Security](https://github.com/security/advanced-security)
- [Azure Key Vault](https://learn.microsoft.com/azure/key-vault/)

### **Estándares de Seguridad**
- [Mejores Prácticas de Seguridad OAuth 2.0 (RFC 9700)](https://datatracker.ietf.org/doc/html/rfc9700)

- [OWASP Top 10 para Modelos de Lenguaje a Gran Escala](https://genai.owasp.org/)

- [Marco de Ciberseguridad NIST](https://www.nist.gov/cyberframework)

---

> **Importante:** Estos controles de seguridad reflejan la Especificación MCP
> `2026-07-28`. Siempre verifique con la
> [documentación oficial actual](https://modelcontextprotocol.io/specification/2026-07-28/)
> ya que los estándares continúan evolucionando.

## Qué sigue

- Volver a: [Resumen del Módulo de Seguridad](./README.md)
- Continuar a: [Módulo 3: Comenzando](../03-GettingStarted/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Descargo de responsabilidad**:
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional humana. No somos responsables de cualquier malentendido o interpretación errónea que surja del uso de esta traducción.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->