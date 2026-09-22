# Mejores prácticas de seguridad MCP - Actualización septiembre 2026

Esta guía integral describe las mejores prácticas de seguridad esenciales para
implementar sistemas del Protocolo de Contexto de Modelo (MCP) basados en
**Especificación MCP 2026-07-28** y los estándares industriales actuales. Estas
prácticas abordan tanto preocupaciones tradicionales de seguridad como amenazas específicas de IA
únicas para las implementaciones MCP.

## Requisitos críticos de seguridad

### Controles de seguridad obligatorios (Requisitos MUST)

1. **Validación de tokens**: Los servidores MCP **NO DEBEN** aceptar ningún token que no haya sido emitido explícitamente para el servidor MCP mismo
2. **Verificación de autorización**: Los servidores MCP que implementen autorización **DEBEN** verificar TODAS las solicitudes entrantes y **NO DEBEN** usar sesiones para autenticación  
3. **Consentimiento del usuario**: Los servidores proxy MCP que usen IDs de cliente terceros estáticos **DEBEN** obtener consentimiento explícito para cada cliente MCP antes de reenviar un flujo de autorización
4. **Seguridad del identificador de estado**: Los servidores MCP **NO DEBEN** tratar la posesión de un
	identificador de estado de aplicación como autenticación y **DEBEN** autorizar cada
	solicitud que use uno

## Prácticas básicas de seguridad

### 1. Validación y saneamiento de entradas
- **Validación completa de entradas**: Validar y sanear todas las entradas para prevenir ataques de inyección, problemas de intermediarios confundidos y vulnerabilidades de inyección en prompts
- **Aplicación de esquema de parámetros**: Implementar validación estricta de esquema JSON para todos los parámetros de herramientas y entradas API
- **Filtrado de contenido**: Usar Microsoft Prompt Shields y Azure Content Safety para filtrar contenido malicioso en prompts y respuestas
- **Saneamiento de salidas**: Validar y sanear todas las salidas del modelo antes de presentarlas a usuarios o sistemas posteriores

### 2. Excelencia en autenticación y autorización  
- **Proveedores de identidad externos**: Delegar autenticación a proveedores de identidad establecidos (Microsoft Entra ID, proveedores OAuth 2.1) en lugar de implementar autenticación personalizada
- **Registro del cliente**: Preferir Documentos de metadatos de ID de cliente o pre-registro; usar registro dinámico de cliente obsoleto solo por compatibilidad
- **Permisos detallados**: Implementar permisos granulares específicos para cada herramienta siguiendo el principio de menor privilegio
- **Gestión del ciclo de vida de tokens**: Usar tokens de acceso de corta duración con rotación segura y validación adecuada de audiencia
- **Autenticación multifactor**: Requerir MFA para todo acceso administrativo y operaciones sensibles

### 3. Protocolos de comunicación seguros
- **Seguridad de capa de transporte**: Usar HTTPS con validación adecuada de certificados
	para comunicaciones HTTP remotas MCP; usar aislamiento de procesos y credenciales
	de entorno para servidores locales stdio
- **Cifrado de extremo a extremo**: Implementar capas adicionales de cifrado para datos altamente sensibles en tránsito y en reposo
- **Gestión de certificados**: Mantener una gestión adecuada del ciclo de vida de certificados con procesos automatizados de renovación
- **Aplicación de versión de protocolo**: Usar MCP `2026-07-28`, incluir los metadatos de versión requeridos
	en cada solicitud y rechazar versiones no soportadas

### 4. Limitación avanzada de tasa y protección de recursos
- **Limitación de tasa multinivel**: Implementar limitación de tasa por usuario, credencial,
  operación, herramienta y recurso para prevenir abusos
- **Limitación de tasa adaptativa**: Usar limitación de tasa basada en aprendizaje automático que se adapta a patrones de uso e indicadores de amenazas
- **Gestión de cuotas de recursos**: Establecer límites apropiados para recursos computacionales, uso de memoria y tiempo de ejecución
- **Protección contra DDoS**: Desplegar sistemas completos de protección contra DDoS y análisis de tráfico

### 5. Registro y monitoreo exhaustivos
- **Registro estructurado de auditoría**: Implementar registros detallados y buscables para todas las operaciones MCP, ejecuciones de herramientas y eventos de seguridad

- **Monitoreo de Seguridad en Tiempo Real**: Despliegue sistemas SIEM con detección de anomalías impulsada por IA para cargas de trabajo MCP
- **Registro Cumpliendo la Privacidad**: Registre eventos de seguridad respetando los requisitos y regulaciones de privacidad de datos
- **Integración de Respuesta a Incidentes**: Conecte sistemas de registro con flujos de trabajo automatizados de respuesta a incidentes

