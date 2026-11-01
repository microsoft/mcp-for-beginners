# Põhikalulaatori MCP-teenus

See teenus pakub põhilisi kalkulaatori toiminguid Model Context Protocoli (MCP) kaudu. See on loodud lihtsaks näiteks alustajatele, kes õpivad MCP-i rakendusi.

Lisainfo saamiseks vaata [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk)

## Omadused

See kalkulaatori teenus pakub järgmisi võimalusi:

1. **Põhilised aritmeetilised toimingud**:
   - Kahe arvu liitmine
   - Ühe arvu lahutamine teisest
   - Kahe arvu korrutamine
   - Ühe arvu jagamine teisega (sisaldab nulliga jagamise kontrolli)

## `stdio` tüübi kasutamine
  
## Konfiguratsioon

1. **MCP-serverite konfigureerimine**:
   - Ava oma tööruum VS Code'is.
   - Loo oma tööruumi kausta `.vscode/mcp.json` fail MCP-serverite konfigureerimiseks. Näide konfiguratsioonist:

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

   - Sult küsitakse GitHubi repoteegi juurkausta, mida saab hankida käsuga `git rev-parse --show-toplevel`.

## Teenuse kasutamine

Teenus pakub MCP-protokolli kaudu järgmisi API lõpp-punkte:

- `add(a, b)`: Liidab kaks arvu
- `subtract(a, b)`: Lahutab teise arvu esimesest
- `multiply(a, b)`: Korrutab kahte arvu
- `divide(a, b)`: Jagab esimese arvu teisega (sisaldab nulliga jagamise kontrolli)
- isPrime(n): Kontrollib, kas arv on algarv

## Testimine GitHub Copilot Chati abil VS Code'is

1. Proovi saata teenusele päring MCP-protokolli kaudu. Näiteks võid küsida:
   - "Liida 5 ja 3"
   - "Lahuta 10 arvust 4"
   - "Korruta 6 ja 7"
   - "Jaga 8 kahega"
   - "Kas 37854 on algarv?"
   - "Millised on 3 algarvu enne ja pärast 4242?"
2. Selleks, et veenduda, et see kasutab tööriistu, lisa promptile #MyCalculator. Näiteks:
   - "Liida 5 ja 3 #MyCalculator"
   - "Lahuta 10 arvust 4 #MyCalculator


## Konteineriseeritud versioon

Eelmine lahendus sobib hästi, kui sul on .NET SDK paigaldatud ja kõik sõltuvused olemas. Kui soovid lahendust jagada või käivitada teises keskkonnas, võid kasutada konteineriseeritud versiooni.

1. Käivita Docker ja veendu, et see töötab.
1. Terminalis liigu kausta `03-GettingStarted\samples\csharp\src` 
1. Docker-pildi ehitamiseks kalkulaatori teenuse jaoks käivita järgmine käsk (asenda `<YOUR-DOCKER-USERNAME>` oma Docker Hubi kasutajanimega):
   ```bash
   docker build -t <YOUR-DOCKER-USERNAME>/mcp-calculator .
   ``` 
1. Pärast pildi ehitamist laadime selle Docker Hubi üles. Käivita järgmine käsk:
   ```bash
   docker push <YOUR-DOCKER-USERNAME>/mcp-calculator
   ```

## Kasuta konteineriseeritud versiooni

1. Failis `.vscode/mcp.json` asenda serveri konfiguratsioon järgmisega:
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
   Vaadates konfiguratsiooni, näed, et käsk on `docker` ja argumendid on `run --rm -i <YOUR-DOCKER-USERNAME>/mcp-calculator`. Lipp `--rm` tagab, et konteiner eemaldatakse pärast peatamist, ja lipp `-i` võimaldab suhelda konteineri standardse sisendiga. Viimane argument on pildi nimi, mille me just ehitasime ja lükkasime Docker Hubi.

## Testi konteineriseeritud versiooni

Käivita MCP-server, klõpsates väikesel Start-nupul üleval `"mcp-calculator": {`, ja nagu varem võid paluda kalkulaatori teenusel teha mõningaid arvutusi.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Lahtiütlus**:
See dokument on tõlgitud kasutades AI tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi me püüdleme täpsuse poole, palun pange tähele, et automatiseeritud tõlgetes võib esineda vigu või ebatäpsusi. Originaaldokument selle emakeeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta selle tõlkega seotud eksimustest või valesti mõistmistest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->