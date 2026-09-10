> [!WARNING]
> El muestreo está desaprobado en MCP `2026-07-28`. Esta lección se mantiene para
> implementaciones heredadas. Los nuevos servidores deben integrarse directamente con una API
> de proveedor de LLM.

# Muestreo en el Protocolo de Contexto de Modelo

> El muestreo permanece en la especificación `2026-07-28` por compatibilidad y es
> elegible para su eliminación en la primera revisión publicada en o después del 28 de julio de
> 2027. Los ejemplos en esta lección pueden usar APIs del SDK que implementan `2025-11-25`.
> Vea [Qué ha cambiado en MCP: La especificación 2026-07-28](../../01-CoreConcepts/mcp-2026-07-28.md).

En implementaciones heredadas de MCP, el muestreo permite a los servidores solicitar completaciones de LLM
a través del cliente. Esta lección explica ese flujo de protocolo desaprobado
para compatibilidad y trabajos de migración.

## Introducción

En esta lección, exploraremos cómo configurar parámetros de muestreo en solicitudes MCP y comprender la mecánica subyacente del protocolo de muestreo.

## Objetivos de Aprendizaje

Al final de esta lección, serás capaz de:

- Entender los parámetros clave de muestreo disponibles en MCP.
- Configurar parámetros de muestreo para diferentes casos de uso.
- Implementar muestreo determinista para resultados reproducibles.
- Ajustar dinámicamente parámetros de muestreo según el contexto y preferencias del usuario.
- Aplicar estrategias de muestreo para mejorar el rendimiento del modelo en varios escenarios.
- Entender cómo funciona el muestreo en el flujo cliente-servidor de MCP.

## Cómo Funciona el Muestreo en MCP

El flujo de muestreo en MCP sigue estos pasos:

1. El servidor envía una solicitud `sampling/createMessage` al cliente
2. El cliente revisa la solicitud y puede modificarla
3. El cliente muestrea desde un LLM
4. El cliente revisa la completación
5. El cliente devuelve el resultado al servidor

Este diseño con intervención humana garantiza que los usuarios mantengan control sobre lo que el LLM ve y genera.

## Resumen de Parámetros de Muestreo

MCP define los siguientes parámetros de muestreo que pueden configurarse en solicitudes cliente:

| Parámetro | Descripción | Rango Típico |
|-----------|-------------|--------------|
| `temperature` | Controla la aleatoriedad en la selección de tokens | 0.0 - 1.0 |
| `maxTokens` | Número máximo de tokens a generar | Valor entero |
| `stopSequences` | Secuencias personalizadas que detienen la generación al ser encontradas | Arreglo de cadenas |
| `metadata` | Parámetros adicionales específicos del proveedor | Objeto JSON |

Muchos proveedores de LLM soportan parámetros adicionales a través del campo `metadata`, que pueden incluir:

| Parámetro de Extensión Común | Descripción | Rango Típico |
|-----------|-------------|--------------|
| `top_p` | Muestreo de núcleo - limita tokens a la probabilidad acumulada superior | 0.0 - 1.0 |
| `top_k` | Limita la selección de tokens a las mejores K opciones | 1 - 100 |
| `presence_penalty` | Penaliza tokens según su presencia en el texto hasta ahora | -2.0 - 2.0 |
| `frequency_penalty` | Penaliza tokens según su frecuencia en el texto hasta ahora | -2.0 - 2.0 |
| `seed` | Semilla aleatoria específica para resultados reproducibles | Valor entero |

## Formato de Solicitud de Ejemplo

Aquí hay un ejemplo de solicitar muestreo desde un cliente en MCP:

```json
{
  "method": "sampling/createMessage",
  "params": {
    "messages": [
      {
        "role": "user",
        "content": {
          "type": "text",
          "text": "What files are in the current directory?"
        }
      }
    ],
    "systemPrompt": "You are a helpful file system assistant.",
    "includeContext": "thisServer",
    "maxTokens": 100,
    "temperature": 0.7
  }
}
```

## Formato de Respuesta

El cliente devuelve un resultado de completación:

```json
{
  "model": "string",  // Name of the model used
  "stopReason": "endTurn" | "stopSequence" | "maxTokens" | "string",
  "role": "assistant",
  "content": {
    "type": "text",
    "text": "string"
  }
}
```

