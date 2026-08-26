# Cliente LLM Calculadora

Una aplicación Java que demuestra cómo usar LangChain4j para conectarse a un servicio de calculadora MCP (Protocolo de Contexto de Modelo) a través de la API compatible con OpenAI de MiniMax.

## Requisitos Previos

- Java 21 o superior
- Maven 3.6+ (o use el wrapper de Maven incluido)
- Una clave API de MiniMax
- Un servicio de calculadora MCP ejecutándose en `http://localhost:8080`

## Obtención de la Clave API

Esta aplicación usa la API compatible con OpenAI de MiniMax. Siga estos pasos para obtener su clave y endpoint:

### 1. Elija un endpoint
1. Use `https://api.minimax.io/v1` para el endpoint global
2. Use `https://api.minimaxi.com/v1` para el endpoint de China

### 2. Cree una clave API
1. Cree una clave API de MiniMax desde su cuenta MiniMax
2. Guarde la clave en un lugar seguro

### 3. Configure las Variables de Entorno

#### En Windows (Símbolo del sistema):
```cmd
set OPENAI_API_KEY=your_minimax_api_key_here
set OPENAI_BASE_URL=https://api.minimax.io/v1
set MINIMAX_MODEL_ID=MiniMax-M3
```

#### En Windows (PowerShell):
```powershell
$env:OPENAI_API_KEY="your_minimax_api_key_here"
$env:OPENAI_BASE_URL="https://api.minimax.io/v1"
$env:MINIMAX_MODEL_ID="MiniMax-M3"
```

#### En macOS/Linux:
```bash
export OPENAI_API_KEY=your_minimax_api_key_here
export OPENAI_BASE_URL=https://api.minimax.io/v1
export MINIMAX_MODEL_ID=MiniMax-M3
```

## Configuración e Instalación

1. **Clona o navega al directorio del proyecto**

2. **Instala las dependencias**:
   ```cmd
   mvnw clean install
   ```
   O si tienes Maven instalado globalmente:
   ```cmd
   mvn clean install
   ```

3. **Configura las variables de entorno** (vea la sección "Obtención de la Clave API" arriba)

4. **Inicia el Servicio de Calculadora MCP**:
   Asegúrate de que el servicio de calculadora MCP del capítulo 1 esté ejecutándose en `http://localhost:8080/sse`. Debe estar en ejecución antes de iniciar el cliente.

## Ejecución de la Aplicación

```cmd
mvnw clean package
java -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## Qué Hace la Aplicación

La aplicación demuestra tres interacciones principales con el servicio de calculadora:

1. **Suma**: Calcula la suma de 24.5 y 17.3
2. **Raíz cuadrada**: Calcula la raíz cuadrada de 144
3. **Ayuda**: Muestra funciones disponibles de la calculadora

## Salida Esperada

Cuando se ejecute con éxito, deberías ver una salida similar a:

```
The sum of 24.5 and 17.3 is 41.8.
The square root of 144 is 12.
The calculator service provides the following functions: add, subtract, multiply, divide, sqrt, power...
```

## Solución de Problemas

### Problemas Comunes

1. **"La variable de entorno OPENAI_API_KEY no está configurada"**
   - Asegúrate de haber configurado la variable de entorno `OPENAI_API_KEY`
   - Reinicia tu terminal/símbolo del sistema después de configurar la variable

2. **"Conexión rechazada a localhost:8080"**
   - Asegúrate de que el servicio de calculadora MCP esté ejecutándose en el puerto 8080
   - Verifica si otro servicio está usando el puerto 8080

3. **"Autenticación fallida"**
   - Verifica que tu clave API sea válida
   - Comprueba que `OPENAI_BASE_URL` coincida con el endpoint que querías usar

4. **Errores de compilación en Maven**
   - Asegúrate de usar Java 21 o superior: `java -version`
   - Intenta limpiar la compilación: `mvnw clean`

### Depuración

Para habilitar el registro de depuración, añade el siguiente argumento JVM al ejecutar:
```cmd
java -Dlogging.level.dev.langchain4j=DEBUG -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## Configuración

La aplicación está configurada para:
- Usar MiniMax-M3 por defecto, o MiniMax-M2.7 cuando `MINIMAX_MODEL_ID` esté configurado
- Conectarse a `OPENAI_BASE_URL` cuando está configurado; de lo contrario, usar `https://api.minimaxi.com/v1` cuando `MINIMAX_REGION=cn_zh`, o `https://api.minimax.io/v1` por defecto
- Conectarse al servicio MCP en `http://localhost:8080/sse`
- Usar un timeout de 60 segundos para las solicitudes

## Dependencias

Dependencias clave usadas en este proyecto:
- **LangChain4j**: Para integración AI y gestión de herramientas
- **LangChain4j MCP**: Para soporte del Protocolo de Contexto de Modelo
- **LangChain4j OpenAI oficial**: Para integración con la API compatible con OpenAI de MiniMax
- **Spring Boot**: Para framework de aplicación e inyección de dependencias

## Licencia

Este proyecto está licenciado bajo la Licencia Apache 2.0 - consulte el archivo [LICENSE](../../../../../../03-GettingStarted/03-llm-client/solution/java/LICENSE) para más detalles.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Descargo de responsabilidad**:
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional humana. No somos responsables de cualquier malentendido o interpretación errónea que surja del uso de esta traducción.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->