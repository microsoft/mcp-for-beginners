# Muestreo en el Protocolo de Contexto de Modelo (MCP)

El muestreo es una función poderosa de MCP que permite a los servidores solicitar completaciones de LLM a través del cliente, habilitando comportamientos agenticos sofisticados mientras se mantiene la seguridad y privacidad. La configuración adecuada del muestreo puede mejorar drásticamente la calidad y el rendimiento de las respuestas. MCP ofrece una forma estandarizada de controlar cómo los modelos generan texto con parámetros específicos que influyen en la aleatoriedad, creatividad y coherencia.

## Introducción

En esta lección, exploraremos cómo configurar los parámetros de muestreo en las solicitudes MCP y entender la mecánica subyacente del protocolo de muestreo.

## Objetivos de Aprendizaje

Al finalizar esta lección, podrás:

- Comprender los parámetros clave de muestreo disponibles en MCP.
- Configurar parámetros de muestreo para diferentes casos de uso.
- Implementar muestreo determinista para resultados reproducibles.
- Ajustar dinámicamente los parámetros de muestreo según el contexto y las preferencias del usuario.
- Aplicar estrategias de muestreo para mejorar el rendimiento del modelo en diversos escenarios.
- Entender cómo funciona el muestreo en el flujo cliente-servidor de MCP.

## Cómo Funciona el Muestreo en MCP

El flujo de muestreo en MCP sigue estos pasos:

1. El servidor envía una solicitud `sampling/createMessage` al cliente.
2. El cliente revisa la solicitud y puede modificarla.
3. El cliente realiza el muestreo desde un LLM.
4. El cliente revisa la completación.
5. El cliente devuelve el resultado al servidor.

Este diseño con intervención humana garantiza que los usuarios mantengan el control sobre lo que el LLM ve y genera.

## Resumen de Parámetros de Muestreo

MCP define los siguientes parámetros de muestreo que pueden configurarse en las solicitudes del cliente:

| Parámetro | Descripción | Rango Típico |
|-----------|-------------|--------------|
| `temperature` | Controla la aleatoriedad en la selección de tokens | 0.0 - 1.0 |
| `maxTokens` | Número máximo de tokens a generar | Valor entero |
| `stopSequences` | Secuencias personalizadas que detienen la generación al encontrarse | Array de cadenas |
| `metadata` | Parámetros adicionales específicos del proveedor | Objeto JSON |

Muchos proveedores de LLM soportan parámetros adicionales a través del campo `metadata`, que pueden incluir:

| Parámetro Común de Extensión | Descripción | Rango Típico |
|------------------------------|-------------|--------------|
| `top_p` | Muestreo núcleo - limita tokens a la probabilidad acumulada superior | 0.0 - 1.0 |
| `top_k` | Limita la selección de tokens a las K opciones principales | 1 - 100 |
| `presence_penalty` | Penaliza tokens según su presencia en el texto hasta ahora | -2.0 - 2.0 |
| `frequency_penalty` | Penaliza tokens según su frecuencia en el texto hasta ahora | -2.0 - 2.0 |
| `seed` | Semilla aleatoria específica para resultados reproducibles | Valor entero |

## Formato de Solicitud de Ejemplo

Aquí hay un ejemplo de cómo solicitar muestreo desde un cliente en MCP:

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

## Controles con Intervención Humana

El muestreo en MCP está diseñado con supervisión humana en mente:

- **Para prompts**:
  - Los clientes deben mostrar a los usuarios el prompt propuesto.
  - Los usuarios deben poder modificar o rechazar los prompts.
  - Los prompts del sistema pueden ser filtrados o modificados.
  - La inclusión del contexto es controlada por el cliente.

- **Para completaciones**:
  - Los clientes deben mostrar a los usuarios la completación.
  - Los usuarios deben poder modificar o rechazar las completaciones.
  - Los clientes pueden filtrar o modificar las completaciones.
  - Los usuarios controlan qué modelo se utiliza.