## Controles Humanos en el Bucle

El muestreo en MCP está diseñado con supervisión humana en mente:

- **Para indicaciones**:
  - Los clientes deben mostrar a los usuarios la indicación propuesta
  - Los usuarios deben poder modificar o rechazar las indicaciones
  - Las indicaciones del sistema pueden ser filtradas o modificadas
  - La inclusión del contexto es controlada por el cliente

- **Para completaciones**:
  - Los clientes deben mostrar a los usuarios la completación
  - Los usuarios deben poder modificar o rechazar completaciones
  - Los clientes pueden filtrar o modificar completaciones
  - Los usuarios controlan qué modelo se usa

Con estos principios en mente, veamos cómo implementar muestreo en diferentes lenguajes de programación, enfocándonos en los parámetros que comúnmente apoyan los proveedores de LLM.

## Consideraciones de Seguridad

Al implementar muestreo en MCP, considere estas mejores prácticas de seguridad:

- **Validar todo el contenido del mensaje** antes de enviarlo al cliente
- **Sanitizar información sensible** de indicaciones y completaciones
- **Implementar límites de tasa** para prevenir abusos
- **Monitorear el uso de muestreo** para detectar patrones inusuales
- **Encriptar datos en tránsito** usando protocolos seguros
- **Manejar la privacidad de datos del usuario** conforme a regulaciones relevantes
- **Auditar solicitudes de muestreo** para cumplimiento y seguridad
- **Controlar exposición de costos** con límites apropiados
- **Implementar tiempos de espera** para solicitudes de muestreo
- **Manejar errores del modelo con gracia** y con soluciones adecuadas

Los parámetros de muestreo permiten ajustar finamente el comportamiento de los modelos de lenguaje para lograr el equilibrio deseado entre salidas deterministas y creativas.

Veamos cómo configurar estos parámetros en diferentes lenguajes de programación.

# [.NET](#tab-dotnet)

```csharp
// .NET Example: Configuring sampling parameters in MCP
public class SamplingExample
{
    public async Task RunWithSamplingAsync()
    {
        // Create MCP client with sampling configuration
        var client = new McpClient("https://mcp-server-url.com");
        
        // Create request with specific sampling parameters
        var request = new McpRequest
        {
            Prompt = "Generate creative ideas for a mobile app",
            SamplingParameters = new SamplingParameters
            {
                Temperature = 0.8f,     // Higher temperature for more creative outputs
                TopP = 0.95f,           // Nucleus sampling parameter
                TopK = 40,              // Limit token selection to top K options
                FrequencyPenalty = 0.5f, // Reduce repetition
                PresencePenalty = 0.2f   // Encourage diversity
            },
            AllowedTools = new[] { "ideaGenerator", "marketAnalyzer" }
        };
        
        // Send request using specific sampling configuration
        var response = await client.SendRequestAsync(request);
        
        // Output results
        Console.WriteLine($"Generated with Temperature={request.SamplingParameters.Temperature}:");
        Console.WriteLine(response.GeneratedText);
    }
}
```

En el código anterior hemos:

- Creado un cliente MCP con una URL de servidor específica.
- Configurado una solicitud con parámetros de muestreo como `temperature`, `top_p` y `top_k`.
- Enviado la solicitud e impreso el texto generado.
- Usado:
    - `allowedTools` para especificar qué herramientas puede usar el modelo durante la generación. En este caso, permitimos que las herramientas `ideaGenerator` y `marketAnalyzer` ayuden a generar ideas creativas para apps.
    - `frequencyPenalty` y `presencePenalty` para controlar la repetición y diversidad en la salida.
    - `temperature` para controlar la aleatoriedad de la salida, donde valores más altos generan respuestas más creativas.
    - `top_p` para limitar la selección de tokens a aquellos que contribuyen a la masa de probabilidad acumulada superior, mejorando la calidad del texto generado.
    - `top_k` para restringir el modelo a los mejores K tokens más probables, lo que puede ayudar a generar respuestas más coherentes.
    - `frequencyPenalty` y `presencePenalty` para reducir la repetición y fomentar diversidad en el texto generado.

# [JavaScript](#tab/javascript)

