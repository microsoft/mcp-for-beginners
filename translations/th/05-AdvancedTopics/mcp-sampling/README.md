# การสุ่มตัวอย่างในโปรโตคอล Model Context Protocol

การสุ่มตัวอย่างเป็นฟีเจอร์ที่ทรงพลังของ MCP ที่ช่วยให้เซิร์ฟเวอร์สามารถร้องขอการเติมข้อความจาก LLM ผ่านทางไคลเอนต์ได้ ทำให้เกิดพฤติกรรมตัวแทนอัจฉริยะในขณะที่ยังคงรักษาความปลอดภัยและความเป็นส่วนตัว การตั้งค่าการสุ่มตัวอย่างที่เหมาะสมสามารถปรับปรุงคุณภาพและประสิทธิภาพของการตอบกลับได้อย่างมาก MCP มีวิธีมาตรฐานในการควบคุมการสร้างข้อความของโมเดลด้วยพารามิเตอร์เฉพาะที่มีผลต่อความสุ่ม ความคิดสร้างสรรค์ และความสอดคล้อง

## บทนำ

ในบทเรียนนี้ เราจะสำรวจวิธีการตั้งค่าพารามิเตอร์การสุ่มตัวอย่างในคำขอ MCP และทำความเข้าใจกลไกโปรโตคอลพื้นฐานของการสุ่มตัวอย่าง

## วัตถุประสงค์การเรียนรู้

เมื่อจบบทเรียนนี้ คุณจะสามารถ:

- เข้าใจพารามิเตอร์การสุ่มตัวอย่างหลักที่มีใน MCP
- ตั้งค่าพารามิเตอร์การสุ่มตัวอย่างสำหรับกรณีการใช้งานต่างๆ
- นำการสุ่มตัวอย่างแบบกำหนดผลลัพธ์ได้มาใช้เพื่อให้ได้ผลลัพธ์ที่ทำซ้ำได้
- ปรับพารามิเตอร์การสุ่มตัวอย่างแบบไดนามิกตามบริบทและความชอบของผู้ใช้
- ใช้กลยุทธ์การสุ่มตัวอย่างเพื่อเพิ่มประสิทธิภาพของโมเดลในสถานการณ์ต่างๆ
- เข้าใจการทำงานของการสุ่มตัวอย่างในกระบวนการไคลเอนต์-เซิร์ฟเวอร์ของ MCP

## การทำงานของการสุ่มตัวอย่างใน MCP

กระบวนการสุ่มตัวอย่างใน MCP มีขั้นตอนดังนี้:

1. เซิร์ฟเวอร์ส่งคำขอ `sampling/createMessage` ไปยังไคลเอนต์
2. ไคลเอนต์ตรวจสอบคำขอและสามารถแก้ไขได้
3. ไคลเอนต์สุ่มตัวอย่างจาก LLM
4. ไคลเอนต์ตรวจสอบผลลัพธ์การเติมข้อความ
5. ไคลเอนต์ส่งผลลัพธ์กลับไปยังเซิร์ฟเวอร์

การออกแบบที่มีมนุษย์เป็นส่วนร่วมนี้ช่วยให้ผู้ใช้ยังคงควบคุมสิ่งที่ LLM เห็นและสร้างขึ้นได้

## ภาพรวมพารามิเตอร์การสุ่มตัวอย่าง

MCP กำหนดพารามิเตอร์การสุ่มตัวอย่างดังต่อไปนี้ที่สามารถตั้งค่าในคำขอของไคลเอนต์:

| พารามิเตอร์ | คำอธิบาย | ช่วงค่าทั่วไป |
|--------------|-----------|---------------|
| `temperature` | ควบคุมความสุ่มในการเลือกโทเค็น | 0.0 - 1.0 |
| `maxTokens` | จำนวนโทเค็นสูงสุดที่สร้างได้ | ค่าจำนวนเต็ม |
| `stopSequences` | ลำดับข้อความที่กำหนดเองเพื่อหยุดการสร้างเมื่อพบ | อาร์เรย์ของสตริง |
| `metadata` | พารามิเตอร์เพิ่มเติมเฉพาะผู้ให้บริการ | อ็อบเจ็กต์ JSON |

ผู้ให้บริการ LLM หลายรายรองรับพารามิเตอร์เพิ่มเติมผ่านฟิลด์ `metadata` ซึ่งอาจรวมถึง:

