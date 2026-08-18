# Transmisión HTTPS con el Protocolo de Contexto de Modelo (MCP)

Este capítulo proporciona una guía completa para implementar transmisión segura, escalable y en tiempo real con el Protocolo de Contexto de Modelo (MCP) usando HTTPS. Cubre la motivación para la transmisión, los mecanismos de transporte disponibles, cómo implementar HTTP transmisible en MCP, las mejores prácticas de seguridad, la migración desde SSE y guías prácticas para construir tus propias aplicaciones MCP con transmisión.

> **Mirando hacia adelante:** esta lección describe HTTP transmisible bajo la **Especificación MCP 2025-11-25**, donde se establece una sesión durante `initialize` y se fija con un encabezado `Mcp-Session-Id`. El candidato a versión `2026-07-28` elimina por completo el apretón de manos y el ID de sesión, haciendo que cada solicitud sea autónoma y direccionable a cualquier instancia del servidor sin sesiones persistentes. Consulta [Qué cambia en MCP: El candidato a versión 2026-07-28](../../01-CoreConcepts/mcp-2026-07-28-release-candidate.md) para más detalles.

## Mecanismos de Transporte y Transmisión en MCP

Esta sección explora los diferentes mecanismos de transporte disponibles en MCP y su papel en habilitar capacidades de transmisión para la comunicación en tiempo real entre clientes y servidores.

### ¿Qué es un Mecanismo de Transporte?

Un mecanismo de transporte define cómo se intercambian los datos entre el cliente y el servidor. MCP soporta múltiples tipos de transporte para adaptarse a diferentes entornos y requerimientos:

- **stdio**: Entrada/salida estándar, adecuado para herramientas locales y basadas en CLI. Simple pero no adecuado para web o nube.
- **SSE (Server-Sent Events)**: Permite que los servidores envíen actualizaciones en tiempo real a los clientes vía HTTP. Bueno para interfaces web, pero limitado en escalabilidad y flexibilidad. Según la Especificación MCP 2025-06-18, el transporte independiente SSE (Server-Sent Events) ha sido desaprobado y reemplazado por el transporte "HTTP transmisible".
- **HTTP transmisible**: Transporte moderno basado en HTTP para transmisión, soporta notificaciones y mejor escalabilidad. Recomendado para la mayoría de escenarios de producción y en la nube.

### Tabla Comparativa

Mira la tabla comparativa a continuación para entender las diferencias entre estos mecanismos de transporte:

| Transporte         | Actualizaciones en Tiempo Real | Transmisión | Escalabilidad | Caso de Uso            |
|-------------------|-------------------------------|-------------|---------------|------------------------|
| stdio             | No                            | No          | Baja          | Herramientas CLI locales|
| SSE               | Sí                            | Sí          | Media         | Web, actualizaciones en tiempo real |
| HTTP transmisible | Sí                            | Sí          | Alta          | Nube, multi-cliente     |

> **Consejo:** Elegir el transporte correcto impacta en el rendimiento, la escalabilidad y la experiencia del usuario. **HTTP transmisible** es recomendado para aplicaciones modernas, escalables y preparadas para la nube.

Nota los transportes stdio y SSE que se mostraron en capítulos anteriores y cómo HTTP transmisible es el transporte cubierto en este capítulo.

## Transmisión: Conceptos y Motivación

Entender los conceptos fundamentales y la motivación detrás de la transmisión es esencial para implementar sistemas efectivos de comunicación en tiempo real.

**Transmisión** es una técnica en programación de redes que permite enviar y recibir datos en fragmentos pequeños y manejables o como una secuencia de eventos, en lugar de esperar a que toda una respuesta esté lista. Esto es especialmente útil para:

- Archivos o conjuntos de datos grandes.
- Actualizaciones en tiempo real (ej., chat, barras de progreso).
- Cálculos de larga duración donde se desea mantener informado al usuario.

Aquí hay lo que debes saber sobre la transmisión a alto nivel:

- Los datos se entregan progresivamente, no todos de una vez.
- El cliente puede procesar datos a medida que llegan.
- Reduce la latencia percibida y mejora la experiencia del usuario.

### ¿Por qué usar transmisión?

Las razones para usar transmisión son las siguientes:

