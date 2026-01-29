# تشغيل العينة

## تثبيت التبعيات

```sh
npm install
```

## البناء

```sh
npm run build
```

## إنشاء الرموز

```sh
npm run generate
```

هذا ينشئ رمزًا في ملف *.env*. سيقوم العميل بقراءة هذا الملف.

## تشغيل الكود

ابدأ الخادم باستخدام:

```sh
npm start
```

قم بتشغيل العميل، في نافذة طرفية منفصلة باستخدام:

```sh
npm run client
```

في نافذة طرفية الخادم، يجب أن ترى مخرجات مشابهة لـ:

```text
User exists
User has required scopes
Middleware executed
```

وفي نافذة طرفية العميل، يجب أن ترى مخرجات مشابهة لـ:

```text
Connected to MCP server with session ID: c1e50d7b-acff-4f11-8f96-5ae490ca1eaa
Available tools: { tools: [ { name: 'process-files', inputSchema: [Object] } ] }
Client disconnected.
Exiting...
```

### تغيير الأمور

لنتأكد من فهمنا للنطاقات. ابحث عن الملف *server.ts* وهذا الكود:

```typescript
 if(!hasScopes(token, ["User.Read"])){
        res.status(403).send('Forbidden - insufficient scopes');
    }
```

هذا يشير إلى أن الرمز الممرر يحتاج إلى أن يحتوي على "User.Read"، دعنا نغير ذلك إلى "User.Write". الآن قم بتشغيل `npm run build` وأعد تشغيل الخادم باستخدام `npm start`. يجب أن ترى الآن فشل المصادقة لأننا لا نملك هذا النطاق (لدينا User.Read و Admin.Write):

العميل الآن يقول

```text
Error initializing client: Error: Error POSTing to endpoint (HTTP 403): Forbidden - insufficient scopes
```

ويمكنك أن ترى في نافذة طرفية الخادم أنه يقول:

```text
User exists
```

وأنه لا يتجاوز هذه النقطة.

إما أن تضيف هذا النطاق "User.Write" وتشغل `npm run generate` ثم تعيد تشغيل العميل، أو تعيد الكود في الخادم إلى حالته السابقة.

---

**إخلاء المسؤولية**:  
تم ترجمة هذا المستند باستخدام خدمة الترجمة بالذكاء الاصطناعي [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى لتحقيق الدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الرسمي. للحصول على معلومات حاسمة، يُوصى بالترجمة البشرية الاحترافية. نحن غير مسؤولين عن أي سوء فهم أو تفسيرات خاطئة ناتجة عن استخدام هذه الترجمة.