# Servidor MCP stdio - Solución .NET

> **⚠️ Importante**: Esta solución ha sido actualizada para usar el **transporte stdio** según lo recomendado por la Especificación MCP 2025-06-18. El transporte SSE original ha sido descontinuado.

## Descripción general

Esta solución .NET demuestra cómo construir un servidor MCP utilizando el transporte stdio actual. El transporte stdio es más simple, más seguro y ofrece un mejor rendimiento que el enfoque SSE descontinuado.

## Requisitos previos

- SDK de .NET 9.0 o posterior
- Comprensión básica de la inyección de dependencias en .NET

## Instrucciones de configuración

### Paso 1: Restaurar dependencias

```bash
dotnet restore
```

### Paso 2: Compilar el proyecto

```bash
dotnet build
```

## Ejecutar el servidor

El servidor stdio funciona de manera diferente al antiguo servidor basado en HTTP. En lugar de iniciar un servidor web, se comunica a través de stdin/stdout:

```bash
dotnet run
```

**Importante**: El servidor parecerá estar bloqueado: ¡esto es normal! Está esperando mensajes JSON-RPC desde stdin.

## Probar el servidor

### Método 1: Usar el Inspector MCP (Recomendado)

```bash
npx @modelcontextprotocol/inspector dotnet run
```

Esto hará lo siguiente:
1. Iniciar tu servidor como un subproceso
2. Abrir una interfaz web para pruebas
3. Permitir probar todas las herramientas del servidor de manera interactiva

### Método 2: Pruebas directas desde la línea de comandos

También puedes probar lanzando el Inspector directamente:

```bash
npx @modelcontextprotocol/inspector dotnet run --project .
```

### Herramientas disponibles

El servidor proporciona estas herramientas:

- **AddNumbers(a, b)**: Suma dos números
- **MultiplyNumbers(a, b)**: Multiplica dos números  
- **GetGreeting(name)**: Genera un saludo personalizado
- **GetServerInfo()**: Obtiene información sobre el servidor

### Probar con Claude Desktop

Para usar este servidor con Claude Desktop, agrega esta configuración a tu archivo `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "example-stdio-server": {
      "command": "dotnet",
      "args": ["run", "--project", "path/to/server.csproj"]
    }
  }
}
```

## Estructura del proyecto

```
dotnet/
├── Program.cs           # Main server setup and configuration
├── Tools.cs            # Tool implementations
├── server.csproj       # Project file with dependencies
├── server.sln         # Solution file
├── Properties/         # Project properties
└── README.md          # This file
```

## Diferencias clave respecto a HTTP/SSE

**Transporte stdio (Actual):**
- ✅ Configuración más simple: no se necesita servidor web
- ✅ Mejor seguridad: no hay puntos de acceso HTTP
- ✅ Usa `Host.CreateApplicationBuilder()` en lugar de `WebApplication.CreateBuilder()`
- ✅ `WithStdioTransport()` en lugar de `WithHttpTransport()`
- ✅ Aplicación de consola en lugar de aplicación web
- ✅ Mejor rendimiento

**Transporte HTTP/SSE (Descontinuado):**
- ❌ Requería servidor web ASP.NET Core
- ❌ Necesitaba configuración de enrutamiento con `app.MapMcp()`
- ❌ Configuración y dependencias más complejas
- ❌ Consideraciones adicionales de seguridad
- ❌ Ahora descontinuado en MCP 2025-06-18

## Funcionalidades de desarrollo

- **Inyección de dependencias**: Soporte completo de DI para servicios y registro
- **Registro estructurado**: Registro adecuado en stderr usando `ILogger<T>`
- **Atributos de herramientas**: Definición limpia de herramientas usando atributos `[McpServerTool]`
- **Soporte asincrónico**: Todas las herramientas admiten operaciones asincrónicas
- **Manejo de errores**: Manejo de errores y registro de manera elegante

## Consejos de desarrollo

- Usa `ILogger` para el registro (nunca escribas directamente en stdout)
- Compila con `dotnet build` antes de probar
- Prueba con el Inspector para depuración visual
- Todo el registro se envía automáticamente a stderr
- El servidor maneja señales de apagado de manera elegante

Esta solución sigue la especificación actual de MCP y demuestra las mejores prácticas para la implementación del transporte stdio utilizando .NET.

---

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por garantizar la precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o imprecisiones. El documento original en su idioma nativo debe considerarse como la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o interpretaciones erróneas que puedan surgir del uso de esta traducción.