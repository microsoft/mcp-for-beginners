> [!WARNING]
> דגימה מייגעת בפרוטוקול MCP מ-`2026-07-28`. לקח זה נשמר עבור
> מימושים ישנים. שרתים חדשים צריכים להשתלב ישירות עם API של ספק LLM.


# דגימה בפרוטוקול הקשר דגם (Model Context Protocol)

> דגימה נשארת במפרט `2026-07-28` לניצול תאימות והיא
> מועמדת להסרה בסקירה ראשונה שתפורסם ב-או לאחר 28 ביולי,
> 2027. דוגמאות בשיעור זה עשויות להשתמש ב-SDK שמממש `2025-11-25`.
> ראה [מה השתנה ב-MCP: מפרט 2026-07-28](../../01-CoreConcepts/mcp-2026-07-28.md).

במימושים ישנים של MCP, דגימה מאפשרת לשרתים לבקש השלמות מתוך LLM
דרך הלקוח. שיעור זה מסביר את זרימת הפרוטוקול המוגבלת הזו
לטובת תאימות ועבודת מעבר.

## מבוא

בשיעור זה נחקור כיצד להגדיר פרמטרי דגימה בבקשות MCP ולהבין את המכניקה הבסיסית של הדגימה בפרוטוקול.

## מטרות הלמידה

בסוף שיעור זה תוכל:

- להבין את פרמטרי הדגימה המרכזיים הזמינים ב-MCP.
- להגדיר פרמטרי דגימה למקרים שימוש שונים.
- ליישם דגימה דטרמיניסטית לתוצאות שחוזרות על עצמן.
- לכוון דינמית פרמטרי דגימה לפי הקשר והעדפות משתמש.
- ליישם אסטרטגיות דגימה לשיפור ביצועי המודל בתרחישים שונים.
- להבין כיצד דגימה עובדת בזרימת השרת-לקוח של MCP.

## כיצד דגימה פועלת ב-MCP

זרימת הדגימה ב-MCP כוללת את השלבים הבאים:

1. השרת שולח בקשת `sampling/createMessage` ללקוח
2. הלקוח בוחן את הבקשה ויכול לשנותה
3. הלקוח מבצע דגימה מתוך LLM
4. הלקוח בוחן את ההשלמה
5. הלקוח מחזיר את התוצאה לשרת

עיצוב בלולאת אדם מבטיח שהמשתמשים שומרים שליטה על מה שה-LLM רואה ומייצר.

## סקירת פרמטרי דגימה

MCP מגדיר את פרמטרי הדגימה הבאים שניתן להגדיר בבקשות הלקוח:

| פרמטר | תיאור | טווח אופייני |
|-----------|-------------|---------------|
| `temperature` | שולט באקראיות בבחירת טוקנים | 0.0 - 1.0 |
| `maxTokens` | מספר מקסימלי של טוקנים ליצירה | ערך שלם |
| `stopSequences` | רצפים מותאמים שמפסיקים את היצירה כשהם מופיעים | מערך מחרוזות |
| `metadata` | פרמטרים נוספים לפי ספק | אובייקט JSON |

רבים מספקי LLM תומכים בפרמטרים נוספים דרך שדה `metadata`, שעשוי לכלול:

| פרמטר הרחבה נפוץ | תיאור | טווח אופייני |
|-----------|-------------|---------------|
| `top_p` | דגימת גרעין - מגביל טוקנים לסיכוי מצטבר מוביל | 0.0 - 1.0 |
| `top_k` | מגביל בחירת טוקנים לאפשרויות K מובילות | 1 - 100 |
| `presence_penalty` | מעניש טוקנים לפי הופעתם בטקסט עד כה | -2.0 - 2.0 |
| `frequency_penalty` | מעניש טוקנים לפי התדירות שלהם בטקסט עד כה | -2.0 - 2.0 |
| `seed` | זרע אקראי ספציפי לתוצאות שניתן לשחזור | ערך שלם |

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

## פיקוח אדם בלולאה

דגימה ב-MCP תוכננה עם השגחה אנושית:

