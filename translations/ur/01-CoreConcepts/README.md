<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f00defb149ee1ac4a799e44a9783c7fc",
  "translation_date": "2025-06-06T18:01:39+00:00",
  "source_file": "01-CoreConcepts/README.md",
  "language_code": "ur"
}
-->
# 📖 MCP Core Concepts: AI انضمام کے لیے Model Context Protocol میں مہارت حاصل کرنا

Model Context Protocol (MCP) ایک طاقتور، معیاری فریم ورک ہے جو Large Language Models (LLMs) اور بیرونی ٹولز، ایپلیکیشنز، اور ڈیٹا ذرائع کے درمیان مواصلات کو بہتر بناتا ہے۔ یہ SEO کے لیے بہتر بنایا گیا گائیڈ آپ کو MCP کے بنیادی تصورات سے روشناس کرائے گا، تاکہ آپ اس کی کلائنٹ-سرور آرکیٹیکچر، اہم اجزاء، رابطے کے طریقہ کار، اور بہترین عمل درآمد کو سمجھ سکیں۔

## جائزہ

یہ سبق Model Context Protocol (MCP) کے بنیادی آرکیٹیکچر اور اجزاء کا جائزہ لیتا ہے جو MCP ایکوسسٹم کی تشکیل کرتے ہیں۔ آپ کلائنٹ-سرور آرکیٹیکچر، اہم اجزاء، اور مواصلاتی طریقہ کار کے بارے میں سیکھیں گے جو MCP کی بات چیت کو ممکن بناتے ہیں۔

## 👩‍🎓 اہم تعلیمی مقاصد

اس سبق کے اختتام تک، آپ:

- MCP کلائنٹ-سرور آرکیٹیکچر کو سمجھ جائیں گے۔
- Hosts، Clients، اور Servers کے کردار اور ذمہ داریاں پہچانیں گے۔
- MCP کو ایک لچکدار انضمام پرت بنانے والی بنیادی خصوصیات کا تجزیہ کریں گے۔
- MCP ایکوسسٹم میں معلومات کے بہاؤ کو سیکھیں گے۔
- .NET، Java، Python، اور JavaScript میں کوڈ کی مثالوں کے ذریعے عملی بصیرت حاصل کریں گے۔

## 🔎 MCP آرکیٹیکچر: ایک گہری نظر

MCP ایکوسسٹم کلائنٹ-سرور ماڈل پر مبنی ہے۔ یہ ماڈیولر ڈھانچہ AI ایپلیکیشنز کو ٹولز، ڈیٹا بیسز، APIs، اور سیاق و سباق کے وسائل کے ساتھ مؤثر طریقے سے تعامل کرنے کی اجازت دیتا ہے۔ آئیے اس آرکیٹیکچر کو اس کے بنیادی اجزاء میں تقسیم کرتے ہیں۔

### 1. Hosts

Model Context Protocol (MCP) میں، Hosts ایک اہم کردار ادا کرتے ہیں کیونکہ وہ وہ بنیادی انٹرفیس ہیں جن کے ذریعے صارفین پروٹوکول کے ساتھ تعامل کرتے ہیں۔ Hosts وہ ایپلیکیشنز یا ماحولیات ہیں جو MCP سرورز کے ساتھ کنکشن شروع کرتے ہیں تاکہ ڈیٹا، ٹولز، اور پرامپٹس تک رسائی حاصل کی جا سکے۔ Hosts کی مثالوں میں Visual Studio Code جیسے Integrated Development Environments (IDEs)، Claude Desktop جیسے AI ٹولز، یا مخصوص کاموں کے لیے بنائے گئے کسٹم ایجنٹس شامل ہیں۔

**Hosts** وہ LLM ایپلیکیشنز ہیں جو کنکشن شروع کرتی ہیں۔ وہ:

- AI ماڈلز کے ساتھ تعامل یا ان سے جوابات پیدا کرتی ہیں۔
- MCP سرورز کے ساتھ کنکشن شروع کرتی ہیں۔
- گفتگو کے بہاؤ اور یوزر انٹرفیس کا انتظام کرتی ہیں۔
- اجازت اور سیکیورٹی پابندیوں کو کنٹرول کرتی ہیں۔
- ڈیٹا شیئرنگ اور ٹول کے نفاذ کے لیے صارف کی رضامندی سنبھالتی ہیں۔