```javascript
// Ejemplo de JavaScript: configuración de temperatura y muestreo Top-P
const { McpClient } = require('@mcp/client');

async function demonstrateSampling() {
  // Inicializar el cliente MCP
  const client = new McpClient({
    serverUrl: 'https://mcp-server-example.com',
    apiKey: process.env.MCP_API_KEY
  });
  
  // Configurar la solicitud con diferentes parámetros de muestreo
  const creativeSampling = {
    temperature: 0.9,    // Mayor temperatura = más aleatoriedad/creatividad
    topP: 0.92,          // Considerar tokens con masa de probabilidad del 92% superior
    frequencyPenalty: 0.6, // Reducir la repetición de secuencias de tokens
    presencePenalty: 0.4   // Penalizar tokens que han aparecido en el texto hasta ahora
  };
  
  const factualSampling = {
    temperature: 0.2,    // Temperatura baja = más determinista/factual
    topP: 0.85,          // Selección de tokens ligeramente más enfocada
    frequencyPenalty: 0.2, // Penalización mínima por repetición
    presencePenalty: 0.1   // Penalización mínima por presencia
  };
  
  try {
    // Enviar dos solicitudes con diferentes configuraciones de muestreo
    const creativeResponse = await client.sendPrompt(
      "Generate innovative ideas for sustainable urban transportation",
      {
        allowedTools: ['ideaGenerator', 'environmentalImpactTool'],
        ...creativeSampling
      }
    );
    
    const factualResponse = await client.sendPrompt(
      "Explain how electric vehicles impact carbon emissions",
      {
        allowedTools: ['factChecker', 'dataAnalysisTool'],
        ...factualSampling
      }
    );
    
    console.log('Creative Response (temperature=0.9):');
    console.log(creativeResponse.generatedText);
    
    console.log('\nFactual Response (temperature=0.2):');
    console.log(factualResponse.generatedText);
    
  } catch (error) {
    console.error('Error demonstrating sampling:', error);
  }
}

demonstrateSampling();
```

En el código anterior hemos:

- Inicializado un cliente MCP con una URL de servidor y clave API.
- Configurado dos conjuntos de parámetros de muestreo: uno para tareas creativas y otro para tareas factual.
- Enviado solicitudes con estas configuraciones, permitiendo que el modelo use herramientas específicas para cada tarea.
- Impreso las respuestas generadas para demostrar los efectos de distintos parámetros de muestreo.
- Usado `allowedTools` para especificar qué herramientas puede usar el modelo durante la generación. En este caso, permitimos `ideaGenerator` y `environmentalImpactTool` para tareas creativas, y `factChecker` y `dataAnalysisTool` para tareas factuales.
- Usado `temperature` para controlar la aleatoriedad de la salida, donde valores más altos generan respuestas más creativas.

- Usado `top_p` para limitar la selección de tokens a aquellos que contribuyen a la masa de probabilidad acumulada superior, mejorando la calidad del texto generado.
- Usado `frequencyPenalty` y `presencePenalty` para reducir la repetición y fomentar la diversidad en la salida.
- Usado `top_k` para restringir el modelo a los K tokens más probables, lo que puede ayudar a generar respuestas más coherentes.

---

## Muestreo Determinista

Para aplicaciones que requieren salidas consistentes, el muestreo determinista asegura resultados reproducibles. Cómo lo hace es usando una semilla aleatoria fija y configurando la temperatura a cero.

Vamos a ver la siguiente implementación de ejemplo para demostrar el muestreo determinista en diferentes lenguajes de programación.

# [Java](#tab/java)

```java
// Ejemplo en Java: Respuestas deterministas con semilla fija
public class DeterministicSamplingExample {
    public void demonstrateDeterministicResponses() {
        McpClient client = new McpClient.Builder()
            .setServerUrl("https://mcp-server-example.com")
            .build();
            
        long fixedSeed = 12345; // Usando una semilla fija para resultados deterministas
        
        // Primera solicitud con semilla fija
        McpRequest request1 = new McpRequest.Builder()
            .setPrompt("Generate a random number between 1 and 100")
            .setSeed(fixedSeed)
            .setTemperature(0.0) // Temperatura cero para máximo determinismo
            .build();
            
        // Segunda solicitud con la misma semilla
        McpRequest request2 = new McpRequest.Builder()
            .setPrompt("Generate a random number between 1 and 100")
            .setSeed(fixedSeed)
            .setTemperature(0.0)
            .build();
        
        // Ejecutar ambas solicitudes
        McpResponse response1 = client.sendRequest(request1);
        McpResponse response2 = client.sendRequest(request2);
        
        // Las respuestas deberían ser idénticas debido a la misma semilla y temperatura=0
        System.out.println("Response 1: " + response1.getGeneratedText());
        System.out.println("Response 2: " + response2.getGeneratedText());
        System.out.println("Are responses identical: " + 
            response1.getGeneratedText().equals(response2.getGeneratedText()));
    }
}
```

