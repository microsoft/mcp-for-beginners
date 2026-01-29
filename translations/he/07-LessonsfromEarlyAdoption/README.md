# 🌟 שיעורים ממאמצים מוקדמים

[![שיעורים ממאמצים מוקדמים של MCP](../../../translated_images/he/08.980bb2babbaadd8a97739effc9b31e5f1abd8f4c4a3fbc90fb9f931a866674d0.png)](https://youtu.be/jds7dSmNptE)

_(לחצו על התמונה למעלה לצפייה בסרטון של השיעור)_

## 🎯 מה מכסה המודול הזה

המודול הזה בוחן כיצד ארגונים ומפתחים אמיתיים משתמשים בפרוטוקול Model Context Protocol (MCP) כדי לפתור אתגרים אמיתיים ולהניע חדשנות. דרך מחקרי מקרה מפורטים ודוגמאות מעשיות, תגלו כיצד MCP מאפשר אינטגרציה מאובטחת ומדרגית של AI שמחברת מודלים שפתיים, כלים ונתוני ארגון.

### 📚 ראו את MCP בפעולה

רוצים לראות את העקרונות הללו מיושמים בכלים מוכנים לייצור? עיינו ב-[**10 שרתי MCP של Microsoft שמשנים את פרודוקטיביות המפתחים**](microsoft-mcp-servers.md), המציגים שרתי MCP אמיתיים של Microsoft שתוכלו להשתמש בהם כבר היום.

## סקירה כללית

השיעור הזה בוחן כיצד מאמצים מוקדמים השתמשו בפרוטוקול Model Context Protocol (MCP) כדי לפתור אתגרים אמיתיים ולהניע חדשנות בתעשיות שונות. דרך מחקרי מקרה מפורטים ופרויקטים מעשיים, תראו כיצד MCP מאפשר אינטגרציה סטנדרטית, מאובטחת ומדרגית של AI—חיבור מודלים שפתיים גדולים, כלים ונתוני ארגון במסגרת אחידה. תרכשו ניסיון מעשי בתכנון ובניית פתרונות מבוססי MCP, תלמדו מדפוסי יישום מוכחים ותגלו את השיטות הטובות ביותר לפריסת MCP בסביבות ייצור. השיעור גם מדגיש מגמות מתפתחות, כיוונים עתידיים ומשאבים בקוד פתוח שיעזרו לכם להישאר בחזית טכנולוגיית MCP והמערכת האקולוגית המתפתחת שלה.

## מטרות למידה

- לנתח יישומי MCP אמיתיים בתעשיות שונות  
- לתכנן ולבנות יישומים מלאים מבוססי MCP  
- לחקור מגמות מתפתחות וכיוונים עתידיים בטכנולוגיית MCP  
- ליישם שיטות עבודה מומלצות בתרחישי פיתוח אמיתיים  

## יישומי MCP אמיתיים

### מחקר מקרה 1: אוטומציה של תמיכת לקוחות ארגונית

תאגיד רב-לאומי יישם פתרון מבוסס MCP כדי לסטנדרט את האינטראקציות של AI במערכות תמיכת הלקוחות שלהם. זה אפשר להם:

- ליצור ממשק אחיד עבור ספקי LLM מרובים  
- לשמור על ניהול הנחיות עקבי בין מחלקות  
- ליישם בקרות אבטחה וציות חזקות  
- לעבור בקלות בין מודלים AI שונים בהתאם לצרכים ספציפיים  

**יישום טכני:**

```python
# Python MCP server implementation for customer support
import logging
import asyncio
from modelcontextprotocol import create_server, ServerConfig
from modelcontextprotocol.server import MCPServer
from modelcontextprotocol.transports import create_http_transport
from modelcontextprotocol.resources import ResourceDefinition
from modelcontextprotocol.prompts import PromptDefinition
from modelcontextprotocol.tool import ToolDefinition

# Configure logging
logging.basicConfig(level=logging.INFO)

async def main():
    # Create server configuration
    config = ServerConfig(
        name="Enterprise Customer Support Server",
        version="1.0.0",
        description="MCP server for handling customer support inquiries"
    )
    
    # Initialize MCP server
    server = create_server(config)
    
    # Register knowledge base resources
    server.resources.register(
        ResourceDefinition(
            name="customer_kb",
            description="Customer knowledge base documentation"
        ),
        lambda params: get_customer_documentation(params)
    )
    
    # Register prompt templates
    server.prompts.register(
        PromptDefinition(
            name="support_template",
            description="Templates for customer support responses"
        ),
        lambda params: get_support_templates(params)
    )
    
    # Register support tools
    server.tools.register(
        ToolDefinition(
            name="ticketing",
            description="Create and update support tickets"
        ),
        handle_ticketing_operations
    )
    
    # Start server with HTTP transport
    transport = create_http_transport(port=8080)
    await server.run(transport)

if __name__ == "__main__":
    asyncio.run(main())
```

**תוצאות:** הפחתה של 30% בעלויות מודלים, שיפור של 45% בעקביות התגובות ושיפור הציות בתפעול גלובלי.

### מחקר מקרה 2: עוזר אבחון רפואי

ספק שירותי בריאות פיתח תשתית MCP כדי לשלב מודלים רפואיים AI מתמחים תוך שמירה על הגנת נתוני מטופלים רגישים:

- מעבר חלק בין מודלים רפואיים כלליים ומתמחים  
- בקרות פרטיות מחמירות ונתיבי ביקורת  
- אינטגרציה עם מערכות רשומות רפואיות אלקטרוניות (EHR) קיימות  
- הנדסת הנחיות עקבית עבור טרמינולוגיה רפואית  

**יישום טכני:**

```csharp
// C# MCP host application implementation in healthcare application
using Microsoft.Extensions.DependencyInjection;
using ModelContextProtocol.SDK.Client;
using ModelContextProtocol.SDK.Security;
using ModelContextProtocol.SDK.Resources;

public class DiagnosticAssistant
{
    private readonly MCPHostClient _mcpClient;
    private readonly PatientContext _patientContext;
    
    public DiagnosticAssistant(PatientContext patientContext)
    {
        _patientContext = patientContext;
        
        // Configure MCP client with healthcare-specific settings
        var clientOptions = new ClientOptions
        {
            Name = "Healthcare Diagnostic Assistant",
            Version = "1.0.0",
            Security = new SecurityOptions
            {
                Encryption = EncryptionLevel.Medical,
                AuditEnabled = true
            }
        };
        
        _mcpClient = new MCPHostClientBuilder()
            .WithOptions(clientOptions)
            .WithTransport(new HttpTransport("https://healthcare-mcp.example.org"))
            .WithAuthentication(new HIPAACompliantAuthProvider())
            .Build();
    }
    
    public async Task<DiagnosticSuggestion> GetDiagnosticAssistance(
        string symptoms, string patientHistory)
    {
        // Create request with appropriate resources and tool access
        var resourceRequest = new ResourceRequest
        {
            Name = "patient_records",
            Parameters = new Dictionary<string, object>
            {
                ["patientId"] = _patientContext.PatientId,
                ["requestingProvider"] = _patientContext.ProviderId
            }
        };
        
        // Request diagnostic assistance using appropriate prompt
        var response = await _mcpClient.SendPromptRequestAsync(
            promptName: "diagnostic_assistance",
            parameters: new Dictionary<string, object>
            {
                ["symptoms"] = symptoms,
                patientHistory = patientHistory,
                relevantGuidelines = _patientContext.GetRelevantGuidelines()
            });
            
        return DiagnosticSuggestion.FromMCPResponse(response);
    }
}
```

**תוצאות:** שיפור בהצעות אבחון לרופאים תוך שמירה על תאימות מלאה ל-HIPAA והפחתה משמעותית במעברים בין מערכות.

### מחקר מקרה 3: ניתוח סיכונים בשירותים פיננסיים

מוסד פיננסי יישם MCP כדי לסטנדרט את תהליכי ניתוח הסיכונים שלהם בין מחלקות שונות:

- יצירת ממשק אחיד עבור מודלים של סיכון אשראי, גילוי הונאות וסיכון השקעות  
- יישום בקרות גישה מחמירות וגרסאות מודלים  
- הבטחת יכולת ביקורת של כל המלצות ה-AI  
- שמירה על פורמט נתונים עקבי בין מערכות מגוונות  

**יישום טכני:**

```java
// Java MCP server for financial risk assessment
import org.mcp.server.*;
import org.mcp.security.*;

public class FinancialRiskMCPServer {
    public static void main(String[] args) {
        // Create MCP server with financial compliance features
        MCPServer server = new MCPServerBuilder()
            .withModelProviders(
                new ModelProvider("risk-assessment-primary", new AzureOpenAIProvider()),
                new ModelProvider("risk-assessment-audit", new LocalLlamaProvider())
            )
            .withPromptTemplateDirectory("./compliance/templates")
            .withAccessControls(new SOCCompliantAccessControl())
            .withDataEncryption(EncryptionStandard.FINANCIAL_GRADE)
            .withVersionControl(true)
            .withAuditLogging(new DatabaseAuditLogger())
            .build();
            
        server.addRequestValidator(new FinancialDataValidator());
        server.addResponseFilter(new PII_RedactionFilter());
        
        server.start(9000);
        
        System.out.println("Financial Risk MCP Server running on port 9000");
    }
}
```

**תוצאות:** שיפור בציות רגולטורי, מחזורי פריסת מודלים מהירים ב-40% ושיפור בעקביות הערכת סיכונים בין מחלקות.

### מחקר מקרה 4: שרת MCP של Microsoft Playwright לאוטומציה בדפדפן

Microsoft פיתחה את [שרת MCP של Playwright](https://github.com/microsoft/playwright-mcp) כדי לאפשר אוטומציה מאובטחת ומסטנדרטת של דפדפנים דרך פרוטוקול Model Context Protocol. שרת זה, המוכן לייצור, מאפשר לסוכני AI ול-LLMs לתקשר עם דפדפנים בצורה מבוקרת, ניתנת לביקורת ומתרחבת—מאפשר שימושים כמו בדיקות אינטרנט אוטומטיות, חילוץ נתונים וזרימות עבודה מקצה לקצה.

> **🎯 כלי מוכן לייצור**  
> 
> מחקר מקרה זה מציג שרת MCP אמיתי שתוכלו להשתמש בו כבר היום! למדו עוד על שרת MCP של Playwright ו-9 שרתי MCP נוספים של Microsoft במדריך שלנו [**Microsoft MCP Servers Guide**](microsoft-mcp-servers.md#8--playwright-mcp-server).

**תכונות עיקריות:**
- חשיפת יכולות אוטומציה בדפדפן (ניווט, מילוי טפסים, לכידת צילומי מסך וכו') ככלי MCP  
- יישום בקרות גישה מחמירות וסביבת עבודה מבודדת למניעת פעולות לא מורשות  
- מתן יומני ביקורת מפורטים עבור כל אינטראקציות בדפדפן  
- תמיכה באינטגרציה עם Azure OpenAI וספקי LLM אחרים לאוטומציה מונעת סוכנים  
- הנעת יכולות גלישה באינטרנט של סוכן הקידוד של GitHub Copilot  

**יישום טכני:**

```typescript
// TypeScript: Registering Playwright browser automation tools in an MCP server
import { createServer, ToolDefinition } from 'modelcontextprotocol';
import { launch } from 'playwright';

const server = createServer({
  name: 'Playwright MCP Server',
  version: '1.0.0',
  description: 'MCP server for browser automation using Playwright'
});

// Register a tool for navigating to a URL and capturing a screenshot
server.tools.register(
  new ToolDefinition({
    name: 'navigate_and_screenshot',
    description: 'Navigate to a URL and capture a screenshot',
    parameters: {
      url: { type: 'string', description: 'The URL to visit' }
    }
  }),
  async ({ url }) => {
    const browser = await launch();
    const page = await browser.newPage();
    await page.goto(url);
    const screenshot = await page.screenshot();
    await browser.close();
    return { screenshot };
  }
);

// Start the MCP server
server.listen(8080);
```

**תוצאות:**

- אפשר אוטומציה מאובטחת ומתוכנתת של דפדפנים עבור סוכני AI ו-LLMs  
- הפחתת מאמץ בדיקות ידניות ושיפור כיסוי הבדיקות עבור יישומי אינטרנט  
- מתן מסגרת ניתנת לשימוש חוזר ומתרחבת לאינטגרציה של כלים מבוססי דפדפן בסביבות ארגוניות  
- הנעת יכולות גלישה באינטרנט של GitHub Copilot  

**מקורות:**

- [מאגר GitHub של שרת MCP של Playwright](https://github.com/microsoft/playwright-mcp)  
- [פתרונות AI ואוטומציה של Microsoft](https://azure.microsoft.com/en-us/products/ai-services/)  

### מחקר מקרה 5: Azure MCP – פרוטוקול Model Context ברמה ארגונית כשירות

שרת Azure MCP ([https://aka.ms/azmcp](https://aka.ms/azmcp)) הוא יישום מנוהל של Microsoft ברמה ארגונית של פרוטוקול Model Context, שנועד לספק יכולות שרת MCP מדרגיות, מאובטחות ותואמות כשרות ענן. Azure MCP מאפשר לארגונים לפרוס, לנהל ולשלב שרתי MCP במהירות עם שירותי AI, נתונים ואבטחה של Azure, תוך הפחתת עומס תפעולי והאצת אימוץ AI.

> **🎯 כלי מוכן לייצור**  
> 
> זהו שרת MCP אמיתי שתוכלו להשתמש בו כבר היום! למדו עוד על שרת MCP של Azure AI Foundry במדריך שלנו [**Microsoft MCP Servers Guide**](microsoft-mcp-servers.md).

- אירוח שרת MCP מנוהל לחלוטין עם יכולות מדרוג, ניטור ואבטחה מובנות  
- אינטגרציה טבעית עם Azure OpenAI, Azure AI Search ושירותי Azure אחרים  
- אימות והרשאה ארגוניים באמצעות Microsoft Entra ID  
- תמיכה בכלים מותאמים אישית, תבניות הנחיות ומחברי משאבים  
- תאימות לדרישות אבטחה ורגולציה ארגוניות  

**יישום טכני:**

```yaml
# Example: Azure MCP server deployment configuration (YAML)
apiVersion: mcp.microsoft.com/v1
kind: McpServer
metadata:
  name: enterprise-mcp-server
spec:
  modelProviders:
    - name: azure-openai
      type: AzureOpenAI
      endpoint: https://<your-openai-resource>.openai.azure.com/
      apiKeySecret: <your-azure-keyvault-secret>
  tools:
    - name: document_search
      type: AzureAISearch
      endpoint: https://<your-search-resource>.search.windows.net/
      apiKeySecret: <your-azure-keyvault-secret>
  authentication:
    type: EntraID
    tenantId: <your-tenant-id>
  monitoring:
    enabled: true
    logAnalyticsWorkspace: <your-log-analytics-id>
```

**תוצאות:**  
- הפחתת זמן לערך עבור פרויקטי AI ארגוניים על ידי מתן פלטפורמת שרת MCP מוכנה לשימוש ותואמת  
- פישוט אינטגרציה של LLMs, כלים ומקורות נתונים ארגוניים  
- שיפור אבטחה, יכולת תצפית ויעילות תפעולית עבור עומסי עבודה של MCP  
- שיפור איכות הקוד עם שיטות העבודה הטובות ביותר של Azure SDK ודפוסי אימות עדכניים  

**מקורות:**  
- [תיעוד Azure MCP](https://aka.ms/azmcp)  
- [מאגר GitHub של שרת MCP של Azure](https://github.com/Azure/azure-mcp)  
- [שירותי AI של Azure](https://azure.microsoft.com/en-us/products/ai-services/)  
- [מרכז MCP של Microsoft](https://mcp.azure.com)  

### מחקר מקרה 6: NLWeb

MCP (Model Context Protocol) הוא פרוטוקול מתפתח עבור צ'אטבוטים ועוזרי AI לתקשר עם כלים. כל מופע של NLWeb הוא גם שרת MCP, שתומך בשיטה מרכזית אחת, ask, המשמשת לשאול אתר שאלה בשפה טבעית. התגובה המוחזרת עושה שימוש ב-schema.org, אוצר מילים נפוץ לתיאור נתוני אינטרנט. באופן כללי, MCP הוא NLWeb כפי ש-Http הוא ל-HTML. NLWeb משלב פרוטוקולים, פורמטים של Schema.org וקוד לדוגמה כדי לעזור לאתרים ליצור במהירות נקודות קצה אלו, לטובת בני אדם דרך ממשקים שיחתיים ומכונות דרך אינטראקציה טבעית בין סוכנים.

ישנם שני רכיבים מובחנים ב-NLWeb:
- פרוטוקול, פשוט מאוד להתחלה, לתקשר עם אתר בשפה טבעית ופורמט, תוך שימוש ב-json ו-schema.org לתשובה המוחזרת. ראו את התיעוד על REST API לפרטים נוספים.  
- יישום פשוט של (1) שעושה שימוש במרכיבים קיימים, עבור אתרים שניתן להפשיטם כרשימות של פריטים (מוצרים, מתכונים, אטרקציות, ביקורות וכו'). יחד עם סט ווידג'טים של ממשק משתמש, אתרים יכולים לספק בקלות ממשקים שיחתיים לתוכן שלהם. ראו את התיעוד על Life of a chat query לפרטים נוספים על איך זה עובד.  

**מקורות:**  
- [תיעוד Azure MCP](https://aka.ms/azmcp)  
- [NLWeb](https://github.com/microsoft/NlWeb)  

### מחקר מקרה 7: שרת MCP של Azure AI Foundry – אינטגרציה של סוכני AI ארגוניים

שרתי MCP של Azure AI Foundry מדגימים כיצד ניתן להשתמש ב-MCP כדי לתזמר ולנהל סוכני AI וזרימות עבודה בסביבות ארגוניות. על ידי שילוב MCP עם Azure AI Foundry, ארגונים יכולים לסטנדרט אינטראקציות סוכנים, לנצל את ניהול זרימות העבודה של Foundry ולהבטיח פריסות מאובטחות ומדרגיות.

> **🎯 כלי מוכן לייצור**  
> 
> זהו שרת MCP אמיתי שתוכלו להשתמש בו כבר היום! למדו עוד על שרת MCP של Azure AI Foundry במדריך שלנו [**Microsoft MCP Servers Guide**](microsoft-mcp-servers.md#9--azure-ai-foundry-mcp-server).

**תכונות עיקריות:**
- גישה מקיפה למערכת האקולוגית של AI של Azure, כולל קטלוגים של מודלים וניהול פריסות  
- אינדוקס ידע עם Azure AI Search עבור יישומי RAG  
- כלי הערכה לביצועי מודלים AI ואבטחת איכות  
- אינטגרציה עם קטלוג ומעבדות Azure AI Foundry עבור מודלים מחקריים מתקדמים  
- יכולות ניהול והערכה של סוכנים עבור תרחישי ייצור  

**תוצאות:**
- יצירת אב-טיפוס מהירה וניטור חזק של זרימות עבודה של סוכני AI  
- אינטגרציה חלקה עם שירותי AI של Azure עבור תרחישים מתקדמים  
- ממשק אחיד לבנייה, פריסה וניטור של צינורות סוכנים  
- שיפור אבטחה, תאימות ויעילות תפעולית עבור ארגונים  
- האצת אימוץ AI תוך שמירה על שליטה בתהליכים מורכבים מונעי סוכנים  

**מקורות:**
- [מאגר GitHub של שרת MCP של Azure AI Foundry](https://github.com/azure-ai-foundry/mcp-foundry)  
- [שילוב סוכני AI של Azure עם MCP (בלוג Microsoft Foundry)](https://devblogs.microsoft.com/foundry/integrating-azure-ai-agents-mcp/)  

### מחקר מקרה 8: Foundry MCP Playground – ניסויים ויצירת אב-טיפוס

Foundry MCP Playground מציע סביבה מוכנה לשימוש לניסויים עם שרתי MCP ואינטגרציות של Azure AI Foundry. מפתחים יכולים ליצור אב-טיפוס, לבדוק ולהעריך מודלים AI וזרימות עבודה של סוכנים במהירות תוך שימוש במשאבים מקטלוג ומעבדות Azure AI Foundry. ה-Playground מפשט את ההגדרה, מספק פרויקטים לדוגמה ותומך בפיתוח שיתופי, מה שמקל על חקר שיטות עבודה מומלצות ותרחישים חדשים עם מינימום עומס. הוא שימושי במיוחד לצוותים המעוניינים לאמת רעיונות, לשתף ניסויים ולהאיץ למידה ללא צורך בתשתית מורכבת. על ידי הורדת חסמי הכניסה, ה-Playground מסייע לטפח חדשנות ותרומות קהילתיות במערכת האקולוגית של MCP ו-Azure AI Foundry.

**מקורות:**

- [מאגר GitHub של Foundry MCP Playground](https://github.com/azure-ai-foundry/foundry-mcp-playground)  

### מחקר מקרה 9: שרת MCP של Microsoft Learn Docs – גישה לתיעוד מונעת AI

שרת MCP של Microsoft Learn Docs הוא שירות מבוסס ענן המספק לעוזרי AI גישה בזמן אמת לתיעוד הרשמי של Microsoft דרך פרוטוקול Model Context. שרת זה, המוכן לייצור, מתחבר למערכת האקולוגית המקיפה של Microsoft Learn ומאפשר חיפוש סמנטי בכל המקורות הרשמיים של Microsoft.  
> **🎯 כלי מוכן לייצור**
> 
> זהו שרת MCP אמיתי שתוכלו להשתמש בו כבר היום! למדו עוד על שרת ה-MCP של Microsoft Learn Docs במדריך שלנו [**Microsoft MCP Servers Guide**](microsoft-mcp-servers.md#1--microsoft-learn-docs-mcp-server).
**תכונות מרכזיות:**
- גישה בזמן אמת לתיעוד הרשמי של Microsoft, תיעוד Azure ותיעוד Microsoft 365
- יכולות חיפוש סמנטי מתקדמות שמבינות הקשר וכוונה
- מידע תמיד מעודכן עם פרסום תוכן Microsoft Learn
- כיסוי מקיף על פני Microsoft Learn, תיעוד Azure ומקורות Microsoft 365
- החזרת עד 10 מקטעי תוכן איכותיים עם כותרות מאמרים וקישורים

**למה זה קריטי:**
- פותר את בעיית "ידע AI מיושן" עבור טכנולוגיות Microsoft
- מבטיח שלעוזרי AI תהיה גישה לתכונות העדכניות ביותר של .NET, C#, Azure ו-Microsoft 365
- מספק מידע סמכותי ומקורי ליצירת קוד מדויק
- חיוני למפתחים שעובדים עם טכנולוגיות Microsoft שמתפתחות במהירות

**תוצאות:**
- שיפור משמעותי בדיוק של קוד שנוצר על ידי AI עבור טכנולוגיות Microsoft
- הפחתת זמן חיפוש אחר תיעוד עדכני ופרקטיקות מומלצות
- שיפור פרודוקטיביות המפתחים עם שליפה של תיעוד מודע להקשר
- אינטגרציה חלקה עם זרימות עבודה של פיתוח מבלי לצאת מה-IDE

**מקורות:**
- [מאגר GitHub של Microsoft Learn Docs MCP Server](https://github.com/MicrosoftDocs/mcp)
- [תיעוד Microsoft Learn](https://learn.microsoft.com/)

## פרויקטים מעשיים

### פרויקט 1: בניית שרת MCP רב-ספקים

**מטרה:** ליצור שרת MCP שיכול לנתב בקשות למספר ספקי מודלים AI על בסיס קריטריונים ספציפיים.

**דרישות:**

- תמיכה בלפחות שלושה ספקי מודלים שונים (לדוגמה, OpenAI, Anthropic, מודלים מקומיים)
- יישום מנגנון ניתוב המבוסס על מטא-נתונים של בקשות
- יצירת מערכת תצורה לניהול אישורי ספקים
- הוספת מנגנון מטמון לשיפור ביצועים ועלויות
- בניית לוח מחוונים פשוט לניטור שימוש

**שלבי יישום:**

1. הקמת תשתית בסיסית לשרת MCP
2. יישום מתאמים לספקי שירותי מודלים AI
3. יצירת לוגיקת ניתוב המבוססת על מאפייני בקשות
4. הוספת מנגנוני מטמון לבקשות תכופות
5. פיתוח לוח מחוונים לניטור
6. בדיקה עם דפוסי בקשות שונים

**טכנולוגיות:** בחירה בין Python (.NET/Java/Python לפי העדפתך), Redis למטמון, ומסגרת אינטרנט פשוטה ללוח המחוונים.

### פרויקט 2: מערכת ניהול הנחיות ארגונית

**מטרה:** פיתוח מערכת מבוססת MCP לניהול, גרסאות ופריסת תבניות הנחיות ברחבי הארגון.

**דרישות:**

- יצירת מאגר מרכזי לתבניות הנחיות
- יישום גרסאות ותהליכי אישור
- בניית יכולות בדיקת תבניות עם קלט לדוגמה
- פיתוח בקרות גישה מבוססות תפקידים
- יצירת API לשליפת תבניות ופריסתן

**שלבי יישום:**

1. עיצוב סכמת בסיס נתונים לאחסון תבניות
2. יצירת API מרכזי לפעולות CRUD על תבניות
3. יישום מערכת גרסאות
4. בניית תהליך אישור
5. פיתוח מסגרת בדיקה
6. יצירת ממשק אינטרנט פשוט לניהול
7. אינטגרציה עם שרת MCP

**טכנולוגיות:** בחירת מסגרת צד שרת, בסיס נתונים SQL או NoSQL, ומסגרת צד לקוח לממשק הניהול.

### פרויקט 3: פלטפורמת יצירת תוכן מבוססת MCP

**מטרה:** בניית פלטפורמת יצירת תוכן שמנצלת MCP כדי לספק תוצאות עקביות על פני סוגי תוכן שונים.

**דרישות:**

- תמיכה בפורמטים תוכן שונים (פוסטים בבלוג, מדיה חברתית, טקסט שיווקי)
- יישום יצירה מבוססת תבניות עם אפשרויות התאמה אישית
- יצירת מערכת סקירת תוכן ומשוב
- מעקב אחר מדדי ביצוע תוכן
- תמיכה בגרסאות תוכן ואיטרציות

**שלבי יישום:**

1. הקמת תשתית לקוח MCP
2. יצירת תבניות לסוגי תוכן שונים
3. בניית צינור יצירת תוכן
4. יישום מערכת סקירה
5. פיתוח מערכת מעקב מדדים
6. יצירת ממשק משתמש לניהול תבניות ויצירת תוכן

**טכנולוגיות:** שפת תכנות מועדפת, מסגרת אינטרנט, ומערכת בסיס נתונים.

## כיוונים עתידיים לטכנולוגיית MCP

### מגמות מתפתחות

1. **MCP רב-מודלי**
   - הרחבת MCP לסטנדרטיזציה של אינטראקציות עם מודלים של תמונה, אודיו ווידאו
   - פיתוח יכולות הסקת מסקנות בין-מודליות
   - פורמטים הנחיות סטנדרטיים למודלים שונים

2. **תשתית MCP מבוזרת**
   - רשתות MCP מבוזרות שיכולות לשתף משאבים בין ארגונים
   - פרוטוקולים סטנדרטיים לשיתוף מודלים מאובטח
   - טכניקות חישוב משמרות פרטיות

3. **שוקי MCP**
   - אקוסיסטמות לשיתוף ומונטיזציה של תבניות ותוספים MCP
   - תהליכי הבטחת איכות והסמכה
   - אינטגרציה עם שוקי מודלים

4. **MCP למחשוב קצה**
   - התאמת סטנדרטים של MCP למכשירי קצה עם משאבים מוגבלים
   - פרוטוקולים מותאמים לסביבות בעלות רוחב פס נמוך
   - יישומי MCP מיוחדים לאקוסיסטמות IoT

5. **מסגרות רגולטוריות**
   - פיתוח הרחבות MCP לציות רגולטורי
   - מסלולי ביקורת סטנדרטיים וממשקי הסבר
   - אינטגרציה עם מסגרות ממשל AI מתפתחות

### פתרונות MCP מ-Microsoft

Microsoft ו-Azure פיתחו מספר מאגרי קוד פתוח כדי לעזור למפתחים ליישם MCP בתרחישים שונים:

#### ארגון Microsoft

1. [playwright-mcp](https://github.com/microsoft/playwright-mcp) - שרת MCP Playwright לאוטומציה ובדיקות דפדפן
2. [files-mcp-server](https://github.com/microsoft/files-mcp-server) - יישום שרת MCP OneDrive לבדיקות מקומיות ותרומות קהילתיות
3. [NLWeb](https://github.com/microsoft/NlWeb) - אוסף פרוטוקולים פתוחים וכלים פתוחים נלווים. מתמקד ביצירת שכבה בסיסית ל-AI Web

#### ארגון Azure-Samples

1. [mcp](https://github.com/Azure-Samples/mcp) - קישורים לדוגמאות, כלים ומשאבים לבניית שרתי MCP ואינטגרציה שלהם ב-Azure
2. [mcp-auth-servers](https://github.com/Azure-Samples/mcp-auth-servers) - שרתי MCP לדוגמה המדגימים אימות עם מפרט Model Context Protocol הנוכחי
3. [remote-mcp-functions](https://github.com/Azure-Samples/remote-mcp-functions) - דף נחיתה ליישומי שרת MCP מרוחקים ב-Azure Functions עם קישורים למאגרי שפות ספציפיות
4. [remote-mcp-functions-python](https://github.com/Azure-Samples/remote-mcp-functions-python) - תבנית התחלה מהירה לבניית שרתי MCP מותאמים אישית ב-Azure Functions עם Python
5. [remote-mcp-functions-dotnet](https://github.com/Azure-Samples/remote-mcp-functions-dotnet) - תבנית התחלה מהירה לבניית שרתי MCP מותאמים אישית ב-Azure Functions עם .NET/C#
6. [remote-mcp-functions-typescript](https://github.com/Azure-Samples/remote-mcp-functions-typescript) - תבנית התחלה מהירה לבניית שרתי MCP מותאמים אישית ב-Azure Functions עם TypeScript
7. [remote-mcp-apim-functions-python](https://github.com/Azure-Samples/remote-mcp-apim-functions-python) - ניהול API של Azure כשער AI לשרתי MCP מרוחקים באמצעות Python
8. [AI-Gateway](https://github.com/Azure-Samples/AI-Gateway) - ניסויים APIM ❤️ AI כולל יכולות MCP, אינטגרציה עם Azure OpenAI ו-AI Foundry

מאגרי קוד אלו מספקים יישומים שונים, תבניות ומשאבים לעבודה עם Model Context Protocol על פני שפות תכנות ושירותי Azure שונים. הם מכסים מגוון שימושים, החל מיישומי שרת בסיסיים ועד אימות, פריסה בענן ואינטגרציה ארגונית.

#### ספריית משאבי MCP

ספריית [משאבי MCP](https://github.com/microsoft/mcp/tree/main/Resources) במאגר הרשמי של Microsoft MCP מספקת אוסף אוצר של משאבים לדוגמה, תבניות הנחיות והגדרות כלים לשימוש עם שרתי Model Context Protocol. ספרייה זו נועדה לעזור למפתחים להתחיל במהירות עם MCP על ידי הצעת אבני בניין לשימוש חוזר ודוגמאות לפרקטיקות מומלצות עבור:

- **תבניות הנחיות:** תבניות הנחיות מוכנות לשימוש למשימות ותסריטים AI נפוצים, שניתן להתאים ליישומי שרת MCP משלך.
- **הגדרות כלים:** סכמות כלים לדוגמה ומטא-נתונים לסטנדרטיזציה של אינטגרציה והפעלה של כלים על פני שרתי MCP שונים.
- **דוגמאות משאבים:** הגדרות משאבים לדוגמה לחיבור למקורות נתונים, APIs ושירותים חיצוניים במסגרת MCP.
- **יישומים לדוגמה:** דוגמאות מעשיות שמדגימות כיצד לבנות ולארגן משאבים, הנחיות וכלים בפרויקטי MCP בעולם האמיתי.

משאבים אלו מאיצים פיתוח, מקדמים סטנדרטיזציה ועוזרים להבטיח פרקטיקות מומלצות בעת בנייה ופריסה של פתרונות מבוססי MCP.

#### ספריית משאבי MCP

- [משאבי MCP (תבניות הנחיות, כלים והגדרות משאבים לדוגמה)](https://github.com/microsoft/mcp/tree/main/Resources)

### הזדמנויות מחקר

- טכניקות אופטימיזציה יעילות להנחיות במסגרת MCP
- מודלים אבטחתיים לפריסות MCP מרובות דיירים
- מדדי ביצועים על פני יישומי MCP שונים
- שיטות אימות פורמליות לשרתי MCP

## סיכום

פרוטוקול Model Context Protocol (MCP) מעצב במהירות את עתיד האינטגרציה הסטנדרטית, המאובטחת והאינטרופרטיבית של AI בתעשיות שונות. דרך מחקרי המקרה והפרויקטים המעשיים בשיעור זה, ראיתם כיצד מאמצים מוקדמים—כולל Microsoft ו-Azure—מנצלים את MCP כדי לפתור אתגרים בעולם האמיתי, להאיץ את אימוץ AI ולהבטיח תאימות, אבטחה ויכולת הרחבה. הגישה המודולרית של MCP מאפשרת לארגונים לחבר מודלים שפתיים גדולים, כלים ונתוני ארגון במסגרת מאוחדת וניתנת לביקורת. ככל ש-MCP ממשיך להתפתח, מעורבות בקהילה, חקר משאבים פתוחים ויישום פרקטיקות מומלצות יהיו המפתח לבניית פתרונות AI חזקים ומוכנים לעתיד.

## משאבים נוספים

- [מאגר GitHub של MCP Foundry](https://github.com/azure-ai-foundry/mcp-foundry)
- [מגרש משחקים MCP Foundry](https://github.com/azure-ai-foundry/foundry-mcp-playground)
- [אינטגרציה של סוכני Azure AI עם MCP (בלוג Microsoft Foundry)](https://devblogs.microsoft.com/foundry/integrating-azure-ai-agents-mcp/)
- [מאגר GitHub של MCP (Microsoft)](https://github.com/microsoft/mcp)
- [ספריית משאבי MCP (תבניות הנחיות, כלים והגדרות משאבים לדוגמה)](https://github.com/microsoft/mcp/tree/main/Resources)
- [קהילת MCP ותיעוד](https://modelcontextprotocol.io/introduction)
- [תיעוד MCP של Azure](https://aka.ms/azmcp)
- [מאגר GitHub של שרת MCP Playwright](https://github.com/microsoft/playwright-mcp)
- [שרת MCP Files (OneDrive)](https://github.com/microsoft/files-mcp-server)
- [Azure-Samples MCP](https://github.com/Azure-Samples/mcp)
- [שרתים לאימות MCP (Azure-Samples)](https://github.com/Azure-Samples/mcp-auth-servers)
- [פונקציות MCP מרוחקות (Azure-Samples)](https://github.com/Azure-Samples/remote-mcp-functions)
- [פונקציות MCP מרוחקות Python (Azure-Samples)](https://github.com/Azure-Samples/remote-mcp-functions-python)
- [פונקציות MCP מרוחקות .NET (Azure-Samples)](https://github.com/Azure-Samples/remote-mcp-functions-dotnet)
- [פונקציות MCP מרוחקות TypeScript (Azure-Samples)](https://github.com/Azure-Samples/remote-mcp-functions-typescript)
- [פונקציות MCP מרוחקות APIM Python (Azure-Samples)](https://github.com/Azure-Samples/remote-mcp-apim-functions-python)
- [AI-Gateway (Azure-Samples)](https://github.com/Azure-Samples/AI-Gateway)
- [פתרונות AI ואוטומציה של Microsoft](https://azure.microsoft.com/en-us/products/ai-services/)

## תרגילים

1. נתחו אחד ממחקרי המקרה והציעו גישה יישומית חלופית.
2. בחרו אחד מרעיונות הפרויקטים וצרו מפרט טכני מפורט.
3. חקרו תעשייה שלא כוסתה במחקרי המקרה ופרטו כיצד MCP יכול להתמודד עם האתגרים הספציפיים שלה.
4. חקרו אחד מהכיוונים העתידיים וצרו רעיון להרחבת MCP חדשה שתתמוך בו.

הבא: [שרת MCP של Microsoft](../07-LessonsfromEarlyAdoption/microsoft-mcp-servers.md)

**כתב ויתור**:  
מסמך זה תורגם באמצעות שירות תרגום מבוסס בינה מלאכותית [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש להיות מודעים לכך שתרגומים אוטומטיים עשויים להכיל שגיאות או אי דיוקים. המסמך המקורי בשפתו המקורית צריך להיחשב כמקור סמכותי. עבור מידע קריטי, מומלץ להשתמש בתרגום מקצועי על ידי אדם. איננו נושאים באחריות לאי הבנות או לפרשנויות שגויות הנובעות משימוש בתרגום זה.