# Generador de Plan de Estudio con Chainlit y Microsoft Learn Docs MCP

## Requisitos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)
- Acceso a internet para conectarse al servidor de Microsoft Learn Docs MCP

## Instalación

1. Clona este repositorio o descarga los archivos del proyecto.
2. Instala las dependencias necesarias:

   ```bash
   pip install -r requirements.txt
   ```

## Uso

### Escenario 1: Consulta Simple a Docs MCP
Un cliente de línea de comandos que se conecta al servidor Docs MCP, envía una consulta y muestra el resultado.

1. Ejecuta el script:
   ```bash
   python scenario1.py
   ```
2. Ingresa tu pregunta sobre la documentación en el indicador.

### Escenario 2: Generador de Plan de Estudio (Aplicación Web con Chainlit)
Una interfaz web (usando Chainlit) que permite a los usuarios generar un plan de estudio personalizado, semana por semana, para cualquier tema técnico.

1. Inicia la aplicación Chainlit:
   ```bash
   chainlit run scenario2.py
   ```
2. Abre la URL local proporcionada en tu terminal (por ejemplo, http://localhost:8000) en tu navegador.
3. En la ventana de chat, ingresa tu tema de estudio y el número de semanas que deseas estudiar (por ejemplo, "Certificación AI-900, 8 semanas").
4. La aplicación responderá con un plan de estudio semana por semana, incluyendo enlaces a la documentación relevante de Microsoft Learn.

**Variables de Entorno Requeridas:**

Para usar el Escenario 2 (la aplicación web Chainlit con Azure OpenAI), debes configurar las siguientes variables de entorno en un archivo `.env` dentro del directorio `python`:

```
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=
AZURE_OPENAI_API_KEY=
AZURE_OPENAI_ENDPOINT=
AZURE_OPENAI_API_VERSION=
```

Completa estos valores con los detalles de tu recurso de Azure OpenAI antes de ejecutar la aplicación.

> [!TIP]
> Puedes desplegar fácilmente tus propios modelos usando [Azure AI Foundry](https://ai.azure.com/).

### Escenario 3: Documentación en el Editor con el Servidor MCP en VS Code

En lugar de cambiar entre pestañas del navegador para buscar documentación, puedes traer Microsoft Learn Docs directamente a tu VS Code usando el servidor MCP. Esto te permite:
- Buscar y leer documentación dentro de VS Code sin salir de tu entorno de codificación.
- Referenciar documentación e insertar enlaces directamente en tu README o archivos de curso.
- Usar GitHub Copilot y MCP juntos para un flujo de trabajo de documentación impulsado por IA.

**Ejemplos de Casos de Uso:**
- Agregar rápidamente enlaces de referencia a un README mientras escribes documentación de un curso o proyecto.
- Usar Copilot para generar código y MCP para encontrar y citar documentación relevante al instante.
- Mantenerte enfocado en tu editor y aumentar la productividad.

> [!IMPORTANT]
> Asegúrate de tener una configuración válida [`mcp.json`](../../../../../../09-CaseStudy/docs-mcp/solution/scenario3/mcp.json) en tu espacio de trabajo (ubicación: `.vscode/mcp.json`).

## ¿Por qué usar Chainlit para el Escenario 2?

Chainlit es un marco moderno de código abierto para construir aplicaciones web conversacionales. Facilita la creación de interfaces de usuario basadas en chat que se conectan a servicios de backend como el servidor Microsoft Learn Docs MCP. Este proyecto utiliza Chainlit para proporcionar una forma simple e interactiva de generar planes de estudio personalizados en tiempo real. Al aprovechar Chainlit, puedes construir y desplegar rápidamente herramientas basadas en chat que mejoran la productividad y el aprendizaje.

## Qué Hace Esta Aplicación

Esta aplicación permite a los usuarios crear un plan de estudio personalizado simplemente ingresando un tema y una duración. La aplicación analiza tu entrada, consulta el servidor Microsoft Learn Docs MCP para obtener contenido relevante y organiza los resultados en un plan estructurado semana por semana. Las recomendaciones de cada semana se muestran en el chat, lo que facilita seguir y rastrear tu progreso. La integración asegura que siempre obtengas los recursos de aprendizaje más recientes y relevantes.

## Consultas de Ejemplo

Prueba estas consultas en la ventana de chat para ver cómo responde la aplicación:

- `Certificación AI-900, 8 semanas`
- `Aprender Azure Functions, 4 semanas`
- `Azure DevOps, 6 semanas`
- `Ingeniería de datos en Azure, 10 semanas`
- `Fundamentos de seguridad de Microsoft, 5 semanas`
- `Power Platform, 7 semanas`
- `Servicios de Azure AI, 12 semanas`
- `Arquitectura en la nube, 9 semanas`

Estos ejemplos demuestran la flexibilidad de la aplicación para diferentes objetivos de aprendizaje y plazos.

## Referencias

- [Documentación de Chainlit](https://docs.chainlit.io/)
- [Documentación de MCP](https://github.com/MicrosoftDocs/mcp)

---

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Si bien nos esforzamos por lograr precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o imprecisiones. El documento original en su idioma nativo debe considerarse como la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o interpretaciones erróneas que puedan surgir del uso de esta traducción.