| พารามิเตอร์เสริมทั่วไป | คำอธิบาย | ช่วงค่าทั่วไป |
|-------------------------|-----------|---------------|
| `top_p` | การสุ่มแบบนิวเคลียส - จำกัดโทเค็นให้อยู่ในความน่าจะเป็นสะสมสูงสุด | 0.0 - 1.0 |
| `top_k` | จำกัดการเลือกโทเค็นให้อยู่ในตัวเลือกสูงสุด K | 1 - 100 |
| `presence_penalty` | ลงโทษโทเค็นตามการปรากฏในข้อความจนถึงปัจจุบัน | -2.0 - 2.0 |
| `frequency_penalty` | ลงโทษโทเค็นตามความถี่ในการปรากฏในข้อความจนถึงปัจจุบัน | -2.0 - 2.0 |
| `seed` | ค่าเมล็ดสุ่มเฉพาะเพื่อให้ผลลัพธ์ทำซ้ำได้ | ค่าจำนวนเต็ม |

## ตัวอย่างรูปแบบคำขอ

นี่คือตัวอย่างการร้องขอการสุ่มตัวอย่างจากไคลเอนต์ใน MCP:

```json
{
  "method": "sampling/createMessage",
  "params": {
    "messages": [
      {
        "role": "user",
        "content": {
          "type": "text",
          "text": "What files are in the current directory?"
        }
      }
    ],
    "systemPrompt": "You are a helpful file system assistant.",
    "includeContext": "thisServer",
    "maxTokens": 100,
    "temperature": 0.7
  }
}
```

## รูปแบบการตอบกลับ

ไคลเอนต์จะส่งผลลัพธ์การเติมข้อความกลับมา:

```json
{
  "model": "string",  // Name of the model used
  "stopReason": "endTurn" | "stopSequence" | "maxTokens" | "string",
  "role": "assistant",
  "content": {
    "type": "text",
    "text": "string"
  }
}
```

## การควบคุมโดยมนุษย์ในวงจร

การสุ่มตัวอย่างใน MCP ถูกออกแบบโดยคำนึงถึงการควบคุมของมนุษย์:

- **สำหรับพรอมต์**:
  - ไคลเอนต์ควรแสดงพรอมต์ที่เสนอให้ผู้ใช้ดู
  - ผู้ใช้ควรสามารถแก้ไขหรือปฏิเสธพรอมต์ได้
  - พรอมต์ระบบสามารถถูกกรองหรือแก้ไขได้
  - การรวมบริบทถูกควบคุมโดยไคลเอนต์

- **สำหรับผลลัพธ์การเติมข้อความ**:
  - ไคลเอนต์ควรแสดงผลลัพธ์ให้ผู้ใช้ดู
  - ผู้ใช้ควรสามารถแก้ไขหรือปฏิเสธผลลัพธ์ได้
  - ไคลเอนต์สามารถกรองหรือแก้ไขผลลัพธ์ได้
  - ผู้ใช้ควบคุมการเลือกโมเดลที่ใช้

ด้วยหลักการเหล่านี้ เรามาดูวิธีการใช้งานการสุ่มตัวอย่างในภาษาโปรแกรมต่างๆ โดยเน้นที่พารามิเตอร์ที่ผู้ให้บริการ LLM ส่วนใหญ่รองรับ

## ข้อควรพิจารณาด้านความปลอดภัย

เมื่อใช้งานการสุ่มตัวอย่างใน MCP ควรพิจารณาข้อปฏิบัติด้านความปลอดภัยดังนี้:

- **ตรวจสอบความถูกต้องของเนื้อหาข้อความทั้งหมด** ก่อนส่งไปยังไคลเอนต์
- **ล้างข้อมูลที่ละเอียดอ่อน** ออกจากพรอมต์และผลลัพธ์การเติมข้อความ
- **ตั้งค่าขีดจำกัดอัตราการใช้งาน** เพื่อป้องกันการใช้งานเกินขอบเขต
- **ตรวจสอบการใช้งานการสุ่มตัวอย่าง** เพื่อหาลักษณะผิดปกติ
- **เข้ารหัสข้อมูลระหว่างส่ง** ด้วยโปรโตคอลที่ปลอดภัย
- **จัดการความเป็นส่วนตัวของข้อมูลผู้ใช้** ตามกฎระเบียบที่เกี่ยวข้อง
- **ตรวจสอบคำขอการสุ่มตัวอย่าง** เพื่อความสอดคล้องและความปลอดภัย
- **ควบคุมค่าใช้จ่าย** ด้วยขีดจำกัดที่เหมาะสม
- **ตั้งค่าหมดเวลาสำหรับคำขอการสุ่มตัวอย่าง**
- **จัดการข้อผิดพลาดของโมเดลอย่างเหมาะสม** โดยมีแผนสำรอง

