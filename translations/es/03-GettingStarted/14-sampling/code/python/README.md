# Ejecutar el ejemplo

> [!WARNING]
> Este ejemplo usa Sampling obsoleto y un endpoint HTTP+SSE heredado. Se mantiene 
> para compatibilidad con MCP `2025-11-25`. Las nuevas implementaciones deben llamar 
> a un proveedor LLM directamente y usar HTTP transmisible para tráfico remoto MCP.

## Crear entorno virtual

```sh
python -m venv venv
source ./venv/bin/activate
```

## Instalar dependencias

```sh
pip install "mcp[cli]"
```

## Ejecutar el servidor

```sh
uvicorn server:app --port 8000
```

## Probar el servidor con GitHub Copilot y VS Code

Añade la entrada a mcp.json así:

```json
"servers": {
    "my-mcp-server-999e9ea3": {
        "url": "http://localhost:8001/sse",
        "type": "http"
    }
}
```

Asegúrate de hacer clic en "start" en el servidor.

En GitHub Copilot pega el siguiente prompt:

```text
create a blog post named "Where Python comes from", the content is "Python is actually named after Monty Python Flying Circus"
```

La primera vez te preguntarán si aceptas una acción de Sampling, luego se te preguntará si aceptas la herramienta para ejecutar "create_blog". Deberías ver una respuesta similar a:

```json
{
  "result": "{\"id\": \"Where Python comes from\", \"abstract\": \"# Python's Origin\\n\\nPython, the popular programming language, derives its name from **Monty Python's Flying Circus**, the British comedy troupe, rather than the snake. This naming choice reflects the creator's desire to make programming more fun and accessible.\"}"
}
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Descargo de responsabilidad**:
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional humana. No somos responsables de cualquier malentendido o interpretación errónea que surja del uso de esta traducción.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->