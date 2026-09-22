# Raíces MCP (Funcionalidad heredada)

> [!WARNING]
> Las raíces están obsoletas desde MCP `2026-07-28`. Permanece en esta revisión para 
> compatibilidad y son elegibles para su eliminación en la primera revisión de especificación 
> publicada en o después del 28 de julio de 2027. Las nuevas implementaciones deben pasar 
> directorios o archivos mediante parámetros de herramientas, URIs de recursos o 
> configuración del servidor.

## Visión general

Las raíces permiten a un cliente MCP indicarle a un servidor qué ubicaciones del sistema de archivos son relevantes
para la solicitud actual. Una raíz contiene un URI `file://` obligatorio y un nombre legible opcional.


sesiones de protocolo, ni un mecanismo de control de acceso. El protocolo no
garantiza que un servidor se mantenga dentro de las raíces listadas.


## Objetivos de aprendizaje

Al final de esta lección, podrás:

- Explicar qué representan las raíces MCP y qué no representan.
- Reconocer el flujo multi-interacción `roots/list` actual.
- Aplicar controles de seguridad independientemente de las raíces.
- Migrar nuevas implementaciones a alternativas soportadas.

## Datos de raíces

Un cliente devuelve cada raíz como un URI `file://` con un nombre de visualización opcional:

```json
{
  "roots": [
    {
      "uri": "file:///home/user/projects/weather-service",
      "name": "Weather Service"
    }
  ]
}
```

Los clientes deben exponer solo ubicaciones aprobadas por el usuario. Los servidores deben tratar
el resultado como una guía sobre archivos relevantes, no como prueba de autorización.

## Flujo MCP 2026-07-28

Un cliente que soporta raíces declara la capacidad en cada solicitud:

```json
{
  "_meta": {
    "io.modelcontextprotocol/clientCapabilities": {
      "roots": {}
    }
  }
}
```

Mientras procesa una solicitud del cliente, un servidor puede devolver un
`InputRequiredResult` que contiene una solicitud de entrada `roots/list`:

```json
{
  "resultType": "input_required",
  "inputRequests": {
    "workspaceRoots": {
      "method": "roots/list"
    }
  },
  "requestState": "opaque-state-from-server"
}
```

El cliente recopila las raíces aprobadas y reintenta la solicitud original con las
`inputResponses` correspondientes y el `requestState` sin cambios. Este patrón de múltiples interacciones
mantiene el protocolo sin estado; no hay un apretón de manos `initialize` ni
sesión a nivel de protocolo.

## Comportamiento heredado 2025-11-25

En MCP `2025-11-25`, los clientes anunciaban raíces durante la inicialización. Un servidor
podía emitir una solicitud directa `roots/list`, y un cliente podía enviar
`notifications/roots/list_changed` cuando sus raíces cambiaban.

Ese ciclo de vida es un comportamiento heredado. No combines sus ejemplos de inicialización o
notificación con una implementación `2026-07-28`.

## Reemplazos recomendados

### Parámetros de herramientas

Haz explícito el directorio o archivo requerido en el esquema de la herramienta:

```json
{
  "name": "analyze_project",
  "inputSchema": {
    "type": "object",
    "properties": {
      "projectDirectory": {
        "type": "string",
        "description": "Approved project directory to analyze"
      }
    },
    "required": ["projectDirectory"]
  }
}
```

### URIs de recursos

Usa Recursos MCP cuando el servidor pueda exponer los archivos relevantes mediante URIs
estables. Esto mantiene el descubrimiento y recuperación explícitos.

### Configuración del servidor

Para despliegues fijos, configura los directorios permitidos al arrancar el servidor.
Esto suele ser más claro que descubrirlos durante una llamada de herramienta.

## Requisitos de seguridad

Sea cual sea el reemplazo que elijas:

- Obtén el consentimiento del usuario antes de exponer ubicaciones del sistema de archivos.
- Canonicaliza y valida rutas para prevenir traversales.
- Aplica autorización y sandboxing independientemente de los valores de raíz.
- Verifica permisos al acceder a un archivo, no solo cuando se liste.
- Evita devolver rutas sensibles en registros o mensajes de error.

## Puntos clave

- Las raíces describen ubicaciones relevantes del sistema de archivos; no almacenan el estado de la conversación.

- Las raíces son una guía, no una frontera de control de acceso.
- MCP `2026-07-28` lleva la capacidad por solicitud y usa
  `InputRequiredResult` para `roots/list`.
- Las nuevas implementaciones deben usar parámetros de herramientas, URIs de recursos o
  configuración del servidor en su lugar.

## Recursos adicionales

- [Raíces en MCP 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/client/roots)
- [Registro de características obsoletas](https://modelcontextprotocol.io/specification/2026-07-28/deprecated)
- [Qué ha cambiado en MCP: La especificación 2026-07-28](../../01-CoreConcepts/mcp-2026-07-28.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Descargo de responsabilidad**:
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional humana. No somos responsables de cualquier malentendido o interpretación errónea que surja del uso de esta traducción.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->