# Mejores Prácticas de Seguridad MCP - Actualización Diciembre 2025

> **Importante**: Este documento refleja los últimos requisitos de seguridad de la [Especificación MCP 2025-11-25](https://spec.modelcontextprotocol.io/specification/2025-11-25/) y las [Mejores Prácticas de Seguridad MCP oficiales](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices). Siempre consulte la especificación actual para obtener la orientación más actualizada.

## Prácticas Esenciales de Seguridad para Implementaciones MCP

El Protocolo de Contexto de Modelo introduce desafíos de seguridad únicos que van más allá de la seguridad tradicional del software. Estas prácticas abordan tanto los requisitos fundamentales de seguridad como las amenazas específicas de MCP, incluyendo inyección de prompts, envenenamiento de herramientas, secuestro de sesiones, problemas de delegado confundido y vulnerabilidades de paso de tokens.

### **Requisitos de Seguridad OBLIGATORIOS** 

**Requisitos Críticos de la Especificación MCP:**

### **Requisitos de Seguridad OBLIGATORIOS** 

**Requisitos Críticos de la Especificación MCP:**

> **NO DEBE**: Los servidores MCP **NO DEBEN** aceptar tokens que no hayan sido emitidos explícitamente para el servidor MCP  
>  
> **DEBE**: Los servidores MCP que implementen autorización **DEBEN** verificar TODAS las solicitudes entrantes  
>  
> **NO DEBE**: Los servidores MCP **NO DEBEN** usar sesiones para autenticación  
>  
> **DEBE**: Los servidores proxy MCP que usen IDs de cliente estáticos **DEBEN** obtener el consentimiento del usuario para cada cliente registrado dinámicamente

---

## 1. **Seguridad de Tokens y Autenticación**

**Controles de Autenticación y Autorización:**  
   - **Revisión Rigurosa de Autorización**: Realizar auditorías exhaustivas de la lógica de autorización del servidor MCP para asegurar que solo los usuarios y clientes previstos puedan acceder a los recursos  
   - **Integración con Proveedores de Identidad Externos**: Usar proveedores de identidad establecidos como Microsoft Entra ID en lugar de implementar autenticación personalizada  
   - **Validación de Audiencia del Token**: Validar siempre que los tokens hayan sido emitidos explícitamente para su servidor MCP; nunca aceptar tokens ascendentes  
   - **Ciclo de Vida Adecuado del Token**: Implementar rotación segura de tokens, políticas de expiración y prevenir ataques de repetición de tokens  

**Almacenamiento Protegido de Tokens:**  
   - Usar Azure Key Vault o almacenes de credenciales seguros similares para todos los secretos  
   - Implementar cifrado para tokens tanto en reposo como en tránsito  
   - Rotación regular de credenciales y monitoreo para accesos no autorizados  

## 2. **Gestión de Sesiones y Seguridad en el Transporte**

**Prácticas Seguras de Sesión:**  
   - **IDs de Sesión Criptográficamente Seguros**: Usar IDs de sesión seguros y no determinísticos generados con generadores de números aleatorios seguros  
   - **Vinculación Específica al Usuario**: Vincular los IDs de sesión a identidades de usuario usando formatos como `<user_id>:<session_id>` para prevenir abuso de sesión entre usuarios  
   - **Gestión del Ciclo de Vida de Sesión**: Implementar expiración, rotación e invalidación adecuadas para limitar ventanas de vulnerabilidad  
   - **Aplicación de HTTPS/TLS**: HTTPS obligatorio para toda comunicación para prevenir la intercepción de IDs de sesión  

**Seguridad en la Capa de Transporte:**  
   - Configurar TLS 1.3 cuando sea posible con gestión adecuada de certificados  
   - Implementar pinning de certificados para conexiones críticas  
   - Rotación regular de certificados y verificación de validez  

## 3. **Protección Contra Amenazas Específicas de IA** 🤖

**Defensa contra Inyección de Prompts:**  
   - **Microsoft Prompt Shields**: Desplegar AI Prompt Shields para detección avanzada y filtrado de instrucciones maliciosas  
   - **Saneamiento de Entradas**: Validar y sanear todas las entradas para prevenir ataques de inyección y problemas de delegado confundido  
   - **Límites de Contenido**: Usar sistemas de delimitadores y marcado de datos para distinguir entre instrucciones confiables y contenido externo  

**Prevención de Envenenamiento de Herramientas:**  
   - **Validación de Metadatos de Herramientas**: Implementar verificaciones de integridad para definiciones de herramientas y monitorear cambios inesperados  
   - **Monitoreo Dinámico de Herramientas**: Supervisar comportamiento en tiempo de ejecución y configurar alertas para patrones de ejecución inesperados  
   - **Flujos de Aprobación**: Requerir aprobación explícita del usuario para modificaciones de herramientas y cambios de capacidades  

## 4. **Control de Acceso y Permisos**

**Principio de Mínimos Privilegios:**  
   - Conceder a los servidores MCP solo los permisos mínimos necesarios para la funcionalidad prevista  
   - Implementar control de acceso basado en roles (RBAC) con permisos detallados  
   - Revisiones regulares de permisos y monitoreo continuo para escalamiento de privilegios  

**Controles de Permisos en Tiempo de Ejecución:**  
   - Aplicar límites de recursos para prevenir ataques de agotamiento de recursos  
   - Usar aislamiento en contenedores para entornos de ejecución de herramientas  
   - Implementar acceso justo a tiempo para funciones administrativas  

## 5. **Seguridad de Contenido y Monitoreo**

**Implementación de Seguridad de Contenido:**  
   - **Integración con Azure Content Safety**: Usar Azure Content Safety para detectar contenido dañino, intentos de jailbreak y violaciones de políticas  
   - **Análisis de Comportamiento**: Implementar monitoreo de comportamiento en tiempo de ejecución para detectar anomalías en la ejecución del servidor MCP y herramientas  
   - **Registro Exhaustivo**: Registrar todos los intentos de autenticación, invocaciones de herramientas y eventos de seguridad con almacenamiento seguro e inviolable  

**Monitoreo Continuo:**  
   - Alertas en tiempo real para patrones sospechosos e intentos de acceso no autorizados  
   - Integración con sistemas SIEM para gestión centralizada de eventos de seguridad  
   - Auditorías de seguridad regulares y pruebas de penetración de implementaciones MCP  

## 6. **Seguridad de la Cadena de Suministro**

**Verificación de Componentes:**  
   - **Escaneo de Dependencias**: Usar escaneo automatizado de vulnerabilidades para todas las dependencias de software y componentes de IA  
   - **Validación de Procedencia**: Verificar el origen, licenciamiento e integridad de modelos, fuentes de datos y servicios externos  
   - **Paquetes Firmados**: Usar paquetes firmados criptográficamente y verificar firmas antes del despliegue  

**Pipeline de Desarrollo Seguro:**  
   - **GitHub Advanced Security**: Implementar escaneo de secretos, análisis de dependencias y análisis estático CodeQL  
   - **Seguridad CI/CD**: Integrar validación de seguridad en pipelines automatizados de despliegue  
   - **Integridad de Artefactos**: Implementar verificación criptográfica para artefactos y configuraciones desplegadas  

## 7. **Seguridad OAuth y Prevención de Delegado Confundido**

**Implementación OAuth 2.1:**  
   - **Implementación PKCE**: Usar Proof Key for Code Exchange (PKCE) para todas las solicitudes de autorización  
   - **Consentimiento Explícito**: Obtener consentimiento del usuario para cada cliente registrado dinámicamente para prevenir ataques de delegado confundido  
   - **Validación de URI de Redirección**: Implementar validación estricta de URIs de redirección e identificadores de cliente  

**Seguridad de Proxy:**  
   - Prevenir eludir la autorización mediante explotación de ID de cliente estático  
   - Implementar flujos de consentimiento adecuados para acceso a APIs de terceros  
   - Monitorear robo de códigos de autorización y accesos no autorizados a APIs  

## 8. **Respuesta a Incidentes y Recuperación**

**Capacidades de Respuesta Rápida:**  
   - **Respuesta Automatizada**: Implementar sistemas automáticos para rotación de credenciales y contención de amenazas  
   - **Procedimientos de Reversión**: Capacidad para revertir rápidamente a configuraciones y componentes conocidos como buenos  
   - **Capacidades Forenses**: Rutas de auditoría detalladas y registros para investigación de incidentes  

**Comunicación y Coordinación:**  
   - Procedimientos claros de escalamiento para incidentes de seguridad  
   - Integración con equipos organizacionales de respuesta a incidentes  
   - Simulacros regulares de incidentes de seguridad y ejercicios de mesa  

## 9. **Cumplimiento y Gobernanza**

**Cumplimiento Regulatorio:**  
   - Asegurar que las implementaciones MCP cumplan con requisitos específicos de la industria (GDPR, HIPAA, SOC 2)  
   - Implementar clasificación de datos y controles de privacidad para el procesamiento de datos de IA  
   - Mantener documentación completa para auditorías de cumplimiento  

**Gestión de Cambios:**  
   - Procesos formales de revisión de seguridad para todas las modificaciones del sistema MCP  
   - Control de versiones y flujos de aprobación para cambios de configuración  
   - Evaluaciones regulares de cumplimiento y análisis de brechas  

## 10. **Controles Avanzados de Seguridad**

**Arquitectura Zero Trust:**  
   - **Nunca Confiar, Siempre Verificar**: Verificación continua de usuarios, dispositivos y conexiones  
   - **Microsegmentación**: Controles granulares de red que aíslan componentes individuales MCP  
   - **Acceso Condicional**: Controles de acceso basados en riesgo que se adaptan al contexto y comportamiento actual  

**Protección de Aplicaciones en Tiempo de Ejecución:**  
   - **Protección de Aplicaciones en Tiempo de Ejecución (RASP)**: Desplegar técnicas RASP para detección de amenazas en tiempo real  
   - **Monitoreo de Rendimiento de Aplicaciones**: Supervisar anomalías de rendimiento que puedan indicar ataques  
   - **Políticas de Seguridad Dinámicas**: Implementar políticas de seguridad que se adapten según el panorama actual de amenazas  

## 11. **Integración con el Ecosistema de Seguridad Microsoft**

**Seguridad Integral Microsoft:**  
   - **Microsoft Defender for Cloud**: Gestión de postura de seguridad en la nube para cargas de trabajo MCP  
   - **Azure Sentinel**: Capacidades SIEM y SOAR nativas en la nube para detección avanzada de amenazas  
   - **Microsoft Purview**: Gobernanza de datos y cumplimiento para flujos de trabajo y fuentes de datos de IA  

**Gestión de Identidad y Acceso:**  
   - **Microsoft Entra ID**: Gestión empresarial de identidad con políticas de acceso condicional  
   - **Privileged Identity Management (PIM)**: Acceso justo a tiempo y flujos de aprobación para funciones administrativas  
   - **Protección de Identidad**: Acceso condicional basado en riesgo y respuesta automatizada a amenazas  

## 12. **Evolución Continua de la Seguridad**

**Mantenerse Actualizado:**  
   - **Monitoreo de Especificaciones**: Revisión regular de actualizaciones de especificación MCP y cambios en guías de seguridad  
   - **Inteligencia de Amenazas**: Integración de fuentes de amenazas específicas de IA e indicadores de compromiso  
   - **Participación en la Comunidad de Seguridad**: Participación activa en la comunidad de seguridad MCP y programas de divulgación de vulnerabilidades  

**Seguridad Adaptativa:**  
   - **Seguridad basada en Aprendizaje Automático**: Uso de detección de anomalías basada en ML para identificar patrones de ataque novedosos  
   - **Análisis Predictivo de Seguridad**: Implementar modelos predictivos para identificación proactiva de amenazas  
   - **Automatización de Seguridad**: Actualizaciones automáticas de políticas de seguridad basadas en inteligencia de amenazas y cambios en especificaciones  

---

## **Recursos Críticos de Seguridad**

### **Documentación Oficial MCP**
- [Especificación MCP (2025-11-25)](https://spec.modelcontextprotocol.io/specification/2025-11-25/)
- [Mejores Prácticas de Seguridad MCP](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices)
- [Especificación de Autorización MCP](https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization)

### **Soluciones de Seguridad Microsoft**
- [Microsoft Prompt Shields](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)
- [Azure Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/)
- [Seguridad Microsoft Entra ID](https://learn.microsoft.com/entra/identity-platform/secure-least-privileged-access)
- [GitHub Advanced Security](https://github.com/security/advanced-security)

### **Estándares de Seguridad**
- [Mejores Prácticas de Seguridad OAuth 2.0 (RFC 9700)](https://datatracker.ietf.org/doc/html/rfc9700)
- [OWASP Top 10 para Modelos de Lenguaje Grande](https://genai.owasp.org/)
- [Marco de Gestión de Riesgos de IA NIST](https://www.nist.gov/itl/ai-risk-management-framework)

### **Guías de Implementación**
- [Azure API Management MCP Authentication Gateway](https://techcommunity.microsoft.com/blog/integrationsonazureblog/azure-api-management-your-auth-gateway-for-mcp-servers/4402690)
- [Microsoft Entra ID con Servidores MCP](https://den.dev/blog/mcp-server-auth-entra-id-session/)

---

> **Aviso de Seguridad**: Las prácticas de seguridad MCP evolucionan rápidamente. Siempre verifique contra la [especificación MCP actual](https://spec.modelcontextprotocol.io/) y la [documentación oficial de seguridad](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices) antes de implementar.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso legal**:
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o interpretaciones erróneas derivadas del uso de esta traducción.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->