พารามิเตอร์การสุ่มตัวอย่างช่วยให้ปรับแต่งพฤติกรรมของโมเดลภาษาเพื่อให้ได้สมดุลระหว่างผลลัพธ์ที่กำหนดได้และความคิดสร้างสรรค์

มาดูวิธีตั้งค่าพารามิเตอร์เหล่านี้ในภาษาโปรแกรมต่างๆ กัน

# [.NET](../../../../05-AdvancedTopics/mcp-sampling)

```csharp
// .NET Example: Configuring sampling parameters in MCP
public class SamplingExample
{
    public async Task RunWithSamplingAsync()
    {
        // Create MCP client with sampling configuration
        var client = new McpClient("https://mcp-server-url.com");
        
        // Create request with specific sampling parameters
        var request = new McpRequest
        {
            Prompt = "Generate creative ideas for a mobile app",
            SamplingParameters = new SamplingParameters
            {
                Temperature = 0.8f,     // Higher temperature for more creative outputs
                TopP = 0.95f,           // Nucleus sampling parameter
                TopK = 40,              // Limit token selection to top K options
                FrequencyPenalty = 0.5f, // Reduce repetition
                PresencePenalty = 0.2f   // Encourage diversity
            },
            AllowedTools = new[] { "ideaGenerator", "marketAnalyzer" }
        };
        
        // Send request using specific sampling configuration
        var response = await client.SendRequestAsync(request);
        
        // Output results
        Console.WriteLine($"Generated with Temperature={request.SamplingParameters.Temperature}:");
        Console.WriteLine(response.GeneratedText);
    }
}
```

ในโค้ดข้างต้น เราได้:

- สร้างไคลเอนต์ MCP ด้วย URL เซิร์ฟเวอร์เฉพาะ
- ตั้งค่าคำขอด้วยพารามิเตอร์การสุ่มตัวอย่าง เช่น `temperature`, `top_p` และ `top_k`
- ส่งคำขอและพิมพ์ข้อความที่สร้างขึ้น
- ใช้:
    - `allowedTools` เพื่อระบุเครื่องมือที่โมเดลสามารถใช้ระหว่างการสร้าง ในกรณีนี้เราอนุญาตให้ใช้เครื่องมือ `ideaGenerator` และ `marketAnalyzer` เพื่อช่วยสร้างไอเดียแอปที่สร้างสรรค์
    - `frequencyPenalty` และ `presencePenalty` เพื่อควบคุมการซ้ำซ้อนและความหลากหลายในผลลัพธ์
    - `temperature` เพื่อควบคุมความสุ่มของผลลัพธ์ โดยค่าที่สูงกว่าจะทำให้ตอบสนองมีความคิดสร้างสรรค์มากขึ้น
    - `top_p` เพื่อจำกัดการเลือกโทเค็นให้อยู่ในกลุ่มที่มีความน่าจะเป็นสะสมสูงสุด ช่วยเพิ่มคุณภาพของข้อความที่สร้าง
    - `top_k` เพื่อจำกัดโมเดลให้เลือกโทเค็นที่มีความน่าจะเป็นสูงสุด K ตัว ซึ่งช่วยให้การตอบกลับมีความสอดคล้องมากขึ้น
    - `frequencyPenalty` และ `presencePenalty` เพื่อลดการซ้ำซ้อนและส่งเสริมความหลากหลายในข้อความที่สร้าง

# [JavaScript](../../../../05-AdvancedTopics/mcp-sampling)

```javascript
// JavaScript Example: Temperature and Top-P sampling configuration
const { McpClient } = require('@mcp/client');

async function demonstrateSampling() {
  // Initialize the MCP client
  const client = new McpClient({
    serverUrl: 'https://mcp-server-example.com',
    apiKey: process.env.MCP_API_KEY
  });
  
  // Configure request with different sampling parameters
  const creativeSampling = {
    temperature: 0.9,    // Higher temperature = more randomness/creativity
    topP: 0.92,          // Consider tokens with top 92% probability mass
    frequencyPenalty: 0.6, // Reduce repetition of token sequences
    presencePenalty: 0.4   // Penalize tokens that have appeared in the text so far
  };
  
  const factualSampling = {
    temperature: 0.2,    // Lower temperature = more deterministic/factual
    topP: 0.85,          // Slightly more focused token selection
    frequencyPenalty: 0.2, // Minimal repetition penalty
    presencePenalty: 0.1   // Minimal presence penalty
  };
  
  try {
    // Send two requests with different sampling configurations
    const creativeResponse = await client.sendPrompt(
      "Generate innovative ideas for sustainable urban transportation",
      {
        allowedTools: ['ideaGenerator', 'environmentalImpactTool'],
        ...creativeSampling
      }
    );
    
    const factualResponse = await client.sendPrompt(
      "Explain how electric vehicles impact carbon emissions",
      {
        allowedTools: ['factChecker', 'dataAnalysisTool'],
        ...factualSampling
      }
    );
    
    console.log('Creative Response (temperature=0.9):');
    console.log(creativeResponse.generatedText);
    
    console.log('\nFactual Response (temperature=0.2):');
    console.log(factualResponse.generatedText);
    
  } catch (error) {
    console.error('Error demonstrating sampling:', error);
  }
}

demonstrateSampling();
```

