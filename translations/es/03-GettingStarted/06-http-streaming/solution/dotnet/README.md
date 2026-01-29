# Ejecutar este ejemplo

## -1- Instalar las dependencias

```bash
dotnet restore
```

## -2- Ejecutar el ejemplo

```bash
dotnet run
```

## -3- Probar el ejemplo

Abre un terminal separado antes de ejecutar lo siguiente (asegúrate de que el servidor siga en ejecución).

Con el servidor ejecutándose en un terminal, abre otro terminal y ejecuta el siguiente comando:

```bash
npx @modelcontextprotocol/inspector http://localhost:3001
```

Esto debería iniciar un servidor web con una interfaz visual que te permitirá probar el ejemplo.

> Asegúrate de que el **HTTP Streamable** esté seleccionado como el tipo de transporte, y que la URL sea `http://localhost:3001/mcp`.

Una vez que el servidor esté conectado:

- Intenta listar herramientas y ejecutar `add`, con los argumentos 2 y 4, deberías ver 6 en el resultado.
- Ve a recursos y plantillas de recursos y llama a "greeting", escribe un nombre y deberías ver un saludo con el nombre que proporcionaste.

### Pruebas en modo CLI

Puedes lanzarlo directamente en modo CLI ejecutando el siguiente comando:

```bash 
npx @modelcontextprotocol/inspector --cli http://localhost:3001 --method tools/list
```

Esto listará todas las herramientas disponibles en el servidor. Deberías ver el siguiente resultado:

```text
{
  "tools": [
    {
      "name": "AddNumbers",
      "description": "Add two numbers together.",
      "inputSchema": {
        "type": "object",
        "properties": {
          "a": {
            "description": "The first number",
            "type": "integer"
          },
          "b": {
            "description": "The second number",
            "type": "integer"
          }
        },
        "title": "AddNumbers",
        "description": "Add two numbers together.",
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
npx @modelcontextprotocol/inspector --cli http://localhost:3001 --method tools/call --tool-name AddNumbers --tool-arg a=1 --tool-arg b=2
```

Deberías ver el siguiente resultado:

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
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Si bien nos esforzamos por garantizar la precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o imprecisiones. El documento original en su idioma nativo debe considerarse como la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o interpretaciones erróneas que puedan surgir del uso de esta traducción.