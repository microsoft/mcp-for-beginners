<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "344a126b620ff7997158542fd31be6a4",
  "translation_date": "2025-05-19T18:34:20+00:00",
  "source_file": "07-LessonsfromEarlyAdoption/README.md",
  "language_code": "he"
}
-->
# לקחים מאימוץ מוקדם

## סקירה כללית

השיעור הזה חוקר כיצד מאמצים מוקדמים ניצלו את Model Context Protocol (MCP) כדי לפתור אתגרים בעולם האמיתי ולקדם חדשנות בתעשיות שונות. באמצעות מחקרי מקרה מפורטים ופרויקטים מעשיים, תראו כיצד MCP מאפשר אינטגרציה סטנדרטית, מאובטחת וניתנת להרחבה של בינה מלאכותית—מחבר בין מודלים לשוניים גדולים, כלים ונתוני ארגונים במסגרת אחידה. תרכשו ניסיון מעשי בעיצוב ובניית פתרונות מבוססי MCP, תלמדו מדפוסי יישום מוכחים ותגלו שיטות עבודה מומלצות לפריסה בסביבות ייצור. השיעור גם מדגיש מגמות מתפתחות, כיוונים עתידיים ומשאבים בקוד פתוח שיעזרו לכם להישאר בחזית הטכנולוגיה והאקוסיסטם המתפתח של MCP.

## מטרות הלמידה

- לנתח יישומים אמיתיים של MCP בתעשיות שונות  
- לעצב ולבנות אפליקציות שלמות מבוססות MCP  
- לחקור מגמות מתפתחות וכיוונים עתידיים בטכנולוגיית MCP  
- ליישם שיטות עבודה מומלצות בתרחישי פיתוח אמיתיים  

## יישומים אמיתיים של MCP

### מחקר מקרה 1: אוטומציה בתמיכת לקוחות בארגונים

תאגיד רב-לאומי יישם פתרון מבוסס MCP כדי לאחד את האינטראקציות עם בינה מלאכותית במערכות התמיכה בלקוחות שלו. זה איפשר להם:

- ליצור ממשק אחיד לספקים שונים של LLM  
- לשמור על ניהול עקבי של הפקודות בין המחלקות  
- ליישם בקרות אבטחה וציות חזקים  
- לעבור בקלות בין מודלים שונים של AI בהתאם לצרכים ספציפיים  

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

**תוצאות:** הפחתה של 30% בעלויות המודלים, שיפור של 45% בעקביות התגובות, והגברת הציות בתפעול הגלובלי.

### מחקר מקרה 2: עוזר אבחון בתחום הבריאות

ספק שירותי בריאות פיתח תשתית MCP לשילוב מספר מודלים רפואיים מומחים תוך שמירה על הגנת נתוני מטופלים רגישים:

- מעבר חלק בין מודלים רפואיים כלליים למומחים  
- בקרות פרטיות מחמירות ומסלולי ביקורת  
- אינטגרציה עם מערכות רשומות רפואיות אלקטרוניות (EHR) קיימות  
- הנדסת פקודות עקבית למונחים רפואיים  

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

**תוצאות:** שיפורים בהצעות האבחון לרופאים תוך שמירה מלאה על ציות ל-HIPAA והפחתה משמעותית במעברי הקשר בין מערכות.

### מחקר מקרה 3: ניתוח סיכונים בשירותים פיננסיים

מוסד פיננסי יישם MCP כדי לאחד את תהליכי ניתוח הסיכונים במחלקות שונות:

- יצירת ממשק אחיד למודלים של סיכון אשראי, זיהוי הונאות וסיכון השקעות  
- יישום בקרות גישה מחמירות וניהול גרסאות מודלים  
- הבטחת יכולת ביקורת של כל ההמלצות מבוססות AI  
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

**תוצאות:** שיפור בציות לרגולציה, מחזורי פריסה מהירים ב-40%, ושיפור בעקביות הערכת הסיכונים במחלקות.

### מחקר מקרה 4: שרת Playwright MCP של Microsoft לאוטומציה בדפדפן

