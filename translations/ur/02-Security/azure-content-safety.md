# Azure Content Safety کے ساتھ اعلیٰ سطح کی MCP سیکیورٹی

Azure Content Safety کئی طاقتور اوزار فراہم کرتا ہے جو آپ کی MCP کی تنصیبات کی سیکیورٹی کو بہتر بنا سکتے ہیں:

## Prompt Shields

Microsoft کے AI Prompt Shields براہ راست اور بالواسطہ prompt injection حملوں کے خلاف مضبوط تحفظ فراہم کرتے ہیں، جن میں شامل ہیں:

1. **جدید شناخت**: مشین لرننگ کا استعمال کرتے ہوئے مواد میں شامل نقصان دہ ہدایات کی نشاندہی کرتا ہے۔
2. **نمایاں کرنا**: ان پٹ متن کو اس طرح تبدیل کرتا ہے کہ AI سسٹمز درست ہدایات اور بیرونی ان پٹ میں فرق کر سکیں۔
3. **حد بندی اور ڈیٹا مارکنگ**: قابل اعتماد اور غیر قابل اعتماد ڈیٹا کے درمیان حدود کو نشان زد کرتا ہے۔
4. **Content Safety انضمام**: Azure AI Content Safety کے ساتھ کام کرتا ہے تاکہ jailbreak کی کوششوں اور نقصان دہ مواد کا پتہ چلایا جا سکے۔
5. **مسلسل اپ ڈیٹس**: Microsoft باقاعدگی سے نئے خطرات کے خلاف حفاظتی طریقہ کار کو اپ ڈیٹ کرتا رہتا ہے۔

## MCP کے ساتھ Azure Content Safety کا نفاذ

یہ طریقہ کار کئی سطحی تحفظ فراہم کرتا ہے:
- پروسیسنگ سے پہلے ان پٹ کی جانچ
- نتائج کو واپس کرنے سے پہلے تصدیق
- معلوم شدہ نقصان دہ پیٹرنز کے لیے بلاک لسٹ کا استعمال
- Azure کے مسلسل اپ ڈیٹ ہونے والے Content Safety ماڈلز کا فائدہ اٹھانا

## Azure Content Safety کے وسائل

اپنے MCP سرورز کے ساتھ Azure Content Safety کے نفاذ کے بارے میں مزید جاننے کے لیے، ان سرکاری وسائل سے رجوع کریں:

1. [Azure AI Content Safety Documentation](https://learn.microsoft.com/azure/ai-services/content-safety/) - Azure Content Safety کی سرکاری دستاویزات۔
2. [Prompt Shield Documentation](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/prompt-shield) - prompt injection حملوں کو روکنے کا طریقہ سیکھیں۔
3. [Content Safety API Reference](https://learn.microsoft.com/rest/api/contentsafety/) - Content Safety کے نفاذ کے لیے تفصیلی API حوالہ۔
4. [Quickstart: Azure Content Safety with C#](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-csharp) - C# استعمال کرتے ہوئے فوری نفاذ کی رہنمائی۔
5. [Content Safety Client Libraries](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-client-libraries-rest-api) - مختلف پروگرامنگ زبانوں کے لیے کلائنٹ لائبریریز۔
6. [Detecting Jailbreak Attempts](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection) - jailbreak کی کوششوں کا پتہ لگانے اور روک تھام کے لیے مخصوص رہنمائی۔
7. [Best Practices for Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/best-practices) - مؤثر طریقے سے content safety نافذ کرنے کے بہترین طریقے۔

مزید تفصیلی نفاذ کے لیے، ہمارا [Azure Content Safety Implementation guide](./azure-content-safety-implementation.md) دیکھیں۔

**دستخطی دستبرداری**:  
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کے ذریعے ترجمہ کی گئی ہے۔ اگرچہ ہم درستگی کے لیے کوشاں ہیں، براہ کرم آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا عدم درستیاں ہو سکتی ہیں۔ اصل دستاویز اپنی مادری زبان میں معتبر ماخذ سمجھی جانی چاہیے۔ اہم معلومات کے لیے پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کی ذمہ داری ہم پر عائد نہیں ہوتی۔