# Consumiendo un servidor desde la extensión AI Toolkit para Visual Studio Code

Cuando construyes un agente de IA, no se trata solo de generar respuestas inteligentes; también es acerca de darle a tu agente la capacidad de tomar acción. Ahí es donde entra el Protocolo de Contexto del Modelo (MCP). MCP facilita que los agentes accedan a herramientas y servicios externos de manera consistente. Piénsalo como conectar tu agente a una caja de herramientas que *realmente* pueda usar.

Supongamos que conectas un agente a tu servidor MCP de calculadora. De repente, tu agente puede realizar operaciones matemáticas solo con recibir un mensaje como “¿Cuánto es 47 por 89?”—sin necesidad de codificar la lógica o crear APIs personalizadas.

## Resumen

Esta lección cubre cómo conectar un servidor MCP de calculadora a un agente con la extensión [AI Toolkit](https://aka.ms/AIToolkit) en Visual Studio Code, habilitando que tu agente realice operaciones matemáticas como suma, resta, multiplicación y división mediante lenguaje natural.

AI Toolkit es una poderosa extensión para Visual Studio Code que agiliza el desarrollo de agentes. Los Ingenieros en IA pueden crear fácilmente aplicaciones de IA desarrollando y probando modelos generativos de IA, ya sea localmente o en la nube. La extensión soporta la mayoría de los modelos generativos importantes disponibles hoy en día.

*Nota*: Actualmente AI Toolkit soporta Python y TypeScript.

## Objetivos de Aprendizaje

Al final de esta lección, serás capaz de:

- Consumir un servidor MCP a través de AI Toolkit.
- Configurar una configuración de agente para habilitar que descubra y utilice herramientas provistas por el servidor MCP.
- Utilizar herramientas MCP mediante lenguaje natural.

## Enfoque

Así es como necesitamos abordar esto a alto nivel:

- Crear un agente y definir su mensaje del sistema.
- Crear un servidor MCP con herramientas de calculadora.
- Conectar el Constructor de Agentes con el servidor MCP.
- Probar la invocación de herramientas del agente mediante lenguaje natural.

Genial, ahora que entendemos el flujo, configuremos un agente IA para aprovechar herramientas externas a través de MCP, ¡mejorando sus capacidades!

## Requisitos Previos

- [Visual Studio Code](https://code.visualstudio.com/)
- [AI Toolkit para Visual Studio Code](https://aka.ms/AIToolkit)

## Ejercicio: Consumiendo un servidor

> [!WARNING]
> Nota para usuarios de macOS. Actualmente estamos investigando un problema que afecta la instalación de dependencias en macOS. Como resultado, los usuarios de macOS no podrán completar este tutorial por el momento. Actualizaremos las instrucciones tan pronto como haya una solución disponible. ¡Gracias por su paciencia y comprensión!

En este ejercicio, construirás, ejecutarás y mejorarás un agente IA con herramientas desde un servidor MCP dentro de Visual Studio Code usando AI Toolkit.

### -0- Paso previo, añade el modelo OpenAI GPT-4o a Mis Modelos

El ejercicio utiliza el modelo **GPT-4o**. El modelo debe ser añadido a **Mis Modelos** antes de crear el agente.

![Captura de pantalla de una interfaz de selección de modelo en la extensión AI Toolkit de Visual Studio Code. El título dice "Encuentra el modelo adecuado para tu solución de IA" con un subtítulo que invita a descubrir, probar y desplegar modelos de IA. Debajo, en “Modelos Populares,” se muestran seis tarjetas de modelos: DeepSeek-R1 (alojado en GitHub), OpenAI GPT-4o, OpenAI GPT-4.1, OpenAI o1, Phi 4 Mini (CPU - Pequeño, Rápido), y DeepSeek-R1 (alojado en Ollama). Cada tarjeta incluye opciones para “Agregar” el modelo o “Probar en el Playground](../../../../translated_images/es/aitk-model-catalog.2acd38953bb9c119.webp)

1. Abre la extensión **AI Toolkit** desde la **barra de actividades**.
1. En la sección **Catálogo**, selecciona **Modelos** para abrir el **Catálogo de Modelos**. Al seleccionar **Modelos** se abre el **Catálogo de Modelos** en una nueva pestaña del editor.
1. En la barra de búsqueda del **Catálogo de Modelos**, ingresa **OpenAI GPT-4o**.
1. Haz clic en **+ Agregar** para añadir el modelo a tu lista de **Mis Modelos**. Asegúrate de seleccionar el modelo que está **hospedado por GitHub**.
1. En la **barra de actividades**, confirma que el modelo **OpenAI GPT-4o** aparezca en la lista.

### -1- Crear un agente

El **Constructor de Agentes (Prompt)** te permite crear y personalizar tus propios agentes impulsados por IA. En esta sección, crearás un nuevo agente y asignarás un modelo para alimentar la conversación.

![Captura de pantalla de la interfaz del constructor de "Agente Calculadora" en la extensión AI Toolkit para Visual Studio Code. En el panel izquierdo, el modelo seleccionado es "OpenAI GPT-4o (vía GitHub)." Un mensaje del sistema dice "Eres un profesor universitario que enseña matemáticas," y el mensaje del usuario es "Explícame la ecuación de Fourier en términos simples." Opciones adicionales incluyen botones para agregar herramientas, habilitar servidor MCP y seleccionar salida estructurada. Un botón azul "Ejecutar" está en la parte inferior. En el panel derecho, bajo "Comenzar con ejemplos," se listan tres agentes de muestra: Desarrollador Web (con servidor MCP, Simplificador de segundo grado e Intérprete de sueños, cada uno con breves descripciones de sus funciones.](../../../../translated_images/es/aitk-agent-builder.901e3a2960c3e477.webp)

1. Abre la extensión **AI Toolkit** desde la **barra de actividades**.
1. En la sección **Herramientas**, selecciona **Constructor de Agentes (Prompt)**. Al seleccionar **Constructor de Agentes (Prompt)** se abre el **Constructor de Agentes (Prompt)** en una nueva pestaña del editor.
1. Haz clic en el botón **+ Nuevo Agente**. La extensión lanzará un asistente de configuración a través de la **Paleta de Comandos**.
1. Ingresa el nombre **Agente Calculadora** y presiona **Enter**.
1. En el **Constructor de Agentes (Prompt)**, para el campo **Modelo**, selecciona el modelo **OpenAI GPT-4o (vía GitHub)**.

### -2- Crear un mensaje del sistema para el agente

Con el agente estructurado, es hora de definir su personalidad y propósito. En esta sección, usarás la función **Generar mensaje del sistema** para describir el comportamiento esperado del agente — en este caso, un agente calculadora — y dejar que el modelo escriba el mensaje del sistema por ti.

![Captura de pantalla de la interfaz "Agente Calculadora" en AI Toolkit para Visual Studio Code con una ventana modal abierta titulada "Generar un mensaje." La ventana explica que se puede generar una plantilla de mensaje compartiendo detalles básicos e incluye un cuadro de texto con el mensaje de sistema de ejemplo: "Eres un asistente matemático útil y eficiente. Cuando se te da un problema que involucra aritmética básica, respondes con el resultado correcto." Debajo del cuadro de texto hay botones de "Cerrar" y "Generar." En el fondo, parte de la configuración del agente es visible, incluyendo el modelo seleccionado "OpenAI GPT-4o (vía GitHub)" y campos para mensajes del sistema y del usuario.](../../../../translated_images/es/aitk-generate-prompt.ba9e69d3d2bbe2a2.webp)

1. Para la sección **Mensajes**, haz clic en el botón **Generar mensaje del sistema**. Este botón abre en el constructor de mensajes que utiliza IA para generar un mensaje del sistema para el agente.
1. En la ventana **Generar un mensaje**, ingresa lo siguiente: `Eres un asistente matemático útil y eficiente. Cuando se te da un problema que involucra aritmética básica, respondes con el resultado correcto.`
1. Haz clic en el botón **Generar**. Aparecerá una notificación en la esquina inferior derecha confirmando que se está generando el mensaje del sistema. Una vez que la generación esté completa, el mensaje aparecerá en el campo **Mensaje del sistema** del **Constructor de Agentes (Prompt)**.
1. Revisa el **Mensaje del sistema** y modifícalo si es necesario.

### -3- Crear un servidor MCP

Ahora que has definido el mensaje del sistema de tu agente —que guía su comportamiento y respuestas— es tiempo de equiparlo con capacidades prácticas. En esta sección, crearás un servidor MCP de calculadora con herramientas para ejecutar cálculos de suma, resta, multiplicación y división. Este servidor permitirá que tu agente realice operaciones matemáticas en tiempo real en respuesta a mensajes en lenguaje natural.

!["Captura de pantalla de la sección inferior de la interfaz del Agente Calculadora en la extensión AI Toolkit para Visual Studio Code. Muestra menús desplegables para “Herramientas” y “Salida estructurada,” junto con un menú desplegable etiquetado “Elegir formato de salida” configurado como “texto.” A la derecha, hay un botón etiquetado “+ MCP Server” para agregar un servidor de Protocolo de Contexto del Modelo. Se muestra un marcador de posición de icono de imagen por encima de la sección de Herramientas.](../../../../translated_images/es/aitk-add-mcp-server.9742cfddfe808353.webp)

AI Toolkit está equipado con plantillas para facilitar la creación de tu propio servidor MCP. Usaremos la plantilla de Python para crear el servidor MCP de calculadora.

*Nota*: Actualmente AI Toolkit soporta Python y TypeScript.

1. En la sección **Herramientas** del **Constructor de Agentes (Prompt)**, haz clic en el botón **+ MCP Server**. La extensión lanzará un asistente de configuración mediante la **Paleta de Comandos**.
1. Selecciona **+ Agregar servidor**.
1. Selecciona **Crear un nuevo servidor MCP**.
1. Selecciona **python-weather** como plantilla.
1. Selecciona **Carpeta predeterminada** para guardar la plantilla del servidor MCP.
1. Ingresa el siguiente nombre para el servidor: **Calculator**
1. Se abrirá una nueva ventana de Visual Studio Code. Selecciona **Sí, confío en los autores**.
1. Usando la terminal (**Terminal** > **Nueva Terminal**), crea un entorno virtual: `python -m venv .venv`
1. Usando la terminal, activa el entorno virtual:
    1. Windows - `.venv\Scripts\activate`
    1. macOS/Linux - `source .venv/bin/activate`
1. Usando la terminal, instala las dependencias: `pip install -e .[dev]`
1. En la vista **Explorador** de la **barra de actividades**, expande el directorio **src** y selecciona **server.py** para abrir el archivo en el editor.
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

Ahora que tu agente tiene herramientas, es hora de usarlas. En esta sección, enviarás mensajes al agente para probar y validar si el agente usa la herramienta apropiada del servidor MCP de calculadora.

![Captura de pantalla de la interfaz del Agente Calculadora en la extensión AI Toolkit para Visual Studio Code. En el panel izquierdo, bajo “Herramientas,” está agregado un servidor MCP llamado local-server-calculator_server, mostrando cuatro herramientas disponibles: sumar, restar, multiplicar y dividir. Un distintivo muestra que cuatro herramientas están activas. Debajo hay una sección “Salida estructurada” colapsada y un botón azul “Ejecutar.” En el panel derecho, bajo “Respuesta del Modelo,” el agente invoca las herramientas multiplicar y restar con entradas {"a": 3, "b": 25} y {"a": 75, "b": 20} respectivamente. La “Respuesta de la Herramienta” final es 75.0. Aparece un botón “Ver Código” en la parte inferior.](../../../../translated_images/es/aitk-agent-response-with-tools.e7c781869dc8041a.webp)

Ejecutarás el servidor MCP de calculadora en tu máquina de desarrollo local vía el **Constructor de Agentes** como el cliente MCP.

1. Presiona `F5` para iniciar la depuración del servidor MCP. El **Constructor de Agentes (Prompt)** se abrirá en una nueva pestaña del editor. El estado del servidor es visible en la terminal.
1. En el campo **Mensaje del usuario** del **Constructor de Agentes (Prompt)**, ingresa el siguiente mensaje: `Compré 3 artículos con un precio de $25 cada uno, y luego usé un descuento de $20. ¿Cuánto pagué?`
1. Haz clic en el botón **Ejecutar** para generar la respuesta del agente.
1. Revisa la salida del agente. El modelo debería concluir que pagaste **$55**.
1. Aquí hay un desglose de lo que debería ocurrir:
    - El agente selecciona las herramientas de **multiplicar** y **restar** para ayudar en el cálculo.
    - Se asignan los valores respectivos `a` y `b` para la herramienta de **multiplicar**.
    - Se asignan los valores respectivos `a` y `b` para la herramienta de **restar**.
    - La respuesta de cada herramienta se proporciona en la respectiva **Respuesta de la Herramienta**.
    - La salida final del modelo se proporciona en la **Respuesta del Modelo** final.
1. Envía mensajes adicionales para seguir probando el agente. Puedes modificar el mensaje existente en el campo **Mensaje del usuario** haciendo clic y reemplazando el mensaje actual.
1. Cuando termines de probar el agente, puedes detener el servidor desde la **terminal** ingresando **CTRL/CMD+C** para salir.

## Asignación

Intenta agregar una entrada de herramienta adicional a tu archivo **server.py** (por ejemplo: devolver la raíz cuadrada de un número). Envía mensajes adicionales que requieran que el agente utilice tu nueva herramienta (o herramientas existentes). Asegúrate de reiniciar el servidor para cargar las herramientas añadidas.

## Solución

[Solución](./solution/README.md)

## Puntos Clave

Los puntos clave de este capítulo son los siguientes:

- La extensión AI Toolkit es un gran cliente que permite consumir servidores MCP y sus herramientas.
- Puedes agregar nuevas herramientas a los servidores MCP, ampliando las capacidades del agente para satisfacer los requisitos en evolución.
- AI Toolkit incluye plantillas (por ejemplo, plantillas de servidor MCP en Python) para simplificar la creación de herramientas personalizadas.

## Recursos Adicionales

- [Documentación de AI Toolkit](https://aka.ms/AIToolkit/doc)

## Qué sigue
- Siguiente: [Pruebas y Depuración](../08-testing/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Descargo de responsabilidad**:
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional humana. No somos responsables de cualquier malentendido o interpretación errónea que surja del uso de esta traducción.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->