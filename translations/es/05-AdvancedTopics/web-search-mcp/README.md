# Lección: Construyendo un Servidor MCP de Búsqueda Web

Este capítulo muestra cómo construir un agente de IA real que se integra con APIs externas, maneja diversos tipos de datos, gestiona errores y orquesta múltiples herramientas, todo en un formato listo para producción. Verás:

- **Integración con APIs externas que requieren autenticación**
- **Manejo de diversos tipos de datos desde múltiples endpoints**
- **Estrategias robustas de manejo de errores y registro**
- **Orquestación de múltiples herramientas en un solo servidor**

Al final, tendrás experiencia práctica con patrones y buenas prácticas esenciales para aplicaciones avanzadas de IA y potenciadas por LLM.

## Introducción

En esta lección aprenderás a construir un servidor y cliente MCP avanzados que extienden las capacidades de LLM con datos web en tiempo real usando SerpAPI. Esta es una habilidad clave para desarrollar agentes de IA dinámicos que puedan acceder a información actualizada de la web.

## Objetivos de Aprendizaje

Al finalizar esta lección, podrás:

- Integrar APIs externas (como SerpAPI) de forma segura en un servidor MCP
- Implementar múltiples herramientas para búsqueda web, noticias, productos y preguntas y respuestas
- Analizar y formatear datos estructurados para el consumo de LLM
- Manejar errores y gestionar límites de tasa de API de manera efectiva
- Construir y probar clientes MCP tanto automatizados como interactivos

## Servidor MCP de Búsqueda Web

Esta sección presenta la arquitectura y características del Servidor MCP de Búsqueda Web. Verás cómo FastMCP y SerpAPI se usan juntos para ampliar las capacidades de LLM con datos web en tiempo real.

### Resumen

Esta implementación cuenta con cuatro herramientas que demuestran la capacidad de MCP para manejar tareas diversas impulsadas por APIs externas de forma segura y eficiente:

- **general_search**: Para resultados web generales
- **news_search**: Para titulares recientes
- **product_search**: Para datos de comercio electrónico
- **qna**: Para fragmentos de preguntas y respuestas

### Características
- **Ejemplos de Código**: Incluye bloques de código específicos para Python (y fácilmente extensibles a otros lenguajes) usando pivotes de código para mayor claridad

### Python

```python
# Example usage of the general_search tool
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def run_search():
    server_params = StdioServerParameters(
        command="python",
        args=["server.py"],
    )
    async with stdio_client(server_params) as (reader, writer):
        async with ClientSession(reader, writer) as session:
            await session.initialize()
            result = await session.call_tool("general_search", arguments={"query": "open source LLMs"})
            print(result)
```

---

Antes de ejecutar el cliente, es útil entender qué hace el servidor. El archivo [`server.py`](../../../../05-AdvancedTopics/web-search-mcp/server.py) implementa el servidor MCP, exponiendo herramientas para búsqueda web, noticias, productos y preguntas y respuestas mediante la integración con SerpAPI. Maneja las solicitudes entrantes, gestiona las llamadas a la API, analiza las respuestas y devuelve resultados estructurados al cliente.

Puedes revisar la implementación completa en [`server.py`](../../../../05-AdvancedTopics/web-search-mcp/server.py).

Aquí tienes un breve ejemplo de cómo el servidor define y registra una herramienta:

### Servidor Python

```python
# server.py (excerpt)
from mcp.server import MCPServer, Tool

async def general_search(query: str):
    # ...implementation...

server = MCPServer()
server.add_tool(Tool("general_search", general_search))

if __name__ == "__main__":
    server.run()
```

---

- **Integración con API Externa**: Demuestra el manejo seguro de claves API y solicitudes externas
- **Análisis de Datos Estructurados**: Muestra cómo transformar respuestas de API en formatos amigables para LLM
- **Manejo de Errores**: Manejo robusto de errores con registro adecuado
- **Cliente Interactivo**: Incluye pruebas automatizadas y un modo interactivo para pruebas
- **Gestión de Contexto**: Aprovecha MCP Context para registro y seguimiento de solicitudes

