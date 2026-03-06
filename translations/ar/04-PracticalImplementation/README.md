# التنفيذ العملي

[![كيفية بناء واختبار ونشر تطبيقات MCP باستخدام أدوات حقيقية وسير عمل](../../../translated_images/ar/05.64bea204e25ca891.webp)](https://youtu.be/vCN9-mKBDfQ)

_(انقر على الصورة أعلاه لمشاهدة فيديو هذا الدرس)_

التنفيذ العملي هو المكان الذي يصبح فيه قوة بروتوكول سياق النموذج (MCP) ملموسة. بينما يعد فهم النظرية والهندسة المعمارية وراء MCP أمرًا مهمًا، القيمة الحقيقية تظهر عندما تطبق هذه المفاهيم لبناء واختبار ونشر حلول تحل مشاكل العالم الحقيقي. هذا الفصل يجسر الفجوة بين المعرفة المفاهيمية والتطوير العملي، ويوجهك خلال عملية إحياء التطبيقات المبنية على MCP.

سواء كنت تطور مساعدين أذكياء، أو تدمج الذكاء الاصطناعي في سير عمل الأعمال، أو تبني أدوات مخصصة لمعالجة البيانات، يوفر MCP أساسًا مرنًا. تصميمه المستقل عن اللغة وSDKs الرسمية للغات البرمجة الشائعة تجعله متاحًا لمجموعة واسعة من المطورين. باستخدام هذه SDKs، يمكنك بسرعة إنشاء نماذج أولية، وتكرار، وتوسيع حلولك عبر منصات وبيئات مختلفة.

في الأقسام التالية، ستجد أمثلة عملية، وأكواد عينة، واستراتيجيات نشر توضح كيفية تنفيذ MCP في C# وJava مع Spring، وTypeScript، وJavaScript، وPython. ستتعلم أيضًا كيفية تصحيح أخطاء واختبار خوادم MCP، وإدارة واجهات برمجة التطبيقات، ونشر الحلول إلى السحابة باستخدام Azure. هذه الموارد العملية مصممة لتسريع تعلمك ومساعدتك على بناء تطبيقات MCP قوية وجاهزة للإنتاج بثقة.

## نظرة عامة

يركز هذا الدرس على الجوانب العملية لتنفيذ MCP عبر لغات برمجة متعددة. سوف نستكشف كيفية استخدام SDKs MCP في C# وJava مع Spring، وTypeScript، وJavaScript، وPython لبناء تطبيقات متينة، وتصحيح واختبار خوادم MCP، وإنشاء موارد وقوالب وأدوات قابلة لإعادة الاستخدام.

## الأهداف التعليمية

بحلول نهاية هذا الدرس، ستكون قادرًا على:

- تنفيذ حلول MCP باستخدام SDKs الرسمية في لغات برمجة مختلفة  
- تصحيح واختبار خوادم MCP بشكل منهجي  
- إنشاء واستخدام ميزات الخادم (الموارد، القوالب، والأدوات)  
- تصميم سير عمل MCP فعال للمهام المعقدة  
- تحسين تنفيذات MCP للأداء والموثوقية  

## موارد SDK الرسمية

يقدم بروتوكول سياق النموذج SDKs رسمية لعدة لغات (مطابقة مع [مواصفات MCP 2025-11-25](https://spec.modelcontextprotocol.io/specification/2025-11-25/)):

- [SDK C#](https://github.com/modelcontextprotocol/csharp-sdk)  
- [SDK Java مع Spring](https://github.com/modelcontextprotocol/java-sdk) **ملاحظة:** يتطلب اعتمادًا على [Project Reactor](https://projectreactor.io). (انظر [مناقشة issue 246](https://github.com/orgs/modelcontextprotocol/discussions/246).)  
- [SDK TypeScript](https://github.com/modelcontextprotocol/typescript-sdk)  
- [SDK Python](https://github.com/modelcontextprotocol/python-sdk)  
- [SDK Kotlin](https://github.com/modelcontextprotocol/kotlin-sdk)  
- [SDK Go](https://github.com/modelcontextprotocol/go-sdk)  

## العمل مع SDKs MCP

يوفر هذا القسم أمثلة عملية لتنفيذ MCP عبر لغات برمجة متعددة. يمكنك العثور على أكواد عينة في دليل `samples` منظم حسب اللغة.

### العينات المتاحة

يتضمن المستودع [نماذج تنفيذ](../../../04-PracticalImplementation/samples) في اللغات التالية:

- [C#](./samples/csharp/README.md)  
- [Java مع Spring](./samples/java/containerapp/README.md)  
- [TypeScript](./samples/typescript/README.md)  
- [JavaScript](./samples/javascript/README.md)  
- [Python](./samples/python/README.md)  

كل نموذج يوضح مفاهيم MCP الرئيسية وأنماط التنفيذ لتلك اللغة والبيئة المحددة.

### الإرشادات العملية

أدلة إضافية لتنفيذ MCP العملي:

- [الترقيم ومجموعات النتائج الكبيرة](./pagination/README.md) - التعامل مع الترقيم القائم على المؤشر للأدوات، الموارد، ومجموعات البيانات الكبيرة

## الميزات الأساسية للخادم

يمكن لخوادم MCP تنفيذ أي مزيج من هذه الميزات:

### الموارد

توفر الموارد السياق والبيانات للمستخدم أو نموذج الذكاء الاصطناعي لاستخدامها:

- مستودعات الوثائق  
- قواعد المعرفة  
- مصادر البيانات المنظمة  
- أنظمة الملفات  

### القوالب

القوالب هي رسائل ونماذج سير عمل محددة للمستخدمين:

- قوالب محادثات محددة مسبقًا  
- أنماط تفاعل موجهة  
- تراكيب حوار متخصصة  

### الأدوات

الأدوات هي وظائف يقوم نموذج الذكاء الاصطناعي بتنفيذها:

- أدوات معالجة البيانات  
- تكاملات API خارجية  
- قدرات الحوسبة  
- وظيفة البحث  

## نماذج تنفيذ: تنفيذ C#

يتضمن مستودع SDK الرسمي لـC# عدة نماذج تنفيذ توضح جوانب مختلفة من MCP:

- **عميل MCP أساسي**: مثال بسيط يوضح كيفية إنشاء عميل MCP واستدعاء الأدوات  
- **خادم MCP أساسي**: تنفيذ خادم بسيط مع تسجيل أدوات أساسي  
- **خادم MCP متقدم**: خادم متكامل مع تسجيل أدوات، المصادقة، والتعامل مع الأخطاء  
- **تكامل ASP.NET**: أمثلة توضح التكامل مع ASP.NET Core  
- **أنماط تنفيذ الأدوات**: أنماط مختلفة لتنفيذ الأدوات بمستويات تعقيد مختلفة  

توجد الـ SDK لـC# في مرحلة المعاينة وقد تتغير واجهات برمجة التطبيقات. سنقوم بتحديث هذه المدونة باستمرار مع تطور SDK.

### الميزات الرئيسية

- [C# MCP Nuget ModelContextProtocol](https://www.nuget.org/packages/ModelContextProtocol)  
- بناء [أول خادم MCP الخاص بك](https://devblogs.microsoft.com/dotnet/build-a-model-context-protocol-mcp-server-in-csharp/).

للحصول على نماذج تنفيذ كاملة لـC#، تفضل بزيارة [مستودع عينات SDK C# الرسمي](https://github.com/modelcontextprotocol/csharp-sdk)

## نموذج تنفيذ: تنفيذ Java مع Spring

يوفر SDK Java مع Spring خيارات تنفيذ MCP متينة مع ميزات على مستوى المؤسسات.

### الميزات الرئيسية

- تكامل إطار Spring  
- أمان نوع قوي  
- دعم البرمجة التفاعلية  
- معالجة أخطاء شاملة  

للحصول على نموذج تنفيذ كامل لـJava مع Spring، راجع [نموذج Java مع Spring](samples/java/containerapp/README.md) في دليل العينات.

## نموذج تنفيذ: تنفيذ JavaScript

يوفر SDK JavaScript نهجًا خفيف الوزن ومرنًا لتنفيذ MCP.

### الميزات الرئيسية

- دعم Node.js والمتصفح  
- API قائم على الوعود  
- تكامل سهل مع Express وأطر عمل أخرى  
- دعم WebSocket للبث  

للحصول على نموذج تنفيذ كامل لـJavaScript، راجع [نموذج JavaScript](samples/javascript/README.md) في دليل العينات.

## نموذج تنفيذ: تنفيذ Python

يقدم SDK Python نهجًا بلغة بايثون لتنفيذ MCP مع تكاملات ممتازة لإطارات تعلم الآلة.

### الميزات الرئيسية

- دعم async/await مع asyncio  
- تكامل FastAPI  
- تسجيل أدوات بسيط  
- تكامل أصلي مع مكتبات تعلم الآلة الشهيرة  

للحصول على نموذج تنفيذ كامل لـPython، راجع [نموذج Python](samples/python/README.md) في دليل العينات.

## إدارة واجهات برمجة التطبيقات

تُعد إدارة واجهات برمجة التطبيقات في Azure إجابة رائعة على كيفية تأمين خوادم MCP. الفكرة هي وضع مثيل إدارة API من Azure أمام خادم MCP الخاص بك والسماح له بمعالجة الميزات التي من المحتمل أن تحتاجها مثل:

- تحديد معدلات الاستخدام  
- إدارة الرموز  
- المراقبة  
- توزيع الحمولة  
- الأمان  

### نموذج Azure

إليك نموذج Azure يقوم بالضبط بذلك، أي [إنشاء خادم MCP وتأمينه باستخدام إدارة API في Azure](https://github.com/Azure-Samples/remote-mcp-apim-functions-python).

شاهد كيف يتم سير ترخيص الدخول في الصورة أدناه:

![APIM-MCP](https://github.com/Azure-Samples/remote-mcp-apim-functions-python/blob/main/mcp-client-authorization.gif?raw=true)

في الصورة السابقة، يحدث التالي:

- تتم المصادقة/التفويض باستخدام Microsoft Entra.  
- تعمل إدارة API في Azure كبوابة وتستخدم السياسات لتوجيه وإدارة الحركة.  
- يقوم Azure Monitor بتسجيل كل الطلبات للتحليل المستقبلي.  

#### سير تفويض الدخول

لننظر أكثر في سير تفويض الدخول بالتفصيل:

![Sequence Diagram](https://github.com/Azure-Samples/remote-mcp-apim-functions-python/blob/main/infra/app/apim-oauth/diagrams/images/mcp-client-auth.png?raw=true)

#### مواصفة تفويض MCP

تعرف أكثر على [مواصفة تفويض MCP](https://spec.modelcontextprotocol.io/specification/2025-11-25/basic/authorization/)

## نشر خادم MCP عن بُعد على Azure

لنرَ إذا كان بإمكاننا نشر النموذج الذي ذكرناه سابقًا:

1. استنساخ المستودع

    ```bash
    git clone https://github.com/Azure-Samples/remote-mcp-apim-functions-python.git
    cd remote-mcp-apim-functions-python
    ```
  
1. تسجيل مزود الموارد `Microsoft.App`.

   - إذا كنت تستخدم Azure CLI، قم بتشغيل `az provider register --namespace Microsoft.App --wait`.  
   - إذا كنت تستخدم Azure PowerShell، قم بتشغيل `Register-AzResourceProvider -ProviderNamespace Microsoft.App`. ثم شغّل `(Get-AzResourceProvider -ProviderNamespace Microsoft.App).RegistrationState` بعد فترة للتحقق من اكتمال التسجيل.  

1. شغّل أمر [azd](https://aka.ms/azd) لتوفير خدمة إدارة API، وتطبيق الدوال (مع الكود) وجميع موارد Azure المطلوبة الأخرى

    ```shell
    azd up
    ```
  
    يجب أن تنشر هذه الأوامر كل الموارد السحابية على Azure

### اختبار الخادم باستخدام MCP Inspector

1. في **نافذة طرفية جديدة**، ثبت وشغّل MCP Inspector

    ```shell
    npx @modelcontextprotocol/inspector
    ```
  
    يجب أن ترى واجهة مشابهة لـ:

    ![الاتصال بـ Node inspector](../../../translated_images/ar/connect.141db0b2bd05f096.webp)

1. اضغط CTRL وانقر لتحميل تطبيق MCP Inspector من الرابط الذي يعرضه التطبيق (مثل [http://127.0.0.1:6274/#resources](http://127.0.0.1:6274/#resources))  
1. اضبط نوع النقل على `SSE`  
1. اضبط عنوان URL إلى نقطة نهاية SSE الخاصة بإدارة API الجارية التي تم عرضها بعد `azd up` و**اتصل**:

    ```shell
    https://<apim-servicename-from-azd-output>.azure-api.net/mcp/sse
    ```
  
1. **قائمة الأدوات**. انقر على أداة ثم **شغل الأداة**.  

إذا نجحت كل الخطوات، يجب أن تكون الآن متصلًا بخادم MCP وتمكنت من استدعاء أداة.

## خوادم MCP لـ Azure

[Remote-mcp-functions](https://github.com/Azure-Samples/remote-mcp-functions-dotnet): هذه المجموعة من المستودعات هي قالب بداية سريع لبناء ونشر خوادم MCP عن بُعد مخصصة باستخدام Azure Functions مع Python، C# .NET أو Node/TypeScript.

يوفر النموذج حلاً كاملاً يسمح للمطورين بـ:

- البناء والتشغيل محليًا: تطوير وتصحيح خادم MCP على جهاز محلي  
- النشر إلى Azure: نشر سهل إلى السحابة بأمر بسيط azd up  
- الاتصال من العملاء: الاتصال بخادم MCP من عملاء مختلفين بما في ذلك وضع الوكيل في VS Code وأداة MCP Inspector  

### الميزات الرئيسية

- الأمان حسب التصميم: خادم MCP مؤمن باستخدام المفاتيح وHTTPS  
- خيارات المصادقة: يدعم OAuth باستخدام المصادقة المدمجة و/أو إدارة API  
- عزل الشبكة: يسمح بعزل الشبكة باستخدام الشبكات الافتراضية في Azure (VNET)  
- بنية بدون خادم: يستخدم Azure Functions لتنفيذ قابل للتوسع ويعتمد الأحداث  
- تطوير محلي: دعم شامل للتطوير المحلي وتصحيح الأخطاء  
- نشر بسيط: عملية نشر مبسطة إلى Azure  

يتضمن المستودع كل ملفات التكوين الضرورية، والكود المصدري، وتعريفات البنية التحتية للبدء السريع بتنفيذ خادم MCP جاهز للإنتاج.

- [Azure Remote MCP Functions Python](https://github.com/Azure-Samples/remote-mcp-functions-python) - نموذج تنفيذ MCP باستخدام Azure Functions مع Python

- [Azure Remote MCP Functions .NET](https://github.com/Azure-Samples/remote-mcp-functions-dotnet) - نموذج تنفيذ MCP باستخدام Azure Functions مع C# .NET

- [Azure Remote MCP Functions Node/Typescript](https://github.com/Azure-Samples/remote-mcp-functions-typescript) - نموذج تنفيذ MCP باستخدام Azure Functions مع Node/TypeScript.

## النقاط الأساسية

- SDKs MCP توفر أدوات خاصة بكل لغة لتنفيذ حلول MCP متينة  
- عملية تصحيح الأخطاء والاختبار حاسمة لتطبيقات MCP موثوقة  
- قوالب تحفيز قابلة لإعادة الاستخدام تمكن تفاعلات AI متسقة  
- سير العمل المصمم جيدًا يمكنه تنسيق المهام المعقدة باستخدام أدوات متعددة  
- تنفيذ حلول MCP يتطلب النظر في الأمان، الأداء، والتعامل مع الأخطاء  

## تمرين

صمم سير عمل عملي لـ MCP يعالج مشكلة في العالم الحقيقي في مجالك:

1. حدد 3-4 أدوات ستكون مفيدة لحل هذه المشكلة  
2. أنشئ مخطط سير عمل يوضح كيف تتفاعل هذه الأدوات  
3. نفذ نسخة أساسية من إحدى الأدوات باستخدام لغتك المفضلة  
4. أنشئ قالب تحفيز يساعد النموذج على استخدام أداتك بفعالية  

## موارد إضافية

---

## ماذا بعد

التالي: [مواضيع متقدمة](../05-AdvancedTopics/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**تنويه**:  
تمت ترجمة هذا المستند باستخدام خدمة الترجمة بالذكاء الاصطناعي [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى لتحقيق الدقة، يُرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الموثوق به. بالنسبة للمعلومات الهامة، يُنصح بالترجمة المهنية البشرية. نحن غير مسؤولين عن أي سوء فهم أو تفسير ناتج عن استخدام هذه الترجمة.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->