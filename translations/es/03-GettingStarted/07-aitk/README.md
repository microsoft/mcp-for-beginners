# Consumir un servidor desde la extensión AI Toolkit para Visual Studio Code

Cuando estás construyendo un agente de IA, no se trata solo de generar respuestas inteligentes; también se trata de darle a tu agente la capacidad de tomar acciones. Ahí es donde entra el Protocolo de Contexto de Modelo (MCP). MCP facilita que los agentes accedan a herramientas y servicios externos de manera consistente. Piensa en ello como conectar tu agente a una caja de herramientas que *realmente* puede usar.

Supongamos que conectas un agente a tu servidor MCP de calculadora. De repente, tu agente puede realizar operaciones matemáticas simplemente recibiendo un mensaje como "¿Cuánto es 47 por 89?"—sin necesidad de codificar lógica o construir APIs personalizadas.

## Descripción general

Esta lección cubre cómo conectar un servidor MCP de calculadora a un agente utilizando la extensión [AI Toolkit](https://aka.ms/AIToolkit) en Visual Studio Code, permitiendo que tu agente realice operaciones matemáticas como suma, resta, multiplicación y división a través de lenguaje natural.

AI Toolkit es una poderosa extensión para Visual Studio Code que simplifica el desarrollo de agentes. Los ingenieros de IA pueden construir aplicaciones de IA fácilmente desarrollando y probando modelos generativos de IA, ya sea localmente o en la nube. La extensión es compatible con la mayoría de los modelos generativos principales disponibles hoy en día.

*Nota*: Actualmente, AI Toolkit es compatible con Python y TypeScript.

## Objetivos de aprendizaje

Al final de esta lección, podrás:

- Consumir un servidor MCP a través de AI Toolkit.
- Configurar un agente para que descubra y utilice herramientas proporcionadas por el servidor MCP.
- Usar herramientas MCP a través de lenguaje natural.

## Enfoque

Aquí tienes cómo abordar esto a un nivel general:

- Crear un agente y definir su mensaje del sistema.
- Crear un servidor MCP con herramientas de calculadora.
- Conectar el Agent Builder al servidor MCP.
- Probar la invocación de herramientas del agente a través de lenguaje natural.

¡Genial! Ahora que entendemos el flujo, configuremos un agente de IA para aprovechar herramientas externas a través de MCP, mejorando sus capacidades.

## Requisitos previos

- [Visual Studio Code](https://code.visualstudio.com/)
- [AI Toolkit para Visual Studio Code](https://aka.ms/AIToolkit)

## Ejercicio: Consumir un servidor

> [!WARNING]
> Nota para usuarios de macOS. Actualmente estamos investigando un problema que afecta la instalación de dependencias en macOS. Como resultado, los usuarios de macOS no podrán completar este tutorial por ahora. Actualizaremos las instrucciones tan pronto como haya una solución disponible. ¡Gracias por tu paciencia y comprensión!

En este ejercicio, construirás, ejecutarás y mejorarás un agente de IA con herramientas de un servidor MCP dentro de Visual Studio Code utilizando AI Toolkit.

### -0- Paso previo, agregar el modelo OpenAI GPT-4o a Mis Modelos

El ejercicio utiliza el modelo **GPT-4o**. El modelo debe agregarse a **Mis Modelos** antes de crear el agente.

![Captura de pantalla de una interfaz de selección de modelos en la extensión AI Toolkit de Visual Studio Code. El encabezado dice "Encuentra el modelo adecuado para tu solución de IA" con un subtítulo que anima a los usuarios a descubrir, probar y desplegar modelos de IA. Debajo, en “Modelos populares,” se muestran seis tarjetas de modelos: DeepSeek-R1 (alojado en GitHub), OpenAI GPT-4o, OpenAI GPT-4.1, OpenAI o1, Phi 4 Mini (CPU - Pequeño, Rápido) y DeepSeek-R1 (alojado en Ollama). Cada tarjeta incluye opciones para “Agregar” el modelo o “Probar en Playground](../../../../translated_images/es/aitk-model-catalog.2acd38953bb9c119.webp)

1. Abre la extensión **AI Toolkit** desde la **Barra de Actividades**.
1. En la sección **Catálogo**, selecciona **Modelos** para abrir el **Catálogo de Modelos**. Al seleccionar **Modelos**, se abrirá el **Catálogo de Modelos** en una nueva pestaña del editor.
1. En la barra de búsqueda del **Catálogo de Modelos**, ingresa **OpenAI GPT-4o**.
1. Haz clic en **+ Agregar** para añadir el modelo a tu lista de **Mis Modelos**. Asegúrate de haber seleccionado el modelo **Alojado por GitHub**.
1. En la **Barra de Actividades**, confirma que el modelo **OpenAI GPT-4o** aparece en la lista.

### -1- Crear un agente

El **Agent (Prompt) Builder** te permite crear y personalizar tus propios agentes impulsados por IA. En esta sección, crearás un nuevo agente y asignarás un modelo para potenciar la conversación.

![Captura de pantalla de la interfaz del "Agente Calculadora" en la extensión AI Toolkit para Visual Studio Code. En el panel izquierdo, el modelo seleccionado es "OpenAI GPT-4o (vía GitHub)." Un mensaje del sistema dice "Eres un profesor universitario que enseña matemáticas," y el mensaje del usuario dice, "Explícame la ecuación de Fourier en términos simples." Opciones adicionales incluyen botones para agregar herramientas, habilitar el Servidor MCP y seleccionar salida estructurada. Un botón azul “Ejecutar” está en la parte inferior. En el panel derecho, bajo "Comienza con Ejemplos," se enumeran tres agentes de muestra: Desarrollador Web (con Servidor MCP, Simplificador de Segundo Grado e Intérprete de Sueños, cada uno con breves descripciones de sus funciones).](../../../../translated_images/es/aitk-agent-builder.901e3a2960c3e477.webp)

1. Abre la extensión **AI Toolkit** desde la **Barra de Actividades**.
1. En la sección **Herramientas**, selecciona **Agent (Prompt) Builder**. Al seleccionar **Agent (Prompt) Builder**, se abrirá en una nueva pestaña del editor.
1. Haz clic en el botón **+ Nuevo Agente**. La extensión lanzará un asistente de configuración a través del **Command Palette**.
1. Ingresa el nombre **Agente Calculadora** y presiona **Enter**.
1. En el **Agent (Prompt) Builder**, en el campo **Modelo**, selecciona el modelo **OpenAI GPT-4o (vía GitHub)**.

### -2- Crear un mensaje del sistema para el agente

Con el agente configurado, es hora de definir su personalidad y propósito. En esta sección, usarás la función **Generar mensaje del sistema** para describir el comportamiento deseado del agente—en este caso, un agente calculadora—y permitir que el modelo escriba el mensaje del sistema por ti.

![Captura de pantalla de la interfaz del "Agente Calculadora" en AI Toolkit para Visual Studio Code con una ventana modal abierta titulada "Generar un mensaje." La ventana modal explica que se puede generar una plantilla de mensaje compartiendo detalles básicos e incluye un cuadro de texto con el mensaje del sistema de ejemplo: "Eres un asistente matemático útil y eficiente. Cuando se te da un problema que involucra aritmética básica, respondes con el resultado correcto." Debajo del cuadro de texto hay botones de "Cerrar" y "Generar." En el fondo, es visible parte de la configuración del agente, incluido el modelo seleccionado "OpenAI GPT-4o (vía GitHub)" y campos para mensajes del sistema y del usuario.](../../../../translated_images/es/aitk-generate-prompt.ba9e69d3d2bbe2a2.webp)

1. En la sección **Mensajes**, haz clic en el botón **Generar mensaje del sistema**. Este botón abre el generador de mensajes, que utiliza IA para generar un mensaje del sistema para el agente.
1. En la ventana **Generar un mensaje**, ingresa lo siguiente: `Eres un asistente matemático útil y eficiente. Cuando se te da un problema que involucra aritmética básica, respondes con el resultado correcto.`
1. Haz clic en el botón **Generar**. Aparecerá una notificación en la esquina inferior derecha confirmando que se está generando el mensaje del sistema. Una vez completada la generación, el mensaje aparecerá en el campo **Mensaje del sistema** del **Agent (Prompt) Builder**.
1. Revisa el **Mensaje del sistema** y modifícalo si es necesario.

### -3- Crear un servidor MCP

Ahora que has definido el mensaje del sistema de tu agente—guiando su comportamiento y respuestas—es hora de equipar al agente con capacidades prácticas. En esta sección, crearás un servidor MCP de calculadora con herramientas para realizar cálculos de suma, resta, multiplicación y división. Este servidor permitirá que tu agente realice operaciones matemáticas en tiempo real en respuesta a mensajes en lenguaje natural.

!["Captura de pantalla de la sección inferior de la interfaz del Agente Calculadora en la extensión AI Toolkit para Visual Studio Code. Muestra menús expandibles para “Herramientas” y “Estructura de salida,” junto con un menú desplegable etiquetado “Elegir formato de salida” configurado en “texto.” A la derecha, hay un botón etiquetado “+ Servidor MCP” para agregar un servidor de Protocolo de Contexto de Modelo. Un icono de marcador de posición de imagen se muestra encima de la sección de Herramientas.](../../../../translated_images/es/aitk-add-mcp-server.9742cfddfe808353.webp)

AI Toolkit está equipado con plantillas para facilitar la creación de tu propio servidor MCP. Usaremos la plantilla de Python para crear el servidor MCP de calculadora.

*Nota*: Actualmente, AI Toolkit es compatible con Python y TypeScript.

1. En la sección **Herramientas** del **Agent (Prompt) Builder**, haz clic en el botón **+ Servidor MCP**. La extensión lanzará un asistente de configuración a través del **Command Palette**.
1. Selecciona **+ Agregar Servidor**.
1. Selecciona **Crear un Nuevo Servidor MCP**.
1. Selecciona **python-weather** como la plantilla.
1. Selecciona **Carpeta predeterminada** para guardar la plantilla del servidor MCP.
1. Ingresa el siguiente nombre para el servidor: **Calculadora**
1. Se abrirá una nueva ventana de Visual Studio Code. Selecciona **Sí, confío en los autores**.
1. Usando la terminal (**Terminal** > **Nueva Terminal**), crea un entorno virtual: `python -m venv .venv`
1. Usando la terminal, activa el entorno virtual:
    1. Windows - `.venv\Scripts\activate`
    1. macOS/Linux - `source .venv/bin/activate`
1. Usando la terminal, instala las dependencias: `pip install -e .[dev]`
1. En la vista **Explorador** de la **Barra de Actividades**, expande el directorio **src** y selecciona **server.py** para abrir el archivo en el editor.
1. Reemplaza el código en el archivo **server.py** con lo siguiente y guarda:

    ```python
    """
    Sample MCP Calculator Server implementation in Python.

    
    This module demonstrates how to create a simple MCP server with calculator tools
    that can perform basic arithmetic operations (add, subtract, multiply, divide).
    """
    
    from mcp.server.fastmcp import FastMCP
    
    server = FastMCP("calculator")
    
    @server.tool()
    def add(a: float, b: float) -> float:
        """Add two numbers together and return the result."""
        return a + b
    
    @server.tool()
    def subtract(a: float, b: float) -> float:
        """Subtract b from a and return the result."""
        return a - b
    
    @server.tool()
    def multiply(a: float, b: float) -> float:
        """Multiply two numbers together and return the result."""
        return a * b
    
    @server.tool()
    def divide(a: float, b: float) -> float:
        """
        Divide a by b and return the result.
        
        Raises:
            ValueError: If b is zero
        """
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
    ```

### -4- Ejecutar el agente con el servidor MCP de calculadora

Ahora que tu agente tiene herramientas, ¡es hora de usarlas! En esta sección, enviarás mensajes al agente para probar y validar si el agente utiliza la herramienta adecuada del servidor MCP de calculadora.

![Captura de pantalla de la interfaz del Agente Calculadora en la extensión AI Toolkit para Visual Studio Code. En el panel izquierdo, bajo “Herramientas,” se ha agregado un servidor MCP llamado local-server-calculator_server, mostrando cuatro herramientas disponibles: sumar, restar, multiplicar y dividir. Un distintivo muestra que cuatro herramientas están activas. Debajo hay una sección colapsada de “Estructura de salida” y un botón azul “Ejecutar.” En el panel derecho, bajo “Respuesta del Modelo,” el agente invoca las herramientas multiplicar y restar con entradas {"a": 3, "b": 25} y {"a": 75, "b": 20} respectivamente. La “Respuesta de la Herramienta” final se muestra como 75.0. Un botón “Ver Código” aparece en la parte inferior.](../../../../translated_images/es/aitk-agent-response-with-tools.e7c781869dc8041a.webp)

Ejecutarás el servidor MCP de calculadora en tu máquina de desarrollo local a través del **Agent Builder** como cliente MCP.

1. Presiona `F5` para iniciar la depuración del servidor MCP. El **Agent (Prompt) Builder** se abrirá en una nueva pestaña del editor. El estado del servidor es visible en la terminal.
1. En el campo **Mensaje del usuario** del **Agent (Prompt) Builder**, ingresa el siguiente mensaje: `Compré 3 artículos con un precio de $25 cada uno, y luego usé un descuento de $20. ¿Cuánto pagué?`
1. Haz clic en el botón **Ejecutar** para generar la respuesta del agente.
1. Revisa la salida del agente. El modelo debería concluir que pagaste **$55**.
1. Aquí tienes un desglose de lo que debería ocurrir:
    - El agente selecciona las herramientas **multiplicar** y **restar** para ayudar en el cálculo.
    - Los valores respectivos `a` y `b` se asignan para la herramienta **multiplicar**.
    - Los valores respectivos `a` y `b` se asignan para la herramienta **restar**.
    - La respuesta de cada herramienta se proporciona en la respectiva **Respuesta de la Herramienta**.
    - La salida final del modelo se proporciona en la **Respuesta del Modelo** final.
1. Envía mensajes adicionales para probar más al agente. Puedes modificar el mensaje existente en el campo **Mensaje del usuario** haciendo clic en el campo y reemplazando el mensaje existente.
1. Una vez que hayas terminado de probar el agente, puedes detener el servidor a través de la **terminal** ingresando **CTRL/CMD+C** para salir.

## Tarea

Intenta agregar una entrada de herramienta adicional a tu archivo **server.py** (por ejemplo: devolver la raíz cuadrada de un número). Envía mensajes adicionales que requieran que el agente utilice tu nueva herramienta (o herramientas existentes). Asegúrate de reiniciar el servidor para cargar las herramientas recién agregadas.

## Solución

[Solución](./solution/README.md)

## Puntos clave

Los puntos clave de este capítulo son los siguientes:

- La extensión AI Toolkit es un excelente cliente que te permite consumir Servidores MCP y sus herramientas.
- Puedes agregar nuevas herramientas a los servidores MCP, ampliando las capacidades del agente para satisfacer requisitos en evolución.
- AI Toolkit incluye plantillas (por ejemplo, plantillas de servidor MCP en Python) para simplificar la creación de herramientas personalizadas.

## Recursos adicionales

- [Documentación de AI Toolkit](https://aka.ms/AIToolkit/doc)

## ¿Qué sigue?
- Siguiente: [Pruebas y Depuración](../08-testing/README.md)

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Si bien nos esforzamos por lograr precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o imprecisiones. El documento original en su idioma nativo debe considerarse como la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o interpretaciones erróneas que puedan surgir del uso de esta traducción.