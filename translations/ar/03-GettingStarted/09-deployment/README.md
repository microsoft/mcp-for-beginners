# نشر خوادم MCP

يتيح نشر خادم MCP الخاص بك للآخرين الوصول إلى أدواته وموارده خارج بيئتك المحلية. هناك عدة استراتيجيات للنشر يمكن النظر فيها، حسب متطلباتك من حيث القابلية للتوسع، والموثوقية، وسهولة الإدارة. أدناه ستجد إرشادات لنشر خوادم MCP محليًا، في الحاويات، وعلى السحابة.

## نظرة عامة

تغطي هذه الدرس كيفية نشر تطبيق خادم MCP الخاص بك.

## أهداف التعلم

بنهاية هذا الدرس، ستكون قادرًا على:

- تقييم طرق النشر المختلفة.
- نشر تطبيقك.

## التطوير والنشر المحلي

إذا كان من المفترض أن يتم استخدام خادمك عن طريق تشغيله على جهاز المستخدم، يمكنك اتباع الخطوات التالية:

1. **تحميل الخادم**. إذا لم تكن قد كتبت الخادم، فقم بتحميله أولاً إلى جهازك.
1. **تشغيل عملية الخادم**: قم بتشغيل تطبيق خادم MCP الخاص بك.

بالنسبة لـ SSE (غير مطلوب لخادم نوع stdio)

1. **تكوين الشبكة**: تأكد من أن الخادم متاح على المنفذ المتوقع.
1. **ربط العملاء**: استخدم عناوين الاتصال المحلية مثل `http://localhost:3000`

## النشر على السحابة

يمكن نشر خوادم MCP على منصات سحابية مختلفة:

- **الدوال بدون خادم**: نشر خوادم MCP خفيفة الوزن كدوال بدون خادم.
- **خدمات الحاويات**: استخدام خدمات مثل Azure Container Apps، AWS ECS، أو Google Cloud Run.
- **Kubernetes**: نشر وإدارة خوادم MCP في مجموعات Kubernetes لتحقيق توافر عالي.

### مثال: Azure Container Apps

تدعم Azure Container Apps نشر خوادم MCP. لا يزال هذا العمل قيد التطوير ويدعم حاليًا خوادم SSE.

إليك كيفية القيام بذلك:

1. استنساخ مستودع:

  ```sh
  git clone https://github.com/anthonychu/azure-container-apps-mcp-sample.git
  ```

1. تشغيله محليًا لاختبار الأمور:

  ```sh
  uv venv
  uv sync

  # linux/macOS
  export API_KEYS=<AN_API_KEY>
  # windows
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

  بمجرد بدء خادم SSE، يمكنك النقر على أيقونة التشغيل في ملف JSON، يجب أن ترى الآن الأدوات على الخادم يتم التقاطها بواسطة GitHub Copilot، انظر إلى أيقونة الأداة.

1. للنشر، شغّل الأمر التالي:

  ```sh
  az containerapp up -g <RESOURCE_GROUP_NAME> -n weather-mcp --environment mcp -l westus --env-vars API_KEYS=<AN_API_KEY> --source .
  ```

ها قد انتهيت، انشره محليًا، وانشره على Azure من خلال هذه الخطوات.

## موارد إضافية

- [Azure Functions + MCP](https://learn.microsoft.com/en-us/samples/azure-samples/remote-mcp-functions-dotnet/remote-mcp-functions-dotnet/)
- [مقال Azure Container Apps](https://techcommunity.microsoft.com/blog/appsonazureblog/host-remote-mcp-servers-in-azure-container-apps/4403550)
- [مستودع Azure Container Apps MCP](https://github.com/anthonychu/azure-container-apps-mcp-sample)

## ما التالي

- التالي: [التنفيذ العملي](../../04-PracticalImplementation/README.md)

**إخلاء المسؤولية**:  
تمت ترجمة هذا المستند باستخدام خدمة الترجمة الآلية [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى لتحقيق الدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الموثوق به. للمعلومات الهامة، يُنصح بالاعتماد على الترجمة البشرية المهنية. نحن غير مسؤولين عن أي سوء فهم أو تفسير ناتج عن استخدام هذه الترجمة.