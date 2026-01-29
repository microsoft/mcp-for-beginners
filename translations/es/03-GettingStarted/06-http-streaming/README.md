# Transmisión HTTPS con el Protocolo de Contexto de Modelo (MCP)

Este capítulo ofrece una guía completa para implementar transmisión segura, escalable y en tiempo real con el Protocolo de Contexto de Modelo (MCP) utilizando HTTPS. Cubre la motivación para la transmisión, los mecanismos de transporte disponibles, cómo implementar HTTP transmisible en MCP, mejores prácticas de seguridad, migración desde SSE y orientación práctica para construir tus propias aplicaciones MCP de transmisión.

## Mecanismos de Transporte y Transmisión en MCP

Esta sección explora los diferentes mecanismos de transporte disponibles en MCP y su papel en habilitar capacidades de transmisión para la comunicación en tiempo real entre clientes y servidores.

### ¿Qué es un Mecanismo de Transporte?

Un mecanismo de transporte define cómo se intercambian los datos entre el cliente y el servidor. MCP admite múltiples tipos de transporte para adaptarse a diferentes entornos y requisitos:

- **stdio**: Entrada/salida estándar, adecuado para herramientas locales y basadas en CLI. Simple pero no apto para web o nube.
- **SSE (Server-Sent Events)**: Permite que los servidores envíen actualizaciones en tiempo real a los clientes a través de HTTP. Bueno para interfaces web, pero limitado en escalabilidad y flexibilidad.
- **HTTP transmisible**: Transporte moderno basado en HTTP para transmisión, que admite notificaciones y mejor escalabilidad. Recomendado para la mayoría de los escenarios de producción y nube.

### Tabla Comparativa

Consulta la tabla comparativa a continuación para entender las diferencias entre estos mecanismos de transporte:

| Transporte         | Actualizaciones en Tiempo Real | Transmisión | Escalabilidad | Caso de Uso                |
|--------------------|-------------------------------|-------------|---------------|---------------------------|
| stdio              | No                            | No          | Baja          | Herramientas CLI locales   |
| SSE                | Sí                            | Sí          | Media         | Web, actualizaciones en tiempo real |
| HTTP transmisible  | Sí                            | Sí          | Alta          | Nube, múltiples clientes   |

> **Consejo:** Elegir el transporte adecuado impacta el rendimiento, la escalabilidad y la experiencia del usuario. **HTTP transmisible** es recomendado para aplicaciones modernas, escalables y preparadas para la nube.

Nota los transportes stdio y SSE que se te mostraron en los capítulos anteriores y cómo HTTP transmisible es el transporte cubierto en este capítulo.

## Transmisión: Conceptos y Motivación

Entender los conceptos fundamentales y las motivaciones detrás de la transmisión es esencial para implementar sistemas efectivos de comunicación en tiempo real.

**Transmisión** es una técnica en programación de redes que permite enviar y recibir datos en pequeños fragmentos manejables o como una secuencia de eventos, en lugar de esperar a que toda la respuesta esté lista. Esto es especialmente útil para:

- Archivos o conjuntos de datos grandes.
- Actualizaciones en tiempo real (por ejemplo, chat, barras de progreso).
- Computaciones de larga duración donde se desea mantener informado al usuario.

Esto es lo que necesitas saber sobre la transmisión a nivel general:

- Los datos se entregan progresivamente, no todos a la vez.
- El cliente puede procesar los datos a medida que llegan.
- Reduce la latencia percibida y mejora la experiencia del usuario.

### ¿Por qué usar transmisión?

Las razones para usar transmisión son las siguientes:

- Los usuarios reciben retroalimentación inmediatamente, no solo al final.
- Habilita aplicaciones en tiempo real e interfaces de usuario receptivas.
- Uso más eficiente de los recursos de red y computación.

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

- El servidor genera cada mensaje a medida que está listo.
- El cliente recibe e imprime cada fragmento a medida que llega.

**Requisitos:**

- El servidor debe usar una respuesta de transmisión (por ejemplo, `StreamingResponse` en FastAPI).
- El cliente debe procesar la respuesta como una transmisión (`stream=True` en requests).
- El tipo de contenido suele ser `text/event-stream` o `application/octet-stream`.

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