### 6. Prácticas Mejoradas de Almacenamiento Seguro
- **Módulos de Seguridad de Hardware**: Use almacenamiento de llaves respaldado por HSM (Azure Key Vault, AWS CloudHSM) para operaciones criptográficas críticas
- **Gestión de Llaves de Encriptación**: Implemente rotación adecuada de llaves, segregación y controles de acceso para llaves de encriptación
- **Gestión de Secretos**: Almacene todas las claves API, tokens y credenciales en sistemas dedicados de gestión de secretos
- **Clasificación de Datos**: Clasifique los datos según niveles de sensibilidad y aplique medidas de protección adecuadas

### 7. Gestión Avanzada de Tokens
- **Prevención de Paso de Token**: Prohíba explícitamente patrones de paso de token que evadan controles de seguridad
- **Validación de Audiencia**: Verifique siempre que las reclamaciones de audiencia del token coincidan con la identidad del servidor MCP previsto
- **Autorización Basada en Reclamaciones**: Implemente autorización detallada basada en reclamaciones del token y atributos del usuario
- **Vinculación de Token**: Valide que los tokens apunten al recurso MCP previsto y
	vincule el estado de la aplicación gestionado por el servidor con el principal autenticado

### 8. Estado Seguro de la Aplicación

- **Manejadores de Estado Criptográficos**: Genere manejadores opacos y no deterministas
	para el estado que abarca solicitudes
- **Vinculación Específica de Usuario**: Vincule cada manejador del lado servidor al principal autenticado; no confíe en una ID de usuario proporcionada por el cliente

- **Controles de Ciclo de Vida**: Expire y revoque manejadores, y defina cómo los llamadores
	recuperan estado obsoleto
- **Autorización por Solicitud**: Verifique nuevamente la autorización cada vez que se presenta un manejador; un manejador es un nombre, no una credencial


### 9. Controles de Seguridad Específicos para IA
- **Defensa contra Inyección de Prompt**: Despliegue Microsoft Prompt Shields con técnicas de iluminación, delimitadores y marcado de datos
- **Prevención de Envenenamiento de Herramientas**: Valide metadatos de herramientas, monitoree cambios dinámicos y verifique la integridad de las herramientas
- **Validación de Salida del Modelo**: Escanee las salidas del modelo en busca de posibles fugas de datos, contenido dañino o violaciones de políticas de seguridad
- **Protección de Ventana de Contexto**: Implemente controles para evitar envenenamiento de la ventana de contexto y ataques de manipulación

### 10. Seguridad en la Ejecución de Herramientas
- **Ejecución en Entornos Aislados**: Ejecute herramientas en ambientes containerizados e aislados con límites de recursos
- **Separación de Privilegios**: Ejecute herramientas con los mínimos privilegios requeridos y cuentas de servicio separadas
- **Aislamiento de Red**: Implemente segmentación de red para los entornos de ejecución de herramientas
- **Monitoreo de Ejecución**: Monitoree la ejecución de herramientas para comportamientos anómalos, uso de recursos y violaciones de seguridad

### 11. Validación Continua de Seguridad
- **Pruebas de Seguridad Automatizadas**: Integre pruebas de seguridad en pipelines CI/CD con herramientas como GitHub Advanced Security
- **Gestión de Vulnerabilidades**: Escanee regularmente todas las dependencias, incluidos modelos de IA y servicios externos
- **Pruebas de Penetración**: Realice evaluaciones periódicas de seguridad específicamente dirigidas a implementaciones MCP
- **Revisiones de Código de Seguridad**: Implemente revisiones obligatorias de seguridad para todos los cambios de código relacionados con MCP

### 12. Seguridad de la Cadena de Suministro para IA
- **Verificación de Componentes**: Verifique la procedencia, integridad y seguridad de todos los componentes de IA (modelos, embeddings, APIs)
- **Gestión de Dependencias**: Mantenga inventarios actualizados de todas las dependencias de software e IA con seguimiento de vulnerabilidades
- **Repositorios Confiables**: Utilice fuentes verificadas y confiables para todos los modelos, bibliotecas y herramientas de IA

- **Monitoreo de la cadena de suministro**: Supervisar continuamente en busca de compromisos en proveedores de servicios de IA y repositorios de modelos


## Patrones Avanzados de Seguridad

