## Pruebas y Depuración

Antes de comenzar a probar tu servidor MCP, es importante comprender las herramientas disponibles y las mejores prácticas para la depuración. Las pruebas efectivas aseguran que tu servidor se comporte según lo esperado y te ayudan a identificar y resolver problemas rápidamente. La siguiente sección describe los enfoques recomendados para validar tu implementación MCP.

## Resumen

Esta lección cubre cómo seleccionar el enfoque correcto de pruebas y la herramienta de pruebas más efectiva.

## Objetivos de Aprendizaje

Al final de esta lección, podrás:

- Describir varios enfoques para las pruebas.
- Usar diferentes herramientas para probar tu código de manera efectiva.

## Pruebas de Servidores MCP

MCP proporciona herramientas para ayudarte a probar y depurar tus servidores:

- **MCP Inspector**: Una herramienta de línea de comandos que se puede ejecutar tanto como herramienta CLI como visual.
- **Pruebas manuales**: Puedes usar una herramienta como curl para realizar solicitudes web, pero cualquier herramienta capaz de ejecutar HTTP servirá.
- **Pruebas unitarias**: Es posible usar tu marco de pruebas preferido para probar las funcionalidades tanto del servidor como del cliente.

### Usando MCP Inspector

Hemos descrito el uso de esta herramienta en lecciones anteriores, pero hablemos un poco a nivel general. Es una herramienta construida en Node.js y puedes usarla llamando al ejecutable `npx` que descargará e instalará la herramienta temporalmente y la eliminará una vez que termine de ejecutar tu solicitud.

El [MCP Inspector](https://github.com/modelcontextprotocol/inspector) te ayuda a:

- **Descubrir Capacidades del Servidor**: Detectar automáticamente recursos, herramientas y prompts disponibles
- **Probar Ejecución de Herramientas**: Probar diferentes parámetros y ver respuestas en tiempo real
- **Ver Metadatos del Servidor**: Examinar información del servidor, esquemas y configuraciones

Un uso típico de la herramienta es así:

```bash
npx @modelcontextprotocol/inspector node build/index.js
```

El comando anterior inicia un MCP y su interfaz visual y lanza una interfaz web local en tu navegador. Puedes esperar ver un panel que muestra tus servidores MCP registrados, sus herramientas, recursos y prompts disponibles. La interfaz permite probar la ejecución de herramientas interactivamente, inspeccionar metadatos del servidor y ver respuestas en tiempo real, facilitando la validación y depuración de las implementaciones de tu servidor MCP.

Así es como puede verse: ![Inspector](../../../../translated_images/es/connect.141db0b2bd05f096.webp)

También puedes ejecutar esta herramienta en modo CLI, en cuyo caso añades el atributo `--cli`. Aquí hay un ejemplo de cómo ejecutar la herramienta en modo "CLI", que lista todas las herramientas del servidor:

```sh
npx @modelcontextprotocol/inspector --cli node build/index.js --method tools/list
```

### Pruebas Manuales

Además de ejecutar la herramienta inspector para probar las capacidades del servidor, otro enfoque similar es usar un cliente capaz de hacer solicitudes HTTP como, por ejemplo, curl.

Con curl, puedes probar servidores MCP directamente usando solicitudes HTTP:

```bash
# Ejemplo: Metadatos del servidor de prueba
curl http://localhost:3000/v1/metadata

# Ejemplo: Ejecutar una herramienta
curl -X POST http://localhost:3000/v1/tools/execute \
  -H "Content-Type: application/json" \
  -d '{"name": "calculator", "parameters": {"expression": "2+2"}}'
```

Como puedes ver en el uso de curl anterior, usas una solicitud POST para invocar una herramienta usando una carga útil que consiste en el nombre de la herramienta y sus parámetros. Usa el enfoque que mejor se adapte a ti. Las herramientas CLI en general suelen ser más rápidas de usar y se prestan para ser automatizadas, lo cual puede ser útil en un entorno CI/CD.

### Pruebas Unitarias

Crea pruebas unitarias para tus herramientas y recursos para asegurar que funcionen como se espera. Aquí tienes un ejemplo de código de prueba.

```python
import pytest

from mcp.server.fastmcp import FastMCP
from mcp.shared.memory import (
    create_connected_server_and_client_session as create_session,
)

# Marca todo el módulo para pruebas asíncronas
pytestmark = pytest.mark.anyio


async def test_list_tools_cursor_parameter():
    """Test that the cursor parameter is accepted for list_tools.

    Note: FastMCP doesn't currently implement pagination, so this test
    only verifies that the cursor parameter is accepted by the client.
    """

 server = FastMCP("test")

    # Crea un par de herramientas de prueba
    @server.tool(name="test_tool_1")
    async def test_tool_1() -> str:
        """First test tool"""
        return "Result 1"

    @server.tool(name="test_tool_2")
    async def test_tool_2() -> str:
        """Second test tool"""
        return "Result 2"

    async with create_session(server._mcp_server) as client_session:
        # Prueba sin el parámetro cursor (omitido)
        result1 = await client_session.list_tools()
        assert len(result1.tools) == 2

        # Prueba con cursor=None
        result2 = await client_session.list_tools(cursor=None)
        assert len(result2.tools) == 2

        # Prueba con cursor como cadena
        result3 = await client_session.list_tools(cursor="some_cursor_value")
        assert len(result3.tools) == 2

        # Prueba con cursor como cadena vacía
        result4 = await client_session.list_tools(cursor="")
        assert len(result4.tools) == 2
    
```

El código anterior realiza lo siguiente:

- Utiliza el framework pytest que te permite crear pruebas como funciones y usar sentencias assert.
- Crea un servidor MCP con dos herramientas diferentes.
- Usa la sentencia `assert` para verificar que ciertas condiciones se cumplan.

Consulta el [archivo completo aquí](https://github.com/modelcontextprotocol/python-sdk/blob/main/tests/client/test_list_methods_cursor.py)

Dado el archivo anterior, puedes probar tu propio servidor para asegurarte de que las capacidades se creen como deberían.

Todos los SDK principales tienen secciones de prueba similares, por lo que puedes ajustarte a tu entorno de ejecución elegido.

## Ejemplos

- [Calculadora Java](../samples/java/calculator/README.md)
- [Calculadora .Net](../../../../03-GettingStarted/samples/csharp)
- [Calculadora JavaScript](../samples/javascript/README.md)
- [Calculadora TypeScript](../samples/typescript/README.md)
- [Calculadora Python](../../../../03-GettingStarted/samples/python)

## Recursos Adicionales

- [SDK de Python](https://github.com/modelcontextprotocol/python-sdk)

## Qué Sigue

- Siguiente: [Despliegue](../09-deployment/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por humanos. No nos hacemos responsables de ningún malentendido o interpretación errónea que surja del uso de esta traducción.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->