- Usa la pila reactiva de Spring Boot con `Flux` para transmisión.
- `ServerSentEvent` proporciona transmisión estructurada de eventos con tipos de eventos.
- `WebClient` con `bodyToFlux()` habilita el consumo reactivo de transmisiones.
- `delayElements()` simula tiempo de procesamiento entre eventos.
- Los eventos pueden tener tipos (`info`, `result`) para un mejor manejo por parte del cliente.

### Comparación: Transmisión Clásica vs Transmisión MCP

Las diferencias entre cómo funciona la transmisión de manera "clásica" frente a cómo funciona en MCP pueden representarse así:

| Característica          | Transmisión HTTP Clásica       | Transmisión MCP (Notificaciones)   |
|-------------------------|-------------------------------|------------------------------------|
| Respuesta principal     | Fragmentada                  | Única, al final                   |
| Actualizaciones de progreso | Enviadas como fragmentos de datos | Enviadas como notificaciones       |
| Requisitos del cliente  | Debe procesar la transmisión | Debe implementar un manejador de mensajes |
| Caso de uso             | Archivos grandes, transmisiones de tokens de IA | Progreso, registros, retroalimentación en tiempo real |

### Diferencias Clave Observadas

Además, aquí hay algunas diferencias clave:

- **Patrón de Comunicación:**
  - Transmisión HTTP clásica: Usa codificación de transferencia fragmentada para enviar datos en fragmentos.
  - Transmisión MCP: Usa un sistema estructurado de notificaciones con protocolo JSON-RPC.

- **Formato de Mensaje:**
  - HTTP clásico: Fragmentos de texto plano con saltos de línea.
  - MCP: Objetos estructurados LoggingMessageNotification con metadatos.

- **Implementación del Cliente:**
  - HTTP clásico: Cliente simple que procesa respuestas de transmisión.
  - MCP: Cliente más sofisticado con un manejador de mensajes para procesar diferentes tipos de mensajes.

- **Actualizaciones de Progreso:**
  - HTTP clásico: El progreso es parte de la transmisión de respuesta principal.
  - MCP: El progreso se envía mediante mensajes de notificación separados mientras la respuesta principal llega al final.

### Recomendaciones

Hay algunas cosas que recomendamos al elegir entre implementar transmisión clásica (como un endpoint que mostramos anteriormente usando `/stream`) frente a elegir transmisión vía MCP.

- **Para necesidades de transmisión simples:** La transmisión HTTP clásica es más sencilla de implementar y suficiente para necesidades básicas de transmisión.

- **Para aplicaciones complejas e interactivas:** La transmisión MCP proporciona un enfoque más estructurado con metadatos más ricos y separación entre notificaciones y resultados finales.

- **Para aplicaciones de IA:** El sistema de notificaciones de MCP es particularmente útil para tareas de IA de larga duración donde se desea mantener a los usuarios informados sobre el progreso.

## Transmisión en MCP

Bien, ya has visto algunas recomendaciones y comparaciones sobre la diferencia entre transmisión clásica y transmisión en MCP. Vamos a detallar exactamente cómo puedes aprovechar la transmisión en MCP.

Entender cómo funciona la transmisión dentro del marco MCP es esencial para construir aplicaciones receptivas que proporcionen retroalimentación en tiempo real a los usuarios durante operaciones de larga duración.

En MCP, la transmisión no se trata de enviar la respuesta principal en fragmentos, sino de enviar **notificaciones** al cliente mientras una herramienta está procesando una solicitud. Estas notificaciones pueden incluir actualizaciones de progreso, registros u otros eventos.

### Cómo funciona

El resultado principal aún se envía como una única respuesta. Sin embargo, las notificaciones pueden enviarse como mensajes separados durante el procesamiento y, de este modo, actualizar al cliente en tiempo real. El cliente debe ser capaz de manejar y mostrar estas notificaciones.

## ¿Qué es una Notificación?

Dijimos "Notificación", ¿qué significa eso en el contexto de MCP?

Una notificación es un mensaje enviado desde el servidor al cliente para informar sobre el progreso, estado u otros eventos durante una operación de larga duración. Las notificaciones mejoran la transparencia y la experiencia del usuario.

Por ejemplo, un cliente debe enviar una notificación una vez que se haya realizado el saludo inicial con el servidor.

Una notificación se ve así como un mensaje JSON:

```json
{
  jsonrpc: "2.0";
  method: string;
  params?: {
    [key: string]: unknown;
  };
}
```