Con estos principios en mente, veamos cómo implementar el muestreo en diferentes lenguajes de programación, enfocándonos en los parámetros comúnmente soportados por los proveedores de LLM.

## Consideraciones de Seguridad

Al implementar muestreo en MCP, considera estas mejores prácticas de seguridad:

- **Validar todo el contenido del mensaje** antes de enviarlo al cliente.
- **Sanitizar información sensible** de prompts y completaciones.
- **Implementar límites de tasa** para prevenir abusos.
- **Monitorear el uso del muestreo** para detectar patrones inusuales.
- **Encriptar datos en tránsito** usando protocolos seguros.
- **Manejar la privacidad de datos de usuarios** conforme a regulaciones aplicables.
- **Auditar solicitudes de muestreo** para cumplimiento y seguridad.
- **Controlar la exposición de costos** con límites apropiados.
- **Implementar tiempos de espera** para solicitudes de muestreo.
- **Manejar errores del modelo con gracia** usando mecanismos de respaldo adecuados.

Los parámetros de muestreo permiten afinar el comportamiento de los modelos de lenguaje para lograr el equilibrio deseado entre salidas deterministas y creativas.

Veamos cómo configurar estos parámetros en diferentes lenguajes de programación.

# [.NET](../../../../05-AdvancedTopics/mcp-sampling)

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
    - `allowedTools` para especificar qué herramientas puede usar el modelo durante la generación. En este caso, permitimos las herramientas `ideaGenerator` y `marketAnalyzer` para ayudar a generar ideas creativas para apps.
    - `frequencyPenalty` y `presencePenalty` para controlar la repetición y diversidad en la salida.
    - `temperature` para controlar la aleatoriedad de la salida, donde valores más altos conducen a respuestas más creativas.
    - `top_p` para limitar la selección de tokens a aquellos que contribuyen a la masa de probabilidad acumulada superior, mejorando la calidad del texto generado.
    - `top_k` para restringir el modelo a los K tokens más probables, lo que puede ayudar a generar respuestas más coherentes.
    - `frequencyPenalty` y `presencePenalty` para reducir la repetición y fomentar la diversidad en el texto generado.

# [JavaScript](../../../../05-AdvancedTopics/mcp-sampling)

