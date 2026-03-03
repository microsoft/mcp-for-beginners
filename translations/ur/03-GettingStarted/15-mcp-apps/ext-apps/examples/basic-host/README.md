# مثال: بنیادی میزبان

ایک حوالہ جاتی نفاذ جو دکھاتا ہے کہ ایک MCP میزبان ایپلیکیشن کیسے بنائی جائے جو MCP سرورز سے جڑتی ہے اور ایک محفوظ سینڈباکس میں ٹول کے یوزر انٹرفیس کو رینڈر کرتی ہے۔

یہ بنیادی میزبان لوکل ترقی کے دوران MCP ایپس کی جانچ کے لیے بھی استعمال کیا جا سکتا ہے۔

## اہم فائلیں

- [`index.html`](../../../../../../../03-GettingStarted/15-mcp-apps/ext-apps/examples/basic-host/index.html) / [`src/index.tsx`](../../../../../../../03-GettingStarted/15-mcp-apps/ext-apps/examples/basic-host/src/index.tsx) - ری ایکٹ UI میزبان جس میں ٹول کا انتخاب، پیرا میٹر داخل کرنا، اور iframe انتظام شامل ہے
- [`sandbox.html`](../../../../../../../03-GettingStarted/15-mcp-apps/ext-apps/examples/basic-host/sandbox.html) / [`src/sandbox.ts`](../../../../../../../03-GettingStarted/15-mcp-apps/ext-apps/examples/basic-host/src/sandbox.ts) - بیرونی iframe پروکسی جس میں سیکیورٹی تصدیق اور دو طرفہ پیغام رسانی ہوتی ہے
- [`src/implementation.ts`](../../../../../../../03-GettingStarted/15-mcp-apps/ext-apps/examples/basic-host/src/implementation.ts) - بنیادی منطق: سرور کنکشن، ٹول کالنگ، اور AppBridge سیٹ اپ

## آغاز کیسے کریں

```bash
npm install
npm run start
# کھولیں http://localhost:8080
```
  
ڈیفالٹ کے مطابق، میزبان ایپلیکیشن `http://localhost:3001/mcp` پر ایک MCP سرور سے جڑنے کی کوشش کرے گی۔ آپ اس رویے کو `SERVERS` ماحول متغیر کو سرور URLs کی JSON صف فراہم کر کے ترتیب دے سکتے ہیں:

```bash
SERVERS='["http://localhost:1234/mcp", "http://localhost:5678/mcp"]' npm run start
```
  
## فن تعمیر

یہ مثال محفوظ UI علیحدگی کے لیے ڈبل-iframe سینڈباکس پیٹرن استعمال کرتی ہے:

```
Host (port 8080)
  └── Outer iframe (port 8081) - sandbox proxy
        └── Inner iframe (srcdoc) - untrusted tool UI
```
  
**دو iframes کی ضرورت کیوں ہے؟**

- بیرونی iframe ایک الگ origin (پورٹ 8081) پر چلتا ہے جو میزبان تک براہ راست رسائی کو روکتا ہے  
- اندرونی iframe `srcdoc` کے ذریعے HTML وصول کرتا ہے اور سینڈباکس خصوصیات کی پابندی میں ہے  
- پیغامات بیرونی iframe کے ذریعے گزرتے ہیں جو ان کی تصدیق کرتا ہے اور دو طرفہ طور پر پہنچاتا ہے  

یہ فن تعمیر اس بات کو یقینی بناتا ہے کہ اگر ٹول UI کوڈ نقصان دہ بھی ہو تو وہ میزبان ایپلیکیشن کے DOM، کوکیز، یا JavaScript کانٹیکسٹ تک رسائی حاصل نہیں کر سکتا۔

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**دستخطی وضاحت**:  
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) استعمال کرتے ہوئے ترجمہ کی گئی ہے۔ اگرچہ ہم درستگی کی کوشش کرتے ہیں، براہ کرم یاد رکھیں کہ خودکار تراجم میں غلطیاں یا عدم درستگیاں ہو سکتی ہیں۔ اصل دستاویز اپنی مادری زبان میں مستند ذریعہ سمجھی جانی چاہیے۔ اہم معلومات کے لیے پیشہ ورانہ انسانی ترجمہ کی سفارش کی جاتی ہے۔ ہم اس ترجمے کے استعمال سے پیدا ہونے والے کسی بھی غلط فہمی یا غلط تشریح کے لیے ذمہ دار نہیں ہیں۔
<!-- CO-OP TRANSLATOR DISCLAIMER END -->