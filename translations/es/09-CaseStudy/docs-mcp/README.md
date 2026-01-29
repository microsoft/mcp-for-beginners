# Estudio de Caso: Conectarse al Servidor MCP de Microsoft Learn Docs desde un Cliente

¿Alguna vez te has encontrado alternando entre sitios de documentación, Stack Overflow y pestañas interminables del buscador, todo mientras intentas resolver un problema en tu código? Tal vez tengas un segundo monitor solo para la documentación, o estés constantemente cambiando entre tu IDE y un navegador. ¿No sería mejor si pudieras integrar la documentación directamente en tu flujo de trabajo, dentro de tus aplicaciones, tu IDE o incluso tus propias herramientas personalizadas? En este estudio de caso, exploraremos cómo hacer exactamente eso conectándonos directamente al servidor MCP de Microsoft Learn Docs desde tu propia aplicación cliente.

## Resumen

El desarrollo moderno es más que solo escribir código: se trata de encontrar la información correcta en el momento adecuado. La documentación está en todas partes, pero rara vez donde más la necesitas: dentro de tus herramientas y flujos de trabajo. Al integrar la obtención de documentación directamente en tus aplicaciones, puedes ahorrar tiempo, reducir los cambios de contexto y aumentar la productividad. En esta sección, te mostraremos cómo conectar un cliente al servidor MCP de Microsoft Learn Docs, para que puedas acceder a documentación en tiempo real y con contexto sin salir de tu aplicación.

Recorreremos el proceso de establecer una conexión, enviar una solicitud y manejar respuestas en streaming de manera eficiente. Este enfoque no solo agiliza tu flujo de trabajo, sino que también abre la puerta a construir herramientas de desarrollo más inteligentes y útiles.

## Objetivos de Aprendizaje

¿Por qué hacemos esto? Porque las mejores experiencias para desarrolladores son aquellas que eliminan fricciones. Imagina un mundo donde tu editor de código, chatbot o aplicación web pueda responder a tus preguntas de documentación al instante, usando el contenido más reciente de Microsoft Learn. Al final de este capítulo, sabrás cómo:

- Entender los conceptos básicos de la comunicación cliente-servidor MCP para documentación
- Implementar una aplicación de consola o web para conectarte al servidor MCP de Microsoft Learn Docs
- Usar clientes HTTP con streaming para obtener documentación en tiempo real
- Registrar e interpretar las respuestas de documentación en tu aplicación

Verás cómo estas habilidades te ayudarán a crear herramientas que no solo reaccionan, sino que son verdaderamente interactivas y conscientes del contexto.

## Escenario 1 - Obtención de Documentación en Tiempo Real con MCP

En este escenario, te mostraremos cómo conectar un cliente al servidor MCP de Microsoft Learn Docs, para que puedas acceder a documentación en tiempo real y con contexto sin salir de tu aplicación.

Pongámoslo en práctica. Tu tarea es escribir una aplicación que se conecte al servidor MCP de Microsoft Learn Docs, invoque la herramienta `microsoft_docs_search` y registre la respuesta en streaming en la consola.

### ¿Por qué este enfoque?
Porque es la base para construir integraciones más avanzadas, ya sea que quieras alimentar un chatbot, una extensión de IDE o un panel web.

Encontrarás el código e instrucciones para este escenario en la carpeta [`solution`](./solution/README.md) dentro de este estudio de caso. Los pasos te guiarán para configurar la conexión:
- Usar el SDK oficial de MCP y un cliente HTTP con capacidad de streaming para la conexión
- Llamar a la herramienta `microsoft_docs_search` con un parámetro de consulta para obtener documentación
- Implementar un registro adecuado y manejo de errores
- Crear una interfaz de consola interactiva que permita a los usuarios ingresar múltiples consultas de búsqueda

Este escenario demuestra cómo:
- Conectarse al servidor Docs MCP
- Enviar una consulta
- Analizar e imprimir los resultados

Así podría verse la ejecución de la solución:

```
Prompt> What is Azure Key Vault?
Answer> Azure Key Vault is a cloud service for securely storing and accessing secrets. ...
```

A continuación, un ejemplo mínimo de solución. El código completo y detalles están disponibles en la carpeta de solución.

<details>
<summary>Python</summary>

```python
import asyncio
from mcp.client.streamable_http import streamablehttp_client
from mcp import ClientSession

async def main():
    async with streamablehttp_client("https://learn.microsoft.com/api/mcp") as (read_stream, write_stream, _):
        async with ClientSession(read_stream, write_stream) as session:
            await session.initialize()
            result = await session.call_tool("microsoft_docs_search", {"query": "Azure Functions best practices"})
            print(result.content)

if __name__ == "__main__":
    asyncio.run(main())
```

- Para la implementación completa y registro, consulta [`scenario1.py`](../../../../09-CaseStudy/docs-mcp/solution/python/scenario1.py).
- Para instrucciones de instalación y uso, revisa el archivo [`README.md`](./solution/python/README.md) en la misma carpeta.
</details>

## Escenario 2 - Aplicación Web Interactiva para Generar Planes de Estudio con MCP

En este escenario, aprenderás a integrar Docs MCP en un proyecto de desarrollo web. El objetivo es permitir a los usuarios buscar documentación de Microsoft Learn directamente desde una interfaz web, haciendo que la documentación sea accesible al instante dentro de tu aplicación o sitio.

