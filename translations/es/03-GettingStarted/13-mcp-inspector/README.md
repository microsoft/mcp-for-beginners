# Depuración con MCP Inspector

> [!NOTE]
> Los comandos que usan `--sse` y las URLs que terminan en `/sse` prueban el transporte heredado HTTP+SSE.
> Para un servidor MCP `2026-07-28` nuevo, use una versión de Inspector que
> soporte HTTP Streamable y seleccione ese transporte en su lugar.

El **MCP Inspector** es una herramienta esencial de depuración que le permite probar y solucionar problemas interactivamente en sus servidores MCP sin necesidad de una aplicación anfitriona completa de IA. Piénselo como el "Postman para MCP"; proporciona una interfaz visual para enviar solicitudes, ver respuestas y comprender cómo se comporta su servidor.

## ¿Por qué usar MCP Inspector?

Al construir servidores MCP, a menudo enfrentará estos desafíos:

- **"¿Mi servidor está funcionando?"** - Inspector muestra el estado de la conexión
- **"¿Mis herramientas están registradas correctamente?"** - Inspector lista todas las herramientas disponibles
- **"¿Cuál es el formato de respuesta?"** - Inspector muestra respuestas JSON completas
- **"¿Por qué no funciona esta herramienta?"** - Inspector muestra mensajes de error detallados

## Requisitos previos

- Node.js 18+ instalado
- npm (incluido con Node.js)
- Un servidor MCP para probar (ver [Módulo 3.1 - Primer Servidor](../01-first-server/README.md))

## Instalación

### Opción 1: Ejecutar con npx (Recomendado para pruebas rápidas)

```bash
npx @modelcontextprotocol/inspector
```

### Opción 2: Instalar globalmente

```bash
npm install -g @modelcontextprotocol/inspector
mcp-inspector
```

### Opción 3: Añadir a su proyecto

```bash
cd your-mcp-server-project
npm install --save-dev @modelcontextprotocol/inspector
```

Añada a `package.json`:
```json
{
  "scripts": {
    "inspector": "mcp-inspector"
  }
}
```

---

## Conexión a su servidor

### Servidores stdio (Proceso local)

Para servidores que se comunican mediante entrada/salida estándar:

```bash
# Servidor Python
npx @modelcontextprotocol/inspector python -m your_server_module

# Servidor Node.js
npx @modelcontextprotocol/inspector node ./build/index.js

# Con variables de entorno
OPENAI_API_KEY=xxx npx @modelcontextprotocol/inspector python server.py
```

### Servidores SSE/HTTP (Red)

Para servidores que funcionan como servicios HTTP:

1. Inicie su servidor primero:
   ```bash
   python server.py  # Servidor ejecutándose en http://localhost:8080
   ```

2. Lance Inspector y conéctese:
   ```bash
   npx @modelcontextprotocol/inspector --sse http://localhost:8080/sse
   ```

---

## Vista general de la interfaz de Inspector

Al iniciar Inspector, verá una interfaz web (normalmente en `http://localhost:5173`):

```
┌─────────────────────────────────────────────────────────────┐
│  MCP Inspector                              [Connected ✅]   │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐         │
│  │   🔧 Tools  │  │ 📄 Resources│  │ 💬 Prompts  │         │
│  │    (3)      │  │    (2)      │  │    (1)      │         │
│  └─────────────┘  └─────────────┘  └─────────────┘         │
│                                                             │
│  ┌───────────────────────────────────────────────────────┐ │
│  │  📋 Message Log                                       │ │
│  │  ─────────────────────────────────────────────────── │ │
│  │  → initialize                                         │ │
│  │  ← initialized (server info)                          │ │
│  │  → tools/list                                         │ │
│  │  ← tools (3 tools)                                    │ │
│  └───────────────────────────────────────────────────────┘ │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## Prueba de herramientas

### Listar herramientas disponibles

1. Haga clic en la pestaña **Tools**
2. Inspector llamará automáticamente a `tools/list`
3. Verá todas las herramientas registradas con:
   - Nombre de la herramienta
   - Descripción
   - Esquema de entrada (parámetros)

### Invocar una herramienta

1. Seleccione una herramienta de la lista
2. Rellene los parámetros requeridos en el formulario
3. Haga clic en **Run Tool**
4. Vea la respuesta en el panel de resultados

**Ejemplo: Probando una herramienta de calculadora**

```
Tool: add
Parameters:
  a: 25
  b: 17

