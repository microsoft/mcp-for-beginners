# خدمة الآلة الحاسبة الأساسية MCP

تقدم هذه الخدمة عمليات الآلة الحاسبة الأساسية من خلال بروتوكول سياق النموذج (MCP). تم تصميمها كمثال بسيط للمبتدئين الذين يتعلمون عن تطبيقات MCP.

لمزيد من المعلومات، راجع [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk)

## الميزات

تقدم خدمة الآلة الحاسبة هذه القدرات التالية:

1. **العمليات الحسابية الأساسية**:
   - جمع رقمين
   - طرح رقم من رقم آخر
   - ضرب رقمين
   - قسمة رقم على آخر (مع التحقق من القسمة على الصفر)

## استخدام نوع `stdio`
  
## التهيئة

1. **تهيئة خوادم MCP**:
   - افتح مساحة العمل الخاصة بك في VS Code.
   - أنشئ ملف `.vscode/mcp.json` في مجلد مساحة العمل لتهيئة خوادم MCP. مثال على التهيئة:

     ```jsonc
     {
       "inputs": [
         {
           "type": "promptString",
           "id": "repository-root",
           "description": "The absolute path to the repository root"
         }
       ],
       "servers": {
         "calculator-mcp-dotnet": {
           "type": "stdio",
           "command": "dotnet",
           "args": [
             "run",
             "--project",
             "${input:repository-root}/03-GettingStarted/samples/csharp/src/calculator.csproj"
           ]
         }
       }
     }
     ```

   - سيُطلب منك إدخال جذر مستودع GitHub، والذي يمكن الحصول عليه من الأمر `git rev-parse --show-toplevel`.

## استخدام الخدمة

تقدم الخدمة نقاط نهاية API التالية عبر بروتوكول MCP:

- `add(a, b)`: جمع رقمين معًا
- `subtract(a, b)`: طرح الرقم الثاني من الأول
- `multiply(a, b)`: ضرب رقمين
- `divide(a, b)`: قسمة الرقم الأول على الثاني (مع التحقق من الصفر)
- isPrime(n): التحقق مما إذا كان الرقم أوليًا

## الاختبار مع Github Copilot Chat في VS Code

1. جرب إرسال طلب إلى الخدمة باستخدام بروتوكول MCP. على سبيل المثال، يمكنك أن تطلب:
   - "Add 5 and 3"
   - "Subtract 10 from 4"
   - "Multiply 6 and 7"
   - "Divide 8 by 2"
   - "Does 37854 prime?"
   - "What are the 3 prime numbers before after 4242?"
2. للتأكد من استخدام الأدوات، أضف #MyCalculator إلى الطلب. على سبيل المثال:
   - "Add 5 and 3 #MyCalculator"
   - "Subtract 10 from 4 #MyCalculator"

## النسخة المحوسبة بالحاويات

الحل السابق ممتاز عندما يكون لديك .NET SDK مثبتًا وجميع التبعيات متوفرة. ومع ذلك، إذا كنت ترغب في مشاركة الحل أو تشغيله في بيئة مختلفة، يمكنك استخدام النسخة المحوسبة بالحاويات.

1. شغّل Docker وتأكد من أنه يعمل.
1. من الطرفية، انتقل إلى المجلد `03-GettingStarted\samples\csharp\src`
1. لبناء صورة Docker لخدمة الآلة الحاسبة، نفذ الأمر التالي (استبدل `<YOUR-DOCKER-USERNAME>` باسم مستخدم Docker Hub الخاص بك):
   ```bash
   docker build -t <YOUR-DOCKER-USERNAME>/mcp-calculator .
   ``` 
1. بعد بناء الصورة، لنرفعها إلى Docker Hub. نفذ الأمر التالي:
   ```bash
    docker push <YOUR-DOCKER-USERNAME>/mcp-calculator
  ```

## استخدام النسخة المحوسبة بالحاويات

1. في ملف `.vscode/mcp.json`، استبدل تهيئة الخادم بالتالي:
   ```json
    "mcp-calc": {
      "command": "docker",
      "args": [
        "run",
        "--rm",
        "-i",
        "<YOUR-DOCKER-USERNAME>/mcp-calc"
      ],
      "envFile": "",
      "env": {}
    }
   ```
   بالنظر إلى التهيئة، يمكنك رؤية أن الأمر هو `docker` والوسائط هي `run --rm -i <YOUR-DOCKER-USERNAME>/mcp-calc`. العلم `--rm` يضمن إزالة الحاوية بعد توقفها، والعلم `-i` يسمح لك بالتفاعل مع الإدخال القياسي للحاوية. الوسيط الأخير هو اسم الصورة التي بنيناها ورفعناها إلى Docker Hub.

## اختبار النسخة المحوسبة بالحاويات

ابدأ خادم MCP بالنقر على زر البدء الصغير فوق `"mcp-calc": {`، ومثل السابق يمكنك أن تطلب من خدمة الآلة الحاسبة إجراء بعض العمليات الحسابية لك.

**إخلاء المسؤولية**:  
تمت ترجمة هذا المستند باستخدام خدمة الترجمة الآلية [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى لتحقيق الدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الموثوق به. للمعلومات الهامة، يُنصح بالاعتماد على الترجمة البشرية المهنية. نحن غير مسؤولين عن أي سوء فهم أو تفسير ناتج عن استخدام هذه الترجمة.