Verás cómo:
- Configurar una aplicación web
- Conectarse al servidor Docs MCP
- Manejar la entrada del usuario y mostrar resultados

Así podría verse la ejecución de la solución:

```
User> I want to learn about AI102 - so suggest the roadmap to get it started from learn for 6 weeks

Assistant> Here’s a detailed 6-week roadmap to start your preparation for the AI-102: Designing and Implementing a Microsoft Azure AI Solution certification, using official Microsoft resources and focusing on exam skills areas:

---
## Week 1: Introduction & Fundamentals
- **Understand the Exam**: Review the [AI-102 exam skills outline](https://learn.microsoft.com/en-us/credentials/certifications/exams/ai-102/).
- **Set up Azure**: Sign up for a free Azure account if you don't have one.
- **Learning Path**: [Introduction to Azure AI services](https://learn.microsoft.com/en-us/training/modules/intro-to-azure-ai/)
- **Focus**: Get familiar with Azure portal, AI capabilities, and necessary tools.

....more weeks of the roadmap...

Let me know if you want module-specific recommendations or need more customized weekly tasks!
```

A continuación, un ejemplo mínimo de solución. El código completo y detalles están disponibles en la carpeta de solución.

![Resumen del Escenario 2](../../../../translated_images/es/scenario2.0c92726d5cd81f68.webp)

<details>
<summary>Python (Chainlit)</summary>

Chainlit es un framework para construir aplicaciones web de IA conversacional. Facilita la creación de chatbots y asistentes interactivos que pueden llamar a herramientas MCP y mostrar resultados en tiempo real. Es ideal para prototipos rápidos e interfaces amigables para el usuario.

```python
import chainlit as cl
import requests

MCP_URL = "https://learn.microsoft.com/api/mcp"

@cl.on_message
def handle_message(message):
    query = {"question": message}
    response = requests.post(MCP_URL, json=query)
    if response.ok:
        result = response.json()
        cl.Message(content=result.get("answer", "No answer found.")).send()
    else:
        cl.Message(content="Error: " + response.text).send()
```

- Para la implementación completa, consulta [`scenario2.py`](../../../../09-CaseStudy/docs-mcp/solution/python/scenario2.py).
- Para instrucciones de configuración y ejecución, revisa el [`README.md`](./solution/python/README.md).
</details>

## Escenario 3: Documentación Dentro del Editor con el Servidor MCP en VS Code

Si quieres tener Microsoft Learn Docs directamente dentro de tu VS Code (en lugar de cambiar entre pestañas del navegador), puedes usar el servidor MCP en tu editor. Esto te permite:
- Buscar y leer documentación en VS Code sin salir de tu entorno de codificación.
- Referenciar documentación e insertar enlaces directamente en tus archivos README o de cursos.
- Aprovechar GitHub Copilot y MCP juntos para un flujo de trabajo de documentación potenciado por IA y sin interrupciones.

**Verás cómo:**
- Agregar un archivo válido `.vscode/mcp.json` en la raíz de tu espacio de trabajo (ver ejemplo abajo).
- Abrir el panel MCP o usar la paleta de comandos en VS Code para buscar e insertar documentación.
- Referenciar documentación directamente en tus archivos markdown mientras trabajas.
- Combinar este flujo con GitHub Copilot para una productividad aún mayor.

Aquí tienes un ejemplo de cómo configurar el servidor MCP en VS Code:

```json
{
  "servers": {
    "LearnDocsMCP": {
      "url": "https://learn.microsoft.com/api/mcp"
    }
  }
}
```

</details>

> Para una guía detallada con capturas de pantalla y pasos, consulta [`README.md`](./solution/scenario3/README.md).

![Resumen del Escenario 3](../../../../translated_images/es/step4-prompt-chat.12187bb001605efc.webp)

Este enfoque es ideal para quienes crean cursos técnicos, escriben documentación o desarrollan código con necesidades frecuentes de referencia.

## Puntos Clave

Integrar la documentación directamente en tus herramientas no es solo una comodidad, es un cambio radical para la productividad. Al conectarte al servidor MCP de Microsoft Learn Docs desde tu cliente, puedes:

- Eliminar los cambios de contexto entre tu código y la documentación
- Obtener documentación actualizada y con contexto en tiempo real
- Construir herramientas de desarrollo más inteligentes e interactivas

Estas habilidades te ayudarán a crear soluciones que no solo sean eficientes, sino también agradables de usar.

## Recursos Adicionales

Para profundizar tu comprensión, explora estos recursos oficiales:

- [Microsoft Learn Docs MCP Server (GitHub)](https://github.com/MicrosoftDocs/mcp)
- [Comenzar con Azure MCP Server (mcp-python)](https://learn.microsoft.com/en-us/azure/developer/azure-mcp-server/get-started#create-the-python-app)
- [¿Qué es el Azure MCP Server?](https://learn.microsoft.com/en-us/azure/developer/azure-mcp-server/)
- [Introducción al Model Context Protocol (MCP)](https://modelcontextprotocol.io/introduction)
- [Agregar plugins desde un MCP Server (Python)](https://learn.microsoft.com/en-us/semantic-kernel/concepts/plugins/adding-mcp-plugins)

**Aviso legal**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda la traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o interpretaciones erróneas derivadas del uso de esta traducción.