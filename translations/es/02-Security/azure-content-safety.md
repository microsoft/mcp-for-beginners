# Seguridad avanzada de MCP con Azure Content Safety

Azure Content Safety ofrece varias herramientas potentes que pueden mejorar la seguridad de tus implementaciones de MCP:

## Prompt Shields

Los AI Prompt Shields de Microsoft brindan una protección sólida contra ataques de inyección de prompts tanto directos como indirectos mediante:

1. **Detección avanzada**: Utiliza aprendizaje automático para identificar instrucciones maliciosas ocultas en el contenido.
2. **Resaltado**: Transforma el texto de entrada para ayudar a los sistemas de IA a distinguir entre instrucciones válidas y entradas externas.
3. **Delimitadores y marcado de datos**: Señala los límites entre datos confiables y no confiables.
4. **Integración con Content Safety**: Funciona con Azure AI Content Safety para detectar intentos de jailbreak y contenido dañino.
5. **Actualizaciones continuas**: Microsoft actualiza regularmente los mecanismos de protección contra nuevas amenazas.

## Implementación de Azure Content Safety con MCP

Este enfoque ofrece una protección en múltiples capas:
- Escaneo de entradas antes de procesarlas
- Validación de salidas antes de devolverlas
- Uso de listas negras para patrones dañinos conocidos
- Aprovechamiento de los modelos de seguridad de contenido de Azure, que se actualizan continuamente

## Recursos de Azure Content Safety

Para aprender más sobre cómo implementar Azure Content Safety con tus servidores MCP, consulta estos recursos oficiales:

1. [Azure AI Content Safety Documentation](https://learn.microsoft.com/azure/ai-services/content-safety/) - Documentación oficial de Azure Content Safety.
2. [Prompt Shield Documentation](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/prompt-shield) - Aprende cómo prevenir ataques de inyección de prompts.
3. [Content Safety API Reference](https://learn.microsoft.com/rest/api/contentsafety/) - Referencia detallada de la API para implementar Content Safety.
4. [Quickstart: Azure Content Safety with C#](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-csharp) - Guía rápida de implementación usando C#.
5. [Content Safety Client Libraries](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-client-libraries-rest-api) - Bibliotecas cliente para varios lenguajes de programación.
6. [Detecting Jailbreak Attempts](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection) - Guía específica para detectar y prevenir intentos de jailbreak.
7. [Best Practices for Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/best-practices) - Mejores prácticas para implementar la seguridad de contenido de forma efectiva.

Para una implementación más detallada, consulta nuestra [guía de implementación de Azure Content Safety](./azure-content-safety-implementation.md).

**Aviso legal**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o interpretaciones erróneas derivadas del uso de esta traducción.