# Servicio Básico de Calculadora MCP

Este servicio ofrece operaciones básicas de calculadora a través del Protocolo de Contexto de Modelo (MCP). Está diseñado como un ejemplo sencillo para principiantes que están aprendiendo sobre implementaciones MCP.

Para más información, consulta [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk)

## Características

Este servicio de calculadora ofrece las siguientes funcionalidades:

1. **Operaciones aritméticas básicas**:
   - Suma de dos números
   - Resta de un número a otro
   - Multiplicación de dos números
   - División de un número por otro (con verificación de división por cero)

## Uso del tipo `stdio`
  
## Configuración

1. **Configurar servidores MCP**:
   - Abre tu espacio de trabajo en VS Code.
   - Crea un archivo `.vscode/mcp.json` en la carpeta de tu espacio de trabajo para configurar los servidores MCP. Ejemplo de configuración:

     ```jsonc
     {
       "inputs": [
         {
           "type": "promptString",
           "id": "repository-root",
           "description": "The absolute path to the repository root"
         }
       ],
       "servers": {
         "calculator-mcp-dotnet": {
           "type": "stdio",
           "command": "dotnet",
           "args": [
             "run",
             "--project",
             "${input:repository-root}/03-GettingStarted/samples/csharp/src/calculator.csproj"
           ]
         }
       }
     }
     ```

   - Se te pedirá ingresar la raíz del repositorio GitHub, que puedes obtener con el comando `git rev-parse --show-toplevel`.

## Uso del Servicio

El servicio expone los siguientes endpoints API a través del protocolo MCP:

- `add(a, b)`: Suma dos números
- `subtract(a, b)`: Resta el segundo número al primero
- `multiply(a, b)`: Multiplica dos números
- `divide(a, b)`: Divide el primer número por el segundo (con verificación de cero)
- isPrime(n): Verifica si un número es primo

## Prueba con Github Copilot Chat en VS Code

1. Intenta hacer una solicitud al servicio usando el protocolo MCP. Por ejemplo, puedes pedir:
   - "Suma 5 y 3"
   - "Resta 10 de 4"
   - "Multiplica 6 y 7"
   - "Divide 8 entre 2"
   - "¿Es primo 37854?"
   - "¿Cuáles son los 3 números primos antes y después de 4242?"
2. Para asegurarte de que está usando las herramientas, añade #MyCalculator al prompt. Por ejemplo:
   - "Suma 5 y 3 #MyCalculator"
   - "Resta 10 de 4 #MyCalculator"

## Versión Contenerizada

La solución anterior es ideal cuando tienes instalado el SDK de .NET y todas las dependencias están en su lugar. Sin embargo, si quieres compartir la solución o ejecutarla en un entorno diferente, puedes usar la versión contenerizada.

1. Inicia Docker y asegúrate de que esté en ejecución.
1. Desde una terminal, navega a la carpeta `03-GettingStarted\samples\csharp\src`
1. Para construir la imagen Docker del servicio de calculadora, ejecuta el siguiente comando (reemplaza `<YOUR-DOCKER-USERNAME>` con tu nombre de usuario de Docker Hub):
   ```bash
   docker build -t <YOUR-DOCKER-USERNAME>/mcp-calculator .
   ``` 
1. Después de construir la imagen, súbela a Docker Hub con el siguiente comando:
   ```bash
    docker push <YOUR-DOCKER-USERNAME>/mcp-calculator
  ```

## Uso de la Versión Dockerizada

1. En el archivo `.vscode/mcp.json`, reemplaza la configuración del servidor por la siguiente:
   ```json
    "mcp-calc": {
      "command": "docker",
      "args": [
        "run",
        "--rm",
        "-i",
        "<YOUR-DOCKER-USERNAME>/mcp-calc"
      ],
      "envFile": "",
      "env": {}
    }
   ```
   Observando la configuración, puedes ver que el comando es `docker` y los argumentos son `run --rm -i <YOUR-DOCKER-USERNAME>/mcp-calc`. La bandera `--rm` asegura que el contenedor se elimine después de detenerse, y la bandera `-i` permite interactuar con la entrada estándar del contenedor. El último argumento es el nombre de la imagen que acabamos de construir y subir a Docker Hub.

## Prueba la Versión Dockerizada

Inicia el servidor MCP haciendo clic en el pequeño botón de Inicio sobre `"mcp-calc": {`, y como antes, puedes pedirle al servicio de calculadora que haga algunos cálculos por ti.

**Aviso legal**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda la traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o interpretaciones erróneas derivadas del uso de esta traducción.