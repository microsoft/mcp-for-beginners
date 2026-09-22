# Transmisión HTTPS con el Protocolo de Contexto de Modelo (MCP)

Este capítulo proporciona una guía completa para implementar transmisión segura, escalable y en tiempo real con el Protocolo de Contexto de Modelo (MCP) utilizando HTTPS. Cubre la motivación para la transmisión, los mecanismos de transporte disponibles, cómo implementar HTTP transmisible en MCP, las mejores prácticas de seguridad, la migración desde SSE y orientación práctica para construir tus propias aplicaciones MCP con transmisión. 

> [!WARNING]
> Los ejemplos de implementación en esta lección están dirigidos a la **Especificación MCP
> `2025-11-25`** y demuestran el protocolo de enlace (handshake) legado `initialize`,
> `Mcp-Session-Id`, flujo de eventos GET, y modelo de capacidad de reanudación. MCP `2026-07-28`
> elimina esas características. Las solicitudes Streamable HTTP actuales son solicitudes POST autosuficientes
> con encabezados `MCP-Protocol-Version` y `Mcp-Method`, además de
> `Mcp-Name` cuando se requiere. Consulta
> [Cambios en MCP: La especificación 2026-07-28](../../01-CoreConcepts/mcp-2026-07-28.md)
> antes de usar estos ejemplos en una implementación nueva.

## Mecanismos de Transporte y Transmisión en MCP

Esta sección explora los diferentes mecanismos de transporte disponibles en MCP y su papel en habilitar capacidades de transmisión para la comunicación en tiempo real entre clientes y servidores.

### ¿Qué es un Mecanismo de Transporte?

Un mecanismo de transporte define cómo se intercambian datos entre el cliente y el servidor. MCP soporta múltiples tipos de transporte para adaptarse a diferentes entornos y requerimientos:

- **stdio**: Entrada/salida estándar, adecuado para herramientas locales y basadas en CLI. Simple pero no adecuado para web o nube.
- **HTTP+SSE**: El transporte remoto legado, desaprobado en MCP `2025-03-26`
    y reemplazado por Streamable HTTP. No lo uses para implementaciones nuevas.
- **Streamable HTTP**: Transporte de transmisión basado en HTTP moderno, soportando notificaciones y mejor escalabilidad. Recomendado para la mayoría de escenarios productivos y en la nube.

### Tabla Comparativa

Observa la siguiente tabla comparativa para entender las diferencias entre estos mecanismos de transporte:

| Transporte | Estado | Notificaciones | Uso típico |
|---|---|---|---|
| stdio | Actual | Sí | Subprocesos locales |
| HTTP+SSE | Desaprobado | Sí | Implementaciones remotas legadas |
| Streamable HTTP | Actual | Sí | Servidores remotos y en la nube |

> **Consejo:** Elegir el transporte correcto impacta el rendimiento, la escalabilidad y la experiencia del usuario. **Streamable HTTP** es recomendado para aplicaciones modernas, escalables y listas para la nube.

Los transportes estándar son stdio y Streamable HTTP. HTTP+SSE aparece solo en
ejemplos más antiguos.

## Transmisión: Conceptos y Motivación

Entender los conceptos fundamentales y las motivaciones detrás de la transmisión es esencial para implementar sistemas efectivos de comunicación en tiempo real.

**Streaming** es una técnica en programación de redes que permite enviar y recibir datos en pequeñas porciones manejables o como una secuencia de eventos, en lugar de esperar a que toda la respuesta esté lista. Esto es especialmente útil para:

- Archivos o conjuntos de datos grandes.
- Actualizaciones en tiempo real (por ejemplo, chat, barras de progreso).
- Cálculos de larga duración donde se quiere mantener informado al usuario.

Esto es lo que necesitas saber sobre la transmisión a nivel alto:

- Los datos se entregan progresivamente, no todos a la vez.
- El cliente puede procesar los datos a medida que llegan.
- Reduce la latencia percibida y mejora la experiencia del usuario.

### ¿Por qué usar transmisión?

Las razones para usar transmisión son las siguientes:

