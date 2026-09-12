> [!WARNING]
> A amostragem está obsoleta na MCP `2026-07-28`. Esta lição é mantida para
> implementações legadas. Novos servidores devem integrar-se diretamente com uma API
> de fornecedor de LLM.

# Amostragem no Protocolo de Contexto de Modelo

> A amostragem permanece na especificação `2026-07-28` por compatibilidade e está
> elegível para remoção na primeira revisão lançada a partir de 28 de julho de
> 2027. Os exemplos nesta lição podem usar APIs do SDK que implementam `2025-11-25`.
> Consulte [O que mudou na MCP: A especificação 2026-07-28](../../01-CoreConcepts/mcp-2026-07-28.md).

Nas implementações legadas do MCP, a amostragem permite que servidores solicitem
completions do LLM através do cliente. Esta lição explica esse fluxo de protocolo
obsoleto para compatibilidade e trabalho de migração.

## Introdução

Nesta lição, exploraremos como configurar parâmetros de amostragem em pedidos MCP e compreender a mecânica do protocolo subjacente à amostragem.

## Objetivos de Aprendizagem

No final desta lição, será capaz de:

- Compreender os principais parâmetros de amostragem disponíveis no MCP.
- Configurar parâmetros de amostragem para diferentes casos de uso.
- Implementar amostragem determinística para resultados reproduzíveis.
- Ajustar dinamicamente parâmetros de amostragem com base no contexto e preferências do utilizador.
- Aplicar estratégias de amostragem para melhorar o desempenho do modelo em vários cenários.
- Compreender como funciona a amostragem no fluxo cliente-servidor do MCP.

## Como a Amostragem Funciona no MCP

O fluxo de amostragem no MCP segue estes passos:

1. O servidor envia um pedido `sampling/createMessage` ao cliente
2. O cliente revê o pedido e pode modificá-lo
3. O cliente amostra a partir de um LLM
4. O cliente revê a conclusão
5. O cliente devolve o resultado ao servidor

Este design com intervenção humana assegura que os utilizadores mantêm controlo sobre o que o LLM vê e gera.

## Visão Geral dos Parâmetros de Amostragem

O MCP define os seguintes parâmetros de amostragem que podem ser configurados nos pedidos do cliente:

| Parâmetro | Descrição | Intervalo Típico |
|-----------|-------------|---------------|
| `temperature` | Controla a aleatoriedade na seleção de tokens | 0.0 - 1.0 |
| `maxTokens` | Número máximo de tokens a gerar | Valor inteiro |
| `stopSequences` | Sequências personalizadas que interrompem a geração quando encontradas | Array de strings |
| `metadata` | Parâmetros adicionais específicos do fornecedor | Objeto JSON |

Muitos fornecedores de LLM suportam parâmetros adicionais através do campo `metadata`, que podem incluir:

| Parâmetro Comum de Extensão | Descrição | Intervalo Típico |
|-----------|-------------|---------------|
| `top_p` | Amostragem núcleo - limita tokens à probabilidade cumulativa superior | 0.0 - 1.0 |
| `top_k` | Limita a seleção de tokens às top K opções | 1 - 100 |
| `presence_penalty` | Penaliza tokens com base na sua presença prévia no texto | -2.0 - 2.0 |
| `frequency_penalty` | Penaliza tokens com base na frequência no texto até agora | -2.0 - 2.0 |
| `seed` | Semente aleatória específica para resultados reproduzíveis | Valor inteiro |

## Exemplo de Formato de Pedido

Aqui está um exemplo de pedido de amostragem a partir de um cliente no MCP:

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

O cliente devolve um resultado de conclusão:

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

A amostragem no MCP foi desenhada para supervisão humana:

- **Para prompts**:
  - Os clientes devem mostrar aos utilizadores o prompt proposto
  - Os utilizadores devem poder modificar ou rejeitar prompts
  - Prompts do sistema podem ser filtrados ou modificados
  - A inclusão do contexto é controlada pelo cliente

- **Para conclusões**:
  - Os clientes devem mostrar aos utilizadores a conclusão
  - Os utilizadores devem poder modificar ou rejeitar conclusões
  - Os clientes podem filtrar ou modificar conclusões
  - Os utilizadores controlam qual modelo é utilizado

Com estes princípios em mente, vejamos como implementar a amostragem em diferentes linguagens de programação, focando nos parâmetros comuns suportados por fornecedores de LLM.

## Considerações de Segurança