- **עבור פקודות חיפוש**:
  - הלקוחות צריכים להראות למשתמשים את הפקודה המוצעת
  - משתמשים צריכים להיות מסוגלים לשנות או לדחות פקודות
  - פקודות מערכת יכולות לעבור סינון או שינוי
  - הכללת ההקשר נשלטת על ידי הלקוח

- **עבור השלמות**:
  - הלקוחות צריכים להראות למשתמשים את ההשלמה
  - משתמשים צריכים להיות מסוגלים לשנות או לדחות השלמות
  - הלקוחות יכולים לסנן או לשנות השלמות
  - המשתמשים שולטים באיזה דגם נעשה שימוש

עם עקרונות אלה, נבחן כיצד ליישם דגימה בשפות תכנות שונות, בהתמקדות בפרמטרים הנתמכים בדרך כלל על ידי ספקי LLM.

## שיקולי אבטחה

כאשר מיישמים דגימה ב-MCP, יש לשקול את פרקטיקות האבטחה הבאות:

- **ולידציה של כל תוכן ההודעה** לפני שליחתה ללקוח
- **ניקוי מידע רגיש** מהפקודות ומההשלמות
- **יישום מגבלות קצב** למניעת תקיפות
- **ניטור שימוש בדגימה** לתבניות חריגות
- **הצפנת נתונים במעבר** בעזרת פרוטוקולים מאובטחים
- **טיפול בפרטיות משתמש** בהתאם לתקנות רלוונטיות
- **ביקורת בקשות דגימה** לצורך תאימות ואבטחה
- **שליטה בעלויות** דרך הגבלות מתאימות
- **יישום גבולות זמן** לבקשות דגימה
- **טיפול שגיאות במודל בחן** עם פתרונות חלופיים מתאימים

פרמטרי דגימה מאפשרים כיוון מדויק של התנהגות דגמי השפה להשגת איזון מיטבי בין פלטים דטרמיניסטיים ליצירתיים.

בואו נבחן כיצד להגדיר פרמטרים אלה בשפות תכנות שונות.

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

בקוד הקודם אנחנו:

- יצרנו לקוח MCP עם כתובת URL ספציפית לשרת.
- הגדירו בקשה עם פרמטרי דגימה כגון `temperature`, `top_p`, ו-`top_k`.
- שלחנו את הבקשה והדפסנו את הטקסט שנוצר.
- השתמשנו ב:
    - `allowedTools` כדי לציין אילו כלים המודל יכול להשתמש בהם במהלך היצירה. במקרה זה, אפשרנו את כלים `ideaGenerator` ו-`marketAnalyzer` לסייע ביצירת רעיונות אפליקציה יצירתית.
    - `frequencyPenalty` ו-`presencePenalty` לשליטה בהכפלה ובגיוון בתוצאה.
    - `temperature` לשליטה באקראיות הפלט, כאשר ערכים גבוהים גורמים לתגובות יצירתיות יותר.
    - `top_p` להגביל את בחירת הטוקנים לאלו שתורמים להסתברויות מצטברות מובילות, לשיפור איכות הטקסט שנוצר.
    - `top_k` להגבלת המודל לטוקנים היותר סבירים מתוך K העליונים, מה שיכול לסייע ביצירת תגובות קשורות יותר.
    - `frequencyPenalty` ו-`presencePenalty` להפחתת שכפולים ולעידוד גיוון בטקסט שנוצר.

# [JavaScript](#tab/javascript)