מיקרוסופט פיתחה את [Playwright MCP server](https://github.com/microsoft/playwright-mcp) כדי לאפשר אוטומציה מאובטחת וסטנדרטית של דפדפנים באמצעות Model Context Protocol. הפתרון מאפשר לסוכני AI ול-LLM אינטראקציה עם דפדפנים בצורה מבוקרת, ניתנת לביקורת ומורחבת—ומאפשר שימושים כמו בדיקות ווב אוטומטיות, חילוץ נתונים וזרימות עבודה מקצה לקצה.

- מציג יכולות אוטומציה של דפדפן (ניווט, מילוי טפסים, צילום מסך ועוד) ככלים במסגרת MCP  
- מיישם בקרות גישה מחמירות וסביבת ריצה מבודדת למניעת פעולות לא מורשות  
- מספק יומני ביקורת מפורטים לכל האינטראקציות עם הדפדפן  
- תומך באינטגרציה עם Azure OpenAI וספקי LLM נוספים לאוטומציה מונעת סוכנים  

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
- אפשר אוטומציה מאובטחת ומתוכנתת של דפדפנים עבור סוכני AI ו-LLM  
- הפחית את מאמץ הבדיקות הידניות ושיפר את כיסוי הבדיקות של יישומי ווב  
- סיפק מסגרת ניתנת לשימוש חוזר והרחבה לאינטגרציה של כלים מבוססי דפדפן בסביבות ארגוניות  

**הפניות:**  
- [Playwright MCP Server GitHub Repository](https://github.com/microsoft/playwright-mcp)  
- [Microsoft AI and Automation Solutions](https://azure.microsoft.com/en-us/products/ai-services/)  

### מחקר מקרה 5: Azure MCP – Model Context Protocol ברמת ארגון כשירות

Azure MCP ([https://aka.ms/azmcp](https://aka.ms/azmcp)) הוא יישום מנוהל ברמת ארגון של Model Context Protocol, שנועד לספק יכולות שרת MCP ניתנות להרחבה, מאובטחות ותואמות רגולציה כשירות בענן. Azure MCP מאפשר לארגונים לפרוס, לנהל ולשלב שרתי MCP במהירות עם שירותי Azure AI, נתונים ואבטחה, תוך הפחתת עומס תפעולי והאצת אימוץ AI.

- אירוח מנוהל מלא של שרת MCP עם קנה מידה מובנה, ניטור ואבטחה  
- אינטגרציה טבעית עם Azure OpenAI, Azure AI Search ושירותי Azure נוספים  
- אימות והרשאות ארגוניות באמצעות Microsoft Entra ID  
- תמיכה בכלים מותאמים, תבניות פקודות ומחברים למשאבים  
- עמידה בדרישות אבטחה ורגולציה ארגוניות  

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
- קיצור זמן הגעה לתוצאות בפרויקטי AI ארגוניים באמצעות פלטפורמת שרת MCP מוכנה לשימוש ותואמת  
- פישוט האינטגרציה של LLM, כלים ומקורות נתונים ארגוניים  
- שיפור האבטחה, הניטור והיעילות התפעולית בעומסי עבודה מבוססי MCP  

**הפניות:**  
- [Azure MCP Documentation](https://aka.ms/azmcp)  
- [Azure AI Services](https://azure.microsoft.com/en-us/products/ai-services/)  

## מחקר מקרה 6: NLWeb

MCP (Model Context Protocol) הוא פרוטוקול מתפתח לצ'אטבוטים ועוזרי AI לאינטראקציה עם כלים. כל מופע של NLWeb הוא גם שרת MCP, התומך בשיטה מרכזית אחת, ask, המשמשת לשאילת שאלות לאתר בשפה טבעית. התשובה המוחזרת משתמשת ב-schema.org, אוצר מילים נפוץ לתיאור נתוני ווב. במובן הרחב, MCP הוא NLWeb כפי ש-Http הוא ל-HTML. NLWeb משלב פרוטוקולים, פורמטים של Schema.org וקוד לדוגמה כדי לסייע לאתרים ליצור במהירות נקודות קצה אלה, המועילות הן לבני אדם בממשקי שיחה והן למכונות באינטראקציה טבעית בין סוכנים.

יש שני מרכיבים מובחנים ל-NLWeb:  
- פרוטוקול פשוט להתחלה, לאינטראקציה עם אתר בשפה טבעית ופורמט המשתמש ב-json ו-schema.org לתשובה המוחזרת. ראו תיעוד REST API לפרטים נוספים.  
- יישום פשוט של (1) המשתמש בסימון קיים, לאתרים שניתן להציגם כרשימות פריטים (מוצרים, מתכונים, אטרקציות, ביקורות וכו'). יחד עם אוסף ווידג'טים לממשק משתמש, אתרים יכולים לספק ממשקי שיחה לתוכן שלהם בקלות. ראו תיעוד Life of a chat query לפרטים נוספים על האופן בו זה עובד.  

**הפניות:**  
- [Azure MCP Documentation](https://aka.ms/azmcp)  
- [NLWeb](https://github.com/microsoft/NlWeb)  

## פרויקטים מעשיים

### פרויקט 1: בניית שרת MCP עם מספר ספקים

**מטרה:** ליצור שרת MCP שיכול לכוון בקשות לספקים שונים של מודלים מבוססי AI בהתאם לקריטריונים ספציפיים.

**דרישות:**  
- תמיכה בלפחות שלושה ספקי מודלים שונים (למשל OpenAI, Anthropic, מודלים מקומיים)  
- יישום מנגנון ניתוב מבוסס מטא-נתוני בקשה  
- יצירת מערכת תצורה לניהול אישורי ספקים  
- הוספת מטמון לאופטימיזציה של ביצועים ועלויות  
- בניית לוח בקרה פשוט למעקב שימוש  

**שלבי יישום:**  
1. הקמת תשתית בסיסית של שרת MCP  
2. יישום מתאמי ספק לכל שירות מודל AI  
3. יצירת לוגיקת ניתוב מבוססת מאפייני בקשה  
4. הוספת מנגנוני מטמון לבקשות תכופות  
5. פיתוח לוח בקרה למעקב  
6. בדיקה עם תבניות בקשה שונות  

**טכנולוגיות:** בחירה בין Python (.NET/Java/Python לפי העדפתך), Redis למטמון, ומסגרת ווב פשוטה ללוח הבקרה.

### פרויקט 2: מערכת ניהול פקודות ארגונית

**מטרה:** לפתח מערכת מבוססת MCP לניהול, גרסאות ופריסה של תבניות פקודות בארגון.

**דרישות:**  
- יצירת מאגר מרכזי לתבניות פקודות  
- יישום ניהול גרסאות ותהליכי אישור  
- בניית יכולות בדיקה של תבניות עם קלטים לדוגמה  
- פיתוח בקרות גישה מבוססות תפקידים  
- יצירת API לשליפה ופריסה של תבניות  

**שלבי יישום:**  
1. עיצוב סכמת מסד נתונים לאחסון תבניות  
2. יצירת API מרכזי לפעולות CRUD על תבניות  
3. יישום מערכת ניהול גרסאות  
4. בניית תהליך אישור  
5. פיתוח מסגרת בדיקה  
6. יצירת ממשק ווב פשוט לניהול  
7. אינטגרציה עם שרת MCP  

**טכנולוגיות:** בחירת מסגרת backend, מסד SQL או NoSQL, ומסגרת frontend לממשק הניהול.

### פרויקט 3: פלטפורמת יצירת תוכן מבוססת MCP

**מטרה:** לבנות פלטפורמה ליצירת תוכן המשתמשת ב-MCP כדי לספק תוצאות עקביות בסוגי תוכן שונים.

**דרישות:**  
- תמיכה בפורמטים שונים של תוכן (פוסטים בבלוג, רשתות חברתיות, טקסט שיווקי)  
- יישום יצירה מבוססת תבניות עם אפשרויות התאמה אישית  
- יצירת מערכת סקירה ומשוב לתוכן  
- מעקב אחרי מדדי ביצועים של תוכן  
- תמיכה בניהול גרסאות וחזרות  

**שלבי יישום:**  
1. הקמת תשתית לקוח MCP  
2. יצירת תבניות לסוגי תוכן שונים  
3. בניית צינור יצירת התוכן  
4. יישום מערכת סקירה  
5. פיתוח מערכת מעקב מדדים  
6. יצירת ממשק משתמש לניהול תבניות ויצירת תוכן  

**טכנולוגיות:** שפת תכנות מועדפת, מסגרת ווב ומערכת מסד נתונים.

## כיוונים עתידיים לטכנולוגיית MCP

### מגמות מתפתחות

1. **MCP רב-מודלי**  
   - הרחבת MCP לאינטראקציה סטנדרטית עם מודלים של תמונה, אודיו ווידאו  
   - פיתוח יכולות הסקת מסקנות בין-מודליות  
   - פורמטים סטנדרטיים לפקודות במודאליות שונות  

2. **תשתית MCP פדרטיבית**  
   - רשתות MCP מבוזרות לשיתוף משאבים בין ארגונים  
   - פרוטוקולים סטנדרטיים לשיתוף מודלים מאובטח  
   - טכניקות חישוב לשמירת פרטיות  

3. **שווקי MCP**  
   - אקוסיסטמים לשיתוף ומונטיזציה של תבניות ותוספים ל-MCP  
   - תהליכי אבטחת איכות והסמכה  
   - אינטגרציה עם שווקי מודלים  

4. **MCP למחשוב קצה**  
   - התאמת תקני MCP למכשירי קצה עם משאבים מוגבלים  
   - פרוטוקולים מותאמים לסביבות עם רוחב פס נמוך  
   - יישומים מיוחדים ל-MCP באקוסיסטמי IoT  

5. **מסגרות רגולטוריות**  
   - פיתוח הרחבות MCP לציות לרגולציה  
   - מסלולי ביקורת ויכולות הסבר סטנדרטיים  
   - אינטגרציה עם מסגרות ממשל AI מתפתחות  

### פתרונות MCP של Microsoft

מיקרוסופט ו-Azure פיתחו מספר מאגרי קוד פתוח כדי לסייע למפתחים ליישם MCP בתרחישים שונים:

#### ארגון Microsoft  
1. [playwright-mcp](https://github.com/microsoft/playwright-mcp) - שרת MCP ל-Playwright לאוטומציה ובדיקות דפדפן  
2. [files-mcp-server](https://github.com/microsoft/files-mcp-server) - יישום שרת MCP ל-OneDrive לבדיקה מקומית ותרומה לקהילה  
3. [NLWeb](https://github.com/microsoft/NlWeb) - אוסף פרוטוקולים וכלים בקוד פתוח. מתמקד בשכבת יסוד לאינטרנט מבוסס AI  

#### ארגון Azure-Samples  
1. [mcp](https://github.com/Azure-Samples/mcp) - קישורים לדוגמאות, כלים ומשאבים לבניית ושילוב שרתי MCP ב-Azure בשפות שונות  
2. [mcp-auth-servers](https://github.com/Azure-Samples/mcp-auth-servers) - שרתי MCP לדוגמה המדגימים אימות לפי מפרט MCP הנוכחי  
3. [remote-mcp-functions](https://github.com/Azure-Samples/remote-mcp-functions) - דף נחיתה ליישומי שרת MCP מרוחקים ב-Azure Functions עם קישורים לריפוזיטוריות לפי שפה  
4. [remote-mcp-functions-python](https://github.com/Azure-Samples/remote-mcp-functions-python) - תבנית התחלה מהירה לבניית ופריסת שרתי MCP מרוחקים מותאמים ב-Azure Functions בפייתון  
5. [remote-mcp-functions-dotnet](https://github.com/Azure-Samples/remote-mcp-functions-dotnet) - תבנית התחלה מהירה לבניית ופריסת שרתי MCP מרוחקים מותאמים ב-.NET/C#  
6. [remote-mcp-functions-typescript](https://github.com/Azure-Samples/remote-mcp-functions-typescript) - תבנית התחלה מהירה לבניית ופריסת שרתי MCP מרוחקים ב-TypeScript  
7. [remote-mcp-apim-functions-python](https://github.com/Azure-Samples/remote-mcp-apim-functions-python) - ניהול API של Azure כשער AI לשרתי MCP מרוחקים בפייתון  
8. [AI-Gateway](https://github.com/Azure-Samples/AI-Gateway) - ניסויים באינטגרציה של APIM ו-AI כולל יכולות MCP, עם אינטגרציה ל-Azure OpenAI ו-AI Foundry  

מאגרים אלו מספקים יישומים, תבניות ומשאבים לעבודה עם Model Context Protocol בשפות תכנות שונות ובשירותי Azure. הם מכסים מגוון שימושים מיישומי שרת בסיסיים ועד אימות, פריסה בענן ואינטגרציה ארגונית.

#### מדריך משאבי MCP

[מדריך המשאבים של MCP](https://github.com/microsoft/mcp/tree/main/Resources) במאגר הרשמי של Microsoft MCP מציע אוסף מובחר של דוגמאות משאבים, תבניות פקודות והגדרות כלים לשימוש עם שרתי Model Context Protocol. מדריך זה נועד לסייע למפתחים להתחיל במהירות עם MCP על ידי מתן בלוקים לבנייה לשימוש חוזר ודוגמאות לשיטות עבודה מומלצות עבור:

- **תבניות פקודות:** תבניות מוכנות לשימוש למשימות ותסריטים נפוצים של AI, שניתן להתאים ליישומי שרת MCP שלכם  
- **הגדרות כלים:** דוגמאות לסכמות כלים ומטא-נתונים לסטנדרטיזציה של אינטגרציה והפעלה של כלים בשרתי MCP שונים  
- **דוגמאות משאבים:** הגדרות משאבים לדוגמה לחיבור למקורות נתונים, API ושירותים חיצוניים במסגרת MCP  
- **יישומים לדוג
- [Remote MCP Functions Python (Azure-Samples)](https://github.com/Azure-Samples/remote-mcp-functions-python)
- [Remote MCP Functions .NET (Azure-Samples)](https://github.com/Azure-Samples/remote-mcp-functions-dotnet)
- [Remote MCP Functions TypeScript (Azure-Samples)](https://github.com/Azure-Samples/remote-mcp-functions-typescript)
- [Remote MCP APIM Functions Python (Azure-Samples)](https://github.com/Azure-Samples/remote-mcp-apim-functions-python)
- [AI-Gateway (Azure-Samples)](https://github.com/Azure-Samples/AI-Gateway)
- [Microsoft AI and Automation Solutions](https://azure.microsoft.com/en-us/products/ai-services/)

## תרגילים

1. נתחו אחד ממקרי הבוחן והציעו גישה חלופית ליישום.
2. בחרו באחת מרעיונות הפרויקט וצרו מפרט טכני מפורט.
3. חקרו ענף שלא נכלל במקרי הבוחן ותארו כיצד MCP יכול להתמודד עם האתגרים הספציפיים שלו.
4. חקרו אחת מהכיוונים העתידיים וצרו קונספט להרחבה חדשה של MCP לתמיכה בכך.

הבא: [Best Practices](../08-BestPractices/README.md)

**כתב ויתור**:  
מסמך זה תורגם באמצעות שירות תרגום מבוסס בינה מלאכותית [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון כי תרגומים אוטומטיים עלולים להכיל שגיאות או אי-דיוקים. המסמך המקורי בשפת המקור שלו נחשב למקור הסמכותי. למידע קריטי מומלץ להשתמש בתרגום מקצועי אנושי. אנו לא נושאים באחריות לכל אי הבנה או פרשנות שגויה הנובעת משימוש בתרגום זה.