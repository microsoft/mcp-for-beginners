# Échantillonnage dans le protocole Model Context

L’échantillonnage est une fonctionnalité puissante de MCP qui permet aux serveurs de demander des complétions LLM via le client, favorisant des comportements agentiques sophistiqués tout en garantissant sécurité et confidentialité. Une bonne configuration de l’échantillonnage peut considérablement améliorer la qualité des réponses et les performances. MCP offre une méthode standardisée pour contrôler la génération de texte par les modèles avec des paramètres spécifiques influençant l’aléa, la créativité et la cohérence.

## Introduction

Dans cette leçon, nous allons explorer comment configurer les paramètres d’échantillonnage dans les requêtes MCP et comprendre les mécanismes sous-jacents du protocole d’échantillonnage.

## Objectifs d’apprentissage

À la fin de cette leçon, vous serez capable de :

- Comprendre les principaux paramètres d’échantillonnage disponibles dans MCP.
- Configurer les paramètres d’échantillonnage pour différents cas d’usage.
- Mettre en œuvre un échantillonnage déterministe pour des résultats reproductibles.
- Ajuster dynamiquement les paramètres d’échantillonnage selon le contexte et les préférences utilisateur.
- Appliquer des stratégies d’échantillonnage pour améliorer les performances du modèle dans divers scénarios.
- Comprendre le fonctionnement de l’échantillonnage dans le flux client-serveur de MCP.

## Fonctionnement de l’échantillonnage dans MCP

Le flux d’échantillonnage dans MCP suit ces étapes :

1. Le serveur envoie une requête `sampling/createMessage` au client  
2. Le client examine la requête et peut la modifier  
3. Le client effectue l’échantillonnage à partir d’un LLM  
4. Le client vérifie la complétion  
5. Le client renvoie le résultat au serveur  

Cette conception avec intervention humaine garantit que les utilisateurs gardent le contrôle sur ce que le LLM voit et génère.

## Vue d’ensemble des paramètres d’échantillonnage

MCP définit les paramètres d’échantillonnage suivants, configurables dans les requêtes client :

| Paramètre | Description | Plage typique |
|-----------|-------------|---------------|
| `temperature` | Contrôle l’aléa dans la sélection des tokens | 0.0 - 1.0 |
| `maxTokens` | Nombre maximal de tokens à générer | Valeur entière |
| `stopSequences` | Séquences personnalisées qui arrêtent la génération lorsqu’elles sont rencontrées | Tableau de chaînes |
| `metadata` | Paramètres supplémentaires spécifiques au fournisseur | Objet JSON |

De nombreux fournisseurs LLM supportent des paramètres additionnels via le champ `metadata`, qui peuvent inclure :

| Paramètre d’extension courant | Description | Plage typique |
|-------------------------------|-------------|---------------|
| `top_p` | Échantillonnage nucleus - limite les tokens à la probabilité cumulative maximale | 0.0 - 1.0 |
| `top_k` | Limite la sélection aux K tokens les plus probables | 1 - 100 |
| `presence_penalty` | Pénalise les tokens en fonction de leur présence dans le texte généré jusqu’à présent | -2.0 - 2.0 |
| `frequency_penalty` | Pénalise les tokens selon leur fréquence dans le texte généré jusqu’à présent | -2.0 - 2.0 |
| `seed` | Graine aléatoire spécifique pour des résultats reproductibles | Valeur entière |

## Exemple de format de requête

Voici un exemple de requête d’échantillonnage depuis un client MCP :

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

## Format de la réponse

Le client renvoie un résultat de complétion :

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

## Contrôles avec intervention humaine

L’échantillonnage MCP est conçu pour intégrer une supervision humaine :

- **Pour les prompts** :  
  - Les clients doivent afficher le prompt proposé aux utilisateurs  
  - Les utilisateurs doivent pouvoir modifier ou rejeter les prompts  
  - Les prompts système peuvent être filtrés ou modifiés  
  - L’inclusion du contexte est contrôlée par le client  

