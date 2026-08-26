# កម្មវិធីអត្រាកំណត់អត្រា LLM Client

កម្មវិធី Java មួយ ដែលបង្ហាញពីរបៀបប្រើ LangChain4j ដើម្បីភ្ជាប់ទៅសេវាកម្មកាល់គយ៊ីយ៉ង់ MCP (Model Context Protocol) តាមរយៈ API MiniMax ដែលផ្គត់ផ្គង់តាម OpenAI.

## លក្ខខណ្ឌមុនចាប់ផ្តើម

- Java 21 ឬខ្ពស់ជាងនេះ
- Maven 3.6+ (ឬប្រើ Maven wrapper ដែលភ្ជាប់មកជាមួយ)
- Key MiniMax API មួយ
- សេវាកម្មកាល់គយ៊ីយ៉ង់ MCP ដំណើរការលើ `http://localhost:8080`

## របៀបទទួលបាន Key API

កម្មវិធីនេះប្រើ API MiniMax ដែលផ្គត់ផ្គង់តាម OpenAI។ បើកវិធីដូចខាងក្រោមដើម្បីទទួល key និង endpoint របស់អ្នក:

### 1. ជ្រើសរើស endpoint
1. ប្រើ `https://api.minimax.io/v1` សម្រាប់ endpoint បូកសកល
2. ប្រើ `https://api.minimaxi.com/v1` សម្រាប់ endpoint ប្រទេសចិន

### 2. បង្កើត Key API
1. បង្កើត MiniMax API key ពីគណនី MiniMax របស់អ្នក
2. ទុក key ទុកនៅកន្លែងដែលមានសុវត្ថិភាព

### 3. កំណត់បរិស្ថានអថេរ

#### នៅលើ Windows (Command Prompt):
```cmd
set OPENAI_API_KEY=your_minimax_api_key_here
set OPENAI_BASE_URL=https://api.minimax.io/v1
set MINIMAX_MODEL_ID=MiniMax-M3
```

#### នៅលើ Windows (PowerShell):
```powershell
$env:OPENAI_API_KEY="your_minimax_api_key_here"
$env:OPENAI_BASE_URL="https://api.minimax.io/v1"
$env:MINIMAX_MODEL_ID="MiniMax-M3"
```

#### នៅលើ macOS/Linux:
```bash
export OPENAI_API_KEY=your_minimax_api_key_here
export OPENAI_BASE_URL=https://api.minimax.io/v1
export MINIMAX_MODEL_ID=MiniMax-M3
```

## ការតំឡើងនិងដំឡើង

1. **លីសឬចូលទៅក្នុងថតគម្រោង**

2. **ដំឡើងអង្គធាតុដែលចាំបាច់**៖
   ```cmd
   mvnw clean install
   ```
   ឬប្រសិនបើអ្នកមាន Maven ដំឡើងជាសកល:
   ```cmd
   mvn clean install
   ```

3. **កំណត់អថេរបរិស្ថាន** (មើលផ្នែក "ទទួល Key API" ខាងលើ)

4. **ចាប់ផ្តើមសេវាកម្ម MCP Calculator**:
   ប្រាកដថាអ្នកមានសេវាកម្មកាល់គយ៊ីយ៉ង់ MCP ភាគ 1 ដំណើរការលើ `http://localhost:8080/sse` ។ វាត្រូវបានដំណើរការមុនពេលអ្នកចាប់ផ្តើមកម្មវិធីអត្រាកំណត់ខាងក្រោម។

## ការប្រតិបត្តិកម្មកម្មវិធី

