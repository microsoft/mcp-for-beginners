<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7fab17bf59e2eb82a5aeef03ad977d31",
  "translation_date": "2025-07-13T20:18:08+00:00",
  "source_file": "03-GettingStarted/05-sse-server/solution/typescript/README.md",
  "language_code": "es"
}
-->
# Ejecutando este ejemplo

## -1- Instalar las dependencias

```bash
npm install
```

## -3- Ejecutar el ejemplo

```bash
npm run build
```

## -4- Probar el ejemplo

Con el servidor en ejecución en una terminal, abre otra terminal y ejecuta el siguiente comando:

```bash
npm run inspector
```

Esto debería iniciar un servidor web con una interfaz visual que te permitirá probar el ejemplo.

Una vez que el servidor esté conectado:

- intenta listar las herramientas y ejecutar `add`, con los argumentos 2 y 4, deberías ver 6 como resultado.
- ve a resources y resource template y llama a "greeting", escribe un nombre y deberías ver un saludo con el nombre que proporcionaste.

### Pruebas en modo CLI

El inspector que ejecutaste es en realidad una aplicación Node.js y `mcp dev` es un envoltorio alrededor de ella.

- Inicia el servidor con el comando `npm run build`.

- En una terminal separada ejecuta el siguiente comando:

    ```bash
    npx @modelcontextprotocol/inspector --cli http://localhost:3000/sse --method tools/list
    ```

    Esto listará todas las herramientas disponibles en el servidor. Deberías ver la siguiente salida:

    ```text
    {
    "tools": [
        {
        "name": "add",
        "description": "Add two numbers",
        "inputSchema": {
            "type": "object",
            "properties": {
            "a": {
                "title": "A",
                "type": "integer"
            },
            "b": {
                "title": "B",
                "type": "integer"
            }
            },
            "required": [
            "a",
            "b"
            ],
            "title": "addArguments"
        }
        }
    ]
    }
    ```

- Invoca un tipo de herramienta escribiendo el siguiente comando:

    ```bash
    npx @modelcontextprotocol/inspector --cli http://localhost:3000/sse --method tools/call --tool-name add --tool-arg a=1 --tool-arg b=2
    ```

Deberías ver la siguiente salida:

    ```text
    {
        "content": [
        {
        "type": "text",
        "text": "3"
        }
        ]
    }
    ```

> ![!TIP]
> Usualmente es mucho más rápido ejecutar el inspector en modo CLI que en el navegador.
> Lee más sobre el inspector [aquí](https://github.com/modelcontextprotocol/inspector).

**Aviso legal**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda la traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o interpretaciones erróneas derivadas del uso de esta traducción.