### 2. Clients

Clients وہ اہم اجزاء ہیں جو Hosts اور MCP سرورز کے درمیان تعامل کو آسان بناتے ہیں۔ Clients ایک درمیانی حیثیت رکھتے ہیں، جو Hosts کو MCP سرورز کی فراہم کردہ فعالیتوں تک رسائی اور استعمال کی اجازت دیتے ہیں۔ وہ MCP آرکیٹیکچر کے اندر ہموار رابطے اور مؤثر ڈیٹا کے تبادلے کو یقینی بنانے میں اہم کردار ادا کرتے ہیں۔

**Clients** Host ایپلیکیشن کے اندر کنیکٹرز ہوتے ہیں۔ وہ:

- پرامپٹس/ہدایات کے ساتھ سرورز کو درخواستیں بھیجتے ہیں۔
- سرورز کے ساتھ صلاحیتوں پر مذاکرات کرتے ہیں۔
- ماڈلز سے ٹول کے نفاذ کی درخواستوں کا انتظام کرتے ہیں۔
- صارفین کو جوابات پروسیس اور دکھاتے ہیں۔

### 3. Servers

Servers MCP کلائنٹس کی درخواستوں کو سنبھالتے ہیں اور مناسب جوابات فراہم کرتے ہیں۔ وہ مختلف آپریشنز جیسے ڈیٹا بازیافت، ٹول کا نفاذ، اور پرامپٹ جنریشن کو منظم کرتے ہیں۔ Servers اس بات کو یقینی بناتے ہیں کہ کلائنٹس اور Hosts کے درمیان مواصلات مؤثر اور قابل اعتماد ہوں، اور تعامل کے عمل کی سالمیت برقرار رکھیں۔

**Servers** وہ سروسز ہیں جو سیاق و سباق اور صلاحیتیں فراہم کرتی ہیں۔ وہ:

- دستیاب خصوصیات (وسائل، پرامپٹس، ٹولز) کو رجسٹر کرتے ہیں۔
- کلائنٹ سے ٹول کالز وصول کرتے اور ان پر عملدرآمد کرتے ہیں۔
- ماڈل کے جوابات کو بہتر بنانے کے لیے سیاق و سباق کی معلومات فراہم کرتے ہیں۔
- نتائج کو کلائنٹ کو واپس کرتے ہیں۔
- ضرورت پڑنے پر تعاملات کے دوران حالت کو برقرار رکھتے ہیں۔

Servers کسی بھی شخص کی طرف سے ماڈل کی صلاحیتوں کو تخصصی فعالیت کے ساتھ بڑھانے کے لیے تیار کیے جا سکتے ہیں۔

### 4. Server Features

Model Context Protocol (MCP) میں Servers بنیادی تعمیراتی بلاکس فراہم کرتے ہیں جو کلائنٹس، Hosts، اور زبان کے ماڈلز کے درمیان بھرپور تعاملات کو ممکن بناتے ہیں۔ یہ خصوصیات MCP کی صلاحیتوں کو منظم سیاق و سباق، ٹولز، اور پرامپٹس فراہم کرکے بڑھانے کے لیے ڈیزائن کی گئی ہیں۔

MCP سرورز درج ذیل میں سے کوئی بھی خصوصیات پیش کر سکتے ہیں:

#### 📑 Resources

Model Context Protocol (MCP) میں Resources مختلف اقسام کے سیاق و سباق اور ڈیٹا کو شامل کرتے ہیں جنہیں صارفین یا AI ماڈلز استعمال کر سکتے ہیں۔ ان میں شامل ہیں:

