> [!WARNING]
> A amostragem está obsoleta em MCP `2026-07-28`. Esta lição é mantida para
> implementações legadas. Novos servidores devem integrar-se diretamente com uma API
> de provedores LLM.

# Amostragem no Protocolo de Contexto de Modelo

> A amostragem permanece na especificação `2026-07-28` para compatibilidade e pode
> ser removida na primeira revisão lançada em ou após 28 de julho de
> 2027. Exemplos nesta lição podem usar APIs SDK que implementam `2025-11-25`.
> Veja [O que mudou em MCP: A especificação 2026-07-28](../../01-CoreConcepts/mcp-2026-07-28.md).

Em implementações legadas do MCP, a amostragem permite que servidores solicitem
completions do LLM através do cliente. Esta lição explica o fluxo do protocolo
obsoleto para compatibilidade e trabalho de migração.

## Introdução

Nesta lição, exploraremos como configurar parâmetros de amostragem em solicitações MCP e entender a mecânica de protocolo subjacente da amostragem.

## Objetivos de Aprendizagem

Ao final desta lição, você será capaz de:

- Compreender os principais parâmetros de amostragem disponíveis no MCP.
- Configurar parâmetros de amostragem para diferentes casos de uso.
- Implementar amostragem determinística para resultados reproduzíveis.
- Ajustar dinamicamente parâmetros de amostragem com base no contexto e preferências do usuário.
- Aplicar estratégias de amostragem para melhorar o desempenho do modelo em vários cenários.
- Compreender como a amostragem funciona no fluxo cliente-servidor do MCP.

## Como a Amostragem Funciona no MCP

O fluxo de amostragem no MCP segue os seguintes passos:

1. O servidor envia uma requisição `sampling/createMessage` para o cliente
2. O cliente revisa e pode modificar a requisição
3. O cliente realiza a amostragem de um LLM
4. O cliente revisa a completion
5. O cliente retorna o resultado ao servidor

Este design com intervenção humana assegura que os usuários mantenham o controle sobre o que o LLM vê e gera.

## Visão Geral dos Parâmetros de Amostragem

O MCP define os seguintes parâmetros de amostragem que podem ser configurados em solicitações do cliente:

| Parâmetro | Descrição | Intervalo Típico |
|-----------|-------------|---------------|
| `temperature` | Controla a aleatoriedade na seleção de tokens | 0.0 - 1.0 |
| `maxTokens` | Número máximo de tokens a gerar | Valor inteiro |
| `stopSequences` | Sequências personalizadas que interrompem a geração ao serem encontradas | Array de strings |
| `metadata` | Parâmetros adicionais específicos do provedor | Objeto JSON |

Muitos provedores LLM suportam parâmetros adicionais através do campo `metadata`, que podem incluir:

| Parâmetro de Extensão Comum | Descrição | Intervalo Típico |
|-----------|-------------|---------------|
| `top_p` | Amostragem de núcleo - limita tokens à probabilidade cumulativa superior | 0.0 - 1.0 |
| `top_k` | Limita seleção de tokens às K opções mais prováveis | 1 - 100 |
| `presence_penalty` | Penaliza tokens com base na presença prévia no texto | -2.0 - 2.0 |
| `frequency_penalty` | Penaliza tokens com base na frequência no texto até agora | -2.0 - 2.0 |
| `seed` | Semente aleatória específica para resultados reproduzíveis | Valor inteiro |

## Exemplo de Formato de Requisição

Aqui está um exemplo de solicitação de amostragem de um cliente no MCP:

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

## Formato de Resposta

O cliente retorna um resultado de completion:

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

## Controles com Intervenção Humana

A amostragem no MCP foi projetada com supervisão humana em mente:

- **Para prompts**:
  - Os clientes devem mostrar aos usuários o prompt proposto
  - Os usuários devem poder modificar ou rejeitar os prompts
  - Prompts do sistema podem ser filtrados ou modificados
  - A inclusão do contexto é controlada pelo cliente

- **Para completions**:
  - Os clientes devem mostrar aos usuários a completion
  - Os usuários devem poder modificar ou rejeitar as completions
  - Clientes podem filtrar ou modificar completions
  - Os usuários controlam qual modelo é utilizado

