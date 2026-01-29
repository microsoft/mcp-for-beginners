# أمان MCP المتقدم مع Azure Content Safety

يوفر Azure Content Safety عدة أدوات قوية يمكنها تعزيز أمان تطبيقات MCP الخاصة بك:

## دروع المطالبات

تقدم دروع المطالبات من Microsoft حماية قوية ضد هجمات حقن المطالبات المباشرة وغير المباشرة من خلال:

1. **الكشف المتقدم**: يستخدم التعلم الآلي لتحديد التعليمات الخبيثة المدمجة في المحتوى.
2. **التسليط الضوئي**: يحول النص المدخل لمساعدة أنظمة الذكاء الاصطناعي على التمييز بين التعليمات الصحيحة والمدخلات الخارجية.
3. **الفواصل وعلامات البيانات**: يحدد الحدود بين البيانات الموثوقة وغير الموثوقة.
4. **التكامل مع Content Safety**: يعمل مع Azure AI Content Safety لاكتشاف محاولات كسر الحماية والمحتوى الضار.
5. **التحديثات المستمرة**: تقوم Microsoft بتحديث آليات الحماية بانتظام لمواجهة التهديدات الجديدة.

## تنفيذ Azure Content Safety مع MCP

يوفر هذا النهج حماية متعددة الطبقات:
- فحص المدخلات قبل المعالجة
- التحقق من المخرجات قبل الإرجاع
- استخدام قوائم الحظر للأنماط الضارة المعروفة
- الاستفادة من نماذج Content Safety المحدثة باستمرار من Azure

## موارد Azure Content Safety

لتعلم المزيد عن كيفية تنفيذ Azure Content Safety مع خوادم MCP الخاصة بك، راجع هذه الموارد الرسمية:

1. [توثيق Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/) - التوثيق الرسمي لـ Azure Content Safety.
2. [توثيق درع المطالبات](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/prompt-shield) - تعلّم كيفية منع هجمات حقن المطالبات.
3. [مرجع API الخاص بـ Content Safety](https://learn.microsoft.com/rest/api/contentsafety/) - مرجع مفصل لواجهة برمجة التطبيقات لتنفيذ Content Safety.
4. [البدء السريع: Azure Content Safety مع C#](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-csharp) - دليل تنفيذ سريع باستخدام C#.
5. [مكتبات العملاء لـ Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-client-libraries-rest-api) - مكتبات العملاء لمختلف لغات البرمجة.
6. [كشف محاولات كسر الحماية](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection) - إرشادات محددة لكشف ومنع محاولات كسر الحماية.
7. [أفضل الممارسات لـ Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/best-practices) - أفضل الممارسات لتنفيذ Content Safety بفعالية.

للحصول على تنفيذ أكثر تفصيلاً، راجع دليل [تنفيذ Azure Content Safety](./azure-content-safety-implementation.md).

**إخلاء المسؤولية**:  
تمت ترجمة هذا المستند باستخدام خدمة الترجمة الآلية [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى لتحقيق الدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الموثوق به. للمعلومات الهامة، يُنصح بالاعتماد على الترجمة البشرية المهنية. نحن غير مسؤولين عن أي سوء فهم أو تفسير ناتج عن استخدام هذه الترجمة.