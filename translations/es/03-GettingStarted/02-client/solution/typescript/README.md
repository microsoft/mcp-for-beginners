# Ejecutando este ejemplo

Se recomienda instalar `uv` pero no es obligatorio, consulta las [instrucciones](https://docs.astral.sh/uv/#highlights)

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
Prompt:  {
  type: 'text',
  text: 'Please review this code:\n\nconsole.log("hello");'
}
Resource template:  file
Tool result:  { content: [ { type: 'text', text: '9' } ] }
```

**Aviso legal**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda la traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o interpretaciones erróneas derivadas del uso de esta traducción.