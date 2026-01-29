# דגימה בפרוטוקול הקשר מודל (Model Context Protocol)

דגימה היא תכונה חזקה ב-MCP שמאפשרת לשרתים לבקש השלמות LLM דרך הלקוח, ומאפשרת התנהגויות סוכניות מתוחכמות תוך שמירה על אבטחה ופרטיות. תצורת הדגימה הנכונה יכולה לשפר משמעותית את איכות התגובה והביצועים. MCP מספק דרך סטנדרטית לשלוט באיך מודלים מייצרים טקסט עם פרמטרים ספציפיים שמשפיעים על אקראיות, יצירתיות וקוהרנטיות.

## מבוא

בשיעור זה נחקור כיצד להגדיר פרמטרי דגימה בבקשות MCP ונבין את המכניקה הבסיסית של פרוטוקול הדגימה.

## מטרות הלמידה

בסיום השיעור תוכלו:

- להבין את פרמטרי הדגימה המרכזיים הזמינים ב-MCP.
- להגדיר פרמטרי דגימה למקרים שונים.
- ליישם דגימה דטרמיניסטית לתוצאות שחוזרות על עצמן.
- להתאים דינמית את פרמטרי הדגימה בהתאם להקשר ולהעדפות המשתמש.
- ליישם אסטרטגיות דגימה לשיפור ביצועי המודל בתרחישים שונים.
- להבין כיצד הדגימה פועלת בזרימת לקוח-שרת ב-MCP.

## כיצד פועלת הדגימה ב-MCP

זרימת הדגימה ב-MCP עוברת את השלבים הבאים:

1. השרת שולח בקשת `sampling/createMessage` ללקוח  
2. הלקוח בוחן את הבקשה ויכול לשנותה  
3. הלקוח מבצע דגימה מ-LLM  
4. הלקוח בוחן את ההשלמה  
5. הלקוח מחזיר את התוצאה לשרת  

עיצוב זה עם אדם בלולאה מבטיח שהמשתמשים שומרים על שליטה במה שה-LLM רואה ומייצר.

## סקירת פרמטרי דגימה

MCP מגדיר את פרמטרי הדגימה הבאים שניתן להגדיר בבקשות הלקוח:

| פרמטר | תיאור | טווח טיפוסי |
|--------|--------|--------------|
| `temperature` | שולט באקראיות בבחירת הטוקנים | 0.0 - 1.0 |
| `maxTokens` | מספר מקסימלי של טוקנים ליצירה | ערך שלם |
| `stopSequences` | רצפים מותאמים שמפסיקים את היצירה כשהם מופיעים | מערך מחרוזות |
| `metadata` | פרמטרים נוספים ספציפיים לספק | אובייקט JSON |

רבים מספקי LLM תומכים בפרמטרים נוספים דרך שדה ה-`metadata`, שיכולים לכלול:

| פרמטר הרחבה נפוץ | תיאור | טווח טיפוסי |
|-------------------|--------|--------------|
| `top_p` | דגימת נוקליאוס - מגביל טוקנים לסיכוי מצטבר עליון | 0.0 - 1.0 |
| `top_k` | מגביל את בחירת הטוקנים ל-K העליונים | 1 - 100 |
| `presence_penalty` | מעניש טוקנים לפי נוכחותם בטקסט עד כה | -2.0 - 2.0 |
| `frequency_penalty` | מעניש טוקנים לפי תדירותם בטקסט עד כה | -2.0 - 2.0 |
| `seed` | זרע אקראי ספציפי לתוצאות שחוזרות על עצמן | ערך שלם |

## דוגמת פורמט בקשה

הנה דוגמה לבקשת דגימה מלקוח ב-MCP:

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

## פורמט תגובה

הלקוח מחזיר תוצאת השלמה:

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

## בקרות אדם בלולאה

דגימת MCP מעוצבת עם פיקוח אנושי:

- **עבור פרומפטים**:  
  - הלקוחות צריכים להציג למשתמשים את הפרומפט המוצע  
  - המשתמשים צריכים להיות מסוגלים לשנות או לדחות את הפרומפטים  
  - פרומפטים מערכתיים יכולים להיות מסוננים או מותאמים  
  - הכללת ההקשר נשלטת על ידי הלקוח  

