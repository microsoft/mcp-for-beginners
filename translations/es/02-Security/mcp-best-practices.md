# Mejores Prácticas de Seguridad MCP 2025

Esta guía integral describe las mejores prácticas esenciales de seguridad para implementar sistemas Model Context Protocol (MCP) basados en la última **Especificación MCP 2025-11-25** y los estándares actuales de la industria. Estas prácticas abordan tanto preocupaciones tradicionales de seguridad como amenazas específicas de IA únicas para implementaciones MCP.

## Requisitos Críticos de Seguridad

### Controles de Seguridad Obligatorios (Requisitos MUST)

1. **Validación de Tokens**: Los servidores MCP **NO DEBEN** aceptar tokens que no hayan sido emitidos explícitamente para el propio servidor MCP.
2. **Verificación de Autorización**: Los servidores MCP que implementen autorización **DEBEN** verificar TODAS las solicitudes entrantes y **NO DEBEN** usar sesiones para autenticación.  
3. **Consentimiento del Usuario**: Los servidores proxy MCP que usen IDs de cliente estáticos **DEBEN** obtener consentimiento explícito del usuario para cada cliente registrado dinámicamente.
4. **IDs de Sesión Seguros**: Los servidores MCP **DEBEN** usar IDs de sesión criptográficamente seguros y no determinísticos generados con generadores de números aleatorios seguros.

## Prácticas Básicas de Seguridad

### 1. Validación y Saneamiento de Entradas
- **Validación Integral de Entradas**: Validar y sanear todas las entradas para prevenir ataques de inyección, problemas de delegado confundido y vulnerabilidades de inyección en prompts.
- **Aplicación de Esquemas de Parámetros**: Implementar validación estricta de esquemas JSON para todos los parámetros de herramientas y entradas API.
- **Filtrado de Contenido**: Usar Microsoft Prompt Shields y Azure Content Safety para filtrar contenido malicioso en prompts y respuestas.
- **Saneamiento de Salidas**: Validar y sanear todas las salidas del modelo antes de presentarlas a usuarios o sistemas posteriores.

### 2. Excelencia en Autenticación y Autorización  
- **Proveedores de Identidad Externos**: Delegar la autenticación a proveedores de identidad establecidos (Microsoft Entra ID, proveedores OAuth 2.1) en lugar de implementar autenticación personalizada.
- **Permisos Granulares**: Implementar permisos específicos por herramienta siguiendo el principio de menor privilegio.
- **Gestión del Ciclo de Vida de Tokens**: Usar tokens de acceso de corta duración con rotación segura y validación adecuada de audiencia.
- **Autenticación Multifactor**: Requerir MFA para todo acceso administrativo y operaciones sensibles.

### 3. Protocolos de Comunicación Seguros
- **Seguridad en la Capa de Transporte**: Usar HTTPS/TLS 1.3 para todas las comunicaciones MCP con validación adecuada de certificados.
- **Cifrado de Extremo a Extremo**: Implementar capas adicionales de cifrado para datos altamente sensibles en tránsito y en reposo.
- **Gestión de Certificados**: Mantener una gestión adecuada del ciclo de vida de certificados con procesos automatizados de renovación.
- **Aplicación de Versión de Protocolo**: Usar la versión actual del protocolo MCP (2025-11-25) con negociación adecuada de versión.

### 4. Limitación Avanzada de Tasa y Protección de Recursos
- **Limitación de Tasa Multicapa**: Implementar limitación de tasa a nivel de usuario, sesión, herramienta y recurso para prevenir abusos.
- **Limitación de Tasa Adaptativa**: Usar limitación de tasa basada en aprendizaje automático que se adapte a patrones de uso e indicadores de amenaza.
- **Gestión de Cuotas de Recursos**: Establecer límites apropiados para recursos computacionales, uso de memoria y tiempo de ejecución.
- **Protección contra DDoS**: Desplegar sistemas integrales de protección DDoS y análisis de tráfico.

### 5. Registro y Monitoreo Integral
- **Registro de Auditoría Estructurado**: Implementar registros detallados y buscables para todas las operaciones MCP, ejecuciones de herramientas y eventos de seguridad.
- **Monitoreo de Seguridad en Tiempo Real**: Desplegar sistemas SIEM con detección de anomalías impulsada por IA para cargas de trabajo MCP.
- **Registro Cumplidor de Privacidad**: Registrar eventos de seguridad respetando los requisitos y regulaciones de privacidad de datos.
- **Integración de Respuesta a Incidentes**: Conectar sistemas de registro a flujos de trabajo automatizados de respuesta a incidentes.

