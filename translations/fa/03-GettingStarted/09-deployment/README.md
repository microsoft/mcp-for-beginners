# استقرار سرورهای MCP

استقرار سرور MCP شما این امکان را می‌دهد که دیگران نیز به ابزارها و منابع آن فراتر از محیط محلی شما دسترسی داشته باشند. بسته به نیازهای شما برای مقیاس‌پذیری، قابلیت اطمینان و سهولت مدیریت، استراتژی‌های مختلفی برای استقرار وجود دارد. در ادامه راهنمایی‌هایی برای استقرار سرورهای MCP به صورت محلی، در کانتینرها و در فضای ابری خواهید یافت.

## بررسی اجمالی

این درس نحوه استقرار اپلیکیشن MCP Server شما را پوشش می‌دهد.

## اهداف یادگیری

در پایان این درس، قادر خواهید بود:

- روش‌های مختلف استقرار را ارزیابی کنید.
- اپلیکیشن خود را مستقر کنید.

## توسعه و استقرار محلی

اگر سرور شما قرار است توسط اجرای آن روی ماشین کاربر مصرف شود، می‌توانید مراحل زیر را دنبال کنید:

1. **دانلود سرور**. اگر سرور را خودتان ننوشته‌اید، ابتدا آن را روی ماشین خود دانلود کنید.  
1. **شروع فرایند سرور**: اپلیکیشن MCP server خود را اجرا کنید.

برای SSE (نیاز به آن برای سرور نوع stdio نیست)

1. **پیکربندی شبکه**: اطمینان حاصل کنید سرور بر روی پورت مورد انتظار قابل دسترسی است.  
1. **اتصال کلاینت‌ها**: از URLهای اتصال محلی مانند `http://localhost:3000` استفاده کنید.

## استقرار ابری

سرورهای MCP می‌توانند روی پلتفرم‌های ابری مختلف مستقر شوند:

- **توابع بدون سرور**: استقرار سرورهای سبک MCP به‌عنوان توابع بدون سرور  
- **خدمات کانتینر**: استفاده از خدماتی مانند Azure Container Apps، AWS ECS، یا Google Cloud Run  
- **کوبرنتیز (Kubernetes)**: استقرار و مدیریت سرورهای MCP در کلاسترهای کوبرنتیز برای دسترس‌پذیری بالا

### مثال: Azure Container Apps

Azure Container Apps از استقرار سرورهای MCP پشتیبانی می‌کند. این سرویس هنوز در مرحله توسعه است و در حال حاضر سرورهای SSE را پشتیبانی می‌کند.

در اینجا نحوه انجام آن را خواهید دید:

1. یک مخزن (repo) را کلون کنید:

  ```sh
  git clone https://github.com/anthonychu/azure-container-apps-mcp-sample.git
  ```

1. آن را به صورت محلی اجرا کنید تا عملکرد را تست کنید:

  ```sh
  uv venv
  uv sync

  # لینوکس/مک‌اواس
  export API_KEYS=<AN_API_KEY>
  # ویندوز
  set API_KEYS=<AN_API_KEY>

  uv run fastapi dev main.py
  ```

1. برای آزمایش محلی، یک فایل *mcp.json* در فهرست *.vscode* بسازید و محتوای زیر را اضافه کنید:

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

 پس از راه‌اندازی سرور SSE، می‌توانید روی آیکون پخش در فایل JSON کلیک کنید؛ باید اکنون ابزارها روی سرور توسط GitHub Copilot شناسایی شوند، آیکون Tool را ببینید.

1. برای استقرار، دستور زیر را اجرا کنید:

  ```sh
  az containerapp up -g <RESOURCE_GROUP_NAME> -n weather-mcp --environment mcp -l westus --env-vars API_KEYS=<AN_API_KEY> --source .
  ```

همین است، آن را محلی مستقر کنید و با این مراحل به Azure هم منتقل کنید.

## منابع بیشتر

- [Azure Functions + MCP](https://learn.microsoft.com/en-us/samples/azure-samples/remote-mcp-functions-dotnet/remote-mcp-functions-dotnet/)
- [مقاله Azure Container Apps](https://techcommunity.microsoft.com/blog/appsonazureblog/host-remote-mcp-servers-in-azure-container-apps/4403550)
- [مخزن MCP برای Azure Container Apps](https://github.com/anthonychu/azure-container-apps-mcp-sample)

## گام بعدی

- بعدی: [موضوعات پیشرفته سرور](../10-advanced/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**سلب مسئولیت**:  
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما برای دقت تلاش می‌کنیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است شامل خطاها یا نادرستی‌هایی باشند. سند اصلی به زبان بومی آن باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حیاتی، ترجمه حرفه‌ای انسانی توصیه می‌شود. ما مسئول هیچ‌گونه سوءتفاهم یا برداشت نادرستی که از استفاده از این ترجمه به وجود آید، نیستیم.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->