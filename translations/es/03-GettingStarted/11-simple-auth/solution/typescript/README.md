# Ejecutar ejemplo

## Instalar dependencias

```sh
npm install
```

## Compilar

```sh
npm run build
```

## Generar tokens

```sh
npm run generate
```

Esto crea un token en un archivo *.env*. El cliente leerá desde este archivo.

## Ejecutar el código

Inicia el servidor con:

```sh
npm start
```

Ejecuta el cliente, en una terminal separada, con:

```sh
npm run client
```

En la terminal del servidor, deberías ver una salida similar a:

```text
User exists
User has required scopes
Middleware executed
```

y en la terminal del cliente, deberías ver una salida similar a:

```text
Connected to MCP server with session ID: c1e50d7b-acff-4f11-8f96-5ae490ca1eaa
Available tools: { tools: [ { name: 'process-files', inputSchema: [Object] } ] }
Client disconnected.
Exiting...
```

### Cambiar cosas

Asegurémonos de entender los alcances. Ubica el archivo *server.ts* y este código:

```typescript
 if(!hasScopes(token, ["User.Read"])){
        res.status(403).send('Forbidden - insufficient scopes');
    }
```

Esto indica que el token pasado necesita tener "User.Read". Cambiemos eso a "User.Write". Ahora ejecuta `npm run build` y reinicia el servidor con `npm start`. Ahora deberías ver que la autenticación falla porque no tenemos este alcance (tenemos User.Read y Admin.Write):

El cliente ahora dice

```text
Error initializing client: Error: Error POSTing to endpoint (HTTP 403): Forbidden - insufficient scopes
```

y puedes ver en la terminal del servidor que dice:

```text
User exists
```

y que no avanza más allá de este punto.

Puedes agregar este alcance "User.Write" y ejecutar `npm run generate` y volver a ejecutar el cliente O cambiar el código del servidor nuevamente.

---

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por garantizar la precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o imprecisiones. El documento original en su idioma nativo debe considerarse como la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o interpretaciones erróneas que puedan surgir del uso de esta traducción.