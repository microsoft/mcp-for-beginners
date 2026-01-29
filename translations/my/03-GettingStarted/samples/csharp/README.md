# Basic Calculator MCP Service

ဤဝန်ဆောင်မှုသည် Model Context Protocol (MCP) မှတဆင့် အခြေခံ ကိန်းဂဏန်းတွက်ချက်မှုများကို ပေးဆောင်သည်။ MCP ကို လေ့လာနေသော စတင်သူများအတွက် ရိုးရှင်းသည့် ဥပမာတစ်ခုအဖြစ် ဒီဝန်ဆောင်မှုကို ဒီဇိုင်းဆွဲထားသည်။

အသေးစိတ်အချက်အလက်များအတွက် [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk) ကို ကြည့်ပါ။

## Features

ဤ ကိန်းဂဏန်းတွက်ချက်မှု ဝန်ဆောင်မှုတွင် အောက်ပါ လုပ်ဆောင်ချက်များ ပါဝင်သည်-

1. **အခြေခံ သင်္ချာဆိုင်ရာ လုပ်ဆောင်ချက်များ**:
   - နံပါတ်နှစ်ခုကို ပေါင်းခြင်း
   - နံပါတ်တစ်ခုမှ နံပါတ်တစ်ခုကို ဖြုတ်ခြင်း
   - နံပါတ်နှစ်ခုကို မြှောက်ခြင်း
   - နံပါတ်တစ်ခုကို နံပါတ်တစ်ခုဖြင့် ခွဲခြင်း (သုညဖြင့် ခွဲခြင်းကို စစ်ဆေးသည်)

## Using `stdio` Type
  
## Configuration

1. **MCP Servers ကို ပြင်ဆင်ခြင်း**:
   - သင့် workspace ကို VS Code တွင် ဖွင့်ပါ။
   - MCP servers များကို ပြင်ဆင်ရန် သင့် workspace ဖိုလ်ဒါအတွင်း `.vscode/mcp.json` ဖိုင်ကို ဖန်တီးပါ။ ဥပမာ ပြင်ဆင်မှုမှာ -

     ```jsonc
     {
       "inputs": [
         {
           "type": "promptString",
           "id": "repository-root",
           "description": "The absolute path to the repository root"
         }
       ],
       "servers": {
         "calculator-mcp-dotnet": {
           "type": "stdio",
           "command": "dotnet",
           "args": [
             "run",
             "--project",
             "${input:repository-root}/03-GettingStarted/samples/csharp/src/calculator.csproj"
           ]
         }
       }
     }
     ```

   - GitHub repository root ကို ထည့်ရန် မေးမြန်းမည်ဖြစ်ပြီး၊ ၎င်းကို `git rev-parse --show-toplevel` ကွန်မန်းဒ်မှ ရယူနိုင်သည်။

## Using the Service

ဝန်ဆောင်မှုသည် MCP protocol မှတဆင့် အောက်ပါ API endpoints များကို ဖော်ပြပေးသည်-

- `add(a, b)`: နံပါတ်နှစ်ခုကို ပေါင်းခြင်း
- `subtract(a, b)`: ပထမနံပါတ်မှ ဒုတိယနံပါတ်ကို ဖြုတ်ခြင်း
- `multiply(a, b)`: နံပါတ်နှစ်ခုကို မြှောက်ခြင်း
- `divide(a, b)`: ပထမနံပါတ်ကို ဒုတိယနံပါတ်ဖြင့် ခွဲခြင်း (သုညစစ်ဆေးမှုပါ)
- isPrime(n): နံပါတ်တစ်ခုသည် ဗဟိုနံပါတ်ဖြစ်မဖြစ် စစ်ဆေးခြင်း

## Test with Github Copilot Chat in VS Code

1. MCP protocol ကို အသုံးပြု၍ ဝန်ဆောင်မှုသို့ တောင်းဆိုမှုတစ်ခု ပြုလုပ်ကြည့်ပါ။ ဥပမာ၊ မေးမြန်းနိုင်သည်-
   - "Add 5 and 3"
   - "Subtract 10 from 4"
   - "Multiply 6 and 7"
   - "Divide 8 by 2"
   - "Does 37854 prime?"
   - "What are the 3 prime numbers before after 4242?"
