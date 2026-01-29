# تشغيل هذا المثال

يتطلب هذا المثال وجود نموذج لغة كبير (LLM) على العميل. يحتاج النموذج إلى أن تقوم إما بتشغيل هذا في Codespaces أو إعداد رمز وصول شخصي في GitHub ليعمل.

## -1- تثبيت التبعيات

```bash
npm install
```

## -3- تشغيل الخادم

```bash
npm run build
```

## -4- تشغيل العميل

```sh
npm run client
```

يجب أن ترى نتيجة مشابهة لـ:

```text
Asking server for available tools
MCPClient started on stdin/stdout
Querying LLM:  What is the sum of 2 and 3?
Making tool call
Calling tool add with args "{\"a\":2,\"b\":3}"
Tool result:  { content: [ { type: 'text', text: '5' } ] }
```

**إخلاء المسؤولية**:  
تمت ترجمة هذا المستند باستخدام خدمة الترجمة الآلية [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى لتحقيق الدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الموثوق به. للمعلومات الهامة، يُنصح بالترجمة البشرية المهنية. نحن غير مسؤولين عن أي سوء فهم أو تفسير ناتج عن استخدام هذه الترجمة.