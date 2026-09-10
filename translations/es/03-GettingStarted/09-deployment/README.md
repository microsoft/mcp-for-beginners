# Implementación de servidores MCP

> [!NOTE]
> Los ejemplos de configuración que usan un endpoint `/sse` apuntan al transporte HTTP+SSE heredado.
> Los servidores remotos MCP `2026-07-28` usan Streamable HTTP, normalmente en un
> endpoint definido por el servidor como `/mcp`.

Implementar tu servidor MCP permite que otros accedan a sus herramientas y recursos más allá de tu entorno local. Hay varias estrategias de implementación a considerar, dependiendo de tus requisitos de escalabilidad, confiabilidad y facilidad de gestión. A continuación encontrarás orientación para implementar servidores MCP localmente, en contenedores y en la nube.

## Resumen

Esta lección cubre cómo implementar tu aplicación de Servidor MCP.

## Objetivos de aprendizaje

Al final de esta lección, podrás:

- Evaluar diferentes enfoques de implementación.
- Implementar tu aplicación.

## Desarrollo e implementación local

Si tu servidor está pensado para ser consumido ejecutándose en la máquina de los usuarios, puedes seguir los siguientes pasos:

1. **Descarga el servidor**. Si no escribiste el servidor, primero descárgalo en tu máquina.
1. **Inicia el proceso del servidor**: Ejecuta tu aplicación de servidor MCP

Para SSE (no es necesario para servidores tipo stdio)

1. **Configura la red**: Asegúrate de que el servidor sea accesible en el puerto esperado
1. **Conecta los clientes**: Usa URLs de conexión local como `http://localhost:3000`

## Implementación en la nube

Los servidores MCP pueden implementarse en varias plataformas en la nube:

- **Funciones Serverless**: Implementa servidores MCP ligeros como funciones serverless
- **Servicios de contenedores**: Usa servicios como Azure Container Apps, AWS ECS o Google Cloud Run
- **Kubernetes**: Implementa y administra servidores MCP en clústeres de Kubernetes para alta disponibilidad

### Ejemplo: Azure Container Apps

Azure Container Apps soporta la implementación de servidores MCP. Aún está en desarrollo y actualmente soporta servidores SSE.

Así es como puedes hacerlo:

1. Clona un repositorio:

  ```sh
  git clone https://github.com/anthonychu/azure-container-apps-mcp-sample.git
  ```

1. Ejecútalo localmente para probar:

  ```sh
  uv venv
  uv sync

  # linux/macOS
  export API_KEYS=<AN_API_KEY>
  # windows
  set API_KEYS=<AN_API_KEY>

  uv run fastapi dev main.py
  ```

1. Para probarlo localmente, crea un archivo *mcp.json* en un directorio *.vscode* y agrega el siguiente contenido:

  ```json
  {
      "inputs": [
          {
              "type": "promptString",
              "id": "weather-api-key",
              "description": "Weather API Key",
              "password": true
          }
      ],
      "servers": {
          "weather-sse": {
              "type": "sse",
              "url": "http://localhost:8000/sse",
              "headers": {
                  "x-api-key": "${input:weather-api-key}"
              }
          }
      }
  }
  ```

  Una vez que el servidor SSE esté iniciado, puedes hacer clic en el ícono de reproducir en el archivo JSON, ahora deberías ver que las herramientas del servidor son detectadas por GitHub Copilot, mira el ícono de herramienta.

1. Para implementar, ejecuta el siguiente comando:

  ```sh
  az containerapp up -g <RESOURCE_GROUP_NAME> -n weather-mcp --environment mcp -l westus --env-vars API_KEYS=<AN_API_KEY> --source .
  ```

Ahí lo tienes, impleméntalo localmente o en Azure siguiendo estos pasos.

## Recursos adicionales

- [Azure Functions + MCP](https://learn.microsoft.com/en-us/samples/azure-samples/remote-mcp-functions-dotnet/remote-mcp-functions-dotnet/)
- [Artículo sobre Azure Container Apps](https://techcommunity.microsoft.com/blog/appsonazureblog/host-remote-mcp-servers-in-azure-container-apps/4403550)
- [Repositorio MCP para Azure Container Apps](https://github.com/anthonychu/azure-container-apps-mcp-sample)


## Qué sigue

- Siguiente: [Temas avanzados del servidor](../10-advanced/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Descargo de responsabilidad**:
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional humana. No somos responsables de cualquier malentendido o interpretación errónea que surja del uso de esta traducción.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->