2. ၎င်းသည် tools ကို အသုံးပြုနေကြောင်း သေချာစေရန် prompt တွင် #MyCalculator ကို ထည့်ပါ။ ဥပမာ-
   - "Add 5 and 3 #MyCalculator"
   - "Subtract 10 from 4 #MyCalculator"

## Containerized Version

ယခင်ဖြေရှင်းချက်သည် .NET SDK ထည့်သွင်းပြီး၊ လိုအပ်သော dependencies များ ပြည့်စုံသောအခါ အထူးသင့်တော်သည်။ သို့သော် ဖြေရှင်းချက်ကို မျှဝေလိုပါက သို့မဟုတ် အခြားပတ်ဝန်းကျင်တွင် ပြေးဆွဲလိုပါက containerized version ကို အသုံးပြုနိုင်သည်။

1. Docker ကို စတင်ပြီး အလုပ်လုပ်နေကြောင်း သေချာပါစေ။
1. terminal မှ `03-GettingStarted\samples\csharp\src` ဖိုလ်ဒါသို့ သွားပါ။
1. ကိန်းဂဏန်းတွက်ချက်မှု ဝန်ဆောင်မှုအတွက် Docker image ကို တည်ဆောက်ရန် အောက်ပါ command ကို အကောင်အထည်ဖော်ပါ ( `<YOUR-DOCKER-USERNAME>` ကို သင့် Docker Hub username ဖြင့် အစားထိုးပါ)-
   ```bash
   docker build -t <YOUR-DOCKER-USERNAME>/mcp-calculator .
   ``` 
1. image တည်ဆောက်ပြီးနောက် Docker Hub သို့ တင်ရန် အောက်ပါ command ကို ပြေးပါ-
   ```bash
    docker push <YOUR-DOCKER-USERNAME>/mcp-calculator
  ```

## Use the Dockerized Version

1. `.vscode/mcp.json` ဖိုင်တွင် server configuration ကို အောက်ပါအတိုင်း ပြောင်းလဲပါ-
   ```json
    "mcp-calc": {
      "command": "docker",
      "args": [
        "run",
        "--rm",
        "-i",
        "<YOUR-DOCKER-USERNAME>/mcp-calc"
      ],
      "envFile": "",
      "env": {}
    }
   ```
   configuration ကို ကြည့်မယ်ဆိုရင် command သည် `docker` ဖြစ်ပြီး args တွေမှာ `run --rm -i <YOUR-DOCKER-USERNAME>/mcp-calc` ဖြစ်သည်။ `--rm` flag သည် container ရပ်နားပြီးနောက် ဖျက်ပစ်ရန် ဖြစ်ပြီး `-i` flag သည် container ၏ standard input နှင့် အပြန်အလှန် ဆက်သွယ်နိုင်စေရန် ဖြစ်သည်။ နောက်ဆုံး argument သည် ကျွန်ုပ်တို့ တည်ဆောက်ပြီး Docker Hub သို့ တင်ထားသော image အမည်ဖြစ်သည်။

## Test the Dockerized Version

`"mcp-calc": {` အပေါ်ရှိ Start ခလုတ်ကို နှိပ်၍ MCP Server ကို စတင်ပါ၊ ယခင်ကဲ့သို့ ကိန်းဂဏန်းတွက်ချက်မှု ဝန်ဆောင်မှုကို တောင်းဆိုနိုင်ပါပြီ။

**အကြောင်းကြားချက်**  
ဤစာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ဖြင့် ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှန်ကန်မှုအတွက် ကြိုးစားသော်လည်း၊ အလိုအလျောက် ဘာသာပြန်ခြင်းသည် အမှားများ သို့မဟုတ် မှားယွင်းချက်များ ပါဝင်နိုင်ကြောင်း သတိပြုပါရန် မေတ္တာရပ်ခံအပ်ပါသည်။ မူရင်းစာတမ်းကို မိမိဘာသာစကားဖြင့်သာ တရားဝင်အရင်းအမြစ်အဖြစ် ယူဆသင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူ့ဘာသာပြန်သူမှ တာဝန်ယူ၍ ဘာသာပြန်ခြင်းကို အကြံပြုပါသည်။ ဤဘာသာပြန်ချက်ကို အသုံးပြုရာမှ ဖြစ်ပေါ်လာနိုင်သည့် နားလည်မှုမှားယွင်းမှုများအတွက် ကျွန်ုပ်တို့သည် တာဝန်မယူပါ။