- Los usuarios reciben retroalimentación inmediata, no solo al final
- Permite aplicaciones en tiempo real e interfaces responsivas
- Uso más eficiente de los recursos de red y computación

### Ejemplo Simple: Servidor y Cliente de Transmisión HTTP

Aquí hay un ejemplo simple de cómo se puede implementar la transmisión:

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

Este ejemplo demuestra un servidor enviando una serie de mensajes al cliente a medida que están disponibles, en lugar de esperar a que todos los mensajes estén listos.

**Cómo funciona:**

- El servidor produce cada mensaje a medida que está listo.
- El cliente recibe e imprime cada fragmento a medida que llega.

**Requisitos:**

- El servidor debe usar una respuesta de transmisión (ej., `StreamingResponse` en FastAPI).
- El cliente debe procesar la respuesta como un flujo (`stream=True` en requests).
- Content-Type usualmente es `text/event-stream` o `application/octet-stream`.

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

**Notas de Implementación en Java:**

- Utiliza el stack reactivo de Spring Boot con `Flux` para transmisión
- `ServerSentEvent` proporciona transmisión estructurada de eventos con tipos de evento
- `WebClient` con `bodyToFlux()` permite consumo reactivo de transmisión
- `delayElements()` simula tiempo de procesamiento entre eventos
- Los eventos pueden tener tipos (`info`, `result`) para mejor manejo en el cliente

### Comparación: Transmisión Clásica vs Transmisión MCP

Las diferencias entre cómo funciona la transmisión de manera "clásica" versus cómo funciona en MCP pueden representarse así:

| Característica          | Transmisión HTTP Clásica      | Transmisión MCP (Notificaciones)     |
|------------------------|-------------------------------|-------------------------------------|
| Respuesta principal     | Fragmentada                   | Única, al final                     |
| Actualizaciones de progreso | Enviadas como fragmentos de datos | Enviadas como notificaciones          |
| Requisitos del cliente  | Debe procesar el flujo        | Debe implementar un manejador de mensajes |
| Caso de uso             | Archivos grandes, flujos de tokens AI | Progreso, registros, retroalimentación en tiempo real |

### Diferencias Clave Observadas

Además, aquí algunas diferencias clave:

- **Patrón de Comunicación:**
  - Transmisión HTTP clásica: Usa codificación de transferencia fragmentada simple para enviar datos en fragmentos
  - Transmisión MCP: Usa un sistema estructurado de notificaciones con protocolo JSON-RPC

- **Formato de Mensaje:**
  - HTTP clásico: Fragmentos en texto plano con saltos de línea
  - MCP: Objetos estructurados LoggingMessageNotification con metadatos

- **Implementación Cliente:**
  - HTTP clásico: Cliente simple que procesa respuestas en streaming
  - MCP: Cliente más sofisticado con un manejador de mensajes para procesar distintos tipos de mensajes

- **Actualizaciones de Progreso:**
  - HTTP clásico: El progreso es parte del flujo de respuesta principal
  - MCP: El progreso se envía vía mensajes de notificación separados mientras la respuesta principal llega al final

### Recomendaciones

Hay algunas recomendaciones cuando se trata de elegir entre implementar transmisión clásica (como un endpoint que mostramos arriba usando `/stream`) versus elegir transmisión vía MCP.

- **Para necesidades sencillas de transmisión:** La transmisión HTTP clásica es más sencilla de implementar y suficiente para necesidades básicas.

- **Para aplicaciones complejas e interactivas:** La transmisión MCP ofrece un enfoque más estructurado con metadatos enriquecidos y separación entre notificaciones y resultados finales.

- **Para aplicaciones de IA:** El sistema de notificaciones de MCP es particularmente útil para tareas de IA de larga duración donde se quiere mantener informados a los usuarios sobre el progreso.

## Transmisión en MCP

Bien, ya viste algunas recomendaciones y comparaciones hasta aquí sobre la diferencia entre transmisión clásica y transmisión en MCP. Entremos en detalle exactamente cómo puedes aprovechar la transmisión en MCP.

Entender cómo funciona la transmisión dentro del marco MCP es esencial para construir aplicaciones responsivas que brinden retroalimentación en tiempo real a los usuarios durante operaciones de larga duración.