ในโค้ดข้างต้น เราได้:

- เริ่มต้นไคลเอนต์ MCP ด้วย URL เซิร์ฟเวอร์และคีย์ API
- ตั้งค่าพารามิเตอร์การสุ่มตัวอย่างสองชุด: หนึ่งสำหรับงานสร้างสรรค์ และอีกหนึ่งสำหรับงานที่ต้องการข้อเท็จจริง
- ส่งคำขอด้วยการตั้งค่าเหล่านี้ โดยอนุญาตให้โมเดลใช้เครื่องมือเฉพาะสำหรับแต่ละงาน
- พิมพ์ผลลัพธ์ที่สร้างขึ้นเพื่อแสดงผลของพารามิเตอร์การสุ่มตัวอย่างที่แตกต่างกัน
- ใช้ `allowedTools` เพื่อระบุเครื่องมือที่โมเดลสามารถใช้ระหว่างการสร้าง ในกรณีนี้เราอนุญาตให้ใช้ `ideaGenerator` และ `environmentalImpactTool` สำหรับงานสร้างสรรค์ และ `factChecker` กับ `dataAnalysisTool` สำหรับงานที่ต้องการข้อเท็จจริง
- ใช้ `temperature` เพื่อควบคุมความสุ่มของผลลัพธ์ โดยค่าที่สูงกว่าจะทำให้ตอบสนองมีความคิดสร้างสรรค์มากขึ้น
- ใช้ `top_p` เพื่อจำกัดการเลือกโทเค็นให้อยู่ในกลุ่มที่มีความน่าจะเป็นสะสมสูงสุด ช่วยเพิ่มคุณภาพของข้อความที่สร้าง
- ใช้ `frequencyPenalty` และ `presencePenalty` เพื่อลดการซ้ำซ้อนและส่งเสริมความหลากหลายในผลลัพธ์
- ใช้ `top_k` เพื่อจำกัดโมเดลให้เลือกโทเค็นที่มีความน่าจะเป็นสูงสุด K ตัว ซึ่งช่วยให้การตอบกลับมีความสอดคล้องมากขึ้น

---

## การสุ่มตัวอย่างแบบกำหนดผลลัพธ์ได้

สำหรับแอปพลิเคชันที่ต้องการผลลัพธ์ที่สม่ำเสมอ การสุ่มตัวอย่างแบบกำหนดผลลัพธ์ได้ช่วยให้ได้ผลลัพธ์ที่ทำซ้ำได้ วิธีการคือใช้ค่าเมล็ดสุ่มคงที่และตั้งค่า temperature เป็นศูนย์

มาดูตัวอย่างการใช้งานการสุ่มตัวอย่างแบบกำหนดผลลัพธ์ได้ในภาษาโปรแกรมต่างๆ

# [Java](../../../../05-AdvancedTopics/mcp-sampling)

```java
// Java Example: Deterministic responses with fixed seed
public class DeterministicSamplingExample {
    public void demonstrateDeterministicResponses() {
        McpClient client = new McpClient.Builder()
            .setServerUrl("https://mcp-server-example.com")
            .build();
            
        long fixedSeed = 12345; // Using a fixed seed for deterministic results
        
        // First request with fixed seed
        McpRequest request1 = new McpRequest.Builder()
            .setPrompt("Generate a random number between 1 and 100")
            .setSeed(fixedSeed)
            .setTemperature(0.0) // Zero temperature for maximum determinism
            .build();
            
        // Second request with the same seed
        McpRequest request2 = new McpRequest.Builder()
            .setPrompt("Generate a random number between 1 and 100")
            .setSeed(fixedSeed)
            .setTemperature(0.0)
            .build();
        
        // Execute both requests
        McpResponse response1 = client.sendRequest(request1);
        McpResponse response2 = client.sendRequest(request2);
        
        // Responses should be identical due to same seed and temperature=0
        System.out.println("Response 1: " + response1.getGeneratedText());
        System.out.println("Response 2: " + response2.getGeneratedText());
        System.out.println("Are responses identical: " + 
            response1.getGeneratedText().equals(response2.getGeneratedText()));
    }
}
```

