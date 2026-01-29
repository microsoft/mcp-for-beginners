# Pagrindinė skaičiuoklės MCP paslauga

Ši paslauga teikia pagrindines skaičiuoklės operacijas per Model Context Protocol (MCP). Ji sukurta kaip paprastas pavyzdys pradedantiesiems, norintiems išmokti apie MCP įgyvendinimus.

Daugiau informacijos rasite [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk)

## Funkcijos

Ši skaičiuoklės paslauga siūlo šias galimybes:

1. **Pagrindinės aritmetinės operacijos**:
   - Dviejų skaičių sudėtis
   - Vieno skaičiaus atimtis iš kito
   - Dviejų skaičių daugyba
   - Vieno skaičiaus dalyba iš kito (su nulio dalybos patikra)

## Naudojant `stdio` tipą

## Konfigūracija

1. **Konfigūruokite MCP serverius**:
   - Atidarykite savo darbo aplinką VS Code.
   - Sukurkite `.vscode/mcp.json` failą savo darbo aplanko kataloge, kad sukonfigūruotumėte MCP serverius. Konfigūracijos pavyzdys:

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

   - Jūsų bus paprašyta įvesti GitHub saugyklos šaknį, kurį galima gauti naudojant komandą `git rev-parse --show-toplevel`.

## Paslaugos naudojimas

Paslauga per MCP protokolą teikia šiuos API galinius taškus:

- `add(a, b)`: Sudeda du skaičius
- `subtract(a, b)`: Atima antrą skaičių iš pirmojo
- `multiply(a, b)`: Padaugina du skaičius
- `divide(a, b)`: Padalina pirmą skaičių iš antrojo (su nulio patikra)
- `isPrime(n)`: Patikrina, ar skaičius yra pirminis

## Testavimas su Github Copilot Chat VS Code

1. Pabandykite pateikti užklausą paslaugai naudodami MCP protokolą. Pavyzdžiui, galite klausti:
   - „Sudėk 5 ir 3“
   - „Atimk 10 iš 4“
   - „Padaugink 6 ir 7“
   - „Padalink 8 iš 2“
   - „Ar 37854 yra pirminis?“
   - „Kokie yra 3 pirminiai skaičiai prieš ir po 4242?“
2. Kad įsitikintumėte, jog naudojami įrankiai, pridėkite #MyCalculator prie užklausos. Pavyzdžiui:
   - „Sudėk 5 ir 3 #MyCalculator“
   - „Atimk 10 iš 4 #MyCalculator“

## Konteinerizuota versija

Ankstesnis sprendimas puikiai tinka, kai turite įdiegtą .NET SDK ir visas priklausomybes. Tačiau, jei norite pasidalinti sprendimu arba paleisti jį kitoje aplinkoje, galite naudoti konteinerizuotą versiją.

1. Paleiskite Docker ir įsitikinkite, kad jis veikia.
1. Terminale pereikite į katalogą `03-GettingStarted\samples\csharp\src`
1. Norėdami sukurti Docker vaizdą skaičiuoklės paslaugai, vykdykite šią komandą (pakeiskite `<YOUR-DOCKER-USERNAME>` savo Docker Hub vartotojo vardu):
   ```bash
   docker build -t <YOUR-DOCKER-USERNAME>/mcp-calculator .
   ```
1. Kai vaizdas bus sukurtas, įkelkite jį į Docker Hub. Vykdykite šią komandą:
   ```bash
    docker push <YOUR-DOCKER-USERNAME>/mcp-calculator
  ```

## Naudokite Dockerizuotą versiją

1. `.vscode/mcp.json` faile pakeiskite serverio konfigūraciją į šią:
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
   Žvelgiant į konfigūraciją, matote, kad komanda yra `docker`, o argumentai yra `run --rm -i <YOUR-DOCKER-USERNAME>/mcp-calc`. `--rm` vėliava užtikrina, kad konteineris bus pašalintas po sustojimo, o `-i` vėliava leidžia sąveikauti su konteinerio standartiniu įvesties srautu. Paskutinis argumentas yra vaizdo, kurį ką tik sukūrėme ir įkėlėme į Docker Hub, pavadinimas.

## Dockerizuotos versijos testavimas

Paleiskite MCP serverį paspausdami mažą Start mygtuką virš `"mcp-calc": {`, ir kaip ir anksčiau, galite paprašyti skaičiuoklės paslaugos atlikti matematikos veiksmus.

---

**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojama naudoti profesionalų žmogaus vertimą. Mes neprisiimame atsakomybės už nesusipratimus ar klaidingus interpretavimus, atsiradusius dėl šio vertimo naudojimo.