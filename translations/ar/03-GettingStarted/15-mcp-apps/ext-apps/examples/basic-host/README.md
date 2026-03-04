# المثال: المضيف الأساسي

تنفيذ مرجعي يوضح كيفية بناء تطبيق مضيف MCP يتصل بخوادم MCP ويعرض واجهات أدوات في بيئة آمنة معزولة.

يمكن استخدام هذا المضيف الأساسي أيضًا لاختبار تطبيقات MCP أثناء تطويرها محليًا.

## الملفات الأساسية

- [`index.html`](../../../../../../../03-GettingStarted/15-mcp-apps/ext-apps/examples/basic-host/index.html) / [`src/index.tsx`](../../../../../../../03-GettingStarted/15-mcp-apps/ext-apps/examples/basic-host/src/index.tsx) - مضيف واجهة المستخدم React مع اختيار الأداة، إدخال المعلمات، وإدارة iframe
- [`sandbox.html`](../../../../../../../03-GettingStarted/15-mcp-apps/ext-apps/examples/basic-host/sandbox.html) / [`src/sandbox.ts`](../../../../../../../03-GettingStarted/15-mcp-apps/ext-apps/examples/basic-host/src/sandbox.ts) - وكيل iframe الخارجي مع التحقق الأمني وتتابع الرسائل ثنائي الاتجاه
- [`src/implementation.ts`](../../../../../../../03-GettingStarted/15-mcp-apps/ext-apps/examples/basic-host/src/implementation.ts) - المنطق الأساسي: اتصال الخادم، استدعاء الأدوات، وإعداد AppBridge

## البدء

```bash
npm install
npm run start
# افتح http://localhost:8080
```

بشكل افتراضي، سيحاول تطبيق المضيف الاتصال بخادم MCP على العنوان `http://localhost:3001/mcp`. يمكنك تكوين هذا السلوك عن طريق تعيين متغير البيئة `SERVERS` كمصفوفة JSON لعناوين URL الخاصة بالخوادم:

```bash
SERVERS='["http://localhost:1234/mcp", "http://localhost:5678/mcp"]' npm run start
```

## هندسة النظام

يستخدم هذا المثال نمط صندوق حماية بإطارين متداخلين لعزل واجهة المستخدم بأمان:

```
Host (port 8080)
  └── Outer iframe (port 8081) - sandbox proxy
        └── Inner iframe (srcdoc) - untrusted tool UI
```

**لماذا إطاران؟**

- إطار خارجي يعمل على أصل منفصل (المنفذ 8081) يمنع الوصول المباشر إلى المضيف
- الإطار الداخلي يستقبل HTML عبر `srcdoc` ويكون مقيدًا بسمات الصندوق
- تتدفق الرسائل عبر الإطار الخارجي الذي يتحقق منها ويعيد إرسالها ثنائي الاتجاه

تضمن هذه الهندسة أنه حتى إذا كان كود واجهة أداة ما ضارًا، فلا يمكنه الوصول إلى DOM أو ملفات تعريف الارتباط الخاصة بتطبيق المضيف أو سياق جافا سكريبت الخاص به.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**تنويه**:
تمت ترجمة هذا المستند باستخدام خدمة الترجمة الآلية [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى جاهدين لتحقيق الدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الرسمي والمعتمد. للمعلومات الحساسة، يُنصح بالترجمة البشرية المهنية. نحن غير مسؤولين عن أي سوء فهم أو تفسير ناتج عن استخدام هذه الترجمة.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->