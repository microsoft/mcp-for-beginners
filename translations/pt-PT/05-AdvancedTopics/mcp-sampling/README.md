# Amostragem no Protocolo de Contexto do Modelo

A amostragem é uma funcionalidade poderosa do MCP que permite aos servidores solicitar completions de LLM através do cliente, possibilitando comportamentos agentivos sofisticados enquanto mantém a segurança e a privacidade. A configuração correta da amostragem pode melhorar significativamente a qualidade e o desempenho das respostas. O MCP fornece uma forma padronizada de controlar como os modelos geram texto com parâmetros específicos que influenciam a aleatoriedade, criatividade e coerência.

## Introdução

Nesta lição, vamos explorar como configurar os parâmetros de amostragem em pedidos MCP e compreender a mecânica subjacente do protocolo de amostragem.

## Objetivos de Aprendizagem

No final desta lição, será capaz de:

- Compreender os principais parâmetros de amostragem disponíveis no MCP.
- Configurar parâmetros de amostragem para diferentes casos de uso.
- Implementar amostragem determinística para resultados reproduzíveis.
- Ajustar dinamicamente os parâmetros de amostragem com base no contexto e nas preferências do utilizador.
- Aplicar estratégias de amostragem para melhorar o desempenho do modelo em vários cenários.
- Entender como a amostragem funciona no fluxo cliente-servidor do MCP.

## Como Funciona a Amostragem no MCP

O fluxo de amostragem no MCP segue estes passos:

1. O servidor envia um pedido `sampling/createMessage` ao cliente
2. O cliente revê o pedido e pode modificá-lo
3. O cliente realiza a amostragem a partir de um LLM
4. O cliente revê a completion
5. O cliente devolve o resultado ao servidor

Este design com intervenção humana garante que os utilizadores mantêm controlo sobre o que o LLM vê e gera.

## Visão Geral dos Parâmetros de Amostragem

O MCP define os seguintes parâmetros de amostragem que podem ser configurados nos pedidos do cliente:

| Parâmetro | Descrição | Intervalo Típico |
|-----------|-----------|------------------|
| `temperature` | Controla a aleatoriedade na seleção de tokens | 0.0 - 1.0 |
| `maxTokens` | Número máximo de tokens a gerar | Valor inteiro |
| `stopSequences` | Sequências personalizadas que interrompem a geração quando encontradas | Array de strings |
| `metadata` | Parâmetros adicionais específicos do fornecedor | Objeto JSON |

Muitos fornecedores de LLM suportam parâmetros adicionais através do campo `metadata`, que podem incluir:

| Parâmetro de Extensão Comum | Descrição | Intervalo Típico |
|-----------------------------|-----------|------------------|
| `top_p` | Amostragem núcleo - limita tokens à probabilidade cumulativa superior | 0.0 - 1.0 |
| `top_k` | Limita a seleção de tokens às K opções mais prováveis | 1 - 100 |
| `presence_penalty` | Penaliza tokens com base na sua presença no texto até ao momento | -2.0 - 2.0 |
| `frequency_penalty` | Penaliza tokens com base na sua frequência no texto até ao momento | -2.0 - 2.0 |
| `seed` | Semente aleatória específica para resultados reproduzíveis | Valor inteiro |

## Exemplo de Formato de Pedido

Aqui está um exemplo de pedido de amostragem a um cliente no MCP:

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

## Formato da Resposta

O cliente devolve um resultado de completion:

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

## Controlo Humano no Processo

A amostragem MCP foi desenhada com supervisão humana em mente:

- **Para prompts**:
  - Os clientes devem mostrar aos utilizadores o prompt proposto
  - Os utilizadores devem poder modificar ou rejeitar prompts
  - Prompts do sistema podem ser filtrados ou modificados
  - A inclusão do contexto é controlada pelo cliente

- **Para completions**:
  - Os clientes devem mostrar aos utilizadores a completion
  - Os utilizadores devem poder modificar ou rejeitar completions
  - Os clientes podem filtrar ou modificar completions
  - Os utilizadores controlam qual modelo é usado

Com estes princípios em mente, vejamos como implementar a amostragem em diferentes linguagens de programação, focando nos parâmetros que são comumente suportados pelos fornecedores de LLM.

## Considerações de Segurança

Ao implementar a amostragem no MCP, considere estas melhores práticas de segurança:

- **Validar todo o conteúdo da mensagem** antes de o enviar ao cliente
- **Sanitizar informações sensíveis** dos prompts e completions
- **Implementar limites de taxa** para prevenir abusos
- **Monitorizar o uso da amostragem** para detetar padrões invulgares
- **Encriptar dados em trânsito** usando protocolos seguros
- **Gerir a privacidade dos dados dos utilizadores** conforme as regulamentações aplicáveis
- **Auditar pedidos de amostragem** para conformidade e segurança
- **Controlar a exposição a custos** com limites apropriados
- **Implementar timeouts** para pedidos de amostragem
- **Tratar erros do modelo de forma elegante** com mecanismos de fallback adequados