En el código precedente hemos:

- Creado un cliente MCP con una URL de servidor especificada.
- Configurado dos solicitudes con el mismo prompt, semilla fija y temperatura cero.
- Enviado ambas solicitudes e impreso el texto generado.
- Demostrado que las respuestas son idénticas debido a la naturaleza determinista de la configuración de muestreo (misma semilla y temperatura).
- Usado `setSeed` para especificar una semilla aleatoria fija, asegurando que el modelo genere la misma salida para la misma entrada cada vez.
- Configurado `temperature` a cero para asegurar máximo determinismo, es decir, el modelo siempre seleccionará el token siguiente más probable sin aleatoriedad.

# [JavaScript](#tab/javascript-deterministic)

```javascript
// Ejemplo de JavaScript: respuestas deterministas con control de semilla
const { McpClient } = require('@mcp/client');

async function deterministicSampling() {
  const client = new McpClient({
    serverUrl: 'https://mcp-server-example.com'
  });
  
  const fixedSeed = 12345;
  const prompt = "Generate a random password with 8 characters";
  
  try {
    // Primera solicitud con semilla fija
    const response1 = await client.sendPrompt(prompt, {
      seed: fixedSeed,
      temperature: 0.0  // Temperatura cero para máximo determinismo
    });
    
    // Segunda solicitud con la misma semilla y temperatura
    const response2 = await client.sendPrompt(prompt, {
      seed: fixedSeed,
      temperature: 0.0
    });
    
    // Tercera solicitud con diferente semilla pero misma temperatura
    const response3 = await client.sendPrompt(prompt, {
      seed: 67890,
      temperature: 0.0
    });
    
    console.log('Response 1:', response1.generatedText);
    console.log('Response 2:', response2.generatedText);
    console.log('Response 3:', response3.generatedText);
    console.log('Responses 1 and 2 match:', response1.generatedText === response2.generatedText);
    console.log('Responses 1 and 3 match:', response1.generatedText === response3.generatedText);
    
  } catch (error) {
    console.error('Error in deterministic sampling demo:', error);
  }
}

deterministicSampling();
```

En el código precedente hemos:

- Inicializado un cliente MCP con una URL de servidor.
- Configurado dos solicitudes con el mismo prompt, semilla fija y temperatura cero.
- Enviado ambas solicitudes e impreso el texto generado.
- Demostrado que las respuestas son idénticas debido a la naturaleza determinista de la configuración de muestreo (misma semilla y temperatura).
- Usado `seed` para especificar una semilla aleatoria fija, asegurando que el modelo genere la misma salida para la misma entrada cada vez.
- Configurado `temperature` a cero para asegurar máximo determinismo, es decir, el modelo siempre seleccionará el token siguiente más probable sin aleatoriedad.
- Usado una semilla diferente para la tercera solicitud para mostrar que cambiar la semilla resulta en salidas diferentes, incluso con el mismo prompt y temperatura.

---

## Configuración Dinámica de Muestreo

El muestreo inteligente adapta los parámetros según el contexto y los requisitos de cada solicitud. Eso significa ajustar dinámicamente parámetros como temperatura, top_p y penalizaciones basadas en el tipo de tarea, preferencias del usuario o desempeño histórico.

Vamos a ver cómo implementar el muestreo dinámico en diferentes lenguajes de programación.

# [Python](#tab/python)