### 6. Prácticas Mejoradas de Almacenamiento Seguro
- **Módulos de Seguridad de Hardware**: Usar almacenamiento de claves respaldado por HSM (Azure Key Vault, AWS CloudHSM) para operaciones criptográficas críticas.
- **Gestión de Claves de Cifrado**: Implementar rotación adecuada de claves, segregación y controles de acceso para claves de cifrado.
- **Gestión de Secretos**: Almacenar todas las claves API, tokens y credenciales en sistemas dedicados de gestión de secretos.
- **Clasificación de Datos**: Clasificar datos según niveles de sensibilidad y aplicar medidas de protección apropiadas.

### 7. Gestión Avanzada de Tokens
- **Prevención de Passthrough de Tokens**: Prohibir explícitamente patrones de passthrough de tokens que evadan controles de seguridad.
- **Validación de Audiencia**: Verificar siempre que las reclamaciones de audiencia del token coincidan con la identidad del servidor MCP previsto.
- **Autorización Basada en Reclamaciones**: Implementar autorización granular basada en reclamaciones de tokens y atributos de usuario.
- **Vinculación de Tokens**: Vincular tokens a sesiones, usuarios o dispositivos específicos cuando sea apropiado.

### 8. Gestión Segura de Sesiones
- **IDs de Sesión Criptográficos**: Generar IDs de sesión usando generadores de números aleatorios criptográficamente seguros (no secuencias predecibles).
- **Vinculación Específica de Usuario**: Vincular IDs de sesión a información específica del usuario usando formatos seguros como `<user_id>:<session_id>`.
- **Controles del Ciclo de Vida de Sesión**: Implementar mecanismos adecuados de expiración, rotación e invalidación de sesiones.
- **Encabezados de Seguridad para Sesiones**: Usar encabezados HTTP de seguridad apropiados para protección de sesiones.

### 9. Controles de Seguridad Específicos para IA
- **Defensa contra Inyección en Prompts**: Desplegar Microsoft Prompt Shields con técnicas de spotlighting, delimitadores y datamarking.
- **Prevención de Envenenamiento de Herramientas**: Validar metadatos de herramientas, monitorear cambios dinámicos y verificar integridad de herramientas.
- **Validación de Salidas del Modelo**: Escanear salidas del modelo para posibles fugas de datos, contenido dañino o violaciones de políticas de seguridad.
- **Protección de Ventana de Contexto**: Implementar controles para prevenir envenenamiento y ataques de manipulación de la ventana de contexto.

### 10. Seguridad en la Ejecución de Herramientas
- **Sandboxing de Ejecución**: Ejecutar herramientas en entornos aislados y contenerizados con límites de recursos.
- **Separación de Privilegios**: Ejecutar herramientas con privilegios mínimos requeridos y cuentas de servicio separadas.
- **Aislamiento de Red**: Implementar segmentación de red para entornos de ejecución de herramientas.
- **Monitoreo de Ejecución**: Monitorear la ejecución de herramientas para detectar comportamientos anómalos, uso de recursos y violaciones de seguridad.

### 11. Validación Continua de Seguridad
- **Pruebas de Seguridad Automatizadas**: Integrar pruebas de seguridad en pipelines CI/CD con herramientas como GitHub Advanced Security.
- **Gestión de Vulnerabilidades**: Escanear regularmente todas las dependencias, incluidos modelos de IA y servicios externos.
- **Pruebas de Penetración**: Realizar evaluaciones de seguridad regulares dirigidas específicamente a implementaciones MCP.
- **Revisiones de Código de Seguridad**: Implementar revisiones de seguridad obligatorias para todos los cambios de código relacionados con MCP.

### 12. Seguridad en la Cadena de Suministro para IA
- **Verificación de Componentes**: Verificar la procedencia, integridad y seguridad de todos los componentes de IA (modelos, embeddings, APIs).
- **Gestión de Dependencias**: Mantener inventarios actualizados de todo el software y dependencias de IA con seguimiento de vulnerabilidades.
- **Repositorios Confiables**: Usar fuentes verificadas y confiables para todos los modelos, bibliotecas y herramientas de IA.
- **Monitoreo de la Cadena de Suministro**: Monitorear continuamente compromisos en proveedores de servicios de IA y repositorios de modelos.

