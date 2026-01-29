# กรณีศึกษา: เปิดเผย REST API ใน API Management เป็นเซิร์ฟเวอร์ MCP

Azure API Management เป็นบริการที่ให้ Gateway อยู่บน API Endpoints ของคุณ วิธีการทำงานคือ Azure API Management ทำหน้าที่เป็นพร็อกซีที่อยู่ด้านหน้าของ API ของคุณ และสามารถตัดสินใจว่าจะทำอะไรกับคำขอที่เข้ามา

โดยการใช้งาน คุณจะได้รับฟีเจอร์มากมาย เช่น:

- **ความปลอดภัย** คุณสามารถใช้ทุกอย่างตั้งแต่ API keys, JWT ไปจนถึง managed identity
- **การจำกัดอัตรา** ฟีเจอร์ที่ยอดเยี่ยมคือการสามารถกำหนดจำนวนการเรียกที่ผ่านได้ในช่วงเวลาหนึ่ง ซึ่งช่วยให้ผู้ใช้ทุกคนมีประสบการณ์ที่ดีและป้องกันไม่ให้บริการของคุณถูกคำขอถล่ม
- **การปรับขนาดและการกระจายโหลด** คุณสามารถตั้งค่า endpoints หลายตัวเพื่อกระจายโหลด และยังสามารถกำหนดวิธีการ "load balance" ได้
- **ฟีเจอร์ AI เช่น semantic caching**, token limit และ token monitoring และอื่น ๆ ฟีเจอร์เหล่านี้ช่วยปรับปรุงการตอบสนองและช่วยให้คุณควบคุมการใช้ token ได้ [อ่านเพิ่มเติมที่นี่](https://learn.microsoft.com/en-us/azure/api-management/genai-gateway-capabilities)

## ทำไมต้อง MCP + Azure API Management?

Model Context Protocol กำลังกลายเป็นมาตรฐานสำหรับแอป AI แบบตัวแทน และวิธีการเปิดเผยเครื่องมือและข้อมูลในรูปแบบที่สอดคล้องกัน Azure API Management เป็นตัวเลือกที่เหมาะสมเมื่อคุณต้องการ "จัดการ" APIs เซิร์ฟเวอร์ MCP มักจะรวมเข้ากับ APIs อื่น ๆ เพื่อแก้ไขคำขอไปยังเครื่องมือ ตัวอย่างเช่น ดังนั้นการรวม Azure API Management และ MCP จึงมีเหตุผลที่ดี

## ภาพรวม

ในกรณีการใช้งานนี้ เราจะเรียนรู้วิธีเปิดเผย API endpoints เป็นเซิร์ฟเวอร์ MCP โดยการทำเช่นนี้ เราสามารถทำให้ endpoints เหล่านี้เป็นส่วนหนึ่งของแอปตัวแทนได้อย่างง่ายดาย พร้อมทั้งใช้ประโยชน์จากฟีเจอร์ของ Azure API Management

## ฟีเจอร์สำคัญ

- คุณสามารถเลือกวิธี endpoint ที่ต้องการเปิดเผยเป็นเครื่องมือ
- ฟีเจอร์เพิ่มเติมที่คุณได้รับขึ้นอยู่กับสิ่งที่คุณกำหนดค่าในส่วน policy สำหรับ API ของคุณ แต่ที่นี่เราจะแสดงวิธีการเพิ่มการจำกัดอัตรา

## ขั้นตอนเบื้องต้น: นำเข้า API

หากคุณมี API ใน Azure API Management อยู่แล้ว คุณสามารถข้ามขั้นตอนนี้ได้ หากไม่เป็นเช่นนั้น ดูลิงก์นี้ [การนำเข้า API ไปยัง Azure API Management](https://learn.microsoft.com/en-us/azure/api-management/import-and-publish#import-and-publish-a-backend-api)

## เปิดเผย API เป็นเซิร์ฟเวอร์ MCP

เพื่อเปิดเผย API endpoints ให้ทำตามขั้นตอนเหล่านี้:

1. ไปที่ Azure Portal และที่อยู่ต่อไปนี้ <https://portal.azure.com/?Microsoft_Azure_ApiManagement=mcp>  
ไปที่ instance ของ API Management ของคุณ

1. ในเมนูด้านซ้าย เลือก APIs > MCP Servers > + Create new MCP Server

1. ใน API เลือก REST API ที่ต้องการเปิดเผยเป็นเซิร์ฟเวอร์ MCP

1. เลือกหนึ่งหรือหลาย API Operations ที่ต้องการเปิดเผยเป็นเครื่องมือ คุณสามารถเลือกทุก operations หรือเฉพาะ operations ที่ต้องการ

    ![เลือกวิธีการที่จะเปิดเผย](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/create-mcp-server-small.png)

1. เลือก **Create**

1. ไปที่ตัวเลือกเมนู **APIs** และ **MCP Servers** คุณควรเห็นดังนี้:

    ![ดูเซิร์ฟเวอร์ MCP ในหน้าหลัก](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-list.png)

    เซิร์ฟเวอร์ MCP ถูกสร้างขึ้นและ API operations ถูกเปิดเผยเป็นเครื่องมือ เซิร์ฟเวอร์ MCP จะปรากฏในหน้าต่าง MCP Servers คอลัมน์ URL แสดง endpoint ของเซิร์ฟเวอร์ MCP ที่คุณสามารถเรียกใช้เพื่อทดสอบหรือในแอปพลิเคชันของลูกค้า

## ตัวเลือก: กำหนดค่ากฎ (Policies)

Azure API Management มีแนวคิดหลักของกฎ (Policies) ที่คุณสามารถตั้งค่ากฎต่าง ๆ สำหรับ endpoints เช่น การจำกัดอัตรา หรือ semantic caching กฎเหล่านี้ถูกเขียนในรูปแบบ XML

นี่คือวิธีการตั้งค่ากฎเพื่อจำกัดอัตราสำหรับเซิร์ฟเวอร์ MCP ของคุณ:

1. ในพอร์ทัล ภายใต้ APIs เลือก **MCP Servers**

1. เลือกเซิร์ฟเวอร์ MCP ที่คุณสร้างขึ้น

1. ในเมนูด้านซ้าย ภายใต้ MCP เลือก **Policies**

1. ในตัวแก้ไขกฎ เพิ่มหรือแก้ไขกฎที่คุณต้องการใช้กับเครื่องมือของเซิร์ฟเวอร์ MCP กฎถูกกำหนดในรูปแบบ XML ตัวอย่างเช่น คุณสามารถเพิ่มกฎเพื่อจำกัดการเรียกใช้เครื่องมือของเซิร์ฟเวอร์ MCP (ในตัวอย่างนี้ 5 ครั้งต่อ 30 วินาทีต่อ client IP address) นี่คือ XML ที่จะทำให้เกิดการจำกัดอัตรา:

    ```xml
     <rate-limit-by-key calls="5" 
       renewal-period="30" 
       counter-key="@(context.Request.IpAddress)" 
       remaining-calls-variable-name="remainingCallsPerIP" 
    />
    ```

    นี่คือภาพของตัวแก้ไขกฎ:

    ![ตัวแก้ไขกฎ](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-policies-small.png)

## ทดลองใช้งาน

มาทดสอบว่าเซิร์ฟเวอร์ MCP ของเราทำงานตามที่ตั้งใจไว้

สำหรับสิ่งนี้ เราจะใช้ Visual Studio Code และ GitHub Copilot ในโหมด Agent เราจะเพิ่มเซิร์ฟเวอร์ MCP ลงในไฟล์ *mcp.json* โดยการทำเช่นนี้ Visual Studio Code จะทำหน้าที่เป็นลูกค้าด้วยความสามารถแบบตัวแทน และผู้ใช้ปลายทางจะสามารถพิมพ์คำสั่งและโต้ตอบกับเซิร์ฟเวอร์ดังกล่าวได้

มาดูกันว่าจะเพิ่มเซิร์ฟเวอร์ MCP ใน Visual Studio Code ได้อย่างไร:

1. ใช้คำสั่ง MCP: **Add Server command จาก Command Palette**

1. เมื่อถูกถาม เลือกประเภทเซิร์ฟเวอร์: **HTTP (HTTP หรือ Server Sent Events)**

1. ป้อน URL ของเซิร์ฟเวอร์ MCP ใน API Management ตัวอย่าง: **https://<apim-service-name>.azure-api.net/<api-name>-mcp/sse** (สำหรับ SSE endpoint) หรือ **https://<apim-service-name>.azure-api.net/<api-name>-mcp/mcp** (สำหรับ MCP endpoint) สังเกตความแตกต่างระหว่าง transports คือ `/sse` หรือ `/mcp`

1. ป้อน server ID ที่คุณเลือก ค่านี้ไม่สำคัญมาก แต่จะช่วยให้คุณจำได้ว่า instance ของเซิร์ฟเวอร์นี้คืออะไร

1. เลือกว่าจะบันทึกการตั้งค่าไปยัง workspace settings หรือ user settings

  - **Workspace settings** - การตั้งค่าเซิร์ฟเวอร์จะถูกบันทึกในไฟล์ .vscode/mcp.json ที่มีเฉพาะใน workspace ปัจจุบัน

    *mcp.json*

    ```json
    "servers": {
        "APIM petstore" : {
            "type": "sse",
            "url": "url-to-mcp-server/sse"
        }
    }
    ```

    หรือหากคุณเลือก streaming HTTP เป็น transport จะมีความแตกต่างเล็กน้อย:

    ```json
    "servers": {
        "APIM petstore" : {
            "type": "http",
            "url": "url-to-mcp-server/mcp"
        }
    }
    ```

  - **User settings** - การตั้งค่าเซิร์ฟเวอร์จะถูกเพิ่มในไฟล์ *settings.json* ทั่วโลก และสามารถใช้งานได้ในทุก workspace การตั้งค่าจะมีลักษณะคล้ายกับดังนี้:

    ![การตั้งค่าผู้ใช้](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-servers-visual-studio-code.png)

1. คุณยังต้องเพิ่มการตั้งค่า header เพื่อให้แน่ใจว่ามีการตรวจสอบสิทธิ์อย่างถูกต้องกับ Azure API Management โดยใช้ header ที่เรียกว่า **Ocp-Apim-Subscription-Key**

    - นี่คือวิธีการเพิ่ม header ใน settings:

    ![การเพิ่ม header สำหรับการตรวจสอบสิทธิ์](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-with-header-visual-studio-code.png) ซึ่งจะทำให้มีการแสดง prompt เพื่อขอค่าคีย์ API ซึ่งคุณสามารถหาได้ใน Azure Portal สำหรับ instance ของ Azure API Management ของคุณ

   - หากต้องการเพิ่มใน *mcp.json* แทน คุณสามารถเพิ่มได้ดังนี้:

    ```json
    "inputs": [
      {
        "type": "promptString",
        "id": "apim_key",
        "description": "API Key for Azure API Management",
        "password": true
      }
    ]
    "servers": {
        "APIM petstore" : {
            "type": "http",
            "url": "url-to-mcp-server/mcp",
            "headers": {
                "Ocp-Apim-Subscription-Key": "Bearer ${input:apim_key}"
            }
        }
    }
    ```

### ใช้โหมด Agent

ตอนนี้เราตั้งค่าเสร็จแล้วใน settings หรือใน *.vscode/mcp.json* มาลองใช้งานกัน

ควรมีไอคอน Tools ดังนี้ ซึ่งเครื่องมือที่เปิดเผยจากเซิร์ฟเวอร์ของคุณจะปรากฏอยู่:

![เครื่องมือจากเซิร์ฟเวอร์](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/tools-button-visual-studio-code.png)

1. คลิกไอคอน Tools และคุณควรเห็นรายการเครื่องมือดังนี้:

    ![เครื่องมือ](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/select-tools-visual-studio-code.png)

1. ป้อนคำสั่งในแชทเพื่อเรียกใช้เครื่องมือ ตัวอย่างเช่น หากคุณเลือกเครื่องมือเพื่อรับข้อมูลเกี่ยวกับคำสั่งซื้อ คุณสามารถถามตัวแทนเกี่ยวกับคำสั่งซื้อ นี่คือตัวอย่างคำสั่ง:

    ```text
    get information from order 2
    ```

    คุณจะเห็นไอคอนเครื่องมือที่ขอให้คุณดำเนินการเรียกใช้เครื่องมือ เลือกเพื่อดำเนินการเรียกใช้เครื่องมือ คุณควรเห็นผลลัพธ์ดังนี้:

    ![ผลลัพธ์จากคำสั่ง](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/chat-results-visual-studio-code.png)

    **สิ่งที่คุณเห็นด้านบนขึ้นอยู่กับเครื่องมือที่คุณตั้งค่า แต่แนวคิดคือคุณจะได้รับการตอบกลับเป็นข้อความดังที่แสดงด้านบน**

## อ้างอิง

นี่คือวิธีที่คุณสามารถเรียนรู้เพิ่มเติม:

- [บทเรียนเกี่ยวกับ Azure API Management และ MCP](https://learn.microsoft.com/en-us/azure/api-management/export-rest-mcp-server)
- [ตัวอย่าง Python: การรักษาความปลอดภัยเซิร์ฟเวอร์ MCP ระยะไกลโดยใช้ Azure API Management (ทดลอง)](https://github.com/Azure-Samples/remote-mcp-apim-functions-python)

- [ห้องปฏิบัติการการอนุญาตลูกค้า MCP](https://github.com/Azure-Samples/AI-Gateway/tree/main/labs/mcp-client-authorization)

- [ใช้ส่วนขยาย Azure API Management สำหรับ VS Code เพื่อนำเข้าและจัดการ APIs](https://learn.microsoft.com/en-us/azure/api-management/visual-studio-code-tutorial)

- [ลงทะเบียนและค้นพบเซิร์ฟเวอร์ MCP ระยะไกลใน Azure API Center](https://learn.microsoft.com/en-us/azure/api-center/register-discover-mcp-server)
- [AI Gateway](https://github.com/Azure-Samples/AI-Gateway) โครงการที่ยอดเยี่ยมที่แสดงความสามารถ AI หลายอย่างด้วย Azure API Management
- [เวิร์กช็อป AI Gateway](https://azure-samples.github.io/AI-Gateway/) มีเวิร์กช็อปที่ใช้ Azure Portal ซึ่งเป็นวิธีที่ดีในการเริ่มต้นประเมินความสามารถ AI

**ข้อจำกัดความรับผิดชอบ**:  
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษา AI [Co-op Translator](https://github.com/Azure/co-op-translator) แม้ว่าเราจะพยายามให้การแปลมีความถูกต้อง แต่โปรดทราบว่าการแปลอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่แม่นยำ เอกสารต้นฉบับในภาษาต้นทางควรถือเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ แนะนำให้ใช้บริการแปลภาษาจากผู้เชี่ยวชาญที่เป็นมนุษย์ เราจะไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความที่ผิดพลาดซึ่งเกิดจากการใช้การแปลนี้