```python
# Ejemplo en Python: muestreo dinámico basado en el contexto de la solicitud
class DynamicSamplingService:
    def __init__(self, mcp_client):
        self.client = mcp_client
        
    async def generate_with_adaptive_sampling(self, prompt, task_type, user_preferences=None):
        """Uses different sampling strategies based on task type and user preferences"""
        
        # Definir configuraciones de muestreo para diferentes tipos de tareas
        sampling_presets = {
            "creative": {"temperature": 0.9, "top_p": 0.95, "frequency_penalty": 0.7},
            "factual": {"temperature": 0.2, "top_p": 0.85, "frequency_penalty": 0.2},
            "code": {"temperature": 0.3, "top_p": 0.9, "frequency_penalty": 0.5},
            "analytical": {"temperature": 0.4, "top_p": 0.92, "frequency_penalty": 0.3}
        }
        
        # Seleccionar configuración base
        sampling_params = sampling_presets.get(task_type, sampling_presets["factual"])
        
        # Ajustar según preferencias del usuario si se proporcionan
        if user_preferences:
            if "creativity_level" in user_preferences:
                # Escalar la temperatura basándose en la preferencia de creatividad (1-10)
                creativity = min(max(user_preferences["creativity_level"], 1), 10) / 10
                sampling_params["temperature"] = 0.1 + (0.9 * creativity)
            
            if "diversity" in user_preferences:
                # Ajustar top_p según la diversidad de respuestas deseada
                diversity = min(max(user_preferences["diversity"], 1), 10) / 10
                sampling_params["top_p"] = 0.6 + (0.39 * diversity)
        
        # Crear y enviar solicitud con parámetros personalizados de muestreo
        response = await self.client.send_request(
            prompt=prompt,
            temperature=sampling_params["temperature"],
            top_p=sampling_params["top_p"],
            frequency_penalty=sampling_params["frequency_penalty"]
        )
        
        # Devolver respuesta con metadatos de muestreo para transparencia
        return {
            "text": response.generated_text,
            "applied_sampling": sampling_params,
            "task_type": task_type
        }
```

En el código precedente hemos:

- Creado una clase `DynamicSamplingService` que gestiona el muestreo adaptativo.
- Definido presets de muestreo para diferentes tipos de tareas (creativa, factual, código, analítica).
- Seleccionado un preset base de muestreo basado en el tipo de tarea.
- Ajustado los parámetros de muestreo según las preferencias del usuario, como nivel de creatividad y diversidad.
- Enviado la solicitud con los parámetros de muestreo configurados dinámicamente.
- Retornado el texto generado junto con los parámetros de muestreo aplicados y el tipo de tarea para transparencia.
- Usado `temperature` para controlar la aleatoriedad de la salida, donde valores más altos conducen a respuestas más creativas.
- Usado `top_p` para limitar la selección de tokens a aquellos que contribuyen a la masa de probabilidad acumulada superior, mejorando la calidad del texto generado.
- Usado `frequency_penalty` para reducir la repetición y fomentar la diversidad en la salida.
- Usado `user_preferences` para permitir la personalización de parámetros de muestreo basados en niveles de creatividad y diversidad definidos por el usuario.
- Usado `task_type` para determinar la estrategia de muestreo adecuada para la solicitud, permitiendo respuestas más ajustadas según la naturaleza de la tarea.
- Usado método `send_request` para enviar el prompt con los parámetros de muestreo configurados, asegurando que el modelo genere texto según los requisitos especificados.
- Usado `generated_text` para recuperar la respuesta del modelo, que es devuelta junto con los parámetros de muestreo y el tipo de tarea para análisis o presentación posterior.
- Usado funciones `min` y `max` para asegurar que las preferencias del usuario se mantengan dentro de rangos válidos, evitando configuraciones de muestreo inválidas.

# [JavaScript Dinámico](#tab/javascript-dynamic)