```cmd
mvnw clean package
java -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## អ្វីដែលកម្មវិធីធ្វើ

កម្មវិធីបង្ហាញនូវការប្រាស្រ័យទំនាក់ទំនងចម្បងបីគឺជាមួយសេវាកម្មកាល់គយ៊ីយ៉ង់៖

1. **ការដាក់បូក**៖ គណនាចំនួនបូករបស់ 24.5 និង 17.3
2. **គណនាឪ្យមូលដ្ឋាន**៖ គណនាឪ្យមូលដ្ឋាននៃ 144
3. **ជំនួយ**៖ បង្ហាញមុខងារកាល់គយ៊ីយ៉ង់ដែលមាន

## លទ្ធផលដែលរំពឹងទុក

នៅពេលដំណើរការ​បានជោគជ័យ អ្នកគួរតែឃើញលទ្ធផលដូចជា៖

```
The sum of 24.5 and 17.3 is 41.8.
The square root of 144 is 12.
The calculator service provides the following functions: add, subtract, multiply, divide, sqrt, power...
```

## ការដោះស្រាយបញ្ហា

### បញ្ហាធម្មតា

1. **"សូមកំណត់អថេរបរិស្ថាន OPENAI_API_KEY មិនទាន់បានកំណត់ឡើយ"**
   - ប្រាកដថាអ្នកបានកំណត់អថេរបរិស្ថាន `OPENAI_API_KEY`
   - ចាប់ផ្តើមថ្មី terminal/command prompt បន្ទាប់ពីកំណត់អថេរនេះ

2. **"ការតភ្ជាប់ត្រូវបានបដិសេធទៅ localhost:8080"**
   - ធ្វើការត្រួតពិនិត្យថាសេវាកម្ម MCP calculator កំពុងដំណើរការលើច្រក 8080
   - ពិនិត្យថាមានសេវាផ្សេងទៀតដែលកំពុងប្រើច្រក 8080 មែនឬទេទេ

3. **"ការផ្ទៀងផ្ទាត់បរាជ័យ"**
   - ផ្ទៀងផ្ទាត់ key API របស់អ្នកមានសុពលភាព
   - ពិនិត្យមើលថា `OPENAI_BASE_URL` ត្រូវគ្នាជាមួយ endpoint ដែលអ្នកចង់ប្រើ

4. **កំហុស Maven build**
   - ធ្វើការផ្ទៀងផ្ទាត់ថាអ្នកកំពុងប្រើ Java 21 ឬខ្ពស់ជាងនេះ៖ `java -version`
   - សាកល្បងសំអាត build៖ `mvnw clean`

### ការត្រួតពិនិត្យបញ្ហា (Debugging)

ដើម្បីបើក log debugging ចូលបន្ថែម argument JVM ខាងក្រោមពេលរត់:
```cmd
java -Dlogging.level.dev.langchain4j=DEBUG -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## ការកំណត់រចនា

កម្មវិធីត្រូវបានកំណត់ដូច​ខាងក្រោម៖
- ប្រើការ MiniMax-M3 ជាដើមទូទៅ ឬ MiniMax-M2.7 នៅពេលកំណត់ `MINIMAX_MODEL_ID`
- ភ្ជាប់ទៅ `OPENAI_BASE_URL` នៅពេលវាត្រូវបានកំណត់; មិនដូច្នោះទេប្រើ `https://api.minimaxi.com/v1` នៅពេល `MINIMAX_REGION=cn_zh` ឬ `https://api.minimax.io/v1` ជាមុនគេល
- ភ្ជាប់ទៅសេវាកម្ម MCP នៅ `http://localhost:8080/sse`
- ប្រើពេលផុតកំណត់ 60 វិនាទីសម្រាប់ការស្នើសុំ

## អង្គធាតុទាមទារ

អង្គធាតុសំខាន់ដែលបានប្រើក្នុងគម្រោងនេះ៖
- **LangChain4j**៖ សម្រាប់ការភ្ជាប់ AI និងការគ្រប់គ្រងឧបករណ៍
- **LangChain4j MCP**៖ សម្រាប់ការគាំទ្រពិធីការបរិបទម៉ូឌែល
- **LangChain4j OpenAI official**៖ សម្រាប់ការភ្ជាប់ API MiniMax OpenAI-compatible
- **Spring Boot**៖ សម្រាប់សមាសធាតុកម្មវិធី និងការវាយបញ្ចូលអង្គធាតុ

## រក្សាសិទ្ធិ

គម្រោងនេះគឺបានរក្សាសិទ្ធិក្រោមអាជ្ញាបណ្ណ Apache License 2.0 - មើលឯកសារ [LICENSE](../../../../../../03-GettingStarted/03-llm-client/solution/java/LICENSE) សម្រាប់ព័ត៌មានលម្អិត។

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ការបដិសេធ**:
ឯកសារនេះត្រូវបានបម្លែងភាសា ដោយប្រើសេវាបម្លែងភាសា AI [Co-op Translator](https://github.com/Azure/co-op-translator)។ ទោះយើងខ្ញុំមានក្តីប្រាថ្នាឱ្យបានច្បាស់លាស់ តែសូមយល់ដឹងថាការបម្លែងដោយស្វ័យប្រវត្តិក៏អាចមានកំហុសឬភាពមិនត្រឹមត្រូវ។ ឯកសារដើមជាភាសាទីតាំងគួរត្រូវបានគេប្រើជាប្រភពច្បាស់លាស់។ សម្រាប់ព័ត៌មានសំខាន់ៗ សូមណែនាំឱ្យប្រើប្រាស់ការប្រែដោយមនុស្សជំនាញ។ យើងខ្ញុំមិនទទួលខុសត្រូវចំពោះការយល់ច្រឡំ ឬការបកស្រាយខុសបន្ទាប់ពីការប្រើប្រាស់ការបម្លែងនេះនោះទេ។
<!-- CO-OP TRANSLATOR DISCLAIMER END -->