- **עבור השלמות**:  
  - הלקוחות צריכים להציג למשתמשים את ההשלמה  
  - המשתמשים צריכים להיות מסוגלים לשנות או לדחות השלמות  
  - הלקוחות יכולים לסנן או לשנות השלמות  
  - המשתמשים שולט על איזה מודל משמש  

עם עקרונות אלו, נבחן כיצד ליישם דגימה בשפות תכנות שונות, תוך התמקדות בפרמטרים הנתמכים בדרך כלל על ידי ספקי LLM.

## שיקולי אבטחה

בעת יישום דגימה ב-MCP, יש לקחת בחשבון את שיטות האבטחה הטובות הבאות:

- **לאמת את כל תוכן ההודעה** לפני שליחתה ללקוח  
- **לנקות מידע רגיש** מהפרומפטים ומההשלמות  
- **ליישם הגבלות קצב** למניעת שימוש לרעה  
- **לנטר שימוש בדגימה** לזיהוי דפוסים חריגים  
- **להצפין נתונים בתעבורה** באמצעות פרוטוקולים מאובטחים  
- **לטפל בפרטיות נתוני המשתמש** בהתאם לתקנות הרלוונטיות  
- **לבצע ביקורת על בקשות דגימה** לצורך תאימות ואבטחה  
- **לשלוט בחשיפת עלויות** עם הגבלות מתאימות  
- **ליישם זמני המתנה** לבקשות דגימה  
- **לטפל בשגיאות מודל בעדינות** עם פתרונות חלופיים מתאימים  

פרמטרי הדגימה מאפשרים לכוונן את התנהגות מודלי השפה כדי להשיג את האיזון הרצוי בין פלט דטרמיניסטי ליצירתי.

בואו נבחן כיצד להגדיר פרמטרים אלו בשפות תכנות שונות.

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

בקוד שלמעלה ביצענו:

- יצירת לקוח MCP עם כתובת URL ספציפית של השרת.  
- הגדרת בקשה עם פרמטרי דגימה כמו `temperature`, `top_p` ו-`top_k`.  
- שליחת הבקשה והדפסת הטקסט שנוצר.  
- שימוש ב-`allowedTools` לציון הכלים שהמודל יכול להשתמש בהם במהלך היצירה. במקרה זה, אפשרנו את הכלים `ideaGenerator` ו-`marketAnalyzer` לסייע ביצירת רעיונות יצירתיים לאפליקציה.  
- שימוש ב-`frequencyPenalty` ו-`presencePenalty` לשליטה על חזרתיות וגיוון בפלט.  
- שימוש ב-`temperature` לשליטה באקראיות הפלט, כאשר ערכים גבוהים יותר מובילים לתגובות יצירתיות יותר.  
- שימוש ב-`top_p` להגבלת בחירת הטוקנים לאלו התורמים למסת הסיכוי המצטברת העליונה, לשיפור איכות הטקסט שנוצר.  
- שימוש ב-`top_k` להגבלת המודל לטוקנים הסבירים ביותר ב-K העליונים, מה שיכול לסייע ביצירת תגובות קוהרנטיות יותר.  
- שימוש ב-`frequencyPenalty` ו-`presencePenalty` להפחתת חזרתיות ועידוד גיוון בטקסט שנוצר.

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

בקוד שלמעלה ביצענו:

- אתחול לקוח MCP עם כתובת URL של השרת ומפתח API.  
- הגדרת שתי קבוצות פרמטרי דגימה: אחת למשימות יצירתיות ואחת למשימות עובדתיות.  
- שליחת בקשות עם ההגדרות הללו, תוך מתן אפשרות למודל להשתמש בכלים ספציפיים לכל משימה.  
- הדפסת התגובות שנוצרו להדגמת השפעות פרמטרי הדגימה השונים.  
- שימוש ב-`allowedTools` לציון הכלים שהמודל יכול להשתמש בהם במהלך היצירה. במקרה זה, אפשרנו את `ideaGenerator` ו-`environmentalImpactTool` למשימות יצירתיות, ואת `factChecker` ו-`dataAnalysisTool` למשימות עובדתיות.  
- שימוש ב-`temperature` לשליטה באקראיות הפלט, כאשר ערכים גבוהים יותר מובילים לתגובות יצירתיות יותר.  
- שימוש ב-`top_p` להגבלת בחירת הטוקנים לאלו התורמים למסת הסיכוי המצטברת העליונה, לשיפור איכות הטקסט שנוצר.  
- שימוש ב-`frequencyPenalty` ו-`presencePenalty` להפחתת חזרתיות ועידוד גיוון בפלט.  
- שימוש ב-`top_k` להגבלת המודל לטוקנים הסבירים ביותר ב-K העליונים, מה שיכול לסייע ביצירת תגובות קוהרנטיות יותר.