```javascript
// Ejemplo de JavaScript: configuración dinámica de muestreo basada en el contexto del usuario
class AdaptiveSamplingManager {
  constructor(mcpClient) {
    this.client = mcpClient;
    
    // Definir perfiles de muestreo base
    this.samplingProfiles = {
      creative: { temperature: 0.85, topP: 0.94, frequencyPenalty: 0.7, presencePenalty: 0.5 },
      factual: { temperature: 0.2, topP: 0.85, frequencyPenalty: 0.3, presencePenalty: 0.1 },
      code: { temperature: 0.25, topP: 0.9, frequencyPenalty: 0.4, presencePenalty: 0.3 },
      conversational: { temperature: 0.7, topP: 0.9, frequencyPenalty: 0.6, presencePenalty: 0.4 }
    };
    
    // Registrar el rendimiento histórico
    this.performanceHistory = [];
  }
  
  // Detectar tipo de tarea a partir del prompt
  detectTaskType(prompt, context = {}) {
    const promptLower = prompt.toLowerCase();
    
    // Detección heurística simple - podría mejorarse con clasificación ML
    if (context.taskType) return context.taskType;
    
    if (promptLower.includes('code') || 
        promptLower.includes('function') || 
        promptLower.includes('program')) {
      return 'code';
    }
    
    if (promptLower.includes('explain') || 
        promptLower.includes('what is') || 
        promptLower.includes('how does')) {
      return 'factual';
    }
    
    if (promptLower.includes('creative') || 
        promptLower.includes('imagine') || 
        promptLower.includes('story')) {
      return 'creative';
    }
    
    // Predeterminar a conversacional si no se detecta un tipo claro
    return 'conversational';
  }
  
  // Calcular parámetros de muestreo según el contexto y preferencias del usuario
  getSamplingParameters(prompt, context = {}) {
    // Detectar el tipo de tarea
    const taskType = this.detectTaskType(prompt, context);
    
    // Obtener perfil base
    let params = {...this.samplingProfiles[taskType]};
    
    // Ajustar según las preferencias del usuario
    if (context.userPreferences) {
      const { creativity, precision, consistency } = context.userPreferences;
      
      if (creativity !== undefined) {
        // Escalar de 1 a 10 al rango adecuado de temperatura
        params.temperature = 0.1 + (creativity * 0.09); // 0.1-1.0
      }
      
      if (precision !== undefined) {
        // Mayor precisión significa topP más bajo (selección más enfocada)
        params.topP = 1.0 - (precision * 0.05); // 0.5-1.0
      }
      
      if (consistency !== undefined) {
        // Mayor consistencia significa menores penalizaciones
        params.frequencyPenalty = 0.1 + ((10 - consistency) * 0.08); // 0.1-0.9
      }
    }
    
    // Aplicar ajustes aprendidos del historial de rendimiento
    this.applyLearnedAdjustments(params, taskType);
    
    return params;
  }
  
  applyLearnedAdjustments(params, taskType) {
    // Lógica adaptativa simple - podría mejorarse con algoritmos más sofisticados
    const relevantHistory = this.performanceHistory
      .filter(entry => entry.taskType === taskType)
      .slice(-5); // Considerar solo el historial reciente
    
    if (relevantHistory.length > 0) {
      // Calcular puntajes promedios de rendimiento
      const avgScore = relevantHistory.reduce((sum, entry) => sum + entry.score, 0) / relevantHistory.length;
      
      // Si el rendimiento está por debajo del umbral, ajustar parámetros
      if (avgScore < 0.7) {
        // Ajuste ligero hacia valores más seguros
        params.temperature = Math.max(params.temperature * 0.9, 0.1);
        params.topP = Math.max(params.topP * 0.95, 0.5);
      }
    }
  }
  
  recordPerformance(prompt, samplingParams, response, score) {
    // Registrar rendimiento para ajustes futuros
    this.performanceHistory.push({
      timestamp: Date.now(),
      taskType: this.detectTaskType(prompt),
      samplingParams,
      responseLength: response.generatedText.length,
      score // Calificación de 0 a 1 de la calidad de la respuesta
    });
    
    // Limitar tamaño del historial
    if (this.performanceHistory.length > 100) {
      this.performanceHistory.shift();
    }
  }
  
  async generateResponse(prompt, context = {}) {
    // Obtener parámetros de muestreo optimizados
    const samplingParams = this.getSamplingParameters(prompt, context);
    
    // Enviar solicitud con parámetros optimizados
    const response = await this.client.sendPrompt(prompt, {
      ...samplingParams,
      allowedTools: context.allowedTools || []
    });
    
    // Si el usuario proporciona retroalimentación, registrarla para futura optimización
    if (context.recordPerformance) {
      this.recordPerformance(prompt, samplingParams, response, context.feedbackScore || 0.5);
    }
    
    return {
      response,
      appliedSamplingParams: samplingParams,
      detectedTaskType: this.detectTaskType(prompt, context)
    };
  }
}

// Ejemplo de uso
async function demonstrateAdaptiveSampling() {
  const client = new McpClient({
    serverUrl: 'https://mcp-server-example.com'
  });
  
  const samplingManager = new AdaptiveSamplingManager(client);
  
  try {
    // Tarea creativa con preferencias personalizadas del usuario
    const creativeResult = await samplingManager.generateResponse(
      "Write a short poem about artificial intelligence",
      {
        userPreferences: {
          creativity: 9,  // Alta creatividad (1-10)
          consistency: 3  // Baja consistencia (1-10)
        }
      }
    );
    
    console.log('Creative Task:');
    console.log(`Detected type: ${creativeResult.detectedTaskType}`);
    console.log('Applied sampling:', creativeResult.appliedSamplingParams);
    console.log(creativeResult.response.generatedText);
    
    // Tarea de generación de código
    const codeResult = await samplingManager.generateResponse(
      "Write a JavaScript function to calculate the Fibonacci sequence",
      {
        userPreferences: {
          creativity: 2,  // Baja creatividad
          precision: 8,   // Alta precisión
          consistency: 9  // Alta consistencia
        }
      }
    );
    
    console.log('\nCode Task:');
    console.log(`Detected type: ${codeResult.detectedTaskType}`);
    console.log('Applied sampling:', codeResult.appliedSamplingParams);
    console.log(codeResult.response.generatedText);
    
  } catch (error) {
    console.error('Error in adaptive sampling demo:', error);
  }
}

demonstrateAdaptiveSampling();
```

