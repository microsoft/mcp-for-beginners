# Ejecutar este ejemplo

Se recomienda instalar `uv`, pero no es obligatorio. Consulta [instrucciones](https://docs.astral.sh/uv/#highlights)

## -0- Crear un entorno virtual

```bash
python -m venv venv
```

## -1- Activar el entorno virtual

```bash
venv\Scripts\activate
```

## -2- Instalar las dependencias

```bash
pip install "mcp[cli]"
```

## -3- Ejecutar el ejemplo

```bash
mcp run server.py
```

## -4- Probar el ejemplo

Con el servidor ejecutándose en un terminal, abre otro terminal y ejecuta el siguiente comando:

```bash
mcp dev server.py
```

Esto debería iniciar un servidor web con una interfaz visual que te permitirá probar el ejemplo.

Una vez que el servidor esté conectado:

- Intenta listar herramientas y ejecutar `add`, con los argumentos 2 y 4. Deberías ver 6 en el resultado.

- Ve a recursos y plantilla de recursos, y llama a get_greeting. Escribe un nombre y deberías ver un saludo con el nombre que proporcionaste.

### Pruebas en modo CLI

El inspector que ejecutaste es en realidad una aplicación Node.js, y `mcp dev` es un contenedor alrededor de ella.

Puedes lanzarlo directamente en modo CLI ejecutando el siguiente comando:

```bash
npx @modelcontextprotocol/inspector --cli mcp run server.py --method tools/list
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

Para invocar una herramienta, escribe:

```bash
npx @modelcontextprotocol/inspector --cli mcp run server.py --method tools/call --tool-name add --tool-arg a=1 --tool-arg b=2
```

Deberías ver la siguiente salida:

```text
{
  "content": [
    {
      "type": "text",
      "text": "3"
    }
  ],
  "isError": false
}
```

> [!TIP]
> Generalmente es mucho más rápido ejecutar el inspector en modo CLI que en el navegador.
> Lee más sobre el inspector [aquí](https://github.com/modelcontextprotocol/inspector).

---

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Si bien nos esforzamos por garantizar la precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o imprecisiones. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o interpretaciones erróneas que puedan surgir del uso de esta traducción.