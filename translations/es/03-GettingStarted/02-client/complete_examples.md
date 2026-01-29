# Ejemplos Completos de Clientes MCP

Este directorio contiene ejemplos completos y funcionales de clientes MCP en diferentes lenguajes de programación. Cada cliente demuestra toda la funcionalidad descrita en el tutorial principal README.md.

## Clientes Disponibles

### 1. Cliente Java (`client_example_java.java`)

- **Transporte**: SSE (Eventos Enviados por el Servidor) sobre HTTP
- **Servidor Objetivo**: `http://localhost:8080`
- **Características**:
  - Establecimiento de conexión y ping
  - Listado de herramientas
  - Operaciones de calculadora (sumar, restar, multiplicar, dividir, ayuda)
  - Manejo de errores y extracción de resultados

**Para ejecutar:**

```bash
# Ensure your MCP server is running on localhost:8080
javac client_example_java.java
java client_example_java
```

### 2. Cliente C# (`client_example_csharp.cs`)

- **Transporte**: Stdio (Entrada/Salida Estándar)
- **Servidor Objetivo**: Servidor MCP local de .NET mediante dotnet run
- **Características**:
  - Inicio automático del servidor mediante transporte stdio
  - Listado de herramientas y recursos
  - Operaciones de calculadora
  - Análisis de resultados en JSON
  - Manejo de errores integral

**Para ejecutar:**

```bash
dotnet run
```

### 3. Cliente TypeScript (`client_example_typescript.ts`)

- **Transporte**: Stdio (Entrada/Salida Estándar)
- **Servidor Objetivo**: Servidor MCP local de Node.js
- **Características**:
  - Soporte completo del protocolo MCP
  - Operaciones con herramientas, recursos y prompts
  - Operaciones de calculadora
  - Lectura de recursos y ejecución de prompts
  - Manejo robusto de errores

**Para ejecutar:**

```bash
# First compile TypeScript (if needed)
npm run build

# Then run the client
npm run client
# or
node client_example_typescript.js
```

### 4. Cliente Python (`client_example_python.py`)

- **Transporte**: Stdio (Entrada/Salida Estándar)  
- **Servidor Objetivo**: Servidor MCP local de Python
- **Características**:
  - Patrón async/await para operaciones
  - Descubrimiento de herramientas y recursos
  - Pruebas de operaciones de calculadora
  - Lectura de contenido de recursos
  - Organización basada en clases

**Para ejecutar:**

```bash
python client_example_python.py
```

## Características Comunes en Todos los Clientes

Cada implementación de cliente demuestra:

1. **Gestión de Conexión**
   - Establecimiento de conexión con el servidor MCP
   - Manejo de errores de conexión
   - Limpieza adecuada y gestión de recursos

2. **Descubrimiento del Servidor**
   - Listado de herramientas disponibles
   - Listado de recursos disponibles (cuando sea compatible)
   - Listado de prompts disponibles (cuando sea compatible)

3. **Invocación de Herramientas**
   - Operaciones básicas de calculadora (sumar, restar, multiplicar, dividir)
   - Comando de ayuda para información del servidor
   - Paso adecuado de argumentos y manejo de resultados

4. **Manejo de Errores**
   - Errores de conexión
   - Errores en la ejecución de herramientas
   - Fallos controlados y retroalimentación al usuario

5. **Procesamiento de Resultados**
   - Extracción de contenido de texto de las respuestas
   - Formateo de salida para mejor legibilidad
   - Manejo de diferentes formatos de respuesta

## Requisitos Previos

Antes de ejecutar estos clientes, asegúrate de tener:

1. **El servidor MCP correspondiente en ejecución** (desde `../01-first-server/`)
2. **Dependencias necesarias instaladas** para el lenguaje elegido
3. **Conectividad de red adecuada** (para transportes basados en HTTP)

## Diferencias Clave Entre Implementaciones

| Lenguaje   | Transporte | Inicio del Servidor | Modelo Async | Bibliotecas Clave       |
|------------|-----------|---------------------|--------------|-------------------------|
| Java       | SSE/HTTP  | Externo             | Sincrónico   | WebFlux, MCP SDK        |
| C#         | Stdio     | Automático          | Async/Await  | .NET MCP SDK            |
| TypeScript | Stdio     | Automático          | Async/Await  | Node MCP SDK            |
| Python     | Stdio     | Automático          | AsyncIO      | Python MCP SDK          |
| Rust       | Stdio     | Automático          | Async/Await  | Rust MCP SDK, Tokio     |

## Próximos Pasos

Después de explorar estos ejemplos de clientes:

1. **Modifica los clientes** para agregar nuevas características u operaciones
2. **Crea tu propio servidor** y pruébalo con estos clientes
3. **Experimenta con diferentes transportes** (SSE vs. Stdio)
4. **Construye una aplicación más compleja** que integre la funcionalidad MCP

## Resolución de Problemas

### Problemas Comunes

1. **Conexión rechazada**: Asegúrate de que el servidor MCP esté ejecutándose en el puerto/ruta esperados
2. **Módulo no encontrado**: Instala el SDK MCP requerido para tu lenguaje
3. **Permiso denegado**: Verifica los permisos de archivo para el transporte stdio
4. **Herramienta no encontrada**: Confirma que el servidor implemente las herramientas esperadas

### Consejos de Depuración

1. **Habilita el registro detallado** en tu SDK MCP
2. **Revisa los registros del servidor** para mensajes de error
3. **Verifica los nombres y firmas de las herramientas** entre el cliente y el servidor
4. **Prueba primero con MCP Inspector** para validar la funcionalidad del servidor

## Documentación Relacionada

- [Tutorial Principal de Clientes](./README.md)
- [Ejemplos de Servidores MCP](../../../../03-GettingStarted/01-first-server)
- [MCP con Integración LLM](../../../../03-GettingStarted/03-llm-client)
- [Documentación Oficial de MCP](https://modelcontextprotocol.io/)

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Si bien nos esforzamos por lograr precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o imprecisiones. El documento original en su idioma nativo debe considerarse como la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o interpretaciones erróneas que puedan surgir del uso de esta traducción.