---

## דגימה דטרמיניסטית

ליישומים שדורשים פלט עקבי, דגימה דטרמיניסטית מבטיחה תוצאות שחוזרות על עצמן. היא עושה זאת באמצעות שימוש בזרע אקראי קבוע והגדרת הטמפרטורה לאפס.

נבחן למטה דוגמת יישום להדגמת דגימה דטרמיניסטית בשפות תכנות שונות.

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

בקוד שלמעלה ביצענו:

- יצירת לקוח MCP עם כתובת URL של שרת מוגדרת.  
- הגדרת שתי בקשות עם אותו פרומפט, זרע קבוע וטמפרטורה אפסית.  
- שליחת שתי הבקשות והדפסת הטקסט שנוצר.  
- הוכחה שהתשובות זהות בזכות טבע דטרמיניסטי של תצורת הדגימה (אותו זרע וטמפרטורה).  
- שימוש ב-`setSeed` לציון זרע אקראי קבוע, שמבטיח שהמודל יפיק את אותו פלט עבור אותו קלט בכל פעם.  
- הגדרת `temperature` לאפס כדי להבטיח דטרמיניזם מקסימלי, כלומר שהמודל תמיד יבחר את הטוקן הסביר ביותר הבא ללא אקראיות.

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

בקוד שלמעלה ביצענו:

- אתחול לקוח MCP עם כתובת URL של השרת.  
- הגדרת שתי בקשות עם אותו פרומפט, זרע קבוע וטמפרטורה אפסית.  
- שליחת שתי הבקשות והדפסת הטקסט שנוצר.  
- הוכחה שהתשובות זהות בזכות טבע דטרמיניסטי של תצורת הדגימה (אותו זרע וטמפרטורה).  
- שימוש ב-`seed` לציון זרע אקראי קבוע, שמבטיח שהמודל יפיק את אותו פלט עבור אותו קלט בכל פעם.  
- הגדרת `temperature` לאפס כדי להבטיח דטרמיניזם מקסימלי, כלומר שהמודל תמיד יבחר את הטוקן הסביר ביותר הבא ללא אקראיות.  
- שימוש בזרע שונה עבור הבקשה השלישית כדי להראות ששינוי הזרע מביא לתוצאות שונות, גם עם אותו פרומפט וטמפרטורה.

---

## תצורת דגימה דינמית

דגימה חכמה מתאימה את הפרמטרים בהתאם להקשר ולדרישות כל בקשה. כלומר, התאמת פרמטרים כמו temperature, top_p וענישות בהתאם לסוג המשימה, העדפות המשתמש או ביצועים היסטוריים.

נבחן כיצד ליישם דגימה דינמית בשפות תכנות שונות.

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

בקוד שלמעלה ביצענו:

- יצירת מחלקת `DynamicSamplingService` שמנהלת דגימה אדפטיבית.  
- הגדרת פרופילי דגימה מראש לסוגי משימות שונים (יצירתי, עובדתית, קוד, אנליטי).  
- בחירת פרופיל דגימה בסיסי בהתאם לסוג המשימה.  
- התאמת פרמטרי הדגימה בהתאם להעדפות המשתמש, כמו רמת יצירתיות וגיוון.  
- שליחת הבקשה עם פרמטרי הדגימה שהוגדרו דינמית.  
- החזרת הטקסט שנוצר יחד עם פרמטרי הדגימה וסוג המשימה לשקיפות.  
- שימוש ב-`temperature` לשליטה באקראיות הפלט, כאשר ערכים גבוהים יותר מובילים לתגובות יצירתיות יותר.  
- שימוש ב-`top_p` להגבלת בחירת הטוקנים לאלו התורמים למסת הסיכוי המצטברת העליונה, לשיפור איכות הטקסט שנוצר.  
- שימוש ב-`frequency_penalty` להפחתת חזרתיות ועידוד גיוון בפלט.  
- שימוש ב-`user_preferences` לאפשר התאמה אישית של פרמטרי הדגימה על בסיס רמות יצירתיות וגיוון שהוגדרו על ידי המשתמש.  
- שימוש ב-`task_type` לקביעת אסטרטגיית הדגימה המתאימה לבקשה, לאפשר תגובות מותאמות יותר לפי אופי המשימה.  
- שימוש בשיטת `send_request` לשליחת הפרומפט עם פרמטרי הדגימה שהוגדרו, להבטיח שהמודל יפיק טקסט בהתאם לדרישות.  
- שימוש ב-`generated_text` לקבלת תגובת המודל, שמוחזרת יחד עם פרמטרי הדגימה וסוג המשימה לניתוח או הצגה.  
- שימוש בפונקציות `min` ו-`max` להבטיח שהעדפות המשתמש יוגבלו לטווחים תקינים, למניעת תצורות דגימה לא חוקיות.

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