Os parâmetros de amostragem permitem afinar o comportamento dos modelos de linguagem para alcançar o equilíbrio desejado entre saídas determinísticas e criativas.

Vamos ver como configurar estes parâmetros em diferentes linguagens de programação.

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

No código anterior fizemos:

- Criámos um cliente MCP com uma URL de servidor específica.
- Configurámos um pedido com parâmetros de amostragem como `temperature`, `top_p` e `top_k`.
- Enviámos o pedido e imprimimos o texto gerado.
- Usámos:
    - `allowedTools` para especificar quais ferramentas o modelo pode usar durante a geração. Neste caso, permitimos as ferramentas `ideaGenerator` e `marketAnalyzer` para ajudar a gerar ideias criativas para apps.
    - `frequencyPenalty` e `presencePenalty` para controlar a repetição e diversidade na saída.
    - `temperature` para controlar a aleatoriedade da saída, onde valores mais altos levam a respostas mais criativas.
    - `top_p` para limitar a seleção de tokens àqueles que contribuem para a massa cumulativa de probabilidade superior, melhorando a qualidade do texto gerado.
    - `top_k` para restringir o modelo aos K tokens mais prováveis, o que pode ajudar a gerar respostas mais coerentes.
    - `frequencyPenalty` e `presencePenalty` para reduzir a repetição e incentivar a diversidade no texto gerado.

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

No código anterior fizemos:

- Inicializámos um cliente MCP com uma URL de servidor e uma chave API.
- Configurámos dois conjuntos de parâmetros de amostragem: um para tarefas criativas e outro para tarefas factuais.
- Enviámos pedidos com estas configurações, permitindo que o modelo usasse ferramentas específicas para cada tarefa.
- Imprimimos as respostas geradas para demonstrar os efeitos de diferentes parâmetros de amostragem.
- Usámos `allowedTools` para especificar quais ferramentas o modelo pode usar durante a geração. Neste caso, permitimos `ideaGenerator` e `environmentalImpactTool` para tarefas criativas, e `factChecker` e `dataAnalysisTool` para tarefas factuais.
- Usámos `temperature` para controlar a aleatoriedade da saída, onde valores mais altos levam a respostas mais criativas.
- Usámos `top_p` para limitar a seleção de tokens àqueles que contribuem para a massa cumulativa de probabilidade superior, melhorando a qualidade do texto gerado.
- Usámos `frequencyPenalty` e `presencePenalty` para reduzir a repetição e incentivar a diversidade na saída.
- Usámos `top_k` para restringir o modelo aos K tokens mais prováveis, o que pode ajudar a gerar respostas mais coerentes.

---

## Amostragem Determinística

Para aplicações que requerem saídas consistentes, a amostragem determinística garante resultados reproduzíveis. Isto é conseguido usando uma semente aleatória fixa e definindo a temperatura a zero.

Vamos ver um exemplo de implementação para demonstrar a amostragem determinística em diferentes linguagens de programação.

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

No código anterior fizemos:

- Criámos um cliente MCP com uma URL de servidor especificada.
- Configurámos dois pedidos com o mesmo prompt, semente fixa e temperatura zero.
- Enviámos ambos os pedidos e imprimimos o texto gerado.
- Demonstrámos que as respostas são idênticas devido à natureza determinística da configuração de amostragem (mesma semente e temperatura).
- Usámos `setSeed` para especificar uma semente aleatória fixa, garantindo que o modelo gera a mesma saída para a mesma entrada todas as vezes.
- Definimos `temperature` a zero para garantir máxima determinismo, significando que o modelo selecionará sempre o token seguinte mais provável sem aleatoriedade.

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

No código anterior fizemos:

- Inicializámos um cliente MCP com uma URL de servidor.
- Configurámos dois pedidos com o mesmo prompt, semente fixa e temperatura zero.
- Enviámos ambos os pedidos e imprimimos o texto gerado.
- Demonstrámos que as respostas são idênticas devido à natureza determinística da configuração de amostragem (mesma semente e temperatura).
- Usámos `seed` para especificar uma semente aleatória fixa, garantindo que o modelo gera a mesma saída para a mesma entrada todas as vezes.
- Definimos `temperature` a zero para garantir máxima determinismo, significando que o modelo selecionará sempre o token seguinte mais provável sem aleatoriedade.
- Usámos uma semente diferente para o terceiro pedido para mostrar que alterar a semente resulta em saídas diferentes, mesmo com o mesmo prompt e temperatura.

---

## Configuração Dinâmica da Amostragem