- Los usuarios reciben retroalimentación inmediatamente, no solo al final
- Permite aplicaciones en tiempo real y interfaces de usuario responsivas
- Uso más eficiente de los recursos de red y computación

### Ejemplo simple: Servidor y Cliente HTTP Streaming

Aquí tienes un ejemplo simple de cómo se puede implementar la transmisión:

#### Python

**Servidor (Python, usando FastAPI y StreamingResponse):**

```python
from fastapi import FastAPI
from fastapi.responses import StreamingResponse
import time

app = FastAPI()

async def event_stream():
    for i in range(1, 6):
        yield f"data: Message {i}\n\n"
        time.sleep(1)

@app.get("/stream")
def stream():
    return StreamingResponse(event_stream(), media_type="text/event-stream")
```

**Cliente (Python, usando requests):**

```python
import requests

with requests.get("http://localhost:8000/stream", stream=True) as r:
    for line in r.iter_lines():
        if line:
            print(line.decode())
```

Este ejemplo demuestra un servidor que envía una serie de mensajes al cliente a medida que están disponibles, en lugar de esperar a que todos los mensajes estén listos.

**Cómo funciona:**

- El servidor entrega cada mensaje conforme está listo.
- El cliente recibe e imprime cada fragmento a medida que llega.

**Requisitos:**

- El servidor debe usar una respuesta de transmisión (por ejemplo, `StreamingResponse` en FastAPI).
- El cliente debe procesar la respuesta como una transmisión (`stream=True` en requests).
- El Content-Type suele ser `text/event-stream` o `application/octet-stream`.

#### Java

**Servidor (Java, usando Spring Boot y Server-Sent Events):**

```java
@RestController
public class CalculatorController {

    @GetMapping(value = "/calculate", produces = MediaType.TEXT_EVENT_STREAM_VALUE)
    public Flux<ServerSentEvent<String>> calculate(@RequestParam double a,
                                                   @RequestParam double b,
                                                   @RequestParam String op) {
        
        double result;
        switch (op) {
            case "add": result = a + b; break;
            case "sub": result = a - b; break;
            case "mul": result = a * b; break;
            case "div": result = b != 0 ? a / b : Double.NaN; break;
            default: result = Double.NaN;
        }

        return Flux.<ServerSentEvent<String>>just(
                    ServerSentEvent.<String>builder()
                        .event("info")
                        .data("Calculating: " + a + " " + op + " " + b)
                        .build(),
                    ServerSentEvent.<String>builder()
                        .event("result")
                        .data(String.valueOf(result))
                        .build()
                )
                .delayElements(Duration.ofSeconds(1));
    }
}
```

**Cliente (Java, usando Spring WebFlux WebClient):**

```java
@SpringBootApplication
public class CalculatorClientApplication implements CommandLineRunner {

    private final WebClient client = WebClient.builder()
            .baseUrl("http://localhost:8080")
            .build();

    @Override
    public void run(String... args) {
        client.get()
                .uri(uriBuilder -> uriBuilder
                        .path("/calculate")
                        .queryParam("a", 7)
                        .queryParam("b", 5)
                        .queryParam("op", "mul")
                        .build())
                .accept(MediaType.TEXT_EVENT_STREAM)
                .retrieve()
                .bodyToFlux(String.class)
                .doOnNext(System.out::println)
                .blockLast();
    }
}
```

**Notas sobre la implementación en Java:**

- Usa el stack reactivo de Spring Boot con `Flux` para transmisión
- `ServerSentEvent` provee transmisión de eventos estructurados con tipos de eventos
- `WebClient` con `bodyToFlux()` permite consumir transmisión de forma reactiva
- `delayElements()` simula tiempo de procesamiento entre eventos
- Los eventos pueden tener tipos (`info`, `result`) para mejor manejo en el cliente

### Comparación: Transmisión Clásica vs Transmisión MCP

Las diferencias entre cómo funciona la transmisión de manera "clásica" versus cómo funciona en MCP pueden representarse así:

