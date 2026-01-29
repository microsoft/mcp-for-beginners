# Demo de Streaming HTTP de Calculadora

Este proyecto demuestra el streaming HTTP usando Server-Sent Events (SSE) con Spring Boot WebFlux. Consiste en dos aplicaciones:

- **Calculator Server**: Un servicio web reactivo que realiza cálculos y transmite resultados usando SSE
- **Calculator Client**: Una aplicación cliente que consume el endpoint de streaming

## Requisitos Previos

- Java 17 o superior
- Maven 3.6 o superior

## Estructura del Proyecto

```
java/
├── calculator-server/     # Spring Boot server with SSE endpoint
│   ├── src/main/java/com/example/calculatorserver/
│   │   ├── CalculatorServerApplication.java
│   │   └── CalculatorController.java
│   └── pom.xml
├── calculator-client/     # Spring Boot client application
│   ├── src/main/java/com/example/calculatorclient/
│   │   └── CalculatorClientApplication.java
│   └── pom.xml
└── README.md
```

## Cómo Funciona

1. El **Calculator Server** expone un endpoint `/calculate` que:
   - Acepta parámetros de consulta: `a` (número), `b` (número), `op` (operación)
   - Operaciones soportadas: `add`, `sub`, `mul`, `div`
   - Devuelve Server-Sent Events con el progreso del cálculo y el resultado

2. El **Calculator Client** se conecta al servidor y:
   - Realiza una solicitud para calcular `7 * 5`
   - Consume la respuesta en streaming
   - Imprime cada evento en la consola

## Ejecutando las Aplicaciones

### Opción 1: Usando Maven (Recomendado)

#### 1. Iniciar el Calculator Server

Abre una terminal y navega al directorio del servidor:

```bash
cd calculator-server
mvn clean package
mvn spring-boot:run
```

El servidor se iniciará en `http://localhost:8080`

Deberías ver una salida similar a:
```
Started CalculatorServerApplication in X.XXX seconds
Netty started on port 8080 (http)
```

#### 2. Ejecutar el Calculator Client

Abre una **nueva terminal** y navega al directorio del cliente:

```bash
cd calculator-client
mvn clean package
mvn spring-boot:run
```

El cliente se conectará al servidor, realizará el cálculo y mostrará los resultados en streaming.

### Opción 2: Usando Java directamente

#### 1. Compilar y ejecutar el servidor:

```bash
cd calculator-server
mvn clean package
java -jar target/calculator-server-0.0.1-SNAPSHOT.jar
```

#### 2. Compilar y ejecutar el cliente:

```bash
cd calculator-client
mvn clean package
java -jar target/calculator-client-0.0.1-SNAPSHOT.jar
```

## Probando el Servidor Manualmente

También puedes probar el servidor usando un navegador web o curl:

### Usando un navegador web:
Visita: `http://localhost:8080/calculate?a=10&b=5&op=add`

### Usando curl:
```bash
curl "http://localhost:8080/calculate?a=10&b=5&op=add" -H "Accept: text/event-stream"
```

## Salida Esperada

Al ejecutar el cliente, deberías ver una salida en streaming similar a:

```
event:info
data:Calculating: 7.0 mul 5.0

event:result
data:35.0
```

## Operaciones Soportadas

- `add` - Suma (a + b)
- `sub` - Resta (a - b)
- `mul` - Multiplicación (a * b)
- `div` - División (a / b, devuelve NaN si b = 0)

## Referencia de la API

### GET /calculate

**Parámetros:**
- `a` (requerido): Primer número (double)
- `b` (requerido): Segundo número (double)
- `op` (requerido): Operación (`add`, `sub`, `mul`, `div`)

**Respuesta:**
- Content-Type: `text/event-stream`
- Devuelve Server-Sent Events con el progreso del cálculo y el resultado

**Ejemplo de Solicitud:**
```
GET /calculate?a=7&b=5&op=mul HTTP/1.1
Host: localhost:8080
Accept: text/event-stream
```

**Ejemplo de Respuesta:**
```
event: info
data: Calculating: 7.0 mul 5.0

event: result
data: 35.0
```

## Solución de Problemas

### Problemas Comunes

1. **Puerto 8080 ya en uso**
   - Detén cualquier otra aplicación que esté usando el puerto 8080
   - O cambia el puerto del servidor en `calculator-server/src/main/resources/application.yml`

2. **Conexión rechazada**
   - Asegúrate de que el servidor esté en ejecución antes de iniciar el cliente
   - Verifica que el servidor haya arrancado correctamente en el puerto 8080

3. **Problemas con nombres de parámetros**
   - Este proyecto incluye configuración del compilador Maven con la bandera `-parameters`
   - Si tienes problemas con el enlace de parámetros, asegúrate de que el proyecto esté compilado con esta configuración

### Detener las Aplicaciones

- Presiona `Ctrl+C` en la terminal donde se está ejecutando cada aplicación
- O usa `mvn spring-boot:stop` si se está ejecutando como proceso en segundo plano

## Tecnología Utilizada

- **Spring Boot 3.3.1** - Framework de aplicación
- **Spring WebFlux** - Framework web reactivo
- **Project Reactor** - Biblioteca de streams reactivos
- **Netty** - Servidor de I/O no bloqueante
- **Maven** - Herramienta de construcción
- **Java 17+** - Lenguaje de programación

## Próximos Pasos

Intenta modificar el código para:
- Agregar más operaciones matemáticas
- Incluir manejo de errores para operaciones inválidas
- Añadir registro de solicitudes/respuestas
- Implementar autenticación
- Agregar pruebas unitarias

**Aviso legal**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda la traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o interpretaciones erróneas derivadas del uso de esta traducción.