### Arquitectura Zero Trust para MCP
- **Nunca confiar, siempre verificar**: Implementar verificación continua para todos los participantes del MCP
- **Microsegmentación**: Aislar componentes del MCP con controles granulares de red e identidad
- **Acceso Condicionado**: Implementar controles de acceso basados en riesgos que se adapten al contexto y comportamiento
- **Evaluación Continua de Riesgos**: Evaluar dinámicamente la postura de seguridad basada en indicadores actuales de amenazas

### Implementación de IA que Preserva la Privacidad
- **Minimización de Datos**: Exponer solo los datos mínimos necesarios para cada operación del MCP
- **Privacidad Diferencial**: Implementar técnicas de preservación de privacidad para el procesamiento de datos sensibles
- **Encriptación Homomórfica**: Usar técnicas avanzadas de cifrado para computación segura sobre datos cifrados
- **Aprendizaje Federado**: Implementar enfoques de aprendizaje distribuido que preserven la localización y privacidad de los datos

### Respuesta a Incidentes para Sistemas de IA
- **Procedimientos Específicos para Incidentes de IA**: Desarrollar procedimientos de respuesta a incidentes adaptados a amenazas específicas de IA y MCP
- **Respuesta Automatizada**: Implementar contención y remediación automática para incidentes comunes de seguridad en IA  
- **Capacidades Forenses**: Mantener preparación forense para compromisos del sistema de IA y brechas de datos
- **Procedimientos de Recuperación**: Establecer procedimientos para recuperarse de envenenamiento de modelos IA, ataques de inyección de solicitudes y compromisos de servicio

## Recursos y Estándares de Implementación