- **Pour les complétions** :  
  - Les clients doivent afficher la complétion aux utilisateurs  
  - Les utilisateurs doivent pouvoir modifier ou rejeter les complétions  
  - Les clients peuvent filtrer ou modifier les complétions  
  - Les utilisateurs contrôlent le modèle utilisé  

Avec ces principes en tête, examinons comment implémenter l’échantillonnage dans différents langages de programmation, en nous concentrant sur les paramètres couramment supportés par les fournisseurs LLM.

## Considérations de sécurité

Lors de l’implémentation de l’échantillonnage dans MCP, prenez en compte ces bonnes pratiques de sécurité :

- **Valider tout le contenu des messages** avant de l’envoyer au client  
- **Assainir les informations sensibles** des prompts et complétions  
- **Mettre en place des limites de débit** pour éviter les abus  
- **Surveiller l’utilisation de l’échantillonnage** pour détecter des comportements anormaux  
- **Chiffrer les données en transit** avec des protocoles sécurisés  
- **Gérer la confidentialité des données utilisateur** conformément aux réglementations en vigueur  
- **Auditer les requêtes d’échantillonnage** pour conformité et sécurité  
- **Contrôler les coûts** avec des limites appropriées  
- **Implémenter des délais d’attente** pour les requêtes d’échantillonnage  
- **Gérer les erreurs du modèle avec des solutions de secours adaptées**  

Les paramètres d’échantillonnage permettent d’affiner le comportement des modèles de langage pour trouver le bon équilibre entre sorties déterministes et créatives.

Voyons comment configurer ces paramètres dans différents langages de programmation.

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

Dans le code précédent, nous avons :

- Créé un client MCP avec une URL de serveur spécifique.  
- Configuré une requête avec des paramètres d’échantillonnage tels que `temperature`, `top_p` et `top_k`.  
- Envoyé la requête et affiché le texte généré.  
- Utilisé :  
    - `allowedTools` pour spécifier les outils que le modèle peut utiliser lors de la génération. Ici, nous avons autorisé les outils `ideaGenerator` et `marketAnalyzer` pour aider à générer des idées d’applications créatives.  
    - `frequencyPenalty` et `presencePenalty` pour contrôler la répétition et la diversité dans la sortie.  
    - `temperature` pour contrôler l’aléa de la sortie, où des valeurs plus élevées favorisent des réponses plus créatives.  
    - `top_p` pour limiter la sélection des tokens à ceux qui contribuent à la masse de probabilité cumulative maximale, améliorant la qualité du texte généré.  
    - `top_k` pour restreindre le modèle aux K tokens les plus probables, ce qui peut aider à générer des réponses plus cohérentes.  
    - `frequencyPenalty` et `presencePenalty` pour réduire la répétition et encourager la diversité dans le texte généré.

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

Dans le code précédent, nous avons :

- Initialisé un client MCP avec une URL de serveur et une clé API.  
- Configuré deux ensembles de paramètres d’échantillonnage : un pour les tâches créatives et un autre pour les tâches factuelles.  
- Envoyé des requêtes avec ces configurations, permettant au modèle d’utiliser des outils spécifiques pour chaque tâche.  
- Affiché les réponses générées pour démontrer les effets des différents paramètres d’échantillonnage.  
- Utilisé `allowedTools` pour spécifier les outils que le modèle peut utiliser lors de la génération. Ici, nous avons autorisé `ideaGenerator` et `environmentalImpactTool` pour les tâches créatives, et `factChecker` et `dataAnalysisTool` pour les tâches factuelles.  
- Utilisé `temperature` pour contrôler l’aléa de la sortie, où des valeurs plus élevées favorisent des réponses plus créatives.  
- Utilisé `top_p` pour limiter la sélection des tokens à ceux qui contribuent à la masse de probabilité cumulative maximale, améliorant la qualité du texte généré.  
- Utilisé `frequencyPenalty` et `presencePenalty` pour réduire la répétition et encourager la diversité dans la sortie.  
- Utilisé `top_k` pour restreindre le modèle aux K tokens les plus probables, ce qui peut aider à générer des réponses plus cohérentes.