En MCP, la transmisión no se trata de enviar la respuesta principal en fragmentos, sino de enviar **notificaciones** al cliente mientras una herramienta procesa una solicitud. Estas notificaciones pueden incluir actualizaciones de progreso, registros u otros eventos.

### Cómo funciona

El resultado principal sigue siendo enviado como una única respuesta. Sin embargo, las notificaciones pueden enviarse como mensajes separados durante el procesamiento y así actualizar al cliente en tiempo real. El cliente debe ser capaz de manejar y mostrar estas notificaciones.

## ¿Qué es una Notificación?

Dijimos "Notificación", ¿qué significa eso en el contexto de MCP?

Una notificación es un mensaje enviado del servidor al cliente para informar sobre progreso, estado u otros eventos durante una operación prolongada. Las notificaciones mejoran la transparencia y la experiencia de usuario.

Por ejemplo, un cliente debe enviar una notificación una vez que se ha realizado el apretón de manos inicial con el servidor.

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

Las notificaciones pertenecen a un tema en MCP referido como ["Logging"](https://modelcontextprotocol.io/specification/draft/server/utilities/logging).

> **Aviso de desaprobación:** el candidato a versión `2026-07-28` de la especificación MCP marca el primitivo Logging como desaprobado en favor de `stderr` para transportes stdio y OpenTelemetry para observabilidad estructurada. Logging sigue funcionando en `2025-11-25` y por lo menos un año después de cualquier desaprobación formal. Consulta [Qué cambia en MCP: El candidato a versión 2026-07-28](../../01-CoreConcepts/mcp-2026-07-28-release-candidate.md).

Para que el logging funcione, el servidor necesita habilitarlo como característica/capacidad así:

```json
{
  "capabilities": {
    "logging": {}
  }
}
```

> [!NOTE]
> Dependiendo del SDK usado, el logging podría estar habilitado por defecto, o es posible que necesites habilitarlo explícitamente en la configuración de tu servidor.

Hay diferentes tipos de notificaciones:

| Nivel      | Descripción                    | Caso de Uso Ejemplo            |
|------------|-------------------------------|-------------------------------|
| debug      | Información detallada de depuración | Puntos de entrada/salida de funciones |
| info       | Mensajes informativos generales | Actualizaciones de progreso de operación |
| notice     | Eventos normales pero significativos | Cambios de configuración       |
| warning    | Condiciones de advertencia     | Uso de funciones desaprobadas  |
| error      | Condiciones de error           | Fallos en operaciones          |
| critical   | Condiciones críticas           | Fallos en componentes del sistema |
| alert      | Se debe tomar acción inmediata | Detección de corrupción de datos |
| emergency  | El sistema es inutilizable     | Fallo completo del sistema     |

## Implementando Notificaciones en MCP

Para implementar notificaciones en MCP, necesitas configurar tanto el servidor como el cliente para manejar actualizaciones en tiempo real. Esto permite que tu aplicación proporcione retroalimentación inmediata a los usuarios durante operaciones prolongadas.

### Lado servidor: Enviar Notificaciones

Empecemos con el lado servidor. En MCP, defines herramientas que pueden enviar notificaciones mientras procesan solicitudes. El servidor usa el objeto contexto (usualmente `ctx`) para enviar mensajes al cliente.

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

Además, para habilitar notificaciones, asegúrate de que tu servidor use un transporte de transmisión (como `streamable-http`) y que tu cliente implemente un manejador de mensajes para procesar las notificaciones. Aquí te mostramos cómo configurar el servidor para usar el transporte `streamable-http`:

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

En este ejemplo .NET, la herramienta `ProcessFiles` está decorada con el atributo `Tool` y envía tres notificaciones al cliente mientras procesa cada archivo. Se usa el método `ctx.Info()` para enviar mensajes informativos.

Para habilitar notificaciones en tu servidor MCP .NET, asegúrate de usar un transporte de transmisión:

```csharp
var builder = McpBuilder.Create();
await builder
    .UseStreamableHttp() // Enable streamable HTTP transport
    .Build()
    .RunAsync();
```

### Lado cliente: Recibir Notificaciones

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

En el código anterior, la función `message_handler` verifica si el mensaje entrante es una notificación. Si lo es, la imprime; de lo contrario, la procesa como un mensaje normal del servidor. También observa cómo `ClientSession` se inicializa con el `message_handler` para manejar las notificaciones entrantes.

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

En este ejemplo .NET, la función `MessageHandler` verifica si el mensaje entrante es una notificación. Si lo es, la imprime; de lo contrario, la procesa como un mensaje regular del servidor. `ClientSession` se inicializa con el manejador de mensajes a través de `ClientSessionOptions`.

Para habilitar notificaciones, asegúrate de que el servidor use un transporte de transmisión (como `streamable-http`) y que el cliente implemente un manejador de mensajes para procesar notificaciones.

## Notificaciones de Progreso y Escenarios

Esta sección explica el concepto de notificaciones de progreso en MCP, por qué son importantes y cómo implementarlas usando HTTP transmisible. También encontrarás una tarea práctica para reforzar tu comprensión.

Las notificaciones de progreso son mensajes en tiempo real enviados del servidor al cliente durante operaciones prolongadas. En lugar de esperar a que todo el proceso termine, el servidor mantiene al cliente actualizado sobre el estado actual. Esto mejora la transparencia, la experiencia del usuario y facilita la depuración.

**Ejemplo:**

```text

"Processing document 1/10"
"Processing document 2/10"
...
"Processing complete!"

```

### ¿Por qué usar notificaciones de progreso?

Las notificaciones de progreso son esenciales por varias razones:

- **Mejor experiencia de usuario:** Los usuarios ven actualizaciones a medida que avanza el trabajo, no solo al final.
- **Retroalimentación en tiempo real:** Los clientes pueden mostrar barras de progreso o registros, haciendo que la aplicación se sienta responsiva.
- **Depuración y monitoreo más fáciles:** Desarrolladores y usuarios pueden ver dónde un proceso podría estar lento o bloqueado.

### Cómo implementar notificaciones de progreso

Aquí te mostramos cómo implementar notificaciones de progreso en MCP:

- **En el servidor:** Usa `ctx.info()` o `ctx.log()` para enviar notificaciones a medida que cada elemento se procesa. Esto envía un mensaje al cliente antes de que esté listo el resultado principal.
- **En el cliente:** Implementa un manejador de mensajes que escuche y muestre notificaciones a medida que llegan. Este manejador distingue entre notificaciones y el resultado final.

**Ejemplo en el servidor:**


#### Python

```python
@mcp.tool(description="A tool that sends progress notifications")
async def process_files(message: str, ctx: Context) -> TextContent:
    for i in range(1, 11):
        await ctx.info(f"Processing document {i}/10")
    await ctx.info("Processing complete!")
    return TextContent(type="text", text=f"Done: {message}")
```

**Ejemplo Cliente:**

#### Python

```python
async def message_handler(message):
    if isinstance(message, types.ServerNotification):
        print("NOTIFICATION:", message)
    else:
        print("SERVER MESSAGE:", message)
```

## Consideraciones de Seguridad

La seguridad debe ser una prioridad principal al implementar cualquier servidor, especialmente cuando se utilizan transportes basados en HTTP como Streamable HTTP en MCP.

Al implementar servidores MCP con transportes basados en HTTP, la seguridad se vuelve una preocupación primordial que requiere atención cuidadosa a múltiples vectores de ataque y mecanismos de protección.

### Visión General

La seguridad es crítica cuando se exponen servidores MCP sobre HTTP. Streamable HTTP introduce nuevas superficies de ataque y requiere una configuración cuidadosa.

Aquí hay algunas consideraciones clave de seguridad:

- **Validación de la cabecera Origin**: Siempre valide la cabecera `Origin` para evitar ataques de reanudación DNS.
- **Vinculación a localhost**: Para desarrollo local, vincule los servidores a `localhost` para evitar exponerlos a Internet público.
- **Autenticación**: Implemente autenticación (por ejemplo, claves API, OAuth) para despliegues en producción.
- **CORS**: Configure políticas de Compartición de Recursos Cross-Origin (CORS) para restringir el acceso.
- **HTTPS**: Use HTTPS en producción para cifrar el tráfico.

### Mejores Prácticas

Además, aquí hay algunas mejores prácticas para seguir al implementar seguridad en su servidor de streaming MCP:

- Nunca confíe en solicitudes entrantes sin validación.
- Registre y monitoree todos los accesos y errores.
- Actualice regularmente las dependencias para corregir vulnerabilidades de seguridad.

### Desafíos

Se enfrentará a algunos desafíos al implementar seguridad en servidores de streaming MCP:

- Equilibrar la seguridad con la facilidad de desarrollo
- Asegurar compatibilidad con diversos entornos clientes


## Actualización de SSE a Streamable HTTP

Para aplicaciones que actualmente usan Server-Sent Events (SSE), migrar a Streamable HTTP ofrece capacidades mejoradas y una mejor sostenibilidad a largo plazo para sus implementaciones MCP.

### ¿Por qué actualizar?

Hay dos razones convincentes para actualizar de SSE a Streamable HTTP:

- Streamable HTTP ofrece mejor escalabilidad, compatibilidad y soporte de notificaciones más rico que SSE.
- Es el transporte recomendado para nuevas aplicaciones MCP.

### Pasos para migrar

Así es como puede migrar de SSE a Streamable HTTP en sus aplicaciones MCP:

- **Actualice el código del servidor** para usar `transport="streamable-http"` en `mcp.run()`.
- **Actualice el código del cliente** para usar `streamablehttp_client` en lugar del cliente SSE.
- **Implemente un manejador de mensajes** en el cliente para procesar notificaciones.
- **Pruebe la compatibilidad** con herramientas y flujos de trabajo existentes.

### Mantener la compatibilidad

Se recomienda mantener la compatibilidad con clientes SSE existentes durante el proceso de migración. Aquí hay algunas estrategias:

- Puede soportar tanto SSE como Streamable HTTP ejecutando ambos transportes en diferentes endpoints.
- Migre gradualmente los clientes al nuevo transporte.

### Desafíos

Asegúrese de abordar los siguientes desafíos durante la migración:

- Asegurar que todos los clientes estén actualizados
- Manejar diferencias en la entrega de notificaciones

### Tarea: Construya su propia aplicación MCP de streaming

**Escenario:**
Construya un servidor y cliente MCP donde el servidor procese una lista de elementos (por ejemplo, archivos o documentos) y envíe una notificación por cada elemento procesado. El cliente debe mostrar cada notificación a medida que llega.

**Pasos:**

1. Implemente una herramienta de servidor que procese una lista y envíe notificaciones por cada elemento.
2. Implemente un cliente con un manejador de mensajes para mostrar notificaciones en tiempo real.
3. Pruebe su implementación ejecutando tanto servidor como cliente, y observe las notificaciones.

[Solución](./solution/README.md)

## Más Lecturas y ¿Qué sigue?

Para continuar su camino con el streaming MCP y expandir su conocimiento, esta sección proporciona recursos adicionales y pasos sugeridos para construir aplicaciones más avanzadas.

### Más Lecturas

- [Microsoft: Introducción al Streaming HTTP](https://learn.microsoft.com/aspnet/core/fundamentals/http-requests?view=aspnetcore-8.0&WT.mc_id=%3Fwt.mc_id%3DMVP_452430#streaming)
- [Microsoft: Server-Sent Events (SSE)](https://learn.microsoft.com/azure/application-gateway/for-containers/server-sent-events?tabs=server-sent-events-gateway-api&WT.mc_id=%3Fwt.mc_id%3DMVP_452430)
- [Microsoft: CORS en ASP.NET Core](https://learn.microsoft.com/aspnet/core/security/cors?view=aspnetcore-8.0&WT.mc_id=%3Fwt.mc_id%3DMVP_452430)
- [Python requests: Solicitudes de Streaming](https://requests.readthedocs.io/en/latest/user/advanced/#streaming-requests)

### ¿Qué sigue?

- Intente construir herramientas MCP más avanzadas que usen streaming para análisis en tiempo real, chat o edición colaborativa.
- Explore la integración del streaming MCP con frameworks frontend (React, Vue, etc.) para actualizaciones en vivo de UI.
- Siguiente: [Utilizando AI Toolkit para VSCode](../07-aitk/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Descargo de responsabilidad**:
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional humana. No somos responsables de cualquier malentendido o interpretación errónea que surja del uso de esta traducción.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->