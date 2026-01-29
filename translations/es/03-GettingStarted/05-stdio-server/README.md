# Servidor MCP con transporte stdio

> **⚠️ Actualización Importante**: A partir de la Especificación MCP 2025-06-18, el transporte SSE (Server-Sent Events) independiente ha sido **obsoleto** y reemplazado por el transporte "Streamable HTTP". La especificación actual de MCP define dos mecanismos de transporte principales:
> 1. **stdio** - Entrada/salida estándar (recomendado para servidores locales)
> 2. **Streamable HTTP** - Para servidores remotos que pueden usar SSE internamente
>
> Esta lección se ha actualizado para centrarse en el **transporte stdio**, que es el enfoque recomendado para la mayoría de las implementaciones de servidores MCP.

El transporte stdio permite que los servidores MCP se comuniquen con los clientes a través de flujos de entrada y salida estándar. Este es el mecanismo de transporte más utilizado y recomendado en la especificación actual de MCP, proporcionando una forma simple y eficiente de construir servidores MCP que se integren fácilmente con diversas aplicaciones cliente.

## Descripción general

Esta lección cubre cómo construir y consumir servidores MCP utilizando el transporte stdio.

## Objetivos de aprendizaje

Al final de esta lección, podrás:

- Construir un servidor MCP utilizando el transporte stdio.
- Depurar un servidor MCP utilizando el Inspector.
- Consumir un servidor MCP utilizando Visual Studio Code.
- Comprender los mecanismos de transporte actuales de MCP y por qué se recomienda stdio.

## Transporte stdio - Cómo funciona

El transporte stdio es uno de los dos tipos de transporte compatibles en la especificación actual de MCP (2025-06-18). Así es como funciona:

- **Comunicación simple**: El servidor lee mensajes JSON-RPC desde la entrada estándar (`stdin`) y envía mensajes a la salida estándar (`stdout`).
- **Basado en procesos**: El cliente lanza el servidor MCP como un subproceso.
- **Formato de mensajes**: Los mensajes son solicitudes, notificaciones o respuestas JSON-RPC individuales, delimitados por saltos de línea.
- **Registro**: El servidor PUEDE escribir cadenas UTF-8 en la salida de error estándar (`stderr`) para propósitos de registro.

### Requisitos clave:
- Los mensajes DEBEN estar delimitados por saltos de línea y NO DEBEN contener saltos de línea incrustados.
- El servidor NO DEBE escribir nada en `stdout` que no sea un mensaje MCP válido.
- El cliente NO DEBE escribir nada en el `stdin` del servidor que no sea un mensaje MCP válido.

### TypeScript

```typescript
import { Server } from "@modelcontextprotocol/sdk/server/index.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";

const server = new Server(
  {
    name: "example-server",
    version: "1.0.0",
  },
  {
    capabilities: {
      tools: {},
    },
  }
);
```

En el código anterior:

- Importamos la clase `Server` y `StdioServerTransport` del SDK de MCP.
- Creamos una instancia del servidor con configuración y capacidades básicas.

### Python

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server

# Create server instance
server = Server("example-server")

@server.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

async def main():
    async with stdio_server(server) as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            server.create_initialization_options()
        )

if __name__ == "__main__":
    asyncio.run(main())
```

En el código anterior:

- Creamos una instancia del servidor utilizando el SDK de MCP.
- Definimos herramientas utilizando decoradores.
- Usamos el administrador de contexto stdio_server para manejar el transporte.

### .NET

```csharp
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;
using Microsoft.Extensions.Logging;
using ModelContextProtocol.Server;

var builder = Host.CreateApplicationBuilder(args);

builder.Services
    .AddMcpServer()
    .WithStdioTransport()
    .WithTools<Tools>();

builder.Services.AddLogging(logging => logging.AddConsole());