---

## Échantillonnage déterministe

Pour les applications nécessitant des sorties constantes, l’échantillonnage déterministe garantit des résultats reproductibles. Cela se fait en utilisant une graine aléatoire fixe et en réglant la température à zéro.

Voyons ci-dessous un exemple d’implémentation pour démontrer l’échantillonnage déterministe dans différents langages de programmation.

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

Dans le code précédent, nous avons :

- Créé un client MCP avec une URL de serveur spécifiée.  
- Configuré deux requêtes avec le même prompt, une graine fixe et une température nulle.  
- Envoyé les deux requêtes et affiché le texte généré.  
- Montré que les réponses sont identiques grâce à la nature déterministe de la configuration d’échantillonnage (même graine et température).  
- Utilisé `setSeed` pour spécifier une graine aléatoire fixe, garantissant que le modèle génère la même sortie pour la même entrée à chaque fois.  
- Réglé `temperature` à zéro pour assurer un maximum de déterminisme, ce qui signifie que le modèle sélectionnera toujours le token suivant le plus probable sans aléa.

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

Dans le code précédent, nous avons :

- Initialisé un client MCP avec une URL de serveur.  
- Configuré deux requêtes avec le même prompt, une graine fixe et une température nulle.  
- Envoyé les deux requêtes et affiché le texte généré.  
- Montré que les réponses sont identiques grâce à la nature déterministe de la configuration d’échantillonnage (même graine et température).  
- Utilisé `seed` pour spécifier une graine aléatoire fixe, garantissant que le modèle génère la même sortie pour la même entrée à chaque fois.  
- Réglé `temperature` à zéro pour assurer un maximum de déterminisme, ce qui signifie que le modèle sélectionnera toujours le token suivant le plus probable sans aléa.  
- Utilisé une graine différente pour la troisième requête afin de montrer que changer la graine produit des sorties différentes, même avec le même prompt et la même température.

---

## Configuration dynamique de l’échantillonnage

L’échantillonnage intelligent adapte les paramètres en fonction du contexte et des exigences de chaque requête. Cela signifie ajuster dynamiquement des paramètres comme temperature, top_p et les pénalités selon le type de tâche, les préférences utilisateur ou les performances historiques.

Voyons comment implémenter l’échantillonnage dynamique dans différents langages de programmation.

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

Dans le code précédent, nous avons :

- Créé une classe `DynamicSamplingService` qui gère l’échantillonnage adaptatif.  
- Défini des presets d’échantillonnage pour différents types de tâches (créative, factuelle, code, analytique).  
- Sélectionné un preset d’échantillonnage de base selon le type de tâche.  
- Ajusté les paramètres d’échantillonnage en fonction des préférences utilisateur, telles que le niveau de créativité et de diversité.  
- Envoyé la requête avec les paramètres d’échantillonnage configurés dynamiquement.  
- Renvoyé le texte généré ainsi que les paramètres d’échantillonnage appliqués et le type de tâche pour plus de transparence.  
- Utilisé `temperature` pour contrôler l’aléa de la sortie, où des valeurs plus élevées favorisent des réponses plus créatives.  
- Utilisé `top_p` pour limiter la sélection des tokens à ceux qui contribuent à la masse de probabilité cumulative maximale, améliorant la qualité du texte généré.  
- Utilisé `frequency_penalty` pour réduire la répétition et encourager la diversité dans la sortie.  
- Utilisé `user_preferences` pour permettre la personnalisation des paramètres d’échantillonnage selon les niveaux de créativité et de diversité définis par l’utilisateur.  
- Utilisé `task_type` pour déterminer la stratégie d’échantillonnage appropriée à la requête, permettant des réponses plus adaptées selon la nature de la tâche.  
- Utilisé la méthode `send_request` pour envoyer le prompt avec les paramètres d’échantillonnage configurés, garantissant que le modèle génère du texte selon les exigences spécifiées.  
- Utilisé `generated_text` pour récupérer la réponse du modèle, qui est ensuite renvoyée avec les paramètres d’échantillonnage et le type de tâche pour analyse ou affichage.  
- Utilisé les fonctions `min` et `max` pour s’assurer que les préférences utilisateur restent dans des plages valides, évitant des configurations d’échantillonnage invalides.

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

