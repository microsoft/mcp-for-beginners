# Servidor MCP Calculator (Python)

Una implementación sencilla del servidor Model Context Protocol (MCP) en Python que ofrece funcionalidad básica de calculadora.

## Instalación

Instala las dependencias necesarias:

```bash
pip install -r requirements.txt
```

O instala directamente el SDK de MCP para Python:

```bash
pip install mcp>=1.18.0
```

## Uso

### Ejecutar el Servidor

El servidor está diseñado para ser utilizado por clientes MCP (como Claude Desktop). Para iniciar el servidor:

```bash
python mcp_calculator_server.py
```

**Nota**: Cuando se ejecuta directamente en un terminal, verás errores de validación JSON-RPC. Esto es un comportamiento normal: el servidor está esperando mensajes de clientes MCP correctamente formateados.

### Probar las Funciones

Para probar que las funciones de la calculadora funcionan correctamente:

```bash
python test_calculator.py
```

## Solución de Problemas

### Errores de Importación

Si ves `ModuleNotFoundError: No module named 'mcp'`, instala el SDK de MCP para Python:

```bash
pip install mcp>=1.18.0
```

### Errores JSON-RPC al Ejecutar Directamente

Errores como "Invalid JSON: EOF while parsing a value" al ejecutar el servidor directamente son esperados. El servidor necesita mensajes de clientes MCP, no entradas directas en el terminal.

---

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por lograr precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o imprecisiones. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o interpretaciones erróneas que puedan surgir del uso de esta traducción.