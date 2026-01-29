# Protocolo de Contexto de Modelo (MCP) Implementación en Python

Este repositorio contiene una implementación en Python del Protocolo de Contexto de Modelo (MCP), que muestra cómo crear una aplicación tanto de servidor como de cliente que se comuniquen usando el estándar MCP.

## Resumen

La implementación de MCP consta de dos componentes principales:

1. **Servidor MCP (`server.py`)** - Un servidor que expone:
   - **Herramientas**: Funciones que pueden ser llamadas de forma remota
   - **Recursos**: Datos que pueden ser recuperados
   - **Prompts**: Plantillas para generar prompts para modelos de lenguaje

2. **Cliente MCP (`client.py`)** - Una aplicación cliente que se conecta al servidor y utiliza sus funcionalidades

## Características

Esta implementación demuestra varias características clave de MCP:

### Herramientas
- `completion` - Genera completados de texto a partir de modelos de IA (simulado)
- `add` - Calculadora simple que suma dos números

### Recursos
- `models://` - Devuelve información sobre los modelos de IA disponibles
- `greeting://{name}` - Devuelve un saludo personalizado para un nombre dado

### Prompts
- `review_code` - Genera un prompt para revisar código

## Instalación

Para usar esta implementación de MCP, instala los paquetes requeridos:

```powershell
pip install mcp-server mcp-client
```

## Ejecutando el Servidor y el Cliente

### Iniciando el Servidor

Ejecuta el servidor en una ventana de terminal:

```powershell
python server.py
```

El servidor también puede ejecutarse en modo desarrollo usando la CLI de MCP:

```powershell
mcp dev server.py
```

O instalarse en Claude Desktop (si está disponible):

```powershell
mcp install server.py
```

### Ejecutando el Cliente

Ejecuta el cliente en otra ventana de terminal:

```powershell
python client.py
```

Esto conectará con el servidor y demostrará todas las funcionalidades disponibles.

### Uso del Cliente

El cliente (`client.py`) demuestra todas las capacidades de MCP:

```powershell
python client.py
```

Esto conectará con el servidor y utilizará todas las funciones, incluyendo herramientas, recursos y prompts. La salida mostrará:

1. Resultado de la herramienta calculadora (5 + 7 = 12)
2. Respuesta de la herramienta completion a "¿Cuál es el sentido de la vida?"
3. Lista de modelos de IA disponibles
4. Saludo personalizado para "MCP Explorer"
5. Plantilla de prompt para revisión de código

## Detalles de la Implementación

El servidor está implementado usando la API `FastMCP`, que provee abstracciones de alto nivel para definir servicios MCP. Aquí hay un ejemplo simplificado de cómo se definen las herramientas:

```python
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers together
    
    Args:
        a: First number
        b: Second number
    
    Returns:
        The sum of the two numbers
    """
    logger.info(f"Adding {a} and {b}")
    return a + b
```

El cliente usa la librería cliente MCP para conectarse y llamar al servidor:

```python
async with stdio_client(server_params) as (reader, writer):
    async with ClientSession(reader, writer) as session:
        await session.initialize()
        result = await session.call_tool("add", arguments={"a": 5, "b": 7})
```

## Aprende Más

Para más información sobre MCP, visita: https://modelcontextprotocol.io/

**Aviso legal**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda la traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o interpretaciones erróneas derivadas del uso de esta traducción.