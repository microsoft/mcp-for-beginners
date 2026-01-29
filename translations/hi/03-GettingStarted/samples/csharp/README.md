# Basic Calculator MCP Service

यह सेवा Model Context Protocol (MCP) के माध्यम से बुनियादी कैलकुलेटर ऑपरेशंस प्रदान करती है। इसे MCP इम्प्लीमेंटेशन सीखने वाले शुरुआती लोगों के लिए एक सरल उदाहरण के रूप में डिज़ाइन किया गया है।

अधिक जानकारी के लिए देखें [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk)

## Features

यह कैलकुलेटर सेवा निम्नलिखित क्षमताएं प्रदान करती है:

1. **बुनियादी अंकगणितीय ऑपरेशंस**:
   - दो संख्याओं का जोड़
   - एक संख्या से दूसरी संख्या को घटाना
   - दो संख्याओं का गुणा
   - एक संख्या को दूसरी संख्या से भाग देना (शून्य से भाग देने की जाँच के साथ)

## Using `stdio` Type
  
## Configuration

1. **MCP सर्वर्स को कॉन्फ़िगर करें**:
   - अपने वर्कस्पेस को VS Code में खोलें।
   - MCP सर्वर्स को कॉन्फ़िगर करने के लिए अपने वर्कस्पेस फ़ोल्डर में `.vscode/mcp.json` फ़ाइल बनाएं। उदाहरण कॉन्फ़िगरेशन:

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

   - आपसे GitHub रिपॉजिटरी रूट दर्ज करने के लिए कहा जाएगा, जिसे कमांड `git rev-parse --show-toplevel` से प्राप्त किया जा सकता है।

## Using the Service

यह सेवा MCP प्रोटोकॉल के माध्यम से निम्नलिखित API एंडपॉइंट्स प्रदान करती है:

- `add(a, b)`: दो संख्याओं को जोड़ें
- `subtract(a, b)`: पहली संख्या में से दूसरी संख्या घटाएं
- `multiply(a, b)`: दो संख्याओं का गुणा करें
- `divide(a, b)`: पहली संख्या को दूसरी संख्या से भाग दें (शून्य जाँच के साथ)
- isPrime(n): जांचें कि कोई संख्या अभाज्य है या नहीं

## Test with Github Copilot Chat in VS Code

1. MCP प्रोटोकॉल का उपयोग करके सेवा को अनुरोध भेजने का प्रयास करें। उदाहरण के लिए, आप पूछ सकते हैं:
   - "Add 5 and 3"
   - "Subtract 10 from 4"
   - "Multiply 6 and 7"
   - "Divide 8 by 2"
   - "Does 37854 prime?"
   - "What are the 3 prime numbers before after 4242?"
2. यह सुनिश्चित करने के लिए कि यह टूल्स का उपयोग कर रहा है, प्रॉम्प्ट में #MyCalculator जोड़ें। उदाहरण के लिए:
   - "Add 5 and 3 #MyCalculator"
   - "Subtract 10 from 4 #MyCalculator"

## Containerized Version

पिछला समाधान तब अच्छा है जब आपके पास .NET SDK इंस्टॉल हो और सभी निर्भरताएं मौजूद हों। हालांकि, यदि आप समाधान साझा करना चाहते हैं या इसे किसी अलग वातावरण में चलाना चाहते हैं, तो आप कंटेनराइज्ड संस्करण का उपयोग कर सकते हैं।

1. Docker शुरू करें और सुनिश्चित करें कि यह चल रहा है।
1. टर्मिनल से `03-GettingStarted\samples\csharp\src` फ़ोल्डर में जाएं
1. कैलकुलेटर सेवा के लिए Docker इमेज बनाने के लिए निम्नलिखित कमांड चलाएं (अपने Docker Hub उपयोगकर्ता नाम के साथ `<YOUR-DOCKER-USERNAME>` बदलें):
   ```bash
   docker build -t <YOUR-DOCKER-USERNAME>/mcp-calculator .
   ``` 
1. इमेज बनने के बाद, इसे Docker Hub पर अपलोड करें। निम्नलिखित कमांड चलाएं:
   ```bash
    docker push <YOUR-DOCKER-USERNAME>/mcp-calculator
  ```

## Use the Dockerized Version

1. `.vscode/mcp.json` फ़ाइल में, सर्वर कॉन्फ़िगरेशन को निम्नलिखित से बदलें:
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
   कॉन्फ़िगरेशन को देखकर आप देख सकते हैं कि कमांड `docker` है और args हैं `run --rm -i <YOUR-DOCKER-USERNAME>/mcp-calc`। `--rm` फ्लैग यह सुनिश्चित करता है कि कंटेनर बंद होने के बाद हटा दिया जाए, और `-i` फ्लैग आपको कंटेनर के स्टैंडर्ड इनपुट के साथ इंटरैक्ट करने की अनुमति देता है। आखिरी आर्गुमेंट वह इमेज का नाम है जिसे हमने अभी बनाया और Docker Hub पर अपलोड किया है।

## Test the Dockerized Version

MCP सर्वर को `"mcp-calc": {` के ऊपर छोटे Start बटन पर क्लिक करके शुरू करें, और पहले की तरह आप कैलकुलेटर सेवा से गणना करने के लिए कह सकते हैं।

**अस्वीकरण**:  
यह दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके अनुवादित किया गया है। जबकि हम सटीकता के लिए प्रयासरत हैं, कृपया ध्यान दें कि स्वचालित अनुवादों में त्रुटियाँ या अशुद्धियाँ हो सकती हैं। मूल दस्तावेज़ अपनी मूल भाषा में ही अधिकारिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सलाह दी जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम जिम्मेदार नहीं हैं।