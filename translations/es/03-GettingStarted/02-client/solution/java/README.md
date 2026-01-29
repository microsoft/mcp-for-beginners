# Cliente Java MCP - Demo Calculadora

Este proyecto muestra cómo crear un cliente Java que se conecta e interactúa con un servidor MCP (Model Context Protocol). En este ejemplo, nos conectaremos al servidor de calculadora del Capítulo 01 y realizaremos varias operaciones matemáticas.

## Requisitos previos

Antes de ejecutar este cliente, necesitas:

1. **Iniciar el Servidor de Calculadora** del Capítulo 01:
   - Navega al directorio del servidor de calculadora: `03-GettingStarted/01-first-server/solution/java/`
   - Compila y ejecuta el servidor de calculadora:
     ```cmd
     cd ..\01-first-server\solution\java
     .\mvnw clean install -DskipTests
     java -jar target\calculator-server-0.0.1-SNAPSHOT.jar
     ```
   - El servidor debería estar corriendo en `http://localhost:8080`

2. Tener instalado **Java 21 o superior** en tu sistema  
3. Tener **Maven** (incluido mediante Maven Wrapper)

## ¿Qué es el SDKClient?

El `SDKClient` es una aplicación Java que demuestra cómo:
- Conectarse a un servidor MCP usando transporte Server-Sent Events (SSE)
- Listar las herramientas disponibles en el servidor
- Llamar remotamente a varias funciones de la calculadora
- Manejar las respuestas y mostrar los resultados

## Cómo Funciona

El cliente utiliza el framework Spring AI MCP para:

1. **Establecer Conexión**: Crea un transporte WebFlux SSE para conectarse al servidor de calculadora  
2. **Inicializar Cliente**: Configura el cliente MCP y establece la conexión  
3. **Descubrir Herramientas**: Lista todas las operaciones disponibles de la calculadora  
4. **Ejecutar Operaciones**: Llama a varias funciones matemáticas con datos de ejemplo  
5. **Mostrar Resultados**: Presenta los resultados de cada cálculo

## Estructura del Proyecto

```
src/
└── main/
    └── java/
        └── com/
            └── microsoft/
                └── mcp/
                    └── sample/
                        └── client/
                            └── SDKClient.java    # Main client implementation
```

## Dependencias Clave

El proyecto utiliza las siguientes dependencias principales:

```xml
<dependency>
    <groupId>org.springframework.ai</groupId>
    <artifactId>spring-ai-starter-mcp-server-webflux</artifactId>
</dependency>
```

Esta dependencia provee:  
- `McpClient` - La interfaz principal del cliente  
- `WebFluxSseClientTransport` - Transporte SSE para comunicación web  
- Esquemas del protocolo MCP y tipos de solicitud/respuesta

## Construyendo el Proyecto

Construye el proyecto usando el wrapper de Maven:

```cmd
.\mvnw clean install
```

## Ejecutando el Cliente

```cmd
java -jar .\target\calculator-client-0.0.1-SNAPSHOT.jar
```

**Nota**: Asegúrate de que el servidor de calculadora esté corriendo en `http://localhost:8080` antes de ejecutar cualquiera de estos comandos.

## Qué Hace el Cliente

Al ejecutar el cliente, este:

1. **Se conecta** al servidor de calculadora en `http://localhost:8080`  
2. **Lista las Herramientas** - Muestra todas las operaciones disponibles de la calculadora  
3. **Realiza Cálculos**:  
   - Suma: 5 + 3 = 8  
   - Resta: 10 - 4 = 6  
   - Multiplicación: 6 × 7 = 42  
   - División: 20 ÷ 4 = 5  
   - Potencia: 2^8 = 256  
   - Raíz Cuadrada: √16 = 4  
   - Valor Absoluto: |-5.5| = 5.5  
   - Ayuda: Muestra las operaciones disponibles

## Salida Esperada

```
Available Tools = ListToolsResult[tools=[Tool[name=add, description=Add two numbers together, ...], ...]]
Add Result = CallToolResult[content=[TextContent[text="5,00 + 3,00 = 8,00"]], isError=false]
Subtract Result = CallToolResult[content=[TextContent[text="10,00 - 4,00 = 6,00"]], isError=false]
Multiply Result = CallToolResult[content=[TextContent[text="6,00 * 7,00 = 42,00"]], isError=false]
Divide Result = CallToolResult[content=[TextContent[text="20,00 / 4,00 = 5,00"]], isError=false]
Power Result = CallToolResult[content=[TextContent[text="2,00 ^ 8,00 = 256,00"]], isError=false]
Square Root Result = CallToolResult[content=[TextContent[text="√16,00 = 4,00"]], isError=false]
Absolute Result = CallToolResult[content=[TextContent[text="|-5,50| = 5,50"]], isError=false]
Help = CallToolResult[content=[TextContent[text="Basic Calculator MCP Service\n\nAvailable operations:\n1. add(a, b) - Adds two numbers\n2. subtract(a, b) - Subtracts the second number from the first\n..."]], isError=false]
```

**Nota**: Puede que veas advertencias de Maven sobre hilos activos al final; esto es normal en aplicaciones reactivas y no indica un error.

## Entendiendo el Código

### 1. Configuración del Transporte  
```java
var transport = new WebFluxSseClientTransport(WebClient.builder().baseUrl("http://localhost:8080"));
```  
Esto crea un transporte SSE (Server-Sent Events) que se conecta al servidor de calculadora.

### 2. Creación del Cliente  
```java
var client = McpClient.sync(this.transport).build();
client.initialize();
```  
Crea un cliente MCP síncrono e inicializa la conexión.

### 3. Llamada a Herramientas  
```java
CallToolResult resultAdd = client.callTool(new CallToolRequest("add", Map.of("a", 5.0, "b", 3.0)));
```  
Llama a la herramienta "add" con los parámetros a=5.0 y b=3.0.

## Solución de Problemas

### Servidor No Está Corriendo  
Si recibes errores de conexión, asegúrate de que el servidor de calculadora del Capítulo 01 esté en ejecución:  
```
Error: Connection refused
```  
**Solución**: Inicia primero el servidor de calculadora.

### Puerto Ya Está en Uso  
Si el puerto 8080 está ocupado:  
```
Error: Address already in use
```  
**Solución**: Detén otras aplicaciones que usen el puerto 8080 o modifica el servidor para usar otro puerto.

### Errores de Compilación  
Si encuentras errores al compilar:  
```cmd
.\mvnw clean install -DskipTests
```

## Aprende Más

- [Documentación Spring AI MCP](https://docs.spring.io/spring-ai/reference/api/mcp/)  
- [Especificación Model Context Protocol](https://modelcontextprotocol.io/)  
- [Documentación Spring WebFlux](https://docs.spring.io/spring-framework/docs/current/reference/html/web-reactive.html)

**Aviso legal**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda la traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o interpretaciones erróneas derivadas del uso de esta traducción.