- **سیاق و سباق کا ڈیٹا**: وہ معلومات اور سیاق و سباق جو صارفین یا AI ماڈلز فیصلہ سازی اور کام انجام دینے کے لیے استعمال کر سکتے ہیں۔
- **نالج بیسز اور دستاویزات کے ذخیرے**: منظم اور غیر منظم ڈیٹا کے مجموعے، جیسے مضامین، دستی، اور تحقیقی مقالے، جو قیمتی بصیرت اور معلومات فراہم کرتے ہیں۔
- **مقامی فائلز اور ڈیٹا بیسز**: وہ ڈیٹا جو آلات پر مقامی طور پر یا ڈیٹا بیسز میں محفوظ ہوتا ہے، جس تک رسائی اور تجزیہ ممکن ہوتا ہے۔
- **APIs اور ویب سروسز**: بیرونی انٹرفیسز اور سروسز جو اضافی ڈیٹا اور فعالیت فراہم کرتی ہیں، مختلف آن لائن وسائل اور ٹولز کے ساتھ انضمام کو ممکن بناتی ہیں۔

ایک resource کی مثال ایک ڈیٹا بیس اسکیمہ یا فائل ہو سکتی ہے جس تک اس طرح رسائی حاصل کی جا سکتی ہے:

```text
file://log.txt
database://schema
```

### 🤖 Prompts

Model Context Protocol (MCP) میں Prompts مختلف پہلے سے متعین ٹیمپلیٹس اور تعامل کے نمونے شامل ہوتے ہیں جو صارف کے کام کے بہاؤ کو آسان بناتے اور مواصلات کو بہتر کرتے ہیں۔ ان میں شامل ہیں:

- **ٹیمپلیٹ شدہ پیغامات اور ورک فلو**: پہلے سے منظم پیغامات اور عمل جو صارفین کو مخصوص کاموں اور تعاملات میں رہنمائی کرتے ہیں۔
- **پہلے سے متعین تعامل کے نمونے**: معیاری عمل اور جوابات کے سلسلے جو مستقل اور مؤثر مواصلات کو سہولت فراہم کرتے ہیں۔
- **خصوصی گفتگو کے ٹیمپلیٹس**: مخصوص قسم کی بات چیت کے لیے حسب ضرورت ٹیمپلیٹس جو متعلقہ اور سیاق و سباق کے لحاظ سے مناسب تعاملات کو یقینی بناتے ہیں۔

ایک پرامپٹ ٹیمپلیٹ اس طرح دکھائی دے سکتا ہے:

```markdown
Generate a product slogan based on the following {{product}} with the following {{keywords}}
```

#### ⛏️ Tools

Model Context Protocol (MCP) میں Tools وہ فنکشنز ہیں جنہیں AI ماڈل مخصوص کام انجام دینے کے لیے چلا سکتا ہے۔ یہ ٹولز AI ماڈل کی صلاحیتوں کو منظم اور قابل اعتماد آپریشنز فراہم کرکے بڑھانے کے لیے ڈیزائن کیے گئے ہیں۔ اہم پہلو یہ ہیں:

- **AI ماڈل کے لیے قابل عمل فنکشنز**: ٹولز قابل عمل فنکشنز ہوتے ہیں جنہیں AI ماڈل مختلف کام انجام دینے کے لیے کال کر سکتا ہے۔
- **منفرد نام اور وضاحت**: ہر ٹول کا ایک الگ نام اور تفصیلی وضاحت ہوتی ہے جو اس کے مقصد اور فعالیت کو بیان کرتی ہے۔
- **پیرامیٹرز اور آؤٹ پٹ**: ٹولز مخصوص پیرامیٹرز قبول کرتے ہیں اور منظم آؤٹ پٹ فراہم کرتے ہیں، تاکہ نتائج مستقل اور متوقع ہوں۔
- **مخصوص فنکشنز**: ٹولز ویب سرچ، حساب کتاب، اور ڈیٹا بیس کوئریز جیسے مخصوص فنکشنز انجام دیتے ہیں۔

ایک مثال کے طور پر ٹول اس طرح دکھائی دے سکتا ہے:

```typescript
server.tool(
  "GetProducts",
  {
    pageSize: z.string().optional(),
    pageCount: z.string().optional()
  }, () => {
    // return results from API
  }
)
```

## Client Features

Model Context Protocol (MCP) میں کلائنٹس سرورز کو کئی اہم خصوصیات فراہم کرتے ہیں جو پروٹوکول کے اندر مجموعی فعالیت اور تعامل کو بڑھاتی ہیں۔ ان میں سے ایک نمایاں خصوصیت Sampling ہے۔

