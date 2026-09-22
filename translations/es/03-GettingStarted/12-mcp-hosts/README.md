# Configuración de Clientes Populares de Host MCP

> [!NOTE]
> Las configuraciones de host que apuntan a `/sse` son ejemplos heredados de HTTP+SSE para
> MCP `2025-11-25`. Para MCP `2026-07-28`, selecciona HTTP transmitible en hosts que
> lo soporten y usa el punto final configurado por el servidor.

Esta guía explica cómo configurar y usar servidores MCP con aplicaciones populares de host de IA. Cada host tiene su propio enfoque de configuración, pero una vez configurados, todos ellos se comunican con servidores MCP utilizando el protocolo estandarizado.

## ¿Qué es un Host MCP?

Un **Host MCP** es una aplicación de IA que puede conectarse a servidores MCP para ampliar sus capacidades. Piensa en él como el "front end" con el que interactúan los usuarios, mientras que los servidores MCP proporcionan las herramientas y datos del "back end".

```mermaid
flowchart LR
    User[👤 Usuario] --> Host[🖥️ Anfitrión MCP]
    Host --> S1[Servidor MCP A]
    Host --> S2[Servidor MCP B]
    Host --> S3[Servidor MCP C]
    
    subgraph "Anfitriones Populares"
        H1[Claude Escritorio]
        H2[VS Code]
        H3[Cursor]
        H4[Cline]
        H5[Windsurf]
    end
```

## Requisitos Previos

- Un servidor MCP para conectarse (ver [Módulo 3.1 - Primer Servidor](../01-first-server/README.md))
- La aplicación host instalada en tu sistema
- Familiaridad básica con archivos de configuración JSON

---

## 1. Claude Desktop

**Claude Desktop** es la aplicación de escritorio oficial de Anthropic que soporta MCP nativamente.

### Instalación

