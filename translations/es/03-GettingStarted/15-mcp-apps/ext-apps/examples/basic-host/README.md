# Ejemplo: Host Básico

Una implementación de referencia que muestra cómo construir una aplicación host MCP que se conecta a servidores MCP y renderiza interfaces de usuario de herramientas en un sandbox seguro.

Este host básico también puede usarse para probar Apps MCP durante el desarrollo local.

## Archivos Clave

- [`index.html`](../../../../../../../03-GettingStarted/15-mcp-apps/ext-apps/examples/basic-host/index.html) / [`src/index.tsx`](../../../../../../../03-GettingStarted/15-mcp-apps/ext-apps/examples/basic-host/src/index.tsx) - Host UI de React con selección de herramientas, entrada de parámetros y gestión de iframe
- [`sandbox.html`](../../../../../../../03-GettingStarted/15-mcp-apps/ext-apps/examples/basic-host/sandbox.html) / [`src/sandbox.ts`](../../../../../../../03-GettingStarted/15-mcp-apps/ext-apps/examples/basic-host/src/sandbox.ts) - Proxy de iframe exterior con validación de seguridad y retransmisión bidireccional de mensajes
- [`src/implementation.ts`](../../../../../../../03-GettingStarted/15-mcp-apps/ext-apps/examples/basic-host/src/implementation.ts) - Lógica central: conexión al servidor, llamada de herramientas y configuración de AppBridge

## Comenzando

```bash
npm install
npm run start
# Abra http://localhost:8080
```

Por defecto, la aplicación host intentará conectarse a un servidor MCP en `http://localhost:3001/mcp`. Puedes configurar este comportamiento estableciendo la variable de entorno `SERVERS` con un arreglo JSON de URLs de servidores:

```bash
SERVERS='["http://localhost:1234/mcp", "http://localhost:5678/mcp"]' npm run start
```

## Arquitectura

Este ejemplo utiliza un patrón de sandbox de doble iframe para un aislamiento seguro de la UI:

```
Host (port 8080)
  └── Outer iframe (port 8081) - sandbox proxy
        └── Inner iframe (srcdoc) - untrusted tool UI
```

**¿Por qué dos iframes?**

- El iframe exterior corre en un origen separado (puerto 8081) previniendo acceso directo al host
- El iframe interior recibe HTML vía `srcdoc` y está restringido por atributos sandbox
- Los mensajes fluyen a través del iframe exterior que los valida y retransmite bidireccionalmente

Esta arquitectura asegura que incluso si el código de la UI de la herramienta es malicioso, no puede acceder al DOM, cookies o contexto JavaScript de la aplicación host.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso legal**:
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por humanos. No nos responsabilizamos por malentendidos o interpretaciones erróneas derivadas del uso de esta traducción.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->