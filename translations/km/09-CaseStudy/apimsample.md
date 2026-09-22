# ករណីសិក្សា៖ បង្ហាញ REST API ក្នុង API Management ជា MCP server

Azure API Management គឺជាសេវាកម្មមួយដែលផ្តល់ Gateway នៅលើចុងបញ្ចប់ API របស់អ្នក។ វាដំណើរការដោយ Azure API Management មានតួនាទីដូចជា proxy នៅមុខ API របស់អ្នក ហើយអាចសម្រេចចិត្តថាតើត្រូវធ្វើអ្វីជាមួយសំណើបញ្ចូល។

ដោយប្រើវា អ្នកអាចបន្ថែមមុខងារច្រើនដូចជា៖

- **សន្តិសុខ** អ្នកអាចប្រើបានគ្រប់យ៉ាងចាប់ពី API keys, JWT រហូតដល់ managed identity។
- **កំណត់អត្រា (Rate limiting)** មុខងារដ៏ចម្លែកមួយគឺអាចសម្រេចចិត្តថាតើការហៅប៉ុន្មានដែលអាចឆ្លងកាត់ក្នុងរយៈពេលកំណត់មួយ។ វាជួយធានាថា អ្នកប្រើទាំងអស់ទទួលបានបទពិសោធរល្អ និងសេវាកម្មរបស់អ្នកមិនភ្លឺចរន្តសំណើខ្លាំងពេកទេ។
- **ការវាស់វែង និងតុល្យភាពបន្ទុក** អ្នកអាចកំណត់ចុងបញ្ចប់ជាច្រើនដើម្បីតុល្យភាពបន្ទុក ហើយអ្នកអាចសម្រេចចិត្តរបៀប "តុល្យភាពបន្ទុក" ផងដែរ។
- **មុខងារ AI ដូចជាការស្តុកតាមអត្ថន័យ (semantic caching), កំណត់បរិមាណ token, មើលទីតាំង token និងផ្សេងៗទៀត** មុខងារទាំងនេះមានសារៈសំខាន់ពង្រីកប្រសិទ្ធភាពនៃការឆ្លើយតប និងជួយឱ្យអ្នកគ្រប់គ្រងចំណាយវិនិយោគ token បានល្អ។ [អានបន្ថែមនៅទីនេះ](https://learn.microsoft.com/en-us/azure/api-management/genai-gateway-capabilities)។ 

## ហេតុអ្វី MCP + Azure API Management?

Model Context Protocol កំពុងតែក្លាយជាមាត្រដ្ឋានមួយសម្រាប់កម្មវិធី AI មូលដ្ឋានភ្នាក់ងារនិងរបៀបបង្ហាញឧបករណ៍និងទិន្នន័យនៅក្នុងរបៀបស្ថាពរ។ Azure API Management ជាជម្រើសធម្មជាតិបើអ្នកត្រូវ "គ្រប់គ្រង" API។ MCP Servers ជាញឹកញាប់បញ្ចូលជាមួយ API ផ្សេងទៀតដើម្បីជួយដោះស្រាយសំណើទៅឧបករណ៍មួយ។ ដូច្នេះការរួមបញ្ចូល Azure API Management និង MCP មានអត្ថន័យច្រើន។

## ទិដ្ឋភាពទូទៅ

ក្នុងករណីនេះ យើងនឹងរៀនរបៀបបង្ហាញចុងបញ្ចប់ API ជា MCP Server។ ដោយធ្វើដូចនេះ យើងអាចបញ្ចូលចុងបញ្ចប់ទាំងនេះជាផ្នែកមួយនៃកម្មវិធី agentic ខណៈដែលក៏ប្រើប្រាស់មុខងារពី Azure API Management ផងដែរ។

## មុខងារសំខាន់

- អ្នកជ្រើសរើសវិធីសាស្រ្តចុងបញ្ចប់ដែលចង់បង្ហាញជាឧបករណ៍។
- មុខងារបន្ថែមដែលអ្នកទទួលបានអាស្រ័យលើនីតិវិធីដែលអ្នកកំណត់នៅផ្នែកគោលនយោបាយសម្រាប់ API របស់អ្នក។ តែកន្លែងនេះយើងនឹងបង្ហាញអ្នករបៀបបន្ថែមកំណត់អត្រា។

## ជំហានមុន៖ នាំចូល API

ប្រសិនបើអ្នកមាន API នៅក្នុង Azure API Management រួចហើយ គឺល្អហើយ អ្នកអាចរំកិលជំហាននេះបាន។ ប្រសិនបើមិនមាន សូមពិនិត្យតំណភ្ជាប់នេះ [នាំចូល API ទៅ Azure API Management](https://learn.microsoft.com/en-us/azure/api-management/import-and-publish#import-and-publish-a-backend-api)។

## បង្ហាញ API ជា MCP Server

ដើម្បីបង្ហាញចុងបញ្ចប់ API សូមអនុវត្តតាមជំហានខាងក្រោម៖

1. ចូលទៅ Azure Portal និងអាសយដ្ឋាន <https://portal.azure.com/?Microsoft_Azure_ApiManagement=mcp> 
ចូលទៅវត្តមាន API Management របស់អ្នក។

1. នៅម៉ឺនុយด้านឆ្វេង ជ្រើស APIs > MCP Servers > + បង្កើត MCP Server ថ្មី។

1. នៅក្នុង API ជ្រើស REST API មួយសម្រាប់បង្ហាញជាផ្នែក MCP Server។

1. ជ្រើសកម្មវិធី API មួយឬច្រើនសម្រាប់បង្ហាញជាឧបករណ៍។ អ្នកអាចជ្រើសកម្មវិធីទាំងអស់ ឬក៏ជាជាក់លាក់។

    ![ជ្រើសវិធីសាស្រ្តសម្រាប់បង្ហាញ](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/create-mcp-server-small.png)


1. ជ្រើស **បង្កើត(Create)**។

1. ចូលទៅម៉ឺនុយជ្រើស **APIs** និង **MCP Servers** អ្នកគួរតែឃើញដូចខាងក្រោម៖

    ![មើល MCP Server នៅផ្ទាំងចម្បង](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-list.png)

    MCP server ត្រូវបានបង្កើត ហើយកម្មវិធី API ត្រូវបានបង្ហាញជា ឧបករណ៍។ MCP server ត្រូវបានបញ្ជីនៅផ្ទាំង MCP Servers។ ជួរឈរបង្ហាញ URL នៃចុងបញ្ចប់ MCP server ដែលអ្នកអាចហៅសម្រាប់ការសាកល្បង ឬក្នុងកម្មវិធី client។

## ជម្រើស៖ កំណត់គោលនយោបាយ

Azure API Management មានគំនិតមូលដ្ឋានគឺគោលនយោបាយ ដែលអ្នកអាចកំណត់ច្បាប់ខុសៗគ្នាសម្រាប់ចុងបញ្ចប់ រួមមាន ការកំណត់អត្រាឬស្តុកតាមអត្ថន័យ។ គោលនយោបាយទាំងនេះត្រូវបានបង្កើតនៅទ្រង់ទ្រាយ XML។

នេះជារបៀបដែលអ្នកអាចកំណត់គោលនយោបាយដើម្បីកំណត់អត្រាការហៅទៅ MCP Server របស់អ្នក៖

1. នៅក្នុង portal ខាងក្រោម APIs ជ្រើស **MCP Servers**។

1. ជ្រើស MCP Server ដែលអ្នកបានបង្កើត។

1. នៅម៉ឺនុយបង្ហាញនៅឆ្វេងក្រោម MCP ជ្រើស **Policies**។

1. នៅម៉ាស៊ីនកែសម្រួលគោលនយោបាយ បន្ថែម ឬកែសម្រួលគោលនយោបាយដែលអ្នកចង់អនុវត្តទៅ​ឧបករណ៍របស់ MCP server។ គោលនយោបាយត្រូវបានកំណត់​នៅទ្រង់ទ្រាយ XML។ ឧទាហរណ៍ អ្នកអាចបន្ថែមគោលនយោបាយដើម្បីកំណត់ការហៅទៅឧបករណ៍ MCP server (ក្នុងឧទាហរណ៍នេះ គឺ ៥ ហៅក្នុងរយៈពេល ៣០ វិនាទី ក្នុងមួយអាសយដ្ឋាន IP client)។ នេះគឺ XML ដែលនឹងធ្វើឱ្យវាកំណត់អត្រា៖

    ```xml
     <rate-limit-by-key calls="5" 
       renewal-period="30" 
       counter-key="@(context.Request.IpAddress)" 
       remaining-calls-variable-name="remainingCallsPerIP" 
    />
    ```

    នេះជារូបភាពនៃម៉ាស៊ីនកែសម្រួលគោលនយោបាយ៖

    ![ម៉ាស៊ីនកែសម្រួលគោលនយោបាយ](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-policies-small.png)
 
## សាកល្បងវា

យើងត្រូវធានាថា MCP Server របស់យើងដំណើរការត្រឹមត្រូវ។

> [!NOTE]
> Azure API Management បច្ចុប្បន្នបង្ហាញម៉ាស៊ីនបម្រើនេះតាមរយៈ Streamable
> HTTP `/mcp` endpoint។ ការដឹកជញ្ជូន HTTP+SSE `/sse` ដែលចាស់ជាងនេះត្រូវបានលះបង់ និង
> គួរតែប្រើប្រាស់តែជាមួយ client ចាស់ៗប៉ុណ្ណោះ។

សម្រាប់នេះ យើងនឹងប្រើ Visual Studio Code និង GitHub Copilot ជាមួយរបៀប Agent របស់វា។ យើងនឹងបន្ថែម MCP server ទៅក្នុង *mcp.json* មួយ។ ដោយធ្វើដូចនេះ Visual Studio Code នឹងដំណើរការជា client មានសមត្ថភាព agentic ហើយអ្នកប្រើបញ្ចូលអាកាសន័យហើយអាចទៅតាមរបៀបចូលរួមជាមួយម៉ាស៊ីនបម្រើនោះបាន។

មកមើលរបៀបបន្ថែម MCP server ក្នុង Visual Studio Code៖

1. ប្រើក្រុមបញ្ជា MCP: **Add Server command from the Command Palette**។

1. នៅពេលប្រើប្រាស់ ជ្រើសប្រភេទម៉ាស៊ីនបម្រុង៖ **HTTP (HTTP ឬ Server Sent Events)**។

1. បញ្ចូល Streamable HTTP URL ដែលបានបង្ហាញសម្រាប់ MCP server ក្នុង API Management។
    ឧទាហរណ៍៖
    `https://<apim-service-name>.azure-api.net/<api-name>-mcp/mcp`។

1. បញ្ចូល server ID មួយដែលអ្នកចូលចិត្ត។ វាមិនមែនតម្លៃសំខាន់ទេ ប៉ុន្តែវាជួយអ្នកចងចាំថា ម៉ាស៊ីនបម្រើនេះជារូបមន្តណា។

1. ជ្រើសថាតើអ្នកចង់រក្សាកាលបរិច្ឆេទនេះទៅក្នុងការកំណត់ workspace របស់អ្នក ឬការកំណត់ user settings។

  - **Workspace settings** - ការកំណត់ម៉ាស៊ីនបម្រើត្រូវបានរក្សាទុកនៅក្នុងឯកសារ .vscode/mcp.json ដែលមានតែក្នុង workspace បច្ចុប្បន្នប៉ុណ្ណោះ។

    *mcp.json*

    ```json
    "servers": {
        "APIM petstore" : {
            "type": "http",
            "url": "url-to-mcp-server/mcp"
        }
    }
    ```

  - **User settings** - ការកំណត់ម៉ាស៊ីនបម្រើត្រូវបានបញ្ចូលទៅឯកសារ *settings.json* កូដកំណត់របស់អ្នក និងអាចប្រើបានគ្រប់ workspace ។ ការកំណត់នេះសម្រួលដូចខាងក្រោម៖

    ![User setting](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-servers-visual-studio-code.png)

1. អ្នកត្រូវបន្ថែមកំណត់មួយផង ប្រើ header ដើម្បីធានាថាវាបានធ្វើការផ្ទៀងផ្ទាត់សម្ងាត់ចូលរបៀបត្រឹមត្រូវទៅ Azure API Management។ វាប្រើ header ឈ្មោះ **Ocp-Apim-Subscription-Key**។


    - នេះជាវិធីដែលអ្នកអាចបន្ថែមវាទៅកាន់ការកំណត់បាន៖

    ![Adding header for authentication](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-with-header-visual-studio-code.png), នេះនឹងបណ្ដាលឲ្យមានបង្ហាញជាសារ​ដើម្បីសួរអំពីតម្លៃកូនសោ API ដែលអ្នកអាចរកបាននៅក្នុងផតថល Azure សម្រាប់ឧបករណ៍គ្រប់គ្រង Azure API របស់អ្នក។

   - ដើម្បីបន្ថែមវាទៅ *mcp.json* ផ្ទាល់ អ្នកអាចបន្ថែមវាដូចខាងក្រោម៖

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

### ប្រើរបៀប Agent

ឥឡូវនេះយើងបានតំឡើងរួចរួមទាំងក្នុងការកំណត់ឬក្នុង *.vscode/mcp.json*។ តោះសាកល្បងវា។

គួរតែមានរូបតំណាងឧបករណ៍មួយដូចខាងក្រោម ដែលបង្ហាញឧបករណ៍ដែលបង្ហាញពីម៉ាស៊ីនមេរបស់អ្នក៖

![Tools from the server](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/tools-button-visual-studio-code.png)

1. ចុចរូបតំណាងឧបករណ៍ ហើយអ្នកគួរតែឃើញបញ្ជីឧបករណ៍ដូចខាងក្រោម៖

    ![Tools](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/select-tools-visual-studio-code.png)

1. បញ្ចូលសារ​ជជែកដើម្បីហៅឧបករណ៍។ ឧទាហរណ៍ បើអ្នកជ្រើសឧបករណ៍មួយសម្រាប់ទទួលព័ត៌មានអំពីការបញ្ជារទិញ អ្នកអាចសួរអ្នកតំណាងអំពីការបញ្ជារទិញនោះ។ នេះជាការបញ្ចូលសារជាឧទាហរណ៍៖

    ```text
    get information from order 2
    ```

    ឥឡូវនេះអ្នកនឹងបានបង្ហាញជាមួយរូបតំណាងឧបករណ៍ដែលសួរអ្នកថាតើចង់បន្តហៅឧបករណ៍ដែរឬទេ។ ជ្រើសរើសបន្តដំណើរការ​ឧបករណ៍ អ្នកគួរតែឃើញលទ្ធផលដូចខាងក្រោម៖

    ![Result from prompt](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/chat-results-visual-studio-code.png)

    **អ្វីដែលអ្នកមើលឃើញខាងលើពឹងផ្អែកលើឧបករណ៍ដែលអ្នកបានកំណត់ ប៉ុន្តិគំនិតគឺអ្នកទទួលបានការឆ្លើយតបជារបាយការណ៍អក្សរដូចខាងលើ**


## ឯកសារយោង

វិធីដែលអ្នកអាចរៀនបន្ថែម៖

- [មេរៀនលើ Azure API Management និង MCP](https://learn.microsoft.com/en-us/azure/api-management/export-rest-mcp-server)
- [គំរូ Python: ដាក់សោរការចូលប្រើរបស់ម៉ាស៊ីន MCP ដោយប្រើ Azure API Management (កំពុងបណ្តុះបណ្តាល)](https://github.com/Azure-Samples/remote-mcp-apim-functions-python)

- [មន្ទីរបណ្ដុះបណ្ដាលការអនុញ្ញាត MCP client](https://github.com/Azure-Samples/AI-Gateway/tree/main/labs/mcp-client-authorization)

- [ប្រើកម្មវិធីបន្ថែម Azure API Management សម្រាប់ VS Code ដើម្បីនាំចូល និងគ្រប់គ្រង API](https://learn.microsoft.com/en-us/azure/api-management/visual-studio-code-tutorial)

- [ចុះបញ្ជី និងស្វែងរកម៉ាស៊ីន MCP តាមចគ្រវាត់ Azure API Center](https://learn.microsoft.com/en-us/azure/api-center/register-discover-mcp-server)
- [AI Gateway](https://github.com/Azure-Samples/AI-Gateway) ជាគម្រោងរួមបង្ហាញពីសមត្ថភាព AI ច្រើនជាមួយ Azure API Management
- [សិក្ខាសាលា AI Gateway](https://azure-samples.github.io/AI-Gateway/) រួមមានសិក្ខាសាលាដែលប្រើ Azure Portal ដែលជា វិធីល្អសម្រាប់ចាប់ផ្ដើមវាយតម្លៃសមត្ថភាព AI។

## តើអ្វីទៅជា ជំហានបន្ទាប់

- ត្រឡប់ទៅ៖ [ទិដ្ឋភាពទូទៅនៃករណីសិក្សា](./README.md)
- បន្ទាប់៖ [ភ្នាក់ងារធ្វើដំណើរប្រើ AI របស់ Azure](./travelagentsample.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ការបដិសេធ**:
ឯកសារនេះត្រូវបានបម្លែងភាសា ដោយប្រើសេវាបម្លែងភាសា AI [Co-op Translator](https://github.com/Azure/co-op-translator)។ ទោះយើងខ្ញុំមានក្តីប្រាថ្នាឱ្យបានច្បាស់លាស់ តែសូមយល់ដឹងថាការបម្លែងដោយស្វ័យប្រវត្តិក៏អាចមានកំហុសឬភាពមិនត្រឹមត្រូវ។ ឯកសារដើមជាភាសាទីតាំងគួរត្រូវបានគេប្រើជាប្រភពច្បាស់លាស់។ សម្រាប់ព័ត៌មានសំខាន់ៗ សូមណែនាំឱ្យប្រើប្រាស់ការប្រែដោយមនុស្សជំនាញ។ យើងខ្ញុំមិនទទួលខុសត្រូវចំពោះការយល់ច្រឡំ ឬការបកស្រាយខុសបន្ទាប់ពីការប្រើប្រាស់ការបម្លែងនេះនោះទេ។
<!-- CO-OP TRANSLATOR DISCLAIMER END -->