## Requisitos Previos

Antes de comenzar, asegúrate de que tu entorno esté configurado correctamente siguiendo estos pasos. Esto garantizará que todas las dependencias estén instaladas y tus claves API configuradas adecuadamente para un desarrollo y pruebas sin problemas.

- Python 3.8 o superior
- Clave API de SerpAPI (Regístrate en [SerpAPI](https://serpapi.com/) - disponible plan gratuito)

## Instalación

Para comenzar, sigue estos pasos para configurar tu entorno:

1. Instala las dependencias usando uv (recomendado) o pip:

```bash
# Using uv (recommended)
uv pip install -r requirements.txt

# Using pip
pip install -r requirements.txt
```

2. Crea un archivo `.env` en la raíz del proyecto con tu clave SerpAPI:

```
SERPAPI_KEY=your_serpapi_key_here
```

## Uso

El Servidor MCP de Búsqueda Web es el componente central que expone herramientas para búsqueda web, noticias, productos y preguntas y respuestas mediante la integración con SerpAPI. Maneja las solicitudes entrantes, gestiona las llamadas a la API, analiza las respuestas y devuelve resultados estructurados al cliente.

Puedes revisar la implementación completa en [`server.py`](../../../../05-AdvancedTopics/web-search-mcp/server.py).

### Ejecutando el Servidor

Para iniciar el servidor MCP, usa el siguiente comando:

```bash
python server.py
```

El servidor funcionará como un servidor MCP basado en stdio al que el cliente puede conectarse directamente.

### Modos del Cliente

El cliente (`client.py`) soporta dos modos para interactuar con el servidor MCP:

- **Modo normal**: Ejecuta pruebas automatizadas que ejercitan todas las herramientas y verifican sus respuestas. Esto es útil para comprobar rápidamente que el servidor y las herramientas funcionan como se espera.
- **Modo interactivo**: Inicia una interfaz basada en menú donde puedes seleccionar y llamar herramientas manualmente, ingresar consultas personalizadas y ver resultados en tiempo real. Ideal para explorar las capacidades del servidor y experimentar con diferentes entradas.

Puedes revisar la implementación completa en [`client.py`](../../../../05-AdvancedTopics/web-search-mcp/client.py).

### Ejecutando el Cliente

Para ejecutar las pruebas automatizadas (esto iniciará el servidor automáticamente):

```bash
python client.py
```

O para ejecutar en modo interactivo:

```bash
python client.py --interactive
```

### Pruebas con Diferentes Métodos

Existen varias formas de probar e interactuar con las herramientas que ofrece el servidor, según tus necesidades y flujo de trabajo.

#### Escribiendo Scripts de Prueba Personalizados con el SDK MCP para Python
También puedes crear tus propios scripts de prueba usando el SDK MCP para Python:

# [Python](../../../../05-AdvancedTopics/web-search-mcp)

```python
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def test_custom_query():
    server_params = StdioServerParameters(
        command="python",
        args=["server.py"],
    )
    
    async with stdio_client(server_params) as (reader, writer):
        async with ClientSession(reader, writer) as session:
            await session.initialize()
            # Call tools with your custom parameters
            result = await session.call_tool("general_search", 
                                           arguments={"query": "your custom query"})
            # Process the result
```

---

En este contexto, un "script de prueba" es un programa Python personalizado que escribes para actuar como cliente del servidor MCP. En lugar de ser una prueba unitaria formal, este script te permite conectarte programáticamente al servidor, llamar a cualquiera de sus herramientas con los parámetros que elijas e inspeccionar los resultados. Este enfoque es útil para:
- Prototipar y experimentar con llamadas a herramientas
- Validar cómo responde el servidor a diferentes entradas
- Automatizar invocaciones repetidas de herramientas
- Construir tus propios flujos de trabajo o integraciones sobre el servidor MCP

Puedes usar scripts de prueba para probar rápidamente nuevas consultas, depurar el comportamiento de las herramientas o incluso como punto de partida para automatizaciones más avanzadas. A continuación, un ejemplo de cómo usar el SDK MCP para Python para crear dicho script:

## Descripciones de Herramientas

Puedes usar las siguientes herramientas proporcionadas por el servidor para realizar diferentes tipos de búsquedas y consultas. Cada herramienta se describe a continuación con sus parámetros y un ejemplo de uso.

Esta sección ofrece detalles sobre cada herramienta disponible y sus parámetros.

### general_search

Realiza una búsqueda web general y devuelve resultados formateados.

**Cómo llamar a esta herramienta:**

Puedes llamar a `general_search` desde tu propio script usando el SDK MCP para Python, o de forma interactiva usando el Inspector o el modo interactivo del cliente. Aquí tienes un ejemplo de código usando el SDK:

# [Ejemplo en Python](../../../../05-AdvancedTopics/web-search-mcp)

```python
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def run_general_search():
    server_params = StdioServerParameters(
        command="python",
        args=["server.py"],
    )
    async with stdio_client(server_params) as (reader, writer):
        async with ClientSession(reader, writer) as session:
            await session.initialize()
            result = await session.call_tool("general_search", arguments={"query": "latest AI trends"})
            print(result)
```

---

Alternativamente, en modo interactivo, selecciona `general_search` en el menú e ingresa tu consulta cuando se te solicite.

**Parámetros:**
- `query` (string): La consulta de búsqueda

**Ejemplo de Solicitud:**

```json
{
  "query": "latest AI trends"
}
```

### news_search

Busca artículos de noticias recientes relacionados con una consulta.

**Cómo llamar a esta herramienta:**

Puedes llamar a `news_search` desde tu propio script usando el SDK MCP para Python, o de forma interactiva usando el Inspector o el modo interactivo del cliente. Aquí tienes un ejemplo de código usando el SDK:

# [Ejemplo en Python](../../../../05-AdvancedTopics/web-search-mcp)

```python
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def run_news_search():
    server_params = StdioServerParameters(
        command="python",
        args=["server.py"],
    )
    async with stdio_client(server_params) as (reader, writer):
        async with ClientSession(reader, writer) as session:
            await session.initialize()
            result = await session.call_tool("news_search", arguments={"query": "AI policy updates"})
            print(result)
```

---

Alternativamente, en modo interactivo, selecciona `news_search` en el menú e ingresa tu consulta cuando se te solicite.

**Parámetros:**
- `query` (string): La consulta de búsqueda

**Ejemplo de Solicitud:**

```json
{
  "query": "AI policy updates"
}
```

### product_search

Busca productos que coincidan con una consulta.

**Cómo llamar a esta herramienta:**

Puedes llamar a `product_search` desde tu propio script usando el SDK MCP para Python, o de forma interactiva usando el Inspector o el modo interactivo del cliente. Aquí tienes un ejemplo de código usando el SDK:

# [Ejemplo en Python](../../../../05-AdvancedTopics/web-search-mcp)

```python
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def run_product_search():
    server_params = StdioServerParameters(
        command="python",
        args=["server.py"],
    )
    async with stdio_client(server_params) as (reader, writer):
        async with ClientSession(reader, writer) as session:
            await session.initialize()
            result = await session.call_tool("product_search", arguments={"query": "best AI gadgets 2025"})
            print(result)
```

---

Alternativamente, en modo interactivo, selecciona `product_search` en el menú e ingresa tu consulta cuando se te solicite.

**Parámetros:**
- `query` (string): La consulta de búsqueda de productos

**Ejemplo de Solicitud:**

```json
{
  "query": "best AI gadgets 2025"
}
```

### qna

Obtiene respuestas directas a preguntas desde motores de búsqueda.

**Cómo llamar a esta herramienta:**

Puedes llamar a `qna` desde tu propio script usando el SDK MCP para Python, o de forma interactiva usando el Inspector o el modo interactivo del cliente. Aquí tienes un ejemplo de código usando el SDK:

# [Ejemplo en Python](../../../../05-AdvancedTopics/web-search-mcp)

```python
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def run_qna():
    server_params = StdioServerParameters(
        command="python",
        args=["server.py"],
    )
    async with stdio_client(server_params) as (reader, writer):
        async with ClientSession(reader, writer) as session:
            await session.initialize()
            result = await session.call_tool("qna", arguments={"question": "what is artificial intelligence"})
            print(result)
```

---

Alternativamente, en modo interactivo, selecciona `qna` en el menú e ingresa tu pregunta cuando se te solicite.

**Parámetros:**
- `question` (string): La pregunta para la cual buscar una respuesta

**Ejemplo de Solicitud:**

```json
{
  "question": "what is artificial intelligence"
}
```

## Detalles del Código

Esta sección proporciona fragmentos de código y referencias para las implementaciones del servidor y cliente.

# [Python](../../../../05-AdvancedTopics/web-search-mcp)

Consulta [`server.py`](../../../../05-AdvancedTopics/web-search-mcp/server.py) y [`client.py`](../../../../05-AdvancedTopics/web-search-mcp/client.py) para detalles completos de la implementación.

```python
# Example snippet from server.py:
import os
import httpx
# ...existing code...
```

---

## Conceptos Avanzados en Esta Lección

Antes de comenzar a construir, aquí tienes algunos conceptos avanzados importantes que aparecerán a lo largo de este capítulo. Entenderlos te ayudará a seguir el contenido, incluso si son nuevos para ti:

- **Orquestación Multi-herramienta**: Esto significa ejecutar varias herramientas diferentes (como búsqueda web, búsqueda de noticias, búsqueda de productos y preguntas y respuestas) dentro de un solo servidor MCP. Permite que tu servidor maneje una variedad de tareas, no solo una.
- **Manejo de Límites de Tasa de API**: Muchas APIs externas (como SerpAPI) limitan cuántas solicitudes puedes hacer en cierto tiempo. Un buen código verifica estos límites y los maneja con gracia, para que tu aplicación no falle si alcanzas un límite.
- **Análisis de Datos Estructurados**: Las respuestas de API suelen ser complejas y anidadas. Este concepto trata de convertir esas respuestas en formatos limpios y fáciles de usar, amigables para LLM u otros programas.
- **Recuperación de Errores**: A veces algo sale mal—quizás falla la red o la API no devuelve lo esperado. La recuperación de errores significa que tu código puede manejar estos problemas y aún así dar retroalimentación útil, en lugar de colapsar.
- **Validación de Parámetros**: Se trata de verificar que todas las entradas a tus herramientas sean correctas y seguras de usar. Incluye establecer valores por defecto y asegurarse de que los tipos sean correctos, lo que ayuda a prevenir errores y confusiones.

Esta sección te ayudará a diagnosticar y resolver problemas comunes que puedas encontrar al trabajar con el Servidor MCP de Búsqueda Web. Si te topas con errores o comportamientos inesperados, esta sección de solución de problemas ofrece soluciones a los problemas más comunes. Revisa estos consejos antes de buscar ayuda adicional—frecuentemente resuelven problemas rápidamente.

## Solución de Problemas

Al trabajar con el Servidor MCP de Búsqueda Web, es normal que ocasionalmente surjan problemas—esto es común al desarrollar con APIs externas y nuevas herramientas. Esta sección ofrece soluciones prácticas a los problemas más frecuentes, para que puedas volver a la normalidad rápidamente. Si encuentras un error, comienza aquí: los consejos a continuación abordan los problemas que la mayoría de los usuarios enfrentan y a menudo pueden resolver tu problema sin ayuda extra.

### Problemas Comunes

A continuación, algunos de los problemas más frecuentes que enfrentan los usuarios, junto con explicaciones claras y pasos para resolverlos:

1. **Falta SERPAPI_KEY en el archivo .env**
   - Si ves el error `SERPAPI_KEY environment variable not found`, significa que tu aplicación no puede encontrar la clave API necesaria para acceder a SerpAPI. Para solucionarlo, crea un archivo llamado `.env` en la raíz de tu proyecto (si no existe) y añade una línea como `SERPAPI_KEY=tu_clave_serpapi_aqui`. Asegúrate de reemplazar `tu_clave_serpapi_aqui` con tu clave real del sitio de SerpAPI.

2. **Errores de módulo no encontrado**
   - Errores como `ModuleNotFoundError: No module named 'httpx'` indican que falta un paquete Python requerido. Esto suele ocurrir si no has instalado todas las dependencias. Para resolverlo, ejecuta `pip install -r requirements.txt` en tu terminal para instalar todo lo que tu proyecto necesita.

3. **Problemas de conexión**
   - Si recibes un error como `Error during client execution`, a menudo significa que el cliente no puede conectarse al servidor, o que el servidor no está corriendo como se espera. Verifica que tanto el cliente como el servidor sean versiones compatibles, y que `server.py` esté presente y ejecutándose en el directorio correcto. Reiniciar ambos también puede ayudar.

4. **Errores de SerpAPI**
   - Ver el mensaje `Search API returned error status: 401` significa que tu clave SerpAPI está ausente, es incorrecta o ha expirado. Ve a tu panel de SerpAPI, verifica tu clave y actualiza tu archivo `.env` si es necesario. Si tu clave es correcta pero aún ves este error, revisa si tu plan gratuito ha agotado la cuota.

### Modo Debug

Por defecto, la aplicación solo registra información importante. Si quieres ver más detalles sobre lo que está pasando (por ejemplo, para diagnosticar problemas difíciles), puedes activar el modo DEBUG. Esto mostrará mucha más información sobre cada paso que da la aplicación.

**Ejemplo: Salida Normal**
```plaintext
2025-06-01 10:15:23,456 - __main__ - INFO - Calling general_search with params: {'query': 'open source LLMs'}
2025-06-01 10:15:24,123 - __main__ - INFO - Successfully called general_search

GENERAL_SEARCH RESULTS:
... (search results here) ...
```

**Ejemplo: Salida DEBUG**
```plaintext
2025-06-01 10:15:23,456 - __main__ - INFO - Calling general_search with params: {'query': 'open source LLMs'}
2025-06-01 10:15:23,457 - httpx - DEBUG - HTTP Request: GET https://serpapi.com/search ...
2025-06-01 10:15:23,458 - httpx - DEBUG - HTTP Response: 200 OK ...
2025-06-01 10:15:24,123 - __main__ - INFO - Successfully called general_search

GENERAL_SEARCH RESULTS:
... (search results here) ...
```

Fíjate cómo el modo DEBUG incluye líneas adicionales sobre solicitudes HTTP, respuestas y otros detalles internos. Esto puede ser muy útil para la solución de problemas.
Para habilitar el modo DEBUG, configura el nivel de logging a DEBUG al inicio de tu `client.py` o `server.py`:

# [Python](../../../../05-AdvancedTopics/web-search-mcp)

```python
# At the top of your client.py or server.py
import logging
logging.basicConfig(
    level=logging.DEBUG,  # Change from INFO to DEBUG
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
```

---

---

## Qué sigue

- [5.10 Transmisión en Tiempo Real](../mcp-realtimestreaming/README.md)

**Aviso legal**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda la traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o interpretaciones erróneas derivadas del uso de esta traducción.