Response:
{
  "content": [
    {
      "type": "text",
      "text": "42"
    }
  ]
}
```

### Depuración de errores de herramientas

Cuando una herramienta falla, Inspector muestra:

```
Error Response:
{
  "error": {
    "code": -32602,
    "message": "Invalid params: 'b' is required"
  }
}
```

Códigos de error comunes:
| Código | Significado |
|------|------------|
| -32700 | Error de análisis (JSON inválido) |
| -32600 | Solicitud inválida |
| -32601 | Método no encontrado |
| -32602 | Parámetros inválidos |
| -32603 | Error interno |

---

## Prueba de recursos

### Listar recursos

1. Haga clic en la pestaña **Resources**
2. Inspector llama a `resources/list`
3. Verá:
   - URI de recursos
   - Nombres y descripciones
   - Tipos MIME

### Leer un recurso

1. Seleccione un recurso
2. Haga clic en **Read Resource**
3. Vea el contenido devuelto

**Ejemplo de salida:**

```
Resource: file:///config/settings.json
Content-Type: application/json

{
  "config": {
    "debug": true,
    "maxConnections": 10
  }
}
```

---

## Prueba de prompts

### Listar prompts

1. Haga clic en la pestaña **Prompts**
2. Inspector llama a `prompts/list`
3. Vea las plantillas de prompt disponibles

### Obtener un prompt

1. Seleccione un prompt
2. Rellene los argumentos requeridos
3. Haga clic en **Get Prompt**
4. Vea los mensajes del prompt renderizados

---

## Análisis del registro de mensajes

El registro de mensajes muestra todos los mensajes del protocolo MCP. La transcripción a continuación es de un
servidor legado `2025-11-25` e incluye el handshake `initialize` eliminado. Un
servidor `2026-07-28` usa metadatos de solicitud autónomos y `server/discover`
en su lugar.

```
14:32:01 → {"jsonrpc":"2.0","id":1,"method":"initialize",...}
14:32:01 ← {"jsonrpc":"2.0","id":1,"result":{"protocolVersion":"2025-11-25",...}}
14:32:02 → {"jsonrpc":"2.0","id":2,"method":"tools/list"}
14:32:02 ← {"jsonrpc":"2.0","id":2,"result":{"tools":[...]}}
14:32:05 → {"jsonrpc":"2.0","id":3,"method":"tools/call","params":{"name":"add",...}}
14:32:05 ← {"jsonrpc":"2.0","id":3,"result":{"content":[...]}}
```

### Qué buscar

- **Pares solicitud/respuesta**: Cada `→` debe tener un `←` correspondiente
- **Mensajes de error**: Busque `"error"` en las respuestas
- **Temporización**: Grandes intervalos pueden indicar problemas de rendimiento
- **Versión del protocolo**: Asegúrese de que servidor y cliente coincidan en versión

---

## Integración con VS Code

Puede ejecutar Inspector directamente desde VS Code:

### Usando launch.json

Añada a `.vscode/launch.json`:

```json
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "Debug with MCP Inspector",
      "type": "node",
      "request": "launch",
      "runtimeExecutable": "npx",
      "runtimeArgs": [
        "@modelcontextprotocol/inspector",
        "python",
        "${workspaceFolder}/server.py"
      ],
      "console": "integratedTerminal"
    },
    {
      "name": "Debug SSE Server with Inspector",
      "type": "chrome",
      "request": "launch",
      "url": "http://localhost:5173",
      "preLaunchTask": "Start MCP Inspector"
    }
  ]
}
```

### Usando Tasks

Añada a `.vscode/tasks.json`:

```json
{
  "version": "2.0.0",
  "tasks": [
    {
      "label": "Start MCP Inspector",
      "type": "shell",
      "command": "npx @modelcontextprotocol/inspector node ${workspaceFolder}/build/index.js",
      "isBackground": true,
      "problemMatcher": {
        "pattern": {
          "regexp": "^$"
        },
        "background": {
          "activeOnStart": true,
          "beginsPattern": "Inspector",
          "endsPattern": "listening"
        }
      }
    }
  ]
}
```

---

## Escenarios comunes de depuración

### Escenario 1: El servidor no se conecta

**Síntomas:** Inspector muestra "Disconnected" o se queda en "Connecting..."

**Checklist:**
1. ✅ ¿El comando para el servidor es correcto?
2. ✅ ¿Están todas las dependencias instaladas?
3. ✅ ¿La ruta del servidor es absoluta o relativa al directorio actual?
4. ✅ ¿Están definidas las variables de entorno requeridas?

**Pasos de depuración:**
```bash
# Probar el servidor manualmente primero
python -c "import your_server_module; print('OK')"

