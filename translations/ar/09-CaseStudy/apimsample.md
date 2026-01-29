# دراسة حالة: كشف واجهة برمجة التطبيقات REST في إدارة واجهات برمجة التطبيقات كخادم MCP

تُعد خدمة Azure API Management بوابة تُضاف فوق نقاط نهاية واجهات برمجة التطبيقات الخاصة بك. تعمل هذه الخدمة كوكيل أمام واجهات برمجة التطبيقات الخاصة بك وتقرر كيفية التعامل مع الطلبات الواردة.

باستخدامها، يمكنك إضافة مجموعة واسعة من الميزات مثل:

- **الأمان**، حيث يمكنك استخدام كل شيء بدءًا من مفاتيح واجهات برمجة التطبيقات (API keys) وJWT وصولاً إلى الهوية المُدارة.
- **تحديد معدل الطلبات**، وهي ميزة رائعة تتيح لك تحديد عدد الطلبات التي يمكن معالجتها خلال وحدة زمنية معينة. يساعد ذلك في ضمان تجربة ممتازة لجميع المستخدمين وحماية خدمتك من التحميل الزائد.
- **التوسع وتوزيع الأحمال**. يمكنك إعداد عدد من نقاط النهاية لتوزيع الأحمال، كما يمكنك تحديد كيفية "توزيع الأحمال".
- **ميزات الذكاء الاصطناعي مثل التخزين المؤقت الدلالي**، وحدود الرموز، ومراقبة الرموز والمزيد. هذه الميزات تعزز الاستجابة وتساعدك على إدارة استهلاك الرموز. [اقرأ المزيد هنا](https://learn.microsoft.com/en-us/azure/api-management/genai-gateway-capabilities).

## لماذا MCP + Azure API Management؟

يُعد بروتوكول Model Context Protocol معيارًا سريع الانتشار لتطبيقات الذكاء الاصطناعي الوكيلية وكيفية كشف الأدوات والبيانات بطريقة متسقة. تُعتبر Azure API Management خيارًا طبيعيًا عندما تحتاج إلى "إدارة" واجهات برمجة التطبيقات. غالبًا ما تتكامل خوادم MCP مع واجهات برمجة تطبيقات أخرى لمعالجة الطلبات، مما يجعل الجمع بين Azure API Management وMCP منطقيًا للغاية.

## نظرة عامة

في هذه الحالة العملية، سنتعلم كيفية كشف نقاط نهاية واجهات برمجة التطبيقات كخادم MCP. من خلال القيام بذلك، يمكننا بسهولة جعل هذه النقاط جزءًا من تطبيق وكيل مع الاستفادة من ميزات Azure API Management.

## الميزات الرئيسية

- يمكنك اختيار طرق نقاط النهاية التي تريد كشفها كأدوات.
- الميزات الإضافية التي تحصل عليها تعتمد على ما تقوم بتكوينه في قسم السياسات لواجهة برمجة التطبيقات الخاصة بك. ولكن هنا سنوضح كيفية إضافة تحديد معدل الطلبات.

## الخطوة التمهيدية: استيراد واجهة برمجة التطبيقات

إذا كانت لديك واجهة برمجة تطبيقات في Azure API Management بالفعل، يمكنك تخطي هذه الخطوة. إذا لم يكن لديك، تحقق من هذا الرابط، [استيراد واجهة برمجة تطبيقات إلى Azure API Management](https://learn.microsoft.com/en-us/azure/api-management/import-and-publish#import-and-publish-a-backend-api).

## كشف واجهة برمجة التطبيقات كخادم MCP

لكشف نقاط نهاية واجهة برمجة التطبيقات، اتبع الخطوات التالية:

1. انتقل إلى بوابة Azure عبر العنوان التالي <https://portal.azure.com/?Microsoft_Azure_ApiManagement=mcp> 
   وانتقل إلى مثيل إدارة واجهات برمجة التطبيقات الخاص بك.

1. في القائمة اليسرى، اختر APIs > MCP Servers > + Create new MCP Server.

1. في API، اختر واجهة برمجة تطبيقات REST للكشف عنها كخادم MCP.

1. اختر عملية أو أكثر من عمليات واجهة برمجة التطبيقات للكشف عنها كأدوات. يمكنك اختيار جميع العمليات أو عمليات محددة فقط.

    ![اختيار الطرق للكشف عنها](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/create-mcp-server-small.png)

1. اختر **إنشاء**.

1. انتقل إلى خيار القائمة **APIs** و**MCP Servers**، يجب أن ترى ما يلي:

    ![عرض خادم MCP في اللوحة الرئيسية](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-list.png)

    تم إنشاء خادم MCP وتم كشف عمليات واجهة برمجة التطبيقات كأدوات. يتم إدراج خادم MCP في لوحة MCP Servers. تعرض عمود URL نقطة نهاية خادم MCP التي يمكنك استدعاؤها للاختبار أو ضمن تطبيق العميل.

## اختياري: تكوين السياسات

تحتوي Azure API Management على مفهوم أساسي يُعرف بالسياسات، حيث يمكنك إعداد قواعد مختلفة لنقاط النهاية الخاصة بك مثل تحديد معدل الطلبات أو التخزين المؤقت الدلالي. يتم تأليف هذه السياسات بتنسيق XML.

إليك كيفية إعداد سياسة لتحديد معدل الطلبات لخادم MCP الخاص بك:

1. في البوابة، ضمن APIs، اختر **MCP Servers**.

1. اختر خادم MCP الذي أنشأته.

1. في القائمة اليسرى، ضمن MCP، اختر **Policies**.

1. في محرر السياسات، أضف أو عدّل السياسات التي تريد تطبيقها على أدوات خادم MCP. يتم تعريف السياسات بتنسيق XML. على سبيل المثال، يمكنك إضافة سياسة لتحديد عدد الطلبات إلى أدوات خادم MCP (في هذا المثال، 5 طلبات لكل 30 ثانية لكل عنوان IP للعميل). إليك XML الذي سيؤدي إلى تحديد معدل الطلبات:

    ```xml
     <rate-limit-by-key calls="5" 
       renewal-period="30" 
       counter-key="@(context.Request.IpAddress)" 
       remaining-calls-variable-name="remainingCallsPerIP" 
    />
    ```

    إليك صورة لمحرر السياسات:

    ![محرر السياسات](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-policies-small.png)

## جربه

لنتأكد من أن خادم MCP يعمل كما هو متوقع.

لهذا، سنستخدم Visual Studio Code وGitHub Copilot ووضع الوكيل الخاص به. سنضيف خادم MCP إلى ملف *mcp.json*. من خلال القيام بذلك، سيعمل Visual Studio Code كعميل بقدرات وكيلة، وسيتمكن المستخدمون النهائيون من كتابة طلبات والتفاعل مع هذا الخادم.

إليك كيفية إضافة خادم MCP في Visual Studio Code:

1. استخدم الأمر MCP: **Add Server من Command Palette**.

1. عند الطلب، اختر نوع الخادم: **HTTP (HTTP أو Server Sent Events)**.

1. أدخل عنوان URL لخادم MCP في إدارة واجهات برمجة التطبيقات. مثال: **https://<apim-service-name>.azure-api.net/<api-name>-mcp/sse** (لنقطة نهاية SSE) أو **https://<apim-service-name>.azure-api.net/<api-name>-mcp/mcp** (لنقطة نهاية MCP)، لاحظ الفرق بين النقلين هو `/sse` أو `/mcp`.

1. أدخل معرف خادم من اختيارك. هذا ليس قيمة مهمة ولكنه سيساعدك على تذكر ما هو هذا الخادم.

1. اختر ما إذا كنت تريد حفظ التكوين في إعدادات مساحة العمل أو إعدادات المستخدم.

  - **إعدادات مساحة العمل** - يتم حفظ تكوين الخادم في ملف .vscode/mcp.json المتاح فقط في مساحة العمل الحالية.

    *mcp.json*

    ```json
    "servers": {
        "APIM petstore" : {
            "type": "sse",
            "url": "url-to-mcp-server/sse"
        }
    }
    ```

    أو إذا اخترت HTTP كوسيلة نقل، فسيكون مختلفًا قليلاً:

    ```json
    "servers": {
        "APIM petstore" : {
            "type": "http",
            "url": "url-to-mcp-server/mcp"
        }
    }
    ```

  - **إعدادات المستخدم** - يتم إضافة تكوين الخادم إلى ملف *settings.json* العالمي الخاص بك ويكون متاحًا في جميع مساحات العمل. يبدو التكوين مشابهًا لما يلي:

    ![إعداد المستخدم](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-servers-visual-studio-code.png)

1. تحتاج أيضًا إلى إضافة تكوين، وهو رأس للتأكد من المصادقة بشكل صحيح تجاه Azure API Management. يستخدم رأسًا يسمى **Ocp-Apim-Subscription-Key**.

    - إليك كيفية إضافته إلى الإعدادات:

    ![إضافة رأس للمصادقة](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-with-header-visual-studio-code.png)، سيؤدي ذلك إلى عرض طلب يطلب منك قيمة مفتاح API التي يمكنك العثور عليها في بوابة Azure لمثيل Azure API Management الخاص بك.

   - لإضافته إلى *mcp.json* بدلاً من ذلك، يمكنك إضافته كما يلي:

    ```json
    "inputs": [
      {
        "type": "promptString",
        "id": "apim_key",
        "description": "API Key for Azure API Management",
        "password": true
      }
    ]
    "servers": {
        "APIM petstore" : {
            "type": "http",
            "url": "url-to-mcp-server/mcp",
            "headers": {
                "Ocp-Apim-Subscription-Key": "Bearer ${input:apim_key}"
            }
        }
    }
    ```

### استخدام وضع الوكيل

الآن نحن جاهزون تمامًا سواء في الإعدادات أو في *.vscode/mcp.json*. لنجرّب.

يجب أن يكون هناك رمز أدوات مثل هذا، حيث يتم إدراج الأدوات المكشوفة من خادمك:

![الأدوات من الخادم](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/tools-button-visual-studio-code.png)

1. انقر على رمز الأدوات ويجب أن ترى قائمة بالأدوات مثل هذه:

    ![الأدوات](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/select-tools-visual-studio-code.png)

1. أدخل طلبًا في الدردشة لاستدعاء الأداة. على سبيل المثال، إذا اخترت أداة للحصول على معلومات حول طلب، يمكنك أن تسأل الوكيل عن الطلب. إليك مثال على طلب:

    ```text
    get information from order 2
    ```

    ستظهر لك الآن أيقونة أدوات تطلب منك المتابعة لاستدعاء أداة. اختر متابعة تشغيل الأداة، وسترى الآن نتيجة مثل هذه:

    ![نتيجة الطلب](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/chat-results-visual-studio-code.png)

    **ما تراه أعلاه يعتمد على الأدوات التي قمت بإعدادها، ولكن الفكرة هي أنك تحصل على استجابة نصية مثل ما سبق.**

## المراجع

إليك كيفية معرفة المزيد:

- [دليل حول Azure API Management وMCP](https://learn.microsoft.com/en-us/azure/api-management/export-rest-mcp-server)
- [مثال Python: تأمين خوادم MCP البعيدة باستخدام Azure API Management (تجريبي)](https://github.com/Azure-Samples/remote-mcp-apim-functions-python)

- [مختبر تفويض عميل MCP](https://github.com/Azure-Samples/AI-Gateway/tree/main/labs/mcp-client-authorization)

- [استخدام ملحق Azure API Management لـ VS Code لاستيراد وإدارة واجهات برمجة التطبيقات](https://learn.microsoft.com/en-us/azure/api-management/visual-studio-code-tutorial)

- [تسجيل واكتشاف خوادم MCP البعيدة في Azure API Center](https://learn.microsoft.com/en-us/azure/api-center/register-discover-mcp-server)
- [بوابة الذكاء الاصطناعي](https://github.com/Azure-Samples/AI-Gateway) مستودع رائع يعرض العديد من قدرات الذكاء الاصطناعي مع Azure API Management
- [ورش عمل بوابة الذكاء الاصطناعي](https://azure-samples.github.io/AI-Gateway/) تحتوي على ورش عمل باستخدام بوابة Azure، وهي طريقة رائعة لبدء تقييم قدرات الذكاء الاصطناعي.

**إخلاء المسؤولية**:  
تم ترجمة هذا المستند باستخدام خدمة الترجمة بالذكاء الاصطناعي [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى لتحقيق الدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو معلومات غير دقيقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الموثوق. للحصول على معلومات حاسمة، يُوصى بالاستعانة بترجمة بشرية احترافية. نحن غير مسؤولين عن أي سوء فهم أو تفسيرات خاطئة تنشأ عن استخدام هذه الترجمة.