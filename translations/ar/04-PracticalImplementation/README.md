# التنفيذ العملي

[![كيفية بناء واختبار ونشر تطبيقات MCP باستخدام أدوات وسير عمل حقيقي](../../../translated_images/ar/05.64bea204e25ca891.webp)](https://youtu.be/vCN9-mKBDfQ)

_(انقر على الصورة أعلاه لمشاهدة فيديو هذا الدرس)_

التنفيذ العملي هو المكان الذي يصبح فيه قوة بروتوكول سياق النموذج (MCP) ملموسة. بينما يعد فهم النظرية والهندسة المعمارية وراء MCP أمرًا مهمًا، تظهر القيمة الحقيقية عندما تطبق هذه المفاهيم لبناء واختبار ونشر حلول تحل مشاكل العالم الحقيقي. يجسر هذا الفصل الفجوة بين المعرفة المفاهيمية والتطوير العملي، موجّهًا إياك خلال عملية إحياء تطبيقات تعتمد على MCP.

سواء كنت تطور مساعدين ذكيين، تدمج الذكاء الاصطناعي في سير العمل التجاري، أو تبني أدوات مخصصة لمعالجة البيانات، يوفر MCP أساسًا مرنًا. تصميمه غير المرتبط بلغة معينة وواجهات برمجة التطبيقات الرسمية للغات البرمجة الشائعة تجعله متاحًا لمجموعة واسعة من المطورين. من خلال الاستفادة من هذه الـ SDKs، يمكنك بسرعة إنشاء نماذج أولية، وتكرار، وتوسيع حلولك عبر منصات وبيئات مختلفة.

في الأقسام التالية، ستجد أمثلة عملية، وأكواد تجريبية، واستراتيجيات نشر تظهر كيفية تنفيذ MCP في C#، Java مع Spring، TypeScript، JavaScript، وPython. ستتعلم أيضًا كيفية تصحيح الأخطاء واختبار خوادم MCP، إدارة APIs، ونشر الحلول على السحابة باستخدام Azure. هذه الموارد العملية مصممة لتسريع تعلمك ومساعدتك على بناء تطبيقات MCP متينة وجاهزة للإنتاج بثقة.

## نظرة عامة

يركز هذا الدرس على الجوانب العملية لتنفيذ MCP عبر لغات برمجة متعددة. سنستكشف كيفية استخدام MCP SDKs في C#، Java مع Spring، TypeScript، JavaScript، وPython لبناء تطبيقات قوية، تصحيح واختبار خوادم MCP، وإنشاء موارد، ونماذج استدعاء، وأدوات قابلة لإعادة الاستخدام.

## أهداف التعلم

بنهاية هذا الدرس، ستكون قادرًا على:

- تنفيذ حلول MCP باستخدام SDKs الرسمية في لغات برمجة متنوعة
- تصحيح واختبار خوادم MCP بشكل منهجي
- إنشاء واستخدام ميزات الخادم (الموارد، النماذج، والأدوات)
- تصميم سير عمل فعال لـ MCP للمهام المعقدة
- تحسين تنفيذ MCP للأداء والموثوقية

## موارد SDK الرسمية

يقدم بروتوكول سياق النموذج SDKs رسمية لعدة لغات (متوافقة مع [مواصفة MCP 2025-11-25](https://spec.modelcontextprotocol.io/specification/2025-11-25/)):

- [SDK لـ C#](https://github.com/modelcontextprotocol/csharp-sdk)
- [SDK لـ Java مع Spring](https://github.com/modelcontextprotocol/java-sdk) **ملاحظة:** يتطلب اعتمادًا على [Project Reactor](https://projectreactor.io). (راجع [نقاش المسألة 246](https://github.com/orgs/modelcontextprotocol/discussions/246).)
- [SDK لـ TypeScript](https://github.com/modelcontextprotocol/typescript-sdk)
- [SDK لـ Python](https://github.com/modelcontextprotocol/python-sdk)
- [SDK لـ Kotlin](https://github.com/modelcontextprotocol/kotlin-sdk)
- [SDK لـ Go](https://github.com/modelcontextprotocol/go-sdk)

## العمل مع SDKs الخاصة بـ MCP

يوفر هذا القسم أمثلة عملية لتنفيذ MCP عبر عدة لغات برمجة. يمكنك العثور على عينات الأكواد في دليل `samples` المصنفة حسب اللغة.

### العينات المتاحة

يتضمن المستودع [تنفيذات نموذجية](../../../04-PracticalImplementation/samples) باللغات التالية:

- [C#](./samples/csharp/README.md)
- [Java مع Spring](./samples/java/containerapp/README.md)
- [TypeScript](./samples/typescript/README.md)
- [JavaScript](./samples/javascript/README.md)
- [Python](./samples/python/README.md)

كل عينة توضح مفاهيم MCP الأساسية وأنماط التنفيذ الخاصة بتلك اللغة والنظام البيئي.

### أدلة عملية

أدلة إضافية لتطبيق عملي لـ MCP:

- [التصفح الصفحي ومجموعات النتائج الكبيرة](./pagination/README.md) - التعامل مع التصفح باستخدام مؤشرات للمصادر والأدوات ومجموعات البيانات الكبيرة

## ميزات الخادم الأساسية

يمكن لخوادم MCP تنفيذ أي مزيج من هذه الميزات:

### الموارد

توفر الموارد سياقًا وبيانات للاستخدام من قبل المستخدم أو النموذج الذكي:

- مستودعات المستندات
- قواعد المعرفة
- مصادر البيانات المنظمة
- نظم الملفات

### النماذج

النماذج هي رسائل ونماذج سير عمل نموذجية للمستخدمين:

- قوالب محادثات محددة مسبقًا
- أنماط تفاعل موجهة
- هياكل حوار متخصصة

### الأدوات

الأدوات هي دوال قابلة للتنفيذ من قبل النموذج الذكي:

- أدوات معالجة البيانات
- تكاملات API خارجية
- قدرات حسابية
- وظائف البحث

## عينات التنفيذ: تنفيذ C#

يحتوي مستودع SDK الرسمي لـ C# على عدة عينات تنفيذية توضح جوانب مختلفة من MCP:

- **عميل MCP أساسي**: مثال بسيط يظهر كيفية إنشاء عميل MCP واستدعاء أدوات
- **خادم MCP أساسي**: تنفيذ خادم بسيط مع تسجيل أدوات أساسي
- **خادم MCP متقدم**: خادم كامل الميزات مع تسجيل الأدوات، المصادقة، والتعامل مع الأخطاء
- **تكامل ASP.NET**: أمثلة توضح التكامل مع ASP.NET Core
- **أنماط تنفيذ الأدوات**: أنماط مختلفة لتنفيذ الأدوات بمستويات تعقيد متعددة

SDK الخاص بـ MCP لـ C# في مرحلة المعاينة وقد تتغير واجهات برمجة التطبيقات. سنقوم بتحديث هذا المدونة باستمرار مع تطور SDK.

### الميزات الرئيسية

- [C# MCP Nuget ModelContextProtocol](https://www.nuget.org/packages/ModelContextProtocol)
- بناء [أول خادم MCP الخاص بك](https://devblogs.microsoft.com/dotnet/build-a-model-context-protocol-mcp-server-in-csharp/).

للحصول على عينات تنفيذ كاملة لـ C#، توجه إلى [مستودع عينات SDK الرسمي لـ C#](https://github.com/modelcontextprotocol/csharp-sdk)

## عينة التنفيذ: تنفيذ Java مع Spring

يوفر SDK لـ Java مع Spring خيارات تنفيذ MCP قوية بميزات على مستوى المؤسسات.

### الميزات الرئيسية

- تكامل مع Spring Framework
- أمان نوعي قوي
- دعم البرمجة التفاعلية
- معالجة شاملة للأخطاء

للحصول على عينة تنفيذ كاملة لـ Java مع Spring، انظر [عينة Java مع Spring](samples/java/containerapp/README.md) في دليل العينات.

## عينة التنفيذ: تنفيذ JavaScript

يقدم SDK لـ JavaScript نهجًا خفيف الوزن ومرنًا لتنفيذ MCP.

### الميزات الرئيسية

- دعم Node.js والمتصفحات
- واجهة برمجة تطبيقات تعتمد على الوعود (Promises)
- تكامل سهل مع Express وأطر عمل أخرى
- دعم WebSocket للبث

للحصول على عينة تنفيذ كاملة لـ JavaScript، انظر [عينة JavaScript](samples/javascript/README.md) في دليل العينات.

## عينة التنفيذ: تنفيذ Python

يقدم SDK لـ Python نهجًا بيثونيًا لتنفيذ MCP مع تكامل ممتاز مع أُطُر تعلم الآلة.

### الميزات الرئيسية

- دعم async/await مع asyncio
- تكامل FastAPI
- تسجيل أدوات بسيط
- تكامل أصلي مع مكتبات تعلم آلة شائعة

للحصول على عينة تنفيذ كاملة لـ Python، انظر [عينة Python](samples/python/README.md) في دليل العينات.

## إدارة API

تعد إدارة API عبر Azure إجابة ممتازة على كيفية تأمين خوادم MCP. الفكرة هي وضع مثيل إدارة API من Azure أمام خادم MCP الخاص بك وتركه يتعامل مع الميزات التي قد ترغب بها مثل:

- تحديد معدلات الاستخدام
- إدارة الرموز (Tokens)
- المراقبة
- موازنة التحميل
- الأمان

### عينة Azure

هنا عينة Azure تقوم بذلك بالضبط، أي [إنشاء خادم MCP وتأمينه باستخدام إدارة API من Azure](https://github.com/Azure-Samples/remote-mcp-apim-functions-python).

راجع كيف يتم تدفق التفويض في الصورة أدناه:

![APIM-MCP](https://github.com/Azure-Samples/remote-mcp-apim-functions-python/blob/main/mcp-client-authorization.gif?raw=true)

في الصورة السابقة، يحدث ما يلي:

- تتم المصادقة/التفويض باستخدام Microsoft Entra.
- تعمل إدارة API من Azure كبوابة وتستخدم السياسات لتوجيه وإدارة حركة المرور.
- يقوم Azure Monitor بتسجيل كل الطلبات للتحليل لاحقًا.

#### تدفق التفويض

لنلقِ نظرة أكثر تفصيلاً على تدفق التفويض:

![Sequence Diagram](https://github.com/Azure-Samples/remote-mcp-apim-functions-python/blob/main/infra/app/apim-oauth/diagrams/images/mcp-client-auth.png?raw=true)

#### مواصفة تفويض MCP

تعرف أكثر على [مواصفة تفويض MCP](https://spec.modelcontextprotocol.io/specification/2025-11-25/basic/authorization/)

## نشر خادم MCP عن بُعد إلى Azure

لنرَ هل يمكننا نشر العينة التي ذكرناها سابقًا:

1. استنساخ المستودع

    ```bash
    git clone https://github.com/Azure-Samples/remote-mcp-apim-functions-python.git
    cd remote-mcp-apim-functions-python
    ```

1. تسجيل مزود الموارد `Microsoft.App`.

   - إذا كنت تستخدم Azure CLI، شغل الأمر `az provider register --namespace Microsoft.App --wait`.
   - إذا كنت تستخدم Azure PowerShell، شغل الأمر `Register-AzResourceProvider -ProviderNamespace Microsoft.App`. ثم شغل `(Get-AzResourceProvider -ProviderNamespace Microsoft.App).RegistrationState` بعد فترة للتأكد من اكتمال التسجيل.

1. شغل هذا الأمر [azd](https://aka.ms/azd) لتوفير خدمة إدارة API، تطبيق الوظائف (مع الكود) وجميع موارد Azure المطلوبة الأخرى.

    ```shell
    azd up
    ```

    يجب أن تنشر هذه الأوامر كل موارد السحابة على Azure

### اختبار الخادم الخاص بك باستخدام MCP Inspector

1. في **نافذة طرفية جديدة**، ثبت وشغل MCP Inspector

    ```shell
    npx @modelcontextprotocol/inspector
    ```

    يجب أن ترى واجهة مشابهة لـ:

    ![Connect to Node inspector](../../../translated_images/ar/connect.141db0b2bd05f096.webp)

1. اضغط CTRL وانقر لتحميل تطبيق MCP Inspector من عنوان URL المعروض بواسطة التطبيق (مثلاً [http://127.0.0.1:6274/#resources](http://127.0.0.1:6274/#resources))
1. اضبط نوع النقل على `SSE`
1. اضبط عنوان URL إلى نقطة النهاية SSE الخاصة بإدارة API التي تعمل لديك والمعروضة بعد تشغيل `azd up` و**اتصل**:

    ```shell
    https://<apim-servicename-from-azd-output>.azure-api.net/mcp/sse
    ```

1. **قائمة الأدوات**. انقر على أداة و**شغل الأداة**.

إذا سارت كل الخطوات بنجاح، ينبغي الآن أن تكون متصلاً بخادم MCP وقد تمكنت من استدعاء أداة.

## خوادم MCP لـ Azure

[Remote-mcp-functions](https://github.com/Azure-Samples/remote-mcp-functions-dotnet): مجموعة من المستودعات كنماذج بداية سريعة لبناء ونشر خوادم MCP (بروتوكول سياق النموذج) عن بُعد مخصصة باستخدام Azure Functions مع Python، C# .NET أو Node/TypeScript.

تقدم العينات حلاً كاملاً يمكّن المطورين من:

- البناء والتشغيل محليًا: تطوير وتصحيح خادم MCP على جهاز محلي
- النشر إلى Azure: سهولة النشر إلى السحابة بأمر بسيط `azd up`
- الاتصال من العملاء: الاتصال بخادم MCP من عملاء متنوعين بما في ذلك وضع عميل Copilot في VS Code وأداة MCP Inspector

### الميزات الرئيسية

- الأمان مصمم منذ البداية: يتم تأمين خادم MCP باستخدام مفاتيح و HTTPS
- خيارات المصادقة: تدعم OAuth باستخدام المصادقة المدمجة و/أو إدارة API
- عزل الشبكة: يسمح بعزل الشبكة باستخدام الشبكات الافتراضية لـ Azure (VNET)
- هندسة بدون خادم: تستفيد من Azure Functions للتنفيذ القابل للتوسع المعتمد على الأحداث
- التطوير المحلي: دعم شامل للتطوير المحلي وتصحيح الأخطاء
- النشر البسيط: عملية نشر مصممة ببساطة إلى Azure

يتضمن المستودع كل ملفات التكوين، شفرة المصدر، وتعريفات البنية التحتية اللازمة للبدء سريعًا بتنفيذ خادم MCP جاهز للإنتاج.

- [Azure Remote MCP Functions Python](https://github.com/Azure-Samples/remote-mcp-functions-python) - تنفيذ عينة لـ MCP باستخدام Azure Functions مع Python

- [Azure Remote MCP Functions .NET](https://github.com/Azure-Samples/remote-mcp-functions-dotnet) - تنفيذ عينة لـ MCP باستخدام Azure Functions مع C# .NET

- [Azure Remote MCP Functions Node/Typescript](https://github.com/Azure-Samples/remote-mcp-functions-typescript) - تنفيذ عينة لـ MCP باستخدام Azure Functions مع Node/TypeScript.

## النقاط الأساسية

- توفر SDKs الخاصة بـ MCP أدوات مرتبطة باللغات لتنفيذ حلول MCP متينة
- عملية التصحيح والاختبار حاسمة لتطبيقات MCP موثوقة
- نماذج النماذج القابلة لإعادة الاستخدام تتيح تفاعلات ذكاء اصطناعي متسقة
- سير العمل المصمم جيدًا يمكن أن ينسق مهامًا معقدة باستخدام عدة أدوات
- تنفيذ حلول MCP يتطلب النظر في الأمان، الأداء، والتعامل مع الأخطاء

## تمرين

صمم سير عمل MCP عملي يعالج مشكلة واقعية في مجالك:

1. حدد 3-4 أدوات ستكون مفيدة لحل هذه المشكلة
2. أنشئ مخطط سير عمل يظهر كيف تتفاعل هذه الأدوات
3. نفذ نسخة أساسية من إحدى الأدوات باستخدام لغتك المفضلة
4. أنشئ نموذج استدعاء يساعد النموذج على استخدام أداتك بفعالية

## موارد إضافية

---

## ما التالي

التالي: [موضوعات متقدمة](../05-AdvancedTopics/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**تنويه**:
تمت ترجمة هذا المستند باستخدام خدمة الترجمة بالذكاء الاصطناعي [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى لتحقيق الدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار الوثيقة الأصلية بلغتها الأصلية المصدر المعتمد. للمعلومات الحرجة، يُنصح بالاعتماد على ترجمة بشرية مهنية. نحن غير مسؤولين عن أي سوء فهم أو تفسير ناتج عن استخدام هذه الترجمة.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->