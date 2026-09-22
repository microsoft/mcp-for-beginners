# กรณีศึกษา: เปิดเผย REST API ใน API Management เป็นเซิร์ฟเวอร์ MCP

Azure API Management เป็นบริการที่ให้เกตเวย์อยู่เหนือ API Endpoints ของคุณ วิธีการทำงานก็คือ Azure API Management ทำหน้าที่เหมือนพร็อกซีอยู่หน้าของ API ของคุณและสามารถตัดสินใจว่าจะทำอย่างไรกับคำขอที่เข้ามา

ด้วยการใช้มัน คุณจะได้รับคุณสมบัติมากมาย เช่น:

- **ความปลอดภัย** คุณสามารถใช้ทุกอย่างตั้งแต่ API keys, JWT ถึง managed identity
- **การจำกัดอัตราการเรียกใช้งาน (Rate limiting)** คุณสมบัติที่ยอดเยี่ยมคือการสามารถกำหนดจำนวนครั้งที่รับได้ในช่วงเวลาหนึ่ง ซึ่งช่วยให้แน่ใจว่าผู้ใช้ทุกคนจะได้รับประสบการณ์ที่ดี และยังช่วยป้องกันไม่ให้บริการของคุณถูกคำขอเกินกว่าที่รับไหว
- **การขยายและการปรับสมดุลโหลด** คุณสามารถตั้งค่า endpoint จำนวนหนึ่งเพื่อปรับสมดุลโหลดและยังสามารถกำหนดวิธี “load balance” ได้
- **คุณสมบัติปัญญาประดิษฐ์ เช่น semantic caching, token limit และ token monitoring และอื่นๆ** คุณสมบัติเหล่านี้ช่วยให้การตอบสนองดีขึ้นและช่วยให้คุณควบคุมการใช้โทเค็นได้ [อ่านเพิ่มเติมที่นี่](https://learn.microsoft.com/en-us/azure/api-management/genai-gateway-capabilities)

## ทำไมต้อง MCP + Azure API Management?

Model Context Protocol กำลังกลายเป็นมาตรฐานสำหรับแอป AI agentic และวิธีการเปิดเผยเครื่องมือและข้อมูลในรูปแบบที่สอดคล้องกัน Azure API Management เป็นตัวเลือกที่ดีเมื่อคุณต้องการ “จัดการ” APIs MCP Servers มักจะรวมเข้ากับ APIs อื่นเพื่อแก้ไขคำขอไปยังเครื่องมือต่างๆ ตัวอย่าง ดังนั้นการรวม Azure API Management กับ MCP จึงมีความสมเหตุสมผลมาก

## ภาพรวม

ในกรณีใช้งานนี้ เราจะเรียนรู้วิธีเปิดเผย API endpoints เป็น MCP Server ด้วยวิธีนี้ เราสามารถทำให้ endpoints เหล่านี้เป็นส่วนหนึ่งของแอป agentic ได้อย่างง่ายดายพร้อมกับใช้ประโยชน์จากคุณสมบัติของ Azure API Management

## คุณสมบัติหลัก

- คุณเลือกวิธีของ endpoint ที่ต้องการเปิดเผยเป็นเครื่องมือ
- คุณสมบัติเพิ่มเติมที่ได้รับขึ้นกับการตั้งค่าในส่วน policy สำหรับ API ของคุณ แต่ในที่นี้เราจะแสดงวิธีการเพิ่มการจำกัดอัตราเรียกใช้งาน

## ขั้นตอนก่อนหน้า: นำเข้า API

หากคุณมี API อยู่ใน Azure API Management แล้ว ยอดเยี่ยม คุณสามารถข้ามขั้นตอนนี้ไปได้ หากไม่มีก็ลองดูที่ลิงก์นี้ [นำเข้า API ไปยัง Azure API Management](https://learn.microsoft.com/en-us/azure/api-management/import-and-publish#import-and-publish-a-backend-api)

## เปิดเผย API เป็น MCP Server

เพื่อเปิดเผย API endpoints ให้ทำตามขั้นตอนเหล่านี้:

1. ไปที่ Azure Portal ที่ลิงก์ <https://portal.azure.com/?Microsoft_Azure_ApiManagement=mcp> 
ไปยังตัวอย่าง API Management ของคุณ

1. ในเมนูด้านซ้าย เลือก APIs > MCP Servers > + สร้าง MCP Server ใหม่

1. ใน API ให้เลือก REST API ที่จะเปิดเผยเป็น MCP server

1. เลือก API Operations หนึ่งหรือมากกว่าที่จะเปิดเผยเป็นเครื่องมือ คุณสามารถเลือกทุก operation หรือเลือกบาง operation ก็ได้

    ![เลือกเมธอดที่จะเปิดเผย](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/create-mcp-server-small.png)


1. เลือก **สร้าง (Create)**

1. ไปที่เมนู **APIs** และ **MCP Servers** คุณจะเห็นดังนี้:

    ![เห็น MCP Server ในหน้าหลัก](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-list.png)

    MCP server ถูกสร้างขึ้นและ API operations ได้เปิดเผยเป็นเครื่องมือ MCP server จะแสดงในหน้าต่าง MCP Servers คอลัมน์ URL แสดง endpoint ของ MCP server ที่คุณสามารถเรียกเพื่อทดสอบหรือใช้ในแอปไคลเอนต์

## ทางเลือก: กำหนดนโยบาย

Azure API Management มีแนวคิดหลักของนโยบายที่คุณตั้งกฎต่าง ๆ สำหรับ endpoints เช่น การจำกัดอัตราการเรียกใช้งานหรือ semantic caching ซึ่งนโยบายเหล่านี้ถูกเขียนในรูปแบบ XML

นี่คือวิธีตั้งค่านโยบายจำกัดอัตราการเรียกใช้งานสำหรับ MCP Server:

1. ในพอร์ทัล ภายใต้ APIs เลือก **MCP Servers**

1. เลือก MCP server ที่คุณสร้างไว้

1. ในเมนูซ้ายใต้ MCP เลือก **Policies**

1. ในตัวแก้ไขนโยบาย ให้เพิ่มหรือแก้ไขนโยบายที่ต้องการใช้กับเครื่องมือของ MCP server นโยบายนี้ถูกกำหนดในรูปแบบ XML เช่น คุณสามารถเพิ่มนโยบายจำกัดเรียกใช้งานเครื่องมือ MCP server (ในตัวอย่างนี้ 5 ครั้งต่อ 30 วินาทีต่อที่อยู่ IP ของลูกค้า) นี่คือตัวอย่าง XML ที่จะทำให้จำกัดอัตราการใช้งาน:

    ```xml
     <rate-limit-by-key calls="5" 
       renewal-period="30" 
       counter-key="@(context.Request.IpAddress)" 
       remaining-calls-variable-name="remainingCallsPerIP" 
    />
    ```

    นี่คือตัวอย่างภาพตัวแก้ไขนโยบาย:

    ![ตัวแก้ไขนโยบาย](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-policies-small.png)
 
## ทดลองใช้งาน

ให้เรามั่นใจว่า MCP Server ของเราทำงานตามที่ตั้งใจไว้

> [!NOTE]
> Azure API Management เปิดเผยเซิร์ฟเวอร์นี้ผ่าน Streamable
> HTTP `/mcp` endpoint ปัจจุบัน โปรโตคอลเก่า HTTP+SSE `/sse` ถูกเลิกใช้แล้วและ
> ควรใช้เฉพาะกับไคลเอนต์รุ่นเก่าเท่านั้น

สำหรับสิ่งนี้ เราจะใช้ Visual Studio Code และ GitHub Copilot โหมด Agent เราจะเพิ่ม MCP server ลงใน *mcp.json* เมื่อทำเช่นนี้ Visual Studio Code จะทำหน้าที่เป็นไคลเอนต์ที่มีความสามารถแบบ agentic และผู้ใช้ปลายทางจะสามารถพิมพ์คำสั่งและโต้ตอบกับเซิร์ฟเวอร์นั้นได้

มาดูวิธีเพิ่ม MCP server ใน Visual Studio Code:

1. ใช้คำสั่ง MCP: **Add Server จาก Command Palette** 

1. เมื่อต้องเลือกประเภท server ให้เลือก **HTTP (HTTP หรือ Server Sent Events)**

1. ป้อน URL Streamable HTTP ที่แสดงสำหรับ MCP server ใน API Management
    ตัวอย่างเช่น:
    `https://<apim-service-name>.azure-api.net/<api-name>-mcp/mcp`

1. ป้อน ID server ที่คุณเลือก ไม่ใช่ค่าที่สำคัญแต่จะช่วยให้คุณจำได้ว่าเป็นเซิร์ฟเวอร์ตัวไหน

1. เลือกว่าจะบันทึกการตั้งค่าไว้ใน workspace settings หรือ user settings

  - **Workspace settings** - การตั้งค่าเซิร์ฟเวอร์จะถูกบันทึกในไฟล์ .vscode/mcp.json ที่ใช้ได้เฉพาะใน workspace ปัจจุบัน

    *mcp.json*

    ```json
    "servers": {
        "APIM petstore" : {
            "type": "http",
            "url": "url-to-mcp-server/mcp"
        }
    }
    ```

  - **User settings** - การตั้งค่าเซิร์ฟเวอร์ถูกเพิ่มลงในไฟล์ *settings.json* ทั่วไปของคุณและสามารถใช้ได้ในทุก workspace การตั้งค่าจะมีลักษณะคล้ายตัวอย่างนี้:

    ![การตั้งค่าผู้ใช้](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-servers-visual-studio-code.png)

1. คุณยังต้องเพิ่มการตั้งค่า header เพื่อให้ตรวจสอบสิทธิ์กับ Azure API Management ได้อย่างถูกต้อง โดยใช้ header ที่ชื่อว่า **Ocp-Apim-Subscription-Key**

    - นี่คือวิธีเพิ่มลงใน settings:

    ![เพิ่ม header เพื่อการตรวจสอบสิทธิ์](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-with-header-visual-studio-code.png) ซึ่งจะทำให้มีการแสดง prompt ให้ป้อนค่า API key ที่คุณสามารถหาจาก Azure Portal สำหรับ API Management ที่คุณใช้งาน

   - หากต้องการเพิ่มลงใน *mcp.json* แทน สามารถเพิ่มแบบนี้:

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

### ใช้งานโหมด Agent

ตอนนี้เราตั้งค่าพร้อมแล้วใน settings หรือใน *.vscode/mcp.json* มาลองใช้งานกัน

ควรจะมีไอคอนเครื่องมืออย่างนี้ ซึ่งแสดงเครื่องมือที่เปิดเผยจากเซิร์ฟเวอร์ของคุณ:

![เครื่องมือจากเซิร์ฟเวอร์](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/tools-button-visual-studio-code.png)

1. คลิกที่ไอคอนเครื่องมือ แล้วคุณจะเห็นรายการเครื่องมือดังนี้:

    ![เครื่องมือ](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/select-tools-visual-studio-code.png)

1. ป้อนข้อความในแชทเพื่อเรียกใช้งานเครื่องมือ เช่น ถ้าคุณเลือกเครื่องมือเพื่อขอข้อมูลเกี่ยวกับคำสั่งซื้อ คุณสามารถถามเอเจนต์เกี่ยวกับคำสั่งซื้อนั้นได้ ตัวอย่างคำสั่ง:

    ```text
    get information from order 2
    ```

    ตอนนี้คุณจะเห็นไอคอนเครื่องมือถามว่าต้องการเรียกใช้เครื่องมือต่อหรือไม่ เลือกดำเนินการต่อ คุณจะเห็นผลลัพธ์ดังนี้:

    ![ผลลัพธ์จากคำสั่ง](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/chat-results-visual-studio-code.png)

    **สิ่งที่คุณเห็นด้านบนขึ้นอยู่กับเครื่องมือที่ตั้งค่าไว้ แต่แนวคิดคือคุณจะได้รับคำตอบเป็นข้อความแบบนี้**


## เอกสารอ้างอิง

นี่คือวิธีที่คุณจะเรียนรู้เพิ่มเติม:

- [บทเรียนเกี่ยวกับ Azure API Management และ MCP](https://learn.microsoft.com/en-us/azure/api-management/export-rest-mcp-server)
- [ตัวอย่าง Python: การรักษาความปลอดภัยเซิร์ฟเวอร์ MCP ระยะไกลโดยใช้ Azure API Management (ทดลอง)](https://github.com/Azure-Samples/remote-mcp-apim-functions-python)

- [ห้องปฏิบัติการอนุญาตไคลเอ็นต์ MCP](https://github.com/Azure-Samples/AI-Gateway/tree/main/labs/mcp-client-authorization)

- [ใช้ส่วนขยาย Azure API Management สำหรับ VS Code เพื่อนำเข้าและจัดการ APIs](https://learn.microsoft.com/en-us/azure/api-management/visual-studio-code-tutorial)

- [ลงทะเบียนและค้นหาเซิร์ฟเวอร์ MCP ระยะไกลใน Azure API Center](https://learn.microsoft.com/en-us/azure/api-center/register-discover-mcp-server)
- [AI Gateway](https://github.com/Azure-Samples/AI-Gateway) รีโพสยอดเยี่ยมที่แสดงความสามารถ AI มากมายกับ Azure API Management
- [เวิร์กช็อป AI Gateway](https://azure-samples.github.io/AI-Gateway/) มีเวิร์กช็อปโดยใช้ Azure Portal ซึ่งเป็นวิธีที่ดีในการเริ่มประเมินความสามารถ AI

## ต่อไปคืออะไร

- กลับไปที่: [ภาพรวมกรณีศึกษา](./README.md)
- ต่อไป: [ตัวอย่างตัวแทนท่องเที่ยว Azure AI](./travelagentsample.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ปฏิเสธความรับผิดชอบ**:
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษา AI [Co-op Translator](https://github.com/Azure/co-op-translator) ขณะที่เราพยายามให้ความถูกต้อง โปรดทราบว่าการแปลโดยอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาต้นทางควรถูกพิจารณาเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ แนะนำให้ใช้การแปลโดยมนุษย์มืออาชีพ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความที่ผิดพลาดที่เกิดขึ้นจากการใช้การแปลนี้
<!-- CO-OP TRANSLATOR DISCLAIMER END -->