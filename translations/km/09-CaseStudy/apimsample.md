# Case Study: បង្ហាញ REST API នៅក្នុងការគ្រប់គ្រង API ជា​ MCP server

Azure API Management គឺជាសេវាកម្មដែលផ្ដល់នូវ Gateway នៅលើ Endpoints API របស់អ្នក។ វាដំណើរការដូចជា Azure API Management លេងតួនាទីជា proxy នៅ μπ្តុខ API របស់អ្នក និងអាចសម្រេចចិត្តអ្វីដែលត្រូវធ្វើជាមួយសំណើដែលមកដល់។

ដោយការប្រើវា អ្នកអាចបន្ថែមលក្ខណៈពិសេសជាច្រើនដូចជា៖

- **សន្តិសុខ** អ្នកអាចប្រើគ្រប់យ៉ាងពី API keys, JWT រហូតដល់ managed identity។
- **ការកំណត់អត្រា**​ លក្ខណៈមួយដ៏អស្ចារ្យគឺការអាចសម្រេចចិត្តថាម៉ោងប៉ុន្មានដែលអាចទទួលសំណើក្នុងចន្លោះពេលកំណត់មួយ។ នេះជួយធានាថា អ្នកប្រើប្រាស់ទាំងអស់មានបទពិសោធន៍ល្អ និងក៏ធានាថាសេវាកម្មរបស់អ្នកមិនត្រូវបានផ្ទុកច្រើនពេក។
- **ការវាស់វែងនិងបែងចែកដាក់បន្ទុក** អ្នកអាចដាក់ស្ថានដែលមួយចំនួនសម្រាប់ការបែងចែកបន្ទុក ហើយអាចសម្រេចចិត្តក៍បែប "load balance" ។
- **មុខងារ AI ដូចជា semantic caching**, កំណត់កម្រិត token និងការត្រួតពិនិត្យ token និងផ្សេងៗទៀត។ សំរាប់មុខងារទាំងនេះមានអត្ថប្រយោជន៍ក្នុងការកែលម្អការឆ្លើយតបរហ័ស និងជួយអ្នកតាមដានការចំណាយ token របស់អ្នក។ [អានបន្ថែមនៅទីនេះ](https://learn.microsoft.com/en-us/azure/api-management/genai-gateway-capabilities)។

## ហេតុអ្វី MCP + Azure API Management?

Model Context Protocol កំពុងក្លាយជាស្តង់ដារយ៉ាងឆាប់រហ័សសម្រាប់កម្មវិធី AI agentic និងរបៀបបង្ហាញឧបករណ៍ និងទិន្នន័យបែបមានស៊ុមស្រាប់។ Azure API Management គឺជាជម្រើសធម្មជាតិនៅពេលអ្នកត្រូវការក្នុងការគ្រប់គ្រង APIs។ MCP Servers ភាគច្រើនរួមបញ្ចូលជាមួយ API ផ្សេងទៀត ដើម្បីដោះស្រាយសំណើទៅឧបករណ៍មួយឧទាហរណ៍។ ដូច្នេះ ការភ្ជាប់ Azure API Management និង MCP គឺមានហេតុការណ៍មិនគួរបដិសេធ។

## ទិដ្ឋភាពទូទៅ

ក្នុងករណីប្រើប្រាស់ជាក់លាក់នេះ យើងសិក្សាពីរបៀបបង្ហាញ endpoint API ជាធាតុ MCP Server។ ដោយធ្វើបែបនេះ យើងអាចធ្វើឲ្យ endpoints ទាំងនេះជាផ្នែកមួយនៃកម្មវិធី agentic ហើយក៏អាចប្រើប្រាស់លក្ខណៈពិសេសពី Azure API Management បានផងដែរ។

## លក្ខណៈសំខាន់ៗ

- អ្នកជ្រើសរើសវិធីសាស្ត្រនៃ endpoint ដែលចង់បង្ហាញជាឧបករណ៍។
- លក្ខណៈបន្ថែមដែលអ្នកទទួលបានអាស្រ័យលើការកំណត់របស់អ្នកនៅផ្នែកគោលនយោបាយសម្រាប់ API របស់អ្នក។ តែទីនេះ យើងនឹងបង្ហាញរបៀបបន្ថែមការកំណត់អត្រា។

## ជំហានមុន៖ នាំចូល API

បើអ្នកមាន API នៅក្នុង Azure API Management រួចហើយ មិនបាច់ធ្វើជំហាននេះទេ។ បើមិនមាន សូមពិនិត្យតំណភ្ជាប់នេះ [នាំចូល API ទៅ Azure API Management](https://learn.microsoft.com/en-us/azure/api-management/import-and-publish#import-and-publish-a-backend-api)។

## បង្ហាញ API ជា MCP Server

ដើម្បីបង្ហាញ endpoints API យើងត្រូវតាមដានជំហានដូចខាងក្រោម៖

1. ចូលទៅកាន់ Azure Portal តាមអាសយដ្ឋាន <https://portal.azure.com/?Microsoft_Azure_ApiManagement=mcp>  
ចូលទៅកាន់ឧបករណ៍ API Management របស់អ្នក។

1. នៅម៉ឺនុយខាងឆ្វេង ជ្រើសរើស APIs > MCP Servers > + Create new MCP Server។

1. នៅក្នុង API ជ្រើសរើស REST API ដើម្បីបង្ហាញជាធាតុ MCP Server។

1. ជ្រើសរើស API Operations មួយឬច្រើន ដើម្បីបង្ហាញជាឧបករណ៍។ អ្នកអាចជ្រើសធ្វើបំផុតឬជ្រើសតែប្រតិបត្តិការណ៍ជាក់លាក់។

    ![ជ្រើសរើសវិធីបង្ហាញ](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/create-mcp-server-small.png)

1. ជ្រើសរើស **Create**។

1. ចូលទៅមុខម្ខាងម៉ឺនុយ **APIs** និង **MCP Servers** អ្នកគួរតែកើតឃើញដូចខាងក្រោម៖

    ![មើល MCP Server នៅផ្នែកចម្បង](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-list.png)

    MCP server ត្រូវបានបង្កើត ហើយ API operations ត្រូវបានបង្ហាញជាឧបករណ៍។ MCP server ត្រូវបានបញ្ជាក់នៅក្នុងផ្នែក MCP Servers។ ជួរឈរ URL បង្ហាញ endpoint នៃ MCP server ដែលអ្នកអាចហៅសាកល្បងឬក្នុងកម្មវិធីភ្ញៀវបាន។

## ជម្រើស៖ កំណត់គោលនយោបាយ

Azure API Management មានគោលនយោបាយជាគោលដៅ ដែលអ្នកអាចកំណត់ច្បាប់ផ្សេងៗសម្រាប់ endpoints របស់អ្នក ដូចជា rate limiting ឬ semantic caching។ គោលនយោបាយទាំងនេះត្រូវបានបង្កើតជាទ្រង់ទ្រាយ XML ។

នេះជារបៀបកំណត់គោលនយោបាយដើម្បីកំណត់អត្រាជាមួយ MCP Server របស់អ្នក៖

1. នៅក្នុង portal ខាងក្រោម APIs ជ្រើសរើស **MCP Servers**។

1. ជ្រើសរើស MCP server ដែលអ្នកបានបង្កើត។

1. នៅម៉ឺនុយខាងឆ្វេង ត្រូវជ្រើសរើស **Policies** នៅក្រោម MCP។

1. នៅក្នុងកម្មវិធីកែសម្រួលគោលនយោបាយ បន្ថែម ឬកែសម្រួលគោលនយោបាយដែលអ្នកចង់អនុវត្តលើឧបករណ៍របស់ MCP server។ គោលនយោបាយត្រូវបានកំណត់ជាទ្រង់ទ្រាយ XML។ ឧទាហរណ៍ អ្នកអាចបន្ថែមគោលនយោបាយដើម្បីកំណត់កំណត់ចំនួនការហៅទៅឧបករណ៍ MCP server (នៅក្នុងឧទាហរណ៍នេះ គឺ5 ហៅក្នុងរយៈពេល 30 វិនាទីរៀងរាល់អាសយដ្ឋាន IP របស់ភ្ញៀវ)៖

    ```xml
     <rate-limit-by-key calls="5" 
       renewal-period="30" 
       counter-key="@(context.Request.IpAddress)" 
       remaining-calls-variable-name="remainingCallsPerIP" 
    />
    ```
  
    រូបភាពខាងក្រោមបង្ហាញកម្មវិធីកែសម្រួលគោលនយោបាយ៖

    ![កម្មវិធីកែសម្រួលគោលនយោបាយ](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-policies-small.png)
 
## សាកល្បង

យើងត្រូវធានាថា MCP Server របស់យើងដំណើរការត្រឹមត្រូវ។

សម្រាប់នេះ យើងនឹងប្រើ Visual Studio Code និង GitHub Copilot និងរបៀប Agent mode របស់វា។ យើងនឹងបន្ថែម MCP server ទៅក្នុង *mcp.json*។ ដោយធ្វើនេះ Visual Studio Code នឹងដើរតួជា client ជា agentic និងអ្នកប្រើប្រាស់ចុងក្រោយអាចវាយអត្ថបទជំរុញហើយធ្វើអន្តរកម្មជាមួយ server នេះបាន។

មើលរបៀបបន្ថែម MCP server ក្នុង Visual Studio Code ៖

1. ប្រើអនុស្សាណៈ MCP: **Add Server command from the Command Palette**។

1. នៅពេលស្នើសុំ ជ្រើសរើសប្រភេទ server៖ **HTTP (HTTP or Server Sent Events)**។

1. បញ្ចូល URL របស់ MCP server ក្នុង API Management។ ឧទាហរណ៍៖ **https://<apim-service-name>.azure-api.net/<api-name>-mcp/sse** (សម្រាប់ SSE endpoint) ឬ **https://<apim-service-name>.azure-api.net/<api-name>-mcp/mcp** (សម្រាប់ MCP endpoint), សម្គាល់ភាពខុសគ្នានៅលើ `/sse` ឬ `/mcp` ជា តំបន់ដឹកជញ្ជូន។

1. បញ្ចូល ID server ដែលអ្នកចូលចិត្ត។ នេះគឺមិនមែនតម្លៃសំខាន់ប៉ុន្មានទេ ប៉ុន្តែជួយអ្នកចងចាំថា instance server នេះសំដៅធ្វើអ្វី។

1. ជ្រើសរើសថាត្រូវរក្សាទុកការកំណត់ក្នុង workspace settings ឬ user settings ។

  - **Workspace settings** - ការកំណត់ server ត្រូវបានរក្សាទុកនៅក្នុងឯកសារ .vscode/mcp.json ដែលមានគត់ក្នុង workspace បច្ចុប្បន្ន។

    *mcp.json*

    ```json
    "servers": {
        "APIM petstore" : {
            "type": "sse",
            "url": "url-to-mcp-server/sse"
        }
    }
    ```
  
    ឬបើអ្នកជ្រើសរើសការដឹកជញ្ជូន HTTP streaming វានឹងខុសគ្នាបន្តិច៖

    ```json
    "servers": {
        "APIM petstore" : {
            "type": "http",
            "url": "url-to-mcp-server/mcp"
        }
    }
    ```
  
  - **User settings** - ការកំណត់ server ត្រូវបានបន្ថែមទៅក្នុងឯកសារ *settings.json* ទូទៅ ហើយអាចប្រើបានក្នុង workspace ទាំងអស់។ ការកំណត់មានរូបរាងដូចខាងក្រោម៖

    ![User setting](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-servers-visual-studio-code.png)

1. អ្នកក៏ត្រូវការបន្ថែមការកំណត់មួយ ជា header ដើម្បីធានាថាវាចូលប្រើបានត្រឹមត្រូវទៅ Azure API Management។ វាប្រើ header ឈ្មោះ **Ocp-Apim-Subscription-Key**។

    - របៀបបន្ថែមវាទៅក្នុងការកំណត់៖

    ![បន្ថែម header សម្រាប់ការផ្ទៀងផ្ទាត់](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-with-header-visual-studio-code.png), វានឹងបង្ហាញសំណើឲ្យអ្នកបញ្ចូលតម្លៃ API key ដែលអ្នកអាចស្វែងរកបាននៅក្នុង Azure Portal សម្រាប់ឧបករណ៍ Azure API Management របស់អ្នក។

   - ក្នុងករណីបន្ថែមវាទៅ *mcp.json* អ្នកអាចបន្ថែមដូចខាងក្រោម៖

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
  
### ប្រើរបៀប Agent mode

ឥឡូវនេះយើងបានតំឡើងរួចទាំងស្រុង ទាំងនៅក្នុង settings ឬ *.vscode/mcp.json*។ សូមសាកល្បងវា។

គួរតែមានរូបតំណាង Tools មួយដូចខាងក្រោម ដែលបង្ហាញឧបករណ៍ដែលបានបង្ហាញពី server របស់អ្នក៖

![ឧបករណ៍ពី server](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/tools-button-visual-studio-code.png)

1. ចុចរូបតំណាងឧបករណ៍ ហើយអ្នកគួរតែបានមើលឃើញបញ្ជីឧបករណ៍ដូចខាងក្រោម៖

    ![ឧបករណ៍](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/select-tools-visual-studio-code.png)

1. វាយបញ្ចូលអត្ថបទក្នុងការជជែកដើម្បីហៅឧបករណ៍មួយ។ ឧទាហរណ៍ ប្រសិនបើអ្នកបានជ្រើសរើសឧបករណ៍សម្រាប់ទទួលព័ត៌មានអំពីការបញ្ជាទិញ អ្នកអាចសួរអ្នកបំរើអំពីការបញ្ជាទិញ។ នេះជាឧទាហរណ៍នៃបញ្ចូលអត្ថបទ៖

    ```text
    get information from order 2
    ```
  
    ឥឡូវនេះ អ្នកនឹងបានឃើញរូបតំណាងឧបករណ៍មួយសួរឲ្យអ្នកបន្តហៅឧបករណ៍។ ជ្រើសរើសបន្តបើកឧបករណ៍ ទោះបីជាអ្នកឃើញលទ្ធផលដូចខាងក្រោម៖

    ![លទ្ធផលពីបញ្ចូលអត្ថបទ](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/chat-results-visual-studio-code.png)

    **អ្វីដែលអ្នកឃើញខាងលើអាស្រ័យលើយន្តនារបស់អ្នកបានកំណត់ ប៉ុន្តែគំនិតគឺអ្នកទទួលបានចម្លើយជាអត្ថបទដូចខាងលើ**


## ឯកសារយោង

នេះជារបៀបដែលអ្នកអាចរៀនបន្ថែម៖

- [មេរៀនអំពី Azure API Management និង MCP](https://learn.microsoft.com/en-us/azure/api-management/export-rest-mcp-server)
- [ខ្នាតឧទាហរណ៍ Python៖ បញ្ជាក់ម្សៅ MCP server ចម្ងាយដោយប្រើ Azure API Management (ប្រើជំនួយ)](https://github.com/Azure-Samples/remote-mcp-apim-functions-python)

- [មន្ទីរប្រឡងអនុញ្ញាត MCP client](https://github.com/Azure-Samples/AI-Gateway/tree/main/labs/mcp-client-authorization)

- [ប្រើផ្គុំបន្ថែម Azure API Management សម្រាប់ VS Code ដើម្បីនាំចូលនិងគ្រប់គ្រង APIs](https://learn.microsoft.com/en-us/azure/api-management/visual-studio-code-tutorial)

- [ចុះឈ្មោះ និងស្គាល់ម៉ាស៊ីន MCP server ចម្ងាយនៅ Azure API Center](https://learn.microsoft.com/en-us/azure/api-center/register-discover-mcp-server)
- [AI Gateway](https://github.com/Azure-Samples/AI-Gateway) repo ល្អដែលបង្ហាញមុខងារ AI ច្រើនជាមួយ Azure API Management  
- [វេទិកា AI Gateway](https://azure-samples.github.io/AI-Gateway/) មានវេទិកាកម្មវិធីប្រើប្រាស់ Azure Portal ដដែល ជាវិធីល្អសម្រាប់ចាប់ផ្តើមវាយតម្លៃមុខងារ AI។

## តើជំហានបន្ទាប់ជាអ្វី?

- ត្រឡប់ទៅ៖ [ទិដ្ឋភាពទូទៅរបស់ ករណីសិក្សា](./README.md)
- បន្ទាប់៖ [Azure AI Travel Agents](./travelagentsample.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ចេញផ្សាយប្រកាស**៖
ឯកសារនេះត្រូវបានបកប្រែដោយប្រើសេវាកម្មបកប្រែ AI [Co-op Translator](https://github.com/Azure/co-op-translator)។ ខណៈពេលដែលយើងខិតខំប្រឹងប្រែងសម្រាប់ភាពត្រឹមត្រូវ សូមយល់ថាការបកប្រែដោយស្វ័យប្រវត្តិកម្មអាចមានកំហុស ឬភាពមិនត្រឹមត្រូវ។ ឯកសារដើមនៅក្នុងភាសាទូទៅគួរត្រូវបានគេយកទៅជាប្រភពផ្លូវការជាផ្លូវការជាងគេ។ សម្រាប់ព័ត៌មានសំខាន់ៗ ការបកប្រែដោយអ្នកជំនាញមនុស្សត្រូវបានណែនាំ។ យើងមិនទទួលខុសត្រូវចំពោះការយល់ច្រឡំ ឬការបកប្រែខុសណាដែលបណ្តាលមកពីការប្រើប្រាស់ការបកប្រែនេះឡើយ។
<!-- CO-OP TRANSLATOR DISCLAIMER END -->