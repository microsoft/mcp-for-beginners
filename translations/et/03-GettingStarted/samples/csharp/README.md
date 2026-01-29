# Põhiline Kalkulaatori MCP Teenus

See teenus pakub põhilisi kalkulaatori funktsioone Model Context Protocoli (MCP) kaudu. See on loodud lihtsa näitena algajatele, kes õpivad MCP rakendusi.

Lisainfo saamiseks vaata [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk)

## Funktsioonid

See kalkulaatori teenus pakub järgmisi võimalusi:

1. **Põhilised aritmeetilised toimingud**:
   - Kahe arvu liitmine
   - Ühe arvu lahutamine teisest
   - Kahe arvu korrutamine
   - Ühe arvu jagamine teisega (nulliga jagamise kontroll)

## `stdio` Tüübi Kasutamine
  
## Konfiguratsioon

1. **MCP serverite seadistamine**:
   - Ava oma tööruum VS Code'is.
   - Loo oma tööruumi kausta `.vscode/mcp.json` fail MCP serverite seadistamiseks. Näidis konfiguratsioon:

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

   - Sinult küsitakse GitHubi repositooriumi juurt, mida saab hankida käsuga `git rev-parse --show-toplevel`.

## Teenuse Kasutamine

Teenus pakub järgmisi API lõpp-punkte MCP protokolli kaudu:

- `add(a, b)`: Kahe arvu liitmine
- `subtract(a, b)`: Teise arvu lahutamine esimesest
- `multiply(a, b)`: Kahe arvu korrutamine
- `divide(a, b)`: Esimese arvu jagamine teisega (nulliga jagamise kontroll)
- isPrime(n): Kontrollib, kas arv on algarv

## Testimine Github Copilot Chatiga VS Code'is

1. Proovi teha päring teenusele MCP protokolli kaudu. Näiteks võid küsida:
   - "Liida 5 ja 3"
   - "Lahuta 10-st 4"
   - "Korruta 6 ja 7"
   - "Jaga 8 kahega"
   - "Kas 37854 on algarv?"
   - "Millised on 3 algarvu enne ja pärast 4242?"
2. Veendumaks, et tööriistu kasutatakse, lisa #MyCalculator päringule. Näiteks:
   - "Liida 5 ja 3 #MyCalculator"
   - "Lahuta 10-st 4 #MyCalculator"

## Konteineriseeritud Versioon

Eelnev lahendus on suurepärane, kui sul on .NET SDK paigaldatud ja kõik sõltuvused olemas. Kui aga soovid lahendust jagada või käivitada seda teises keskkonnas, saad kasutada konteineriseeritud versiooni.

1. Käivita Docker ja veendu, et see töötab.
1. Ava terminal ja liigu kausta `03-GettingStarted\samples\csharp\src`
1. Kalkulaatori teenuse Docker-pildi loomiseks käivita järgmine käsk (asenda `<YOUR-DOCKER-USERNAME>` oma Docker Hubi kasutajanimega):
   ```bash
   docker build -t <YOUR-DOCKER-USERNAME>/mcp-calculator .
   ``` 
1. Pärast pildi loomist laadi see Docker Hubi üles. Käivita järgmine käsk:
   ```bash
    docker push <YOUR-DOCKER-USERNAME>/mcp-calculator
  ```

## Use the Dockerized Version

1. In the `.vscode/mcp.json` file, replace the server configuration by the following:
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
   Konfiguratsiooni vaadates näed, et käsk on `docker` ja argumendid on `run --rm -i <YOUR-DOCKER-USERNAME>/mcp-calc`. `--rm` lipp tagab, et konteiner eemaldatakse pärast selle peatamist, ja `-i` lipp võimaldab suhelda konteineri standardse sisendiga. Viimane argument on pildi nimi, mille me just lõime ja Docker Hubi üles laadisime.

## Dockeriseeritud Versiooni Testimine

Käivita MCP server, klõpsates väikest Start nuppu `"mcp-calc": {` kohal, ja nagu varem, saad kalkulaatori teenuselt küsida matemaatilisi tehteid.

---

**Lahtiütlus**:  
See dokument on tõlgitud AI tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi püüame tagada täpsust, palume arvestada, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algses keeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitame kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valesti tõlgenduste eest.