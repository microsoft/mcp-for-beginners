# اس نمونے کو چلانا

## -1- ضروریات انسٹال کریں

```bash
dotnet restore
```

## -2- نمونہ چلائیں

```bash
dotnet run
```

## -3- نمونہ آزمائیں

نمونہ چلانے سے پہلے ایک الگ ٹرمینل شروع کریں (یقینی بنائیں کہ سرور ابھی بھی چل رہا ہو)۔

ایک ٹرمینل میں سرور چلانے کے ساتھ، دوسرا ٹرمینل کھولیں اور درج ذیل کمانڈ چلائیں:

```bash
npx @modelcontextprotocol/inspector http://localhost:3001
```

یہ ایک ویب سرور شروع کرے گا جس میں ایک بصری انٹرفیس ہوگا جو آپ کو نمونہ آزمانے کی اجازت دے گا۔

> یقینی بنائیں کہ **Streamable HTTP** کو ٹرانسپورٹ ٹائپ کے طور پر منتخب کیا گیا ہے، اور URL `http://localhost:3001/mcp` ہے۔

جب سرور کنیکٹ ہو جائے:

- ٹولز کی فہرست بنانے کی کوشش کریں اور `add` چلائیں، دلائل 2 اور 4 کے ساتھ، آپ کو نتیجے میں 6 نظر آنا چاہیے۔
- وسائل اور وسائل کے ٹیمپلیٹ پر جائیں اور "greeting" کو کال کریں، ایک نام ٹائپ کریں اور آپ کو فراہم کردہ نام کے ساتھ ایک سلام نظر آئے گا۔

### CLI موڈ میں آزمائش

آپ اسے CLI موڈ میں براہ راست درج ذیل کمانڈ چلا کر شروع کر سکتے ہیں:

```bash 
npx @modelcontextprotocol/inspector --cli http://localhost:3001 --method tools/list
```

یہ سرور میں دستیاب تمام ٹولز کی فہرست دے گا۔ آپ کو درج ذیل آؤٹ پٹ نظر آنا چاہیے:

```text
{
  "tools": [
    {
      "name": "AddNumbers",
      "description": "Add two numbers together.",
      "inputSchema": {
        "type": "object",
        "properties": {
          "a": {
            "description": "The first number",
            "type": "integer"
          },
          "b": {
            "description": "The second number",
            "type": "integer"
          }
        },
        "title": "AddNumbers",
        "description": "Add two numbers together.",
        "required": [
          "a",
          "b"
        ]
      }
    }
  ]
}
```

کسی ٹول کو چلانے کے لیے درج کریں:

```bash
npx @modelcontextprotocol/inspector --cli http://localhost:3001 --method tools/call --tool-name AddNumbers --tool-arg a=1 --tool-arg b=2
```

آپ کو درج ذیل آؤٹ پٹ نظر آنا چاہیے:

```text
{
  "content": [
    {
      "type": "text",
      "text": "3"
    }
  ],
  "isError": false
}
```

> [!TIP]
> CLI موڈ میں انسپکٹر چلانا عام طور پر براؤزر کے مقابلے میں بہت تیز ہوتا ہے۔
> انسپکٹر کے بارے میں مزید پڑھیں [یہاں](https://github.com/modelcontextprotocol/inspector)۔

---

**ڈسکلیمر**:  
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کا استعمال کرتے ہوئے ترجمہ کی گئی ہے۔ ہم درستگی کے لیے کوشش کرتے ہیں، لیکن براہ کرم آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا غیر درستیاں ہو سکتی ہیں۔ اصل دستاویز کو اس کی اصل زبان میں مستند ذریعہ سمجھا جانا چاہیے۔ اہم معلومات کے لیے، پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ ہم اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کے ذمہ دار نہیں ہیں۔