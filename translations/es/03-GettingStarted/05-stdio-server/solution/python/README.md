# Servidor MCP stdio - Solución en Python

> **⚠️ Importante**: Esta solución ha sido actualizada para usar el **transporte stdio** según lo recomendado por la Especificación MCP 2025-06-18. El transporte SSE original ha sido descontinuado.

## Descripción general

Esta solución en Python demuestra cómo construir un servidor MCP utilizando el transporte stdio actual. El transporte stdio es más simple, más seguro y ofrece un mejor rendimiento que el enfoque SSE descontinuado.

## Requisitos previos

- Python 3.8 o posterior
- Se recomienda instalar `uv` para la gestión de paquetes, consulta [instrucciones](https://docs.astral.sh/uv/#highlights)

## Instrucciones de configuración

### Paso 1: Crear un entorno virtual

```bash
python -m venv venv
```

### Paso 2: Activar el entorno virtual

**Windows:**
```bash
venv\Scripts\activate
```

**macOS/Linux:**
```bash
source venv/bin/activate
```

### Paso 3: Instalar las dependencias

```bash
pip install mcp
```

## Ejecutar el servidor

El servidor stdio funciona de manera diferente al antiguo servidor SSE. En lugar de iniciar un servidor web, se comunica a través de stdin/stdout:

```bash
python server.py
```

**Importante**: El servidor parecerá estar bloqueado - ¡esto es normal! Está esperando mensajes JSON-RPC desde stdin.

## Probar el servidor

### Método 1: Usar el Inspector MCP (Recomendado)

```bash
npx @modelcontextprotocol/inspector python server.py
```

Esto hará lo siguiente:
1. Iniciar tu servidor como un subproceso
2. Abrir una interfaz web para pruebas
3. Permitir probar todas las herramientas del servidor de manera interactiva

### Método 2: Pruebas directas con JSON-RPC

También puedes probar enviando mensajes JSON-RPC directamente:

1. Inicia el servidor: `python server.py`
2. Envía un mensaje JSON-RPC (ejemplo):

```json
{"jsonrpc": "2.0", "id": 1, "method": "tools/list"}
```

3. El servidor responderá con las herramientas disponibles

### Herramientas disponibles

El servidor proporciona estas herramientas:

- **add(a, b)**: Suma dos números
- **multiply(a, b)**: Multiplica dos números  
- **get_greeting(name)**: Genera un saludo personalizado
- **get_server_info()**: Obtiene información sobre el servidor

### Probar con Claude Desktop

Para usar este servidor con Claude Desktop, agrega esta configuración a tu archivo `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "example-stdio-server": {
      "command": "python",
      "args": ["path/to/server.py"]
    }
  }
}
```

## Diferencias clave con SSE

**Transporte stdio (Actual):**
- ✅ Configuración más simple - no se necesita servidor web
- ✅ Mejor seguridad - sin puntos de acceso HTTP
- ✅ Comunicación basada en subprocesos
- ✅ JSON-RPC a través de stdin/stdout
- ✅ Mejor rendimiento

**Transporte SSE (Descontinuado):**
- ❌ Requería configuración de servidor HTTP
- ❌ Necesitaba un marco web (Starlette/FastAPI)
- ❌ Gestión de rutas y sesiones más compleja
- ❌ Consideraciones de seguridad adicionales
- ❌ Ahora descontinuado en MCP 2025-06-18

## Consejos para depuración

- Usa `stderr` para registrar logs (nunca `stdout`)
- Prueba con el Inspector para depuración visual
- Asegúrate de que todos los mensajes JSON estén delimitados por saltos de línea
- Verifica que el servidor se inicie sin errores

Esta solución sigue la especificación actual de MCP y demuestra las mejores prácticas para la implementación del transporte stdio.

---

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Si bien nos esforzamos por garantizar la precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o imprecisiones. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o interpretaciones erróneas que puedan surgir del uso de esta traducción.