var app = builder.Build();
await app.RunAsync();
```

La diferencia clave con SSE es que los servidores stdio:

- No requieren configuración de servidor web ni puntos finales HTTP.
- Son lanzados como subprocesos por el cliente.
- Se comunican a través de flujos stdin/stdout.
- Son más simples de implementar y depurar.

## Ejercicio: Crear un servidor stdio

Para crear nuestro servidor, debemos tener en cuenta dos cosas:

- Necesitamos usar un servidor web para exponer puntos finales para la conexión y los mensajes.

## Laboratorio: Crear un servidor MCP stdio simple

En este laboratorio, crearemos un servidor MCP simple utilizando el transporte stdio recomendado. Este servidor expondrá herramientas que los clientes pueden llamar utilizando el Protocolo de Contexto de Modelo estándar.

### Requisitos previos

- Python 3.8 o posterior.
- SDK de MCP para Python: `pip install mcp`.
- Comprensión básica de la programación asíncrona.

Comencemos creando nuestro primer servidor MCP stdio:

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp import types

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Create the server
server = Server("example-stdio-server")

@server.tool()
def calculate_sum(a: int, b: int) -> int:
    """Calculate the sum of two numbers"""
    return a + b

@server.tool() 
def get_greeting(name: str) -> str:
    """Generate a personalized greeting"""
    return f"Hello, {name}! Welcome to MCP stdio server."

async def main():
    # Use stdio transport
    async with stdio_server(server) as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            server.create_initialization_options()
        )

if __name__ == "__main__":
    asyncio.run(main())
```

## Diferencias clave con el enfoque obsoleto de SSE

**Transporte stdio (Estándar actual):**
- Modelo simple de subproceso: el cliente lanza el servidor como un proceso hijo.
- Comunicación a través de stdin/stdout utilizando mensajes JSON-RPC.
- No se requiere configuración de servidor HTTP.
- Mejor rendimiento y seguridad.
- Depuración y desarrollo más sencillos.

**Transporte SSE (Obsoleto a partir de MCP 2025-06-18):**
- Requería un servidor HTTP con puntos finales SSE.
- Configuración más compleja con infraestructura de servidor web.
- Consideraciones de seguridad adicionales para puntos finales HTTP.
- Ahora reemplazado por Streamable HTTP para escenarios basados en web.

### Crear un servidor con transporte stdio

Para crear nuestro servidor stdio, necesitamos:

1. **Importar las bibliotecas necesarias** - Necesitamos los componentes del servidor MCP y el transporte stdio.
2. **Crear una instancia del servidor** - Definir el servidor con sus capacidades.
3. **Definir herramientas** - Agregar la funcionalidad que queremos exponer.
4. **Configurar el transporte** - Configurar la comunicación stdio.
5. **Ejecutar el servidor** - Iniciar el servidor y manejar los mensajes.

Construyámoslo paso a paso:

### Paso 1: Crear un servidor stdio básico

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Create the server
server = Server("example-stdio-server")

@server.tool()
def get_greeting(name: str) -> str:
    """Generate a personalized greeting"""
    return f"Hello, {name}! Welcome to MCP stdio server."

async def main():
    async with stdio_server(server) as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            server.create_initialization_options()
        )

if __name__ == "__main__":
    asyncio.run(main())
```

### Paso 2: Agregar más herramientas

```python
@server.tool()
def calculate_sum(a: int, b: int) -> int:
    """Calculate the sum of two numbers"""
    return a + b

@server.tool()
def calculate_product(a: int, b: int) -> int:
    """Calculate the product of two numbers"""
    return a * b

@server.tool()
def get_server_info() -> dict:
    """Get information about this MCP server"""
    return {
        "server_name": "example-stdio-server",
        "version": "1.0.0",
        "transport": "stdio",
        "capabilities": ["tools"]
    }
