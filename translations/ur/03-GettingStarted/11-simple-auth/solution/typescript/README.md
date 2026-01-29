# نمونہ چلائیں

## ضروریات انسٹال کریں

```sh
npm install
```

## تعمیر کریں

```sh
npm run build
```

## ٹوکنز بنائیں

```sh
npm run generate
```

یہ ایک ٹوکن *.env* فائل میں بناتا ہے۔ کلائنٹ اس فائل سے پڑھ لے گا۔

## کوڈ چلائیں

سرور شروع کریں:

```sh
npm start
```

کلائنٹ کو ایک الگ ٹرمینل میں چلائیں:

```sh
npm run client
```

سرور کے ٹرمینل میں آپ کو کچھ ایسا آؤٹ پٹ نظر آنا چاہیے:

```text
User exists
User has required scopes
Middleware executed
```

اور کلائنٹ کے ٹرمینل میں آپ کو کچھ ایسا آؤٹ پٹ نظر آنا چاہیے:

```text
Connected to MCP server with session ID: c1e50d7b-acff-4f11-8f96-5ae490ca1eaa
Available tools: { tools: [ { name: 'process-files', inputSchema: [Object] } ] }
Client disconnected.
Exiting...
```

### چیزیں تبدیل کرنا

آئیے یہ یقینی بنائیں کہ ہم اسکوپس کو سمجھتے ہیں۔ فائل *server.ts* کو تلاش کریں اور یہ کوڈ دیکھیں:

```typescript
 if(!hasScopes(token, ["User.Read"])){
        res.status(403).send('Forbidden - insufficient scopes');
    }
```

یہ کہتا ہے کہ دیے گئے ٹوکن میں "User.Read" ہونا چاہیے، آئیے اسے "User.Write" میں تبدیل کریں۔ اب `npm run build` چلائیں اور سرور کو دوبارہ شروع کریں `npm start`۔ اب آپ کو دیکھنا چاہیے کہ تصدیق ناکام ہو گئی ہے کیونکہ ہمارے پاس یہ اسکوپ نہیں ہے (ہمارے پاس User.Read اور Admin.Write ہیں):

اب کلائنٹ کہتا ہے

```text
Error initializing client: Error: Error POSTing to endpoint (HTTP 403): Forbidden - insufficient scopes
```

اور آپ سرور کے ٹرمینل میں دیکھ سکتے ہیں کہ یہ کہتا ہے:

```text
User exists
```

اور یہ اس پوائنٹ سے آگے نہیں بڑھتا۔

یا تو اس اسکوپ "User.Write" کو شامل کریں اور `npm run generate` چلائیں اور کلائنٹ کو دوبارہ چلائیں یا سرور کوڈ کو واپس تبدیل کریں۔

---

**ڈسکلیمر**:  
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کا استعمال کرتے ہوئے ترجمہ کی گئی ہے۔ ہم درستگی کے لیے کوشش کرتے ہیں، لیکن براہ کرم آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا غیر درستیاں ہو سکتی ہیں۔ اصل دستاویز کو اس کی اصل زبان میں مستند ذریعہ سمجھا جانا چاہیے۔ اہم معلومات کے لیے، پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ ہم اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کے ذمہ دار نہیں ہیں۔