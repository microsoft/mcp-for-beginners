# Temas Avanzados en MCP

[![MCP Avanzado: Agentes de IA seguros, escalables y multimodales](../../../translated_images/es/06.42259eaf91fccfc6.webp)](https://youtu.be/4yjmGvJzYdY)

_(Haz clic en la imagen arriba para ver el video de esta lección)_

Este capítulo cubre una serie de temas avanzados en la implementación del Protocolo de Contexto del Modelo (MCP), incluyendo la integración multimodal, la escalabilidad, las mejores prácticas de seguridad y la integración empresarial. Estos temas son cruciales para construir aplicaciones MCP robustas y listas para producción que puedan cumplir con las demandas de los sistemas modernos de IA.

## Visión general

Esta lección explora conceptos avanzados en la implementación del Protocolo de Contexto del Modelo, enfocándose en la integración multimodal, la escalabilidad, las mejores prácticas de seguridad y la integración empresarial. Estos temas son esenciales para construir aplicaciones MCP de nivel de producción que puedan manejar requisitos complejos en entornos empresariales.

## Objetivos de aprendizaje

Al final de esta lección, podrás:

- Implementar capacidades multimodales dentro de los marcos MCP
- Diseñar arquitecturas MCP escalables para escenarios de alta demanda
- Aplicar las mejores prácticas de seguridad alineadas con los principios de seguridad de MCP
- Integrar MCP con sistemas y marcos de IA empresariales
- Optimizar el rendimiento y la confiabilidad en entornos de producción

## Lecciones y proyectos de ejemplo

| Enlace | Título | Descripción |
|------|-------|-------------|
| [5.1 Integración con Azure](./mcp-integration/README.md) | Integrarse con Azure | Aprende cómo integrar tu Servidor MCP en Azure |
| [5.2 Ejemplo multimodal](./mcp-multi-modality/README.md) | Ejemplos multimodales MCP | Ejemplos para audio, imagen y respuesta multimodal |
| [5.3 Ejemplo MCP OAuth2](../../../05-AdvancedTopics/mcp-oauth2-demo) | Demostración MCP OAuth2 | Aplicación mínima Spring Boot que muestra OAuth2 con MCP, tanto como Servidor de Autorización como de Recursos. Demuestra emisión segura de tokens, endpoints protegidos, despliegue en Azure Container Apps e integración con API Management. |
| [5.4 Contextos raíz](./mcp-root-contexts/README.md) | Contextos raíz | Aprende más sobre contextos raíz y cómo implementarlos |
| [5.5 Enrutamiento](./mcp-routing/README.md) | Enrutamiento | Aprende diferentes tipos de enrutamiento |
| [5.6 Muestreo](./mcp-sampling/README.md) | Muestreo | Aprende a trabajar con muestreos |
| [5.7 Escalado](./mcp-scaling/README.md) | Escalado | Aprende sobre escalado |
| [5.8 Seguridad](./mcp-security/README.md) | Seguridad | Asegura tu Servidor MCP |
| [5.9 Ejemplo de búsqueda web](./web-search-mcp/README.md) | Búsqueda web MCP | Servidor y cliente MCP en Python integrando SerpAPI para búsqueda en tiempo real web, noticias, productos y preguntas y respuestas. Demuestra orquestación multi-herramientas, integración con API externas y manejo robusto de errores. |
| [5.10 Transmisión en tiempo real](./mcp-realtimestreaming/README.md) | Transmisión | La transmisión de datos en tiempo real se ha vuelto esencial en el mundo actual impulsado por datos, donde empresas y aplicaciones requieren acceso inmediato a información para tomar decisiones oportunas. |
| [5.11 Búsqueda web en tiempo real](./mcp-realtimesearch/README.md) | Búsqueda web | Cómo MCP transforma la búsqueda web en tiempo real proporcionando un enfoque estandarizado para la gestión de contexto entre modelos de IA, motores de búsqueda y aplicaciones. |
| [5.12 Autenticación Entra ID para Servidores de Protocolo de Contexto del Modelo](./mcp-security-entra/README.md) | Autenticación Entra ID | Microsoft Entra ID ofrece una solución robusta en la nube para la gestión de identidad y acceso, ayudando a asegurar que solo usuarios y aplicaciones autorizados puedan interactuar con tu servidor MCP. |
| [5.13 Integración de Agentes Azure AI Foundry](./mcp-foundry-agent-integration/README.md) | Integración Azure AI Foundry | Aprende cómo integrar servidores de Protocolo de Contexto del Modelo con agentes de Azure AI Foundry, habilitando una orquestación potente de herramientas y capacidades de IA empresariales con conexiones estandarizadas a fuentes de datos externas. |
| [5.14 Ingeniería de Contexto](./mcp-contextengineering/README.md) | Ingeniería de Contexto | La oportunidad futura de técnicas de ingeniería de contexto para servidores MCP, incluyendo optimización de contexto, gestión dinámica de contexto y estrategias para ingeniería efectiva de prompts dentro de marcos MCP. |
| [5.15 Transporte personalizado MCP](./mcp-transport/README.md) | Transporte personalizado | Aprende cómo implementar mecanismos de transporte personalizados para escenarios especializados de comunicación MCP. |
| [5.16 Profundización en características del protocolo](./mcp-protocol-features/README.md) | Características del protocolo | Domina características avanzadas del protocolo incluyendo notificaciones de progreso, cancelación de solicitudes, plantillas de recursos y patrones de manejo de errores. |
| [5.17 Razonamiento multi-agente adversarial](./mcp-adversarial-agents/README.md) | Agentes adversariales | Usa dos agentes con posiciones opuestas, compartiendo un conjunto de herramientas MCP, para detectar alucinaciones, exponer casos límite y producir salidas mejor calibradas mediante debate estructurado. |

> **Nuevo en la especificación MCP 2025-11-25**: La especificación ahora incluye soporte experimental para **Tareas** (operaciones de larga duración con seguimiento de progreso), **Anotaciones de Herramientas** (metadatos sobre el comportamiento de la herramienta para seguridad), **Elicitación en modo URL** (solicitud de contenido URL específico a los clientes) y **Raíces** mejoradas (para la gestión de contexto del espacio de trabajo). Consulta el [registro de cambios de la especificación MCP](https://spec.modelcontextprotocol.io/) para detalles completos.

## Referencias adicionales

Para la información más actualizada sobre temas avanzados de MCP, consulta:
- [Documentación MCP](https://modelcontextprotocol.io/)
- [Especificación MCP (2025-11-25)](https://spec.modelcontextprotocol.io/specification/2025-11-25/)
- [Repositorio GitHub](https://github.com/modelcontextprotocol)
- [OWASP MCP Top 10](https://microsoft.github.io/mcp-azure-security-guide/mcp/) - Riesgos de seguridad y mitigaciones
- [Taller MCP Security Summit (Sherpa)](https://azure-samples.github.io/sherpa/) - Entrenamiento práctico de seguridad

## Conclusiones clave

- Las implementaciones multimodales MCP extienden las capacidades de IA más allá del procesamiento de texto
- La escalabilidad es esencial para despliegues empresariales y puede abordarse mediante escalado horizontal y vertical
- Medidas de seguridad integrales protegen datos y aseguran el control adecuado de acceso
- La integración empresarial con plataformas como Azure OpenAI y Microsoft AI Foundry mejora las capacidades MCP
- Las implementaciones avanzadas MCP se benefician de arquitecturas optimizadas y una gestión cuidadosa de recursos

## Ejercicio

Diseña una implementación MCP de nivel empresarial para un caso de uso específico:

1. Identifica los requisitos multimodales para tu caso de uso
2. Esboza los controles de seguridad necesarios para proteger datos sensibles
3. Diseña una arquitectura escalable que pueda manejar cargas variables
4. Planifica puntos de integración con sistemas de IA empresariales
5. Documenta posibles cuellos de botella de rendimiento y estrategias de mitigación

## Recursos adicionales

- [Documentación Azure OpenAI](https://learn.microsoft.com/en-us/azure/ai-services/openai/)
- [Documentación Microsoft AI Foundry](https://learn.microsoft.com/en-us/ai-services/)

---

## Qué sigue

Explora las lecciones de este módulo comenzando con: [5.1 Integración MCP](./mcp-integration/README.md)

Una vez completes este módulo, continúa con: [Módulo 6: Contribuciones de la comunidad](../06-CommunityContributions/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por humanos. No nos hacemos responsables de ningún malentendido o interpretación errónea derivada del uso de esta traducción.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->