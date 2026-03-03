![MCP-for-beginners](../../translated_images/ar/mcp-beginners.2ce2b317996369ff.webp) 

[![GitHub contributors](https://img.shields.io/github/contributors/microsoft/mcp-for-beginners.svg)](https://GitHub.com/microsoft/mcp-for-beginners/graphs/contributors)
[![GitHub issues](https://img.shields.io/github/issues/microsoft/mcp-for-beginners.svg)](https://GitHub.com/microsoft/mcp-for-beginners/issues)
[![GitHub pull-requests](https://img.shields.io/github/issues-pr/microsoft/mcp-for-beginners.svg)](https://GitHub.com/microsoft/mcp-for-beginners/pulls)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)

[![GitHub watchers](https://img.shields.io/github/watchers/microsoft/mcp-for-beginners.svg?style=social&label=Watch)](https://GitHub.com/microsoft/mcp-for-beginners/watchers)
[![GitHub forks](https://img.shields.io/github/forks/microsoft/mcp-for-beginners.svg?style=social&label=Fork)](https://GitHub.com/microsoft/mcp-for-beginners/fork)
[![GitHub stars](https://img.shields.io/github/stars/microsoft/mcp-for-beginners?style=social&label=Star)](https://GitHub.com/microsoft/mcp-for-beginners/stargazers)


[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

اتبع هذه الخطوات للبدء باستخدام هذه الموارد:
1. **أنشئ نسخة من المستودع**: اضغط على [![GitHub forks](https://img.shields.io/github/forks/microsoft/mcp-for-beginners.svg?style=social&label=Fork)](https://GitHub.com/microsoft/mcp-for-beginners/fork)
2. **انسخ المستودع**:   `git clone https://github.com/microsoft/mcp-for-beginners.git`
3. **انضم إلى** [![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)


### 🌐 دعم متعدد اللغات

#### مدعوم عبر GitHub Action (آلي ومحدث دائمًا)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabic](./README.md) | [Bengali](../bn/README.md) | [Bulgarian](../bg/README.md) | [Burmese (Myanmar)](../my/README.md) | [Chinese (Simplified)](../zh-CN/README.md) | [Chinese (Traditional, Hong Kong)](../zh-HK/README.md) | [Chinese (Traditional, Macau)](../zh-MO/README.md) | [Chinese (Traditional, Taiwan)](../zh-TW/README.md) | [Croatian](../hr/README.md) | [Czech](../cs/README.md) | [Danish](../da/README.md) | [Dutch](../nl/README.md) | [Estonian](../et/README.md) | [Finnish](../fi/README.md) | [French](../fr/README.md) | [German](../de/README.md) | [Greek](../el/README.md) | [Hebrew](../he/README.md) | [Hindi](../hi/README.md) | [Hungarian](../hu/README.md) | [Indonesian](../id/README.md) | [Italian](../it/README.md) | [Japanese](../ja/README.md) | [Kannada](../kn/README.md) | [Korean](../ko/README.md) | [Lithuanian](../lt/README.md) | [Malay](../ms/README.md) | [Malayalam](../ml/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Nigerian Pidgin](../pcm/README.md) | [Norwegian](../no/README.md) | [Persian (Farsi)](../fa/README.md) | [Polish](../pl/README.md) | [Portuguese (Brazil)](../pt-BR/README.md) | [Portuguese (Portugal)](../pt-PT/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Romanian](../ro/README.md) | [Russian](../ru/README.md) | [Serbian (Cyrillic)](../sr/README.md) | [Slovak](../sk/README.md) | [Slovenian](../sl/README.md) | [Spanish](../es/README.md) | [Swahili](../sw/README.md) | [Swedish](../sv/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Tamil](../ta/README.md) | [Telugu](../te/README.md) | [Thai](../th/README.md) | [Turkish](../tr/README.md) | [Ukrainian](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamese](../vi/README.md)

> **تفضل استنساخ المستودع محليًا؟**
>
> يتضمن هذا المستودع أكثر من 50 ترجمة للغات مما يزيد بشكل كبير من حجم التنزيل. للاستنساخ بدون الترجمات، استخدم تقنية sparse checkout:
>
> **Bash / macOS / Linux:**
> ```bash
> git clone --filter=blob:none --sparse https://github.com/microsoft/mcp-for-beginners.git
> cd mcp-for-beginners
> git sparse-checkout set --no-cone '/*' '!translations' '!translated_images'
> ```
>
> **CMD (Windows):**
> ```cmd
> git clone --filter=blob:none --sparse https://github.com/microsoft/mcp-for-beginners.git
> cd mcp-for-beginners
> git sparse-checkout set --no-cone "/*" "!translations" "!translated_images"
> ```
>
> هذا يوفر لك كل ما تحتاجه لإكمال الدورة بسرعة تحميل أكبر.
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

# 🚀 منهج بروتوكول سياق النموذج (MCP) للمبتدئين

## **تعلم MCP من خلال أمثلة عملية في C#، Java، JavaScript، Rust، Python، و TypeScript**

## 🧠 نظرة عامة على منهج بروتوكول سياق النموذج
مرحبًا بك في رحلتك مع بروتوكول سياق النموذج! إذا تساءلت يومًا كيف تتواصل تطبيقات الذكاء الاصطناعي مع أدوات وخدمات مختلفة، فأنت على وشك اكتشاف الحل الأنيق الذي يغير طريقة بناء المطورين للأنظمة الذكية.

فكر في MCP كمترجم عالمي لتطبيقات الذكاء الاصطناعي - تمامًا كما تسمح لك منافذ USB بتوصيل أي جهاز إلى حاسوبك، يتيح MCP لنماذج الذكاء الاصطناعي الاتصال بأي أداة أو خدمة بطريقة موحدة. سواء كنت تبني أول روبوت دردشة خاص بك أو تعمل على تدفقات عمل ذكاء اصطناعي معقدة، فإن فهم MCP يمنحك القدرة على إنشاء تطبيقات أكثر قدرة ومرونة.

تم تصميم هذا المنهج بصبر وعناية لدعم رحلتك التعليمية. سنبدأ بمفاهيم بسيطة تعرفها بالفعل ونجمع خبراتك تدريجيًا من خلال الممارسة العملية في لغة البرمجة التي تفضلها. كل خطوة تتضمن شروحات واضحة، أمثلة عملية، والكثير من التشجيع على طول الطريق.

عندما تنهي هذه الرحلة، ستكون واثقًا من بناء خوادم MCP الخاصة بك، ودمجها مع منصات الذكاء الاصطناعي الشهيرة، وفهم كيف تعيد هذه التكنولوجيا تشكيل مستقبل تطوير الذكاء الاصطناعي. هيا لنبدأ هذه المغامرة المثيرة معًا!

### الوثائق والمواصفات الرسمية

هذا المنهج متوافق مع **مواصفة MCP بتاريخ 2025-11-25** (الإصدار المستقر الأخير). تستخدم مواصفة MCP نظام إصدار معتمد على التاريخ (بصيغة YYYY-MM-DD) لضمان تتبع واضح لإصدارات البروتوكول.

تصبح هذه الموارد أكثر قيمة مع تنامي فهمك، لكن لا تشعر بضغط قراءة كل شيء فورًا. ابدأ بالمجالات التي تهمك أكثر!
- 📘 [توثيق MCP](https://modelcontextprotocol.io/) – هذا هو المورد الرئيسي لك للتعلم خطوة بخطوة والدروس الإرشادية. التوثيق مكتوب مع مراعاة المبتدئين، ويشمل أمثلة واضحة يمكنك متابعتها بالوتيرة التي تناسبك.
- 📜 [مواصفة MCP](https://modelcontextprotocol.io/specification/2025-11-25) – اعتبرها دليل المرجع الشامل الخاص بك. أثناء عملك عبر المنهج، ستعود هنا للبحث عن تفاصيل معينة واستكشاف ميزات متقدمة.
- 📜 [إصدارات مواصفة MCP](https://modelcontextprotocol.io/specification/versioning) – تحتوي على معلومات حول تاريخ إصدارات البروتوكول وكيف يستخدم MCP نظام إصدار معتمد على التاريخ (بصيغة YYYY-MM-DD).
- 🧑‍💻 [مستودع MCP على GitHub](https://github.com/modelcontextprotocol) – هنا ستجد مجموعات تطوير البرمجيات، الأدوات، وعينات الكود بلغات برمجة متعددة. يشبه ذلك كنزًا من الأمثلة العملية والمكونات الجاهزة للاستخدام.
- 🌐 [مجتمع MCP](https://github.com/orgs/modelcontextprotocol/discussions) – انضم إلى زملاء المتعلمين والمطورين ذوي الخبرة في نقاشات حول MCP. إنه مجتمع داعم حيث الأسئلة مرحب بها والمعرفة تتشارك بحرية.
  
## أهداف التعلم

بنهاية هذا المنهج، ستشعر بالثقة والحماس لقدراتك الجديدة. إليك ما ستحققه:

• **فهم أساسيات MCP**: ستدرك ما هو بروتوكول سياق النموذج ولماذا يغير طريقة عمل تطبيقات الذكاء الاصطناعي معًا، باستخدام تشبيهات وأمثلة واضحة تسهل الفهم.

• **بناء أول خادم MCP خاص بك**: ستنشئ خادم MCP يعمل ضمن لغة البرمجة التي تفضلها، بدءًا بأمثلة بسيطة وتنمو مهاراتك خطوة بخطوة.

• **ربط نماذج الذكاء الاصطناعي بالأدوات الحقيقية**: ستتعلم كيف تجسر الفجوة بين نماذج الذكاء الاصطناعي والخدمات الحقيقية، مما يمنح تطبيقاتك قدرات جديدة قوية.

• **تطبيق أفضل ممارسات الأمان**: ستفهم كيف تحافظ على تنفيذات MCP آمنة ومحفوظة، تحمي تطبيقاتك ومستخدميك.

• **النشر بثقة**: ستعرف كيف تنقل مشاريع MCP من مرحلة التطوير إلى الإنتاج، مع استراتيجيات نشر عملية تعمل في العالم الحقيقي.

• **الانضمام إلى مجتمع MCP**: ستصبح جزءًا من مجتمع متنامي من المطورين الذين يشكلون مستقبل تطوير تطبيقات الذكاء الاصطناعي.

## الخلفية الأساسية

قبل أن نغوص في تفاصيل MCP، دعنا نتأكد من شعورك بالراحة مع بعض المفاهيم الأساسية. لا تقلق إذا لم تكن خبيرًا في هذه المجالات - سنشرح لك كل ما تحتاج إلى معرفته ونحن نتابع!

### فهم البروتوكولات (الأساس)

فكر في البروتوكول كأنه قواعد للمحادثة. عندما تتصل بصديق، تعرفان أن تقولوا "مرحبًا" عند الرد، وتأخذان دور الكلام، وتقول "وداعًا" عند الانتهاء. تحتاج برامج الحاسوب إلى قواعد مماثلة لتتواصل بفعالية.

MCP هو بروتوكول - مجموعة من القواعد المتفق عليها التي تساعد نماذج التطبيقات الذكية على إجراء "محادثات" مثمرة مع الأدوات والخدمات. تمامًا كما تجعل قواعد المحادثة التواصل البشري أكثر سلاسة، يجعل MCP تواصل تطبيقات الذكاء الاصطناعي أكثر موثوقية وقوة.

### علاقات العميل والخادم (كيف تعمل البرامج معًا)

أنت تستخدم علاقات العميل والخادم يوميًا! عندما تستخدم متصفح الويب (العميل) لتصفح موقع، فإنك تتصل بخادم ويب يرسل لك المحتوى. المتصفح يعرف كيف يطلب المعلومات، والخادم يعرف كيف يرد.

في MCP، لدينا علاقة مماثلة: نماذج الذكاء الاصطناعي تعمل كعملاء يطلبون معلومات أو إجراءات، وخوادم MCP توفر هذه القدرات. يشبه وجود مساعد مفيد (الخادم) يمكن للذكاء الاصطناعي أن يطلب منه أداء مهام محددة.

### لماذا التوحيد مهم (جعل الأشياء تعمل معًا)

تخيل لو أن كل مصنع سيارات يستخدم مضخات وقود بشكل مختلف - ستحتاج إلى محول مختلف لكل سيارة! التوحيد يعني الاتفاق على أساليب مشتركة لكي تعمل الأشياء معًا بسلاسة.

يوفر MCP هذا التوحيد لتطبيقات الذكاء الاصطناعي. بدلاً من أن يحتاج كل نموذج إلى كود مخصص للعمل مع كل أداة، يخلق MCP طريقة عالمية للتواصل. هذا يعني أن المطورين يمكنهم بناء الأدوات مرة واحدة وجعلها تعمل مع العديد من أنظمة الذكاء الاصطناعي المختلفة.

## 🧭 نظرة عامة على مسار التعلم الخاص بك

تم هيكلة رحلتك مع MCP بعناية لبناء ثقتك ومهاراتك تدريجيًا. يقدم كل مرحلة مفاهيم جديدة مع تعزيز ما تعلمته بالفعل.

### 🌱 مرحلة الأساس: فهم الأساسيات (الوحدات 0-2)

هذه هي بداية مغامرتك! سنعرفك على مفاهيم MCP باستخدام تشبيهات مألوفة وأمثلة بسيطة. ستفهم ما هو MCP، ولماذا يوجد، وكيف يندمج في عالم تطوير الذكاء الاصطناعي الأوسع.

• **الوحدة 0 - مقدمة إلى MCP**: سنبدأ باستكشاف ماهية MCP ولماذا هو مهم جدًا لتطبيقات الذكاء الاصطناعي الحديثة. سترى أمثلة من الواقع عن MCP وكيف يحل مشاكل شائعة يواجهها المطورون.

• **الوحدة 1 - شرح المفاهيم الأساسية**: هنا ستتعلم اللبنات الأساسية لـ MCP. سنستخدم الكثير من التشبيهات والأمثلة المرئية لضمان أن هذه المفاهيم تبدو طبيعية وسهلة الفهم.

• **الوحدة 2 - الأمان في MCP**: قد يبدو الأمان مخيفًا، لكننا سنريك كيف يتضمن MCP ميزات أمان مدمجة ونعلمك أفضل الممارسات التي تحمي تطبيقاتك من البداية.

### 🔨 مرحلة البناء: إنشاء أول تنفيذاتك (الوحدة 3)

المرح الحقيقي يبدأ الآن! ستحصل على تجربة عملية في بناء خوادم وعملاء MCP فعليين. لا تقلق - سنبدأ ببساطة ونرشدك خلال كل خطوة.
تتضمن هذه الوحدة العديد من الدلائل العملية التي تسمح لك بالممارسة بلغتك البرمجية المفضلة. ستقوم بإنشاء أول خادم لك، وبناء عميل للاتصال به، وحتى التكامل مع أدوات التطوير الشهيرة مثل VS Code.

تتضمن كل دليل أمثلة كود كاملة، ونصائح لحل المشكلات، وتفسيرات حول سبب اتخاذنا لخيارات تصميم معينة. بحلول نهاية هذه المرحلة، سيكون لديك تطبيقات MCP تعمل يمكنك أن تفخر بها!

### 🚀 مرحلة النمو: مفاهيم متقدمة وتطبيق في العالم الحقيقي (الوحدات 4-5)

بعد إتقان الأساسيات، ستكون مستعدًا لاستكشاف ميزات MCP الأكثر تعقيدًا. سنغطي استراتيجيات التنفيذ العملية، وتقنيات تصحيح الأخطاء، ومواضيع متقدمة مثل التكامل متعدد الوسائط للذكاء الاصطناعي.

ستتعلم أيضًا كيفية توسيع تطبيقات MCP للاستخدام في الإنتاج والتكامل مع منصات السحابة مثل Azure. هذه الوحدات تُعدك لبناء حلول MCP يمكنها التعامل مع متطلبات العالم الحقيقي.

### 🌟 مرحلة الإتقان: المجتمع والتخصص (الوحدات 6-11)

تركز المرحلة النهائية على الانضمام إلى مجتمع MCP والتخصص في المجالات التي تهمك أكثر. ستتعلم كيفية المساهمة في مشاريع MCP مفتوحة المصدر، وتنفيذ أنماط مصادقة متقدمة، وبناء حلول متكاملة شاملة لقواعد البيانات.

تستحق الوحدة 11 ذِكرًا خاصًا - فهي مسار تعليمي عملي متكامل مكون من 13 مختبرًا يعلمك كيف تبني خوادم MCP جاهزة للإنتاج مع تكامل PostgreSQL. إنها مثل مشروع تخرج يجمع كل ما تعلمته!

### 📚 هيكل المنهج الكامل

| الوحدة | الموضوع | الوصف | الرابط |
|--------|---------|---------|---------|
| **الوحدات 0-3: الأساسيات** | | | |
| 00 | مقدمة إلى MCP | نظرة عامة على بروتوكول نموذج السياق وأهميته في أنابيب الذكاء الاصطناعي | [اقرأ المزيد](./00-Introduction/README.md) |
| 01 | شرح المفاهيم الأساسية | استكشاف متعمق لمفاهيم MCP الأساسية | [اقرأ المزيد](./01-CoreConcepts/README.md) |
| 02 | الأمن في MCP | تهديدات الأمان وأفضل الممارسات | [اقرأ المزيد](./02-Security/README.md) |
| 03 | البدء مع MCP | إعداد البيئة، الخوادم/العملاء الأساسية، التكامل | [اقرأ المزيد](./03-GettingStarted/README.md) |
| **الوحدة 3: بناء أول خادم وعميل** | | | |
| 3.1 | أول خادم | أنشئ أول خادم MCP لك | [الدليل](./03-GettingStarted/01-first-server/README.md) |
| 3.2 | أول عميل | تطوير عميل MCP أساسي | [الدليل](./03-GettingStarted/02-client/README.md) |
| 3.3 | عميل مع LLM | دمج نماذج اللغة الكبيرة | [الدليل](./03-GettingStarted/03-llm-client/README.md) |
| 3.4 | تكامل VS Code | استهلاك خوادم MCP في VS Code | [الدليل](./03-GettingStarted/04-vscode/README.md) |
| 3.5 | خادم stdio | إنشاء خوادم باستخدام نقل stdio | [الدليل](./03-GettingStarted/05-stdio-server/README.md) |
| 3.6 | البث عبر HTTP | تنفيذ البث عبر HTTP في MCP | [الدليل](./03-GettingStarted/06-http-streaming/README.md) |
| 3.7 | أدوات AI Toolkit | استخدام AI Toolkit مع MCP | [الدليل](./03-GettingStarted/07-aitk/README.md) |
| 3.8 | الاختبار | اختبار تنفيذ خادم MCP الخاص بك | [الدليل](./03-GettingStarted/08-testing/README.md) |
| 3.9 | النشر | نشر خوادم MCP للإنتاج | [الدليل](./03-GettingStarted/09-deployment/README.md) |
| 3.10 | استخدام الخادم المتقدم | استخدام خوادم متقدمة لميزات متطورة وتحسين الهندسة المعمارية | [الدليل](./03-GettingStarted/10-advanced/README.md) |
| 3.11 | المصادقة البسيطة | فصل يشرح المصادقة من البداية وRBAC | [الدليل](./03-GettingStarted/11-simple-auth/README.md) |
| 3.12 | مضيفو MCP | تكوين Claude Desktop وCursor وCline ومضيفي MCP الآخرين | [الدليل](./03-GettingStarted/12-mcp-hosts/README.md) |
| 3.13 | MCP Inspector | تصحيح واختبار خوادم MCP باستخدام أداة Inspector | [الدليل](./03-GettingStarted/13-mcp-inspector/README.md) |
| 3.14 | أخذ عينات | استخدام العينة للتعاون مع العميل | [الدليل](./03-GettingStarted/14-sampling/README.md) |
| **الوحدات 4-5: عملي ومتقدم** | | | |
| 04 | التنفيذ العملي | SDKs، تصحيح الأخطاء، الاختبار، قوالب النصوص القابلة لإعادة الاستخدام | [اقرأ المزيد](./04-PracticalImplementation/README.md) |
| 4.1 | الترقيم | التعامل مع مجموعات نتائج كبيرة مع ترقيم يعتمد على المؤشر | [الدليل](./04-PracticalImplementation/pagination/README.md) |
| 05 | مواضيع متقدمة في MCP | الذكاء الاصطناعي متعدد الوسائط، التوسع، استخدام المؤسسات | [اقرأ المزيد](./05-AdvancedTopics/README.md) |
| 5.1 | تكامل Azure | تكامل MCP مع Azure | [الدليل](./05-AdvancedTopics/mcp-integration/README.md) |
| 5.2 | تعدد الوسائط | العمل مع وسائط متعددة | [الدليل](./05-AdvancedTopics/mcp-multi-modality/README.md) |
| 5.3 | عرض OAuth2 | تنفيذ مصادقة OAuth2 | [الدليل](./05-AdvancedTopics/mcp-oauth2-demo/README.md) |
| 5.4 | سياقات الجذر | فهم وتنفيذ سياقات الجذر | [الدليل](./05-AdvancedTopics/mcp-root-contexts/README.md) |
| 5.5 | التوجيه | استراتيجيات توجيه MCP | [الدليل](./05-AdvancedTopics/mcp-routing/README.md) |
| 5.6 | أخذ العينات | تقنيات أخذ العينات في MCP | [الدليل](./05-AdvancedTopics/mcp-sampling/README.md) |
| 5.7 | التوسع | توسيع تطبيقات MCP | [الدليل](./05-AdvancedTopics/mcp-scaling/README.md) |
| 5.8 | الأمن | اعتبارات أمنية متقدمة | [الدليل](./05-AdvancedTopics/mcp-security/README.md) |
| 5.9 | البحث على الويب | تنفيذ قدرات البحث على الويب | [الدليل](./05-AdvancedTopics/web-search-mcp/README.md) |
| 5.10 | البث في الوقت الحقيقي | بناء وظيفة البث في الوقت الحقيقي | [الدليل](./05-AdvancedTopics/mcp-realtimestreaming/README.md) |
| 5.11 | البحث في الوقت الحقيقي | تنفيذ البحث في الوقت الحقيقي | [الدليل](./05-AdvancedTopics/mcp-realtimesearch/README.md) |
| 5.12 | مصادقة Entra ID | المصادقة باستخدام Microsoft Entra ID | [الدليل](./05-AdvancedTopics/mcp-security-entra/README.md) |
| 5.13 | تكامل Foundry | التكامل مع Azure AI Foundry | [الدليل](./05-AdvancedTopics/mcp-foundry-agent-integration/README.md) |
| 5.14 | هندسة السياق | تقنيات هندسة السياق الفعالة | [الدليل](./05-AdvancedTopics/mcp-contextengineering/README.md) |
| 5.15 | نقل MCP المخصص | تنفيذات نقل مخصصة | [الدليل](./05-AdvancedTopics/mcp-transport/README.md) |
| 5.16 | ميزات البروتوكول | إشعارات التقدم، الإلغاء، قوالب الموارد | [الدليل](./05-AdvancedTopics/mcp-protocol-features/README.md) |
| **الوحدات 6-10: المجتمع وأفضل الممارسات** | | | |
| 06 | مساهمات المجتمع | كيفية المساهمة في نظام MCP البيئي | [الدليل](./06-CommunityContributions/README.md) |
| 07 | رؤى من التبني المبكر | قصص تنفيذ من العالم الحقيقي | [الدليل](./07-LessonsfromEarlyAdoption/README.md) |
| 08 | أفضل الممارسات لـ MCP | الأداء، تحمل الأخطاء، المرونة | [الدليل](./08-BestPractices/README.md) |
| 09 | دراسات حالة MCP | أمثلة تنفيذ عملية | [الدليل](./09-CaseStudy/README.md) |
| 10 | ورشة عمل عملية | بناء خادم MCP باستخدام AI Toolkit | [المختبر](./10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/README.md) |
| **الوحدة 11: مختبر عملي لخادم MCP** | | | |
| 11 | تكامل خادم MCP مع قاعدة البيانات | مسار تعليمي عملي مكون من 13 مختبرًا للتكامل مع PostgreSQL | [المختبرات](./11-MCPServerHandsOnLabs/README.md) |
| 11.1 | المقدمة | نظرة عامة على MCP مع تكامل قاعدة البيانات وحالة استخدام تحليلات التجزئة | [المختبر 00](./11-MCPServerHandsOnLabs/00-Introduction/README.md) |
| 11.2 | الهندسة المعمارية الأساسية | فهم هندسة خادم MCP، طبقات قاعدة البيانات، وأنماط الأمان | [المختبر 01](./11-MCPServerHandsOnLabs/01-Architecture/README.md) |
| 11.3 | الأمان وتعدد المستأجرين | أمان مستوى الصف، المصادقة، والوصول متعدد المستأجرين للبيانات | [المختبر 02](./11-MCPServerHandsOnLabs/02-Security/README.md) |
| 11.4 | إعداد البيئة | إعداد بيئة التطوير، Docker، موارد Azure | [المختبر 03](./11-MCPServerHandsOnLabs/03-Setup/README.md) |
| 11.5 | تصميم قاعدة البيانات | إعداد PostgreSQL، تصميم مخطط التجزئة، والبيانات النموذجية | [المختبر 04](./11-MCPServerHandsOnLabs/04-Database/README.md) |
| 11.6 | تنفيذ خادم MCP | بناء خادم FastMCP مع تكامل قاعدة البيانات | [المختبر 05](./11-MCPServerHandsOnLabs/05-MCP-Server/README.md) |
| 11.7 | تطوير الأدوات | إنشاء أدوات استعلام قاعدة البيانات وفحص المخطط | [المختبر 06](./11-MCPServerHandsOnLabs/06-Tools/README.md) |
| 11.8 | البحث الدلالي | تنفيذ التضمينات المتجهية باستخدام Azure OpenAI و pgvector | [المختبر 07](./11-MCPServerHandsOnLabs/07-Semantic-Search/README.md) |
| 11.9 | الاختبار وتصحيح الأخطاء | استراتيجيات الاختبار، أدوات التصحيح، ونهج التحقق | [المختبر 08](./11-MCPServerHandsOnLabs/08-Testing/README.md) |
| 11.10 | تكامل VS Code | تكوين تكامل MCP مع VS Code واستخدام دردشة AI | [المختبر 09](./11-MCPServerHandsOnLabs/09-VS-Code/README.md) |
| 11.11 | استراتيجيات النشر | نشر Docker، تطبيقات الحاويات Azure، واعتبارات التوسع | [المختبر 10](./11-MCPServerHandsOnLabs/10-Deployment/README.md) |
| 11.12 | المراقبة | Application Insights، التسجيل، ومراقبة الأداء | [المختبر 11](./11-MCPServerHandsOnLabs/11-Monitoring/README.md) |
| 11.13 | أفضل الممارسات | تحسين الأداء، تقوية الأمان، ونصائح الإنتاج | [المختبر 12](./11-MCPServerHandsOnLabs/12-Best-Practices/README.md) |

### 💻 مشاريع عينة كود

أحد أكثر أجزاء تعلم MCP إثارة هو رؤية مهاراتك في الكود تتطور تدريجيًا. لقد صممنا أمثلة الكود الخاصة بنا لتبدأ بسيطة وتنمو أكثر تعقيدًا كلما تعمقت فهمك. إليك كيف نقدم المفاهيم - بكود سهل الفهم لكنه يُظهر مبادئ MCP الحقيقية، ستفهم ليس فقط ما يفعله هذا الكود، ولكن لماذا هو مُهيكل بهذه الطريقة وكيف يناسب التطبيقات الأكبر لـ MCP.

#### عينات حاسبة MCP الأساسية

| اللغة | الوصف | الرابط |
|--------|--------|---------|
| C# | مثال خادم MCP | [عرض الكود](./03-GettingStarted/samples/csharp/README.md) |
| Java | حاسبة MCP | [عرض الكود](./03-GettingStarted/samples/java/calculator/README.md) |
| JavaScript | عرض MCP | [عرض الكود](./03-GettingStarted/samples/javascript/README.md) |
| Python | خادم MCP | [عرض الكود](../../03-GettingStarted/samples/python/mcp_calculator_server.py) |
| TypeScript | مثال MCP | [عرض الكود](./03-GettingStarted/samples/typescript/README.md) |
| Rust | مثال MCP | [عرض الكود](./03-GettingStarted/samples/rust/README.md) |

#### تطبيقات MCP المتقدمة

| اللغة | الوصف | الرابط |
|--------|--------|---------|
| C# | عينة متقدمة | [عرض الكود](./04-PracticalImplementation/samples/csharp/README.md) |
| Java مع Spring | مثال تطبيق الحاوية | [عرض الكود](./04-PracticalImplementation/samples/java/containerapp/README.md) |
| JavaScript | عينة متقدمة | [عرض الكود](./04-PracticalImplementation/samples/javascript/README.md) |
| Python | تنفيذ معقد | [عرض الكود](./04-PracticalImplementation/samples/python/README.md) |
| TypeScript | عينة حاوية | [عرض الكود](./04-PracticalImplementation/samples/typescript/README.md) |


## 🎯 المتطلبات الأساسية لتعلم MCP

للحصول على أقصى استفادة من هذا المنهج، يجب أن يكون لديك:
- المعرفة الأساسية بالبرمجة في واحدة على الأقل من اللغات التالية: C#، Java، JavaScript، Python، أو TypeScript  
- فهم نموذج العميل-الخادم وواجهات برمجة التطبيقات (APIs)  
- الإلمام بمفاهيم REST وHTTP  
- (اختياري) خلفية في مفاهيم الذكاء الاصطناعي والتعلم الآلي  

- الانضمام إلى مناقشات مجتمعنا للدعم  

## 📚 دليل الدراسة والموارد

يتضمن هذا المستودع عدة موارد لمساعدتك على التنقل والتعلم بفعالية:

### دليل الدراسة

يتوفر [دليل الدراسة](./study_guide.md) الشامل لمساعدتك على التنقل في هذا المستودع بفعالية. يعرض هذا المخطط التدريسي المرئي كيف ترتبط جميع المواضيع ويوفر إرشادات حول كيفية استخدام مشاريع العينة بفعالية. إنه مفيد بشكل خاص إذا كنت متعلمًا بصريًا تحب رؤية الصورة الكاملة.

يتضمن الدليل:  
- مخطط تدريسي بصري يظهر جميع المواضيع المشمولة  
- تفصيل دقيق لكل قسم من أقسام المستودع  
- إرشادات حول كيفية استخدام مشاريع العينة  
- مسارات تعلم موصى بها لمستويات مهارية مختلفة  
- موارد إضافية تكمل رحلتك التعليمية  

### سجل التغييرات

نحتفظ بـ [سجل التغييرات](./changelog.md) مفصّل يتتبع جميع التحديثات المهمة في مواد المنهج الدراسي، لكي تظل مواكبًا لأحدث التحسينات والإضافات.  
- إضافات محتوى جديدة  
- تغييرات هيكلية  
- تحسينات في الميزات  
- تحديثات الوثائق  

## 🛠️ كيفية استخدام هذا المنهج الدراسي بفعالية

يتضمن كل درس في هذا الدليل:  

1. تفسيرات واضحة لمفاهيم MCP  
2. أمثلة تعليمية حية بلغات برمجة متعددة  
3. تمارين لبناء تطبيقات MCP حقيقية  
4. موارد إضافية للمتعلمين المتقدمين  

### لنتعلم MCP مع C# - سلسلة تعليمية  
دعونا نتعرف على بروتوكول سياق النموذج (MCP)، وهو إطار عمل متطور مصمم لتوحيد التفاعلات بين نماذج الذكاء الاصطناعي وتطبيقات العميل. من خلال هذه الجلسة المخصصة للمبتدئين، سنقدم لك MCP ونرشدك خلال إنشاء أول خادم MCP خاص بك.  
#### C#: [https://aka.ms/letslearnmcp-csharp](https://aka.ms/letslearnmcp-csharp)  
#### Java: [https://aka.ms/letslearnmcp-java](https://aka.ms/letslearnmcp-java)  
#### JavaScript: [https://aka.ms/letslearnmcp-javascript](https://aka.ms/letslearnmcp-javascript)  
#### Python: [https://aka.ms/letslearnmcp-python](https://aka.ms/letslearnmcp-python)  

## 🎓 تبدأ رحلتك مع MCP

مبروك! لقد اتخذت للتو الخطوة الأولى في رحلة مثيرة ستوسع قدراتك البرمجية وتربطك بواجهة تطوير الذكاء الاصطناعي الحديثة.

### ما أنجزته بالفعل

بقراءتك لهذا التقديم، بدأت بالفعل في بناء أساس معرفتك بـ MCP. أنت تفهم ما هو MCP، ولماذا هو مهم، وكيف سيدعمك هذا المنهج في رحلتك التعليمية. هذا إنجاز هام وبداية خبرتك في هذه التقنية المهمة.

### المغامرة القادمة

بينما تتقدم في الدروس، تذكر أن كل خبير كان مبتدئًا يومًا ما. المفاهيم التي قد تبدو معقدة الآن ستصبح طبيعية مع الممارسة والتطبيق. كل خطوة صغيرة تبني قدرات قوية ستفيدك طوال مسيرتك في التطوير.

### شبكة الدعم الخاصة بك

أنت تنضم إلى مجتمع من المتعلمين والخبراء الذين يحرصون على MCP ويتطلعون لمساعدة الآخرين على النجاح. سواء كنت عالقًا في تحدي ترميز أو متحمسًا لمشاركة اكتشاف جديد، فالمجتمع هنا لدعم رحلتك.

إذا واجهت مشكلة أو كان لديك أي أسئلة حول بناء تطبيقات الذكاء الاصطناعي، انضم إلى المتعلمين والمطورين ذوي الخبرة في مناقشات MCP. إنه مجتمع داعم حيث الأسئلة مرحب بها والمعرفة تُنقل بحرية.

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

إذا كان لديك ملاحظات عن المنتج أو أخطاء أثناء البناء قم بزيارة:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

### هل أنت مستعد للبدء؟

تبدأ مغامرتك مع MCP الآن! ابدأ بالوحدة 0 للخوض في أول تجارب MCP عملية، أو استكشف مشاريع العينة لترى ما ستبنيه. تذكر - كل خبير بدأ من حيث أنت الآن، وبالصبر والممارسة ستندهش مما يمكنك تحقيقه.

مرحبًا بك في عالم تطوير بروتوكول سياق النموذج. دعونا نبني شيئًا مذهلًا معًا!

## 🤝 المساهمة في مجتمع التعلم

يتقوى هذا المنهج بمساهمات المتعلمين مثلك! سواء كنت تصلح خطأ مطبعي، أو تقترح شرحًا أوضح، أو تضيف مثالًا جديدًا، فإن مساهماتك تساعد المبتدئين الآخرين على النجاح.

شكر خاص للخبير المعتمد من مايكروسوفت [Shivam Goyal](https://www.linkedin.com/in/shivam2003/) على مساهمته بأمثلة الشيفرة.

تم تصميم عملية المساهمة لتكون مرحبة وداعمة. معظم المساهمات تتطلب اتفاقية ترخيص مساهم (CLA)، لكن الأدوات الآلية ستوجهك خلال العملية بسلاسة.

## 📜 التعلم مفتوح المصدر

هذا المنهج الدراسي كامل متاح بموجب رخصة MIT [LICENSE](../../LICENSE)، مما يعني أنه يمكنك استخدامه وتعديله ومشاركته بحرية. هذا يدعم مهمتنا في جعل معرفة MCP متاحة للمطورين في كل مكان.

## 🤝 إرشادات المساهمة

يرحب هذا المشروع بالمساهمات والاقتراحات. معظم المساهمات تتطلب منك الموافقة على  
اتفاقية ترخيص مساهم (CLA) تعلن فيها أنك تمتلك الحق، وبالفعل تمنحنا  
حقوق استخدام مساهمتك. للمزيد من التفاصيل، زوروا <https://cla.opensource.microsoft.com>.

عند تقديم طلب سحب، سيقرر روبوت CLA تلقائيًا ما إذا كنت بحاجة لتقديم  
اتفاقية CLA ويضيف التعليقات المناسبة على الطلب (مثل فحص الحالة، تعليق). فقط اتبع  
الإرشادات التي يوفرها الروبوت. تحتاج فقط إلى القيام بذلك مرة واحدة لجميع المستودعات التي تستخدم CLA الخاصة بنا.

هذا المشروع اعتمد [مدونة السلوك لمشاريع مايكروسوفت مفتوحة المصدر](https://opensource.microsoft.com/codeofconduct/).  
لمزيد من المعلومات انظر [الأسئلة الشائعة عن مدونة السلوك](https://opensource.microsoft.com/codeofconduct/faq/) أو  
تواصل مع [opencode@microsoft.com](mailto:opencode@microsoft.com) لأي أسئلة أو تعليقات إضافية.

---

*هل أنت مستعد لبدء رحلتك مع MCP؟ ابدأ بـ [الوحدة 00 - مقدمة إلى MCP](./00-Introduction/README.md) وخطو أولى خطواتك في عالم تطوير بروتوكول سياق النموذج!*



## 🎒 دورات أخرى  
يقوم فريقنا بإنتاج دورات أخرى! تحقق من:  

<!-- CO-OP TRANSLATOR OTHER COURSES START -->
### LangChain  
[![LangChain4j للمبتدئين](https://img.shields.io/badge/LangChain4j%20for%20Beginners-22C55E?style=for-the-badge&&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchain4j-for-beginners)  
[![LangChain.js للمبتدئين](https://img.shields.io/badge/LangChain.js%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchainjs-for-beginners?WT.mc_id=m365-94501-dwahlin)  
[![LangChain للمبتدئين](https://img.shields.io/badge/LangChain%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://github.com/microsoft/langchain-for-beginners?WT.mc_id=m365-94501-dwahlin)  
---

### Azure / Edge / MCP / Agents  
[![AZD للمبتدئين](https://img.shields.io/badge/AZD%20for%20Beginners-0078D4?style=for-the-badge&labelColor=E5E7EB&color=0078D4)](https://github.com/microsoft/AZD-for-beginners?WT.mc_id=academic-105485-koreyst)  
[![Edge AI للمبتدئين](https://img.shields.io/badge/Edge%20AI%20for%20Beginners-00B8E4?style=for-the-badge&labelColor=E5E7EB&color=00B8E4)](https://github.com/microsoft/edgeai-for-beginners?WT.mc_id=academic-105485-koreyst)  
[![MCP للمبتدئين](https://img.shields.io/badge/MCP%20for%20Beginners-009688?style=for-the-badge&labelColor=E5E7EB&color=009688)](https://github.com/microsoft/mcp-for-beginners?WT.mc_id=academic-105485-koreyst)  
[![وكلاء AI للمبتدئين](https://img.shields.io/badge/AI%20Agents%20for%20Beginners-00C49A?style=for-the-badge&labelColor=E5E7EB&color=00C49A)](https://github.com/microsoft/ai-agents-for-beginners?WT.mc_id=academic-105485-koreyst)  

---
 
### سلسلة الذكاء الاصطناعي التوليدي  
[![الذكاء الاصطناعي التوليدي للمبتدئين](https://img.shields.io/badge/Generative%20AI%20for%20Beginners-8B5CF6?style=for-the-badge&labelColor=E5E7EB&color=8B5CF6)](https://github.com/microsoft/generative-ai-for-beginners?WT.mc_id=academic-105485-koreyst)  
[![الذكاء الاصطناعي التوليدي (.NET)](https://img.shields.io/badge/Generative%20AI%20(.NET)-9333EA?style=for-the-badge&labelColor=E5E7EB&color=9333EA)](https://github.com/microsoft/Generative-AI-for-beginners-dotnet?WT.mc_id=academic-105485-koreyst)  
[![الذكاء الاصطناعي التوليدي (Java)](https://img.shields.io/badge/Generative%20AI%20(Java)-C084FC?style=for-the-badge&labelColor=E5E7EB&color=C084FC)](https://github.com/microsoft/generative-ai-for-beginners-java?WT.mc_id=academic-105485-koreyst)  
[![الذكاء الاصطناعي التوليدي (JavaScript)](https://img.shields.io/badge/Generative%20AI%20(JavaScript)-E879F9?style=for-the-badge&labelColor=E5E7EB&color=E879F9)](https://github.com/microsoft/generative-ai-with-javascript?WT.mc_id=academic-105485-koreyst)  

---
 
### التعلم الأساسي  
[![التعلم الآلي للمبتدئين](https://img.shields.io/badge/ML%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=22C55E)](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)  
[![علوم البيانات للمبتدئين](https://img.shields.io/badge/Data%20Science%20for%20Beginners-84CC16?style=for-the-badge&labelColor=E5E7EB&color=84CC16)](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)  
[![الذكاء الاصطناعي للمبتدئين](https://img.shields.io/badge/AI%20for%20Beginners-A3E635?style=for-the-badge&labelColor=E5E7EB&color=A3E635)](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)  
[![الأمن السيبراني للمبتدئين](https://img.shields.io/badge/Cybersecurity%20for%20Beginners-F97316?style=for-the-badge&labelColor=E5E7EB&color=F97316)](https://github.com/microsoft/Security-101?WT.mc_id=academic-96948-sayoung)  
[![تطوير الويب للمبتدئين](https://img.shields.io/badge/Web%20Dev%20for%20Beginners-EC4899?style=for-the-badge&labelColor=E5E7EB&color=EC4899)](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)  
[![إنترنت الأشياء للمبتدئين](https://img.shields.io/badge/IoT%20for%20Beginners-14B8A6?style=for-the-badge&labelColor=E5E7EB&color=14B8A6)](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)  
[![تطوير الواقع الممتد للمبتدئين](https://img.shields.io/badge/XR%20Development%20for%20Beginners-38BDF8?style=for-the-badge&labelColor=E5E7EB&color=38BDF8)](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)  

---
 
### سلسلة كوبايلوت
[![المساعد البرمجي للبرمجة الزوجية المعتمدة على الذكاء الاصطناعي](https://img.shields.io/badge/Copilot%20for%20AI%20Paired%20Programming-FACC15?style=for-the-badge&labelColor=E5E7EB&color=FACC15)](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)
[![المساعد البرمجي لـ C#/.NET](https://img.shields.io/badge/Copilot%20for%20C%23/.NET-FBBF24?style=for-the-badge&labelColor=E5E7EB&color=FBBF24)](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)
[![مغامرة المساعد البرمجي](https://img.shields.io/badge/Copilot%20Adventure-FDE68A?style=for-the-badge&labelColor=E5E7EB&color=FDE68A)](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)
<!-- CO-OP TRANSLATOR OTHER COURSES END -->

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**إخلاء المسؤولية**:
تمت ترجمة هذا المستند باستخدام خدمة الترجمة الآلية [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى لتحقيق الدقة، يُرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر المعتمد. بالنسبة للمعلومات الهامة، يُنصح باللجوء إلى الترجمة البشرية المهنية. لسنا مسؤولين عن أي سوء فهم أو تفسيرات خاطئة تنشأ من استخدام هذه الترجمة.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->