```

### Paso 3: Ejecutar el servidor

Guarda el código como `server.py` y ejecútalo desde la línea de comandos:

```bash
python server.py
```

El servidor se iniciará y esperará entrada desde stdin. Se comunica utilizando mensajes JSON-RPC a través del transporte stdio.

### Paso 4: Probar con el Inspector

Puedes probar tu servidor utilizando el Inspector de MCP:

1. Instala el Inspector: `npx @modelcontextprotocol/inspector`.
2. Ejecuta el Inspector y apúntalo a tu servidor.
3. Prueba las herramientas que has creado.

### .NET

```csharp
var builder = WebApplication.CreateBuilder(args);
builder.Services
    .AddMcpServer();
 ```

## Depurar tu servidor stdio

### Usando el Inspector de MCP

El Inspector de MCP es una herramienta valiosa para depurar y probar servidores MCP. Así es como puedes usarlo con tu servidor stdio:

1. **Instalar el Inspector**:
   ```bash
   npx @modelcontextprotocol/inspector
   ```

2. **Ejecutar el Inspector**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

3. **Probar tu servidor**: El Inspector proporciona una interfaz web donde puedes:
   - Ver las capacidades del servidor.
   - Probar herramientas con diferentes parámetros.
   - Monitorear mensajes JSON-RPC.
   - Depurar problemas de conexión.

### Usando VS Code

También puedes depurar tu servidor MCP directamente en VS Code:

1. Crea una configuración de lanzamiento en `.vscode/launch.json`:
   ```json
   {
     "version": "0.2.0",
     "configurations": [
       {
         "name": "Debug MCP Server",
         "type": "python",
         "request": "launch",
         "program": "server.py",
         "console": "integratedTerminal"
       }
     ]
   }
   ```

2. Establece puntos de interrupción en tu código del servidor.
3. Ejecuta el depurador y prueba con el Inspector.

### Consejos comunes para depuración

- Usa `stderr` para registro: nunca escribas en `stdout`, ya que está reservado para mensajes MCP.
- Asegúrate de que todos los mensajes JSON-RPC estén delimitados por saltos de línea.
- Prueba con herramientas simples primero antes de agregar funcionalidad compleja.
- Usa el Inspector para verificar formatos de mensajes.

## Consumir tu servidor stdio en VS Code

Una vez que hayas construido tu servidor MCP stdio, puedes integrarlo con VS Code para usarlo con Claude u otros clientes compatibles con MCP.

### Configuración

1. **Crea un archivo de configuración MCP** en `%APPDATA%\Claude\claude_desktop_config.json` (Windows) o `~/Library/Application Support/Claude/claude_desktop_config.json` (Mac):

   ```json
   {
     "mcpServers": {
       "example-stdio-server": {
         "command": "python",
         "args": ["path/to/your/server.py"]
       }
     }
   }
   ```

2. **Reinicia Claude**: Cierra y vuelve a abrir Claude para cargar la nueva configuración del servidor.

3. **Prueba la conexión**: Inicia una conversación con Claude y prueba las herramientas de tu servidor:
   - "¿Puedes saludarme usando la herramienta de saludo?"
   - "Calcula la suma de 15 y 27."
   - "¿Cuál es la información del servidor?"

### Ejemplo de servidor stdio en TypeScript

Aquí tienes un ejemplo completo en TypeScript como referencia:

```typescript
#!/usr/bin/env node
import { Server } from "@modelcontextprotocol/sdk/server/index.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { CallToolRequestSchema, ListToolsRequestSchema } from "@modelcontextprotocol/sdk/types.js";

const server = new Server(
  {
    name: "example-stdio-server",
    version: "1.0.0",
  },
  {
    capabilities: {
      tools: {},
    },
  }
);

// Add tools
server.setRequestHandler(ListToolsRequestSchema, async () => {
  return {
    tools: [
      {
        name: "get_greeting",
        description: "Get a personalized greeting",
        inputSchema: {
          type: "object",
          properties: {
            name: {
              type: "string",
              description: "Name of the person to greet",
            },
          },
          required: ["name"],
        },
      },
    ],
  };
});

server.setRequestHandler(CallToolRequestSchema, async (request) => {
  if (request.params.name === "get_greeting") {
    return {
      content: [
        {
          type: "text",
          text: `Hello, ${request.params.arguments?.name}! Welcome to MCP stdio server.`,
        },
      ],
    };
  } else {
    throw new Error(`Unknown tool: ${request.params.name}`);
  }
});

async function runServer() {
  const transport = new StdioServerTransport();
  await server.connect(transport);
}

runServer().catch(console.error);
```

### Ejemplo de servidor stdio en .NET

```csharp
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;
using Microsoft.Extensions.Logging;
using ModelContextProtocol.Server;
using System.ComponentModel;

var builder = Host.CreateApplicationBuilder(args);

builder.Services
    .AddMcpServer()
    .WithStdioTransport()
    .WithTools<Tools>();

var app = builder.Build();
await app.RunAsync();

public class Tools
{
    [Description("Get a personalized greeting")]
    public string GetGreeting(string name)
    {
        return $"Hello, {name}! Welcome to MCP stdio server.";
    }