### 👉 Sampling

- **سرور کی طرف سے شروع کیے گئے Agentic رویے**: کلائنٹس سرورز کو مخصوص اقدامات یا رویے خود مختار طریقے سے شروع کرنے کی اجازت دیتے ہیں، جو نظام کی متحرک صلاحیتوں کو بڑھاتا ہے۔
- **Recursive LLM Interactions**: یہ خصوصیت بڑی زبان کے ماڈلز (LLMs) کے ساتھ تکراری تعاملات کی اجازت دیتی ہے، جس سے کاموں کی زیادہ پیچیدہ اور تکراری پروسیسنگ ممکن ہوتی ہے۔
- **ماڈل سے اضافی مکملات کی درخواست**: سرورز ماڈل سے اضافی مکملات طلب کر سکتے ہیں، تاکہ جوابات مکمل اور سیاق و سباق کے لحاظ سے مناسب ہوں۔

## MCP میں معلومات کا بہاؤ

Model Context Protocol (MCP) میزبانوں، کلائنٹس، سرورز، اور ماڈلز کے درمیان معلومات کے منظم بہاؤ کی وضاحت کرتا ہے۔ اس بہاؤ کو سمجھنا یہ واضح کرتا ہے کہ صارف کی درخواستیں کیسے پروسیس ہوتی ہیں اور بیرونی ٹولز اور ڈیٹا ماڈلز کے جوابات میں کیسے شامل کیے جاتے ہیں۔

- **Host کنکشن شروع کرتا ہے**  
  میزبان ایپلیکیشن (جیسے IDE یا چیٹ انٹرفیس) عام طور پر STDIO، WebSocket، یا کسی اور سپورٹڈ ٹرانسپورٹ کے ذریعے MCP سرور سے کنکشن قائم کرتا ہے۔

- **صلاحیتوں پر مذاکرات**  
  کلائنٹ (جو میزبان میں شامل ہوتا ہے) اور سرور اپنی سپورٹڈ خصوصیات، ٹولز، وسائل، اور پروٹوکول ورژنز کے بارے میں معلومات کا تبادلہ کرتے ہیں۔ اس سے دونوں فریق کو سیشن کے لیے دستیاب صلاحیتوں کا پتہ چلتا ہے۔

- **صارف کی درخواست**  
  صارف میزبان کے ساتھ تعامل کرتا ہے (مثلاً پرامپٹ یا کمانڈ داخل کرتا ہے)۔ میزبان یہ ان پٹ جمع کرتا ہے اور پروسیسنگ کے لیے کلائنٹ کو بھیج دیتا ہے۔

- **وسائل یا ٹول کا استعمال**  
  - کلائنٹ اضافی سیاق و سباق یا وسائل سرور سے طلب کر سکتا ہے (جیسے فائلز، ڈیٹا بیس اندراجات، یا نالج بیس آرٹیکلز) تاکہ ماڈل کی سمجھ بوجھ کو بڑھایا جا سکے۔
  - اگر ماڈل یہ طے کرے کہ ٹول کی ضرورت ہے (مثلاً ڈیٹا حاصل کرنا، حساب کرنا، یا API کال کرنا)، تو کلائنٹ سرور کو ٹول کی کال کی درخواست بھیجتا ہے، جس میں ٹول کا نام اور پیرامیٹرز شامل ہوتے ہیں۔

- **سرور کا نفاذ**  
  سرور وسائل یا ٹول کی درخواست وصول کرتا ہے، ضروری آپریشنز انجام دیتا ہے (جیسے فنکشن چلانا، ڈیٹا بیس کوئری کرنا، یا فائل بازیافت کرنا)، اور نتائج کو منظم شکل میں کلائنٹ کو واپس کرتا ہے۔

- **جواب کی تخلیق**  
  کلائنٹ سرور کے جوابات (وسائل کا ڈیٹا، ٹول کے نتائج وغیرہ) کو ماڈل کے ساتھ جاری تعامل میں شامل کرتا ہے۔ ماڈل اس معلومات کو استعمال کرتے ہوئے مکمل اور سیاق و سباق کے لحاظ سے مناسب جواب تیار کرتا ہے۔