ในโค้ดข้างต้น เราได้:

- สร้างไคลเอนต์ MCP ด้วย URL เซิร์ฟเวอร์ที่ระบุ
- ตั้งค่าคำขอสองคำขอโดยใช้พรอมต์เดียวกัน เมล็ดสุ่มคงที่ และ temperature เป็นศูนย์
- ส่งคำขอทั้งสองและพิมพ์ข้อความที่สร้างขึ้น
- แสดงให้เห็นว่าผลลัพธ์เหมือนกันเนื่องจากการตั้งค่าการสุ่มตัวอย่างแบบกำหนดผลลัพธ์ได้ (เมล็ดสุ่มและ temperature เดียวกัน)
- ใช้ `setSeed` เพื่อระบุเมล็ดสุ่มคงที่ ทำให้โมเดลสร้างผลลัพธ์เดียวกันสำหรับอินพุตเดียวกันทุกครั้ง
- ตั้งค่า `temperature` เป็นศูนย์เพื่อให้ได้ความแน่นอนสูงสุด หมายความว่าโมเดลจะเลือกโทเค็นถัดไปที่มีความน่าจะเป็นสูงสุดเสมอโดยไม่มีความสุ่ม

# [JavaScript](../../../../05-AdvancedTopics/mcp-sampling)

```javascript
// JavaScript Example: Deterministic responses with seed control
const { McpClient } = require('@mcp/client');

async function deterministicSampling() {
  const client = new McpClient({
    serverUrl: 'https://mcp-server-example.com'
  });
  
  const fixedSeed = 12345;
  const prompt = "Generate a random password with 8 characters";
  
  try {
    // First request with fixed seed
    const response1 = await client.sendPrompt(prompt, {
      seed: fixedSeed,
      temperature: 0.0  // Zero temperature for maximum determinism
    });
    
    // Second request with same seed and temperature
    const response2 = await client.sendPrompt(prompt, {
      seed: fixedSeed,
      temperature: 0.0
    });
    
    // Third request with different seed but same temperature
    const response3 = await client.sendPrompt(prompt, {
      seed: 67890,
      temperature: 0.0
    });
    
    console.log('Response 1:', response1.generatedText);
    console.log('Response 2:', response2.generatedText);
    console.log('Response 3:', response3.generatedText);
    console.log('Responses 1 and 2 match:', response1.generatedText === response2.generatedText);
    console.log('Responses 1 and 3 match:', response1.generatedText === response3.generatedText);
    
  } catch (error) {
    console.error('Error in deterministic sampling demo:', error);
  }
}

deterministicSampling();
```

ในโค้ดข้างต้น เราได้:

- เริ่มต้นไคลเอนต์ MCP ด้วย URL เซิร์ฟเวอร์
- ตั้งค่าคำขอสองคำขอโดยใช้พรอมต์เดียวกัน เมล็ดสุ่มคงที่ และ temperature เป็นศูนย์
- ส่งคำขอทั้งสองและพิมพ์ข้อความที่สร้างขึ้น
- แสดงให้เห็นว่าผลลัพธ์เหมือนกันเนื่องจากการตั้งค่าการสุ่มตัวอย่างแบบกำหนดผลลัพธ์ได้ (เมล็ดสุ่มและ temperature เดียวกัน)
- ใช้ `seed` เพื่อระบุเมล็ดสุ่มคงที่ ทำให้โมเดลสร้างผลลัพธ์เดียวกันสำหรับอินพุตเดียวกันทุกครั้ง
- ตั้งค่า `temperature` เป็นศูนย์เพื่อให้ได้ความแน่นอนสูงสุด หมายความว่าโมเดลจะเลือกโทเค็นถัดไปที่มีความน่าจะเป็นสูงสุดเสมอโดยไม่มีความสุ่ม
- ใช้เมล็ดสุ่มที่ต่างกันสำหรับคำขอที่สามเพื่อแสดงว่าการเปลี่ยนเมล็ดสุ่มจะทำให้ได้ผลลัพธ์ที่แตกต่าง แม้จะใช้พรอมต์และ temperature เดียวกัน

---

## การตั้งค่าการสุ่มตัวอย่างแบบไดนามิก

