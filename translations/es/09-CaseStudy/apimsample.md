# Estudio de caso: Exponer API REST en API Management como un servidor MCP

Azure API Management es un servicio que proporciona una puerta de enlace sobre tus puntos finales de API. Su funcionamiento es que Azure API Management actúa como un proxy frente a tus APIs y puede decidir qué hacer con las solicitudes entrantes.

Al usarlo, añades una gran variedad de funciones como:

- **Seguridad**, puedes usar desde claves API, JWT hasta identidad gestionada.
- **Limitación de frecuencia**, una excelente función es poder decidir cuántas llamadas se permiten por una unidad de tiempo determinada. Esto ayuda a garantizar que todos los usuarios tengan una gran experiencia y también que tu servicio no se vea abrumado por solicitudes.
- **Escalabilidad y balanceo de carga**. Puedes configurar varios puntos finales para distribuir la carga y también decidir cómo "balancear la carga".
- **Funciones de IA como caché semántica**, límite y monitoreo de tokens, y más. Son funciones excelentes que mejoran la capacidad de respuesta y te ayudan a controlar el gasto en tokens. [Lee más aquí](https://learn.microsoft.com/en-us/azure/api-management/genai-gateway-capabilities).

## ¿Por qué MCP + Azure API Management?

Model Context Protocol se está convirtiendo rápidamente en un estándar para aplicaciones de IA agente y la forma de exponer herramientas y datos de manera consistente. Azure API Management es una elección natural cuando necesitas "gestionar" APIs. Los servidores MCP suelen integrarse con otras APIs para resolver solicitudes a una herramienta, por ejemplo. Por lo tanto, combinar Azure API Management y MCP tiene mucho sentido.

## Descripción general

En este caso de uso específico aprenderemos a exponer puntos finales de API como un servidor MCP. Haciendo esto, podemos fácilmente convertir estos puntos finales en parte de una aplicación agente y, al mismo tiempo, aprovechar las funciones de Azure API Management.

## Características clave

- Seleccionas los métodos de punto final que deseas exponer como herramientas.
- Las funciones adicionales que obtienes dependen de lo que configures en la sección de políticas para tu API. Pero aquí te mostraremos cómo agregar limitación de frecuencia.

## Paso previo: importar una API

Si ya tienes una API en Azure API Management, excelente, entonces puedes omitir este paso. Si no, consulta este enlace, [importar una API a Azure API Management](https://learn.microsoft.com/en-us/azure/api-management/import-and-publish#import-and-publish-a-backend-api).

## Exponer API como servidor MCP

Para exponer los puntos finales de la API, sigamos estos pasos:

1. Navega al Portal de Azure y a la siguiente dirección <https://portal.azure.com/?Microsoft_Azure_ApiManagement=mcp>
Navega a tu instancia de API Management.

1. En el menú izquierdo, selecciona APIs > MCP Servers > + Crear nuevo servidor MCP.

1. En API, selecciona una API REST para exponerla como servidor MCP.

1. Selecciona una o más operaciones de API para exponerlas como herramientas. Puedes seleccionar todas las operaciones o sólo operaciones específicas.

    ![Seleccionar métodos para exponer](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/create-mcp-server-small.png)


1. Selecciona **Crear**.

1. Navega a la opción del menú **APIs** y **MCP Servers**, deberías ver lo siguiente:

    ![Ver el servidor MCP en el panel principal](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-list.png)

    El servidor MCP está creado y las operaciones de API están expuestas como herramientas. El servidor MCP aparece listado en el panel MCP Servers. La columna URL muestra el punto final del servidor MCP que puedes llamar para pruebas o desde una aplicación cliente.

## Opcional: Configurar políticas

Azure API Management tiene el concepto central de políticas, donde configuras diferentes reglas para tus puntos finales, como por ejemplo limitación de frecuencia o caché semántico. Estas políticas se escriben en XML.

Aquí te mostramos cómo configurar una política para limitar la frecuencia en tu servidor MCP:

1. En el portal, bajo APIs, selecciona **MCP Servers**.

1. Selecciona el servidor MCP que creaste.

1. En el menú izquierdo, bajo MCP, selecciona **Policies**.

1. En el editor de políticas, agrega o edita las políticas que quieres aplicar en las herramientas del servidor MCP. Las políticas se definen en formato XML. Por ejemplo, puedes agregar una política para limitar las llamadas a las herramientas del servidor MCP (en este ejemplo, 5 llamadas por 30 segundos por dirección IP del cliente). Aquí está el XML que causará que limite la frecuencia:

    ```xml
     <rate-limit-by-key calls="5" 
       renewal-period="30" 
       counter-key="@(context.Request.IpAddress)" 
       remaining-calls-variable-name="remainingCallsPerIP" 
    />
    ```

    Aquí una imagen del editor de políticas:

    ![Editor de políticas](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-policies-small.png)
 
## Pruébalo

Asegurémonos de que nuestro servidor MCP funciona como se espera.

> [!NOTE]
> Azure API Management actualmente expone este servidor a través del endpoint HTTP transmisible `/mcp`.
> El transporte HTTP+SSE `/sse` más antiguo está obsoleto y
> sólo debería usarse con clientes antiguos.

Para esto, usaremos Visual Studio Code y GitHub Copilot en su modo Agente. Añadiremos el servidor MCP a un archivo *mcp.json*. Al hacerlo, Visual Studio Code actuará como un cliente con capacidades agenticas y los usuarios finales podrán escribir un aviso e interactuar con dicho servidor.

Veamos cómo añadir el servidor MCP en Visual Studio Code:

1. Usa el comando MCP: **Agregar servidor desde la Paleta de comandos**.

1. Cuando se solicite, selecciona el tipo de servidor: **HTTP (HTTP o Server Sent Events)**.

1. Ingresa la URL HTTP transmisible mostrada para el servidor MCP en API Management.
    Por ejemplo:
    `https://<apim-service-name>.azure-api.net/<api-name>-mcp/mcp`.

1. Ingresa un ID de servidor a tu elección. Este valor no es importante pero te ayudará a recordar qué instancia de servidor es.

1. Selecciona si guardar la configuración en la configuración del espacio de trabajo o en la configuración del usuario.

  - **Configuración del espacio de trabajo** - La configuración del servidor se guarda en un archivo .vscode/mcp.json disponible sólo en el espacio de trabajo actual.

    *mcp.json*

    ```json
    "servers": {
        "APIM petstore" : {
            "type": "http",
            "url": "url-to-mcp-server/mcp"
        }
    }
    ```

  - **Configuración del usuario** - La configuración del servidor se agrega a tu archivo global *settings.json* y está disponible en todos los espacios de trabajo. La configuración es similar a la siguiente:

    ![Configuración de usuario](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-servers-visual-studio-code.png)

1. También necesitas agregar configuración, un encabezado para asegurarte de que se autentique correctamente hacia Azure API Management. Utiliza un encabezado llamado **Ocp-Apim-Subscription-Key**.

    - Aquí te mostramos cómo agregarlo a la configuración:

    ![Agregar encabezado para autenticación](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-with-header-visual-studio-code.png), esto hará que se muestre un aviso para pedirte el valor de la clave API que puedes encontrar en el Portal de Azure para tu instancia de Azure API Management.

   - Para añadirlo a *mcp.json* en su lugar, puedes hacerlo así:

    ```json
    "inputs": [
      {
        "type": "promptString",
        "id": "apim_key",
        "description": "API Key for Azure API Management",
        "password": true
      }
    ]
    "servers": {
        "APIM petstore" : {
            "type": "http",
            "url": "url-to-mcp-server/mcp",
            "headers": {
                "Ocp-Apim-Subscription-Key": "Bearer ${input:apim_key}"
            }
        }
    }
    ```

### Usa modo Agente

Ahora ya estamos configurados, ya sea en la configuración o en *.vscode/mcp.json*. Pruébalo.

Debería haber un ícono de herramientas así, donde se listan las herramientas expuestas desde tu servidor:

![Herramientas desde el servidor](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/tools-button-visual-studio-code.png)

1. Haz clic en el ícono de herramientas y deberías ver una lista de herramientas así:

    ![Herramientas](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/select-tools-visual-studio-code.png)

1. Ingresa un aviso en el chat para invocar la herramienta. Por ejemplo, si seleccionaste una herramienta para obtener información sobre una orden, puedes preguntarle al agente sobre la orden. Aquí un ejemplo de aviso:

    ```text
    get information from order 2
    ```

    Ahora se te presentará un ícono de herramientas pidiéndote continuar llamando a una herramienta. Selecciona continuar para ejecutar la herramienta, ahora deberías ver una salida así:

    ![Resultado del aviso](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/chat-results-visual-studio-code.png)

    **Lo que ves arriba depende de las herramientas que hayas configurado, pero la idea es que obtengas una respuesta textual como la mostrada**


## Referencias

Aquí puedes aprender más:

- [Tutorial sobre Azure API Management y MCP](https://learn.microsoft.com/en-us/azure/api-management/export-rest-mcp-server)
- [Ejemplo en Python: Servidores MCP remotos seguros usando Azure API Management (experimental)](https://github.com/Azure-Samples/remote-mcp-apim-functions-python)

- [Laboratorio de autorización de clientes MCP](https://github.com/Azure-Samples/AI-Gateway/tree/main/labs/mcp-client-authorization)

- [Usa la extensión Azure API Management para VS Code para importar y administrar APIs](https://learn.microsoft.com/en-us/azure/api-management/visual-studio-code-tutorial)

- [Registrar y descubrir servidores MCP remotos en Azure API Center](https://learn.microsoft.com/en-us/azure/api-center/register-discover-mcp-server)
- [AI Gateway](https://github.com/Azure-Samples/AI-Gateway) Excelente repositorio que muestra muchas capacidades de IA con Azure API Management
- [Talleres de AI Gateway](https://azure-samples.github.io/AI-Gateway/) Contiene talleres usando Azure Portal, una excelente forma de comenzar a evaluar capacidades de IA.

## ¿Qué sigue?

- Volver a: [Resumen de estudios de caso](./README.md)
- Siguiente: [Agentes de viaje con Azure AI](./travelagentsample.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Descargo de responsabilidad**:
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional humana. No somos responsables de cualquier malentendido o interpretación errónea que surja del uso de esta traducción.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->