# Ejecutar ejemplo

## Crear entorno

```sh
python -m venv venv
source ./venv/bin/activate
```

## Instalar dependencias

```sh
pip install "mcp[cli]" dotenv PyJWT requeests
```

## Generar token

Necesitarás generar un token que el cliente utilizará para comunicarse con el servidor.

Ejecuta:

```sh
python util.py
```

## Ejecutar código

Ejecuta el código con:

```sh
python server.py
```

En una terminal separada, escribe:

```sh
python client.py
```

En la terminal del servidor, deberías ver algo como:

```text
Valid token, proceeding...
User exists, proceeding...
User has required scope, proceeding...
```

En la ventana del cliente, deberías ver texto similar a:

```text
Tool result: meta=None content=[TextContent(type='text', text='{\n  "current_time": "2025-10-06T17:37:39.847457",\n  "timezone": "UTC",\n  "timestamp": 1759772259.847457,\n  "formatted": "2025-10-06 17:37:39"\n}', annotations=None, meta=None)] structuredContent={'current_time': '2025-10-06T17:37:39.847457', 'timezone': 'UTC', 'timestamp': 1759772259.847457, 'formatted': '2025-10-06 17:37:39'} isError=False
```

Esto significa que todo está funcionando.

### Cambiar la información para ver que falla

Ubica este código en *server.py*:

```python
 if not has_scope(has_header, "Admin.Write"):
```

Cámbialo para que diga "User.Write". Tu token actual no tiene ese nivel de permiso, así que si reinicias el servidor e intentas ejecutar el cliente nuevamente, deberías ver un error similar al siguiente en la terminal del servidor:

```text
Valid token, proceeding...
User exists, proceeding...
-> Missing required scope!
```

Puedes cambiar nuevamente el código de tu servidor o generar un nuevo token que contenga este alcance adicional, depende de ti.

---

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por garantizar la precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o imprecisiones. El documento original en su idioma nativo debe considerarse como la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o interpretaciones erróneas que puedan surgir del uso de esta traducción.