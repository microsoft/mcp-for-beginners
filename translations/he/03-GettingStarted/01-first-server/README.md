# להתחיל עם MCP

ברוכים הבאים לצעדים הראשונים שלכם עם פרוטוקול הקשר מודל (MCP)! בין אם אתם חדשים ל-MCP או מחפשים להעמיק את ההבנה שלכם, המדריך הזה ילווה אתכם בתהליך ההקמה והפיתוח ההכרחי. תגלו כיצד MCP מאפשר אינטגרציה חלקה בין מודלים של בינה מלאכותית ויישומים, ותלמדו כיצד להכין במהירות את הסביבה שלכם לבניית ולטסט פתרונות המופעלים על ידי MCP.

> TLDR; אם אתם בונים אפליקציות AI, אתם יודעים שניתן להוסיף כלים ומשאבים נוספים ל-LLM שלכם (מודל שפה גדול), כדי להפוך את ה-LLM ליותר אינפורמטיבי. אך אם תמקמו את הכלים והמשאבים האלה בשרת, יכולות האפליקציה והשרת יכולות לשמש כל לקוח עם או בלי LLM.

## סקירה כללית

השיעור הזה מספק הדרכה מעשית על הגדרת סביבות MCP ובניית האפליקציות הראשונות שלכם ב-MCP. תלמדו כיצד להגדיר את הכלים והמסגרות הדרושים, לבנות שרתי MCP בסיסיים, ליצור יישומי מארח ולבדוק את המימושים שלכם.

פרוטוקול הקשר מודל (MCP) הוא פרוטוקול פתוח המייצב איך אפליקציות מספקות הקשר ל-LLMs. חשבו על MCP כמו פורט USB-C לאפליקציות AI - הוא מספק דרך סטנדרטית לחבר מודלי AI למשאבי נתונים וכלים שונים.

## מטרות למידה

בסיום השיעור תוכלו:

- להגדיר סביבות פיתוח ל-MCP ב-C#, Java, Python, TypeScript ו-Rust
- לבנות ולפרוס שרתי MCP בסיסיים עם תכונות מותאמות אישית (משאבים, תבניות וכלים)
- ליצור אפליקציות מארחות שמתחברות לשרתי MCP
- לבדוק ולתקן באגים במימושי MCP

## הגדרת סביבת ה-MCP שלכם

לפני שתתחילו לעבוד עם MCP, חשוב להכין את סביבת הפיתוח שלכם ולהבין את זרימת העבודה הבסיסית. מדור זה ינחה אתכם בשלבי ההתקנה הראשוניים כדי להבטיח התחלה חלקה עם MCP.

### דרישות מוקדמות

לפני שתצללו לפיתוח ב-MCP, ודאו שיש לכם:

- **סביבת פיתוח**: עבור השפה שבחרתם (C#, Java, Python, TypeScript או Rust)
- **IDE/עורך קוד**: Visual Studio, Visual Studio Code, IntelliJ, Eclipse, PyCharm או כל עורך קוד מודרני
- **מנהל חבילות**: NuGet, Maven/Gradle, pip, npm/yarn או Cargo
- **מפתחות API**: עבור כל שירות AI שאתם מתכננים להשתמש בהם באפליקציות המארחות שלכם

## מבנה בסיסי של שרת MCP

שרת MCP טיפוסי כולל:

- **קונפיגורציה של השרת**: הגדרת פורט, אימות והגדרות נוספות
- **משאבים**: נתונים והקשר שנגישים ל-LLMs
- **כלים**: פונקציונליות שהמודלים יכולים להפעיל
- **תבניות**: תבניות ליצירת או מבנה טקסט

הנה דוגמה מפושטת ב-TypeScript:

```typescript
import { McpServer, ResourceTemplate } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";

// צור שרת MCP
const server = new McpServer({
  name: "Demo",
  version: "1.0.0"
});

// הוסף כלי נוסף
server.tool("add",
  { a: z.number(), b: z.number() },
  async ({ a, b }) => ({
    content: [{ type: "text", text: String(a + b) }]
  })
);

// הוסף משאב ברכה דינמי
server.resource(
  "file",
  // הפרמטר 'list' שולט כיצד המשאב מביא רשימה של קבצים זמינים. הגדרתו כ-undefined מבטלת את הרישום עבור משאב זה.
  new ResourceTemplate("file://{path}", { list: undefined }),
  async (uri, { path }) => ({
    contents: [{
      uri: uri.href,
      text: `File, ${path}!`
    }]
  })
);

// הוסף משאב קובץ שקורא את תוכן הקובץ
server.resource(
  "file",
  new ResourceTemplate("file://{path}", { list: undefined }),
  async (uri, { path }) => {
    let text;
    try {
      text = await fs.readFile(path, "utf8");
    } catch (err) {
      text = `Error reading file: ${err.message}`;
    }
    return {
      contents: [{
        uri: uri.href,
        text
      }]
    };
  }
);

server.prompt(
  "review-code",
  { code: z.string() },
  ({ code }) => ({
    messages: [{
      role: "user",
      content: {
        type: "text",
        text: `Please review this code:\n\n${code}`
      }
    }]
  })
);

// התחל לקבל הודעות בקלט סטנדרטי ולשלוח הודעות ביציאה סטנדרטית
const transport = new StdioServerTransport();
await server.connect(transport);
```

בקוד שלמעלה אנחנו:

- מייבאים את המחלקות הנחוצות מ-SDK של MCP ב-TypeScript.
- יוצרים ומגדירים מופע חדש של שרת MCP.
- מרשימים כלי מותאם אישית (`calculator`) עם פונקציית טיפול.
- מפעילים את השרת להאזנה לבקשות MCP נכנסות.

## בדיקה ותיקון באגים

לפני שתתחילו לבדוק את שרת ה-MCP שלכם, חשוב להבין את הכלים והפרקטיקות הטובות ביותר לתיקון באגים. בדיקה יעילה מבטיחה שהשרת יתנהג כמצופה ועוזרת לכם לזהות ולפתור בעיות במהירות. המדור הבא מפרט דרכי עבודה מומלצות לאימות מימוש ה-MCP שלכם.

MCP מספק כלים שיעזרו לכם לבדוק ולתקן את השרתים:

- **כלי Inspector**, ממשק גרפי המאפשר חיבור לשרת ובדיקה של הכלים, התבניות והמשאבים שלכם.
- **curl**, אפשר גם להתחבר לשרת באמצעות כלי שורת הפקודה curl או לקוחות אחרים שיכולים להריץ פקודות HTTP.

### שימוש ב-MCP Inspector

[MCP Inspector](https://github.com/modelcontextprotocol/inspector) הוא כלי בדיקה ויזואלי שעוזר לכם:

1. **לגלות יכולות של השרת**: לזהות אוטומטית משאבים, כלים ותבניות זמינות
2. **לבחון הרצת כלים**: לנסות פרמטרים שונים ולראות תגובות בזמן אמת
3. **לצפות במטא נתונים של השרת**: לבדוק מידע על השרת, סכמות והגדרות

```bash
# לדוגמה TypeScript, התקנה והרצה של MCP Inspector
npx @modelcontextprotocol/inspector node build/index.js
```

כאשר תריצו את הפקודות הנ"ל, MCP Inspector יפתח ממשק אינטרנט מקומי בדפדפן שלכם. תוכלו לצפות בלוח בקרה המציג את שרתי ה-MCP שרשמתם, הכלים, המשאבים והתבניות הזמינים להם. הממשק מאפשר לכם לבדוק אינטראקטיבית את הרצת הכלים, לבדוק מטא נתונים של השרת ולצפות בתגובות בזמן אמת, מה שמקל לאמת ולתקן את מימושי שרת ה-MCP שלכם.

הנה צילום מסך של המראה האפשרי:

![MCP Inspector server connection](../../../../translated_images/he/connected.73d1e042c24075d3.webp)

## בעיות הגדרה נפוצות ופתרונות

| בעיה | פתרון אפשרי |
|-------|-------------------|
| חיבור נדחה | בדקו האם השרת פועל והפורט נכון |
| שגיאות בהרצת כלי | בדקו את אימות הפרמטרים וטיפול בשגיאות |
| כשלי אימות | ודאו מפתחות ה-API והרשאות נכונות |
| שגיאות אימות סכימה | ודאו שהפרמטרים תואמים לסכימה שהוגדרה |
| השרת לא מתחיל | בדקו קונפליקטים בפורט או תלות חסרה |
| שגיאות CORS | הגדירו כותרות CORS מתאימות לבקשות חוצות מקור |
| בעיות אימות | בדקו תוקף טוקנים והרשאות |

## פיתוח מקומי

עבור פיתוח ובדיקה מקומית, תוכלו להריץ שרתי MCP ישירות על המחשב שלכם:

1. **הפעלת תהליך השרת**: הריצו את אפליקציית השרת MCP שלכם
2. **הגדרת רשת**: ודאו שהשרת זמין בפורט הרצוי
3. **חיבור לקוחות**: השתמשו בכתובות מקומיות כמו `http://localhost:3000`

```bash
# דוגמה: הפעלת שרת MCP ב-TypeScript מקומית
npm run start
# השרת רץ בכתובת http://localhost:3000
```

## בניית שרת MCP ראשון שלכם

כיסינו את [מושגי הליבה](../../01-CoreConcepts/README.md) בשיעור קודם, ועכשיו הגיע הזמן לממש את הידע.

### מה שרת יכול לעשות

לפני שנתחיל לכתוב קוד, נזכיר לעצמנו מה שרת יכול לעשות:

שרת MCP יכול למשל:

- לגשת לקבצים ומסדי נתונים מקומיים
- להתחבר ל-APIs מרוחקים
- לבצע חישובים
- להשתלב עם כלים ושירותים אחרים
- לספק ממשק משתמש לאינטראקציה

מצוין, עכשיו שאנחנו יודעים מה אפשר לעשות, בואו נתחיל לקודד.

## תרגיל: יצירת שרת

ליצירת שרת, יש לעקוב אחרי השלבים הבאים:

- התקנת SDK של MCP.
- יצירת פרויקט והגדרת מבנה הפרויקט.
- כתיבת קוד השרת.
- בדיקת השרת.

### -1- יצירת פרויקט

#### TypeScript

```sh
# צור מדריך פרויקט ואתחל פרויקט npm
mkdir calculator-server
cd calculator-server
npm init -y
```

#### Python

```sh
# צור תיקיית פרויקט
mkdir calculator-server
cd calculator-server
# פתח את התיקייה ב-Visual Studio Code - דלג על כך אם אתה משתמש ב-IDE שונה
code .
```

#### .NET

```sh
dotnet new console -n McpCalculatorServer
cd McpCalculatorServer
```

#### Java

עבור Java, צרו פרויקט Spring Boot:

```bash
curl https://start.spring.io/starter.zip \
  -d dependencies=web \
  -d javaVersion=21 \
  -d type=maven-project \
  -d groupId=com.example \
  -d artifactId=calculator-server \
  -d name=McpServer \
  -d packageName=com.microsoft.mcp.sample.server \
  -o calculator-server.zip
```

חלצו את קובץ ה-zip:

```bash
unzip calculator-server.zip -d calculator-server
cd calculator-server
# אפשרי להסיר את הבדיקה הלא בשימוש
rm -rf src/test/java
```

הוסיפו את ההגדרה המלאה הבאה לקובץ *pom.xml* שלכם:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    
    <!-- Spring Boot parent for dependency management -->
    <parent>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-parent</artifactId>
        <version>3.5.0</version>
        <relativePath />
    </parent>

    <!-- Project coordinates -->
    <groupId>com.example</groupId>
    <artifactId>calculator-server</artifactId>
    <version>0.0.1-SNAPSHOT</version>
    <name>Calculator Server</name>
    <description>Basic calculator MCP service for beginners</description>

    <!-- Properties -->
    <properties>
        <java.version>21</java.version>
        <maven.compiler.source>21</maven.compiler.source>
        <maven.compiler.target>21</maven.compiler.target>
    </properties>

    <!-- Spring AI BOM for version management -->
    <dependencyManagement>
        <dependencies>
            <dependency>
                <groupId>org.springframework.ai</groupId>
                <artifactId>spring-ai-bom</artifactId>
                <version>1.0.0-SNAPSHOT</version>
                <type>pom</type>
                <scope>import</scope>
            </dependency>
        </dependencies>
    </dependencyManagement>

    <!-- Dependencies -->
    <dependencies>
        <dependency>
            <groupId>org.springframework.ai</groupId>
            <artifactId>spring-ai-starter-mcp-server-webflux</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-actuator</artifactId>
        </dependency>
        <dependency>
         <groupId>org.springframework.boot</groupId>
         <artifactId>spring-boot-starter-test</artifactId>
         <scope>test</scope>
      </dependency>
    </dependencies>

    <!-- Build configuration -->
    <build>
        <plugins>
            <plugin>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-maven-plugin</artifactId>
            </plugin>
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-compiler-plugin</artifactId>
                <configuration>
                    <release>21</release>
                </configuration>
            </plugin>
        </plugins>
    </build>

    <!-- Repositories for Spring AI snapshots -->
    <repositories>
        <repository>
            <id>spring-milestones</id>
            <name>Spring Milestones</name>
            <url>https://repo.spring.io/milestone</url>
            <snapshots>
                <enabled>false</enabled>
            </snapshots>
        </repository>
        <repository>
            <id>spring-snapshots</id>
            <name>Spring Snapshots</name>
            <url>https://repo.spring.io/snapshot</url>
            <releases>
                <enabled>false</enabled>
            </releases>
        </repository>
    </repositories>
</project>
```

#### Rust

```sh
mkdir calculator-server
cd calculator-server
cargo init
```

### -2- הוספת תלותים

כעת כשיש לכם פרויקט, נוסיף את התלותים הבאות:

#### TypeScript

```sh
# אם עדיין לא מותקן, התקן את TypeScript באופן גלובלי
npm install typescript -g

# התקן את MCP SDK ואת Zod לאימות סכימה
npm install @modelcontextprotocol/sdk zod
npm install -D @types/node typescript
```

#### Python

```sh
# צור סביבה וירטואלית והתקן תלותים
python -m venv venv
venv\Scripts\activate
pip install "mcp[cli]"
```

#### Java

```bash
cd calculator-server
./mvnw clean install -DskipTests
```

#### Rust

```sh
cargo add rmcp --features server,transport-io
cargo add serde
cargo add tokio --features rt-multi-thread
```

### -3- יצירת קבצי הפרויקט

#### TypeScript

פתחו את הקובץ *package.json* והחליפו את התוכן הבא כדי להבטיח שתוכלו לבנות ולהריץ את השרת:

```json
{
  "name": "calculator-server",
  "version": "1.0.0",
  "main": "index.js",
  "type": "module",
  "scripts": {
    "build": "tsc",
    "start": "npm run build && node ./build/index.js",
  },
  "keywords": [],
  "author": "",
  "license": "ISC",
  "description": "A simple calculator server using Model Context Protocol",
  "dependencies": {
    "@modelcontextprotocol/sdk": "^1.16.0",
    "zod": "^3.25.76"
  },
  "devDependencies": {
    "@types/node": "^24.0.14",
    "typescript": "^5.8.3"
  }
}
```

צרו קובץ *tsconfig.json* עם התוכן הבא:

```json
{
  "compilerOptions": {
    "target": "ES2022",
    "module": "Node16",
    "moduleResolution": "Node16",
    "outDir": "./build",
    "rootDir": "./src",
    "strict": true,
    "esModuleInterop": true,
    "skipLibCheck": true,
    "forceConsistentCasingInFileNames": true
  },
  "include": ["src/**/*"],
  "exclude": ["node_modules"]
}
```

צרו תיקייה לקוד המקור שלכם:

```sh
mkdir src
touch src/index.ts
```

#### Python

צרו קובץ *server.py*

```sh
touch server.py
```

#### .NET

התקינו את חבילות NuGet הנדרשות:

```sh
dotnet add package ModelContextProtocol --prerelease
dotnet add package Microsoft.Extensions.Hosting
```

#### Java

לפרויקטי Java Spring Boot, מבנה הפרויקט נוצר אוטומטית.

#### Rust

עבור Rust, קובץ *src/main.rs* נוצר כברירת מחדל כשמריצים `cargo init`. פתחו את הקובץ ומחקו את הקוד המוגדר כברירת מחדל.

### -4- כתיבת קוד השרת

#### TypeScript

צרו קובץ *index.ts* והוסיפו את הקוד הבא:

```typescript
import { McpServer, ResourceTemplate } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";
 
// צור שרת MCP
const server = new McpServer({
  name: "Calculator MCP Server",
  version: "1.0.0"
});
```

כעת יש לכם שרת, אבל הוא לא עושה הרבה, בואו נשפר אותו.

#### Python

```python
# server.py
from mcp.server.fastmcp import FastMCP

# צור שרת MCP
mcp = FastMCP("Demo")
```

#### .NET

```csharp
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;
using Microsoft.Extensions.Logging;
using ModelContextProtocol.Server;
using System.ComponentModel;

var builder = Host.CreateApplicationBuilder(args);
builder.Logging.AddConsole(consoleLogOptions =>
{
    // Configure all logs to go to stderr
    consoleLogOptions.LogToStandardErrorThreshold = LogLevel.Trace;
});

builder.Services
    .AddMcpServer()
    .WithStdioServerTransport()
    .WithToolsFromAssembly();
await builder.Build().RunAsync();

// add features
```

#### Java

לגבי Java, צרו את הרכיבים המרכזיים של השרת. תחילה, ערכו את מחלקת האפליקציה הראשית:

*src/main/java/com/microsoft/mcp/sample/server/McpServerApplication.java*:

```java
package com.microsoft.mcp.sample.server;

import org.springframework.ai.tool.ToolCallbackProvider;
import org.springframework.ai.tool.method.MethodToolCallbackProvider;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.Bean;
import com.microsoft.mcp.sample.server.service.CalculatorService;

@SpringBootApplication
public class McpServerApplication {

    public static void main(String[] args) {
        SpringApplication.run(McpServerApplication.class, args);
    }
    
    @Bean
    public ToolCallbackProvider calculatorTools(CalculatorService calculator) {
        return MethodToolCallbackProvider.builder().toolObjects(calculator).build();
    }
}
```

צרו את שירות החשבון *src/main/java/com/microsoft/mcp/sample/server/service/CalculatorService.java*:

```java
package com.microsoft.mcp.sample.server.service;

import org.springframework.ai.tool.annotation.Tool;
import org.springframework.stereotype.Service;

/**
 * Service for basic calculator operations.
 * This service provides simple calculator functionality through MCP.
 */
@Service
public class CalculatorService {

    /**
     * Add two numbers
     * @param a The first number
     * @param b The second number
     * @return The sum of the two numbers
     */
    @Tool(description = "Add two numbers together")
    public String add(double a, double b) {
        double result = a + b;
        return formatResult(a, "+", b, result);
    }

    /**
     * Subtract one number from another
     * @param a The number to subtract from
     * @param b The number to subtract
     * @return The result of the subtraction
     */
    @Tool(description = "Subtract the second number from the first number")
    public String subtract(double a, double b) {
        double result = a - b;
        return formatResult(a, "-", b, result);
    }

    /**
     * Multiply two numbers
     * @param a The first number
     * @param b The second number
     * @return The product of the two numbers
     */
    @Tool(description = "Multiply two numbers together")
    public String multiply(double a, double b) {
        double result = a * b;
        return formatResult(a, "*", b, result);
    }

    /**
     * Divide one number by another
     * @param a The numerator
     * @param b The denominator
     * @return The result of the division
     */
    @Tool(description = "Divide the first number by the second number")
    public String divide(double a, double b) {
        if (b == 0) {
            return "Error: Cannot divide by zero";
        }
        double result = a / b;
        return formatResult(a, "/", b, result);
    }

    /**
     * Calculate the power of a number
     * @param base The base number
     * @param exponent The exponent
     * @return The result of raising the base to the exponent
     */
    @Tool(description = "Calculate the power of a number (base raised to an exponent)")
    public String power(double base, double exponent) {
        double result = Math.pow(base, exponent);
        return formatResult(base, "^", exponent, result);
    }

    /**
     * Calculate the square root of a number
     * @param number The number to find the square root of
     * @return The square root of the number
     */
    @Tool(description = "Calculate the square root of a number")
    public String squareRoot(double number) {
        if (number < 0) {
            return "Error: Cannot calculate square root of a negative number";
        }
        double result = Math.sqrt(number);
        return String.format("√%.2f = %.2f", number, result);
    }

    /**
     * Calculate the modulus (remainder) of division
     * @param a The dividend
     * @param b The divisor
     * @return The remainder of the division
     */
    @Tool(description = "Calculate the remainder when one number is divided by another")
    public String modulus(double a, double b) {
        if (b == 0) {
            return "Error: Cannot divide by zero";
        }
        double result = a % b;
        return formatResult(a, "%", b, result);
    }

    /**
     * Calculate the absolute value of a number
     * @param number The number to find the absolute value of
     * @return The absolute value of the number
     */
    @Tool(description = "Calculate the absolute value of a number")
    public String absolute(double number) {
        double result = Math.abs(number);
        return String.format("|%.2f| = %.2f", number, result);
    }

    /**
     * Get help about available calculator operations
     * @return Information about available operations
     */
    @Tool(description = "Get help about available calculator operations")
    public String help() {
        return "Basic Calculator MCP Service\n\n" +
               "Available operations:\n" +
               "1. add(a, b) - Adds two numbers\n" +
               "2. subtract(a, b) - Subtracts the second number from the first\n" +
               "3. multiply(a, b) - Multiplies two numbers\n" +
               "4. divide(a, b) - Divides the first number by the second\n" +
               "5. power(base, exponent) - Raises a number to a power\n" +
               "6. squareRoot(number) - Calculates the square root\n" + 
               "7. modulus(a, b) - Calculates the remainder of division\n" +
               "8. absolute(number) - Calculates the absolute value\n\n" +
               "Example usage: add(5, 3) will return 5 + 3 = 8";
    }

    /**
     * Format the result of a calculation
     */
    private String formatResult(double a, String operator, double b, double result) {
        return String.format("%.2f %s %.2f = %.2f", a, operator, b, result);
    }
}
```

**רכיבים אופציונליים לשירות מוכן לפרודקשן:**

צרו קונפיגורציית הפעלה *src/main/java/com/microsoft/mcp/sample/server/config/StartupConfig.java*:

```java
package com.microsoft.mcp.sample.server.config;

import org.springframework.boot.CommandLineRunner;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

@Configuration
public class StartupConfig {
    
    @Bean
    public CommandLineRunner startupInfo() {
        return args -> {
            System.out.println("\n" + "=".repeat(60));
            System.out.println("Calculator MCP Server is starting...");
            System.out.println("SSE endpoint: http://localhost:8080/sse");
            System.out.println("Health check: http://localhost:8080/actuator/health");
            System.out.println("=".repeat(60) + "\n");
        };
    }
}
```

צרו בקרה לבריאות השרת *src/main/java/com/microsoft/mcp/sample/server/controller/HealthController.java*:

```java
package com.microsoft.mcp.sample.server.controller;

import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;
import java.time.LocalDateTime;
import java.util.HashMap;
import java.util.Map;

@RestController
public class HealthController {
    
    @GetMapping("/health")
    public ResponseEntity<Map<String, Object>> healthCheck() {
        Map<String, Object> response = new HashMap<>();
        response.put("status", "UP");
        response.put("timestamp", LocalDateTime.now().toString());
        response.put("service", "Calculator MCP Server");
        return ResponseEntity.ok(response);
    }
}
```

צרו מטפל בשגיאות *src/main/java/com/microsoft/mcp/sample/server/exception/GlobalExceptionHandler.java*:

```java
package com.microsoft.mcp.sample.server.exception;

import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.ExceptionHandler;
import org.springframework.web.bind.annotation.RestControllerAdvice;

@RestControllerAdvice
public class GlobalExceptionHandler {

    @ExceptionHandler(IllegalArgumentException.class)
    public ResponseEntity<ErrorResponse> handleIllegalArgumentException(IllegalArgumentException ex) {
        ErrorResponse error = new ErrorResponse(
            "Invalid_Input", 
            "Invalid input parameter: " + ex.getMessage());
        return new ResponseEntity<>(error, HttpStatus.BAD_REQUEST);
    }

    public static class ErrorResponse {
        private String code;
        private String message;

        public ErrorResponse(String code, String message) {
            this.code = code;
            this.message = message;
        }

        // מאגרים
        public String getCode() { return code; }
        public String getMessage() { return message; }
    }
}
```

צרו באנר מותאם *src/main/resources/banner.txt*:

```text
_____      _            _       _             
 / ____|    | |          | |     | |            
| |     __ _| | ___ _   _| | __ _| |_ ___  _ __ 
| |    / _` | |/ __| | | | |/ _` | __/ _ \| '__|
| |___| (_| | | (__| |_| | | (_| | || (_) | |   
 \_____\__,_|_|\___|\__,_|_|\__,_|\__\___/|_|   
                                                
Calculator MCP Server v1.0
Spring Boot MCP Application
```

</details>

#### Rust

הוסיפו את הקוד הבא לראש הקובץ *src/main.rs*. הוא מייבא את הספריות והמודולים הנחוצים לשרת MCP שלכם.

```rust
use rmcp::{
    handler::server::{router::tool::ToolRouter, tool::Parameters},
    model::{ServerCapabilities, ServerInfo},
    schemars, tool, tool_handler, tool_router,
    transport::stdio,
    ServerHandler, ServiceExt,
};
use std::error::Error;
```

שרת המכונה המחשבת יהיה פשוט ויוכל להוסיף שני מספרים יחד. בואו ניצור מבנה נתונים (struct) שמייצג בקשת מחשבון.

```rust
#[derive(Debug, serde::Deserialize, schemars::JsonSchema)]
pub struct CalculatorRequest {
    pub a: f64,
    pub b: f64,
}
```

לאחר מכן, צרו struct שמייצג את שרת המחשבון. struct זה יחזיק את המנתב לכלים, המשמש לרישום כלים.

```rust
#[derive(Debug, Clone)]
pub struct Calculator {
    tool_router: ToolRouter<Self>,
}
```

כעת, נוכל לממש את ה-`Calculator` struct כדי ליצור מופע חדש של השרת ולממש את מטפל השרת שיספק מידע על השרת.

```rust
#[tool_router]
impl Calculator {
    pub fn new() -> Self {
        Self {
            tool_router: Self::tool_router(),
        }
    }
}

#[tool_handler]
impl ServerHandler for Calculator {
    fn get_info(&self) -> ServerInfo {
        ServerInfo {
            instructions: Some("A simple calculator tool".into()),
            capabilities: ServerCapabilities::builder().enable_tools().build(),
            ..Default::default()
        }
    }
}
```

לבסוף, עלינו לממש את פונקציית ה-main כדי להפעיל את השרת. פונקציה זו תיצור מופע של struct ה-`Calculator` ותפעיל אותו באמצעות קלט/פלט סטנדרטי.

```rust
#[tokio::main]
async fn main() -> Result<(), Box<dyn Error>> {
    let service = Calculator::new().serve(stdio()).await?;
    service.waiting().await?;
    Ok(())
}
```

השרת מוכן כעת לספק מידע בסיסי על עצמו. בהמשך נוסיף כלי שיבצע חיבור.

### -5- הוספת כלי ומשאב

הוסיפו כלי ומשאב על ידי הוספת הקוד הבא:

#### TypeScript

```typescript
server.tool(
  "add",
  { a: z.number(), b: z.number() },
  async ({ a, b }) => ({
    content: [{ type: "text", text: String(a + b) }]
  })
);

server.resource(
  "greeting",
  new ResourceTemplate("greeting://{name}", { list: undefined }),
  async (uri, { name }) => ({
    contents: [{
      uri: uri.href,
      text: `Hello, ${name}!`
    }]
  })
);
```

הכלי שלכם מקבל פרמטרים `a` ו-`b` ומריץ פונקציה שמחזירה תגובה בצורה:

```typescript
{
  contents: [{
    type: "text", content: "some content"
  }]
}
```

המשאב שלכם ניגש באמצעות המחרוזת "greeting" ומקבל פרמטר `name` ומחזיר תגובה דומה לזו של הכלי:

```typescript
{
  uri: "<href>",
  text: "a text"
}
```

#### Python

```python
# הוסף כלי חיבור
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


# הוסף משאב ברכה דינמי
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}!"
```

בקוד שלמעלה הגדרנו:

- כלי `add` שלוקח פרמטרים `a` ו-`b`, שניהם שלמים.
- יצרנו משאב בשם `greeting` שלוקח פרמטר `name`.

#### .NET

הוסיפו זאת לקובץ Program.cs שלכם:

```csharp
[McpServerToolType]
public static class CalculatorTool
{
    [McpServerTool, Description("Adds two numbers")]
    public static string Add(int a, int b) => $"Sum {a + b}";
}
```

#### Java

הכלים כבר נוצרו בשלב קודם.

#### Rust

הוסיפו כלי חדש בתוך בלוק `impl Calculator`:

```rust
#[tool(description = "Adds a and b")]
async fn add(
    &self,
    Parameters(CalculatorRequest { a, b }): Parameters<CalculatorRequest>,
) -> String {
    (a + b).to_string()
}
```

### -6- קוד סופי

בואו נוסיף את הקוד האחרון הנדרש כדי שהשרת יוכל להתחיל:

#### TypeScript

```typescript
// התחלת קבלת הודעות על stdin ושליחת הודעות על stdout
const transport = new StdioServerTransport();
await server.connect(transport);
```

הנה הקוד המלא:

```typescript
// index.ts
import { McpServer, ResourceTemplate } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";

// יצירת שרת MCP
const server = new McpServer({
  name: "Calculator MCP Server",
  version: "1.0.0"
});

// הוסף כלי חיבור
server.tool(
  "add",
  { a: z.number(), b: z.number() },
  async ({ a, b }) => ({
    content: [{ type: "text", text: String(a + b) }]
  })
);

// הוסף משאב ברכה דינמי
server.resource(
  "greeting",
  new ResourceTemplate("greeting://{name}", { list: undefined }),
  async (uri, { name }) => ({
    contents: [{
      uri: uri.href,
      text: `Hello, ${name}!`
    }]
  })
);

// התחל לקבל הודעות ב-stdin ולשלוח הודעות ב-stdout
const transport = new StdioServerTransport();
server.connect(transport);
```

#### Python

```python
# server.py
from mcp.server.fastmcp import FastMCP

# צור שרת MCP
mcp = FastMCP("Demo")


# הוסף כלי חיבור
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


# הוסף משאב ברכה דינאמית
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}!"

# בלוק ביצוע ראשי - זה דרוש כדי להפעיל את השרת
if __name__ == "__main__":
    mcp.run()
```

#### .NET

צרו קובץ Program.cs עם התוכן הבא:

```csharp
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;
using Microsoft.Extensions.Logging;
using ModelContextProtocol.Server;
using System.ComponentModel;

var builder = Host.CreateApplicationBuilder(args);
builder.Logging.AddConsole(consoleLogOptions =>
{
    // Configure all logs to go to stderr
    consoleLogOptions.LogToStandardErrorThreshold = LogLevel.Trace;
});

builder.Services
    .AddMcpServer()
    .WithStdioServerTransport()
    .WithToolsFromAssembly();
await builder.Build().RunAsync();

[McpServerToolType]
public static class CalculatorTool
{
    [McpServerTool, Description("Adds two numbers")]
    public static string Add(int a, int b) => $"Sum {a + b}";
}
```

#### Java

מחלקת האפליקציה הראשית המלאה שלכם תיראה כך:

```java
// McpServerApplication.java
package com.microsoft.mcp.sample.server;

import org.springframework.ai.tool.ToolCallbackProvider;
import org.springframework.ai.tool.method.MethodToolCallbackProvider;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.Bean;
import com.microsoft.mcp.sample.server.service.CalculatorService;

@SpringBootApplication
public class McpServerApplication {

    public static void main(String[] args) {
        SpringApplication.run(McpServerApplication.class, args);
    }
    
    @Bean
    public ToolCallbackProvider calculatorTools(CalculatorService calculator) {
        return MethodToolCallbackProvider.builder().toolObjects(calculator).build();
    }
}
```

#### Rust

הקוד הסופי לשרת Rust יראה כך:

```rust
use rmcp::{
    ServerHandler, ServiceExt,
    handler::server::{router::tool::ToolRouter, tool::Parameters},
    model::{ServerCapabilities, ServerInfo},
    schemars, tool, tool_handler, tool_router,
    transport::stdio,
};
use std::error::Error;

#[derive(Debug, serde::Deserialize, schemars::JsonSchema)]
pub struct CalculatorRequest {
    pub a: f64,
    pub b: f64,
}

#[derive(Debug, Clone)]
pub struct Calculator {
    tool_router: ToolRouter<Self>,
}

#[tool_router]
impl Calculator {
    pub fn new() -> Self {
        Self {
            tool_router: Self::tool_router(),
        }
    }
    
    #[tool(description = "Adds a and b")]
    async fn add(
        &self,
        Parameters(CalculatorRequest { a, b }): Parameters<CalculatorRequest>,
    ) -> String {
        (a + b).to_string()
    }
}

#[tool_handler]
impl ServerHandler for Calculator {
    fn get_info(&self) -> ServerInfo {
        ServerInfo {
            instructions: Some("A simple calculator tool".into()),
            capabilities: ServerCapabilities::builder().enable_tools().build(),
            ..Default::default()
        }
    }
}

#[tokio::main]
async fn main() -> Result<(), Box<dyn Error>> {
    let service = Calculator::new().serve(stdio()).await?;
    service.waiting().await?;
    Ok(())
}
```

### -7- בדקו את השרת

הפעילו את השרת עם הפקודה הבאה:

#### TypeScript

```sh
npm run build
```

#### Python

```sh
mcp run server.py
```

> לשימוש ב-MCP Inspector, השתמשו בפקודה `mcp dev server.py` שמפעילה אוטומטית את Inspector ומספקת את טוקן המפסק לשיחות הפרוקסי. אם מריצים עם `mcp run server.py`, תצטרכו להפעיל ידנית את ה-Inspector ולהגדיר את החיבור.

#### .NET

ודאו שאתם בספריית הפרויקט שלכם:

```sh
cd McpCalculatorServer
dotnet run
```

#### Java

```bash
./mvnw clean install -DskipTests
java -jar target/calculator-server-0.0.1-SNAPSHOT.jar
```

#### Rust

הריצו את הפקודות הבאות לעיצוב וריצה של השרת:

```sh
cargo fmt
cargo run
```

### -8- הפעלה באמצעות Inspector

ה-Inspector הוא כלי מצוין שיכול להפעיל את השרת שלכם ולתת לכם אינטראקציה איתו כדי לבדוק שהוא פועל. בואו נפעיל אותו:

> [!NOTE]
> יתכן שהשדה "command" ייראה שונה כיוון שהוא מכיל את פקודת ההפעלה של השרת עם זמן הריצה הספציפי שלכם.

#### TypeScript

```sh
npx @modelcontextprotocol/inspector node build/index.js
```

או הוסיפו זאת ל-*package.json* כך: `"inspector": "npx @modelcontextprotocol/inspector node build/index.js"` ואז הריצו `npm run inspector`

#### Python

Python עוטף כלי Node.js בשם inspector. ניתן לקרוא לכלי זה כך:

```sh
mcp dev server.py
```

אולם, הכלי הזה לא מממש את כל השיטות הזמינות, לכן מומלץ להריץ את כלי Node.js ישירות כך:

```sh
npx @modelcontextprotocol/inspector mcp run server.py
```

אם אתם משתמשים בכלי או IDE שמאפשר להגדיר פקודות וארגומנטים להרצת סקריפטים,
ודא שהגדרת `python` בשדה `Command` ו-`server.py` כ`Arguments`. זה מבטיח שהסקריפט ירוץ כראוי.

#### .NET

ודא שאתה בספריית הפרויקט שלך:

```sh
cd McpCalculatorServer
npx @modelcontextprotocol/inspector dotnet run
```

#### Java

ודא שהשרת של המחשבון שלך פועל  
אז הרץ את הכלי inspector:

```cmd
npx @modelcontextprotocol/inspector
```

בממשק הרשת של ה-inspector:

1. בחר "SSE" כסוג התעבורה  
2. הגדר את הכתובת ל: `http://localhost:8080/sse`  
3. לחץ על "Connect"

![Connect](../../../../translated_images/he/tool.163d33e3ee307e20.webp)

**כעת אתה מחובר לשרת**  
**קטע בדיקת השרת בג'אווה הושלם כעת**

הקטע הבא עוסק באינטראקציה עם השרת.

עליך לראות את ממשק המשתמש הבא:

![Connect](../../../../translated_images/he/connect.141db0b2bd05f096.webp)

1. התחבר לשרת על ידי בחירת כפתור Connect  
  ברגע שאתה מתחבר לשרת, עליך לראות את הדבר הבא:

  ![Connected](../../../../translated_images/he/connected.73d1e042c24075d3.webp)

1. בחר "Tools" ואז "listTools", אמור להופיע "Add", בחר ב- "Add" ומלא את ערכי הפרמטרים.

  עליך לראות את התגובה הבאה, כלומר תוצאה מהכלי "add":

  ![Result of running add](../../../../translated_images/he/ran-tool.a5a6ee878c1369ec.webp)

מזל טוב, הצלחת ליצור ולהריץ את השרת הראשון שלך!

#### Rust

כדי להריץ את שרת ה-Rust עם MCP Inspector CLI, השתמש בפקודה הבאה:

```sh
npx @modelcontextprotocol/inspector cargo run --cli --method tools/call --tool-name add --tool-arg a=1 b=2
```

### SDKs רשמיים

MCP מספק SDKs רשמיים למספר שפות:

- [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk) - מתוחזק בשותפות עם מיקרוסופט  
- [Java SDK](https://github.com/modelcontextprotocol/java-sdk) - מתוחזק בשותפות עם Spring AI  
- [TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk) - המימוש הרשמי של TypeScript  
- [Python SDK](https://github.com/modelcontextprotocol/python-sdk) - המימוש הרשמי של Python  
- [Kotlin SDK](https://github.com/modelcontextprotocol/kotlin-sdk) - המימוש הרשמי של Kotlin  
- [Swift SDK](https://github.com/modelcontextprotocol/swift-sdk) - מתוחזק בשותפות עם Loopwork AI  
- [Rust SDK](https://github.com/modelcontextprotocol/rust-sdk) - המימוש הרשמי של Rust  

## נקודות מרכזיות להבנה

- הקמת סביבת פיתוח MCP היא פשוטה עם SDK ספציפיים לשפה  
- בניית שרתי MCP כוללת יצירה ורישום של כלים עם סכימות ברורות  
- בדיקות וניפוי שגיאות הם חיוניים למימושים אמינים של MCP  

## דוגמאות

- [מחשבון בג׳אווה](../samples/java/calculator/README.md)  
- [מחשבון .Net](../../../../03-GettingStarted/samples/csharp)  
- [מחשבון ב-JavaScript](../samples/javascript/README.md)  
- [מחשבון ב-TypeScript](../samples/typescript/README.md)  
- [מחשבון בפייתון](../../../../03-GettingStarted/samples/python)  
- [מחשבון ברסט](../../../../03-GettingStarted/samples/rust)  

## משימה

צור שרת MCP פשוט עם כלי לבחירתך:

1. מימוש הכלי בשפת התכנות המועדפת עליך (.NET, Java, Python, TypeScript, או Rust).  
2. הגדר פרמטרי קלט וערכי החזרה.  
3. הרץ את כלי ה-inspector כדי לוודא שהשרת עובד כמתוכנן.  
4. בדוק את המימוש עם קלטים שונים.  

## פתרון

[פתרון](./solution/README.md)

## משאבים נוספים

- [בניית סוכנים באמצעות Model Context Protocol על Azure](https://learn.microsoft.com/azure/developer/ai/intro-agents-mcp)  
- [MCP מרחוק עם Azure Container Apps (Node.js/TypeScript/JavaScript)](https://learn.microsoft.com/samples/azure-samples/mcp-container-ts/mcp-container-ts/)  
- [סוכן MCP של OpenAI ב-.NET](https://learn.microsoft.com/samples/azure-samples/openai-mcp-agent-dotnet/openai-mcp-agent-dotnet/)  

## מה הלאה

הבא: [התחלת עבודה עם לקוחות MCP](../02-client/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**כתב אחריות**:  
מסמך זה תורגם באמצעות שירות תרגום אוטומטי [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש להיות מודעים לכך שתרגומים אוטומטיים עשויים להכיל שגיאות או אי-דיוקים. יש להתייחס למסמך המקורי בשפתו המקורית כמקור הסמכות הראשי. למידע קריטי מומלץ להיעזר בתרגום מקצועי על ידי אדם. איננו נושאים באחריות לכל אי הבנה או פרשנות שגויה הנובעות משימוש בתרגום זה.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->