Com esses princípios em mente, vamos ver como implementar amostragem em diferentes linguagens de programação, focando nos parâmetros comumente suportados entre provedores LLM.

## Considerações de Segurança

Ao implementar amostragem no MCP, considere as melhores práticas de segurança a seguir:

- **Validar todo o conteúdo das mensagens** antes de enviá-las ao cliente
- **Sanitizar informações sensíveis** em prompts e completions
- **Implementar limites de taxa** para prevenir abusos
- **Monitorar o uso da amostragem** para padrões incomuns
- **Criptografar dados em trânsito** usando protocolos seguros
- **Tratar a privacidade dos dados do usuário** conforme regulamentos aplicáveis
- **Auditar solicitações de amostragem** para conformidade e segurança
- **Controlar exposição de custos** com limites apropriados
- **Implementar timeouts** para solicitações de amostragem
- **Tratar erros do modelo com elegância** usando alternativas adequadas

Parâmetros de amostragem permitem ajuste fino do comportamento dos modelos de linguagem para alcançar o equilíbrio desejado entre saídas determinísticas e criativas.

Vamos ver como configurar esses parâmetros em diferentes linguagens de programação.

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

No código precedente nós:

- Criamos um cliente MCP com uma URL de servidor específica.
- Configuramos uma requisição com parâmetros de amostragem como `temperature`, `top_p` e `top_k`.
- Enviamos a requisição e imprimimos o texto gerado.
- Usamos:
    - `allowedTools` para especificar quais ferramentas o modelo pode usar durante a geração. Neste caso, permitimos as ferramentas `ideaGenerator` e `marketAnalyzer` para ajudar a gerar ideias criativas de apps.
    - `frequencyPenalty` e `presencePenalty` para controlar repetição e diversidade na saída.
    - `temperature` para controlar a aleatoriedade da saída, onde valores mais altos levam a respostas mais criativas.
    - `top_p` para limitar a seleção de tokens àqueles que contribuem para a massa cumulativa de probabilidade superior, aprimorando a qualidade do texto gerado.
    - `top_k` para restringir o modelo aos K tokens mais prováveis, o que pode ajudar a gerar respostas mais coerentes.
    - `frequencyPenalty` e `presencePenalty` para reduzir repetição e incentivar diversidade no texto gerado.

# [JavaScript](#tab/javascript)

