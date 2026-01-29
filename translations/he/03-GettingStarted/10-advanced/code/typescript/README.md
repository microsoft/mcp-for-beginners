# הפעלת דוגמה

## התקנת תלותים

```sh
npm install
```

## בנייה

```sh
npm run build
```

## הפעלה

```sh
npm start
```

אתם אמורים לראות את הטקסט:

```text
Registering tools...
Starting server...
```

מעולה, זה אומר שההפעלה מתבצעת בצורה תקינה.

## בדיקת השרת

בדקו את היכולות עם הפקודה הבאה:

```sh
npx @modelcontextprotocol/inspector node build/app.js
```

זה אמור להפעיל את ממשק האינטרנט של כלי הבדיקה.

### בדיקה במצב CLI

```sh
npx @modelcontextprotocol/inspector --cli node ./build/app.js --method tools/list
```

אתם אמורים לראות את הפלט הבא:

```json
{
  "tools": [
    {
      "name": "add",
      "inputSchema": {
        "type": "object",
        "properties": {
          "a": {
            "type": "number"
          },
          "b": {
            "type": "number"
          }
        },
        "required": [
          "a",
          "b"
        ],
        "additionalProperties": false,
        "$schema": "http://json-schema.org/draft-07/schema#"
      },
      "rawSchema": {
        "_def": {
          "unknownKeys": "strip",
          "catchall": {
            "_def": {
              "typeName": "ZodNever"
            },
            "~standard": {
              "version": 1,
              "vendor": "zod"
            }
          },
          "typeName": "ZodObject"
        },
        "~standard": {
          "version": 1,
          "vendor": "zod"
        },
        "_cached": null
      }
    },
    {
      "name": "subtract",
      "inputSchema": {
        "type": "object",
        "properties": {
          "a": {
            "type": "number"
          },
          "b": {
            "type": "number"
          }
        },
        "required": [
          "a",
          "b"
        ],
        "additionalProperties": false,
        "$schema": "http://json-schema.org/draft-07/schema#"
      },
      "rawSchema": {
        "_def": {
          "unknownKeys": "strip",
          "catchall": {
            "_def": {
              "typeName": "ZodNever"
            },
            "~standard": {
              "version": 1,
              "vendor": "zod"
            }
          },
          "typeName": "ZodObject"
        },
        "~standard": {
          "version": 1,
          "vendor": "zod"
        },
        "_cached": null
      }
    }
  ]
}
```

הפעלת כלי:

```sh
npx @modelcontextprotocol/inspector --cli node ./build/app.js --method tools/call --tool-name add --tool-arg a=1 --tool-arg b=2
```

אתם אמורים לראות תגובה דומה ל:

```text
{
  "content": [
    {
      "type": "text",
      "text": "Tool add called with arguments: {\"a\":1,\"b\":2}, result: {\"content\":[{\"type\":\"text\",\"text\":\"3\"}]}"
    }
  ]
```

נסו לבדוק כלי שלא קיים כמו "add2" עם הפקודה הזו:

```sh
npx @modelcontextprotocol/inspector --cli node ./build/app.js --method tools/call --tool-name add2 --tool-arg a=1 --tool-arg b=2
```

כעת אתם אמורים לראות את ההודעה הזו שמראה שהאימות שלכם עובד:

```text
{
  "content": [],
  "error": {
    "code": "tool_not_found",
    "message": "Tool add2 not found."
  }
```

נסו גם לשלוח פרמטר `c` שאמור להידחות על ידי הסכימה, כך:

```sh
npx @modelcontextprotocol/inspector --cli node ./build/app.js --method tools/call --tool-name add --tool-arg a=1 --tool-arg c=2
```

כעת אתם אמורים לראות שגיאה של "ארגומנטים לא חוקיים":

```text
{
  "content": [],
  "error": {
    "code": "invalid_arguments",
    "message": "Invalid arguments for tool add: [\n  {\n    \"code\": \"invalid_type\",\n    \"expected\": \"number\",\n    \"received\": \"undefined\",\n    \"path\": [\n      \"b\"\n    ],\n    \"message\": \"Required\"\n  }\n]"
  }
}
```

---

**כתב ויתור**:  
מסמך זה תורגם באמצעות שירות תרגום מבוסס בינה מלאכותית [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון שתרגומים אוטומטיים עשויים להכיל שגיאות או אי דיוקים. המסמך המקורי בשפתו המקורית צריך להיחשב כמקור הסמכותי. עבור מידע קריטי, מומלץ להשתמש בתרגום מקצועי על ידי אדם. אנו לא נושאים באחריות לאי הבנות או לפרשנויות שגויות הנובעות משימוש בתרגום זה.