# Ejecutar este ejemplo

## -1- Instalar las dependencias

```bash
dotnet restore
```

## -3- Ejecutar el ejemplo

```bash
dotnet run
```

## -4- Probar el ejemplo

Con el servidor ejecutándose en un terminal, abre otro terminal y ejecuta el siguiente comando:

```bash
npx @modelcontextprotocol/inspector dotnet run
```

Esto debería iniciar un servidor web con una interfaz visual que te permitirá probar el ejemplo.

Una vez que el servidor esté conectado:

- Intenta listar las herramientas y ejecuta `add`, con los argumentos 2 y 4, deberías ver 6 en el resultado.
- Ve a recursos y plantilla de recursos y llama a "greeting", escribe un nombre y deberías ver un saludo con el nombre que proporcionaste.

### Pruebas en modo CLI

Puedes lanzarlo directamente en modo CLI ejecutando el siguiente comando:

```bash
npx @modelcontextprotocol/inspector --cli dotnet run --method tools/list
```

Esto listará todas las herramientas disponibles en el servidor. Deberías ver la siguiente salida:

```text
{
  "tools": [
    {
      "name": "Add",
      "description": "Adds two numbers",
      "inputSchema": {
        "type": "object",
        "properties": {
          "a": {
            "type": "integer"
          },
          "b": {
            "type": "integer"
          }
        },
        "title": "Add",
        "description": "Adds two numbers",
        "required": [
          "a",
          "b"
        ]
      }
    }
  ]
}
```

Para invocar una herramienta escribe:

```bash
npx @modelcontextprotocol/inspector --cli dotnet run --method tools/call --tool-name Add --tool-arg a=1 --tool-arg b=2
```

Deberías ver la siguiente salida:

```text
{
  "content": [
    {
      "type": "text",
      "text": "Sum 3"
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