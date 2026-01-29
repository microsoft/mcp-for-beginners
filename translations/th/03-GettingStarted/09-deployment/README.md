# การติดตั้ง MCP Servers

การติดตั้งเซิร์ฟเวอร์ MCP ของคุณช่วยให้ผู้อื่นสามารถเข้าถึงเครื่องมือและทรัพยากรต่างๆ นอกเหนือจากสภาพแวดล้อมในเครื่องของคุณ มีหลายวิธีในการติดตั้งที่ควรพิจารณา ขึ้นอยู่กับความต้องการด้านการขยายตัว ความน่าเชื่อถือ และความง่ายในการจัดการ ด้านล่างนี้คุณจะพบคำแนะนำสำหรับการติดตั้ง MCP servers ทั้งในเครื่อง ในคอนเทนเนอร์ และบนคลาวด์

## ภาพรวม

บทเรียนนี้ครอบคลุมวิธีการติดตั้งแอป MCP Server ของคุณ

## วัตถุประสงค์การเรียนรู้

เมื่อจบบทเรียนนี้ คุณจะสามารถ:

- ประเมินวิธีการติดตั้งที่แตกต่างกัน
- ติดตั้งแอปของคุณ

## การพัฒนาและติดตั้งในเครื่อง

ถ้าเซิร์ฟเวอร์ของคุณถูกออกแบบให้ใช้งานบนเครื่องของผู้ใช้ คุณสามารถทำตามขั้นตอนดังนี้:

1. **ดาวน์โหลดเซิร์ฟเวอร์** หากคุณไม่ได้เขียนเซิร์ฟเวอร์เอง ให้ดาวน์โหลดมาไว้ในเครื่องก่อน
1. **เริ่มกระบวนการเซิร์ฟเวอร์**: รันแอป MCP server ของคุณ

สำหรับ SSE (ไม่จำเป็นสำหรับเซิร์ฟเวอร์แบบ stdio)

1. **ตั้งค่าเครือข่าย**: ตรวจสอบให้แน่ใจว่าเซิร์ฟเวอร์สามารถเข้าถึงได้ผ่านพอร์ตที่กำหนด
1. **เชื่อมต่อไคลเอนต์**: ใช้ URL การเชื่อมต่อในเครื่อง เช่น `http://localhost:3000`

## การติดตั้งบนคลาวด์

MCP servers สามารถติดตั้งบนแพลตฟอร์มคลาวด์ต่างๆ ได้ดังนี้:

- **Serverless Functions**: ติดตั้ง MCP servers ขนาดเล็กในรูปแบบฟังก์ชันแบบไม่มีเซิร์ฟเวอร์
- **Container Services**: ใช้บริการอย่าง Azure Container Apps, AWS ECS หรือ Google Cloud Run
- **Kubernetes**: ติดตั้งและจัดการ MCP servers ในคลัสเตอร์ Kubernetes เพื่อความพร้อมใช้งานสูง

### ตัวอย่าง: Azure Container Apps

Azure Container Apps รองรับการติดตั้ง MCP Servers ซึ่งยังอยู่ในระหว่างการพัฒนาและปัจจุบันรองรับเฉพาะเซิร์ฟเวอร์แบบ SSE

วิธีการทำมีดังนี้:

1. โคลนรีโป:

  ```sh
  git clone https://github.com/anthonychu/azure-container-apps-mcp-sample.git
  ```

1. รันในเครื่องเพื่อลองทดสอบ:

  ```sh
  uv venv
  uv sync

  # linux/macOS
  export API_KEYS=<AN_API_KEY>
  # windows
  set API_KEYS=<AN_API_KEY>

  uv run fastapi dev main.py
  ```

1. เพื่อทดสอบในเครื่อง ให้สร้างไฟล์ *mcp.json* ในไดเรกทอรี *.vscode* และเพิ่มเนื้อหาดังนี้:

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

  เมื่อเซิร์ฟเวอร์ SSE เริ่มทำงานแล้ว คุณสามารถคลิกไอคอนเล่นในไฟล์ JSON ได้ คุณจะเห็นเครื่องมือบนเซิร์ฟเวอร์ถูก GitHub Copilot ดึงขึ้นมา ดูที่ไอคอนเครื่องมือ

1. เมื่อต้องการติดตั้ง ให้รันคำสั่งดังนี้:

  ```sh
  az containerapp up -g <RESOURCE_GROUP_NAME> -n weather-mcp --environment mcp -l westus --env-vars API_KEYS=<AN_API_KEY> --source .
  ```

เท่านี้ก็เสร็จเรียบร้อย ติดตั้งในเครื่องหรือติดตั้งบน Azure ตามขั้นตอนนี้ได้เลย

## แหล่งข้อมูลเพิ่มเติม

- [Azure Functions + MCP](https://learn.microsoft.com/en-us/samples/azure-samples/remote-mcp-functions-dotnet/remote-mcp-functions-dotnet/)
- [บทความ Azure Container Apps](https://techcommunity.microsoft.com/blog/appsonazureblog/host-remote-mcp-servers-in-azure-container-apps/4403550)
- [รีโป Azure Container Apps MCP](https://github.com/anthonychu/azure-container-apps-mcp-sample)

## ต่อไป

- ต่อไป: [Practical Implementation](../../04-PracticalImplementation/README.md)

**ข้อจำกัดความรับผิดชอบ**:  
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษาอัตโนมัติ [Co-op Translator](https://github.com/Azure/co-op-translator) แม้เราจะพยายามให้ความถูกต้องสูงสุด แต่โปรดทราบว่าการแปลอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาต้นทางถือเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ ขอแนะนำให้ใช้บริการแปลโดยผู้เชี่ยวชาญมนุษย์ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความผิดที่เกิดขึ้นจากการใช้การแปลนี้