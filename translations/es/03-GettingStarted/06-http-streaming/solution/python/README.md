# Ejecutar este ejemplo

Aquí te mostramos cómo ejecutar el servidor y cliente de streaming HTTP clásico, así como el servidor y cliente de streaming MCP utilizando Python.

### Descripción general

- Configurarás un servidor MCP que envía notificaciones de progreso al cliente mientras procesa elementos.
- El cliente mostrará cada notificación en tiempo real.
- Esta guía cubre los requisitos previos, la configuración, la ejecución y la resolución de problemas.

### Requisitos previos

- Python 3.9 o superior
- El paquete de Python `mcp` (instálalo con `pip install mcp`)

### Instalación y configuración

1. Clona el repositorio o descarga los archivos de la solución.

   ```pwsh
   git clone https://github.com/microsoft/mcp-for-beginners
   ```

1. **Crea y activa un entorno virtual (recomendado):**

   ```pwsh
   python -m venv venv
   .\venv\Scripts\Activate.ps1  # On Windows
   # or
   source venv/bin/activate      # On Linux/macOS
   ```

1. **Instala las dependencias necesarias:**

   ```pwsh
   pip install "mcp[cli]" fastapi requests
   ```

### Archivos

- **Servidor:** [server.py](../../../../../../03-GettingStarted/06-http-streaming/solution/python/server.py)
- **Cliente:** [client.py](../../../../../../03-GettingStarted/06-http-streaming/solution/python/client.py)

### Ejecutar el servidor de streaming HTTP clásico

1. Navega al directorio de la solución:

   ```pwsh
   cd 03-GettingStarted/06-http-streaming/solution
   ```

2. Inicia el servidor de streaming HTTP clásico:

   ```pwsh
   python server.py
   ```

3. El servidor se iniciará y mostrará:

   ```
   Starting FastAPI server for classic HTTP streaming...
   INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
   ```

### Ejecutar el cliente de streaming HTTP clásico

1. Abre una nueva terminal (activa el mismo entorno virtual y directorio):

   ```pwsh
   cd 03-GettingStarted/06-http-streaming/solution
   python client.py
   ```

2. Deberías ver los mensajes transmitidos impresos secuencialmente:

   ```text
   Running classic HTTP streaming client...
   Connecting to http://localhost:8000/stream with message: hello
   --- Streaming Progress ---
   Processing file 1/3...
   Processing file 2/3...
   Processing file 3/3...
   Here's the file content: hello
   --- Stream Ended ---
   ```

### Ejecutar el servidor de streaming MCP

1. Navega al directorio de la solución:
   ```pwsh
   cd 03-GettingStarted/06-http-streaming/solution
   ```
2. Inicia el servidor MCP con el transporte streamable-http:
   ```pwsh
   python server.py mcp
   ```
3. El servidor se iniciará y mostrará:
   ```
   Starting MCP server with streamable-http transport...
   INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
   ```

### Ejecutar el cliente de streaming MCP

1. Abre una nueva terminal (activa el mismo entorno virtual y directorio):
   ```pwsh
   cd 03-GettingStarted/06-http-streaming/solution
   python client.py mcp
   ```
2. Deberías ver las notificaciones impresas en tiempo real a medida que el servidor procesa cada elemento:
   ```
   Running MCP client...
   Starting client...
   Session ID before init: None
   Session ID after init: a30ab7fca9c84f5fa8f5c54fe56c9612
   Session initialized, ready to call tools.
   Received message: root=LoggingMessageNotification(...)
   NOTIFICATION: root=LoggingMessageNotification(...)
   ...
   Tool result: meta=None content=[TextContent(type='text', text='Processed files: file_1.txt, file_2.txt, file_3.txt | Message: hello from client')]
   ```

### Pasos clave de implementación

1. **Crea el servidor MCP utilizando FastMCP.**
2. **Define una herramienta que procese una lista y envíe notificaciones usando `ctx.info()` o `ctx.log()`.**
3. **Ejecuta el servidor con `transport="streamable-http"`.**
4. **Implementa un cliente con un manejador de mensajes para mostrar las notificaciones a medida que llegan.**

### Recorrido por el código
- El servidor utiliza funciones asíncronas y el contexto MCP para enviar actualizaciones de progreso.
- El cliente implementa un manejador de mensajes asíncrono para imprimir notificaciones y el resultado final.

### Consejos y resolución de problemas

- Usa `async/await` para operaciones no bloqueantes.
- Maneja siempre las excepciones tanto en el servidor como en el cliente para mayor robustez.
- Prueba con múltiples clientes para observar actualizaciones en tiempo real.
- Si encuentras errores, verifica tu versión de Python y asegúrate de que todas las dependencias estén instaladas.

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Si bien nos esforzamos por lograr precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o imprecisiones. El documento original en su idioma nativo debe considerarse como la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o interpretaciones erróneas que puedan surgir del uso de esta traducción.