```javascript
// דוגמת JavaScript: קביעת טמפרטורה ודגימת Top-P
const { McpClient } = require('@mcp/client');

async function demonstrateSampling() {
  // אתחול לקוח MCP
  const client = new McpClient({
    serverUrl: 'https://mcp-server-example.com',
    apiKey: process.env.MCP_API_KEY
  });
  
  // קביעת תצורת בקשה עם פרמטרי דגימה שונים
  const creativeSampling = {
    temperature: 0.9,    // טמפרטורה גבוהה יותר = עוד אקראיות/יצירתיות
    topP: 0.92,          // לשקול טוקנים עם מסה הסתברותית עליונה של 92%
    frequencyPenalty: 0.6, // להפחית חזרה של רצפי טוקנים
    presencePenalty: 0.4   // להעניש טוקנים שהופיעו בטקסט עד כה
  };
  
  const factualSampling = {
    temperature: 0.2,    // טמפרטורה נמוכה יותר = יותר דטרמיניסטי/עובדתי
    topP: 0.85,          // בחירת טוקנים ממוקדת יותר במעט
    frequencyPenalty: 0.2, // עונש חזרה מינימלי
    presencePenalty: 0.1   // עונש נוכחות מינימלי
  };
  
  try {
    // שלח שתי בקשות עם תצורות דגימה שונות
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

בקוד הקודם אנחנו:

- יצרנו לקוח MCP עם כתובת URL לשרת ומפתח API.
- הגדירו שתי קבוצות פרמטרי דגימה: אחת למשימות יצירתיות ואחת למשימות עובדתיות.
- שלחנו בקשות עם ההגדרות הללו, מאפשרים למודל להשתמש בכלים ספציפיים לכל משימה.
- הדפסנו את התגובות שנוצרו כדי להציג את ההשפעות של פרמטרי דגימה שונים.
- השתמשנו ב-`allowedTools` לציון אילו כלים המודל יכול להשתמש בהם במהלך היצירה. במקרה זה, אפשרנו את `ideaGenerator` ו-`environmentalImpactTool` למשימות יצירתיות, ו-`factChecker` ו-`dataAnalysisTool` למשימות עובדתיות.
- השתמשנו ב-`temperature` לשליטה באקראיות הפלט, כאשר ערכים גבוהים גורמים לתגובות יצירתיות יותר.
- השתמשנו ב-`top_p` להגבלת בחירת הטוקנים לאלו שתורמים להסתברויות מצטברות מובילות, לשיפור איכות הטקסט שנוצר.
- השתמשנו ב-`frequencyPenalty` ו-`presencePenalty` להפחתת שכפולים ולעידוד גיוון בפלט.
- השתמשנו ב-`top_k` להגבלת המודל לטוקנים היותר סבירים מתוך K העליונים, מה שיכול לסייע ביצירת תגובות קשורות יותר.

---

## דגימה דטרמיניסטית

ליישומים שדורשים תוצאות עקביות, דגימה דטרמיניסטית מבטיחה תוצאות שניתן לשחזור. זאת נעשה על ידי שימוש בזרע אקראי קבוע והגדרת הטמפרטורה לאפס.

בואו נבחן דוגמה ליישום דגימה דטרמיניסטית בשפות תכנות שונות.

# [Java](#tab/java)

```java
// דוגמה ב-Java: תגובות דטרמיניסטיות עם זרעים קבועים
public class DeterministicSamplingExample {
    public void demonstrateDeterministicResponses() {
        McpClient client = new McpClient.Builder()
            .setServerUrl("https://mcp-server-example.com")
            .build();
            
        long fixedSeed = 12345; // שימוש בזרע קבוע לתוצאות דטרמיניסטיות
        
        // הבקשה הראשונה עם הזרע הקבוע
        McpRequest request1 = new McpRequest.Builder()
            .setPrompt("Generate a random number between 1 and 100")
            .setSeed(fixedSeed)
            .setTemperature(0.0) // טמפרטורה אפס למקסימום דטרמיניזם
            .build();
            
        // הבקשה השנייה עם אותו הזרע
        McpRequest request2 = new McpRequest.Builder()
            .setPrompt("Generate a random number between 1 and 100")
            .setSeed(fixedSeed)
            .setTemperature(0.0)
            .build();
        
        // ביצוע שתי הבקשות
        McpResponse response1 = client.sendRequest(request1);
        McpResponse response2 = client.sendRequest(request2);
        
        // התגובות צריכות להיות זהות עקב אותו הזרע והטמפרטורה=0
        System.out.println("Response 1: " + response1.getGeneratedText());
        System.out.println("Response 2: " + response2.getGeneratedText());
        System.out.println("Are responses identical: " + 
            response1.getGeneratedText().equals(response2.getGeneratedText()));
    }
}
```

בקוד הקודם אנחנו:

- יצרנו לקוח MCP עם כתובת URL לשרת ספציפית.
- הגדירו שתי בקשות עם אותה פקודה, זרע קבוע, וטמפרטורה אפס.
- שלחנו את שתי הבקשות והדפסנו את הטקסט שנוצר.
- הראינו שהתשובות זהות בגלל האופי הדטרמיניסטי של הגדרת הדגימה (אותו זרע וטמפרטורה).
- השתמשנו ב-`setSeed` לציון זרע אקראי קבוע, להבטיח שהמודל ייצור את אותה הפלט לכל קלט פעם אחר פעם.
- הגדרנו את `temperature` לאפס להבטחת דטרמיניזם מרבי, כלומר המודל תמיד יבחר את הטוקן הסביר ביותר הבא ללא אקראיות.

# [JavaScript](#tab/javascript-deterministic)

```javascript
// דוגמת JavaScript: תגובות דטרמיניסטיות עם שליטה בזרע
const { McpClient } = require('@mcp/client');

