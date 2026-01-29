# Servidor MCP stdio - Solución en TypeScript

> **⚠️ Importante**: Esta solución ha sido actualizada para usar el **transporte stdio** según lo recomendado por la Especificación MCP 2025-06-18. El transporte SSE original ha sido descontinuado.

## Descripción general

Esta solución en TypeScript demuestra cómo construir un servidor MCP utilizando el transporte stdio actual. El transporte stdio es más simple, más seguro y ofrece un mejor rendimiento que el enfoque SSE descontinuado.

## Requisitos previos

- Node.js 18+ o posterior
- Administrador de paquetes npm o yarn

## Instrucciones de configuración

### Paso 1: Instalar las dependencias

```bash
npm install
```

### Paso 2: Construir el proyecto

```bash
npm run build
```

## Ejecutar el servidor

El servidor stdio funciona de manera diferente al antiguo servidor SSE. En lugar de iniciar un servidor web, se comunica a través de stdin/stdout:

```bash
npm start
```

**Importante**: El servidor parecerá estar detenido - ¡esto es normal! Está esperando mensajes JSON-RPC desde stdin.

## Probar el servidor

### Método 1: Usar el MCP Inspector (Recomendado)

```bash
npm run inspector
```

Esto hará lo siguiente:
1. Iniciar tu servidor como un subproceso
2. Abrir una interfaz web para pruebas
3. Permitir probar todas las herramientas del servidor de manera interactiva

### Método 2: Pruebas directas desde la línea de comandos

También puedes probar lanzando el Inspector directamente:

```bash
npx @modelcontextprotocol/inspector node build/index.js
```

### Herramientas disponibles

El servidor proporciona estas herramientas:

- **add(a, b)**: Sumar dos números
- **multiply(a, b)**: Multiplicar dos números  
- **get_greeting(name)**: Generar un saludo personalizado
- **get_server_info()**: Obtener información sobre el servidor

### Pruebas con Claude Desktop

Para usar este servidor con Claude Desktop, agrega esta configuración a tu archivo `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "example-stdio-server": {
      "command": "node",
      "args": ["path/to/build/index.js"]
    }
  }
}
```

## Estructura del proyecto

```
typescript/
├── src/
│   └── index.ts          # Main server implementation
├── build/                # Compiled JavaScript (generated)
├── package.json          # Project configuration
├── tsconfig.json         # TypeScript configuration
└── README.md            # This file
```

## Diferencias clave con SSE

**Transporte stdio (Actual):**
- ✅ Configuración más simple - no se necesita un servidor HTTP
- ✅ Mejor seguridad - sin puntos de acceso HTTP
- ✅ Comunicación basada en subprocesos
- ✅ JSON-RPC a través de stdin/stdout
- ✅ Mejor rendimiento

**Transporte SSE (Descontinuado):**
- ❌ Requería configuración de servidor Express
- ❌ Necesitaba enrutamiento complejo y gestión de sesiones
- ❌ Más dependencias (Express, manejo de HTTP)
- ❌ Consideraciones adicionales de seguridad
- ❌ Ahora descontinuado en MCP 2025-06-18

## Consejos para el desarrollo

- Usa `console.error()` para registrar mensajes (nunca `console.log()` ya que escribe en stdout)
- Construye con `npm run build` antes de probar
- Prueba con el Inspector para depuración visual
- Asegúrate de que todos los mensajes JSON estén correctamente formateados
- El servidor maneja automáticamente el cierre ordenado en SIGINT/SIGTERM

Esta solución sigue la especificación actual de MCP y demuestra las mejores prácticas para la implementación del transporte stdio utilizando TypeScript.

---

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por garantizar la precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o imprecisiones. El documento original en su idioma nativo debe considerarse como la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o interpretaciones erróneas que puedan surgir del uso de esta traducción.