## Patrones Avanzados de Seguridad

### Arquitectura Zero Trust para MCP
- **Nunca Confiar, Siempre Verificar**: Implementar verificación continua para todos los participantes MCP.
- **Microsegmentación**: Aislar componentes MCP con controles granulares de red e identidad.
- **Acceso Condicional**: Implementar controles de acceso basados en riesgo que se adapten al contexto y comportamiento.
- **Evaluación Continua de Riesgos**: Evaluar dinámicamente la postura de seguridad basada en indicadores actuales de amenaza.

### Implementación de IA que Preserva la Privacidad
- **Minimización de Datos**: Exponer solo los datos mínimos necesarios para cada operación MCP.
- **Privacidad Diferencial**: Implementar técnicas que preserven la privacidad para el procesamiento de datos sensibles.
- **Cifrado Homomórfico**: Usar técnicas avanzadas de cifrado para computación segura sobre datos cifrados.
- **Aprendizaje Federado**: Implementar enfoques de aprendizaje distribuido que preserven la localidad y privacidad de datos.

### Respuesta a Incidentes para Sistemas de IA
- **Procedimientos Específicos para IA**: Desarrollar procedimientos de respuesta a incidentes adaptados a amenazas específicas de IA y MCP.
- **Respuesta Automatizada**: Implementar contención y remediación automatizadas para incidentes comunes de seguridad en IA.  
- **Capacidades Forenses**: Mantener preparación forense para compromisos de sistemas IA y brechas de datos.
- **Procedimientos de Recuperación**: Establecer procedimientos para recuperación de envenenamiento de modelos IA, ataques de inyección en prompts y compromisos de servicios.

## Recursos y Estándares para Implementación