การสุ่มตัวอย่างอัจฉริยะจะปรับพารามิเตอร์ตามบริบทและความต้องการของแต่ละคำขอ ซึ่งหมายถึงการปรับพารามิเตอร์เช่น temperature, top_p และ penalties ตามประเภทงาน ความชอบของผู้ใช้ หรือประสิทธิภาพในอดีต

มาดูวิธีการใช้งานการสุ่มตัวอย่างแบบไดนามิกในภาษาโปรแกรมต่างๆ

# [Python](../../../../05-AdvancedTopics/mcp-sampling)

```python
# Python Example: Dynamic sampling based on request context
class DynamicSamplingService:
    def __init__(self, mcp_client):
        self.client = mcp_client
        
    async def generate_with_adaptive_sampling(self, prompt, task_type, user_preferences=None):
        """Uses different sampling strategies based on task type and user preferences"""
        
        # Define sampling presets for different task types
        sampling_presets = {
            "creative": {"temperature": 0.9, "top_p": 0.95, "frequency_penalty": 0.7},
            "factual": {"temperature": 0.2, "top_p": 0.85, "frequency_penalty": 0.2},
            "code": {"temperature": 0.3, "top_p": 0.9, "frequency_penalty": 0.5},
            "analytical": {"temperature": 0.4, "top_p": 0.92, "frequency_penalty": 0.3}
        }
        
        # Select base preset
        sampling_params = sampling_presets.get(task_type, sampling_presets["factual"])
        
        # Adjust based on user preferences if provided
        if user_preferences:
            if "creativity_level" in user_preferences:
                # Scale temperature based on creativity preference (1-10)
                creativity = min(max(user_preferences["creativity_level"], 1), 10) / 10
                sampling_params["temperature"] = 0.1 + (0.9 * creativity)
            
            if "diversity" in user_preferences:
                # Adjust top_p based on desired response diversity
                diversity = min(max(user_preferences["diversity"], 1), 10) / 10
                sampling_params["top_p"] = 0.6 + (0.39 * diversity)
        
        # Create and send request with custom sampling parameters
        response = await self.client.send_request(
            prompt=prompt,
            temperature=sampling_params["temperature"],
            top_p=sampling_params["top_p"],
            frequency_penalty=sampling_params["frequency_penalty"]
        )
        
        # Return response with sampling metadata for transparency
        return {
            "text": response.generated_text,
            "applied_sampling": sampling_params,
            "task_type": task_type
        }
```

ในโค้ดข้างต้น เราได้:

- สร้างคลาส `DynamicSamplingService` ที่จัดการการสุ่มตัวอย่างแบบปรับตัว
- กำหนดค่าพรีเซ็ตการสุ่มตัวอย่างสำหรับประเภทงานต่างๆ (สร้างสรรค์, ข้อเท็จจริง, โค้ด, วิเคราะห์)
- เลือกพรีเซ็ตการสุ่มตัวอย่างพื้นฐานตามประเภทงาน
- ปรับพารามิเตอร์การสุ่มตัวอย่างตามความชอบของผู้ใช้ เช่น ระดับความคิดสร้างสรรค์และความหลากหลาย
- ส่งคำขอพร้อมพารามิเตอร์การสุ่มตัวอย่างที่ตั้งค่าแบบไดนามิก
- ส่งคืนข้อความที่สร้างขึ้นพร้อมกับพารามิเตอร์การสุ่มตัวอย่างและประเภทงานเพื่อความโปร่งใส
- ใช้ `temperature` เพื่อควบคุมความสุ่มของผลลัพธ์ โดยค่าที่สูงกว่าจะทำให้ตอบสนองมีความคิดสร้างสรรค์มากขึ้น
- ใช้ `top_p` เพื่อจำกัดการเลือกโทเค็นให้อยู่ในกลุ่มที่มีความน่าจะเป็นสะสมสูงสุด ช่วยเพิ่มคุณภาพของข้อความที่สร้าง
- ใช้ `frequency_penalty` เพื่อลดการซ้ำซ้อนและส่งเสริมความหลากหลายในผลลัพธ์
- ใช้ `user_preferences` เพื่อให้ผู้ใช้ปรับแต่งพารามิเตอร์การสุ่มตัวอย่างตามระดับความคิดสร้างสรรค์และความหลากหลายที่กำหนดเอง
- ใช้ `task_type` เพื่อกำหนดกลยุทธ์การสุ่มตัวอย่างที่เหมาะสมสำหรับคำขอ ทำให้ตอบสนองได้เหมาะสมกับลักษณะงาน
- ใช้เมธอด `send_request` เพื่อส่งพรอมต์พร้อมพารามิเตอร์การสุ่มตัวอย่างที่ตั้งค่าไว้ เพื่อให้โมเดลสร้างข้อความตามข้อกำหนด
- ใช้ `generated_text` เพื่อดึงคำตอบจากโมเดล ซึ่งจะถูกส่งคืนพร้อมกับพารามิเตอร์การสุ่มตัวอย่างและประเภทงานเพื่อการวิเคราะห์หรือแสดงผลต่อไป
- ใช้ฟังก์ชัน `min` และ `max` เพื่อให้แน่ใจว่าความชอบของผู้ใช้ถูกจำกัดให้อยู่ในช่วงที่ถูกต้อง ป้องกันการตั้งค่าการสุ่มตัวอย่างที่ไม่ถูกต้อง