### 🏔️ Capacitación Práctica en Seguridad
- **[Taller MCP Security Summit (Sherpa)](https://azure-samples.github.io/sherpa/)** - Taller práctico integral para asegurar servidores MCP en Azure
- **[Guía de Seguridad MCP Azure OWASP](https://microsoft.github.io/mcp-azure-security-guide/)** - Arquitectura de referencia y guía de implementación del Top 10 MCP OWASP

### Documentación Oficial MCP
- [Especificación MCP 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/) - Especificación actual del protocolo MCP
- [Mejores Prácticas de Seguridad MCP](https://modelcontextprotocol.io/specification/2026-07-28/basic/security_best_practices) - Guía oficial de seguridad
- [Especificación de Autorización MCP](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization) - Patrones de autorización HTTP
- [Transporte MCP](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/) - Requisitos de transporte

### Soluciones de Seguridad Microsoft
- [Microsoft Prompt Shields](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection) - Protección avanzada contra inyección de solicitudes
- [Azure Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/) - Filtrado integral de contenido de IA
- [Microsoft Entra ID](https://learn.microsoft.com/entra/identity-platform/v2-oauth2-auth-code-flow) - Gestión empresarial de identidad y acceso
- [Azure Key Vault](https://learn.microsoft.com/azure/key-vault/general/basic-concepts) - Gestión segura de secretos y credenciales
- [GitHub Advanced Security](https://github.com/security/advanced-security) - Escaneo de seguridad para cadena de suministro y código

### Estándares y Marcos de Seguridad
- [Mejores Prácticas de Seguridad OAuth 2.1](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-security-topics) - Guía actual de seguridad OAuth
- [OWASP Top 10](https://owasp.org/www-project-top-ten/) - Riesgos de seguridad de aplicaciones web
- [OWASP Top 10 para LLMs](https://genai.owasp.org/download/43299/?tmstv=1731900559) - Riesgos de seguridad específicos de IA
- [Marco de Gestión de Riesgos de IA del NIST](https://www.nist.gov/itl/ai-risk-management-framework) - Gestión integral de riesgos de IA
- [ISO 27001:2022](https://www.iso.org/standard/27001) - Sistemas de gestión de seguridad de la información

### Guías y Tutoriales de Implementación
- [Azure API Management como MCP Auth Gateway](https://techcommunity.microsoft.com/blog/integrationsonazureblog/azure-api-management-your-auth-gateway-for-mcp-servers/4402690) - Patrones empresariales de autenticación
- [Microsoft Entra ID con servidores MCP](https://den.dev/blog/mcp-server-auth-entra-id-session/) - Integración del proveedor de identidad
- [Implementación de Almacenamiento Seguro de Tokens](https://youtu.be/uRdX37EcCwg?si=6fSChs1G4glwXRy2) - Mejores prácticas para la gestión de tokens
- [Cifrado End-to-End para IA](https://learn.microsoft.com/azure/architecture/example-scenario/confidential/end-to-end-encryption) - Patrones avanzados de cifrado

### Recursos Avanzados de Seguridad
- [Ciclo de Vida de Desarrollo de Seguridad Microsoft](https://www.microsoft.com/sdl) - Prácticas de desarrollo seguro
- [Guía Red Team de IA](https://learn.microsoft.com/security/ai-red-team/) - Pruebas de seguridad específicas de IA
- [Modelado de Amenazas para Sistemas de IA](https://learn.microsoft.com/security/adoption/approach/threats-ai) - Metodología de modelado de amenazas para IA
- [Ingeniería de Privacidad para IA](https://www.microsoft.com/security/blog/2021/07/13/microsofts-pet-project-privacy-enhancing-technologies-in-action/) - Técnicas de IA que preservan la privacidad

### Cumplimiento y Gobernanza
- [Cumplimiento GDPR para IA](https://learn.microsoft.com/compliance/regulatory/gdpr-data-protection-impact-assessments) - Cumplimiento de privacidad en sistemas de IA
- [Marco de Gobernanza AI](https://learn.microsoft.com/azure/architecture/guide/responsible-ai/responsible-ai-overview) - Implementación responsable de IA
- [SOC 2 para Servicios de IA](https://learn.microsoft.com/compliance/regulatory/offering-soc) - Controles de seguridad para proveedores de servicios de IA
- [Cumplimiento HIPAA para IA](https://learn.microsoft.com/compliance/regulatory/offering-hipaa-hitech) - Requisitos de cumplimiento sanitario para IA

### DevSecOps y Automatización
- [Pipeline DevSecOps para IA](https://learn.microsoft.com/azure/devops/migrate/security-validation-cicd-pipeline) - Pipelines seguros para desarrollo de IA
- [Pruebas de Seguridad Automatizadas](https://learn.microsoft.com/security/engineering/devsecops) - Validación continua de seguridad
- [Seguridad en Infraestructura como Código](https://learn.microsoft.com/security/engineering/infrastructure-security) - Despliegue seguro de infraestructura
- [Seguridad de Contenedores para IA](https://learn.microsoft.com/azure/container-instances/container-instances-image-security) - Seguridad en la contenedorización de cargas de trabajo IA

### Monitoreo y Respuesta a Incidentes  
- [Azure Monitor para cargas de trabajo IA](https://learn.microsoft.com/azure/azure-monitor/overview) - Soluciones integrales de monitoreo
- [Respuesta a Incidentes de Seguridad IA](https://learn.microsoft.com/security/compass/incident-response-playbooks) - Procedimientos específicos para incidentes de IA
- [SIEM para Sistemas de IA](https://learn.microsoft.com/azure/sentinel/overview) - Gestión de información y eventos de seguridad

- [Inteligencia de Amenazas para IA](https://learn.microsoft.com/security/compass/security-operations-videos-and-decks#threat-intelligence) - Fuentes de inteligencia sobre amenazas de IA

## 🔄 Mejora Continua

### Mantenerse Actualizado con los Estándares en Evolución
- **Actualizaciones de Especificaciones MCP**: Monitorear cambios oficiales en las especificaciones MCP y avisos de seguridad
- **Inteligencia de Amenazas**: Suscribirse a fuentes de amenazas de seguridad de IA y bases de datos de vulnerabilidades  
- **Participación Comunitaria**: Participar en discusiones y grupos de trabajo de la comunidad de seguridad MCP
- **Evaluación Regular**: Realizar evaluaciones trimestrales de la postura de seguridad y actualizar las prácticas en consecuencia

### Contribuyendo a la Seguridad MCP
- **Investigación en Seguridad**: Contribuir a la investigación en seguridad MCP y programas de divulgación de vulnerabilidades
- **Compartir Mejores Prácticas**: Compartir implementaciones de seguridad y lecciones aprendidas con la comunidad
- **Desarrollo de Estándares**: Participar en el desarrollo de especificaciones MCP y creación de estándares de seguridad
- **Desarrollo de Herramientas**: Desarrollar y compartir herramientas y bibliotecas de seguridad para el ecosistema MCP

---

*Este documento refleja las mejores prácticas de seguridad MCP al 9 de septiembre de 2026,
basado en la Especificación MCP `2026-07-28`. Las prácticas de seguridad deben ser revisadas regularmente
a medida que el protocolo y el panorama de amenazas evolucionan.*

## Qué Sigue

- Leer: [Mejores Prácticas de Seguridad MCP](./mcp-security-best-practices.md)
- Volver a: [Resumen del Módulo de Seguridad](./README.md)
- Continuar a: [Módulo 3: Primeros Pasos](../03-GettingStarted/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Descargo de responsabilidad**:
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional humana. No somos responsables de cualquier malentendido o interpretación errónea que surja del uso de esta traducción.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->