# Soluciones de Servidor MCP stdio

> **⚠️ Importante**: Estas soluciones han sido actualizadas para usar el **transporte stdio** según lo recomendado por la Especificación MCP 2025-06-18. El transporte original SSE (Server-Sent Events) ha sido descontinuado.

Aquí están las soluciones completas para construir servidores MCP utilizando el transporte stdio en cada entorno de ejecución:

- [TypeScript](../../../../../03-GettingStarted/05-stdio-server/solution/typescript) - Implementación completa de servidor stdio
- [Python](../../../../../03-GettingStarted/05-stdio-server/solution/python) - Servidor stdio en Python con asyncio
- [.NET](../../../../../03-GettingStarted/05-stdio-server/solution/dotnet) - Servidor stdio en .NET con inyección de dependencias

Cada solución demuestra:
- Configuración del transporte stdio
- Definición de herramientas del servidor
- Manejo adecuado de mensajes JSON-RPC
- Integración con clientes MCP como Claude

Todas las soluciones siguen la especificación actual de MCP y utilizan el transporte stdio recomendado para un rendimiento y seguridad óptimos.

---

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Si bien nos esforzamos por garantizar la precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o imprecisiones. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o interpretaciones erróneas que puedan surgir del uso de esta traducción.