| Característica           | Transmisión HTTP Clásica          | Transmisión MCP (Notificaciones)      |
|------------------------|---------------------------------|-------------------------------------|
| Respuesta principal    | Fragmentada                     | Única, al final                     |
| Actualizaciones de progreso | Enviadas como fragmentos de datos | Enviadas como notificaciones        |
| Requisitos del cliente  | Debe procesar el flujo           | Debe implementar un manejador de mensajes |
| Caso de uso            | Archivos grandes, streams de tokens AI | Progreso, registros, retroalimentación en tiempo real |

### Diferencias clave observadas

Además, aquí algunas diferencias clave:

- **Patrón de Comunicación:**
  - Transmisión HTTP clásica: Usa codificación de transferencia fragmentada para enviar datos en fragmentos
  - Transmisión MCP: Usa un sistema estructurado de notificaciones con protocolo JSON-RPC

- **Formato del Mensaje:**
  - HTTP clásica: Fragmentos de texto plano con saltos de línea
  - MCP: Objetos estructurados LoggingMessageNotification con metadatos

- **Implementación del Cliente:**
  - HTTP clásica: Cliente simple que procesa respuestas en transmisión
  - MCP: Cliente más sofisticado con manejador de mensajes para procesar distintos tipos de mensajes

- **Actualizaciones de Progreso:**
  - HTTP clásica: El progreso es parte de la respuesta principal en streaming
  - MCP: El progreso se envía mediante mensajes de notificación separados mientras la respuesta principal llega al final

### Recomendaciones

Hay algunas recomendaciones cuando se trata de elegir entre implementar transmisión clásica (como un endpoint que te mostramos arriba usando `/stream`) versus elegir transmisión vía MCP.

- **Para necesidades simples de transmisión:** La transmisión HTTP clásica es más simple de implementar y suficiente para necesidades básicas de transmisión.


- **Para aplicaciones complejas e interactivas:** la transmisión MCP ofrece un enfoque más estructurado con metadatos más ricos y separación entre notificaciones y resultados finales.

- **Para aplicaciones de IA:** el sistema de notificaciones de MCP es particularmente útil para tareas de IA de larga duración donde se desea mantener a los usuarios informados sobre el progreso.

## Transmisión en MCP

Bien, hasta ahora has visto algunas recomendaciones y comparaciones sobre la diferencia entre la transmisión clásica y la transmisión en MCP. Vamos a entrar en detalle sobre cómo puedes aprovechar la transmisión en MCP.

Entender cómo funciona la transmisión dentro del marco MCP es esencial para construir aplicaciones receptivas que proporcionen retroalimentación en tiempo real a los usuarios durante operaciones prolongadas.

En MCP, la transmisión no consiste en enviar la respuesta principal en fragmentos, sino en enviar **notificaciones** al cliente mientras una herramienta procesa una solicitud. Estas notificaciones pueden incluir actualizaciones de progreso, registros u otros eventos.

### Cómo funciona

El resultado principal se sigue enviando como una única respuesta. Sin embargo, las notificaciones pueden enviarse como mensajes separados durante el procesamiento y así actualizar al cliente en tiempo real. El cliente debe poder manejar y mostrar estas notificaciones.

### Ejercicio opcional: conectar a un servidor MCP alojado