Las notificaciones pertenecen a un tema en MCP denominado ["Logging"](https://modelcontextprotocol.io/specification/draft/server/utilities/logging).

Para que el registro funcione, el servidor necesita habilitarlo como característica/capacidad de esta manera:

```json
{
  "capabilities": {
    "logging": {}
  }
}
```

> [!NOTE]
> Dependiendo del SDK utilizado, el registro puede estar habilitado por defecto, o puede que necesites habilitarlo explícitamente en la configuración de tu servidor.

Hay diferentes tipos de notificaciones:

| Nivel      | Descripción                     | Caso de Uso Ejemplo             |
|------------|--------------------------------|---------------------------------|
| debug      | Información detallada de depuración | Puntos de entrada/salida de funciones |
| info       | Mensajes informativos generales | Actualizaciones de progreso de operaciones |
| notice     | Eventos normales pero significativos | Cambios de configuración        |
| warning    | Condiciones de advertencia      | Uso de características obsoletas |
| error      | Condiciones de error            | Fallos de operación             |
| critical   | Condiciones críticas            | Fallos de componentes del sistema |
| alert      | Se debe tomar acción inmediata | Detección de corrupción de datos |
| emergency  | El sistema es inutilizable      | Fallo completo del sistema      |

## Implementación de Notificaciones en MCP

Para implementar notificaciones en MCP, necesitas configurar tanto el lado del servidor como el del cliente para manejar actualizaciones en tiempo real. Esto permite que tu aplicación proporcione retroalimentación inmediata a los usuarios durante operaciones de larga duración.

### Lado del Servidor: Enviando Notificaciones

Comencemos con el lado del servidor. En MCP, defines herramientas que pueden enviar notificaciones mientras procesan solicitudes. El servidor usa el objeto de contexto (generalmente `ctx`) para enviar mensajes al cliente.

#### Python

```python
@mcp.tool(description="A tool that sends progress notifications")
async def process_files(message: str, ctx: Context) -> TextContent:
    await ctx.info("Processing file 1/3...")
    await ctx.info("Processing file 2/3...")
    await ctx.info("Processing file 3/3...")
    return TextContent(type="text", text=f"Done: {message}")
```

En el ejemplo anterior, la herramienta `process_files` envía tres notificaciones al cliente mientras procesa cada archivo. El método `ctx.info()` se utiliza para enviar mensajes informativos.

Además, para habilitar notificaciones, asegúrate de que tu servidor use un transporte de transmisión (como `streamable-http`) y tu cliente implemente un manejador de mensajes para procesar notificaciones. Aquí está cómo puedes configurar el servidor para usar el transporte `streamable-http`:

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

En este ejemplo de .NET, la herramienta `ProcessFiles` está decorada con el atributo `Tool` y envía tres notificaciones al cliente mientras procesa cada archivo. El método `ctx.Info()` se utiliza para enviar mensajes informativos.

Para habilitar notificaciones en tu servidor MCP de .NET, asegúrate de usar un transporte de transmisión:

```csharp
var builder = McpBuilder.Create();
await builder
    .UseStreamableHttp() // Enable streamable HTTP transport
    .Build()
    .RunAsync();
```

### Lado del Cliente: Recibiendo Notificaciones

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

En el código anterior, la función `message_handler` verifica si el mensaje entrante es una notificación. Si lo es, imprime la notificación; de lo contrario, lo procesa como un mensaje regular del servidor. También observa cómo se inicializa el `ClientSession` con el `message_handler` para manejar notificaciones entrantes.

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

En este ejemplo de .NET, la función `MessageHandler` verifica si el mensaje entrante es una notificación. Si lo es, imprime la notificación; de lo contrario, lo procesa como un mensaje regular del servidor. El `ClientSession` se inicializa con el manejador de mensajes a través de las `ClientSessionOptions`.

Para habilitar notificaciones, asegúrate de que tu servidor use un transporte de transmisión (como `streamable-http`) y tu cliente implemente un manejador de mensajes para procesar notificaciones.

## Notificaciones de Progreso y Escenarios

Esta sección explica el concepto de notificaciones de progreso en MCP, por qué son importantes y cómo implementarlas usando HTTP transmisible. También encontrarás una tarea práctica para reforzar tu comprensión.

Las notificaciones de progreso son mensajes en tiempo real enviados desde el servidor al cliente durante operaciones de larga duración. En lugar de esperar a que todo el proceso termine, el servidor mantiene al cliente actualizado sobre el estado actual. Esto mejora la transparencia, la experiencia del usuario y facilita la depuración.

**Ejemplo:**

```text

"Processing document 1/10"
"Processing document 2/10"
...
"Processing complete!"

```

### ¿Por qué Usar Notificaciones de Progreso?

Las notificaciones de progreso son esenciales por varias razones:

- **Mejor experiencia del usuario:** Los usuarios ven actualizaciones a medida que el trabajo progresa, no solo al final.
- **Retroalimentación en tiempo real:** Los clientes pueden mostrar barras de progreso o registros, haciendo que la aplicación se sienta receptiva.
- **Facilita la depuración y el monitoreo:** Los desarrolladores y usuarios pueden ver dónde un proceso podría ser lento o estar atascado.

### Cómo Implementar Notificaciones de Progreso

Aquí está cómo puedes implementar notificaciones de progreso en MCP:

- **En el servidor:** Usa `ctx.info()` o `ctx.log()` para enviar notificaciones a medida que se procesa cada elemento. Esto envía un mensaje al cliente antes de que el resultado principal esté listo.
- **En el cliente:** Implementa un manejador de mensajes que escuche y muestre notificaciones a medida que llegan. Este manejador distingue entre notificaciones y el resultado final.

**Ejemplo de Servidor:**

#### Python

```python
@mcp.tool(description="A tool that sends progress notifications")
async def process_files(message: str, ctx: Context) -> TextContent:
    for i in range(1, 11):
        await ctx.info(f"Processing document {i}/10")
    await ctx.info("Processing complete!")
    return TextContent(type="text", text=f"Done: {message}")
```

**Ejemplo de Cliente:**

#### Python

```python
async def message_handler(message):
    if isinstance(message, types.ServerNotification):
        print("NOTIFICATION:", message)
    else:
        print("SERVER MESSAGE:", message)
```

## Consideraciones de Seguridad

Al implementar servidores MCP con transportes basados en HTTP, la seguridad se convierte en una preocupación primordial que requiere atención cuidadosa a múltiples vectores de ataque y mecanismos de protección.

### Resumen

La seguridad es crítica al exponer servidores MCP sobre HTTP. HTTP transmisible introduce nuevas superficies de ataque y requiere configuración cuidadosa.

### Puntos Clave

- **Validación del Encabezado Origin**: Siempre valida el encabezado `Origin` para prevenir ataques de reconfiguración de DNS.
- **Vinculación a Localhost**: Para desarrollo local, vincula servidores a `localhost` para evitar exponerlos a internet pública.
- **Autenticación**: Implementa autenticación (por ejemplo, claves API, OAuth) para despliegues en producción.
- **CORS**: Configura políticas de Cross-Origin Resource Sharing (CORS) para restringir el acceso.
- **HTTPS**: Usa HTTPS en producción para encriptar el tráfico.

### Mejores Prácticas

- Nunca confíes en solicitudes entrantes sin validación.
- Registra y monitorea todos los accesos y errores.
- Actualiza regularmente las dependencias para corregir vulnerabilidades de seguridad.

### Desafíos

- Equilibrar seguridad con facilidad de desarrollo.
- Garantizar compatibilidad con diversos entornos de cliente.

## Actualización de SSE a HTTP Transmisible

Para aplicaciones que actualmente usan Server-Sent Events (SSE), migrar a HTTP transmisible proporciona capacidades mejoradas y una mejor sostenibilidad a largo plazo para tus implementaciones MCP.

### ¿Por qué Actualizar?
Hay dos razones convincentes para actualizar de SSE a Streamable HTTP:

- Streamable HTTP ofrece mejor escalabilidad, compatibilidad y soporte más completo para notificaciones que SSE.
- Es el transporte recomendado para nuevas aplicaciones MCP.

### Pasos para la Migración

Aquí te explicamos cómo migrar de SSE a Streamable HTTP en tus aplicaciones MCP:

- **Actualiza el código del servidor** para usar `transport="streamable-http"` en `mcp.run()`.
- **Actualiza el código del cliente** para usar `streamablehttp_client` en lugar del cliente SSE.
- **Implementa un manejador de mensajes** en el cliente para procesar las notificaciones.
- **Prueba la compatibilidad** con herramientas y flujos de trabajo existentes.

### Mantener la Compatibilidad

Se recomienda mantener la compatibilidad con los clientes SSE existentes durante el proceso de migración. Aquí tienes algunas estrategias:

- Puedes soportar tanto SSE como Streamable HTTP ejecutando ambos transportes en diferentes endpoints.
- Migra gradualmente los clientes al nuevo transporte.

### Desafíos

Asegúrate de abordar los siguientes desafíos durante la migración:

- Garantizar que todos los clientes estén actualizados.
- Manejar las diferencias en la entrega de notificaciones.

## Consideraciones de Seguridad

La seguridad debe ser una prioridad al implementar cualquier servidor, especialmente cuando se utilizan transportes basados en HTTP como Streamable HTTP en MCP.

Al implementar servidores MCP con transportes basados en HTTP, la seguridad se convierte en una preocupación primordial que requiere atención cuidadosa a múltiples vectores de ataque y mecanismos de protección.

### Descripción General

La seguridad es fundamental al exponer servidores MCP a través de HTTP. Streamable HTTP introduce nuevas superficies de ataque y requiere una configuración cuidadosa.

Aquí tienes algunas consideraciones clave de seguridad:

- **Validación del encabezado Origin**: Siempre valida el encabezado `Origin` para prevenir ataques de DNS rebinding.
- **Vinculación a Localhost**: Para el desarrollo local, vincula los servidores a `localhost` para evitar exponerlos a internet público.
- **Autenticación**: Implementa autenticación (por ejemplo, claves API, OAuth) para despliegues en producción.
- **CORS**: Configura políticas de Cross-Origin Resource Sharing (CORS) para restringir el acceso.
- **HTTPS**: Usa HTTPS en producción para cifrar el tráfico.

### Mejores Prácticas

Además, aquí tienes algunas mejores prácticas a seguir al implementar seguridad en tu servidor de streaming MCP:

- Nunca confíes en solicitudes entrantes sin validación.
- Registra y monitorea todos los accesos y errores.
- Actualiza regularmente las dependencias para corregir vulnerabilidades de seguridad.

### Desafíos

Enfrentarás algunos desafíos al implementar seguridad en servidores de streaming MCP:

- Equilibrar la seguridad con la facilidad de desarrollo.
- Garantizar la compatibilidad con diversos entornos de clientes.

### Asignación: Construye tu Propia Aplicación de Streaming MCP

**Escenario:**
Construye un servidor y un cliente MCP donde el servidor procese una lista de elementos (por ejemplo, archivos o documentos) y envíe una notificación por cada elemento procesado. El cliente debe mostrar cada notificación a medida que llega.

**Pasos:**

1. Implementa una herramienta de servidor que procese una lista y envíe notificaciones por cada elemento.
2. Implementa un cliente con un manejador de mensajes para mostrar notificaciones en tiempo real.
3. Prueba tu implementación ejecutando tanto el servidor como el cliente, y observa las notificaciones.

[Solución](./solution/README.md)

## Lecturas Adicionales y Próximos Pasos

Para continuar tu aprendizaje sobre streaming MCP y ampliar tus conocimientos, esta sección proporciona recursos adicionales y sugerencias para construir aplicaciones más avanzadas.

### Lecturas Adicionales

- [Microsoft: Introducción al Streaming HTTP](https://learn.microsoft.com/aspnet/core/fundamentals/http-requests?view=aspnetcore-8.0&WT.mc_id=%3Fwt.mc_id%3DMVP_452430#streaming)
- [Microsoft: Server-Sent Events (SSE)](https://learn.microsoft.com/azure/application-gateway/for-containers/server-sent-events?tabs=server-sent-events-gateway-api&WT.mc_id=%3Fwt.mc_id%3DMVP_452430)
- [Microsoft: CORS en ASP.NET Core](https://learn.microsoft.com/aspnet/core/security/cors?view=aspnetcore-8.0&WT.mc_id=%3Fwt.mc_id%3DMVP_452430)
- [Python requests: Streaming Requests](https://requests.readthedocs.io/en/latest/user/advanced/#streaming-requests)

### Próximos Pasos

- Intenta construir herramientas MCP más avanzadas que utilicen streaming para análisis en tiempo real, chat o edición colaborativa.
- Explora la integración del streaming MCP con frameworks frontend (React, Vue, etc.) para actualizaciones en vivo de la interfaz de usuario.
- Próximo: [Utilizando el Kit de Herramientas de IA para VSCode](../07-aitk/README.md)

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por garantizar la precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o imprecisiones. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o interpretaciones erróneas que puedan surgir del uso de esta traducción.