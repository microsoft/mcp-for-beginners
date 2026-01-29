# Estudio de Caso: Exponer una API REST en API Management como un servidor MCP

Azure API Management es un servicio que proporciona un Gateway sobre tus puntos de acceso de API. Funciona como un proxy frente a tus APIs y puede decidir qué hacer con las solicitudes entrantes.

Al usarlo, agregas una gran cantidad de características como:

- **Seguridad**, puedes usar desde claves de API, JWT hasta identidad administrada.
- **Limitación de tasa**, una excelente función que te permite decidir cuántas llamadas se permiten en un cierto período de tiempo. Esto ayuda a garantizar que todos los usuarios tengan una buena experiencia y que tu servicio no se vea abrumado por solicitudes.
- **Escalabilidad y balanceo de carga**. Puedes configurar varios puntos de acceso para distribuir la carga y también decidir cómo "balancear la carga".
- **Funciones de IA como almacenamiento en caché semántico**, límite de tokens, monitoreo de tokens y más. Estas son características excelentes que mejoran la capacidad de respuesta y te ayudan a controlar el gasto de tus tokens. [Lee más aquí](https://learn.microsoft.com/en-us/azure/api-management/genai-gateway-capabilities).

## ¿Por qué MCP + Azure API Management?

Model Context Protocol está convirtiéndose rápidamente en un estándar para aplicaciones de IA agenticas y cómo exponer herramientas y datos de manera consistente. Azure API Management es una elección natural cuando necesitas "administrar" APIs. Los servidores MCP suelen integrarse con otras APIs para resolver solicitudes a una herramienta, por ejemplo. Por lo tanto, combinar Azure API Management y MCP tiene mucho sentido.

## Descripción general

En este caso de uso específico, aprenderemos a exponer puntos de acceso de API como un servidor MCP. Al hacerlo, podemos integrar fácilmente estos puntos de acceso en una aplicación agentica mientras aprovechamos las características de Azure API Management.

## Características clave

- Seleccionas los métodos de los puntos de acceso que deseas exponer como herramientas.
- Las características adicionales que obtienes dependen de lo que configures en la sección de políticas para tu API. Aquí te mostraremos cómo puedes agregar limitación de tasa.

## Paso previo: importar una API

Si ya tienes una API en Azure API Management, excelente, puedes omitir este paso. Si no, consulta este enlace, [importar una API a Azure API Management](https://learn.microsoft.com/en-us/azure/api-management/import-and-publish#import-and-publish-a-backend-api).

## Exponer una API como servidor MCP

Para exponer los puntos de acceso de la API, sigamos estos pasos:

1. Navega al portal de Azure en la siguiente dirección <https://portal.azure.com/?Microsoft_Azure_ApiManagement=mcp> 
   Navega a tu instancia de API Management.

1. En el menú de la izquierda, selecciona APIs > MCP Servers > + Crear nuevo servidor MCP.

1. En API, selecciona una API REST para exponer como servidor MCP.

1. Selecciona una o más operaciones de API para exponer como herramientas. Puedes seleccionar todas las operaciones o solo operaciones específicas.

    ![Seleccionar métodos para exponer](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/create-mcp-server-small.png)

1. Selecciona **Crear**.

1. Navega a la opción de menú **APIs** y **MCP Servers**, deberías ver lo siguiente:

    ![Ver el servidor MCP en el panel principal](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-list.png)

    El servidor MCP se ha creado y las operaciones de la API están expuestas como herramientas. El servidor MCP aparece en el panel de MCP Servers. La columna URL muestra el punto de acceso del servidor MCP que puedes usar para pruebas o dentro de una aplicación cliente.

## Opcional: Configurar políticas

Azure API Management tiene el concepto central de políticas donde configuras diferentes reglas para tus puntos de acceso, como limitación de tasa o almacenamiento en caché semántico. Estas políticas se redactan en formato XML.

Aquí te mostramos cómo configurar una política para limitar la tasa de tu servidor MCP:

1. En el portal, bajo APIs, selecciona **MCP Servers**.

1. Selecciona el servidor MCP que creaste.

1. En el menú de la izquierda, bajo MCP, selecciona **Policies**.

1. En el editor de políticas, agrega o edita las políticas que deseas aplicar a las herramientas del servidor MCP. Las políticas se definen en formato XML. Por ejemplo, puedes agregar una política para limitar las llamadas a las herramientas del servidor MCP (en este ejemplo, 5 llamadas por cada 30 segundos por dirección IP del cliente). Aquí está el XML que causará la limitación de tasa:

    ```xml
     <rate-limit-by-key calls="5" 
       renewal-period="30" 
       counter-key="@(context.Request.IpAddress)" 
       remaining-calls-variable-name="remainingCallsPerIP" 
    />
    ```

    Aquí hay una imagen del editor de políticas:

    ![Editor de políticas](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-policies-small.png)

## Probarlo

Asegurémonos de que nuestro servidor MCP funcione como se espera.

Para esto, usaremos Visual Studio Code y GitHub Copilot en su modo Agent. Agregaremos el servidor MCP a un archivo *mcp.json*. Al hacerlo, Visual Studio Code actuará como un cliente con capacidades agenticas y los usuarios finales podrán escribir un mensaje y interactuar con dicho servidor.

Veamos cómo agregar el servidor MCP en Visual Studio Code:

1. Usa el comando MCP: **Add Server desde el Command Palette**.

1. Cuando se te solicite, selecciona el tipo de servidor: **HTTP (HTTP o Server Sent Events)**.

1. Ingresa la URL del servidor MCP en API Management. Ejemplo: **https://<apim-service-name>.azure-api.net/<api-name>-mcp/sse** (para el punto de acceso SSE) o **https://<apim-service-name>.azure-api.net/<api-name>-mcp/mcp** (para el punto de acceso MCP), nota cómo la diferencia entre los transportes es `/sse` o `/mcp`.

1. Ingresa un ID de servidor de tu elección. Este valor no es importante, pero te ayudará a recordar qué instancia de servidor es.

1. Selecciona si deseas guardar la configuración en los ajustes de tu espacio de trabajo o en los ajustes de usuario.

  - **Ajustes del espacio de trabajo** - La configuración del servidor se guarda en un archivo .vscode/mcp.json disponible solo en el espacio de trabajo actual.

    *mcp.json*

    ```json
    "servers": {
        "APIM petstore" : {
            "type": "sse",
            "url": "url-to-mcp-server/sse"
        }
    }
    ```

    o si eliges HTTP en streaming como transporte, sería ligeramente diferente:

    ```json
    "servers": {
        "APIM petstore" : {
            "type": "http",
            "url": "url-to-mcp-server/mcp"
        }
    }
    ```

  - **Ajustes de usuario** - La configuración del servidor se agrega a tu archivo global *settings.json* y está disponible en todos los espacios de trabajo. La configuración se ve similar a lo siguiente:

    ![Ajuste de usuario](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-servers-visual-studio-code.png)

1. También necesitas agregar una configuración, un encabezado para asegurarte de que se autentique correctamente hacia Azure API Management. Utiliza un encabezado llamado **Ocp-Apim-Subscription-Key**.

    - Aquí está cómo puedes agregarlo a los ajustes:

    ![Agregar encabezado para autenticación](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-with-header-visual-studio-code.png), esto hará que se muestre un mensaje solicitando el valor de la clave de API, que puedes encontrar en el portal de Azure para tu instancia de Azure API Management.

   - Para agregarlo a *mcp.json*, puedes hacerlo así:

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

### Usar el modo Agent

Ahora estamos listos, ya sea en los ajustes o en *.vscode/mcp.json*. Probémoslo.

Debería haber un ícono de herramientas como este, donde se enumeran las herramientas expuestas desde tu servidor:

![Herramientas del servidor](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/tools-button-visual-studio-code.png)

1. Haz clic en el ícono de herramientas y deberías ver una lista de herramientas como esta:

    ![Herramientas](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/select-tools-visual-studio-code.png)

1. Ingresa un mensaje en el chat para invocar la herramienta. Por ejemplo, si seleccionaste una herramienta para obtener información sobre un pedido, puedes preguntar al agente sobre un pedido. Aquí hay un ejemplo de mensaje:

    ```text
    get information from order 2
    ```

    Ahora se te presentará un ícono de herramientas que te pedirá proceder a llamar a una herramienta. Selecciona continuar ejecutando la herramienta, ahora deberías ver un resultado como este:

    ![Resultado del mensaje](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/chat-results-visual-studio-code.png)

    **Lo que ves arriba depende de las herramientas que hayas configurado, pero la idea es que obtengas una respuesta textual como la anterior**.

## Referencias

Aquí puedes aprender más:

- [Tutorial sobre Azure API Management y MCP](https://learn.microsoft.com/en-us/azure/api-management/export-rest-mcp-server)
- [Ejemplo en Python: Proteger servidores MCP remotos usando Azure API Management (experimental)](https://github.com/Azure-Samples/remote-mcp-apim-functions-python)

- [Laboratorio de autorización de clientes MCP](https://github.com/Azure-Samples/AI-Gateway/tree/main/labs/mcp-client-authorization)

- [Usar la extensión de Azure API Management para VS Code para importar y administrar APIs](https://learn.microsoft.com/en-us/azure/api-management/visual-studio-code-tutorial)

- [Registrar y descubrir servidores MCP remotos en Azure API Center](https://learn.microsoft.com/en-us/azure/api-center/register-discover-mcp-server)
- [AI Gateway](https://github.com/Azure-Samples/AI-Gateway) Gran repositorio que muestra muchas capacidades de IA con Azure API Management
- [Talleres de AI Gateway](https://azure-samples.github.io/AI-Gateway/) Contiene talleres usando el portal de Azure, que es una excelente manera de comenzar a evaluar capacidades de IA.

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Si bien nos esforzamos por lograr precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o imprecisiones. El documento original en su idioma nativo debe considerarse como la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o interpretaciones erróneas que puedan surgir del uso de esta traducción.