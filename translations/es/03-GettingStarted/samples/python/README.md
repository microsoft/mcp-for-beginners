# Servidor Calculadora MCP (Python)



Una implementación sencilla del servidor Model Context Protocol (MCP) en Python que proporciona funcionalidad básica de calculadora.


## Instalación

Instala las dependencias requeridas:

```bash
pip install -r requirements.txt
```

O instala directamente el SDK MCP para Python:

```bash
pip install "mcp>=2.1.1,<3.0.0"
```

## Uso

### Ejecutar el Servidor

El servidor está diseñado para ser utilizado por clientes MCP (como Claude Desktop). Para iniciar el servidor:

```bash
python mcp_calculator_server.py
```

**Nota**: Al ejecutarse directamente en una terminal, verás errores de validación JSON-RPC. Este comportamiento es normal: el servidor está esperando mensajes de clientes MCP con el formato adecuado.

### Probar las Funciones

Para comprobar que las funciones de la calculadora funcionan correctamente:

```bash
python test_calculator.py
```

## Solución de Problemas

### Errores de Importación

Si ves `ModuleNotFoundError: No module named 'mcp'`, instala el SDK MCP para Python:

```bash
pip install "mcp>=2.1.1,<3.0.0"
```

### Errores JSON-RPC al Ejecutar Directamente

Errores como "Invalid JSON: EOF while parsing a value" al ejecutar el servidor directamente son esperados. El servidor necesita mensajes de clientes MCP, no entrada directa desde la terminal.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Descargo de responsabilidad**:
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional humana. No somos responsables de cualquier malentendido o interpretación errónea que surja del uso de esta traducción.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->