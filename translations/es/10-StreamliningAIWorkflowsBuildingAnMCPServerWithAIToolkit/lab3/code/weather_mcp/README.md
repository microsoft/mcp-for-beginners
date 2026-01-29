# Servidor MCP de Clima

Este es un ejemplo de Servidor MCP en Python que implementa herramientas meteorológicas con respuestas simuladas. Puede usarse como base para tu propio Servidor MCP. Incluye las siguientes características:

- **Herramienta de Clima**: Una herramienta que proporciona información meteorológica simulada según la ubicación dada.
- **Conexión con Agent Builder**: Una función que permite conectar el servidor MCP con Agent Builder para pruebas y depuración.
- **Depuración en [MCP Inspector](https://github.com/modelcontextprotocol/inspector)**: Una función que permite depurar el Servidor MCP usando MCP Inspector.

## Comenzar con la plantilla del Servidor MCP de Clima

> **Requisitos previos**
>
> Para ejecutar el Servidor MCP en tu máquina local de desarrollo, necesitarás:
>
> - [Python](https://www.python.org/)
> - (*Opcional - si prefieres uv*) [uv](https://github.com/astral-sh/uv)
> - [Extensión de depurador de Python](https://marketplace.visualstudio.com/items?itemName=ms-python.debugpy)

## Preparar el entorno

Hay dos formas de configurar el entorno para este proyecto. Puedes elegir la que prefieras.

> Nota: Recarga VSCode o la terminal para asegurarte de que se use el Python del entorno virtual después de crearlo.

| Enfoque | Pasos |
| -------- | ----- |
| Usando `uv` | 1. Crear entorno virtual: `uv venv` <br>2. Ejecutar el comando de VSCode "***Python: Select Interpreter***" y seleccionar el Python del entorno virtual creado <br>3. Instalar dependencias (incluyendo dependencias de desarrollo): `uv pip install -r pyproject.toml --extra dev` |
| Usando `pip` | 1. Crear entorno virtual: `python -m venv .venv` <br>2. Ejecutar el comando de VSCode "***Python: Select Interpreter***" y seleccionar el Python del entorno virtual creado<br>3. Instalar dependencias (incluyendo dependencias de desarrollo): `pip install -e .[dev]` |

Después de configurar el entorno, puedes ejecutar el servidor en tu máquina local de desarrollo a través de Agent Builder como cliente MCP para comenzar:
1. Abre el panel de depuración de VS Code. Selecciona `Debug in Agent Builder` o presiona `F5` para iniciar la depuración del servidor MCP.
2. Usa AI Toolkit Agent Builder para probar el servidor con [este prompt](../../../../../../../../../../open_prompt_builder). El servidor se conectará automáticamente a Agent Builder.
3. Haz clic en `Run` para probar el servidor con el prompt.

**¡Felicidades!** Has ejecutado con éxito el Servidor MCP de Clima en tu máquina local de desarrollo a través de Agent Builder como cliente MCP.  
![DebugMCP](https://raw.githubusercontent.com/microsoft/windows-ai-studio-templates/refs/heads/dev/mcpServers/mcp_debug.gif)

## Qué incluye la plantilla

| Carpeta / Archivo | Contenido                                   |
| ----------------- | ------------------------------------------ |
| `.vscode`         | Archivos de VSCode para depuración         |
| `.aitk`           | Configuraciones para AI Toolkit             |
| `src`             | Código fuente del servidor MCP de clima    |

## Cómo depurar el Servidor MCP de Clima

> Notas:
> - [MCP Inspector](https://github.com/modelcontextprotocol/inspector) es una herramienta visual para desarrolladores para probar y depurar servidores MCP.
> - Todos los modos de depuración soportan puntos de interrupción, por lo que puedes añadirlos en el código de implementación de la herramienta.

| Modo de depuración | Descripción | Pasos para depurar |
| ------------------ | ----------- | ------------------ |
| Agent Builder | Depura el servidor MCP en Agent Builder a través de AI Toolkit. | 1. Abre el panel de depuración de VS Code. Selecciona `Debug in Agent Builder` y presiona `F5` para iniciar la depuración del servidor MCP.<br>2. Usa AI Toolkit Agent Builder para probar el servidor con [este prompt](../../../../../../../../../../open_prompt_builder). El servidor se conectará automáticamente a Agent Builder.<br>3. Haz clic en `Run` para probar el servidor con el prompt. |
| MCP Inspector | Depura el servidor MCP usando MCP Inspector. | 1. Instala [Node.js](https://nodejs.org/)<br> 2. Configura Inspector: `cd inspector` && `npm install` <br> 3. Abre el panel de depuración de VS Code. Selecciona `Debug SSE in Inspector (Edge)` o `Debug SSE in Inspector (Chrome)`. Presiona F5 para iniciar la depuración.<br> 4. Cuando MCP Inspector se abra en el navegador, haz clic en el botón `Connect` para conectar este servidor MCP.<br> 5. Luego puedes `List Tools`, seleccionar una herramienta, ingresar parámetros y `Run Tool` para depurar tu código del servidor.<br> |

## Puertos predeterminados y personalizaciones

| Modo de depuración | Puertos | Definiciones | Personalizaciones | Nota |
| ------------------ | ------- | ------------ | ----------------- | ----- |
| Agent Builder | 3001 | [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/tasks.json) | Edita [launch.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/launch.json), [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/tasks.json), [\_\_init\_\_.py](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/src/__init__.py), [mcp.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.aitk/mcp.json) para cambiar los puertos mencionados. | N/A |
| MCP Inspector | 3001 (Servidor); 5173 y 3000 (Inspector) | [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/tasks.json) | Edita [launch.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/launch.json), [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/tasks.json), [\_\_init\_\_.py](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/src/__init__.py), [mcp.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.aitk/mcp.json) para cambiar los puertos mencionados. | N/A |

## Comentarios

Si tienes algún comentario o sugerencia para esta plantilla, por favor abre un issue en el [repositorio de AI Toolkit en GitHub](https://github.com/microsoft/vscode-ai-toolkit/issues)

**Aviso legal**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda la traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o interpretaciones erróneas derivadas del uso de esta traducción.