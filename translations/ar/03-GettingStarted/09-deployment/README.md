# نشر خوادم MCP

> [!NOTE]
> تستخدم أمثلة التكوين التي تستهدف نقطة نهاية `/sse` بروتوكول HTTP+SSE القديم للنقل. تستخدم خوادم MCP `2026-07-28` البعيدة بروتوكول HTTP قابل للبث عادة عند نقطة نهاية محددة من الخادم مثل `/mcp`.
> النقل. خوادم MCP `2026-07-28` البعيدة تستخدم بروتوكول HTTP قابل للبث، عادة عند نقطة نهاية يحددها الخادم مثل `/mcp`.




## نظرة عامة

يغطي هذا الدرس كيفية نشر تطبيق خادم MCP الخاص بك.

## أهداف التعلم

بحلول نهاية هذا الدرس، ستكون قادرًا على:

- تقييم نهج النشر المختلفة.
- نشر تطبيقك.

## التطوير والنشر المحلي

إذا كان من المفترض أن يتم استخدام الخادم الخاص بك عن طريق تشغيله على جهاز المستخدمين، يمكنك اتباع الخطوات التالية:

1. **قم بتنزيل الخادم**. إذا لم تكن قد كتبت الخادم، فقم بتنزيله أولًا على جهازك.
1. **ابدأ عملية الخادم**: شغّل تطبيق خادم MCP الخاص بك

بالنسبة لـ SSE (غير مطلوب لخادم نوع stdio)

1. **قم بتكوين الشبكة**: تأكد من أن الخادم يمكن الوصول إليه على المنفذ المتوقع
1. **اتصل بالعملاء**: استخدم عناوين الاتصال المحلية مثل `http://localhost:3000`

## النشر على السحابة

يمكن نشر خوادم MCP على منصات سحابية متنوعة:

- **الدوال بدون خادم**: نشر خوادم MCP خفيفة الوزن كدوال بدون خادم
- **خدمات الحاويات**: استخدم خدمات مثل Azure Container Apps، AWS ECS، أو Google Cloud Run
- **كوبيرنيتس**: نشر وإدارة خوادم MCP في مجموعات Kubernetes لتحقيق توافر عالٍ

### مثال: تطبيقات حاويات Azure

تدعم تطبيقات حاويات Azure نشر خوادم MCP. لا يزال العمل جارياً عليها وتدعم حالياً خوادم SSE.

إليك كيفية المتابعة:

1. استنساخ المستودع:

  ```sh
  git clone https://github.com/anthonychu/azure-container-apps-mcp-sample.git
  ```

1. شغّله محليًا لاختبار الأمور:

  ```sh
  uv venv
  uv sync

  # لينكس/ماك أو إس
  export API_KEYS=<AN_API_KEY>
  # ويندوز
  set API_KEYS=<AN_API_KEY>

  uv run fastapi dev main.py
  ```

1. لتجربته محليًا، أنشئ ملف *mcp.json* في مجلد *.vscode* وأضف المحتوى التالي:

  ```json
  {
      "inputs": [
          {
              "type": "promptString",
              "id": "weather-api-key",
              "description": "Weather API Key",
              "password": true
          }
      ],
      "servers": {
          "weather-sse": {
              "type": "sse",
              "url": "http://localhost:8000/sse",
              "headers": {
                  "x-api-key": "${input:weather-api-key}"
              }
          }
      }
  }
  ```

  بمجرد بدء خادم SSE، يمكنك النقر على أيقونة التشغيل في ملف JSON، يجب أن ترى الآن الأدوات على الخادم يتم التقاطها بواسطة GitHub Copilot، انظر أيقونة الأداة.

1. للنشر، شغل الأمر التالي:

  ```sh
  az containerapp up -g <RESOURCE_GROUP_NAME> -n weather-mcp --environment mcp -l westus --env-vars API_KEYS=<AN_API_KEY> --source .
  ```

هذا كل شيء، انشره محليًا، وانشره على Azure من خلال هذه الخطوات.

## موارد إضافية

- [وظائف Azure + MCP](https://learn.microsoft.com/en-us/samples/azure-samples/remote-mcp-functions-dotnet/remote-mcp-functions-dotnet/)
- [مقال حول Azure Container Apps](https://techcommunity.microsoft.com/blog/appsonazureblog/host-remote-mcp-servers-in-azure-container-apps/4403550)
- [مستودع Azure Container Apps MCP](https://github.com/anthonychu/azure-container-apps-mcp-sample)


## ماذا بعد

- التالي: [مواضيع متقدمة للخادم](../10-advanced/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**تنويه**:
تمت ترجمة هذا المستند باستخدام خدمة الترجمة بالذكاء الاصطناعي [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى للدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الرسمي والمعتمد. للمعلومات الهامة، يُنصح بالاستعانة بترجمة بشرية محترفة. نحن غير مسؤولين عن أي سوء فهم أو تفسير ناتج عن استخدام هذه الترجمة.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->