```javascript
// JavaScript Example: Temperature and Top-P sampling configuration
const { McpClient } = require('@mcp/client');

async function demonstrateSampling() {
  // Initialize the MCP client
  const client = new McpClient({
    serverUrl: 'https://mcp-server-example.com',
    apiKey: process.env.MCP_API_KEY
  });
  
  // Configure request with different sampling parameters
  const creativeSampling = {
    temperature: 0.9,    // Higher temperature = more randomness/creativity
    topP: 0.92,          // Consider tokens with top 92% probability mass
    frequencyPenalty: 0.6, // Reduce repetition of token sequences
    presencePenalty: 0.4   // Penalize tokens that have appeared in the text so far
  };
  
  const factualSampling = {
    temperature: 0.2,    // Lower temperature = more deterministic/factual
    topP: 0.85,          // Slightly more focused token selection
    frequencyPenalty: 0.2, // Minimal repetition penalty
    presencePenalty: 0.1   // Minimal presence penalty
  };
  
  try {
    // Send two requests with different sampling configurations
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

- Inicializado un cliente MCP con una URL de servidor y una clave API.
- Configurado dos conjuntos de parámetros de muestreo: uno para tareas creativas y otro para tareas factuales.
- Enviado solicitudes con estas configuraciones, permitiendo que el modelo use herramientas específicas para cada tarea.
- Impreso las respuestas generadas para demostrar los efectos de diferentes parámetros de muestreo.
- Usado `allowedTools` para especificar qué herramientas puede usar el modelo durante la generación. En este caso, permitimos `ideaGenerator` y `environmentalImpactTool` para tareas creativas, y `factChecker` y `dataAnalysisTool` para tareas factuales.
- Usado `temperature` para controlar la aleatoriedad de la salida, donde valores más altos conducen a respuestas más creativas.
- Usado `top_p` para limitar la selección de tokens a aquellos que contribuyen a la masa de probabilidad acumulada superior, mejorando la calidad del texto generado.
- Usado `frequencyPenalty` y `presencePenalty` para reducir la repetición y fomentar la diversidad en la salida.
- Usado `top_k` para restringir el modelo a los K tokens más probables, lo que puede ayudar a generar respuestas más coherentes.

---

## Muestreo Determinista

Para aplicaciones que requieren salidas consistentes, el muestreo determinista asegura resultados reproducibles. Esto se logra usando una semilla aleatoria fija y estableciendo la temperatura en cero.

Veamos la siguiente implementación de ejemplo para demostrar el muestreo determinista en diferentes lenguajes de programación.

# [Java](../../../../05-AdvancedTopics/mcp-sampling)

```java
// Java Example: Deterministic responses with fixed seed
public class DeterministicSamplingExample {
    public void demonstrateDeterministicResponses() {
        McpClient client = new McpClient.Builder()
            .setServerUrl("https://mcp-server-example.com")
            .build();
            
        long fixedSeed = 12345; // Using a fixed seed for deterministic results
        
        // First request with fixed seed
        McpRequest request1 = new McpRequest.Builder()
            .setPrompt("Generate a random number between 1 and 100")
            .setSeed(fixedSeed)
            .setTemperature(0.0) // Zero temperature for maximum determinism
            .build();
            
        // Second request with the same seed
        McpRequest request2 = new McpRequest.Builder()
            .setPrompt("Generate a random number between 1 and 100")
            .setSeed(fixedSeed)
            .setTemperature(0.0)
            .build();
        
        // Execute both requests
        McpResponse response1 = client.sendRequest(request1);
        McpResponse response2 = client.sendRequest(request2);
        
        // Responses should be identical due to same seed and temperature=0
        System.out.println("Response 1: " + response1.getGeneratedText());
        System.out.println("Response 2: " + response2.getGeneratedText());
        System.out.println("Are responses identical: " + 
            response1.getGeneratedText().equals(response2.getGeneratedText()));
    }
}
```

En el código anterior hemos:

- Creado un cliente MCP con una URL de servidor especificada.
- Configurado dos solicitudes con el mismo prompt, semilla fija y temperatura cero.
- Enviado ambas solicitudes e impreso el texto generado.
- Demostrado que las respuestas son idénticas debido a la naturaleza determinista de la configuración de muestreo (misma semilla y temperatura).
- Usado `setSeed` para especificar una semilla aleatoria fija, asegurando que el modelo genere la misma salida para la misma entrada cada vez.
- Establecido `temperature` en cero para asegurar máxima determinismo, lo que significa que el modelo siempre seleccionará el token siguiente más probable sin aleatoriedad.

# [JavaScript](../../../../05-AdvancedTopics/mcp-sampling)

```javascript
// JavaScript Example: Deterministic responses with seed control
const { McpClient } = require('@mcp/client');

