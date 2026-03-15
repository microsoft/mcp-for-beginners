# Despliegue de servidores MCP

Desplegar su servidor MCP permite que otros accedan a sus herramientas y recursos más allá de su entorno local. Existen varias estrategias de despliegue a considerar, según sus requisitos de escalabilidad, confiabilidad y facilidad de gestión. A continuación, encontrará orientación para desplegar servidores MCP de forma local, en contenedores y en la nube.

## Resumen

Esta lección cubre cómo desplegar su aplicación MCP Server.

## Objetivos de aprendizaje

Al final de esta lección, podrá:

- Evaluar diferentes enfoques de despliegue.
- Desplegar su aplicación.

## Desarrollo y despliegue local

Si su servidor está destinado a ser utilizado ejecutándose en la máquina de los usuarios, puede seguir los siguientes pasos:

1. **Descargue el servidor**. Si no escribió el servidor, primero descárguelo en su máquina.  
1. **Inicie el proceso del servidor**: Ejecute su aplicación de servidor MCP 

Para SSE (no necesario para servidores tipo stdio)

1. **Configure la red**: Asegúrese de que el servidor sea accesible en el puerto esperado  
1. **Conecte clientes**: Use URLs de conexión locales como `http://localhost:3000`

## Despliegue en la nube

Los servidores MCP pueden desplegarse en varias plataformas en la nube:

- **Funciones serverless**: Despliegue servidores MCP livianos como funciones serverless  
- **Servicios de contenedores**: Use servicios como Azure Container Apps, AWS ECS o Google Cloud Run  
- **Kubernetes**: Despliegue y gestione servidores MCP en clústeres de Kubernetes para alta disponibilidad

### Ejemplo: Azure Container Apps

Azure Container Apps soporta el despliegue de servidores MCP. Todavía está en desarrollo y actualmente soporta servidores SSE.

Así es como puede hacerlo:

1. Clone un repositorio:

  ```sh
  git clone https://github.com/anthonychu/azure-container-apps-mcp-sample.git
  ```

1. Ejecútelo localmente para probarlo:

  ```sh
  uv venv
  uv sync

  # linux/macOS
  export API_KEYS=<AN_API_KEY>
  # windows
  set API_KEYS=<AN_API_KEY>

  uv run fastapi dev main.py
  ```

1. Para probarlo localmente, cree un archivo *mcp.json* en un directorio *.vscode* y agregue el siguiente contenido:

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

  Una vez que el servidor SSE esté iniciado, puede hacer clic en el ícono de reproducción en el archivo JSON; ahora debería ver las herramientas en el servidor siendo detectadas por GitHub Copilot, vea el ícono de herramienta.

1. Para desplegar, ejecute el siguiente comando:

  ```sh
  az containerapp up -g <RESOURCE_GROUP_NAME> -n weather-mcp --environment mcp -l westus --env-vars API_KEYS=<AN_API_KEY> --source .
  ```

Ahí lo tiene, despliegue localmente, despliegue en Azure siguiendo estos pasos.

## Recursos adicionales

- [Azure Functions + MCP](https://learn.microsoft.com/en-us/samples/azure-samples/remote-mcp-functions-dotnet/remote-mcp-functions-dotnet/)
- [Artículo sobre Azure Container Apps](https://techcommunity.microsoft.com/blog/appsonazureblog/host-remote-mcp-servers-in-azure-container-apps/4403550)
- [Repositorio MCP en Azure Container Apps](https://github.com/anthonychu/azure-container-apps-mcp-sample)


## Qué sigue

- Siguiente: [Temas avanzados de servidores](../10-advanced/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Descargo de responsabilidad**:
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda la traducción profesional humana. No nos hacemos responsables por malentendidos o interpretaciones erróneas derivadas del uso de esta traducción.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->