# [JavaScript Dynamic](../../../../05-AdvancedTopics/mcp-sampling)

```javascript
// JavaScript Example: Dynamic sampling configuration based on user context
class AdaptiveSamplingManager {
  constructor(mcpClient) {
    this.client = mcpClient;
    
    // Define base sampling profiles
    this.samplingProfiles = {
      creative: { temperature: 0.85, topP: 0.94, frequencyPenalty: 0.7, presencePenalty: 0.5 },
      factual: { temperature: 0.2, topP: 0.85, frequencyPenalty: 0.3, presencePenalty: 0.1 },
      code: { temperature: 0.25, topP: 0.9, frequencyPenalty: 0.4, presencePenalty: 0.3 },
      conversational: { temperature: 0.7, topP: 0.9, frequencyPenalty: 0.6, presencePenalty: 0.4 }
    };
    
    // Track historical performance
    this.performanceHistory = [];
  }
  
  // Detect task type from prompt
  detectTaskType(prompt, context = {}) {
    const promptLower = prompt.toLowerCase();
    
    // Simple heuristic detection - could be enhanced with ML classification
    if (context.taskType) return context.taskType;
    
    if (promptLower.includes('code') || 
        promptLower.includes('function') || 
        promptLower.includes('program')) {
      return 'code';
    }
    
    if (promptLower.includes('explain') || 
        promptLower.includes('what is') || 
        promptLower.includes('how does')) {
      return 'factual';
    }
    
    if (promptLower.includes('creative') || 
        promptLower.includes('imagine') || 
        promptLower.includes('story')) {
      return 'creative';
    }
    
    // Default to conversational if no clear type is detected
    return 'conversational';
  }
  
  // Calculate sampling parameters based on context and user preferences
  getSamplingParameters(prompt, context = {}) {
    // Detect the type of task
    const taskType = this.detectTaskType(prompt, context);
    
    // Get base profile
    let params = {...this.samplingProfiles[taskType]};
    
    // Adjust based on user preferences
    if (context.userPreferences) {
      const { creativity, precision, consistency } = context.userPreferences;
      
      if (creativity !== undefined) {
        // Scale from 1-10 to appropriate temperature range
        params.temperature = 0.1 + (creativity * 0.09); // 0.1-1.0
      }
      
      if (precision !== undefined) {
        // Higher precision means lower topP (more focused selection)
        params.topP = 1.0 - (precision * 0.05); // 0.5-1.0
      }
      
      if (consistency !== undefined) {
        // Higher consistency means lower penalties
        params.frequencyPenalty = 0.1 + ((10 - consistency) * 0.08); // 0.1-0.9
      }
    }
    
    // Apply learned adjustments from performance history
    this.applyLearnedAdjustments(params, taskType);
    
    return params;
  }
  
  applyLearnedAdjustments(params, taskType) {
    // Simple adaptive logic - could be enhanced with more sophisticated algorithms
    const relevantHistory = this.performanceHistory
      .filter(entry => entry.taskType === taskType)
      .slice(-5); // Only consider recent history
    
    if (relevantHistory.length > 0) {
      // Calculate average performance scores
      const avgScore = relevantHistory.reduce((sum, entry) => sum + entry.score, 0) / relevantHistory.length;
      
      // If performance is below threshold, adjust parameters
      if (avgScore < 0.7) {
        // Slight adjustment toward safer values
        params.temperature = Math.max(params.temperature * 0.9, 0.1);
        params.topP = Math.max(params.topP * 0.95, 0.5);
      }
    }
  }
  
  recordPerformance(prompt, samplingParams, response, score) {
    // Record performance for future adjustments
    this.performanceHistory.push({
      timestamp: Date.now(),
      taskType: this.detectTaskType(prompt),
      samplingParams,
      responseLength: response.generatedText.length,
      score // 0-1 rating of response quality
    });
    
    // Limit history size
    if (this.performanceHistory.length > 100) {
      this.performanceHistory.shift();
    }
  }
  
  async generateResponse(prompt, context = {}) {
    // Get optimized sampling parameters
    const samplingParams = this.getSamplingParameters(prompt, context);
    
    // Send request with optimized parameters
    const response = await this.client.sendPrompt(prompt, {
      ...samplingParams,
      allowedTools: context.allowedTools || []
    });
    
    // If user provides feedback, record it for future optimization
    if (context.recordPerformance) {
      this.recordPerformance(prompt, samplingParams, response, context.feedbackScore || 0.5);
    }
    
    return {
      response,
      appliedSamplingParams: samplingParams,
      detectedTaskType: this.detectTaskType(prompt, context)
    };
  }
}

// Example usage
async function demonstrateAdaptiveSampling() {
  const client = new McpClient({
    serverUrl: 'https://mcp-server-example.com'
  });
  
  const samplingManager = new AdaptiveSamplingManager(client);
  
  try {
    // Creative task with custom user preferences
    const creativeResult = await samplingManager.generateResponse(
      "Write a short poem about artificial intelligence",
      {
        userPreferences: {
          creativity: 9,  // High creativity (1-10)
          consistency: 3  // Low consistency (1-10)
        }
      }
    );
    
    console.log('Creative Task:');
    console.log(`Detected type: ${creativeResult.detectedTaskType}`);
    console.log('Applied sampling:', creativeResult.appliedSamplingParams);
    console.log(creativeResult.response.generatedText);
    
    // Code generation task
    const codeResult = await samplingManager.generateResponse(
      "Write a JavaScript function to calculate the Fibonacci sequence",
      {
        userPreferences: {
          creativity: 2,  // Low creativity
          precision: 8,   // High precision
          consistency: 9  // High consistency
        }
      }
    );
    
    console.log('\nCode Task:');
    console.log(`Detected type: ${codeResult.detectedTaskType}`);
    console.log('Applied sampling:', codeResult.appliedSamplingParams);
    console.log(codeResult.response.generatedText);
    
  } catch (error) {
    console.error('Error in adaptive sampling demo:', error);
  }
}

demonstrateAdaptiveSampling();
```

