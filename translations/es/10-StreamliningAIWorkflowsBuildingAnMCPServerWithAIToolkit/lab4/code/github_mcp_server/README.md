# Servidor MCP de Clima

Este es un servidor MCP de ejemplo en Python que implementa herramientas de clima con respuestas simuladas. Puede ser utilizado como base para tu propio servidor MCP. Incluye las siguientes características:

- **Herramienta de Clima**: Una herramienta que proporciona información meteorológica simulada basada en la ubicación proporcionada.
- **Herramienta de Clonación de Git**: Una herramienta que clona un repositorio de git en una carpeta especificada.
- **Herramienta de Apertura en VS Code**: Una herramienta que abre una carpeta en VS Code o VS Code Insiders.
- **Conexión con Agent Builder**: Una función que permite conectar el servidor MCP al Agent Builder para pruebas y depuración.
- **Depuración en [MCP Inspector](https://github.com/modelcontextprotocol/inspector)**: Una función que permite depurar el servidor MCP utilizando el MCP Inspector.

## Comienza con la plantilla del Servidor MCP de Clima

> **Requisitos previos**
>
> Para ejecutar el servidor MCP en tu máquina de desarrollo local, necesitarás:
>
> - [Python](https://www.python.org/)
> - [Git](https://git-scm.com/) (Requerido para la herramienta git_clone_repo)
> - [VS Code](https://code.visualstudio.com/) o [VS Code Insiders](https://code.visualstudio.com/insiders/) (Requerido para la herramienta open_in_vscode)
> - (*Opcional - si prefieres uv*) [uv](https://github.com/astral-sh/uv)
> - [Extensión de Depuración de Python](https://marketplace.visualstudio.com/items?itemName=ms-python.debugpy)

## Preparar el entorno

Hay dos enfoques para configurar el entorno de este proyecto. Puedes elegir cualquiera de ellos según tu preferencia.

> Nota: Recarga VSCode o la terminal para asegurarte de que se utiliza el Python del entorno virtual después de crearlo.

| Enfoque | Pasos |
| -------- | ----- |
| Usando `uv` | 1. Crear entorno virtual: `uv venv` <br>2. Ejecutar el comando de VSCode "***Python: Select Interpreter***" y seleccionar el Python del entorno virtual creado <br>3. Instalar dependencias (incluyendo dependencias de desarrollo): `uv pip install -r pyproject.toml --extra dev` |
| Usando `pip` | 1. Crear entorno virtual: `python -m venv .venv` <br>2. Ejecutar el comando de VSCode "***Python: Select Interpreter***" y seleccionar el Python del entorno virtual creado <br>3. Instalar dependencias (incluyendo dependencias de desarrollo): `pip install -e .[dev]` |

Después de configurar el entorno, puedes ejecutar el servidor en tu máquina de desarrollo local a través de Agent Builder como cliente MCP para comenzar:
1. Abre el panel de depuración de VS Code. Selecciona `Debug in Agent Builder` o presiona `F5` para iniciar la depuración del servidor MCP.
2. Utiliza AI Toolkit Agent Builder para probar el servidor con [este prompt](../../../../../../../../../../../open_prompt_builder). El servidor se conectará automáticamente al Agent Builder.
3. Haz clic en `Run` para probar el servidor con el prompt.

**¡Felicidades**! Has ejecutado exitosamente el Servidor MCP de Clima en tu máquina de desarrollo local a través de Agent Builder como cliente MCP.
![DebugMCP](https://raw.githubusercontent.com/microsoft/windows-ai-studio-templates/refs/heads/dev/mcpServers/mcp_debug.gif)

## Qué incluye la plantilla

| Carpeta / Archivo | Contenido                                     |
| ------------------ | -------------------------------------------- |
| `.vscode`          | Archivos de VSCode para depuración           |
| `.aitk`            | Configuraciones para AI Toolkit              |
| `src`              | Código fuente del servidor MCP de clima      |

## Cómo depurar el Servidor MCP de Clima

> Notas:
> - [MCP Inspector](https://github.com/modelcontextprotocol/inspector) es una herramienta visual para desarrolladores que permite probar y depurar servidores MCP.
> - Todos los modos de depuración admiten puntos de interrupción, por lo que puedes añadir puntos de interrupción al código de implementación de herramientas.

## Herramientas disponibles

### Herramienta de Clima
La herramienta `get_weather` proporciona información meteorológica simulada para una ubicación especificada.

| Parámetro | Tipo | Descripción |
| --------- | ---- | ----------- |
| `location` | string | Ubicación para obtener el clima (por ejemplo, nombre de ciudad, estado o coordenadas) |

### Herramienta de Clonación de Git
La herramienta `git_clone_repo` clona un repositorio de git en una carpeta especificada.

| Parámetro | Tipo | Descripción |
| --------- | ---- | ----------- |
| `repo_url` | string | URL del repositorio de git a clonar |
| `target_folder` | string | Ruta de la carpeta donde se debe clonar el repositorio |

La herramienta devuelve un objeto JSON con:
- `success`: Booleano que indica si la operación fue exitosa
- `target_folder` o `error`: La ruta del repositorio clonado o un mensaje de error

### Herramienta de Apertura en VS Code
La herramienta `open_in_vscode` abre una carpeta en la aplicación VS Code o VS Code Insiders.

| Parámetro | Tipo | Descripción |
| --------- | ---- | ----------- |
| `folder_path` | string | Ruta de la carpeta a abrir |
| `use_insiders` | boolean (opcional) | Indica si se debe usar VS Code Insiders en lugar de VS Code regular |

La herramienta devuelve un objeto JSON con:
- `success`: Booleano que indica si la operación fue exitosa
- `message` o `error`: Un mensaje de confirmación o un mensaje de error

| Modo de Depuración | Descripción | Pasos para depurar |
| ------------------ | ----------- | ------------------ |
| Agent Builder | Depura el servidor MCP en el Agent Builder a través de AI Toolkit. | 1. Abre el panel de depuración de VS Code. Selecciona `Debug in Agent Builder` y presiona `F5` para iniciar la depuración del servidor MCP.<br>2. Utiliza AI Toolkit Agent Builder para probar el servidor con [este prompt](../../../../../../../../../../../open_prompt_builder). El servidor se conectará automáticamente al Agent Builder.<br>3. Haz clic en `Run` para probar el servidor con el prompt. |
| MCP Inspector | Depura el servidor MCP utilizando el MCP Inspector. | 1. Instala [Node.js](https://nodejs.org/)<br> 2. Configura el Inspector: `cd inspector` && `npm install` <br> 3. Abre el panel de depuración de VS Code. Selecciona `Debug SSE in Inspector (Edge)` o `Debug SSE in Inspector (Chrome)`. Presiona F5 para iniciar la depuración.<br> 4. Cuando MCP Inspector se lance en el navegador, haz clic en el botón `Connect` para conectar este servidor MCP.<br> 5. Luego puedes `List Tools`, seleccionar una herramienta, ingresar parámetros y `Run Tool` para depurar tu código del servidor.<br> |

## Puertos predeterminados y personalizaciones

| Modo de Depuración | Puertos | Definiciones | Personalizaciones | Nota |
| ------------------ | ------ | ------------ | ----------------- | ---- |
| Agent Builder | 3001 | [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json) | Edita [launch.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/launch.json), [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json), [\_\_init\_\_.py](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/src/__init__.py), [mcp.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.aitk/mcp.json) para cambiar los puertos mencionados. | N/A |
| MCP Inspector | 3001 (Servidor); 5173 y 3000 (Inspector) | [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json) | Edita [launch.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/launch.json), [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json), [\_\_init\_\_.py](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/src/__init__.py), [mcp.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.aitk/mcp.json) para cambiar los puertos mencionados. | N/A |

## Comentarios

Si tienes comentarios o sugerencias para esta plantilla, por favor abre un issue en el [repositorio de GitHub de AI Toolkit](https://github.com/microsoft/vscode-ai-toolkit/issues).

---

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por garantizar la precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o imprecisiones. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o interpretaciones erróneas que puedan surgir del uso de esta traducción.