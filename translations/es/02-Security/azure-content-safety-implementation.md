# Implementación de Azure Content Safety con MCP

Para fortalecer la seguridad de MCP contra la inyección de prompts, el envenenamiento de herramientas y otras vulnerabilidades específicas de IA, se recomienda encarecidamente integrar Azure Content Safety.

## Integración con el servidor MCP

Para integrar Azure Content Safety con tu servidor MCP, añade el filtro de seguridad de contenido como middleware en tu pipeline de procesamiento de solicitudes:

1. Inicializa el filtro durante el arranque del servidor  
2. Valida todas las solicitudes entrantes de herramientas antes de procesarlas  
3. Revisa todas las respuestas salientes antes de devolverlas a los clientes  
4. Registra y alerta sobre violaciones de seguridad  
5. Implementa un manejo adecuado de errores para las comprobaciones fallidas de seguridad de contenido  

Esto proporciona una defensa sólida contra:  
- Ataques de inyección de prompts  
- Intentos de envenenamiento de herramientas  
- Exfiltración de datos mediante entradas maliciosas  
- Generación de contenido dañino  

## Mejores prácticas para la integración de Azure Content Safety

1. **Listas de bloqueo personalizadas**: Crea listas de bloqueo específicas para patrones de inyección en MCP  
2. **Ajuste de severidad**: Modifica los umbrales de severidad según tu caso de uso y tolerancia al riesgo  
3. **Cobertura integral**: Aplica las comprobaciones de seguridad de contenido a todas las entradas y salidas  
4. **Optimización del rendimiento**: Considera implementar caché para las comprobaciones repetidas de seguridad de contenido  
5. **Mecanismos de respaldo**: Define comportamientos claros de respaldo cuando los servicios de seguridad de contenido no estén disponibles  
6. **Retroalimentación al usuario**: Proporciona una retroalimentación clara a los usuarios cuando el contenido sea bloqueado por motivos de seguridad  
7. **Mejora continua**: Actualiza regularmente las listas de bloqueo y patrones basándote en amenazas emergentes

**Aviso legal**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda la traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o interpretaciones erróneas derivadas del uso de esta traducción.