# Huduma ya Calculator Msingi MCP

Huduma hii hutoa shughuli za msingi za calculator kupitia Model Context Protocol (MCP). Imetengenezwa kama mfano rahisi kwa wanaoanza kujifunza kuhusu utekelezaji wa MCP.

Kwa maelezo zaidi, angalia [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk)

## Sifa

Huduma hii ya calculator inatoa uwezo ufuatao:

1. **Shughuli za Msingi za Hisabati**:
   - Kuongeza nambari mbili
   - Kutoa nambari moja kutoka nyingine
   - Kuzidisha nambari mbili
   - Kugawanya nambari moja kwa nyingine (ikiwa na ukaguzi wa mgawanyiko kwa sifuri)

## Kutumia Aina ya `stdio`
  
## Usanidi

1. **Sanidi Seva za MCP**:
   - Fungua eneo lako la kazi (workspace) katika VS Code.
   - Tengeneza faili `.vscode/mcp.json` katika folda ya eneo lako la kazi ili kusanidi seva za MCP. Mfano wa usanidi:

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

   - Utaombwa kuingiza mzizi wa hifadhi ya GitHub, ambao unaweza kupatikana kwa amri, `git rev-parse --show-toplevel`.

## Kutumia Huduma

Huduma inaonyesha API endpoints zifuatazo kupitia itifaki ya MCP:

- `add(a, b)`: Ongeza nambari mbili pamoja
- `subtract(a, b)`: Toa nambari ya pili kutoka ya kwanza
- `multiply(a, b)`: Zidisha nambari mbili
- `divide(a, b)`: Gawanya nambari ya kwanza kwa ya pili (ikiwa na ukaguzi wa sifuri)
- isPrime(n): Angalia kama nambari ni ya kwanza (prime)

## Jaribu na Github Copilot Chat katika VS Code

1. Jaribu kutuma ombi kwa huduma ukitumia itifaki ya MCP. Kwa mfano, unaweza kuuliza:
   - "Ongeza 5 na 3"
   - "Toa 10 kutoka 4"
   - "Zidisha 6 na 7"
   - "Gawanya 8 kwa 2"
   - "Je, 37854 ni nambari ya kwanza?"
   - "Nambari zipi 3 za kwanza kabla na baada ya 4242?"
2. Ili kuhakikisha inatumia zana, ongeza #MyCalculator kwenye maelezo. Kwa mfano:
   - "Ongeza 5 na 3 #MyCalculator"
   - "Toa 10 kutoka 4 #MyCalculator"

## Toleo la Containerized

Suluhisho lililopita ni zuri wakati una SDK ya .NET imewekwa, na utegemezi wote uko sawa. Hata hivyo, ikiwa ungependa kushiriki suluhisho au kuendesha katika mazingira tofauti, unaweza kutumia toleo la containerized.

1. Anzisha Docker na hakikisha inaendesha.
1. Kutoka kwenye terminal, elekea kwenye folda `03-GettingStarted\samples\csharp\src`
1. Ili kujenga picha ya Docker kwa huduma ya calculator, tumia amri ifuatayo (badilisha `<YOUR-DOCKER-USERNAME>` na jina lako la mtumiaji wa Docker Hub):
   ```bash
   docker build -t <YOUR-DOCKER-USERNAME>/mcp-calculator .
   ```
1. Baada ya picha kujengwa, tushirikishe kwenye Docker Hub. Endesha amri ifuatayo:
   ```bash
    docker push <YOUR-DOCKER-USERNAME>/mcp-calculator
  ```

## Tumia Toleo la Dockerized

1. Katika faili `.vscode/mcp.json`, badilisha usanidi wa seva kwa ifuatayo:
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
   Ukiangalia usanidi, utaona amri ni `docker` na hoja ni `run --rm -i <YOUR-DOCKER-USERNAME>/mcp-calc`. Bendera `--rm` inahakikisha kontena linaondolewa baada ya kusimama, na bendera `-i` inakuwezesha kuingiliana na ingizo la kawaida la kontena. Hoja ya mwisho ni jina la picha tuliyojenga na kusukuma kwenye Docker Hub.

## Jaribu Toleo la Dockerized

Anzisha MCP Server kwa kubofya kitufe kidogo cha Anza juu ya `"mcp-calc": {`, na kama awali unaweza kumuomba huduma ya calculator kufanya hesabu kwako.

**Kiarifu cha Kutotegemea**:  
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kwa usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Hati ya asili katika lugha yake ya asili inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu inayofanywa na binadamu inapendekezwa. Hatubebei dhamana kwa kutoelewana au tafsiri potofu zinazotokana na matumizi ya tafsiri hii.