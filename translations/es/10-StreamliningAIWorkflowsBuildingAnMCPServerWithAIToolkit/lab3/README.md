# 🔧 Módulo 3: Desarrollo Avanzado de MCP con AI Toolkit

![Duración](https://img.shields.io/badge/Duration-20_minutes-blue?style=flat-square)
![AI Toolkit](https://img.shields.io/badge/AI_Toolkit-Required-orange?style=flat-square)
![Python](https://img.shields.io/badge/Python-3.10+-green?style=flat-square)
![MCP SDK](https://img.shields.io/badge/MCP_SDK-1.9.3-purple?style=flat-square)
![Inspector](https://img.shields.io/badge/MCP_Inspector-0.14.0-blue?style=flat-square)

## 🎯 Objetivos de Aprendizaje

Al finalizar este laboratorio, podrás:

- ✅ Crear servidores MCP personalizados usando AI Toolkit
- ✅ Configurar y utilizar el último MCP Python SDK (v1.9.3)
- ✅ Configurar y usar MCP Inspector para depuración
- ✅ Depurar servidores MCP tanto en Agent Builder como en Inspector
- ✅ Comprender flujos de trabajo avanzados para desarrollo de servidores MCP

## 📋 Requisitos Previos

- Haber completado el Laboratorio 2 (Fundamentos de MCP)
- VS Code con la extensión AI Toolkit instalada
- Entorno Python 3.10+
- Node.js y npm para la configuración de Inspector

## 🏗️ Lo que Construirás

En este laboratorio crearás un **Servidor MCP de Clima** que demostrará:
- Implementación personalizada de un servidor MCP
- Integración con AI Toolkit Agent Builder
- Flujos de trabajo profesionales de depuración
- Uso moderno del SDK MCP

---

## 🔧 Resumen de Componentes Principales

### 🐍 MCP Python SDK  
El SDK Python del Protocolo de Contexto de Modelo proporciona la base para construir servidores MCP personalizados. Usarás la versión 1.9.3 con capacidades mejoradas de depuración.

### 🔍 MCP Inspector  
Una herramienta poderosa para depuración que ofrece:  
- Monitoreo en tiempo real del servidor  
- Visualización de la ejecución de herramientas  
- Inspección de solicitudes y respuestas de red  
- Entorno interactivo de pruebas

---

## 📖 Implementación Paso a Paso

### Paso 1: Crear un WeatherAgent en Agent Builder

1. **Abre Agent Builder** en VS Code a través de la extensión AI Toolkit  
2. **Crea un nuevo agente** con la siguiente configuración:  
   - Nombre del agente: `WeatherAgent`

![Creación de Agente](../../../../translated_images/es/Agent.c9c33f6a412b4cde.webp)

### Paso 2: Inicializar el Proyecto del Servidor MCP

1. **Ve a Herramientas** → **Agregar Herramienta** en Agent Builder  
2. **Selecciona "MCP Server"** entre las opciones disponibles  
3. **Elige "Crear un nuevo servidor MCP"**  
4. **Selecciona la plantilla `python-weather`**  
5. **Nombra tu servidor:** `weather_mcp`

![Selección de Plantilla Python](../../../../translated_images/es/Pythontemplate.9d0a2913c6491500.webp)

### Paso 3: Abrir y Examinar el Proyecto

1. **Abre el proyecto generado** en VS Code  
2. **Revisa la estructura del proyecto:**  
   ```
   weather_mcp/
   ├── src/
   │   ├── __init__.py
   │   └── server.py
   ├── inspector/
   │   ├── package.json
   │   └── package-lock.json
   ├── .vscode/
   │   ├── launch.json
   │   └── tasks.json
   ├── pyproject.toml
   └── README.md
   ```

### Paso 4: Actualizar al Último MCP SDK

> **🔍 ¿Por qué actualizar?** Queremos usar el último MCP SDK (v1.9.3) y el servicio Inspector (0.14.0) para obtener funciones mejoradas y mejores capacidades de depuración.

#### 4a. Actualizar dependencias de Python

**Edita `pyproject.toml`:** actualiza [./code/weather_mcp/pyproject.toml](../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/pyproject.toml)

#### 4b. Actualizar configuración de Inspector

**Edita `inspector/package.json`:** actualiza [./code/weather_mcp/inspector/package.json](../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/inspector/package.json)

#### 4c. Actualizar dependencias de Inspector

**Edita `inspector/package-lock.json`:** actualiza [./code/weather_mcp/inspector/package-lock.json](../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/inspector/package-lock.json)

> **📝 Nota:** Este archivo contiene definiciones extensas de dependencias. A continuación se muestra la estructura esencial; el contenido completo asegura la resolución correcta de dependencias.

> **⚡ Paquete completo:** El package-lock.json completo contiene unas ~3000 líneas de definiciones de dependencias. Lo anterior muestra la estructura clave; usa el archivo proporcionado para la resolución completa.

### Paso 5: Configurar la Depuración en VS Code

*Nota: Por favor copia el archivo en la ruta especificada para reemplazar el archivo local correspondiente*

#### 5a. Actualizar configuración de lanzamiento

**Edita `.vscode/launch.json`:**

```json
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "Attach to Local MCP",
      "type": "debugpy",
      "request": "attach",
      "connect": {
        "host": "localhost",
        "port": 5678
      },
      "presentation": {
        "hidden": true
      },
      "internalConsoleOptions": "neverOpen",
      "postDebugTask": "Terminate All Tasks"
    },
    {
      "name": "Launch Inspector (Edge)",
      "type": "msedge",
      "request": "launch",
      "url": "http://localhost:6274?timeout=60000&serverUrl=http://localhost:3001/sse#tools",
      "cascadeTerminateToConfigurations": [
        "Attach to Local MCP"
      ],
      "presentation": {
        "hidden": true
      },
      "internalConsoleOptions": "neverOpen"
    },
    {
      "name": "Launch Inspector (Chrome)",
      "type": "chrome",
      "request": "launch",
      "url": "http://localhost:6274?timeout=60000&serverUrl=http://localhost:3001/sse#tools",
      "cascadeTerminateToConfigurations": [
        "Attach to Local MCP"
      ],
      "presentation": {
        "hidden": true
      },
      "internalConsoleOptions": "neverOpen"
    }
  ],
  "compounds": [
    {
      "name": "Debug in Agent Builder",
      "configurations": [
        "Attach to Local MCP"
      ],
      "preLaunchTask": "Open Agent Builder",
    },
    {
      "name": "Debug in Inspector (Edge)",
      "configurations": [
        "Launch Inspector (Edge)",
        "Attach to Local MCP"
      ],
      "preLaunchTask": "Start MCP Inspector",
      "stopAll": true
    },
    {
      "name": "Debug in Inspector (Chrome)",
      "configurations": [
        "Launch Inspector (Chrome)",
        "Attach to Local MCP"
      ],
      "preLaunchTask": "Start MCP Inspector",
      "stopAll": true
    }
  ]
}
```

**Edita `.vscode/tasks.json`:**

```
{
  "version": "2.0.0",
  "tasks": [
    {
      "label": "Start MCP Server",
      "type": "shell",
      "command": "python -m debugpy --listen 127.0.0.1:5678 src/__init__.py sse",
      "isBackground": true,
      "options": {
        "cwd": "${workspaceFolder}",
        "env": {
          "PORT": "3001"
        }
      },
      "problemMatcher": {
        "pattern": [
          {
            "regexp": "^.*$",
            "file": 0,
            "location": 1,
            "message": 2
          }
        ],
        "background": {
          "activeOnStart": true,
          "beginsPattern": ".*",
          "endsPattern": "Application startup complete|running"
        }
      }
    },
    {
      "label": "Start MCP Inspector",
      "type": "shell",
      "command": "npm run dev:inspector",
      "isBackground": true,
      "options": {
        "cwd": "${workspaceFolder}/inspector",
        "env": {
          "CLIENT_PORT": "6274",
          "SERVER_PORT": "6277",
        }
      },
      "problemMatcher": {
        "pattern": [
          {
            "regexp": "^.*$",
            "file": 0,
            "location": 1,
            "message": 2
          }
        ],
        "background": {
          "activeOnStart": true,
          "beginsPattern": "Starting MCP inspector",
          "endsPattern": "Proxy server listening on port"
        }
      },
      "dependsOn": [
        "Start MCP Server"
      ]
    },
    {
      "label": "Open Agent Builder",
      "type": "shell",
      "command": "echo ${input:openAgentBuilder}",
      "presentation": {
        "reveal": "never"
      },
      "dependsOn": [
        "Start MCP Server"
      ],
    },
    {
      "label": "Terminate All Tasks",
      "command": "echo ${input:terminate}",
      "type": "shell",
      "problemMatcher": []
    }
  ],
  "inputs": [
    {
      "id": "openAgentBuilder",
      "type": "command",
      "command": "ai-mlstudio.agentBuilder",
      "args": {
        "initialMCPs": [ "local-server-weather_mcp" ],
        "triggeredFrom": "vsc-tasks"
      }
    },
    {
      "id": "terminate",
      "type": "command",
      "command": "workbench.action.tasks.terminate",
      "args": "terminateAll"
    }
  ]
}
```

---

## 🚀 Ejecutar y Probar tu Servidor MCP

### Paso 6: Instalar Dependencias

Después de hacer los cambios de configuración, ejecuta los siguientes comandos:

**Instalar dependencias de Python:**  
```bash
uv sync
```

**Instalar dependencias de Inspector:**  
```bash
cd inspector
npm install
```

### Paso 7: Depurar con Agent Builder

1. **Presiona F5** o usa la configuración **"Debug in Agent Builder"**  
2. **Selecciona la configuración compuesta** desde el panel de depuración  
3. **Espera a que el servidor inicie** y Agent Builder se abra  
4. **Prueba tu servidor MCP de clima** con consultas en lenguaje natural

Introduce un prompt como este

SYSTEM_PROMPT

```
You are my weather assistant
```

USER_PROMPT

```
How's the weather like in Seattle
```

![Resultado de Depuración en Agent Builder](../../../../translated_images/es/Result.6ac570f7d2b1d538.webp)

### Paso 8: Depurar con MCP Inspector

1. **Usa la configuración "Debug in Inspector"** (Edge o Chrome)  
2. **Abre la interfaz de Inspector** en `http://localhost:6274`  
3. **Explora el entorno interactivo de pruebas:**  
   - Visualiza las herramientas disponibles  
   - Prueba la ejecución de herramientas  
   - Monitorea solicitudes de red  
   - Depura las respuestas del servidor

![Interfaz MCP Inspector](../../../../translated_images/es/Inspector.5672415cd02fe873.webp)

---

## 🎯 Resultados Clave de Aprendizaje

Al completar este laboratorio, has:

- [x] **Creado un servidor MCP personalizado** usando plantillas de AI Toolkit  
- [x] **Actualizado al último MCP SDK** (v1.9.3) para funcionalidad mejorada  
- [x] **Configurado flujos de trabajo profesionales de depuración** para Agent Builder e Inspector  
- [x] **Configurado MCP Inspector** para pruebas interactivas del servidor  
- [x] **Dominado configuraciones de depuración en VS Code** para desarrollo MCP

## 🔧 Funcionalidades Avanzadas Exploradas

| Funcionalidad | Descripción | Caso de Uso |
|---------------|-------------|-------------|
| **MCP Python SDK v1.9.3** | Última implementación del protocolo | Desarrollo moderno de servidores |
| **MCP Inspector 0.14.0** | Herramienta interactiva de depuración | Pruebas en tiempo real del servidor |
| **Depuración en VS Code** | Entorno de desarrollo integrado | Flujo profesional de depuración |
| **Integración con Agent Builder** | Conexión directa con AI Toolkit | Pruebas completas de agentes |

## 📚 Recursos Adicionales

- [Documentación MCP Python SDK](https://modelcontextprotocol.io/docs/sdk/python)  
- [Guía de la Extensión AI Toolkit](https://code.visualstudio.com/docs/ai/ai-toolkit)  
- [Documentación de Depuración en VS Code](https://code.visualstudio.com/docs/editor/debugging)  
- [Especificación del Protocolo de Contexto de Modelo](https://modelcontextprotocol.io/docs/concepts/architecture)

---

**🎉 ¡Felicidades!** Has completado con éxito el Laboratorio 3 y ahora puedes crear, depurar y desplegar servidores MCP personalizados usando flujos de trabajo profesionales de desarrollo.

### 🔜 Continúa al Siguiente Módulo

¿Listo para aplicar tus habilidades MCP en un flujo de trabajo real? Continúa con **[Módulo 4: Desarrollo Práctico de MCP - Servidor Clonador Personalizado de GitHub](../lab4/README.md)** donde:  
- Construirás un servidor MCP listo para producción que automatiza operaciones en repositorios GitHub  
- Implementarás funcionalidad de clonación de repositorios GitHub vía MCP  
- Integrarás servidores MCP personalizados con VS Code y GitHub Copilot Agent Mode  
- Probarás y desplegarás servidores MCP personalizados en entornos de producción  
- Aprenderás automatización práctica de flujos de trabajo para desarrolladores

**Aviso legal**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda la traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o interpretaciones erróneas derivadas del uso de esta traducción.