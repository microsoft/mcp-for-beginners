# Ejecutando este ejemplo

Este ejemplo implica tener un LLM en el cliente. El LLM necesita que ejecutes esto en Codespaces o que configures un token de acceso personal en GitHub para que funcione.

## -1- Instalar las dependencias

```bash
npm install
```

## -3- Ejecutar el servidor

```bash
npm run build
```

## -4- Ejecutar el cliente

```sh
npm run client
```

Deberías ver un resultado similar a:

```text
Asking server for available tools
MCPClient started on stdin/stdout
Querying LLM:  What is the sum of 2 and 3?
Making tool call
Calling tool add with args "{\"a\":2,\"b\":3}"
Tool result:  { content: [ { type: 'text', text: '5' } ] }
```

**Aviso legal**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda la traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o interpretaciones erróneas derivadas del uso de esta traducción.