1. Descarga Claude Desktop desde [claude.ai/download](https://claude.ai/download)
2. Instala e inicia sesión con tu cuenta de Anthropic

### Configuración

Claude Desktop utiliza un archivo de configuración JSON para definir servidores MCP.

**Ubicación del archivo de configuración:**
- **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
- **Windows**: `%APPDATA%\Claude\claude_desktop_config.json`
- **Linux**: `~/.config/Claude/claude_desktop_config.json`

**Ejemplo de configuración:**

```json
{
  "mcpServers": {
    "calculator": {
      "command": "python",
      "args": ["-m", "mcp_calculator_server"],
      "env": {
        "PYTHONPATH": "/path/to/your/server"
      }
    },
    "weather": {
      "command": "node",
      "args": ["/path/to/weather-server/build/index.js"]
    },
    "database": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-postgres"],
      "env": {
        "DATABASE_URL": "postgresql://user:pass@localhost/mydb"
      }
    }
  }
}
```

### Opciones de Configuración

| Campo | Descripción | Ejemplo |
|-------|-------------|---------|
| `command` | El ejecutable a ejecutar | `"python"`, `"node"`, `"npx"` |
| `args` | Argumentos de línea de comandos | `["-m", "my_server"]` |
| `env` | Variables de entorno | `{"API_KEY": "xxx"}` |
| `cwd` | Directorio de trabajo | `"/path/to/server"` |

### Probando tu Configuración

1. Guarda el archivo de configuración
2. Reinicia completamente Claude Desktop (cierra y vuelve a abrir)
3. Abre una nueva conversación
4. Busca el icono 🔌 que indica servidores conectados
5. Intenta pedirle a Claude que use alguna de tus herramientas

### Solución de Problemas en Claude Desktop

**Servidor no aparece:**
- Revisa la sintaxis del archivo de configuración con un validador JSON
- Asegúrate que la ruta del comando sea correcta
- Revisa los registros de Claude Desktop: Ayuda → Mostrar Registros

**El servidor falla al iniciar:**
- Prueba tu servidor manualmente en la terminal primero
- Verifica que las variables de entorno estén configuradas correctamente
- Asegúrate que todas las dependencias estén instaladas

---

## 2. VS Code con GitHub Copilot

VS Code soporta MCP a través de extensiones de GitHub Copilot Chat.

### Requisitos Previos

1. VS Code 1.99+ instalado
2. Extensión GitHub Copilot instalada
3. Extensión GitHub Copilot Chat instalada

### Configuración

VS Code usa `.vscode/mcp.json` en la configuración del espacio de trabajo o de usuario.

**Configuración de espacio de trabajo** (`.vscode/mcp.json`):

```json
{
  "servers": {
    "my-calculator": {
      "type": "stdio",
      "command": "python",
      "args": ["-m", "mcp_calculator_server"]
    },
    "my-database": {
      "type": "sse",
      "url": "http://localhost:8080/sse"
    }
  }
}
```

**Configuración de usuario** (`settings.json`):

```json
{
  "mcp.servers": {
    "global-server": {
      "type": "stdio",
      "command": "npx",
      "args": ["-y", "@anthropic/mcp-server-memory"]
    }
  },
  "mcp.enableLogging": true
}
```

### Usando MCP en VS Code

1. Abre el panel Copilot Chat (Ctrl+Shift+I / Cmd+Shift+I)
2. Escribe `@` para ver las herramientas MCP disponibles
3. Usa lenguaje natural para invocar herramientas: "Calcula 25 * 48 usando la calculadora"

### Solución de Problemas en VS Code

**Los servidores MCP no se cargan:**
- Revisa el panel de Salida → "MCP" para registros de error
- Recarga la ventana: Ctrl+Shift+P → "Developer: Reload Window"
- Verifica que el servidor funcione de forma independiente primero

---

## 3. Cursor

**Cursor** es un editor de código con enfoque en IA con soporte MCP integrado.

### Instalación

1. Descarga Cursor desde [cursor.sh](https://cursor.sh)
2. Instala e inicia sesión

### Configuración

Cursor usa un formato de configuración similar a Claude Desktop.

**Ubicación del archivo de configuración:**
- **macOS**: `~/.cursor/mcp.json`
- **Windows**: `%USERPROFILE%\.cursor\mcp.json`
- **Linux**: `~/.cursor/mcp.json`

**Ejemplo de configuración:**

```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "/path/to/allowed/directory"]
    },
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_TOKEN": "ghp_your_token_here"
      }
    }
  }
}
```

### Usando MCP en Cursor

1. Abre el chat IA de Cursor (Ctrl+L / Cmd+L)
2. Las herramientas MCP aparecen automáticamente en las sugerencias
3. Pide a la IA realizar tareas usando los servidores conectados

---

## 4. Cline (Basado en Terminal)

**Cline** es un cliente MCP basado en terminal, ideal para flujos de trabajo en línea de comandos.

### Instalación

```bash
npm install -g @anthropic/cline
```

### Configuración

Cline usa variables de entorno y argumentos de línea de comandos.

**Uso de variables de entorno:**

```bash
export ANTHROPIC_API_KEY="your-api-key"
export MCP_SERVER_CALCULATOR="python -m mcp_calculator_server"
```

**Uso de argumentos de línea de comandos:**

```bash
cline --mcp-server "calculator:python -m mcp_calculator_server" \
      --mcp-server "weather:node /path/to/weather/index.js"
```

**Archivo de configuración** (`~/.clinerc`):

```json
{
  "apiKey": "your-api-key",
  "mcpServers": {
    "calculator": {
      "command": "python",
      "args": ["-m", "mcp_calculator_server"]
    }
  }
}
```

### Usando Cline

```bash
# Iniciar una sesión interactiva
cline

# Consulta única con MCP
cline "Calculate the square root of 144 using the calculator"

# Listar herramientas disponibles
cline --list-tools
```

---

## 5. Windsurf

**Windsurf** es otro editor de código potenciado por IA con soporte MCP.

### Instalación

1. Descarga Windsurf desde [codeium.com/windsurf](https://codeium.com/windsurf)
2. Instala y crea una cuenta

### Configuración

La configuración de Windsurf se maneja a través de la interfaz de configuración:

1. Abre Configuración (Ctrl+, / Cmd+,)
2. Busca "MCP"
3. Haz clic en "Editar en settings.json"

**Ejemplo de configuración:**

```json
{
  "windsurf.mcp.servers": {
    "my-tools": {
      "command": "python",
      "args": ["/path/to/server.py"],
      "env": {}
    }
  },
  "windsurf.mcp.enabled": true
}
```

---

## Comparación de Tipos de Transporte

Diferentes hosts soportan diferentes mecanismos de transporte:

| Host | stdio | SSE/HTTP | WebSocket |
|------|-------|----------|-----------|
| Claude Desktop | ✅ | ❌ | ❌ |
| VS Code | ✅ | ✅ | ❌ |
| Cursor | ✅ | ✅ | ❌ |
| Cline | ✅ | ✅ | ❌ |
| Windsurf | ✅ | ✅ | ❌ |

**stdio** (entrada/salida estándar): Mejor para servidores locales iniciados por el host
**SSE/HTTP**: Mejor para servidores remotos o servidores compartidos entre múltiples clientes

---

## Solución de Problemas Comunes

### El servidor no inicia

1. **Prueba el servidor manualmente primero:**
   ```bash
   # Para Python
   python -m your_server_module
   
   # Para Node.js
   node /path/to/server/index.js
   ```

2. **Revisa la ruta del comando:**
   - Usa rutas absolutas cuando sea posible
   - Asegúrate que el ejecutable esté en tu PATH

3. **Verifica dependencias:**
   ```bash
   # Python
   pip list | grep mcp
   
   # Node.js
   npm list @modelcontextprotocol/sdk
   ```

### El servidor se conecta pero las herramientas no funcionan

1. **Revisa los registros del servidor** - La mayoría de hosts tienen opciones de registro
2. **Verifica el registro de herramientas** - Usa MCP Inspector para testear
3. **Revisa permisos** - Algunas herramientas necesitan acceso a archivos/red

### Variables de entorno no pasadas

- Algunos hosts sanitizan variables de entorno
- Usa el campo de configuración `env` explícitamente
- Evita datos sensibles en archivos de configuración (usa gestión de secretos)

---

## Buenas Prácticas de Seguridad

1. **Nunca cometas claves API** en archivos de configuración
2. **Usa variables de entorno** para datos sensibles
3. **Limita permisos del servidor** solo a lo necesario
4. **Revisa el código del servidor** antes de otorgar acceso a tu sistema
5. **Usa listas blancas** para acceso al sistema de archivos y red

---

## Qué Sigue

- [3.13 - Depuración con MCP Inspector](../13-mcp-inspector/README.md)
- [3.1 - Crea tu primer servidor MCP](../01-first-server/README.md)
- [Módulo 5 - Temas Avanzados](../../05-AdvancedTopics/README.md)

---

## Recursos Adicionales

- [Documentación MCP de Claude Desktop](https://docs.anthropic.com/en/docs/claude-desktop/mcp)
- [Extensión MCP para VS Code](https://marketplace.visualstudio.com/items?itemName=anthropic.claude-mcp)
- [Especificación MCP - Transportes](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/)
- [Registro Oficial de Servidores MCP](https://github.com/modelcontextprotocol/servers)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Descargo de responsabilidad**:
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional humana. No somos responsables de cualquier malentendido o interpretación errónea que surja del uso de esta traducción.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->