```javascript
// Exemplo em JavaScript: Configuração de temperatura e amostragem Top-P
const { McpClient } = require('@mcp/client');

async function demonstrateSampling() {
  // Inicializar o cliente MCP
  const client = new McpClient({
    serverUrl: 'https://mcp-server-example.com',
    apiKey: process.env.MCP_API_KEY
  });
  
  // Configurar requisição com diferentes parâmetros de amostragem
  const creativeSampling = {
    temperature: 0.9,    // Temperatura mais alta = mais aleatoriedade/criatividade
    topP: 0.92,          // Considerar tokens com massa de probabilidade top 92%
    frequencyPenalty: 0.6, // Reduzir repetição de sequências de tokens
    presencePenalty: 0.4   // Penalizar tokens que já apareceram no texto até agora
  };
  
  const factualSampling = {
    temperature: 0.2,    // Temperatura mais baixa = mais determinístico/factual
    topP: 0.85,          // Seleção de tokens um pouco mais focada
    frequencyPenalty: 0.2, // Penalidade mínima por repetição
    presencePenalty: 0.1   // Penalidade mínima por presença
  };
  
  try {
    // Enviar duas requisições com diferentes configurações de amostragem
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

No código precedente nós:

- Inicializamos um cliente MCP com uma URL de servidor e chave de API.
- Configuramos dois conjuntos de parâmetros de amostragem: um para tarefas criativas e outro para tarefas factuais.
- Enviamos requisições com essas configurações, permitindo que o modelo use ferramentas específicas para cada tarefa.
- Imprimimos as respostas geradas para demonstrar os efeitos dos diferentes parâmetros de amostragem.
- Usamos `allowedTools` para especificar quais ferramentas o modelo pode usar durante a geração. Neste caso, permitimos `ideaGenerator` e `environmentalImpactTool` para tarefas criativas, e `factChecker` e `dataAnalysisTool` para tarefas factuais.
- Usamos `temperature` para controlar a aleatoriedade da saída, onde valores mais altos levam a respostas mais criativas.
- Usamos `top_p` para limitar a seleção de tokens àqueles que contribuem para a massa cumulativa de probabilidade superior, aprimorando a qualidade do texto gerado.
- Usamos `frequencyPenalty` e `presencePenalty` para reduzir repetição e incentivar diversidade na saída.
- Usamos `top_k` para restringir o modelo aos K tokens mais prováveis, o que pode ajudar a gerar respostas mais coerentes.

---

## Amostragem Determinística

Para aplicações que requerem saídas consistentes, a amostragem determinística assegura resultados reproduzíveis. Como isso é feito usando uma semente aleatória fixa e configurando a temperature em zero.

Vamos ver a seguir uma implementação exemplo para demonstrar amostragem determinística em diferentes linguagens de programação.

# [Java](#tab/java)

```java
// Exemplo em Java: Respostas determinísticas com semente fixa
public class DeterministicSamplingExample {
    public void demonstrateDeterministicResponses() {
        McpClient client = new McpClient.Builder()
            .setServerUrl("https://mcp-server-example.com")
            .build();
            
        long fixedSeed = 12345; // Usando uma semente fixa para resultados determinísticos
        
        // Primeira requisição com semente fixa
        McpRequest request1 = new McpRequest.Builder()
            .setPrompt("Generate a random number between 1 and 100")
            .setSeed(fixedSeed)
            .setTemperature(0.0) // Temperatura zero para máximo determinismo
            .build();
            
        // Segunda requisição com a mesma semente
        McpRequest request2 = new McpRequest.Builder()
            .setPrompt("Generate a random number between 1 and 100")
            .setSeed(fixedSeed)
            .setTemperature(0.0)
            .build();
        
        // Executar ambas as requisições
        McpResponse response1 = client.sendRequest(request1);
        McpResponse response2 = client.sendRequest(request2);
        
        // As respostas devem ser idênticas devido à mesma semente e temperatura=0
        System.out.println("Response 1: " + response1.getGeneratedText());
        System.out.println("Response 2: " + response2.getGeneratedText());
        System.out.println("Are responses identical: " + 
            response1.getGeneratedText().equals(response2.getGeneratedText()));
    }
}
```

No código precedente nós:

- Criamos um cliente MCP com uma URL de servidor especificada.
- Configuramos duas requisições com o mesmo prompt, semente fixa, e temperatura zero.
- Enviamos ambas requisições e imprimimos o texto gerado.
- Demonstramos que as respostas são idênticas devido à natureza determinística da configuração de amostragem (mesma semente e temperatura).
- Usamos `setSeed` para especificar uma semente aleatória fixa, garantindo que o modelo gere a mesma saída para a mesma entrada sempre.
- Configuramos `temperature` para zero para garantir máximo determinismo, o que significa que o modelo sempre selecionará o token seguinte mais provável sem aleatoriedade.

# [JavaScript](#tab/javascript-deterministic)

```javascript
// Exemplo JavaScript: Respostas determinísticas com controle de semente
const { McpClient } = require('@mcp/client');