Ao implementar a amostragem no MCP, considere estas práticas recomendadas de segurança:

- **Validar todo o conteúdo das mensagens** antes de enviar ao cliente
- **Sanitizar informação sensível** de prompts e conclusões
- **Implementar limites de taxa** para prevenir abusos
- **Monitorizar o uso da amostragem** para padrões invulgares
- **Encriptar dados em trânsito** usando protocolos seguros
- **Gerir a privacidade dos dados dos utilizadores** conforme regulamentos aplicáveis
- **Auditar pedidos de amostragem** para conformidade e segurança
- **Controlar a exposição a custos** com limites adequados
- **Implementar temporizadores** para pedidos de amostragem
- **Tratar erros do modelo com suavidade** usando estratégias adequadas

Os parâmetros de amostragem permitem ajustar finamente o comportamento dos modelos de linguagem para alcançar o equilíbrio desejado entre resultados determinísticos e criativos.

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

No código anterior nós:

- Criámos um cliente MCP com uma URL de servidor específica.
- Configurámos um pedido com parâmetros de amostragem como `temperature`, `top_p` e `top_k`.
- Enviámos o pedido e imprimimos o texto gerado.
- Usámos:
    - `allowedTools` para especificar quais ferramentas o modelo pode usar durante a geração. Neste caso, permitimos as ferramentas `ideaGenerator` e `marketAnalyzer` para ajudar a gerar ideias criativas para apps.
    - `frequencyPenalty` e `presencePenalty` para controlar a repetição e diversidade na saída.
    - `temperature` para controlar a aleatoriedade da saída, onde valores mais altos levam a respostas mais criativas.
    - `top_p` para limitar a seleção de tokens àqueles que contribuem para a massa de probabilidade cumulativa superior, melhorando a qualidade do texto gerado.
    - `top_k` para restringir o modelo aos tokens K mais prováveis, o que ajuda a gerar respostas mais coerentes.
    - `frequencyPenalty` e `presencePenalty` para reduzir a repetição e incentivar diversidade no texto gerado.

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
  
  // Configurar pedido com diferentes parâmetros de amostragem
  const creativeSampling = {
    temperature: 0.9,    // Temperatura mais alta = mais aleatoriedade/criatividade
    topP: 0.92,          // Considerar tokens com 92% de massa de probabilidade superior
    frequencyPenalty: 0.6, // Reduzir repetição de sequências de tokens
    presencePenalty: 0.4   // Penalizar tokens que já apareceram no texto até agora
  };
  
  const factualSampling = {
    temperature: 0.2,    // Temperatura mais baixa = mais determinístico/factual
    topP: 0.85,          // Seleção de tokens ligeiramente mais focada
    frequencyPenalty: 0.2, // Penalização mínima de repetição
    presencePenalty: 0.1   // Penalização mínima de presença
  };
  
  try {
    // Enviar dois pedidos com diferentes configurações de amostragem
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

No código anterior nós:

- Inicializámos um cliente MCP com uma URL do servidor e uma chave API.
- Configurámos dois conjuntos de parâmetros de amostragem: um para tarefas criativas e outro para factuais.
- Enviámos pedidos com estas configurações, permitindo que o modelo use ferramentas específicas para cada tarefa.
- Imprimimos as respostas geradas para demonstrar os efeitos dos diferentes parâmetros de amostragem.
- Usámos `allowedTools` para especificar quais ferramentas o modelo pode usar durante a geração. Neste caso, permitimos `ideaGenerator` e `environmentalImpactTool` para tarefas criativas, e `factChecker` e `dataAnalysisTool` para tarefas factuais.
- Usámos `temperature` para controlar a aleatoriedade da saída, onde valores mais altos levam a respostas mais criativas.
- Usámos `top_p` para limitar a seleção de tokens aos que contribuem para a massa top de probabilidade cumulativa, melhorando a qualidade do texto gerado.
- Usámos `frequencyPenalty` e `presencePenalty` para reduzir a repetição e incentivar diversidade na saída.
- Usámos `top_k` para restringir o modelo aos tokens K mais prováveis, o que pode ajudar a gerar respostas mais coerentes.

---

## Amostragem Determinística

Para aplicações que requerem saídas consistentes, a amostragem determinística assegura resultados reproduzíveis. Faz isso ao usar uma semente aleatória fixa e definindo a temperatura para zero.

Vejamos abaixo uma implementação de exemplo para demonstrar amostragem determinística em diferentes linguagens de programação.

# [Java](#tab/java)

```java
// Exemplo Java: Respostas determinísticas com semente fixa
public class DeterministicSamplingExample {
    public void demonstrateDeterministicResponses() {
        McpClient client = new McpClient.Builder()
            .setServerUrl("https://mcp-server-example.com")
            .build();
            
        long fixedSeed = 12345; // Utilizando uma semente fixa para resultados determinísticos
        
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

No código anterior nós:

- Criámos um cliente MCP com uma URL de servidor específica.
- Configurámos dois pedidos com o mesmo prompt, semente fixa e temperatura zero.
- Enviámos ambos os pedidos e imprimimos o texto gerado.
- Demonstrámos que as respostas são idênticas devido à natureza determinística da configuração de amostragem (mesma semente e temperatura).
- Usámos `setSeed` para especificar uma semente aleatória fixa, garantindo que o modelo gera a mesma saída para a mesma entrada sempre.
- Definimos `temperature` para zero para assegurar máximo determinismo, significando que o modelo selecionará sempre o token seguinte mais provável sem aleatoriedade.

# [JavaScript](#tab/javascript-deterministic)

```javascript
// Exemplo de JavaScript: Respostas determinísticas com controlo de semente
const { McpClient } = require('@mcp/client');

async function deterministicSampling() {
  const client = new McpClient({
    serverUrl: 'https://mcp-server-example.com'
  });
  
  const fixedSeed = 12345;
  const prompt = "Generate a random password with 8 characters";
  
  try {
    // Primeiro pedido com semente fixa
    const response1 = await client.sendPrompt(prompt, {
      seed: fixedSeed,
      temperature: 0.0  // Temperatura zero para máximo determinismo
    });
    
    // Segundo pedido com a mesma semente e temperatura
    const response2 = await client.sendPrompt(prompt, {
      seed: fixedSeed,
      temperature: 0.0
    });
    
    // Terceiro pedido com semente diferente mas mesma temperatura
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

No código anterior nós:

- Inicializámos um cliente MCP com uma URL de servidor.
- Configurámos dois pedidos com o mesmo prompt, semente fixa e temperatura zero.
- Enviámos ambos os pedidos e imprimimos o texto gerado.
- Demonstrámos que as respostas são idênticas devido à natureza determinística da configuração de amostragem (mesma semente e temperatura).
- Usámos `seed` para especificar uma semente aleatória fixa, garantindo que o modelo gera a mesma saída para a mesma entrada sempre.
- Definimos `temperature` para zero para assegurar máximo determinismo, significando que o modelo selecionará sempre o token seguinte mais provável sem aleatoriedade.
- Usámos uma semente diferente para o terceiro pedido para mostrar que mudar a semente resulta em saídas diferentes, mesmo com o mesmo prompt e temperatura.

---

## Configuração Dinâmica da Amostragem

A amostragem inteligente adapta parâmetros com base no contexto e requisitos de cada pedido. Isso significa ajustar dinamicamente parâmetros como temperature, top_p e penalizações baseando-se no tipo de tarefa, preferências do utilizador ou desempenho histórico.

Vamos ver como implementar a amostragem dinâmica em diferentes linguagens de programação.

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
        
        # Ajustar com base nas preferências do utilizador se fornecidas
        if user_preferences:
            if "creativity_level" in user_preferences:
                # Escalar a temperatura com base na preferência de criatividade (1-10)
                creativity = min(max(user_preferences["creativity_level"], 1), 10) / 10
                sampling_params["temperature"] = 0.1 + (0.9 * creativity)
            
            if "diversity" in user_preferences:
                # Ajustar top_p com base na diversidade de resposta desejada
                diversity = min(max(user_preferences["diversity"], 1), 10) / 10
                sampling_params["top_p"] = 0.6 + (0.39 * diversity)
        
        # Criar e enviar pedido com parâmetros de amostragem personalizados
        response = await self.client.send_request(
            prompt=prompt,
            temperature=sampling_params["temperature"],
            top_p=sampling_params["top_p"],
            frequency_penalty=sampling_params["frequency_penalty"]
        )
        
        # Devolver resposta com metadados de amostragem para transparência
        return {
            "text": response.generated_text,
            "applied_sampling": sampling_params,
            "task_type": task_type
        }
```

No código anterior nós:

- Criámos uma classe `DynamicSamplingService` que gere a amostragem adaptativa.
- Definimos predefinições de amostragem para diferentes tipos de tarefa (criativa, factual, código, analítica).
- Selecionámos uma predefinição base de amostragem com base no tipo de tarefa.
- Ajustámos os parâmetros de amostragem conforme as preferências do utilizador, como nível de criatividade e diversidade.
- Enviámos o pedido com os parâmetros de amostragem configurados dinamicamente.
- Devolvemos o texto gerado juntamente com os parâmetros de amostragem aplicados e o tipo de tarefa para transparência.
- Usámos `temperature` para controlar a aleatoriedade da saída, onde valores mais altos levam a respostas mais criativas.
- Usámos `top_p` para limitar a seleção de tokens aos que contribuem para a massa cumulativa superior de probabilidade, aprimorando a qualidade do texto gerado.
- Usámos `frequency_penalty` para reduzir a repetição e incentivar diversidade na saída.
- Usámos `user_preferences` para permitir a personalização dos parâmetros de amostragem com base em níveis de criatividade e diversidade definidos pelo utilizador.
- Usámos `task_type` para determinar a estratégia de amostragem adequada para o pedido, possibilitando respostas mais apropriadas à natureza da tarefa.
- Usámos o método `send_request` para enviar o prompt com os parâmetros de amostragem configurados, garantindo que o modelo gera texto conforme os requisitos especificados.
- Usámos `generated_text` para obter a resposta do modelo, que é depois devolvida junto com os parâmetros de amostragem e o tipo de tarefa para análise ou visualização adicional.
- Usámos as funções `min` e `max` para garantir que as preferências do utilizador estão limitadas a intervalos válidos, evitando configurações inválidas de amostragem.

# [JavaScript Dinâmico](#tab/javascript-dynamic)

```javascript
// Exemplo em JavaScript: configuração dinâmica de amostragem baseada no contexto do utilizador
class AdaptiveSamplingManager {
  constructor(mcpClient) {
    this.client = mcpClient;
    
    // Definir perfis base de amostragem
    this.samplingProfiles = {
      creative: { temperature: 0.85, topP: 0.94, frequencyPenalty: 0.7, presencePenalty: 0.5 },
      factual: { temperature: 0.2, topP: 0.85, frequencyPenalty: 0.3, presencePenalty: 0.1 },
      code: { temperature: 0.25, topP: 0.9, frequencyPenalty: 0.4, presencePenalty: 0.3 },
      conversational: { temperature: 0.7, topP: 0.9, frequencyPenalty: 0.6, presencePenalty: 0.4 }
    };
    
    // Registar desempenho histórico
    this.performanceHistory = [];
  }
  
  // Detectar tipo de tarefa a partir do prompt
  detectTaskType(prompt, context = {}) {
    const promptLower = prompt.toLowerCase();
    
    // Detecção heurística simples - poderia ser melhorada com classificação por ML
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
    
    // Padrão para conversacional se nenhum tipo claro for detetado
    return 'conversational';
  }
  
  // Calcular parâmetros de amostragem com base no contexto e preferências do utilizador
  getSamplingParameters(prompt, context = {}) {
    // Detetar o tipo de tarefa
    const taskType = this.detectTaskType(prompt, context);
    
    // Obter perfil base
    let params = {...this.samplingProfiles[taskType]};
    
    // Ajustar com base nas preferências do utilizador
    if (context.userPreferences) {
      const { creativity, precision, consistency } = context.userPreferences;
      
      if (creativity !== undefined) {
        // Escalar de 1-10 para o intervalo de temperatura apropriado
        params.temperature = 0.1 + (creativity * 0.09); // 0.1-1.0
      }
      
      if (precision !== undefined) {
        // Maior precisão significa topP mais baixo (seleção mais focada)
        params.topP = 1.0 - (precision * 0.05); // 0.5-1.0
      }
      
      if (consistency !== undefined) {
        // Maior consistência significa penalizações inferiores
        params.frequencyPenalty = 0.1 + ((10 - consistency) * 0.08); // 0.1-0.9
      }
    }
    
    // Aplicar ajustes aprendidos a partir do histórico de desempenho
    this.applyLearnedAdjustments(params, taskType);
    
    return params;
  }
  
  applyLearnedAdjustments(params, taskType) {
    // Lógica adaptativa simples - poderia ser melhorada com algoritmos mais sofisticados
    const relevantHistory = this.performanceHistory
      .filter(entry => entry.taskType === taskType)
      .slice(-5); // Considerar apenas o histórico recente
    
    if (relevantHistory.length > 0) {
      // Calcular médias de pontuações de desempenho
      const avgScore = relevantHistory.reduce((sum, entry) => sum + entry.score, 0) / relevantHistory.length;
      
      // Se o desempenho estiver abaixo do limite, ajustar os parâmetros
      if (avgScore < 0.7) {
        // Ajuste ligeiro para valores mais seguros
        params.temperature = Math.max(params.temperature * 0.9, 0.1);
        params.topP = Math.max(params.topP * 0.95, 0.5);
      }
    }
  }
  
  recordPerformance(prompt, samplingParams, response, score) {
    // Registar desempenho para ajustes futuros
    this.performanceHistory.push({
      timestamp: Date.now(),
      taskType: this.detectTaskType(prompt),
      samplingParams,
      responseLength: response.generatedText.length,
      score // Avaliação de 0-1 da qualidade da resposta
    });
    
    // Limitar o tamanho do histórico
    if (this.performanceHistory.length > 100) {
      this.performanceHistory.shift();
    }
  }
  
  async generateResponse(prompt, context = {}) {
    // Obter parâmetros de amostragem otimizados
    const samplingParams = this.getSamplingParameters(prompt, context);
    
    // Enviar pedido com parâmetros otimizados
    const response = await this.client.sendPrompt(prompt, {
      ...samplingParams,
      allowedTools: context.allowedTools || []
    });
    
    // Se o utilizador fornecer feedback, registar para otimização futura
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

// Exemplo de utilização
async function demonstrateAdaptiveSampling() {
  const client = new McpClient({
    serverUrl: 'https://mcp-server-example.com'
  });
  
  const samplingManager = new AdaptiveSamplingManager(client);
  
  try {
    // Tarefa criativa com preferências personalizadas do utilizador
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

No código anterior nós:

- Criámos uma classe `AdaptiveSamplingManager` que gere amostragem dinâmica baseada no tipo de tarefa e nas preferências do utilizador.
- Definimos perfis de amostragem para diferentes tipos de tarefa (criativa, factual, código, conversacional).
- Implementámos um método para detectar o tipo de tarefa a partir do prompt usando heurísticas simples.
- Calculámos parâmetros de amostragem com base no tipo de tarefa detectado e nas preferências do utilizador.
- Aplicámos ajustes aprendidos baseados no desempenho histórico para otimizar parâmetros de amostragem.
- Registámos o desempenho para ajustes futuros, permitindo que o sistema aprenda com interações passadas.
- Enviámos pedidos com parâmetros de amostragem configurados dinamicamente e devolvemos o texto gerado juntamente com os parâmetros aplicados e o tipo de tarefa detetado.
- Usámos:
    - `userPreferences` para permitir a personalização dos parâmetros de amostragem com base em níveis definidos pelo utilizador para criatividade, precisão e consistência.
    - `detectTaskType` para determinar a natureza da tarefa com base no prompt, permitindo respostas mais personalizadas.
    - `recordPerformance` para registar o desempenho das respostas geradas, permitindo que o sistema se adapte e melhore ao longo do tempo.
    - `applyLearnedAdjustments` para modificar parâmetros de amostragem com base no desempenho histórico, aprimorando a capacidade do modelo de gerar respostas de alta qualidade.
    - `generateResponse` para encapsular todo o processo de geração de uma resposta com amostragem adaptativa, facilitando o uso com diferentes prompts e contextos.
    - `allowedTools` para especificar quais ferramentas o modelo pode usar durante a geração, possibilitando respostas com maior contextualização.
    - `feedbackScore` para permitir aos utilizadores fornecer feedback sobre a qualidade da resposta gerada, que pode ser usado para refinar ainda mais o desempenho do modelo ao longo do tempo.
    - `performanceHistory` para manter um registo de interações passadas, permitindo que o sistema aprenda com sucessos e falhas anteriores.
    - `getSamplingParameters` para ajustar dinamicamente os parâmetros de amostragem com base no contexto do pedido, permitindo um comportamento do modelo mais flexível e responsivo.
    - `detectTaskType` para classificar a tarefa com base no prompt, permitindo que o sistema aplique estratégias de amostragem apropriadas para diferentes tipos de pedidos.
    - `samplingProfiles` para definir configurações base de amostragem para diferentes tipos de tarefa, permitindo ajustes rápidos conforme a natureza do pedido.

---

## O que vem a seguir

- [5.7 Escalar](../mcp-scaling/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas resultantes da utilização desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->