# Pangunahing Serbisyo ng Calculator MCP

Ang serbisyong ito ay nagbibigay ng pangunahing mga operasyon ng calculator sa pamamagitan ng Model Context Protocol (MCP). Ito ay dinisenyo bilang isang simpleng halimbawa para sa mga nagsisimula na nag-aaral tungkol sa mga implementasyon ng MCP.

Para sa karagdagang impormasyon, tingnan ang [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk)

## Mga Tampok

Ang serbisyong calculator na ito ay nag-aalok ng mga sumusunod na kakayahan:

1. **Pangunahing Mga Operasyong Aritmetika**:
   - Pagdaragdag ng dalawang numero
   - Pagbabawas ng isang numero mula sa isa pa
   - Pagmumultiplika ng dalawang numero
   - Paghahati ng isang numero sa isa pa (na may tseke sa paghahati sa zero)

## Paggamit ng `stdio` Uri
  
## Konfigurasyon

1. **I-configure ang Mga Server ng MCP**:
   - Buksan ang iyong workspace sa VS Code.
   - Gumawa ng `.vscode/mcp.json` file sa iyong workspace folder upang i-configure ang mga server ng MCP. Halimbawa ng konfigurasyon:

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

   - Hihilingin sa'yo na ipasok ang GitHub repository root, na maaaring makuha mula sa utos na `git rev-parse --show-toplevel`.

## Paggamit ng Serbisyo

Inilalantad ng serbisyo ang mga sumusunod na API endpoints sa pamamagitan ng MCP protocol:

- `add(a, b)`: Idagdag ang dalawang numero
- `subtract(a, b)`: Ibawas ang pangalawang numero mula sa una
- `multiply(a, b)`: Imultiply ang dalawang numero
- `divide(a, b)`: Hatiin ang unang numero sa pangalawa (na may tseke sa zero)
- isPrime(n): Suriin kung ang isang numero ay prime

## Subukan gamit ang Github Copilot Chat sa VS Code

1. Subukang gumawa ng kahilingan sa serbisyo gamit ang MCP protocol. Halimbawa, maaari mong itanong:
   - "Add 5 and 3"
   - "Subtract 10 from 4"
   - "Multiply 6 and 7"
   - "Divide 8 by 2"
   - "Does 37854 prime?"
   - "What are the 3 prime numbers before after 4242?"
2. Upang matiyak na ginagamit nito ang mga tools, idagdag ang #MyCalculator sa prompt. Halimbawa:
   - "Add 5 and 3 #MyCalculator"
   - "Subtract 10 from 4 #MyCalculator


## Containerized na Bersyon

Ang naunang solusyon ay maganda kapag naka-install ang .NET SDK, at ang lahat ng mga dependencies ay nasa lugar na. Gayunpaman, kung nais mong ibahagi ang solusyon o patakbuhin ito sa ibang kapaligiran, maaari mong gamitin ang containerized na bersyon.

1. Simulan ang Docker at tiyaking ito ay tumatakbo.
1. Mula sa terminal, pumunta sa folder na `03-GettingStarted\samples\csharp\src` 
1. Upang buuin ang Docker image para sa calculator service, patakbuhin ang sumusunod na utos (palitan ang `<YOUR-DOCKER-USERNAME>` ng iyong Docker Hub username):
   ```bash
   docker build -t <YOUR-DOCKER-USERNAME>/mcp-calculator .
   ``` 
1. Pagkatapos mabuo ang imahe, i-upload natin ito sa Docker Hub. Patakbuhin ang sumusunod na utos:
   ```bash
   docker push <YOUR-DOCKER-USERNAME>/mcp-calculator
   ```

## Paggamit ng Dockerized na Bersyon

1. Sa `.vscode/mcp.json` file, palitan ang server configuration ng sumusunod:
   ```json
    "mcp-calculator": {
      "command": "docker",
      "args": [
        "run",
        "--rm",
        "-i",
        "<YOUR-DOCKER-USERNAME>/mcp-calculator"
      ],
      "envFile": "",
      "env": {}
    }
   ```
   Sa pagtingin sa konfigurasyon, makikita mo na ang utos ay `docker` at ang mga args ay `run --rm -i <YOUR-DOCKER-USERNAME>/mcp-calculator`. Tinutiyak ng `--rm` na flag na ang container ay matatanggal pagkatapos itong tumigil, at pinapayagan ng `-i` flag na makipag-interact ka sa standard input ng container. Ang huling argumento ay ang pangalan ng imahe na kakabuo lang natin at naipush sa Docker Hub.

## Subukan ang Dockerized na Bersyon

Simulan ang MCP Server sa pamamagitan ng pag-click ng maliit na Start button sa itaas ng `"mcp-calculator": {`, at tulad ng dati, maaari mong utusan ang calculator service na magsagawa ng ilang mga kalkulasyon para sa iyo.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Pagtatanggi**:
Ang dokumentong ito ay isinalin gamit ang serbisyo ng AI translation na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't nagsusumikap kami para sa katumpakan, pakatandaan na ang awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang maling pagkakaintindi o maling interpretasyon na nagmula sa paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->