async function deterministicSampling() {
  const client = new McpClient({
    serverUrl: 'https://mcp-server-example.com'
  });
  
  const fixedSeed = 12345;
  const prompt = "Generate a random password with 8 characters";
  
  try {
    // Primeira requisição com semente fixa
    const response1 = await client.sendPrompt(prompt, {
      seed: fixedSeed,
      temperature: 0.0  // Temperatura zero para máximo determinismo
    });
    
    // Segunda requisição com mesma semente e temperatura
    const response2 = await client.sendPrompt(prompt, {
      seed: fixedSeed,
      temperature: 0.0
    });
    
    // Terceira requisição com semente diferente, mas mesma temperatura
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

No código precedente nós:

- Inicializamos um cliente MCP com uma URL de servidor.
- Configuramos duas requisições com o mesmo prompt, semente fixa, e temperatura zero.
- Enviamos ambas requisições e imprimimos o texto gerado.
- Demonstramos que as respostas são idênticas devido à natureza determinística da configuração de amostragem (mesma semente e temperatura).
- Usamos `seed` para especificar uma semente aleatória fixa, garantindo que o modelo gere a mesma saída para a mesma entrada sempre.
- Configuramos `temperature` para zero para garantir máximo determinismo, o que significa que o modelo sempre selecionará o token seguinte mais provável sem aleatoriedade.
- Usamos uma semente diferente para a terceira requisição para mostrar que mudar a semente resulta em saídas diferentes, mesmo com o mesmo prompt e temperatura.

---

## Configuração Dinâmica de Amostragem

A amostragem inteligente adapta parâmetros com base no contexto e requisitos de cada solicitação. Isso significa ajustar dinamicamente parâmetros como temperature, top_p e penalidades com base no tipo de tarefa, preferências do usuário ou desempenho histórico.

Vamos ver como implementar amostragem dinâmica em diferentes linguagens de programação.

# [Python](#tab/python)

```python
# Exemplo em Python: Amostragem dinâmica baseada no contexto da requisição
class DynamicSamplingService:
    def __init__(self, mcp_client):
        self.client = mcp_client
        
    async def generate_with_adaptive_sampling(self, prompt, task_type, user_preferences=None):
        """Uses different sampling strategies based on task type and user preferences"""
        
        # Definir predefinições de amostragem para diferentes tipos de tarefa
        sampling_presets = {
            "creative": {"temperature": 0.9, "top_p": 0.95, "frequency_penalty": 0.7},
            "factual": {"temperature": 0.2, "top_p": 0.85, "frequency_penalty": 0.2},
            "code": {"temperature": 0.3, "top_p": 0.9, "frequency_penalty": 0.5},
            "analytical": {"temperature": 0.4, "top_p": 0.92, "frequency_penalty": 0.3}
        }
        
        # Selecionar predefinição base
        sampling_params = sampling_presets.get(task_type, sampling_presets["factual"])
        
        # Ajustar com base nas preferências do usuário, se fornecidas
        if user_preferences:
            if "creativity_level" in user_preferences:
                # Escalar a temperatura com base na preferência de criatividade (1-10)
                creativity = min(max(user_preferences["creativity_level"], 1), 10) / 10
                sampling_params["temperature"] = 0.1 + (0.9 * creativity)
            
            if "diversity" in user_preferences:
                # Ajustar top_p com base na diversidade de resposta desejada
                diversity = min(max(user_preferences["diversity"], 1), 10) / 10
                sampling_params["top_p"] = 0.6 + (0.39 * diversity)
        
        # Criar e enviar requisição com parâmetros de amostragem personalizados
        response = await self.client.send_request(
            prompt=prompt,
            temperature=sampling_params["temperature"],
            top_p=sampling_params["top_p"],
            frequency_penalty=sampling_params["frequency_penalty"]
        )
        
        # Retornar resposta com metadados de amostragem para transparência
        return {
            "text": response.generated_text,
            "applied_sampling": sampling_params,
            "task_type": task_type
        }
```

No código precedente nós:

- Criamos uma classe `DynamicSamplingService` que gerencia a amostragem adaptativa.
- Definimos presets de amostragem para diferentes tipos de tarefa (criativa, factual, código, analítica).
- Selecionamos um preset base de amostragem baseado no tipo de tarefa.
- Ajustamos os parâmetros de amostragem com base nas preferências do usuário, como nível de criatividade e diversidade.
- Enviamos a requisição com os parâmetros de amostragem configurados dinamicamente.
- Retornamos o texto gerado junto com os parâmetros de amostragem aplicados e o tipo de tarefa para transparência.
- Usamos `temperature` para controlar a aleatoriedade da saída, onde valores mais altos levam a respostas mais criativas.
- Usamos `top_p` para limitar a seleção de tokens àqueles que contribuem para a massa cumulativa de probabilidade superior, aprimorando a qualidade do texto gerado.
- Usamos `frequency_penalty` para reduzir repetição e incentivar diversidade na saída.
- Usamos `user_preferences` para permitir personalização dos parâmetros de amostragem com base em níveis definidos pelo usuário de criatividade e diversidade.
- Usamos `task_type` para determinar a estratégia de amostragem adequada para a solicitação, permitindo respostas mais personalizadas baseadas na natureza da tarefa.
- Usamos o método `send_request` para enviar o prompt com os parâmetros de amostragem configurados, garantindo que o modelo gere texto conforme os requisitos especificados.
- Usamos `generated_text` para obter a resposta do modelo, que é então retornada junto com os parâmetros de amostragem e tipo de tarefa para análise ou exibição adicional.
- Usamos funções `min` e `max` para assegurar que as preferências do usuário estão dentro de intervalos válidos, prevenindo configurações inválidas de amostragem.

# [JavaScript Dinâmico](#tab/javascript-dynamic)

```javascript
// Exemplo em JavaScript: Configuração dinâmica de amostragem baseada no contexto do usuário
class AdaptiveSamplingManager {
  constructor(mcpClient) {
    this.client = mcpClient;
    
    // Definir perfis de amostragem base
    this.samplingProfiles = {
      creative: { temperature: 0.85, topP: 0.94, frequencyPenalty: 0.7, presencePenalty: 0.5 },
      factual: { temperature: 0.2, topP: 0.85, frequencyPenalty: 0.3, presencePenalty: 0.1 },
      code: { temperature: 0.25, topP: 0.9, frequencyPenalty: 0.4, presencePenalty: 0.3 },
      conversational: { temperature: 0.7, topP: 0.9, frequencyPenalty: 0.6, presencePenalty: 0.4 }
    };
    
    // Rastrear desempenho histórico
    this.performanceHistory = [];
  }
  
  // Detectar tipo de tarefa a partir do prompt
  detectTaskType(prompt, context = {}) {
    const promptLower = prompt.toLowerCase();
    
    // Detecção heurística simples - pode ser aprimorada com classificação por ML
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
    
    // Padrão para conversacional se nenhum tipo claro for detectado
    return 'conversational';
  }
  
  // Calcular parâmetros de amostragem com base no contexto e preferências do usuário
  getSamplingParameters(prompt, context = {}) {
    // Detectar o tipo de tarefa
    const taskType = this.detectTaskType(prompt, context);
    
    // Obter perfil base
    let params = {...this.samplingProfiles[taskType]};
    
    // Ajustar com base nas preferências do usuário
    if (context.userPreferences) {
      const { creativity, precision, consistency } = context.userPreferences;
      
      if (creativity !== undefined) {
        // Escalar de 1-10 para a faixa de temperatura apropriada
        params.temperature = 0.1 + (creativity * 0.09); // 0.1-1.0
      }
      
      if (precision !== undefined) {
        // Maior precisão significa topP menor (seleção mais focada)
        params.topP = 1.0 - (precision * 0.05); // 0.5-1.0
      }
      
      if (consistency !== undefined) {
        // Maior consistência significa penalidades menores
        params.frequencyPenalty = 0.1 + ((10 - consistency) * 0.08); // 0.1-0.9
      }
    }
    
    // Aplicar ajustes aprendidos a partir do histórico de desempenho
    this.applyLearnedAdjustments(params, taskType);
    
    return params;
  }
  
  applyLearnedAdjustments(params, taskType) {
    // Lógica adaptativa simples - pode ser aprimorada com algoritmos mais sofisticados
    const relevantHistory = this.performanceHistory
      .filter(entry => entry.taskType === taskType)
      .slice(-5); // Considerar apenas o histórico recente
    
    if (relevantHistory.length > 0) {
      // Calcular médias de pontuações de desempenho
      const avgScore = relevantHistory.reduce((sum, entry) => sum + entry.score, 0) / relevantHistory.length;
      
      // Se o desempenho estiver abaixo do limite, ajustar parâmetros
      if (avgScore < 0.7) {
        // Ajuste leve em direção a valores mais seguros
        params.temperature = Math.max(params.temperature * 0.9, 0.1);
        params.topP = Math.max(params.topP * 0.95, 0.5);
      }
    }
  }
  
  recordPerformance(prompt, samplingParams, response, score) {
    // Registrar desempenho para ajustes futuros
    this.performanceHistory.push({
      timestamp: Date.now(),
      taskType: this.detectTaskType(prompt),
      samplingParams,
      responseLength: response.generatedText.length,
      score // Avaliação de 0-1 da qualidade da resposta
    });
    
    // Limitar tamanho do histórico
    if (this.performanceHistory.length > 100) {
      this.performanceHistory.shift();
    }
  }
  
  async generateResponse(prompt, context = {}) {
    // Obter parâmetros de amostragem otimizados
    const samplingParams = this.getSamplingParameters(prompt, context);
    
    // Enviar requisição com parâmetros otimizados
    const response = await this.client.sendPrompt(prompt, {
      ...samplingParams,
      allowedTools: context.allowedTools || []
    });
    
    // Se o usuário fornecer feedback, registrá-lo para otimização futura
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

// Exemplo de uso
async function demonstrateAdaptiveSampling() {
  const client = new McpClient({
    serverUrl: 'https://mcp-server-example.com'
  });
  
  const samplingManager = new AdaptiveSamplingManager(client);
  
  try {
    // Tarefa criativa com preferências personalizadas do usuário
    const creativeResult = await samplingManager.generateResponse(
      "Write a short poem about artificial intelligence",
      {
        userPreferences: {
          creativity: 9,  // Alta criatividade (1-10)
          consistency: 3  // Baixa consistência (1-10)
        }
      }
    );
    
    console.log('Creative Task:');
    console.log(`Detected type: ${creativeResult.detectedTaskType}`);
    console.log('Applied sampling:', creativeResult.appliedSamplingParams);
    console.log(creativeResult.response.generatedText);
    
    // Tarefa de geração de código
    const codeResult = await samplingManager.generateResponse(
      "Write a JavaScript function to calculate the Fibonacci sequence",
      {
        userPreferences: {
          creativity: 2,  // Baixa criatividade
          precision: 8,   // Alta precisão
          consistency: 9  // Alta consistência
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

No código precedente nós:

- Criamos uma classe `AdaptiveSamplingManager` que gerencia amostragem dinâmica baseada no tipo de tarefa e nas preferências do usuário.
- Definimos perfis de amostragem para diferentes tipos de tarefa (criativa, factual, código, conversacional).
- Implementamos um método para detectar o tipo de tarefa a partir do prompt usando heurísticas simples.
- Calculamos parâmetros de amostragem baseados no tipo de tarefa detectado e nas preferências do usuário.
- Aplicamos ajustes aprendidos com base em desempenho histórico para otimizar os parâmetros de amostragem.
- Registramos desempenho para ajustes futuros, permitindo que o sistema aprenda com interações passadas.
- Enviamos requisições com parâmetros de amostragem configurados dinamicamente e retornamos o texto gerado junto com parâmetros aplicados e tipo de tarefa detectado.
- Usamos:
    - `userPreferences` para permitir personalização dos parâmetros de amostragem com base em níveis definidos pelo usuário de criatividade, precisão e consistência.
    - `detectTaskType` para determinar a natureza da tarefa com base no prompt, permitindo respostas mais personalizadas.
    - `recordPerformance` para registrar desempenho das respostas geradas, permitindo que o sistema se adapte e melhore ao longo do tempo.
    - `applyLearnedAdjustments` para modificar parâmetros de amostragem com base no desempenho histórico, aprimorando a capacidade do modelo de gerar respostas de alta qualidade.
    - `generateResponse` para encapsular todo o processo de geração de resposta com amostragem adaptativa, facilitando chamadas com diferentes prompts e contextos.
    - `allowedTools` para especificar quais ferramentas o modelo pode usar durante a geração, permitindo respostas mais contextualizadas.
    - `feedbackScore` para permitir que usuários forneçam feedback sobre a qualidade da resposta gerada, que pode ser usado para refinar ainda mais o desempenho do modelo com o tempo.
    - `performanceHistory` para manter um registro das interações passadas, permitindo que o sistema aprenda com sucessos e falhas anteriores.
    - `getSamplingParameters` para ajustar dinamicamente os parâmetros de amostragem com base no contexto da solicitação, permitindo um comportamento mais flexível e responsivo do modelo.
    - `detectTaskType` para classificar a tarefa baseada no prompt, permitindo que o sistema aplique estratégias de amostragem apropriadas para diferentes tipos de solicitações.
    - `samplingProfiles` para definir configurações base de amostragem para diferentes tipos de tarefas, permitindo ajustes rápidos baseados na natureza da solicitação.

---

## O que vem a seguir

- [5.7 Escalabilidade](../mcp-scaling/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido usando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, por favor, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->