בקוד שלמעלה ביצענו:

- יצירת מחלקת `AdaptiveSamplingManager` שמנהלת דגימה דינמית על בסיס סוג המשימה והעדפות המשתמש.  
- הגדרת פרופילי דגימה לסוגי משימות שונים (יצירתי, עובדתית, קוד, שיחתי).  
- יישום שיטה לזיהוי סוג המשימה מהפרומפט באמצעות היריסטיקות פשוטות.  
- חישוב פרמטרי דגימה בהתבסס על סוג המשימה שזוהה והעדפות המשתמש.  
- יישום התאמות שנלמדו בהתבסס על ביצועים היסטוריים לאופטימיזציה של פרמטרי הדגימה.  
- תיעוד ביצועים להתאמות עתידיות, המאפשר למערכת ללמוד מאינטראקציות קודמות.  
- שליחת בקשות עם פרמטרי דגימה שהוגדרו דינמית והחזרת הטקסט שנוצר יחד עם הפרמטרים שהוחלו וסוג המשימה שזוהה.  
- שימוש ב-`userPreferences` לאפשר התאמה אישית של פרמטרי הדגימה על בסיס רמות יצירתיות, דיוק ועקביות שהוגדרו על ידי המשתמש.  
- שימוש ב-`detectTaskType` לקביעת אופי המשימה מהפרומפט, לאפשר תגובות מותאמות יותר.  
- שימוש ב-`recordPerformance` לתיעוד ביצועי התגובות שנוצרו, לאפשר למערכת להסתגל ולשפר עם הזמן.  
- שימוש ב-`applyLearnedAdjustments` לשינוי פרמטרי הדגימה בהתבסס על ביצועים היסטוריים, לשיפור יכולת המודל לייצר תגובות איכותיות.  
- שימוש ב-`generateResponse` לאריזת כל תהליך יצירת התגובה עם דגימה אדפטיבית, להקל על קריאה עם פרומפטים והקשרים שונים.  
- שימוש ב-`allowedTools` לציון הכלים שהמודל יכול להשתמש בהם במהלך היצירה, לאפשר תגובות מודעות להקשר.  
- שימוש ב-`feedbackScore` לאפשר למשתמשים לספק משוב על איכות התגובה שנוצרה, שניתן להשתמש בו לשיפור ביצועי המודל לאורך זמן.  
- שימוש ב-`performanceHistory` לשמירת רשומות של אינטראקציות קודמות, לאפשר למערכת ללמוד מהצלחות וכישלונות.  
- שימוש ב-`getSamplingParameters` להתאמת פרמטרי הדגימה דינמית בהתאם להקשר הבקשה, לאפשר התנהגות מודל גמישה ותגובתית יותר.  
- שימוש ב-`detectTaskType` לסיווג המשימה על בסיס הפרומפט, לאפשר יישום אסטרטגיות דגימה מתאימות לסוגי בקשות שונים.  
- שימוש ב-`samplingProfiles` להגדרת תצורות דגימה בסיסיות לסוגי משימות שונים, לאפשר התאמות מהירות בהתאם לאופי הבקשה.

---

## מה הלאה

- [5.7 Scaling](../mcp-scaling/README.md)

**כתב ויתור**:  
מסמך זה תורגם באמצעות שירות תרגום מבוסס בינה מלאכותית [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון כי תרגומים אוטומטיים עלולים להכיל שגיאות או אי-דיוקים. המסמך המקורי בשפת המקור שלו נחשב למקור הסמכותי. למידע קריטי מומלץ להשתמש בתרגום מקצועי על ידי מתרגם אנושי. אנו לא נושאים באחריות לכל אי-הבנה או פרשנות שגויה הנובעת משימוש בתרגום זה.