- **نتائج کی پیشکش**  
  میزبان کلائنٹ سے حتمی آؤٹ پٹ وصول کرتا ہے اور اسے صارف کو پیش کرتا ہے، جس میں اکثر ماڈل کا پیدا کردہ متن اور ٹول کے نفاذ یا وسائل کی تلاش کے نتائج شامل ہوتے ہیں۔

یہ بہاؤ MCP کو ماڈلز کو بیرونی ٹولز اور ڈیٹا ذرائع کے ساتھ بغیر رکاوٹ جوڑ کر جدید، تعاملی، اور سیاق و سباق سے آگاہ AI ایپلیکیشنز کی حمایت کرنے کے قابل بناتا ہے۔

## پروٹوکول کی تفصیلات

MCP (Model Context Protocol) [JSON-RPC 2.0](https://www.jsonrpc.org/) کے اوپر بنایا گیا ہے، جو میزبانوں، کلائنٹس، اور سرورز کے درمیان مواصلات کے لیے ایک معیاری، زبان سے آزاد پیغام فارمیٹ فراہم کرتا ہے۔ یہ بنیاد مختلف پلیٹ فارمز اور پروگرامنگ زبانوں میں قابل اعتماد، منظم، اور توسیع پذیر تعاملات کو ممکن بناتی ہے۔

### اہم پروٹوکول خصوصیات

MCP JSON-RPC 2.0 کو ٹول کال، وسائل تک رسائی، اور پرامپٹ مینجمنٹ کے لیے اضافی کنونشنز کے ساتھ بڑھاتا ہے۔ یہ متعدد ٹرانسپورٹ پرتوں (STDIO، WebSocket، SSE) کی حمایت کرتا ہے اور اجزاء کے درمیان محفوظ، توسیع پذیر، اور زبان سے آزاد مواصلات کو ممکن بناتا ہے۔

#### 🧢 بنیادی پروٹوکول

- **JSON-RPC میسج فارمیٹ**: تمام درخواستیں اور جوابات JSON-RPC 2.0 وضاحت کا استعمال کرتے ہیں، جس سے میتھڈ کالز، پیرامیٹرز، نتائج، اور ایرر ہینڈلنگ کے لیے مستقل ڈھانچہ یقینی بنتا ہے۔
- **حالت دار کنکشنز**: MCP سیشنز متعدد درخواستوں کے دوران حالت کو برقرار رکھتے ہیں، جس سے جاری گفتگو، سیاق و سباق کا جمع ہونا، اور وسائل کا انتظام ممکن ہوتا ہے۔
- **صلاحیتوں پر مذاکرات**: کنکشن کے قیام کے دوران، کلائنٹس اور سرورز اپنی سپورٹڈ خصوصیات، پروٹوکول ورژنز، دستیاب ٹولز، اور وسائل کے بارے میں معلومات کا تبادلہ کرتے ہیں۔ اس سے دونوں طرف کو ایک دوسرے کی صلاحیتوں کا علم ہوتا ہے اور وہ مطابق ڈھال سکتے ہیں۔

#### ➕ اضافی یوٹیلٹیز

ذیل میں کچھ اضافی یوٹیلٹیز اور پروٹوکول توسیعات ہیں جو MCP ڈویلپر کے تجربے کو بہتر بنانے اور پیچیدہ منظرناموں کو ممکن بنانے کے لیے فراہم کرتا ہے:

- **کنفیگریشن آپشنز**: MCP سیشن پیرامیٹرز کی متحرک کنفیگریشن کی اجازت دیتا ہے، جیسے ٹول کی اجازتیں، وسائل تک رسائی، اور ماڈل کی ترتیبات، جو ہر تعامل کے مطابق ہوتی ہیں۔
- **پروگریس ٹریکنگ**: طویل عرصے تک چلنے والے آپریشنز پروگریس اپ ڈیٹس رپورٹ کر سکتے ہیں، جو صارف کے انٹرفیس کو جوابدہ اور پیچیدہ کاموں کے دوران بہتر صارف تجربہ فراہم کرتا ہے۔
- **درخواست کی منسوخی**: کلائنٹس جاری درخواستوں کو منسوخ کر سکتے ہیں، جس سے صارفین کو ان آپریشنز کو روکنے کی اجازت ملتی ہے جو اب ضروری نہیں یا بہت زیادہ وقت لے رہے ہوں۔
- **ایرر رپورٹنگ**: معیاری ایرر پیغامات اور کوڈز مسائل کی تشخیص، ناکامیوں کو مؤدبانہ طریقے سے سنبھالنے، اور صارفین اور ڈویلپرز کو قابل عمل فیڈبیک فراہم کرنے میں مدد کرتے ہیں۔
- **لاگنگ**: کلائنٹس اور سرورز دونوں پروٹوکول تعاملات کے لیے آڈٹ، ڈیبگنگ، اور مانیٹرنگ کے لیے منظم لاگز جاری کر سکتے ہیں۔

ان پروٹوکول خصوصیات کا فائدہ اٹھا کر، MCP زبان کے ماڈلز اور بیرونی ٹولز یا ڈیٹا ذرائع کے درمیان مضبوط، محفوظ، اور لچکدار مواصلات کو یقینی بناتا ہے۔

### 🔐 سیکیورٹی کے پہلو

MCP کی تعمیل کرتے ہوئے کئی کلیدی سیکیورٹی اصولوں پر عمل کرنا چاہیے تاکہ محفوظ اور قابل اعتماد تعاملات کو یقینی بنایا جا سکے:

- **صارف کی رضامندی اور کنٹرول**: کسی بھی ڈیٹا تک رسائی یا آپریشن کرنے سے پہلے صارف کی واضح رضامندی ضروری ہے۔ انہیں یہ واضح کنٹرول حاصل ہونا چاہیے کہ کون سا ڈیٹا شیئر کیا جاتا ہے اور کون سے اقدامات کی اجازت ہے، جس کی حمایت صارف دوست انٹرفیس کے ذریعے کی جائے جو سرگرمیوں کا جائزہ لینے اور منظوری دینے میں مدد دے۔
- **ڈیٹا کی پرائیویسی**: صارف کا ڈیٹا صرف واضح رضامندی کے ساتھ ظاہر کیا جانا چاہیے اور مناسب رسائی کنٹرولز کے ذریعے محفوظ ہونا چاہیے۔ MCP کی تعمیل غیر مجاز ڈیٹا ٹرانسمیشن سے بچاؤ اور تمام تعاملات میں پرائیویسی کے تحفظ کو یقینی بناتی ہے۔
- **ٹول کی حفاظت**: کسی بھی ٹول کو کال کرنے سے پہلے واضح صارف کی رضامندی ضروری ہے۔ صارفین کو ہر ٹول کی فعالیت کی واضح سمجھ ہونی چاہیے، اور مضبوط سیکیورٹی حدود نافذ کی جانی چاہئیں تاکہ غیر متوقع یا غیر محفوظ ٹول کے نفاذ سے بچا جا سکے۔

ان اصولوں پر عمل کرتے ہوئے، MCP صارف کے اعتماد، پرائیویسی، اور حفاظت کو تمام پروٹوکول تعاملات میں برقرار رکھتا ہے۔

## کوڈ کی مثالیں: اہم اجزاء

ذیل میں کئی مقبول پروگرامنگ زبانوں میں کوڈ کی مثالیں دی گئی ہیں جو دکھاتی ہیں کہ MCP سرور کے اہم اجزاء اور ٹولز کو کیسے نافذ کیا جائے۔

### .NET مثال: Tools کے ساتھ ایک سادہ MCP سرور بنانا

یہ ایک عملی .NET کوڈ مثال ہے جو

**اعلانِ دستبرد**:  
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کے ذریعے ترجمہ کی گئی ہے۔ اگرچہ ہم درستگی کے لیے کوشاں ہیں، براہِ کرم یہ بات ذہن میں رکھیں کہ خودکار ترجمے میں غلطیاں یا نواقص ہو سکتے ہیں۔ اصل دستاویز اپنی مادری زبان میں معتبر ماخذ سمجھی جانی چاہیے۔ اہم معلومات کے لیے پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کی ذمہ داری ہم پر عائد نہیں ہوگی۔