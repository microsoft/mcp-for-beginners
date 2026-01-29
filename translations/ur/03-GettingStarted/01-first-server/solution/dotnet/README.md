# اس نمونے کو چلانا

## -1- ضروریات انسٹال کریں

```bash
dotnet restore
```

## -3- نمونہ چلائیں

```bash
dotnet run
```

## -4- نمونہ آزمائیں

جب سرور ایک ٹرمینل میں چل رہا ہو، تو دوسرا ٹرمینل کھولیں اور درج ذیل کمانڈ چلائیں:

```bash
npx @modelcontextprotocol/inspector dotnet run
```

یہ ایک ویب سرور شروع کرے گا جس میں ایک بصری انٹرفیس ہوگا جو آپ کو نمونہ آزمانے کی اجازت دے گا۔

جب سرور جڑ جائے:

- ٹولز کی فہرست بنانے کی کوشش کریں اور `add` چلائیں، دلائل 2 اور 4 کے ساتھ، آپ کو نتیجے میں 6 نظر آنا چاہیے۔
- وسائل اور وسائل کے سانچے پر جائیں اور "greeting" کو کال کریں، ایک نام ٹائپ کریں اور آپ کو فراہم کردہ نام کے ساتھ ایک سلام نظر آنا چاہیے۔

### CLI موڈ میں آزمائش

آپ اسے براہ راست CLI موڈ میں درج ذیل کمانڈ چلا کر شروع کر سکتے ہیں:

```bash
npx @modelcontextprotocol/inspector --cli dotnet run --method tools/list
```

یہ سرور میں دستیاب تمام ٹولز کی فہرست دے گا۔ آپ کو درج ذیل آؤٹ پٹ نظر آنا چاہیے:

```text
{
  "tools": [
    {
      "name": "Add",
      "description": "Adds two numbers",
      "inputSchema": {
        "type": "object",
        "properties": {
          "a": {
            "type": "integer"
          },
          "b": {
            "type": "integer"
          }
        },
        "title": "Add",
        "description": "Adds two numbers",
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
npx @modelcontextprotocol/inspector --cli dotnet run --method tools/call --tool-name Add --tool-arg a=1 --tool-arg b=2
```

آپ کو درج ذیل آؤٹ پٹ نظر آنا چاہیے:

```text
{
  "content": [
    {
      "type": "text",
      "text": "Sum 3"
    }
  ],
  "isError": false
}
```

> [!TIP]
> عام طور پر CLI موڈ میں انسپکٹر کو چلانا براؤزر کے مقابلے میں بہت تیز ہوتا ہے۔
> انسپکٹر کے بارے میں مزید پڑھیں [یہاں](https://github.com/modelcontextprotocol/inspector)۔

---

**ڈسکلیمر**:  
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کا استعمال کرتے ہوئے ترجمہ کی گئی ہے۔ ہم درستگی کے لیے کوشش کرتے ہیں، لیکن براہ کرم آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا غیر درستیاں ہو سکتی ہیں۔ اصل دستاویز کو اس کی اصل زبان میں مستند ذریعہ سمجھا جانا چاہیے۔ اہم معلومات کے لیے، پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ ہم اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کے ذمہ دار نہیں ہیں۔