# Comprobar si hay errores de importación
python -m your_server_module 2>&1 | head -20

# Verificar que el SDK de MCP esté instalado
pip show mcp
```

### Escenario 2: Las herramientas no aparecen

**Síntomas:** La pestaña de herramientas muestra una lista vacía

**Posibles causas:**
1. Herramientas no registradas durante la inicialización del servidor
2. Servidor se bloqueó después del inicio
3. Manejador `tools/list` devuelve un arreglo vacío

**Pasos de depuración:**
1. Revise el registro de mensajes para la respuesta `tools/list`
2. Añada registros (logging) en el código de registro de herramientas
3. Verifique que están presentes los decoradores `@mcp.tool()` (Python)

### Escenario 3: La herramienta devuelve error

**Síntomas:** La llamada a la herramienta devuelve respuesta con error

**Enfoque para depurar:**
1. Lea el mensaje de error cuidadosamente
2. Verifique que los tipos de los parámetros coincidan con el esquema
3. Añada try/catch con mensajes de error detallados
4. Revise los registros del servidor para rastros de pila

**Ejemplo de manejo de errores mejorado:**

```python
@mcp.tool()
async def my_tool(param1: str, param2: int) -> str:
    try:
        # Lógica de la herramienta aquí
        result = process(param1, param2)
        return str(result)
    except ValueError as e:
        raise McpError(f"Invalid parameter: {e}")
    except Exception as e:
        raise McpError(f"Tool failed: {type(e).__name__}: {e}")
```

### Escenario 4: Contenido del recurso vacío

**Síntomas:** El recurso responde pero el contenido está vacío o es nulo

**Checklist:**
1. ✅ La ruta del archivo o URI es correcta
2. ✅ El servidor tiene permiso para leer el recurso
3. ✅ El contenido del recurso se está devolviendo correctamente

---

## Funciones avanzadas de Inspector

### Cabeceras personalizadas (SSE)

```bash
npx @modelcontextprotocol/inspector \
  --sse http://localhost:8080/sse \
  --header "Authorization: Bearer your-token"
```

### Registro detallado (Verbose Logging)

```bash
DEBUG=mcp* npx @modelcontextprotocol/inspector python server.py
```

### Grabación de sesiones

Inspector puede exportar registros de mensajes para análisis posteriores:
1. Haga clic en **Export Log** en el panel de mensajes
2. Guarde el archivo JSON
3. Compártalo con miembros del equipo para depuración

---

## Mejores prácticas

1. **Pruebe temprano y a menudo** – Use Inspector durante el desarrollo, no solo cuando algo falla
2. **Empiece simple** – Pruebe conectividad básica antes de llamadas complejas a herramientas
3. **Revise el esquema** – Muchos errores provienen de incompatibilidades en tipos de parámetros
4. **Lea los mensajes de error** – Los errores MCP suelen ser descriptivos
5. **Mantenga Inspector abierto** – Ayuda a detectar problemas mientras desarrolla

---

## Qué sigue

Ha completado el Módulo 3: ¡Primeros pasos! Continúe su aprendizaje:

- [Módulo 4: Implementación práctica](../../04-PracticalImplementation/README.md)

---

## Recursos adicionales

- [Repositorio GitHub de MCP Inspector](https://github.com/modelcontextprotocol/inspector)
- [Especificación MCP - Mensajes de protocolo](https://modelcontextprotocol.io/specification/2026-07-28/)
- [Especificación JSON-RPC 2.0](https://www.jsonrpc.org/specification)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Descargo de responsabilidad**:
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional humana. No somos responsables de cualquier malentendido o interpretación errónea que surja del uso de esta traducción.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->