ในโค้ดข้างต้น เราได้:

- สร้างคลาส `AdaptiveSamplingManager` ที่จัดการการสุ่มตัวอย่างแบบไดนามิกตามประเภทงานและความชอบของผู้ใช้
- กำหนดโปรไฟล์การสุ่มตัวอย่างสำหรับประเภทงานต่างๆ (สร้างสรรค์, ข้อเท็จจริง, โค้ด, การสนทนา)
- นำเมธอดมาช่วยตรวจจับประเภทงานจากพรอมต์โดยใช้เฮียวริสติกง่ายๆ
- คำนวณพารามิเตอร์การสุ่มตัวอย่างตามประเภทงานที่ตรวจจับได้และความชอบของผู้ใช้
- ปรับพารามิเตอร์ตามประสิทธิภาพในอดีตเพื่อเพิ่มประสิทธิภาพการสุ่มตัวอย่าง
- บันทึกประสิทธิภาพเพื่อใช้ปรับปรุงในอนาคต ทำให้ระบบเรียนรู้จากการโต้ตอบที่ผ่านมา
- ส่งคำขอด้วยพารามิเตอร์การสุ่มตัวอย่างที่ตั้งค่าแบบไดนามิก และส่งคืนข้อความที่สร้างขึ้นพร้อมพารามิเตอร์ที่ใช้และประเภทงานที่ตรวจจับได้
- ใช้:
    - `userPreferences` เพื่อให้ผู้ใช้ปรับแต่งพารามิเตอร์การสุ่มตัวอย่างตามระดับความคิดสร้างสรรค์ ความแม่นยำ และความสม่ำเสมอที่กำหนดเอง
    - `detectTaskType` เพื่อกำหนดลักษณะของงานจากพรอมต์ ทำให้ตอบสนองได้เหมาะสมกับ

**ข้อจำกัดความรับผิดชอบ**:  
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษาอัตโนมัติ [Co-op Translator](https://github.com/Azure/co-op-translator) แม้เราจะพยายามให้ความถูกต้องสูงสุด แต่โปรดทราบว่าการแปลอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาต้นทางถือเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ ขอแนะนำให้ใช้บริการแปลโดยผู้เชี่ยวชาญมนุษย์ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความผิดใด ๆ ที่เกิดจากการใช้การแปลนี้