A amostragem inteligente adapta os parâmetros com base no contexto e nos requisitos de cada pedido. Isso significa ajustar dinamicamente parâmetros como temperature, top_p e penalizações com base no tipo de tarefa, preferências do utilizador ou desempenho histórico.

Vamos ver como implementar a amostragem dinâmica em diferentes linguagens de programação.

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

No código anterior fizemos:

- Criámos uma classe `DynamicSamplingService` que gere a amostragem adaptativa.
- Definimos predefinições de amostragem para diferentes tipos de tarefa (criativa, factual, código, analítica).
- Selecionámos uma predefinição base de amostragem com base no tipo de tarefa.
- Ajustámos os parâmetros de amostragem com base nas preferências do utilizador, como nível de criatividade e diversidade.
- Enviámos o pedido com os parâmetros de amostragem configurados dinamicamente.
- Devolvemos o texto gerado juntamente com os parâmetros de amostragem aplicados e o tipo de tarefa para transparência.
- Usámos `temperature` para controlar a aleatoriedade da saída, onde valores mais altos levam a respostas mais criativas.
- Usámos `top_p` para limitar a seleção de tokens àqueles que contribuem para a massa cumulativa de probabilidade superior, melhorando a qualidade do texto gerado.
- Usámos `frequency_penalty` para reduzir a repetição e incentivar a diversidade na saída.
- Usámos `user_preferences` para permitir a personalização dos parâmetros de amostragem com base nos níveis de criatividade e diversidade definidos pelo utilizador.
- Usámos `task_type` para determinar a estratégia de amostragem apropriada para o pedido, permitindo respostas mais ajustadas à natureza da tarefa.
- Usámos o método `send_request` para enviar o prompt com os parâmetros de amostragem configurados, garantindo que o modelo gera texto conforme os requisitos especificados.
- Usámos `generated_text` para obter a resposta do modelo, que é então devolvida juntamente com os parâmetros de amostragem e o tipo de tarefa para análise ou apresentação.
- Usámos as funções `min` e `max` para garantir que as preferências do utilizador estão dentro de intervalos válidos, evitando configurações inválidas de amostragem.

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

No código anterior fizemos:

- Criámos uma classe `AdaptiveSamplingManager` que gere a amostragem dinâmica com base no tipo de tarefa e nas preferências do utilizador.
- Definimos perfis de amostragem para diferentes tipos de tarefa (criativa, factual, código, conversacional).
- Implementámos um método para detetar o tipo de tarefa a partir do prompt usando heurísticas simples.
- Calculámos os parâmetros de amostragem com base no tipo de tarefa detetado e nas preferências do utilizador.
- Aplicámos ajustes aprendidos com base no desempenho histórico para otimizar os parâmetros de amostragem.
- Registámos o desempenho para ajustes futuros, permitindo que o sistema aprenda com interações passadas.
- Enviámos pedidos com parâmetros de amostragem configurados dinamicamente e devolvemos o texto gerado juntamente com os parâmetros aplicados e o tipo de tarefa detetado.
- Usámos:
    - `userPreferences` para permitir a personalização dos parâmetros de amostragem com base nos níveis de criatividade, precisão e consistência definidos pelo utilizador.
    - `detectTaskType` para determinar a natureza da tarefa com base no prompt, permitindo respostas mais ajustadas.
    - `recordPerformance` para registar o desempenho das respostas geradas, permitindo que o sistema se adapte e melhore ao longo do tempo.
    - `applyLearnedAdjustments` para modificar os parâmetros de amostragem com base no desempenho histórico, melhorando a capacidade do modelo de gerar respostas de alta qualidade.
    - `generateResponse` para encapsular todo o processo de geração de resposta com amostragem adaptativa, facilitando a chamada com diferentes prompts e contextos.
    - `allowedTools` para especificar quais ferramentas o modelo pode usar durante a geração, permitindo respostas mais contextualizadas.
    - `feedbackScore` para permitir que os utilizadores forneçam feedback sobre a qualidade da resposta gerada, que pode ser usado para refinar ainda mais o desempenho do modelo ao longo do tempo.
    - `performanceHistory` para manter um registo das interações passadas, permitindo que o sistema aprenda com sucessos e falhas anteriores.
    - `getSamplingParameters` para ajustar dinamicamente os parâmetros de amostragem com base no contexto do pedido, permitindo um comportamento do modelo mais flexível e responsivo.
    - `detectTaskType` para classificar a tarefa com base no prompt, permitindo que o sistema aplique estratégias de amostragem apropriadas para diferentes tipos de pedidos.
    - `samplingProfiles` para definir configurações base de amostragem para diferentes tipos de tarefa, permitindo ajustes rápidos com base na natureza do pedido.

---

## O que vem a seguir

- [5.7 Escalabilidade](../mcp-scaling/README.md)

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, por favor tenha em conta que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes da utilização desta tradução.