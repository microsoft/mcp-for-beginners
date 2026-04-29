# កម្មវិធីអតិថិជន Calculator LLM

កម្មវិធី Java មួយដែលបង្ហាញពីរបៀបប្រើប្រាស់ LangChain4j ដើម្បីភ្ជាប់ទៅកាន់សេវាកម្មគណនាគ្រាប់ MCP (Model Context Protocol) ជាមួយការបញ្ចូល GitHub Models។

## តម្រូវការមុន

- Java 21 ឬច្រើនជាងនេះ
- Maven 3.6+ (ឬប្រើ Maven wrapper ដែលបានបញ្ចូល)
- គណនី GitHub ដែលមានសិទ្ធិចូលប្រើ GitHub Models
- សេវា MCP calculator កំពុងដំណើរការនៅ `http://localhost:8080`

## របៀបទទួលបាន Token GitHub

កម្មវិធីនេះប្រើ GitHub Models ដែលត្រូវការប្រើ Token អ្នកប្រើប្រាស់ផ្ទាល់ GitHub។ សូមអនុវត្តជំហានខាងក្រោមដើម្បីទទួលបាន token របស់អ្នក៖

### 1. ចូលទៅ GitHub Models
1. ចូលទៅ [GitHub Models](https://github.com/marketplace/models)
2. ចុះឈ្មោះជាមួយគណនី GitHub របស់អ្នក
3. ស្នើសុំចូលប្រើ GitHub Models ប្រសិនបើអ្នកមិនបានធ្វើរួច

### 2. បង្កើត Personal Access Token
1. ចូលទៅ [GitHub Settings → Developer settings → Personal access tokens → Tokens (classic)](https://github.com/settings/tokens)
2. ចុច "Generate new token" → "Generate new token (classic)"
3. ផ្ដល់ឈ្មោះនូវ token នេះ (ឧ. "MCP Calculator Client")
4. កំណត់ថ្ងៃផុតកំណត់បើចង់
5. ជ្រើសរើស scopes ខាងក្រោម៖
   - `repo` (ប្រសិនបើចូលទៅ repositories ព្រៃវេ)
   - `user:email`
6. ចុច "Generate token"
7. **សំខាន់**: ចម្លង token តាមភ្លាមៗ - អ្នកមិនអាចមើលវា​បានម្ដងទៀតទេ!

### 3. កំណត់អថេរបរិស្ថាន

#### នៅលើ Windows (Command Prompt):
```cmd
set GITHUB_TOKEN=your_github_token_here
```

#### នៅលើ Windows (PowerShell):
```powershell
$env:GITHUB_TOKEN="your_github_token_here"
```

#### នៅលើ macOS/Linux:
```bash
export GITHUB_TOKEN=your_github_token_here
```

## ការតំឡើង និងផ្ទុកកម្មវិធី

1. **ចម្លងឬទៅកាន់ថតគម្រោង**

2. **ដំឡើងការពឹងផ្អែក**:
   ```cmd
   mvnw clean install
   ```
   ឬប្រសិនបើអ្នកមាន Maven តំឡើងនៅជាតិសកល:
   ```cmd
   mvn clean install
   ```

3. **កំណត់អថេរបរិស្ថាន** (មើលផ្នែក "របៀបទទួលបាន Token GitHub" ខាងលើ)

4. **ចាប់ផ្តើមសេវា MCP Calculator**:
   សូមធានាថា អ្នកបានចាប់ផ្តើមសេវា MCP calculator ក្នុងជំពូកទី១ នៅ `http://localhost:8080/sse` រួចហើយ មុនពេលចាប់ផ្តើមអតិថិជននេះ។

## របៀបដំណើរការ​កម្មវិធី

```cmd
mvnw clean package
java -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## កម្មវិធីធ្វើអ្វីខ្លះ

កម្មវិធីបង្ហាញអំពីបីប្រតិកម្មសំខាន់ជាមួយសេវាកម្មគណនាគ្រាប់នេះ៖

1. **បូកគ្នា**៖ គណនាប្រាក់សរុបរបស់ 24.5 និង 17.3
2. **គ្រឹះជាប្រភាគដើម**៖ គណនាគ្រឹះជាប្រភាគដើមនៃ 144
3. **ជំនួយ**៖ បង្ហាញមុខងារគណនាគ្រាប់ដែលមាន

## លទ្ធផលដែលរំពឹងទុក

នៅពេលដំណើរការជោគជ័យ អ្នកគួរតែឃើញលទ្ធផលដូចខាងក្រោម៖

```
The sum of 24.5 and 17.3 is 41.8.
The square root of 144 is 12.
The calculator service provides the following functions: add, subtract, multiply, divide, sqrt, power...
```

## ការត្រួតពិនិត្យបញ្ហា

### បញ្ហាទូទៅ

1. **"អថេរបរិស្ថាន GITHUB_TOKEN មិនបានកំណត់"**
   - សូមប្រាកដថាអ្នកបានកំណត់អថេរបរិស្ថាន `GITHUB_TOKEN` រួចហើយ
   - ចាប់ផ្តើមផ្ទេរកម្មវិធី/Command Prompt ម្តងទៀតបន្ទាប់ពីកំណត់អថេរ

2. **"ការតភ្ជាប់បដិសេធទៅ localhost:8080"**
   - សូមធានាថា សេវា MCP calculator កំពុងដំណើរការនៅឆ្នោត 8080
   - ពិនិត្យមើលថា មានសេវាផ្សេងមួយកំពុងប្រើឆ្នោត 8080 ទេឬដែរ

3. **"ការផ្ទៀងផ្ទាត់បរាជ័យ"**
   - ផ្ទៀងផ្ទាត់ថា token GitHub របស់អ្នកត្រឹមត្រូវ និងមានសិទ្ធិគ្រប់គ្រាន់
   - ពិនិត្យថាអ្នកអាចចូលទៅ GitHub Models

4. **កំហុសបង្កើត Maven**
   - សូមប្រាកដថាអ្នកកំពុងប្រើ Java 21 ឬខ្ពស់ជាងនេះ៖ `java -version`
   - សាកល្បងសម្អាតការបង្កើត៖ `mvnw clean`

### ការរកកំហុស

ដើម្បីបើក logging សម្រាប់សម្អាតកំហុស សូមបញ្ចូល argument JVM ខាងក្រោមពេលដំណើរការ៖
```cmd
java -Dlogging.level.dev.langchain4j=DEBUG -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## ការកំណត់រចនាសម្ព័ន្ធ

កម្មវិធីនេះកំណត់ដូចជា៖
- ប្រើ GitHub Models ជាមួយម៉ូដែល `gpt-4.1-nano`
- ភ្ជាប់ទៅសេវា MCP នៅ `http://localhost:8080/sse`
- ប្រើពេលវេលាចំណាយស្នើសុំ 60 វិនាទី
- បើកការចុះបញ្ជីសំណើ/ការឆ្លើយតបសម្រាប់ការសម្អាតកំហុស

## ការពឹងផ្អែក

ការពឹងផ្អែកសំខាន់ៗប្រើក្នុងគម្រោងនេះ៖
- **LangChain4j**: សម្រាប់ការបញ្ចូល AI និងការគ្រប់គ្រងឧបករណ៍
- **LangChain4j MCP**: សម្រាប់គាំទ្រ Model Context Protocol
- **LangChain4j GitHub Models**: សម្រាប់ការបញ្ចូល GitHub Models
- **Spring Boot**: សម្រាប់ស៊ុមកម្មវិធី និងការចាក់សោរ Dependency

## អាជ្ញាបណ្ណ

គម្រោងនេះមានអាជ្ញាបណ្ណក្រោម Apache License 2.0 - សូមមើលឯកសារ [LICENSE](../../../../../../03-GettingStarted/03-llm-client/solution/java/LICENSE) សម្រាប់ព័ត៌មានលម្អិត។

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ការព្រមាន**៖  
ឯកសារនេះគឺបានបកប្រែដោយប្រើសេវាកម្មបកប្រែ AI [Co-op Translator](https://github.com/Azure/co-op-translator)។ ទោះបីយើងខិតខំអោយបានត្រឹមត្រូវ ក៏សូមយកចិត្តទុកដាក់ទៅលើព្រោះការបកប្រែដោយស្វ័យប្រវត្តិអាចមានកំហុស ឬការខុសឆ្គងណាមួយ។ ឯកសារដើមក្នុងភាសាម្តដើមគួរត្រូវបានទទួលស្គាល់ថាជា ប្រភពដែលមានអំណាចបំផុត។ សម្រាប់ព័ត៌មានសំខាន់ៗ នេះគួរត្រូវបានបកប្រែដោយអ្នកជំនាញមនុស្សជាជម្រើសល្អជាងគេ។ យើងមិនទទួលខុសត្រូវចំពោះការយល់ខុស ឬការបកប្រែមិនបានត្រឹមត្រូវឡើយដែលកើតឡើងពីការប្រើប្រាស់ការបកប្រែនេះ។
<!-- CO-OP TRANSLATOR DISCLAIMER END -->