### Documentación Oficial MCP
- [MCP Specification 2025-11-25](https://spec.modelcontextprotocol.io/specification/2025-11-25/) - Especificación actual del protocolo MCP
- [MCP Security Best Practices](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices) - Guía oficial de seguridad
- [MCP Authorization Specification](https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization) - Patrones de autenticación y autorización
- [MCP Transport Security](https://modelcontextprotocol.io/specification/2025-11-25/transports/) - Requisitos de seguridad en la capa de transporte

### Soluciones de Seguridad Microsoft
- [Microsoft Prompt Shields](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection) - Protección avanzada contra inyección en prompts
- [Azure Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/) - Filtrado integral de contenido IA
- [Microsoft Entra ID](https://learn.microsoft.com/entra/identity-platform/v2-oauth2-auth-code-flow) - Gestión empresarial de identidad y acceso
- [Azure Key Vault](https://learn.microsoft.com/azure/key-vault/general/basic-concepts) - Gestión segura de secretos y credenciales
- [GitHub Advanced Security](https://github.com/security/advanced-security) - Escaneo de seguridad en cadena de suministro y código

### Estándares y Marcos de Seguridad
- [OAuth 2.1 Security Best Practices](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-security-topics) - Guía actual de seguridad OAuth
- [OWASP Top 10](https://owasp.org/www-project-top-ten/) - Riesgos de seguridad en aplicaciones web
- [OWASP Top 10 for LLMs](https://genai.owasp.org/download/43299/?tmstv=1731900559) - Riesgos de seguridad específicos de IA
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework) - Gestión integral de riesgos IA
- [ISO 27001:2022](https://www.iso.org/standard/27001) - Sistemas de gestión de seguridad de la información

### Guías y Tutoriales de Implementación
- [Azure API Management as MCP Auth Gateway](https://techcommunity.microsoft.com/blog/integrationsonazureblog/azure-api-management-your-auth-gateway-for-mcp-servers/4402690) - Patrones empresariales de autenticación
- [Microsoft Entra ID with MCP Servers](https://den.dev/blog/mcp-server-auth-entra-id-session/) - Integración de proveedores de identidad
- [Secure Token Storage Implementation](https://youtu.be/uRdX37EcCwg?si=6fSChs1G4glwXRy2) - Mejores prácticas en gestión de tokens
- [End-to-End Encryption for AI](https://learn.microsoft.com/azure/architecture/example-scenario/confidential/end-to-end-encryption) - Patrones avanzados de cifrado

### Recursos Avanzados de Seguridad
- [Microsoft Security Development Lifecycle](https://www.microsoft.com/sdl) - Prácticas de desarrollo seguro
- [AI Red Team Guidance](https://learn.microsoft.com/security/ai-red-team/) - Pruebas de seguridad específicas para IA
- [Threat Modeling for AI Systems](https://learn.microsoft.com/security/adoption/approach/threats-ai) - Metodología de modelado de amenazas IA
- [Privacy Engineering for AI](https://www.microsoft.com/security/blog/2021/07/13/microsofts-pet-project-privacy-enhancing-technologies-in-action/) - Técnicas de IA que preservan la privacidad

### Cumplimiento y Gobernanza
- [GDPR Compliance for AI](https://learn.microsoft.com/compliance/regulatory/gdpr-data-protection-impact-assessments) - Cumplimiento de privacidad en sistemas IA
- [AI Governance Framework](https://learn.microsoft.com/azure/architecture/guide/responsible-ai/responsible-ai-overview) - Implementación responsable de IA
- [SOC 2 for AI Services](https://learn.microsoft.com/compliance/regulatory/offering-soc) - Controles de seguridad para proveedores de servicios IA
- [HIPAA Compliance for AI](https://learn.microsoft.com/compliance/regulatory/offering-hipaa-hitech) - Requisitos de cumplimiento para IA en salud

### DevSecOps y Automatización
- [DevSecOps Pipeline for AI](https://learn.microsoft.com/azure/devops/migrate/security-validation-cicd-pipeline) - Pipelines seguros para desarrollo IA
- [Automated Security Testing](https://learn.microsoft.com/security/engineering/devsecops) - Validación continua de seguridad
- [Infrastructure as Code Security](https://learn.microsoft.com/security/engineering/infrastructure-security) - Despliegue seguro de infraestructura
- [Container Security for AI](https://learn.microsoft.com/azure/container-instances/container-instances-image-security) - Seguridad en contenerización de cargas IA

### Monitoreo y Respuesta a Incidentes  
- [Azure Monitor for AI Workloads](https://learn.microsoft.com/azure/azure-monitor/overview) - Soluciones integrales de monitoreo
- [AI Security Incident Response](https://learn.microsoft.com/security/compass/incident-response-playbooks) - Procedimientos específicos para incidentes IA
- [SIEM for AI Systems](https://learn.microsoft.com/azure/sentinel/overview) - Gestión de información y eventos de seguridad
- [Threat Intelligence for AI](https://learn.microsoft.com/security/compass/security-operations-videos-and-decks#threat-intelligence) - Fuentes de inteligencia de amenazas IA

## 🔄 Mejora Continua

### Mantenerse Actualizado con Estándares en Evolución
- **Actualizaciones de la Especificación MCP**: Monitorear cambios oficiales en la especificación MCP y avisos de seguridad.
- **Inteligencia de Amenazas**: Suscribirse a fuentes de amenazas de seguridad IA y bases de datos de vulnerabilidades.  
- **Participación Comunitaria**: Participar en discusiones y grupos de trabajo de la comunidad de seguridad MCP.
- **Evaluación Regular**: Realizar evaluaciones trimestrales de la postura de seguridad y actualizar prácticas en consecuencia.

### Contribuir a la Seguridad MCP
- **Investigación en Seguridad**: Contribuir a la investigación de seguridad MCP y programas de divulgación de vulnerabilidades.
- **Compartir Mejores Prácticas**: Compartir implementaciones de seguridad y lecciones aprendidas con la comunidad.
- **Desarrollo Estándar**: Participar en el desarrollo de especificaciones MCP y la creación de estándares de seguridad  
- **Desarrollo de Herramientas**: Desarrollar y compartir herramientas y bibliotecas de seguridad para el ecosistema MCP  

---

*Este documento refleja las mejores prácticas de seguridad MCP al 18 de diciembre de 2025, basado en la Especificación MCP 2025-11-25. Las prácticas de seguridad deben revisarse y actualizarse regularmente a medida que el protocolo y el panorama de amenazas evolucionan.*

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o interpretaciones erróneas derivadas del uso de esta traducción.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->