En el código precedente hemos:

- Creado una clase `AdaptiveSamplingManager` que gestiona el muestreo dinámico basado en el tipo de tarea y preferencias del usuario.
- Definido perfiles de muestreo para diferentes tipos de tareas (creativa, factual, código, conversacional).
- Implementado un método para detectar el tipo de tarea desde el prompt usando heurísticas simples.
- Calculado parámetros de muestreo basados en el tipo de tarea detectado y preferencias del usuario.
- Aplicado ajustes aprendidos basados en el desempeño histórico para optimizar los parámetros de muestreo.
- Registrado el desempeño para ajustes futuros, permitiendo que el sistema aprenda de interacciones pasadas.
- Enviado solicitudes con parámetros de muestreo configurados dinámicamente y retornado el texto generado junto con los parámetros aplicados y tipo de tarea detectado.
- Usado:
    - `userPreferences` para permitir la personalización de los parámetros de muestreo basados en niveles definidos por el usuario de creatividad, precisión y consistencia.
    - `detectTaskType` para determinar la naturaleza de la tarea basada en el prompt, permitiendo respuestas más ajustadas.
    - `recordPerformance` para registrar el desempeño de las respuestas generadas, habilitando que el sistema se adapte y mejore con el tiempo.
    - `applyLearnedAdjustments` para modificar parámetros de muestreo basados en desempeño histórico, mejorando la capacidad del modelo para generar respuestas de alta calidad.
    - `generateResponse` para encapsular todo el proceso de generación de una respuesta con muestreo adaptativo, facilitando su uso con diferentes prompts y contextos.
    - `allowedTools` para especificar qué herramientas puede usar el modelo durante la generación, permitiendo respuestas más conscientes del contexto.
    - `feedbackScore` para permitir a los usuarios proporcionar retroalimentación sobre la calidad de la respuesta generada, que puede usarse para refinar aún más el desempeño del modelo con el tiempo.
    - `performanceHistory` para mantener un registro de interacciones pasadas, permitiendo que el sistema aprenda de éxitos y fracasos anteriores.
    - `getSamplingParameters` para ajustar dinámicamente los parámetros de muestreo según el contexto de la solicitud, permitiendo un comportamiento del modelo más flexible y receptivo.
    - `detectTaskType` para clasificar la tarea según el prompt, habilitando que el sistema aplique estrategias de muestreo apropiadas para diferentes tipos de solicitudes.
    - `samplingProfiles` para definir configuraciones base de muestreo para diferentes tipos de tareas, permitiendo ajustes rápidos basados en la naturaleza de la solicitud.

---

## Qué sigue

- [5.7 Escalado](../mcp-scaling/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Descargo de responsabilidad**:
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional humana. No somos responsables de cualquier malentendido o interpretación errónea que surja del uso de esta traducción.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->