También puedes usar HTTP transmitible sin ejecutar un servidor local. Este ejemplo
se conecta a [Parallel Search MCP](https://docs.parallel.ai/integrations/mcp/search-mcp),
descubre sus herramientas y busca documentación pública de MCP usando el mismo
SDK de Python que el [cliente local](../../../../03-GettingStarted/06-http-streaming/solution/python/client.py).

El endpoint anónimo de Parallel no requiere cuenta ni clave API. El acceso gratis está
limitado por tasa. Ejecutar este script envía las consultas de búsqueda, objetivo y un
identificador de sesión aleatorio a Parallel. El servicio también ofrece `web_fetch`,
que envía URLs solicitadas y cualquier contexto proporcionado a Parallel. Usa información pública
para este ejercicio; consulta sus [términos](https://parallel.ai/customer-terms)
y [política de privacidad](https://parallel.ai/privacy-policy).

Con Python 3.10 o superior y un entorno virtual activado, instala el SDK:

```sh
python -m pip install "mcp>=1.10,<2"
```

Guarda esto como `hosted_search.py` y ejecuta `python hosted_search.py`:

```python
import asyncio
from uuid import uuid4

from mcp import ClientSession
from mcp.client.streamable_http import streamablehttp_client


async def main() -> None:
    session_id = str(uuid4())
    async with streamablehttp_client("https://search.parallel.ai/mcp") as (
        read_stream,
        write_stream,
        _,
    ):
        async with ClientSession(read_stream, write_stream) as session:
            await session.initialize()
            tools = await session.list_tools()
            print("Available tools:", [tool.name for tool in tools.tools])

            result = await session.call_tool(
                "web_search",
                {
                    "objective": "Find the official MCP Streamable HTTP documentation",
                    "search_queries": ["MCP Streamable HTTP documentation"],
                    "session_id": session_id,
                },
            )
            if result.isError:
                raise RuntimeError(f"Search tool failed: {result.content}")
            for block in result.content:
                if block.type == "text":
                    print(block.text)


async def run() -> None:
    await asyncio.wait_for(main(), timeout=60)


if __name__ == "__main__":
    asyncio.run(run())
```

Espera que el descubrimiento incluya `web_search` y `web_fetch`, seguido de una respuesta de búsqueda
con URLs de origen y extractos. Los resultados pueden variar o estar vacíos.
El script verifica `isError` porque una herramienta puede fallar incluso cuando la solicitud HTTP
tiene éxito. Si el acceso está limitado por tasa, espera antes de intentar de nuevo. Reutiliza el mismo
`session_id` si extiendes el script con llamadas relacionadas de búsqueda o extracción.

HTTP transmitible permite respuestas en JSON y SSE; este servidor puede devolver un
resultado JSON completo sin notificaciones de progreso. El SDK maneja el
transporte. Continúa con el ejemplo local abajo para aprender sobre notificaciones.
Este script opcional realiza una búsqueda explícita y cierra su conexión cuando
finaliza. Si más tarde expones estas herramientas a un agente, este puede invocarlas
durante su trabajo; trata el texto web recuperado como datos no confiables.

## ¿Qué es una Notificación?

Dijimos "Notificación", ¿qué significa eso en el contexto de MCP?

Una notificación es un mensaje JSON-RPC que no tiene un `id` y no
recibe respuesta. MCP usa notificaciones para progreso, cancelación y
otros eventos unidireccionales.

En MCP `2025-11-25`, un cliente envía `notifications/initialized` después del
saludo de inicialización. MCP `2026-07-28` no tiene saludo de inicialización, por lo que
esta notificación es un comportamiento heredado.

Una notificación se ve así como mensaje JSON:

```json
{
  jsonrpc: "2.0";
  method: string;
  params?: {
    [key: string]: unknown;
  };
}
```

El registro es una característica que usa notificaciones; las notificaciones en sí son un
tipo general de mensaje JSON-RPC.

> **Obsoleto en MCP `2026-07-28`:** la característica de registro sigue disponible
> por compatibilidad, pero es elegible para eliminación en la primera revisión
> de la especificación publicada a partir del 28 de julio de 2027. Las nuevas implementaciones deberían usar
> `stderr` con stdio o OpenTelemetry para observabilidad estructurada.

Para una implementación heredada `2025-11-25`, el servidor habilita la capacidad de registro
de esta manera:

```json
{
  "capabilities": {
    "logging": {}
  }
}
```

> [!NOTE]
> Dependiendo del SDK usado, el registro podría estar habilitado por defecto o podría ser necesario activarlo explícitamente en la configuración del servidor.

Hay diferentes tipos de notificaciones:

| Nivel     | Descripción                    | Caso de uso ejemplo            |
|-----------|-------------------------------|---------------------------------|
| debug     | Información detallada de depuración | Puntos de entrada/salida de funciones |
| info      | Mensajes informativos generales | Actualizaciones de progreso    |
| notice    | Eventos normales pero significativos | Cambios de configuración     |
| warning   | Condiciones de advertencia    | Uso de características obsoletas|
| error     | Condiciones de error          | Fallos en la operación         |
| critical  | Condiciones críticas          | Fallos en componentes del sistema|
| alert     | Acción debe tomarse inmediatamente | Corrupción de datos detectada|
| emergency | El sistema es inutilizable     | Fallo completo del sistema     |

## Implementación de Notificaciones en MCP

Para implementar notificaciones en MCP, necesitas configurar tanto el lado del servidor como el del cliente para manejar actualizaciones en tiempo real. Esto permite que tu aplicación proporcione retroalimentación inmediata a los usuarios durante operaciones prolongadas.

### Lado servidor: envío de notificaciones

Comencemos con el lado servidor. En MCP defines herramientas que pueden enviar notificaciones mientras procesan solicitudes. El servidor usa el objeto de contexto (usualmente `ctx`) para enviar mensajes al cliente.

#### Python

```python
@mcp.tool(description="A tool that sends progress notifications")
async def process_files(message: str, ctx: Context) -> TextContent:
    await ctx.info("Processing file 1/3...")
    await ctx.info("Processing file 2/3...")
    await ctx.info("Processing file 3/3...")
    return TextContent(type="text", text=f"Done: {message}")
```

En el ejemplo anterior, la herramienta `process_files` envía tres notificaciones al cliente mientras procesa cada archivo. Se usa el método `ctx.info()` para enviar mensajes informativos.

Además, para habilitar las notificaciones, asegúrate de que tu servidor use un transporte de transmisión (como `streamable-http`) y que tu cliente implemente un manejador de mensajes para procesar notificaciones. Así es como puedes configurar el servidor para usar el transporte `streamable-http`:

```python
mcp.run(transport="streamable-http")
```

#### .NET

```csharp
[Tool("A tool that sends progress notifications")]
public async Task<TextContent> ProcessFiles(string message, ToolContext ctx)
{
    await ctx.Info("Processing file 1/3...");
    await ctx.Info("Processing file 2/3...");
    await ctx.Info("Processing file 3/3...");
    return new TextContent
    {
        Type = "text",
        Text = $"Done: {message}"
    };
}
```

En este ejemplo de .NET, la herramienta `ProcessFiles` está decorada con el atributo `Tool` y envía tres notificaciones al cliente mientras procesa cada archivo. Se usa el método `ctx.Info()` para enviar mensajes informativos.

Para habilitar notificaciones en tu servidor MCP .NET, asegúrate de usar un transporte de transmisión:

```csharp
var builder = McpBuilder.Create();
await builder
    .UseStreamableHttp() // Enable streamable HTTP transport
    .Build()
    .RunAsync();
```

### Lado cliente: recepción de notificaciones

El cliente debe implementar un manejador de mensajes para procesar y mostrar notificaciones a medida que llegan.

#### Python

```python
async def message_handler(message):
    if isinstance(message, types.ServerNotification):
        print("NOTIFICATION:", message)
    else:
        print("SERVER MESSAGE:", message)

async with ClientSession(
   read_stream, 
   write_stream,
   logging_callback=logging_collector,
   message_handler=message_handler,
) as session:
```

En el código anterior, la función `message_handler` verifica si el mensaje entrante es una notificación. Si lo es, imprime la notificación; de lo contrario, la procesa como un mensaje regular del servidor. También observa cómo la `ClientSession` se inicializa con el `message_handler` para manejar notificaciones entrantes.

#### .NET

```csharp
// Define a message handler
void MessageHandler(IJsonRpcMessage message)
{
    if (message is ServerNotification notification)
    {
        Console.WriteLine($"NOTIFICATION: {notification}");
    }
    else
    {
        Console.WriteLine($"SERVER MESSAGE: {message}");
    }
}

// Create and use a client session with the message handler
var clientOptions = new ClientSessionOptions
{
    MessageHandler = MessageHandler,
    LoggingCallback = (level, message) => Console.WriteLine($"[{level}] {message}")
};

using var client = new ClientSession(readStream, writeStream, clientOptions);
await client.InitializeAsync();

// Now the client will process notifications through the MessageHandler
```


En este ejemplo de .NET, la función `MessageHandler` verifica si el mensaje entrante es una notificación. Si lo es, imprime la notificación; de lo contrario, lo procesa como un mensaje normal del servidor. La `ClientSession` se inicializa con el manejador de mensajes a través de las `ClientSessionOptions`.

Para habilitar notificaciones, asegúrate de que tu servidor use un transporte de streaming (como `streamable-http`) y que tu cliente implemente un manejador de mensajes para procesar notificaciones.

## Notificaciones de Progreso y Escenarios

Esta sección explica el concepto de notificaciones de progreso en MCP, por qué son importantes y cómo implementarlas usando Streamable HTTP. También encontrarás una tarea práctica para reforzar tu comprensión.

Las notificaciones de progreso son mensajes en tiempo real enviados desde el servidor al cliente durante operaciones largas. En lugar de esperar a que todo el proceso termine, el servidor mantiene al cliente actualizado sobre el estado actual. Esto mejora la transparencia, la experiencia del usuario y facilita la depuración.

**Ejemplo:**

```text

"Processing document 1/10"
"Processing document 2/10"
...
"Processing complete!"

```

### ¿Por qué usar notificaciones de progreso?

Las notificaciones de progreso son esenciales por varias razones:

- **Mejor experiencia de usuario:** Los usuarios ven actualizaciones mientras avanza el trabajo, no solo al final.
- **Retroalimentación en tiempo real:** Los clientes pueden mostrar barras de progreso o registros, haciendo que la app se sienta más receptiva.
- **Depuración y monitoreo más fáciles:** Desarrolladores y usuarios pueden ver dónde un proceso podría estar lento o detenido.

### Cómo implementar notificaciones de progreso

Aquí te mostramos cómo puedes implementar notificaciones de progreso en MCP:

- **En el servidor:** Usa `ctx.info()` o `ctx.log()` para enviar notificaciones conforme se procesa cada elemento. Esto envía un mensaje al cliente antes de que el resultado principal esté listo.
- **En el cliente:** Implementa un manejador de mensajes que escuche y muestre notificaciones a medida que llegan. Este manejador distingue entre notificaciones y el resultado final.

**Ejemplo de servidor:**

#### Python

```python
@mcp.tool(description="A tool that sends progress notifications")
async def process_files(message: str, ctx: Context) -> TextContent:
    for i in range(1, 11):
        await ctx.info(f"Processing document {i}/10")
    await ctx.info("Processing complete!")
    return TextContent(type="text", text=f"Done: {message}")
```

**Ejemplo de cliente:**

#### Python

```python
async def message_handler(message):
    if isinstance(message, types.ServerNotification):
        print("NOTIFICATION:", message)
    else:
        print("SERVER MESSAGE:", message)
```

## Consideraciones de Seguridad

La seguridad debe ser una prioridad máxima al implementar cualquier servidor, especialmente cuando se usan transportes basados en HTTP como Streamable HTTP en MCP.

Al implementar servidores MCP con transportes basados en HTTP, la seguridad es una preocupación primordial que requiere atención cuidadosa a múltiples vectores de ataque y mecanismos de protección.

### Resumen

La seguridad es crítica al exponer servidores MCP sobre HTTP. Streamable HTTP introduce nuevas superficies de ataque y requiere configuración cuidadosa.

Aquí algunas consideraciones clave de seguridad:

- **Validación del encabezado Origin:** Siempre valida el encabezado `Origin` para prevenir ataques de DNS rebinding.
- **Enlace a localhost:** Para desarrollo local, enlaza los servidores a `localhost` para evitar exponerlos a internet pública.
- **Autenticación:** Implementa autenticación (por ejemplo, claves API, OAuth) para despliegues en producción.
- **CORS:** Configura políticas de Cross-Origin Resource Sharing (CORS) para restringir accesos.
- **HTTPS:** Usa HTTPS en producción para cifrar el tráfico.

### Mejores Prácticas

Además, aquí hay algunas mejores prácticas a seguir al implementar seguridad en tu servidor MCP de streaming:

- Nunca confíes en solicitudes entrantes sin validación.
- Registra y monitorea todos los accesos y errores.
- Actualiza regularmente las dependencias para parchear vulnerabilidades de seguridad.

### Desafíos

Enfrentarás algunos desafíos al implementar seguridad en servidores MCP de streaming:

- Balancear seguridad con facilidad de desarrollo
- Asegurar compatibilidad con diversos entornos cliente


## Actualizando de SSE a Streamable HTTP

Para aplicaciones que actualmente usan Server-Sent Events (SSE), migrar a Streamable HTTP ofrece capacidades mejoradas y mejor sostenibilidad a largo plazo para tus implementaciones MCP.

### ¿Por qué actualizar?

Hay dos razones convincentes para actualizar de SSE a Streamable HTTP:

- Streamable HTTP ofrece mejor escalabilidad, compatibilidad y soporte enriquecido para notificaciones que SSE.
- Es el transporte recomendado para nuevas aplicaciones MCP.

### Pasos para la migración

Aquí te mostramos cómo migrar de SSE a Streamable HTTP en tus aplicaciones MCP:

- **Actualiza el código del servidor** para usar `transport="streamable-http"` en `mcp.run()`.
- **Actualiza el código del cliente** para usar `streamablehttp_client` en lugar del cliente SSE.
- **Implementa un manejador de mensajes** en el cliente para procesar notificaciones.
- **Prueba la compatibilidad** con herramientas y flujos de trabajo existentes.

### Manteniendo la compatibilidad

Se recomienda mantener compatibilidad con clientes SSE existentes durante el proceso de migración. Aquí algunas estrategias:

- Puedes soportar tanto SSE como Streamable HTTP ejecutando ambos transportes en diferentes endpoints.
- Migra gradualmente los clientes al nuevo transporte.

### Desafíos

Asegúrate de abordar los siguientes desafíos durante la migración:

- Asegurar que todos los clientes estén actualizados
- Manejar las diferencias en la entrega de notificaciones

### Tarea: Construye tu propia aplicación MCP de streaming

**Escenario:**
Construye un servidor y cliente MCP donde el servidor procese una lista de ítems (por ejemplo, archivos o documentos) y envíe una notificación por cada ítem procesado. El cliente debe mostrar cada notificación a medida que llega.

**Pasos:**

1. Implementa una herramienta servidor que procese una lista y envíe notificaciones por cada ítem.
2. Implementa un cliente con un manejador de mensajes para mostrar notificaciones en tiempo real.
3. Prueba tu implementación ejecutando ambos servidor y cliente, y observa las notificaciones.

[Solución](./solution/README.md)

## Lecturas adicionales y qué sigue

Para continuar tu camino con el streaming MCP y expandir tu conocimiento, esta sección provee recursos adicionales y pasos sugeridos para construir aplicaciones más avanzadas.

### Lecturas adicionales

- [Microsoft: Introducción a HTTP Streaming](https://learn.microsoft.com/aspnet/core/fundamentals/http-requests?view=aspnetcore-8.0&WT.mc_id=%3Fwt.mc_id%3DMVP_452430#streaming)
- [Microsoft: Server-Sent Events (SSE)](https://learn.microsoft.com/azure/application-gateway/for-containers/server-sent-events?tabs=server-sent-events-gateway-api&WT.mc_id=%3Fwt.mc_id%3DMVP_452430)
- [Microsoft: CORS en ASP.NET Core](https://learn.microsoft.com/aspnet/core/security/cors?view=aspnetcore-8.0&WT.mc_id=%3Fwt.mc_id%3DMVP_452430)
- [Python requests: Solicitudes streaming](https://requests.readthedocs.io/en/latest/user/advanced/#streaming-requests)

### Qué sigue

- Intenta construir herramientas MCP más avanzadas que usen streaming para analíticas en tiempo real, chat o edición colaborativa.
- Explora integrar el streaming MCP con frameworks frontend (React, Vue, etc.) para actualizaciones en vivo en la UI.
- Siguiente: [Uso del AI Toolkit para VSCode](../07-aitk/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Descargo de responsabilidad**:
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional humana. No somos responsables de cualquier malentendido o interpretación errónea que surja del uso de esta traducción.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->