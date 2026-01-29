# Basic Calculator MCP Service

Ang serbisyong ito ay nagbibigay ng mga pangunahing operasyon ng calculator gamit ang Model Context Protocol (MCP). Dinisenyo ito bilang isang simpleng halimbawa para sa mga nagsisimula na gustong matutunan ang tungkol sa mga implementasyon ng MCP.

Para sa karagdagang impormasyon, tingnan ang [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk)

## Mga Tampok

Ang serbisyong calculator na ito ay may mga sumusunod na kakayahan:

1. **Pangunahing Operasyon sa Aritmetika**:
   - Pagdaragdag ng dalawang numero
   - Pagbabawas ng isang numero mula sa isa pa
   - Pagmumultiply ng dalawang numero
   - Pagdidibisyon ng isang numero sa isa pa (na may tseke sa zero division)

## Paggamit ng `stdio` Type

## Konfigurasyon

1. **I-configure ang MCP Servers**:
   - Buksan ang iyong workspace sa VS Code.
   - Gumawa ng `.vscode/mcp.json` na file sa iyong workspace folder para i-configure ang MCP servers. Halimbawa ng konfigurasyon:

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

   - Hihingin sa iyo na ilagay ang root ng GitHub repository, na makukuha gamit ang utos na `git rev-parse --show-toplevel`.

## Paggamit ng Serbisyo

Ipinapakita ng serbisyo ang mga sumusunod na API endpoints sa pamamagitan ng MCP protocol:

- `add(a, b)`: Idagdag ang dalawang numero
- `subtract(a, b)`: Ibawas ang pangalawang numero mula sa una
- `multiply(a, b)`: Imultiply ang dalawang numero
- `divide(a, b)`: Hatiin ang unang numero sa pangalawa (na may tseke sa zero)
- isPrime(n): Suriin kung ang isang numero ay prime

## Pagsubok gamit ang Github Copilot Chat sa VS Code

1. Subukang gumawa ng request sa serbisyo gamit ang MCP protocol. Halimbawa, maaari mong itanong:
   - "Add 5 and 3"
   - "Subtract 10 from 4"
   - "Multiply 6 and 7"
   - "Divide 8 by 2"
   - "Does 37854 prime?"
   - "What are the 3 prime numbers before after 4242?"
2. Para matiyak na ginagamit nito ang mga tools, idagdag ang #MyCalculator sa prompt. Halimbawa:
   - "Add 5 and 3 #MyCalculator"
   - "Subtract 10 from 4 #MyCalculator"

## Containerized Version

Maganda ang naunang solusyon kapag naka-install ang .NET SDK at kumpleto ang mga dependencies. Ngunit kung nais mong ibahagi ang solusyon o patakbuhin ito sa ibang environment, maaari mong gamitin ang containerized na bersyon.

1. Simulan ang Docker at siguraduhing ito ay tumatakbo.
1. Mula sa terminal, pumunta sa folder na `03-GettingStarted\samples\csharp\src`
1. Para i-build ang Docker image para sa calculator service, patakbuhin ang sumusunod na utos (palitan ang `<YOUR-DOCKER-USERNAME>` ng iyong Docker Hub username):
   ```bash
   docker build -t <YOUR-DOCKER-USERNAME>/mcp-calculator .
   ```
1. Pagkatapos mabuo ang image, i-upload ito sa Docker Hub gamit ang sumusunod na utos:
   ```bash
    docker push <YOUR-DOCKER-USERNAME>/mcp-calculator
  ```

## Paggamit ng Dockerized Version

1. Sa `.vscode/mcp.json` na file, palitan ang server configuration ng sumusunod:
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
   Sa konfigurasyon, makikita mo na ang command ay `docker` at ang args ay `run --rm -i <YOUR-DOCKER-USERNAME>/mcp-calc`. Ang `--rm` flag ay nagsisiguro na matatanggal ang container pagkatapos itong huminto, at ang `-i` flag ay nagbibigay-daan para makipag-ugnayan sa standard input ng container. Ang huling argumento ay ang pangalan ng image na kakabuo lang natin at na-upload sa Docker Hub.

## Pagsubok sa Dockerized Version

Simulan ang MCP Server sa pamamagitan ng pag-click sa maliit na Start button sa itaas ng `"mcp-calc": {`, at tulad ng dati, maaari mong hilingin sa calculator service na gumawa ng mga kalkulasyon para sa iyo.

**Paalala**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagamat nagsusumikap kami para sa katumpakan, pakatandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o di-tumpak na impormasyon. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na maaaring magmula sa paggamit ng pagsasaling ito.