async function deterministicSampling() {
  const client = new McpClient({
    serverUrl: 'https://mcp-server-example.com'
  });
  
  const fixedSeed = 12345;
  const prompt = "Generate a random password with 8 characters";
  
  try {
    // First request with fixed seed
    const response1 = await client.sendPrompt(prompt, {
      seed: fixedSeed,
      temperature: 0.0  // Zero temperature for maximum determinism
    });
    
    // Second request with same seed and temperature
    const response2 = await client.sendPrompt(prompt, {
      seed: fixedSeed,
      temperature: 0.0
    });
    
    // Third request with different seed but same temperature
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

En el código anterior hemos:

- Inicializado un cliente MCP con una URL de servidor.
- Configurado dos solicitudes con el mismo prompt, semilla fija y temperatura cero.
- Enviado ambas solicitudes e impreso el texto generado.
- Demostrado que las respuestas son idénticas debido a la naturaleza determinista de la configuración de muestreo (misma semilla y temperatura).
- Usado `seed` para especificar una semilla aleatoria fija, asegurando que el modelo genere la misma salida para la misma entrada cada vez.
- Establecido `temperature` en cero para asegurar máxima determinismo, lo que significa que el modelo siempre seleccionará el token siguiente más probable sin aleatoriedad.
- Usado una semilla diferente para la tercera solicitud para mostrar que cambiar la semilla resulta en salidas diferentes, incluso con el mismo prompt y temperatura.

---

## Configuración Dinámica de Muestreo

El muestreo inteligente adapta los parámetros según el contexto y los requisitos de cada solicitud. Esto significa ajustar dinámicamente parámetros como temperature, top_p y penalizaciones según el tipo de tarea, preferencias del usuario o desempeño histórico.

Veamos cómo implementar muestreo dinámico en diferentes lenguajes de programación.

# [Python](../../../../05-AdvancedTopics/mcp-sampling)

```python
# Python Example: Dynamic sampling based on request context
class DynamicSamplingService:
    def __init__(self, mcp_client):
        self.client = mcp_client
        
    async def generate_with_adaptive_sampling(self, prompt, task_type, user_preferences=None):
        """Uses different sampling strategies based on task type and user preferences"""
        
        # Define sampling presets for different task types
        sampling_presets = {
            "creative": {"temperature": 0.9, "top_p": 0.95, "frequency_penalty": 0.7},
            "factual": {"temperature": 0.2, "top_p": 0.85, "frequency_penalty": 0.2},
            "code": {"temperature": 0.3, "top_p": 0.9, "frequency_penalty": 0.5},
            "analytical": {"temperature": 0.4, "top_p": 0.92, "frequency_penalty": 0.3}
        }
        
        # Select base preset
        sampling_params = sampling_presets.get(task_type, sampling_presets["factual"])
        
        # Adjust based on user preferences if provided
        if user_preferences:
            if "creativity_level" in user_preferences:
                # Scale temperature based on creativity preference (1-10)
                creativity = min(max(user_preferences["creativity_level"], 1), 10) / 10
                sampling_params["temperature"] = 0.1 + (0.9 * creativity)
            
            if "diversity" in user_preferences:
                # Adjust top_p based on desired response diversity
                diversity = min(max(user_preferences["diversity"], 1), 10) / 10
                sampling_params["top_p"] = 0.6 + (0.39 * diversity)
        
        # Create and send request with custom sampling parameters
        response = await self.client.send_request(
            prompt=prompt,
            temperature=sampling_params["temperature"],
            top_p=sampling_params["top_p"],
            frequency_penalty=sampling_params["frequency_penalty"]
        )
        
        # Return response with sampling metadata for transparency
        return {
            "text": response.generated_text,
            "applied_sampling": sampling_params,
            "task_type": task_type
        }
```

En el código anterior hemos:

- Creado una clase `DynamicSamplingService` que gestiona el muestreo adaptativo.
- Definido presets de muestreo para diferentes tipos de tarea (creativa, factual, código, analítica).
- Seleccionado un preset base de muestreo según el tipo de tarea.
- Ajustado los parámetros de muestreo según las preferencias del usuario, como nivel de creatividad y diversidad.
- Enviado la solicitud con los parámetros de muestreo configurados dinámicamente.
- Devuelto el texto generado junto con los parámetros de muestreo aplicados y el tipo de tarea para transparencia.
- Usado `temperature` para controlar la aleatoriedad de la salida, donde valores más altos conducen a respuestas más creativas.
- Usado `top_p` para limitar la selección de tokens a aquellos que contribuyen a la masa de probabilidad acumulada superior, mejorando la calidad del texto generado.
- Usado `frequency_penalty` para reducir la repetición y fomentar la diversidad en la salida.
- Usado `user_preferences` para permitir la personalización de los parámetros de muestreo según niveles definidos por el usuario de creatividad y diversidad.
- Usado `task_type` para determinar la estrategia de muestreo adecuada para la solicitud, permitiendo respuestas más ajustadas según la naturaleza de la tarea.
- Usado el método `send_request` para enviar el prompt con los parámetros de muestreo configurados, asegurando que el modelo genere texto conforme a los requisitos especificados.
- Usado `generated_text` para obtener la respuesta del modelo, que luego se devuelve junto con los parámetros de muestreo y el tipo de tarea para análisis o visualización.
- Usado funciones `min` y `max` para asegurar que las preferencias del usuario estén dentro de rangos válidos, evitando configuraciones de muestreo inválidas.

# [JavaScript Dynamic](../../../../05-AdvancedTopics/mcp-sampling)

```javascript
// JavaScript Example: Dynamic sampling configuration based on user context
class AdaptiveSamplingManager {
  constructor(mcpClient) {
    this.client = mcpClient;
    
    // Define base sampling profiles
    this.samplingProfiles = {
      creative: { temperature: 0.85, topP: 0.94, frequencyPenalty: 0.7, presencePenalty: 0.5 },
      factual: { temperature: 0.2, topP: 0.85, frequencyPenalty: 0.3, presencePenalty: 0.1 },
      code: { temperature: 0.25, topP: 0.9, frequencyPenalty: 0.4, presencePenalty: 0.3 },
      conversational: { temperature: 0.7, topP: 0.9, frequencyPenalty: 0.6, presencePenalty: 0.4 }
    };
    
    // Track historical performance
    this.performanceHistory = [];
  }
  
  // Detect task type from prompt
  detectTaskType(prompt, context = {}) {
    const promptLower = prompt.toLowerCase();
    
    // Simple heuristic detection - could be enhanced with ML classification
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
    
    // Default to conversational if no clear type is detected
    return 'conversational';
  }
  
  // Calculate sampling parameters based on context and user preferences
  getSamplingParameters(prompt, context = {}) {
    // Detect the type of task
    const taskType = this.detectTaskType(prompt, context);
    
    // Get base profile
    let params = {...this.samplingProfiles[taskType]};
    
    // Adjust based on user preferences
    if (context.userPreferences) {
      const { creativity, precision, consistency } = context.userPreferences;
      
      if (creativity !== undefined) {
        // Scale from 1-10 to appropriate temperature range
        params.temperature = 0.1 + (creativity * 0.09); // 0.1-1.0
      }
      
      if (precision !== undefined) {
        // Higher precision means lower topP (more focused selection)
        params.topP = 1.0 - (precision * 0.05); // 0.5-1.0
      }
      
      if (consistency !== undefined) {
        // Higher consistency means lower penalties
        params.frequencyPenalty = 0.1 + ((10 - consistency) * 0.08); // 0.1-0.9
      }
    }
    
    // Apply learned adjustments from performance history
    this.applyLearnedAdjustments(params, taskType);
    
    return params;
  }
  
  applyLearnedAdjustments(params, taskType) {
    // Simple adaptive logic - could be enhanced with more sophisticated algorithms
    const relevantHistory = this.performanceHistory
      .filter(entry => entry.taskType === taskType)
      .slice(-5); // Only consider recent history
    
    if (relevantHistory.length > 0) {
      // Calculate average performance scores
      const avgScore = relevantHistory.reduce((sum, entry) => sum + entry.score, 0) / relevantHistory.length;
      
      // If performance is below threshold, adjust parameters
      if (avgScore < 0.7) {
        // Slight adjustment toward safer values
        params.temperature = Math.max(params.temperature * 0.9, 0.1);
        params.topP = Math.max(params.topP * 0.95, 0.5);
      }
    }
  }
  
  recordPerformance(prompt, samplingParams, response, score) {
    // Record performance for future adjustments
    this.performanceHistory.push({
      timestamp: Date.now(),
      taskType: this.detectTaskType(prompt),
      samplingParams,
      responseLength: response.generatedText.length,
      score // 0-1 rating of response quality
    });
    
    // Limit history size
    if (this.performanceHistory.length > 100) {
      this.performanceHistory.shift();
    }
  }
  
  async generateResponse(prompt, context = {}) {
    // Get optimized sampling parameters
    const samplingParams = this.getSamplingParameters(prompt, context);
    
    // Send request with optimized parameters
    const response = await this.client.sendPrompt(prompt, {
      ...samplingParams,
      allowedTools: context.allowedTools || []
    });
    
    // If user provides feedback, record it for future optimization
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

// Example usage
async function demonstrateAdaptiveSampling() {
  const client = new McpClient({
    serverUrl: 'https://mcp-server-example.com'
  });
  
  const samplingManager = new AdaptiveSamplingManager(client);
  
  try {
    // Creative task with custom user preferences
    const creativeResult = await samplingManager.generateResponse(
      "Write a short poem about artificial intelligence",
      {
        userPreferences: {
          creativity: 9,  // High creativity (1-10)
          consistency: 3  // Low consistency (1-10)
        }
      }
    );
    
    console.log('Creative Task:');
    console.log(`Detected type: ${creativeResult.detectedTaskType}`);
    console.log('Applied sampling:', creativeResult.appliedSamplingParams);
    console.log(creativeResult.response.generatedText);
    
    // Code generation task
    const codeResult = await samplingManager.generateResponse(
      "Write a JavaScript function to calculate the Fibonacci sequence",
      {
        userPreferences: {
          creativity: 2,  // Low creativity
          precision: 8,   // High precision
          consistency: 9  // High consistency
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

En el código anterior hemos:

- Creado una clase `AdaptiveSamplingManager` que gestiona el muestreo dinámico basado en el tipo de tarea y preferencias del usuario.
- Definido perfiles de muestreo para diferentes tipos de tarea (creativa, factual, código, conversacional).
- Implementado un método para detectar el tipo de tarea a partir del prompt usando heurísticas simples.
- Calculado los parámetros de muestreo basados en el tipo de tarea detectado y las preferencias del usuario.
- Aplicado ajustes aprendidos basados en el desempeño histórico para optimizar los parámetros de muestreo.
- Registrado el desempeño para futuros ajustes, permitiendo que el sistema aprenda de interacciones pasadas.
- Enviado solicitudes con parámetros de muestreo configurados dinámicamente y devuelto el texto generado junto con los parámetros aplicados y el tipo de tarea detectado.
- Usado:
    - `userPreferences` para permitir la personalización de los parámetros de muestreo según niveles definidos por el usuario de creatividad, precisión y consistencia.
    - `detectTaskType` para determinar la naturaleza de la tarea basada en el prompt, permitiendo respuestas más ajustadas.
    - `recordPerformance` para registrar el desempeño de las respuestas generadas, habilitando que el sistema se adapte y mejore con el tiempo.
    - `applyLearnedAdjustments` para modificar los parámetros de muestreo basados en el desempeño histórico, mejorando la capacidad del modelo para generar respuestas de alta calidad.
    - `generateResponse` para encapsular todo el proceso de generación de respuesta con muestreo adaptativo, facilitando su uso con diferentes prompts y contextos.
    - `allowedTools` para especificar qué herramientas puede usar el modelo durante la generación, permitiendo respuestas más contextualizadas.
    - `feedbackScore` para permitir que los usuarios proporcionen retroalimentación sobre la calidad de la respuesta generada, que puede usarse para refinar aún más el desempeño del modelo con el tiempo.
    - `performanceHistory` para mantener un registro de interacciones pasadas, permitiendo que el sistema aprenda de éxitos y fallos anteriores.
    - `getSamplingParameters` para ajustar dinámicamente los parámetros de muestreo según el contexto de la solicitud, permitiendo un comportamiento del modelo más flexible y receptivo.
    - `detectTaskType` para clasificar la tarea basada en el prompt, habilitando la aplicación de estrategias de muestreo apropiadas para diferentes tipos de solicitudes.
    - `samplingProfiles` para definir configuraciones base de muestreo para diferentes tipos de tarea, permitiendo ajustes rápidos según la naturaleza de la solicitud.

---

## Qué sigue

- [5.7 Escalado](../mcp-scaling/README.md)

**Aviso legal**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda la traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o interpretaciones erróneas derivadas del uso de esta traducción.