Dans le code précédent, nous avons :

- Créé une classe `AdaptiveSamplingManager` qui gère l’échantillonnage dynamique selon le type de tâche et les préférences utilisateur.  
- Défini des profils d’échantillonnage pour différents types de tâches (créative, factuelle, code, conversationnelle).  
- Implémenté une méthode pour détecter le type de tâche à partir du prompt en utilisant des heuristiques simples.  
- Calculé les paramètres d’échantillonnage en fonction du type de tâche détecté et des préférences utilisateur.  
- Appliqué des ajustements appris basés sur les performances historiques pour optimiser les paramètres d’échantillonnage.  
- Enregistré les performances pour des ajustements futurs, permettant au système d’apprendre des interactions passées.  
- Envoyé des requêtes avec des paramètres d’échantillonnage configurés dynamiquement et renvoyé le texte généré avec les paramètres appliqués et le type de tâche détecté.  
- Utilisé :  
    - `userPreferences` pour permettre la personnalisation des paramètres d’échantillonnage selon les niveaux de créativité, précision et cohérence définis par l’utilisateur.  
    - `detectTaskType` pour déterminer la nature de la tâche à partir du prompt, permettant des réponses plus adaptées.  
    - `recordPerformance` pour enregistrer la performance des réponses générées, permettant au système de s’adapter et de s’améliorer avec le temps.  
    - `applyLearnedAdjustments` pour modifier les paramètres d’échantillonnage en fonction des performances historiques, améliorant la capacité du modèle à générer des réponses de haute qualité.  
    - `generateResponse` pour encapsuler l’ensemble du processus de génération d’une réponse avec échantillonnage adaptatif, facilitant l’appel avec différents prompts et contextes.  
    - `allowedTools` pour spécifier les outils que le modèle peut utiliser lors de la génération, permettant des réponses plus contextuelles.  
    - `feedbackScore` pour permettre aux utilisateurs de donner leur avis sur la qualité de la réponse générée, utilisé pour affiner davantage les performances du modèle au fil du temps.  
    - `performanceHistory` pour conserver un historique des interactions passées, permettant au système d’apprendre des succès et échecs précédents.  
    - `getSamplingParameters` pour ajuster dynamiquement les paramètres d’échantillonnage selon le contexte de la requête, offrant un comportement de modèle plus flexible et réactif.  
    - `detectTaskType` pour classifier la tâche à partir du prompt, permettant d’appliquer des stratégies d’échantillonnage adaptées aux différents types de requêtes.  
    - `samplingProfiles` pour définir des configurations d’échantillonnage de base selon les types de tâches, facilitant les ajustements rapides selon la nature de la requête.

---

## Et ensuite

- [5.7 Mise à l’échelle](../mcp-scaling/README.md)

**Avertissement** :  
Ce document a été traduit à l’aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d’assurer l’exactitude, veuillez noter que les traductions automatiques peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d’origine doit être considéré comme la source faisant foi. Pour les informations critiques, une traduction professionnelle réalisée par un humain est recommandée. Nous déclinons toute responsabilité en cas de malentendus ou de mauvaises interprétations résultant de l’utilisation de cette traduction.