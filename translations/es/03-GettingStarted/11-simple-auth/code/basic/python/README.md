# Ejecutar ejemplo

Este ejemplo inicia un servidor MCP con un middleware que verifica si el encabezado de autorización es válido.

## Instalar dependencias

```bash
pip install "mcp[cli]" 
```

## Iniciar servidor

```bash
python server.py
```

inicia el cliente en otra terminal

```bash
python client.py
```

Deberías ver un resultado similar a:

```text
2025-09-30 13:25:54 - mcp_client - INFO - Tool result: meta=None content=[TextContent(type='text', text='{\n  "current_time": "2025-09-30T13:25:54.311900",\n  "timezone": "UTC",\n  "timestamp": 1759238754.3119,\n  "formatted": "2025-09-30 13:25:54"\n}', annotations=None, meta=None)] structuredContent={'current_time': '2025-09-30T13:25:54.311900', 'timezone': 'UTC', 'timestamp': 1759238754.3119, 'formatted': '2025-09-30 13:25:54'} isError=False
```

esto significa que la credencial enviada está siendo aceptada.

Intenta cambiar la credencial en `client.py` a "secret-token2", entonces deberías ver este texto como parte de la respuesta:

```text
2025-09-30 13:27:44 - httpx - INFO - HTTP Request: POST http://localhost:8000/mcp "HTTP/1.1 403 Forbidden"
```

esto significa que fuiste autenticado (tenías una credencial), pero era inválida.

---

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por lograr precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o imprecisiones. El documento original en su idioma nativo debe considerarse como la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o interpretaciones erróneas que puedan surgir del uso de esta traducción.