async function deterministicSampling() {
  const client = new McpClient({
    serverUrl: 'https://mcp-server-example.com'
  });
  
  const fixedSeed = 12345;
  const prompt = "Generate a random password with 8 characters";
  
  try {
    // הבקשה הראשונה עם זרע קבוע
    const response1 = await client.sendPrompt(prompt, {
      seed: fixedSeed,
      temperature: 0.0  // טמפרטורה אפסית למקסימום דטרמיניזם
    });
    
    // הבקשה השנייה עם אותו זרע וטמפרטורה
    const response2 = await client.sendPrompt(prompt, {
      seed: fixedSeed,
      temperature: 0.0
    });
    
    // הבקשה השלישית עם זרע שונה אך אותה טמפרטורה
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

בקוד הקודם אנחנו:

- יצרנו לקוח MCP עם כתובת URL לשרת.
- הגדירו שתי בקשות עם אותה פקודה, זרע קבוע, וטמפרטורה אפס.
- שלחנו את שתי הבקשות והדפסנו את הטקסט שנוצר.
- הראינו שהתשובות זהות בגלל האופי הדטרמיניסטי של הגדרת הדגימה (אותו זרע וטמפרטורה).
- השתמשנו ב-`seed` לציון זרע אקראי קבוע, להבטיח שהמודל ייצור את אותה הפלט לכל קלט פעם אחר פעם.
- הגדרנו את `temperature` לאפס להבטחת דטרמיניזם מרבי, כלומר המודל תמיד יבחר את הטוקן הסביר ביותר הבא ללא אקראיות.
- השתמשנו בזרע שונה לבקשה השלישית כדי להראות ששינוי הזרע מביא לפלטים שונים, אפילו עם אותה פקודה וטמפרטורה.

---

## הגדרת דגימה דינמית

דגימה אינטיליגנטית מתאימה פרמטרים על פי ההקשר ודרישות כל בקשה. כלומר, התאמה דינמית של פרמטרים כמו טמפרטורה, top_p ועונשים לפי סוג המשימה, העדפות משתמש או ביצועים היסטוריים.

בואו נבחן כיצד ליישם דגימה דינמית בשפות תכנות שונות.

# [Python](#tab/python)

```python
# דוגמה בפייתון: דגימה דינמית המבוססת על הקשר הבקשה
class DynamicSamplingService:
    def __init__(self, mcp_client):
        self.client = mcp_client
        
    async def generate_with_adaptive_sampling(self, prompt, task_type, user_preferences=None):
        """Uses different sampling strategies based on task type and user preferences"""
        
        # הגדרת פריסת דגימות עבור סוגי משימות שונים
        sampling_presets = {
            "creative": {"temperature": 0.9, "top_p": 0.95, "frequency_penalty": 0.7},
            "factual": {"temperature": 0.2, "top_p": 0.85, "frequency_penalty": 0.2},
            "code": {"temperature": 0.3, "top_p": 0.9, "frequency_penalty": 0.5},
            "analytical": {"temperature": 0.4, "top_p": 0.92, "frequency_penalty": 0.3}
        }
        
        # בחירת פריסת דגימה בסיסית
        sampling_params = sampling_presets.get(task_type, sampling_presets["factual"])
        
        # התאמה בהתבסס על העדפות המשתמש אם ניתנו
        if user_preferences:
            if "creativity_level" in user_preferences:
                # שינוי טמפרטורה בהתבסס על העדפת יצירתיות (1-10)
                creativity = min(max(user_preferences["creativity_level"], 1), 10) / 10
                sampling_params["temperature"] = 0.1 + (0.9 * creativity)
            
            if "diversity" in user_preferences:
                # התאמת top_p בהתבסס על גיוון התגובה הרצוי
                diversity = min(max(user_preferences["diversity"], 1), 10) / 10
                sampling_params["top_p"] = 0.6 + (0.39 * diversity)
        
        # יצירה ושליחת בקשה עם פרמטרים מותאמים לדגימה
        response = await self.client.send_request(
            prompt=prompt,
            temperature=sampling_params["temperature"],
            top_p=sampling_params["top_p"],
            frequency_penalty=sampling_params["frequency_penalty"]
        )
        
        # החזרת תגובה עם מטא-נתוני דגימה לשקיפות
        return {
            "text": response.generated_text,
            "applied_sampling": sampling_params,
            "task_type": task_type
        }
```

בקוד הקודם אנחנו:

- יצרנו מחלקת `DynamicSamplingService` שמנהלת דגימה אדפטיבית.
- הגדרנו קונפיגורציות דגימה מוקדמות לסוגי משימות שונים (יצירתי, עובדתית, קוד, אנליטי).
- בחרנו קונפיגורציית דגימה בסיסית לפי סוג המשימה.
- כיוונו את פרמטרי הדגימה בהתאם להעדפות המשתמש כמו רמת יצירתיות וגיוון.
- שלחנו את הבקשה עם פרמטרי הדגימה המוגדרים דינמית.
- החזרנו את הטקסט שנוצר יחד עם פרמטרי הדגימה וסוג המשימה לשקיפות.
- השתמשנו ב-`temperature` לשליטה באקראיות הפלט, כאשר ערכים גבוהים גורמים לתגובות יצירתיות יותר.
- השתמשנו ב-`top_p` להגבלת בחירת הטוקנים לאלו שתורמים להסתברויות מצטברות מובילות, לשיפור איכות הטקסט שנוצר.
- השתמשנו ב-`frequency_penalty` להפחתת שכפולים ולעידוד גיוון בפלט.
- השתמשנו ב-`user_preferences` לאפשר התאמה אישית של פרמטרי הדגימה לפי רמות יצירתיות וגיוון שהוגדרו על ידי המשתמש.
- השתמשנו ב-`task_type` לקביעת אסטרטגיית דגימה מתאימה לפי סוג המשימה.
- השתמשנו בשיטה `send_request` לשליחת הפקודה עם פרמטרי הדגימה המוגדרים, להבטיח שהמודל מייצר טקסט לפי הדרישות.
- השתמשנו ב-`generated_text` לקבלת תגובת המודל, שהוחזרה יחד עם פרמטרי הדגימה וסוג המשימה לניתוח או תצוגה.
- השתמשנו ב`min` ו-`max` כדי לוודא שהעדפות המשתמש מוגבלות לטווחים תקפים, למניעת הגדרות דגימה שגויות.

# [JavaScript Dynamic](#tab/javascript-dynamic)

```javascript
// דוגמה ל-JavaScript: קביעת תצורת דגימה דינמית על פי הקשר המשתמש
class AdaptiveSamplingManager {
  constructor(mcpClient) {
    this.client = mcpClient;
    
    // הגדרת פרופילי דגימה בסיסיים
    this.samplingProfiles = {
      creative: { temperature: 0.85, topP: 0.94, frequencyPenalty: 0.7, presencePenalty: 0.5 },
      factual: { temperature: 0.2, topP: 0.85, frequencyPenalty: 0.3, presencePenalty: 0.1 },
      code: { temperature: 0.25, topP: 0.9, frequencyPenalty: 0.4, presencePenalty: 0.3 },
      conversational: { temperature: 0.7, topP: 0.9, frequencyPenalty: 0.6, presencePenalty: 0.4 }
    };
    
    // מעקב ביצועים היסטוריים
    this.performanceHistory = [];
  }
  
  // זיהוי סוג המשימה מההנחיה
  detectTaskType(prompt, context = {}) {
    const promptLower = prompt.toLowerCase();
    
    // זיהוי פשוט באמצעות היגיון חישובי - ניתן לשפר עם סיווג באמצעות למידת מכונה
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
    
    // ברירת מחדל לשיחתי במקרה שלא מזוהים סוגים ברורים
    return 'conversational';
  }
  
  // חישוב פרמטרי דגימה על פי ההקשר והעדפות המשתמש
  getSamplingParameters(prompt, context = {}) {
    // זיהוי סוג המשימה
    const taskType = this.detectTaskType(prompt, context);
    
    // קבלת הפרופיל הבסיסי
    let params = {...this.samplingProfiles[taskType]};
    
    // התאמה על פי העדפות המשתמש
    if (context.userPreferences) {
      const { creativity, precision, consistency } = context.userPreferences;
      
      if (creativity !== undefined) {
        // סקאלה מ-1 עד 10 לטווח טמפרטורה מתאים
        params.temperature = 0.1 + (creativity * 0.09); // 0.1-1.0
      }
      
      if (precision !== undefined) {
        // דיוק גבוה יותר משמעותו topP נמוך יותר (בחירה ממוקדת יותר)
        params.topP = 1.0 - (precision * 0.05); // 0.5-1.0
      }
      
      if (consistency !== undefined) {
        // עקביות גבוהה יותר משמעותה קנסות נמוכים יותר
        params.frequencyPenalty = 0.1 + ((10 - consistency) * 0.08); // 0.1-0.9
      }
    }
    
    // יישום התאמות שנלמדו מתוך היסטוריית ביצועים
    this.applyLearnedAdjustments(params, taskType);
    
    return params;
  }
  
  applyLearnedAdjustments(params, taskType) {
    // לוגיקה אדפטיבית פשוטה - ניתן לשפר עם אלגוריתמים מתקדמים יותר
    const relevantHistory = this.performanceHistory
      .filter(entry => entry.taskType === taskType)
      .slice(-5); // מתחשבים רק בהיסטוריה האחרונה
    
    if (relevantHistory.length > 0) {
      // חישוב ציוני ביצועים ממוצעים
      const avgScore = relevantHistory.reduce((sum, entry) => sum + entry.score, 0) / relevantHistory.length;
      
      // אם הביצועים נמוכים מהסף, להתאים פרמטרים
      if (avgScore < 0.7) {
        // התאמה קלה לכיוון ערכים בטוחים יותר
        params.temperature = Math.max(params.temperature * 0.9, 0.1);
        params.topP = Math.max(params.topP * 0.95, 0.5);
      }
    }
  }
  
  recordPerformance(prompt, samplingParams, response, score) {
    // הקלטת ביצועים להתאמות עתידיות
    this.performanceHistory.push({
      timestamp: Date.now(),
      taskType: this.detectTaskType(prompt),
      samplingParams,
      responseLength: response.generatedText.length,
      score // דירוג 0-1 של איכות התשובה
    });
    
    // הגבלת גודל ההיסטוריה
    if (this.performanceHistory.length > 100) {
      this.performanceHistory.shift();
    }
  }
  
  async generateResponse(prompt, context = {}) {
    // קבלת פרמטרי דגימה מותאמים
    const samplingParams = this.getSamplingParameters(prompt, context);
    
    // שליחת בקשה עם הפרמטרים המותאמים
    const response = await this.client.sendPrompt(prompt, {
      ...samplingParams,
      allowedTools: context.allowedTools || []
    });
    
    // אם המשתמש מספק משוב, להקליט אותו לאופטימיזציה עתידית
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

// דוגמת שימוש
async function demonstrateAdaptiveSampling() {
  const client = new McpClient({
    serverUrl: 'https://mcp-server-example.com'
  });
  
  const samplingManager = new AdaptiveSamplingManager(client);
  
  try {
    // משימה יצירתית עם העדפות משתמש מותאמות אישית
    const creativeResult = await samplingManager.generateResponse(
      "Write a short poem about artificial intelligence",
      {
        userPreferences: {
          creativity: 9,  // יצירתיות גבוהה (1-10)
          consistency: 3  // עקביות נמוכה (1-10)
        }
      }
    );
    
    console.log('Creative Task:');
    console.log(`Detected type: ${creativeResult.detectedTaskType}`);
    console.log('Applied sampling:', creativeResult.appliedSamplingParams);
    console.log(creativeResult.response.generatedText);
    
    // משימת יצירת קוד
    const codeResult = await samplingManager.generateResponse(
      "Write a JavaScript function to calculate the Fibonacci sequence",
      {
        userPreferences: {
          creativity: 2,  // יצירתיות נמוכה
          precision: 8,   // דיוק גבוה
          consistency: 9  // עקביות גבוהה
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

בקוד הקודם אנחנו:

- יצרנו מחלקת `AdaptiveSamplingManager` שמנהלת דגימה דינמית לפי סוג המשימה והעדפות המשתמש.
- הגדרנו פרופילי דגימה לסוגי משימות שונים (יצירתי, עובדתית, קוד, שיחתי).
- יישמנו שיטה לזיהוי סוג המשימה מתוך הפקודה לפי סימנים פשוטים.
- חישבנו פרמטרי דגימה על פי סוג המשימה שהתגלה והעדפות המשתמש.
- יישמנו כיוונים שנלמדו לפי ביצועים היסטוריים כדי לאופטימיזציה של פרמטרי הדגימה.
- תיעדנו ביצועים לשיפורים עתידיים, מאפשר למערכת ללמוד מאינטראקציות קודמות.
- שלחנו בקשות עם פרמטרי דגימה מוגדרים דינמית והחזרנו את הטקסט שנוצר יחד עם הפרמטרים ועם סוג המשימה שזוהה.
- השתמשנו ב:
    - `userPreferences` לאפשר התאמה אישית של פרמטרי הדגימה לפי רמות יצירתיות, דיוק ועקביות שהוגדרו על ידי המשתמש.
    - `detectTaskType` לקביעת אופי המשימה לפי הפקודה, לאפשר תגובות מותאמות יותר.
    - `recordPerformance` לתעד ביצועי תגובות שנוצרו, לאפשר למערכת להסתגל ולהשתפר עם הזמן.
    - `applyLearnedAdjustments` לשינוי פרמטרי הדגימה בהתבסס על ביצועים היסטוריים, לשיפור איכות התגובות.
    - `generateResponse` לאגד את תהליך יצירת תגובה עם דגימה אדפטיבית, להקל על קריאה עם פקודות והקשרים שונים.
    - `allowedTools` לציון אילו כלים המודל יכול להשתמש בהם ביצירה, לקבל תגובות מודעות להקשר טוב יותר.
    - `feedbackScore` לאפשר למשתמשים לספק משוב על איכות התגובה שנוצרה, לשימוש בשיפור ביצועי המודל בהמשך.
    - `performanceHistory` לשמירה על תיעוד של אינטראקציות קודמות, להקנות למערכת יכולת ללמוד מהצלחות וכישלונות עבר.
    - `getSamplingParameters` לכוונן פרמטרי דגימה דינמית בהתבסס על הקשר הבקשה, לאפשר התנהגות מודל גמישה ותגובתית יותר.
    - `detectTaskType` למיון המשימה לפי הפקודה, לאפשר יישום אסטרטגיות דגימה מתאימות לסוגי בקשות שונים.
    - `samplingProfiles` להגדיר קונפיגורציות דגימה בסיסיות לסוגי משימות שונים, לאפשר כיוונים מהירים בהתבסס על טבע הבקשה.

---

## מה הלאה

- [5.7 סקלאביליות](../mcp-scaling/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**כתב ויתור**:
מסמך זה תורגם באמצעות שירות תרגום אוטומטי [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון שתרגומים אוטומטיים עלולים להכיל שגיאות או אי-דיוקים. יש להחשיב את המסמך המקורי בשפתו הטבעית כמקור הסמכות. למידע קריטי מומלץ להשתמש בתרגום מקצועי על ידי מתרגם אדם. אנו לא אחראים לכל אי-הבנה או פירוש שגוי הנובע מהשימוש בתרגום זה.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->