    [Description("Calculate the sum of two numbers")]
    public int CalculateSum(int a, int b)
    {
        return a + b;
    }
}
```

## Resumen

En esta lección actualizada, aprendiste a:

- Construir servidores MCP utilizando el transporte **stdio** actual (enfoque recomendado).
- Comprender por qué el transporte SSE fue obsoleto en favor de stdio y Streamable HTTP.
- Crear herramientas que puedan ser llamadas por clientes MCP.
- Depurar tu servidor utilizando el Inspector de MCP.
- Integrar tu servidor stdio con VS Code y Claude.

El transporte stdio proporciona una forma más simple, segura y eficiente de construir servidores MCP en comparación con el enfoque obsoleto de SSE. Es el transporte recomendado para la mayoría de las implementaciones de servidores MCP según la especificación 2025-06-18.

## Ejercicio: Probar tu servidor stdio

Ahora que has construido tu servidor stdio, probémoslo para asegurarnos de que funcione correctamente.

### Requisitos previos

1. Asegúrate de tener instalado el Inspector de MCP:
   ```bash
   npm install -g @modelcontextprotocol/inspector
   ```

2. Tu código del servidor debe estar guardado (por ejemplo, como `server.py`).

### Probar con el Inspector

1. **Inicia el Inspector con tu servidor**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

2. **Abre la interfaz web**: El Inspector abrirá una ventana del navegador mostrando las capacidades de tu servidor.

3. **Prueba las herramientas**: 
   - Prueba la herramienta `get_greeting` con diferentes nombres.
   - Prueba la herramienta `calculate_sum` con varios números.
   - Llama a la herramienta `get_server_info` para ver los metadatos del servidor.

4. **Monitorea la comunicación**: El Inspector muestra los mensajes JSON-RPC que se intercambian entre el cliente y el servidor.

### Qué deberías ver

Cuando tu servidor se inicie correctamente, deberías ver:
- Capacidades del servidor listadas en el Inspector.
- Herramientas disponibles para probar.
- Intercambios exitosos de mensajes JSON-RPC.
- Respuestas de herramientas mostradas en la interfaz.

### Problemas comunes y soluciones

**El servidor no se inicia:**
- Verifica que todas las dependencias estén instaladas: `pip install mcp`.
- Revisa la sintaxis e indentación de Python.
- Busca mensajes de error en la consola.

**Las herramientas no aparecen:**
- Asegúrate de que los decoradores `@server.tool()` estén presentes.
- Verifica que las funciones de herramientas estén definidas antes de `main()`.
- Confirma que el servidor esté configurado correctamente.

**Problemas de conexión:**
- Asegúrate de que el servidor esté utilizando correctamente el transporte stdio.
- Verifica que no haya otros procesos interfiriendo.
- Confirma la sintaxis del comando del Inspector.

## Tarea

Intenta ampliar tu servidor con más capacidades. Consulta [esta página](https://api.chucknorris.io/) para, por ejemplo, agregar una herramienta que llame a una API. Tú decides cómo debería ser el servidor. ¡Diviértete! 

## Solución

[Solución](./solution/README.md) Aquí tienes una posible solución con código funcional.

## Puntos clave

Los puntos clave de este capítulo son los siguientes:

- El transporte stdio es el mecanismo recomendado para servidores MCP locales.
- El transporte stdio permite una comunicación fluida entre servidores MCP y clientes utilizando flujos de entrada y salida estándar.
- Puedes usar tanto el Inspector como Visual Studio Code para consumir servidores stdio directamente, lo que facilita la depuración y la integración.

## Ejemplos 

- [Calculadora en Java](../samples/java/calculator/README.md)
- [Calculadora en .Net](../../../../03-GettingStarted/samples/csharp)
- [Calculadora en JavaScript](../samples/javascript/README.md)
- [Calculadora en TypeScript](../samples/typescript/README.md)
- [Calculadora en Python](../../../../03-GettingStarted/samples/python) 

## Recursos adicionales

- [SSE](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events)

## Qué sigue

## Próximos pasos

Ahora que has aprendido a construir servidores MCP con el transporte stdio, puedes explorar temas más avanzados:

- **Siguiente**: [HTTP Streaming con MCP (Streamable HTTP)](../06-http-streaming/README.md) - Aprende sobre el otro mecanismo de transporte compatible para servidores remotos.
- **Avanzado**: [Mejores prácticas de seguridad en MCP](../../02-Security/README.md) - Implementa seguridad en tus servidores MCP.
- **Producción**: [Estrategias de despliegue](../09-deployment/README.md) - Despliega tus servidores para uso en producción.

## Recursos adicionales

- [Especificación MCP 2025-06-18](https://spec.modelcontextprotocol.io/specification/) - Especificación oficial.
- [Documentación del SDK de MCP](https://github.com/modelcontextprotocol/sdk) - Referencias del SDK para todos los lenguajes.
- [Ejemplos de la comunidad](../../06-CommunityContributions/README.md) - Más ejemplos de servidores de la comunidad.

---

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Si bien nos esforzamos por garantizar la precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o imprecisiones. El documento original en su idioma nativo debe considerarse como la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por humanos. No nos hacemos responsables de ningún malentendido o interpretación errónea que surja del uso de esta traducción.